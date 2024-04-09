const prisma = require("../utils/prisma");
const bcrypt = require("bcrypt");

const RecoveryCode = {
  tablename: "recovery_codes",
  writable: [],
  create: async function (userId, code) {
    try {
      const codeHash = await bcrypt.hash(code, 10);
      const recoveryCode = await prisma.recovery_codes.create({
        data: { user_id: userId, code_hash: codeHash },
      });
      return { recoveryCode, error: null };
    } catch (error) {
      console.error("FAILED TO CREATE RECOVERY CODE.", error.message);
      return { recoveryCode: null, error: error.message };
    }
  },
  createMany: async function (data) {
    try {
      const recoveryCodes = await prisma.recovery_codes.createMany({ data });
      return { recoveryCodes, error: null };
    } catch (error) {
      console.error("FAILED TO CREATE RECOVERY CODES.", error.message);
      return { recoveryCodes: null, error: error.message };
    }
  },
  findFirst: async function (clause = {}) {
    try {
      const recoveryCode = await prisma.recovery_codes.findFirst({
        where: clause,
      });
      return recoveryCode;
    } catch (error) {
      console.error("FAILED TO FIND RECOVERY CODE.", error.message);
      return null;
    }
  },
  deleteMany: async function (clause = {}) {
    try {
      await prisma.recovery_codes.deleteMany({ where: clause });
      return true;
    } catch (error) {
      console.error("FAILED TO DELETE RECOVERY CODES.", error.message);
      return false;
    }
  },
};

const PasswordResetToken = {
  tablename: "password_reset_tokens",
  writable: [],
  create: async function (userId, token, expiresAt) {
    try {
      const passwordResetToken = await prisma.password_reset_tokens.create({
        data: { user_id: userId, token, expiresAt },
      });
      return { passwordResetToken, error: null };
    } catch (error) {
      console.error("FAILED TO CREATE PASSWORD RESET TOKEN.", error.message);
      return { passwordResetToken: null, error: error.message };
    }
  },
  findUnique: async function (clause = {}) {
    try {
      const passwordResetToken = await prisma.password_reset_tokens.findUnique({
        where: clause,
      });
      return passwordResetToken;
    } catch (error) {
      console.error("FAILED TO FIND PASSWORD RESET TOKEN.", error.message);
      return null;
    }
  },
  delete: async function (clause = {}) {
    try {
      await prisma.password_reset_tokens.delete({ where: clause });
      return true;
    } catch (error) {
      console.error("FAILED TO DELETE PASSWORD RESET TOKEN.", error.message);
      return false;
    }
  },
};

module.exports = { RecoveryCode, PasswordResetToken };

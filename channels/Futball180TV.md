<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn5.telesco.pe/file/Acj64csvQBsys5TPezw2zR-1z6Ym67dejw6csrfrtdSTkL7LbKVLqLJHbhB_d76-q3469NcD4dmozNsvAPcFuAQFsn7a4QR3MJ0AzSiN-QMms3scuE5hAliNPkV2YmObXk-x2cfK8XONgm2X7k4UxdezN7ChkXL8D81YTDMA1sVRcT3uBnzqhLLXrzTszt5EhJ5-vbQ5XTg7GLSP5sUAWrVIWBG1lXZH7yByewbtmWAdwRPnAFNq56eb-YOxNAWAWar2MRisVK1KhYpeKS9Biz0L0kvmmXKwj1m8gD2uUxbVX4nresCXBGerj29azs6Na55TBNu5J9FxYR4FtniLSw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 386K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-18 16:17:25</div>
<hr>

<div class="tg-post" id="msg-108252">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13447d981f.mp4?token=OsjYncW09tVi5hTgDQqjTi57OSIYZqoNgZ48V13E6Vaws8mANLF7ha4Rw-Cd8aA6VcCCheGrJWV2D1bD9vjVF4sPeApQm23XNL145TRNtceuZ8wzJmTp71Yq9FT2KArO-i_erBlQvGlMreVkBSg57Xd8PbL0_HriwUQ0iyH75PVNZObOMzmj3Px76pM_67Cw9mD-TAFuZFxtC97ct4v9O2m6cq_dj_SICRFgM41gD6cYbp2JiiT7WhLceqqHbNvrxdJqr2DrOJwyAa8khXsYuu99vWuAta4dsiVZ8HBHzMHotuopnEuLjGupNWWQ2QdP_zazVjejWSTlVCOGl_5eEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13447d981f.mp4?token=OsjYncW09tVi5hTgDQqjTi57OSIYZqoNgZ48V13E6Vaws8mANLF7ha4Rw-Cd8aA6VcCCheGrJWV2D1bD9vjVF4sPeApQm23XNL145TRNtceuZ8wzJmTp71Yq9FT2KArO-i_erBlQvGlMreVkBSg57Xd8PbL0_HriwUQ0iyH75PVNZObOMzmj3Px76pM_67Cw9mD-TAFuZFxtC97ct4v9O2m6cq_dj_SICRFgM41gD6cYbp2JiiT7WhLceqqHbNvrxdJqr2DrOJwyAa8khXsYuu99vWuAta4dsiVZ8HBHzMHotuopnEuLjGupNWWQ2QdP_zazVjejWSTlVCOGl_5eEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل اول لیدزیونایتد یونایتد به آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/Futball180TV/108252" target="_blank">📅 16:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108251">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYVpmeYv1gjQUShnpsYMHnn1bgq_lnOV6I6JitP4xkRRWbTngowsz7qbRz87WDaeeLdpMSW_IKLrgLDoUwSf0L5Gcn3fGklTNsfH9FidQS34fzo1s-RoxSMmH-fqkPFLD9BB4YbmnrKFWjUt0odmHs_1VXuAyToJjxSQJThIQeKJ1cmMK_lZGi7JGQ440xwuSBPBxza9DOhEEciEXskU5_eHL6mtb--XheILMN0ST6SpQcrjwGLiqjqaq9D3q9v8mOM_JtmelMfiXjUYOUY-hpN5_7dSMPhl-X37IU0TpL8ZBvgYVXa7C9C4iinB_MItFP_8M5mzEh_e0wIqUsY3SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
در فاصله دو روز مانده به بازی استقلال و الغرافه قطر، هواداران پرسپولیس درحال کامنت گذاری زیر پیج این تیم قطری درباره یاسر‌آسانی هستند. این درحالیست که آسانی بدلیل مصدومیت مقابل الغرافه به میدان نخواهد رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/Futball180TV/108251" target="_blank">📅 16:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108250">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5lTCisoILdU4sSbpn3qGXR0wcisKc7ObhVDlDQ_Mnh5ccx0zBzBmPOY3pcI-vDbEGt3FrL_YKlfCDCyubkTWpETME48tGk-2ShbOQ2KnN231ur_srYTR7P1J-N5ICKe2UqsdvRZJ8hGz5d0OCOxd_gAE88alnLqy5DR9xtislfD-hziAQjW8Z3OHVPvTgisOor8HtYA-Vh79e57apeLkBkIhIUThJVDY9g2KzFyI3-CafU-f4UQxVEFnlWtlQeur0CpxTzL97IZcorIO6y6bRUD9FNOEYTtf1iKpH5Q31XwxImhUKkI3IGXKGLGybCGbAM7I4yU9aGQSxYXLYsd5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇩🇪
شماتیک ترکیب بایرن‌مونیخ مقابل آکزبورگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/Futball180TV/108250" target="_blank">📅 16:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108249">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85108132e1.mp4?token=EOsViv1oDj39Dw4WEnuGUQKoHdAzMGPt94N2ZRM6V8hIKShqYraqlXBRMpCycUCO3ec2k0CtaE2y8v8sM8IEnuZwXvdtxmrgC5K4vPy-WKdN-OJTYnOyDTm-5jAVeKU52kyyUlFG33sXfmTiiqTwHjzrDPi2x6UQeRpg-7Jz-wWoQFIe_MbFcxECylY8X2IJbq9PgPmOK3EQ6_H0sI6K3xA-zrZXF_pBuFISSTp0C9wypx_wM_X5lKNcANhBU-fvWyXMWJ8kLeSByV3G09x9kn_W2v9Kxpi05rCxh3Wz8TP40A-h6jYtDJ5FJti8e0BIW6kXovHkjltV0aya_FmkMGxiRqdCObvHKRhYOlqQycoJASBCHYqiaco8VeiIfDMlqNBKkxu4jLvFlRg3k0MP8YrSh4PDBW5735nxgGncr08VQ-T-32RLTurCXOEP-C73wgQFDZa2_VObhx5V0TuGFNOgyfxHo8sAMWD4UJXBcZsf4fMzfKKr4CLwrmlZBSO7SOJWVp9sP6jR-oGpjjrImh8R-aCAV4tElQcvs68KN9snP9VTiSZg1NI-1g01jK5VCgc9_oXO2AhlB1xY05m3LdolvF1soyBccgQnDHODJcRytGhoA50ngx2HKVYu6ICimD4gXmrwgwCQUd_aWs3IV1X19fcW8XgyYr0-qg3jhAo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85108132e1.mp4?token=EOsViv1oDj39Dw4WEnuGUQKoHdAzMGPt94N2ZRM6V8hIKShqYraqlXBRMpCycUCO3ec2k0CtaE2y8v8sM8IEnuZwXvdtxmrgC5K4vPy-WKdN-OJTYnOyDTm-5jAVeKU52kyyUlFG33sXfmTiiqTwHjzrDPi2x6UQeRpg-7Jz-wWoQFIe_MbFcxECylY8X2IJbq9PgPmOK3EQ6_H0sI6K3xA-zrZXF_pBuFISSTp0C9wypx_wM_X5lKNcANhBU-fvWyXMWJ8kLeSByV3G09x9kn_W2v9Kxpi05rCxh3Wz8TP40A-h6jYtDJ5FJti8e0BIW6kXovHkjltV0aya_FmkMGxiRqdCObvHKRhYOlqQycoJASBCHYqiaco8VeiIfDMlqNBKkxu4jLvFlRg3k0MP8YrSh4PDBW5735nxgGncr08VQ-T-32RLTurCXOEP-C73wgQFDZa2_VObhx5V0TuGFNOgyfxHo8sAMWD4UJXBcZsf4fMzfKKr4CLwrmlZBSO7SOJWVp9sP6jR-oGpjjrImh8R-aCAV4tElQcvs68KN9snP9VTiSZg1NI-1g01jK5VCgc9_oXO2AhlB1xY05m3LdolvF1soyBccgQnDHODJcRytGhoA50ngx2HKVYu6ICimD4gXmrwgwCQUd_aWs3IV1X19fcW8XgyYr0-qg3jhAo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
ماجرای خرید تراکتور توسط زنوزی به زبان نماینده مجلس سابق(عای هیمتی)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/Futball180TV/108249" target="_blank">📅 16:05 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108248">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yg1hE2XiHD3SNcUT_6702q7cymjxmwRvpGOvDpr0UYExxehQrKz5OYSYBmzTUJ_LI-WpciUjK8_PoDus7v7gBrAfVsyP4yQRdZsOMpXcvPX4fXh56xjhgyWzgvHLXwWB7Ew7Ii7H2XMw4tdSDqNDhgjw0KKePiypr_eiko5fFusavMelmPY1MRhy-3Y-Zc6iRuA7nyj7QlnfHwznPLvhKLEftQ2EQ0oijkphPbQV7aCEcPJlb-eev9r0Wee4YMnNEQi_fs-79lvX72AuRlmByPcCl6OIGub1CZ4VOBmMsBGahvk67MCkj-P_Jtg38CZr9p_rSBp7giKmtO4aQU__og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
😳
مصطفی میرسلیم، عضو کسخل مجمع تشخیص مصلحت نظام: تیبا با خودروهای خارجی قابلیت رقابت دارد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/Futball180TV/108248" target="_blank">📅 15:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108247">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d024a83d11.mp4?token=XkseNjrgGEGt7yCz2ZYemwYthbYvnK9f8nR--IQirY786aDPcZV7zz6U6A8yxPk37b0qCC_adcbSbkz9vww0kBy2vcgATsKF1V-tPDk-nCGqJ7cQM_iAcw78JwG8uLf2aLA8DcYWDwBjQKix29RQfyLzejph03fhy_DfTlwbNAmVY_4e7BEqXTtM2EP3Bxef1nOx4s-4scLBT5b2uPlqzabWoTBpjyg7nNV0dCpVqm3G89Hyvuv3Y8ABdlM813ApCz73ycdwnC7na7XvO9TgmMFnRJ_YRmY8h5J7Xey2xCtvQ7evd4fkxfb61hYq1D-0ivS35FjOFfjlJDoJvt0EspOdkXYsCgijnr9nygtE4wjTg3am6vsmRLfclKRrtCAHuihbuouRP7x9kaudmr6ZirMmKs2YA0A-YaZjGJZp0IoWsvDy0RFrBpbpoy5BctnRsKBjK64P0hiCYy0HjNZeNXq3BskLwJPxHfpYsnrmbnLrNzZCR2k0Pl7zFYvPifHfraTFGGrlPGFDYeakfTFYbjTDEsTEeOLSpeZW_8veggGTuf9L5HZt5mw99svu2ADQhAcEluAI0Cm7n6zJ9l0UhdXGQu_62mLu9z5DtBeq8uhNr4XeoJzBJd7pVjgCnAg4Fe9dsXJBCuYpbqIxGpRupwWpg9o0AG7GvJ16vZjCpgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d024a83d11.mp4?token=XkseNjrgGEGt7yCz2ZYemwYthbYvnK9f8nR--IQirY786aDPcZV7zz6U6A8yxPk37b0qCC_adcbSbkz9vww0kBy2vcgATsKF1V-tPDk-nCGqJ7cQM_iAcw78JwG8uLf2aLA8DcYWDwBjQKix29RQfyLzejph03fhy_DfTlwbNAmVY_4e7BEqXTtM2EP3Bxef1nOx4s-4scLBT5b2uPlqzabWoTBpjyg7nNV0dCpVqm3G89Hyvuv3Y8ABdlM813ApCz73ycdwnC7na7XvO9TgmMFnRJ_YRmY8h5J7Xey2xCtvQ7evd4fkxfb61hYq1D-0ivS35FjOFfjlJDoJvt0EspOdkXYsCgijnr9nygtE4wjTg3am6vsmRLfclKRrtCAHuihbuouRP7x9kaudmr6ZirMmKs2YA0A-YaZjGJZp0IoWsvDy0RFrBpbpoy5BctnRsKBjK64P0hiCYy0HjNZeNXq3BskLwJPxHfpYsnrmbnLrNzZCR2k0Pl7zFYvPifHfraTFGGrlPGFDYeakfTFYbjTDEsTEeOLSpeZW_8veggGTuf9L5HZt5mw99svu2ADQhAcEluAI0Cm7n6zJ9l0UhdXGQu_62mLu9z5DtBeq8uhNr4XeoJzBJd7pVjgCnAg4Fe9dsXJBCuYpbqIxGpRupwWpg9o0AG7GvJ16vZjCpgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
🚨
‼️
عزیزی در فرودگاه بغداد: فقط ۲ تا سگ دنبال مهدی شیری و اعضای تیم افتاده بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/Futball180TV/108247" target="_blank">📅 15:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108246">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1ba40b7cc.mp4?token=sOduAAGBsB94-jejbFQCxwMnQZReXNfOksSig1xrLCxK0_E_Z64sCsBHuP6uyRVFDf4rfBd71PpKyTXTBTa490y1nbo31lqt69k2Qnueg_sJGGMHFm_cSxULCo4DvoM81NXnbdiGRTe9_zqlsDzMMGR7gRuYuDQ9zBDR0P18XoBD3tQDf_k7Cgg87HuIFpEDk5LszGEbmGuArB1s_ussgEHFoLDuG_Zld4XeW5bYjmkFTEigUdz4_ZQbrPiqRN1mmNOlvCuaMC-l3XmWNReNzasjFnepq_O5bBhp3bdoAlMkAbc77vgGH68pWFZivJcedqnwX5YuE0Ho9yr2JR6gCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1ba40b7cc.mp4?token=sOduAAGBsB94-jejbFQCxwMnQZReXNfOksSig1xrLCxK0_E_Z64sCsBHuP6uyRVFDf4rfBd71PpKyTXTBTa490y1nbo31lqt69k2Qnueg_sJGGMHFm_cSxULCo4DvoM81NXnbdiGRTe9_zqlsDzMMGR7gRuYuDQ9zBDR0P18XoBD3tQDf_k7Cgg87HuIFpEDk5LszGEbmGuArB1s_ussgEHFoLDuG_Zld4XeW5bYjmkFTEigUdz4_ZQbrPiqRN1mmNOlvCuaMC-l3XmWNReNzasjFnepq_O5bBhp3bdoAlMkAbc77vgGH68pWFZivJcedqnwX5YuE0Ho9yr2JR6gCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد مدت‌ها فردوسی پور و میثاقی رودرو شدن
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/Futball180TV/108246" target="_blank">📅 15:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108245">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a5e7db4ee.mp4?token=K-zbQzXkdyCQozFreW3KdQImEgqABSqJmCJ8UpTjarllveX91I0UYgaJ8aYPCEuhXjXh4GqRR15FPMJl7CqJMNIxVoVS4ezXjR-AOlpjNMsCE8L8iRHNs29fs01YKknYfoooPnlb4x04EROBFN0LEeOdwnHFJZa1U645hPevKsH9pezF_1gnIOp0KOJEcB7xM6cS5QqHN-i07zoWU_qmyc2Yfab9UWEOqLiXWSDquN_pc4pIYZiWGurUUXD3I9yreA4yfC5-uA91fLfmZEEwMXfPaAhOnS_epQcYHHCfFO-O99FvWH60t6OYs-criqjHtT3WAnKYbTUdNuD0hDtRBSRpxJrKmXJXIL_Wjp5tJLBoIpvWr1o3WkFBm165eVs4iRPALbfpblMFhKB7_osnVPvGzWGELNw6Q3Uwy4Xs7WISrmV4z16JXJIAriQgAhM6IP0Ipbe6E1K4BcMcxp9HxX8XVr1m6jaOgbS3O2LB265LCU2DKmDIMlQeuqPHsewvsczeFGYdlJE3NUokJmh1jJQA4nZmx7jLqsU33P98n-RoPJrM_ufXdemE3_u1Ut4rQ49xNEw0Mpy_TCyoyn5yWOl6SQ85-xIMRrXKhY1IpVMQ1LcmV9p46bv9DgZxxikNGClDr6KijdOCKF1tOygVkH4WUH2pD86ybMr4iVXM7aE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a5e7db4ee.mp4?token=K-zbQzXkdyCQozFreW3KdQImEgqABSqJmCJ8UpTjarllveX91I0UYgaJ8aYPCEuhXjXh4GqRR15FPMJl7CqJMNIxVoVS4ezXjR-AOlpjNMsCE8L8iRHNs29fs01YKknYfoooPnlb4x04EROBFN0LEeOdwnHFJZa1U645hPevKsH9pezF_1gnIOp0KOJEcB7xM6cS5QqHN-i07zoWU_qmyc2Yfab9UWEOqLiXWSDquN_pc4pIYZiWGurUUXD3I9yreA4yfC5-uA91fLfmZEEwMXfPaAhOnS_epQcYHHCfFO-O99FvWH60t6OYs-criqjHtT3WAnKYbTUdNuD0hDtRBSRpxJrKmXJXIL_Wjp5tJLBoIpvWr1o3WkFBm165eVs4iRPALbfpblMFhKB7_osnVPvGzWGELNw6Q3Uwy4Xs7WISrmV4z16JXJIAriQgAhM6IP0Ipbe6E1K4BcMcxp9HxX8XVr1m6jaOgbS3O2LB265LCU2DKmDIMlQeuqPHsewvsczeFGYdlJE3NUokJmh1jJQA4nZmx7jLqsU33P98n-RoPJrM_ufXdemE3_u1Ut4rQ49xNEw0Mpy_TCyoyn5yWOl6SQ85-xIMRrXKhY1IpVMQ1LcmV9p46bv9DgZxxikNGClDr6KijdOCKF1tOygVkH4WUH2pD86ybMr4iVXM7aE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🇮🇷
آنالیز ساختار دفاعی استقلال در این‌فصل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/Futball180TV/108245" target="_blank">📅 14:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108244">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bed940014.mp4?token=UlGpL8jN4KllYf-ta2qQKFnS_ii2GQNGDF-BiJtWW39fJ29ECqdBJmWc4zYx-eaNuaWDmaM9pziOx0k1bU75LoEZLo5qMv3FctqOCm2gThPy5Xzac4tPMFkAhjjDabCc6_l7VF0AP7hGlqysZomXIW-5r1AvkwEk2qAhExNVuEKNcN3BBmFbT_QrYbrUqUToeZW3C3_6DZJEPlR0eRgdafe9mnSdp4vz0QNuCkKSea5hnYmYTHTpwT_RzwMKSU40a6kUd5ZrGjrYou_HvwqdwSLe_BJxyIrvUGCn9EcH5RAkrw9zaftMuFuIUu1ShVEcWSeiU2RVWDGKL8ORHGHIm7CsmiNLXPfGm0VUpISe4XE96jnGdaRmTK1AMsntuxa7y8bpolmRet46nm3KegXp0b1uRhu5mrSXax8okrJZWPwlocjBZCwrH6qbQsmsV8WXRe86S7TMQABfSF-POgShwtyfcfDgMvqu161CdRT_AqsutegpQ24Chma2L3oodfjM1J8bcOGuCF5hucLW5FtzFjw891Qeu-rh6FAYfY52X7D4_FivOllON_CzIJsqubeIsr6mD_qsyBwtMzHvQVqVpwwaRfhcidPI77LLY3Ko3yeptrg-RzSa66Tuyt5IzARpTLkv72jNcSlM1lISO0PGXr1KuKc8req9g2SOmq992tI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bed940014.mp4?token=UlGpL8jN4KllYf-ta2qQKFnS_ii2GQNGDF-BiJtWW39fJ29ECqdBJmWc4zYx-eaNuaWDmaM9pziOx0k1bU75LoEZLo5qMv3FctqOCm2gThPy5Xzac4tPMFkAhjjDabCc6_l7VF0AP7hGlqysZomXIW-5r1AvkwEk2qAhExNVuEKNcN3BBmFbT_QrYbrUqUToeZW3C3_6DZJEPlR0eRgdafe9mnSdp4vz0QNuCkKSea5hnYmYTHTpwT_RzwMKSU40a6kUd5ZrGjrYou_HvwqdwSLe_BJxyIrvUGCn9EcH5RAkrw9zaftMuFuIUu1ShVEcWSeiU2RVWDGKL8ORHGHIm7CsmiNLXPfGm0VUpISe4XE96jnGdaRmTK1AMsntuxa7y8bpolmRet46nm3KegXp0b1uRhu5mrSXax8okrJZWPwlocjBZCwrH6qbQsmsV8WXRe86S7TMQABfSF-POgShwtyfcfDgMvqu161CdRT_AqsutegpQ24Chma2L3oodfjM1J8bcOGuCF5hucLW5FtzFjw891Qeu-rh6FAYfY52X7D4_FivOllON_CzIJsqubeIsr6mD_qsyBwtMzHvQVqVpwwaRfhcidPI77LLY3Ko3yeptrg-RzSa66Tuyt5IzARpTLkv72jNcSlM1lISO0PGXr1KuKc8req9g2SOmq992tI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
🇮🇷
على تاجرنيا رئیس هیئت‌مدیره استقلال: از فحاشى هواداران به مادرم خيلى ناراحتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/Futball180TV/108244" target="_blank">📅 14:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108243">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/879a0a76f5.mp4?token=Ef_4vxtK_t77cRPGc70ahM6QW_fHy8FXerIozjpCxq1gZbAo-SUmMGQ5Vgre5NumgYck2-EVE2XGYuRegssbUyYor03-7pRW21orN2w8MjIgFbLF8bMqqkkVwWttBqfznv3eae1oVzAh5pHzEZYUGFN3C8mrLAyFLPIkRPYqEnH-lznd6vH8VVYG8Ozu0ZRcemSUjbcZcHhwJgqNTA7JRcgvTYzznVvWdTT-_GW9HHb2BtjjJswQI72z-IvBgqXTjIfCyidQsZXg4OPj1DGlJ_GTF5oklccLhc3TWWACx_-Kdj1U5I3rFwsJYQPlN1I8lCQYGFPSmx0SvJH9D1o5Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/879a0a76f5.mp4?token=Ef_4vxtK_t77cRPGc70ahM6QW_fHy8FXerIozjpCxq1gZbAo-SUmMGQ5Vgre5NumgYck2-EVE2XGYuRegssbUyYor03-7pRW21orN2w8MjIgFbLF8bMqqkkVwWttBqfznv3eae1oVzAh5pHzEZYUGFN3C8mrLAyFLPIkRPYqEnH-lznd6vH8VVYG8Ozu0ZRcemSUjbcZcHhwJgqNTA7JRcgvTYzznVvWdTT-_GW9HHb2BtjjJswQI72z-IvBgqXTjIfCyidQsZXg4OPj1DGlJ_GTF5oklccLhc3TWWACx_-Kdj1U5I3rFwsJYQPlN1I8lCQYGFPSmx0SvJH9D1o5Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برادر چالش را پر قدرت ادامه می‌دهد
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/108243" target="_blank">📅 14:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108242">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_wa1-6sLqhecWP60HgU2STdpcg7BUQ_lfXtpcJiyzEYLoDGy61yAvzjXrv0JXeyjDIlG5-jpPXLpdHaCrQWB8K37DRZY-xXZh1qYnl8s-HapbYmA7p_-9YgxCN4P7p75GygJAFodYUIBeI4afccd8mvZn0xih139nEj4cyVR1-fiBp3VZCWSbZiDEKW5XQiQSwi1L8W09SPWrEPRgzf9jZG-YtqQL1b61R8HldWDHml7lEi8ZEXUJnYcGMJ23B9Zw137D-Hl24ORSzeZYGvFM3MWQENBUab5fh6mWGkiah3JkOV_2U05QOTpG8Yy3neMeJ5LY-AWCuyFvOno60Iqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
لیست بارسلونا برای بازی با ختافه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/Futball180TV/108242" target="_blank">📅 13:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108241">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgU__yV3Aeyx0pmjERFpvqEcyJu9wsmRTebnW9Tp3jo4-wrnq3LmZL0uAHndQVx8a7TaQKQDm9iD5kIj-9qkZ47bcz3GF1Z0bh5oSQw8ACsGVdfQCZAqPrLZ45cccbbcbtPus6MSo4zCA688re_kn7Wtpagi0Di_80ZtoZKMP5sKUAfcMd7eELiote5adPHeyFo5AmwOVwQQ-cwn5uTcRTq6kMJ6ymnlaw-QdLSciN6e_EyYJon7ACIXycmgcg4JAKgUz9E8ZEM5a3bujPpeWmrMK_nIn_bFCjPYTnpLCUDDShV919XHXLWMVoNU8zc2PWftqcy5YPyIkkO3uPISug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب آرسنال برای بازی مقابل لیدز؛ ساعت ۱۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/Futball180TV/108241" target="_blank">📅 13:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108240">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kM5VkCswOz3TQqZ-jEzqaPf4fV9dYYpAO_jq_wBGf-O7qd-IBmEbRimFlessvAx3lAUdzc_J6MUJFKI71nw4gjWU0JlJtnAdFjpIIVTA5sSZ9NJTDykQ5-SGptTsZHxPxFHNXfJgmhMOVQKZtBDexQOGEs5ZCkwn8vFtRJYbg5sGuD6Si-cRwL04ApEQL-6vk2OWPxA7EYUpNSVAKKyK0KMJaHqdnejqZRlgEPy1DgAOGUCr90BXH0BWyviN8UbGZ-jIE04YR7LBznkSk4-43KDINU3Z16lpFF6OMSF92_abhLIzXyYzwhOagFDIHxEJj228aFeQHh5vcXz4SwrntQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚔️
🔥
بازی‌های باشگاهی بالاخره برگشتن و قراره طی ۴۸ ساعت آینده این بازی‌هارو داشته باشیم:
😍
🇪🇸
بارسلونا
🆚
ختافه
🇪🇸
🇪🇸
رئال‌مادرید
🆚
ویارئال
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستریونایتد
🆚
تاتنهام
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپول
🆚
منچسترسیتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/Futball180TV/108240" target="_blank">📅 13:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108239">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90ee39992.mp4?token=k7iVvouLNlgKaIoRwcoFD_1i5dgtUH6IedZk3lA0io3J0aL978CR4E5NlRRp5-3Q_w5C-Gm3-bMAUbVOeFoyaZ7AklQpAbVTifQqVSAg5asmGbgdmd67LhRWwMoMLad4HX3nWf-6nojTM0tPG7MXRFeJaZ7OgPDtC0qT1r1u1-Tdu5HSqXqrwIkfXj2my5QPNc3g-NKQEmnEkRO4RHwqLNoI71F4hSx55rjYwoRUwhBOJ8k4lom_amHV6XHXzWbZbK1AYrIdr1KlpicroXmsy4IkQqjY2kTJon8fv1w2SDGy_UNzHG_EXndm1Z-0yEgX1eVpsfjx2lcLLHhjhh99sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90ee39992.mp4?token=k7iVvouLNlgKaIoRwcoFD_1i5dgtUH6IedZk3lA0io3J0aL978CR4E5NlRRp5-3Q_w5C-Gm3-bMAUbVOeFoyaZ7AklQpAbVTifQqVSAg5asmGbgdmd67LhRWwMoMLad4HX3nWf-6nojTM0tPG7MXRFeJaZ7OgPDtC0qT1r1u1-Tdu5HSqXqrwIkfXj2my5QPNc3g-NKQEmnEkRO4RHwqLNoI71F4hSx55rjYwoRUwhBOJ8k4lom_amHV6XHXzWbZbK1AYrIdr1KlpicroXmsy4IkQqjY2kTJon8fv1w2SDGy_UNzHG_EXndm1Z-0yEgX1eVpsfjx2lcLLHhjhh99sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
باهنر: ایرانی که صداوسیما نشان می‌دهد کجاست که ما به آن پناهنده شویم؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/Futball180TV/108239" target="_blank">📅 13:35 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108238">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qjt7DMVWWMqPPf-Hl7nYWVqnEbF29iy_80hFE0WwLaLVHZ3_hQnwD_6HOPUSEsHeOdFSXdGXZkGRkZOLzD6bqTYnfx8cZGALLzaL3_oDYyECzJMwuUWxaR2VRVoWPVGhGOlR4ck5LG5YDGyJMppcxUq3XDC1NFUhrVkvZot6Qn-D90vLq7z2DRJMo18RZh43ltF-awRnHdbCELp3r3QaVWaf7BAZm1MPiRUU4Wnxh6yOVNIc7aWBOiT3eKBaHmiNdy8p1IP34JhK20R_ERB_6gqo6t2KuyJzOfzBYmPMELS9uuj2hTRPiJtZZ1Yy8djeWAYUSDh6V2FDYEd45iFpnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
قرارداد کول‌پالمر با چلسی تا سال 2034 میلادی تمدید شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/Futball180TV/108238" target="_blank">📅 13:24 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108237">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3554e4463e.mp4?token=Hetej7uGJA_QNuEULAHiqEJmgHW5WPxRDFGlmpWqToIe4iOdaBvvTW3kkgk1sh44OuhA2QfAioH0H744RUEdGdTv1cxYx5dc4khs5xBCJ5vLWh3ortPioLC6qbg84j4p7Eoz0USG4IIR2FUh0VSIktT6V9acI60O-ky5FtEoZILnBj1flw1POs_ziHOwFon1dbveoVssn6D8HqkyuIqTsBrZrq22lgAllxJzg9Ohow4D62X3iu7A6v5N2qMr8maqKv75Dmq6pnIViBwLrsQUv5ZSC2pNxi0Fjl0JMhc-vukZBH83R1vOdqWhdY19fwqG-Ra1gq4Z_23_gZ5MzvZdeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3554e4463e.mp4?token=Hetej7uGJA_QNuEULAHiqEJmgHW5WPxRDFGlmpWqToIe4iOdaBvvTW3kkgk1sh44OuhA2QfAioH0H744RUEdGdTv1cxYx5dc4khs5xBCJ5vLWh3ortPioLC6qbg84j4p7Eoz0USG4IIR2FUh0VSIktT6V9acI60O-ky5FtEoZILnBj1flw1POs_ziHOwFon1dbveoVssn6D8HqkyuIqTsBrZrq22lgAllxJzg9Ohow4D62X3iu7A6v5N2qMr8maqKv75Dmq6pnIViBwLrsQUv5ZSC2pNxi0Fjl0JMhc-vukZBH83R1vOdqWhdY19fwqG-Ra1gq4Z_23_gZ5MzvZdeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله جدید هادی‌چوپان به منتقدانش در ایران!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/108237" target="_blank">📅 13:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108236">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62f9b3658c.mp4?token=TFWJrSXdKn7bEIRNSjboqrk2t1lPTw2ipalbm32M0hoMp03TMQGxnfQ-I9H6WszLOcvVKzrUSVqGVMZUXKY-VKZmrHJZhtbZNcLOnJZ8lpLd2gvjpJnpKNcd8qr9-dP0bQcjJlIyQG9E7WaFF9t92Lro7oLU2V_UXK904yYB20qI2-1bpxKgW98w4MoYfvp1h0C5QVfhQ0-MtDC1-y-THGIVNCq74xcHiDlEPAsizPE10CiKgFbC8GFnTI6dCVIOYixNZhzMu82hPM_HeKi1dgSfACkYkJCCRW4-2wFMNBdLxSn-6Jk5jD7d2Q3NPQmiXWBK1mtD6PENW58wkSE8gZDixHnY5OmLmitR9eMcWRFHmI74-tan2brYYIa0tcT6ZUgRnh_tAvb0Zm_8O1ExxBpVKsEEEczJCKp_XlEh-0UMio3jOFwNbRRRK5Ghn-M7lRdsue-MF9Uu4SfZVkpSr4QpIWYrUReDXh3Ti16J8QnDDZtrMx0eyExZFGfw-ByY-bPQs-hbAMyfUov7sBBO-b9KDyRMROJmiA0qMw6v-K143oBwhA0yuOacl5g7OqvrbUV8hX68htigQjDaukSU6yRHgj53dxON0UTvlOahJGaHekIboxud8CN-p1z0O3rxoxH2rlmr28rHdvs8AwZJn6j8bdTHU1i-NXk3W3hyZxs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62f9b3658c.mp4?token=TFWJrSXdKn7bEIRNSjboqrk2t1lPTw2ipalbm32M0hoMp03TMQGxnfQ-I9H6WszLOcvVKzrUSVqGVMZUXKY-VKZmrHJZhtbZNcLOnJZ8lpLd2gvjpJnpKNcd8qr9-dP0bQcjJlIyQG9E7WaFF9t92Lro7oLU2V_UXK904yYB20qI2-1bpxKgW98w4MoYfvp1h0C5QVfhQ0-MtDC1-y-THGIVNCq74xcHiDlEPAsizPE10CiKgFbC8GFnTI6dCVIOYixNZhzMu82hPM_HeKi1dgSfACkYkJCCRW4-2wFMNBdLxSn-6Jk5jD7d2Q3NPQmiXWBK1mtD6PENW58wkSE8gZDixHnY5OmLmitR9eMcWRFHmI74-tan2brYYIa0tcT6ZUgRnh_tAvb0Zm_8O1ExxBpVKsEEEczJCKp_XlEh-0UMio3jOFwNbRRRK5Ghn-M7lRdsue-MF9Uu4SfZVkpSr4QpIWYrUReDXh3Ti16J8QnDDZtrMx0eyExZFGfw-ByY-bPQs-hbAMyfUov7sBBO-b9KDyRMROJmiA0qMw6v-K143oBwhA0yuOacl5g7OqvrbUV8hX68htigQjDaukSU6yRHgj53dxON0UTvlOahJGaHekIboxud8CN-p1z0O3rxoxH2rlmr28rHdvs8AwZJn6j8bdTHU1i-NXk3W3hyZxs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🇪🇸
آنالیز دیدنی از سبک پرس فوق‌العاده بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/108236" target="_blank">📅 12:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108235">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ae47b4ef9.mp4?token=ZXjkMM3JfHdSjjsj1wYrmHdQhuWEEXwwwx71ircAQhWjLpsTA7fo7E4CcGR_soi-sEB41UNqJjHgSidjXmXA7ZUjhzNOdRJLEQSBGQ8DACLQZTo4UcXIgnH2zEq-vqpU4ModXGvsdtWj9Hyx0pNOLZpBgnlt4bg28RqsyrWtW-jC7DtSRBPjWkbysqMyfOkYXyBWmcaWhRyInhr-t4BwA1doaT_2SCJD_3dfH3FJ_wgVs29JimQDj0NSBrqixCLc_-KWo7KQJAdO0uhXKC7U1nMAkg0Hhgl8hpkfXev_KxapbwVTbeH7Otx6TBzY7fhGr7CJmFOdrUelvXLfg1FJXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ae47b4ef9.mp4?token=ZXjkMM3JfHdSjjsj1wYrmHdQhuWEEXwwwx71ircAQhWjLpsTA7fo7E4CcGR_soi-sEB41UNqJjHgSidjXmXA7ZUjhzNOdRJLEQSBGQ8DACLQZTo4UcXIgnH2zEq-vqpU4ModXGvsdtWj9Hyx0pNOLZpBgnlt4bg28RqsyrWtW-jC7DtSRBPjWkbysqMyfOkYXyBWmcaWhRyInhr-t4BwA1doaT_2SCJD_3dfH3FJ_wgVs29JimQDj0NSBrqixCLc_-KWo7KQJAdO0uhXKC7U1nMAkg0Hhgl8hpkfXev_KxapbwVTbeH7Otx6TBzY7fhGr7CJmFOdrUelvXLfg1FJXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
دیس شنیدنی قیاسی به قیمت کالابرگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/108235" target="_blank">📅 12:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108234">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec43246d0.mp4?token=r_Rq415374rK-tvP98IpgT5mqiK8S2KxzqIMYHu3XeHclyQNnKJqf6nyPKOg0HGt6hR0nl9tTh_RCzXjsCVkZiMrqna-AGURf2K-dx5fc9pcc6Sj-hf1oSrM_CLx9hFJY_NmVPzyvdE-1_10weJbMjuUE4sFWTE1NAWhq8x4OvszNUcUdHpvF2bLhCuY2Ua0jRNEmOgBXHr9PZGtwhUSpa1C5xlh1-Qbv-i6zSQD9XrJRZFFvPas6pGj17x7ho6qhuO4LXk7mbINiNClmhMCYF4iaBLqoT959HHZGdzRzzy4NJU3kPRXSofoQanbgTP7Sf3dOhfBNDdgO3GaeVLWUgXAfr3xA8w3zMgmxJFZZR1oan64Yvp78O1G3Pajp0lPUM5vOJcdyNeBmvrjXWbFTn4AsTuibUO21XW7ofj33lWWuYd6ctY-1Dg5Tp0Uv023MMBNluZK4QbgLQFphCMCD7zSBEHhuf6NrY11e0NZuKrcAWSkq13nPDvEI5_YyWn_Tg_BaSwO4GELyYSqdqvL5T7obIHz6mg-C9Y98h5bYm0kfyeKLPfTOfZ1E9wEppwR9P4exiQyFIC9Ivi4Nr2fpItPFgP0dfZvVGzDslnsymwMADL4652F22iDmkfFZGofR-xMS90VTTLi_lfss2PK8_XYAOhMcRGPG7kb4Yy6q1I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec43246d0.mp4?token=r_Rq415374rK-tvP98IpgT5mqiK8S2KxzqIMYHu3XeHclyQNnKJqf6nyPKOg0HGt6hR0nl9tTh_RCzXjsCVkZiMrqna-AGURf2K-dx5fc9pcc6Sj-hf1oSrM_CLx9hFJY_NmVPzyvdE-1_10weJbMjuUE4sFWTE1NAWhq8x4OvszNUcUdHpvF2bLhCuY2Ua0jRNEmOgBXHr9PZGtwhUSpa1C5xlh1-Qbv-i6zSQD9XrJRZFFvPas6pGj17x7ho6qhuO4LXk7mbINiNClmhMCYF4iaBLqoT959HHZGdzRzzy4NJU3kPRXSofoQanbgTP7Sf3dOhfBNDdgO3GaeVLWUgXAfr3xA8w3zMgmxJFZZR1oan64Yvp78O1G3Pajp0lPUM5vOJcdyNeBmvrjXWbFTn4AsTuibUO21XW7ofj33lWWuYd6ctY-1Dg5Tp0Uv023MMBNluZK4QbgLQFphCMCD7zSBEHhuf6NrY11e0NZuKrcAWSkq13nPDvEI5_YyWn_Tg_BaSwO4GELyYSqdqvL5T7obIHz6mg-C9Y98h5bYm0kfyeKLPfTOfZ1E9wEppwR9P4exiQyFIC9Ivi4Nr2fpItPFgP0dfZvVGzDslnsymwMADL4652F22iDmkfFZGofR-xMS90VTTLi_lfss2PK8_XYAOhMcRGPG7kb4Yy6q1I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😳
مصطفی میرسلیم، عضو کسخل مجمع تشخیص مصلحت نظام: تیبا با خودروهای خارجی قابلیت رقابت دارد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/108234" target="_blank">📅 12:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108233">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108233" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/108233" target="_blank">📅 12:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108232">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqR1_SgT4b1VtgHwWcZz-B_Z3aEj3lFEDt5BZpa-_wyrl2leyxRpiaN7geJFFGignLQoDLBqBsp7CXeA5mruqW0DeqXLs_wdzJzwgl5qx0c-e1FGgGezZTekVnPeM5f9wH-dGtvvClKGWHOCAtZ_pYbZSc4RtFJF_i4LROpczsJ_FNztuFQndAGGeFu896nX4DwEADbMeMlXJarE2o4HL9T8RcAcQpQ9oR3wJNbG6xzxKDEGDZuUmSwzZSPa4AgQzF8czcgn-HQcEcLX2oVtAKDrFSnepVLEoKbyBVxelIBazPPUW_mRZtiCyGjEOsrOXFQT6CQ-Jtnm9RISmED8NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
لیدز
🆚
آرسنال
بورنموث
🆚
چلسی
تاتنهام
🆚
منچستر یونایتد
ختافه
🆚
بارسلونا
ویارئال
🆚
رئال مادرید
بایرن مونیخ
🆚
آگزبورگ
پارما
🆚
اینتر
فروزینونه
🆚
ناپولی
لومان
🆚
پاریسن‌ژرمن
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/108232" target="_blank">📅 12:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108231">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46a6a1545e.mp4?token=GT5KJLKckoJMmcIqfmqVSx-USGRUoVQIqRFNCfcx4rQSyUB5fN01pT4o8Q7pv0_RfpdKcMCdhjSNEocMEr5CWdORvXdb5zRelIr1jY4VT9dOqpSAXdY6mEqlQd98liUUQCMSzsp52R1hYNSET3kKwU3NdVFu02gRD3G5fuOUDEx59mXBl0rEf3H9O62pUL6JvBPzhKRUIrI6yjyokqk-9VoVsuzt8_dznElXs1UQQ6bE2UF0qK_E3SjKDDzq2ARPYrlAyzqPn-PsiXRzQl68_fMEUOfeqNNasnoajGxCSuvuxWmQ0CWsZx5o6yDlkIqRukrIUZiyCdhLzhL3bMtM7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46a6a1545e.mp4?token=GT5KJLKckoJMmcIqfmqVSx-USGRUoVQIqRFNCfcx4rQSyUB5fN01pT4o8Q7pv0_RfpdKcMCdhjSNEocMEr5CWdORvXdb5zRelIr1jY4VT9dOqpSAXdY6mEqlQd98liUUQCMSzsp52R1hYNSET3kKwU3NdVFu02gRD3G5fuOUDEx59mXBl0rEf3H9O62pUL6JvBPzhKRUIrI6yjyokqk-9VoVsuzt8_dznElXs1UQQ6bE2UF0qK_E3SjKDDzq2ARPYrlAyzqPn-PsiXRzQl68_fMEUOfeqNNasnoajGxCSuvuxWmQ0CWsZx5o6yDlkIqRukrIUZiyCdhLzhL3bMtM7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
امیرحسین قیاسی: گلشیفته میخواد برگرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/108231" target="_blank">📅 11:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108230">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28909a001b.mp4?token=m4Dgj4Qg5wzkZLx7oal_G7zDai7QIurFctgKwtcxeyV-oKLCJ4u5O41Zhxtyii56jqzDokYvylDB_s-mrqnLF-dm1O7sBpcL6HFahYbtThEyENkl5Qk1dLUd_5VWsliFd-3RdACN_sZYpYIraWAdHBzA900ComwN_yJCSDA0JgcqmN9MtZhht2AdDDgT1XcCGyTeP-nPGBPe0JNCsSdL8obI3Zxtk5rLkI1yYBYs22rqBDoz4tmtIg4YoS7zjYB5cDl40W7dj9d-_D8hVN56oPywlQ9fkEgTTfelm67vy_lnMBv6MqabcI5NhNb7Ftmuv-waAbWrln9mbD_WAaPLUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28909a001b.mp4?token=m4Dgj4Qg5wzkZLx7oal_G7zDai7QIurFctgKwtcxeyV-oKLCJ4u5O41Zhxtyii56jqzDokYvylDB_s-mrqnLF-dm1O7sBpcL6HFahYbtThEyENkl5Qk1dLUd_5VWsliFd-3RdACN_sZYpYIraWAdHBzA900ComwN_yJCSDA0JgcqmN9MtZhht2AdDDgT1XcCGyTeP-nPGBPe0JNCsSdL8obI3Zxtk5rLkI1yYBYs22rqBDoz4tmtIg4YoS7zjYB5cDl40W7dj9d-_D8hVN56oPywlQ9fkEgTTfelm67vy_lnMBv6MqabcI5NhNb7Ftmuv-waAbWrln9mbD_WAaPLUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇳🇱
نوادگان یوهان‌کرایوف در آکادمی آژاکس!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/108230" target="_blank">📅 11:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108229">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e15d66cbfc.mp4?token=iRwakiobHZUuI4t8vPnyslyXTgNtAmKPZxhWE-KfAQJzl4XbuC6QSQK9WE9XXHxlXN6YK-rUUDKoHkEy2yYsaIpc7K_eM-R90S9r-vxsJtXIqpLY0KKQCClpVLG5vpbNgPLeR0vZJl2vk20ZKSlWrAIlJ56cHoDXe15REGvs3j33m1_KrLxdrzlnlwvZYzB0OVaJe6TKUJ7PKDFh0MAKI-r_F66ACqa8jeXbtLFUy9zKY1krUezPFtpSth89YN7cDIcvRw5XqbQs35rmCB83Zt5nFIMU4O8b1N-Uj5SgcTZ9FZtCqT3839lOewqIk2iC8zO_gQxMQPU1QrPOtmycszzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e15d66cbfc.mp4?token=iRwakiobHZUuI4t8vPnyslyXTgNtAmKPZxhWE-KfAQJzl4XbuC6QSQK9WE9XXHxlXN6YK-rUUDKoHkEy2yYsaIpc7K_eM-R90S9r-vxsJtXIqpLY0KKQCClpVLG5vpbNgPLeR0vZJl2vk20ZKSlWrAIlJ56cHoDXe15REGvs3j33m1_KrLxdrzlnlwvZYzB0OVaJe6TKUJ7PKDFh0MAKI-r_F66ACqa8jeXbtLFUy9zKY1krUezPFtpSth89YN7cDIcvRw5XqbQs35rmCB83Zt5nFIMU4O8b1N-Uj5SgcTZ9FZtCqT3839lOewqIk2iC8zO_gQxMQPU1QrPOtmycszzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🎙
ماجرای خواستگار عجیب رضا گلزار: دختره بهم گفت نمیخوای تکلیفم رو روشن کنید آقای گلزار!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/108229" target="_blank">📅 11:05 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108228">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f9b62a8b.mp4?token=DnFp8ES1vPDRio6-WCtTswfcOrvKuqnCduGxbgxGz3qRVzvpiOE5_KwKQBIHdw-NX33YGmBxQrulYyDCjNTG1Edt8pOrSWXLFLGev1RrpMrI7pX0aI6OerqM1ipRg1aThcDetrM7HPYhVZpRN5WtbEi4miyLZ1o0oQ-2MAlHW7RvzETZsjrStxlDQzZSmDfJZnmSm8RzREXkoge2tG_H8h9fF9X5UHv6mMiGebrEzW2XvNxBgYm7vQxM5rRZbTv5ZSp03nDMvmU4yWOgGRZ555trNRedLcswxc4DdTq8IoHxHFfc1GOM21afNIEOFAYM2imLQFg2rx8BWvqVcqAWhTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f9b62a8b.mp4?token=DnFp8ES1vPDRio6-WCtTswfcOrvKuqnCduGxbgxGz3qRVzvpiOE5_KwKQBIHdw-NX33YGmBxQrulYyDCjNTG1Edt8pOrSWXLFLGev1RrpMrI7pX0aI6OerqM1ipRg1aThcDetrM7HPYhVZpRN5WtbEi4miyLZ1o0oQ-2MAlHW7RvzETZsjrStxlDQzZSmDfJZnmSm8RzREXkoge2tG_H8h9fF9X5UHv6mMiGebrEzW2XvNxBgYm7vQxM5rRZbTv5ZSp03nDMvmU4yWOgGRZ555trNRedLcswxc4DdTq8IoHxHFfc1GOM21afNIEOFAYM2imLQFg2rx8BWvqVcqAWhTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
تاج ادعای کریمی را تکذیب کرد: نه تنها ۳۵۰ هزار یورو ندادیم، از مربی تیم ملی جریمه هم گرفتیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/108228" target="_blank">📅 10:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108227">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حسین‌کنعانی جلو این اسطوره سندورم‌داون داشت خودشو به فنا میداد که شانس آورد
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/108227" target="_blank">📅 10:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108226">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4db6a9148c.mp4?token=Aad4M05ouFlGxnr3zCpYTtbQXD9eDY07wvtbv_4N5P2hXibZVZ2qkgJ-Bstx6kNZ7hQyo7fPu88QlDFAM0gSY6jtrTQOoIp21v8xyHfHjpyHt4b-qmeyohKMQaQm9cHcaPS7yh_mYD82brhX2i_I4ZcfWAOxMsKjyVM8VU8o0O3kxkKxiXpdooBLdYcfU1UblYDjvOFlS8Ted7GiNqDAjkOvcZrJTeE4lkpeSOXDBDeNQYlr5vQqiPO_HsjSdOF6IHB7b_kZDlueizvG7gIwmJhH9Ymsr6S8dah2hka-EKjfPRpUsawaM4AkRryTcjZzbuLkCuyRYDRGKIrEOg3HAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4db6a9148c.mp4?token=Aad4M05ouFlGxnr3zCpYTtbQXD9eDY07wvtbv_4N5P2hXibZVZ2qkgJ-Bstx6kNZ7hQyo7fPu88QlDFAM0gSY6jtrTQOoIp21v8xyHfHjpyHt4b-qmeyohKMQaQm9cHcaPS7yh_mYD82brhX2i_I4ZcfWAOxMsKjyVM8VU8o0O3kxkKxiXpdooBLdYcfU1UblYDjvOFlS8Ted7GiNqDAjkOvcZrJTeE4lkpeSOXDBDeNQYlr5vQqiPO_HsjSdOF6IHB7b_kZDlueizvG7gIwmJhH9Ymsr6S8dah2hka-EKjfPRpUsawaM4AkRryTcjZzbuLkCuyRYDRGKIrEOg3HAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
گلرها بعد از تعطیلات فیفادی
🫨
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/108226" target="_blank">📅 09:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108225">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e462fbf72a.mp4?token=OJadKsycy_arLlTS8u5Ts73jnKRUa8M4AklgSJssWD_TvAHr9UVTdVkMzM8ZIuCps8ILwOQEr89UWU141febOiKTNZ_PdkqOkTWdtSCCaCCq8MK5qORVP2rtAF50JEVdH06Pch-hfdWRzC3j-SZuE5RCnTCXLaE91ALVfTPcH7m3IokhAOwYrD-RzTXTV1Kf8ton904P-06u8-O1lg27QeLOkJPd2EyjSSLXkXuXeBTmWxKNQy1u_0TbbCSiV_3D8mUuFhOv69pmQNc837NUjnwheXaA2HPKrsYZwVu4xmRIsJdku0DdBZRnrvUjoyCmjz530T7vDXjcvmvt5VTrvjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e462fbf72a.mp4?token=OJadKsycy_arLlTS8u5Ts73jnKRUa8M4AklgSJssWD_TvAHr9UVTdVkMzM8ZIuCps8ILwOQEr89UWU141febOiKTNZ_PdkqOkTWdtSCCaCCq8MK5qORVP2rtAF50JEVdH06Pch-hfdWRzC3j-SZuE5RCnTCXLaE91ALVfTPcH7m3IokhAOwYrD-RzTXTV1Kf8ton904P-06u8-O1lg27QeLOkJPd2EyjSSLXkXuXeBTmWxKNQy1u_0TbbCSiV_3D8mUuFhOv69pmQNc837NUjnwheXaA2HPKrsYZwVu4xmRIsJdku0DdBZRnrvUjoyCmjz530T7vDXjcvmvt5VTrvjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
حمله علی‌علیپور به میثاقی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/108225" target="_blank">📅 09:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108224">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8286fc429.mp4?token=FJhJ-ri1JplfnJkfWC5woR3-y9dLklMo28_bRiUedrDNGsgQjzodjhiDq4GbV6BlJw_OMCSS3MtbMqSMKtGLZXK5IY3w5fk2FwhMjNgH7gVmReeqVHrP8c0n8-CMJkDMMTlu9EPsWOZp0G1HlclDnXSm_OvNdWlGHUD_I27YwERWmxIXLGQDPAJLV9bO7gISMnRvT4ZZBD4YHP6iGyvzIVj17EmQzywABKNrolW5ma1owrgKloPDgK7tTx9mnnYtJ7TLW0-UB6oYgAxd1nzZe954wrXKsAiPvPXcXMa7EPwABfxi6ej3gokDvebtV8lN3TlJbw3WmsXaHf5NW4oHzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8286fc429.mp4?token=FJhJ-ri1JplfnJkfWC5woR3-y9dLklMo28_bRiUedrDNGsgQjzodjhiDq4GbV6BlJw_OMCSS3MtbMqSMKtGLZXK5IY3w5fk2FwhMjNgH7gVmReeqVHrP8c0n8-CMJkDMMTlu9EPsWOZp0G1HlclDnXSm_OvNdWlGHUD_I27YwERWmxIXLGQDPAJLV9bO7gISMnRvT4ZZBD4YHP6iGyvzIVj17EmQzywABKNrolW5ma1owrgKloPDgK7tTx9mnnYtJ7TLW0-UB6oYgAxd1nzZe954wrXKsAiPvPXcXMa7EPwABfxi6ej3gokDvebtV8lN3TlJbw3WmsXaHf5NW4oHzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
میرسلیم: چه کسی گفته نفت ایران متعلق به مردم ایران است؟ نفت ایران مال مردم نیست و متعلق به خدا و پیامبر است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/108224" target="_blank">📅 09:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108223">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdfc01a1a5.mp4?token=cBLH3JZ7WiGXG2vMK3_hWN5-hMC1U5gercsR5UvvYZXJ6Vbvl49IfBL_-rLm7fSngWXzcTXuApACqfzL2q0Ftq8dXHd_N0_avnYyZriW_kzfN3Sbd6xN3KyYbD0k3qWVtoWRQWD07at8Ymus5G3e218yObXW4ApQNCw1rlQl5KgmMErCFf3njwBb3JE6D_2ulJY9Z36bEyOK8prb7ZOKRP-W6gh3-C-_lJ9c14iTaV9Ui6zRKEXLw7VEv9p4neDLPinRa0n65GdoUNe2cO4VpRx1I7NKvNzD3YVDd9_ggLpnm4IIQ_-C6CaSk_B-bFtUcpQRX3oqedLgYcVOEO0o7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdfc01a1a5.mp4?token=cBLH3JZ7WiGXG2vMK3_hWN5-hMC1U5gercsR5UvvYZXJ6Vbvl49IfBL_-rLm7fSngWXzcTXuApACqfzL2q0Ftq8dXHd_N0_avnYyZriW_kzfN3Sbd6xN3KyYbD0k3qWVtoWRQWD07at8Ymus5G3e218yObXW4ApQNCw1rlQl5KgmMErCFf3njwBb3JE6D_2ulJY9Z36bEyOK8prb7ZOKRP-W6gh3-C-_lJ9c14iTaV9Ui6zRKEXLw7VEv9p4neDLPinRa0n65GdoUNe2cO4VpRx1I7NKvNzD3YVDd9_ggLpnm4IIQ_-C6CaSk_B-bFtUcpQRX3oqedLgYcVOEO0o7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🇮🇷
🇮🇷
محمد تقوی، در برنامه هت‌تریک با آنالیز بازی پرسپولیس-صنعت نفت آبادان گفت: «سه بازیکن نقش پررنگی در پیروزی پرسپولیس داشتند؛ محمدمهدی محبی، بیفوما و ارونوف. صنعت نفت توان رودررویی با پرسپولیس را نداشت.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/108223" target="_blank">📅 08:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108222">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ffece8e7c.mp4?token=SlrlfaLxuT5oTFuzImqESC-4YNCQgaLN9ZW7bOf5iuQH0LYb4441HDcFBPsnwpIo0tjBhWU-_dquKo1P3S0Onya3lI-dgAG5lMf_pK_sXdhfifCfDFiJERohoZfSAUiXKwOT7p67Z2sJMDWV7KHKdFhlqJTeto_3KoEwCrOs8rYJhOZol_tXzdCf8VY5JJSU3xtCLq-nLmTF9LwE8YnNuIWNho2PNKHHfOBd7dK68jz0XjcRA51_UKZQCy1LmO2YYq64eBZQTrmGQLBu9UtYsZkGrVYJA4Jk8qUh-ddP-YFL89iz9gH8TrdE9n1vo6f2T2aFxPuJR6K2YV8j2zhafw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ffece8e7c.mp4?token=SlrlfaLxuT5oTFuzImqESC-4YNCQgaLN9ZW7bOf5iuQH0LYb4441HDcFBPsnwpIo0tjBhWU-_dquKo1P3S0Onya3lI-dgAG5lMf_pK_sXdhfifCfDFiJERohoZfSAUiXKwOT7p67Z2sJMDWV7KHKdFhlqJTeto_3KoEwCrOs8rYJhOZol_tXzdCf8VY5JJSU3xtCLq-nLmTF9LwE8YnNuIWNho2PNKHHfOBd7dK68jz0XjcRA51_UKZQCy1LmO2YYq64eBZQTrmGQLBu9UtYsZkGrVYJA4Jk8qUh-ddP-YFL89iz9gH8TrdE9n1vo6f2T2aFxPuJR6K2YV8j2zhafw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🇮🇷
🇮🇷
محمد تقوی با آنالیز بازی تراکتور و استقلال گفت: «من بازی را به دو بخش مجزا تقسیم می‌کنم؛ نیمه اول به طور کامل در اختیار استقلال و نیمه دوم تراکتور بازی را در اختیار داشت؛ استقلال شانس آورد که بازی را نباخت. اما مساوی، شایسته هر دو تیم بود.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/108222" target="_blank">📅 08:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108221">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c27c71fd.mp4?token=Nq4ArjjAmgdU0xgxAwXuB_uw_k5C8jm4LQRwRoNsBqrym1cHPo9Z5J25RDemZW-32Lv8wT7wshOKnCiFsR97xMxpjOAJGtKUbliocJTmIFiOmnD_PEi-_JlpprLh5urWNwVZS-WcREaPO2e_itJSHQN9BUsrguY9CcF-CLI1XLTvT93NKRcqELWSjaa3ZEYU9FSipczfxBEPTJMSOuifrLOgUVOgTUMkApB0OYepz0NCsr1va7if5sKEGVMytp1A0LxAMjHU40Fdg3hnr2ekbHLmDmxTSU596lgP91wDz5g_s6bESgzwBGa7xLp2o0dKflDzwSEs20W8TBOrKbwXaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c27c71fd.mp4?token=Nq4ArjjAmgdU0xgxAwXuB_uw_k5C8jm4LQRwRoNsBqrym1cHPo9Z5J25RDemZW-32Lv8wT7wshOKnCiFsR97xMxpjOAJGtKUbliocJTmIFiOmnD_PEi-_JlpprLh5urWNwVZS-WcREaPO2e_itJSHQN9BUsrguY9CcF-CLI1XLTvT93NKRcqELWSjaa3ZEYU9FSipczfxBEPTJMSOuifrLOgUVOgTUMkApB0OYepz0NCsr1va7if5sKEGVMytp1A0LxAMjHU40Fdg3hnr2ekbHLmDmxTSU596lgP91wDz5g_s6bESgzwBGa7xLp2o0dKflDzwSEs20W8TBOrKbwXaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
انتقام بیرو از حجت؟ دیس‌بک بعد از ۲۸ ماه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/108221" target="_blank">📅 08:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108218">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTFnB1puOvGcVzqbbT2T-BAy1Rck3WyA3UlOLRhPwZ7s78nq8vcLsluQwxBIrfHGhotRE6FqDwL_8TOvnaU68EUnwwBUr_WNwPnTPolYNX9D_9eiKza8dyDIwXoPL4KjuOkndJN6AJSrAABfGSNLY2c0oz_25W3j4nqH1OOC52dnqI6GaLrf0jd7nZVC_CGFEj2rsul7DkOsMf8VkHLLFaBuSzuMOsSRIrr7IMHLnvdIWNe0EAvj3JAXToKwkaNXhFVe4nSsOMNNBl9ili8mJU69JQRxdRnD9klLAuOzY5k_e2Zf8FH1skRdonzWpTK48w2VQZaJmoKUEQsjK5z90Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
❌
#اختصاصی_فوتبال‌180
؛
🔴
در گفتگویی کوتاه با مدیران پرسپولیس این باشگاه اعلام کرد که در نیم‌فصل هیچ قصدی برای مذاکره و جذب بشار رسن یا بازیکن خارجی دیگر ندارد چون ظرفیت بازیکنان خارجی این تیم پر است و محدودیت‌های نقل‌وانتقالاتی فصل‌جدید مانع از جذب نفرات دیگر خارجی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/108218" target="_blank">📅 01:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108217">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tg0DxvcgnB7wIwmOGuyhtjQTvRhthfqFiPoR08r3axTqstwpwRUVGf6C3WkAcRaHgfgvUbpDyDAS2snhwMM4e7Jj-tN34ellDZzHKOCFB1Vz1td-pNlREgtxGv3n7AfGQXo9SO3NhIjDblxKt28XDXcTcs3qNrAwE-yo-uVvU446OWGuBfO343Pu2sSAjUw-mweSUjku19v1Nqltw4nTu-OG6lClVuqCNEpYqHjxvKfs_luJrrOrnTZ8H0bNewC_xttsurHuK9wveCXQ06I5KgBFjPzw3K-SXnKsKA6697IGFU4KGFuctPe9wOP_Rt_qIutA8KhzvrKrMbhq4IXWfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔝
❌
🚨
وزارت امور خارجه آمریکا در توییتر: به هیچ دلیلی به ایران سفر نکنید. شهروندان آمریکایی باید همین حالا ایران را ترک کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/108217" target="_blank">📅 00:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108216">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrdXeEkVxcrGPVhLARZkRbmi3Zm-kxvn5E6pppkkidd5euFvEnVZAeWaVSK1qebeavn6M2mKeBfv35cSPYgKSJjfeQvde7Z9zSxZU1SXoNccalDg1hJt_EIxca4gX4Wo1XYalPbabLjqBaM0SpMrZrxG6YZwemg1UlgGykg8wt2nac_UTUS3mSmdzEcLctCw3SS3NCcH6Xn2XJ00fFLu3rfNqwn2OxZGvNY6E2R85IPemQNVLbUNvWAKVzanFj3WjimsA9-_sxcrDKrVZgEOir70DFxBSaJXAHNu8NExm19u2sP8R-cbHOZOdsDHjO8Isuxxq_VqI2Ql8dUxlBvz4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
🚨
ظاهراً سازمان نظام وظیفه به بیرانوند اعلام کرده تا زمان مشخص شدن وضعیت کمیسیون پزشکیش حق خروج از کشور رو نداره و حتی اگه بیرو با مدیران باشگاه به این اختلاف نمی‌خورد هم نمی‌تونست شاگردان نکونام رو در سفر به مسقط برای بازی با الشمال همراهی کنه مگه اینکه مشکل خروج از کشورش رو حل کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/108216" target="_blank">📅 00:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108215">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ab16b6ba1.mp4?token=pJKpu_pG6qlUNC8ss04hHmp3ArmS66OTO6ZVQVGZwWIIEBzVKU20EBrP243CitJeSHKK-dmDEYF5JD34XwPeWvy3Py2ckxEYVe-DrDVx2J0y618qaUINNk5KoC_WiMJhRw4Bgp-ZLRDi8IOxIH0uneLt7fHbhDlymKF7v9wjfL2StLVjf2c2MZ7Xv19fXSKk7c-tq_wu-eaO-wvR8WJ7Abt32Y5PMkBTIJmwd6pIsDIv-qXv3NHrLqecqwnLTlGv59eVFZ-4DnMR1wdC926VbQr6iC89jyYYS1Px43242PAns4y24CYcCR7T1ZvLy_MwZDrOXOnY-cK87PPN6OJNXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ab16b6ba1.mp4?token=pJKpu_pG6qlUNC8ss04hHmp3ArmS66OTO6ZVQVGZwWIIEBzVKU20EBrP243CitJeSHKK-dmDEYF5JD34XwPeWvy3Py2ckxEYVe-DrDVx2J0y618qaUINNk5KoC_WiMJhRw4Bgp-ZLRDi8IOxIH0uneLt7fHbhDlymKF7v9wjfL2StLVjf2c2MZ7Xv19fXSKk7c-tq_wu-eaO-wvR8WJ7Abt32Y5PMkBTIJmwd6pIsDIv-qXv3NHrLqecqwnLTlGv59eVFZ-4DnMR1wdC926VbQr6iC89jyYYS1Px43242PAns4y24CYcCR7T1ZvLy_MwZDrOXOnY-cK87PPN6OJNXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
🇮🇷
آخرین وضعیت شکایت باشگاه ها از آسانی از زبان رئیس فدراسیون فوتبال: هر تیمی دلش میخواد میتونه به CAS شکایت کنه و مانعی نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/108215" target="_blank">📅 23:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108214">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MicHYqf_TP5yzcqu0F5rZoGkKDZYWE-WOHd7Lp6IUQlaURzxlbLGjC-yxzJFmDftkMAfRaDb7H4wcV3FCWK-R5-hL-zE8vE0xcuM5FoMxW4A2WS_z2tNp6ZtX9ud_SE-GUeM8ETQVzQgkgwHHoqR5_r6JNMKLJhLUwcH2fGOUY71BOILpNQUeyLdnWSf1RsaRRwTYF6hTEnrGYoi-Fk148Pq0DajqXoKuk8PsRnlfwSbOa6OO_jKZ5TKNJwgV3TWyQTULOxf3tCc3rFY1tZNoCiG2peuXCUyG8_RJrdjfTOwfF8EjFlq-FynxOH_QChgCmquYXWWSookVxMUNjUX3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
فوری؛ بیرانوند از هتل اخراج شد!
علیرضا بیرانوند پس از درگیری لفظی با مدیران تراکتور و در آستانه سفر آسیایی این تیم، از حضور در اردوی تراکتور منع شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/108214" target="_blank">📅 22:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108213">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQ46HYOLK_bhXY1TC39CZzIZiFwDd4cLtdTGmK_GEvrn0SURM5Ima_S_z5dAPM_WBNEPvmOfkwqG8hH6eBr4g56Z6wBbsxvB6OtJ-FBpfyRDB6bJqBXRNBA80vjwW0BR6NmccxA71JL7_zOLMHI8Jz7wDFSdWTdOyLs1BqTCaz8fyp5YnyWV2srM4dJgs6H1CVQYJA39IEdDkx345jTiP5uyuh5maOKwcg4o01nfe2KlFM4i1ysPvSrE76RngSPu5XpkPQVn7H8K2OfMYR3jbh-jAltqs5wMOqYouFn6NoxPnO8m4Uh4Z_lxz1BBZaQzyH5pcehqC61giQCY9V1bAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
❌
محمد نوری پس از شکست مقابل پرسپولیس از هدایت نفت‌آبادان اخراج شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/108213" target="_blank">📅 22:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108212">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b78fb174d.mp4?token=ALhSJ4ZrGycj4QZghXELD2mnTaDyiaYhjRtXWJoH7Cw9hvxMT5ZBjjbWM_etuYANsa0JLWUJ2qqJWpt2oFvYYI27wNNPlT3RcLVc5L-_saAA7gtJZULzMtJCPt5fKIeAczB4WVduiD2WhjqjakKB58jM0lpdL84zPkVm-5KrYk3bR_575CN0pPAdG0qTkmjMZGAAWX5iIv9_mR5wJ9BTmjG5Rry8wZ5H3x_MtwQmOBIL4jhGnOWIioitlamQ0fIOufTZO0umSSlCauktB04Mb8kNamSJ6UukjdtDyqt1njBMp-X_-KMXJTFW3CeNW0KajTSRirEVBDtNa1In9YBmqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b78fb174d.mp4?token=ALhSJ4ZrGycj4QZghXELD2mnTaDyiaYhjRtXWJoH7Cw9hvxMT5ZBjjbWM_etuYANsa0JLWUJ2qqJWpt2oFvYYI27wNNPlT3RcLVc5L-_saAA7gtJZULzMtJCPt5fKIeAczB4WVduiD2WhjqjakKB58jM0lpdL84zPkVm-5KrYk3bR_575CN0pPAdG0qTkmjMZGAAWX5iIv9_mR5wJ9BTmjG5Rry8wZ5H3x_MtwQmOBIL4jhGnOWIioitlamQ0fIOufTZO0umSSlCauktB04Mb8kNamSJ6UukjdtDyqt1njBMp-X_-KMXJTFW3CeNW0KajTSRirEVBDtNa1In9YBmqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
گل‌شماره ۹۸۰ کریس‌رونالدو در بازی امشب النصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/108212" target="_blank">📅 22:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108211">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🔴
طبق شنیده‌ها؛ باشگاه پرسپولیس مذاکرات خود را با مدیربرنامه‌های بشار رسن عراقی آغاز کرده تابرای جذب این بازیکن در نیم فصل به توافق برسد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/108211" target="_blank">📅 22:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108210">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
⭕️
🇮🇷
مهدی تاج: هیئت‌رئیسه مخالف دادن جام قهرمانی به استقلال بود، ولی این مورد مجدداً در حال بررسی است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/108210" target="_blank">📅 21:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108209">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
‼️
🇮🇷
محسن خلیلی، سرپرست پرسپولیس:
یاسر آسانی؟ باشگاه تمام مسائل را از صفر تا صد پیگیری می کند. داخل کشور به نتیجه نرسیم صددرصد در دادگاه عالی ورزش دنبال می کنیم. ما نگفتیم این پرونده پایان یافته است. مندیت آسانی به پرسپولیس؟ بله او مندیت را داشت اما زمان همه چیز را در این زمینه نشان می دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/108209" target="_blank">📅 20:08 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108208">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VF1m8kwzlpUDTlItW2b4TuSg2pSAxlmMjMukpFXXK0h1Obsb_K0O0WaOzSph5FWyV9rvKZmJ7qZ6N5gsrNBeg6CGlzpQ6X03t-qa0xp6YsHHUIAKlBWm3Ths6EURtLvgcyjKUQ4YvohUApiyhuxjM3MIpJBJ_V1n8CeaULoYYt5t7yhWEraNCg7LCHJWQHWFvB-nW_eVyPOgTbA9pqDyzW34BRsfw5XD334ZPJIAmHLpP7lg6xCAp0Xr4z6bgUVck4ZgHxhdOvwFRjeAk4Wdm_X-jiLFDifSf_2t-HVE6VPdtgBPIMV3Gfnm_LtoU2msrlBgtEYCG_KOetbTJOe5aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
رونالدو در ترکیب فیکس النصر بازی بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/108208" target="_blank">📅 19:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108207">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e597b9b54.mp4?token=G5NDLE3fDTstfUcE50c6lEgiagjas9Lb0Z3kDtaa21drkKQUUOygmby-Iusi8DTO8X1y9HM4KFQ9AaAEwnVBwdBRpp5FomgZfAm4-SZetoku37gL0Hn1f4vojwLvi-MklglBF6CGvc6gKeE_tNBrn6mn1CSgiDs_X8GPvDwcbzyQUelmpMnXKDnmHdjGxOYFmRK2sGM5zGQX3YWTZSgvLA--5pc4EhjzUciDE8DFbiak4Flrf3y2kOed36HoCCCs27llxpklPOkgtKY7k78nOG2Yp0J9dEgIbhjoIPPfZ9tSzDP_yl-1SJwnE7Xwgn0M9p5dBx542rLjKQt40623ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e597b9b54.mp4?token=G5NDLE3fDTstfUcE50c6lEgiagjas9Lb0Z3kDtaa21drkKQUUOygmby-Iusi8DTO8X1y9HM4KFQ9AaAEwnVBwdBRpp5FomgZfAm4-SZetoku37gL0Hn1f4vojwLvi-MklglBF6CGvc6gKeE_tNBrn6mn1CSgiDs_X8GPvDwcbzyQUelmpMnXKDnmHdjGxOYFmRK2sGM5zGQX3YWTZSgvLA--5pc4EhjzUciDE8DFbiak4Flrf3y2kOed36HoCCCs27llxpklPOkgtKY7k78nOG2Yp0J9dEgIbhjoIPPfZ9tSzDP_yl-1SJwnE7Xwgn0M9p5dBx542rLjKQt40623ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
‼️
🎙
پیام نیازمند: گل صنعت نفت؟ من را ساندویچ کردند و گل زدند؛ مثل روش آرسنال/ از گلزنی اورونوف خوشحال شدیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/108207" target="_blank">📅 19:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108206">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1c0466c5f.mp4?token=qMWtiQ3Qb5k73B5cr8sKZ-HGFyWmPXPmJpNb3Km4h8UV3dCZgWoWseNSwH7Wr2DxR_1VD1xautMz3SuwOhrX1fbZB-9DOGZ7go7VfU_rA4sfmGJhajr7O0COo8rSSXb2fFwXB6TGl_r7Daok5_VqPhY7qC2csdapnpz4mAgOuVX_dvhhYYUGQfaSfRnicQ2KBH8tSjzv5dntqT006o6J45cs3i6uJoxqlPmtoe-XWUSrLSJydLTDdYVreyNofQdByTYHkskMmyYcJF0iXHtJ0Eqy5ZPK8zElpEe5bNggFMpjTTZVtXrNRYjnPO2jnOlDPZE75mR4Sp7IXiA94qfVSSy_KWMYQeBoGnkF2eiEAEcDZPviZ1g025LfrMmjYaXIuYiSP_F6vMBx5I1Ty11tm553rrl9KNg7iVtH_EeipDjbp7V73Q8pIBS-JXBjny5uSOO1ZkrDZiSoxwfuC-LH8omrDdPmDVV23MYWGdZQsUnIkYlpcvMVdLFkWjS4Ivnb1Ios6LNeQIRdWXyyt6e9G814BLlVmSYIIVJB8u0OIxPCbgXxB0Sw-vXFByxqbaZtGZyprD3NvB9OdZGEGov8nw8ubxx3RMOaXx_HDHKL_YuWicvVRcWYXfVXSWJKlqTG8fEJnuX5tjfrgOrvEDnzOh8BDQQcTt64iUCT9WlnYkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1c0466c5f.mp4?token=qMWtiQ3Qb5k73B5cr8sKZ-HGFyWmPXPmJpNb3Km4h8UV3dCZgWoWseNSwH7Wr2DxR_1VD1xautMz3SuwOhrX1fbZB-9DOGZ7go7VfU_rA4sfmGJhajr7O0COo8rSSXb2fFwXB6TGl_r7Daok5_VqPhY7qC2csdapnpz4mAgOuVX_dvhhYYUGQfaSfRnicQ2KBH8tSjzv5dntqT006o6J45cs3i6uJoxqlPmtoe-XWUSrLSJydLTDdYVreyNofQdByTYHkskMmyYcJF0iXHtJ0Eqy5ZPK8zElpEe5bNggFMpjTTZVtXrNRYjnPO2jnOlDPZE75mR4Sp7IXiA94qfVSSy_KWMYQeBoGnkF2eiEAEcDZPviZ1g025LfrMmjYaXIuYiSP_F6vMBx5I1Ty11tm553rrl9KNg7iVtH_EeipDjbp7V73Q8pIBS-JXBjny5uSOO1ZkrDZiSoxwfuC-LH8omrDdPmDVV23MYWGdZQsUnIkYlpcvMVdLFkWjS4Ivnb1Ios6LNeQIRdWXyyt6e9G814BLlVmSYIIVJB8u0OIxPCbgXxB0Sw-vXFByxqbaZtGZyprD3NvB9OdZGEGov8nw8ubxx3RMOaXx_HDHKL_YuWicvVRcWYXfVXSWJKlqTG8fEJnuX5tjfrgOrvEDnzOh8BDQQcTt64iUCT9WlnYkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
واکنش جنجالی گوهری به جدایی از پیکان: تیم می‌باخت، سرمربی می‌گفت ما جادو شدیم و فقط دنبال این مسائل بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/108206" target="_blank">📅 19:54 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108205">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4ed7f5cfd.mp4?token=SEP_1JG62IoElIpgRDsZHjBt-K8cviVs7vtzqvaeN7LxZ0QrANadozazc6-e4--6rzMJykk-KjKebKWjhUKO8RqGNS_XaOegpnQUkzN2AQD3YM-jKDQ9kNjmzXARDIR1Vd99FPkAbGRHvUpKeQG9fmrYa8uqWLyRyMKwCkcoHOkpu4wlr3nLvhz5h27E1tZIEoQmgFJBDv275dk4OvM9mQnK0tL6YSPuY9qurd8akJ_qwBqkKLnHt5WUeeI4dTSjrIpsfyte02O7lrkHmG6OIUOp_fAvLW3zIhW_dSggILPLxkq9HjEeQ2RVbgA37SEnBY62_Dk3RUVzjcfIGUQifUlM1IIlbeycDIRaEVvvemu32boZhdgCWCrON5_Gx2GhxvM25W-rTneYutlAH07veV0Oeze4Fn09JHPlhCvjFN6xkgmj8fFUP30Aqa31VZVG6DHdeo6oFrR7suJ65ANyNQBV7zzErFuVIZlfYK-3l1INbXQwnVHkI5xhFH_h53KEBfM--CpveV8XqwTZt0qyuUkhC_WBkxZWNCB6ZrM6hcpo9jaAEj_qWJ7AVY5LDRDXAd3k7krPLDF2fdLGMHJUtncCbWVrR8TbMaXySYoVFG1_2Whwm5SG1hEOtqEvVLo02lp6bM_6gAPyuM63chADqIL-a_X__EShCzVD_3e3LYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4ed7f5cfd.mp4?token=SEP_1JG62IoElIpgRDsZHjBt-K8cviVs7vtzqvaeN7LxZ0QrANadozazc6-e4--6rzMJykk-KjKebKWjhUKO8RqGNS_XaOegpnQUkzN2AQD3YM-jKDQ9kNjmzXARDIR1Vd99FPkAbGRHvUpKeQG9fmrYa8uqWLyRyMKwCkcoHOkpu4wlr3nLvhz5h27E1tZIEoQmgFJBDv275dk4OvM9mQnK0tL6YSPuY9qurd8akJ_qwBqkKLnHt5WUeeI4dTSjrIpsfyte02O7lrkHmG6OIUOp_fAvLW3zIhW_dSggILPLxkq9HjEeQ2RVbgA37SEnBY62_Dk3RUVzjcfIGUQifUlM1IIlbeycDIRaEVvvemu32boZhdgCWCrON5_Gx2GhxvM25W-rTneYutlAH07veV0Oeze4Fn09JHPlhCvjFN6xkgmj8fFUP30Aqa31VZVG6DHdeo6oFrR7suJ65ANyNQBV7zzErFuVIZlfYK-3l1INbXQwnVHkI5xhFH_h53KEBfM--CpveV8XqwTZt0qyuUkhC_WBkxZWNCB6ZrM6hcpo9jaAEj_qWJ7AVY5LDRDXAd3k7krPLDF2fdLGMHJUtncCbWVrR8TbMaXySYoVFG1_2Whwm5SG1hEOtqEvVLo02lp6bM_6gAPyuM63chADqIL-a_X__EShCzVD_3e3LYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⭕️
🇮🇷
بازگشا، سخنگوی باشگاه پرسپولیس: مدارک کامل و جدید خود را در مورد آسانی به کمیته استیناف ارائه کردیم
🔴
همه تلاشمان این است که موضوع در داخل کشور حل شود. حل شدن در داخل کشور احترام به ارکان قضایی کشور خودمان است. درخواست از پرسپولیس برای پیگیری نکردن شکایت؟ ما دیروز نامه ای به فدراسیون زدیم که قانون محل مصلحت نباشد. یک بازیکن می تواند نظم جدول را به دلیل تاثیرگذاری اش بهم بزند. فدراسیون درخواستی برای عدم پیگیری به ما نداشته است. تا آخرین مسیر از حق باشگاه دفاع می کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/108205" target="_blank">📅 19:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108204">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ad5142fc9.mp4?token=KEgVLiJndQLAvBBisgg9HmEuCrqWl2yEG0OmdFM3lkqkwzGINsy4D8RNcfVBgdc2nlGATpfql0lvrioTmmXNNQN6ZFGZFMShPX9pjjrBUA2151OrcSuoSpZ5MX9JSJHWwDSQquSlcFjZXOK2ow4bOAlw5jlycnIJecdgKJtZ9AA2zG-LdxO92UnLheWTPIpkRFAAJWlVpozA9t354GheUC0BjXzzcMzj7Pu8XW9e5bbMxAc7y4mQ3WT2EdVqcLGmxTfHwBxK4kzhHmBy1xxirW_-4Kih5_XsPBztupKSAqBUQXR4bhEtBMXVwEk3HJPvl14jNvzRWOd_8Ve6iqVQjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ad5142fc9.mp4?token=KEgVLiJndQLAvBBisgg9HmEuCrqWl2yEG0OmdFM3lkqkwzGINsy4D8RNcfVBgdc2nlGATpfql0lvrioTmmXNNQN6ZFGZFMShPX9pjjrBUA2151OrcSuoSpZ5MX9JSJHWwDSQquSlcFjZXOK2ow4bOAlw5jlycnIJecdgKJtZ9AA2zG-LdxO92UnLheWTPIpkRFAAJWlVpozA9t354GheUC0BjXzzcMzj7Pu8XW9e5bbMxAc7y4mQ3WT2EdVqcLGmxTfHwBxK4kzhHmBy1xxirW_-4Kih5_XsPBztupKSAqBUQXR4bhEtBMXVwEk3HJPvl14jNvzRWOd_8Ve6iqVQjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🚨
‼️
🇮🇷
هوادار پرسپولیس: کامنت در پیج السد؟ ماجرای آل کثیر را یادتان رفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/108204" target="_blank">📅 19:22 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108203">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwUfIiOrxXBVSIqJHB7kHyuH4m9RsvmslsI61e_5c6ioIk-WDNJHqpcEGvko0W4MdZl9jWCwqFYYAbQAqJCrdXkkLKsfrQWaJbHanGDu6JP4l0x1uWsrvro7F8L0lJ1YDQBP7RX-kYq7JEj3xO2GZKCHNwgPXZqVgJpxIOoeqeDFazD1aIy03zSwy9RmWA1jvMw0ZOm2YXz9A5Bu52t16mzZ72kW4PHgWc29UnLo2bxN4bnxaEBaR_SugzZsJlWc3P4g6VbpsFPzDRYENI1PpOvgQK6xQJVaN5JDcv6zW037L7oLNyD_lzrs5_MwAZjr7ev5v7Yeg9CducmdA3HEmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
هفته‌هشتم لیگ‌برتر؛ بهتر از این نمیشد؛ برتری خانگی با گلزنی اورونوف و بیفوما؛ علیپور هم طبق معمول گلزنی کرد؛ پرسپولیس در آستانه گرفتن صدرجدول از تراکتور
🇮🇷
پرسپولیس
3️⃣
-
1️⃣
نفت‌آبادان
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/108203" target="_blank">📅 19:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108202">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOExE8tlY3U8eSgPD6iT_sfdtaH7rZ3QZgJsJUhypJTRknOdeqkrMi6AIZU2Dm4PmCYjzmSm0q8RaH1IVd47ZfjDIvFONVhAH4zAecT3Wrj0dr-B3afuyPUbxht4WyKkNY9hv1xTAESczTcMKFn0NvqiRAh7qq7xoQY-JNOQJ4_6_PxriA57nDu7rXzoL4ynR6z5ZvvsQt-uJmkjy0EWGRU1kPnLWM31shp5MrD9bJlFFMIL0XzCrgn7LHZQ4DyU0zREw9piKvfy1B294QAPqvfMrDSqw9jj2fGti8yUo3C2useYWBF8xasLO7BVpqcNYbVQ1qkMqd-EME40gegbHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
هفته‌هشتم لیگ‌برتر؛ بهتر از این نمیشد؛ برتری خانگی با گلزنی اورونوف و بیفوما؛ علیپور هم طبق معمول گلزنی کرد؛ پرسپولیس در آستانه گرفتن صدرجدول از تراکتور
🇮🇷
پرسپولیس
3️⃣
-
1️⃣
نفت‌آبادان
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/108202" target="_blank">📅 18:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108201">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19c9ae46fc.mp4?token=aESFZLhEnE2aJWVCNxOu7DV-NiavPIWIHkVXftvmJXFD6eB0g6hYpJEGyCkBx5plKHGQxWg2y5b_bkjk7J6_1B_FAMx6l4GyKYl21xlmBVKUzT0eZQ-wILTA6HrK9VBqcJMOtJXQ6njdg-uDlCdCq5dtlw0L-NbQNKniKPvJ-ib7hedffD6VJ-TBGnAIVlU0sFlsqTqWvATHefwrfs7cgWSjS00Z2trY53jE_MYvJ9uApxtqVHxttIn6i7hcQTmOHmvzjPIYDw5jdo-ex00TpS0e39PPXJG8x3Ba_D_CZZvWTi42RSv3aoi3XF1y3r_5ssI0-wF0EZFzIxUrbDHI8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19c9ae46fc.mp4?token=aESFZLhEnE2aJWVCNxOu7DV-NiavPIWIHkVXftvmJXFD6eB0g6hYpJEGyCkBx5plKHGQxWg2y5b_bkjk7J6_1B_FAMx6l4GyKYl21xlmBVKUzT0eZQ-wILTA6HrK9VBqcJMOtJXQ6njdg-uDlCdCq5dtlw0L-NbQNKniKPvJ-ib7hedffD6VJ-TBGnAIVlU0sFlsqTqWvATHefwrfs7cgWSjS00Z2trY53jE_MYvJ9uApxtqVHxttIn6i7hcQTmOHmvzjPIYDw5jdo-ex00TpS0e39PPXJG8x3Ba_D_CZZvWTi42RSv3aoi3XF1y3r_5ssI0-wF0EZFzIxUrbDHI8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گل سوم پرسپولیس به نفت آبادان توسط اورنوف (84)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/108201" target="_blank">📅 18:50 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108200">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4da4e50a3.mp4?token=XMOilZu27D-E17Rp4F2NrVQOMgrgQZ9VdWrXS2zexMlFtVICjt0FO16MC8xqgj-jpiDwQJn4VllTKHVSnb228Hg8QODKN-goiV0VXaxh72826ZVb5aefdwXVWsiNwbvpH7-vUsyE2nrt3l2pVeimS06Wi1O6G2aRAfoYQt3E7z8Ux9wZDqZGOy9jXt50HCCXuhnPYBO6kzVvv6gZ2dVmge1YivC7Rjh1OG64yUpiFejv1Nv_dsaGzv3cSKeU_MaafORwzqLBF5NLsqRt5H7QcXwBUMwRo8KIjOk4RQIk9B_P6ISpYA3natC2u4zqsj5BvhEAjwpW6YU5xCpWmQAS1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4da4e50a3.mp4?token=XMOilZu27D-E17Rp4F2NrVQOMgrgQZ9VdWrXS2zexMlFtVICjt0FO16MC8xqgj-jpiDwQJn4VllTKHVSnb228Hg8QODKN-goiV0VXaxh72826ZVb5aefdwXVWsiNwbvpH7-vUsyE2nrt3l2pVeimS06Wi1O6G2aRAfoYQt3E7z8Ux9wZDqZGOy9jXt50HCCXuhnPYBO6kzVvv6gZ2dVmge1YivC7Rjh1OG64yUpiFejv1Nv_dsaGzv3cSKeU_MaafORwzqLBF5NLsqRt5H7QcXwBUMwRo8KIjOk4RQIk9B_P6ISpYA3natC2u4zqsj5BvhEAjwpW6YU5xCpWmQAS1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
گل اول صنعت نفت به پرشپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/108200" target="_blank">📅 18:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108199">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aa65c912b.mp4?token=mr_Vs1oKqnuHdVNlQyIWdKPGkeH5JDxOOQMBVDEN_VEgJiNaZ3V_MraQEfv2sql8HKQFM_hISW_rT0B-LiFOHfrHjL6Ujg2c6AUT-ZksX3tWqpNiiTTpd9-j3zuZTEH8woR7Dxms7CR0VpsDJI4Fv6pNH67x5nO4GZnOl1eOQZ2zaiXq_PsbS5hhROVrFH6AsSvOrXULEy7c6l4730m-H8bO6poGBeN9UZfsivIq2M32TeHda08qgmxPptPnHsjM8PRLhnzRxv_G_halNPg1D_ipNJ8hQXeJQjun-5d4yDbpXoa08w0cj6zHF8a4lrU_iYXZhfBA2_nCv-uMu4gX8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aa65c912b.mp4?token=mr_Vs1oKqnuHdVNlQyIWdKPGkeH5JDxOOQMBVDEN_VEgJiNaZ3V_MraQEfv2sql8HKQFM_hISW_rT0B-LiFOHfrHjL6Ujg2c6AUT-ZksX3tWqpNiiTTpd9-j3zuZTEH8woR7Dxms7CR0VpsDJI4Fv6pNH67x5nO4GZnOl1eOQZ2zaiXq_PsbS5hhROVrFH6AsSvOrXULEy7c6l4730m-H8bO6poGBeN9UZfsivIq2M32TeHda08qgmxPptPnHsjM8PRLhnzRxv_G_halNPg1D_ipNJ8hQXeJQjun-5d4yDbpXoa08w0cj6zHF8a4lrU_iYXZhfBA2_nCv-uMu4gX8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گل دوم پرسپولیس به صنعت نفت توسط علی علیپور
P53
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/108199" target="_blank">📅 18:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108198">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4b20c129.mp4?token=ZU7G5VNHBbHBhmGfj9su5a4oM6QM2SjZUldBib581EzttktCFajYqzIfoR_i7TRMHhHUTv425jKlcwkWjnHA-Xz2t7CmwFao7gofL-ZYhFBtyyKRkWAH0mEcIDbn1xES1DGzUY6Vw6GqV4Arm_gEA50eSm1FP_eg9m9tG2OlHBY5qvmPCPHRpz_-o7vGz9HStJT24gOU24TLoPLXE0_UpjgU5yi8cqIqGjYcTqA_THiEBhO1XFFkfOASmItkUV2s4fJxpKekaqqwqMGysFsE7Bxd7K8oevPfXGxgFbmKnvmMnOosq4QLrtf8s2bAJ8VrlgY-Sl_R7adJsGBhtZvpsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4b20c129.mp4?token=ZU7G5VNHBbHBhmGfj9su5a4oM6QM2SjZUldBib581EzttktCFajYqzIfoR_i7TRMHhHUTv425jKlcwkWjnHA-Xz2t7CmwFao7gofL-ZYhFBtyyKRkWAH0mEcIDbn1xES1DGzUY6Vw6GqV4Arm_gEA50eSm1FP_eg9m9tG2OlHBY5qvmPCPHRpz_-o7vGz9HStJT24gOU24TLoPLXE0_UpjgU5yi8cqIqGjYcTqA_THiEBhO1XFFkfOASmItkUV2s4fJxpKekaqqwqMGysFsE7Bxd7K8oevPfXGxgFbmKnvmMnOosq4QLrtf8s2bAJ8VrlgY-Sl_R7adJsGBhtZvpsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اعتراض شدید تارتار به پنالتی مشکوک صنعت نفت
🔴
@Perspolis
@RedStarFc</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/108198" target="_blank">📅 17:36 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108197">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3013266bc8.mp4?token=VuhcP5-wfRVqVSSVhp7tMMHif4xTLaXlAh9LpZF42WStTRooDwG-hmodM0XZD6eqvGs8GV0uQr51OdTxtLpO9kN9N1apWF2egpo-mcr0M5kUGn5OXd4BM5_7U-BR4-MDiMYmNUR3F9CXM_ATQhi9R395HWvwLIyQyv0KTf_-tBV08zn-gapg6WRmAbfaKrfJnK0IKONOuT5YgU_Y-1aZy-gmix8zJka12QeZtv-sTlWPP2ko_DbD8NvDc1hU_0Yg1aGxKj022cOexXLPLuuuR37GLykcIm6v7FJenlvfFZVNjjw8l6aG6RrnCKE0asm_3XD_vHk14hHjRdFXLHwW3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3013266bc8.mp4?token=VuhcP5-wfRVqVSSVhp7tMMHif4xTLaXlAh9LpZF42WStTRooDwG-hmodM0XZD6eqvGs8GV0uQr51OdTxtLpO9kN9N1apWF2egpo-mcr0M5kUGn5OXd4BM5_7U-BR4-MDiMYmNUR3F9CXM_ATQhi9R395HWvwLIyQyv0KTf_-tBV08zn-gapg6WRmAbfaKrfJnK0IKONOuT5YgU_Y-1aZy-gmix8zJka12QeZtv-sTlWPP2ko_DbD8NvDc1hU_0Yg1aGxKj022cOexXLPLuuuR37GLykcIm6v7FJenlvfFZVNjjw8l6aG6RrnCKE0asm_3XD_vHk14hHjRdFXLHwW3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشتباه عجیب سیروس صادقیان!
⚽️
⚪️
گل اول خیبر | امیرحسین فارسی '35
چادرملو 0 - خیبر 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/108197" target="_blank">📅 17:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108194">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‼️
اعلام پنالتی به سود صنعت نفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/108194" target="_blank">📅 17:15 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108193">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef96e5b249.mp4?token=iBh9n5HbhsqR5ZqiAB6eqExp6b6YAT3B1xc-jmA6yPv0IqQCgbw7LbEqAzQr7WDoGIyvY-bEN1R_vpJQY8f71S4PYlxjRvZqglmtZ0zuKO8hBPiWhtJK6YQSsXIWSjkRKGSQ_AW4XHyFJlxrY4qhO6k4S09duwKA80bankXo0w1Ik_NMR2CBgkre8BnbGOhvKjOzxPnBZ8RwDgvbiQbrv-zwLyzqeupmkFCN74dwxgxcFnzdniHj9d8j4ZaB659QkhJgJOsoizOwTg2KkkXqTRMinf_25xpNmHufVOmDf-yZOiKIYApk5vz2YCsJ5WZAlepKRp-_O3EQkaKkGnwbeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef96e5b249.mp4?token=iBh9n5HbhsqR5ZqiAB6eqExp6b6YAT3B1xc-jmA6yPv0IqQCgbw7LbEqAzQr7WDoGIyvY-bEN1R_vpJQY8f71S4PYlxjRvZqglmtZ0zuKO8hBPiWhtJK6YQSsXIWSjkRKGSQ_AW4XHyFJlxrY4qhO6k4S09duwKA80bankXo0w1Ik_NMR2CBgkre8BnbGOhvKjOzxPnBZ8RwDgvbiQbrv-zwLyzqeupmkFCN74dwxgxcFnzdniHj9d8j4ZaB659QkhJgJOsoizOwTg2KkkXqTRMinf_25xpNmHufVOmDf-yZOiKIYApk5vz2YCsJ5WZAlepKRp-_O3EQkaKkGnwbeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اعلام پنالتی به سود صنعت نفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/108193" target="_blank">📅 17:14 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108192">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60684bf96a.mp4?token=HGc6Cr7sztKuPQB_86DJvzeo2kjNQjXTcXUqVdAYGNzMZ4yq0ZPzwL5_6tdJHp8qDWBYJ1A0vk066YAkPyzH9zzBolnX45ds4pOvbynk3CNlcWav5Bq-c-OMvkaYSArt6QNbVEUcwOMAiSS9_V1kx_-nASe7KnRl3Gy6WTaLYpvn7ve922vqQ3eS9C5y2FwuxPY6yxcJM-0mIXiwmarKCKH29st4Q2rMhLm4nX83NOg-9EJAgqb6rNQ-ijRMQ5pTU5AD-D7np81Nwzafu9uBQscTEHAOpfkpP_LpXT81YgM4Snbm0slu8fE1fEZFXA2CMkd8mhPMnfN4Eg33lWDJfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60684bf96a.mp4?token=HGc6Cr7sztKuPQB_86DJvzeo2kjNQjXTcXUqVdAYGNzMZ4yq0ZPzwL5_6tdJHp8qDWBYJ1A0vk066YAkPyzH9zzBolnX45ds4pOvbynk3CNlcWav5Bq-c-OMvkaYSArt6QNbVEUcwOMAiSS9_V1kx_-nASe7KnRl3Gy6WTaLYpvn7ve922vqQ3eS9C5y2FwuxPY6yxcJM-0mIXiwmarKCKH29st4Q2rMhLm4nX83NOg-9EJAgqb6rNQ-ijRMQ5pTU5AD-D7np81Nwzafu9uBQscTEHAOpfkpP_LpXT81YgM4Snbm0slu8fE1fEZFXA2CMkd8mhPMnfN4Eg33lWDJfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
گل اول پرسپولیس به صنعت نفت توسط تیوی بیفوما در دقیقه 5
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/108192" target="_blank">📅 17:12 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108191">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b705c5cdea.mp4?token=YwggkLWlvPrgxVe5n1ZuAD0r_af-G_8twlQVUvr5yIyjiVB_Ex2_XXgBKPi8AXbij6ygEhquHiTihjqaaoJ3F1oxnOxE43JTSQBW7d-I6-zh-EdkbDMqMRi_UI80uASTjdNbsM9JXId0PjpTU2igTuFAy-io4n9NcNLmJrNzCR_C-r6n4So-yGAX4e_Di_aGN-d_SCn4Wi5B-ZE3RpnzQw8zu62MLq9ycYDdmeH6EzdRijeAMOrNEnA_DLhT4VZnawEge3hMU0GrBU9nUOMB3ntyTNbtqVLgEgKw66g_3cUl7DDij1BMLDdwL68Vi23tMOqTp09XM8q1hneTAA1pkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b705c5cdea.mp4?token=YwggkLWlvPrgxVe5n1ZuAD0r_af-G_8twlQVUvr5yIyjiVB_Ex2_XXgBKPi8AXbij6ygEhquHiTihjqaaoJ3F1oxnOxE43JTSQBW7d-I6-zh-EdkbDMqMRi_UI80uASTjdNbsM9JXId0PjpTU2igTuFAy-io4n9NcNLmJrNzCR_C-r6n4So-yGAX4e_Di_aGN-d_SCn4Wi5B-ZE3RpnzQw8zu62MLq9ycYDdmeH6EzdRijeAMOrNEnA_DLhT4VZnawEge3hMU0GrBU9nUOMB3ntyTNbtqVLgEgKw66g_3cUl7DDij1BMLDdwL68Vi23tMOqTp09XM8q1hneTAA1pkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
هوادار پرسپولیس: به عنوان یک لر بختیاری از بیرانوند متنفرم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/108191" target="_blank">📅 16:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108190">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74fffee2ce.mp4?token=S3vY9nx13w3X5T61KJ6Or8wlVJekn6n715zIziVUtPHUWZLYLKBW7df4e-2lYx65Lt_8UZpOU71rRR5B3xVjvZN3gMIgew_XoLnWZhoHfNQs51zLXZhd7IO0MLVH4pyUsyD6clAQNzeORhulCGOyk0_2v2QP_8HW0uIJu0-Kv52aeBEYzyKV2RhCHdq3epbkSB_1QlyaaBjKBi5KzNPMR77on0OiC8RhYo6te1HKF2rho3VW2XU90i_KVZAUhVOqEwOUuyvsSdeJ5Wyg6xd4RQoTfkbOV7lv1TiE3mwflYxkuTmksT5LZuk3dAYC6_1ly7N9w9H0pMVijjyJDXXT7Zolk16U77KDP14P0JnocEBg5eJL0PQfztlnbcEu45C5IOnKc9yRDqOas1U3TpN9R1BmrP_Nk1Z95FlZ06fSUYwDkcGkYVDF573KGgm8zT6Uth6Et3TLNjgmkkqbxFxUni9Od8CTwNSmSyk7emBAU0-L_G0UJO2Bqu6pYuCFniOAEK8GNkAZFNgmy-iqSwNQ36to2Dpsqu_U9ZEp6lghRpCz1nB8rvMG8jx8b9Wyo5ljm2l5tePT3rMiQWJEj95vAQ5tdRgfuk8PJl0HSpDYHhLRt7G1akaI1CmmWzR38o5_c5OkqsBe6HxAR-UhH0-iv7OERzafHZIro9Au6WBhX3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74fffee2ce.mp4?token=S3vY9nx13w3X5T61KJ6Or8wlVJekn6n715zIziVUtPHUWZLYLKBW7df4e-2lYx65Lt_8UZpOU71rRR5B3xVjvZN3gMIgew_XoLnWZhoHfNQs51zLXZhd7IO0MLVH4pyUsyD6clAQNzeORhulCGOyk0_2v2QP_8HW0uIJu0-Kv52aeBEYzyKV2RhCHdq3epbkSB_1QlyaaBjKBi5KzNPMR77on0OiC8RhYo6te1HKF2rho3VW2XU90i_KVZAUhVOqEwOUuyvsSdeJ5Wyg6xd4RQoTfkbOV7lv1TiE3mwflYxkuTmksT5LZuk3dAYC6_1ly7N9w9H0pMVijjyJDXXT7Zolk16U77KDP14P0JnocEBg5eJL0PQfztlnbcEu45C5IOnKc9yRDqOas1U3TpN9R1BmrP_Nk1Z95FlZ06fSUYwDkcGkYVDF573KGgm8zT6Uth6Et3TLNjgmkkqbxFxUni9Od8CTwNSmSyk7emBAU0-L_G0UJO2Bqu6pYuCFniOAEK8GNkAZFNgmy-iqSwNQ36to2Dpsqu_U9ZEp6lghRpCz1nB8rvMG8jx8b9Wyo5ljm2l5tePT3rMiQWJEj95vAQ5tdRgfuk8PJl0HSpDYHhLRt7G1akaI1CmmWzR38o5_c5OkqsBe6HxAR-UhH0-iv7OERzafHZIro9Au6WBhX3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
صحبت‌های هوادار خردسال پرسپولیس: اگر یک بلیت داشتم که یک بازیکن را پرسپولیس برگردانم، آن کریم باقری بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/108190" target="_blank">📅 16:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108189">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0df85fa87.mp4?token=l8j1eOV7DRKzy3GDuMDtdmKXiPNc4PAv2eBWGXTVge54lzn8PySLYCv40KdUaURKMUN1LSZCea_4kOhVJzC57K_g49zGw5aBZc0ZQA1uFFs93fgiZsuEW4d4tEizmOuDAesPRyYK9xf_0WL8-EZo2jcKgr3u1m2fIa2O0Y18giN5SjjG8_eBq62qTNF_YSKzhIGkNfbiJVa2LyrxtNCc2R3uPNzhFKgMW2YyOjhtLTNaWwXCw8MsC2HWfWyw3ZkaSNop1x8lzRrzgHKtpP6qb1L_B-rYYJT3CcJ0Ru9G_y2ZAHDnjwQOjjF0WqS9gR0h9GrwVoenz5Ky8sPNZbOAKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0df85fa87.mp4?token=l8j1eOV7DRKzy3GDuMDtdmKXiPNc4PAv2eBWGXTVge54lzn8PySLYCv40KdUaURKMUN1LSZCea_4kOhVJzC57K_g49zGw5aBZc0ZQA1uFFs93fgiZsuEW4d4tEizmOuDAesPRyYK9xf_0WL8-EZo2jcKgr3u1m2fIa2O0Y18giN5SjjG8_eBq62qTNF_YSKzhIGkNfbiJVa2LyrxtNCc2R3uPNzhFKgMW2YyOjhtLTNaWwXCw8MsC2HWfWyw3ZkaSNop1x8lzRrzgHKtpP6qb1L_B-rYYJT3CcJ0Ru9G_y2ZAHDnjwQOjjF0WqS9gR0h9GrwVoenz5Ky8sPNZbOAKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بانوی پرسپولیسی: به خاطر پدرم استقلالی بودم اما زود متوجه بزرگی‌ پرسپولیس شدم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/108189" target="_blank">📅 16:39 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108188">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRwYfhA_LdPGz8zUo0Ux3yC0Yp5zdSeXdg6WWoJRm8mYd8amCvbXu_68LY8i6VBmQ_smR6b1wM9tyrLsBQteggxGfdg76QxBhP9xLw373bZWgDFKHm-IcaOkg4ca8ZaZHCy1QXyIg0HsO-t2pv9TvYsQ5px0A2NK25JOszs1JHTdVk6AERMMon9gx3z1wPg7qTvzueoAfaTUjyfqLSu8MgSp1zwTOY8gsZ5S8gEWAL2u7nV6rwXwXpd4uW7_RgPYDJvMv1GLCxn-6k8dbY-KyIqOyMBf-Zu_ZEn4vM_xE7OlTsfj1ZkyR3zwgRNbhDTLydHLtbT2BwcSXQ2A8U36BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
لیست رئال‌مادرید برای بازی با ویارئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/108188" target="_blank">📅 16:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108187">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c488f1154.mp4?token=GnjRoJ4nVQFWA5jMBQVE4NZ4Pn6URX8QTBlDuT_0SUkldVueKwP1RoAcFtYPUJ-dd5h4Cd-PMfU-dJDiANhm4LB6U0K-2N2Q30c_Upl8SPjtfJuv7M1ibZcAOivnQaOf4Uu2DRIcADXkiwskCSMvtZ3h5rmVb3c59Pr7OP7ESQFaEANxY9WWg3R-6ypM0iEwMRwL9GzeW2JA_f2TLNHfJ_oJpDkBLOZxDFKFodOwVIYuBECiJHwOTkJ7jszOhqDY6HLS2xF_0y5oikKkB4ZDez4UrIByCKTHE5B0wpJyUSjsAKP9cB_L7-NeGpW4Sk7Lm0yhFoTKzWs-YhMvpE0qYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c488f1154.mp4?token=GnjRoJ4nVQFWA5jMBQVE4NZ4Pn6URX8QTBlDuT_0SUkldVueKwP1RoAcFtYPUJ-dd5h4Cd-PMfU-dJDiANhm4LB6U0K-2N2Q30c_Upl8SPjtfJuv7M1ibZcAOivnQaOf4Uu2DRIcADXkiwskCSMvtZ3h5rmVb3c59Pr7OP7ESQFaEANxY9WWg3R-6ypM0iEwMRwL9GzeW2JA_f2TLNHfJ_oJpDkBLOZxDFKFodOwVIYuBECiJHwOTkJ7jszOhqDY6HLS2xF_0y5oikKkB4ZDez4UrIByCKTHE5B0wpJyUSjsAKP9cB_L7-NeGpW4Sk7Lm0yhFoTKzWs-YhMvpE0qYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
هوادار اصفهانی پرسپولیس: تیم دسته سومی هم پول زیاد بدهد، بیرانوند قبول می کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/108187" target="_blank">📅 16:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108186">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f38bccfd90.mp4?token=BpnpG9ml_J_DMqowf7POGvJWhnPv8zxEaSBpApuNfSQ1055qWp4rx533j7yeQAYPuoojs1eZk_zsaDMIVkpRm5ct92W9yHnZMKVGONFE_4q1o9NSCwtkHfvmY1QcT2AmBzuNMznZRURtHd0oAM4VVI6rCRrWgy2FMiXBkaChmrYPtsOziJ0ZuVHV98_ZjYYkbHvHTiKnAxOJbjDdqB8O3XjDHweXkn5Dl-w5RaPCm2YOTzXzOoZuYnDn9VquimBRhtYB5trcLozu1n0kkvm00z3xPNNIrrdSSGGYgt7oRF27NpiG_RW__F47-pMCnxZC3QLXdaddD6yR9s723RdI2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f38bccfd90.mp4?token=BpnpG9ml_J_DMqowf7POGvJWhnPv8zxEaSBpApuNfSQ1055qWp4rx533j7yeQAYPuoojs1eZk_zsaDMIVkpRm5ct92W9yHnZMKVGONFE_4q1o9NSCwtkHfvmY1QcT2AmBzuNMznZRURtHd0oAM4VVI6rCRrWgy2FMiXBkaChmrYPtsOziJ0ZuVHV98_ZjYYkbHvHTiKnAxOJbjDdqB8O3XjDHweXkn5Dl-w5RaPCm2YOTzXzOoZuYnDn9VquimBRhtYB5trcLozu1n0kkvm00z3xPNNIrrdSSGGYgt7oRF27NpiG_RW__F47-pMCnxZC3QLXdaddD6yR9s723RdI2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
هوادار پرسپولیس: جام فصل قبل؟ هیچ کدام لیاقتش را ندارند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/108186" target="_blank">📅 16:22 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108185">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
⭕️
🇮🇷
براساس گزارشات اولیه، مصدومیت یاسر‌آسانی جدی نیست با این حال سهراب بختیاری‌زاده هیچ ریسکی روی این بازیکن نخواهد کرد و زمان بازگشت این بازیکن حداقل مقابل گل‌گهر است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/108185" target="_blank">📅 16:14 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108184">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f4416442e.mp4?token=tWRfUnzDfkiw5AhcFXyUaVXsrih3N3qZd2-fAseQBTjtF99bu9uvgZIocpl9HbI-W-61UZf9wz3lp_NEeZc5C5UPd66W4LcLqaZ55QbpFCyUoSUHVaH1xVli0Jl2Y2P_HiWnbADEUk6mMli0Bk4tORG0bvPzTYGbtFWL-N_LQlsNCQdy_fQ8P9Gap_GKnSMioATBfXNH6EEzRTLwbO8bJXR07EXAjv9Lt9ClsIWvEWpVk0KaVYSRwbYvgNVmIxlzafv0PdppgICZTv7ex_8RBMn2e9G6PwKo1R7bHVpfcdEudeXhBBE41v8uh6CMutk6egDiQ5rJn0S_6G0q99IKgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f4416442e.mp4?token=tWRfUnzDfkiw5AhcFXyUaVXsrih3N3qZd2-fAseQBTjtF99bu9uvgZIocpl9HbI-W-61UZf9wz3lp_NEeZc5C5UPd66W4LcLqaZ55QbpFCyUoSUHVaH1xVli0Jl2Y2P_HiWnbADEUk6mMli0Bk4tORG0bvPzTYGbtFWL-N_LQlsNCQdy_fQ8P9Gap_GKnSMioATBfXNH6EEzRTLwbO8bJXR07EXAjv9Lt9ClsIWvEWpVk0KaVYSRwbYvgNVmIxlzafv0PdppgICZTv7ex_8RBMn2e9G6PwKo1R7bHVpfcdEudeXhBBE41v8uh6CMutk6egDiQ5rJn0S_6G0q99IKgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
کنایه هوادار پرسپولیس به گلر سابق: وجه اشتراک ما با تراکتوری‌ها اینه که بعد از 3 سال می‌فهمن بیرانوند چه کاره بوده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/108184" target="_blank">📅 16:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108183">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8-MZc5PGVlTDA_w_4ol268jWLgUQRI5cmamGO85dvxRBwUrcM6yor-CDJ0PwoTeWS8pzPNl5bUpKidMKJCPhcFRRg-vbnI6KLGq29O5lR0zVX42zYp3NADdZySTzqYGWwlLlxtD47D_3RawoBfpVb8rfttU5FRxo05sxIgS7mjG8pIWPhjmFuTHiP9E2DHoHA9abRjCN-pDVHF9ahKqtriT3aeU6exkflDUX7_4qmf4DMRob7ZBACHABrutYH5j9_tkXUFGI_z2cY6hFUilvWaPICGLtPVBYtZ2d1mYjKkaeVyd5jJZqq33psFx6AADpA4MA27z_85U2-wHTWllyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
اعلام ترکیب پرسپولیس مقابل صنعت‌نفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/108183" target="_blank">📅 16:07 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108182">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a8dae1c8a.mp4?token=oktIQ9VyJv7KBZTccuAUM5BIs3-RbcK6-hxVw0plGDDnYZqDrMRJxQfX7--j3_7eyUiE_Lg3H9RKciMSOC9SN8LgA2lyh-7G7c7mjjDSTXLx24IXfF4sc3vXykyKObbQ4QG_dkYXHKcBfiWKN9tcWYtRrNqBU9aNY6WSwIRw_SjyHsNrrto1QEAqKlzJ55cHiRaz_Wd33inXyxmchzdlZ5muk-bOzCWz2etpmiBo5_B5DhkVksDBO8W2IgcRsBiszRhKDf0epfeeUAHKrKz0Kx9C6BAR2vR3RZ5T_V5SLFkggERRR225mDWfSs34yGisujNmF7wSa3ZVUSjx4gULFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a8dae1c8a.mp4?token=oktIQ9VyJv7KBZTccuAUM5BIs3-RbcK6-hxVw0plGDDnYZqDrMRJxQfX7--j3_7eyUiE_Lg3H9RKciMSOC9SN8LgA2lyh-7G7c7mjjDSTXLx24IXfF4sc3vXykyKObbQ4QG_dkYXHKcBfiWKN9tcWYtRrNqBU9aNY6WSwIRw_SjyHsNrrto1QEAqKlzJ55cHiRaz_Wd33inXyxmchzdlZ5muk-bOzCWz2etpmiBo5_B5DhkVksDBO8W2IgcRsBiszRhKDf0epfeeUAHKrKz0Kx9C6BAR2vR3RZ5T_V5SLFkggERRR225mDWfSs34yGisujNmF7wSa3ZVUSjx4gULFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
کنایه تند پهلوان پنبه هادی‌چوپان به منتقدان!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/108182" target="_blank">📅 15:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108181">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daa24f6046.mp4?token=vGaXmiI7DAWb-OZfWHaN3USTvxO2vq3ywm2Pe7z8BaBTpSS7LebOkT5lpXbnOtvDJhn9-Q8jAczsLK-IG_awE5vKUcziuEzqfn-flix_KRshWGPdany-j9YpbZE9Je5UydkEVDuiUkdxyH4bC42k7JiHZFwqwI3vpMsFX4i2in9ZQgzJDdSbDpbkONsfsR1s4N-5AY9XczDun5qKpm7V3PJWb1Dnho49iugSzBpkdOxH7Ozwk2q1WJ5Mx12pn_Q71GJBLyMSp1ch-81UY9VwdOjASvO0rAeFBkVrgnLGW56sdmvYOApARh6_TlJij87cLSzhIF7daEQHWcxNqfokLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daa24f6046.mp4?token=vGaXmiI7DAWb-OZfWHaN3USTvxO2vq3ywm2Pe7z8BaBTpSS7LebOkT5lpXbnOtvDJhn9-Q8jAczsLK-IG_awE5vKUcziuEzqfn-flix_KRshWGPdany-j9YpbZE9Je5UydkEVDuiUkdxyH4bC42k7JiHZFwqwI3vpMsFX4i2in9ZQgzJDdSbDpbkONsfsR1s4N-5AY9XczDun5qKpm7V3PJWb1Dnho49iugSzBpkdOxH7Ozwk2q1WJ5Mx12pn_Q71GJBLyMSp1ch-81UY9VwdOjASvO0rAeFBkVrgnLGW56sdmvYOApARh6_TlJij87cLSzhIF7daEQHWcxNqfokLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
همچین ذهنیتی برای همه آرزومندم...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/108181" target="_blank">📅 15:15 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108180">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e35d4b3b4.mp4?token=fHssxBy-8NzTDp2mzwEdsjilZFwEFuxFZZXZfF8QzyEHQzCTLh3Qb-ySnTTO9FdSJmXYCv_VIRtp3lvAqsU_28Rhfd-yX87_WwZYpBzCUBwvtolbCUMWeJ67vQFNDEcdK5kWa9jOo8dDU0Y2-cvyipvGCq91Oxqv1hiib1uM_thOyujxQxaNVCC6tlEZ2puaEnYaz2BEEqHYu9Rzg-82jduM-gO9AZjkL91R_Z6YRJ57AnITi94QM1s9KXqci9sidz9g5oUzo8JF0r5Q7UJavY4feHatqbzzwFsZtY-JAnqb62ODs0jIhL1Os1kApD_8xrRk2aEJ0J5CS0WBmuqdEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e35d4b3b4.mp4?token=fHssxBy-8NzTDp2mzwEdsjilZFwEFuxFZZXZfF8QzyEHQzCTLh3Qb-ySnTTO9FdSJmXYCv_VIRtp3lvAqsU_28Rhfd-yX87_WwZYpBzCUBwvtolbCUMWeJ67vQFNDEcdK5kWa9jOo8dDU0Y2-cvyipvGCq91Oxqv1hiib1uM_thOyujxQxaNVCC6tlEZ2puaEnYaz2BEEqHYu9Rzg-82jduM-gO9AZjkL91R_Z6YRJ57AnITi94QM1s9KXqci9sidz9g5oUzo8JF0r5Q7UJavY4feHatqbzzwFsZtY-JAnqb62ODs0jIhL1Os1kApD_8xrRk2aEJ0J5CS0WBmuqdEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرگ صفر زندگی یک
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/108180" target="_blank">📅 15:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108179">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bn9UKuxgFuuC7vbmV-ZIFFUZRGoXXqqMfE6oEZ5UQRMnu3Ep4nW0jwcLuVL6PQ1Y7pfp5q3seihTh2qWBi3MJMpo2PMzDa8TsnGrGB8XMU5iPe0bSePyFFNTkqhwFwUSW9RIT232xwpXyKJrtchqhrmUNrDBEvZx88SPdohhuhNLZ3OF8h6o3gN2kFM8DTjKoglr7Beplp9sjYgxtUnIIKYxZHzFt0xoAksdO0AbLZ05JLfgoFlHu1wmwh9XXmYbAhvQLCkzHVScFGWhGz-YsgTpqhfKTMzNpD6H0cYI6k--YcP6U4gqSDWS1IvEKJlCQSyygaYo-wZKiNhrjGoifQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
🇶🇦
با اعلام پزشکان باشگاه استقلال، یاسر‌آسانی به طور قطع بازی روز دوشنبه استقلال مقابل الغرافه را از دست خواهد داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/108179" target="_blank">📅 14:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108178">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmuqAkAxQesOSoz6qo1gqbnsUrbTF4bsUf0AWGJS77U-7dwxKoQX7ytyJ8--O8wqJ89HgWUAK1DJmbbdTPNqSVccpVz58SnoJhhtlwcQnQnGwqdh12AZu6ZfQE_opmrfd2fC47dZPjdvCal7kNVPaUDhFj88pkVsxdeyKFlMgpR0VWdr_9SaeYP2J_doT9OG4K3HbxVtnBcI9zzaDbJNluqxT7_AAsNBz7MaRJApv9WA34JGUUgFEQhL7vhD6S0u3Wscl3jRqo3MJBwAVjGV-60j7mW_9HGcKgOCHYfCePhgm7pB8dt3beBD_VCDPc3pxn0W5D2s3lt4JXWVAeKGSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
هانسی‌فلیک: مشکل رافینیا جدی نیست اما محض احتیاط بازی جلو ختافه و گالاتاسرای قرار نیست به میدان بره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/108178" target="_blank">📅 14:41 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108177">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">توصیف وضعیت اقتصادی ایران به زیباترین شکل ممکن..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/108177" target="_blank">📅 14:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108176">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vNAsIalj_P993Igz2jkrlUZKqYBV04AqiDcbtcsvahJvGHuwcKZayoba7xbiqSdn5KhK33X0mF_P5Zp-Qr64S_ooaBEP2dWegQ02OqHiy-JXCL6TS3Hb2x7HU4NANlkd0LVdAekJM0owQnp866kWLJnVqpy6fsUjzc3P-zcSvHGnaY4jsQIkvPyraWTjeHtCUWF4ghQDVhbbvTa4VNCE5b80uvX4KBZx2fx4rciiA5dWYy0WUQV7JahLefy3j-j-drHBvwkNL_EPyplp3iQIZf4WRYUNbHwtRCzgi_arqJ-Y5h7vq-UQKYkZ_8EggBzPurxbSfoOk8yd_H98-1dmNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
🇮🇷
استوری علیرضا بیرانوند خطاب به هواداران تراکتور: حرف‌های دیشبم از سر دلسوزی بود؛ الان زمان مناسبی برای صحبت‌های بیشتر نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/108176" target="_blank">📅 14:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108175">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhCnph7vkTDJQ3dE0NMo476zSvuAxfCVKrH6iq4Xf6ExCpYaM2xBnWOfkrCWE3hizhQfAkuWEoMSf3N0YwA5-zgvLYTmsmbs_e789pz1p8u38xkkahQ06rGxnEOPB_XqwDo9Y1QilbnzJ3dO8zodT51X4W8FDF0TynNyNsT3Y8WjXNqkKJR7PADbwTnKfm0UPJRU_O9EeKYK8BERFyGQFSKu5dSTUSbMgSVJK-PACZzlJASa0bN1iOBodEn6DQFBBNdEuI89eY3XlhZzsBQ6OUZ-XtLNqWsCf0anPLFqqRZuxrapYEZJZZwcKI_jb74AMMr0NhBb11VzR9aLQvJNjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
ترنسفر مارکت: ارزشمندترین بازیکنان لالیگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/108175" target="_blank">📅 14:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108174">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/601dba4230.mp4?token=L9Vvys0zVOFftuDTFnZq03Ta4uyJeekBset4IWuy9Lk0vNG2YDYJynUiWmDa73ZM7XbKqODHb5fF3I3EDfshAhrBYrBxc2DEJpflxWnvwjYRlL2uhWCYnhW8psDTs49OJPGaU-qwdsGZXpf-CBIEbeTFR2mjxdLL78xub5OtyjnMHC8gamK28vv0LMNbcUSdxx_ndzrYKscV9uc0fmdR6LDbm6MpZFCxD0jZcDqbam8IxY8X1As03wUPOY3jGOg2fyCPGDjXeNWdmJkDnZ8yl33LGegHceGQxZ6538n5Zj4GSz6MrUvV79nZ7LhkNAzAJBF5-yWUeMeFo2SZH1wR5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/601dba4230.mp4?token=L9Vvys0zVOFftuDTFnZq03Ta4uyJeekBset4IWuy9Lk0vNG2YDYJynUiWmDa73ZM7XbKqODHb5fF3I3EDfshAhrBYrBxc2DEJpflxWnvwjYRlL2uhWCYnhW8psDTs49OJPGaU-qwdsGZXpf-CBIEbeTFR2mjxdLL78xub5OtyjnMHC8gamK28vv0LMNbcUSdxx_ndzrYKscV9uc0fmdR6LDbm6MpZFCxD0jZcDqbam8IxY8X1As03wUPOY3jGOg2fyCPGDjXeNWdmJkDnZ8yl33LGegHceGQxZ6538n5Zj4GSz6MrUvV79nZ7LhkNAzAJBF5-yWUeMeFo2SZH1wR5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
وقتی فساد سیستماتیک می‌شود، بعضی رفتارها آن‌قدر تکرار می‌شوند که دیگر حتی عجیب و غیرعادی هم به نظر نمی‌رسند؛ گاهی آنچه باید غیرطبیعی باشد، تبدیل به بخشی از زندگی روزمره می‌شود و کارهای عادی جامعه دیگر به چشم نمی‌آیند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/108174" target="_blank">📅 13:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108173">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_vS5tRbOd1KrbA8LVc3vcnDUfxY_InEuMx66LJ-CwVkHTLxt8KOovdmGtDRyqzvTqBmYCYKysGW4gnhdYwKIyV7dVqRHpgzuXCG_GEHzdnnfxbO34STVNCSPnYEq1---YAkzS4ShUUX-DhpWgjKAT4uDKBf-2_nx1pRAvIoF0irReajsYnRBKQ-wd8ksbKRMKSM2WVX5C43W1Oui7IcdweG0yLXKvgK7xdsvUZ-OOrZQ9Bj9juAN-xKRAfvWu3q3mGfDIUmZ5udCWiYH6Oe56Yz3KaBpHd9DLuvubIcegMIcNHv_dQ53t39T4KC1kSZWgUD7_aNR340ExRNUy3Ceg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇷
📊
آمار بازی روز گذشته استقلال
🆚
تراکتور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/108173" target="_blank">📅 13:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108172">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❗️
⚠️
انگار ۱۰۰ سال پیشه
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/108172" target="_blank">📅 13:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108171">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6JQ8NYB2h2BVmF6nJnhDKEy8NRF0jm0lG5aGYt2Bs9kdgxRTPp42qb4sWnwOLKDCeGSGhaA4NZFwpojxZ4t0UCijuoW6dwMWDooD7HEyWQ9yEgQi_7DZfw9KqF6HHSCCqHLDje7OITugqWqKT5WhVmYYspkkhXRba3AgIEvGAoERk6_lPzJERkWS5cCXJH1a7P7bcsJapmfomoLyYFmxYDXmEUnLW0nW46HQvzw90HoJEkK-qlXj-KBm4_101FX9wFWl6L3m3OrX9tQ957yms-lfMjohwuVebBA-pYE2BIQnR1T_frfPcsnrX1065TDzDjEhs1wEQ4Dv11VHWlaUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇳🇱
عملکرد ژاوی در اولین‌فیفادی خود با هلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/108171" target="_blank">📅 12:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108170">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
‼️
⭕️
🇮🇷
با اعلام باشگاه تراکتور و با تصمیم جواد نکونام، علیرضا بیرانوند تا اطلاع ثانوی از این تیم کنار گذاشته شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/108170" target="_blank">📅 12:41 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108169">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATA53QfJRtz10z_MsGjaWDDamtPOyCPPSNus6pVw-iGnxCp2Zj9kdcug_adj6HMgzCnUMXMNf_STHgLhUaMH8wF16YXlIdyYu7j4Bk4XPU-Oa7ZdaCiKKDOvgonOU7BkcVwz9ur9jqGSXyxMFSO3zOGGrOYugnqajYjL2zWRVEXse5pX2Zzc3JX9uv4_SWxDRHbpvAJ3Ov1g67Ht1DAA-OKLSvXj81o6418eAlk3v-7pmd17UD6PwC0ZAUNFsp3l4pRi_aw6YqQOn7q4m7PiCj-N9qYrmm3oQPlOD5OAE8JutGPKqnqV4LfKSSos5ZBaxfF3xfrkO5ieznER9yw1Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🇮🇷
استوری جدید یاسر‌آسانی از مراحل درمانش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/108169" target="_blank">📅 12:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108167">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dg9mFMVITCO6c0FFGYMDhQzcHubAnRI6t-RBW73t9RlsuX27QpW3NejRqwufnKOYUcdhW1p5KRVV7OcMqyJdgt9x1D3iRhrZqUEPVpIu1JI_YU5vsclEiZuqTm9ez5ax8jK0_2uaOJAAE5nSBXVp-3uqfi-byqOY3v49MMHbm26f36VDl6EM_DDLcLtx4EubQG6Y67xKqJ94lP_d7RzNldSgJxbuSIaaU9vxJdTfKucBj6XTKqbB6-H5rPLJlaAX8BwBWhNnpNlYNZ-L4T3crAYxKKEWNvgJZ5G6TtWKHEf6w9LVhn0NGr92tOHurv4LFY6Fir-sw6-QIN1rqqIbNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y74f6bqZuzFrNpvxD4Oeev7rd0GcvRBmVxJjJla2Kh7OghTK7FgovaNBXfoOmVh07DrrdVzeGi9uHUwNkjA9e9o4Caeh9jW597k4a2oVe_jHzdIc14EmDdSCz4xa4TcFIb-1WqXg14bBOjXU5jja0K-30zdT56m5vGzhRiFBYb8WfkQBFYDbZv-rumCo4nEW5mvnRG-2YkldyAFNLzFdBAlrkX7PzIbP3h6oGfuGePrReBQxWKFMBNyV6wZfg70QizJa6iRaJjbDUmSISAsHsoFgoF86LuYi7pyf0VI2g3EFh4YVjxbvg8GLHu658xsd7efgpvLt97SDCU4Dn5YeFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
❌
🇮🇷
🇶🇦
با اعلام پزشکان باشگاه استقلال، یاسر‌آسانی به طور قطع بازی روز دوشنبه استقلال مقابل الغرافه را از دست خواهد داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/108167" target="_blank">📅 12:18 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108166">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65716e5170.mp4?token=VQc8_IlEtIAb9fYWCFsjdeCPERoUeLRMBmRXA-NaV_SKBExZXWT1EgWcvrkWNIP1gbYyrKWLYX9zbMgZR_A8L_n_OL5W2ctyXCc0PUhjdMS66e8RKi32BQNyoVzgumFH2xbtDQBLqRdJ8-A1nZZYR0mfqHhRcMySaz2ZXomU372lmLaHsmsuLiZErsqR2Mn_fdYOH_kc_cEQenR00B8uFVcVFCvcAupJgA9OKnDSazBFD8QxSaD_1YNBu1ijUFQVaNv0p5FoqSo9iGpdQ6V5gtQz9a-RXgBaCSR02P1VaqXu_H9KJe89qEOx-ppbu2Z2Wacs5NjI9zIeUmeJgSGaaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65716e5170.mp4?token=VQc8_IlEtIAb9fYWCFsjdeCPERoUeLRMBmRXA-NaV_SKBExZXWT1EgWcvrkWNIP1gbYyrKWLYX9zbMgZR_A8L_n_OL5W2ctyXCc0PUhjdMS66e8RKi32BQNyoVzgumFH2xbtDQBLqRdJ8-A1nZZYR0mfqHhRcMySaz2ZXomU372lmLaHsmsuLiZErsqR2Mn_fdYOH_kc_cEQenR00B8uFVcVFCvcAupJgA9OKnDSazBFD8QxSaD_1YNBu1ijUFQVaNv0p5FoqSo9iGpdQ6V5gtQz9a-RXgBaCSR02P1VaqXu_H9KJe89qEOx-ppbu2Z2Wacs5NjI9zIeUmeJgSGaaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
اشک‌های نیروی امنیتی آرژانتینی برای لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/108166" target="_blank">📅 11:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108165">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e97652f0e6.mp4?token=jL8AhoTzXpoe-vqISjZsLYqaGvipyI4U_1shU3Wpy4mFzcYQDKgcQt-lB1bR6ah6VH7xDr1ytU21rmi817cH7ZN64YMq1FDo7V_5TTPm6b7ucEN01J32pOlAog6NWUynQj30xaHyjI4fko_VBuUCTi2e1PR8tWHb4IEixu2aJD8d2-qi9Ef4pa_FFVfrMm_yOg8OtlzBP89Dgo43LFYQiIb_t4MdKHv6mv1cucYAUYuQOEeVJzw7qDOZs4VNtzJrZSIumBUCmm9hgC1e0YRLHX7kJlbCbpqVJ2DTK2M255R7jIdIcTv3GgR4CFRqv6zacG7xtFuLgmYzDVyH_NYnug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e97652f0e6.mp4?token=jL8AhoTzXpoe-vqISjZsLYqaGvipyI4U_1shU3Wpy4mFzcYQDKgcQt-lB1bR6ah6VH7xDr1ytU21rmi817cH7ZN64YMq1FDo7V_5TTPm6b7ucEN01J32pOlAog6NWUynQj30xaHyjI4fko_VBuUCTi2e1PR8tWHb4IEixu2aJD8d2-qi9Ef4pa_FFVfrMm_yOg8OtlzBP89Dgo43LFYQiIb_t4MdKHv6mv1cucYAUYuQOEeVJzw7qDOZs4VNtzJrZSIumBUCmm9hgC1e0YRLHX7kJlbCbpqVJ2DTK2M255R7jIdIcTv3GgR4CFRqv6zacG7xtFuLgmYzDVyH_NYnug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
صحنه‌گل دیروز ذوب‌آهن به نساجی که به شکل بسیار عجیب و نامشخصی توسط وار مردود و باعث اعتراض شدید شاگردان حدادی‌فر شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/108165" target="_blank">📅 11:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108164">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41de558131.mp4?token=Rkrhw6fs21G5-JW1mJSGjLJUNy-eN_HfheKmR5uT0xJn2XFFRMY5pipz6qflgKQqcAnlRlhxkWfV8iJGMUOcBs4Uwm141Q7KT2YPT_tDUU8kGQcZo_iQ5Zsg5cR_4u6cIIHOEnjFyg0bOyqcuKrbUVrWEz_M_J8UlCbO_A5zELHEMej0ef5xpzpQ1j20pJu1_TKWCp8HBgdnEwGE_cGuf-Ht1CLTDfHTcAJ0wX2zytCa-Tm2snW6qibMA94Hbew48A25PQewwET94LNJ9YJXnpxS20GSIR1sk0sYGDYAJQ-evCoyWbM7-3eAhiKMqIigjmG430BIIhLAf70M6zTF3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41de558131.mp4?token=Rkrhw6fs21G5-JW1mJSGjLJUNy-eN_HfheKmR5uT0xJn2XFFRMY5pipz6qflgKQqcAnlRlhxkWfV8iJGMUOcBs4Uwm141Q7KT2YPT_tDUU8kGQcZo_iQ5Zsg5cR_4u6cIIHOEnjFyg0bOyqcuKrbUVrWEz_M_J8UlCbO_A5zELHEMej0ef5xpzpQ1j20pJu1_TKWCp8HBgdnEwGE_cGuf-Ht1CLTDfHTcAJ0wX2zytCa-Tm2snW6qibMA94Hbew48A25PQewwET94LNJ9YJXnpxS20GSIR1sk0sYGDYAJQ-evCoyWbM7-3eAhiKMqIigjmG430BIIhLAf70M6zTF3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
هاشم بیک‌زاده: در تایلند اتاقمان کنار استخر مختلط بود. دستیار قلعه‌نویی نیمه‌شب رفته بود لب استخر و دخترا را دید میزد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/108164" target="_blank">📅 11:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108163">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwzBWS-7yVTOGXgRdBcHEGhGBh4mLHBCTPfK793eR_GfFiKf6ry_0kJj4nEQqePxlsC00wXcjEyM-L75Qo-OPGiF9Ud6nFgRVNZZthqbTNTW8bHeYt3d05vouNvcW_8bbcdCyVs5lT_08uQdP9BoJjML3vPEtLPcsOvBG3t5mtY-VzsyLv05oCY93bqBkr0HV_sKuM0dxuGcz8NjVCrTVGm1G5XrEKILZ7HEVnYVHox5I7bJn2ao4kRnZ7_iCYzAWemUXBoiwL6AYalDv5IcY6QIJVyqOqsQRQieejdDJNZNCJnDh81UHfsvxKla8xP1tvrIrKm6JuMlIdVQKKQJ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
علیرضا بیرانوند اعلام کرد که از کریمی مدیرعامل تراکتور بدلیل اتهام تبانی شکایت می‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/108163" target="_blank">📅 11:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108162">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b39729529.mp4?token=WXmGO_R_-YwgM_ncSPX46MQxhCXsUzrwTNG7VwKoTSWfL_vIZxC6OoqM7ttnSj5NmMdIngLjALS45PMh650qHXualoGYEJXsq0E0THFmaqxU2o9C2-Ko__OcKk2OFUKVQ8dPMMT_wUZmxueRZPggOoDMHa_11UFHk8IlXzJurFWbC-8KVEf4wtaVs4nzeA9-zC4kSBGuLcXVvzH6BMU1mud9Fvqm35SsM6bMHLlUHkRGZ6yHSJ9AKoap_O5AKNXvBdrbxjCmUelaZ2Ot7_SvKscXR11ze9LXAyh7Gp1DpwyADuAEMo7EAPHVJEeKWl1tb2dN03V4NPhZ4U0MmwdTx7QmE7Sdghl8rIX2Z1RUuNIUAtbaZ6zfwN5g6jIWbLf6DhjZr-Z9W18Z4OblsOSwHPBrbTiKzA-4y1n-oizg0XoiPmQycS6KxXcg2u2_6GR3wfkMEC2ru4Dgi8_1OhtStJddxnTJEJOlVjOJ7s__pNVLjxnUnpLbs9QNK2Ycy30v-fs0Iy_z7IAcVh-K-HlSwZt38gaJEb_E6ZZODvGXSttvuFs6DlwIdAXdiEjg-n1J5g161MJhJrix4Z3fXBtxrhPfmGgnbeh2iBOXC2BzYCMd1Wp3VDd_xc5Vb5rX76GVaCbeVIzjWH7KpS0XktZPiN9lBk2XFeSvW8YP75JEg5E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b39729529.mp4?token=WXmGO_R_-YwgM_ncSPX46MQxhCXsUzrwTNG7VwKoTSWfL_vIZxC6OoqM7ttnSj5NmMdIngLjALS45PMh650qHXualoGYEJXsq0E0THFmaqxU2o9C2-Ko__OcKk2OFUKVQ8dPMMT_wUZmxueRZPggOoDMHa_11UFHk8IlXzJurFWbC-8KVEf4wtaVs4nzeA9-zC4kSBGuLcXVvzH6BMU1mud9Fvqm35SsM6bMHLlUHkRGZ6yHSJ9AKoap_O5AKNXvBdrbxjCmUelaZ2Ot7_SvKscXR11ze9LXAyh7Gp1DpwyADuAEMo7EAPHVJEeKWl1tb2dN03V4NPhZ4U0MmwdTx7QmE7Sdghl8rIX2Z1RUuNIUAtbaZ6zfwN5g6jIWbLf6DhjZr-Z9W18Z4OblsOSwHPBrbTiKzA-4y1n-oizg0XoiPmQycS6KxXcg2u2_6GR3wfkMEC2ru4Dgi8_1OhtStJddxnTJEJOlVjOJ7s__pNVLjxnUnpLbs9QNK2Ycy30v-fs0Iy_z7IAcVh-K-HlSwZt38gaJEb_E6ZZODvGXSttvuFs6DlwIdAXdiEjg-n1J5g161MJhJrix4Z3fXBtxrhPfmGgnbeh2iBOXC2BzYCMd1Wp3VDd_xc5Vb5rX76GVaCbeVIzjWH7KpS0XktZPiN9lBk2XFeSvW8YP75JEg5E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
صحبت‌های تامل‌برانگیز مجتبی پوربخش درباره میزبان دوره بعدی مسابقات آسیایی سال ۲۰۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/108162" target="_blank">📅 11:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108159">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f27270d1b9.mp4?token=cvLiTssSNgfApRvaEE71N9cQD2FfI_F2olaABqs0tM9Vg7kuE95ZiIRLMaPzCsSJcfFO-uZrSj036L0icgFV_EubXUpU78NTmWq0rb2lQYJJbS4WKgre1as8zlCs49SWvayQeEOtlv8rm4Fh5HsdbNEQ5PBLdJzLDRAbWKNeBEX9MSW92bQX7ajYwKwydpn_70MoDevItuEmIqT3kfCDD0WVLSnWjGOlH7jnTBDCnYbL172XMDs6EBfaF-01U6I41HdJ9ps-mSfWvXn316xl0u_Y687mwP4M6yXBz_pYwN_8cESEy7ZzMM7lTOfNYbh1G_OdZlct3ravAOZHkMCAAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f27270d1b9.mp4?token=cvLiTssSNgfApRvaEE71N9cQD2FfI_F2olaABqs0tM9Vg7kuE95ZiIRLMaPzCsSJcfFO-uZrSj036L0icgFV_EubXUpU78NTmWq0rb2lQYJJbS4WKgre1as8zlCs49SWvayQeEOtlv8rm4Fh5HsdbNEQ5PBLdJzLDRAbWKNeBEX9MSW92bQX7ajYwKwydpn_70MoDevItuEmIqT3kfCDD0WVLSnWjGOlH7jnTBDCnYbL172XMDs6EBfaF-01U6I41HdJ9ps-mSfWvXn316xl0u_Y687mwP4M6yXBz_pYwN_8cESEy7ZzMM7lTOfNYbh1G_OdZlct3ravAOZHkMCAAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
✔️
🇮🇷
فاطمه‌احمدی ملی‌پوش تکواندو که در ناگویا مدال گرفت: شدیدا طرفدار استقلال هستم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/108159" target="_blank">📅 10:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108158">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23161a114d.mp4?token=dQJKsVw0XY6npXhbIu5VvotLIZ8T75EaiifyhiTda8CPhy2UYg-INmWjS_d5eGo7D4PvkNonS8Wf7Hb8UrzJBp9Vs7yaojPmQk3B6Ni9UKPYvxqxszHJn92dqoVCga0l8CumgWH_3Tebx1TRLp_q8Le91ukLBmPry7DDdZKc8EPiCjy23whAy5kMmHNfzJ7vGGQ75y8ylo1LVu9iyyfNjPRLMIB0fHLExEYBISkeAT3GMWq_VeNW5erQ7PBGYq2JXYBu2e3Q44mKKw2V4jC-fw1_45vt5Q_T9YIjrYm6jl46ZiAeZloncpfDqIJ6E098Dt_KLxndaqS-SflQocI43Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23161a114d.mp4?token=dQJKsVw0XY6npXhbIu5VvotLIZ8T75EaiifyhiTda8CPhy2UYg-INmWjS_d5eGo7D4PvkNonS8Wf7Hb8UrzJBp9Vs7yaojPmQk3B6Ni9UKPYvxqxszHJn92dqoVCga0l8CumgWH_3Tebx1TRLp_q8Le91ukLBmPry7DDdZKc8EPiCjy23whAy5kMmHNfzJ7vGGQ75y8ylo1LVu9iyyfNjPRLMIB0fHLExEYBISkeAT3GMWq_VeNW5erQ7PBGYq2JXYBu2e3Q44mKKw2V4jC-fw1_45vt5Q_T9YIjrYm6jl46ZiAeZloncpfDqIJ6E098Dt_KLxndaqS-SflQocI43Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
فلسفه جالب نام فرزندان لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/108158" target="_blank">📅 10:15 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108157">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c50646a3df.mp4?token=J0JlVGpijDJ87g_pN8ckbNGDlEww_hUhMBBLpfh5QEVwWfXQ6AvkS11lhNyx3yJ58d8vbup4e9OI-BQIPias84_0W0xHt-LQJiJRdXuFbBxIX1tXz2T7-VZFqRepbTulck0HfOxYbRIL2UMm35k7m9funOaLP9F1a5S0j64E590BC1N17OVSTVdVjPykKZc98CMJjg-4oZlh9NNfdJPxPeCLn1S7iktaF6lE1JZOm2nIeO_9AFf-qakqlpOWRwT0z7gOanixqNnRHLCWsNDgJ_D5FH3kMpF3xBiBhtHZFFe9xUnQ6NzyLl51Zom_bQw9VZhH6-AXlAjySj3oWqlKaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c50646a3df.mp4?token=J0JlVGpijDJ87g_pN8ckbNGDlEww_hUhMBBLpfh5QEVwWfXQ6AvkS11lhNyx3yJ58d8vbup4e9OI-BQIPias84_0W0xHt-LQJiJRdXuFbBxIX1tXz2T7-VZFqRepbTulck0HfOxYbRIL2UMm35k7m9funOaLP9F1a5S0j64E590BC1N17OVSTVdVjPykKZc98CMJjg-4oZlh9NNfdJPxPeCLn1S7iktaF6lE1JZOm2nIeO_9AFf-qakqlpOWRwT0z7gOanixqNnRHLCWsNDgJ_D5FH3kMpF3xBiBhtHZFFe9xUnQ6NzyLl51Zom_bQw9VZhH6-AXlAjySj3oWqlKaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
کنایه ابوطالب به نحوه برخورد بازیکنان آرژانتین و پرتغال با لیونل‌مسی و رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/108157" target="_blank">📅 09:50 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108156">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9a44b2ebc.mp4?token=l7VGp0XnBLbUcbySeGEP4B6Xt-UhjhuQIjjqG95jFqvOyeeBFJKs1Rjo25aLIIER87rEpkKdteWKQiQXWMCJPVhftNeXPuO-8yLlbruEZvXFWndnjnoNPFh4uAS48XHH38oQS7f_suha_Aa7-VY15SWtF22TM_FTDncl30auC2FItyYDgdtVACk-nkGUlykXUEJM850Xg53Bfixp_4trSWYx8h7mXQzfc0Y5OBZPVD3iSYwZj9LO11OS-TItKnkX0LkrYVqsJzBvLdPQ0FMdMQ-49GfUYKpHJQXCiyrsC2V1gtGzEI_M7eioeplE8IXbEgvs1djIMuAkH8yP-l3DKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9a44b2ebc.mp4?token=l7VGp0XnBLbUcbySeGEP4B6Xt-UhjhuQIjjqG95jFqvOyeeBFJKs1Rjo25aLIIER87rEpkKdteWKQiQXWMCJPVhftNeXPuO-8yLlbruEZvXFWndnjnoNPFh4uAS48XHH38oQS7f_suha_Aa7-VY15SWtF22TM_FTDncl30auC2FItyYDgdtVACk-nkGUlykXUEJM850Xg53Bfixp_4trSWYx8h7mXQzfc0Y5OBZPVD3iSYwZj9LO11OS-TItKnkX0LkrYVqsJzBvLdPQ0FMdMQ-49GfUYKpHJQXCiyrsC2V1gtGzEI_M7eioeplE8IXbEgvs1djIMuAkH8yP-l3DKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معلوم نیست داستان چیه هرچقدر هم ببازه بازم از فدراسیون پاداش میگیره
😂
😂
☠️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/108156" target="_blank">📅 09:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108155">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‼️
🙂
سرمربی فولاد مطهری: داریوش؟ گرشا گوش می کنم، وسعت صدای ابی را دوست دارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/108155" target="_blank">📅 09:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108154">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77201b62ab.mp4?token=uHY0OOAhKLUU0Y-xMVwNAvc8o4beGnFcW5cCjFdsPGl-MK4p9SrfNPVSxi9lnnYsxC8e_dsDSP5lp9Cjhn4LYv8EF1TO4ZLw3e-vfnXdoVofvZE3YiRMmNu9LLS7F1xYHwvJ-YYZ9CGyOJI5ucibFLGgYYsmKcilOuTXPJYacfryLKgLAE7VFL3GA4C95VZDPtOXYw7GGq5PrsEAJSe6kjIpdoZtbTCdTLzJKxoR79zWEYQmO_pvkVD36MHdvJTIG_lW1DnE3MVC5N5hrKAsmuWWhIGYYHwNsVwqo5weFrYhk5-1Zhp7ZTUEmH9FzOjONRchrDUJOtsB1TzsEAjY7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77201b62ab.mp4?token=uHY0OOAhKLUU0Y-xMVwNAvc8o4beGnFcW5cCjFdsPGl-MK4p9SrfNPVSxi9lnnYsxC8e_dsDSP5lp9Cjhn4LYv8EF1TO4ZLw3e-vfnXdoVofvZE3YiRMmNu9LLS7F1xYHwvJ-YYZ9CGyOJI5ucibFLGgYYsmKcilOuTXPJYacfryLKgLAE7VFL3GA4C95VZDPtOXYw7GGq5PrsEAJSe6kjIpdoZtbTCdTLzJKxoR79zWEYQmO_pvkVD36MHdvJTIG_lW1DnE3MVC5N5hrKAsmuWWhIGYYHwNsVwqo5weFrYhk5-1Zhp7ZTUEmH9FzOjONRchrDUJOtsB1TzsEAjY7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇷
عاقبت تیم‌گرفتن با رانت و فشار بالادستی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/108154" target="_blank">📅 08:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108151">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEeQSemrP94hWBVlz9jVvBuxzsS9OWnwFUaWBzi3aL6z7NWLlgF_ubGVoyDY6HorLVTdRA7kHyc_nR6z_2zRY6U9H1cqh7fEboIq6WgYPbg1bi2mYSrA--m3huTmHA1B6EJJOWu_Qk1ZQTyhbYmDuFWAXUZhCoiTkZNsG_y2aKwOn_OvdQNbx3hvOKM90HCtwR8OboXhbj6URCiqvOxH2gulS0safZ6TMX6crsQJP493y5BM6NK9ws-2Ous57vC6fyg4MyC-U2ZV_dlTiDGoR2wiaf8e0V_3VjmE--ATqnzydaNZNu1vkMLD7NC5WqTlvAsv4hNRXfDryTd0ugyohg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🇶🇦
نتایج ۷ بازی اخیر الغرافه حریف استقلال؛ 5 باخت - 1 مساوی - 1 برد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/108151" target="_blank">📅 00:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108150">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa5d1caab6.mp4?token=p41t3o9c8aWAv-3u496-zlC8OurDrmy2b7wlczyH8ULfa2XWVYdAncn52QRRT5dJLXp4WuxzlNbhAMzzWsWC1Ys1HpB-bPBFJ8on00A1pZyDdduo4lqOqI3zP81rymtNi__4TlP4rX6-_z7avgyk738WHaZnSNBGKMrMF6bXdgH2ElYMsMQFKGttIxWgwHnkxgi8hvKlH-BF9XK9K6fGhg7Zp-K6lO_VfS1OCmNDvggW3BYYqa2KZaBeC7pQXSIIZ1nbe7x5Of2ajJKmL2ho1YmoiHNNeUAt89-AlzdylmF26A3ylN4F_0lvwiB5kK4M_H3ObWKQB8XchT8x3HFMJYdCq5FyFZa_q1qw5WgdGmmKGGrKRk8TxOAnmCcDeztkNB2Fd_kEGD5YmQDhJ-DSsCU7hBxza8KD8PC_2lI22JFcV7qPd9XrrpG-D54P2wTC17bM6WeHyWwglVWdn08QeXBB8psNC6ZPyRFc_W-NMm5x39bfMDPUs7YlGK_1eYz3jjU3JFdETYNbzvQsbrH5r2DHGabkccMXSokKI6m-dvYR73I_nEtzNtHda9fxua_cKmNtoTd7v644_Arf4h2lTnMapWfYyTJOpgLVg-sK1zkZTrG4S0k-LhagG0A3gYZHvVAeDQS4Hq79VdO-kKnNJxpl4WQGaNaZkXd9faRdxV0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa5d1caab6.mp4?token=p41t3o9c8aWAv-3u496-zlC8OurDrmy2b7wlczyH8ULfa2XWVYdAncn52QRRT5dJLXp4WuxzlNbhAMzzWsWC1Ys1HpB-bPBFJ8on00A1pZyDdduo4lqOqI3zP81rymtNi__4TlP4rX6-_z7avgyk738WHaZnSNBGKMrMF6bXdgH2ElYMsMQFKGttIxWgwHnkxgi8hvKlH-BF9XK9K6fGhg7Zp-K6lO_VfS1OCmNDvggW3BYYqa2KZaBeC7pQXSIIZ1nbe7x5Of2ajJKmL2ho1YmoiHNNeUAt89-AlzdylmF26A3ylN4F_0lvwiB5kK4M_H3ObWKQB8XchT8x3HFMJYdCq5FyFZa_q1qw5WgdGmmKGGrKRk8TxOAnmCcDeztkNB2Fd_kEGD5YmQDhJ-DSsCU7hBxza8KD8PC_2lI22JFcV7qPd9XrrpG-D54P2wTC17bM6WeHyWwglVWdn08QeXBB8psNC6ZPyRFc_W-NMm5x39bfMDPUs7YlGK_1eYz3jjU3JFdETYNbzvQsbrH5r2DHGabkccMXSokKI6m-dvYR73I_nEtzNtHda9fxua_cKmNtoTd7v644_Arf4h2lTnMapWfYyTJOpgLVg-sK1zkZTrG4S0k-LhagG0A3gYZHvVAeDQS4Hq79VdO-kKnNJxpl4WQGaNaZkXd9faRdxV0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
🇮🇷
مارک‌کلاتنبرگ کارشناس داوری: هیچ پنالتی روی یاسر‌آسانی اتفاق نیفتاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/108150" target="_blank">📅 00:18 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108149">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
⭕️
🚑
🇮🇷
براساس گزارشات از رختکن استقلال، مصدومیت یاسر‌آسانی جدی است و احتمالا حداقل یکماه از میادین دور خواهد بود. باید تا انجام معاینات پزشکی و نتایج آن منتظر بمانیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/108149" target="_blank">📅 23:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108148">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kG_M3kKt20McDE4zM2hJVFGe4rsRxQxozjfit2C9g434sh-u7EASMFfCmfRCPUoWUsNzw-ABtyvcQySLapvRA8RFvgSbHf2O8XwjWbB2j6zYOObJsM6Wnn0R7QX_hvcjV1A2usav8QC9oagcvZzkL3GausY1JmSdtZmJMXCQZnbREETlclV-T9-bOF_oGv_2hUuQ9pKS0D-ehTUdSqaQTs0m3zDpY1lRG7t0eBKhU-yX3I3HGKcVtImfFzRG4h8fivDoZV3YXD7i9ic1CbxDL9942MCzbVGOtxl24IyCEXMDYTYoKL4dEct7QTiWkkGmw499a6FZgpROODY55LexFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
اسکای اسپورت؛ مایکل اولیسه تنها در صورتی از بایرن جدا میشه که به رئال بره. اگر مادرید پیشنهاد جدی ارائه نده، او احتمالاً با بایرن قراردادش رو تمدید خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/108148" target="_blank">📅 23:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108147">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UwQyjkakpm7-mMDHA2ObmrK8K2PTWCWBlqnPYLkqM1V6jeDjr-Y3w0bMXaL3g49p71KbWwJIQBmOhBAJkzDvI0Z-YXue4p4mAzzL0cUKVDfzZkKjysAJVVp8OrRU1FzRftbNC_b-AWcBF7oPGrEL8B7-6qr-lphmEnQFxkifbxWRqdvsHvbRskiCHs5vRHBGxQ9p92bCByUkZwom_F8_9NAM4_BfBAaZP4UyTPWzmqRLd5911kCv67pEPJpknuI_DJKr5L66ostgPshduKh0hRO7r0x8To2TzdVxrIp1dWaRMEYebkxvYpOpYbGVVscvLpcGQDui0b5H9aq2izDWhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
⭕️
بیرانوند: استقلال تیم بزرگیه. فصل بعد بازیکن آزادم و یه تصمیم خیلی بزرگ میگیرم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/108147" target="_blank">📅 23:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108146">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwsbCzN8gxPOxK_VxdmII6HB_CtZm83Jdsq4EFsqYkwkqij6PFf_jXauJ8bpD2S9VggZkF-2iNT3u3rgOTL_gaYdo9eKu1KofUUTMtDfa7fh6juFK3APU-vzGtCBixf0Q2l2zNFHIs6x-6HsYkbWabJ3KzMmXPocqDlJYOsZjOSR-oE_lvvftOnnJ_4TXb__3gvAdUGQlF4Cf1Axf4hbcxMxOtdjSYMUHebPslLHs71SEBVf1TVdP08guju8DkGVA8CLPPmRMt7DjciZL47-gXtWIe-fGeiG9Gq4UlVYD1Beb1iQrWXjwGjVATPMF4wf-JM6u_9ylm4-PbgTw_E_8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
👤
کنایه خداداد عزیزی به بیرانوند: اجازه هیچ حاشیه‌سازی را نخواهیم داد و از زنوزی بابت انضباط مالی قدردانی میکنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/108146" target="_blank">📅 23:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108145">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/109c5cc92a.mp4?token=ei88JiheapOdO1eJiVCQjVc2iQMwYoF7qENVS4cQ2Oq5SG5xt4bGSPMU_9OYETFi4YKMVcQyl-s3X4WOGtbK7Gxq7C4qdL3LrSKReZfOTbXH77pHHmUjiP5gm8ahtW2ZiQS14Syw910qtdTDDkz7SNxMneWu42mXupr1-9z4Qd8MWrYc8YbBQYtufPDof5TgBbvEwQUa2Jr61SMh46l8oD_sUAfmky7Egp7S10nU1hYbxVaU8bEeTKAkYez_c42jzJPS8vVbRtCDVfFmfm33SQyaSRjlFfg-39iuXqpad5YIFNuHk5swtnFVjhPjIH0OiHYpwwanDDw4rPAERDfnkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/109c5cc92a.mp4?token=ei88JiheapOdO1eJiVCQjVc2iQMwYoF7qENVS4cQ2Oq5SG5xt4bGSPMU_9OYETFi4YKMVcQyl-s3X4WOGtbK7Gxq7C4qdL3LrSKReZfOTbXH77pHHmUjiP5gm8ahtW2ZiQS14Syw910qtdTDDkz7SNxMneWu42mXupr1-9z4Qd8MWrYc8YbBQYtufPDof5TgBbvEwQUa2Jr61SMh46l8oD_sUAfmky7Egp7S10nU1hYbxVaU8bEeTKAkYez_c42jzJPS8vVbRtCDVfFmfm33SQyaSRjlFfg-39iuXqpad5YIFNuHk5swtnFVjhPjIH0OiHYpwwanDDw4rPAERDfnkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🇮🇷
🇮🇷
در اتفاقی جالب و زیبا جایگاه هواداران استقلال در ورزشگاه یادگار امام به صورت مختلط درآمد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/108145" target="_blank">📅 23:15 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108144">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdXQlSeEKTVsxCQlxmoi-3hg2Ft-QV9Kuv07LGkXkN1juQx1QXeBnBPNjPwEHIhBqtorjRU_wI69jOw-oRB0B9nqsgc87XPxFuhFWqPegK_uFRGD5Pu6RbURVgdPnXNzJOU1n5bCiA7JQ1l1DUDoq92w0WPDrYuEg7xVDgOkjYiiF3oZw2fgd6k4RMVnvnHVMnNgAfIxnTsworJH2_FxMl05f072M8dpUbf0xBy9LxHOnJvDvzrMxTIXdhTouRlXzKlr28eIvphEU_kj4qL6bWcTCltQFMVpw8nR8N4cuLeXgELm-JDSma5He4vp26NJ9y7icqXCkTpsxxiJtO_97g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
مورینیو در پاسخ به سوال درباره رابطه‌اش با داوران: فکر نمی‌کنم مشکل از من باشد. فکر می‌کنم مشکل، بدشانسی و حضور در باشگاه‌های خاص در مقاطع زمانی خاص بوده است. من در اوج دوران نگریرا به رئال مادرید آمدم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/108144" target="_blank">📅 23:10 · 16 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

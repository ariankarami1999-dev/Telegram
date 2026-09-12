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
<img src="https://cdn5.telesco.pe/file/g_T0J-9oMiFcHbOwG-iYQulyaeUCybY1nE82xIt_tUkMj_r4eHzPazEr5xgPkYhn1JLFqjMeDo9Eh0n-sw_E8QlSzveSa2Pilm6Q3sCLlNv7CJbh6s5TkOWCOWhefuJ2nwET6MnhNfxLvikj61SWjECDsYynS1wrBcJeDCzUCTkBDsAWC3DUO3m24YubEyb3Q066zMIL2_O_n1rWI8xieTMgkIc9s44oIihAJ2Xqvp-TSWpTr-avHQsbrHoJ-832feQcRYHdUMwANZvLsIeQ6yFPRCaLEc-q68gypUo8-L1LniEHwREvxG1i2rYRoh2RkYa2FUvuHyba1_UNo-JG0A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 416K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 20:48:51</div>
<hr>

<div class="tg-post" id="msg-106296">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBo172705bT2zbV0Sj3F0KKht0mre5b3H_I_9HrGxMff-qh45L5GCMDQA1h_kzQyeYJIIZ9DyVGttkE6RXORYWUu7fG5kkVtdoriE8tVbiwZHzpnvHxuOVfdi9IP25rFRvcoHheZK0N3e6iSgfBEsBHbtQZyz36FQut_g7lRoJe52rTIdRBVAYuVVDttXDbfCrYiUantaILz50d50_k88UflA9emDiuDvBE0F1PubWHDiz8MZ4Xb9qUowB3IjYzhcC7EFVxIWzHCuBh2M7x4lIbRI_xqBEWEUjh7Y-jN2irorCQme3SQAzGbz5zTHN9KIxTgB3Hgxxua2DQEXaqBWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇮🇷
🇶🇦
پوستر السد برا بازی مقابل استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/Futball180TV/106296" target="_blank">📅 20:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106295">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOz2XwwmDJ3RUsTlnoJA0sFDpuSwjCpne0vR7WALwLZ7f4_J3H6mvt-rDbF7a9N9BuJP0zzIYr7AxD1IPn7CIyMNoE3-bkPy_-o_0z758IP63hMj1MfnV9zrOlB786PoL4AlA85Co94dp9zcNo_1JhQk6mvbBRBkjtq-gyJtV0hp2i_e1qATNpNZ1sSCO-_j_qBYpfB5CFMcM49kS_-Qm4ns0RIQqKnkkzz8X7lC0Q6vT-4s_YWPQQ9bBTUq66MIQAzDkz7IGeaMVgMO0wp5fMMxvuPMWK_NMgVPwJX5EoLmt_3amb7MCOhQy5WSos3D9FPdlLt9MmAaFqOelFPI0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
😱
قیمت PS5 Pro در ایران به حدود ۳۰۰ میلیون تومان رسید
🔻
قیمت کنسول PS5 Pro در بازار ایران به حدود ۳۰۰ میلیون تومان رسیده؛ در حالی که این کنسول هنگام عرضه در ایران حدود ۷۵ میلیون تومان قیمت داشت.
🔻
یعنی قیمت PS5 Pro در مدت نه‌چندان طولانی تقریباً ۴ برابر شده و حدود ۲۲۵ میلیون تومان افزایش یافته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/Futball180TV/106295" target="_blank">📅 20:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106294">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ReveQs77sKCxVIKZ3fpffNtNJNlu53is-4qP1c_wymw6R8gKmY3eubVAocIu275wk9Ie9BWqHG5aMuTVd1vI02Hp4W75vecp4NPQEjoBdGqUwvZjXFP-HwADNDO4zYfob67irFioBy-uaBos2ntYKLWoGaMY1jDWG9WXIwf332YC58yFxcgELqX1W-MwhU7c02CX6E6nbeZA8xowGskgwgGlJKbMA6xIZhlw7V0Vrs1DwQjF7aOxup6aK9sxWnc_5yD1uGw3o7kLuGy1HgY9MM7Ecc9GztvyCbVzXI5zwsrEqxHTz0YqyFUrZob-IQphfu2Cj7Xpzip1yfyJbc4HzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
ترکیب النصر مقابل الخلیج با حضور GOAT
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/Futball180TV/106294" target="_blank">📅 20:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106293">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMUmauHOnW9KsuTduB6N_khWFkDVx8OMEpLcT-V69UiaDaGoEI1FRMLJC_bV8zhfl2vjU8g1NTKmnAuMwo4qbw2ZPaAjfvSwwf5K60WA7ILThBa6kUrBME2a0Pzt2ED49xu3CcOr1104LxNv-gLOYzmoD8sgweEGie0glwVIaV28pymOWFOX4-Al_v1_-1TpiuAsl0EJEZngVxePtoJbRRQGJdBke9sHyhmHU36fBrqSAc0wpDuWqvjgQmrEO-bB1USuUou8x7TqWVoK-x3hUO4Vw5Hak--zsc93ne4jrvfoBdBPrRLcjEiKV1Jc8PP4H2Lr5JrDrT5rH-q_OaZtSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
🇶🇦
استقلالی خبر جدید براتون اومد؛ مارسلو بروزوویچ از النصر به السد پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/Futball180TV/106293" target="_blank">📅 20:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106292">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
▶️
صحبت‌های‌جالب یک‌بانوی ایرانی شاغل در آکادمی باشگاه چارلتون انگلیس که بسیار شنیدنی و جذابه. حتما ببینید از دستش ندید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/Futball180TV/106292" target="_blank">📅 20:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106291">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/045726ccbe.mp4?token=BTfYLBLNZZ3nzqTmxR7M5KeBrIL6zjJcCs2NhDkInU4-_8wDLjD6AnaalIwUEV6HmIbqzWfBd0D9kd48kJLEe1CWNVZI-lGClirusRIG61XhpM8m5tyoAFXSY3gGSbTcoExecpW5vAPwtiYJUUgF4Cp1bOsD8_YhJf_PcGB6tfvoSJSeg3c2_2kVpAJ1VWqStWL6UvnDTnikYWw4rHbQSYJYZMpqpPnocfDijBm7mf2R-DSepvds99PgrpH6D8gQ3tKuxgShyb2To_l7Q8O41QKo-o4TLnBtw-cmQin7G36uS8Lj_barmWgAFrunilSk7tzNwxmSPafOzH9gGEe-Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/045726ccbe.mp4?token=BTfYLBLNZZ3nzqTmxR7M5KeBrIL6zjJcCs2NhDkInU4-_8wDLjD6AnaalIwUEV6HmIbqzWfBd0D9kd48kJLEe1CWNVZI-lGClirusRIG61XhpM8m5tyoAFXSY3gGSbTcoExecpW5vAPwtiYJUUgF4Cp1bOsD8_YhJf_PcGB6tfvoSJSeg3c2_2kVpAJ1VWqStWL6UvnDTnikYWw4rHbQSYJYZMpqpPnocfDijBm7mf2R-DSepvds99PgrpH6D8gQ3tKuxgShyb2To_l7Q8O41QKo-o4TLnBtw-cmQin7G36uS8Lj_barmWgAFrunilSk7tzNwxmSPafOzH9gGEe-Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔵
گلزنی گابریل‌مارتینلی در بازی امشب الهلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/Futball180TV/106291" target="_blank">📅 19:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106290">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMAjTQC1cmkn4DC5eoeKRDFfYLy2o7vkCwSOYV9P7TeSPnpuh_yH8zHnok8FWhpr2-Z0Yypn-dmGbVD7u7fKTVrrYZZTLT9SR_tCkwdzYoT87f0NC1sAk4Gcc6di8BZ6Wcy1zs4GBQPqjwwsrqDKscrc0kH66TsnsjLO_mM3g8GXCi3jbS0YCzZ2naFL0ipwIut3r1HcZacvKSiijreXz7tV6Yzc3D4ofCswVtfou9IbX4sCxh0mjVCLoK42oPg-SxWvLlNLd5Fgvt0UXSaKjuOrXR5RSfAkOw7eFWks4zzoYX06Nvvuq8CCksSpzrphopBqyEtr-N3TjaH8eh9zEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست بارسلونا برای دیدار فرداشب مقابل لوانته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/Futball180TV/106290" target="_blank">📅 19:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106289">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106289" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/Futball180TV/106289" target="_blank">📅 19:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106288">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSyi0BYqJr-o5XSkc0q2A4fk_K6e7zhdA6dtKtjnPC_klnrUK13FxKlZ8_N_Pt8T6sDhSFEfiBtjgOKdXdyb7yYQyGHoNfwKV08NQ762vOxA72wGwLewMBht45v3lnWWCyLhcvmnNipdO8tmjcwk4L4VilKU-yCSQaCW7vs1g3xkVZeFnl0MUxGgx4rKLdy0ayVWsqTwSDXHjBoLCFY7XzBfRWQX8XVwsdCwJlrNfPoeIjsQbMg-HIlWalbe3reZ3ltnFfG0KIqgyeR5b4J_2XdvSQ9Ouy8eMzPcSHtKtPLXQQyY5dsFq8iBLwdfr5vY_vH9cM_xS72SY-lU3MXHiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
میلان
🆚
لاتزیو
⚽️
را در
TrexBet
پیش‌بینی کنید.
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
میلان: ۳ برد، ۱ تساوی و ۱ شکست و ۹ گل زده
⚽️
لاتزیو: ۴ برد، ۱ شکست و ۶ گل زده
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/Futball180TV/106288" target="_blank">📅 19:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106287">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41e5692356.mp4?token=AFzTt0uq5r5N_10CAnhZPCTqHMUxq2Ay6_XJwUItAll0HrsgDd_rWj-MKZXYzAwk5Avuc35mAme0siR_WB4DxEm5Izg_nLGiWkZkPLfX08j_3bKeifN9tvOqhBOsQWtWizHTtB5oFbTlqtAQlOo_JEhQhrHQEvIdVGmhCbAH3IigG5pR_ws8PcwpkDaf8wqNw7715PSJPh42t4hDa0AgOD3VFfRr40u8CJyJ48hKNo5v9NfJTphe-zlfuQ5BsxrzcNU1TLvoCEpBtfWkYziD6uAHQ9OOZMdUwQ0xnWQwPgJg6cwbpEAKreR4jCg320ostk1wnkI8t8xLmZMPuNc8XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41e5692356.mp4?token=AFzTt0uq5r5N_10CAnhZPCTqHMUxq2Ay6_XJwUItAll0HrsgDd_rWj-MKZXYzAwk5Avuc35mAme0siR_WB4DxEm5Izg_nLGiWkZkPLfX08j_3bKeifN9tvOqhBOsQWtWizHTtB5oFbTlqtAQlOo_JEhQhrHQEvIdVGmhCbAH3IigG5pR_ws8PcwpkDaf8wqNw7715PSJPh42t4hDa0AgOD3VFfRr40u8CJyJ48hKNo5v9NfJTphe-zlfuQ5BsxrzcNU1TLvoCEpBtfWkYziD6uAHQ9OOZMdUwQ0xnWQwPgJg6cwbpEAKreR4jCg320ostk1wnkI8t8xLmZMPuNc8XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
تفاوت صحبت‌های چوپان قبل و بعد جدایی از هانی‌رامبد! نمک نشناس هم که هست ظاهرا!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/Futball180TV/106287" target="_blank">📅 19:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106286">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gt2ObcPcNbvoBiVjsNnx7-CMPSp3XFPPve-x6pIvnWuU_Gxi1ibvrsw0N9ORmXC21PsMyNlpAaZR1FrN_m4z3Ka3IA3OrlUNT0LULDaVgRJGO6fVs250l8d-0rQGBm4fbaqT9pgSPu8xoTELF8XwOYVXvG2sl_p0Scx0LrvG9-FNrAjfcyVmgONrF4esknjoY-bZYON3zJSnLFBOxuueu6i5weOBT0vSvmGaoI_jSH5KWqbZ_iAqLHkY5pi3T4rLJjssjCQnc1Exo54FDBRPWrG5acPkMy7yxna0RVBen_dvdjf200mfMJKQ9-F2inH6T4T14w6paZXjUf7Hes2_Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇺
جدول بهترین‌گلزنان تاریخ لیگ‌قهرمانان اروپا؛ هالند و امباپه با همین فرمون پیش برن به راحتی رکورد رونالدو و مسی رو میزنن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/Futball180TV/106286" target="_blank">📅 19:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106285">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90c64420bb.mp4?token=OYJmeJ2HPSb5aefobaE1Z0VKEIlNQYVzcO5-NnUwOa8R3GDk-8_XQmGY_2NpS0q_7HPLzdIiZvl6kEV_Xo484TRJEo57JgcCAKfadp2j-81vSTzrMoWYfhnqQ8Ovkx7asfN0sUBAyZbYaO4C3ZgburoMLuXnHtydGCLUGAcb-4Yg4oPgcH5V9MdNUQ4A2Ssfwd0F9TePSVbnQS1sra7pKPK-39lCXW2H9t5MUfbxZ9jxg2a4bLbTgH7qKJeHHfQN1t7Rm-Ju95IQiYUliYN-Iha1R5Fk16gJetQtPge6rSUmwPoOE5GTUOtndlLOMO1vdQN1jqmbooxoygIp4GQbjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90c64420bb.mp4?token=OYJmeJ2HPSb5aefobaE1Z0VKEIlNQYVzcO5-NnUwOa8R3GDk-8_XQmGY_2NpS0q_7HPLzdIiZvl6kEV_Xo484TRJEo57JgcCAKfadp2j-81vSTzrMoWYfhnqQ8Ovkx7asfN0sUBAyZbYaO4C3ZgburoMLuXnHtydGCLUGAcb-4Yg4oPgcH5V9MdNUQ4A2Ssfwd0F9TePSVbnQS1sra7pKPK-39lCXW2H9t5MUfbxZ9jxg2a4bLbTgH7qKJeHHfQN1t7Rm-Ju95IQiYUliYN-Iha1R5Fk16gJetQtPge6rSUmwPoOE5GTUOtndlLOMO1vdQN1jqmbooxoygIp4GQbjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🫣
🥲
دردسر‌های کیلیان امباپه هنگام دیدن سکانس‌های فیلم زیدش اکسپوزیتو :)))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/Futball180TV/106285" target="_blank">📅 18:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106284">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/833fb28b6e.mp4?token=NpE7eJ2DmY052v2JTsFFfYHjIKd9gCNsGNMq45mSu6Cgw0FqRB4fSx50i4p1ciCcijGKUdz2dlB-jwpJ-Bsq5vTK10NiXD7O1GWjAYfGw6sX9mgd1RpffJAFOQky81284FRinH5DWJjx3EeTAvSnJYOXBvFJclfz-2h41bJPWnnAXR9i3qZdOFBKiV2cUbMyoecp34WhvZDn1sZ6itzuRRpfhQLPxsDkJmDSM1O_IQIwdtj8s2Qqz3PcNEUc_BEWVb7L77EFBP46nx3NeGfjZVhz5JWTg7crM6QZAFyXED8uT1IAGfiQ9t1VatwzP6qjawVhSkZte3U1HXza6j-BGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/833fb28b6e.mp4?token=NpE7eJ2DmY052v2JTsFFfYHjIKd9gCNsGNMq45mSu6Cgw0FqRB4fSx50i4p1ciCcijGKUdz2dlB-jwpJ-Bsq5vTK10NiXD7O1GWjAYfGw6sX9mgd1RpffJAFOQky81284FRinH5DWJjx3EeTAvSnJYOXBvFJclfz-2h41bJPWnnAXR9i3qZdOFBKiV2cUbMyoecp34WhvZDn1sZ6itzuRRpfhQLPxsDkJmDSM1O_IQIwdtj8s2Qqz3PcNEUc_BEWVb7L77EFBP46nx3NeGfjZVhz5JWTg7crM6QZAFyXED8uT1IAGfiQ9t1VatwzP6qjawVhSkZte3U1HXza6j-BGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
ریدمان دیشب داور اسپانیایی بازی لیگ عربستان که بجای کارت زرد اشتباه کارت قرمز نشون داد
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/106284" target="_blank">📅 17:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106283">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9242df0ef5.mp4?token=c0MpQQP4OptSRX9aFwJkYzd3WvutngxANuvaxIOchhEenwvr87L0dW4zm0MJm9i3EFCJ6zxunUfguNoN0cjy2mMhLqzMquD7lTEBEmd4MPGCVJKvr_YjCVQg1ieFacNyts_yGg29karF68IwhXE50iesplFh3LaPycrC-wao3Rf0kRZIbFxzdHPCuIxD4cIk1Adg9q_jF2ARqVxUWo7ZjBOhxDojjSx3tG93-9zRZ7sRQ7IwYaMKZ1pX3c0jYcXC73iRvCrC22YpXqgR8W9X6iMOV3LITTa-IBEGbJgJe7ugTCZ9jVy6gHzeSsT4hVS7UUN0v9fThZPxhx8Bw4RwhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9242df0ef5.mp4?token=c0MpQQP4OptSRX9aFwJkYzd3WvutngxANuvaxIOchhEenwvr87L0dW4zm0MJm9i3EFCJ6zxunUfguNoN0cjy2mMhLqzMquD7lTEBEmd4MPGCVJKvr_YjCVQg1ieFacNyts_yGg29karF68IwhXE50iesplFh3LaPycrC-wao3Rf0kRZIbFxzdHPCuIxD4cIk1Adg9q_jF2ARqVxUWo7ZjBOhxDojjSx3tG93-9zRZ7sRQ7IwYaMKZ1pX3c0jYcXC73iRvCrC22YpXqgR8W9X6iMOV3LITTa-IBEGbJgJe7ugTCZ9jVy6gHzeSsT4hVS7UUN0v9fThZPxhx8Bw4RwhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
افشاگری جنجالی محمد سيانكى: برخی تیم‌ها در سفره خانه هاى تهران بازيكن جابجا ميکنن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/106283" target="_blank">📅 17:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106282">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iM1Bvv3HZKf9s4skskgwM2Eh5vmnTB7pberyOuFWejmNvMMHfG0TQdFXQniMrpNzlp9DJbX6NSNfyiIZpD9x6ZGkhExqxLBDBEH_DMc2i91_sdZpf7R6-ms0_6SQMVOL9gcWr-FbayNUGHipPm1rwyMOfbNZNVHTnjtMAtzYzrQrtGZ2AsuMB0RDt8HHKbeszpu2Ops2JuNvcYlwR37ZglXtiymmSf1UHl1wYAps9UmTjEr7MD8o9W-GTIsNHKt4Z0joEUbCQ8OFFoXAEDeMY8idswQpBU8cE7h7So86FaOl2wTHvuk4SLVwT4X6YBNyDU2suzeDBx2xnSZuttkbZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
🔥
🇪🇺
عملکرد تیم‌های انگلیسی در هفته‌اول UCL
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/106282" target="_blank">📅 16:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106281">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc8b60637a.mp4?token=C32jIRSNGbzE7dkPygxVXuLsb9L_GE1ixIH_UD4rCP2z8eoQ5UxTqAwCrMgYpwQ5vG-KAan7S9297IyKWfpV84EzefTFbWSeA5S86IhEIbFj_-DW-69qWQbGqHrylS0Q_ekI5ssRwBwMUGGi_Cq2kEk1PGdFkgo5z_SWbGoUhlGHctKU1P05jJMWxLE_kaXWGUpEL2x274YpKInOK_1a3d9l8rXvNVMkI68tpuE4ot22WEw84k2Ma2gXLyI_iZZpJgW42GD7Ky2-7FnSbpcF06Ry2TEtQan31fENfCfUEsMyM-P0KuVAYTmBFIKwhgK--t6omCAJPy6Akv4mBAB4OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc8b60637a.mp4?token=C32jIRSNGbzE7dkPygxVXuLsb9L_GE1ixIH_UD4rCP2z8eoQ5UxTqAwCrMgYpwQ5vG-KAan7S9297IyKWfpV84EzefTFbWSeA5S86IhEIbFj_-DW-69qWQbGqHrylS0Q_ekI5ssRwBwMUGGi_Cq2kEk1PGdFkgo5z_SWbGoUhlGHctKU1P05jJMWxLE_kaXWGUpEL2x274YpKInOK_1a3d9l8rXvNVMkI68tpuE4ot22WEw84k2Ma2gXLyI_iZZpJgW42GD7Ky2-7FnSbpcF06Ry2TEtQan31fENfCfUEsMyM-P0KuVAYTmBFIKwhgK--t6omCAJPy6Akv4mBAB4OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولی تو تاریخ لیگ‌برتر ایران هیچ‌شادی گلی مثل این نبوده و نخواهد اومد
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/106281" target="_blank">📅 16:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106280">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5318ea7807.mp4?token=I8lc3rFASqQ5IUBZUTbAIqjM1EYjGMGALHXBQnHCkDmsbaKS0IOOIRjn5CEtMx2WMUnsM2su-aXXo5tBgesLimUbOksPimybxg2d0QTojmjKBW1D0Qffg8ZXI_KsAHvwPv4RxOuFtuc4-MNMS0-N_uN0ydhlrA7So9DXrJGzK2tYmBkMHhcX2jApam6cEbyuslAVDeq3YYk85rJ_p5tYN7neBigTL3_xzKA9_8DzIFvT47sy3zN3skzCIz85V4mEUzLiKib29Tr6UE22fXvF7Rwfy1hP-0lz7_Bm6n31a_-zMgJf9y8dPgaP-xi1Q0qU_Yosge0p1DqC3QPaoUj15w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5318ea7807.mp4?token=I8lc3rFASqQ5IUBZUTbAIqjM1EYjGMGALHXBQnHCkDmsbaKS0IOOIRjn5CEtMx2WMUnsM2su-aXXo5tBgesLimUbOksPimybxg2d0QTojmjKBW1D0Qffg8ZXI_KsAHvwPv4RxOuFtuc4-MNMS0-N_uN0ydhlrA7So9DXrJGzK2tYmBkMHhcX2jApam6cEbyuslAVDeq3YYk85rJ_p5tYN7neBigTL3_xzKA9_8DzIFvT47sy3zN3skzCIz85V4mEUzLiKib29Tr6UE22fXvF7Rwfy1hP-0lz7_Bm6n31a_-zMgJf9y8dPgaP-xi1Q0qU_Yosge0p1DqC3QPaoUj15w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🥶
باریک‌ترین خودرو جهان با عرض ۵۰ سانتی‌متر ثبت گینس شد! وزن خودرو ۲۶۴ کیلو هست و حداکثر سرعتش ۱۵ کیلومتر بر ساعت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/106280" target="_blank">📅 16:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106279">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76c27ec481.mp4?token=lwR-M-2h0OBNO6BvP4hqRpvMx-K4dyS4li2_FTKZXDA4rP69ZbBO2C5NTjzmKt6VLVGeKw_gkm8s03HYXghH3wQhOrU09OlUcJJ5rXaQlOPVtrkmamWZyz51q2yhmMMEaQl6reqm6xIUq6gO_PECfFO2QHVvq7m9y2Qx_9uSYjXxzkjM0M4_YIppmloXFiyBvipRhqJf44_3pKr0J7xa1YVc-qM4KFrP9MPUSA3xTaLBC9Zc5UeE2e49_hVS7xn2kjSRA-2-ql1xr-p7mTKXGW3cj7TCXvQ0p9QYBXQFOJIFpllYwipc5rVRe9BX4Wk52I574FwyFIamgff-79MYBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76c27ec481.mp4?token=lwR-M-2h0OBNO6BvP4hqRpvMx-K4dyS4li2_FTKZXDA4rP69ZbBO2C5NTjzmKt6VLVGeKw_gkm8s03HYXghH3wQhOrU09OlUcJJ5rXaQlOPVtrkmamWZyz51q2yhmMMEaQl6reqm6xIUq6gO_PECfFO2QHVvq7m9y2Qx_9uSYjXxzkjM0M4_YIppmloXFiyBvipRhqJf44_3pKr0J7xa1YVc-qM4KFrP9MPUSA3xTaLBC9Zc5UeE2e49_hVS7xn2kjSRA-2-ql1xr-p7mTKXGW3cj7TCXvQ0p9QYBXQFOJIFpllYwipc5rVRe9BX4Wk52I574FwyFIamgff-79MYBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚫
🎙
هادی چوپان درباره کلیپ رقصی که در دی ماه از او در صداوسیما منتشر شده، توضیح داد این برنامه دو ماه پیش از اتفاقات دی‌ماه ضبط شده و ارتباطی با حوادث آن روزها ندارد
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/106279" target="_blank">📅 15:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106278">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f692d60102.mp4?token=v9S7HksaqP4IbkizNXG4cJp4PFyI28n9P4gGsCoONHUNw_FeeVeaePkXgT9JwdNVJyRut4Xz0yku_V3_ZPN6QuME4bFfZbMV27PvdtilbzgmVYFwhZUyQFllzHYKJlBRi15v33xp9gD8fS8bZPrwIo72dn9IgJdM7fEsBOSr7WeeKE4Gz0115ovhtuQLrNHtYFRbxiChoqWNDmHWimAH62EU1jFv_mVgscK2f1M1jUfDppj7mXsBhoo2B7YUnX-Pv61ToaSLEbxswD6XfwrtTOLtAHcUlL_TbPWaIjGeUufn8MepQCdWy9oceyWJoUCAYTLpq_94EP1WA8Y_Ez-OUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f692d60102.mp4?token=v9S7HksaqP4IbkizNXG4cJp4PFyI28n9P4gGsCoONHUNw_FeeVeaePkXgT9JwdNVJyRut4Xz0yku_V3_ZPN6QuME4bFfZbMV27PvdtilbzgmVYFwhZUyQFllzHYKJlBRi15v33xp9gD8fS8bZPrwIo72dn9IgJdM7fEsBOSr7WeeKE4Gz0115ovhtuQLrNHtYFRbxiChoqWNDmHWimAH62EU1jFv_mVgscK2f1M1jUfDppj7mXsBhoo2B7YUnX-Pv61ToaSLEbxswD6XfwrtTOLtAHcUlL_TbPWaIjGeUufn8MepQCdWy9oceyWJoUCAYTLpq_94EP1WA8Y_Ez-OUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
✅
تو این شرایط اگر از اینترنت زیاد استفاده میکنین برای مدیریت هزینه‌های خرید بسته، این ترفند راه خوبیه. برای دوستانتون هم بفرستید
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/106278" target="_blank">📅 15:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106277">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb9d15a53b.mp4?token=PwFbODS4N48IHuz9wOOcwXh_VaYRQk9ABDLo-lmlAECtToYpFjygoL75J-2CncaYI53JlyeScCAn3rgcm6jgH0N78_ihpvt_OlbMZLAsY73WuAWn_uxI0grFqqvW9DS2OYOv1hCnntpm3zA8Xtd-oMIOmNaUTz7X-tlNhr5QWyxKEN2fxvfmyh7Mflh-6SMtV0LQOrPlgQ7ebb64u9lJW_nl7me8JSaXycGH5ngs7CbyMVMu0M_hfrwsHvNCb-NVM8rVwPHeLZ8MoFUEMSx6EvbqnxPU-lKN_cO_0K2k-1Uwy7DJKAxlTtzD6lgBu1FA0jCJ7jB3HX43Lf5XtfbG9IisgzfCu5pKq7wK7U4ykuYcLY4_PXUMo51bObHhGhm-A8XjCCPjawABAPiKhTbH3NNuiJ3v8Tw2VZp83mqG1IKWBGrSbt7tPpG5NcgWlr8ESYac0dOKazNdYb5Kd8T5SNRU_Vcfknr7r3Q0hEWQGjJfj1I-DGwwhF9KyEmSrm9LOyBvSckYtkvvwjlqLKuDbci-1wDhPtPynT7_HGCTs3DvpvMIUBntHTz_BSzdocePZeRo-WisVhKrY0NS9IxLE5TMmfuqYGOpXlbER6lb-Vy6V3VieXJvS1gW3oa5L4lKbM9DTQZ5-fB0Dmi7sxX7TMti9ZG5uNmIgzwP6FPgChY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb9d15a53b.mp4?token=PwFbODS4N48IHuz9wOOcwXh_VaYRQk9ABDLo-lmlAECtToYpFjygoL75J-2CncaYI53JlyeScCAn3rgcm6jgH0N78_ihpvt_OlbMZLAsY73WuAWn_uxI0grFqqvW9DS2OYOv1hCnntpm3zA8Xtd-oMIOmNaUTz7X-tlNhr5QWyxKEN2fxvfmyh7Mflh-6SMtV0LQOrPlgQ7ebb64u9lJW_nl7me8JSaXycGH5ngs7CbyMVMu0M_hfrwsHvNCb-NVM8rVwPHeLZ8MoFUEMSx6EvbqnxPU-lKN_cO_0K2k-1Uwy7DJKAxlTtzD6lgBu1FA0jCJ7jB3HX43Lf5XtfbG9IisgzfCu5pKq7wK7U4ykuYcLY4_PXUMo51bObHhGhm-A8XjCCPjawABAPiKhTbH3NNuiJ3v8Tw2VZp83mqG1IKWBGrSbt7tPpG5NcgWlr8ESYac0dOKazNdYb5Kd8T5SNRU_Vcfknr7r3Q0hEWQGjJfj1I-DGwwhF9KyEmSrm9LOyBvSckYtkvvwjlqLKuDbci-1wDhPtPynT7_HGCTs3DvpvMIUBntHTz_BSzdocePZeRo-WisVhKrY0NS9IxLE5TMmfuqYGOpXlbER6lb-Vy6V3VieXJvS1gW3oa5L4lKbM9DTQZ5-fB0Dmi7sxX7TMti9ZG5uNmIgzwP6FPgChY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
داش‌علیرضا منصوریان درحال یاد دادن ترفند سرمربیگری به اسطوره سندروم‌داون استاد علیرضا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/106277" target="_blank">📅 14:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106276">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aa2c3aa1e.mp4?token=tmfodG9LIKfSl4s8ZgOtrqlphyRANXAaXPxxkfMqgz68c0rO2Aln7TTxxKUkTVL3gz5FIS4kfeSrL25sX53wUWDkIqJxtvM0aO3jXTnb6aDAfmgTQaTnAP2EV5stt5Af8ibGI2MGVUT22z5-gRr_eEpyAG2kpzH8Wl77w9u5GU1_CCY6MuEXEN3t-6cPiU5S_5Rhjpskk0UNyMrszYuUBxfFU2tLU1P1nq8ut-tqxtXarkSIcVeaC6KHpsl0VPA8rOnQ08TgyMEeoqVqH_Cd67pRaB4aFPziBySO_zKYbUerGzjOOzL4xPvshdjJshE30-dZqBQVxxU_53MaoxkU6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aa2c3aa1e.mp4?token=tmfodG9LIKfSl4s8ZgOtrqlphyRANXAaXPxxkfMqgz68c0rO2Aln7TTxxKUkTVL3gz5FIS4kfeSrL25sX53wUWDkIqJxtvM0aO3jXTnb6aDAfmgTQaTnAP2EV5stt5Af8ibGI2MGVUT22z5-gRr_eEpyAG2kpzH8Wl77w9u5GU1_CCY6MuEXEN3t-6cPiU5S_5Rhjpskk0UNyMrszYuUBxfFU2tLU1P1nq8ut-tqxtXarkSIcVeaC6KHpsl0VPA8rOnQ08TgyMEeoqVqH_Cd67pRaB4aFPziBySO_zKYbUerGzjOOzL4xPvshdjJshE30-dZqBQVxxU_53MaoxkU6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
دلیل جدایی هانی رامبد از هادی چوپان: اون مثل برادر بزرگترم بود ولی یه زمانی از من خواست پشت جمهوری اسلامی نباشم که من قبول نکردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106276" target="_blank">📅 14:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106275">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NkdtYwK23yGjgok9GeJpU2rYRHV0U8ZERIeiQKsS6OpPLZII4kAFXfRg9fgGBipBMK_DxBYnvJ9zsuOor3A_SxW1MNUWLbyyOTJd3peKBHg-sG78eLGShfgrAyfuRmFrluCi2AFg9Je-EloejLMhJxQs67UMSWvn8RcxWbtel27sO1ek1PoBQs2Egx8ySCG0rn78GaFk7rAJ-0p16a7bedqPsuzYi49zDJ8HHjpjSubQkCsUCQqJKJ4eAmwIr6VNVt4xYNze2hs45i73dlWHA4A55Rz46rzdx47wzx_tc1M_el6D8vTi-2Ck63oApL74eybPzEo3QuDyRZ6OqPxrWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه افتخارات لواندوفسکی و دی‌پائول که درگیری‌شان در هفته‌اخیر جنجالی شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/106275" target="_blank">📅 14:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106274">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4SuPig6yK8t3LszTfZMWGmiQ8bO-Ac0Qxh9ycVwPjGVb1QvHIGjgkqME4cgSDfbWTRBa2Gsd8owFQ6NZ9QLoDZNQ1dVLek3_k6Zay1Y8qG8aVGYkGdlnfBNEqpNQF5fOmz0206Aje6G1oqkTVQRtxmEGhi5-kqI-2e31sVEEys2sn5f02Obxjz4kk5UDMm31mzMJmPBUFTpWkYs8lN5NRv3wiIYxzzcvjGt2rNY4KJGXgdGs2Y3xaoTNiAIaENSaIhAiUU827cxzMnFnhSdymNB1VGkXhBjgPAIC-upq7KYLd0754cK5U_Jz13eGqLjzQrqWe3piQ_J6wMo1K_JOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
درخواست تاجرنیا از هواداران عراقی برای حمایت از استقلال در بازی مقابل السد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/106274" target="_blank">📅 13:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106273">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bcc13d5f9.mp4?token=SovcbNbqfFUlyQMJrAypRhWb8q9FEGQfaA7PwvTL9-BbP2Zydhfgerc-aT3FsNKlpbT1oC4XVNOiW3lOL3HbMt_yxksueMQGaMUZzUZjX87kF5BgGVZd7r6siO18uf-PbVSpcO6KuHoQviwCD8xOVADBSwA3mslvuXv5xCk5R0TM_numMssSaCIsJS262FYlZY6s18_C3AMCPaAkulP2LrOpNM01vJaFjLW9Pah_Go9i4xPmlwurKO7tZjJV-xkc1BpdsjaN0Hccx-jZgzEutxoeAuRtUpeg1bbVryJSLQjbO_89cj4FJWerbF1MV0JXdfsqUzBqebwZf2yYsWy_34WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bcc13d5f9.mp4?token=SovcbNbqfFUlyQMJrAypRhWb8q9FEGQfaA7PwvTL9-BbP2Zydhfgerc-aT3FsNKlpbT1oC4XVNOiW3lOL3HbMt_yxksueMQGaMUZzUZjX87kF5BgGVZd7r6siO18uf-PbVSpcO6KuHoQviwCD8xOVADBSwA3mslvuXv5xCk5R0TM_numMssSaCIsJS262FYlZY6s18_C3AMCPaAkulP2LrOpNM01vJaFjLW9Pah_Go9i4xPmlwurKO7tZjJV-xkc1BpdsjaN0Hccx-jZgzEutxoeAuRtUpeg1bbVryJSLQjbO_89cj4FJWerbF1MV0JXdfsqUzBqebwZf2yYsWy_34WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
محمود فکری: سهراب بختیاری‌زاده از دست صالح حردانی حالش بد شده بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106273" target="_blank">📅 13:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106272">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFpeiqMFsZn1Q6zKBcKGqV_HpdP4St75VNstKAP77OsGYuIW2a3eRf4xGILiCT5OvdArEM4gU2O574zyDx9kHom3J-LD8_FHMcfPwGlgoPm9sn8L22vvHvlHWw5r3jq8BhyItKu-Tx38qK6Z1tpMQgtWjChiofYV1CXmnNUamDGU1hRBjUDPBUVb2JxhjOGMUxVeyPlmDthmeJgms763A_8dFR7ltMIN4xRfbL0Ligly3qWMRb8RrI5Plx_3o2SDTuwNhC6sIpkJF4LMCobuMgtXUKnSyVeTaMk0lud6BiOmimmRnUT7ANdnBpOzopPTqVaX94cY8XUh0cQ_KbBgpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🏆
کیلیان‌امباپه: اگر عدالتی وجود داشته باشه بدون‌شک توپ‌طلا امسال باید به من برسه. درسته جام باشگاهی نبردم اما در جام‌جهانی تاریخ‌سازی کردم و این جایزه هم برای عناوین فردی هست نه صرفا تیمی. پس مطمئن باشید به خودم رای خواهم داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106272" target="_blank">📅 12:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106271">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_LYZMWXQOJ0mTG_13JQDUpK4DXOS_NZsV7I1fKY8cWViyD0jqitdmQwRSP_Zw_g8ygLtIh0KHBUe9d5-d5zS7ngncV1Dhisihm_5M4FNQNR_fTu4sAG8ZUlhKhjMbkOWGzU7Je-GWEkU2vMneN-Q80wUjwpj_bLXit1-ysCf-bbNyt1Bb66smnW24t0rb4s6bhfSvOY-71M_NYi7xAfpt9KR0EIogCAxmjZbUgjepZe0iLpkzCoGtVM5NjuBhyySO7sPA63wIodNCqaGzWbuxCgPYYsU2Ar716-5n5VqRRvckTkMs7L7s-9dtrpTk84lQP_XudrtS9v9eIDNUPj_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇮🇷
با رایزنی صورت گرفته مشکل پرواز استقلال به بصره حل شد و کاروان آبی‌ها تا ساعاتی دیگر عازم این شهر میشوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106271" target="_blank">📅 12:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106270">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92b41d0adb.mp4?token=M6E0zArPVsU7a5AMoyZu1VCfzdeoWFRloHyP8NM7POUYWtgD4FDbOXtRKkEjmjfI-OE0MoC1vdQrc6GHgBwJw-ZMHGO54b_2TV6b5KoliwQH-ZkxBIw-NFJ0eKCCn7rJcCEV1SBZLZdS5sFvW60Lc_fOEkhFl73835eFzi6JLYP36VeWSl8fc5nyKzXiy1vlFlUcamtkaMRb3B5s3qnXxyXoWSPtz8BSkZ-wvosP7WVcXv0L549Y4dLAGy1B6g0nIHXeec4QrnITgm_njUYclG-foA2eloE3l27hVK9S-AhsVObk5aXDDW6cixYiVH8wWJ_b3L5K3eSZbOC0jbGRVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92b41d0adb.mp4?token=M6E0zArPVsU7a5AMoyZu1VCfzdeoWFRloHyP8NM7POUYWtgD4FDbOXtRKkEjmjfI-OE0MoC1vdQrc6GHgBwJw-ZMHGO54b_2TV6b5KoliwQH-ZkxBIw-NFJ0eKCCn7rJcCEV1SBZLZdS5sFvW60Lc_fOEkhFl73835eFzi6JLYP36VeWSl8fc5nyKzXiy1vlFlUcamtkaMRb3B5s3qnXxyXoWSPtz8BSkZ-wvosP7WVcXv0L549Y4dLAGy1B6g0nIHXeec4QrnITgm_njUYclG-foA2eloE3l27hVK9S-AhsVObk5aXDDW6cixYiVH8wWJ_b3L5K3eSZbOC0jbGRVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
پاسخ جواد نکونام به سرمربی پرسپولیس!
جواد نکونام سرمربی تیم تراکتور در پاسخ به صحبتهای مهدی تارتار در کنفرانس مطبوعاتی پس از بازی با استقلال خوزستان صحبت کرد و گفت که «آنها از آب گل آلود ماهی گرفتند!» تارتار هفته گذشته خواستار برخورد شدید با خداداد عزیزی شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106270" target="_blank">📅 12:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106269">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106269" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/106269" target="_blank">📅 12:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106268">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVUqGpsYK3zxLRfP0wqJspvY_pcf7Ud_RmUNzlYVA_cXHky69Mt-WFuNROfUpROEya4e0HsD2vXL4Lqp_arG6-agbDBmSuC3mvCcAZajVv1K2srYPn8WldU-VAtrk2iSn9WQ7fhVABElX6rGoDdYgVccfsK1UnUJE6ZsG_UVigE_37lszFLWzjmZTw02PNF20qYyaoIn4Gjhl5aELBrblr2fzWG42kGQwfsAwLTMgiJhogk2v2iRZ7Jjn8kwViNa9OyLKGByHVOCZY0csIWSwRe6oFXCvToqgDggiPhlsDT1OHAHlwNos98eSEDztRTub9qchrQ-RVJ9hJV0RN1xtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت‌بین‌المللی
TrexBet
پیش ‌بینی کنید.
چلسی
🆚
لیدز یونایتد
فولام
🆚
لیورپول
اورتون
🆚
تاتنهام
ساندرلند
🆚
آرسنال
رایو وایکانو
🆚
رئال مادرید
میلان
🆚
لاتزیو
کالیاری
🆚
آتالانتا
پادربورن
🆚
دورتموند
🦖
🦖
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب برای بازی‌های امروز
🦖
واریز آسان و امن از طریق کارت به کارت و ارز های دیجیتال
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106268" target="_blank">📅 12:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106267">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
⭕️
🇮🇷
درحالی‌که مدیر سازمان فوتبال استقلال دیشب گفته بود که اعضای این تیم امروز ساعت ۱۴ تهران را به‌مقصد بصره ترک می‌کنند، فرودگاه بین‌المللی این شهر تمام پروازهای با مبدأ و به‌مقصد ایران را تا اطلاع ثانوی تعلیق کرد
‼️
‼️
‼️
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/106267" target="_blank">📅 11:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106266">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d37095ed52.mp4?token=eSU2raGGBXmp4JM7UizmkqUK_yNwoA_mF1hshvktUpo0MdWJZYgK2n7L248xJGg4n2STfdeaxBf23mtJzl-v4h7x5mhihCw807VHhXed_frdParEh6x5AMxySpREFssqPma4AC8Ok-aDqZSIgUS5ul796UXTEDRaAFuMSHY5wyr7paF9JMO8ihZZEOdyQudvWg-V9ADNxRHssMx7t4txBHv4o9FdC5mjQZX_WQhG6IUChFZ8XC3VNNm75GfZ0mgdQ70vw7TAnNeOEZaVp_jl7Z2Hu19uumYx4rDuhPofF36d0WLWRwxAhKLHnBprG-P6VDRy6QEMHnkEFUIWlGKeyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d37095ed52.mp4?token=eSU2raGGBXmp4JM7UizmkqUK_yNwoA_mF1hshvktUpo0MdWJZYgK2n7L248xJGg4n2STfdeaxBf23mtJzl-v4h7x5mhihCw807VHhXed_frdParEh6x5AMxySpREFssqPma4AC8Ok-aDqZSIgUS5ul796UXTEDRaAFuMSHY5wyr7paF9JMO8ihZZEOdyQudvWg-V9ADNxRHssMx7t4txBHv4o9FdC5mjQZX_WQhG6IUChFZ8XC3VNNm75GfZ0mgdQ70vw7TAnNeOEZaVp_jl7Z2Hu19uumYx4rDuhPofF36d0WLWRwxAhKLHnBprG-P6VDRy6QEMHnkEFUIWlGKeyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚠️
بختیاری نویسنده و کارشناس اقتصادی: چند سال قبل من رو به سمینار دعوت میکردم تا اقتصاد رو با انیمیشن به رئیسی یاد بدم؛ گفتند ۳ دقیقه بیشتر نشه چون ذهنش می‌پره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106266" target="_blank">📅 11:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106265">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbe7ae3e84.mp4?token=KKtk7BK7bGkDg8gEwyBgWZ-8cQeI9wV4Pzk9yEgzc1qX_Ok7-pmypnaoxPyqJobDjk4d4noXsgNriWSC1AZ6e9XL04sHVJR0VTjsNwPKf1wKrCpaqYqxteD7mxmOa-0lgZ8_6y4LvkuqmzCOel_tsDsZ-6bA-85V1GlwwkF71YVO5Gho0_Bn14K01NYf8y8z7NS4LDIXxJVHDC0ucKArcPDqQQgV9c7Pj3-o7apypZ7Im4TVNCyPesKfz3_y17c2zPTRRywvdCYEwdxl52yge4l4AZ-L8mQpdXiUPxozfjqjSWdQphZLPULQKK6xcfDzBfD9jgXy9isGDe7j4MTG5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbe7ae3e84.mp4?token=KKtk7BK7bGkDg8gEwyBgWZ-8cQeI9wV4Pzk9yEgzc1qX_Ok7-pmypnaoxPyqJobDjk4d4noXsgNriWSC1AZ6e9XL04sHVJR0VTjsNwPKf1wKrCpaqYqxteD7mxmOa-0lgZ8_6y4LvkuqmzCOel_tsDsZ-6bA-85V1GlwwkF71YVO5Gho0_Bn14K01NYf8y8z7NS4LDIXxJVHDC0ucKArcPDqQQgV9c7Pj3-o7apypZ7Im4TVNCyPesKfz3_y17c2zPTRRywvdCYEwdxl52yge4l4AZ-L8mQpdXiUPxozfjqjSWdQphZLPULQKK6xcfDzBfD9jgXy9isGDe7j4MTG5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
‼️
🇪🇺
🇪🇸
کارشناس چمپیونزلیگ: امسال نوبت بارساست که قهرمان این مسابقات بشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106265" target="_blank">📅 11:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106264">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecba46a4ad.mp4?token=eKITosdEVTqIYJl16CkRV_vwrNkgNZUd3Apt5DCF46ahlyykrE_sgMPBCxrM-tTvozLFceUYI48C10ym57n-ZDlcFvVmAF0s2-ePrQXVwWBF-JcH-bn8qd_pksDumM33A9qjbbnLzxalh8I_xT6JTFFXfmwTcsaht-fo3aI0o64z_HAQHD3BDaJZIruBpiRP069SzLvSW8Io8Qe7ysBOOHGTJbw5RKP1zarZcb3mjclYVWlUq7b6ZCzhHndiK0rY2w9BSqJiw_OVhxoS9noKy4RQJ_dM96EwELRroTVrBQmyIQxvN1Kt81BAN4fJ-VafCoeNKWcLROgeXafcTzlwxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecba46a4ad.mp4?token=eKITosdEVTqIYJl16CkRV_vwrNkgNZUd3Apt5DCF46ahlyykrE_sgMPBCxrM-tTvozLFceUYI48C10ym57n-ZDlcFvVmAF0s2-ePrQXVwWBF-JcH-bn8qd_pksDumM33A9qjbbnLzxalh8I_xT6JTFFXfmwTcsaht-fo3aI0o64z_HAQHD3BDaJZIruBpiRP069SzLvSW8Io8Qe7ysBOOHGTJbw5RKP1zarZcb3mjclYVWlUq7b6ZCzhHndiK0rY2w9BSqJiw_OVhxoS9noKy4RQJ_dM96EwELRroTVrBQmyIQxvN1Kt81BAN4fJ-VafCoeNKWcLROgeXafcTzlwxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هیچوقت این دوراهی سخت فراموش نمیشه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106264" target="_blank">📅 11:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106263">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84d171b8e1.mp4?token=Uok2e6H0OzN_JIpGAKMfiGIQ_8ftFEfbMgLhkJuyeTuKNBGANJ4ID0L18ulRjvklsHfM38WTK--ydZty16KRlZYM1vY51dWu4oTBGnD5KAl5mYQMQU57NTWaPksPDPa4ogUK_TLD3HIObyfdteNJlPG5UTq4BsRxljAUg6VBt9OaIAUUmQNZVdlSxwXqwoaKMYOz3-YA18ZUCgFlFPaBmAYIL8owPI5XeAhEoT6BjUNg8-Ryz7a63WpnXlHedmRYBqOCLWE9AzQ24oouBPY29PDvQj66OZP2ByqeCWoeGKtv3zZFlNLtbRUEote3lzQtbaGypMPYY94eVQaEAxZBAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84d171b8e1.mp4?token=Uok2e6H0OzN_JIpGAKMfiGIQ_8ftFEfbMgLhkJuyeTuKNBGANJ4ID0L18ulRjvklsHfM38WTK--ydZty16KRlZYM1vY51dWu4oTBGnD5KAl5mYQMQU57NTWaPksPDPa4ogUK_TLD3HIObyfdteNJlPG5UTq4BsRxljAUg6VBt9OaIAUUmQNZVdlSxwXqwoaKMYOz3-YA18ZUCgFlFPaBmAYIL8owPI5XeAhEoT6BjUNg8-Ryz7a63WpnXlHedmRYBqOCLWE9AzQ24oouBPY29PDvQj66OZP2ByqeCWoeGKtv3zZFlNLtbRUEote3lzQtbaGypMPYY94eVQaEAxZBAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اعتراف جیمی کرگر به اشتباهش درباره لیساندرو مارتینز مدافع منچستریونایتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106263" target="_blank">📅 10:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106262">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d19807ddf.mp4?token=KHLy3JFmHYYZWf4Uj8A9_pz3HDWpeb8a_v2oUwzqGgEVd5GosXGBFMZM2DNFvbH5Jv7YUoRHMFWQMckKpJimTSPt5D2gUA70_pnDM-xeQUfvjX7jxBZf5fZs6MJ4i40JYYca8DcRbT5JMd9nz8lSaSJmo4XWL1EHd6FnpFO6PY-V1dSOVJona4BYdL9V9bm0Lk7yNsRAbhdue7pcricnx49pYDJOz29DqFcb-FQbJMOJYlzV8_1kseVctwAM8IfrE1G2zOBEBl2L5B9AUi7dOWnsyKXhZKcBanf667P6nTvhphOv_sMAnjkm2d40KlfQQex73OhrjNwJilgVmyGxkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d19807ddf.mp4?token=KHLy3JFmHYYZWf4Uj8A9_pz3HDWpeb8a_v2oUwzqGgEVd5GosXGBFMZM2DNFvbH5Jv7YUoRHMFWQMckKpJimTSPt5D2gUA70_pnDM-xeQUfvjX7jxBZf5fZs6MJ4i40JYYca8DcRbT5JMd9nz8lSaSJmo4XWL1EHd6FnpFO6PY-V1dSOVJona4BYdL9V9bm0Lk7yNsRAbhdue7pcricnx49pYDJOz29DqFcb-FQbJMOJYlzV8_1kseVctwAM8IfrE1G2zOBEBl2L5B9AUi7dOWnsyKXhZKcBanf667P6nTvhphOv_sMAnjkm2d40KlfQQex73OhrjNwJilgVmyGxkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🙂
جدیدا تو صداوسیما دیدن که مخاطب زیادی ندارن دیگه خیلی احساس راحتی میکنن
🎙
مهمون شبکه دو: زیر کونشون میزاشتن
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106262" target="_blank">📅 10:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106261">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
⭕️
🇮🇷
درحالی‌که مدیر سازمان فوتبال استقلال دیشب گفته بود که اعضای این تیم امروز ساعت ۱۴ تهران را به‌مقصد بصره ترک می‌کنند، فرودگاه بین‌المللی این شهر تمام پروازهای با مبدأ و به‌مقصد ایران را تا اطلاع ثانوی تعلیق کرد
‼️
‼️
‼️
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106261" target="_blank">📅 10:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106260">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31134b7828.mp4?token=Fq8dcJYsfwKiFGVgCKxHoAtL-W3NmwxuMVyuUtVfRAp-MarHXIMpFcL8E8XBLXqtv_-her0DlPz3YLPEXRO0JdphHnPsFwZIxyQH4o65w070gdKwZNhqwwr2pDc1AJ_OI0TaY5yFIxX9CUOieoLtQ1OxtPKA9S5OiLqsPYdtzXAqBuNOT6UclIayoNca9ox6xpWnJ_alZtiVshq036euu-V0SOFkYyYzDCJfeYFgCQR1HCBP9yUTvkB768DYyW3ep98KmLlOVLMoD8ZnO7w-zrvrxAWZtliWd9wRlU8y73Krb3p1AlDfsTBCo-dTN7U6glnJkgiX9PP9Hzb1Pb3R-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31134b7828.mp4?token=Fq8dcJYsfwKiFGVgCKxHoAtL-W3NmwxuMVyuUtVfRAp-MarHXIMpFcL8E8XBLXqtv_-her0DlPz3YLPEXRO0JdphHnPsFwZIxyQH4o65w070gdKwZNhqwwr2pDc1AJ_OI0TaY5yFIxX9CUOieoLtQ1OxtPKA9S5OiLqsPYdtzXAqBuNOT6UclIayoNca9ox6xpWnJ_alZtiVshq036euu-V0SOFkYyYzDCJfeYFgCQR1HCBP9yUTvkB768DYyW3ep98KmLlOVLMoD8ZnO7w-zrvrxAWZtliWd9wRlU8y73Krb3p1AlDfsTBCo-dTN7U6glnJkgiX9PP9Hzb1Pb3R-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇮🇹
اولین‌حضور کومو دوست‌داشتنی در UCL
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106260" target="_blank">📅 09:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106259">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f0128cf1a.mp4?token=XO30ZmgWnoESPotfxuMlQUjbGE0nD6DxlY1B4zKD2CapZA2SuhHZFPLIv7lJakpLqbiAmxGotasQCSmjHXGgAQkA-6L687PDSTLrcCKT2MC8z40WJ5-0Ng5-_dAQ0uMKPjgdpPVtDo5hYpUtNbHsxpxTHF8oSmPgznpge0Bh1jQ_h3xBq0eyakKqTtFbhajdSaGwKMy56wrElrHnUXyO3zO48S6SAb6iBBVQb7AfXxJ7XuEsjy2tihCbA4Ef1YjMrOsKC5AQ_omiQDG8iT9S7JrdhQdOMg5utriMOP2QpMgYIWMS5_PD3nnlKwSgByN2Qda5VcA8u54Hj1Ru9-tpPDoUkV4cyPVuvR9WCnCql6Sxn3otoo8B_Pvu56KHIpImzDqVwvcJCztTH3B4pU4vAtdPZse5fjgcEQL0vlu3tj-D58NzSer6Z-e3TSwAYHqIPnF6e1OlBitZgUKc-6wvZYnIU5Xrn4Wpm17PDwyy51_YtdYnestBM67KSpMefmnaiGXVsEY3nOTV25CmOee4GsinGgSwFze0R77oI5X_YMP62IPWbPDAHMZFP2SucYIwo1db_i8I7wnnxolPyP_HnPzFKPvUtxkE8xKnqTFytl7D0TK4vnyuu3YQCmP7OEAMusOmrdc1fgm8U843DSV37Uc9eEvBHDBvycUUeRzadPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f0128cf1a.mp4?token=XO30ZmgWnoESPotfxuMlQUjbGE0nD6DxlY1B4zKD2CapZA2SuhHZFPLIv7lJakpLqbiAmxGotasQCSmjHXGgAQkA-6L687PDSTLrcCKT2MC8z40WJ5-0Ng5-_dAQ0uMKPjgdpPVtDo5hYpUtNbHsxpxTHF8oSmPgznpge0Bh1jQ_h3xBq0eyakKqTtFbhajdSaGwKMy56wrElrHnUXyO3zO48S6SAb6iBBVQb7AfXxJ7XuEsjy2tihCbA4Ef1YjMrOsKC5AQ_omiQDG8iT9S7JrdhQdOMg5utriMOP2QpMgYIWMS5_PD3nnlKwSgByN2Qda5VcA8u54Hj1Ru9-tpPDoUkV4cyPVuvR9WCnCql6Sxn3otoo8B_Pvu56KHIpImzDqVwvcJCztTH3B4pU4vAtdPZse5fjgcEQL0vlu3tj-D58NzSer6Z-e3TSwAYHqIPnF6e1OlBitZgUKc-6wvZYnIU5Xrn4Wpm17PDwyy51_YtdYnestBM67KSpMefmnaiGXVsEY3nOTV25CmOee4GsinGgSwFze0R77oI5X_YMP62IPWbPDAHMZFP2SucYIwo1db_i8I7wnnxolPyP_HnPzFKPvUtxkE8xKnqTFytl7D0TK4vnyuu3YQCmP7OEAMusOmrdc1fgm8U843DSV37Uc9eEvBHDBvycUUeRzadPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇩🇪
عملکرد درخشان اولیسه مقابل بودگلیمت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106259" target="_blank">📅 09:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106258">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a312ae120.mp4?token=Or28nh3MmCTLvES-kdNcfSmK8wEZMHNiG2Dhrt-NDwLcwROcpPBcausjWukr0yukTOLmuUmccp4v1Kn-DIG_56NYZdspUv8NMGDJQnnR2bMBbePZwOEItQw2F3n5n2Ovu0SCg4gWQp4uH7UEhGny2BPSW08NIyqkHZ25qgG2u4fMPo53s_5iEdUfdyspvFtLYNkkZRyc5-LF5mz1QwvvyoC0Cw4wzWVz2OzhkrD27Rp1nXE-Y85kjOlBh4Vi7V5BOqxw_tDmJp-kcZXPk87ooan5SWa3-G5NPa-P-hbNHsL7Tj2WeUSQ62RQ-_-dAD4O3ol0duEPy9kvTOg4q3KmPm4iDVLsB-K9kUbmEbHPAsECDKK00hlt8l0fzhH2MJyR3WuT46QkUW36ec_ZSwWnOaW8b9u8CA-wj6DP-K2pS0PhwegHRls26H_Ia6u3n--CpaOCD9JadsJaW1owew4iexnIAycCbA0H8S4wYjKYkqa3agNV0CM-SnXLzILPUH1DgnhSBSsFyZddbjwUbWiZ3zu_fGadPuUUI1GkyE0cnZHr9AqYVj_pfJuFWHbHCnX3ZKOY1FVK_FcI5qzB5Y5c8Xn_ppbeBtNxbeAWcpADnaXK3CAESKmRqGT8nVujyL-tpZD7Uy5Q-35YEMQH9NwRsgdkoZxNCRUVFAYF04gm7bs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a312ae120.mp4?token=Or28nh3MmCTLvES-kdNcfSmK8wEZMHNiG2Dhrt-NDwLcwROcpPBcausjWukr0yukTOLmuUmccp4v1Kn-DIG_56NYZdspUv8NMGDJQnnR2bMBbePZwOEItQw2F3n5n2Ovu0SCg4gWQp4uH7UEhGny2BPSW08NIyqkHZ25qgG2u4fMPo53s_5iEdUfdyspvFtLYNkkZRyc5-LF5mz1QwvvyoC0Cw4wzWVz2OzhkrD27Rp1nXE-Y85kjOlBh4Vi7V5BOqxw_tDmJp-kcZXPk87ooan5SWa3-G5NPa-P-hbNHsL7Tj2WeUSQ62RQ-_-dAD4O3ol0duEPy9kvTOg4q3KmPm4iDVLsB-K9kUbmEbHPAsECDKK00hlt8l0fzhH2MJyR3WuT46QkUW36ec_ZSwWnOaW8b9u8CA-wj6DP-K2pS0PhwegHRls26H_Ia6u3n--CpaOCD9JadsJaW1owew4iexnIAycCbA0H8S4wYjKYkqa3agNV0CM-SnXLzILPUH1DgnhSBSsFyZddbjwUbWiZ3zu_fGadPuUUI1GkyE0cnZHr9AqYVj_pfJuFWHbHCnX3ZKOY1FVK_FcI5qzB5Y5c8Xn_ppbeBtNxbeAWcpADnaXK3CAESKmRqGT8nVujyL-tpZD7Uy5Q-35YEMQH9NwRsgdkoZxNCRUVFAYF04gm7bs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
داستان جالب منیجر ایرانی مسعود اوزیل؛ مهدی کیا: پدر مسعود اوزیل باعث پایان فوتبالش شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106258" target="_blank">📅 09:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106257">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در TrexBet، بین ۲ تا ۴ عکس چالشی منتشر می‌کنیم که داخل هرکدوم یک Promo Code یک‌دلاری مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.  18:30 → اولین شکار  20:00 → شکار دوم
🦖
• شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106257" target="_blank">📅 01:36 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106256">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQjxw_nRcNhuX_rcOm6vgpBKslDB4gBE70VYWeNESdxWDQs4fQ9SNCAGWkDWbOUFUgoGHejrSiLmccqBC_GnJZeUV1oo9-gWk9aZ7rxw-8oalMdBLVxaN6qXfl8IimAnr6n_MqNx-cQA07hEmGAumPULDr5evg3hpJye4EmcUZtqhZ3bB23Dgf99Pg_fBCYJPWHh7Q5ewn0rIokq9s1TzmCaxTOsbTcaBt--Ki2EOQujqFtvUBzEDl9lG4Ecz1oHZBTcK1FkSDiWZPM8u9XozuSc9bsBIxUnlGsP0u9bQ0J1vxLKCHwIt4rlvGfdA2cqFEDvyBO1HNQYfVs4ee217g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در
TrexBet
، بین
۲ تا ۴ عکس چالشی
منتشر می‌کنیم که داخل هرکدوم یک
Promo Code یک‌دلاری
مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.
18:30 → اولین شکار
20:00 → شکار دوم
🦖
•
شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت نره...
ممکنه کدی که دنبالش هستی، فقط چند ثانیه با تو فاصله داشته باشه.
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106256" target="_blank">📅 01:36 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106255">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106255" target="_blank">📅 01:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106254">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_l0gXkuMszbhAG9RWOl3EKOzz2tY1vG66jPWgnGfHi5g5HKneomQ5lVAHzkCoVHB-Bl4bAwf48ujSBNFMEnlBZhkit1qplqcqvsf8P_Dee1ggn1kWH_TY2UVDz4Kdyx9LjMA2myW4BKmx6akWMHMA7rQi4-0STL7yO3nBfkDmP72_Ia-SLuRbNNVcIYEWpneSAvZjaKWxPfQvFZmP9ZYD_8j69rqiTA6UYXTTpNTaJ9gWmFnZkYkfXzGc34_hyBsoMp_K56I1OFQhoLdy0T6iYWGpFhctOlm7JyGjC53ukTdGrNDmDocowHfwrx-9dMN8Vtzq6ybXYLJW4bN0WGJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
✅
🚨
کیلیان‌امباپه:
🔻
من سال‌هاست که خودم را بهترین بازیکن جهان می‌دانم اما اگر در مراسمی توپ‌طلا به مسی یا رونالدو می‌رسید، اصلا ناراحت نمی‌شدم چون می‌دانستم آنها چه بازیکنانی هستند. اما درباره سایر بازیکنان و کسب جوایز کمی تعجب میکردم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106254" target="_blank">📅 01:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106253">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFWZHmxZ6FFn6igNb031nukfI1npeLw7KqH4x_Fz1H-n0pryBSUkYwcDkjRLm26wP3wJ48wT1U3JRKgoYjFumAduL7ljkgwWopoy3clHmIB2VGF-nZMINWmPXE2ZUJyud1ruZrhh2iHwbyAiM-iaek3S67Uk0_wVlGoLYB-YufnKVgWRHDGj86cJTUKO_jHT_CDf_RS9qCczjD9rB_3SOnIP_DrxjJIQwSOIRtZYyac8pvpdwvxBq6s48NBbzhhgJy_A9wcRAVfUUhb6-CNe-XV_60dgYpWcUmxuO5PhPDXbZRObYDTKYclQQ3HSN4x_41TY7UCZeyGs3K28gJenwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
آیا فکر می‌کنید می‌توانید مانند لیونل مسی تا سن 39 سالگی بازی کنید؟
🚨
🎙
کیلیان امباپه:  اگر لازم باشد، تا صد سال هم بازی می‌کنم! (می‌خندد).
🔻
آیا کیفیت من هم به همین اندازه خواهد بود؟ این به هوش بستگی دارد: اینکه بدانید چه زمانی دیگر نمی‌توانید ادامه دهید.…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106253" target="_blank">📅 01:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106252">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UP0pA7UV42kofgBDgK7UokLsP9bzWrBfzPSxYNaYnQpJNKf96qoY0cYDyEcZuk3Fm6kkm0Yi2uWjlCULzx3RT2hp3l7fQQw_gnH27BDBuCbADbz_sdp0YIsxeMaSO1zNlasNGM4T6wHTDoqkmewFzcP23TCGNGZClvwclNYM2JJAUacNy0hFM8_ei_yPJhCD98KjWWpmsMSzV9mKbD7vUh9tRYWRv-DPT1mhP5zFTKb2eS0bV-GegF4QPhPkCljkYWgdfzJ2d0pnll9pzcKlK7GlmHg6E-mvRytlfbbOIHfNjnQKPPHOOWg6p09mXfd6u4ElierCwlHs92TqGjQoyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
آیا فکر می‌کنید می‌توانید مانند لیونل مسی تا سن 39 سالگی بازی کنید؟
🚨
🎙
کیلیان امباپه:
اگر لازم باشد، تا صد سال هم بازی می‌کنم! (می‌خندد).
🔻
آیا کیفیت من هم به همین اندازه خواهد بود؟ این به هوش بستگی دارد: اینکه بدانید چه زمانی دیگر نمی‌توانید ادامه دهید.
🔻
او نیازی به فکر کردن در این مورد ندارد، چون هنوز می‌تواند این کار را انجام دهد. ضمن اینکه، مسی خودش یک بازیکن فوق‌العاده‌ خاص است.
🔻
من خودم را یک بازیکن متفاوت می‌دانم. اما او هم یک بازیکن متفاوت، در بین نسل‌های مختلف بازیکنان است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106252" target="_blank">📅 01:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106251">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFER1IBZ4rxvoL9qhX16UWpSFO9r_gZVt-IMNlThpKbocGD74xYhPzn4QQ63gJokgiyWR1uV4HUm4lK4bY6Q9feuaZ42mqYe7fwv3QOZjCX1Awt6_90JP1ofU8pPcL7yEspoRr-emSzQHvlP9u71ITkRQAoUbUEgLgzFpfJFXMpmzUx_IXQiBQ0GHJd-MmY-UiNVReG63AxCTHD-6QUyP31R5gtCvDMzGH2Ljg8oYNdA9uveEa8cTO5YtfFX5TeceFLOrWQIvQt_0L4cMo3DSxuY8wYFdAYY5kB_GZmm1Mi87JvzM328qh4fx4iMmHgRzVYwX_3CNJHvJ2qW2Ee2FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😆
📱
استوری ابوطالب‌حسینی: ما نبودیم دیگه تو فوتبال حاشیه نبود و همه پاها موازی بود دیگه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/106251" target="_blank">📅 00:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106250">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b4f3dd673.mp4?token=UUB-3pc-EuPscV-3gTDJmdS7S1Ho1eMLXxNm4JTLqoqK4ErD4869_Os_W58VVwtJfkZ6BRpgt97maQMgfiX88Vc6PledOMpp2P_ZSyTe3rvxJCA884og8uPD6JYhGow83eIr4WoCxL-Bbu71ZwA2Fbp2Z64vQa8vD1lWeQlwkbRFiDgvFm4N9vIF72l2_WUco_72OnTjyaxuqwt4EPdOC8WreKOYPedWIq0IUzDH4QHJw6vUqZwrji-BBYEXxPCgCQDapu6Ri2LrhcTY-AI20kDwc9w9XZdI5YrMuoKlS-4uHyQCtNktVQiQU0w-aKSCqJ4Pa3Bs9QciYOn7yYqi8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b4f3dd673.mp4?token=UUB-3pc-EuPscV-3gTDJmdS7S1Ho1eMLXxNm4JTLqoqK4ErD4869_Os_W58VVwtJfkZ6BRpgt97maQMgfiX88Vc6PledOMpp2P_ZSyTe3rvxJCA884og8uPD6JYhGow83eIr4WoCxL-Bbu71ZwA2Fbp2Z64vQa8vD1lWeQlwkbRFiDgvFm4N9vIF72l2_WUco_72OnTjyaxuqwt4EPdOC8WreKOYPedWIq0IUzDH4QHJw6vUqZwrji-BBYEXxPCgCQDapu6Ri2LrhcTY-AI20kDwc9w9XZdI5YrMuoKlS-4uHyQCtNktVQiQU0w-aKSCqJ4Pa3Bs9QciYOn7yYqi8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🇮🇷
🇮🇷
آنالیز بازی استقلال و پیکان توسط تقوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106250" target="_blank">📅 00:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106249">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ki6c9qgAj0H2rpDsdJEHeXPxgEbNjYmf93wwkSsCKbtmbOZbIwMczr9WwwDhQuOfW-e_cCxzJEDXFH46CW82v1_iYadEWmRLpkwob89I2q1NJM7nPVIVJCUbCJ512B2P8sJT-drjtCpIvjDCqPslp2QZTp4l7wOQZJJl3ABfZ3wGZuSzLMaUGG7feCeYMWE-VDG-zRBqr8s6zfqIStLUKfDIddLw7Mn880pLL_9PMTL1s8PXGrEwzVvVqJiRNK1YR1EupmD4HFhfMQp-lzeqqkRKqVm_mpEcGjc0NNdriVeXOZBrL1T9izMLwxfsnCf1dCWwFJ0AJm0dultlX8guvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
⭕️
🇮🇷
با اعلام باشگاه استقلال، مشکل مصدومیت یاسر‌آسانی جدی نیست و این بازیکن برای بازی روز دوشنبه مقابل السد در دسترس است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/106249" target="_blank">📅 23:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106248">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/op1XwY78NlfoP4KuGiDZ3NozBZohg6SH-opG0CIphNN5KmcGiDw5UDX25J_L7TpiCpFsyRjtzjVlluDCZTJBQVrALQj-QH3yodBGhjgRDTBe-kp5-eZiVWIdn86hSvXOQeGPspcHjRdSTYjw6XhS-4Q3OtmDGnPeXNZ5FKR3ThBH-d2Dl5fjUJcbTJMTD_mijCSpIwXXVCg73INvMkQLz7soVbQ43fQ02VrZocGpovJEyJX0NGSgEFel6OzMviCfCVmApK71sxjE37JOCDecZGJFuYGVZf4TxUGrd6Q7p_ZZWS1HfQNVAx968vZaChQ3UWQhclmM1vtk_z2RI4IICw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🙂
🇮🇷
نحوه برخورد شجاع خلیل‌زاده با مدافعان تراکتور: حمال‌های بی‌خاصیت
❗️
❗️
❗️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/106248" target="_blank">📅 23:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106247">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63b0b11397.mp4?token=fEDKzYoL8GrkjGh8NUnVUTrO0ZyF-0j15v99M-wJC9D0vMG6gXopDlbcFC48IO73XGVg81sqBNBGcghfZ27jPRmsJayutJie1JGN1Cju5yRercxS6NWVJ7XKmWw5EPbFyiIzmWIUQbheZM814T-aRNTSIYW3J3ZTUCi342cFeCl4UVuSPCJOdP02Fv3neBVPKrkUPW1N6pAl6Mqr3nfWPcWKUW2mzrYutgnYChS4T9-IorrM8Ov3bfcFttDgmfwquDUNaiHsT8BBpM0Fbr_JbgRmnfkMf8dvUTC-oA1tEoS0Wo63RbX1eKDoB44er3hu8uPSFxOemZ9O8IJrH4zONwagBmkBpaAgWEUoDhal_7A1HWbz5I4IrZxHNihuuiPuPdItH3gVWJy8V44ShMG09hnM5ppoCAUT64a4Y2f6lxfFy1xI0EZ0_19vifJWrXTf93PA-HKobB91DBalqyp9QZwsnIsbBCK0H6aVxcKDgAhvflDRhooig6V0fLj5FmZdA2awzi5jvMbMBwcmyo_MtdgPS8Xq6gecADT5ZmUCqpO1OnYxTJTSJK-poxsoef8Ewr1UOjyZiAoW7_yU_Zob-WjtZB8jj8rmpZDWLO07JSd1l3t_LecH2HryJyDru_gAQXnIIT2cjVZPhwR0_BgSwp-yer39U3CFtiIBSgRdw6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63b0b11397.mp4?token=fEDKzYoL8GrkjGh8NUnVUTrO0ZyF-0j15v99M-wJC9D0vMG6gXopDlbcFC48IO73XGVg81sqBNBGcghfZ27jPRmsJayutJie1JGN1Cju5yRercxS6NWVJ7XKmWw5EPbFyiIzmWIUQbheZM814T-aRNTSIYW3J3ZTUCi342cFeCl4UVuSPCJOdP02Fv3neBVPKrkUPW1N6pAl6Mqr3nfWPcWKUW2mzrYutgnYChS4T9-IorrM8Ov3bfcFttDgmfwquDUNaiHsT8BBpM0Fbr_JbgRmnfkMf8dvUTC-oA1tEoS0Wo63RbX1eKDoB44er3hu8uPSFxOemZ9O8IJrH4zONwagBmkBpaAgWEUoDhal_7A1HWbz5I4IrZxHNihuuiPuPdItH3gVWJy8V44ShMG09hnM5ppoCAUT64a4Y2f6lxfFy1xI0EZ0_19vifJWrXTf93PA-HKobB91DBalqyp9QZwsnIsbBCK0H6aVxcKDgAhvflDRhooig6V0fLj5FmZdA2awzi5jvMbMBwcmyo_MtdgPS8Xq6gecADT5ZmUCqpO1OnYxTJTSJK-poxsoef8Ewr1UOjyZiAoW7_yU_Zob-WjtZB8jj8rmpZDWLO07JSd1l3t_LecH2HryJyDru_gAQXnIIT2cjVZPhwR0_BgSwp-yer39U3CFtiIBSgRdw6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
کنایه‌های تند وحید هاشمیان به حدادی:
🔻
حداقل درویش از مدیریت الان مرام بیشتری داشت و به نظرم برکنار شد چون من را برکنار نکرد. چطور برای اوسمار این چنین مراسم بدرقه ای انجام دادید ولی با من این گونه برخورد شد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/106247" target="_blank">📅 23:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106246">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa1d2ea919.mp4?token=dhrOo1Z86rrTK9Trs_jZ8JUJEOrO0L5KWLfLAqUpbFirOWmDnRqPURi6g9c41Dx2WmA3Hxl4fPAb26lfMvige6Qjcd-NZD0xjQjfUIadT1K2cFettPNrVh1LmBC8l44UE3tf8qGd1a9yNEC9X1r7wl6GG_6IZrXGyfAK8m3wq394Oj0reCFjFEyzu8U88FJNnnlyzbBZTmgBgHQ5WkJpuJivdXqNDU8eW1nMTYfOAWeQ7ZSOcrofuoPlsxmDfkOeYecAOHXDJJezMoxmq1QdZIz6BxmkXxJj1X3JHkEQtO4gKMQ2wz_Ui_i6O3BuwVkbdOsNjG9Kmx6PExwq9sE1Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa1d2ea919.mp4?token=dhrOo1Z86rrTK9Trs_jZ8JUJEOrO0L5KWLfLAqUpbFirOWmDnRqPURi6g9c41Dx2WmA3Hxl4fPAb26lfMvige6Qjcd-NZD0xjQjfUIadT1K2cFettPNrVh1LmBC8l44UE3tf8qGd1a9yNEC9X1r7wl6GG_6IZrXGyfAK8m3wq394Oj0reCFjFEyzu8U88FJNnnlyzbBZTmgBgHQ5WkJpuJivdXqNDU8eW1nMTYfOAWeQ7ZSOcrofuoPlsxmDfkOeYecAOHXDJJezMoxmq1QdZIz6BxmkXxJj1X3JHkEQtO4gKMQ2wz_Ui_i6O3BuwVkbdOsNjG9Kmx6PExwq9sE1Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
محمد تقوی، درباره پیروزی استقلال برابر پیکان در هفته هفتم لیگ برتر گفت: «استقلال نمایش خوبی در این بازی نداشت اما باید این بازی را می‌برد. خط دفاعی استقلال آشفته است و با این شرایط در بازی‌های آسیایی مشکل بزرگی خواهند داشت.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/106246" target="_blank">📅 23:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106245">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/657c84dea6.mp4?token=hSj_OZoBlEnKxrIVT1yT2la3mYWtmTSNIlpD2_y9BF6H4H4c_8agbprWlMpMdW8lJA4u-BCrDjffRIV68NbRrDhyuYgmnHqqHDkeqT3hegDyzaSyTqSM_yzyuCkHUSQFN8gpBeyIrN-iXOaiAFSomM3x7bkPCHD3x3RonD2IuHQilP5SvOqP-hLzWCKlFuUaf94INeWBUgrEXnBwTC5yd4dePlLLYqNV3NnTfpb7XWP-pEJ6bh3t9SLgzkTvXFlNaI2YSEplRi6xXOSGYsvMZmm9FZEop9GJhbItYKXJ8e-e6X5z5Ypg98xKoEpN12RUFFeh3iDFzR7y1Oi2nGcW7gnFuQ-Sk8LLZ6bIRTebgTHzEcxOVBw8PQt4Yb7QcjkG1L84jxPzJXta_iLQdUmpDQ2xpX0IZ2XIp0DPa9rAgh58RVJYc0wbE4T9d2u7_eEzA15DgHw4MEWKqoaHu8MrbDaJhUygT3rKQvzHXwJ3agIJWVzwNSClWjfwjizBOI5_hGUD6IjGfD8nhZ6gf01kHZ8T9iuopJeHJatX1r_5_5KCXCdB3BXWMIcKAgHW2d4M0U-G5EEsjhv8apPHacbHrnzdq13_J7Mg8rfEr9Jk8AlzTvohb8Vchnoijn2Gaxkp6ha4FzMtYXGwm-0iWyNvTHI8t2kGmMx_W5aKYvT40VU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/657c84dea6.mp4?token=hSj_OZoBlEnKxrIVT1yT2la3mYWtmTSNIlpD2_y9BF6H4H4c_8agbprWlMpMdW8lJA4u-BCrDjffRIV68NbRrDhyuYgmnHqqHDkeqT3hegDyzaSyTqSM_yzyuCkHUSQFN8gpBeyIrN-iXOaiAFSomM3x7bkPCHD3x3RonD2IuHQilP5SvOqP-hLzWCKlFuUaf94INeWBUgrEXnBwTC5yd4dePlLLYqNV3NnTfpb7XWP-pEJ6bh3t9SLgzkTvXFlNaI2YSEplRi6xXOSGYsvMZmm9FZEop9GJhbItYKXJ8e-e6X5z5Ypg98xKoEpN12RUFFeh3iDFzR7y1Oi2nGcW7gnFuQ-Sk8LLZ6bIRTebgTHzEcxOVBw8PQt4Yb7QcjkG1L84jxPzJXta_iLQdUmpDQ2xpX0IZ2XIp0DPa9rAgh58RVJYc0wbE4T9d2u7_eEzA15DgHw4MEWKqoaHu8MrbDaJhUygT3rKQvzHXwJ3agIJWVzwNSClWjfwjizBOI5_hGUD6IjGfD8nhZ6gf01kHZ8T9iuopJeHJatX1r_5_5KCXCdB3BXWMIcKAgHW2d4M0U-G5EEsjhv8apPHacbHrnzdq13_J7Mg8rfEr9Jk8AlzTvohb8Vchnoijn2Gaxkp6ha4FzMtYXGwm-0iWyNvTHI8t2kGmMx_W5aKYvT40VU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇶🇦
کامنت‌ هواداران پرسپولیس زیر پست‌های السد: قرارداد آسانی غیرقانونی است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/106245" target="_blank">📅 22:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106244">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9444ed9ae1.mp4?token=YEllYRrhSxkfTvqb8sDuwHkCulTrk_JpUc7M_CNaQpYuUpnZ_zXQwRGdLu0I2_BG8ZphLIfCMi7lVOdETr1QA6i7My55Mmy9Puv2aHbFehMFD2FgCrS2bQw3WE1ackHswetZK7h2W4O_0EN7SV6nl_NW9vUCqa7KT84EWWvCNMloKDOmDD2k0jBFUL2q9jldCnPWIvyXqJQrX2ADpvh91c3BpXd27imZ0oOpeonzqtpUa0UJOGyCYEcj1j0BTYZqVPXVuNsX1HBibfQ_qDmb-fwAulHz_bnxPlC-VN7xLHxK9VHeaCZWZNBc8tBO3jZn5Jri3M20WEiTFhdUmKTbfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9444ed9ae1.mp4?token=YEllYRrhSxkfTvqb8sDuwHkCulTrk_JpUc7M_CNaQpYuUpnZ_zXQwRGdLu0I2_BG8ZphLIfCMi7lVOdETr1QA6i7My55Mmy9Puv2aHbFehMFD2FgCrS2bQw3WE1ackHswetZK7h2W4O_0EN7SV6nl_NW9vUCqa7KT84EWWvCNMloKDOmDD2k0jBFUL2q9jldCnPWIvyXqJQrX2ADpvh91c3BpXd27imZ0oOpeonzqtpUa0UJOGyCYEcj1j0BTYZqVPXVuNsX1HBibfQ_qDmb-fwAulHz_bnxPlC-VN7xLHxK9VHeaCZWZNBc8tBO3jZn5Jri3M20WEiTFhdUmKTbfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💙
سعید فتاحی رئیس سازمان فوتبال استقلال: به غیر از خلیفه و گودرزی در نیم فصل هربازیکنی سهراب بختیاری زاده بخواهد باشگاه استقلال جذب خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/106244" target="_blank">📅 22:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106243">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dab1b117ec.mp4?token=U4dO6M0EyVyBrICYQRYD9X7_Ezatf859CGPM27BXoPrVsWz3CWKwSh8eFoAc13h_nrejumgyoVPqkZpKQfdtudcF-Drog7NYZLnH20Q-LCtJMC3MMIgEYBs4QyFgju5AXJ739SXMgX7M0pNu_3DPRewDJypUXUGJgaJ2bKgKYMWTEY7AusDkq3j5fQozmpClKSbdlJZjh_bmzRq1VKrBF7BXL0O3751k2eZvD7x4omnz6xw4ui1F-vL32Qx7SNEL62oOGYITfhgCL3zkW-J8zjmHwKuMcTvvOKD6zYg_OeMIE4K2-I0Sa9YB5_e5tGq1N58z2saPgUDcjwcLReCgRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dab1b117ec.mp4?token=U4dO6M0EyVyBrICYQRYD9X7_Ezatf859CGPM27BXoPrVsWz3CWKwSh8eFoAc13h_nrejumgyoVPqkZpKQfdtudcF-Drog7NYZLnH20Q-LCtJMC3MMIgEYBs4QyFgju5AXJ739SXMgX7M0pNu_3DPRewDJypUXUGJgaJ2bKgKYMWTEY7AusDkq3j5fQozmpClKSbdlJZjh_bmzRq1VKrBF7BXL0O3751k2eZvD7x4omnz6xw4ui1F-vL32Qx7SNEL62oOGYITfhgCL3zkW-J8zjmHwKuMcTvvOKD6zYg_OeMIE4K2-I0Sa9YB5_e5tGq1N58z2saPgUDcjwcLReCgRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
🎙
نادر محمدی منجنیق: به صورت اتفاقی این نوع پرتاب رو یاد گرفتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/106243" target="_blank">📅 22:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106242">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
⭕️
⭕️
🇮🇷
با اعلام باشگاه استقلال، مشکل مصدومیت یاسر‌آسانی جدی نیست و این بازیکن برای بازی روز دوشنبه مقابل السد در دسترس است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/106242" target="_blank">📅 22:24 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106241">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e3e40e30b.mp4?token=FZNX8SF6ThPTG0xFfN5rsdGspXLke2848dx8TWWT55OLBjc0OkX8waUJHWVsGmKa4rqTFtzlzYtMCQbr9NJbYe-D0OkFP-gKVV-kQcyzCgkJoUki_npJXpooaLKhclmsN4isNvDQJ-wasSQKZrCCqt6Nd6ygnn7Hc7r-gUiD-7d4n4kGaAKlAxZWojt7I2Xe8nQPPahhAWVJiEzIWGS1je1GOGxHWynCUz0XGlbfMzey9HMJi5QRPfnYFMbQPeYJ74sRWS4iPKJHMNCeI_mHbkwFcwERWDeTCgfEu43xhP6v5znTYBJ54ePMSKfzqfJTlE7BZ9zASwgd3D6jZ2z_vn3GH9WMBRC4ttRy7U2tN_v1AxM97TRIP_co_DAPH9XPOOVvcZBWltkhgzns0k2NedndHvoT_cm59KaFIsNk35zERINrrmeOVyXZfqWFZF-9iBt16NRiclJ7ZsoxkNgLsSGP7oAItVS_JR5yoLm-EC3J7COzSniOUb12KI_5S7n9Iashrpl3Hf1kNXFJxCwd9ibBReEtsENYQXC-76ar0DgjbIgKX-_tcGQSAHeE5-gYCujeO0_OtYUr-rAsZWRGzoIcSLE2KNWMLvjpuTLjLhP3qTimRSCqOrWbFauzqh3Wm3rZykt-kaKn7lVypfOXBB1Lehue15xgsabGDRE-X_U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e3e40e30b.mp4?token=FZNX8SF6ThPTG0xFfN5rsdGspXLke2848dx8TWWT55OLBjc0OkX8waUJHWVsGmKa4rqTFtzlzYtMCQbr9NJbYe-D0OkFP-gKVV-kQcyzCgkJoUki_npJXpooaLKhclmsN4isNvDQJ-wasSQKZrCCqt6Nd6ygnn7Hc7r-gUiD-7d4n4kGaAKlAxZWojt7I2Xe8nQPPahhAWVJiEzIWGS1je1GOGxHWynCUz0XGlbfMzey9HMJi5QRPfnYFMbQPeYJ74sRWS4iPKJHMNCeI_mHbkwFcwERWDeTCgfEu43xhP6v5znTYBJ54ePMSKfzqfJTlE7BZ9zASwgd3D6jZ2z_vn3GH9WMBRC4ttRy7U2tN_v1AxM97TRIP_co_DAPH9XPOOVvcZBWltkhgzns0k2NedndHvoT_cm59KaFIsNk35zERINrrmeOVyXZfqWFZF-9iBt16NRiclJ7ZsoxkNgLsSGP7oAItVS_JR5yoLm-EC3J7COzSniOUb12KI_5S7n9Iashrpl3Hf1kNXFJxCwd9ibBReEtsENYQXC-76ar0DgjbIgKX-_tcGQSAHeE5-gYCujeO0_OtYUr-rAsZWRGzoIcSLE2KNWMLvjpuTLjLhP3qTimRSCqOrWbFauzqh3Wm3rZykt-kaKn7lVypfOXBB1Lehue15xgsabGDRE-X_U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
✅
🇺🇲
بررسی حادثه ۱۱ سپتامبر از این زاویه؛ برای دوستانی که اطلاعات کمی دارن دیدنش توصیه میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/106241" target="_blank">📅 22:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106240">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16ebf2050a.mp4?token=VQICLhFztAjowQkj7UKIpq6aywK0g6PfHax4ZT12WMYYzYADOVJ9Pr9wVLfv2t1YYOopt4FUa_l2M0SEtw7r1yxHhXoPb-oJ0QaUzefOyYmRgla02hniPhyCoK-tUbBNmCirpPi9WavJPItbpoImCQfL2nByXFOIcOiqYpqEOVVIKBtTokoUpzlNPvEVUtLVEXShGsIhrBY6cNavqFY62SuJdwggUgVPLMzXhMg6g4hgyEVXGMI6Syc-VoORFvcfAzaQbGVLe6S7xf_se13EHh399R5ynqrroJW0f2eSmJYs4dW5jOQiBxy38d9PD-es7FskA5qSjK3Jp3mlAuPIDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16ebf2050a.mp4?token=VQICLhFztAjowQkj7UKIpq6aywK0g6PfHax4ZT12WMYYzYADOVJ9Pr9wVLfv2t1YYOopt4FUa_l2M0SEtw7r1yxHhXoPb-oJ0QaUzefOyYmRgla02hniPhyCoK-tUbBNmCirpPi9WavJPItbpoImCQfL2nByXFOIcOiqYpqEOVVIKBtTokoUpzlNPvEVUtLVEXShGsIhrBY6cNavqFY62SuJdwggUgVPLMzXhMg6g4hgyEVXGMI6Syc-VoORFvcfAzaQbGVLe6S7xf_se13EHh399R5ynqrroJW0f2eSmJYs4dW5jOQiBxy38d9PD-es7FskA5qSjK3Jp3mlAuPIDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
❤️
محسن خلیلی مدیر پرسپولیس: چرا می خواهند ترمز پرسپولیس را بکشند؟ چرا می خواهند حق پرسپولیس را بخورند واقعا این شائبه برانگیز است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/106240" target="_blank">📅 22:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106239">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/febf5e7a8e.mp4?token=qdz-zbSxbiWcp-11mnefX5W8D0sOTJk_xTZ8WyuO_xnT2Gr_y4Z8vJc4gFsfMyg_U_WbEQHEOzFR0Lf25Y4DaxlLGDmNNGxkc79zIuZAZxA662f-kUkWt0VMfWposDAElizLSF--cUHkVLQ7yEOGjBjDfrUSU5BVCUoD1WlkE8gyp-fOr2WZjcEOaMt_kcVeIMfrZlWZu977AjsMaWUc7KBAnjQ7zor5hO7QlLe0HOe-UwvGsw4Gv1X1QyEE-bmgaoqzpOg3L4h0ORadgxFqd3NmRwGdlwr0ewhl5yGmSChQFATeH9qpLDaYxl1Q39yl32i4NSCfw7Z-FZ0pN8KzWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/febf5e7a8e.mp4?token=qdz-zbSxbiWcp-11mnefX5W8D0sOTJk_xTZ8WyuO_xnT2Gr_y4Z8vJc4gFsfMyg_U_WbEQHEOzFR0Lf25Y4DaxlLGDmNNGxkc79zIuZAZxA662f-kUkWt0VMfWposDAElizLSF--cUHkVLQ7yEOGjBjDfrUSU5BVCUoD1WlkE8gyp-fOr2WZjcEOaMt_kcVeIMfrZlWZu977AjsMaWUc7KBAnjQ7zor5hO7QlLe0HOe-UwvGsw4Gv1X1QyEE-bmgaoqzpOg3L4h0ORadgxFqd3NmRwGdlwr0ewhl5yGmSChQFATeH9qpLDaYxl1Q39yl32i4NSCfw7Z-FZ0pN8KzWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
❤️
محسن خلیلی مدیر پرسپولیس:  2 تیم ( استقلال و تراکتور) با تیم ملی امید همکاری نکردند و بازیکن ندادند چرا کمیته انضباطی با آنها برخورد نکرد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/106239" target="_blank">📅 21:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106238">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a557a62450.mp4?token=hrg4tR6n6zG331GCbsH7cyUYqCydinkJj65JGcriD7htJnb-ZshMlVNiMn9vf8yYdc6vWWSYj0lLIpcSVb0z-5nxPIqkdG-6Ph6eHuBOlSYVuLeBFjLIfBueGkZYB7obAmTLnfmY9B-Rk45fNSJF4zdXZcS7XpogJFImFEnfi4E9UE_HiHeEgo6cZNKvweFdSpNqFj7auLzslnCNEETHCspF8UjSZV_94wso546nHf6hhhwyWXh-1UA_y485bc6IStcvelAAB2jCu1MFFZ4vUdcSjIaHWS4wXwFbIRgdb1npfOjiNI9q6TpeRKhTN67mIc_ybJg32UeKP1etGBVYXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a557a62450.mp4?token=hrg4tR6n6zG331GCbsH7cyUYqCydinkJj65JGcriD7htJnb-ZshMlVNiMn9vf8yYdc6vWWSYj0lLIpcSVb0z-5nxPIqkdG-6Ph6eHuBOlSYVuLeBFjLIfBueGkZYB7obAmTLnfmY9B-Rk45fNSJF4zdXZcS7XpogJFImFEnfi4E9UE_HiHeEgo6cZNKvweFdSpNqFj7auLzslnCNEETHCspF8UjSZV_94wso546nHf6hhhwyWXh-1UA_y485bc6IStcvelAAB2jCu1MFFZ4vUdcSjIaHWS4wXwFbIRgdb1npfOjiNI9q6TpeRKhTN67mIc_ybJg32UeKP1etGBVYXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببینیم دیشب در لیگ قهرمانان چه خبر بوده.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/106238" target="_blank">📅 21:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106237">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xx8WLc2oVc7pfFHEZNso_LVxm3PJhgb6Ri2tI_J-OQ7qRjWF2Na0sJVReLMILUp1KSKeCnrDs65dTLb0D9TB5oGTUKiv5vvSK1Nge8uZRanQs0nrfFDykusE10fVCwezGkFtutir38jLRc3vjy9DwUaJKXR71AvB8NF0BU5QDEM5DFYu_dWCRZZYseQ8JBWT1q0ZN44Sb9EnNpLHI3j39UM2VwUE-Tr6h03JJfp48DoX3ndIpfdgwzcZuECSkgajRCtx170h8NSUkze_1sLSMt-TnXya601ATgEtMuixRWMECe4BPAYwvdlwemUPB3ELious0bKT2OBjCnnVeU0PqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇮🇹
🇪🇸
سسک فابرگاس، سرمربی کومو:
🔻
«بارسلونا ترسناک شده. سطحی که تیم در حال حاضر داره واقعا ترسناکه. بازی دیشب رو دیدم. فاینورد تیم خیلی خوبیه، ولی بارسلونا کاری می‌کنه که حریف ضعیف به نظر برسه، چون در هر لحظه راه‌حل پیدا می‌کنن.»
🔻
«می‌تونی مقابلشون نفر به نفر دفاع کنی؛ همون‌طور که فاینورد سعی کرد این کار رو مقابل رودری یا پدری انجام بده، اما بارسا از هر نقطه‌ای راه‌حل پیدا می‌کنه. فرقی نمی‌کنه چه بازیکنی وارد زمین بشه؛ سطح تیم همچنان خیلی بالاست.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/106237" target="_blank">📅 21:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106236">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/525ed46310.mp4?token=Nsgrocxc9RPfInhbIrDp3GGszYKaeaTNvVYDA19qOtmQlE18HR_06mfy_-fAPFwb34auhEokdv1K-FbM3QRBAETjGPZQrJtEs9Q3_MJkmrxx4J_mjLxSCyJYx__FhZWw0_g1_om0-1OPLG0qGdGqoJ-u2vUCRsc1hPaAjcXfEA-cpMI1_bAWF3xnx8OXoQ-WaCTc2rZD8H1za4iPbZve8JtwVgsHVp4-MFGJyQ_88H2nzFdJwrQD0k2PPLpXC_JU8rPdt0-6808RqcQdrHKq9jrQzEwpcqjKnIzcLDYBF2aAgDsp5GCtNOHXcX0IV_le7k6Qggab4CDl-i3t0sGs-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/525ed46310.mp4?token=Nsgrocxc9RPfInhbIrDp3GGszYKaeaTNvVYDA19qOtmQlE18HR_06mfy_-fAPFwb34auhEokdv1K-FbM3QRBAETjGPZQrJtEs9Q3_MJkmrxx4J_mjLxSCyJYx__FhZWw0_g1_om0-1OPLG0qGdGqoJ-u2vUCRsc1hPaAjcXfEA-cpMI1_bAWF3xnx8OXoQ-WaCTc2rZD8H1za4iPbZve8JtwVgsHVp4-MFGJyQ_88H2nzFdJwrQD0k2PPLpXC_JU8rPdt0-6808RqcQdrHKq9jrQzEwpcqjKnIzcLDYBF2aAgDsp5GCtNOHXcX0IV_le7k6Qggab4CDl-i3t0sGs-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😳
😳
😳
اینارو از کجا پیدا می‌کنن
😂
- کارشناس صداوسیما می‌گوید ذخایر طلای بانک مرکزی ایران ۵۰۰ میلیون تن است!
یک ۵۰۰ میلیون تن و یک ۸۰۰ میلیون تن دیگه هم گفت تازه
😂
حالا جالبه بدونید که کل طلای کشف شده توسط بشر در طول تاریخ ۲۲۲ هزار تن بوده
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/106236" target="_blank">📅 20:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106235">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e059f4f8a8.mp4?token=DVIl25zGqzYv0cP9VqMJ_KuN7y35O4qTN0C6kvZQbV2mpAQqaHbmyH2HRm6hPdhV3BaLNyRuND31YYt9G6KNPOFaWJ300t7rUduKnifh8mHnO1-DA-muZ7CeLmgUySkkWO1OpZ_ABTl2c1qv0QhmijTepwHBwvPcquGJ3JGnXnAoybxj4C8N7_4cEI-aLXu3vOS8GHPJryCF6msFA7POPjNnGfrO9vdnbB36f2PDYNUGP3fPAmZ7GJJmuL3efyyWW8LXaGqr5iSJzlpLi8QRaKSO1HUei-sn3glN1UEAaz8ttxryxybUkOzFlxgpoTOD9oMJNDYi5O_31r8_nuJz7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e059f4f8a8.mp4?token=DVIl25zGqzYv0cP9VqMJ_KuN7y35O4qTN0C6kvZQbV2mpAQqaHbmyH2HRm6hPdhV3BaLNyRuND31YYt9G6KNPOFaWJ300t7rUduKnifh8mHnO1-DA-muZ7CeLmgUySkkWO1OpZ_ABTl2c1qv0QhmijTepwHBwvPcquGJ3JGnXnAoybxj4C8N7_4cEI-aLXu3vOS8GHPJryCF6msFA7POPjNnGfrO9vdnbB36f2PDYNUGP3fPAmZ7GJJmuL3efyyWW8LXaGqr5iSJzlpLi8QRaKSO1HUei-sn3glN1UEAaz8ttxryxybUkOzFlxgpoTOD9oMJNDYi5O_31r8_nuJz7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
فراز کمالوند سرمربی خیبر: الان که پرسپولیسی‌ها مخالف هستند 3 ماه پیش هم که پرسپولیس اصرار داشت تورنمنت 3 جانبه برگزار شود همه مخالف بودند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/106235" target="_blank">📅 20:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106234">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzlCQLfVG3XInwodGg6rUkzM7YdXqUH1YdVgGYFJS36oyM3N7anH3JbCitUEaa3YXgC4Ze2ibWhAjqbDscp8xtRUWsiehtvkU_G5YDkKeXEQKYsKgBjNcv17jcRADcYxzXALKaHS7wAO-XHyShD776SsoOZnGJBcx-6ZBuvDjcpPhRDrjjW1goNEJPtFu369WVMGojbmDFq7h91A6a45BAhwsNeVdssRBA392_xSDBpTPBG-a8hCGVFDPmdGa9njQwbZzFUM4Iy_y8muqOEDRFfJAnpF6fi6pqtQezHnKZx05Al7BmnYHgHuvyBFVdqpb7vEOVBrtIXDGl409Lkxew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین‌ماهینی عزیز و همسرش
✅
🔥
👍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/106234" target="_blank">📅 20:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106233">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7d8215d3c.mp4?token=Xzw6rbq52GUVdT_IDuAvSDAyqnBkulfx7-fW0IA6sPB5O0bu7ydJBPydTlR8-MLMYycs2FjuEX3YvMB5pPLEXmX7QRFxuCCalLj73rwhIJqBRusI5aVaPRy7L8X20bSIoiCYRRodDIQas56e0D7A7tpOvT42GKFWWTe3aAjxxrwe6_lFEi4Y6Kx4eBsE98OZ5UoB3fEksYe1APFYi_CT5427BoRQZe_Yma0_F8PqpR7G7zVuRHXPzuwfAWwYdaq64MVSTDjOwBQ8Ds4uEonM-jA7y9F5Yceu5F0_MSEddiivZAUZlg7TgGTQZGva1erHoc7MUsAvkrG25E95_82xW06gM4vXIKM42nRCzKiT0-D3frx4TEc8y3cEfYlYjdQao3xYS3fkE-GFk1OOXaqvX6KLP8Mpw62mKqoYgB0BPPmXQ4jK0U21BzxwGskFz_LA2fVTFNENxS8Wx2E1PoeF6x1xBLBgyi-DRi2stUwJsgcFyBMNBocHDbXnZAhRkeHs8J-Luf2n92nQpeo8duUnDyJDQrEi5OfyQ_xifwONh79zIS9MQkOrslflnhza-HmyySU32hq0sU1zUMOoxKP9lTZ1hR3rEz54atgiOFknDj_V9snGadIHpSkMYcIKT6O2B9khrlNcUZCfRKoatCfVNGLoxRo2Rn1yw7bKVqsMDmI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7d8215d3c.mp4?token=Xzw6rbq52GUVdT_IDuAvSDAyqnBkulfx7-fW0IA6sPB5O0bu7ydJBPydTlR8-MLMYycs2FjuEX3YvMB5pPLEXmX7QRFxuCCalLj73rwhIJqBRusI5aVaPRy7L8X20bSIoiCYRRodDIQas56e0D7A7tpOvT42GKFWWTe3aAjxxrwe6_lFEi4Y6Kx4eBsE98OZ5UoB3fEksYe1APFYi_CT5427BoRQZe_Yma0_F8PqpR7G7zVuRHXPzuwfAWwYdaq64MVSTDjOwBQ8Ds4uEonM-jA7y9F5Yceu5F0_MSEddiivZAUZlg7TgGTQZGva1erHoc7MUsAvkrG25E95_82xW06gM4vXIKM42nRCzKiT0-D3frx4TEc8y3cEfYlYjdQao3xYS3fkE-GFk1OOXaqvX6KLP8Mpw62mKqoYgB0BPPmXQ4jK0U21BzxwGskFz_LA2fVTFNENxS8Wx2E1PoeF6x1xBLBgyi-DRi2stUwJsgcFyBMNBocHDbXnZAhRkeHs8J-Luf2n92nQpeo8duUnDyJDQrEi5OfyQ_xifwONh79zIS9MQkOrslflnhza-HmyySU32hq0sU1zUMOoxKP9lTZ1hR3rEz54atgiOFknDj_V9snGadIHpSkMYcIKT6O2B9khrlNcUZCfRKoatCfVNGLoxRo2Rn1yw7bKVqsMDmI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
آشتی جالب هواداران نساجی با مجتبی حسینی سرمربی تیمشون بعد از فحاشی اخیر به وی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/106233" target="_blank">📅 19:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106232">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMH8ScQHZ0LVfw_jNVU7DuRNaTJBRU3Ejk_vNOui0meD14yeJe5u-bh7t6q4WdL7gsaXHw3j94Q96W-E8uTyu_PzE6NVSEYD_lx2F46OaCpnheZK6IEC4P1O9NXEWYCWNtV2RwLD-TvD2tsGyL0eUJLF7DsDfLNJi_0WZSevZKOybFbaBS_4cAHZVuQJr2A0B4LngM087_oEeHRkZCAeR71DchbHClETM9i29SabxpKFYLIWiAyrpVzI1c6ak1fORg0O0iBkgUetJgULhenT5M8r0IGfzH3THZJcD1Yog-DYy03aSDDtOhi403PyEcY2VzuME19F3sjSigQUrYDtbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
🇮🇷
طبق پیش‌بینی‌ها، یکی از پربارش‌ترین پاییزها برای ایران در راه است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/106232" target="_blank">📅 19:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106231">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be84e2f3d7.mp4?token=ZvdUF_eMJVHIOJPH4sz4Um5qXQeZmirGDeFF3JYJgOes-si-BEenwPxYl5O2vZMCUuW63eEIh653JstdZIReceeydhcK37PBEADn8VPW6eYbVkhT6DiBj_3SwizkhChvLfFnhoQAx3jjEpi0_Z_GF0YAQW58jdV0n2t9PjMg9HYZ5_mUyLZdfMvbWCkVcX_yGaug8SJS9RYEBhwPJGc2c4-uasKvKUsFHx6AVxl91wlfS9Jn-43ZAZLDaZGfYcxdf8JCAOAp4ZuN5cheVsumB1ftsnj65sVFDnwDe5KcbEmG_-dJcIb6tRF-SJLecCJAarPrCZvFEiHqlPsYmTRp1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be84e2f3d7.mp4?token=ZvdUF_eMJVHIOJPH4sz4Um5qXQeZmirGDeFF3JYJgOes-si-BEenwPxYl5O2vZMCUuW63eEIh653JstdZIReceeydhcK37PBEADn8VPW6eYbVkhT6DiBj_3SwizkhChvLfFnhoQAx3jjEpi0_Z_GF0YAQW58jdV0n2t9PjMg9HYZ5_mUyLZdfMvbWCkVcX_yGaug8SJS9RYEBhwPJGc2c4-uasKvKUsFHx6AVxl91wlfS9Jn-43ZAZLDaZGfYcxdf8JCAOAp4ZuN5cheVsumB1ftsnj65sVFDnwDe5KcbEmG_-dJcIb6tRF-SJLecCJAarPrCZvFEiHqlPsYmTRp1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
به مناسبت سالروز واقعه ۱۱ سپتامبر یادی کنیم از همدردی مردم شریف ایران با آمریکایی‌ها؛ این درحالیه که کشورهایی نظیر عراق جشن و سرور به پا کرده بودن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/106231" target="_blank">📅 19:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106230">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boac1O2nE8BujbDKwYYdN4sOTwTOoSwz9DjKycb3KZV59b3olfFFFzrt8-qmjTCk860paLM7MyLfFGdOHzmVZRX3wZiEylFmFU-N_Bm_Ft53k1pHbJohncTFt76leMKjt4tfUO-TurkXldy6B_jJtLlYSfj3A0blBkzP-bQA3rFzVBd616maQ_5pdUcRGSZxuDvSII5Byq5CxjYyKMfI0gWA0-rKc_E33aMl2S25K2dkmGKqbOvk4v8qM-0tUyNXqb8lH6uM7d4VBsD5r_lNWE_lUqft-dN4nJapeVJQ6vNV5bTdq4M1ne1OIdkW6VmjFXTqUnWkaY-r1Qy2cnxEQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
👋
گئورگی گولسیانی مدافع سابق پرسپولیس ‌و سپاهان از فوتبال خداحافظی کرد. گولسیانی زننده گل قهرمانی پرسپولیس در لیگ بیست‌وسوم بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106230" target="_blank">📅 19:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106229">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5lsv60n8hd-1SYXremHTCHJvbbiMq8GeSOp2N5kIxdjsBOv30N8C_Qktous6IDxXnqKekkrKo9PTkR5K8Z0PrO4jIcL2m848PxkOErS8n-qUNgHp8ZSeHhdhV9X-mGyR-DGc6AWl2VE6_ycBAIAIxbyz4kuOW9xnNhZ9pBCT5sqS5cBmi2lbEoAfXq0UvToBp2ww6Ad7G2JDVWMf6VNzkpd0dFMNG1OKoiY8lW-D21netI9LNGEsDO_4GDZBiYng80cWxCYVvLzx0lhimq5aQqrN_6xWGPf4qo-pARRle-meL5k-J8KFbr9CYeFGyl5BP89FKN-yIxKZDqN1-Px3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🔥
🔥
🔥
اکتبر خونین که در پیش‌داریم!
🗓
🇪🇸
🇫🇷
20 اکتبر/بارسلونا - پاری‌سن‌ژرمن
🗓
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇩🇪
21اکتبر/آرسنال - بایرن‌مونیخ
🗓
🇪🇸
🇪🇸
25اکتبر/بارسلونا - رئال‌مادرید
🗓
🏆
26 اکتبر/اعلام رسمی برنده توپ‌طلا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106229" target="_blank">📅 18:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106228">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106228" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106228" target="_blank">📅 18:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106227">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwQ1MF4PW7y_XfnXjnXcJA3jSiNKbGwzISdfpeKfMNoTSU3uML7P8AVey6xmcnn6THaclvzcZF_ApXQXduwqHt93chBF5wuxylLYVZR0vVOS2rENp_8aav9Icw4Cho_Oe3cONrg0DTC6LnpUgq-4wMGzhq-61YM2sjhvHmefXCQws_UEPiKeTPQrmhfMVHwwLYgT0cobfFew1u1eSiucT361J11iJtwZxrD55T1Sgz7Xyi5FMhwOfB7-pn0FeqE8rWGx61zY1geRYuRtlEZRH8Ji6Ry90_mpShffrqH52RYM1cixSoN3DAwIG5MPbqdQaDF9doFNnrolRIIaYsqAkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106227" target="_blank">📅 18:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106226">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pG6vMaviEdnLPJWmIzK_jVxVFnnDnchohUXwPtjb_jaAoroAJlpXTHmBH9s6myprQUPGThnyImmSsWyLt8EakGs2aRpTflCyydDZlgCafpYg5zRBrlm_sEQMNLfk8IIoWuGdh7TxwYF8sjDVpsiafgUvaRnqj_69LDdRGptDN97HP_1W7jh6oEgSVmUL0EgprQXrCwg-q3YfgaXt1AS2bEtRcknUpOTK-0tEbz8hy9L2eb0AH6Ekr6Xnkc8Y4t3Lr7oYSpHwbzlyWrJi4pAzBhMaLgXnnH9gIr8c0d3FnUOwfM21LY-yQl2p2Mqt_F3PyoVuZWw2klEUmRb4vee2ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇪🇺
تیم‌منتخب هفته‌اول لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106226" target="_blank">📅 18:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106225">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e1c6bb479.mp4?token=DYkqT-XUnN76nvKgjOcvuggoxr3NfiJsKebf4cfDp0_C-U7LYei-kJrWh5EpxJhVfmx8qeREWgaLt0M9u4ZjIgWnaRl7-T2Ltxb4psE1RGLCbEV4hoIZmYIsJeUctomgnNs3vkyg_PXBzxckFnvG0VlGN33-ywqnmi354SS9zq_k8sOUmzptzApnKJ9myWeKRRqmuGrl7EYtzvxC-UgGCi5PqSVUzGnLO0SNJtfxzzBQbNLkGS-ZRveGHxupIy7OZuY2ResPIK8DqZ40TZbsyLttg4YXm9iUePqGD2F4KouLBYGaL9ZyKAtRpOcJynTCuVuoAEb1Nyz6sIyC0OyTxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e1c6bb479.mp4?token=DYkqT-XUnN76nvKgjOcvuggoxr3NfiJsKebf4cfDp0_C-U7LYei-kJrWh5EpxJhVfmx8qeREWgaLt0M9u4ZjIgWnaRl7-T2Ltxb4psE1RGLCbEV4hoIZmYIsJeUctomgnNs3vkyg_PXBzxckFnvG0VlGN33-ywqnmi354SS9zq_k8sOUmzptzApnKJ9myWeKRRqmuGrl7EYtzvxC-UgGCi5PqSVUzGnLO0SNJtfxzzBQbNLkGS-ZRveGHxupIy7OZuY2ResPIK8DqZ40TZbsyLttg4YXm9iUePqGD2F4KouLBYGaL9ZyKAtRpOcJynTCuVuoAEb1Nyz6sIyC0OyTxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
پخش‌صدای بانو هایده در مراسم هفته‌مد در نیویورک آمریکا؛ روحش شاد اسطوره
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106225" target="_blank">📅 18:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106224">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8904bfcc25.mp4?token=NoKrIchkZgNk0cfaueYkNkPtk4CNk6MaRSj4SdfnEgjEaF6ndwPloISnEOxVUF35FDb_fxIu_oxRnbD2cJ8duKJKNN3Q-p4LouSlkkG4uSuiKDCWrntOuqVQzLx0bqHc6ycqaLQCYuNpeiP_w-Ma0RHIRHfGiaAGVi_Ra8WWJ2tFesDw2oBsd606ZhN0UI0mYVy6Oa2WIg7hBFAaZv3VR2cENlBwZyFsBac7y-p88en7LiQ4msXa51qRnTb5A0K3ot7kvbjggUPfcPrxp6pT1c1SWmVhAOvV2ucPjFJb4m6oCdsFXgzIgYBA5yS4d1J24qNGXZQ6p4sHo8R3tLZ1NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8904bfcc25.mp4?token=NoKrIchkZgNk0cfaueYkNkPtk4CNk6MaRSj4SdfnEgjEaF6ndwPloISnEOxVUF35FDb_fxIu_oxRnbD2cJ8duKJKNN3Q-p4LouSlkkG4uSuiKDCWrntOuqVQzLx0bqHc6ycqaLQCYuNpeiP_w-Ma0RHIRHfGiaAGVi_Ra8WWJ2tFesDw2oBsd606ZhN0UI0mYVy6Oa2WIg7hBFAaZv3VR2cENlBwZyFsBac7y-p88en7LiQ4msXa51qRnTb5A0K3ot7kvbjggUPfcPrxp6pT1c1SWmVhAOvV2ucPjFJb4m6oCdsFXgzIgYBA5yS4d1J24qNGXZQ6p4sHo8R3tLZ1NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇪🇺
برخی از اتفاقات هفته‌اول لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106224" target="_blank">📅 17:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106223">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3be86e9eb1.mp4?token=KQmc51kXWwtqplImuDA-JP11zd_pEGpVCA_xGDjapHJYMxhxIKSlCZfvwn6gBOmdGiqDzJ2PUJCKW1YeSx3vocgdsBFvYg4E8EB3ruwTdUE4TfMxijaeWK40XKbpaCtMyWI87vZ9n5uegYR2B7Yf0L2wLgzsT_LPni60x_FkVo_K_joZYRd9xy5g9vqg_t1HLV81cv9BK2vXIkYoVm3c-8PM96RsW5-XjlEGWxNvo0M9cWHUiuMuV4M9a8lXfPMcfbxGV8tIojYCJGDCjc65YjzTwpAn_w7-VqYtoeBEsoa0lv_afgdkVY7OD2UaWabsRrr2XARxAJwI61lJ-lgnKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3be86e9eb1.mp4?token=KQmc51kXWwtqplImuDA-JP11zd_pEGpVCA_xGDjapHJYMxhxIKSlCZfvwn6gBOmdGiqDzJ2PUJCKW1YeSx3vocgdsBFvYg4E8EB3ruwTdUE4TfMxijaeWK40XKbpaCtMyWI87vZ9n5uegYR2B7Yf0L2wLgzsT_LPni60x_FkVo_K_joZYRd9xy5g9vqg_t1HLV81cv9BK2vXIkYoVm3c-8PM96RsW5-XjlEGWxNvo0M9cWHUiuMuV4M9a8lXfPMcfbxGV8tIojYCJGDCjc65YjzTwpAn_w7-VqYtoeBEsoa0lv_afgdkVY7OD2UaWabsRrr2XARxAJwI61lJ-lgnKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراسم تشیع جنازه بابای مسی با علی‌آقا دایی
😂
🚫
با صدای کم‌گوش بدید فقط
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106223" target="_blank">📅 17:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106222">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLLuflheP-q7iGrs-HCYmQDpYE5mRl8eOGjwKjt35y6zhEiSm4RarQmALodOk14s42MqzuGJm8z_jRGQdsQDEmSE2HfqSTWOVy8H2xRRpGdD9nQtO_Xe6pjMeE2ixQHDJ2QvDI5sEGDNx_AjCYsbkoLb5dHe3lu11NSwK-ObTb38zfkipV-jXfw7nkmTYKXjNigoZFm_MNJU6Ik8ll8vsdPuKzyCV1qT9ox0P1ParclpWkTFpQitGYW9hC0oE4rAkAnsoMQIa1bjnin2cgFSJFGUFgCxJh3ukBJFeF9bkTeqAMKxVVkayKdP6MLdOdjZ_q5A1KwL-XDdyowZXbuIow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
واکنش علی تاجرنیا به بخشیده شدن صالح‌حردانی توسط بختیاری‌زاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106222" target="_blank">📅 17:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106221">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d24125c19.mp4?token=ILxV3iOBCeUBaoA2EYzQyI3esjvvXl1ETxTz4SY9_bRjTCNrHh22QT2L46rusJ-QQR87oHHzqvJD5GKkhKcmszDswsEHioWJL2ureosLzLbypwL1fptWFotYvJsonGp6kLWVGonn9eIjz0G-3INjyjpjnkBe2OYKBWjj-2nKlvelq01sCC8TuegLdxb_KwPmDVVfUWy7ExH4YhSD8EXFsCXdxxZirlu1jr4geOCE9RnsAmojiOTNFRBYrmWuNmDvrnu3eQT5Xy_5DqmGa2cKIbMLM71gvBIYz6G35XqqGZxUorRjcVlJjccbs8Bsxn2dPa-RWt9ywn-_okNu8ZQfABJ9Kt8orWAUXL25WbuOJBOlvyxPucXMhsf8A7S4FYRdXvZ9V6LSh0tshAzAMUHkMQQOdQ5M0VkjeT8xOdZO9fNXcryP_4LeZ3cgBeHuEZtYxFAc5VFEOS_OVpVs74G07jlbTZiMD8oru0-Zu-PzhIZNGQ2pjl-kScGRY0QeFOAOEl2IhBtIlWNRU2B7fbViRFHVMbIFVuvDoLO-urys_U5x4IWU7326A_OkEZ-11mNFDxXuf8o5aSkSotR88x4qfJksHQyBWN_lCNIWzLGBEahBsY62C2hX6wr6U8cFrbtI9_-Hvo0JWhlaSk7WxjBvOM40g5XdrGP5WVhCeufV0K4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d24125c19.mp4?token=ILxV3iOBCeUBaoA2EYzQyI3esjvvXl1ETxTz4SY9_bRjTCNrHh22QT2L46rusJ-QQR87oHHzqvJD5GKkhKcmszDswsEHioWJL2ureosLzLbypwL1fptWFotYvJsonGp6kLWVGonn9eIjz0G-3INjyjpjnkBe2OYKBWjj-2nKlvelq01sCC8TuegLdxb_KwPmDVVfUWy7ExH4YhSD8EXFsCXdxxZirlu1jr4geOCE9RnsAmojiOTNFRBYrmWuNmDvrnu3eQT5Xy_5DqmGa2cKIbMLM71gvBIYz6G35XqqGZxUorRjcVlJjccbs8Bsxn2dPa-RWt9ywn-_okNu8ZQfABJ9Kt8orWAUXL25WbuOJBOlvyxPucXMhsf8A7S4FYRdXvZ9V6LSh0tshAzAMUHkMQQOdQ5M0VkjeT8xOdZO9fNXcryP_4LeZ3cgBeHuEZtYxFAc5VFEOS_OVpVs74G07jlbTZiMD8oru0-Zu-PzhIZNGQ2pjl-kScGRY0QeFOAOEl2IhBtIlWNRU2B7fbViRFHVMbIFVuvDoLO-urys_U5x4IWU7326A_OkEZ-11mNFDxXuf8o5aSkSotR88x4qfJksHQyBWN_lCNIWzLGBEahBsY62C2hX6wr6U8cFrbtI9_-Hvo0JWhlaSk7WxjBvOM40g5XdrGP5WVhCeufV0K4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
یک‌دقیقه با کورتوا بهترین گلر فعلی اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106221" target="_blank">📅 16:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106220">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0df98090f.mp4?token=eo8LEHvgf_P3NloMLusgBSszZ62JJ51qTKEw9UKwDl5P_H7a--uswt33mL0UvicieGExeGHdU647Dzdk2h35_htXPM7SApUncoQaRnmwLvlVdLPymIM6ZQmnkMXRVXPqF4URXlB0-DE3q4VvONrkL1tFtKYmgngtOBwiCtvktRISl0Ux6OxHh1pDPqH5PICHtmG1ijd6Jsbo3kpzU7xcYaqf12O7096K0ByMr1GS10Gs70KXJcWMpiz53_l5KeacASQl-aBPFTj5Uz-5S8dveNKXGpmqHgRNClS5M_e7RUBhiAJOm0OkGILElOVi8z2mzc-dCSHeUt9oqKhXnriwH6IzQpOQObrwBquMQZvyz6XSshTWG9ymGeze2Cndj0QQOuryACn_jQeXsPrRUeqqrPT7ahsnZojUXEiZBN_HD_65aTe7Rq1ltan3IJc5dCqMw5FRCDkPkRGaVJot5YXMHtRkqz8d3gCWOTKWEAtcxsFT4XiIDSKDQ4dgWk5y4xadGerm0sHHjMeTpKT9BQN0Kb4Jw_YR9ZbAuzmo82yJNvnZtcbBVMbWrmAGfaOfucr_mB4bPjyPQRaIAE7c1UpV_Cq1KmjoZVIcOSFWbTbfAbyvIKQ4Jcov7Y4ljk9dzmuzwbt4I_LEdKkxcGZWVMjqAep-HhNhmYT_CrCs5kmvOoM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0df98090f.mp4?token=eo8LEHvgf_P3NloMLusgBSszZ62JJ51qTKEw9UKwDl5P_H7a--uswt33mL0UvicieGExeGHdU647Dzdk2h35_htXPM7SApUncoQaRnmwLvlVdLPymIM6ZQmnkMXRVXPqF4URXlB0-DE3q4VvONrkL1tFtKYmgngtOBwiCtvktRISl0Ux6OxHh1pDPqH5PICHtmG1ijd6Jsbo3kpzU7xcYaqf12O7096K0ByMr1GS10Gs70KXJcWMpiz53_l5KeacASQl-aBPFTj5Uz-5S8dveNKXGpmqHgRNClS5M_e7RUBhiAJOm0OkGILElOVi8z2mzc-dCSHeUt9oqKhXnriwH6IzQpOQObrwBquMQZvyz6XSshTWG9ymGeze2Cndj0QQOuryACn_jQeXsPrRUeqqrPT7ahsnZojUXEiZBN_HD_65aTe7Rq1ltan3IJc5dCqMw5FRCDkPkRGaVJot5YXMHtRkqz8d3gCWOTKWEAtcxsFT4XiIDSKDQ4dgWk5y4xadGerm0sHHjMeTpKT9BQN0Kb4Jw_YR9ZbAuzmo82yJNvnZtcbBVMbWrmAGfaOfucr_mB4bPjyPQRaIAE7c1UpV_Cq1KmjoZVIcOSFWbTbfAbyvIKQ4Jcov7Y4ljk9dzmuzwbt4I_LEdKkxcGZWVMjqAep-HhNhmYT_CrCs5kmvOoM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇮🇷
واکنش مجتبی‌پوربخش و علیرضا مرزبان به تصویر تلخ دستفروشی یک‌دختر خردسال در استادیوم اراک!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106220" target="_blank">📅 16:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106219">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBnEwUpchoIx3uzjcKztMe1zGytsySqGNDEBxJx5dMvC8-hK9wr6Xo1dzCqsCjvnK54uBUPucwim2WYLLTf47hL3R6Ru8-MMy0IjSyzwwvn437lVbtPrPG_hDJzvg00JTJPEAa52VO7wB-chuJp_BUYyfUJvgjYoFKVgZyqLYipYT2lxny6G9hkwytTnCWl_tyKxF4_dOPUdV6Mo-gF0ES2k8dbIjNPuTAGecYzPlaBzYcTwQKDM6IcroY05wZXRmXJZbJwg_u6YDiXwF63JNEdAeiVgGsWgJ1tqTYMyR1gDXnJjfE7mvTjShxaNQOyRFf1NB0h-87s_vDRbMAx5ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
‼️
📊
🏆
سوفا اسکور: مقایسه میانگین نمره رافینیا با نامزدهای توپ طلا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106219" target="_blank">📅 16:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106218">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCQM3wxnJ2Y7FeGSfLP-Al7ZcB1U72FIpD_-o65JRaq1ZXid4DQkB9SPQ2buHPkJQSxmCygN36XkzB6cykN9HFzQ3IjQf1Nn0F-3fIGux7inOq1j-cTYVwVqgIHvsWcQ7OmGRdOkipKl8Lfqwpw3gzoOjwdgenUE6nfWZrXADQ74bITx62rusy_gLO5PFO5FE_UE-k8vlN21DxofVjBkXdNQASxVeneLtxCz3mJlfSjfbFWshda7e4kY26xhyAsY_49C__8ROMBxUtELKXu5S2goKr4q9VsiuyATFBty6ySBGsfSQydhDn0ZJwfGeF3Qh0P6AYW3qURUIZX99q0zsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🤯
امار و ارقام لامین یامال در کریرش
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106218" target="_blank">📅 15:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106217">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88e638c5ef.mp4?token=d3i5O04qqE4lhZNmluFPSaoVTOfKOcgNAvrVf0HXRXCVZw0J1N6dacf2hYPv_Ea2Fpc9EGAy-QAQ3MNOMXT6icEWSeaboC85uQ2r0y1-cPtzpBKirOftpB_wBCNF2Z9M6xlUqd5IO1KXW-KQafrhKIru9D8XnSc4EcLLPzio_qZFj9YS8hD6UlGu5OKZ6XE9eEdACEl1LOH6p2Fmx7MI1vuodQRQhlYsbsXdzJ8O-ym0GAldN1r0ACzDJN2sWCSwtivbLNBir0t_wAc_B9L_t00dxHS_lxtlQRGK3tenrb0-Y1olseMHPQzCBsMupp0M1nQayx4ZYuWxW14GijOGlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88e638c5ef.mp4?token=d3i5O04qqE4lhZNmluFPSaoVTOfKOcgNAvrVf0HXRXCVZw0J1N6dacf2hYPv_Ea2Fpc9EGAy-QAQ3MNOMXT6icEWSeaboC85uQ2r0y1-cPtzpBKirOftpB_wBCNF2Z9M6xlUqd5IO1KXW-KQafrhKIru9D8XnSc4EcLLPzio_qZFj9YS8hD6UlGu5OKZ6XE9eEdACEl1LOH6p2Fmx7MI1vuodQRQhlYsbsXdzJ8O-ym0GAldN1r0ACzDJN2sWCSwtivbLNBir0t_wAc_B9L_t00dxHS_lxtlQRGK3tenrb0-Y1olseMHPQzCBsMupp0M1nQayx4ZYuWxW14GijOGlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
از مالیدن روی آنتن‌زنده و صحبت از قناعت تا عروسی سوپرلاکچری سامان گوران مجری صداوسیما
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/106217" target="_blank">📅 15:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106216">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/225d461ea8.mp4?token=G4lLg10Fs2wVZQIRZioncsMFgKktp9z7lGtevI2GQZJKRwh-OwUFVmwWLxwBPOC7uyOD2VgqU66WDPo7WFeIOBzeUeO9aHZmyQQl32zDNDJ9kop_KXXR-1BuFvJAqQ-949-UMSKHU1Zr2VYyv_qdBWftI7jaJayFC27ZVM2FsVtLjtlQOFWZXAcjd2lXNMulGP6F6TaFXuHV1wEaH81ej6E0wfPcvxYuL0UAokihm60dIOixZ1GP2F42BQOwD7QL_EIk1Yxl6147JXmx3kYOYyJ-QPt1jIz-ZGvc1TedtGQ6wryeT3JHcz_fBUx_jcdwvHajJjxYkTLjGuVT7XO-8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/225d461ea8.mp4?token=G4lLg10Fs2wVZQIRZioncsMFgKktp9z7lGtevI2GQZJKRwh-OwUFVmwWLxwBPOC7uyOD2VgqU66WDPo7WFeIOBzeUeO9aHZmyQQl32zDNDJ9kop_KXXR-1BuFvJAqQ-949-UMSKHU1Zr2VYyv_qdBWftI7jaJayFC27ZVM2FsVtLjtlQOFWZXAcjd2lXNMulGP6F6TaFXuHV1wEaH81ej6E0wfPcvxYuL0UAokihm60dIOixZ1GP2F42BQOwD7QL_EIk1Yxl6147JXmx3kYOYyJ-QPt1jIz-ZGvc1TedtGQ6wryeT3JHcz_fBUx_jcdwvHajJjxYkTLjGuVT7XO-8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
▶️
حس‌واقعی هنر در ایام‌قبل از انقلاب با حضور ستارگانی نظیر بانو گوگوش...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106216" target="_blank">📅 14:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106215">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDyzkyGXuhwcHma2DJtNcPBLPBiuCfCXBm6_99weEKvTXwCzbKYoeOsBza5LjtPG2f-kSY5afgxqLYW37REtX7GWC9BKOx__npA2LiNsdNHdgvnVPkvpklTrNFLevL3aUy3tumXwgkNdZqASINx-6KD1dJUicibNL9UCHQ2JOekCQ9_mU0cXE69XtfTouuIBO0zq9e35g3-OhbYIecgQyBQelPCIG-jQ35xPbcYYKMCsuzs1dqD-8qvH_l5NwiQtXV81qgikbWEbHi10OvGCgHG1byWUucpuRLknu2pvSEgrn3ahXRhD-ADOMMCKmBc9DFIEn7oPA-AgskU5IhemYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
💥
🇪🇸
عملکرد فوق‌العاده رافینیا از شروع‌فصل:
🇪🇸
الچه
⚽️
⚽️
🔴
🇪🇸
بیلبائو
⚽️
🇪🇸
رایووایکانو
⚽️
⚽️
🇪🇸
والنسیا
⚽️
🇳🇱
فاینورد
⚽️
⚽️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106215" target="_blank">📅 14:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106214">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e2cd36180.mp4?token=l8FUBDqpDwMIDRxzX1mGb1PhgF3NNaspclQfpCJWVusNRXQQjkTIFAaAzN1Lp1lsApbCYlJveZ1IH9BT4q-zdsMJ4o6Yl4wkSctrVTmIHn8R6a9M6nA44f6sVld1aLIovSiyYTMxSYD3GJT8m8N5IN_sUCwWAZNSSY4NPb1kxGRsNcFQfSqwHcOdSnKNGSUo7Q4MjQcjBr7uLreFRSU7cfSxb_KWLJrK6xUeJWccnatoRGNQ-bo3l9_vVGRQkO5b_P8yz9CumU9LS2XZwZz-LNwgfnk4MFyxlz4crPrHgTAH6oAFpf7wAWg7TFYEa6FakbBjmmQ9L8hC_LAdnZMiwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e2cd36180.mp4?token=l8FUBDqpDwMIDRxzX1mGb1PhgF3NNaspclQfpCJWVusNRXQQjkTIFAaAzN1Lp1lsApbCYlJveZ1IH9BT4q-zdsMJ4o6Yl4wkSctrVTmIHn8R6a9M6nA44f6sVld1aLIovSiyYTMxSYD3GJT8m8N5IN_sUCwWAZNSSY4NPb1kxGRsNcFQfSqwHcOdSnKNGSUo7Q4MjQcjBr7uLreFRSU7cfSxb_KWLJrK6xUeJWccnatoRGNQ-bo3l9_vVGRQkO5b_P8yz9CumU9LS2XZwZz-LNwgfnk4MFyxlz4crPrHgTAH6oAFpf7wAWg7TFYEa6FakbBjmmQ9L8hC_LAdnZMiwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرمین یا بلینگام؟‌ کی بهتره؟
👀
⁉️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106214" target="_blank">📅 14:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106213">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAfdmg-wvPGgwY6eGBjxaiNeBqaMSG7QVOGD9fsEIQBmdYdS-osz-NRa_J3PSP31eTACEZ9nN9WHxBI8ZAItu3Yf7FSv4SZp5cLAFWcgudLAzGSAINKylbVBGZj8s2DgzV7D6vpOhAKpPz_GEba0CwHDxQ5TD4UXkiAglUy4_ov6NeL5megvBoyJKkvjTo5GLy4g1o1vTxllYB_SAaWlk5iacHLbhHQYGiro4gCwI_Dq69dVxlK35VAoVOsLCxRpVC-DlICa_mdP-7v0Fdn0BTq8_RRxHC-5jH2keIQwQ4tcCVIZfAkU2ozVf9-ArkClgkVW_SIK2wy_8BjDfmlS7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکرد درخشان مورگان راجرز در چلسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106213" target="_blank">📅 13:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106212">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4258e2b29.mp4?token=Zy83TIpLB096e3_g3lZJRCoWhn-p8DBW-C3mk8Myzl7W8fKit8FPl2ri-N3xMCJ8B7HpHjg5FvebK_fZF0zzJM_MjfT6C4Dc4rxC8bhwpW8CtNSfDv3z5WgMmp5jlNVZ3sjHRM6xbfmaSygvn1YL5XuP939xixLrRweJ6zwNvtnYfFYrNbB8dTWEPWqByuDScOARfbavs-t12RmN67t4v-DXuyQwPiNqi792nkeGvn_UrAopeSjezdUQrw-SDpJGVYoiPUlq30T_BwOYn1dXH0eKf1682ptYgwH9QAhU2HF4oX9KsGFFmu1mrtbTaeLSXEG_yvi7VNKcIY0we2rytg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4258e2b29.mp4?token=Zy83TIpLB096e3_g3lZJRCoWhn-p8DBW-C3mk8Myzl7W8fKit8FPl2ri-N3xMCJ8B7HpHjg5FvebK_fZF0zzJM_MjfT6C4Dc4rxC8bhwpW8CtNSfDv3z5WgMmp5jlNVZ3sjHRM6xbfmaSygvn1YL5XuP939xixLrRweJ6zwNvtnYfFYrNbB8dTWEPWqByuDScOARfbavs-t12RmN67t4v-DXuyQwPiNqi792nkeGvn_UrAopeSjezdUQrw-SDpJGVYoiPUlq30T_BwOYn1dXH0eKf1682ptYgwH9QAhU2HF4oX9KsGFFmu1mrtbTaeLSXEG_yvi7VNKcIY0we2rytg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
ویدیوی وایرال شده از تجمعات شبانه:
«تو تاریکی می‌شینیم، ذلت نمی‌پذیریم
بنزین رو کم میگیریم، ذلت نمی‌پذیریم
دلاری گوشت میگیریم، ذلت نمی‌پذیریم
مهریه کم میگیریم، ذلت نمی پذیریم»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/106212" target="_blank">📅 13:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106211">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62e4095a95.mp4?token=RScCpgF79zysThRiZRUPSQ5uFeO3RFl2ae8qCOi3gg3QAxxI5BtgtmaMt12j4LSGeN6dEjzPJ5ron5qUS-R2FB8KSztBGJoavXXxu7gzARni3mm7L4QOo_4_Ng7R1F1vDq_YtMBw456XWrmFz-0NbVlzlRtvIPBBCpVz8lFAQLb3PG2DkLPEOiA4SDGY1N72pZn59VvYBR-CNeVW1oyB2viNDntWnmwaUbkoYXWEeBQUgIJf1ErHCHTYaq6jZze5QNn5pgmbrZlXVeLjwjvGYCqvWyOD4tthEwoPdfo2AbQG664YS153Mnc7qQLer5RblvEOtFU-7d9rfwdqLyDyHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62e4095a95.mp4?token=RScCpgF79zysThRiZRUPSQ5uFeO3RFl2ae8qCOi3gg3QAxxI5BtgtmaMt12j4LSGeN6dEjzPJ5ron5qUS-R2FB8KSztBGJoavXXxu7gzARni3mm7L4QOo_4_Ng7R1F1vDq_YtMBw456XWrmFz-0NbVlzlRtvIPBBCpVz8lFAQLb3PG2DkLPEOiA4SDGY1N72pZn59VvYBR-CNeVW1oyB2viNDntWnmwaUbkoYXWEeBQUgIJf1ErHCHTYaq6jZze5QNn5pgmbrZlXVeLjwjvGYCqvWyOD4tthEwoPdfo2AbQG664YS153Mnc7qQLer5RblvEOtFU-7d9rfwdqLyDyHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🙂
🇮🇷
نحوه برخورد شجاع خلیل‌زاده با مدافعان تراکتور: حمال‌های بی‌خاصیت
❗️
❗️
❗️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106211" target="_blank">📅 12:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106210">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106210" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106210" target="_blank">📅 12:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106209">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1pRaHGpw58qkmxlFtTnFi8bEK9rY57cHEO9rJosq6KQ1r6JtC-jPbDK1TJkiLSdvvrO0YhdJKq0ZAk0hcU1Il3IuFIB0PL_PAiEgMdjEVSRKbcllLgBtbl5p8t08s6EeV-FRrDJr7rhVA8QgNhFGuXnELOCrCFChf-iTEPde3-Ah0ZtdVdr1HFSRWeC--i2r3dXKC5OEdL6ahgFw1ApP5qmmbeGYjD0RptEFtd3a_CqmzCse_KtxOKxn4PrExKmdD3WvlXQm1Wvxl9_YK8DVhVawYXFZRFhQugs9IJykcYdviHjn6jHw-H0HU_U6vx3gGP9BsIFHDwWdofr8Kd0-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
والنسیا
🆚
سویا
فیورنتینا
🆚
ونزیا
شالکه
🆚
انیون برلین
مارسی
🆚
رن
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
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/106209" target="_blank">📅 12:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106207">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👀
🎙
🇹🇷
اسماعیل کارتال: بمولا از ۵ تا بازی اخیر تنها یکی باختم اونم جلو بشیکتاش بوده. تو پلی‌آف اروپا هم لیون رو بردم و به مرحله گروهی رسیدیم. نمیدونم مردم دیگه از یه سرمربی چی میخوان. دهنم سرویس شده و قصد استعفا دارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106207" target="_blank">📅 12:38 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106206">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46400b9012.mp4?token=hOgrpcBDdwkjLgrdiPkOfZHW-lnXWB1zmMtsY8VGB993afu_Ms203FDY5qFoDZNEZcZ7b-q4yKiQUxSs4Ba2yGzqnk0sXpS7mmdvAU3hu6ZELjrNNU7QTxeB5Tr5MwkIxp0TthKNpVS1nw-9lTM6KxjTmRxXrYibxK7KqdFefsHsEOSukbHr49D2nwwy8z0b7JMWQqZhkVK8NFwE0PNT6WL0XmAvvbhD1gDqUncKCdTW0CAQll5h5ogVXkGhHuz4mBxtUvjAjk-c5FP7kO5wRCpxKrcRYVrvCoCuMKpyJQS3Rzayyg5ml1o0xiqpDn95NAWrF4E9MCyxMUmaguI8SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46400b9012.mp4?token=hOgrpcBDdwkjLgrdiPkOfZHW-lnXWB1zmMtsY8VGB993afu_Ms203FDY5qFoDZNEZcZ7b-q4yKiQUxSs4Ba2yGzqnk0sXpS7mmdvAU3hu6ZELjrNNU7QTxeB5Tr5MwkIxp0TthKNpVS1nw-9lTM6KxjTmRxXrYibxK7KqdFefsHsEOSukbHr49D2nwwy8z0b7JMWQqZhkVK8NFwE0PNT6WL0XmAvvbhD1gDqUncKCdTW0CAQll5h5ogVXkGhHuz4mBxtUvjAjk-c5FP7kO5wRCpxKrcRYVrvCoCuMKpyJQS3Rzayyg5ml1o0xiqpDn95NAWrF4E9MCyxMUmaguI8SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
محسن افشانی: اون شورت و کرستی که استوری کردم برای خریدن آبروی یک بازیکن فوتبال بود!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/106206" target="_blank">📅 12:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106205">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abdf4b56cc.mp4?token=Wa-kXQoBXGEnoMJJJura_NvM6vhfgLCnrgPayIdpo_AhcDv_QpFQsXdEy4hUTBOm_3j8swMJjC3dVAmSEOqVPD3MZV6HRekDHOoI95ZpQ5ZNY3iA9sE2Hl5JsF19HoET0FjhdruTxxlID3T6a880L8NaBQ2OKeK-y2USR6Zuai2m4nbWbuoQCC5qgGdXwkrDiqYcaPiX4uzO4i9_stdle34jdQTkqeB_Ik3aN4SjNlXLwfYBAsmH3riXP_LUTVJ_1bHnpGzYD4F14-L5YbAEsasEUc64GlT_qpcT5-CqeFmmjCDnx4_iLWlwnMYg9K9TMN-X40lQOxjk2MNSTTxO1RqfxLBI6MNLDbhxl1FNhfb2l-ow51n-u1sF89LRL5zpk7mvvilWVgoXbpOqLkofw2ew8EUP5LJM9qn0y0m1fYWrAn0m6ccvuq9qk47q7k23LbBEntbErSksvJoNlCZVh9Gk418djExeJ9TxT0BcmMzaPBN08j1lufmi3j-rn8mRtbPEojUWOM9j4LcBcFI14VUZr632cWChRO3dA1sUKRYapm4qdKaOgQzsxBlh_R91HqD17RFePemra3R__WqBDiB92fES6WOc4XjsspXjYXyOUifSVhwy5r_yOCjgNEcSKeC10a7iUvq7B1NMHiFvA1iHCViAa9WSDe1nOPrETWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abdf4b56cc.mp4?token=Wa-kXQoBXGEnoMJJJura_NvM6vhfgLCnrgPayIdpo_AhcDv_QpFQsXdEy4hUTBOm_3j8swMJjC3dVAmSEOqVPD3MZV6HRekDHOoI95ZpQ5ZNY3iA9sE2Hl5JsF19HoET0FjhdruTxxlID3T6a880L8NaBQ2OKeK-y2USR6Zuai2m4nbWbuoQCC5qgGdXwkrDiqYcaPiX4uzO4i9_stdle34jdQTkqeB_Ik3aN4SjNlXLwfYBAsmH3riXP_LUTVJ_1bHnpGzYD4F14-L5YbAEsasEUc64GlT_qpcT5-CqeFmmjCDnx4_iLWlwnMYg9K9TMN-X40lQOxjk2MNSTTxO1RqfxLBI6MNLDbhxl1FNhfb2l-ow51n-u1sF89LRL5zpk7mvvilWVgoXbpOqLkofw2ew8EUP5LJM9qn0y0m1fYWrAn0m6ccvuq9qk47q7k23LbBEntbErSksvJoNlCZVh9Gk418djExeJ9TxT0BcmMzaPBN08j1lufmi3j-rn8mRtbPEojUWOM9j4LcBcFI14VUZr632cWChRO3dA1sUKRYapm4qdKaOgQzsxBlh_R91HqD17RFePemra3R__WqBDiB92fES6WOc4XjsspXjYXyOUifSVhwy5r_yOCjgNEcSKeC10a7iUvq7B1NMHiFvA1iHCViAa9WSDe1nOPrETWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
روش‌های نوین تیم‌ساکت‌الهامی برای وقت‌کشی! الحق که رو دستش کارکشته‌باز نیومده
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106205" target="_blank">📅 11:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106204">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/249d50f161.mp4?token=GGyPfnYu_bYyKMcDZy824bT2yQK-FTK7ekUOvtdVDyPe7l3RvXViynjJqWfr9i7zkeKSO8qeoJmVf06RAJOo0oOqLTWwmWwR9VsINBK_jJFtNy0cbzOGYMK7caNkROxY-1DIrjKduTys-_tAzJ9azopH5LAXv_zx7eD-NpRKgiDh6OjSsr4YH3E96kyD7dMmNcxMdRCBOgtzrohu4CeBCWthtTEkhrafSznLmPid0W1DUb6l6D_VN8GxL32Sop93gLMjzOkqcf9-co2H_zsw9wYsdJxy8UtsbwECHXT0-59bQSnlz_2Ea1ILZJEXRjAx7xAoDa_EHv0CibuBmiri8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/249d50f161.mp4?token=GGyPfnYu_bYyKMcDZy824bT2yQK-FTK7ekUOvtdVDyPe7l3RvXViynjJqWfr9i7zkeKSO8qeoJmVf06RAJOo0oOqLTWwmWwR9VsINBK_jJFtNy0cbzOGYMK7caNkROxY-1DIrjKduTys-_tAzJ9azopH5LAXv_zx7eD-NpRKgiDh6OjSsr4YH3E96kyD7dMmNcxMdRCBOgtzrohu4CeBCWthtTEkhrafSznLmPid0W1DUb6l6D_VN8GxL32Sop93gLMjzOkqcf9-co2H_zsw9wYsdJxy8UtsbwECHXT0-59bQSnlz_2Ea1ILZJEXRjAx7xAoDa_EHv0CibuBmiri8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇪🇺
پس از ۱۰ سال ایران در UCL نماینده نداره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106204" target="_blank">📅 11:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106203">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c7627bb5d.mp4?token=Hdwk5mVDr23TTBPXT2I931SAOUWr0RhaWa1Y9k6nZGVUI5WNyKgwHrTYBIZTP_AOIfs2s4iWIvI6qW-zUIiDqSkCWDt4SO_zn7qXeGPNRgr7wJEa7IxTRJnYLFJ5ziE7lkU09FmC35UoVURyQxT4xWplj72Cp3iM87oJhmymYTmOp68tDiUDCOSTcmhEC3ECbVhcOhOgTXKuHwZROVOT-s65BaA0OGCbWDY21Ugk4mKl71KzOWNWd7mWEPwPbAlMDC0aQ5vottwtjkqSGoKO8fAa_sf8uvYcjXeViLNNjh0hUBt-oJxmXvm56lAIKz8659dihzS43hyJ4qf4nV5qtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c7627bb5d.mp4?token=Hdwk5mVDr23TTBPXT2I931SAOUWr0RhaWa1Y9k6nZGVUI5WNyKgwHrTYBIZTP_AOIfs2s4iWIvI6qW-zUIiDqSkCWDt4SO_zn7qXeGPNRgr7wJEa7IxTRJnYLFJ5ziE7lkU09FmC35UoVURyQxT4xWplj72Cp3iM87oJhmymYTmOp68tDiUDCOSTcmhEC3ECbVhcOhOgTXKuHwZROVOT-s65BaA0OGCbWDY21Ugk4mKl71KzOWNWd7mWEPwPbAlMDC0aQ5vottwtjkqSGoKO8fAa_sf8uvYcjXeViLNNjh0hUBt-oJxmXvm56lAIKz8659dihzS43hyJ4qf4nV5qtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🎙
⚠️
ادموند اختر :لويى ويتون هزار دلارى رامين رو با دو تومن تو منيريه مى تونى بخرى
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106203" target="_blank">📅 11:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106202">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/629b78a14c.mp4?token=MB7z6ZDeaAIJTtQ10mJ6VBQ-dw7N1mWOzMekm8r7_fhqSJ2dJpoIPWhHH_xpffmoHR8-u-g1eahprtlTPLmAuihXNq-dEEmA66UJUYN9gxcuIlvtHNt63UPNxUxnCpf6AeI7yHXvv2pj_dAaxDLl0GMvLlqVt3qFJSzrlpur06pvyd8-kmWLCcscAd34uUVDUbAduwqqNwN8edyt4vQYmzhRbCC4JSUuz4HJ0d77A9EW5uGKAA8Xm8KKdlLZmq89XuB31ODCL6MOwk9yrohuJU2nbuhEtxSSDEfGvswVNeRnHK-Xf174fJ9L4qr9Bylv8C8T2vQ9TXTnRq01ZWCXapvlrntVWeQf6b8ySwuUiAiSebQvIukrNmzmjLtVShOFT-uAtL2O6B9uDTCYy5LjICv7OXt7imRqOmlcI8fRuT1O2nqv1HNssBIzPIkViMpCX7vstb9MijluCWLfIhxXgOd2FeKxOTYIsqeMcaFpMHZJ-3s03GiMRNm1plqURLRA-qQMC09A2OjHRnd781mXfOeah046iA1Et3pWB2xzdmXYPVXM0_5XRuRmKaw_K9w_RR9gUiuLCUdHkFoZuyowrA6xMJtcvBd_c8R1Pt_wqAJ68KewpPHcSEjlbRcpkf5kXA2NLs-OlvShjksKoudkHb33i2wqURxUg8WT7kSVI3Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/629b78a14c.mp4?token=MB7z6ZDeaAIJTtQ10mJ6VBQ-dw7N1mWOzMekm8r7_fhqSJ2dJpoIPWhHH_xpffmoHR8-u-g1eahprtlTPLmAuihXNq-dEEmA66UJUYN9gxcuIlvtHNt63UPNxUxnCpf6AeI7yHXvv2pj_dAaxDLl0GMvLlqVt3qFJSzrlpur06pvyd8-kmWLCcscAd34uUVDUbAduwqqNwN8edyt4vQYmzhRbCC4JSUuz4HJ0d77A9EW5uGKAA8Xm8KKdlLZmq89XuB31ODCL6MOwk9yrohuJU2nbuhEtxSSDEfGvswVNeRnHK-Xf174fJ9L4qr9Bylv8C8T2vQ9TXTnRq01ZWCXapvlrntVWeQf6b8ySwuUiAiSebQvIukrNmzmjLtVShOFT-uAtL2O6B9uDTCYy5LjICv7OXt7imRqOmlcI8fRuT1O2nqv1HNssBIzPIkViMpCX7vstb9MijluCWLfIhxXgOd2FeKxOTYIsqeMcaFpMHZJ-3s03GiMRNm1plqURLRA-qQMC09A2OjHRnd781mXfOeah046iA1Et3pWB2xzdmXYPVXM0_5XRuRmKaw_K9w_RR9gUiuLCUdHkFoZuyowrA6xMJtcvBd_c8R1Pt_wqAJ68KewpPHcSEjlbRcpkf5kXA2NLs-OlvShjksKoudkHb33i2wqURxUg8WT7kSVI3Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
💥
یک‌دقیقه خاطره‌بازی با اسطوره آرین‌روبن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106202" target="_blank">📅 10:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106201">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c278d8437.mp4?token=ltCvL6vrHB4-X_IJcAsFlMqoJPA1QsMJ78QkieSxUqeUMIDMdIGvdv9qwJgSnFvTKhDT6_510X1Ef9QyTt3-1IKRz5TFOhg9eQqFDJknijdpO71eLXj5M07JgASqVwPh93TYM_qNwwnnqsfQZLY8a-P-n2npe-NFHgK8Us1uEmuvJTRxLoDAgryw8sMZaLW70nBbmuebCwpuTpTgWPoEOwOKMz-Iw3XSj3GnzuO5DEaca9nlVF2t0rZg_Hw6f751cwP2B-ugOqxYvnb_P8XvZPX9A-dAkkjK4onlPoxNQWwN5PHsyTChW2JNLz3N_oF6LRTpWa-s68HCrvwBMsQ4MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c278d8437.mp4?token=ltCvL6vrHB4-X_IJcAsFlMqoJPA1QsMJ78QkieSxUqeUMIDMdIGvdv9qwJgSnFvTKhDT6_510X1Ef9QyTt3-1IKRz5TFOhg9eQqFDJknijdpO71eLXj5M07JgASqVwPh93TYM_qNwwnnqsfQZLY8a-P-n2npe-NFHgK8Us1uEmuvJTRxLoDAgryw8sMZaLW70nBbmuebCwpuTpTgWPoEOwOKMz-Iw3XSj3GnzuO5DEaca9nlVF2t0rZg_Hw6f751cwP2B-ugOqxYvnb_P8XvZPX9A-dAkkjK4onlPoxNQWwN5PHsyTChW2JNLz3N_oF6LRTpWa-s68HCrvwBMsQ4MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💥
نیروی دفاعی اسرائیل (IDF) دیشب با انتشار این ویدیو از انهدام کامل تونل‌های متعلق به سپاه و حزب‌الله در منطقه استراتژیک علی‌الطاهر در جنوب لبنان خبر داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106201" target="_blank">📅 10:24 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106200">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLud_U-Stv4UO2Cb15UDgMPWwiYQlAsNqXpy8VhH3jxiA3LT-uhQ5dOof44dxpTG6T0RZFtGpKmGTAtwgfCPlXq6TShG57kP-cPQrSuVoZVP8NCl_7T13fPP4xC7RAUKM14LQ1X8iMaO_SEZJYiuMHJCpwoYvb5vds25MRA8j994R-KMperUwDQpy22FPZ0qYH3j7I94m6M-yB77sB9cWN9sj5UJLnOIKuUweZbhL0KcT1QPVkX7XfITrv-keD8RzuhcQqQgk3pxh1ewKgCfmLN706MtBw87BzSjfOSErtzW8WO2wikFIIgyTP4N3GzcMN3s81IUco5zAqeb8rd1BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نامزدهای بهترین بازیکن هفته اول UCL
🔸
فران تورس
🔸
رافینیا
🔸
ارمدین دمیروویچ
🔸
مارک بارترا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106200" target="_blank">📅 10:11 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106199">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c20f0a6e3.mp4?token=G4NmxkzqU7GNOR-tfuWIbFa5kgbkFS9PzrvgYDlRZuerEzI46AALxRmIfAjCNfFAKAcqSl63EyYPGsRjd1tYUlMVh4jw2KoE2PBkvVCXsM8DUgiQiJYAdSZK5UElY1aWLQ6LmYHGAojXX2ctBh5376r64cG82F1pq4SgkfTWzwE_m8kbZvdCFgiRKRzeXqs3QfM_1kevPbL9Dl7x80alZ046xSHFYS5xcJ5ybBea3BlDUGwuFoAlksOs7lt2tlnqPirSwFtJJnW2mdZy9bWLSPOs5x823dtSS8C0OTKH8J1fqObzIMh0C3_StZyCPlhiA7LKKdb8Q3U_L-4Tx0Cgeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c20f0a6e3.mp4?token=G4NmxkzqU7GNOR-tfuWIbFa5kgbkFS9PzrvgYDlRZuerEzI46AALxRmIfAjCNfFAKAcqSl63EyYPGsRjd1tYUlMVh4jw2KoE2PBkvVCXsM8DUgiQiJYAdSZK5UElY1aWLQ6LmYHGAojXX2ctBh5376r64cG82F1pq4SgkfTWzwE_m8kbZvdCFgiRKRzeXqs3QfM_1kevPbL9Dl7x80alZ046xSHFYS5xcJ5ybBea3BlDUGwuFoAlksOs7lt2tlnqPirSwFtJJnW2mdZy9bWLSPOs5x823dtSS8C0OTKH8J1fqObzIMh0C3_StZyCPlhiA7LKKdb8Q3U_L-4Tx0Cgeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
ویدیو وایرال شده و دلهره آور از جنگ اوکراین ؛ سربازی که شانس میاره و از زیر تانک سالم بیرون میاد ...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106199" target="_blank">📅 09:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106198">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc5454d366.mp4?token=FXipusFKDPNloL3m3YPoUTiPe3Euq2bEqFuMTHBXbUD501vjj1-8r31ro6mlDXgQ9xcU370qhn4CRQFaj7f8DHjZXVH2q8VYzVQBkXuUOt2uOYvdMPKyfUENvRPgg8q2LIacgEjouM7PDwxj-jf6M_pyeqchpyK5CwWvK2Uaw9KqevxF6M5J3KFsOMZx2X6278PIpDOJQ_z5m3DgGW5dow4gAYwVFnEuCSne5MG9QX0aDP_v1WsG0vj-iXNB-LycH4QSDDJu92Vzk-v6o-2dTfXU8NKnMgT5JvjyLpYPFIcRXy6DcSqnycaXWMIxR8xU5JwvuXPUISrOoUxIBNH1ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc5454d366.mp4?token=FXipusFKDPNloL3m3YPoUTiPe3Euq2bEqFuMTHBXbUD501vjj1-8r31ro6mlDXgQ9xcU370qhn4CRQFaj7f8DHjZXVH2q8VYzVQBkXuUOt2uOYvdMPKyfUENvRPgg8q2LIacgEjouM7PDwxj-jf6M_pyeqchpyK5CwWvK2Uaw9KqevxF6M5J3KFsOMZx2X6278PIpDOJQ_z5m3DgGW5dow4gAYwVFnEuCSne5MG9QX0aDP_v1WsG0vj-iXNB-LycH4QSDDJu92Vzk-v6o-2dTfXU8NKnMgT5JvjyLpYPFIcRXy6DcSqnycaXWMIxR8xU5JwvuXPUISrOoUxIBNH1ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🎙
🇪🇸
تعریف و‌ تمجید جالب تیری‌آنری از رودری خرید جدید بارسلونا و تشبیه‌ش به سرخیو بوسکتس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106198" target="_blank">📅 09:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106197">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf8721a346.mp4?token=t54jJ6utterLpQlxhU-Ag-rD0OlJBOtnR6aC_LetP5c4l1_30DyEpOErMPDyTuxZ0x7iwwpy9WKgdGcDtCkfMX7cAKcMua87DW_19joI1vzpOcJYXsKLmqiM9L-53QeX_E5F_NivO41TofdBI30UZnbVqVnfhIBWqwg0ZKzuWO6f5HWckk7zzN_2QywnSW8IKMh0Nri-k7-2gHfp3q7Wqfoy6WVneG8lTKcyl5TXj_bHTvuRvxqg9svDT46aHFptI2urFQbPF5XurBHd6J8W8aCPgMrB6LWkgjApsgNQyWSp-9FIhx8Zjp7Cf2OCys7r2jVQZzzoCg17httS2cA6WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf8721a346.mp4?token=t54jJ6utterLpQlxhU-Ag-rD0OlJBOtnR6aC_LetP5c4l1_30DyEpOErMPDyTuxZ0x7iwwpy9WKgdGcDtCkfMX7cAKcMua87DW_19joI1vzpOcJYXsKLmqiM9L-53QeX_E5F_NivO41TofdBI30UZnbVqVnfhIBWqwg0ZKzuWO6f5HWckk7zzN_2QywnSW8IKMh0Nri-k7-2gHfp3q7Wqfoy6WVneG8lTKcyl5TXj_bHTvuRvxqg9svDT46aHFptI2urFQbPF5XurBHd6J8W8aCPgMrB6LWkgjApsgNQyWSp-9FIhx8Zjp7Cf2OCys7r2jVQZzzoCg17httS2cA6WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
اینبار کنایه تاجرنیا به پیمان حدادی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106197" target="_blank">📅 09:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106196">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2JOxTHsTX_9hYkv6rsWrqoJ6aiJjs62JqDPsXLHnVcR0NKGhM07BDK_GBDZWsHb2nFVNPPgZHcOr9_bFFKFX528JjYpJb7ljp055Pcry2lkYBAoUU_HGGZSb1cmoqYIBckkGAO5d2LptJ8VU6vWD4SizJYv14Kg-pRIPEcMb2DeenXHlZYV0B81ZU5R1ky0feHibG0WrnDaTAPbSTKfoJIQw005njuEcCZtgRB4ZId7Ij_69ZbJPuO8tfVTaYNezFLe84B-QXjeHBwrOnv05HnDoueJrB2O8EqFNOYEj_ywMojp2Tai23oYqoWyGRpJWvZU0Bk1WzzCH4cTJzwFPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔻
🇪🇺
کمترین تعداد بازی برای به ثمر رساندن 55 گل در لیگ قهرمانان اروپا:
◎
🥇
🥶
ارلینگ هالند — 49 بازی
⚽️
◎
🥈
رود فن نیستلروی — 70 بازی
⚽️
◉
🥉
هری کین — 71 بازی
⚽️
🆕
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106196" target="_blank">📅 08:01 · 20 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

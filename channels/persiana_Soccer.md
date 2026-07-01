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
<img src="https://cdn4.telesco.pe/file/tZ1CiN2Qtmi1p-7tx9iFkCrLSN0ZyybLcO1J49ho7ZJHIdzNTU-X7cZBlxC8xryoYRAQBxRm3I0QZTQ_f4zXJnZKE8KyFe--_12N13iVYz49FGHAMbBh9n63JfvePFo_MdSMWZFhWZS_5nc5p8pCnzPAhDz20zJyhv_RKapKNTDPc-z2Ahb7EkLHaO5DIhchLR6kDkZl9kq73MXUnGOewshSZER5N5_1rwIA4B9YBdijpDB19nbcoAOiIRaX73WORcUGYPX5WqqSU0PX-HCO3QfwiQQ0eYMvtL9_1zKz7kmkDjSSdoImkDHfS_vGfCfQcJTCEZXRfxFTTRJxIo2oBg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 355K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 07:45:33</div>
<hr>

<div class="tg-post" id="msg-24728">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVXVeCxvedXByY4b_Jm_HB0fOPoIF13YuJbBbWgOZoCqGmExFmGPR6oD2LXGjwPY87pyfPYzoqJrW7J6V1jy4Nq2nFANxp9I8n5fMh6gyYZscSNMe3dV7NmeBhf5sBGxiHjN3eSwdi_XSfHxIhd09dq_0L7eCENpt0s7gwNvWnlYOkHC3c-H7FFUKKJVEU5t9JkdgLgvziIJKzYsyt0ruRNwyKG_RifS0I5V2kWLLMACwbAB9WmGgtzrlrUz50ztCKQvg3Nl-EU2crOyBArxp-whAs2ukhmDB6w2ISN31k-uHWuVH2BzuI302dauEFAnAYPbFHaNJmOZ-lSyZ6c5RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک شانردهم نهایی جام جهانی؛ خروس ها با درخشش کیلیان امباپه قاطعانه راهی مرحله بعدی شدند. گل‌های این دیدار دیدنی رو مشاهده کنید.
🇸🇪
سوئد
0️⃣
-
3️⃣
فرانسه
🇫🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/persiana_Soccer/24728" target="_blank">📅 02:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24727">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDJ64XNucJR7hbbtnovGq1X5IC8tYi_PXPAH9YUQsrBJhrU_001T8ZJENlL2jtQi43kpu6sLjJnTmTY5ecTLgomEb0WaZljsdNFYvad8BpnUos9H3ht4g0OzC0cDyKwF8itxGfLuOj3eWbikvEW_di8s3df1DyH5AhyKz6BscfPlPIEFAyfS-0uT-0DQegp1oKh-FFuT9A2McbNAOmIhPXXYob5eIbz6Vdb73lYKQIjLF7dWaCql4-2K5onwXw3NhQRPXLZ67LJVAPtU9ZHgI3ug0XPWm_k5oWeW7WWpEKlrK_4v4Ljed_CTv8lpRZImXH8rsCTHf0huZXYntsCaWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/24727" target="_blank">📅 02:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24726">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
برنامه‌‌‌دیدارها‌ی‌‌امروز؛ از مصاف سه‌شیرها مقابل کنگو تا دوئل جذاب یاران امباپه
🆚
گیوکرش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/persiana_Soccer/24726" target="_blank">📅 02:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24723">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e80e84f3dd.mp4?token=Z4YC0N_mmC2E1dhNdwbMUZ_v562acDuB1lCIu47igwPpuTnOE-dlS6ciFz3m2u5eeL_nbznj4SxlfQMU9KOUw16uBIvU8IPgd-JatR1Q9l9FEGOHHfEEq1Hb_sIQEwNLIP5jZuEYpLhN5bn-9j-ja9SonaAi-43TuNonpSpJ2FF0qfprdnaiZK_8-RE0A4xsjy48XQ2P9V-7DNPRU7QcruQi4X2CLJdjbD9gYMFrNh3eG81NoRf6XQzkcTUhPKGbB5g8USlJMdIA87me6fiDSZLUefm2TRhbwRCvDpkeKQn9KG50UYcOdXoflOBwYTHiDXUVVfNI--dfC9Gs7q8-rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e80e84f3dd.mp4?token=Z4YC0N_mmC2E1dhNdwbMUZ_v562acDuB1lCIu47igwPpuTnOE-dlS6ciFz3m2u5eeL_nbznj4SxlfQMU9KOUw16uBIvU8IPgd-JatR1Q9l9FEGOHHfEEq1Hb_sIQEwNLIP5jZuEYpLhN5bn-9j-ja9SonaAi-43TuNonpSpJ2FF0qfprdnaiZK_8-RE0A4xsjy48XQ2P9V-7DNPRU7QcruQi4X2CLJdjbD9gYMFrNh3eG81NoRf6XQzkcTUhPKGbB5g8USlJMdIA87me6fiDSZLUefm2TRhbwRCvDpkeKQn9KG50UYcOdXoflOBwYTHiDXUVVfNI--dfC9Gs7q8-rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇯🇵
اشتباه مرگ‌بار و فاجعه‌بازیکنان‌تیم ژاپن در بازی شب‌گذشته‌مقابل برزیل که باعث حذف این تیم شایسته از جام جهانی شد؛ با گزارش عادل ببینید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/24723" target="_blank">📅 02:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24722">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J47ma4SayyIgs0CJU4EPRtiTL696VwtJ0OV0vQsIspt6b4hFL_qNcu9SInmmaQnDQpcBIAscLXYAjMOhBTr142WtLUc60XybUjXaYwps4jaXCef3X8ADTzeQAIK1TX3jrAcEv8CmI_FZ0wKRu9q1DBzfmlDLz29ya2-8gyxOUAa3d3F5ow3qxL-SWhIWC7NH3rrtSaXhyNuRsROP1I1C5ZEwevvXBdYPhsce-Xe-5f47jZqmvez52ZhJin8_eFIKJSMg_MGxpEXsuWPhdbChERP1tBg6175uXUxLIbbEl-nKhfg352HN4d6QZUO5AW_2leJ9OSUeT17d1LbE6qHsMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بعداز آسانی؛ منیر الحدادی نیز چراغ سبز نشون داد: تاابتدای هفته‌آینده با خانواده‌ام به تهران برمیگردیم. بااستقلال قرارداد دارم و به آن متعهدم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/persiana_Soccer/24722" target="_blank">📅 01:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24721">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de066ea2ae.mp4?token=gQuUR2qHeybos2CQbL8_0-yD9N4LR-qfAqIhbsTJyQ7-5529tfTcW9i2h3Ys93D6bD0SVLfbXyTYMqxidw-Wuool9ZIf-AO716RhkqTinI_L69YqNDLZ3SI3pTGIUF6aQyfwWf8v-MG58EpO1HgwGu4s8UKTGnTdXIfQ7Xew1b-p33wOZp6IVaHl0VzOjHnVVdKRPGqysnaCony_W_j87GpYBxE_OnYI0zfGygke7Ig6K0bOCthbz9PrtACmNfiyBrGn4cLzIde2POTnC69iyFOFliUuWJSS79dUzecb-aGx6uPhAdqMrK6Ksx-Migeg72OlQcPw8X7ek1Rpw9xtdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de066ea2ae.mp4?token=gQuUR2qHeybos2CQbL8_0-yD9N4LR-qfAqIhbsTJyQ7-5529tfTcW9i2h3Ys93D6bD0SVLfbXyTYMqxidw-Wuool9ZIf-AO716RhkqTinI_L69YqNDLZ3SI3pTGIUF6aQyfwWf8v-MG58EpO1HgwGu4s8UKTGnTdXIfQ7Xew1b-p33wOZp6IVaHl0VzOjHnVVdKRPGqysnaCony_W_j87GpYBxE_OnYI0zfGygke7Ig6K0bOCthbz9PrtACmNfiyBrGn4cLzIde2POTnC69iyFOFliUuWJSS79dUzecb-aGx6uPhAdqMrK6Ksx-Migeg72OlQcPw8X7ek1Rpw9xtdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
داستان عجیب ازدواج و جدایی محسن مسلمان ستاره سال‌های نچندان‌دور باشگاه پرسپولیس: دو تا خونه و ۱۱۴سکه‌به‌نیت ۱۱۴ معصوم توهمون سال ۹۶ دادم رفت! دیگه هیجوقت سمت زن گرفتن نمیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/persiana_Soccer/24721" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24720">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7qVUJN9x4VxDEz6m4UAJoVe910SFityoIpZ75jgu_hpx4tnlD_xKXYgEr9hqmgrMWFZCtcMN26G13ehTsWN3Tlukd7Q5vr9U9U2yVCEVO7u2z4QWEXAjSvHCvUVOby8R4eA5OXPgir0WBmtwm0vhop8L8Rnl9YGFJ92_pYgIG37oHkuhc6zJyoMrwyOk47X221IAlsHL9RlCc6SmXMlgqf7et_IugGfCNCqCKBB03zW1Yp8i50AE4I-lTOeknNHy-eG7smyfGC7uDZBmIR-apSYI_DG9btzL_B415KekDwmc9VCppVYhW1nZE4iXzzNE0I2yZBm7JPrgoSFNJcYPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نشریه بیلد: هری کین اگه با بایرن مونیخ قراردادش رو تمدید نکنه مقصد بعدی او قطعا بارسا خواهد بود اما الان هدف اصلی بارسا جذب آلوارز و هدف کین تمدید قراردادش با باواریایی‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/24720" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24719">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSmK8Vkee4I761o4RBw5nSISJXmojyxb25iSDeQE4zLIAiMbJjzN5MECowZ_lq29fUSIYOXJeF4lCNt9-65HmUvYIG8TtgqZaPo4ENrg5SZlR11kuQrBMBk2CWPr2hCs7zv2jtNOq3aLunDR29pNnfMZOv5ZjDNqzWFfPbEd_CoU0gVNsrg4B3KGksoqSTgmxmSF3LxvZ0niK-FZvthj0AccJcKdnjTHrsrKIFnD3BeTWHCKX_JW7tFhWdh4lml6Hwv1lTObLNdDdiPVIK5J60nP5wph2Llch6MeWFzYJTyFdkbRVPYYt-bgR0sAYEPpssz-l8z3coaxbHikNO8v6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤝
از این لحظه با هر 1,000,000 تومان شارژ 1,200,000 تومان دریافت کنید !
🔞
✅
یعنی به ازای هر یک میلیون تومان ، 200 هزارتومان پاداش نقدی دریافت کنید.
🔞
🔴
اگر هم باخت بدی هرشب
🤩
🤩
درصد  مبلغ باخت به حسابت برمیگرده.
⌛
پشتیبانی 24 ساعته
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
r9
@betinjabet</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/24719" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24718">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fy-LFKMmbRcgtom0n1S_IeeeQf-63VjIoCrI6drR7EZdahbJZdZRIS49bUcLvNdGtB35GyaWEt6c0mnibV230gkmxo6FanAkiPBgnWPqank-hIXcNBUKz0JWxjV_gYw5mWQEw_42RPq2xTYAIkTweUdCC1uXkNueQTLqvBv7Kz1VLVb39Jru568XLY-TBvH1nPNMUajtMYxRw_PimXSVJvuRgtLpgHRIjUtvlxN7Yj31OfLBz67MtxcQyfAD1EQTG-3ZK9Pch2BXTAsg8U-UWiCwoYeWZ_xgFx1DuxQY_z8-U_8k7LsngdRTKvkiap39mifRA9UKSSTejzZWbRMT5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
نشریهESPN
: علیرضا فغانی باعملکرد فوق العاده خود در رقابت های جام جهانی به اصلی ترین گزینه فیفا برای‌‌قضاوت بازی فینال جام تبدیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/persiana_Soccer/24718" target="_blank">📅 01:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24717">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/df_E89dgBGGFrYZOu_H3fZHynYsq6JzF9hZsXnHZ6ayuw8f4ujHd9LtnTsXSR7YUWCflrELcS5JkGwlEVPVKJmYbMNfwARano_lz4OPSq4_x7SH6bJSUwawX74IhDOl83hXJrKeCigsoNBghAJJA_cC79CqgJ6iareii_GNszNZ3oJKBLMG39NSAhoECr6_Vw_4YepEWi9ETMuv9C8jwYUAXbRpzaU414ZG7-vafWedHMwOzmJvDvGvRMYUbhLcmFTlGwe5vsogi1RUfvo_WfR38zYuLCPGyinoKTaBk-gDXoWMnvQmN7A_HImu4AFpeYSGt4D8isToxbXOUT8ze3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/24717" target="_blank">📅 01:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24715">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQ_xPAHE_4nwqeF_tXWDFSGoIP2JPUWZJWXkuPhjv6Fb9jpaAQBoMRIjBqfU_Mwve93hZGH9iJnYG25-te4jVXcgBY2lqYO6RejGcI8pXjheJUdku4veUm8YNIyqr6AWgrs7csGU-p6T9EP2cShJTFwSnUYjWyJfX7DaSQ-2xpY9Kd0LEReUBpyeNCZiUiOjdQZrUNp2Qk7aLzHdZCXOC9n9csgaOuhy_y8rqcuWqRqZWMyg4F6r94oa7o7TyIUYFUKe7OQDwocoD52WbreEv7X3F53vShuxGtnRco1lwgoac8gkcOktcpuX3ChAzGg9nEjDILRDgqkHpy3E9M5ghA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
جیانی‌اینفانتینو رئیس‌فیفا تو دوهفته گذشته 24 مسابقه رو تو جام‌‌جهانی از نزدیک نگاه کرد و بیش از 50 هزار کیلومتر رو در یک جت خصوصی گذروند.
‼️
براساس‌برآوردهای بی بی سی، تاثیر آب و هوایی سفر جت اینفانتینو در این دو هفته با انتشار سالانه گازهای گلخانه ای حدود…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/persiana_Soccer/24715" target="_blank">📅 01:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24714">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOZ_D1udFyesgBEYScwQN4m3RXKOV2Mma6Vutm6uga3d2W7Eyhhbm48aAbGJp3MvafO0P4Zty0gHNK9aorCPOdUVYuDh095ELzE1S6POC4LDeu0R1fQPOjjF3sW2C3JYLbrMDpfTSvvMMgZzh9R-X1wZ1rRmppxkUtgDvawqzEv-tM-k8X7mEy7X3RF668iLWroS0KklFKq5HQDwpwADMNwAGmMw7RMpv8pzRQ8owLrW8py0V5bBcEv76Yawy3AdYWngPPl7Lq8tAAVgGcTgY2SS_9WroT-0UKtijLoeSozl7P3oxyW8HWm9fyKtb6qKIAgOT25wB5qsPjIBJNkT_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏این‌چجوری‌هرروزکل‌بازیارومیبینه‌اصلا میخوابه چیزی میخوره؟ چجوری به‌این‌سرعت جابجا میشه؟ منی‌که‌میدونم از اینفانتینو دو تا هست ولی نمیتونم ثابت کنم‌. مگه‌میشه‌به‌این سرعت استادیوما رو بره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/24714" target="_blank">📅 00:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24713">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9YgkOrtOtxaK6lEIS7-eX7RCSStLrcKEiU_wwmR0MBm1Zwjov1jhh5rlPReIw9xmk1x9Ucxx-JAk6zYnqGcB75MbpuVwZc7jO3xBy8NSJFVkPKePYbfM0jcOIDqvctaoQABiVujrF7hgFMi2tH2YMsmJXx3S98YdzV3tn0PbJ_sMubix6ofrX_ScS9vWCfxy7PlwHDnwEIJi-zZzGE93bnuon2Wo0zi8AI7YAMxyeSTmDuA0IzOBPv_bQcJcS43RTdUchM_8XmAeJdLFJzLMQ4RX9de5dtD3hhy_9KVPECV7vKLuKQb436NPrdaw5reSbmhihnV2GGt_O95fGlVZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اگراتفاق خاصی رخ‌ندهد گابریل پین مربی ایتالیایی سابق تیم ملی ایتالیا با عقد قرار دادی 1+1 ساله به جمع آبی پوشان پایتخت باز خواهد گشت. توافقات نهایی بین طرفین در ساعات گذشته انجام شده و با دریافت پیش پرداختی قرارداد…</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/24713" target="_blank">📅 00:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24712">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLUlMjjFP-jaqC2mZf_JkuWGl2JdANXZbsEoqk6aeTO3-N16OVOnij0EdgGn0U7PGPtsQwpMsha_Dk-Aj5CXcq2zFkwKG-MAO5G39H4Ypp_JaetuKfhwco9b2mjf0QOu7pM1-iang-6j1xqoQVPi8CHWt9pNmeLfWBXSjywy6DUTgsvh0omcKYVSdX-FSB5VaBp-G-WB9i1cBvjISvtIDPryICwLlAuI-IbCSLOZbP2QSHA1H5VKNseOmXe4G8QcznaIQDNrLnReQM_BmSZORdV0uGHqlC7jZihD4eGMWfOT-Xwslzj_-Pu5DG3j-Obl_kJZZyUbXoD-dTvhIoWAqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/24712" target="_blank">📅 00:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24710">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhqLMqkgu5rXeTUCFu7ZrF9iKLw6Iep7G5Y_UpI2b64WV9E5_uDYfgzy6A2nKjZpJpLVXM61c-YELNu-rZVS3Xgwh5lil9RrFVchzv6ijOD_A7CCEjkZeZjcqI1iUmLzyLr37rtVe2xG2eaFGX_dc7xd09jCHazAJPuR1walSGpWndsaS56HBCMCSW1pSU0Jn2JUyEpkN3qwttBvtJ0IiA-bFey1O21vVVtLY4Uh2RqLgCAx2IN1g6PNbJT8XdYhjiftkuNUeQwShTdJbgi3dgae81rywX12Ltr7G2DvnekhysFdSXIck6B206vYFoIsZOTtJ-mKcgWGQ12Pg0Awbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌دیدارها‌ی‌‌امروز؛
از مصاف سه‌شیرها مقابل کنگو تا دوئل جذاب یاران امباپه
🆚
گیوکرش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/24710" target="_blank">📅 23:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24709">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g219ldTcho1iMJ7KwQ-ouyl04AMLIDPk9EF3cqpTc9nQsLR4N4lS9oFdhOwEXAfboAwV6HDed6uhqxwQWIPTheU55LHJgpkspA48g06KUZLUa9n32O8iRkaMecwp91uO2tXBzSBLmOe9x9179hIIoU2SbmwfKtkbxpgzqrHipGGuYMI-PqegpFE_DWlLJ2GAJKTujAS31ne7h4eysWLB6cKP8GXQ1wWEgluB7mi_UKVI3PhbcAuT7K1cBLeS4xoEuxAC8MwbmYvqR2JhymTgYy7Ab70pRRDXwZ87sCnlMuklIuALt6RlfnnZglu0Bk3FNbSBmVj3tQP8dVgSrvw7jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای دیروز؛
از وداع زودهنگام هلند و آلمان با جام‌جهانی تا برتری بزرگ نروژ با گلزنی هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/24709" target="_blank">📅 23:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24708">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAN2dRqX_T1ywOxzPhoY3pvwy8VECJrbcHDiXBE_vNdP1NqDiRKF-MnkAZBcjG9GXn1U09DvjBUvuQhtX-25GnwaLBQU6Z70xOfpsFiy5EBvgIMfsSRkC8BX07yIt_MhFZmKW1ClyqVWoy1uUjeYTJAoo6U6Z7zAXqr5YmvAm28YT35nTqXjtN5Mc5sjzlyLoEK72ko7lL78Dv61MwwtPjtZDixXsjJ4TWs2_CoQVojr3fvtZIYXXikMwGo7JtP3pPpcI9EdnbvBtrlt3HfQUeVQGS8tKtwdNDC78JGgr2PnfMrW5ZgDhVt1oeAiZSjmmx-iD4ROX9L0ox5iCx5cFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
مقایسه جذاب عملکرد بردلی بارکولا و لامین یامال دوستاره‌پاریسن‌ژرمن
🆚
بارسلونا در کل دوران حرفه‌ایشون؛ بارکولا بسیار علاقمنده که بعد از رقابت های جام جهانی از PSG جدا و راهی بارسا بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/24708" target="_blank">📅 23:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24707">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Am1hd1bno0NTAnTmYjQYN-kj1MI00CRpsI4hRpqkmBgQneUVAo2C9__hE3LhTgi5ERmHZVcVHFBhQ3mlFgpDZ5nS9WpsKSM6FT17D-JNWKVWrsxlGWDYWvoVVD7SUDrYycTSoC60HwSmcX_hsu-qABGLDu8u47qdufsYmgjxgGBlTSdVUUEyOFlHaidZ2O_INOR7ZIumMpNlZVWxrHfsnTyF6lNb3_Lzy45pQ-ipu99KYjRbbwkU7L6d8fum9V5-2BGWoEX2xDSESYH69DLd3QcUhcnDVTIoEM6hZ0Gd0hW1TtLfii7yEKIgxSQyLDUoMYV470U92UpMcHMGCptSlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نروژ باگل دقیقه 86 هالند ساحل‌عاج‌رو شکست داد و حریف برزیل در یک هشتم جام جهانی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/24707" target="_blank">📅 23:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24705">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RRlWk8iUpP6eygsDaKtg3C54FCB_IA-ctz8D7sX6Hp-NCnfkoUfzx2ottN2S01Tg4NoS27kFUyax0jPimRtX2vVI1iOKSLMIRgnBWMM_IzDXi4s16aFeUeHEGCEgBoggs_E7tO7_3LgLo8Vj2GFFBX22vUyqRDHdpvKui5oNiQXXSyRWCdoYEqt2UoPxJZP556Z1FYkMuYf1-wqReXuBDtIMXKUH70qQOQZ8FY1iPIMesvL_mtzqISVoW3cyA9KfBkls_-3aZ8bCHYGHAl76QwxWqj04VzGP1Frut1YsI0qAOZPh_j2cu2tJzQYoz__K1sjOMseTl6b8ml9lKts2fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aSgg5ma3FyAO-P_HBlP9krMgT3mZXMtqKxvyUd54y-6dZYDdznTWwYscjQ6JgPElWyMQjHDS8WzhVNXhI2Uyib_nHnWaWBfVJWOkzRyLdJcSQWyXJbx_iQZwcyS-Gja4968U9O7_k8_Gj1YxjQCun8CQADuhwOoQiEHlvEtgcNgttsg7dhKyP7kFQIUio4BV8vVzYwpAvpSPROTlPifek6PubpBAkn1OfVL8qhvg-wVpxTiYg9AftXZh_pFjuH1pbtcVWzLnCXW-7nhfy0A68WHIH1xr2HZQc_cPP-msc6ZNbH_4Sr12SS7acBualmo3z8hT94n2aiDhgKgrUn_b-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇽
🆚
🇻🇪
🗓️
۱۰ تیر
⏰
۰۴:۳۰
مکزیک
🆚
ونزوئلا
صعود مکزیک یا شگفتی ونزوئلا؟
⚽
🔥
مکزیکِ به عنوان یکی از میزبانها این رقابتها برای ادامه مسیر به میدان می‌آید، اما ونزوئلا با انگیزه ادامه شگفتی‌هایش به دنبال حذف یکی از میزبانان است.
👀
⚡️
میزبان صعود می‌کند یا شگفتی در این جام ادامه دارد؟
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/24705" target="_blank">📅 23:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24703">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mG5YSnWAZvdKGUNRGSP7XKBUsEZZPN5eAtJdEqdVfwZKG7Wbzyf2A3GzEV7BKlLfS89bAEaMuoY3z3MIGUUCMNSSITeteDw75X7jeFFtMPRQCm7CWgO-qGiw7yHRJJbWjOq9BJtvqdwO6e5lHugqBldH2WURcs29qQO0h9zb4rdwzRls5SX-V0wkIX0NbB79do5QQVqzg7qWddwrT5NnTQtWKCbRwpBHPa3TUlSvZLVszpykVTxgB_FfnHRX-T-fX-IwXTBtBABL_GW_g4Z4NQ_69DGi1h_xzqTVhDsZQBRw-aoADHWCOHaM3oG56KriQs6dsqgD9xiby9HIlcJHZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vpR-JFUPWOBeEwAGZwfxY7-bae1DPr5QV09XN0vUWxEpquFEx8QbtPPaCjz-hZiXnWvyuQ8TVRCEc-eErwyC1FVJXkdhXVLkEHsVjOeio0BcX9gcHTKBGa-oSITVjuliNaF93c0KA1lRVanqs8PYjUdn3kHHG3Ho14RSBO3fkWkPR5LbmpeQxlg5VJYg3jc4Gr5SFH-ppD0vdz9hRGvBOu-FgHgEsNLhkUuxOrSs5C5j5lZ_5uoxf6N7gHw3Xditw6t_Er9tVlaKiQwA1g4GqlzcxxYg6qHLjmy-_eH5oDo19ysHuBJoq2FVG7nplWMz5ikkkOK2ylMcToVanVkHgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌هفته‌اول لالیگا و الکلاسیکوهای رفت و برگشت پس از انجام قرعه‌کشی فصل جدی
د
‼️
دیدار رفت ال‌کلاسیکو:‌ یکشنبه 3 آبان 1405 در نوکمپ؛ دیدار برگشت ال‌کلاسیکو:‌ یکشنبه 19 اردیبهشت ماه 1406 در ورزشگاه برنابئو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/24703" target="_blank">📅 23:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24702">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccKE8qDkqWHjD37RhMtQ5KeSRHZIZazEQ6gP7fKvvVwsGepaW3P4Hm0EzjAxWzmG3ERNe76GGnei7g03PeyJz0p3aDWi7LO1a8HWme2ZRxFHWCvBCC052f0DgDyitC7nFnl1vNvqhXkBe0wJbEv_YzvpXzxiEZE6-jU8n-vsvZLcjQezRzwjIesnrD6PRpahdgIc6X2B1uuCa_jMnSFhVRoFkKhhnUA8nYe6qtaY63XDrQXeKUYROCzXC7lf_tmySR9GiIveq_gt_fpklzghUUqAC1dHUMNAuWizP1fi7EA-aVEBor8uveyY8Q1F6qkU66Myljb0svZlhhrD6QLl0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخباردریافتی پرشیانا؛ باشگاه پرسپولیس تا پایان‌هفته‌از دراگان اسکوچیچ، مهدی تیکدری و کسری طاهری سه خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/24702" target="_blank">📅 22:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24701">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLnIdfs_am2_a2irfZi9CEF21zixY-pM1_5iQYYgSIh5hX2kFI1mkE9Y2BvKiI6YsVBFF6lAWTvYjIpMpx65jp3SiUqRtZK59JyGDs75iZhQQGDGsRD2uX0U0x1x97fQh5aQ92hAeBAoYXqCX3NrAg-OtX-7TRmfY4Lco_gUOzCVa3U-Z4nK6yFY6K6QHRuA0vOscYEFU5aUBomfeoTNdXO6FKSaUUH6jEq0iSozxataiAJUYA8RfcMo54cbmQpeUBcORKjy5eHYOBMv7iGf5r9FSy17clap2T1001xsghqYLiBRuSqTHcJ9y-BjGqo8TRAU1sTZgp1coxapHhv1zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تااینجای‌جام‌جهانی 2026؛ خطرناک‌ترین چیز نه پنالتی بوده، نه وار فقط و فقط یه عکس یادگاری!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/24701" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24700">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJRoAmosYAwTmtUiAs7-lkWJnwY_j3Ixtg7LGU4mD9tQHTvuefQ16dBdyGMBEFMSNL5EIHLpl6YHHWIVtSqxutTf5H9GJdaC7CR5SJ5s4VPkSNnKb0b4CrbKGDDD7iwszKbNfs_N62-SYSQg7SDChboQ4KfLAZlbIPQ43WIEAqinNAVjIKhP4iGjCQTd92kgX51l3TTXqafF6KKZ35R8G4hnlcj86vyRRKY67X69kwJeh6emxzgax8FH-tTiWZqBI7qHzjaeOBW6Qhr_ct4-jA0TA665dK5eP_sjVRyafSWTnGKePdza539ESwirHYWKV-vKXNvlLHW03Udjn8LNcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇳🇴
سوپرگل‌دیدنی نروژی‌ها در بازی امشب مقابل ساحل عاج در یک شانردهم نهایی؛ چه کاتی برداشت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/24700" target="_blank">📅 22:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24699">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XN8E5EHIz8S2wOQANxf9okRmytkNMnJz6PDROHGdef9mypBwzsUD31WcgsD6iHMxePswKVg7Imu61ByjBJ9v9cI_jauinKE54FlGfdVlikJFRG-n1yZaD-m81XYTqMQv4VkovAwIw7jMynznAUh6izF8DwQ7J15b7IISxy222VshJqR74Ell80t2cAI1tzVGVi1gSJIoUYpFHtxZT-Jv1oFAOFtttEykn_UBF9u3kztYOmnZ8UJ1BIG8M2ETaKSmBggpWw4jTteoGx7aDnplm2RTc-Jhigy10rlh46KzoD47F5wXqzzPaGsEe3cmHqTV6GA6xjdtYle4iPrT4Le0OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال بسیار زیاد بخش رسانه ای باشگاه پرسپولیس فردا پوستر رونمایی از دراگان اسکوچیچ سرمربی‌جدید خود رو منتشر خواهد کرد‌.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24699" target="_blank">📅 22:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24698">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HkVdl4aWrmcD0-A2_biYRPwxfrqKdr2cHc8CbE5Yl-nFxv_fPUDspNZkOjGmLWobLs745wwAtbvR77P1C_h6iSAU51orEwtM6dcETFVK8deCnk2maha9sFhndsfKIisZ7LsT6wIsh_lvRvTBqj8RyD1Dc4vkh7WR1-9gX9J8eYlhQe-RQavSgWImn-_M0ClY1MNpeeMYVzBO_lWxoV4oEV6GHNiagm3jhot3pQ6MiSPSk2KkYhHkBfzEXNdt-p5s6vMBowF7edwQr19vdGy_u97OkkdKxKrU2J2IUiQZzFCfKSk_ragaitLSSizhIHzyqCqk_ZAdDIUheeN_gkHVDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خداداد عزیزی در ویژه برنامه امشب جام جهانی اعلام کرد بنا به دلایلی پیوستنش به تیم پرسپولیس منتفی شده و فصل بعد نیز در تراکتور خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24698" target="_blank">📅 22:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24697">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b011e22cad.mp4?token=ZCkhPFpsjuD9KwNATGItaltgbLOZw9p2Te-06vgbXXPdksdyoD6KkgLOixa02vbl0OE4BvzENtQtxW0-fXgkGs3nvnT6gY9GZjRuRfj6Fcs1X_pi-PVGT6lLzbuj43jDME-9dxnpjqWJTi2wg232_ujwXQVVuFn3etFEWVilW-O8E0D6Iyj_KTTthIdGg-ZVOHknzbLTsvBD3xIYlMyIuu6hyVFKJtyHayvOidd69sz2yprR8nmCPE6RG3UcwWw5_s4vNev7cIqz8U-7ovDXNC07yQf3w5Fhl1sSe5ax3F1du2GQdi3PgSwlCi4ILv1n4hk4jYnp3wDy4G7Nn_MQzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b011e22cad.mp4?token=ZCkhPFpsjuD9KwNATGItaltgbLOZw9p2Te-06vgbXXPdksdyoD6KkgLOixa02vbl0OE4BvzENtQtxW0-fXgkGs3nvnT6gY9GZjRuRfj6Fcs1X_pi-PVGT6lLzbuj43jDME-9dxnpjqWJTi2wg232_ujwXQVVuFn3etFEWVilW-O8E0D6Iyj_KTTthIdGg-ZVOHknzbLTsvBD3xIYlMyIuu6hyVFKJtyHayvOidd69sz2yprR8nmCPE6RG3UcwWw5_s4vNev7cIqz8U-7ovDXNC07yQf3w5Fhl1sSe5ax3F1du2GQdi3PgSwlCi4ILv1n4hk4jYnp3wDy4G7Nn_MQzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اون‌بازیکن‌تیم‌ملی‌هائیتی‌که‌کارش‌هندونه کاشتن و فروختنه، وقتی میفهمه من رو کلین شیت مراکش بت زدم: این چه سوپرگل برگ ریزونی بود که زدن!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/24697" target="_blank">📅 21:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24696">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdMojqV6Cs3jFm147rBSxfAypPmTUufUDaEziotwWerM_ogeWQoO7oRA2VD3a026B_NuHc_k7Rv7tK_Qlz3Jx_D-skupZFKkBrotguEQgvAwKcObGmpXZto6E7wRLgh1bOno6mZri0NzLhB2OfvYs7Ym417-oHpz4-6MYbAV0J2mEv5c7anmJBKY6UQVH233E3Rr6KjaYPB0HVjvmIVATL9BhkK5Nx5s7uWBNSH4R25naOPScMyNFf4Z3EbHW7O5NlOFzwVlcVs0rtpO9hxWI3baRLTHy_RasJh3k4j0OX49dzMM5HXwoecXZhQYXmneHsx1ext-59vtZsEG9pDhAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
لامین‌یامال:
شانس تیم‌ملی اسپانیا برای قهرمانی درجام‌جهانی‌بسیار بیشتر از بقیه تیم هاست. فرانسه بسیار ضعیف‌شده و تیمی نیست که بخواد ما روتهدیدکنه. هرچند بازی دیگه با اونا داشته باشیم باز هم با اختلاف میبریمشون؛ ضمن این‌که تو عکسه هم خبرنگاره سرشوخی رو با سپهر حیدری هم بازی کرد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/24696" target="_blank">📅 21:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24695">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9726fa772b.mp4?token=KPetDvPBzAyfC-pilnTnr5XPmvNFAVmfrYZQTS6iTjE3DaC7-YzKAXuP2Ib5UH0CfW8oJijltEg4w1OJY6pi7ukn_HCVP77CpAw-O2O7RhRPP8-RTNb3sVEvth4P1p7XmM9SW9HK-6rleE17eOjUdbD9cA2hQL1t5yVJ4a73Vq8G1rTnp1igrc1kWLPEyngdb3ebQ1kO8iDjK3s-pr10rZ6DvNgIvSUbtr3U79TP5UlZDs-jQal-bN2atdQZpnWiLXrdVIHKdhpCxNcMUwPva9aytK6RvOynM2pv2bJGyfq5cXzt38dJvyKd9uLX1zdhsgSxb0ulVJVyaMzJTRU3ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9726fa772b.mp4?token=KPetDvPBzAyfC-pilnTnr5XPmvNFAVmfrYZQTS6iTjE3DaC7-YzKAXuP2Ib5UH0CfW8oJijltEg4w1OJY6pi7ukn_HCVP77CpAw-O2O7RhRPP8-RTNb3sVEvth4P1p7XmM9SW9HK-6rleE17eOjUdbD9cA2hQL1t5yVJ4a73Vq8G1rTnp1igrc1kWLPEyngdb3ebQ1kO8iDjK3s-pr10rZ6DvNgIvSUbtr3U79TP5UlZDs-jQal-bN2atdQZpnWiLXrdVIHKdhpCxNcMUwPva9aytK6RvOynM2pv2bJGyfq5cXzt38dJvyKd9uLX1zdhsgSxb0ulVJVyaMzJTRU3ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ فردا؛ از مصاف مانشافت برابر پاراگوئه تا نبرد تماشایی هلند vs مراکش و جدال حساس یاران هالند مقابل ساحل عاج
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24695" target="_blank">📅 21:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24694">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72b5a564e.mp4?token=oY_v9SK2lK3wqB9_YaMLWG1aCIjEYzjKIDkxW0vbR03xL6ARHVhEIIB5yoNL3uKWC-0fd2Bx979OrlgAICRqz9epvVh6BgRcf5p_4mPs0VXqfMVCbq7stsGGmBYrbLxd_ICWwLciG23upTLpJ4stmVB5eoGCxRyMOiVFwy0sjKEBws8IWWlYVaKjd-nTZLI71bGkKis1rdlk5xJOy_Dx8Fpd6SaVtsRrdPzSDGrEO6mHX6_9cmftyDJONAYJUdgwGIJ1kSvHj_ZchehapRM9r95zXMYLezI853b1d7kLqmzES82WiZvyc5AeiYeSi5jxgMOtKIUC5Die0DcC5WtiGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72b5a564e.mp4?token=oY_v9SK2lK3wqB9_YaMLWG1aCIjEYzjKIDkxW0vbR03xL6ARHVhEIIB5yoNL3uKWC-0fd2Bx979OrlgAICRqz9epvVh6BgRcf5p_4mPs0VXqfMVCbq7stsGGmBYrbLxd_ICWwLciG23upTLpJ4stmVB5eoGCxRyMOiVFwy0sjKEBws8IWWlYVaKjd-nTZLI71bGkKis1rdlk5xJOy_Dx8Fpd6SaVtsRrdPzSDGrEO6mHX6_9cmftyDJONAYJUdgwGIJ1kSvHj_ZchehapRM9r95zXMYLezI853b1d7kLqmzES82WiZvyc5AeiYeSi5jxgMOtKIUC5Die0DcC5WtiGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
👤
باشگاه پرسپولیس در اقدامی عجیب در روزهای گذشته با خداداد عزیزی سرپرست فصل قبل تراکتورصحبت‌‌های‌‌مفصلی  داشته‌اند و قصد دارند که او رو برای فصل بعنوان بعنوان سرپرست جدید سرخ ها انتخاب کنند. فعلا قراردادی امضانشده اما احتمال اینکه عزیزی به پرسپولیس بیاید…</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24694" target="_blank">📅 20:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24693">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6-Udv9cN13f1Enyax2S9JS8VnWNsE4-sbwMu1UiA2073DBYpc1co6o8ter_po3ddWkOzyUqDPlE3yWYzPzbeSrtIrYqKhYSfUjvHSeA_585CaZtAmls5I-AYvrZ4OKmZdlTczg2wtSGxPMD6ROELsTw2LAZcJzJcTKvG7_hTwmMrLoLGnto93V4EcloQW11kygxvpIlYKWNq_he-GVrfb069QAp42r693L1JtOFjzJlqQS0YRpBV--oDMPLkoi5ena3NP8pSBxZ-GoNOE8NjoaW6keo4wZNQlnlSdiGp_keOg0ht42a4gDVe5N8AHjSG2uOdIf-lSgKPpMVwTATaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
همانطور که پیش‌تر خبر دادیم؛ یاسر آسانی ستاره آلبانیایی استقلال بامدادفردا وارد تهران خواهد شد و در تمرینات آبی پوشان پایتخت شرکت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24693" target="_blank">📅 20:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24692">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMN7AT8fRVngPS3XUv5d3wc8MsNkCBF01IRFEn1pcTCKpBgbLwPCxhmwZDa-yEh8zfkMInVMyP_jTSKoXV5juBtMyZKzKPsK6qjOadKgD33BGzEr4QbptHtNUynTzjmLmc-mKHOu3JCF2Ad700m4bZ0o87V0sdn6bk3cLgHAnhtUJR3mpdrk2jArjDuHpA8GU33roh7A0Qs1gSa1XmlHzWblFP-uxWrebV8MQ5H_y72SgSgBs2KjvbFrdrWpXOoRSeAWziK04VefQUFv0um9cLRY_mAjuMML9irTxLyKu-myUw_H7-IogGugQQl7gGvUosIGznTnWJI_MED_x4dn_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فلورین‌پلتنبرگ: سران‌منچستریونایتد با ماتئوس فرناندز برای عقد قراردادی پنج ساله به توافق کامل رسیده و حالا توافق با وستهم باقی مونده است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24692" target="_blank">📅 20:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24691">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLjnQQ59dRRCgV7u82sDsnyiy5kzunGlS8pZaSDZGrxZ6T86CThu4IFcdenOj0eaWFU_3L0-Mf4zYY70F6DyGAEw7JjEb7PlOYq8fQNTZySu5cnni-bz5WigHW59CELTyN8JTYdWdGdtKe5oFf2rsuiqT_iBdUwwi3fKNYhrBsAz5QCSnAzfZg0gT15f_XybORI_TUL537r70llv4NWdn1cOWvNNPlzH-syMBddjBacusTQb95omkknjWLgYjFs3IVizyULnS2UeBCqmJXWuU2cR21g_a3M1M6NMyYrGFJKdy-2G0qrD7hp3kuafJ7ngYkoadVmT-Qg6acVT-gcgCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ باشگاه پرسپولیس درتلاشه امروز برای دراگان اسکوچیچ بلیط‌تهیه‌کنه و این سرمربی کروات ظرف 48 ساعت‌آینده با دستیارانش وارد تهران شود.
‼️
بعد از رونمایی‌ از سنگ‌ اندازی این مدت بازیکن کهنه‌کارباندباز سرخپوشان‌پایتخت خواهیم گفت. این بازیکن از وقتی فهمید…</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/24691" target="_blank">📅 19:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24690">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrGwScrGnSsY6uswge5bAXPzBNjLdDutkJJ_2NuEzmx4h2XB_ULAx5JGEy7M08oeFP-M94WhYRA1YZGGxnJ0zIYI8TuzBNFkd7Nu0TLBe6xIQQskIfNkkinLr4_a9uTDv_QwdIjXzg3NaJEouPxx1sEIzdx4hcUdfWY_xarTQa3iSlROYhO4UsZAD5dAiiT-yGq0hZxb6om3Z8V2KQuHotzb7gM8s3gUdXhIWmwbko3hN6AFA8ezS3CDSvbs_ke695X8RfTwzEy-VcLkvvru7rW5sRKvnFhZSNbC3Rk1JJ_nApIYPMdCvke3vNVENXR-XFy4MgtF0DT_LspxVmIsnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛باشگاه پرسپولیس و بانک شهر مبلغ توافق شده به اوسمار ویرا و کادرش روفراهم کرده و فرداصبح قراره‌این‌مبلغ به حساب او واریز کنه و رسما پوستر برکناری‌اش رو منتشر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/24690" target="_blank">📅 19:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24689">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1LhQXfUAV1hvnLemCvuhVrH58qle8UvTyaFDlSwF5wvFKp5feNRGuCbYFw4-IX-3fzZarideKCjVEsWbVA92zUu5o6YnIw5UHDsJ7b4iEP-YOcyEJp8xlIoa7Y1BcTk8hpseKMwjSa1vvxcn0TUnzS0Jgi4MVZqHYTYva2bOUFsBValbLa2K76vGAt4ovsU28YPfTARNWSYgYYpX-rpJ8GQbIOVOb4feqLCRqzs5mbQE_e36sgccM9DUOm_q0Y2aRXGY799Jue-q6AwBIya0rFQa95rH8lNb1DT1RhcnbbTuwopW_4qgBZ7kyBz7ZlVMrde4Leir4Afqrh-2__rLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ضربات پنالتی دیدار امشب آلمان
🆚
پاراگوئه در مرحله یک شانردهم نهایی رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/24689" target="_blank">📅 19:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24686">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e47b5880.mp4?token=BwHoAMbqx-apqDvXin7KeGhf01KBFSxms7oiCDnMfOSlp7QAxCXeoBwhmiFLcgc-6TvmWqjipn-jGHlnAlFd_q77ZrHA6taFzYGQOi_Ml6zlQmOzB6ytyOrtbkkWBowqLt83Gynx_DTS7zRjo2ni_kaekTME2FJJSwDznMTLJlIRFn9s6EULBgDbhZtFahSF4ItORkXzi0Ep9bJJK6Rmfh39qFE78BuEgvD39B6FHM8awIv6eydIBD9lxGghk6FgBNXaHQ_OdAKDRRUm9CqEbAE1EIRrssL_K1cfUG17mMuHzvE0__PAsPFfk2JC9wvPi9Xh6gaoFuW3gHNw186zSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e47b5880.mp4?token=BwHoAMbqx-apqDvXin7KeGhf01KBFSxms7oiCDnMfOSlp7QAxCXeoBwhmiFLcgc-6TvmWqjipn-jGHlnAlFd_q77ZrHA6taFzYGQOi_Ml6zlQmOzB6ytyOrtbkkWBowqLt83Gynx_DTS7zRjo2ni_kaekTME2FJJSwDznMTLJlIRFn9s6EULBgDbhZtFahSF4ItORkXzi0Ep9bJJK6Rmfh39qFE78BuEgvD39B6FHM8awIv6eydIBD9lxGghk6FgBNXaHQ_OdAKDRRUm9CqEbAE1EIRrssL_K1cfUG17mMuHzvE0__PAsPFfk2JC9wvPi9Xh6gaoFuW3gHNw186zSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
سبک خاص و جذاب پنالتی گرفتن یاسین بونو که قبلا هم دیده بودیمش؛ پنالتی امروز صبح هلند رو به صورت عادی شیرجه میبست عمرا میگرفتش ولی اینطوری راحت سیوش کرد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24686" target="_blank">📅 18:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24685">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c85d949fba.mp4?token=DayV63JvBtYo7iVk59NReyoqS1R3eIxpI5fv8GAm-IB87_POCHLmw5UDQqbO_ECzOEyV_Q8GBmOGMOXiTK7BdZE8tHPteeLq9A3A-Geq5rdECJXx1I1i4DVDrwERCIKKkWsgADyvYeKNyBo_81haL8cxkxvnylYj-M071bZSS9AjylqzUtbk-QIswIxDZZzUNj91nlXVdSDrswfGMhOuyWmlksUW1_bseAW4tywYKvBfOw4I30uEKBVqzwycInNSzS01BO5hiutPgKWv4SGO2pYbrSVeEoNPBNRQbB0aGoEXRbWv_11AgsQgj255iLMW9UgUbuSkKe2mI_r5K19VWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c85d949fba.mp4?token=DayV63JvBtYo7iVk59NReyoqS1R3eIxpI5fv8GAm-IB87_POCHLmw5UDQqbO_ECzOEyV_Q8GBmOGMOXiTK7BdZE8tHPteeLq9A3A-Geq5rdECJXx1I1i4DVDrwERCIKKkWsgADyvYeKNyBo_81haL8cxkxvnylYj-M071bZSS9AjylqzUtbk-QIswIxDZZzUNj91nlXVdSDrswfGMhOuyWmlksUW1_bseAW4tywYKvBfOw4I30uEKBVqzwycInNSzS01BO5hiutPgKWv4SGO2pYbrSVeEoNPBNRQbB0aGoEXRbWv_11AgsQgj255iLMW9UgUbuSkKe2mI_r5K19VWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
تیم‌ملی‌آلمان همینجا حذف شد، نه مقابل تیم ملی پاراگوئه؛ اصلا بعداین‌دیگه نتونستن درست بازی کنند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24685" target="_blank">📅 18:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24684">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLJgzDWZcG9AxvwON9lYhceyYnLF4GH8BZcYKnzbPYSbC5bVAr_MLEhNQqtRrpi4RcioAANtBgldc4svRg4U2bl97siRHtheVrIPzke7RvdbGvLhH6rCu7XYZt7-Lk8Pf08ZKG7iAILCiD5oq8GM3TEThaR4p5y3f3_5RuLWosk1jxNDX9NoDor5mtgmmY3U8DvxD8_il47lgLiYUiAWOX_tS8OHD2hCAQ7MmODCsIkwqRTwBQLtNrZcYW_C-ihTu81fm0c3rLw7VX7gLaK4v0-J5CpNf7hTIZf8vvqDXL1fC6aM9ALqs0RRSs8nBjiwwxGSIsRBC4P4HMbWQXpJvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
جادوگر تیم ملی غنا: در طالع و سرنوشت کریستیانو رونالدو نوشته‌شده‌که امسال قهرمان جام جهانی 2026 خواهد شد. سخت و دراماتیک است اماپرتعال بشکل باور نکردنی قهرمان خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24684" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24683">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CaCUPqxv32UYRku8h8qkKVQdWEAK8MtSQSZgjbsopbpTzAaponwwGxuokY5DqVCsnJQVLZpjT0jAZuANXM_nQvuBLPdjc7-IKXmp0NpnkvNi2LnmPGR0GEEWdHc8vzQD4EQvMk2wKbgGN7NuoZL8yoL3eF-pMlhW_JEbCnMJZ_X1kGBsVCH9eTc_BRTq-8WnpedUqejDJYhIUmIc5Mu5k6FVpRir2hOrsxT8-3ZHYfKNym5yEY4d8EelsQGlhyiAt9P4KD6YmAPR942htpcoW3bExbmJvk0y9iQirN9flb6Q1XaGHTqgF3W-Y-iwIG7h7T0cfinnefaydKflRMfCvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: باتوجه به علاقه اینترمیلان به نیکو پاز؛ فلورنتینو پرز میخواد او رو با الساندرو باستونی مدافع 27 ساله این باشگاه معاوضه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24683" target="_blank">📅 17:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24682">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ia9-hUcgG6dxHrn1d0vDFwb5wNtD5lrDSj7hrK_domfe6eBp0EEG7Ud6f-Vepoh8tfY2Pw8W9xynPUHQsU_GyJ-FLMcjnRlGFj5wxUKWemqWGMM6hJEZWLnIGBEj_ffgmWPkqHN-nUQ93_Qx6hTO90RzQ5qlAiziwmIzm2g95nSMgagv7AlYVlDbwlqxdp24T7u2Y-ag5joyl6WWERY6Y09hwgZncJlSjnnKoNyoJmBSe_CPMfE-_8rP3AFM-yQq32Z392SqITrOjON8FnoR_iG5B4a6S5na3_rH1ZFff9SCyaJicP2tP2oR3vYL5PHGA8j9IoUA_PvWboM7XfgGsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24682" target="_blank">📅 17:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24681">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b6727cd80.mp4?token=d9pDhpllx0MpCkMu_pJDq77tRN4O0HbKDlKcerzNgR2WRv0r7UeYvtWWYFsAWHVHc9sXcw-z2uPRVXccYGQ2CK8tlt5FD9Ck2JD_mqJ8etUuAku7MiEjR01YtXJ3e_6fbzKXHJXMs_VYgJ9ICTL_bx3a5pO4uur1ktr4rPwHJam1hEzIFYNHH26XF2ny6YQ8pRTOl0zK-zjS4S-Pxd_bC7VQOIpUgnMi5UfD6TmgaOyj-RO7BBvq79Qx8sUH9bMhfgQMrO3J-FRUy9mRImdny2Tw4_wbvcumcDKd9UTHs2afnn0OUBiGJ2j_QKkFEt897bM3uDzuM8TdPdOjrDIYfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b6727cd80.mp4?token=d9pDhpllx0MpCkMu_pJDq77tRN4O0HbKDlKcerzNgR2WRv0r7UeYvtWWYFsAWHVHc9sXcw-z2uPRVXccYGQ2CK8tlt5FD9Ck2JD_mqJ8etUuAku7MiEjR01YtXJ3e_6fbzKXHJXMs_VYgJ9ICTL_bx3a5pO4uur1ktr4rPwHJam1hEzIFYNHH26XF2ny6YQ8pRTOl0zK-zjS4S-Pxd_bC7VQOIpUgnMi5UfD6TmgaOyj-RO7BBvq79Qx8sUH9bMhfgQMrO3J-FRUy9mRImdny2Tw4_wbvcumcDKd9UTHs2afnn0OUBiGJ2j_QKkFEt897bM3uDzuM8TdPdOjrDIYfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇩🇪
#تکمیلی؛ بعد از حذف آلمان از جام جهانی؛ مانوئل نویر گلر 40 ساله ژرمن‌ها رسما اعلام کرد که از بازی های ملی خداحافظی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24681" target="_blank">📅 17:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24680">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESibDmisJKlZ2zyEycqGMW2K333jb-N7lpBKQhkLy5trmW6yFGSF32GgvOjVDYvVJeNwnhzs_Tg3ILjg3fmdlQDAawTZ51pzeSao1mg3oZLGK7_Eui5uZA4xmCmFSBqXp-pa2DYZY_y5SXH-X4Zs3SqxPbAbS_CeN9CkcFkwG4hRbadD2-XIPxeOhbqId05TcolPrWXD6Yi4QeJ9GC3toobkkmIQF6g3n01L3S9N_662qBqLPfhSZwLlxNAB2J_oOrblY9kxZJMcsPLWszT_TuhC30BZfhSSzOk3M3vU9ATgIoybrGzmjXylZyYj5fLgzv3MJV65xOhpxedoHRO-gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مسیر به‌ظاهرآسون تیم‌ملی آرژانتین و لیونل مسی برای رسیدن به فینال جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24680" target="_blank">📅 17:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24679">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XgNRiuXY4QiUGGBhOoE96Kw_7AgC3HpHjpi1SXmLQdnVz1SnrM04oxMn8MtPkMNL26RmBfRfNrWrVryYtCL3fmgcRATslzD3d6kxq4K7KaPJ0Zod00CrOG8rZzJ34VyZxvjT2MFZFa9ogGOV08zxUnz4UT3t501QtCS--5-grt9jeXJpqAda-bAioSqJKuILpdh-0A301UKginkQk3M5W6ni9QohaRVuJjpQtKmLq1XBJQOCHlSkqAmfzIwouU6PcpuwgH5c-Hv3Ykfxw73ZSd1EP1Eb69J7MHcEXxCehxfhpgJZT_W864rqTZ96D6jT5QCpzJaldQMWZUxde9NLvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تااینجای‌جام‌جهانی 2026؛ خطرناک‌ترین چیز نه پنالتی بوده، نه وار فقط و فقط یه عکس یادگاری!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24679" target="_blank">📅 16:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24678">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUW1VdeOzSApUZzYsu8hya8h6bpxqBA4E_Zf5-U0_mlN4kVDhZdWIOUt9N_L9MXXFkHu1MGjfXgv0vDYoiwaV98DGMEt6ivuKX72NQJ5__8DaNKtAYfWfh1d742bqeCPkndHKLg7lJX6m_lbBO_JTs2zoAU3zwSShcRFqPGHn7kvklmHXSen5tybr-EYOYgYWkoCTu86UQDy_K97hiDPZ9tT0Y3AjGM-1VRnoPrSMAuwmKmY74l5K6yMHkzfOtD614miUnNoFI2UcxO5ABfp1lUCgSlXL8dtVKX0Ww_-hGS1svr667Y2H3k-Xx4y753ugYdlWKGKxq5bkrscyOhCVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بااعلام‌ایجنت دوماگوی دروژدک مهاجم کروات تراکتور؛ قرارداد این‌مهاجم‌گلزن بااین باشگاه به پایان رسید و هم‌اکنون بازیکن‌آزاد بشمار می‌آید. دو باشگاه پرسپولیس و سپاهان به دنبال جذب او هستند.
‼️
اولش دراگان اسکوچیچ باهاش حرف زد... بعدش مدیریت باشگاه سپاهان با…</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24678" target="_blank">📅 16:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24677">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmayYgkO170ckdvm_x-3h8bxi9DgB30vAeRIVswYJftkvIJhQPQx9LQwIlNnB9wA7vww5TI80KHHMwoqhGWD8zwKgXw70BaN-g60z9c9sWJEjIggq-KmPUzY90U-h-IAgIaS6NS_9YgGhzhOggDj-bS1BQTAHEXiFRfrTBziTipv0eq1dWuo3_hjUyoB0utt9BQuJ8N93_FKT0YWz7k54RV4OZWWEEI1eNErHzrdGA3vYVLaTlzO4v__NxXKm6v-uXLmTyxr9W9GeOfJcKNmUHY5L9YulHlEtoTTtngPQkDx0bND-CGmnoD9e7F6cN_M7v9NGL_REUBVBtNfY1ai3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
شش بازی بین آمریکای جنوبی و اروپا در جام جهانی 2026: 5 برد یا صعود تیمهای آمریکای جنوبی. 1برد تیمهای اروپایی. فوتبال اروپا این دوره بد ریده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24677" target="_blank">📅 15:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24676">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUDTzOf3jhg5g3q8R3rxF-ssYHIx9VOswn3pIVdAIuxz2jxqBOi3LDIVulByD7ocmayMR_91oXhLwPp6XEzQiFEiuepZMnFkRu3cO164q7CP1PHxL9i6S3xWmGEjURVXXpWS6V5TOg_4Du85qkdP5-27OJjHl3MvdXs_i-ve11ZWeKg4m8-SVmNENFHBC93jHxmLzXSHys__Fj1jqnbOUbt1CpWURItMWKJRlCHn7kgJwlk58AUJkuZCV9lIi1E-Z6N8w9eph3bCouFedim-rJmEEI6OdF3v7oyY8XtiW8bWQX_L6zQXKyPXnKqhMWhxE4AAq5OM6jpc5LIhUVxwtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛باشگاه تراکتور به‌ سید حسین حسینی اعلام کرده مدیر برنامه هایش روتغییر بدهد با او قراردادی 3 ساله امضا خواهد کرد. پرشورها قصد دارند در صورتیکه علیرضا بیرانوند در این تیم نماند با گلر سابق استقلال قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/24676" target="_blank">📅 15:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24675">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOAJICmzls7FNEVerV3aLM9zr9lGkVjesN5P9QCMNGI3-SzYVgJRAZ7JrnIZuMPh7_XnnkOfMrIh3hnqOXBqkF-QNXo9qY6O-d1HGPg15Gs6aurW3J9iYXEmpaIuhmNy3E_fMW_wEoc3MabzFknc-csqlaESyNusgTjnP-WtR1rD4j_MlKkZ6WYaeQ-fB7PzArCZEhbHYGWkOrc3lEKbnF105wf49jTfejGD0NXkRCVE2974QbmuZm0qPX5GCOoY7jbvaqSfXp9umWLmOroexW_2bu8IC7swXM3u-iQfLfUD-Isq5ilCehEtUt7wWFdbzCqp22sTzZi0W37tYyqDHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی؛  حذف تلخ و زود هنگام لاله‌ های‌ نارنجی‌ برابر یاران اشرف حکیمی در مراکش در ضربات پنالتی؛ مراکش در دیداری سخت و نفس گیر راهی مرحله بعدی رقابت‌های جام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24675" target="_blank">📅 14:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24674">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMnCYVk0QNOCiwgVr-ejHk69zOc_50KcoVOAS4JCgOd8tFdylayvpI8jXSMlEY2ldWEXiEGV0-3PkCP6c6nks4deq_auVbj2VEjcJwOi290jyHxQswAfl5t622raRsGZ4ViqMFpTQ1fbgb9ObcjIYJ5z6ZApOJjQAxxn9dVpdMf2yreNltdTol59oF7_ejZOp5KDc_er0ZyPFZf1CiPW81UtGUY7_kHN0KMUl0W29aOKfInFNrtBmveuFzrStYLy6WsDKlxjReeyIi_HMIG5OVKfSHLeaHg7K2R-gPFfl6jUeSrJ68wAcswZPSY2oibDoJJ8EQUWUQGxV50TsPZaLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه تراکتور در روزهای گذشته علاوه بر تمدید قرار داد دانیال اسماعیلی‌ فر؛ قرارداد خلیل زاده به مدت یک‌ فصل و قرار داد محمد نادری رو به مدت دو فصل با پرشورها تمدید کرده‌است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24674" target="_blank">📅 14:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24673">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JebykU6BHWvjFlYjBQvMbT3GhsU3ucKCwHbVIuA-Z949Wl9hXebdiEPOSgyLEpsrwLHCZM-lyoPEkPAvxbUIeLPBPVEQWj2MF4GYIgeLezKXjGRT7ik1EHES-kNJ6XhPiZP-bGYer9XMcTBEy3Bb1J3ujzzecHJ82XgsobOzR0Sx-Wr-bDulndDavK-sXeF1haTBO0pkrfnuQnQylAF1B4lQIFbRe1fpTTS090U5tPFzE0u6ljZ4wRDsGwbpHw7K6cyqRYZqraxkclcTagMyFQzonPdy5gFk9nHbmVZIvMKYNbLQUMgSvXtHNj8JLMOR_i4R-5S-n-o7Afxc0JFOMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌استقلال باید مبلغ 150 هزار دلار نیز به حساب جوئل کوجو بابت فسخ قراردادش واریز کنه تا پرونده این بازیکن به فیفا کشیده نشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24673" target="_blank">📅 14:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24672">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82624c7740.mp4?token=qDZkyR2BNhJUqQ01YOnXYvypherRGqbSJoub_1pwUjeuuOBMiePkq1gncLQu95p1oArBTVkTN6hvCf2WW8gYyEZNxrm2ViLcuraxscdPvg1OiFw3POvwmFEVo_icnvNIn4yH1WK2kNE5ok2e8Vs7Bwg6l-3JKGJ8pNFCAzxF7z1FGP31m3uhRybbm0UIjhNQLwpoJ1Q6p9XsO6pXBcfbqM7hrocgjZrRhYIfzsg2TiINXUazsn6de551L-NPdFYC3JrzJhPPwCF3NyIw42GgGOmwkUndrBjoK5Cw0WYeAqz3eKNL84XSGaRiYb-L6ROqcCgisyXxSETBL_R1GbhoUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82624c7740.mp4?token=qDZkyR2BNhJUqQ01YOnXYvypherRGqbSJoub_1pwUjeuuOBMiePkq1gncLQu95p1oArBTVkTN6hvCf2WW8gYyEZNxrm2ViLcuraxscdPvg1OiFw3POvwmFEVo_icnvNIn4yH1WK2kNE5ok2e8Vs7Bwg6l-3JKGJ8pNFCAzxF7z1FGP31m3uhRybbm0UIjhNQLwpoJ1Q6p9XsO6pXBcfbqM7hrocgjZrRhYIfzsg2TiINXUazsn6de551L-NPdFYC3JrzJhPPwCF3NyIw42GgGOmwkUndrBjoK5Cw0WYeAqz3eKNL84XSGaRiYb-L6ROqcCgisyXxSETBL_R1GbhoUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
میثاقی ژاپنی که بعنوان بهترین تیم اسیا اونم نه مقابل هرتیمی مثل‌نیوزیلند و مصر، بلکه مقابل برزیل پرافتخار ترین تیم جام‌ جهانی حذف شد رو مسخره میکنه؛ جوری میگه منتظر 2050 باشین اینا میخوان قهرمان‌جهان‌بشن انگارخودمون‌خیلی‌وضعمون خوبه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24672" target="_blank">📅 13:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24671">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tOKVbgKv4hfjARfkp4YG3xWg4dfNoPRFC-oBxpXXtYnqOu1LoL_ComMrJLX3hUXReFFXfs5fjRGAFhmRFa8qDwT5sTyES0qIvS3Na4o5QbZMdd5AuCC04EtDfOF7rB5EqPXMdVAmZW5Aq7-1KaKqvlpaai-oQNJg15AMByDrytzgIAvL1G2bcwVqcKRcWj6_QEyBxhBeh_Mauhj4jkAFvBXOEvEmaq_Rupra1-xsCSAmJEx2DlN_ITrL0jx-102BBRjKWhhHATwCfwegkmHfh9wQojsg6PuXJv6rzj1bGQY4iL5XiaONhAjlRSvMQoyts10JhIsCT_F5q30BsPaE5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنهابازی‌مهم‌امروز؛ گذر شاگردان آنجلوتی از سد سامورایی‌ها با گل نجات‌بخش مارتینلی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24671" target="_blank">📅 13:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24670">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HR7o309-nG9pZTX1RCvRQ24cYDpXQ4ba9WQBuC8y5suegFw9wnZ6gEQ56cOqtuWcIYPLBPfnGkEVi4nrP-o6tDgwrEFIMEmEq5iWfF4-cD4lVaL_BqYV0-_MWp4cElWfB0UOZ_ZenmD2EQeb8zNwSKwInQoNCRoWtOzmn24dy-9gp3_pkgqn7Sbt3hOi2ax6560TKSb20E195S2CaghfUvneBcjPCM62y_1wFOuZizALPMF1QAYCkyMqyPaO_LrV1CdrZ7rsNuVzrW4rK5-7X0LvoHr0gSGlSiCbEtDWChzNlUZRLql7e06JbrJ65W49pU2cWzkA9uOgKqMmV9EDuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24670" target="_blank">📅 12:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24669">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68e8477068.mp4?token=jmY9wroeDl-pBsW6jmI7L-HfBje8aQR7xP4avu9QLwvAkkAbjeW7MhAh9yo0x1_jYkr4-6pnYysr_9yB9r9P1oweKPdXXrnOwWNSC-8WXCruFAsmZYtZJpIqPU7wN-x1DrNBifT4FRTp0xfBMmRmvkFNndKHiXVid2CdRWE-Afr1Ld_z_WgtbnFfwO7_Kvll3WJmAQBdAybaVw5mI9rj1jhk05zDg2c50nU29m4O3t94RcELyTAu77x5bwl3rTtSEZxmY211VnxmBdXGQdf_PaK3TcpnQsN-dEP1RdHZy1xkwJjXnKPfPZkNBOnZzCR_QtG0M62OA5ZOJ4Huu4Ww0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68e8477068.mp4?token=jmY9wroeDl-pBsW6jmI7L-HfBje8aQR7xP4avu9QLwvAkkAbjeW7MhAh9yo0x1_jYkr4-6pnYysr_9yB9r9P1oweKPdXXrnOwWNSC-8WXCruFAsmZYtZJpIqPU7wN-x1DrNBifT4FRTp0xfBMmRmvkFNndKHiXVid2CdRWE-Afr1Ld_z_WgtbnFfwO7_Kvll3WJmAQBdAybaVw5mI9rj1jhk05zDg2c50nU29m4O3t94RcELyTAu77x5bwl3rTtSEZxmY211VnxmBdXGQdf_PaK3TcpnQsN-dEP1RdHZy1xkwJjXnKPfPZkNBOnZzCR_QtG0M62OA5ZOJ4Huu4Ww0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
یان سومر دروازه‌بان37ساله سوئیسی‌ تیم اینتر میلان بعد از چند فصل حضور در این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24669" target="_blank">📅 12:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24668">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/786ffe7041.mp4?token=s4yR0s92Oc0pRt69GZzG9xQMJVWIC8yloEfhh8EYZfK8cjXCe-p9Togk1GcyQN6efy46oVyp7hxWVCn1sPBy6WLatPA8gWzbxcp_ItwA5p79OGolOIegHxu2QwWSUaElrG6uNRjoJsJ3f9Cn97eRhai04FxAVTySm8PVjtSkUFIZ8ywMmHTADIzNFEwAk-7oIQZiRGFfID4uwflKz4YwFPBNy2UtNqK2xfsR4Y6VIFmAI45cZTCHFSugxLOTU1-3CqN2c043NTRhsEjHpU5l-55iXorbg91tj9GgyjfyVfiDSlGblWKBd1xAQeJklmBrfr1yP71ts3ZJO2Gl7a4jWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/786ffe7041.mp4?token=s4yR0s92Oc0pRt69GZzG9xQMJVWIC8yloEfhh8EYZfK8cjXCe-p9Togk1GcyQN6efy46oVyp7hxWVCn1sPBy6WLatPA8gWzbxcp_ItwA5p79OGolOIegHxu2QwWSUaElrG6uNRjoJsJ3f9Cn97eRhai04FxAVTySm8PVjtSkUFIZ8ywMmHTADIzNFEwAk-7oIQZiRGFfID4uwflKz4YwFPBNy2UtNqK2xfsR4Y6VIFmAI45cZTCHFSugxLOTU1-3CqN2c043NTRhsEjHpU5l-55iXorbg91tj9GgyjfyVfiDSlGblWKBd1xAQeJklmBrfr1yP71ts3ZJO2Gl7a4jWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی درگفتگو با ESPN گفته شک ندارم که آرژانتین باتموم‌ ستاره‌هاش مقابل کیپ ورد غافل‌گیرمیشه و خیلی‌زود از جام 2026 کنار میره!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24668" target="_blank">📅 11:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24667">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d5676f715.mp4?token=WpIMRd7kNQVtUizmc4P_DPaJWeY8EvZf6VFDpxfTRB6uwZMI3cnazetiyTGo1x1I0PPVTPDIsat1lS6jaQx324ncC8635SkdIwliNDnLJraBN4gCegOZTA4vFnggJprpFcJWHvRB_VqK1qrTlDti4nOK78xggbyUud03q7v5HT5wO_EpqFOFcxW0pQ6Pg84mDuBlemCcmvk7_RQZbVeXeNJv9qDJ2JKn7z5vALQ7ZygAaA11xEKCiV2bQdEZ6xS_-9O_cC_jB5mzRiIpGpNotvHgVUm_TVyNWuJjtZapG_nNFPWA2n8t_OkesDPxPTQn76ZN5d-ClxdNYLJQR5Ypcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d5676f715.mp4?token=WpIMRd7kNQVtUizmc4P_DPaJWeY8EvZf6VFDpxfTRB6uwZMI3cnazetiyTGo1x1I0PPVTPDIsat1lS6jaQx324ncC8635SkdIwliNDnLJraBN4gCegOZTA4vFnggJprpFcJWHvRB_VqK1qrTlDti4nOK78xggbyUud03q7v5HT5wO_EpqFOFcxW0pQ6Pg84mDuBlemCcmvk7_RQZbVeXeNJv9qDJ2JKn7z5vALQ7ZygAaA11xEKCiV2bQdEZ6xS_-9O_cC_jB5mzRiIpGpNotvHgVUm_TVyNWuJjtZapG_nNFPWA2n8t_OkesDPxPTQn76ZN5d-ClxdNYLJQR5Ypcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداگذاری‌باورنکردنی جوادخیابانی مجری ویژه برنامه جام جهانی روی آرناتوویچ و خداداد عزیزی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24667" target="_blank">📅 11:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24666">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OnKEmK8BbFRfPwPh55MweU9mmpeEt8jkU4lb3iWiEnlK2mqavEieTyT_n5a8UfOP3IjdAdrZwytGIDFNxg2QF5Ul9M5kHpfL154OfJLQ1B2-l6YqUf5iv4JW4GhGXG33OLvZVqwvVx4jE90_UZVEEwOiwjya0yMchvmUdImNd4AQV4qHvwIBU4hVwb7JvLoMT60KGff85HNrjCXNRocwbEsU1FfoRipWzA_FehrzDTogbo9QgtWsrYKErF3otdmV85NEjNMNntxyOawFFLZOoMcjYSu9F2nLVS5JB1Vb6CpApa7KADGpums4GsFY7pnDeUCEh7-fh332VK0l_6JSyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه‌پرشیانا؛
به احتمال فراوان باشگاه استاندارد لیژ قرارداد دنیس اکرت مهاجم 28 ساله خود را فسخ خواهد کرد و این مهاجم ایرانی الاصل احتمالا به لیگ برتر ایران خواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24666" target="_blank">📅 11:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24665">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThwHG1y9Xp9waHzyn5nccPA0l-3Yrppt3zqvUhb93yrtreVpZnBvaB-GC4KJxqIKxM4MDzOmOv_1u73sJLT5r8rj0EywN3am4vJCLoZInUrlVkloiqLP8eRT63dfNizLCz6vq7scApPqwC2U93poDb5rmo5eXR4e86QWX50CwAv4qlYGmc2whhaUIX6xxI0oCkdmnjY_IqCRCFn7fmxon0-Ss51IgM64kLZYZLITk0xYegctBKFb1LoXO5xj4mz1va0ydIeupWLW9fEoaxy3FGiRUmrpoUgIGSS9Nk67RQctWJ8fcmySGMnWvB66D7w95hb5hkxbm0G1cynwGyBO3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک شانزدهم نهایی جام جهانی 2026؛ صعود ارزشمند و شیرین کانادا به یک‌هشتم نهایی رقابت‌ها باپیروزی دیر هنگام و سخت مقابل آفریقای جنوبی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24665" target="_blank">📅 11:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24663">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNGEWyd5hpQBo9LccwJdVa5imBL-57CsKT9ZYtV0sjDLYOYMxZln0bfJRrs96DitCmlFOP0YKsgbRWdG57WGEEIV1jbG7o0MZEQuV8rPsXUsqmkfSo9Vei-bv7J1EXjkSEUR39prvkn4EAzCA4Ve8AqvhZyQP-Z6ZjT4lLs8X9aDM0wGSWj-uuNHb931_i1BW3WbDmL71mCSd2jAQbRJ7gL5n2PHftBL4O1XSKrzYdwb44xVC5AEfjAlcTwlCzFVvbV0U0a51bpEiHRTVTiYB1Ff107fE0eNsBnW6uVscjoi7PYwhRcTiJARb8x7oGzERwM33dIlnwP_Bl3SBW1u9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ باشگاه پرسپولیس درتلاشه امروز برای دراگان اسکوچیچ بلیط‌تهیه‌کنه و این سرمربی کروات ظرف 48 ساعت‌آینده با دستیارانش وارد تهران شود.
‼️
بعد از رونمایی‌ از سنگ‌ اندازی این مدت بازیکن کهنه‌کارباندباز سرخپوشان‌پایتخت خواهیم گفت. این بازیکن از وقتی فهمید…</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24663" target="_blank">📅 10:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24661">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/572d6647db.mp4?token=d671_pjatUvlucmYdc0k5SR4Q3DqoZkuJYzKiE25KDdEMXnJRqhgmrkxpEgDMg0dsuBOAriQzI6tH4vJaBgaOLW0SXuGkQAaxYTJbnq03KULe7S8talSah7Myn5lnLr1iIElWDLhImE4oXdGil-x6pLhZkCjhchfQRg_21JE7BXmobUU46vSIGS_rsn5oSSnocJrviSlE41xSgEK9X7mqLSjcrDecWBBAVx1NRYSx5822NVv2v_WnTJoZ0EDfBcNNDXOv1q5pPtdvVGfIrtJ4j2eLP88GOrYzqL3pCZZ8iNSaYJpe3NRJ2sFPUIhqhTdIsT5eai-NOkkv3V2bzOThw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/572d6647db.mp4?token=d671_pjatUvlucmYdc0k5SR4Q3DqoZkuJYzKiE25KDdEMXnJRqhgmrkxpEgDMg0dsuBOAriQzI6tH4vJaBgaOLW0SXuGkQAaxYTJbnq03KULe7S8talSah7Myn5lnLr1iIElWDLhImE4oXdGil-x6pLhZkCjhchfQRg_21JE7BXmobUU46vSIGS_rsn5oSSnocJrviSlE41xSgEK9X7mqLSjcrDecWBBAVx1NRYSx5822NVv2v_WnTJoZ0EDfBcNNDXOv1q5pPtdvVGfIrtJ4j2eLP88GOrYzqL3pCZZ8iNSaYJpe3NRJ2sFPUIhqhTdIsT5eai-NOkkv3V2bzOThw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
صحبت‌ها و عذرخواهی هاجیمه موریاسو پس از حذف ژاپن مقابل برزیل بدون بهونه اوردن و گیر دادن به زمین و زمان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24661" target="_blank">📅 09:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24660">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wxg-WQOnyzJR9u_UsiBrO8Xi4eW5jMs-Xv9ZTmyo2w1X6pD9csqYRiNkxKO0YdMDZeGViv1DnEWOBqTwAmf8ZWGoMj86qZ0jdp4W30e9WEHK4Ot5h2wc4-kc7CJbBPbu-VR2W9dnaU4j9jVQfgv-bNWIWQ3_eOZg5IUWdSFrqeVgOAQlRkIUNFjKfCr6q5jP065eHjY_XZhtkUf4USwIz7-1PBYyL765TjpQ71g2sBeJHA6FzbIB6JSi8MmA1VA2NHFu5qy1_CPQ8YFijgolVlvcSKn5eRGo5nKA0dh0aKwg5b_Xpcb8gXx7tJc4Gnr7XzMvfGfLOss_HmHCRVU95A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
سه‌فینال‌آینده‌جام‌جهانی فوتبال در این ورزشگاه ها برگزار خواهد شد؛ کدام ورزشگاه باشکوه‌تره؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24660" target="_blank">📅 09:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24659">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی؛  حذف تلخ و زود هنگام لاله‌ های‌ نارنجی‌ برابر یاران اشرف حکیمی در مراکش در ضربات پنالتی؛ مراکش در دیداری سخت و نفس گیر راهی مرحله بعدی رقابت‌های جام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24659" target="_blank">📅 08:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24658">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmFIz1bRv6veKOwfu4ouK7-U8NNoElWTx3K1PK2ADUH_4Cw-shFVwZ7zRjyWKiC2I0JDKHcnkAflMwGqQ6wYkLv97S1mSLDQB6Yttws3CroLA7Ob_dnI9lYBZqaH1LuPwpJtAMFihgGmTDvyaQa6WECkqz47_M4Ppxsr4EKR4SvFK-J9o3nyKdqd2GvCbSdbrfuSHoe_gE1l5BK1dOdDca0zTikmHebPZv7GxE49NGU1ILNLezoe-sAYkEBiME7DSBAXXX8vTIri3BnEYCrzp-tcGPKY7esrVFpkVHyGwR78-tUKOle0K9S9Fy7S4vrWSxqORwdmxJVk3IT7ESolPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی؛  حذف تلخ و زود هنگام لاله‌ های‌ نارنجی‌ برابر یاران اشرف حکیمی در مراکش در ضربات پنالتی؛ مراکش در دیداری سخت و نفس گیر راهی مرحله بعدی رقابت‌های جام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24658" target="_blank">📅 08:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24657">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CvJHoOx7dfpP3VNoARj1dc5xub2UAnIAqxM7NwmCwYP2hvNMJ0J4dfjFcPc7eD6B33iVorhl-7EBq2VLmB76Nmn5bb2swyAxq0gX8Ij3uDbyEYSI7YHjG4WPPLvtkyNw5rqFWBnEp_0VDFkkjA3VfnH-5A05AGPBFYR8IQoBS0XnWNepKrNLt_lqIBsSE94zf3OKEmp2AxBkvWat2ZF0IMMzD8jW-EgYFi5vaFQuU39FbLddMtDjVI1-DRXpUvn9bOGAVQ1Gdv2vn8Fz-SyF2pdiV1tpTtOKrAuRw-TdDrWfXn1VIZE7aYxv6f4zC0TLx7rG7Tpww2R1fuhAvIa12g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی جام جهانی بعد از صعود برزیل و پاراگوئه به مرحله یک هشتم نهایی جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24657" target="_blank">📅 08:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24656">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56f71a194a.mp4?token=v7RqjOxzervAeWLnt9eUD-PS_cE_dmDTD3KdlRC2R4ma5Cduv5QKBtKeuEfR_L3DaExluuCPYswXCBjU3BrRB874nlBpwoePb0XMtj0XC_TVMxCwbXlZ-49WUTXAuUNgeScTGOjkPikP4UGKtGBP-Evb1HwvBU3U5xMOYHzT2M6c0Lo-kxEGExzuiemGZY4dxVbRElMMWJUeC1gGk1eCXerwyed1Y-X6L-fJeblDdsjLWGh45nvn2gCS0q_jMru-vgoHXBp0IWIxdnZy_AfofX49-9uUZNLnj_jvKQJIIM6bvG9YYTf7yZcdkHnORLEThZtQ46ddWq_QnWL_hY3V84RncjicGVrOElg3a7l8Z-zQOlkyFb8UXAB2F54ZSfZGBLEwdyEN0p7v_6QGA5xBiUz_GmiEm_v25A-bxzYxMvE0ltu7a6ZGzc6UmjEO6t-ss4oZV_Jfhu_CqyV87lo9O34IEpdJsejFLY_D0sbEXK3Z9uRAtR8tTYL8aYxh8nvqc9HMEVdo6N643U20kHhhv-cCO4paSRUl0HaCJaI1RSy1IAsPxA0KZ_RdUnxbryaYdbcZyi9d63zRV02aJP05pd5roPwEf9uyyu2zcc9s2ISfB2xrGgF8oI3TCWKA1FxEUNXxGMuC7ZRC3xxrrjEZQ6SFf-jXf1T69C5-FaOROdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56f71a194a.mp4?token=v7RqjOxzervAeWLnt9eUD-PS_cE_dmDTD3KdlRC2R4ma5Cduv5QKBtKeuEfR_L3DaExluuCPYswXCBjU3BrRB874nlBpwoePb0XMtj0XC_TVMxCwbXlZ-49WUTXAuUNgeScTGOjkPikP4UGKtGBP-Evb1HwvBU3U5xMOYHzT2M6c0Lo-kxEGExzuiemGZY4dxVbRElMMWJUeC1gGk1eCXerwyed1Y-X6L-fJeblDdsjLWGh45nvn2gCS0q_jMru-vgoHXBp0IWIxdnZy_AfofX49-9uUZNLnj_jvKQJIIM6bvG9YYTf7yZcdkHnORLEThZtQ46ddWq_QnWL_hY3V84RncjicGVrOElg3a7l8Z-zQOlkyFb8UXAB2F54ZSfZGBLEwdyEN0p7v_6QGA5xBiUz_GmiEm_v25A-bxzYxMvE0ltu7a6ZGzc6UmjEO6t-ss4oZV_Jfhu_CqyV87lo9O34IEpdJsejFLY_D0sbEXK3Z9uRAtR8tTYL8aYxh8nvqc9HMEVdo6N643U20kHhhv-cCO4paSRUl0HaCJaI1RSy1IAsPxA0KZ_RdUnxbryaYdbcZyi9d63zRV02aJP05pd5roPwEf9uyyu2zcc9s2ISfB2xrGgF8oI3TCWKA1FxEUNXxGMuC7ZRC3xxrrjEZQ6SFf-jXf1T69C5-FaOROdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24656" target="_blank">📅 03:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24655">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14530aa1d.mp4?token=MP5I2BxHkbPoxSPFhQICBO9jNIVsdqhWVD_VdKOJN1RGH7z0GNCcx_oklCJ87H0l5mQq5f52m3IWX7mFzjW3P0GeQf3wwKbtzxbjaqIoPSZ-Z5bNqBeTFmvsKneA7NKywWAU_WgckrGkLfSlBiEuhqD2cI1pXs0J2tRJ28uLgipqWvaxj3lbXikMwKAVz2hAbf6V0nzrLfCbt-vbgJH-si6Z8dJNlSIQ6e-Y6sKAuacsqwVlrbg2-BbLIWgWzgYW5ElvVVe6Z2nVzfP2RsBEgbaaSElrpS8sbWwQt00VK3MwTyWAoYyTKAXXLFh4C41K4rnnyrQ4RWTN9v9N44K3u4C-4JJy5Hl6wbppsnb7I_fgk0cyTCsJ8TT6ABeyrSxREO4R963APusdH9FC5asvWD75LQpGx23jiQBjwKHxlBFBQpAUkg8XseLeu8gca3gr_Y04Ki9mZ2vrvm8RFPpyDav3Hnq9n_vfHyEaXrgcY1xXr1CExNtzT3dIm9yp5KtTWXcKNo8S_DzEzt7VEt3VTACZ2NYGHftDiMiObBYtwm_w5ZxGhmPqttcCdzIpWz0Hqe_zrVwx-8S0itg0_g0OYxGT5gKtZw1LbaJFkBuBNWyCFkkUlOQcfq-Lf-dlGvo8Eyc_6tCSumEaPzMXcrU5gOOkkIWtZlUt3RVc23tu4-k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14530aa1d.mp4?token=MP5I2BxHkbPoxSPFhQICBO9jNIVsdqhWVD_VdKOJN1RGH7z0GNCcx_oklCJ87H0l5mQq5f52m3IWX7mFzjW3P0GeQf3wwKbtzxbjaqIoPSZ-Z5bNqBeTFmvsKneA7NKywWAU_WgckrGkLfSlBiEuhqD2cI1pXs0J2tRJ28uLgipqWvaxj3lbXikMwKAVz2hAbf6V0nzrLfCbt-vbgJH-si6Z8dJNlSIQ6e-Y6sKAuacsqwVlrbg2-BbLIWgWzgYW5ElvVVe6Z2nVzfP2RsBEgbaaSElrpS8sbWwQt00VK3MwTyWAoYyTKAXXLFh4C41K4rnnyrQ4RWTN9v9N44K3u4C-4JJy5Hl6wbppsnb7I_fgk0cyTCsJ8TT6ABeyrSxREO4R963APusdH9FC5asvWD75LQpGx23jiQBjwKHxlBFBQpAUkg8XseLeu8gca3gr_Y04Ki9mZ2vrvm8RFPpyDav3Hnq9n_vfHyEaXrgcY1xXr1CExNtzT3dIm9yp5KtTWXcKNo8S_DzEzt7VEt3VTACZ2NYGHftDiMiObBYtwm_w5ZxGhmPqttcCdzIpWz0Hqe_zrVwx-8S0itg0_g0OYxGT5gKtZw1LbaJFkBuBNWyCFkkUlOQcfq-Lf-dlGvo8Eyc_6tCSumEaPzMXcrU5gOOkkIWtZlUt3RVc23tu4-k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24655" target="_blank">📅 03:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24654">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OvGho1ToZZ7vnhfurPFyl_o5wFlzxN678Rf0EmmnsE5xX7r4w8DglSeUvfTQNxMU-utc-DtydoQmysUAWsSRTTXHXjj7IrtLsgu-qGpB0eQ1D2eJkR5N8gW5doWYgRaiRmHkHfpSux_eE9SN6SjrSYPtQYChnuWKzvCYzw9RX7fScT-KzdjkpXNNzoDF3dkgebHZ6D83QgZkFyJ9Uv1cdWEICughFKhur-fZwx0zUvN-oOQ0kCKpncLzAOZa4cRjY7U7qJtIy_7ab9AsYraZixJlCdQpDhEXaH_GOImRP7QI6VNJWtq-N8G8sgkP0j-j6M2E9Mj3G9YAT6y-v1CyAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24654" target="_blank">📅 03:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24653">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef2bb58ba6.mp4?token=AuBsas6vazvrI-C2EpuMqPYtkcyWXpBxPDq0sRUr0WY6g-QtNQKnzYvuNAVpyoCpuvesyX4_k1PAanCdblZ1Y60gpLmRf5wgzhQ6WUxoAaAVpU5D2dwVcns_BsyLWZ_V87aJ-UeIxoj_A6-Bz2brj8jUjkdgLFj1EE5JrNsBCyrLpTdgurNSiMZkpY9XoWEQKDNzLQwWu8c_C5RaUDahhNXzTYpUJG4tBhA-RZtnyF8fNP6ax_62bvkBXsE3sL9G9Ids3eUUw7NeiLtcC_SWx1GBXszWxV22iYVBCCPO8IsjZVHvAucRD1os0rKqzmaAyg-d8lK_2SKLnuffr0ASTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef2bb58ba6.mp4?token=AuBsas6vazvrI-C2EpuMqPYtkcyWXpBxPDq0sRUr0WY6g-QtNQKnzYvuNAVpyoCpuvesyX4_k1PAanCdblZ1Y60gpLmRf5wgzhQ6WUxoAaAVpU5D2dwVcns_BsyLWZ_V87aJ-UeIxoj_A6-Bz2brj8jUjkdgLFj1EE5JrNsBCyrLpTdgurNSiMZkpY9XoWEQKDNzLQwWu8c_C5RaUDahhNXzTYpUJG4tBhA-RZtnyF8fNP6ax_62bvkBXsE3sL9G9Ids3eUUw7NeiLtcC_SWx1GBXszWxV22iYVBCCPO8IsjZVHvAucRD1os0rKqzmaAyg-d8lK_2SKLnuffr0ASTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هالک‌ایرانی‌درگفتگوباابوطالب‌حسینی:
شمشیر خوردم و مانع کشته شدن یه بنده خدایی شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24653" target="_blank">📅 03:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24652">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgYxHG3Xg42s5Jj5ogqaBvbWXWs-UJ3-DBu_wbdo-nF1GKzYo8LeevtbMvW94ZZ_aIJ2VjRbEkKCVS2vOPLUoC1tuUwhaVvCOt4rjsaImydB-9w5GSPih-zHAlHKlHEfQmY1dlSCK8GLV_4EyBlWp_2DBfFzmFs5eqksv538rZImK1m6l8r0C6fU0jlU2ywgRg7-ZoXrrVKBbSCqDGQvFtgKOt-olCeSHMocz0IuHkgDbKYl4yzd8pcyopfs9bxjE2icQ6b1uIvvRIHpiLumHEjbJLT9U_0j_L0KHykryaKpWDywQaSk1jCU6i_ts_jsJsN3IlaLy7Kke0q4gcicEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24652" target="_blank">📅 03:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24651">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4Q_YJbalv0FznLMtFYtJukFJEAqLaQXepwE5C78Ielpok6sOO_NhwrpJTH3cbVfnRFcgfaJnLiKN2jzJyXtqyrDe2Cx43zMXxO0T2uvyg09etVRKOpmrSIh0JGbd-SqpmG12dyYs5aNrvG6C3Yn2Wm3t_6ZPxEHlq8jyUWIoZvzS_tq_nXVlogp9j5QvSR-cF0pnj-tIAH1PXF3EdcvZxO075PNxQrZQdgNLIDkxNYOpFKyc1XWvNeicWOprXK0kjzm6IGmNirduz0vwQucHcaHkx-IzTpfrhivj1X5IG5QZDqK-wGod_myFPEdzThM49TgMHj9qcikLnaePoLxmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آلمان‌امشب‌از پاراگوئه‌گل‌خورد؛ آخرین کلین‌شیت نویر و آلمان توجام‌جهانی‌برمیگرده به فینال 2014:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24651" target="_blank">📅 02:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24650">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8d0fcfa32.mp4?token=K-mHP78QTLGF7xHrSlaXUMw71zGVDSyYV8f9NZSU1Vby-8lTQunYdqGDeFyoidKHBLyRX2hWXUZJ9hM87BGa5PZAMr6OS74FqedvrFK8W2C5vSU7w3EbsybScUA1WF8Ntjp4xc0jsrbNz4Yn7QSkv_BGVtP9u6ZkGWMNlwPSjqYayvnK6QzhCdttBqlSVBZ0HxKpoOXg46l8iQ9tHQnE3kM8-OE5z4x3y2p6bIVRhozDuOMHJmapIyXC1Y4BmRKRUMF20zg4fv60ooPDxD5sNh97yKXKx09g6TR5sBCX7lB2FnqJXcygjusqa98rCgZmXcNBxiB38ueB0Yf47x_tXjOlcICGXBYUCSO_ir6b2pKEDyaM9VbrR36EXa00KobuRs0-jam5ZrzUOTJWV-o2FnBl9yxFuYb9-Vc974BGpM-QYaAbf6eo6I_9z-aAVNj54e__DS1JfUGCQ4MK_N0sth6WtNPQ1stSLrpPk8hXWxhRw5yYFcFYC5E1VhJZcapfGlOadR57O5lr6X8yVBMXjWKfXwuCVHL-337s6U9z-tKL_xDb4P3AZmdtcoiG4HYutJbKliyk_1ovHp_nkIxl0l702AEmvcWVLSlQ8w3Tq33orUXROKZZ8Zmi3HgPQ3L8d3YQAYgi7t0KFGGGu4XHqPw2BfyiUlrtIPKj13yDGlk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8d0fcfa32.mp4?token=K-mHP78QTLGF7xHrSlaXUMw71zGVDSyYV8f9NZSU1Vby-8lTQunYdqGDeFyoidKHBLyRX2hWXUZJ9hM87BGa5PZAMr6OS74FqedvrFK8W2C5vSU7w3EbsybScUA1WF8Ntjp4xc0jsrbNz4Yn7QSkv_BGVtP9u6ZkGWMNlwPSjqYayvnK6QzhCdttBqlSVBZ0HxKpoOXg46l8iQ9tHQnE3kM8-OE5z4x3y2p6bIVRhozDuOMHJmapIyXC1Y4BmRKRUMF20zg4fv60ooPDxD5sNh97yKXKx09g6TR5sBCX7lB2FnqJXcygjusqa98rCgZmXcNBxiB38ueB0Yf47x_tXjOlcICGXBYUCSO_ir6b2pKEDyaM9VbrR36EXa00KobuRs0-jam5ZrzUOTJWV-o2FnBl9yxFuYb9-Vc974BGpM-QYaAbf6eo6I_9z-aAVNj54e__DS1JfUGCQ4MK_N0sth6WtNPQ1stSLrpPk8hXWxhRw5yYFcFYC5E1VhJZcapfGlOadR57O5lr6X8yVBMXjWKfXwuCVHL-337s6U9z-tKL_xDb4P3AZmdtcoiG4HYutJbKliyk_1ovHp_nkIxl0l702AEmvcWVLSlQ8w3Tq33orUXROKZZ8Zmi3HgPQ3L8d3YQAYgi7t0KFGGGu4XHqPw2BfyiUlrtIPKj13yDGlk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
👤
صحبت های عادل فردوسی پور در تعریف و تمجیداز رامین‌رضاییان‌ ستاره36ساله فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24650" target="_blank">📅 02:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24648">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3a278b0.mp4?token=Fg-zuU4H3aI_GwSvNKiJENv_3N8fTN5Ka31HDPocU9o3kwK-XOX4pOspPCY5W7UIL7DlTLCnnCkN3ZepiVUEZi5eCTs9Ne9aysOnnNQtUUvmycn8gUe7iXP59Hf9I2eNNg_D43bzlN60uM1G0bu5FX5cmrVOrSPDnh2fZaBqxkSYcu_JI-_RW-rQGWYltEF7akljumYEEKhXxUXM-MiQxNBVdp7W8eVmOzqb2hDrpCYzHV5Uw-2GZRVSSXYobO2MyStR8ttaugVGJj93C1Oc7bt4luBPrNJVLt7ULs1VA9kVX3bscGskeTpEwz3F_0Ko3dbGGb6OKesi3V5h8uipxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3a278b0.mp4?token=Fg-zuU4H3aI_GwSvNKiJENv_3N8fTN5Ka31HDPocU9o3kwK-XOX4pOspPCY5W7UIL7DlTLCnnCkN3ZepiVUEZi5eCTs9Ne9aysOnnNQtUUvmycn8gUe7iXP59Hf9I2eNNg_D43bzlN60uM1G0bu5FX5cmrVOrSPDnh2fZaBqxkSYcu_JI-_RW-rQGWYltEF7akljumYEEKhXxUXM-MiQxNBVdp7W8eVmOzqb2hDrpCYzHV5Uw-2GZRVSSXYobO2MyStR8ttaugVGJj93C1Oc7bt4luBPrNJVLt7ULs1VA9kVX3bscGskeTpEwz3F_0Ko3dbGGb6OKesi3V5h8uipxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
اینطوری که پیش میره مکزیک سال بعد یه افزایش جمعیت چشم گیر رو خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24648" target="_blank">📅 02:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24647">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVh5Idq8PmCPIP27NA7XoWVp5l2iOyqq4NTeG1Jjra9ym1h-aXHtbDuPhkSlKOChbBO2lGLcL3EB1A-ZPeyo8uqaeoT0ypP6GcACCIyCZg7CuYP-w-_zXopcopwMZEbnLWzgC-DEWNbF4CJQXTz9GdKDErSqv3NVcCcUVbrHWdAl6kNxGEcb86Xw6fcOGfcLn8DI3fXFnQMFMYwD22c25wFNtMqctACdlA-Pg0CJLMQkaGLHAI3nihrw5pN-6h-HGjCPXCT36zUTPzqeot4rJWOoMP4RYIpmHO_EjlUoqSiGrJptl80i128yuBwAu4CRQ0rk8-UKPmZMvzZzgJYfBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جواد آقایی‌پور مهاجم‌سپاهان:مردم عزیز اگه تو رشت هستید و نیاز به کمک ضروری دارید به من پیام بدید، کاری از دستم بر بیاد براتون انجام میدم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24647" target="_blank">📅 02:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24646">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‼️
بازیکنان چادرملو به لیدری رضا میرزایی وینگر این‌تیم سرود قهرمانی این تیم تو آسیا رو خوندند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24646" target="_blank">📅 02:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24644">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECNPk0lgjfRkjmUHAZM4bVBOmTMRv5KseZGHL6Hkh8uD8uaDu-TH5ZBgE3IgFdqunWvT6nWQxQAuhiMugZ8VK1nIy7yMJOgmrRgg9MMkSh1FO65LIuPgk5Ih6TW3_4YrCIbeh0CAdn700Y56rdGhRciTbXPk-QmzLL2mUhCF64v_EMpmdAwqBQdh-qokQk2ccbnh2qPweAgVxuSvL-_WSaWJogWfhlnar1NvfhmkW1OhPZhBsCG8_-OV6d70ihoSuuHp8WQuW9eboKt_zpf77XnTHabhRZQc30PX3eR_fizg76BxKXl8lRKPAK48e6KHtpPzcpWtokiB48mvobmEPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#فکت؛ علیرضا بیرانوند تو جام جهانی 2026 :1 کلین شیت نویر تو جام جهانی 2026 :‌ 0 کلین شیت
‼️
تعداد کلین‌شیت درسه‌جام‌جهانی اخیر: بیرانوند دو کلین شیت داشته. مانویل نویر - 0 کلین شیت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24644" target="_blank">📅 01:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24643">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2fs3nwlgtk9Z0CKQffOS0WtrWvViLzpXkcUm2oWJY9B1k5Yz4Wul9yDh3VcLvl35sOJNnH8I1Xrqpa19qitv83qj83vBmGFJ1Kq_jnzrhytggZcn8D5_J-J9FOkgbSeLdmQ6spyIL2Ix09lJGuCIDsiq_lT4JSU7Y2Ax2FK1SqprvjROcleGcozq4TJduRjDfsSFxxpIW5W4B7KpReK_fqpCMBpgZuhxzpI8aTf-y1-9jck1nH7YYTBoPzrgwnEd1idHdr1HPUgxb8JCe6iQzGP1VPId2IHY8YTcGenzGNm_k7RT7H_yzNxojSTuO9IajpV-qI9LJ6WFpl0Mg2ddQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24643" target="_blank">📅 00:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24642">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cADdVtMCRrSyGk9SuPZ4x56rmm3SmRzmQa5lIWgyoY0zxjUj8h2v8tFZ1r2UYdicZ__BQLURlMgaAylslzw7CQa7SdMNsXyue4tilabf5jsL4lolQ257LqC5LYu1IeQPSxbmICmt-li8dZTt3v9vmdjM3g6CwIZm_B9TqnKSDeeLuYdyGHbE4UwuL3JJXp_diu1yM5ZzC-rBgckKDmHP6W_TQqMwHbbaXwTvkAPF5Evc-AbgCUkRT3fgWm5C_frhng0ogSXfh1q4_eFFjoGlRYVKHrmJzPiyu7y-6Kaqwmmih_st_V_jbMmQmPdMbw8uxcDCz5UOqgMqSV3w9KokcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
🤩
جادوگرغنایی: تیم ملی آرژانتین با تمام ستاره هایش مقابل کیپ‌ورد غافل گیر خواهد شد و باشکست در این مسابقه از جام جهانی کنار میرود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24642" target="_blank">📅 00:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24641">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lH4OLKOz0B9N3LkivYHiRUaclFCb6CZtzJ9aqvRAz4xmHnXFAKOIGD5-SF1R9jb1NWVZVTALD03n54UfsqNa5a_fR1LeIbjZKpR0RNd4tjQovtbVRQWCEqYrWlcJ4ZPKhXZolTl0Qichi7In5sPs7n8rlBMcaQGkB60aml35q4jd5Wvr2BjhZe1P9O3gezhiWDbjEZiRC_TnVOoyR1vPOQPNzwZOuJtggXjGB8boDTnuIHVOD0RZ68ZM4lSKTQmC5IxJueTfpy7MgiIKbRou2AxLJN7KrfhAV1kG5jYwfNfeFIRPy8Y9MlC8Yv-nODLIthyiheVfs32OjSmHxrvhxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق پیگیری‌های رسانه پرشیانا؛ بخش رسانه‌ای باشگاه پرسپولیس پوستر خداحافظی از اوسمار ویرا روآماده کرده و بعد از تسویه با او منتشر خواهد شد.
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24641" target="_blank">📅 23:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24640">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d09c7fb1ae.mp4?token=W39zSqUkd0VuN2JecLTQtpr76FnhzHUhdTq3q6MWjWqf0gg7xLDxFUVlxz4Uo_Lpxvt1S8jynZxKbIt_9NghKyZlp9H-tNyaPtBdBKv5j7qb-fzRwXU70IEvlYCuCXdQ6g80_Wp8rHQSMxHyKW6nKO59Ozl7Tty1_aqaoRx5rr5I8cwJi-kQxPF9JITRCX8EJF6gFeGjhdR8BtYygtqIWqP-QsYLFukLyrGvQdHsqb1ApkUJK0zNVxEJHNgkKLTy4ezdYh39DQROWSsOsX5NGRlt0N9ScHEDy-qH9BmFnaKSDwTJGpC4h7CkwDsSR6vj3sMsNYMGJMpJMbZJYTKOLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d09c7fb1ae.mp4?token=W39zSqUkd0VuN2JecLTQtpr76FnhzHUhdTq3q6MWjWqf0gg7xLDxFUVlxz4Uo_Lpxvt1S8jynZxKbIt_9NghKyZlp9H-tNyaPtBdBKv5j7qb-fzRwXU70IEvlYCuCXdQ6g80_Wp8rHQSMxHyKW6nKO59Ozl7Tty1_aqaoRx5rr5I8cwJi-kQxPF9JITRCX8EJF6gFeGjhdR8BtYygtqIWqP-QsYLFukLyrGvQdHsqb1ApkUJK0zNVxEJHNgkKLTy4ezdYh39DQROWSsOsX5NGRlt0N9ScHEDy-qH9BmFnaKSDwTJGpC4h7CkwDsSR6vj3sMsNYMGJMpJMbZJYTKOLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
سرمربی ژاپن بعد از کامبک خوردن مقابل برزیل: بنطرم خدا با من هم سر ناسازگاری داره. این عدالت نیست. ایناهمش‌آزمایش الهیه. خدا داره منو میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24640" target="_blank">📅 23:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24639">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4Y6o562OTvePF32dtAVbHO93eZmW3zFaA83cvITcF1dzGBskzF5Hjkr-iqMjvyoTXZnQJ0RVac2PQi57DZlC48Apo7EPb9WKnpJZKXs_5pX0LHX1E_Pw5MvufvYok0B8jIAvhliKHdRDU_0DCpZnVZ1t7UmHZMRmrqgETK-Dds4UtYowOFRjBZq5AX4iIoljjebiD2aLMRsuoYUBFWw4xOrDIcL6zbl4Z44x3WUGX_Q9Eu8VLTovZcPYq26kc7CEji8z9o11ludrNJXM8ltF6dJIUiu3y8vkseBTVT2za43jDZFu5aae1hk3UC_1FERFvfJutReRjXI5Uwe2B8ReQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
سرمربی ژاپن بعد از کامبک خوردن مقابل برزیل: بنطرم خدا با من هم سر ناسازگاری داره. این عدالت نیست. ایناهمش‌آزمایش الهیه. خدا داره منو میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24639" target="_blank">📅 23:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24638">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoddwneLjaHPZgT1YyY3X7ey4JHVkHuPuM5Nn-nHkCR_hKthZJx8-7gZI2Y6RUeIdb2yuRtKmRu02sgct4joB_5pnMyJ78V0A0ROSz6-Ag3MRJExEMFEADPDdGSmxvBpQZ88CSyLhjuJ8a7MhuCAJyyyioVprSitjRh11UQk12oN0oIb0oC349mjJFfcyYKUbU0VkYaBio9K0LA_CY39HM5idjAkJ8sSvl8Gngy82Sl7XQQO54ZgjaP7BQGw0nNXwrfklq5oXcT2poFTrbt-SgfTSdepVetXNiSbAxTjxzZBjmT9qttB0COYct2qXVKgeadebVrhx4t9gQ6spB6p6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛صعود دراماتیک و نفس‌گیر شاگردان کارلتو با برتری مقابل تیم شایسته ژاپن؛ سلسائو بالاخره سامورائی‌ها رو شکست داد و منتظر نتیجه دیدار ساحل عاج و نروژ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24638" target="_blank">📅 23:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24636">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/toaLPLDjknRFRWpk1gXPUyeKkDbORE--CdIuypc4uTbmd7apT0Quv13mUqjcoexDj0uHIVnQnkvcxGRvq7M23dcV9XixYfrtvO21R3qNzI4vzZtKTxxMRh4LLxrbLWzoIDmUotRRL44P0wtMqvRLF8187pk5Am8aWsvLbZuu3CCzyMU2NewSaalOCtnPgLLQ8xlZR7lpQKoKk7vu1LAQNU-WiAi8g8DqbCGH2mrZSN-DDLtCz8PQe4a-Z40luWAxxsyQUOpS9vKNP7e6eJ88KGcVBIt8eJDVb9gRQp-xOjtJBTm0N51WE83rw-mSiECZaY0o84SrGXD0CkfYhmNdUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ فردا؛
از مصاف مانشافت برابر پاراگوئه تا نبرد تماشایی هلند vs مراکش و جدال حساس یاران هالند مقابل ساحل عاج
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24636" target="_blank">📅 23:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24635">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1qSO9DKDAF9NjnPP-8JXBLrJ4CioMgnBpu115SUTy7BYuYb0nzOde0JvvOUEoRLoSsVJyfLjnsxbKUGhTxy0rQ1tvCeR4GVL_lI9gkBkmmskI_r4fYhEI0_nGh7TQ0BtZawWfoIgWTl949VS1wZKrrGaWtGDOK6yWL-GSLjgTWLosK4i-D9xFIKL_hBvd25jy1ihekoy58QeylBsZ-pNdFuKRkVcMKdBkn3022EjIBL2smHcfb23_bkISfwqQhQZ5KJcs_x53OgQ9ym-ojVrdEP-_UGY8Vt3ron7sQjpLQB8aqwLEYUeSxgwBoLwCmzDo5e1nMOv4x4ibODnnVTaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنهابازی‌مهم‌امروز؛
گذر شاگردان آنجلوتی از سد سامورایی‌ها با گل نجات‌بخش مارتینلی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24635" target="_blank">📅 23:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24633">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZvdydemQwqEq0gI_E0QjOpicRhYHG-9kplP0zOUwK5eEX_YnRTQdS7NEgM4u4cydUmD3t2Ew6Y_KhSo1bmP1F20Nq_jrfw81hWy860g3BGQUPBhl3qcVu_X7lsT6ycVqB5wCEkICYrNAjtjTeB_YzttftRaROXpB0z3lrY3PKvz6u0TAMdgAc_efw2stlsnC96jduOELRwAphE__64nFw2-dzRY80EZYbjbfo5rfkYEQMccXpxJehHeXJr2XD_uNgdIVCP-NLEcQDplE_pBBKJYNY-JQVduieHtLMBxf_p3jqwSULKiFRocL99iJgf3pwe0Enee_RKn2UvSKbHJ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24633" target="_blank">📅 22:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24632">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9jBAZiXXOpEznxMsotMJ3AQjKtkGR_C7RYz7e4VJ0Xk1HnUOUZ0e86imYRjSJPUYUGksa42f4jtrNEs5I88W8qrf_v-Wi8V6u0a8bZV3DEEVX0QLsmWUBqrg3E065_Fo9_eZAkIWmog_ebOjDuLrK73Eqkh08FVN88o7lA-0yePv6aLqNz5yiaWw-io8l116EbTnHdQn7vTkUH4pTUD8Bgipd__0bufRQwhY41RFiEj2xOzBID5VpG-Drc-Cz838LqL8PqO6WvEdLiOprIbLmpTo4OfL0bFXV7BSKq8R_BSQ5AyKRd4s99wuXe4-f4E_UXvX43EbURVWJ9jIysQVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاسمیرو ستاره سابق رئال مادرید به این شکل گل مساوی رو وارد دروازه سامورایی‌ها کرد. سانتر دیدنی گابریل رو ببینید. قشنگ گذاشت رو سر کاسمیرو‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24632" target="_blank">📅 22:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24631">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56a71ed73a.mp4?token=ID9heJJJZhPg7Ap_yrnHu5FkmTD7bz8ML98iFmMoe4xaj2VcvrLa7SGJ8sj_KK5kOqV91qDsVbescGUAXiGxA6bVRaQf5-cA_5L67xBhmd7K4Pr21DZ_WYtjwxaUF3ECgBEC2QMzhGLRyeWoOY-5rbNSkAbBzHNA6HM8cHid1H0b9QsQpJvqQ6cvtIiycNDyQM8eoupcSJgAyrrGOJp4h4C_AAKfdzBb-bEOX-YjbDkLoBBAkE1rxWOCuVDAcd8Kd-2DiE42ti9V3lyyVDR4SAVrS4zHpALIMvKeIi7RQyM5BoBWtVEY96ExAlnx6ikpYp2DI9UDif_GODnaDW3rAFWbOL7HOsJEWpv8IdSOi_sDEOOHAX_S6FHVd0yeG-8u6NDS0LX5RVnibooGKSZ2n-LxIFDY0PdtezdO4liBfAXLWXe45dGUf35-vlu3z0rifArnQ-iDalXJCgf6wedg2kVyWv4ihqgB8WF9Ra2bmNS69wE-MMxWwBuoWUDdUapqUTm4REOV7Omz9akGnehdpysBhP-E0EEgKnx9vjMgMvQuw4gYmdWQiG5ctTXCyfzcg9HflrICA221YqFBFczeP5CKeBj-KNd6n8FqRr8Cc7CY4fzvu3DX0YmdbqPXIeLQyBgBlnwNzHuvoZ8IFmEmPhGw6XNhD0Q4syjqX_8z42E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56a71ed73a.mp4?token=ID9heJJJZhPg7Ap_yrnHu5FkmTD7bz8ML98iFmMoe4xaj2VcvrLa7SGJ8sj_KK5kOqV91qDsVbescGUAXiGxA6bVRaQf5-cA_5L67xBhmd7K4Pr21DZ_WYtjwxaUF3ECgBEC2QMzhGLRyeWoOY-5rbNSkAbBzHNA6HM8cHid1H0b9QsQpJvqQ6cvtIiycNDyQM8eoupcSJgAyrrGOJp4h4C_AAKfdzBb-bEOX-YjbDkLoBBAkE1rxWOCuVDAcd8Kd-2DiE42ti9V3lyyVDR4SAVrS4zHpALIMvKeIi7RQyM5BoBWtVEY96ExAlnx6ikpYp2DI9UDif_GODnaDW3rAFWbOL7HOsJEWpv8IdSOi_sDEOOHAX_S6FHVd0yeG-8u6NDS0LX5RVnibooGKSZ2n-LxIFDY0PdtezdO4liBfAXLWXe45dGUf35-vlu3z0rifArnQ-iDalXJCgf6wedg2kVyWv4ihqgB8WF9Ra2bmNS69wE-MMxWwBuoWUDdUapqUTm4REOV7Omz9akGnehdpysBhP-E0EEgKnx9vjMgMvQuw4gYmdWQiG5ctTXCyfzcg9HflrICA221YqFBFczeP5CKeBj-KNd6n8FqRr8Cc7CY4fzvu3DX0YmdbqPXIeLQyBgBlnwNzHuvoZ8IFmEmPhGw6XNhD0Q4syjqX_8z42E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
جالبه بدونید که؛ گل حساس کایشو سانو مقابل برزیل اولین گل دوران حرفه‌ای او برای ژاپن بود. تو ایران هم‌بازیکن‌داریم تو بازی دوستانه هتریک میکنه تویه بازی خیلی مهم مثل مصر پنالتی خراب میکنه. فوتبال ژاپن 100 سال از کل آسیا جلو تره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24631" target="_blank">📅 22:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24630">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔵
تیم چادرملو بعدتساوی بدون‌گل دروقت‌های عادی و اضافه توانست بعداز زدن ۲۲ پنالتی در مجموع ۷ بر ۶ گل‌گهر را شکست دهد و به سطح دوم آسیا برسد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24630" target="_blank">📅 22:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24629">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/riVBY1UTRYzRcF_r_MQ64lLnwoBmNBlaU-hYlgB7RXqiPjGTNCRdNYqZTFCSE4_NWGiAES0VPGOG6qK5H_aQSUeVTCWWY4_kzM_K-czVqTmoSG7zWmiBthrMPQtVIi89odNFm0Aebr7RoN4rfrHuGDCBn-sz2f-jpRTb1cqeUOZlrfP_HQL1Rb9LlVhL8cUTMlz5k4xykJ3b8e_aDkPVX-TQ9twgrxkR7-J5LKGj1wqtFR3IcABO-mMT7UPkpCkULbgOMAK7Qu9UgpdbZVEhweSNJGfcFtvSVD-rWsbbWwBgh2FjxOmjIUO4fdeCqRVviXy7BW7MF2zoRUjXNS_tGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
باشگاه گل‌گهر سیرجان: مدیران باشگاه پرسپولیس مدعی‌شده‌بودند که این تیم یک ماه کامل برای تورنمنت آسیایی‌تمرین کرده و این تورنمنت باید حتما برگزارشود امادیدید که تیم چادرملو در تنها دو جلسه تمرین این‌تیم رو تهران باتمام ستاره هاش برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24629" target="_blank">📅 22:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24628">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b41af009b6.mp4?token=agOVe1bZCi04TNK4tyHd-jTpjrL6chrg05qX28C9WaT_x7eaL9wOUhuKQPUoMiy6ATbel3RZ62mYdoV7HvhrOO4_iAFUp5eOSCi9Klrf4l7cuhwE3u30fq-sVgIKPjovEvvh7pZ7nt7ZcLOGYC73PDHWW46U_oc8rfpkKADTC4fsexvoBlm_O-Fvc_27KHr4X4WgDk0Okf4tLWWkTc02wbWYgG1IHJ77d_pTML7EDncXVVe7hA8SFS5NPJHe5b8DEks-b8Uh5uPWTjy9f3JMDZu8ABqqKvufhohNyXw-o3U4vTMx5NHXei35sTMCa6c-1lwwUBw9XGn-QU08R5M2Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b41af009b6.mp4?token=agOVe1bZCi04TNK4tyHd-jTpjrL6chrg05qX28C9WaT_x7eaL9wOUhuKQPUoMiy6ATbel3RZ62mYdoV7HvhrOO4_iAFUp5eOSCi9Klrf4l7cuhwE3u30fq-sVgIKPjovEvvh7pZ7nt7ZcLOGYC73PDHWW46U_oc8rfpkKADTC4fsexvoBlm_O-Fvc_27KHr4X4WgDk0Okf4tLWWkTc02wbWYgG1IHJ77d_pTML7EDncXVVe7hA8SFS5NPJHe5b8DEks-b8Uh5uPWTjy9f3JMDZu8ABqqKvufhohNyXw-o3U4vTMx5NHXei35sTMCa6c-1lwwUBw9XGn-QU08R5M2Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت های ابوطالب حسینی درباره خوشحالی بعد از گل شجاع خلیل زاده در بازی برابر مصر‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24628" target="_blank">📅 22:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24626">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/863d336b56.mp4?token=iKcsup1UB3RgF3tEVXWkCHszOH6AwecgAvxG_vLzeMjjBKnzxcp4UQkK85gjM5I-0AqaJlVqYF5KdVQ2LK-uJfr9XPkm165jEDnA5-wYCMs_gcVzWTyrWjK7hQP3xFJXTwcGxbgpJMLgkbebI9zZ4nCQBdGOZ7jN1ELLlzUfOSymhPrOcAzRQmsvm-njAetu0pkGvR-6ZxCnZqati8DVl7wztAxjJIQvo2WkmTs-3bnyDgX7vK5y5jncZRaukdQqxJbglPaL566Lk1DXiOwGrMhXDn3Vlb8_4VRKD6wkNC-_lde5AybD-mqoplsJorvnrtohDtF7sa6dXaYrV0XPplaJS_TVTTANW99nZBWKPTeTBsRt4KHgWoiV1OKPubWD2m35wuI8LRWjS5bosLmwEuxKZ2CSqESWoq9CUGTaGidzHKvFgUQ43mRxMHQlD8JhVKtwH5-u_m10Jc1nkkHpoACazOVKqbGjW0NR6SLRmTAFgSpG9jASmjP6-boX4W6Q8cneP0Qve0Ixih7UHmjx3_yc6H1Cq6jmqCKYEy_d_P0T77QnU1CqmnZosYk5JzcbDcSxBuq_gsJ43H5wdfd05ZA1AmLRqxKvG0Iec6Te5kbU1TBqWfjVP9o8GKVxnJKjtNRpZioqz0NQt7PRESbdQ1p8zmHB2kVwEM66XnJrFZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/863d336b56.mp4?token=iKcsup1UB3RgF3tEVXWkCHszOH6AwecgAvxG_vLzeMjjBKnzxcp4UQkK85gjM5I-0AqaJlVqYF5KdVQ2LK-uJfr9XPkm165jEDnA5-wYCMs_gcVzWTyrWjK7hQP3xFJXTwcGxbgpJMLgkbebI9zZ4nCQBdGOZ7jN1ELLlzUfOSymhPrOcAzRQmsvm-njAetu0pkGvR-6ZxCnZqati8DVl7wztAxjJIQvo2WkmTs-3bnyDgX7vK5y5jncZRaukdQqxJbglPaL566Lk1DXiOwGrMhXDn3Vlb8_4VRKD6wkNC-_lde5AybD-mqoplsJorvnrtohDtF7sa6dXaYrV0XPplaJS_TVTTANW99nZBWKPTeTBsRt4KHgWoiV1OKPubWD2m35wuI8LRWjS5bosLmwEuxKZ2CSqESWoq9CUGTaGidzHKvFgUQ43mRxMHQlD8JhVKtwH5-u_m10Jc1nkkHpoACazOVKqbGjW0NR6SLRmTAFgSpG9jASmjP6-boX4W6Q8cneP0Qve0Ixih7UHmjx3_yc6H1Cq6jmqCKYEy_d_P0T77QnU1CqmnZosYk5JzcbDcSxBuq_gsJ43H5wdfd05ZA1AmLRqxKvG0Iec6Te5kbU1TBqWfjVP9o8GKVxnJKjtNRpZioqz0NQt7PRESbdQ1p8zmHB2kVwEM66XnJrFZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خطای شدید روی وینیسیوس در بازی امشب با ژاپن؛کارت‌قرمزنداشت؟ داور به کارت زرد اکتفا کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24626" target="_blank">📅 21:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24625">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGN50fi-9EQaM8TGroF7_kICWrFLmk6gL7wXqAj7eUgYYVmVQWPdrwtfSQazmOAHB9eXLqx0jOwrzOQkvyDPazSfbFOe6jdjL3YaYo9oeDaimfN1BCEiizGqseJ16PrRLXFir2gcNWTqc2hr3PaEdrTND7UwlIQaBOUwTBZMJm_qB6Vvwb_IsemzShJ-dAR1wCaMykrRvNCm3ZQGkoFpPGPM_RSrdW5D9hRBgPFPs3-XVUT82Cr5dB7-SCgCh6FTagjbRyj6DjhTrRLVSbOyEGDIF4kyS0V2AgeaqfNRDnVAFmg9M0i4eW1D-Khq0o4r4efnLASPd9qMOGQOCmBhIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک شانزدهم نهایی جام جهانی؛ شماتیک ترکیب دو تیم برزیل
🆚
ژاپن؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24625" target="_blank">📅 21:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24624">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7056183539.mp4?token=oiXKCbylLop3UdCbo0PFoOIDJU0n7pF4waNGiEX200RkJEcUeYyfZ_2NTsPbbeHaiF8PopjSl0_XZUloS7MJbwDhjCfENyYGCNsUjG7lPpnGnsPzkzkCiMf5RhA-IQAf7Sufyuva4VZqDf1MasQGRuFJKivmTOzKETjScskNvLdSz-BO7xKNpqFRCk3wn20R7UAnrtdn-DtXmpscynW3an3USs79stOySCd3_2RVi6voH3C6GsKsymCeRrS5GUSmOZW8H1ghfci7pUaWqKPnP72pkkkXG1SzpvGMKkC3uZ8OtCn75vqu_N3oo6Fq7qOiQQWJ-gmShI9wdENI6PcvawQnXvmUoBCpzZRZP5jzW4QgMUasq7PUYNOfXH-2Yh_9mKf0v63nlrFePGi2-Jh3W6z5d2VTsT7_2siHrEZTeMkIXKUyurU4KgReNvN-jDNbb3JxBNJ_S_6mqG2GQL4N46pnovMN2y414A63Fik0hjlLn8VfGVJ0XGpB_zx93KIMGkyQGPmefx1WM2Ztn0qjcBWYtwSpPlrdb-8W5vP34mYV_FGjhZx9YGLv_M3u5KtIdVHwYjJDE7FSFTV1BxbFM9ILrGcPNqHdoLcwKpTfdFzpvm80fgRJ-ijF3wGi69JHrHv8UPBTIv1MvLV32Tyg-u93X3BJaadL_3VNV7FLQfU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7056183539.mp4?token=oiXKCbylLop3UdCbo0PFoOIDJU0n7pF4waNGiEX200RkJEcUeYyfZ_2NTsPbbeHaiF8PopjSl0_XZUloS7MJbwDhjCfENyYGCNsUjG7lPpnGnsPzkzkCiMf5RhA-IQAf7Sufyuva4VZqDf1MasQGRuFJKivmTOzKETjScskNvLdSz-BO7xKNpqFRCk3wn20R7UAnrtdn-DtXmpscynW3an3USs79stOySCd3_2RVi6voH3C6GsKsymCeRrS5GUSmOZW8H1ghfci7pUaWqKPnP72pkkkXG1SzpvGMKkC3uZ8OtCn75vqu_N3oo6Fq7qOiQQWJ-gmShI9wdENI6PcvawQnXvmUoBCpzZRZP5jzW4QgMUasq7PUYNOfXH-2Yh_9mKf0v63nlrFePGi2-Jh3W6z5d2VTsT7_2siHrEZTeMkIXKUyurU4KgReNvN-jDNbb3JxBNJ_S_6mqG2GQL4N46pnovMN2y414A63Fik0hjlLn8VfGVJ0XGpB_zx93KIMGkyQGPmefx1WM2Ztn0qjcBWYtwSpPlrdb-8W5vP34mYV_FGjhZx9YGLv_M3u5KtIdVHwYjJDE7FSFTV1BxbFM9ILrGcPNqHdoLcwKpTfdFzpvm80fgRJ-ijF3wGi69JHrHv8UPBTIv1MvLV32Tyg-u93X3BJaadL_3VNV7FLQfU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
صحبت‌های جالب حمیدمحمدی درباره شبه علم، خرافه و فوتبال در ویژه برنامه جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24624" target="_blank">📅 20:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24623">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_P-N4nuLhdJhVuyIDg9J-ysKgYyOq0Grbs9kAayBx0nXk4SCkW_DPVwZ0NB8um0LZEBDvZphqVc2f63Uv1L6tP1EzX0C2COvXcKmFZsE4nUueYju-X-OwOYgp5dwk6ix60LoJsCmuCmdrIigGNJOIHOvsYtAYaFE6b8JQhfXSToxU-s5UuAFpjruxHnu9gUiYYKF_RW_MnVHtZTymuVulnmfvfjiseoi3hneexbbfjiK6Z0Ncs9BENYjvoghBeCriXeF84HIE2c1kRAanAaCb8frmR-VdGpLCsusC_t-H0WR7BnSBvKdfu82GGxzptIRQ-enw62soJM_a-VmQf5rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
طبق‌شنیده‌های‌پرشیانا؛
جواد نکونام در جلسه با مدیران‌ایرانخودرو برای‌پذیرفتن‌سکان هدایت باشگاه پیکان برای یک فصل حضور در این تیم خواستار 55 میلیارد تومان شده. درصورتی که پیکانی‌ ها موافقت کنند نکونام قرارداد خود را با این تیم امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24623" target="_blank">📅 20:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24622">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tO8BYls9jRDe4F6PAaQeabM5e-4VvKfRPUzdvoljyDoa4U7fgZhlA09Kpm4S4LLBGcdlPHyD1cqu5GE7-riRxdXG8AysG5-ftQ_3EppL_0nicZ70bmzpBrKDntS07qq16hmVT-1psVjXpESsvAZrBU-qOPzTfDwHhlntF-Ygj4eUPfLnlEg8M0n5iirwp1FAdfpvmwe30q5lvPnR8k1_d1lbC73tbJOmkarjhbLdUqR9b1e1ZT5POJ2kIFZ5k4ACyyyCGvZKHbW2Al8vu4ZzsVNN7z9hNdU6dBKXAQYmn-eL3_wgWQoLTAKkFgiQ2UP8A1ahSZ2cqUIZof6KldVN_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه‌پرشیانا
؛ سیدمهدی رحمتی بعد از عدم توافق با مدیران ذوب آهن؛ با صنعت نفت آبادان مذاکرات مثبتی داشته و احتمال اینکه به‌زودی هدایت این‌باشگاه رو برعهده بگیره زیاده. تیم صنعت نفت در آستانه بازگشت به لیگ برتر ایران قرار داره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24622" target="_blank">📅 19:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24620">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tni37eAr91VYFAc6FVULBUJI3GjzNjQyrP-ZfRP2ecRK8UUUYptNUPNqsp-uJU5FtfNEheAi-QpQPrOf3jFv_J7vl1efxtt7jJ5XkelqVsEkV_JLU1RSSbczrPqNJ8pAvGqmw3VarLtoo01fQhTRMXON98rwzXF-_siCPKR0Cxoq4ITecJYgpukj88h5XyjfVEHAgUuumttg_mVt7fGXLyZLnZYLbhn6Keaj6jLbYkP-23p_K07dq8gi6ecCa_OE-5ZssQFUm31D0Y7VMow0pJBxnzjAPMwc6Sx1C2u3MSZtSm-cDlZ5ZHKL9hcMeCZJopyb40RjLFUfwuAWs-fEiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iRiHtMTWwAy94S0DcxuCwVQhlDIzBcXSa4iFmLw2acvf5QCQtNEI0U4PoSuukyoiWAb1B_xi4nQne7c8AyW2Uf2hMh_mwlSewkMqRGh83BWHxXgy5XeWLDZJ2-tlaP7l9vxQbt-g69YIU7yFJYMgqk02S-uzcbAFxbuVoHmIG1ksC37_PW7TR40jhSszgRu5v0NxEVtqrhjo-PAi3K4oc7id8cOUPvLyKCg4T_wxIukLdnjtGc367askvoZb2sqS4KIlT0yWUu9mZMp_Y6SEMMfxyIrAX5N2ibqwF-UeyF3Nxn2ADa0YoerOBN-zg_rSbs2rlcy94vQ2sMTeoxmHNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
از تلویزیون تا زمین فوتبال؛ بالاخره اتفاق افتاد؛ تقابل جذاب ژاپن
🆚
برزیل؛ امشب ساعت 20:30
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24620" target="_blank">📅 19:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24619">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBMsbk5HSM2GpEUD4CW3KGeXoJJo1Bu-QZ7bHIrdicnl8JxDZl2iie2z61k1hy4_MZ8l--de8oc0HoSJgbT6P_h5QrO1A-x6WwswTB3cGJk8b0JMgmjNGPv8Vfu3XMsCpqWdYbpVcsN_b5fhFy8pc6ma0qhshwZT5D6qexb_phLwSSClhvdykIEuRZ94YbIQt6V8tbEpepKqQRAEmIVJHEaNwCGNMD10_eTDuqvei9nGFFUo23fvsI4UTqV8hL1FQiUJbdhf2432wLbzfh_kxlBB_tN1aYbZ0_dn5bSS6jup3S_AGX7LaXiLgti0wwu2y5sle-8a_Zxrnn3EVaSqcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شانس قهرمانی تیم‌ها درجام جهانی ۲۰۲۶ از نگاه بازار پیش‌بینی؛ فرانسه با شانس ۲۳ درصدی در صدر قرار دارد. پس از آن آرژانتین با ۲۰ درصد و اسپانیا با ۱۱ درصد در رتبه‌های بعدی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24619" target="_blank">📅 19:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24617">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENFRSAQ55GR0GaXdTypQLWXXaH2kGB3AqOk0UAGcFRsGPPuWgvDnJc3DHmCiawhRKwCC87nWAvy75SepBJOYUnEqRDNDnPzJov6wcoqh78nBFVuEgwWtv2T8O0ZY27SmpnAw-QlkC1GKAIayErJN183NH3FgTuCrS6pfVxXI3KaokU4kQPP3jpHk_MKjFmoApej871idRJoGjW8V_2fmOZLSzJj6q7M-Yr1DwxPjKSDejgd9iMyXCuPbGX9dky_4TFzKYZ2KNcdybHuT_8N6H3BJbsCw3LVv4D_m41Vcf9K7fvt2u4Oxg5RlbdQQoaVm1jv000fWL2pnYU9xMxXh8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛ ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر…</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24617" target="_blank">📅 19:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24616">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uA0hNrjdBVBg2DZ9tpSe0Rl3ESE8b3CKoOEael0DreMRf683huthxR2E1pX0XtsERBOTGbqYbWVOYeKxw21ji2kLukHmRXqDMdLudpHpG8PVQ-ed48dTSqadZEZ_zfv3Dtqn9FiGY5mezaxQc1Vjq78fVL9JRHWUI-AEA1GGgEUFO1B7n3eFgZqyg_ook9GlDZG6d0nx9mfm1alyCte8_JPNoZ8xxRN1Dk6bo1FAuNH-cZze9odU3h2RzAU-_tECwqhvO5brQaMvFTybmjGLbzTFmFYffj8xuo4Wd6cE48_rt05x4aZ5M0VZHcTHfHFm81yhWjjbcPQ9xtaRe2xMnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
باشگاه‌هایی که در جام‌جهانی رکورددار بیشترین دریافت جایزه انتخاب بهترین بازبکن زمین‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24616" target="_blank">📅 18:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24615">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONmLbTSocA6NJT01TU9zuedwMatv3O1YCuw5Cqt-73a_y-uzZ5ugVcWa7JZwB3Img3tfpFaRmypgxCZc3w0C5Da_nRpTK28C6-tk4ntrCe2JslN79oqFs1N9Y3tOHL5XFkvijxnWt6TvPRglrXBiAqcqlDQBBJz_K0flJb_vxXP2DvledObSIOSNPz66KoWEwJKq2eF2YqE5tV3ZDra1Oro9gGnZf9py3fEg15DAUxlB_LD4qPxnvpLrXnm6_aDBo2v6sa4KlcqAqIBPyAeFJMpSDOkC2C0MQfU_Tm68xa3i1HhTkI0lexNHFK7Um7TffIfaeE2fNqht7Sz44G3CSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
باشگاه‌هایی که در جام‌جهانی رکورددار بیشترین دریافت جایزه انتخاب بهترین بازبکن زمین‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24615" target="_blank">📅 18:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24614">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLxL9RTRhf1SvhESccGYWzXDip8GSiEQTZztlvrsCmSIVhHQSUMb0LjK8LWQ-90mu8o-mukcjRFOkS7wQcUbKBWR1Fageo8drS5nR1ZPomeBpdu6O6JQL6cJBKI-jW1DL0NyeqSwc03OSFj0Y3FkDrJA6103lyzAu0SyC2eu5LKxrPBWJ5BmdiobqAMTKeS7lXYAu5UQu2-36J5V-KMY2jC2VnDFni7Uq4Dk5m9WDKmS7OqNNGHumTKfSeen-4BjZkUvGErf-bDTGXHacUxJzuPUcpErXzvHcfHx5UnibRt_a7PnA9nixmS5VxlsI8nEwf2a3Uv5sjibyik8DzBOCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ نشریه مارکا: مایکل اولیسه بله ضمنی رو برای پیوستن به رئال مادرید به مدیران این باشگاه گفته و اعلام‌کرده‌درصورت کردن رضایت سران بایرن مونیخ اماده عقد قرارداد با کهکشانی‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24614" target="_blank">📅 18:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24612">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZbAeHOa6mmbdyeUucKs53kBY1OnO-Qvqe5XiBHrio07UVmDOLNZYodmFOabicvjTLN_2AgTCTeCYLjFfG0yztJRDUo4XlvjU3Yas3zD2ncEkhiMjWiqjX35WEvRJ4VjK5GPGBT48rsFa8EXdSJETQLTXQ5H5SAPeAVHEvsWO9YB1nAV0rnnyDjtrZYs-B8Bn5Z1ULXw7XWKxe18zrQdFydqlVJb-cMXyLz7nLjTO31glTspySRnhN-eGeRKDsIFfT75_M491eM7KrwVCrIE0I87dWIPXyBztXlQhifDoZFyvN_SWbZqOILyHYwqqgAGfXYdKk2F1zOm5VqSbH-AXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
محمدمحبی امروز به‌ایجنت‌ خود گفته تا دو هفته‌آینده‌افری دریافت نکرده به استقلال برمیگرده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24612" target="_blank">📅 16:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24611">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AChBpk01FsvPvnRjyxk9Qej6YWCMnxlLXGOOcoN4C3vr_jPhRX5B_YZe6hnAztttJZBKAmuFD8GFcXSqdhmlpEGH1NrMnrr0kmRFDZ8oUAd7HUMNGhAX_ogQ1Sdojr3z-f8Kjwlq-HgF_oNpGFUYmDPFpfTZl8IziupnnCljfFEFxPa2kYpE2DnuAp--afxI7wSxK3iid7ay8FQ_CrkEVsAvDejxWBogm-aNRLyoCVc8HaowE-hBnh2lZX192PqsrfsrrR-C-XIEusRuL2XWshqcJfgYxRGac2srgNJ1UhzzzLf-aGw_mN69U4eBgUVLc7saDgfg1z7r4aXh4GEgoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریتزیو رومانو: انزو مارسکا با قراردادی 3 ساله به عنوان سرمربی جدید منچستر سیتی انتخاب شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24611" target="_blank">📅 16:41 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<p>@persiana_Soccer • 👥 356K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 03:29:46</div>
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
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/persiana_Soccer/24728" target="_blank">📅 02:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24727">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDJ64XNucJR7hbbtnovGq1X5IC8tYi_PXPAH9YUQsrBJhrU_001T8ZJENlL2jtQi43kpu6sLjJnTmTY5ecTLgomEb0WaZljsdNFYvad8BpnUos9H3ht4g0OzC0cDyKwF8itxGfLuOj3eWbikvEW_di8s3df1DyH5AhyKz6BscfPlPIEFAyfS-0uT-0DQegp1oKh-FFuT9A2McbNAOmIhPXXYob5eIbz6Vdb73lYKQIjLF7dWaCql4-2K5onwXw3NhQRPXLZ67LJVAPtU9ZHgI3ug0XPWm_k5oWeW7WWpEKlrK_4v4Ljed_CTv8lpRZImXH8rsCTHf0huZXYntsCaWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/persiana_Soccer/24727" target="_blank">📅 02:30 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/persiana_Soccer/24726" target="_blank">📅 02:23 · 10 Tir 1405</a></div>
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
اشتباه مرگ‌بار و فاجعه‌بازیکنان‌تیم ژاپن در بازی شب‌گذشته‌مقابل برزیل که مانع حذف این تیم شایسته از جام جهانی شد؛ با گزارش عادل ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/persiana_Soccer/24723" target="_blank">📅 02:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24722">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J47ma4SayyIgs0CJU4EPRtiTL696VwtJ0OV0vQsIspt6b4hFL_qNcu9SInmmaQnDQpcBIAscLXYAjMOhBTr142WtLUc60XybUjXaYwps4jaXCef3X8ADTzeQAIK1TX3jrAcEv8CmI_FZ0wKRu9q1DBzfmlDLz29ya2-8gyxOUAa3d3F5ow3qxL-SWhIWC7NH3rrtSaXhyNuRsROP1I1C5ZEwevvXBdYPhsce-Xe-5f47jZqmvez52ZhJin8_eFIKJSMg_MGxpEXsuWPhdbChERP1tBg6175uXUxLIbbEl-nKhfg352HN4d6QZUO5AW_2leJ9OSUeT17d1LbE6qHsMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بعداز آسانی؛ منیر الحدادی نیز چراغ سبز نشون داد: تاابتدای هفته‌آینده با خانواده‌ام به تهران برمیگردیم. بااستقلال قرارداد دارم و به آن متعهدم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/24722" target="_blank">📅 01:52 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/24721" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24720">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7qVUJN9x4VxDEz6m4UAJoVe910SFityoIpZ75jgu_hpx4tnlD_xKXYgEr9hqmgrMWFZCtcMN26G13ehTsWN3Tlukd7Q5vr9U9U2yVCEVO7u2z4QWEXAjSvHCvUVOby8R4eA5OXPgir0WBmtwm0vhop8L8Rnl9YGFJ92_pYgIG37oHkuhc6zJyoMrwyOk47X221IAlsHL9RlCc6SmXMlgqf7et_IugGfCNCqCKBB03zW1Yp8i50AE4I-lTOeknNHy-eG7smyfGC7uDZBmIR-apSYI_DG9btzL_B415KekDwmc9VCppVYhW1nZE4iXzzNE0I2yZBm7JPrgoSFNJcYPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نشریه بیلد: هری کین اگه با بایرن مونیخ قراردادش رو تمدید نکنه مقصد بعدی او قطعا بارسا خواهد بود اما الان هدف اصلی بارسا جذب آلوارز و هدف کین تمدید قراردادش با باواریایی‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/24720" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/24719" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/persiana_Soccer/24718" target="_blank">📅 01:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24717">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/df_E89dgBGGFrYZOu_H3fZHynYsq6JzF9hZsXnHZ6ayuw8f4ujHd9LtnTsXSR7YUWCflrELcS5JkGwlEVPVKJmYbMNfwARano_lz4OPSq4_x7SH6bJSUwawX74IhDOl83hXJrKeCigsoNBghAJJA_cC79CqgJ6iareii_GNszNZ3oJKBLMG39NSAhoECr6_Vw_4YepEWi9ETMuv9C8jwYUAXbRpzaU414ZG7-vafWedHMwOzmJvDvGvRMYUbhLcmFTlGwe5vsogi1RUfvo_WfR38zYuLCPGyinoKTaBk-gDXoWMnvQmN7A_HImu4AFpeYSGt4D8isToxbXOUT8ze3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/persiana_Soccer/24717" target="_blank">📅 01:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24715">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQ_xPAHE_4nwqeF_tXWDFSGoIP2JPUWZJWXkuPhjv6Fb9jpaAQBoMRIjBqfU_Mwve93hZGH9iJnYG25-te4jVXcgBY2lqYO6RejGcI8pXjheJUdku4veUm8YNIyqr6AWgrs7csGU-p6T9EP2cShJTFwSnUYjWyJfX7DaSQ-2xpY9Kd0LEReUBpyeNCZiUiOjdQZrUNp2Qk7aLzHdZCXOC9n9csgaOuhy_y8rqcuWqRqZWMyg4F6r94oa7o7TyIUYFUKe7OQDwocoD52WbreEv7X3F53vShuxGtnRco1lwgoac8gkcOktcpuX3ChAzGg9nEjDILRDgqkHpy3E9M5ghA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
جیانی‌اینفانتینو رئیس‌فیفا تو دوهفته گذشته 24 مسابقه رو تو جام‌‌جهانی از نزدیک نگاه کرد و بیش از 50 هزار کیلومتر رو در یک جت خصوصی گذروند.
‼️
براساس‌برآوردهای بی بی سی، تاثیر آب و هوایی سفر جت اینفانتینو در این دو هفته با انتشار سالانه گازهای گلخانه ای حدود…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/persiana_Soccer/24715" target="_blank">📅 01:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24714">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOZ_D1udFyesgBEYScwQN4m3RXKOV2Mma6Vutm6uga3d2W7Eyhhbm48aAbGJp3MvafO0P4Zty0gHNK9aorCPOdUVYuDh095ELzE1S6POC4LDeu0R1fQPOjjF3sW2C3JYLbrMDpfTSvvMMgZzh9R-X1wZ1rRmppxkUtgDvawqzEv-tM-k8X7mEy7X3RF668iLWroS0KklFKq5HQDwpwADMNwAGmMw7RMpv8pzRQ8owLrW8py0V5bBcEv76Yawy3AdYWngPPl7Lq8tAAVgGcTgY2SS_9WroT-0UKtijLoeSozl7P3oxyW8HWm9fyKtb6qKIAgOT25wB5qsPjIBJNkT_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏این‌چجوری‌هرروزکل‌بازیارومیبینه‌اصلا میخوابه چیزی میخوره؟ چجوری به‌این‌سرعت جابجا میشه؟ منی‌که‌میدونم از اینفانتینو دو تا هست ولی نمیتونم ثابت کنم‌. مگه‌میشه‌به‌این سرعت استادیوما رو بره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/persiana_Soccer/24714" target="_blank">📅 00:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24713">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9YgkOrtOtxaK6lEIS7-eX7RCSStLrcKEiU_wwmR0MBm1Zwjov1jhh5rlPReIw9xmk1x9Ucxx-JAk6zYnqGcB75MbpuVwZc7jO3xBy8NSJFVkPKePYbfM0jcOIDqvctaoQABiVujrF7hgFMi2tH2YMsmJXx3S98YdzV3tn0PbJ_sMubix6ofrX_ScS9vWCfxy7PlwHDnwEIJi-zZzGE93bnuon2Wo0zi8AI7YAMxyeSTmDuA0IzOBPv_bQcJcS43RTdUchM_8XmAeJdLFJzLMQ4RX9de5dtD3hhy_9KVPECV7vKLuKQb436NPrdaw5reSbmhihnV2GGt_O95fGlVZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اگراتفاق خاصی رخ‌ندهد گابریل پین مربی ایتالیایی سابق تیم ملی ایتالیا با عقد قرار دادی 1+1 ساله به جمع آبی پوشان پایتخت باز خواهد گشت. توافقات نهایی بین طرفین در ساعات گذشته انجام شده و با دریافت پیش پرداختی قرارداد…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/persiana_Soccer/24713" target="_blank">📅 00:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24712">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLUlMjjFP-jaqC2mZf_JkuWGl2JdANXZbsEoqk6aeTO3-N16OVOnij0EdgGn0U7PGPtsQwpMsha_Dk-Aj5CXcq2zFkwKG-MAO5G39H4Ypp_JaetuKfhwco9b2mjf0QOu7pM1-iang-6j1xqoQVPi8CHWt9pNmeLfWBXSjywy6DUTgsvh0omcKYVSdX-FSB5VaBp-G-WB9i1cBvjISvtIDPryICwLlAuI-IbCSLOZbP2QSHA1H5VKNseOmXe4G8QcznaIQDNrLnReQM_BmSZORdV0uGHqlC7jZihD4eGMWfOT-Xwslzj_-Pu5DG3j-Obl_kJZZyUbXoD-dTvhIoWAqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/persiana_Soccer/24712" target="_blank">📅 00:03 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/24710" target="_blank">📅 23:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24709">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g219ldTcho1iMJ7KwQ-ouyl04AMLIDPk9EF3cqpTc9nQsLR4N4lS9oFdhOwEXAfboAwV6HDed6uhqxwQWIPTheU55LHJgpkspA48g06KUZLUa9n32O8iRkaMecwp91uO2tXBzSBLmOe9x9179hIIoU2SbmwfKtkbxpgzqrHipGGuYMI-PqegpFE_DWlLJ2GAJKTujAS31ne7h4eysWLB6cKP8GXQ1wWEgluB7mi_UKVI3PhbcAuT7K1cBLeS4xoEuxAC8MwbmYvqR2JhymTgYy7Ab70pRRDXwZ87sCnlMuklIuALt6RlfnnZglu0Bk3FNbSBmVj3tQP8dVgSrvw7jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای دیروز؛
از وداع زودهنگام هلند و آلمان با جام‌جهانی تا برتری بزرگ نروژ با گلزنی هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/24709" target="_blank">📅 23:42 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/24708" target="_blank">📅 23:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24707">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Am1hd1bno0NTAnTmYjQYN-kj1MI00CRpsI4hRpqkmBgQneUVAo2C9__hE3LhTgi5ERmHZVcVHFBhQ3mlFgpDZ5nS9WpsKSM6FT17D-JNWKVWrsxlGWDYWvoVVD7SUDrYycTSoC60HwSmcX_hsu-qABGLDu8u47qdufsYmgjxgGBlTSdVUUEyOFlHaidZ2O_INOR7ZIumMpNlZVWxrHfsnTyF6lNb3_Lzy45pQ-ipu99KYjRbbwkU7L6d8fum9V5-2BGWoEX2xDSESYH69DLd3QcUhcnDVTIoEM6hZ0Gd0hW1TtLfii7yEKIgxSQyLDUoMYV470U92UpMcHMGCptSlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نروژ باگل دقیقه 86 هالند ساحل‌عاج‌رو شکست داد و حریف برزیل در یک هشتم جام جهانی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/24707" target="_blank">📅 23:37 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/24705" target="_blank">📅 23:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24703">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mG5YSnWAZvdKGUNRGSP7XKBUsEZZPN5eAtJdEqdVfwZKG7Wbzyf2A3GzEV7BKlLfS89bAEaMuoY3z3MIGUUCMNSSITeteDw75X7jeFFtMPRQCm7CWgO-qGiw7yHRJJbWjOq9BJtvqdwO6e5lHugqBldH2WURcs29qQO0h9zb4rdwzRls5SX-V0wkIX0NbB79do5QQVqzg7qWddwrT5NnTQtWKCbRwpBHPa3TUlSvZLVszpykVTxgB_FfnHRX-T-fX-IwXTBtBABL_GW_g4Z4NQ_69DGi1h_xzqTVhDsZQBRw-aoADHWCOHaM3oG56KriQs6dsqgD9xiby9HIlcJHZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dr-om08pVyZjOdv4mIrA-Zx--sqii9yT3kUbu7kFbV0cILru3VnLBi7Y1u9YgA0133GvYEhy4FDGqIsP8l_OB2O5UhLb6b3iFFfmM2DI526eHHQ-3qf6mi3p7G0dbdsjphCn9627-sMYP98fC7q0eNQ4LBwGISZn0i9J2O-0qIy7LaWuJmQ8LJ7Gx0DzMQh2cCtfOJ3DmzRqRbfYsYjRL3lrl_GAz7Lix9Zo90RhWprGL2_og6aOwSteLgLQpnYgXnWs1xGJb79xH70G-JIXQ9zcDYMv76WlTaCQ79wWaKE7LTTsyn_f0dRO3Vha6D2IOGJAcFB4FfVQjWUJP1ru8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌هفته‌اول لالیگا و الکلاسیکوهای رفت و برگشت پس از انجام قرعه‌کشی فصل جدی
د
‼️
دیدار رفت ال‌کلاسیکو:‌ یکشنبه 3 آبان 1405 در نوکمپ؛ دیدار برگشت ال‌کلاسیکو:‌ یکشنبه 19 اردیبهشت ماه 1406 در ورزشگاه برنابئو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/24703" target="_blank">📅 23:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24702">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccKE8qDkqWHjD37RhMtQ5KeSRHZIZazEQ6gP7fKvvVwsGepaW3P4Hm0EzjAxWzmG3ERNe76GGnei7g03PeyJz0p3aDWi7LO1a8HWme2ZRxFHWCvBCC052f0DgDyitC7nFnl1vNvqhXkBe0wJbEv_YzvpXzxiEZE6-jU8n-vsvZLcjQezRzwjIesnrD6PRpahdgIc6X2B1uuCa_jMnSFhVRoFkKhhnUA8nYe6qtaY63XDrQXeKUYROCzXC7lf_tmySR9GiIveq_gt_fpklzghUUqAC1dHUMNAuWizP1fi7EA-aVEBor8uveyY8Q1F6qkU66Myljb0svZlhhrD6QLl0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخباردریافتی پرشیانا؛ باشگاه پرسپولیس تا پایان‌هفته‌از دراگان اسکوچیچ، مهدی تیکدری و کسری طاهری سه خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/24702" target="_blank">📅 22:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24701">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLnIdfs_am2_a2irfZi9CEF21zixY-pM1_5iQYYgSIh5hX2kFI1mkE9Y2BvKiI6YsVBFF6lAWTvYjIpMpx65jp3SiUqRtZK59JyGDs75iZhQQGDGsRD2uX0U0x1x97fQh5aQ92hAeBAoYXqCX3NrAg-OtX-7TRmfY4Lco_gUOzCVa3U-Z4nK6yFY6K6QHRuA0vOscYEFU5aUBomfeoTNdXO6FKSaUUH6jEq0iSozxataiAJUYA8RfcMo54cbmQpeUBcORKjy5eHYOBMv7iGf5r9FSy17clap2T1001xsghqYLiBRuSqTHcJ9y-BjGqo8TRAU1sTZgp1coxapHhv1zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تااینجای‌جام‌جهانی 2026؛ خطرناک‌ترین چیز نه پنالتی بوده، نه وار فقط و فقط یه عکس یادگاری!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/24701" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24700">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJRoAmosYAwTmtUiAs7-lkWJnwY_j3Ixtg7LGU4mD9tQHTvuefQ16dBdyGMBEFMSNL5EIHLpl6YHHWIVtSqxutTf5H9GJdaC7CR5SJ5s4VPkSNnKb0b4CrbKGDDD7iwszKbNfs_N62-SYSQg7SDChboQ4KfLAZlbIPQ43WIEAqinNAVjIKhP4iGjCQTd92kgX51l3TTXqafF6KKZ35R8G4hnlcj86vyRRKY67X69kwJeh6emxzgax8FH-tTiWZqBI7qHzjaeOBW6Qhr_ct4-jA0TA665dK5eP_sjVRyafSWTnGKePdza539ESwirHYWKV-vKXNvlLHW03Udjn8LNcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇳🇴
سوپرگل‌دیدنی نروژی‌ها در بازی امشب مقابل ساحل عاج در یک شانردهم نهایی؛ چه کاتی برداشت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/24700" target="_blank">📅 22:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24699">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XN8E5EHIz8S2wOQANxf9okRmytkNMnJz6PDROHGdef9mypBwzsUD31WcgsD6iHMxePswKVg7Imu61ByjBJ9v9cI_jauinKE54FlGfdVlikJFRG-n1yZaD-m81XYTqMQv4VkovAwIw7jMynznAUh6izF8DwQ7J15b7IISxy222VshJqR74Ell80t2cAI1tzVGVi1gSJIoUYpFHtxZT-Jv1oFAOFtttEykn_UBF9u3kztYOmnZ8UJ1BIG8M2ETaKSmBggpWw4jTteoGx7aDnplm2RTc-Jhigy10rlh46KzoD47F5wXqzzPaGsEe3cmHqTV6GA6xjdtYle4iPrT4Le0OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال بسیار زیاد بخش رسانه ای باشگاه پرسپولیس فردا پوستر رونمایی از دراگان اسکوچیچ سرمربی‌جدید خود رو منتشر خواهد کرد‌.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24699" target="_blank">📅 22:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24698">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HkVdl4aWrmcD0-A2_biYRPwxfrqKdr2cHc8CbE5Yl-nFxv_fPUDspNZkOjGmLWobLs745wwAtbvR77P1C_h6iSAU51orEwtM6dcETFVK8deCnk2maha9sFhndsfKIisZ7LsT6wIsh_lvRvTBqj8RyD1Dc4vkh7WR1-9gX9J8eYlhQe-RQavSgWImn-_M0ClY1MNpeeMYVzBO_lWxoV4oEV6GHNiagm3jhot3pQ6MiSPSk2KkYhHkBfzEXNdt-p5s6vMBowF7edwQr19vdGy_u97OkkdKxKrU2J2IUiQZzFCfKSk_ragaitLSSizhIHzyqCqk_ZAdDIUheeN_gkHVDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خداداد عزیزی در ویژه برنامه امشب جام جهانی اعلام کرد بنا به دلایلی پیوستنش به تیم پرسپولیس منتفی شده و فصل بعد نیز در تراکتور خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24698" target="_blank">📅 22:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24697">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b011e22cad.mp4?token=dzzMgWHaFS5YeiGDShIN4Aj1tFkUeoJe9p20vIyvsqqn4jbsMNE_IqlPydxCkGeXaNTmEBVUZby53s_xgTCmc8eGap3dIocd3kZWjIhyzbFdRqWb_FJQyabxsVqkJ5doMyFVfp_pjnVV_fEbW8NeJzCmSQPIv1C7hqUNr4Yy8rdNEx2EVF96Fo5fxHFWzly7pZRyi5gpITisPgI3jkZ4Wwvo7fB9VYwuFiZMlZfazIxDKck-GiTZDPAXqiKDj5_G5Vy3s7ejUaTPlDtzdbcpi2Sa8NxLx3GNbUEjTf0FCCdNFxhhe__MY4SYY357ESwHAwkPrW0Q7ImW-NH861QN-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b011e22cad.mp4?token=dzzMgWHaFS5YeiGDShIN4Aj1tFkUeoJe9p20vIyvsqqn4jbsMNE_IqlPydxCkGeXaNTmEBVUZby53s_xgTCmc8eGap3dIocd3kZWjIhyzbFdRqWb_FJQyabxsVqkJ5doMyFVfp_pjnVV_fEbW8NeJzCmSQPIv1C7hqUNr4Yy8rdNEx2EVF96Fo5fxHFWzly7pZRyi5gpITisPgI3jkZ4Wwvo7fB9VYwuFiZMlZfazIxDKck-GiTZDPAXqiKDj5_G5Vy3s7ejUaTPlDtzdbcpi2Sa8NxLx3GNbUEjTf0FCCdNFxhhe__MY4SYY357ESwHAwkPrW0Q7ImW-NH861QN-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اون‌بازیکن‌تیم‌ملی‌هائیتی‌که‌کارش‌هندونه کاشتن و فروختنه، وقتی میفهمه من رو کلین شیت مراکش بت زدم: این چه سوپرگل برگ ریزونی بود که زدن!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24697" target="_blank">📅 21:44 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24696" target="_blank">📅 21:29 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24695" target="_blank">📅 21:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24694">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72b5a564e.mp4?token=iIaTcFIqbXhneYRHgA90lt0cLtpx-nWoXMzBtALoCSG65NDBmZLjWmDIkOC4h12UKOs8b7LHSChgm-AQEuLod5Q2XDk-8nRilmfX_tZ63hIJH6q-UxmWwmm5k8HBS1-zr7YNUntBvjuhfUNx-Emq7G5E8vv7KuaS3nqQXJ0ZxRKMoMl8n56Uud2SnWFfymLuLNhmGwDszjxs_7O2UP1SQKywVDsROtpqBSnMFMG6KX6LXzk7PjV2S2JolFp-B5_1n4-0LeuDGtaQ6Mo0TUpZELqgN4u80ZYKgHip6L6lNY7rqak-lP2bAUHSmQbcbLk4CulVnaZmEWSDu688errU-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72b5a564e.mp4?token=iIaTcFIqbXhneYRHgA90lt0cLtpx-nWoXMzBtALoCSG65NDBmZLjWmDIkOC4h12UKOs8b7LHSChgm-AQEuLod5Q2XDk-8nRilmfX_tZ63hIJH6q-UxmWwmm5k8HBS1-zr7YNUntBvjuhfUNx-Emq7G5E8vv7KuaS3nqQXJ0ZxRKMoMl8n56Uud2SnWFfymLuLNhmGwDszjxs_7O2UP1SQKywVDsROtpqBSnMFMG6KX6LXzk7PjV2S2JolFp-B5_1n4-0LeuDGtaQ6Mo0TUpZELqgN4u80ZYKgHip6L6lNY7rqak-lP2bAUHSmQbcbLk4CulVnaZmEWSDu688errU-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
👤
باشگاه پرسپولیس در اقدامی عجیب در روزهای گذشته با خداداد عزیزی سرپرست فصل قبل تراکتورصحبت‌‌های‌‌مفصلی  داشته‌اند و قصد دارند که او رو برای فصل بعنوان بعنوان سرپرست جدید سرخ ها انتخاب کنند. فعلا قراردادی امضانشده اما احتمال اینکه عزیزی به پرسپولیس بیاید…</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24694" target="_blank">📅 20:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24693">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6-Udv9cN13f1Enyax2S9JS8VnWNsE4-sbwMu1UiA2073DBYpc1co6o8ter_po3ddWkOzyUqDPlE3yWYzPzbeSrtIrYqKhYSfUjvHSeA_585CaZtAmls5I-AYvrZ4OKmZdlTczg2wtSGxPMD6ROELsTw2LAZcJzJcTKvG7_hTwmMrLoLGnto93V4EcloQW11kygxvpIlYKWNq_he-GVrfb069QAp42r693L1JtOFjzJlqQS0YRpBV--oDMPLkoi5ena3NP8pSBxZ-GoNOE8NjoaW6keo4wZNQlnlSdiGp_keOg0ht42a4gDVe5N8AHjSG2uOdIf-lSgKPpMVwTATaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
همانطور که پیش‌تر خبر دادیم؛ یاسر آسانی ستاره آلبانیایی استقلال بامدادفردا وارد تهران خواهد شد و در تمرینات آبی پوشان پایتخت شرکت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24693" target="_blank">📅 20:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24692">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMN7AT8fRVngPS3XUv5d3wc8MsNkCBF01IRFEn1pcTCKpBgbLwPCxhmwZDa-yEh8zfkMInVMyP_jTSKoXV5juBtMyZKzKPsK6qjOadKgD33BGzEr4QbptHtNUynTzjmLmc-mKHOu3JCF2Ad700m4bZ0o87V0sdn6bk3cLgHAnhtUJR3mpdrk2jArjDuHpA8GU33roh7A0Qs1gSa1XmlHzWblFP-uxWrebV8MQ5H_y72SgSgBs2KjvbFrdrWpXOoRSeAWziK04VefQUFv0um9cLRY_mAjuMML9irTxLyKu-myUw_H7-IogGugQQl7gGvUosIGznTnWJI_MED_x4dn_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فلورین‌پلتنبرگ: سران‌منچستریونایتد با ماتئوس فرناندز برای عقد قراردادی پنج ساله به توافق کامل رسیده و حالا توافق با وستهم باقی مونده است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24692" target="_blank">📅 20:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24691">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLjnQQ59dRRCgV7u82sDsnyiy5kzunGlS8pZaSDZGrxZ6T86CThu4IFcdenOj0eaWFU_3L0-Mf4zYY70F6DyGAEw7JjEb7PlOYq8fQNTZySu5cnni-bz5WigHW59CELTyN8JTYdWdGdtKe5oFf2rsuiqT_iBdUwwi3fKNYhrBsAz5QCSnAzfZg0gT15f_XybORI_TUL537r70llv4NWdn1cOWvNNPlzH-syMBddjBacusTQb95omkknjWLgYjFs3IVizyULnS2UeBCqmJXWuU2cR21g_a3M1M6NMyYrGFJKdy-2G0qrD7hp3kuafJ7ngYkoadVmT-Qg6acVT-gcgCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ باشگاه پرسپولیس درتلاشه امروز برای دراگان اسکوچیچ بلیط‌تهیه‌کنه و این سرمربی کروات ظرف 48 ساعت‌آینده با دستیارانش وارد تهران شود.
‼️
بعد از رونمایی‌ از سنگ‌ اندازی این مدت بازیکن کهنه‌کارباندباز سرخپوشان‌پایتخت خواهیم گفت. این بازیکن از وقتی فهمید…</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/24691" target="_blank">📅 19:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24690">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrGwScrGnSsY6uswge5bAXPzBNjLdDutkJJ_2NuEzmx4h2XB_ULAx5JGEy7M08oeFP-M94WhYRA1YZGGxnJ0zIYI8TuzBNFkd7Nu0TLBe6xIQQskIfNkkinLr4_a9uTDv_QwdIjXzg3NaJEouPxx1sEIzdx4hcUdfWY_xarTQa3iSlROYhO4UsZAD5dAiiT-yGq0hZxb6om3Z8V2KQuHotzb7gM8s3gUdXhIWmwbko3hN6AFA8ezS3CDSvbs_ke695X8RfTwzEy-VcLkvvru7rW5sRKvnFhZSNbC3Rk1JJ_nApIYPMdCvke3vNVENXR-XFy4MgtF0DT_LspxVmIsnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛باشگاه پرسپولیس و بانک شهر مبلغ توافق شده به اوسمار ویرا و کادرش روفراهم کرده و فرداصبح قراره‌این‌مبلغ به حساب او واریز کنه و رسما پوستر برکناری‌اش رو منتشر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/24690" target="_blank">📅 19:06 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/24689" target="_blank">📅 19:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24686">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e47b5880.mp4?token=S9fhAAM-J75y0qxEQKf1CYkpYA54zSx7Gi76-KpF1TGX7HKkRrXD0VqiX6QMMrGbpcP0_Lq0CU4Cg0dwyWRRz4cq2jl6Od7ZDx7yjHVdWlryNFvaCCLxoVCENzJ97R5rsyzoMJNTyecBrso4ifGi8DyHzHMrxncKfjKs9P2QCyQYWrNcKJY7EfLQPPyANTN8CjZgSa_CLMF6sjVlybIEEk741w5BoHgMZOfqjhZoREhFlv7CdxLS7p0BLLb_tDHnJJZvYN2OvpmXTqov8Ik4WEK_PuyAWBOvI6OwsKAQG2rP6WhsqqETOiGn31Srpw3aEY8_UvrFl0JYxI6j4m9d1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e47b5880.mp4?token=S9fhAAM-J75y0qxEQKf1CYkpYA54zSx7Gi76-KpF1TGX7HKkRrXD0VqiX6QMMrGbpcP0_Lq0CU4Cg0dwyWRRz4cq2jl6Od7ZDx7yjHVdWlryNFvaCCLxoVCENzJ97R5rsyzoMJNTyecBrso4ifGi8DyHzHMrxncKfjKs9P2QCyQYWrNcKJY7EfLQPPyANTN8CjZgSa_CLMF6sjVlybIEEk741w5BoHgMZOfqjhZoREhFlv7CdxLS7p0BLLb_tDHnJJZvYN2OvpmXTqov8Ik4WEK_PuyAWBOvI6OwsKAQG2rP6WhsqqETOiGn31Srpw3aEY8_UvrFl0JYxI6j4m9d1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
سبک خاص و جذاب پنالتی گرفتن یاسین بونو که قبلا هم دیده بودیمش؛ پنالتی امروز صبح هلند رو به صورت عادی شیرجه میبست عمرا میگرفتش ولی اینطوری راحت سیوش کرد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24686" target="_blank">📅 18:25 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24685" target="_blank">📅 18:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24684">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLJgzDWZcG9AxvwON9lYhceyYnLF4GH8BZcYKnzbPYSbC5bVAr_MLEhNQqtRrpi4RcioAANtBgldc4svRg4U2bl97siRHtheVrIPzke7RvdbGvLhH6rCu7XYZt7-Lk8Pf08ZKG7iAILCiD5oq8GM3TEThaR4p5y3f3_5RuLWosk1jxNDX9NoDor5mtgmmY3U8DvxD8_il47lgLiYUiAWOX_tS8OHD2hCAQ7MmODCsIkwqRTwBQLtNrZcYW_C-ihTu81fm0c3rLw7VX7gLaK4v0-J5CpNf7hTIZf8vvqDXL1fC6aM9ALqs0RRSs8nBjiwwxGSIsRBC4P4HMbWQXpJvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
جادوگر تیم ملی غنا: در طالع و سرنوشت کریستیانو رونالدو نوشته‌شده‌که امسال قهرمان جام جهانی 2026 خواهد شد. سخت و دراماتیک است اماپرتعال بشکل باور نکردنی قهرمان خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24684" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24683">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CaCUPqxv32UYRku8h8qkKVQdWEAK8MtSQSZgjbsopbpTzAaponwwGxuokY5DqVCsnJQVLZpjT0jAZuANXM_nQvuBLPdjc7-IKXmp0NpnkvNi2LnmPGR0GEEWdHc8vzQD4EQvMk2wKbgGN7NuoZL8yoL3eF-pMlhW_JEbCnMJZ_X1kGBsVCH9eTc_BRTq-8WnpedUqejDJYhIUmIc5Mu5k6FVpRir2hOrsxT8-3ZHYfKNym5yEY4d8EelsQGlhyiAt9P4KD6YmAPR942htpcoW3bExbmJvk0y9iQirN9flb6Q1XaGHTqgF3W-Y-iwIG7h7T0cfinnefaydKflRMfCvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: باتوجه به علاقه اینترمیلان به نیکو پاز؛ فلورنتینو پرز میخواد او رو با الساندرو باستونی مدافع 27 ساله این باشگاه معاوضه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24683" target="_blank">📅 17:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24682">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsIXrE17XfkzWW8239RTeGd8uXxt-lz3UBWK42K4uF5GFgeowu3kJOdxtINLIWjFMQ2QxqPgQ71YgAWsnBXCBrO7yxOuK5_inqNfR9S9plfXdlP2tvA6WNcjVozwORoh3FvFBBEwaqbLEYDPL0YavgEOxWLF0yo3QEngIx8j0uZccz0qnqgJtKkGDi9syWYabscwXqfD8LcXHzgCQSznHL3bjZSPoP_EJvK-7WXMlwOdC2Cbw1EVUIl5heJYF80cq5qV0DAN9hndZO2K46pazLC7pXGZlELbyzOBlzNUJxmI9f-sOtGwkIAV-GNtj9_JVBkRgdDWukeenfCaJEaQqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24682" target="_blank">📅 17:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24681">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b6727cd80.mp4?token=QC0CcCVNr8lkSet0WcVm-rubgZTv-st0xs56uYPnF_IHywM2eFjsGS_hZqZsPORGr4Qi3djSndpFm1ux2Wc1SFE6Mipj8hACInQ3fjTQJGp63GFv5pvY1sSUFhdcWc2O7WBdBaSZlsXn1lfhZk4lv7ZXXL_Af1xoWdYrSMmF_npjpWTJZvCg8LM9fPbivwqPJQzrzKquwQP67DqJCRcKtM1E7W_GqBdu4ux5XrnVcczQsOa9Pjys3GAXXhW-PdCJNPL_mqQkTSiBWqPhDV-sYabjDGDtdAvaV4DLpaz13M0cqQ8BzAuOi7W_6nOd-IX9GlDtVQpiowQc4Yrswikgmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b6727cd80.mp4?token=QC0CcCVNr8lkSet0WcVm-rubgZTv-st0xs56uYPnF_IHywM2eFjsGS_hZqZsPORGr4Qi3djSndpFm1ux2Wc1SFE6Mipj8hACInQ3fjTQJGp63GFv5pvY1sSUFhdcWc2O7WBdBaSZlsXn1lfhZk4lv7ZXXL_Af1xoWdYrSMmF_npjpWTJZvCg8LM9fPbivwqPJQzrzKquwQP67DqJCRcKtM1E7W_GqBdu4ux5XrnVcczQsOa9Pjys3GAXXhW-PdCJNPL_mqQkTSiBWqPhDV-sYabjDGDtdAvaV4DLpaz13M0cqQ8BzAuOi7W_6nOd-IX9GlDtVQpiowQc4Yrswikgmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇩🇪
#تکمیلی؛ بعد از حذف آلمان از جام جهانی؛ مانوئل نویر گلر 40 ساله ژرمن‌ها رسما اعلام کرد که از بازی های ملی خداحافظی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24681" target="_blank">📅 17:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24680">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESibDmisJKlZ2zyEycqGMW2K333jb-N7lpBKQhkLy5trmW6yFGSF32GgvOjVDYvVJeNwnhzs_Tg3ILjg3fmdlQDAawTZ51pzeSao1mg3oZLGK7_Eui5uZA4xmCmFSBqXp-pa2DYZY_y5SXH-X4Zs3SqxPbAbS_CeN9CkcFkwG4hRbadD2-XIPxeOhbqId05TcolPrWXD6Yi4QeJ9GC3toobkkmIQF6g3n01L3S9N_662qBqLPfhSZwLlxNAB2J_oOrblY9kxZJMcsPLWszT_TuhC30BZfhSSzOk3M3vU9ATgIoybrGzmjXylZyYj5fLgzv3MJV65xOhpxedoHRO-gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مسیر به‌ظاهرآسون تیم‌ملی آرژانتین و لیونل مسی برای رسیدن به فینال جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24680" target="_blank">📅 17:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24679">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9VqGRQQwqWCw7DRSm5IRDFfkVW_AChBdyXlUaxdoVe3uUicRVMB09csv2FibYrSmeQpu63gol2w4fU0bVSY2Yzwbii54G_IibMx6VCsZdEQ6-TDHL8LQ6P7NvLDWsNOG53PzBaGnK-qlJOsmVIITlo4p9gUjDiO0QJDjm9YAD0nfaTX-57-fnNunrK9zuw8SAeNHb8XUEEr35R7xDXt1Rs9AgB5ezni1k-NuCTnlymdvB7f1qGPq00lW4Xr9iK_aWfTzlx4bh9zCksjT7A-HcfeYXeczT7hP2ZEMYn_OE1rd9aqxcR6CcTY_rWyvxlovltOJsDVz1u0eOTEN0-iaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تااینجای‌جام‌جهانی 2026؛ خطرناک‌ترین چیز نه پنالتی بوده، نه وار فقط و فقط یه عکس یادگاری!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24679" target="_blank">📅 16:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24678">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5a1o-ts5-egllzUBeHk_zg0YUrqQ_f51B-vXYjBNF-WZJwREc7u112BhGxTxqvFmwosPrYZe4o_a-APzoVlSWDolwBhviZsmVCp6XoAsP5YkNGpfaZe_S8ob0Gf_C2L9Fuuh1W3vb9tmdzi22DmWioitKt6p_yV4B-cO1KFn1V0HeUuLNRyTNUJYjyY6izFoYVdZMyshzeAsQX6PLRbv1q5st9pE8pULl-Mv3yTas5-FOyMLVZvSJNfQf3BcNaPvRUVrxQYK0vZGSpwGAWpEoejubFCNsOW5QmyFB76msG2eWPsBISiaXUzb1B532VO2ytf2xT1ZhWPSuDClWYIIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بااعلام‌ایجنت دوماگوی دروژدک مهاجم کروات تراکتور؛ قرارداد این‌مهاجم‌گلزن بااین باشگاه به پایان رسید و هم‌اکنون بازیکن‌آزاد بشمار می‌آید. دو باشگاه پرسپولیس و سپاهان به دنبال جذب او هستند.
‼️
اولش دراگان اسکوچیچ باهاش حرف زد... بعدش مدیریت باشگاه سپاهان با…</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24678" target="_blank">📅 16:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24677">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmayYgkO170ckdvm_x-3h8bxi9DgB30vAeRIVswYJftkvIJhQPQx9LQwIlNnB9wA7vww5TI80KHHMwoqhGWD8zwKgXw70BaN-g60z9c9sWJEjIggq-KmPUzY90U-h-IAgIaS6NS_9YgGhzhOggDj-bS1BQTAHEXiFRfrTBziTipv0eq1dWuo3_hjUyoB0utt9BQuJ8N93_FKT0YWz7k54RV4OZWWEEI1eNErHzrdGA3vYVLaTlzO4v__NxXKm6v-uXLmTyxr9W9GeOfJcKNmUHY5L9YulHlEtoTTtngPQkDx0bND-CGmnoD9e7F6cN_M7v9NGL_REUBVBtNfY1ai3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
شش بازی بین آمریکای جنوبی و اروپا در جام جهانی 2026: 5 برد یا صعود تیمهای آمریکای جنوبی. 1برد تیمهای اروپایی. فوتبال اروپا این دوره بد ریده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24677" target="_blank">📅 15:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24676">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUDTzOf3jhg5g3q8R3rxF-ssYHIx9VOswn3pIVdAIuxz2jxqBOi3LDIVulByD7ocmayMR_91oXhLwPp6XEzQiFEiuepZMnFkRu3cO164q7CP1PHxL9i6S3xWmGEjURVXXpWS6V5TOg_4Du85qkdP5-27OJjHl3MvdXs_i-ve11ZWeKg4m8-SVmNENFHBC93jHxmLzXSHys__Fj1jqnbOUbt1CpWURItMWKJRlCHn7kgJwlk58AUJkuZCV9lIi1E-Z6N8w9eph3bCouFedim-rJmEEI6OdF3v7oyY8XtiW8bWQX_L6zQXKyPXnKqhMWhxE4AAq5OM6jpc5LIhUVxwtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛باشگاه تراکتور به‌ سید حسین حسینی اعلام کرده مدیر برنامه هایش روتغییر بدهد با او قراردادی 3 ساله امضا خواهد کرد. پرشورها قصد دارند در صورتیکه علیرضا بیرانوند در این تیم نماند با گلر سابق استقلال قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/24676" target="_blank">📅 15:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24675">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPXUM0H1LHOvjCj-QVpb2elpuebLaE1sBNDT3PJ8vjilp01EYarDHlIWVfBgg7tWfZp76ffXaoOJ9Wu18xvc0uiJYr4Sb7Oo2QmwDZCdOOZxQPiNNVuoL9xdEG-gerwDopc2b4ECcmCxYODDP7GDQP7EWxjT1zqD6GrdgU6RKIHUblqTr5hRZx57mt2FITgDXl_NfcOLRfytkSIhpVoFoAD0JOz-ukFDV0uIIbqwp5dFmdAUdH4pN49USDHQijIOKQ4zgQUaahGClHAIa0RMjmjoypK1NUSw07WJW9MDxCva51yB033SW_ABw3xwJxvF19n-f3HjmS5YrIsDxZiY9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی؛  حذف تلخ و زود هنگام لاله‌ های‌ نارنجی‌ برابر یاران اشرف حکیمی در مراکش در ضربات پنالتی؛ مراکش در دیداری سخت و نفس گیر راهی مرحله بعدی رقابت‌های جام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24675" target="_blank">📅 14:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24674">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Thls_gMFdC63gweVPxD_2sX1WbtNj8XD-CSh5TWC1ncv1Kxy-icMpQx5MwajHun5MCHQovtO4hAkcFkbo633DvW6jQniUgLETJiCoOn2sxC7VvhP1xbuEQzTbba6VIse8VFzOiraCfDjD6hpAdtUFtHVfIgfoR6ud4f3wGuFRAOhO61puWDA-kBKYTPDENCwByksKVnd-aPef1i7SJiqMq7o_H5jV80nnLdLhRmfqDlvPzz_87FrLFgfY9lM2rXtcOYrVk0dpZ3IJJcF4Q0wwn2bT0ES7FUiMCrR743gUa59hgDflRESlmHF1q_jkVZx2XvvxtnkvA3--ELb3T2lPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه تراکتور در روزهای گذشته علاوه بر تمدید قرار داد دانیال اسماعیلی‌ فر؛ قرارداد خلیل زاده به مدت یک‌ فصل و قرار داد محمد نادری رو به مدت دو فصل با پرشورها تمدید کرده‌است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24674" target="_blank">📅 14:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24673">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KK49MlO5GHiXyumBmKVJsFpLV_fNpaHRsGr7LZ8hK-5gNx-PHPPMJXvH9yMJ6FAgJvdz3I03pwWRlOp1OsrTHQyCMbSzHFEMAZ7EU_j6FzXc-f3_jtJFUOGedeYFO4nae7Rm0ee9rBngrMAO71Jcc5LGkWolgxaGRQxJIsKAnQpzOC-LjYWJ8ofQEHx0pRSuGMpH4D1DfiTdpj_llVNCF5fqscD2yB6NaVddRlqgN73B8xH380IfCJ1ji0nItJ7YiADfDx386DHqOolkI968zwsHvJ7eq7SEmjp2E22KG-T1Pg188RzdXhDJ8ykKqeIqhcd_16EkCzn4ao2eg8gO7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌استقلال باید مبلغ 150 هزار دلار نیز به حساب جوئل کوجو بابت فسخ قراردادش واریز کنه تا پرونده این بازیکن به فیفا کشیده نشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24673" target="_blank">📅 14:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24672">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82624c7740.mp4?token=JtZ5ec3peGmiIfOF4Gg3-8IlBjqdQVOtfjUZPM2fvyR14OvkrE_F_21YZsIu7NC8e_uTWe-e4lHDZFPGfJCnHW8ldZqRz7uVoGtxkDmKyq0rXXSr9OYbvCVOUWz1mdLdd3JQEK1ULATlFxFrkBQT4NqI75pnOZQEQ6ynQEPT07CC5xrJD-rVxwcG1Ct6_F5O4WjVS58kXf3S-w74OkclCjGr3X5Vt7cKdLgoEF3D8F83VNdf4LFXhlUcGPIdKqdNOmrFUQVdPPim5X8Ex-H14I-0sgCN27bqF4K-dnSQEYS0JoZthlLhnCL2lZAqnJT1oH8X1aVht6b9MGXrYMlYmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82624c7740.mp4?token=JtZ5ec3peGmiIfOF4Gg3-8IlBjqdQVOtfjUZPM2fvyR14OvkrE_F_21YZsIu7NC8e_uTWe-e4lHDZFPGfJCnHW8ldZqRz7uVoGtxkDmKyq0rXXSr9OYbvCVOUWz1mdLdd3JQEK1ULATlFxFrkBQT4NqI75pnOZQEQ6ynQEPT07CC5xrJD-rVxwcG1Ct6_F5O4WjVS58kXf3S-w74OkclCjGr3X5Vt7cKdLgoEF3D8F83VNdf4LFXhlUcGPIdKqdNOmrFUQVdPPim5X8Ex-H14I-0sgCN27bqF4K-dnSQEYS0JoZthlLhnCL2lZAqnJT1oH8X1aVht6b9MGXrYMlYmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
میثاقی ژاپنی که بعنوان بهترین تیم اسیا اونم نه مقابل هرتیمی مثل‌نیوزیلند و مصر، بلکه مقابل برزیل پرافتخار ترین تیم جام‌ جهانی حذف شد رو مسخره میکنه؛ جوری میگه منتظر 2050 باشین اینا میخوان قهرمان‌جهان‌بشن انگارخودمون‌خیلی‌وضعمون خوبه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24672" target="_blank">📅 13:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24671">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/knGcUrUIgJhsms9-xYzq9jznnNeLQqsEjVMakq-41rKxYBSImkca8kXM1lvtC3ZSei-xeuzgGV_6Efb8iT3q3E571Nb2TTSt8WwCSDqbusZP1ZhzNRrXEbWN73R8s_zkauK5XuLzJ10JsxpyJClJZ2LgFbH8tRgHk3RtZd8PkYZ8NTKYAxVqr2srlPZmuwD3YeMpoyPKf2AZKbM3rYUQa5Zz_JqRYLAyJQdiA_Lsm3hrhZOlJobNnovqaQ0TUqlB7Z4cIWPfXRLd5E1BlXiOex31NrRb7JNy1Jnn6GiPm8cRPMwZie6Yo8YO8VaTVhuEYJ-OUk9AFTQGXa5zUxoERA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنهابازی‌مهم‌امروز؛ گذر شاگردان آنجلوتی از سد سامورایی‌ها با گل نجات‌بخش مارتینلی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24671" target="_blank">📅 13:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24670">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ze3-4O1Ilz7mIBoJRXoo0ngvC6vzBBbJXzuc5P0VOSQB1fGxGZHvbfLJ4Rra6ZV6_p2OC_vjiWAXjt2s2ifNKYcShZEdhh8UyB-843OyKABXNlLrb9RrOs-NbZW0SV6pz2dWmA9DPdzmig3d26FWkAfDUO7flBgxMUZ4ermNFjkQPq_waFBKBVb765VnY2rSvg28JVyE7ftwpFG_ZIrxGyVvwqieE_WlENxL7nONZiaSZP77xe0vdGnG23OaQecMLZxAtCr705QpdmsEM-Q82IzrCZWG3UZd0eTGVDoi4vy2hZbKKIC5ErkS5zo7MJjXCh9drDq-dkCgnwFstaGCrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24670" target="_blank">📅 12:44 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24669" target="_blank">📅 12:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24668">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/786ffe7041.mp4?token=b7WI_-PVsMo1gWEEUBWFReN_kuzsWU6wKTN31oPqx58qpOs5_ExYgqax44-NKlsfaPr1PWSgjhKxxbEPgEW6bDFaBm_o-USAMGlV8J4Z_kU-1ZH_gjzfe6VCGtvcqYyUYAx_zIzHAEsVINqU7jC-lEqSB86xtFkYgSLHHJaU_8QjliOBfJIq23dC3mDuXsZnG5dUY_Y5Ofu-UyzirhaNJBS6M9RPv3tIZX-WefkNdMyU3P2r9TaF--MKY8qN4stI1sIVrkPh1Q0ZpURUPrQHVOiw-flJL47nrajfX0_bbtD1QWqP6N0jcOnAWN81INOxZGcmCA3es1TK3aUwYuFxng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/786ffe7041.mp4?token=b7WI_-PVsMo1gWEEUBWFReN_kuzsWU6wKTN31oPqx58qpOs5_ExYgqax44-NKlsfaPr1PWSgjhKxxbEPgEW6bDFaBm_o-USAMGlV8J4Z_kU-1ZH_gjzfe6VCGtvcqYyUYAx_zIzHAEsVINqU7jC-lEqSB86xtFkYgSLHHJaU_8QjliOBfJIq23dC3mDuXsZnG5dUY_Y5Ofu-UyzirhaNJBS6M9RPv3tIZX-WefkNdMyU3P2r9TaF--MKY8qN4stI1sIVrkPh1Q0ZpURUPrQHVOiw-flJL47nrajfX0_bbtD1QWqP6N0jcOnAWN81INOxZGcmCA3es1TK3aUwYuFxng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی درگفتگو با ESPN گفته شک ندارم که آرژانتین باتموم‌ ستاره‌هاش مقابل کیپ ورد غافل‌گیرمیشه و خیلی‌زود از جام 2026 کنار میره!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24668" target="_blank">📅 11:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24667">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d5676f715.mp4?token=QmP0kjX7aTvcTtEbrHEFkQQvORtze38UMNY2f5punq9PlJs7-mR-85isNFM4DCfOHjKChY5mS82KtE_7riyTO_67v7Q_sCbd4sUfRqZLOzjS7xv4jWzG52hzOxBVLBvA6l9TGZPnDHCxGphn8ag8E2H08q1uWk0Uv2degXjZ151KIDYT1rkZnuP1zA4ztLA2qNvKJ6WLWGIHwZBBXYcCx7yFd_HX0fZICYsFV8_ANoePaJFBkJMM5XtMS2-tina77xqSVh9JV4wbYM0UKc8u-9wmh7k6986jD7gQxYI73_WVYySoxEqu19_x5V-jdAqbufsG2MVkCGIX1Vb7jaH6ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d5676f715.mp4?token=QmP0kjX7aTvcTtEbrHEFkQQvORtze38UMNY2f5punq9PlJs7-mR-85isNFM4DCfOHjKChY5mS82KtE_7riyTO_67v7Q_sCbd4sUfRqZLOzjS7xv4jWzG52hzOxBVLBvA6l9TGZPnDHCxGphn8ag8E2H08q1uWk0Uv2degXjZ151KIDYT1rkZnuP1zA4ztLA2qNvKJ6WLWGIHwZBBXYcCx7yFd_HX0fZICYsFV8_ANoePaJFBkJMM5XtMS2-tina77xqSVh9JV4wbYM0UKc8u-9wmh7k6986jD7gQxYI73_WVYySoxEqu19_x5V-jdAqbufsG2MVkCGIX1Vb7jaH6ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداگذاری‌باورنکردنی جوادخیابانی مجری ویژه برنامه جام جهانی روی آرناتوویچ و خداداد عزیزی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24667" target="_blank">📅 11:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24666">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nf7b-DxR5HYJEaWdIZqRwCZjPApJ41C1qJ7-3_u8Ro2auGc9G-hinu-9DiZO5v9qsLqH4QG6bkv4CQ_k0RnaBeCgdgIkHzaYKc_tSc61hiWGTG2LVjcEJoTgsyWytL150pva2VtRHhRjV08-yrTulsgiMwoy98n7vw5zRagHDb582PiCtrpEDYQ_XEt_C39H_uDDq_XmoTJbVXU2m-6itM_Z9Dd_ocb8Y3EK8Sj2vBjky5AYHF97uE3OJRxpCuBkn0a2PJmV_poZENhhyapPqXWUWXGtQDFJT_hTmMXdkLPnEGizwL0JEwADTF_jMoBYI4LNcxx3HZkpYNkt8Q0SvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه‌پرشیانا؛
به احتمال فراوان باشگاه استاندارد لیژ قرارداد دنیس اکرت مهاجم 28 ساله خود را فسخ خواهد کرد و این مهاجم ایرانی الاصل احتمالا به لیگ برتر ایران خواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24666" target="_blank">📅 11:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24665">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThwHG1y9Xp9waHzyn5nccPA0l-3Yrppt3zqvUhb93yrtreVpZnBvaB-GC4KJxqIKxM4MDzOmOv_1u73sJLT5r8rj0EywN3am4vJCLoZInUrlVkloiqLP8eRT63dfNizLCz6vq7scApPqwC2U93poDb5rmo5eXR4e86QWX50CwAv4qlYGmc2whhaUIX6xxI0oCkdmnjY_IqCRCFn7fmxon0-Ss51IgM64kLZYZLITk0xYegctBKFb1LoXO5xj4mz1va0ydIeupWLW9fEoaxy3FGiRUmrpoUgIGSS9Nk67RQctWJ8fcmySGMnWvB66D7w95hb5hkxbm0G1cynwGyBO3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک شانزدهم نهایی جام جهانی 2026؛ صعود ارزشمند و شیرین کانادا به یک‌هشتم نهایی رقابت‌ها باپیروزی دیر هنگام و سخت مقابل آفریقای جنوبی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24665" target="_blank">📅 11:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24663">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pC_3cw1GzWxjb38D2ACa0MuJdRnK5jYhZMt3WZjEBhQtje4oo3xiPXOhLw61slsPFWQEmxqBzycT2mJTsc6MwaIVR_3nAtVi4IhKpxDgBNbuOYjojXojx7ALSxLniAsopFTiE1t7yV59jJobL0LqeWpnbpEygMDqOBkxkRqOUNhUmuaFfLny4cyZUyfflOgqetppjPgqeSuXX2K1RvzV6AmivEL_Oj8lRrXVWZUCtQ8HIHLjSGE1TYAcpMuZkVzBz47M4yB65TgUgegoYTtBMPMTOL_hpZt6c1y_v6V9Kmjd2t1nwhEbs8otzC8Fd_kj4uX9YoN7HfS1NvbX09CXIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ باشگاه پرسپولیس درتلاشه امروز برای دراگان اسکوچیچ بلیط‌تهیه‌کنه و این سرمربی کروات ظرف 48 ساعت‌آینده با دستیارانش وارد تهران شود.
‼️
بعد از رونمایی‌ از سنگ‌ اندازی این مدت بازیکن کهنه‌کارباندباز سرخپوشان‌پایتخت خواهیم گفت. این بازیکن از وقتی فهمید…</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24663" target="_blank">📅 10:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24661">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/572d6647db.mp4?token=oxCtH6vJ1-x5jB0l8TAp_CTFtj44tN_Flj13023wZCn6jr-tHs8D-G2iZaAw0sb8dJ1N2WVI9nVcJUvs4rgdYWV3nZB3pcI1SLfhiNdKihZbIOKS5Xzl9Mgk9PMmmo6Aw-BlpvGPx81d9ubXA8LggvbUvMW0-6u8v6AtLvg1p8210VKwB2-fB0SsRjZ7-2qnIfFq4O2Ca8Xom4gG9JG7NfI17Fvd6KTwcq-hCLmc4ooADIw7BtH_snUV2E95Cm1F7vNsPL3AwEb4nBhy9prQ2HRvPdUb0iwCCHboWzvxCxR68kRmgKWlEv0Ddz1EoGvvMk3ieiTqg6phtnobQfdFuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/572d6647db.mp4?token=oxCtH6vJ1-x5jB0l8TAp_CTFtj44tN_Flj13023wZCn6jr-tHs8D-G2iZaAw0sb8dJ1N2WVI9nVcJUvs4rgdYWV3nZB3pcI1SLfhiNdKihZbIOKS5Xzl9Mgk9PMmmo6Aw-BlpvGPx81d9ubXA8LggvbUvMW0-6u8v6AtLvg1p8210VKwB2-fB0SsRjZ7-2qnIfFq4O2Ca8Xom4gG9JG7NfI17Fvd6KTwcq-hCLmc4ooADIw7BtH_snUV2E95Cm1F7vNsPL3AwEb4nBhy9prQ2HRvPdUb0iwCCHboWzvxCxR68kRmgKWlEv0Ddz1EoGvvMk3ieiTqg6phtnobQfdFuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
صحبت‌ها و عذرخواهی هاجیمه موریاسو پس از حذف ژاپن مقابل برزیل بدون بهونه اوردن و گیر دادن به زمین و زمان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24661" target="_blank">📅 09:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24660">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/feHlFOKsccZquDKl8ImOWbpShoN_znE7EmZR6imKC-6qwy4PQTb3vXilP3_fyYnGMf4Kl-nPPeI22abjhwXAF-cU35ZzDqUVcSw4FxkwquPmFcNPrmPHHvxwj92_DCG8DSo7qoYHP3yX6xqd5KsZk9ce0q6MFWQiRwvy9FyGQBi8n9uBDkVx2BRKx_PwI_NUIAqk9n3jK_0y6G2eHdksJkYNGdLUinw4ZAHRJ59pCS0W1hVgFmtFkEF_G4URXWQ5nNSHlcAc1eaGmucMSBGiOvZ5_ZmiXLh7yVGW5AARQ_8_3hd5ckjD9zdFLzP70z9BI3C6Esjkxv-1U6oBwXtD6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
سه‌فینال‌آینده‌جام‌جهانی فوتبال در این ورزشگاه ها برگزار خواهد شد؛ کدام ورزشگاه باشکوه‌تره؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24660" target="_blank">📅 09:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24659">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی؛  حذف تلخ و زود هنگام لاله‌ های‌ نارنجی‌ برابر یاران اشرف حکیمی در مراکش در ضربات پنالتی؛ مراکش در دیداری سخت و نفس گیر راهی مرحله بعدی رقابت‌های جام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24659" target="_blank">📅 08:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24658">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oC12Frofh8bwInUtdjuAQG5UrHGSO8olYIPd87-NkcE8YI5O8ILewCiZOOYc0ZRyYcH5QJPi7FIB1qlJtbtl8ZgoGhzPAPS9WXv35tI3pV-Y1UurYOfICihDMojuKbfnRuoTjToVtaNmvxJvsvmvgkaTTQOIl33v1VQUh6CrSsJJMznNAHiOBk-aThNRzF7x0KhZqUlxqDCQnnKOUQFuLTgeeL03S_xCoWo8WPagmL-pv-3HAEKT2DQh7_MgwKcyGgJ8nRoeTQ7VKM7aEX8dtEElKoUrr5MslOIFqtyl91ct6gDasmQ3xgiDFiENGHccV15dLD0kilDTTNhhzpmbYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی؛  حذف تلخ و زود هنگام لاله‌ های‌ نارنجی‌ برابر یاران اشرف حکیمی در مراکش در ضربات پنالتی؛ مراکش در دیداری سخت و نفس گیر راهی مرحله بعدی رقابت‌های جام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24658" target="_blank">📅 08:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24657">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZKIAB5XB3SNyINcmIyKPWrm9dlyvSWfEP46m7qXnZGYl9_ZhWcXZxT11pXjMS_F8AfAX1-oNkgZiiTYoPtA-txsJYY1qHp34yfFoXFnQen_QbEgguoy-LSIEUgcPzrx-1FijqsM3Z_Rt_M9QRBENus0mqcJpQ0ch7EZzQzun8Mge5xWPxH2r2cJTYEBU0R8scFsqWeNt-2Y5uljsxdH8mSTNTa2g-QR3I7kyQr80J1Zq5AqmxjVHsYZyqgLNV7S4ev2G0NT5ohd6iCtAJtQN4FAnpMW5xAs5O9NsmnVBohWi5aJl2vaShuafUnaY72R63c-I5PKp-lhD3ibtpqZqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی جام جهانی بعد از صعود برزیل و پاراگوئه به مرحله یک هشتم نهایی جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24657" target="_blank">📅 08:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24656">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56f71a194a.mp4?token=v7RqjOxzervAeWLnt9eUD-PS_cE_dmDTD3KdlRC2R4ma5Cduv5QKBtKeuEfR_L3DaExluuCPYswXCBjU3BrRB874nlBpwoePb0XMtj0XC_TVMxCwbXlZ-49WUTXAuUNgeScTGOjkPikP4UGKtGBP-Evb1HwvBU3U5xMOYHzT2M6c0Lo-kxEGExzuiemGZY4dxVbRElMMWJUeC1gGk1eCXerwyed1Y-X6L-fJeblDdsjLWGh45nvn2gCS0q_jMru-vgoHXBp0IWIxdnZy_AfofX49-9uUZNLnj_jvKQJIIM6bvG9YYTf7yZcdkHnORLEThZtQ46ddWq_QnWL_hY3V84HkcfCVSmFlMvKb4FtYyO0FTLD-wJVd6UNQH7jam7WuZ1WBriXvgTchDB3RTzTWxji_WuE1yHsLs3u3GK4GedKAHaxgluNRiVoUbRh98nxCuNDqVqsHvUR3KI2pP5cKAkaK1yt9A0u06GVw4sPph3PmrTQGQOScC6vAizUMfvygZx6IwhNEI32dZq9c2kCG8et20KjyHgIQkBUcV33nHR3OYJ-KUFbZprK1ceXvS9KN_R4poFMqg_4yvA7p1CDYhu_mD-Yx5MnJ6vpdmlitwwe6EW6877Mo6E_bo8Rr8ZOBPINCOcTeH2aMNDNlnwcmopm6mZ-v9lQ6RIQjiXn2RB8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56f71a194a.mp4?token=v7RqjOxzervAeWLnt9eUD-PS_cE_dmDTD3KdlRC2R4ma5Cduv5QKBtKeuEfR_L3DaExluuCPYswXCBjU3BrRB874nlBpwoePb0XMtj0XC_TVMxCwbXlZ-49WUTXAuUNgeScTGOjkPikP4UGKtGBP-Evb1HwvBU3U5xMOYHzT2M6c0Lo-kxEGExzuiemGZY4dxVbRElMMWJUeC1gGk1eCXerwyed1Y-X6L-fJeblDdsjLWGh45nvn2gCS0q_jMru-vgoHXBp0IWIxdnZy_AfofX49-9uUZNLnj_jvKQJIIM6bvG9YYTf7yZcdkHnORLEThZtQ46ddWq_QnWL_hY3V84HkcfCVSmFlMvKb4FtYyO0FTLD-wJVd6UNQH7jam7WuZ1WBriXvgTchDB3RTzTWxji_WuE1yHsLs3u3GK4GedKAHaxgluNRiVoUbRh98nxCuNDqVqsHvUR3KI2pP5cKAkaK1yt9A0u06GVw4sPph3PmrTQGQOScC6vAizUMfvygZx6IwhNEI32dZq9c2kCG8et20KjyHgIQkBUcV33nHR3OYJ-KUFbZprK1ceXvS9KN_R4poFMqg_4yvA7p1CDYhu_mD-Yx5MnJ6vpdmlitwwe6EW6877Mo6E_bo8Rr8ZOBPINCOcTeH2aMNDNlnwcmopm6mZ-v9lQ6RIQjiXn2RB8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24656" target="_blank">📅 03:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24655">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14530aa1d.mp4?token=r-QEburi0jArQhRkAo1_KThTAxM28ey7lKhoRuow9VmgLJImTlAat9H3qPZU1eRT-d1XCKMUBxMwlyhgjAUlUZf_Yq9NN4gspLPTSfJziPcaOek6ll_ISdsHQ7cBZmAtbQmaj7Z2E61BfqM1oCNPqNYmvaQ38fBYpIQ9hUfyGBegJKQ_nizdd_36JwMcnNUlkKKSRLwpoMYN_uEzQ4c1yP64v91sTDT9HwGtQ18WWBRLFo1xVf6sKHoYP25wrcYU-rjvtibpio6LhLt5Mcg0CpsMu4xNL0lbL6shQdiKgxXC1RhS1jfWqON82ooUNvHWo1q0NpXZxYcMHQjEf2nDPG6wtFVfRSWFBsbw6DvafXoOmD-Fvn1AENmmqb5y2vznb8DGHgevFsZOusoyZenkZ39VTX3BMa5Kf-kIfljicO8ETjij6_e23PATQOBPCUqv3jLL-o86G8DM2_yp-prWLWJwNHhgvot59dbbya18gE5HRol8SSUwVBfeeFAoZtHgscs2DcPwsD7TmuNU7cnkvFo9DQaJi06pdyY4XDM7X9YJQ6Ln3LkKJwG00dmpV7KN8MvVmpSYURtj48dJbq1cy2kCUimfHsXzsbZPwUyENWkFPuqMqmH6-FrESuTsyn_b3pudBcr-uFH-tmIv_nmfTRkpEDTmxvdVhpgpm88oOnI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14530aa1d.mp4?token=r-QEburi0jArQhRkAo1_KThTAxM28ey7lKhoRuow9VmgLJImTlAat9H3qPZU1eRT-d1XCKMUBxMwlyhgjAUlUZf_Yq9NN4gspLPTSfJziPcaOek6ll_ISdsHQ7cBZmAtbQmaj7Z2E61BfqM1oCNPqNYmvaQ38fBYpIQ9hUfyGBegJKQ_nizdd_36JwMcnNUlkKKSRLwpoMYN_uEzQ4c1yP64v91sTDT9HwGtQ18WWBRLFo1xVf6sKHoYP25wrcYU-rjvtibpio6LhLt5Mcg0CpsMu4xNL0lbL6shQdiKgxXC1RhS1jfWqON82ooUNvHWo1q0NpXZxYcMHQjEf2nDPG6wtFVfRSWFBsbw6DvafXoOmD-Fvn1AENmmqb5y2vznb8DGHgevFsZOusoyZenkZ39VTX3BMa5Kf-kIfljicO8ETjij6_e23PATQOBPCUqv3jLL-o86G8DM2_yp-prWLWJwNHhgvot59dbbya18gE5HRol8SSUwVBfeeFAoZtHgscs2DcPwsD7TmuNU7cnkvFo9DQaJi06pdyY4XDM7X9YJQ6Ln3LkKJwG00dmpV7KN8MvVmpSYURtj48dJbq1cy2kCUimfHsXzsbZPwUyENWkFPuqMqmH6-FrESuTsyn_b3pudBcr-uFH-tmIv_nmfTRkpEDTmxvdVhpgpm88oOnI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24655" target="_blank">📅 03:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24654">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fms7kjNl8PCb87-X7cIcCXaS3k_go8mnD23QPaNOFBd_2dleHWufDE4tU0YCmNfRUQBg_Dq5NsNHCsFsNw58guXDrRAbfLTXGnkx1MEjbQ6Dx9B7E746UOYkbEZh8tp2F2Wz07MAFFqDKYIN87ODc6E6n7Y7aqqPAi9OTEe1K8rgUWO4X3C_Jz2qwjjuc43uHmDd2yT_1KVwrVqNjiLS-FGcSCAqbK8WZ97OZLc2dF6llI2zCf2VyONMAM1SFU_h8flMR36Q9SwE4R1tHHAvKr3_iHMimYxinniuMffbNKPGPtc-LTOacI-mJPINBUd1Yw1wtQV3ZmmnU0A5btYoSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24654" target="_blank">📅 03:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24653">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef2bb58ba6.mp4?token=CyjpCaMntPiNazDwrFVzD9Ps45652XFz3v4hSQCPlpMiIjzfJCxFWlbJGNiTfKTN1HD0BP5tD6hBjcLBQFFaXqIUBG9CVuVZVIqe-bHjtNS7ioV7MbA1YrWHDjcUoRlRNbUb5b5hDPmXnfM7YZgIvEBSpfDHn6qFyzOahRVKmToZiuggNAThIyCIOX4wz_nvRRnN7AvU6LThk-xup3EM4h-Q8Fvc3r9_Alcfr1QH94KHI4JUBIri2hN02SDk1twaQS5knIMUIOf9mp5L2QYu5kJja8NGJiXSJWe5hEJ4fAgE4EQUKZaCEhiqUH6tF4ykVY4KpC6-MM53wcqgyvZ7fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef2bb58ba6.mp4?token=CyjpCaMntPiNazDwrFVzD9Ps45652XFz3v4hSQCPlpMiIjzfJCxFWlbJGNiTfKTN1HD0BP5tD6hBjcLBQFFaXqIUBG9CVuVZVIqe-bHjtNS7ioV7MbA1YrWHDjcUoRlRNbUb5b5hDPmXnfM7YZgIvEBSpfDHn6qFyzOahRVKmToZiuggNAThIyCIOX4wz_nvRRnN7AvU6LThk-xup3EM4h-Q8Fvc3r9_Alcfr1QH94KHI4JUBIri2hN02SDk1twaQS5knIMUIOf9mp5L2QYu5kJja8NGJiXSJWe5hEJ4fAgE4EQUKZaCEhiqUH6tF4ykVY4KpC6-MM53wcqgyvZ7fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هالک‌ایرانی‌درگفتگوباابوطالب‌حسینی:
شمشیر خوردم و مانع کشته شدن یه بنده خدایی شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24653" target="_blank">📅 03:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24652">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6cQrOGYMpKE-x2EYr3BTW3f3PjotCb6hltzDcz_slRLvywvel8XShpY8KnPXdU8j3lT1n-LczxxKxynmYSaQkzpCHeKvXiaDbqrQR_pEVBdoVjUEKQgbFh223SkXZfIipouEbfeMczF12HHj7Nbguz9cwRlW7YbaTpGXDhk3zUHLk0D6S-sq8J2cnvM08B1ibscSOmPUfteJtxUzjrW-qj1rpnhHeHpu-UdjJLQVjahUzN1JQUfeK2bty-302qh_Y8mb7AIQpNJ_DIN4T05TlAA4MMsXHSwDJI_dem7rrhIdvy8w0es09T5qZ-mzujWNR5oKwh6f1e_kuijb0PUiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24652" target="_blank">📅 03:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24651">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdXRF2_L59Gm4g99WxvUfIXtLyS6q9rSk9zWmJK-g5_AoaND1NC0a9eURmmwSfq4VmEhrzQd5AimXG1Y7y25rA7qbrP3VrXGabyL-xAYz8VP_mrWoj_TcJijWRjEMDD4CdDIrEW8N3B9x6ECSPvAbnKh9qyBmbfgpGRRvLUbxmQlWzfI63y4zTnlECNbr8X4RpKArwOuifyfzK4YFD24jPfEH_wh6QK5ZqFRlnGeGKjzKIdYSk0FFKNBQpG1S2W_UaEbWTYOIj7679KVNHHQx4cqxzBUqXDmnO3Kv00AjvDFoIugDYUYHQNEqJApKOQLmL-JDSrxSYbjWwcwtwTmyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آلمان‌امشب‌از پاراگوئه‌گل‌خورد؛ آخرین کلین‌شیت نویر و آلمان توجام‌جهانی‌برمیگرده به فینال 2014:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24651" target="_blank">📅 02:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24650">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8d0fcfa32.mp4?token=uPyusF91Rvx2huia4DU8PNl_eMU_aQ_SHBVxQzk18TQbgFpNy8xtriWizuy8cpHhQpBminB0cUpxy0Zl8zwY1yviXk5TCobjVkTsRLrN_qJjoO3x42fhB4YnFZ9JV5805BNaAxO_WOcmsdcd6hW0Hnbi3LwkThq64IMv796_MMBBeHoqMPPXBRdx0D_7ZxPndzzbhoTz-aaibuRMZg6poX6B2FQeEMVTyF1mdFmkOer6GeQbSeYV2bITWZI_Dfi9MLWzNwenKKJNctVJ05BWhP0Z1-1mKRpLx9IzszPvWP_w6JAmLsB1qcddazWJBa56M3tMFpLDkDA25k18Qo39aUicwfWHGlYYozb2yk4eeU0IoAKGEJ9J3_fAmYqQlKNR1TscNmQqdwHpHv4JSvTfsJWi_YgdBhDw-bSHcIWOb7SjK3OJn3ADQPuZ58sLGvPWvs7-4SVuJqoOquGTylRMYivQU0Xrw2uBEYLqHC2S3PeWjZQ4Mc_QrG-c9XGr9qFHlW70MdxNcx8TmG0aBh4PyALZm0Nb9_CCOZpGFxSbO42j-BcMZBAEvQBLqjodxlo1flBHZdtHTOUcSFkf4oaX28uIXZxLNUDO00MPvFjRdofCGBKSUnoISEKt66EUzUPIlBX3aRwxBtP9lIJasWM-cxEKA-QHAphuG49dFX9oeKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8d0fcfa32.mp4?token=uPyusF91Rvx2huia4DU8PNl_eMU_aQ_SHBVxQzk18TQbgFpNy8xtriWizuy8cpHhQpBminB0cUpxy0Zl8zwY1yviXk5TCobjVkTsRLrN_qJjoO3x42fhB4YnFZ9JV5805BNaAxO_WOcmsdcd6hW0Hnbi3LwkThq64IMv796_MMBBeHoqMPPXBRdx0D_7ZxPndzzbhoTz-aaibuRMZg6poX6B2FQeEMVTyF1mdFmkOer6GeQbSeYV2bITWZI_Dfi9MLWzNwenKKJNctVJ05BWhP0Z1-1mKRpLx9IzszPvWP_w6JAmLsB1qcddazWJBa56M3tMFpLDkDA25k18Qo39aUicwfWHGlYYozb2yk4eeU0IoAKGEJ9J3_fAmYqQlKNR1TscNmQqdwHpHv4JSvTfsJWi_YgdBhDw-bSHcIWOb7SjK3OJn3ADQPuZ58sLGvPWvs7-4SVuJqoOquGTylRMYivQU0Xrw2uBEYLqHC2S3PeWjZQ4Mc_QrG-c9XGr9qFHlW70MdxNcx8TmG0aBh4PyALZm0Nb9_CCOZpGFxSbO42j-BcMZBAEvQBLqjodxlo1flBHZdtHTOUcSFkf4oaX28uIXZxLNUDO00MPvFjRdofCGBKSUnoISEKt66EUzUPIlBX3aRwxBtP9lIJasWM-cxEKA-QHAphuG49dFX9oeKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
👤
صحبت های عادل فردوسی پور در تعریف و تمجیداز رامین‌رضاییان‌ ستاره36ساله فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24650" target="_blank">📅 02:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24648">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3a278b0.mp4?token=v194M8z3Klil487_w3AY33hYhG3EF6Xlalvk0m3abg8hDx_jCO_KwpDHUc7H7LKD1-jjW-l5Hi0Di7Grp1W0-2hKOm9FNlnBoyXiCkinr3szPjoeENqNR7kXpmGUy223icBiaZTVRqLmVmuqIPs8DD8koIkRkOGQ0Kr4P23yS17afGIzhwHRKlXY_dYbmuCEpHUPYu7_JofkLopcHLOY7d5FFsPV3tlPf7sxabapJPwdzle6n2w3VsK1E0GnpDdqZaoJIvQuWF_mbcj3S61Q53QHNqfkX0ojthpi89rOM6pMRajPJvsM3PCSxGvc88A3kKA2Y_bBYrofQOI0QFQgaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3a278b0.mp4?token=v194M8z3Klil487_w3AY33hYhG3EF6Xlalvk0m3abg8hDx_jCO_KwpDHUc7H7LKD1-jjW-l5Hi0Di7Grp1W0-2hKOm9FNlnBoyXiCkinr3szPjoeENqNR7kXpmGUy223icBiaZTVRqLmVmuqIPs8DD8koIkRkOGQ0Kr4P23yS17afGIzhwHRKlXY_dYbmuCEpHUPYu7_JofkLopcHLOY7d5FFsPV3tlPf7sxabapJPwdzle6n2w3VsK1E0GnpDdqZaoJIvQuWF_mbcj3S61Q53QHNqfkX0ojthpi89rOM6pMRajPJvsM3PCSxGvc88A3kKA2Y_bBYrofQOI0QFQgaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
اینطوری که پیش میره مکزیک سال بعد یه افزایش جمعیت چشم گیر رو خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24648" target="_blank">📅 02:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24647">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBRJV0UsnIwxIg-2N_SpocWMTWloJMhUz9psPD5GTzhucnmqxd5QRUFl_SlfxrxeYbZbc-3zgLHjvPwCFvSBRus0fZKlxPFCWDpJQTVkhYIZxq5Pt29UzO-ffHyOBFKurN5LVgeSI5D9OUjyL_nrCtJDbVea_txojX-6tL7np6J1dPmVxO8ofyS8qqXjjVl0RPk4SBr34blSrMHzwga5xf9aD0M0Ozc0gmYdbw8nf89osmVewMY4yIwZzXytpuvRghAKmiTmHQAqW2ZJjPT7Lqo_E02XtHKtDzy7t1nzWZB5lDB-VYYC_eMmwjA8ZL66bAjjzzQ0Pi-SWlYXN06bBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جواد آقایی‌پور مهاجم‌سپاهان:مردم عزیز اگه تو رشت هستید و نیاز به کمک ضروری دارید به من پیام بدید، کاری از دستم بر بیاد براتون انجام میدم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24647" target="_blank">📅 02:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24646">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‼️
بازیکنان چادرملو به لیدری رضا میرزایی وینگر این‌تیم سرود قهرمانی این تیم تو آسیا رو خوندند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24646" target="_blank">📅 02:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24644">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SreSWGt81gJauBUgxgV0zYCB9L09eFgWlTp560LzEvZvjxs8Jk7vKszoiblDviAMVNy05vr41EVfVfKfnxN2wWPGUnWRer1UcSvdVxhM04OstmocEQOOtvQ01ouGhVkeLV-LZ2St7_sJJwSHOI8cgtLrYCFnvhryz-cp8k-pys_zO3LrznRtBPGuEfgRFThFCC2uHuZD9BsYuR4JDCASDZtTkcL4C0pbL_p4x6AIRubpgAV34SktoNPB-5wSOwt8RqDPzYnvZObZqYXxiwsdpCGme4yKFUALqkDyFsZAovKSPK5fTq9sf8Qxu-JUcvxY8opNRkVW2-RCI5UL3-QR4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#فکت؛ علیرضا بیرانوند تو جام جهانی 2026 :1 کلین شیت نویر تو جام جهانی 2026 :‌ 0 کلین شیت
‼️
تعداد کلین‌شیت درسه‌جام‌جهانی اخیر: بیرانوند دو کلین شیت داشته. مانویل نویر - 0 کلین شیت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24644" target="_blank">📅 01:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24643">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7FaxHMDaP6NeRyt-LfT91MPwxeGmhFui8zSSLjHQwuWNAwC2lpT8u0hCHLHpfG93EW7hww9aFTpILJF4S8LC_3PGAsbPUB0R1ifopTFKwI5_M_LAwWPiGZEWV2HeE9n_nHUwdMrSOBoVij4fEx3whLjovCejPBiyl6vB7qtUAanOuHO4CqwOa45B5DGgv-rskg17mugYmSYkW1H511-0kHKyW8m4cZ5zj7A1OSEMa3sso_mOhVLI3zJkDecFp9a_1fmAEsLKIdifjLV2KzqLEwnMH8vyxFKXRfdfc6LEc23jw64sVDBdkVdO7PTdxyBR00i0VODQvxBkCoNV3vXww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24643" target="_blank">📅 00:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24642">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1_je-zTgsgMm_pqnf1gE6jl-pkzTCjMMcY_YrWklXNUnumXGQFu2ROLjX4UeruPC7JFCej5abDn6ROrAcvLHE9TP6j3FaSxAnKsoOqAmvU5mwoHM4A-L-cfN-M0seuYDibbkBTv9ZYkjIDpdumkOxfjONOXapKeK3k3zyZRJnA9_83f17KOOgYUJcZDCyS1woyN8yxbNzh2V2HKDG7BZLHaxKTgroO4ar22ZbnGj6YE8WUpL0Ycui_EAvKFXJMhOoXsYU1J75ptishTG3d1Ntna6yp99ArFrcY0i6E8Y9cnzvKSana6G4t1EdqFJC6vv1bo2EMV8sMq0s4Smh3ApA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-mQWAGffHIXm2rZWnTKsvcgaP9kF3lwgFkb7sh8zXw09HawKx-pWshMFcrmo7h6wowpmLH3qJ_FxT-hSpEqgjbFPO42njx3uEtyGel_1OK0UPHCfnX3-TbiK8MJgupB1rhLfKSGn-XgJd4O5e83n3Ku_J4TMw8ESuADWvvpCZEIhPpkVEEAQlSf1PhoPQvQSYaoztG1nNWmZ6ukXnSskpOh1K2dmavKPFYMpUiiwlH2Mup7Z6HYFHoAvgSS92gcQrmtKpmsr-XH26N-0m7d36HGNDoxRddTYP_lkCfNYYWCJJktKSlFOzE8Wfb6vYQINEzMomsnVMdphGkLANAOng.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d09c7fb1ae.mp4?token=H7yvrNRDK38i4dY8mLOn7TlX6kcT-fSIT-hyL3c4b_j5QnwI2tyR1Hj2GWu8eFGNj8wpicZ2FhTyb1rq5q9P9T__ZILuzu8W1Hg3e4FxX39noEHTmWXlS_MtXiJVdUw-jlVVP6x-LtZs5hBw3s0tUmyVaFpT1v2unlQ4JenuM2eITW3hJOHvH5uX9rzNpjQQ1DRU9VVawRIt_1zc819CAVFmgMDlJyRS97gssTnBlldDEPibeZ54kKXbt2Yd8ncZ4R0jZbd_P26rYewWzxMqFzD7JtDugEL7ef_7to5pYm1tivU6C-meRVBLQMWszXv-0x7w0CPemf5jYybD2_TY2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d09c7fb1ae.mp4?token=H7yvrNRDK38i4dY8mLOn7TlX6kcT-fSIT-hyL3c4b_j5QnwI2tyR1Hj2GWu8eFGNj8wpicZ2FhTyb1rq5q9P9T__ZILuzu8W1Hg3e4FxX39noEHTmWXlS_MtXiJVdUw-jlVVP6x-LtZs5hBw3s0tUmyVaFpT1v2unlQ4JenuM2eITW3hJOHvH5uX9rzNpjQQ1DRU9VVawRIt_1zc819CAVFmgMDlJyRS97gssTnBlldDEPibeZ54kKXbt2Yd8ncZ4R0jZbd_P26rYewWzxMqFzD7JtDugEL7ef_7to5pYm1tivU6C-meRVBLQMWszXv-0x7w0CPemf5jYybD2_TY2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
سرمربی ژاپن بعد از کامبک خوردن مقابل برزیل: بنطرم خدا با من هم سر ناسازگاری داره. این عدالت نیست. ایناهمش‌آزمایش الهیه. خدا داره منو میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24640" target="_blank">📅 23:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24639">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9noMyoZ--EZshxs9DTG4SN-ejY5FD3WqgJxcAyle1OMCyGpo2OLzO3-yz8kKP-unQpmiLWAHwxk3_2UXxt4wNMD5hWPB-Qw-82X3vvD8ePfGTeDQ__Ps7hW-J0FkOZKQlQihdaf0x-MtB0ASUCSLYTK1JEs-khGNUFcdf-_q7NhWwupR1vIhVDi3D4tXIHpzTTXy0dz9fRX4GQqw2oVbH3bO0PJWL6vTesWncR3zCF9TEGqqkP5HF6QU8qi-BgEgxviNMwb1oAudWZe6rNgr97hfDs6DoPIIaLsMIq4LvuGZuvISRLorsc529DZ-Hmbvw-FFDaDS_UeMx45rRu7Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
سرمربی ژاپن بعد از کامبک خوردن مقابل برزیل: بنطرم خدا با من هم سر ناسازگاری داره. این عدالت نیست. ایناهمش‌آزمایش الهیه. خدا داره منو میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24639" target="_blank">📅 23:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24638">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQaGWydUPd6mOCat6K5D4wxAu6UM6lD3hV7nHqvDgsa0loOZ4sl9NVAK3w_8udWstZYinJP7b400exRmwPooigsqpmwVLZItP-pzOG5XSnWA9yFPv4-_79GqiYJEoWJip83a56JnM3vz_dEmHEjO9OFX6QdvEsFY9yQPEFIQ6mUorXetLMac8eDYcsoABoc3aGEYiAOiq4Xi3L8TvKM5DEzuDogRMfH2-0z0nj3RryrSsKNBeYweKzWjL2NGk0sUJ4JoOFtC1Er3A8dOXkdV2jl75MOWPHWCZrbQz_x7aHimUQl7EV5dBBgK-R2fRpllwzB0l1xndosxfYJG7rGk5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛صعود دراماتیک و نفس‌گیر شاگردان کارلتو با برتری مقابل تیم شایسته ژاپن؛ سلسائو بالاخره سامورائی‌ها رو شکست داد و منتظر نتیجه دیدار ساحل عاج و نروژ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24638" target="_blank">📅 23:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24636">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjMWacv6apFs4V6MQOZDCka2OuD0zCZg4sTv9qS7H1_XIEdSfsXzLqL1gs_wctSDdh1vgcTfchPVmDP2LkyML1qgFBYXk7DIBUhIkSMZi5JXcYqoOGpDkk9LJKXeeVew4azOXbJ5e7PAOMJ6nlun9oBMzQR-jqdMYTb6j7FKV9L-yH9JyXtykUzHWBrSlDpgIEcf28SeP_2x8szbJySd40JbF7Snp_R99jc8dB2MPx250JVXO9G_FBpT0PebMJbFRyU0QRnRd3MXBNygT8ZH1Kij_baiy9wu-4G56wM9YMZnitOIMOJ3Ncw5OwqgAgysbfZkkFZn9rrk_LiuRclzvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ فردا؛
از مصاف مانشافت برابر پاراگوئه تا نبرد تماشایی هلند vs مراکش و جدال حساس یاران هالند مقابل ساحل عاج
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24636" target="_blank">📅 23:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24635">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AoHjPDBEwci1IwJwOUi_limbsYRJq5la8OUiFUWGUVuMltY5G_9MAqIhQpzNFYzf3A3eyRI9q71Iz_jIhATxPcQxJJKEhVFD5fYDTFG70snhGZvElFLLSO0wnHXGYvfj5cNPncr69pPBCgkwi6T9r6s3hBSBeohfZVTb1WhhE7vAzueH8tSjcqVFsO_JuCpOzYJ19zN-dPrjEjjv_B8yKOnMnc2kxr5WsmLK_6qFZGpyu0iVsHSC50rGYLqOUdb_FjiBb6MxF5FdolknKeewGs2SEqjxq9xv4JD_WhGr3if0ADml8lKXpWaeOFvY-apuULQbOrH6eJ7ifRO-818VmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنهابازی‌مهم‌امروز؛
گذر شاگردان آنجلوتی از سد سامورایی‌ها با گل نجات‌بخش مارتینلی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24635" target="_blank">📅 23:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24633">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxwPmoq6VuzBryAjj07R0zMXfLlQiqlpp7z7vyHuG13AHFeZ6RxZd659QKL6fKaCRErvd4mqG52WWJzqT-Wl0gDDrpjri53g-TwzPLRQ6kVx5wnog_iLKDmcVHiUBFBW-HjS9e0C23ME271gaErDeNKtcvJfv6Ej_toOc1ew61uJ2o2JzodEb8flhtmXrgYHOXK105ImIiPJ9QoX2vPudA7Rw4snjgRLwtloq5WsZ-MAgEkD4DidnYKSsRUFZ_p2rBYC2jJ57AyKL4Kfs5UGzwjbd5hxpqCTmOC1GWiZ4l8_z26mh-RameNOwrXdxW_srvytL0evEdO4ysz7gj27eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24633" target="_blank">📅 22:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24632">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sg6sM-mytFZcAkcuY3ufsPely0BQcfqYt_zfvOa6j-EgJSz2R1EQJNwv6gNe4p4BV_S5WJbpdWDCHrwMhInk_XI8UYhu4Bou1AyHedPhczLgwT6LW6e_hnz9vGvjK6ypF0XrCGIJKYdlyvTVaOg1v7zJuAzuskM109oYyn3urrh0UVOoI3mBUFL5lgb-qzgrajGJLoF-D6sQy7rEZJS24qOyHMyYNRXxujx5OTP_4UASpvOMo0PCX2NTAVlUwTcTpQVLDXrVkA_B0cxiUSrcueV9i4F83Y9bT69jQnfBVrHaxWidJPVG_nE3OxwjWVdtvp2ay_TDsxnMaW6wX2e14Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/56a71ed73a.mp4?token=AUMb_RoaQU0PHq3u3vGkTQkw1bExOCYxcg7uO8eOHU8_GofE7R8SSprieykJj_4OtWdHTRWAy6KRMVX7NGs4P-es_JEBtCeayvh4E20l5vtjuALFNtcYSesda2KDtxtKszF8xm0t56jYr6Gp1VduUh9f-HWxao--lTXWtG0uShnzxJs8s__PqZ-PuG2ZDCWh4Jic1naf78edrh2kMc1hPXmD2AnCbfYnotvu5oF6UyjbzoVEgCDFQLJy4jfnCH11Oz6fNSX40PlpbvVw7wAdrp2HGW_KP0O1djeFFby3X23YlOKDba4jk-Ie2wyN55UEuJF9CyZQWP5WizZZv-YzJ6oBs3DLfQNg2bNF9e3ZRm4KT5v6uJztvID_MWgrvq2-zNerg8j8o1NVAosCtUELh38Z2M0tqx-aZKRuAuSqPIAoQRSe1Ktxkt0iV1F_EMm7izqoKskzbHE6-6qQi7Q-320M8PQC2QzzhDYGGjUEB3g3BmiYX4pOP_p84B7DGxd7A6LA3gdqdDJwp39Pxd69tUXiNXguFGfzlJJ2N6BSRYEoMeGrDeeUFTrMTtAQy_mOSh4KOjxwAMBgmVJgv1b72usyYhqoFL8-ZbrcYLTOenpX5fMyeMJYW8XviR3TNTRVKA3LY3Ikq33aOLuM2MQe5j2OvQ43rHx04QBiixzkTME" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56a71ed73a.mp4?token=AUMb_RoaQU0PHq3u3vGkTQkw1bExOCYxcg7uO8eOHU8_GofE7R8SSprieykJj_4OtWdHTRWAy6KRMVX7NGs4P-es_JEBtCeayvh4E20l5vtjuALFNtcYSesda2KDtxtKszF8xm0t56jYr6Gp1VduUh9f-HWxao--lTXWtG0uShnzxJs8s__PqZ-PuG2ZDCWh4Jic1naf78edrh2kMc1hPXmD2AnCbfYnotvu5oF6UyjbzoVEgCDFQLJy4jfnCH11Oz6fNSX40PlpbvVw7wAdrp2HGW_KP0O1djeFFby3X23YlOKDba4jk-Ie2wyN55UEuJF9CyZQWP5WizZZv-YzJ6oBs3DLfQNg2bNF9e3ZRm4KT5v6uJztvID_MWgrvq2-zNerg8j8o1NVAosCtUELh38Z2M0tqx-aZKRuAuSqPIAoQRSe1Ktxkt0iV1F_EMm7izqoKskzbHE6-6qQi7Q-320M8PQC2QzzhDYGGjUEB3g3BmiYX4pOP_p84B7DGxd7A6LA3gdqdDJwp39Pxd69tUXiNXguFGfzlJJ2N6BSRYEoMeGrDeeUFTrMTtAQy_mOSh4KOjxwAMBgmVJgv1b72usyYhqoFL8-ZbrcYLTOenpX5fMyeMJYW8XviR3TNTRVKA3LY3Ikq33aOLuM2MQe5j2OvQ43rHx04QBiixzkTME" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
جالبه بدونید که؛ گل حساس کایشو سانو مقابل برزیل اولین گل دوران حرفه‌ای او برای ژاپن بود. تو ایران هم‌بازیکن‌داریم تو بازی دوستانه هتریک میکنه تویه بازی خیلی مهم مثل مصر پنالتی خراب میکنه. فوتبال ژاپن 100 سال از کل آسیا جلو تره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24631" target="_blank">📅 22:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24630">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔵
تیم چادرملو بعدتساوی بدون‌گل دروقت‌های عادی و اضافه توانست بعداز زدن ۲۲ پنالتی در مجموع ۷ بر ۶ گل‌گهر را شکست دهد و به سطح دوم آسیا برسد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24630" target="_blank">📅 22:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24629">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kah2uIg8RYvmzhCnbEvPi-dnly0P30vz2SRn-N3XFrzC_qEg9fbzygkiQ5rkoUpmB9DP4cYI_oszBN81lTiMSCvLFZbTqtdYGJYUal7ydlcsyi_PWrjHiSJ1oCDMVNLTGvctPDOyLtZ9aVPlzJ9w8co_tjFs71gwzEgVK_qA-vaJlx6Ahho5jq4gjZ9kIuRWPVwB9m1SvnAEp27qfk6vyGLFBrqAHvE9JCKOHKzYu7iCPbtg-Odhl6EWP665xmJmLsEVxkeZnAm0bKbzXEduVOkR0EmF4LO3LU9o-dg2pnJupWko5-5d7hKgZ3vOqyPrFYUF3tagWQx7NOh8A7Rung.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b41af009b6.mp4?token=Ezxl-aQ8iZkmCHno7aUeIeHFo9jLVNWxpqkfV5NNr7k_TDD2zhdoioUbvjSROpXYLBr-q5SKa33LQchrE4hPoh2jXze17h8URUUVfQemzJMJ09wRBTQykk9LmeKJdvdgLXWgdvmXWQyX1LDbuJf8kVdbMcFDO5HdBFnAf-VA14XaeXVmfsSR_42TBOoHcqHOHb0ySPYYZdJ4DHVqrzn3jpmqUB9m_dCjKhqwUtm4MhKkMyW9kZ9wtIWjxBJr06xQLNGKrUIEUY2E9q-D8iBljaWsKbtfBopSYHj5vzeQcCyK31s7FHZhhfuTlMo91UV4ZRg2AH91G9kMw0AcbQpW2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b41af009b6.mp4?token=Ezxl-aQ8iZkmCHno7aUeIeHFo9jLVNWxpqkfV5NNr7k_TDD2zhdoioUbvjSROpXYLBr-q5SKa33LQchrE4hPoh2jXze17h8URUUVfQemzJMJ09wRBTQykk9LmeKJdvdgLXWgdvmXWQyX1LDbuJf8kVdbMcFDO5HdBFnAf-VA14XaeXVmfsSR_42TBOoHcqHOHb0ySPYYZdJ4DHVqrzn3jpmqUB9m_dCjKhqwUtm4MhKkMyW9kZ9wtIWjxBJr06xQLNGKrUIEUY2E9q-D8iBljaWsKbtfBopSYHj5vzeQcCyK31s7FHZhhfuTlMo91UV4ZRg2AH91G9kMw0AcbQpW2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت های ابوطالب حسینی درباره خوشحالی بعد از گل شجاع خلیل زاده در بازی برابر مصر‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24628" target="_blank">📅 22:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24626">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/863d336b56.mp4?token=v5_UxUEqefJsqipgn3PN_29o-fgQvucWDd6wSEuFv9i0q5YjUnj0cac3oMZu4TaAVvuBMwGceOqELIiweRB4Ah0zMGe15BwQZDcsRXSIEHf_dxNq0X_XuinN8zXpJ8pmJ4rKvC_Fu5ebFYUiuy3z6Yt2P1ryvD5KQ5ZV4VGAn5siNtHFgTubhCVSK4qwdfuaHdUywD4_47TSsTEC6KTn6jBCear_v-EgVM0gVaFjjRi7Dl_SMqsycZbz5quvWZ3NncplSqY4PXh-50ZUQqhDJg2sMm02vDHzU2xxpXpyoJ1yMXZuSS6kduGhQuNb4o0UqMlZEOZSwud8EJZWQ2Jf17ULY_Js6KsgWUeyvhca5F2jVf2jKqQjvZcM-VcImEWwIhd7AN9PQXGJFIr561ccp7baLasMpitpAFA4FJ37iC3fK9JLl9P-1QB1_aPUnWsWkygpCf-JR9SxUvXh7OvTzYwlZ8bLw4mbxL9AvCqbySYVbnzDlPY4rrFDoEIda7fRKElTRdzu-Gzs8fz6P5UK2EggHL73dck8R7VrCwf2fKQxSEAZgCDNNeOvtImcns-ljgxffmicdeoxcDCjtdyF7NrmRJWkDgOOi_ud8GqofP_Vwxxm8R6QHmVpT6JdsExnlGimEaaaj3KjsmX-797lcerwsqpQ1nZPeD9Xbqdb6cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/863d336b56.mp4?token=v5_UxUEqefJsqipgn3PN_29o-fgQvucWDd6wSEuFv9i0q5YjUnj0cac3oMZu4TaAVvuBMwGceOqELIiweRB4Ah0zMGe15BwQZDcsRXSIEHf_dxNq0X_XuinN8zXpJ8pmJ4rKvC_Fu5ebFYUiuy3z6Yt2P1ryvD5KQ5ZV4VGAn5siNtHFgTubhCVSK4qwdfuaHdUywD4_47TSsTEC6KTn6jBCear_v-EgVM0gVaFjjRi7Dl_SMqsycZbz5quvWZ3NncplSqY4PXh-50ZUQqhDJg2sMm02vDHzU2xxpXpyoJ1yMXZuSS6kduGhQuNb4o0UqMlZEOZSwud8EJZWQ2Jf17ULY_Js6KsgWUeyvhca5F2jVf2jKqQjvZcM-VcImEWwIhd7AN9PQXGJFIr561ccp7baLasMpitpAFA4FJ37iC3fK9JLl9P-1QB1_aPUnWsWkygpCf-JR9SxUvXh7OvTzYwlZ8bLw4mbxL9AvCqbySYVbnzDlPY4rrFDoEIda7fRKElTRdzu-Gzs8fz6P5UK2EggHL73dck8R7VrCwf2fKQxSEAZgCDNNeOvtImcns-ljgxffmicdeoxcDCjtdyF7NrmRJWkDgOOi_ud8GqofP_Vwxxm8R6QHmVpT6JdsExnlGimEaaaj3KjsmX-797lcerwsqpQ1nZPeD9Xbqdb6cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خطای شدید روی وینیسیوس در بازی امشب با ژاپن؛کارت‌قرمزنداشت؟ داور به کارت زرد اکتفا کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24626" target="_blank">📅 21:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24625">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q05gK6HSlJfx64vTv4-nL320N1fFTKp2WBgACkwWf-XP3SZIK4vVmNAW-XohtjZ8mJ_7M_lJgne6RZuo0B4u09QxVRyFPgdtFsTR7KQs-LJbSznQWTLEZK6AsjfDOyCy9VMgGhB7UkHiQ-c62YbTqHG7yxSFeZmA6zgH0mu2KKIqKS_p6p7BtHibQ8dzFr9jyeNmYRByoHSC4gLzb-PnOgMtGiv5XjqNu3xhLtwsJjV1--wV-RISTLz8QBWr6FuyiUz9ZTS07neHCGY4njR3gI6NiG5UkESotbSxbKiFH4jmd5v8nGHdaAiGfso1zlXIAKuWV5MI-XVqSFIDfeRgSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک شانزدهم نهایی جام جهانی؛ شماتیک ترکیب دو تیم برزیل
🆚
ژاپن؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24625" target="_blank">📅 21:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24624">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7056183539.mp4?token=NL65ywZUmFlkfVPRjTHrdB_JQhPKyvvfur2VUvj7ZE1pTNT1HsoVJgQELlCUZgbLCkflIGnAJBXTuW3HKkT03T350BbC_FN3UhSFdc-wMEQIHRuW8lcFhPDntipjEFFD_YscAOh99H55xk0fa3dktoE5k_d1GaZUN55FeQgv92Qpb7d8zPA5CtSCrIP5cqyvUHP193DqIr8Uxfuzx9YLbK1TRLSZySuSXRsEIhvPXQUQxx6ThqcADmFUgWZH-_IZN87paA5gALnj6soPQ5QqJHOHHrZXyx3sC7ZJWQ9mn4x3qKJJiIW0GNj9VrnoI-dXihcQYjxatea0IbrYRdmGyjb0cCtSGOy5x8cv4MNPAKAi4ZVR0fSU6kPUzEJA9xDyp5Ph0jn2WYdXWTQRQ5MqFU4S-DqIks7tCQKE4FYZ5nK8xLye1kYdejI03a_VpxHQuQCs5TTujW0pWbmRmx-4ofsWvueLTQZZLFoeare469ht2QFEzSWrOQ--PGDO42c1J8zN_AqehBKNK3Y2euP2mCmLvHrU1ppwe7plsiAXhsc6n6yBur5-tmFxmVDYGpGFror8RCAv24sedTtinmA2_1JtZbHeB9WinfoGQKaOeeHHr105f_U1UuZQXUVNSwhFsQ3Qtjp60uS2IDasvc2tysCyevAsxjjjuiK2JSV5-kM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7056183539.mp4?token=NL65ywZUmFlkfVPRjTHrdB_JQhPKyvvfur2VUvj7ZE1pTNT1HsoVJgQELlCUZgbLCkflIGnAJBXTuW3HKkT03T350BbC_FN3UhSFdc-wMEQIHRuW8lcFhPDntipjEFFD_YscAOh99H55xk0fa3dktoE5k_d1GaZUN55FeQgv92Qpb7d8zPA5CtSCrIP5cqyvUHP193DqIr8Uxfuzx9YLbK1TRLSZySuSXRsEIhvPXQUQxx6ThqcADmFUgWZH-_IZN87paA5gALnj6soPQ5QqJHOHHrZXyx3sC7ZJWQ9mn4x3qKJJiIW0GNj9VrnoI-dXihcQYjxatea0IbrYRdmGyjb0cCtSGOy5x8cv4MNPAKAi4ZVR0fSU6kPUzEJA9xDyp5Ph0jn2WYdXWTQRQ5MqFU4S-DqIks7tCQKE4FYZ5nK8xLye1kYdejI03a_VpxHQuQCs5TTujW0pWbmRmx-4ofsWvueLTQZZLFoeare469ht2QFEzSWrOQ--PGDO42c1J8zN_AqehBKNK3Y2euP2mCmLvHrU1ppwe7plsiAXhsc6n6yBur5-tmFxmVDYGpGFror8RCAv24sedTtinmA2_1JtZbHeB9WinfoGQKaOeeHHr105f_U1UuZQXUVNSwhFsQ3Qtjp60uS2IDasvc2tysCyevAsxjjjuiK2JSV5-kM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
صحبت‌های جالب حمیدمحمدی درباره شبه علم، خرافه و فوتبال در ویژه برنامه جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24624" target="_blank">📅 20:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24623">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clVQoz-3bw9_ci7dkvmt9DAnOgzllndkFJI_mwk9vaivxwo2jPEH8sTK5xhPjGeLiwo8C2sPUBKj4oXtkelzDONVDbHfEvZ6AXrim554cFmK7B1rqO2jC-6ChjB4d3EFYUMykDag1t2G6qv_c7-ucKg_AFvVLx7SvTb4efBAgNwp5NV-0-loTKd-TDVWy9auQL_6JaV-BWdave8cPhKk2dDlfNrZPV4bra7twSS1gLR063kGTLJTV-lk_M4QQQMHq3o2f9xL3Xd7Z4tXiH7s-71mPkYDLAt4qiHYHBbxvOC0w0iNxqqeawOHPlMtgvMQfJnujGXQQ3UC_RxTz2FCwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
طبق‌شنیده‌های‌پرشیانا؛
جواد نکونام در جلسه با مدیران‌ایرانخودرو برای‌پذیرفتن‌سکان هدایت باشگاه پیکان برای یک فصل حضور در این تیم خواستار 55 میلیارد تومان شده. درصورتی که پیکانی‌ ها موافقت کنند نکونام قرارداد خود را با این تیم امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24623" target="_blank">📅 20:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24622">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v44Dk6Z4y1DYxFOyu9SC0YG_CrMl3KWCjp4wibSSZkUOwmCMGfiFqg6_RwkOdAvKjdiLv4vxM7iNSMp23RrGUTD93g7ouUkgm1_gRmmjvkoWkwgYMNu0vkeBYrQ45q5ISGtVQqOBV0RO9JmlWwJQ6BJNjTOKilQUCFAHntF7f33yv1_LWyJiXOBkW57Ck7BgpGEDcq52ZfeY1hZXLDM5hQbDB_I5z-nhw2OFKfEeDNMS3zeCNRIimXh41M3ukoBW38KF6cCK23RPzULSLNaLz0WPM553dba93VuUr7p_BaJFazNVrmU2wAzA3ndItYPlKIPXN5Iwr-CGQsn4SN288A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه‌پرشیانا
؛ سیدمهدی رحمتی بعد از عدم توافق با مدیران ذوب آهن؛ با صنعت نفت آبادان مذاکرات مثبتی داشته و احتمال اینکه به‌زودی هدایت این‌باشگاه رو برعهده بگیره زیاده. تیم صنعت نفت در آستانه بازگشت به لیگ برتر ایران قرار داره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24622" target="_blank">📅 19:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24620">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EWPGCj_rnyWvfMa-TyKcEB6BeLEGSrVRkm4DKKx5knBMK_9ooOohx6TWQ00R3xqsF5JJjokgTMkvVVgdCUiGrRSATcgg73X_mZqr3a_sRF1og8rjYwQ-QrwKDru9zkr7MYEnI_qPW7T5HRTbxQ9xDtb1ewAS4JZsJf3-aQho9Jmu_LY2W4wf27DQjEcl6RytqNxi44o_cOfwmQpxkKLJyoaNbAJaXu8FuBSfWROeTtBctJbg9rIrjtWRzLB_wET-PUdbtyIn8PhI9nJCcluhFycT0lI3a2P-shl87YbVrw1NH4NXjOZ0fZUAUa6WsTAz77rjzN_Mm3ayH5NQ-nPS2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rNCnw0QxPXHeL-dgL0sx7Ek-uyjd2wGkRGCwaCXU_dPfqS9Vju0QHT5lfzrio_NLcCjMtLPDJ44qLR3L1cGLRbhdWqEkMeKVBHCJFhW8sloepbayRg_HDFC7vErUKDqFAiea-6zHFbVvNLMtmIjH7ZynayarRTk4rczlN-xxGCZGaw0He6EB7Gtc9_h1VMhkhcoKc-cDml6eMxBSJfR7WR10wYUaB24S8GPRZDnODctEvwcYLjYG6kHo3b2t7CCkE__CSBgEMCYasnK0M9Kv6w3tFtUC138ii7-4slWK1zx7-eAYX1E6C3278lzLo-wrcwHmrJOB5tGzsCk3bXnplg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
از تلویزیون تا زمین فوتبال؛ بالاخره اتفاق افتاد؛ تقابل جذاب ژاپن
🆚
برزیل؛ امشب ساعت 20:30
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24620" target="_blank">📅 19:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24619">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwyfyvsgP91hYHI_ovsTgDFwgsDSN40tpZHgkLMHBeG_CuFNm1JsVZIrNOxKU6jAP8xPzxucJA5igeqAfBlXVq9czr3tP_iJdqLMx86S3wO9oMsImW3Wh8UNcyjD2MUQQFB9rAZfAuofTWKk1qhTpiBHA1FehOFIvqlpyEWhwrjPWpxiTGBfhfB3C-Z4vOfl6deOHhpfsju-GyOUVKyoz8vw0rVzEpUUnSbwdmjYtzk-djsKraOAHLFpmXC5of78upkQAYPRQiwgRy8igq2S-opWcoLuwxUAQMBbv05z59NTmjWgcM9Z8N7ruU86gnjkM70ovLJwFK957ud9i3N7MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شانس قهرمانی تیم‌ها درجام جهانی ۲۰۲۶ از نگاه بازار پیش‌بینی؛ فرانسه با شانس ۲۳ درصدی در صدر قرار دارد. پس از آن آرژانتین با ۲۰ درصد و اسپانیا با ۱۱ درصد در رتبه‌های بعدی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24619" target="_blank">📅 19:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24617">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Us1RBZ7QpONHf5i9-Ky_SFQf9FyqlMdHr7nI_DyZ-EAca-pVI1Sxf4bFyGV73tOFfuCxkJD_UBb7u6sewVLBfLGwaCGRGb0VsD05NQQlB31WVMIaiY7jwuwu6JA_TwnJtgsZUXyVyYy3VsdJZtMtUlw_aMpvcTjA3H1bWbSV6CEQH_mx5Q55Yzdp5M8tJwMd2qX87apWARQbUkm2lA-vv8VtRH0l77VxsBFEiQZEr6KRKu1lHfAyxz_W1bbUwJsKPyX_v8VyqwsqWV6Kc0S8nb6nl-u6Bdtl1KYT2mzQ1Sdzm8Oc0xyIisDMeulsnA0Nbnkv2OHWartxfOwLtDgFdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛ ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر…</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24617" target="_blank">📅 19:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24616">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SjsIMezuCJaDenLXPg9br7tAuwwBUUHYrRK-6_mq8aFxMGn9j5EDOU7j7fD2ViKdaRLjB4g-40YXCYhQiwPbBx1njjPr_CDCpbW5jLAXQyT0xCnfQEB4KZl6VRqV1KSdDOIbpb0qq2rjX--F7IfuN87PCmGDGJJ0qRky_8R1kE1D26YFyO2q1NWijBHtbqrNV4SpZO-20DkCiLtW_76FQLVUDHtFbjfMGrYjlC80swWX2CLG457Bjwp1mMFopNeIcnlTFW_PMRnZOGOhCUKrfw5JUbu3Y0m8Wz5Qr_bkGdWVTq3lhFiszlHN5ylFpOc6oEJgKEcRgUC4n3ybPHAFZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
باشگاه‌هایی که در جام‌جهانی رکورددار بیشترین دریافت جایزه انتخاب بهترین بازبکن زمین‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24616" target="_blank">📅 18:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24615">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gU61smu5CV7Lvawpbhx-zoEo_bJomTErK7Mjaz17HqYn2OUuvGCJ3MygZ1Z3UTECIHSQx6zzKwKvcI7JEPIjojo12ffy3xHaFtm2mFfZXCCoz9V20WkmXzokdhJqQ6TxLxRZKNfKouOVNCJFILI3GbB2H10TJ6ftgH9-dGARNWfO1ghmMcl74SVJrxpKWnL1tC1rdyTAHbA7hNFugWZMFFq9Lx3L8dxEktwB-dGUUO0TleYXC8Nn_vQtUtZHZrJDfFjktpfrlgxiuNZSJW1zS1tn-NhdDt3urO4KCnqAtymaB36BZX9ZscpBQZfrAi5r3BYKmbtJXpCA0Vyyu98_SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
باشگاه‌هایی که در جام‌جهانی رکورددار بیشترین دریافت جایزه انتخاب بهترین بازبکن زمین‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24615" target="_blank">📅 18:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24614">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KbWC_t_HepBuyJlSKi0L2M-TchRxMIb5FIaz762BY80tnC6yDlyW28gL6HgTtfoKisNvX7rzVOr2gAyR5SjZDlWt3AmmOumLr3rzb8uN4vibHAsjWRKMUwQZDuU8Ngi-ViVzLKmhOiaXaPcj0Ba8HoCMuc-uA5O029vmJAA_xxWgm3E0fboejPq1z4s2JC9hN5iW01ej6OkZWSCG0mP_hVePmXuMBVcZvXI0L1GBwB3R2N3bVBX3bs7cgEe7AmEdjt22BYnl6ojgqbqm4BinsdyDZ4xTf0d5LROmaLYEQjXKb62Z9j5tDGMPV18PQkbD6PV5xQgn0kT0jBzODUAWJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ نشریه مارکا: مایکل اولیسه بله ضمنی رو برای پیوستن به رئال مادرید به مدیران این باشگاه گفته و اعلام‌کرده‌درصورت کردن رضایت سران بایرن مونیخ اماده عقد قرارداد با کهکشانی‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24614" target="_blank">📅 18:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24612">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbY8IyFgkrWW2iFkSg9uDJDxECLYNhx5GrmDBls2HbUpG5OqgxGAenVESFA-BtqgAY0mUGsrHPm91pgyJ_eYUxfmJJIaCjo_ddWzxilJKF46u4qL4FQXILJW7f8m7MnhvrHOPrDyQn0hHmk3RNhMgoHVoIZDd-coCamsIxuUWSxqPMAMdrWUMngVvHFfG51ZDPgpzuqVK_vV3xYm3tAg5SdSmBwzTnSidOjh8nsvOfXEVsXrxjShAzHcnDzhAfgFtfRh_Je2OGyhTXohtdxxdzpFfrfeTlNLdJ6SQ_Rw5jPc7mP62PRoVQJDvZLRrRqBeQLQUWaaAsB00-Ivl64z_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
محمدمحبی امروز به‌ایجنت‌ خود گفته تا دو هفته‌آینده‌افری دریافت نکرده به استقلال برمیگرده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24612" target="_blank">📅 16:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24611">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVGx9SylMYZBtYAz-_8VTga6t_8HEYPJpWb0RkbsTajYz6A9fTJAxqWKiXCNi15OmwBThty-wIW4liHijbaJ7AUR2RxRclt0FNj-0zSKmZS-NftSK3Sbq4Co8W5ZO9Ij7e_uMD9pUN76k1b1ZwJkJPrDu4PGHulfiTbjnEsxp_WJWMxJOUlRfhACMNECdv4gH_9rETuAC-O24PuVlOjZs88Oa8gb_xGTs29luCKoMKkfAb2GW0lUcwJ29DuhuC2zyBiPmX-kZ7Dz5g3KUCYLUuWWAj0CCsvUKZwITZ5yIPOPn0GuLdcDZfssh6XvuGbQXj2iHnrZdvxzYbaMDFPI9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریتزیو رومانو: انزو مارسکا با قراردادی 3 ساله به عنوان سرمربی جدید منچستر سیتی انتخاب شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24611" target="_blank">📅 16:41 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

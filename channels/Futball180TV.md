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
<img src="https://cdn4.telesco.pe/file/ZXgNxLRwGeFgrDEcxLYBwncoRleNzzsGzS8a6uz6ogWlj1d4lmtFsDXOqTiNH5_ohJqZIP6j5NfKEaU4s2RlIUy-F0rbA3C5_WR4OZ2oS-jMQLUXpXufhKVtdK9eR_M-9BlOIA419_nKHySppgwFZoe1kr7MDmGp_DP0LWTxAQe2sdBbD3lnrvfxLOwYXfLqWqY6q0PqcWLpn6hqwItlWNEqfa0NJNCHOs-9A4ZDvJmVasBlSKxv3LdpHawF-cwQsu9j_ErKIHRl4D87sPAIZ9_xrFOJjf_T6EUsyxX3l58GQUmy6gIfFmhuZ0vS1DOm6sjppqDJfOG83Y70s1OtbA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 123K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-07 05:44:51</div>
<hr>

<div class="tg-post" id="msg-90315">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🎯
شانستو #رایگان امتحان کن
⚠️
🤔
میدونستی توی #وینرو میتونی  رایگان شرط ببندی؟
👍
تنها کاری که باید بکنی اینه که عضو سایتش بشید و
🤩
🤩
🤩
هزارتومان جایزه بگیرید بدون نیاز به واریز
💖
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io…</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/Futball180TV/90315" target="_blank">📅 01:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90313">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFBGWfbsmH2X--9Tf6XXoZFCJ2ixvTQ_ez9TxGmZV_ifilpwNOwcqD6ULGJsdWZk9-_taUXpPGl5_PcMYyHrYfulQUmlKz8dox8JtCsiND6lCRSX6cDPy5b3ExjwMBuE5y-tnnEdG_DU7-pdQjfHz1t9GE6p_5SGcHcqPSwraEw1BJxS1zEh52LQO_lOkCFF4CEwwqxF-RCa_XNazkx4qABedBQykNZJAdglIuRfbuMv0bE0ggdXZXx4gEvsZiSbbCu-iwtq8H6myq4RPSQKZaaEQzHQGCL70DIidr1ODFeIyBKxclEWbmBUNpduMzlCjukLR_q9ERUAMy3mSz8btQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
شانستو
#رایگان
امتحان کن
⚠️
🤔
میدونستی توی
#وینرو
میتونی  رایگان شرط ببندی؟
👍
تنها کاری که باید بکنی اینه که عضو سایتش بشید و
🤩
🤩
🤩
هزارتومان جایزه بگیرید بدون نیاز به واریز
💖
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
a6
📱
@winro_io</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/Futball180TV/90313" target="_blank">📅 01:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90312">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRzMJReUmk8hwMRfWCy8xSvYXoZ6KaSGxdiQwN5cRaAKq4Sqvt9jZPk_n1atP-ncz7s_ScO6Xvp8atB14bZ8GgmDkpUCieR5ZEZs_TI0hwqO8JtI1imWZ-Ur3j45Iub9Oj1ypEbrOymUaTvfjoNboNNEOejz38pJqxgvnLe4uJiKwM79kAeyNkmzvDN8t9pWormPb4AQsgTQ2UskFFXii_efGyU5s47gOeeNEyGFJN_bA8AM7T_dddP9V4EdgiXdMRWuEVgaDsrCPrYG5mzUL0il5mE_KO8W63Sva12upOexZ9GZxwrcldJfr8V2Tt-6wYLabqE1L1pB9jBN53XWsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم‌فوتبال کریستال‌پالاس قهرمان لیگ‌کنفرانس شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/Futball180TV/90312" target="_blank">📅 01:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90311">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAc81RRyjuVoidZHMTmEXwJXhRd6SICxPzzINra_MBHHT58BQ-vC6kPoKGdyRtbD97LUSureFU2PGsxdlvjRFA8EggUQThW1JEj26nXRdAxqvDHrcfAVucATn8f9pwSenTZ6dqKBbpRsRrxEPc_1sPRyQXfbl_tB4n_ST_gS8G49GCnObt9vWwUiEtcZHhUFXutq1z7LaIsO9dQZLI8xZpUz-bhEDfEoQx066Vmf3u80qIWIPJMt5i2n6f3SJ7clqxirF4L2RN0il1vs3m5vtnVes62PUUCyFQ5DTeM_PsTHoqU0XkPVMiBussZSTKpD7-Rc2rImjf8iRb6hpjlxnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کافو تنها بازیکن تاریخ فوتبال است که توانسته سه دوره به فینال جام‌جهانی دست‌یابد. حالا لیونل‌مسی و امباپه این فرصت را دارند که در کنار کافو تاریخ‌ساز شوند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/Futball180TV/90311" target="_blank">📅 23:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90310">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
برخی اخبار کاربران گویا این است که سرویس گوگل‌پلی درحال‌حاضر رفع فیلتر شده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/Futball180TV/90310" target="_blank">📅 23:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90309">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4BuwOmX5Q5hXdTzQJWh-J_RJgAf5JTQy7dw4YIepMpum9XXgOQw3HD0o67z5ILG-DzWoPYfrdBGbH0b8k8B9_u8U41zDh3qkTE4p_onJ5LoWlQVsTfqcg0uj8rITQC6oP1_1QWfo7c28dzx5GsHH66_HPyMDPHuQx_FWmmVZQwZd2ci6-IRvsI2M-AU_TmNhx_M1YbSvT9Htt8vBnWSA-xFUaof9Wc5bEhm_3dlctlM5lUuKFYb-vqp6Jw3rna2pO7gBNo2ER_xoE1q_mqCULdccTeIUqPeKxCPYchLAkw9_9mmI7gVzTNFCJsc-ez0Y3pBRCLMS0LXGvxVIQBv-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عملکرد تاریخی اسطوره فوتبال مردان و زنان بارسا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/Futball180TV/90309" target="_blank">📅 23:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90308">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3evZK2281CBnBTeIzi5ZTiv3wdHSp5MH1pFnlFuLelmBDa1gjJvtt5IoMwpfsT-yp74Zd1ejUvmDG_mE6s_C7Gh_shh02lDwWur0W4vBH7yCcPjojVxqRygOxjBWTATMec8Ouhf78WTWW12yp6EEvPiupHR4Y0TQxnmUj7ohbm06P_zmxkX-JClgVzfkGfX-uGcM2l-ZPody6NGGmpFjfnCa-nyK9QtIq47QlyF8Z7HAeQuJLjb2XFuz4N6gpXRlCVpPadSa-O3UDWR1gFfcaixDR-e-fBRUFSbWUpV5Barnu3bZR3MosHP9LDRAyWgwL4gNfUA4U-6QZPxkTpxtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
گردونه شگفت‌انگیز جام جهانی
🏆
⏩
با پیش‌بینی رقابت‌های ورزشی و بازی‌های کازینویی، مراحل هفتگی «گردونه شگفت‌انگیز» ویژه جام جهانی را تکمیل کرده و هر هفته تا دو چرخش دریافت کنید.
اطلاعات بیش‌تر و قوانین:
🔗
bfrd.link/WCW
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/Futball180TV/90308" target="_blank">📅 23:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90307">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84204a485b.mp4?token=FNiHnsJ9tejIJH450uUiGl_vn409uzHytbHYk0qgqTjyX5jIO5QqmNVT5k-nQ2VK7dedbh0skW7xB9bcu2QB73QsRJC9hnb5ZLxgMusDjMsZP3gSKnJsMdvqOnbtGyjgTuoZwZTA53sGOO3DmpATbU98Pg-tkJM4UE4EzJENJN-rg-3TDZ-wvRvYfYuGNFxwErXbStcGTVfBwGbrpvFV3WPdZrfW0AmAyiud-Ma4qpnJHMlBo-wzhuTA2GD0fHUZvEmomT6Uy6D2i2thpyPW1C5o1GSq1w64z0Dvk39CztF4_RpDe8NpnDPb01JVGTh-Ayl2sM7XtZpntjpsz-KdDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84204a485b.mp4?token=FNiHnsJ9tejIJH450uUiGl_vn409uzHytbHYk0qgqTjyX5jIO5QqmNVT5k-nQ2VK7dedbh0skW7xB9bcu2QB73QsRJC9hnb5ZLxgMusDjMsZP3gSKnJsMdvqOnbtGyjgTuoZwZTA53sGOO3DmpATbU98Pg-tkJM4UE4EzJENJN-rg-3TDZ-wvRvYfYuGNFxwErXbStcGTVfBwGbrpvFV3WPdZrfW0AmAyiud-Ma4qpnJHMlBo-wzhuTA2GD0fHUZvEmomT6Uy6D2i2thpyPW1C5o1GSq1w64z0Dvk39CztF4_RpDe8NpnDPb01JVGTh-Ayl2sM7XtZpntjpsz-KdDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیر قلعه‌نویی به سبک لوئیز انریکه درحال هدایت شاگردانش برای جام‌جهانی فوتبال!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/Futball180TV/90307" target="_blank">📅 23:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90306">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fa7TUkEfvWd3apo-jfpcfv5fovppJLiM8nRVN8bJW5JGowgQHYCHeAP8JfP4UOWqAFGE-EZa9RB-45SOUGnbTZjI1SA0qWUwhT7VnD9SQ2JovCoc7BBV46N7nFEEVguFx0h_cFet_wh_g2Qmdv605plb6aBnJsVDJKSZH0Q7rz9OAdzuxTxnxpkrues-OwdALcR7gqmnnjEqGB849543FRvUtqsI7zQGmsYm6EUfx2_qnv0qw8au7i_h37ehUIcngLBADc6A3LloJhiPfCPtxcA_n8NG3Po_UmS3PO_TtzxZimocEw8RU8wVMskPyxuZWitCjAuMA87YwwGFi34A3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندی رابرتسون ستاره خط‌دفاعی لیورپول با عقد قراردادی به عنوان بازیکن آزاد به تاتنهام پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/Futball180TV/90306" target="_blank">📅 22:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90305">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80080a6ded.mp4?token=hEuIBkcw_KhUmWPz7qRaLsyXfrT5OEsUdGRu54Yjr0b7rMu2x90GrPHAiIY4TFfdx5ELdsnrrXY_qtXWkOlZN7lhyDVvWPwObVY1mSy-00yMUW3LnZaKZXLYNVFB5g20XtWoTyflqSYcENLO3PuJvyYLSQPMRV1yEOmCLe1FSmkJ9xUqhkoVPG9h5OZo4mN_Kbl1BK6MX9Oxvg5o9K40w4RGc8KjKoLnBeiK-d9rMVJISpGstOf6AXbOoAHpFxR0P8BGaWL7UdnqTYjBwyNGzu0XQ8imHkABBVK_yNBgQ_P3XgS3KetgHyMPpilYdRlwqx9f0xk1hWjUtHMI2Hy3zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80080a6ded.mp4?token=hEuIBkcw_KhUmWPz7qRaLsyXfrT5OEsUdGRu54Yjr0b7rMu2x90GrPHAiIY4TFfdx5ELdsnrrXY_qtXWkOlZN7lhyDVvWPwObVY1mSy-00yMUW3LnZaKZXLYNVFB5g20XtWoTyflqSYcENLO3PuJvyYLSQPMRV1yEOmCLe1FSmkJ9xUqhkoVPG9h5OZo4mN_Kbl1BK6MX9Oxvg5o9K40w4RGc8KjKoLnBeiK-d9rMVJISpGstOf6AXbOoAHpFxR0P8BGaWL7UdnqTYjBwyNGzu0XQ8imHkABBVK_yNBgQ_P3XgS3KetgHyMPpilYdRlwqx9f0xk1hWjUtHMI2Hy3zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگ هادی‌چوپان با رقبایش برای عکس گرفتن با آرنولد در رقابت‌های اوهایو!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/Futball180TV/90305" target="_blank">📅 22:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90304">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35b0dae947.mp4?token=uSKvF1pAkWivot-Bq5-2hpjxtpgGnWhnn7FPgmz7-CiMxx6IzpO0Lo3qDBz0IYjmidLZHifeAXq9MHhdUF9hb3eTAIAd7iRnWsrsryWlaj78eszSYJtPAbQeAfMPWRnO5HDXvsFNuUAqz3L-oGiAVoNvrs15SpuvAkIFAOJYYrW6m_kvjdp_MkU9ZQDw0XUE1LEGGPo-RkjLWIrIimgkLVj1ZpL0Qg_kLZqgGzqVwg-ALon2zToeXuXg1GU71jpZCxE3DtqtRrZzm9tC8bJ4_LOM-yvx7jRU96D2fB426E9ZZf5J7F8BvcWtQzl4a5wQBa-4RF_Reie8-XPSN1mJuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35b0dae947.mp4?token=uSKvF1pAkWivot-Bq5-2hpjxtpgGnWhnn7FPgmz7-CiMxx6IzpO0Lo3qDBz0IYjmidLZHifeAXq9MHhdUF9hb3eTAIAd7iRnWsrsryWlaj78eszSYJtPAbQeAfMPWRnO5HDXvsFNuUAqz3L-oGiAVoNvrs15SpuvAkIFAOJYYrW6m_kvjdp_MkU9ZQDw0XUE1LEGGPo-RkjLWIrIimgkLVj1ZpL0Qg_kLZqgGzqVwg-ALon2zToeXuXg1GU71jpZCxE3DtqtRrZzm9tC8bJ4_LOM-yvx7jRU96D2fB426E9ZZf5J7F8BvcWtQzl4a5wQBa-4RF_Reie8-XPSN1mJuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حق‌ترین جمله‌ای که درباره وضعیت فعلی میشه گفت:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/Futball180TV/90304" target="_blank">📅 22:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90303">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05aa244672.mp4?token=S5Bs8B989P8yOojO8GbbWbghTAEu4aaZzoJD6ra8K01MTocVPRfR5GNriR_skic3uhwocElBE1EqqOYYnz3_GdGpMVz4EdUKmDlSdd-ZM8ydPrBXV4K59ZkG0f-4WGJf6QSEVpAAoTUQaNW31H9VlYQsdQ6Mtm6gwvln6S9SMhyx1zdFjwqYXV9OnQYtIhzDKp5vI6j4WiTY3TiVykxj2JesRO6qvbmD57_AIseQ9cxdpuQs4z0j7OqdSNjXqfonY2viXSdclueiwQVJxHsVp2hJkFi_qnt3IJ2vZzCd1eaIXJ8UTkYtBpMdzzMADcfdsWqDQHyDfeGxDKlSKhGHMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05aa244672.mp4?token=S5Bs8B989P8yOojO8GbbWbghTAEu4aaZzoJD6ra8K01MTocVPRfR5GNriR_skic3uhwocElBE1EqqOYYnz3_GdGpMVz4EdUKmDlSdd-ZM8ydPrBXV4K59ZkG0f-4WGJf6QSEVpAAoTUQaNW31H9VlYQsdQ6Mtm6gwvln6S9SMhyx1zdFjwqYXV9OnQYtIhzDKp5vI6j4WiTY3TiVykxj2JesRO6qvbmD57_AIseQ9cxdpuQs4z0j7OqdSNjXqfonY2viXSdclueiwQVJxHsVp2hJkFi_qnt3IJ2vZzCd1eaIXJ8UTkYtBpMdzzMADcfdsWqDQHyDfeGxDKlSKhGHMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دنیا برای آخرین جام جهانی شما آماده نیست.
💔
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/Futball180TV/90303" target="_blank">📅 21:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90302">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NthtgRDn9nWUDg6MyoVPh6chkWF7NAZ7NEvhnemShEhzp5eE-pGL7dDmiPCZZ3rvxkc89H5y-dwt7tzYHWnrSVuEwaL47BX7lIbeaPQye519qYfEf6oSjxVZ87PfdhZZ8G0a0StRSG9Wdpwf2pdQp1QjYyAStrgHTW1iAiL_uI_I1zn0cD1bWS7h6ZSAWwrcWTQoyI5DAoWsZ6ZfuGjq-Ab3QxU8BcpcUFax5BuYKHNulNugRGcptvgIVtCdIXqgmT1CCFxzjxSi7Q7hudozickn7Owk7ngAxR7iuK_gPYivvugLt9EfLBkH2pwMy3sOy9Fd-7b5EAPvxqfhVH7bxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#غیررسمی
؛ آنتونی گوردون با عقد قراردادی به ارزش ۷۰ میلیون یورو از نیوکاسل به بارسلونا پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/Futball180TV/90302" target="_blank">📅 21:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90301">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b45e4bbf26.mp4?token=aJlbmzh7TI7Fi5QDcaeo4kDJFWn5YxOOD2Wmt_sOfYprhHsGsi_lJhElp_2Aeeg-V02zOzCHSw0hPw80pTaIdcVru0oVKHzQa2k7S33ppp3DbmJE0_Yl2spt24KbLTZID2AfXZ_I8obLPmAd89wL0ihuk3IA0RdpUnSNyJN2gUqEM7OdIY9tPCo_dDQFwtVK21_g87zfjlznMeGQ8f7afJixKBUS628xpDgsgloZMD24veK0Jf2_cY25Ze-IdgH-gK0FCcVTwReD3VEbSiglnAJc8f43htnM6kJOKu__tLktHs5TiKfjU3SufmwJgnM6boiVZ5bCPds9PR_R1zob_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b45e4bbf26.mp4?token=aJlbmzh7TI7Fi5QDcaeo4kDJFWn5YxOOD2Wmt_sOfYprhHsGsi_lJhElp_2Aeeg-V02zOzCHSw0hPw80pTaIdcVru0oVKHzQa2k7S33ppp3DbmJE0_Yl2spt24KbLTZID2AfXZ_I8obLPmAd89wL0ihuk3IA0RdpUnSNyJN2gUqEM7OdIY9tPCo_dDQFwtVK21_g87zfjlznMeGQ8f7afJixKBUS628xpDgsgloZMD24veK0Jf2_cY25Ze-IdgH-gK0FCcVTwReD3VEbSiglnAJc8f43htnM6kJOKu__tLktHs5TiKfjU3SufmwJgnM6boiVZ5bCPds9PR_R1zob_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چالش جنجالى و جالب مجری با محمد نوری پيشكسوت باشگاه استقلال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/Futball180TV/90301" target="_blank">📅 21:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90300">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KInlT9wEkb3vaIuEqlinV4EzZw_Hq53bRXbwjQ4-uiVjx0xxQkqplT2cvI9ULRBd0l-vxMhaoea-A0OWeL_iwFH2gZ7rCRdWk9SPZx6NLloWAp_dCOUAJyaj_keM0Lzh5q7HuFODt_Rgu5_lpapQHymSSoxptu-hHePMIaZDA2n03jiu9_9z7QD9gL5745wyaehpS_ZLgkHZDctw7kDE_T1IXbSeDjVKquHUYiW0veP__StD2Wp7lOD33S5mQtewaHkz_hT59EIRfyYGd1MkYOm3K26AKRD3goHqdK1FFGf8x7Gh6yYdu26GGKUl__BzfEbERiZXQVjOozBClsaH8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات‌تاریخی از مراسم جدایی الکس‌پوتیاس ستاره تاریخ فوتبال زنان بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/Futball180TV/90300" target="_blank">📅 21:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90299">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-trhlD_zjHfP9Z1RBOA8c8q0NsYhyPezdNUpaH6e-hjIuSZej5JtJLnSZQVoYX1NTE_laNDErlBjT4-UFu5jND1Cm443lzHWM-W4mBXzRTmk1VzOPdEunz1qOsw7OTfj62Rs0CY_2qbncA0J5Obh_Rshc5F-zM5fU1vRbIRWXgxlD3bALyxVG4Chy8WZX2Yhi31CB9MtA2Gv8DdS21XD8V9nWequWrB2j7MqNPWiS_ZaSG9Cm9VNotzrZYVy622SEEGq9pnrDM15CJRvakRITh0EkXEtpWLhY-aVuUPmOI-eq6pm8OPx8bW0hROA2HP45mobtrUngDolJxbsJnKTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قهرمانان تاریخ لیگ‌کنفرانس اروپا به مناسبت فینال امشب این‌فصل از رقابت‌ها
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/Futball180TV/90299" target="_blank">📅 20:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90298">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a28e2aed.mp4?token=pVF1O8YNWNx5oGtz249NF-_wpSku1kW4dPFXp4WTYoIVkyk1sru5KktfV6bSwPwmaGx7ng8IYot8J2JHpVoxDk5e1IZcW5a1Z1w390n_p2FEI8HaKhqvQ-u7DVn3_4OTuoEXvXWtl19BiROn_alqAbrK9PEmtGD3sTjyaGeJ0rnwqDWKW9elSm1tA6Bb9u6rw5AAY0z8SfPLT02zupw1q5bChMntp4Miyf7jfwsZ2NEyP_3ihHEsnYPnkTDRfKlt4qoC9ucszt3ulz2X_WWRTH-g4qVlg9KMTyplj1CEEHlz3lvj-pGM2k6BQJ_C3dbXQYh_PR7bwJXdVunGp1slnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a28e2aed.mp4?token=pVF1O8YNWNx5oGtz249NF-_wpSku1kW4dPFXp4WTYoIVkyk1sru5KktfV6bSwPwmaGx7ng8IYot8J2JHpVoxDk5e1IZcW5a1Z1w390n_p2FEI8HaKhqvQ-u7DVn3_4OTuoEXvXWtl19BiROn_alqAbrK9PEmtGD3sTjyaGeJ0rnwqDWKW9elSm1tA6Bb9u6rw5AAY0z8SfPLT02zupw1q5bChMntp4Miyf7jfwsZ2NEyP_3ihHEsnYPnkTDRfKlt4qoC9ucszt3ulz2X_WWRTH-g4qVlg9KMTyplj1CEEHlz3lvj-pGM2k6BQJ_C3dbXQYh_PR7bwJXdVunGp1slnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله عجیب مجری پرسپولیس صداوسیما به سروش رفیعی: پرسپولیس باید یقه بازیکنی را بگیرد که حال نداشت بازی کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/Futball180TV/90298" target="_blank">📅 20:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90297">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ac28b3311.mp4?token=tLIN2-KIzc7z12ZQb0uoxK9aGOuApf9JRddMMx_edPO1CBwnRx18lCbMaeswiOeRkcCppGjD7aWlEWDq_fgWXQtp2C8kLfrr2U_spJTtBLZEDls6bzJ9coQrcBBuYPeIQbbFzY5paKUaMkG8rJheZE9ntxyCeI3QZC4wMtYnmp8VsEMp_AGheKWKcdpYgVacvMnwDZW1gATl4GfeMOp582tdNr7r4-PNpA4vtOfKbqZSllCrPtoIHTZXgqN3qoDJzpAvHgBrDrpR2s6JAfENqbBR9wVMlR2CgnEqAluIj9Ganqj8D0WzRZtgDlau8Ou96gdeLYQF4Ovu0HZv2ZB3aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ac28b3311.mp4?token=tLIN2-KIzc7z12ZQb0uoxK9aGOuApf9JRddMMx_edPO1CBwnRx18lCbMaeswiOeRkcCppGjD7aWlEWDq_fgWXQtp2C8kLfrr2U_spJTtBLZEDls6bzJ9coQrcBBuYPeIQbbFzY5paKUaMkG8rJheZE9ntxyCeI3QZC4wMtYnmp8VsEMp_AGheKWKcdpYgVacvMnwDZW1gATl4GfeMOp582tdNr7r4-PNpA4vtOfKbqZSllCrPtoIHTZXgqN3qoDJzpAvHgBrDrpR2s6JAfENqbBR9wVMlR2CgnEqAluIj9Ganqj8D0WzRZtgDlau8Ou96gdeLYQF4Ovu0HZv2ZB3aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال شیک نمایندگان آمریکا از تیم‌ملی عربستان در بدو ورود به این کشور برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/Futball180TV/90297" target="_blank">📅 19:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90296">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4496fe5fe.mp4?token=OCoLVxE1kFCLVhEDIonDcm5Wyurqc82uMLd1l-WGuBbcWWNVUt-zZGpSCAOJKd6MWbKHPbpvtMX2YlRZiuJ0_8USV1qxsKv9tXo1e3luXRweHOuCo9_p92nPwOodQYX5zVxA2nHk55ZhE1Rz0hGjK-Fp5mJQErGsYX42QCOUXtq17yHRxGbz6O3EpSlKpAdOfkqd-QC9BshK0O2sbm0b8Bll76w-i0DltK92n_qOtN0X89JmdrT3mGww26Yvzvte507u5mPyK6AI-RlE8OuZRW2jmSWBigDAkIZfjk9HKcfP0FtSH_8MY6YuWMdfmyE92NHpHbdhStxeimpTVCdMzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4496fe5fe.mp4?token=OCoLVxE1kFCLVhEDIonDcm5Wyurqc82uMLd1l-WGuBbcWWNVUt-zZGpSCAOJKd6MWbKHPbpvtMX2YlRZiuJ0_8USV1qxsKv9tXo1e3luXRweHOuCo9_p92nPwOodQYX5zVxA2nHk55ZhE1Rz0hGjK-Fp5mJQErGsYX42QCOUXtq17yHRxGbz6O3EpSlKpAdOfkqd-QC9BshK0O2sbm0b8Bll76w-i0DltK92n_qOtN0X89JmdrT3mGww26Yvzvte507u5mPyK6AI-RlE8OuZRW2jmSWBigDAkIZfjk9HKcfP0FtSH_8MY6YuWMdfmyE92NHpHbdhStxeimpTVCdMzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور نیمار در اردوی‌تیم‌ملی برزیل با بالگرد شخصی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/Futball180TV/90296" target="_blank">📅 19:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90295">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFKqbup26FCEMHhtNHLFItxy8ExxXhmfrMcln3jTN4_4RS1Q7nDH3C2EWQNpqHgA9mYLe22lN09uf89PPIyGOouBvHYYB2fzSdqcQkzR1aY3o2baErX0t64NYBgWXHvfM6bX8ks7C5g38Zv-umLB1uSEzQcxHp2raifuG2nuPQPfkoDmDflk1IV2pB9he92PYdUwubtjAwcGsLmXnBJDT_wjq37V5-OoYD2eXsoksb0l1tKQZBFflbqttJrB1nemOfDaMLQLybXzBclPQUY0WRryoFMI1ru6hKv6EYtFLdALTsvRkVFNN6TgH0lu2Ms8lpsOdg8lH0cIIjQRpScOXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جیکوبز خبرنگار مطرح اروپایی: چلسی برای فروش انزو فرناندز درخواست ۱۲۰ میلیون یورو از رئال‌مادرید که جدی‌ترین مشتری وی است، داشته!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/Futball180TV/90295" target="_blank">📅 19:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90294">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c0fba26b8.mp4?token=vrb9jf-euJTJmMdkV-W2Icv_G5X274ea1ttQZIQVvcHVFldY9-IT3JGOHoWsHnr1T0EfL3kkTfFjBr5aCa6y631GFDHRyc2pbR5IAhloHlQ8vzb_KSQSOiPUydEFCnlV_gTnXKspEBbScjFiqKlVXtom7EahVwOA69b1NifNEP9sm3_mchE2KuSVmMK-UJQopZegTnvZOs3_YnVqlkWOKcJtqIEaylPwFpzEtqPR0H83C7e1koUAWxj4ZoUczP-zO8PCuXv15VNbHrYWk0R-WFS2fha4yFMwDCvC4UGe0k4niVMz1OhA1jHm1lX74mM_-deA7uS0TgMSSzDxULBrs1gZtWtZ8nDHuuYwIHWjXkXeEKcCIhpf6x7JPZaoy4C9JGM4uoRUVeZoMM_WG0z1L7vUxGa4gU1Fu1FM-QLLxzEonI76swZv2KLtf13TeWXc1Hq2oufS2Ls7hBCs2_XsA69KCBE02FSjJI4xjn3U3EZAtLP3Y8cerAyLKEeiK4PsNg_Fgdv-PPLIkmyO_3W_ltlohb91PCpalX7R8BBIT5WMkEmMb2iztj22sykcLUPdDMYJzlwRej0ESHmvAFr6_iNzS8JBZEvqOgYRq9BomicIA4JwRJQsJZN4R7fMBcswWaVYRUyH8NaWxtQ415UEdDHwDus5CuW3nQoW56vewYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c0fba26b8.mp4?token=vrb9jf-euJTJmMdkV-W2Icv_G5X274ea1ttQZIQVvcHVFldY9-IT3JGOHoWsHnr1T0EfL3kkTfFjBr5aCa6y631GFDHRyc2pbR5IAhloHlQ8vzb_KSQSOiPUydEFCnlV_gTnXKspEBbScjFiqKlVXtom7EahVwOA69b1NifNEP9sm3_mchE2KuSVmMK-UJQopZegTnvZOs3_YnVqlkWOKcJtqIEaylPwFpzEtqPR0H83C7e1koUAWxj4ZoUczP-zO8PCuXv15VNbHrYWk0R-WFS2fha4yFMwDCvC4UGe0k4niVMz1OhA1jHm1lX74mM_-deA7uS0TgMSSzDxULBrs1gZtWtZ8nDHuuYwIHWjXkXeEKcCIhpf6x7JPZaoy4C9JGM4uoRUVeZoMM_WG0z1L7vUxGa4gU1Fu1FM-QLLxzEonI76swZv2KLtf13TeWXc1Hq2oufS2Ls7hBCs2_XsA69KCBE02FSjJI4xjn3U3EZAtLP3Y8cerAyLKEeiK4PsNg_Fgdv-PPLIkmyO_3W_ltlohb91PCpalX7R8BBIT5WMkEmMb2iztj22sykcLUPdDMYJzlwRej0ESHmvAFr6_iNzS8JBZEvqOgYRq9BomicIA4JwRJQsJZN4R7fMBcswWaVYRUyH8NaWxtQ415UEdDHwDus5CuW3nQoW56vewYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماجرای بازداشت نیکبخت در پارتی شبانه؛ این همه آدم معروف آن‌شب آن‌جا بودند چرا فقط چسبیدید به علی نیکبخت؟ گفتم نفرینت می‌کنم یک روز جای من زندگی کنی ببینی جنبه‌اش را داری!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/Futball180TV/90294" target="_blank">📅 18:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90293">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SvgOTvvQ9xpGz60O5qNam82e68sujU4h377XekGO4iPlKPK1vfkZmiQMECJcSCM9ZWU53Ca1JeewAYiVuIsIYwRsS_rEimyUjCyX6inDWPN9pe8MAxZe5JDpCM4qbZKAYPlDFdWwLRlRhzkNRIrrED6S5YNkqyfFM5T8ziG6zWS-WA8S7BY9Pgyfjg84OilKDuAgfNv8royGUPF2k5NSj6SjtU0K15onNZiH11bgteuvNe7wwiC60VETnuQHyGDkCa5ATQWd8icGHbslhNpou1zNgtSIvnOAzsXAXSH-XXeW6_zBRelIomHvmUJw3pDmcztx0w8pRMBuYOtQY01gYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین هتریک‌های تاریخ ستارگان فوتبال
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/Futball180TV/90293" target="_blank">📅 18:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90292">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">⭕️
تا حالا بدون واریزی روی فوتبال ها شرط بستی؟!
🎉
500 هزارتومن بونوس رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
شارژ سریع و امن با درگاه ریالی ، تتر یا ترون فقط با یک کلیک!
⌛
پشتیبانی 24 ساعته
💖
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:…</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/Futball180TV/90292" target="_blank">📅 18:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90291">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBMN4k15SFfLweXvwG9RYaJpfHf3kmxyFLWt5cA6LlerM9ySF4SbfXHTN_78R6QiTAtWgw19zk-Uxc4m07J6XQU4OhZevCT_rmLX6567bjDw7Pl28zuAughMhDfUyvPl_1YMEg9E8fK9eVcXrxvdBaSTv43F0ppGo4FlB6XYxDI1G9Ve7TqMovzN8NfnLg4KrCWulUMbdISn5PoYKzlLrSt6WYXd1dabOmB5eKaDboG2w-73cC-HCwWsxQ-MNCOsuHZbQnGgEhWu8vz9RwW84N3pyB9gF6sWS-gdbtNpqsNuzy5j2Lijl5nIgf_CckMAYkvPKQE1Fu-UEBd7zyu39A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تا حالا بدون واریزی روی فوتبال ها شرط بستی؟!
🎉
500 هزارتومن بونوس رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
شارژ سریع و امن با درگاه ریالی ، تتر یا ترون فقط با یک کلیک!
⌛
پشتیبانی 24 ساعته
💖
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g6
📱
@winro_io</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/Futball180TV/90291" target="_blank">📅 18:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90290">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cs5XFl-scToXIR1p0vwnjz4hBffCfxhyPF4hh541h3-uy2xCrENigDuwhnSBlhmiuZn3PKhSXS5LoBCfSmuM3pbVM2pESSqh13vpsPygXdGPEPh63r3l_vjfhJqrqciY5PshiC--pJAH_j-c9anF-9fGrHt0vm6M_1FWa5nJ6qN-V0kEg-_9Rzw2e_M3pJP5Hm5bGc2qw_PbSpYVNvlrAq-PyxMOr-sBEgFGmM5QDhifq2RDziKT87vLTHbjgAoB7XCBMmzfi8-4AKPB0T6V3fUUi3sN5l1Wx8NrdL0bGjLjRHhfn1OgX4Z8jpQC-1zBjRD_RZiq5rgCFpKlqZNvZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمامی قهرمانان جام‌جهانی در یک نگاه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/Futball180TV/90290" target="_blank">📅 18:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90289">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Coe5SXlJ3GBuYSYiHIlHmtS8FHeabG6JQn42kdqxBVHz8db5JstUmCVxF2CAaebbVki7w78-vEzKTLKRoBpW5X7DCBVjlcfovcOxVmP4IFBaYRfZx1TMbc25f9qViV6qElYvtE7uGqBjgddUXOtvr541DR7C-i6G7I6JtotoIRIqM87NSj337LwApTNX5uNiJLbyBlpKljAZ71y098lUWFkYpYgoV4oE5H4Jf6yGB0KT-hJsoRH0ubSsIb5V4y-sFEpGt8rwnGMLKYzYPpVdMK40yOSk2Bxpp_5chfNt51BOac0NZ3eV18bI7R-vfqz9VqKIWbhchK3jw2YvHqksIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
به گفته اکثر منابع خبری، قرارداد آنتونی گوردون با بارسلونا تا ساعاتی دیگر نهایی خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/Futball180TV/90289" target="_blank">📅 17:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90288">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXzQW_o8F2W6gqwPid1kVl_qJF6SlrfJ6gmfjJRiR-ULDRwFvMS70YbwgPF4T5FhlTSY0YlrbTf3w6MFE15KkV5Z8e-l6xnBg5HZeu3-doF1Ir0KhXHf_nPiO20gw_D3hWuEYlBEgAsRWxgVWqGDD_nxgALi4zMetfDSwacnFppD7FvIq1cHs4keIwBnDhMZuqqM0Xsi5VbsUnFE3sUHOnZU3wuXnm_q6tsML3U08gQoSSXzv3TyqezOzTxSdZcQ6FJlyqHOMgeoOCQvDNLGPKqjedD3KRO1l3bxnvd0RqxtsC3g7ZcgZBLpWLuWtXg-qRt7Pw81G-ERHVCam1FjVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه میزان بازدید پست معروف جام‌جهانی با پست اخیر نیمار در صفحه شخصی‌اش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/Futball180TV/90288" target="_blank">📅 17:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90287">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hu729zj7E4x21Qjz9ZkvIK4XzNuvtPRNt6toX1q4hT4v3nJXQ8BmYt_JIw7cEeAC7wOqTuOMNEFjVPM7rPqHWfmjUP9dKqASVvQc5S9iJqAIkyOgvT9Wu0pelPdEpKrSiC_mxQNTOMFjlm-kOMT3vo-FdxwuIpsFcdtz3GIwsw9YVfKRNVpehKcdXm6DH5JvFzgmTft5YrJJJ2PyINjTY7SjZejKacRWaqkOmUDUKJGpc6BSkpGrn1CEHow27KNv7KxfAeIJ6CpScf9OBPym6eiM8dI0Qbd2ZouF6mYgn4xsF9m7P0YySXh8iUJVU51uwz3f8jBq1gqydx_m8YaXZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جرارد رومرو: بارسلونا قصد داره قبل از جام‌جهانی قرارداد گوردون رو نهایی کنه و سپس به آرامی در طول تابستان مذاکرات با آلوارز و اتلتیکومادرید رو جلو ببره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/Futball180TV/90287" target="_blank">📅 16:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90286">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30945cae67.mp4?token=sQmW_I_RMzPoLCGX04LpAYWfHi0RPlBCKBOSURqQfCZw7XhhlOPht1aScJLJrhZaRy4RYjSmt2zctV85H-G8opQYxf0oj-2xrRfy-MFP8ZDH1ncfKIfdidvMhYWj8LvHCOoK9YP5p94YUJScJ--tiS7nX3XxpZpq2W0kpKQa2GcXOBXeptuAeJgdF23hf0gWatQWxa13Edmtc0rjaY7ln0i74OEen4HHlL1rXVqwetStBGIAwecoHe_HkT67EZ7cB-E9VrOr5z8FV1kbEVB_QegSwL3XM-vh7bK4Fu1MEQgU82Qrblid8YYNOSRsGBr0m-HIFvBxYt3S3AEmXjs8wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30945cae67.mp4?token=sQmW_I_RMzPoLCGX04LpAYWfHi0RPlBCKBOSURqQfCZw7XhhlOPht1aScJLJrhZaRy4RYjSmt2zctV85H-G8opQYxf0oj-2xrRfy-MFP8ZDH1ncfKIfdidvMhYWj8LvHCOoK9YP5p94YUJScJ--tiS7nX3XxpZpq2W0kpKQa2GcXOBXeptuAeJgdF23hf0gWatQWxa13Edmtc0rjaY7ln0i74OEen4HHlL1rXVqwetStBGIAwecoHe_HkT67EZ7cB-E9VrOr5z8FV1kbEVB_QegSwL3XM-vh7bK4Fu1MEQgU82Qrblid8YYNOSRsGBr0m-HIFvBxYt3S3AEmXjs8wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از حواشی بامزه مراسم خداحافظی باشکوه پپ با سیتیزن‌ها
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/Futball180TV/90286" target="_blank">📅 16:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90285">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c42b3ba26.mp4?token=HsprUocrlvDe_Ki-suB-S_FbrGMwMGNk5rPP7LPI7wdcy2ElXMBGvPLoSnyCaSNRaBjQqC9jaOxuIuh5WpHTjTCNQKH7YOfFOmAT7tAMpVxz4WpzIxCaArsCNx5ZOi8UOnE2kYf7RIi83vzDby6PAUPybazLgvq8VsHijxMbwUGBdv7p5XPkmBCgN0AwlcNllW3ED3q2MdmAQiM4AIwjVujxM5KuyIjT0KzEBOrgg_SDz-568IXXx0Yr7UPO5KzrTTZw9-I0LJdbnPxc1NqLYrZ6PoUL54r82vjX_6zYZcTS9EUA1MRB_2zYCwVG3TQGQoDNzlNEIO_HM4NYw-uQCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c42b3ba26.mp4?token=HsprUocrlvDe_Ki-suB-S_FbrGMwMGNk5rPP7LPI7wdcy2ElXMBGvPLoSnyCaSNRaBjQqC9jaOxuIuh5WpHTjTCNQKH7YOfFOmAT7tAMpVxz4WpzIxCaArsCNx5ZOi8UOnE2kYf7RIi83vzDby6PAUPybazLgvq8VsHijxMbwUGBdv7p5XPkmBCgN0AwlcNllW3ED3q2MdmAQiM4AIwjVujxM5KuyIjT0KzEBOrgg_SDz-568IXXx0Yr7UPO5KzrTTZw9-I0LJdbnPxc1NqLYrZ6PoUL54r82vjX_6zYZcTS9EUA1MRB_2zYCwVG3TQGQoDNzlNEIO_HM4NYw-uQCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرتتا و همسرش در جشن قهرمانی آرسنال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/Futball180TV/90285" target="_blank">📅 16:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90284">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZZUBhClMlC2Pffqsey1BSCVonztJMGScNWDPvcguZDmO3pvHDOw5E9soAcI32tJP3RR4bTzFEvMdgrjFxnkNn3lcaJssnQ6SvrC1KBGb61oVanHiC4lIsdHhCO_U2qANWhoNI0-PyY_ZtTygkGSfT6PdIzqC1MIk5qShRDIMnkhgRMlCjoom2b2OHjjtB-GMYCSEv3z0j3QMzCg-wpx30-hLAFBTfflVz2foOQ0IOvqTpEiyhaoqHEUE-y0UxNAsvY4TlX8WTjV7SqDxfibiHi2035iYLDJEXF1Th8-MfaQoz2eVVivZ1joRfMdcXt5jcrrcoMIjQ_8CWeHHVmtvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست تیم‌ملی هلند برای جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/Futball180TV/90284" target="_blank">📅 15:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90283">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDAmxhI6I1VGqJBIMfP2JcSIIdO6Gr3YlkPzT4rxvVWBIEtVi5RZ8vbIiRhp-oxvlYUr335S1BXzSGkxCEDmxc6xSH_HdUbN0vpAJq7i7ziH-pPu0Sm2DENh_ohbc-T4SrfgJY_hHH9N6Z160ugx80MC2GCS5wYReB4ScNBDhv_s1QfWoaWJRv7_Hib-67MqWF0TL1rlyIomAAmkBuYKjb0nxwVWbuxYou7Y_WcMXQpd3xTGj-QvbTvl92gMTsCXDM3Mw75c5IIaoIyVyfGUo1_w2XoCPBpm78bippvdQHGAaj_pW0GYs5023RdnJUzMDqowLwX7Wq_eCbvGi9yFfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنج سال گذشته: کریستیانو رونالدو ۵ عنوان کسب کرده است، در حالی که لیونل مسی به طور چشمگیری ۱۳ عنوان به دست آورده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/Futball180TV/90283" target="_blank">📅 15:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90282">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZMVn6YWe3uDlsjKCPt1H469iSvqVsvHgWpYJS1rOt6-CtEvRWTftUVEYWvq49dbNtsnAu5sdwBpwyJyR8MhnE37pMmSCC6xaCPmHrJxX_2q3RViBaK4RBIks05r0N7HNpZ-j2DxTVydxdIL-VaK_5LkezCxv0LqMT0epYsAVvPBwHA08QJRFEq_0hs0pUXodNHyhAJSE2VVHyB3dvZJP9V9O2w3gnrlml4maY_ZP0vUxmF00umGQq2w1SVgOASR3CE4yDCv2_V9odvzDUtYinjDuQlD5DeWVA3GULK1EAEXhoignczJGvxUvbqXcUufZwMQk0xaMf6hzGF9il2GRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">180TV
🤩
🌐
دوست‌دختر جدید دوگلاس لوییس در عرض چند روز به ستاره اینستاگرام فوتبالی تبدیل شد.
👙
طرفداران نه تنها درباره رابطه عاشقانه این فوتبالیست‌، بلکه درباره عکس‌های نیمه‌برهنه این مدل ۱۹ ساله با مایو بحث می‌کنند.
1️⃣
جذاب‌ترین عکس‌های دوست‌دختر جدید این فوتبالیست در کانال ما قراردارد</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/Futball180TV/90282" target="_blank">📅 15:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90281">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">آخرین وضعیت بازسازی ورزشگاه آزادی؛ 3.2 هزار میلیارد تومان دیگر بودجه نیاز است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/Futball180TV/90281" target="_blank">📅 15:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90280">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbe3da6710.mp4?token=PyY4CFc5hOP5Jm2klbwah4LaQnsctRsXZNi5qAvB-QyjgFhcPx1FUFJWUWwq-FZ47CYViU_1U3vz9PxZqxR3JGsSdcjcTOM8u-FsyP20slkobce4b6R3RGuzJHP1ysSQjXPTW1PWnG1qJBCvOzqLbZ6jlUsB5QdW4zbZYDiX5xesbJwO3madtPj7AgN5wVPLWWYoN98flyTwX6OW5ejd9T5rYwOp4tpV4htgunCggjZ7OWEYN0DMNbTSvuGzp3-BG7QTMtce_EyFC8Gpuz1-5v1alHctItZSu1TL5yd3msOSiuoACumqk0HNvf1HuE5XinYyzsLd7JdJv8i17MKiAKZdghAV6N3RDlPEzggS7Iiw3H844wWcPuEnBKgIStn27tmDtFuSfGfa8ZIkYTNPrT2YIy1Qo8yPFnRnorc8xx-ruM-tooW-WGLZeV29ox8b4ybZT9dowdMTfRJRNOLjPNzV_gTZZk_ImfU-FvHq7QPOw1G0bRBN3L68h-T_shCnisYltGZRPfCZZObgmRA5YBsTQeiONmBSvxT29ii4Rws0q4v_DT2Rd66X4YCRdyRrwsxa4TElG-9sfeDt9l0VfDG4O6qMvjyZPvBiTN9HgCXWe6KSijWu9W_-6eOB8Qhzq43zoM2-h48jNtrOnjve9NHomwD1u3jn3SBLEFM4tI0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbe3da6710.mp4?token=PyY4CFc5hOP5Jm2klbwah4LaQnsctRsXZNi5qAvB-QyjgFhcPx1FUFJWUWwq-FZ47CYViU_1U3vz9PxZqxR3JGsSdcjcTOM8u-FsyP20slkobce4b6R3RGuzJHP1ysSQjXPTW1PWnG1qJBCvOzqLbZ6jlUsB5QdW4zbZYDiX5xesbJwO3madtPj7AgN5wVPLWWYoN98flyTwX6OW5ejd9T5rYwOp4tpV4htgunCggjZ7OWEYN0DMNbTSvuGzp3-BG7QTMtce_EyFC8Gpuz1-5v1alHctItZSu1TL5yd3msOSiuoACumqk0HNvf1HuE5XinYyzsLd7JdJv8i17MKiAKZdghAV6N3RDlPEzggS7Iiw3H844wWcPuEnBKgIStn27tmDtFuSfGfa8ZIkYTNPrT2YIy1Qo8yPFnRnorc8xx-ruM-tooW-WGLZeV29ox8b4ybZT9dowdMTfRJRNOLjPNzV_gTZZk_ImfU-FvHq7QPOw1G0bRBN3L68h-T_shCnisYltGZRPfCZZObgmRA5YBsTQeiONmBSvxT29ii4Rws0q4v_DT2Rd66X4YCRdyRrwsxa4TElG-9sfeDt9l0VfDG4O6qMvjyZPvBiTN9HgCXWe6KSijWu9W_-6eOB8Qhzq43zoM2-h48jNtrOnjve9NHomwD1u3jn3SBLEFM4tI0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رمزگشایی سامان آقازمانی بازیکن سابق پرسپولیس از علت اختلاف با قدیمی‌ترهای باشگاه: جوان بودم و خوب بازی می‌کردم برای همین از من خوششان نمی‌آمد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/Futball180TV/90280" target="_blank">📅 15:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90279">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7_BJmb0ABTb-aDUQFjvvcXEoEoZzQ_28-drbG7sjEN-PJOsNKAo-CGXDpP8UOZMCmBvTkOvdK4VkBbitMCo01zLiqlPKsvkUOVx83_H9q8iNv1s_us_N_jggmg7ymlpXL6nZ69iOsHO3UqGCwPaUnPVwiY-wfIZ3nivlr1vZn0WYxW77DNkADVHUBG67upnIw1DzjXQvbG2yphqFcmtKmFoHUK5byYBRvhFEL5qt8UJx0MnvKM0K8Db4drSbRXEBOQxBMkZTg-RfY2iUOiT6IcKkgkgeyThggiixefnomOZdDHqTmzU9pDpffZmT3BLGJmjfz6-kHbpIfk56G3-Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم‌های ملی که توانسته‌اند دو بار پیاپی قهرمان رقابت‌های جام‌جهانی شوند؛ تاریخ برای آرژانتین رقم خواهد خورد؟!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/Futball180TV/90279" target="_blank">📅 15:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90278">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cbec1c58c.mp4?token=tJzVN8U2puyDIy-d8yR_vs0Yd18qpj9LkHcQY9PLodlkLzQ5ti4ea4vsV31pkqkz4_ull27V6b7Rsd0cHgqiTiEbBIjnBZgfdbeCHu01An1mzdsJTCzmoaUKfF3p0IZSpz-mQXKZzb9QNnDkIcZ4f3c2HffsH1b4RtbKdAFGsy0EEV6IdhHvMh03jjlQgblvEaF-scAIIWSsNpWVJBjDcFTWPFLrKbSIqgiJKoxL49D8HBYlKwV0fxdfJ_fBqz4D6rsaf8_PK328EwZHHwV1GaFh1WUMKbUXkbbc9JHxgr_THJ1gpda_mEYhVgyquvnp1agETH4mwAi8slblQ955Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cbec1c58c.mp4?token=tJzVN8U2puyDIy-d8yR_vs0Yd18qpj9LkHcQY9PLodlkLzQ5ti4ea4vsV31pkqkz4_ull27V6b7Rsd0cHgqiTiEbBIjnBZgfdbeCHu01An1mzdsJTCzmoaUKfF3p0IZSpz-mQXKZzb9QNnDkIcZ4f3c2HffsH1b4RtbKdAFGsy0EEV6IdhHvMh03jjlQgblvEaF-scAIIWSsNpWVJBjDcFTWPFLrKbSIqgiJKoxL49D8HBYlKwV0fxdfJ_fBqz4D6rsaf8_PK328EwZHHwV1GaFh1WUMKbUXkbbc9JHxgr_THJ1gpda_mEYhVgyquvnp1agETH4mwAi8slblQ955Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد شدید صداوسیما از دستور پزشکیان برای اتصال اینترنت بین‌الملل!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/Futball180TV/90278" target="_blank">📅 14:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90277">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/083cb252a0.mp4?token=bMm5zKvi6CUrXm_3nxNs03WGAqZVzSe3rL7Yh4a1FFn9sSpescEPmB67dKyYM3bGK4tTVwQrCZ2vO_X_6mNpLjfoowK44jOLcEPpe6CWCKXOtbjIowx045yFrs8JtufZbvB4FS1ThiqUKhjDR0O-pw_WpY1wqUc6N0yAbEpI_oihxBBh-Pnc3cZXQfwusoseBukPTNfgg1Wer0DtmYFU4bRLfT2cFch6pz4wxH0oLQLEiljf9ZP2R8uJ7H5XM99sTTDFOOz-zChCkaolO7nGqGrNWxJUvT5zeb0scNv2LF9s0ylLIFT7gWRjxUILXqTuwmLetWLKHymG4K2SPUnXig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/083cb252a0.mp4?token=bMm5zKvi6CUrXm_3nxNs03WGAqZVzSe3rL7Yh4a1FFn9sSpescEPmB67dKyYM3bGK4tTVwQrCZ2vO_X_6mNpLjfoowK44jOLcEPpe6CWCKXOtbjIowx045yFrs8JtufZbvB4FS1ThiqUKhjDR0O-pw_WpY1wqUc6N0yAbEpI_oihxBBh-Pnc3cZXQfwusoseBukPTNfgg1Wer0DtmYFU4bRLfT2cFch6pz4wxH0oLQLEiljf9ZP2R8uJ7H5XM99sTTDFOOz-zChCkaolO7nGqGrNWxJUvT5zeb0scNv2LF9s0ylLIFT7gWRjxUILXqTuwmLetWLKHymG4K2SPUnXig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد نوری پیشکسوت فوتبال: سردار آزمون را ببخشيد. اشتباه كرده و عذرخواهى ميكنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/Futball180TV/90277" target="_blank">📅 14:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90276">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThkrgbjTwkYQEtBcqiAFVgbEFaWw7cUSmcXx5mkwCApxPaYIVXSvaIxHbkc7eq8FYac-hx7ylIFIyy_HhIXg7G8zWssaj8PD0UoaUpVH8aMA5tpHCViWSaScElCiYRnNcOjExQZ8xFunVJHd94M4hpxKA5r9HpDb3iCuR6LJxgBirHiOYZqRCX0-RLvqHbv72nQipQT4i1qcvFQ_wXOr9Fu-Z0rbDL5KLTeGfczElyZ2BXhNEh_RTgWcLi299ysYengs5gNZeWQc1sW3kT6UO23yXbumiim8r6cBdBj0H2yiN92I0N8d0Bi7DMXzvGSqFAvJjDE1XjEp7kBn6Ex94w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین باری که باشگاه بارسلونا ۸ بازیکن در تیم‌ملی اسپانیا داشت، این کشور قهرمان جام‌جهانی شد و حالا پس از گذشت ۱۶ سال بار دیگر ممکن است تاریخ تکرار شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/Futball180TV/90276" target="_blank">📅 13:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90275">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=QY_2vAYOKxGmLv-qZPRSgj_nPsoNCc-SG5FNlOvwTN1FxNvs-Y2P31NUEyBx59VTUU5oCzw0r87BraHD_YJp4xs-HbzRFmVqilCEBysLZgL1gx6UDaksQTRVa6Rt67jq9fTqIDhSZl_kOhE0_JMsrQKuMgdaP_3wmwraEvZrDUsPrLiWLOLV80PZuxGHHoim7jP3szUO7B0HhreU5x54YpDPzHPQg2M_PnHCDtbtcw5W0FPbZ_JB-IcKYnAHq-mSNZDvcITZqhPP_-QQ21NFFpWl3exVGZEZ4R5cpg7AnMEJcN7OdzdqS0j9jDY8Wv3ZvbknCJ9UgHtbCzLkOtLinQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=QY_2vAYOKxGmLv-qZPRSgj_nPsoNCc-SG5FNlOvwTN1FxNvs-Y2P31NUEyBx59VTUU5oCzw0r87BraHD_YJp4xs-HbzRFmVqilCEBysLZgL1gx6UDaksQTRVa6Rt67jq9fTqIDhSZl_kOhE0_JMsrQKuMgdaP_3wmwraEvZrDUsPrLiWLOLV80PZuxGHHoim7jP3szUO7B0HhreU5x54YpDPzHPQg2M_PnHCDtbtcw5W0FPbZ_JB-IcKYnAHq-mSNZDvcITZqhPP_-QQ21NFFpWl3exVGZEZ4R5cpg7AnMEJcN7OdzdqS0j9jDY8Wv3ZvbknCJ9UgHtbCzLkOtLinQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از عجایب فوتبال بانوان در آمریکا؛ بازیکنی باردار درحال انجام بازی🫪
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/90275" target="_blank">📅 13:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90274">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMolkyy4GZIjfMPJIci9P6Q9LZ1tJiiLuknNWO4jIjL-GbXhe9OjvSD-jc9gXbE3wBWJJP-_MJJa_0FafozdAloCl79QQtpnKtRbA5VwQWPDaeeeYNV90jPQxohp-fWSFwKpC9qWliCwDWD8Fay6BEojOzNvoDCJOWDhNq4Wgf_F6lpwJqVta3P6q8bJEV7rtaVeV2GCvQx0OdWwnxLuBypzR0m2aqI_FyEofsgtSkuo-xBY0ga5oIN723ExHt6QkaMsTnbjGR404PovKm5ZCVFUOOr4ghVSMopETtc5-yrbxCdd2OLlx6iVGy8AWwhGpfmsNqWrMxlkgAi9o7e1fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
متئو مورتو:
مذاکرات بین بارسلونا و نیوکاسل برای جذب آنتونی گوردون در حال انجام است. با وجود علاقه باشگاه‌های لیگ برتری و بایرن مونیخ، گوردون اولویت خود را به بارسا داده است. نیوکاسل برای جدایی او آماده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/Futball180TV/90274" target="_blank">📅 13:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90273">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rL2VHTcMfywk8L202XFA9ptpGQ9uPVhylLDsXgukp4HDV01_f6QztiR07l22KvWt6JoFrrGFHcFUVOtKB71NUw-shm0dEWVVzcKsc1rQRJjw4xsFwbe-lRghyJm1oI7x7g6FwZEPUv92eRCZw_LrHAGJycQtavPvS9hp8gB_Hnqjuwp1q-SJfEsNMYZZaT_4-JWy1_d36Ye4Xt1tafuXZzT2CPb258Pl-Moz95QGX-CK4csgOi_RhbTNIPsALyWWlznyYFkueUzfgX-nStWimnmeiKybWApClUcTlb2y4QfD36RZ58Dx83KEAzLo31ew4p8Qpt-RB2SzW00QNVUwIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین گلزنان فصول اخیر لیگ‌قهرمانان اروپا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/Futball180TV/90273" target="_blank">📅 12:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90272">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا #وینرو  بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io…</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/Futball180TV/90272" target="_blank">📅 12:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90269">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejZt9fe6UkoXe0Kamvw7y8LJCXY4jwHTYZXiuJ_2yZP5I3IczxHObl-QKQS7OzlDnc-EgT2jVVZKjwkuOzFzvRzL1byAyNd76UV9BYJQJb0rAa4Uc5Y8rCqQYHlDwYbXoAQCMsCvMg2JXanfeCrDfpbmL7AZPXZ8lW35t_W5nt5hoyWsRBKcFvCuZGe-KArGBd9MZZoJRfSoUNNVgJ6-btYdDKVVSyKQr9wDD2GnDJRzF5o8URgpRKKu0qCUD4HShxtlSvkjlqh2rAUGT91R6GdGKJLeMnkJfWosHYm1eZzee2GYxwy-qeivX8uPeoKTEJWX50JOxl-69mX2E2WXOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا
#وینرو
بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r6
📱
@winro_io</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/Futball180TV/90269" target="_blank">📅 12:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90268">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cf55f690d.mp4?token=mrWYiTgoDaY72J9di8zZkvULMffgWX3EPKobFxXZJ9SI0m4E3cKuxk42Kf838dPLVbEM9oM0F8VMudqgHrjumHIsXrA5-G2FRF9PPIsNt6JNMfXeGePPhL8_JmokmSRPcOc-oWzKPEQWHZhHdN-q-MTMKh1eF8HnKibLUPOXrnrFslEpk4v08XgE6lP1inIAo0akKUq0cKXYzcFybnTu56hXuBsykd9WfWMea6zA9eaPNdKS8x6GNP4Ns9nyKtVX0_Bnwvjm7_d1gd5d9BRJG5JLnK0IUaatN92pgBtw9ukwoTkMtaC_y7xwCpaB8VmfzyBRzdMwqP49YK8KD0Yl3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cf55f690d.mp4?token=mrWYiTgoDaY72J9di8zZkvULMffgWX3EPKobFxXZJ9SI0m4E3cKuxk42Kf838dPLVbEM9oM0F8VMudqgHrjumHIsXrA5-G2FRF9PPIsNt6JNMfXeGePPhL8_JmokmSRPcOc-oWzKPEQWHZhHdN-q-MTMKh1eF8HnKibLUPOXrnrFslEpk4v08XgE6lP1inIAo0akKUq0cKXYzcFybnTu56hXuBsykd9WfWMea6zA9eaPNdKS8x6GNP4Ns9nyKtVX0_Bnwvjm7_d1gd5d9BRJG5JLnK0IUaatN92pgBtw9ukwoTkMtaC_y7xwCpaB8VmfzyBRzdMwqP49YK8KD0Yl3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اظهارات تند نیکبخت واحدی: افشین قطبی کاره‌ای نبود. چرا در تیم ملی نتیجه نگرفت؟ قطبی ذات قشنگی نداشت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/Futball180TV/90268" target="_blank">📅 12:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90267">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98d2b87299.mp4?token=S8QvqawS2cO6n-_SDB_yzUmn6AEPON28vKCocAlz79L1O6J-28D4wT4lpzhRzirAMd5u-BuoAJQqL8luwXfpLohKhZpVceQcr-C8oVyjb3Jac4Evwz0daYsfnJhor3okzB4r9f06cCiYkbrwEKsD_Wd1xjfPd0XrLD-lsIsl9qey_LmRa4Q32pyCnJ-wRPoVImnLK2-Yo85fJlV5ZI_YEV8FiDIaYO1dYUtWSZniz2HnR8Tz9xoAwdH_JCXvp4Nz5X0hcT9ql7xEAHPQYDWtdShvpijaKwVFdqaA1xlFYws-40sTbk0x5WTdfCUPiIwLWccdLQ9L0nOhBacsytswAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98d2b87299.mp4?token=S8QvqawS2cO6n-_SDB_yzUmn6AEPON28vKCocAlz79L1O6J-28D4wT4lpzhRzirAMd5u-BuoAJQqL8luwXfpLohKhZpVceQcr-C8oVyjb3Jac4Evwz0daYsfnJhor3okzB4r9f06cCiYkbrwEKsD_Wd1xjfPd0XrLD-lsIsl9qey_LmRa4Q32pyCnJ-wRPoVImnLK2-Yo85fJlV5ZI_YEV8FiDIaYO1dYUtWSZniz2HnR8Tz9xoAwdH_JCXvp4Nz5X0hcT9ql7xEAHPQYDWtdShvpijaKwVFdqaA1xlFYws-40sTbk0x5WTdfCUPiIwLWccdLQ9L0nOhBacsytswAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اسپویلِ بازی آرسنال و پی اس جی.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/Futball180TV/90267" target="_blank">📅 12:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90266">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99be172cd9.mp4?token=sm1bEC9RENAiixs2J0u_9GtXdOcgb6-QbG276IijDwFFlzzcOStJwDOke-SEDW-_IRDsI1elhXDUk498C8VR65GNVzLkVtcEiGa3UtD6NqP_fwSZF8vkT8F5iVHsQ_7AVIg6dcvpFUJLOsrHEIi49AKLElctYFi5_0zWzF5LV2DPKlhx4Xr87HjpToWhTI1jiPo5f3_lFnLvKyhtnajEzpIXCg_JeAiUPrQWksfh5SkaSGtWj9s_-6CVDBv7WUY_eNboCZ84GXOyccw6fDm01t6Pnlno9qxncXQfel9P5dAwqQS3Yj97czsi8YAWu41YyIBRpAPkXY7btm-90-Ql6gUKBYPzHV_Y1fwFhy9ktEXQukn5Yr7q04xwYOC9pMS83jvg32rTy6NoEuhTJ05QLRWfdu_r4y569RJ6CGIwQOupslSXD284n-PnvzLTfXILvXiY5i7xDIgehL5FS-2sFmCmM55cJNFDvWHKVmnWKC5KcA4uChuPErv1qT_VZlv33CmtjIEC5R0_qBe9Yta7mBgegrSnynbcfSJSVWbkVOjdBBfMxG20DYwuqv1spEQXRIQ3NZwWWhx4AWM3wE-tIXwCkmVZKpBC_TMmHcqPzikbSXKD1HC1FuhVWWfMISUxbxP9eQLrLM7M06GZo4AlWohrwUXH1mU5rARcHZ3pLNU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99be172cd9.mp4?token=sm1bEC9RENAiixs2J0u_9GtXdOcgb6-QbG276IijDwFFlzzcOStJwDOke-SEDW-_IRDsI1elhXDUk498C8VR65GNVzLkVtcEiGa3UtD6NqP_fwSZF8vkT8F5iVHsQ_7AVIg6dcvpFUJLOsrHEIi49AKLElctYFi5_0zWzF5LV2DPKlhx4Xr87HjpToWhTI1jiPo5f3_lFnLvKyhtnajEzpIXCg_JeAiUPrQWksfh5SkaSGtWj9s_-6CVDBv7WUY_eNboCZ84GXOyccw6fDm01t6Pnlno9qxncXQfel9P5dAwqQS3Yj97czsi8YAWu41YyIBRpAPkXY7btm-90-Ql6gUKBYPzHV_Y1fwFhy9ktEXQukn5Yr7q04xwYOC9pMS83jvg32rTy6NoEuhTJ05QLRWfdu_r4y569RJ6CGIwQOupslSXD284n-PnvzLTfXILvXiY5i7xDIgehL5FS-2sFmCmM55cJNFDvWHKVmnWKC5KcA4uChuPErv1qT_VZlv33CmtjIEC5R0_qBe9Yta7mBgegrSnynbcfSJSVWbkVOjdBBfMxG20DYwuqv1spEQXRIQ3NZwWWhx4AWM3wE-tIXwCkmVZKpBC_TMmHcqPzikbSXKD1HC1FuhVWWfMISUxbxP9eQLrLM7M06GZo4AlWohrwUXH1mU5rARcHZ3pLNU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاسخ شفاف سهراب بختیاری‌زاده سرمربی استقلال به پرسپولیسی‌ها: فاسد نیستم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/Futball180TV/90266" target="_blank">📅 11:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90265">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNDnq0wzrNdDzTYnBlLOoMvXLbMGTsUhKckiepBlnS5Ja_tiV22vy-xtKvxN_kd3MGwu2hgSgdmCCaA4jddlmWSdQw2Kj6IuFnPwwYU8m3drYZMRiyXDdSb2cC5ntsrIhMZ4TjqXpSpsXMBiLjxBKU-qZE-Q8mXpvsy1g3jL8yv0vOHCg2WL_8DiX9QFn1KWIus1230qFc8scyJ1d3UtP-7Nnp2y9dyRY0cB7lnSMx653yu7TdrrPLZ3af6H8RlZQ7FLSMSh64IIQ29GHvydhF-dFM5WwP9SIGhwQKJCZNkd1GB18UetuColLSw51QXX_mq1QHSWPrSUX5xaQpkAdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
به گزارش رومانو، باشگاه بارسلونا بدنبال عقد قرارداد با آنتونی گوردون ستاره نیوکاسل است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/Futball180TV/90265" target="_blank">📅 11:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90264">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/426e74bc07.mp4?token=ot9F94mn8WicqtB02S7skhFNy_1cpUJnroCxlM6iW7gwPkklPS6GpjxAcF9jTfOMHkHZxQfB7MMCPu7bS2HN4yMNtOe55djHS3oDWhtaAuqrJ1241vxiMzNC5B93qw6hH-guhubXMI8I9Ak5NAUao0bVPohJ9vZr9oNgfM6_56BbH6nKCQ73r1BkgATK3uV_g2rJrn4hrxF8yZqer6NRIG836ITPqMed5rBdC6AbUUjvpabEpJUYMQerjNOkNX4tOtq0C99XkzFbyDhFih-jgtgB9dUmu6qqTSP4hJDVdLRzFVtkroDiMm6XQJP6hkTv4x5tWBGsrVcpNU3l_djtMCKfiM6Mj_s2MuLSH3mNebvIFtOI9Pm4gQiQE8SS6-rTtYTLUsfppu1Jg7dFnrFW-bQblD1jHQ9WbReeNSu94rH5XWdZPGvPPdGXJyQNxC8bkhNvImMKQw4RvT6DKoR9Y9ho0vXqdQOX4pohFGCWNA4R40IxKJ89OHYCHIgNoqjUS-Hox6JB9xfBSWYQtRkmOblk06oQvYGlhd14gL5Swat7_3bq6gPyGgO14G0G__WHyglr2CpCballuGABXpy3SH4tD7QEjKrW_ZIB7UKi4oqGgxNRWxLu0FkePS4HJYxj7Nlou2UqdrAV0E4Q1N9-VGqRibjrlYAT82inT-IuEwU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/426e74bc07.mp4?token=ot9F94mn8WicqtB02S7skhFNy_1cpUJnroCxlM6iW7gwPkklPS6GpjxAcF9jTfOMHkHZxQfB7MMCPu7bS2HN4yMNtOe55djHS3oDWhtaAuqrJ1241vxiMzNC5B93qw6hH-guhubXMI8I9Ak5NAUao0bVPohJ9vZr9oNgfM6_56BbH6nKCQ73r1BkgATK3uV_g2rJrn4hrxF8yZqer6NRIG836ITPqMed5rBdC6AbUUjvpabEpJUYMQerjNOkNX4tOtq0C99XkzFbyDhFih-jgtgB9dUmu6qqTSP4hJDVdLRzFVtkroDiMm6XQJP6hkTv4x5tWBGsrVcpNU3l_djtMCKfiM6Mj_s2MuLSH3mNebvIFtOI9Pm4gQiQE8SS6-rTtYTLUsfppu1Jg7dFnrFW-bQblD1jHQ9WbReeNSu94rH5XWdZPGvPPdGXJyQNxC8bkhNvImMKQw4RvT6DKoR9Y9ho0vXqdQOX4pohFGCWNA4R40IxKJ89OHYCHIgNoqjUS-Hox6JB9xfBSWYQtRkmOblk06oQvYGlhd14gL5Swat7_3bq6gPyGgO14G0G__WHyglr2CpCballuGABXpy3SH4tD7QEjKrW_ZIB7UKi4oqGgxNRWxLu0FkePS4HJYxj7Nlou2UqdrAV0E4Q1N9-VGqRibjrlYAT82inT-IuEwU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از اظهارات عجیب شیدا یوسفی بازیگر گمنام سینمای خانگی: در کارخانه پدرم، روی شمش‌های طلا راه می‌رفتم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/Futball180TV/90264" target="_blank">📅 11:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90263">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b5959b18a.mp4?token=OUuZlq9Dx7JCUPKSY45nUUf0wX-6O0m1QCVnyNMycZ8OsioYpMsyEJmcmyIw5imaj3PH3KZB5vkIHnoqVJ4zBPyqzMPc10AD8xRzvvWiDDB52UQsEit_UVNshhEFi9Koh8znn1MtGu6X7XORuEH445G_L2nusWDpNx_-P1sbcHuHYKe-soaXQs9G4nLejwThBUcq9nv6jALU1Aua5rIa7MtzG5h2x8XXJWa0rN2ZsakQjrVnbLOK_R_6MA8PJIvR0AhPhoqjiTXRI_u17ovQxlvpEQ76N2XExs_hK0A4uwD8l1N3AU9ilBTted-Z7KHFHy_YUVGtQxMRnAuzJ5_hcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b5959b18a.mp4?token=OUuZlq9Dx7JCUPKSY45nUUf0wX-6O0m1QCVnyNMycZ8OsioYpMsyEJmcmyIw5imaj3PH3KZB5vkIHnoqVJ4zBPyqzMPc10AD8xRzvvWiDDB52UQsEit_UVNshhEFi9Koh8znn1MtGu6X7XORuEH445G_L2nusWDpNx_-P1sbcHuHYKe-soaXQs9G4nLejwThBUcq9nv6jALU1Aua5rIa7MtzG5h2x8XXJWa0rN2ZsakQjrVnbLOK_R_6MA8PJIvR0AhPhoqjiTXRI_u17ovQxlvpEQ76N2XExs_hK0A4uwD8l1N3AU9ilBTted-Z7KHFHy_YUVGtQxMRnAuzJ5_hcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی صحبت از مهارت و دقت میشه
🔥
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/Futball180TV/90263" target="_blank">📅 10:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90262">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gy3oCbMvtAicqOQiVumkDXnFA1YQlB08V1qa39G8awWl1_rexeUGL_IjiCz2BOEd0UiwPog1DZ_HYHslybbj1JrsjOraYu0BAJ62B0dpdbqIOanit1AzaRFd17jU2RkiiGzrvLLbNwakUgoDdqJ4UbIovxwmiD1P0h1Fywv_qoZcr9xF_UgBrdjwxv5I1XY9rDAjCFUxziTOs27nFBtWl5xijT-gi6yEXYRYzqbEGwC-LyMkgmZhIiPqoQcZZZ4D_Owvpt6VshyTntuNH-HGnN5FFgIEUEdJlTMWD-nm9okihxHWoYXULZDuJkybJFeh8Y_LK1wDv7HCSSlKAJnxIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ترکیب اصلی رئال‌مادرید در فصل گذشته هیچ بازیکنی از اسپانیا فیکس نبود و بنظر عدم حضور بازیکنی از این تیم در تیم‌ملی اسپانیا برخلاف بارسلونا طبیعی است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/Futball180TV/90262" target="_blank">📅 10:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90261">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d64b58d74.mp4?token=eKcavSO-R9I4VQjH7Gks-yOmiNR1EvkfYp6KqWHHO5V4beVHxtyml5OsDgPhbelLhms7ySWQK0anBuieQiGV_USZ7taD-1-vJ96kfT7m6dgdcfLUL_euSsU0VfMynCNKHUDKjsHa9yJMPzJ8lMTp1lqc09CuMAaMUPdEXU2JHdMpSMRGOnyhbemMwKOJZyv7ER-KojkO32QruXHUlLE9ittdjtBk703UvVKloNXzxTfh8c2kUM_Prc365-U2Y29TnVC96sTV69WbVjLLmzdpRhX1EU3mllOeo1Afj5mzXuFPqhC9X8KRMm0yyIjq58wkxcBlbZUydaKYNxNzsndBSIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d64b58d74.mp4?token=eKcavSO-R9I4VQjH7Gks-yOmiNR1EvkfYp6KqWHHO5V4beVHxtyml5OsDgPhbelLhms7ySWQK0anBuieQiGV_USZ7taD-1-vJ96kfT7m6dgdcfLUL_euSsU0VfMynCNKHUDKjsHa9yJMPzJ8lMTp1lqc09CuMAaMUPdEXU2JHdMpSMRGOnyhbemMwKOJZyv7ER-KojkO32QruXHUlLE9ittdjtBk703UvVKloNXzxTfh8c2kUM_Prc365-U2Y29TnVC96sTV69WbVjLLmzdpRhX1EU3mllOeo1Afj5mzXuFPqhC9X8KRMm0yyIjq58wkxcBlbZUydaKYNxNzsndBSIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهترین گل‌های فعلی در سال ۲۰۲۶ فوتبال
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/Futball180TV/90261" target="_blank">📅 09:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90260">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26b4bc8543.mp4?token=nMc_Gikoq9ouO3MdhYKTjxHEbD8q5smHrHTSsfw7SLUQ20TZa7DWTPFdG3Tk95P2m10zKwdu43LnOcNHr-r14YzDjuEDfFxTe5L3rBzc4Od9R9cp3NjCHCxCsHX2MdggtH6AojdfmkRtFiSs87c3t5PI-q2DRGJvTZQOHjxDWe1Fwp7eNUQvUveVMGTHokScevakAAzD2bXH_k66jdv1NnwSFaT91wPT1TloAHAT4DrHHOstF1TvAo2SwTES92HKC90vzSeyeXIVEbo-UfhLTebvZSWvwyS_Z_91Hflc2WjW573b8fDTO8AQiMGqwDwqse9-NVIcuUWq6Vl2izx4Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26b4bc8543.mp4?token=nMc_Gikoq9ouO3MdhYKTjxHEbD8q5smHrHTSsfw7SLUQ20TZa7DWTPFdG3Tk95P2m10zKwdu43LnOcNHr-r14YzDjuEDfFxTe5L3rBzc4Od9R9cp3NjCHCxCsHX2MdggtH6AojdfmkRtFiSs87c3t5PI-q2DRGJvTZQOHjxDWe1Fwp7eNUQvUveVMGTHokScevakAAzD2bXH_k66jdv1NnwSFaT91wPT1TloAHAT4DrHHOstF1TvAo2SwTES92HKC90vzSeyeXIVEbo-UfhLTebvZSWvwyS_Z_91Hflc2WjW573b8fDTO8AQiMGqwDwqse9-NVIcuUWq6Vl2izx4Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحید قلیچ برا خودش عالمی داره
😂
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/Futball180TV/90260" target="_blank">📅 09:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90259">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4b0e0df75.mp4?token=Cxq8hekgOaieQWo78Gl1YZB4jgA1jbM4iGk9JJG9vh6gVIWUmzG8CJKxTknFwEUz9mkebxdmjfG3XmvAN512k94Zs_otzFBhT91EeH9nvpUkaV9Nc4pmDPjwtZUmG1lwjF-Df4u-FZABGO1VRBW976l1zpxPK_TmwOi-1DMt_AuBspDgmThFeytFnuoUVohpepm3nU18u5euZOTGKGTywz3S6hQzW726NKtTsxa-Z8Kt7HoTWAhBQtIJBN4g8hfKtePINJrjuSK9OsOkqomtbv3EJGyI4Wfln5TMQcba_UTpIKzjpkZPv76rTmADDJ7vXERxP5nE55sA45R8iD96dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4b0e0df75.mp4?token=Cxq8hekgOaieQWo78Gl1YZB4jgA1jbM4iGk9JJG9vh6gVIWUmzG8CJKxTknFwEUz9mkebxdmjfG3XmvAN512k94Zs_otzFBhT91EeH9nvpUkaV9Nc4pmDPjwtZUmG1lwjF-Df4u-FZABGO1VRBW976l1zpxPK_TmwOi-1DMt_AuBspDgmThFeytFnuoUVohpepm3nU18u5euZOTGKGTywz3S6hQzW726NKtTsxa-Z8Kt7HoTWAhBQtIJBN4g8hfKtePINJrjuSK9OsOkqomtbv3EJGyI4Wfln5TMQcba_UTpIKzjpkZPv76rTmADDJ7vXERxP5nE55sA45R8iD96dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
همسر ناصر حجازی: به او یک میلیون تومان پیشنهاد دادند تا گل بخورد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90259" target="_blank">📅 08:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90258">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">روایت قرارداد نجومی فرزاد آشوبی با راه‌آهن در ایام مالکیت بابک زنجانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90258" target="_blank">📅 08:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90257">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">Soren-VPN.apk</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90257" target="_blank">📅 01:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90256">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Soren-VPN.apk</div>
  <div class="tg-doc-extra">62.2 MB</div>
</div>
<a href="https://t.me/Futball180TV/90256" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔵
فیلترشکن سورن (اندروید)
• نسخه 2.1
برای اینترنت ملی و بین‌الملل، عملکرد خوبی داره.
وصل نشد، مجدداً برای اتصال تلاش کنید.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90256" target="_blank">📅 01:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90255">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WC_BZWJHjzewVTkWMHUmAS2n8rP-0q62bsBp159j7wt433Tj0rg2ON7DXjivCf97YKKUBCWwkENb2jVrVt24mxQBytylvUpsn-dAydgu8382hcz7b9ZXolgqB9jEReL3xqCH31A6XduxPCkexEB6qkjdWx-13oke12Vw8VYhsD-HKkbEXHPg_DmC5EvWJCh-gQcxyKHCi5kxLjFZtNNba2vTXxC6bvo6enJ-CBnYOCrHtdu_i1ayKOmW7wj5AwcRxB36BGvBuMYn7c3cUiLPsVRjY_4azu18nlZyoABJNjTprUnSVxNWQ6_pnwCorbMvOM4pSf_9kutFD5jkaXAOXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکل آرتتا بهترین سرمربی فصل لیگ‌برتر شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90255" target="_blank">📅 00:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90254">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔥
برترین گل‌های این فصل سوبوسلای در لیورپول
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90254" target="_blank">📅 00:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90253">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQ1Wc6hTh43gpUDg-9uJ6EW_H4kxl2OF6PsA88du90T00cAuUHzAS13NGBbjef1Li1WeibPMek_Xr273urU2nlOCNHiOv0jS8-HbyFB0VP9Td6Pg9hPebjCdQWrA-Q6h7cvFLRAytIng0mIfmDhcINCXCqGkjF5yCw78gse3inJuATziuVY_lGMPoF19zppr92rsX7G9QinXVF5XPOQQnoulSUgcfmxhYrX0AYxCELuHRZBNC_SAj-nseBHAT6szUwlshtINVEsHDm3mDoZVexQxF2cQQuNK0Vp8x5CyOiChaRgtOrC_6I4JrhLte7zWXWVjn3O7A562bSqZXGBfDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الکسیا پوتیاس بعد از ۱۴ سال از بارسا جدا شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90253" target="_blank">📅 21:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90252">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea61c87680.mp4?token=scyQEwH5IMRA5eKABOyDUZUyG9_qv9xKYAgywVbuh_OejTGbn8sUD0Y9IOafsCsVPATc9YsIg8yZ3TbM3QiLnukYHACsaHDIjjwEFHc9nid0IILvza4VUk1RrZi3sdQjwTdgBhumcVPhSY80CU96oHn76vGoE2hUI8axz5-TK5WdYsWNwSh8bam9jW5XWrcl7qwzt8DnmfzEmKhrxAR4AX77cZfEFCwN-70JGa-0H2jT4S98jhSN8Ie9DW2mTFT1fnHObF6F_Ju_-wlv1KsDQurk1IvH1cP20wGU3ZtqBK21ae1JdtiZlR90eDFrVhq-KH42tdJ4pbpWZmGEzGKebw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea61c87680.mp4?token=scyQEwH5IMRA5eKABOyDUZUyG9_qv9xKYAgywVbuh_OejTGbn8sUD0Y9IOafsCsVPATc9YsIg8yZ3TbM3QiLnukYHACsaHDIjjwEFHc9nid0IILvza4VUk1RrZi3sdQjwTdgBhumcVPhSY80CU96oHn76vGoE2hUI8axz5-TK5WdYsWNwSh8bam9jW5XWrcl7qwzt8DnmfzEmKhrxAR4AX77cZfEFCwN-70JGa-0H2jT4S98jhSN8Ie9DW2mTFT1fnHObF6F_Ju_-wlv1KsDQurk1IvH1cP20wGU3ZtqBK21ae1JdtiZlR90eDFrVhq-KH42tdJ4pbpWZmGEzGKebw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش ناصر حجازی به پیشنهاد گرین کارت؛ آمریکایی ها باید به دستبوس ما بیایند!
همسر مرحوم حجازی: وقتی بهش پیشنهاد گرین کارت آمریکا رو دادم چنان فریادهایی میزد که ستون خونه می‌لرزید!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/Futball180TV/90252" target="_blank">📅 21:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90251">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90251" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/Futball180TV/90251" target="_blank">📅 21:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90250">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsdud2iD7J4xL1sXn8G02O8bPwrUgO33VkEPqwf7JJ3XPcEmYXU0Cm7Y7CXw2ETk__tECJMh6Ctg8FvC3oVW1z2oevUuEKEezfx6WtTgc3oD8eSFP1fZxD2j-tVFDR2ZN0zAq3_Xar-KPSB_iv6BlRBpDH8T6rjA1UMLCbkhGcZwkjwK2Bo33-Jg-lGyW3y3moCfebmbc-dInyDk3gzcOtqthTCr5OK_yHUWbFKNkGAKFiUQJMj9r6PtHWmVPUxjlIGoXnhId372AYP9wvhJvqIYYDnq2_MB1cwPabDcgmQkmd_TWjOW4IppBL1RDfSwZ52trB36DOJF0fn_7E84ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤑
پروموی Crypto Freebet
🤑
💠
حداقل 5$ با ارز دیجیتال واریز کن (حداقل 5 بار در هفته، در 3 روز متفاوت)
💠
هر دوشنبه
💎
یه پروموکد می‌گیری برای 30% بازگشت وجه از میانگین واریزت
💠
سقف بازگشت:
💸
تا 300$ در هفته!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/Futball180TV/90250" target="_blank">📅 21:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90249">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baad93a3a8.mp4?token=cjKE28SgYNSIPsTJ-vx0xOBUQYyLAHLHwbabq3brCjTf5yvulJrRw7bWio-o9AHpW9_6XMgeOzUfpirNgXl9TNYraG8fbsro4gIllGIB4jn53JftERilsrrSxGuzh5-pnOTE-sDecvdY1VsU8bBco4y9n8ECN7nmz6MfMglvmtmA1dFcZRItCIQDjIJCQagywBQoHAuzbxlVkuyFH-SAbbRkS71MHQmJ5fGguXklKETn2iF2OMO-b3nOsqgtSfc49qXLTNfW_PQfYJQiJzjaCg5qYwJlJKYFByWeNko8WfVXIJ7SwyVU0FXUrfLHSOes-lIBwHiRyzIpv-rgno9sqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baad93a3a8.mp4?token=cjKE28SgYNSIPsTJ-vx0xOBUQYyLAHLHwbabq3brCjTf5yvulJrRw7bWio-o9AHpW9_6XMgeOzUfpirNgXl9TNYraG8fbsro4gIllGIB4jn53JftERilsrrSxGuzh5-pnOTE-sDecvdY1VsU8bBco4y9n8ECN7nmz6MfMglvmtmA1dFcZRItCIQDjIJCQagywBQoHAuzbxlVkuyFH-SAbbRkS71MHQmJ5fGguXklKETn2iF2OMO-b3nOsqgtSfc49qXLTNfW_PQfYJQiJzjaCg5qYwJlJKYFByWeNko8WfVXIJ7SwyVU0FXUrfLHSOes-lIBwHiRyzIpv-rgno9sqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ازبک‌ها آماده حضور در جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/Futball180TV/90249" target="_blank">📅 20:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90248">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FnssZXpvfiT_-Z8YwIujw3cO3BXS_Cz5uQZ3Jqq-4_w8irOHi4cjFnxRsl6vyKYse52njTJHq5ZQc0ZVfdjpQqhFjv7Eqh9BHqbfhVQ_AmbZzxLyeJlq6W8mf80XuBD7JYtjaXFhVvPWqJR72DgfdWXDDWWxvNVmsMOPo3Th1txvR71QwUPCw54_S-FALSHi1PNE8RHsZ7WTnCcfjF_a9PIJhTHVc7r_UZFbknz0g-8H2ncUpoBG1AC9xZLNnYxW1YwRnIx8rWy-GRLlHTmEClbXP3zHZ2T2FYLHsnKmgIAw8JT3UchFJNRHU6BkaJ0yWGnxFDhe4dVvNf_eCuf0Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با اعلام رومانو، قرارداد آنتونی رودیگر با رئال‌مادرید یکسال دیگر تمدید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/Futball180TV/90248" target="_blank">📅 20:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90247">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🔺
دسترسی به ChatGPT روی خطوط همراه اول و ایرانسل برقرار شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/Futball180TV/90247" target="_blank">📅 19:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90246">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orpa7gMzHwdSY-3nWIZNopMXDoX50SuX0Jz3sUdJJDmAGLuAmP4Vm0UfTUDCmhnxoCzzbdIm9i7ts6_JvikiLFsMR_-2zRZ_wvN_Og9azK4-llrg43K3tjDGVdKTno6jYwRoKwUwXzNtJXR6jgXoiCMXMbCcFrhV9qIJ2-6RN2fxd5d_T_uIaAOrhR29gYdJ647Sgf-gbuxRwFXYkNwsqqa9NWLZohSHPzkvaBko5fK6Fd6PVZlRzBmZQ4rX6KUfcToDm63Alqphb9xqO1Go9cFdlm3g-x2KkAwExGy_oLoo4r3l3rDkk2L6SUfmwGWQbo-hdApMzzz6crVw_sPWgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سیدبندی فصل‌آینده لیگ‌قهرمانان مشخص شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/Futball180TV/90246" target="_blank">📅 19:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90245">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">تا ۲۴ ساعت آینده سطح دسترسی به اینترنت به حالت قبلی برخواهد گشت. درحال حاضر اتصال وای‌فای درحال بازگشت به شرایط قبل است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/Futball180TV/90245" target="_blank">📅 19:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90244">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">تا ۲۴ ساعت آینده سطح دسترسی به اینترنت به حالت قبلی برخواهد گشت. درحال حاضر اتصال وای‌فای درحال بازگشت به شرایط قبل است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/Futball180TV/90244" target="_blank">📅 19:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90243">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVmUpjr4YiDw4pj2Zct6hFHpdlch2HbEA2h5ekEIK1gAvwzQ0KxQLldlC7Rb_9Ff8mgFfecQCDZ3kxJF9etl5zGx0Rb8-Cek_0RtCSiY8HS1X_nsAWqWIdS_yXXNpMmFV7JrKEuq5HuYSY_IFxJoDvZ9IuMMw03RxWvI-mH2TeiW4PbUMgdj8YKYeW5LSW9Ghrl6PQcFRmLLiBk1EZ1G4i_N-cfyHi7pP_TPdPMAlq3-TBfj_ewRqWn0NnF3JJFB2b7O86jJ9to8MaYiqqd9RQk9r3qRHZoq4CgB_kWyUDJam-5iIzUXBsDzyhsV2i4ZO3FAYwQnLlKhr6odokE6Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توپ‌فصل 2026/27 سری‌آ ایتالیا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/Futball180TV/90243" target="_blank">📅 18:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90242">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SF7DTAQ0Zb2xL1KWU7p8oSnNf8tOAph4cZyKMMTkvEcBEhG08x8M9LROKqOnboglHoq3qXrU2QHngQ3Od9UMely5rrQcplcGA7if452_6rCWXUumU-GNPg6V8a3Jsuqlhwf5rQp4Vv4D2vulairCwiV5JAbwC1uefrTbr2vWE85X1yMEyH5T5N63oinqhwfrEhB_axU5Bqu1-u3EP0N_fpH8jLnjRJSwOL3PmffLCJMlZN2dduYQ_4mEJVwrnhvXbNHBwzjp8vM4rXIZom5LybXBSVALxsJ_srMhU1xyrV1R5GE_j7Ne-2U3myJrxUzPzirvBZkprBuOWEu6MBsHXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توپ فصل 2026/27 لیگ‌برتر جزیره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/Futball180TV/90242" target="_blank">📅 17:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90241">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSFbYEdqBLJz3IY6doknWuT5b8SQQbMhgxTWQuq8ILu80yAa7wRIEY1lbcXnIWIWysdLD4-QQVBtot_kjqwSkP6Lxn1VURUlbcV06Z6-uCKIeSC1L2HB-l_unw2asxJVWYS_4cItuPH7qKyk7x03bUweFPmzH7NmPl0KLG8b6uWFUtxIyySRg7fW6xQA8iArqzknmDZWUY-HanZMkpkpwl9iV7NSUlZBVxvWdL3c0l5x5spPtNF-sIyD8UxZrRMh8Ij5m0M0T2dJfS6oMfCk6AbEGWHMeg_GTGG6jg3X960cmpKh2MT0O6W-T5wu1PBFA6a7DDh3SzPjTwvi6K2yYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باشگاه بارسلونا برای جذب آلوارز پیشنهاد پرداخت ۱۰۰ میلیون یورو + مارک کاسادو را به اتلتیکومادرید ارائه کرده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/Futball180TV/90241" target="_blank">📅 17:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90240">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JU5zq-AbkKy8ZK3XuusYk7hj63dL3nth46YrPMkLx5dXc5KbaqO2btwfiwh_q0b4k7pSRoEWayACD7uCJF6y5tSpYPJrwfH9bBwWFzDz7BrZ9m4vcU1gUG0d8_QK5xJME6Uk504pBeW9JHhrYwKcaZtABdaanaLu7-yCSBnpAVqWeiTc-CjqFUdNpxhoNURijLVmuP0NZ53sr0LpacfKuOnaM3NPv1CO_h5jGh2V0jqZNT7ybGtLvqmcC8VwtQ8N5HldoZ5D8w1_RJjVZzXF-Qol6aLCxc4uN-BBcHztG9wdRZ3p_f35xtIrk04i1lEfbuGej_enqFduNpVMGHOk_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۶ ورزشگاهی که میزبان بازی‌های جام‌جهانی هستند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/Futball180TV/90240" target="_blank">📅 17:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90239">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Our8ib19l2L-xpA8yEP4r6gkTFgUC_2zlT3sJUf2wB_MfL34cexqJQp4rFkvbqnw9053SN_cl9J1mhoZ1sRU8OhVw4BpUYvs-xTL-LQECwWc6ZTB6E7jTFqt6-38xIEbNLXk66qC6NuiLJhxPuNoM8wZmdU4TfV1gkWlJzeaJ30X8jACIp4E8YxHeACxswQcm475xvkCtQwAQHOwXfSpyQiPYVTiGvtg4xf4JVQsr77wq2qsU8eiars3GQjKikTcNrSE1raSZxTJWqPT-D9OjMCMdBVjj5CZwJxczY_YVAiCfVZM536wokoODoJuCfBkrCvbrmS7sWGVDNQ2K6taKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
محمدرضا عارف معاون اول پزشکیان: اینترنت بین‌الملل در دسترس قرار گرفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/Futball180TV/90239" target="_blank">📅 16:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90238">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">مخصوص وای‌فای :
https://t.me/proxy?server=87.248.129.199&port=25565&secret=79e344818749bd7ac519130220c25d09</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/Futball180TV/90238" target="_blank">📅 16:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90237">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gt22KubXEbkPMAALPYbHn1ggJhdvj7j0l_gzXW194HGSPHDMVyfKPXOzQ0Jw4Hlto8BPyzoAPkpTmV0J_Mtp9pcEbT6ypSQ9LqxLNoPnx88igG4jM30HhHI9wo6-MVEWnihrMriK3rU5hL4cgyH557pc9UOZKbAQ62SzguorNgMS_j65Y0ldlNZbiS8Kk5NBqlC1K3Tka6zImU2JlF528wyVDkWAXKGSiCP7YU2ApIkFEyFFEqaDHiZ9CCCPCzXRrmWc2iQ4Hw4KZznU7tsQFBAPVMByYF21190M7fjir12Na4yFH0ScUdwOQ0hFNnvkeeeouIN-tLpVMpx9OO_faw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نت بلاکس: نمودار زنده نشان‌دهنده بازگشت نسبی اتصال اینترنت بین‌الملل در ایران است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/Futball180TV/90237" target="_blank">📅 16:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90236">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7Iu9c-jV9NQvZ3IllAmVUHQrniXRbPw3Ifc_tnNCMLo42BkhFGprcrzgFMbkA4v9F7_0pW3pNs3RfOblWDU7rhCpvmPsiOg0bz8n-y_IgHwJN33cRXc15tD6C68fIZfbSTu2Soiwjb6AI-AsIoqwjnBPNrr1i_uQ6IO4_bBxht5bXiosCX0uvtYmytbqcke6o429wjlEhaALdl2Gjz1h-Vndbgx6sk8Gpoa2Ojkz7fHWBdfNZ-ER-DWeTOW-fou5m4_GIDzt0U6NAD0mjhKBmiuZkPo19QAcSu3NGKaAQuEMjMFo2Gkx133RSGKXE_uuyGx0mlRTocEP73xBdSdNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور خوسلو در مراسم خداحافظی کارواخال؛ این دو نفر باجناق هستن و با خواهران دوقلو ازدواج کردند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/Futball180TV/90236" target="_blank">📅 14:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90235">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzR4rP72CeKTCjCz3ZmFsWOOOA7b44xBMND1AUcprLB0o2WOuCxyd6CtLfpa08eIDjq10I8Kj157ivhqb-yiJX37o9vKuW_1wyg6D1uxPYtVXdzEyCwR7dFuMoVL5neGEBn43XLjxK6qSRGvgZDMJ-q_XErRDpX0P640GBcBR1tp5LEJ_yM42EGB_woiu8oGMJSs-qBg433yd6CXEcz76JVsilBTpiAqn7ZUy_G06GoFOlgVzfm7E3ALbnhH814rxugUzXRdCexiX1alARnTCvTiBAqgW-4cwQsFR6XIQPcFq4DONPel8o0niRmZMvEl_i8C7dD3dywT5AknQdcASg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
این ۴ نفر، شاکی قضایی «اتصال اینترنت بین‌الملل» هستند
خبرنگار «انتخاب» دقایقی پیش کسب اطلاع کرد که ۴ نفر شاکی حقیقیِ «توقف اتصال اینترنت بین‌الملل» هستند. این ۴ نفر که گرایش سیاسی آن‌ها کاملاً مشخص است و تحت راهبری یک مقام ابقا شده‌ی دولت رییسی، دست به شکایت زده‌اند، عبارتند از
کامیار ثقفی، رضا تقی پور، رسول جلیلی و محمد حسن انتظاری
. / انتخاب
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/Futball180TV/90235" target="_blank">📅 14:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90234">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
وزیر علوم اعلام کرد که تکلیف امتحانات پایان ترم دانشجویان کارشناسی طی چند روز آینده مشخص و اعلام خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/Futball180TV/90234" target="_blank">📅 13:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90233">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
#فوری؛ سیتنا:
🔸
دستور وزیر ارتباطات برای اتصال اینترنت صادر شد؛ اتصال جهانی ایران از همین دقایق احیا می‌شود؛ اتصال کامل مردم تا 24 ساعت آینده
🔸
معاون سیاست گذاری و برنامه‌ریزی توسعه فاوا و اقتصاد دیجیتال وزارت ارتباطات، در پی دستور رییس جمهور از بازگشایی…</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/Futball180TV/90233" target="_blank">📅 13:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90232">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBti6MtsRQrvDSUaQ3VG2HPSv-ryFi73kDvMPZTTnBVlxBI49sus0WFzXBsL1OGahlvHYUkJhgYAakeHboMlwME-hTcLloWi8MLGfDoflyKkjGaS_9XYBdJ96r_eMQ-KAl2J7dIFXcyMWLWt2DGyiYSZrsGQaWwsiLcVjXqPLmFXG0pgLLVVjtwqOcs7SLj_JG5nLqq2h3d3UX3xqPCA4EXPPRlTNBusx7cGsEDCUqHsB3sCaJNYr2QcZLUdT6P48iU6pApSOikhVwouj6mCBzWD2BMYoU4BgovZkvAGFUFxEi3OYtplVxxavjembgn-2wOkEKL9YFsB7cOuOCztKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ سیتنا:
🔸
دستور وزیر ارتباطات برای اتصال اینترنت صادر شد؛ اتصال جهانی ایران از همین دقایق احیا می‌شود؛ اتصال کامل مردم تا 24 ساعت آینده
🔸
معاون سیاست گذاری و برنامه‌ریزی توسعه فاوا و اقتصاد دیجیتال وزارت ارتباطات، در پی دستور رییس جمهور از بازگشایی تدریجی اینترنت تا دقایقی دیگر خبر داد و گفت: دسترسی کامل مردم به اینترنت تا 24 ساعت آینده میسر می شود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/Futball180TV/90232" target="_blank">📅 13:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90231">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0edb93becd.mp4?token=PGQtgQ1tAhUc4ZHPC8ngT4SPfRzZQLL-S9nkbtAuIj_QcET1Y5dv2s1oPa-i-d7eXNRSnmMVjPr7xtpDdDz-XnfS4sF-jIw6ZYX3a_Ngsg-RkB7bsoye48GfKtGkjBB2YHWBphoeQq1txKMMDCJYl71xCcy3RVBig7W3yqdxXVJoCuUOKnnfx5vAN4vUbq0YGbDCNeKWlDOMn6CqFldSv6cDZLNAUdsf5FIZJVqs3KgGMgC_1ymz2G_0qymn_oGOzd339oYBCtAAkaMYiAYQGiaJ8xq5mqDmqcTdX2RY8sgonDMsGB6VxY--t9ubHknn7u2-oJxw7chWCqxB8kwe_nFpOzHxYXTlZN_fqOoi9kNx_1VbFDGWeeeYQw1-5irZ9W32Fv2BfMow6STx_bRJaz1ZCBbEMbCVMEK1oWTNuEtQ1wJk8VKuncIUT7xEaKK1Zl_WgxJp3oOJ4zUQO1lYDCikpPD1kaY4sSY1zV3wDb5FhSgGkv8woOBSMecoT1aeQ098WBIfE19cDUzQWea1n4Pu4t4OE4EyOTj6xJb3QdXOOxhW0BiJVNeQnbI9xK2FgnoId7xgYMaETHP4YtnXKszxle0ascqn2YpTtJM6CSUU8PB5dHd9SSriEff3_hI45uWBebI8uotp6hh7iJj4eMj3B3G4g7EWAJA80udYuaU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0edb93becd.mp4?token=PGQtgQ1tAhUc4ZHPC8ngT4SPfRzZQLL-S9nkbtAuIj_QcET1Y5dv2s1oPa-i-d7eXNRSnmMVjPr7xtpDdDz-XnfS4sF-jIw6ZYX3a_Ngsg-RkB7bsoye48GfKtGkjBB2YHWBphoeQq1txKMMDCJYl71xCcy3RVBig7W3yqdxXVJoCuUOKnnfx5vAN4vUbq0YGbDCNeKWlDOMn6CqFldSv6cDZLNAUdsf5FIZJVqs3KgGMgC_1ymz2G_0qymn_oGOzd339oYBCtAAkaMYiAYQGiaJ8xq5mqDmqcTdX2RY8sgonDMsGB6VxY--t9ubHknn7u2-oJxw7chWCqxB8kwe_nFpOzHxYXTlZN_fqOoi9kNx_1VbFDGWeeeYQw1-5irZ9W32Fv2BfMow6STx_bRJaz1ZCBbEMbCVMEK1oWTNuEtQ1wJk8VKuncIUT7xEaKK1Zl_WgxJp3oOJ4zUQO1lYDCikpPD1kaY4sSY1zV3wDb5FhSgGkv8woOBSMecoT1aeQ098WBIfE19cDUzQWea1n4Pu4t4OE4EyOTj6xJb3QdXOOxhW0BiJVNeQnbI9xK2FgnoId7xgYMaETHP4YtnXKszxle0ascqn2YpTtJM6CSUU8PB5dHd9SSriEff3_hI45uWBebI8uotp6hh7iJj4eMj3B3G4g7EWAJA80udYuaU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
جزئیات درگیری علی دایی و علی کریمی در مراکش:
🔺
رضا جباری: فکر نمی کردم اینقدر علنی و شدید با هم اختلاف داشته باشند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/Futball180TV/90231" target="_blank">📅 12:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90230">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90230" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/Futball180TV/90230" target="_blank">📅 12:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90229">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2CDtHdNSYzQUnstlvXTHN4CuLM2xon_EuVcAd3EzuWJDGQi1CKXlK88EwDhy4TNlsSZ-f7vCcr94O5orfeCToDzN61Rd11dy5VJSQqwUwqXBvRcF3Q9hC0areH8CHv2LoYEkgPstJvFRjjBcvbQkTELjAUYAFGwEupF_JdDs0l3aeqS3iz_bbq4ciJ-Wrrx81q9Ui_Wkt2SEiK8ZTc2BD9TwAlihO_KZKDaKocikBylWwP9XQmwij_2RBuygVo8BfQhieMK7_EWFXsKByhl1ZWRpMp6wjo2r5R4I67012gHM6yavhSnTrZXF2x1HXalQD6NCBPgqpcSfndp2FniRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/Futball180TV/90229" target="_blank">📅 12:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90228">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d9611d964.mp4?token=gPSVwn3joaCZkPfXYLjkk-dcRIHwLewYV-MkZL1h3e8K8VRPTP56gi7FjiXQczd0EZRIb4zwIKIi8rUngXYeA50Pi0tngNV1m1KOxMQtK74t7CJ8D-08Do3mdK6dpXYlteRr7dCP7mTRo9p73n3Oi0B3izY4Ll67ui56749jMK0uyHjqJQo6qft2ZMwC4HzekNdFVCiujcIjSQUz-fASbw-cVnxOgRTenyyudXHX2d6WA8-BdYzWL7ieXAdUdBHqTpOkzWV_j2I0rpNLKA8AitsrvSq4pPiAw3urlPDu-NLbjV5JeEIj_5fgn3RWWAyPpcynFxJDux8BRc2K3rLTBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d9611d964.mp4?token=gPSVwn3joaCZkPfXYLjkk-dcRIHwLewYV-MkZL1h3e8K8VRPTP56gi7FjiXQczd0EZRIb4zwIKIi8rUngXYeA50Pi0tngNV1m1KOxMQtK74t7CJ8D-08Do3mdK6dpXYlteRr7dCP7mTRo9p73n3Oi0B3izY4Ll67ui56749jMK0uyHjqJQo6qft2ZMwC4HzekNdFVCiujcIjSQUz-fASbw-cVnxOgRTenyyudXHX2d6WA8-BdYzWL7ieXAdUdBHqTpOkzWV_j2I0rpNLKA8AitsrvSq4pPiAw3urlPDu-NLbjV5JeEIj_5fgn3RWWAyPpcynFxJDux8BRc2K3rLTBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریکشن گاوی و لامین‌یامال پس از حضور در جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/Futball180TV/90228" target="_blank">📅 11:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90227">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
آیت‌الله مجتبی خامنه‌ای: رژیم صهیونیستی مطابق گفته پدرم، ۲۵ سال آینده را نخواهد دید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/Futball180TV/90227" target="_blank">📅 11:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90226">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d0834d346.mp4?token=Adk5gOc-fVVJUg75CADvgcBpBjuebGqX3uV45RAH7tU2yhZSoxzsmSGmzp3PWjzif_MbxW8aTy4hamKqgqO0_CXa8mkQAdSZ1wx5DngDfLhKdzQw34gEYkbuaOgS5MmBFM_isJrXTKlbI3EMn8wDL5zFEP_rEHvP2IeEZ0M-NVQPdR8MQoXw_RXAgpVSpiNpBfPivZ-0YYXOEGWjmk4kfVUY--q0RuiTX3bGjVcz6bAzoXBgptPhqM57VI7-YmuBrY0PR4AYvwRP8U21Q1eZvxVINQauCI1CB4V0HoryybL4jWUTnylHKCfZg_NlABMahtrkB5J47T6I3VFfPodA5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d0834d346.mp4?token=Adk5gOc-fVVJUg75CADvgcBpBjuebGqX3uV45RAH7tU2yhZSoxzsmSGmzp3PWjzif_MbxW8aTy4hamKqgqO0_CXa8mkQAdSZ1wx5DngDfLhKdzQw34gEYkbuaOgS5MmBFM_isJrXTKlbI3EMn8wDL5zFEP_rEHvP2IeEZ0M-NVQPdR8MQoXw_RXAgpVSpiNpBfPivZ-0YYXOEGWjmk4kfVUY--q0RuiTX3bGjVcz6bAzoXBgptPhqM57VI7-YmuBrY0PR4AYvwRP8U21Q1eZvxVINQauCI1CB4V0HoryybL4jWUTnylHKCfZg_NlABMahtrkB5J47T6I3VFfPodA5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اینترنت بین الملل چه زمانی وصل می‌شود؟
🔘
سخنگوی دولت: امیدواریم با ابلاغ رئیس جمهور ظرف روزهای آتی اینترنت بین الملل بازگشایی شود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/Futball180TV/90226" target="_blank">📅 11:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90225">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsSKzQcDnOOFJLiR7jAu5I1VnT5eXuYh6g3fplTs6btSA0dRqgrLQwrsZP9H-kNgq_et8MXs3RZDXmWPGPJLQrN8MHxvlfEBCUd75U-E6DU0fH7PtCRCwVFKncgPpiFxTmWd6Z3gmfuK5PMqukD7puMz1W8Dg5B2hOhT_xkQXwJa_KoDrQ3VqcwYDctUSqX5-06jrTmMG_Nt_7cJvaxOfirQGIBxvd7QCNM42kT4W_e_WJPdbyPU6D3aNQvUVjrIZpq1fefPaIhBY0GprTo16yz7EbG0OFMqvXOhQY8hGshhZFA2d_zDlimwNw35-8dFopmJaJgHXrqPrIFWZueROQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قهرمانان دو جام‌جهانی اخیر در مرحله گروهی در گروه C قرار داشتند. برزیل مهمترین تیم گروه C در جام‌جهانی است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/Futball180TV/90225" target="_blank">📅 11:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90224">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HixNaZcQGRZqrVbOilbkLdzpHVAw3Oy2nuOGEv2JddpztyhB6S3nsw6bFLnZ8LKjHYHa3K48RiL-0PhhTzLfpZcfSV4OSurcflr9fviSTRtWPkDlWDKTSrWnCUod6TFQEJy-dBKpJYfSlRuEEYFp5SX8kh8msGiJ8XbjmkuoDt3ZXQdDA-kn0mAJpbJ-uvW9HO-psoqXEXs_minvoReIed-Eu7RbwaMbhfnxhtqlnJwbujj52t90lkVxoj-lT6WiIJTLFubX17xbEp9E5QHOgx4whufcBeRUSHwL7lPTohMFbAk_T4ASdBKkVMk1LvxP8dBZ918UOlQkeKIB6LXB0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با آغاز اتصال احتمالی اینترنت بین‌الملل؛
ساعاتی است جیمیل در دسترس کاربران ایران قرار گرفت.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/Futball180TV/90224" target="_blank">📅 10:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90223">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7673ee9149.mp4?token=k3-wYXd_2tJ8WHs6n6wuTGNup4RZ1ktzbM4sDy6ftoOMFtzdJbzFMFjaaPEvW0CUJcdviJJWsy-VqeN3H3UbvQdRhYsZr9HJ9KNNNAaLgQSWQohoVIWTJvk0UdgbTvRtOUkOSQLUkKF0xVBh8eSEzvwKJG-x0ND1GkUkyc7pTo4OlYo9Kn7Z7ESQJi0FR8oKqa21PLWVT2Pjw-Axgeu0lerz84FO4ceRlmTU5iNqggjFCv_oo0kI0UUlnCyk5wKwchM2ZlVbC54CrRFdhbIVyQswG6YUwD9cC2DVrozpBIslJs4NV_L4wKw2AJh-t6Ub3hWQegbOqcG4cMTLlAINfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7673ee9149.mp4?token=k3-wYXd_2tJ8WHs6n6wuTGNup4RZ1ktzbM4sDy6ftoOMFtzdJbzFMFjaaPEvW0CUJcdviJJWsy-VqeN3H3UbvQdRhYsZr9HJ9KNNNAaLgQSWQohoVIWTJvk0UdgbTvRtOUkOSQLUkKF0xVBh8eSEzvwKJG-x0ND1GkUkyc7pTo4OlYo9Kn7Z7ESQJi0FR8oKqa21PLWVT2Pjw-Axgeu0lerz84FO4ceRlmTU5iNqggjFCv_oo0kI0UUlnCyk5wKwchM2ZlVbC54CrRFdhbIVyQswG6YUwD9cC2DVrozpBIslJs4NV_L4wKw2AJh-t6Ub3hWQegbOqcG4cMTLlAINfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هواداران ترکیه در آستانه جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/Futball180TV/90223" target="_blank">📅 10:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90222">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ed589fd9b.mp4?token=HNmDD5OHTpxsB-xz0x8tThlmRTW-pyb7kCBrHld7UFTgx7e4rb3aet5jaqZysuYPUu8EhMSvQM-cpeIMJhfA1Ktao4h99JkJCeqK8eIup_xrJqEjTPQo3_fXk_s8nkzjUtj73B2wKqevxhBv7AAgAAw6zN3FrhuFTefMLbUBW1uIVmDw9H2zMQVNLmHwVZhSkbZmc3CjqHhSBCCty6OrA5yXYJnz67i7NM0WAeIjoAKg8YzI_dE7N5iIZdKx4tJaFaqqHL_MBHgBS1ktdvtrIEimi5I7mzMBUtXgnIAORJ1lH43AS5mEYCPSD3Sl7-Coaiyc8H9pjyY55JAF0ra9Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ed589fd9b.mp4?token=HNmDD5OHTpxsB-xz0x8tThlmRTW-pyb7kCBrHld7UFTgx7e4rb3aet5jaqZysuYPUu8EhMSvQM-cpeIMJhfA1Ktao4h99JkJCeqK8eIup_xrJqEjTPQo3_fXk_s8nkzjUtj73B2wKqevxhBv7AAgAAw6zN3FrhuFTefMLbUBW1uIVmDw9H2zMQVNLmHwVZhSkbZmc3CjqHhSBCCty6OrA5yXYJnz67i7NM0WAeIjoAKg8YzI_dE7N5iIZdKx4tJaFaqqHL_MBHgBS1ktdvtrIEimi5I7mzMBUtXgnIAORJ1lH43AS5mEYCPSD3Sl7-Coaiyc8H9pjyY55JAF0ra9Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
سیاوش اکبرپور: جرمی دوکو رو می‌شه مهار کرد!
😁
محسن مسلمان: ولی نمی‌شه؛ فکر نکنم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/Futball180TV/90222" target="_blank">📅 08:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90221">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90221" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/Futball180TV/90221" target="_blank">📅 00:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90220">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svJvWDaJ0aK26GkS2PwIKJLISV6SFTf40bOZ5YwGhcYqisAlFtD8C9FoEAVbaJ7c-Hps0GC7Mpx5sh8quY1MfoW9DR-u7_CfqkyDzxmAZDLO9uyuRTOeLXFzS7n4Fw0ZbCWuqOXwMuuKf_Vg5Xxv3ndSfTo7I8RBU9l5Yu6M4gWoanQVy7OC1ST4qh2uANVQWqHjhZ-y6kUDatCk5xZ4p164EkaRM6gdmt537UxQPPojIZ91f71hn7QAvXD7tTt7D1LhxVMKGZlDCWRn49hUlCMaE9wCOYiAIk1uLPvfun3Nw-c0tTAGsk5qw_b9ps7Fduz45xxoLMpRWQDMYW5apg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
با پیش‌بینی روی مسابقات افسانه‌ای Roland Garros در پروموی Grand Slam Tournaments، فری‌بت‌های تضمینی و شانس برنده شدن جوایز بزرگ رو به دست بیارین!
🏆
جوایز ویژه قرعه‌کشی:
📱
گوشی iPhone 17 Pro Max
📱
گوشی Samsung Galaxy Z Flip7
⌚️
ساعت Apple Watch Ultra 2
🎧
هدفون Samsung Galaxy Buds3 Pro
🎫
فری‌بت و امتیازهای بونوس
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/Futball180TV/90220" target="_blank">📅 00:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90219">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Grf0qWQ0CnyOsHDWjES24Td6mnR5EIv6AlUK0r3elxdRCGiRPwAe_Ij7ZL2s0vERO-1O28Nbe7SVHbvyGuN0EB-kpIIRiq-3qFLbTu_s8YwjShHHPgbQHQ19WTfs0AS-zsPSSPcwS5C31CEEknvH94pMvyKU_GZhm246kKctRivHiPm9fJ-ejCxhR72B9ia6BNVwt7PZp-c13yRFEHcMCKS4f4PlJdZUuodXzr03eEQOMspefmeD54QBz6FAF7mbLvW6ggur8ATMSltPEpuQjOxL5d_zkOCP78F6Q87TSLvOLPNrDXd2dWcJgXsjt2i6ty3WM0IpxIV8VT2Hq8VO5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇴
لیست تیم ملی کلمبیا برای
#جام_جهانی2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/Futball180TV/90219" target="_blank">📅 23:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90218">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHtiZTllODOJc7BNTHoZOjvrihf5FbElmani04Za0erS95i59TrgIqmGnitCw9DcpOifQSoAaiINhaajrba-8TJNDpY3VJDCh0mOnE2UXIhT0j_VkS-81La0es9xQqz4mxoRllbq2pLwE7yoLV3R9M3azG-7nNJWNf4qnJG4zE2kc6H-HQq0AdzIvAJcrFo43suSqZlOOmMGPjf7RgFiqJM-QDajmtZi79UNRp6hOG7T_xrVZWwdbbOUbh2O1sgLkxKgASIH1Q38sgSLehn6rvbNNZV5uyeMXZwbJDxwYoDsuGyc7b0tEz3HGbqmLeJxY6WmTNFM5KHeKE6UijX_tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مکس آلگری از هدایت میلان برکنار شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/Futball180TV/90218" target="_blank">📅 23:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90217">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3602a6e5c9.mp4?token=WqNWXFN6flacCJ4OQl8TCPJCYgPPU3GpRHCW3wg5cfw2KDg4lWkZcYVr2MNd1-PqPIg_AeB6SAj1oO5Z0b3YHO4tzTim2PkHPoQ_vtqBwNc1WpoR0moegFGpa4BgVfFU-EVAa1X8jbzAzZEg1RQZqXS7Hi2s9dnFK6Fx8eabYphddnYco0sCh8ANpbMH4IzpVC7QF-VTDZ9eDG9jEYverr322Xv6XwohBdpQ4Of9RCOXU6yT5IkCrfx-DsA2KN0L5J7RAtfmbDYX9HIJNHgz2fCRCTzdGGvARvHnxGCRN3fIYjwZAzc4bon4dlNSpXO4VUfsuFB6D0q8Omv7jPFpvAvNF1m9W-i7m2HoX9ClXngwmTm9GxWI_nd8f5HSksvwVLLmlAh1heZqi0ADrp1A4WrQOtAlafnqQQ68-tybA0Wnj26b4ifSAaxoKS5kQdV4cH3JcRxPQJozFj9azzx4ELUxejErkxo5aa_YnZOrCBnHRwefjCP3VU0ZS3XEfcGGlbuC2ubNJos7Ny-qpnWBUx77_wLB5nO7j4Hf29sXrFWQ-dETUpMvacTFAe41a7CwqYR9gBSQGvR2giIR5LLbQzQ7Qoq-Ilv1g35mfmyBFEIr82_1dAHPDzTo1GWHkjjyD5S2V7zUWmoonBg4abSHbuX_0RZIRMh7gZnpm_xMrhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3602a6e5c9.mp4?token=WqNWXFN6flacCJ4OQl8TCPJCYgPPU3GpRHCW3wg5cfw2KDg4lWkZcYVr2MNd1-PqPIg_AeB6SAj1oO5Z0b3YHO4tzTim2PkHPoQ_vtqBwNc1WpoR0moegFGpa4BgVfFU-EVAa1X8jbzAzZEg1RQZqXS7Hi2s9dnFK6Fx8eabYphddnYco0sCh8ANpbMH4IzpVC7QF-VTDZ9eDG9jEYverr322Xv6XwohBdpQ4Of9RCOXU6yT5IkCrfx-DsA2KN0L5J7RAtfmbDYX9HIJNHgz2fCRCTzdGGvARvHnxGCRN3fIYjwZAzc4bon4dlNSpXO4VUfsuFB6D0q8Omv7jPFpvAvNF1m9W-i7m2HoX9ClXngwmTm9GxWI_nd8f5HSksvwVLLmlAh1heZqi0ADrp1A4WrQOtAlafnqQQ68-tybA0Wnj26b4ifSAaxoKS5kQdV4cH3JcRxPQJozFj9azzx4ELUxejErkxo5aa_YnZOrCBnHRwefjCP3VU0ZS3XEfcGGlbuC2ubNJos7Ny-qpnWBUx77_wLB5nO7j4Hf29sXrFWQ-dETUpMvacTFAe41a7CwqYR9gBSQGvR2giIR5LLbQzQ7Qoq-Ilv1g35mfmyBFEIr82_1dAHPDzTo1GWHkjjyD5S2V7zUWmoonBg4abSHbuX_0RZIRMh7gZnpm_xMrhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما ۱۳ نظامی در عملیات خشم حماسی از دست دادیم تا مطمئن شویم ایران به سلاح اتمی دست پیدا نمی‌کند.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/Futball180TV/90217" target="_blank">📅 21:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90216">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNYDeM8JjWl2wyLLlt5fPCRMPI7uBNyHej2hBCi15UdKDcriHZEkCcy2VWo4ZefMokJbGeTK6jfGSROdTE2pzyZL0b55wUMrwIeOHYMoLd-bjgDx4YIDOA5ePJy3LEX6graqNRsm--qhelk3Pxj8JrBYjf7LwlqXpj4rsyF2x6JKI_s5JdMZhr_wMoIP5AGg0ah0WNEryLXiqtCVXqbzFQZzM1PaHdxbqYBBT_vBLq8Wo_6phdXFmNAd2C5_voBO0_W8O313ieT41PVjZ66vvKwWl_Jsp2HYySc8VFmQXhC8Qc0G0iy7_Mz3-nV2QHu9U-5OJPv4WZgpX6ZrYytxUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
سن-اتین - نیس
🏆
پلی‌آف لیگ ۱ فرانسه
🇫🇷
⏰
سه‌شنبه ساعت ۲۲:۱۵
🏟
ورزشگاه جفری-گیشارد
🎲
با بیش از ۴۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
سن-اتین در
۱۰
دیدار اخیر خود، چهار برد و سه تساوی کسب کرده و در سه بازی شکست خورده است.
✅
نیس در
۱۰
دیدار اخیر خود،
پنج
تساوی کسب کرده و در
چهار
بازی شکست خورده و تنها در
یک
بازی پیروز شده است.
📈
میانگین گل در
۱۰
دیدار اخیر سن-اتین
۲.۵
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر نیس
۲.۳
گل در هر بازی بوده است.
🧠
اطمینان صددرصدی نشانه خطای شناختی است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/Futball180TV/90216" target="_blank">📅 21:09 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90215">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7263cfb5.mp4?token=Z4kNZM9OxASo4W5vZDO9JADXwZZqJs5XAmjg9lSVf8R6WSs_bUIi6GTZhOXuySFWQXYdyBiyqTciQh-pJRRr8U5XK2IRoBP_lLEzCRMWiPTOupTENLQW0uCkMVTjMDkzSA2XKOrNbPm1dXAHnJjUEZ9veueMexf6_qZeXrlixAEuMVNRCkjcLNZ5T3dOEzng66uMH1t-xHY2ELoYge6jT2d8NCuaTitA6_PSaPj0zV8HlxCC5slWXTH02W9Ee98EgKuOBOetDYOZ_spsgFWDRtlhElGoOmAw9XQ8EgjcdypM5RJgj5cHLGmwWGUWfXhfJ7PXQRgHmet-DQOAWqKv0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7263cfb5.mp4?token=Z4kNZM9OxASo4W5vZDO9JADXwZZqJs5XAmjg9lSVf8R6WSs_bUIi6GTZhOXuySFWQXYdyBiyqTciQh-pJRRr8U5XK2IRoBP_lLEzCRMWiPTOupTENLQW0uCkMVTjMDkzSA2XKOrNbPm1dXAHnJjUEZ9veueMexf6_qZeXrlixAEuMVNRCkjcLNZ5T3dOEzng66uMH1t-xHY2ELoYge6jT2d8NCuaTitA6_PSaPj0zV8HlxCC5slWXTH02W9Ee98EgKuOBOetDYOZ_spsgFWDRtlhElGoOmAw9XQ8EgjcdypM5RJgj5cHLGmwWGUWfXhfJ7PXQRgHmet-DQOAWqKv0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن‌روشن: فيتيله ترامپ رو بكشيد پايين وگرنه با "اسلحه ژ ٣ "ميريم آمريكا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/Futball180TV/90215" target="_blank">📅 20:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90214">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/Futball180TV/90214" target="_blank">📅 20:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90213">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cecznzR2_Tg6OeP_jPlDfSnU_md-8y8jKHbDmzPPsg8NwHjKScAR9I7ikeJ_bwiPe0VYMvoHz-mVidXKBk2AKmTBbz1vYssGbBkHBu_E0ELmvZVlI6hbJbpqxYJjPrzfOFGOn8NUJFlBskb2M2wrQ3IoyLFygWcf_bIx6V8FFhWfjPrMe7NKvZjpph-6asR8sXGnzWXaKvmjQ6Q3qQLsLc96WeUy5-qj6W21i2PyvJOrIipzTu9KBsGdJf2_G-c9HWoBXq-lI0DuPhDHMdjAOjUtJ7wQGfoPZ-l0YZVN4-AzDOvEu6IZ1mdi4Yvk27cwT4_MObAwimFFvXuNw8h_Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/Futball180TV/90213" target="_blank">📅 20:53 · 04 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/iTP5dEGbN-JKPgO1U0Og-VqIdnEQwGx1lHjREcYd_j76Fn0z0BlKPAdTNEHVPv400Vq5kzpnwPXCPhoUrm8hmleYnm-JBRtj0OCbyQyhiLWmNBfqjfcOv1X5ZrL3C6pQWBle0TCdky2SWoFEVmh1qjwIFlb2HJsU8jwhDn80ZJ9a5Z7aeN_CSKPnw29BwiUM9W6H71td3auhpMZZb0prWgDatshhwRisBFVdYX5WN0UleM2xynIP6lZJsFEPjTpF2ZEGfY0Hst-gWOeGxqaBUuWO4F1pB7kV1KSKPiBBqn7MGiVfW7yoTTMUrR6j7dBLJ935PxL0TDrJCmRM7Gm5aw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 973K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 02:35:05</div>
<hr>

<div class="tg-post" id="msg-126087">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PyMBBHrkZwxL0mdcTb-tixhnWh4Rw2XILMJTLA56J56EPoqO6CxroquIsuemNYbYb11Rd2JZQUSZPndMGUvfs4aPbyKSuMrcB7b3ItxTp9iUbs-raG5hSdkD1dkOnsg8h36tbLkPsQz_WRRRfaPOMbZGdYsrDfeyKHKx-UgO86YvuHD_B3zuIqXdTxLUeBw9bdKzlIJMtlpzQ2SlINCQQUfBWjK0cPp2KqaR38luEsmlMieua4KAJn3Y5Ps_puMrFRSGoZe5fUzyN52W1UOGcb7O2X-dFm7v_fw-n6QgekmZIroMHZB5c4Kdrw1y2QAM4q3RvDHP4uj5Fkn6WXDBnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با سابقه ۵ سال فعالیت مداوم
🛡
حتی بدون قطعی تو دوران جنگ
🌐
با ما همراه شو و در زمان قطعی
وصل بمون
🐸
بقیه هنوز VPN حجمی میفروشن
اونم با قیمتای نجومی
🚀
از ما با کمترین قیمت ، بهترین سرویس رو بگیر
👀
💥
بدون محدودیت حجم
⬇️
⬇️
⬇️
@NetAazaadBot
@NetAazaadBot</div>
<div class="tg-footer">👁️ 9 · <a href="https://t.me/alonews/126087" target="_blank">📅 02:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126086">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
ادعای یک مقام آمریکایی به کانال ۱۲:
نتانیاهو «به نحوی» با به تأخیر انداختن پاسخ به حمله ایران موافقت کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/alonews/126086" target="_blank">📅 02:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126085">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dguil-xNUkB1eTxx7QhO1gJp909CcFiPxlLaVAfMpqjHt7sLzb770wrIBcvY4YhHyTfFUdbjq3w9iA0-n9Wq4Ssn8YomvQ5RhxwraGZ3g_LL4EEgkCDtL8g3camvtmuIhrBXj_Cxo-8jQPBN89u0j0PvIpzZbJP4M9guS--04P_O-86U1lTwxtMzNxxUHOXZY1_31UkDZskH0j_G4dsuM6ErdQAEjApQmeFi8rYKxb3smy4wjxI-HaFEhuzZnNAe8vD9pwoOV8kFA1PeA1wcLbDBJ68aUe-pcm2k14oeuSfIFWpWGYadlEYWL8cjXNhYeIQh0b58mny6KbnxTY_K9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری تسنیم :
ایران امشب تو حملهِ به اسرائیل از موشک‌های "خیبرشکن" استفاده کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/126085" target="_blank">📅 02:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126083">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjymmoaZF93nI4cwTvUa_Uh5cCoW59arg9tGyXhLWSkkO0hyvufaqAktvHjwmS5Ozzo5yHAcr_tXJ4-caYxm_KmhD4bXWIiWhwIyB_5Fd36WDQ2aixNcVu96NxyPH5mlrPkct7YHw5Bpr0vF_1AM-KE05-zqRY-pleQ6k-dVAe1prt3M17U4TlEwUwo9j9f0r9oo0jxwLihmnzR3H-q7dWIVqtM2I7tXdhU8oFdPnwKIQRJuDKBgj6BqouYjonoTSAF1rIpJwfCJ9hnxsDG0XsE28fq6w7VmuSAUtoiBSkVUjDu-2JbeMPT1g-kCCjdBXTpdhAaZVFWdFSA3fLXEFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5a7a839ab.mp4?token=dRl22uPpnNApLutETiAKxs0sfwmvBqWlBpmKf_CPSveJwb7n0YErKXzLqaexzAWpgv2yvMa1Rktog7CRy6_VOMAalWE3iHMUTid6xXEIWsMDORdjD8fMZnEPIBNnocTAOAgCvi9DRY2013sCf1fH-rJCXEeRT9edaYWu67GWl87QKYpsOQ5mfJd2gO04yvk6gyX2zkRklK_2hq17MUr5NbOHAAHHgSKvkZ_SOLNbp54V1VLz3TtWo1pL-mEL2xlytfcXdlId4hvc4XmNbxZAwtlSo9MD1uD-DaMz-4ui0r5MVEdMaSCMs8PDDafg3--SolmJ_IgwewaNXx3G3RFk1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5a7a839ab.mp4?token=dRl22uPpnNApLutETiAKxs0sfwmvBqWlBpmKf_CPSveJwb7n0YErKXzLqaexzAWpgv2yvMa1Rktog7CRy6_VOMAalWE3iHMUTid6xXEIWsMDORdjD8fMZnEPIBNnocTAOAgCvi9DRY2013sCf1fH-rJCXEeRT9edaYWu67GWl87QKYpsOQ5mfJd2gO04yvk6gyX2zkRklK_2hq17MUr5NbOHAAHHgSKvkZ_SOLNbp54V1VLz3TtWo1pL-mEL2xlytfcXdlId4hvc4XmNbxZAwtlSo9MD1uD-DaMz-4ui0r5MVEdMaSCMs8PDDafg3--SolmJ_IgwewaNXx3G3RFk1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون حملات اسرائیل به لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/126083" target="_blank">📅 02:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126080">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szAH46000VhelVHYGrG9iFIT2vSWjMzejGMmmdsZVIpzL9hc6rE-tEf7h8huXivFQEAn0_lt7YmqL4kyuA1S97VT9lC4sl2AZiUhPAjB-dh0EItTx_V266kbs2Hk3ueRbmWhIGQItoZldXprw717ObioRPI9SoaQsFU6hPesPPshfm3_nUDEluji3_yg2dZOUjoxTuB5EosW8R3JxwVwnghYlCZ4c6v7xcDQdj9RHfnHQoIUKTuhIWg282ZfbDQtpTTLk9Sk37XGxL9yw8-NktDKFJo3pkn1p4qfNjDso5vK_Tvrt5b_pmF8I3E8UDpsBcl4linDMEKeYiVGuL3fTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمید رسایی: هر چه زودتر اینترنت رو قطع کنین تا دشمن نتونه به ما ضربه بزنه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/126080" target="_blank">📅 02:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126079">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
ترامپ: محاصره ممکن است قوی تر از هر حمله ای باشد که به ایران آغاز شده است‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/126079" target="_blank">📅 01:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126078">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
کانال کان اسرائیل: در اسرائیل در حال بررسی تصمیم به عدم پاسخ‌دهی امشب، بلکه پس از چند روز هستیم، و این قطعاً به دلیل مخالفت ترامپ با حمله است. در حال حاضر تصمیم نهایی گرفته نشده و بحث‌ها ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/126078" target="_blank">📅 01:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126077">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
فایننشال تایمز به نقل از ترامپ: فکر می کنم توافق با ایران در حال انجام است و خواهیم دید چه اتفاقی می افتد‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/126077" target="_blank">📅 01:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126076">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
ترامپ: ایران اگر بازهم اسرائیل را بزند ما اقدامی نخواهیم کرد زیرا دنبال توافقیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/126076" target="_blank">📅 01:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126075">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ترامپ: اگه توافق از نظرم خودش شکست بخوره احتمالاً گزینه انجام یک حمله کماندویی به ایران رو هم در نظر می‌گیرم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/126075" target="_blank">📅 01:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126074">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
ترامپ: من تصمیم‌گیرنده هستم. من همه تصمیم‌ها را می‌گیرم. نتانیاهو تصمیم‌گیرنده نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/126074" target="_blank">📅 01:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126073">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
ترامپ : نتانیاهو هیچ انتخابی نداره بجز قبول توافق با ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/126073" target="_blank">📅 01:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126072">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8PrZbvctbrVtxLKJz06BuprCPqcrcyMaZzdXy6K2M4eRg_a71v8NMSe2W7TeH9PHGs-BHtP4Grrqu8p6q2EJmKxaL8qpKHmiw0Y67KS_wf_pjB58LAmyXi9XvWA0nIuml9XTJvnNkZy3ABSnN_DVz11eGAtwBnlkX7NiXDjZJgKDvkwVmlAS6T9TqPNfVm9s4CLlTCCI-5SPHjBte43S83SNrhWSOnrCZ-z9GWARudAGh-Yh64W1uQ8F9NZHzdXy9UJ9gpcayQbIHHjz2yKUljM8ye0V7wGZxaIg0mL2gSOv81RjaOh4vqDzxpoUWYGEQAD5Jdj3CQdGR4aSzVx2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دقایقی پیش؛ آمریکا هشدار داد به اسرائیل نرید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/126072" target="_blank">📅 01:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126071">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
قیمت نفت برنت پس از باز شدن بازار های جهانی با صعود سه دلاری به 96دلار رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/126071" target="_blank">📅 01:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126070">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbg76q9YYHFgY8r6k7tO3O83EsfqCMhDeJ-udsWvt7-tQbWVW_94gh2AHp-W7VdVEaAXwaLTrFyN3MqMG7MY2hSG5BO4R331i0MyLMKzt7xiBUy3N8EK0zYG8kYHahYFbigVjxFALEH7Ob8zbh0d4pera7JPgcuwFmHjVMwJyvVfvd-VxQcSKkmbX04Ofi8SxYNvIhLsOfG-JccuPYuBcMUxkuVJusZf975oNrKOtZKbt89pzBPpiCI-_sTIjXk73lNwd5yIhn1XmjQ3o6J5H6975qNxZfEoWbVPkb9iCIq0yXZkCiLcs0HvNw1SCpEz2FTz9rgVf3AT_l6c2xaFjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر کشور پاکستان از تهران رفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/126070" target="_blank">📅 01:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126069">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
جروزالم پست، به نقل از منابع: اسرائیل به ایران پاسخ خواهد داد و هنوز در حال بررسی زمان و مقیاس این پاسخ است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/126069" target="_blank">📅 01:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126068">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
مراد ویسی: احتمال پاسخ اسرائیل بالاست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/126068" target="_blank">📅 01:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126067">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
منبع پاکستانی به العربیه: پاکستان برای حفظ آتش‌بس و جلوگیری از تشدید تنش، تماس‌های خود را شدت بخشیده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/126067" target="_blank">📅 01:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126066">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
منابع العربیه: عراقچی به پاکستان اطلاع داد که لبنان بخش جدایی‌ناپذیری از پرونده مذاکره است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/126066" target="_blank">📅 01:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126065">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amrftNo62Rb7Bru3MHoPxYVlkyNJxpgxCq2Zq_VwaSkg-YTwklEvm_4qmBCYQY-R8eths6_uoOB0CXotgMRZ25FUsLAQP_tBORJWcG2x6SsgQpZcLsLy4pvQV4O3cydHuAiizwipPQME4DExVq-fb87qMW3eUdSz3Y-EHm-5JyRz5yk9spumt8Ac-wAj9y97uYTJmeCLTsMYuQBOWAsg7uN2L3pThZWmJI2uv4vDr1qW1aHTPJglCTlEtmcVrXgUae1StdMu4jokp6jZ0ZeQOg9cR9k7xh9HHTV7gj8OYnLJYCNEj9ODWnQb1BikS_9ViVC4lKXn0tVuaI9mjV132A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی مجلس: شلیک‌ها از آن جایی انجام شد که ترامپ می‌گفت نابودشان کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/126065" target="_blank">📅 01:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126064">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dec0f487e0.mp4?token=VYOlSRi201ARD3xwqtHXdSCZaPufv4r3LnSBqmcR9S84V6-ZrNcSVd6qwSMhRGUDZNjG5ucFGejyCZMprSGWmcs54r7OnDRRDytymLnjSDM0HfB7fPeREgp_tPJCUmMRgu39XK0dhWTMRlQ_ty8yBYSc_6jXebkA-pnCnw4w7xspvcG56qC0710NDxma-dczTqb2dWovGO_QKPmEYHQ9Nwjn-SpAXh_cLJ9tRwaE7V0Nz-7ZDweASFbp9VjSpY2mefvJGH52UNXMZ7kcK9PYW7ZuTvoVjTcdhEePSBN4n5y2-Py1SdBDLwz_VRn-mKjvw4SOQcUZQ1-P5FRMaFeTKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dec0f487e0.mp4?token=VYOlSRi201ARD3xwqtHXdSCZaPufv4r3LnSBqmcR9S84V6-ZrNcSVd6qwSMhRGUDZNjG5ucFGejyCZMprSGWmcs54r7OnDRRDytymLnjSDM0HfB7fPeREgp_tPJCUmMRgu39XK0dhWTMRlQ_ty8yBYSc_6jXebkA-pnCnw4w7xspvcG56qC0710NDxma-dczTqb2dWovGO_QKPmEYHQ9Nwjn-SpAXh_cLJ9tRwaE7V0Nz-7ZDweASFbp9VjSpY2mefvJGH52UNXMZ7kcK9PYW7ZuTvoVjTcdhEePSBN4n5y2-Py1SdBDLwz_VRn-mKjvw4SOQcUZQ1-P5FRMaFeTKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جابجایی هواپیماها از فرودگاه مهرآباد ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/126064" target="_blank">📅 01:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126063">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54201f2699.mp4?token=p1OuKV5t_CuSOrOuZ70blAP4nkPzhnVHKRF3KwXH-jhxEBhUhnkB35cUZhlw8NXOjtxXNKSbZU3v3RBM0VuugizY46e1f8lHvltn3Jto-CE2jlr19jnYEhinxdiSdvseyysW_vLLkLcPGM_JOqtrKNXBrzjc6yH_nH2O1LAY72GWdAlabiKe0RN9MAmL_7lmqJhHr2cw9rsdrErDepXZbrOYI1X0cXBk32OVI7PMeQhnI5ijgtiPdnKWG9X0FQAB_yNp7_1yVJc2aNVbpkAEkMGESuRwa12bS2Llc1MBBG-U-lmm6vKzy5ZreWPnMieThAmqQ87enSJsoUZCtQEvXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54201f2699.mp4?token=p1OuKV5t_CuSOrOuZ70blAP4nkPzhnVHKRF3KwXH-jhxEBhUhnkB35cUZhlw8NXOjtxXNKSbZU3v3RBM0VuugizY46e1f8lHvltn3Jto-CE2jlr19jnYEhinxdiSdvseyysW_vLLkLcPGM_JOqtrKNXBrzjc6yH_nH2O1LAY72GWdAlabiKe0RN9MAmL_7lmqJhHr2cw9rsdrErDepXZbrOYI1X0cXBk32OVI7PMeQhnI5ijgtiPdnKWG9X0FQAB_yNp7_1yVJc2aNVbpkAEkMGESuRwa12bS2Llc1MBBG-U-lmm6vKzy5ZreWPnMieThAmqQ87enSJsoUZCtQEvXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه شلیک موشک‌های ایرانی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/126063" target="_blank">📅 01:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126062">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
مقام اسرائیلی به اسرائیل هیوم:
ما به این حمله پاسخ خواهیم داد، حتی اگر در بازه زمانی فوری رخ ندهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/126062" target="_blank">📅 01:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126061">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVdsOW0FLNqvYTZhmlX_kXUd1cG8rsu8cOLh8LHaMMAgZv8_GOEuEhI1E2cknCkFs7-1Rleq0u-DyhmvCmyEMX_ewOrchywJAViJBd-pmugqyzPNb1yrqIw_lS_aoGAyeIDSBpVrnnLjfbp34QVQBJdmsfncbSIMnE4esyTe43QI03dnKFDbcwdApvGn68urUAy30e2n2g0MBajTSedX-XaOnYWBNFSy52dnPIachU-3ul2Z4cNK1M-YzmhntuEuY2efmxiGniGhI971GXm1lu6nIJ86cig5HX2RYo7lb_SIItEMHwChPaNnuiJsLMye02nx0OCgl4YBtIaxkmKNWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل کمک‌های بشردوستانه به غزه را تا اطلاع ثانوی متوقف کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/126061" target="_blank">📅 01:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126060">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KA_MWGWtHPTtyTOocWy1EBhMeQz1svx5oi6WISMUTv75N7rXUAlMNQ4Ym2SCTpv5C9p6LItmQZ4wrso4AYllVtPCfX7qk35_ej0ssZsjx_uIpzFVVPvDa_7n7v8PqQzseYa2xjcL9tV4Mwdvz1ISncYrL5FrlmFMzUWnnCS24TsRQxA1UxaYpdQK_S8VdPWTvNg-LoqhC7dz29kL02YCY6TkaoUpbhG2qbfHuVrUzQ3_CPYWfAM6mHukpJubHsUNKXoDRGFsQBad2GQ4sowrsbOfc2g3ZUYcPiTxxvMePVRvkmnNEGJLS-xa_AWScxBRr9XggvqTVyu_ApWQ3KxliQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نتانیاهو وارد یه جلسه امنیتی گسترده با وزیر جنگ، فرماندهان ارتش و موساد شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/126060" target="_blank">📅 01:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126059">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">📱
لطفا توییتر الونیوز رو دنبال کنین
🔴
پست های انگلیسی در رابطه با جنایت های حکومت به انگلیسی نوشته شده و افراد مهم منشن و هشتگ های مهم قرار داده شده.
🔴
ریپست کنین. مهمترین کمک این روزها جلوگیری از پروپاگاندا حکومت علیه این قتل عام مردم هستش. خونشون نباید پایمال…</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/126059" target="_blank">📅 01:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126057">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">💢
فووووووووری/جنگنده‌های اسرائیلی پرواز کردن و فعلا معلوم نیست به مقصد کجا
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/126057" target="_blank">📅 01:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126056">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
کانال 11 عبری: ایران از طریق واسطه‌ها پیامی به اسرائیل فرستاده است که تهران حملات خود به اسرائیل را به پایان رسانده و حملات بیشتری انجام نخواهد داد مگر اینکه اسرائیل حمله کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/126056" target="_blank">📅 01:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126055">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKEKZ2GJEQQ9Lo1CFnxWe7TTItRYeQgm7n3aAbwAVKoSVtM4BpdjuCnN_jGxe4x7wc-LUfFQeGt7YW-oMBbvCHLbEGqsCkM-naks4M_uiOjsH8zhKj9_b4e1Tb-BvE3fXbY6Uz7WmFcs1uJ6FtYe9aT3xsAqZq2LmZRbwqWJyEsVGpv-_T7aBrFdnJunAeLmcQasBBhFg_IkjsvUms_6aFJId1P4iJTS4vp1TSnzYGNqBQ1djO1vm8Plb5emanD4sGFDZ3MsdodwWliHgxHQIUnavtKdB3jjtjAPOYGV4vsvz8huE3RJu32yoxnZJ_ZBDEdnrNJAxlEkRnIXXpe13w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مهدی مطهرنیا: درگیری ایران و اسرائیل بخشی از بازآرایی نظم جهانی است. ایران برای حفظ بازدارندگی اقدام کرده و اسرائیل نیز احتمالاً پاسخی کنترل‌شده خواهد داد تا هم اعتبار بازدارندگی خود را حفظ کند و هم از گسترش بحران جلوگیری شود. آمریکا نیز به‌دنبال مدیریت تنش و جلوگیری از جنگی فراگیر است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/126055" target="_blank">📅 01:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126054">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
ایران به سمت گروه های کرد مخالف ایرانی در سلیمانیه عراق پهپاد شلیک کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/126054" target="_blank">📅 01:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126053">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/187389113b.mp4?token=d6UA1-q4dbmRFrKrNIYlscxAdThYVHG-NIW-3zUVnwFKNTrflQDpXRuz08fHWQcCNnNyR6BVt0sc4ibGKc1Oklk0q3Kz6ORcAnH99J_75r_1xEyIaxeGq_8J4XCyDz-22TAwetqVqCkH1XPzICVvJepcqyV3dO6YQ7750gMTy6gMCELhoiKcv7QVOonTv7QUAc2iiTviO-pDmeK6rhE9Jbt3eTlrkFVWpn4L0depZ3PtCBxxtjQx3U2UgovUyjDewRQN3lZc16uuEkLsDWP1DQtwVyMOspG_n7NXS-botza27i3DhBuuyBvnsYVDy2oapecMyVutYgz6cFvl5lbPFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/187389113b.mp4?token=d6UA1-q4dbmRFrKrNIYlscxAdThYVHG-NIW-3zUVnwFKNTrflQDpXRuz08fHWQcCNnNyR6BVt0sc4ibGKc1Oklk0q3Kz6ORcAnH99J_75r_1xEyIaxeGq_8J4XCyDz-22TAwetqVqCkH1XPzICVvJepcqyV3dO6YQ7750gMTy6gMCELhoiKcv7QVOonTv7QUAc2iiTviO-pDmeK6rhE9Jbt3eTlrkFVWpn4L0depZ3PtCBxxtjQx3U2UgovUyjDewRQN3lZc16uuEkLsDWP1DQtwVyMOspG_n7NXS-botza27i3DhBuuyBvnsYVDy2oapecMyVutYgz6cFvl5lbPFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سوتی عجیب در شبکه خبر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/126053" target="_blank">📅 01:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126052">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
خبرنگار شبکه ۱۴ اسرائیل:‌ احتمال پاسخ قدرتمند آمریکا و اسرائیل ضعیف است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/126052" target="_blank">📅 01:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126051">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: آمریکا تا الان برای اجرای حمله علیه ایران موافقت نکرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/126051" target="_blank">📅 01:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126050">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Mt7lUCZGpsL3wHPj2wSocVdm-x-NA0ns-y8xZwF9d7uU-AxHUEEnXSzVyknNaCAudwNN2X-RwtXFiBzYiy2JuiorHI8Et7v5qRY6KnyJg5h5f1cqiLLu2SYYpHEPZPpKNIA11wdAabzfip_cpV0VOpzGgcchawo4LhqhmGVy3-WbMKHV5peWyhsg4oAaOonOSSwMSi7dsk8kq1NLsNB6WB0AEwWF6EVX-LXmxmlcJ1u-I4gGe0DScWPpFksMqmF6MKPN6Qn7a7nUaNYiICxTy8MNuXdSx5J5tUXM7HvgOKCzxqHchZYqnpXV-4HJpZTOuoEnh7Hrm7-u2eerESowdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ:
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/126050" target="_blank">📅 01:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126049">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
جنگ اینبار بخاطر تروریستهای حزب الله شروع شد و قراره زندگی مردم ایران رو تحت شعاع قرار بده.
🤔
ایران برای جمهوری اسلامی و عرزشی های حرام زاده وطن نیست، بلکه یک مقر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/126049" target="_blank">📅 01:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126048">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
شبکه کان اسرائیل: رئیس ستاد کل ارتش اسرائیل، ایال زامیر، در ۲۴ ساعت گذشته دو گفت‌وگو با فرمانده سنتکام (فرماندهی مرکزی ایالات متحده)، دریاسالار برد کوپر، انجام داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/126048" target="_blank">📅 01:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126047">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
فوری/یدیعوت آحارونوت: بر اساس گزارش‌های دریافتی، در گفتگویی که کمی پیش به پایان رسید، نتانیاهو به ترامپ اطلاع داد که قصد حمله‌ای قدرتمند به ایران را دارد. رئیس‌جمهور آمریکا روشن کرد که اگر چنین حمله‌ای انجام شود، آمریکایی‌ها در آن شرکت نخواهند کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/126047" target="_blank">📅 01:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126046">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ترامپ به آکسیوس: من نمی‌خواهم این توافق به دلیل تشدید تنش‌های فعلی بین ایران و اسرائیل از بین برود، زیرا این یک توافق خوب است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/126046" target="_blank">📅 01:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126045">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
والا به نقل از یک مقام ارشد اسرائیلی: پاسخ مورد انتظار به ایران سخت و گسترده خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/126045" target="_blank">📅 00:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126044">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sU9Hqm6A9ugBnig6oNF_A2iaH7dYyz_9_7g0DZ7woPIriNRy1aMnUeFTd8wih8O685YPrMA3YPuPQNSwtbfJ5i9bNO56UxIsEpxmwnMi6ncmRkLZjWA2eUxZ2sRt_t-bh0CkRq0IzBgrV2dWuXHnJqNTh6KrNYm3E7wSj1-4WGbbHFo7YXCVcUI642Ox4mwrkCP0Vlcfb5C6mOy9VRQXCCQhd74n-zhv6QEKge5nnQmrttF5vviaTbAcPuVWlm4VYbKcGn8TDcs9zAVC0LIbWeFdpdEgzNN4tgwB4UiqTqegyQYwAHqYwGBaSqAJcUE--7RcfjgxkKwvMm-Pq-8l-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: خو اومد زد
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/126044" target="_blank">📅 00:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126043">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
یک مقام آمریکایی به اکسیوس: ما بخشی از این عملیات نیستیم.
🔴
اما هنوز مشخص نیست که آیا دونالد ترامپ به ارتش آمریکا دستور خواهد داد که در صورت حمله احتمالی اسرائیل به ایران، هیچ کمکی به اسرائیل نکند یا نه؛ به‌ویژه در زمینه‌هایی مانند سوخت‌رسانی هوایی و سایر هماهنگی‌های نظامی.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/126043" target="_blank">📅 00:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126042">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tl_fYztEpGm128dYsevDpeb1RQnOf49_LN7gF5JVOP0YSP3T6J4otfsESLauTSSLX2mA3eIqWxVICzHpM0NaHdXMJKqK1eiwdGD2QnxnDBAeknCNqasxdP4UGJs4eXTm0SPj_JcYLQKyYnj_m_iPXVAmvca3ye8XHK30NhcJJTOmZN_o20t6LT5sPyS_G4zJn8yAs77UKcug-jh1oO2YFOdRM_RcMsaMvqW4R5dYMyqE3MbhlmVsnrDqzyAcyOjmexJ4Zi7k--FmPorjoNLz0L3RIf4_RZ_V3UVnu7P9mRduP_7_PQO1NqP_kzmmmiEF4gG4H8DxAyTSU35p06ubEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وای نت: آمریکا به اسرائیل گفته بهتره چند روز صبر کنه ببینن آیا امکان توافق هست یا نه
🔴
اگه نه، طبق «طرح اقدام مشترک» جلو می‌رن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/126042" target="_blank">📅 00:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126041">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
خبرگزاری ایرنا:
پروازهای فرودگاه امام خمینی تهران فعلاً تا اطلاع بعدی متوقف شده و هیچ پروازی انجام نمی‌شه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/126041" target="_blank">📅 00:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126040">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNbpcTK3wVc-UQMtD8jUozuOCCCl2A3HpHyr7iKz-1z1PzWC5n0NJK7CEOuyEBCm-D0bPzY5-yc2WWn1aYnt4TGReADq4G8hsYlT4xwDXEYFIH-Gs2M_czgoTuK6nzdYc7_SfrEYpRulUgL0W-lpgCXpZeOeJscntxswufazdjadnzdYiYXYJx_WTyZAgMzDw4T3rg-h_4ogefiwnCvGeI8gkYbvZ__L41ruogRLb1ROWphKQ6XppMqwZjZu1ChQHc2sVrEwLLcUbMfFaCImaa11gyKZrjinmuJAp5K7OysIuNFNzo1JbvOrMt_dUlN9D4fs18Wo2O1NfhBjUKV8TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم:
اسرائیل و آمریکا جرات حمله رو ندارن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/126040" target="_blank">📅 00:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126039">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
جمهوری اسلامی و عرزشی های حرام زاده علنا نشان می‌دهند که ‎لبنان برایشان از جان مردم ‎ایران و کشور ایران مهم‌تر است.
🤔
اینا با چه زبانی بگن که ایرانی نیستن؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/126039" target="_blank">📅 00:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126038">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
کانال ۱۵ اسرائیل:
پس از پایان گفتگوی نتانیاهو و ترامپ، نخست‌وزیر جلسه گسترده‌ای درباره موضوع ایران برگزار خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/126038" target="_blank">📅 00:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126037">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ww3AzQz9sYYoG4VPMA6lJK-I1r8k-X6f3dVRgLezOVGuYjEprKkPimEVXLAQGtpY1vbDosK1Uj0GpLbH_xlJq9Ii4SAoAAIj9o4in9vIS-nIPSTlgGw7GGrSxJhWS9bqs4zkTK8n50eemkl55X6R3JYRMpX1fVJtGHkeVwtjdBtrQTGK4eyjx1epkzkPamXjz7XeiUIkNPpP92WMtNNraJ76iHhMUWBy5JsEinfG2TsFuOP07utQc0HmyFKV_6NPdC4JuW98QW74ZjV7MlBXz9Qho98GWYGAOpF6pC0ZL7PP8eNL3MCLCLlouJHeQuyII7cmfJaO9D1uQILCidy0iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفارت ایالات متحده در اورشلیم به همه کارمندان دولت ایالات متحده و خانواده‌هایشان دستور داده است که در محل خود پناه بگیرند و آماده باشند تا در صورت اعلام وضعیت قرمز، تا اطلاع ثانوی، به پناهگاه‌های محافظت‌شده منتقل شوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/126037" target="_blank">📅 00:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126036">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzuQ9O58MkwUhf2HlFU3m90ka5CbO0OATTlzmoDYWFNAild4IKH2s3megsgt44i4mDZDXa_ayfXdQtDB2YR4YY6QAeQ5eg2UUZ9Wydgpk7AOWhve9R94BrKdjVpcyQ-8Kh9RPHNqjENVU8hVAvRcL92ZlmpDQlmiX93j-S2y8VzCiWSdXC4YjMVPBNuAFLh9JIMgwi_LbbzJK4U9qoJDIouqNAkqokgTJxYWgHnwOnhsl50RdntTlgZUt-lgz1XfSBz8UCKwSKvlzVqJK26_FkxRGxCP_bQgFqJHkAh-fHKYoawgGaswqktb_CAx5A09xakOqyDpT3pZqpXJRV5ntA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: باید حملات رو ادامه بدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/126036" target="_blank">📅 00:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126035">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKTqJhYVoNPHGQt4xiZU9zdB3V5NAr5XdBhX8XsCgc60exH1FtMNakf4hig6GqnKYBgpkLTF09QPcEuHsbHbBFT7_hwfvChUU7AzcCia4JaLXhLmmjuv-1xO9kwSxirYsEGotVCU35OOqPdGqNGTJh8miJJ16x7t1mzTL9uK0WwAp-pG-1nD-QZvgc0TNeIL5EX-lOir0jnGOvRJ9gq4mkzJVbaIJ9ilWClFF-8moCRjEu_G2AbvTeIZvlasA3GUJyG_mz4pr_ic2fTgn58EezwkLpG2VhPWCJnLYt4Pzw3FpyvOHiCqYiePth6S3efvT5T9KH_ngElNU517_MNBHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تمام هواپیماهای غیرنظامی تو تهران برای پیش‌بینی حملات اسرائیل جابه‌جا شدن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/126035" target="_blank">📅 00:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126034">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
آمیکای اشتاین خبرنگار آی ۲۴:
«در طول یک ساعت آینده، یک بحث گسترده با حضور بنیامین نتانیاهو، وزیر جنگ، و فرماندهی عالی امنیتی درباره ایران آغاز خواهد شد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/126034" target="_blank">📅 00:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126033">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">💢
فوووووووووری/پرواز شدید جنگنده‌های آمریکایی در مرز ایران
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/126033" target="_blank">📅 00:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126032">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc3b1eadd2.mp4?token=B07DJAbuwUGFXlMMayBo1p3MjXS1ETu1DGaSqAsfqY07Lp-JidtpPd5A53TFtd-oiys80VWkTsHi-3gLGAG6Mj90JAwmuD6cw01IB72zRFxeLFItlfnd35t9Zjptgkfse48wTe0igEor53iZXhI__pyxZMm8Ak1LLqgB65gwVJOkXxK_e5puHt2xMUXoxgPOnY2yo49LVO5OlIssNYAi57-hLN4cspR3XalGcwwy2tMXihZRD1SrSaeXsLCKgwbvOtkwmbZ95aLz8LLxEt6F5DhxtaD4ba3smUeWRWqC-LMyug6oxUGRv1Hnj81Cbd25mXLhgRe_kdiM0teXJ1dkVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc3b1eadd2.mp4?token=B07DJAbuwUGFXlMMayBo1p3MjXS1ETu1DGaSqAsfqY07Lp-JidtpPd5A53TFtd-oiys80VWkTsHi-3gLGAG6Mj90JAwmuD6cw01IB72zRFxeLFItlfnd35t9Zjptgkfse48wTe0igEor53iZXhI__pyxZMm8Ak1LLqgB65gwVJOkXxK_e5puHt2xMUXoxgPOnY2yo49LVO5OlIssNYAi57-hLN4cspR3XalGcwwy2tMXihZRD1SrSaeXsLCKgwbvOtkwmbZ95aLz8LLxEt6F5DhxtaD4ba3smUeWRWqC-LMyug6oxUGRv1Hnj81Cbd25mXLhgRe_kdiM0teXJ1dkVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فاکس نیوز: با اینکه ترامپ به اسرائیل گفته پاسخ نده اما اسرائیل همین الان جلسه اضطراری تشکیل داده تا تصمیم بگیره آیا به حملات اخیر پاسخ می‌ده یا نه؛ و اگه پاسخ بده، چطور این کار رو انجام خواهد داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/126032" target="_blank">📅 00:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126031">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
اسرائیل بازم به لبنان حمله کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/126031" target="_blank">📅 00:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126030">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gm3WuikJX6iYGEj5rKPIwOLirk6ipdX9XnAmk1kHd70AIplqmBEBxnVnhLdJiY334Th_X_AfVGiYEwIcxG8wLFBfXrgDfbyH2yLzTeBlEE2d4qNMUbtQvUtdrm23vJvAbUCOxVwBEcS8dngoKGtJktJ_YFvvP7ese2JWKEMHZy19K5_YlinLFrM05sH4hMSSVcVdV95LkNJYoTmSpeDjzWAmPEG-d8JP4jN2KstqNAbcTgmYu627G7QPrO2Fn_n7L-pjKJkzBkWmFwuQDHNxTuusTQYsewITQjvgazU8Vxd03BkaqCK32Kj8RbqyGHPznDGXUUEpQchMS4THI3-vhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایران اطلاعیه NOTAM صادر کرده است که بخش غربی فضای هوایی تهران را تا ۸ ژوئن به روی تمام ترافیک هوایی غیرنظامی می‌بندد.
🔴
تنها هواپیماهای نظامی، دولتی، تخلیه پزشکی و جست‌وجو و نجات مجاز به فعالیت در این منطقه محدود شده هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/126030" target="_blank">📅 00:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126029">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
چپ و راست داره از فرودگاه مهرآباد تهران هواپیما بلند میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/126029" target="_blank">📅 00:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126028">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
هم اکنون قیصر در میدان انقلاب: پیک‌ها همه بالا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/126028" target="_blank">📅 00:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126027">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
وزارت خارجه پاکستان: ایران نشانه‌هایی از پیشرفت را در راستای تصویب یادداشت تفاهم نشان داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/126027" target="_blank">📅 00:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126026">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
وزیر خارجه عربستان سعودی به صورت تلفنی با همتای قطری خود تحولات اوضاع و پیامدهای آن بر منطقه را بررسی کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/126026" target="_blank">📅 00:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126025">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
طبق گزارش i24 نیوز، نخست‌وزیر اسرائیل نتانیاهو، وزیر دفاع کاتز و رهبری امنیتی اسرائیل قرار است در ساعت آینده جلسه اضطراری درباره ایران برگزار کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/126025" target="_blank">📅 00:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126024">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbac3626bc.mp4?token=na2y6xcnsXRowEttmPktQyDHZabhiwqZMa5SV4d-iZXa7IkNhPg8XZU1ToUMMdKBhN1YgW0wchXzY9Vs42TIZGgxY5KyD4eiRLiZnSdrlcUifJvJ9iGfbZBgoxDkL_UEPp2Jl-_J1iEDRQ7RYjhO5JSrmp6kjL0pqBFRr5eOqYF1yz73vpW6B1QydVvm64fmBm13T30RPyGru9utU2F9q63nrGv-bf2zirwBYKYhsLqreD1gdPjRe7L4-EGOxw9m0x5BDuWY5bvuwLgzHmZFXxaBoBpA-GqXYpzt2YPvLRfE76QCR72ZD2ja3pIV_QI2D3msfvuod-I7aTPx4VTF7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbac3626bc.mp4?token=na2y6xcnsXRowEttmPktQyDHZabhiwqZMa5SV4d-iZXa7IkNhPg8XZU1ToUMMdKBhN1YgW0wchXzY9Vs42TIZGgxY5KyD4eiRLiZnSdrlcUifJvJ9iGfbZBgoxDkL_UEPp2Jl-_J1iEDRQ7RYjhO5JSrmp6kjL0pqBFRr5eOqYF1yz73vpW6B1QydVvm64fmBm13T30RPyGru9utU2F9q63nrGv-bf2zirwBYKYhsLqreD1gdPjRe7L4-EGOxw9m0x5BDuWY5bvuwLgzHmZFXxaBoBpA-GqXYpzt2YPvLRfE76QCR72ZD2ja3pIV_QI2D3msfvuod-I7aTPx4VTF7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک پهپاد ناشناس، احتمالاً یک پهپاد نظارتی آمریکایی یا اسرائیلی، در استان کربلا در مرکز عراق سرنگون شد.
🔴
این اتفاق تقریباً همزمان با حمله موشکی بالستیک ایران رخ داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/126024" target="_blank">📅 00:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126023">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
تسنیم: منبع نظامی به ما گفت موشک ها آماده اند که در صورت جواب اسرائیل فورا شلیک شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/126023" target="_blank">📅 00:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126022">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
صدای شنیده شده در‌فرودگاه تبریز تست پدافند بوده و هیچ‌گونه حمله‌ای به این فرودگاه اتفاق نیفتاده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/126022" target="_blank">📅 00:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126021">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
خبرگزاری MSN به نقل از یک منبع در وزارت خارجه پاکستان مدعی شد: سفر وزیر کشور به تهران مثبت بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/126021" target="_blank">📅 00:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126020">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
پروازها به عراق به دلیل بسته شدن حریم هوایی لغو شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/126020" target="_blank">📅 00:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126019">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
نیویورک تایمز، به نقل از وزارت امور خارجه ایالات متحده: ۲۲ ژوئن به عنوان تاریخ دور جدید مذاکرات بین اسرائیل و لبنان تعیین شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/126019" target="_blank">📅 00:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126018">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
منابع عبری:ترامپ و نتانیاهو در حال حاضر در حال گفتگو هستن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/126018" target="_blank">📅 00:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126017">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mfu3WSFfGRYGogesqYZB0lU50J8uj9gLJ0joK7m6V2s6OrMEFVRWL8pG-grjtdepOVdXBYDYy3otKPWBU32OcRZwN4Wc4EAwlYt8vjggzDsfFoYVv7e_3sMBB6VEpFdKWnRF2vwOepeAYru7P-BaA1fL8_NRfI0Z0A5eIEQEUryO9Os5C9XzEiAXRTWloCISJT-6HsbHXHOl6L6LwvU5quzp9Yr2YEq12WPTT4p-hfV_M_5zLTgvJ_eL16GDJW98MpL0brNki2ysw8OmyLcxCeqW8KB784vhFSSfobbwCJz77Cxh5AbyzRFEmwb6ZSCw9Nc5jb5P1mXnzt8KP6p0hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال 12 اسرائیل:
مخالفان نتانیاهو در عرصه سیاسی اسرائیل از این وضعیت سوءاستفاده خواهند کرد و از سوی دیگر، نخست وزیر نمی‌تواند تنها چند ماه پیش از انتخابات به چنین وضعیتی(ترامپ مانع حمله شود) تن دهد، زیرا این امر می‌تواند برای او یک فاجعه سیاسی تلقی شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/126017" target="_blank">📅 00:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126016">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O1Wf65h6xL6zvfe271ztkPfOT2h870CLfkm1bMhi5tSqCyJ3_1N1uql6G2W1FgfG6LITC1yQ2BEyKDYa3ke1Qgxm7nKULHAlEI48_v3d0k5xF9CPV3dnYHA0qOw6w4pVtA_QxN_b4U8QFbjQs9r_PG80v93kncZNdczep28FkLivrf-jDL0gOVTjZtKW_vTtBFqfDaKGbbR6dvfhGElFCM7LJ625hixmTcry1fP0jl1557bB6G0gPWR8phsfogRvOp62wOGqn5UDFQFBKM9iWTLEDR4hNlF8vbrtTnj3WecAbQrtjcKpXIngCuJ1tsFFBC-uZlsD6pey6InxwXdOhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم‌اکنون  ، وضعیت آسمان منطقه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/126016" target="_blank">📅 00:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126014">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0889c9dd3.mp4?token=nLqH-7N3Nht44OuT5w53Fd_wLwDw51LvMRRxA3aqb3xuyATXbPyoEmxVeKI2aM5LpmVtU1NmazR6i5Bq_AdjukdibOngJXv7ChlghPpl7roYjz-_TwoOB78o_DAjw7USYLlC-BoyFcy_N5fqKw1PNFWDEMApXEDvrP8GTFmBUnAbKdwZaKRQeJoVNvJRndNdID3PRNFDofSYh8JTXQ1M8GNcBFU5PMceB_yzJYIOYK2xBg3ZdmZlAI2Tn-Jqlv1p2KoaUoJ4w_2-tTCdeSzt9VT2Vy2y0yHrA89K-8bYPSjxaPwtVLmqo29BFYVsLVZbU2bzhtaeo3RROndWaaFy_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0889c9dd3.mp4?token=nLqH-7N3Nht44OuT5w53Fd_wLwDw51LvMRRxA3aqb3xuyATXbPyoEmxVeKI2aM5LpmVtU1NmazR6i5Bq_AdjukdibOngJXv7ChlghPpl7roYjz-_TwoOB78o_DAjw7USYLlC-BoyFcy_N5fqKw1PNFWDEMApXEDvrP8GTFmBUnAbKdwZaKRQeJoVNvJRndNdID3PRNFDofSYh8JTXQ1M8GNcBFU5PMceB_yzJYIOYK2xBg3ZdmZlAI2Tn-Jqlv1p2KoaUoJ4w_2-tTCdeSzt9VT2Vy2y0yHrA89K-8bYPSjxaPwtVLmqo29BFYVsLVZbU2bzhtaeo3RROndWaaFy_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گویا هواپیماها از فرودگاه مهرآباد درحال تخلیه شدن هستن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/126014" target="_blank">📅 00:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126013">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: امشب فقط موشک‌ها و جت‌ها نیستند که بین آسمان و زمین در نوسان هستند، بلکه سرنوشت سیاسی نتانیاهو نیز همین گونه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/126013" target="_blank">📅 00:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126012">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
جمهوری اسلامی و عرزشی های حرام زاده علنا نشان می‌دهند که ‎لبنان برایشان از جان مردم ‎ایران و کشور ایران مهم‌تر است.
🤔
اینا با چه زبانی بگن که ایرانی نیستن؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/126012" target="_blank">📅 00:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126011">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12488477e1.mp4?token=f3qsczWWUXUNEgA8q8nel2NFti5YxFkU9mInOu5TRPFWDUea02vzIfOV5Gjp4Gedn60CQIm_wHYcTHzbK4HIxw6cgBJ9ccjEPXorqCONTnbuO5VUOZnNcQfUldBOTYXZ53BIoci9N29oJL33LCZw2n51siVz5kyrU-PnNYQbsh6cf76E8WaU_XmW3oaH5khs3zBG3F-DaGxzi3Jk6ZDOKYiRjJDVX8omMrUgx-n8GBxuN2VE4ns0gZ-NvddR2VwtZZUAmIT9Wwsn94nw8GWAfyphvbAexTQ7DoknpsvCPMNT6HMwQxj5aYbFj0ZtbBWjej3eGm5NHFA1orzYAYsY3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12488477e1.mp4?token=f3qsczWWUXUNEgA8q8nel2NFti5YxFkU9mInOu5TRPFWDUea02vzIfOV5Gjp4Gedn60CQIm_wHYcTHzbK4HIxw6cgBJ9ccjEPXorqCONTnbuO5VUOZnNcQfUldBOTYXZ53BIoci9N29oJL33LCZw2n51siVz5kyrU-PnNYQbsh6cf76E8WaU_XmW3oaH5khs3zBG3F-DaGxzi3Jk6ZDOKYiRjJDVX8omMrUgx-n8GBxuN2VE4ns0gZ-NvddR2VwtZZUAmIT9Wwsn94nw8GWAfyphvbAexTQ7DoknpsvCPMNT6HMwQxj5aYbFj0ZtbBWjej3eGm5NHFA1orzYAYsY3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایای موشک ایرانی در دشت‌های شمالی شهر تفس در جنوب سوریه سقوط کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/126011" target="_blank">📅 00:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126009">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
نت تو پاکستان قطع شد جنگ شروع شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/126009" target="_blank">📅 00:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126008">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
منابع عراقی: نیروهای امنیتی در عراق هشدار جدیدی در نزدیکی منطقه سبز و فرودگاه بغداد اعلام کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/126008" target="_blank">📅 00:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126007">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: رقبای نتانیاهو در عرصه سیاسی اسرائیل از این وضعیت سوءاستفاده خواهند کرد.
🔴
از سوی دیگر، نتانیاهو نمی‌تواند چند ماه پیش از انتخابات به چنین وضعیتی برسد، زیرا این می‌تواند فاجعه‌ای سیاسی برای او باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/126007" target="_blank">📅 00:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126006">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
ارتش اسرائیل می‌گوید به عملیات خود در سراسر لبنان ادامه خواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/126006" target="_blank">📅 00:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126005">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
کانال ۱۲ عبری: به دنبال وضعیت امنیتی، کنست (مجلس اسرائیل) چندین جلسه که برای فردا برنامه‌ریزی شده بود را لغو کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/126005" target="_blank">📅 00:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126004">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
ترامپ به نیویورک پست: در حال حاضر نتوانستیم با نتانیاهو تماس بر قرار کنیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/126004" target="_blank">📅 00:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126003">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ترامپ به نیویورک پست: «اوضاع بسیار خوب پیش می‌رود.»
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/126003" target="_blank">📅 00:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126002">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
ترامپ به نیویورک پست: «اوضاع بسیار خوب پیش می‌رود.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/126002" target="_blank">📅 00:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126001">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
اسرائیل: آماده شلیک موشک‌های بیشتری از ایران هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/126001" target="_blank">📅 00:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126000">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
حریم هوایی سوریه نیز بسته شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/126000" target="_blank">📅 00:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125999">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
تماس های تلفنی عراقچی با وزرای خارجه فرانسه و قطر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/125999" target="_blank">📅 00:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125998">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
سخنگوی ارتش اسرائیل: ما برای احتمال ادامه حملات آتش به سمت خود آماده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/125998" target="_blank">📅 00:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125997">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
سخنگوی ارتش اسرائیل در یک کنفرانس مطبوعاتی ادعا کرد که رئیس ستاد ارتش، ایال زامیر، در حال ارزیابی وضعیت است و «طرح‌هایی را برای آینده تصویب می‌کند»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/125997" target="_blank">📅 00:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125996">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
فوری /  سخنگوی ارتش اسرائیل: ایران اشتباه بزرگی مرتکب شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/125996" target="_blank">📅 00:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125995">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
تابناک: پدافند در بخش محدودی از غرب تهران فعال شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/125995" target="_blank">📅 23:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125994">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
صداها در تبریز مربوط به پدافنده
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/125994" target="_blank">📅 23:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125993">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
ارتش اسرائیل به زودی بیانیه ای صادر خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/125993" target="_blank">📅 23:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125992">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
صداها در تبریز مربوط به پدافنده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/125992" target="_blank">📅 23:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125991">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
ترامپ به باراک راوید: هر کدام از آنها خوش گذراندند. اسرائیل حمله خود را انجام داد و ایران هم حمله خود را. ما به حمله دیگری نیاز نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/125991" target="_blank">📅 23:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125990">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
العربی الجدید: رئیس سازمان هوانوردی غیرنظامی عراق سقوط یک هواپیمای مسافربری در عراق را تکذیب می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/125990" target="_blank">📅 23:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125989">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
ترامپ:
منم با اینا مشکل دارم ولی بحث بحثه وطنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/125989" target="_blank">📅 23:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125988">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
ترامپ : «در حمله موشکی هیچ‌کس آسیب ندید. اگر نتانیاهو پاسخ بدهد، این روند ادامه پیدا خواهد کرد و ادامه خواهد داشت.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/125988" target="_blank">📅 23:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125987">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
تماس‌های تلفنی عراقچی با وزرای خارجه انگلیس و ترکیه و فرمانده ارتش پاکستان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/125987" target="_blank">📅 23:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125986">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89e3d13213.mp4?token=Jzq_MCig2RpaQ2fN-LdEax1Ka5ftI3BFvFZKVqHU70QSObWDbs0oS86d_pXUT_w9eqeKwmmURKLIpnTtNLbZvGf8oAqyjVQaY2H21s9htbc5lU4_Ft1QTR9nJsHpig89oKILGYHPIicrNn2mDe0DQxWuWoeTweKlv_iUP4UQEX18QB16ZTR2-ntI_El5y2X23ewC5eg-pgLK8WQEe3jHk8SGpKL5NORYGHWA0zNwfkOzNBuv98ub7EL5grj4wTaZWCTk6wg3y0tSgmH01vZUxm7iiDGd_NpHm7lC5QvYSSF1U16PYwwTE0qInUQ0Lwl1EKuEEihi5qFn-zd30IexmoUXIS0Ey23MAcIMV02D9VMoZES6zhKB-pGLqN2_2th5jQFQC0bp25eqS7zw6mXAzhm6jXLOOqIakO19D5SG3lE1ph0ghr0_TcQR1E08KBB3Mr23rCPfO2Aak4NfDm768olboIiYZ4Zx9qJ4md-iym8NuxPlC5IAHXQfs9vrkiMxchYa4ArDzPipZmmXqU_KxV--v3UbJd2j10CK_RohabiLi98XTuihzSBOB0JWEXMLf6HFoiNHsxaS3JmzbNyIHmxaDg58h367fKy2H4NrzLucPdA-aJU2SoFd21f6S1kew2g61q-GC3y9lLBeHlhS6KCFRMQzCxO3dffvDXCqfeE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89e3d13213.mp4?token=Jzq_MCig2RpaQ2fN-LdEax1Ka5ftI3BFvFZKVqHU70QSObWDbs0oS86d_pXUT_w9eqeKwmmURKLIpnTtNLbZvGf8oAqyjVQaY2H21s9htbc5lU4_Ft1QTR9nJsHpig89oKILGYHPIicrNn2mDe0DQxWuWoeTweKlv_iUP4UQEX18QB16ZTR2-ntI_El5y2X23ewC5eg-pgLK8WQEe3jHk8SGpKL5NORYGHWA0zNwfkOzNBuv98ub7EL5grj4wTaZWCTk6wg3y0tSgmH01vZUxm7iiDGd_NpHm7lC5QvYSSF1U16PYwwTE0qInUQ0Lwl1EKuEEihi5qFn-zd30IexmoUXIS0Ey23MAcIMV02D9VMoZES6zhKB-pGLqN2_2th5jQFQC0bp25eqS7zw6mXAzhm6jXLOOqIakO19D5SG3lE1ph0ghr0_TcQR1E08KBB3Mr23rCPfO2Aak4NfDm768olboIiYZ4Zx9qJ4md-iym8NuxPlC5IAHXQfs9vrkiMxchYa4ArDzPipZmmXqU_KxV--v3UbJd2j10CK_RohabiLi98XTuihzSBOB0JWEXMLf6HFoiNHsxaS3JmzbNyIHmxaDg58h367fKy2H4NrzLucPdA-aJU2SoFd21f6S1kew2g61q-GC3y9lLBeHlhS6KCFRMQzCxO3dffvDXCqfeE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بیانیه قرارگاه خاتم الانبیا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/125986" target="_blank">📅 23:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125985">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
ترامپ بزودی:
و من نصر الی من عندالله عزیز الحکیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/125985" target="_blank">📅 23:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125984">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/or5DyRxsSRLEXsgcAfz7Ihjbki3gf46247MTX4JMEIWOukXuxfe8Dyr_Afc8xtSsxEUlPykkAg7PPQbLjlAPPC0AZp8Phsksv6GTengQcaIVGObEcm6DJ9IO1OygvCYdiGW_T4-tf6eKX-G_afpSmLwAWTB5MZvAGgKZJ2YileeLGMkndkvU1b-BAWkyvFMok9LfCPVvk-xVpyYWG3KksVyfrC1Zx9eAlrsxIUTTlQggIM9NIjoaeEFUK_keXTaA0XvFFv4Rmx9k-joXdWLlCD0tkNXyc_lq8DiSjHIdE5Hsvbc7dZLZtbqHQutrGaHovGfhKCrS8wu_buW5VYfFGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید خبرنگار آکسیوس هم تایید کرد، ترامپ زنگ زده به نتانیاهو که به حملات ایران پاسخ نده!!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/125984" target="_blank">📅 23:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125983">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07f9652347.mp4?token=rWnCHnKuT5vY7G97BZ9rdJRDm4oSnx9qx54_Gga7vjHn5tzwcBkWc2dWjIvdAeu2di2ulUqTDjyqZIyVkemaYOYRY7OOk9S5IuP4S8WhNiU0s1W1i4zPstFHui_U2R5V5E9EUFuU-EJ9V-MlNiLhIv6tbVWcjr4ftKJSAuWiChWcu1jpPZIsjHIcS_xvq7ISQR_PUHfED9Em9msI7TXcsVk3ZTcaoOFI9vbN1S1mOR5LvRgby_RjSgULz--llEZVznCgiTWcr5t71qDg35KYq8aoKSEF18iIaSerrwCY5-xm2qODCcV4h7scBe-ZYDqin3qJ95GorO0Tiytt_On8sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07f9652347.mp4?token=rWnCHnKuT5vY7G97BZ9rdJRDm4oSnx9qx54_Gga7vjHn5tzwcBkWc2dWjIvdAeu2di2ulUqTDjyqZIyVkemaYOYRY7OOk9S5IuP4S8WhNiU0s1W1i4zPstFHui_U2R5V5E9EUFuU-EJ9V-MlNiLhIv6tbVWcjr4ftKJSAuWiChWcu1jpPZIsjHIcS_xvq7ISQR_PUHfED9Em9msI7TXcsVk3ZTcaoOFI9vbN1S1mOR5LvRgby_RjSgULz--llEZVznCgiTWcr5t71qDg35KYq8aoKSEF18iIaSerrwCY5-xm2qODCcV4h7scBe-ZYDqin3qJ95GorO0Tiytt_On8sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر واضحی از لحظه اصابت موشک ایران به هدف خود در اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/125983" target="_blank">📅 23:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125982">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ترامپ به خبرگزاری کان: فکر می‌کنم اسرائیل به اندازه کافی واکنش نشان داده است. دیگر نیازی به واکنش بیشتر نیست.
🔴
ما می‌توانیم پس از ۳۰۰۰ سال به صلح دست یابیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/125982" target="_blank">📅 23:48 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

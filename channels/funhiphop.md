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
<img src="https://cdn4.telesco.pe/file/sKFWNxPpngTFxR8rB8D1vP4VGx5HkIUknD6dxQBBnXsT_e_dj15kE8TIJoYX8qj8flqB3ROIrIAC7ZMc0LFMVjPHZmBsJozjLF4xb_t-DELs5u9t9Po1mGFdTC60oDxbxeyFcW92urjOmeALcF5RPn_nI34629G6bN3_MRkCVMyT5rPeilLSWb32q-VVsFpWJUeiiqNDZeQK51WDfq00V8PuZvieuJBssJtaMT7hQUsn_e5EKytVq4oRIULn804WiITMH1keKiVxLCNbogW_ZXC0uwUSAhqZ2xvoLc4q-vMgZHVR-nDdQ6jzWmY1Am1yJLpAB6NY6O9CZ-WL0eCAsA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 179K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-09 19:29:26</div>
<hr>

<div class="tg-post" id="msg-76347">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">هم فنای فوتبال عقب موندن هم فنای هیپ هاپ، برا همینم اکثر کسایی که رپ گوش میدن فوتبالی هم هستن و برعکس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/funhiphop/76347" target="_blank">📅 19:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76345">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دوستان به صورت قاطع فضای فان هیپ هاپ برا فوتبال مناسبه یا هیپ هاپ
فوتبال
💘
هیپ هاپ
🦄</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/funhiphop/76345" target="_blank">📅 19:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76344">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">شما منتظر فینال سی ال اید من منتظر گیم هفت سری اسپرز تاندر تو‌ Nba  پ‌ن: فهمیدید شاخم یا بیشتر ادامه بدم   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/funhiphop/76344" target="_blank">📅 18:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76343">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">جدی چرا اینقد آرسنال منفوره
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/funhiphop/76343" target="_blank">📅 18:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76342">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEfHNMdVY824aYgIxJGmmvZkZ1qg6_pk9G0Itt82fb0aV3vIweSeYg9hjnxENtGAjNxdLq26v1XEtQdsRq6j9pXwucDSt5p5poxPgNvgd4UIAGWhw_5POtt6aQGwBSN_KccJazF7pUOxUqeua-5P_w8fVbarY3xlT30UN3hS_7TXS6QOCDx46Bhoo945x2VgeKtpUC7chiPaLg2GO9KCN6LRbjoOXljE2MvPs5a2pyIGR2L4cb9GnEadQE6kbTEC_ROlBnSpaghz1q6Ybb3OJ-xOXHCOLPN1zJJs4gIe671LgyVRJ_EXP4yEAL75zNyAyeRSKv7WaEK5KB7UI0Phyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیدمجید نقطه زن، کاخ سفید رو شخم بزن
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/funhiphop/76342" target="_blank">📅 18:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76341">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">شما منتظر فینال سی ال اید من منتظر گیم هفت سری اسپرز تاندر تو‌ Nba
پ‌ن: فهمیدید شاخم یا بیشتر ادامه بدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/funhiphop/76341" target="_blank">📅 17:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76340">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMImqoSp0jVizWsLP_PMEUdGPoXiKUV3lOKYvHdyXm34LFMT7cIZyW7UmZc5_D-yNFOjJXCsJ6fXm32OdFnUhNJu3qCX_8nV1JPtan7jeQlKLz3y5BjoE_fj3209-mLu9RiJ5dzIwDitrhf1iIPIbrdhElM1oUb15P0DzmO6vFMETkbbgbaC8bhMyqHCy0mDQO3q1Nr9JLpZrfp_X2HG6sPD9Z_mGgWtP7kqeseVeZB-OYfYtcWGjcCfAIVZPoAcNRysF-jg_3HeFy-dO2AQyyobGH9cslAclKam1u39QBdJnfc3fDx7Y5XL-2KIf8Dl44j0Cwrc5xcM0xDj6gqlFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تایید؟
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/funhiphop/76340" target="_blank">📅 17:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76339">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmCe89m3lwhQbkTOnuISoM6ZEqyWbDo0RVYFIsr1k6PVLU92MUkwyfO7O4VL6e0Xf_MKlfSbPFSjr66Udn4LdsQaUSNgU7PxqMRRQ85uZRxCJeFfsIJrz5lI8Ao0BOezgbWX4pWaoPsI65LlLT97OEq_TnGuGq2JLsCea-2qF4EDKcmesldOal7VqZ3Hst6b2QvSM5OI2N1Necy-y4ozh1Net2gXGpof64McS61NY6ArFfbfpmKiXjlCcHrc3bN-rmTw5fPOV-6OjlxNbkYeN4CC-Vt6HSsx5EIG-nbLyWtfvu0tZCUP1fYMDQOCI4r03OrIWNZi1m8HzFhf6o6mrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشب ساندویچ کباب شامی رایگان از ساعت ۱۹ الی ۲۱
مشهد،نبش پیروزی ۱۴،رستوران پلنگی
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/funhiphop/76339" target="_blank">📅 17:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76338">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vfjd0oB1FcVwt6tUJDCR0vGPJVd6OfrqYNS-CpBVFv-exsLc5YoCxjv4XQLNYCtksogc6jHA_2_edOrc9b0_JETAbM3bj00szTjFwCfnNk8nF0FR_vtipj8zGCMdZDVkgET6thth0Q_bHDCqzm_d1B3fRXJLlwYgOnmR7YcEx5p48EXh5pI47F6NYBv3ByEiAd7_tA854ZizDwG2HCbAzBKrlXA9PihHJnKt61P7_Nl6ZEVPK0JSviPW2TA6hlURJumirXxQ7QihQLJz9CMDgqJd5NJbKxtrebWp16vcKQaT7U1nse0PZMS8JFC15VBzuzhgCbngtp_kMRx5N7zCww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
سایت بین المللی
bet120x
✖️
👍
دارای مجوز رسمی Gambling Judge سوئد
👍
💳
شارژ حساب از طریق ارز و
یووچر
و پرمیوم ووچر
💳
تسویه حساب دلاری سریع
💊
بیمه شرط میکس
⚠️
فروش شرط
🔔
ویرایش شرط
3️⃣
2️⃣
🎁
20%هدیه واریز از طریق ارز و ووچر
┅━━━━━━━━━━━
🎁
10%برگشت باخت به صورت روزانه
🎁
10%برگشت باخت به صورت هفتگی
🎁
10%برگشت باخت به صورت ماهانه
💻
ادرس ورود به سایت:
https://bet120x.com/fa/?btag=971470
➖
➖
➖
➖
➖
👈
آموزش واریز و برداشت دلاری
👉
🔪
کانال اطلاع رسانی:
👇
g9
🅰
✈️
https://t.me/+RvVnWMHCqUc4YzFk</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/funhiphop/76338" target="_blank">📅 17:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76337">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">تو کامنت نتیجه بازی امشب رو پیشبینی کنید
اولین نفری که بعد از اتمام بازی درست گفته باشه نتیجه رو
یک گیفت Nft میزنم برا اکانتش
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/funhiphop/76337" target="_blank">📅 17:13 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76336">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gybqzG-KfzASpp3_MlZoUaMkKvXqxWF2WXNBQ2QdtV27fFNe3W9vOH_l5YhBnTDVIJk_HxSRgq2FAKWNo0ITC4SrD7Xych07xj9_u2XhQTLE5CWceaE9JENYowguZM26qv74vOMkg1IcwqQDa4b7FXIogEaHw4zQ9SSgO9KDLTL7qDCtG0H-YgFsZ8mQqKuY58fg6l1oMZrxtf4WPzTMthq67PZUcHrnJPFSl1_ZLHPfYfr0fIIHot84VLRNH4GV6b8YJeptl9j-M7eko28zht6Wn-u2yTf10O9MFoSIoqYIwFBa-c9FYZzbMRkJ2tu0BNePfVn9PHbsEUd76Goo1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایا فرار کن این میخواد بخورتت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/funhiphop/76336" target="_blank">📅 16:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76335">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-W6eTELdi-lbSmJ6BhfJaLj4x1gF7-e_6JgFS0IomLEiqgEYJHL67UW_IW6SQC3GbMCFKonVvTkIQT9WAGNPXjD0AlpHtWQIvxzoMhDQ2E7q-nBLVs38xgSfUeAuq_8VXBw4XIgwwnYMzGo7i963D0B3hLxFleRJPyv2xJd9amy988MncL-q5L5C3foA-wnvcMX1Nf0dV7RVmcXHpwH3YQ4MKVBkVnE7dm-3fnFgaEUWJyPO8yFOvFthBCoDuwBJoKw0MR37h8G12t3FYdcc8tWLgE9Xh2I6eJpnqeL81702hPTHFe7bNbySv50C4lzpDdZza3VrT18OtiV37-UQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیدم مردم کوبا ازم کمک میخوان، میرم اونجا هم یه سر برینم امیدوارم اشتباه شده باشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/funhiphop/76335" target="_blank">📅 16:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76334">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSQmWupNPqrRuhxPc7nqaWPDUmtkO72hUvVczrOtsIS_2W7OKFmivCMJES_rpsfN7xBsymNJD8luL4W3FKOsdwOib8zTtwaqrlt8M-BEId_eeNvEZ0T5Gak_7LT5RUmiDB1PGDQubzn5mzqa6ujTtzg2RiurYJ4RfBM9l17hXEudR2LE9jMmbKOcjg65h687_M6mQyLRkwMwqfai5IieU1taeb3L_n7HBMBplAZppp7QEaQlAFEGdkLhwFybob8I5d6UuvTTC5jTGHjrYkEXvWMhiejxJL0JJaWR0vqg3U4ycxtm9XJirOB-w73RX6DHUvWoZxW1bwSI_2a-7t6laQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه عکستو فرستادی برا ChatGpt و پرامپت آنالیز جذابیت رو براش فرستادی، قطعاً و یقیناً کونی هستی  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/funhiphop/76334" target="_blank">📅 16:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76332">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اگه عکستو فرستادی برا ChatGpt و پرامپت آنالیز جذابیت رو براش فرستادی، قطعاً و یقیناً کونی هستی
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/funhiphop/76332" target="_blank">📅 16:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76331">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سلام به دوستان عزیز در خدمتتون هستم با برنامه فوتبال با فرید   آرسنالِ آرتتا تیمیه که دوست داره بازی رو در اختیار خودش داشته باشه. از عقب زمین با حوصله بازی‌سازی می‌کنه، با جابه‌جایی و پاس‌های کوتاه فضا ایجاد می‌کنه و سعی می‌کنه موقعیت بسازه. وقتی هم توپ رو…</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/funhiphop/76331" target="_blank">📅 16:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76329">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سلام به دوستان عزیز در خدمتتون هستم با برنامه فوتبال با فرید
آرسنالِ آرتتا تیمیه که دوست داره بازی رو در اختیار خودش داشته باشه. از عقب زمین با حوصله بازی‌سازی می‌کنه، با جابه‌جایی و پاس‌های کوتاه فضا ایجاد می‌کنه و سعی می‌کنه موقعیت بسازه. وقتی هم توپ رو از دست می‌ده، سریع و با فشار زیاد برای پس گرفتنش اقدام می‌کنه. در دفاع هم تیمی منظم و سخت‌گیر داره و روی ضربات ایستگاهی هم خیلی خطرناکه. به طور کلی، آرسنالِ آرتتا تیمیه که می‌خواد با کنترل بازی، پرس شدید و نظم تاکتیکی حریفش رو تحت فشار بذاره.
پاری سن ژرمنِ لوئیس انریکه بر پایه مالکیت توپ، پرس شدید و فوتبال تهاجمی بازی می‌کند. این تیم با پاس‌های سریع، جابه‌جایی مداوم بازیکنان و گردش توپ سعی می‌کند دفاع حریف را به هم بریزد و موقعیت خلق کند. بازیکنان در حمله آزادی زیادی برای تغییر جایگاه دارند و به جای تکیه بر یک ستاره، روی کار گروهی تمرکز می‌شود. همچنین پس از از دست دادن توپ، تیم بلافاصله پرس می‌کند تا مالکیت را دوباره به دست بیاورد و اجازه ضدحمله به حریف ندهد.
پاریس احتمالاً آرسنال را شکست میدهد چون در انتقال‌های سریع، حفظ مالکیت تحت فشار و استفاده از فضاهای خالی بسیار قوی است. اگر پرس آرسنال را بشکند، می‌تواند با سرعت و کیفیت بالای بازیکنانش موقعیت‌های خطرناکی ایجاد کند.
تا آنالیز های دیگر بدرود
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/funhiphop/76329" target="_blank">📅 15:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76328">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پیت هگست وزیر جنگ آمریکا:
محاصره هنوز برقرار است
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/funhiphop/76328" target="_blank">📅 15:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76327">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">المانیتور به نقل از یک منبع اطلاعاتی ارشد اسرائیلی:
طرح سرنگونی نظام ایران با همکاری کردها جامع و مفصل بود، آمریکایی‌ها کاملاً از این طرح آگاه بودند زیرا یک جلسه توجیهی کامل دریافت کردند.
کردها مشتاق اجرای عملیات بودند اما واشنگتن در آخرین لحظه آن را متوقف کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/funhiphop/76327" target="_blank">📅 15:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76326">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">آرنه اسلوت لالالالالا
آرنه اسلووووت لالالالالا
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/76326" target="_blank">📅 15:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76325">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بکیرتونه ولی آرنه اسلوت از هدایت لیورپول اخراج شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/76325" target="_blank">📅 14:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76324">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5Egks3mJQbiisDnOzrS48JgnfVuK3D-cCbbDGrvYuCuXShG4y_5yp5DeyDbKXH2EdA4cL-O6kmzIfG25HrwqnrSta1hjqz6BxA6YXq4IQlUB5FWnRCgnp0Bg3YZxtflY-5LP1jjJsfcMzp6ApxK_sGuaspH1amHulfl-qA-7U2G3F8XguEC3rrNNoUr6nm8YCsNwSuAkgxjKHHURGJjbHB-lzZM15qsDn5OIptfsXoDY-hFjqgpVatKt1m56YKT5TuCpqgLNeCotPZq1EBQ_UHUWUOIZEFsVB3aLCSbwOcu5WkdkZl1P7Xm1GMqik4x7_VXYga3t7kBPXad8kauRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسب دستور مقام محترم قضایی این صفحه به علت فعالیت غیر مجرمانه و طرفدارگونه ترفیع مقام گرفت.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/76324" target="_blank">📅 14:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76323">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">برا مثال شاهی به هیپهاپولوژیست دیس ناموسی میده بعد کاگان میاد باهاش کار می‌بنده الان  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/76323" target="_blank">📅 13:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76322">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">برا مثال شاهی به هیپهاپولوژیست دیس ناموسی میده
بعد کاگان میاد باهاش کار می‌بنده الان
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/76322" target="_blank">📅 13:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76321">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">حاجی شاید نداشته بنده خدا مسخرش نکنین</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/76321" target="_blank">📅 13:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76320">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3rdEBpujToiluGWOgB5Heob1SNhuKJtwOvx6oxOjbemjYjKmkdhPb1IT9WHXjFtitHnf0e9tpHU9djTLfF7R3pRbCGna0DXpAjyPDY2pTKcw_bh4DLF3N8UrwhwmRieiTBKkmzh-gTeZsLIHj-lNmmUizkXONptyAHhTCUKYHC_QIOpvegUVhaBRdZFaFCr4M8f5FxfeVc-QblEu-uAL6J7Kk9llrrQce-hSOMT8IRhkpbqbPvxZPdIGQSOmX_v6eckohhYuoTXCMTKrjJ1ZAfm3v-YpYzouxTZ-1tDacoqTgzMWmnjmJyl7NsEn_NZjZ3Xm4vt2MWlLpxh44Q9xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیو نمیفهمن پوبون جان؟
اینکه چرا کصشو تو میکنی بعد پول بیمارستانشو ما باید بدیم؟
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76320" target="_blank">📅 13:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76319">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">نتیجه بازی امشب رو پیش‌بینی کنید، دو نفر اولی که پیش بینیشون درست در بیاد باید نفری صد هزار تومن به کارت من بزنن.
@FunHipHop
| محمدرضا ناصری آزاد</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/76319" target="_blank">📅 13:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76318">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJrFsukjKO1TJRBFkwXLgftpvZJHQK7kUg2TVeHVqXOeVY33n_NSDxKYjhlqnIAbUgoDfvLov7GUFx3Ezuc7zFbAjUEDc5bSodo7J9_YqLWN47LAcn23LhsHLUchKXe_ya0IYRTrBOoMu30Iuc9QiM5uCJO18kQBwkHMg5SfofxDxWDT9eDZ0UeJr9lVQFez0kka2gwwMy9GDww4P9QAhjrVckB6evh9NDTi3a-mOYwHkJREgcT85DYrkQFtHdPWmwh6tawOnZ20hZbKMaGyVcmh1xe7J-SkYa8kuifUgOuf7JlSx4BPFqD81Wqy7DThJS4Mqg7Ae-4F8je2CwZTdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچکس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76318" target="_blank">📅 12:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76317">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">خداشاهده ۳ ماهه تو ضعیف ترین نقطه ی ایران توی روستا توی نت ملی و قطعی کامل اینترنت من وصل بودم
تا پزشکیان نتو بازکرده نصف روز قطعم
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76317" target="_blank">📅 12:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76316">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">کنکور سراسری به همراه آزمون پذیرش دانشجو معلم پنجشنبه و جمعه ۲۹ و ۳۰ مرداد ماه برگزار میشه، البته اگه باز نزنن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76316" target="_blank">📅 11:54 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76315">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پولاتونو جمع کنید ببندید رو پاریس، دریک رو آرسنال بسته</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76315" target="_blank">📅 11:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76313">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-r71Fi9t5WYacAPycOc06tN3vPbKir-42TZvymNBwYCvY4cOpV_nFgaa3JOge6kdlTMcVLS_b5ZBzLKDhgNhgQKe5NMTJygMR2ezomwpZMuAOEH-wudigVHN6V3H4g4J0an4gWNb6H5kOvVOriq6HNk-73Z9FXbv-E10Hf36sDmiUixP3NcXvv_pHvMis70s3QjoZghYtxrZ33q98js3M8CxYG4LmtLii0wZdrxIko017V_IBwrGBLBz4jCaaAi_hGXmtEhE0fef4VBJ5v08bIqC9nfYNXxQhiWMgdgrBLrYEGMRj5E81Msbpcu24uRF-vR_C7BLyTzIFL6rPK7vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس تهران
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76313" target="_blank">📅 11:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76312">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خدایا خودت امشب به سگ و گربه های مشهد رحم کن.
@funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76312" target="_blank">📅 10:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76311">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZJURr3zRSGiy3_wx6SDjE2IXKXY6rNA2ZfbqLxisMQaKZdwOVCjN2u8KfSevB1sp_JjqFcb17IjkUQWQSJQKVDBgzOM5hKAyU7cBVIyPOapXfyFNbvN6aI0q768PvnW77qOpT3qYDEApCKkcDVUTDVs4XF1KSm1bi5uvGPD332pVc7aPufNnoiV-R38xrvonCtPMAeZ6xe3FUVPuM2hadQZns8J3bD2wRsAdT5dYHzX89GlbcNXUeeWo9kSKV_TwiNSQVe5ACK5dLFAWlnCPwA7fZbKgj_1uw2HSuLFZIJW4qk3b9JWAoKRHAjWebiLnsSW52aHLT4_haucFpZ6GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب فینال لیگ قهرمانان داریم.
@funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76311" target="_blank">📅 10:40 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76310">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/76310" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
💰
اولین سایت جهانی با امکان شارژ و برداشت با کارت بانکی
🔹
برای ورود فیلترشکن خاموش کنید
😀
Telegram Channel
👇
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/76310" target="_blank">📅 10:40 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76309">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1CKH6_u-D1EBENpcLXdFE32_DwEkmK2DMvdnVzhZ6DSze0XV57XdnRNPzwRvS6GVnay7nYthjd4-7azmJR1NzCJZKu5t2xFu7oLUeiYEalVAoYwRSpvsQOpQp2oau2yeorh6YHKyA3F9-gX1n6drqox_YC505BvUX2VxukWTnyPeSgL_Slr0l4l6Eta62IOI4I5dMHDpPWQUfaMBy3K_VdVB1iPDrOG6EsorN2EHb4V3RYZXm0RzAJHc_i9AtHC36cqfv6CUWpZpSCJPvP48dvGV6soyFM4s5jTFU6R5B4Xu7z_tKClToCKyjbaWdutj4DvO8ErH4LqqAmylFF7_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت :
👇
r9
🅰
✅
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/76309" target="_blank">📅 10:40 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76308">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b21fcfedbc.mp4?token=vZ6mZQWN9CeIeFmmiYaVVVZbFqYVKHt65_drUY-1w93U5Q_GJ7u3qdqVG963WszGEIQtZ3U3kchcy1MJgvYGHyEHsZUXNTA0e9IY1zt-GkFRMb3YdXkBkDarxoDpM0FVwi2g95S7Oo1R7rIO-3fTLKvx34s6LzzeMidLW-x-Wwr8k-noJGaw4kI-mNHTcU8X7Pb84MReRwcUnTX90wk-2HtsEUWM-64kOttljpvNeN7lUdnMKC3ismNWJV1G3xswAMJY8ltSHB4e_wtymZzy4gRhRbperyGOi5N97gQ3mzx_wmfQfleDr_aX96yTCublOfjukMM160uGAfSEBW9lfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b21fcfedbc.mp4?token=vZ6mZQWN9CeIeFmmiYaVVVZbFqYVKHt65_drUY-1w93U5Q_GJ7u3qdqVG963WszGEIQtZ3U3kchcy1MJgvYGHyEHsZUXNTA0e9IY1zt-GkFRMb3YdXkBkDarxoDpM0FVwi2g95S7Oo1R7rIO-3fTLKvx34s6LzzeMidLW-x-Wwr8k-noJGaw4kI-mNHTcU8X7Pb84MReRwcUnTX90wk-2HtsEUWM-64kOttljpvNeN7lUdnMKC3ismNWJV1G3xswAMJY8ltSHB4e_wtymZzy4gRhRbperyGOi5N97gQ3mzx_wmfQfleDr_aX96yTCublOfjukMM160uGAfSEBW9lfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همون همیشگی  @funhiphop | reza</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/76308" target="_blank">📅 10:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76307">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/310846887a.mp4?token=rwiMCfafO2SdCyoawcWqEmpzY9EL_NbLkKWg3cM5ET_ZdEZEgRdHlc9CBDYX76Qg4JUdBqdDw1TXnSaIxtCU_DobPJaR48tkKT3pIfUZvU5zzt2deUyE1urIA0eDiFf4eU3K65CGFX0lH7JGy_jUzkSFtk_S5PZiZ0z3VF45O2vLk3AAB7d4esz9-jdNbWHaGi64Ua8evJGnwrYWaVFptfclMtiggJAeH8fkxf_JaQkxADBLjUeDw_UX7wPS-icdK0fE6CgchR48AIY_O-yi1YLxJPAvYqb9hdr-bxwNCVuqVsMLVPjDeDwgo7BBjMedn7mubTqiHwSW4CI_WsnxQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/310846887a.mp4?token=rwiMCfafO2SdCyoawcWqEmpzY9EL_NbLkKWg3cM5ET_ZdEZEgRdHlc9CBDYX76Qg4JUdBqdDw1TXnSaIxtCU_DobPJaR48tkKT3pIfUZvU5zzt2deUyE1urIA0eDiFf4eU3K65CGFX0lH7JGy_jUzkSFtk_S5PZiZ0z3VF45O2vLk3AAB7d4esz9-jdNbWHaGi64Ua8evJGnwrYWaVFptfclMtiggJAeH8fkxf_JaQkxADBLjUeDw_UX7wPS-icdK0fE6CgchR48AIY_O-yi1YLxJPAvYqb9hdr-bxwNCVuqVsMLVPjDeDwgo7BBjMedn7mubTqiHwSW4CI_WsnxQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست:
همین چند روز پیش در جلسه کابینه بودیم و رئیس جمهور گفت: "هی، این یک معامله عالی خواهد بود، و اگر ایران نمیخواد توافق بزرگی انجام بده که تضمین کنه به سلاح هسته ای دست پیدا نمی کنه، میتونه با مرد سمت چپ من برخورد کنه."
و این تنها باری بود که به چپ بودن متهم شدم.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/76307" target="_blank">📅 10:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76305">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EUM9y3_8yftOT8b3B5ONBZJsdj3Xyc424aahTdh4JEZ4k1wTSQLyfMIdWYfjoCp0tnLU_uzfof-OjzwwoX3UHUX0xrpPDEc_FmAN9-o6HJ8-7gnS3uhAutA91T6vc6Wa5gKipxbf0NBmd8sEzcuyg9aJF-AYcD7c4x7-0weyS0p88XKaV4PRbrT1G-GpXZNXdBxMntTBr6eY2SkyIhXAeIlm_jzVktTkQP6osI-GYzLulN7jHM_pSKuzEjtYFu-VXk3-9lVpc6wMQeTR6I8g4_zWWfIK5i7E4PsDxQNNvrXvNISrKCK1iomAmN7bkBsHTVEN7-lXzQn-nvRcYHCFiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WP0gs24SFvO7cx1043QxdAdaQAwQXnrmjbyJlyzLKLZspqGGoS0U_2Lm2fnBEyRx5clIvLnnAE4Qk-QkOiB7YFLbvE3NacRb3dnbcSf8bh86AEaN3GH7Wgjiz7FQZ8t078j0yeBSfHzAXWTIiEO_E4HohHZFUBEa_R5h_1PzN27SwhuqINf_bywjQdpQ0-Hru3jSLd8ptQZIU_QjvqJbvIFkXZ3J8Aj3B5tL6u8l_yfsHFGUQ1SrOmfULGcn7ubIr_A6s_NYJjtRSU6FW4nXNlqnO_AYxGTj8NNrR5zd9ovG9KzR-51wMRAgtjb3irh55AwyN2hFr5ADCxdRcNmCDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرماندهی مرکزی نیروی دریایی ایالات متحده به دریانوردان و خلبانان هشدار داده است که سنتکام عملیات نظامی در تنگه هرمز، شمال شبه‌جزیره مسندم عمان که در وسط تنگه قرار دارد، انجام خواهد داد.
طبق هشدار USNAVCENT به دریانوردان توصیه کرده است که هنگام عبور از تنگه هرمز با ایالات متحده همکاری کنند. همچنین USNAVCENT اعلام کرده است که هر شناوری که در فعالیت‌های مین‌گذاری شرکت کند یا از آن حمایت کند، هدف ایالات متحده قرار خواهد گرفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76305" target="_blank">📅 09:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76304">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromInfected</strong></div>
<div class="tg-text">سلام فربد جان ساعت 00:23 است از خونه همسایه بغلی صدا آهو ناله میاد</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76304" target="_blank">📅 00:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76303">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سلام فرید جان امشب نزدیک میناب ۵ تا صدای انفجار اومد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76303" target="_blank">📅 00:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76302">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">حوصلمون سر رفت بیاید فینال فردا رو پیشبینی کنید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76302" target="_blank">📅 00:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76301">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvebJz740tx_dmVxbYrUicaGGOCTioyuqUW8MXdYZBcRgczf9U3bKOw_IWK6-8WKesYc2f5nx2NOnr7iiCKGPuu5_RuRKX7XvBs3wbmhSUXF_LXwR0xhjALtvsg6YjCberdeOtQsJPdqdbPovQWbPq4GtYsRpIby0YDfyGOhpdrgKX9AA86wp9A55fNrM6C2cyJ7UA0LG13kqn3ktC4yPIGVzp2O9AfwLdbxd0rv8BorgtbQoJfM09aprhH6khLfFLOuJPpXCiOinva8grGd9qywHA4KzEUbWIxGdQEOD2xQy6CQfSt9JUlOdMi81Fqgkw6CVMS8lTmZ2EohfUI18Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا 1411 با پزشکیان
✌🏻
@FunHiphop
| ALI</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/76301" target="_blank">📅 23:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76300">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlHY4NjJ6cwByRvUuRkz-7vW8ExvwV1DETYF41ze6KN3Lgzdtp1oNRbPpI-KEq_HKTgEL7k0kbHGDU3ov6jgE2e00Zq9o-j4HqlfWla6FI9cktrDUY5BxTnotq6ucIsFQ4tQ6OhiMNfEAXqjPzF8pUShQLl09NjiN7wClFuvIQ2sARFSQewDbkHSGup1-dUxQD_WLceJvNNEOFZWcIBnFz1PefyEP6Jerlk1UebOox1EkHI-7eT4kL9HaEKhwNz48MBd8QtZuOtMM7MSjdd3_oTmYxZ2ZQZ4VY0K_ODAbG8913eCNYBmJ6UXl5fTEhln_Xl7FTWnR0eWeCsTKAma8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کصکش شبیه شوالیه هاس</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76300" target="_blank">📅 23:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76299">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNoah</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_3czsL0iXUB4Ihtnqf7Og_1pTtAW11gZyOcSzX23UrOQLcRnFH_8c4Es5KVLQlozx2TMFb2lW3N-gBhO2PuF-uXu1QWnCsbm_p89PuDNkIc6GNPGntZ5UVbo8z60c5tq1DUTOt_3MCqqcAUXkEty7PXVotlhhJ_2DkgeO7bptgFIgLFBvF6eer8GRapkalWescOVo5edNKUlKeX3mu8LAXw8kqcT-1EgloNn95s705fDe8oOLmoXMASv_7ntwFBSrI5R3aOM7QrjWZmHgSzHlfH48J_fzxFnBkq-OcBi9IgVWLYlw6pTIvCETYUHuZ3aGHDNxzSj97CY5kOhDh5ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس قدیمی گوردون با لیونل مسی
یادش بخیر</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76299" target="_blank">📅 23:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76298">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">از گوردون پرسیدن تو که انگلیسی هستی چطوری اسپانیایی بلدی، گفته چون از بچگی میخواستم بیام بارسا یاد گرفتم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76298" target="_blank">📅 23:10 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76297">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">پست جدید کاخ سفید: اونا بین ما راه میرن  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76297" target="_blank">📅 22:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76296">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e95e3a0cee.mp4?token=veLL7fRv6LAm_sHjvu8FKj001QKSwQ6tG8QkgTo_SJeqAuF0XXUohIc-cct0b3812nr4KTsz8nzVsd6p9BHZBRiZ-enlNvi68qiG5dT246IyABJZTyt13OlCqSZPg0iolXPPWzXTFqYRHO_7TTWUE7ZGthhc29dqCC5sxAPY2rwupciUo_T-kXEelCPZWjvQedRAoMtUSQH-UvhaIniffE4SjbCWRzqsGO2rShLX8-si3srUP0qHqOob7BJppoiYIGP-XreZkOSnEocFW494GL6NMXP9gWNJV0AvPMdlOGRo0qIW55tPFiVPWLzuStj8BEzyy9P2rfkUFaZuBDpLqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e95e3a0cee.mp4?token=veLL7fRv6LAm_sHjvu8FKj001QKSwQ6tG8QkgTo_SJeqAuF0XXUohIc-cct0b3812nr4KTsz8nzVsd6p9BHZBRiZ-enlNvi68qiG5dT246IyABJZTyt13OlCqSZPg0iolXPPWzXTFqYRHO_7TTWUE7ZGthhc29dqCC5sxAPY2rwupciUo_T-kXEelCPZWjvQedRAoMtUSQH-UvhaIniffE4SjbCWRzqsGO2rShLX8-si3srUP0qHqOob7BJppoiYIGP-XreZkOSnEocFW494GL6NMXP9gWNJV0AvPMdlOGRo0qIW55tPFiVPWLzuStj8BEzyy9P2rfkUFaZuBDpLqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید کاخ سفید
:
اونا بین ما راه میرن
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76296" target="_blank">📅 22:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76295">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ تو پستش گفت تصمیم نهایی درمورد توافق و برداشتن محاصره رو تو جلسه امروز می‌گیرم.
الان نیویورک تایمز گزارش داد:
ترامپ حدود دو ساعت در اتاق وضعیت جلسه برگزار کرد اما هیچ تصمیمی درباره توافق با ایران نگرفت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76295" target="_blank">📅 22:27 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76294">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سلام وحید جان قشم ساعت ۲۱:۲۵ تاریخ جمعه ۸ خرداد پدافند فعال شد من در محدوده قلعه پرتغالی‌ها شهر قشمم و شلیک پدافند کاملا قابل دیدن و شنیدن بود  @FunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76294" target="_blank">📅 22:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76293">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/158dd2ae98.mp4?token=gecGtB8Bg9I-iT3OBtUDSKuKXZXXaj2bGhmxj560Aqkf2exAnQG9sBfP-nof8ARByUTUE3UDi0D7DOEI8w_XzbEzwTFl1pKhAsxdNhcbG06fhda8ckFZgMjsVWkj_btuOB_xjc6v-jv5lzXIDnuN533Is8PtjxbRWXFejtWACKLcNpY0NC_GBprhB7TJJLcq-a3u4lwtkWtGnyS5boYhxQjRp3iW4Pun6XcWEfLtYnMfBO80sgVr6GWmdYtvzB1J9ILamkBbtTYV2QT_ZlODd7TW86zETFx_JZKS0Oomajm8TLIid8u3quCAXs9XshjlvgZHUdC_GsEp-V0l4cy4Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/158dd2ae98.mp4?token=gecGtB8Bg9I-iT3OBtUDSKuKXZXXaj2bGhmxj560Aqkf2exAnQG9sBfP-nof8ARByUTUE3UDi0D7DOEI8w_XzbEzwTFl1pKhAsxdNhcbG06fhda8ckFZgMjsVWkj_btuOB_xjc6v-jv5lzXIDnuN533Is8PtjxbRWXFejtWACKLcNpY0NC_GBprhB7TJJLcq-a3u4lwtkWtGnyS5boYhxQjRp3iW4Pun6XcWEfLtYnMfBO80sgVr6GWmdYtvzB1J9ILamkBbtTYV2QT_ZlODd7TW86zETFx_JZKS0Oomajm8TLIid8u3quCAXs9XshjlvgZHUdC_GsEp-V0l4cy4Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قشم
@FunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76293" target="_blank">📅 21:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76292">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سلام وحید جان
قشم ساعت ۲۱:۲۵ تاریخ جمعه ۸ خرداد
پدافند فعال شد من در محدوده قلعه پرتغالی‌ها شهر قشمم و شلیک پدافند کاملا قابل دیدن و شنیدن بود
@FunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76292" target="_blank">📅 21:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76291">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اگه نمیاید بگید باغ و بیم و فدایی پست کنیم اینو  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76291" target="_blank">📅 21:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76290">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuvhGun5SWQWA8hkmb-eItTNuCYQIHtZlut-A638P--PYDRvB16nU5na3pgYp5oeZ2soWNXi9gJjOM47FOfbl53vxI_HkwKsfh85E_zEUVD2r1xKwPuOM64-Yk43q25fnzgEnP96ZMHdYpdeHMj4aHSHJ1efzfYxNZLp6Bt8SOT6kSwEISz5OV0MRANtXcRL_pzCx55SwwQTqvJnkcRZaeV8yF-8B-uyI0FBMZMjJSyg0JnT5oOkk4PyTWl5MH3xP_Ja7BKznX7f8fDJzdsF49pDeipnnqs1PVH5gqFS6GOoFmqivyREsRjtBwgvDkfakCvyWrjzlRLzMO_QPW9igA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه نمیاید بگید باغ و بیم و فدایی پست کنیم اینو
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76290" target="_blank">📅 21:29 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76289">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">هیشکی خایه نداره موزیکای اصلیشو بندازه بالا، همه دارن هرچی موزیک کصشر که رو دستشون مونده رو میدن بیرون مارکت زنده شه بعد شروع کنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76289" target="_blank">📅 21:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76286">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">تا حالا شده در پی پیدا کردن یه پورن استار خوب ساعت‌ها سایت های فیلم سوپرو جابجا کنی و اینترنتتو بگا بدی؟ یه چنل داشته باش که اطلاعاتتو در زمینه پورن‌استار ها ببره بالا تا بتونی یه جق باکیفیت بزنی :)))
👇🏻
•
@PornHubCom</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76286" target="_blank">📅 21:08 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76285">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سلام بیدارید؟</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76285" target="_blank">📅 21:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76284">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpFL1a19OZiIprDwz6D2P4mzhHX5twNheXZ7-IRNkb5ScRK59RBujeEy8THpkfpLe6gOhMzU5aCwZfEgmuWCrrqeBGDFC4FAhbrJ7Tw_VcgT9l-Rjx-7v_k3CTPhoxOOZW7ONr6UujmJTlBh76lr7GoHc85PJyzWyzw2GCR6sCe-UE000UvSrtmSsmAOFi8NhBmSZxpAJVA-r_78M3peUEAKtCziYUNtADBqOcQDIRgIXZUux-23g2TYiBfTwfGQnmM1EFrz-5bwmQkDD_ex9C1SSZptQM1d8jppYkIkxQUi0WjWRTJtdHT5IgWgEqIxSOlG8TxK436IIIDZ07_Dvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کپشن خنده دار
@FunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76284" target="_blank">📅 20:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76282">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تیم ملی جمهوری اسلامی از تیم قدرتمند گامبیا گل خورده   @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76282" target="_blank">📅 20:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76281">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">خبرگزاری مهر به نقل از یک منبع بسیار دقیق و بلند پایه درمورد پست ترامپ:
هنوز اختلافاتی در مذاکرات وجود دارد و ترامپ آرزوهای خود را بیان کرده است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76281" target="_blank">📅 20:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76280">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">تیم ملی جمهوری اسلامی از تیم قدرتمند گامبیا گل خورده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76280" target="_blank">📅 19:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76277">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EMHvB4w2I-wC7-MvJYPmLz_n8ldcudV5Vdpt2NcYmX6vLnynE_mXZu6eh2qHqiQJmjuqGVqz3kBaUtkKmvRS6LeiVqnfrJtDB2eijwaLooJxMtQI7Cr4g1En07muR0ryWNm8Mu5J0ld5oNBq4vZ0XTmNRG_VQGQ4D1IU97GQCMA1jZw5HSqW_I6WKhAHUmV2NceWnV6NryCuNAjnkRRX2RnlNwc5dFXFpwbtsO9H_SevljgQej8QuNz42bILkQUUBWDfCXDxwZJTVRoePg8jAgt1D0PMGhIWhxMgWnmcbn8wgTmW3Arts_9AK28NIeZwx7cAz3pMPX5LpmQEd7aBAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jfKX8ENdybU3TL0YSrMkWZXpXlZmQHWh256IEk529RE2P_lXz3kESBpfWvnQDYMRJ67itvyTd6texYEmHw3IDfeIZ9D2Q7ZvxI6WU6vouQToq0iKeytAhLhLqF41AUU1uDTZu8j8xXQXainGxUHyIsTrndrNLvhnHNRPH1_ewJ92LPdk2gL-38finc3bC99uUzeTR-IoQd0fsxbD-qmRrlVNpewhHsSgy7Fa3KOCy7Vm2-rHIf6KzFAvV3dLDb39mWYHJPIo6dgJ4l55wrVf-zQQFkktZip8DcOCnv9eB2Ku-BETULRC4xx080RNxgt_RsSbIjfdyr1JVuVukPAx3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بیانیه اتلتیکو مادرید : بفرمایید! ما همین الان ایمیل پیشنهاد انتقال‌مون رو برای بارسلونا فرستادیم :  4 تا بلیت کنسرت بد بانی برای فردا اشتراک یک‌ساله روزنامه ABC 1 بسته تخمه! الان هم با اشتیاق منتظر جواب بارسا هستیم تا ویدیوی معارفه انتقال رو آماده کنیم. …</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76277" target="_blank">📅 19:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76276">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3ji3OHH7TsACUs6hk7OAO4GNmG3CVHIq86ES4RUJq5hNx0JGgCoYrtX7PsJqDtVemHS4a21s99nxg73rWZ4nscg8M4eyZf1tuTjBt4yYx2mp2Yc7iMtJZ61biY6UQ7oG1L-XPD1aNNY6QwWSyRKUSURYsdGaL3fNYcwM49hgqqqCHbeBHMQ7EDWlAXwq9UpPQ3Vd6HTE8Hp4Va1op3tUjSeotGsWACkHws1XeR1fioG0ORDEwKg5t5NjqtXlmsLqgnnA8U9-xOeVZzfjNeI0f1CgZtXUryEiJS6CdmORAyJRnNmSc91WZo66auOYh_naPt8aovB5NMoCG-0f37Amg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه اتلتیکو مادرید :
بفرمایید! ما همین الان ایمیل پیشنهاد انتقال‌مون رو برای بارسلونا فرستادیم :
4 تا بلیت کنسرت بد بانی برای فردا
اشتراک یک‌ساله روزنامه ABC
1 بسته تخمه!
الان هم با اشتیاق منتظر جواب بارسا هستیم تا ویدیوی معارفه انتقال رو آماده کنیم.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76276" target="_blank">📅 19:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76275">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">غیر منتظرانه ترین اتفاق ممکنننن
فارس و تسنیم:
منابع آگاه جدیدترین ادعاهای ترامپ را رد کردند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76275" target="_blank">📅 19:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76274">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">حرفای مانوک خدابخشیان رو گوش کردید؟</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76274" target="_blank">📅 18:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76273">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">حیف از خون هایی که ریخته شد و خانواده هایی که تا آخر عمرشون باید با این داغ بزرگ زندگی کنن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76273" target="_blank">📅 18:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76271">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">کل هدف ترامپ کبریت بی خطر کردن جمهوری اسلامی بود که به هدفش رسید و تموم شد
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76271" target="_blank">📅 18:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76270">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ: توافق انجام شده
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76270" target="_blank">📅 18:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76269">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامپ:
محاصره دریایی ایران از همین حالا برداشته خواهد شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76269" target="_blank">📅 18:35 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76268">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ: با همکاری چین و امارات اورانیوم های ایرانو منهدم میکنیم و هیچ پولی هم بهشون نمیدم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76268" target="_blank">📅 18:35 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76267">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">رسایی با اینکاراش میخاد بگه من طرف حکومت نیستم درحالی که نمیدونه روزای آخر عمرش رو داره سپری میکنه
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76267" target="_blank">📅 18:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76265">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خوش چشم، کارشناس ارشد صدا و سیما: ایندفعه دیگه جنگی نمیشه.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76265" target="_blank">📅 18:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76264">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHKGGtusY0jtyLjnwMhXgkROqlnJlDP7RA6cT3HUM2y-gkfzC_s5UydSDMLBb397ww8gPbnNozYgwBOWpfe0wYmFEViFXuMCsM3tB15-racn3Pwaf20LJAfO1xL7GaP-rxNacayS-s_DpCCVDorIe-GvVCPsrdzrHVF6ZOblzj-AnqDuWRgx7oEYCM3NyblBcXKPDG3_bcCdG0l3sImgnaeNsrnPZfAm2fFsK2EmLeJrwIpFWxqSLoMKH0Nwdll4OCPlNN2f4HHPyfe-bh3MWFTy_NK5XVpduWUvRogU1frJpVX1_wFpPbIVwn5Z9nBzJS4OPJWmHKImMFmIcajCXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچی مواد میزد تو وحشی واقعی بود پسر
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76264" target="_blank">📅 17:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76261">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">به شخصه حاضرم ۵ بار ترک تیجی و ۳ دقیقه از ترک باغ یاس رو گوش بدم ولی ترک پیشرو رو پلی نکنم
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/76261" target="_blank">📅 17:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76260">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">عمان هم باید مثل همه رفتار کند و اینکار را نکند، وگرنه مجبوریم آن‌ها را منفجر کنیم.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76260" target="_blank">📅 17:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76259">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یجور میگید برگردیم بله انگار من از اول بله رفتم که برگردم
جمع نبندید بابا</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/76259" target="_blank">📅 17:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76256">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">واقعا تلگرام ریده، میبندی بازش میکنی ۲۰ تا پیوی میپره
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76256" target="_blank">📅 17:14 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76255">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اینارو خودش لیک کرد که کسی لیک نکنه
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76255" target="_blank">📅 17:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76254">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">قبلیو نمی‌فهمیدم چی میگه اینو میفهمم چی میگه و کصشره</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76254" target="_blank">📅 16:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76253">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">وایستید یکی دیگه انداخت بالا</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76253" target="_blank">📅 16:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76252">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">Demo
Amin Tijay _ Members Only
Download
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76252" target="_blank">📅 16:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76249">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">یکی تیجیو نجات بده</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76249" target="_blank">📅 16:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76248">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">محسن رضایی: محاصره آمریکا رو می‌شکنیم؛ حالا چه با جنگ و چه با مذاکره.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76248" target="_blank">📅 16:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76247">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">وزیر امور خارجه عمان: امروز با معاون رئیس‌جمهور جی‌دی ونس دیدار کردم و جزئیات مذاکرات جاری بین ایالات متحده و ایران و پیشرفت‌های حاصل شده تاکنون را به اشتراک گذاشتم. از مشارکت آن‌ها سپاسگزارم و منتظر پیشرفت‌های بیشتر و قاطع در روزهای آینده هستم. صلح در دسترس…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76247" target="_blank">📅 16:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76246">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHjAjWcAKawSsQSaudL6d6W55Q5GKeCNktOqUdf7OzmOIjfdYBX4_yj329zcsMBQlN3IsdCWm_CgU4jifLBe7hSzQqTt7-1vr2jZxKv3X79Eq3JOg4wOQLswgWztFatjArsBB9Q1mJwPzZGNoQK2rZFLTiNsT0RuMIqvD11I8KwcXRsh7JxUozUU9kQdXxlA7CJxY1CEsc3CETZocP6EJdUpNZ9QyjaYG4XwTlBZfqa4Ov3FKljcBoVBhbSM7chHIIYVBHazVjMo1T92iHVNh4el_r5E1NX0FCEzLUnpLWqHwWV4TLk1m0cCUf-VzFgEBSggSEx4bpg1tT3xaOOmtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باقرشاه کاملا آماده مذاکره و امتیاز دادنه:
۱-ما امتیازات را نه با گفت وگو، بلکه با موشک‌‌ها می‌گیریم، در مذاکره فقط آن‌ها را تفهیم می‌کنیم.
۲-اعتمادی به تضمین‌ها و حرف‌ها نداریم، فقط رفتارها معیار است. هیچ اقدامی پیش از اقدام طرف مقابل انجام نخواهد شد.
۳-پیروز هر توافقی کسی است که از فردای آن، بهتر برای جنگ آماده شود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76246" target="_blank">📅 16:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76245">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">تا حالا شده گربتون فرار کنه برگرده؟ هوش مصنوعی میگه برمیگرده  @funhiphop | reza</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76245" target="_blank">📅 16:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76244">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">تا حالا شده گربتون فرار کنه برگرده؟ هوش مصنوعی میگه برمیگرده  @funhiphop | reza</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76244" target="_blank">📅 16:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76243">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">تا حالا شده گربتون فرار کنه برگرده؟
هوش مصنوعی میگه برمیگرده
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76243" target="_blank">📅 16:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76241">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">بارسا هر خریدی که میکنه فناش فرمین و اولمو رو میندازن نیمکت، تهشم این دوتا از همشون بیشتر بازی میکنن</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76241" target="_blank">📅 15:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76240">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">گرمه خوارکصده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76240" target="_blank">📅 15:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76239">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEa2PLfPDESf5PwY_nYs9VXXtKai_NjSjHq8A_pbdFWRaEbvo82IaNLmDoWwghhVd6VqVtXuz6Bg3JzyksjRbZdmyWB68YBOz8_CWJPXG83Y9LeoCmWkjJzKtMYJgAZjkFdJZt06eyqE-4SW53qJKcmFeN5MiwQM7ZRxVoed3_gY8S3VU2xP_4O5n1Peq5ohCw6mhFw7F44z-qEqnsq9nS3dj3lZDzRSkgvWokv7KPoV5qvvigmgkTu_g8MSN_Xktj1K8LN5ZDQgLmvvbddREBiee22nc6pNI8bi-98WUWVuLgUnaE6zjIjUM5n_d0wwaTAx2WHRM3R335jf0Sn1vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز می‌گه توافق نزدیکه و آمریکا قراره ۳۰۰ میلیارد دلار بابت خسارت جنگ به ایران بده: مقامات درگیر در مذاکرات می‌گویند پیش‌نویس یادداشت تفاهم جدیدی در حال بحث است که به تأیید هر دو طرف نزدیک‌تر شده. شگفت‌انگیزترین مورد در طرح توافق صلح ایران، صندوق…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/76239" target="_blank">📅 14:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76238">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نیویورک تایمز می‌گه توافق نزدیکه و آمریکا قراره ۳۰۰ میلیارد دلار بابت خسارت جنگ به ایران بده: مقامات درگیر در مذاکرات می‌گویند پیش‌نویس یادداشت تفاهم جدیدی در حال بحث است که به تأیید هر دو طرف نزدیک‌تر شده. شگفت‌انگیزترین مورد در طرح توافق صلح ایران، صندوق…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76238" target="_blank">📅 14:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76237">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نیویورک تایمز می‌گه توافق نزدیکه و آمریکا قراره ۳۰۰ میلیارد دلار بابت خسارت جنگ به ایران بده:
مقامات درگیر در مذاکرات می‌گویند پیش‌نویس یادداشت تفاهم
جدیدی
در حال بحث است که به تأیید هر دو طرف نزدیک‌تر شده.
شگفت‌انگیزترین مورد در طرح توافق صلح ایران، صندوق سرمایه‌گذاری پیشنهادی برای ایران است - که طبق گزارش‌ها حجمی معادل ۳۰۰ میلیارد دلار آمریکا دارد.
ایران در ابتدا این را به عنوان غرامت خسارات جنگ (که بین ۳۰۰ میلیارد تا ۱ تریلیون دلار آمریکا برآورد می‌شود) طبقه‌بندی کرد. طرف آمریکایی آن را به عنوان «صندوق سرمایه‌گذاری» بین‌المللی که به تسهیل آن کمک خواهد کرد، بازنامی کرده است - چارچوبی نرم‌تر که از کلمه غرامت اجتناب می‌کند.
به نظر می‌رسد این ایده از سوی استیو ویتکوف و جرد کوشنر مطرح شده است، کسانی که پیشنهاد دادند پروژه‌های املاک در تهران و مکانیزم سرمایه‌گذاری گسترده‌تر به عنوان مشوق‌هایی برای این معامله تقویت شود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/76237" target="_blank">📅 14:24 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76236">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">مدیران اتلتیکو:
خولیان نخواهد رفت
مذاکره نخواهیم کرد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/76236" target="_blank">📅 14:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76235">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ناتو: روسیه شب گذشته یه ساختمون تو رومانی رو هدف حمله قرار داده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/76235" target="_blank">📅 13:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76234">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">آه رسایی اینترنت و گرفته
هر لحظه داره ضعیف تر میشه
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/76234" target="_blank">📅 13:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76233">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">رسایی آقا مجتبی رو به پسر نوح تشبیه کرد  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/76233" target="_blank">📅 12:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76228">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jcpG-QaSzDXgDF_m9ke9EhmDmn-Xduuz1f-R0zd5lGEQyl79pkoOsP3NFBxPQoybmVp9zfrpSgTcgediEyheM0ONkvfrEvdpPPDiPKvsq6VfWxBM4UAnaG_gehY4MdhURJsjxyG4U67IBs-f3f7zrg7QiQrTvYt9kNFNSHVaqmUIMYaIg1-kUkMvdoY093nOQc_s8NA0xNFOE5I7-NrY-Yfjh9DibWnlVb_pnCG2F9CJ92_8RTPdgZGqyXtGRlXwKvuL6rYas-TxE8b_No_HTM7CBFYvY_7Jw2jJPIHU_VLdlj1ew9m1ROYE1RE_euUCeh1o6S1amOSPOSU0tqTNjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسایی آقا مجتبی رو به پسر نوح تشبیه کرد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/76228" target="_blank">📅 11:47 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76227">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8334aba596.mp4?token=Z1jJYm3mUrf9WAZitOkK8p4f4puYPENEk8WufVSjoDoxPYp93fI6_mzIqyH8ookWxYQB3xW39steRrcSZJQRDAWYDXF-R504T16RGanH4vvUdm1R1DEe7T6zvIGFrhrPr0z1SuSV7XVxKDAs7gyZeE0iH-o6b9P1fbEUHpwT3kLxOLxdTRvXDtkMf-u9Q28vOS5yAEbgUU-d9OSzuLfBGlP04TFYiSg5MLvGv2XNRvEa4DUYae9fEqjhq_s0tJXZvh9FuH9Izr3UfdC4IO2wEQzM9s822D9QXZCNcvnUrOY7asMRPlKPs7-_n00nR5twJ0-_PtICaamGkLd0lDMvWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8334aba596.mp4?token=Z1jJYm3mUrf9WAZitOkK8p4f4puYPENEk8WufVSjoDoxPYp93fI6_mzIqyH8ookWxYQB3xW39steRrcSZJQRDAWYDXF-R504T16RGanH4vvUdm1R1DEe7T6zvIGFrhrPr0z1SuSV7XVxKDAs7gyZeE0iH-o6b9P1fbEUHpwT3kLxOLxdTRvXDtkMf-u9Q28vOS5yAEbgUU-d9OSzuLfBGlP04TFYiSg5MLvGv2XNRvEa4DUYae9fEqjhq_s0tJXZvh9FuH9Izr3UfdC4IO2wEQzM9s822D9QXZCNcvnUrOY7asMRPlKPs7-_n00nR5twJ0-_PtICaamGkLd0lDMvWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب ایران ۱۲ شب به بعد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/76227" target="_blank">📅 11:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76226">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">چرا وقتی اینترنت وصل شد انگار قطع شدیم؟
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76226" target="_blank">📅 11:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76225">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGLZwaRq5Vo30QE7sg3_u2w8UsikB5ubSdglUTAVQZUsfAQlMRT4FDQ78Mnhpb_OA-e8zv3wqGfxP90_lV2L0R31sXSl2OsygdLNLIFlIY5eJCPY08u9V_nR-7YpMYmFpkRR0sdyY5sc2P8u_oHKAT0LwJcdDEVaYARloCbbnxaKq7uYKR-lZVKk5vhBsXjzrCs8IMpfBxXhtfdPNvQUfEGH4vAmdNSLRsaY8eQH8cpmByWN2BG87wI0FHyJDvS37tGopKiVVrytl2RYSSyvxE3kW5JiK2AjzPcAOS2zKR6nA1VAaNeN6gsiCevCOuMYbY21XGPjjke6tze01wQ7hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت کتاب پاور آف نگوشییشن، امروز به دلیل تخفیف، ۵ درصد افت قیمت و تجربه کرد.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/76225" target="_blank">📅 10:53 · 08 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

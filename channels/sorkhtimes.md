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
<img src="https://cdn4.telesco.pe/file/GGkIGqFbnJ6O-gauj7hrjlUy7aMIl7r9Cm1z4Ozyu3KW9Roks5lFom6pGbBIXxfxO8jq3x3a34R5DpzpZnlMVFyF3bKUUomT4rvMI9EZxCUoPmP8EdS8zrvODRKQKwwRmMhKn1WwtrZ1_-7CjElfcY-ls6Q4bzZA3s8h123HMTaTFBFrUHoipdu7DpV-s4Y8Ml8XWo4YA-FZo6rLiCaa9qUPXnQPD6KtO6ZJ6wJKPJnrzweATmDf62iZHFFTLtTB_EBSSRNNNeqSVbLvmIA3dj6AmQ5YO15bHdoXX3UNDJhcBVVE8lpqQJZ3U7IDt7LmSmV6g2GBgyQpWR4vU1Vwbg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.7K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-09 19:29:26</div>
<hr>

<div class="tg-post" id="msg-132489">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❗️
ساعت 19/30 فینال جام باشگاه های اروپا بین پاریس و آرسنال انجام میشه ...پیش بینی شما از این بازی چیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 94 · <a href="https://t.me/SorkhTimes/132489" target="_blank">📅 19:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132488">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EY20R1V6VPKM0z5rN95Z0Gwtz9Qons4t4AsERDSKRXmTE512yUiigmOpPUjR4AeHCrLiPx7A1SCC_I0BNxjcfJPbp4MtJ9DarnCrcVLskv868dvQcQ83nvbxMGpxQYpmGBGsJksvlALCqyXHc0tbgfFqjQlzhEwlUEvq1Kb02CqovTJfg5oUoaQCFJK8HDFxcrZwdetEC7ZMwtLRS8V-chnMKXtH6dEp6MQlsVzPQ69vRTG4PSbxGS30dZrFWYH5x6JQcbQ_lMmQvX_1dy08hMDFz3auGbr9PRUkZ7m0lQrgmVe0ONeKPKmfBiTV9zkkx3aAuZJIMiPpjHtL8--PpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
باشگاه پرسپولیس سازمان لیگ را به مناظره دعوت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 414 · <a href="https://t.me/SorkhTimes/132488" target="_blank">📅 19:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132487">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GENe2-5SHqrK8B-r6DTYQS-rZ22HD_IUd04GPbHrp2MVPw1AV9LlRCA4U42p_9b33amrkpw1LShExx7QfIDj-xzQJNEaKdTVLNtd5zgS3N_eYcanOjWzaGIpwHjIPTbdCsjSlNVUglo4aS8Wha3yVgMyCiD3lbOAjlGWaCSeIYc3W_u37Df6zw3jLADi3CWM-Im0sdC2MldWpyLPpHoajWwDFg4-XU3_Y1L3L1tZ3-0dPLxyz2P_GAEgPnQmCLlB7nXnWVrfrR20YPCTCuITVVN6s94zG6VKverLt6CvxHtZwXTy_5Of9IAChx_o828ujQeJlP-8EdsAlbaLQmqsqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری؛ با اعلام دبیر سازمان لیگ، ادامه مسابقات لیگ برتر برگزار نخواهد شد و نمایندگان آسیایی ایران بر اساس جدول فعلی تعیین می‌شوند. به این ترتیب پرسپولیس سهمیه آسیایی نخواهد گرفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 994 · <a href="https://t.me/SorkhTimes/132487" target="_blank">📅 18:54 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132486">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
مهدی لیموچی با مدیران پرسپولیس به توافق رسیده و به زودی با اتمام قراردادش به جمع سرخپوشان پایتخت اضافه خواهد شد/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/SorkhTimes/132486" target="_blank">📅 18:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132485">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❗️
ساعت 19/30 فینال جام باشگاه های اروپا بین پاریس و آرسنال انجام میشه ...پیش بینی شما از این بازی چیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/SorkhTimes/132485" target="_blank">📅 18:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132484">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
اولین بمب تابستانی پرسپولیس؟
🔴
ادعای سایت هفت ورزشی؛ اگر اتفاق خاصی نیفتد آریا یوسفی را باید اولین بمب تابستانی باشگاه پرسپولیس برای فصل آینده لقب داد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/SorkhTimes/132484" target="_blank">📅 18:46 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132482">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔰
آف ویژه سرویس VIP
🔰
5 گیگ 150T
🔥
10 گیگ 300T
🔥
20 گیگ 400T
🔥
30 گیگ 500T
🔥
40 گیگ 600T
🔥
70 گیگ 900T
🔥
100 گیگ 1T
🔥
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال و مدت زمان نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/SorkhTimes/132482" target="_blank">📅 17:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132481">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
امیر عابدینی: فدراسیون هر کاری می کند تا سپاهان به آسیا برود؛ لیگ باید ادامه پیدا کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/SorkhTimes/132481" target="_blank">📅 16:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132480">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
اوسمار کراش زده رو آریا و لیموچی و حزباوی و باشگاه در تلاشه برای جذب شون راهی پیدا کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/SorkhTimes/132480" target="_blank">📅 16:47 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132479">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">⁉️
⁉️
نت بلاکس: سه ماه پیش در چنین روزی Iran دسترسی به اینترنت جهانی را قطع کرد. در حالی که اتصال اکنون تا حد زیادی بازگشته است، شاخص‌ها نشان می‌دهند که کاربران هنوز با فیلترینگ شدید مواجه‌اند، مشابه دوره موقت بین اعتراضات ژانویه و آغاز جنگ.
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/SorkhTimes/132479" target="_blank">📅 16:46 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132478">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8ec1381c4.mp4?token=GUtoAvKhxeXspRGVUTWgnBauVhZ_ZPcZ45uAVbtP7s1AwjOJNScSj7-ii_4C3klWUsyg_0LEFY4IJu3H7VUpbnNYtmVMaSEl0P9g9uniQm1R758Ops658cYq1fTjBnypG7yXf6oM3Ix0fagQ--acYjyvuiaNePG5AnI-d6wz0WMD_jRCpIj8geyX7tF_XOti2NyDtExFFWG2Vx1Pi5x3c-C4fr-fY3RknZISNdyt7_xZhaH5GRRQS7Nuqhz2T_cI6Uexnk1mD8jET_K-WdM4SYxuu2tBP_v5fJ22uk1WJ_WvX3jBBtl3cJfBa6ppgcCm-ykkspgmpbYiwTTK1K00CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8ec1381c4.mp4?token=GUtoAvKhxeXspRGVUTWgnBauVhZ_ZPcZ45uAVbtP7s1AwjOJNScSj7-ii_4C3klWUsyg_0LEFY4IJu3H7VUpbnNYtmVMaSEl0P9g9uniQm1R758Ops658cYq1fTjBnypG7yXf6oM3Ix0fagQ--acYjyvuiaNePG5AnI-d6wz0WMD_jRCpIj8geyX7tF_XOti2NyDtExFFWG2Vx1Pi5x3c-C4fr-fY3RknZISNdyt7_xZhaH5GRRQS7Nuqhz2T_cI6Uexnk1mD8jET_K-WdM4SYxuu2tBP_v5fJ22uk1WJ_WvX3jBBtl3cJfBa6ppgcCm-ykkspgmpbYiwTTK1K00CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
محسن خلیلی، سرپرست پرسپولیس: وقتی پیراهن تیم ملی را میپوشی، سرود ملی را هم با افتخار بخوان!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/SorkhTimes/132478" target="_blank">📅 16:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132476">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❗️
🔴
وقتی قرمزآنلاین فاش کرد محمودی از سوی ایجنت ها محاصره شده و برای تمدید قرارداد هر هفته یک ایجنت را به باشگاه فرستاده متهم شدیم به حاشیه سازی اما انچه گفتیم حقیقتت بود.از او خواستیم مراقب باشد.محمودی از برترین استعدادهای فوتبال اسیاست.
🔺
احسان خرسندی، سرمربی…</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/SorkhTimes/132476" target="_blank">📅 15:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132475">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✅
باوجودی که فدراسیون فوتبال رسما اعلام کرده بود موافق برگزاری مسابقات شش جانبه است اما در تصمیمی ناگهانی و عجولانه، بر اساس جدول نصفه نیمه و ناقص، نمایندگان آسیا رو معرفی کرده!!!
🔴
سپاهان که قطعا مجوز حرفه‌ای نمیگیره ولی جدی میخوایین گل‌گهر یا چادرملو رو بفرستین…</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/SorkhTimes/132475" target="_blank">📅 15:40 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132474">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
مجوز حرفه ای سپاهان صادر نشد و ممکنه یه تیم از بین پرسپولیس و گلگهر بره اسیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/SorkhTimes/132474" target="_blank">📅 15:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132473">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
فرهیختگان: علیپور از پرسپولیس خواسته رقم قراردادش از همه ایرانیای لیگ بالاتر باشه و اگه موافقت کنن بعد جام جهانی تمدید میکنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/SorkhTimes/132473" target="_blank">📅 15:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132472">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-ZKwCwzdzLx-TcJcHbfacGWvJpnDZiu1Eq-D95Ze7i60RdV9sBDu7B69t-HVDuumSKPIjhy1uoemOl56uu3TwDkYxzVTBkoVRGReonkIMOfCSZSIijJ81-zPITeoaHEqyAtdSOp2wSj0G-bNnMt0km1BNX0cSUkihwf-ZgK1sRbe9nwN01ufM7QzgHE2rRf2zEXMJsxcoXy_yQU4aIlpLiStu_LTwGz7bH_tAqdi_y-sCOoacWrlOcFtfldSx1AENJi5gUN2j_g8H7_iUeJ0zNQrGHPPvidkjynLVTeY79dVKSAeqDffzdE19_Sbw1g_Dg7ZbXKfiUhnBpsldLBxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🇪🇺
فینال لیگ قهرمانان اروپا
[
پاری‌سن‌ژرمن
⚽️
-
⚽️
آرسنال
]
⏰
امشب ساعت ۱۹:۳۰
🏟
استادیوم پوشکاش‌آرنا
🔗
فینال جذاب و هیجان‌انگیز امشب رو در سایت اسپورت نود با بالاترین ضرایب و بیشترین آپشن ممکن پیش‌‌بینی کنید.
🎁
بونوس ویژه ثبت‌نام برای کاربران جدید، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/SorkhTimes/132472" target="_blank">📅 15:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132471">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
فراز کمالوند سرمربی صنعت نفت: سوال مردم آبادان این است که دو سوم شهر بوی گاز پیچیده اما چرا پولش در تهران برای استقلال خرج شود؟ بوی گاز برای آبادانی‌هاست اما پولش برای یک تیم تهرانی!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚩
⭐
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SorkhTimes/132471" target="_blank">📅 14:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132469">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc298e01b9.mp4?token=NFtuZ9oVs3CsvbtachlRSFJy5yiIJNsdKy8ROxGfv8IwgZaW52V1b7NhxcgX9PxoMn8cbLFrDes4d51nP-JhDiezzI3fBGz7QRsi8lr0wM1kU2Kqua9kkpBJXIf_nn5CpJwN8A9xRta5Qbz4aoien5YQKEjaPFNEVk80uCbKuO4uGubjE9_gJ5-MsBadwYWWHzIBQ0x0iDdPRHzl0yxXF5WAv6EekpWGVVBvoUfg9LwBDBngxe0n7hddKi4JDQ2VJLuu0uANkBFzR4xfEizl9VFgayNealJSlxspM7qVZ5jpJAXowUhK7ZuauiQUrymQ-9AXX52xPe3arUu6kOiwrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc298e01b9.mp4?token=NFtuZ9oVs3CsvbtachlRSFJy5yiIJNsdKy8ROxGfv8IwgZaW52V1b7NhxcgX9PxoMn8cbLFrDes4d51nP-JhDiezzI3fBGz7QRsi8lr0wM1kU2Kqua9kkpBJXIf_nn5CpJwN8A9xRta5Qbz4aoien5YQKEjaPFNEVk80uCbKuO4uGubjE9_gJ5-MsBadwYWWHzIBQ0x0iDdPRHzl0yxXF5WAv6EekpWGVVBvoUfg9LwBDBngxe0n7hddKi4JDQ2VJLuu0uANkBFzR4xfEizl9VFgayNealJSlxspM7qVZ5jpJAXowUhK7ZuauiQUrymQ-9AXX52xPe3arUu6kOiwrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
آشتیانی پیشکسوت پرسپولیس: از سهراب بختیاری‌زاده انتظار نداشتم برای بدست آوردن دل هواداران استقلال به همه پرسپولیسی‌‌ها بگویید شما فاسد هستید!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SorkhTimes/132469" target="_blank">📅 14:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132467">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‼️
وقتی هوادار اسیر دست جو رسانه ای میشه و ارکان باشگاه و بانک شهر رو تحت فشار قرار میده ثمرش میشه مربی ۴۰۰ هزار دلاری با باشگاه برای ۶ ماه ببنده ۱.۲ برای فصل بعدش هم ۱.۷ این ک.ص.کش خان همین الان بشینه تو خونش تا ۳۰ سال دیگم ۳ میلیون دلارو تموم نمیکنه… ایرانیه…</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/SorkhTimes/132467" target="_blank">📅 13:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132466">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
قرارداد اوسمار برای فصل آینده ۱.۷ میلیون دلار هست دقیقا مشابه دستمزد پابلو وانولی سرمربی فیورنتینا در سری آ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SorkhTimes/132466" target="_blank">📅 13:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132465">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v41PbIs6NeUwkHyH3gwj5ZjrG4cBO6WDLlKAurLqqd7Qx3SH6DOcCYtmx5bmGrVoBZf-BLSwc1txblF18GwUzS8ggniKxo12qe0bYXX_tf7KJiH7SWrVyhUfg0exW8WJKyrcifelVup6GHUUvQuh24IKCB4WFoLdpOjI_NfLH685vkCpkjIFmReUqw2P4hZQ8rNF2VXOXRxnSjIsH8KDeAhfyM8SefPNZVcRNcvoXPSjq6dDBV0mj1ioBEoGqlZmA5cRpq9O1MuI9Hixwf5r5Npao1NDwiVfXaHPc0QiE0ODqlwjxd1zg5eSKRWjaNddLlZjTRzESTiR3QQ9WsIRJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قرارداد اوسمار برای فصل آینده ۱.۷ میلیون دلار هست دقیقا مشابه دستمزد پابلو وانولی سرمربی فیورنتینا در سری آ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/SorkhTimes/132465" target="_blank">📅 13:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132464">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اصرار بی مورد برای بازگشت؛
🔴
«اوسمار» استخوان در گلوی پرسپولیس/ ۳۰۰ میلیارد برای مربی شکست خورده!
❌
خبرگزاری مهر: متحمل شدن چهار شکست در پنج بازی آخر پرسپولیس باعث شد سرخپوشان تهرانی فاصله قابل توجهی با صدر جدول بگیرند و با ۷ امتیاز اختلاف نسبت به رقیب سنتی…</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SorkhTimes/132464" target="_blank">📅 13:14 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132463">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اصرار بی مورد برای بازگشت؛
🔴
«اوسمار» استخوان در گلوی پرسپولیس/ ۳۰۰ میلیارد برای مربی شکست خورده!
❌
خبرگزاری مهر:
متحمل شدن چهار شکست در پنج بازی آخر پرسپولیس باعث شد سرخپوشان تهرانی فاصله قابل توجهی با صدر جدول بگیرند و با ۷ امتیاز اختلاف نسبت به رقیب سنتی خود در رده ششم بایستند. اتفاقی که انتقادات زیادی را متوجه «اوسمار ویه را» سرمربی برزیلی سرخپوشان کرد.
❌
در این میان هم کمتر کسی به این نکته توجه می کند که مربی گرانقیمت برزیلی یکی از مقصران اصلی وضعیت کنونی پرسپولیس است. ویه را که به خاطر دریافت دلارهای بیشتر در دوره گذشته پرسپولیس را ترک کرد و به تایلند رفت، پس از آن که سرخپوشان نتوانستند با وحید هاشمیان نتایج مدنظرشان را کسب کنند، دوباره گزینه شد و پس از قهرمان کردن بوریرام تایلند با چهره ای مدعی به ایران برگشت.
❌
اوسمار در حالی به پرسپولیس برگشت که رقم های پیشنهادی اش چند برابر گذشته بود و جالب این که مدیران باشگاه هم با این درخواست موافق کردند به گونه ای که گفته می شود او برای نیم فصل یک میلیون و ۲۰۰ هزار دلار دریافت کرده است و برای فصل آینده این رقم ها سرسام آورتر می شود.
❌
به گفته یکی از نزدیکان باشگاه پرسپولیس رقم قرارداد او برای یک فصل و نیم بیشتر از ۳ میلیون دلار است که با وضعیت اقتصادی کنونی باشگاه وحشتناک و غیرقابل تصور است. این در حالی است که چنین رقمی در لیگ های مطرح برای مربیان طراز اول پرداخت می شود/مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SorkhTimes/132463" target="_blank">📅 13:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132460">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
محسن خلیلی، معاون پرسپولیس:
‼️
شانس داشتیم که اگر بازی‌ها برگزار می‌شد، سهمیه بگیریم. باید تیمی به آسیا برود که سابقه خوبی داشته باشد و اصلح باشد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SorkhTimes/132460" target="_blank">📅 12:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132459">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✅
بهادر عبدی، مربی تیم امید پرسپولیس: امیرحسین محمودی آینده درخشانی دارد. او می‌تواند در همه پست‌های هجومی بازی کند. می‌تواند حتی به بارسلونا برود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SorkhTimes/132459" target="_blank">📅 11:41 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132458">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
المـاس ارتش سـرخ فقط ۴ دقیقه زمان برای درخشیدن نیاز داشت.
🔴
امیر حسین محمودی در جریان بازی دیشب تیم ملی مقابل گامبیا بعنوان بازیکن تعویضی در دقیقه ۸۶ وارد زمین شد که اون تنها در ۴ دقیقه زمان تونست با دو پاس عمقی فوق العاده علیپور و بار دیگر ترابی رو در موقعیت…</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SorkhTimes/132458" target="_blank">📅 11:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132457">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❗️
باشگاه پرسپولیس تصمیم‌گرفته است بزودی؛ قرارداد امیرحسین محمودی را از لحاظ مالی افزایش دهد
🔴
به احتمال فراوان قرارداد وی 4 ساله می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/SorkhTimes/132457" target="_blank">📅 11:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132456">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJ2iNL9KYjuWSSbzYdOWdTd7NSwZSzxPUEH1mACxRc_v0j9p2FmjvuJAgJ332J8dqtShKSP-NjFXs1PcGXLqCU5zHNl-EOwOFnCLYSenIZk03HNvt10Ani_24UAT4HlfjvT7TqZWd67FmqFaSoORfyjUBxTYEze6f1coIDHhvLDC9mNWFSw82Q74JPdBBhuDW7cMPN4Pvp6jbiOLdioH2VndVeSzH7ti292TcJtXIJf2fQ9xrZaNBZmVCs_-T2ABiua8A9_DiwuNLtYPmtWK1-PUvE5O5r_1zg8Fg8WqG3svB18-xcEW0MUj5jrgVX-rhqmyDPDD81itZbRUf83BEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🇫🇷
مسابقات گرنداسلم رولان‌گاروس رو با بالاترین ضرایب در اسپورت نود پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SorkhTimes/132456" target="_blank">📅 01:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132455">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❗️
فرهیختگان: AFC مجددا با درخواست فدراسیون جمهوری اسلامی مبنی بر دیر اعلام کردن 3 نماینده برای حضور در آسیا مخالفت کرده و اعلام کرده ۱۳ روز وقت دارید که 3 نماینده خود را معرفی کنید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/132455" target="_blank">📅 00:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132454">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❗️
فرهیختگان: AFC مجددا با درخواست فدراسیون جمهوری اسلامی مبنی بر دیر اعلام کردن 3 نماینده برای حضور در آسیا مخالفت کرده و اعلام کرده ۱۳ روز وقت دارید که 3 نماینده خود را معرفی کنید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/132454" target="_blank">📅 00:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132453">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🎙
پیمان حدادی:
🔴
ما هم می‌گوییم استقلال نباید معرفی شود؛ در حالی که نماینده پلی‌آف در آسیا نداریم؛ بعد از جام جهانی در کنار لیگ حتی می‌شود جام حذفی هم برگزار کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/132453" target="_blank">📅 00:16 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132452">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
مرتضی فنونی زاده پیشکسوت پرسپولیس:
❌
آقای تاجرنیا از اسمش معلومه پولدار، بابای منم تاجر بود، ولی آخراش، تاش رفته بود جرش مونده بود
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/132452" target="_blank">📅 00:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132451">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">⚡️
⚡️
⚡️
برکناری با چند هفته تاخیر
❌
قطع همکاری محترمانه پرسپولیس با کرمانشاهی
⚡️
⚡️
فرهیختگان: یکی از انتصاب‌های عجیب رضا درویش در دوران مدیریتش در باشگاه پرسپولیس صدور حکم مدیر اجرایی برای رضا کرمانشاهی با رقم قرارداد قابل توجه بود. جالب اینکه کرمانشاهی فقط…</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SorkhTimes/132451" target="_blank">📅 23:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132449">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aa86d2930.mp4?token=uORdh-kASO2HDE2irJOTcPz0kDGGVXNFyfCOj9r8PLfU1dKm-50SAqvM8zOJTCtp5n_V7gVbXzw7fJOji9b_a9sI_sOY2q0J-F9quUh9BF3yg_sR2T4YoVY5zD9NfOFbkpGUkwkwxAD5_OyVwq5hkg948rM_00RYlLpINLm5-165H8T_3atO-B5GQO1n4Q_Aq9t32M0VtB5gMXtpXIbwv1u6vLFa-rs_KHKZi2744P2Z_KhKJdcGfIqmaqrwO4aVc0oq8OqyG0-bh8X53SOQSF_5Jvj_yalLHHKr6CQ2x18Ai3ZkYEUp7nedonvuoAT5zPeHZzkT92d7rlrq4o0H-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aa86d2930.mp4?token=uORdh-kASO2HDE2irJOTcPz0kDGGVXNFyfCOj9r8PLfU1dKm-50SAqvM8zOJTCtp5n_V7gVbXzw7fJOji9b_a9sI_sOY2q0J-F9quUh9BF3yg_sR2T4YoVY5zD9NfOFbkpGUkwkwxAD5_OyVwq5hkg948rM_00RYlLpINLm5-165H8T_3atO-B5GQO1n4Q_Aq9t32M0VtB5gMXtpXIbwv1u6vLFa-rs_KHKZi2744P2Z_KhKJdcGfIqmaqrwO4aVc0oq8OqyG0-bh8X53SOQSF_5Jvj_yalLHHKr6CQ2x18Ai3ZkYEUp7nedonvuoAT5zPeHZzkT92d7rlrq4o0H-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤍
ریکاوری ملی پوشان پس از پایان دیدار با گامبیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/132449" target="_blank">📅 21:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132448">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wms0LeQR4-6uIO9hhjaN27mqWgxitd0_nzrdScEzjd9YvygQ_d-jei3hPCUWWMiP7fuJDDJxudmogBD6pchl4VgYpTA2j6-Lw8LOG4r40eTEr-TOSl05erzns0BnuW0XXv5YIXSG_Vfe2fxfn41vT9H85fRKPSH_Am98cx6rzl-RmAKKveNzK3qycbEwZDG5Qc_S1B9s4rEYS2Qc7Fhq82JdD0gdk1trsjVubAKvhEHf_f-QKMxCK1NVmhm1fBjCXDfCtWMpQ8gBBXdPd2HTgUXxz3wf9J3j7_gGVGyUxsbBbeafLfSIbTjBK7ME5gfH4lGoZZ-orECP-gWZlLGr9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚡️
هر مسابقه یک فرصت، هر انتخاب یک هیجان!
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/132448" target="_blank">📅 21:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132447">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e547127cf5.mp4?token=TioVGhan7jT3Vlsn5BPZn7k60Ly7pjDVlw0mS-5t0xXg-B7XRSlcrGlVq2H14m2yBQy5Wi-tuZDJIDqlY0Tv1Uz2hgeAbGzsfQ78NDtgZHVT5IpFqVnQeDcmHVQ2SOayiMMpWMwQO_XwT3JBefaRlDtPJSsYeIF0BKqCHfqFVzEIOppwjB4zjfZ5meeJJwJHqtDAP5nnfD-VLe8aSneAiL35naG6-Cg4qA1TLyQ7dMCHfjE_8DoS2XVT2desn6oLIDlFYnlasubmWfSXJCOrDQ0-95rS9uQlphTWNmGh2Z6R_yF4F3EOA0Stj7B_5KRqTf9icO7cIDfE758YPxlTEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e547127cf5.mp4?token=TioVGhan7jT3Vlsn5BPZn7k60Ly7pjDVlw0mS-5t0xXg-B7XRSlcrGlVq2H14m2yBQy5Wi-tuZDJIDqlY0Tv1Uz2hgeAbGzsfQ78NDtgZHVT5IpFqVnQeDcmHVQ2SOayiMMpWMwQO_XwT3JBefaRlDtPJSsYeIF0BKqCHfqFVzEIOppwjB4zjfZ5meeJJwJHqtDAP5nnfD-VLe8aSneAiL35naG6-Cg4qA1TLyQ7dMCHfjE_8DoS2XVT2desn6oLIDlFYnlasubmWfSXJCOrDQ0-95rS9uQlphTWNmGh2Z6R_yF4F3EOA0Stj7B_5KRqTf9icO7cIDfE758YPxlTEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
#فوری
| رسانه اسرائیلی:
🔻
ایالات متحده و ایران در آستانه امضای توافق هستند
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SorkhTimes/132447" target="_blank">📅 21:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132446">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
تیمه گروهبان از گامبیا گل خورده و عقبه.گامبیا با ۱۵ بازیکن اومده
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SorkhTimes/132446" target="_blank">📅 21:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132445">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
علی علیپور پس از پاس گلی که به مهدی طارمی داد به سمت قلعه نویی رفت و او را در آغوش گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SorkhTimes/132445" target="_blank">📅 21:03 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132442">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be1699b581.mp4?token=M7gWHjfroToOwJGbGqRX2r6ViWX_b87c3waImXK-kaYWOZtTJqbOuFA8Y56MHk53Gdg0-cKraGuTGQfp7Zk3i3ev0TPPX6klKOiG9sPsrD-gH_MGsE-vvVYkArReIJZYf_lNe-MDAgCNXNRDk2hDaoHCI3SHEneCUXcvXaOycaNnoBusN-Y5h4OM0jBhP_3-B3Vmws4cArAjor6DfASy5VBUF01Ijvk9i5a4aL7uwpOgjLlEPzpEgtqaHTHZxmPnSMGA7Yxy2u3FFvn2kr5WMi5BxNhdMGzYbRXmvDSBrcLWAbOcjfI7DP7czWmm8afVl_G37bPrw7kMU9EQz5YC4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be1699b581.mp4?token=M7gWHjfroToOwJGbGqRX2r6ViWX_b87c3waImXK-kaYWOZtTJqbOuFA8Y56MHk53Gdg0-cKraGuTGQfp7Zk3i3ev0TPPX6klKOiG9sPsrD-gH_MGsE-vvVYkArReIJZYf_lNe-MDAgCNXNRDk2hDaoHCI3SHEneCUXcvXaOycaNnoBusN-Y5h4OM0jBhP_3-B3Vmws4cArAjor6DfASy5VBUF01Ijvk9i5a4aL7uwpOgjLlEPzpEgtqaHTHZxmPnSMGA7Yxy2u3FFvn2kr5WMi5BxNhdMGzYbRXmvDSBrcLWAbOcjfI7DP7czWmm8afVl_G37bPrw7kMU9EQz5YC4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
مصدومیت شدید کنعانی در جریان بازی با گامبیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/132442" target="_blank">📅 19:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132441">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‼️
🎙
سامان آقازمانی، بازیکن پیشین پرسپولیس:
‼️
اصلا دوست نداشتم جای بازیکنان تیم ملی باشم. راست بری، با دولت درگیری. چپ بری با مردم درگیری. بی‌طرف هم بخوای باشی بهت تخم‌مرغ میزنن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/132441" target="_blank">📅 19:49 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132440">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
گامبیا حریف ایران فقط با ۱۵ بازیکن به آنتالیا آمده است!  در بازی دوستانه هم به ما توهین میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/132440" target="_blank">📅 19:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132439">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
ترامپ: دستور دادم از این لحظه محاصره دریایی ایران پایان یابد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/132439" target="_blank">📅 19:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132438">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
ترامپ: دستور دادم از این لحظه محاصره دریایی ایران پایان یابد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SorkhTimes/132438" target="_blank">📅 19:27 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132437">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
ترامپ: ایران باید قبول کنه هیچ‌وقت سلاح هسته‌ای نخواهد داشت
🔴
تنگه هرمز باید فوری باز بشه و عبور کشتی‌ها بدون هیچ محدودیتی انجام بشه. هر نوع مین دریایی هم باید کامل جمع‌آوری یا نابود بشه
🔴
کشتی‌هایی که به خاطر محاصره متوقف شدن می‌تونن برگردن به مسیرشون و…</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/132437" target="_blank">📅 19:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132435">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
ترامپ: دستور دادم از این لحظه محاصره دریایی ایران پایان یابد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/132435" target="_blank">📅 18:47 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132434">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❗️
شبکه ۱۵ اسرائیل : به نظر می رسه ترامپ با یادداشت تفاهم با ایران موافقت کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SorkhTimes/132434" target="_blank">📅 18:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132433">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❗️
ترامپ: محاصره دریایی ایران از همین حالا برداشته خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/132433" target="_blank">📅 18:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132431">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❌
ترکیب بهترین تیم جام‌جهانی برای دیدار دوستانه با یه تیم ناشناخته اعلام شد.   علیرضا بیرانوند، علی نعمتی، حسین کنعانی‌زادگان، احسان حاج صفی، آریا یوسفی، سعید عزت‌اللهی، امیرمحمد رزاقی‌نیا، امیرحسین حسین‌زاده، محمد محبی، مهدی طارمی و کسری طاهری
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SorkhTimes/132431" target="_blank">📅 18:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132430">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❌
ورزش سه: باشگاه پرسپولیس تو نقل و انتقالات تابستانی دو هدف داره: یکی پوست‌اندازی و جوان‌سازی ترکیب پرسپولیس و دیگری اضافه شدن چند ستاره مهم و تاثیرگذار برای بستن تیمی در حد کسب قهرمانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SorkhTimes/132430" target="_blank">📅 18:30 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132429">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
🔴
🔴
و تمام
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SorkhTimes/132429" target="_blank">📅 18:29 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132428">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
آکسیوس: ایران و آمریکا در حال حاضر به توافق رسیدن و فقط تأیید نهایی ترامپ باقی مونده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/SorkhTimes/132428" target="_blank">📅 18:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132427">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❌
ورزش سه: باشگاه پرسپولیس تو نقل و انتقالات تابستانی دو هدف داره: یکی پوست‌اندازی و جوان‌سازی ترکیب پرسپولیس و دیگری اضافه شدن چند ستاره مهم و تاثیرگذار برای بستن تیمی در حد کسب قهرمانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SorkhTimes/132427" target="_blank">📅 18:10 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132426">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
فارس: مدیرای پرسپولیس منتظر تعیین تکلیف رقابتای لیگ هستن و هیچ فعالیتی در نقل و انتقالات انجام نمیدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SorkhTimes/132426" target="_blank">📅 18:03 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132425">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
ترکیب بهترین تیم جام‌جهانی برای دیدار دوستانه با یه تیم ناشناخته اعلام شد.   علیرضا بیرانوند، علی نعمتی، حسین کنعانی‌زادگان، احسان حاج صفی، آریا یوسفی، سعید عزت‌اللهی، امیرمحمد رزاقی‌نیا، امیرحسین حسین‌زاده، محمد محبی، مهدی طارمی و کسری طاهری
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/132425" target="_blank">📅 17:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132424">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
تیم ملی قراره امروز ساعت 19 با یکی از تیم های قَدَر فوتبال جهان بازی دوستانه برگزار کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/132424" target="_blank">📅 17:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132423">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🎙
🔴
محسن بنگر: وقتی که نمی‌تونیم حتی تیم های اماراتی رو ببریم چه اصراری به حضور تیم های ایرانی تو آسیا داریم؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/132423" target="_blank">📅 17:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132421">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
🚨
🚨
🚨
فووووووووووووری
🚨
سی‌ان‌ان: در این هفته خبر رسید که ایران با آخرین پیش‌نویس پیشنهادی موافق است؛ دونالد ترامپ به مشاوران خود گفت که برای تصمیم‌گیری درباره امضای این توافق احتمالی، چند روز وقت می‌خواهد.
‼️
به گفته یکی از مقامات، به نظر بعید می‌رسد که ترامپ…</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SorkhTimes/132421" target="_blank">📅 16:03 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132420">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
شبکه العربیه از منابع مطلع:
🔴
جمهوری اسلامی میخواد اورانیوم غنی‌شده‌ش رو به چین بفرسته، به شرطی که چین تضمین کنه این مواد رو به آمریکا تحویل نمیده.
🔴
به گفته این منابع، خیلی از نکات مربوط به برنامه هسته‌ای جمهوری اسلامی تو مذاکرات الان حل و فصل شده.
🔴
بر…</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/132420" target="_blank">📅 15:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132419">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d178f9cb33.mp4?token=L7hSXqvh5rs7gMdOGaD0cBp1bvdxdqiNT4N4w4S64spTtHWGHlBzl7Mf8cuPb2lCyzsLEWMl5Vkq8NXva9Go3Yb7yoIq0yyjJYpHzZ_Ck4VCbEhoA4hJcrMZLJ5U0sKgD_ewG3zNX5k_v1peS3_FY7SDOox8rThWxdN7LlPv9yi6HFskBV3chr0deyzR4ZQGrmjiW9-HfUAFbkdGb_GsiFmXBzRg3o2XaQfWcacYuKBZ1xvA9oly4x_DvX4ihAbqfO9KNd4ZfghQScjBgwsjSIgNuU14yjdE2NkHnNZQ3g_tQ9LZw7tecS7FHIWtzN1x7s8LDhRStOSsbBHrQsIcPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d178f9cb33.mp4?token=L7hSXqvh5rs7gMdOGaD0cBp1bvdxdqiNT4N4w4S64spTtHWGHlBzl7Mf8cuPb2lCyzsLEWMl5Vkq8NXva9Go3Yb7yoIq0yyjJYpHzZ_Ck4VCbEhoA4hJcrMZLJ5U0sKgD_ewG3zNX5k_v1peS3_FY7SDOox8rThWxdN7LlPv9yi6HFskBV3chr0deyzR4ZQGrmjiW9-HfUAFbkdGb_GsiFmXBzRg3o2XaQfWcacYuKBZ1xvA9oly4x_DvX4ihAbqfO9KNd4ZfghQScjBgwsjSIgNuU14yjdE2NkHnNZQ3g_tQ9LZw7tecS7FHIWtzN1x7s8LDhRStOSsbBHrQsIcPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تیم ملی قراره امروز ساعت 19 با یکی از تیم های قَدَر فوتبال جهان بازی دوستانه برگزار کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/132419" target="_blank">📅 15:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132418">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🏆
موزیک ویدیو رسمی جام جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/132418" target="_blank">📅 15:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132417">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
فارس: مدیرای پرسپولیس منتظر تعیین تکلیف رقابتای لیگ هستن و هیچ فعالیتی در نقل و انتقالات انجام نمیدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/132417" target="_blank">📅 15:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132416">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
اوسمار به باشگاه پرسپولیس گفته واسه فصل بعد بازیکن خارجی می‌خواد و از باشگاه خواسته اگه جذب خارجی ممکن نیست، زودتر بهش بگن تا گزینه لژیونر معرفی کنه
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SorkhTimes/132416" target="_blank">📅 15:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132415">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJb4lP0MsItuIKOFCpyzNvYrlabMkqxc646oe7xjMvY1GkxS1TUV9kdbam8EUp8vC8_oeAx_rf5jKkeXmwUBsjUUsc2bSYRzWwOs7ZyPUBcBo9hnqUyUwOKclHmK2GYlkFrpAV4yEyP_HEt3UUWHUejJEyZHsDMtgZlOOPRLHYN1h7kABqd7g1_4zF6WQFrkdD46ZEF5ElK_LhJBQCxJx1IThdkbWhpxSD55otzMwgvYR4Y4uDfKuTlyK8HxTxZgisvwMYAF0ok3tNSCK4zhouT-0hipGgVlbIaa6_B8XcrV5yt_zpLaC_lnz9Cs5YFxq8D1B4uE7iQwu2Z23pwdeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🇫🇷
مسابقات گرنداسلم رولان‌گاروس رو با بالاترین ضرایب در اسپورت نود پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SorkhTimes/132415" target="_blank">📅 14:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132414">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
✅
خروجی ها احتمالی پرسپولیس:
🔺
میلاد سرلک
🔺
امین کاظمیان
🔺
مرتضی پورعلی گنجی
🔺
میلاد محمدی
🔺
دنیل گرا
🔺
تیوی بیفوما
🔺
امید عالیشاه
🔺
سروش رفیعی
🔺
یاسین سلمانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/132414" target="_blank">📅 14:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132413">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhneXm9CIT_Ut8ZW8AyhIV5aBTHVL6xvDUxXzOZA50skgxkjep7QIeh4mzP_2sJH40dJ916Sfneqyl2OcmEor_ZVbmiNu0eEBBz305DZx7-yMuQmFtB-XL6cAmhTYc-34-WfJ4uaNUrZXrwe9ow-K8xVwfVs4z_Bw-Ao8zUsKd_2tctzANSbFhkg2ZgWf0qQetpJM5Xc2JUXbSwynXZ9JQLbV00BjWaEV4pyP_ICLCugQ5XAJeOqC6W_qTzXCxeuDrVD2yJkJzyPZxEfrd624jEEyULbgoCnIZWyaHi-9dOiLZ9aky6wKfKkWkm9YdUcfHrODsKuZXttYqF-peX7Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اوسمار به باشگاه پرسپولیس گفته واسه فصل بعد بازیکن خارجی می‌خواد و از باشگاه خواسته اگه جذب خارجی ممکن نیست، زودتر بهش بگن تا گزینه لژیونر معرفی کنه
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/132413" target="_blank">📅 12:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132412">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
*یک مقام آمریکایی به الجزیره:*  ما تأیید می‌کنیم که ایالات متحده و ایران به یک یادداشت تفاهم در مورد تنگه هرمز و مذاکرات هسته‌ای دست یافته‌اند.
🔴
توافق بر سر یادداشت تفاهم با ایران در انتظار تأیید رئیس‌جمهور ترامپ است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/132412" target="_blank">📅 11:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132411">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
فرزین معامله گری، علیرضا همایی فر، علیرضا عنایت زاده، سهیل صحرایی، محمدحسین صادقی و محمد گندمی به اردوی تیم ملی امید دعوت شدند   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/132411" target="_blank">📅 11:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132409">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❗️
مدیر برنامه‌های اورونوف به باشگاه پرسپولیس اعلام کرده که حاضر هست قرارداد اورونوف رو تا سال 2030 با پرسپولیس تمدید کنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/132409" target="_blank">📅 10:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132408">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KY4iI0DKzn2dueLjcjjv7xrGW3vGUdenqXXQLVT5WdPINOJH8ugAxZ0JGFYVJA3hpAv0akvIelQbbaAemEyZH3hvZ-9opwQlVYSlC0nOyjpXM0sJu0mPt13MZ6Dv79Mt08FvtUnTsjGo78oeS15skfm1NsSWkqMD3OXWqpsa-BpoLlEY2EUFWoStF1OzyBksKz5eIyGIIQw8kGG9G7JHQF4s2nbmbyiDudQ6Bq6nvG5UzCnETqOOdfkzAjp77N20a3UtM7YZfLy2JX_FBu5ifdKc_8ITsUlWvXTM5Dc_u9P9exwnI0yihOWDyVqCMrgi-v1XqXpZJTuZs5s7xXUVtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اوسمار ویرا به سبک بازی مهدی هاشم نژاد علاقه‌مند شده و به مدیران پرسپولیس گفته است تا شرایط جذب این بازیکن را جویا شوند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/132408" target="_blank">📅 10:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132407">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M2FEPyv0irHgQ-0U3pnKuokRot8QbNCm1Bb-p3kZv5e-6GUeQe4O_4wUj4Q6m_VskF843-GeUSL3bk12085BYjf_58xe_Xe5cvbDZCc8pWUAz1_xQpWqvyKt6A_vmS0jZEVgdKn_gVxZhp0aUNV0d1MiW-Y2ye0WuQ8hOXTXWNQphe9asBAF9fG_xJs2K6EN7565AMtXcboSg4Sj7FO-ZCzSe0GB2qs1YOhDfxhePqdg3-HqHGl0g5Xqy3IbDd6iH05VOCxhjGAPSfhQ_nYjdsQvedOBA8wV8HrvockgSjv-IzccSOy61fAqiR7bh7Zm9s_eaU7MN6CpYg8pOwq4Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آریا یوسفی علاوه بر پرسپولیس، از تیم الشارجه امارات نیز پیشنهاد دریافت کرده است.
✅
ترجیح سپاهان این است که یوسفی را به یک تیم خارج از لیگ برتر منتقل کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/132407" target="_blank">📅 10:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132406">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❗️
🔴
وقتی قرمزآنلاین فاش کرد محمودی از سوی ایجنت ها محاصره شده و برای تمدید قرارداد هر هفته یک ایجنت را به باشگاه فرستاده متهم شدیم به حاشیه سازی اما انچه گفتیم حقیقتت بود.از او خواستیم مراقب باشد.محمودی از برترین استعدادهای فوتبال اسیاست.
🔺
احسان خرسندی، سرمربی…</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/132406" target="_blank">📅 10:29 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132403">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oR5XOjkMkyTE2cDQ3Nj9OtMRg_91mjwjAfQC9NPJK1iZKfjqbnKzccGuS4QWsjSHyQ9jQobf317EpZ09e10jGb4ijIQEtXn0z5NROoI1V74C7VuYtw8Pnfap7wbTWbPxhtRecdf9xuV4yAwkfy9ZcG45_c31Qfe7eVRF6JvfJ_HyZQlRsUwXEisvjBElGxXtsLK8h-KS9l8bpBBczvCsvTUx9EqqMVMgVDqp_rOO3gGbWyFCPabAQWcxqMZRXy5EQzjIlyl8ZuFFTKDRy5OV84Hf2t-CZGiKoGrmI-0bd0CoMoJ1Ilh-62_552EfiT44xllTTUYyHvd2QzT1EGp3ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🤐
دیدار ششم از فینال کنفرانس غرب رو بین دوتیم سن‌آنتونیو اسپرز
📀
و اوکلاهاما تاندر
🆗
رو در سایت اسپورت نود با آپشن‌های متنوع پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/132403" target="_blank">📅 01:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132402">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
خودمون رو گول نزنیم ، بازیکن خارجی با کیفیت نمیاد تو کشوری بازی کنه که ۴۰ روز جنگ رو پشت سر گذاشته و هنوز هم هر لحظه امکان متلاشی شدن آتش بس و آغاز مجدد جنگ در اون وجود داره
🔺
اما آیا این اتفاق و این جنگ باید بهانه ای برای انجام نقل و انتقالات ضعیف برای ما باشه؟ نه به هیچ وجه ، جنگ پیش اومده ، پنجره بسته استقلال و مشکلات مالی سپاهان  باید باعث شه که ما به سراغ بازیکنان جوون و تراز اول داخلی بریم
🔺
امثال دانیال ایری ، مسعود محبی ، فرهان جعفری ، مهدی گودرزی ، پوریا شهرآبادی ، بهرام گودرزی ، پوریا لطیفی فر ، کسری طاهری ، جوون های سپاهان مثل لیموچی و حزباوی و کلی تلنت دیگه تو بازار داخلی وجود داره
🔺
حتی لژیونر هایی مثل محمد مهدی زارع و امثال الهیار صیادمنش که جام جهانی رو از دست دادن و نمیخوان جام ملت ها رو از دست بدن هم میتونن جزو گزینه های باشگاه باشن
🔺
این پنجره بهترین فرصت برای پوست اندازی و جذب بازیکنان جوون و تلنت لیگ هست چون رقبای متمولی مثل سپاهان و استقلال در بازار حضور ندارند و پرسپولیس و بانک شهر در جنگ ۴۰ روزه دچار مشکل مالی نشدند و اکنون وقت خودنمایی پرسپولیس در پنجره نقل و انتقالاتی است تا سال بعد با شایستگی و بدون حرف و‌ حدیث به قهرمانی برسیم و به لیگ نخبگان بریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/132402" target="_blank">📅 00:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132401">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47978b8339.mp4?token=bxC-ypL4xk9dGhfhjUU7EAkeF83Jd5WX-8pPOaJghpFXYB9CyVYkEU9stNb6aY8SiJrpy22uhaAAnlIbCz7RtxGx8P06R2nqaTbnRRNRABNHybDfDDRK8glb3_AvvfQe26kYgbcVS5ciNMTjhOtKQ55Pq8vHNu4np_R6ldio-Ou3i8XT7ND3Yuix7bM8SjCJeMu6L6BF1l9diSLWBbHiYFGVVUdlcL__kTEwtHzQv6gJmanLDDHdrJKr5YYZVWb6B6MZ1Y3QebZcXkvSt1o0e_a8YPWXeHNXpiw2JBrUC6wtR_xORPHG00cJNoiSbgkYQJahWARV6xiOzknw4nm5qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47978b8339.mp4?token=bxC-ypL4xk9dGhfhjUU7EAkeF83Jd5WX-8pPOaJghpFXYB9CyVYkEU9stNb6aY8SiJrpy22uhaAAnlIbCz7RtxGx8P06R2nqaTbnRRNRABNHybDfDDRK8glb3_AvvfQe26kYgbcVS5ciNMTjhOtKQ55Pq8vHNu4np_R6ldio-Ou3i8XT7ND3Yuix7bM8SjCJeMu6L6BF1l9diSLWBbHiYFGVVUdlcL__kTEwtHzQv6gJmanLDDHdrJKr5YYZVWb6B6MZ1Y3QebZcXkvSt1o0e_a8YPWXeHNXpiw2JBrUC6wtR_xORPHG00cJNoiSbgkYQJahWARV6xiOzknw4nm5qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مجری صداوسیما:
◻️
آقای حدادی چه گیری دادی که باید حتما در آسیا حضور داشته باشید؟ حتی اگر CAS رأی بدهد و امتیازات تراکتور و استقلال کسر شود و سپاهان هم مجوز حرفه‌ای نگیرد، پرسپولیس به آسیا نمی‌رود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/132401" target="_blank">📅 00:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132400">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
از بین شهریار مغانلو و علی علیپور؛ یکنفر از لیست نهایی تیم ملی برای جام جهانی 2026 خط خواهد خورد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/132400" target="_blank">📅 23:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132399">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hF5qKGphP3v4jJ52niOlVyS9osYjOX0PSbFlMsnECA8dijk-JNp6ksWINcjT_QXJURUCwNODiM9VQRAKZd0_t-BAONjCz3XrcQ-DplTlC-CLNfCMkdQhGWSEN6CrEmLrFppngleiLtuR54o_AfN7-7tgxUqHDoI-Cf5LjHaNKgfwQYEyklU-KqvKhJt4XuOcGk4s-A1BaX2Hv-FIbcDmatnOaqug677oyCV1PJiHcgnBnhl9oQNCR3SxueQogNWIeP4emdNjRdf0f7vGlCQ8ldpRTMyBibpAw6pCIo_E7QMfu_u56ngvaQJlgcQMnJxZy9ceo6zn3Qu9Deks5pnbxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پیمان حدادی:
اگر با سروش رفیعی و میلاد محمدی برخورد نکنیم، توهین به بقیه است. به هیچ بازیکنی اجازه ندادیم که سر تمرین نیاید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/132399" target="_blank">📅 23:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132398">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‼️
فداحسین مالکی، عضو کمیسیون امنیت ملی مجلس:
🔺
بیشتر پیشنهادات ایران در مذاکرات پذیرفته شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SorkhTimes/132398" target="_blank">📅 22:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132396">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❗️
سی‌ان‌ان : ترامپ تو تلاشه قبل از تایید توافق با ایران، مشورت بگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SorkhTimes/132396" target="_blank">📅 21:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132395">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GB9CD4iTRmiMRxkXqY0SWLtBHo1rzbrfyaBNoBMwVxR_LYQUp4Kg3JdhVb74Zi03PMwL9P0LMbz5YiK8Y4O_NJO7AIbu_bE67ZNQmIhoz92Sv871XhuiCxd4oXCPclkrjf5qLHNQ-HZ_Q-8zMEX2l431GZ2O-_aEU1V93nXdpK3W8lK5XU6RcxE-vlKZcw0xDd4agcMuZ4biChhA8gCgjxriZs8E5dIV7oMhiDK4DjHauUT52DflyoDLU4ZgWuGWkaPWGM3EdFJ--sklwVa8qe34BqG5EE7OpGhUYN2sTq3687sABWvZCwJOhz2SD_9TsnHd6eg3m3uPPK3stay-uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کیت‌های ایران و هم‌گروه‌هایش در جام‌جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SorkhTimes/132395" target="_blank">📅 21:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132394">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
*یک مقام آمریکایی به الجزیره:*  ما تأیید می‌کنیم که ایالات متحده و ایران به یک یادداشت تفاهم در مورد تنگه هرمز و مذاکرات هسته‌ای دست یافته‌اند.
🔴
توافق بر سر یادداشت تفاهم با ایران در انتظار تأیید رئیس‌جمهور ترامپ است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/132394" target="_blank">📅 21:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132393">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ll1F4DYF5vfhNwrgCn576ZO-OXb-B8QwdAbHtNvQGEK5Lct-YsvbF22x7giPWI7rvbhJOk17pI5V4JnvWQ2t64NtRF4GO-nVUZD1QUWpQ22OcnhriFN5_NqSQfsSQfFOFBvhStlJktMjdl5Jp_g81nCg0ylVQHak7xzttCgeR-bg-ttABH5PKkYzCIJzVPdpm6qgPU_WZjn_AlRNWmPHvIG1zBgpwqy_e1tOEwjO6of15ht53pNbIbhlnJe9AxBTJbBh3bZhl5Xnru9bUv0VaIQhWdVzDlhIYuurer_1OhQHWrXnH8B9SPsNAsflM03ns4sz6TZMnU4x3uVmreoBYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کشور های دارای سریع ترین اینترنت موبایل در جهان
❌
ایران اصلا حتی تو لیست هم نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SorkhTimes/132393" target="_blank">📅 21:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132391">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
ادعای العربیه به نقل از یک منبع دیپلماتیک :
🔻
توافق بین واشنگتن و تهران در دو مرحله خواهد بود
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/132391" target="_blank">📅 20:58 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132390">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDfdpSbUxvTAUCjpl4mQrHUd-KJZQJ1eZcVlwIPLM_joZBzf4LuHETvflTl4meKc1QN7e_8bnJQzwhaMx1_tWzNpJkKMD0_2b6vjC9gV53GiGsdTeGgkJkIBH0U-II48IcZ1u80gp26WW4sZ719o72WQV8BNO1bdEpFBxIXfSHxX6kvjYa3LpEYPiFXkfLrxEkHGGSdmMkr0dObVBJn4JjipF0cIiX7M9qCu0lPTPh7qssA-PqdImli1Fs2voMJhb_ZJgRRvoge-KkeTcglsbj23XFMiffMcp9fV1OvW72xfB0jg_BYe6tvDaBSEtmh_ObYLC7WFyQPj_wDt5nfdqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🇫🇷
مسابقات گرنداسلم رولان‌گاروس رو با بالاترین ضرایب در اسپورت نود پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/132390" target="_blank">📅 20:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132389">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gCVrsyPaf0s5Y9GgozxQbspKbPl4iwUbEUdpjP1mlQ_1wW_n7U1ZxHEIF-g1EU7TVt5PT_ou39Gml6a1VxAhRYUFFTdjGp3_snwqdPASPvj_gWn1I-XlToLZpLCxShizJ966uLxVcS16LiApS4CA06ExaSuYJjjXHIRDNMz-8l2Izacaauw5cx4uwkLOOvPAmtei-93AnChPhwxmZTeTuXxuH_gJdGoBcgAUqHhHpl-cE962Dcz4niJCXy_wrkOBVGeL013totlbTPmk1R0VpXCU6zf29ChTCyCUT7QhqFuT9XcPVr1E_97Bp9M196E2TVmfn_jYopkteS7Wp9euxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ادعای العربیه به نقل از یک منبع دیپلماتیک :
🔻
توافق بین واشنگتن و تهران در دو مرحله خواهد بود
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/132389" target="_blank">📅 20:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132388">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
مبلغ رضایت نامه آریا یوسفی از سوی باشگاه اصفهانی ۲۰۰ میلیارد اعلام شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SorkhTimes/132388" target="_blank">📅 19:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132387">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">⁉️
⁉️
نت بلاکس: سه ماه پیش در چنین روزی Iran دسترسی به اینترنت جهانی را قطع کرد. در حالی که اتصال اکنون تا حد زیادی بازگشته است، شاخص‌ها نشان می‌دهند که کاربران هنوز با فیلترینگ شدید مواجه‌اند، مشابه دوره موقت بین اعتراضات ژانویه و آغاز جنگ.
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/132387" target="_blank">📅 19:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132385">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
✅
خروجی ها احتمالی پرسپولیس:
🔺
میلاد سرلک
🔺
امین کاظمیان
🔺
مرتضی پورعلی گنجی
🔺
میلاد محمدی
🔺
دنیل گرا
🔺
تیوی بیفوما
🔺
امید عالیشاه
🔺
سروش رفیعی
🔺
یاسین سلمانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SorkhTimes/132385" target="_blank">📅 18:47 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132384">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
آکسیوس: ایران و آمریکا در حال حاضر به توافق رسیدن و فقط تأیید نهایی ترامپ باقی مونده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/132384" target="_blank">📅 18:46 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132383">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
✅
خروجی ها احتمالی پرسپولیس:
🔺
میلاد سرلک
🔺
امین کاظمیان
🔺
مرتضی پورعلی گنجی
🔺
میلاد محمدی
🔺
دنیل گرا
🔺
تیوی بیفوما
🔺
امید عالیشاه
🔺
سروش رفیعی
🔺
یاسین سلمانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/132383" target="_blank">📅 18:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132382">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
طبق گزارش Axios، این توافق شامل موارد زیر خواهد بود:
🔴
دسترسی بدون محدودیت از طریق تنگه هرمز بدون عوارض یا مداخله از سوی ایران.
🔴
محاصره دریایی آمریکا نیز برداشته خواهد شد، اما متناسب با بازگشت حمل و نقل از طریق تنگه هرمز خواهد بود.
🔴
تعهد ایران به عدم دنبال…</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/132382" target="_blank">📅 18:16 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132381">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
آکسیوس: ایران و آمریکا در حال حاضر به توافق رسیدن و فقط تأیید نهایی ترامپ باقی مونده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/132381" target="_blank">📅 18:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132380">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
✅
خروجی ها احتمالی پرسپولیس:
🔺
میلاد سرلک
🔺
امین کاظمیان
🔺
مرتضی پورعلی گنجی
🔺
میلاد محمدی
🔺
دنیل گرا
🔺
تیوی بیفوما
🔺
امید عالیشاه
🔺
سروش رفیعی
🔺
یاسین سلمانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SorkhTimes/132380" target="_blank">📅 17:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132379">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
آکسیوس: ایران و آمریکا در حال حاضر به توافق رسیدن و فقط تأیید نهایی ترامپ باقی مونده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/132379" target="_blank">📅 17:58 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132378">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
🔴
🔴
و تمام
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/132378" target="_blank">📅 17:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132377">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
🔴
🔴
و تمام
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/132377" target="_blank">📅 17:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132375">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">💬
🎙
🔴
عبدالصمد ابراهیمی، کارشناس حقوقی:
🗣
شکایت پرسپولیس از فدراسیون و سازمان لیگ زمان بر است و رای بیرانوند قبل از جام جهانی صادر نمی‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/132375" target="_blank">📅 17:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132374">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
✅
خروجی ها احتمالی پرسپولیس:
🔺
میلاد سرلک
🔺
امین کاظمیان
🔺
مرتضی پورعلی گنجی
🔺
میلاد محمدی
🔺
دنیل گرا
🔺
تیوی بیفوما
🔺
امید عالیشاه
🔺
سروش رفیعی
🔺
یاسین سلمانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/132374" target="_blank">📅 17:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132373">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pI8ZsCCNbbgKgEor_7AWM7LkLZ91UyYSa-0qUiL7Q89LlQx_3UB0VnxlhqSuC1hGejfgxr-S8on5HdGich_VP4dgd6gH6JajwEP21Sqv60RC8q42tGOY_4SSKohxvwIEUTJqgaFdafENdMTYzAouDGRFddmBvZhOqo-f4HwKTyiGODreKqPO4c2D2ZRJ5O2UfLEk_TTzfpht7ZReqVA-o55ceMqTbXgcRX0tEZK_WNDzBPyynTireHMLgQuRtPHGx86fk7YeobzhGEGhiopG3_Zrzqe369gI00J0zloJh2xummhdFNlDklCLlBiCydthhcO2aEa0lZ2CEaUf11EY8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚡️
هر مسابقه یک فرصت، هر انتخاب یک هیجان!
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SorkhTimes/132373" target="_blank">📅 15:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132372">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✅
فارس: هنوز جام‌جهانی شروع نشده اورونوف از دو تیم روسی روبین‌کازان و دینامو مخاچ‌قلعه پیشنهاد دریافت کرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/132372" target="_blank">📅 15:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132371">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
مهدی طارمی - شجاع خلیل زاده - دانیال اسماعیلی فر و احسان حاج صفی تا این لحظه به دلیل خدمت در سپاه ، احتمال صدور ویزا واسشون پایینه و به جام جهانی نمیرن ، البته فدراسیون درحال رایزنیه ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/132371" target="_blank">📅 15:38 · 07 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

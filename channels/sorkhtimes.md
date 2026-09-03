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
<img src="https://cdn4.telesco.pe/file/HVHNnZVEfZwhBXFC_ykW-C95tQbmsa7EBoa4bG9tuNn_APwdDG2dmZLZ2wjt9la-4AKAUg_6jvi9VfyrNGLzb_4gja7JFUIo2sAdYQp5-_9o1jDq3Dp3lkgyRr_HMk8dAlzJFR2ee-ShVm1Y8eVY1oJXr94mJ457tMV_a4El1A8bbmXGGzjEYkmoihil4orZUjrYwifrMTUr49LpDK5ErMFzMdvrXRndeZqtEmzu1Rp3gKAY-KVZJ9o_GYwJqzaNbBdKaSZUwACAHgDCyUnc0OxM5fWW1zaLt_G2_q6cQvVIsyil0g92tCwra3bB2BOs6DrDUV7Hyl0O1_q6D9_fcw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 17:11:05</div>
<hr>

<div class="tg-post" id="msg-139486">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✔️
✔️
دانیال گرا مدافع مجارستانی تیم پرسپولیس برای هفته پنجم از لیست بازی خط خورد تا یک سهمیه خارجی سرخپوشان برای فصل آینده به خطر بیوفته.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/SorkhTimes/139486" target="_blank">📅 16:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139485">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✔️
✔️
خبرگزاری مهر:
🔴
پرسپولیس پیشاپیش شکایت خودشو برای حضور یاسر آسانی تو دربی آماده کرده. پرسپولیس اعتقاد داره کمیته انضباطی و سازمان لیگ صلاحیت لازم رو برای پرونده درباره یاسر آسانی رو ندارن و استعلام فیفا باید منتشر بشه
🔴
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/SorkhTimes/139485" target="_blank">📅 16:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139484">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
❌
❌
❌
طولانی‌ترین روند شکست‌ناپذیری در تاریخ دربی؛ پرسپولیس با 20 دربی بدون باخت
✔️
✔️
کیسه کش حسرت برد دربی رو به گور می‌بری
😂
🫵
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/SorkhTimes/139484" target="_blank">📅 15:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139483">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9bc0b70b2.mp4?token=HrdRYNy9p0jp8nHNEeZsd0AzntHmzw4RXvOj4MarbdShq5CIB-26Nn-8xN_7lOHYb9hHtTqCRnHug96-j8zYUo6XJwJQ7NSn7PVVz3pV4jSPoXGucjT97dVy1IPjyV2FHn0RxcG2QDAiht0YlJirRDi3TDgf8khdQLd-rAkaLC4bJwdFIh-jiDof6GmLWsB_-rnGq7lxqgrKQpfat4EwbC9kYSJX7Ev8F96IF_gavpRv4Jj6T9WuRJ4GTYvsoiAO_5b7DlhRiOCmxUwAEWKYhcHpJap1KlzAEoylBDvyjA8rkgQJdRyUUZo2yh_wIipqkhb9Fcsmj4L3ft3K_m9ZQhRgAqpvre9lRExkDg_JrK80XbrtoHruHFR6YhPx2L__7MLHXd27un5_W0USAp6XIilSuf5-41SDYnxmkXoyeV9x6PAw0m5S21Q1Q86NwYGvbxWOipIVVoBJi03wAKxbnziOY8s9SlwYVuHfw0vfyLPqsbCPniTF7HRmxiXXWQZZnh6m68YBPPHVqsEZNSijjBHLle-eJt_ZHYALPtaNAWh8b9FtA3mBntgh0Pneqbd6Nf5kINIHmuG1a-fkaw12P9DbsuMhWWYIuYTnwMi3UpurIu0dYg83SSNDONjFuYs97Z5gBHqQ7hn2mvvhQle8PJ9Zq93ppaIIf6KS3Yzq42k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9bc0b70b2.mp4?token=HrdRYNy9p0jp8nHNEeZsd0AzntHmzw4RXvOj4MarbdShq5CIB-26Nn-8xN_7lOHYb9hHtTqCRnHug96-j8zYUo6XJwJQ7NSn7PVVz3pV4jSPoXGucjT97dVy1IPjyV2FHn0RxcG2QDAiht0YlJirRDi3TDgf8khdQLd-rAkaLC4bJwdFIh-jiDof6GmLWsB_-rnGq7lxqgrKQpfat4EwbC9kYSJX7Ev8F96IF_gavpRv4Jj6T9WuRJ4GTYvsoiAO_5b7DlhRiOCmxUwAEWKYhcHpJap1KlzAEoylBDvyjA8rkgQJdRyUUZo2yh_wIipqkhb9Fcsmj4L3ft3K_m9ZQhRgAqpvre9lRExkDg_JrK80XbrtoHruHFR6YhPx2L__7MLHXd27un5_W0USAp6XIilSuf5-41SDYnxmkXoyeV9x6PAw0m5S21Q1Q86NwYGvbxWOipIVVoBJi03wAKxbnziOY8s9SlwYVuHfw0vfyLPqsbCPniTF7HRmxiXXWQZZnh6m68YBPPHVqsEZNSijjBHLle-eJt_ZHYALPtaNAWh8b9FtA3mBntgh0Pneqbd6Nf5kINIHmuG1a-fkaw12P9DbsuMhWWYIuYTnwMi3UpurIu0dYg83SSNDONjFuYs97Z5gBHqQ7hn2mvvhQle8PJ9Zq93ppaIIf6KS3Yzq42k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
❤️
👀
✔️
تو این صحنه کسی متوجه نشد ولی وقتی از دوربین نزدیک تر صحنه پخش شد مشخص شد نوک انگشتای نیازمند بود که باعث شده توپ به تیرک بخوره وگرنه گلو خورده بودیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SorkhTimes/139483" target="_blank">📅 15:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139482">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
❌
20 بازی بدون شکست
🔥
✔️
حسرت کیسه در آستانه ده سالگی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SorkhTimes/139482" target="_blank">📅 15:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139481">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❤️
خدا بنده لو، بازیکن پرسپولیس:
⚪️
بیش از اندازه در مورد ارونوف حرف زده می شود. چیز خاصی اصلا وجود ندارد و هنوز خیلی از بازی ها باقی مانده است. او اصلا افت نکرده است و اصلا زیاد بازی نکرده که بخواهد افت کند. همه از کیفیت اورنوف خبر دارند و هر تصمیمی سرمربی…</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/139481" target="_blank">📅 13:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139480">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">⭕️
⭕️
⭕️
با اعلام یاسر همرنگ
🚨
کوپال ناظمی داور دربی شد
📺
موعود بنيادی فر داور var شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SorkhTimes/139480" target="_blank">📅 13:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139479">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✔️
✔️
باشگاه استقلال نسبت به عملکرد و سرعت بالای تیوی بیفوما مشکوک شده و احتمال می‌رود درخواست تست دوپینگ از این بازیکن پرسپولیس را مطرح کند.//هفت صبح
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/139479" target="_blank">📅 13:37 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139478">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jo5R-94qlvy-51HFMSF2n56xLSjHH1lhC15pZ7hzB_c8xA6YUkM3maxqQ1O_y9uwQfcwJnfpNT3uqE2qcqw2JmmNaKt61pTLyho-1Kzgry4DokoaXycIv6V722NNDsm73bgfiDncqRreEny7ALrT1sfiSMk5Ks6MujLesPshjwWb_PFnAGXOXSRagfW5qPq7OpCui-s-RbAR5Te_ukNurSPFldIG1l6x0N8Pdw_y695GVGP4zkI2xKFtIQVHnumWBedhIewHHYokMolxafmWtmwL5898DVcq-qK_2wuDr2Ak9IdxsHifCMU1AtrLTOzOZtUFd_Jb9Ey6lN8beTzqkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سوسیداد و سلتا؛ جدالی برای سه امتیاز
دو تیم آماده برای یک نبرد نزدیک و تماشایی
کدام‌یک دست بالاتر را خواهد داشت؟
[
رئال‌سوسیداد
🔵
🆚
🔴
سلتاویگو
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/139478" target="_blank">📅 13:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139477">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔄
🔄
🔄
با حضور یاسین سلمانی در بازی دیشب حالا مهدی تارتار به تمام بازیکنان پرسپولیس بجز محمدحسین صادقی که تا حالا در لیست قرار نگرفته بازی داده و تمامی بازیکنان با ذهنیت آماده به سراغ ادامه‌ی لیگ میرن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/139477" target="_blank">📅 13:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139476">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🤩
| فارس:
🔴
❤️
🔄
تارتار امید چندانی به دنیل گرا ندارد و حتی درصورت بهبود مصدومیت هم نیمکت نشین خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/139476" target="_blank">📅 10:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139475">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✔️
✔️
باشگاه استقلال نسبت به عملکرد و سرعت بالای تیوی بیفوما مشکوک شده و احتمال می‌رود درخواست تست دوپینگ از این بازیکن پرسپولیس را مطرح کند.//هفت صبح
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/139475" target="_blank">📅 09:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139474">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
♨️
🗞
| #فوووری از تسنیم:
🔴
🔵
👤
پرسپولیس بخاطر استفاده از آسانی مستقیم به فیفا شکایت می‌خواد بکنه نه کمیته انضباطی
⚠️
❌
کمیته انضباطی فدراسیون شکایت های گذشته در مورد آسانی رو رد کرده بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/139474" target="_blank">📅 09:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139473">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✔️
✔️
عادل فردوسی‌پور: ترابی قطعاً ادامه فصل رو از دست میده، با خودش صحبت کردم و گفت دو پزشک بهش گفتن رباطش پاره شده و باید عمل کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/139473" target="_blank">📅 09:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139472">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✖️
✖️
هافبک و کلا استقلال برداشته و خیلی خالی هست هافبک ما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/139472" target="_blank">📅 09:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139471">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❤️
❤️
❤️
❤️
🔴
صبحی که دربی و مساوی کردیم و هنوز داریم حسرت تک به تک نزدن علیپور میکشیم بخیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/139471" target="_blank">📅 08:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139470">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsvU1A7tYkHdl9IMvFz-wS__-7ZtVjFXvFfcM0S3oQ_mZ3zFs1Ur9hv22rh_2wCc9FUr3QxEh9wFIGLsyo3XKYQV3KXUjAjsyzeIj0tQIpTsqdnFoo_t8QYgGCFDq3VPE_fidq5QhCLxrz6FKfnwZpF5nrsFhlnPJuTqS5Dzt0votnsa8TEcE5k8u2ySemEZewKDKEY0JCu1qRmLp39jWun8VDTPo5Ie3xGlnZKlbVbGSfgdsdpr8H6GLPEWuhX6pkM4XMWxjwds5m6MNJBisrDSmOKizyWguoheiFBedUCdqgdt8Vkr5ZzxLoBs9N4k9m-tz8b-vXs_1NqxS4Bj9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
دوئل‌های جذاب در یو‌اس اوپن!
🎾
جیمی فاریا
🆚
کارلوس آلکاراز
🎾
رِی ساکاموتو
🆚
فرانسیس تیافو
🟡
کدوم ستاره‌ها از این نبردهای حساس سربلند بیرون میان؟
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی دیدارهای یواس اوپن همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/139470" target="_blank">📅 01:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139469">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✅
✅
سه بازی مهم هفته بعدی
✔️
شنبه :گل گهر و تراکتور
✔️
یکشنبه : آلمینیوم اراک و کیسه در اراک
✔️
دوشنبه : پرسپولیس و ذوب آهن شهر قدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/139469" target="_blank">📅 01:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139468">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">⚽️
⚽️
استقلال و پرسپولیس امشب در مجموع 33 شوت بهم زدن که 9 تاش در چارچوب بود، برای درک بزرگی این عدد باید بهتون بگم که در مجموع دو دربی قبلی 33 شوت زده بودن که 10 تاش تو چارچوب بوده که یعنی امشب به تنهایی اندازه دوتا دربی قبلی روهم موقعیت دیدیم
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/139468" target="_blank">📅 00:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139467">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0X8LxkR-zoI7ukPi6zKc-wwRAHyC0nlCUMCrM8JFhuH88h-l7JEssXzmoNR8JMUj15W8i8JctUIDuNJ3tAkhiLK8ugpfd7tD0GXqiZZhficXWOYdFI09B4BHiLVxPfb7GwP9WEoyAB268vmKsw1GTo9tyUVACdxsfrEgPspkHA47pVKO_mwhcb1MtTl-dp9NWqfNVH1E68DvdS1Bng0puZy5zInDufcBFEDv67SsgE5mvXKORRP3cwXv2QfIsVwH3KWAspTeo2_jsG-UYzHAHLMuFzLM9ORLHmfnwBdcBYv3PkGhkVU04ocWH_5fyr9rzAJluH5NQaKH1-T6W25mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚽️
استقلال و پرسپولیس امشب در مجموع 33 شوت بهم زدن که 9 تاش در چارچوب بود، برای درک بزرگی این عدد باید بهتون بگم که در مجموع دو دربی قبلی 33 شوت زده بودن که 10 تاش تو چارچوب بوده که یعنی امشب به تنهایی اندازه دوتا دربی قبلی روهم موقعیت دیدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139467" target="_blank">📅 00:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139466">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
❌
20 بازی بدون شکست
🔥
✔️
حسرت کیسه در آستانه ده سالگی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/139466" target="_blank">📅 00:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139464">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
❌
فارس : نظر می‌رسد نظر کادرفنی پرسپولیس نسبت به ۲  بازیکن دانیل گرا و تیوی بیفوما  تغییر کرده و احتمال ماندن آنها در جمع سرخپوشان بسیار زیاد است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/139464" target="_blank">📅 23:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139463">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnxzwnxYcDi_Mv46NEhUhI7YYY5jVi7WS4dYj9w8wKI_Jqi5chwkgScFxtL9RDK-maG46b1UIwAhLvFUJMzjhLC-AXBtVmKb4o2RzuefziYT5OTOP_z2gvx6dHS5ps88kNpCUJJBz-Qs4nK6jyw0P3DsQpMklOxdyn_E8DoLL9_H0zRmLkcEuZecUZUNrGn7pR8XyICQpA3UaBibBgFStgqiNodFDbvfUcmUBEOuVFoKLtg07oSFrdY0EzmudxpQyaW1X83e34D2utkFj2N6iAWnUVT4iZcYGPvDBJi03ZJbXzgXuRb0d-oR68fKtD5vBGsoVkEwImjp8G1JnEDdcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
✔️
پایان بازی | شکست ناپذیری پرسپولیس به ۹ سال رسید/دربی جذاب برنده‌نداشت  استقلال
1️⃣
-
1️⃣
پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/139463" target="_blank">📅 23:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139462">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fc62967a0.mp4?token=r5p7xDrwRI3fTbBJxVQO7ohqatT_beZWnBLrtf9GQjJ93x9zfinjntWgmQUZAt8VJP5UmKwKwK_Ebt08lThs5sbt7P2vF_k3ECoosQdBJCy1u-67E68gTrM9yuZq_pTL8dr61dVAdtareQRSSXdUnVT3BAsWuAhKZOoSuGzsK8puTCnilGhMJfa0E_2oVPQAcvDYMFm0cM6dmvvfIUnrSdBj5dgb_TBdGDlQLK9qas2COCurHvYh_K4A8YVy0TQs24q-afxwRQaJMZWU7b79m1x1dQUy0hf26k6Bi6K4XfD1_C-OS_l9weMzdG-IULOaUPoQIxkLB-xNpKygVbKMaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fc62967a0.mp4?token=r5p7xDrwRI3fTbBJxVQO7ohqatT_beZWnBLrtf9GQjJ93x9zfinjntWgmQUZAt8VJP5UmKwKwK_Ebt08lThs5sbt7P2vF_k3ECoosQdBJCy1u-67E68gTrM9yuZq_pTL8dr61dVAdtareQRSSXdUnVT3BAsWuAhKZOoSuGzsK8puTCnilGhMJfa0E_2oVPQAcvDYMFm0cM6dmvvfIUnrSdBj5dgb_TBdGDlQLK9qas2COCurHvYh_K4A8YVy0TQs24q-afxwRQaJMZWU7b79m1x1dQUy0hf26k6Bi6K4XfD1_C-OS_l9weMzdG-IULOaUPoQIxkLB-xNpKygVbKMaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
بیفوما امشب دوباره یه استارت ۴٠ متری زد فرعباسی وحشت کرد دستپاچه توپو زد بیرون‌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/139462" target="_blank">📅 23:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139461">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✔️
جدول لیگ بعد از هفته پنجم .اختلاف با صدر سه امتیاز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/139461" target="_blank">📅 23:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139460">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❤️
خدا بنده لو، بازیکن پرسپولیس:
⚪️
بیش از اندازه در مورد ارونوف حرف زده می شود. چیز خاصی اصلا وجود ندارد و هنوز خیلی از بازی ها باقی مانده است. او اصلا افت نکرده است و اصلا زیاد بازی نکرده که بخواهد افت کند. همه از کیفیت اورنوف خبر دارند و هر تصمیمی سرمربی…</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/139460" target="_blank">📅 23:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139459">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
❌
کنعانی زادگان: تارتار تیم خیلی خوبی بسته است و امیدوارم آخر فصل قهرمان شویم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139459" target="_blank">📅 23:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139458">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
❌
کنعانی زادگان: تارتار تیم خیلی خوبی بسته است و امیدوارم آخر فصل قهرمان شویم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/139458" target="_blank">📅 23:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139457">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❤️
❤️
❤️
ترکیب پرسپولیس برابر استقلال
🇮🇷
پیام نیازمند، مهدی زارع، حسین کنعانی، مهدی تیکدری، مجید عیدی، پویا پورعلی، محمد خدابنده‌لو، محمدمهدی محبی، تیوی بیفوما، ایگور سرگیف و علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/139457" target="_blank">📅 22:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139456">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✔️
✔️
✔️
هر دو گلر بد خوردن گلارو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/139456" target="_blank">📅 22:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139455">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✔️
✔️
مهدی تارتار: ما و استقلال خانه نداریم!
✔️
پرسپولیس و استقلال متضرر می‌شوند و ما خانه نداریم در شهرقدس از پتانسیل هواداری نمی‌توانیم استفاده کنیم.امیدوارم هر چه سریع‌تر استادیوم آزادی آماده شود.
✔️
اورونوف هم یکی از آن‌هاست هر کسی از هم‌پستی‌اش جلو بزند،…</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/139455" target="_blank">📅 22:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139454">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✔️
✔️
تارتار در نشست خبری: گروه داوری امروز خیلی خوب عمل کرد، خسته نباشید به آنها می گویم/ امروز هم پرسپولیس خوب بازی کرد و هم استقلال
✔️
✔️
به خاطر گل مساوی که خوردیم واقعا حسرت خوردیم
✔️
✔️
هم ما می توانستیم برنده بازی باشیم هم استقلال اما در مجموع ما یک مقدار…</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/139454" target="_blank">📅 22:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139453">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👤
خدابنده لو، بازیکن پرسپولیس:
✔️
بازی بیرون خانه برای ما حساب شد‌. امیدوارم ورزشگاه آزادی زودتر درست شود. در مورد خودم نمی توانم اظهار نظر کنم. الان فضا بازتر است و امیدوارم ادامه دار باشد. دو تیم موقعیت های خوبی داشتند و آمده بودیم برای بردن اما حیف شد.‌شرایط…</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/139453" target="_blank">📅 22:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139452">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00bebc6bdd.mp4?token=K0QbmmprOLReMEabQ9cniBP-p_xy38BQg7B9rfaunZ2yVva8Wi92WUS_ePlhfeAMVUPAcNrbZXHvXaXco4cuY-vsIz0r2FcDHlt4lGiSMRq6npl00Ne_X9VWVYhj5eGqOOjICvQgEHMdogURtaATnnuEsh-E0aRLzapIR7bWUKscF3GgVlZXSV8_PzhvQoieTLyyVX09x0WPUuqPHZmdnU6r0Uke7MNl1UjHM3-OrHMEaeiibMKCAH2pqnWN81w7Gx5qFy2dWyixHcVVV7zns_HTBJdSDLE3jK6MWkuzrADS2Wywu59nxogqmobZBJgixWPwvWrG5pq2B9uenmMHkzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00bebc6bdd.mp4?token=K0QbmmprOLReMEabQ9cniBP-p_xy38BQg7B9rfaunZ2yVva8Wi92WUS_ePlhfeAMVUPAcNrbZXHvXaXco4cuY-vsIz0r2FcDHlt4lGiSMRq6npl00Ne_X9VWVYhj5eGqOOjICvQgEHMdogURtaATnnuEsh-E0aRLzapIR7bWUKscF3GgVlZXSV8_PzhvQoieTLyyVX09x0WPUuqPHZmdnU6r0Uke7MNl1UjHM3-OrHMEaeiibMKCAH2pqnWN81w7Gx5qFy2dWyixHcVVV7zns_HTBJdSDLE3jK6MWkuzrADS2Wywu59nxogqmobZBJgixWPwvWrG5pq2B9uenmMHkzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
خدابنده لو، بازیکن پرسپولیس:
✔️
بازی بیرون خانه برای ما حساب شد‌. امیدوارم ورزشگاه آزادی زودتر درست شود. در مورد خودم نمی توانم اظهار نظر کنم. الان فضا بازتر است و امیدوارم ادامه دار باشد. دو تیم موقعیت های خوبی داشتند و آمده بودیم برای بردن اما حیف شد.‌شرایط تیم خوب است و همه متحد هستیم. هواداران صبورتر باشند ما تغییرات زیاد داشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139452" target="_blank">📅 22:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139451">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✔️
✔️
✔️
مهدی تارتار : بازی زیبایی دیدیم/هم ما و هم استقلال میتونستیم برنده باشیم/از مسئولین اصفهانی و از داور تشکر میکنم/حسرت میخورم که نبردیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/139451" target="_blank">📅 22:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139450">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVH0btZVD_ifeEQv9lADHK4M_ZPnwo6DRp0akEXzvhQIluZZiBDQ7ch9gtlAdVharA67Eas90BSoTL5OQqDknInOzfta78Q60YC88ygK17GGP8m7gU7QTEa-jHQxj0C0Ihv4W1rm3xYfu2fb629IwtUIF7J_8YnQSDXE9fRgYwQPd6ZSJPeCPnmdyKiQQ76wSiB0LT5jZitdgtZLCrxK37OxLKAMpWVZXTHIVpad4I4RucRqWGH8r7XjG4xiVYSGC5bFwVpxk3QmDx79FKrrnH9C-fcrgJAFffr8srUwF-1yBSr8mhtDhFvQACVA2IFjzGfOcjeoODDfXgPX5jyYgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
جدول لیگ بعد از هفته پنجم .اختلاف با صدر سه امتیاز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/139450" target="_blank">📅 22:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139449">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✔️
✔️
ترامپ: من استفاده از سلاح هسته‌ای علیه ایران را رد کرده‌ام/ ما دوست داریم با همه کنار بیاییم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/139449" target="_blank">📅 22:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139448">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❗️
🤩
🤩
خداییش یکی از بهترین داربی‌های چند وقت اخیر بود
✔️
داربی چهارشنبه‌شب نقش جهان، برخلاف پیش‌بینی‌های اولیه/ اطمینان وریا در مقایسه با سیدجلال، موقعیت‌های استقلال بیشتر بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/139448" target="_blank">📅 22:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139447">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4d2d12ad.mp4?token=MAx-4GLDF_Jx1lQDeAtYxCgla_YUE-b9Hikn09Lrz1z8387eOqPsp3xzI8gJwW-yIpOGLVWQln3kzUPThibaqi445BAOzlzoIrOiQZ1QsmvhdKUaXlFap4y5E55Zmyr-t37L8krF2L-QsfZ-chQdER1c82nyM76RrfrJTVSvPP-WgK0AKpuYKkOOzHD0f_HtMdgE8XEIzu0L4758DFpoF5O357ciTRwsu8vNFHhtQCloAKVZu_0kEgPtnfHvr_R_3JybgfReklRoaWQ9pGmI6oXBocQZiy0te3Rpl7C8VIhx1Es_-JgWjxDGZphHoZL1A-f87lSXXyIhVhmKrIqiGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4d2d12ad.mp4?token=MAx-4GLDF_Jx1lQDeAtYxCgla_YUE-b9Hikn09Lrz1z8387eOqPsp3xzI8gJwW-yIpOGLVWQln3kzUPThibaqi445BAOzlzoIrOiQZ1QsmvhdKUaXlFap4y5E55Zmyr-t37L8krF2L-QsfZ-chQdER1c82nyM76RrfrJTVSvPP-WgK0AKpuYKkOOzHD0f_HtMdgE8XEIzu0L4758DFpoF5O357ciTRwsu8vNFHhtQCloAKVZu_0kEgPtnfHvr_R_3JybgfReklRoaWQ9pGmI6oXBocQZiy0te3Rpl7C8VIhx1Es_-JgWjxDGZphHoZL1A-f87lSXXyIhVhmKrIqiGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🤩
🤩
خداییش یکی از بهترین داربی‌های چند وقت اخیر بود
✔️
داربی چهارشنبه‌شب نقش جهان، برخلاف پیش‌بینی‌های اولیه/ اطمینان وریا در مقایسه با سیدجلال، موقعیت‌های استقلال بیشتر بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/139447" target="_blank">📅 21:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139446">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6faf16beef.mp4?token=cGykWqWvUqWpvkChgl1EZ8AjJ7rcwm1bt9Bs25kXVPejER18oIC2v4OG50QM3Rdb96nhLxKra1VoiD_AWiugc08JGp2XRYgDckc4pzwBMiwcAJEuabu7tMhR1m7aeaYvCZ91Gv0rFqbymOODdhyhgCNdjGfFNTSWys31U6cWCNCIbb1F1Uw5qlnz0fedZcKklIF7JhAnYs7YYg4wP0aKKw_-_Adp0ldcALYTFNJJVdv5B6Plv1_usjP6PDzqZDyQmDDL_LhdkNPYTVt4rAW0wcSJ-qO3vwXjCftZCNarKIjmVVcl6T0OWra2EKi8hOiK9pGsEhOrCOOTAydLVIG5hTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6faf16beef.mp4?token=cGykWqWvUqWpvkChgl1EZ8AjJ7rcwm1bt9Bs25kXVPejER18oIC2v4OG50QM3Rdb96nhLxKra1VoiD_AWiugc08JGp2XRYgDckc4pzwBMiwcAJEuabu7tMhR1m7aeaYvCZ91Gv0rFqbymOODdhyhgCNdjGfFNTSWys31U6cWCNCIbb1F1Uw5qlnz0fedZcKklIF7JhAnYs7YYg4wP0aKKw_-_Adp0ldcALYTFNJJVdv5B6Plv1_usjP6PDzqZDyQmDDL_LhdkNPYTVt4rAW0wcSJ-qO3vwXjCftZCNarKIjmVVcl6T0OWra2EKi8hOiK9pGsEhOrCOOTAydLVIG5hTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
تشکر بازیکنان پرسپولیس و استقلال از هواداران‌شان پس‌از پایان داربی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/139446" target="_blank">📅 21:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139445">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🔱 Hero 🔱</strong></div>
<div class="tg-text">سر لجبازی ایشون سهمیه های فصل بعد ما هم به باد میره،نه با گرا فسخ کردن ،نه به ارونوف بازی میده نه باکیچ،هر کارشناسی هم حرف میزنه میگه ارونوف فاصله داره با ورژن خوب خودش،سوال من اینجاس ارونوف دقیقه ی ۸۰ به بعد اومده تو بازی چیکار بکنه تو کمتر از ده دقیقه؟؟؟ اونم دربی</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139445" target="_blank">📅 21:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139444">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">⬇
👤
آقای تارتار بازنگری بکن وسط زمین وله، چرا از باکیچ و لطیفی فر استفاده نمیکنی ؟! لطیفی فر هم بازیکن مستعدی هست هم قامت بلندی داره،مسئلت با خارجی هارو کی میخای تموم بکنی ؟ به چه قیمتی میخای اورنوف و باکیچ بازی ندی؟دقیقه ۷۵-۸۰ برای بازی دادن بازیکن جوان و تلنته…</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139444" target="_blank">📅 21:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139443">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrpnr1m6RV3ytH8SeDGmKt9CsluGbyvTWOuzcxpDAe4U2lQZkdcpIBIi4AmhMLJJPp7FGvdb0rLIW2mXFp_H89ZW7xkj_WyQBbO_OpjBe-YtFtdljeW6mJ-jSef94nPtZzPsHSCmYVwTmttNMId0f6C5zsanXi1j2UN6kmPOnFLZn2ml-eymQMz6dG5lp-fJzbEdjP7ppo72VZIAoosoi2uqmRRXPJqpWdUC2CirYfx42S_oQfcbNjaEMCrhkRYRglxNL-C1GzQsqSxu8uAH2LvDQ3mQwGGymgAl6P8PHiNvvKLQiJuWDC4av5N212Q6A1N-Kx8pkwRhJhmcRqmsxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
♨️
🗞
|
#فوووری
از تسنیم:
🔴
🔵
👤
پرسپولیس بخاطر استفاده از آسانی مستقیم به فیفا شکایت می‌خواد بکنه نه کمیته انضباطی
⚠️
❌
کمیته انضباطی فدراسیون شکایت های گذشته در مورد آسانی رو رد کرده بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/139443" target="_blank">📅 21:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139442">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
هر دو تیم و هر دو سرمربی به مساوی راضی بودن و خوشحال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/139442" target="_blank">📅 21:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139441">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🗣
🟥
بازی خیلی خوبی بود از هر دو تیم ولی بنظرم بعدا حسرت این امتیاز های از دست رفته رو میخوریم، تراکتور تیمی نیست که مثل بازی جلوی شمس آذر به راحتی مساوی بده و باید قدر این موقعیت هارو بدونیم، بنظرم راحت میتونستیم ببریم اگر تعویض ها زودتر انجام میشد و باز هم…</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139441" target="_blank">📅 21:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139440">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🗣
🟥
بازی خیلی خوبی بود از هر دو تیم ولی بنظرم بعدا حسرت این امتیاز های از دست رفته رو میخوریم، تراکتور تیمی نیست که مثل بازی جلوی شمس آذر به راحتی مساوی بده و باید قدر این موقعیت هارو بدونیم، بنظرم راحت میتونستیم ببریم اگر تعویض ها زودتر انجام میشد و باز هم اگر وسط زمین رو داشتیم متاسفانه هم جلوی تراکتور هم استقلال وسط رو دادیم و همین باعث میشه دقایق حساس فشار سنگین بیاد روی تیم و بعدش با کوچک ترین اشتباهی باعث میشه گل بخوریم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/139440" target="_blank">📅 21:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139439">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🚩سرخ تایمز🚩</strong></div>
<div class="tg-text">📌
وسط وله…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/139439" target="_blank">📅 21:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139438">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🚩سرخ تایمز🚩</strong></div>
<div class="tg-text">📌
وسط وله…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/139438" target="_blank">📅 21:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139437">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🚩سرخ تایمز🚩</strong></div>
<div class="tg-text">🔵
دربی تهران در نقش‌جهان اصفهان!
پرسپولیس
🔴
و
🔵
استقلال؛ در دیداری حساس و هیجانی از دقایقی دیگر در لیگ خلیج‌فارس ایران به مصاف یکدیگر می‌روند.
🔗
برای پیش‌بینی این دیدار حساس همین حالا وارد سایت معتبر اسپورت‌نود بشید و با بالاترین ضرایب پیش‌بینی کنید:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
مینی‌اپ رسمی اسپورت نود:
👇
🔵
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/SorkhTimes/139437" target="_blank">📅 21:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139436">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✔️
✔️
✔️
بی انصافیه اگه از عملکرد خوب مهدی تیکدری نگیم!
✔️
برای اولین بار تو عمرش اومد پست غیر تخصصی دفاع چپ بازی کرد و هم در دفاع و هم در حمله موثر و خوب بود
✔️
✔️
پر تلاش و انگیزه از دقیقه اول تا آخرین دقیقه ظاهر شد و امیدوار مون کرد
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/139436" target="_blank">📅 21:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139435">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
ما به اینا نمیبازیم ...نه ساله نباختیم به اینا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/139435" target="_blank">📅 21:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139434">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✔️
✔️
✔️
پایان بازی | شکست ناپذیری پرسپولیس به ۹ سال رسید/دربی جذاب برنده‌نداشت  استقلال
1️⃣
-
1️⃣
پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/139434" target="_blank">📅 21:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139433">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✔️
✔️
✔️
پایان بازی | شکست ناپذیری پرسپولیس به ۹ سال رسید/دربی جذاب برنده‌نداشت  استقلال
1️⃣
-
1️⃣
پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/139433" target="_blank">📅 21:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139432">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✔️
✔️
امروز هر کاری خواستن با مجید عیدی کردن از بس که اون سمت اتوبان بوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/139432" target="_blank">📅 21:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139431">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✖️
✖️
هافبک و کلا استقلال برداشته و خیلی خالی هست هافبک ما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/139431" target="_blank">📅 21:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139430">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✔️
✔️
✔️
هر دو گلر بد خوردن گلارو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/139430" target="_blank">📅 21:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139429">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
❌
گل مساوی و خوردیم متاسفانه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/139429" target="_blank">📅 20:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139428">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❤️
❤️
❤️
ما به اینا نمیبازیم ...گل اول و محبی زد روی پاس بیفوما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/139428" target="_blank">📅 20:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139427">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
🔴
بریم برای نیمه دوم ..الهی به امید توووووو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/139427" target="_blank">📅 20:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139426">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
امیدوارم نیمه دوم شانس با ما یار باشه و کارو تمام کنیم ..شاید ارونوف تعویض طلایی ما باشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/139426" target="_blank">📅 20:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139425">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
نیمه اول دو تیم خوب بازی کردن و بازی زیبایی و دیدیم از سمت هر دو تیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/139425" target="_blank">📅 20:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139424">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
نیمه اول دربی بدون گل تموم شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/139424" target="_blank">📅 20:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139423">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
بدون شک بهترین بازیکن نیمه اول .تیکدری و زارع بودن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/139423" target="_blank">📅 20:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139422">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✔️
✔️
✔️
پرسپولیس خوشگل کیسه رو کرده تو قوطی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/139422" target="_blank">📅 20:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139421">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‌
❌
❌
پرسپولیس بهتر و سرتر و سرحال تر داره بازی می‌کنه و سوار بازی هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/139421" target="_blank">📅 20:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139420">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❤️
❤️
بریم برای بازی ..الهی به امید ...خدایا امشب و پرسپولیسی باش ..حس خوب و انرژی مثبت و بفرستید برای بچه ها ..انشالله برنده بازی ماییم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/139420" target="_blank">📅 19:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139419">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✔️
✔️
همه چیز آماده دربی پایتخت؛
✔️
✔️
هم اکنون ورزشگاه نقش جهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/139419" target="_blank">📅 19:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139418">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/105ef18474.mp4?token=KpEMeN8HQ0LLByOhZbC3RMMknbR6PLMnwj5aGMMK-OuNj9pC2tQ2PM5RGzLt-vU4iC7M__Xo-S7-fcUXllBly_yRZ6zYCJUJzSfE4OwGNp8O7dn-t60KIu0ul42kSgShgqrlSJ6o9PrQ3vp_JkKnpQr3l60-RFrC6qfNDST3U4ITwGklvJ40Jthm_l2S8OcwI4EE7V5PX_11VKMBoXE_Gl0KFM_T1yRDX1pHdSjvGh1XOy1R9Ogc1ddmIvh90sUw0WChPkOjGFs_L9IfmE_2OUSMrDxMup7nZmOEpsmPRwGKeBXDIOsw-Ig0_QCaqcY5bYRgmvW4GbYW4ySpDDSEAx6Do0vPJ9A9ipT7WpU_tFybroS9GY6Zv3K6GkM2qU4Nbb1_Gq5QlZbI08qOel40Gre2-yf11lVlAaucOK1Ge3MJxDFAJXUIyXmGGFANAY3WgGn-E2Zs_yy6q-ethMhXSc4aYS9u3Uf9XuVXub5ALlmr0RiASXm6NA3JwqNxhXlya8s4cnIZf1apRkWdNzp72UmdepCOzffBmfu6j8i_SHDX5KPrt05gdyNEmlf0UhlvSDuhloSfFA2VY6g5WqGDj_OI9Vfmdmv9dG0z5wu_RdFmToDFuTGn0OgotK5QhjjBBQqsZLPv2zsO_BMbUcB_baRhSqe6SoaLzE38xewP3Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/105ef18474.mp4?token=KpEMeN8HQ0LLByOhZbC3RMMknbR6PLMnwj5aGMMK-OuNj9pC2tQ2PM5RGzLt-vU4iC7M__Xo-S7-fcUXllBly_yRZ6zYCJUJzSfE4OwGNp8O7dn-t60KIu0ul42kSgShgqrlSJ6o9PrQ3vp_JkKnpQr3l60-RFrC6qfNDST3U4ITwGklvJ40Jthm_l2S8OcwI4EE7V5PX_11VKMBoXE_Gl0KFM_T1yRDX1pHdSjvGh1XOy1R9Ogc1ddmIvh90sUw0WChPkOjGFs_L9IfmE_2OUSMrDxMup7nZmOEpsmPRwGKeBXDIOsw-Ig0_QCaqcY5bYRgmvW4GbYW4ySpDDSEAx6Do0vPJ9A9ipT7WpU_tFybroS9GY6Zv3K6GkM2qU4Nbb1_Gq5QlZbI08qOel40Gre2-yf11lVlAaucOK1Ge3MJxDFAJXUIyXmGGFANAY3WgGn-E2Zs_yy6q-ethMhXSc4aYS9u3Uf9XuVXub5ALlmr0RiASXm6NA3JwqNxhXlya8s4cnIZf1apRkWdNzp72UmdepCOzffBmfu6j8i_SHDX5KPrt05gdyNEmlf0UhlvSDuhloSfFA2VY6g5WqGDj_OI9Vfmdmv9dG0z5wu_RdFmToDFuTGn0OgotK5QhjjBBQqsZLPv2zsO_BMbUcB_baRhSqe6SoaLzE38xewP3Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
همه چیز آماده دربی پایتخت؛
✔️
✔️
هم اکنون ورزشگاه نقش جهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/139418" target="_blank">📅 19:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139417">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
بازدید بازیکنان پرسپولیس از ورزشگاه در میان تشویق هواداران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/139417" target="_blank">📅 19:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139416">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1244018c05.mp4?token=DgBFKUi_Gtrq9ZoIJslw17GIfx_OHYOcC2zMIzdQAj3LER_snWxCIaPetTcVrlp9ecK5QZrbYkS1W22aW1Z3VDsCPqI9brnP7wNThpOYjR5CP2ST1GjkoCXJ5SbbHK1ii-Ja3lyzPeHEr6aiBvwptuj-Z47CTIqi52l6-O_ODDyWTWBci1yqFLEJ72FfjyaOHI2pZR6q2_ZJ_yIMYbD7fnFuWCyqM9nLOkhG9LCW0yYAlDzNH15PwpmoMPbalKsHq5TkmNPvpvLDwyNu12flyk_2rldllEk2wrS4hLso_8twcWDWf3fy7gR69ahCZfbeicbX6qo8k-lwvHHdkZ5qBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1244018c05.mp4?token=DgBFKUi_Gtrq9ZoIJslw17GIfx_OHYOcC2zMIzdQAj3LER_snWxCIaPetTcVrlp9ecK5QZrbYkS1W22aW1Z3VDsCPqI9brnP7wNThpOYjR5CP2ST1GjkoCXJ5SbbHK1ii-Ja3lyzPeHEr6aiBvwptuj-Z47CTIqi52l6-O_ODDyWTWBci1yqFLEJ72FfjyaOHI2pZR6q2_ZJ_yIMYbD7fnFuWCyqM9nLOkhG9LCW0yYAlDzNH15PwpmoMPbalKsHq5TkmNPvpvLDwyNu12flyk_2rldllEk2wrS4hLso_8twcWDWf3fy7gR69ahCZfbeicbX6qo8k-lwvHHdkZ5qBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بازدید بازیکنان پرسپولیس از ورزشگاه در میان تشویق هواداران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/139416" target="_blank">📅 18:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139415">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❤️
❤️
❤️
ترکیب پرسپولیس برابر استقلال
🇮🇷
پیام نیازمند، مهدی زارع، حسین کنعانی، مهدی تیکدری، مجید عیدی، پویا پورعلی، محمد خدابنده‌لو، محمدمهدی محبی، تیوی بیفوما، ایگور سرگیف و علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/139415" target="_blank">📅 18:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139414">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❤️
❤️
❤️
ترکیب پرسپولیس برابر استقلال
🇮🇷
پیام نیازمند، مهدی زارع، حسین کنعانی، مهدی تیکدری، مجید عیدی، پویا پورعلی، محمد خدابنده‌لو، محمدمهدی محبی، تیوی بیفوما، ایگور سرگیف و علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/139414" target="_blank">📅 18:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139413">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❤️
❤️
❤️
ترکیب پرسپولیس برابر استقلال
🇮🇷
پیام نیازمند، مهدی زارع، حسین کنعانی، مهدی تیکدری، مجید عیدی، پویا پورعلی، محمد خدابنده‌لو، محمدمهدی محبی، تیوی بیفوما، ایگور سرگیف و علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/139413" target="_blank">📅 18:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139412">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔵
دربی تهران در نقش‌جهان اصفهان!
پرسپولیس
🔴
و
🔵
استقلال؛ در دیداری حساس و هیجانی از دقایقی دیگر در لیگ خلیج‌فارس ایران به مصاف یکدیگر می‌روند.
🔗
برای پیش‌بینی این دیدار حساس همین حالا وارد سایت معتبر اسپورت‌نود بشید و با بالاترین ضرایب پیش‌بینی کنید:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
مینی‌اپ رسمی اسپورت نود:
👇
🔵
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/139412" target="_blank">📅 18:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139411">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">⚽
⚽
اندازه گیری چمن ورزشگاه نقش جهان توسط نوشه ور  مدیر برگزاری مسابقه دربی 107
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/139411" target="_blank">📅 17:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139410">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44157a322f.mp4?token=eCS9WnvrjsyvPStOUO_Bcu2o6jVLy_or-lBv2lvleJXzywFEWEAHJ-a3B2Bz0DWVcIwCQdYnN-BriILzGtpzCpPQL7J7wLymDoNf5oCt3uk4_6QR0lv-e7m9z92YN9GjIVwklrWS0-2ImcS1dJA8HSvvCWokfNIZLgJdwRlEmL5q7-zTKSG7eUysFe_f6xWZF5WghnOp1TMkB9d6lVqMbAOES6eJ23orLPJvRi3sT_bRA2WBFD0CyaMEz-HbqRpclV7WFqxMsnG7zSu_xaDUbdZkTlolLbM_NVPR1a7gwPtljE_gzs0B_cX2Tk8KouUaQT1shuEP7MFqwKmNccFmpKtwtjHN_OE_2hriAEexrdO2culPcAbDxZ8nXgSKeD2snEvdhCgpUWzcWK4209xk43tNL2MJT3ALZuKIGrtdqrf-HEw4AhsvrTMyyRlTGV6N6qMTA47YS9-H_vK3mscS6inFFehZkWlSbYPQqtNzPT4Op57zSTpP8S98EjyIRKgYH8jvcr0QE6V8-DAijP5N85d-VqKXBjJsl24c1U5oArI0ZcskqdMX61NxeKNLU8TfQ7ArNoWmOPw5IMilGok1_QQ6gKrBO9sq5nDjjixkOUfmS9wTIFRXwrPlFFrHkpHJ4k_447xfBPjkL5EPYXkhdEHjauYn2OuSy5PU3ohsbsM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44157a322f.mp4?token=eCS9WnvrjsyvPStOUO_Bcu2o6jVLy_or-lBv2lvleJXzywFEWEAHJ-a3B2Bz0DWVcIwCQdYnN-BriILzGtpzCpPQL7J7wLymDoNf5oCt3uk4_6QR0lv-e7m9z92YN9GjIVwklrWS0-2ImcS1dJA8HSvvCWokfNIZLgJdwRlEmL5q7-zTKSG7eUysFe_f6xWZF5WghnOp1TMkB9d6lVqMbAOES6eJ23orLPJvRi3sT_bRA2WBFD0CyaMEz-HbqRpclV7WFqxMsnG7zSu_xaDUbdZkTlolLbM_NVPR1a7gwPtljE_gzs0B_cX2Tk8KouUaQT1shuEP7MFqwKmNccFmpKtwtjHN_OE_2hriAEexrdO2culPcAbDxZ8nXgSKeD2snEvdhCgpUWzcWK4209xk43tNL2MJT3ALZuKIGrtdqrf-HEw4AhsvrTMyyRlTGV6N6qMTA47YS9-H_vK3mscS6inFFehZkWlSbYPQqtNzPT4Op57zSTpP8S98EjyIRKgYH8jvcr0QE6V8-DAijP5N85d-VqKXBjJsl24c1U5oArI0ZcskqdMX61NxeKNLU8TfQ7ArNoWmOPw5IMilGok1_QQ6gKrBO9sq5nDjjixkOUfmS9wTIFRXwrPlFFrHkpHJ4k_447xfBPjkL5EPYXkhdEHjauYn2OuSy5PU3ohsbsM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎦
مصاحبه با مادر و دختر پرسپولیسی
✅
پرسپولیس امرور برنده دربی خواهد بود؛ شک نکنید.۲-٠ استقلال را می‌بریم؛ علیپور و بیفوما گلزنی خواهند کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/139410" target="_blank">📅 17:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139409">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5be238bd7.mp4?token=EMv25T9QAl6x48hWvbh5ovepbkWWsODFpfqq4TnT1ZwIWBuOCIWV83L1PrO1o7iGgf3XzlNf1an10rGZhw0mfc62AGb44LdFNAXUnPJiiey8gtJ8HbU8hpdo__2B-RpOVHCx3SsK50GoPiCkTatz2zy3tJLzuRkZ1lm6efqOH4Br9VKHzutFFKJ445JCC9AfykrZfQ3Vqvp_65LpI9_dk_sKFHqxPICQt8lI-FojrpIeWLsBT7lkXymGFaOO_k0UqWIJSY1bc7vXmqIPfNwXjHr0i5fZLZVA2byiId_8LRvdHZcCExaW-J75xGhjYAS1hIM0Ft48ttSwmOKrBZN2dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5be238bd7.mp4?token=EMv25T9QAl6x48hWvbh5ovepbkWWsODFpfqq4TnT1ZwIWBuOCIWV83L1PrO1o7iGgf3XzlNf1an10rGZhw0mfc62AGb44LdFNAXUnPJiiey8gtJ8HbU8hpdo__2B-RpOVHCx3SsK50GoPiCkTatz2zy3tJLzuRkZ1lm6efqOH4Br9VKHzutFFKJ445JCC9AfykrZfQ3Vqvp_65LpI9_dk_sKFHqxPICQt8lI-FojrpIeWLsBT7lkXymGFaOO_k0UqWIJSY1bc7vXmqIPfNwXjHr0i5fZLZVA2byiId_8LRvdHZcCExaW-J75xGhjYAS1hIM0Ft48ttSwmOKrBZN2dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔵
ترافیک سنگین در مسیر ورودی به سمت ورزشگاه نقش جهان اصفهان در آستانه  شروع دربی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/139409" target="_blank">📅 16:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139408">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7a4db0aec.mp4?token=e0n_ioz6-TE6qBx2s0Yeejrm8orYKLnMgIQJKcglPeL16MHUbBuW6IiHyqociwsk9PrT9fiQM1g_Iqr-YH8d2a5ceM_-D3zBgyUejPBOrJ7nWi4yuOGrt7lfhCSVUqzuf1M_h1cD8D5nXJyserrnPVAVVubADeMHOwg6xrndXJGyK7vVAfgGVh2fp6XOHpBONgR1N-Iw8AU-bMhCi_mVUB-mCe1cGJ9EfRyd1w0CDbAlLUY5ZRM6_OpBe32IB0oOMUVsjexpCr11swKx8OFY4Qg27b6sLAZZMvPv3oCtxlRa0zVSAA7MxjC31zyqLeVVwqiQDwt3ojUTetaHtVvCpTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7a4db0aec.mp4?token=e0n_ioz6-TE6qBx2s0Yeejrm8orYKLnMgIQJKcglPeL16MHUbBuW6IiHyqociwsk9PrT9fiQM1g_Iqr-YH8d2a5ceM_-D3zBgyUejPBOrJ7nWi4yuOGrt7lfhCSVUqzuf1M_h1cD8D5nXJyserrnPVAVVubADeMHOwg6xrndXJGyK7vVAfgGVh2fp6XOHpBONgR1N-Iw8AU-bMhCi_mVUB-mCe1cGJ9EfRyd1w0CDbAlLUY5ZRM6_OpBe32IB0oOMUVsjexpCr11swKx8OFY4Qg27b6sLAZZMvPv3oCtxlRa0zVSAA7MxjC31zyqLeVVwqiQDwt3ojUTetaHtVvCpTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔵
هواداران استقلال و پرسپولیس در مسیر ورود به ورزشگاه نقش‌جهان اصفهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/139408" target="_blank">📅 16:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139407">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/282676305a.mp4?token=o4TeiY4fAyj-4mDBWfc7OiuRZtvjXjQIIoaRFWbYbtVtqHQXPjbEHXyA9mReQPCgqlNUKe_1h4oBqE6XCWr46-pJsFeQfy276jwoA6jptC-fOJjoDP6hY1SLlwc3H3ETzbpy9FXPnH4ZUGzcdpNeZWzT1GY72dlQCKbsGjg66ANWZCMtkRILwQ9QxQxbhWZPwyJ_bMwwU1cQS3NiXPCCOBSlXdZqFO8nOSEzpeuUbuE-jniU-byLl0ZaQhXtltV7IgXaGIwqoPIMGPhtgHIrumnZRwRCO-mlPg199WDJmHhl7Q7F14gdGGmPaB1TjPsHf8ODbf0pcyK1djWrQNA9yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/282676305a.mp4?token=o4TeiY4fAyj-4mDBWfc7OiuRZtvjXjQIIoaRFWbYbtVtqHQXPjbEHXyA9mReQPCgqlNUKe_1h4oBqE6XCWr46-pJsFeQfy276jwoA6jptC-fOJjoDP6hY1SLlwc3H3ETzbpy9FXPnH4ZUGzcdpNeZWzT1GY72dlQCKbsGjg66ANWZCMtkRILwQ9QxQxbhWZPwyJ_bMwwU1cQS3NiXPCCOBSlXdZqFO8nOSEzpeuUbuE-jniU-byLl0ZaQhXtltV7IgXaGIwqoPIMGPhtgHIrumnZRwRCO-mlPg199WDJmHhl7Q7F14gdGGmPaB1TjPsHf8ODbf0pcyK1djWrQNA9yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حضور دو جیمی جامپ پرسپولیسی و انجام خوشحالی رونالدویی
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/139407" target="_blank">📅 16:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139406">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7410fd3106.mp4?token=Owb9skGkDSeQyblQgThyEdHmUgGgklK_Ymgu3QqkkV3YEJahTE4XmbXcA-fhlcwdRMSbxZaCc9InqTW48n8zlNRHs7_Hf2UlAlQdTATOfJGVKiQxgatx4UybmvNMgMnVV0y_ZX31DTs7Uc5EZ7KMrZ4TKJcsulcbv_FeLAHsE4rWqv6-ULLe8hKPSgsouP7uAu8iiLlVff6jU6Rs8RulVqylBumJ1YP456bjQ8Npe8BUK1wYk_GLU1Tmh6jthS_2ZJ0T90rm0uHz1dsXerYqP7AbcAQ550EzHJDsdqZaHQ9KEIZR5bvYVcU9yTI8plpIVgyKrhgntN57qfHBtK-oRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7410fd3106.mp4?token=Owb9skGkDSeQyblQgThyEdHmUgGgklK_Ymgu3QqkkV3YEJahTE4XmbXcA-fhlcwdRMSbxZaCc9InqTW48n8zlNRHs7_Hf2UlAlQdTATOfJGVKiQxgatx4UybmvNMgMnVV0y_ZX31DTs7Uc5EZ7KMrZ4TKJcsulcbv_FeLAHsE4rWqv6-ULLe8hKPSgsouP7uAu8iiLlVff6jU6Rs8RulVqylBumJ1YP456bjQ8Npe8BUK1wYk_GLU1Tmh6jthS_2ZJ0T90rm0uHz1dsXerYqP7AbcAQ550EzHJDsdqZaHQ9KEIZR5bvYVcU9yTI8plpIVgyKrhgntN57qfHBtK-oRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
⚽
اندازه گیری چمن ورزشگاه نقش جهان توسط نوشه ور  مدیر برگزاری مسابقه دربی 107
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139406" target="_blank">📅 16:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139405">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✔️
✔️
✔️
محسن خلیلی: ابوالفضل جلالی به دربی رسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/139405" target="_blank">📅 15:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139404">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
❌
❌
رسمی؛ ممبینی که صبح از سمت دبیرکلی برکنار شده بود، مشاور مهدی تاج شد.
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/139404" target="_blank">📅 15:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139403">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">⚽
⚽
پوستر جذاب باشگاه پرسپولیس برای دربی
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/139403" target="_blank">📅 15:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139402">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55bf0f119c.mp4?token=EE_sQD3PEG4wB-JBb3P12mD5ht29Sdos1vuBVjZhsHAiVDw9c5FO-blACKiLsHrNUM4sPHzGRKaNhJCdxTHfBL_cJg_m4YXrAnDAA0jyvHOYeE-4WvVJzp_nD6oWEXKFSu2VVooUrWAlJnqUWq2S2GFGC6EiXJrUazWg2pXBxywD7qexRaEmsY7YnY-W2MvUc7rxvwo-jDUogn3nkV1jfkUH9kEXms49-xd9wZgflhBYPV_Joy-RIj32w4d3dE-OsAe_EUJrs6JOMpJIauk1YWGgoDTk_zI-Ig2ojsaGz28wqoMo0VfhdT548DC6uZcneEqv0jzw5tnYxW6CnsvC5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55bf0f119c.mp4?token=EE_sQD3PEG4wB-JBb3P12mD5ht29Sdos1vuBVjZhsHAiVDw9c5FO-blACKiLsHrNUM4sPHzGRKaNhJCdxTHfBL_cJg_m4YXrAnDAA0jyvHOYeE-4WvVJzp_nD6oWEXKFSu2VVooUrWAlJnqUWq2S2GFGC6EiXJrUazWg2pXBxywD7qexRaEmsY7YnY-W2MvUc7rxvwo-jDUogn3nkV1jfkUH9kEXms49-xd9wZgflhBYPV_Joy-RIj32w4d3dE-OsAe_EUJrs6JOMpJIauk1YWGgoDTk_zI-Ig2ojsaGz28wqoMo0VfhdT548DC6uZcneEqv0jzw5tnYxW6CnsvC5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ورزشگاه نقش‌جهان ساعاتی مانده به شروع دربی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/139402" target="_blank">📅 14:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139401">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✔️
✔️
✔️
محسن خلیلی: ابوالفضل جلالی به دربی رسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/139401" target="_blank">📅 14:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139400">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✔️
✔️
با اعلام استاندار اصفهان دربی تهران در ساعت 19:30 در استادیوم نقش جهان اصفهان با حضور تماشاگران برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139400" target="_blank">📅 13:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139399">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
🔴
🔴
مروری بر بهترین گلهای پرسپولیس در دربی‌های لیگ برتری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/139399" target="_blank">📅 13:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139398">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rj2H4-BZW3ouPle0LQymjRCFdb3tu9SHKQrwoxnucXajshpZ0Iq1vM_PwbxkjocasInHE1GqD1r8jESiXoIsXgm7XwbW18aCjrr5lKhRfiEvSr784jENqdvdD5mr23PfFwoYHtTQ1pQY9Apv6nCo29at1KNrgPwBitBjg5EZ4LR1sv13Ahx4C4bqhau_YiAEadD8U0mXm6SBiJ-6_Ge5cTGJD3wHRzh3bN0rnAsiETMfEZHuNIscPHRZs7BqSt3MPtKLJEXKzSV7OTr1qn0jKlvEq7WorBdJovDHgHsihD5Lk3Qsd-KZ45K_WRriz-_Ahuk52xoe0SED6rng3_jIqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
اصفهان در آستانه یک نبرد بزرگ!
⚽️
پرسپولیس و استقلال؛ دربی پایتخت در حساس‌ترین جدال فصل برای شبِ فراموش نشدنی.
[
استقلال
🔵
🆚
🔴
پرسپولیس
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/139398" target="_blank">📅 12:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139397">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
نتایج 19 دربی اخیر پرسپولیس و کیسه:
📊
در 19 دربی اخیر دو تیم 8 برد سهم پرسپولیس و 11 مساوی سهم دو تیم بوده، و نکته اینکه کیسه بردی نداشته
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139397" target="_blank">📅 11:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139396">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">⚽
⚽
پوستر جذاب باشگاه پرسپولیس برای دربی
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139396" target="_blank">📅 11:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139395">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bcd6b3f28.mp4?token=iBFUkzR8oYucmOAxVmOShOyDY1h6mOdY6Rl8vHfkA2KDEX3_z5VvrGyTf8cPTH_jDgqH99KTixTreIZ8alCjrUhiHx8o54qACK3Z88c7HwAMDRuLe2UMqtVOublAtIl1EV79DgXqP9G-sqHZ9YQbjxMJrQCvLJYb4S1xzwUfYnDmnMtTTFaTVljADFizPmVeJu9xzXLEv1BQn76BhCpX5OozljBEitZJwrZ24J1Y0jiaCpLsYnR3dYhtQPt9R4TZ0npmUPX76rjh2OXNWO_cOH70-xLqa4m7e7X7LBRASMBSDOBXQ5mIkQsu8Ta4fQWmaCgIHZsesO3t-YSCmsbgtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bcd6b3f28.mp4?token=iBFUkzR8oYucmOAxVmOShOyDY1h6mOdY6Rl8vHfkA2KDEX3_z5VvrGyTf8cPTH_jDgqH99KTixTreIZ8alCjrUhiHx8o54qACK3Z88c7HwAMDRuLe2UMqtVOublAtIl1EV79DgXqP9G-sqHZ9YQbjxMJrQCvLJYb4S1xzwUfYnDmnMtTTFaTVljADFizPmVeJu9xzXLEv1BQn76BhCpX5OozljBEitZJwrZ24J1Y0jiaCpLsYnR3dYhtQPt9R4TZ0npmUPX76rjh2OXNWO_cOH70-xLqa4m7e7X7LBRASMBSDOBXQ5mIkQsu8Ta4fQWmaCgIHZsesO3t-YSCmsbgtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
بهمنی، سخنگوی سازمان لیگ: 6 هزار بانوی هوادار تماشاگر دربی 107 خواهند بود/ درهای استادیوم نقش جهان ساعت 12 باز می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139395" target="_blank">📅 10:56 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139394">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/566218d82d.mp4?token=f9kmXw2RaoMRRtSvzm5QQ6APakGpn2w_alFTA6QQvtuz9P5JRMABH0P1BG89EaoTTzlqRNsqxfTcpkd9oy3Gy5bXq0SJIi-kWI3ZMQl0uqKNt9jPRgEIOpfc5MNX42B-_JCygvFfwsKENJ7Acw5ckH8Ik4R1tin5KoVy40pMyy76HCjqGRG8Lv3F-2pF7OMWIMOay3A0DJZVdDKcge8dsCj3012OIHLwXveotsVI04FuxVL0flEw-ekgUqq9xOnHhXfH0TfoEiCrBZ-RprqzoxV-6oceS2z88gJ6_TM1zFF6qk7AlJq4q-_Ho4c0UBdk4fgA3Z9JCUncm7x1nEvhqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/566218d82d.mp4?token=f9kmXw2RaoMRRtSvzm5QQ6APakGpn2w_alFTA6QQvtuz9P5JRMABH0P1BG89EaoTTzlqRNsqxfTcpkd9oy3Gy5bXq0SJIi-kWI3ZMQl0uqKNt9jPRgEIOpfc5MNX42B-_JCygvFfwsKENJ7Acw5ckH8Ik4R1tin5KoVy40pMyy76HCjqGRG8Lv3F-2pF7OMWIMOay3A0DJZVdDKcge8dsCj3012OIHLwXveotsVI04FuxVL0flEw-ekgUqq9xOnHhXfH0TfoEiCrBZ-RprqzoxV-6oceS2z88gJ6_TM1zFF6qk7AlJq4q-_Ho4c0UBdk4fgA3Z9JCUncm7x1nEvhqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
فیلمی وحشتناک از حمله دیشب به سیریک
🗣
بیچاره مردمان این منطقه
🖤
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/139394" target="_blank">📅 10:56 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139393">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvdrzR2bM4GDF14Pyfu2VnQzjZvincE3l8vnpjP6lmPThYX7-N32lf8hRxHQcxPW9xweMVicO5m0Uu0u1zgMgiMycSGUF6Ad4glLsmmDAsL15hRnePYiCqGn2-x5V3X6PRDVq5aIg1ZysGoB5RtCv3apcN2EbheK2uYVlPsqQLuPfFBAhzPIOnbt4viQ9Ztt-o_Y2G2byTHqXU8UjkjTjB6EIp3qL48LyEQwKJMBsMhS5w1lD3tMko2Nhgl3uptgefzw66Jm943aGZAcEYkNwIgzEV3m2yMQb2zVryySG3ryKx6nE4ZWe5Ko418LKygrwGDPPWubC8veGu8qHDMRog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
⚽
پوستر جذاب باشگاه پرسپولیس برای دربی
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139393" target="_blank">📅 10:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139392">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✔️
✔️
برای کمک به تیم ملی امید  هفته هفتم لیگ برتر فوتبال لغو شد!
✔️
ایسنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/139392" target="_blank">📅 10:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139391">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcEoPnH_gtYUZWWjpXqAnopUkzuY01tgVFr1T-vcEeThedyQR4Wt7f-U8gS5xs7uKyAzgBbiuU7yX6wQ5lvXboHaeVqiofOsYxShMt7DLVSsRBF_cBJJ7HuHytgQRwmch16JfbH8gwVaWnqzTgCDIl_g5kGcuKS7TybmJlV223Hah_H38YAZVASxOrjqrSgGANwMgU_eldlplsMMDwlaxw0iOXSRQdyGxuawhPBbCfRNVadO8SDqGlKTLQ2DA-YV47OWlUtjsW20jjcPVCkQ9NOBw3v8Xu7obHeQ3l5tWmlYpRPtybK7NCO_shhPzd6gJzxZJcNIQwQisyoiPsasXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
⚽️
تسنیم: شایعات الکی و بی مورد نسازید، دربی با حضور تماشاگران و بدون هیچ تغییری در استادیوم نقش‌جهان امروز برگزار خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/139391" target="_blank">📅 09:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139389">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CX4XCcoi4VdWve5YgRRAuP2UHEHlQjbtwNOHHBV5GUGOpmHMltF4YyLLeRsE91XvoojqBv_RdSDbRsL2bSIOYqzgi8zq2zT9GCJmeTBbYubruU_ngmtD8gld5UIjfEEiXz4rjYH2SiQlpOuNV1R5kVspUnyNwsG2O2AtmehYxVNcMeSr2hGyl-9DwYr3uWEID3gjbPp_96wv2PtPyNFs56khuHHILxv7BN0aRFMq6A9hadWV08zdlTeLO6j7hWL7CWC619nyhHsZ_3e26zaG2T2R5Ws-G-KH5Qk7eW0L-T6xrsKv4kKICpsGiCnXBKTLxi1Tz9kv1GpQPZkLC1GOWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
با اعلام استاندار اصفهان دربی تهران در ساعت 19:30 در استادیوم نقش جهان اصفهان با حضور تماشاگران برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139389" target="_blank">📅 09:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139388">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❤️
تکذیب شایعه برگزاری بدون تماشاگر دربی استقلال و پرسپولیس در نقش جهان
⚪️
⚪️
استاندار اصفهان شایعات مطرح‌ شده درباره برگزاری بدون تماشاگر این دیدار را تکذیب کرد و گفت: این مسابقه با حضور تماشاگران و طبق روال پیش‌بینی‌ شده برگزار می‌شود./ مهر
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/139388" target="_blank">📅 09:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139387">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✔️
خبرهای رسیده از فدراسیون فوتبال حاکی از اینه که احتمال لغو یا برگزاری بدون تماشاگر دیدارهای فردا لیگ برتر، از جمله دربی وجود دارد
❌
❌
تصمیم نهایی به‌زودی اعلام خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/139387" target="_blank">📅 09:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139386">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇷
🇮🇷
صبح روز دربی و پر از استرس بخیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/139386" target="_blank">📅 09:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139385">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZM_N7ztxYUU1dujAKkwQU1xhD9TtzHOAHIHtGXDRu6OhO70VXiRiRiPVETYnps7fkNyXAG1SybC-XeZXmFfPB0uf2Elynosn6wkfJKRCi-CnkUn95YXR0EY8Gyvc1pLGRgiRXrD5DUkOttufcIirkaxSLUjhABtTxBDqJfl67UwVq1Aw3JOVm__wHYW1WV49iRX0s3HZNaFPx4kL4kMlfq6sBXg6P_fK0saQstumK0RVYwwfd8WZ2oz_RuyLdIod0RL9WRTSscO5ytqFCUOYYh1Uhg0dudnqeddCpCixm-tIh9hFito666qxUyGEcFUPupQKYJs6dTJXy5gcA2ZQbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
دوئل‌های جذاب در یو‌اس اوپن!
🎾
الکساندر زورف
🆚
لورنزو سونگو
🎾
آندره‌آ گِریِری
🆚
الکس د مینور
🟡
کدوم ستاره‌ها از این نبردهای حساس سربلند بیرون میان؟
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی دیدارهای یواس اوپن همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/139385" target="_blank">📅 01:22 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

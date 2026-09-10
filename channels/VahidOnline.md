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
<img src="https://cdn1.telesco.pe/file/caByYYjX8QXRQyeERv_CIvEF4Bzs9vlZdb4Qtyp6LGi7A6yC9qhISzV4BkgvRREbP8X_WGtZiNwqECGaJ2NPXFoLuGOcNaKg0RxOg6wjDktbGrVwg9S6I-bF2g5qxcXPWkxeSu51gA3CfR2k4pegAikg2HmjEbOIJe0UKUWtf23t_n7wx1v1Tbnqhyam6RJA5y7Rue7PKE4QJor_Mecr2qNxh81XWMxP9EFiEZ-lUZb4u3uJtXtsXfYxbDjXNyrpvl3gohYxT6GgRf0tYJ0IDeDtJwjnV2JLwQb2e98ZvSP7SagtFL9ml-VCfGvw2WvPUAAeYRAXn9mxrhEgcuZvTw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.41M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 04:45:16</div>
<hr>

<div class="tg-post" id="msg-78305">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پیام‌های دریافتی:
سلام الان ساعت ۰۰:۲۵ قشم صدای انفجار اومد
قشم صدای انفجار اومد
وحید قشم بد زدن تمام خونه لرزید
#قشم
00:24 نوزدهم شهریور
صدای انفجار و لرزش
قشم صدای شدید
شیشه ها لرزید
موج انفجار شدید همین الان قشم 00:25
وحید قشم یه صدایی اومد
شیشه ها لرزید
صدای یک انفجار بندرعباس
وحید جان انفجار شدید ساعت 12:25 قشم
سلام صدای وحشتناک باعث لرزش شیشه خونه شد
سلام قشمو بد زد کل ساختمون لرزید
همین الان نزدیک قشم صدا انفجار اومد.
خونه لرزید.
صدای انفجار به بندرعباس رسید لب ساحل نمیدونم کجا زدن
درود به آقا وحید شبت بخیر ساعت 0:25 انفجار سنگین از سمت دریا نمیدونم قشم بود یا جای دیگه ولی بندرعباس به شدت حس شد
قشم لرزید
موجش قوی بود
شدید بود خیلی
توی دریا بود انگار
سلام داداش وحید .صدای انفجار مهیب در قشم شنیدیم
خیلی مهیب بود ..
۰۰:۲۶ بندرعباس انفجار رخ داد
فقط صدا نبود
در و پنجرها هم تکون خوردن
صداش انقدر جدید بود ما داریم میگردیم میگیم لابد اسانسور ساختمونمون ول شده
🤦‍♀️
صدای انفجار در خونه لرزيد قشم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 177K · <a href="https://t.me/VahidOnline/78305" target="_blank">📅 00:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78304">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/692967643d.mp4?token=YFJ5IBX8i0StbH7dw0DtutKXVZK1G-DuR3sTY2hc8bUoKGVTvNTG9dqaoNfv0qbJQ0qkAcEGscxBMYsx7FshtGrj8S2vDwyeJgJMhtoshevH4wWcC5nQePx-W26Zo1EWaTTL4OPlZbvKO1macpYvsd4HIdirUqFmOUug8LoU7d0n0s9zUMHS8caMSokg4BeQgoxlMpeQCt_i087l-Xd1AaUhpcUTxjiQ08VUED3c6TEl_KAN4knqL_wqLVm7Cvbphlm3HpZ5P5OGYS6FY9FqcZZDpnUlQopHJqASh5BUEFkVd06orh1GdUgamxfrpMD-znqOwaWsGDb_0v0rZIF2Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/692967643d.mp4?token=YFJ5IBX8i0StbH7dw0DtutKXVZK1G-DuR3sTY2hc8bUoKGVTvNTG9dqaoNfv0qbJQ0qkAcEGscxBMYsx7FshtGrj8S2vDwyeJgJMhtoshevH4wWcC5nQePx-W26Zo1EWaTTL4OPlZbvKO1macpYvsd4HIdirUqFmOUug8LoU7d0n0s9zUMHS8caMSokg4BeQgoxlMpeQCt_i087l-Xd1AaUhpcUTxjiQ08VUED3c6TEl_KAN4knqL_wqLVm7Cvbphlm3HpZ5P5OGYS6FY9FqcZZDpnUlQopHJqASh5BUEFkVd06orh1GdUgamxfrpMD-znqOwaWsGDb_0v0rZIF2Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده روز چهارشنبه ۱۸ شهریور گفت که از دید او جنگ با ایران «بلافاصله» بعد از انتخابات میان‌دوره‌ای آمریکا پایان خواهد یافت.
دونالد ترامپ پیش از عزیمت به سمت شهر دالاس برای شرکت در اجلاس حزب جمهوری‌خواه به خبرنگاران گفت: «فکر می‌کنم جنگ بلافاصله بعد از انتخابات تمام خواهد شد. چون آن‌ها (ایران) دیگر نمی‌توانند دوام بیاورند».
ترامپ درباره وضعیت ایران افزود: «آن‌ها مستأصل هستند و تلاش می‌کنند بر انتخابات تأثیر بگذارند».
ترامپ در پاسخ به پرسشی درباره حملات گسترده طرفین در اطراف تنگهٔ هرمز گفت: «حملات توسط ما انجام شد. ما ۹ نفتکش آن‌ها را زدیم. قرار است حملات بیشتری انجام شود».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 233K · <a href="https://t.me/VahidOnline/78304" target="_blank">📅 23:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78303">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/739c863db9.mp4?token=J-yffbEo8F7mZtp8Ok5EciiVIEP84a9UxwEj2aFKROong77DMR2LqtuQGqcl6Ci0elldmPuf3ToqSwkKGhaNMDePSZn8TGjoRa9cSKL2PCjwW7FPhYkeGuyTAmnHRDbePv3S7vYcpD31XUX_eDTm-dk5g45o2GFHdaS_HAo60t2E953xSKR5mj6X2E1OnOn6QNWczkKvlbLRn-GwXbYgeqZdE_5g45-Hmjn5YkF3ox9ctFEW4XBjaEFeodhovCxBwcwNVGuBGA5XOH-zGw99Kvwu9oQqDNTKI8RXiWRC8Xwopz5C9BwYUFgGeuuYs0mwE9y4PM8USQufw_QwVeLvDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/739c863db9.mp4?token=J-yffbEo8F7mZtp8Ok5EciiVIEP84a9UxwEj2aFKROong77DMR2LqtuQGqcl6Ci0elldmPuf3ToqSwkKGhaNMDePSZn8TGjoRa9cSKL2PCjwW7FPhYkeGuyTAmnHRDbePv3S7vYcpD31XUX_eDTm-dk5g45o2GFHdaS_HAo60t2E953xSKR5mj6X2E1OnOn6QNWczkKvlbLRn-GwXbYgeqZdE_5g45-Hmjn5YkF3ox9ctFEW4XBjaEFeodhovCxBwcwNVGuBGA5XOH-zGw99Kvwu9oQqDNTKI8RXiWRC8Xwopz5C9BwYUFgGeuuYs0mwE9y4PM8USQufw_QwVeLvDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غلامعلی حداد عادل می‌گوید حکومت فعلا نمی‌تواند «به علت شرایط جنگ آن‌طور که باید وارد جبهه حجاب» شود.
این عضو شورای عالی انقلاب فرهنگی و مجمع تشخیص مصلحت نظام در ادامه می‌گوید شرایط کنونی کشور از نظر حجاب «بسیار سخت‌تر از سال ۶۰ است که شروع به کار کرده بودیم».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/78303" target="_blank">📅 21:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78302">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AF1MW_zd1y_IacijIrNijclIcgAi3VFEo-3D-vxUJLNVGrWxDP3PjxOWehTaKp-RdArqdURVaHWaC3DPDS4TdCk4A1H30CBpdzuZK_514njRsTZQlDX2UwDy6RJ3Z4uzofYPQ87AXFmKvt4uByn2iFPGy1s2kfcQKBWqJVhewLxV3cWAbVkg7LLMCzNvW16wjF5PidCQ0WSGTfp5-DmR5eG-XCgAfXPSwBFA2UfJUlkqJtjjbP3Oo0KqHjIlLnN18vzFZTapead1EWF18H6LUy140XHYmyQhMbWQ-KmQ932TAA_UdZLZZCrti9R1U5pSUBL5V4l5oZqn-rcmdWWKsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز روز چهارشنبه ۱۸ شهریور به نقل از منابع دیپلماتیک گزارش داد که شورای حکام آژانس بین‌المللی انرژی اتمی با صدور قطعنامه‌ای، پرونده ایران را به دلیل نقض تعهدات منع اشاعه هسته‌ای، پس از ۲۰ سال به شورای امنیت سازمان ملل متحد ارجاع داده است.
این قطعنامه جدید در پی قطعنامه پیشین شورای حکام در ۱۲ ژوئن سال گذشته صادر شد؛ فهرستی از موارد «پایبند نبودن» ایران به تعهداتش که درست یک روز پیش از آغاز حملات هوایی اسرائیل و متعاقبا ایالات متحده به تاسیسات هسته‌ای ایران تصویب شده بود.
بر اساس قوانین و الزامات حقوقی، گزارش رسمی این نقض تعهدات به شورای امنیت سازمان ملل، مستلزم تصویب دومین قطعنامه از سوی این شورای ۳۵ عضوی بود که اکنون به سرانجام رسیده است. این اقدام می‌تواند مسیر را برای بازگشت تحریم‌های بین‌المللی و افزایش فشارهای دیپلماتیک بر تهران هموارتر کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/78302" target="_blank">📅 20:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78301">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bQdR-r8YOXWSR_OCj50nck3ECxyLssK-G9kBsguEGVf-BDHxkxKrTI7bEXhEwZnfvJlGxCCEjXG4eDRiK5wrge_6EyEAl7fqcNGYN22rN0N4ArJ6dDxzjn2uvDqDG8rddZyu03Auv_-woNfXBzBrVimDfzv2XXiL2Ot_s-Y4t-RfB--68ghJAYPToylgPtzKbyn6XBV89t1_mRa45YhZHDHdAt8_nztavGHSqWOnNpqhveOa6sBg3Pt9fxV3h2w86aToTC60y0QDo8xODJv05wXnmt3WnNIJyTksyQVhjZdC2nsoqUUlhG7v71wMSujNqi1hDM0swL-kYNceD8caMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی با شرح: 'شناور آمریکایی در تنگه هرمز، سمت جزیره سلامه خصب عمان، چهارشنبه ۱۸ شهریور'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/78301" target="_blank">📅 19:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78300">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d5c510746f.mp4?token=MCbGeXS2xTPHDWcSRA1stum3UukS571IcxVJ9OMTkS5XlbriPGsNsRhFGGKT8Sn99e4L-nNe9vswd8_K7i7YRBDa8jap7r6R-LfGpEWEcxGknIqEBd8286vZ1ib0hxcsM5pHHbfcdkSIA4EQ52_7DGHu5ANiNoh7J-sRiz4RD8U6qEqhlJcJgDZuBZAdRmnYaTVkYpJB6z763McnqfOWcXuvF7f7GLiOr6tbbYzp0BE5WaR-xiEN5AIn9fb4d1LnsqE5cEoOwBmn4F-cyztzx9I827-wIyjpwR4CJmhjkk07Qk-F6F0QD0ui1plt4cqm-5zE7E-jRVbEiGO1VFR7wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d5c510746f.mp4?token=MCbGeXS2xTPHDWcSRA1stum3UukS571IcxVJ9OMTkS5XlbriPGsNsRhFGGKT8Sn99e4L-nNe9vswd8_K7i7YRBDa8jap7r6R-LfGpEWEcxGknIqEBd8286vZ1ib0hxcsM5pHHbfcdkSIA4EQ52_7DGHu5ANiNoh7J-sRiz4RD8U6qEqhlJcJgDZuBZAdRmnYaTVkYpJB6z763McnqfOWcXuvF7f7GLiOr6tbbYzp0BE5WaR-xiEN5AIn9fb4d1LnsqE5cEoOwBmn4F-cyztzx9I827-wIyjpwR4CJmhjkk07Qk-F6F0QD0ui1plt4cqm-5zE7E-jRVbEiGO1VFR7wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با حضور در قله جبل‌الشیخ (حرمون) و اشاره به تسلط بر مناطق مرزی سوریه و لبنان، هدف اصلی کارزارهای نظامی جاری این کشور در منطقه را شکست و سرنگونی رژیم ایران عنوان کرد.
نتانیاهو در پیامی ویدیویی، به حضور نیروهای نظامی اسرائیل در مناطق مرزی سوریه و لبنان اشاره کرد و گفت: ما اجازه نخواهیم داد هیچ گروه تروریستی در مرزهای ما مستقر شود. این یکی از دستاوردهای عظیم ماست، اما کار اصلی هنوز باقی مانده است.
نخست‌وزیر اسرائیل با ابراز اطمینان از دستیابی به این هدف افزود: کار اصلی ما شکست دادن و تضعیف کامل رژیم ایران است. ما بسیار به این هدف نزدیک هستیم و می‌دانیم که کل این محور سرانجام سقوط خواهد کرد و ما این کار را انجام خواهیم داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/78300" target="_blank">📅 18:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78299">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BozDaWZ5HF_4rC3O-7_Tj9drgBEq6djNvo7ykZEqtU1W5NPDzhqLIAGqk4KUmK0h3Yw5sCY2LrE-dwuBKWxtXVmt9Ye2EE_elvuACqtNPMqSGYEayzEtKxzeVBJvK2hXNcgiqZPzCN_rpI_3ujmB2BDJId9P2B86FZJJbw6eCfDTqSn8GIx4Uv5-qKHRtsvsj2-YEj-gLDp0qLDYchra6VrvH51KrJbjJaHR0lTlbPCliJq8ZRXT6alHiVrO5UfpC30pXMjilpJsAdgpaRHkRmuCwY9kc29jBLx5rvhGpWk8qIfcrSdD4U6_h1huc_1z2ECodlrbmYW1dQwAIAr7Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه پاسداران برای پایان وضعیت کنونی و بازگشایی تنگه هرمز از آمریکا خواست جنگ و تهدیدها را متوقف کند، اسرائیل از لبنان عقب‌نشینی کند، محاصره یمن پایان یابد، ۲۴ میلیارد دلار از دارایی‌های مسدودشده ایران آزاد شود و مداخله در برنامه‌های هسته‌ای و موشکی جمهوری اسلامی متوقف شود.
حسین محبی، سخنگوی سپاه پاسداران، روز چهارشنبه ۱۸ شهریورماه گفت اگر آمریکا خواهان پایان وضعیت کنونی است، باید ضمن «توقف کامل جنگ» از تهدید دوباره دست بکشد.
محبی در بخش دیگری از سخنانش تهدید کرد که در صورت ادامه حملات، پاسخ سپاه گسترده‌تر خواهد بود و گفت: «اگر دشمن دو یا سه هدف ما را بزند، ما با ۲۰ هدف پاسخ محکم می‌دهیم.» او همچنین گفت جنگ کنونی برای نخستین‌بار «آسیب‌های راهبردی» را مستقیما به آمریکا منتقل کرده است.
این اظهارات در حالی مطرح شد که با تداوم محاصره دریایی ایران، صادرات نفت از طریق تنگه هرمز متوقف شده و فشار تحریم‌های مضاعف دولت ترامپ، باعث تورم کم‌سابقه در ایران و رسیدن قیمت دلار به ۲۳۳هزار تومان شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/78299" target="_blank">📅 16:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78298">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNrs6A8DQWeGuse-pjCcnn3yu9XzAvBAeseJPe33p56Cq3avzvxVUzx_HV7rlDvKsl99QMd71yoORz5c9SIsv1qhd7-pjFwQIWePqy_mHhXyUDvykLgmibCTJv5iS1lFS3v93IH0uMtluRohl5URP8KzY77cALkZJbXtejxlE1dbzfapmyqQu8dWqN_a1B_Opf1FdpTMtbJtAIK-IFLwP0zQseOs8qUSGQeteWBsQkoosKkAolxMYzSIESF9VbjKGwNP9xz-B7tNg4HCDSvFVMxizltGqXeS2zOcW0O8K2JMlPJg0pdFJEUF2AP-Wqd9Ls0wKC0krhWe299djLcxGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت ارزهای خارجی در بازار آزاد ایران روز چهارشنبه ۱۸ شهریور ۱۴۰۵ رکورد تازه‌ای ثبت کرد و نرخ دلار آمریکا از ۲۳۲ هزار تومان گذشت.
برخی وب‌سایت‌های اعلام قیمت ارز نرخ دلار را در معاملات ظهر چهارشنبه تا ۲۳۵ هزار و ۵۰۰ تومان نیز گزارش کردند.
هم‌زمان قیمت یورو از ۲۷۱ هزار تومان و پوند بریتانیا از ۳۱۵ هزار تومان فراتر رفت. این افزایش‌ها در حالی ادامه دارد که ریال طی دو هفته گذشته بیش از ۱۵ درصد ارزش خود را در برابر دلار از دست داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/78298" target="_blank">📅 16:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78297">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h09n6J4775H0ZTH6kT-RGkMQ417JVEG91MiCijG0VdGLVGxtQBzy1hd1B81R0pjtiLae4lxzTNpO3CV_G6cRfxiYvMOZXY94sASw61rMeXyopBiDDtnOYCylOo04-I-ADnaN3nwAr2jQNEHdvV9_UB5wIFeNJQndQpaObDTxnvb5LqiV55OOemLEDUab3uNmXRUvzr2zNc59MeCKP1gFQpIDPhjRo7i0Ydmnnf0NgbcYgZKxb9Uo18UhMvTEhi3Kz1zDUPr8AjINH1nU0eflFV9KJ4GbOouKUm4kqOxAGdfijkj0_bYxfW-7WyCFtxu1dLl-_qO49X0WBPuqTqFFZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت خام برنت برای نخستین بار از دوم مرداد به ۱۰۰ دلار در هر بشکه رسید و بار دیگر وارد محدوده سه‌رقمی شد.
افزایش قیمت نفت و ارز در شرایطی رخ داده است که درگیری‌ها در خلیج فارس و منطقه ادامه دارد. شامگاه سه‌شنبه ۱۷ شهریور، آمریکا اعلام کرد پس از حملات موشکی ناموفق جمهوری اسلامی به دو ناو جنگی این کشور در خلیج فارس، پنج نفتکش مرتبط با سپاه پاسداران را منهدم کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 245K · <a href="https://t.me/VahidOnline/78297" target="_blank">📅 16:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78295">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hf1Wm8UMUmdLvKNbc27gzo6lBnGBLeGn8PPNebzdBj23XGTYLA92dvZkyt_7VhRSOXPZ-wrQ0qk7hg7aG9IUsdOjyOayD2-x-VhwmXooq6on26BgGRgpc8xNLe9FZsFfQXWE1K78fEjnu-Jc_0_9PSYaZ-FsCC3vF98IlTNt0d7BuRlDU3F04iYVDRDqgz1SgngSVHPAKan7T5t6cTELVT0Gmbofe-xmy20mTJZkNfsgwkz_pF4Uz6JPA3vnQoameFPQov7vlo0qirpbC-kFRw-3tGPtbbyGU-Q3cfo6wwmUUyFX-QbiyxMWRc9exrjuTeZoWn2ZWkT6MHcUZJX3IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ftzvZV9R2Zgwt46ZQHVxglYxCYIQgIMMy3o1gXXTtpev9VlrdYtpXBXADwlGOCx8ySos7j5djPyfa4Bv72C_pq_d1UEsR9cNWBcNvSXBoKqkiPDj78NVzErygo8HkZQH2fypO7geueeAQMHwSzeU9achPWbvd5dOhu9TTsyNi52Ua8g3axpCSxkuRjYMiE9PhfkI-VUEJUwu0Tn-so-FMAP66RlbwZ4X_u4MjFCoenT3lm9CitQT9dgCCc_-osuc4Ue3NloKFTcIFPlMe0UZ8APCq6QCuHyuvpTdt64pUY6OWj7-gu0Hgi5Nge60JjPXpnYP0OSog6MIzSpcdxBKOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سازمان تجارت دریایی بریتانیا (UKMTO) ظهر چهارشنبه ۱۸  شهریورماه از وقوع حادثه برای یک نفتکش در ۲۴ مایلی بندر راشد امارات متحده عربی خبر داد.
براساس این گزارش، «کاپیتان یک نفتکش گزارش داده است کشتی‌ای را مشاهده کرده که در حالت لنگراندازی کج شده است، که احتمالا نشان‌دهنده ورود آب به داخل آن پس از حمله با یک پرتابه نامشخص است.»
@
VahidOOnLine
مرکز عملیات تجارت دریایی بریتانیا اعلام کرد یک نفتکش در ۲۸ مایل دریایی جنوب شرقی بندر فاو عراق با یک پرتابه ناشناس هدف قرار گرفته است.
بر اساس این گزارش، ناخدای نفتکش برخورد پرتابه با شناور را گزارش کرده است.
خدمه نفتکش در سلامت هستند و تاکنون هیچ پیامد زیست‌محیطی ناشی از این حمله گزارش نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 228K · <a href="https://t.me/VahidOnline/78295" target="_blank">📅 16:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78294">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TWaB1pcxUfZ4R20eNDCDq4_bcycIzojtPrVuwdM38DZGysseOvdAX8sjEnV6cdaRzVVRaoAR2W_0-KaDa6PbT9WP0AkuGt-bnYEt_7DrIjz7rRK5-J9M7H0HWrx7LTKWw2kgDZshpibMfewCAG2H2vd4nRS_aQvsS1bVIbeqrlPrn60TbBuQgsShYJqr_3xFVYTBcFbPhs5MOL-WtzeXKhnou8LPItXpI1n2HRqIrUFHFCyfQjEeHXoyhifK8GE8yTdUrcppHVqlb2aHhIwR8K5WgGESoxa1jlsSh-LuK02TcUPVTdugI3alOXvLz-mYWV9Q1SpAZvgC7jPAtkRYLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترجمه ماشین:
🚫
ادعا:
نیروهای سپاه پاسداران انقلاب اسلامی ایران (IRGC) مدعی شده‌اند که دو ناوشکن نیروی دریایی آمریکا را که در خاورمیانه در حال عملیات بودند، هدف قرار داده‌اند.
این ادعا کاملاً دروغ است.
✅
واقعیت:
هیچ ناو جنگی نیروی دریایی آمریکا هدف قرار نگرفته است؛ تمام حملات مورد تلاش سپاه پاسداران شکست خورده‌اند.
در همین حال، نیروهای آمریکایی تنها طی هفته گذشته موفق شده‌اند ۱۰ نفتکش ایرانی را منهدم کنند.
این شناورها بخشی از یک شبکه سایه چندمیلیارددلاری بودند که منابع مالی سپاه پاسداران را تأمین می‌کند و ایران قادر به دفاع از آن‌ها نیست.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 228K · <a href="https://t.me/VahidOnline/78294" target="_blank">📅 16:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78293">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SBoN0Ip7wMU1NSpCKlVEhUEjDuVhuZRy-0uS8iGHGevsYglw_aYjuTtXtOLGIuJb2YtVrV-95Qgqdigf75_4b9jyoX1qCdajAszJ37jIjX4x4PhbRCl7FqOPpGJtDz4fSZD4ErzPtuR6Y77hRrj-mLtYgXVauD8Lc4Wt04yn7OEld32SanVldAYEkuUyqTa45jutpYdnflbz0U2t2YBQJI1kPEQ3iHBM10lyCuytm6gbDJaoak1u-pxTGvPc66hCxQRaQTQPF6d2gpkkg6W8AeNkT2_vmUs1NTQuPik10j7U0YIZ0zc6iSH6kQd__dYsIa3JE-aRBzNPFiUUve3jUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«ماموستا محمد نزهتی»، روحانی اهل سنت و امام جماعت منطقه چیانه در شهرستان پیرانشهر، در یک حمله مسلحانه کشته شد.
سپاه پاسداران او را از روحانیون همکار با بسیج معرفی کرده و مسئولیت کشته‌شدن نزهتی را متوجه آنچه «گروهک‌های تجزیه‌طلب کردی» و «صهیونیستی-آمریکایی» خوانده، کرده است.
براساس این بیانیه، نزهتی سابقه «همکاری طولانی» با «بسیج اساتید، طلاب و روحانیون» داشته است.
سپاه همچنین فعالیت‌های او را در راستای حمایت از جمهوری اسلامی و آنچه «وحدت شیعه و سنی» خوانده، توصیف کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 254K · <a href="https://t.me/VahidOnline/78293" target="_blank">📅 16:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78292">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11f95a9d62.mp4?token=otNRe6dVsxBG7a5NRfoASPRjGENMO7WGJZzTmyK5k3vIn2b3aDz94N-795ULQiLbZ3-kVNkaNqMGWHMoaOp7jJG4_d4zBw7R1V3OQPmkGUHAem8GloKoxnABZ4v_MkYhElFadNlaLLKYOPgFbcGjSW7Cef1sPwvXgk3lL49b03i4Pvk8WjgbiFYLUlTb4BgjLUtQmZ9f02ymeR-qPttFp4E5XOU1HeK2PBfCi_LRF4cx904u9tc6asioUg5HLDRQNxEOrzBxPjFJIAWdlXHpeRZrDnYto4Ar814nSiBkZitOBJwWIdTrUsIGgiTnaQ2ohCNYBBZLqm1dzsU6_4Q0rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11f95a9d62.mp4?token=otNRe6dVsxBG7a5NRfoASPRjGENMO7WGJZzTmyK5k3vIn2b3aDz94N-795ULQiLbZ3-kVNkaNqMGWHMoaOp7jJG4_d4zBw7R1V3OQPmkGUHAem8GloKoxnABZ4v_MkYhElFadNlaLLKYOPgFbcGjSW7Cef1sPwvXgk3lL49b03i4Pvk8WjgbiFYLUlTb4BgjLUtQmZ9f02ymeR-qPttFp4E5XOU1HeK2PBfCi_LRF4cx904u9tc6asioUg5HLDRQNxEOrzBxPjFJIAWdlXHpeRZrDnYto4Ar814nSiBkZitOBJwWIdTrUsIGgiTnaQ2ohCNYBBZLqm1dzsU6_4Q0rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشک‌های مادر یسنا (فروغ) اسکندری در سوگ دخترش
یسنا اسکندری، وکیل دادگستری و نقاش، شامگاه ۱۸ دی‌ماه ۱۴۰۴ در منطقه آریاشهر تهران هدف شلیک نیروهای جمهوری اسلامی قرار گرفت و جان باخت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/78292" target="_blank">📅 16:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78291">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kEpljqU20_xf7Hph9RtgB0kGSCqQnJmKv1g7CIukNCaAcMXw59H9cb82qy9pWM8XDEnNo-B8LEOnqwvcOwZKx1Cr5RPy8iKpKkHK91XnUYRdBqVc34cZPO-o573zSVVBlBBxNM2wAsSY-n_zQ8ul0yTooZSEQHg2OZO9ZmnnH2CTZYiXBcVsmsobMLPQvdv64e4xjYZFS-euJ0G4DL6uMd5BBWXqN63LZST3qCRJya3FszNkkQFFBcJ8X_KTEjSXxXN6YOSeRByzjsuMKW7zCC3wsZ8_JlZZTLJWGQmi7kcl2OialvMPhUZ6BFPmP545qWr06uDTtK2IAdjtGAQBDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران: دو شناور و هشت نفتکش را هدف قرار دادیم
سپاه پاسداران که در طول چند ساعت گذشته با انتشار چند اطلاعیه از حملات موشکی خود به مواضع آمریکا در اردن و بحرین خبر داده بود، در آخرین اطلاعیه مدعی شده است که در واکنش به حمله آمریکا به ۵ نفتکش ایران نیروی دریایی سپاه به «دو فروند شناور آمریکایی و هشت نفتکش» حمله کرده و «خسارت های زیادی» به آنها وارد کرده است.
در این اطلاعیه که بامداد چهارشنبه ۱۸ شهریور منتشر شده همچنین ادعا شده است که «۱۰ فروند کشتی متخلف که به گفته نیروی دریایی سپاه، قصد عبور از «منطقه ممنوعه و ناایمن تنگه هرمز» را داشتند حمله شده است.
این گزارش‌ها هنوز از سوی منابع مستقل تایید نشده است.
با این حال، سنتکام در اطلاعیه نیمه شب سه‌شنبه خود هدف قرار دادن ۵ نفتکش ایران را در واکنش به حمله به رزم‌ناوهای خود دانسته و گفته بود این ناوهای جنگی خسارت ندیده و در حال ادامه ماموریت‌های خود هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/78291" target="_blank">📅 08:24 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78290">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3e8057645e.mp4?token=XM-sygrDS03vfixPKght-aghptPLliFWPODoykHY89-e33_mDyaEgbiYZl6kuL61us6AmN8qByTRnPw3gqIh_1yD6yzRSyNXjX8YIEOi-5pf1SmGR-dWuans3EVEG2W3ZO2DndoHCyepi88aFvnSXdmQB88gBZljSCWPK61OJFfTE6j3bS1SiF3pPd9dY-1TXnYg5knHtk5N2IxMqBYMVQyEoXTMrs62N1kgULs1HIS2gL0kLpWya06evZS0Dn_mkE___DUs6hqbRIqY9UvbNeHr0JXnllQxJpcfrFOGcSJq5Pghj2fQkCMC7zn3KSkZ_8BYkzMdv44jXEWI-uwqwg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3e8057645e.mp4?token=XM-sygrDS03vfixPKght-aghptPLliFWPODoykHY89-e33_mDyaEgbiYZl6kuL61us6AmN8qByTRnPw3gqIh_1yD6yzRSyNXjX8YIEOi-5pf1SmGR-dWuans3EVEG2W3ZO2DndoHCyepi88aFvnSXdmQB88gBZljSCWPK61OJFfTE6j3bS1SiF3pPd9dY-1TXnYg5knHtk5N2IxMqBYMVQyEoXTMrs62N1kgULs1HIS2gL0kLpWya06evZS0Dn_mkE___DUs6hqbRIqY9UvbNeHr0JXnllQxJpcfrFOGcSJq5Pghj2fQkCMC7zn3KSkZ_8BYkzMdv44jXEWI-uwqwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده (سنتکام) با انتشار ویدیویی نوشت: نفتکش ریسکو روز سه‌شنبه، پس از آن‌که در واکنش به تلاش‌های سپاه پاسداران برای حمله به یک ناو جنگی نیروی دریایی آمریکا توسط نیروهای سنتکام منهدم شد، در خلیج عمان غرق شد.
@
VahidOOnLine
M/T Riesco sinks in the Gulf of Oman, Sept. 8, after being destroyed by CENTCOM forces in response to attempted IRGC attacks on a U.S. Navy warship.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/78290" target="_blank">📅 05:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78289">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پیام‌های دریافتی:
ساعت 4.19 دقیقه صبح بندرکنگان الان صدای انفجار اومد
در و پنجره ها شدید لرزید
سلام صدای انفجار نزدیکای بندر دیر
صدای انفجار شدید.بندر دیر.
ساعت ۴/۲۰ بامداد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/78289" target="_blank">📅 04:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78288">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uI3f1pDskdbuEqmTCilMTrR_33GTVlx2UHw7aYjlIenQUhX2g3UXj_tuNT-8hFxM3GFxmr7Puv8dJzg1qyghB2hRjMXmicoy9P1_SXPOXu2V104lwy1uCQSFokLQ_Z96vW8BacfHd1jJhKGaxYU75rRfqNnz2I9qxmrR2UULGw5cd8IRKCwaN3tLlt3sSh6GrrUx9SlD_y7Ykj_gbbsyTf4OIot6ihjn2-xxcpSh_KxuCPH75zYdxuivrF-Xm_LrEq71OSf19v_uywPieT2KzDyPcJ16WsHV1-zgraZG4eSOd5Xigu5iSOcBtSfVFV8IBBMfmh5L_Ks-sBnbe2H61g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران در بیانیه‌ای خطاب به «مردم مبعوث شده ایران اسلامی» اعلام کرد که با رمز «حیدر کرار» به پایگاه الازرق اردن حمله کرده است.
در این بیانیه آمده که به محل استقرار جنگنده‌ها حمله شده است.
پیش‌تر اسکای‌نیوز از رهگیری موشک‌ها در آسمان اردن خبر داده بود.
تلویزیون دولتی سوریه نیز گزارش داد که پدافند هوایی سوریه برخی موشک‌ها را که از ایران شلیک شده بودند بر فراز شهر مرزی اربد در اردن رهگیری کرده است.
برخی رسانه‌ها در ایران از جمله همشهری نیز گفته‌اند که سپاه با «موشک‌های خوشه‌ای» به اردن حمله کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/78288" target="_blank">📅 02:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78287">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6d875f49ad.mp4?token=lmZhUSu_k2EjyTyJE46J1tjJpvEgVMY09X_BahIMQlzmpnZRZWf3iCxpw-4bY41JtrL4NvdmD84_6Zkp-Oxh0UBQ_dE3AUgI5HT8FlZR7nNFn1x-D3hE2j3HrtOL_9jDqV1FNolQS3IHJCIMmerin-T6C0a9zgsENl-oW1DFnefZXI1qk-3giTgC6mHWF_AD5BqEVr8ta5-cELL3pfr858yTvStpUHcZDlVv1kW4kArs4Xmx1Oaj4w3ax9C2xW7vkEaWIN8sVyIHspXjnoCpItSEuq5gq9RyoAp2qjYGFXTykFrnN0upIthaBn2jVPjWHpg5PDhmIt2C8NRY3M0yfA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6d875f49ad.mp4?token=lmZhUSu_k2EjyTyJE46J1tjJpvEgVMY09X_BahIMQlzmpnZRZWf3iCxpw-4bY41JtrL4NvdmD84_6Zkp-Oxh0UBQ_dE3AUgI5HT8FlZR7nNFn1x-D3hE2j3HrtOL_9jDqV1FNolQS3IHJCIMmerin-T6C0a9zgsENl-oW1DFnefZXI1qk-3giTgC6mHWF_AD5BqEVr8ta5-cELL3pfr858yTvStpUHcZDlVv1kW4kArs4Xmx1Oaj4w3ax9C2xW7vkEaWIN8sVyIHspXjnoCpItSEuq5gq9RyoAp2qjYGFXTykFrnN0upIthaBn2jVPjWHpg5PDhmIt2C8NRY3M0yfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترجمه ماشین
خبرنگار:
آقای وزیر، بخش زیادی از توجه افکار عمومی آمریکا معطوف به آخرین تحولات در ایران است. می‌توانید درباره حملات آمریکا به نفتکش‌های ایرانی صحبت کنید و توضیح دهید که این رفت‌وبرگشت اقدامات در ۲۴ ساعت گذشته چگونه بوده است؟
مارکو روبیو:
بله، این رفت‌وبرگشت کاملاً روشن است: ایران همچنان تلاش می‌کند کشتی‌های نیروی دریایی آمریکا را هدف قرار دهد و هر بار که این کار را انجام دهند یا تلاش کنند انجامش دهند، نفتکش از دست خواهند داد. فکر می‌کنم امروز هم دوباره شاهد این موضوع خواهید بود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/78287" target="_blank">📅 02:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78286">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b638672d55.mp4?token=ApyiBqUWbOQP1WevtRWSMh6qOJyt2l5Ak3hNU452xTYlC87uO_WPLIxxV_LAcXpyzrZE2xcywhGR2IhAOpThRw3db2W5TMhFFlvJgCNTu2dFHPLqIWNhrf3xXlEtj3mmVB1B-hnpWOkpPYt7Ns82KPtGdRGlMlocEnpex_fNSz8SvrJbrdDyxSO7-unY4VMveezfaYsmsq4CYFETjATuobmwk2eKRSPDrZHOKYEMGdEpZGqs-TjZapi8UZ5UaE2pAac9pBWmbHkpNWginxMPPIN6hu8EN77HhBIboLlC_I8xtyaTI3Ni5aCzCdCfOq13QUqmjFOpb6RJK1u4lrKzxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b638672d55.mp4?token=ApyiBqUWbOQP1WevtRWSMh6qOJyt2l5Ak3hNU452xTYlC87uO_WPLIxxV_LAcXpyzrZE2xcywhGR2IhAOpThRw3db2W5TMhFFlvJgCNTu2dFHPLqIWNhrf3xXlEtj3mmVB1B-hnpWOkpPYt7Ns82KPtGdRGlMlocEnpex_fNSz8SvrJbrdDyxSO7-unY4VMveezfaYsmsq4CYFETjATuobmwk2eKRSPDrZHOKYEMGdEpZGqs-TjZapi8UZ5UaE2pAac9pBWmbHkpNWginxMPPIN6hu8EN77HhBIboLlC_I8xtyaTI3Ni5aCzCdCfOq13QUqmjFOpb6RJK1u4lrKzxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: "
آمریکا ۵ نفتکش سپاه پاسداران را پس از هدف قرار گرفتن یک ناو جنگی دیگر آمریکایی توسط ایران منهدم کرد"
"U.S. Destroys 5 IRGC Tankers After Iran Targets Another American Warship"
ترجمه ماشین:
تمپا، فلوریدا —
نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) روز ۸ سپتامبر پنج نفتکش حامل نفت خام ایران را منهدم کردند؛
این اقدام پس از آن صورت گرفت که سپاه پاسداران انقلاب اسلامی (IRGC) طی دو روز گذشته، دو بار یک ناو جنگی نیروی دریایی آمریکا را با موشک‌های بالستیک هدف قرار داد.
ناو جنگی آمریکا با موفقیت از حملات ایران اجتناب کرد و به گشت‌زنی در آب‌های منطقه ادامه داد. هیچ‌یک از نیروهای آمریکایی آسیب ندیدند.
در پاسخ به تازه‌ترین حملات ناموفق ایران، سنتکام نفتکش‌های حامل نفت خام سپاه پاسداران
M/T Kaviz، M/T Charminar، M/T Horizon 1 و M/T Riesco
را در
دریای عمان
و همچنین نفتکش
M/T Derya
را در نزدیکی
جزیره خارک
منهدم کرد. نیروهای آمریکایی پیش از حمله به کشتی‌ها و از کار انداختن آن‌ها، به خدمه دستور دادند کشتی‌ها را ترک کنند.
ایران از این نفتکش‌ها به‌عنوان بخشی از یک شبکه چندمیلیارددلاری پنهانی استفاده کرده که منابع مالی سپاه پاسداران و نیروهای نیابتی منطقه‌ای آن را تأمین می‌کند. ایران هیچ وسیله‌ای برای دفاع از این شناورها ندارد.
در ۵ سپتامبر نیز نیروهای سنتکام سه نفتکش حامل نفت خام ایران را پس از آن منهدم کردند که سپاه پاسداران تلاش کرد به یک ناو هواپیمابر و یک ناوشکن موشک‌انداز هدایت‌شونده آمریکا حمله کند. تمامی تلاش‌های سپاه پاسداران برای حمله به ناوهای جنگی نیروی دریایی آمریکا ناکام مانده است.
centcom
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/78286" target="_blank">📅 01:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78285">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dc7356e9f5.mp4?token=XHsXmcffQZhbJjSpUmCYtdtCMkuEzApNmH6uDF7fLnUEpk2oCmmLIcraR4rYv4BXtUDjUh73crNf3fEwit8YOxKulQ50dFCmkz-9Vb7WL9wrXMWlBGmAZKSGapkLo12HNndihQhHHwsL1t8pcY2TvRNg88x8PoeDMbXnlAOj8Vpdv7hDezGVsptLK1h55LZoAP6XyCJQ4XiTeHNsITk13k1I3dXnp97gjmsfcy0UL4qMytDKOpyXHniK9PL1w-gAm0h721tvjEA8kZ4UGGXDdZPL5mFqaXmmmf5MHCnFINyoiKUUG1rm-c2J5Q052OQ9YQgJ0ciDM7au1CQ9cXsK3A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dc7356e9f5.mp4?token=XHsXmcffQZhbJjSpUmCYtdtCMkuEzApNmH6uDF7fLnUEpk2oCmmLIcraR4rYv4BXtUDjUh73crNf3fEwit8YOxKulQ50dFCmkz-9Vb7WL9wrXMWlBGmAZKSGapkLo12HNndihQhHHwsL1t8pcY2TvRNg88x8PoeDMbXnlAOj8Vpdv7hDezGVsptLK1h55LZoAP6XyCJQ4XiTeHNsITk13k1I3dXnp97gjmsfcy0UL4qMytDKOpyXHniK9PL1w-gAm0h721tvjEA8kZ4UGGXDdZPL5mFqaXmmmf5MHCnFINyoiKUUG1rm-c2J5Q052OQ9YQgJ0ciDM7au1CQ9cXsK3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنا بر ده‌ها پیام‌های دریافتی از صفهان، یزد، خرم‌آباد، خمین و شهرهای دیگر چندین موشک پرتاب شده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/78285" target="_blank">📅 00:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78284">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jv4qZ2lXUPIOByzDFxc2PusBplEz1Wqoji1thI12FTdP5p8wqXdkB5NKD4bTj0aSDpdM5UNDXJlCuHQV74-YaeSW58Hf7uiSEbg4flghKfdo2yFG4Bi2LxNjgT9cIVJy_qmfgeY20MoG3SlOLZunGUI_LVMKdnlPmmuGc_cq3s2XzqcS0luaiiVjkbHGKdzab8a7bkyLX3yrcR3VD8m-WeY1uWMkH8SDHegrtDhozCd8CVuyd90meOYxRl-MEd12tIn_YE3KR_G2jxrntSFkqDBAU9CzF2teul3FwXcfONpmsddXRLHlg9VTdHKZeK1gtJ1k2nE5TP9KyMGAPGO0Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی گزارش‌ها از حمله ارتش آمریکا به اهدافی در جاسک و اطراف جزیره خارک، رسانه‌های حکومتی در ایران تائید کردند که یک نفتکش دیگر نیز در اطراف جاسک هدف قرار گرفت و خدمه آن با قایق نجات در حال انتقال به مناطق ساحلی هستند.
پیشتر رسانه‌های حکومتی در ایران گفته بودند یک نفتکش در اطراف خارک هدف قرار گرفت.
رسانه‌های اسرائيلی و آمریکایی به نقل از مقامات آمریکایی گزارش داده بودند که علاوه بر اهداف دیگر، چند نفتکش ایرانی نیز هدف نیروهای آمریکایی قرار گرفته‌‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/78284" target="_blank">📅 00:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78283">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tsnKWv_5TcbRdePZqSibFnVT6WXHbroBUFQsYaGIybN_I6dGFnL2BME7EMOTuCnKQBw1sX4p1nr23fqGCZkr7rJO8OVOHcpInO0RDPy9Utl2F0ntPKFIa-JhP2HT4Y81sml7XmCXBMEUZAcZyAtXUBEVUx8svNq6nFMHkURnWqNd8DMM3tUIY9EA_el7BpobdeoSRoM9VNCzS5vZyEtLawh2e9hM7MAuYzluXnwemyqzPXF5f8tc040moVAfdhcDmyehW0EfUxdgr4oPoJ4Vu3jqZZrB2ZbirT4mOZQeSh6PdDNtCePeQWHSEXt8v2lvKPaL3pSmfwc9nfaeQF6y2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار سپاه به خدمه نفت‌کش‌ها در کویت و بحرین: شناورهای خود را ترک کنید
سپاه پاسداران انقلاب اسلامی هشدار داد که نفتکش‌های مستقر در لنگرگاه‌ها و اسکله‌های بحرین و کویت را هدف قرار خواهد داد.
در این بیانیه که در رسانه‌های جمهوری اسلامی بازتاب یافت، اشاره شده که آمریکا به «چند نفتکش ایرانی» حمله کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/78283" target="_blank">📅 23:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78282">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PRL20bJ4tll3-ASUdiKVKeOSmJHefBFrG6Jy15zlVxYxoSjGrjrkuK8wR8muMQv0if6KmX07kmfFBDcGq8mA6xoM8aysyFse-HJvCljSEWrX2k3PLmitx7AdEppraDOEfjfiTq58LczB-RCEz87F8as5L4TtSTVlNUqRMNBPg79mScBAorR371q58WDqQc8eSO91iwstWKhg6sBlj6f9OtB5ZJyUZZsxHrJ2teGWC8epYALjGfwhInUNaJrmFyRCS9SByceRkamx1zBHDnHNOI7LMb_qmNNmYHVdeMHCfpsuZwaPzmlV-JSpJZELWP_zxTdGjzgD20srqEeUCOky4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاکس‌نیوز: ارتش آمریکا نفتکش‌های ایرانی را در نزدیکی جزیره خارک و جاسک هدف قرار داده است
شبکه فاکس‌نیوز شامگاه سه‌شنبه ۱۷ شهریور به نقل از مقام‌های ارشد آمریکایی گزارش داد ارتش آمریکا اهدافی را در نزدیکی جزیره خارک و جاسک هدف قرار داده است که شامل نفتکش‌های ایرانی می‌شوند.
فاکس‌نیوز به نقل از این مقام‌ها گزارش داد، این حملات بخشی از تلاش گسترده‌تر آمریکا برای افزایش فشار اقتصادی بر ایران است.
مقام‌های ارشد آمریکایی افزودند این راهبرد شامل غرق کردن و از کار انداختن نفتکش‌های حامل نفت خام ایران می‌شود.
@
VahidOnLive
خبرگزاری تسنیم، رسانه وابسته به سپاه پاسداران، گزارش داد که یک نفتکش کوچک ایرانی در فاصله ۴ مایلی جزیره خارک، هدف حمله موشکی ارتش آمریکا قرار گرفت.
تسنیم نوشت که این نفتکش در محدوده لنگرگاه جزیره خارک مورد اصابت پرتابه نیروهای آمریکایی قرار گرفت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/78282" target="_blank">📅 22:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78281">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbsZQvTwlxzU8Jj82J-vVOLmKARRroyIY0If8yx1Ovpr3k_o_ueKXIMMok1mP5KqFXWcTJHMax89mqXh4sjb5HjxSn8PJl2CH1X1HEXTwVPqyiMI06g4XbIl6c3fpmXeU1g4lzFWSyaM5qL6t4yKwUX4FaiZTq3L_wpMD0yBwYxK0T65RcRFS4qVNbqtTpqSPZ1dRvWkwBJQccrXANroWmmNfxqYYJy9ZcU9rlx2FWpFW7a_pBGrWZfti8exPPltVnKjqOJ8UrPxyLRc-JMnqpKXLGQXA8YNAFxlevbtFSMsNDDG0XqxdTsUayWGUtv3v0HrAw1Y0Fo9fLQRMF96bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی عبداللهی، فرمانده قرارگاه مرکزی خاتم‌الانبیا، روز سه‌شنبه ۱۷ شهریور اعلام کرد ارتش آمریکا به سه نفتکش ایرانی اخطار تخلیه داده و آن‌ها را به هدف قرار دادن تهدید کرده است.
عبداللهی هشدار داد هرگونه حمله به نفتکش‌های ایران با واکنش نیروهای مسلح جمهوری اسلامی ایران همراه خواهد شد و پایگاه‌ها و منافع آمریکا در منطقه هدف قرار خواهند گرفت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/78281" target="_blank">📅 22:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78280">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">"صدای انفجار از حوالی ساحل جاسک"
خبرگزاری فارس وابسته به سپاه پاسداران:
حوالی ساعت ۲۱:۴۵ امشب، صدای انفجار در شهرستان جاسک شنیده شد.
منابع محلی می‌گویند صدا از سمت دریا و نزدیکی منطقه سنگ سیاه به گوش رسیده و انفجار در دو مرحله و با فاصله کوتاه رخ داده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/78280" target="_blank">📅 22:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78279">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MgigP9TTCqwVqh-UzbnscBEfXTiOX39bPYKPDpn_iaRQ6UDQnycAOXiSLodg4C9G36Kzm7uo3xI5Sa6ckKed5hqOMIHPzksG07fRv3wcOL_BpXXRJqblbrRs7UzWaeUddxxkGZhiqLFkykJQ_yfTC5HgIlXKuf_YOoFW9SNAHGy7MWwPkrjvGJfS84Fk4vT6oSwxRw5-7ARIaDand6Fih3QG_7YknA_1W-47Jlv8eq7N0tqhJK_ubUKbQv90v7MxtZJeLOEhWw2fbISWHCquzUr0aMiMpdkbdDVo6Gjv7iyvmu9qHR1XuOXG1BL-5oR3-2K3L72iN9wtl0zt8qHgsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام آمریکایی روز سه‌شنبه ۱۷ شهریور به رویترز گفت یک شناور بدون سرنشین زیرسطحی نظامی آمریکا در خاورمیانه، هنگام پایش آب‌های منطقه در حمایت از جنگ علیه ایران، دچار نقص فنی شده است.
این اظهارنظر ساعاتی بعد از آن منتشر شده که سپاه پاسداران انقلاب اسلامی از «شکار» و به «غنیمت گرفتن» یک شناور زیرسطحی آمریکایی در تنگه هرمز خبر داد.
مقام آمریکایی که به شرط ناشناس ماندن صحبت می‌کرد، گفت این شناور معیوب از «مدل قدیمی‌تر» بوده و هیچ‌گونه تجهیزات سونار یا رادار طبقه‌بندی‌شده حمل نمی‌کرد.
او افزود این شناور بیش از یک روز پیش دچار نقص فنی شده است اما به سرنوشت آن و یا کنترل نیروهای نظامی ایران بر آن اشاره نکرد.
در بیانیه نیروی دریایی سپاه پاسداران ادعا شده که «یکی از مدرن‌ترین زیر دریایی‌های هوشمند و بدون سرنشین» ارتش آمریکا در بامداد روز سه‌شنبه به دام افتاده است.
پیش از این گزارش‌هایی درباره مین‌روبی آب‌های تنگه هرمز توسط ارتش آمریکا با استفاده از تجهیزاتی مانند شناورهای زیر آبی بدون سرنشین منتشر شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/78279" target="_blank">📅 22:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78278">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-B42IgPNjqXTK99tdX899jKNq3QErZ4aGOz4GIW8lvauCne7877GFGoJ74gNG2qyE5K_nBTwTN408fLFlbmJe425iUA6QRS05jem2sG9TRabDbiws64aHvfANlrc8DCFXwNbFTSMjTKJ4ZGcfOCZa5keazNh2b3iX2fGdRg4KmslekdtAeTx5adSOaWwkargHUykp3f6haLBN2y_94fj0j-VmFm4jBsv4Yv9Kv8oUZj_16GeI2vf0hg1lMUTC4XwZRfFN8oxtBJ_-VGiL8Ch5gCQfd5hlIf0wL4e1G7VKGBu9xdhBddb_61g_QcPR_8Z2vfDKtgQfM-TxUmZ2Pu9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای دولتی یمن روز سه‌شنبه ۱۷ شهریور خبر دادند یکی از فرماندهان ارشد حوثی‌ها را در جریان یک درگیری در استان تعز به اسارت گرفته‌اند.
منابع نظامی، این فرماندۀ حوثی را ابوعلی الاجنی، رئیس سازمان اطلاعات و شناسایی انصارالله، معرفی کرده‌اند که در یک درگیری سنگین در تعز در جنوب غربی یمن به اسارت درآمده است.
این چهرۀ مهم حوثی‌ها، که با وجود جایگاه نظامی‌اش در کادر رهبری حوثی‌ها جا ندارد، به همراه ۹ تن دیگر بازداشت شده است.
درگیری‌های سنگین در تعز از پنجشنبۀ گذشته در جریان بوده و تلفات زیادی به جا گذاشته است.
در همین حال مارکو روبیو وزیر خارجۀ آمریکا هم با اشاره به نقش نیابتی حوثی‌ها در قبال جمهوری اسلامی، گفت معتقد است که «دست ایران پشت بسیاری از حملات حوثی‌ها به عربستان سعودی مخفی است».
وزیر خارجۀ آمریکا با تأکید بر روابط دفاعی کشورش با عربستان سعودی، گفت واشینگتن تحولات یمن را از نزدیک زیر نظر دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/78278" target="_blank">📅 22:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78277">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwQUc1HSuv0XrZEundGB0J2nlOpQRZaGJdE620v2UxgEfRunVwFUrAXT0E2Q9viWFVsPKYuWGQWWzKM8KHxNRQlKxMy086QLAulLWnYFUFjBYpoAlt4yvorrw95bFtrpAwcu2AKmWiQNXWAE7DfG4btDfG1M7EHKA7v7BktvnTF9FeHlCbeckaBcvj4_66WgC9pBiHJ7F6rfHrkUJZSL6ANxhffFWWkiJ7fdWQoH_GgblljVOm0tPe0t0r12qm9kw7SdJFip903xOOTeisN-lCMXyTetj3gnmm4lOA1FOZ2TugK75ilotK5Tw_71E1YJ9GjsZyveSPOXcm9riE--Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری آمریکا، روز سه‌شنبه ۱۷ شهریور ۱۴۰۵، اعلام کرد در چارچوب «عملیات طرد اقتصادی»، ۳۶ شرکت و فرد مرتبط با بخش هوانوردی ایران را در فهرست تحریم‌های خود قرار داده است. این اقدام شامل ۲۷ شرکت هواپیمایی فعال در ایران و همچنین شماری از شرکت‌های واسطه، نمایندگان فروش و ارایه‌دهندگان خدمات باربری در کشورهای ثالث است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/78277" target="_blank">📅 20:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78275">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cI10Sh-lwBCI6Qd1FaCsqJB-qJuVDmj-2tZQFkdXg2EmHDf_KkOj96zF5QJmd46cGNmSYpdAD3vFAEnbP0z3KIBEPL0P60EFssup_79xp7z8qFQv2yheGDA146chhxjm77y3NUJL7hkDHf_RhlM4HCveWHdz-JpKOmEW682-ZSiUGs0ejJpZWCZ-bewL7Xei-typkEtkUXeX6h2-9T-OMDpah5izMdOWR0nR4OzwCJGZgE0mm6-to4iPwR5YVkp1d-7OpkKDbKaPtGNgGD-l3-jrCuDvC3C23lBThrXDyVpaqnBCTpXYhoLhxQaIvZlTtFO1Yq5DCxOlpCF3TjB-IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ucQirvv2QIb0jXoK-mx3ZuBL4I5U_r4DY7YPjkZXdWEunzYg3Tcd14IA8Ki7YIzurWdGw2cV0TYOEzZ4dOMcSn-xaVDP7Bx2vzU1ZQj4fdQkbi7fyDhO2GJsOVvyTBFeTYxngMQoFtjsdvmFVMmsqGcnsgt50cTHQuv6FiEKLYcqElV6XYzT__9pwRnpQzen1ud61c7G3mgvIoRBWr4jARBFC43AM5RQjFGk2BjAgLcC-0LJnHZDvUNZS2mAvptECCoHB_8B4P67nBleZixbN62_mmbiG5ls4cuJpsAptrR8SYM_hdIlo5-AF1aUGzRk1GzskUutQ2z4X8HQu7Vqpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی، روز سه‌شنبه ۱۷ شهریور اعلام کرد که یک زیردریایی بدون سرنشین متعلق به ارتش آمریکا را در محدوده آب‌های تنگه هرمز توقیف کرده است.
سپاه پاسداران توقیف این زیردریایی را «غنیمت گرفتن» توصیف کرده و اعلام کرد که تا ساعاتی دیگر تصاویری از آن را منتشر خواهد کرد.
این زیردریایی هوشمند حدود ۵۸۰ سانتی‌متر طول و نزدیک به سه تن وزن دارد و می‌تواند تا ۱۰ روز بدون نیاز به بازگشت به مرکز هدایت، عملیات خود را ادامه دهد.
@
VahidOOnLine
روابط عمومی ارتش جمهوری اسلامی ایران، روز سه‌شنبه ۱۷ شهریور اعلام کرد که یک پهپاد MQ-1 در آسمان بندرعباس شناسایی شده و با شلیک سامانه پدافند هوایی ارتش، سرنگون شده است. این پهپاد تهاجمی از سوی ارتش آمریکا مورد استفاده قرار می‌گیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/78275" target="_blank">📅 18:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78274">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NENpV_JwlpqzVLizkxjTrzjO_OtDrfNXU-syYcv4F_wX6I-SdBw-9unmnMmrel6vEqiL4oF3VtMvpRbSky1P6VlhjeIwg4LI5mNY62C2Han2u7idk2eBQ6uE5JuStmsPoYF0bdenUnGP1QAoOBZX6KY96vvMukHEm0gD0Npa9Fre7p95WNKnYcWNpJljIK0qdbme1Lko2EyxT2YbKPs2_lZ-ynNDQvBHK_Rlf5mGDNUjGlgpMdkScFd5viyx6e6LyLW0doPlSHYEMWrfixaNCSmRfmqNi6i5oXterDm1QsEKAyM-uDdGe8dYrWnQIItyPjEZdzEUMrRh9-bKvXGCeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عبدالرئوف اسحاقی، فرمانده حوزه مقاومت بسیج پارود در شهرستان راسک استان سیستان و بلوچستان، روز سه‌شنبه ۱۷ شهریور در جریان حمله افراد ناشناس کشته شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/78274" target="_blank">📅 18:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78268">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IBjF4sgQWtKMcYeeyIphQyjdjrz17izzpGU-azA-iRsjZnlBVfUAZPGtGzGeKEUtV3DxjKxVrAgV5VJaUNj-1NeoISVhZkCLcac51AwmBp71ly7ClboJWqtM3rneXxkF0hRDUjLrncM76vGZXyiYUcgMVIPml9lqcw_3qopk8Z7j4kVZN8k0eb3jTj5TiE2sUzMKruU6uTj-trbVAmKYRCbEh0qrV2Vh_ChuEdc18V5UoC6uJHzRwc0BwXHyUMrVSreqhUN3HNwJAYpKIePBl1WcAHGw2MVnLWMNIKQDFvFEue6zdVyO1AOA2S-pTb8N27VYXm1TgCta1qkwZA9mRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hZ0b0aSkCr1aBKghNuDPcgTQM5I7BUFqTyltEkwvyAZTQtW68F6d43PCbIpBlQYLXsdJQOaOLguqhXkjnBps4d734Ltpgh_bIbQjJOGDx9oGSTcFd9vjrqgG2qMRc8E83sMMqmTcA5bAcWhdSHSQN8j7JVHDXJXqOvyNhcHmFCmLiwnTGvn_0i-YUHVbFtZ0Z_zPJOCsjqlP47VPXSKqE1KOeuNUWd0pywdovAAE_nKdCoygmXVuZWDq7HQGdn8vkRub7bTNBp3-ZRDSVTHJ_JN7TEYXsRhRr0X8NwCG8Gj0PDLZ85PZeo5j8cu2nZz8Jr23t6v-HKdflkizSdYwMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/S_poAtBSUFbJ7ephizAbapqwQjf2bfo_hZxOdlVPuzh6LO8KpDJKlQjKHGdX6g1C2oP6PUckJ8aAAUdHXQc2f5WS9PG9Q73PNbPkAC_KViaKrFBr76W3b77HmgY9QXNK3rorlaQLiK76npXB1VTk1TMxsf9gowxhVG3Btc4fCY_SFL-hUTkpfklJNJABJeLxPztfefs1JpqnAmkna_mJbs1nCAiJqsXb00-Zb-1sgWLnpmaqzt0-LN0NHdiwoa21ZYNLoH11rewkYlH-MskWBOom8Q5m74HD73lEitDDaE9aoQMqUgHd6Z5m_YdNQf7OHIIj2JBRD8sXzysNxTdA1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BVwDdQ4v7Sxfa40fH5pafXIJfg-s99mqbEK-HUpEfjaR_v6meq1LKWAn6hwibeXE4Dr18bVce4yJxt5NdJ84seTHkfVktZNniFMQvLD_q9ZoYlzA4IzbRiSwyzlv6tCp3EmX0MHMLPqakMY48uc0FXuV8nbUd6FYehusfuqsUZH9OLA1nVd35KNUqNMPsMRqjdfHZz3fktcqsW6dtfIbGntxMHPp5QZhYa9jii2V341yUFQg2fQCFtpo-ifTtDrR-VQ8uXdhTq_oAkODW6CvjcNmrG3GZtiHYZD-529-L5Xpqq7ajmtpuH_f0L9raDLQkhAWGaE8B0ZMAnijKes7qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Vskz4MGHhE6CeXO2scRK3rTeICizSKqCWhqwIjnHtATOtzVxZwwX-ZGyae4kw_m4DQc24AI_Iw5mszvUg8zlD6BBgomURVw_bolJv4pW5ufrrb5N1iGHBILixddceWePTlTSlqYZ-bOe8mMT9d1wmnZ9m8Ksauw1xzHoWzdStIlT-7hMENI2veX6mr2RX3PFWRGCuWKtftGfCuxJVkNzg3gWowdj0NkISt41DBeU7BV_qd8oFjuy2AZXnODwqDX2tc9IIlhlqbhZYAYBgRbO2kt1DUP7pZj8wFeVRxvqtmEGZajcdddrbWCFM5B6cLvEqfzoPQQcXifkeRU73Z4GVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4e0b5c1294.mp4?token=CBIAxpzLW_1PnFtIyavuQaZNjk5wG96IAgLJNZDKK8S5nyi35JFoD0hC5n5IgXdMUjRzK5g8EjjOfDM5o4kMQ11QMA7CX3C5T_TZ4-GXWuiG738VYsYa4SbIBUktX1vgExiim21ZxW2apFpK9fVRP-jKLGCBqt4j1aeB31gZoQ4noJHi4qbbLooH9opq1uZCkbcTypURkAzB4ycLRlmK_GsNzv2y_QPJDlDhDuFAO1GIngJDNy4882kJ4zLukVVGLCWzO6G84itbwLQi2y21Bvlk79lhOJNTTBWXpdIcIxJdFJ_GdLnfAZjcCwdtr6bNB4BD9eOYtM5KVqjRL75ZDA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4e0b5c1294.mp4?token=CBIAxpzLW_1PnFtIyavuQaZNjk5wG96IAgLJNZDKK8S5nyi35JFoD0hC5n5IgXdMUjRzK5g8EjjOfDM5o4kMQ11QMA7CX3C5T_TZ4-GXWuiG738VYsYa4SbIBUktX1vgExiim21ZxW2apFpK9fVRP-jKLGCBqt4j1aeB31gZoQ4noJHi4qbbLooH9opq1uZCkbcTypURkAzB4ycLRlmK_GsNzv2y_QPJDlDhDuFAO1GIngJDNy4882kJ4zLukVVGLCWzO6G84itbwLQi2y21Bvlk79lhOJNTTBWXpdIcIxJdFJ_GdLnfAZjcCwdtr6bNB4BD9eOYtM5KVqjRL75ZDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عرفان میرزایی، خواننده رپ ۲۱ ساله و از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، در زندان دستگرد اصفهان جان باخته است.
درباره چگونگی مرگ او دو روایت متفاوت منتشر شده؛ ایران‌وایر از اجرای حکم اعدام و ایندیپندنت فارسی از مرگ بر اثر شکنجه خبر داده است.
بر اساس گزارش ایران‌وایر، میرزایی پس از شناسایی در ارتباط با اعتراضات بازداشت و با اتهام «محاربه» به اعدام محکوم شد.
این رسانه می‌گوید حکم او روز یکشنبه ۱۵ شهریور بدون اطلاع قبلی خانواده اجرا شد و تلاش نزدیکانش برای جلوگیری از اعدام نیز نتیجه‌ای نداشت.
ایران‌وایر همچنین به نقل از منابع خود گزارش داده است که خانواده میرزایی پیش‌تر برای خودداری از اطلاع‌رسانی درباره پرونده و حکم اعدام تهدید شده بودند.
به گفته این منابع، آثار متعدد جراحت و کبودی نیز پس از مرگ بر بدن و صورت او مشاهده شده و پیکرش با محدودیت‌های امنیتی در روستای غرغن فریدن به خاک سپرده شده است.
در مقابل، ایندیپندنت فارسی به نقل از نزدیکان میرزایی روایت متفاوتی از مرگ او ارایه کرده و نوشته است که این جوان در نتیجه شکنجه و ضرب‌وجرح شدید در دوران بازداشت جان باخته است.
خانواده او گفته‌اند هنگام تحویل پیکر، شکستگی‌هایی در دست‌ها، پا و لگن مشاهده کرده‌اند که آن را ناشی از بدرفتاری در زندان می‌دانند.
بر اساس این گزارش، میرزایی اواخر فروردین ۱۴۰۵ در یک ایست بازرسی در شاهین‌شهر بازداشت شد؛ ماموران پس از بازرسی تلفن همراه او و مشاهده ویدیوهایی مرتبط با حضورش در اعتراضات، وی را به زندان دستگرد منتقل کردند. نزدیکانش می‌گویند او در ماه‌های بازداشت برای گرفتن اعتراف اجباری تحت فشار و شکنجه قرار داشته است.
دادبان تاکید می‌کند، تفاوت جدی میان دو روایت درباره علت مرگ عرفان میرزایی، ضرورت انجام تحقیقی مستقل، بی‌طرفانه و شفاف درباره مرگ او در بازداشت را دوچندان می‌کند. اصل ۳۸ قانون اساسی شکنجه برای گرفتن اقرار یا اطلاعات را ممنوع و اعتراف حاصل از اجبار را فاقد اعتبار می‌داند؛ ضمن آنکه هر مرگ مشکوک در زندان، به‌ویژه همراه با ادعای شکنجه و آثار جراحت، مستلزم بررسی موثر و پاسخگویی مسئولان است.
dadban4
دو منبع به ایران‌اینترنشنال گفتند دلیل جان‌باختن او، شکنجه شدید در زندان دستگرد اصفهان بوده است.
اطلاعات رسیده حاکی است پیکر او هنگام خاکسپاری، آثار متعدد شکنجه داشته و دست و صورت و لگن‌اش به شدت متورم بوده است.
بنا به اطلاعات رسیده، ماموران امنیتی به دلیل ترس از تجمع مردم، اجازه خاکسپاری عرفان میرزایی در اصفهان را ندادند و پیکر او روز دوشنبه ۱۶ شهریور در روستای غرغن شهرستان فریدن به خاک سپرده شد.
زمان دقیق بازداشت عرفان میرزایی مشخص نیست اما منابع می‌گویند که او در ارتباط با اعتراض‌های دی‌ماه بازداشت شده بود.
بنابر این اطلاعات، ماموران پس از بازداشت، ویدیویی را در تلفن همراه میرزایی پیدا کردند که درگیری میان معترضان و نیروهای حکومتی را نشان می‌داد و از آن به‌عنوان مدرکی علیه او در پرونده استفاده شده است.
iranintl.com
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/78268" target="_blank">📅 16:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78267">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ib-0Pic-8IU__wU4HuTBNt7rs_KGik8iT1cCgW0n2sS2qKr3arOH9__LDRlXFR3dArlcXlWO-J4u0zjGWVBCNL7HyyXUL8lWw6hIbtEX2vagVIgltGC5NiEaQA4Rpl55FC6DUGz23YS6ajylZD_WPjhvroZYW5h0TkfOlbvT2puQaUCDIiC5TSCwIBnbBDM-6ETYMl5ued07xdndW4gmVcfsKs9ecPxRC-EnxjVi4TFI5-HOlJyLW6F2tT0m1heF8M7T4WBO45hIcFCkb8gkK73ec0DLyYK9jg38W9rjPb7MUR1I7mJxnGcVx1wFMOmfV1yBcIrCx2EdIZ3c5yQf9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش آسوشیتدپرس مقام‌های سعودی اعلام کردند موجی از حملات حوثی‌های مورد حمایت حکومت ایران به عربستان سعودی در ساعات اولیه روز سه‌شنبه، ۷۳ نفر را مجروح کرده است.
سرلشکر ترکی المالکی، سخنگوی ائتلاف به رهبری عربستان سعودی که در یمن می‌جنگد، گفت حوثی‌ها «تأسیسات غیرنظامی و اقتصادی» را در شهرهای ابها، جازان، نجران و خمیس مشیط در عربستان سعودی هدف قرار داده‌اند.
او گفت ائتلاف به رهبری عربستان سعودی «با نهایت قاطعیت، تمام اقدامات عملیاتی لازم را برای بازدارندگی شبه‌نظامیان تروریست حوثی» انجام خواهد داد.
به نوشته این خبرگزاری آمریکایی، این حملات در حالی صورت گرفته است که درگیری‌ها میان حوثی‌ها و نیروهای دولت یمن که مورد حمایت عربستان سعودی هستند، طی چند هفته گذشته تشدید شده است؛ درگیری‌هایی که آتش‌بس چهار ساله در جنگ داخلی یمن را از بین برده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/78267" target="_blank">📅 08:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78266">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ag6NoZSWDynvt-anH06d-SXZFVNdaVGkf6aNJKW56nLV53WC7kpdw5HUC_hDtTKg2V5A4DDDDopVd9HLtC1VP9rBD9vHUvPqXrRiA8P6nVn1SQPTTCki0ml3yfhItt6ShE3z1rOXNYZvA_paLW4zJoKXuCSEFHH_ycjyGrv2SKn34lK1QxVaEV4k71pN45bqrHZ0EZCgcJiYm1Arz1_cA-f1R7hhKbLzDMMo2DW46iRQm2laCInsUwG16JuMCROFU3VB-d28qNnmVq821BijRtR-reuPX751PTSMjqm5tjGvig8otquwZ_Fv3NTKl26HEJ7KTsTB5tuIyPMyZdzBTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
وقتی ما در جنگ با ایران پیروز شویم، قیمت نفت به‌شدت سقوط خواهد کرد؛ درست مثل هر چیز دیگری که دارد سقوط می‌کند (اما بیشتر!).
بنزین گالنی سه دلار، اما در نهایت به زیر دو دلار در هر گالن خواهد رسید.
همه این‌ها به‌سرعت اتفاق خواهد افتاد و ایران هرگز سلاح هسته‌ای نخواهد داشت.
MAGA!
رئیس‌جمهور DJT
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/78266" target="_blank">📅 04:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78265">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/980dd40283.mp4?token=qqanxFtcnDB36RgLI5FYTit9ezuuBJJXkjsqW-Qp20lVWsBGG3W8whJ1m8VjBwpAvYX2RqEi7OBh4eKPAY5UbB7mhrKgPESaqpWKQIfQZ_txIdaw4lfqPSRU_wqR0hHH-yUIHvrklfa3p7h2Do6XFE7f_Lx0hVHKUEiWFWsd0OPsV7fz1jit9Sp2blwkvBjfwn2QA3T6fLvyM4Ibcv37IiwfqcfWoG3rgSwQ_g84aZ2ZmSvrRapcka-a4UL-iSBV0y5Mgyhkeff2jA9NHViIQEufwKQrAERONDR2yLHAFkajDtQ77GymizRq_DtOq9lu-hEzNOEIZby9Kd4jYD_VRA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/980dd40283.mp4?token=qqanxFtcnDB36RgLI5FYTit9ezuuBJJXkjsqW-Qp20lVWsBGG3W8whJ1m8VjBwpAvYX2RqEi7OBh4eKPAY5UbB7mhrKgPESaqpWKQIfQZ_txIdaw4lfqPSRU_wqR0hHH-yUIHvrklfa3p7h2Do6XFE7f_Lx0hVHKUEiWFWsd0OPsV7fz1jit9Sp2blwkvBjfwn2QA3T6fLvyM4Ibcv37IiwfqcfWoG3rgSwQ_g84aZ2ZmSvrRapcka-a4UL-iSBV0y5Mgyhkeff2jA9NHViIQEufwKQrAERONDR2yLHAFkajDtQ77GymizRq_DtOq9lu-hEzNOEIZby9Kd4jYD_VRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجید ابن‌الرضا، سرپرست وزارت دفاع، مدعی شده است که نیروهای نظامی این کشور توانایی هدف قرار دادن ناوهای رزمی آمریکا را دارند.
روز گذشته محسن رضایی نیز گفت: برای اولین بار موشک ضدناوشکن را بالای سر یک ناو آمریکایی آزمایش کردیم. این موشک خاص، جهنمی برای آمریکایی‌ها به وجود آورد و فرار کردند.
فرماندهی مرکزی ارتش آمریکا - سنتکام - روز گذشته در
پستی که در شبکه ایکس منتشر کرد
تلویحا به حمله به دو ناو خود اشاره کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/78265" target="_blank">📅 04:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78264">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VmVnE2Q16F-LI_mbTcYEbtQQlWc8qG3BKUESHTBBynVG2CglbeNguIYUr-I9-GmZdnMw4cSO874F5pjs7AjsskpF6axsIUmitucA676ibn2nf5gGWcb41Bwrj1Fpxy-Of737EGXUgNEKfFQyOd52VugWBLyS6Y1COGMNLdv88FwxOvpBhvIMrx18_EkfyAanDHVBDU6A3uCt8jvnXHRtKFC8w5Kf93iVOYrVDnUD3EdHV7_l3Jc8xkdh5azR7uBVSqK1tUDJhE9zGnVhxxoCAa0vcp-8AliI3a1xhUJ_M4kFRQ8HcMrwtgXdPj9EeliEfGAV9mTcf_AVIgBCKHIjzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانیال کریمی، پدر امیرمحمد کریمی، از جان‌باختگان اعتراضات دی‌ماه ۱۴۰۴ در مرودشت، روز ۱۵ شهریور به زندگی خود پایان داد.
امیرمحمد کریمی، فرزند ۱۹ ساله او، ورزشکار و عضو سابق تیم ملی نوجوانان تکواندو ایران بود که ۱۹ دی‌ماه ۱۴۰۴ در جریان اعتراضات مرودشت با اصابت گلوله کشته شد.
پیکر او در روستای جونجان از توابع مرودشت به خاک سپرده شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 423K · <a href="https://t.me/VahidOnline/78264" target="_blank">📅 19:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78263">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AclD2VUgTEvOzAhrwYY77G6B81RMhvEWPyQ3NQLJ3wEntX5guYz-F5A0bXOVZgEColp_U-TOaKevVQXWv-lWONuDf5PMq4aockjBMinz2omXjxqpb6wwuSVuBV-dfpM262FHs4Vu9g3KUF0oqx4_lMDY0Dd8bfe_O7fK8qrTnBOZvFPeGVS6DodxYKRP27TprQ8UwzjTUGOtuwt-UDpltBrzrCgvS_4tw_ilIGIw7xuitptTw1kRvBHZfL8nmf2cZxx8sAmfDksnHBvbLKEQvcS1K1fJD5OM04b4_mIg5wsoba2Kjb6ONVVyrHKkUtlWJgzQl6oxARXTY1hM3gZ0uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیدا حیدری، نامزد ابوالفضل سلیمانی الموتی، از جان‌باختگان اعتراضات دی‌ماه، روز پنج‌شنبه ۱۲ شهریور ۱۴۰۵ به زندگی خود پایان داد.
منابع حقوق بشری ایران، به نقل از خانواده آیدا حیدری نوشته‌اند که این جوان ۲۵ ساله، حدود هشت ماه پس‌از کشته‌شدن نامزدش جان خود را گرفته است.
خانواده آیدا حیدری گفته‌اند که آیدا و ابوالفضل قرار بود همین ماه مراسم ازدواج خود را برگزار کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 429K · <a href="https://t.me/VahidOnline/78263" target="_blank">📅 19:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78261">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eP2UenuQc3J4lILfUbVdLr5ugVnp2rlv1w-x6YK7oItqqDB0t8MyNzWbfZgVznHcYkYKOImLnAT3XdHdiFy6_nIRjqDwaVprM1c7w36ATzpvNA2s_OKAgBcGP5p4vvZN9kwjsYbgITDfokzCLIlWSHcV-xe21Dve1lKfxADVpczVr9hPdhIaSx8hFVJneVZzvNq7PW91YCMzGvZZxFX3WS0TGb1RdbV5SuOttjEiFMk9rqh2mMSNuFJWrrj-MsSswxQw_oK8bAveA0w_t1lehgbR_MulCYucR3uU_mvQt9knVs5PMa8g9VuAym-i9BQn11ML0Ib1KGM4q1KrZtRvpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ تصویری ساخته‌شده با هوش مصنوعی از حمله جنگنده‌های آمریکایی به جزیره خارک در تروث‌سوشال منتشر کرد که روی آن عبارت «خداحافظ خارک» نوشته شده است.
realDonaldTrump
رییس‌جمهوری آمریکا چند تصویر دیگر نیز در این شبکه اجتماعی منتشر کرد؛ یک نمودار آماری که روی آن نوشته شده «ارزش پول ایران از بین رفته است»، دیگری نموداری که روی آن نوشته شده «ایران با یک ابرتورم مواجه است» و نمودار سوم که روی آن نوشته شده «صادرات نفت ایران سقوط کرده است».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 436K · <a href="https://t.me/VahidOnline/78261" target="_blank">📅 22:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78260">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer">👁️ 423K · <a href="https://t.me/VahidOnline/78260" target="_blank">📅 22:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78259">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bhwr5db0QObNGjTGEdNNG5axkyAbUgCWTCo9_jc1WisCpkOYl7ZQnquBvHPo3r9HFln5h9JlbsWFgURHRXusBOULSslEHa9ZNx7RX8NdgL7EaZUreJEDM3NQrDrG5XaFkRZ1akTGOKc79Bh8Da5c9qXUZf8_xj6S7VVnYm-IvqYWUrPtzkJVK8KqKOFLgeCocAhVUnZpclqXNEshK7sfDcskW7qNaixyvBLkGTqx6o4GBlFPBRi5iJspb1L0cRbZ00wZaGOPSL1a7AJSubZR_8cPOOJ3OjmauXE2nLUsUsGh8SLU-Tl5iQvGFbmZWRP2SNfGaZSwc2yafY2Kth1CBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 419K · <a href="https://t.me/VahidOnline/78259" target="_blank">📅 21:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78258">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4f1fd10186.mp4?token=jKfyBeLlLPk9bca0wi8cL0TtsnCC9D_kJbKydOx3515lD4wVrsspF8Eqa1nw6ixAikOC_ju0hQBMs7y9U7ARtZ2bpdEZ2hN5IP0tkCMtiiLgRobXMWm12MZQvIJPwc-f591g9veakUtRwheS-UgyEAC7Up2PFvfEfOinZ34hwOLnd5mSenu2ZmoEeHYMRFWkqOpGF1IpEe9Tiu7cFb4HPTP_9pTDY2GFmDsmbQORRp1IuT5WWaY1e93ToFoY3hXIVUslqnvEYqQWeATGHlhbwtXZZ8nStkrvr3wrHoZVpoVJ4u_DpuGA1eSd7aR2R11s-Wg-XEG30K5LpWqhNXmA5A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4f1fd10186.mp4?token=jKfyBeLlLPk9bca0wi8cL0TtsnCC9D_kJbKydOx3515lD4wVrsspF8Eqa1nw6ixAikOC_ju0hQBMs7y9U7ARtZ2bpdEZ2hN5IP0tkCMtiiLgRobXMWm12MZQvIJPwc-f591g9veakUtRwheS-UgyEAC7Up2PFvfEfOinZ34hwOLnd5mSenu2ZmoEeHYMRFWkqOpGF1IpEe9Tiu7cFb4HPTP_9pTDY2GFmDsmbQORRp1IuT5WWaY1e93ToFoY3hXIVUslqnvEYqQWeATGHlhbwtXZZ8nStkrvr3wrHoZVpoVJ4u_DpuGA1eSd7aR2R11s-Wg-XEG30K5LpWqhNXmA5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نرخ سوم بنزین به ۱۰ هزارتومان افزایش یافت
فاطمه مهاجرانی، سخنگوی دولت گفت نرخ سوم بنزین از بامداد ۱۷ شهریور به لیتری ۱۰ هزار تومان افزایش می‌یابد.
سهمیه ماهانه ۶۰ لیتر بنزین با نرخ لیتری ۱۵۰۰ تومان و ۵۰ لیتر با نرخ لیتری ۳۰۰۰ تومان بدون تغییر باقی می‌ماند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/78258" target="_blank">📅 21:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78257">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gb36LEmZfgoEaEiZmx6DEPBNFa5XBDMxt9lPZxdWT3IGVK2bkL2Y-WmQIrhOg9WXZ88Qqc6o9WO9lhrdxfN_Z4AE160nClb2hDgMf9QBr54CTt9Jn_W69SLuZzCoM3ENqeTRatlpnLsV3_px1uXPEjlPs78fToZZJ_4hSxTmxY_dmWJRXUKK3Oqngv4MDspPxq-4XpAYAhs1jC8hRsehz7A_acU8CtzOGgE76miFTGgZM-XCWD8pySZwnlxBYsh30RdHcy3POMpRibixWQWNVhOBBKLArsZQMQ44F5yoWNe58RYbOkCHWwRTRxqkQKqvqaK0VN21itadDTBpdSoQsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که سپاه پاسداران، بامداد یکشنبه ۱۵ شهریور ماه در بیانیه‌ای
اعلام کرده بود
یک شناور بدون سرنشین سنتکام را در تنگه هرمز هدف قرار داده است، ارتش آمریکا این ادعا را رد کرد و آن را «دروغ محض» خواند.
رسانه‌های دولتی ایران گزارش داده بودند که این شناور بدون سرنشین آمریکایی قصد ورود به منطقه‌ای از تنگه هرمز را داشته که ایران آن را ممنوعه اعلام کرده است.
کاپیتان تیم هاوکینز، سخنگوی فرماندهی مرکزی آمریکا (سنتکام)، در گفتگو با آسوشیتدپرس گفت ادعای سپاه پاسداران «دروغ محض» است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/78257" target="_blank">📅 17:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78256">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9239224ea3.mp4?token=u69Ta6nHaF_jwO9Ho_2my4V9w--x7L0U9KwT7LzORkGJ98A0-QlDIS6w2g4DVagz9AACjxIDc2ntb6WMDaHl9UcNTBdHn4vlrUoRCBIIZ4nhq-05vq_Kbjla2rsmH59Sl47eUv7RJtVGs7Fmou7cv2-iwlF5ajfaSLxqwaww2rnlQxKr2fDQWhGWNOa_9vxjBcTWT9_-fW9UPvkR4UCWX0Xl5Q5CNayE5JsgJtOppHLt12FxHJEI3668L218OoaoBREVNO74cIXx6b0w4SUbEpwJQ0RXXQIw7pzZbzSaYvWAK6GpR_690TRz3lrW0-TjmcZf2AXxmZ_JMBZHeEmQww" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9239224ea3.mp4?token=u69Ta6nHaF_jwO9Ho_2my4V9w--x7L0U9KwT7LzORkGJ98A0-QlDIS6w2g4DVagz9AACjxIDc2ntb6WMDaHl9UcNTBdHn4vlrUoRCBIIZ4nhq-05vq_Kbjla2rsmH59Sl47eUv7RJtVGs7Fmou7cv2-iwlF5ajfaSLxqwaww2rnlQxKr2fDQWhGWNOa_9vxjBcTWT9_-fW9UPvkR4UCWX0Xl5Q5CNayE5JsgJtOppHLt12FxHJEI3668L218OoaoBREVNO74cIXx6b0w4SUbEpwJQ0RXXQIw7pzZbzSaYvWAK6GpR_690TRz3lrW0-TjmcZf2AXxmZ_JMBZHeEmQww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف: قاعده بازی عوض شده و دوران پاسخ متناسب به پایان رسیده است
رئیس مجلس شورای اسلامی روز یکشنبه ۱۵ شهریور، یک روز پس از حمله آمریکا به چند نفتکش ایرانی در خلیج فارس، گفت دوران «پاسخ‌های متناسب» به پایان رسیده است. او همزمان به وجود مشکلات اقتصادی در کشور اذعان کرد.
محمدباقر قالیباف در سخنانی در جلسه علنی مجلس تهدید کرد: «هرگونه تجاوز به منافع و امنیت ایران، پاسخی سریع‌تر، سنگین‌تر و دردناک‌تر دریافت خواهد کرد.»
قالیباف که مذاکره‌کننده ارشد جمهوری اسلامی در گفت‌وگوهای بعد از آتش‌بس با آمریکا است، در بخش دیگری از نطق روز یکشنبه گفت: «نوسانات شدید قیمت ارز، تورم، بیکاری و مدیریت بازار، چالش‌های اساسی هستند که به معیشت مردم فشار جدی وارد کرده است.»
او افزود: «در کنار میدان نظامی، امروز اصلی‌ترین نبرد ما در میدان تولید و معیشت مردم است.»
این سخنان یک روز بعد از آن است که قیمت دلار در بازار آزاد ایران تا مرز ۲۲۸ هزار تومان بالا رفت و از سوی دیگر آمارهای رسمی نیز نشان‌گر افزایش شدید تورم در ماه‌های اخیر است.
علی مدنی‌زاده، وزیر اقتصاد ایران، نیز روز یکشنبه گفت واکنش تهران در برابر تشدید فشارهای اقتصادی آمریکا «مقاومت اقتصادی در کنار اصلاحات اقتصادی» است و این دیدگاه را که تحریم‌ها باعث تغییر مسیر ایران خواهند شد، رد کرد.
او با اشاره به اظهارات مقام‌های ارشد دولت دونالد ترامپ درباره اقدام آمریکا برای قطع رابطه ایران با اقتصاد جهانی گفت: «تصور اینکه بتوان با فشار بر اقتصاد ایران، تصمیمات یک ملت را تغییر داد، اشتباه است.»
وزیر اقتصاد ایران افزود: «مسئولیت اصلاح اقتصاد ایران بر عهده دولت و مردم ایران است، نه وزارت خزانه‌داری آمریکا.»
این در حالی است که همزمان وزیر خزانه‌داری آمریکا اعلام کرد ترکیب محاصره دریایی و تحریم‌های گسترده، صادرات نفت و دسترسی جمهوری اسلامی ایران به درآمدهای آن را به‌شدت محدود کرده است.
اسکات بسنت در گفت‌وگو با شبکه فاکس‌نیوز که روز یکشنبه منتشر شد، با اشاره به نقش چین به‌عنوان خریدار اصلی نفت ایران گفت محاصره دریایی مانع خروج محموله‌های تازه شده و برآورد کرد که «احتمالاً تنها حدود ۳۰ میلیون بشکه نفت خام ایران باقی مانده که چین هنوز نخریده است».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/78256" target="_blank">📅 17:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78255">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B7pKqzv8_rqj2B_SFMqzf5tyTadk_xmODPxB-QdWqf8MZSRsWqd_Cr8pIj4RjQV7uJtaHwhn7wiLdVYHxEY9ZG_o84u1oRSVn4tg7A56VGmaCxxoK2B7NRLlE0FRwLrUdwiGGoZMK96enQepjT9dFr0kODtWOjcYV3tHd1PUj9B619g-dDY2FEAuYRaAkKNbvjvOmlNBG1ckHp-Nq9UOL7_dOECupdj5alL6zCIANOY4Iwr0IUVB8wDltGT4C-FrEVvdbbirR0DFb1kHLjKZ7kyMHeZvriCnfZWVMSgdjBrpM-y3NtCRduz74lvnPFNJOtEb2STvWTljYMw-sda6Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت دلار در بازار آزاد ایران پس از عبور از مرز ۲۳۰ هزار تومان، به کانال ۲۲۶ هزار تومان بازگشت.
بر پایه گزارش اقتصاد۲۴، نرخ دلار صبح امروز یکشنبه ۲۲۶ هزار و ۱۰۵ تومان بود. وب‌سایت‌های اطلاع‌رسانی طلا و ارز پیش‌تر برای ساعتی از جهش قیمت دلار به بالای ۲۳۰ هزار تومان خبر داده بودند.
بهای دلار در ادامه با شیب نسبتاً تند عقب نشست. اقتصادنیوز این افت را به ورود بانک مرکزی به بازار نسبت داد و نوشت این بانک به دنبال جذب نقدینگی در بازار است.
حواله دلار در مرکز مبادله ارز و طلای ایران نیز ۱۶۰ هزار و ۹۸۳ تومان اعلام شد که شکافی بیش از ۶۵ هزار تومان با بازار آزاد ایجاد می‌کند.
حتی با احتساب اصلاح امروز، رقم کنونی نزدیک به ۱۰ درصد بالاتر از آغاز هفته گذشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/78255" target="_blank">📅 17:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78250">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MNubMhnu10y4mYKIZ9F0sf57SNANOozApA5Cl6ecVXya9xogJn2duvxhtW5CmMKmvAbmZY2jt_yBtDrc6p3ZxOk4sSslwCM2T3ruwqj0CPWK2Rbg1-e2EZtIduijSyqq9oA31GNVeYlO_4szczd-_az88RoucVlk1wMYf0uZYLZolLkDkpcoUo7p9Sa6K0ySvMcS0O9z8T-FWYh-i4Tchm3Sdd6Ni72gN4DLyFbzgPKknQtNwQOFltvzBMJACmjZbvMt6gdrUh_jWk8WGNEnXDFWW_xR5zLoq1XZbyTw-1S89kqfp8mHrpzoiIc6ozE0YYzLpuNAY4V4YabMNMkCBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JtEVvwW24orFyLD2w6KXeL51BPCnDJKv94ry937EnEDRYwfGwQyBHBFoA4U2TL8bIA-ak_tupY7VkSZyzLDtC4mOGvrJm0-jRIRDAZKi1Uup2Ftjy14vvhLsCQvf6QG9BV2DUvHyg8GtmVSBdRLs0LiqMm4qWm_CQ7oh-YEAcqC1GEUCZZsQTdZ2ZlHOg3nguwxrBpsTGhtzDQmBNbF6ScInyeJVV6ROfqva6GM9Mz1Jt9QPNaVlKGiMNQc0hb8FZnwRYAWa3GXa4f0VSktMYTNT-5DfmyTPl09F7aVgDrzIQV_8B1SPuTEHMC9wpKe-VUF5dj9pLnMh6vTW4Eynqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YMkRb0KcEaz0k7ik1WCuMLmPew_P0-Ezgbpav1usYZm-xIM9nrBkKMfQ8szfEP3ja_5K8wuMH9EttY_WoLSUusoYMwnE_7hm18N1W6Uf3WnqMmcjFGSZPiZIEbUjnU8jqPd6z0tpoSRQdX6D9Lst6HSjjaXaT90Q6XQmRoUX5w7GTxWakbYzsnOCVtkee0xIAZyXg981u-iUzSIFfRpUASwnw7KdW8ZxFUEvSjGoK2RhU2QeY_OlWpoD9DZ4hXro4gNR6n60LzMntee_hZqYSW9s7PJLEJ4pO2vgRxJ65eJZNq2Vh_4oCxmOPcHectmugmbGJQqB7YxcmWhivkRwsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FM_roVg9DE_XQQzYLwmkPzzjcWeLHjq5r-TDYK9cT38xU8dDLVuviF10jx_-ZYvN_pNw33tAWQOEX0Nk6K_g1CUvKVEJgj1McSfNtjIAL2vgq1El_1GK08stdT0CF_G7kyM_0663g2ZmcEz3f_yB5gfzUGiHvw-q8DUiIMCWGDXYfLkeICbq9xh4CqGbSWrnZudRI1KXssKBtGSg-9AEOd6Ly0tZAOAuQvWRTWH_yEKOxlEJxg1oGkVcy6ewun2vi9i-todERXMwr7-hzHuVv4qxlYTX2sBOUg2AyVUO3x0HeVndEefAHKd29LXfSr4myncCJzoVot6-EE45wDJ3Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RmVpfAe7Fadpqk4jFLmJFCAy49UKKINyR5J24R2iSHNjhjq8o6C0bfM-Bq2NIsDMf3uRCs-DlcLMKGzU-XsbFhTTs9HoehKZj7o4bZuIn5FwB9Q8JHrxfdbdPGtxozjfQgUmHTLboMMvVHE_Y6m74F0-PDM2b0riS86RElEExC_Lm-hsitX0Douqho3xs1Hi9DsqZuoWcDxLmSoY9RwRXzbyKwn612sD4ilWOeAbGYzEFDSxzezzC4Rls2LvPBdsNNujnw3oCuTOX-x2hn0OEvJmH6e44P36Ag7dMGAsLqN0dvELmvHhhQ0k1_8L7RkyWxApGLRME0Fyk0Xbm2GjuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">BadAngel66636
آرمین تیموری راد ۱۹ ساله
پدرش: امید تیموری راد ۴۷ ساله
عموش: امیر تیموری راد ۴۲ ساله
نوشته بودند ۱۸ دی در فردیس کرج به دست ماموران سرکوبگر حکومت کشته شدند.
روی مزارشون نوشته شده ۱۹ دی
و نوشته بودند:
به جز این سه نفر، همسر امید تیموری‌راد و مادر آرمین هم در پی اصابت گلولەهای جنگی، بە شدت مجروح شدە است:
@VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/78250" target="_blank">📅 17:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78249">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iOenC_orqfnxUmAXEBKAMfXuv7vi5-F8scsCJAhyBicq7ftctv38XGXwflkcA7NXJhxT0GibS1JKdjnypzTprWxHmWo6HsHKLr5wiEKWVWAtuHC_Vp3aFdlwhWlBPLp0DiA4dnP8oHZXRmM3BUtlL60XtkYSyiB-E9qY6qedPR9n04duNM8qB5W4XsurQKzqJA_QvXT31MmXQfufxFyGeogaESzy8ClDnqWxTIZ5pEc2eL7DBTUJh2pQ396eKWK-zIpb8Ez5ywRANCJckWQe_n3IUqQ85S88Xckved1vjC0hWm-oVtu_nXMfWKMWSmKwA5HOokI7ZvZQBDDPtc3ftQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران می‌گوید یک فروند شناور مدیریت‌پذیر از راه دور ارتش آمریکا را هدف قرار داده است.
روابط عمومی سپاه پاسداران در بیانیه‌ای اعلام کرد که این شناور قصد ورود به «منطقه حفاظت شده» تنگه هرمز را داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/78249" target="_blank">📅 09:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78248">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5782c4c6b3.mp4?token=K8HC_-LiwN1QV-sAQ_AiOtgIJV7WmSPbRChrGKBh1CP1GSLKz4Dwuqvw4yKM_lWUdNVfyG1A75vEUbiIBCuXscM7M2uSMHjz6sdlovWzpSoy6GRZpDtZ_z4NycR0KpRn8jhu9QZXUbUx_VOFEb2iH6LbcwAs92IgboeuBm0cz5CtXc6c7N8oG9vcB6ZoDfI1O1F4mZu9-MH0tSpYPOXLCn2USptl3QqNb88dyRnSQLZpwKHVx7We0dWSvKtOaOqWc58sUGTuQ3OjANVZHUNDqgu4_Gf9M8gFbkwVIJZQRSEa8cnD9EV6fDqkXFlsYe8y4sb-TyZj56avdUXLqwxjpg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5782c4c6b3.mp4?token=K8HC_-LiwN1QV-sAQ_AiOtgIJV7WmSPbRChrGKBh1CP1GSLKz4Dwuqvw4yKM_lWUdNVfyG1A75vEUbiIBCuXscM7M2uSMHjz6sdlovWzpSoy6GRZpDtZ_z4NycR0KpRn8jhu9QZXUbUx_VOFEb2iH6LbcwAs92IgboeuBm0cz5CtXc6c7N8oG9vcB6ZoDfI1O1F4mZu9-MH0tSpYPOXLCn2USptl3QqNb88dyRnSQLZpwKHVx7We0dWSvKtOaOqWc58sUGTuQ3OjANVZHUNDqgu4_Gf9M8gFbkwVIJZQRSEa8cnD9EV6fDqkXFlsYe8y4sb-TyZj56avdUXLqwxjpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اکانت سنتکام ویدیویی از غرق شدن نفتکش M/T Kylo در دریای عمان منتشر کرد و نوشت در قعر دریا به نیروی دریایی ایران پیوست:
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 413K · <a href="https://t.me/VahidOnline/78248" target="_blank">📅 04:48 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78247">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tM4soItAge92sIM7JzCUhzu4kXVKMFLakeMR3xm51RzxXcVAhsKbpoAbx5RTpMySSjJ6mZrvjQkTgy0FVxI4KCJY5gd3A1x8pYoVAkLH2PPYTYa3hyiIaCA7cRn7rBT8I2UxlWaNDgRCBFQr-JvNYUFRCvd7NAJRtTSmvjnifBOfeveh42G5X2OUUkLtb13cTwR20ml5H6PLjK_sncvRem_dqWP9inPDu_Q6tKsj_n3gOzzfEDhpNwEemw3f6AkF7rQGuGg2_MZNfzQOJrjpeqHWLjQV7ZnbpBroipOUtLlq62ejpPSsMZjPMAkOjG7T7RxOojhzAQjjYpx5IzUaeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی سپاه پاسداران، بامداد یکشنبه، با انتشار بیانیه‌ای اعلام کرد که نیروی هوافضای این نهاد با استفاده از چند موشک بالستیک، یک ناو هواپیمابر و یک ناوشکن ارتش ایالات متحده را هدف قرار داده است. در این بیانیه آمده است که این شناورها در محاصره دریایی و مسدود کردن مسیر کشتی‌های ایرانی مشارکت داشته‌اند و پس از این حمله «دچار خسارت شده» و «منطقه درگیری را ترک کرده‌اند». سپاه پاسداران همچنین با اشاره به تایید وقوع درگیری‌ها از سوی سنتکام، این عملیات را پاسخی به اقدامات نظامی واشنگتن دانسته و هشدار داده است که در صورت تداوم فشارهای نظامی و محاصره دریایی، پاسخ‌های نظامی گسترده‌تری متوجه نیروهای آمریکایی خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 421K · <a href="https://t.me/VahidOnline/78247" target="_blank">📅 02:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78246">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQ8TMJMtvliiapEwFO0EKb7mfiWLGwUBj8xRPm4L3iNzu49NYR3QncgOJwDCkFUsOFmYmMyWIEIuPDeRGreM_ddYetDG7i6TCpzLg54FUyLuTd141YpyzzISsIChTcCZBE_VpVQWod67TEFQoEObzzYW3lbzzXOx2rLMAe5CifvXdsaTAJwgU4ovulmBH0T5V_j_judm0nbE6mmRi9fmfPeUmlOrEQKG1PCvP3jxle-16lgU3SmNIKRXFvpsPGVr7aU9Vrr44AIx8d2lp-Xv38NEB5tM2FMa8X502pKgdeCwSxYlbpUq-pTfuzu8bB9jaVqebqY0PnCCMtuuFcIEqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش خبرگزاری تسنیم نیروی دریایی سپاه پاسداران انقلاب اسلامی روز شنبه در بیانیه‌ای اعلام کرد که سه نفتکش را که از «مسیرهای غیرمجاز در تنگه هرمز عبور می‌کردند، و همچنین سه شناور دیگر آمریکایی را در مناطق دیگر هدف قرار داده است.»
نیروی دریایی سپاه در این بیانیه به هدف قرار گرفتن سه نفتکش ایرانی توسط نیروهای آمریکایی در صبح امروز اشاره کرده و گفته است که این حملات خساراتی به‌بار آورده است.
@
VahidHeadline
علی محمدی، معاون سیاسی نیروی دریایی سپاه، روز شنبه در گفتگو با خبرگزاری فارس، گفت: «در ۱۰ روز منتهی به هشتم شهریور، نیروی دریایی سپاه هر شب بین ۲ تا ۵ شناور متخلف را تنبیه و مجازات کرده و پس از آن نیز هرگاه اراده کرده با کشتی‌های متخلف برخورد کرده است.»
او گفت:‌ «حملات آمریکا کوچک‌ترین خللی در اشراف و تحمیل اراده نیروی دریایی سپاه بر این منطقه ایجاد نکرده است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 424K · <a href="https://t.me/VahidOnline/78246" target="_blank">📅 23:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78245">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0f413c1eb0.mp4?token=BzmstTtNEdpahSZNI5rpo7sEmHwJY1gOGY34Rw3woC7UllTY2W_4mz2xsYfYRuC5qgF64K0VmyR-P3EUxdd3e7eway6dlvVcIDByHiOAJhjme0jGIcmzfLDScJ_rN9n2wvkMPWq-jaVnrZ-UqCSuN1-RkKniy--aLs9NEMirHAd_qhvuJvWuIvlmLPvOQP3uEbbRflBficdO_bu_8EN_kXgqgDigYR_Kx43shMdKM6lmma4h2iIGrMWG859XnL5zG2_m1AiWr46tMMOfgSZtjCiW961gjSRmDI5CdIiwXNxqC_zT5oKsb4sIij-llkI6QEU6BtwcnyjHK6vyBX6o1w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0f413c1eb0.mp4?token=BzmstTtNEdpahSZNI5rpo7sEmHwJY1gOGY34Rw3woC7UllTY2W_4mz2xsYfYRuC5qgF64K0VmyR-P3EUxdd3e7eway6dlvVcIDByHiOAJhjme0jGIcmzfLDScJ_rN9n2wvkMPWq-jaVnrZ-UqCSuN1-RkKniy--aLs9NEMirHAd_qhvuJvWuIvlmLPvOQP3uEbbRflBficdO_bu_8EN_kXgqgDigYR_Kx43shMdKM6lmma4h2iIGrMWG859XnL5zG2_m1AiWr46tMMOfgSZtjCiW961gjSRmDI5CdIiwXNxqC_zT5oKsb4sIij-llkI6QEU6BtwcnyjHK6vyBX6o1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس مرکز فوریت‌های پزشکی استان کردستان اعلام کرد که در پی آتش گرفتن یک تانکر حامل مواد سوختی در محور سنندج–همدان، دست‌کم ۱۱ نفر جان باختند و پنج نفر دیگر زخمی شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 411K · <a href="https://t.me/VahidOnline/78245" target="_blank">📅 20:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78244">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EMezkFYtGDC6IamY3EGHTNpa0knQm3tHgSJRUR0fNphZ7rHOiUNxw0oF-7jiX14Ep_SnJs8Ncax7b9JQXE72xk4ISCbJQkbVzDfiq1bR7OJEf16qNgJgS95sNcnxi03VeoKsBefl-oMsRGZKiFXgLzlsA91yDbzYVpI3n1XvuMI6NfhqBiZSg8VsqtThPLIhSm_qytH0PcPkqhQwkgOnHPAI-iCkcA7vv-QnBIbO2t-0uAWi9gHHnLWBhHroDHoB3EfMgEcAsvvRLVL_PJRCKEdBrIZvNdjm2l9CWhHj1GOi18UV9Lx-l4UWA2cGquceNgMVJOLHQYXs2aPotx9k5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا  گزارشی درباره چندین کشتی تجاری در شمال خلیج فارس و دریای عمان دریافت کرده است.
گزارش‌ها حاکی از آن است که این کشتی‌ها در چارچوب فعالیت‌های نظامی جاری در منطقه، هدف آتش با هدف از کار انداختن آن‌ها قرار گرفته‌اند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/78244" target="_blank">📅 19:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78242">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرانه‌ها(مهدی محمودیان)</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jp9ntzI50tEqjKstVTGzpoOZp8rFOfA8BzASGUmwJeJ3vnkHLjAm5cSSkFJG-Up-ramaOSTOTNBcspS5ON6C5hOEPnsrz5UkfRmEHamCf8JJt0RK4NqvF_pnlqw1BwNk6QqFTG9oCu_QBqqZS7A3LFpVzz6p21GYtkaaDJErNZ_OhmNx7NIrc5JKvhXdNm3jscNJV8rhpVchNwdg_smdyiOtOM5sllYyUBisvz7PS5CoQOH5PnTz2D9svAnNGb63I9NOJRqgOwgAKllPD-GVdyf2h6siwoXUUtOZsc8_7Nz_Hnf3bGVBlFCc4Nuh2-xjZZmS8OTU8tLWGnVklzaHlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M-yz1mfvZ0xwH7hNDFqz4B8s7GrxUIl7_Zp0XmIFVZf-UJVQ3hF2Cx4WMbCLJpYFuhF5PL7KD5cfViK2MWH-9tZB8ol36i0n6Ioa2pMrk1SvWPlvyhrt_PXtOZClihGuBDC3BA8xey0pOR2w3T_fcWX5hdUsmdF5LkjCcugt44yyuWd7s6PXOCZcV_OPXoQ5Vyw-u-0t_xVBPwAhAQC7Q7m_jgbXZP7kJKgTQHUOYD8mD45hPqgIqPuwjBe-AqZAYiVIvlNNkuaZABpB1mruV9QeK3X2aNHcIFc-22UuXz7uspTgkMNDacaE33J5xiQ6JMhupOPCgYybejFrsylMSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❇️
مادر دو معترض جان‌باخته، در لاهیجان بازداشت
🔹
مادر دو جانباخته اعتراضات ایران نزهت میرراضی، معروف به «مامان نزهت»، مادر علی و عماد شوش، دو تن از جان‌باختگان اعتراضات سراسری ایران، روز جمعه ۱۳ شهریور در لاهیجان بازداشت و به مکانی نامعلوم منتقل شده است.
🔹
نیروهای امنیتی نزهت میرراضی را در حالی بازداشت کردند که تاکنون اطلاعاتی درباره نهاد بازداشت‌کننده، محل نگهداری و اتهامات احتمالی مطرح‌شده علیه او منتشر نشده است.
🔹
بازداشت این مادر دادخواه یک روز پس از آن روی داد که او با انتشار ویدئویی به پیشواز زادروز یکی از دو فرزند کشته‌شده‌اش، عماد شوش، رفته بود. خانم میرراضی همزمان با افزایش فشارهای امنیتی در استان گیلان و جلوگیری نیروهای اطلاعاتی و انتظامی از برگزاری مراسم زادروز هومن صباغ بر سر مزار او در لاهیجان صورت گرفته است.
🔹
نزهت میرراضی در دو دوره از اعتراضات سراسری ایران دو فرزند خود را از دست داده است.علی شوش، شاعر، بازیگر تئاتر و نوازنده اهل لاهیجان، در جریان اعتراضات سراسری «زن، زندگی، آزادی» در سال ۱۴۰۱ جان باخت. هه‌نگاو می‌گوید او در جریان اعتراضات در اصفهان به دست نیروهای حکومتی کشته شد.
🔹
عماد شوش، برادر علی، نیز از اعضای فعال خانواده‌های دادخواه بود و بر اساس گزارش‌ها، در جریان اعتراضات سال ۱۴۰۱ سابقه بازداشت داشت.
🔹
عماد شوش روز ۱۸ دی ۱۴۰۴ در جریان اعتراضات در لاهیجان بر اثر شلیک مستقیم نیروهای حکومتی و اصابت چهار گلوله جان باخت.
🔹
در هفته‌ی گذشته نیز جعفر پناهی به دیدار مادر این خانواده رفته بود.
@MahmoudianMehdi</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/78242" target="_blank">📅 18:14 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78241">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1d8dfb05eb.mp4?token=nKksOWEUFcK_oXnMTgzqbCCUwzF5YW95mG7DbgDdHraW2qxUh4eWLS14oiVH1KAdEbWq71Zu9wqeE_NYxQzQvKYESIMwPJLEDMvcMbZk9m9NGG-UzN6lHXz9zN8ir9gRgvXjkKrTFiHT-GmPYMedm1eR91xcabwpBIFK7A7Cy9IU35mF1tWJ1P1k1jLexVP8MTA-Ll0WeRhvVY6DKJsEzvmELApCSbax_hnvycjp7tYzhzfOwhf-QvSMb5vB9o48GmB4yJNpqJ3WJyV0wWAUU1SzR-7z1aNXh5e17jWHZj18bX2Khj-O56WH-I-0Cb9oi8Yk-xVeNbANPfCajbcD0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1d8dfb05eb.mp4?token=nKksOWEUFcK_oXnMTgzqbCCUwzF5YW95mG7DbgDdHraW2qxUh4eWLS14oiVH1KAdEbWq71Zu9wqeE_NYxQzQvKYESIMwPJLEDMvcMbZk9m9NGG-UzN6lHXz9zN8ir9gRgvXjkKrTFiHT-GmPYMedm1eR91xcabwpBIFK7A7Cy9IU35mF1tWJ1P1k1jLexVP8MTA-Ll0WeRhvVY6DKJsEzvmELApCSbax_hnvycjp7tYzhzfOwhf-QvSMb5vB9o48GmB4yJNpqJ3WJyV0wWAUU1SzR-7z1aNXh5e17jWHZj18bX2Khj-O56WH-I-0Cb9oi8Yk-xVeNbANPfCajbcD0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست اکانت سنتکام:
'
سنتکام پس از هدف قرار گرفتن ۲ ناو جنگی نیروی دریایی آمریکا توسط ایران، ۳ نفتکش سپاه پاسداران را منهدم کرد
'
ترجمه ماشین:
تامپا، فلوریدا —
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) روز ۵ سپتامبر، پس از آنکه سپاه پاسداران انقلاب اسلامی موشک‌های بالستیک به سوی دو ناو جنگی نیروی دریایی آمریکا در حال گشت‌زنی در آب‌های منطقه شلیک کرد، سه نفتکش حامل نفت خام ایران را هدف قرار دادند.
یک ناو هواپیمابر آمریکا و یک ناوشکن مجهز به موشک‌های هدایت‌شونده با موفقیت از چندین حمله بدون تحریک قبلی ایران گریختند. هیچ‌یک از نیروهای آمریکایی آسیب ندیدند.
پس از حملات ناموفق ایران، سنتکام نفتکش‌های حامل نفت خام سپاه پاسداران،
M/T Downy
در نزدیکی ساحل جزیره خارک و
M/T Stark 1
در نزدیکی جاسک را به‌طور دائمی از کار انداخت. نیروهای آمریکایی همچنین نفتکش خالی
M/T Kylo
(که با نام «Noxen» نیز شناخته می‌شود) را در دریای عمان به‌طور کامل منهدم کردند؛ این شناور پس از آنکه به خدمه دستور داده شد کشتی را ترک کنند، در چندین نقطه حیاتی هدف قرار گرفت تا غیرقابل استفاده شود.
این سه نفتکش ایرانی بخشی از یک شبکه سایه چندمیلیارددلاری هستند که منابع مالی سپاه پاسداران و نیروهای نیابتی منطقه‌ای آن را تأمین می‌کند. ایران هیچ ابزاری برای دفاع از آن‌ها ندارد.
دریاسالار برد کوپر، فرمانده سنتکام، گفت: «پیام به سپاه پاسداران روشن باشد: اگر به دو کشتی ما شلیک کنید، ما هزینه اقتصادی حتی سنگین‌تری به شما تحمیل خواهیم کرد — سه کشتی شما را از بین خواهیم برد. ما در دفاع از نیروهای آمریکایی تردید نخواهیم کرد و در صورت لزوم، ناوگان نفتی محدود و در معرض آسیب ایران را نابود خواهیم کرد.»
CENTCOM
دقایقی بعد در پستی دیگر:
«پیام به سپاه پاسداران باید روشن باشد: اگر به دو فروند از کشتی‌های ما شلیک کنید، ما هزینه اقتصادی حتی سنگین‌تری به شما تحمیل خواهیم کرد — سه فروند از کشتی‌های شما را از بین خواهیم برد. ما در دفاع از نیروهای آمریکایی تردید نخواهیم کرد و در صورت لزوم، ناوگان نفتی محدود و آسیب‌پذیر ایران را نابود خواهیم کرد.» — دریاسالار برد کوپر، فرمانده سنتکام
CENTCOM
پیت هگست وزیر جنگ آمریکا:
ساده است: اگر ایران به کشتی‌های آمریکا شلیک کند، ما نفتکش‌هایش را نابود خواهیم کرد (و غرقشان خواهیم کرد). تنها کاری که باید بکنند این است که شلیک به @‌USNavy را متوقف کنند.
ناوگان نفتکش‌های ایران بی‌دفاع است — ایران نه نیروی دریایی دارد و نه نیروی هوایی. هواپیماها، کشتی‌ها و زیردریایی‌های ما می‌توانند همه آن‌ها را، در حوزه‌های @‌CENTCOM و @‌USPACOM، هدف قرار دهند.
PeteHegseth
خبرگزاری صداوسیمای جمهوری اسلامی گزارش کرده که خدمه دو نفتکشی که امروز از سوی آمریکا مورد حمله قرار گرفته بودند «با قایق‌های نجات به ساحل منتقل شدند.»
براساس این خبر یکی از این نفتکش‌ها «خالی و دومی حامل محموله نفت» بود.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/78241" target="_blank">📅 17:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78240">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sj7M-TDLuAjhMr7wZiIzrIv8sM7aAPEPuqwaHcsG_nl--59wz3byHnXx5hqSEQIJa4dgDEH0j5OukUe-B__t6fvZI1tF6dFaG2BtH82_-twu8py5TEBamfyoA-ytaSHc_caPiZUqVSkMzUTPCkwOCWqqRDeQPX15dpu9PsRwZemHcllemKiPMDZAYFFb18uQyoKudtAvXBZDbJMJMAMhtcDFvcxtk7RBnBW2KSfaIuhq52rM8CTaVg5kCGUgD-T4w1jFfxvgirO0ZyOC9_ETxAa7O-igkqcTHkZyqSAE81bPm6QJAGI992ZhItwRy4ulm83UufGf9ouNgyBUTbHigw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت دلار در بازار آزاد ایران روز شنبه ۱۴ شهریور با جهشی دیگر به ۲۲۸ هزار تومان رسید و بهای یورو نیز از ۲۶۳ هزار تومان عبور کرد.
وب‌سایت‌هایی که نرخ غیررسمی ارز در ایران را به نمایش می‌گذارند، همچنین بهای پوند انگلیس را ۳۰۷ هزار و درهم امارات را بیش از ۶۲ هزار تومان اعلام کرده‌اند.
این افزایش مجدد تنها یک روز بعد از آن رخ داده که عبدالناصر همتی، رئیس‌کل بانک مرکزی ایران، کمبود جدی ارز برای واردات را رد کرد و کاهش شدید پول ملی ایران را ناشی از افزایش تقاضای «احتیاطی، سفته‌بازانه و خروج سرمایه» دانست.
قیمت دلار در ابتدای شهریور از مرز ۲۰۰ هزار تومان عبور کرد و طی دو هفته گذشته به شکل مداوم افزایش یافته است.
این در حالی است که همتی هفته پیش گفته بود ایران «به‌اندازهٔ کافی» ارز در اختیار دارد و بانک مرکزی در صورت نیاز آمادهٔ تزریق تا دو میلیارد دلار به بازار است، اما این اظهارات مانع ادامهٔ افزایش نرخ ارز نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/78240" target="_blank">📅 17:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78239">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MlBbgpXy0ClVunDJrNyeXZVH3NJ7SqdXf1nl_1xNj7YXCfZuctgysmhuRrEFUlDP7cATAyhx2dvCDyIHXox2BS4d2e_c2Rk0vVgVRmpuLmJORE7AahYOUq2mpHZMfQVwlUo4kv3fO2XV06X4QL4HCHCkyN32hJIb22-wBPxwKUmip9eczL3fs6xoc0P6t1fHdZTFVMBEHiz_YDZSwutnDSyg6ZSFAwu4fAhWgNpPRq-kvDmG0MCHJScmBNQcXRkHS-22cqNjepGjyrmEFqHbU8k3WrmxOn9ToSmjJHkey7NBHQ1mAiL-G4vJnmygyJesfyMyFl8UyEANrHKpaQ4ePQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه ایالات متحده روز جمعه ۱۳ شهریور از موافقت با فروش پنج میلیارد دلار بمب، کیت‌های هدایت و دیگر تجهیزات نظامی به عربستان سعودی خبر داد.
این وزارتخانه اعلام کرد این فروش، توان دفاع هوایی عربستان را برای مقابله با تهدیدهای کنونی و آینده منطقه‌ای تقویت و هماهنگی تجهیزات این کشور با سامانه‌های نیروهای آمریکایی و دیگر شرکای واشینگتن در خلیج فارس را بیشتر می‌کند.
عربستان سعودی از زمان آغاز جنگ آمریکا و اسرائیل علیه ایران بارها هدف حملات موشکی و پهپادی نیروهای ایرانی و حوثی‌های مورد حمایت تهران در یمن قرار گرفته است.
وزارت خارجه آمریکا کنگره را از این معامله مطلع کرده است؛ این فروش برای نهایی شدن همچنان به تأیید قانون‌گذاران آمریکایی نیاز دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/78239" target="_blank">📅 17:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78238">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/19446f537f.mp4?token=MTQh8MUHi7Babo6Evj0rsRSiNqvnuWePV9OEcCPmtGQbz1uBFoOgsLtU4p5RgItXxYw6V1MjO_p1rKVsXkUVf0ATA1UQIM4YOWeM-4Hh4yngfflK8VnN4Dees-53PbYRW8vlPndcTg1ZbGpMh_bPSaHYOgtxfgVB6OFFilK68iP25o8OuxqqXiQpXjTENmkSwWGQvPIN12MxS3L6GXVLhT5YWS-EOn51ohITI1PBO_zxbUDWgJit-90Xcj0avXDYMU1m9pzwrlvvR83umgnctpaJYS4Ra-4Ra9YkiLhwpeGSdNq5JYOprwZ8toU-oY0FYSfGEsTvfts7gWMJ0rA9Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/19446f537f.mp4?token=MTQh8MUHi7Babo6Evj0rsRSiNqvnuWePV9OEcCPmtGQbz1uBFoOgsLtU4p5RgItXxYw6V1MjO_p1rKVsXkUVf0ATA1UQIM4YOWeM-4Hh4yngfflK8VnN4Dees-53PbYRW8vlPndcTg1ZbGpMh_bPSaHYOgtxfgVB6OFFilK68iP25o8OuxqqXiQpXjTENmkSwWGQvPIN12MxS3L6GXVLhT5YWS-EOn51ohITI1PBO_zxbUDWgJit-90Xcj0avXDYMU1m9pzwrlvvR83umgnctpaJYS4Ra-4Ra9YkiLhwpeGSdNq5JYOprwZ8toU-oY0FYSfGEsTvfts7gWMJ0rA9Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های ایران از شنیده شدن صدای چند انفجار در نزدیکی جزیره خارک، مهم‌ترین پایانه صادرات نفت ایران، و هدف قرار گرفتن یک نفتکش کوچک ایرانی خبر داده‌اند.
خبرگزاری تسنیم گزارش داد این نفتکش صبح شنبه ۱۴ شهریور در شش مایلی جزیره خارک و در محدوده لنگرگاه، «هدف قرار گرفته است.»
تسنیم می‌گوید این هدف‌گیری «با چهار پرتابه نیروهای آمریکایی» انجام شده است.
به گفته منابع محلی، این حادثه تلفات جانی نداشته و کارکنان در حال تخلیه نفتکش هستند. وب‌سایت عصر ایران نیز اصابت چهار پرتابه به این شناور را گزارش کرده است.
خبرگزاری فارس پیشتر اعلام کرده بود که صدای انفجارها از محدوده خلیج فارس شنیده شده، اما نشانه‌ای از دود مشاهده نشده و منشأ صداها مشخص نیست.
نورنیوز نیز به نقل از منابع محلی، گزارش «حمله موشکی آمریکا به یک نفتکش ایرانی» را منتشر کرد، اما آن را تأییدنشده خواند.
خبرگزاری دانشجو هم ویدیویی را منتشر کرده که می‌گوید مربوط به این نفتکش هدف قرار گرفته شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/78238" target="_blank">📅 17:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78237">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9ee2041b46.mp4?token=LX3bov0oza96TCWplkIFtwm1b2insQHUoOY-lBhpcQvKOB4sGYfjWXWnBgGxgSzchummRlnukqtSck0h08tFP9OqGZCVnnD06jKl8uWXGIVY8A3HZtpkLvXWCg5FPy1Xbg4w48sb9BdwGLl6OwqYF58AsSpe41brSMWnAsSWM6Hoq8is89B9ET2S7w6CTZsXxdT4oSZV2IUPogOn5VuD9xAcNGa1DnfGSx0SYkeRRGmmsKUuRkGD9f0a8LnqgQHizPwrpQug0-ekZ7FjAOH_S7By5i2lo-rtgm3VN27rV9vZaHwSXxgEA3Wz5CTTZhQl7bNv66Z1qb77ubUMEt6Q9w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9ee2041b46.mp4?token=LX3bov0oza96TCWplkIFtwm1b2insQHUoOY-lBhpcQvKOB4sGYfjWXWnBgGxgSzchummRlnukqtSck0h08tFP9OqGZCVnnD06jKl8uWXGIVY8A3HZtpkLvXWCg5FPy1Xbg4w48sb9BdwGLl6OwqYF58AsSpe41brSMWnAsSWM6Hoq8is89B9ET2S7w6CTZsXxdT4oSZV2IUPogOn5VuD9xAcNGa1DnfGSx0SYkeRRGmmsKUuRkGD9f0a8LnqgQHizPwrpQug0-ekZ7FjAOH_S7By5i2lo-rtgm3VN27rV9vZaHwSXxgEA3Wz5CTTZhQl7bNv66Z1qb77ubUMEt6Q9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرتین خواجوی‌نیا، دانش‌آموز ۱۶ ساله رشته کامپیوتر، شامگاه ۱۸دی۱۴۰۴ در جریان اعتراضات مقابل فرمانداری شهر قدس، قلعه حسن‌خان، با شلیک گلوله جنگی کشته شد.
مادر آرتین ویدیویی از جمع‌آوری کفش‌های فرزندش منتشر کرده است؛ کفش‌هایی از دوره‌های مختلف زندگی او که حالا به یادگار مانده‌اند.
مادر این نوجوان کشته شده، نوشته است: «از اولین تا آخرین قدم‌های تو را مرور می‌کنم پسر قهرمانم. از لحظه‌به‌لحظه بزرگ شدنت حالا فقط خاطراتی برای من مانده که هر ثانیه از مقابل چشمانم می‌گذرد.»
«از آن نوزاد زیبا با آن لباس زرد در آغوشم تا آن مرد بلند قامتی که باید برای دیدنش سرم را بالا می‌بردم، تو همیشه یادگار مادر شدن من خواهی ماند.»
او فرزندش را «قهرمان جاودانه من» خطاب کرده و نوشته است: «هر لحظه و هر جا یادت جاوید و راهت پرنور.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/78237" target="_blank">📅 17:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78236">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 425K · <a href="https://t.me/VahidOnline/78236" target="_blank">📅 23:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78235">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C293vlrGsVDQk3ndERC21d6klKO6_RnpkZxNqnJ7dVRN8JGnYUq6KmXzr-86D5Kkw_EGY4NuY57enG7q_6flvrGk8SrBfMxb47ZyKo-mA2IIxktd_WQgEHUWNKpWYRpbSDekEiXOuK9_UtgvoxxQwlHcN_6aJfbAN2wAdJAJqL1esANQrq7J-8ovHBiAEPkX7utWqyQtanx0Qg3ZFL2KH2RJ-KKhcgsrS6J1QqkPgH957mN47FIQlXZIv7IPVVlcVED2D12zk-XRichbMZAtM0KHH64esSr8q39bMvWLcPlCbbhtqdF0ggSB9ZdA9EcgwlpBGMoFtKrYOWJSILo2Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده آمریکا همراه با بریتانیا، فرانسه، و آلمان در تلاش است شورای حکام آژانس بین‌المللی انرژی اتمی هفته آینده قطعنامه‌ای تصویب کند که پرونده هسته‌ای جمهوری اسلامی را برای نخستین بار در ۲۰ سال گذشته به شورای امنیت سازمان ملل متحد گزارش دهد.
خبرگزاری رویترز روز جمعه ۱۳ شهریور به نقل از دیپلمات‌ها و با استناد به متن پیشنهادی قطعنامه گزارش داد که چهار کشور در حال رایزنی با دیگر اعضای شورای حکام ۳۵ عضوی آژانس برای تصویب این قطعنامه هستند.
مذاکرات درباره متن نهایی همچنان ادامه دارد و پیش‌نویس هنوز به طور رسمی به شورای حکام ارائه نشده است.
بر اساس پیش‌نویسی که رویترز مشاهده کرده است، شورای حکام از مدیرکل آژانس خواهد خواست قطعنامه جدید و قطعنامه‌های پیشین مرتبط با برنامه هسته‌ای جمهوری اسلامی را برای اعضای آژانس، شورای امنیت و مجمع عمومی سازمان ملل ارسال کند.
در متن پیشنهادی همچنین بار دیگر از جمهوری اسلامی خواسته شده است موارد نقض توافق پادمانی خود را «فوراً» برطرف کند و اقداماتی را که آژانس و شورای حکام ضروری می‌دانند انجام دهد تا مدیرکل آژانس بتواند درباره صحت و کامل بودن اظهارنامه‌های هسته‌ای حکومت ایران اطمینان لازم را ارائه کند.
اقدام آمریکا، بریتانیا، فرانسه و آلمان ادامه قطعنامه‌ای است که شورای حکام روز ۲۲ خرداد ۱۴۰۴ تصویب کرد. در آن قطعنامه جمهوری اسلامی به دلیل همکاری نکردن کامل با تحقیقات آژانس درباره آثار اورانیوم در مکان‌های اعلام‌نشده، ناقض تعهدات خود در زمینه منع گسترش تسلیحات هسته‌ای شناخته شد.
یک روز پس از تصویب آن قطعنامه، در ۲۳ خرداد ۱۴۰۴، اسرائیل حملات به تأسیسات هسته‌ای ایران را آغاز کرد و ایالات متحده آمریکا نیز پس از آن به عملیات پیوست. بر اساس گزارش رویترز، تأسیسات غنی‌سازی اورانیوم ایران در این حملات تخریب شدند یا به‌شدت آسیب دیدند.
جمهوری اسلامی از زمان این حملات به بازرسان آژانس اجازه نداده است به تأسیسات بمباران‌شده بازگردند یا وضعیت باقی‌مانده ذخایر اورانیوم غنی‌شده را راستی‌آزمایی کنند. شورای حکام طی یک سال گذشته دو قطعنامه دیگر نیز تصویب کرده و از حکومت ایران خواسته است موجودی اورانیوم غنی‌شده خود را اعلام و دسترسی کامل بازرسان آژانس برای راستی‌آزمایی آن را فراهم کند.
آژانس بین‌المللی انرژی اتمی برآورد کرده است جمهوری اسلامی پیش از حملات به تأسیسات هسته‌ای، ۴۴۰.۹ کیلوگرم اورانیوم غنی‌شده تا سطح ۶۰ درصد در اختیار داشت. بر اساس معیارهای آژانس، در صورت غنی‌سازی بیشتر، این مقدار می‌تواند برای تولید مواد شکافت‌پذیر مورد نیاز حدود ۱۰ سلاح هسته‌ای کافی باشد. آژانس میزان غنی‌سازی ۶۰ درصدی جمهوری اسلامی را «مایه نگرانی جدی» دانسته است.
جمهوری اسلامی می‌گوید قصد تولید سلاح هسته‌ای ندارد و فعالیت‌های هسته‌ای خود را صلح‌آمیز می‌داند. ایران به عنوان عضو پیمان منع گسترش سلاح‌های هسته‌ای حق استفاده صلح‌آمیز از فناوری هسته‌ای، از جمله غنی‌سازی اورانیوم، را دارد؛ اما آژانس می‌گوید جمهوری اسلامی تنها حکومتی است که بدون داشتن سلاح هسته‌ای، اورانیوم را تا سطح ۶۰ درصد غنی کرده است.
رویترز گزارش داده است در سال‌های اخیر هر بار آمریکا، بریتانیا، فرانسه و آلمان پیش‌نویس قطعنامه‌ای درباره برنامه هسته‌ای جمهوری اسلامی به شورای حکام ارائه کرده‌اند، آن قطعنامه تصویب شده است. با این حال، اقدام عملی شورای امنیت علیه جمهوری اسلامی ممکن است با مانع روبه‌رو شود؛ روسیه و چین که از متحدان حکومت ایران به شمار می‌روند، از اعضای دائم شورای امنیت و دارای حق وتو هستند.
@
VahidHeadline
نمایندگی جمهوری اسلامی در سازمان ملل در وین اعلام کرد این اقدام آمریکا، بریتانیا، فرانسه و آلمان نشانه «شکست کامل توهم مکانیسم ماشه» است.این نمایندگی افزود این اقدام نیز «هیچ سودی» برای این کشورها نخواهد داشت.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 417K · <a href="https://t.me/VahidOnline/78235" target="_blank">📅 21:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78234">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E-RQnpkk-HStv6T7US9HygocS48x6du5NT_5yQEAMXQOXdwNQ1ngSVZJ7nyIM_av9Fnb36zXoFHZ83bG8VPiQYuMNJkr_Jfj54HhnrQeeaQDPEtEPNB97_ls2SKWlBm4XTlIs4zwaauFn9i0Mq_zdZMKEiPjP9_Q1QvoyLVz6eT_wuhaP7s5znNzbY1SnZ22crLPU0Q8R3G_pmVuaGrAs8obeSSpLB6Q4AByAnwG-3sWZ05KgVe63oGhBGhI-c5At8GCGfkSo8kZ0OwKQUaGhSkKtm9Hek3WKrmCYawbVffc3NRzU8G4S-xHwYxj7NDz2gxdhxOviC8J8eL11MpXyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العربیه شامگاه جمعه گزارش داد که موشک‌های پرتاب شده از سوی ایران، در شمال اردن رهگیری شدند. به گزارش این رسانه تصاویر رهگیری موشک‌های ایرانی در شمال اردن منتشر شد.
ساعاتی پیش از این گزارش، برخی کانال‌های تلگرامی نزدیک به سپاه پاسداران، اعلام کرده بودند موشک‌هایی از اصفهان، کرمان و کرمانشاه پرتاب شده است.
@
VahidOnLive
وزارت خارجه قطر جمعه ۱۳ شهریور در بیانیه‌ای اعلام کرد این کشور طرف درگیری نیست و حمله به خاک قطر را نمی‌توان توجیه کرد.
این وزارتخانه افزود موفقیت نیروهای مسلح قطر در رهگیری حملات جمهوری اسلامی، از خطر این حملات نمی‌کاهد.
وزارت خارجه قطر همچنین در این بیانیه نوشت «تاسف‌بار»است که با وجود مستند شدن رسمی حمله به راس لفان، وقوع این حمله زیر سوال برده می‌شود.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/78234" target="_blank">📅 20:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78233">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KuD8e9X8PetyDkb_Z3egyO4PFiqzV76TCP8NUf8r4uD9bBXuB9lBY78DU7x-auYWJRB2YNw5Uh4NZM_egZr6nMYEQMM0QsnkRTIQvH3EJORfeQ0n94o4oe2LQo95SEH2qpu6UVLsCHlNX3clXF00nt11taJ6Ni2PZAVVNKXwQWbE9fTKqxQVGS64D4M3hAXYP5WiuuM_Og7v9LEdnOjv5JWXtVle9ooA1_KAIC2stLUrfx0mFwOIfUfMDYoJijIpFO-_I5GHdBuwvbkBZmqhkmd1YOvs4zF6vH-KhhUVodkRrlNL9XeGNNw27d0vkcxs5u10F5mhaEt2hWb9IvaW1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا یک بانک مستقر در ترکیه و دو شرکت وابسته به آن را به دلیل تسهیل انتقال ده‌ها میلیون دلار برای نیروی قدس سپاه پاسداران و فراهم کردن دسترسی جمهوری اسلامی به شبکه بانکی بین‌المللی تحریم کرد.
وزارت خزانه‌داری آمریکا روز جمعه ۱۳ شهریور اعلام کرد «گلدن گلوبال بانک» و دو شرکت زیرمجموعه آن، «گلدن گلوبال وارلیک کیرالاما» و «گلدن گلوبال پورتفوی یونتیمی»، در چارچوب عملیات «طرد اقتصادی» به فهرست تحریم‌ها افزوده شده‌اند. هر سه نهاد در ترکیه مستقر هستند.
وزارت خزانه‌داری آمریکا همچنین در حساب رسمی خود در شبکه اجتماعی «ایکس» اعلام کرد این اقدام بخشی از عملیات «طرد اقتصادی» است و هدف آن قطع «شریان‌های حیاتی مالی» جمهوری اسلامی در ترکیه است. به گفته این وزارتخانه، گلدن گلوبال بانک و شرکت‌های وابسته به آن ده‌ها میلیون دلار تراکنش برای نیروی قدس سپاه پاسداران تسهیل کرده و دسترسی مهمی به خدمات بانکداری کارگزاری در اختیار جمهوری اسلامی قرار داده‌اند؛ دسترسی‌ای که امکان جابه‌جایی بین‌المللی منابع مالی حکومت ایران را فراهم می‌کند.
اسکات بسنت، وزیر خزانه‌داری آمریکا، با اشاره به کارزار دولت پرزیدنت ترامپ برای قطع منابع مالی جمهوری اسلامی گفت مؤسسات مالی همچنان درمی‌یابند که ایالات متحده در اجرای عملیات «طرد اقتصادی» جدی است.
او افزود آمریکا امیدوار است بانک‌های بیشتری نیاز به تحریم نداشته باشند، اما این مسئله به این بستگی دارد که جامعه بین‌المللی به سرعت حمایت از حکومت ایران را متوقف کند. آقای بسنت همچنین تأکید کرد ایالات متحده به همراه متحدان و شرکای خود به اقدامات علیه شبکه‌های مالی جمهوری اسلامی ادامه خواهد داد.
بر اساس اعلام وزارت خزانه‌داری آمریکا، گلدن گلوبال بانک برای فراهم کردن امکان انتقال درآمدهای نفتی جمهوری اسلامی از چین به ترکیه ایجاد شده بود؛ درآمدهایی که پس از انتقال به ترکیه می‌توانست به پول نقد و طلا تبدیل شود.
وزارت خزانه‌داری می‌گوید این بانک همچنین آگاهانه پیشنهاد ارائه خدمات بانکداری کارگزاری به مؤسسات مالی جمهوری اسلامی را داده و از این طریق انجام تراکنش از طریق حساب‌های تحت کنترل نیروی قدس سپاه پاسداران و شبکه‌های وابسته به آن را امکان‌پذیر کرده است.
در اطلاعیه وزارت خزانه‌داری همچنین به شبکه «سیتکی آیان»، بازرگان ترکیه‌ای، اشاره شده است. ایالات متحده این شبکه را پیش‌تر در سال ۱۴۰۱ به دلیل نقش آن در انتقال صدها میلیون دلار درآمد حاصل از فروش نفت مرتبط با نیروی قدس سپاه پاسداران تحریم کرده بود.
@
VahidHeadline
اسکات بسنت، وزیر خزانه‌داری آمریکا، جمعه ۱۳ شهریور در شبکه اجتماعی ایکس نوشت از زمان برقراری دوباره محاصره آمریکا، هیچ محموله نفت خام ایران نتوانسته با موفقیت از تنگه هرمز عبور کند و به چین برسد.
او افزود نفت خام در کشتی‌های گرفتار در داخل تنگه انباشته شده و امکان جایگزین کردن ذخایر صادرشده وجود ندارد.
بسنت نوشت: «مسیر حیاتی صادرات ایران در حال قطع شدن است؛ نفت سرگردان، ظرفیت محدود ذخیره‌سازی و درآمدهایی که به‌سرعت در حال کاهش است.»
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/78233" target="_blank">📅 20:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78232">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZXGe7Ils5-O9TW1HBgiNhmgCrbxiX48lOBxpAdMJwT56vb8G-soe4HLPvjaw_Xd3XxBRjEAAcWc4yjAs87boVkw7Cgl6t6aDQ5-lVmJufS8xp9OSkueF3ytYaPS9Mgo9YOX_6alI-USRmJbzKLg0oaDeQata0PaERH9BJc00BXFR2h3eoWt-E5ADMT_uO-5V75APkAf63urUASBMDCUGeGMgrXk3X6VHoSvO70R1Tw0Kx2SanfPfa5u-HW9tvRV6anO1vJvBHG97meFI4y-Zi3x-1Mx4whJ-n-r9mcoSoGOYLa2HFQf28IVF-sUXg4SxiVCaXZSA_p55QMWUalnwBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
دیوانه‌های چپ رادیکال، دموکرات‌های احمق و کمونیست‌ها ترجیح می‌دهند ما در جنگ ایران شکست بخوریم تا اینکه رئیس‌جمهور دونالد جی. ترامپ جنگ را برای آمریکا ببرد.
به عبارت دیگر، آن‌ها ترجیح می‌دهند ما ببازیم تا اینکه ما پیروز شویم!
این‌ها آدم‌های بسیار بیماری هستند که از TDS شدید رنج می‌برند؛ چیزی که گاهی از آن با عنوان «سندرم جنون ترامپ» (TRUMP DERANGEMENT SYNDROME) یاد می‌شود.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/78232" target="_blank">📅 20:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78231">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5P2bNb83F2xwA9IRlTdqhbBUw_iqrcpNz_2ZnSBQpdf1sJin2Dk5ZVicBTDJN0j4u8Jjzr26wHSpfngM5IJuEb4p8ilR0f6kdhioFvvt_TqcVoExmOc8fVmWFR-89hStiUYcqMyWvWjCwoSO7z9YdNbMJw1Rrffx_hPBMHMTp8FilKQxYqSYdM1HvgdrzyxBEEQdgA1-PIFuFxMLHQ6ujMZPmL_Oy-lePTWOsMlBsVv2qSxWJllolO3GG1EZ3jID1_npvb_48DA4oOCM9I5YywChA3CSka2qwJe5f-HR0iSuKjYOCrchF4PCZkiM2jW0_KIaOnEb71zQf5Qe4q1Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه «فایننشال تایمز» روز جمعه ۱۳ شهریور در گزارشی اعلام کرد اختلافات میان ایالات متحده و جمهوری اسلامی ایران بیش از پیش بر سر آینده تنگه هرمز متمرکز شده است؛ چرا که دولت دونالد ترامپ بازگشت به یادداشت تفاهم اسلام‌آباد را رد کرده، در حالی که تهران خواهان احیای این توافق به عنوان زمینه‌ای برای کاهش تنش‌ها و ازسرگیری عبور نفت از تنگه هرمز است.
بر اساس این گزارش، تلاش‌های دیپلماتیک برای بازگرداندن طرفین به تفاهم‌نامه اسلام‌آباد که شامل توقف اقدامات نظامی، بازگشایی تنگه هرمز و آغاز مذاکرات جامع‌تر بود، با مخالفت واشنگتن روبرو شده است. آمریکا اکنون خواستار توافقی جدید و فراگیرتر است که علاوه بر وضعیت تنگه هرمز، پرونده هسته‌ای ایران را نیز شامل شود.
در مقابل، مسعود پزشکیان تاکید کرده که کشورش آماده است به محض بازگشت آمریکا به تعهدات خود در توافق موقت، به تعهداتش عمل کند.
با این حال، واشنگتن بر اهرم فشار میدانی حساب باز کرده و با تقویت حضور نظامی، مین‌روبی و ایجاد مسیرهای امن، سعی دارد ثابت کند ایران دیگر نمی‌تواند از تنگه هرمز به عنوان یک کارت فشار بر بازار انرژی استفاده کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/78231" target="_blank">📅 19:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78230">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tr7yCjXi4DTg6cQWMzu5EMBsWVqw-x94jbc15gUZwxlDIuUl3jXj5ltNEDLhJ99A2czjcEPzrspr9PCG6Tie2_GdVUuFaMvloO_zodrHQ9QbvxovID3LmX8FOLdwb0NOaBDBwiw5v12C2uNIO-Uwu25vF7OfC-P-nZftWZaxQQMWH5JziHBxJXtqWWsfetWAMBWkFPBWc7QV1OVFJhxICzOPIlnfmU01F61SCj8R6SE_re4pwXcP_UhCMLbuHg-Wh-KotE0WsMmaSUlxa1R959AAbgxI6HjuVnoWMIpflZGmn9plGcY_52MwF9kIHme9xBLfLifCWZp0JCJvoJhrRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت گازوئیل در آمریکا با ثبت رکورد تازه‌ای به بیش از پنج و نیم دلار در هر گالن رسید.
انجمن اتوموبیل آمریکا روز جمعه ۱۳ شهریور اعلام کرد که قیمت گازوئیل در این کشور در حال حاضر به پنج دلار و ۸۵ سنت به ازای هر گالن رسیده، در حالی که یک سال پیش قیمت آن سه دلار و ۷۱ سنت بود.
هر گالن حدود ۳.۸ لیتر است.
انجمن یادشده این افزایش قیمت را ناشی از اختلالات در حمل‌ونقل سوخت به‌دلیل جنگ آمریکا با ایران عنوان کرده است.
گازوئیل، سوخت حیاتی مورد استفاده در حمل‌ونقل جاده‌ای، کشاورزی و ساخت‌وساز محسوب می‌شود و بیم آن می‌رود که افزایش چشمگیر قیمت آن، نرخ تورم را افزایش دهد.
قیمت بنزین معمولی در آمریکا نیز چهار دلار و ۱۵ سنت به ازای هر گالن است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/78230" target="_blank">📅 19:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78229">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UWAXy8z52ttvHy9SgyoEn0nS6Zox3fHol0NFLWE2y4NJ88aWIO4cuZ91bPgD2_a1CRrScLm-taxyZ4xz2DW6O6t7ti-EuS8_I_nJDiXri1gAhXoxuJRH1e98oH-jhsmrCIZMbYsu1OB4tW09dDfIwVW33r59dqyYWmpk_hoLGuvlsuXo2B40R7n3335anXj2RNcKlxQtvYPVjIgI-bnVvyY4uLJE_x7hxBfLDukgo2HqcoTwA7z2520bpoQ--dFRVhAi1NLATT06-ZalzFefbdl3lhreIs7_kmZnPP3FkUM6Ts92-c57Y6xJPhLgitEkXBhDUKPc49qMPKmLuegQfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌هایی که من دیروز دریافت کرده بودم:
▪️
آزمون Pte  زبان برای ساکنان ایران لغو شد
▪️
موسسه‌ی پیرسون هم تمام آزمون‌هاش رو برای ساکنین ایران کنسل کرد.
امروز صبح روی سایت اعلامیه زدن یک دفعه.
مشهورترین‌هاش برای ایرانی‌ها امتحان مدیکال کانسیل استرالیا و وزارت بهداشت عمان هست.
و امتحان‌ زبان PTE
▪️
ما جمعی از پزشکا برای مهاجرت استرالیا تلاش میکردیم و هزینه ازمونمون ۳۰۰۰ دلار بود
الان لغو شده بدون هیچ توضیح خاصی
دوستان هتل و پرواز بوک کرده بودند برن هند پیام بدن الان میگه نمیشه باید کارت اقامت کشور دیگه ارائه بدی
خبر:
موسسه بریتانیایی «پیرسون» که برگزار کننده آزمون‌ زبان انگلیسی «پی‌تی‌ئی» و آزمون ای‌ام‌سی (شورای پزشکی استرالیا) است، در بیانیه‌ای اعلام کرد که به دلیل تحریم‌های جدید آمریکا علیه ایران، آزمون‌های داوطلبان ساکن ایران را لغو می‌کند.
پیشتر در تاریخ ۷شهریور۱۴۰۵، تعداد دیگری از برگزارکنندگان آزمون‌های مهارت‌های زبان‌های خارجی، از جمله دولینگو و تافل، اعلام کرده بودند که این آزمون‌ها دیگر در ایران برگزار نخواهد شد.
پیرسون در اطلاعیه‌ای درباره لغو آزمون پی‌تی‌ئی آورده است: «در پی تعلیق 'مجوز عمومی G' توسط دفتر کنترل دارایی‌های خارجی (OFAC) در وزارت دارایی آمریکا، از ساعت ۱۲:۰۰ بامداد هشتم سپتامبر ۲۰۲۶ به وقت شرق آمریکا تا اطلاع ثانوی، ما قادر به برنامه‌ریزی یا برگزاری آزمون برای داوطلبان ساکن ایران‌ نخواهیم بود، مگر آنکه بتوانند مدرکی دال بر اقامت اصلی خود در خارج از ایران ارایه کنند.»
در ادامه این اطلاعیه آمده است: «آزمون‌هایی که در حال حاضر برای داوطلبان مشمول این محدودیت برنامه‌ریزی شده‌اند، لغو خواهند شد. به‌خاطر این مشکل که برای آنها ایجاد شده، پوزش می‌طلبیم.»
سرنوشت شمار زیادی از دانشجویانی که قصد مهاجرت با هدف ادامه تحصیل به کشورهای اروپایی، آمریکا، آمریکای شمالی و استرالیا را دارند تحت تاثیر این اقدامات قرار خواهد گرفت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/78229" target="_blank">📅 19:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78228">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/113b0b4eab.mp4?token=uRfMEdISpWBGiUJf7bJlJ0BayrIsKTlJTjeqKl2ZvHkLEmYf6HaXitvnGHJiNJ9krVozo5cDXtOpJTWYmehb3r05v_zE7Fl-eDMCz4cpJTPkjOIe99lC1xVBXK9bMAGI3gR-gNX3qG82BXJIIWk3pf5LiCjYtjU394OGrQemtN_p7Evgv7yI5Rf32VjQ7YZeVR_tJRe0yxEJG7wBdhKV9rITnFv4XnBCkG9KsHJVFZCjQly4xsUspn27g0zghVlV8NAuhdAlOxm2ODSEjQCl_BxZy3fdc08OSsgoXCNLAQRQwekWdsyUGgshOfbt5vPly9o24teyEM22i5YeSK_4PA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/113b0b4eab.mp4?token=uRfMEdISpWBGiUJf7bJlJ0BayrIsKTlJTjeqKl2ZvHkLEmYf6HaXitvnGHJiNJ9krVozo5cDXtOpJTWYmehb3r05v_zE7Fl-eDMCz4cpJTPkjOIe99lC1xVBXK9bMAGI3gR-gNX3qG82BXJIIWk3pf5LiCjYtjU394OGrQemtN_p7Evgv7yI5Rf32VjQ7YZeVR_tJRe0yxEJG7wBdhKV9rITnFv4XnBCkG9KsHJVFZCjQly4xsUspn27g0zghVlV8NAuhdAlOxm2ODSEjQCl_BxZy3fdc08OSsgoXCNLAQRQwekWdsyUGgshOfbt5vPly9o24teyEM22i5YeSK_4PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
الان از اصفهان موشک زدن یه دونه
سلام وحید جان
ساعت 7:12 دقیقه از اصفهان موشک شلیک کردن ( از سمت [....] اصفهان)
همین الان [...] اصفهان موشک رفت
19:13 از سمت [...] اصفهان موشک زدن
همین الان ۱۹:۱۲ از سمت [...] اصفهان
فکر کنم [...] بود
بالسیک شلیک شد به سمت [...] رفت
از اصفهان همین الان موشک زدن صدای وحشتناکی داد
اقا همین الان یه موشک از سمت اصفهان شلیک شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/78228" target="_blank">📅 19:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78227">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PexjlT0ui9lV12sWJSmC9HQ1P3oakIMApXsxAmYmrRJJy7ZTsrAOzOniy5536J-R-Jij7RJdt3dud5PmWM26ojnqDUw-FCQTm6jyiJ8d-PUuC3KeoHOLCz9zf69E_p9iEDkvpx78R9d3w3loeTRKdITFsGvNpmfnwm_TijaVzmiOHXsml1kq1sb4K0kTzfgWYIQaBYm6A7pXTRM2_wIQAmnicvR0Os450SIFiX4ZfFuDeRdZQBLX4Zv8Qo8SkiRuiX8X7UoMAIdUwuZOqjxy7Hov4-k7HO4Ts2y6TQF_4TYmtcYlYWOyLBM9jhAjgGKiC_XTdzFOcMQx0Hn19LXP1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌پست پنج‌شنبه ۱۲ شهریور به نقل از یک مقام ارشد منطقه‌ای گزارش داد عمان پیشنهاد جمهوری اسلامی برای دریافت مشترک هزینه خدمات از کشتی‌های تجاری عبوری از تنگه هرمز را رد کرده است.
این مقام گفت مسقط حتی با دریافت داوطلبانه هزینه خدمات زیست‌محیطی و امنیتی از کشتی‌ها موافقت نکرده است.
یک مقام آمریکایی نیز به نیویورک‌پست گفت شرایط توافق پیشنهادی میان جمهوری اسلامی و عمان برای تقسیم درآمد نهایی نشده است.
این اظهارات در حالی مطرح شد که حسین محبی، سخنگوی سپاه پاسداران، پیش‌تر از دستیابی تهران و مسقط به توافق در این زمینه خبر داده بود.
رویترز هفتم مرداد گزارش داده بود عمان طرحی با حمایت کشورهای خلیج فارس به جمهوری اسلامی ارایه کرده است که بر اساس آن، مدیریت تنگه هرمز به شکل منطقه‌ای انجام می‌شد و شرکت‌های کشتیرانی می‌توانستند به‌صورت داوطلبانه برای تامین هزینه‌های ناوبری، حفاظت زیست‌محیطی و عملیات جست‌وجو و نجات مبالغی پرداخت کنند.
عمان پیش‌تر نیز با دریافت اجباری هزینه از کشتی‌های عبوری از این آبراه مخالفت کرده بود.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/78227" target="_blank">📅 02:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78225">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gnuHUSZLYbrtEgZ6oUMwm24FzXIUUDuJY9rvFcWF3E2U5htw0oMvMEhPmEilbU6bvCTzHE8VHzUio5U7JKiseErnlKoHm9vC35WzQNZIDlR2fSEEcCmNA3BGs5UoAiA-nZR9DZJzNKyoGpm6pOhWTJxl6pMHMS6tZmFG8ZTLm_jQqE4VlapJKqjf78Iwg8diyPOxIz7P_k9uFGlhgihlmJ49KY7z52imfEZxVFnhRhQGkl2w0QI2_TzrAZBhrxrtw3jClT8nZkU4DNjuusuPemKTdX8c5jDj-x9whnQyoVicRlsPV6vUXFHOnkCD-Qu-oYuP-dkqsafUAkpHF3hndw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GVuqgpOnVMrygrFwqgOfnmBpwIccAPmL0ec8y6XR6ohkJ8yuxZMaUWGSp_IpVLR9mlskQDGWjWQsNoc386o5mj9IAyAwAG3nFp-pO7bYAkBWIpJV4yhWDfAknv5nqw8DVW5V0tc2a0AGCQlSFqniN6SEyHB0pKx31neSNb9znT01BQytsLrKmXHble5u3-YFx9ZXClvkeclX5rS264Hp8Eu6yHSceA1icHZiW8mcfiqhkJiXI25XjmTdbWZOBIdX3C6YNSPQIFkL_Aaes4RlGb0seK8wOkYfVKxPCON_gP8K81q9v4uKj-Y8SXZQ0biuB7WzF3YlFSl2Fy1adsHQLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در گفتگو با شبکه جی‌بی نیوز گفت:
«آن‌ها سه سایت داشتند و شاید حالا کوه کلنگ گزلا را هم داشته باشند، اما ما روی همه این مناطق دوربین داریم. می‌دانیم چه کسی وارد می‌شود و چه کسی خارج می‌شود.»
او در ادامه درباره توان اطلاعاتی آمریکا افزود: «حتی می‌توانیم از فضا اسم افراد را بخوانیم. آن‌ها حتی نمی‌توانند بدون اینکه ما متوجه شویم جابه‌جا شوند. ما دقیقا می‌دانیم چه خبر است و از این بابت کاملا مطمئن هستیم.»
@
VahidOOnLine
گفت:
ما کنترل کامل تنگه هرمز را در اختیار داریم. هر شب ۳۰ تا ۴۰ قایق آن‌ها را از بین می‌بریم و رادارهایشان را هدف قرار می‌دهیم.
او همچنین افزود اقتصاد ایران «در حال فروپاشی» است و افزود: تورم ممکن است به ۳۰۰ درصد برسد، پولشان تقریبا بی‌ارزش شده و نرخ برابری آن با دلار حدود دو میلیون به یک است و هر روز هم بدتر می‌شود. آن‌ها واقعا در وضعیت بسیار بدی قرار دارند.
@
VahidOOnLine
گفت:
با جلوگیری از هسته‌ای شدن ایران، اروپا و بریتانیا را هم نجات دادم
«من کشور شما را هم از این تهدید نجات می‌دهم، چون اگر ایران سلاح هسته‌ای داشت، احتمال اینکه از آن در اروپا استفاده کند بیشتر از آمریکاست، زیرا توان موشکی برای رسیدن به اروپا را دارد، نه آمریکا.»
او همچنین افزود ایران تنها «دو تا چهار هفته» با دستیابی به سلاح هسته‌ای فاصله داشته و حملات آمریکا این روند را متوقف کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/78225" target="_blank">📅 02:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78224">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">پاسخ جی‌دی ونس معاون رئیس‌جمهور آمریکا به پرسش‌های خبرنگاران
بخش‌های مربوط به ایران با تشخیص و ترجمه ماشین
متن زیرنویس:
https://telegra.ph/vance-09-03-3
خلاصه‌ای از اون متن مفصل به تشخیص ماشین:
1️⃣
ونس: «تنها دلیل اینکه بحران جهانی انرژی نداریم، رهبری ترامپ است»
▪️
«دلیل اینکه قیمت بنزین اکنون این‌قدر بالاست این است که ایرانی‌ها به کشتیرانی تجاری شلیک می‌کنند.»
▪️
«فقط دیروز حدود ۱۵ میلیون بشکه از تنگه هرمز خارج کردیم.»
▪️
«ایرانی‌ها دارند می‌فهمند که کنترلشان بر تنگه هرمز عملاً از بین رفته و این اهرم هر روز کم‌ارزش‌تر می‌شود.»
▪️
«توصیه من به ایرانی‌ها این است که دست از رفتار مثل آدم‌های دیوانه بردارند و به کشتیرانی تجاری شلیک نکنند.»
▪️
درباره حمله به مراسم عروسی: «در این مورد مشخص، من فکر نمی‌کنم اطلاعاتی داشته باشیم که چیزی را به این سو یا آن سو ثابت کند.»
▪️
«ایالات متحده هرگز در جنگ غیرنظامیان را هدف قرار نمی‌دهد.»
▪️
«در حال بررسی آن هستیم.»
2️⃣
ونس درباره ایران: «فشار اقتصادی، نظامی، دیپلماتیک و مخفیانه؛ همه روی میز است»
▪️
«ابزارهای اضافی زیادی هم در اختیار داریم. رئیس‌جمهور از برخی از آن‌ها استفاده می‌کند و از برخی هم نه.»
▪️
«هر اتفاقی که ممکن است بیفتد روی میز است: فشار اقتصادی، فشار نظامی، فشار دیپلماتیک، فشار مخفیانه.»
▪️
«ایرانی‌ها مثل تروریست‌ها در تنگه هرمز رفتار می‌کنند.»
▪️
درباره احتمال حمایت از مخالفان ایران: «البته، من قرار نیست درباره‌اش صحبت کنم.»
3️⃣
ونس: «آمریکا تنها کشوری است که می‌تواند کنترل تنگه هرمز را تضمین کند»
▪️
«ما تنها کشور دنیا هستیم که می‌تواند کنترل تنگه هرمز را تضمین کند.»
▪️
«ایرانی‌ها دوست دارند صفر میلیون بشکه از تنگه هرمز خارج شود. دیشب ۱۵ میلیون بشکه از تنگه هرمز خارج شد؛ و این به‌خاطر ایالات متحده آمریکاست.»
▪️
«اگر ما این کار را نکنیم، هیچ‌کس دیگری نخواهد کرد.»
▪️
«پیام ما به ایرانی‌ها ساده است: باید شلیک به کشتیرانی تجاری را متوقف کنید.»
▪️
«ما با آن‌ها صحبت نمی‌کنیم و صحبت هم نخواهیم کرد مگر اینکه شلیک به کشتیرانی تجاری را متوقف کنند.»
4️⃣
ونس: «برای پایان درگیری با ایران ضرب‌الاجل مصنوعی تعیین نمی‌کنیم»
▪️
«باز هم، من اسمش را جنگ نمی‌گذارم.»
▪️
«عملیات عمده رزمی حدود شش هفته طول کشید.»
▪️
«با عملیات Midnight Hammer تأسیسات هسته‌ای‌شان را نابود کردیم.»
▪️
«با Epic Fury، پایگاه صنعت دفاعی آن‌ها برای تولید سلاح و همچنین بخش بزرگی از توان نظامی متعارفشان را نابود کردیم.»
▪️
«یک ضرب‌الاجل مصنوعی تعیین نمی‌کنیم.»
▪️
«غیرمسئولانه خواهد بود اگر راهبرد و جدول زمانی‌مان را برای کشوری مثل ایران تشریح کنیم.»
5️⃣
ونس: «توان ایران برای مختل کردن زندگی عادی آمریکایی‌ها بسیار محدود است»
▪️
«اطمینان زیادی داریم خاک کشور امن است.»
▪️
«ایرانی‌ها تلاش خواهند کرد کارهای زیادی انجام دهند که توان انجامشان را ندارند.»
▪️
«اگر توان ایران را برای مختل کردن زندگی عادی آمریکایی‌ها در نظر بگیرید، به نظرم بسیار محدود است.»
▪️
«صفر نیست، اما بسیار محدود است.»
▪️
«من خیلی بیشتر نگران حملات سایبری از سوی بازیگران دیگر می‌بودم.»
6️⃣
ونس: «چین به برخی درخواست‌های آمریکا درباره ایران پاسخ مثبت داده است»
▪️
«ما قطعاً چندین گفت‌وگو با چینی‌ها داشته‌ایم.»
▪️
«فکر می‌کنم چینی‌ها به برخی درخواست‌های ما پاسخ مثبت داده‌اند.»
▪️
درباره تماس مستقیم ترامپ و شی: «در واقع نمی‌دانم آیا رئیس‌جمهور مستقیماً با شی صحبت کرده یا نه.»
7️⃣
ونس: «کشورهایی در خفا برای مجازات ایران به آمریکا کمک می‌کنند»
▪️
«فکر می‌کنم جمهوری خلق چین قطعاً بسیار مسئولانه‌تر از ایرانی‌ها رفتار کرده است.»
▪️
«اگر به ترکیه، آذربایجان، امارات، عربستان سعودی، قطر و بسیاری از کشورهای ائتلاف عربی خلیج [فارس] نگاه کنید... کشورهای زیادی هستند.»
▪️
«گاهی حاضر نیستند علناً بگویند، اما در خفا کارهای خوب زیادی انجام می‌دهند تا به ما کمک کنند مطمئن شویم ایرانی‌ها بابت شلیک به کشتیرانی تجاری هزینه می‌دهند.»
▪️
«این کار همچنین منابع اقتصادی لازم برای بازسازی برنامه هسته‌ای‌شان را از آن‌ها می‌گیرد.»
▪️
«تا اینجا ندیده‌ایم که تلاش کنند چنین کاری انجام دهند.»
▪️
«همه این‌ها در خدمت این است که مطمئن شویم ایران به یک قدرت دارای سلاح هسته‌ای تبدیل نمی‌شود.»
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/78224" target="_blank">📅 01:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78222">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ونس: نسبت به احتمال نقش آمریکا در حمله به مراسم عروسی در سیریک بدبین هستم
🔸
معاون رئیس‌جمهور ایالات متحده می‌گوید تحقیقات دربارۀ «ادعای حمله به یک مراسم عروسی» در جنوب ایران ادامه دارد.
🔸
جی‌ دی ونس که روز پنجشنبه ۱۲ شهریور در کاخ سفید به پرسش‌های خبرنگاران پاسخ می‌داد، در پاسخ به سوالی در این زمینه گفت: هنوز اطلاعات کافی در اختیار نداریم اما ارتش ایالات متحده «بر خلاف سپاه پاسداران» هرگز غیر نظامیان را هدف قرار نمی‌دهد؛ اما گاهی ممکن است «اشتباهاتی» رخ دهد.
🔸
معاون دونالد ترامپ در ادامه گفت: نکتۀ مهم این‌ است که حتی در صورت بروز اشتباه هم، نیروهای مسلح ایالات متحده، «باز هم بر خلاف سپاه پاسداران»، از اشتباهاتشان درس می‌گیرند تا چنین اشتباهاتی تکرار نشود.
🔸
ونس در نهایت با تأکید بر این‌که تحقیقات ادامه دارد و هنوز اطلاعات کامل نشده، گفت شخصاً نسبت به احتمال نقش آمریکا در بروز این حادثه «بدبین» است.
🔸
به گفتۀ مقام‌های ایرانی، در جریان حمله شامگاه ۱۰ شهریور آمریکا به یک مراسم عروسی در کوهستک سیریک در نزدیکی تنگهٔ هرمز، چهار تن از جمله یک کودک کشته و ده‌ها تن زخمی شدند.
🔸
وزارت دفاع آمریکا از ۹ اسفند‌ ۱۴۰۴ و حادثۀ حمله به یک مدرسه ابتدایی دخترانه در میناب هم اعلام کرده که مشغول تحقیق است، اما بیش از شش ماه پس از حادثه و با وجود فشار کنگره، هنوز حاضر به انتشار نتیجۀ تحقیقات نشده است.
🔸
مقام‌های جمهوری اسلامی می‌گویند که در جریان حمله به مدرسه شجرۀ طیبه، بیش از یکصد دانش‌آموز،‌ معلم و اعضای خانواده‌های دانش‌آموزان کشته شدند.
@
VahidHeadline
بعدا ویدیویی زیرنویس شده شامل حرف‌های احتمالی دیگر می‌گذارم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/78222" target="_blank">📅 22:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78219">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFactNameh | فکت‌نامه</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h43jcpMYJTiSoGELRRkIAu6Eh3YNmFH0fmr5pHYXeNBTHU9QpGJZ4onwMgPd8_qU9yT5fMleCF8RQ4iddWUMecaM8P09pxwqaaINkdKbfzqUqibew-2BpP16hIE1xlf_XMNjZviDUn5JGYGZpoEtBDpoNBCAidi-LtwcyDDbKNvcN5t0Kdy-ongJl84mdgLJUgKYWYhshO7xVYXarMKZsO9BHO5fCZh8wr2sOFZJP319W2rLiYiQDeD9MLflq3JjOvF6BXeuHg0bb2NxHT1FxJ9_1KD0JIBso3Mx6AYRLAfle69J5SDf1skkia_oCQ0wJAZ6FuBdIIi0HSPxdkIBHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qyrSVLFDjkuaaCiH9gSsnF4eNpCa9SVJccH9z2CakuZhSmiRL-GcWtUfh1aHltxxHY2xkfOxeHhRUb_5b6OLZG32dp7HPQvVBoD_Ui67x2XD8sRGfu9TG2HICT5XwJX2NE5VLYQf3YhBDmtJT3ScrVxKGINJoOGRZCT4dVK1s9GqSW8WsvcazixqEPJ9rWItvdTqW8tW-d3lUKes5hpof48RZGNYDLdcactev28vszA1yCTRuNY2CMykwdfm43I2CiS_dB9WYSnNXpG5CfDxqQa8Z848Z1h40hHpbXqnK1eI2yY1mr9C1ndHytJj35VeEteKD_ZgIsxbfUrsA1GT8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DyZom3E5s4zmkcsKEmgRho3qtApWo_gaeXLJ3ED4vXqGmqidtQcFFGAimdWYty3RrgIstOdYB5gyOY7KV-5OPMkIhhRMI4fdt4oC_R6tTobwCkbzyfZyk4B_Sa2ohT439d-1LvDzoNH37E00tY4srjA36U6BTinjKBpUaQtEgiSIVVqw4BxhhExXn5oB6R-9b7CCn2zvsUES2Xuu_8Zhhx4Xz78DiBQ0xiFewbhitIHDw0UGCoGZLVgmglg0vMVtck90Y-PVPNhiEJpfEj8oTRQ1MtkytjJFtMnXFyrFZ1rl3RRH5x2kllU5ohcrthud_U638ig7zm-gPDg_iR198A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📝
درباره حمله به مراسم عروسی در سیریک چه می‌دانیم؟
🔹
همزمان با حملات هوایی آمریکا به شهرستان سیریک در شب ۱۰ شهریور ۱۴۰۵، انفجاری خانه‌ای را در بندر کوهستک تخریب کرد که در آن مراسم عروسی برگزار می‌شد. بر اساس گزارش‌های منتشرشده، تاکنون پنج نفر، از جمله یک کودک چهار ساله، جان باختند و ۶۵ نفر مجروح شدند.
🔹
تصاویر محل حادثه، صدای چند انفجار در ویدیوی دوربین مداربسته، بیانیه سنتکام و تکذیب‌نشدن حمله از سوی سخنگوی این نهاد، انتساب حملات آن شب به آمریکا را تقویت می‌کند.
🔹
همزمان در شبکه‌های اجتماعی ادعا شده بود که انفجار خانه نتیجه «پرتاب ناموفق موشک سپاه» بوده است؛ اما تاکنون هیچ گزارش رسمی یا مدرک معتبری این ادعا را تایید نمی‌کند.
🔹
برخی حساب‌ها برای اثبات این ادعا، ویدیوهای قدیمی یا نامرتبط را منتشر کرده‌اند. تنها گزارش مشابه درباره یک پرتاب ناموفق سپاه در همان شب، مربوط به خمین در استان مرکزی بوده و ارتباطی با سیریک در جنوب ایران ندارد.
🔹
با وجود شواهدی که از حمله آمریکا به سیریک وجود دارد اما هنوز مشخص نیست دقیقا چه پرتابه‌ای به خانه محل برگزاری عروسی برخورد کرده است.
🔹
این در حالی است که در ویدیوی دوربین مداربسته، صدای پهپاد شنیده می‌شود و پدر عروس نیز در یک مصاحبه تصویری به شنیدن صدای پهپادها اشاره می‌کند؛ شواهدی که احتمال استفاده همزمان از موشک و پهپاد در عملیات را تقویت می‌کند.
🔹
این در حالی است که قطعاتی از موشک کروز SLAM-ER در منطقه دیده شده، اما میزان تخریب خانه با انفجار کامل سرجنگی ۳۶۰ کیلوگرمی این موشک سازگار به نظر نمی‌رسد.
🔹
احتمال دارد خانه با مهماتی کوچک‌تر، (مثلا پهپاد لوکاس با سرجنگی حدود ۱۸ کیلوگرمی) هدف قرار گرفته باشد و قطعات SLAM-ER به اصابت دیگری در همان محدوده (دکل مخابراتی در فاصله حدود ۱۳۰ متری) مربوط باشند.
👈
در فکت‌نامه بخوانید
🌐
@Factnameh</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/78219" target="_blank">📅 20:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78218">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LCH672_bhYOBchtd0P3V91YkvXlPRS-QpdAdfRTovW79l9pOJEo7dg9kVQhL9F0hzzs4lQzr2cSUbbBjtuUI-yNXlHSZihT0NnN-4-3s3pNsUiULahcCZpl2ceB23ITESP_nG9PC3MH6ZQofWznj0K_JDc_3yl0FWLWGyYg42TCMbpSdQsrQkYr0WqVARRbI3tqH7nTJL2ZqbtruTR3u4PJottbmsicxvqPcXMnNDRo88WcMIQxi0iWXkdC_rHzn6oWbXdL9W94daiU4jsv5y75244SV0GS05g_ZYkdf0NC4LXhA8pMnf_RIRBkV_Ck8JaYeFc05IgtS5jgRwmOpQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پست‌ها که در گوشه کادرشون نوشته شده Ad تبلیغاتی هستند که به خود تلگرام سفارش داده میشن.
من نمی‌تونم جلوی نمایش‌شون رو بگیرم:
https://t.me/VahidOnline/73400
https://t.me/VahidOnline/77482
https://t.me/VahidOnline/77989
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/78218" target="_blank">📅 19:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78217">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F_VKRWHX-e2IVRTQVdGCAPrcvUWaZmqbbbDnwY3tksXAEAJ419ErhROcMMrKIB8gLDF9zhOxxKHiagAxMNrj8mdHnFEWJCY4AwJ9r1L_t6XZuYREVDtiAMo7gM8OH5tlmF5KoQ-ScdqqEadvhwA18Oev9cU-H7qssXbZYiCWCeAKh2FQQ36M5rjVB5QyKXzX5WCk6R3kYqPXB28b4CjRHXdqp_qAmGD89CV5mIyTdCU_pxT-5SRqQohJ4di5ZH3lBLeuCt_cQ_SFntp9i0H7A1rED4LISLDEIps22X-HXYh_j0pUxqZX0LDs3U9oTlrJ8poRwYEIvgxOkpsS3HWm3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
برای آن آشغال‌های خائنی که حاضر نیستند درباره عملیات نظامی ما در ایران گزارش دقیق بدهند: ما عملاً مقادیر نامحدودی مهمات با کیفیت متوسط تا بالا در اختیار داریم؛ بسیار بیشتر از آنچه بتوانیم در این جنگ یا هر جنگ دیگری ــ که وقوعش بسیار بعید است! ــ مصرف کنیم. علاوه بر این، ما در سطحی بی‌سابقه در حال تولید مهمات هستیم. در حال ذخیره‌سازی و آماده شدن برای هر وضعیت احتمالی هستیم که ممکن است پیش بیاید. این مهمات را برای خودمان، ایالات متحده آمریکا، نگه می‌داریم، به‌جای اینکه آن‌ها را به دیگران بفروشیم؛ اما فروش به متحدان نیز به‌زودی دوباره آغاز خواهد شد.
همچنین لطفاً همه بدانند که دولت بایدن بسیار بیشتر از میزان مهماتی که ما در ایران مصرف کرده‌ایم، مهمات را کاملاً رایگان در اختیار اوکراین قرار داد. صدها میلیارد دلار بدون دریافت هیچ هزینه‌ای به اوکراین و ناتو داده شد؛ پولی که اروپا حاضر بود بابت آن بپردازد ــ اگر فقط از آن‌ها خواسته می‌شد. اما ما آن پول را مطالبه خواهیم کرد، هرچند با کمی تأخیر!
از توجه شما به این موضوع متشکرم.
رئیس‌جمهور دونالد جی. ترامپ
truthsocial.com
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/78217" target="_blank">📅 18:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78216">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jnlQl6ApPQ5VbC8HSUcDYZ2eMBE2TiFulcQngRGpTwl2vQPMipTwI87dD975EmFJz93uamMxgK2zqcUQVchFNu3n8ob_krJQTsjuHlGYwfhh0hIEzu8n6_3YOnR1TwLMQ8gP4I404-irex73Dwh-wPQgsfEUoujb-EbKg5k0BYB2q8WgNcPerDoZj0aNELmSeEQFrXiaTrj3d_wxVokaJQ8u3YwmyhBnvy98M_ngXbxFanwejRhWG6qDFNJByGY-cjoT3aaIsBOlrBNnZDCJVXSHTX1lrKfP_P8GkgEyDztGGQQkhZpdrbqy1wMuQnhNuN6gTE1zrw2nyoU_ZMWDYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا عارف، معاون اول رئیس‌جمهوری اسلامی ایران، روز پنجشنبه ۱۲ شهریور هشدار داد که «ماه‌های تاریکی» در انتظار اقتصاد ایالات متحده است و از مردم آمریکا خواست اقدام به ذخیره‌سازی سوخت و بنزین کنند.
او تاکید کرد که «جنایات جدید آمریکا»، دکترین دفاعی خود را به تاکتیک‌های «نامتوازن» و «چندلایه» تغییر داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/78216" target="_blank">📅 17:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78215">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cSb-TGiyfIue-pwW612Gum1nK21tpOAnCitgGaGcdIWHDIR1xdQm2loL5dKC_z7iyYuE-_7ptaOdxbBOqfpoByO_PPyO0EkyE9etfC7XmaPbCwvFl-WhZQfd96tU8bmaq-fk1UEjTVULU3IdXiDVcR-nHllc0B3Mg_NTMOkpwE6eJbKWtAEcf4CJMmn5V45MTfd5FmtC7yC7-cro8tkR5weuz44pVoZXSDkRtqAczInPINwHiPnAxN1zcPxfuxQuif4LMWeocuhcjtfjzaEzUKOKjQwzSFw2-w2tACMcQ0jU4Al3VyKVqqIs_pW07VQ6o95zyiDPZ73WYO73syTlpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">916208
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/78215" target="_blank">📅 16:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78214">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vPbTc1fC3bTiiEN19vtZZUPFRwyHQBNm8UOliXUaBH4lOWCjACTMUXPZhrrsVSG077thUkbhjr-OlMWFaMxH43dwXW_inQMfD8-LN1vYxcH6GyqU7_5aIQgFmxQjw5dQp9gUV76p4z6nAgdwp_fFI1G3pL140HkHVJObTHhs8yqHzcrczYz0kb2Rc4Xp6HFyau4gQTCqos-aV9OFhHVoLCUXm6hkZFFdwYvkH5LhERU7PGJNBxMIG8v10a85LMe-iuyJc9aMt-DfBxTxt2hnErQQc7G2_KbCOsARBXthMQWXwyKfFvOz3Kp9XBg-zS2ENTztEaVSsdssKZ-BU5TsGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا با انتشار تصویری در شبکه اجتماعی تروث سوشال، مجموع حجم نفت و گاز مایعی که پیش از جنگ از تنگه هرمز عبور می‌کرد را با میزان کنونی آن مقایسه کرد و نوشت: «حجم نفت هرمز بازگشته است!»
ترامپ در این تصویر، مجموع حجم نفت و گاز مایع عبوری از تنگه هرمز در زمان پیش از جنگ را حدود ۲۰ میلیون بشکه در روز در نظر گرفت و میزان عبور این مایعات در حال حاضر را ۱۸ میلیون بشکه اعلام کرد.
این در حالی است که سامانه پیگیری موقعیت نفتکش‌ها در جهان، میزان عبور نفت و گاز مایع در ماه گذشته را به‌صورت میانگین ۷.۵۴ میلیون بشکه در روز اعلام کرده است.
بر اساس داده‌های این سامانه، حداکثر میزان عبوری در یک روز، ۱۰ میلیون بشکه بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/78214" target="_blank">📅 16:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78211">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/beDK_WHqHb5jryG3MkO_epSUdubRyVuemZAm8uTreijnUdKXRxuYsIALnBUwn7-vAw9Zl_WemUMsQXcec9LHOJ4tL6ttuUUXf_UE-Fd_aUrKfOh0tAR5Tp8hjG0zJDPR6Pod4W9h6mTa5cJxxNZ6aLdW6SVXZehnytPecuZawhZ5XfshHLWlBSOhvyBO0hZfPJ5x9iDp2D-AaaFrpOhBhmQxgBtcNIPZ0YVT-gSoDPwYDrHGJV4GwUpmaF6XP3CBsYC079ax9qNjq9-3Bqagp3QqcW4I2CZ13leQKcOojlQnYXATPhQFNNLoav3OfAjc4e2FGGUC9Yf5W6HtiH_D7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MwWZbufuL_7AA0sa_GzJbPHPQ2OtF-vp33sqGAcPGCP1orUkQ4tDBMaVxQ3kUErz-nWnb4i9TGZlDoofVaqLip7UCJg_Vt158hDU0EJTYv0dHJbP_jugrcok7Xkh466f-bS7H8j3CGjdLZ0dO96Wz9nWv6T1wwnzBw0yM0ePxqjn3hBLr_xN9GvB8wRWbNfdLkXIIydAx_oZII1-igS8GweqbSFb9CExOpZH9kUo4NfSDlUhJHH7DCAbztthgY9_WkS0bOlMM20TMXpgwEuTMq2f2evRgvzY-YCdPV76GccnmsMT6W8vPVg0wE0fF3kjja_lrDrYE8Ih37pNieFcZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6484aadc92.mp4?token=MsvH9tteSw9uFO2sm2k8VGZcN65Y49cP-y0BuGVjwo2Xb4cftLcL2uMqo0NkHNORIIMcfX9WVR5m2jtxTI9hkCKIXd5FBYJ9RuptQ9ibq9V_vgde-gH9x-dpjHKNdjiSYUTzEmauVkaGTKNTPdQj6o5dDboE0zQ7UXHlWhf8jQldjaUOTDObCLT8dB8rg7zBgwELnc_Tvgi9BiP9DYo1cuXL2touU7kaGisWtYuVcArAKNJ5BjNoe2DHwf4hewFJt61VYSVAefUmLVwDWn4jr7NRVC-4Ta0z1ePWXepYK03djXZ-_NVoqFD-tCxXcHLXXxzEwf-blvml5fkZi21eCw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6484aadc92.mp4?token=MsvH9tteSw9uFO2sm2k8VGZcN65Y49cP-y0BuGVjwo2Xb4cftLcL2uMqo0NkHNORIIMcfX9WVR5m2jtxTI9hkCKIXd5FBYJ9RuptQ9ibq9V_vgde-gH9x-dpjHKNdjiSYUTzEmauVkaGTKNTPdQj6o5dDboE0zQ7UXHlWhf8jQldjaUOTDObCLT8dB8rg7zBgwELnc_Tvgi9BiP9DYo1cuXL2touU7kaGisWtYuVcArAKNJ5BjNoe2DHwf4hewFJt61VYSVAefUmLVwDWn4jr7NRVC-4Ta0z1ePWXepYK03djXZ-_NVoqFD-tCxXcHLXXxzEwf-blvml5fkZi21eCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">dadban4
:
"امیرعلی قنبرزاده، بازیکن تیم نونهالان آکادمی بسکتبال پاس، روز ۱۹ دی ۱۴۰۴ در گرمدره استان البرز کشته شد.
مادر او با انتشار این ویدیو نوشته است:
«امیرعلی عزیزم، دل بارانا برات خیلی تنگ شده، جات برای مامان خیلی خالیه.
شادی را به گور خواهند برد، آنان که رنج را در ما آفریدند.
ما مادران نه می بخشیم و نه فراموش می کنیم.»
امیرعلی قنبرزاده در جریان اعتراضات، جلوتر از دیگران حرکت می کرد و دست هایش را باز کرده بود تا از سایرین محافظت کند.
او در همان حال با اصابت سه گلوله جنگی به سرش، جان خود را از دست داد."
abelbalb
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/78211" target="_blank">📅 15:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78210">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4iG8aDLpYOPaHbl7L5qXbMDO-045keRCyqVdHl6G7PWqt3UjjObvduND2dYI4J5IkbsHUQL5ogHBSWvz1wqf0Lr0PPC-8lD53dtrwy8jPnfLw1Q499FecicbOj8_TC1dDQtNBSi1e7Bk1X7IogEs7euQd5TD594REaK1fmZAYxyrOJhiOpBEd58BrP2jEykMwYk941to6SMMejyXHYSdOiD-F9WWA4s1L51YzRLXeuI6pE7UGnfUiyldKBIWaC2seYTjAZDlE4hP3JmZZ6n1n4IrLB66qfzcIOh0-E7wnIz-nWXyaaeQb_Yy2Kbsy7DgpR2xVKkKaCnfDnyDDR8Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، نزدیک به سپاه پاسداران، از کشته شدن سه خلبان ارتش جمهوری اسلامی ایران در حمله سه‌شنبه شب آمریکا به ایران خبر داد.
این خبرگزاری با انتشار اسامی و تصاویر این خلبانان گفته است دو نفر از آن‌ها از خلبانان نیروی دریایی و یکی از آن‌ها از خلبانان نیروی هوایی ارتش بودند، اما اعلام نکرد در کجا و چگونه کشته شدند.
با این حال، اسامی اعلام‌شده سه نفر از هفت نفری هستند که روز چهارشنبه ۱۱ شهریور اعلام شد در حملات آمریکا به شهرهای اهواز و آغاجاری کشته شدند.
در جریان حملات شامگاه سه‌شنبه آمریکا، به‌‌گفتهٔ مقام‌های ایران، مناطقی از جمله فرودگاه جیرفت در جنوب استان کرمان، عسلویه، کرمانشاه، مناطقی در استان خوزستان، شهرهای چابهار و کنارک در استان سیستان و بلوچستان، سیریک، لاوان، قشم و بندرعباس در استان هرمزگان هدف قرار گرفتند.
سخنگوی وزارت بهداشت صبح پنجشنبه از کشته شدن «۱۸ نفر و مجروح شدن ۱۴۲ نفر» در جریان حملات اخیر آمریکا خبر داده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/78210" target="_blank">📅 15:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78208">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qOwluHyukEjMYVN1leczX4uUJZ27rgwFjQxgMO2E8TzQZKuBFTr5WOy7iGa7lvFR1mYzRu61iWH2bUtn_QPxoMRYMTqAfZQwjF3KoKJm2zup0ZSHuUmI937T1L8N1xkKTyOO2IaSqsWrtwS0pQesG2IDDqApgqlEiAVsd98SRahozke0WXfZctOAtwhZn2adAu6nQOMP5bDP9_iDd1hWnvtC0vtKI7OmlTJWnA-R_bCAHEeZL58Zk2pJO8Kx7tjOcLDCM8rijr3uVBta-JA_zT_5JA5jR-aC6osUocMsw-hWyMyRuLPRmEQenGHlxfssZ754yoj-kDsc57v-G9UEqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">quotes
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/78208" target="_blank">📅 15:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78207">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oy7rYdvRLf1clrOYUVHrntRDwu0gxFskWH3Jkk8qxhBkrEBnTD88S5vEuALv0JHrSfN0iy7nczIGA5eyW4JwsY6YdmAoGU-sOTL4NFYxJxuKc4sZeSX9tB8Jri1W4WvH1VusKLwW04c8C6Gwll8K4KoXwwvWW9t8rEN8D4aUZAWiSOmodPwOru6_TGS4li7cpLfrfwyTY05B_DDS4Tx_wfR6ldFNJTcIDvRZ0VNYrnx0qqSfNeQ-2HeMSSprHVMc52usUqZus_4mnpM2z7l2Hb-9rw9xsqYx-7PnyOnhQpjzoWx7TUunkZ1Md1WGxEsaodkXbpk6hQ2aWGbzLnOZmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یسرائیل کاتز، وزیر دفاع اسرائیل، پنج‌شنبه ۱۲ شهریور در مراسم روش هشانا با کارکنان وزارت دفاع اعلام کرد حمله جمهوری اسلامی به این کشور، اسرائیل را از همه محدودیت‌ها رها خواهد کرد و این کشور حتی زیرساخت‌های انرژی را نیز هدف قرار خواهد داد.
وزیر دفاع اسرائیل گفت: تمام زیرساخت‌های ملی، نظامی و غیرنظامی، از جمله زیرساخت‌های انرژی را هدف قرار خواهیم داد و ایران را به اعماق عصر حجر و تاریکی بازخواهیم گرداند.
کاتز همچنین افزود: فشار اقتصادی و نگرانی از قیام و سقوط حکومت ممکن است جمهوری اسلامی را به اقدامات از سر استیصال سوق دهد.
او گفت: حکومت آیت‌الله‌ها در ایران به‌خوبی می‌داند چرا پس از آنکه دو بار ضربات سختی به آنها وارد کردیم، برنامه هسته‌ای را نابود کردیم، خامنه‌ای را کشتیم و به توانایی‌های راهبردی آنها آسیب شدیدی زدیم، به اسرائیل حمله نمی‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/78207" target="_blank">📅 15:00 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78206">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rhmmOdbGT4fq9T_6QwkE5dn_iLz5piRJK7J02W8GKAR6AHGycvEJ07PYg153oW0c4ULQZMbj9pwCaJl3buoFUhbXSlsdzO5NLpmHamJQwc_GW4_clmwNIirf4QfpTspo3i35WEYXoaqiBvTcrkhkL_Zivsr_VT7xTT-atiYOdabrmrvLY2bYmFBPidCDn6l0bgOYOFYRewu9_vNuk74XnkS2n2Zi97I-NhX7y3-ev200Cpi-tLBYWpEjqSpdwoB0F3GlkNGskCjUlhaNguMhF3nhk9p1areG93SFDg8xL9l1LFDUWmfRbeymboebqpDrr2JqgWCnXB4ewSOfXjsz9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت خودروسازی سایپا، روز پنجشنبه ۱۲ شهریور ماه و چند روز پس از آغاز ثبت‌نام طرح فروش فوق‌العاده، با صدور اصلاحیه‌ای رسمی، بهای مصوب چهار محصول عرضه‌شده را به بهانه «افزایش هزینه گواهی اسقاط خودروهای فرسوده و سایر عوارض قانونی شماره‌گذاری» به‌طور چشمگیری بالا برد.
بر اساس جدول جدید منتشرشده، بهای مصرف‌کننده «کوییک اس» و «سهند اس دوگانه‌سوز» هر کدام ۳۳ میلیون تومان گران‌تر شده و به ترتیب به یک میلیارد و ۳۲ میلیون و ۵۱۰ هزار تومان و یک میلیارد و ۱۲۳ میلیون و ۶۸۸ هزار تومان رسیده است.
در بخش خودروهای مونتاژی و وارداتی نیز قیمت «سیتروئن سی۳-ایکس‌آر نسخه وی‌یک» با افزایش ۱۱۵ میلیون و ۵۰۰ هزار تومانی به ۳ میلیارد و ۳۸۹ میلیون و ۳۲۲ هزار تومان و قیمت «چانگان سی‌اس ۵۵ پلاس» با جهش ۱۹۸ میلیون تومانی به ۵ میلیارد و ۸۱۹ میلیون و ۱۲ هزار تومان افزایش یافته است.
این در حالی است که متقاضیان در روزهای گذشته بر مبنای نرخ‌های اولیه اقدام به ثبت درخواست کرده بودند و حالا این محصولات با موعد تحویل ۹۰ تا ۱۲۰ روزه با نرخ‌های جدید تحویل داده خواهند شد.
روز چهارشنبه ۱۱ شهریور، بازار آزاد نیز با موج تازه‌ای از گرانی همراه شد و چند خودروی داخلی دیگر جهش قیمت داشتند.
به‌طوری‌که تارا اتوماتیک با رکوردشکنی و رشد حدود ۱۰۰ میلیون تومانی به محدوده ۳ میلیارد و ۷۵ میلیون تومان رسید. بر اساس گزارش فرارو، در همین روز دنا پلاس اتوماتیک با افزایش ۲۵ میلیونی به ۳ میلیارد و ۱۹۰ میلیون تومان و پژو ۲۰۷ اتوماتیک پانوراما به ۲ میلیارد و ۹۸۰ میلیون تومان رسید و محصولاتی نظیر شاهین اتوماتیک پلاس و سورن پلاس دوگانه‌سوز نیز به‌ترتیب در سطوح قیمتی ۳ میلیارد و ۳۰ میلیون و ۲ میلیارد و ۴۱۰ میلیون تومان معامله شدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/78206" target="_blank">📅 14:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78203">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i8EXxC5XdT5uj54hfiUBKx8zrrLuEY2MBaeSPOZHIMe0ofoU0jfl5HaF28pCqkTcravt_9Bd54oa8Gy7OZC6fCaqR968bG3_BWrUyz4hjpWfQeJEORH_-FJ8kpUr_hYEJ7tE0SJ7DftxEzSYGJgjnWZtVdhGQGucq2fazxJwrKeTM_uvDZYF1HQ-KktAieCBolV92CCEOvmaG7lcpdIBriPpja4syhxdGeV6fwS96-Qkyw83onuauSGnnv-OfpqjMSZaHIFUw-8QkVId_BBIVRBa2YhOPGi8Y5M2sgIHhzFr5blDutFEzXKbMXgEUYjqBdT3RneL_uGrRSphVUGavg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین شریعتمداری، مدیرمسئول روزنامه کیهان، پنج‌شنبه ۱۲ شهریور در یادداشتی نوشت که ارتش و سپاه باید از «اهرم» عبور کابل‌های فیبر نوری بین‌المللی در خلیج فارس و تنگه هرمز برای «مقابله با آمریکا و متحدانش» استفاده کنند.
مدیرمسئول روزنامه کیهان نوشت: «در عمق آب‌های خلیج فارس و تنگه هرمز یکی از شاهراه‌های فیبر نوری بین‌المللی جای گرفته است. شاهراهی که بیشترین ارتباطات اینترنت، تماس‌های بین‌المللی، تراکنش‌های بانکی، سرویس‌های ابری (iCloud) و حتی ارتباطات هوش مصنوعی و دیتاسنترها از همین کابل‌ها عبور می‌کنند.»
حسین شریعتمداری، نماینده خامنه‌ای در روزنامه کیهان، تاکید کرد: «سخن با مسئولان کشور و مخصوصا با ارتش و سپاه است؛ خوب نگاه کنید! کابل‌های اینترنت جهانی از زیر آب‌های تنگه هرمز و خلیج همیشه فارس برایمان دست تکان می‌دهند و با هزار زبان می‌گویند چرا نقش ما را در این جنگ فراموش کرده‌اید؟»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/78203" target="_blank">📅 14:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78202">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NP8zONZXMvludZukkapUJK2VqWXSD4qtJxTL2tvphLOpzZxSpQB2vexw7DQfVyEjaNsGimZZ82Q9cvtF8SsA8Hey6TeXMDQZr7J1vhcQDQzHqs7TUakK5GabMOLJsLHxmLTURW3EKXQ7IXmpBAXV9sWGlspkjcOIXCk1ei2yuFwhGCCng5TJsq8hqXRM02F7KO6yJ36PUU-uBOG9MOM9mcf9obajsFVbqMmvErdpXlPSvaFdtZRihFAaER1uMElZs37uj6UJ-OH35hZSFL0-7K1EaAXPOG2b2IDUl-8QUesytwacHatYkvBe1dplmDTu_3ZjqRTkMwY0JjKTf1OCEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با ادامه افزایش نرخ ارز در ایران، قیمت پوند بریتانیا پنج‌شنبه ۱۲ شهریور در بازار آزاد برای نخستین بار از مرز ۳۰۰ هزار تومان عبور کرد و تا زمان تنظیم این گزارش به ۳۰۰ هزار و ۲۸۰ تومان رسید.
در همین حال، دلار در بازار آزاد با قیمت بیش از ۲۲۲ هزار تومان معامله شد و قیمت یورو نیز از ۲۵۸ هزار تومان عبور کرد.
قیمت سکه امامی نیز از ۲۳۵ میلیون تومان عبور کرد و نیم‌سکه به ۱۲۰ میلیون تومان رسید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/78202" target="_blank">📅 14:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78201">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qTXC46wSXiP-B7aN7-cCQQdniQTiA5YBbDxXHYsgG2W8RgqoNcFvRP4NWFX-Uoycfceq8UoSjbkw0SZgAjdsFi3NhNqGcEPEFaL1093Z-0MVaj-LG1tyfQMGHgiO2hchvDhr35hQaebIYrE44aNElP_QlsUH6jRlRniMz82bx0NSCoDugL9SoeHK-syZTcAxe0c7U9g1CGAakfGztacSU8xSsDJCCgb2shSHqOIMPj9oaC-nDs4aNTgg82zzR6s-2CJeUAI3FpR6ohaL3OxpP2jCz_ZBfWFXfDAdWVgeFRH1_vQeOg9s6KJeChGAETg4kY7zDTSM3A-uePwwvh4Uzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوان عالی کشور حکم ۱۲ سال و شش ماه و یک روز حبس، مصادره تمامی اموال و دو سال محرومیت از کافه‌داری برای صادق ساعدی‌نیا، مدیر کافه‌های زنجیره‌ای «ساعدی‌نیا»، را تایید کرده است.
خبرگزاری میزان، ارگان رسانه‌ای قوه قضاییه، روز پنج‌شنبه ۱۲ شهریور ۱۴۰۵ اعلام کرد این حکم به‌دلیل حمایت ساعدی‌نیا از اعتراضات دی‌ماه ۱۴۰۴ و تعطیل‌کردن واحدهای صنفی زیر مجموعه این برند صادر شده است.
براساس اعلام قوه قضاییه، صادق ساعدی‌نیا به اتهام «فعالیت رسانه‌ای و تبلیغی علیه امنیت کشور به نفع گروه‌های معاند» به ۱۲ سال و شش ماه و یک روز حبس تعزیری و مصادره تمامی اموال منقول و غیرمنقول خود به نفع دولت محکوم شده است.
دادگاه همچنین او را پس از پایان دوران حبس، به دو سال محرومیت از فعالیت در حرفه کافه‌داری محکوم کرده است.
قوه قضاییه انتشار مطالب اعتراضی در اینستاگرام، حمایت از فراخوان‌ها، تعطیل‌کردن کافه‌ها و فروشگاه‌های مجموعه و تشویق کارکنان به شرکت در اعتراضات را از مصادیق اتهامات او اعلام کرده است.
براساس کیفرخواست، صادق ساعدی‌نیا با سه عنوان اتهامی شامل «فعالیت تبلیغی یا رسانه‌ای برخلاف امنیت کشور»، «اقدام عملیاتی برای گروه‌های مخالف جمهوری اسلامی» و «فعالیت تبلیغی علیه نظام» محاکمه شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/78201" target="_blank">📅 14:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78200">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aXMD09m_2FTwcTszfaVFmAJJ5DjT2kSfKd7hTHu1mE3lCtSL2aimCNf_zO5uHAgMCGnuEZS2tjC7kdo3EIt3IX4NfFlfGMCYIw2c51KhEkPZVgDsIt0YM932D1cqQRFjcNcN5xgFdi1e_ZbpMob5WB0qtuYkuYmzrZOfO28PZBbEfsuLykxIScQ8w3Nl0lF0fyTvJdoFkzxBWAilZ4LuPHqXZvoc1pd1u4VM0rTSVi_8ZAbJEo_v-wU0J4-FD2YK2EgkH1CjZBzR73uQnIplUwfxi70ABLf5_qp_N4xUHmni3E-QULhJzchEqGdneN3T3u3J1SSQvB6JUurLva2lfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر دریافتی: هشدار در کویت
ترجمه ماشین:
⚠️
هشدار: خطر قریب‌الوقوع
تهدید امنیتی
از همه خواسته می‌شود در مکان‌های امن باقی بمانند و برای حفظ ایمنی عمومی، از پنجره‌ها و فضاهای روباز و در معرض خطر دوری کنند.
دفاع مدنی – وزارت کشور
آپدیت:
کویت: ایران حمله کرده
متن پست ارتش کویت، ترجمه ماشین:
پدافند هوایی کویت در حال حاضر در حال مقابله با حملات موشکی و پهپادهای متخاصم، در پی تجاوز جنایتکارانه ایران است.
ستاد کل ارتش اعلام می‌کند که اگر صدای انفجار شنیده شود، ناشی از رهگیری حملات متخاصم توسط سامانه‌های پدافند هوایی است.
از همه خواسته می‌شود دستورالعمل‌های امنیتی و ایمنی صادرشده از سوی نهادهای ذی‌صلاح را رعایت کنند.
KuwaitArmyGHQ
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/78200" target="_blank">📅 05:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78199">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">آکسیوس:
ویتکاف در بحبوحه تشدید فشارها علیه ایران با مقام قدرتمند اماراتی دیدار کرد
ترجمه ماشین:
استیو ویتکاف، فرستاده کاخ سفید، آخر هفته گذشته با مشاور امنیت ملی امارات متحده عربی دیدار کرد تا درباره گام‌های بعدی در قبال ایران گفت‌وگو کند؛ این را دو منبع مطلع از این دیدار گفته‌اند.
چرا مهم است:
این گفت‌وگوها که کاخ سفید آن‌ها را اعلام نکرده بود و تاکنون نیز گزارشی درباره‌شان منتشر نشده بود، در شرایطی انجام شد که دولت ترامپ در تلاش است تنگه هرمز را بازگشایی کند و هم‌زمان ایران را از نظر اقتصادی تحت فشار شدید قرار دهد. ویتکاف در جزیره ساردینیا در دریای مدیترانه با شیخ طحنون بن زاید آل نهیان (TBZ) دیدار کرد.
▪️
امارات شریک کلیدی عملیات تحت رهبری آمریکا برای بازگشایی تنگه و هدایت نفتکش‌ها در عبور از آن بوده است. این کشور همچنین برای موفقیت کارزار فشار اقتصادی آمریکا علیه ایران نقشی حیاتی دارد.
▪️
طحنون بن زاید یکی از قدرتمندترین چهره‌های امارات است: او برادر محمد بن زاید، رئیس امارات، مشاور امنیت ملی این کشور و معاون حاکم ابوظبی است و بر منافع گسترده سرمایه‌گذاری و فناوری امارات نظارت دارد.
▪️
به گفته منابع، ویتکاف و طحنون بن زاید درباره گام‌های بعدی در بحران ایران تبادل نظر کردند و درباره مسائل دیگری نیز گفت‌وگو داشتند.
▪️
کاخ سفید به درخواست برای اظهارنظر پاسخ نداد.
زمینه خبر:
این دیدار چند روز پس از آن انجام شد که اسکات بسنت، وزیر خزانه‌داری آمریکا، «عملیات طرد اقتصادی» (Operation Economic Outcast) را اعلام کرد؛ تعهدی برای اعمال تحریم‌های سنگین علیه کشورها و نهادهایی که با جمهوری اسلامی تجارت می‌کنند.
▪️
به گفته یک منبع مطلع از این تماس، بسنت پیش از اعلام این طرح با طحنون بن زاید گفت‌وگو کرده بود.
▪️
در همان روزی که ویتکاف با طحنون دیدار کرد، وزارت خزانه‌داری آمریکا برای قطع دسترسی شعب اماراتی «بانک مصر» از نظام مالی آمریکا به‌دلیل معاملات این بانک با ایران اقدام کرد. اقدام پیشنهادی، تراکنش‌های دلاری این بانک را مسدود خواهد کرد.
▪️
بانک مرکزی امارات اعلام کرد «بررسی فوری» تراکنش‌هایی را که شعب این بانک مصری با ایران داشته‌اند، انجام خواهد داد.
نگاهی دقیق‌تر:
چند روز پیش از اعلام تحریم‌های دولت ترامپ، امارات تصمیم گرفت تمام تجارت، مبادلات بازرگانی و تراکنش‌های مالی با ایران را متوقف کند.
▪️
این تصمیم اقدامی چشمگیر بود، زیرا امارات — و به‌ویژه دبی — یکی از مراکز اصلی تجارت و صادرات مجدد برای ایران محسوب می‌شد. حجم تجارت دو کشور در سال ۲۰۲۴ به ۲۸ میلیارد دلار رسیده بود.
▪️
یک منبع دیگر مطلع از موضوع گفت مقام‌های اماراتی به دولت ترامپ گفته‌اند برای آنکه هر کارزار فشار اقتصادی علیه ایران مؤثر باشد، باید همه کشورهای کلیدی که با جمهوری اسلامی تجارت می‌کنند در آن گنجانده شوند.
پشت پرده:
به گفته دو منبع مطلع، تحریم‌های ثانویه قریب‌الوقوع دولت ترامپ علیه ایران یکی از عوامل تصمیم امارات بود، اما دلیل اصلی آن نبود.
▪️
به گفته منابع، ۱۱ اوت یک هیئت ایرانی برای گفت‌وگوهای دیپلماتیک کم‌سروصدا با مقام‌های اماراتی به ابوظبی سفر کرد.
▪️
منابع گفتند ایرانی‌ها در این گفت‌وگوها اعلام کردند که خواهان کاهش تنش و بهبود روابط هستند — پس از آنکه ایران در جریان جنگ هزاران موشک و پهپاد به سوی امارات شلیک کرده بود.
▪️
به گفته منابع، ایرانی‌ها حتی از امارات برای تأمین غذا و دارو درخواست کمک کردند و از اماراتی‌ها خواستند با تحریم‌های آمریکا همکاری نکنند؛ درخواستی که بلافاصله رد شد.
▪️
اما در چند روز بعد، سپاه پاسداران حملات خود به نفتکش‌های شرکت ملی نفت امارات را که تلاش می‌کردند از تنگه هرمز عبور کنند، تشدید کرد.
▪️
منابع گفتند اماراتی‌ها خشمگین شدند و تصمیم گرفتند تمام روابط تجاری با ایران را تعلیق کنند.
موضوعی که باید زیر نظر داشت:
مقام‌های آمریکایی گفتند مارکو روبیو، وزیر خارجه آمریکا، اوایل این هفته به همه سفارتخانه‌های آمریکا در سراسر جهان دستور داد درباره «عملیات طرد اقتصادی» یک پیام رسمی دیپلماتیک به عالی‌ترین سطوح دولت‌های میزبان خود ارائه کنند.
▪️
به سفارتخانه‌های آمریکا دستور داده شد از کشورها بخواهند «فوراً و به‌صورت نظام‌مند» تمام تجارت با ایران را قطع و فعالیت‌های تجاری غیرقانونی ایران را شناسایی کنند.
▪️
مقام‌های آمریکایی گفتند در این پیام دیپلماتیک تأکید شده است که کشورها، شرکت‌ها و افرادی که به تجارت با ایران ادامه دهند، در معرض تحریم و قطع دسترسی به نظام دلاری قرار خواهند گرفت.
▪️
یکی از مقام‌ها گفت پیام ویژه‌ای برای نمایندگی‌های دیپلماتیک آمریکا در ابوظبی، مسقط، هنگ‌کنگ، دوحه، لندن، برلین و چند پایتخت آسیای مرکزی ارسال شده است. در این پیام به آن‌ها دستور داده شده از دولت‌های میزبان خود بخواهند تمام شعب بانک‌های ملی و صادرات ایران را که با سپاه پاسداران مرتبط هستند، تعطیل کنند.
گام بعدی:
یک مقام آمریکایی گفت دولت ترامپ در حال تشکیل یک کارگروه بین‌سازمانی برای هماهنگی اجرای کارزار فشار اقتصادی علیه ایران و نظارت بر اجرای آن است.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/78199" target="_blank">📅 03:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78197">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h-jd3U9pdjwZFOPiGL0hVNbo5tBCvKbxjUJnn-4L8cXD2db7d6M1xeUw6LqwRwxHx5ocOJ1SmIBrEb0qv3-okAofmdKfCadsP8LGEz2get6zVSjT8oV18Z-v1ebxKyJy4i1L7voMjf3Ap2DmuoDpTLHo30xeV9CXRDAHwIs2oxw0UKTqxyfGVbZLEqgfozzeKEuIXzgP76wJGZIFIx7IKCruVIKtoVuvp1N3EXC5PiUk9kLJBchdq1rfBHFtiNP4lKVrOcTYPZoZKlh6F92nQ9cCLhbiJhSkqd8mdbWUS85oQ8llDExpKcKGmvSJvDEEMLwrv53hAa4ascJJvS7bdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4e08d6ca26.mp4?token=k4udHpokFUzeJDKBCRmGhdLZpuWpVvDv-jCYh8icTUGosZQwfNmwTO53an75ymb_j3oCZwnd25uW3Tj5DYb2hhw_pvBrQrLgVWAs-_oUK3EfAATaHNJW1qI3IVJ-_ob0_PwcRxX-Oy_i4wQ0YQGCuIxcMZkI5InxFGVHdlybg8efZ2ucsAEUdrd5a0oJjrR3RjdE2UHR-u_5glJAkTLv5435tX-kYbtiJy-JZKnKhrTOJz8ZL__wralnMi0ilcpcUhiYkgGK_j9wpCaXjRQ2x7P-O0SbuvYwn4OhNu23CjLq21hLTM7rsO7dgr6S6AcPoSAb8eRuq8kiuTMXE1gsCA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4e08d6ca26.mp4?token=k4udHpokFUzeJDKBCRmGhdLZpuWpVvDv-jCYh8icTUGosZQwfNmwTO53an75ymb_j3oCZwnd25uW3Tj5DYb2hhw_pvBrQrLgVWAs-_oUK3EfAATaHNJW1qI3IVJ-_ob0_PwcRxX-Oy_i4wQ0YQGCuIxcMZkI5InxFGVHdlybg8efZ2ucsAEUdrd5a0oJjrR3RjdE2UHR-u_5glJAkTLv5435tX-kYbtiJy-JZKnKhrTOJz8ZL__wralnMi0ilcpcUhiYkgGK_j9wpCaXjRQ2x7P-O0SbuvYwn4OhNu23CjLq21hLTM7rsO7dgr6S6AcPoSAb8eRuq8kiuTMXE1gsCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان حملات شب گذشته آمریکا به روستای کوهستک در سیریک، علاوه بر یک برج مخابراتی، دستکم دو خانه مسکونی هم هدف حمله قرار گرفتند.
کوهستک دیشب پنج بار هدف قرار گرفت که به نظر می‌رسد چهار موشک به یک محل اصابت کرده است.
بر اساس تصاویر دوربین مدار بسته، سه موشک اول به خانه محل عروسی اصابت می‌کند.
به نظر می‌رسد موشک چهارم به دکل مخابراتی همراه اول و موشک پنجم دوباره به محل عروسی اصابت می‌کند.
دکل مخابراتی با خانه محل عروسی حدود ۱۱۲ متر فاصله داشته است و چند خانه اطراف هم آسیب دیده است.
@
VahidHeadline
به گزارش خبرگزاری مهر، خانه مسکونی محل برگزاری عروسی ۱۳۶ متر با دکل مخابراتی که هدف حمله موشک‌های آمریکایی بود، فاصله داشت.
مقام‌های امداد و نجات جمهوری اسلامی و رسانه‌های دولتی ایران اعلام کردند بر اثر این حمله ۴ نفر کشته و ۶۸ نفر دیگر زخمی شدند.
کوچکترین قربانی این حمله، امیرعلی کریمی چهار ساله بوده است.
@
VahidOOnLine
آپدیت:
بی‌بی‌سی چند ساعت بعد خبرش رو ویرایش کرد و اسم سلاحی که نوشته بود رو عوض کرد ولی همچنان نوشتند موشک.
گویا پیش‌تر نیویورک‌تایمز هم درباره نوع پرتابه ادعای مشابهی مطرح کرده بود ولی بعدا پس گرفت.
با جست‌وجو دیدم یکی اینجا خیلی مفصل بررسی کرده:
Mk20002000B
آپدیت:
حال‌وش روز چهارشنبه ۱۱ شهریور ۱۴۰۵، به نقل از شماری از شاهدان محلی خبر داد که پیش از انفجار، صدای دو پهپاد در منطقه شنیده شده است.
این رسانه، علی ملاحی، صاحب خانه و پدر عروس، را یکی از شاهدان معرفی کرده است. او گفته پیش از وقوع انفجار صدای دو پهپاد را شنیده و پس از آن، ساختمان هدف قرار گرفته است.
شماری دیگر از ساکنان کوهستک نیز از مشاهده یک پهپاد یا شنیدن صدای آن خبر داده‌اند.
منابع محلی همچنین می‌گویند خسارت‌های واردشده به خانه تنها ناشی از ترکش انفجار در یک محل دیگر نبوده و یک یا چند پرتابه مستقیما به ساختمان اصابت کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/78197" target="_blank">📅 01:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78196">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2c4ae3e5e5.mp4?token=FLUtFwycosWnZG6sdNvAEwhs6flc6CQmGF3raDHzdOa_Fhg5sxzMmcYxKS_xkcCcf2k7jNBuIjE-YzkXfKpZ7x8yKKX1PLDcl6Xb9YA7afxsgKURRJUXgAipNUtj9rPWrZ-kJTNwa1wrvzgDnZHAxtZXm13nYun7YU8EM1yBOMcDTS-diDmzXKbYCJWxoLgdOsY_IvQFQKmiyFZk2z6PEPePUjAzqxRq3x-klyHCyVULfS9G1T2PK2TqkiLCGGNhUCNXwxRb--7he1W5xVh0Xc5r6B0pVPQYzcY1fp4XqzD2Xbh119N7_l69-iaq_GvgZko5USm_gZm104KHqQT6kC-IQeq9C1wNOrWaFDTmkh_KeNhMVl4BL7WQOmXxrhnv1BzolFQSkl1wwCiUROFlNpFQvvzwP84RjN15vzNS4O0pP8GUdKJlm-V2V0_3chyKgdyvmJ2aKQYwAH3-yvvBuRvKB9CpGHeCF4EEvfbPicybxpFR7LfxFIaj2Kz8-BIXylvOT8F-JEZL3qHtDoBJnNlxVi8QEbYPaebC-8HnBuayezc6ACJSJijpBgPHxu8cY4GSjTFmc0zxJtKXYYmwnUhjqIWGo_9df1pFExcisXPBM1nFmtD6bTwHoDMtx8RDRzaCoNRVf57pDFVquZmkZvKoTNo6_2h9AjKXYL4_imk" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2c4ae3e5e5.mp4?token=FLUtFwycosWnZG6sdNvAEwhs6flc6CQmGF3raDHzdOa_Fhg5sxzMmcYxKS_xkcCcf2k7jNBuIjE-YzkXfKpZ7x8yKKX1PLDcl6Xb9YA7afxsgKURRJUXgAipNUtj9rPWrZ-kJTNwa1wrvzgDnZHAxtZXm13nYun7YU8EM1yBOMcDTS-diDmzXKbYCJWxoLgdOsY_IvQFQKmiyFZk2z6PEPePUjAzqxRq3x-klyHCyVULfS9G1T2PK2TqkiLCGGNhUCNXwxRb--7he1W5xVh0Xc5r6B0pVPQYzcY1fp4XqzD2Xbh119N7_l69-iaq_GvgZko5USm_gZm104KHqQT6kC-IQeq9C1wNOrWaFDTmkh_KeNhMVl4BL7WQOmXxrhnv1BzolFQSkl1wwCiUROFlNpFQvvzwP84RjN15vzNS4O0pP8GUdKJlm-V2V0_3chyKgdyvmJ2aKQYwAH3-yvvBuRvKB9CpGHeCF4EEvfbPicybxpFR7LfxFIaj2Kz8-BIXylvOT8F-JEZL3qHtDoBJnNlxVi8QEbYPaebC-8HnBuayezc6ACJSJijpBgPHxu8cY4GSjTFmc0zxJtKXYYmwnUhjqIWGo_9df1pFExcisXPBM1nFmtD6bTwHoDMtx8RDRzaCoNRVf57pDFVquZmkZvKoTNo6_2h9AjKXYL4_imk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نشست خبری ترامپ
بخش‌های مرتبط با ایران به تشخیص و ترجمه ماشین
و متن زیرنویس تا اونجایی که جا می‌شد در یک پست:
🔺
خبرنگار:
ترامپ، شما امروز در تروث سوشال نوشتید: «مردم ایران چه زمانی قیام می‌کنند و می‌جنگند؟» خب، اگر این چیزی است که می‌خواهید، آیا سیا را می‌فرستید تا ایرانی‌ها را مسلح کند؟
🔻
ترامپ:
خب، نمی‌خواهم این را به تو بگویم، پیتر. خیلی دوست دارم به تو بگویم، اما گفتنش مناسب نیست. اما من... یعنی، من وضعیت دشوارشان را درک می‌کنم. همین حالا دارند به آن‌ها شلیک می‌کنند.
می‌دانید، این آقایان اینجا در ناز و نعمت نشسته‌اند و چیزهایی را می‌بینند، اما آنجا اوضاع چندان راحت و مرفه نیست. تا سه ماه پیش، ۵۲ هزار معترض کشته شده بودند. می‌توانید تصورش کنید؟ و حالا می‌شنوم که این تعداد احتمالاً ۲۰ تا ۲۵ هزار نفر دیگر هم بیشتر شده. نزدیک به ۶۵ هزار معترض کشته شده‌اند.
پس وقتی آن سؤال را مطرح می‌کنم، به‌نوعی جوابش را هم می‌دانم. تنها پاسخ این است که به آن‌ها شلیک می‌شود. رژیم هر روز ضعیف‌تر و ضعیف‌تر می‌شود و در مقطعی دیگر نمی‌توانند به این راحتی شلیک کنند، چون فکر می‌کنم مردم دیگر این را تحمل نخواهند کرد.
اما من آن سؤال را مطرح کردم چون، می‌دانید، وقتش رسیده است. اما بیشترِ... بیشتر مردم نمی‌توانند مردم خودشان را این‌طور بکشند. بیشتر مردم سعی می‌کنند منطقی برخورد کنند، گفت‌وگو می‌کنند و بعد ممکن است حکومت سرنگون شود. در ایران، مردم را می‌کشند. وقتی برای اعتراض بیرون می‌آیند، آن‌ها را می‌کشند. درست بین دو چشمشان شلیک می‌کنند.
آن‌ها دو روش دارند: مسلسل و تک‌تیرانداز، و از هر دو استفاده می‌کنند؛ گاهی مسلسل‌ها و گاهی تک‌تیراندازها. تک‌تیراندازها را بیشتر دوست دارند، چون کافی است جمعیتی ۲۰۰ هزار نفری باشد و یک نفر همین‌جا با گلوله‌ای بین دو چشمش به زمین بیفتد، و سه تک‌تیرانداز این کار را انجام دهند؛ و تماشای آن وحشتناک است. واقعاً وحشتناک است.
برای همین است که این اتفاق نمی‌افتد. و چه کسی می‌تواند سرزنششان کند؟ چه کسی می‌تواند سرزنششان کند؟ اما رژیم هر روز ضعیف‌تر می‌شود.
—————-
ما  داریم تنگه هرمز را کنترل می‌کنیم. ما داریم هر روز کشتی‌های زیادی را خارج می‌کنیم که میلیون‌ها بشکه نفت حمل می‌کنند. در بیشتر موارد این کار را بدون مشکل انجام می‌دهیم. هر از گاهی آن‌ها یک پهپاد می‌فرستند و ما آن را ساقط می‌کنیم.
اما ما کنترل داریم؛ کنترل بسیار قدرتمندی. آن‌ها تلاش می‌کردند سامانه‌های راداری و یک سامانه موشکی و سامانه‌ای برای ریختن مین را بازسازی کنند. می‌دانید، ما همه مین‌ها را در تنگه هرمز از بین بردیم. آن‌ها تلاش می‌کردند موشکی بسازند که مین می‌ریزد. چه کسی چنین کاری می‌کند؟ تا حالا موشکی ساخته‌اید که مین بریزد؟ من هرگز چنین چیزی نشنیده بودم، اما این کاری بود که آن‌ها می‌کردند.
داشتند آن را می‌ساختند. تقریباً تمام شده بود، پس ما نابودش کردیم. دیدیم که داشتند آن را می‌ساختند. ما هر کاری را که می‌کنند می‌بینیم. نمی‌توانند تکان بخورند. حتی نمی‌توانند به دستشویی بروند بدون اینکه ما ببینیم. پس آن را دیدیم. نابودش کردیم.
...
بنابراین دیشب محکم به آن‌ها حمله کردیم؛ خیلی محکم. آن‌ها یک ضربه خیلی کوچک زدند، اما ما دیشب خیلی محکم به آن‌ها حمله کردیم. همه تجهیزات جدیدی را که تلاش کرده بودند در امتداد تنگه هرمز بسازند نابود کردیم؛ بعضی دفاعی و بعضی تهاجمی.
آن‌ها سعی می‌کردند کشتی‌ها را ببینند، چون نمی‌توانند کشتی‌ها را ببینند. می‌دانید، ما تعداد زیادی از کشتی‌ها را از بین برده‌ایم. آن‌ها نمی‌توانند ببینند، چون رادار ندارند، چون ما آن را منفجر کردیم، و دیشب چیزهای بسیار بیشتری از فقط رادارشان را منفجر کردیم.
دیشب حمله بسیار سنگینی بود و آماده‌ایم هر زمان که بخواهیم، حمله دیگری انجام دهیم.
....
بنزین با آن قیمت فروخته می‌شد؛ چون نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد.
...
اما مسئله خیلی ساده است. ایران نمی‌تواند سلاح هسته‌ای داشته باشد. به‌محض اینکه تمام شود، که فکر نمی‌کنم خیلی بیشتر طول بکشد، نمی‌دانم چقدر دیگر می‌توانند تحمل کنند، اما می‌دانید، هرچه باشد، اهمیتی ندارد.
و انتخابات روی من تأثیری ندارد. اول اینکه، من نامزد نیستم. اما حزب من نامزد دارد و من قرار است به حزبم کمک کنم. اما فکر می‌کنم حزب من به این واقعیت احترام می‌گذارد که ما اجازه نمی‌دهیم ایران سلاح هسته‌ای داشته باشد.
————-
🔺
خبرنگار:
آقای رئیس‌جمهور، چقدر درباره تغییر نام تنگه هرمز به «تنگه ترامپ» جدی هستید؟ و اگر جدی هستید، چطور این کار را انجام می‌دهید؟ چطور این کار را می‌کنید، آقای رئیس‌جمهور؟
🔻
ترامپ:
فقط همین‌طوری مطرح شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/78196" target="_blank">📅 22:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78195">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/583f7fe047.mp4?token=CxnCKKpYYTKO8LkMlPxg9YkEFvOqWe4JzhYr5fylfp3x5qknaI9eOTmPIL1ihRr-F0vJXehTODAo2ghpsbfbMjvepugjUIs7e88Zvr4kKjUA4DHq6nmVGaKrrgKY6a8H-knN2dssREzHDUoM7jMxJT_Ogdrlqwq_waozZgSZgLdfKtyHU4cLSOqO_sqm8Zd7omNL60BAH50ADek38YsIEf97Tk5mVKXxB_HjHuMuXuPBRK58Ls0LHMudvpb9G6D5KzMQTc9RhIY654Tvy9n1EXX_tsh94yokyhiT8I4rlfI-f8xudoxriXWlEV6bcJLxZAZyh0-bWYMmlCW0sZxadQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/583f7fe047.mp4?token=CxnCKKpYYTKO8LkMlPxg9YkEFvOqWe4JzhYr5fylfp3x5qknaI9eOTmPIL1ihRr-F0vJXehTODAo2ghpsbfbMjvepugjUIs7e88Zvr4kKjUA4DHq6nmVGaKrrgKY6a8H-knN2dssREzHDUoM7jMxJT_Ogdrlqwq_waozZgSZgLdfKtyHU4cLSOqO_sqm8Zd7omNL60BAH50ADek38YsIEf97Tk5mVKXxB_HjHuMuXuPBRK58Ls0LHMudvpb9G6D5KzMQTc9RhIY654Tvy9n1EXX_tsh94yokyhiT8I4rlfI-f8xudoxriXWlEV6bcJLxZAZyh0-bWYMmlCW0sZxadQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کریس رایت، وزیر انرژی آمریکا، و دلسی رودریگز، رئیس‌جمهور موقت ونزوئلا، روز چهارشنبه توافقی نفتی را در کاراکاس امضا کردند که بر اساس آن ایالات متحده کنترل اکثریتی بر ۶۵ میلیارد بشکه از ذخایر نفت ونزوئلا به دست می‌آورد.
این میزان حدود یک‌پنجم ذخایر عظیم نفتی ونزوئلا را شامل می‌شود. دونالد ترامپ، رئیس‌جمهور آمریکا، این توافق را «بزرگ‌ترین معامله نفتی در تاریخ جهان» توصیف کرده است.
بر اساس این توافق، آمریکا به ۱۷ میدان نفتی ونزوئلا دسترسی ترجیحی خواهد داشت؛ تأسیساتی که برخی از آنها پیشتر در اختیار شرکت‌های روسی و چینی بوده‌اند.
همزمان، شرکت شورون نیز از توافق جداگانه‌ای به ارزش هفت میلیارد دلار برای توسعه دو میدان نفتی دیگر در کمربند اورینوکو خبر داده است. شورون می‌گوید این سرمایه‌گذاری می‌تواند تولیدش در ونزوئلا را طی پنج سال بیش از دو برابر کند.
وزیر انرژی آمریکا پیش‌بینی کرده است تولید نفت ونزوئلا تا پایان دهه جاری به بیش از دو میلیون بشکه در روز برسد؛ حدود دو برابر سطح تولید در ژانویه، زمانی که نیروهای آمریکایی نیکلاس مادورو را سرنگون کردند و دلسی رودریگز قدرت را در دست گرفت.
این توافق با انتقادهایی نیز روبه‌رو شده و منتقدان دولت رودریگز را به واگذاری حاکمیت ونزوئلا بر منابع نفتی خود متهم کرده‌اند. دولت ونزوئلا در مقابل می‌گوید این توافق به این کشور برای بهره‌برداری از ظرفیت‌های انرژی و جذب سرمایه‌گذاری کمک خواهد کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/78195" target="_blank">📅 22:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78193">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t4ldamT4239qd2OtgyEoMVD75HrILGdvM4E1M9QCeq_iJUiLg4_NBoXlGebpjCrjEPALoXh_lGV8sHI07fdMkgMPtV04BX4o53rAKs6Gz4WAVbJ8b4TM_q1oa-UmN4umUbcg87HJ83Ub_FJUzKHWPweuEM-z61Xp8kPtTwgSiCSa07gcu0Dp8pz9852diCItHuZQf_z5gpzNj0b1HDoMQ9GXSEbN69_iKT3UVgwIm-0z5DXQ2w0av2Uch9tDlqvnZRdt-NAD29YljnsQvmi3CDkonuewgYY4vN3JjvF4IQCb9KYMYXOF3K_yNslfO8JOiWvl8g-otJUfEYjDjznfHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b44a8875b1.mp4?token=unZdiW7ygSNobUrJJKb9gDeDiWbpiKNrkCVLTIBt5HlLpbniiDcNhe0gTosjiNe4NqG03VU-m9A035TqL5KqckpDRYJVC-V55WT2lyzjetJWUDAB_jpbEFzyclK7OLDgovZmAq8JwiM3-ao6OSZzrR1GGQn53gGMsV2oXZmh4S7xoEI1u-d2gGHPweUWCwg6L8mSa8bWVB3-wXwt7JPqwKcE0rUWiac83l9cIwisAuYg7aJywCOxzQ2mU4yFIu4VmJaSMUk5PLaFFnzVfbc9wUoPUI4KaK6X68T9p6OgzEcro5cDlDyS0Kg5yS6AbFZQYKtC3N2UnFAinUxBMILbkw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b44a8875b1.mp4?token=unZdiW7ygSNobUrJJKb9gDeDiWbpiKNrkCVLTIBt5HlLpbniiDcNhe0gTosjiNe4NqG03VU-m9A035TqL5KqckpDRYJVC-V55WT2lyzjetJWUDAB_jpbEFzyclK7OLDgovZmAq8JwiM3-ao6OSZzrR1GGQn53gGMsV2oXZmh4S7xoEI1u-d2gGHPweUWCwg6L8mSa8bWVB3-wXwt7JPqwKcE0rUWiac83l9cIwisAuYg7aJywCOxzQ2mU4yFIu4VmJaSMUk5PLaFFnzVfbc9wUoPUI4KaK6X68T9p6OgzEcro5cDlDyS0Kg5yS6AbFZQYKtC3N2UnFAinUxBMILbkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا در گفتگو با شبکه نیوزمکس گفت که ایالات متحده لزوما به دنبال فروپاشی جمهوری اسلامی ایران نیست، هرچند تحولات درونی و قیام مردم امکان‌پذیر است.
او همچنین به مخاطرات شخصی پیش‌روی رهبران و فرماندهان نظامی ایران با افزایش فشارها اشاره کرد.
بسنت ادعاهای ایران درباره کنترل بر تنگه هرمز را رد کرد و گفت با عبور حدود ۱۷ میلیون بشکه نفت در روز گذشته، کنترل ایران بر این تنگه بی‌معناست. او همچنین گزارش‌ها درباره وجود مین یا برخورد دو کشتی با مین در تنگه هرمز را تکذیب کرد و رسانه‌ها را به بازنشر سریع ادعاهای نادرست ایران متهم ساخت.
وزیر خزانه‌داری آمریکا، با اشاره به تداوم خرید نفت ایران توسط چین تاکید کرد که تنها حدود ۳۰ میلیون بشکه نفت ایران روی آب باقی مانده و این ذخایر نیز به‌زودی به پایان خواهد رسید.
بسنت روز گذشته نیز در جریان سخنرانی در مجمع اقتصادی جی۲۰، تاکید کرده بود که فشارهای اقتصادی یا به ایجاد شکاف و دودستگی در سپاه پاسداران و احتمالا مقابله مردم با آن‌ها منجر می‌شود یا مقام‌های تهران تصمیم می‌گیرند که به میز مذاکره بازگردند.
@
VahidOOnLine
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در گفت‌وگو با شبکه آی‌۲۴ درباره حکومت ایران گفت: «نیروهای ما می‌توانند هر لحظه در آنجا باشند. ما این حکومت را شکست خواهیم داد.»
نتانیاهو درباره اینکه آیا منظور او از شکست دادن، سقوط کردن حکومت است، گفت: «بله، سقوط خواهد کرد و ما آن را سرنگون می‌کنیم.»
نتانیاهو در پاسخ به این سوال که آیا رومان گوفمن، رییس موساد، برای سرنگونی جمهوری اسلامی فعالیت می‌کند، گفت: «همه دستگاه‌های ما تحت هدایت من برای سرنگونی این حکومت و شکست آن فعالیت می‌کنند.»
نتانیاهو گفت: «در نهایت با سر اختاپوس، برخورد خواهیم کرد، بازوها را قطع خواهیم کرد و محور شر ایران را هدف قرار خواهیم داد. این کار را با قدرت بسیار انجام دادیم؛ خلبانان ما آنجا بودند و هر لحظه می‌توانند آن جا باشند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/78193" target="_blank">📅 21:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78192">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KfyC7K9IPfSVZu6UvZNC18jo35YSyRJ6dRHqCjY-Gw1M2Aq_WUZ27olFdJU2YILfiET5lm2O-KsZA1kDC71fb7BmXOpe4_EJ61IRSjcJNE3ZBK_n60mVqN-ntTLWfIKCeLZHinJtYzy-uEOfhVpu1ivppHPWelF8ywrcUdm-gPmDAJ-ElAm5IvWPZRRqjRCgITz3vs8UCLrc-esPiQ0pcd4VnKuaiRjji4U9crR0GTZNEyJk7vjDSh31J4CYz9xqCRO0Q2GyG3ixrose0-eL7kkfsaiNg7xpl2JC5wwSyJNZFVky3mQ33XUutvqFn9hfnLZJ-nBY5HFQK-CZQjjQQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی جمهوری اسلامی، با هشدار به ایالات متحده گفت تهران در جنگ جاری از «راهبردی جدید» استفاده خواهد کرد.
رضایی، چهارشنبه ۱۱ شهریور ۱۴۰۵، در پستی در ایکس نوشت که تلاش‌های آمریکا برای خروج از شرایط کنونی نتیجه‌ای نخواهد داشت و افزود: «به‌زودی خواهید دید که راهبرد جدید ایران در میدان نبرد، دیپلماسی و مقابله با محاصره اقتصادی، پایه‌های شما را درهم خواهد شکست.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/78192" target="_blank">📅 19:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78191">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ac0X2ZYz76Rsc_7i0OjabNEISk_tQU69DJFKZs0ZBwHf1pDQ13M8Iw_yWqdavVa76r-KslbjsbpKQeF9jH797eG0mGrpK0KDy8eD2-fLz5oeQ3Lu99u8ym2ogRHSWAVDd_XYjMeL4YC5Hvx7uoXOiDBH1EWcbMf3llHgCStRVxo4qyNAGRApgCAhQZx4AU1vxicc3EhseeNqtlIScsgTjkcoqT0HpoUC6uMwS429tco578zDn6zO-VIAior_yPIWBDsLqGLABm7Rg7ilgGGt0ZTptsZyHwbnA4HLLdbP7sIPiHWFjHSyJiVr5Zxh8Bq0bZf0oVhcT2_jb5lxa-uERg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
حالا که آن را تحت کنترل ایالات متحده آمریکا درآورده‌ایم، آیا باید نام «تنگه هرمز» را به «تنگه ترامپ» تغییر دهیم؟؟؟ درست مثل خود آمریکا، این تنگه هم «داغ‌تر» از هر زمان دیگری خواهد بود!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
Now that we have it under U.S.A. control, should we change the name Hormuz Strait to TRUMP STRAIT??? Like America itself, it would be “hotter” than ever before! Thank you for your attention to this matter. President DONALD J. TRUMP
realDonaldTrump
در خبری دیگر:
ترامپ در گفت‌وگو با پادکست «دن پاتریک»، درباره حملات سه‌شنبه شب آمریکا در اطراف تنگه هرمز، گفت: «ما اکنون کنترل تنگه هرمز را در اختیار داریم. ما آن را کنترل می‌کنیم. دیشب ۲۸ کشتی را از بین بردیم. ما آن را کنترل می‌کنیم، آنها چیزی دریافت نمی‌کنند و ما کشتی‌ها را از بین بردیم.»
ترامپ همچنین درباره حکومت ایران گفت که جمهوری اسلامی دو هفته با داشتن یک سلاح هسته‌ای فاصله داشت. او افزود: «اگر آنها سلاح هسته‌ای داشتند، اسرائیل از بین می‌رفت، خاورمیانه از بین می‌رفت و آنها به شهرهای ایالات متحده حمله می‌کردند. چون آنها دیوانه هستند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/78191" target="_blank">📅 19:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78190">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KuanU2jArCq8rtHoIsymXaxbLtzIyBzaU2bFo346VIYNpRwu94vbIRhmAQoHIoZpdVEskj8YpyCVH9GJCGQj-ltIbM9HlpxgfDJamQBNUKSAOSXiTEeIH0TGyeVQstkVlMAPJOWe15qN4YtjccSXo_-U5-KlW48Ux5VbtKXNfzy-7IJx5E3wWsNblnFvcLzioYM3n5f9CCYgjEn_JG8D2nQYQgTVn2-G8wdGUp53jOztjFzc_FoY2vKeDSuUZMS57zje6NNPeYeymRlBTAoOxCBapghECXsoxLzt3NShVWz976cKy9QBGh0gU68ayNYhQuKTYy3kSL660WyLiVKv-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رییس مجلس شورای اسلامی گفت: آمریکایی‌ها باید به تعهدات خود عمل کنند تا ما اقدام به بازگشایی تنگه هرمز کنیم.
محمدباقر قالیباف، در دیدار با مسئول ارتباطات اسلامی حماس گفت جمهوری اسلامی مذاکره را رد نمی‌کند، اما آن را «ابزاری برای مبارزه» می‌داند.
او گفت کنار گذاشتن مبارزه با آمریکا و اسرائیل به معنای شکست است.
او افزود جمهوری اسلامی در جریان مذاکرات، پایان جنگ علیه ایران و متحدانش در «جبهه مقاومت» را در ماده نخست تفاهم‌نامه مطرح کرد، در حالی که به گفته او، طرف مقابل در متن اولیه ۱۵ ماده‌ای خواستار توقف کامل فعالیت‌های موشکی، هسته‌ای و فعالیت‌های «جبهه مقاومت» شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/78190" target="_blank">📅 19:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78189">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vfKt_J9yHCATSwe2PclpmBsiD5AhI-DtefA-YQrSZ_92tOpuWQ6i6v4K1VhBuNNHaL_1NWQNQ6A-htvsAtAO6XY-V7AF2yJE1-0BNTmPbgN7vs1lnhpyRIAkNWBoKoC3wKwSC_Y2TwmA21DmnVXWqTMv1ibldugw-JitqjmYk7ocIhw7rx6Mvb5xlIqiazrPY3rEYjIf1cKIpf-8rHGfFZ03Ce3ecH9xHPLYbhGl1XLJNmUN8b8XSuoOjsxfOEAX8ExFxQyoVsXfy-SUr9FXIOx6UtvPh3XQsrHmrI-JW_dVnKZS6M5mcn6fc9LdkrVKjZN_p3e9YkbFsMgrwAqi6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس آمارهای اعلام شده از سوی شرکت ملی پخش فرآورده‌های نفتی ایران، میانگین مصرف روزانۀ بنزین در نخستین هفتۀ شهریورماه از مرز ۱۴۸ میلیون لیتر گذشته است.
بر اساس این آمارها، بیشترین میزان تقاضای روزانه در ۸ روز نخست آخرین‌ماه تابستان، بیش از ۱۵۴ میلیون لیتر بوده و در این بازه در مجموع بیش از یک میلیارد و ۲۰۰ میلیون لیتر بنزین عرضه شده است.
کاهش شدید ظرفیت تولید در ماه‌های اخیر در اثر حملات آمریکا به تأسیسات نفتی ایران از یک‌سو و مشکلات دولت برای وارد کردن بنزین از سایر کشورها از سوی دیگر، باعث افزایش قیمت بنزین و حتی مطرح شدن احتمال بالاتر رفتن قیمت این فراورده و افزایش شدید تقاضا برای آن شده است.
مسعود پزشکیان رئیس‌جمهور و شماری دیگر از مقام‌ها تأکید کرده‌اند که دولت توان چندانی برای وارد کردن بنزین و بخصوص عرضۀ آن با قیمت‌های قبلی ندارد.
دولت ایران اما در عین حال ادعا می‌کند که تشکیل صف در برخی جایگاه‌های عرضۀ بنزین، ناشی از هیجان و بار روانی بوده و مشکلی در تأمین بنزین مورد نیاز کشور وجود ندارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/78189" target="_blank">📅 17:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78188">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q5IyyuoZkZowXfHNMNMnKEZd88ZcGgk2_8eTR45FyknbdtQu1K-O1rcHjZL8knZ3kTn9olaStr4Nd57ws3B0oVavcf9Tq3ehogYJ_rpS0DklF_QlcMSIHM1OzNs9yMvk7O-DjEHvOKW6u1vTAbks2N6_06zwSYVesO_nECm6YOX2bscU2Hh3u4XlFaC4iqTVq3-rjky8OLVIJZCgVB0255t971A1OfTpM6gcI5woWBA71OjYVgJTQptYf81ilKrZ2iZJRphDOPzPTx7GjlaUubWjTlYxSdOuJwhLGaMfJgJWBpVth7k4OxJLqC9vzA2ifXtrDuwABVB0ia6dh6QSEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت ارزهای خارجی در ایران بامداد چهارشنبه ۱۱ شهریور و ساعاتی پس از دور جدید حملات آمریکا، رکورد تازه‌ای ثبت کرد و قیمت یورو، پول واحد اروپایی، برای نخستین بار از مرز ۲۵۵ هزار تومان گذشت.
وب‌سایت‌های اعلام نرخ ارز قیمت دلار از جمله «نوسان»، قیمت دلار آمریکا را حدود ۲۲۰ هزار تومان گزارش کردند. قیمت درهم امارات هم به بیش از ۶۰ هزار تومان رسیده است.
افزایش قیمت نرخ ارزهای خارجی در بازار آزاد ایران از زمان اعلام امارات در قطع روابط مالی با ایران و آغاز برنامهٔ فشار اقتصادی آمریکا موسوم به «عملیات طرد اقتصادی» شدت گرفته است.
در دو هفته اخیر پول ملی ایران در مقابل ارزهای عمده خارجی بیش از ۱۰ درصد دیگر از ارزش خود را از دست داده است.
روز چهارشنبه قیمت سکه طلای موسوم به «امامی» هم با وجود کاهش جهانی قیمت طلا، ۲۲۴ میلیون تومان گزارش شد.
عبدالناصر همتی، رئیس‌کل بانک مرکزی، روز ۱۰ شهریور ادعای کمبود منابع ارزی و احتمال فروپاشی اقتصاد ایران را رد کرد و گفت بانک مرکزی آماده است برای مهار بازار تا دو میلیارد دلار ارز عرضه کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/78188" target="_blank">📅 16:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78187">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tYjVEiEfiVPMkiJvrnWi7AmWv2h_lSk8OMPo8h4a2QdNCpZbFwqeuESWftoXZyKJjZm6x0c5gTIVIk23lr9HldghnDUVGeBYw1HAfH2tgMI0s8XZ9lm1hLwWkpSP4d_oM2YRZ0CL29b5jA-4nQp1WDEjTOv65ydz2w58d5vWjzo6fVnVefJxOMt8tUsygIARR2PM4A6c3CayvV_GKwcX7cChqbZ-HWauQ6kaS3ZLLPq3At3STyzkoM_gZY9PQWuAA935Rk26Nl9IsPPweHMjWOaksT6gbjG0vrCCYDjLw2mD1Ry5W0PPxjfrF4ekcm3AKXhVIlTyIWZrpTNlFyDVrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وب‌سایت اکسیوس به نقل از مقام‌های آمریکایی گزارش داد که ارتش ایالات متحده در جریان موج حملات شامگاه سه‌شنبه دهم شهریور به اهدافی در جنوب ایران، «دو نفتکش دولتی» این کشور را نیز هدف قرار داده است.
بر اساس این گزارش، این دو نفتکش در نزدیکی سواحل ایران و در شمال خط محاصره دریایی آمریکا لنگر انداخته بودند و پهپادهای آمریکایی با شلیک موشک موتورخانه‌های آن‌ها را هدف قرار دادند.
فرماندهی مرکزی ارتش آمریکا، سنتکام، در بیانیهٔ رسمی خود پس از حملات سه‌شنبه‌شب اشارهٔ مشخصی به حمله به نفتکش‌ها نکرد، اما در تصاویر ویدئویی که از حملات منتشر کرد، صحنه‌ای از اصابت موشک به نفتکش نیز دیده می‌شود.
اکسیوس می‌گوید این نخستین بار است که ارتش آمریکا نفتکش‌های ایرانی را نه برای جلوگیری از نقض محاصره دریایی، بلکه در واکنش به حملات ایران به کشتی‌های عبوری از تنگه هرمز هدف قرار می‌دهد.
یک مقام آمریکایی این اقدام را بخشی از سیاست تازه‌ای موسوم به «نفتکش در برابر نفتکش» توصیف کرده که به‌گفتۀ او دونالد ترامپ برای بازدارندگی از حملات بیشتر ایران به کشتی‌ها تأیید کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/78187" target="_blank">📅 16:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78183">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromILIA HASHEMI</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sAbajTOFkRiSq_Jtt2-mTiZn5t7LhFdm6P5Z7e9qpLi_aoATgQgLw0uxJH8_ptep4je8lt5E7COMuNw4gkXj9vwv3xBEli-84_GBcgRmVyqaJX2K07USTisHbEADFQIS6sDD_jTZnHpDhOUoVECPV17VMef4E0ifdZmiuM5UVIoF9zuPJVFtwYwj-aE2D2grbfDsbNHZeE8xR_JpYu_hJVE69G0SA_7wzuD8a_kob4aLTvUN88ezb_dDdXkPOscTk1WClmJQlY5ZqNiQyBKNPC2FKRPDQhdi2ZYXoNIdKUkFRKKO_bWL6DLmPN6YOgL9nr8I5ra9X0RS4vTsV6e-fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ujWcQ4UUFw6wsNQly6njDvPMQKzsBmvInXXxeOIF2H6xH3obYNwB8OpinHC3fMGk2jQBNMwTH19ibDoxChx6b3i3S_dtKDjXqliXfriMzD0A_pFd3CaXu-Zy1536VGl66AZOTYxFHp7SMSarNdOyCzLG0ZwKf-NWI7xn_2zT4WWCHgJ_80q7OjrD9qu4HuQhIuJkg0JSPAwki3_Jqj5heLRIjUxFdAiUkDxOdoqoShybQRho7fRbMbVp2gZpBoqfCI-fWs8bUlG8qgZMCuZxmtHZnYjJEtwCVrujzlwwwBxgWNhWYgXT75RMpo4sYCd5e0fwG4s3gkrTZDGflNjHlg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/937ffb9011.mp4?token=PjllafmfuL6BjL1CO9pebGuhTNT-I_MAvQMrnY1_lE-ZmexJqQ20yh7TFRA9bEDZWotU5C-2VIEZGJd2Qeibq4FQAMxDKQoM8jRdZpEUbH380nY66j_8BBAzGDb7n6zPWjYs_tpRoaQ1jJj_wFBPLAQEyXg_ZyS4z8teI4RIaNW-qjnkgBboiMdO7j_EJUqhOq3LGyHF8LDZ0MsOt06SBvegbG2m3oyp4MuTz5sBjP5o1JyjE7-pP9_yQZsGSvhUCWYVcAFHFsPKCabjmCMK-jk2nbNCJIU-gD8M0HjBqjW79WIk4Cso0wErwYXDKPsBdZYP-Pf86mMIYMPwHXuozw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/937ffb9011.mp4?token=PjllafmfuL6BjL1CO9pebGuhTNT-I_MAvQMrnY1_lE-ZmexJqQ20yh7TFRA9bEDZWotU5C-2VIEZGJd2Qeibq4FQAMxDKQoM8jRdZpEUbH380nY66j_8BBAzGDb7n6zPWjYs_tpRoaQ1jJj_wFBPLAQEyXg_ZyS4z8teI4RIaNW-qjnkgBboiMdO7j_EJUqhOq3LGyHF8LDZ0MsOt06SBvegbG2m3oyp4MuTz5sBjP5o1JyjE7-pP9_yQZsGSvhUCWYVcAFHFsPKCabjmCMK-jk2nbNCJIU-gD8M0HjBqjW79WIk4Cso0wErwYXDKPsBdZYP-Pf86mMIYMPwHXuozw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح چهارشنبه؛ وضعیت چند منزل مسکونی در کوهستک (هرمزگان).
@iliaen</div>
<div class="tg-footer">👁️ 394K · <a href="https://t.me/VahidOnline/78183" target="_blank">📅 09:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78182">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/05113c6026.mp4?token=IJYNw-u7vCJez8Z3oRjexJ1bQcsLTEpsHJ44NRyNkCqPLO6XMkRKwBYWGoAvJSCoYuwQWrCzr_45nxEEUVwBAlXQrPW_1etABwEcrlsCoUSWfjpM_EXAR3M8doo_umyN4iJm2WY2l9mb5LW0gSE-r96Vne5qzhrmIOI4FC2p-dAGS1vwSIyg-t3M1NLIPlTOT11BL1oBSojMjv__YE40yAJbn7tgH4zUMw13h2Ynh-hqZE4g2ahW-4wjHiVTDXu3abIHVIR0xbmruMA68hRd9flEMau2iKRcBSUdj6HIPDwaqcqsf21KUHuvPCOpNjTffTa66kB2jCcH16ReJGBT5A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/05113c6026.mp4?token=IJYNw-u7vCJez8Z3oRjexJ1bQcsLTEpsHJ44NRyNkCqPLO6XMkRKwBYWGoAvJSCoYuwQWrCzr_45nxEEUVwBAlXQrPW_1etABwEcrlsCoUSWfjpM_EXAR3M8doo_umyN4iJm2WY2l9mb5LW0gSE-r96Vne5qzhrmIOI4FC2p-dAGS1vwSIyg-t3M1NLIPlTOT11BL1oBSojMjv__YE40yAJbn7tgH4zUMw13h2Ynh-hqZE4g2ahW-4wjHiVTDXu3abIHVIR0xbmruMA68hRd9flEMau2iKRcBSUdj6HIPDwaqcqsf21KUHuvPCOpNjTffTa66kB2jCcH16ReJGBT5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روستای کوهستک در سیریک هرمزگان
ویدیوی منتشر شده در منابع حکومتی از مکانی که مورد حمله هوایی آمریکا قرار گرفت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 427K · <a href="https://t.me/VahidOnline/78182" target="_blank">📅 09:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78181">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EAQEKIvPXQdjdU4coTOnImsTsfXIHzDH2Z0FYw9FHR8BBW4_Rqr0Y4YEh_pS0oT67PM4M-OggmXq1zXNywW0XDJhuxtgfCUfhjgTn5WjMsbxYcVSSHPusbHdCHwX4sxis_19UPf5kNtLSXIh7iBa_XX4UGUFukGUQphZRmI1nHGsYMoHsYbdimHDhYpw7j7KMqeOgg0fB6zjlYSZktG8XR-OTaLzUKaYmS99zsCEU3mghijYn2hnbuuEykadC9ZbLxQ_ikEfLknKI4TP975dj5l9AoAAXCUzicRA4q9PUS4Np8nR5FRRUVKV2-DOSRhBuZOpwZNtIrCpaiLkYyFd_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
من تلاش نمی‌کنم ایران را، آن‌طور که ABC Fake News گزارش داده، به پای میز مذاکره بکشانم.
اصلاً برایم مهم نیست که آن‌ها توافقی امضا کنند که برای خودشان هم ارزشی ندارد.
من موقعیت فعلی‌مان را خیلی بیشتر می‌پسندم؛ با کنترل تقریباً کامل بر تنگه هرمز و اقتصادی که در ایران کاملاً در حال فروپاشی است.
آن‌ها فقط دارند روند اجتناب‌ناپذیر را طی می‌کنند.
مردم ایران چه زمانی به پا خواهند خاست و خواهند جنگید؟
رئیس‌جمهور DJT
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 471K · <a href="https://t.me/VahidOnline/78181" target="_blank">📅 04:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78180">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ec60d5ccce.mp4?token=CT6exhHCHbB9XfnFIsftaqOXfhbjowaAKXGks3b7bfgaFayz9efkDvmWImr4Wdjlul32uwI_ooRi61IBqwYKwelkYaXBmqSnOPT-D7ecQt58fumLj2C7Y0otgAR7PMbyxGvYEacFMC8AMwpWbkq8XL5cdo9IFk1dL49Q_ZB8dgScns0y-IAeOJ8ShKGBnnCHashAGIFbTeaH2UV94HzK-ARM-B7lde9IPpZPCNmq4DMgcTZYMklSRnxSQ8BYsm0cPrMJb2irkCHKsl5-hztj98Q7toG3hsg_vLJGzkIzBkP9EJoHj-YkBa6smqdzs1aQzNNIPr667Pfj5i00F6HpUw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ec60d5ccce.mp4?token=CT6exhHCHbB9XfnFIsftaqOXfhbjowaAKXGks3b7bfgaFayz9efkDvmWImr4Wdjlul32uwI_ooRi61IBqwYKwelkYaXBmqSnOPT-D7ecQt58fumLj2C7Y0otgAR7PMbyxGvYEacFMC8AMwpWbkq8XL5cdo9IFk1dL49Q_ZB8dgScns0y-IAeOJ8ShKGBnnCHashAGIFbTeaH2UV94HzK-ARM-B7lde9IPpZPCNmq4DMgcTZYMklSRnxSQ8BYsm0cPrMJb2irkCHKsl5-hztj98Q7toG3hsg_vLJGzkIzBkP9EJoHj-YkBa6smqdzs1aQzNNIPr667Pfj5i00F6HpUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'شروط پکن برای سفر قالیباف به چین'
حسین مرعشی، دبیرکل "حزب کارگزاران سازندگی"، گفت: خیلی روشن به ما گفته‌اند که
۱- تنگه هرمز را باز می‌کنید
۲- عوارض نمی‌گیرید
۳- با عربستان سعودی مسئله‌تان را حل می‌کنید
۴-  با آمریکا مسئله‌تان را حل می‌کنید
بعد قالیباف به چین بیاید.
قالیباف در اردیبهشت سال جاری، با پیشنهاد مسعود پزشکیان و تایید رهبر جمهوری اسلامی به عنوان «نماینده ویژه ایران در امور چین» منصوب شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 457K · <a href="https://t.me/VahidOnline/78180" target="_blank">📅 04:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78179">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">منابع حکومتی:
روابط عمومی سپاه:
🔹
مردم شریف و انقلابی اردن؛ یکبار دیگر دست شیطان از آستین ارتش کودک‌کش آمریکا به درآمد و با بمباران وحشیانه به مراسم جشن عقد یک زوج جوان اهل تسنن در منطقه سیریک هرمزگان، عمق کینه خود را به امت اسلام به نمایش گذاشت.
🔹
ارتش تروریستی شکست خورده آمریکا که از رویارویی مستقیم با رزمندگان اسلام عاجز است، با استیصال مردم مظلوم را به خاک و خون کشید و مراسم جشن عقد پاک مردم را به عزا تبدیل کرد.
🔹
ارتش جنایتکار آمریکا که در آغاز تجاوز خود به ایران اسلامی ۱۶۸ کودک دانش آموز را در مدرسه میناب و ۲۱ کودک ورزشکار را در ورزشگاه لامرد به شهادت رسانده بود، شب گذشته در این حمله ناجوانمردانه حدود ۷۰ نفر از مهمانان این مراسم را مورد اصابت قرار داد که ۴ نفر از آنان از جمله یک کودک خردسال به شهادت رسیده و حال تعدادی از مجروحان وخیم هست.
🔹
در قصاص این جنایت، رزمندگان نیروی هوافضای سپاه پاسداران انقلاب اسلامی در یک حمله سنگین با موشک‌های بالستیک، آشیانه‌های هواپیماهای بدون سرنشین دور پرواز آر کیو ۴ و ام کیو ۹ را در پایگاه هوایی آمریکا در اردن موسوم به پرنس حسن مورد حمله قراردادند که تعدادی از پهپادها منهدم و تعدادی از خلبانان و خدمه فنی پروازی به هلاکت رسیدند.
🔹
همچنین چندین زیر ساخت فنی آنها به آتش کشیده شد.
🔹
مردم شریف و پاکدل اردن، اردن قدمگاه مقدس انبیاء الهی است، نباید جایگاه ولیدهای شیطان بماند. امروز با این جنایت های سبعانه، حجت بر همگان تمام است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 432K · <a href="https://t.me/VahidOnline/78179" target="_blank">📅 02:31 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

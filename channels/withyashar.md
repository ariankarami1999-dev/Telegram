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
<img src="https://cdn4.telesco.pe/file/qegKs_oH9UrZBAiWNu7PKcQtxTfNNHILGM3gdaCLan3ZppQO-vG4P2GLsejpQPZUaJcF4kkq7WTfZq5xTEARqmqpkq-5tU0KJ3waPitG75qyz4gzipOxlzWgGXK7pmXaMGW_HVzPOWIxLxW2-GJEtiFLnuerOiqC_13OcVnZhY6u5YGybXQlPLGpBSLFqa7NF8GrOGx1tPvCB2LiTtd4TjUzqMOeLxL9oBAUs0o15p3pby2thxDoz3ykATkrNBi1YiTdcr8cYtwOQswxIyzGtzQJbn3Ppa3ErV6o9k6cwzuZ926j6szXsuWudU2Smnfsq6dz3Om0IcCP68Kh7TUbJw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 288K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 20:54:24</div>
<hr>

<div class="tg-post" id="msg-13415">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">نتانیاهو:
اسرائیل آماده است. نیروهای آمریکا آماده‌اند.
ایران با آتش بازی می‌کند.
@withyashar
شمام آماده اید ؟
😁</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/withyashar/13415" target="_blank">📅 20:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13414">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/withyashar/13414" target="_blank">📅 20:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13413">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یعنی چی ؟  منظورش اینه جنگ تموم شد ؟</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/withyashar/13413" target="_blank">📅 20:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13412">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromR</strong></div>
<div class="tg-text">یعنی چی ؟
منظورش اینه جنگ تموم شد ؟</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/withyashar/13412" target="_blank">📅 20:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13411">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">مقامات اسرائیلی: تخمین زده می‌شود که اسرائیل در روزهای آینده به بیروت حمله کند
@withyashar</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/withyashar/13411" target="_blank">📅 20:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13410">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ادعای روبیو، وزیر خارجه آمریکا:
ما دیگر حملات مداومی در داخل ایران برای تضعیف ارتش آنها انجام نمی‌دهیم، زیرا جنگ «خشم حماسی» تمام شده است.
@withyashar</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/withyashar/13410" target="_blank">📅 20:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13409">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تکذیب شد
😃
🤣
خاک دوباره پس زد</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/withyashar/13409" target="_blank">📅 20:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13408">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">غرب‌ دوباره صدا اومد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/withyashar/13408" target="_blank">📅 20:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13407">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">غرب‌ دوباره صدا اومد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/withyashar/13407" target="_blank">📅 20:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13406">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">sample : yourname.warroom</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/withyashar/13406" target="_blank">📅 20:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13405">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">یه ایده جالب دارم ویس میدم …</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/withyashar/13405" target="_blank">📅 20:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13404">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">https://www.instagram.com/reel/DZIVRzvuaUf/?comment_id=17892109731481781
به درخواست شما متن برای بانو نور هم کامنت شد</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/withyashar/13404" target="_blank">📅 20:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13403">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">صدای مشکوک به انفجار از غرب‌ تهران
🚨
@withyashar</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/withyashar/13403" target="_blank">📅 20:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13402">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اتاق جنگ با یاشار : ما الان با دو بخار مواجه هستیم، بخار هسته ای و بخار خامنه ای
@withyashar
پایان چالش رو اعلام میکنم
🙌🏾
🤣</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/withyashar/13402" target="_blank">📅 20:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13401">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">رافائل گروسی مدیرکل آژانس بین‌المللی انرژی اتمی در گفت‌وگو با شبکه اسکای‌نیوز با بیان اینکه از موقعیت مکانی ذخایر اورانیوم غنی‌شده ایران که در جنگ  سال گذشته هدف حمله قرار گرفت، مطلع است.
او ادعا کرد که این مواد همچنان در همان محل پیشین قرار دارد اما دسترسی به آن به‌دلیل خسارت‌های فیزیکی دشوار شده است.
@withyashar</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/withyashar/13401" target="_blank">📅 20:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13400">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">💩
تاریخ برگزاری آئین وداع، تشییع و خاکسپاری علی خامنه‌ای اعلام شد   ۲۰، ۲۱، ۲۲ خرداد؛ وداع در حرم امام‌ خمینی  ۲۳ خرداد؛ تشییع در تهران  ۲۴ خرداد؛ تشییع در قم  ۲۵ خرداد؛ تشییع در عراق  ۲۶ خرداد؛ تشییع و خاکسپاری در مشهد @withyashar</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/withyashar/13400" target="_blank">📅 19:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13399">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">💩
تاریخ برگزاری آئین وداع، تشییع و خاکسپاری علی خامنه‌ای اعلام شد
۲۰، ۲۱، ۲۲ خرداد؛ وداع در حرم امام‌ خمینی
۲۳ خرداد؛ تشییع در تهران
۲۴ خرداد؛ تشییع در قم
۲۵ خرداد؛ تشییع در عراق
۲۶ خرداد؛ تشییع و خاکسپاری در مشهد
@withyashar</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/withyashar/13399" target="_blank">📅 19:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13398">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e72ba1695.mp4?token=JoeiKNnpHVN1vQav2ESycveRUVtUZVWyowG9OBtBIlbH65bTBdzk9XYYDW4DUQ3ms0LJs3YvAnvjXEqAiCo4XTmKZfnp4zFsrHJ9n1G26K4PEJFL3PN0thgZURxOyjaDhJIYBV82lEhXOhsbxA3qzKO0WYlqIRnB4_fzFhtnlaYNcAOo8SS0mqn0gDhZSc8i7u_cLx6pmls6tb3yukZFf_G7MlGHhU2LvjAkKY7kwzIrT1gDBnccN40ZC4uDwdXYdAEXeSIkOTi9CaAtAMeeb0GfrxYr6Htl7oKsaJHMkQnvX87KAMvMK_E5FdEi0a37FI7tlTJXrdsORdF_y4yOOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e72ba1695.mp4?token=JoeiKNnpHVN1vQav2ESycveRUVtUZVWyowG9OBtBIlbH65bTBdzk9XYYDW4DUQ3ms0LJs3YvAnvjXEqAiCo4XTmKZfnp4zFsrHJ9n1G26K4PEJFL3PN0thgZURxOyjaDhJIYBV82lEhXOhsbxA3qzKO0WYlqIRnB4_fzFhtnlaYNcAOo8SS0mqn0gDhZSc8i7u_cLx6pmls6tb3yukZFf_G7MlGHhU2LvjAkKY7kwzIrT1gDBnccN40ZC4uDwdXYdAEXeSIkOTi9CaAtAMeeb0GfrxYr6Htl7oKsaJHMkQnvX87KAMvMK_E5FdEi0a37FI7tlTJXrdsORdF_y4yOOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر امور خارجه عباس چپقچی:
نیروهای مسلح ما در حال انجام حملات دفاعی به سایت‌هایی هستند که آمریکا اجازه استفاده از آن‌ها را برای حمله به کشتی‌رانی غیرنظامی و نقض آتش‌بس دارد.
هر عمل خصمانه‌ای با پاسخی فوری و قاطع مواجه خواهد شد. تحریم‌ها و جنگی که نتوانستند به هدف برسند، با جنگ بیشتر به دست نخواهند آمد.
@withyashar</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/withyashar/13398" target="_blank">📅 19:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13397">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">پست جدید پیج دوم شاهزاده کامنت رو گزاشتم
🙌🏾
ادامه میدیم تا جوابی بگیریم
https://www.instagram.com/p/DZILMCsFoyR/?img_index=1&igsh=ZmZzNTQ2NHMwN2x2
و این پست
https://www.instagram.com/reel/DZIOnXHRKuy/?igsh=MWkzYmpzN2pjMmgyYQ==</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/withyashar/13397" target="_blank">📅 19:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13395">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/withyashar/13395" target="_blank">📅 18:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13394">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">مجری: چرا نمی‌تواند آمریکا فقط تنگه هرمز را باز کند؟
نتانیاهو: خب، می‌توانید، اما به مالکان کشتی‌هایی نیاز دارید که ریسک مالی برخورد را بپذیرند. از نظر نظامی ممکن است، اما ساده نیست
@withyashar</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/withyashar/13394" target="_blank">📅 18:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13393">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d25386882.mp4?token=NwvzwVYa5ZGFhw-9D5VA2t3X-heY-SNmK5lACQc1Xmg3qG4SJfUDJSsh70Eom0MoufQOmpvC2qfnzn8GvAB2t57eUyeINKBDNhjHpztYR8BkA6p6lDttW24dU7WlQDj7wpO0HnJfJsJVLHfcPnZFybSJS_P2J-adohhjxj4cMuCnHwngsZU-PQtxqeYzkydP3M05Yme61oBgOBN3saKMxHGSa8Pm10EXj5LZTEj6mWNmUS746trcJB_E6LlfnP2zY5cZ1Q37_M7p4-f4dbWPfh16FsLF8XgchH5tOvQ-FD3VoYDAGeRqazxrdHJbBZTbLlHctYOmaEki5COM_1H6gldqYN7DgZdeoDfCI3XOVT82SJw8YUb0t-4jHONeZ3Xo-G3zKRBkUAkbYGX-EBazdw0DwlM-LhqIP_SXSLqeKLQAr0SxsIt_S7wd2-cnxzcT5oQY6JO5WQsYWf2Va4RqqyvkZL6N-ZW08QnbZ6OyYLeRtQkfduMeYeG3yLzYrVBCIskI0DMX1s1K-sIhc-Pb2lRDdxuVPzE4JjThtvYjJjZHWbeLcxREKnIm9619-xpX561X277KOIr53yLxVSW_g1o2b4pn6_SHOSz4NzYMymSIZO_l9TpEz2J9x1uMeJp2pUIDwSRzLC3xhsk1ZmHoHSDA9Zh-8DXnHLCJhT81Loo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d25386882.mp4?token=NwvzwVYa5ZGFhw-9D5VA2t3X-heY-SNmK5lACQc1Xmg3qG4SJfUDJSsh70Eom0MoufQOmpvC2qfnzn8GvAB2t57eUyeINKBDNhjHpztYR8BkA6p6lDttW24dU7WlQDj7wpO0HnJfJsJVLHfcPnZFybSJS_P2J-adohhjxj4cMuCnHwngsZU-PQtxqeYzkydP3M05Yme61oBgOBN3saKMxHGSa8Pm10EXj5LZTEj6mWNmUS746trcJB_E6LlfnP2zY5cZ1Q37_M7p4-f4dbWPfh16FsLF8XgchH5tOvQ-FD3VoYDAGeRqazxrdHJbBZTbLlHctYOmaEki5COM_1H6gldqYN7DgZdeoDfCI3XOVT82SJw8YUb0t-4jHONeZ3Xo-G3zKRBkUAkbYGX-EBazdw0DwlM-LhqIP_SXSLqeKLQAr0SxsIt_S7wd2-cnxzcT5oQY6JO5WQsYWf2Va4RqqyvkZL6N-ZW08QnbZ6OyYLeRtQkfduMeYeG3yLzYrVBCIskI0DMX1s1K-sIhc-Pb2lRDdxuVPzE4JjThtvYjJjZHWbeLcxREKnIm9619-xpX561X277KOIr53yLxVSW_g1o2b4pn6_SHOSz4NzYMymSIZO_l9TpEz2J9x1uMeJp2pUIDwSRzLC3xhsk1ZmHoHSDA9Zh-8DXnHLCJhT81Loo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری
: ترامپ شما را «دیوانه لعنتی» خطاب کرد.
نتانیاهو: گاهی اوقات، مانند بهترین خانواده‌ها، ما این اختلافات تاکتیکی را داریم. همیشه راهی برای حل آن‌ها پیدا می‌کنیم.
می‌توانیم صبح با هم اختلاف نظر داشته باشیم و تا بعدازظهر اقدام مشترکی انجام دهیم.
@withyashar</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/withyashar/13393" target="_blank">📅 18:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13392">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09d950e42b.mp4?token=DGjAtJ0TVGO_AoP09oGWO9nPYIBkBkgBUfCxW15wK4qW4rdLuYivrzA29sWFPgBmCL43ntR1-jeIZqnXL4gAOggpSYChIQ1P6gKEO53TkF5Du2sqoMh4mRIlX03SqWQ_kfT39_hMO2yigHbMjOtdQKRn0vZgB8-rCjwJZ4JdIEn9xZZasNLyt6j9wnHusvYJ9K4Z7uhZ38QhwhKX8fY7UDwYgodiD2JlwTvA4D81T6LnghzM2LU_bhPQAky6q7rfNk5RywDacWmDyhyYcP5XhjmG3G5SoR0xpeUfjrF0OPnpheaTso9uuax1GQjgs1HGt2Rq6uCWyCRoCL71z9tMmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09d950e42b.mp4?token=DGjAtJ0TVGO_AoP09oGWO9nPYIBkBkgBUfCxW15wK4qW4rdLuYivrzA29sWFPgBmCL43ntR1-jeIZqnXL4gAOggpSYChIQ1P6gKEO53TkF5Du2sqoMh4mRIlX03SqWQ_kfT39_hMO2yigHbMjOtdQKRn0vZgB8-rCjwJZ4JdIEn9xZZasNLyt6j9wnHusvYJ9K4Z7uhZ38QhwhKX8fY7UDwYgodiD2JlwTvA4D81T6LnghzM2LU_bhPQAky6q7rfNk5RywDacWmDyhyYcP5XhjmG3G5SoR0xpeUfjrF0OPnpheaTso9uuax1GQjgs1HGt2Rq6uCWyCRoCL71z9tMmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: مردم ایران خواهان روابط خوب با آمریکا هستند و خواهان روابط خوب با اسرائیل. این می‌تواند اتفاق بیفتد.
@withyashar</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/withyashar/13392" target="_blank">📅 18:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13391">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مجری : شما درباره تغییر رژیم صحبت می‌کردید. چرا الان هیچ‌کس درباره آن صحبت نمی‌کند؟
بی بی : چرا این را می‌گویید؟
مجری: به نظر می‌رسد ترامپ آماده است با این رژیم فعلی معامله کند.
بی بی : این به این معنا نیست که او می‌خواهد این رژیم فعلی باقی بماند.
ما باید به مردم ایران کمک کنیم تا این رژیم را سرنگون کنند و این تغییر نکرده است.
اما این اتفاق دقیقاً در لحظه‌ای که ما بخواهیم رخ نخواهد داد.
@withyashar</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/withyashar/13391" target="_blank">📅 18:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13390">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">نتانیاهو به ان‌بی‌سی: وضعیت در ایران تمام نشده، اما ضعیف شده است. ما و آمریکایی‌ها آماده‌ایم در صورت لزوم اقدام کنیم.
اگر تشدید تنش لازم باشد، آن را به ترامپ واگذار می‌کنیم و باز کردن تنگه هرمز از طریق نظامی امکان‌پذیر است.
ترامپ در حال بررسی چندین گزینه است و ما هر دو روز یکبار با هم صحبت می‌کنیم.
ایران هنوز با حذف مواد هسته‌ای موافقت نکرده است، اما فشار فزاینده‌ای وجود دارد.
@withyashar</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/withyashar/13390" target="_blank">📅 18:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13389">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">روبیو: سکوهای پرتاب موشک ایران آسیب شدیدی دیده‌اند که منجر به زوال قابل توجه قابلیت‌های آنها شده است.
ما می‌خواهیم شاهد تغییر در ایران و حکومت مردم بر آن باشیم و دیگر تهدیدی برای منطقه نباشد.
امیدواریم که ایران جاه‌طلبی‌های هسته‌ای خود را کنار بگذارد و حمایت از تروریسم در سراسر جهان را متوقف کند.
«عملیات خشم حماسی» به هدف خود یعنی شکستن سپر سنتی ایران و کشاندن آن به پای میز مذاکره دست یافته است.
@withyashar</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/withyashar/13389" target="_blank">📅 18:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13388">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">روبیو: امیدواریم امروز بین اسرائیل و لبنان توافق صورت گیرد
وزیر امور خارجه ایالات متحده:
رهبران دولت‌های لبنان و اسرائیل در حال حاضر در مقر وزارتخانه ما برای مذاکره دیدار می‌کنند.
ما امیدواریم که جلسه امروز بین لبنان و اسرائیل به بیانیه و برنامه عملی برای مسیر امنیتی لبنان مستقل از حزب‌الله منجر شود.
@withyashar</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/withyashar/13388" target="_blank">📅 17:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13387">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fx7zGWsN7Yzq5huTCjVKZm6Zm5N5UqWusi23GaBnL3Rlwbf0qpfCetiCAZ-v7AUnbnHxlYNyZmPPtqIiZDCEKuGslc4NNQMyD4UsCvMIt9m7I6cUQj9_jd6pGGVkr9BMDQQapngjEAzIWJvye-IQbKJBrB4E3CEhLY-FjKLuR2BX0TK-kqAPOHQaLDtzAQhIBznzmd7KZ1fYbqFVOMnphPvvrFeXmb-tx_xUUR_SGzwAXPqMjr7tfg3t2z397xCA_hczad6SpXiFA5uK6p72Q6MVd7LV9f34u3Zqkz0FKTI1W4wbCkY8FtjVNiXT4N1mFoQPHBmMnBZdjFri9p2S0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تانکر ترکرز: یک ابرتانکر VLCC برای اولین بار در چهار هفته اخیر، نفت خام را در جزیره خارک ایران بارگیری می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/withyashar/13387" target="_blank">📅 17:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13386">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">وکیل شخصی نتانیاهو، مایکل رابلو، به عنوان بازرس کل دولت اسرائیل انتخاب شد.
@withyashar</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/withyashar/13386" target="_blank">📅 17:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13385">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">کویت در پاسخ حمله جمهوری اسلامی ، دو دیپلمات را عنصر نامطلوب اعلام و اخراج کرد.
@withyashar</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/withyashar/13385" target="_blank">📅 17:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13384">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ارتش کویت: ما 13 موشک بالستیک و 17 پهپاد رو شناسایی کردیم.
یک فرد هندی جان باخت و شماری از افراد زخمی شدن، همچنین خسارات مادی سنگینی وارد شده.
به دلیل حملات، امروز 5 بار آژیرهای خطر به صدا در اومدن.
@withyashar</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/withyashar/13384" target="_blank">📅 16:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13383">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">️بیانیه نیروی دریایی ایران:
فقط مسیر تعیین‌شده ایران برای تردد امن در خلیج فارس است / شناورهای متخلف هدف قرار می‌گیرند
@withyashar</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/withyashar/13383" target="_blank">📅 15:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13382">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترامپ : ما خیلی خوب با هم کار کردیم. من «بی‌بی» رو خیلی دوست دارم و همکاری خیلی خوبی باهاش داشتم
می‌دونی، ما تو شرایطی بودیم که اون نخست‌وزیر زمان جنگه و من هم رئیس‌جمهور زمان جنگ هستم
ولی در کل رابطه خیلی خوبی دارم. با هم خوب کار کردیم، نتیجه هم گرفته شده
همیشه هم همین‌طوره. بدون آمریکا اصلاً نمی‌شد انجامش داد، همه اینو می‌دونن. ولی ما تونستیم
@withyashar</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/withyashar/13382" target="_blank">📅 15:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13381">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PebnkRN28McbYk0N8Dq0ng-AV4KIwH74eC1PKUHHAG-EUFTkvwBPlyuahKnRPKWJnKmb3wbgXb1SLvpmvBg44P-efgRe9rX3aoOZEvW9TPmTN3Z3-QJ1AEntiZ60A6qBqx5q_W-GFYZwHY0HJDNOyyQi3RangMQbcUwWv-tJXxUWDiQ5mAht5Qt3qOvW9qcfKTKVdiIGYr6Hclfcxraa8GOofsq2ehi6___S-N_DXtFcUnClEgWDGwiN5VizzBmM5haZUqGAlnz6W5JCyiDqmP96eXVUFNNmmHFE4JIW3zYamiQI1JyIuNG8KwIJcDvzoIc8pY3A_Z334unxzglKoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در پست جدیدی در تروث با تلقین حس مخفی‌کاری و چند چهره بودن در قالب جیمز باند مأمور مخفی شکست ناپزیر ظاهر شده
@withyashar</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/withyashar/13381" target="_blank">📅 14:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13380">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYVrutj9E36pMSSJUJPfJy4DqGbtG4-VYK1X_vkVL9XwcXDa5m23FU1VqXv81QiHCo-Sb3Jc4II_C8ffcF2lQ8NYJ0QOYAdqHT8nZr2LqeLWmSa3icsVgP3qTLW1RcX6qUl-TwIThVbF6wiM6M4YaopeItAPD0xyk34xML8y4duB5ZwXxo6B7inA3OzkxS7vFmzR5QzHLC-p6bH0xghn7wZ6uGL9-9W2iqvpQjpEJaj8g2iJ5YEpGZ_5SW69lPCXEcj6nMJ7pInbquG2pTRag-TfSYSLoYkLHYLaR0I27jY8vD2FQidvbLWmnT5Xb2jsJmIRlyi0k19q6IOCshRrzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین الان تحرکات سنگین دارن
جهیزیه را میارن
🎉
@withyashar</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/withyashar/13380" target="_blank">📅 14:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13379">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ دربارهٔ سال ۲۰۲۸:  من هر دو نفر، جی‌دی ونس و مارکو روبیو را دوست دارم. دوست دارم که با هم باشند. جی‌دی و مارکو تیم فوق‌العاده‌ای خواهند بود. هر دو بسیار با استعداد هستند. @withyashar</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/withyashar/13379" target="_blank">📅 14:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13378">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامپ دربارهٔ سال ۲۰۲۸:
من هر دو نفر، جی‌دی ونس و مارکو روبیو را دوست دارم.
دوست دارم که با هم باشند. جی‌دی و مارکو تیم فوق‌العاده‌ای خواهند بود.
هر دو بسیار با استعداد هستند.
@withyashar</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/withyashar/13378" target="_blank">📅 14:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13377">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ درباره ایران:
ما نیازی به حضور نیروهای زمینی نداریم. با بمباران، بخش زیادی از نیروی نظامی آن‌ها را نابود کردیم.
آنها نه نیرو دریایی دارند و نه نیروی هوایی همچنین سرباز‌ زیادی هم ندارند
@withyashar</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/withyashar/13377" target="_blank">📅 14:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13376">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ایالات متحده به تازگی یک جزیره کلیدی ایران را بمباران کرد.
این یک تشدید تنش بزرگ است.
کینگ ترامپ با ملاها بازی نمی‌کند و آنها دارند متوجه می‌شوند.
اوضاع به سرعت در حال وخیم شدن است.
@withyashar</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/withyashar/13376" target="_blank">📅 14:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13375">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ : گروه‌های مختلفی از آدم‌ها هستن؛ گروه اول دیگه نیست، گروه دوم هم نیست، بخشی از گروه سوم هم حذف شده
و اون آدم‌هایی که الان باهاشون طرف هستیم، همونایی هستن که الان کشور رو هدایت می‌کنن
@withyashar</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/withyashar/13375" target="_blank">📅 14:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13374">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترامپ: اگر من نبودم، الان اسرائیلی هم وجود نداشت.
@withyashar</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/withyashar/13374" target="_blank">📅 14:06 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13373">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ:
هر کسی که من حمایت می‌کنم برنده می‌شود. منظورم این است، همه. هفته گذشته دیدی، درست است؟
هر فردی که من حمایت می‌کنم برنده می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/withyashar/13373" target="_blank">📅 14:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13372">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ:
می‌توانم پاسخی بدهم و سپس، ۲۰ دقیقه بعد، وارد دفتر بیضی‌شکل شوم و متوجه شوم پاسخم اکنون نادرست است.
می‌دانی، تغییر می‌کند. حقایق تغییر می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/withyashar/13372" target="_blank">📅 14:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13371">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامپ درباره اینکه آیا نتانیاهو او را برای جنگ با ایران فریب داده است:
یعنی من کسی هستم که این را شروع کردم.
نمی‌خواهم کسی را خسته کنم، اما من شروع‌کننده بودم چون نمی‌توانیم اجازه دهیم آنها سلاح هسته‌ای داشته باشند.
اگر من نبودم، اسرائیل هم وجود نداشت.
@withyashar</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/withyashar/13371" target="_blank">📅 14:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13370">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ: به نتانیاهو گفتم او کاملاً دیوانه است، چون از درگیری او با لبنان نگران بودم.
من رابطه خوبی با نتانیاهو دارم
@withyashar</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/withyashar/13370" target="_blank">📅 13:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13369">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">وزارت امور خارجه کویت : حمله ایران به فرودگاه کویت یک کشته و چند زخمی در بر داشته !
@withyashar</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/withyashar/13369" target="_blank">📅 13:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13368">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">صدای انفجار در‌ قشم
🚨
@withyashar</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/withyashar/13368" target="_blank">📅 13:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13367">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ تعریف میکنه نشونه زدنه
😁
🚨
@withyashar</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/withyashar/13367" target="_blank">📅 13:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13366">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ در پادکست :
: احتمالاً تا روز کارگر (Labor Day) بتونیم محاصره ایران رو برداریم
هیچ‌وقت به دیدار با هیچ‌یک از مقام‌های ایرانی فکر نکرده‌ام
آیت‌الله ایران تو مذاکرات با آمریکا نقش داره و تو جریان گفت‌وگوهاست.
احتمالاً یه زمانی با آیت‌الله ایران دیدار خواهم کرد
قیمت بنزین به زودی کاهش می‌یابد
وضعیت ایران خیلی سریع داره تغییر می‌کنه، و در نهایت اوضاع خیلی خوب پیش می‌ره
@withyashar</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/withyashar/13366" target="_blank">📅 13:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13365">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ: ایران موافقت کرده است که سلاح هسته‌ای نداشته باشد.
@withyashar</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/withyashar/13365" target="_blank">📅 13:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13364">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">صدای انفجار بندر عباس (گفته بودن ۳ روز مهمات عمل نکرده است که دیروز روز سوم بود )
@withyashar</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/withyashar/13364" target="_blank">📅 13:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13363">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QcSqayzfk7ulgobQiIt__TAZF8aj0MaUZP8w_t0soe-r6WSlgnXH3kxxjqoO1OpScvuUAi7R7fp_BeHDJpVv0I17OeqdCeOBQiFVTV98OvT1cVlb6cnNOuCE3gMElWDA1T2tOkfw5SIKFaTWOI7TJGNFnVOporUA6OBpnvFeLJODT6N4Vlzr_KQ9WWpz9cPHCa0Mh_JIbqUBd5ajtUrgSpIB3J4EFWt91FMiykhFmbwVg1V9Dkk33wwFP34LyX86jkmF0w135I_G6ERKQExQOL9WzQuALQXum5Qj3RvmGE7XzvnbhS_ihI33cSb1w3WaeSF2bRhcj2isdcgZ2z8AIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر ماهواره‌ای مربوط به دیروز ، آخرین موقعیت ناو هواپیمابر آبی خاکی یو‌اس‌اس تریپولی (LHA 7) را نشان می‌دهد که بسیار جلو و در نزدیکی رأس الحد عمان آمده!!!
🚨
@withyashar</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/withyashar/13363" target="_blank">📅 13:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13362">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b108e3f2b1.mp4?token=H1eAYLPs9_W7_tBziPZseMZllKioOR2li9u3ORdkH8BJ28LESVdmq-JDO_Hw_RlApTTwyFjVkY-6kV1-7crcDtLTeA4PVIBrTXlXpme1tntPPWldwt0p67B-Xy_e5VFeC_aomqnnunVD28K-cfL8z6e0V7NIn65nMdhplHMKKc6j5zW8RRFQdWan1UmP7vqZlhnXue3mrlu03qrvXS1l0mdBfxn6qYizmr-xfQxoSdOhz2yjzXQnr9jy_NQPvs9liExIXkWJO0UnPwyuiPmPJRz2D7IZVRiQkmj3sC_Zr0yBysM4FmxmU7CPDRRNhGeQU1rKQG_Mn252wHkKXnwmmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b108e3f2b1.mp4?token=H1eAYLPs9_W7_tBziPZseMZllKioOR2li9u3ORdkH8BJ28LESVdmq-JDO_Hw_RlApTTwyFjVkY-6kV1-7crcDtLTeA4PVIBrTXlXpme1tntPPWldwt0p67B-Xy_e5VFeC_aomqnnunVD28K-cfL8z6e0V7NIn65nMdhplHMKKc6j5zW8RRFQdWan1UmP7vqZlhnXue3mrlu03qrvXS1l0mdBfxn6qYizmr-xfQxoSdOhz2yjzXQnr9jy_NQPvs9liExIXkWJO0UnPwyuiPmPJRz2D7IZVRiQkmj3sC_Zr0yBysM4FmxmU7CPDRRNhGeQU1rKQG_Mn252wHkKXnwmmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همکنون فرودگاه بین المللی کویت
@withyashar</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/withyashar/13362" target="_blank">📅 13:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13361">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دیروز، مدیرعامل شرکت هواپیمایی کویت ایرویز از سرگیری فعالیت فرودگاه بین‌المللی کویت خبر داد و تصاویری از کارمندان فرودگاه در حال انجام آخرین مراحل بازگشت به ظرفیت کامل آن منتشر کرد ولی
لحظاتی پیش، شرکت هواپیمایی کویت ایرویز از به تعویق افتادن فعالیت‌های عملیاتی خود تا اطلاع ثانوی خبر داد.
@withyashar</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/withyashar/13361" target="_blank">📅 13:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13360">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16168fdf19.mp4?token=k4K1qMaSOrBIUnw8nGIHTgcHPfUPnDCDNMAj7IAeXi8bXOGD7ZBC_INR8RaSnzWni_4rZyEINac-2sV9exXftdxsMXeXMSwMvsTIQmsKNb_LgPa8_-PAEEplkhFIBn3U0qXf15TkBjKH3_RxeSsySsqzuyYKqRxrjSO7i1PxZo2WFNC0pKgELF7b14F1u9lKPXQorrk_o1XbYfSMukIwJc3-kus4Q6hkaCEe1gwz2fUIu45miHEXMv6r6_SNUKJ2M4chLbXz-VbO3eMSnuxSOtXedKVn1XpHkvod_0aQJVG9JMk8fglpYGgZ5JRqjtrGFknUt3RNRMysZtF42coZbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16168fdf19.mp4?token=k4K1qMaSOrBIUnw8nGIHTgcHPfUPnDCDNMAj7IAeXi8bXOGD7ZBC_INR8RaSnzWni_4rZyEINac-2sV9exXftdxsMXeXMSwMvsTIQmsKNb_LgPa8_-PAEEplkhFIBn3U0qXf15TkBjKH3_RxeSsySsqzuyYKqRxrjSO7i1PxZo2WFNC0pKgELF7b14F1u9lKPXQorrk_o1XbYfSMukIwJc3-kus4Q6hkaCEe1gwz2fUIu45miHEXMv6r6_SNUKJ2M4chLbXz-VbO3eMSnuxSOtXedKVn1XpHkvod_0aQJVG9JMk8fglpYGgZ5JRqjtrGFknUt3RNRMysZtF42coZbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت پس از حمله رژیم جمهوری اسلامی
@withyashar</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/withyashar/13360" target="_blank">📅 12:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13359">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ادعای ای‌بی‌سی به نقل از مقامات آمریکایی: ترامپ، از تهران می‌خواهد که امتیازات مشخص هسته‌ای را به صورت مکتوب به عنوان بخشی از یک توافق مقدماتی ارائه دهد
تا بتوان بر بن‌بست طولانی میان آمریکا و ایران غلبه کرد.
ایران در حال بررسی شرایط به‌روز شده است و مذاکره‌کنندگانش نشان نداده‌اند که آیا تهران این شرایط را می‌پذیرد یا خیر
@withyashar</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/withyashar/13359" target="_blank">📅 12:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13356">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from₃₆₄</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDytAYTfEncnryhQ85JB9eZq5zJ044v3-oMK24PKfF7jCBNMbzZWEfuqETRRX6ODpj1YVCE44MBai1FUDCji5fG4_V_4N-J8FrFX4TFqY6ddOEv8XJN58FTeA8LEhPOroD34oluvq2plGxwl3ng6aR5CzC1g2NXCq9WRK9iOHdJFjRHhw5GXnLY8rhZFM5VY_pmA5CEYEPYJtLhhnAzXgs-DmPnlj-xCjXZ9_tIWq2zAzrJd_yEOJ3uLLUzyjTEuz1pvrT07CVHX8oy6XkhQk19lcgi6Z7ZSr5wGvq2V60zxbxusGsauaeWo7AOAC_2z2Q1Hhs890C4HuRBTVOO0yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا یاشار مهربان</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/withyashar/13356" target="_blank">📅 12:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13355">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/withyashar/13355" target="_blank">📅 12:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13354">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🍁┅┅✿❀𝒩𝒾𝓃𝒶❀✿┅┅🍁</strong></div>
<div class="tg-text">درود آقا یاشار مهربان
تحلیل هاتون خیلی جالبه
جوری توضیح میدید که درکش برای همه راحت باشه
سپاس از شما
🙏
🌹
😊</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/withyashar/13354" target="_blank">📅 12:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13353">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خبرهای تایید نشده از اینکه که سه نفر از وطن پرست ها مجری محمدرضا شهبازی رو گیر میارن و بهش تجاوز میکنن  به همین دلیل هم برنامه پاورقی فعلا متوقف شده @withyashar</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/withyashar/13353" target="_blank">📅 12:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13352">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/withyashar/13352" target="_blank">📅 11:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13351">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03f509353.mp4?token=T31QcSjm6MS8bpXnCQzDa6r6A_rym0RqhYnCMs8HLbilMLD3nKyhKEDqOe2_AzWXoUSVemBGaRYXlRj2S8owM-wpUY4TsVpGetgGDQAMyLru1qCDt4xA7nfpceX1VUs0KR45kC1ZglxWO79Jxjx4byNk_sUwk5pGFpqLK3ejdrfBk3Pa4Z2-fvySz6G3SV99gY9jv7Oc49xet00SwtyWGRgIsW0sfO1PifZEJdxLYq9b3WJccnbfamSfgbZdwqgo-UFqJEg2OEBK8RiJq-DQVr2EJFpozQYZvnHwN0g_2NAyhHpd2i-2CyYXBNHY38rNw_HeNJhwsYgDnU_XPAJaWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03f509353.mp4?token=T31QcSjm6MS8bpXnCQzDa6r6A_rym0RqhYnCMs8HLbilMLD3nKyhKEDqOe2_AzWXoUSVemBGaRYXlRj2S8owM-wpUY4TsVpGetgGDQAMyLru1qCDt4xA7nfpceX1VUs0KR45kC1ZglxWO79Jxjx4byNk_sUwk5pGFpqLK3ejdrfBk3Pa4Z2-fvySz6G3SV99gY9jv7Oc49xet00SwtyWGRgIsW0sfO1PifZEJdxLYq9b3WJccnbfamSfgbZdwqgo-UFqJEg2OEBK8RiJq-DQVr2EJFpozQYZvnHwN0g_2NAyhHpd2i-2CyYXBNHY38rNw_HeNJhwsYgDnU_XPAJaWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/13351" target="_blank">📅 11:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13350">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromToranj</strong></div>
<div class="tg-text">درود یاشار عزیز ، چرا حملات اخیر جمهوری اسلامی به کشور های منطقه نقض آتش بس نیست ؟ و واکنشی خاصی از امریکا و اسرائیل دیده نمیشه ؟</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/withyashar/13350" target="_blank">📅 11:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13347">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/orAjsAxFxEk_HEBT-DzP3K0io7Vt_NsoBKsm52OaVif4wm5iXtvgmFAa_jFDpUvklAczeniKpvqVV3ouvJT37pwUSkBy64lxB2Ot16K3x5MokUKtXtJbdJwQJV9XjYaZdlnXjat3JrkiKxGH1rvhHYdQWJMwNFVr4PNr59IYVHPtpjuQWPNCkoj636gD1WWWMqYNDAuRGasqG13rU80Wd1_GYyMVAVN_egfw8uzhA8nIUNRJ3RCOXAJ2RzVWCiHdkpWq6uJ2t-rP_ybv9KNb-4kDmz385_H5tVxxB-nT40VOsZGQag7l7lLpkkpjGQLDbr5a_ZMwTqOt1WF54I5Wjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E-_TwhCS5oBP5JGCYqngsUuvlW8rSzjA3EqHtLuMejS2BHZhKPsO6WN1W8kWOWbSDQq20qNS1Nqe6aEd29easChkctNqPZv0Pbs8iG4XdNx_4kmtZEOwSAbRzHbYoKsBncr9l2MhAVHEY0ECe41amrvp6KxkVyzy-ll4pbo-IXYDzgh19TrMLe93XhUOrjELX1Ei-ITU2wfx_hWeiBaiALrQ2kPtta6OzWtV-M6DWHXRJ6MptrXUpo5cjNxqdLx20r6BNUXMFccBkfr0RzXCkpfI7UZZrh2S6HcZWVERGqvQRsMrJ-n0RntJGBSfMJ9qOmfx_WlW6clEnSdKXAOSOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cAydhtGlupD4wf_FmlHPpMNYST-xjWw2xnM62Qs1rQgVR74yhH7WP3JS4iQnVtVqV654L83aIIslnVz8pKopliXHV6AaM7JdA1D1NKqP7Wgy3XliS_iliVYAwOuxer_GS-lxWQxtjzRSYxxXhZ_g_Y7IGEHa2fJNkBRdoqE-kBDvEMdKhL1VitkyMNhR7EmRquGS5-L0uBvjqC1PwjiBmpMv4y6KYwSsgKalpaLXwyLqDsyBzyvInUZJf3pdY2DEkCFsptds_yozkCfEiakks7G5TkS39N06e5L38ZyR8a7BPiK9yWJUzVWC4F5YRRKH3sWOaas0zcLiIONZ0oK8Vw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همکنون وضعیت فرودگاه کویت
@withyashar</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/withyashar/13347" target="_blank">📅 11:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13346">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwfyk93nR10_H9QMv63t2ycBLP5KcqgXCVbrherX325eJgAOvJytimbidimQgRhqL8fVVEelQAQeVmRT2MNWLCpPZwhcjS5b_wT1Dh3mEOsnIZzoQ4JN4rH0WQlvZkQIydOQxmTa4t-1FWCZpsAMkV7V_u23hUrFWO-AYD0WBorM1WXaYH7KtCk3EiM1JgGhItD1InIXAGUqK8vidYOm2xdrXdldPeHx-QcQZdXSgpD2uSsH8QwB58JQuY1D1evu32dsgs98epMIAe_VhIhodnc22iXE8_wysrAMk2k7MtVli47WmsQ08jFyxmldAeDjivnIS6UTUj6nGvN-ou2Djg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با شما : مشاهده شدن سه ستون دود غیر معمول سمت آزادراه تهران پردیس
@withyashar</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/withyashar/13346" target="_blank">📅 10:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13345">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خبرهای تایید نشده از اینکه که سه نفر از وطن پرست ها مجری محمدرضا شهبازی رو گیر میارن و بهش تجاوز میکنن
به همین دلیل هم برنامه پاورقی فعلا متوقف شده
@withyashar</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/withyashar/13345" target="_blank">📅 10:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13344">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نایب رئیس مجلس: موشک‌هایی که به بیت اصابت کرد تنها چند کروز بود نه سنگرشکن
@withyashar</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/withyashar/13344" target="_blank">📅 10:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13343">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سی‌ان ان : شدیدترین تبادل آتش از زمان آتش‌بس!
هم‌زمان با دور تازه حملات آمریکا، ایران کویت و بحرین را هدف قرار داد.
یکی از شدیدترین تبادل‌های آتش از زمان آغاز آتش‌بس در شرایطی رخ داده که مذاکرات همچنان شکننده و ناپایدار توصیف می‌شود.
۹۴ روز بن‌بست؛ تنگه هرمز همچنان در وضعیت انسداد باقی مانده است.
@withyashar</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/withyashar/13343" target="_blank">📅 10:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13342">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ce930b592.mp4?token=bu4wudyTjiS8e0kadLMalQ_aaDq5wqA4kzIYf_siUTwczAmLKpU6ITpO67wQRQ3VnNMPtWvLr5NgTugaWvv9kB0edmu0NbPfUBDsEZmTz8O3z-FSL9qSp3v3OEGx5YZjwl8Ia_HMKhHCQPKI9AZ6jfLLqT8ivn-GDMX77nbAqOAoZlWQDN7ZgAcGfIqlc5IjnwBW55hXuY-V4_yiHUm65H0V7bIH-oU_3DfF4v54khPdh75qBhkuhwMqHXWVsstTzC0ewBecaRGRuqu4A6xRoM09UFZgIDCkgarzCrMbiqCEqYp9CFLNoSUUPoUx442__FEr5ctisRWko6WV0hvAQAiHMGsg_FGl5TfYX_qO6JdWqEdANJlM3ZrJR4PkYBqR-YGnLZTIrRsLGS0wBVGPsz7HAkNZZiXjAFMntlPunYgJ3dx3xHU9eCt8wS8_0-6MsEXfbDlBvvzCgMrFpZwQPxJWQaBZdHS3J4zaEVLObV3FeZwZQcpDebC9ZzEgCoh7k36MOjptX67zTRsIO7CEzRHbK0_Gjj2cHAYdSUEi5HINJv0dqOy1yyXLxFpVn21ohunjuj4_EVJOV8CvwjrZ6dg8zTQChGdr99F3MbZmh7p42OXhK_tJIe1YJxN_5G1jgVdbodxbDFZmBPfZy6bM_baj_OMNxjrpFoklMMa9e0E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ce930b592.mp4?token=bu4wudyTjiS8e0kadLMalQ_aaDq5wqA4kzIYf_siUTwczAmLKpU6ITpO67wQRQ3VnNMPtWvLr5NgTugaWvv9kB0edmu0NbPfUBDsEZmTz8O3z-FSL9qSp3v3OEGx5YZjwl8Ia_HMKhHCQPKI9AZ6jfLLqT8ivn-GDMX77nbAqOAoZlWQDN7ZgAcGfIqlc5IjnwBW55hXuY-V4_yiHUm65H0V7bIH-oU_3DfF4v54khPdh75qBhkuhwMqHXWVsstTzC0ewBecaRGRuqu4A6xRoM09UFZgIDCkgarzCrMbiqCEqYp9CFLNoSUUPoUx442__FEr5ctisRWko6WV0hvAQAiHMGsg_FGl5TfYX_qO6JdWqEdANJlM3ZrJR4PkYBqR-YGnLZTIrRsLGS0wBVGPsz7HAkNZZiXjAFMntlPunYgJ3dx3xHU9eCt8wS8_0-6MsEXfbDlBvvzCgMrFpZwQPxJWQaBZdHS3J4zaEVLObV3FeZwZQcpDebC9ZzEgCoh7k36MOjptX67zTRsIO7CEzRHbK0_Gjj2cHAYdSUEi5HINJv0dqOy1yyXLxFpVn21ohunjuj4_EVJOV8CvwjrZ6dg8zTQChGdr99F3MbZmh7p42OXhK_tJIe1YJxN_5G1jgVdbodxbDFZmBPfZy6bM_baj_OMNxjrpFoklMMa9e0E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاباری استیون براون که در مسابقه معروف «۱۰۰ خلبان برای یک جت خصوصی» متعلق به مستر ‌بیست برنده یک جت شده بود ، توسط مقامات پاراگوئه در جت خصوصی که از میامی و از طریق پاناما وارد شده بود و حدود ۲۶۱٫۶ کیلوگرم ماری‌جوانا با THC بالا به ارزش ۳.۶ میلیون دلار حمل و نقل میکرد دستگیرشد !
@withyashar</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/withyashar/13342" target="_blank">📅 10:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13341">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">حرکت پهپاد شاهد۱۳۶ ، فعالیت پدافند و در پایان برخورد و انفجار در فرودگاه کویت !
@withyashar</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/13341" target="_blank">📅 09:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13340">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سازمان هواپیمایی کشوری کویت: یک ساختمان مسافربری در فرودگاه
کویت هدف پهپادها و موشک‌های ایرانی قرار گرفت و حالت اضطراری فعال شده.
@withyashar</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/withyashar/13340" target="_blank">📅 09:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13339">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">وال‌استریت ژورنال: حمله سنتکام به جزیره قشم، قیمت نفت را صعودی کرد و چشم‌انداز بازگشایی تنگه هرمز را کمرنگ ساخت.
@withyashar</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/withyashar/13339" target="_blank">📅 09:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13338">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">منبع آمریکایی: اگر پاسخ ندهیم، باید به رهبری کاخ سفید شک کرد
@withyashar</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/13338" target="_blank">📅 03:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13337">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ الان میاد میگه چون موشک ها از رو آب رد شده مسافر حساب‌ میشن و رعب و وحشتشون شکسته حساب میشه پس این جنگ نیست !!! هرچی شده رفع بلا بوده فکر کنین دادین خمس و زکات ، حالا هم آشتی و من به  یک جنگ دیگه پایان دادم و رژیم هم تغییر کرد ولی سلاح هسته ای نباید…</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/13337" target="_blank">📅 03:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13336">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گروه کومله کردستان در بیانیه‌ای اعلام کرد که ساعت ۲۳:۰۰ به وقت محلی دیشب ، دو موشک ایرانی به مقر حزب کومله در دره آلانه، واقع در شمال شرقی اربیل، اصابت کرده است
در این خبر جزئیات دقیقی از تلفات احتمالی ارائه نشده است.
@withyashar</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/withyashar/13336" target="_blank">📅 03:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13335">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ الان میاد میگه چون موشک ها از رو آب رد شده مسافر حساب‌ میشن و رعب و وحشتشون شکسته حساب میشه پس این جنگ نیست !!! هرچی شده رفع بلا بوده فکر کنین دادین خمس و زکات ، حالا هم آشتی و من به  یک جنگ دیگه پایان دادم و رژیم هم تغییر کرد ولی سلاح هسته ای نباید داشته باشن
@withyashar
👱🏽‍♂️
📿</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/withyashar/13335" target="_blank">📅 03:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13334">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">کانال ۱۴ اسرائیل: اگر رژیم ایران امشب حتی یک گلوله به سمت اسرائیل شلیک کند، تمام دروازه های جهنم به رویشان باز خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/13334" target="_blank">📅 03:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13333">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سنتکام : نیروهای آمریکایی با موفقیت چندین موشک بالستیک و پهپاد ایرانی را سرنگون کردند و در پاسخ به حملات احتمالی ایران در سراسر خاورمیانه، امروز ، حملات دفاعی به جزیره قشم انجام دادند.
ایران چندین موشک بالستیک به سمت همسایگان منطقه‌ای پرتاب کرد؛ اما همه آنها نتوانستند به اهداف مورد نظر خود اصابت کنند. دو موشک ایرانی که به کویت شلیک شده بودند، کوتاه آمدند یا در مسیر شکسته شدند و سه موشک پرتاب شده به بحرین بلافاصله توسط نیروهای دفاع هوایی آمریکا و بحرین رهگیری شدند.
لحظاتی پیش‌تر، نیروهای فرماندهی مرکزی آمریکا (سنتکام) سه پهپاد حمله یک‌طرفه را که ایران به سمت دریانوردان غیرنظامی که به‌حق در حال عبور از آب‌های منطقه‌ای بودند، شلیک کرده بود، سرنگون کردند. نیروهای آمریکایی همچنین حملات دفاعی به یک ایستگاه کنترل زمینی نظامی ایرانی در جزیره قشم انجام دادند.
هیچ یک از پرسنل آمریکایی آسیب ندیدند. نیروهای سنتکام هوشیار باقی مانده و آماده دفاع در برابر تجاوزات بی‌دلیل ایران در طول آتش‌بس جاری هستند.
@withyashar</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/13333" target="_blank">📅 03:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13332">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اصابت در عربستان
@withyashar</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/13332" target="_blank">📅 03:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13331">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">امارات هیچ آلارمی ‌نیست سایت فرودگاه هم کنسل شدن پرواز نشون نمیده فیکه !
@withyashar</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/13331" target="_blank">📅 02:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13330">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اخبار تایید نشده از صدای آژیر خطر در عربستان
@withyashar</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/13330" target="_blank">📅 02:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13329">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/13329" target="_blank">📅 02:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13328">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">حملات جدید به کویت
@withyashar</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/13328" target="_blank">📅 02:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13327">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">رژیم جمهوری اسلامی به بحرین حمله  کرد پدافند بحرین فعال شد @withyashar</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/withyashar/13327" target="_blank">📅 02:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13326">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">۳‌پا
اعلام کرد در پاسخ به آنچه «حمله آمریکا به حاکمیت ایران در جزیره قشم» خوانده، پایگاه‌های نظامی آمریکا در کویت را با حملات موشکی هدف قرار داده و این اقدام را «پاسخ اولیه» توصیف کرده است.
در این بیانیه به آمریکا و هر کشوری که خاک یا آسمان خود را برای عملیات علیه ایران در اختیار بگذارد هشدار داده شده که هرگونه اقدام جدید با پاسخی شدیدتر و فراتر از «قواعد متعارف» روبه‌رو خواهد شد.
۳پا همچنین تأکید کرده است که دوران «بزن و فرار کن» پایان یافته و نیروهای آمریکایی و متحدانشان باید منتظر پیامدهای اقدامات خود باشند.
@withyashar</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/withyashar/13326" target="_blank">📅 02:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13325">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">حمله دوباره جمهوری اسلامی به اقلیم کردستان
@withyashar</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/13325" target="_blank">📅 02:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13324">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مهر: یک موشک به ساحل ایران برخورد کرد
خبرگزاری مهر گزارش داد یک پرتابه در محدوده ساحلی بین شهر سوزا و روستای ماسان برخورد کرده است
@withyashar</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/withyashar/13324" target="_blank">📅 02:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13323">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">انفجار در بحرین
@withyashar</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/13323" target="_blank">📅 02:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13322">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxebCx8I-e7oV2yVcC9lcjTwnY1aii32UA1SfOB9G0BllbIUEOQWxBcymdXiJp97jSocu2OJqY6JLzIvkf0SH8PXZW8xRNjFlKMEFE-XkE6D_jITWnv7KRTGtr7_bQvRrSO2Jv7irXVixMbumPJY3Djra26m0xk0OXExfELyieJQNlzJa6p0OAvBqsGUAkkE7ec8lcG_jQJx6oHXMaF-G0OFz-vLiZlhllkficlVDmuJ3scz2dZRRmLQyU6KnN2vOoj7fWhd1gIWk7bQQ190diXcswpqxQ9JRTrHFW4-6c2ydqURkDju3yhHVyeIbqgGEAqZ6j22l_1QfLhrDo81fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رژیم جمهوری اسلامی به بحرین حمله
کرد
پدافند بحرین فعال شد
@withyashar</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/13322" target="_blank">📅 02:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13321">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dee78f961.mp4?token=KAWsACFWfKMLg33q_Ukw67RfjDrUl9I6UIcckQkMSb2_foG_TgljrmpdWVtAQ1n_Kl5Wm7JLnoVnjlyOsZaUw-5-pKp1bPeS8wMhgDz2vTWIt08WKL8tGm1nJ4bMrYXeSImsRDo_KtMB2Dqo7iQfrE2n25BEbkVcZAmpw1e6HQeXt0brQsNqqSL9LQCwMm0e0sFBP2945vY5AMtW9P81lNWOSd650L0h6EgHDkoMxn4XvHxwvK8su7VNj3B5ZVCeO7D0LRYOZsbJBqRiFxVSYSE8gqYQR7J6h142tYbEODgM7pZO8UriTvftN-l-CExfOjYwWhcMbuL6dbYgpLUScg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dee78f961.mp4?token=KAWsACFWfKMLg33q_Ukw67RfjDrUl9I6UIcckQkMSb2_foG_TgljrmpdWVtAQ1n_Kl5Wm7JLnoVnjlyOsZaUw-5-pKp1bPeS8wMhgDz2vTWIt08WKL8tGm1nJ4bMrYXeSImsRDo_KtMB2Dqo7iQfrE2n25BEbkVcZAmpw1e6HQeXt0brQsNqqSL9LQCwMm0e0sFBP2945vY5AMtW9P81lNWOSd650L0h6EgHDkoMxn4XvHxwvK8su7VNj3B5ZVCeO7D0LRYOZsbJBqRiFxVSYSE8gqYQR7J6h142tYbEODgM7pZO8UriTvftN-l-CExfOjYwWhcMbuL6dbYgpLUScg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصادف در خیابان های کویت بر اثر تماشای موشکهای ایران
@withyashar</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/withyashar/13321" target="_blank">📅 02:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13320">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39ff7e3bcc.mp4?token=a4HpxG-JBNnC4-58ona60nBseTxfTgm8cc2qXvCGbYr5SHP572MyhjY4zXooetvM4kiTlexMMv6vQhBHpAcF1TVLzIYDpxVDzGjmkhrf_Tfr0YhUCuhaXYD3IsaVJ_I9B5gNZAy-8EBG3XxP8iXYAgD_kTNBd0IMD8qCqMWeKs4fkVByNZvH1wI7LsqOffwe5u_XtDqAm6QVIiWmGsvOV-5Zzn42hpVKDTcq1cr0-vT0uCF9Bz92GM-YcwnD-CL9cqaF5_K4w5NDXyrGByUWja71jDA4y5qI8wguCpH5fo1Ku2GMTLCTORNKAACx7nb5KUPi_uQKWk_JiitTGt7xcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39ff7e3bcc.mp4?token=a4HpxG-JBNnC4-58ona60nBseTxfTgm8cc2qXvCGbYr5SHP572MyhjY4zXooetvM4kiTlexMMv6vQhBHpAcF1TVLzIYDpxVDzGjmkhrf_Tfr0YhUCuhaXYD3IsaVJ_I9B5gNZAy-8EBG3XxP8iXYAgD_kTNBd0IMD8qCqMWeKs4fkVByNZvH1wI7LsqOffwe5u_XtDqAm6QVIiWmGsvOV-5Zzn42hpVKDTcq1cr0-vT0uCF9Bz92GM-YcwnD-CL9cqaF5_K4w5NDXyrGByUWja71jDA4y5qI8wguCpH5fo1Ku2GMTLCTORNKAACx7nb5KUPi_uQKWk_JiitTGt7xcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیکه دیگری از لاشه موشک
@withyashar</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/13320" target="_blank">📅 02:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13319">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2918449436.mp4?token=U97aUiv6lt6INy3KcSfLGkUN8-vR565N1lWtWjGaGl-V6LBeD_tK13_XWkWe_BeXvlKIir26rYj4-KpAHCXCEs6DY2vwdZiuTYi9jvcOWC1bVoawY61gz2d7xcHeyX-AZgZHpehQVEdA_tOTwdcNEKAfXe52TAKMPFygb2gspHjKWwcCScECaGe2Yef1QgYRznQvfnHO5e2HbGzii22xPVOZCwrU7zXkexk16oHW_Hf5ByzxvkczXEF64cXrhNiGj_4HuGniDWTG1mFrsdJmGvcpbohtYPqPO1UpIGbOGvZ2lphVlwRRWDdb4bRZBWCPvXlfhB59pmyvKp7KnucgLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2918449436.mp4?token=U97aUiv6lt6INy3KcSfLGkUN8-vR565N1lWtWjGaGl-V6LBeD_tK13_XWkWe_BeXvlKIir26rYj4-KpAHCXCEs6DY2vwdZiuTYi9jvcOWC1bVoawY61gz2d7xcHeyX-AZgZHpehQVEdA_tOTwdcNEKAfXe52TAKMPFygb2gspHjKWwcCScECaGe2Yef1QgYRznQvfnHO5e2HbGzii22xPVOZCwrU7zXkexk16oHW_Hf5ByzxvkczXEF64cXrhNiGj_4HuGniDWTG1mFrsdJmGvcpbohtYPqPO1UpIGbOGvZ2lphVlwRRWDdb4bRZBWCPvXlfhB59pmyvKp7KnucgLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لاشه موشک منهدم شده ایرانی‌توسط پدافند امریکایی کویت
@withyashar</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/withyashar/13319" target="_blank">📅 02:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13318">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اینترنت ایران داره به همین سرعت محدود میشه
🚨
😞
@withyashar</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/withyashar/13318" target="_blank">📅 02:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13317">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9349aaf84.mp4?token=dFbidzUkSaYIfJ9GqvPUvlt7cpLJorR_iMy8pvrrCvA8-rF8dul3nysWIyRlm6v6mwCFzhr0E-91yxNLuMABz0UGiojdjwvFVZwT9bp6Ut_ZmnKL9XrhvZGoxVQIqeq6DnQE2eeEmF5xmfdEV9JdDGoqrm3tDNl7868yNwOeQ6YiA8V9kP1yWKkhHLFh5r9V4zG0RHbzLQCoijp2Miq5mkYF-MTFC5LbRWoxFxKDOoEvbm9BEIWc7F2QLzneHMUCB8zGUn_ftAcU6fbS_1UTDsUFfqZzhQ-bLA2mgRk1VqdTGE6bRiz-GLLrDMRFzQpr039GkfdTua9JOrXCibpSxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9349aaf84.mp4?token=dFbidzUkSaYIfJ9GqvPUvlt7cpLJorR_iMy8pvrrCvA8-rF8dul3nysWIyRlm6v6mwCFzhr0E-91yxNLuMABz0UGiojdjwvFVZwT9bp6Ut_ZmnKL9XrhvZGoxVQIqeq6DnQE2eeEmF5xmfdEV9JdDGoqrm3tDNl7868yNwOeQ6YiA8V9kP1yWKkhHLFh5r9V4zG0RHbzLQCoijp2Miq5mkYF-MTFC5LbRWoxFxKDOoEvbm9BEIWc7F2QLzneHMUCB8zGUn_ftAcU6fbS_1UTDsUFfqZzhQ-bLA2mgRk1VqdTGE6bRiz-GLLrDMRFzQpr039GkfdTua9JOrXCibpSxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آسمان کویت کمی‌پیش
@withyashar</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/withyashar/13317" target="_blank">📅 02:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13315">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">جنگنده‌های اسرائیلی پرواز کردن
@withyashar</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/13315" target="_blank">📅 02:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13314">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/13314" target="_blank">📅 01:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13313">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پست جدید از صحبت‌های بسیار زیبای شاهنشاه آریامهر  ارتباط قلبی ما
❤️‍🩹
فرا مرزی شده  https://www.instagram.com/reel/DZGNeRLxq-Y/?igsh=MXQ1dTZmdXk2bGZpdQ==</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/13313" target="_blank">📅 01:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13312">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b76b57549.mp4?token=og_kBr-dNlwOVwwTtv4T_2htW7r7-y2YwMCCnQv8dwuHwdAD0dqadTnDEkiC_8dj0gi2umuiU1QRat1wBRx7Im6VYxUCirx-f0XSdQqGywKYzygddTRBNIO1hpS3s0j5n5lScS-0dODDooVje-g_YYLL9gtUpk1A1YzTZPios7CSIV3GHZkcvE5OMxDUmtgDkFFFCWg-bz4JUok8fP-g3Q8MPZFt7LJOAqHYOoo3qbH4-zQStaVegHDio0-_ie64KiCJCyjZyZ0KS6smPE0KRvl9zqAxCgBGSlrhja-eya53I7C-f4ZZAIRC92Q9EhyDWJRMG11Zbk1r2GStLqMU2CLfByWY9fp6VFazs1JuOYCZm1tiLNtetv0Q3B3iQSZLcNAovREg31EQerRIgDtg2BJaldgeYC-kHjeDoPYcnGp592QS_klKjtl6IL6O04RxdjYfKKdpjeanFY61r9Qrl8ImcwmS9eafCV8-gMki-rnrQR3O1Zmom0zT799tJfBWWZLo2Ia7wIIdFNrJ5NCoy7RIlkCugM8xIq1RrCYM5MtOhI6UQ0_hifWQ0dwimcJ1b-WuBMVycXYNdOQ8YNy5xBpNOXIz5d5spDN_pPMc95vVu_sjkSHktOJWYQGde8igXezN6cHncOF0MZibPmK19ZN8_NWhiws0GPiOYRPaaRs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b76b57549.mp4?token=og_kBr-dNlwOVwwTtv4T_2htW7r7-y2YwMCCnQv8dwuHwdAD0dqadTnDEkiC_8dj0gi2umuiU1QRat1wBRx7Im6VYxUCirx-f0XSdQqGywKYzygddTRBNIO1hpS3s0j5n5lScS-0dODDooVje-g_YYLL9gtUpk1A1YzTZPios7CSIV3GHZkcvE5OMxDUmtgDkFFFCWg-bz4JUok8fP-g3Q8MPZFt7LJOAqHYOoo3qbH4-zQStaVegHDio0-_ie64KiCJCyjZyZ0KS6smPE0KRvl9zqAxCgBGSlrhja-eya53I7C-f4ZZAIRC92Q9EhyDWJRMG11Zbk1r2GStLqMU2CLfByWY9fp6VFazs1JuOYCZm1tiLNtetv0Q3B3iQSZLcNAovREg31EQerRIgDtg2BJaldgeYC-kHjeDoPYcnGp592QS_klKjtl6IL6O04RxdjYfKKdpjeanFY61r9Qrl8ImcwmS9eafCV8-gMki-rnrQR3O1Zmom0zT799tJfBWWZLo2Ia7wIIdFNrJ5NCoy7RIlkCugM8xIq1RrCYM5MtOhI6UQ0_hifWQ0dwimcJ1b-WuBMVycXYNdOQ8YNy5xBpNOXIz5d5spDN_pPMc95vVu_sjkSHktOJWYQGde8igXezN6cHncOF0MZibPmK19ZN8_NWhiws0GPiOYRPaaRs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دفع موشک های ایرانی در کویت
@withyashar</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/withyashar/13312" target="_blank">📅 01:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13311">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/withyashar/13311" target="_blank">📅 01:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13310">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پایگاه عریفجان در جنوب کویت، نیز هدف قرار گرفت
@withyashar</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/withyashar/13310" target="_blank">📅 01:46 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

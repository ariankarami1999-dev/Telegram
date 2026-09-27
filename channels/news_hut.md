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
<img src="https://cdn4.telesco.pe/file/S3wgdqW2d8hdyUXkpgTgwpjZP-vOfDuEbH7fOvdFntQX8FpAuMSmJZrQFlg-ndwR4JBpYUqQhRy8s4gE7oymxDbxBsaqeEx3a8k4bNen0v4oXqCrxSTnmqkxL8-ntpQZD-ROeSoPwB5zIoj2fTVwXFP_HEvTbtlD4oosneOI15pOJC0CJDRmX3_Xy523C1aguJRYUcaTUrwOxDCPWtHzKQDsKH37ktyTxzeqRrYc1mZpeydvDZUUvNSbKpdZwJk98ZmEkGAjIgJDgwGLMCSobLUCsDzUWvGbM8260WME-4bcpA9tcSK6wptfafPGyKz3aYVmZtgCc-pa63PVE5B8Rw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-05 21:22:03</div>
<hr>

<div class="tg-post" id="msg-72381">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51ab5c624e.mp4?token=pn5a_IUhlvR_cCCxDszJh8KwyzLzBmTW59RD_QxMrurWEVrsYgWFhWmcazwpYEAZqYBoh7DU85aDNrY9vw-veC_7SndYc5xJ7_IpFRdmJKc4tm9nK_2h7bLADKYaQEvaq85nSy6iyvx7LK_WD9wg9apkxLYL-_sHUwuBpz331eHFkK4Rf1FfrqqpQh-9O7GeJNArMBKg4caqGGCn-I5rGx5nL_TZMsmh3hXkji3GS6aL_q7U3R-636A11DVaEmjNZyhtY5HWSCWshzth6u_VeiiX7ivjjTLTlLXtH40zioXDGrGA0Sqxwers2Z1CLhgGsqg2Wbc5qCc1du7TEpZDtX2uJi8FPjvUHGvmqRqOChsFYS_sRcJL55OtaMSehWEs1kCsDsXPay9pGmj6nTGhFejF0zaETAR6TXbJQOyaHzcRouqMn_4y2NHe2k5ugFTGA8kqVDPKGseh2vwaRLOM939D4fhBvsgjttXT7PXyLRgjDIiQd-NFbwVSALxw3OOxUUchgNjQqzWQiYj9cBGm67nz0S8mzWheLjFbfUQIN_AI_RSHlgVzTrZ1zBWhixXjKIJObd_Kl6bhqqiuhYNnrGq6__KxNq0VNltQ48hduveKXZQd1jr5O84AbXUc-6HWW0pn7MWV6xeFAsKWRUDGqram8SvvwoZkm_7ZfTwxCJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51ab5c624e.mp4?token=pn5a_IUhlvR_cCCxDszJh8KwyzLzBmTW59RD_QxMrurWEVrsYgWFhWmcazwpYEAZqYBoh7DU85aDNrY9vw-veC_7SndYc5xJ7_IpFRdmJKc4tm9nK_2h7bLADKYaQEvaq85nSy6iyvx7LK_WD9wg9apkxLYL-_sHUwuBpz331eHFkK4Rf1FfrqqpQh-9O7GeJNArMBKg4caqGGCn-I5rGx5nL_TZMsmh3hXkji3GS6aL_q7U3R-636A11DVaEmjNZyhtY5HWSCWshzth6u_VeiiX7ivjjTLTlLXtH40zioXDGrGA0Sqxwers2Z1CLhgGsqg2Wbc5qCc1du7TEpZDtX2uJi8FPjvUHGvmqRqOChsFYS_sRcJL55OtaMSehWEs1kCsDsXPay9pGmj6nTGhFejF0zaETAR6TXbJQOyaHzcRouqMn_4y2NHe2k5ugFTGA8kqVDPKGseh2vwaRLOM939D4fhBvsgjttXT7PXyLRgjDIiQd-NFbwVSALxw3OOxUUchgNjQqzWQiYj9cBGm67nz0S8mzWheLjFbfUQIN_AI_RSHlgVzTrZ1zBWhixXjKIJObd_Kl6bhqqiuhYNnrGq6__KxNq0VNltQ48hduveKXZQd1jr5O84AbXUc-6HWW0pn7MWV6xeFAsKWRUDGqram8SvvwoZkm_7ZfTwxCJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری:
رئیس‌جمهورایران این هفته اظهار داشت که ایران هرگز به دنبال سلاح هسته‌ای نبوده است؛ با این حال، ایران اورانیوم را تا سطح ۶۰ درصد غنی‌سازی کرده که این میزان ۲۰ برابرِ درصدِ غنی‌سازیِ مورد نیاز برای تولید برق است. چرا ایران به ذخیره‌ای ازاورانیوم با غنای ۶۰ درصد نیاز دارد؟
عباس عراقچی:
اولاً، غنی‌سازی تا سطح ۶۰ درصد غیرقانونی نیست و همچنان در چارچوب معاهده منع گسترش سلاح‌های هسته‌ای (NPT) و برنامه صلح‌آمیز ما قرار دارد؛ ما این کار را برای اهداف مشخصی، از جمله مصارف پزشکی و دیگر مقاصد، انجام داده‌ایم. با این حال، ما پیشنهادی برای تعیین تکلیف مواد غنی‌شده تا سطح ۶۰ درصد در سال‌های ۲۰۲۵ و ۲۰۲۶ ارائه کرده‌ایم؛ موضوعی که اگر آن‌ها حسن نیت و عزم واقعی خود را برای صلح ثابت کنند، قابل بررسی است. پیشنهاد ما این است که مسائل پیچیده‌تر به مراحل بعدی موکول شوند و در این مرحله بر اعتمادسازی تمرکز کنیم. به همین دلیل، ما این طرح هفت‌روزه را بر اساس تفاهمی‌که در گذشته با صاحب‌نظران آمریکایی داشتیم، ارائه کردیم. نخستین گام این است که دارایی‌های ما که به‌طور غیرقانونی مسدود شده‌اند، آزاد شوند؛
@News_Hut</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/news_hut/72381" target="_blank">📅 20:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72380">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">صدای انفجاری از سمت تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/news_hut/72380" target="_blank">📅 20:16 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72379">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNn2yzzAiDfomiPbfcWs0SgNp6ixI03tyivYi6W5tTyKYMTB7z2ThR2XyznUQsyt7V-kLV7AQxhbK-gFwZOB_A9eMRAMkUClu45Zx6RVxCquIyuavOGM5myv4ohA_Ayts4-nhCry-mAwJi_YALSQXCWgEALdWlDMfcEEnRi922hb2Y8S16eqs3IvEOJy8apqJH7SWc_ykPKKaXeRGJSeswa5UKrl2pOy3Vd30DOT-OCsRqxP0sh2fbmtBJJbN0gDik3chyLAM78eIOF7TazR9VQn_ZEcCz7sugZYiYi95slIJHpbBN1EHOoYK7ZL29IcZiyBlVSktpnlcwgxztoLBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای آوش به نقل از اداره حقوقی مجلس: حمید رسایی به ده ماه زندان محکوم شد
آوش:
این پرونده که دوبخش دارد مربوط به سال ۱۴۰۲ و زمانی است که حمید رسایی هنوز نماینده مجلس نبود.
حمید رسایی که از حکم شعبه دوم دادگاه ویژه روحانیت تهران، برای عذرخواهی نسبت به انتشار مطالب خلاف واقع درباره مجلس شورای اسلامی امتناع کرده، با حکم قاضی برای تحمل ۱۰ ماه حبس تعزیری به اجرای احکام احضار شده است.
بخش اول پرونده مربوط به انتشار مطلبی با تیتر «دستکاری قالیباف در اسناد مجلس» در صفحه اول نشریه «۹ دی» است، و بخش دوم مربوط به انتشار کلیپی تصویری در کانال تلگرامی متهم که رسایی در آن از تعبیر «دیکتاتور پارلمانی» برای باقر قالیباف می‌کند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/news_hut/72379" target="_blank">📅 20:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72375">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZCH96pkv5gUHVrk4raXFuhoIdryT4mf3q8lWnQ4A_Pwc6Sd-b1meO7Xc3ph7j7R-X54FFdKvfQ9hVMxQA4w6tcvB8riDEAWNweSXPgPX7RSIC1elBSj3X79J8ZSIGqryFBXuAZxvzdmKk4TwzWbUjDAwxHh-fTrtQYZmh6es4ikqBp8WnXtZhl2xFD2KR-pXnKH8OGVgYMtGHIUeNlU8yBEuAGY7tiUrbp9w8GHioeHvqRv6gXiruiVxHW1KsERrpfSJl3UqrnU6XF8iF7muKy__gkD2CSKugDy6Cq1Exzi4A7Ficn0f6ObpncaJAYZQ5G_TREaw0RJiZXMqPRl6hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mea0ZbmkMGu3UdjYZivSvAIXzcDc_4laDdytlKi4pZ-rRbd4QDyU-Sy9KsievyHNY6eGpDRUaWGIv7DUmgNBnlZ47KLocm3ZTFMHbBC7YV_8kXKUQSSUu2dORngWBMlVuZXUnsAKgqiOUgMS8odXxr9ck1YZVfx8b23We1xoH4k5aTLVRJWJRdpUvcc8ohUwFDsI9jAEyOkpfLza9AyiOdUk6be5iUi-URI_LKKDzsVJ6U79ODLLl16d11rIQ4W0pDNoCswn86Roy-Z81CJLHOwPDZo7qRMYL_1bbM2dsWwgz7NTP6lJ2SML8bUfgDpWSV1UZl8nUV25bep7NkBQ5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b78db64d5d.mp4?token=isY47yglFXCzkbmzT3QrI2vZRNDynMMcpvR_Y4a2itGd9hOnA8D7FIa73MHvTHCpHBEg85B89nftDhgydu-vW-zHrKssN5T4V1eQyRuicDI6Ewy4AfpKPRjDZNTX1tEjdfviazdN26vEOuN4uaYWzCJiLI5yR5UObpfctCPZhZt5x5w_6-2vGmFpz8YdgkERGNV0HTh2F3Pg4C_HhbanzZmdWBq4AdRPLGQikb6z577RVvxFdpHGfODDtZZYytF0LGMgiynZijfG-khfp7WREJ4HEq-kEH7BVxjHZvBXT2E_Tem9--UBB3nuih9-Gkqwz1IdpCgohnvGQ46nqHGe_1dI1oNuHHaQdx9IyBQAz6gA6LXrMfFKBATQvXi8ycqUacQuS-LoVnDPKf4x_7GFazziG5pmLj3VQvl_OWukNNnBWwQAhwlgYvuiSCLgz4riOCV7e0dD25eK6BBKWsrJptfE0Wx8LWj5S360XiCStAqAub5T6fAH3hViidnRJYZBWIZM3XWIWfVvAJo_g4YeMNuKUYflRS934lHnRAozad6MXBVda3wkhlOu0kTPaMq6fJ-jji0K4Y7IXWzCvITavIeCbpcrtV0WcuoI1XLQNHhATgJS58afO2VwepinwXmkQsv8W_TIvYdLXk-VMkv0ONEuX4FE4a8RTP4OygGHJp8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b78db64d5d.mp4?token=isY47yglFXCzkbmzT3QrI2vZRNDynMMcpvR_Y4a2itGd9hOnA8D7FIa73MHvTHCpHBEg85B89nftDhgydu-vW-zHrKssN5T4V1eQyRuicDI6Ewy4AfpKPRjDZNTX1tEjdfviazdN26vEOuN4uaYWzCJiLI5yR5UObpfctCPZhZt5x5w_6-2vGmFpz8YdgkERGNV0HTh2F3Pg4C_HhbanzZmdWBq4AdRPLGQikb6z577RVvxFdpHGfODDtZZYytF0LGMgiynZijfG-khfp7WREJ4HEq-kEH7BVxjHZvBXT2E_Tem9--UBB3nuih9-Gkqwz1IdpCgohnvGQ46nqHGe_1dI1oNuHHaQdx9IyBQAz6gA6LXrMfFKBATQvXi8ycqUacQuS-LoVnDPKf4x_7GFazziG5pmLj3VQvl_OWukNNnBWwQAhwlgYvuiSCLgz4riOCV7e0dD25eK6BBKWsrJptfE0Wx8LWj5S360XiCStAqAub5T6fAH3hViidnRJYZBWIZM3XWIWfVvAJo_g4YeMNuKUYflRS934lHnRAozad6MXBVda3wkhlOu0kTPaMq6fJ-jji0K4Y7IXWzCvITavIeCbpcrtV0WcuoI1XLQNHhATgJS58afO2VwepinwXmkQsv8W_TIvYdLXk-VMkv0ONEuX4FE4a8RTP4OygGHJp8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ساعات اولیه ۲۷ سپتامبر ۲۰۲۶، ساکنان از سه وسیله نقلیه مشکوک که به سمت پایگاه نیروی هوایی سلطنتی فیرفورد در حرکت بودند، خبر دادند.
یک توطئه تروریستی برای انفجار پایگاه نیروی هوایی سلطنتی فیرفورد وجود داشت.
پنج مرد در منطقه ویلفورد به ظن ارتکاب جرائم تحت قانون مواد منفجره دستگیر شدند.
پایگاه نیروی هوایی سلطنتی توسط بمب‌افکن‌های آمریکایی برای حمله به ایران استفاده می‌شود.
پلیس مبارزه با تروریسم در حال بررسی این موضوع است که آیا ایران پشت یک توطئه بمب‌گذاری مشکوک با هدف قرار دادن یک پایگاه نیروی هوایی سلطنتی مورد استفاده نیروهای آمریکایی بوده است یا خیر.
@News_Hut</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/news_hut/72375" target="_blank">📅 19:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72374">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9233dc65e9.mp4?token=klBtLA96IeZKfDT0krf7otmswMZktCaUgZlHlS9yKi31DZeyIUs7gMPQI7NFSbTaOD7FOQ8wmAATp9APpc69XmN3nVq_0qbt1X9fqp8PofzFzikNSMTvI5SS2J3NOoxRdrqZGWlym4Nc5iEegUJfqnJJWUQo4xXUgjApVq5vy27iV6iKqwVMWPiNoycWhCfhhw2ydMWInnqrElWV3_1qgfbJMiIldBzkdbZ6TvPnqlN5qs1Fugp-JLhfSMLaavBkCMM7CdDoAp1tjJu6Zzba_oHSjxpAiHrxZ5UVaNqIUNGgspon1ILw4pyxjQLUoadSXksy_8rJ35F_R8x8noy0nJtRUhN97xp6PgPrmz8aQygo_fknetrlybq9DoUTo8rGBMgz3BrrtC80pKsgJwVOsBSsotydhOGfog3itMmUXpSlvG1x4wMj-3qCDxs7A5-d-WpI_T_MR3bAMfy6mnTQ4c39GrmYIrx3MDEjgKhEOrLbJI7uBd8oy5qIaWMMK1TT4oKkg3W4fx5ikFm1N0LveKJ6v68GZgbwzA8gK020XaZegj4WgXew_82oDx_mRrYQVkQMGR7bcXB7MxTIbjxjnTvdqo1OLN6TtdWaPgMkmC0RlRR0-mSavxLi5VkLQoHDnxN0YGVjTVfJ_ARlkAgGh1kiusD093kL_yIpr8xRUic" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9233dc65e9.mp4?token=klBtLA96IeZKfDT0krf7otmswMZktCaUgZlHlS9yKi31DZeyIUs7gMPQI7NFSbTaOD7FOQ8wmAATp9APpc69XmN3nVq_0qbt1X9fqp8PofzFzikNSMTvI5SS2J3NOoxRdrqZGWlym4Nc5iEegUJfqnJJWUQo4xXUgjApVq5vy27iV6iKqwVMWPiNoycWhCfhhw2ydMWInnqrElWV3_1qgfbJMiIldBzkdbZ6TvPnqlN5qs1Fugp-JLhfSMLaavBkCMM7CdDoAp1tjJu6Zzba_oHSjxpAiHrxZ5UVaNqIUNGgspon1ILw4pyxjQLUoadSXksy_8rJ35F_R8x8noy0nJtRUhN97xp6PgPrmz8aQygo_fknetrlybq9DoUTo8rGBMgz3BrrtC80pKsgJwVOsBSsotydhOGfog3itMmUXpSlvG1x4wMj-3qCDxs7A5-d-WpI_T_MR3bAMfy6mnTQ4c39GrmYIrx3MDEjgKhEOrLbJI7uBd8oy5qIaWMMK1TT4oKkg3W4fx5ikFm1N0LveKJ6v68GZgbwzA8gK020XaZegj4WgXew_82oDx_mRrYQVkQMGR7bcXB7MxTIbjxjnTvdqo1OLN6TtdWaPgMkmC0RlRR0-mSavxLi5VkLQoHDnxN0YGVjTVfJ_ARlkAgGh1kiusD093kL_yIpr8xRUic" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت وزیر خزانه‌داری آمریکا درباره ایران:
ایرانی‌ها می‌گویند که تنگه‌ها را ظرف ۷ روز باز خواهند کرد؛ [در حالی که] تنگه‌ها باز هستند.
ما اکنون به‌طور میانگین روزانه ۱۵ تا ۲۲ میلیون بشکه [نفت] صادر می‌کنیم.
نتیجه این است: ایالات متحده بیش از ۱ میلیارد بشکه صادر کرده، و ایران صفر.
@News_Hut</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/news_hut/72374" target="_blank">📅 19:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72373">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15b7065503.mp4?token=e67toM9JHn0tfsA7-fo57OaMi1o1q3-6puayBTBiPEH1u2klbcBcSHSKuQm6TkieCX1ffZGMnzhxm9TiBsuhg7x_71JchXmAEzbW_E67TWWSHp0LGPD4-E9AzWH8sqxfTbzt7pAMkUV4CGJYxbgo8uzGjsszS0VtohbSZe6hZoaAqKibdl_1EjUbeedGxYHDa7XuKaF6iX3F8K3iBdZcEikvvUiX2P0tTOXXC9KsyG8Lc5p9lAPHu02gOTCpTactphuUtbqFH1jbdvlI_RZZMnovzVUuDkIonVb40SjtX-DDBdM7FKJX5aA6dxsvNbzTOZVYW2BROpK31PMIML7RlIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15b7065503.mp4?token=e67toM9JHn0tfsA7-fo57OaMi1o1q3-6puayBTBiPEH1u2klbcBcSHSKuQm6TkieCX1ffZGMnzhxm9TiBsuhg7x_71JchXmAEzbW_E67TWWSHp0LGPD4-E9AzWH8sqxfTbzt7pAMkUV4CGJYxbgo8uzGjsszS0VtohbSZe6hZoaAqKibdl_1EjUbeedGxYHDa7XuKaF6iX3F8K3iBdZcEikvvUiX2P0tTOXXC9KsyG8Lc5p9lAPHu02gOTCpTactphuUtbqFH1jbdvlI_RZZMnovzVUuDkIonVb40SjtX-DDBdM7FKJX5aA6dxsvNbzTOZVYW2BROpK31PMIML7RlIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت درباره ایران:
تنها ۱۵ میلیون بشکه دیگر از نفت ایران روی آب باقی مانده است. ایران دیگر چیزی برای معاوضه یا دادوستد نخواهد داشت.
احتمالاً ظرف دو هفته آینده، آن‌ها آخرین محموله‌های نفت خود را به چین تحویل خواهند داد و پس از آن، دیگر چیزی در اختیار نخواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/news_hut/72373" target="_blank">📅 18:58 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72372">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GdQUYeDRwbjlA3vNLd-7aTe-fuhMyMufVFjUYSjy5BOZyZxwJK9H9FITD2ntWjLHVTkG69X3l22o421uhF8mheDoKnbn3GIlTw_2fAu6SlUBquQCXFtWaiGDvg7OtWYENbHhz2WHvYf0hwLUVh9OYRdoXdt7zJfeSDFc6i1Umj580hb7IMbE5RMO_TufnOHkEPQW9qTJ1kCqUqIp-3YBvgiaUQK7rhfHu_RdG_SChHxsjvkq_s1xUOMFHIaSfdKa8loaYPQ32FogUC2o-J_hfjSKFT6wmj9TRTn4BZ4gLuCAtmgjWdD-KOqfyj1sZCFPefFOvPxUJKY7LoOr8GKv-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به «اکسیوس» گفت که با وجود رد پیشنهاد ایران، انتظار دارد در هفته جاری مذاکرات بیشتری میان آمریکا و ایران انجام شود:
آن‌ها خواهان توافق هستند، اما این آن توافقی نیست که من می‌خواهم. آن‌ها در بازی خود زیاده‌روی کردند.
ترامپ در پاسخ به پرسشی درباره ازسرگیری حملات:
همواره به آن فکر می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/news_hut/72372" target="_blank">📅 18:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72371">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd27ff889b.mp4?token=orkKIKlZ-ZbHLatIhLYFP_sTCTGUHcCm2V6vDpyY9ALb_UkdJaDXdnUiRuxE2rkHYOxxtYzuma_1Y4qEzC71XFt1CEKllIGCLQmiY05x5QPA_WG3XCLB2rzCNRE8eMmaD06TXtwqp_5SS8dEzaxuwsxRil9-z9HsWEcyWb60iJi_XroGOveyG4EpD9kw2XaiqNfJzUmGK6G-jAycgxFaYkD3-wJXAJczpp3v_azJytNyN2e6YOxptURwvvXJRCba-9of6-vOk-5BKBiJDwNNgtA0yAuIJBbz3P37s8P-oLdg2G1Tyg1C_HAVOOnNeqj8T_cYHeM7E4o27B2DY4-MBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd27ff889b.mp4?token=orkKIKlZ-ZbHLatIhLYFP_sTCTGUHcCm2V6vDpyY9ALb_UkdJaDXdnUiRuxE2rkHYOxxtYzuma_1Y4qEzC71XFt1CEKllIGCLQmiY05x5QPA_WG3XCLB2rzCNRE8eMmaD06TXtwqp_5SS8dEzaxuwsxRil9-z9HsWEcyWb60iJi_XroGOveyG4EpD9kw2XaiqNfJzUmGK6G-jAycgxFaYkD3-wJXAJczpp3v_azJytNyN2e6YOxptURwvvXJRCba-9of6-vOk-5BKBiJDwNNgtA0yAuIJBbz3P37s8P-oLdg2G1Tyg1C_HAVOOnNeqj8T_cYHeM7E4o27B2DY4-MBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی:
ما همان‌قدر که برای مذاکره آمادگی داریم، برای رویارویی با هر چالشی نیز آماده‌ایم.
ما در برابر هرگونه تجاوزی علیه خود قاطعانه می‌ایستیم، حتی اگر کار به جنگی آخرالزمانی بکشد.
@News_Hut</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/news_hut/72371" target="_blank">📅 18:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72370">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">حملات اخیر پهپادهای جت‌سوز روسی «گران-۴/۵» (Geran-4/5)، یازده مرکز داده اوکراین را هدف قرار داده است که شامل ۱۰ مرکز در کی‌یف و یک مرکز در دنیپرو می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/72370" target="_blank">📅 18:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72369">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c66f5a0a1.mp4?token=hWB0oxnaLJtEAvxN2RNrQoEjB9_Cl6iDDHdRBefYym-my29kyvhA30AOrvmUf7uZDF51FGXNDgh3NwjtMZnrv-HW-tu9KbCGMpS-qaOpLqhT6D3A7oeCd8F8Ecppm9LcyXv52KMUy7KxupVA3a6VzSTXSDJMLE0ADugN73BxgkaWAFL3faU2MOZxZwBEfZ2ynnAyjsBA9z5T5aCPpEme5EuTLOjZ-3wf8YLMZfv7t7ADrYdk9QE7BClQLDFWQhe24lZBircBBeZKKS65PujuldPqEg5HwIIInQJnmniezyG4kfFjmFfqM7uEzMQftSi9Q2EU8O_b7CmHTWynQ-jZ0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c66f5a0a1.mp4?token=hWB0oxnaLJtEAvxN2RNrQoEjB9_Cl6iDDHdRBefYym-my29kyvhA30AOrvmUf7uZDF51FGXNDgh3NwjtMZnrv-HW-tu9KbCGMpS-qaOpLqhT6D3A7oeCd8F8Ecppm9LcyXv52KMUy7KxupVA3a6VzSTXSDJMLE0ADugN73BxgkaWAFL3faU2MOZxZwBEfZ2ynnAyjsBA9z5T5aCPpEme5EuTLOjZ-3wf8YLMZfv7t7ADrYdk9QE7BClQLDFWQhe24lZBircBBeZKKS65PujuldPqEg5HwIIInQJnmniezyG4kfFjmFfqM7uEzMQftSi9Q2EU8O_b7CmHTWynQ-jZ0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جعفرقائم پناه؛ معاون اجرایی پزشکیان:
به عربستانی‌ها گفتم انشاءالله برد موشک‌های ما به آمریکا برسد تا دیگه به پایگاه‌ آمریکا تو کشور شما حمله نکنیم بلکه مستقیماً به خود کاخ سفید موشک بزنیم
😐
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/72369" target="_blank">📅 18:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72368">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/72368" target="_blank">📅 18:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72367">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GVjAcqBwtiXeHDX2NlIyVeuNusGXjfKFLiM26pgacvxpBVAYF1-Z6cJTMYySS8dM1M4QYIf7bXonMDNc8NBUXGO0XuepzeTiwU6RIM1LW7PVhOruhF-xdu0jZ7-YM8FTWgOGJNyebiXqO9U9sdFJ643xsMaM2KrkwZfL1VGSVe6OLdlj3d_ramjxBUBob5xvuqtYeKkpCZEh8xel8oEhUaeYX2zYLVmeqWLpnyeopqKh702WkYi_eLXJY9lDP0zLUF_tbpOF2qCe5IBvYwUwQWcpk9_SYhjnP2C4dzHEa4VE0eoQVydMV1hicApZ9gwE04iAAmRDuPVADSf1OQYOIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/72367" target="_blank">📅 18:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72366">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a495b9a3cc.mp4?token=ZIozHMWGy3_YNbQoX95KRtzvnwxhdBPe3zPP8pjMlJFunY5g-vhJkjkQJfj0uzK0zp_P3GedjfVPalKc7X7gXWi122n5uckn2yWznS-0SAsvAAuzI9coaDZEA6FqyF-5-2FCJmJRaIOW8x87g6wVx_XPDzLapSSdq00aSbZ_9Rjb0pUMphGWyDTjzUYaZZQW4KVgvIwNC_PoPMJTxBkWRqUxzUXooaI_NhiBn2N1m_Nh8-rRms1B-4gLrJMu6kSmuZijUKkGc7CndfbqzcmK0setoHHHGmVEKHIuB_gFGbsNmnOV9Q80Ou5sR4p9hw2CLQuXTUMd1kLYt8hD5Y6qOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a495b9a3cc.mp4?token=ZIozHMWGy3_YNbQoX95KRtzvnwxhdBPe3zPP8pjMlJFunY5g-vhJkjkQJfj0uzK0zp_P3GedjfVPalKc7X7gXWi122n5uckn2yWznS-0SAsvAAuzI9coaDZEA6FqyF-5-2FCJmJRaIOW8x87g6wVx_XPDzLapSSdq00aSbZ_9Rjb0pUMphGWyDTjzUYaZZQW4KVgvIwNC_PoPMJTxBkWRqUxzUXooaI_NhiBn2N1m_Nh8-rRms1B-4gLrJMu6kSmuZijUKkGc7CndfbqzcmK0setoHHHGmVEKHIuB_gFGbsNmnOV9Q80Ou5sR4p9hw2CLQuXTUMd1kLYt8hD5Y6qOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ درباره ایران:
به‌محض اینکه ایران تسلیم شود و جنگ پایان یابد — که به‌زودی هم چنین خواهد شد — قیمت نفت به‌شدت کاهش خواهد یافت.
قیمت نفت سقوط خواهد کرد و قیمت همه کالاها پایین می‌آید؛ البته قیمت مواد غذایی هم نسبت به دوران بایدن بسیار کاهش یافته است. تقریباً قیمت همه چیز پایین آمده است.
قیمت نفت اکنون نسبت به دوران دولت بایدن کمتر است.
ما مقادیر عظیمی نفت استخراج و عرضه می‌کنیم؛ دیشب رکورد جدیدی در انتقال نفت از تنگه هرمز ثبت کردیم؛ مقداری بیش از آنچه پیش از آغاز جنگ از آنجا عبور می‌دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/72366" target="_blank">📅 17:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72365">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82ccd821b0.mp4?token=WyP1P6OvOpjHK7qV2s2uyex4zQALSLSujcCQECUYVdydv1-kjBCA_C1Q_dESkz1cCx648AP6aLBB6pFdkDctK4HhtM6cW8CjVuU_wDta2buTKboTb9mK5SH4H98K5ZGmKolNBmmHkiuDgJWc6fYlx8XiuLQ5zNA96i9F38XtQAUHplb2puyHcG2_irsQYyno6rogEr28Yx2vYgDFDpBS_TKtCY8TRGvgC36HR8rUc-Xb-lAozkyPYg8lL1CrlavqY5U1SPseOZ5PgPGiQ_2Wm0sfPvVmWCWrflPT67rN_IvB6_dyuFAwO133MmDXUB-s1_t66vXAPcKlrChrJP3icg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82ccd821b0.mp4?token=WyP1P6OvOpjHK7qV2s2uyex4zQALSLSujcCQECUYVdydv1-kjBCA_C1Q_dESkz1cCx648AP6aLBB6pFdkDctK4HhtM6cW8CjVuU_wDta2buTKboTb9mK5SH4H98K5ZGmKolNBmmHkiuDgJWc6fYlx8XiuLQ5zNA96i9F38XtQAUHplb2puyHcG2_irsQYyno6rogEr28Yx2vYgDFDpBS_TKtCY8TRGvgC36HR8rUc-Xb-lAozkyPYg8lL1CrlavqY5U1SPseOZ5PgPGiQ_2Wm0sfPvVmWCWrflPT67rN_IvB6_dyuFAwO133MmDXUB-s1_t66vXAPcKlrChrJP3icg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمود کریمی، مداح حکومتی، در مراسمی برای علی خامنه‌ای نوحه‌ای به زبان انگلیسی خواند
😂
@News_Hut</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/72365" target="_blank">📅 16:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72364">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94d47f6b44.mp4?token=Cvf6KCMbBP0s-Bt91NXwxcWncjR1-h001jid-R1R0W81Fc2C53hJLdAxnVkjVHr5n-9_1ATdITyzTmn_YDDKb8jEXbbWpkOSOGh0ufbZx6VK77hRmA3hZ0poga9B6-7uJkxtK-G1hpdziHq8M7Fjyzbmi9Y-fVCFEbT0gKlhKkF6bwbOt10oSKtILF9s7HhpeTe7_XMg_6BoAC4I4RFtW9K200Z8PGsmy3jtuJOa55yOiH5qX0REfwpIZVN1kdQV-H7b-8ne3CU1UKM2qophs2y2RmnnHUwFPxxHVHBmlt1eNLwGIqeQdbMZXyyocWw4v7l89k9EHRDuWibPkm74403KBjMf2Fx0ed9AZskI5HtqB3bhuIIPwwJJSmRNNnbBEDeCmXu2sGsq3To271iAO2qxOd0_2TmpL_LElZnI8L8XfU7JlXkmpQ_VCUZpFX7ss5OfSdPJtgwzCj209-OnsILtfwDVCGOt-7BU-voyAmgB8uVew_Bc_4XJtZBaYSCuKZHnetL5Hmt0CUjewWgzc7fhYoheyK0xd3FO33NBzcZX-JOy6k8zMW1HeTBANy17bVrTzxCNv5uuHX09gG8EncInSABqwbumxIe0MFuESo48HrbYcD_3poD-fgbOWyD54be0QuriCLVe49hPYRdAFAKb3Za37fQXpLDgMecXbPo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94d47f6b44.mp4?token=Cvf6KCMbBP0s-Bt91NXwxcWncjR1-h001jid-R1R0W81Fc2C53hJLdAxnVkjVHr5n-9_1ATdITyzTmn_YDDKb8jEXbbWpkOSOGh0ufbZx6VK77hRmA3hZ0poga9B6-7uJkxtK-G1hpdziHq8M7Fjyzbmi9Y-fVCFEbT0gKlhKkF6bwbOt10oSKtILF9s7HhpeTe7_XMg_6BoAC4I4RFtW9K200Z8PGsmy3jtuJOa55yOiH5qX0REfwpIZVN1kdQV-H7b-8ne3CU1UKM2qophs2y2RmnnHUwFPxxHVHBmlt1eNLwGIqeQdbMZXyyocWw4v7l89k9EHRDuWibPkm74403KBjMf2Fx0ed9AZskI5HtqB3bhuIIPwwJJSmRNNnbBEDeCmXu2sGsq3To271iAO2qxOd0_2TmpL_LElZnI8L8XfU7JlXkmpQ_VCUZpFX7ss5OfSdPJtgwzCj209-OnsILtfwDVCGOt-7BU-voyAmgB8uVew_Bc_4XJtZBaYSCuKZHnetL5Hmt0CUjewWgzc7fhYoheyK0xd3FO33NBzcZX-JOy6k8zMW1HeTBANy17bVrTzxCNv5uuHX09gG8EncInSABqwbumxIe0MFuESo48HrbYcD_3poD-fgbOWyD54be0QuriCLVe49hPYRdAFAKb3Za37fQXpLDgMecXbPo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک بالگرد رسانه‌ای تصاویری از بمب‌افکن‌های B-1B نیروی هوایی ایالات متحده ثبت کرده است که در محوطه‌های پارکینگ شرقی پایگاه نیروی هوایی سلطنتی بریتانیا در «فِیرفورد» (RAF Fairford) مستقر شده‌اند؛ این در حالی است که یگان‌های خنثی‌سازی بمب همچنان مشغول عملیات پاکسازی مهمات منفجرنشده در منطقه «وِل‌فورد» (Whelford) در مجاورت این پایگاه هوایی هستند.
این پایگاه برای ایالات متحده در جریان جنگ علیه ایران، نقشی حیاتی داشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/72364" target="_blank">📅 16:33 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72362">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUrP3xXxwNJ8NVejr-_uQUV7YA_wOcmAQjwoZqTTY8Ru2zQ6ruD2UU7OQhiAc-iGV1A_QgLeg5h2n4RzGHAlErT_FHWWGP3a9c-uIOcO2MlQUrzkRoeU8YJss8n3Eq2rxKSklbnzlbmkBj3hXXFpmr_3b6AfDEprjn7aIvZT-JTMC1yAeXZGBKmXSPBY-XOx9-cY_C9Uh6SsTXMMrKSED6EH6DbJASIq6W49pBnCDd8qFxNussjrZwRrlK5JKYgnGxIUspsa9FE4NodjrpOfXumQMD99juQAiIKV3d-hksTtQuZiFLQ0KzrrgsOHCo5IR8eS7iQESpTUFHNtmE8xMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a6bd02b6.mp4?token=UJhe5a0dFTgW5JSy_0_JdFhw4Wm1UkWh9k549Z0QHtFuPop1cafzdmzPwr3KrR3MoAJlbH91orenaZvRYJOFchELhOZoLHsD5oaILRpdvMl-gI2675EZNetfxDLuM4Sc9giT2clGdqFpmAyxxXW_sNJ-2Wd9Bl8xJ-RDL3HtJE2RnfaE0Nwp2QZapPi-x6xbB4vf4ctnG2Ieqli4Obh68UZvjnwy9pwJrMbjRzAibpqWfjy8FpJLleq5r1PZAHfSYSGEOZLSw_o7tZri8AfXX11XAobGC3i3dSEycZooet0hBRiWT8dHaozX8Evu0EyR2YyYzpQJ49clpeJ0FMaNVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a6bd02b6.mp4?token=UJhe5a0dFTgW5JSy_0_JdFhw4Wm1UkWh9k549Z0QHtFuPop1cafzdmzPwr3KrR3MoAJlbH91orenaZvRYJOFchELhOZoLHsD5oaILRpdvMl-gI2675EZNetfxDLuM4Sc9giT2clGdqFpmAyxxXW_sNJ-2Wd9Bl8xJ-RDL3HtJE2RnfaE0Nwp2QZapPi-x6xbB4vf4ctnG2Ieqli4Obh68UZvjnwy9pwJrMbjRzAibpqWfjy8FpJLleq5r1PZAHfSYSGEOZLSw_o7tZri8AfXX11XAobGC3i3dSEycZooet0hBRiWT8dHaozX8Evu0EyR2YyYzpQJ49clpeJ0FMaNVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی ارتش اسرائیل لحظاتی پیش منطقه «حداثا» در جنوب لبنان را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/72362" target="_blank">📅 15:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72361">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a85f2632d6.mp4?token=Gdkznlma7VIAgM-0R-UXK0B4pokgwxSF8CqVkSKpvVbjx0c6UW8gyUxNNUKYfOkfbloJb0ZdBxY8nSa34ZLAmzpKrV78WHtIoWuc23b0QRwd_fmI73G3tBT6bF8frYs92Vz4dfZ-wO2KZFYv6MlgKgi1sgG7vBTaYlSclioXOqDmbR_cGT6VcKIP1CmCIQWyVo3TLgsqlObWQ9jz5MGyaw5DwguzRz25aIQ4SfaHVYOt5rObNablzsqzCPbkzHkTV2pldlkyqIk5b53Pq6Ixv3hXkwsyNDpzvl6k1LjDq8gvw3ybqLoaQni6a-vgGWcnfOjb9021sLRl4WzL6t4E2ztN9JxZh0BMVrRaV-ySct7GIWB3tR25EIEvFyr4iqJ8BMfYVAuweEs0sPmhwwsrqLKT4xNtQ4wKt54DCsgyKbTSIsI42J5zFJTzw7wewDHUgrDxvG-zKxgqXGPi7-BE-Irq_Hgu05xbgRvmLO3uuaqA8HA115j2syM18zW18p8mzRJ6D3f-3FzKzqTVFoaOBqTf_ClQMVkRFQkPe_UNdSdeYYrTh4Y7xQCH3PcwiBonPLb7Doge-1viZu6wrQLNqubh39-o_Cw63XjLdrCzuXerQa8jdl7dHtDgNVTX0wbrxAm-rKSKXXycQygCyqJa-fejNCeeZW5iDrDi9smQIRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a85f2632d6.mp4?token=Gdkznlma7VIAgM-0R-UXK0B4pokgwxSF8CqVkSKpvVbjx0c6UW8gyUxNNUKYfOkfbloJb0ZdBxY8nSa34ZLAmzpKrV78WHtIoWuc23b0QRwd_fmI73G3tBT6bF8frYs92Vz4dfZ-wO2KZFYv6MlgKgi1sgG7vBTaYlSclioXOqDmbR_cGT6VcKIP1CmCIQWyVo3TLgsqlObWQ9jz5MGyaw5DwguzRz25aIQ4SfaHVYOt5rObNablzsqzCPbkzHkTV2pldlkyqIk5b53Pq6Ixv3hXkwsyNDpzvl6k1LjDq8gvw3ybqLoaQni6a-vgGWcnfOjb9021sLRl4WzL6t4E2ztN9JxZh0BMVrRaV-ySct7GIWB3tR25EIEvFyr4iqJ8BMfYVAuweEs0sPmhwwsrqLKT4xNtQ4wKt54DCsgyKbTSIsI42J5zFJTzw7wewDHUgrDxvG-zKxgqXGPi7-BE-Irq_Hgu05xbgRvmLO3uuaqA8HA115j2syM18zW18p8mzRJ6D3f-3FzKzqTVFoaOBqTf_ClQMVkRFQkPe_UNdSdeYYrTh4Y7xQCH3PcwiBonPLb7Doge-1viZu6wrQLNqubh39-o_Cw63XjLdrCzuXerQa8jdl7dHtDgNVTX0wbrxAm-rKSKXXycQygCyqJa-fejNCeeZW5iDrDi9smQIRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریه های یک خانم به خاطر شرایط اضطراری که واسش به وجود اومده و عدم وجود سرویس بهداشتی در مترو.
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/72361" target="_blank">📅 15:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72360">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">تمسخر پزشکیان در شبکه فاکس‌نیوز؛
در مصاحبه ای که با رئیس جمهور ایران پژاکیان(پزشکیان) کردیم همش جوابای مبهم و بی معنی میداد.
اصلا اون به هیچ سوالی جواب نداد.
حتی نتونست بگه رهبر رو دیده یا نه.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/72360" target="_blank">📅 14:58 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72358">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5drwvHb96D1QM08kgRJv1vrkvClFawy08Wm_7Q0Sqn85ycJrWmAv2w6hrVkE92ShWvODx3E5L5gAFgNWi_6b2dnxxRhOiv6unY0aSAdAH6KtQyDyyvh_asJqLI0mlaXqJl3SUoykx5LIRMdrH3HBpafZTrPU8SEbvZzCOp3Hw_YO2ZamxHNeYWItvQFr9tSihlbtRgQf6iiNhJOOBujhynELOp9smo2nX7jeU18lfoubpJZ9WqV2V8VuaYh87XQwPQHD5V6DKXgu-h1ly4DWkvuEkCE1LC57MJgrWXfhcGdPw2TOnE8Zq_0g-v_L6LGhpleokr8YSPBfhvmwThmQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2634d568.mp4?token=QH80-oaVdweEKZgkjms7r1v19SB_ojDeYtQZaora9PJiDy0GgP4egXpsElXlOtbv1V4y6z-v_i5Vfs9vSzeYCxHXqkmmleOLp34rn-NGV1HjKL8c-VUajp4qCacXjGUWYIhDwWvKIhxMwDLVkmy_iH2g7wKPLalF1pMzGFKRgy8wvHg19hf_jWhHC7EZpjCJqS8DW4x0HQS_sLJrgJzFv3PlBsVN03fktxhqtAjNAHnhD5XmN4NobttmoLZVfdLuyCNFTd9zNGs0yzhQjMt8LxdsSMzp37kaqMtDdohqLjw_-UGn2mSlbq0Ncrgn4q2dYPEuEmnDffoK1muR4D8jgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2634d568.mp4?token=QH80-oaVdweEKZgkjms7r1v19SB_ojDeYtQZaora9PJiDy0GgP4egXpsElXlOtbv1V4y6z-v_i5Vfs9vSzeYCxHXqkmmleOLp34rn-NGV1HjKL8c-VUajp4qCacXjGUWYIhDwWvKIhxMwDLVkmy_iH2g7wKPLalF1pMzGFKRgy8wvHg19hf_jWhHC7EZpjCJqS8DW4x0HQS_sLJrgJzFv3PlBsVN03fktxhqtAjNAHnhD5XmN4NobttmoLZVfdLuyCNFTd9zNGs0yzhQjMt8LxdsSMzp37kaqMtDdohqLjw_-UGn2mSlbq0Ncrgn4q2dYPEuEmnDffoK1muR4D8jgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی
سپاه پاسداران:دومین زهپاد(زیرسطحی )ارتش آمریکا در تنگه هرمز شکار شد.
شناور توقیف‌شده از نوع پیشرفته «Remus 600» است که به گفته سپاه، متعلق به «ارتش آمریکا» بوده و با اهداف جاسوسی فعالیت می‌کرده است.
این شناور طی یک عملیات هماهنگ و با بهره‌گیری از قابلیت‌های اطلاعاتی و جنگ الکترونیک توقیف شد و هم‌اکنون برای استخراج اطلاعات در اختیار کارشناسان سپاه قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/72358" target="_blank">📅 14:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72356">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4389424237.mp4?token=rHTBi-9mW_w9_au3Dv5aHDg7z8pGRjEfKwTwHjS8q2Cuprw9IduvFYfu9RzSz-rv3X_JYTNqeF9zBiqHIwE8rLaeJAaiaC2I7jk4Lciw4GxoPTCqoQikB87fFdfs8_-2hQ8sXdRy58VRb671TqOrLvagOOCRbz_95BJ-96O6tzarGd_BK3odX50-rU2zjKEJtoDZLBt_0LnM_peMg8KQ__BtCgvyn7tXzoxrFDyeZBbOk-NccUwCXv0ttTP3XcJxMI21Rxq1fNo0WG6Lzs333pWNjIWPG21kCRe6E8IJE647m_2bzp2t-1S5AyKvwcYsPRFoE8S9yOw-fNEDGX9RSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4389424237.mp4?token=rHTBi-9mW_w9_au3Dv5aHDg7z8pGRjEfKwTwHjS8q2Cuprw9IduvFYfu9RzSz-rv3X_JYTNqeF9zBiqHIwE8rLaeJAaiaC2I7jk4Lciw4GxoPTCqoQikB87fFdfs8_-2hQ8sXdRy58VRb671TqOrLvagOOCRbz_95BJ-96O6tzarGd_BK3odX50-rU2zjKEJtoDZLBt_0LnM_peMg8KQ__BtCgvyn7tXzoxrFDyeZBbOk-NccUwCXv0ttTP3XcJxMI21Rxq1fNo0WG6Lzs333pWNjIWPG21kCRe6E8IJE647m_2bzp2t-1S5AyKvwcYsPRFoE8S9yOw-fNEDGX9RSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو سال پیش در چنین روزی سید حسن نصرالله به همراه چند فرمانده ارشد حزب‌الله و سپاه پاسداران در حمله نیروی هوایی اسرائیل کشته شدند.
در آن عملیات ۸۳ بمب سنگرشکن ۲۰۰۰ پوندی به مقر فرماندهی زیرزمینی حزب‌الله در زیر یک شهرک ضاحیه بیروت اصابت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/72356" target="_blank">📅 13:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72355">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a6a80862.mp4?token=WEJ6kLNT4GsM4nJRUAQkIZlAqEeK3ZyHO1qHjmYB4AHXU7lX8gTxGP2mGhpkkOlRdGOxydfRMwqPBLeWCA0KGHvzM__yr4yb4Smt-ET4qiU1KStJvHhsME8K-Cub7z4Zoq2OguDL1Pji4xFM9DMDk_Wo9br-90Cx96GXnXSvDhJ5ph7l0rMZAn4Wdvyr2zEPZkUBuJmvdAQH1XgEuPtMd54CrTWmLNisH0WMggq4RwkFGzDEk9RbDZDGJdNnUHllE-bnuyue9DImVgtdQAAMo1kMwmZAgqTXGxlTrDiwBA7o89J5D-urM5vO85GAKRqEegW0kkqPvuHgQnuxhJABWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a6a80862.mp4?token=WEJ6kLNT4GsM4nJRUAQkIZlAqEeK3ZyHO1qHjmYB4AHXU7lX8gTxGP2mGhpkkOlRdGOxydfRMwqPBLeWCA0KGHvzM__yr4yb4Smt-ET4qiU1KStJvHhsME8K-Cub7z4Zoq2OguDL1Pji4xFM9DMDk_Wo9br-90Cx96GXnXSvDhJ5ph7l0rMZAn4Wdvyr2zEPZkUBuJmvdAQH1XgEuPtMd54CrTWmLNisH0WMggq4RwkFGzDEk9RbDZDGJdNnUHllE-bnuyue9DImVgtdQAAMo1kMwmZAgqTXGxlTrDiwBA7o89J5D-urM5vO85GAKRqEegW0kkqPvuHgQnuxhJABWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابطحی میگه: سال ۸۸ توی زندان گفتند اعتراف کن که خاتمی به اسرائیل سفر کرده
گفتم خب سفر نکرده
گفتند اگر بگویی که به اسرائیل سفر کرده، آینده دینی ایران را ایمن نگه می‌داریم...!
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/72355" target="_blank">📅 13:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72354">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0MVEqbsQHYwUh8feNtqvnpctw4HEmkhmObseyhu4PbTUAV536J_cu5S5Iic-E0e-wIcmzNfK8NGv6zaNXD8eR5QY1ITv3H8KmJ_I5BcJeAOFanPONoWLAavoH6at2zpJqAeyczjpyVw9DAoxt2zWzfIgckT6gV4CcVCdighesgvbQAcIs7nJcmPB_5ktNfy7R-Z56ynJieHwWaJVc3bjK5wUa-fr_-dPmQ8L-lCqt42XGxAQRqTTlmMDUTzkFT3AGip3UC4Lcm2nT_l9k0bPdTEi3N_BedGaIzi6ViXNojvg5eG6VNdTB72t11yAIRlspvknP5ZAGrV4a7IvKnEZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت وزیر خزانه‌داری آمریکا:
در پی آغاز «عملیات طرد اقتصادی» (Operation Economic Outcast)، وزارت خزانه‌داری ایالات متحده اقدامات مالی هدفمندی را علیه بانک‌ها و شرکت‌های ارائه‌دهنده خدمات هوانوردی اعمال کرد. به دستور من، تیم‌هایی به سراسر جهان اعزام شدند تا با کشورها رایزنی کرده و خواستار اقدام علیه رژیم ایران شوند.
این تلاش‌ها در حال به ثمر نشستن است. ترکیه و عمان از توقف پروازهای «هواپیمایی ماهان» به کشورهای خود خبر دادند. امارات متحده عربی نیز تمامی پروازهای شرکت‌های هواپیمایی ایرانی را متوقف کرده و بانک‌های تجاری بزرگ در امارات و ترکیه، انجام هرگونه تراکنش مالی با ایران را متوقف ساخته‌اند.
حتی رهبران ایران نیز به پیامدهای اقتصادی این وضعیت اذعان کرده‌اند، چرا که ارزش ریال به پایین‌ترین حد تاریخی خود سقوط کرده است.
من از دولت‌های بریتانیا، ترکیه، عمان و امارات متحده عربی قدردانی می‌کنم. ما به همکاری‌های خود ادامه خواهیم داد، زیرا برای جلوگیری از پیشبرد دستورکار تروریستی تهران، هنوز کارهای بیشتری باید انجام شود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/72354" target="_blank">📅 12:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72353">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72353" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/72353" target="_blank">📅 12:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72352">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gU0VZm32LytR-9VdbnVfjOQag9y37IDTkq8b0yQ1jJVpVWP_1Zi8_S7ISuO8ZD81DjF_1Y9d8aLJZPI_OREfdqS2FXGdmWf131gpy-Cu7z9H_-mBrDYxmOtOCmkWa9f5BbsZCZSWSNN7kjIoYf5tTWEMHTJeNk4hn6Sym8kNmAi4PVpRct0VR8zyNZJd4xOGmvjFqz7WLhPMNyDci0tmASpenRYza8tfoaAzeE38MFHKyXU9V4zGDzGDr-fkizZ0Rm44ifX1RPIjT68lV2R5bK2Bv0r3xer95v69EOaLPl3i6dY9W3NoNb97pHuszIHsbAo-YDsFAVIyhCHV1ThKhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز
پرتغال
🆚
نروژ
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
پرتغال: ۳ برد، ۱ تساوی، ۱ شکست و ۸ گل زده
نروژ: ۳ برد، ۲ شکست و ۹ کل زده
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
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/72352" target="_blank">📅 12:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72351">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">مدارس ریاض به دستور مقامات سعودی و بدون اعلام دلیل رسمی، به مدت یک هفته به آموزش از راه دور روی آورده‌اند.
این تصمیم یک روز پس از آن اتخاذ شد که پدافند هوایی عربستان دو پهپاد حوثی را که ریاض را هدف قرار داده بودند، رهگیری و منهدم کرد؛ اقدامی که در بحبوحه تشدید حملات حوثی‌ها به این پادشاهی صورت گرفت.
در دو پیام جداگانه که خبرگزاری فرانسه (AFP) آن‌ها را مشاهده کرده، آمده است: «به‌تازگی از سوی مقامات سعودی مطلع شدیم که مدارس باید در تمام طول هفته تعطیل بمانند.»
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/72351" target="_blank">📅 11:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72348">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RZrtOzKYm_4K7WQq62q51cFnoJLNt5DS074Dl56AkjF9JWjxDfAUSFvDoP9b56N9dsPgolnr0_ZG_A5McrEMssk1KXdsSXRGk5ab3lpulnS0CmtPwE3xhKSo_VKd0udgfp63gL1Uymxv4m7FiD222EKE_ih5QYfD15pCO6yctJTWYpJzA_-M9p2R3Dtcy369V9XDFI4pbB2TN6wu0F7UFZorDAQDZgeFAj4KFpoVCYX93g9C-zb7JHCUM8_5Ywp5VO1lbol7ZbnxbZ7mCs8lZIIWXJSUlgmZoF8xGmHXkqHGwVLqzTm73Zeq3__d1Xu2i5Pm29UeH18k-1fqitcO3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iGSFprswkExyMNB-6HDws1EYiBrFQ_76nTiUHzvzbRUuHU2ByRMpqN4nQDdsduc5e_YdXvNLdJ0Dok7RRRINXoVxqb0qIpt3VEHv8ccgf8viH3EliC6Lh3oBgWtIPdKXNOHETo46IHYZFGJ7gtRvDG_X7wD9sV_RYp7VetLXk5tCf1vwzCMvR5YVey5hTHKelJlc1OCuJG9uP83BtDO6v0ePkgYrOfe4f1dFp8IZ1vAp9GBYE9IekC72cSfazLxK8SMcWxSt_R412JzZ9fLfi5JxsjBbEd5fPmbNsnxb_U3yrbMcwU-BJhBrdWWoRW5CLY_BKCHkA__uAHEn7ndo8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rILzzjUkYxdodvTn0-dSJ0IsbOnFSiqQRRiLAC91U7WcWqA36sPiggIzkrXiLufLBBq_8RDSIjfqTs0T4LNeaSIjT4__ew1E6i0FSQY_QVh879mWYy0fqwauw4nr0Ox0v09S-DJ_AP5oMnp-a21dleHQmLlQ46xInmbjZ5x9mt7e_lYi9GyP-KAO5PJmIpCCOnS-cUifOP6Ic7hURDNitcCWKBh4IDz-NFFKfcVuRpAZcLIvUDM-1ToA5N8KenbKv8B2smxlaRN6aazVE6i6AMPPwhnHWh2X2cCJgPRa5sfxI6kklp6mF3BHGyeVnR8Bu309tIgeQ6MzrVElY3csOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رژیم جمهوری اسلامی که خودش فرودگاه نجف را ساخته بود و هزینه‌ی آن را تقبل کرده بود، از استفاده از این فرودگاه محروم شد!
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72348" target="_blank">📅 11:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72347">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7c28b66c8.mp4?token=nCuRLGRKlQ5OFkA2ayNaEw9VBak4qoB5cJvafw8y5JU-tJoxqfO3Yx8kt-9x7K3DjuPqe5g4C_IZSMUa8Q0uwXfHuWdhyZOgVg8P-4wOWEYHP7_WaCLEq0cFf-gqm2W1Joo3uuoy7SpMcvv9Jvduq8NA_LKlXgUd3VLcC1E3KRO5-2AZa55WQ1CUfu87N9wG5bElSmJGVmnUGm43atLf7WyzW8YUvB7iY3511rGffolIJJQM4l37GiQeHXjjOvFfKLHHCEBYjVy4M8xTt3kP9IyHvc8kj57QH-BTMqddlgrpFMw9EWVf_PetR8FuX1sHTq1mHy3SclQAgZP9iCTCTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7c28b66c8.mp4?token=nCuRLGRKlQ5OFkA2ayNaEw9VBak4qoB5cJvafw8y5JU-tJoxqfO3Yx8kt-9x7K3DjuPqe5g4C_IZSMUa8Q0uwXfHuWdhyZOgVg8P-4wOWEYHP7_WaCLEq0cFf-gqm2W1Joo3uuoy7SpMcvv9Jvduq8NA_LKlXgUd3VLcC1E3KRO5-2AZa55WQ1CUfu87N9wG5bElSmJGVmnUGm43atLf7WyzW8YUvB7iY3511rGffolIJJQM4l37GiQeHXjjOvFfKLHHCEBYjVy4M8xTt3kP9IyHvc8kj57QH-BTMqddlgrpFMw9EWVf_PetR8FuX1sHTq1mHy3SclQAgZP9iCTCTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌سخنگوی ارشد نیروهای مسلح ج ا :
آمریکایی‌ها باید خواب این را ببینند که در مدیریت تنگهٔ هرمز دخالت کنند و در صورت دخالت سیلی از نیروهای مسلح ایران خواهند خورد؛ آن‌ها باید از منطقهٔ ما بروند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72347" target="_blank">📅 11:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72346">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/58f2375d54.mp4?token=TFAQ5-qjul784a7IK3utRH2ie51u6m6giZGDF0j8XbrNgoh1pPz2xgZdkqb3q-aSqrGuMgnmW6b37MtyULVTHrk8Nov-nMX1rz_RSLPJl9Q-Svaer6BxY5JRh7WT399-nbSZEPivAc7sg8qVjJVcdFLI5irWJJSnoScdK9e8NlSEdN7hyuKa9foMQ9220EuRzpOWKh5DPIx3IaP5lnOxuo4WDT3lv1JuI8cpZiUxIzp69-YaBzMOHezHlaYPbZNwSSWAjY2_SKa_yY6FeyPfprio1_0_ySdAlQpHyIbSwvJBzy5jm-6pqfFIcdYVoMHC_OlL6fAZtj7Nf7kjol-nWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/58f2375d54.mp4?token=TFAQ5-qjul784a7IK3utRH2ie51u6m6giZGDF0j8XbrNgoh1pPz2xgZdkqb3q-aSqrGuMgnmW6b37MtyULVTHrk8Nov-nMX1rz_RSLPJl9Q-Svaer6BxY5JRh7WT399-nbSZEPivAc7sg8qVjJVcdFLI5irWJJSnoScdK9e8NlSEdN7hyuKa9foMQ9220EuRzpOWKh5DPIx3IaP5lnOxuo4WDT3lv1JuI8cpZiUxIzp69-YaBzMOHezHlaYPbZNwSSWAjY2_SKa_yY6FeyPfprio1_0_ySdAlQpHyIbSwvJBzy5jm-6pqfFIcdYVoMHC_OlL6fAZtj7Nf7kjol-nWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبتای ایشون در مورد مظلومیت پسرا، بیشترین لایک ۲۴ ساعت اخیر رو داشته:
پسرا از یه جایی به بعد، از بس کار دارن و به فکر آینده‌ان، حتی یادشون نمیاد که کِی تولدشونه!
ولی همینکه یکی باشه و بهشون بگه تو چقدر برام مهم و با ارزشی، اندازه هزاران کادوی میلیاردی براشون ارزش داره!
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72346" target="_blank">📅 10:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72345">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2CGP0CT_ZgnJAuY68Bf6DpfJLDFyr0Hlq63FAlV8Y9YqCZXaTy313PZdOx3v7JDZurjaPi-vVqMUS3bLv22arBDOMFLxhFC3yj1l3EBAHMMH4FbJ9qFTUnKF1DdWa5n9m8GVHRqyugwZQF43m5hl_dZBy8kgWxzAkjTeEad6blQjdZsxHg3ec8m6hzQEZpap5VA0bnGbRolYX1yKCzRaW3T5yp3XkEHC36at0YHauQNmTgeCn_anfk40AGs6ho14Je_2vAH-xvnTeQqspgVNatE-pZUBgMeFJ4PPwZZxH_wtrNRvGRmzv9KVRps9o6INZM3lBnl6vtOGqrNmpMIMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی ارشد نیروهای مسلح جمهوری اسلامی :
قدرتمندترین ارتش جهان مقابل نیروهای مسلح ایران زانو زد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72345" target="_blank">📅 10:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72344">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c277f60d17.mp4?token=jJEn12rOqdLjNUceTRz7sJMA9tFQ5fs8C2AjvzMkIMPA-ix7tN5JgkgbBj20dtI5Z2rivoPtMyWnuU1kTaF3HCLDWf832O03fNYDBT_ygzapo35oKR1Y0S1-YO-Ngqll4OGzncIVUQLNx0BdPwkMdpWpaAUIaTQXSU7iiIMHLcjbE4LYQ-zAZzfknaVxhWBdB7bPDIRRMwq4_0GD0tbaTinBk3MQUwSi6fxdLvyEKT2z7HvWXUSuqjevT1XTtyP_Y31gTLC5M9LpF97eeOYanOdy-YLa04owf7exOPCGyB9bGM_PYocFJDrqUtjTHhce_FBrsQfGJM1lunaniF6ezA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c277f60d17.mp4?token=jJEn12rOqdLjNUceTRz7sJMA9tFQ5fs8C2AjvzMkIMPA-ix7tN5JgkgbBj20dtI5Z2rivoPtMyWnuU1kTaF3HCLDWf832O03fNYDBT_ygzapo35oKR1Y0S1-YO-Ngqll4OGzncIVUQLNx0BdPwkMdpWpaAUIaTQXSU7iiIMHLcjbE4LYQ-zAZzfknaVxhWBdB7bPDIRRMwq4_0GD0tbaTinBk3MQUwSi6fxdLvyEKT2z7HvWXUSuqjevT1XTtyP_Y31gTLC5M9LpF97eeOYanOdy-YLa04owf7exOPCGyB9bGM_PYocFJDrqUtjTHhce_FBrsQfGJM1lunaniF6ezA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آقای سفیر، پیام دولت آمریکا به مردم ایران چیه؟؟
سفیر آمریکا در سازمان ملل: این رژیم تروریستی باید بره راهی دیگه نیست
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72344" target="_blank">📅 09:30 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72343">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YjjRho10B0MqJnfCEJwI9LaxBK4_7jiEWhx9hNjw2Uk80gFHNzZHq-somvoQubUtF7m58LsKmhTJcfq1m6bAUPVaMXGT88JptMwMF7H9tIVgP7gTlQRouLTEsIcFgx8-gYSbMqmTZG79MXN7MCy0epf-qBAQFcNXsbXswLEC0nvph5JDFkOCH41ZEnJheUe2cqg1mfN4Vu7euoHcQkqLl247RP-1FG_JqVFT4x2bio_rqtRd-pTSZcw6eu0F8qqSsi8rTBto7ocSKOGnBN2X37tG9_stlEW3RR6w84tpCB6IMjKQ1WGsK7mi46v6zwpsmM1vAMFvxewho87SDnekMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش وال‌استریت ژورنال، دولت ترامپ فشار اقتصادی خود را بر ایران افزایش داده و از کشورها در سراسر خاورمیانه و اروپا می‌خواهد تا روابط هوایی و بانکی خود را با تهران قطع کنند.
جاناتان برک، مسئول ارشد وزارت خزانه‌داری آمریکا، این ماه از چندین کشور بازدید کرد و به شرکای تجاری ایران هشدار داد که باید بین انجام تجارت با تهران یا واشنگتن یکی را انتخاب کنند.
در پی این کمپین دیپلماتیک، عمان، امارات متحده عربی و ترکیه، پروازهای ایران را محدود کردند، در حالی که مقامات امارات، تراکنش‌های مرتبط با ایران را توسط بانک ملی مسدود کردند و ترکیه، مجوز فعالیت بانک ملت را لغو کرد.
آذربایجان و گرجستان نیز پروازهای شرکت‌های هواپیمایی ایران را محدود کرده‌اند، در حالی که بریتانیا قصد دارد معافیت‌های بانکی را که به موسسات مالی ایران اجازه فعالیت در لندن را داده بود، لغو کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72343" target="_blank">📅 09:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72342">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72342" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72342" target="_blank">📅 01:52 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72341">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rj56Cw4WBmRUjaS7kYngHQHCHc-ezC2RnsdlsU3AxsMCgc40kGOjnAeNqFF5SjSfGYelIytQY-2EeCB-a5L_ts6KcWNQylABb6jjTebMF-9ifJQ7wtFcHlQPlNp0pXwBEaoY6FpjJn8AL6rkrXM2K3R1hcW3ccjzjAeznnerOAtFBsXtXzYVyP9b1dkEDl6Ie0VDF1IEbL9IC1ggI1HmM1t2yaqBRx_zwWvY7hob-hOMfLksUKe3MZt7s6SZ__80TZ5UpFsG47YDqY9EZpU_PrAEgMkIh3MWqxSBnwyf2iu8kALJzr8kyGcDuScYgB3rSYlRljn1G3Fj4HAz2cO00w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72341" target="_blank">📅 01:52 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72340">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">انفجار های جدید در تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72340" target="_blank">📅 01:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72339">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سپاه پاسداران:توی جنگ بعدی ناوها و ناوشکن‌های دشمن حتی توی اقیانوس هند هم امنیت نداره و قطعا هدف قرارشون میدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72339" target="_blank">📅 01:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72338">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ ویدئویی منتشر کرده که در پایان اون بخشی از سخنرانیش در زمان آغاز حملات مشترک آمریکا و اسرائیل به جمهوری اسلامی آورده شده که میگه</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72338" target="_blank">📅 00:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72336">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ایلیا هاشمی:
ساعت در محدوده ۰۰:۱۵ الی ۰۰:۴۰ بامداد یکشنبه، چندین انفجار مهیب همراه با لرزش در محدوده تنگه هرمز شنیده شد.
تحرکات نظامیِ سواحل جنوبی هرمزگان در کنار تعداد و شدت انفجارهای امشب، نسبت به دو ماهه اخیر بی‌سابقه است و می‌تواند گسترده‌تر شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72336" target="_blank">📅 00:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72335">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">شنیده شدن صدای چند انفجار در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72335" target="_blank">📅 00:41 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72334">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">عراقچی رفته نیویورک گفته اگه این هفت تا کارو بکنید تنگه رو باز می‌کنیم، اونام گفتن مرتیکه جاکش تنگه که دست خودمونه پس صیکتیر کن تا پیشنهاد بعدی
و این شد پایان این دوره از مذاکرات:
#hjAly‌</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/72334" target="_blank">📅 00:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72333">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b153f7fb8.mp4?token=h6DqJw5S4L1lA9fG_8IQnSsmFdbMrXjY1jcAubeRdf_mzeVUbfcINYmZ77jw5QPaqME0OJJgFddqX8Uw-RPoT-nhdU0QGtrlIiWv99PCaGC-DH6q_J6XkiO3TbGn6nidMj8K-U7weafj5fQLoLw2N8kbJGZXK0-dTE4m6Y2ULmCT58CmrkLXVw95cpbkTdNgIr5q7GHQviWuIWzNxlN39bT3QzdbcLcdBhrd7YNeHQ89Z8KJ7De_KCJtZJHoNxtp4bp8wzkrSDOfwhQyqYZ3mj0-f99ohQHlcb6EwfNDJ7LQnRuvnB-_S6NIpEGx3_kS9cSFXqWtQs-SZbfB3NUl_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b153f7fb8.mp4?token=h6DqJw5S4L1lA9fG_8IQnSsmFdbMrXjY1jcAubeRdf_mzeVUbfcINYmZ77jw5QPaqME0OJJgFddqX8Uw-RPoT-nhdU0QGtrlIiWv99PCaGC-DH6q_J6XkiO3TbGn6nidMj8K-U7weafj5fQLoLw2N8kbJGZXK0-dTE4m6Y2ULmCT58CmrkLXVw95cpbkTdNgIr5q7GHQviWuIWzNxlN39bT3QzdbcLcdBhrd7YNeHQ89Z8KJ7De_KCJtZJHoNxtp4bp8wzkrSDOfwhQyqYZ3mj0-f99ohQHlcb6EwfNDJ7LQnRuvnB-_S6NIpEGx3_kS9cSFXqWtQs-SZbfB3NUl_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پریشب تو تهرانپارس، یه خانواده برای مریض بدحالشون با 115 تماس گرفتن تا آمبولانس بیاد و ببرتش بیمارستان؛
ولی از اونجایی که خودِ آمبولانس خراب شد، همراه‌هایِ مریض مجبور شدن تا نزدیکی‌های بیمارستان هُلش بدن:
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/72333" target="_blank">📅 23:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72332">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e49705c5.mp4?token=GpojuarLDbzjglRA1S8mZ-u3txJzhgf27zdmep3hUjvTFEPwcpXAQoHzsDO-qYq_LVLn43KixUxev3hwoeYobQ2gMt3gFGLbKLpGMaAWhCcCtw-3veTAy-5eIay5ZmtHVaIgvdBI9iqugib6Cj8-UozmrEkVfLXMD9NWwFxvJzBx5M4owZHUhMEADdsfAnTPaK_iO4Zx7JLnrrUB1SlA-Orrw2orld9RWKYwIdsEhKATe6hKNfpXi18fmDheLaDGIRa8X9lp_N240Ihtpnd5QBbRVPYItCOw6NSNcITXyFx7IDYNT5MyrGp-kOQwHchoBBkNpuqDx24tbiW6JH9eXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e49705c5.mp4?token=GpojuarLDbzjglRA1S8mZ-u3txJzhgf27zdmep3hUjvTFEPwcpXAQoHzsDO-qYq_LVLn43KixUxev3hwoeYobQ2gMt3gFGLbKLpGMaAWhCcCtw-3veTAy-5eIay5ZmtHVaIgvdBI9iqugib6Cj8-UozmrEkVfLXMD9NWwFxvJzBx5M4owZHUhMEADdsfAnTPaK_iO4Zx7JLnrrUB1SlA-Orrw2orld9RWKYwIdsEhKATe6hKNfpXi18fmDheLaDGIRa8X9lp_N240Ihtpnd5QBbRVPYItCOw6NSNcITXyFx7IDYNT5MyrGp-kOQwHchoBBkNpuqDx24tbiW6JH9eXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز داخل تهران اولین مرکز آموزش نظامی برای جان‌فداها افتتاح شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/72332" target="_blank">📅 22:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72331">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff29e8be2f.mp4?token=EZvlR6QcpRabU9ImOUTdvhfaSwQpwfp27ZgfQterbhJfLEKQyEUdOAbYS96MSkubn3U310MkV5Uh1aO3H81yCnMdRm7AT0k2fAx4aAtFS0d4p_Ir1yDiueasssSAda-kKVyo0yHy-WZAPKtYfKl4C9bDIMKsQtpxKDQqXDfaGKaqXuybJa3NXLEZq8yRrMnNeesLwjhpQxhAyP8qcJoXldylx6ZD3Jv7epO6l623datd1ZD_j13azUDKLpHxHFMuaUV-zCA55tg8PDVdUBcUUM2ZFwROCpTCFXmX_XRUdErMdlepUlqM9RExEmSFAEyWKCyz7LiQNOy_pocA1qa_rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff29e8be2f.mp4?token=EZvlR6QcpRabU9ImOUTdvhfaSwQpwfp27ZgfQterbhJfLEKQyEUdOAbYS96MSkubn3U310MkV5Uh1aO3H81yCnMdRm7AT0k2fAx4aAtFS0d4p_Ir1yDiueasssSAda-kKVyo0yHy-WZAPKtYfKl4C9bDIMKsQtpxKDQqXDfaGKaqXuybJa3NXLEZq8yRrMnNeesLwjhpQxhAyP8qcJoXldylx6ZD3Jv7epO6l623datd1ZD_j13azUDKLpHxHFMuaUV-zCA55tg8PDVdUBcUUM2ZFwROCpTCFXmX_XRUdErMdlepUlqM9RExEmSFAEyWKCyz7LiQNOy_pocA1qa_rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرازیر شدن موج جدید افغان ها از کوه‌های صعب‌العبور به سوی خاک ایران
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/72331" target="_blank">📅 21:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72328">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIu4IQpkRN4fgqT-hlY3Mje_rBHuqbz1CtcG1HQdwaQsaX3SHNxjUZuSGAalk78Xf-2MBKkzNxJAHlZRnecgb541ZHgjsd4ifcChpqqsJ3bMIHodXN42Q3-kCUQLEddO8yOxIwXNa3JJu4Sus84zfOVqOaoCi_Gdc5sTrq4TvXKIUtN6VLwkRoI4VY8MNsBjxTULpzcrxWmmN_xWGIPkyYSHFk2IW0eE_IPHBeOCssRCVP2w4ibEFKKssIB1BOSwXX6JafFUhZunEDUIMfznh73RonerMi__-420hMLhaz6ZcoDiYlOQddHDjhNxgjhpwj6xh5rcPIYV3XlE9WpFaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7fb8f6948.mp4?token=Fcr_V_1bMg-Ye3PJp980QqhkvR5klKmtCODD0sCplobeXtUX8gW5ZGZ3xmFubQNs5r5maBV0BXu9IPDDqXibHKck4ObnbkG4749CX_8JKVXBCUhRAIJFv6U-zA7IHmQYxN-iBCTfbUfZ5IQDxMFiU-sCn1RYqpD1R5sOPPlImelUCmEiAmI0jqGGcBQAfCpBWkOp2n_f1QCBFGZXIx0g7fZ_JY0WWlgMRWcmiX-K2uYNXHS1mN1UQ2z44u0xXIaPTLNZgRD1Cr3dQbqS2S98yJ6Cdwi0kntnBB6pNVDuiu37oIB0s4hYzkAzSLkkUE0QOuMiPqi41uY3fhC22_QFtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7fb8f6948.mp4?token=Fcr_V_1bMg-Ye3PJp980QqhkvR5klKmtCODD0sCplobeXtUX8gW5ZGZ3xmFubQNs5r5maBV0BXu9IPDDqXibHKck4ObnbkG4749CX_8JKVXBCUhRAIJFv6U-zA7IHmQYxN-iBCTfbUfZ5IQDxMFiU-sCn1RYqpD1R5sOPPlImelUCmEiAmI0jqGGcBQAfCpBWkOp2n_f1QCBFGZXIx0g7fZ_JY0WWlgMRWcmiX-K2uYNXHS1mN1UQ2z44u0xXIaPTLNZgRD1Cr3dQbqS2S98yJ6Cdwi0kntnBB6pNVDuiu37oIB0s4hYzkAzSLkkUE0QOuMiPqi41uY3fhC22_QFtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر ۱۸ ساله یه مدت به خونه صمیمی‌ترین دوستش که مامان باباش طلاق گرفته بودن، رفت و آمد داشته.
بعد از یه مدت، دختره رو بابای دوستش که ۴۷ سالش بوده کراش میزنه و مخِ بابای صمیمی‌ترین دوستشو میزنه تا باهم ازدواج کنن!
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72328" target="_blank">📅 20:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72327">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77bb2e5af4.mp4?token=IoFsmlXSOaxjKA9KsYSiSKzK54x5GwVI914VPi2dV5FNvU3rWFYVbLA_OYJ2BX3efZ3QAPu3nzfWXiiySxOAwRGZH59NEX0r2vf0rQ_9oHtYrdAMwf4VJoGwYJQkd4oR88iW23R-DqDaPKgJ3spdgQPLc7MUPVq84fgpJg1PyQyUdA127jZKnIlu-iagk7uEX4uC8SuyXCag-VOsqfDhR8nJrlYxlHMAGQhAzsthhqiR94MyiT6LC3jftklLi_5_Mh-BPcQaIukiSetXamrdLirfE3XgPzkDKe1T9eS-RaqOf_zR26XRGX1zodavVK7vqcmBd3gM9AcDYQLcMZhRXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77bb2e5af4.mp4?token=IoFsmlXSOaxjKA9KsYSiSKzK54x5GwVI914VPi2dV5FNvU3rWFYVbLA_OYJ2BX3efZ3QAPu3nzfWXiiySxOAwRGZH59NEX0r2vf0rQ_9oHtYrdAMwf4VJoGwYJQkd4oR88iW23R-DqDaPKgJ3spdgQPLc7MUPVq84fgpJg1PyQyUdA127jZKnIlu-iagk7uEX4uC8SuyXCag-VOsqfDhR8nJrlYxlHMAGQhAzsthhqiR94MyiT6LC3jftklLi_5_Mh-BPcQaIukiSetXamrdLirfE3XgPzkDKe1T9eS-RaqOf_zR26XRGX1zodavVK7vqcmBd3gM9AcDYQLcMZhRXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از یه مینی رپر کوچولو و زیبا
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72327" target="_blank">📅 20:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72326">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✅
چرا باید عضو کانال ما باشی؟
🔹
تحلیل‌های روزانه و اختصاصی بازی‌های مهم
🔹
پیشنهادهای ویژه با وین‌ریت بالا
🔹
استراتژی‌های مدیریت سرمایه برای جلوگیری از ضرر
🔹
پشتیبانی و پاسخگویی سریع در گروه VIP همین حالا به جمع حرفه‌ای‌ها بپیوند و پیش از هر بازی، استراتژی…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72326" target="_blank">📅 20:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72325">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQlEPmlWW4lceqmuu6JafKHt1BydmU73x7a6ugzZmbYv5BXQefdasN1gUBX0OUGHW-o54URvtD5wRcxz4Gh7r5XKVNpVKOJmjdyJ7yIRyPMu1fxgVzJ1sw8L7A7xm7kG2tb00iUikrCT3TnO2FyOFywfwjcFv29n9zvHjNi6TxsrKQ4Kg1CyBdu8a9xJxZGEfdIozZzOYGu48gtZqT5-ru0dC2gUCTZv3WZ_mLUTMXV_a-cO5nEnz5fTom3h8p1_GBuaipFCXv5Fj7E4ucL2UYcZIXPmZGnrpsq5OgVn0gKvpOGfNHwg4hr-TcGRNQrFTZTjnENUJNX_K_0kYjfe2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا باید عضو کانال ما باشی؟
🔹
تحلیل‌های روزانه و اختصاصی بازی‌های مهم
🔹
پیشنهادهای ویژه با وین‌ریت بالا
🔹
استراتژی‌های مدیریت سرمایه برای جلوگیری از ضرر
🔹
پشتیبانی و پاسخگویی سریع در گروه VIP
همین حالا به جمع حرفه‌ای‌ها بپیوند و پیش از هر بازی، استراتژی برنده رو از ما بگیر!
🚀
همین حالا به جمع حرفه‌ای‌ها ملحق شو:
📢
ورود به کانال اصلی (آنالیزها و فرم‌های روزانه):
🔗
اینجا کلیک کنید و عضو کانال شوید
💬
ورود به سوپرگروه (چت و تبادل نظر کاربران):
🔗
اینجا کلیک کنید و به گروه بپیوندید</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72325" target="_blank">📅 20:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72324">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">طبق گزارش های تایید نشده، عباس عراقچی بازگشتش به ایران تاخیر افتاده و قراره سه‌شنبه ۷ مهر ۱۴۰۵ (۲۹ سپتامبر ۲۰۲۶) از نیویورک به تهران برگرده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72324" target="_blank">📅 20:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72323">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9470296462.mp4?token=lWJHFxw8a6SIzj28mJvsA1qO7oz7iVNnC0aZ4LGCtEJZk4wH7FyWyFmDwywfl23zsoaPCwLzaesNdPoIPjPdPN8-M6Q8f-Cy3uu5PaPX4eDLDC_4DMzQjIt432z0kUoQZAklDpl8lV6lVtKqn0_9ukFVTdamq80aBWTQ1fqQUcAUr51qdg00SHC4tKzwoWk4NIm8XRx8QGeh_1aKukh_mW9oscK1EVZ6XZxx8UY82O7M_QKUzWDNjnrthk7T3taq-qaZvXiVdBMgyTQKpwGDSIJW381oNVoBGVerGuSC9PcgZSydWUZmzXdsGp2Vck4DoVc6WNxxJlk3OIqO6JFNUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9470296462.mp4?token=lWJHFxw8a6SIzj28mJvsA1qO7oz7iVNnC0aZ4LGCtEJZk4wH7FyWyFmDwywfl23zsoaPCwLzaesNdPoIPjPdPN8-M6Q8f-Cy3uu5PaPX4eDLDC_4DMzQjIt432z0kUoQZAklDpl8lV6lVtKqn0_9ukFVTdamq80aBWTQ1fqQUcAUr51qdg00SHC4tKzwoWk4NIm8XRx8QGeh_1aKukh_mW9oscK1EVZ6XZxx8UY82O7M_QKUzWDNjnrthk7T3taq-qaZvXiVdBMgyTQKpwGDSIJW381oNVoBGVerGuSC9PcgZSydWUZmzXdsGp2Vck4DoVc6WNxxJlk3OIqO6JFNUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجمع عده‌ای در فرودگاه مهرآباد و شعار علیه پزشکیان و عراقچی
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72323" target="_blank">📅 20:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72322">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f33229cec0.mp4?token=XS2SwalsjKB2pV1gJUpkQkNR8TaWiGXbGN7r2hYACnXDkm_XpDKWWFSNf8Mu4GYwvL-qZJQjTdstGvgA4e9xMbPt3ASs5D1RgkzdaxuEAYZHrzSTgUBQ5YP-dy8F5W-JIfpVzIoGhZ6NDcgaMad3zumzahn0zLJfT9Z3ww34-aFneqtVbdVwjS5BHXlN1zvM5G_WY4c8n9wc-SVf_Zf7MQQPiSyzsblpGvHDJ9pd_eDAZFBslxNYiwG3JYKrP1-4LsoscVZYqgg9Alo-B2LguOSkrdkcxYIzC0PTZVrSY-dCrxUNd-UOZMsrvUV01Z2ZrsDUbh2d4FRijzM5_-g99g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f33229cec0.mp4?token=XS2SwalsjKB2pV1gJUpkQkNR8TaWiGXbGN7r2hYACnXDkm_XpDKWWFSNf8Mu4GYwvL-qZJQjTdstGvgA4e9xMbPt3ASs5D1RgkzdaxuEAYZHrzSTgUBQ5YP-dy8F5W-JIfpVzIoGhZ6NDcgaMad3zumzahn0zLJfT9Z3ww34-aFneqtVbdVwjS5BHXlN1zvM5G_WY4c8n9wc-SVf_Zf7MQQPiSyzsblpGvHDJ9pd_eDAZFBslxNYiwG3JYKrP1-4LsoscVZYqgg9Alo-B2LguOSkrdkcxYIzC0PTZVrSY-dCrxUNd-UOZMsrvUV01Z2ZrsDUbh2d4FRijzM5_-g99g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ از پاسخ دادن به سوال خبرنگار درباره زمان آغاز جنگ خودداری کرد.
خبرنگار:
آیا پس از انتخابات میان‌دوره‌ای به ایران حمله خواهید کرد؟
ترامپ:
من توافق آن‌ها را رد می‌کنم. آن‌ها می‌خواهند توافقی کنند که در آن بلافاصله تنگه را باز کنند، چون دارند به‌شدت متحمل شکست می‌شوند.
آن‌ها خواهان توافق هستند و به نظر من این اشکالی ندارد. من هم از توافق کردن استقبال می‌کنم، اما آن توافق [مدنظر آن‌ها] قابل‌قبول نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72322" target="_blank">📅 19:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72321">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GvTFfuZhqUzVllkqk73Z9BxW_0r4zBv0ka_rmLbet2buffwJssUW3TsdAINIk3F29ZO8COFiZ0_oW7IYt4CVKPIetlJg7PYOk_jinfUedB1jbdCwU7W0_6RoyjmtvvD7ulVKWhYIw3ILNK6McC2KoAsa6W7cDAEOvbUTQz_2KNzAiIB7vTrKHsh63UAfP2liwusME2nKKDpMpd5KGnddO_P-S2RRh_ZGWGy1qp53dr7kPe4v8-Sn2SIIDNjrV70MWghxcvjZY4uCvOwS0c11g0Ci0YPcxX5QCsEqgVb_TAO4kYoQ2cm9RpZOf91dMwe5wYPysxTkZUEmt-EzdzmM2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک هواپیمای ترابری نظامی آمریکایی(C-40 Clipper) که بر پایه Boeing 737-700C ساخته شده و عمدتاً در اختیار نیروی دریایی آمریکا (US Navy) است در بحرین فرود آمد. مأموریت اصلی آن جابه‌جایی پرسنل و محموله‌های لجستیکی است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72321" target="_blank">📅 19:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72320">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ما کنترل کامل تنگه هرمز را در اختیار داریم. حجم عظیمی از نفت از تنگه هرمز عبور می‌کند؛ همین دیشب، ۲۹ کشتی از آنجا عبور کردند.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72320" target="_blank">📅 19:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72319">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2074b2f37f.mp4?token=pWe94UC8-7tv56cjGPz9uCHyut6kAG1vqp1yze1Cu0-AQTZA8KGRom0BBR6eLu4aanE6c_g-pKSZnFG5Y-7RHhgt-Wemn7rbRH7RKwMxARnhzGh-S4SLBf4P4ImMa1PtyjsAWvqr3h_YzCBCoyust7ub7nbK93j2ZZJ0y-a5tP4JzDiY6Q351S6szJrnQH2RFImDD5kZILYtAdqKXVN-WFnSFC1kngn_ZSZT57WUuWtF5qD3uWRwBpRZ3iBg0PKh1nPGLUXQP8fBXYBVr-skPOdk2HzhlLnSUr2n0Q2H-duzgdBGIgjdJ1LdRTTOK-bPjPokTKGARaMl-AaOYnGKxA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2074b2f37f.mp4?token=pWe94UC8-7tv56cjGPz9uCHyut6kAG1vqp1yze1Cu0-AQTZA8KGRom0BBR6eLu4aanE6c_g-pKSZnFG5Y-7RHhgt-Wemn7rbRH7RKwMxARnhzGh-S4SLBf4P4ImMa1PtyjsAWvqr3h_YzCBCoyust7ub7nbK93j2ZZJ0y-a5tP4JzDiY6Q351S6szJrnQH2RFImDD5kZILYtAdqKXVN-WFnSFC1kngn_ZSZT57WUuWtF5qD3uWRwBpRZ3iBg0PKh1nPGLUXQP8fBXYBVr-skPOdk2HzhlLnSUr2n0Q2H-duzgdBGIgjdJ1LdRTTOK-bPjPokTKGARaMl-AaOYnGKxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بانوی گاثی که دریک براش هاپ هاپ کرد:
غذای مورد علاقه‌ام کباب کوبیده‌اس! بابای من ایرانیه و عاشق انواع کبابم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72319" target="_blank">📅 18:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72318">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72318" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72318" target="_blank">📅 18:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72317">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CismXcDen09iQGAp2SCbGHNje90TuCzqiiZ-m1qYcaeUy1oFR1KWA57fjdTuEQgZidr50MDnkjEMOGseJGCMQSrKevxlyWLQi3ERM4GJitaZWB4kX5yeI9ZMjya_rFzq4XKcBhAJ3T0S5bsb9ds93GAim89dWp2LLo6sJh-fyisSInGz1W_Anho90hCuCU61rgOHqol705sks1g60QQb3D7AvSM24TVYOe-Xd1CHff85M4rmc_ORDK5xAEej-1NP0eHuZT-Feoqa2-4-TAs4brWRDFmL6cBaTgVAD0zupktnc7JKYenrccA-39kh4M4CrrXux-NHvfq8G94EtJUdrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72317" target="_blank">📅 18:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72316">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20a8e0532e.mp4?token=J7KzeSKaRv4J7h4I_aCEV0HZNe_nQFuoHA-dUTkPsjt83hN_kfj0EhFG34iYAy2CZP7urB4pnKNM8eTsgrzdn0dtcMS8qFEPWu5Ot7AOrljkOLCcJqEvVzBd4ooVpW5Gvi1VuHnIfqI6IzhKYddWbqot6TmmeECtB0Hh4eNo0b6f91NMj5klJh5RSgZFZkcKCO3HWT3IVpKPFcvrzn2PjVkL1MCDLt7NkrVWOfqzSu_oTVL09C6suPp7IhlS2KEHYMPuRDmveozAIt1WAlJl_TXPefeRdRTjtIiB9eU4RlYJHIFLuwmpbjVtGsiiekJyrPHqgwBGqsUOpNH9x9gp3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20a8e0532e.mp4?token=J7KzeSKaRv4J7h4I_aCEV0HZNe_nQFuoHA-dUTkPsjt83hN_kfj0EhFG34iYAy2CZP7urB4pnKNM8eTsgrzdn0dtcMS8qFEPWu5Ot7AOrljkOLCcJqEvVzBd4ooVpW5Gvi1VuHnIfqI6IzhKYddWbqot6TmmeECtB0Hh4eNo0b6f91NMj5klJh5RSgZFZkcKCO3HWT3IVpKPFcvrzn2PjVkL1MCDLt7NkrVWOfqzSu_oTVL09C6suPp7IhlS2KEHYMPuRDmveozAIt1WAlJl_TXPefeRdRTjtIiB9eU4RlYJHIFLuwmpbjVtGsiiekJyrPHqgwBGqsUOpNH9x9gp3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراد ویسی:
بعید میدونم مجتبی خامنه‌ای بیاد بیرون؛ بنظرم مجتبی خامنه‌ای تنها رهبریه که توی تونل رهبر شده،
توی تونل رهبریشو طی میکنه
و توی تونل رهبریش به پایان میرسه.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72316" target="_blank">📅 18:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72315">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9475808af6.mp4?token=Kit50sOn8RK9Wqba1hFWLtuk_KZ2wMFou3rqvWPNeeTqPrE9k1V3yfTAYaf_hio6Dw0801kHFobNoIYJktg7H2Vf6p4BkROmHtDZ9ou6NWTQtefx3rS5i7qpZox_ue6Yn5nRLK6VomKJZW2MPoodlAXawvQMF-XZjOf4HefeALClBqzTn-TAoFzATMn2qjo9AtMU8tTwW_t6FpIsLONCnpTkhVbMCSAYgqKPIp-cPwUqUDsXiCl0-2y9iMA_00VTml2Xx5CfwcoIOA7lWSpiRgOu4c6EWJ44V08R-F8cWaLcl8UsPtmpV-TVH2ipHow4o0kMgoQy7BElle-u1fjjcBMCurApMOCU8kfVF_VjCd1CkfrXarlWUToGQKazcJVSgGqIOf7izqZqecu7WoqS6VhdbmFrzoxn6Q3XaTa5k4faR32foc7RSjCBcfthmYow35-x2TuwBV7QJIsAeMugohRIfC7TDBjFgN5uNHtzwF1QaaifgLfyqcuuId_GgaWBK1vJrXM4BoNWNIzpS_GqFgb9YzOM9hgfO0jT_sdGksw59ChmuYjPZKqDEiyFYTJ7uvdXKWyaoq7tuIxNN7fZibW638CUPOPK5KE9tWDV5nfASwiyjL3OjbI-RVd7nPY3wG_2LnvyvZ-XbPV3n7G_yJXMHOY-JDARYYZzw0NsUxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9475808af6.mp4?token=Kit50sOn8RK9Wqba1hFWLtuk_KZ2wMFou3rqvWPNeeTqPrE9k1V3yfTAYaf_hio6Dw0801kHFobNoIYJktg7H2Vf6p4BkROmHtDZ9ou6NWTQtefx3rS5i7qpZox_ue6Yn5nRLK6VomKJZW2MPoodlAXawvQMF-XZjOf4HefeALClBqzTn-TAoFzATMn2qjo9AtMU8tTwW_t6FpIsLONCnpTkhVbMCSAYgqKPIp-cPwUqUDsXiCl0-2y9iMA_00VTml2Xx5CfwcoIOA7lWSpiRgOu4c6EWJ44V08R-F8cWaLcl8UsPtmpV-TVH2ipHow4o0kMgoQy7BElle-u1fjjcBMCurApMOCU8kfVF_VjCd1CkfrXarlWUToGQKazcJVSgGqIOf7izqZqecu7WoqS6VhdbmFrzoxn6Q3XaTa5k4faR32foc7RSjCBcfthmYow35-x2TuwBV7QJIsAeMugohRIfC7TDBjFgN5uNHtzwF1QaaifgLfyqcuuId_GgaWBK1vJrXM4BoNWNIzpS_GqFgb9YzOM9hgfO0jT_sdGksw59ChmuYjPZKqDEiyFYTJ7uvdXKWyaoq7tuIxNN7fZibW638CUPOPK5KE9tWDV5nfASwiyjL3OjbI-RVd7nPY3wG_2LnvyvZ-XbPV3n7G_yJXMHOY-JDARYYZzw0NsUxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ:
کاری که آن‌ها می‌خواهند انجام دهند، باز کردن فوری تنگه هرمز است. می‌دانید چرا؟ چون دارند از پا درمی‌آیند. می‌دانید چرا دارند از پا درمی‌آیند؟ چون هیچ پولی عایدشان نمی‌شود.
آن‌ها درآمدشان را از طریق تنگه هرمز به دست می‌آورند؛ بنابراین با این کار، عملاً علیه منافع خودشان عمل کردند.
آن‌ها گفتند: «بیایید تنگه را ببندیم و برای دنیا مشکل ایجاد کنیم.» اما من وارد عمل شدم و ما بزرگ‌ترین محاصره تاریخ نظامی را برقرار کردیم؛ یک دیوار فولادی.
و حالا چه شده؟ آن‌ها دیگر پولی ندارند، چون می‌خواستند تنگه را ببندند.
و من گفتم: «بسیار خب. ما آن را به روی شما می‌بندیم، اما بقیه می‌توانند از آن استفاده کنند.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72315" target="_blank">📅 17:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72314">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6488dcc10a.mp4?token=EJV5-w6c7DdSxzPSsT0H5tBnBTBieP2UjN7sPYCSqm62GkrtRP2-MBjdzFKioUnLaDHu5N8Bxp-ijV1SxJRCo77gwgaoQYawgEA4eYTbKTjA5XlVXlMzZJvYiXLzGqHGBqQT3aHcnU10IEhD2jDshBoHSP7HVz4eVKyOlOkCTnPfuNhvIyNf9sVAoMB1_F2ZoqtakQIO-pE3TpRV8WyYjNNQf855AVCEUkEcBQGNtaoccnbDL3iTVpPA4rVQY9u-y110U_dZWPtx1A2ZeBAvIGO6DMMCerkh9cu8kqaVr6FgBdhsG-NqLcGyyKKe2VTTXAFoGpmNtP0Wn_O3zh8Fp7Crsix8TMCbim7XLg1cJgJJ8CXFWyAlFSnPycYjGiiSgaPT6z6wj71NJSi0kMRxfVDFSlxnlisYQmFchXLpYZniWQFi4WNz4NxD2FXsQhMlMIy0uzcRyBaLSSnbJvjlB4zL1o_2-8eEkwZfO1NU9LQtbuTKLcFR37gxG3qzVD3JqktJphMgOPOQXalQbvp1AcUYgLgCV7aMBCyLFXGqIAVRzxhxn0E8rtZqjpmWF4qt1znwcTj4baoUTgFHzdUecA8gHgVhsezrVjmNMc1hN7uoSvP297A78ypSNQshk6t8RNorkhKwiBrH0ge2g3_UlUR74228BIwP4rppKF5wJI8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6488dcc10a.mp4?token=EJV5-w6c7DdSxzPSsT0H5tBnBTBieP2UjN7sPYCSqm62GkrtRP2-MBjdzFKioUnLaDHu5N8Bxp-ijV1SxJRCo77gwgaoQYawgEA4eYTbKTjA5XlVXlMzZJvYiXLzGqHGBqQT3aHcnU10IEhD2jDshBoHSP7HVz4eVKyOlOkCTnPfuNhvIyNf9sVAoMB1_F2ZoqtakQIO-pE3TpRV8WyYjNNQf855AVCEUkEcBQGNtaoccnbDL3iTVpPA4rVQY9u-y110U_dZWPtx1A2ZeBAvIGO6DMMCerkh9cu8kqaVr6FgBdhsG-NqLcGyyKKe2VTTXAFoGpmNtP0Wn_O3zh8Fp7Crsix8TMCbim7XLg1cJgJJ8CXFWyAlFSnPycYjGiiSgaPT6z6wj71NJSi0kMRxfVDFSlxnlisYQmFchXLpYZniWQFi4WNz4NxD2FXsQhMlMIy0uzcRyBaLSSnbJvjlB4zL1o_2-8eEkwZfO1NU9LQtbuTKLcFR37gxG3qzVD3JqktJphMgOPOQXalQbvp1AcUYgLgCV7aMBCyLFXGqIAVRzxhxn0E8rtZqjpmWF4qt1znwcTj4baoUTgFHzdUecA8gHgVhsezrVjmNMc1hN7uoSvP297A78ypSNQshk6t8RNorkhKwiBrH0ge2g3_UlUR74228BIwP4rppKF5wJI8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ:
من توافق آن‌ها را رد می‌کنم. آن‌ها می‌خواهند توافقی کنند که طی آن فوراً تنگه هرمز را باز کنند، چون دارند به‌شدت متحمل شکست می‌شوند.
می‌دانید، شما این موضوع را در «اخبار جعلی» نمی‌خوانید یا نمی‌بینید؛ اما ما داریم با قدرت تمام پیروز می‌شویم.
ما کنترل کامل تنگه هرمز را در اختیار داریم. حجم عظیمی از نفت از تنگه هرمز عبور می‌کند؛ همین دیشب، ۲۹ کشتی از آنجا عبور کردند.
آن‌ها خواهان توافق هستند و به نظر من این اشکالی ندارد. من هم از توافق کردن استقبال می‌کنم، اما آن توافق [مدنظر آن‌ها] قابل‌قبول نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72314" target="_blank">📅 17:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72313">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5297b02f7.mp4?token=HIkoJfLh82XHs_Wt5C4HYtyYQBnctzuyl13RPZSbuUXVlUrrJW_s-GfM3Ki4qy6vdOfSB7rNSbUoTvX-mnNja7rELQoHd-fw839oO8LktyYB15GoIh6jwQ9VnXJ-1auE3TnNx1wru6_4CEhWS-8S4oT58v2wNZq2CSRkijboOo4H8lNcJaB4zaASSt2FB90R4mxKE6XX7Bt6kbC0DmNVGGGmezmQ4RRLlMWxRRCoS8yFkCVGQiaA1A7z9p2RRCvY2XNf8-Q9gSxv7wXM3EUBEzwb_conihsMHhB6OTlk_KRttCejFE9_ksy6jV2h0Dx5bd_TjbL9sOqkthUnHSrfAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5297b02f7.mp4?token=HIkoJfLh82XHs_Wt5C4HYtyYQBnctzuyl13RPZSbuUXVlUrrJW_s-GfM3Ki4qy6vdOfSB7rNSbUoTvX-mnNja7rELQoHd-fw839oO8LktyYB15GoIh6jwQ9VnXJ-1auE3TnNx1wru6_4CEhWS-8S4oT58v2wNZq2CSRkijboOo4H8lNcJaB4zaASSt2FB90R4mxKE6XX7Bt6kbC0DmNVGGGmezmQ4RRLlMWxRRCoS8yFkCVGQiaA1A7z9p2RRCvY2XNf8-Q9gSxv7wXM3EUBEzwb_conihsMHhB6OTlk_KRttCejFE9_ksy6jV2h0Dx5bd_TjbL9sOqkthUnHSrfAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛ترامپ درباره طرح هفت ماده ای ارائه شده توسط ایران:
آن‌ها پیشنهادی ارائه کردند، اما من آن را رد کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72313" target="_blank">📅 17:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72312">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXOpfoKGCURXk-w1zvzmPryjov8nmFKje4R3BUadJJvsBD3QBnYSkYbkOTV2OfKov4j3h5guS4oOFs0JXmD6dk7i_kbYsI5ID2zsqf0teUvE0nnEvtdlC0d-WSZkmCm2f2SeS6JZzkEZceVcnodzGWWpK917XdY_QA79eXUR5aBh-htQKcdMPfl3JBExtX6ZZJrcrypNUnC_fwwBS8U_ryAMjLX9iCppX9RYs4o0WMwftJIwvcQ9zsW69L3k6O-I_4YenpE_0ks5l6y40zz0QZwltuDMa8Jd5BGn5GBDf1iwCrOZcnfEHtjOesJDERWdBMi3InO2ZNZhDbm0ykWW0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایران نمی‌تواند سلاح هسته‌ای داشته باشد!!!
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72312" target="_blank">📅 17:09 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72311">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b70e110ec.mp4?token=BZdO0U1WlSdUoYj6J99pYwqclZbAAl0opRoqLMGqRpFvF62T29CphkxwAfZfP2HkpIVkM8_2NhIsGGNdYiCfBXru-IlMYxfIQCIbhCpIQsdYldpKWi7JgjAv6v5stk0b5d228Nrl3D63mw2r_FD5uVVs9M-t3RnaMPvc2CiwyHzSfVphQPPRjIrCa7HpZnWRw50UaaCGasnBRWAAWEYBfWR7LrrafnbS7zhv3CMpMhHRoX1Eq1ul7YKPsco0xMDMjdqjEGHGgnurem7lfNR5cOb0Tiy2qeyT-_W0UCyuoKcCJq__HxP_qvvcm-p5259F4OV0ZGDPPEkLZp8QjqxpAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b70e110ec.mp4?token=BZdO0U1WlSdUoYj6J99pYwqclZbAAl0opRoqLMGqRpFvF62T29CphkxwAfZfP2HkpIVkM8_2NhIsGGNdYiCfBXru-IlMYxfIQCIbhCpIQsdYldpKWi7JgjAv6v5stk0b5d228Nrl3D63mw2r_FD5uVVs9M-t3RnaMPvc2CiwyHzSfVphQPPRjIrCa7HpZnWRw50UaaCGasnBRWAAWEYBfWR7LrrafnbS7zhv3CMpMhHRoX1Eq1ul7YKPsco0xMDMjdqjEGHGgnurem7lfNR5cOb0Tiy2qeyT-_W0UCyuoKcCJq__HxP_qvvcm-p5259F4OV0ZGDPPEkLZp8QjqxpAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه عرزشی داره فخر میفروشه نسبت به بنزین مفتی که میگیره در حالی که بقیه مردم ایران و دنیا باید گرون تر بخرن
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72311" target="_blank">📅 17:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72310">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/204024e85e.mp4?token=cEKMyUwpjycqiqMbNHAmsaiWkIJxGHAoZP11t30ppclo4xPo9D_BYQXKW4Tr5LUvq4LOcW-rKtOlbADERjp3a3YBkQbVilK1s42ZKs0EEMmtWzaKtbe-7kuSxejgkyx0hjWt99SVzLTTHMz-ShiQyMRAStHr14KaPUHZ9_5P7EnPMglwYno-uZekq_jB1aT7CDfOCnGsC36xjVzecdeEhuj4HzvMe7VdlIoWoAZ66Cbj-bHCEQDCnQ65hrCpc164rbiDKGXelRojxkgSkcivEzWRzfgPyzZvv00DUvLOARsbRZQ1Rph0FPpVdRWLBMC7G2d_mpFAuTnl1PZGL_Iqwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/204024e85e.mp4?token=cEKMyUwpjycqiqMbNHAmsaiWkIJxGHAoZP11t30ppclo4xPo9D_BYQXKW4Tr5LUvq4LOcW-rKtOlbADERjp3a3YBkQbVilK1s42ZKs0EEMmtWzaKtbe-7kuSxejgkyx0hjWt99SVzLTTHMz-ShiQyMRAStHr14KaPUHZ9_5P7EnPMglwYno-uZekq_jB1aT7CDfOCnGsC36xjVzecdeEhuj4HzvMe7VdlIoWoAZ66Cbj-bHCEQDCnQ65hrCpc164rbiDKGXelRojxkgSkcivEzWRzfgPyzZvv00DUvLOARsbRZQ1Rph0FPpVdRWLBMC7G2d_mpFAuTnl1PZGL_Iqwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه تعداد هم وطن به مناسبت شروع سال تحصیلی لوازم تحریر جدید گرفتن پخش کردن بین بچه های محلشون
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72310" target="_blank">📅 16:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72309">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11382bd536.mp4?token=YbK6rutQ3hAIrZjQmKbse_v4cNtevnVLc5UEkuAWokcWZsn0mcliwYTAjBcJMm0XI0hrRALyphGYK4PiTZKXnq5i8A5w9rJGr9pi_7-Rtv44P-mpzedmgCSicAGxUKPcP-k0B9lsHWSCmYMofiY41L70zz0WgmiZ7UKQB3RpjZRwyDS6b8ecXFdjZHWYU2GvlvZRLQgkl-TwWTlUA-097YldKA2sR0bWzw9D1-CbCUc7QEIUqFQnong24yqKSDSRHWJfmHtafLqhexSYf4strup16JV4m97HBmX6puB64r6-NIsvSezqSWJKwkKwhXyGqdzNATmGhBHFG007BlUHxQC-iEPhjFupUbD2GQEDCPUMCCRxxr6tSIfb-D22i72EIcTXScr7rc2ZSk2SdMBqKKV2fg9WrIwmGtT4KV0lqS0IX1A_YwOPZW6zRhR7Fb49Odwe1YCgCYcXIZZK1E0s_XRu5kdlNkF8YeehHioZsLNEWJAscxI9g_Jybt5kpgg1O4ehB7K2bMPy6EEabwu8SGvm7YugH1wU-bxaR4DW3Zz7UfRsrGMLZIaDfHwOzdbdXsrHYEmn3nTkOlWb1leL-USioXISqgu6yoIxs0930elhadXlPoM-KjuJopttBB3aomACjwZZ2pw66sxVGIpJCs4iTa9emw7onQmgDlmJ9to" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11382bd536.mp4?token=YbK6rutQ3hAIrZjQmKbse_v4cNtevnVLc5UEkuAWokcWZsn0mcliwYTAjBcJMm0XI0hrRALyphGYK4PiTZKXnq5i8A5w9rJGr9pi_7-Rtv44P-mpzedmgCSicAGxUKPcP-k0B9lsHWSCmYMofiY41L70zz0WgmiZ7UKQB3RpjZRwyDS6b8ecXFdjZHWYU2GvlvZRLQgkl-TwWTlUA-097YldKA2sR0bWzw9D1-CbCUc7QEIUqFQnong24yqKSDSRHWJfmHtafLqhexSYf4strup16JV4m97HBmX6puB64r6-NIsvSezqSWJKwkKwhXyGqdzNATmGhBHFG007BlUHxQC-iEPhjFupUbD2GQEDCPUMCCRxxr6tSIfb-D22i72EIcTXScr7rc2ZSk2SdMBqKKV2fg9WrIwmGtT4KV0lqS0IX1A_YwOPZW6zRhR7Fb49Odwe1YCgCYcXIZZK1E0s_XRu5kdlNkF8YeehHioZsLNEWJAscxI9g_Jybt5kpgg1O4ehB7K2bMPy6EEabwu8SGvm7YugH1wU-bxaR4DW3Zz7UfRsrGMLZIaDfHwOzdbdXsrHYEmn3nTkOlWb1leL-USioXISqgu6yoIxs0930elhadXlPoM-KjuJopttBB3aomACjwZZ2pw66sxVGIpJCs4iTa9emw7onQmgDlmJ9to" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مقایسه ارزش برگ‌های اسکناس با یک برگ دستمال‌کاغذیِ دورانداختنی
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72309" target="_blank">📅 16:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72308">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d50ab7df03.mp4?token=ZKw6r7Xz7DWr2Hbis4o3G3UN7u6_CuJTgkDvKBd0snv8vmylsH9nXMoGDsEh4KM0Ndg-8Papqwv8ZQcSPWVv24oGwOyl3opaGJJexmurMPlDY9-BoAEMAc8_10DVlpap773NylJT2oW-hoIF2sDrX8VQ1O7xmQYEGJ0_FpkyRkXYWSkatZzxYT53gXzqiRcVeFz5Xo-TO_chXtW4MVnpQnhE5SeTVPokv7-t8otJuyUNKVt_NICRBaOwKH516dcl9D3xAANwfACnVHyfua0ioytESeobPYhnq6KLaadWNksoKsvIhmlIHgEwiQ6uwYGWlMp7hnyeVZl01qvRjG5oSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d50ab7df03.mp4?token=ZKw6r7Xz7DWr2Hbis4o3G3UN7u6_CuJTgkDvKBd0snv8vmylsH9nXMoGDsEh4KM0Ndg-8Papqwv8ZQcSPWVv24oGwOyl3opaGJJexmurMPlDY9-BoAEMAc8_10DVlpap773NylJT2oW-hoIF2sDrX8VQ1O7xmQYEGJ0_FpkyRkXYWSkatZzxYT53gXzqiRcVeFz5Xo-TO_chXtW4MVnpQnhE5SeTVPokv7-t8otJuyUNKVt_NICRBaOwKH516dcl9D3xAANwfACnVHyfua0ioytESeobPYhnq6KLaadWNksoKsvIhmlIHgEwiQ6uwYGWlMp7hnyeVZl01qvRjG5oSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضخامت رنگ کوییک اسباب بازی از تولیدی کارخونه بیشتره !
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72308" target="_blank">📅 15:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72306">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c686tLJcbbtx0SF00Jrje-dBAI0pSuQp8VKA6HqRlmhPNMlhQbS0Z7MtI-ylE7ASX2fzx0I-ANKhwQ2z3wG4ZZQcC2gCoQ3yR4trEuEh9x3rgXAqjyKblCiqw7lGQjOzd31LmALht-mmw8z1zarRlnZEUELYKuzXayptXxfxvklOT3bDMlUTaFBOnQ7HQDAK3vkqCge7UtaJqkya7ltBs2-TeX73rqAe-ODUGZKDu-QHViDsdlcg6hGQ_lQftCG66efcHc6Tt7n4pLHl5bw0zjD7FHb4EcFa8o_oTZNbQN1x0k6H26jpoJILCF8aLuityCNcYnXnYJ7VHmawbL74fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0d7c1c9217.mp4?token=HWTVHOPD1vxmLFHTElVDtM34nETeXEPdfL0xolbJUIhHvlSJII3p_0wsFPRC-TxU-m2Qzmpmk84F8x6OCDLPZZWnTa0orSequ3UTyRAdoBM2fIRX_LqG0WFzNXK6J3i531rU7NNjsFL6Q-0AgX-5FUFst5-K5gNG3-FWpgzcmfv--qomFbi4j0AgOtFL5ZRGBPeZVn5fhN8kGNC3K7zUr3Li60PB9YGVkfR8c85L0VLlW1Iwg-_7KL4SdBEmZHWyHkHWg3BBKvAoCdkLznpBooTS-TzfbXQ1fvrtvt2G26mtxlvW4bnVWqlOQQBMmSNiZzRx6VumkTUSwFc9_jLngg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0d7c1c9217.mp4?token=HWTVHOPD1vxmLFHTElVDtM34nETeXEPdfL0xolbJUIhHvlSJII3p_0wsFPRC-TxU-m2Qzmpmk84F8x6OCDLPZZWnTa0orSequ3UTyRAdoBM2fIRX_LqG0WFzNXK6J3i531rU7NNjsFL6Q-0AgX-5FUFst5-K5gNG3-FWpgzcmfv--qomFbi4j0AgOtFL5ZRGBPeZVn5fhN8kGNC3K7zUr3Li60PB9YGVkfR8c85L0VLlW1Iwg-_7KL4SdBEmZHWyHkHWg3BBKvAoCdkLznpBooTS-TzfbXQ1fvrtvt2G26mtxlvW4bnVWqlOQQBMmSNiZzRx6VumkTUSwFc9_jLngg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
ما زندانیان آمریکایی را آزاد کردیم اما آمریکا زیر قولش زد و پول‌های ما را آزاد نکرد
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72306" target="_blank">📅 14:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72305">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اثر جدید ابی به یاد جان‌باختگان ۱۸ و ۱۹ دی
از او بگو به دنیا..
از او که قصه ای داشت او جشنِ زندگی بود..
سروی که قد برافراشت از اُجرتِ گلوله ..
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72305" target="_blank">📅 14:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72304">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a59d978fb2.mp4?token=CxH8aISwpQow8RHq44vNxGiox0mfevjlmHQTkBgj3TgZzreNq8RQ_WclDxBv-x09Bcj3YabT4jkBNPLFymUHxwQvu7FfAjGT4n1LRXfhP4QdDpTbqRusAyUwbPTIEqXn0IyIjGPOREZKm4uvKFuPZuG8ZMCnk7yW3zisV7WGBTPUDedTgWw-6GmYXYcq5h0eIbuiWV1nXrJoGLhIX7Aiw54_sFj3ppS_5LgFOcMMBNudN_V3IWRY9pMk1cS2LTyhmxoL12-3VaC11aQGvVu_Tpi4jDqxMVb984b8gOiVlAsix1N5K3QX5nlPoG5gDM__7AcPZIhFE6-Hoh5bJtFHzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a59d978fb2.mp4?token=CxH8aISwpQow8RHq44vNxGiox0mfevjlmHQTkBgj3TgZzreNq8RQ_WclDxBv-x09Bcj3YabT4jkBNPLFymUHxwQvu7FfAjGT4n1LRXfhP4QdDpTbqRusAyUwbPTIEqXn0IyIjGPOREZKm4uvKFuPZuG8ZMCnk7yW3zisV7WGBTPUDedTgWw-6GmYXYcq5h0eIbuiWV1nXrJoGLhIX7Aiw54_sFj3ppS_5LgFOcMMBNudN_V3IWRY9pMk1cS2LTyhmxoL12-3VaC11aQGvVu_Tpi4jDqxMVb984b8gOiVlAsix1N5K3QX5nlPoG5gDM__7AcPZIhFE6-Hoh5bJtFHzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ترامپ در پلتفرم ایکس منتشر کرده:
در این ویدیو تصاویری از انهدام یک لانچر سپاه دیده می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72304" target="_blank">📅 13:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72303">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">گزارش های تایید نشده از انفجار در نزدیکی جزیره خارگ/همچنین صدای انفجارهایی از سمت تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72303" target="_blank">📅 13:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72302">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afc192b406.mp4?token=RPGta2xBb36hm1wp8SKCIuUoKV1b4rsze94dY50e16YUnJFnKeT65fugrdCZj-l_j9cCowIHHUPr55zkIa87fKci45V3Q8qz77P3826tCGZ7wvH2CF62SiUfT58KFE_efhU1MmgObaZycf1cbPfWEmKwYgIUNSaFTj4gCTze38UhEqZUB5DUhRrvc1knBr_jgggUHpJ4K148cN0WvrOCp7Sulc2zWf_qzI5QB0K_R-MqKOLXKLLrVWqkuvn8e12QN9n-VlMeB1hMaXPp3OVK9A3vCYQRXIollb69ZgdOVdpfXU4KI42bqa4KK9NKA_NyuSzejitl5s18ra-uh4bdbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afc192b406.mp4?token=RPGta2xBb36hm1wp8SKCIuUoKV1b4rsze94dY50e16YUnJFnKeT65fugrdCZj-l_j9cCowIHHUPr55zkIa87fKci45V3Q8qz77P3826tCGZ7wvH2CF62SiUfT58KFE_efhU1MmgObaZycf1cbPfWEmKwYgIUNSaFTj4gCTze38UhEqZUB5DUhRrvc1knBr_jgggUHpJ4K148cN0WvrOCp7Sulc2zWf_qzI5QB0K_R-MqKOLXKLLrVWqkuvn8e12QN9n-VlMeB1hMaXPp3OVK9A3vCYQRXIollb69ZgdOVdpfXU4KI42bqa4KK9NKA_NyuSzejitl5s18ra-uh4bdbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهدی خراتیان کارشناس صداوسیما از نامه ای محرمانه که چند روز بعد از اعتراضات ۱۸و۱۹ دی از طرف جمهوری اسلامی برای دونالد ترامپ فرستاده شد می‌گوید :
ما از طریق سوئیسی‌ها، حدود دو سه روز بعد از حوادث ۱۸ و ۱۹ دی، نامه‌ای محرمانه برای ترامپ فرستادیم.
نامه به تقریر رهبر شهید بود و فکر می‌کنم آقای پزشکیان هم آن را امضا کرده بود.
متن نامه چند محور داشت و لحن آن بسیار جدی بود. در این نامه به ترامپ هشدار داده شده بود که اگر جنگ را آغاز کند، شرایط مثل گذشته نخواهد بود و ایران درخواست آتش‌بس را نخواهد پذیرفت.
تأکید شده بود که جنگ را به منطقه خواهیم کشاند، به پایگاه‌های آمریکا حملات بی‌سابقه خواهیم کرد، به نفت رحم نخواهیم کرد، مسیرهای انرژی را خواهیم بست و چه جنگ باشد و چه نباشد، به اسرائیل حمله خواهیم کرد.
رهبر شهید نیز در یکی از آخرین سخنرانی‌هایش تأکید کرده بود که این جنگ قطعاً به یک جنگ منطقه‌ای تبدیل خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72302" target="_blank">📅 13:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72301">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72301" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72301" target="_blank">📅 13:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72300">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3QfRb0SErty7i_VYw86U-xoxY7qbk_QkTHpRqRl2HJLyO3pnKDsf9V5NIArhBlHXiBJiIGy-DjH6CBXpL4RAWa82jYUkFbChVj1ytinFAw8HdgJkfhVQANn-WBu2WN9vXU7Qs2MUGXnXGJIt6L-nhxIlFsfPdFtizny3j5iSzlR24pQs2-tM_jWDb5Ro0e683q2Yl5krydtAuoFZBswRdavtPL-y0czY5Zd-bYOYES7rXYjRqlaIbJzSXu_rtGgCBQjsnDjdwd9zNIl92l9siARrn3sAPJ07ew8LphroRhOh9s_La7IEIOF4GKhGDTeNxCZ1sPl8xugbyjCBGxjfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز اسپانیا
🆚
انگلیس را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
اسپانیا: ۵ برد و ۹ گل زده
انگلیس: ۴ برد، ۱ شکست و ۱۴ گل زده
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
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72300" target="_blank">📅 13:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72297">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mTi5xwiLDeJ7Gxyw_mIPFT0MpL_ownU_dFk59U4QPgWbI9twSeEhzq2UDi2RdMnoUP_S8DXHJ58s914HQKEiSW6ou2RVlIAmbd-nOscmarz2q5JJspRWbvJBgN5l5brXrN02OgDSiVFAJvzRPilEuqNsotwf2eNKJWLnqBjT_6sP4MK1Jw1F8Gl6G-7e9xFzgW2MTfe6E6dPCDDy8JcjrEBcG1-59NwSOjZ05xzidsjBG0qBruapWHsWxuwoO0CUOWlemptdDrA8WVytH5dHFyGaMarBSWCIkZBEL_61_dIjyaaQYDRmDJOKjsMmvh5hDiGjKXtb3bqAOAmOZIxYlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mzf7fdfRe6eBjdJNqrAWmO-GqAPqBl38K27fOblWakZiHZPPdu3PSh7meaXFulbhY3bj6QBH8vul8kkuMWY8pk85veopZkDTZVXn6vVgql8aQdRtvGt-9AS40O7LIc0oQLD4au7EWum0ZsmYX8iapIP51vENCIEHiMuTUrr5o_n2Oh17hHD-YnJUeSjJDNeYgNidhmKIyzTNxuYn67ndWLdmxW8oWX43jL1hVB2hybhtuoLx_LXvw36jPfpE6q-MN4O5E0csk-XYHRi-LYSu9MHrkkAHzp3DU4LVRiigkKAZDN6IEpKpK9JemtelQBYb7sBM44HbiCMW6i78z-9GYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AoVilneX-GkfexFXaEu2UapPMp19iyisSBpKwz1-kFL4LXxNfNFvGZfo3OY75r2iYUpqkWwIHHjdXWTkcEp9LNKSYQXge-e13pn3Hyr3fpuDxBlXxe-1wq95odk6BT0KB7D8WJP_tya36NcQMvxneZI3a9mzpDtOyqOWABGawssLAfVX5aBPrZEQJP9SI21ooU_HHJUXzL5vMVmpfTEQC6yXM5u0Kl8a4rhHHq-ImbyXQjJADRoyvkYeY4HixjhRhw7FkTNJq7mETDmQKQ-1-tIs--asANlqlNOnbEjLJEh2b7UxtmFuyfTuF-lehffHCO_Ba8IWRW9rizrlgz5_mg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سیرک جان فدایان ادامه دارد
ترامپ توسط جان فدایان دستگیر شد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72297" target="_blank">📅 12:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72296">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/748f1ed77f.mp4?token=lGxcVkAhHXVMvwA_eZHORl1D8RpNQH7NBpHh6FQD_7t3X2RrxaX8bCOUaLVmzk20sychc7B52cH7L24hCord0vroqre9HW0zyT6FaiG6lW43KvlnWOPxg39W0_8ehnc7Qxu99Yg84X5XL7VJqbJREBj8kDErJb8dztWK6JNXh7hx_6kqrfIAfjJ1CC1o13BtrRCcIGp9B52o31Z5rUOOE5h1NjLKl7CptYNWebIh8lloiW3tmje6nSXWi-1JtPQX0eDFvxbG2OdDrGpOobRvvtZo6i7p8GIOwnPFKNfFS7nWK_-xWrY2yYWfTlR1aUQV_f7mp22JSTzpIH0ZgcWAlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/748f1ed77f.mp4?token=lGxcVkAhHXVMvwA_eZHORl1D8RpNQH7NBpHh6FQD_7t3X2RrxaX8bCOUaLVmzk20sychc7B52cH7L24hCord0vroqre9HW0zyT6FaiG6lW43KvlnWOPxg39W0_8ehnc7Qxu99Yg84X5XL7VJqbJREBj8kDErJb8dztWK6JNXh7hx_6kqrfIAfjJ1CC1o13BtrRCcIGp9B52o31Z5rUOOE5h1NjLKl7CptYNWebIh8lloiW3tmje6nSXWi-1JtPQX0eDFvxbG2OdDrGpOobRvvtZo6i7p8GIOwnPFKNfFS7nWK_-xWrY2yYWfTlR1aUQV_f7mp22JSTzpIH0ZgcWAlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاکر کارلسون گفت که پس از تلاش برای متقاعد کردن دونالد ترامپ جهت پرهیز از جنگ با ایران، او به وی چنین پاسخ داد:
«بله، حق با توست؛ اما در نهایت همه ما می‌میریم، پس [این موضوع] اهمیتی ندارد.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72296" target="_blank">📅 11:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72295">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47aef3d95c.mp4?token=TncWze5tQEOTs0E9MED5R98KmT3gP22eguBHKZR5pIaXBYmr-LCqvI5lqE5eKPQCL1cCPP0L42rznhNVFMj-WxGDH0zZYbgVfAJJ0bi1I-63eIRuSLxB3GGoRzia-CYvCnHO6zkp8gMPE5HQ0NAla0olKukUe-mIDcOULUTuRg9BKhPF8D_jaXhHUSVoLnpBorQf2UtKsWAS1bKnugyaHshxXA8AvNE6J6SWlelfazy56QwNCusLileZWrTcaDy156ibNtUisZGrCWLNKttLFtJI74dsz2k7sOexa2LdHWbfOtT6QbSCUnzDLAwUvZA1bLbefjhqV8VCCOE-Y11SGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47aef3d95c.mp4?token=TncWze5tQEOTs0E9MED5R98KmT3gP22eguBHKZR5pIaXBYmr-LCqvI5lqE5eKPQCL1cCPP0L42rznhNVFMj-WxGDH0zZYbgVfAJJ0bi1I-63eIRuSLxB3GGoRzia-CYvCnHO6zkp8gMPE5HQ0NAla0olKukUe-mIDcOULUTuRg9BKhPF8D_jaXhHUSVoLnpBorQf2UtKsWAS1bKnugyaHshxXA8AvNE6J6SWlelfazy56QwNCusLileZWrTcaDy156ibNtUisZGrCWLNKttLFtJI74dsz2k7sOexa2LdHWbfOtT6QbSCUnzDLAwUvZA1bLbefjhqV8VCCOE-Y11SGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان درباره مجتبی خامنه‌ای:
مجتبی خامنه‌ای هیچ‌گونه مشکل یا چالش جسمانی خاص و مداومی ندارد.
در آخرین دیداری که بیش از هفت ساعت طول کشید، البته ما عادت نداشتیم که آن‌قدر طولانی‌مدت در حالت نشسته بمانیم.
ما زاویه و وضعیت نشستن خود را تغییر می‌دادیم، پاها را روی هم می‌انداختیم و کارهایی از این قبیل؛ اما قطعاً او از سلامت کافی برخوردار بود که بتواند پس از آن ساعات طولانی در آن وضعیت، بایستد.
از منظر پزشکی، او کاملاً سالم است. این را از زبان من به عنوان یک پزشک بشنوید و بپذیرید: او هیچ مشکلی ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72295" target="_blank">📅 11:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72294">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d63e3933a.mp4?token=s8LPgDx0_OBv3hsaRn-OKSsJ8w2pNQmHB3D9WsLtKkA5XTC-q3RnyAP2_Zi6JyOyCsdqqjYPAQ2plBbSo21a1bqDAmpA_0dyGJhjNfUbbU2Qv8nBAwA6qbYFZaedJvCt9gKfhPRTbzzTlgOCpJRVhWGqpIaiOTEFiEy5K11siwZaaSQxaSaEks2svChdogtayStJyif1ba83TsJrKutZnyr8lQvNnvBpT2fjY8KUNAzznjzWdqF06O4bmyMKDOFk0D7oXmnkNxm04cbYatafeDaUbTrQP5YNUs4wjsBRicC4kMOfPSOKWjgE6fU5Aeuc05dDi5lQHvfIxW_yNHVexg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d63e3933a.mp4?token=s8LPgDx0_OBv3hsaRn-OKSsJ8w2pNQmHB3D9WsLtKkA5XTC-q3RnyAP2_Zi6JyOyCsdqqjYPAQ2plBbSo21a1bqDAmpA_0dyGJhjNfUbbU2Qv8nBAwA6qbYFZaedJvCt9gKfhPRTbzzTlgOCpJRVhWGqpIaiOTEFiEy5K11siwZaaSQxaSaEks2svChdogtayStJyif1ba83TsJrKutZnyr8lQvNnvBpT2fjY8KUNAzznjzWdqF06O4bmyMKDOFk0D7oXmnkNxm04cbYatafeDaUbTrQP5YNUs4wjsBRicC4kMOfPSOKWjgE6fU5Aeuc05dDi5lQHvfIxW_yNHVexg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا ایران بعد از امضای تفاهم‌نامه با آمریکا سه کشتی را زد و تنگه هرمز را بست؟
اینجا احمدی‌مقدم در حال توضیح دادن یکی از دلایل آن است:
نود میلیون بشکه نفت‌مان از محاصره خارج شد اما خریداری نشد.
چون ناگهان نفت زیادی عرضه شده بود، مشتری‌ها با قیمت‌های پایین می‌خواستند بخرند.
با بسته شدن تنگه، همان را با قیمت بالا فروختیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72294" target="_blank">📅 10:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72293">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_k9KVIVvTmlxM3E5kxhjJKWiDdlhdL22WZ0l9yH1yAl1FrYiNRP5U8Z5Y-Gp7XiMqNAJDoPNRtLiAsSbBweZAXfGsPzwHAaZr0JhnMsRFm1q7kZxy11N_tt6PYITnjotLs6hsj_NyrDRC9rovYTP8J8kcr9RKZhTbVMtKkTocaEzICJUIW0TRJUcejZh-FcfeaUhAzUMjBiwoZVduqCM-n49XgY8Dr536FSk7NEBR5OMGDOAACRe7AQkUEElW_lNO6zOsJEmqUm19kNojeUrp7pMr3hsK4ProGoBoDClnzfn37spB5Qta_enud7Pzc0FXN2KMz1s5Ys9u0hTyEu0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛وال‌استریت ژورنال:
به گفته مقامات آمریکایی، ترامپ پیشنهاد ایران برای برقراری آتش‌بس هفت‌روزه را رد کرده و اعلام داشته است که انتظار دارد پس از انتخابات میان‌دوره‌ای ماه نوامبر، بمباران ایران از سر گرفته شود.
پیشنهاد ایران شامل بازگشایی تنگه هرمز و ازسرگیری مذاکرات هسته‌ای در ازای لغو محاصره بنادر ایران و کاهش فشارهای اقتصادی از سوی آمریکا بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72293" target="_blank">📅 10:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72292">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2ed2f431b.mp4?token=IfVMB4lxIViCcI6mJD3osBoT6qIghNIbAQ2ROs0XIfy2nepAYhYVQKYJdCiM-KdbI_2BhgFeoiTqJOJS0NPxJe_w18l3ClRWZ8-ksfyQzal55s9STq5ixuzpmyqyDKLLAN5yqGdz4Q3AT_lCexU6vbazu-IVFroofGM6jahfI9eMI32_cY2PGnRGGPltKTbzhstkPQSNWRh5jNuIUViCokVAAUejYXa_zrRPQtNFEq3v4YjcrDqwJhCYQ5uBQ42MfwdmGJRyyKZwVaA4vsTzAamE7-g61TkwuFTaSRVR3JZiHFCPwnPNU3PStymsyEg0BNcqqwG7Bcg4IV6p40fMaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2ed2f431b.mp4?token=IfVMB4lxIViCcI6mJD3osBoT6qIghNIbAQ2ROs0XIfy2nepAYhYVQKYJdCiM-KdbI_2BhgFeoiTqJOJS0NPxJe_w18l3ClRWZ8-ksfyQzal55s9STq5ixuzpmyqyDKLLAN5yqGdz4Q3AT_lCexU6vbazu-IVFroofGM6jahfI9eMI32_cY2PGnRGGPltKTbzhstkPQSNWRh5jNuIUViCokVAAUejYXa_zrRPQtNFEq3v4YjcrDqwJhCYQ5uBQ42MfwdmGJRyyKZwVaA4vsTzAamE7-g61TkwuFTaSRVR3JZiHFCPwnPNU3PStymsyEg0BNcqqwG7Bcg4IV6p40fMaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رامبد جوان :
سانسورچی‌های صداوسیما واقعا مریض جنسی هستن
طوری که با سیبیل خانم تحریک میشدن. میگفتن سیبیل فلان مرد زنانه‌ست و تحریک کنندست.
یادمه توی یه سکانس یکی از بازیگرا میگفت «بیا بشین اینجا». میگفتن اگه یکی فقط صدا رو بشنوه ممکنه از «بشین اینجا» برداشت بدی کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72292" target="_blank">📅 10:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72291">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f2932ca5f.mp4?token=q1phndXkIQz7SeCSV1foKbv6jp0YrYO8du2Bc0CYyjQR73Z4638NiK1ugW4muYS-tEAdWNfSAunQcIzBoZAcEZuOiqEMVS8to6gSgFoQiYl4FxcjqlvygNXEEd765A5TeIiyytJivo1doqGvQBlzAiXl5FGp2inInG6vEFTls3XpplL7GdYmUY87V0oKcjssxSBFBMDC1ynfgyUyd9MDdRDfgt6sxYWuisbVrbcsXDuTAZcvoA4AvTnxAK6XjsgXo4YbDzcM7jo_5pY5KSLKP5O0dJ-mL0sHYLDp1LF_VQebzrSAD2DoP_iK2SqOrSmlSVM8iLkLlkbTeTzI7lss3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f2932ca5f.mp4?token=q1phndXkIQz7SeCSV1foKbv6jp0YrYO8du2Bc0CYyjQR73Z4638NiK1ugW4muYS-tEAdWNfSAunQcIzBoZAcEZuOiqEMVS8to6gSgFoQiYl4FxcjqlvygNXEEd765A5TeIiyytJivo1doqGvQBlzAiXl5FGp2inInG6vEFTls3XpplL7GdYmUY87V0oKcjssxSBFBMDC1ynfgyUyd9MDdRDfgt6sxYWuisbVrbcsXDuTAZcvoA4AvTnxAK6XjsgXo4YbDzcM7jo_5pY5KSLKP5O0dJ-mL0sHYLDp1LF_VQebzrSAD2DoP_iK2SqOrSmlSVM8iLkLlkbTeTzI7lss3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی کامل سخنرانی بنیامین نتانیاهو نخست وزیر اسرائیل در مجمع عمومی سازمان ملل به زیرنویس فارسی:  @News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72291" target="_blank">📅 09:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72290">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de7db87608.mp4?token=Ka_Y-UvLxaai0nlCfiI-lscVu5NlqH0KPfGlceANNWWyoedbCHuUqnIfCpJGDUKMDgw0qQmHdqa-V5vOeHLux6hXXeF6tCT7RCHlJTIpv3zNyXgXQhFZnA76BJceoMhy5q4A4VRi_5Z-7eyhzhcfY6tJb9vcrx8sUJDZKfaz-lApnqGHYXOWPrOXNPDu9J23hx3qvNncoF6Y71EZ6WUTORtss5L0YU2Cr_K7cfDyx8J00lt7AYpq9sdWr-LB86DNDDblHTb2Qkb5EUxAPGh1jUi36_TqCFO9m9gJBPt_t-SQfpk9ZezHV2Rrd0HWg32_McCT7S4KQrh14t1KOiGj7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de7db87608.mp4?token=Ka_Y-UvLxaai0nlCfiI-lscVu5NlqH0KPfGlceANNWWyoedbCHuUqnIfCpJGDUKMDgw0qQmHdqa-V5vOeHLux6hXXeF6tCT7RCHlJTIpv3zNyXgXQhFZnA76BJceoMhy5q4A4VRi_5Z-7eyhzhcfY6tJb9vcrx8sUJDZKfaz-lApnqGHYXOWPrOXNPDu9J23hx3qvNncoF6Y71EZ6WUTORtss5L0YU2Cr_K7cfDyx8J00lt7AYpq9sdWr-LB86DNDDblHTb2Qkb5EUxAPGh1jUi36_TqCFO9m9gJBPt_t-SQfpk9ZezHV2Rrd0HWg32_McCT7S4KQrh14t1KOiGj7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احسان کاظمیون فعال اینستاگرامی، یک هفته با یک پیج فیک دخترانه با پیمان اکبری، مجری سپاهی صداوسیما توی تله انداخته!
آخرش هم باهاش تماس تصویری می‌گیره و پیمان وقتی می‌بینه طرف پسره، خشکش می‌زنه
پیمان اکبری همون مجری حکومتی بود که بابت اعدام ها از اژه‌ای تشکر کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72290" target="_blank">📅 09:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72289">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72289" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBe
t
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72289" target="_blank">📅 01:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72288">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWuGdELYEXKuDPjL1b31UcelkZBJ0Q5BO5Rj6-8GNVj25VmdkiJA2vbil6mGGM7D6H1Q81k888YxhvB8Z8PjGuNUIX_B7mZYs72idYQN5q_Rg3gPOOaCtKUDwhV3oXOr2UTka8_T5pgDysTkEO8b2EZQXjlTk7UQFHG6t1V8kyy5tbWtXzEOjLLceAKjuBe4pGr-JS4a6Q4uM7uh3qOR-HUy4uBvwDRhy81Ad5jo_5y4QzGi8MK3ukOQhZ9ysNU8x6dIVcRxlD4TVS19BJaXxSsOSHr1BXAh7nMwxiDcBZqh_bceIXFpLP2fw2YzDsasJosApWW8f24YS2hEzVbxyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72288" target="_blank">📅 01:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72287">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UNhrk3sJ4peTDKE3-A9kpizubArJlKS6DZvN_st11tAwdKfufLrUjVvh1HtvOc2s10XEuzYGRz_ppFItTrj8UjceapZ7LzsdqVG2a0F1b6yybmi1WKQY5ESlbfF0UHmB2pHBrTeI083r9B0IZAHctK8abJBGrs_3onsIbG7utFNQdTaRL-XJb7O9p4biGLZfNFU6Pw0ol9QaZC350NXImw6bsT0BFrkib7VI679KIQ5YCKJUMoMr_TJATC_BPlCfwS9U1JBXatA4jLuWkj-U7WNtYUEHLdp84F1y1BMOVi2Kp01kp_CO77IkjvtmfOVE6LuIU64b_f_Aj4k1aGzBvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه توی ریاضیات و بخش توابع مشکل داشتین؛
این عکس به بهترین شکل تابع f(f(x)) رو نشون میده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/72287" target="_blank">📅 01:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72286">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">صحبت های عباس عراقچی در نیویورک:   طرح هفت روزه به طرف آمریکایی ارائه شده و اگه بپذیره شرایط رو از همین فردا شروع میشه. در روز ششم تنگه هرمز باز میشه و روز هفتم هم گفتگو ها برای رسیدن به توافق نهایی آغاز میشه. توپ در زمین آمریکاست.  @News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/72286" target="_blank">📅 00:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72285">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0dbcfd0ec.mp4?token=MV1BAK7d-eUGZp_vbajZ6D-CYo2FRvPDMOBw8NQ9JPEomFhYsWvdTFkTQzPmB1KvLQ4_CkfHAd3d3-gvCB8hED1H0_oh6gpusVZYyXKqvhqICr8Iz61Cc6UbgJSfgglGN33qQm5VfXl-nyc00OqyN2DlTZ8te9s6A3KhT76mqQL3zEhhZ2d4n-axVOH32tdVCpApjfsTCTBexfV58hF9Ja8i-IhW69QaJjmeryRV1ZKUp3ulRFAGSyv1eUu9pIw1JRoKpsRz_-Gi2Q_43JLl1JeWTeUflVgDqPVRwOugrxtKtmGn-Y_oZ-ELp6Nc5S7jw7Agirzlelq7pipbZ1QYPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0dbcfd0ec.mp4?token=MV1BAK7d-eUGZp_vbajZ6D-CYo2FRvPDMOBw8NQ9JPEomFhYsWvdTFkTQzPmB1KvLQ4_CkfHAd3d3-gvCB8hED1H0_oh6gpusVZYyXKqvhqICr8Iz61Cc6UbgJSfgglGN33qQm5VfXl-nyc00OqyN2DlTZ8te9s6A3KhT76mqQL3zEhhZ2d4n-axVOH32tdVCpApjfsTCTBexfV58hF9Ja8i-IhW69QaJjmeryRV1ZKUp3ulRFAGSyv1eUu9pIw1JRoKpsRz_-Gi2Q_43JLl1JeWTeUflVgDqPVRwOugrxtKtmGn-Y_oZ-ELp6Nc5S7jw7Agirzlelq7pipbZ1QYPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های عباس عراقچی در نیویورک:
طرح هفت روزه به طرف آمریکایی ارائه شده و اگه بپذیره شرایط رو از همین فردا شروع میشه.
در روز ششم تنگه هرمز باز میشه و روز هفتم هم گفتگو ها برای رسیدن به توافق نهایی آغاز میشه.
توپ در زمین آمریکاست.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/72285" target="_blank">📅 00:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72284">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55143aaecc.mp4?token=aRTPAu0IfYapgYApF_TYQdmZEpFE0AOObKCmVaXazrtYwCp7bwaKOrBcE8SMaQHtoPail1cXwEKsNavbq4_bu9xfukAWaE5hdDC6BB1aVuzDZC4bpCFJ8UNSJ6hV04MP__B7xIal2Pmfr0osDvyrGPyJp1cGvhnEGqzQrcTlqrtAZrqsWvg6YC9bSUdsNf7CW_gI0ybwdmL319A7sFWnxR6swx3_0_cHJEE-4q5mOxlM9xhTgbkv5owopHMNKiYWdWIGO2SNSyjuoxAR55twAne83uSCKHijgDKv3acD10StLVNZrHO0AqOYdtit8eSMMQ17pdBpz4r69UI3g5l9UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55143aaecc.mp4?token=aRTPAu0IfYapgYApF_TYQdmZEpFE0AOObKCmVaXazrtYwCp7bwaKOrBcE8SMaQHtoPail1cXwEKsNavbq4_bu9xfukAWaE5hdDC6BB1aVuzDZC4bpCFJ8UNSJ6hV04MP__B7xIal2Pmfr0osDvyrGPyJp1cGvhnEGqzQrcTlqrtAZrqsWvg6YC9bSUdsNf7CW_gI0ybwdmL319A7sFWnxR6swx3_0_cHJEE-4q5mOxlM9xhTgbkv5owopHMNKiYWdWIGO2SNSyjuoxAR55twAne83uSCKHijgDKv3acD10StLVNZrHO0AqOYdtit8eSMMQ17pdBpz4r69UI3g5l9UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بمب‌افکن جدید «بی-۲۱ رایدر» (B-21 Raider) ایالات متحده، پرواز آزمایشی خود را بر فراز کالیفرنیا انجام داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/72284" target="_blank">📅 23:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72283">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خبرگزاری فارس به نقل از یک منبع آگاه ایرانی، گزارش‌های «اکسیوس» و «الجزیره» درباره دور جدید مذاکرات ایران و آمریکا را تکذیب کرد و مدعی شد که هدف اصلی این گزارش‌ها، تأثیرگذاری بر قیمت نفت و ایجاد ثبات در بازارهاست.
این منبع همچنین ادعای الجزیره مبنی بر اعزام کارشناسان فنی ایران به نیویورک برای شرکت در مذاکرات را رد و این گزارش‌ها را نادرست توصیف کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/72283" target="_blank">📅 22:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72282">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09eda15604.mp4?token=mbfpL0vAwvf66b8CGNv3js_pUeGCZwSnb3Mi5EknUD1fxSfLt6B55qwn3_x0BJBe5Xpkw7VUbD7QJRpDltgvqRupflLWyv3u8dkL-0om3NTbb8DJw1nz2mQmBit0eP9TBjJ9aQ5cJOuDZ299M44lSA3coO6pmZILReCbB0DqZMxHbxgVXPraBkVijh3CEnm8lh8GGxvw9C7OSTXaBP7kmuF4Umz4ebmCPyhmcvvx6zV0KnsuUMHagsvOvaBXYAfvUUeo9mBK-fRP9VCZfaLZpors4qUXLVZqMv1uj_9WjULv9yPKpJ6fkXUshnFx-G21yBhdRi3ghXRMOReG15dfXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09eda15604.mp4?token=mbfpL0vAwvf66b8CGNv3js_pUeGCZwSnb3Mi5EknUD1fxSfLt6B55qwn3_x0BJBe5Xpkw7VUbD7QJRpDltgvqRupflLWyv3u8dkL-0om3NTbb8DJw1nz2mQmBit0eP9TBjJ9aQ5cJOuDZ299M44lSA3coO6pmZILReCbB0DqZMxHbxgVXPraBkVijh3CEnm8lh8GGxvw9C7OSTXaBP7kmuF4Umz4ebmCPyhmcvvx6zV0KnsuUMHagsvOvaBXYAfvUUeo9mBK-fRP9VCZfaLZpors4qUXLVZqMv1uj_9WjULv9yPKpJ6fkXUshnFx-G21yBhdRi3ghXRMOReG15dfXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاید براتون سوال باشه چرا به یه جمع دخترونه میگن خانوادگی ولی به یه جمع پسرونه میگن مجردی:
دیروز ، رامسر به سمت جواهرده
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/72282" target="_blank">📅 22:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72281">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2600d0ba66.mp4?token=iis5FTvExOwlvMcCUlZc03RNQ2-zw0Sv0GBsmYJspAj9lqyJZl_kNFq2_XhhOnrZM8HQhytKwZj2pc8FVJ1_NGpYoLf36uKmG1DObf1qNfX-sYhLTaccHlbvWFCFmwDWUVEZKTiBiHnnXQpexSdFM46sz-WYRWSDiSPL9sgSQBVwyk37GK5GiJQzuh2vk7nMfE29bW0Nt6mqwWisMiMlQz9Vm7NiWZ7HgSGTGJHwfUwOBbe3SVv04yXylasu8kRRoDpGoXjxaPNPJkGzBQa4H0P-ToeP1hC_LOBub0m4h3PWuGIkjUmh823FVHSlxrQJyGimSpo3_RYpGe3HKxqLXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2600d0ba66.mp4?token=iis5FTvExOwlvMcCUlZc03RNQ2-zw0Sv0GBsmYJspAj9lqyJZl_kNFq2_XhhOnrZM8HQhytKwZj2pc8FVJ1_NGpYoLf36uKmG1DObf1qNfX-sYhLTaccHlbvWFCFmwDWUVEZKTiBiHnnXQpexSdFM46sz-WYRWSDiSPL9sgSQBVwyk37GK5GiJQzuh2vk7nMfE29bW0Nt6mqwWisMiMlQz9Vm7NiWZ7HgSGTGJHwfUwOBbe3SVv04yXylasu8kRRoDpGoXjxaPNPJkGzBQa4H0P-ToeP1hC_LOBub0m4h3PWuGIkjUmh823FVHSlxrQJyGimSpo3_RYpGe3HKxqLXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روسیه در حال اتخاذ تدابیری برای محافظت از پالایشگاه‌های نفت در برابر پهپادهای اوکراینی است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/72281" target="_blank">📅 21:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72280">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">یک مقام ارشد ایرانی به رویترز:
ایران حتی در صورت پذیرش پیشنهاد تهران برای بازگشایی تنگه هرمز از سوی آمریکا، هیچ‌گونه امتیازی در حوزه هسته‌ای نخواهد داد.
تنگه هرمز تا زمانی که شروط ایران برآورده نشود، بسته خواهد ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/72280" target="_blank">📅 20:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72279">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecb62dc836.mp4?token=tNa9tQucLrpPTwN6V2WxCqbVKq4Wpieac3h6tALerkyxOXfIcMl0R2RZb9rrV-zL33YnHY2P62qq4ukE0RyFAuI5m6W-5L4UGUnPyCs0fDmHMwp745sVqV9hvk4D_Ad0O7ZA2QNHvQjWz2TjuV-iD2i4hdawOn5GVgaJiaK2BbM-WrOMqL2nUZbccmpfo9PqFsWg8OB-s1xz8BCTJluW8a7DhGc6U6ZbOmbhM5OBhdkaQcNk66bEDdTTg2Yd_6gBjQasVyVMblTI-RU0Xx_ra_K5veGcYtuLYtJ8htIFWoJXnSrzC2zWBKp3YiqJf4s1gaEAPmndQKEBFzzPRufPIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecb62dc836.mp4?token=tNa9tQucLrpPTwN6V2WxCqbVKq4Wpieac3h6tALerkyxOXfIcMl0R2RZb9rrV-zL33YnHY2P62qq4ukE0RyFAuI5m6W-5L4UGUnPyCs0fDmHMwp745sVqV9hvk4D_Ad0O7ZA2QNHvQjWz2TjuV-iD2i4hdawOn5GVgaJiaK2BbM-WrOMqL2nUZbccmpfo9PqFsWg8OB-s1xz8BCTJluW8a7DhGc6U6ZbOmbhM5OBhdkaQcNk66bEDdTTg2Yd_6gBjQasVyVMblTI-RU0Xx_ra_K5veGcYtuLYtJ8htIFWoJXnSrzC2zWBKp3YiqJf4s1gaEAPmndQKEBFzzPRufPIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بی‌بی نتانیاهو یه شوخی برا میلی رئیس جمهور آرژانتین کرد و اونم یهو زد زیر خنده
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/72279" target="_blank">📅 20:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72278">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c6656758c.mp4?token=DibJB539I7fl8gvv3imP8C78-1aAtZw5zRUxA652MzG4bSDOHZ7DninwPidSAA0_AcfI39ueo_SVHt7DfCHf3mUDSlrjwJ2EnD_iOcwetpNGd46fRdbCXVjh9jwpCstyRHBIZYXnXY2VKMellZZR3cBGiNE9KySniYjXeSa3anv_3kc8wAZl2xWTWErVmwTdv6vRM8IW2z_9xUglMs3zY-bnaQYzUFSuNvojBQKOZgtCpiUdgulUkzF4TXMTvQocaOvUxpxeVjH-s8HqgXS3n7YiEq0whbH92n2aQGkWcGLA3GgGbCTxB2k0Jk_bTw5nWVcKOHVbFiC6t-ZUvwsBuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c6656758c.mp4?token=DibJB539I7fl8gvv3imP8C78-1aAtZw5zRUxA652MzG4bSDOHZ7DninwPidSAA0_AcfI39ueo_SVHt7DfCHf3mUDSlrjwJ2EnD_iOcwetpNGd46fRdbCXVjh9jwpCstyRHBIZYXnXY2VKMellZZR3cBGiNE9KySniYjXeSa3anv_3kc8wAZl2xWTWErVmwTdv6vRM8IW2z_9xUglMs3zY-bnaQYzUFSuNvojBQKOZgtCpiUdgulUkzF4TXMTvQocaOvUxpxeVjH-s8HqgXS3n7YiEq0whbH92n2aQGkWcGLA3GgGbCTxB2k0Jk_bTw5nWVcKOHVbFiC6t-ZUvwsBuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روزهای ۲۴ و ۲۵ سپتامبر (دیروز و امروز)، افزایش فعالیت‌های ترابری ایالات متحده در ارتباط با خاورمیانه مشاهده شد که شامل هواپیماهای ترابری و پشتیبانی آمریکا—مانند مدل‌های C-17، C-5M، C-130 و KC-135می‌شد...
تدارکاتی در جریان است!
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/72278" target="_blank">📅 19:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72277">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/332f3ab7c2.mp4?token=GoneHh4WTtIvLRRGoiXDh4G1IYQVlV9KKYh9xfJzXUnUieWXcmKiAM_8OlqmtuX6nJtrnmDhb5cUpcam86Di3sRPED7_6sEjkklr1cY-8HLVciWh3KJ0Ve5qmRCNqCZWczHm2382FGWhnzrr0qWqOXkUs57DJm8ngpHqFfUn4yElDIlC1taJMtSF-cGEXjf0LStpcPKY5E9JsKzU0jEcIrPN3qVL4WM7tVsC-H9rVpm1o0coLcQlbtvKYKq9timjGyhI1TIPxt1Gl8IcR126a-a60UGEF5R6lNHLmh_YwtqtpIeYYuHuc68NEOZDOFsDHeoLaBB9bl-p140Gr5QieQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/332f3ab7c2.mp4?token=GoneHh4WTtIvLRRGoiXDh4G1IYQVlV9KKYh9xfJzXUnUieWXcmKiAM_8OlqmtuX6nJtrnmDhb5cUpcam86Di3sRPED7_6sEjkklr1cY-8HLVciWh3KJ0Ve5qmRCNqCZWczHm2382FGWhnzrr0qWqOXkUs57DJm8ngpHqFfUn4yElDIlC1taJMtSF-cGEXjf0LStpcPKY5E9JsKzU0jEcIrPN3qVL4WM7tVsC-H9rVpm1o0coLcQlbtvKYKq9timjGyhI1TIPxt1Gl8IcR126a-a60UGEF5R6lNHLmh_YwtqtpIeYYuHuc68NEOZDOFsDHeoLaBB9bl-p140Gr5QieQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ به شی رئیس جمهور چین میگه عکس روی دیوارو ببین؛
ما خیلی برات احترام قائلیم!
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/72277" target="_blank">📅 18:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72276">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f168bb0c29.mp4?token=AlNvLkT3yuw7jmWhHi2EzDy6wZhadRVia4UU4kGvQerOaHvOUYJXRlu_yyH7byleIuQ6V2ReNzMQMj8Qp7AdUmVhL3SLXMa__Zigo7sBz4xax32TT4DBInVTVH0BmD912U1E3JC4H7WAqkMTyIb-ncSOOVl0QlVSCRTagZ4T9d9qEl3rxG6w9Rf7561Oq3SydsdVnD__ropjfPB4rWB-CCYziHx-Q3fhaJhHVTkRuj6LY-iNd69joK7K-zyyOXoUIgJIvZaENWYKPQZRYBH5sDHiH0-kD4kalM1kH6CxBa4N6HirPgnUzO4Vet-R8g6VPsLgP9klx5R3TauV-R7-EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f168bb0c29.mp4?token=AlNvLkT3yuw7jmWhHi2EzDy6wZhadRVia4UU4kGvQerOaHvOUYJXRlu_yyH7byleIuQ6V2ReNzMQMj8Qp7AdUmVhL3SLXMa__Zigo7sBz4xax32TT4DBInVTVH0BmD912U1E3JC4H7WAqkMTyIb-ncSOOVl0QlVSCRTagZ4T9d9qEl3rxG6w9Rf7561Oq3SydsdVnD__ropjfPB4rWB-CCYziHx-Q3fhaJhHVTkRuj6LY-iNd69joK7K-zyyOXoUIgJIvZaENWYKPQZRYBH5sDHiH0-kD4kalM1kH6CxBa4N6HirPgnUzO4Vet-R8g6VPsLgP9klx5R3TauV-R7-EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده با این شرح:
مردی در مشهد با انداختن 100 میلیون از امام رضا شفای همسرش رو طلب کرد ولی همسرش شفا نگرفت و درگذشت و اونم برگشت تا 100 میلیون رو پس بگیره
😑
😑
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/72276" target="_blank">📅 18:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72275">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72275" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72275" target="_blank">📅 18:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72274">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNjP_1fpEY4-2c0f9_tWi-r9Y9SLsUbm3JfsVle3IJz2hIWwORGX-JpVqKK0ugtE8QDJ3DtwFfjRzROwi2uOg0gyp6d-tsZlleP9ejQJOLxD_nt_kgNNGeBK6qwPzg7Vbm9Og2Gndq8k45rwiHr3wY93M3X2KoTQPiVKScmOSwFCm9ena4bzkmN16sv8uJ0o-EQiH2NPv6PS9mpb3GnjOiSyx_WNnsySKu23EOuEefg4ufbOFYiZqcdt9_aU3b5zAx0Q4H7WJ6wRnmHPrZKTVC_mOAcL169uPPuGRzi-t4JXieDodPqkUsEJGNzOIdKo5Ouvxk8cKDvClpG8BXgrkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز فرانسه
🆚
ترکیه
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
فرانسه: ۳ برد، ۲ شکست و ۱۲ گل زده
ترکیه: ۳ برد، ۲ شکست و ۹ کل زده
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
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72274" target="_blank">📅 18:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72273">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9246e73cb.mp4?token=KOilM1NmWUiSfixPLZ1dBD0geIDkpOUitzGbQC_Vx4z5Y_aFzQGNS3qSfQsf9jxdkD-jCRG8zpdnweOyRvarTh-_d2mRcUlAgL9tNjZkrsgCqi8U4bblPReiuUnWdYkkAfug5Ys-nEN1tiZ5Bjaon9138xWyHcwdgQP-ZmQJ0viSohkAoA63Mgy_c1nXNilv1MpLv6X66gKkxS-tIIMZUbfzVE68I4UGBFdXT37y4HlScJVxsGY0FeVd0bPT3jkQdVpV0RuauW8utyIr_pGynj6ZMJmcrPBMNBqgtGrtvgmyb-WMe2t_3DHqITpKdOLnO6O3Vgrhi8zaIFs7Vpw9Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9246e73cb.mp4?token=KOilM1NmWUiSfixPLZ1dBD0geIDkpOUitzGbQC_Vx4z5Y_aFzQGNS3qSfQsf9jxdkD-jCRG8zpdnweOyRvarTh-_d2mRcUlAgL9tNjZkrsgCqi8U4bblPReiuUnWdYkkAfug5Ys-nEN1tiZ5Bjaon9138xWyHcwdgQP-ZmQJ0viSohkAoA63Mgy_c1nXNilv1MpLv6X66gKkxS-tIIMZUbfzVE68I4UGBFdXT37y4HlScJVxsGY0FeVd0bPT3jkQdVpV0RuauW8utyIr_pGynj6ZMJmcrPBMNBqgtGrtvgmyb-WMe2t_3DHqITpKdOLnO6O3Vgrhi8zaIFs7Vpw9Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی گسترده در یک کشتی حامل خودرو با پرچم یونان در شمال جزیره میکونوس
این کشتی ۲۹سرنشین و نزدیک به۲۰۰دستگاه کامیون و خودرو داشت
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72273" target="_blank">📅 17:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72272">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a9af590b4.mp4?token=o5n924nvxeLVxKw60EP2-Dkl_XtVkKODJCf-kD9rub7X-HHhgqyrxIRRwM8ujKErE-z3U8wlv1nW9W5zxbJLKF1zJo1Yn4UCre4hqzc5L6D-fySOSs4mrqeUzpSfCLpgCzQjMM6lnZKqC8HZ05FVgPY8l7NQemmQHhHDRKK7dFNrD4BoNRgEoAo3il3Q6xajbLpzkLXGqQrZGUefxwJpFge4VNahhx1ojl5plrENeQ0XUsG8Dazkk0cTmwhjkoeSyBT3U_O6xi3QMA6_9BdxZY4usXVoxQv36tBByuAGmS2v4P1q1o53HoHtM2dGyykKbqL7lGME2sVw3sgQqFSQEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a9af590b4.mp4?token=o5n924nvxeLVxKw60EP2-Dkl_XtVkKODJCf-kD9rub7X-HHhgqyrxIRRwM8ujKErE-z3U8wlv1nW9W5zxbJLKF1zJo1Yn4UCre4hqzc5L6D-fySOSs4mrqeUzpSfCLpgCzQjMM6lnZKqC8HZ05FVgPY8l7NQemmQHhHDRKK7dFNrD4BoNRgEoAo3il3Q6xajbLpzkLXGqQrZGUefxwJpFge4VNahhx1ojl5plrENeQ0XUsG8Dazkk0cTmwhjkoeSyBT3U_O6xi3QMA6_9BdxZY4usXVoxQv36tBByuAGmS2v4P1q1o53HoHtM2dGyykKbqL7lGME2sVw3sgQqFSQEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیئت اسرائیلی در سازمان ملل اسامی کشور هایی رو که حین سخنرانی بنیامین نتانیاهو سالن رو ترک کردن یادداشت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72272" target="_blank">📅 17:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72271">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/327c73b8a8.mp4?token=KDva-gpxVFybpsgElON8JAMMlAoX22Gr82AHUAYqDCwtVuL1myFlFolwtodod7JzZM9zKr7CVjnCsIZoheo3_x2Z60KFbDfS19pWJ9dY6PpR4Fc6silowv6r7yjEBqn3Xgnbgzfc6OKnH19-claUIhOFhvNT6D0pAjoW_h6nwmJ6GVtQ4vxcK-9hFjaS8lbHGJiT4xjAZBCBBUUjwlsmtf9M7z64JSKLnunucsGWmMysgvYnytd34u1Ydw0AcJ9VGOqkFShD6pdDrx9C51IyIe-33FooywWCrDdacfPC8eNmz4mr4Rzok_pWBn6uIr1lRcjubAmqXf2eJemj6KK8SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/327c73b8a8.mp4?token=KDva-gpxVFybpsgElON8JAMMlAoX22Gr82AHUAYqDCwtVuL1myFlFolwtodod7JzZM9zKr7CVjnCsIZoheo3_x2Z60KFbDfS19pWJ9dY6PpR4Fc6silowv6r7yjEBqn3Xgnbgzfc6OKnH19-claUIhOFhvNT6D0pAjoW_h6nwmJ6GVtQ4vxcK-9hFjaS8lbHGJiT4xjAZBCBBUUjwlsmtf9M7z64JSKLnunucsGWmMysgvYnytd34u1Ydw0AcJ9VGOqkFShD6pdDrx9C51IyIe-33FooywWCrDdacfPC8eNmz4mr4Rzok_pWBn6uIr1lRcjubAmqXf2eJemj6KK8SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک پزشک کودکان : امروز تو تهران ی دختربچه ی ۴ ساله ی بسیار زیبارو آوردن پیشمون با خون ریزی شدید واژن، معاینش کردیم و کاملا مشخص بود بهش
تجاوز
شده، از پدرش پرسیدیم میگه با واژن افتاده رو جاروبرقی درصورتی که دروغ میگفت و مادر بچه وقتی رفته بود بیرون این کودکو با پدر کودک و دوست پدرکودک تنها گذاشته بود...
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72271" target="_blank">📅 16:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72268">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mduyuWXcM7id6tOpxfgibuSy2IHL3Punfk4DJduRs_voz9TN-ecNy3L_5_1zf-9JEbuZg6dhijtMboRFqNtVJO1IELGM_MncybQSIhajZ_9d711KEo1C6gxYdgo59Yp22BjvaDkLHnRhJM5tCuAC3GHAVu6-xn2MLZl2GPPOuGLNz-OFr-v-VuQtyyKBskp6D_7m5z0aN7LvMqOeZonXa3Hv4LNG5pH5cPG4fyiwQKYOWvitUEbeNObO1tI0KCnhIcjPULUNYzQ3dDaDbf0MXuS_oKHV_9HJUZyOLxiS6kGXW-980QtPAqDR0Zh7cJqM1LeNDB2_DzoPByPnCAuFiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c33b2c3d47.mp4?token=j9X2UZsT8oz0Pb7QHdos38ouT35xmnDBC8lzQGKCrQ1nkZk_piGWrhyZnitlt81iVhJaHg-XlooPI5u3zzpM6y4jtrTLBZUigAv1snb3jFsddDbueZY9QBcaa1R2-N_bv9sCTPIgepnt4eiTQZt12khEHPAwRpqmQ5pv6J1HR7U1cOUdvCGLa9vObQsI-H5ZJGUX668Sz-BNqnU5TFH78XKwidF-_NjEkEBhONvQwWeRSjVC-oXS8ZG20CXn46Ri1l3ysvzsWjLb3Ckn1UtFsFocSnj0rQRhMhcbllnT_-oGLIZPmihPM7xl9pLUaCYCLnEZVdj4X218r_F2WfG9WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c33b2c3d47.mp4?token=j9X2UZsT8oz0Pb7QHdos38ouT35xmnDBC8lzQGKCrQ1nkZk_piGWrhyZnitlt81iVhJaHg-XlooPI5u3zzpM6y4jtrTLBZUigAv1snb3jFsddDbueZY9QBcaa1R2-N_bv9sCTPIgepnt4eiTQZt12khEHPAwRpqmQ5pv6J1HR7U1cOUdvCGLa9vObQsI-H5ZJGUX668Sz-BNqnU5TFH78XKwidF-_NjEkEBhONvQwWeRSjVC-oXS8ZG20CXn46Ri1l3ysvzsWjLb3Ckn1UtFsFocSnj0rQRhMhcbllnT_-oGLIZPmihPM7xl9pLUaCYCLnEZVdj4X218r_F2WfG9WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پهپادهای اوکراینی به چندین تأسیسات صنعتی در روسیه، از جمله پالایشگاه نفت «پرم»، کارخانه «ایسکرا» در اولیانوفسک و تأسیسات «وورونژ‌سینتزکااوچوک» در وورونژ، حمله کردند.
پالایشگاه پرم که یکی از بزرگ‌ترین پالایشگاه‌های روسیه است، در پی این حمله دچار آتش‌سوزی در واحد فرآوری «AVT-5» شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72268" target="_blank">📅 16:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72267">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ارتش اسرائیل اعلام کرد که یک موشک رهگیر به سمت یک «هدف هوایی مشکوک» که بر فراز جنوب لبنان (منطقه فعالیت نیروهای اسرائیلی) شناسایی شده بود، شلیک کرده است.
ارتش در حال بررسی این حادثه است. هیچ‌گونه آژیر هشداری در شمال اسرائیل به صدا درنیامد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72267" target="_blank">📅 15:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72266">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a4505de81.mp4?token=tws72cgv2iNWxz3GN203xCbnB-ufnMU9EdYfkNicO4NCTnSPUjFGWmnpiwXFbI6taosrizf2jEzlqOYEmAluIs-aq8OIvss861ADrbc688579NG24WVzpT9jzTcdnm1SFJz9XS40U0AIAdgBwgPNNDYWcc3f3m3P8we2BXfhTggFyTYuU4u-o6BrWq6cVEpjT_aIhsIaZua6tWznQhcy6wPxMAPy7WxqtkOjqUFyyloS0xZLv2i2Tzrx-3L-SmOfSZtwdgyIAJF9BlKjbmc1DzX4SZxssC54QWOWUliCHDiexh5Xd9hvybQBf0eUSPP3ma5kDsw0fEDhJFXfxErH7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a4505de81.mp4?token=tws72cgv2iNWxz3GN203xCbnB-ufnMU9EdYfkNicO4NCTnSPUjFGWmnpiwXFbI6taosrizf2jEzlqOYEmAluIs-aq8OIvss861ADrbc688579NG24WVzpT9jzTcdnm1SFJz9XS40U0AIAdgBwgPNNDYWcc3f3m3P8we2BXfhTggFyTYuU4u-o6BrWq6cVEpjT_aIhsIaZua6tWznQhcy6wPxMAPy7WxqtkOjqUFyyloS0xZLv2i2Tzrx-3L-SmOfSZtwdgyIAJF9BlKjbmc1DzX4SZxssC54QWOWUliCHDiexh5Xd9hvybQBf0eUSPP3ma5kDsw0fEDhJFXfxErH7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار از پزشکیان پرسید که میخواید بمب اتم بسازید یا نه اونم میگه نهههه نههه اصلا،
بعد بهش میگه اگه بمب اتم نمیخواید چرا اورانیوم رو بردید زیر زمین ۶۰ درصد غنی کردید؟
گفت اونو که میخوایم رقیقش کنیم! یعنی غلیظ کردید که رقیق کنید؟! بمب نمیخواید بسازید؟!
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72266" target="_blank">📅 15:03 · 03 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

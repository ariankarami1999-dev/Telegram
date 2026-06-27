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
<img src="https://cdn4.telesco.pe/file/MsfGKxPucBbE4jpfY9X16yL8FQ5n6TGcND3qN0GOFTl1zRqAo3yps14AhyU6CHLmMhIdJZsPc0iiuTH0Q9UcxrEUXp4hu_aQCiYM_GsOUUim9FoJ6X3wAlkLqBmec62g3V36xiQJC8-iXhrZnLwpy4zoMndgnUrlEM8F-hD8M2epZqb6HKVw2MY6T1mCLzRIIDyrtPEhibvvvoAbEAgrSeW1tv31aID3QIn-Iwpe1gtFg01P03PuFjdEZeadwHnQcS4UQy3MxNNHXyO1Q7Y0t7_5fBm8ktF470-XsJv0tvAA7eho4BY5uRi64600PlBVbmxflyR8YwWHFOV4Rrz4QQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 331K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 17:53:23</div>
<hr>

<div class="tg-post" id="msg-15954">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">علیرضا حقیر(دبیر) :عامل اصلی خوب نتیجه نگرفتن تیم ملی فوتبال ایرانی‌ها خارج از کشور بودن که باید ادب بشن.
@withyashar</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/withyashar/15954" target="_blank">📅 17:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15953">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مسیر های دریایی عبور از تنگه هرمز  شماره ۱ : که ورودی از بالای جزیره لارک و خروجی از پایین آن عبور میکند  شماره ۲ : هم اکنون مین ریزی شده و به شدت خطرناک است شمار ۳: مسیر ایجاد شده توسط آمریکا که سپاه حملات اخیر را در این مسیر انجام داده @withyashar</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/withyashar/15953" target="_blank">📅 17:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15952">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-wQiLrufTALtA_UYWWtpND_MUuAN-ZTHUJZsyfz-_pBVBKHaZT5Xo3DHSxru1vpFgS_oRaS7j85TGzhcFeFPzmjaYycj8cANjGDCO0UhpGglNSF7vnhxTFk57S1joslL1aEZ1UjAPzE8EJUEg-a8NT-OGccKSVC6YbNDd8PaRNBjhSqn_PNmmVtHsTWvcwy5MMV1nEeIIt09_x9asMP1O07DclIOxBDMtUTApvQbHcJZURbYL-f5h0sWZhrfpqIba9jYjpxXi4gxKyLjZjhdqyve-hKITl2ra-JN2f7uPyPEk63nsMc9xDGZ2atvU3Hf4AmibZrYA8nGhrfbC5yug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گل آفساید شجاع : سعید الهویی موقع خوشحالی با سر زده دماغ  هومن افاضلی رو ترکونده @withyashar</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/withyashar/15952" target="_blank">📅 17:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15951">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBPmCgVOtsduxr_uT2BimGII4sJ7oSlMNx2edbhibpfGjn2QjwblKeaTf2rcbwYcPOpcwI8i___7-LU5J4Z9fGCJ6baMqYj7YGb91Mdu1gT7veVG5X7FHaqrJThiLAAotdC2ko4jRts5NabWZijCOpI2d0wtH2JGaDCmrjRiDbF1TkPjGIZxtOWRhRXAHgIS7YMqQwfm8S6XOIvuNy0P9qzxiWJgTE9UMMRJsErUX5L_6bM96cGuAkY9U83he7bX3vFd6Oa1Y_o0mhRv3PJkW_aE6cnrR3TGebfykgKlx-FflSdApu3WSfWhUzqof7tKnGUPaSezS3g3ujrXrKmU6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت پر ریزون الان کرج !! ایالات متحده با ایالات کرج دعواش شده
😂
@withyashar</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/withyashar/15951" target="_blank">📅 17:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15950">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">مسیر های دریایی عبور از تنگه هرمز  شماره ۱ : که ورودی از بالای جزیره لارک و خروجی از پایین آن عبور میکند  شماره ۲ : هم اکنون مین ریزی شده و به شدت خطرناک است شمار ۳: مسیر ایجاد شده توسط آمریکا که سپاه حملات اخیر را در این مسیر انجام داده @withyashar</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/withyashar/15950" target="_blank">📅 17:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15949">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سازمان دریایی بریتانیا: یک نفتکش در تنگه هرمز مورد حمله یک پرتابه ناشناس قرار گرفته است @withyashar</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/withyashar/15949" target="_blank">📅 17:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15948">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6530513224.mp4?token=IIU1bxySOjIlJzHZIhmqlyq_c6toFznUVHXNqmgLsCKQxaMeMJc7tmRyLHAUM8ZbLZSypXgOZ9yf6u1mmMAClqPTYFq0CLWM8qH2I5fo3OMtO5yQVj0St0aXx2QeiLWAA6QGWeqdzZ60BDhA5ZgHUgZJ2fru3er0b53ZtlyxOZU8dfpBwvKPC6GVAAVzRMFW1HOb3IT1JQM5myJNmMvmYEPYmPjJouaPV4oHesTZWhfxInCTVKqcJHaA_gaQgguxbP0TINB8XuSVwXBm-TlbsjxxvthLkOSCs20o1uKBl_q9dEHj8_tt33s7gxwlDMqjI57YRiDQxaex06cvjxdVqjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6530513224.mp4?token=IIU1bxySOjIlJzHZIhmqlyq_c6toFznUVHXNqmgLsCKQxaMeMJc7tmRyLHAUM8ZbLZSypXgOZ9yf6u1mmMAClqPTYFq0CLWM8qH2I5fo3OMtO5yQVj0St0aXx2QeiLWAA6QGWeqdzZ60BDhA5ZgHUgZJ2fru3er0b53ZtlyxOZU8dfpBwvKPC6GVAAVzRMFW1HOb3IT1JQM5myJNmMvmYEPYmPjJouaPV4oHesTZWhfxInCTVKqcJHaA_gaQgguxbP0TINB8XuSVwXBm-TlbsjxxvthLkOSCs20o1uKBl_q9dEHj8_tt33s7gxwlDMqjI57YRiDQxaex06cvjxdVqjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت پر ریزون الان کرج !!
ایالات متحده با ایالات کرج دعواش شده
😂
@withyashar</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/withyashar/15948" target="_blank">📅 16:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15946">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BL2r0V4xOXAHDUdURUPG5ipB2XUowiPC5X5NyEJ8Nk8LQoMz6Ap9YgwkZg6f4mO63hyZLzEZR4VL4j6LSRuuE9b4SgSYb1jXruKQz6D8Vqu1XFG7zbaII66RNPspJm5pRf6-mmLz3yKDb9hBVXk-LtDa5adIdlNHdRg3vHz5VGRkQvt_ql_87DKa6vmGaQy8563Kfz2XIOeDuNj-I-olqWFb9QGwNSOttufBrwI43cSeWY3NkbZq90-hPxvWbB8Gja7rxlB28GmDPj3TIEBtB0s-NUNvB_o09UjgYCIWb5NKKjcxBYIdSCJKoxMiSYDuHnnjSvVdxU1glhmqp44XYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2d33ddf14.mp4?token=Jr1OTBOVLdGRXeYxgeYIkC2tC6Njipb2BzqygsK7Rwh7Vc_Kw4wf_q1-jBhpb_Zw7AYHBHJYkJo8iPk0Mdu_CF1zfwQAET_lL1sBUfv1IyjUZqHLbfdp8TRLmHT4ZhVJ1vd4vIRp8fLIlF0DzENvCf_Xwmc5DuaQrr8zS9sfWJGPgyRiUlwfeU_nJeMEuTEhsj1AwQKyQDJVGwHiSDDOkN_ac0uFow0I2_5c85N_fA9Y_vSIOHJAlvN9FXpmAilJtLSS6-T3pyjI7TkS8tTOYP1qeipB4eKSmj6G1vUZQsTQapfdPzwmwPvsEGme1vFZElvakWiNSN28IhlcFj5inQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2d33ddf14.mp4?token=Jr1OTBOVLdGRXeYxgeYIkC2tC6Njipb2BzqygsK7Rwh7Vc_Kw4wf_q1-jBhpb_Zw7AYHBHJYkJo8iPk0Mdu_CF1zfwQAET_lL1sBUfv1IyjUZqHLbfdp8TRLmHT4ZhVJ1vd4vIRp8fLIlF0DzENvCf_Xwmc5DuaQrr8zS9sfWJGPgyRiUlwfeU_nJeMEuTEhsj1AwQKyQDJVGwHiSDDOkN_ac0uFow0I2_5c85N_fA9Y_vSIOHJAlvN9FXpmAilJtLSS6-T3pyjI7TkS8tTOYP1qeipB4eKSmj6G1vUZQsTQapfdPzwmwPvsEGme1vFZElvakWiNSN28IhlcFj5inQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل آفساید شجاع : سعید الهویی موقع خوشحالی با سر زده دماغ  هومن افاضلی رو ترکونده
@withyashar</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/withyashar/15946" target="_blank">📅 16:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15945">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b788f70cb.mp4?token=JERfNDTSHkqiyqWRzUuSaIe9bE-X3tGJX-3618YNWQYHtWDk1bVmyls6KuaHBIN5EOxw0xgORQSwKzsjRLxYlp4e2QlUagffwzXwch4l69PwrqJkCFp9fk8FEGnF2as9oLrcyGy1PwAXZ1h450QNJ45GkU57V-tNwmPuR6dRiHugyZsIDD1VAhSpHV2yoJlQQOYQhlohTJVTOujwJ5Y4YvOGLPNt0WrcGn-XF2BNQaeNmLETuWbW7sTUsOnHxrhomfSV6Rr9--f66HWeDbTnNO7GvtgqJSSzA_B9Bi7S8aXaEYC5uV624sL185i5AODyGcN3awtQFlrzqbPlbFJnRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b788f70cb.mp4?token=JERfNDTSHkqiyqWRzUuSaIe9bE-X3tGJX-3618YNWQYHtWDk1bVmyls6KuaHBIN5EOxw0xgORQSwKzsjRLxYlp4e2QlUagffwzXwch4l69PwrqJkCFp9fk8FEGnF2as9oLrcyGy1PwAXZ1h450QNJ45GkU57V-tNwmPuR6dRiHugyZsIDD1VAhSpHV2yoJlQQOYQhlohTJVTOujwJ5Y4YvOGLPNt0WrcGn-XF2BNQaeNmLETuWbW7sTUsOnHxrhomfSV6Rr9--f66HWeDbTnNO7GvtgqJSSzA_B9Bi7S8aXaEYC5uV624sL185i5AODyGcN3awtQFlrzqbPlbFJnRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتیش بسیار بزرگ هم اکنون کرج
@withyashar</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/withyashar/15945" target="_blank">📅 16:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15944">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UdKMVptRikl-Pj000wb-Q8_TUXLm1RkGtE_5Ge1PCcSWZ1l4cBWk8ROsdDQjANxgQ9-r9dDAvhIjnRA9ajmRHz67MGk7AsFoPWXzv_5Eg2ATe74IWYOTQqalAQOZv_Q6L-EGEvi8dRUHo-DAc0vI9kUGmeef5dD54y2FsuRiiRWnZgCnxQRlpXsRzUxK2R-HTbcC3OKpSZNH2dJK3oEpH0NMmpesPEYIyalTaBJ-tyFsh8cJcHbyIqm3w34uRiI4Dd4uD8-80d2vPz879vaSxiZdNBZrzqNvf-94eK-7eNEuNa2MMCS_maWs3Qntu_AYmasWWsF7rXBmcGUNd9VRGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیر های دریایی عبور از تنگه هرمز
شماره ۱ : که ورودی از بالای جزیره لارک و خروجی از پایین آن عبور میکند
شماره ۲ : هم اکنون مین ریزی شده و به شدت خطرناک است
شمار ۳: مسیر ایجاد شده توسط آمریکا که سپاه حملات اخیر را در این مسیر انجام داده
@withyashar</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/withyashar/15944" target="_blank">📅 15:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15943">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">محسن رضایی:پاسخ سریع و کوبنده‌ای در انتظار ناقضان تفاهم‌نامه است.
@withyashar</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/withyashar/15943" target="_blank">📅 14:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15942">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/withyashar/15942" target="_blank">📅 14:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15941">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">حمله اسرائیل به النبطیه  در جنوب لبنان.
@withyashar</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/withyashar/15941" target="_blank">📅 14:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15940">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">حکم ضبط اموال ۲۰۰ همتی برای مؤسسهٔ مولی‌الموحدین صادر شد
رئیس‌کل دادگستری تهران از صدور حکم ضبط اموالی به‌ارزش بیش از ۲۰۰ هزار میلیارد تومان در پروندهٔ مؤسسهٔ مولی‌الموحدین خبر داد.
@withyashar</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/withyashar/15940" target="_blank">📅 14:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15939">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خبرگزاری فارس : ۶ نفر از دانشجویان دانشگاه امیرکبیر به علت آتش زدن پرچم جمهوری اسلامی در تجمعات اسفندماه از دانشگاه اخراج و از تحصیل مجدد برای چند سال محروم شدن.
@withyashar</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/withyashar/15939" target="_blank">📅 13:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15937">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">برقراری رسمی تجارت ایران و امارات پس از توقف چند ماهه به علت جنگ
معاون خدمات تجاری سازمان توسعه تجارت ایران از فعال‌سازی مجدد مراودات تجاری میان ایران و امارات از مسیر بندر جبل‌علی به عنوان یکی از مهمترین بنادر جنوب خلیج فارس خبر داد.
@withyashar</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/withyashar/15937" target="_blank">📅 13:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15936">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3GunpkWm4OguEOCHeemP7VcbiEHpq5qh_RHIeYBWfVexJOKsJ6rxrY6Vs6T9KItwRvJVRlfY693DoeXk5sBchbRd8PdUucerXgT51pknMiRPGVzcR2Re34Yjv4oXFPGESGXKz9_3viigbzDk6m5_TMauW9ef5drdtxc0aR9MLn7VZcqPUXr1z-mjXKXzo9EVm_iSf2rtU9zQmeM9ajUd40_SLYRX0RGmGmmZFhYMLO9qvHv0EUo-JfPI-qcb_cL3z-zutrI1IpHgcgHiP_VDJ6fuvUDc_KkfKeOtTdncWVGxbGWeX0FmqrBDYi4dkWUa_7G-5F0lmRHW8HLX93U3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش‌ها از صدای انفجار در تنگه هرمز
🚨
@withyashar</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/withyashar/15936" target="_blank">📅 13:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15935">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گزارش‌ها از صدای انفجار در تنگه هرمز
🚨
@withyashar</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/withyashar/15935" target="_blank">📅 13:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15934">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">بحرین : صبح امروز جمهوری اسلامی به ما حمله پهپادی کرد
@withyashar
🚨</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/withyashar/15934" target="_blank">📅 12:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15933">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1def3414e6.mp4?token=nWHuPYVj33EP_BgizLCGFkP1La8hBFIbmVFRb8_v1SbkjqY-WB5U6pdVDgvIShbNmdMcKGsDxDveVUVsRciW5M72gmX5E9paw-kj7lZhWmdf1puV0kUZwWYWGrusYEkfzOHvQTZUDaen4h1GhtinHOM6CI26iIuE9wmISFDZEQtkxZLv_tF3NRUKrB165OJYtxdPd05iln5AwJWisvzcxbaW9SS56KDg_wHFNIAA80ab6vGfPXbXqtWS91xpSChyev88q8q-yl4bWOp7N6Sg-g8qdipCiTJQ5a1PaYjH0eZGvNbg5JfbGc9qVEWlUZrXFCV9twVeO7cUI3GG2U-JHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1def3414e6.mp4?token=nWHuPYVj33EP_BgizLCGFkP1La8hBFIbmVFRb8_v1SbkjqY-WB5U6pdVDgvIShbNmdMcKGsDxDveVUVsRciW5M72gmX5E9paw-kj7lZhWmdf1puV0kUZwWYWGrusYEkfzOHvQTZUDaen4h1GhtinHOM6CI26iIuE9wmISFDZEQtkxZLv_tF3NRUKrB165OJYtxdPd05iln5AwJWisvzcxbaW9SS56KDg_wHFNIAA80ab6vGfPXbXqtWS91xpSChyev88q8q-yl4bWOp7N6Sg-g8qdipCiTJQ5a1PaYjH0eZGvNbg5JfbGc9qVEWlUZrXFCV9twVeO7cUI3GG2U-JHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو رو دیدم با توجه به لحن و قدرت کلام و گفتن ابتکار در مصاحبه ، خوشحال شدم که این ساعت مردم و خودم میتونیم مستقیم تماس بگیریم و سوالات رو بپرسیم ، ولی الان پرسیدم ازشون و گفتن برنامه از قبل ضبط شده
😕
به هر حال من از هیچ تلاشی برای پرسیدن سوالات شما ، فقط بصورت مستقیم از شخص شاهزاده نا امید نمیشوم و دنبال فرصت دیگر میگردم در نتیجه فکر نکنید که فراموش میکنم و پشت گوش میندارم
🙌🏾
❤️‍🩹
با توجه به اینکه خانم قاضی مراد پیج رو دنبال میکنه ، اول برای ایشون آرزوی موفقیت میکنم و دوم امیدوارم دست کم بخشی از سوالات ما پرسیده شده باشه ، خواهیم دید چه خواهد شد ، دوستدار شما یاشار</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/withyashar/15933" target="_blank">📅 12:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15932">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ارسالی زیاد: یاشار داداش ساعت ۱۱:۵۰ همین الان شیراز صدای انفجار اومد حوالی فرودگاه و پایگاه هوایی شیراز همونجا هم پایگاه پدافندی شیراز هست
@withyashar</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/withyashar/15932" target="_blank">📅 11:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15931">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flqPPE33I0luqc0Zh05a8N2Y_gfkHkL6bwpXTJFWjtzkvXKTvAVk2Zp2DM80bfosLNGx9OXnvGxBw7VgFTMUFVlfGDgBAdU5Ousu-U2R8wDx-kMhO16_rF64YyoQt91muuT47K1St_-qieWT8fYVG8SUK_s9wtsDDvhMZImglLIAGBaxdkngdpNiVhbVmrmyFuxzLXQ2WxiFkHn5uxdksNTMlzeVz5YKlMkX5GdAE0KiX28dCDW6KhHFYPXc0UMfCBzgqHCWELPTRft6IShewnw2UrTAvXd2Rs9ZQSou9zjWtlkinTOiKrqtwRLeVoAJDq69tARH-Lmtnr_EtV-tBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام :  امروز حملاتی را به سایت‌های ذخیره موشک و پهپادهای ایرانی و تأسیسات رادار ساحلی انجام داده است تا به تلافی حمله پهپادی ایران در 25 ژوئن به کشتی باری M/V Ever Lovely با پرچم سنگاپور در هنگام خروج از تنگه هرمز در امتداد سواحل عمان.  سنتکام این…</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/withyashar/15931" target="_blank">📅 11:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15930">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">صادق خرازی : یک سرویس اطلاعاتی خارجی مدعی شده کمال خرازی در بیمارستان هدف ترور دوباره قرار گرفته بود و کشته شد ! وی گفت کمال خرازی را به صورت استنشاقی(مثلاً گاز، بخار یا ذرات معلق)در بخش عمومی ترور کردند
@withyashar</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/15930" target="_blank">📅 10:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15929">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">شبکه PBS News به نقل از یک مقام آمریکایی : ۶ فروند هواپیمای نظامی ایالات متحده، چهار هدف ایرانی از جمله تأسیسات راداری و انبارهای موشک و پهپاد را در منطقهٔ سیریک در ایران مورد حمله قرار داده‌اند!
@withyashar</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/withyashar/15929" target="_blank">📅 10:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15928">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87cfede001.mp4?token=MlLs6EyBLyaWRO9iR1AFlfGXLzcarK3g2CSXkqjxFmnYuVH5epLwv8kiCDTx1lUysLYImSLMUx1e8H8Lv53iM1V7fRhWYhKgchrNCoUiLNQ62AItRcGSh-uHGsD5GO8sqMKTZP8ne3DZPgGQleP9jq-cd0Q9HW5LgVrBJXjFhOqg824Tg1RAOj6IDGo9KIfPz-wqxftXadR32Tg0xxHQtQFUt42F6rV8i2L4aSw9Hh9kv3Nu9TsDjpWMACEavnMXwRhuV43RL30y-4AJ4amHoh-g7H0Bz0HkQiRpyGmTy8kkG8VWLDe5lRYtFmUvFE8GEImaXGr4NX4vdSQ8PtHeYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87cfede001.mp4?token=MlLs6EyBLyaWRO9iR1AFlfGXLzcarK3g2CSXkqjxFmnYuVH5epLwv8kiCDTx1lUysLYImSLMUx1e8H8Lv53iM1V7fRhWYhKgchrNCoUiLNQ62AItRcGSh-uHGsD5GO8sqMKTZP8ne3DZPgGQleP9jq-cd0Q9HW5LgVrBJXjFhOqg824Tg1RAOj6IDGo9KIfPz-wqxftXadR32Tg0xxHQtQFUt42F6rV8i2L4aSw9Hh9kv3Nu9TsDjpWMACEavnMXwRhuV43RL30y-4AJ4amHoh-g7H0Bz0HkQiRpyGmTy8kkG8VWLDe5lRYtFmUvFE8GEImaXGr4NX4vdSQ8PtHeYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون تهران گشت هوایی     Sukhoi Su-24 با دود سیاه معروفش
@withyashar</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/15928" target="_blank">📅 10:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15927">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">داداش ، چون دروازه بان جلو بود اون بازیکن جای دروازه بان حساب میشه
@withyashar
Bro, since the keeper was upfield, that player counted as the goalkeeper for the offside rule</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/withyashar/15927" target="_blank">📅 09:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15926">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95d4769eb6.mp4?token=dZjUXaTuhH_xeEy9LJnZiO9g463Sp2thd643QtqOtT_FjbGQs8cewppPUA_NmBwJ4uRswEiBjdq1lVKm2oHZ_x3Q_cqGQSlqJtzejB5eWB1-VxwDbSFvA4z-11nowSgS-AcH4QY_tcwYk-zYBwpAa6jOMlmds1aDbitVrNE7_jUnMNUBOXdsFwKDlH_xAKiZw-8zLJu9yL6tCXQbfvb7yI0rPAS-QlborLq56Gmvn5sd7FXMSBiaFUT8Wdss_PQul7jdrBMDLK1V301yLw5NfNz29l0zxN_FRfihRnhTXIctTh6ACxEH6seWPAeCjR1LSBoENeqbjhvpFdadXaBo0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95d4769eb6.mp4?token=dZjUXaTuhH_xeEy9LJnZiO9g463Sp2thd643QtqOtT_FjbGQs8cewppPUA_NmBwJ4uRswEiBjdq1lVKm2oHZ_x3Q_cqGQSlqJtzejB5eWB1-VxwDbSFvA4z-11nowSgS-AcH4QY_tcwYk-zYBwpAa6jOMlmds1aDbitVrNE7_jUnMNUBOXdsFwKDlH_xAKiZw-8zLJu9yL6tCXQbfvb7yI0rPAS-QlborLq56Gmvn5sd7FXMSBiaFUT8Wdss_PQul7jdrBMDLK1V301yLw5NfNz29l0zxN_FRfihRnhTXIctTh6ACxEH6seWPAeCjR1LSBoENeqbjhvpFdadXaBo0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/15926" target="_blank">📅 09:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15925">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">تیم ملی دوباره از استادیوم به فرودگاه می‌رود!
بازیکنان تیم ملی فوتبال مانند دو بازی قبل ساعتی پس از پایان بازی خود برای بازگشت به تیخوانا عازم فرودگاه خواهند شد.
پرواز تیم ساعت ۳۰ دقیقه بامداد از سیاتل راهی تیخوانا می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/15925" target="_blank">📅 09:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15924">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">قوه قضائیه: موتورسواری زنان منع شرعی ندارد
@withyashar</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/withyashar/15924" target="_blank">📅 09:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15923">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">در صورت تساوی تیم رژیم جمهوری اسلامی برابر مصر چطور صعود می‌کنند؟ رخ دادن یکی از این موارد کافی است:  1-غنا کرواسی را شکست دهد 2-کنگو نتواند ازبکستان را ببرد 3-بازی اتریش و الجزایر برنده داشته باشد @withyashar</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/15923" target="_blank">📅 09:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15922">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گل مردود شد</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/withyashar/15922" target="_blank">📅 09:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15921">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aarJbs3qtNiLclLUNoPqxuUNbyU78V60HsnNUksm2CqFmEb3RCFVQyuqFoieGMSXQeqH9gMUoljc7-YFKD0rBGtb-bQULBiwcnT8qtuqXQ9CEbtlxXEHQSbctARJS1iirGEQ4vsaaX9CB5XdNCw6BP4Wlm1DqzER5uY53Y9dLHoB6n5UEAfn4IMp8ZyQKnP64kNZXPGU9ck9X0XtThaBTG1prpMHLDXd66tYD7ekEW-BDkYzr3OCGF3ouUT7A0Y1-xL6inj12beWmqKRznbGT0ktqFfSY85q4mBufGBEYURrkLHodms9ixWnnzQJgSrpOvY97MVh7zLLPAGSmIv4PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله اسرائیل‌ به جنین در کرانه باختری
منابع محلی از حمله اسرائیل به روستای «زبوبا» در جنین ، واقع در کرانه باختری خبر دادند.
@withyashar</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/withyashar/15921" target="_blank">📅 08:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15920">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxaumFyHdEpbLY9lpqFRVyWPMzfhBgGvc2y-lDCPIJKJLnFS42EZI9-_Za9aqIWB4Txdez8UMaK6sPIKpr1srMbqjWKv5aQCfFgJjJwAvAjZfuDze8HpbreGKQ_MeemZxfWKbrfN48_jAnkbaZ8DxKm3bZziHGDilDJGIqqVMUawusDvp_4sDVARPKTB7ru3mbSz4S4HcXGemJ1bXGJhqE5QuJhs-V6RwmG51Ab1UbSlqfNYdw23LYmT811Ba6PiDTs0L37AuRvHgq3IBClLtXLhW4UOvyM4QGwYwFbfDW_KpLlOdVMP7YrtAUiP9LS1YFi8br43cshSSY649c5qdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون حضور ۹ سوخترسان در‌ منطقه خلیج فارس
@withyashar
🚨</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/withyashar/15920" target="_blank">📅 08:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15919">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">پایان دیدار و تساوی جمهوری اسلامی ، مصر
@withyashar</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/withyashar/15919" target="_blank">📅 08:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15917">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گل مردود شد</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/withyashar/15917" target="_blank">📅 08:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15916">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گل در‌دست بررسی برای  آفساید است</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/15916" target="_blank">📅 08:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15915">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">گل‌برای جمهوری اسلامی ‌خلیل زاده
@withyashar</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/withyashar/15915" target="_blank">📅 08:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15914">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">در صورت تساوی تیم رژیم جمهوری اسلامی برابر مصر چطور صعود می‌کنند؟
رخ دادن یکی از این موارد کافی است:
1-غنا کرواسی را شکست دهد
2-کنگو نتواند ازبکستان را ببرد
3-بازی اتریش و الجزایر برنده داشته باشد
@withyashar</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/withyashar/15914" target="_blank">📅 08:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15913">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">نیوزلند ۱ - بلژیک ۳ @withyashar</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/withyashar/15913" target="_blank">📅 08:18 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15912">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نیوزلند ۱ - بلژیک ۳
@withyashar</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/withyashar/15912" target="_blank">📅 08:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15911">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2894ab2ba.mp4?token=asXpFr8L80-LKL3isC1zqT6pahyqONwNVzQItreGVRVAXM2W1D7_SaYF8voY41oq9WnyrfdZq4wmALGy19IKbuHgtECM961WA8bYy1X4X45BXfNCCKwio1qE3FJfIZ0GSVAVLd0LQJEFgTgD6p6Ym97hj9jhxhKNs1N9LVCc_QGYUSpWjhNxu2UxJ99PKnqXTthN5KHbU086sGQbwodOx2Fn6kISrASJtNj43PaVExYbD4omhzsXGROXtuWAAPV7fLCGs5UeDb5m74Ih-cWesUr4jIBZ3zo4LRvDVX6tpOo6THmuPVRSjcFfxfolFPmFLbFn5QtQhrEDuMbgAvePgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2894ab2ba.mp4?token=asXpFr8L80-LKL3isC1zqT6pahyqONwNVzQItreGVRVAXM2W1D7_SaYF8voY41oq9WnyrfdZq4wmALGy19IKbuHgtECM961WA8bYy1X4X45BXfNCCKwio1qE3FJfIZ0GSVAVLd0LQJEFgTgD6p6Ym97hj9jhxhKNs1N9LVCc_QGYUSpWjhNxu2UxJ99PKnqXTthN5KHbU086sGQbwodOx2Fn6kISrASJtNj43PaVExYbD4omhzsXGROXtuWAAPV7fLCGs5UeDb5m74Ih-cWesUr4jIBZ3zo4LRvDVX6tpOo6THmuPVRSjcFfxfolFPmFLbFn5QtQhrEDuMbgAvePgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی مرکزی آمریکا (CENTCOM) ویدئویی از لحظات هدف قرار گرفتن شماری از مواضع در ایران را منتشر کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/15911" target="_blank">📅 08:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15910">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">همکنون محمد صلاح تعویض شد
صعود برای مصر‌ حتمی است
لایو : جمهوری اسلامی ۱ ، مصر ۱
@withyashar</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/withyashar/15910" target="_blank">📅 07:54 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15909">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">نیویورک تایمز به نقل از یک مقام آمریکایی : حملات آمریکا حدود ۱ ساعت و ۳۰ دقیقه ادامه داشت.
@withyashar</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/15909" target="_blank">📅 07:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15908">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ونس : ایران توافق آتش‌بس را امضا کرده است. ما به آن احترام گذاشته‌ایم. اگر آنها در مورد نحوه اجرای تفاهم‌نامه اختلاف نظر دارند، می‌توانند تلفن را بردارند.
اما خشونت با خشونت پاسخ داده خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/withyashar/15908" target="_blank">📅 07:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15907">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/144f492601.mp4?token=F7nRc4c6WO981_hbclCOKk6NzfTpIjE5zYox9tCjbNIAWDvHcIEz1ccLsXCLJqg8LO5joxoPEmCBSpTV2MDrXJAyr4F8510U33IWKSuGqwsLvXq0THAuFPBU-TAMOZZ06iBrEbeiHZBLESQ-G_8nLXhwP2W4T8bskbbAfiPeBSJdIZjat0req1SUft127RrP1dShWE3HbBvZUibwQeDCLk2cEahkuek_3Nj1whRpvyxXscyvQcdIGmmXuA1fwsYH8dGxnTt2Ny5KiQQPihxpcNDjih1Qz1lCvxrW-3v50M9nw6Y1pBHTz9pBaOC1YWN2ykFO3uXgxq-mlQraPMvSkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/144f492601.mp4?token=F7nRc4c6WO981_hbclCOKk6NzfTpIjE5zYox9tCjbNIAWDvHcIEz1ccLsXCLJqg8LO5joxoPEmCBSpTV2MDrXJAyr4F8510U33IWKSuGqwsLvXq0THAuFPBU-TAMOZZ06iBrEbeiHZBLESQ-G_8nLXhwP2W4T8bskbbAfiPeBSJdIZjat0req1SUft127RrP1dShWE3HbBvZUibwQeDCLk2cEahkuek_3Nj1whRpvyxXscyvQcdIGmmXuA1fwsYH8dGxnTt2Ny5KiQQPihxpcNDjih1Qz1lCvxrW-3v50M9nw6Y1pBHTz9pBaOC1YWN2ykFO3uXgxq-mlQraPMvSkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درگیری تن به تن نیروی های لبنانی و طرفداران حزب‌الله
@withyashar
یاشار:درک به ما چه ولی ، روزهای جالبی در انتظار لبنان است... من خبر لبنان بدم میاد</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/15907" target="_blank">📅 01:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15906">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سپاه پاسداران: «ما تأکید می‌کنیم که این حملات بی‌پاسخ نخواهد ماند و پاسخی سریع و قاطع در زمان و مکانی که ما انتخاب می‌کنیم، داده خواهد شد.» @withyashar</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/15906" target="_blank">📅 01:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15905">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سپاه :نگارن نباشید  ما با پیک موتوری میبریم براشون ، قااااررررر قاااااررررررر
😂
@withyashar</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/15905" target="_blank">📅 01:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15904">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">مردم : کجا ما تازه برنج خیس کرده بودیم @withyashar</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/withyashar/15904" target="_blank">📅 01:18 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15903">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سی ان ان: حملات ارتش آمریکا به ایران پایان یافت. @withyashar</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/15903" target="_blank">📅 01:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15902">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">یک مقام آمریکایی به «نیویورک تایمز»: حمله به ایران، ازسرگیری عملیات جنگی گسترده، نیست.
@withyashar</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/15902" target="_blank">📅 01:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15901">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سی ان ان: حملات ارتش آمریکا به ایران پایان یافت.
@withyashar</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/15901" target="_blank">📅 01:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15900">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">بیانیه سنتکام :  امروز حملاتی را به سایت‌های ذخیره موشک و پهپادهای ایرانی و تأسیسات رادار ساحلی انجام داده است تا به تلافی حمله پهپادی ایران در 25 ژوئن به کشتی باری M/V Ever Lovely با پرچم سنگاپور در هنگام خروج از تنگه هرمز در امتداد سواحل عمان.  سنتکام این…</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/withyashar/15900" target="_blank">📅 01:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15899">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">به ایست بازرسی بانه سقز حمله شد و ۲ نفر کشته و ۵ نفر زخمی شدن @withyashar
🚨</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/15899" target="_blank">📅 01:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15898">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QNmrv0d2pq_7swp4veCLQS7ytwQK_43XrgZ6AunsFtqX1hZWVwe55wwCSgRqJ4FEVoKe4FI4nkVNY8L4AsdL_apO4Dw6e1aJ5SYpd9zDkvaAuRFDfHaEuyAqxHsORNpyo6Mru0l4dVMFfJKL3rl8QBqanIQ_UQyU97WQyBueO9ykT41mHKg4lcpdxoY2EksTaaQ2TbZM-AeoH8kLzdRcpXCvyM9g4sGq9mMlkx9MuPMNS_jvVfkeAW3QpWEbr5iDNy2LjAaN5x1L4g5E_ogQOg7TqSilaw7vs69wt8weHT_a_8uzRjh-X8GknRQK6hMYrDE1VgJRM1gxUmm6Jep6vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز ششم تیرماه، روز جشن نیلوفر، (نیلوپر) روز دختر در ایران باستانه
@withyashar
یاشار: این روز رو صمیمانه به تمام دختران سرزمینم تبریک میگم، مخصوصاً خواهران عزیزم در اتاق جنگ که واقعاً من را حمایت کردند. مرسی</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/15898" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15897">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/15897" target="_blank">📅 00:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15896">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">آمریکا به یک مکان در مسن قشم بخش شهاب جزیره قشم حمله موشکی کرد
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/15896" target="_blank">📅 00:54 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15895">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">به ایست بازرسی بانه سقز حمله شد و ۲ نفر کشته و ۵ نفر زخمی شدن @withyashar
🚨</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/withyashar/15895" target="_blank">📅 00:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15894">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">به ایست بازرسی بانه سقز حمله شد و ۲ نفر کشته و ۵ نفر زخمی شدن
@withyashar
🚨</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/withyashar/15894" target="_blank">📅 00:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15893">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اعتراضات طرفداران حزب الله به   امضا صلح با اسرائیل‌
درگیری شدید و ارتش لبنان به سمت معترضان در جاده فرودگاه بیروت گاز اشک‌آور پرتاب می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/15893" target="_blank">📅 00:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15892">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">صدای انفجار و جنگنده در مراغه
@withyashar</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/15892" target="_blank">📅 00:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15891">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سپاه پاسداران: «ما تأکید می‌کنیم که این حملات بی‌پاسخ نخواهد ماند و پاسخی سریع و قاطع در زمان و مکانی که ما انتخاب می‌کنیم، داده خواهد شد.»
@withyashar</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/15891" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15890">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">صدا و سیما:ساعت ۲۳:۱۵ امشب صدای انفجار در اسکله طاهرویی سیریک شنیده شد.یک منبع آگاه نظامی علت این انفجارها را برخورد یک فروند موشک در محدوده اسکله طاهرویی سیریک اعلام کرد.
این منبع آگاه نظامی گفت: حدود ۵ ساعت پیش، چندین تیر هشدار از شهرستان سیریک به سمت شناورهای متخلف در تنگه هرمز شلیک شد.همچنین گزارش‌ها حاکی از شلیک دو موشک هشدار دهنده چند ساعت پیش از اطراف کارپان به سمت تنگه هرمز است.
@withyashar</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/withyashar/15890" target="_blank">📅 00:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15889">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">مقام آمریکایی به فاکس نیوز: حملات همچنان ادامه دارد
@withyashar</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/15889" target="_blank">📅 00:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15888">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivnZyLzY8lPzMxVr-lpHHD4nVfTfgn1AiGsSHhvAcyLHqayqiF7JM0p-UsgtizXKE84tFLPsbcEKIv9DrK-VD3T2TW7ws-4VPMl1cageETzDQ-G-BPGzFi0C9EXwdzq0Z_Wa-chs0NIgba6LZ6sR7HPuZI3bBQB1p-H-lXIXI65RDmWCDKdRITJSQKA-32J6wKP3ZaSYpA6n25OJH3z2QT9HlhBOE9clpl2otaTYJEimiljV_qYQOEAqHkvGZP9WdPFec8lr6XK1bD5FCgRfr6UQu7VAFK0n2ZuRt0IfeIjyIOwdofo_Wr5LMZiS2L3Xfe_ZmWlHTAzFPLx-AUdFSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام :
امروز حملاتی را به سایت‌های ذخیره موشک و پهپادهای ایرانی و تأسیسات رادار ساحلی انجام داده است تا به تلافی حمله پهپادی ایران در 25 ژوئن به کشتی باری M/V Ever Lovely با پرچم سنگاپور در هنگام خروج از تنگه هرمز در امتداد سواحل عمان.
سنتکام این حمله را نقض آشکار آتش بس و تهدیدی برای آزادی ناوبری خواند.
نیروهای ایالات متحده به هماهنگی عبور امن برای کشتی های تجاری ادامه می دهند و می گویند که برای اطمینان از رعایت کامل توافق، هوشیار هستند.
@withyashar</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/withyashar/15888" target="_blank">📅 00:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15887">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">خبرنگار آکسیوس : یک مقام آمریکایی به من گفت که ارتش ایالات متحده حملاتی را در منطقه تنگه هرمز انجام داده است.
@withyashar</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/withyashar/15887" target="_blank">📅 00:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15886">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اتاق جنگ با یاشار : همین فرمون بیداریم تا بازی رژیم با مصر …
💥
زارتان زورتانه گویا</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/15886" target="_blank">📅 00:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15885">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">منابع آگاه : سپاه قصد دارد اهدافی در منطقه را در پاسخ به حمله آمریکا مورد هدف قرار دهد
@withyashar</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/15885" target="_blank">📅 23:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15884">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سنتکام: به دستور دونالد ترامپ عملیات محدود ما در ایران آغاز شد در جواب شکست آتش بس توسط جمهوری اسلامی @withyashar</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/15884" target="_blank">📅 23:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15883">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اتاق جنگ با شما : سه انفجار فوق سنگین همین الان سیریک  احتمالا اسکله سپاه سیریک یا اسکله طاهرویی(چون تو یه خطن از این زاویه نمیشه تشخیص داد کدومه  احتمال ۹۰ درصد جواب اون پهپاد های ج ا رو دادن @withyashar</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/15883" target="_blank">📅 23:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15882">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سنتکام: به دستور دونالد ترامپ عملیات محدود ما در ایران آغاز شد در جواب شکست آتش بس توسط جمهوری اسلامی
@withyashar</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/15882" target="_blank">📅 23:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15881">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترامپ: من از شلیک دیروز ایران به یک کشتی در تنگه هرمز خوشم نیامد/ آنها نباید این کار را می‌کردند و به زودی پاسخ ما را خواهید دید
خبرنگار: آیا همچنان معتقدید آتش‌بس برقرار است؟
ترامپ: از این خوشم نیامد که آن‌ها دیروز چهار موشک به سمت یک کشتی شلیک کردند. ما سه تا از آن‌ها را ساقط کردیم. آن کشتی متعلق به متحدانمان نبود، اما به هر حال یک کشتی بود؛ یک کشتی بسیار گران‌قیمت. کشتی سالم ماند، اما کمی آسیب دید. آن‌ها نباید چنین کاری بکنند. بنابراین، خواهید فهمید.
@withyashar</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/15881" target="_blank">📅 23:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15880">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">خبرنگار به ترامپ : شما گفتید ایران آتش‌بس را نقض کرده است. آیا آنها با عواقبی روبرو خواهند شد؟
ترامپ: خواهید فهمید.
@withyashar</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/15880" target="_blank">📅 23:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15879">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گزارشهای شما به اتاق جنگ : سیریک سپاه سرخور طاهرویی رو زد
گزارش ها نظر بر ‌این هست که پهپاد ها هم امروز از همین مکان شلیک شده بود
@withyashar
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/15879" target="_blank">📅 23:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15878">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/withyashar/15878" target="_blank">📅 23:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15877">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/withyashar/15877" target="_blank">📅 23:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15876">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aU-3xV6vUfZnUBlruKk1pI6nkyZhuZ4f8dEP0vH85jymkySmV0Lfka5z3CLFBdbMDwXEOIN6eUyZZpOuoO9mogxwulCZZK2Cl2MOOLsQAYzk1RnT5rMWKzhYExQ6dhoSAxia8CdZ35Sr8nz-9vfwvHXQ71B3LnwCXtWmZFQW_xBz2WYP1FaT76aSG3hW3ZrYk3lBfCfJ3q3HNvFZsGR33aTjvBNRUHFodBZ_dru1EjnMFcAQQRty_Hv1c4h0k3qoba5xenFuRDFkQWUdS8w3GPX1DIUk_Quh5w6GkLcZIZ8MxsuDMVsL_i9HNnVokKeysJwPpBX4KUm7XLdGWWkf3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با شما : سه انفجار فوق سنگین همین الان سیریک
احتمالا اسکله سپاه سیریک یا اسکله طاهرویی(چون تو یه خطن از این زاویه نمیشه تشخیص داد کدومه
احتمال ۹۰ درصد جواب اون پهپاد های ج ا رو دادن
@withyashar</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/15876" target="_blank">📅 23:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15875">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">صدای انفجار سیریک
🚨
@withyashar</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/withyashar/15875" target="_blank">📅 23:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15874">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">هشدار روسیه به سئول درباره تحریکات نظامی با آمریکا علیه کره شمالی
وزارت خارجه روسیه تأکید کرد: اقدامات نظامی کره جنوبی و آمریکا در نزدیکی مرز کره شمالی موجب تشدید تنش‌ می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/15874" target="_blank">📅 23:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15873">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be2d413441.mp4?token=e5LJZx1xllVLm6SYaTEwC1bn51qTKeDJsmMavF8bvBzKRGBaBAHEBWhNyM7j_C-xCMQ7VP1V1eRhRdIjjnrpbxl4O4mLNlX7JcNqL0-fPh7grQMNkO4MkOKHrPwE0OStKx5jcuSKZoWcQoGDEMW1WffM-xfwr_AVGyKDBH08JVyiHDJbeAJNkUOY2AGhX7WjjHfY0IhEQY7NK-4ZJ8cDecIHrAUjXLjpaGWZCjsi6-1X18QuIYkcnAAoupiusmIymIjaaB8GyNZjvE3OQf7-aHs-LYpqxSvhiIzpnV7ofuxUVvETUgw93VABwNZG3FJeaqK7qeRWsKhqxQWyVBgdeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be2d413441.mp4?token=e5LJZx1xllVLm6SYaTEwC1bn51qTKeDJsmMavF8bvBzKRGBaBAHEBWhNyM7j_C-xCMQ7VP1V1eRhRdIjjnrpbxl4O4mLNlX7JcNqL0-fPh7grQMNkO4MkOKHrPwE0OStKx5jcuSKZoWcQoGDEMW1WffM-xfwr_AVGyKDBH08JVyiHDJbeAJNkUOY2AGhX7WjjHfY0IhEQY7NK-4ZJ8cDecIHrAUjXLjpaGWZCjsi6-1X18QuIYkcnAAoupiusmIymIjaaB8GyNZjvE3OQf7-aHs-LYpqxSvhiIzpnV7ofuxUVvETUgw93VABwNZG3FJeaqK7qeRWsKhqxQWyVBgdeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : کشتن سلیمانی یکی از بزرگترین اتفاقاتی بود که تابه‌حال در خاورمیانه رخ داده است.
من فکر می‌کنم خمینی [خامنه‌ای‌] و دیگران در ایران از اینکه من سلیمانی را کشته بودم خوشحال بودند.
چون آنها هم از او می‌ترسیدند.
او یک ژنرال درخشان بود. او مردی بسیار بیمار از نظر روانی بود.
کشتن سلیمانی یکی از بزرگترین اتفاقاتی بود که در خاورمیانه رخ داد. مردم گفته‌اند که بزرگترین اتفاقی است که در ۱۰۰ سال گذشته رخ داده است.
@withyashar</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/15873" target="_blank">📅 22:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15872">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامپ: اخبار جعلی گفتند ایران امروز بسیار قوی‌تر از ۴ ماه پیش است.
آنها برای رسیدن به توافق لحظه‌شماری می‌کنند.
آنها چیزهای زیادی به ما می‌دهند.
@withyashar</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/15872" target="_blank">📅 21:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15871">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/514bc17e72.mp4?token=vDZUA_Zms43b05eC1Vs3_nH7PZud6oq6rQ7xOJoJL_Q4bzLA1q3DmameUdPRda5LzWb3dRKUcdkD_jvCQ6tVvjRR_UviFrnMSSDrKy6tgcYlaXcbhqof7waZJwUhJeicl0CRB0baFSyPPQGhkoOfJam7MLmlzuukPLXiVpC1uAtSsTI5xclkXwBkrhjRv6oDQ0qbUvMsrWy0mp7glA7VxPGLNr4uG13_3i2hASATjD3gpqyB0DozZllZY9NgW9XRLnE3AacdO1mRed3J0MvH-72i1LcLV4gLn2_qlLO3mybIXS0Sgy3igBe1XTraM41BjvtdgNSrc9jd4yK3Fta2Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/514bc17e72.mp4?token=vDZUA_Zms43b05eC1Vs3_nH7PZud6oq6rQ7xOJoJL_Q4bzLA1q3DmameUdPRda5LzWb3dRKUcdkD_jvCQ6tVvjRR_UviFrnMSSDrKy6tgcYlaXcbhqof7waZJwUhJeicl0CRB0baFSyPPQGhkoOfJam7MLmlzuukPLXiVpC1uAtSsTI5xclkXwBkrhjRv6oDQ0qbUvMsrWy0mp7glA7VxPGLNr4uG13_3i2hASATjD3gpqyB0DozZllZY9NgW9XRLnE3AacdO1mRed3J0MvH-72i1LcLV4gLn2_qlLO3mybIXS0Sgy3igBe1XTraM41BjvtdgNSrc9jd4yK3Fta2Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران: دیگر هیچ‌کس نمی‌خواهد رهبر ایران باشد.
آنها پرسیدند: «چه کسی دوست دارد رئیس جمهور شود؟» و همه گفتند: «نه، متشکرم.»
@withyashar</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/withyashar/15871" target="_blank">📅 21:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15870">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d44d4d0504.mp4?token=bu1VdHtRZngljfXkhW1qcpejvQ1LkIJzYyO2mkit9uXuczG0bILEzwP3etl48V0zfbNXN0sHpJcCiOt6RgxTrVw4oZuMe_DJAaHKEBK_R5DCHLYQPd4rJ6leIYeLhpQMsQmEBREMh9cZOhJVmhpvSxPZoQ-x-jFzbGAQTTDWuXQoLfMZF96BNJJuU6MkBA71pwZqrI5KCCfMTL6tMFeOLaz4Dj8kHdlERjU8JBUAlBzPnFAk5S_3DDul3NS-sVSQLyxM-E1Xrj_jezOZ80uc1XY5G_9o6vf5zN4tkl1NYRXErhXaq9AhIZbw2ENfEidlUMWxuA-YbTsf3RyaXzKbHrzC_O1vdOAMGkyC7b7Kt-M_csCAe73x4scEAn49iC1b_-Yg7g9ldbWB-LIiGSYQOndxfTwAxD4tF6ZxO7aNNUz1wAakKbvhVKV1jBeqzE9lm9TMCx0ZlNUDveZoL8-g9AC7xk7TMJMfi5ek6MlC4V80m4e8gKlHIB90ulue0lj1IMdza4UxV1SeTJSpU8w47FstkVs67zTLc8ar0G8S14RtBCDpg8Kj3WvrZ0_dspaY8NMqey9hdL2Ww8M9Ly33Tiog0ch1hvzagAIpCZ7mB31VykzmugmbuDq5-JeRBFk3m6f4DFs_oR35nA5o6glp-of3-Hl2oMRQluKcqeDh4hU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d44d4d0504.mp4?token=bu1VdHtRZngljfXkhW1qcpejvQ1LkIJzYyO2mkit9uXuczG0bILEzwP3etl48V0zfbNXN0sHpJcCiOt6RgxTrVw4oZuMe_DJAaHKEBK_R5DCHLYQPd4rJ6leIYeLhpQMsQmEBREMh9cZOhJVmhpvSxPZoQ-x-jFzbGAQTTDWuXQoLfMZF96BNJJuU6MkBA71pwZqrI5KCCfMTL6tMFeOLaz4Dj8kHdlERjU8JBUAlBzPnFAk5S_3DDul3NS-sVSQLyxM-E1Xrj_jezOZ80uc1XY5G_9o6vf5zN4tkl1NYRXErhXaq9AhIZbw2ENfEidlUMWxuA-YbTsf3RyaXzKbHrzC_O1vdOAMGkyC7b7Kt-M_csCAe73x4scEAn49iC1b_-Yg7g9ldbWB-LIiGSYQOndxfTwAxD4tF6ZxO7aNNUz1wAakKbvhVKV1jBeqzE9lm9TMCx0ZlNUDveZoL8-g9AC7xk7TMJMfi5ek6MlC4V80m4e8gKlHIB90ulue0lj1IMdza4UxV1SeTJSpU8w47FstkVs67zTLc8ar0G8S14RtBCDpg8Kj3WvrZ0_dspaY8NMqey9hdL2Ww8M9Ly33Tiog0ch1hvzagAIpCZ7mB31VykzmugmbuDq5-JeRBFk3m6f4DFs_oR35nA5o6glp-of3-Hl2oMRQluKcqeDh4hU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ :
می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم
«کمونیسم همه‌چیز را نابود می‌کند، اما بسیار آسان است. راستش را بخواهید، فکر می‌کنم من می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم.
من اجاره را رایگان می‌کردم. خانم‌ها و آقایان، از این به بعد لازم نیست هیچ اجاره‌ای بدهید. از این به بعد هر کسی که خانه می‌خواهد، نگران نباشد. فقط خانه‌ای را که می‌خواهید انتخاب کنید. همه غذای رایگان می‌گیرند. از این لحظه به بعد همه‌چیز رایگان است. همه به من رأی خواهند داد. در سال اول، شما محبوب‌ترین فرد هستید.»
@withyashar</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/withyashar/15870" target="_blank">📅 21:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15869">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ee8d4b334.mp4?token=J5XA6dvXbDADS-Ii_rQ-X6ZMiaQLyeSw24SnBKuTDk5eHHFSs6rN0xVzmID8t3hiYnzss4LwxEyqgLRAiJlQVR3bgO3D7UwSVZYoIS5Y5WNZyB4SwtNPKeYRKSblcxUHF0KlTimsVYFCftDUC0bUJ71l6tbZYWihyyrPCUjf8S58-Dz8lLNPfDRtGVMAJhkSpUw-PWCiZI0hL8J6IRfIC1wFa6nB_G_8VFyIsECd33fywpkawuuhcXkadeAN-pbIQH8YP-u2sm7LdHKkRfdXKwYz45GC0Mti20Lg0T4mfFYsBKAnxoPUhZtiwEOWPW2PHENj-qqakewGswBTEcwGEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ee8d4b334.mp4?token=J5XA6dvXbDADS-Ii_rQ-X6ZMiaQLyeSw24SnBKuTDk5eHHFSs6rN0xVzmID8t3hiYnzss4LwxEyqgLRAiJlQVR3bgO3D7UwSVZYoIS5Y5WNZyB4SwtNPKeYRKSblcxUHF0KlTimsVYFCftDUC0bUJ71l6tbZYWihyyrPCUjf8S58-Dz8lLNPfDRtGVMAJhkSpUw-PWCiZI0hL8J6IRfIC1wFa6nB_G_8VFyIsECd33fywpkawuuhcXkadeAN-pbIQH8YP-u2sm7LdHKkRfdXKwYz45GC0Mti20Lg0T4mfFYsBKAnxoPUhZtiwEOWPW2PHENj-qqakewGswBTEcwGEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ :
دین درحال رونق گرفتن است
«دین دوباره رونق گرفته است. دین واقعاً در حال اوج گرفتن است. اگر دین یک سهم بورسی بود، همهٔ ما بسیار ثروتمند می‌شدیم.»
@withyashar</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/withyashar/15869" target="_blank">📅 21:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15868">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">کانال ۱۲ اسرائیل: ارتش اسرائیل در چارچوب توافق تفاهم با لبنان، تا زمان خلع سلاح حزب‌الله در مرزهای خط زرد باقی خواهد ماند.
@withyashar</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/withyashar/15868" target="_blank">📅 21:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15867">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTfTe3peAO9RHpZGADZkM-NmyP0mQtyRTWC4qlVeckxxyzFWzZ2ihExrzFGoQb4wY-fH_BJlvr8_A2Hbtk-4hz5QVBsI9h3TM6gZqoqBAgpm2Zc8Gdd_L4nvn4ujpC5dlz42EqNrSVx9b-jAei5HMD_2XP8cMjujUxuZnhfXIUfM-NMYGU35sRvEDa41EygvqQ5E8J1JewOKs-fyrYcEH3NEF-yaSchPdWQn5TI7X-36tH8WPnezvpq0JpJyzK33yT72SVcyiYCNt5KcqJsSqMgfMa4duDjemCzmyummVk1SHLT714USxFUs_P1EHlA5I3y4Bj0CQUoVaktpxMKODw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی : اتش سوزی نزدیک فرودگاه امام لعنت الله
@withyashar</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/withyashar/15867" target="_blank">📅 21:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15866">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">افزایش شمار قربانیان دو زلزله‌ ونزوئلا به حدود 600 جان‌باخته و هزاران زخمی و مفقود
@withyashar</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/withyashar/15866" target="_blank">📅 21:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15865">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ارتش اسرائیل مدعی تصرف بلندی علی الطاهر شد ارتش اسرائیل : تپه علی الطاهر در جنوب لبنان فتح شد و نظامیان ما کنترل این نقطه را به دست گرفته‌اند.  این ادعا هنوز از سوی حزب‌الله تأیید نشده است. @withyashar</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/withyashar/15865" target="_blank">📅 20:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15864">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">خبرنگار آکسیوس از امضای توافق بین اسرائیل و لبنان خبر داد @withyashar</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/15864" target="_blank">📅 20:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15863">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">خبرنگار آکسیوس از امضای توافق بین اسرائیل و لبنان خبر داد
@withyashar</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/withyashar/15863" target="_blank">📅 20:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15862">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سپاه : ادعای مقامات آمریکایی درباره برقرار کردن خط ارتباط مستقیم با ایران در مورد تنگه هرمز، کاملا ساختگی و دروغ است.
@withyashar</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/withyashar/15862" target="_blank">📅 20:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15861">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ارتش اسرائیل: نیروهای ما در حال تحمیل یک واقعیت امنیتی جدید هستند که به حضور حزب الله در این منطقه استراتژیک پایان خواهد داد
@withyashar</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/withyashar/15861" target="_blank">📅 20:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15860">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/withyashar/15860" target="_blank">📅 19:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15859">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامپ در‌ تروث: ایران حداقل چهار پهپاد حمله یک‌طرفه را به کشتی‌ها در تنگه هرمز شلیک کرد. یکی از آنها به طور محکم به عرشه بالایی یک کشتی بزرگ و گران‌قیمت بارگیری برخورد کرد. خسارت وارد شد، اما کشتی به مسیر خود ادامه داد. ما سه پهپاد دیگر را سرنگون کردیم. بدیهی…</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/withyashar/15859" target="_blank">📅 19:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15858">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jj60H1D-0WesnjtT7hjIRWoMyk0w8_rD95ef5gP9VJZ_D8v3ZJJydxqbR1ARko5xNqP2W3vern5F8ftZTQCjqSsZ0Z0flU9poZfBjuCDEvr1S15picLukDNXMNqfHW9z1hZ6YLzOuoNvwD33JVNX3YquLVCBoeLEj44I1hi1ULGM8DekDTY4PPzwI505a8FFaBx-N0jv3U_MvJVLhVuVJ7LrDMTpbrt9eFvrDYTr_hzj1SM_6whoopffcDGHCDaTH-Ljo1XVUUXRHsr3UZCxgyHXHi00qwa23-V1AII_ggRqIrXCsXhMv7VM4Gb72W1_X_c6Q3NmFM-vitS1VRgM5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌ تروث: ایران حداقل چهار پهپاد حمله یک‌طرفه را به کشتی‌ها در تنگه هرمز شلیک کرد.
یکی از آنها به طور محکم به عرشه بالایی یک کشتی بزرگ و گران‌قیمت بارگیری برخورد کرد. خسارت وارد شد، اما کشتی به مسیر خود ادامه داد.
ما سه پهپاد دیگر را سرنگون کردیم.
بدیهی است که این نقض احمقانه توافق آتش‌بس ما است.
@withyashar</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/15858" target="_blank">📅 19:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15857">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ارتش اسرائیل مدعی تصرف بلندی علی الطاهر شد
ارتش اسرائیل : تپه علی الطاهر در جنوب لبنان فتح شد و نظامیان ما کنترل این نقطه را به دست گرفته‌اند.
این ادعا هنوز از سوی حزب‌الله تأیید نشده است.
@withyashar</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/withyashar/15857" target="_blank">📅 19:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15856">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه: عمان به اروپایی‌ها اعلام کرده است که دیگر راهی برای بازگشت وضعیت تنگه هرمز به دوران پیش از جنگ وجود ندارد.
@withyashar</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/withyashar/15856" target="_blank">📅 18:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15855">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دولت امارات: در حال رسیدگی به یک مشکل فنی در سامانه هشدار زودهنگام هستیم.
@withyashar</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/withyashar/15855" target="_blank">📅 18:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15854">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-YlKKyu6cvD2TfiWxy6Nu-knubUtiJUZWaMG8H3oLYo-fkDBCCXuBuyn28LDglF6DzXeX45QnZkqB6dag3_jLrBwjRriM6M0uzR6qs7hWS_M4IU0UKWCI6hHh4no56jCRFPkcBv0hqaJs5ndHZ8Ww75BbRkE8v55CkpZAw_j4K4Way-j1lyeaFm08FuvsZhwU0GSX5pLKxl9vkvKNdH7xx3wmcHGXZQAZAyYfbPE-bS3HNcmDh8U_3eRFWEEwXh18h_6mp0LEBsdvngEAW00VJGAlaoIMQu41gmduV0QHZXjSRwt18MrwKz799Zl7qwyDz9_5gfj3xBGx1shV-2_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو سیاتل همجنسگرایان دارن از الان گرم میکنن آماده بازی ایران و‌ مصر بشن
@withyashar</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/withyashar/15854" target="_blank">📅 18:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15853">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">جان بولتون، مشاور سابق امنیت ملی آمریکا، در پرونده نگهداری غیرقانونی اسناد طبقه‌بندی‌شده متهم بود که بخشی از یادداشت‌ها و اطلاعات محرمانه دولت را خارج از سیستم رسمی و در محیط شخصی نگه داشته و در برخی موارد برای امور شخصی استفاده کرده است. او برای جلوگیری از دادگاه طولانی، یک اتهام سوءمدیریت اسناد محرمانه را پذیرفت و با دادستان‌ها به توافق رسید. طبق این توافق، به جای زندان، حدود ۲ تا ۲.۲۵ میلیون دلار جریمه پرداخت کرده و پرونده با توافق قضایی بسته شد.
@withyashar</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/withyashar/15853" target="_blank">📅 18:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15852">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دقایقی پیش وزیر دفاع اسرائیل در پستی به زبان فارسی و بسیار غیر معمول تهدید به جنگ با ایران کرد و گفت: فرمانده نیروی قدس سپاه اخیراً تهدیدهای متعددی علیه اسرائیل مطرح کرده است، به هر حال، اگر ایران به اسرائیل حمله کند، بزرگ‌ترین اشتباه خود را مرتکب خواهد شد،…</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/withyashar/15852" target="_blank">📅 18:15 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

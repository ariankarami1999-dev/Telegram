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
<img src="https://cdn4.telesco.pe/file/H2FM_5IEDeMOrF-i7-wkP1WoMNr2CYbgUL4y9ZaeLgUOX2w__m5MybFM3HUUhqj3sHymSQWR05cpPZO3YefN_oxAsUw3yFbAQbxhS3wgUvNh0HPYeGMwlsryaCllKcDXhNPjcm7_dVWR5WfMPIUX4Ybpdz7-OvseLBcRfnKveN5KqKh6UT6hLR06smeBg0HqKjY56Ph2yaeZOp47LYmxZUSgDZv_6uniwl1cSrLx16Aiw7hyW2mPiL1M060DBbUJabHNrGavlpb8n8SAhiENd9jv8ccsgubHPyNT9XtG5uUHdiMHs-Iwm4eCMimBER8JudlAo5RakL83bBZtg2vOvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 182K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 15:59:24</div>
<hr>

<div class="tg-post" id="msg-78770">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4e63ecc73.mp4?token=vBEQBP2AHMF0HdSjELSqmoI1IoAN4RgvlrziMBfY1AwNibe6b3HGqFUr9jqlM3S3JWRJDWM5fe2h_U5M7UAIHJxIoIFp6VVSn0FgNQ5Gigpaj83HNsqFAdm7dsEGNa-6Shtsu7P8-ezURChEHKPHUMidbNT39rDcjREm6i50ebFFYSpQ4ENFu6rQCtJq2zVUScST0Hoo0JATl7cS_qy1nULEV9T_f1h7QFVvPqK31Hn-bHxfxVD7gPpg1FTiiq0T37yTGoll2aPl5slS-I30jEfYwAqWAVM2YfAZUksJ3nztyW9DnENYLpV8AcZ-d35rjIhkW8O9QapksLAO2Y79cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4e63ecc73.mp4?token=vBEQBP2AHMF0HdSjELSqmoI1IoAN4RgvlrziMBfY1AwNibe6b3HGqFUr9jqlM3S3JWRJDWM5fe2h_U5M7UAIHJxIoIFp6VVSn0FgNQ5Gigpaj83HNsqFAdm7dsEGNa-6Shtsu7P8-ezURChEHKPHUMidbNT39rDcjREm6i50ebFFYSpQ4ENFu6rQCtJq2zVUScST0Hoo0JATl7cS_qy1nULEV9T_f1h7QFVvPqK31Hn-bHxfxVD7gPpg1FTiiq0T37yTGoll2aPl5slS-I30jEfYwAqWAVM2YfAZUksJ3nztyW9DnENYLpV8AcZ-d35rjIhkW8O9QapksLAO2Y79cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسنّین خلق
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/funhiphop/78770" target="_blank">📅 15:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78769">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">وا  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/funhiphop/78769" target="_blank">📅 15:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78768">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ueobnusgu-4ZclXuUlkdT_YDyiyfM1OlalU3xuhIlr7pInAcJBkYLW-ksjo1gEyTa0A8luVdez6_BoD88aX_uGaovSb2b3hmYgW7_eCHqzbGA-SKKanQ83B7RisUJHk4YxdwP5Lvuc9ntDtkGQimlVyfvpcZ-tyqXQ63RgT2PI4uNta8G4Ou-advGF1RgiJmBFysK82jOK75n5ATw0FaKFKZ330tH21FkNUzXsgE1pjkVKU0rbsEhIqFf1FCl2hL8XEBi0LLSeLAp2zcxEGxjl8xgPrEbSJzNBT7m8rv3w_g1xAE8suT6Y3PXmrAMWludgAgqV0OL7Kh6MGKhutoyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/funhiphop/78768" target="_blank">📅 15:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78767">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">بهترین ترکی که بعد جنگ منتشر شد چی بود بنظرتون؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/funhiphop/78767" target="_blank">📅 15:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78766">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اینایی که از علی گرامی حمایت میکنن اینستا بهش شماره کارت دادن یا تلگرام
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/funhiphop/78766" target="_blank">📅 14:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78765">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCdoJJUhw7f3cE13RFgNQtbga0hhVPWyzvuPu4WaoGZBTjQA7sPfM3ozRr0ebRHA4G9wGcu_fb_JFTptw1WuU6WbIN3FkhgUZYnXudfmnRol9XmOVoJOtLONyiTX9t9fbgf62vzuGIgqTMXkyge3j2Bb6V6ffrtjLPp3fmXWAFvIM5kPjDGKvPG6LXlCYRM5VxL1w-m1S8bpn0uoyjAeOOaScdrhSyBzTgUM9VkXxM7Mx02aZN5pt4qvltIyk1dV-CLXO5QZFvcN_06RxFcbNatL0_WhCAoE2OFGYYSq_t7T4BJ-8nRvZNkDbFjCNX9N0H0iPWyNoXh5qDZ4NwmckQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمبود خواب داره بهم فشار میاره، چرا دارم دونفرو تو عکس میبینم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/funhiphop/78765" target="_blank">📅 13:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78764">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">علی گرامی به کدوم قبله قسمت بدم نخونی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/funhiphop/78764" target="_blank">📅 13:49 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78759">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">یه‌چنل بزنم فرم بزارم برعکسشو بزنید؟</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/funhiphop/78759" target="_blank">📅 13:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78758">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یه‌چنل بزنم فرم بزارم برعکسشو بزنید؟</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/funhiphop/78758" target="_blank">📅 13:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78757">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">یعنی چی که به بابام میگم سند خونه رو بده هفته‌ بعد دوتا سند میارم برات میگه نه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/funhiphop/78757" target="_blank">📅 13:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78755">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZvq3xeum-ZZchJQNTLrt3g7UKQScH1tXWvnJdj5LqGf6DZ52YRkIA6AHnYylVXoBVPu7YVaOd2nJQiNh4Hg_CjTZ6bcl4L6VR0DDaNDChEC1cvHXOjLmaOivO5RipC6Qr7fdhLfiU1ExKy0mPgY5meqOgJ3ka_vxTRwsVLft1D8Xx4Ohov6XXpdMEUUbywBcBFSXhAa8MIticHA7eL2Z5nuKt2YVwJhv0_9gnYCdTEWtscU5qaXZ5txvAGHLWRL2xnvaO3ndp_l-B-Wm3FNgzEP8CmKDk-Y3XXXx6hceb-pN5gAOv1A1rHTGY5P5JnhGcO9Xn40n-W4XUvWaclwQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وا مگه شما به لباسش هم نگاه کردید؟  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/78755" target="_blank">📅 12:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78754">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDzQhHSqEUkZyj4deuiKqgE05lmDXzfU7y6lrqE1YpLITgZIgBix7A6SyH6gg6pQ-EBp3Zs-pydmB-YKwvmjZpKfqWtGjt55Q140gMxJ-5fu7owMQ0hO0XIgL0BV23bVINZX4dQSOsU4_umXIPhbMvmDlLZDtDo1TpEKtxF15iFkdPl5hBmVOuJKJGNh1AJR0JuEcrNKy5ikttlI0L8FsPd-fWRajEl4W0iqTZRpqmLb126XtDJAyQQaNp0JWvKQYVn6-zjyRzpVAJLRHVFmV9A6_H_Y5q_vfBNxaji33oe4vhoMFdYvgUPpizUgmtFbskVQBT6qUSlk0b-QBnNooA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمومش کن تروخدا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/funhiphop/78754" target="_blank">📅 12:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78753">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">مصرو خوب نگاه کنید، وضعیت ده سال ایندمونه اینطور که مشخصه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/78753" target="_blank">📅 11:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78752">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">وا مگه شما به لباسش هم نگاه کردید؟  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/78752" target="_blank">📅 11:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78751">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqDZrqqmVHZfTADy1nDyF2jNSLwVhXahCL9dl87dzbOvgE1bA4BqyP3UJOXJX8ovE3pEUXG_8yfXyvRkdDP938crsq3lvlcMw1DtHsJrqjfslXpakoBYrMANbXHo2W21o5hOi8qRfqX7fm_PT5cz_Vkp5qoMjnfekdRcMb48PzG57lZcYLL9R3E6EX3Wji0Oiy_GvIRSGzgnTzbawnKFmo3GyKiG3zBjh2IM6U__DDg17R0sOa5IWCwRDLwyLtuFKn-NSj79bKD5hoPbVhkzof45sU_tn_RRKO1ihtlN-NEBrumRaCbUTlBRrbcjwNu237L5zeI7M9I9qfNE9imfPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وا مگه شما به لباسش هم نگاه کردید؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/78751" target="_blank">📅 11:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78750">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🎉
پیش‌بینی بدون باخت
🎉
بیمه پیش‌بینی
👇🏻
ویژه مسابقه ایران
🇮🇷
vs مصر
🇪🇬
همین الان وارد شو و علاوه بر
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه اولین واریز با معرفی هرکدوم از دوستات به وینرو تا
🤩
🤩
🤩
🤩
دلار درآمد کسب کن
💰
فرصت محدود
🙂
🔤
Winro.io
🔤
Winro.io</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/78750" target="_blank">📅 11:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78749">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWcBNZYK3F82uDEsqu6mpw4YbVDLHm2WXHiEs73xSIlRSIuNGMm5EvD3NkvhhtAKeQWijgBoZbn_N1xJGTobFg2WtutAJzFfApqU9azOJIw4yjvpJf-gz7TVOq2b9lfjtNjYlh-BPHuNjqB0gMOde-eI344pOUdc45hCABNjARSHZwKmL4pyQODYPiNmdfpGMiakn2tlfTBVNyE-jdpvQoFiADIIH6XXiXw0xTG2YZAlk7_UUKY7eF-flZHRC-mL8Xlr5UiyovWwW-w4HknhFrOK41FkU2YIsqxb2YLDFfql62LI5-t4ajYPAUlXHPsakXXI9XxItVxPeDibw4962g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
برای اولین بار در ایران و فقط در Winro
🇮🇷
🎉
پیش‌بینی بدون باخت
🎉
ویژه مسابقه ایران
🇮🇷
vs مصر
🇪🇬
✔️
حداقل
0️⃣
1️⃣
میلیون ریال واریز کنید و روی برد ایران
🇮🇷
شرط بزار ، در صورت باخت از وینرو فری بت بگیر
🟩
⚽️
اگر ایران بازی را ببازد، تا سقف
0️⃣
1️⃣
میلیون ریال،
0️⃣
0️⃣
1️⃣
🔣
مبلغ شرط شما به‌صورت فری‌بت (Free Bet) به حسابتان بازگردانده می‌شود.
✔️
تنها سایتی که این بونوس را ارائه می‌دهد
✔️
فقط برای مسابقه ایران مقابل مصر معتبر است
✔️
حداقل شارژ موردنیاز:
0️⃣
1️⃣
میلیون ریال
چگونه فری‌بت را نقد کنیم؟
کل مبلغ فری‌بت را روی یک شرط با ضریب 1.80 یا بالاتر قرار دهید و سپس سود حاصل را برداشت کنید.
🅰
r5
⏳
فرصت را از دست ندهید!
🎰
همین الان وارد شو و فرصت را از دست نده!
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/78749" target="_blank">📅 11:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78748">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دکی ناموسا بیار پول این ویناکو بده کصونه واویلا بازیاشو بس کنه، همین مونده بود بیف سر قرضو قوله ببینیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/78748" target="_blank">📅 11:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78747">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">بابا خستم کردید، چطوری هر ده روز یبار روز دختره</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78747" target="_blank">📅 10:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78746">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بابای رافینیا پولای رافی رو پیچونده، و الان رافینیا هیچ پولی نداره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78746" target="_blank">📅 10:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78745">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ویناک خطاب به دکی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78745" target="_blank">📅 10:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78744">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">چند روز بعد شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78744" target="_blank">📅 03:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78743">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">هرچی دارید رو ببندید روی برد هلند و ژاپن
این سری دیگه جدیم
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78743" target="_blank">📅 01:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78742">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">هرچی دارید ببندید رو برد آلمان و ساحل عاج  بماند به یادگار   @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78742" target="_blank">📅 01:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78741">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سلام فرید جان خیلی وقته که دیگه صدای انفجار شنیده نمیشه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/78741" target="_blank">📅 00:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78738">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سیتی عجب سکسیه، هیچوقت تیمش ناقص نیست، همیشه بهترینارو میخره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/78738" target="_blank">📅 00:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78737">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">۹۰ درصد رپرا و اطرافیانشون حرومزادن، سعی نکنید بین اینا خوب و بد رو جدا کنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/78737" target="_blank">📅 00:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78736">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nO9od1oa_wFAeq4VXY2V7kZl3yaMnxraGOniSGwquz3ObAPkI4XDE19oTE6MhCUhs_thjGqp5AiuIsrtxpB-GWhzkEHCarENoLsNGl4X9bSkxk3E7sejVMdjgxxuNmVW6BbPiyvc3EibcBpDtKLMaSHI_6J5YhHzhVkAdM1FM70F17PDaf9Os90ZpJJBvP-rclZgtXl-rM0aacb1fldPoo2VMRpa1L_Ho1-LzWO4w7434SNGa1kcc6ot-uRJwuj_jJ0arYIaPjGp7ck-neY9ZJt_Cra1CApi4t7mANiP-q-Z6BJjZ9sd159hmzFfaBca_BZdS5svWDzumBZ6Z3iGhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو اسرائیل دنبال قاآنی میگشتیم
تو هیئت بغل عکس خامنه ای پیداش کردیم
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78736" target="_blank">📅 00:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78735">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzD6EyOuUASRyhL2-xLvlz1usKPgXIvonv45NS1etKn0tJm-ZTFp-542v96Zl9jLSrHrRniEad5SiC3k2IeqN0GLPK7oKhp5ELD5ztGxxcW04otIXjVWTn_pKCS_I5GqpQLhefZgEuARJSIKlmsjrYM92Y66siRcWLOwrva4oW5o8sugUI0YLMK96TZ9u8xwVn_qKoqyQV2Zq4IgnpBKw4_PynofPITidIv6GGN2kEFLpUzbOOx2AHmOxaw5vVhHOIPM5-rbWjpuRX3_Cx83FKz5gqgVnyZyCuOl5xVphYsI_Z65Cidn-OFyRWmoKB2-TPffFE-jirQA9NC7_boQ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باقر شاه با حجاب
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78735" target="_blank">📅 23:56 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78731">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">هرچی دارید ببندید رو برد آلمان و ساحل عاج
بماند به یادگار
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78731" target="_blank">📅 23:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78730">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3gRNmyK0RxLfL91VM4ejuPfWkueT2rGbu8x-RwkFdXh__RXnKB_OpdMVsp3HwAlxghognzcYLVsjDpXJWhsZPloetAYJYKcoYmVPfvl8Pu0BX8b7rauF4AqCp3KAxC1vkhLxR7aCCQnDKUncA8sURIfYeYD84wyuK9cj-GL-FSSPZdYoJCtbPEdjOLLp0qPZI_RVvB0U-XiMvEZASSmMqseLNlWXsX9Ku17dqeAv1DkEbiWFJyfI2nvrNunu35qexorxxzbT3JiFjLGHFoJFUWkJHNoXlF0RauipG4AxN9_f9gRd7Vk3eDXy3kv-4tCsCkVR2-Y9MqJ4bvkCj311A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تروخدا منو از ایران نجات بدید، مگه میشه تو کشور ۱۰۰ میلیونی یه نفر عاقل پیدا نشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78730" target="_blank">📅 21:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78729">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RtBk6jHHXbHR57U8AJCvd2OvYQN7XKzKqQ_qFNKbWCq6l1wq7IDdNsPLPCngEmisBYwOCwceyjuWHIXnaVl3jEOTLjLdkHUxsgF5maS08lezwUEluQkRcntquoUc_9-tXtupCVdHp3XtFtmLcTvFXDwzSV9c6GjMAbpspAKzBARtVNCX-fQwOjF6egPfnuqKlN5JZFKeki5fD3CxeR8njJ59l0TCo8QN-FT9rqOOIIiBMl8OWCaGk-WhnJCSUof1syypQ6jjpsE17JSwRyFU22vnc_pwMHma5QMpowdeYxm4o63BAtrypCPFV8WteMRdbCLgVHSm1hRCKK11bg8teA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78729" target="_blank">📅 21:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78728">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPSFp5xx7ATcOoeFRayxmmMDLtR71KoPmoKI76OOuMO_GtBVvFfNKER71YNqZQnEqtV_pminakj4QmNfvzVTnNvamytAyabt9ni782ItZvLlXdc0QAA9tCMXwRnDquU4-gDwJGduvGr59zj1Z9sX-uNc_k6LcxfNBP_Z5MYYZPWgkPzdTyR-mmDayvDzCcz8Yq4I6nW0-wohllkN9Waj-nzur0b8BcRfrXgQVoxW9VzV2GNqTRxBF0bv1PW0oOwAiNEF9QOxmFnuD2hMHCKEezJEkDpBipC2SWWc1RXeb5BABtqssPwr2CqzuhgiOVv1Z-RraoOe0A2uMRYl1-YJdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیگه هوش مصنوعی داره مرز هارو رد میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78728" target="_blank">📅 20:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78727">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NexHBch2agyZ_y0tnJyNtj7C9sTA-Il8sZVCGUxZakkXxw6mVrgARHwHTP9P3lcLW4EwlUeYLFHBVtZjF1q0YQtpWsW0VB01jmEBUFcAsPrfAJ32a_yWg7a0HiQI20xD2-VojQjaTx9thRPlMXJyZkbLedZuS3uVh_1bAAO2ZMQD6Ee8UGLrCiq9mT84ew-EnVokfareNq3Qte6n0W_EAde5FSWqLWaxsNrTCveHYC8EbXWAmozEOKmIP8SQMX9YSJy_lyvFaS8CQG8IGC9sv4UUP39PRF7W9ESLfBSTWl0VLMk-myaBNRvNJxxfYPNoN9KDeSFXe9IKygMVWgtj_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کابران جدید
🎁
اولین واریزتو انجام بده و
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه بگیر
💰
⚡️
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
🗣️
امکانات ویژه‌ی وینرو
G4
🅰
📺
تلویزیون لایو برای پوشش بازی ها
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78727" target="_blank">📅 20:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78725">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">تو چند ساعت اخیر کریپتو ریخت و ۵۰۰ میلیون دلار آب شد رفت زیر زمین.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78725" target="_blank">📅 20:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78724">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">لازمه یادآوری کنم که کوچک‌ترین ارزشی از ارزش‌های ما کم نشد هنوز تنگه هرمز دست ماست.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78724" target="_blank">📅 20:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78723">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">یاد صابر کاظمی افتادم چقد این پسر گل بود
روحش شاد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/78723" target="_blank">📅 20:04 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78721">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFVW-jwatFGFrTL1zUnVHIOuI1tM592kzs7DYjY44Ug-Him8kOD4UL_Hf__rASO4XTlFhwWbeT9If6oeHwoU_TT4I_wupNRgIevqsHT09iJyPkSp7xtO6lGsqUJYMAA46GcaQfqwIOEvp3Db9Ob3FlBW-nE-JTQ8syDyHQ42fhLFhlf9ifX4mPZIl0h0dPrz38wU_XcSuIUa9Sr6xIeogd9XxQ33tpA4_p0pgXV5NFOyd8dCWuCBBHDfzK9IbAmcKRmScy5L3t5bCCUYY5KZcuGwAcSn4zNUY9hwaINoKFAUoezwbwKzq7S5k4DY2axAFTWfP90monKf0PH74KdZlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توافق حاجی توافق
سپاه باز اعلام کرده تنگه بسته‌ست و فقط کشتی‌هایی که مجوز سپاه رو داشته باشن می‌تونن رد شن.
برا اثبات جدی بودنش هم الان یه کشتی که می‌خواست از تنگه رد شه رو زد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/78721" target="_blank">📅 18:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78720">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">شمر و حسین رفتن برا فایت آخر
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78720" target="_blank">📅 17:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78719">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مارکو روبیو درباره ایران:
سیستم ایران هنوز توسط روحانیون رادیکال هدایت می‌شود.
همیشه اینگونه بوده و همچنان به همین صورت هدایت می‌شود.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/78719" target="_blank">📅 16:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78718">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">میشی فروزان
بلاد بودم نبودی اونروزا
یروز نبودم زدنت فرودگاه
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/78718" target="_blank">📅 14:59 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78717">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/auirGCUhYrdS2X2hZcVfln6vYC3EYTE-DXAranngswjHOvDSfXeZXx5YQyrutby0YHtw3wsfyweXkkyCARVlV_2CQuDt_jjYesOFNBWMOf-Hb6IfX3AOK7xp-KUbwj3kpopOPSKC9RwpzACPzYMvXE8uBgdZoC0FaidEB7INEOuBlorveKS6KMi0As2_nGJ7CAiGsPfePz2ercrZeEW1H6d98yCwe6NNrf85g76-7WCp76lKf1LteiQLIwwoUPYaJHeUXQNgnJgBUxdH1wtVfEUK13v0DoBGeDzLqPVVx2YRfrJ37erQrwqP1xaZpgCOvvWoXf8d2FgpjPCrRFETOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک جدید ویناک به نام "Gin" ریلیز شد.
📺
Youtube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/78717" target="_blank">📅 14:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78716">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🏳
سرور مولتی لوکیشن موجود شد
💎
🟣
لیست قیمت سرور ها
⬇️
🟡
سرور 10g - کاربر و زمان نامحدود - 60000 تومان
🟡
سرور 20g - کاربر و زمان نامحدود - 120000 تومان
🟡
سرور 30g - کاربر و زمان نامحدود - 180000 تومان
🟡
سرور 50g - کاربر و زمان نامحدود - 300000 تومان
🟡
سرور 80g…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78716" target="_blank">📅 14:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78715">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgYqHRJZpnVxa7n0lm4UmEWwJ9caja0hMuJm_r0h8brrvp7yMI5-DTdctDHI6UxiF4I8c8HqAmQ4-dHDH5hVTCSa8_cIX9rwcPUr1TB0N8RlcHNToLUu3mocWGfS4uoNUfShMa0zNhOoF0_7jdYP8oWKAV9BGxf5thgkh0CENse4tck8Gnuf4Ac2g0ev-Qhr7Sso5IC5yWnnvZDFnAg9hbs_NZ5Dx_28F_qT80puuJfmN78g5ICIa9AmNRg9_Kqc80ff1x3e1UVq94QXUS-l9gM_AdKxhrle7G-MMBodc100Cn9j45d74YjkwODbwlkfTpreeR3EV168Jfm-6WuwhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Gta خریدم تا عشق حال به راه باشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78715" target="_blank">📅 14:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78714">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">من نمیدونم داستان چیه ولی علی الحساب کصمادر علی گرامی تا ببینم چخبره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78714" target="_blank">📅 14:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78713">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ویس جدید آدرویت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78713" target="_blank">📅 14:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78712">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pt7rdTo3G-p26Otk7nF4EhlX_PjvjeaMz9YAL0IWLpay4wVGDu03TSZrk2nHynhCriGCwHv16zvXpHLBEseUJQq1hYSWVNmf6SDYz5rXONhpFY0FysBdFx315dcHWPPtf5pw3BbYr_OwXZLeWG-gvyN8h3Lnrju6TDnxWwfvPsS3kFLjLwIgqg8OkuAovJXBcYM0VZR2_pfrDaQoRmHsVo8Z3Ttuo6gtO1vN8A6Y3y7-mu8jGMvnaSInOeM3922Z0NhAh2ZE6BWg1dWrowGnMuxBoPH_Nq7xrVbankrYc8y_UCrz_XqNAm4E79OAftEqFXeJcbuHWt6hiEXrQzt1aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چی بگم والا
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/78712" target="_blank">📅 12:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78711">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">کاش اینایی که برا محرم شهریه یماه باشگاهو دادن بیارن کارتاشونو بدن من حیف نشه از فردا که نمیان
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78711" target="_blank">📅 11:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78710">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ade4f7604.mp4?token=vw2KjuC3obhwlRsWg48_er7rTEE-TuAobCfPV3E7_IuUyxzOLhGOMVTLVISItmiyEc5pmgELyJJyQl74_l5bP0PenMfaFt2yb89fxhvFuOSrMD_GP-BAFEkwocgLVHlECjM3vdXI64qE51ASy0tDSl1jrE3hhcNgVMIBcrkPn9alZ1b6QJBalhCxASMVeZ0BSaKSpU5J6a_z9d-1XhAasXuqM3SFuPqLLgLabsp5h5aIPp2xuZzYf0MNiboHc1OglaeD7YM0nyP2--fxOaeJFB70JI8Y7B8YqI7lTOlBhis23KXMERVJquIXR61oVRpYo_HG4DQOJFAh5JOd8txNfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ade4f7604.mp4?token=vw2KjuC3obhwlRsWg48_er7rTEE-TuAobCfPV3E7_IuUyxzOLhGOMVTLVISItmiyEc5pmgELyJJyQl74_l5bP0PenMfaFt2yb89fxhvFuOSrMD_GP-BAFEkwocgLVHlECjM3vdXI64qE51ASy0tDSl1jrE3hhcNgVMIBcrkPn9alZ1b6QJBalhCxASMVeZ0BSaKSpU5J6a_z9d-1XhAasXuqM3SFuPqLLgLabsp5h5aIPp2xuZzYf0MNiboHc1OglaeD7YM0nyP2--fxOaeJFB70JI8Y7B8YqI7lTOlBhis23KXMERVJquIXR61oVRpYo_HG4DQOJFAh5JOd8txNfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78710" target="_blank">📅 11:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78709">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">شیر امسال خوب غرش میکنه، فک کنم بازیگر عوض شده</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78709" target="_blank">📅 11:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78708">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ذرت حاجی ذرت
ترامپ : وای! سنا رأی خود در مورد ایران را از ۵۰ به ۴۸ مخالف به ۵۰ به ۴۷ موافق تغییر داد. رند پال و بیل کسیدی تغییر کردند. از رهبر جان تون، لیندسی گراهام، برنی مورنو و همه متشکرم.
این رأی، ایران را در معرض توجه قرار می‌دهد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78708" target="_blank">📅 11:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78707">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">کص ننت آروم بزن خوابیدیم</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/78707" target="_blank">📅 11:22 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78706">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">امروز قراره توسط آمریکا تجاوزی سنگین رخ بده از همین الان میگم چیزی از ارزش هامون کم نشده
❤️
@Funhiphop | Jenayi</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/78706" target="_blank">📅 10:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78705">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">امروز قراره توسط آمریکا تجاوزی سنگین رخ بده
از همین الان میگم چیزی از ارزش هامون کم نشده
❤️
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78705" target="_blank">📅 10:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78704">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPH05l6UuOirAxdbDhZkICJyeARw19pxZJtBvTz-ShrYilcn6C_Fc5bc5MjmyiMcnlAB4oeW30a_L83NiTQulc5Gf1kup42z3SQV0Ro-I-SE__cFWqYCa_TGX0BN_MiowDtk8zo8T2QoLRp2pJjBxW5H-VAqeS5HvgUXWzTH1OPmet3Un2Cm-PyApzYvL7pSDI1JVHDP7_Vq98xBTLungTBLRvcQ2paQjdtVVR4u0F1C3ui67FE1O-YJvYezWEt6jlsrsl38EkZld6DabFjtKmlwJ7G7mjCgsgRv8TTImSsgzVd0j0-HEZeHl5FMBzy6LxbT5e6IrORHqDGzra8vaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب 20 دقیقه بازی کرد و حتی یک بار هم مصدوم نشد
اینه شاهزاده فوتبال
🔥
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78704" target="_blank">📅 10:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78702">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwPs3LJwXctG8yJZzvYaTLsAgHXTgqBJ4S8w-Q-sVrtayHCVhRLFps1Z54IOltMa4D8lBrpdRhQIvSf1zyIeBTm65x2vYFEZBB1g31A42W8aSV60zyf99J9lBb07u3w11tqQhNbZt40IH91p-uQmZ1LjcdlF_vGDVpRfdRlTmKymbH8v1qhhQ1RvTwxF2sAtAd0YvwtMz4APGRymvGaCD9w79fN3imnO34p1bHHuiEmmg7yzAOlhxicpSSQW9pQGi-kZClhqIaXKzmxKuK3qIfBfKq8jrk89hfEoXDMP57qpuwdYscRUYe6_8jaunSM1ldA5-w5HW0LYVnPM7uBErQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔝
برای اولین بار در ایران
🇮🇷
تا
0️⃣
0️⃣
1️⃣
🔣
سود اضافه روی شرط‌های ترکیبی
🤩
ده تا بازی میکس کن، سودت رو
2️⃣
برابر کن
⏩
فقط کافیه بازی‌های موردنظرت رو توی یک میکس قرار بدی. هرچی تعداد انتخاب‌هات بیشتر باشه، درصد بیشتری به سود بردت
اضافه میشه
🛍
🆗
تا
0️⃣
3️⃣
🔣
سود بیشتر با 3
انتخاب
🆗
تا
0️⃣
5️⃣
🔣
سود بیشتر با 9 انتخاب
🆗
تا
0️⃣
0️⃣
1️⃣
🔣
سود بیشتر با 10 انتخاب
همون برد، پول بیشتر!
میکس حرفه‌ای بچین و از ACCA Boost
نهایت استفاده رو ببر
💵
💵
📺
تلویزیون لایو برای پوشش بازی ها
💳
واریز و برداشت مستقیم و سریع
بدون واسطه، بدون معطلی
🛫
تسویه در سریع‌ترین زمان ممکن
🎰
همین الان وارد شو و اولین شرط ترکیبی‌ت رو بساز
R4
🅰
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78702" target="_blank">📅 10:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78701">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbd2d4d123.mp4?token=KGOiNnxBZpFlzQlCmKUBHsaXIkgDimN1vT3JttEsQgJnkFSS6OxZekgpPijzR8iXXSfzzBuH6gRCxzFi35BEGkWoWrVpQpq_vCq8EV-ytExOW0BxaPtbGHIKr0gIL03lRKvV835CwcMvjKrqXDkKKnT347K3zLOCxjVrRoCYlJGKLd8UKeziEUGbYzDb4bZWXMzW7abcpBni8Nk-kRXJ42myNRKWvdNNxvWsg7qX6FcdekYkBiZGMKCuZrh3S5tG4u7r5xhRQU7IIoENs5-Ywbt3RnDNkeJdyFK6oHgQNtOfD7u758sYvtN4_vev878xSdi3ST76dmFQcVI2Cln5cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbd2d4d123.mp4?token=KGOiNnxBZpFlzQlCmKUBHsaXIkgDimN1vT3JttEsQgJnkFSS6OxZekgpPijzR8iXXSfzzBuH6gRCxzFi35BEGkWoWrVpQpq_vCq8EV-ytExOW0BxaPtbGHIKr0gIL03lRKvV835CwcMvjKrqXDkKKnT347K3zLOCxjVrRoCYlJGKLd8UKeziEUGbYzDb4bZWXMzW7abcpBni8Nk-kRXJ42myNRKWvdNNxvWsg7qX6FcdekYkBiZGMKCuZrh3S5tG4u7r5xhRQU7IIoENs5-Ywbt3RnDNkeJdyFK6oHgQNtOfD7u758sYvtN4_vev878xSdi3ST76dmFQcVI2Cln5cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاج اقا بنظر شما آقای روحانی کلید تدبیرش کار انجام میده؟
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78701" target="_blank">📅 10:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78698">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">هیچوقت فکر نمی‌کردم با صدای علی اکبر که داره آماده میشه بره نبرد از خواب بیدار شم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78698" target="_blank">📅 09:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78694">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">خب دوستان یک ساعت استراحت کنید تا بریم سراغ بازی جذاب چک و مکزیک
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/78694" target="_blank">📅 03:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78692">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">وینیسیوس تو بهترین شبش هم باید ثابت کنه کصخله
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/78692" target="_blank">📅 03:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78690">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GI036kmmHZmrZQNa3YdVrdEHilIVMrwNcyC6gsjAwQK7vu5FhrmXi0KXw5p5YXQLB09v2Ka3qi7hIODgxgCcm3lsqsK7R_3LbZ08QjQLRqc0bEktFCPADNobkgdR48Ez6Hx0wZdb7M089xwntkrS_FsTdyfMZPfQEExeyl2nG98QniXajTDqrCziJi3f4jjHCEpI7F0-Rplru0N2wze1GqwoHpvJxhFDkKIwTZkcFGvhD3U44chWeaX_X0qBXcejhq6BCsflCPQLmWfnB8ct9UVnOdO6yH_ehvMILqFNR5kktyfbd8MO4JR6Nx_t9Owdf2ttuhcRviN7jvArkSTKsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بایرن عجب جواهری قاپید</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/78690" target="_blank">📅 03:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78688">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ونزوئلا زلزله 7.5 ریشتری اومده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/78688" target="_blank">📅 02:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78684">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">با این جدول تیمای سوم که همشون دارن سه امتیازی میشن، ایران از مصر امتیاز نگیره نمیره بالا</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/78684" target="_blank">📅 02:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78682">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">من یچیو نفهمیدم، تیم ملی فوتبال تیم جمهوری اسلامیه تیم ملی والیبال تیم پهلوی؟
خب خار هردو رو بگایید چرا تبعیض</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/78682" target="_blank">📅 02:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78681">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">کصخلا آدم فضاییا یه فرد باهوش میبرن به دردشون بخوره، میمونو میخوان چیکار</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/78681" target="_blank">📅 02:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78677">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">من دقت کردم از وقتی که دیگه کشتی کج ندیدم کیر رفت تو زندگیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/78677" target="_blank">📅 01:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78674">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ی پیشگوی شیشه ای خارجی گفته امشب مسی و رونالدو(آدم فضاییا)، وینی و نیمارو میدزدن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/78674" target="_blank">📅 01:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78673">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">شاید باورتون نشه ولی تیم ملی ایتالیا دوازده ساله که تو جام جهانی هیچ باختی نداشته.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/78673" target="_blank">📅 01:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78672">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">قضیه لست دنس رو جمع کنید، مسی گفته اگه بدنم یاری بده ۲۰۳۰ هم هستم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/78672" target="_blank">📅 23:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78671">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ss_OOENxk22C3zy5S5kOD-nHIfBRNuKDKCyQFdZnySdoYqfw_8M9Jv69FHqUEMBOxRdl4hanPagYJpUGOCg16hMRO_Tr8L1XQWng3o5VJPqwwVa6-ps-vx1e6NYDL911AsBFyeJv2pz9e6Sw6PZZaekCCwvub5LpS5kg-bNb5KufOWucIc321_k3J35XtonyMArq836MhlyFJ6GduZ7NoCRL_TIfnMvMKJMM3WmEUf-2vDuhBX1cZsU5zNclu5IxV3VljOpFCYFRQXzK7Ng26XBKk7FhVL52PuDIO219QCITGghE90nZRZC6i4CuKkH1_X7WJocwrtxafAwz7OSfYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سخنی هم از مادر عروس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/78671" target="_blank">📅 23:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78670">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">تلگراف: ترامپ با توافقی که الان با ایران کرده؛ فقط میخواست جنگ رو تموم کنه و تنگه هرمز رو باز کنه تا قیمت نفت پایین بیاد و از فشارهای دموکرات ها کم کنه. ترامپ بعد از انتخابات ۱۲ آبان ماه کنگره و سنا این توافق الان رو کنار میذاره و دنبال توافق جدیدی میره که هرچی ایران داره رو ازش بگیره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/78670" target="_blank">📅 22:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78669">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromApexNet Shop | اپکس نت شاپ</strong></div>
<div class="tg-text">🏳
سرور مولتی لوکیشن موجود شد
💎
🟣
لیست قیمت سرور ها
⬇️
🟡
سرور 10g - کاربر و زمان نامحدود - 60000 تومان
🟡
سرور 20g - کاربر و زمان نامحدود - 120000 تومان
🟡
سرور 30g - کاربر و زمان نامحدود - 180000 تومان
🟡
سرور 50g - کاربر و زمان نامحدود - 300000 تومان
🟡
سرور 80g - کاربر و زمان نامحدود - 480000 تومان
🟡
سرور 100g - کاربر و زمان نامحدود - 540000 تومان
🟣
همچنین سرور تست موجوده حتما قبل خرید از ربات سرور تست دریافت‌ کنید و بعد اگر راضی بودید خرید کنید
✅
🟣
برای خرید از ربات زیر استفاده کنید
⬇️
🤖
@ApexNetShop_bot
🟣
برای ارتباط با پشتیبانی و مشاوره با آیدی زیر در ارتباط باشید
✅
👨‍💻
@mehdi_splus</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/78669" target="_blank">📅 21:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78668">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q31HzyMbZIZtY6rNHhuy5A3D4tNGoF7zCrxv1PyhxLv8ITu9CUOsVuSvwaoOmmbR2sOIbM5aKveGkTD3pgSdYv-uuXGkZyLvO7HTg688vN5uZPLwlEeyun7--wZJjEfkaDyEX-hp6-t3raLOLdQKBjuNZoehyqCvltE9juYEeRgT_t-I8wCiLEoL0YZvedkRs9xfUXCaH12jJDVQX5y4mWLzZnvb5iJCeTsiHhEYgX54bZMYBll8osR2BS8NETBYOY_G78mVF_BxSjjBa2aRvhBQYWcT7gU_YbNzHNieDkgqAjku9fRFh_vCXN4JCPDHukIqyoaeghu5ErtDz3Ensw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام آقا ببخشید این رپر کیریاتون چند؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78668" target="_blank">📅 21:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78667">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PbJH1xQdRoB3063zMpK5yeybX97VwAd7K1F4kuIVtzhNB-HCPheJTi1wXkKewVTmprcsbg66jjkH65YCxeWnCjEyH08RWfXA_pXHbQMlQ00J3kam7DgwcG4co0jgRsLT1XKnkHWQnq5iDKRrUkYEFxJxcOTveJJv_MzPyluPwifZ_9flbcUCQliI6ypmUcD-C9DNU3Q2pFTf48ByLlFyYzyoHeDyw0D-KMQABxD22he07UPjyFSEDJBk4unuas_CMC0lOG4rCYCcHZFlggi8AeJZP7OjIRQyM_eK5vWa_Zf34CN52qXSgY3l8SwKogVNVcQodu_tpJCGi4RDy3DH-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا زده ها شما چرا اینجوری صحبت میکنید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/78667" target="_blank">📅 20:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78666">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">بنیامین نتانیاهو: چهره خاورمیانه را تغییر دادیم، بیشتر هم تغییر خواهیم داد  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78666" target="_blank">📅 19:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78665">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بنیامین نتانیاهو:
چهره خاورمیانه را تغییر دادیم، بیشتر هم تغییر خواهیم داد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/78665" target="_blank">📅 19:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78663">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0af0e4cc84.mp4?token=X0AAGe8XaSFH2JKPdQ9MPvKIufJKlO1WBvpPbiYZinVGbWwaGwWQmhuD1e5OcP7RYUY7iFoAW94oHWRqGTzjrlc4y1GdIr4Tcns-yHftfEV_VBANRhoA0WuGcmKBuqK6aA7KyiDGSEi39fXkqzjqzkRo9s_hT2zsTh4oUPIYuvrm9xxMpFU-9bbxAgte0cW1swFTzUgU8JO9eo0gCYMtt9IboXsJvSU9K9bH7YFLmnw6ohSV9tWxbo7kPrSBYLLm3MjPx9-K9zmZIfNMy_MBUZHQB89Lgx5-h0i9SpT5O-uyvat8ajMZnks-i7Cm078ul-88_pbGduYAh9a7hMHANA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0af0e4cc84.mp4?token=X0AAGe8XaSFH2JKPdQ9MPvKIufJKlO1WBvpPbiYZinVGbWwaGwWQmhuD1e5OcP7RYUY7iFoAW94oHWRqGTzjrlc4y1GdIr4Tcns-yHftfEV_VBANRhoA0WuGcmKBuqK6aA7KyiDGSEi39fXkqzjqzkRo9s_hT2zsTh4oUPIYuvrm9xxMpFU-9bbxAgte0cW1swFTzUgU8JO9eo0gCYMtt9IboXsJvSU9K9bH7YFLmnw6ohSV9tWxbo7kPrSBYLLm3MjPx9-K9zmZIfNMy_MBUZHQB89Lgx5-h0i9SpT5O-uyvat8ajMZnks-i7Cm078ul-88_pbGduYAh9a7hMHANA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماشالا مهدی، ماشالا به این تاکتیک پسر
🔥
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/78663" target="_blank">📅 18:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78660">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">خدایا کاش سریعتر GTA 6 بیاد که GTA 5 ارزون شه بتونم GTA 4 بخرم بازی کنم</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78660" target="_blank">📅 18:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78659">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">راکستار:
نسخه فیزیکی GTA 6 فقط شامل کد دیجیتال هست؛ دیسکی در کار نیست (البته فعلا به خاطر جلوگیری از لیک شدن بازی)
- پلی‌استیشن: GTA 6 بهترین تجربه خودش رو روی PS5 ارائه میده؛ همکاری سونی و راکستار گیمز تأیید شد
-گیم GTA 6 روی PS5 تقریبا بدون هیچ لودینگی اجرا میشه!
-ظاهرا داستان GTA 6 مثل Red Dead Redemption 2 به صورت فصل‌بندی‌شده و اپیزودی روایت میشه
-بازی GTA 6 در استور پلی‌استیشن به‌عنوان یک تجربه کاملا سینگل پلیر ثبت شده
﻿
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/78659" target="_blank">📅 18:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78656">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79017d5ab5.mp4?token=kQ5SZAQxc22DqfNgtrLLw8i0VMiTDRr9a8V-VqEylbAyUMVSLXxebT5XEnhp2J1gc-gUTLMfvxIOCUOL8Sqdvtc8D8WAg7NuHhmFDv3hUcgNAuVB8ENO4Ytjxut7yqeiHzCpjRWsIFM4DBB8_sbr4Yia-1Mh7ufhrBDfYuISOX76jFaq7qCzmnilKkDGfk-QxoFHAhneqdIVgE945jHHgM8praUSZb5t1HqvAkiGxfdpXlpv58pUyno4aDRKmi5XDIh7FseH2p2JMFJFCixF_vckEeypTX4Pvj2ApwQdcH_JwAfSBIUJWNYs5ie41D2Pa5B55BGd1iFmwBZoQR2-zwSXZi7u0Pa-Usfw18XaxQncG_HFaGPWRcDhCrUK2mB9SoMb-WFZqeH_5ytX_KSotFSS2Z1wdWN-cr4NTE6Z_hkdC9qqMDi_lxcUMU2z_ZRJTIJYsEZoyrm4BbIO6b0FTIJ067m68OJavhN7nsLzSwtSi0nIKHLGBMLhGhnHKnwv25uDJleGTWqyjGyUx2Iaj07DBbAzVdLc_YDbWN5dKmpZ8oaVn8TCRYNhQEhrFvgBQZ5t5kEgTXqWYVZeCmPTsIza5K7_mQAZSh5V6IM5NBx_flopdQL1ROfkVyKtkg7il4KY8a132EkaUrnmqG5GP1w3U-YirymZ_7x8e0_GpR4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79017d5ab5.mp4?token=kQ5SZAQxc22DqfNgtrLLw8i0VMiTDRr9a8V-VqEylbAyUMVSLXxebT5XEnhp2J1gc-gUTLMfvxIOCUOL8Sqdvtc8D8WAg7NuHhmFDv3hUcgNAuVB8ENO4Ytjxut7yqeiHzCpjRWsIFM4DBB8_sbr4Yia-1Mh7ufhrBDfYuISOX76jFaq7qCzmnilKkDGfk-QxoFHAhneqdIVgE945jHHgM8praUSZb5t1HqvAkiGxfdpXlpv58pUyno4aDRKmi5XDIh7FseH2p2JMFJFCixF_vckEeypTX4Pvj2ApwQdcH_JwAfSBIUJWNYs5ie41D2Pa5B55BGd1iFmwBZoQR2-zwSXZi7u0Pa-Usfw18XaxQncG_HFaGPWRcDhCrUK2mB9SoMb-WFZqeH_5ytX_KSotFSS2Z1wdWN-cr4NTE6Z_hkdC9qqMDi_lxcUMU2z_ZRJTIJYsEZoyrm4BbIO6b0FTIJ067m68OJavhN7nsLzSwtSi0nIKHLGBMLhGhnHKnwv25uDJleGTWqyjGyUx2Iaj07DBbAzVdLc_YDbWN5dKmpZ8oaVn8TCRYNhQEhrFvgBQZ5t5kEgTXqWYVZeCmPTsIza5K7_mQAZSh5V6IM5NBx_flopdQL1ROfkVyKtkg7il4KY8a132EkaUrnmqG5GP1w3U-YirymZ_7x8e0_GpR4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای جدید هیپهاپولوژیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/78656" target="_blank">📅 18:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78655">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
پسر چی داره میشه تو این دنیا
ترامپ دو ساعت پیش: همه از نتانیاهو متنفرن
قوه قضائیه یه ساعت پیش: ازین به بعد هر کس علیه آمریکا شعار بده یا حرف بزنه، 1 سال حبس یا جریمه نقدی میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/78655" target="_blank">📅 18:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78654">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRFjQpUSvJ-OKuiALexfPL56k1kh13SQw0ACWsnqxL1WKc-6Jd9CiNzfp8muSkVWcXw3XW2fCFv8E5UZA0kbgR-IIpfAtirwnGtxuiXzaDKK4uhBOkPwbFbR_sBiiwSxb1uijZat8Cwh9Je-I8ABSnS4duTvBTieGLnGlWeOeegWWn7RAhqwp9zPpSPOhq9VIFOwirXAbPAE1SnTQMSYY_NM4TUAfm8i4fC9Tr-0wR4XClmronQ7ibu8eD6J8TobHUugYYHXbPQ2injttEl5he3yxVFrxexpH4QhNBJ3lWIUlmJJd_iFmw21OPWde5uUvJCPnpHWnLoNV5-UraJKiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادا بخدا داری اشتباه میزنی، سیستم بدنی باید حین پیر شدن افت کنه نه پیشرفت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78654" target="_blank">📅 17:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78653">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9Mi0r7gS5smHZUS1wixvf8Lo4IrOyPjBDObcH8ZAyk0x2ojZFPuzR3qJBceXHRWcfha8Cgn6aevLBbxIZTYWUjjcQykgCJ_Nhm1ITvqIeCoXVwrfVkDgHQU4JU8kd-Zlwf0iHxfRein3cOqc2CGcXJDSFOv6t9T_iitrCcxdyso2pxJlwPR1mT5vI0shVpHizpiKHiTd1EZFpPOCG2T2r_hFUOs0C28Pfl2d9_sFWpUg6Uq6S7hWTB8rqXEl8tdEGyg0EiCUNesN5Hut-P1YilZqegPibz5jt1hantv6kIjN7snqu76CV7h9hHU8xQ3q-k3vWa4PPVfCa5BqmPGxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
🤩
میلیارد ریال جایزه‌ی تورنومنت  جدید Winro
🥇
تورنومنت‌های هفتگی و ماهانه
وینرو
رو از دست نده
🔥
جوایز شگفت‌انگیز و فوق‌العاده
🎟
⭐
بدون محدودیت تعداد شرکت‌کننده
💳
با مبلغ ورودی دلخواه
🔝
بالاترین بونوس‌ها در سایت وینرو
🎯
سایت وینرو
با بیش از 400 گزینه متنوع برای پیش‌بینی
ضرایب ویژه و رقابتی
🗣️
امکانات ویژه‌ی وینرو
📺
تلویزیون لایو برای پوشش مسابقات
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
💳
واریز و برداشت مستقیم و سریع
بدون واسطه، بدون معطلی
🛫
تسویه در سریع‌ترین زمان ممکن
G3
🅰
همین الان وارد شو و در تورنومنت‌های فوق‌العاده‌ی وینرو شرکت کن
🎯
🔤
Winro.io
🔤
Winro.io</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78653" target="_blank">📅 17:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78652">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">از این ۲۰.۳۰ روز نهایت استفاده رو از کل کل سر مسی و رونالدو ببرید، فردا روزی که اینا نیستن بشینید راجب یامال و وینی بحث کنید همتونو فحش کش میکنم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78652" target="_blank">📅 17:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78651">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">نفت wti شده 70دلار
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78651" target="_blank">📅 17:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78650">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/222f81be11.mp4?token=W5r2zo8vcbnzGsl1Q50gkt0VNioeOuStVioxKZCdhHX9VSQDZf8_91pGTy3ewAPX_3DqVEo2SjA2TuIDcZL2JVYMR7a8GfhIMtlw3ZQG9xoUm4AfT9_TAXuDe2-HDufhujHirAAPV-N-ETYW4Evvw-Kp_8-HC1YmGpv7JoecsxUhaCDv6Tfp6-n3mQTt5IKCft-QZjc_LjtufRIaIaOFIKUA9GOyZuIs9HgomvSC28pFeq7MJBP-NQqGpXFnYl-QnyfztRe2d3ejz6ueaEbCLdd7VyDoG7tpo-JODQ-0YbQji67EgsLpMl2ZMlLUMbwOb-ZAmL4AFD_qOzuzGx1bHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/222f81be11.mp4?token=W5r2zo8vcbnzGsl1Q50gkt0VNioeOuStVioxKZCdhHX9VSQDZf8_91pGTy3ewAPX_3DqVEo2SjA2TuIDcZL2JVYMR7a8GfhIMtlw3ZQG9xoUm4AfT9_TAXuDe2-HDufhujHirAAPV-N-ETYW4Evvw-Kp_8-HC1YmGpv7JoecsxUhaCDv6Tfp6-n3mQTt5IKCft-QZjc_LjtufRIaIaOFIKUA9GOyZuIs9HgomvSC28pFeq7MJBP-NQqGpXFnYl-QnyfztRe2d3ejz6ueaEbCLdd7VyDoG7tpo-JODQ-0YbQji67EgsLpMl2ZMlLUMbwOb-ZAmL4AFD_qOzuzGx1bHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">که ترامپ گفته آمریکا میخواد به ایران ذرت بفروشه؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/78650" target="_blank">📅 16:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78649">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">سامان خب آخه...
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/78649" target="_blank">📅 16:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78648">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bp0qM0mjrXQhSuZlju6-E9Bxgj_klPrijK8Csdnpg95LCTvZu1uJwm-Ye1L5Q-1TKI9_SwaMYP5jPWb2BeyVro39VJlZzFZusTJxEi55j79GpRiD1Ftyn5pLtce6xB6pxQHudI3atonvOyyG-QewFSxIlT54EvULKoOQtyfUOqfMy9dqhB6WZE0tIGKvC9IkAHwtENaoqS9gmxX1ZhAWkB1di9Oh2FjeVexNlmy0tpLYwVlWLFLHk6As7H1ngxO1Tk-zxYOzwHCZqoYFqhCRH-zK5Q9dVIYOhP4Sm_onRvT4IGXNVtIW5YzJh2-sXQGuxHcRPjc56ORtkEaYhKkWzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام مهنام نواب صفوی، از معترضین دی ماه صادر شد
فرصت ۲۰ روزه برای اعتراض به حکم داده شده و اگه اعتراض مورد تایید قاضی قرار نگیره، حکم اجرا میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/78648" target="_blank">📅 15:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78647">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">5 گلزن برتر جام جهانی تا اینجای کار  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/78647" target="_blank">📅 14:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78646">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/raVsbtQNHT-9478beIcpsUEQKj7jY0QHdu1KhsX06AHKBKallWoRwiBj_q29j2s-19Jh6jZ1lLtG07GOX-9cp3UCKEklwKZv3zmtlzCicJS24izXiNSrV86tQg5RZqiTBwftZHxH8I3bEXs3xwNIM6YUWQO2cky0vRTBwN-Vl4f5kwAD7KXR-FxSs89fBs9_S4AhX_br3Sv5cWSXLY5-IEZVP9T9EKXLh3RobOUPrxtFNwEpu9GOMb0j4Ro5LSmEZw7BPhVII2DzaogZoDDbJWsIFdIpHsVSdGSUWptBs2QezZDEPD3qGw55wUbMEadv-3OwACvyE6xl-1a8ax023A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 گلزن برتر جام جهانی تا اینجای کار
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/78646" target="_blank">📅 14:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78645">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UA9sKEnV_x-x0qYJKx89D6ymparXz2a4PFYrVOW1DZwNBwjmWOdO-LClrSe3gvxFxsoXLzuiEtwUk6Ui_cdYiXyVsCsDwSI49h-57yKmLq682Y7DUXmir5YO9xEHaeJEdSxSt84AUbPFjj5-Q2RGPEo4djl9FOAHrKSs6i_fJ6X3Sqa07TFkYLVegjgIsIJayQfo2zm6M-y8dAIbahPthEyfahwBevE9Aftqw-_tfq1N_8ys_Rf7VE9hNpBJP-N7ieeIHfv4k6QkDhMv79LPLI-v6LFwMdlUOtOWkiMd-9j-ku-0z819XNgwtvigsfAKELufwdKZ3Flgj4zgwN99Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت بازی GTA VI مشخص شد:
نسخه Standard به قیمت 80 دلار یعنی تقریبا 12 میلیون و 800 هزارتومان
نسخه Ultimate Edition به قیمت 100 دلار یعنی تقریبا 16 میلیون تومان
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/78645" target="_blank">📅 14:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78644">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">قبض تلفن تماسا تتلو رو کی میده یعنی
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78644" target="_blank">📅 13:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78643">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">وزیر خارجه پاکستان: برای عبور از تنگه هرمز، هزینه یا عوارض یا اجازه یا کسب مجوز وجود ندارد.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/78643" target="_blank">📅 13:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78642">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBSDIpRead0LnVGKjRIXreIRUGX1MzvlX-AGgAVyflMjswbkrpfGgmy7W94OTuj25Z_ndTxCOCkPQNnglTxgBTBA3jGaRFLoJYYcSsmRB6TXJW1p_ANXSThxXG6pFJRfDnWpXuKB43NVtlFSrNeuk10-c64V8AIHib9fBvvRQEp3bK7PuQeHI7jLfbrBOOqmDnVcIHtYJn8b8xkAfrMSVn3cERJT2ePyvIuqi7QFZP1x-65sh-7i9V5XGNXZKtwBhDlnVhkBQgkO8Z3sIqANzIufsnYlquhiE3KwJXVl8pUAZE_mz-WnMMJ9jXacg3ugDwiqomtbhxUcwpOZf1jKFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو مغز پدر مادر شماره 2 پاناما چی گذشته که اسمشو این گذاشتن
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/78642" target="_blank">📅 12:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78641">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lw7m6eW6tKtROD6kRsJQAyALBIrQZkYm1jk_bQdqCV0hDRC8XpXLqXPxEWcB5NOrq40qwCqkVdZ8XbBVHW1dNbO38oX_CyY0F7u-ww0yvnjI925-22tOQEBEjVbGuXM0TPqxqBiwUrUAThjr6OVHcP5x3VLLiSRcupYzD-xzu2mXJtkvYTb9G0fju9cBCZ24gyfTjP_tN7G3GBaET15M-tSE3BhLFyudkqWM6QnzUAy_TiT1OVzflJeTO9XhUClhuuKazwc3N4G4accz7JOqybH2oaA3DYU73MbicHKXzZPSVHUZOVrsXhHSsiz_uSbwLf3qO0npTLIqE7vIxdYnuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچه سریعتر شمارشو برای ژنرال گیر بیارید
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78641" target="_blank">📅 12:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78640">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کاربران جدید،
0️⃣
0️⃣
2️⃣
🔤
شارژ اضافه برای اولین واریز
💳
وارد سایت شو و هدیتو دریافت کن و با خیال راحت پیش بینی کن
فرصت محدود
🙂
🔤
Winro.io
🔤
Winro.io</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78640" target="_blank">📅 12:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78639">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtCccADzOu8t4Q5WREYQ6SqwKhCVlFUbCshul1MKikhd0k-jB_frehH7-H4HEYfgcHaY9Xe-XbyXFk-iqDoMH0wprdt4Eu4Ux7AngT8mmdc0UlWIWRvdBAahFK_wQ7-1OEwFkx_XNk1qxcNsknK7l6fZk5BD9-kksgZyucDEB5zDfdw5Dbc8ySFCfIqXSu50Rxivqa3IADbG9I3xWwb0_UAmv9vDMznt-T_sw7CHhzzpFl0MnwiH3Ekfb7Jus0W36MaXMfAMtcjvP7fhQN1bKdN9ojiZEVEEOWbHeslJR2nrLxj_c-Ud_cPw9zmwxyELcDdhiBW0rPV_ZxzChhCXrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کابران جدید
🎁
اولین واریزتو انجام بده و
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه بگیر
💰
⚡️
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
🗣️
امکانات ویژه‌ی وینرو
R3
🅰
📺
تلویزیون لایو برای پوشش بازی ها
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/78639" target="_blank">📅 12:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78638">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">و تمام
انگلیس موفق شد غنای آماده کارلوس کیروش رو متوقف کنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/78638" target="_blank">📅 01:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78636">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">توخل از سبک بازی کیروش کلش کیری شده</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/78636" target="_blank">📅 01:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78634">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">بزرگ‌ترین اشتباه تاریخ فدراسیون فوتبال ایران قطع همکاری با کیروش بود
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/78634" target="_blank">📅 00:46 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

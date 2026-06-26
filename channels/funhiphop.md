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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 13:45:33</div>
<hr>

<div class="tg-post" id="msg-78759">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">یه‌چنل بزنم فرم بزارم برعکسشو بزنید؟</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/funhiphop/78759" target="_blank">📅 13:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78758">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">یه‌چنل بزنم فرم بزارم برعکسشو بزنید؟</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/funhiphop/78758" target="_blank">📅 13:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78757">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یعنی چی که به بابام میگم سند خونه رو بده هفته‌ بعد دوتا سند میارم برات میگه نه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/funhiphop/78757" target="_blank">📅 13:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78755">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZvq3xeum-ZZchJQNTLrt3g7UKQScH1tXWvnJdj5LqGf6DZ52YRkIA6AHnYylVXoBVPu7YVaOd2nJQiNh4Hg_CjTZ6bcl4L6VR0DDaNDChEC1cvHXOjLmaOivO5RipC6Qr7fdhLfiU1ExKy0mPgY5meqOgJ3ka_vxTRwsVLft1D8Xx4Ohov6XXpdMEUUbywBcBFSXhAa8MIticHA7eL2Z5nuKt2YVwJhv0_9gnYCdTEWtscU5qaXZ5txvAGHLWRL2xnvaO3ndp_l-B-Wm3FNgzEP8CmKDk-Y3XXXx6hceb-pN5gAOv1A1rHTGY5P5JnhGcO9Xn40n-W4XUvWaclwQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وا مگه شما به لباسش هم نگاه کردید؟  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/funhiphop/78755" target="_blank">📅 12:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78754">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDzQhHSqEUkZyj4deuiKqgE05lmDXzfU7y6lrqE1YpLITgZIgBix7A6SyH6gg6pQ-EBp3Zs-pydmB-YKwvmjZpKfqWtGjt55Q140gMxJ-5fu7owMQ0hO0XIgL0BV23bVINZX4dQSOsU4_umXIPhbMvmDlLZDtDo1TpEKtxF15iFkdPl5hBmVOuJKJGNh1AJR0JuEcrNKy5ikttlI0L8FsPd-fWRajEl4W0iqTZRpqmLb126XtDJAyQQaNp0JWvKQYVn6-zjyRzpVAJLRHVFmV9A6_H_Y5q_vfBNxaji33oe4vhoMFdYvgUPpizUgmtFbskVQBT6qUSlk0b-QBnNooA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمومش کن تروخدا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/funhiphop/78754" target="_blank">📅 12:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78753">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مصرو خوب نگاه کنید، وضعیت ده سال ایندمونه اینطور که مشخصه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/funhiphop/78753" target="_blank">📅 11:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78752">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">وا مگه شما به لباسش هم نگاه کردید؟  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/funhiphop/78752" target="_blank">📅 11:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78751">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqDZrqqmVHZfTADy1nDyF2jNSLwVhXahCL9dl87dzbOvgE1bA4BqyP3UJOXJX8ovE3pEUXG_8yfXyvRkdDP938crsq3lvlcMw1DtHsJrqjfslXpakoBYrMANbXHo2W21o5hOi8qRfqX7fm_PT5cz_Vkp5qoMjnfekdRcMb48PzG57lZcYLL9R3E6EX3Wji0Oiy_GvIRSGzgnTzbawnKFmo3GyKiG3zBjh2IM6U__DDg17R0sOa5IWCwRDLwyLtuFKn-NSj79bKD5hoPbVhkzof45sU_tn_RRKO1ihtlN-NEBrumRaCbUTlBRrbcjwNu237L5zeI7M9I9qfNE9imfPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وا مگه شما به لباسش هم نگاه کردید؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/funhiphop/78751" target="_blank">📅 11:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78750">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/funhiphop/78750" target="_blank">📅 11:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78749">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/funhiphop/78749" target="_blank">📅 11:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78748">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دکی ناموسا بیار پول این ویناکو بده کصونه واویلا بازیاشو بس کنه، همین مونده بود بیف سر قرضو قوله ببینیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/funhiphop/78748" target="_blank">📅 11:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78747">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">بابا خستم کردید، چطوری هر ده روز یبار روز دختره</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/funhiphop/78747" target="_blank">📅 10:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78746">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بابای رافینیا پولای رافی رو پیچونده، و الان رافینیا هیچ پولی نداره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/funhiphop/78746" target="_blank">📅 10:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78745">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ویناک خطاب به دکی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/78745" target="_blank">📅 10:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78744">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">چند روز بعد شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78744" target="_blank">📅 03:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78743">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">هرچی دارید رو ببندید روی برد هلند و ژاپن
این سری دیگه جدیم
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78743" target="_blank">📅 01:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78742">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">هرچی دارید ببندید رو برد آلمان و ساحل عاج  بماند به یادگار   @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78742" target="_blank">📅 01:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78741">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سلام فرید جان خیلی وقته که دیگه صدای انفجار شنیده نمیشه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78741" target="_blank">📅 00:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78738">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">سیتی عجب سکسیه، هیچوقت تیمش ناقص نیست، همیشه بهترینارو میخره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78738" target="_blank">📅 00:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78737">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">۹۰ درصد رپرا و اطرافیانشون حرومزادن، سعی نکنید بین اینا خوب و بد رو جدا کنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78737" target="_blank">📅 00:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78736">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcrEcyX4IWQo6QnEcqa4ZKTGSRONSRnUUP2uph3KwZUVj79lRk_L-G119GFvp1uT-N_xo_uFvc-Tu6-_gsvqqyH-8-jHyuCRqo-Qjxhsw0drB1AKKFz6QzYyCE_xcxTisoiQP2VrqJ9-2-Dah8WgGXVsFkngeAtE4154CM-6n4xfFV3FLJXVIL2jwnJgLUnU2QfH0SiyFaLNjr8a0oh7TgZkjWUjK0frpWF-xstugF-2ItR0HhtGCMxvbTxzKl21OpE3lB8dubFQSFjYMcKMBbjBMKmWNlZIRrvfb_FepTu7fG-eUQ7_QAF-qd1adwU2YnLjH6TJSmIMiNdggaiUNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو اسرائیل دنبال قاآنی میگشتیم
تو هیئت بغل عکس خامنه ای پیداش کردیم
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78736" target="_blank">📅 00:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78735">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISToCchcVXqliwmIUbr5lKNwtWJ98_zG8DUoCGucWb_ATkPicggvkX98tXAq3b4_GCANTkw5XHh8uE1DqY9ocQWjtWbTIggDX_NQXWEhzGcGuTbW-aFVlCFar9vyeJ5H1Wfg0KcyixjgHlbjpLyUB9wGomqriFeenjioZLEEGjGeAywzsaekC1RESlE2rnxlbgoMotjKDsJA5Yr0JUO8l6Pk8xGmsDDvJ6ZIVBFQGGSzb5vKAceMDXUsLmBCrb_W9NDQw6QOvA6IPWcwx8rp6Fz_Gq2QNs8emxm6esv1MSwemAqU4ZmBsLIlrn_qXmFb04TyeNPw-EjGGzFZ6rt85g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باقر شاه با حجاب
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78735" target="_blank">📅 23:56 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78731">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">هرچی دارید ببندید رو برد آلمان و ساحل عاج
بماند به یادگار
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78731" target="_blank">📅 23:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78730">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffDIS7eXRdKeq8tQZ1mZ2pk6O66bzMVRlH_DNHph_eB3RGCSrYPMqcOUiCjj4MzD7axpz4qPkBbi-ad5KKTg0R7Fo7PUFw8knQdMdQ738let2YI-Y85AEFlbd697AIdVUHo4XebKzjduBEu712tUsbR6EuN41k8QtanMVVr4r0tJNyqZC7XsP2NhMEfrUEvdJ775DDr3CRgxGXaMDmD9yQw6a3PHMSEYcvKuNbcuC_7Rh802OI83k7fHyqe-s8eifkzVD58vw9eQFHHWsPXZpAD4eDOzVXu1aAMkouoMn3uZJnfXmgxdVsrtkpW19GG7n8IDGCDmCa1y-JCefpeYlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تروخدا منو از ایران نجات بدید، مگه میشه تو کشور ۱۰۰ میلیونی یه نفر عاقل پیدا نشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/78730" target="_blank">📅 21:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78729">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwihilxDqZGDb_hjO5Hb6uGpR-fe8b6GkCqEcYzEr70XtrAOJNIVtMxbZKfq3rgt0QC-lOSeUd9onGfTp4uZTJ8v4PgvXBR9OLl-Q7XuhEJxTHFFMqeJ-TeHL5ogFJZAzEAQG7ZKGkYUfbRvdkA5EjtpP2N33POGfGmfY4_7D1fGREhNv1MHX7-ZbFgbqbsFMn2MgVHJTJdwkmd9AhCPUYfMECEWEIeJ7tJMdkT3F1HyPjzWx3wGO7ChPxplFQZxTUShrOXurxcEobtWu6e08kRIEZoS0jfiYq_UOcf6nvfCiA0s9bMYTD6Cf165kw2DOoPWID_DyqWfZqsRrmK0lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78729" target="_blank">📅 21:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78728">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqD-gwNULJXquTYnNzEXonr5GAolPS8UIO8J_9r44Kmgh1jST2p7vU9bgOXFmnL0UsEgp3Lh5FoY9wfQIM7Ad9IM3wfadIGKcDXYLNL_Lu2z2hcxRtfIPRYyaMoDgg4QihyruAlIoG8jAwtq0n3DTxAmzGqszpzcBB_i9jJPzbzVjfXhA12FxoGg1GmMc7_CDyf4iXMmtIh10oc8BlOu_jSlWj-3ZN4stmn0Q4MBDdvX7DorRxy4wK6cnRKfk7ZN8FvftNmFV26RJ2PyFN3BBHfzXeC6ecEDSh0kLHfhMjvCau_j9U338IR5sLqy_URtxABQPxzapdA8XClN7e3rxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیگه هوش مصنوعی داره مرز هارو رد میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78728" target="_blank">📅 20:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78727">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFykXuFJZ6DZnixxovyfZPOxy3EseOpubpUWm_zrsmXiGWvC-9Esqvo1a4iRp6tDdGYK7XL9p_zdgQbsLlkkSlVSM_3hPN8TDUHCYR5DStmiRer69sEcTYQX1XPy_HeWQsqG_XTRMDA86SG-C9Kj1ACEKRFqSj4Oavu5rSdFQ22CskqQS9OFz3aiGLadQjYAfkWeYfkAcktrrgBWO5_Vpab2s36Xorzw5FXWcvFO-t8LnWUU5bqO2gjAWgfJAyPqdvOi8tm5Pdk_aH4nzURhTyGASUyC1gplUXLI0LzsyiuQKvm8uYfgOEYPImyzxv63WSuPrriYUf9pKxazZAw8oQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78727" target="_blank">📅 20:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78725">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">تو چند ساعت اخیر کریپتو ریخت و ۵۰۰ میلیون دلار آب شد رفت زیر زمین.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78725" target="_blank">📅 20:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78724">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">لازمه یادآوری کنم که کوچک‌ترین ارزشی از ارزش‌های ما کم نشد هنوز تنگه هرمز دست ماست.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78724" target="_blank">📅 20:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78723">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">یاد صابر کاظمی افتادم چقد این پسر گل بود
روحش شاد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78723" target="_blank">📅 20:04 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78721">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdbxToxSJS1MH17V5RUX37zu-it406oWJq5kAnu5QZb7MAZRCP78-0U15popBVWq2u4p4ZYJ1dQXozsvzACGD-3i2EPwh2JwbjnbiCvhMvaGaNbyPkVtnfBrwVDqxwnaWUaynVlI7XFtFBTAAmLV-CExN9Gze9gVwHCST_QMjlxy8_Orgk94_GGog5pRbF58KwqbUioQBL_fBHnQyFBrQtHG_rFLoYKSFmNQV9Wt0qCE-gjBKdK1XYGP9JzkL1NUt716qMJXg5jY_vfHpQ8xYMnKliSHIQwzl-th0KRyFOIcqxIH9-r93qVKMvB4a5HPHhgvHpPQ-L6VvzeZFpE9Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توافق حاجی توافق
سپاه باز اعلام کرده تنگه بسته‌ست و فقط کشتی‌هایی که مجوز سپاه رو داشته باشن می‌تونن رد شن.
برا اثبات جدی بودنش هم الان یه کشتی که می‌خواست از تنگه رد شه رو زد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/78721" target="_blank">📅 18:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78720">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">شمر و حسین رفتن برا فایت آخر
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/78720" target="_blank">📅 17:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78719">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مارکو روبیو درباره ایران:
سیستم ایران هنوز توسط روحانیون رادیکال هدایت می‌شود.
همیشه اینگونه بوده و همچنان به همین صورت هدایت می‌شود.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78719" target="_blank">📅 16:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78718">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">میشی فروزان
بلاد بودم نبودی اونروزا
یروز نبودم زدنت فرودگاه
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/78718" target="_blank">📅 14:59 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78717">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4szutpZWmHAQ784B5zJfdqSvb8NwDZSp89j_eQSAgk3Qpj2eFVN9aFVFKJbonHZTi_GrFAkBagqKuuMTuPjemn4LkoC_kqmB11X5tyJdOYnHrHULGqrt3a4tkvluP4Tun3iJLI2EjGJzfG32dwb5qU1_sh8xhgaP2mtGdgyEkAGk5sQGSTZIIXaWGFGSJWVMTmr46Nwe0QBwVh4iz0YxbsAj1DRjb_XaDz4_0kRi4_GSAT_Om9FgWgDPvcdAqyvJI0j7_F5qmxuXlc_cBnJZ8qKzx6x8zmFhVHBqrogHsOqf3l7VIhVHGsPD6PooLJ2PrP5PSSeJSuEElWRQro_AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک جدید ویناک به نام "Gin" ریلیز شد.
📺
Youtube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/78717" target="_blank">📅 14:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78716">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78716" target="_blank">📅 14:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78715">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTpSH6yq3ntlBlPQ7LjBdiHSDhxGbsRaJIoh33fZ-WhS05ROkdQvu9adMHgj3G4JlfjF5UFM36dotYOhcgyXg1yIybVcJCjYthFCYsdSwewPDaYnyDONgZHUfmLsuso6XRiY1mlcVeh1Msfn3uWYUkc57HwxqRN-B58DsjYQQbQ22UJ_Trn8wjSGcV1LYbWFOE7POxfCJQNnnX7CRFnWeeqxyJr4E_ha4P5fNpyIWGjAv3NQmYPHwBNjNoxDlI6TGaWpNWejSDBisloDDIeDEKvxnX2XZaf-8_ufF6FhKENkacHhwdmg4mbdjhOZ2_M9tp5ixbB-P6QQM2otxmnfpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Gta خریدم تا عشق حال به راه باشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78715" target="_blank">📅 14:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78714">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">من نمیدونم داستان چیه ولی علی الحساب کصمادر علی گرامی تا ببینم چخبره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78714" target="_blank">📅 14:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78713">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ویس جدید آدرویت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78713" target="_blank">📅 14:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78712">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQ_n7Ry4CyV9lcf2DOI5mqoLnI_SyjXMQg5Dtkvn20JZRRlK_5jFUlHfRa8vwazjspt5q1RHUK1T0XVX9il7s_OjqsjIAKAjYf3RRtKs9Ysg-uw8JMI5wPbMqDBOYsCE6cHkKrOpZne1m3EvIGHISRDDMghHyCdjq_BN0p9ZUeul8HlE_By6OjmdOBFTBlMpk1CeCsRlbNLkQigkNNMiB0zVjaFLUx_5203t91EsEpFRvcqkN_mgUUu-Ybr5v6JcQoS3WvWmevYtDfdGToDmU_JOx8XB4uatX7a-u0jeeuXR0AZ7LsL7v8qiddoUkXkAZ6GnpGVHJeGmqz547TdZrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چی بگم والا
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/78712" target="_blank">📅 12:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78711">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کاش اینایی که برا محرم شهریه یماه باشگاهو دادن بیارن کارتاشونو بدن من حیف نشه از فردا که نمیان
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78711" target="_blank">📅 11:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78710">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ade4f7604.mp4?token=dKVvb6YkOThB5XtqJqukRfCjacb2On94GBqqdNLnG1O5zTrivk71HOh1SBqJmvl-lJWlIV8BXkvlDnt0gBZi9GSzBYs0TVtdayQcHdWRfVpQ2TpU2HE2zw68potnWFMxp625Z3LU4hRiVUw4DTcjIvA1iDk2iRo-yLbpppXSRc4guyNREHPnuM_f2we8P9UDFoMbm8nwDHh1fX0zsArx32DkhGIWqDA1B3OEgIMTLRPsWLVZKhZ_fK_tYaLwWsX1-uH_QjdZEwjzMNG5N6gjSuZwvlXbBadFHy-RRvbgKfzjq-yR0LSMRyl5T6I0XsZgnGK2C6oU9hg0ZYzlSwEnuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ade4f7604.mp4?token=dKVvb6YkOThB5XtqJqukRfCjacb2On94GBqqdNLnG1O5zTrivk71HOh1SBqJmvl-lJWlIV8BXkvlDnt0gBZi9GSzBYs0TVtdayQcHdWRfVpQ2TpU2HE2zw68potnWFMxp625Z3LU4hRiVUw4DTcjIvA1iDk2iRo-yLbpppXSRc4guyNREHPnuM_f2we8P9UDFoMbm8nwDHh1fX0zsArx32DkhGIWqDA1B3OEgIMTLRPsWLVZKhZ_fK_tYaLwWsX1-uH_QjdZEwjzMNG5N6gjSuZwvlXbBadFHy-RRvbgKfzjq-yR0LSMRyl5T6I0XsZgnGK2C6oU9hg0ZYzlSwEnuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78710" target="_blank">📅 11:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78709">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">شیر امسال خوب غرش میکنه، فک کنم بازیگر عوض شده</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78709" target="_blank">📅 11:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78708">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ذرت حاجی ذرت
ترامپ : وای! سنا رأی خود در مورد ایران را از ۵۰ به ۴۸ مخالف به ۵۰ به ۴۷ موافق تغییر داد. رند پال و بیل کسیدی تغییر کردند. از رهبر جان تون، لیندسی گراهام، برنی مورنو و همه متشکرم.
این رأی، ایران را در معرض توجه قرار می‌دهد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78708" target="_blank">📅 11:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78707">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">کص ننت آروم بزن خوابیدیم</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78707" target="_blank">📅 11:22 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78706">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">امروز قراره توسط آمریکا تجاوزی سنگین رخ بده از همین الان میگم چیزی از ارزش هامون کم نشده
❤️
@Funhiphop | Jenayi</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/78706" target="_blank">📅 10:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78705">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">امروز قراره توسط آمریکا تجاوزی سنگین رخ بده
از همین الان میگم چیزی از ارزش هامون کم نشده
❤️
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78705" target="_blank">📅 10:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78704">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTvCrsirhIFNrcmE1Nj2zdlSFD3Bmj4KjeaK9s4Z_Zpa9FUnASsZPK19dXo09whSPnGwUy1MLlveGTFIuDAHkHIrgpx2TZDSPbmvEXXCB-9bd3Fviedz7ZQSZacYwngVghXgO8O5DLEwzptSIlvs1Amevi4EesxUrpBRsvhQyILG0DW0g_rIi49WncE9IUebkatF5dYaOxliMdUiHRuaGoAZ8-NT1KYUuQkhEFWX9qcNz6uDFKZ-EhwtwOh-y-K2hkUxkLqvKHd84-nOYlnVMb2KjfQGwPqwygCAUmiGDWzqkzGrS6X8l-RPi2Fu_9XGnMB-eBhUbv2WyFIaXtDtbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب 20 دقیقه بازی کرد و حتی یک بار هم مصدوم نشد
اینه شاهزاده فوتبال
🔥
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78704" target="_blank">📅 10:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78702">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/meUIh7NXq6NPMCzdhvtK9oJV47RgeHHdYis67rtmXNT13m8ycsJplGxqiKVVrm-bThcPWvkYT431yS9kbQ60zVPDUt_C43bnOSfzNJqqtQLVk8OCiH4tRaDOpU_onrY8-V7J91jddKplWTlD1X9S2h5mOraaUXaW-bP1BoEkR-XeSPgb6z_y-OXengQmy8GGbm0mXDBCyk-RQLjFGxDax044BCtZAiunyc5b6N4VuFnYKDHvn646L_L9ZneZjq1_T4eUKfRY8kXjhpXurgLhcieMqrolqm-3R14Io4rA1KZBju8U9n6IiuUhJUWHEndKhGX08vdpt2ieA4RAv3Q-ew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78702" target="_blank">📅 10:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78701">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbd2d4d123.mp4?token=OUn0_tQmDgF-QDm3p14-4pXoRVDgRKZbaEdId1-KdOJBMtKq6Ej6_3BKzi8menBAZmMPjLcATAqJvnpC9LSI4lw4QpNA78SBktFPZD2iNVvEd_Hd5Bqm5uKoZ44Hozd4ZfeJpkIPcuCugOINXcnA6WIXaD1RDUX1gNoOEZ3dAMVspmSgxQ8pJugNSgwhh7wMMSutn0syz1VROLrgjX8OWa8axVMS-jUhEl27DNDxFi-BHYEPxA1v3m4utdhcCdgf-7xkMmzOFhdZu4g3bPGMhBqRbjJynArmN2KaTUqnWlmVJE4Rp9QHWzq67hNnENdXapPjPoacw6li-3NHFHbVUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbd2d4d123.mp4?token=OUn0_tQmDgF-QDm3p14-4pXoRVDgRKZbaEdId1-KdOJBMtKq6Ej6_3BKzi8menBAZmMPjLcATAqJvnpC9LSI4lw4QpNA78SBktFPZD2iNVvEd_Hd5Bqm5uKoZ44Hozd4ZfeJpkIPcuCugOINXcnA6WIXaD1RDUX1gNoOEZ3dAMVspmSgxQ8pJugNSgwhh7wMMSutn0syz1VROLrgjX8OWa8axVMS-jUhEl27DNDxFi-BHYEPxA1v3m4utdhcCdgf-7xkMmzOFhdZu4g3bPGMhBqRbjJynArmN2KaTUqnWlmVJE4Rp9QHWzq67hNnENdXapPjPoacw6li-3NHFHbVUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاج اقا بنظر شما آقای روحانی کلید تدبیرش کار انجام میده؟
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78701" target="_blank">📅 10:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78698">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">هیچوقت فکر نمی‌کردم با صدای علی اکبر که داره آماده میشه بره نبرد از خواب بیدار شم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78698" target="_blank">📅 09:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78694">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خب دوستان یک ساعت استراحت کنید تا بریم سراغ بازی جذاب چک و مکزیک
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/78694" target="_blank">📅 03:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78692">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">وینیسیوس تو بهترین شبش هم باید ثابت کنه کصخله
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/78692" target="_blank">📅 03:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78690">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZHM3TDSD1rF2GzdRwsjSSxfbzDJnP7vOJJNj6_8nmzPtpDrun57YG9jGUvrZ9_t8U2oMbNvVqZJQQu5YizpP1FOfb0Vjd90bkSPw_5GeXyL3bKNx-4LK4trf0NS5G-zCtMg2tWyLankhJqeKMHWwiTv2iwmxzuhu-DyetMYHRUblJA4MmDRqry2ca5zp3DOHxNswHPX_YoxQ-sSkQhponsIX7JkpYCPWXoUX4co_BIz9pOiWwwTfYRmh1pzgiS7VCQao0Yw72H4sYeGiMa7aF_H-XgHcbM_x9JatC9zynqSI7-lqAXuNSpw2LV0tn8X8OKGTsSynoAWEYb3k6t4Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بایرن عجب جواهری قاپید</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/78690" target="_blank">📅 03:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78688">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ونزوئلا زلزله 7.5 ریشتری اومده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/78688" target="_blank">📅 02:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78684">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">با این جدول تیمای سوم که همشون دارن سه امتیازی میشن، ایران از مصر امتیاز نگیره نمیره بالا</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/78684" target="_blank">📅 02:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78682">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">من یچیو نفهمیدم، تیم ملی فوتبال تیم جمهوری اسلامیه تیم ملی والیبال تیم پهلوی؟
خب خار هردو رو بگایید چرا تبعیض</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/78682" target="_blank">📅 02:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78681">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">کصخلا آدم فضاییا یه فرد باهوش میبرن به دردشون بخوره، میمونو میخوان چیکار</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/78681" target="_blank">📅 02:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78677">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">من دقت کردم از وقتی که دیگه کشتی کج ندیدم کیر رفت تو زندگیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/78677" target="_blank">📅 01:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78674">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ی پیشگوی شیشه ای خارجی گفته امشب مسی و رونالدو(آدم فضاییا)، وینی و نیمارو میدزدن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/78674" target="_blank">📅 01:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78673">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">شاید باورتون نشه ولی تیم ملی ایتالیا دوازده ساله که تو جام جهانی هیچ باختی نداشته.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/78673" target="_blank">📅 01:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78672">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">قضیه لست دنس رو جمع کنید، مسی گفته اگه بدنم یاری بده ۲۰۳۰ هم هستم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/78672" target="_blank">📅 23:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78671">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TegbHTWtJZhNZhHLi4g_EkUV2qjLOUq_2oVhO_71ojwu9Agpm-9UYAs_Dn4ilIEiR4ruckJcnDmvJvT1v8T8tmYS0dBBmoNlTNs1zoPivrGjNA03ZoEji7S9fTfT41zx3f4ik0J69N04SHLD-a2pu3ywV5i1QYfZKOZ_F67rM2SPAAgnUQDB7DMan8Yvj0PDEswj13OVDTnuATGbTnKvGpPcjLDGxmmk5-7WHqFZwCDkvkDuhQTVOGwgvsthUi2aoPPyQvoS4xBA8f5fkjRhlYOpbaDvf_EEMMvvLYvJSPDSiPECCSqf6JIZAO6A42q47seepDWaH3Akv8muV19Gyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سخنی هم از مادر عروس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/78671" target="_blank">📅 23:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78670">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">تلگراف: ترامپ با توافقی که الان با ایران کرده؛ فقط میخواست جنگ رو تموم کنه و تنگه هرمز رو باز کنه تا قیمت نفت پایین بیاد و از فشارهای دموکرات ها کم کنه. ترامپ بعد از انتخابات ۱۲ آبان ماه کنگره و سنا این توافق الان رو کنار میذاره و دنبال توافق جدیدی میره که هرچی ایران داره رو ازش بگیره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/78670" target="_blank">📅 22:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78669">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/78669" target="_blank">📅 21:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78668">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Csk8Cu60U86JwYzJEMyVLqO40zBjEkmvQCaaa4u_jvRgBGIAm0AOi2vRvFo18NOioeN1eS_8GRKKGgrFfzoyDnpaW4evYaJG9MkZ6lzyjwDeoVGM4btgzj4H6xhqYXIgk_gcrNll9D1q-WEmhHeamhtSSaeOK9k4hq7_AXkChGYjpT4Ce3XDRfJ1NNNkrXN19mbHXRaroPLMywvaVCLPNTtzQKKsXTvk3oxC4ZMKi0hHYfScSyPoLljE0c8KZCg_bB3638ieaGoVU16RTdQq1Qb3D6I99uOFA2lJk0JQHfqBdXKde0Que62eMCma9Vhu4L4EwKaqWKXnWFSd6AHjGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام آقا ببخشید این رپر کیریاتون چند؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78668" target="_blank">📅 21:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78667">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k006FHKewQjGAuhDGCOzqRjlP7KVxiKVkkwtKF7JqyZm8dyRFKf0BZOv_89jrH0_UL693qsmWe6hCCs5FfstShbZjd7SU8upR1xcpFL4V4V3T6J8PuZX6_KWGN9XXu6CTubGsr7j0eqdNMgD73tuY6hT0RhM2Ckky129I-OCK5HLlJwGFQI7N91DpQRF67_11ASOWLWYzvZvdfAsEoy8spq-vrBOfL17VT5863tz5Umov4STmrCVhmNF7nqseMfr1Vq7USBU5uQeY2fxbH9DJ7diAwhFUyJq-AU5isUoioFk_dEkPPv4zwcnr02I4AKhUiI5UprTNKsOU5TwrdMwpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا زده ها شما چرا اینجوری صحبت میکنید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/78667" target="_blank">📅 20:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78666">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">بنیامین نتانیاهو: چهره خاورمیانه را تغییر دادیم، بیشتر هم تغییر خواهیم داد  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78666" target="_blank">📅 19:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78665">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بنیامین نتانیاهو:
چهره خاورمیانه را تغییر دادیم، بیشتر هم تغییر خواهیم داد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/78665" target="_blank">📅 19:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78663">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0af0e4cc84.mp4?token=c-j1iqy3e5XrqcIeokaNzJ2cEbDSOMHbhbzHpfaeF4w5X5pftnTfY-bpYksPBqGhLOdxXIeAiEtE2anadDWJB9xf9qWzPPiH4CI8f5uzZWjzmi-Ok_nWCrjWXN9HpM4MF9VxADugzqOhw8CyTKIK27ZgeGdho3i8VWK0LQgTbPJadnljweGhd1skiHHZ8Wyn5tHBiKR-oTTI8812yZR6szdcBN2iZvHqDI4_cy-aDj9LqdPIVE0w62B4A7gfvQ_u2wz14_7mpPjeV0YVGlrkNEcIxYW8RYJdJx2iA55Rkrr8JmLTinzzLml8ixlKo9geQdp0iIFdKlzhRPfTyuM90Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0af0e4cc84.mp4?token=c-j1iqy3e5XrqcIeokaNzJ2cEbDSOMHbhbzHpfaeF4w5X5pftnTfY-bpYksPBqGhLOdxXIeAiEtE2anadDWJB9xf9qWzPPiH4CI8f5uzZWjzmi-Ok_nWCrjWXN9HpM4MF9VxADugzqOhw8CyTKIK27ZgeGdho3i8VWK0LQgTbPJadnljweGhd1skiHHZ8Wyn5tHBiKR-oTTI8812yZR6szdcBN2iZvHqDI4_cy-aDj9LqdPIVE0w62B4A7gfvQ_u2wz14_7mpPjeV0YVGlrkNEcIxYW8RYJdJx2iA55Rkrr8JmLTinzzLml8ixlKo9geQdp0iIFdKlzhRPfTyuM90Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماشالا مهدی، ماشالا به این تاکتیک پسر
🔥
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/78663" target="_blank">📅 18:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78660">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خدایا کاش سریعتر GTA 6 بیاد که GTA 5 ارزون شه بتونم GTA 4 بخرم بازی کنم</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78660" target="_blank">📅 18:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78659">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">راکستار:
نسخه فیزیکی GTA 6 فقط شامل کد دیجیتال هست؛ دیسکی در کار نیست (البته فعلا به خاطر جلوگیری از لیک شدن بازی)
- پلی‌استیشن: GTA 6 بهترین تجربه خودش رو روی PS5 ارائه میده؛ همکاری سونی و راکستار گیمز تأیید شد
-گیم GTA 6 روی PS5 تقریبا بدون هیچ لودینگی اجرا میشه!
-ظاهرا داستان GTA 6 مثل Red Dead Redemption 2 به صورت فصل‌بندی‌شده و اپیزودی روایت میشه
-بازی GTA 6 در استور پلی‌استیشن به‌عنوان یک تجربه کاملا سینگل پلیر ثبت شده
﻿
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/78659" target="_blank">📅 18:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78656">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79017d5ab5.mp4?token=LgE4YQWYYWrdtm4nVKMNoAbRxA4CszNcdHa91fQUInuniV34shcn0z2KRRrnZTa63gxMQvUT05EFghfWD9l0BL84Z0ndJ3vvGtHBf12QW2qjZjXnliV_OppnjyVq0-q5rbIqufMcZI0qqnJsFX7Z9fDQ18OtMZ8raFCghXgSX8A4aLcApYCLsolNufo1PpVgcrk-wNrnHYS5O7BIC-aHBHufZpi-S0f64BoAU4jXg51Ntt3NU_IrL6yY6U0kUvQdsdF8oTU7-j-GugCHP_w33kAeOuaEqtbcFtrkqG7gA6jKiYz6bYa7nUA3F8yECV5Sv6MrVhrWnNm2cSjKP6EB9Al-m2aEH_wX_-y5ZBSMQP4-XH6BhLSr1lbY8pQ-xnkYH2JiSIJdNX4oMo7f1ZWmlbD1dJ9dTVNIzIEz3BOGz6938P-6sKu1N4lcD34ieykwLT3sDlQNzCIR9F8yLV5e4a5z_T0S72xlkpfpNswR5WB3wDUG7CPpQztabcklYMgdtYU8bJ_K0xZW8TgHiqhURDhee1b5K992dFwnnMQ2ngQjHyLyTMiQ5PmABCcjyEk7J9i_ny3ORKSzBCMenrSfTRYaf65m6lLwqbRYp6aSHx4EXqLRjdVVt6zCpWsrSwPwCDaDL5Sno79nIZpYFFB8uX3X5rksXQna1ASwcalf8r4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79017d5ab5.mp4?token=LgE4YQWYYWrdtm4nVKMNoAbRxA4CszNcdHa91fQUInuniV34shcn0z2KRRrnZTa63gxMQvUT05EFghfWD9l0BL84Z0ndJ3vvGtHBf12QW2qjZjXnliV_OppnjyVq0-q5rbIqufMcZI0qqnJsFX7Z9fDQ18OtMZ8raFCghXgSX8A4aLcApYCLsolNufo1PpVgcrk-wNrnHYS5O7BIC-aHBHufZpi-S0f64BoAU4jXg51Ntt3NU_IrL6yY6U0kUvQdsdF8oTU7-j-GugCHP_w33kAeOuaEqtbcFtrkqG7gA6jKiYz6bYa7nUA3F8yECV5Sv6MrVhrWnNm2cSjKP6EB9Al-m2aEH_wX_-y5ZBSMQP4-XH6BhLSr1lbY8pQ-xnkYH2JiSIJdNX4oMo7f1ZWmlbD1dJ9dTVNIzIEz3BOGz6938P-6sKu1N4lcD34ieykwLT3sDlQNzCIR9F8yLV5e4a5z_T0S72xlkpfpNswR5WB3wDUG7CPpQztabcklYMgdtYU8bJ_K0xZW8TgHiqhURDhee1b5K992dFwnnMQ2ngQjHyLyTMiQ5PmABCcjyEk7J9i_ny3ORKSzBCMenrSfTRYaf65m6lLwqbRYp6aSHx4EXqLRjdVVt6zCpWsrSwPwCDaDL5Sno79nIZpYFFB8uX3X5rksXQna1ASwcalf8r4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای جدید هیپهاپولوژیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/78656" target="_blank">📅 18:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78655">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
پسر چی داره میشه تو این دنیا
ترامپ دو ساعت پیش: همه از نتانیاهو متنفرن
قوه قضائیه یه ساعت پیش: ازین به بعد هر کس علیه آمریکا شعار بده یا حرف بزنه، 1 سال حبس یا جریمه نقدی میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/78655" target="_blank">📅 18:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78654">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjQhhjACGp40DhTGm80rRv9vFyGx-leD0_uAq52Ian6E-xk8yCKFomXkm_ruIYQjYmcZZFl4NWzkv9Do6t-TUg2MVnnxXScN_MJXlILAlWs--m_rDDirPJgjvIzXX9yX6gAHe_9toV59kN0yvCC9Bee833HjmSM5drhdkKQr26Yz9Zge9er-1sEC6wDE2X0Et0Im6_lDGEiipwNsj0SHFIWS_J2_cG3AQZxHaS4-p3xBxPDoJrW65Wf3IqxyxjxIm6xQnMwhL3ORkCu_Iag_5eby3od9vx3om7JquoZ3p-bqvl6EB-ybZisg18hrb7a__LNU2fXVTusIeslL0GqkUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادا بخدا داری اشتباه میزنی، سیستم بدنی باید حین پیر شدن افت کنه نه پیشرفت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78654" target="_blank">📅 17:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78653">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzzTutoopQZctmoNPZK9huYvfCht6OQWsqyi57m6Msrp0lLmdam-s84EZXS2AVQ_NkEPuGf5e1xEeGHBTkUo8uo8_-BMS76ckkCQCO4xsQ5bBfS6pWg5TttEb0eiWxu9j7FxjGIBwWOinkiAUeRqIXV5CNWTdDuec4VUn73DSDlXaCL4NP1BL9HE-GbCeARHdRCzStIAvXn_f8s-NRQKrrgMVzx5BfhYJAjRawr73pv_ZndkjV8Qeu7BFrCez3wUXvRu3JfU9aPB8BQEbsu7ZzToMML1kmDpDqQMxxp7N1m36demH1btKF5QsfV9xfhbccfpUd9jpLFVu9PxaTaq3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">از این ۲۰.۳۰ روز نهایت استفاده رو از کل کل سر مسی و رونالدو ببرید، فردا روزی که اینا نیستن بشینید راجب یامال و وینی بحث کنید همتونو فحش کش میکنم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78652" target="_blank">📅 17:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78651">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نفت wti شده 70دلار
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78651" target="_blank">📅 17:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78650">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/222f81be11.mp4?token=QQ1OC8VuDfLv8Orq461alT2wRhdbzqU8ULgYLvUEaFSTqTrvSzAaaRx2Pst8IzT3EUnK_1dPIZL7zja_po8wrcaSI7tX3gx2-qmC7-VfKfeiMUQu7ST9VNFx-WhBhqjHXziTZH-T29nx4jgVWfoUQRM1WwEHdxEN9rqMBh8aL5F9Hv3G1V5edS7TxcyX6FPfyE7RK_PLzNrhWMEMIqgByJ6S9PNiiyXmdXUcK-A6yjnyjOVuERWLZBy-fqeflNROM7TdFdOOIlLp1kZWAF_OWvrj_TDfPABGQmKhZZAABw_NcK-yZ_I2jrXLvdIod5aDiRSj_6kAG2IhLhbjrrynAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/222f81be11.mp4?token=QQ1OC8VuDfLv8Orq461alT2wRhdbzqU8ULgYLvUEaFSTqTrvSzAaaRx2Pst8IzT3EUnK_1dPIZL7zja_po8wrcaSI7tX3gx2-qmC7-VfKfeiMUQu7ST9VNFx-WhBhqjHXziTZH-T29nx4jgVWfoUQRM1WwEHdxEN9rqMBh8aL5F9Hv3G1V5edS7TxcyX6FPfyE7RK_PLzNrhWMEMIqgByJ6S9PNiiyXmdXUcK-A6yjnyjOVuERWLZBy-fqeflNROM7TdFdOOIlLp1kZWAF_OWvrj_TDfPABGQmKhZZAABw_NcK-yZ_I2jrXLvdIod5aDiRSj_6kAG2IhLhbjrrynAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">که ترامپ گفته آمریکا میخواد به ایران ذرت بفروشه؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/78650" target="_blank">📅 16:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78649">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سامان خب آخه...
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/78649" target="_blank">📅 16:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78648">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxHIBbSafD8s6N1SFB6BauoJCQA6U8IKbCrFh76vcRPNq-2oyguCxh2VNGBTkD--cLyqrMK7Xv7IduJdsBds2rjyMLbBzxov59720sEN_bCwxQXheFDNhRXFrsbrGRN6fVaM5Mu6SUHHXTnM5eRSbRAu4Pyuj6xEuG_9fVusXqG1jQLpSEWhL3le3fP0-_8fyRlusUd8LxsE-wvaxsKu2wweu9vMZsJUlZyGa3CxKSruttEb2wt3pmVpdmE31kTZap686BUscWsJuKC2Ftc3-9IIHdmaU9lrPX7yZZhQvHr-n8ieSxA5KvjGmDGt1_Idl_5WPJfr9dbFMe_ezjxGUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام مهنام نواب صفوی، از معترضین دی ماه صادر شد
فرصت ۲۰ روزه برای اعتراض به حکم داده شده و اگه اعتراض مورد تایید قاضی قرار نگیره، حکم اجرا میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/78648" target="_blank">📅 15:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78647">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">5 گلزن برتر جام جهانی تا اینجای کار  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/78647" target="_blank">📅 14:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78646">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzhTPu2XZRboFkn8B7PX3WWn4HkG2drS9mYeEQv-YdVbyOeF29eB7xB88fX9dNTubrIS8UjVgmAGvd6jUpDiyT23SVU2AVMSzBECvaZ41emkXuiNCZ9I2-Y9_EAfdLlMOcGyQy_GolI12hKuv7bakXAAAmSEtEOSxBsI88MltWYOjfkG1CpeHrxdVWIAOEGHNBIKSWOpwQDb6MK4-47kGhOv2tltOY3G7QvqEJKqGPqDRtQ4gMmWWLYbmjlVongcys8oreHJEBxXkXBTS1R33fVTT3YATsItc-VJ9nJYtRcJpAija3wCtAjgf8Kx00MvwUG9Y_sqZBkzW8b53wZe-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 گلزن برتر جام جهانی تا اینجای کار
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/78646" target="_blank">📅 14:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78645">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAqrnDxLFfzZ5pXFUrhAhOxsviFWqgkllycbqKdUMHcqj-_74AtwHjamBqmVhm63cyWbwO3bNtQMIa8o4fYKyWiWAhxNdz7kJ2UyayLHByTFF8zkkKVG5Ew-exsLf8dLq9yKfBn-pwdhQ8A-hhR5toySiGowC2zr8P_p_61V_dxLVAIBkmoHIf8uKPh4EmaoI1SCYLahAAWUCuDp7L6edlCXf7rv7wO_B6B70mggGSjh5B8ufAH8GxP5cqBc0irdDdakHgcv_uTKBxWL0w3z8NSdn2x49ept9wSlaUJPS8RnrSFWK_EgyJLy7JDSC7rCJwqpozUXLCblxCFdR6LPiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت بازی GTA VI مشخص شد:
نسخه Standard به قیمت 80 دلار یعنی تقریبا 12 میلیون و 800 هزارتومان
نسخه Ultimate Edition به قیمت 100 دلار یعنی تقریبا 16 میلیون تومان
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/78645" target="_blank">📅 14:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78644">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">قبض تلفن تماسا تتلو رو کی میده یعنی
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78644" target="_blank">📅 13:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78643">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">وزیر خارجه پاکستان: برای عبور از تنگه هرمز، هزینه یا عوارض یا اجازه یا کسب مجوز وجود ندارد.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/78643" target="_blank">📅 13:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78642">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mt0tCxRiOsuNw5wnTpZkXecEaIPi1MIcnX_SndP1W7L4LBVKr3A9M6BHVYVUQl22hMWi4WzV3LIOZHfaUdLIuHuOnakUA6CoXtzXsgdzTMqFqJmHADh9W3TswODS8CZiC6wICFE_fFIZrZDHh3r5UcUnTl7-0fCH1nakIkXdAtUIry9ajKA1MkyxAIevRfW-Ogq9GfX5C0kpHZQTgLo1VidPFfgUs_psjHlXaG-ypqLcYIs6dfP54lwEFCO9yyXgNzpJ1wbjobnAwj-v5P2ZnZIgqL02XtyuLUf7y5q4SJpWcMuAE-oM90dwzxZEDVvK5RPfkHwIj5KSj1tvqCFkGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو مغز پدر مادر شماره 2 پاناما چی گذشته که اسمشو این گذاشتن
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/78642" target="_blank">📅 12:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78641">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvvC_vd4sZDdf8NbBegi3Wl1dTySmn8iDMWdeghGZLPRtQdIfdzn0qUcwnkntDBH7blT_cyMvOwH5q-4px_kaaZXJzw7GM25XjP700VGpzvs_rHQkLV-2lNDaLjM8wRizF9OHpDcwdt3E4pAJoc47aIwNrP3B_elyW6tB_45l6z9J9UFoJTOe8Sg9m27xqCADlXaPb4tayWZba7NNAFI7eYZicya1eeUtiglzk_AC5_vrwojzncYnNBoPcO_CbTJvRAwvzMWyaDVphbWj50oCHzKXwoqwyC9hBbx3qMwwNiPd59grD_S_mItrdDXyPTVjIeens4_OcsfzAfSl98nww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچه سریعتر شمارشو برای ژنرال گیر بیارید
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78641" target="_blank">📅 12:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78640">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78640" target="_blank">📅 12:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78639">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQq4yNKFveaBDZf7TO4xujK4BKh9Xazygci5xaGQpRp6aG6dp5VvtHX5wCW9GfVABp5L1DBCe-16_S7qe8xA_nTB9yAWh7TZgTbAa2ggufvavbx-bLGgiCAU2RSYh8lZMjjM7pOdeIomtpfM-4pHNSB6QWwnQqIW8ba-HQdcgrOaAE9x12h38Eu6D7vcR0vGm81b8LEVvzxGHPtdPx_XuLjv2iVFXGuB16NWD4wKhmiPCOjkphkut7xTabw7jDWGLCtnunNJULAhNGA40zeL2Vu2o-e_4tFVLAN2Qeb-eWY62DQP8gQo89GBmehNdFZ09YgNszBtumuxatEvFNoqFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/78639" target="_blank">📅 12:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78638">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">و تمام
انگلیس موفق شد غنای آماده کارلوس کیروش رو متوقف کنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/78638" target="_blank">📅 01:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78636">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">توخل از سبک بازی کیروش کلش کیری شده</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/78636" target="_blank">📅 01:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78634">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بزرگ‌ترین اشتباه تاریخ فدراسیون فوتبال ایران قطع همکاری با کیروش بود
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/78634" target="_blank">📅 00:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78633">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFN9ZEpihPVi8OGa6icjMMkwnD3a3ZSMgSoxL2-jL4OQRPPWlpGyH7Neba2HLwv1wzV4cQFLQk-IFPQZ_Dpq8KoNqMSoFvIshRZj0tWtuowjL7msfbmMSYw64WD7kUJGoT4Abn9O4XBU7S8x8YhZbJW_QUuKjixsvZmc3s3KSvI7wPpcxYpUUwT1PKX6ZRSwbB6VbNou22DenraN5QFTmCiDWj75sV3rUiDUZGsikFm59zfx5bOEoGvsfHs0Ddnv1P7mxSomboUMlz248Zm-Drmex1Ni3xxfNN48WGq8Ix225UR74AqEctBk1_zy0limOfH4wRt_DZaF8o_EYSgiGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز تولد ۳۹ سالگی بزرگ‌ترین، بهترین و با ابهت ترین بازیکن تاریخ فوتبال هست
مردی که با وجود خودش به فوتبال شخصیت و اعتبار داد
تولد لیونل آندرس مسی بر‌تمامی فوتبال دوستان عزیز مبارک باد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/78633" target="_blank">📅 00:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78632">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">کیروش عجب تیم سفتی ساخته دمش گرم
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/78632" target="_blank">📅 23:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78631">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d974a39da8.mp4?token=OFEkzM7154djNhcFzX8UEalS7YOn6EKfknpSpPwVmrp_8GONJsVVLmegvQ84nZf_pDZ6QAlpa8TlRKrgI13A12uC2fvBqGFEueongNPnmWlue8aewbr1hqgwEKLc5RttGHYrm5Poz1Dg4qnEctQY_80iFpKZm0mWLESquhhu9BAFXx0fNehrS3ufJNrzw4eofz8TWn3G9u3rVEJcVzCDUvP8mHPbfXih5xYUEp7SWyZx46pelC25_YnoX_cQE0ymH2ULvm7j6GGeupheO-SL7XBB-cS-rM0-OHlHHVJ6Ijx1RddgJ8VCeIDz6fbmI9LY4sIIDRuCuubQuFNHOhedqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d974a39da8.mp4?token=OFEkzM7154djNhcFzX8UEalS7YOn6EKfknpSpPwVmrp_8GONJsVVLmegvQ84nZf_pDZ6QAlpa8TlRKrgI13A12uC2fvBqGFEueongNPnmWlue8aewbr1hqgwEKLc5RttGHYrm5Poz1Dg4qnEctQY_80iFpKZm0mWLESquhhu9BAFXx0fNehrS3ufJNrzw4eofz8TWn3G9u3rVEJcVzCDUvP8mHPbfXih5xYUEp7SWyZx46pelC25_YnoX_cQE0ymH2ULvm7j6GGeupheO-SL7XBB-cS-rM0-OHlHHVJ6Ijx1RddgJ8VCeIDz6fbmI9LY4sIIDRuCuubQuFNHOhedqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهره هوشی:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/78631" target="_blank">📅 23:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78630">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">واقعا افتخاری که تیم ملی نروژ به اصالت و تاریخشون میکنن رو میبینم حسودیم میشه بهشون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/78630" target="_blank">📅 22:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78629">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">این سری کیروش کمتر از ۶ تا گل از انگلیس میخوره
بماند به یادگار
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/78629" target="_blank">📅 22:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78628">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">شانس اصلی رو پرسپولیس آورد که کاناوارو به اورونوف بازی نداد وگرنه درجا تمام تیم های بزرگ دنیا مشتریش میشدن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/78628" target="_blank">📅 22:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78627">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">بازی تموم شد مبارک رونالدو فنا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/78627" target="_blank">📅 22:30 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/VmhfVL2HADI1SVl6IBT3WQTyMJnaXcARXt6JqZyF6GbbIGfyAX_I17vYzDNucRinoYs4OmChMrpc1mcfOvOSgZ9l5H4ZGtWgUG5kOSYbpx2WGbyU53IqzS1TyLLJ-4msjlNqoV80Wu27nLJfAPoCbhUQRu9ycPv0S-SpuOVjMC22_Pc3vE98MObMg-wd13k2xSXnWiLNSkXOH9x4qYs0A5X356as8rs1TwJLfGkRl4wP2Qzi-cfN3n7VvQ6_vwGkTAS3fNc3eAzVLoDfBGIYlp_AD-oi6dLl1xHKvx8UCndUg-lhpEXAwKBpQxNR8Sc9BDi8r103e5av5gBrwx0fAw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 223K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 15:09:19</div>
<hr>

<div class="tg-post" id="msg-82111">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ویسای خلسه یه جا خطاب به خشی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/funhiphop/82111" target="_blank">📅 13:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82108">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">وزارت خارجه پاکستان:
پرونده میانجی‌گری بین واشنگتن و تهران را نبسته‌ایم و امکان تمدید دوره ۶۰ روزه در یادداشت تفاهم وجود دارد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/funhiphop/82108" target="_blank">📅 13:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82107">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bv9-MYHNjnCW9GoU49NLDfWIQ9C-Lj6PDhF91I4ZHljf2X4kcLmrmTjsIB-1KYK-9QjbJjrneDSJC8gcnx-4vOwpVmh7USwMMLUjOjweGfaZpyUuTg5oPe5SGo0ZIuo21TP3L8SnCNcGTy9W0bw1VJUE2ToypEnriNgCxgvH5WM3YS6SMVZs2S5RshukUyj2Jrp7H1vC--wEbPIVBBqOz1WkWDg4h8m2bao0D-_3EV5odq88pwmcgkje1gCPvXwdQrS65NkU-xn7ReOOrXY9LMIeuQPEK7dyH98Aa5b-dyw-U1BgX0FDAiLSTJN3iwZ3oOqAdgKvH55iHFPToo8BGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو به مناسبت عروسیش یه قصر چند میلیون دلاری زده به نام خانومش
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/funhiphop/82107" target="_blank">📅 12:09 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82106">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJQn-ksn_Nh6YDG0ynD_NfEYMkzTvq-nMtaCzG9ldgmOaGVhXnnZ5bmfdm5ncFSEotAIEjuBH_m8RlmUeXkI5NOS29MLFz8d4ORNHNEPvwJlqAwRM-rm3WEgcoZp9NUdwLMBUeWl_JRa6SWix0J3UTgZDqVIBfdI__BPGsHN2hVrTlau4ZGNeyaxGMkzZj-TCFuYDOv871K9d9YAeVqkaKKW4AHakYMVMCoimnBaLEd589HC6CjUsn8I6bUTVK-GxYAGiq6zCSoG5p0ESfq3mlg2L3XIUFXLO8ZnfgKxoEZ8ig7Ib2CEADXGIc6u-1H4rLpazELyNt6_bW374QIt7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
پاری سن ژرمن
🇫🇷
-
🏴
استون ویلا
🏆
فینال سوپر جام اروپا
🇪🇺
🕔
چهار‌شنبه ساعت ۲۲:۳۰
🏟
ورزشگاه ردبول آرنا، سالزبورگ
🎲
با بیش از ۵۰۰ نوع آپشن پیش‌بینی
👆
با بالاترین ضرایب پیش‌بینی
📊
نگاهی به آمار دو تیم:
✅
پی‌اس‌جی در ۱۰
دیدار اخیر خود، ۴ برد و ۲ تساوی کسب کرده و در ۴ بازی شکست خورده است.
✅
استون ویلا در ۱۰
دیدار اخیر خود، ۶ برد و ۱ تساوی کسب کرده و در ۳ بازی شکست خورده است.
📈
میانگین گل در ۱۰ دیدار اخیر پی‌اس‌جی ۳.۱ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر استون ویلا ۴.۱ گل در هر بازی بوده است.
🧠
آرامش ذهن، دقیق‌ترین ابزار تحلیل است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r21
💻
@BetForward</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/funhiphop/82106" target="_blank">📅 12:09 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82104">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Foj9xasy680V36xP3WaPfbZ5qbT6kgSr_6bkk7JYwPjqdW479DgMzXE6W4jHJrX_TWFBMoWOo88fuSCsDD7keQngCj7Qg5EQJiNMmZVm2_KxT0aNWQRd-D5Xcj5xdQZ9atp2tZVmPW7pmz-WRDVstXXyJIHQfOaC7TawtM_9Or_-Yr9t1VH11bzsIkCZBMHeg3JwKE-yrMBb1mHKnSccfqbzXditZJVtbj6sPiFV20S63SDAR3-ZF2-kDtfTcjKzAS6XbJWTV7ONgg2lYG6KCLbNyqYs2D6kNHHPrCv23WKf2LBSSCXlcV1O1iZdqHBjHEYg3y6IN0NMQPB-E-JdOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mLH5gQl6ZAgjojf_U80WaR1buwLMxt8DzbhNp-bYunB3dgQUj1pQvXmgjk0ia5CbsROUx4GRddqMEE5Ex7knXuGGeu4i67pr1YYOEkMT5IoYMI6o6sa5nShz0QFLoSBFFH8jC8Snn7OnW5Q5zFquJ3aYd3qQ3MKYud8U8i00AZSrU7zkTOCnla8HEH4271CLbLGLYi_owFmhX9n56H60atcZJey1Zu3TTigEmHdSRIY8i5lIHWhZ6g4Jo2asu9xIJkEFd9svk1DQanctYyn-97Pf83tMQrrAzEmSJwY_67yFJr-g6QR_Ba5TaWTyuQTEsI04d0OrI1o00CSk7991-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پسر شایع نسخه مینیمال خودشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/82104" target="_blank">📅 10:16 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82103">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2be999c32f.mp4?token=sKPBBIPqXSkn3sRvGuzKZ1hgy5_POHZmJO3Y-RuMeRUnyCI-1frOuxeF6N4_j4GEXWwHQFsSYmZKmHft-rTgZRphDn5dYpcN19RIlyiCJlSyzRFJwsTCLX3Ut1NTKR86HbGNaZB6D74np_u3CJzwhnEZqYCPgL-HkIWoQ0HwtHc0kS4oUd5VmcJ-vYtyLtAhy2QNsZRd6f1fbBofcSwb6BY63kWCun4ILypRg_j2CL8pTpWG31pVIbHzijUba1DKWoYaUh42IBhM1_d0nOqOvN4wyn2iy_MhjvwdLsDtJPrE32QjUEIc4KZlN5AsDPuiyIGDPnLqBqzt77WFHXUm6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2be999c32f.mp4?token=sKPBBIPqXSkn3sRvGuzKZ1hgy5_POHZmJO3Y-RuMeRUnyCI-1frOuxeF6N4_j4GEXWwHQFsSYmZKmHft-rTgZRphDn5dYpcN19RIlyiCJlSyzRFJwsTCLX3Ut1NTKR86HbGNaZB6D74np_u3CJzwhnEZqYCPgL-HkIWoQ0HwtHc0kS4oUd5VmcJ-vYtyLtAhy2QNsZRd6f1fbBofcSwb6BY63kWCun4ILypRg_j2CL8pTpWG31pVIbHzijUba1DKWoYaUh42IBhM1_d0nOqOvN4wyn2iy_MhjvwdLsDtJPrE32QjUEIc4KZlN5AsDPuiyIGDPnLqBqzt77WFHXUm6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تروخدا یکی از دوست آشنا های این ببرتش تیمارستانی جایی درمان بشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/82103" target="_blank">📅 02:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82102">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کیر تو بارسلونای بدون فران تورس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82102" target="_blank">📅 01:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82101">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">علی گرامی به کدوم قبله قسمت بدم دیگه نخونی؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82101" target="_blank">📅 00:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82100">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmir</strong></div>
<div class="tg-text">چشماش دنیام بودا
دلبر بی ناموس
🤙
🤙</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82100" target="_blank">📅 23:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82099">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cpd0Bd-kBfB-MP45iYldJzE3f_xrF0fvOCx3H4cZ-eL0FBnPkzkjOX9footsDXXKcMOM8OG47gZXl9hQimM3lk14ssbITdKrE8FTcDMbroU4wAICHwRJ9-qGsxtFPoEfLCcP_e0Lj8vfRPwfiAGhioU_xKxtY7lPWNTEFHBAVS-JQAJvc_g_-qKRIDZxL4RD6KIeq0Tsj6DIyfJHPPgM8NEjf1-nKyGZEPrV_liN4ChkKUV0HHSxB3PE3K4-FGJjP2_c618Z_d4nrb1whXZmaLftUD8PRya55LKrfyKcJMvKZtQ3MiKBIjh2A9LWWR9r4A-eS3cTUCaIfMLatCIfbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس فقط یه کپشن "حسبی الله" کم داره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82099" target="_blank">📅 23:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82098">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNoah</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMoIPqbAlCag2yVEMzVDawQ6ZgqN9pS9yekREUmaVa0GMrk4Yw1JYydoTPRtnQBp84GNrYxD-McHxvha7xUuU3PB-IBiPj1XpFzZVu1xcePWfAWI8CSi7w-2TmEypoQKHmwgr6f6YlX8JOyXYUOZ4rp_vD5vy6iJX9rMT2jTInviePexRs_ylWe__SGohXgFJBAYE9mBwwA-toksmK0da9fgEBx1NicB9YLBnE1YwhNGMwaEIB0iHhZRcUIM-xOXxT7qVBP1OgryX6hIqAYGMJb17-AP7hzPZxGV5q8lQBR7F2qcldBFn5v01FMqxoD7wrn0mZ2Eug1i0x9kD9kQLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو حرومزاده یعنی چی که اسپید رو دعوت نکردی به عروسیت، من بت زده بودم روش</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82098" target="_blank">📅 23:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82097">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSSuC9suB7PjCsJZUntRqN4Uw3wGFYs6jKVdE2oD698q4HD6IBBEOXOsbHhoqG-BCy8EgtZlibrHE3D1yWj7Kn1wRGKKt-_dYJQZr1jE6H0RRQDcwSnw2G_VFLaU_quH_pa2ZAz9WtOZbdAq0Vd3g4kMU3bk27gNJd-MMZjMeBpLBp9vez0vK838kJnbyuoiOkc7yFkkQJ8QGWORbD6OVWNNIexazaMgrYgWfuFDjrejxXOIYXx2YbEaKzN8SNWjXLNaCd3gw3kSMaVJebpbwqE7yH8umTXr1JPI1Ery6KM5aDEWhh2wg2OqktQkxWTg1ZyjXl4jeQnewj0k4ATtgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این رسما دزدیه‌بخدا</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82097" target="_blank">📅 23:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82096">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">رونالدو و جورجینا به قاطی مرغا
هیر وی گو
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/82096" target="_blank">📅 22:56 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82095">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBxH4kaByKYJAU3U0UmXS8pJ8Remwos9xHu1sKFjMfK5uU_1cTDozD-tNec0lmfCymAEhtfnoMhCFqzkBeK2EzOGW6CQjpqwS3gy5kNz_XsBvakgShurBgW1ZOn0Uo-m_f7wRDtqC4Pjw8t_Gguu9ZS26gl_jkf7QQ-NEHBb2pRjWXGh0F7cJLvRz2_sWAzpNOSpJX9Gk4x3jazTXYWkkYQHjtcaRXRHHoiN14pLsgfHajXPO-k-WwvepZSnCvkH6VzkmO3283wrRk09ypOeoYfGusnCrh8vDVg4L2KYlsH4aPepgP4BL7zIEOwiadM_K-vSALCl3pHGYxNt8ShqTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داود کیم، خواننده سابق کیپاپ از مسلمان شدن میگوید: صدای اذان در تمام خیابان های کره شنیده خواهد شد و گفت امیدوار است بتواند به ترویج اسلام در کره ادامه دهد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82095" target="_blank">📅 22:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82094">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">آلبوم جدید خلسه به اسم " Margo Zendegi " منتشر شد.   SoundCloud   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82094" target="_blank">📅 21:07 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82093">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">آلبوم جدید خلسه به اسم " Margo Zendegi " منتشر شد.   SoundCloud   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82093" target="_blank">📅 21:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82092">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mST0_T0QvG6jSeOqJNW27_xmgEOLZ6Gd2KDmT_MrexTyCL0tHRrQd-jf4Jzpp8xNG3MDPa-go40tme6m5BvF-i2FfrSGQhBQc-LZ67tYDztVzSqxwDKZKlGG-5kIW6gNK8fEl4y3X1eRbjnJhLYAXR_csDXz6OXuQMnwB1dJ33rfR9YG3zyzKOc_F9PzmFt9fbEKvg8_fwy_zD4O1KVZO3cwSkBqwoRpKef8I5NCpEK5184TARwxRSjJflIBxAPjPnQ7JFObYO7reUq5JKdItF99RLaHm_bgOq7T3_0aIY7ecnxpUlj6UgoYJdOJGaYTnnqRyAGrUjZJ90raiRWTMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید خلسه به اسم "
Margo Zendegi
" منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82092" target="_blank">📅 21:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82091">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNn80o4h5JJ2f0ZTQ8rOkKsZZe6d_QpvBb8yZaDskohLxs4ifohb8GRa3LGw-ARMc0Cez3lBAQ2lZT2CjQSOkA5v1D_VscsVqSZGDGnrpMTcX7azNn90T_q30uD3dF6uCUdk0wUItdX1ePPoCF-Sha6cAXwVj4n9EJORbsdFn6XyIbNleJQ2tpN4Th1VFnrM2KQQHJKKJvIgZ-3Sa5SKOHLtVHlXl3jqfwuCETUA0HerCgXBM3Q7RrJCqJFSsagdJe6Ddbxh4yOamGGJ-q0zGdaobCTkdPQoSfkasggc1pLcTfHK2qtvYan9xnEd93BviJD1wd5Jz8JVxZ6UAGohLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#ایده
#تتو
#مهدی
#پسرعمو
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/82091" target="_blank">📅 20:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82090">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbIpgzBnD_XGC1zDVVmgkLNAOztpr5UisnlK4aa-zNg_OBk8-frtjKmrZHZ5FbK3PQjg_tMKRkrVmQyuPKvZfSEW3w0ioM8xhlwTKsrl3-NT9xN-WMi_wrkfgKh4hzC1IBDVlOcK7d0GC-dNZhxchELTjqja18vYyfLiq5tp6FzQzUy8R1rrkKPDtdWFf6RgE1ngIJ2GE4HFsCbq3ck3-2mgvUtqDMf0BwTqaKVSnxg9bJnM0n9fpobSAMQW7VjBlAYlh8mfuZ2zRYMuQDheauqhA0vNq6PjKOf8KvoBnw0zFg7pqnVgKll43GZrZhkphe_mYcTQMO3QEmoBA95skw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علم‌الهدی : اونایی که داخل کشور میگن جنگ رو تموم کنید، یا بی‌عقل و مریضن یا منافق؛
فکر نکنید اگه جنگ تموم بشه آمریکا دست از سر ما برمی‌داره، حتی اگه همه‌چی رو هم بهش بدیم، باز راضی نمیشه و در نهایت وارد کشور می‌شه و حمله زمینی می‌کنه.
@FuunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/82090" target="_blank">📅 19:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82089">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuaykhXvoRXpnD-s7utqsX_bFKbbOcFttR0y76cwifxElIUZLqdLM_aP110D3vm3-y02EsAh_lsqyHXQAn52zqczs5pw_HYsAn_Q3F_ysdmi733y0TvOmHOfmOAuk7X08sfqm024qKJE5PN6-xqzfGrb6megdvIg7Pjd8P2yDSoy17pF54QHwAlfneydkrrRy6l3yIkKlLvCVgZZgywLt3V1BgFJysuYgSHOz07z3SkiFuvooEiMsSsacNNicXFkRWPltaN8i6_JqAlssdANancvtEAcfMgnLFGSkV2z3wDcL2KZjPf4GVHWcQKI7sqIq1VIy3tz1Wq-dY9coQsNVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دولت لبنان رسما مجازاتِ اعدام توی این کشور رو لغو کرد.
مجلس لبنان با اکثریت آرا به لغو مجازات اعدام رای داد و این مجازات رو با "حبس ابد + اعمال شاقه تشدید شده(احتمالا کارهای سخت و اجباری تو دوران حبس)" جایگزین کرد.
لبنان اولین کشور عرب تو خاورمیانه‌ست که مجازات اعدام رو به طور کامل حذف میکنه.
@FuunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/82089" target="_blank">📅 19:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82088">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iviyk-1qf4LpSwiMgoglWGO-RZBI_MlZU8ZWT5qQQZptzpvByLP08R-hvxDd0mP8_SqkkGxqTdxEcs4o2oFlUYf_f6bWmenAXXuWET5peU4TCKh-mQJRW2aY_hzzJYqw1kwA9t4hfCxp-A0Ubt1bpcUJl4PHy5UoQQ1R104tnpfWt4oOmoMJ4n3OHjd-ZfRXENT6FI2uwwCMYHV8GZmSe0Zz-p9etSADsGeMmt_j8xHs5VQASOf4GqNucmjLDUfoZ25TnlCdSSr304YCeU01nxeP2BrWVZmm7PxiBKQhtLwBr8WJ4jgSqyoKLXVGvrIxqCSFt5pPlHlrDhRGnOq0zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
رقابت‌های مرحله مقدماتی
🏆
لیگ قهرمانان اروپا‌
🇪🇺
⏰
سه‌شنبه از ساعت ۱۸:۳۰
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡
ضرایب شگفت‌انگیز
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r20
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/82088" target="_blank">📅 19:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82087">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اوه اوه آریا یوسفی از جنوا و مایورکا پیشنهاد دریافت کرده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/82087" target="_blank">📅 18:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82086">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc87bc1a00.mp4?token=JLUGIKVSo3ibY0_yINOplG24mOTuZGdJAXY4qqyuwkbjzKW34_CBQIaoIc4wkC2XNJOmHfg2EdPQJkFwbGGA6obwxFsDrkseqNnJgEpwSAzGPmMDt3q2djN4bRzmqUG6aiuZAOcvz8Vj3XMcG3-KEvijwdLgSu0uSo2nR1POcW6wjkebcla5gOFW6i7gU4_QP9-3g0GTgUbHWV_s0hV1Pd3-fzlNXJbse8m3uEdi22H52a5XLWKz2m4kei8W06Y-2HOO4dqCEHHQI4j6zyJpth_YiJJ5iM7KdpyTU-Z-m-xWpUOyzbxXPCXvX8LlzLdTD5ocU9LIF2foL9dlbAhdew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc87bc1a00.mp4?token=JLUGIKVSo3ibY0_yINOplG24mOTuZGdJAXY4qqyuwkbjzKW34_CBQIaoIc4wkC2XNJOmHfg2EdPQJkFwbGGA6obwxFsDrkseqNnJgEpwSAzGPmMDt3q2djN4bRzmqUG6aiuZAOcvz8Vj3XMcG3-KEvijwdLgSu0uSo2nR1POcW6wjkebcla5gOFW6i7gU4_QP9-3g0GTgUbHWV_s0hV1Pd3-fzlNXJbse8m3uEdi22H52a5XLWKz2m4kei8W06Y-2HOO4dqCEHHQI4j6zyJpth_YiJJ5iM7KdpyTU-Z-m-xWpUOyzbxXPCXvX8LlzLdTD5ocU9LIF2foL9dlbAhdew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رامین رضاییان: طارمی بخاطر تیم جلو بلژیک  گل نزد که زیر فشار نریم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82086" target="_blank">📅 18:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82085">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75d87d048c.mp4?token=aM9wwqLpS3edAZhEV5XgsDCo47Li6vyA4Qhe5vvogrN-Dd0Hg2tdDRJogILaR29AuHB0oh5wqiKmPa7eDNk9d8qJrn7LAQrExC6QPetIQ6njPc-zZ4_hncG18aywSc7W0GNx5qbxlZHgmypT78kUSBNvrfCUvH6bvhq0EyQh4Z6vX4q4E46Y8aRmvxE5EMcoGjBHpRS48f3u9NK_4yH1bWoS9OVc4SPFixctZ2z-GSh3yKapyvMxhLttkp8gSwDZgQl57vtCTlnv0dm8wAJ4oGd2VT29-Pm_nU5Z7qGY9ibtrFwi3M5ipEulDmgtczQJhP9wEJi_GghCc-boA9thaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75d87d048c.mp4?token=aM9wwqLpS3edAZhEV5XgsDCo47Li6vyA4Qhe5vvogrN-Dd0Hg2tdDRJogILaR29AuHB0oh5wqiKmPa7eDNk9d8qJrn7LAQrExC6QPetIQ6njPc-zZ4_hncG18aywSc7W0GNx5qbxlZHgmypT78kUSBNvrfCUvH6bvhq0EyQh4Z6vX4q4E46Y8aRmvxE5EMcoGjBHpRS48f3u9NK_4yH1bWoS9OVc4SPFixctZ2z-GSh3yKapyvMxhLttkp8gSwDZgQl57vtCTlnv0dm8wAJ4oGd2VT29-Pm_nU5Z7qGY9ibtrFwi3M5ipEulDmgtczQJhP9wEJi_GghCc-boA9thaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران چقد عجیب شده، تو دیجی کالا مواد می‌فروشن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82085" target="_blank">📅 17:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82084">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cgcn8F6VhqAMQqNvPP1M5ygI8LAYbA2MzevpJmDe6rrGR6W8A0Mqnlm37cqU3KcL3EbA2CfeQMhBnyCdiCBs4O4Jezl-TsiiHAnsxgxlrEko1pq72iBwC9g5hdas6hwcllRd4rp8NeGZmRPnGsjvJ50OdVFHBY6BXv2BQTw5xurhZNYO7xcaMi6jD2HmAP4bDNrjqWK57h_P-aNdCSdtNs92E1aKJh2A687WuhDgagDXrI_khmqJqZ1ToZ8EIct47-FtvUm47xt19n45xgqD-O5C6G-KmVubTCaH25Tv06ZeVeGE6j-_GI7_OVR5H0b7kBRmdyjnMQzBLfxY4rIe6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دورچیو
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82084" target="_blank">📅 17:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82083">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترک جدید متین فتاحی و سجاد شاهی بنام دو سه سال ریلیز شد   YouTube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/82083" target="_blank">📅 17:07 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82082">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dps5hyil2ID1RQ6Tyy4u6H018XqSy_c_eifXG8UyZnTPA1Jb2SBq6aI53S3UxgA0YF0CX-rZPzXR65Sarw2nbOsfQfY3uDsOb6paa3FF9_iYFu0zES5MgSjOg1JDRVBOUQgEQEDGPd_d610Jx2OiP3F5vlNB34FtN4oJEsUNKFi6lWfdu9pSr8xhYQzuxRXCLRQ5Du2OliRsBXNg3q3sJC4MHxymKWObUZTAH9uLUUFomWkxrSfkbCc24MoQFuqZRDy4O0FNNSVjAiSPaCuzwvhz5BhS2DAiu9vhIHTfuExXKMFRGa8YdIIIaGwaRcZCOkHXp5yoQsXBrosn5z_VfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید متین فتاحی و سجاد شاهی بنام دو سه سال ریلیز شد
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82082" target="_blank">📅 17:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82080">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترک جدید سجاد شاهی و متین فتاحی یکم دیگه منتشر میشه</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82080" target="_blank">📅 16:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82079">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترک جدید سجاد شاهی و متین فتاحی یکم دیگه منتشر میشه</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/82079" target="_blank">📅 16:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82078">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8AMd_k9AmOTOeuz3p6cMA_S-63UJhzpRSs3yxPtuJ0VBqCIBNAnuJKSGKruG_rLquOigbA7ZfZkv-LvqrISBqvonvexSgF6f4LQGiZwVafKJNHZ_baEl9haUQIfJna8a7FHg9RT40ipg7OWcSxXwnWiz036mBA4WqqSWS9SgTbR_7tDy1HKwVJS1AGFeETqEnVKa83QFeoCx-HXWI8OAToTWX_BFTfjKWskFWhvMyJMWsqoZP8wYLt4h1MEcMt5HAxJZKuhHDUChmLGhzucCq_y2FcAoWe5RBk3ALJnRcwX8Uco-0ZasCKkgLPcUeEYpini2E59lLMbgLGBzpi18Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیپ استیلر ۲۹ سالش شد  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82078" target="_blank">📅 16:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82077">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">بوی خداحافظی از فوتبال میاد
مسی بعد فوت پدرش هیچ زمان بازگشت دقیقی به اینترمیامی اعلام نکرده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/82077" target="_blank">📅 15:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82076">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGrfYWt4U4RAXxx3ViWmoL7DG82dxaql2N7fA3oQhMGVgQMol2RMojDht4YSUQbBD1wasEK3OeY2ysuUVYb1b5t2EFzdLX6VFREc1O-fKpIWlw8IxD1X3gjuuh1qIhknxHrkCY6irS_j1e4GqFijJOgLf07cNRscBwfFjmWWCxqrd9FeMfAw5UmvYzCW_Ewev-WrH9rxBBdJboi-VrxI4RYulh-pRw9FHpxaKO8p3GKsiTQw5v9z2rEWjkQcNqKk6I-RAdL7K15zeUcc7GAn3hxJI3NcS2SP0crgMKISwhxVEl2Zszi7Vp-ICLrRe5HgOwlBo7RqNbRmEpqmT9HceQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنجشنبه میخواد بگه دکی بیا بدهیتو بده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82076" target="_blank">📅 15:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82074">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rYoE98jlnrY16m-smKt2cVzMGMHDXRokkbG_LUVpt0VZVX3-B5ywNfD13dQMsslhTJ7yE39OoY1Uz_uhhr4l3AYcQ-6OQaD7YdbDZd67UDPn667T5rP1GDPRnUsnTyItg0JGvU1OMeIghiCsw0N66Jq0IIUf38eh-AUKWTstYrgI-pHkC7y48irtWFWoor0Iyz_ZjRaiwEvbwuRTHQDN0dPsF4HLHPDTewN78K6y-G9-LyRvxp1EmY9kyXmp5E7lWkMJ6BiPBU4aQgrJItSG4VA6xfcNu80MgEF52ZzJZ-B-Pt6qnBYQrM7FmLWmjpeFtpYi3wmjgoldvjtmXL9Gvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I7cJfWGUdLiQWFomUUyihKYt7tgNTR9ZewW3szY0mSbjF1RtC1Bfkasb6S0A9iOx_BTyViLi2ucVRe8Kl6XBAGvDh5NoyF4tJVO8ucm6xKvKOzLC0ANWN105m1dRX8gEsKMZ1qDUUomZJYUtS5l5Sy7qVFb6_rzK_vBHa3Ck7ia__e25UveW9gfYUFI6B510FmzpNeAuPie4qjXWVA43PeqmMWWaTcdOwr-NcYrtHta-6MuZMfLCAFmxDa6jO2X7Er0n2fa-1r4yaMl63P_IHvpOMBOrUR-mnQ9JobwPt7CFq1KsHJzV6QAl5m4gtmY-zZlohdTODq0nfvmgd-jgpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شیپ استیلر ۲۹ سالش شد  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82074" target="_blank">📅 14:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82073">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlA5MacPEgsh4I8Bt1ep1i6sShyGWdYjQw_OSEv5aRVu0duxGrUs9mnP7F2_AVNvkTBC715uEldphzY2UexEo1wSVAasORnIhyIk4TBEAQXOPTP6PlKU3CNK5GQsw8Lyd5oOL5QCOLgu2S3LxiK-khKS23jnIFzrgH3535J4GjQFUp9wg5xQeZfdQNITmxE-191PbbAbFDqcDaTMlwUi9hUnN3kB3CQTSsLUEnME7zgq7IC3mrxa5hTy5UBqwb0O08b-dI34FWTKXx7BTCc8u6n_fAjNLakoYPHVG1r3pkPUYIpCgpAWJdNyrj5-gskgtz4yroNweEznA9-S01zb4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیپ استیلر ۲۹ سالش شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82073" target="_blank">📅 14:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82072">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا:  گزارش از وقوع یک حادثه میان یک نفتکش و نیروهای نظامی در خلیج عمان   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82072" target="_blank">📅 13:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82071">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا:  گزارش از وقوع یک حادثه میان یک نفتکش و نیروهای نظامی در خلیج عمان
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82071" target="_blank">📅 13:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82070">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xq8Vky40tycb-yKPdF57Dd8xIscpuEIKIoeEkwlGefKtaeXz3XTt6eItFnHAS2HMIJ5ObHGP-lgFyYs8uJVQ2BX5IyL9E7lwBSWPOAafZMYt7w_JlOUgrA-Gd-aYtVAYPT2tQdCO_s4jOfu6lD6oVMkMUXH2QFDtCThkdRVi3SDcm6NZ8ACwnpR2e3cuQ0RbNcT3SDx2qSEhoJFdkKL7REDS7NtrZE7B17jlStfw_Gi2ZQsattWYxJvvIsnQcrXr71o_8PZp6D_M8K8YkjQuxOoXOgju3MWpIYpVeG-519j3rjGvEOaesVKrXv67w6MzcmeVN2f0n3vTNrGXK0iyNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویناک پولات به گا رفت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82070" target="_blank">📅 12:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82069">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZaVN5xhMTzPfeEWDGEfMSz3E8Q_7ffZ1pjTuRyyK9yO7EEGAyBTDndt-6IXgzrL0RM2OyLsOudmM-4m_gYqP8ifiXfrtt5-xNsujA_Wc_btyBttHuktjuaJ2pa6caPxG-tC7s3HWjZegpvz3pDZWf1SR910ZND_f1a31HIDEje2OI9wpKRHTPXz4Ggyf0bATDZo3LiRdoomu1VBXzh2E8gtxGIJvq238qZIdPDLAmLyog8G_ncLPI2HGpewdwMDVzkqP48dnISUfCzHX1sj4icJU12NY1LZMiaSrtYjs8CX1eEXLXwLZoYNHlQP5HDS0FlKjCCyzWqIf2kFczHpdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82069" target="_blank">📅 12:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82068">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxhX98R4aOjUFrF3z6RqoDKnkJzOO5j_xQSA4EMvyEkRVSLLoOCQXd4rA-vkt8PIU9c40XpIomoZqRYn-6Q6sx_GykMDC8mK3_8Hibrl4Orp1bQKKTfbd3ip2LpJHTM-B8cLHTdKmAcd3MLG7OpO4SYyftOPvDo4bOfoKVlvE6FljAptuGTF4Po3Pw4sIpstS-rB3itqkY5kq74pVaJ781A-pE9s8HAPSbbIvlCiy3f8NSIhtnttRrdZZ-9r-ATz5P05DJEwVcol2WC_zWWcL5yPeCxghc03-Y-WaTLrcau_htIWadRpL-1xJgZihjOzmeUAAXLyRaE3kRoyXR-RZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
رقابت‌های مرحله مقدماتی
🏆
لیگ قهرمانان اروپا‌
🇪🇺
⏰
سه‌شنبه از ساعت ۱۸:۳۰
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡
ضرایب شگفت‌انگیز
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r20
💻
@BetForward</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82068" target="_blank">📅 12:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82067">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKprnrkmi_6aJoC2UmlpKAy7tL3cYuD-7n5THFRL-6S6yqS8iKmk9sjFyGJH2VEejCTxZhgknpcrqiCyM1NgXMY3_Pnmz4VrHHOn3DknCw3nuklAp5ZtsvhME5t81UfI6ZGI9v3U29PTqsMLhqJQVlBMP_9y-q7tdehkHLElyRRo2XcS-uuUeFaujbY-Yt_lm8f916upCKmH5u3uzhLmRXP5qTeNqFqzhfju1ivTjI90QDA_KEGzQV5zMqzkAmBYE5VS2G09Ipts1Oax2VqZb38n9Fv-JguKs-vWjWrKINaCzknOYXGZWYa4CYJkUSHCDPPrNRa8hHLPsLNhYJ6V1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری احمد خدایی همسر جاویدنام صالحه اکبری از پیامی مجاهدین خلق بهش داده شدن که در ازای پول علیه خاندان پهلوی استوری بذاره و اعلام برائت کنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82067" target="_blank">📅 10:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82065">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">داشت یادم میرفتا
کصمادر جی جی و دانیال ددان
کوروش
❤️
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82065" target="_blank">📅 02:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82064">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSQZOQBYLRDjI53Q3CPMtIvwg4btvkBTeniZQBX_cf_4-Vb7dvgWgrLreN3jTZRlIgAvt3JKT1qMDGuA_TR0A4lMVIxO3MDGF2vjMaw2jZ-9B20EMeQGaOsr8qX1PfycB3Jl7AQYGaUnKqglkwuZjFN2bG-95S5A9X3M6SN9BUXgfr_99Xo83z3s80suioxLZGHVPRsBTowfNxntGra7rUxkbY7KyeJOxoq81WpWvMMv8wmXyAq0QVKs9nNmAWMUtMts6hWZ5yfiNZCLWrGs5Wa1OFQj5wolmRqnnJJMc3tKQuRXqq95fDKbxGbS8k8WaSvgFU3PnRI-AhmJi2ZqaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فریک پنج ستاره از ایران داره تکنیک های مارکتینگ یکی از موفق ترین آرتیست های تاریخ تو این زمینه رو زیر سوال میبره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/82064" target="_blank">📅 01:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82063">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دیگه حتی دکل سیریکو هم نمیزنن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/82063" target="_blank">📅 00:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82062">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QerfvtdFH8CMtNT183tocWEPNsIirTPVCPuZaL96YhGodRm48Sl9X1OJ28J3GXT4gS6ybnS-EYbnytQdKi9IOzvKoeMafyVLaOCoST_MZNAhG1wN10v60h3ky4Terl6fBcIMh7nxFBoz6TV3zZyUnXIv8-sv787DuvIcUHlMiuvQQiwpxTwga-3iSt1iQxCSx0bfbuAt8WnN6d7acr4Wc49S6rUPcoS7IsjpMPFVpsUGD9P-McxFenGKTwljz4ruugx-3SYod4rxtQRWZw764xF0jXsFS68aAVjripbEyqAv6Pgf4OinyMFpvEgR3KxJEXhmEH6vywN-hcb8Oqhz7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سطح امیدم به زندگی :
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/82062" target="_blank">📅 00:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82061">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">هنگامی که با یک املاکی مذاکره میکنید، بیش از حد چونه نزنید. _چمن در خاک  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82061" target="_blank">📅 23:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82060">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7XPpMsM-nAcVexo5KofIt0YB7NDF6K1UIlJ69aSzvEpj3o0plEYuQd1b5nE-Ku6u1lmHgGqlJ9xFTR-65aU2kwmuad05TyPrDx5hozY2NI3xfEmN0WINIL5XB91OTLowHVO9ONCT9pIS3Xz10n7MtEES-DrMpDLR2yFVO5OFo5hKrtyvpeDzp7WtBKsJ4UOKkPb5RtdLoVVnZshe51b-Xg-_X-H-3b3zegL9qxbAy2SdG6VjuzU25c9wxbAP7TibmKjXzHsjRiXnlxLqkRMOmxGJLUoesIjtwuRz7qwSqzsPydiy6RZi7u8_XuDnYosIioin9ZHVpxekBKXuJqLsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید بی‌بال به نام آزادم زمان منتشر شد
YouTube
@FuunHipHop
| فان‌هیپ‌هاپ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82060" target="_blank">📅 23:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82058">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUmG_L-gYJOJF8Z5-UA3A23lORYlTRL5suC1yhZhnehZ0giChAJ7bavhEdzVEd7ugqvrEI8d_WdVfK60wtNhdfRpNTBiRUWMKHwfDMvEwiAVmOW5uNNSvyxwd7KEq6ZvdZJKX-QTYfvnnEM3YxmFWmqYO09t-NwrBfaIPlLjfKUPqfUozHubnNMCs3vkT3-iBW7tEeP_XxXzAcm_wEI-QOtXGbNCgHLyrmGyW-Ech9qn6tzdDa33b6Ebb5rMeOH-piyCq510wGUXPAOr6CtYDvQlu98G_DTjyhClV7Nsxvx3Qiss-c2r8vcLQsXPpamHcWKfC2N74cV388R6SRPt2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پینترست چرا تبدیل به کرج شده  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82058" target="_blank">📅 23:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82057">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ عالیه
گفتن خب تنگه رو میبندیم فشار بیاریم، پاشد رفت یکم اونور تر محاصره دریایی گذاشت گفت اصلا خودم میبندم
گفتن خسارت بده، اومد گفت خب من که خسارت نمیدم هیچ شما باید به ۵ تا کشور خسارت بدید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82057" target="_blank">📅 22:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82056">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">هنگامی که با یک املاکی مذاکره میکنید، بیش از حد چونه نزنید.
_چمن در خاک
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82056" target="_blank">📅 21:59 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82055">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دختره انتقام رجب زاده رو از قاتلش گرفت  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82055" target="_blank">📅 21:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82054">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bf0cb6c78a.mp4?token=Ry8Ib6UFXrSy1sXEhh-e16dXCMMFeo6_y9ZHewVLVAQGtouu-F7dfbRw8ZFrRgSL-UhmyRONYh-LqCUFHpKMcwxQWbCzkw1aMgY3aY0SyJQxTpvCz6gYDLkfcYoIaNZG-fGy2oJvwi6qv7lu0RAV48L5RvorJA38k8id2aNlSC-p7jICFPuEO7BAWsdoxf5AuNikLtBfdKkYgyGPf1Lp0KcvkZUrc-YJMMBPULOViYedz6oZ7qpa_g_-acPSxqFL0qWZ0-ettKumy9Eq9lOO_I6SB7h0KV8gMTNNwmg0_E5o9lH1oXRWCehNgMA_sILhSLkA6OnxB6R_VsLKKN3QCw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bf0cb6c78a.mp4?token=Ry8Ib6UFXrSy1sXEhh-e16dXCMMFeo6_y9ZHewVLVAQGtouu-F7dfbRw8ZFrRgSL-UhmyRONYh-LqCUFHpKMcwxQWbCzkw1aMgY3aY0SyJQxTpvCz6gYDLkfcYoIaNZG-fGy2oJvwi6qv7lu0RAV48L5RvorJA38k8id2aNlSC-p7jICFPuEO7BAWsdoxf5AuNikLtBfdKkYgyGPf1Lp0KcvkZUrc-YJMMBPULOViYedz6oZ7qpa_g_-acPSxqFL0qWZ0-ettKumy9Eq9lOO_I6SB7h0KV8gMTNNwmg0_E5o9lH1oXRWCehNgMA_sILhSLkA6OnxB6R_VsLKKN3QCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختره انتقام رجب زاده رو از قاتلش گرفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/82054" target="_blank">📅 21:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82053">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترامپ:
-
من می‌بینم که نمایندگان جمهوری اسلامی ایران درخواست غرامت برای خساراتی که در طول درگیری نظامی پنج ماهه گذشته به آنها وارد شده است (آغاز شده است زیرا آنها سلاح هسته‌ای نخواهند داشت)، حتی اگر هرگز در هیچ یک از مذاکرات یا جلسات ما ذکر نشده باشد! اما این ایده جالبی است زیرا اکنون من نیز از ایران برای همه افرادی که با بمب‌های کنار جاده‌ای و بسیاری از درگیری‌هایی که به خاطر آنها مشهور هستند، کشته و به شدت زخمی کرده‌اند، از جمله خانواده‌های کشته‌شدگان در ناو یو اس اس کول و هزاران نفر دیگر که در جنگ کشته شده‌اند، غرامت می‌خواهم. علاوه بر این، باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است، غرامت پرداخت شود، و ۵۲۰۰۰ نفری که در پنج ماه گذشته کشته شده‌اند را هم نباید فراموش کرد. من به نمایندگان خود دستور داده‌ام که این موضوع را به طور جدی در هر مذاکره و تمام مذاکرات آینده قرار دهند.
-همچنین، در رابطه با مذاکرات ایران، ایران باید مسئول خسارات و مرگ‌ومیر ایجاد شده برای مردم لبنان، سوریه، یمن و غزه باشد! رئیس‌جمهور دونالد جی. ترامپ.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82053" target="_blank">📅 21:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82052">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0ejUZtI3wdDuYgUTuCW5w45dg-o3CHQaMTQmY9-jBBs25-ZmdIF2SUyovsLXlFMU1wfjkc4WN3-zSXV9GXdiR9SPA9_MdatS_BJ3_94sMQYGcO0P2xK9-qaBgR7YL0JyzlKB3r5RHSQfSWYUvWSEyRMY6TzDTF8ikKPmFsm0YhoC8yOLJoLzCLqUbUElPxu7q5-qtnCLdp5xdL-Imm4eSvRJT-9zLqdjeHwniUWIQc18NfHBMMH4tQESMSwq6mVP6OSEScJui4L3KLXQVEwvZjh9AMlcAOJzBLBp56jgRJg0a7BmuhGFi-tKn0BTPqVKoIhciX5w-GgVFiQTGkuDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برید امضا کنید لطفا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82052" target="_blank">📅 20:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82051">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GiVZZLBknRpFv9MuvorUgczSL_w3OJVcZaZZPzq8la-SKrw3NHi6yEE_6nsexY7Au7oXZQUXz6_Hed3hH_0ENAOYkR1Xn8rh59L5eu1Z4Yk51S5VMoRDOkofcsUClH2WBis6xmoxu2jkAmInJeUELns3iWAOUOm3WNR7alIQcrxDk76plIcgo2bRBRmXxdo7vXnDUNynY7lYMikG3veGzklbrM2QPyHI9g371EwAzQP9WkTRB5-XkW6_hMTJsHn14PO-NezS-r8asCeDoBm7Nxs59Da4nfPsGEmAVhjayg8QltXtgc_ucxuKX_UjeKNjfx7sTM3AAZsID3hcFZafXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزش سه تیتر زده جهانبخش رفته تیم صدرنشین لیگ هلند، حالا چند هفته از لیگ گذشته؟ یک هفته، و تیمه پارسال ۱۳ ام شده بوده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82051" target="_blank">📅 19:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82050">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6ECgyCoy_eF4j3NxDn9Vd9CReGL7bHgSbkNeRh1XJh5k4VNTfP8Wb2lDglv1U695xRzhwE3MCWO-MJSFlA3-sb9NpqzmFZQtgVIh5rwZfaVNApvosBZjpADB4Ld6RtgJTWanS6zw1VgP7qZhMO9x7U8FP_ZOc-kT73QHU2WuQD9IUgGrQlVO-Ol2vR40A6rN2o8HfmGzv_cjC2TPvJEWrTWXJ3gomrhn0udozGBLq4mhGexnFmbxNQLzZ2wTrgKhEHNeB4dBQ7Z3GEe9nJgHjGApw5x1CG4p1_7TFA7qVafVSF09vK0VdMxtApLL_xM5GCT8yOJCjrPnmWnY6KaHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حرومزاده
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82050" target="_blank">📅 19:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82048">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdnWwMgZg8vmODUE8xri5IuCYtfHBxxBWAagkit8RovnEExuvFFsSJvyjeeMEVZvxX9ZoEGUwdcq_4ZfjNYkVHlppp9GUYsKGwKd1ITPlBZgIHXQ4q-oa4QwUrVIeXvweuB8WVC0aAwniZX0vFFn5Txa3Vd243_YC9F-s3j6B6NW20g7sMhtxCSGx4FM3Er-pFfOTEjAHvLetiglzoJgrOgwHnUn2hL516oJlYCvVYoLZh9_TeKPWpOVvE2JISqVL8mlDRqQk5FCdg-xNHgBZwOLaNVsTvc9NytIn5RG-vCzhsqqb-QD-GtJrdXQpfwfAcxL2-H5-OQ2Nrd61J1C8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید بانو لنا
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82048" target="_blank">📅 19:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82047">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guZIJPuhohpQpSajd8q4npxzEe9nFUl2aVCKfLXomZHFUQhfQAk-CWCeiTW7jHEfQPyS5ARCa0PLIv9cHUkSt3Wl_iVieEemoVHZ913EvoMh7na5knOPsIoQtZYHTfiKPdjWqg2AUZXQtr_mK1mjiyaJ-cu0E76M3dR1XLTHxNQqjf-fOynhoyoqUeXwiKFiOmVuUaYB0j40kiSGjcmKIsRATmZDnN67skOx2I_B0IFcVA42uDed3env2arARROv1G5VpeYiflOqin3NhUUD1GIq3ZGhEtrBtjLgKqy84bGBcno-vXaCiKjdO3d-kbmmQpRobbVjunHynAp4yWNlnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوماد‌های سابق و فعلی علم الهدی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82047" target="_blank">📅 18:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82046">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">زن ابراهیم رئیسی با احمد مروی, تولیت آستان قدس رضوی ازدواج کرد.
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/82046" target="_blank">📅 16:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82045">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ویناک میگه دکی لندن نیست، ترکیه اس
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/82045" target="_blank">📅 16:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82044">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlHBRoIiK7y7KwTwSduQXXQQ-BLRBzl7hc_rUgJDr_gDRbBBHPFklOmNItD4gvOw9ku3B8sz3wSWZzsYeEZmhOT124DBQPs3GFVaOCWP_cf5PycUpGfGOsb69viQTpWp7sHShc4ENNFaIqulvuVGnkyt-fPHzyCCFGgcIlHg9ULWeLZMsDQZgloLMn06Et4vNh6iosSxWpSVnaIQxI2H2amVW7LMMrOiQJa2i1bBX230hK6jJ5yGyBmPCakzDcLznKdbEhhwT9X1EvDWsO-l4t9lohOIHiez8p-sBqdBOUGO8YO-rkuztAi6eXffvk7YPu_QTkH2il5wqSAfvB4_BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سگتم بانو به روایت دریک  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/82044" target="_blank">📅 15:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82043">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48e95fc990.mp4?token=MNoHp2lIH9Luf0RfKL1HX4lrTCF5dzWafMNB0KrWO46lZaACKgMzPbF7XmMwkZrn4iCkkJJzcnFkMcY-V8YYKAZhW8X6t_MJwNe5sGQwbyp2q7-qChfvHQkU3zGoZlTnw9_N-rOz_sLeC3I_gWnctAXfRscfKslDvOzXPAe5IPaoU0bjLFLXlSz7i5DK2xrZcasiyjMhc9NCz0AWy9o6H9srhs-vkFRquyKsqp-9MHUSr9I4w7OmPu4iLT6s0RujK_nkpUKNQ0liOnNdc9EMufOQhVagPXtPPn0PwCXXQMq5dxJIpynzrIyQKoHTcFtoS1Yp3pxVL8VLdrn6fSizkw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48e95fc990.mp4?token=MNoHp2lIH9Luf0RfKL1HX4lrTCF5dzWafMNB0KrWO46lZaACKgMzPbF7XmMwkZrn4iCkkJJzcnFkMcY-V8YYKAZhW8X6t_MJwNe5sGQwbyp2q7-qChfvHQkU3zGoZlTnw9_N-rOz_sLeC3I_gWnctAXfRscfKslDvOzXPAe5IPaoU0bjLFLXlSz7i5DK2xrZcasiyjMhc9NCz0AWy9o6H9srhs-vkFRquyKsqp-9MHUSr9I4w7OmPu4iLT6s0RujK_nkpUKNQ0liOnNdc9EMufOQhVagPXtPPn0PwCXXQMq5dxJIpynzrIyQKoHTcFtoS1Yp3pxVL8VLdrn6fSizkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سگتم بانو به روایت دریک
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/82043" target="_blank">📅 14:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82042">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6LJvCsKpTYLJoIkYheNvHftrVu3XsATb9qEhXgr18CKjD8xHcfzVgR817VrwCsgVKzNLez9LOZFyFZNnOBov2wlfcgRCA-21n1cfD74BTO90HJlYzJv0FJ7csUkvRuvHGXbRL9_nc85HaYgOOpXUTWtUzVrpistamqP0ZeJ-_IHlnNbKp5upUQ2SQOp-L2pxrlyQPtj7LRwL-9nWPzbnJfv3jOkrBS12Hj8xUe0tFrxL4oiB9KD2BKHoEdKeZiHFHfgPPBvsaA5po7ggVmuOomppzrVGt9COmBgLNqhb2PIvf2uu6hiMVwrL7bAAvaYjEJERxa3pAHYP7HQMzf2BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید. ۷  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82042" target="_blank">📅 14:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82041">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">فابریتزیو
رومانو و اهبر رومانو این روزا سرحالن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82041" target="_blank">📅 14:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82040">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mThg6Mp1unJKBvE5O7bkjZnBFwS6WBb15opj2bO4xV0oBsnAbIbqFHuPtJrlZkHJi-LOiT-LoTKeufQFvXuBv8z9BK_eUA0QBBkpNeHctewZww9WlrECMKIbHvGBLRSx50sKgPgkTgh51lgGWL5bhHchkj07z6BXtA1wX21UXJf3c7-yu9tUbbU0fovCR08EU48cUN7r8_8wXyUpGU4-uBoZLk4JzJ5ilOe91QIRhpYtJXZgwGoNeSBAWkCW_u8ww18-DSS5tG-jyLwbVRaby5d4W6G3UyDvoHW9n4fvXlnci7hyDF0FkwVHkgEkUrcyp6MecDucT-yE70j6O5Ml4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عادی ترین رفتار پدر ایرانی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82040" target="_blank">📅 13:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82039">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_brzoddLhiv6shm3eo0QltWlYZ3UD0xwCpXBaBiQG9edkhMJFestfRuAgIfkOYJTwT82oLp2CI5g9m_dS56CggoE1gkLmSXELJwtcr7NAvuhrjKarS_33ImBHMhwbsJEXkafrq5TXCS6N8Z83E3wy62nIWdlgnelPELQlwENHFabynHiShYz2fFoJfRFmmr1TayUh4Phva1XLrWyQK-jUvM5v2lJhl6yAecFDzQUVcCdIGF_8WIlOD2f5qJ3yBDj4UJQ777u5hCi4XzIefflbpGbdKaYt7-IBAkKJNMIbh1J15g2L_lcxP_KoJ_WtaCC12Yk43ZRbsYCixJ7lTKgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده خامنه ای در شعام، محسن رضایی: باید برای رفع تحریم ها بریم یه اکانت فیک از ترامپ بسازیم و توش بنویسیم تحریم های ایران برداشته شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82039" target="_blank">📅 13:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82038">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIC-73naHC34PDaIUNuvpS96IH5-8TOefY2OyKnWDLQRipVP3r9rDR3Ayg_RhAL8KaG-PoJjvZbl_Xz6G-iu5ETtxaEoJITflAtfWyFmRHX_-_oxRwNitNmSXKMQpA_zCNm1ao3DXEZoVP1LtuLRaToWEISF2jmIL8yNZmTlKKd59oeCc224iH95p-P12Nce-6g9h11e-hM4S-SGSudoMaZ9XaPPgW7OsjB2qm90yWy7w0lufSCd7DPqsLcOAO0s1-WBVNgDLYpq81U3TVrJSXqI-2OwwrRYKPs9vOfpsSjyKtrLUAhY8lB9aEUErcFDeSmsap2u2aVkFFcf9PnDbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فداییو دیس کنید تقصیر اون کصکشه همش
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82038" target="_blank">📅 12:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82037">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMrnZU3Io_S5eMdwoYlv8ktso_svD_KbrjUpzmU_81Wt3s5Uo88T0SG7jritn6zMjDviv27TRIIUZZZCE2JlkXgJV7bXI56zoxtRdpDanQjSLhoBbMaqDvUNv-uTGiHnESOfqoKhuDuPTV5FEtRcAq8XjEx87jdfCUJgooXcNA2hslhysf4lWqnXDHeDJ3NZLQa3HemFpKO5IuAUrYp2NhKfh5l1xG0f1BsfDfRqNjL3Tr-IaWRWocVX6Fs_5gumXOSkDhPcHV5Nj8C60bU4KJbhfbpmbetbJvmwJDrGusgJvYaegC03y_j_dRLxb6_vuXPyKddnIvgA-t4knyX3fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ راجع به ارزش پول ایران
کپشن: ۵۱ سال بد رفتاری
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82037" target="_blank">📅 12:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82036">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5yIrXts_Lp0ngczaUqG4vvSAX39NMITsx7vtDw2SGqESpUWyrSrQX4ZQ_dEa9nvzzSAUtJijUXeeHW7RHcYKPpA4iB73jdIA0C1vnPctuJfA2xh3WzJRdXKoO_XAhhhR5fMdNPKOfH3NTA6wsO6RCVFg0YWnPcTtPvWV5WS763LxjLjzIKL4zlizGg9I0X3CKHCExw-IV_9TfsIkj1flxEta8RwsVHkZtcnFuJbwE0R1-k345E7t2X9fdqu6MMttfqr2kSvzGmX-9bw94WGGaekYAmdyYLYVbpIardmWrDByJxKHp8DX2FPnM0bYDOg-Aj1XktiEL-yy7Wk81uS6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید کوروش به همین اسم که تو تصویر میبینید بزودی منتشر میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82036" target="_blank">📅 12:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82034">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMYzyq4x2XbAvq_pBO-cO8VD-PnMFB3ZpGq1oSjHrWbIv5zPW-egZUoHoNltYlD9VNezNT4rYag37VOpyk3pIsDXP8GvEMVYbkvMFIOXL75VfbBJe2n4tND2dDK7V5G9XTYN7vaPLC_sYzzMfPKG4fcRdcQOJt_ZftcPWFNzRw3_yxmlpFQ_j8zuj-6qWjZWs-GabzOl3s6chgngXXvDWirwU2tIO5OKuTrM2O1KyTeZ3aZBSjptc2gtN9_fFBLzf4IpV_0Yh8ZGQyG3pyQclqCvbeSn8vSLGCh_hvaLlb9lMdmIOcGc2X8fiFLMCrs6_TqtEXnKL1YUBDlxHMTacg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپو میخواستن دوباره تو زمین گلفش ترور کنن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82034" target="_blank">📅 11:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82033">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">از لحاظ روحی نیاز دارم قاف بیا بگه "قاف، مهدیار، ملتفت، تهران"
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/82033" target="_blank">📅 03:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82032">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3RaNxScS0hApbRLjb1IEJVO6buOnBP7iNtgwiZL1lWRuRa9cSSEog5O8CJKV2aTB7-CLNkPaAGO3d0HpCEeBKMF_Zgokn9Y9rMbJ-vhdsra2p1xa934HYoa5sOB0bYIJrxgMxjLda4Oy7X-CFtjs-xpnQwNxeoaYPkjUl1B_oHgHU6W1kKKfkFWZJMj5m_7oL3_KGCzRUOygZLD7_VZDuxPF8fhU5JNEFAHLVaN6aMf33K4Ffpbk3t87i9sbP5AFQrraxCOt-q-BLFC6tTqCF30StqHvHaF7CvtsqkmDWoRvgrkuX4pdsa4gviv4YezrX28WLxrWr1CEmtWPRWDkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار برای سروش، خطر در کمین است.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/82032" target="_blank">📅 02:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82031">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyYWJC-cI4ZpVhNuTYm_bhi2_HXYIqOleae_0EzXiFlXgOvPTSlOxAbBp3qgD1MYshO5WvCzOXIcl1pZpghqTRHGhPcQurpySNMFs6LdPvWCNJya8K6tkJ2cwolLluNx0CmSHamgCvt0xsGE1rE-GQ2p6qZZrW28lOLUjo6mBIl0enBGINaL2jxoBbXMV7Q5PYQewjZBwghrEaO6NYpAUjaNhaAZB89JUoAMSLcb6NsBTyQNeJ54rwJ4uG2G1ILdMxSLuAILXBcqAZlnvy_CZfyP2OezjnqM1Uqp6VarxEdvmllORkHZZDPye2XnDOTk8zNNoQ_Dg_l4Sx9tjT0Eqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکی داداش آروم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/82031" target="_blank">📅 01:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82030">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">منابع امنیتی گزارش میدهند که ناموس سجاد شاهی ترور شده است
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/82030" target="_blank">📅 01:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82029">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">4 تا انفجار تو تنگه هرمز
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/82029" target="_blank">📅 00:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82028">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سپاه زد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/82028" target="_blank">📅 00:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82027">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P60fgXcm7xSHmAQRKNPNo5Vg3pKzAZeJCJ0c9lCUXD74tm8PXnbIN7mMjHvrxRyixsxNfkLZUwVtIgagvCCrSh4JfSzmTVK5ndSzqMy3jdIV2iHIxjU_c70ABBiKjLGyW5mI3r_Cds0JMg7D-vsxjGOPIuUt1oBKVj7E-TtoWKOnhq--pHdx0PZ0HssLgBvh92Ib_dEjnNBpLgkPiA0s1iSexdwkYmaBcNOOa6_BjWh-jmfgqsSxhiYT_w13Mmu9h9XXaUVOo9woe8O2him3qKzAzAcJgovRQe6hayH9P1RTMcIbaLQlaUQOxaruLasz25UbBEN2FOVCT9uf9AYaUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقد عجیبه این عکس دکی و صدف
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/funhiphop/82027" target="_blank">📅 00:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82026">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ژنرال محسن رضایی رسما دبیر شورای عالی امنیت ملی شد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/82026" target="_blank">📅 23:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82025">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6de7c57540.mp4?token=b2TwwUwZ4EcXk24bU54-rfsyVZ1i3n9gXk6AFMt4KPxuKQ2Rb53uAP0E3ETv4PEqsHzRZPx3aHls-EnhbRZPnR0IhOW-5ph-lkzFk326y3UVeWxQOLMFH2KWRaLPARM7kDvOam-eJ8nS-ERKuO6tFXIAcNj_YLRnxqqkzQnelwgX1gAHcB0qcZDIwuSVPNwt_a8yFt1k3mW9ZFeEMGEI6yQXMFCWKFdvyDQgPW1N-cAFbIUhF2v_IvdILaDJ3zqw4UjaQlgl6x0VAyJU6uho78OuD-qjBrTxGPn-cVsb-SdJ4NG-RTPPHQQaTarf6u9V_ZRca7YVKxfVLjFJOAjyAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6de7c57540.mp4?token=b2TwwUwZ4EcXk24bU54-rfsyVZ1i3n9gXk6AFMt4KPxuKQ2Rb53uAP0E3ETv4PEqsHzRZPx3aHls-EnhbRZPnR0IhOW-5ph-lkzFk326y3UVeWxQOLMFH2KWRaLPARM7kDvOam-eJ8nS-ERKuO6tFXIAcNj_YLRnxqqkzQnelwgX1gAHcB0qcZDIwuSVPNwt_a8yFt1k3mW9ZFeEMGEI6yQXMFCWKFdvyDQgPW1N-cAFbIUhF2v_IvdILaDJ3zqw4UjaQlgl6x0VAyJU6uho78OuD-qjBrTxGPn-cVsb-SdJ4NG-RTPPHQQaTarf6u9V_ZRca7YVKxfVLjFJOAjyAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظر قدیمی خلسه راجب شاهین نجفی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/82025" target="_blank">📅 23:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82024">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">۰۲۱کید تولدت مبارک ولی قبول داری شبیه شیپ استیلر تو خاندان اژدهایی؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/82024" target="_blank">📅 22:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82023">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/147038d4e3.mp4?token=RMHmN9r_A7-3xR8zBOg8QKTm8b4XxcYnbnt__lspCeUq6XPUnhFO08EYpsM-EGp5ttXfc0EnlUHDXBeMCOBn0yKALJRxoW6By8m5og69tgtVrkd3tk4e6ZG9mm2snpT4BwlL52ZgCEV-xQS9CO9EsJH9mPjtIx1ITnOvXE2VVD7ZI0vicqy5t9mi-TYgdDTnL_qaA3Ap2yNS772cE-Wc50hOFG6imMcf9FXwhVHSgOYbXfMa71efM00d69l_y4W2_LCTkqXw8GM4b7CLg0221IflB8rqr_bUI8OwVKlAIM31O8DoKcio57LiXtsILNy40VpoVShdMhJYfnl36uvsAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/147038d4e3.mp4?token=RMHmN9r_A7-3xR8zBOg8QKTm8b4XxcYnbnt__lspCeUq6XPUnhFO08EYpsM-EGp5ttXfc0EnlUHDXBeMCOBn0yKALJRxoW6By8m5og69tgtVrkd3tk4e6ZG9mm2snpT4BwlL52ZgCEV-xQS9CO9EsJH9mPjtIx1ITnOvXE2VVD7ZI0vicqy5t9mi-TYgdDTnL_qaA3Ap2yNS772cE-Wc50hOFG6imMcf9FXwhVHSgOYbXfMa71efM00d69l_y4W2_LCTkqXw8GM4b7CLg0221IflB8rqr_bUI8OwVKlAIM31O8DoKcio57LiXtsILNy40VpoVShdMhJYfnl36uvsAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعضای زدبازی، حصین، پوری و الباقی خایه‌مالا بعد از لیک شدن چت‌های مهدیار و فدایی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/82023" target="_blank">📅 21:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82022">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CE9X6irpi9vhSNSVUz1_7VyTeH0FVAAOVqu3Vm0n4_jwws15jpVBxC8HlZgrVztG10kIz66WlFLG6UIaSHm8P1J5W22r-UlAe1RqGTQH3JF3lIExg6p67YdpBcNakm4aC2daY7_WdGz16JxYBfhs5sWt8zKpbD0diGdy6wUqBNe-R1EI-ZJzzK3MzqLImfwtj3zqNVEpkAXIoxQKZ3U9SdNv7i_91BkAmwXzU2BYq6LugkSbYmy_I2hb6tAgUISurQs3KHj_xFEGXs0HKpcpLsqcndPjHXZGJn5iBYc6T4xNuQL0dWYDV2SmBL3ma1nqObUdk9xQiTLyAnVBNPBMNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی امتحان سلامت و بهداشت امسال سوال اومده که یه مادر چطوری ایدز (HIV) رو به فرزندش منتقل میکنه؟
یکی از دانش آموزا نوشته: سکس مادر با فرزندش از جلو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/82022" target="_blank">📅 20:25 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82021">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tpy8Vg972Iy9gYa1evyYV_i1sypXxgD_j9lxifC-nz3m0tdgJmjaxST690KCNIne4VadlKsxaDtgr4z58F85YKE8jOW6xal-O3cCONmYjEkmtSdahOvQGHUzmPwc-wZjDPthSYlOghmB6haPOeSnbPUeYEKHVkQC-mK_yOFPmwPpulMFt-hNYdB4zdbyJzzlaqUEDU8ibYMagIHVoBl1kw7SkgQxpKBnI86O3WNvyEQTkV6oK_GZF6-SNz1a3NwTXazCKbwYYoAUwD7Yhtj6Nbg0q4-ap_F3Z9RU94XV5HmbbVlOaCbUOZFfjA-W1gLLxnWFOh806zIxtojHqLlXjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوری
❤️
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82021" target="_blank">📅 20:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82016">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gaoH3RC6AnNTdhrm8pDENErbq5DJFB-FJyTY_JsOM43XzbkRRhgM0AnlhZG-5l3zekPxKI-EHkptTn3-_1dx3J8Ty3Fxbaa2oJ32WxUPkGxHmGL0ocBHJK7jx_JbBinGauE8_JOeNPe-fJ0uIx0M9t8jb5FdixZecspDOrg61Lk58tz8ktq79qVGV_c4dWKd0rIj_SOr2pa8yCF9ElKI_loxzZTLSplvWVbqeD59J8QQrgWb2V2uu3-lkwqsB5sCTTuTBeJ2LIs6OZL_siQULEdLiLCl_K33s933K6XU1o2rnIkFZ_wCScHiYXHEcJa5xaP3ev4gwjq83oQ1jRk1jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mR-c8Sq0ttqQZT3P2bwzAOFFCaveXNPorD25MAXjIaSnfH-Ji2WkLUslfjuKqlSWA2Vlr-8TgcgahWA8kStncTmfsdZtI-6rfzl8hJirPSh0cDRck3EkpXFoAvWaoVOXS3TNjYu4FYOUslt84uzcISSQuygZGQjj0Q5buQ9S6i7aBm8YhYqN3POgKjZdBXN1VUCGDxnPjQhedACBO1Zp3yWN03nCj5Imbni5a9f2zyFkGxkRDNqb_Qal87lEyIYY2FVuYlRTlKU_gkVdg-xbW2TmE91IWfE4V_hI_wTsDRgIv7An1gY6F0SW_8FqxrgJBmQZarTlL3tkKKVLxZhntQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fJWxLf8YEVxkogmn3fBRgA9TAViqoa6bbBmOoBpfki2c2-DVDSYAgAHZWD-NlZRRze4BjToMyJMoJHWQxkycnmkWiV2BbVX5aWfYGgVVXRE0nZoMxzG3Swdi-3hTa1F5YVhJQ7HIEnwo2_xp5zf1r78bPxLxVp8D0zoikkIUq2xElt5bpO3gQty8xYWK7u4ckZxSscOEPN2Dfmy8gNxkAip6K6cTjMD1Fkd6eWmh8PTCbMb15uwzDYg3O9bI6wxm5uA31x7brnFGq1XRLZ_regGTJWB5b-vcu9bq5g_2cPw0W6b-LICbcPMRqszx38qGsxGnpfCvA8fahkOVH2bm8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d21f2b9ac0.mp4?token=k350Kk7LRN6SaVqfHv745Q6wB2g2C3nTd0hqMi2rKhgMubpOmGk-OSO7ky0r2DkE0IQdc4BW9eSbmsS1LdEXilSfz5cEuxy-Iae2ZHRe8MxpUoCJ2jkv3KsMrOFaH_fk8uWMAgOel8BcQnDKGwCd_tQ1Z7WsAxOtagHnYJVa0TpT2A_ImcQKeTxn3gL1CPy1tUbOPqdgZJPGOzaafE5yuDQ1T6qk2VSxBCOHhT-KrsPX4CIkC5r0zINPm3ESBrTrTe72CIa_GtumycVfIov_0vQy_-4Fe8OTat1lj9sDnmZOmrCyCCDxHGk_MBEkO52TOOvyJ9odrf6aiQD6LsPejg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d21f2b9ac0.mp4?token=k350Kk7LRN6SaVqfHv745Q6wB2g2C3nTd0hqMi2rKhgMubpOmGk-OSO7ky0r2DkE0IQdc4BW9eSbmsS1LdEXilSfz5cEuxy-Iae2ZHRe8MxpUoCJ2jkv3KsMrOFaH_fk8uWMAgOel8BcQnDKGwCd_tQ1Z7WsAxOtagHnYJVa0TpT2A_ImcQKeTxn3gL1CPy1tUbOPqdgZJPGOzaafE5yuDQ1T6qk2VSxBCOHhT-KrsPX4CIkC5r0zINPm3ESBrTrTe72CIa_GtumycVfIov_0vQy_-4Fe8OTat1lj9sDnmZOmrCyCCDxHGk_MBEkO52TOOvyJ9odrf6aiQD6LsPejg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پیج اومده یه ادیت فیک زده که رونالدو بخاطر فوت بابای مسی عروسیشو عقب انداخته
حالا کامنتا ملت:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82016" target="_blank">📅 19:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82015">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">وزارت خارجه اسرائیل:
در تابستان ۲۰۲۷ ایرانی ها میتونن از خود ایران برای سفر تابستونی بیان اسرائیل.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/82015" target="_blank">📅 17:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82014">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GSnkV0rlqH49vTTYpdPEKgFgxLHBMsQzudpzX5MA7l70FZLvEcrlrpUB8F8qXo5GhRXI_9JrBM3NelsBNMhkW6raCYj3E8HfZp_oojniDzyyQidp3dyfYC6AS70u9_Pal5vlGoKv_I0XXsf6Lw2UbAX34TcpEG0tDR92InUPsArhYzdbS7Kaaj5SiRC3BO3S7O1vEBcwEl8kXacWbZ5cIrl_oS-Bbk9iJyclhZCVNjC3JnydMJVqN2-Ho1WcBW77_7DH0uCtWbMcoXHrdcuH9I5tDwDKg1kqI4oicWvewdP5hlHGUKqAN9uhQyqDcZ7hcqezOnJYLzD3-Efs8qf1sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید تیجی به نام لبه تیغ منتشر شد.
YouTube
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/82014" target="_blank">📅 16:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82013">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خدایا یعنی قراره کی بهش دیسبک نده</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/82013" target="_blank">📅 15:42 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82012">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba5625cf46.mp4?token=kbyWGeCwV_DxwKHQylorduz5P_gN-EBxwNz1l3uT1SfuFc3KtH5v8z4uLa9Cebj33lR1N3nmNZL9lxgxH7T1mSGjiuPLAbU77TJhxgWLCz5rfdNORVv82-xBSVMO-jTc3ucpnSLZjFoN7KcyUTdUc0IfNoV8kTzKhIvaiWk5XcmKT3NIAtsXKm4bu3m5VS_w9erTbt7sW3Jx3xwT5C5DLfIT_CFbt8idZhyaN2DdlI-m3sgIwggwi75cTKhYVcgpbZQIxrnznfC2dNM7ed1uOvy8eox67g811TKE3-qHcPem2WKjvLlSkgMi8ankdbDWlFf-9krq65RTjf-TK6W31Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba5625cf46.mp4?token=kbyWGeCwV_DxwKHQylorduz5P_gN-EBxwNz1l3uT1SfuFc3KtH5v8z4uLa9Cebj33lR1N3nmNZL9lxgxH7T1mSGjiuPLAbU77TJhxgWLCz5rfdNORVv82-xBSVMO-jTc3ucpnSLZjFoN7KcyUTdUc0IfNoV8kTzKhIvaiWk5XcmKT3NIAtsXKm4bu3m5VS_w9erTbt7sW3Jx3xwT5C5DLfIT_CFbt8idZhyaN2DdlI-m3sgIwggwi75cTKhYVcgpbZQIxrnznfC2dNM7ed1uOvy8eox67g811TKE3-qHcPem2WKjvLlSkgMi8ankdbDWlFf-9krq65RTjf-TK6W31Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رضا پهلوی و پوریا بشیری
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/82012" target="_blank">📅 14:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82011">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1384fab4ec.mp4?token=iLH2NJHPNwb_QSsHpKvx4OweEakTDZbct43NdnibcBizoIYPY4pKqz2PcO1KQ0FU_jFgtNBQVrMZClsAsZ6QAVit63CBS8eRJjJla3H6yXqcX3376aQRU_wb88QIc8hB2ZhaTAq5FwinIXhW8ZzpqhsR0icAuColgJZkR9PQ3uc9L77qBMnSUo9HxjV7AULjjB8awapn_IigcJmJfYlHO870OH0ykQbVI1P-0xuSjReLPB7HMJZxlVwSTX9xhEISwzX2KrLSdA4_4qsf2h59KjkwNmgvsJf5YRhiWvXGDdXS8qozkyCbc6FP87vg7dc86eQ_GL0Brjp4tpu2O7ySiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1384fab4ec.mp4?token=iLH2NJHPNwb_QSsHpKvx4OweEakTDZbct43NdnibcBizoIYPY4pKqz2PcO1KQ0FU_jFgtNBQVrMZClsAsZ6QAVit63CBS8eRJjJla3H6yXqcX3376aQRU_wb88QIc8hB2ZhaTAq5FwinIXhW8ZzpqhsR0icAuColgJZkR9PQ3uc9L77qBMnSUo9HxjV7AULjjB8awapn_IigcJmJfYlHO870OH0ykQbVI1P-0xuSjReLPB7HMJZxlVwSTX9xhEISwzX2KrLSdA4_4qsf2h59KjkwNmgvsJf5YRhiWvXGDdXS8qozkyCbc6FP87vg7dc86eQ_GL0Brjp4tpu2O7ySiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از کشته‌شدن مداحِ سرکوبگر، حمیدرضا رجب‌زاده، این یارو با انتشار ویدیویی مردم رو تهدید کرده که اگه بازهم بیاید تو خیابون چنان تیکه‌تیکه‌تون میکنیم که پزشکی قانونی با کاردک جمعتون کنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/82011" target="_blank">📅 14:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82010">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">جزئیات جدید از پرونده حمیدرضا رجب زاده:
به گفته رسانه ‌های داخلی؛ قلب حمیدرضا رجب زاده رو از بدنش درآوردن و مایع منی خودشون رو روی جسد این مداح ریختن و از تمام این لحظات فیلم گرفتند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/82010" target="_blank">📅 14:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82009">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">محسن رضایی جای جلیلی رو تو شعام گرفت
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/82009" target="_blank">📅 13:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82008">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">جواد لالیگایی(نکونام) به تراکتور هیرویگو
@FunHipHop
| TaymazROMANO</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/82008" target="_blank">📅 13:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82007">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O1jUOok1rSpl1_FgzxOpJHzG_YLVCjMDzDbH435wNzQ3SXMDN3drpx7nPSkAMocllha2a0w56O8LUY5AIp1c8T92Q7nlf8yCBK18S4gdLluF_CnYH7mFqOeqpoaUkk1Wm1I4W-eg_4O6IBeuftetV_fGmrWhwrJEcvvyAaMd9WW3Wl8AGuwlbaHucEP70pFyyom6AxsukKWvl-gKRwkbARSmRwKW5RO-1h0arTc5CEHRDX27QyFjdeH33IKn813fk93gQzL4zKqDdVKxSFyDgQ5vNUyhnFXZWF-quh5cDVhYaFc7wJlnuC9T0MlhKIe_-uYKlwoirrlYeZLOkyAqfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرکس سالام
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/82007" target="_blank">📅 12:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82006">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
وا
عراقچی: در حال حاضر هیچ مذاکره‌ای با آمریکا نداریم، همش تبادل پیامه نه مذاکره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82006" target="_blank">📅 12:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82005">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">هنوز متتظرم تا انقلاب نشده آیسم نخونه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82005" target="_blank">📅 12:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82004">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oolKQK8e4_odvOvnv_dY3XvO-jdHHq29o4twJZ4Dgwllg-ZamSCZ5F2nuigiS7i_VUrDfUL2QkeRvvqEVsFWonjdUbKtptTkNMWNShmiENAomedzxaPVo4HL5dtzUjZa8OA_r_j0rdgQRvxgVy2QSN5tBpksWC17wyCkoWL9RP4hP-Q_-ymsVYV-lYcn6zDjYIFpOhz1pI-XLanYJF2HCKUdm6kXdPBo7xQG8fjOyhsV4eB2GNtve0JmlBTiihPK1mfsAlwfH7giofTBiqf-5esUZLHNhLpa_170rs438_qX_sgGMmwdmjVMIykowcuDhPO1wfSm-coqiT2pPp2GMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس Calvin Klein صاحب برند معروف لباس زیر به همین نام، کنارشم دوست پسرشه
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/82004" target="_blank">📅 11:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82001">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80e3df60c.mp4?token=SlUWX-CWDimacSumhBj2fHRAKDxIBDxPFmtg90oDzM8OHvLK1-NZNKWa87I5vKRqRFYuE4KkSUXtvmkvgLc7btlDcAY1m8RQXKpFl0rDfCm9rX36cO-JpNmi_sLtp-OZrVDuHA-K90wEpJUVFmdtezLINKGJiv6xfT8Jl3YzPJvF6ix0e-eXuFVvbE5NcWsD4-vIDT9w8-Vd6VM9TsSeyE3du8GL_BNephebDOxq2PG_MaFP9tjBMzeTYnpHyzDv3NSf_2NDv_c2k_62lx-izLWwI8zcaOgYHumJUe1r3eSJmY7na0HYxBIF5B2vfNGV_yvL80wwbtKzrADxlffumQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80e3df60c.mp4?token=SlUWX-CWDimacSumhBj2fHRAKDxIBDxPFmtg90oDzM8OHvLK1-NZNKWa87I5vKRqRFYuE4KkSUXtvmkvgLc7btlDcAY1m8RQXKpFl0rDfCm9rX36cO-JpNmi_sLtp-OZrVDuHA-K90wEpJUVFmdtezLINKGJiv6xfT8Jl3YzPJvF6ix0e-eXuFVvbE5NcWsD4-vIDT9w8-Vd6VM9TsSeyE3du8GL_BNephebDOxq2PG_MaFP9tjBMzeTYnpHyzDv3NSf_2NDv_c2k_62lx-izLWwI8zcaOgYHumJUe1r3eSJmY7na0HYxBIF5B2vfNGV_yvL80wwbtKzrADxlffumQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاسر قلی‌نیا پس از کسب مدال طلای اورال کاسپین ‌کاپ ایران، عکس پهلوان مسعود ذات‌پرور را بالا برد. عکس قهرمانان واقعی مردم همیشه بالاست؛ اما امثال هادی چوپان، جوری فراموش میشن که انگار هیچ‌وقت وجود نداشتن.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/82001" target="_blank">📅 10:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82000">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بیدارید؟</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/82000" target="_blank">📅 05:43 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81999">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">بیدارید؟</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/81999" target="_blank">📅 05:42 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81996">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DxgIQ5Tdja-F0U3UJEJCz8dUY7ZfvPYgKJNZy_WXiP63NJo1LV5gjjDMSL9_VTSkM-UMS86W9_KdUJBh1Uz5yHoyFElH2xGuTE0KIYqAvT5Uy1Ad2PoWpDi_75641fcPvTfJ0KosWX-2QodGj6g92dzXWviAd42jXDqtBeUTYnEtsRCKT5D3DLN6VO8CXcEa7uTro3stP_XUkrHKev60uKNfdJfsw16P7wDcCFUTFFvSK2rRRzvC-SLED2s33ilqHqX2UQWz5yEgGF06_G7koff3u3XZSjlC3Z8RYs5pWB1b7ycHTLaJnolQUn9FTaHyN8HztyO65011Jj5HcAMKVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ym8tL4VFi0D6mSBq9OZKCtoy_DT9ctJyanN70t5K3zNXwZ9tfP9rVd_qQh5DBnXwI73Tihk4Y8RgHxIi21vFnElj2EMIrLORfJ2j42ynCqQi1vMJwfOL17cwbn6DueZngFPPAE55h6VGqilLikmXxENOZlkglhpbbEPHEw1jOtcbr0Iy1908leGnNCSfCDyAb-o8iFY61ZnqNSLVSPdN-py00ugpNoHBK-Qmj7UkBnTwPvIIQl-oSn--ZlfPpc8NMRrMLcUa19UCdbdIIKS3daX5bY70lAGTUNYBbTDgQSXmqhVZuoxihxO7B3r7EG6fJrzXjeoB_jcWvt-ge2gHrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بر طبل شادانه بکوبید
جواد محجوب ملی پوش سابق جودو ایران که قهرمانی آسیا رو در کارنامه خودش داره با رکورد بدون باخت 0-5 به سازمان UFC پیوست
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/funhiphop/81996" target="_blank">📅 02:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81994">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dyQCsI_TARFRjKN8POp8jvUGS3xFSgjcH-hqTbm87-L2rMj1A4hSGushXDgbSs3GpkmYNJN8LTbvJwL_6VOqfoTxKYwMHYCphhz4Z8SMDTy0woQY-5JWiZaKWo5EIQaU8L3Pp6JXuOSfJOpU0QwzDyr1fvSGUDskak5yJ1309ONXwuD5FOe8FV4SIL2G8_LlQiGwmYmShWuCc3VT7GENzH9EjyQgOL1wzITlc758qo_SVv5qEL_BgXMhhZwh2A-wPhJEf6G6Cl1SHaU9BZ7JGODiV1DbPEW134HlszKWrqvabBn8hxpkpRAk7xO5yA25ZeQ9uQyIlHO4PBk0aoDktw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید کابوس و دیگرد به اسم انگ منتشر شد.
SoundCloud
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/81994" target="_blank">📅 02:31 · 18 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

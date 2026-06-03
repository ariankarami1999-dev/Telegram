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
<img src="https://cdn4.telesco.pe/file/nKaNqi6iKzOnoDu8z0qGSclrV0Q2_Naw51JvZEHTAtCZNDndLs_yPYvh5v6JA1TRE_3WRjj9DsZk7kTK1oLmjG5c1IzKm4F0ldIFn6hP--yUwG_MtVPysqgdWDODXgk_XEVbjEtoZIoKdotRAymdaEIy7iZHSixW3omNEuIwt-OQ6_10AfNX-rnSs4Ttn4Ki4UsQeRxYTtpvWJH6_NyFP-yshkrK4aKoMnoT5lmcU1dPnXTEzDvX3mOALSye-N3wmwn3aF9WsptL9KyxTnHNebzcwIcRzuJ4nQ4n3KvLL1ina76Cx7ec0RDfASs1i7gfGYA3c16vV_Ae4OYqbcF8qg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 176K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 00:03:17</div>
<hr>

<div class="tg-post" id="msg-76796">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ درمورد خاورمیانه: در آن بخش از جهان، آتش‌بس به معنای توقف درگیری نیست، به این معناست که شما به شکلی معتدل‌تر و کنترل شده‌تر به یکدیگر شلیک کنید.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 652 · <a href="https://t.me/funhiphop/76796" target="_blank">📅 00:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76795">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ درمورد خاورمیانه:
در آن بخش از جهان، آتش‌بس به معنای توقف درگیری نیست، به این معناست که شما به شکلی معتدل‌تر و کنترل شده‌تر به یکدیگر شلیک کنید.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/funhiphop/76795" target="_blank">📅 23:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76794">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rivx9hgQqKhbJUfS23FZNO7gKZ1pZjkolTShR8U1WRZh3Yj91oeJLGBVPeQ_Bi9BYeeFQeynhy_inodiqLs_apAOkImlfTb7CrQsJ-qNMNnMj-Rr4LND5wR_NtCr38OY4HHcx1FCKeUfE_zEsvZvcoZMs64CUTdeY4-4gFwrpswLQ3AxUhpuh6Ii_9XXclb0LWKiLFlPpJKvw-mPv8CTSaRjYwy6daLyDzqhycC71iOO3UjQIXLManVxCIoMHwvrd9NTryBJ0y3f8sYM92VDarjYmmSwx6PjR5c3bS_saRyk9kr0tZ4D2fUeRSw97UZDoXHlsxhhiSb5lebOzF2qBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادر گادپوری نه نه چیز فاز و نولو درست بزنی هیچی نمیشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/funhiphop/76794" target="_blank">📅 23:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76793">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8VVwY53x-6xuTH9neN_GHWd3Wq6o450Fx3l37K2ZiaCo6wlDR_l3cAxxHavka25O9cteyf2q2GtDkf2o0KROUoAAcrEbx8fqmRAZSJMksTwzOntoFAH56P9cB0W38k8t-d54V0YeK9-4ZXu6KmC06VzwlAWXHeHgN5rAAukWTIKVwttZV5iCJYx6cEeGtuYFu52hfqwa0VL2OPFTqEz0NXYQxk7qn1yEATDNv21pKjKyK0Qk1Kshphjyef2HYUpFmIqg5Ts7jQQbEvJfHI-T7-B3D80-WLAphs3cY2hxPnzod0ROlLvKFxOFUcrzZQoZfEYVJVSo5QYDAWg9hxGww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
اینترنت بدون دردسر با RAYA
🚀
📣
توجه 10%تخفیف تا پایان امروز
📣
⚡
سرعت فوق‌العاده
🔒
امنیت و پایداری بالا
🌍
سرورهای پرسرعت و بدون قطعی
📱
مناسب بازی، استریم و استفاده روزمره
لیست قیمتی سرور ویژه
RAYA
👑
بدون محدودیت کاربر
👑
پشتیبانی تا روز آخر اشتراک
👑
دارای لینک ساب برای مدیریت حجم
⚡️
لیست قیمت RAYA
⚡️
🔹
10GB — 150 تومان
🔹
20GB — 300 تومان
🔹
30GB — 450 تومان
🔹
50GB — 750 تومان
🔹
نامحدود ماهانه — توافقی / ویژه
━━━━━━━━━━━━━━━
📢
مزایای عضویت در کانال RAYA:
✅
دریافت کانفیگ‌های بروز
✅
پشتیبانی سریع
✅
اطلاع‌رسانی لحظه‌ای
✅
آموزش و ترفندهای کاربردی
✅
امکان تست رایگان
🎁
همین الان عضو شو و آنلاین بمون!
📲
لینک کانال در بیو / دایرکت / کامنت‌ها
#RAYA
#فیلترشکن
#VPN
#پرسرعت
#اینترنت
#تلگرام
@RayaVPNChannel</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/funhiphop/76793" target="_blank">📅 23:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76792">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=YMZr94s7VZtCNJkmBPtlq01xLxvLss0EmTmQaYUJqYzAz0hbYq2ZsFpEc3WTgGZQNHQZKu3mAoOjLMhrRMYn2A4VLUepuc-aKLbVOlOcVmkQqx-ogeEMIxpqC7s3gRmtKsnuS1ku695ywvykd0s53dLczWCcoc-kv6HydGrB1KTxJMUmGOHANAtmeUQEO6C6I5BDRvCwDWfZVS183P1eQnjttbzSTB5OkhIbJpnIdaiPRMIxeAYtG8ngiehbfkCC4Y-3y2jVG_URXe17fFNop2KjmEI5QJ44L8Ve3R45hhw943pmRgIV8OcS2VSyN53eTqhVSqD2jY9RApsavmoNVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=YMZr94s7VZtCNJkmBPtlq01xLxvLss0EmTmQaYUJqYzAz0hbYq2ZsFpEc3WTgGZQNHQZKu3mAoOjLMhrRMYn2A4VLUepuc-aKLbVOlOcVmkQqx-ogeEMIxpqC7s3gRmtKsnuS1ku695ywvykd0s53dLczWCcoc-kv6HydGrB1KTxJMUmGOHANAtmeUQEO6C6I5BDRvCwDWfZVS183P1eQnjttbzSTB5OkhIbJpnIdaiPRMIxeAYtG8ngiehbfkCC4Y-3y2jVG_URXe17fFNop2KjmEI5QJ44L8Ve3R45hhw943pmRgIV8OcS2VSyN53eTqhVSqD2jY9RApsavmoNVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فارس:
ساعاتی پیش،
نیروی دریایی ارتش، مرکز فرماندهی و کنترل عملیات‌های ارتش آمریکا علیه کشورمان را به صورت مستقیم هدف قرار داد.
ساعاتی قبل و درپی اقدامات تجاوزکارانه، نقض مقررات تنگهٔ هرمز و شرارت علیه شناورهای تجاری ایرانی در دریای عمان از سوی ارتش تروریستی و متجاوز آمریکا، نیروی دریایی ارتش جمهوری اسلامی ایران، به‌محض کشف و شناسایی، «مرکز فرماندهی و کنترل» این شرارت، مستقر در یک فروند ناوشکن آمریکایی که قصد نزدیک‌شدن به آب‌های جمهوری اسلامی ایران در دریای عمان را داشت، هدف قرار داد.
نیروی دریایی ارتش، با تمام توان، دشمن جنایتکار و متجاوز آمریکایی-صهیونیستی را رصد می‌کند و انتقام خون پاک شهدای سرافراز ناوشکن دنا را به شدیدترین وجه خواهد گرفت و با هرگونه شرارت، در کمترین زمان ممکن برخورد خواهد کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/funhiphop/76792" target="_blank">📅 22:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76790">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">خبرگزاری های کویت دیروز یک گزارشی پخش کردن که بازسازی فرودگاه کویت به دلیل حملات ایران در جنگ۴۰ روزه تازه تموم شده ایران دیشب مجددا بهش حمله زده و همچین صحنه هایی رو رقم زده  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/funhiphop/76790" target="_blank">📅 21:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76789">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترک فردا ویناک احتمالا فیت آرتا عه</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/funhiphop/76789" target="_blank">📅 21:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76788">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مقامات اسرائیلی:
«برآورد می‌شود که اسرائیل در روزهای آینده به بیروت حمله کند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/funhiphop/76788" target="_blank">📅 21:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76787">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یکی مامان روبیکا رو پیدا کنه بیاره فردا ببریم تحویل بدیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/funhiphop/76787" target="_blank">📅 21:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76786">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">خبرگزاری فارس اطلاعیه تشییع جنازه سید علی خامنه ای رو تکذیب کرد و گفت فعلا خبری از مراسم نیست
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/funhiphop/76786" target="_blank">📅 20:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76785">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مارکو روبیو: ما دیگه عملیات گسترده و مداوم نظامی تو ایران انجام نمی‌دیم و عملیات خشم حماسی بصورت کامل به پایان رسیده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/76785" target="_blank">📅 20:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76784">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCcAwtlZDXEb25ZYi8kTEn28aL21LFX6oIp-zDJS16EqT84CSFVDdXWkrdC3S6s1Zljar3osDnXbI300ArJgmKAVhYegQTFS5rgCoNfVww4klDLiF6ompHaEabNuTqoHzMBHy1TZ2J9VyFyccC7RtsyHyueNCKdCXdzR6R7JNkZQIo1X1p9cwyc-l4brGoIfQK6Wn42iTbdJr3sRN-cUvJJiP3Z0i8tF_tYQrwe8dllqdQCIsZlIhiVfYjeD5smAvx9AWKIiRGs9bVnJqc722TfXJCsXNHDhovCwr0aIvmIRcwp2RTUx93Fq6dK9J-_OTa5aOsxKD_8wZONo-wq4vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/76784" target="_blank">📅 20:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76783">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترک فردا ویناک احتمالا فیت آرتا عه</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/funhiphop/76783" target="_blank">📅 20:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76782">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">فوری: گزارش هایی منتشر شده که محمدرضا شهبازی، مجری برنامه پاورقی دیشب مورد تجاوزِ ۳ نفر قرار گرفته و برنامه پاورقی فعلا به طور موقت متوقف شده! هنوز جزئیات دقیقی بیرون نیومده و پلیس در حال بررسیه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/funhiphop/76782" target="_blank">📅 20:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76778">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">این‌ دکی و ویناک با آدمای واحد مشکل دارن، بعد جای این که باهم برینن بهشون با‌خودشونم درگیر شدن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/76778" target="_blank">📅 19:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76777">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">این‌ دکی و ویناک با آدمای واحد مشکل دارن، بعد جای این که باهم برینن بهشون با‌خودشونم درگیر شدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/76777" target="_blank">📅 19:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76776">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">تقریبا تمام رپرایی که ضیا برد تو برنامش و گفت
اینه خانواده‌ی رپفارسی
فید شدن
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/76776" target="_blank">📅 19:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76775">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">نهایت ترک‌ها گسترش خواهند یافت</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/76775" target="_blank">📅 19:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76774">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1894538736.mp4?token=FMgmHR67pO4f1JullsI7-uRoKyw3WKkzuklzBp0dPSvDdeZZ-UsAwXrGmX4iEBhJQBVj4DGOV-Fz1_JKmgqsxk3ZOGKgh-Vd62Rso2Z3g_Ir4v07fDeII2Pur7vaTGekZ099-yVtZ8r_aZCN3jmQrKXqEBU2za5onVlBF00TAPLHAH8IAWHJza9Eo1MpmAD9Dt34gZ8G5_G5SLFlkj4YqIM4H5Fs_TiKG_flhUS9ATPByzVActHqhw-SuadUlw9_SrEIPAzw_oOsvcz8RoOEfiyBCuENJRXpKnlshMuycK6NiiY3U1tEcIRcbXQ1jx4dsJvV3ObQsxntcgHbV3X95A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1894538736.mp4?token=FMgmHR67pO4f1JullsI7-uRoKyw3WKkzuklzBp0dPSvDdeZZ-UsAwXrGmX4iEBhJQBVj4DGOV-Fz1_JKmgqsxk3ZOGKgh-Vd62Rso2Z3g_Ir4v07fDeII2Pur7vaTGekZ099-yVtZ8r_aZCN3jmQrKXqEBU2za5onVlBF00TAPLHAH8IAWHJza9Eo1MpmAD9Dt34gZ8G5_G5SLFlkj4YqIM4H5Fs_TiKG_flhUS9ATPByzVActHqhw-SuadUlw9_SrEIPAzw_oOsvcz8RoOEfiyBCuENJRXpKnlshMuycK6NiiY3U1tEcIRcbXQ1jx4dsJvV3ObQsxntcgHbV3X95A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهوی جنایتکار
😡
:
من معتقدم که در نهایت ترک‌ها گسترش خواهند یافت و رژیم سقوط خواهد کرد، و ما تمام تلاش خود را برای کمک به این امر خواهیم کرد.
فکر می‌کنم که باید به مردم ایران کمک کنیم تا این رژیم را سرنگون کنند، و این تصمیم تغییر نکرده است.
مردم ایران خواهان دموکراسی، روابط خوب با آمریکا و روابط خوب با اسرائیل هستند.
این می‌تواند اتفاق بیفتد.
من هر روز با ترامپ درمورد ایران حرف می‌زنم، اما خب منطقی نیست به شما بگویم چه می‌گوییم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/76774" target="_blank">📅 19:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76773">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">مجری:
شما راجع به رژیم چنج صحبت می‌کردید. چرا الان هیچ‌کس درباره آن صحبت نمی‌کند؟
نتانیاهو:
چرا می‌گویید ما درباره آن صحبت نمی‌کنیم؟
مجری:
به نظر می‌رسد ترامپ آماده است با این رژیم فعلی معامله کند.
نتانیاهو:
این به این معنا نیست که او می‌خواهد این رژیم فعلی باقی بماند
اما نمی‌توان دقیق پیش‌بینی کرد که چنین رژیمی چه زمانی سقوط می‌کند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/funhiphop/76773" target="_blank">📅 18:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76770">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e26311d996.mp4?token=CcrBYZJeOwsxzUV2fAJDNcifUN7oI8V0u4qBNYzR3oOdrwcoKogU0friUcsG3ygFCCTv34lDjhk8_DsIgmebO3L6zn6M3GKqibZjVbmd41WbdKKeP6KfCwvf-n-aEwr8jd4xzZO0-PbeFt4CE5wMAGoKBj3o61uyTTE3dw3CzDWaN_B5rr3HIoUjTxwJDvboXBS-0wu-v3STo5PaThFFKoa7s0bYaCEECNqqoKeTRRRfVY1EsB8HlCk3yfA3Y5_3JiCTg0Wm0mZOiCPyY1itDL73MJ3auBdQDtni6_yqPLuSCcgXhKA73fEK2YOue1WjfrIP2nTJzYcW9rxrbgSaoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e26311d996.mp4?token=CcrBYZJeOwsxzUV2fAJDNcifUN7oI8V0u4qBNYzR3oOdrwcoKogU0friUcsG3ygFCCTv34lDjhk8_DsIgmebO3L6zn6M3GKqibZjVbmd41WbdKKeP6KfCwvf-n-aEwr8jd4xzZO0-PbeFt4CE5wMAGoKBj3o61uyTTE3dw3CzDWaN_B5rr3HIoUjTxwJDvboXBS-0wu-v3STo5PaThFFKoa7s0bYaCEECNqqoKeTRRRfVY1EsB8HlCk3yfA3Y5_3JiCTg0Wm0mZOiCPyY1itDL73MJ3auBdQDtni6_yqPLuSCcgXhKA73fEK2YOue1WjfrIP2nTJzYcW9rxrbgSaoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امین منیجر فقط ثابت کرد حرفای فدایی و شاپور واقعیت داشت  @Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/76770" target="_blank">📅 18:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76769">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">امین منیجر فقط ثابت کرد حرفای فدایی و شاپور واقعیت داشت
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/funhiphop/76769" target="_blank">📅 18:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76768">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">یجور‌ میگید انگار 88 ترک داد حصین</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/76768" target="_blank">📅 18:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76767">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">یجور میگید انگار 98 ترک داد حصین</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/76767" target="_blank">📅 18:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76766">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">بعد حالا فرض کنید حصین حتی تو ۱۴۰۱ هم لال بود مادرجنده  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/76766" target="_blank">📅 18:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76765">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">کی میخواید بفهمید "زن زندگی آزادی" شعار مورد علاقه‌ی اصلاح طلبا و امثال عادل فردوسی پوره؟!</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/76765" target="_blank">📅 18:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76764">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">با خایه ترین سعل چگینی بود که تو دوران مهسا سیاسی داد</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/76764" target="_blank">📅 18:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76763">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">با خایه ی اینا دانیاله تو ایران
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/76763" target="_blank">📅 18:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76762">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">تنها چیزی که بینمون بهم میخوره شات الکله</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/76762" target="_blank">📅 17:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76761">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5tyhDwgetnvo8WrRQAjPa2M2E2bDPlBs03lliBtGzqlP1bF17A1swq-EheB9_ZfoOsMwLisK2yRugq8YvGFfhFAZfOt5xUQt9v8afJct0gDjB62p68YW29BJiBkPFVH1Wh5RF6SOb8_n14h620fW9CVAGhmalAN_M3tMef1cdpI-NETTcPBRREFE25b5nRueYNEbBbdCzoPHU6E752xBcv3OcYvBNIF46d2FglskNW7BJwtHMNEqUDyHYe4F4dk08kANmBh_bQ37hsbgZehelU-CLgvPn7yQYzyxQleA27Jno3unQVgB1NxNbgCdsaDQ2zGQ_5EqKma59WYJmb5MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدممممم ویناک عکس پا خوری دکی رو پخش کرد
😂
😂
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76761" target="_blank">📅 17:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76760">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-mcxpJYXpqLV5Tb7JNtuVfEGMErxMxC-WNi0-H-3SbJeFOYDd_0_XUPyRhnsfdk6A8x0ztn3mpZddniGvdjCnQUy79RMNOUtuJQS4TqNYVVLZyjf8gJRBt_WuJT1G6Ecr5ieM9wvovKep67MfXbpcRCgF7POZXiBjmbCxfX0mpk4hsOLBoeS4vMkYaUHgGBt0-0AUOvzEbWJgErjBOGvM_6B1_9wgQ3pTt-v-zXvYvKLUvEx55NbJBge4nF9nYK_bGafEyjrDNWl1A0ZuJl56NZW6bIWla7NVWDPIAjvgnLzykf0O_StnyZNOtAygZKe46NKTMsxtDqMdsyi8WrxQ.jpg" alt="photo" loading="lazy"/></div>
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
g13
🅰
✈️
https://t.me/+RvVnWMHCqUc4YzFk</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/76760" target="_blank">📅 17:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76759">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نخست‌وزیر عراق از تشکیل یک کمیته مشترک برای تدوین سازوکارهای قطع ارتباط با گروه الحشد الشعبی و انحصار سلاح در دست دولت خبر داد.  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/76759" target="_blank">📅 17:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76758">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نخست‌وزیر عراق از تشکیل یک کمیته مشترک برای تدوین سازوکارهای قطع ارتباط با گروه الحشد الشعبی و انحصار سلاح در دست دولت خبر داد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/76758" target="_blank">📅 16:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76757">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d22d94095.mp4?token=a2O0szjw2x0STkSN0QWaZA1ShezVY-Irksue7jQvABiSQR_dxCiAK2Ez2nBXET-AM64GzSs2Hc_zKb7uI3MjQtfI2DlewVkCB2TAiQetlauELlibPzUUFktEvTJTy4akLI97LJRnf5Hos3X6lCxkmT6wCTGF8s9rDI_-ba2cavIV4OKczc2vYFtwhOMc0wiAMuYBLv1XcCx89mMP9Sa0tTT3UbLGCNaJODNRYmApW2P8Trj-t5kypiZcKylolyKWYLjancqirN1FfUIU7L7KrDdrr8qUczJx7WABp1UqpL8zzw5YhC4EBl_YK6jqfLwld6dJj07-It1S608Wg-idDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d22d94095.mp4?token=a2O0szjw2x0STkSN0QWaZA1ShezVY-Irksue7jQvABiSQR_dxCiAK2Ez2nBXET-AM64GzSs2Hc_zKb7uI3MjQtfI2DlewVkCB2TAiQetlauELlibPzUUFktEvTJTy4akLI97LJRnf5Hos3X6lCxkmT6wCTGF8s9rDI_-ba2cavIV4OKczc2vYFtwhOMc0wiAMuYBLv1XcCx89mMP9Sa0tTT3UbLGCNaJODNRYmApW2P8Trj-t5kypiZcKylolyKWYLjancqirN1FfUIU7L7KrDdrr8qUczJx7WABp1UqpL8zzw5YhC4EBl_YK6jqfLwld6dJj07-It1S608Wg-idDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76757" target="_blank">📅 16:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76756">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c69b8022d2.mp4?token=vIA4KgtgQOk8M621IILwuImsyDAdVPFqXa6tOlvApEGe9sMlLojbXSzdy3ahXtI6XB7xfrKOncwo3G0-qX_H65Tr9AUOxtrj4GREfqfq8e25l6-7m3rFX2VBhexpFOBH2vp6pfUGpZbCYzC0vAL9TQHcSEj8gU_vX404OHBDx4VkJPwqam7AXYHApKsegQwehrEUHePzRPvFOgDL9N1r7WJ6_as7_8rnWmCgyxzctE4ei4vX0GeNy2jyVxtEBe5qGPUx4DsaYYQ-CQiNGVFWTN4kEZx_jnvqq499GW4_ZiqPWsC9Lb3KOarCF91xUhynAocUd1fGe7SC4EaaMs5GKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c69b8022d2.mp4?token=vIA4KgtgQOk8M621IILwuImsyDAdVPFqXa6tOlvApEGe9sMlLojbXSzdy3ahXtI6XB7xfrKOncwo3G0-qX_H65Tr9AUOxtrj4GREfqfq8e25l6-7m3rFX2VBhexpFOBH2vp6pfUGpZbCYzC0vAL9TQHcSEj8gU_vX404OHBDx4VkJPwqam7AXYHApKsegQwehrEUHePzRPvFOgDL9N1r7WJ6_as7_8rnWmCgyxzctE4ei4vX0GeNy2jyVxtEBe5qGPUx4DsaYYQ-CQiNGVFWTN4kEZx_jnvqq499GW4_ZiqPWsC9Lb3KOarCF91xUhynAocUd1fGe7SC4EaaMs5GKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداقل یه فیری استایل برید کصکشا، این‌کونی بازیا چیه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76756" target="_blank">📅 16:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76755">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKEf9aKJSrL_pCq1KMsVDUAjPAHczEU0QrrQfBKKUMAhE3JtC8W-6bidAvJnvlo1UBqP1sek7HIJY-WvJSoivXrnEakhizTlzlROgDE3QEpex7DaWx9J8A8zU-fnktbxG_rVROou3LACmF2G-tovhFAJ-RJokq71gDS2yKkoWFRMkjPFbVDPFdtImC_UwE87Z3-WD0TxR1bQXAvxEhlF6pg7_50a0yH3YNoR-5YUgxxiACED2MbPYLtJ4-eBS1d1AWEh4cLjG2MJRPUkFUrA3JBAkNBsik7DFMEYTmnl5WgA_21u4mqa-bG156hUNesAEL33zQnjkz36F2s4zeKriw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا تا ۱۵ میلیون دلار برای لو دادن شبکه‌ی مالی سپاه پاسداران جایزه گذاشت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/76755" target="_blank">📅 15:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76754">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">شورای عالی اسلامی عراق خواستار تشییع جنازه علی خامنه ای تو عراق شد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76754" target="_blank">📅 15:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76753">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">رییس جمهور لبنان حمله به کویت و محکوم کرد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76753" target="_blank">📅 15:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76749">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NHsS018BHXMSw1jdTZsZyLpmbCAc2GoIr9BRrY-1J3PrhteLWw3fMTAEdtcRyiJ8YRqSchZc9IBKwbJ_GvQ8JqsUrkAhxDiFu0JC9OIfeEXZ3EakGudc_tCWyS9ZTOCIPF7RYuYpFwuz3nBHSy5mgoNVS-kcbJ15MS6b8yYN1ncVUIdnGHWWtPETnAs7kwKqW8FIJ3fmHSqiJb8VRyQZpUAqRcFFi4hmQ7xaecHFFOZ0UAlnlhG2AVf3MehXMLHRHQUVX7poL-beCdcQMaAJNFIxvPSBdOlJqdL8AGJ1AQ5EROJK_QxKUpoVp4rJgJOHz0m-wDXRWkYPS7nSGqhWEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eIYOgisCQqnMzezLmG4YbjwhUB7a6oarH84LRiKTjKXSAvVpQMyJ0PF-rfTYMECGkwHP6LKDffasvo4lA7yae4zbJwlmRYbGulHkis7OGPdPz1HNUbP6B3waoUA973_687a86w7PG1ziLpuYK8oHQLzU-iZS8AHSasV7N3Q2N69_e4-2SOV6VHZpVw5cY9HWxvPvzjWniA1gCPUHb6B6qPEJ9y4wI2yg0IFiGY-Q1Lm9dlmTV7tSLbuk8O6yubWhKXRjqRSqQyqMrMcgGbDQeUieIwSkRPGLW3z6K3pZ4nsbQIDgPjH6EjlkTxf3b4d0jJRrtZgYM43sPWji2VCcRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u-DiJX34PCNujmlNohAoDl7diCwXVwTgfrP9SFf8RO_4iN_36-1iPOFE6k13xiqDEjptyTnK_B-hbjiwuDTw8XjOOZsWShB5DJnodJOoZAP27uT5KXgmaVTKoIMixg7zTcFhl7cXE6BPUJlwD0Px3z32jr7vGHMG1CPAoYGCM5d-B_KEqcLOJYVNaXAAtmG_5mP8xxMBI5CVllmPi8AyyGOlDIi_h83FC-hsiovp8yGITvXsojr2-nmHF5VthXUBozT5rMWIY3o8OP1BtEV9lt3wmS-dp3tjWNyQLEjmS2kGbj1nPlhc-I_90Txwek99nkYHU_V9KjbDhPTpL8-1gg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c69019e0b.mp4?token=N4pRAuE0jWV9Sgm9hrZUwv-CHDTV83XKGSAfKVoX_WFcf28fvi6tfJLY8L6u4h8kKfxpve_jPI0noZpuJ76eHVnuSmayOAMIWcjZDx5hV-VnrFW3aD5gNqvGaFwrJAJ_Ytyw3JaTxTzS5JJf8A3fd27KUDvxmP7_BmalOw1Dr6CjGkAJDw41B6PZI-pX1LXbUlcRkIm_F8By7bmEV5M4lYn2SZISUlQ06jzU9CoboKK8bd4k1iIXO3Wl6RPKSEjjPgoDvEyEYuUfo5ybY7XY2scfp29Zw-Hf00H7k1EFt5FHe8xb5VQIn-nnODcuOaw9rkswUd5wIuO1_TZgBIt8Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c69019e0b.mp4?token=N4pRAuE0jWV9Sgm9hrZUwv-CHDTV83XKGSAfKVoX_WFcf28fvi6tfJLY8L6u4h8kKfxpve_jPI0noZpuJ76eHVnuSmayOAMIWcjZDx5hV-VnrFW3aD5gNqvGaFwrJAJ_Ytyw3JaTxTzS5JJf8A3fd27KUDvxmP7_BmalOw1Dr6CjGkAJDw41B6PZI-pX1LXbUlcRkIm_F8By7bmEV5M4lYn2SZISUlQ06jzU9CoboKK8bd4k1iIXO3Wl6RPKSEjjPgoDvEyEYuUfo5ybY7XY2scfp29Zw-Hf00H7k1EFt5FHe8xb5VQIn-nnODcuOaw9rkswUd5wIuO1_TZgBIt8Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری های کویت دیروز یک گزارشی پخش کردن که بازسازی فرودگاه کویت به دلیل حملات ایران در جنگ۴۰ روزه تازه تموم شده
ایران دیشب مجددا بهش حمله زده و همچین صحنه هایی رو رقم زده
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76749" target="_blank">📅 15:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76748">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUVRercLgqh_3oh96m8hrdfzyIHC6KCIBT2_huj_mWf4oe-KdhEm6jSwyf5HJS8u0DqISuXieZrc9jWcGz9IeQOFQD5CuPCTFuJBiQOGlXQQlSDlcQIUwJ8sqUEMnfm4c7gWtRL3WBM2Ou61iiFo7yXtWjwOLp5lffxV2ctQuvAsN1jk3NwKY0ehW4mFEKRHIh8_8iWYXJnsVui8EXDu7BL37_qsZp0DFfZeJAhFrQSiiAfJkmqPyvM9y7j1OicIOankMRyUNvl2LSq4hM0vmLohK9Yh6MtUnqkaQ-KYguXxtRiRCBJA3NYhJOcrsVJn0EKR7LQohG4or79aTTI7Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید حسین تی‌ام به نام "پیستول" منتشر شد.
YouTube
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76748" target="_blank">📅 15:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76747">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2bd935e81.mp4?token=RbKgCsVYGYutCdA0vHZ3LcRCgczzhmG8P6lrTq13lBT52kHTJePm4wnkIcaKIE_rKB0usJYhDo1q66dy-IqjiHKnNO6IvHsOX0H3IdkCduycJtuxthEmvzxu4OoDhHtupmHFZUJOvHcfdTkKF7rBdtmDXlnZbRUriDbTN47WEh7pjatd227zgGgLzJ2OHkM6JXrMMHXLPP4fL4y71GHvAIemTcusLKPhbog7EfAOGl3yggh3isJCRs1XMs4kb8UWudxjf69rRssVKWnXNzcnpgpqXa_14B568U2-P1ERooSC8EbmVswEr3dzE7ALIa_jk6hnWwyrdjVJ4FG4mzG0Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2bd935e81.mp4?token=RbKgCsVYGYutCdA0vHZ3LcRCgczzhmG8P6lrTq13lBT52kHTJePm4wnkIcaKIE_rKB0usJYhDo1q66dy-IqjiHKnNO6IvHsOX0H3IdkCduycJtuxthEmvzxu4OoDhHtupmHFZUJOvHcfdTkKF7rBdtmDXlnZbRUriDbTN47WEh7pjatd227zgGgLzJ2OHkM6JXrMMHXLPP4fL4y71GHvAIemTcusLKPhbog7EfAOGl3yggh3isJCRs1XMs4kb8UWudxjf69rRssVKWnXNzcnpgpqXa_14B568U2-P1ERooSC8EbmVswEr3dzE7ALIa_jk6hnWwyrdjVJ4FG4mzG0Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بمب جدید از ترامپ: ما همین الان با مجتبی خامنه ای بصورت تلفنی حرف زدیم ما کاملا به توافق رسیده ایم ! بزودی حملات ما علیه اسراییل و متحدان اسراییل اغاز خواهد شد .اسراییل 15 سال آینده را نخواهد دید  از توجه شما به این موضوع سپاسگزارم .پرزیدنت دونالد جی ترامپ…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76747" target="_blank">📅 14:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76746">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اوه اوه بندرعباس و قشم صدای آتش بس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76746" target="_blank">📅 14:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76745">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">بنظرم این نه دیگه</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76745" target="_blank">📅 14:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76744">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">هرچند دکی تو ۵ سال کریر بهتری از حصین تو ۲۵ سال ساخته
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76744" target="_blank">📅 14:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76743">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">حصین در جواب به ویدیوی دکی.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76743" target="_blank">📅 14:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76742">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">MIGA: Make Islam Great Again.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76742" target="_blank">📅 14:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76741">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcLrYw-HaN4n8n4qnMCiEKZOPE8qHBUPU31vfJcr_m3JQbLUUX63XjpsYgavtk_8LXAUh09UxCT6k1XQ1VEu799021VNVpHw9SKXiDa0lm58IHvBWyOeKUQ2Mo2H_KjHXOjzCMDlN9SiOtCn2rweAXwUY5OSykRGnNGO5QxgYmnO2udI5HyN5_-YzVlhUz9FC7UpdmqM5OeGWIKYi5jfS4Hh0SKVxvZczgBV9lDiKySAvJJPNsUa-bsqzMyDXhMyRZSw4O0TbFBjUGQ6yZWJ8JbqYM6ttXkkjaOI0L1k2zD_3_uiv9X8wnzH87ry_9eu2IzQ-zsQI5_ZPA8xR1ncuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حصین در جواب به ویدیوی دکی.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76741" target="_blank">📅 14:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76740">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c517113be7.mp4?token=nU4c3lBbGaAXMpEibuK7Dc6ta0oOyRj-8eY1n8Yg3AIXSZZTHxV34hPQoudpeLqO7CyG3tntAM5AOan4CWzDKU2gy9iDe3D0L6G0kNRx1ynnm-Tdrcbt14ByNpUxN2fl-NrYy3zHzfdwfZES3UECcgRwM1QWYFMfMyb6TaUd_eOpMSe0sB5JzodZOeS_M4TWjwNPdP5c-8V0AzKopKjU0dKMwofpXhO1ZwO1623bUpVqwn58f79fha1gQSQ2dXw7INMGCvf3sZj_c_jZMTQLZEOmvj70xCxljGtu7niq2S-373BBHjB197zIQ5vQdMpT7NpMoiLDEwzWvdHB9ukCLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c517113be7.mp4?token=nU4c3lBbGaAXMpEibuK7Dc6ta0oOyRj-8eY1n8Yg3AIXSZZTHxV34hPQoudpeLqO7CyG3tntAM5AOan4CWzDKU2gy9iDe3D0L6G0kNRx1ynnm-Tdrcbt14ByNpUxN2fl-NrYy3zHzfdwfZES3UECcgRwM1QWYFMfMyb6TaUd_eOpMSe0sB5JzodZOeS_M4TWjwNPdP5c-8V0AzKopKjU0dKMwofpXhO1ZwO1623bUpVqwn58f79fha1gQSQ2dXw7INMGCvf3sZj_c_jZMTQLZEOmvj70xCxljGtu7niq2S-373BBHjB197zIQ5vQdMpT7NpMoiLDEwzWvdHB9ukCLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حصین در جواب به ویدیوی دکی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76740" target="_blank">📅 14:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76738">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بمب جدید از ترامپ: ما همین الان با مجتبی خامنه ای بصورت تلفنی حرف زدیم ما کاملا به توافق رسیده ایم ! بزودی حملات ما علیه اسراییل و متحدان اسراییل اغاز خواهد شد .اسراییل 15 سال آینده را نخواهد دید  از توجه شما به این موضوع سپاسگزارم .پرزیدنت دونالد جی ترامپ…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/76738" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76734">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ: احتمالا در مقطعی با آیت الله ایران دیدار خواهم داشت.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76734" target="_blank">📅 13:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76733">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNZokLQ3tIA39shAMAH3DKE8UyLUzVHaKkEamk63z834y895KYlm88m0WTUO1Bbaaupo27aaVEL_NjT0fW9bwt-mQsPsO0mqPMUG5ETyx6IswUVeFgw6fagcwTQFx8NHMJ46uM7FVXTmJbI9rCx6Ci7Pv4O3sIHgy94SB1mpr1Qp-tmXY8ZGie59h5mq97d3dYmjxhAwuQYYBvTbODqj6nX27xRO2eNRPK-xAN2Q62Jz-o9vkbneGGq6hXcN3DdlM_hG8CbJreBbhzX3DKnc3nX_RBwJtnTXYyFCBuAQ4KlJOOXff9K1k5zVk5WdvdvTHE7NPDXWb00Jh7QK0ZspiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خط دفاع رئال مادرید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76733" target="_blank">📅 13:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76732">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">شما نتونستید بچه ها، شما منو حامله نکردید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76732" target="_blank">📅 12:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76730">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">دیشب در قم، دو بسیجی در عملیات خنثی سازی بمب های عمل نکرده کشته شدند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76730" target="_blank">📅 12:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76729">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iq3ruMatxuinbk_7eDwqTkqB6eUfhDXsYi8BNR7gxSqKUM0RnkLWfJqUHceguU7PuJg85Dm3-eeXnxBdkZP-IispPIxTHTzz4btFxx86dFNlLx9BX8h5_x8APHJpThF_9AG_s-y0BrxjyU9Q38LMpIrnbiAkmUPMXLscSGmFUzSF5AhSB2xEuk8Y-ZpO6eewQgvAFYM2Oq0szFmQ1FZ4XQ6rW5HzeQkKQItMVKzHjdDQeMKnIm7lFGBgLPUqbP8SdMWrT3R5lgbIo5fdUW15GkvoeQBwz9WQ9I_MGlXnHr8eDNYTJlsKWVYaWOX2YMzHuWMr8N3oSg6laBa-fcMvqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استایل جدید کراش العالمین
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/76729" target="_blank">📅 11:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76728">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EB5vfR0EmOiphu91Clu200X4-oMCewwm0jdU2EEf85oe90OBgz-Oe0VNrktyiqs8ng7zW88LZUfIYyUrrb4aGQseKiiBAp7QJhx-Gji2uuYCYb6u38TpLcgL1j_N2d45dLG4f1K8KwaNBwdErA1Q39Oh_i_6BZFcAxXzwtTmbITrjHxYfxf_kmza9qqJf1_8sYyaqwZT72F6_utRSmZcDmxaeni3yuBimLCBR5zdal3Kdgj2xlhYhpwbBfmdiPr3UU0v9C9BTSQaRolyHTcRKndqbBQ6vLikC7EiiP_B658mx3p3NlH__FWaGQ_AuIEWts6dRg8YlH_Vxsvtc3NTCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادی کنیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76728" target="_blank">📅 11:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76723">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YwPaOAhkI5PiiP6gjq-4537ygHtwEYuvVrG_JOxWvwuDoLBPeoR_YZ6IHP09yrNUZY9W9RwUOmUOnMiam7vLrQM261tqHvLkgs7mMBsz-eMmSz0dMIModAq_VkofO8_UTsZyPJTh-_GjYcgzIUHHXCAAqs68ADVGnK80gKMIpQ5qt3sBj-8h7YH5e4BBZcEOUgUbxOKhOb9mCwj0ipKp7wvV8MkwiAKzA7OuC-Gb3fF1zyHRDNQvfPpINPI2dv2pI9__hWnRm06BBB49sI2hRVny66omKYTmtGzFX4sOY9KoJcEUY3p0p_-LQrN811Y7nmimPuoi9hzz4MucwDrUrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P2Lp7pIXs3wZviFvTxGDflw1ZAFMwN3GrGsqCLsO3OkGIpwo9VHGpKyUlzeqNe5xBKgKMQx5n5rOyC6U86cVzdqcqctriquJzMHw2jzC4k298d-1iWfmFDAcG5Zo4CUgX-TVNALHR8pOEYsEMBK7QCUNXGnFa2zKIpbQ1nOGAb1Cwhpo2X48-hQiB5pDdR3Af5_s6-tzm9UCt_kWHqJzKQvNaAulIFgQh-twR-QRQW3UnNWqNnJO322gN_wW1o_kTwc-TZY3fIi8aMyM3zHW1PBeNDIVXUPDSaZMxwOBlX_N-Vo9vCBQmvp1Vn9CnfuabxgLIwr_l7ftkJpZMEFD5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">زن مراد ویسی (
لادن سلامی
) دختر عموی فرمانده سابق کل سپاه حسین سلامی هست
حاجی سیاست حاجی
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/76723" target="_blank">📅 10:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76722">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EKhYyZzmY-QEamLM1JewQIeYMhP9AdxCT-v1uRzmwFqsEZ_Fh0pCaftP84sAMlnk2-G6VsmgB5md8wAUFRdCUhKgxTFzqnJ91lO-qRZpycyUeHtMf07HzSxia7xFaPX9T1_FHEL1ppzyGNMp3HMH01myLf5NMu4f-mIpEckIR0cTZSvpfeP0BnNIOveQXJrkWEf5h-uts3NpkLvUfGJNg2zVpgmnMwjjujkSWgK5dYyorELAouW4YLXzbdpjqSqHvRBJPaLZo5VIeuBvShWUl3rArHgANJVB05rGXX_Y44NYC9_hfbsGzl0xvlKUByt-0M4JvUdYmeCDJioyf6SLDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوری: گزارش هایی منتشر شده که محمدرضا شهبازی، مجری برنامه پاورقی دیشب مورد تجاوزِ ۳ نفر قرار گرفته و برنامه پاورقی فعلا به طور موقت متوقف شده!
هنوز جزئیات دقیقی بیرون نیومده و پلیس در حال بررسیه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/76722" target="_blank">📅 10:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76720">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">این آتش بس با بمب اتم هم نقض نمیشه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76720" target="_blank">📅 10:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76719">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxLLyq9D-okFKkgEzLLkvqgNaDUfguEWBxWPwMEn2C4CJ8G6mcLduA8bBwsJxf4FJxrYkTI_eXZQPxT69t8JEe3stO1HvpXIPfmZDnCBr4dtRNd0ka82a47zSr9W2Xulzexd7YZsgsxHN8vPELl17ZBcIqVqTZol-f_gZdfOsNJzUbrGklH7ZE4bsOCB478OueU9DXOyP5SxMRQZ3Y6yvIgtfy2lyn84E9Go07wOb-9C7bOH_K2ZiT2aTBIKYjr9hjZUtE2Av4T87CLwEjPdT4jWtw7PwNXkwzjgE2_NvUq_xJXk5QVtfVd7xfXt5dnE71IOZ8aOlrX0rsI0DX3jhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب تو با آیفونت توییت میزاری نمیگی من اندرویدم؟
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76719" target="_blank">📅 10:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76718">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/76718" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76718" target="_blank">📅 10:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76717">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uK0pN7_GUPIgQgPNo07P0I0iNWDdyssm1ECnta1NH0QI6Rg2lcOzb9I8SeGpAYUH9nCl7Z8_ODjd-5bOM1lvbmcZRKBG-haGzhGoPVKZG3jvDWTa5mlwh_P7S2UJTfxCy8V3No8ZNcwqBfduiB3rxsDXliLFWJrxbdybj452_GU9_UhpsAbLvUSgm2hxHQb67SsgoMMYMFMyCRhfX_jWxeRY1aWE5_QaN_BZhu2rVuwn1Nmg9yF5igU_ndAg0nmnJLs5LNBmmzGALlojaIv64M4ebxhK9L_joOi2huhT3uCjXmTkg6CQB6zPxgDsKdEZ6phfpuBJjosFAzuZVduSZg.jpg" alt="photo" loading="lazy"/></div>
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
r13
🅰
✅
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76717" target="_blank">📅 10:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76715">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">این آتش بس با بمب اتم هم نقض نمیشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76715" target="_blank">📅 10:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76714">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">زدن؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76714" target="_blank">📅 09:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76713">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">صدای یک تک انفجار مذاکرات در تهران
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/76713" target="_blank">📅 07:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76712">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">وقتی میگید، کصمادرت ترامپ "🫪" اینو بزارید کنارش خیلی بهش میاد
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/76712" target="_blank">📅 03:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76711">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بخوابید ترامپ خایه حمله کردن رو نداره</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/76711" target="_blank">📅 03:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76710">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">دوبی رو هم زدن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/76710" target="_blank">📅 02:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76708">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">عربستان رو هم زدن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/76708" target="_blank">📅 02:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76707">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">آژیرها و انفجارات دوباره در بحرین، کویت و اربیل عراق.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/76707" target="_blank">📅 02:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76706">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=emcSmaCsrxuhLqPjqvez1o4rQ_NGlNthuBi_LmdW7M4iLQkAff3m6oCIwRYgNdFJowgj3bx3HXD1jf1VAUebYZsp96mKU3CgyWJbozR0DjHKJeCvBBGqMpLNxdIe7h6cgs0yQbYT_5J03sP2qLd9VRMsgV8f-4BhVla2-fSGTM9vwqEZdd-YJA10oTvsTbFto5hyeoc6BIYaHcW9GZUO5ykAU0ARxFAxDZwCzEWyaIvpUdBB4sjpTmo4KZAzFqNUF-zcpdZpCRr4as9KvAZr1mjQc_KIHIqRIFSJzx92cnxHRz4Ukryw-5MFApYRAKg2ZgM5DAwRF0ofeUVK_h62uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=emcSmaCsrxuhLqPjqvez1o4rQ_NGlNthuBi_LmdW7M4iLQkAff3m6oCIwRYgNdFJowgj3bx3HXD1jf1VAUebYZsp96mKU3CgyWJbozR0DjHKJeCvBBGqMpLNxdIe7h6cgs0yQbYT_5J03sP2qLd9VRMsgV8f-4BhVla2-fSGTM9vwqEZdd-YJA10oTvsTbFto5hyeoc6BIYaHcW9GZUO5ykAU0ARxFAxDZwCzEWyaIvpUdBB4sjpTmo4KZAzFqNUF-zcpdZpCRr4as9KvAZr1mjQc_KIHIqRIFSJzx92cnxHRz4Ukryw-5MFApYRAKg2ZgM5DAwRF0ofeUVK_h62uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیانیه‌ی سپاه پاسداران انقلاب اسلامی درمورد روند مذاکرات امشب:
به قول آیت الله خامنه‌ای، دوران بزن در رو تمام شده است.
بسم الله الرحمن الرحیم
﴿با آن‌ها بجنگید که خداوند به دست‌های شما آن‌ها را عذاب می‌دهد و آن‌ها را خوار می‌کند و شما را بر آن‌ها یاری می‌دهد و دل‌های گروهی از مؤمنان را شفا می‌بخشد﴾
(خداوند بزرگ و بلندمرتبه راست گفته است)
ای فرزندان آزاد امت اسلامی و مردم مقاوم و سربلند ایران:
در پاسخ به گستاخی و تجاوز آشکاری که نیروهای تروریستی آمریکایی با هدف قرار دادن حاکمیت ملی جمهوری اسلامی ایران در جزیره عزیز "قشم" مرتکب شدند، نیروی هوافضای سپاه پاسداران انقلاب اسلامی، به فضل خدا و یاری‌های او و وفاداری به عهد خود در حفاظت از خاک وطن، با حملات دقیق و گسترده موشکی، پایگاه‌های نظامی اشغالگران آمریکایی در کشور کویت را بمباران کرد که منجر به نابودی موفقیت‌آمیز اهداف و شعله‌ور شدن آتش در دژهای متجاوزان شد.
سپاه پاسداران انقلاب اسلامی ضمن اعلام این پاسخ اولیه برای بازگرداندن ضربه به ضربه، هشدار شدیدی با بالاترین سطح قاطعیت به دولت آمریکا و رأس استکبار جهانی و هر کسی که اجازه استفاده از خاک یا آسمان خود را برای آغاز تجاوز علیه ایران می‌دهد، می‌دهد:
هر حماقت جدید، یا تجاوز دیگر، یا حرکتی که حتی یک وجب از مرزها و حاکمیت ما را لمس کند، با پاسخی لرزه‌آور، خردکننده و قاطع مواجه خواهد شد که از قواعد و مرزهای معمول فراتر می‌رود و نیروهای شجاع ما در تبدیل تمام مقرهای متجاوزان و منافع آن‌ها در منطقه به خاکستر تردید نخواهند کرد.
زمان "بزن و فرار کن" به پایان رسیده است و نیروهای ستمگر باید عواقب وخیم نادانی و ماجراجویی‌های بی‌محاسبه خود را بپذیرند.
﴿و پیروزی جز از جانب خداوند عزیز حکیم نیست﴾
﻿
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/76706" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76705">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سلام فعالیت پدافند و صدای مهیب مذاکره در بحرین.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76705" target="_blank">📅 02:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76704">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">کویت صدای آژیر خطر میاد  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76704" target="_blank">📅 01:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76703">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ادمینای اینجارو دیدم با ۱۹ تا بسیجی درگیر شده بودن و موتور بسیج رو بلند کرده بودن پرت میکردن سمتشون،
چقدر زود قضاوتتون کردیم.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76703" target="_blank">📅 01:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76702">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwPB-LlhfZGyfWtSsxafrtPBTi7ltTsyDR0DZCDAaJjVZgbQXse7-0Ci1JvY-WWBzDQFwsxl5nxXN4MSLMt0eESqd-B-kLgeLi2IkyzNUJYbDExv10_bjwd8AYJ6aLdGoHYawrMuSo6nbA1QvRZyBjpcpOZWZDnkCG5v8y5EFs94hR4Y95LVkyJtwK24-ADX--yAf8cJ3aXuC923Ak4dnoGwSnqX2-_xN8RCorHj2XbixevxtE6Q-LvnaCy2lFGWcCiY4gNyPuf5ifGMGbWTSC3pP4NymwBv7Mb9YLIW5LAP9OfqcZCjC5AD5Bjqhr0cO6OURYKT4c8Zjb4dg6elTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضربه ی اخرو محکم تر بزن، اِبی
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76702" target="_blank">📅 01:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76701">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دوتا موشک از استان فارس داراب شلیک شده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76701" target="_blank">📅 01:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76700">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">کویت صدای آژیر خطر میاد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76700" target="_blank">📅 01:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76699">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">این آتش‌بس ما چرا نصف شبا رفع فیلتر میشه؟  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76699" target="_blank">📅 01:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76698">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFSn9WzlqJQJGgiJfZ0vtazBHddqmiLNuQIplSsp6efObbrDVc9OHiweHT21AP1q0UxNptJH9vJbhsHlegmwC6VPHC3q1Zdo0Pes41Nqh_oRrfMwxhUeF5NV5OOYy8cBG6rJ8X_n7EYzKpcha6qeGbGQnN2ZMoxjYZmK8Szah582AgnPgHGA-ubf_XwfpWTIIlQ6HGg1ivjKkcIKsiqEwgG_jZ6c9Ka67RSACnLT6uJEiBT0oSGfOGvPrg1ZpCX6my_fXCfB32WXxu_Mn__T8Z3P7whSUVu-bttFk6VZAR4i0e-EQfVuFrHUw_4b-cQ7YLfekwMdNvDGTq4Q73iSgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آهنگ مورد علاقتونو زیر این پست بفرستید، شب خوش.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/76698" target="_blank">📅 01:06 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76696">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دنزل دومفرایس دفاع راست هلند و سابق اینترمیلان به رئال مادرید پیوست
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76696" target="_blank">📅 00:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76694">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ننه روبیکا رو کی دزدیده بهش برگردونه
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76694" target="_blank">📅 00:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76693">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خیلی ساده‌اس ما الان میدونیم که ویناک و حصین میمالیدن و دیگه نمالیدن
ولی مثلا دکی چی
کلا نمیمالیده
یا هنوزم داره میماله که چیزی راجبش نمیگن</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/76693" target="_blank">📅 00:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76691">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">از نظر ویناک هرکی نگه جاویدشاه پشت مردم نیست و خایه مال سپاهه، عالیه وضعیت</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/76691" target="_blank">📅 23:49 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76690">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">شوک قلبی به حصین:
وزارت خزانه‌داری آمریکا چهار صرافی ایرانیِ نوبيتكس، بيت پین، رمزینکس و والكس رو تحریم کرد.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/76690" target="_blank">📅 23:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76689">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دخالت نکنید دعوا داخل سازمانیه  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76689" target="_blank">📅 23:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76688">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tl6Kjnj3sg6HMZJpvKIf_eY08kaZrI129-tsPaowLnejWHg1KAEAIb46rD7IbMz1H7BZwvLieLJ7HSzj0mlGZ4WTJLQuWwFT9Omj8xtWru0_CWIRdkAce7IQN5waVENZThA8-TaIJVwaSe_cZdMJe5k50JvxHoz3Ufxnk9oR2wAS5S0SDPaPq1neJNfTDpY9tkb0rXED5UtO95so-RgxTZpvvRaDMdAjeIFvRjTxn4m0FkzUtVf6L_XJ817tvZwgflnqCBRGd5cIIsAz5iebXKiA2eIMc43VtxRUWFIbJxxCHgMv8W4tjKW20OIAkE3aZ4Xb92d3NdfGOXia11DsXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دخالت نکنید دعوا داخل سازمانیه
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76688" target="_blank">📅 23:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76685">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmfRnqy6qzFMmyIEShx6b85yQcewdEo63nEtmR9DtIdYZOCKcgmuZIsCGz-xqYxfaiGPp-VSEtZUlgYHVsWJz4INVo6W_ngywyqzL04tQMVgrm9JIsKoRD7s7AmlyKE_T9kpiifSIKgBHURGE19Ty0vdHo7F37W95WAXp2q4x0cTItEjfSYhgua8bB6JrekdDziBJLLB7M2lOMRosttphonrdMmA-QqVupgUKZb2gedJt7N731m0RW7RTCUhSmvVKsZFb-lwGncGgTdp3m6NpNM8XeAfgOeGjX94IaVddvigCo39uzPx7JOJJJETCaQHm87GZ_obPtlI0XDDKQYVNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دعوای سنگین دکی و ویناک
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76685" target="_blank">📅 23:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76684">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDC4YRfG9SEItE2Pf0fnnBdl3yrvVT8FcCEsGkFy_-WIrOciG18bp7ocrjAOQy2evQjqNgOAqRoBWttwW-spJ91ksCv6vMZXfIWfuu_YGrj6J0Etd1nlyiwS6a7LcWBN0gS-DjKoRUIX6artGyMdisE1Osg9-4nOrxeh0wyVxvPDFMcrdnxNlxF_30n6SDe030iynl8spmOMOPFFVqhpXjf9wnDrepJfAPLqEbgyE_Ght2nINYm3LW6btbet6HRLz0Yuih2p-PvtfIFBJ4RFcZajXYtSGqk8u-ujFvhgPOm5XQOHhzpjUyvH900EAxkJwysG5ud9-rlAU1EV5Tr2rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76684" target="_blank">📅 23:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76683">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76683" target="_blank">📅 23:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76681">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArshia</strong></div>
<div class="tg-text">رپفارسی دو بخش است
یه بخش مادرجنده
یه بخش خارکسه
یه فدایی ای هم این وسط هست که خداست</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76681" target="_blank">📅 23:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76680">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPg9BbSoEhrX4ySQE-TJAMFc4IpRyZ_sSpl2oROfCN9Kd2TTjE98SKpukFBaDPu1St89FfgXuem4XAjjs_ybtIbgoVtPz2aoyoNbGwkakX3ZnBJmDPu3RL2g2IY6AMukKFjdJOlv6_6KVhiPVhV8gvS7LDjB09cqN9IdjcCMYpVEZDXdYpXKLMZeAfZe_ch3N5cPD9LJ8eTEZXdu7y8KK58HKCYt8YkRb8ux8tEcblNOxu98D-OtQI2JhC3Tfd4U3hRMYlk271tkNZ6j7kS4YxG4GGKYZMZ0jdPS0QjecsSdgFFkc3fJ9ZjZRtiEkA5RrNcDuPOcdgwjLnfz-lMSTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76680" target="_blank">📅 23:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76679">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ویناک گرفت رو دکی و حصین و سپاه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76679" target="_blank">📅 23:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76678">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArshia</strong></div>
<div class="tg-text">چرا بی احترامی میکنی بی تربیت</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76678" target="_blank">📅 22:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76677">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">من رپفارس رو دنبال نمیکنم اما ایشون دکتر چی هستن؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76677" target="_blank">📅 22:54 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76675">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee30f49b5b.mp4?token=W1rt6sDtHOwnNhCNhrl9H5P0leCBMbczEl8F2VIq_5BXQMRuULNZ8daZI6YlVGGaccedlFXvYnSsZLpUK4bSGWQK29gVOEY7l9UaJ4M9bzeHIIgnlOd97SXIywoKFKWlSR7PWWzM4iCOPJsPmvSmWQTdTvKrZPbgmMQGWzmbf0geYS2hJQxLGaTMCEBwF_KgM5zkXWGiJaMOWbtZziC0Afm-73DguXaPQbE_cJFp5230-SudZM8RZnH3A9FD5mtvqH9rQeTCBXpDts8mD9AHhE6VX6ZlOguvadxwlybth8fxwCWfwr_QnO7601VBoCRb439tgBC-1wqtV9sCvPdjuKG7GaqFbA-Yn2PJZ6LXSAixDS54BNgdIWVI9foNUNlmz9FSnYJQV6Lq2EBFdmTqxxFfstSWM9dvLlaH4fpmt9XO2P_aSWRJTdC-eDebslyzTD5z6R4O7x8lmTqfhB_k8G8DRjBR0OiaJ9KkhoWsWGbcuSzZV9zeaz6xeF4UasAy8wF6Uaw7dB-MsyuUmLIXUIBSkD8jteaYatFXzRjD9xOmrxTLaez0ibW8CwmdqiFF7VMJfIQyOysJd6aceakPwKPnmLiumng65HEhqFzINdbc5dgDgZL9uXJ0oopJ25ODpAt08X0R6uOpUlyA05EpaW2WoJDepRmHn3iPh9p7CQk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee30f49b5b.mp4?token=W1rt6sDtHOwnNhCNhrl9H5P0leCBMbczEl8F2VIq_5BXQMRuULNZ8daZI6YlVGGaccedlFXvYnSsZLpUK4bSGWQK29gVOEY7l9UaJ4M9bzeHIIgnlOd97SXIywoKFKWlSR7PWWzM4iCOPJsPmvSmWQTdTvKrZPbgmMQGWzmbf0geYS2hJQxLGaTMCEBwF_KgM5zkXWGiJaMOWbtZziC0Afm-73DguXaPQbE_cJFp5230-SudZM8RZnH3A9FD5mtvqH9rQeTCBXpDts8mD9AHhE6VX6ZlOguvadxwlybth8fxwCWfwr_QnO7601VBoCRb439tgBC-1wqtV9sCvPdjuKG7GaqFbA-Yn2PJZ6LXSAixDS54BNgdIWVI9foNUNlmz9FSnYJQV6Lq2EBFdmTqxxFfstSWM9dvLlaH4fpmt9XO2P_aSWRJTdC-eDebslyzTD5z6R4O7x8lmTqfhB_k8G8DRjBR0OiaJ9KkhoWsWGbcuSzZV9zeaz6xeF4UasAy8wF6Uaw7dB-MsyuUmLIXUIBSkD8jteaYatFXzRjD9xOmrxTLaez0ibW8CwmdqiFF7VMJfIQyOysJd6aceakPwKPnmLiumng65HEhqFzINdbc5dgDgZL9uXJ0oopJ25ODpAt08X0R6uOpUlyA05EpaW2WoJDepRmHn3iPh9p7CQk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببینید این بنده خدای مو نارنجی چی میگه من بلد نیستم
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/76675" target="_blank">📅 22:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76674">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmNA_XNh0dlvAnLYKdHOZG7Tv3bw7u6p2hIsA4iEY7iEV8qXQJ29wWv_yngKnYnbrEfPYXsYVvz6AKCveUFRbFhjaheC_4TvPAFZle-tKpvbbGTU-bGEaX-RUIahIHWPhW3tzcsKaozwq8l4xvrfY_B2L6S9L0vz63_xx77x2dGcEIKiRD-ZwJsj2QnGbwupy_BmKSV8-3DY9ogpbOEPePFscdSEiPocGDjRNJb7nR5WPzI2S3zl21RhEYIFTrvmnFQHW0wJe4pOPuoshyAS58aGB4diPpPORO9FshmUhKcnJH9fon7BjwvrJs6MPBF4VnfAGwlZ5dCBzpglJ33_1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاقیت در ملت شریف موج میزند
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76674" target="_blank">📅 22:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76673">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">درگیری مرزی هندوستان با میانجی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76673" target="_blank">📅 22:21 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76669">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMD56lNC_dB8TG62VnAZ2wqcOZ1pwx7sLTYPMnmmN_1lVbHYvjEdeou4u_8RjK_gNJQ7EhKe-Z_Lz2yJQvnUE4oTolhkc8_j6uuPgOPbBqidLpJFIkX-o9UyvZcuAL2YR9073NqEBZFBt__m_pgpyfh1coGN59ZjaZ6Q4JhStWet4SZYVArf8TF2hv_sEp8ZW9SrSflB_eMKTWvXlVb2IXn8ImuGnY30mTve7HlhZ1A9fHj_D8M2VcL-JXkb38KLr-rXF0yDAOKzeDZsN7ucYG_YET3urzXM1P4V3yw2Bmh4LJt0mZRw8JwLnwfSmmSU_kzhv1juNbJMiBeFW0Rtxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغ جدید نایک با حضور لبرون جیمز و G.O.A.T
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76669" target="_blank">📅 21:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76668">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbc__iySPMK0Vjyu87chrDai2ozow7p8rvpOtZI3kLH230GkXF_cu5XIpYwc-_ycliBum18RcEXfU_wVX0xFqo7AijOtsQKgnjLUQef3OWX9OL9i_pZNBrZFStPAr3vjNaMkhL6ro1CAGlrFmhBYlNHUH0Pgqvl3lFbwtc1E-hwrm1ueMFzElnbu8Mw91PIe0lztsS8DVAAZKiu0LQKP0gXAlzhnbcGLnFs3MsS3t_eJKOlm9nmfKNlOrj-OgU7vzAFcbsaW4Y32B6hOgISdXfwWJNNRItPIU6s7V2wx3RHLRRk29e30WGQ498wEu3XbAq_CLop-HA74qDuifPMSZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حصین خارکسه اس، ولی به تو هم نمیرسه کصشر بگی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76668" target="_blank">📅 21:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76667">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚀
تعرفه سرویس‌های VPN
🔹
V2Ray
▫️
هر گیگ — ۳۵ تومان
💰
🔹
Hiddify | نامحدود
▫️
سرعت متوسط رو به بالا — ۴۵۰ تومان
🚀
🔹
Open VPN
▫️
• ۵۰ گیگ | تک‌کاربر — ۸۵۰ تومان
👤
• ۵۰ گیگ | دوکاربر — ۹۵۰ تومان
👥
• ۱۰۰ گیگ | تک‌کاربر — ۱,۵۰۰ تومان
💎
• نامحدود | پرسرعت — ۱…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76667" target="_blank">📅 20:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76666">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚀
تعرفه سرویس‌های VPN
🔹
V2Ray
▫️
هر گیگ — ۳۵ تومان
💰
🔹
Hiddify | نامحدود
▫️
سرعت متوسط رو به بالا — ۴۵۰ تومان
🚀
🔹
Open VPN
▫️
• ۵۰ گیگ | تک‌کاربر — ۸۵۰ تومان
👤
• ۵۰ گیگ | دوکاربر — ۹۵۰ تومان
👥
• ۱۰۰ گیگ | تک‌کاربر — ۱,۵۰۰ تومان
💎
• نامحدود | پرسرعت — ۱,۸۰۰ تومان
🚀
@suii_vpn
@suii_vpn</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76666" target="_blank">📅 20:43 · 12 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

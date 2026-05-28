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
<img src="https://cdn4.telesco.pe/file/F_Ak1Kt0H480Bk5-D_EXP27Yq4UyaeOES_B9N4qAvDN_BdhrlO6ChzSypeuf-XuQbfjBsS4-gm925_KvEjrpbqbTIE1UOds7bdx3nhbeEWb58Y1OPm_l6vBr7JP9zZUyFgg07M0LzyeV0CnsP6oq3c4qbsOTNr_eADT8fGmn5NAXRQ761sGRvVn2tt15b-_ObAbTVtZd-lGPlo5DkUkYW4vzkuA3mB0AxIDWpsU-uT0daz7a8lZceQ6IpF3NSYWlGnAnpcMYc-YRCesYXzTvcGjaloSSq_3mO2hS4YEWCyCwBkSc7mamGvumw7sXry0PN-ylxugEwP1ZMZWEYhnKbA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 9.88K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 03:17:43</div>
<hr>

<div class="tg-post" id="msg-16751">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پدافند خودمان هم فعال شد با این زندگی شخمی که برایمان درست کردید قرمساق ها</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SBoxxx/16751" target="_blank">📅 00:08 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16750">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">خبرهایی دال بر فعال شدن پدافند اصفهان!</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/SBoxxx/16750" target="_blank">📅 00:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16749">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXBjcbMNba9s07ziWuLU_ftQpvFi0h_vvZ4yUirCNbrWOuQthapi8McQVM9QeTlgu9nTX9DeFT7BhYR-8UyX4kET0td6Jj4RGpGsiCOq4anY9_ruk_7pCA3lH2amuVXhzkM88_JNdDnBvNccBzMkFnaSW-KvAVnH-mvG389IIouWxDLWchbanker89qZyoX-ZAjzL9UHA0lza5qwcsZlFJeDg-YLQRv0jOIX_PASvQ6QrvLdDQmzpsSyDo1sG5ykYZXuD_MTdCyNawRB17erLFW-vv6IcRmXMguN6oGrtrVBjI5fjHSew2HAaEOs7AcyUdNjHxBLM2sDmVF8Yn9yKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/SBoxxx/16749" target="_blank">📅 23:57 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16748">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تسنیم گزارش داده که مردم بندرعباس نگران نباشند، منشا صداهایی که شنیده شده به درگیری‌های نظامی در دریا مربوط است!</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/SBoxxx/16748" target="_blank">📅 23:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16747">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">تسنیم گزارش داده که مردم بندرعباس نگران نباشند، منشا صداهایی که شنیده شده به درگیری‌های نظامی در دریا مربوط است!</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SBoxxx/16747" target="_blank">📅 23:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16746">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">کی بشود وعده باقر اجرا بشود از شر این وضعیت راحت بشویم</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/SBoxxx/16746" target="_blank">📅 23:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16745">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">باز گویا در هرمز تبادل آتش داریم!</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/SBoxxx/16745" target="_blank">📅 23:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16744">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">باز گویا در هرمز تبادل آتش داریم!</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/SBoxxx/16744" target="_blank">📅 23:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16743">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eb9Hp0c9YtyHbfpL7XVhfzY1D8kTXKlkEIip5_S5Io8SuSOKxl3oczikMWlvpyMwxD2ALcAMTftderTIxk2t6Fv-E824BtO-IowJIBN1eqABdGzxXgW4vUU6HdrpH_AdliT_uYokKC5EjTVwoFe7ScU5-_ZNvOVKP7wl-Zwrsu4TBdeiVp_n7Iysl51DDtZs3HyYF_YsF3XyEyRi-M4ZqfGLaYmgJg1z82Tv03561362UqQpn0jrXRBQg3jFIs8pSF-JQRitge4vaDOBOmFFoFsVx66WI797Ar1XearzuKBar6W8F8UR7kRu-aD2f-Mk4t3MY1nVTSigEuh4D6yOrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#Gold</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SBoxxx/16743" target="_blank">📅 20:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16742">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">این عمانی ها هم بدبخت‌ها یک بار زمان شاه از شر کمونیسم نجاتشان دادیم ولی ۲۰ سال است که سر‌‌ پرونده هسته ای رنده شده اند!  اینقدر که اینها پیام آوردند و بردند، ۱۲۴ هزار پیامبر نکردند</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SBoxxx/16742" target="_blank">📅 18:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16741">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده:   «من این را به‌طور خاص به عمان می‌گویم؛ ایالات متحده با هر کشوری که به ایران در وضع عوارض در تنگه هرمز کمک کند، قاطعانه برخورد خواهد کرد.»</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SBoxxx/16741" target="_blank">📅 18:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16740">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ تهدید به منفجر کردن عمان کرد.</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SBoxxx/16740" target="_blank">📅 18:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16739">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MgLWNCYtMQvhIadXgMx-VYh-uX36X_ga52EDciIQJAehEDikj_q9yOc0uUxi1hrjPDma9NWTCKS671ZHZvaKxGxsxZ9xHkcwR5toOb9hawi4Fz6P5QDDuutns7h7dqFNPO2lg6s7MmMwfYRPK5ynFp9-F5kpvaed3M2sKS_89K6y1uQGv65Exh3eu6VcG4Z4QrEzirrgV8jx1po3xn4FCKQH2pCUjeSIfW9kgP0DSx-A5M3_ebJGJy81PBv_qtwr6qXf8kjZ4L9wudC11q-WxOOCpjL7qC0ZWwkqSxVVsnjVIK3DmqkH23VIgILi3yL6C6kgjk2kxlrlq5G9CWyLqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#VIX
— H4
شاخص ویکس از محدوده ای که جنگ شروع شد پایینتر آمده و کانال را هم شکسته.
سوگمندانه بازارها ما را به یک ورشان هم حساب نمی کنند.</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SBoxxx/16739" target="_blank">📅 18:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16738">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">این بازی ها فعلاً برای خالی نبودن عریضه است و اینکه فشار جمهوریخواهان تندرو از روی ترامپ برداشته بشود و این ور هم جانفدایان مقداری آرام گیرند و گرنه موج 3 جنگ تمام شده و این حمله اسرائیل به حزب الله هم بخشی از بازی است از دید من.</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SBoxxx/16738" target="_blank">📅 17:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16737">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">نتانیاهو:
باید مأموریت در ایران را کامل کنیم و تقریباً روزانه در این خصوص با ترامپ صحبت می‌کنم.</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SBoxxx/16737" target="_blank">📅 17:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16736">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">شرایط توافق شده :  هیچ گروه مسلحی در جنوب رودخانه لیتانی وجود نداشته باشد  کنترل ارتش لبنان بر جنوب  سلاح‌های حزب‌الله محدود شده یا ‌حذف بشود</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SBoxxx/16736" target="_blank">📅 16:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16735">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ریچارد فانتین تحلیلگر ارشد سیاست خارجی آمریکا :   محتمل‌ترین پایان این جنگ داغ، یک توافق محدود است. سپس مذاکراتی طولانی و شاید بی‌حاصل آغاز خواهد شد. جنگ سرد از سر گرفته می‌شود. و آمریکا و ایران در انتظار دور دیگری از درگیری در روزی دیگر خواهند ماند.</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/16735" target="_blank">📅 14:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16734">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">این بازی ها فعلاً برای خالی نبودن عریضه است و اینکه فشار جمهوریخواهان تندرو از روی ترامپ برداشته بشود و این ور هم جانفدایان مقداری آرام گیرند و گرنه موج 3 جنگ تمام شده و این حمله اسرائیل به حزب الله هم بخشی از بازی است از دید من.</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/16734" target="_blank">📅 14:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16733">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ماکرون و احیای آرمان شارل دوگل  در تحولات اخیر، رئیس‌جمهور فرانسه، امانوئل ماکرون، اقداماتی قاطعانه انجام داده که یادآور میراث شارل دوگل است و خود را به عنوان یک رهبر کلیدی در دفاع و خودمختاری اروپا معرفی کرده است. پیشنهاد ماکرون برای گسترش بازدارندگی هسته‌ای…</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SBoxxx/16733" target="_blank">📅 14:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16732">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q74XYoBMD9E26PEJSLJfDp9dyDD7tkzKvvRa2Bhxu_u81MSoKDpDfsidnGkBeT3xvr9FXipcCTEqDcS3kAtSOEjppB0Cvme8L0SV69ukumpwfZqHCFVTz3Xl2S9o3lMyClUYGqRosj1CdTVmE5M6y4by4sdkz_gnbl-tqf1XXYHjlxykqrEJ8oCi1fWITbBMCJIMg7Pt5xP0n-6OzxpryvSK33J8zdD7vAVvJUHwjAFxsfLpISVklOTHPnfelb2oC1RA_3MKJidNRJ8Fee9slDg-RLBDP-bP1C_fkKPeli5EaMRQAb5e97lHSkefujbW2aEGM4FXqjPJeH8rJ5k82A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز جهانی خودارضایی مبارک!</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/16732" target="_blank">📅 13:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16731">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اگر دولت ما آن بالا Short کرده بود تا الان خسارتش جبران شده بود.</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/16731" target="_blank">📅 11:16 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16730">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">#TOTAL — H4  حدود 250 میلیارد دلار از ارزش بازار کریپتو پودر شد.  اکنون به کف کانال رسیده و اگر فروش هست باید تریل کرد یا کلاً تسویه.</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/16730" target="_blank">📅 11:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16729">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohwQdXvEwFX8IjJeRnjW-CR1EZYBflocGjU1ZYOdR_05I0NlBozH6QfFadtN93E1jCi7Zzg0V-UWOUt8E_Kyy0pEgYIlf0Hm3BLf4dx9Ae-QqpOGC_K5mnm4CQefO6wHguOXD3Aa1DAifDCAoKJlLBs-Npw7fWDpURXbrM77pNIhMg5PcR_M7HTWXJws7nFOul8Zq4-uL9T-MYI6MARpalcEv1aOB91RaC1KSMPAd2uBSK-L5rhifU3tsSoX_KOlPhlulWFkb9icA5q8j4WAa-5EjSL0hiTegTAj8gsxDu3taVe1_s-QtoHAhkSZuZ0g5nwZhyk5x-H0_74B3xAOSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#TOTAL — H4  تایم پایین تر</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/16729" target="_blank">📅 11:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16728">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">این بازی ها فعلاً برای خالی نبودن عریضه است و اینکه فشار جمهوریخواهان تندرو از روی ترامپ برداشته بشود و این ور هم جانفدایان مقداری آرام گیرند و گرنه موج 3 جنگ تمام شده و این حمله اسرائیل به حزب الله هم بخشی از بازی است از دید من.</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/16728" target="_blank">📅 09:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16727">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89cfb8e810.mp4?token=Vg4yEJ7__LhnpKr4wgK1x15lTiZWFKJx3pWWP1m0vh6g57k7YSxtuwfG03B0ILaMd-Hkj_mLtNN9vz7ycYUgmpbqlWIC31JGxpFWQRnSyH3Gmdku7IiAZpCzpdLriZ4wseyjNVXicgJnuLWm4zcaD2oWSKTdHIc8M1dMSnYGmZsOsB2STYaEsQjRd8CgXsKTHInHCO30HA0JIxJCaR1kdOYQtkJ3WyO0Blp-W2IPEDwcNHMvt-xcWxI-G5_k-4NXvc6KfkDvJtNoDEG5suHVzWLZHFNlkqWUDqMW4UooYcEHA9Sv5wzXUAGEEOI1ZlWw5-qDTi237FZhyvljWZI7sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89cfb8e810.mp4?token=Vg4yEJ7__LhnpKr4wgK1x15lTiZWFKJx3pWWP1m0vh6g57k7YSxtuwfG03B0ILaMd-Hkj_mLtNN9vz7ycYUgmpbqlWIC31JGxpFWQRnSyH3Gmdku7IiAZpCzpdLriZ4wseyjNVXicgJnuLWm4zcaD2oWSKTdHIc8M1dMSnYGmZsOsB2STYaEsQjRd8CgXsKTHInHCO30HA0JIxJCaR1kdOYQtkJ3WyO0Blp-W2IPEDwcNHMvt-xcWxI-G5_k-4NXvc6KfkDvJtNoDEG5suHVzWLZHFNlkqWUDqMW4UooYcEHA9Sv5wzXUAGEEOI1ZlWw5-qDTi237FZhyvljWZI7sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حزب الله زندگی شیعیان لبنان را با پیوند زدن سرنوشت شان به حیوانات اخوانی حماس به گه کشید</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/16727" target="_blank">📅 09:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16726">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">این بازی ها فعلاً برای خالی نبودن عریضه است و اینکه فشار جمهوریخواهان تندرو از روی ترامپ برداشته بشود و این ور هم جانفدایان مقداری آرام گیرند و گرنه موج 3 جنگ تمام شده و این حمله اسرائیل به حزب الله هم بخشی
از بازی است
از دید من.</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/16726" target="_blank">📅 09:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16725">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">وضعیت گروه هواداران پروفسور رائفی پور</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/16725" target="_blank">📅 08:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16724">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1oFMXNE4QlCZd1rhOOyvLzaAmYlydLx6z9OjjRrfTngvl-WOCFeezH3bVbdSQs_syUdDZKLs8DxIDTbAJ07A6RTP4zzJuhZC1kTJPCo5qnbEee5lMrdDq40wawhuq0GUFr0QPZuWabG3m02rtfw5PXV-FmXrJo8XbPcO1AAqmP82PNmPJ_zg4B54gou4zLCdi4ZYgzPTZVgkTqvXH-phtmRLjHW47Mu7Lse5ymIE_soV1qtKoHm3SYLSivDz4I3D-CQ_R5tgg1PENSdwRL0QidTiZmg3K3yunqkgB9-QLLepQ6tlQSkAavKc4VzXsBqVkEGSEyD4Ym309DeTrubcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت گروه هواداران پروفسور رائفی پور</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/16724" target="_blank">📅 08:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16723">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-pkIuPQKlt0epmJrGdzep02vfGhmGojYJbNO8S5nZY0xuZn08GcMUwKMj9vRLkCEJKZKpKaTwLU5JjF0IocdMBUDhB3GbAj7BBlg2F_sPjlbF6GSrZDPJob9IvB-kV5PhU0yJllt0xKAiuzwLpENW3Utdpj3R7WvxGdvK_kR-ONluMj-48lsEXgRANx4tAj0ogdP7Mv5boU8zHsmTgYfTzpVnuuUQgvlmOBfKQkpDl3auTa3WzuT1T26tGnm9DRI5RUcf_f9ptOipjynCwCN_XpSglDvJnz80IBraBSFDyye6yRztaUiqx_2yXgfHvAzgGrMp3zmri8Ucw_pmE56g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب خیلی هم الکی نبود و سپاه یک پایگاه هوایی آمریکا را در کویت زد.  ولی هنوز موج 4 هستیم
😆</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SBoxxx/16723" target="_blank">📅 08:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16722">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">یک منبع آگاه نظامی به خبرگزاری تسنیم گفت: ساعاتی پیش یک نفتکش آمریکایی با خاموش کردن سیستم راداری خود قصد عبور از تنگه هرمز را داشت که با اقدام سریع و قاطع نیروی دریایی سپاه و شلیک به سمت آن، مجبور به توقف و بازگشت شد.   در مقابل، ارتش تروریستی آمریکا به زمین…</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SBoxxx/16722" target="_blank">📅 08:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16721">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sM5g6GCsPS0D36ajfN0L4J_oxwpXrFUtTv3v4V5z8K8CVqSlKewuJ8ZZRQaLZuq0PWqS9HFnmicsnSf_myYjDaZaLPpRPy_GbhOa9OzmUk5uTvVBn0O_pPX1YWanMZqYK7wYxfbcfwvmjUrpkQGRCARNVCO0UCxl34xSGJhkwpxsUOeWPuyHmTx52BX4TcQ7zDcw3Gl0dQ_ye4ylMYAnrN544vu93ye52PwIqyQ27yte4XCRXormkf3urAklfmSkZlwM0eSCOOuk0CHKRVpGUXWmb3T9hiXKqBBemDJQTLAXDvm0R-esz9wRC57Ib6usct6aO9uDaaEi3Ij8wPXOJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران یک موشک بالستیک از خوزستان به سمت پایگاه هوایی علی السالم در کویت پرتاب کرد که توسط سامانه پاتریوت مستقر در پایگاه رهگیری شد.</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SBoxxx/16721" target="_blank">📅 08:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16720">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ایران یک موشک بالستیک از خوزستان به سمت پایگاه هوایی علی السالم در کویت پرتاب کرد که توسط سامانه پاتریوت مستقر در پایگاه رهگیری شد.</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SBoxxx/16720" target="_blank">📅 08:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16719">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">این قسمت بیانیه عملاً یعنی خیلی دنبال تنش نیستیم ولی خب.</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SBoxxx/16719" target="_blank">📅 08:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16718">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">این پاسخ یک اخطار جدی است تا دشمن بداند، تجاوز بدون پاسخ نخواهد ماند و در صورت تکرار، پاسخ ما قاطع‌تر خواهد بود و مسئولیت و عواقب آن با متجاوز است.</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SBoxxx/16718" target="_blank">📅 07:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16717">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سپاه پاسداران:
به‌دنبال تعرض سحرگاه امروز ارتش متجاوز آمریکا به نقطه‌ای در حاشیۀ فرودگاه بندرعباس با پرتابه‌های هوایی، پایگاه هوایی آمریکایی به عنوان مبدأ تجاوز، در ساعت ۴:۵۰ دقیقه هدف قرار گرفت.
این پاسخ یک اخطار جدی است تا دشمن بداند، تجاوز بدون پاسخ نخواهد ماند و در صورت تکرار، پاسخ ما قاطع‌تر خواهد بود و مسئولیت و عواقب آن با متجاوز است.
و ماالنصر الا من عندالله العزیز الحکیم.
روابط‌عمومی سپاه پاسداران انقلاب اسلامی</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/16717" target="_blank">📅 07:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16716">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">الکی است و امروز یک توافق امضا می‌شود که البته در چهارچوب همان موج ۴ ارزیابی کنیدش</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/16716" target="_blank">📅 07:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16715">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سبحان الله!
یک نفر که مشخص است از 28 فوریه تا امروز به نت جهانی دسترسی نداشته و صرفاً در بله و ایتا غسل می کرده در دایرکت پرسیده که استاد با این 300 میلیارد دلاری که از آمریکا میگیریم احتمال نمی دهید دلار تا 100 هزار تومن پایین بیاید؟!</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/16715" target="_blank">📅 01:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16714">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ تهدید به منفجر کردن عمان کرد.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/16714" target="_blank">📅 00:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16713">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">شروط کلی ایران به صورت رسمی در صداوسیما اعلام شد:  • آتش‌بس دائمی در همه جبهه‌ها • خروج آمریکا از منطقه • عدم دخالت در امور ایران • رفع کامل تحریم‌های اولیه و ثانویه  • آزادسازی وجوه مسدود شده • +۳۰۰ میلیارد دلار غرامت بازسازی • کنترل و مدیریت ترافیک دریایی…</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/16713" target="_blank">📅 23:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16712">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">شروط کلی ایران به صورت رسمی در صداوسیما اعلام شد:  • آتش‌بس دائمی در همه جبهه‌ها • خروج آمریکا از منطقه • عدم دخالت در امور ایران • رفع کامل تحریم‌های اولیه و ثانویه  • آزادسازی وجوه مسدود شده • +۳۰۰ میلیارد دلار غرامت بازسازی • کنترل و مدیریت ترافیک دریایی…</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/16712" target="_blank">📅 23:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16711">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">شروط کلی ایران به صورت رسمی در صداوسیما اعلام شد:  • آتش‌بس دائمی در همه جبهه‌ها • خروج آمریکا از منطقه • عدم دخالت در امور ایران • رفع کامل تحریم‌های اولیه و ثانویه  • آزادسازی وجوه مسدود شده • +۳۰۰ میلیارد دلار غرامت بازسازی • کنترل و مدیریت ترافیک دریایی…</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/16711" target="_blank">📅 23:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16710">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">شروط کلی ایران به صورت رسمی در صداوسیما اعلام شد:
• آتش‌بس دائمی در همه جبهه‌ها
• خروج آمریکا از منطقه
• عدم دخالت در امور ایران
• رفع کامل تحریم‌های اولیه و ثانویه
• آزادسازی وجوه مسدود شده
• +۳۰۰ میلیارد دلار غرامت بازسازی
• کنترل و مدیریت ترافیک دریایی در تنگه هرمز</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/16710" target="_blank">📅 23:07 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16709">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترور جدید اسرائیل در غزه</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/16709" target="_blank">📅 23:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16708">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_JjbbAQS6uqV_dPyPAPEV0xv7kEphk7Rrpjglkp_Gu5QiJQFBCnn2FoHsLHXrvsOX_dSUkb-L3k9M9p9IJq5GF1VNWQqTv_UoVSjo_4fDQasfdQ409VcpVb14hIFIhF0wPv07f8Qq8unuOvQbh91WJX9czUQTRrKskS-OqhmQs7Dkkb3m0SeTcBWwRwG12bWeBtMNL4-YdQ1HvjtHUMOGdQ6mAXIlA-_BRZdbnyQGT0c061J3YmaGsg5VlRAHKjFXkiAiATYR0jU8e8LOZeF7Vf94Yp-ZvGmM7mWuTaUFaGJ0WDAkG-3HO3bmjPbYKaRidepxMHQfBpIyhWXl_VHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#WHEAT — D  به نظر می رسد گندم هم دارد همان مسیری را می رود که نقره 3 سال پیش در آغاز آن بود...</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/16708" target="_blank">📅 22:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16707">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8e42f7252.mp4?token=WIjH8nPflUcrTT2xc8kkXiGRBCP42UqNo--bs6o4tei2KJUp4xHyzaJ_KkDD30pNL13RAHZK4tI_LdBShgyBG0b5DUTN4C_JfQq_qYGmR-Huw1tqQphGXcVK0AB35ciR3JAs2SPFxTs6fmfXGIj919jZ3KGSU152OUenNoHz88sStXa2d1RRQGWP2yeO4trXi32bjh2oiH1g5Fp1tcYwyXIFTotCBbm7YCtXoemEqPcInB2ik35qCUbFU4Uu4iKf6jeVM2C3IYyjiR7nJ8GLpsShxqxIlcepQtVplzPKe2OjKAwVUZVZlehtKrpBG578MSUvnqloosHmp28g1IlqEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8e42f7252.mp4?token=WIjH8nPflUcrTT2xc8kkXiGRBCP42UqNo--bs6o4tei2KJUp4xHyzaJ_KkDD30pNL13RAHZK4tI_LdBShgyBG0b5DUTN4C_JfQq_qYGmR-Huw1tqQphGXcVK0AB35ciR3JAs2SPFxTs6fmfXGIj919jZ3KGSU152OUenNoHz88sStXa2d1RRQGWP2yeO4trXi32bjh2oiH1g5Fp1tcYwyXIFTotCBbm7YCtXoemEqPcInB2ik35qCUbFU4Uu4iKf6jeVM2C3IYyjiR7nJ8GLpsShxqxIlcepQtVplzPKe2OjKAwVUZVZlehtKrpBG578MSUvnqloosHmp28g1IlqEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ تهدید به منفجر کردن عمان کرد.</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/16707" target="_blank">📅 22:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16706">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">این‌گونه_دکترین_نتانیاهو_برای_ایران_فروپاشید.pdf</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/16706" target="_blank">📅 21:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16705">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ : سومالیایی‌ها، همه‌شون کلاهبردارن، خیلی هم خرابن، ماگرفتیمشون و داریم روشون فشار می‌ذاریم
☑️
@persiannbloomberg بلومبرگ فارسی
✔️</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/16705" target="_blank">📅 19:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16704">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبلومبرگ فارسی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c71816eb9.mp4?token=I7wMRIG4WyKGh8DqE29vsfw1ir5cV1Ou7Sr6riFBQ4DXx3SsJI2aaDRojomQB_juxVgdz1meSBet8qBaIK_oibehgQPWUDlPqlSzyT9MM6S1rTvFk9o5nT7D-Smu-7LpWuzE1evJQe5qRPU0HkPwHP_I3w7m8cLskp08ne8arIERRnuKmjEOHtWQeDfGOJFpPg1vuKIY0KUkmkLu3q63zKhLiSzUmDj0XzWJ6iwG4dpnM8DXl0JZkgGg2IEBd8ijr5o7aWgw_mOgZLGBwB-NHDGWAC8AoUzzsy16PgQVA28ChZbW_1ntv4aUsKJl6qFVD1fYfNMrWFTxN-_HExvJIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c71816eb9.mp4?token=I7wMRIG4WyKGh8DqE29vsfw1ir5cV1Ou7Sr6riFBQ4DXx3SsJI2aaDRojomQB_juxVgdz1meSBet8qBaIK_oibehgQPWUDlPqlSzyT9MM6S1rTvFk9o5nT7D-Smu-7LpWuzE1evJQe5qRPU0HkPwHP_I3w7m8cLskp08ne8arIERRnuKmjEOHtWQeDfGOJFpPg1vuKIY0KUkmkLu3q63zKhLiSzUmDj0XzWJ6iwG4dpnM8DXl0JZkgGg2IEBd8ijr5o7aWgw_mOgZLGBwB-NHDGWAC8AoUzzsy16PgQVA28ChZbW_1ntv4aUsKJl6qFVD1fYfNMrWFTxN-_HExvJIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : سومالیایی‌ها، همه‌شون کلاهبردارن، خیلی هم خرابن، ماگرفتیمشون و داریم روشون فشار می‌ذاریم
☑️
@persiannbloomberg
بلومبرگ فارسی
✔️</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/16704" target="_blank">📅 19:52 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16703">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ:
ما از نتیجه مذاکرات با ایران راضی نیستیم،
مذاکرات رضایت بخش نیست.</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/16703" target="_blank">📅 19:44 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16702">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AYAsi40xZzy3lVJUVpe9hRk3Mz1v1TekwT14uguUl92KBPxNLoHvERlGaYiamn26Nw9gMPeEguoMsCllHnv_q1qedgAZnsckw9x6a4fgKPyupSUj9Z3sE5hL0qeMg7DBUiPX3XIM_f3_I7YxwupbOIMg5mBr0rzcgLCN7NpMD42ImpE22Evijt6BD8ZG5dM69zmFajBoU61PIxNWpiCkro2iB1OG5bRDzgSd6MQNtG5BmFpb1JQTfYbcWB-5BItzXH5fvowbm_CmZ4fOGQH_NTSK_zK-69LxG5b_oTAFjV0osKGdniVvCba0eJ1H65B5-YMkBEgSii-_WhVids-usQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#Gold</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/16702" target="_blank">📅 19:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16701">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtWaw4CS5eEJ7bHx8Z35oRyMzPQuR-kGjzXXPaWwkDoNWbi54FIkOT_EHBLoSBQDX55C65FJMppbv3hw6zQtWgDAravR0CsHf7pnCntDL3PCavNKHPWIZbY6EjlhZJBH6kVL0IWDoPLrI07slQ3dQHFOAPejYylzLmF-Wmxm3k0HJZ90dkI7-pWVsHgIYChWdA7NIu_fu2bD6cPcJm48stVvkojFzkjblm1UN2-cPByfwYQralvguBOqP_9IA0zAal0mRRObCR_iQn6bXLjJ245gB8uA2W8IgyVFVIdOOV5A7Bgc1Dvbkdsrku8LsGlZVPiR8D1WMmvpwajN0kq8Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#US10Y — H4  فعلاً موفق شده با این سیرک امروزش مقداری نرخ بازده و نفت را همزمان سرکوب کند.   خواهیم دید چه خواهدشد.</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/16701" target="_blank">📅 19:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16700">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">کاخ سفید: مذاکرات به خوبی پیش می رود</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SBoxxx/16700" target="_blank">📅 19:07 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16699">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ارتش اسراییل دستور تخلیه سراسر جنوب لبنان را صادر کرد!</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/16699" target="_blank">📅 17:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16698">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">«مسیر ترامپ»: وعده ساخت از سال ۲۰۲۶  وزارت امور خارجه ارمنستان سرانجام زمان‌بندی مشخصی برای پروژه TRIPP اعلام کرد که به «مسیر ترامپ» معروف شده است.  طبق اعلام وزارتخانه در پاسخ به درخواست کتبی SputnikARM، فاز عملیاتی پروژه از سال ۲۰۲۶ آغاز می‌شود.   راستی،…</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/16698" target="_blank">📅 17:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16697">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0X9YPYaNyzG79ndpfQTqVRD2jUC-YkKGM3S_7YL_1ZEY1xXJskAeyMa4NDBhCfNqOBIvfv3Qp5rSOkGBRpt0KzhnOSblz8BeVq8r7l-ISD6zp9Vr6xiycRC5Asty1cA7DGmdTgyVG2qlbbqCVtsOIJXn6v3sN7dZFly5wGyoD7g4AEhBSgoogzMGOhuxvXeDgdjAbeYRntMSbGDrlej1IwMHAqMlraYF9KZPfUYiyqMg3G-e0iBxx8oPIKjkN0_pQjNPLoeOah4Z6fQYgeIJR4pNfxE3LJ5gdtxHcQnBPPc1yne12kfCXLWsTMjdmsytLDmV1AyIXzOZFNQdPpMtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسراییل دستور تخلیه سراسر جنوب لبنان را صادر کرد!</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/16697" target="_blank">📅 17:01 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16696">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ایالات متحده طبق یک نسخه غیررسمی از تفاهم‌نامه، متعهد شده است نیروهای نظامی خود را از مناطق اطراف ایران خارج کند.</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SBoxxx/16696" target="_blank">📅 16:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16695">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گزارش‌ها حاکی از آن است که آمریکا و اسرائیل در تلاش برای پایان دادن به قیمومیت اردن بر مسجدالاقصی در بیت‌المقدس و جایگزینی آن با یک نهاد چنددینی تحت کنترل اسرائیل هستند.   این طرح پیشنهادی امکان دسترسی گسترده‌تر یهودیان برای نماز و اعطای نفوذ به اسرائیل بر…</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/16695" target="_blank">📅 14:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16694">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">این‌گونه_دکترین_نتانیاهو_برای_ایران_فروپاشید.pdf</div>
  <div class="tg-doc-extra">162.7 KB</div>
</div>
<a href="https://t.me/SBoxxx/16694" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترجمه
مقاله Israel Hayom
درباره علل ناکامی عملیات نظامی آمریکا و اسرائیل ضد ایران</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/16694" target="_blank">📅 13:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16693">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gca0mj5JHqm1_hNiXxYUagLI_QBcYl6Nm0KerDL3qfcQyZynRYjWz7QCcHPH9naEcsQyoqblT_9lmU7SMsgQB1Ql6GJoPs134kbFlK5h-MmQdX6dR711wkFlO9vczLVUhTbKJEK3ipl9Gwb-dRHpUNQKfvszUtkzBrT8DOH9KsFheh0msKGftnF3AGHp7zg3csqSRzk_30yZ4peyICH-HfBdxyisf0PJ76iTcRsI8RPSpXnjCDQNVqeYLD_FATRgJBQbsqlk3TTEdVc44PYJGGwsuEZPSycjcVtA51PzRP8gfpZtHlHrVSovecYoXH02rhwbb9Zs3Al7P0_fj2HWJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
گوشه ای از قدردانی کاربران روبیکا نسبت به مسعودپزشکیان پس از بازگشایی اینترنت بین الملل:</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/16693" target="_blank">📅 12:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16692">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">کره جنوبی قوانین ترانزیت نفت خام ایالات متحده را تسهیل می‌کند  آژانس گمرکی کره جنوبی دوشنبه اعلام کرد که رویه های قانونی واردات نفت خام ایالات متحده که از طریق کشورهای ثالث به کره جنوبی ارسال می‌شود را تسهیل می‌کند تا همچنان واجد شرایط بهره‌مندی از مزایای…</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/16692" target="_blank">📅 12:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16691">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">این بستن تنگه هرمز نهایتا باعث:  — ایجاد مسیرهای جایگزین  — تقویت تقاضا برای نفت آمریکا، کانادا و روسیه — تسریع در انقلاب انرژی سبز  خواهدشد</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/16691" target="_blank">📅 12:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16690">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3stuEO1VVGD0m-ZMST6EkLfiUv_dpRL3PXw5zfYA7mPaptEUY8I0WJx7GUpaQPjIX9Ad0k7mctGRgI86VJ4PvW_jlzBE-3NQqoDpIJmOqePSVPptz6OiwatLjvO3dhUHqnP94tX4-9K0_zJOiPqq7jODhaaYw0UVO2b3aTnp0bU1RJcg06TWZUMO0SWZ-gfRabCBlue7rn6EZ9egaRifx80AIzvZlIxGvwLy8Tljn59lkDIkrY4ys86uFRuHwfVcfCKims7pNqncDP1sAPko89_SHkh0dnJBqoOHpjvQWWow2XjBrUx1FvGPRrRxwRSS7KJuGDnxbEFxgwJqQ8Cqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش‌ها حاکی از آن است که آمریکا و اسرائیل در تلاش برای پایان دادن به قیمومیت اردن بر مسجدالاقصی در بیت‌المقدس و جایگزینی آن با یک نهاد چنددینی تحت کنترل اسرائیل هستند.
این طرح پیشنهادی امکان دسترسی گسترده‌تر یهودیان برای نماز و اعطای نفوذ به اسرائیل بر رهبری مسجد و خطبه‌های نماز جمعه را فراهم می‌کند</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/16690" target="_blank">📅 09:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16689">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfYAyZIAKLD2dUFnmoFUHOKt2hPAAjaItWHAjP0jvBLjSrA4zO3_BXTR4tShUCD52T12Mwk3Sp9q1MNSTRfnPQ1d0jLDxNFVEyT_OLGUvIelBiNqJboxLh7uyFD2nFG4nKPl9winCRvBGoMntEWthsoN7amioNZ8omUSnfY0mVnOQaKg3BrzHygqDPiTNjzv7IukgOJ7rBIBUayF-7JAL1adKNJ5g8x_UN8SLpZszCDnesTqpS7ffPJP9J3cFBcLJRuvsUDax8SXMnxIozOsuYVGSRLYP6p7EbAK-CvycT1WCuhvymaEiw2Vc2yyrGuk3EDgMm8ySs9aQfKI4oDTRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه در حال بررسی محدودیت صادرات گازوئیل و سوخت جت است، زیرا نرخ پالایش به پایین‌ترین سطح چند ساله در پی حملات فزاینده اوکراین رسیده است.
به شرکت‌های نفتی توصیه شده فروش فرآورده‌های نفتی به بازارهای خارجی را محدود کنند. تصمیم برای ممنوعیت صادرات گازوئیل و سوخت جت در مراحل پیشرفته است اما تاریخ آن هنوز تعیین نشده است</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/16689" target="_blank">📅 08:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16688">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZlKY0LyYAMZHm1B52pqeN1bubMotgqr0VK5cmMduCSUJ1hnUuy0qj_3gdrktpLU0JC0mvwoP55YCpyf0SK5sJ4L_g2d8hdjhz6uG2e8VkGAcZYvdEcikxxnMdZJO2Mpd7KxyQA_HNCZHYwdb1B6AQTmntzXdVEyowkQ73Q1m5TAWDohG2mO8trQzgPIzYNThq3X957LWU0QgtI3Df5fvDjvvCMJ212rFUyfetZw9RdU0xcGBQD3dA7QI4duq70KT5OO1qduzs6Za463lkdxz41NavKlVulfHhtdn6yOQghj9eiQ22jML9gKFLFLtvgimLgL6l2DP6HWKWriEIndFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از درگیری‌های چند شب گذشته در تنگه هرمز و اطراف آن، احتمال ازسرگیری سریع ترافیک عادی در این آبراه حیاتی در بازار شرط‌بندی پلی‌مارکت کاهش یافته است.
اکنون معامله‌گران احتمال بازگشت ترافیک به حالت عادی تا پایان ژوئن را تنها ۴۲ درصد پیش‌بینی می‌کنند</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/16688" target="_blank">📅 06:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16687">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHHYD1zrowm8tWapDVut25aASTm-hSYkcaGW5BzvIy2QSRTKPjuhDJStZB7NAoXdBBuJ4DCAHIqRJXUUL1pP7cB0izTnN2pQEMeDlY4unBZPV4Zonz5h9meO1YrRDkqXKjZ7dK9aoFLKHa2QXYwqUODzIOjLQN5GehGmM1uzbD422MqcD7kyqho4SWcUsIZKGVGpwdGjVXhgpD9nLhGrdaJWF5zAYfDX3HKEcK0DUkaN7XMuKFMFCFJO1ntT_6mv27pQTp_A_98wM5GgwxnK949yvkI-5W6srf20NAvt-0SIz3KEGYiS27yRbRxfxw-RV9QtcOy9GSUrBXAS22Fdsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو:  عزالدین الحدّاد، رهبر حماس در غزه را ترور کردیم.</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/16687" target="_blank">📅 23:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16686">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مملکت خر تو خر</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/16686" target="_blank">📅 22:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16685">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zl5bweWQyBrfEMLuRmGHChqz3qv9qEEagtQwWtQNlcBoa9ibmeyGghuNSdDyAuQigrBitu_w7Dc3Vny-lwH3t5EkvY6aJcwV58GoNsS4hZQYmkx8JquUe_WMw3LO41MWuRYZmQr896yBZ31XerVZE23Z0kpGSZ4N9_I-baGVU0hmfqv1w6T8Lw2_8RpAF_uNlYnu1ga3RThnwVrWp3aaz6pZabQvDNyhtD2YyiwZoJv501BcN6vPQR4cdjBTOT1y05wBJ_EHmZgcJ8WLMqMTbfDHxj0etEqoDWE0I49oN7ouno5sCONZ91gia1iKy-XdbS_pEh-B-JYU1-2cC5Q2-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سامانه پدافندی کوتاه‌برد ایرانی «مجید» در رژه نظامی ارمنستان در ایروان به نمایش درآمد.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/16685" target="_blank">📅 22:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16684">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45eb7047af.mp4?token=Gd4yju4bY6A_vaqZxXXI5p9yxtsSaFCSYkURqOqAT8aIQoKikkxBxub-kxynsk2n6tlc9bLdfKfDmcLGgnH5Qi9x5GEdgchuXbNBeifz2sitiak1DyuxenfArEYwM0QByiBx6tEpXufOKRdZbubM5ByDwFwiQVydCECPPN0K8LE2CLbWErQuIZK2xDdq4OKV3x8XPlq1A4ZXazfyF91VWt2Jcak0BGAfBssY_fL-ZZHnPuTRerAnqkCx0HEFmJmSHTIzMWqfCaemG9lnQ1FKV3if3TGoT03Lp7y5IvsHu0NCRFZCcP-bPRkKH20prBDQ-4vIKSEcD8N6OoFITizoZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45eb7047af.mp4?token=Gd4yju4bY6A_vaqZxXXI5p9yxtsSaFCSYkURqOqAT8aIQoKikkxBxub-kxynsk2n6tlc9bLdfKfDmcLGgnH5Qi9x5GEdgchuXbNBeifz2sitiak1DyuxenfArEYwM0QByiBx6tEpXufOKRdZbubM5ByDwFwiQVydCECPPN0K8LE2CLbWErQuIZK2xDdq4OKV3x8XPlq1A4ZXazfyF91VWt2Jcak0BGAfBssY_fL-ZZHnPuTRerAnqkCx0HEFmJmSHTIzMWqfCaemG9lnQ1FKV3if3TGoT03Lp7y5IvsHu0NCRFZCcP-bPRkKH20prBDQ-4vIKSEcD8N6OoFITizoZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
خبرگزاری CNN :  کابل های اینترنتی تنگه هرمز ، توجه ایران را به خود جلب کرده است</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/16684" target="_blank">📅 22:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16683">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">⭕️
فضای دیجیتال ایران ، پس از تجربه طولانی ترین خاموشی سراسری اینترنت تاریخ مدرن جهان ، از امروز به صورت تدریجی درحال برگشت به حالت قبل و فیلترینگ مدیریت شده است</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/16683" target="_blank">📅 21:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16682">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">گویا آمریکایی ها عملیات اسکورت کشتی ها در تنگه هرمز را از سر گرفته اند</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/16682" target="_blank">📅 19:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16681">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتوییتی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62edae59af.mp4?token=T46jwTX9fLPmNsFYeLG1WGLUef1e1N0HUzOSHssf4cvcsrHY72wqteX9CHkJGCuYz-hBM66yULadDpVehHx7C3Swqt0lvGO3hIViQkpcVG--8kbCPlhHLyVFTylnjIfKZNk5SLjaMXpQHA4XvjWQ-LtRe76n2oLevTf-TvxAj-rDJoOFE-BZV3eZSWKCCFLMoJ9Ns2RS1Kc2rRSRUel7BuanUCx5n47MXMDnPdjshUtPSoBnsTHwsrwl0JC24qz02Ic9cyf-I-d_MMJ8eq70meb0AP-hQBEBO-rPaNiX-Sl7Qxy4XXZdJHWDLHP6sBNu2ffM_zhrnFNd1V3e2HhFlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62edae59af.mp4?token=T46jwTX9fLPmNsFYeLG1WGLUef1e1N0HUzOSHssf4cvcsrHY72wqteX9CHkJGCuYz-hBM66yULadDpVehHx7C3Swqt0lvGO3hIViQkpcVG--8kbCPlhHLyVFTylnjIfKZNk5SLjaMXpQHA4XvjWQ-LtRe76n2oLevTf-TvxAj-rDJoOFE-BZV3eZSWKCCFLMoJ9Ns2RS1Kc2rRSRUel7BuanUCx5n47MXMDnPdjshUtPSoBnsTHwsrwl0JC24qz02Ic9cyf-I-d_MMJ8eq70meb0AP-hQBEBO-rPaNiX-Sl7Qxy4XXZdJHWDLHP6sBNu2ffM_zhrnFNd1V3e2HhFlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
🙌
@TweetyChannel
| علیچی</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/16681" target="_blank">📅 19:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16680">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">گویا آمریکایی ها عملیات اسکورت کشتی ها در تنگه هرمز را از سر گرفته اند</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/16680" target="_blank">📅 19:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16679">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">خب نت دارد وصل می‌شود و اساتید بزرگی به جمع ما بازمیگردند
سبحان الله!</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/16679" target="_blank">📅 17:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16678">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">فیلم لگویی شهید ابراهیم رئیسی
▪️
رئیس جمهور خستگی‌ ناپذیر
🔹
گروه سازنده فیلم‌های لگویی، بتازگی درباره شهید ابراهیم رئیسی رئیس جمهور فقید ایران فیلم کوتاهی از اقدامات و دستاوردهای او تا شهادت ساختند. @TasnimNews</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SBoxxx/16678" target="_blank">📅 16:36 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16677">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرگزاری تسنیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/110bf069a8.mp4?token=nww3WNfezOYDiLhvqAitS3XZqEecZxIGK61ZKQoYNmqYaPsRCcmUAPtyTtzRJvdqpAP4hcUCwLr6M6V_rcZBrtWz2g8ItWEv6wp8b1s2M-Zm4YQ980GYEtPJyY0JhJ64UhBvisODkrkPwsVAHHquAp6X1UR63D_SKoVCpxhtTkawUQsrBiv3c16TTDmK6kNbcaEDT9ka2ZjZ1qyRyxz5sfEH4AhInr3e2ZyR3NhNp9Eyy9deAKxFgc4XQLBl6M-jsk72UmzqAb-ASr17zwRncfFOMylnY7r6sxeJlX8wNIwcQjJxkH55SOwXsZG7EQmtCI8nD5b6e0aqsxxyvdnsPzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/110bf069a8.mp4?token=nww3WNfezOYDiLhvqAitS3XZqEecZxIGK61ZKQoYNmqYaPsRCcmUAPtyTtzRJvdqpAP4hcUCwLr6M6V_rcZBrtWz2g8ItWEv6wp8b1s2M-Zm4YQ980GYEtPJyY0JhJ64UhBvisODkrkPwsVAHHquAp6X1UR63D_SKoVCpxhtTkawUQsrBiv3c16TTDmK6kNbcaEDT9ka2ZjZ1qyRyxz5sfEH4AhInr3e2ZyR3NhNp9Eyy9deAKxFgc4XQLBl6M-jsk72UmzqAb-ASr17zwRncfFOMylnY7r6sxeJlX8wNIwcQjJxkH55SOwXsZG7EQmtCI8nD5b6e0aqsxxyvdnsPzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم لگویی شهید ابراهیم رئیسی
▪️
رئیس جمهور خستگی‌ ناپذیر
🔹
گروه سازنده فیلم‌های لگویی، بتازگی درباره شهید ابراهیم رئیسی رئیس جمهور فقید ایران فیلم کوتاهی از اقدامات و دستاوردهای او تا شهادت ساختند.
@TasnimNews</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/16677" target="_blank">📅 16:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16676">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UA_1Mhx93kr1HKfDCcbOPfFcgWwqXbg17sLq53IqQgswmtNVel5x01gsTSppsTPOUAmGILQ0VcoLOoaeIjbQuQMIxlF6bH-a3rsS4rh7YelG0P-pAJv6ozoaA-55oo-t0FQs-vguXpslzikg3YR7XneS9g3Y1uwZ1OhTfxuR3PbFf9ocEh0rrjjUAxwceS8TS35jwIU3rS50sodcdixW3XqVS7yZU0ychBhVnh8waPPUBLVDshvcZKHMajI4x4eZ_ojf8jHibiea-eUKTA3xAoQMLyYjCay2nIl7A5XIgGqWL0tfyW30K0qdthrLTso8NDJ8X-csXlGsmBI9jwmdQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواجه عاصف (در مورد پیوستن به توافق‌نامه‌های ابراهیم):   «تمام جهان آگاه است که ما اسرائیل را به رسمیت نمی‌شناسیم. آقای ترامپ از پاکستان خواسته است تا توافق‌نامه‌های ابراهیم را امضا کرده و روابط خود را با اسرائیل عادی کند.  با این حال، اگر توسط دولت آمریکا…</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SBoxxx/16676" target="_blank">📅 16:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16675">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">خواجه عاصف (در مورد پیوستن به توافق‌نامه‌های ابراهیم):   «تمام جهان آگاه است که ما اسرائیل را به رسمیت نمی‌شناسیم. آقای ترامپ از پاکستان خواسته است تا توافق‌نامه‌های ابراهیم را امضا کرده و روابط خود را با اسرائیل عادی کند.  با این حال، اگر توسط دولت آمریکا…</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SBoxxx/16675" target="_blank">📅 16:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16674">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8PewlRbwQ6KhxIt7Gi7bJdBf0wUt0_l6G2_4pyf0NF5GW4S_jr4A18njrstiJRUmTeLQFeIIRcn8kubA8bXm61YM_sogWLuRm78b7g9oXR1zQaZQBV70nSQGMm0IbSS6_iYGCi_1l6yy2xcGgispQUHXSG-NLrMaqQPQt1ww9DWtDhucT99NNTtkGClpQzXNUnHWhWuZ1Ywo3BtKOKfRzYFWSicT5mg08Y5AsPwqOnKV2U0_2kw2TJL0frB9wz1n7FEqHGjzLRtgK0A6Cz7aXAv1qZ4dOkA4nt2wJd5ZyQYNyAQz3qebifgicaAL1CBSp7vw_jXAkn3s9MFFW53Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان از عربستان وام گرفته تا بدهی اش به امارات را بدهد!  مستراح گدایان!</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SBoxxx/16674" target="_blank">📅 16:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16673">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بیانیه وزارت خارجه</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SBoxxx/16673" target="_blank">📅 16:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16672">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7WFEtjkgWETbwZpUr8x_bWrJ1X3u6men_C_66wmTm6ZbyuIgTGiGtxsv89V0zgjGbQvCbPgM0qYj-y7W6UItNeZ5mpxEF0SYjDtd-Xix-LPc07YeJ8ZDFAwjEgArwHYsrjdKrINtyoyfpGN_uAvTxy9FTCwKZUXKQCLgUH4GAjV4s4uq_NPGkicoLaats6Wy8ZXLhh6ZG3HsN8wT2Wdo1lOK-Mj0ZHdV0SVcI4Mbgjwmfov6TAejk3my9ylHqwkwyHz8odKEOfXQ5b-eH-MgsPXjFydNIJKdPcz_-hvHmwSGreA5fBbEKXhi_V-afTJ63DnpngezSGTKGJblqs3BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش کوتاه روابط عمومی سپاه از درگیری‌های روز گذشته در تنگه هرمز
🔻
ارتش تروریستی آمریکا در منطقه خلیج‌فارس در ادامه ماجراجویی‌های مداخله‌گرایانه در منطقه و رفتارهای متجاوزانه وارد حریم هوایی ایران شد و یگان‌های پدافندی سپاه پاسداران در راستای دفاع از حریم…</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SBoxxx/16672" target="_blank">📅 15:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16670">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/153170738b.mp4?token=QUftEtFf8vwXgx5lpADmEdtJ2TD8MxLh0C9PpFb5k3ZVrQKHjMGDU-Ww0oNLGetkkwfSLGSOP0mgufB2bdCLMCetFfGhiwHcACRvbAgYLK0yEtGn3bmgLfG7mR4bmhqXdbImoBToGjwyDLKgKWitcjDfU9hPjgfXKgAsf-DIGAVGDy7m6T34k0il4dqPILiXp3ve67Cmbr2Tf_YkUEyWJRka0DcctUZf3g-UN1g8OSq8z2cHn3fJGHXoTlxs4hl2l7NhcHqWv3jHQ47Lv8qaw2tprooyqNX9skfYFOQ-88ZOQrWCqIcMpYyc6KwHe51ylKKmEBqhNJ_a4F1koSNokQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/153170738b.mp4?token=QUftEtFf8vwXgx5lpADmEdtJ2TD8MxLh0C9PpFb5k3ZVrQKHjMGDU-Ww0oNLGetkkwfSLGSOP0mgufB2bdCLMCetFfGhiwHcACRvbAgYLK0yEtGn3bmgLfG7mR4bmhqXdbImoBToGjwyDLKgKWitcjDfU9hPjgfXKgAsf-DIGAVGDy7m6T34k0il4dqPILiXp3ve67Cmbr2Tf_YkUEyWJRka0DcctUZf3g-UN1g8OSq8z2cHn3fJGHXoTlxs4hl2l7NhcHqWv3jHQ47Lv8qaw2tprooyqNX9skfYFOQ-88ZOQrWCqIcMpYyc6KwHe51ylKKmEBqhNJ_a4F1koSNokQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این حرامزاده پول بده نیست بیخودی امید نداشته باشید</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SBoxxx/16670" target="_blank">📅 14:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16669">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">از این میخوان ۲۴ میلیارد دلار پول نقد بگیرن
🤣</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SBoxxx/16669" target="_blank">📅 14:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16668">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA.P</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe8b34f043.mp4?token=AuWjWUWUDp1RlxWEqXbfI5AK3NefxT8kEzNtKQEdxuzijvQFc93G602F8rzmIJwpGQ6T8Sh67EplFtsJnwTeYfBN7h9xALMxpqB0RPQpfrOHQS45E690KAOfaWnYXXpMgqhejoHVYEeFVmRVnCiZgOSA80p0iUQ8MHK7K-cbI7WrxgTHZJ3tx23k8fZgo_rJjgKMk70Yml-vbTOfF53kHw5H-gC6NmfskF5WGmKvmy81E7IFv28c2VAS0nZWRnHfOpPXDI5G6JNBRff3mUx3IGW4Da07GP2IihT-aXZcoVf-7gXHA_nM_Iqy3hdVTqOMdo4DkRbSyfR8yvU1lY-vZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe8b34f043.mp4?token=AuWjWUWUDp1RlxWEqXbfI5AK3NefxT8kEzNtKQEdxuzijvQFc93G602F8rzmIJwpGQ6T8Sh67EplFtsJnwTeYfBN7h9xALMxpqB0RPQpfrOHQS45E690KAOfaWnYXXpMgqhejoHVYEeFVmRVnCiZgOSA80p0iUQ8MHK7K-cbI7WrxgTHZJ3tx23k8fZgo_rJjgKMk70Yml-vbTOfF53kHw5H-gC6NmfskF5WGmKvmy81E7IFv28c2VAS0nZWRnHfOpPXDI5G6JNBRff3mUx3IGW4Da07GP2IihT-aXZcoVf-7gXHA_nM_Iqy3hdVTqOMdo4DkRbSyfR8yvU1lY-vZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از این میخوان ۲۴ میلیارد دلار پول نقد بگیرن
🤣</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SBoxxx/16668" target="_blank">📅 14:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16667">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJsZFp7ixlwVnKosG8T3G87IAFxmjJzshz03H0E4SkcQRyS5MNaY8qbVqBhLiLMcHpbdXBGbPL3nIeY2w4ramO6edbHLqvxTf3BbtT_nq9ygPxCh20H_DuumfRyyA-sUGQxaE4_B1wAar4RipqEYVzbLwKoWZGVAdB1idEKRGugpcG80lwyVSpHM4ariIbULtoXYepCEa0Rc626vESMleOGmnLTvWXqgBGVSxSXCMorpHUpUjljRCK8taNieyUfUcb0cYeckhUUm3yeIb0E5k-XzTLoPgaxNx4o7vwrYMQMnA_E8ljiDypDKk4bAaSzAz84JyekQ_yI6XGzISpAfPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدرسگ مثل این بستنی فروش های قرمساق استانبول است که پول را میگیرند و اسکل هم میکنند و آخر بستنی را هم نمیدهند</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SBoxxx/16667" target="_blank">📅 13:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16666">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_mUdNlRtjB5ZTsO6PEPd64ohzB7_9qEq23E-Q23iu3VJjncR4pjy0FE1tm3_OOVArejnS34Lo8NhlO1pTWFNfyo5ogzjCGGYciiSD3JKohkgPe4HOLmOMAoVv4QA8y-fa-oihMl8fRRhZrerbQN2CQnE_waFuJDu0EabuIPIIskVsBxiaHx_Wn4gdJPLCvRJP6Bp9a38JOwd2CMouWTLAf42negvzbhP3G-_twgHU5xHfUClHWgLd2cD42pYOsTar2sZTGfSHTFukS6LpGSzvrrCKvNbyruMclT6znbLXS-A4-vLPi8ZcCenjVoqo_nJyX0IPg-kd1uGhpV4tTD8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدرسگ میخواهد دو‌ قران از پول خودمان را آزاد کند چه مسخره بازی درمیاورد!   بسوزد پدر بی پولی</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SBoxxx/16666" target="_blank">📅 13:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16665">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مملکت خر تو خر</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SBoxxx/16665" target="_blank">📅 13:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16664">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">کم کم دارد نت وصل می شود!  نگفته بودمت که در این مُلک، هر آنچه خاطره ات بوده، آرزوی ات می شود و هر آنچه کابوس ات بوده خاطره ات؟!</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SBoxxx/16664" target="_blank">📅 13:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16663">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A08JZMzPNNy0ML13jsXCI6ytBzHqkSmL7WNGN6F3erZhaDhS9I0L5rN3D5Sk8Infxxl__16chbfGMFXxHx1SswbxKNE05g5v41bPPa2kKTJ5fhamighpEFQA7M7Ql-aSxT2TsX4jO2bc0W5giTpbj_PsqWf_5zIKipTqo7fC-7UnEv9qZ33UjJQS3cLi9t0HfeYyfUYYrHOw8tXLAdiXUpnt-5C1GII6qnKr0ZaPC9HvHuoLkBb0xv5EkPwi8ZBwFGRNuzTURJsTNQEFHORbgBUOzCyLe0In5QPDZ5tItX-auWVwOM9kHPdyABTFWw3aSdSmbHtsK7ni3ok9biSzBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤔
پاپ
:
هوش مصنوعی همانند سلاح هسته ای ابزار سلطه و مرگ است</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SBoxxx/16663" target="_blank">📅 12:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16662">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">کم کم دارد نت وصل می شود!
نگفته بودمت که در این مُلک، هر آنچه خاطره ات بوده، آرزوی ات می شود و هر آنچه کابوس ات بوده خاطره ات؟!</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/SBoxxx/16662" target="_blank">📅 11:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16661">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سبحان الله این چه وضعیتی است!  یک انفجار روی می‌دهد تا خبر انفجار قبلی را منتشر کنند!</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SBoxxx/16661" target="_blank">📅 11:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16660">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ارتش اسرائیل آغاز بسیج سربازان خود را برای تشدید عملیات‌هایش در لبنان کرده است.
نیروهای نظامی از سربازانی که در روزهای اخیر مرخص شده‌اند خواسته‌اند تا فوراً به خدمت وظیفه عمومی بپیوندند.</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SBoxxx/16660" target="_blank">📅 10:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16659">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">خاصیت موج  4 همین وضعیت ابهام و سردرگمی است.   مثلاً دو هفته پیش ما تقریباً تا آستانه ایجاد یک فاجعه هسته ای با زدن نیروگاه امارات رفتیم، یا آمریکایی ها پریشب قایق های موشک انداز تندرو و پایگاه پدافندی را زدند، ولی باز هم نه تنها می گویند آتش بس نقض  نشده…</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SBoxxx/16659" target="_blank">📅 09:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16658">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">فکر کنم موج B از ۴ هستیم  از توجه شما به این موضوع سپاسگزارم</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SBoxxx/16658" target="_blank">📅 09:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16657">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">خبرنگار الجزیره نوشت ابتدا سپاه پاسداران به یک کشتی در خلیج فارس حمله کرده و سپس جنگنده‌های آمریکایی قایق‌های نیروی دریایی سپاه را هدف حمله قرار دادند و چند نفرشان را کشتند.</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SBoxxx/16657" target="_blank">📅 08:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16656">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtARm0momcFZiPy4ucyCmaBhRtIOYOBla4ipjj9I4ht2st67qoIjXjWhklQqJ-5bMqn6cIYEhQSziUkiHXr6ma3YGtOXvNlfBqwkgLfCFVbyani2GSKEIwMDYRutNAz9QeWuSdX_q7FFCHMXqKrL9fBCJlCOj9o6gwfrut1yvjbWvoO1Lo0ocVqFjELJkp8XyipTQvQ9QNOqAKhAQT2t56X-AJyR62UKvklypg7N2TREhEFePYYbI9DHJ9Ix_L7qXFQnSPgR2BKPgsjTwR79J96UEWYjPGrAlK6NjcGWDq7zosbrEbRaVfMaAXsY1jk7OH4qp7OknFBP2a7UObqGAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روایت های متفاوت مقامات ایرانی و آمریکایی  از روند مذاکرات از دیدگاه موسسه مطالعات جنگ</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SBoxxx/16656" target="_blank">📅 08:41 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16655">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">این مجری را خیلی دوست دارم؛  اولا با وجودی که نصف شب رفته یک خیابان خلوت تاریک، ولی لحنش جوری است که انگار دارد فینال جام جهانی را لایو گزارش می‌کند! خصوصا آنجا که اشاره می‌کند به «موتوری که هم اکنون از پشت من رد شد….»  ثانیا در هر اجرا، تقریبا ۱۶ بار اشاره…</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/SBoxxx/16655" target="_blank">📅 08:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16654">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">وضعیت بندرعباس آرام و عادی است
🔹
استانداری بندرعباس در حال بررسی منشا صدا در این استان است.  @TasnimNews</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SBoxxx/16654" target="_blank">📅 08:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16653">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرگزاری تسنیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee94b5ab44.mp4?token=nbknjozDweadbOFc20E0XZvBVAkUgg-yui_K5w5n4z1UqZbeJA68Ee0HxOzRzvD89RDnbmlAar-0OHSE-4PvC-Ujpwfiw3qj1qvWju2IZMawKOTQ7-FI_fjdbIu85M0-mtrOCk4UDJRDdGwDRO0V25st53Vf6suHuJkoA16dGXm1yzU6XctwlFvB782ze_zUyx-nDKR-O7b-6N00TtVTUkfMiekdr6POlt1ITsHsz-_XHbP3RyzEam1o_hYmDMlsEdSDQRPwjKgBRZH9sBo_xf8t94LcAr2mbGEqOeD6LVRtsI0VSMlcqIj-J6uY4wGSwmpwGPUOymBZumgirFx2eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee94b5ab44.mp4?token=nbknjozDweadbOFc20E0XZvBVAkUgg-yui_K5w5n4z1UqZbeJA68Ee0HxOzRzvD89RDnbmlAar-0OHSE-4PvC-Ujpwfiw3qj1qvWju2IZMawKOTQ7-FI_fjdbIu85M0-mtrOCk4UDJRDdGwDRO0V25st53Vf6suHuJkoA16dGXm1yzU6XctwlFvB782ze_zUyx-nDKR-O7b-6N00TtVTUkfMiekdr6POlt1ITsHsz-_XHbP3RyzEam1o_hYmDMlsEdSDQRPwjKgBRZH9sBo_xf8t94LcAr2mbGEqOeD6LVRtsI0VSMlcqIj-J6uY4wGSwmpwGPUOymBZumgirFx2eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بندرعباس آرام و عادی است
🔹
استانداری بندرعباس در حال بررسی منشا صدا در این استان است.
@TasnimNews</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SBoxxx/16653" target="_blank">📅 07:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16652">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-dZFMFXpNnlYWKiuHSVxrUuoHw3xQk2BeEMwI-aXYK-7R4dZnYl7qX_bOZISOzFkwQschH0TFY49Sl_epYVbhWBXFT0iBcsKAixMudrxdA4a2krZdKlPDnYvVdU9-DMYpb4JGa07PTSZLvtxhRwv-f7-DpwSi_yht5v1FfhZkuo3kuy97NVOAb9ac8lR7Mi_063cX57RWUNzA4Z7gqi99ALLJ2WF8_8B_X7MTtGu_BLFvs6kM9ASxhSjptGLlVPv-DF49C7ZkFPzSU7wqNNwww9UqJvPlYU935VDbilxqL962wSnn2ITgX1IzOcNOuhlZb4JVSyssBs03-Um8M7_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ننگ بر سازشکار!</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/16652" target="_blank">📅 01:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16651">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">شما خونه تون مورچه داره ؟!</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SBoxxx/16651" target="_blank">📅 01:43 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

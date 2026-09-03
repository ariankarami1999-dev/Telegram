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
<img src="https://cdn4.telesco.pe/file/Zc59DGjKvjKPqgoDuwBZ6LUHyvOni_NdBSyfsIGvKDcMmpRaHXMSH1XLzcbSyIbUr4y-bK8hPBOjdB_fmB8gzt2c3usFCZTipSoXR4OMfzTm3iwf-xMcy69PPqEALQomC9QfIS_HBoMO4ikFS1C6966n6vURoqR7XiO2nseGq1kk0RQhZ8ihOs1EVD9ka7SwqoENhZ4rhGQ7VtMLpSgTWazR9zgXWm9jpsgNgepF8O5_vFGUQg2BqzYRXKN1EsnOIzHo1DzOaD6gpfx4bfQTLqEON4XUt8Ezs8f67Pa4ngR1g4Ab-e8sIhZuQ2slBJlS0theIccWK305kfcBjYQVJw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 17:11:05</div>
<hr>

<div class="tg-post" id="msg-459930">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55e904617e.mp4?token=K5jH9866h7yHmovMbAP17NMFt9_MT_Ef4R8-97FZEcU47A5tuJLIMQEQha8a-C77hDwq4XyoL--S6AbZWNXQqVdlzscIiEgz_Ivq-tHRFxJ2q6CmfK4B6p-ddpy3GkFaIjoMFRN25A_Q4_486ntZdJf15zxs6cy_fFCR8VAypdvNlOeM-Nqvz3r1grDZlufNoTt8zJAxw-FiUd4krAsUPPj25e4dcDDaVHJ0pIxR_efUqdDTHzjKbh42tjX0TtS-5K4CdY_jJGBBJsl4--RVxxZ737mbkC8tDLOcGlbdG6WyrQO7iYpKJta6R6q51TVgWzr4hzoTtUidq1vmp9W20w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55e904617e.mp4?token=K5jH9866h7yHmovMbAP17NMFt9_MT_Ef4R8-97FZEcU47A5tuJLIMQEQha8a-C77hDwq4XyoL--S6AbZWNXQqVdlzscIiEgz_Ivq-tHRFxJ2q6CmfK4B6p-ddpy3GkFaIjoMFRN25A_Q4_486ntZdJf15zxs6cy_fFCR8VAypdvNlOeM-Nqvz3r1grDZlufNoTt8zJAxw-FiUd4krAsUPPj25e4dcDDaVHJ0pIxR_efUqdDTHzjKbh42tjX0TtS-5K4CdY_jJGBBJsl4--RVxxZ737mbkC8tDLOcGlbdG6WyrQO7iYpKJta6R6q51TVgWzr4hzoTtUidq1vmp9W20w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نیروهای صهیونیستی با تانک مرکاوا به خانه‌های باقی‌مانده در حومه غربی شهرک حولا در جنوب لبنان حمله کردند
@Farsna</div>
<div class="tg-footer">👁️ 3 · <a href="https://t.me/farsna/459930" target="_blank">📅 17:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459929">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bolf7HxhZf3AkuAbxNH243XYRGbfxMPTReEbl8xvCA0cWb1rTmRm7YIR4pni99zq9UUbnENnUNk9T2ziz-7sIYhX-KH-cdRoWWUj4p72WwCOeoiEawyXOjXLU0qOPoieIagN4FhYsCltzZqQPNKr8EcSKOkDQXs9IoBitpfqHooGr93BJovB2gy2C7WodNbA5skoMRlSxvT9PbagiaQNIgJwFbQ9_7TFRvCtBtqEZYs5u4Bho03SSdDtqFeDP97nADyGaZeg2HjFpgMITR3pahhwAhDj_1z0rNOZNmyLhoxO1gQqGOg8-K8wTwdVW9DD7Cynwch42JsuZ6oaA4H35A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقائی خطاب به بسنت: تاریخ فراتر از خاطرات حیاط پشتی خانه شماست
🔹
سخنگوی وزارت خارجه:  در چنین روزی، بد نیست نکته‌ای را به وزیر خزانه‌داری آمریکا یادآور شویم. کسی که برای توضیح تصورش از ایران، به خاطرات کودکی‌اش از حیاط خانه‌ای در کارولینای جنوبی و کشتن مارهای سمی با قمه و شن‌کش متوسل شده است.
🔹
اتفاقاً مشکل بسنت همین‌ جاست. او عمق تاریخ و تمدن و غنای فرهنگ ایران را با مساحت حیاط پشتی دوران کودکی‌اش اشتباه گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/farsna/459929" target="_blank">📅 17:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459928">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tfy167kNNFI-7--U9zMdRUckwBCUnI17mLOoQ5pMYrY_A3VZ1tFc7bAEPJWHhgeoJu5dXQKRBD3Uk-qX2TfWJdCqZB8AJX-Tr3eXFaJEzOYu9wi69tICrhcIRt3DVeLn1d1Pn4gBBRc2n1W6urxNvScocTU4MvNmIroNL9NKOqqwnc9ogK1EDAVrqO3nR89KZDaQ_gsD6FA34eOAWtJ8ILy8eGL591S2Wyh8mr8lrl7Oe0fwvV7S1XWTmrb9lWoxHn7KX8S-yB-wfPvZJRZWJkc-Tg0oALkeELu7VClHwqEcFnDwHAxCn8QlQkGcrQ2Ix9ufQG4H7zsOLs9gEemhUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستگیری تیم ۷ نفره از عناصر وابسته به گروهک‌های تجزیه‌طلب کردی در ایلام
🔹
روابط‌عمومی سپاه امیر المومنین استان ایلام:  یک تیم ۷ نفره از عناصر وابسته به گروهک‌های تجزیه‌طلب کردی شناسایی دستگیر شدند.
🔹
این عناصر با تامین مالی و هدایت سرپل خارج از کشور، اقدام به تهیه سلاح نموده و به دنبال اقدامات مسلحانه در شهرهای غربی کشور بودند.
🔹
در بازرسی مقادیری سلاح گرم شامل کلاشینکف، انواع سلاح کمری و شاتگان به‌همراه مهمات مربوطه از مخفیگاه آنها کشف شد.
@Farsna</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/farsna/459928" target="_blank">📅 17:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459927">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">📷
نیروهای مسلح یمن تصاویر جدیدی از هدف قرار دادن تجمعات و خودروهای دشمن سعودی را با پهپاد منتشر کرد.  @Farsna</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/farsna/459927" target="_blank">📅 16:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459922">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pk6T2hAVhKMRzOSFnB2Mz46ivNuFlZIRmuYfQkp24-ZdGLj_WPep3xRHxoZnm8Wgm6ejxavxOKlxMP-cqXgU0MSAKN1SuYwyOEjDBxjE25eXHLd8Oh_M538dkK6LM52-wdD5IPUfv5M3KVwsQdERDbdKf9sEmz-7Tdcx35eUF-WnXrcA1aEfn_wQ2FlQphwhz90PPc9ckx4xZWt5Ip_qfI0A2z15AnaNx40EDlvVLIUL1f6WydN28v-6aGfBZ2NqZzQlSpnnPB47baerRa8t1JkXpz6VIGAJrjcROJNTsBW7KdE3q6kjjqho-ldnQwhxQRJKBGgwBv1mU6cFN9Evhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NTAIoKL90IE-CbCqROUzJ1T9qP6l8ApsgepjTPyjkolc6C14FohlA5wFl3O2dFnwu0x5hi_J5U9ATwk3X3nizueRQhkkqyyv8mIAdTgNT_6qcCVd3mgPAJ1fExaPh_g9yM8QORiVgyhjs_b7xxLa0Ykes1cDZJwgs9udFogELqJjc1eo6w9eDxlUWd81pN8DozrxNMkc1-GPLJprOKNavGqOGNkoCY1dC-hRV1EhR28lKleFYCF7mj0UVhpIGqinY1M82A-iGkr2wM2K5K2S6s4SmmlYItZSVx3Rz3U50IodUyhaW6QCo4O93lU8rU_dZBd42oSjx1i4jARvVX8TDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZI3bq-GsoIn9w1u4FyvGViHXvmsUorVNzUh_WYQwJLRGFJnLeasGgXvzkwN9sHxl86ZZVQSmsCZkZe4OFZyrfQZcTgI3oWR3wP1CbBcEvDp-YxmmTqixa0KaBwCKy2MO-1G9ToqxeIdISCLCDM5y01Ux6YSLHpHi1MhI2a7IcS_vuncBpDyPc5jo60wc6rHpH36QiCQ5WQnUXdLM0iptYW4HgWEKl3085WYta6oaHuXqrN918KBJ7SUVYS9NewbFKnVEhb02Gv3PQryDyMKoq6D6qZT2tYY8KV7GRbfZkLdWzbYzOl1tDP6pFD2wMqw2o8HyXX1WKDeQXa_Zuw-jXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z33kKb4-uc-dHNN-64QNSFOpjevdKZGB0QEnyGpiWae6Zn-aAaAMT8NxeAe04E5csWaaoejI2zqioq538UiDsHPymoV_9wzKvK1MzWLu6mDDTlN2sCQ77G_i0-00ja4L3CelA2xUMV3JIQuS8xMkYP08w9wMfo8saELpUZG-za_3SDUY4Vr9p6PJjx0WskXyn2lxpZEP066rmkN_EHaBTlc_6BAjlGSdWPOKn5fEA9T4GDY4Oxynjm5esJ-ndfdrhaUuMdrkEqmlbgsO7kmH6a7oTTFHVO8vtD6G-PLZzQ6vswTpzVM0f0l79jSUyT9GaAA08l-O8dQinxINQXA33Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LozPo3Z_x1W9J_lN02qKsfYwk8WQAiQvSCsORLefZp-3BctdhhDJFbgXaKQpWEy9Z8LYKHf5AQjbDtRDHt5w0yLDwctu7HdF5RpaIisONMg_quKACe4Rn-ZU2KluS_c8STcqhxb_g83YV-_ZL4QU3MTNgtQUivmoZmlXvLgC7HkIWg0IE6_bta26cOLyX1dbm8XHiBdMLktWCq4sQcbajnImA2KdHjt7SLpyNdg6aoBfxLIX1r9Z9iLVapEbmjKd_bYOw28_dccTnAZaERTd3dWXNVkiVOCLs0stm_-TEdLN-GWohwo2tk6oknWVJa_qmjPq4vpt-WQLq_rXtz95kg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نیروهای مسلح یمن تصاویر جدیدی از هدف قرار دادن تجمعات و خودروهای دشمن سعودی را با پهپاد منتشر کرد
.
@Farsna</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/farsna/459922" target="_blank">📅 16:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459921">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6y5UGouFv7Gsgrn99f-ESXu5tUm9zHzz3JdyK8YNpbtnFAfbCrD-YWl8X4QI0RRwDfp4Jtdz0icvIxgeTO8GGJevtgC9M2Uidc7fuOwgWrB8uezPCezuVQ0xGLC5fOKm5Osco6VfoIWIF5ghjCKrtdBuKY2TcTZ0HYLaV9KlWqXc1jtD-pzG_qT0XAniBV8h66GY3VzABpcculdSZ8SWSjwQA4PUnQuTZ5zJ5Ks_hJd7Dnf642nQ5jLc4CTRjQlzU-k4WBZIr3ni9Wqmr7vkR0zC-wz7A_Of8xKS_K3o7fIvMEyg-mCAet5iOOqSKNGpa82bf2U8C_FiSJdX7ZBuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
رئیس مجمع تشخیص مصلحت نظام: جنایت جنگی سیریک نشان داد تمدن آمریکایی چیزی جز توحش بزک‌شده نیست‏
@Farsna</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/farsna/459921" target="_blank">📅 16:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459920">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‌  پاتک پارس‌جنوبی به تهدیدهای ترامپ
🔹
مدیرعامل شرکت ملی گاز: با اجرای عملیات انشعاب‌گیری از خطوط گاز ترش، زمینۀ بازتولید زودهنگام پالایشگاه ششم پارس‌جنوبی، فراهم شد.
🔸
پیشتر زراعتکار، معاون برنامه‌ریزی وزیر نفت از بازگشت حدود ۴۰ درصد ظرفیت آسیب‌دیدۀ پارس‌جنوبی…</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/farsna/459920" target="_blank">📅 16:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459919">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gje_rk7aAm-GkpPGusgPa9XoxL4kR0AEFso5uVXACh-hez5eqGq6N8WoFifnsl92GEhAw4L-Ik39RhPvWAehR2QfKyveZGaWgFp579NkCV4APW_Kt5lEJEKjeA1_wnXdI0zGBI199xzxqacUg4L837OLe71_qonmc2NsG2MH8kO5pZlk79sAfwcq1ZjH2Sn-aMJ1x7A958LBgQPPPM2YVlD-5tljDorPZmvA-wlmJ-fsRu6qTpt6NVQtgFPuQq7SIV80Kqe0iZmEwRF8g8tiV1V9KpfC5bn4iU-W3drRR2_VQPBf0pgG28kLgZoDyOXbqTKnUzNR3Hl8-v0UsuRJhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتش: همیشه مطمئن بودیم که روزی با آمریکا خواهیم جنگید
🔹
معاون تربیت و آموزش ارتش: مجموعۀ اطلاعات ارتش آیین رزم دشمن را دائماً رصد و منتشر می‌کند و آموزش‌های ما نیز معمولاً براساس آن تنظیم می‌شود.
🔹
ما همیشه مطمئن بودیم که روزی با آمریکا خواهیم جنگید…</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/farsna/459919" target="_blank">📅 16:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459918">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c27655e7e.mp4?token=M6lSvyAd6HxIsJeUz74wY8M7awVWKSVR1xBveSB2JjbpU4zqUpybl3MQcxTncElYWec4tA9Z6GIBooXPVYmqaSNmbIjHGqmvDi-Zi37Bpx3cYUKMj5wbOYOlKf-xvr8eutU8Dyrdy1sTSYFaA6J2m6gXujgHYA2Wj5Bho6s8LYtmLBXyd6225rkUNvqlebmlUtuRJTjvh9pSqxUFLX2ujkZAjMhDA_t26x-ImTT0Omtydy3eHfnUweGueIJjPiJ1sYIdLdJP0aV2zeFM0wq3RuWPbM5j2_LkYo3w-3inCWIkBQZA40D0b0s3MM4JdpuVHAbgEg_RNfs7JC0Y5SbMZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c27655e7e.mp4?token=M6lSvyAd6HxIsJeUz74wY8M7awVWKSVR1xBveSB2JjbpU4zqUpybl3MQcxTncElYWec4tA9Z6GIBooXPVYmqaSNmbIjHGqmvDi-Zi37Bpx3cYUKMj5wbOYOlKf-xvr8eutU8Dyrdy1sTSYFaA6J2m6gXujgHYA2Wj5Bho6s8LYtmLBXyd6225rkUNvqlebmlUtuRJTjvh9pSqxUFLX2ujkZAjMhDA_t26x-ImTT0Omtydy3eHfnUweGueIJjPiJ1sYIdLdJP0aV2zeFM0wq3RuWPbM5j2_LkYo3w-3inCWIkBQZA40D0b0s3MM4JdpuVHAbgEg_RNfs7JC0Y5SbMZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایشگاه الکامپ، فضایی برای عرضۀ محصولات دانش‌بنیان
@Farsna</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/farsna/459918" target="_blank">📅 16:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459917">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ce05RXJ8uuKgjzmFly9VFfMBY8aVLSaihYE2lxFQQMYkY6J1ltxbM-ofYM6cqF4gGVRWKMv5klxNsoY3jPFwuNuwXm0XzSjF10fTCgnkcpNTNm3ZVffNiFTMIz9yOoqhZ3HuKU9tPQWfj-m3ogXzyUklAkf2nkh2JXAzXit5cf6wx4wsOTJ_Chcv_a3RkMyO0oMsMqMDYBSFpoe3pfRvpiCPLlKTglE5bREpCwEh2vIZ3pfkdlHfl9eC_S4UKNmT0o29ACYs_DwA2bwOfNJDBqAEgGvUxlD3YI2FXaD1gqm9r_lnAWFLREFjVESCsNHkPh8EOnND9x-QT8yQnZ1LXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتش: توان حمله و نفوذ در همۀ سطوح را داریم
🔹
امیر علیان‌نژاد، معاون تربیت و آموزش ارتش: دکترین نظامی ایران دفاعی است، اما آموزش‌های نفوذ و حمله در تمام سطوح و با تجهیزات مختلف، از نیروی هوایی تا نیروی زمینی و دریایی، به نیروهای ارتش ارائه می‌شود و این…</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/farsna/459917" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459916">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTOKCBxHcEp1Vkm-4QbumIEv1GLmfesCUeGvo3z_iIFcAcDvq3yp739G-A0FDZvWG7ickpiifD5FnFpSAfkw5mwGku4Dz-5AhN0hiXzsA024kCmJiu6buv6Qfx-YKMmwj0rRx5LbqKGlxwMxjJt2NfPBeMcf7UkCzJeeGvy9PaqFYrWTACr3kOutdL-mbuXvzzH3L2EpSlHK9bZZ9qdMuDpyx4FKknBIUrIVdo5zpxdy8IvI8PLCIYUbu272XVdvlL9j-rzHXunlFdNvrGLSx7yd8hVGKsYkkEkAljXMBNSDDfvLePF88Trg4GchWOnUksiYDQu9jXVF3n9pgvrp2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتش: توان حمله و نفوذ در همۀ سطوح را داریم
🔹
امیر علیان‌نژاد، معاون تربیت و آموزش ارتش: دکترین نظامی ایران دفاعی است، اما آموزش‌های نفوذ و حمله در تمام سطوح و با تجهیزات مختلف، از نیروی هوایی تا نیروی زمینی و دریایی، به نیروهای ارتش ارائه می‌شود و این توانمندی با دستور فرماندهی قابلیت اجرا دارد.
🔹
رزمندگان جنگ‌های تحمیلی دوم و سوم آموزش‌دیدگان دانشگاه‌های نظامی کشور هستند. ما همان‌گونه می‌جنگیم که آموزش دیده‌ایم.
🔹
در جنگ ۱۲ روزه آموختیم که هرچه آموزش‌ها واقعی‌تر باشند، کارآمدتر خواهند بود. این‌ها درس‌آموخته‌هایی بود که از جنگ تحمیلی ۱۲ روزه به دست آمد و الحمدلله در جنگ تحمیلی ۴۰ روزه مورد استفاده قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/farsna/459916" target="_blank">📅 15:58 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459914">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
سرلشکر وحیدی: نیروهای مسلح پاسدار حرمت خون شهدای کوهستک هستند
🔹
پیام فرمانده‌کل سپاه خطاب به خانوادهای شهدای جنایت آمریکا در مجلس عروسی در کوهستک: بار دیگر چهرهٔ خبیث و اهریمنی آمریکا، در اقدامی تروریستی و ضد انسانی، با هدف زدودن شادی و نشاط از صحنه زندگی…</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/farsna/459914" target="_blank">📅 15:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459913">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
سرلشکر وحیدی: نیروهای مسلح پاسدار حرمت خون شهدای کوهستک هستند
🔹
پیام فرمانده‌کل سپاه خطاب به خانوادهای شهدای جنایت آمریکا در مجلس عروسی در کوهستک: بار دیگر چهرهٔ خبیث و اهریمنی آمریکا، در اقدامی تروریستی و ضد انسانی، با هدف زدودن شادی و نشاط از صحنه زندگی ملت شریف ایران و ایجاد رعب و وحشت در شهروندان غیرنظامی بی‌گناه، در معرض جهانیان نمایان شد.
🔹
این جنایت هولناک که در حریم امن میهن عزیزمان و در میان جمعی از زنان، مردان و کودکان معصوم در یک جشن عروسی رخ داد، نشان‌دهندهٔ عمق دشمنی و کینهٔ دیرینهٔ دشمنان انقلاب و نظام اسلامی و عجز و ناتوانی آنان برابر بلندای ایستادگی و اراده پولادین مردمان این سرزمین است.
🔹
سپاه پاسداران و سایر نیروهای مسلح، پاسدار حرمت خون این عزیزان و دیگر شهدای اقتدار ایران اسلامی در جنگ‌های تحمیلی دوم و سوم آمریکایی صهیونی به‌ویژه نبرد هرمز بوده و با قدرت و صلابت هرچه تمام‌تر، حافظ امنیت و آرامش ملت و مملکت اسلامی خواهند بود.
@Farsna</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/farsna/459913" target="_blank">📅 15:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459912">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b774a39ae0.mp4?token=hRATx7JHD8_tVvDbFMaeklQP3mHZjL8h43NcWrG8FknCIJm8luLXZ7qSHmFEKgqCvxELbl-qDoRqAx_er16tuPaaX9-jUnCBxrmxsYoA8vjZzL9woNawG_AIVEiKWfY2mnnKMHkS1uSlJvHbxkPpXLDdCcxhC5GE187DYdPXazC1jXg2ApOlwzvCv3boHEUzxf_0AlCv0ElIR5yx_r5F56nrDk434A5BD3qvgtO4pk_VrgdsvzLuEh3y1D3URaqki20MdzXifjL1kjBE5drBzI6M26KcPe-3uvuc8h39HHMsNqJUWQUfy0AjHghu9j9V0fkG2EANeyzgkEmmIqWWzr6y26np8lajB0tH4pSuX2gkDLwyF4C_JwQCK6hzaPYmAWRIQ3gyr7K49rNrMQjvtKjZ-PNACNEkkGUKQvKpj8t16O4uQpGc1FEyMSdkjomD8ZumjuMMKMn1bU1aYUid6cK1FBMFksfbcdH2ZxmTrQBwlDNMYN17eGVxJ36oJlU-PkbDGoO9nVzvcJsPh_f7PB65AL6X_cf9Sro3uw8eIx3ANi9z7w7H7-EpI10PFAdvsSSEuwDOfZWaeukt0eOVsUBoSTcGk5lHoEx5EtTZ0iBpK0RWc2rdD3ZTedL4nmKwiyeGtEtmhXXwk4b1x7ERcg9N6FbAfn6ft8J3zhJmCac" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b774a39ae0.mp4?token=hRATx7JHD8_tVvDbFMaeklQP3mHZjL8h43NcWrG8FknCIJm8luLXZ7qSHmFEKgqCvxELbl-qDoRqAx_er16tuPaaX9-jUnCBxrmxsYoA8vjZzL9woNawG_AIVEiKWfY2mnnKMHkS1uSlJvHbxkPpXLDdCcxhC5GE187DYdPXazC1jXg2ApOlwzvCv3boHEUzxf_0AlCv0ElIR5yx_r5F56nrDk434A5BD3qvgtO4pk_VrgdsvzLuEh3y1D3URaqki20MdzXifjL1kjBE5drBzI6M26KcPe-3uvuc8h39HHMsNqJUWQUfy0AjHghu9j9V0fkG2EANeyzgkEmmIqWWzr6y26np8lajB0tH4pSuX2gkDLwyF4C_JwQCK6hzaPYmAWRIQ3gyr7K49rNrMQjvtKjZ-PNACNEkkGUKQvKpj8t16O4uQpGc1FEyMSdkjomD8ZumjuMMKMn1bU1aYUid6cK1FBMFksfbcdH2ZxmTrQBwlDNMYN17eGVxJ36oJlU-PkbDGoO9nVzvcJsPh_f7PB65AL6X_cf9Sro3uw8eIx3ANi9z7w7H7-EpI10PFAdvsSSEuwDOfZWaeukt0eOVsUBoSTcGk5lHoEx5EtTZ0iBpK0RWc2rdD3ZTedL4nmKwiyeGtEtmhXXwk4b1x7ERcg9N6FbAfn6ft8J3zhJmCac" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایندۀ آیت‌الله سیستانی: ایران قدرت «توانستن» دارد
🔹
شهرستانی، نمایندۀ تام‌الاختیار آیت‌الله‌العظمی سیستانی در ایران: سال‌ها دشمن تلاش کرد ایران را از فناوری و ابزارهای پیشرفته دورنگه دارد، اما امروز فرزندان این مرزوبوم ثابت کرده‌اند که باتکیه‌بر توان داخلی می‌توان در برابر قدرت‌های بزرگ ایستاد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/farsna/459912" target="_blank">📅 15:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459911">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52391e8544.mp4?token=M6JEtJ5mNoO97YfSaaCYeK0UX_7SgWOnCkqh_wgq8_hAETS0N9Pjp81eOrnNtC9TS8Uh9kepS4UpLgwbO0zf9xvRBmasE-0wdkScs2gY5IO_9piBcFUQyktJqSWSGQpfNG2AZjsX3ijSOIAC4kaSvIMZPTCJM09GbCF_O5ejU3bNPcpQ2YG29ti3CnOWheuf5NoLNhFWBBvFVYqeo4xeMNkitRz1OZr-JAUezJEvlQT--aAsU7--Ww28ocDe-jbZWJcCA9UUo0-V7gzTKCzNXZfYiAqPmrInGUy9fffSiJpfyvBGPvzLHkpvrkkXLVY2ue4NcGadkIj3SNGwja-5Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52391e8544.mp4?token=M6JEtJ5mNoO97YfSaaCYeK0UX_7SgWOnCkqh_wgq8_hAETS0N9Pjp81eOrnNtC9TS8Uh9kepS4UpLgwbO0zf9xvRBmasE-0wdkScs2gY5IO_9piBcFUQyktJqSWSGQpfNG2AZjsX3ijSOIAC4kaSvIMZPTCJM09GbCF_O5ejU3bNPcpQ2YG29ti3CnOWheuf5NoLNhFWBBvFVYqeo4xeMNkitRz1OZr-JAUezJEvlQT--aAsU7--Ww28ocDe-jbZWJcCA9UUo0-V7gzTKCzNXZfYiAqPmrInGUy9fffSiJpfyvBGPvzLHkpvrkkXLVY2ue4NcGadkIj3SNGwja-5Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌  دیوان عالی حکم ۱۲ سال حبس و مصادرۀ اموال ساعدی‌نیا را تایید کرد
🔹
مرکز رسانۀ قوه‌قضاییه: حکم پروندۀ «صادق ساعدی‌نیا» در دیوان عالی کشور تایید و او به حبس و مصادرۀ کلیۀ اموال منقول و غیرمنقول محکوم شد.
🔹
همزمان با کودتای ۱۸ و ۱۹ دی سال گذشته که از سوی دشمن…</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/459911" target="_blank">📅 15:00 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459910">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a1ad3bfd1.mp4?token=Yny8gXUaz5KKwjs5q6cS8m3Wsko995N9dAkcmC4cu47O_M_f4UBgK6QW5pA6EdsMZi9mYZ5ONWLwE-jcnvksBnS-Zk4Vm2021VHGKG_0JmqkT8akwE2hIlJWJghWjickOaIDQcErRrMHXw45pW3Wa0a9cOsXhcNlHqY9rlw2lysXAeJpO4SQdxYaLoAz7OufVOaWbGdQSlP2qsKjXpegCjNZZ66D0H8t27Mmkm6MZK4qg1XkS8TewP3i6bMg_boqjMLluqG8D91IUv4F4U-34aOROBNjOa3tlBqHeoVGWuDqluRjVEdnP7kjS94WqzpcQxZiKpks7Hp4H9l1JGHKIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a1ad3bfd1.mp4?token=Yny8gXUaz5KKwjs5q6cS8m3Wsko995N9dAkcmC4cu47O_M_f4UBgK6QW5pA6EdsMZi9mYZ5ONWLwE-jcnvksBnS-Zk4Vm2021VHGKG_0JmqkT8akwE2hIlJWJghWjickOaIDQcErRrMHXw45pW3Wa0a9cOsXhcNlHqY9rlw2lysXAeJpO4SQdxYaLoAz7OufVOaWbGdQSlP2qsKjXpegCjNZZ66D0H8t27Mmkm6MZK4qg1XkS8TewP3i6bMg_boqjMLluqG8D91IUv4F4U-34aOROBNjOa3tlBqHeoVGWuDqluRjVEdnP7kjS94WqzpcQxZiKpks7Hp4H9l1JGHKIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شکست ایران مقابل کره‌ در کمتر از ۴ دقیقه
⚽️
تیم جوانان ایران در دومین بازی مقدماتی جام ملت‌های زیر ۲۰ سال آسیا با نتیجه ۲-۱ مقابل کره‌شمالی شکست خورد.
⚽️
ایران با گل دقیقه ۴۷ محمدمهدی جان‌نیا در آستانۀ کسب پیروزی بود ولی کره در دقیقه ۲+۹۰ و ۵+۹۰، ۲ گل زد و صعود ایران را به اما و اگر کشاند.
@Farsna</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/459910" target="_blank">📅 14:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459909">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3a1ebec2.mp4?token=k5L7xY7qpUwBbddPrPYoaUF-zAemaeKGi4Hav4wTQ2vuYZ4zKDbRHPxcjr-DnHawbwFpk65-vJLnojY042Dlc3tGuzjTQf55oeCxS6KDrn5TSougV5Fv5IViAeDR9X4Zk7aXWsSmYBrJ7tEnvKb5qGlpzFYRXjZY2z04w6NlI_cADBrCMwjOMYi2mZP4fNy0MUUIiSvxA_ZeCjFKr4_oMkspnLdaq3N8LZZY6nomBSozFQih1YuwlSlcS4zElwKt12alwVtNsNbpFxlHhiDI4U805uktw4LFCnx08qH-FXi5oqW7ZE8cIOmAW0Zi46TA6gqzXfETg3Ypg7TfLU5p3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3a1ebec2.mp4?token=k5L7xY7qpUwBbddPrPYoaUF-zAemaeKGi4Hav4wTQ2vuYZ4zKDbRHPxcjr-DnHawbwFpk65-vJLnojY042Dlc3tGuzjTQf55oeCxS6KDrn5TSougV5Fv5IViAeDR9X4Zk7aXWsSmYBrJ7tEnvKb5qGlpzFYRXjZY2z04w6NlI_cADBrCMwjOMYi2mZP4fNy0MUUIiSvxA_ZeCjFKr4_oMkspnLdaq3N8LZZY6nomBSozFQih1YuwlSlcS4zElwKt12alwVtNsNbpFxlHhiDI4U805uktw4LFCnx08qH-FXi5oqW7ZE8cIOmAW0Zi46TA6gqzXfETg3Ypg7TfLU5p3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پایگاه‌های آمریکا در امارات و کویت زیر آتش حملات موشکی و پهپادی ارتش
🔹
در انتقام خون پاک مردم بی‌گناه و دلاورمردان نیروهای مسلح، بامداد امروز، ارتش «سامانه‌های ارتباطات ماهواره‌ای»، «انبارهای تجهیزات» و «آشیانه هواپیماهای جنگنده» ارتش تروریستی آمریکا در…</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/459909" target="_blank">📅 14:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459908">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b4ac6bc55.mp4?token=RO3dekiYlHIigAWA4qb6-D74c6PY82z0hagm6Io71c-ZqnLdz33OkWPMwXZWI51StSvU5j_Eej2fTOSvR1Romtol6u7xv8kUHlYgjWkLHRFx9xNqVSPLVLJxhNEIGwtqU8qwb3x1C29EH8hGwm3zkkKE4s-0QpMvFFtzVfh7sGn2gfsylmuUn6XySjLqLLwNPJQK7KCRthCShcbVWqkAMRJ1iQvQqJt5CcoaKzTKEVMXYsIupeRPyFLdAOBxkEOJcszXbuDZwPZfVq_3aGLcE5pLsLg_rDAe2UZh0BQbjOOwdocBbdZ-ve9BTFSoeJHVdO9nGrBBQXfbvIginBZSJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b4ac6bc55.mp4?token=RO3dekiYlHIigAWA4qb6-D74c6PY82z0hagm6Io71c-ZqnLdz33OkWPMwXZWI51StSvU5j_Eej2fTOSvR1Romtol6u7xv8kUHlYgjWkLHRFx9xNqVSPLVLJxhNEIGwtqU8qwb3x1C29EH8hGwm3zkkKE4s-0QpMvFFtzVfh7sGn2gfsylmuUn6XySjLqLLwNPJQK7KCRthCShcbVWqkAMRJ1iQvQqJt5CcoaKzTKEVMXYsIupeRPyFLdAOBxkEOJcszXbuDZwPZfVq_3aGLcE5pLsLg_rDAe2UZh0BQbjOOwdocBbdZ-ve9BTFSoeJHVdO9nGrBBQXfbvIginBZSJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: طرح ثبتی‌مبنا از نان شب برای ما واجب‌تر است
🔹
اگر بتوانیم مشکل معماری سرشماری عمومی نفوس و مسكن ثبتی‌مبنا را حل کنیم، مملکت را می‌توانیم درست مدیریت کنیم.
🔸
سرشماری عمومی نفوس و مسكن ثبتی‌مبنا قرار است از آبان امسال به‌جای شیوه‌های سنتی و استفاده از پرسش‌نامه‌های کاغذی اجرا شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/459908" target="_blank">📅 14:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459907">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oObJ8pmj7rd9kWLk7HlNsUwfRZl68StbpYq3TlIZDLjR3ze9VOoc-IjBUXPlvieLckzFAzqYgkPr0zubhTERXWg0vE91TLojgVh3xFxmB22P9w5zpyj0mooJG4jEVhkUDOk37Xfp6ID7chh56DqcEjuOYuPlBWqM8MKt4fnozt5G0LJI5kmt8VxVODECQ_Q-GsmPvFP-gl9_K9YcbVlaW17K2Jt5MdbS_sG0JSvVeDkRtcgE9xqf4r0nttLfXmgRcEyV4VcfgbyKWfA89h3Mg4AiH3g1mnFn2mxvvjAho6SmEv6VBn8lKuF13HJwp7UzWvQc0vUo_SOSTqdJRhmgTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عارف: ماه‌های سیاهی در انتظار اقتصاد آمریکاست
🔹
آمریکایی‌ها به فکر ذخیرۀ بنزین و سوخت باشند
.
@Farsna</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/459907" target="_blank">📅 14:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459901">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FEZkIeByoWBXBp76WvxPcCatFT2f8Qk135mv6k5zHgLRBAWvBt2rnLDdo151Cin6zSNIoJKr_N5Wis1jIFQk6GvzhiLCSvcF18w-ElChmvtFOm85gTec8Zu9SYvYbOlFaqEwkog3_YWqzvcwCCjeoJnSLGaP7yIJipXBpcpqwfWickAz3nyT6Sn4Iaag3nGrZS2if-t7qKpUqtDJs7-OdUO6JsktmJlQYlS0EyVEAuy1aF2WyeIyKw1xTqNYKV83mefxZIhkafpK8lFykhDzyUDNRl_vp1Fb2LR3q4Lf9UM_70gZQQmzIbjmmWssa0vE9nh9i2amhL3_ENsyPVhNXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vhD-shVZ3PXcd66w1NxhWEewpYHHtWu9Z3Oa6ziuOp1mh2V6y4kkKKjKWdMAB2ppXxNLNndORzsDCEhW0aI59b0BypuGom6U7V6WM_txkPIzUXZWiC8kkLBMLkKC5CP6HUxIYN1hvkMt6m06L3yMViXjZYKkaWsnZe9VDW2vYGTekYcnnEDr4hHLYJ-rPEcPI3B6nJSmhId6lwCrdzFMESTR_EmsqvyShgihkZrxl_mu8Lp5iD3_6wZoY0tE0V6Ljd_9eKjnedqic7Rvs1QWC15iwuZ8xPP1XG0A0f6ALDNgDvupWwqlQt29QbHv-vTNc0yF-bJq7pMprXu-_HDJwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bd9GsU_8p1fpkFTO9AlFhgxZMHY3McU3M6jjbR-u04vtVUTlwrPw-n92y-oTJYvLb6tejTmNqO6T_VInOzn0CMILTXk-uwgfVOsdK4EXoCtx_esKRfXEzmuZglGPqFxJADaA7DYHqPwd1rsmQkkmPf7OKMfQ3u0st4R_wfArn3ACDCT1KcE0Vs9D9O0sbzKHCD7A1LkCZqoTDl2lFCEpvV7gCOR4aoMKu2W0C2Naj7lBiFggrdXmEasWSdbBZnU5ADSbYzPCMKwikoLqFDNEQyayqUKaFeCzZwSOVJ9sOPfbQYg9u6d8g66tHSHf1NtUiSM1zIil_L3gXx3zrGCsgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a5zEz4FoIa_7PQ12EgF3bKAdoLMy5TouPJsL1fwPymPy01xailFzVEwlNhRe3Uecc1bBrrE657blquEwHXcxCtDwDcWAV-b7zO-vFWIRkmXW5rEDWa1lalZM3xcAhwcGl3gdGIMU4stRub_UuRFJ64yiXFRsMnaX2aBh_03_BjJRGRV_OQmxig2k3zMgi6R5YCZj6QjjV49QGTeYiLZNQctMyp06kWIBYqJRIYanRLzOR3DjoZ12iDjFoFwZmwZa62fwtbfXdZilX3frz5lHY0xQx28MFfcupDeGcppHv9TVbI7fLGOaPBrDVqzGcVcdnbvGE9vrTWi3ToaDF9o_gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NEEz8J2d_bH9uEz3O6XrTPslUvcm_ihBWASsYaT1BW03TICnAAuCbH4Dfc4dU4DTdrkvmy4SEYpMcgTWtpjsyYkoEMFk2j1ZMcxCetbzbdBleWcpsSNNNwpbcy_K8PILb7qcaC34glaAriVjVnDxf3uvtkmnuxZMI4xIXtHERVowrpk_r9Ri_jowl8Ll2fnOA8kujzE9L040TWbBQxZxOBBkhxd0kugfhTs7uPNsT5f8Cj-9HUuGoVsifk5XJTfWGMkv8t7Aa3WZ6s_2olDMiopfd4gQumz8mZLSvM-uzs20Z3vDng5g18H5AWm4NOnrPRY8o_GYP0IyVa4cmJQ8hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ldPYkXPGALyKArjhlgwk4046JCZDdNeV8D19IBYcM2jnmynKnwtAtXAxLzRjYAWdWoFH1PxlySPxgb8fo0uuHZOxMUxwzko2UieMN2XqKgLQs_mIg2GBeBh-vqqJsuC3_h_WO_NiinekaxP9IhzJM0lRru4SMFpuXmGk8JakQtPitkXYVYReLmJICbnJ4GPZhw-3Ot4Z8rtmjYtMbB-2HSrNptKb56NzQ8fONCoMocE28lSqQi2Db9b0JFi0WleyLnnYj1eBu0iDXIl6FH7okCsIp4rzjaWNG7e1WYNnZlO5RUreN4Nezu2ppW7KkIr1Kr1rKJAs5ZuuwAxiQT6GNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
وداع با شهدای بوشهری جزیرۀ لاوان
🔹
پیکر مطهر ۳ شهید دلاور جزیرۀ لاوان در حمله دو شب گذشتۀ ارتش تروریستی آمریکا در پارسیان تشییع و راهی استان بوشهر برای خاکسپاری شدند.
عکس: عباس کریمی
@Farsna</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/farsna/459901" target="_blank">📅 14:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459898">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TaQQcW85H4c5n9_ldYGOX4m48ayGMDiN1AnLqy4jC8t-9gYFE5kJo0DCDH79xEnKFZSJ4fYwjZ20Ad4ElvO1axh212EKPnI_ghIOyibalCRBKzx3jF7heEACqQmlZCK4mRcbQ6NdHg_8U5SaUlD__bmVZsFrgOXZx9RDoWkD1ooAXO5B3joiaqjjbyzM7ENTCVHx1ftTmUqvp40OhE_J1picCx2yzwWio30M_uNM7WW7XlUWjLU9rtD4NozW3zkY2TYUHKLDPM9XE4Zg0ytR6tcRpPuK2qnetV-OMU_AkKmD3ouYshODj_3Ea3oV4yjosFGwQzkPCxSFAqJiUa7J7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nwYrd0w1bqp_J1HZIi9axSZYKJo_suCcLWNNdemgTGOXkonqYMTy4hWNCKWu1q5xTJqzAmngYB0MkbUedynXpiIAscx3Ts37b03on7a0-iLvvHZRhG3FRKiYaV7xzIEbqt-iGEiADzQ4B5Yt1KceiWgIVH_HO0C3tj9OKR8g6_vrGpjGIGQA6QZ2E31GjB9HBM9jEjjZHorXk9GbnqRpeKht8Uo6fbzWCOhRmr7JDBfmRwJsVAzT3MTt7tMsfeSMQd0CKgg9noJ1_9rPxpd2q7m-r86zDh0JUdz0g9N1YjQpBul2fuyFD8aTd219M14axs5aRELyzcrCN-_HVc8mYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CmTmFIkr6qRszHk0G9DriioNEJptu47Pzau9eq_WEqY3Vb7w9vHIi3MeD3lx-LVhWGuJ73OoEGZvWPtBQzQcZmTpKmcHXOUNQLyEzw9LCjuktpt-Y2WLzMbjY1AQi2Og7ueia9SujA74LJx-EvcpheLUGLuJY-V81StnqHC7gblOV2ljocDVLZntojpuvki78vTHLRdr17--mZ5jCkp6wFR0dEcJdddTxrNOIV70QxzWS11z0pJcrci9Add_SShFwPL3_MEY4lRLbIZmbp6QCZsBfsvdCY8AMcWjJCpt1kdBx4yStE_Wg09Empu0OHn-v_nl4Db5twNWXSsS9Dfm2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
رئیس قوه‌قضائیه به هند رفت
🔹
اژه‌ای پیش از سفر به هند به‌منظور شرکت در اجلاس بریکس: این سفر در راستای امور مربوط به تجارت بین‌الملل انجام می‌شود.
🔹
ایران اسلامی و هند تمدن کهن و فرهنگ قدیمی دارند و می‌توانند در افول جهان یک‌صدا نقش موثر ایفا کنند.
🔹
نشست‌های…</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/459898" target="_blank">📅 14:14 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459897">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8cKK54cFnIK-NzMJ8qq6U504QXvrBZDx0si-YzWl17Z-03fQyE-N4p5V77Um_tt5giyotxtbvgUJYp6-JKyAEURA5wQg7ftm2UamTKXsQzu8quWkJ-V4qQiSx_2_jKI2G2_1Ep_pyv2ZwECQWd6yT8wvYEei3vO638SNn7nocKA1w2ARL9rUxhH2J5KkflEID5rNXmkdoR-V_kC0bR18TIT_ofUpOqVvDX5FyeU-HjlQyUGolnkHl9GKxWz9pXvcrkRvWStF0T3C3OL039M7RT2SDKXDo-NWi19uNHRh0EF-QUb1Kb7v3ywY-ruHVFWIFJw428cT42Ym_P0TfnvAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
باشگاه استقلال با انتشار این تصویر مدعی شد آسیب گلوی آقاسی به‌دلیل درگیری با کنعانی‌زادگان در نیمۀ اول دربی رخ داده  @Farsna</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/459897" target="_blank">📅 14:00 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459896">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_iXlcdVlXZF6KIERA-e35bbu51BRF1sRtDsiIKELcO2RzZ7oPD1frtTHtx9KAt1GzoY86X5lzCH0QY9nTfr2p_uM0jjbuOM1Rpvad0sgcmVC5RrjI_khhC9znxt9F5TH-TwicwGzCENyaZnQZcotMX425DjdPbefx4qi_O1Ee_4Mc4dYKOv0TLPAMAWGatQj7JkRlLJQQHU1C4hSD-RTFPcr1iif6mvibF4TJeXD2oNwkaWs136EoSyHDKHXUY9azRODRcpVJM52KsHWqx51YPdYoC-V5g7j7utFljENBtgH1352jhaTl2ximy-rbFPQB_IOkZE6vBQWeaHyt3Emw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضدحملۀ چین علیه تحریم‌های نفتی ایران
🔹
طبق آمار شینهوا، وزارت بازرگانی چین ۲ مه ۲۰۲۶ با صدور یک «دستور مسدودکننده» اعلام کرد تحریم‌های آمریکا علیه ۵ شرکت چینی نباید در این کشور به‌رسمیت شناخته، اجرا یا رعایت شود.
🔹
آمریکا این شرکت‌ها را به‌دلیل ادعای مشارکت در معاملات نفتی با ایران در فهرست تحریم‌های خود قرار داده و اقداماتی از جمله مسدودسازی دارایی‌ها و ممنوعیت انجام معاملات با آنها را اعمال کرده است.
🔹
وزارت بازرگانی چین اعلام کرد اقدامات آمریکا، فعالیت‌های عادی اقتصادی و تجاری شرکت‌های چینی با کشورهای ثالث را محدود می‌کند و آن را مصداق «اعمال فراسرزمینی» قوانین آمریکا دانست که به گفتۀ پکن با حقوق بین‌الملل و هنجارهای روابط بین‌الملل مغایرت دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/459896" target="_blank">📅 13:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459895">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">محدودیت موقتی در جادۀ کرج-چالوس تا ۲۰ شهریور
🔹
سازمان راهداری: در پی اجرای عملیات عمرانی در مسیر کرج-چالوس، تردد در محدودۀ تونل‌های شماره ۲ب و ۳ از ۷ تا ۲۰ شهریور با محدودیت‌هایی همراه خواهد بود.
🔹
محدودیت تردد در روزهای شنبه از ساعت ۱۲ تا ۱۵، یکشنبه، دوشنبه و سه‌شنبه از ساعت ۸ تا ۱۵ و چهارشنبه از ساعت ۸ تا ۱۲ اجرا خواهد شد.
🔹
روزهای پنجشنبه و جمعه، ایام تعطیلات رسمی و همچنین روزهای قبل و بعد از تعطیلات چندروزه مشمول این محدودیت نخواهند بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/459895" target="_blank">📅 13:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459885">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qcsl4oeWSzmqBUIE5fWz7gxp045yiUm7baULS2qG1Q-GW6TzO8ZCGWPWovtr2Jles_1k2f9wDXH0pzmQDx5wrM1ktyspF6c8jRU08iHCszrzp1RePk-KuoRfXTWwyTnMPkA2zN6Ua3g-cy3Ybh8McLlKk0oRFBlAL9qieZ0HbV5IDQg94qql0OO40Wgu018_zODb5BOrbjL0DZNX4NOX-faq-svnrdUnIqOIhlAVLNQ2slcaRCatnzVi3ErDW3tV8iFi1TMF_oV-OWocXi9l99Eb8OuCRb2gbS_k00ZEh2a6M0SDxNtPEewq6ozUdm0NENCdVK0Y45LMQNzWV4k9aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N-w--N874GeUAwJQRuEt_4_A-i4C2wUXSMQc4iGrGQ86agPwTV4kQKJTZql5TAsGx6d4-XAPPYjEuQgdFmwqW2whRLGUrXXSt48Wx7UURwJFCuMvxvTaBaYwG9V2XfIB7WigZviZZOXgeLChQv2hnez-BcJeCkoRWSv4KuKK4M9saWpIdunwf7-wFn4YzIE8f01jpS3Pxmc7ZLAEWxQb_U8wl2vqZeK-YfZpupzRPMO37SL-sULPU705s59ls36fQ17osGJBCUfJUD-s-ebJzF3iBIgzX0Wf_16v3BuL0Qcth03A-G9bDIwc39O8QOutmA9mt2ZWuO8ni1QHNWpfZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cYb8jvfR9nnzLcT2tR5CZATIzCpxT-ukhW8JS-OnmndpiLqsE17JTCE2fp8FSJlKX9Eu0TdnYlIRtOD6EAMInBE6ME1Kd09W_S7WdtMiHWFmCHoHOoqMIL_zxEB7YN7neOMIWQy28P193k0xuaIi16AK94APIJJbyOE0B6P7iRgaYpKrOskscDaioAd6LKQvMr5iMXgXdSi9-8h2YhOB40C-j5Q4_6ZJD5BYO8p_9d6QPHP--V5ByGAVopfknPO6KVZrcBjmAJBHIKTn52UiF_IYz76LyCfWhlL8b0D7P0JmkSPyz43YuEvIsJj2wnnlKfLvMsh0V9ORV2UsJuvNQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NZQjuRLhy3_snhMXttOiITzhmofauy483qQfiWM0RXwxpfBzwfulhC6KS-xPem6G2Ldhrm1qncSLc2_ynF6Kt0rBQypW89pazydQqd6TjXdeLlTiZiKgistHhhFpT06GxX-P68IlmVgeZag3Y0bj22aK6v-GXFJqXEQHRmLp8HdhP23IY7S7gYR4pbj5uu2bDN7-gqdq09WNl88M4d_1qoYSZSeJ30qyAxgGGcdFMHGSBxZllL_WgBxD59t9gPPAM_Fi0M0R0qN-yFsMLxYlC_11dIPlnUHwUcYjeXKlg5_EDS8Bps3OpRoqYuJPOAlkK4jNagGEbHPaota9yjrtPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PkPGwXwPfWFs2-H6NuwKyqza3B_-QZMiDmdBpdMrALtR2Esw4C3ZYV66Ob3aTgsECKb6j7Fc7EsT55owaxOnDMpxCd0zs0ktwhtPVQTIXJpfSbqE35BSnmDufRtpB-E7OGU4czgldI9F82KQDS_n0G0M_0k3RCorKNIaeCcVT0iel7qeipm47ZaJFohyzj-uh6zZRVeGcDeEs7WuNyJwogYPJGBKITJ_6oYteNBJ4XVILzQKNSC9qKepJqj1cmFnO0yPAPFUyhq2NcV6gU1bTVch-KKqByFyAuah0lsCNKhu_KG6MtJe9mFo-fffnmz1H3MB8AfEkj7GdRTnbT-leg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TNVOv7jyUqRJa99ZL0eh3iCRd-rljsnIRyP7q0dCWbDbrUOGu6BVKA5Xuh8kWhWmatRkfKDlLUAHY2rpZtblOLCvc3RLvoR9pydTlrle0WVDclCOrNDl57a9YKZjB6wX2GLEaaF2GGxuAW8IftwXBQvQOL65jMdlLQIM1FnR7mPsXEobq1oUrWfN81aKuChMii1ZiafABlrlcG0f4h-8y3fzxoBIRbk-uWqCD3IDgRICLvKgB7nMJFsedu1go3qIN_XSvfG7jNecsVoasDWp2EPak4Xn1RFC8xWCz8WtII1_NMY8r7BrRck_J4njWM99riwV4lscVRiTicpHqYj5bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SnOImwpR_IycHWDIlQL_WIn8XwEv0rIRvo1vdHGhuO57rZrLsgUwFR1BzrZ_u-D9Tr6AQlAEE4uhSP4Mr9cAp3qF_NV0Yv9Vdg7_Xs0YSnKl2mt8_2A6LSa6NnSspM-AHSj6Z7V6IejqZGqrzQivfS9L7usCpwlO3L1o1LR-T-s1d3w-fbQHxkzKerGVfBdVRo2Sl0IVSB30ffJjPBTRskWsVvHjiILXpfAd2HefI4NxZEMjldVe6vkfRWEohqTRT1Q6RhRUrG2RF-592qgSUaqhVnhpBPRSPytXZ7XxCyvvd75RSPoQIZ7MQxXnsqK3NzUmBy6OEGrndhBTIX8tJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OljGDLuRns517yTgHS_Lf5ocIfSNBYsQtFi9_mDXUowQ-adKZhwxtMvejnrQqoTgIRlNU0gXWxn88JdDJLa_MhVINm49XJBSQfYTukPQxqROzfQnHDVfrNkmFwsLPFy0RMiwmh5y1ByZTwuq-ZiOMTTePuk8aMxnZfV8l5Glau1DCLob9UcyhUVGHbHlkSrSFZ_9u85NQ3zHBl6-dx4MNFI5gZgsEBYQL6uPp1NDgYx76Kvjv20hBK9aPYEDw1J6wzWCgrXNnxrIaM5uk6tX5nckB_qbYpgTRQnSAQLj_Q29FTYKf4LgrBiiO49pXhh5tc9nskf8yT_w2RfsZgR6Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fHAX-XlgF9jq7rOHC1_c4XnQblVMGfhz6psNWf_ZyIk2vvNwJW5cep9UgzxIJBjaApTXEhQaeWr_ksaLwj0qgQuTVxZs0qxo3uUzaEi_BjNpTug2WgOmrRzmhGlWkCcuDC4nLQoz2MvkdfkDoBg0vi-eS3OnELU7LMqBl639gIP63lXEaldrAR0J-JwBYTsgprA5jObjcbHGNnFzbFqRbcwXcLZ-dH3YZ0lf-cq_SpzkmTFPiLjJL1Wc9zHLa1p4xntPsVelERhDd47fgzawD0Qg0sYHU-sugfkNOCM432YQCpRnLe0VlxUW6nVK68yLx_jRL30B8N43sn93T9DJQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KYK5Qvdsbg3lBJ9WJkhxLTfxFJvVHvt-mhW-F-50oXOgyELL_cPAUFo35433Tz4oDCEqCqZv5o0qih_UlAu8UOUWYzrum0qXm8Fekks_T-ur9aErtT4gvnqJK1IFy4gUfQ6XDQ1Ui7ii7vCbGlva8ypd42Zdz6kMUcmLI76g9hQW6oj6OJdqJsQNhuB0xLHNoY8Hy7i0NKFMmtNcdidXrdsoS1NY2kOIWoJcl5q0eOYbyqx6OA1Cc5nU1TYZ5SrTMMBJCWPSY6lT2f7yaqveeIsDvwgMeJmQtFfI5c84j7Ih8hLsT2xqz8DH-exEId3SqPiMwatloVSGvi6ComAdsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
بازدید مدیرعامل بانک صادرات ایران از نمایشگاه الکامپ/ رونمایی از محصولات نوآورانه توسط افشین خانی
🔹
مدیرعامل بانک صادرات ایران با حضور در ۳۸ امین نمایشگاه بین‌المللی الکامپ به بررسی آخرین دستاوردهای حوزه تجارت الکترونیک و فناوری‌های هوشمند پرداخت و از ۲ محصول نوآورانه این بانک نیز رونمایی کرد.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331
#الکامپ
#اخبار_سایت
#بانکداری_هوشمند
#بانک_صادرات
#بانک_صادرات_ایران</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/459885" target="_blank">📅 13:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459884">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lk4LbnzkIm_EIIU8AOiDEvL3txOsHJhTWLZXymP5CmQ0gM5yX2wX7arHFodx0QHfs_pXYXUefEhE9UVnr3FsLSLdBznmPIM6iiwR3XC9033y6CVmUOfev8NeMe2WObAimI11wHBI2WlGW9z3QNwriz_16iRyAn3Ha_6IBuU1YG4drJH6s1nqNhZWE3fyYqSNobQt1rrnZ9plM4wlHvp1wmVP9uIsFBAYUnlyeDpjKN0oY_6yP_6cwOpyEmZqWaaHzyWz2-T0uPqXCgz8fUSvrAPahHl--O74x8Rm4hbaQFstb3CeRBNr9x2irSHcG1Ubi4DyFhkgMGa3ygwgEQuJeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
یکشنبه‌ها در پارک آبی اُپارک، بازی‌های گروهی منتظر شماست!
در سانس بانوان، در کنار آب‌بازی و تفریحات اُپارک، در بازی‌های گروهی شرکت کنید، با دوستانتان رقابت کنید و شانس برنده شدن هدیه‌های ویژه را داشته باشید.
🎁
🏆
🎟
برای خرید بلیت به سایت اُپارک مراجعه کنید</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farsna/459884" target="_blank">📅 13:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459883">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAZwcXza53Hzz-VkrQuMQXAy6BlrpdU6UhkOccqCLZUPPiBQs7xOypj-IUkym56eIJBpyNSINelq7Ho-MP8phWjv2lObFnsxGNWr5CmqLmte5DhLzZehJXArh7g-dNERsDcCdk-Bm07xn4IGGAABun3X-psvpvZeWJpH1xvf8cPu0o7esjhJgTWVMa9duuimoPfFizZJmBKeFuehwz4JxW7UybYgkNfMsXs9wd0jq-dt5pW30JlkdWXcTCfiJysyw7sfByLkRHvANWFdv8N_9Ax4zXEI5n8IUqwZxPzAbR6bNNajS18qzFCEkpmr9RZQGUj8sWhBvV7X9YhL5X-0zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داروی ایرانی درمان سنگ کلیۀ کودکان رونمایی شد
🔹
داروی ایرانی درمان سنگ کلیۀ کودکان با نام «سیترولیزکا» در بیمارستان شهید لبافی‌نژاد دانشگاه علوم پزشکی شهید بهشتی رونمایی شد.
🔹
رئیس پژوهشکدۀ کلیه و مجاری ادراری دانشگاه علوم پزشکی شهید بهشتی: این دارو پیش از این به‌صورت «دست‌ساز» در داروخانه‌ها ارائه می‌شد. حمل‌ونقل دارو دشوار بود، زیرا تغییر رنگ می‌داد و می‌بایست در محیط‌های خاصی نگهداری می‌شد.
🔹
داروی جدید ترکیبی از «سیتریک اسید» و «سیترات پتاسیم» است که محیط ادرار را در کودکان تغییر می‌دهد؛ این تغییر محیطی باعث می‌شود کریستال‌هایی که قصد تشکیل سنگ را دارند، نتوانند به یکدیگر بچسبند و بزرگ شوند، در نتیجه سنگ تشکیل نمی‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/farsna/459883" target="_blank">📅 13:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459881">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e52a16bbd.mp4?token=Z7j5uSwpS5w-7hRAdmITjfYnd2fdOjrPyie62_sH5d1HFxVp6IXTPeMJYMpiCxI9Q9vEbqOwxwidHva66jteF5DDvVvLqpOZUf69qwNdp2CNT9sJQXz2me6-4xZSHZ33U7BGuO_NK6zh3c2BQmXEzn0z2t4w7FM4iOg8gCIr85XhhZDTTtmWea9pk_FGJASg_lxD7gcX9v5s3lwi0gK--zLpIckRfSE-CxaMvLW_OMWdBpXEySjIIybnGR0P5qBY__ue8PgetcK70L2v-KFwP51OnDWyeRuHMwIy25m8NgUULnJrTrab4MWi8WVrNnMQjBHKucMWLOgl5pMh5PjX8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e52a16bbd.mp4?token=Z7j5uSwpS5w-7hRAdmITjfYnd2fdOjrPyie62_sH5d1HFxVp6IXTPeMJYMpiCxI9Q9vEbqOwxwidHva66jteF5DDvVvLqpOZUf69qwNdp2CNT9sJQXz2me6-4xZSHZ33U7BGuO_NK6zh3c2BQmXEzn0z2t4w7FM4iOg8gCIr85XhhZDTTtmWea9pk_FGJASg_lxD7gcX9v5s3lwi0gK--zLpIckRfSE-CxaMvLW_OMWdBpXEySjIIybnGR0P5qBY__ue8PgetcK70L2v-KFwP51OnDWyeRuHMwIy25m8NgUULnJrTrab4MWi8WVrNnMQjBHKucMWLOgl5pMh5PjX8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملۀ شهپادی اوکراین به «سوچی» روسیه
🔹
درحالی که هشدارها دربارۀ احتمال قطع دسترسی اوکراین به دریای سیاه در نتیجۀ جنگ ادامه دارد، بندر سوچی روسیه هدف حمله قرار گرفت.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/459881" target="_blank">📅 12:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459880">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TcRdtErGikk7KnoH7XDyXvvIcTI53738bJE9HIfEwgVm160PeKdL4Kqfh92vNmz5wGgcjGfJIHOUIdI5pOSSoG1uNUTd5pnid4z4uOHbbFe3FOtJLpaZsELEfFH8Vf6rUwmpEYcRDpAbItWVALd6HA5Z0C9JmRQtcCpCoeviHyGDVaNCQsANDmJdfVIs9DUJtnv5uvXdLqrNjh9MpCoxfhdLsxsz6Wi9oqY3Te-wHzQUSbcNIIPCjd76-EuYjZmYCv6f0uXMbmORUQyyxUNHW9HAGcqyMwEaO_rFB1don97o1KapMsji7uEDqFKiX8RJhRdQhlLyhBlvs7PCpJehOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
سلاحی دقیق که آمریکا با آن به عروسی در سیریک حمله کرد
🔹
بررسی بقایای به‌جامانده از حملۀ دیشب ارتش آمریکا به یک جشن عقد زوج ایرانی در کوهستک سیریک، نشانه‌هایی از به‌کارگیری موشک کروز پیشرفتۀ SLAM-ER را در خود دارد.
🔹
قطعات مربوط به بخش‌های الکترونیکی، حرارتی…</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/459880" target="_blank">📅 12:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459873">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ryJYChaWmrLjwGT8gKWEXFKiplV1B3AxrUNltdFzvww-Z4ZFn0b7328nNgml-y4hAoLOMTc16o49goHapn5Z3ILnvKzF1RHJ3Vgd_pG2eW3amm0Sfi3RpPoyLvn4Z8rYZ6NmabIedgc7jAE79uYoNqryHNI7gYhiet-1Dm3A3bRHU22GHZzQfajglNKuri3cfmYWkrtOXQj0qdG5jCLEPavI9XoYQQ5zdKNBP9KBX1egOTRwlaiVE8QdbyHUjY7lHBH2BHTkUQtFrzIxrP9yMZ25jS68xpa-MCPfKigXUHHr5CxTocUwHiH7L_e8jS_723Mm7NZ_CArkDuStaGnx5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TQ7sHOEFJ-upYFZLf-D-QsEQkCRVDOvj8PJ4uYcnstIe2YEo-UtTXi4a9vy9W-2HG_Q2hc08kYqif15mtToEMFKlmPANIYOfvH9OokH07xYejqCKPu8BFqP3SahuV4rBTH_SIigeO0QiugRFBvNxw-yMjLUjXO0G2v6RITMJFQZyivSYVRinTS9rTBrb3yOPxO052cOd3cvC2h3wE2Q3VxKvOBF9cw7LO6l1gNZOMz9zByEt5QS9_afmI2k1oqpab7jpVqtNv0FOBrkDAflAfJ_G5OgebPRKHqf8t5KObhVHkwQ84UYsN6M2pNsCoQK45Z6cxyulJPAi-EOJJq8c7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/twvWYZJYxJcV_i1cxDwwLE8q-GQApobXofLlaiKKBnjJ2opEb--L1Kk2iSM5lVeoxmDoCyPflRKFV0zfV66iB1BhzPDEz-qeTOUWxy3edgKO_Rb2_t2jcETY777UPqd1UszYTwdPGUDXtkuK6kq0IA6TEbfhgr6ulfC6ZbcDodFvYYNdLlOVDK6sLDqNY_ThC6BZnthP2txjtXbXXK-X-yn1PidyDHAVIvZ_QwurVue_73Ad1jcJNny5RJvFvsQrbfwAoRxcPgjIzo3i0Drf6M3FXJ7DiYkyCbvmpCY462n4lhL3mawSx4eHR-2Ec0STcoQmcceqFceWcJUauLhc5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ttkns9VG4DBphuP57jpS5snZg-F_5p6Du934LVZ1fWeal7902sEe2sEnheSuGx5Lv-yef_WplM_5Yzrqgjnz_Sp5ocFy5LttlVzCN4Yz781cr3oQ3dRTYWG2sWRJXWYm3qeWQ-XXd42Q2AP4WLpLxh27_lJ1heN9LqBln8umUe-D4E2RNj4QXnV4ThnCwfVAbVwdQgeaRbWwkntdY-rG_oTPU500YthKGouM9TsEwsOZpJpib640EzipULYGKybAH1S8fQedv0GDXz47jaj2fsa_DQJDTAeRKBFuKyDt1f2AA7fcxYdoCaObVSnR0G8x8aDRsGAtnRTDhh5jCWrHBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T_Ca9hdb2UVkxRmmOJwIJ2YwAqc2NGQV6AixP1LVJ00OBqXf9nGRTIerK-bdWQLSPlhfeSsBtQsx4ykck2NHAMd34DeKiyv3FMUsYNGaxt1qOHrdeqDwpC-tbXJHA2Ag13eCHScBYZQF7YUNFhvJMMnsggL8BBKAK2uPsDY4UiVB-4i56rnyt_YhgGAMZJ2nmGkxKlEa4qF9coMrtcHI4NzVNK-ftVHR7tiaLY25-WGRNnvY7muzKh4Jpnp8qLHKYgXeC7sWim5-mxzKESggIc324Omo82WODWU47gb0tI15adNvTrstcxVSY9QCDZpX9EX7cbRPnZLt8XyhXxEXrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YiQgBCgJC1-dBUOe09Um3JxG0OXJw054oT4zQgfEHrZv431oxOK_yXUOYtfp-Sgan8RZI0TzKVyveTslMrzBtvyEinaYfob5yDp1d37QhSVZB4d0_oFymJpqb8d-lh7YB3yP7VszuAT4DoLsniOtaciSBt_pny5r7q8P0-_OkrWwr5Z4I0ert9Axia1dIlMseSNGH9jcVtUHDOJ9QIZWxeyytUQNKyry-UWchr1K2ayQ9CY35o5j5VS8f-T-zrYPW1p-ogSnP7yCJr4HElU69q4UARCAlV7mPHcG1jMLMiJ6gk2LFNGSIq6h7nKLw8-W330ChO2FeTMc40M1T1IDUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JQe-F26MfHlgjy3ENBIzA_CIHEXGCybCluqtIaBfePokDMAbZPoQr-SBM13wvSGYOJBg1gXVqpRi3D4UQyyZfjR_DNFZ_gjz7cAkMS8E73AZfhpxFHH1D1fWKKcj8Eefnww9wdMDAi1hjg4NhdhJrFoVvC1bhFrY7-jOsAR7-i6bDs0LXJ3GtGbOwj7hUNRdpRnPlSp54yX82GVq33-_E8KRN1JbdPh8j0FkYA0qY1F6L9ysgE4dIu8UbH7XYYeL37LDmUMNeF-lCxLcpXMcH5SoNcf3uBSni7B-MUi36--kkKYkHBzb_NEXyTO8Zk3I7b8AzNn7q5tC3d_UL3fIeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
گرامیداشت روز پدافند هوایی
🔹
آیین گرامیداشت روز پدافند هوایی با حضور فرمانده قرارگاه مشترک پدافند هوایی خاتم‌الانبیا و نیروی پدافند هوایی ارتش و شهردار تهران برگزار شد.
عکس:
محمدمهدی دهقان
@Farsna</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/459873" target="_blank">📅 12:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459872">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebe69231f1.mp4?token=NN85dAW6tvPCbTmVuPnct8Gvt4mNYt7BMxt1uUFeSrduPv8HhGNkV4hrfbqeRN5_Ms-KwF42w6n0TZ_jOM4ai6xBfU0iHe7sGOcJWXT1nSaocfsf1pEu1OlCLaSotO-CJU3ezTek6w-fB8YQ_rv25_4LW607vIo6xd-c6OmYrZ7dIvoS-Ci4SJpFBopujALXcVWEXokUAu_L88r2YDnEjR2CbfOO3f_XIS3v7eOnV1GGYf8LLZ95QR0UKNmSTckxjebE8Pt14dZmbyRLzqGspwbQW3uqJLb90t95nIX2hJhCk4heUkADujISMQTh0ejQGKTLo50ymJVy4y_rs1NWhS2lPuYhZXidD9kG9NWBuDyDUpKcPnLEPSjOMkS8xfeBNHJmqvWBkR7GYNN8ddvQc1dAnbDTlEtDFmcrzm3_MItD26sBPf3sd70-nEAJ5tG9hl7u3o75MvscAa7mFzbD0qhwv2IjWe7eXGNkK9NqcrRkK8RUwsi29OGq9DLTGbWOjjugsqlnIFNw_1c4-ZKiPodWXX8KzJl-CE2O9r7Xg8xhb8eff7nILkQy8QSIG0FrI6iTVYYyWUvrLd9MXisDpCZhQwNQ4PGu29kwPTE5g30aOCMPYsmjUbeBxBrrPi3yUoWpxkvHgRYuDQhWJt7S5a1KivQ9HQac4SZeQrNe7W4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebe69231f1.mp4?token=NN85dAW6tvPCbTmVuPnct8Gvt4mNYt7BMxt1uUFeSrduPv8HhGNkV4hrfbqeRN5_Ms-KwF42w6n0TZ_jOM4ai6xBfU0iHe7sGOcJWXT1nSaocfsf1pEu1OlCLaSotO-CJU3ezTek6w-fB8YQ_rv25_4LW607vIo6xd-c6OmYrZ7dIvoS-Ci4SJpFBopujALXcVWEXokUAu_L88r2YDnEjR2CbfOO3f_XIS3v7eOnV1GGYf8LLZ95QR0UKNmSTckxjebE8Pt14dZmbyRLzqGspwbQW3uqJLb90t95nIX2hJhCk4heUkADujISMQTh0ejQGKTLo50ymJVy4y_rs1NWhS2lPuYhZXidD9kG9NWBuDyDUpKcPnLEPSjOMkS8xfeBNHJmqvWBkR7GYNN8ddvQc1dAnbDTlEtDFmcrzm3_MItD26sBPf3sd70-nEAJ5tG9hl7u3o75MvscAa7mFzbD0qhwv2IjWe7eXGNkK9NqcrRkK8RUwsi29OGq9DLTGbWOjjugsqlnIFNw_1c4-ZKiPodWXX8KzJl-CE2O9r7Xg8xhb8eff7nILkQy8QSIG0FrI6iTVYYyWUvrLd9MXisDpCZhQwNQ4PGu29kwPTE5g30aOCMPYsmjUbeBxBrrPi3yUoWpxkvHgRYuDQhWJt7S5a1KivQ9HQac4SZeQrNe7W4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شگفتی خبرنگار اینترنشنال از شدت و دقت نفوذ سایبری ایران!
🔹
اردوان روزبه، خبرنگار تلویزیون تروریستی اینترنشنال: فقط در یک مورد در مینه‌سوتا دست‌کم ۳۰ مرکز آب‌وفاضلاب مورد حمله قرار گرفته و ۱۰۰ مرکز مرتبط با مسائل آب در آمریکا مورد حملات پی‌درپی قرار گرفته اند!
🔹
تأکید می‌شود در صورت ادامۀ این شرایط و تامین‌نشدن امنیت، می‌تواند این یک خطر بالقوه حساب شود، همان‌طوری که این هکرهای منتسب به جمهوری اسلامی دست‌کم ۴ روز یک نیروگاه برق را در انگستان از کار انداختند.
@Farsna</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/459872" target="_blank">📅 12:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459871">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دوباره دروغ ، دوباره فریب
🔹
اطلاعیۀ دفتر اطلاع‌رسانی حسن رحیم‌پور در پاسخ به تقلب جدید احمد زیدآبادی: فضای مجازی همچنان در هرج ومرج است و در این بازار سیاه خبرسازی، کلاهبرداران قلم به مزد از صنعت تهمت و توهین و تحریف ارتزاق می‌کنند.
🔹
نمونۀ جدید، نقل قول دروغ احمد زیدآبادی از آقای رحیم‌پور در مورد حجاب خانم شاغل در دولت (مهاجرانی) با جعل و تقطیع ویدیوی از چند سال قبل در فتنۀ ۱۴۰۱ است.
🔹
این شخص چندی پیش نیز  افترای دیگری به آقای رحیم‌پور زده و با وقاحت، به قاضی پروندۀ تعرض سلبریتی‌های سینما و ورزش به زنان توصیه کرده که به فتوای فقهی آقای رحیم‌پور حکم دهید که همه می‌توانند هر نوع رابطهٔ جنسی برقرار کنند و ایراد شرعی ندارد!
🔸
پیشتر نیز بارها کلاهبردارانی چون او و عبدالجواد موسوی و ...  در شبه رسانه‌هایی چون انتخاب، خبرآنلاین، شرق و .... با جعل یا تحریف سخنان رحیم‌پور و دیگرانی درجهت تشویش افکارعمومی و نشر اکاذیب کوشیده اند.
🔹
اما متاسفانه نظارتی در کار نیست و در کشور، تنها یک کس پاسخ‌گو است؛ جناب هیچ‌کس. خدانگهدار تا دروغ بعدی از قلم به مزد بعدی.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/459871" target="_blank">📅 11:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459870">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
پایگاه‌های آمریکا در امارات و کویت زیر آتش حملات موشکی و پهپادی ارتش
🔹
در انتقام خون پاک مردم بی‌گناه و دلاورمردان نیروهای مسلح، بامداد امروز، ارتش «سامانه‌های ارتباطات ماهواره‌ای»، «انبارهای تجهیزات» و «آشیانه هواپیماهای جنگنده» ارتش تروریستی آمریکا در پایگاه احمدالجابر کویت را با موشک‌ها‌ و پهپادهای انهدامی، مورد اصابت قرار داد.
🔹
این حملات، موجب ایجاد خسارات و آسیب به سامانه‌های ارتباطی و آشیانه جنگنده‌ها شد.
🔹
همچنین در ادامه این عملیات کوبنده، «محل‌ استقرار نیروها» و «سامانه‌های راداری» ارتش کودک‌کش آمریکا در پایگاه‌ المنهاد امارات، مورد هجوم موشک‌ها و پهپادهای ارتش قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/459870" target="_blank">📅 11:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459869">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b04d399aa.mp4?token=n6Kcq54-8P18Ig_MqxlzY-BvLyLhF1kiO9zpl-voyKqTio2sPcL7c_rwryCS5mE0RlzXOv-9iqdJjomIWtRBzh1GJvQ_PknDfNUfa1qPlDZKsDh7GOQOriZrRBG0_MwJM6xmvuh4hvskqlJM9zh5tmpmmWxcJofXaNTsfptzBb8l0z0Mgap7T6kLnZAfCrgsEmUxqeHekNAShRWyA_TBxb4pC1COz8S-iQi-X85QFAZK3RnGfPoorg_fhG9fgKkxZ0piffQOARBgHOHNXABfjQGp7Goi_JIoIKTLnsT8z31LXRDhjzeA294meBZad3pzno1Pe7Vfff8QSxQ6P7nGwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b04d399aa.mp4?token=n6Kcq54-8P18Ig_MqxlzY-BvLyLhF1kiO9zpl-voyKqTio2sPcL7c_rwryCS5mE0RlzXOv-9iqdJjomIWtRBzh1GJvQ_PknDfNUfa1qPlDZKsDh7GOQOriZrRBG0_MwJM6xmvuh4hvskqlJM9zh5tmpmmWxcJofXaNTsfptzBb8l0z0Mgap7T6kLnZAfCrgsEmUxqeHekNAShRWyA_TBxb4pC1COz8S-iQi-X85QFAZK3RnGfPoorg_fhG9fgKkxZ0piffQOARBgHOHNXABfjQGp7Goi_JIoIKTLnsT8z31LXRDhjzeA294meBZad3pzno1Pe7Vfff8QSxQ6P7nGwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس قوه‌قضائیه به هند رفت
🔹
اژه‌ای پیش از سفر به هند به‌منظور شرکت در اجلاس بریکس: این سفر در راستای امور مربوط به تجارت بین‌الملل انجام می‌شود.
🔹
ایران اسلامی و هند تمدن کهن و فرهنگ قدیمی دارند و می‌توانند در افول جهان یک‌صدا نقش موثر ایفا کنند.
🔹
نشست‌های دوجانبه یا چند جانبه با مقامات کشورها خواهیم داشت.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/459869" target="_blank">📅 11:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459868">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91845f6765.mp4?token=EGSYRcluxGNMj8Wl4CBNQ56jP0jYpRyEWJArE-1KzbkhzkvqjgEYN9qyWSVFsfwJBiYpsFGbildInkw9iMNTrBs6Bu5JpmBZI3xzud8p1MY96KpIrIXL6ZlIr2ZggxwtdHhEqeqHpuZf-itHcpDnnev1RyGRSb3XJPRDlUGjYeMBm8cxf6RwKdTaUpNWFV_drGr3uC8pW253ld_FpZz8J0h88qRYK6XH1WWPwzCYxh2mI34hvMljZ2kOpzAgUPjunpFCITar0EnCrF06-gnObe37O4OeiWHtRRZgzOW45EqlqmdPnEWuESXDZukJaAmVP7pZKii0GCWRJYAnF1bVQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91845f6765.mp4?token=EGSYRcluxGNMj8Wl4CBNQ56jP0jYpRyEWJArE-1KzbkhzkvqjgEYN9qyWSVFsfwJBiYpsFGbildInkw9iMNTrBs6Bu5JpmBZI3xzud8p1MY96KpIrIXL6ZlIr2ZggxwtdHhEqeqHpuZf-itHcpDnnev1RyGRSb3XJPRDlUGjYeMBm8cxf6RwKdTaUpNWFV_drGr3uC8pW253ld_FpZz8J0h88qRYK6XH1WWPwzCYxh2mI34hvMljZ2kOpzAgUPjunpFCITar0EnCrF06-gnObe37O4OeiWHtRRZgzOW45EqlqmdPnEWuESXDZukJaAmVP7pZKii0GCWRJYAnF1bVQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرمانده نیروی زمینی ارتش: هرجا منافع ایران ایجاب کند با قدرت حضور خواهیم داشت
🔹
یگان‌های نیروی زمینی ارتش آمادۀ مقابله و مواجهه با هرگونه تهدید احتمالی در مناطق مرزی هستند.
🔹
نیروی زمینی ارتش در مرزهای کشور ایستاده‌اند و در هر نقطه‌ای که امنیت و منافع ایران نیازمند حضور و دفاع باشد، با تمام توان در میدان خواهند بود.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/459868" target="_blank">📅 11:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459867">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دلار نفتیِ شهریور، وارد کشور شد
🔹
براساس اسناد رویت شده توسط خبرنگار فارس، از اول شهریور تا دیروز، بیش از یک میلیارد دلار نفتی به ذخایر ارزی کشور اضافه شد.
🔹
پیشتر در ۵ ‌ماهۀ اول سال هم رقم فروش نفت کشور، بیش از ۸۰ درصد درآمد بودجۀ سال ۱۴۰۵ را پوشش داده بود.
🔹
ارز نفتی تزریق شده در شهریور‌ماه با پر کردن دست بانک مرکزی امکان تامین نیازهای کشور را فراهم خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/459867" target="_blank">📅 10:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459866">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اعتراف شبکۀ اسرائیلی به پیوند گروه‌های تجزیه‌طلب با آمریکا و اسرائیل
🔹
شبکۀ ۱۳ اسرائیل اعتراف کرد موساد پیش از آغاز جنگ، طرحی با هدف براندازی جمهوری اسلامی طراحی کرده بود که یکی از محورهای آن، آموزش هزاران نیروی مسلح تجزیه طلب در سرزمین‌های اشغالی و آماده‌سازی آنها برای ورود به خاک ایران بود.
🔹
در این گزارش گفته شده که، این طرح سه روز پس از آغاز جنگ و در پی پیامی از سوی آمریکا متوقف شد و طرح جایگزین برای تغییر رئیس وقت موساد نیز به نتیجه نرسید. گزارش‌های دیگری نیز از رسانه‌های اسرائیلی و ایرانی، جزئیاتی مشابه درباره این طرح منتشر کرده‌اند.
🔹
این موضوع در حالی مطرح می‌شود که دونالد ترامپ، رئیس‌جمهور آمریکا، نیز پیش‌تر گفته بود واشنگتن در مقطعی تلاش کرده است به اغتشاشگران از طریق گروهک‌های تجزیه‌طلب کرد، سلاح برساند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/459866" target="_blank">📅 10:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459865">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3T4gLOhPmQ6-sodR_xuHyVSJvfxoXkT5bONYXpbQrt2aKESpiHKcAf-VtG_sc6Nomv3WWU1Cdhmh85K57Ypwcm77xJcZ9IAVE58iJhjGpvbXbWOi5r_LE4g_vYil3NsPDcz63LaRsKXejl6xa9l7q7Na2woSm61P4vDUFOPt0JZ8tORPTs-D8KifRdf8vn3zeNLwV3O_u10MkCh5fbsmuq3-Hu6esv36k0F3yTMwTvU0uP1CMDHVWV1Zr3elVWaNyqNR04s40Dia6IS3CPDgzvsZj55eYwUSCE9wmtVIbpRaz2xWiIiCzXsLvQl-D_idrWLnAPI4hRT9-F7R9IHYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توسعه مشارکت راهبردی ایرانسل و بهزیستی با پویش «همه حاضر»
🔸
مدیرعامل ایرانسل در آیین افتتاح پویش «همه حاضر» بیان کرد: چتر کشف استعداد، باید در دورترین روستاها و نقاط عشایری کشور گسترده شود.
🔸
ایرانسل، در ادامه همکاری‌های راهبردی با سازمان بهزیستی کشور و با هدف حمایت از عدالت آموزشی و فراهم‌سازی فرصت برابر تحصیل، به عنوان تنها حامی، در پویش ملی «همه حاضر» مشارکت کرد.
🔸
آیین افتتاح این پویش، ۱۱ شهریور، با حضور معاون وزیر و رئیس سازمان بهزیستی کشور و معاونان وی، مدیرعامل و جمعی از مدیران ایرانسل، مدیران سازمان‌های مردم‌نهاد، خبرنگاران و جمعی از دانش‌آموزان نخبه تحت پوشش بهزیستی، در ساختمان مرکزی سازمان بهزیستی کشور برگزار شد.
🔸
رئیس سازمان بهزیستی کشور با اشاره به همکاری‌های مشترک با ایرانسل، از جمله اجرای طرح «دانستان» و غربالگری سلامت روان، ابراز امیدواری کرد پویش «همه حاضر» با حضور ایرانسل، منجر به افزایش مشارکت مردم در حمایت از دانش‌آموزان تحت پوشش بهزیستی شود.
🔸
پویش «همه حاضر» تا ۱۵ مهر برگزار می‌شود و مشارکت در آن از طریق کد *123# امکان‌پذیر است.
👈
جزئیات بیشتر
📷
مشاهده گزارش تصویری
@irancellnews1</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/459865" target="_blank">📅 10:37 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459864">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-text">🎬
جشنواره ۷۵ ساعته آغاز شد!
🕒
✨
۷۵ سال تجربه؛ اعتماد و همراهی
✨
💠
هم‌اکنون وارد جشنواره بزرگ نئوبانک سپینو به مناسبت هفتاد و پنجمین سال آغاز فعالیت بانک صادرات ایران شوید:
🕰
۷۵ ساعت هیجان،
🎁
۷۵ جایزه ۷۵ میلیون تومانی!
❓
چگونه شانس خود را افزایش دهیم؟
🔴
دعوت از دوستان به سپینو
🔵
انجام تراکنش‌های روزمره با اپلیکیشن
🔴
افزایش مانده حساب و دریافت امتیاز بیشتر
🔹
خدمات نوین بانکی، در هر زمان و هر مکان؛
📲
«همه جا با سپینو»
⬅️
همین حالا با دریافت سپینو، وارد جشنواره شوید:
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331
#سپینو
#جشنواره
#نئو_بانک
#بانک_صادرات
#بانک_صادرات_ایران
#خدمات_نوین_بانکی</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farsna/459864" target="_blank">📅 10:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459863">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/459863" target="_blank">📅 10:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459862">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUxLSIyF8oLa41LUp87coCJTzzYX9sipEnkjRVU3jnTvmpRSndFe--fVjeyJ4ZMgCoP9nbD90Jyn_irspTee9gBhS1wmmWFoGk-CS-zW8bq1OHnSZaupr9IquTln5Tfd432Qwd4s7oJ2goH7yyJxZfLOSV6qvrCJIsL8GPYbrvWBSKaqTIgskHqZ1kQbP56Ve7uvrBj5uKDm7x88JnWtbe8Yj5QMOWAJJS5HHDPNIUbhCQWwnBY1Zx2B7x1fE80srPkNVAr_k2HAnJHuATQRGXZ94tgyuVDmT0Nu9joLkCrO_6cwx6C32Li9daxHJ9YrOxkewQ464n_WGE_vGNhpPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامۀ ایران به شورای امنیت: حملۀ آمریکا به مراسم عروسی، جنایت جنگی است
🔹
سفیر و کاردار ایران در سازمان ملل در نامه‌ای به شورای امنیت، حملۀ جنایتکارانه آمریکا به مراسم عروسی در هرمزگان را محکوم کرد و آن را مصداق جنایت جنگی و نقض آشکار حقوق بین‌الملل دانست.
@Farsna</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/459862" target="_blank">📅 10:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459861">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
سپاه: سران آمریکا راجع به پروندۀ سیاه حمله‌های خود به عروسی‌ها در کشورهای مختلف به افکار عمومی جهان پاسخ دهند
🔹
روابط‌عمومی سپاه پاسداران: ملت‌های آزادۀ جهان ملت قهرمان و حماسه‌آفرین ایران، فرماندهی تروریستی سنتکام ارتش آمریکا، در یک جنایت جنگی فراموش نشدنی با حمله مستقیم هوایی به مجلس جشن عقد یک خانواده شریف از اهالی کوهستک شهرستان سیریک، جشن مردم را به عزا مبدل کرد.
🔹
نیروهای تروریست آمریکایی نزدیک به ۷۰ نفر را مورد اصابت قرار دادند که ۴ نفر از آنان شهید شدند و حال ۷ نفر از زخمی ها وخیم گزارش شده است.
🔹
از شب گذشته در پی عکس‌العمل مردم و رسانه‌ها و شخصیت‌های آزاده جهان و حتی بعضی رسانه‌های آمریکایی نسبت به این رسوایی بزرگ، ارتش کودک‌کش و مقامات تبهکار آمریکا در بیانات و بیانیه‌های متعدد سعی در انکار تعمد در این جنایت دارند و ادعای مضحک خود مبنی‌بر عدم حمله به غیر نظامیان را تکرار می‌کنند. حال آنکه وحشی‌گری ارتش تروریستی آمریکا در این زمینه سابقه‌ای تکراری است و ننگ این جنایت از پیشانی سردمداران کاخ سفید پاک نخواهد شد.
🔹
امروز برای ملت‌های جهان احراز شده که حمله به غیر نظامیان برای ایجاد رعب و وحشت بخشی از دکترین ارتش ناجوانمرد آمریکاست:
🔹
۲۰۰۲ اول ژوئیه: بیش از ۱۰۰ شهید در بمباران عروسی روستای کاکرک ولایت ارزگان افغانستان
🔹
۲۰۰۳ هجدهم سپتامبر: بیش از ۵ کشته و مجروح بمباران عروسی شهر فلوجه عراق
🔹
۲۰۰۴ نوزده مه: ۴۲ شهید در بمباران عروسی روستای بکر الذیب استان انبار عراق
🔹
۲۰۰۴ هشتم اکتبر: ۱۳ شهید از جمله داماد در بمباران عروسی شهر فلوجه عراق
🔹
۲۰۰۸ ششم ژوئیه: ۴۷ شهید از جمله عروس در بمباران عروسی ده بالا ننگرهار افغانستان
🔹
۲۰۰۸ نوامبر: ۳۷ شهید از جمله ۲۳ کودک در بمباران عروسی وج بغتو قندهار افغانستان
🔹
۲۰۱۲ ژوئن: ۱۸ شهید از جمله ۹ کودک در بمباران عروسی لوگر افغانستان
🔹
۲۰۱۵ بیست و هشت سپتامبر: ۱۳۱ شهید زن و کودک در بمباران عروسی وحجه تعز یمن (ائتلاف تحت حمایت آمریکا)
🔹
۲۰۲۶ اول سپتامبر: ۷۰ شهید و مجروح در بمباران عروسی کوهستک سیریک هرمزگان ایران
🔹
سران آمریکا که به‌جای عذرخواهی بازهم به دروغ متوسل شده‌اند و همانند پرونده جنایت میناب، لامرد و قشم از پاسخ‌گویی طفره می‌روند، خوبست راجع به پرونده سیاه حمله‌های خود به عروسی‌ها در کشورهای مختلف هم به افکار عمومی جهان پاسخ دهند. آیا همه این حوادث اتفاقی و به اشتباه بوده است؟
🔹
ما که قدرت نظامی داریم و همان دیشب با به هلاکت رساندن تروریست‌های خونخوار سنتکام قصاص کردیم. ملت آمریکا اگر جلوی این ارتش وحشی کودک‌کش را نگیرند، باید از روزی بترسند که روز انتقام مظلومان فرابرسد که «یوم المظلوم علی‌الظالم اشد من یوم الظالم علی المظلوم»
@Farsna</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/459861" target="_blank">📅 10:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459859">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3TBt7MbjoUmTxyuQjZCWxqizFp4ISFj3cRhWStP6D6grj184inFH3IhefFrJLrIit6qmM0a3D31HsYTdcAVw69eM6Lm9s6eDXhBcRPLEbz616kFXZwknss5pPvy8CH_UXn5quMa1mBxIEJTbe2nWBxi-AJjXRh8XoC7Xh0CFuRaRpb5RIImSj-_je3B949-EQVAFzEVjPh-U0za2vNVJdmQZO53t_O1u0n4S1oWJ9Pwv_oSMH9YGiA5yKgvNYnN1QX7hB5C6u0T79kiAm1i2OMiQCwFdFVnOZeb3R6C7GV2RqWmwnst2Tj8En9XeQcpfAveOZCcqOLPOHAOOwaoDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a62b4aec2.mp4?token=IvYSUoZvb0TKeISikHsIpUD8K66uG_IJObFW1UEA4J3Y0hqRJkIQcYp4y3WjpIcbNHisIwljMrRoW-Yy1ll_lUgaVpWF1iUmIefzMOPRv1-nvQUci5ZZv484qhsN_phhna-4gH80eAba1S1s9MJdaF1QOgwilRf9dLMNzlM9y3DPaQCHPGtaLTs3sYJx7v-Tn_NNLQ48qDpDahKpM_3saz27_uPqJiSQbHKkeo827fGsZxN96aXSAsr1x_8PtDofYJ_s0zo9r9OdOmzzdO48Wr6ZQjYQ45QWYGqnrxxO3bYk11AYvPF0jdiDgoSHDgaoM1p-gicx1iFx0I77dCHeaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a62b4aec2.mp4?token=IvYSUoZvb0TKeISikHsIpUD8K66uG_IJObFW1UEA4J3Y0hqRJkIQcYp4y3WjpIcbNHisIwljMrRoW-Yy1ll_lUgaVpWF1iUmIefzMOPRv1-nvQUci5ZZv484qhsN_phhna-4gH80eAba1S1s9MJdaF1QOgwilRf9dLMNzlM9y3DPaQCHPGtaLTs3sYJx7v-Tn_NNLQ48qDpDahKpM_3saz27_uPqJiSQbHKkeo827fGsZxN96aXSAsr1x_8PtDofYJ_s0zo9r9OdOmzzdO48Wr6ZQjYQ45QWYGqnrxxO3bYk11AYvPF0jdiDgoSHDgaoM1p-gicx1iFx0I77dCHeaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نقدی بر یک شبه پارتی با ناظرانی راضی!
🔹
جشنواره و نمایشگاه تخصصی مد، لباس و فشن موسوم به «همای» درحالی در تبریز برگزار شد که فارغ از ابهامات مربوط به چرائی صدور مجوز و همچنین، ضرورت بررسی اهداف موسسۀ برگزارکنندۀ این رویداد، نفس حضور برخی مدیران دولت در آئین افتتاح این ایونت پرحاشیه، بیش از هر مسئلۀ دیگری خبرساز شده است!
🔹
حضور تعدادی از مدیران ارشد استانی در این مراسم که اتفاقا خود در زمرۀ ناظران و صادرکنندگان مجوز برگزاری این جشنواره نیز قرار دارند، از موضوعات بحث برانگیز رویداد به‌شمار می رود؛ حضوری که به نظر می‌رسد نه از باب نظارت بر رعایت استانداردهای قانونی، عرفی و نظارتی، که از منظر نظاره‌گری بر یک نمایشگاه شبه پارتی در فضایی رها شده و دور از استانداردهای زیست عفیفانه صورت گرفته است!
🔹
داستان برگزاری و حواشی برجای مانده از این ایونت زمانی رمزآلودتر می‌شود که مدیرکل فرهنگ و ارشاد اسلامی استان، به عنوان مسئول دبیرخانه کارگروه ساماندهی مد و لباس استان و ناظر قانونی که موظف به ساماندهی این حوزه، تولیدات و سیاست‌گذاری‌های تولید و تطبیق مد و لباس با موازین و الگوهای ایرانی، اسلامی است، مشتاقانه به تماشای رویدادی نشسته که در تضاد و تعارض با بخشی از ماموریت‌ها و محورهای نظارتی او در حوزه مد و لباس را بوده است!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/459859" target="_blank">📅 10:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459851">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sqTIAsNlZN7LsFjj-0OLGTntM02yPJPN-ZQ1Qsii5dpXRi-wcob9TD0kjmwW0bPy-9MUhTreJgxUAMEuZLCqk29PTUeU7H8ncl8ylUNHVF9Tzj2QRjwa72urPlcO7L946SK3SReQf52hY59tXKmw3WtnZdu5XBn2tjrq6_Yf2n35fzTdMQDINUh5p6LRQM7Wb_Eq4Ajf0avI_ufRSkGvgcJRiDIG1oGwpPaEOCKiDqcRQruM8zIlPwWh9GOTaEoNGhsHzzidionwyDmQbDTL9ciDe8GhpZd-djb-T08i-I3buCAudGE7Z4_2CnHrk1_9V5ARAFSgCivK0fgInl84tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hQjhPf0gC7cN06khMNKlsy7c4E927feXKRwuWrUIt7FfegWUeIzuYvz6qyQuAglwbZg4HjZG0GLKk1QOYxGLpWdw9-OjEXsghDPAFzneynGBiQX2Wc3FSNx0KjvDKWW7R7JMvZo9bVTUdAr5mWqlNzQyQ7yDRndqgWSzGrMBmNOZqyVLUTeb_WtDqqfqNF9tf_evZ_8EqkwORybTy4jzhZWOqGbJOWNqcLz-cO-RHjLBamQ5WB2Y2PJHiFQRncX1lyqH1RWstopnJbXbpxQZd5WCligjWosPquf34TbChMEZ1TmtQzXmFqCot7s3P1UTKZGe7VXvyCMFcLiUTal0hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K7Z58i5mM19B2CowK0SNB4UYVrKS6XH6kgtFATnGJ8ZHHvZb6khupHLyh5tUAFoNkNdWySZxAz_biMNuB5gMPNULbZ-zryT8lOsPqTZOXwr7sJUhTXSGaQN7o9SLtL4RX3IrihZMQSpQZmi_B7A72VLe6Y7VH-4YJjb3EqJBE9_6HPpQJucFIS7rUmhCSdIMYXwfZg3VNsKtxez7Szf5zVljAsY_Vjit3sCgoQySAuumqZ0_zfMG-w4TlTxmux9rZDnorRYRWZnCx9mUbUaTSrY3ZWYi8v8Y3zmcyILAIwZLnsh5Rq7i47_whjEk1FPsyxu-YeGeXR0BkrK5MCnUFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eyeF983BwS8HxoiqB1d7L2bNPszpwLO2Obmh3U7WxmpSrjcLyD9IxGwLT0jzbiiqem2MYG8_WczVpNUOra59-NsCk470_aFpwMMqnskXrlx9boLirgGzreKRp6Eg6Y-31xW6555VeO3eN7BGsHkh3f-YNpEV7dVZfR9J8oAYmYKrNOyg5d0KJmOtRIOFy0f2cIB-XOtTy579qSWTshndzFh0M8ovgoTS12cyeQn-f3EuvbgpGep2FjcbtnLGI1U6eppRVfmxxfI3Yz1ztn5ev2JrCW6oc0TSu9uqMIoM1ZPXmZ8G3ieRo1R04Jlyq0FqseFyOdRSxaGWgE1MHVOGDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C8DM4gqlSnbvvJlC39B-TYURITlTG8uFj71ixVNDNnOa4SipoKeuCNnxEapMP8h3HBNj7O_rnCaqIK1RDTzIPJk0wmAbbDiWtB6Zvu-J2_0u8jaSbb7Jy-sdRWoFFhug3T7ErIOhlZU-AkZLu2va59LHY9798EMvJzTlMdymIFiPeXPyA72Jv9lc304YeTSzeADogtZrs3OKAoHgG1wJZ-wkQEEAgm42_18KjbY8bcopHxmdU4eNwU4WpOnD581LdrPH5_-T1lJwmUo66eH0mlYFojhcJXdgL-uuBq9SqaODT65aTXAG2llQg4tWGTwGoo7xypeElukLKcPBlTaXAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qToy0SGW3bj2T4SPh4-_5UfyyyiEVnmx1fSg3a2Swh7qSQaaqrvCIHWrq090aC_dqqRd4xkP0Z_dDo3fNGsagO5hiIxYkKZ2sm5eD8Y8h5ZHJcUH50uu7xH3h-raRXqTqDugh1sBPrTrLAqVlItOMHOXj8UMD6etQU50lC0TmqM-xdc4eEYMaoQy_xpvDV2Yw5jSdhEPpq0nqJOnZhrMI49WYm97oSpWaRIM2qxnaKY-7FDHM62OCF2UhTARbEoGglJLpjSGzbyO9GI5bEVBUaNxtU2-22ZaxEjlzUmEUVWoZJ-9cZIN225Tn_J_zAXF-ZvcAcS6ekTeZpEJ5eia6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ti9nkLut1T4eb1pT0YLFdF-GjlC2WdSNznU9i9-vreWmoS8SsrNeZ6Yzg0nS0vBt9ZYduTl-51kP-HuzSmCEyut40cF7T-hAf5ABjxBmy8IQnLF0j5H67VjoXuVqEi8vtcDB2JMH5u_AOsQ0YRzr_pgLVfelxflMCGBGz1tn_pa0W9FgM80lhKD3PRUFV55myshU0ZKZW3AM3MJU_SJ8RdZES6I0FbMQsKDQoGl8xt2T9LA8FbOpzNOFFt10M-EyZ3LlKzGKiXeOXof56h8Ob6X2QlLxWHjf_8VieFND9-4DvAx0FMp_JKTOn2hGkRXMfEv2_g5JTlCrS1ieWiARmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
افتتاح «دنیای گمشده» بزرگ‌ترین تم‌پارک ایران
🔹
آیین افتتاح بزرگ‌ترین و مدرن‌ترین تم پارک ایران با حضور مسئولان شهری در مجموعه ارم برگزار شد.
عکس:
میثم نهاوندی
@Farsna</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/459851" target="_blank">📅 09:54 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459850">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNgF6308hq5WzBzogjL6jhIAGpJm1VEJdnsvECDePVWiKrytm0vmtetc4b_5i-_2e8UnNwzh-HHaviZbrB6qS8ewd6Uiko88UnaB9Ci2AtQ8XudXOCj6vOCz2l15WP-ZwXhl4fP83xXoj3fJQ8czBqQx63ZKtyigcZGj7mT6vJYa8MhwnL6U8ZQcNYIFiEgcQftviLk6BJ7zxjVDC45-nk9HNGhikO3_5Cx47vEHtEpoB5xuaKo-MuaTn9GR5ZuiHS7kMjYteN-JT3c9xAd8toEdTgzOOJD-XOmAfbeybtSJfTzyHXS_ye1uRNbBVq7ZlZ3AOR_OHtvVmMsEu_BYTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت‌نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار وتولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی.
🔹
ظرفیت محدود است.
مرکز آموزش علمی کاربردی خبرگزاری فارس</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/459850" target="_blank">📅 09:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459849">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">بلوکه‌کردن بخشی از تسهیلات اعطایی به‌عنوان ضمانت ممنوع است
🔹
بانک‌مرکزی: با رای هیئت عمومی دیوان عدالت اداری، بلوکه‌کردن تسهیلات اعطایی توسط بانک‌ها و مؤسسات اعتباری غیربانکی و یا اجبار و الزام تسهیلات گیرنده به افتتاح حساب نقدی و توثیق آن و سپس پرداخت تسهیلات، ممنوع است.
🔹
اما چنان‌چه خود تسهیلات‌گیرنده در راستای قانون، آزادانه به معرفی حساب نقدی و یا سپردۀ نقدی خودش برای وثیقۀ تسهیلات اقدام کند، امکان‌پذیر است.
@Farsna</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farsna/459849" target="_blank">📅 09:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459848">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: رأی مصادره اموال ساعدی‌نیا جهت فرجام‌خواهی به دیوان عالی کشور ارسال شد
🔹
براساس رأی صادره، تمام اموال منقول و غیرمنقول ساعدی‌نیا مشمول مصادره قرار گرفته است؛ شایعات رفع پلمب برخی کافه‌های متعلق به متهم صحت ندارد.
🔹
تا زمان بررسی فرجام‌خواهی…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/459848" target="_blank">📅 09:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459847">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e89075fa.mp4?token=JIcnkPanLVLViaqj0nySWR0A6htwcLXcL-FT3yrNZ1kVWUyOf3UdrpAuDwwRWOgHfEfy7RxCtX3nG8bITkBWij4ZFgVuiQMMSM-VmxN_xuEiUW-93iS1pCwi6r3SJuIQF5MmORinl8fokV1IT_AEcUH8_oMCNYA9Ln_5Wxwoek-_pDHlsAFfKRIExwyodiRo6AfGl1C-cmKQ4Hv73EJS3xfFmOmBEg1Ta5jYY9hKA-ikx5mhxExhPp9T5W0_NopsNflGYmsMwMiTgDvCHicYbn2px_SVq6zhqbT5EjPnOl997yya87YP_tvNwxY8q12ttp6AX5lw_VZxbG_JwQziCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e89075fa.mp4?token=JIcnkPanLVLViaqj0nySWR0A6htwcLXcL-FT3yrNZ1kVWUyOf3UdrpAuDwwRWOgHfEfy7RxCtX3nG8bITkBWij4ZFgVuiQMMSM-VmxN_xuEiUW-93iS1pCwi6r3SJuIQF5MmORinl8fokV1IT_AEcUH8_oMCNYA9Ln_5Wxwoek-_pDHlsAFfKRIExwyodiRo6AfGl1C-cmKQ4Hv73EJS3xfFmOmBEg1Ta5jYY9hKA-ikx5mhxExhPp9T5W0_NopsNflGYmsMwMiTgDvCHicYbn2px_SVq6zhqbT5EjPnOl997yya87YP_tvNwxY8q12ttp6AX5lw_VZxbG_JwQziCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سهم ۱۰ درصدی طارم سفلی قزوین از صادرات مس ایران
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/459847" target="_blank">📅 08:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459846">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcc75ff65f.mp4?token=FFRIAtf9UU0YYLJ07d-Cp349pFH5yMxxHBq5HuViYdIuajU1Keri4Vq0Dhs-7ilCB0N8eI_0zTGpyrsgFth5EoKHDaFGaJEPCr0B8H7gac__Ng76M21pISGbITBaEgdXcZ_hm6DpTDp4FTMiso7cJ897JZSg35wD7nZ7oSyunPzGnBc1TqR0aAwuSOyg7RV9lEHRUpA_yt6dNA4FgCFw-czPddXKA2epCcpBLUxXMnsYKAiplgnEbf4r7RfOXWFKdsXz6jwjFcRbAv_ZyTD0qEpY11pvY3En1GVuid_InfhDMLcJRLgoD4o2VDBjpQWQtSvRbaOct-kyJBVEZGgiow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcc75ff65f.mp4?token=FFRIAtf9UU0YYLJ07d-Cp349pFH5yMxxHBq5HuViYdIuajU1Keri4Vq0Dhs-7ilCB0N8eI_0zTGpyrsgFth5EoKHDaFGaJEPCr0B8H7gac__Ng76M21pISGbITBaEgdXcZ_hm6DpTDp4FTMiso7cJ897JZSg35wD7nZ7oSyunPzGnBc1TqR0aAwuSOyg7RV9lEHRUpA_yt6dNA4FgCFw-czPddXKA2epCcpBLUxXMnsYKAiplgnEbf4r7RfOXWFKdsXz6jwjFcRbAv_ZyTD0qEpY11pvY3En1GVuid_InfhDMLcJRLgoD4o2VDBjpQWQtSvRbaOct-kyJBVEZGgiow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک عکس، یک تخفیف وسوسه‌کننده
🔹
پلیس فتا: کاربران موقع خرید مراقب صفحات و کانال‌های فروش محصولات قسطی باشند و پیش از اقدام به خرید اصالت و اعتبار آنها را بسنجند.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/459846" target="_blank">📅 08:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459845">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtMy2icDpPKvvOas4YuRM17H0cVRxrdxrcg2gBQHytgAIT9Ktyh6Q6kW8OqB5t9tKbtpl1htW1Ywib-oEtcXToifLPA3-ONxxCQ3BAcriqha9mA5eolfm11DjDtpDbKauGQBSAwIfLBmW1AnmRZGh7ZraWFmNLMk2bv6z87Rk7VCeIfV4K0XJ03nrOPmPs50A5ab_x60l-wpBtca8CIsdpFDnF8Cdux-Hh6GwlNMIG0YCVomvm-9A1lPqaMpFGh0LzJ3CJ9jiQPMKoGomfIHBEfEAV9MDcqevziRpDV_GGy6lK3tkIkUdK1uUloUfH4RBWa_bLcl9lcpbGb_wimG-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی در مدارس نیویورک ممنوع شد
🔹
زهران ممدانی، شهردار نیویورک، در آستانۀ آغاز سال تحصیلی جدید تصمیم گرفته استفاده دانش‌آموزان از بسیاری از ابزارهای هوش مصنوعی را در مدارس ابتدایی و دورۀ متوسطه اول محدود کند.
🔹
این ممنوعیت دانش‌آموزان تا پایان پایۀ هشتم را دربر می‌گیرد و حدود ۶۰۰ هزار نفر را تحت تأثیر قرار خواهد داد.
🔹
هدف اعلام‌شده این است که مدارس در این مدت فرصت داشته باشند تأثیر استفاده از هوش مصنوعی بر فرایند یادگیری را بررسی، و چارچوب مشخص‌تری برای استفاده از این فناوری ایجاد کنند.
🔹
البته معلمان همچنان اجازه دارند از این فناوری برای برخی فعالیت‌های کاری مانند برنامه‌ریزی آموزشی و مدیریت امور کلاس استفاده کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/459845" target="_blank">📅 07:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459844">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">هوای تهران ناسالم شد
🔹
شاخص کیفیت هوای امروز پایتخت روی عدد ۱۱۸ و در وضعیت ناسالم برای گروه‌های حساس قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/459844" target="_blank">📅 07:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459843">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qA6AOEl_esaA6Y8kNNtG2dlr0UUjjPtV1tdIO_bZJcEdMVbigSYVX7aaGDvGDA1NQDL7VCQe417XIMlDNzjbJgOSjmKJi3qb4tOc8bJ0pabfgsDXXfCFT6e_apA2imCzF6BwixBYxw-hGMeo3Yv-bVsyfa2oDZtrGucSMG6jTJAlUttColw1wU_gyrXRccT3TR0G__W1e_l4fyQd1wL4fvFMg9e2pT2ExcxRwtFRVNqr1CLy-2Dxr6Lz_-ChdLrWth-kLJr3i6baKMyGhhCHkPHaCd3zgqprAtwk4-sHfY7PdFT1nU-qn__pyDpvnuArBprY3J9vW0U8L5EXKzpbsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: تا من هستم، اسرائیل نگران نباشد
🔹
رئیس‌جمهور تروریست آمریکا: اسرائیل نباید نگران باشد. می‌دانید چرا؟ چون من رئیس‌جمهور هستم و از اسرائیل مراقبت خواهم کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/459843" target="_blank">📅 03:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459842">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b03c35f5b7.mp4?token=CTjvFt9-ledaOa50sdqwDrtlcpPx85G9YqqrzVL_tfZAQfoghgZs6rd0XhJj0Cdy1f6rs60uA2NJ0aFxMO-Z9NBZ3xVDCblziwP4iJtGVuO_DKujjyDZz6vHgiLXWgJhnZlD4JlieKHu2AvEkHGyD3zDbA30xdBLEapMGCtNR04xy_3daf_gjLsN-6f8rupCCstZvVqVa7iAECQ9LNyMaf3V9FxgedzgySHpT2euqDwHKxVa7vVL5CpXP1iifcCrukKnY8PBJ_m87DelaYeYDLdwyAKMxai5-BxwdyXm2eEnf31oqnWxaMhLreGDLsD4uPzari675vkj6QUOte9LCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b03c35f5b7.mp4?token=CTjvFt9-ledaOa50sdqwDrtlcpPx85G9YqqrzVL_tfZAQfoghgZs6rd0XhJj0Cdy1f6rs60uA2NJ0aFxMO-Z9NBZ3xVDCblziwP4iJtGVuO_DKujjyDZz6vHgiLXWgJhnZlD4JlieKHu2AvEkHGyD3zDbA30xdBLEapMGCtNR04xy_3daf_gjLsN-6f8rupCCstZvVqVa7iAECQ9LNyMaf3V9FxgedzgySHpT2euqDwHKxVa7vVL5CpXP1iifcCrukKnY8PBJ_m87DelaYeYDLdwyAKMxai5-BxwdyXm2eEnf31oqnWxaMhLreGDLsD4uPzari675vkj6QUOte9LCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دلیل بسیاری از شکست‌های زندگی
🎙
آیت‌الله جاودان
@FarsMaaref
-
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/459842" target="_blank">📅 02:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459841">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJ5yxIf-svBIkW9o5dAdUZn8ZBWvVPoTurbGX_wjt1pmiY1EHW-K5qWCGOFqd0cwv8IgHWKl8dnbri17P5lwCtwSmEkHbbePQGsob-O27Cty5PRPxyv9KOcW2FrJByEW8tYAYrryXh8p3vHpbOjj4CDz5SmmSDXMHOah9ens3FHSUeOfGsESDYDiNHWQexrMiX7lTYczx9basI11jg_KEgMlOskLq6krYac8CneoIdC-V4-ueapATAI1jCUqUvC_fJ2y4FOS6ZMgEAfDs2HtUjPW4QiCTyX23Bx3vFxBZR0nzKdGfnLDALVTeAeqOzTRYATHUdqP7ghlU3mhcnUr4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی وزارت بهداشت: از ساعت ۲۰:۳۰ روز ۸ شهریور تا ساعت ۲۰:۳۰ روز ۱۱ شهریور، در پی حملات دشمن ۱۴۲ نفر مصدوم و ۱۸ نفر به شهادت رسیده‌اند.
🔹
از میان مصدومان، ۶۱ زن و ۴۴ نفر زیر ۱۸ سال بوده‌ و در میان شهدا نیز ۲ زن و یک کودک دیده‌می‌شوند.
@Farsna</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/459841" target="_blank">📅 02:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459840">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOkPysROHjRgh8yb_vCHsAbVTGbfEgwqLMa0G5VYTaomC_uHbmJgcIT9BUotNIf7I4NsGX7tO3hO-4gaFawfY9w53nZShIA2xJlnNmqCrG6glFmfzoIwkQkyHFkpbrC6yFncQ0HTi53nKDj1egwMT3JbYG-vBd3YVADqjN0U1iEpl9zcOU2OypLVNN04NPmyhqolplLcYS_aKxhvTISNWWTCuq4BC5fiaeG-cg6Sx60FLk1HKp9szkKsJh7l8tent6Ish3ydtfr3fiAeiHrH0STgpAGsF_vYZjc8ugusuNHyczcUbklqbpZeHZYYSp0NPDiKIZ6Nwb2TynjMW2XNwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ثبت پایین‌ترین سطح صادرات نفت سعودی در ۹ سال اخیر
🔹
خبرگزاری آمریکایی بلومبرگ: صادرات نفت خام عربستان سعودی در ماه آگوست به پایین‌ترین سطح خود در حداقل ۹ سال گذشته رسیده است.
🔹
حملات به کشتی‌های سعودی در دریای سرخ، محموله‌های این کشور را از طریق مسیری که در طول جنگ برای دور زدن تنگۀ هرمز استفاده می‌کرد، تهدید کرده است.
🔹
بی‌میلی به استفاده از بنادر دریای سرخ عربستان سعودی، ریاض را مجبور به جستجوی مسیرهای دریایی جایگزین برای دور زدن آفریقا کرده است.
🔹
کاهش صادرات نفت عربستان سعودی نشان دهندۀ یک شکست برای این کشور است.
🔸
همچنین شرکت سعودی نفت «آرامکو» از پاسخ به سوال بلومبرگ درمورد آمار صادرات خودداری کرد و وزارت انرژی ریاض نیز در این‌باره اظهار نظر نکرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/459840" target="_blank">📅 02:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459839">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e2093db70.mp4?token=oUCs-8zKgqZDXtobLjru0iXJ0_-5Bx9CRQ8HMlGvR2KBpPZwgV6YGDiyjLcjRtnqX4NI1oMJpjzbg2_S7JVVhO8OOYIQr_TsB2ker1v4C6KG0dWPIezcPA42tJxL0QQ8A8hL7uK3X-AiaDKG0jByO_mpFYoqJPkcf1muHBn2E3GBbgkCwRVZsG3SbQU8kDxxJl_RnX3lCD4rZc_3CNl3qobkXCr_--jRKdhBoa0ZMA7i5bN1lAwXl8A4q0wPaCRvKi3MJaB4XBgim98T9TD7uwzdzdmSpNiaD3-SZmbbEVkXK0ybYaZcBi1FkwEmUsKx3TpNk0mt4VzD-fLSpGvF1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e2093db70.mp4?token=oUCs-8zKgqZDXtobLjru0iXJ0_-5Bx9CRQ8HMlGvR2KBpPZwgV6YGDiyjLcjRtnqX4NI1oMJpjzbg2_S7JVVhO8OOYIQr_TsB2ker1v4C6KG0dWPIezcPA42tJxL0QQ8A8hL7uK3X-AiaDKG0jByO_mpFYoqJPkcf1muHBn2E3GBbgkCwRVZsG3SbQU8kDxxJl_RnX3lCD4rZc_3CNl3qobkXCr_--jRKdhBoa0ZMA7i5bN1lAwXl8A4q0wPaCRvKi3MJaB4XBgim98T9TD7uwzdzdmSpNiaD3-SZmbbEVkXK0ybYaZcBi1FkwEmUsKx3TpNk0mt4VzD-fLSpGvF1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شور خون‌خواهی قمی‌ها به شب ۱۸۶ رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/459839" target="_blank">📅 01:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459838">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a820bfc659.mp4?token=AkIglIyKx_v96cvaetnfEwMVqBrs1YignukLOxN56sebAO8ifSu5IXpwO6tMun_8jw3XwkBpzAQtt7IkzjByI5GwYlnJzOT3zL0-5vicj1XJcGe3pf3kUDLdhx72jMNWkftme5D-VidV5CMYEHRBgcGnxZshS0BmZLS7E8yTx8HIOi5uoPETH1LTzHRpiRIx4sPa_IpI2UXWsXwdZHayyFKM0V0A6VC23xUU7lUHay2Lkj-XW4xVYhB2LB_m0YNTlEhfxMx81Rn07X8Lyq2tEc1OMphu6csTwvrLvWciO6eS-1t-6HJjm_6P2bkUV-pHp4fbxftEfnNrVjpvyUp3bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a820bfc659.mp4?token=AkIglIyKx_v96cvaetnfEwMVqBrs1YignukLOxN56sebAO8ifSu5IXpwO6tMun_8jw3XwkBpzAQtt7IkzjByI5GwYlnJzOT3zL0-5vicj1XJcGe3pf3kUDLdhx72jMNWkftme5D-VidV5CMYEHRBgcGnxZshS0BmZLS7E8yTx8HIOi5uoPETH1LTzHRpiRIx4sPa_IpI2UXWsXwdZHayyFKM0V0A6VC23xUU7lUHay2Lkj-XW4xVYhB2LB_m0YNTlEhfxMx81Rn07X8Lyq2tEc1OMphu6csTwvrLvWciO6eS-1t-6HJjm_6P2bkUV-pHp4fbxftEfnNrVjpvyUp3bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ما به انتقام خون کودکانمان حساس‌تریم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/459838" target="_blank">📅 01:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459837">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تداوم حملات صهیونیست‌ها به جنوب لبنان
🔹
المیادین: ارتش اشغالگر رژیم صهیونیستی بمباران بزرگی را در شهرک کفر تبنیت در منطقۀ نبطیه انجام داد.
@Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/459837" target="_blank">📅 01:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459836">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2NqtFXaV_Xib1tZFfxtpphs5Kxqesc2bn8pyBAaFxnWTF3T2wWpR5mx1ipAAWNUeKScawi3PTCIKeaqYAELS908LBHS7jz0sZxJLmzfkBul4jPYpEq3YPTX8RHpmX9UInIAJywQZkID90yI56bKqsTmeJctCvpq92CwFduT31wKWvHnt7_el0PT_rxvKCYLsdILfWTgBw3xyS2ZdaGalYuV4KQuYO1N3R0pVDXxJtyo2D8GzPnL6Q5KKKAfGbyDT0K8hz9uR-aAG4ooGbAguwoS-bZTr7lYQwpQsCK6SDORAO-ng-aSk4GaCnDYJP61bbwJOGZ8txZ9BGL0CmDzsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نصیحت زاهد
🔹
محمد بن منکدر، از عابدان مدینه، امام باقر(ع) را در هوای گرم تابستان درحال کار کشاورزی دید.
🔹
او با خود گفت که چرا امامی با این مقام خود را برای دنیا به زحمت می‌اندازد؟ تصمیم گرفت برای امر به معروف و نصیحت، نزد امام برود.
🔹
محمد به امام نزدیک شد، سلام کرد و گفت: «اگر در این حالت مرگ به سراغ شما بیاید، چه پاسخ خواهید داد؟»
🔹
امام باقر(ع) دست از کار کشیدند و فرمودند: «اگر مرگ در این حال به سراغ من بیاید، درحال اطاعت از خدا مرا یافته است؛ زیرا کار می‌کنم تا محتاج دست مردم و امثال تو نباشم. از مرگ زمانی باید ترسید که انسان درحال معصیت و گناه باشد.»
🔹
محمد بن منکدر با شنیدن این سخن متوجه اشتباه خود شد و اعتراف کرد که می‌خواسته امام را پند دهد، اما خودش پند گرفته است.
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/459836" target="_blank">📅 00:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459835">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5199508d6.mp4?token=G1Emqv9M48yOFWfmv5kQKeBRCGo7S7PfxBGe-V2cvmDEnhs-q57mPVWi4AsL_U0tKzKkrLMR1YXkM7PlkIvwDI9IAAc25dj7L118ZoicAOedhQoxhoLcM92KFPavUSmMW5NuH4-LEH4Fmm1L6QDvy60GyBfAdH4ES5UdON4EhmhR3yBcbTj_y0cCK-DxylemX9dKzt1IqlwMJtnTAlX3oj4YVcp3bUskwiw1GlnkSSGxm8B7SVumpjEWbsjtLITYE_KRUQ51F-gjZV2-9AuqqUqIScD7afmimlBKwNHdQO48THgGJWzfd5RKVvqtYHquSicH7iSRiczOJqXBtO-qcIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5199508d6.mp4?token=G1Emqv9M48yOFWfmv5kQKeBRCGo7S7PfxBGe-V2cvmDEnhs-q57mPVWi4AsL_U0tKzKkrLMR1YXkM7PlkIvwDI9IAAc25dj7L118ZoicAOedhQoxhoLcM92KFPavUSmMW5NuH4-LEH4Fmm1L6QDvy60GyBfAdH4ES5UdON4EhmhR3yBcbTj_y0cCK-DxylemX9dKzt1IqlwMJtnTAlX3oj4YVcp3bUskwiw1GlnkSSGxm8B7SVumpjEWbsjtLITYE_KRUQ51F-gjZV2-9AuqqUqIScD7afmimlBKwNHdQO48THgGJWzfd5RKVvqtYHquSicH7iSRiczOJqXBtO-qcIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوجوان پیشوایی: ترامپ، حریفت منم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/459835" target="_blank">📅 00:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459834">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28e5acd944.mp4?token=ohaxrMN9tP5jQ_JB1P8aXdNo8hGy6HihHTuRI5wyK3nOkqslzpbJr_kSiRtRSTivyhCJtTH1Wa1UbtDFw04zTRCF7CkTd_etPBYRtwkKZDuBcZJqMvTkS6IXw-0hZ4HBndaqFfZP7b7PgDIW1unFuNlByu0uP5JHdVgVS0ADr5p2AWj3rAzvMr-WqyOa5PZKf_pNrGTX8lWaqT3P7PBW-zhpVbLGdcKzDFYF7AfEa3tenEQQni7qEIjUKEHSvFA_fzlloADGnK8lfE6e8hCNjdmHJXmJoihCLYdZa1Ren_8Ikn64K_3X7epRgb_dx0DQGE7IdrsiOoD0hvIz_U6aQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28e5acd944.mp4?token=ohaxrMN9tP5jQ_JB1P8aXdNo8hGy6HihHTuRI5wyK3nOkqslzpbJr_kSiRtRSTivyhCJtTH1Wa1UbtDFw04zTRCF7CkTd_etPBYRtwkKZDuBcZJqMvTkS6IXw-0hZ4HBndaqFfZP7b7PgDIW1unFuNlByu0uP5JHdVgVS0ADr5p2AWj3rAzvMr-WqyOa5PZKf_pNrGTX8lWaqT3P7PBW-zhpVbLGdcKzDFYF7AfEa3tenEQQni7qEIjUKEHSvFA_fzlloADGnK8lfE6e8hCNjdmHJXmJoihCLYdZa1Ren_8Ikn64K_3X7epRgb_dx0DQGE7IdrsiOoD0hvIz_U6aQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم نیشابور ۱۸۶ شب پای ایران ایستاده‌اند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/459834" target="_blank">📅 00:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459833">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flZTVQA-5zQ_y4X5zvByU2AOhFGH2LoDVcdSbFBDJcEGQapafESMM_1yrXkEzTNachYcDOqdnMVYWjLM7w__FZRD42uXbf5yDsbHfB9wY4G4QqCeFpAhpo4octsgZ2wvyd6SabfdLt5kAJxLw50q4mEiEapkd7z39uYjXAaWFXOjKU7o-jioVH2efboRHlvVHgzL4MZMVtqjCp1yRjuj-jBYwL_oLMIfMAYG1KhB8BB8_IfWgeAA_6gf-_iMTwFn56ozUzB3_xL7NPC_Fe49Sov04d8z-Y2URD7RY0tc0WrwPATHIuTgEkTKlFlkUWIiHfZmhgeW6OjvjjBhYs2m5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راز پنهان پشت تاریخ‌های دونفره!
🔹
دردنیای پرمشغلهٔ امروز که همه درگیر کارهای روزمره، استرس‌ها و تکنولوژی هستند، اختصاص‌دادن بخشی از حافظه (و زمان) به یک تاریخ خاص، نشان‌دهنده این است که شما عمداً برای «رابطه» فضا باز کرده‌اید. این کار به طرف مقابل حس امنیت و دیده‌شدن می‌دهد.
🔹
هر تاریخ مهم، در واقع یک «نقطه عطف» است. یادآوری این تاریخ‌ها فقط مرور تقویم نیست؛ بلکه فرصتی است تا زوجین در کنار هم بنشینند و بگویند: «یادت هست آن روز چقدر هیجان داشتیم؟» یا «چقدر مسیر را با هم خوب طی کردیم؟».
🔹
زندگی مشترک به‌مرور زمان ممکن است به سمت یکنواختی برود. مناسبت‌ها و یادآوری تاریخ‌ها، مانند «وقفه» یا «نقطه تنفس» عمل می‌کنند. این روزها به رابطه هیجان تزریق می‌کنند، فضای رمانتیک را بازسازی می‌کنند و به‌نوعی به رابطه «رنگ و لعاب» می‌دهند.
🔹
عدم توجه به مناسبت‌ها، گاهی (نه همیشه) به مرور زمان این تصور را ایجاد می‌کند که رابطه برای فرد «عادی» یا «کم‌اهمیت» شده است. این «بی‌تفاوتیِ ظاهری» می‌تواند منشأ سوءتفاهم‌های بزرگ باشد.
🔹
کیفیت مهم‌تر از کمیت است: لازم نیست حتماً هدیه‌های گران‌قیمت یا جشن‌های بزرگ بگیرید. گاهی یک یادداشت ساده، یک شام دونفره یا حتی یک پیام صمیمانه که بگوید «یادم هست آن روز چقدر برایم خاص بود»، بسیار اثرگذارتر است.
🔹
اگر همسر شما تاریخ‌ها را فراموش می‌کند، فوراً آن را به‌حساب «عدم دوست‌داشتن» نگذارید. گاهی مدل ذهنی افراد متفاوت است. به‌جای سرزنش، می‌توانید با هم توافق کنید که این تاریخ‌ها برایتان مهم هستند و از او بخواهید در این مسیر به شما کمک کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/459833" target="_blank">📅 23:59 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459832">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfEJMpRxjrXyqybkNclKccSCOW1wPOl_Cq8u87hLzm96H5R5T1g7rfk07U8q2DqIOdFQQw4YyGIjqI4HiGSMgP-TyFmFI7MwYmLsdF8BHC8s6CtlSkA-IoBEvaNVNq8bJ-mq7kWdDQMN5sK9LnsCJMSiVtNpBEw7CqFB5PU0vI8CRd8KAoIoKrY3cxwQjQdCxrwDTLiD92Ne3ZRUow8yFRzF8_nZS7IZXuE8euNScrRDeihd8Mq-QmUAZW_r1bYTFoWKJD4R6o3TjYJ7Ye7p7M45Ty9Pbw24OQsgM_7qDwOH7YF0yPR3HSyeKRHw9BRacRr9ueJSaahFT1HfKEBZzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریل ترکیه بدون ایران به قفقاز برگشت
🔹
ترکیه بازسازی خط ریلی منتهی به مرز ارمنستان را آغاز کرده؛ مسیری که پس از ۳ دهه قطع ارتباط، بار دیگر قفقاز را به آناتولی متصل می‌کند و مکمل کریدورهای میانی و زنگزور است.
🔹
پس از فروپاشی شوروی، ارمنستان و آذربایجان بر سر منطقهٔ قره‌باغ دچار اختلاف شدند. در سال ۱۹۹۳، نیروهای ارمنی کنترل منطقه کلبجر در خاک آذربایجان را به دست گرفتند و ترکیه که در این درگیری‌ها از باکو حمایت می‌کرد، مرزهای خود را با ارمنستان به طور کامل بست.
🔹
در نتیجه، ارتباطات مستقیم جاده‌ای و ریلی میان ۲ کشور که تا ژوئیه ۱۹۹۳ از طریق خط ریلی گیومری-قارص برقرار بود، به کلی قطع شد.
🔹
اکنون پس از کنترل کامل قره‌باغ توسط آذربایجان در سال ۲۰۲۳، ۲ کشور به دنبال احیای این اتصال ریلی از طریق مسیر گیومری-آخوریک-آکیاکا-قارص هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/459832" target="_blank">📅 23:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459831">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9616ce036c.mp4?token=mWe8p4HQE8lJEbL-bANxS131xd4J4jeNMAGO5CO6YXePNp2oaxYd_NhmPvp3gdwg2PC1HiD4qBWeKg2zShKv_4058asgp7oZJpIvOHXgTvTanLZZC9--pF-HcOTTSApMnifp6wZhXZD21QdytanxH82y8TrjuSSXwhg-4gqZrjjILyFWpndvdNWqeQsDB3oY_hhgH8MSdstFHdtoIG2Tn1wM0S2VCRjzNUEKOWEpHqqvk7juah4afJB3ID_WV9eGvmqAItOVNhX5D1iotIV0ixs8wbHcOkUdsRsPPQKAddBK-IQJfpL5TOM3JR07afy1I-iaNJBkqu4b5DOvbv_UIYlSXCDD5sFUKNqCD_X-_c_aOrBIuF3ikol3_bqVFR2OQEjWSUan7I8tq2gFI3sa0vHTrQCulKQkGlqeBuA27BR2nYOTl7VlUUTJPhihGQON7zNGKAvhgF4GMYPAmD09xSzb2LnoHbJUfS6xxyR5KOsiNBSfIrx6sxKiYMiFx_YmCxLoQqYiwp588uholQSLz6IVRXE07Gf0p85ffkNjCDpHM8rsLAnlnSHKAP9x8yNdupvyBHKL_KQFhAPgcYylXcMS9DHXiB2yOT5ZSrJw3ho1WKmJ6Ai57l8g8EyTflXgYa2sgSDSVd2_cdrLozUyYYYSu00o1k_mvWINGCsQjJ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9616ce036c.mp4?token=mWe8p4HQE8lJEbL-bANxS131xd4J4jeNMAGO5CO6YXePNp2oaxYd_NhmPvp3gdwg2PC1HiD4qBWeKg2zShKv_4058asgp7oZJpIvOHXgTvTanLZZC9--pF-HcOTTSApMnifp6wZhXZD21QdytanxH82y8TrjuSSXwhg-4gqZrjjILyFWpndvdNWqeQsDB3oY_hhgH8MSdstFHdtoIG2Tn1wM0S2VCRjzNUEKOWEpHqqvk7juah4afJB3ID_WV9eGvmqAItOVNhX5D1iotIV0ixs8wbHcOkUdsRsPPQKAddBK-IQJfpL5TOM3JR07afy1I-iaNJBkqu4b5DOvbv_UIYlSXCDD5sFUKNqCD_X-_c_aOrBIuF3ikol3_bqVFR2OQEjWSUan7I8tq2gFI3sa0vHTrQCulKQkGlqeBuA27BR2nYOTl7VlUUTJPhihGQON7zNGKAvhgF4GMYPAmD09xSzb2LnoHbJUfS6xxyR5KOsiNBSfIrx6sxKiYMiFx_YmCxLoQqYiwp588uholQSLz6IVRXE07Gf0p85ffkNjCDpHM8rsLAnlnSHKAP9x8yNdupvyBHKL_KQFhAPgcYylXcMS9DHXiB2yOT5ZSrJw3ho1WKmJ6Ai57l8g8EyTflXgYa2sgSDSVd2_cdrLozUyYYYSu00o1k_mvWINGCsQjJ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وداع با پیکر ۶ شهید حملهٔ دشمن آمریکایی در آغاجری خوزستان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/459831" target="_blank">📅 23:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459827">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc00a2101.mp4?token=At99CeqYjovAJp_PyTWYsjvGoG6QPkB2EJDwuxODeN7gPWSUpWHBm-d3U1M4I-hQdoX9gVI5UToOHGsWvwz3nhkosyp53gOOzkBlhsQ1Bze1OnXi3cfwir_jwY16Zbc8q_kEdambVW4yrhk6lhtcIXJsQXs1ehZJfKLlcuZ1mEq4H_kji_McfBVsHpU0aodXS2MF0wfGpv24aa2yx-jMolebNkn1rY9nC-nnYPxNr5WSW4ClrdEbbBZ0SFi5C35MixzYlAnNwvbioDM_lLzofOArhYmxfCS-Lrdk6qSil734Cc6BZ96JHjFjeNRp-bTkzZQdw1KTqJ46KqwPs89zgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc00a2101.mp4?token=At99CeqYjovAJp_PyTWYsjvGoG6QPkB2EJDwuxODeN7gPWSUpWHBm-d3U1M4I-hQdoX9gVI5UToOHGsWvwz3nhkosyp53gOOzkBlhsQ1Bze1OnXi3cfwir_jwY16Zbc8q_kEdambVW4yrhk6lhtcIXJsQXs1ehZJfKLlcuZ1mEq4H_kji_McfBVsHpU0aodXS2MF0wfGpv24aa2yx-jMolebNkn1rY9nC-nnYPxNr5WSW4ClrdEbbBZ0SFi5C35MixzYlAnNwvbioDM_lLzofOArhYmxfCS-Lrdk6qSil734Cc6BZ96JHjFjeNRp-bTkzZQdw1KTqJ46KqwPs89zgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: دیشب حملهٔ سنگینی به ایران کردیم و آماده‌ایم در صورت نیاز، حملهٔ دیگری را هم انجام دهیم.  @Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/459827" target="_blank">📅 23:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459826">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a925bb7627.mp4?token=mVy1fPEbAeqMQJqpgbNM08-Bt-MXZqNl1_k5tt5c74HVP2595tmug4MqA8YKkR67-RyNNlmTP3YKEmgSL95h6erFmZemtChdBeXPpiZ5cRjgauAb29v2D7Jc7QQ6LhxyKmo_Onf78kk9p3f8iY3FM1E_QXo2of2MSLtWoUFcF6PmxjkFgnQjXuX7iXetZZ5UOtCH5TTLRczrUWcHK0sQ4gqh-cmaZizyV7ww7omUVWV7eR79rlNX86tLGAULNs24LJTh0uMIUXHs-hInmXWvlAZo8io8I-eDW6zlMq3R4a9Nmb97YAUhEswMObPAFbyfIP2CT4f1TvM7dlo4p0tAWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a925bb7627.mp4?token=mVy1fPEbAeqMQJqpgbNM08-Bt-MXZqNl1_k5tt5c74HVP2595tmug4MqA8YKkR67-RyNNlmTP3YKEmgSL95h6erFmZemtChdBeXPpiZ5cRjgauAb29v2D7Jc7QQ6LhxyKmo_Onf78kk9p3f8iY3FM1E_QXo2of2MSLtWoUFcF6PmxjkFgnQjXuX7iXetZZ5UOtCH5TTLRczrUWcHK0sQ4gqh-cmaZizyV7ww7omUVWV7eR79rlNX86tLGAULNs24LJTh0uMIUXHs-hInmXWvlAZo8io8I-eDW6zlMq3R4a9Nmb97YAUhEswMObPAFbyfIP2CT4f1TvM7dlo4p0tAWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاطره جالب نجم‌الدین شریعتی از پیام ویژه‌ای که باید به سردار سید مجید موسوی منتقل می‌کرد
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/459826" target="_blank">📅 23:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459825">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🎥
۱۸۶ شب خروش حافظان تنگهٔ هرمز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/459825" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459824">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">فرود اضطراریِ هواپیمای وزیر آمریکایی
🔹
سی‌بی‌اس نیوز: یک هواپیمای گارد ساحلی که حامل مارکوین مولین، وزیر امنیت داخلی آمریکا، و دیگر مقامات ارشد این وزارتخانه بود، بعدازظهر چهارشنبه پس از کار افتادن یکی از موتورهایش در حومهٔ واشنگتن دی.سی. فرود اضطراری کرد.
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/459824" target="_blank">📅 23:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459823">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a8d7dc5cb.mp4?token=aTWCnUfSfkFHAjOKS798NRX3f8y0QxJ7m4xLCpCOID8rCVbKfLt6qGajKRpWEMP8c0CtfTnJxnFcMP51_x056zQHLaVawasaTwL3_XXJI6tu-sVfFwlWOR9xM9E4USm6vnE3ZKNHpV8R9J4B208wCsQ8bj6evxq-VI85WmlYESIbJSkvlG8GFmG9XoIrL6_JaY5C_IlN0UNaxbO8SzHKrS8ErZNaemkwjFVXzYuufALzWTzoMvHcpIx1vsAo7D6IMVGGzxuBHpWeSMHrboeL_cXE9GW_tZmQ_uMUJSy0hgND8sFWI1M53aW--fQs8IZo-jmf7Bc5T2DVlYnJWArDcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a8d7dc5cb.mp4?token=aTWCnUfSfkFHAjOKS798NRX3f8y0QxJ7m4xLCpCOID8rCVbKfLt6qGajKRpWEMP8c0CtfTnJxnFcMP51_x056zQHLaVawasaTwL3_XXJI6tu-sVfFwlWOR9xM9E4USm6vnE3ZKNHpV8R9J4B208wCsQ8bj6evxq-VI85WmlYESIbJSkvlG8GFmG9XoIrL6_JaY5C_IlN0UNaxbO8SzHKrS8ErZNaemkwjFVXzYuufALzWTzoMvHcpIx1vsAo7D6IMVGGzxuBHpWeSMHrboeL_cXE9GW_tZmQ_uMUJSy0hgND8sFWI1M53aW--fQs8IZo-jmf7Bc5T2DVlYnJWArDcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: ایرانی‌ها درحال ساخت موشکی بودند که مین‌ریزی می‌کند
🔹
تا به‌حال شنیده بودید کسی موشکی بسازد که مین رها کند؟ من که هرگز چنین چیزی نشنیده بودم. اما آن‌ها داشتند همین کار را می‌کردند. @Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/459823" target="_blank">📅 23:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459822">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e02b4187.mp4?token=o23qNWGvB94cvCYS9w1LBYCDJbvzQNLnV0rVRJUeSqMWOjB_l3V34NuXbgeV0G8jBSz0a9vBIl8KT19ghPexrxqqJnsVgUBvci4DaZBslCiFQyPBq-ROkJg4yBsyHUvZ2RRwJkbAptpCUHF_HsWq_qBh0rQ4ghHf2taWRmYs8mYfWeoeN6lgbrLuG6Tagfqpv75nPD5lkk_FaTZcgs2sS1-1DChf7PcmWbsC_pJBvUWyxyURXRppfbHQCpGtWe8-7305aevfdEVIlrP6COt8vfc5WTP1GdBt3QBcurb2wxK6hzsuMO85RKgemUUdFuHJ5lXmZRlNevDxdcXa-HcATA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e02b4187.mp4?token=o23qNWGvB94cvCYS9w1LBYCDJbvzQNLnV0rVRJUeSqMWOjB_l3V34NuXbgeV0G8jBSz0a9vBIl8KT19ghPexrxqqJnsVgUBvci4DaZBslCiFQyPBq-ROkJg4yBsyHUvZ2RRwJkbAptpCUHF_HsWq_qBh0rQ4ghHf2taWRmYs8mYfWeoeN6lgbrLuG6Tagfqpv75nPD5lkk_FaTZcgs2sS1-1DChf7PcmWbsC_pJBvUWyxyURXRppfbHQCpGtWe8-7305aevfdEVIlrP6COt8vfc5WTP1GdBt3QBcurb2wxK6hzsuMO85RKgemUUdFuHJ5lXmZRlNevDxdcXa-HcATA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خروش شهرکرد در شب ۱۸۶: نه سازش نه تسلیم، نبرد با اسرائیل
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/459822" target="_blank">📅 23:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459821">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seLYu0qFV1BLLi5XvlL427eDodBqgDwZhzix47KpPfYP3GkWyLYrCmRBJQG0no2IGwyP1bQhHtVVCl5EgQVAbRclYbNB1SVIdCqIPbHYk8F060JOF4-crvPfOznnpJrn0o0j0EPVpYnPdqskKjOhms8MYYjMwncBw8jrvGQUhg6NRQI-Utrd9_MvVToff-U_t3wHF0ql9Wvhn02nfgqZ7jYUeFMtMzVEidbEPpR2GoZpIdycbdtywOFO1L2Qhn_lnmA9z9w583zcG9-AOFPIX9UEouy3cepWbjht6dDik5EXH83wDRs2xiL6d7u1k0X2qKi85yVZbvct1uIeos_ObQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳۰ شکایت جدید، سازندهٔ چت‌جی‌پی‌تی را غافلگیر کرد
🔹
تک‌کرانچ:  اپن‌ای‌آی با موج تازه‌ای از پرونده‌های قضایی مرتبط با حادثه تیراندازی در تامبلر ریج کانادا روبه‌رو شده است.
🔹
یک شرکت حقوقی که پیش‌تر از طرف قربانیان و خانواده‌های آنان ۷ شکایت علیه اپن‌ای‌آی مطرح کرده بود، این هفته ۳۰ شکایت دیگر را در دادگاهی در کالیفرنیا ثبت کرده است.
🔹
ریشهٔ پرونده‌ها به حادثه‌ای در ۱۰ فوریه ۲۰۲۶ در شهر تامبلر ریج در استان بریتیش کلمبیا بازمی‌گردد. در این حادثه، مهاجم پس از کشتن اعضایی از خانواده خود به مدرسه متوسطه تامبلر ریج رفت و در آنجا چندین نفر را کشت و ده‌ها نفر دیگر را مجروح کرد.
🔹
بر اساس گزارش‌هایی که پیش‌تر منتشر شده بود، کارکنان اپن‌ای‌آی در جریان بررسی فعالیت‌های حساب کاربری مهاجم درباره برخی گفت‌وگوهای او با چت‌جی‌پی‌تی ابراز نگرانی کرده بودند.
🔹
طبق ادعاهای مطرح‌شده در پرونده، برخی کارکنان تیم‌های بررسی تهدید اپن‌ای‌آی خواستار اطلاع‌رسانی به پلیس کانادا شده بودند، اما در نهایت شرکت تصمیم گرفت با مقام‌های کانادایی تماس نگیرد و حساب کاربری را غیرفعال کند.
🔹
شاکیان ادعا کرده‌اند تصمیم برای تماس نگرفتن با پلیس تحت نظارت او گرفته شده و مدعی شده‌اند که تیم اطلاعات و تحقیقات شرکت در ساختار سازمانی زیرمجموعه او قرار داشته است.
🔹
گسترش این پرونده‌ها در حالی اتفاق می‌افتد که اپن‌ای‌آی هم‌زمان با مجموعه دیگری از انتقادها و پرونده‌های حقوقی درباره ایمنی محصولات هوش مصنوعی خود مواجه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/459821" target="_blank">📅 23:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459820">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d24269d2c.mp4?token=TF3enNheEu_AdVXqRwwhQ2HK9eylNFiiCWyZsH4qQVdSu-7pbSq7LOrj80wTO3UXpfpWZURNaEmzIBvIkx1aeCjsAV-w3lF9WttrNWjY4cO-Hb9Y1CbXKjoUvDxfzr4r6ZpNraNdrXGOzuyzeFPvOkzrOW6sQrsGSqbSfFctcrzNR28s1HpfzwJrnsQ4q5O7L6ncvzf4bkNiCDV1pneSDNtekG7ofe_Hi9XgI_m_14rDEXfkXMQkJVJBLb5dFpk-6oyfgJgXo8v3jiMG3F5CrFeVxZMv9sSqtVMaqlldan_fzisMQd-317tNG3zK0gH6Icyn5t1HXQzKps5U_XxPhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d24269d2c.mp4?token=TF3enNheEu_AdVXqRwwhQ2HK9eylNFiiCWyZsH4qQVdSu-7pbSq7LOrj80wTO3UXpfpWZURNaEmzIBvIkx1aeCjsAV-w3lF9WttrNWjY4cO-Hb9Y1CbXKjoUvDxfzr4r6ZpNraNdrXGOzuyzeFPvOkzrOW6sQrsGSqbSfFctcrzNR28s1HpfzwJrnsQ4q5O7L6ncvzf4bkNiCDV1pneSDNtekG7ofe_Hi9XgI_m_14rDEXfkXMQkJVJBLb5dFpk-6oyfgJgXo8v3jiMG3F5CrFeVxZMv9sSqtVMaqlldan_fzisMQd-317tNG3zK0gH6Icyn5t1HXQzKps5U_XxPhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تارتار: استقلال روی اوت‌دستی کار کرده بود و روی همان هم به گل رسید
⚽️
هم ما و هم استقلال می‌توانستیم برنده باشیم. از مسئولین اصفهان برای میزبانی و از داور برای قضاوت خوب تشکر می‌کنم.
⚽️
حسرت می‌خورم که ۳ امتیاز را از دست دادیم. استقلال روی تاکتیک اوت دستی…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/459820" target="_blank">📅 23:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459819">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">فرمانداری سیریک: صدای انفجارهای احتمالی امشب در محدودۀ بندر کوهستک، مربوط به خنثی‌سازی مهمات عمل‌نکرده دشمن آمریکایی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/459819" target="_blank">📅 23:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459818">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2863167ab2.mp4?token=v31lNcKSRkuYwDgkPYhdctWQ4Vi-vgXjcXFj60o7Z2jms-rOZ0AUKKsI-c-dxrGQAPWHItITpafC7VMKkKY3LGY8OCVY9iF18RNOvF49rboF15tiT1AV8-YSYEr-PkjyGf4EGuQ0yx8oeVb7scQPmoUgKts9d44vYSQm_B5Cb3m8DFuRr69WWBH24d1m7VFyjmkPSOP7Yr6hJcW4Bklpkzci9IU-6RsHIMr4-ObF2ujZiYaoudblNhcA4uhQENjEuTHnx1E2BnJ8JPPUTEWyUwxW0HpcsaN1F2ube0C-otanwHTf4C7RE9gbxHPl-Oq1axUP8zx4Ue6mqjTUT3Z0BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2863167ab2.mp4?token=v31lNcKSRkuYwDgkPYhdctWQ4Vi-vgXjcXFj60o7Z2jms-rOZ0AUKKsI-c-dxrGQAPWHItITpafC7VMKkKY3LGY8OCVY9iF18RNOvF49rboF15tiT1AV8-YSYEr-PkjyGf4EGuQ0yx8oeVb7scQPmoUgKts9d44vYSQm_B5Cb3m8DFuRr69WWBH24d1m7VFyjmkPSOP7Yr6hJcW4Bklpkzci9IU-6RsHIMr4-ObF2ujZiYaoudblNhcA4uhQENjEuTHnx1E2BnJ8JPPUTEWyUwxW0HpcsaN1F2ube0C-otanwHTf4C7RE9gbxHPl-Oq1axUP8zx4Ue6mqjTUT3Z0BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: ایرانی‌ها درحال ساخت موشکی بودند که مین‌ریزی می‌کند
🔹
تا به‌حال شنیده بودید کسی موشکی بسازد که مین رها کند؟ من که هرگز چنین چیزی نشنیده بودم. اما آن‌ها داشتند همین کار را می‌کردند.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/459818" target="_blank">📅 23:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459817">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4970a1d1d.mp4?token=gBazwFgl6aAxrXiEDXRHkaSZoLAf5iMJL5uJrVmuNlnknQZATsl2_p5XyzA_LF4nhcEHmT4E-VxjA4LePm6KKuheWjJP_5fmZuhOq2MPhQk8dLzOAMZNOKLJkOqMTo8h0cesCbR9jZT8jkfFd5WHZo9e-WFRLf3Yk1GsiuLhfiFua_JBn6R7t-W89kSa9Y7CCW3Nko8e0Wukexb8RYwWFS0q2eYyWHnvTbvFrhq3q__vHun_tz-BkVuGUV7gFv0G7zbdGvtXhWEFv7G12RbD3UNFIZ1cHZZdG4J2OCe29EUH4ztnNV1gSBubPhzEzieow1ibqUZVzFxUUh55wLUIIYe2F1qi_PyL1mYDtqFAItJacq6Dmkgz8SzKPGma4xSCr6fYP4WILm_rXrqlTYxrtF0esbjpkG-iVZ_MV_Fe7BPLqbE3MNpJ0-_dCb_DbiaLSLqMpdKfFWgri8ezFihPbczZwRft2PKwqASTxPtOnfEl9FkDKC-xYOiKPXsPBUvq_yh7EfA32O9Pafxbfw7LzoESa5N_WRL5SEyRhMLd-mPjOubpfJAWuH5CLE1pznbCNfQBY6ix7q3rMNHuEAxPsrY99nQORAmiRUhCpS69BF80dM3ukkXjU6G0zEdmwJBicoS0WSgh8rllUqY033unKe2eMITq3CwZSPZVC7biPCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4970a1d1d.mp4?token=gBazwFgl6aAxrXiEDXRHkaSZoLAf5iMJL5uJrVmuNlnknQZATsl2_p5XyzA_LF4nhcEHmT4E-VxjA4LePm6KKuheWjJP_5fmZuhOq2MPhQk8dLzOAMZNOKLJkOqMTo8h0cesCbR9jZT8jkfFd5WHZo9e-WFRLf3Yk1GsiuLhfiFua_JBn6R7t-W89kSa9Y7CCW3Nko8e0Wukexb8RYwWFS0q2eYyWHnvTbvFrhq3q__vHun_tz-BkVuGUV7gFv0G7zbdGvtXhWEFv7G12RbD3UNFIZ1cHZZdG4J2OCe29EUH4ztnNV1gSBubPhzEzieow1ibqUZVzFxUUh55wLUIIYe2F1qi_PyL1mYDtqFAItJacq6Dmkgz8SzKPGma4xSCr6fYP4WILm_rXrqlTYxrtF0esbjpkG-iVZ_MV_Fe7BPLqbE3MNpJ0-_dCb_DbiaLSLqMpdKfFWgri8ezFihPbczZwRft2PKwqASTxPtOnfEl9FkDKC-xYOiKPXsPBUvq_yh7EfA32O9Pafxbfw7LzoESa5N_WRL5SEyRhMLd-mPjOubpfJAWuH5CLE1pznbCNfQBY6ix7q3rMNHuEAxPsrY99nQORAmiRUhCpS69BF80dM3ukkXjU6G0zEdmwJBicoS0WSgh8rllUqY033unKe2eMITq3CwZSPZVC7biPCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لاشه‌ٔ متلاشی‌شده‌ٔ «ام‌کیو ۹» زیر پای رزمندگان خمین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/459817" target="_blank">📅 23:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459813">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hg_PSiwujl0jcLd6SIYhUhagASMacBGYXFWLshQET6ZZKFejDBQfjSba5Rhqrmx-s5JEztNNQ2-O6DQqD4fN9LnS_yEOZ6EpYBnTVbcgi_LY4XA82GBhsGs9vmdfAxf_-QC2CEEIhrigYIkj149p9nV4oQAZ_NZlD6kfTVPvq_KeJApJTh29HJlPQptShLDw3lxngGFIeAHyD8hkjHv2CCBVeWcZHepwe6axjmaMZiDjAjR8BlOLgF7Hj3RTR9CrO5F6VaL2PFImP9Sb7dv3x7J-G01OkKbHcqxoGc4yX_tivR1YeDY08C2Yhwwqe2g3aYsFCLi7dDc-0K3cAOooCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c3rhdd6osyKaGOOUvmka8du8hrtvbVhMfvzYaGz2mAo6wIlU-w6QZiuYJRSko2ksWwqe_trGRfRoXKJ1zTq3kQKmqjDlayqdWk_iPL92pSmpl2jxEWvBcOWdazk06cJyfGThl8JIfGvx2Xh_bsz4oYVSRmYF_afv1GSckpHe6aGdX0HSZyYQHmfXuKU60m5e2LwSb2mAEGOTc4Hf4oEWq4xXMR2ZPHk4DrUpZMVA3Nsh8V08Z5AkAhi8NHgkQRmo-aU34Nsv20aYnfigoVIY1LFzrm-NqWhep_NydxY4ajJbK-2CEg9MUvgfAhy9MxguGeQ0Jtl_7NYcPTl7GHmITQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/miMgB_DWTx1PU5qtm0xkBboJfLxwRLn6V3qqDNBhtNAZSgFC9KEmHtg-oxyE3J4ybGY7n63iM10hDHBxq05U8oc7yrEFr2mzFf_xxTF1_EQ9ToAXTXlqGmJQYVWAya3acXoGriqvLU3RfmXDuemTll6P20bMIZxC4wf4h84uWL28YKpN8okpTUapStCxfyrjN-05DIKZO2uC9xTZC9viy5AmA-iJw3G4Rfji9F45Hp0eb8pPuOTqXUiE5R9seNvJvJTSh2o9uLYQCnmjQzITpAFgvNWdy9vkjBrtIj9mxhgu0ClU-j_WT7Ho_k1VKtcUcXL9ZpnTr0WKsELlpMbHVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IyFzI7V_XFaWPaZ0-emvnCpeW9VAcy2ZCDFIcgbyLWCOr1NaOPltU4j9fY482T1AnesyGgGdN1NoDEDLWEX8kJ9eHT7PhoF3vq63f_4fvxNmCjcXK5DbhJrpGrI-ZNYtvJRNbb1EJT3XpJbfuhjDtc2mT23OiEE8dTlogzAL8b225bzLglTnN5krHn45bk1Y-LHlB_6p7D3brsoqMdjyNnhB-24ILMa-5f4qXwkGp41mUKgntxy7uyYD1_melGJqZgsHnla82uWalMWVfHajPbyN3XmqCyU-2Uh8N6b8goj87A9bgsEsIlwNXC9cIurVzKXLI5bkMdhq7k4fCPXcrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بقایای موشکی که دیشب عروسی سیریک را به خاک‌وخون کشید  @Farsna - Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/459813" target="_blank">📅 22:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459812">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/036d5b9fb4.mp4?token=dO7uh-KJY_zsbyi5IgLYZnVS302ibzmTFK7E16lB68ce3OTuNh6GnlvuKW4ue5dmU0u9J03fveS_y_p7r6NSZQz33ViXEG5-LB1GO-3l_ktwAJFTYtyyjAx9JMd0ZQkfClFtXa5QMUkcG9uibpWUPcCtRYLoB0MCxVHiTTpK__EJwXSpiA_T54sItjEIf4XcpMVWdc6zurO3RTE25L2cqtHTpAoH_XHXOPljYoUdfQToO9UwvSKgIk80210Bk7JAOq0xlP284sZpCOSrvAZWdyKxECwpSEbsIjGFNO3HogKzdRdJNZ9joPZN54ERY-ud81Ck8nhxjGuJbOjKoAh4Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/036d5b9fb4.mp4?token=dO7uh-KJY_zsbyi5IgLYZnVS302ibzmTFK7E16lB68ce3OTuNh6GnlvuKW4ue5dmU0u9J03fveS_y_p7r6NSZQz33ViXEG5-LB1GO-3l_ktwAJFTYtyyjAx9JMd0ZQkfClFtXa5QMUkcG9uibpWUPcCtRYLoB0MCxVHiTTpK__EJwXSpiA_T54sItjEIf4XcpMVWdc6zurO3RTE25L2cqtHTpAoH_XHXOPljYoUdfQToO9UwvSKgIk80210Bk7JAOq0xlP284sZpCOSrvAZWdyKxECwpSEbsIjGFNO3HogKzdRdJNZ9joPZN54ERY-ud81Ck8nhxjGuJbOjKoAh4Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تارتار: برای برد آمده بودیم نه تساوی
⚽️
اگر مربیان شجاع باشند، بازیکنان هم از آنها یاد می‌گیرند؛ امسال تیم‌مان فوق‌العاده است و برای قهرمانی می‌جنگیم. @Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/459812" target="_blank">📅 22:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459811">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49ad3b2cbe.mp4?token=qmtCCHQVtwy5XJn9km_Y2Et4bvooYIRgT3T_AjjDxMXYx4Um1NNcJIu6Ut1mgvk3vLzDMSXge5K20aDYWzrOIZ2854ZJ20GfRoYBeGyglMuuBzVe6dwEeSewODuRwlywjmTF3jeqPN9lRqi8ILaXGjBW-K_fzPn7nGCpjcrWhcT8LJ-RhRAk8D5fcS7tRS24nnYgYHvXwx7XTHf5kktHGcrIKte9-UciS4lpDQfKOiyrQLD5DYqFbUiEUoTN7r7CMCl_eEArJj7ATNCN_2vbdNTqkHv-dIs2fbZlmnzMqKsVZ0r0S6Zql9B-Zhq3r302MNy6DtLLgEStixDCaXBUaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49ad3b2cbe.mp4?token=qmtCCHQVtwy5XJn9km_Y2Et4bvooYIRgT3T_AjjDxMXYx4Um1NNcJIu6Ut1mgvk3vLzDMSXge5K20aDYWzrOIZ2854ZJ20GfRoYBeGyglMuuBzVe6dwEeSewODuRwlywjmTF3jeqPN9lRqi8ILaXGjBW-K_fzPn7nGCpjcrWhcT8LJ-RhRAk8D5fcS7tRS24nnYgYHvXwx7XTHf5kktHGcrIKte9-UciS4lpDQfKOiyrQLD5DYqFbUiEUoTN7r7CMCl_eEArJj7ATNCN_2vbdNTqkHv-dIs2fbZlmnzMqKsVZ0r0S6Zql9B-Zhq3r302MNy6DtLLgEStixDCaXBUaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملات صهیونیست‌ها به جنوب لبنان ادامه دارد
🔹
شبکه المنار: ارتش رژیم صهیونیستی اطراف ارتفاعات راهبردی علی‌الطاهر را هدف حملات هوایی و توپخانه‌ای قرار داد.
🔹
همچنین جنگنده‌های این رژیم بار دیگر شهرک النبطیه الفوقا و شهرک حاریص در جنوب لبنان را بمباران کردند.
🔹
ارتش تروریستی اسرائیل، عملیات انفجار و تخریب جدیدی هم در شهرک حولا و بیت لیف انجام داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/459811" target="_blank">📅 22:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459810">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">تشییع شهدای مظلوم عروسی کوهستک فردا برگزار می‌شود
🔹
روابط‌عمومی سپاه هرمزگان: مراسم تشییع پیکر مطهر شهدای مظلوم مراسم عروسی کوهستک که در جریان جنایت رژیم آمریکا به شهادت رسیدند، پنجشنبه برگزار می‌شود.
🔹
مکان: شهر کوهستک، از بلوار ورودی شهر تا گلزار مطهر شهدا…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/459810" target="_blank">📅 22:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459809">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a99e356a4.mp4?token=Ro5O0vVrtolatoQBv2FI9gjOcflNfbtnXaGDUTbKw-4fLvOWAd7XPWw8MsAo2jBZgQVxEl5HyT1HbCWQZdrK4_YfvkRsN-nSzqEQGwjeMcvz8W1ENBubnI8gn05DeyNbQHy5w5OzlHbBV_ivsSi_l79TnZ8qN3yEdwisjAYYwzXR5hXnGdenSP3kOkZv6razzduaW6UT3YlhvOIDdvitOGbLO9TbMrW1hVNd53FV74OtsPjUrmIEup3c0LWkbee3JOspYrLQaAbXmtCiek3j1JOJdilMLy8N1udwObaFGLgoqn4YshmpCkgjcFoqTTiJexJyXL9wg_gYYUTZhUkEnB_6choZTBZ7PCjm-mpeM785X9zauakfem42C9joFHtwRb6L6Y8S1TKkSNGrqBhUlm_x2iN8sz-UTnK-YOtOiwrk96CkQLTVGHez2GUbXcW95JAyDJ09gxt78BQhfqJsoLjmS0_tyaMRMA_w9PW4OUDelXXjOfw54RdeAuGeR4Q-XjknZUWS4bQMTkXohgxO1AlKjT5iTp0Mkxtnoe35XBlF3PIbtbfcdiz3MfylyclsQAMd4kPbt0MO7HyuLol2yrfL4PRKpsFF-TEiDt1B_S9zRjZjOxXNz8horcV332im7qf6Mgb_MHXuTpiycL-iRBj6-WyksqBJlhHKQ3kojbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a99e356a4.mp4?token=Ro5O0vVrtolatoQBv2FI9gjOcflNfbtnXaGDUTbKw-4fLvOWAd7XPWw8MsAo2jBZgQVxEl5HyT1HbCWQZdrK4_YfvkRsN-nSzqEQGwjeMcvz8W1ENBubnI8gn05DeyNbQHy5w5OzlHbBV_ivsSi_l79TnZ8qN3yEdwisjAYYwzXR5hXnGdenSP3kOkZv6razzduaW6UT3YlhvOIDdvitOGbLO9TbMrW1hVNd53FV74OtsPjUrmIEup3c0LWkbee3JOspYrLQaAbXmtCiek3j1JOJdilMLy8N1udwObaFGLgoqn4YshmpCkgjcFoqTTiJexJyXL9wg_gYYUTZhUkEnB_6choZTBZ7PCjm-mpeM785X9zauakfem42C9joFHtwRb6L6Y8S1TKkSNGrqBhUlm_x2iN8sz-UTnK-YOtOiwrk96CkQLTVGHez2GUbXcW95JAyDJ09gxt78BQhfqJsoLjmS0_tyaMRMA_w9PW4OUDelXXjOfw54RdeAuGeR4Q-XjknZUWS4bQMTkXohgxO1AlKjT5iTp0Mkxtnoe35XBlF3PIbtbfcdiz3MfylyclsQAMd4kPbt0MO7HyuLol2yrfL4PRKpsFF-TEiDt1B_S9zRjZjOxXNz8horcV332im7qf6Mgb_MHXuTpiycL-iRBj6-WyksqBJlhHKQ3kojbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مراغه پای عهد ایستاد؛ مطالبهٔ پاسخ قاطع به دشمن
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/459809" target="_blank">📅 22:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459808">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7ebad354f.mp4?token=v0W2zsgUkCHzIxJgRFY5Yov0gMa-hZ1XtHoQ9Z08cbzAEuUFAa_2nfk0lHHU-0QsMaUlSpSb-rdzo6GLtze1tPdpq9zKDNAcbqOA0kHT8gBC_FqeJtEkckin-5v0V4xiNzrFx1NmM74yV2i3ylh0LQhau3udavkueZkR1cMhQYB-F9tbV25RBVvguPImksy_Egdzvqp6q_BrqOUjx58Bo62iyJdlIFf9KhIgsVjEV0GcJOYqTI34rHzaLFPFr3o5Q0Sc7H71yTJ0yw8mPESMBuDwLpe_i6SAhFJ1uKoATyldfa8aYEE81IUHoO-IJt6pFqSOsYR3Un4aDADfbEMpTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7ebad354f.mp4?token=v0W2zsgUkCHzIxJgRFY5Yov0gMa-hZ1XtHoQ9Z08cbzAEuUFAa_2nfk0lHHU-0QsMaUlSpSb-rdzo6GLtze1tPdpq9zKDNAcbqOA0kHT8gBC_FqeJtEkckin-5v0V4xiNzrFx1NmM74yV2i3ylh0LQhau3udavkueZkR1cMhQYB-F9tbV25RBVvguPImksy_Egdzvqp6q_BrqOUjx58Bo62iyJdlIFf9KhIgsVjEV0GcJOYqTI34rHzaLFPFr3o5Q0Sc7H71yTJ0yw8mPESMBuDwLpe_i6SAhFJ1uKoATyldfa8aYEE81IUHoO-IJt6pFqSOsYR3Un4aDADfbEMpTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اینترنشنال این‌بار ناخواسته راست گفت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/459808" target="_blank">📅 22:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459807">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🎥
احترام نظامی سنندجی ها در ۱۸۶ شب ایستادگی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/459807" target="_blank">📅 22:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459806">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🎥
روایت مردم پاکدشت از ۶ ماه ایستادگی در خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/459806" target="_blank">📅 22:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459805">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7651c4643.mp4?token=sZxnXyfxAfS0epy-6Z50-LC1R0MsJZXKL4UdWojEiK4Fva-wB20cAm9YYsGVGcnCdwu2Ky5gnx7bBHTeEy4iHS7Ok3Snx3Nm845Sb1eeBkQ1e-ee0ypxCrHajymCso_zbBJgPukr2GxCLzODT8onM3zXfpSVe5Ik8jZoU0l7rDGLnDad88vm3FvqLpW0w-fvtB-s5Z4VQMWT0XZ-SkbmJWbhpLdfiH4FlGiYVc6XveculvlUNr_WQeJTtekP-h1wsVitU5uYVJWWbTDHR1Pplqj10ELKU5Mi87zd0xzQ_0pqJKSosYLy3geZ168uaCfU90tpxh9aeVoyVZeHrpx-XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7651c4643.mp4?token=sZxnXyfxAfS0epy-6Z50-LC1R0MsJZXKL4UdWojEiK4Fva-wB20cAm9YYsGVGcnCdwu2Ky5gnx7bBHTeEy4iHS7Ok3Snx3Nm845Sb1eeBkQ1e-ee0ypxCrHajymCso_zbBJgPukr2GxCLzODT8onM3zXfpSVe5Ik8jZoU0l7rDGLnDad88vm3FvqLpW0w-fvtB-s5Z4VQMWT0XZ-SkbmJWbhpLdfiH4FlGiYVc6XveculvlUNr_WQeJTtekP-h1wsVitU5uYVJWWbTDHR1Pplqj10ELKU5Mi87zd0xzQ_0pqJKSosYLy3geZ168uaCfU90tpxh9aeVoyVZeHrpx-XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هشدار ژنرال‌های آمریکا به ترامپ: توان ایران را دست‌کم نگیرید
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/459805" target="_blank">📅 22:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459804">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b593798c4.mp4?token=d41VcrlVkUZLwwCXU8-n2tkS5pmC9yM9aNJ37OsScMFV-pZvudhoXyQwlgtfZ0FyeHOKHaD2V5Hi9QODUSMxd6ylfbFBCCqJ29perUfDp7P5zQWEVZraRyH_vTrdk__o5fNqS2ZnVWM6WsdM5pAs0tVQ7CWr3rBoeFxGWK_4HRpHrlIcJvyyuOWeJyT2K-RMacdKeFMWg-qx9nqgoGmWFj-kl2EGJo5K5tn77ji4KGAfYCARZ_sely1XNnxaKhm2SWyZ3_wIaQIehyw_s2YJK55D2Ph0r3F6hXah63nhl-DzI5hrrumNtNFpHGEBxRwUvN5VQ7MCTp51i82kdOmCUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b593798c4.mp4?token=d41VcrlVkUZLwwCXU8-n2tkS5pmC9yM9aNJ37OsScMFV-pZvudhoXyQwlgtfZ0FyeHOKHaD2V5Hi9QODUSMxd6ylfbFBCCqJ29perUfDp7P5zQWEVZraRyH_vTrdk__o5fNqS2ZnVWM6WsdM5pAs0tVQ7CWr3rBoeFxGWK_4HRpHrlIcJvyyuOWeJyT2K-RMacdKeFMWg-qx9nqgoGmWFj-kl2EGJo5K5tn77ji4KGAfYCARZ_sely1XNnxaKhm2SWyZ3_wIaQIehyw_s2YJK55D2Ph0r3F6hXah63nhl-DzI5hrrumNtNFpHGEBxRwUvN5VQ7MCTp51i82kdOmCUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ربات کینه‌جو انتقام گرفت
🔹
یک ویدیوی عجیب از یک فروشگاه در روسیه منتشر شده که در آن، واکنش غیرمنتظره یک ربات انسان‌نما پس از رویارویی با یک مشتری، حسابی خبرساز شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/459804" target="_blank">📅 22:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459803">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
از وقتی در
اهواز
دستگاه تصفیه آب نصب کرده‌ایم، هم مصرف برق بیشتر شده و هم هدررفت آب داریم. برای تهیه یک کلمن آب خنک، باید حدود دو کلمن آب تصفیه‌شده به فاضلاب ریخته شود تا آب تصفیه شود. لطفاً مسئولان درباره این میزان
هدررفت آب و راهکار کاهش آن
چاره‌ای بیندیشند.
🔹
من یک کشاورز از دادین سفلی شهرستان کازرون هستم.
برق چاه کشاورزی
ما از ساعت ۱۰ تا ۵:۳۰ قطع می‌شود و دو ساعت هم خاموشی کلی منطقه‌ای داریم؛ در مجموع روزانه حدود ۱۱ ساعت و نیم برق نداریم. باغ‌های مرکبات ما در دمای ۴۰ درجه و به ‌دلیل کم‌آبی در حال خشک‌شدن هستند و صدای ما هم به جایی نمی‌رسد. لطفاً به داد کشاورزان برسید.
🔸
بنده ساکن نسیم‌شهر، شهرک نور، خیابان جانبازان هستم. لطفاً به مسئولان
رایتل و همراه‌اول
اطلاع دهید که این شهرک به هیچ عنوان اینترنت و آنتن مناسب ندارد. حتی برای کارت‌به‌کارت کردن باید تا سر خیابان برویم تا اینترنت داشته باشیم و در بسیاری از مواقع هم در دسترس نیستیم.
🔹
در شهرستان رابر هنوز حتی یک مرحله واگذاری زمین در
طرح مسکن ملی حمایتی
انجام نشده است. به داد شهرستان رابر برسید؛ تا کی مردم شهرستان‌ها باید تاوان عملکرد ضعیف مدیران شهرستانی را بدهند؟ از دولت درخواست داریم نظارت و کنترل جدی بر عملکرد مدیران شهرستان‌ها، به‌ویژه نماینده ارشد دولت در شهرستان داشته باشد.
🔹
چرا هیچ ‌کس جلوی
افزایش قیمت خودرو در شرکت‌های ایران‌خودرو و سایپا
را نمی‌گیرد؟ چرا نظارتی وجود ندارد؟ مدیران این دو شرکت هر زمان که بخواهند قیمت‌ها را افزایش می‌دهند. مردم چه گناهی دارند؟ در شرایطی که همه باید به یکدیگر کمک کنیم تا کشورمان مثل همیشه سربلند و پیروز باشد چرا این دو شرکت از شرایط موجود سوءاستفاده می‌کنند؟
🔹
یک دختر معلول شدید دارم و خودم هم معلول خفیف هستم. چرا دولت
قانون ماده ۲۷ برای معلولان شدید
بالای ۱۸ سالِ بیکار را که سال‌هاست در مجلس تصویب شده، اجرا نمی‌کند؟ با این فشار اقتصادی و تورم به معلولین که قشر آسیب پذیر جامعه هستند هم برسید.
🔹
در
اسلامشهر
به‌دلیل سرقت کابل‌های تلفن، ماه‌هاست تلفن‌های ثابت قطع شده و
مخابرات
نیز پاسخ‌گو نیست. اینترنت ثابت هم به همین دلیل قطع است و مردم ناچارند از اینترنت گوشی استفاده کنند که آن هم مشکلات و هزینه‌های خود را دارد.
🔹
کارخانه
واگن‌سازی زرند کرمان
(پلور سبز) دو ماه است حقوق کارگران را پرداخت نکرده و هر ماه به بهانه‌های مختلف پرداخت حقوق به تأخیر می‌افتد. از طرفی اعلام ورشکستگی شده و طلبکاران برای مصادره اموال مراجعه کرده‌اند. حدود ۲۰۰ نفر در این مجموعه مشغول به کار هستند. خواهشمندیم صدای ما کارگران را به گوش مسئولان مربوطه برسانید.
🔹
شهرداری منطقه ۲ کرمان
در خصوص آسفالت ‌کردن کوچه‌ها، کاملاً سلیقه‌ای با ارباب‌رجوع برخورد می‌کند و متأسفانه فریاد ما در کرمان به گوش کسی نمی‌رسد.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/459803" target="_blank">📅 22:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459801">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lxLzfan_x4kR7kpb2ieoqGZKwR9YHrSjzPtvjfupjYDkUbcaMaPqFoCMDTGg4F5XRjUdHw3tNucQlqmTQT5SnTr8ltk-o14YDyvPAue3mqMDErLJypb6pH3BZd8-gRmmCn2eXkkhOeZ-KHcP4KJdtJ_ZxToBeT3UUuF8Z_g7AN81QAuvAsKvhr_ODZzTSledfGCLl2zIRqvEkl-AaSAtCmyKqtpxeTEOA80mXMGA_TiVs1TtuFO1jErkwLvlFLJ2_wYuZyV2PBuvqLAbXap92L_KaW9zo-uVS7fLOfJwhk9zpMyhIobC9Q8gwf8B1H6eErLJDVcDbygFm4yYW4jBPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xc-epM9Ts8yMOvVnV5twNw9IWgqg0tNUl5yJDZAT81eFQFp26I78TZaYTuk6mhhtb2atcU0h980BiGuWWU5sNvfiHuEzjAr67QvJ0gHikb7DuyrtsRfxTWDJv8cCOgkX-oKHBehPRZyL9UXBHQjE5wOb-xEE1J6XKdEiUXMslhKC-BqjM_63jpckrnfwNpoJi4X14ALxbxiPsfUxrrD2GI8ELX_tHnRuDrSzy1d4HfFyKYUr_6WMq3aI69yVmANYeCEt0mf0Suo1B2jbJB5-LYXn4-ouSsYF0pfbcFyiknyPXXOhRIra9reUiAwpONni8I9PPxYgvMphU4eVUNjeAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
نهاد مدیریت خلیج‌فارس: فهرست شناورهای متخلف بروز شد
🔹
برخی از این موارد با اطلاعات داوطلبانۀ مردم به‌دست آمده است.
@Fasrna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/459801" target="_blank">📅 22:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459800">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwXHFMCtGTefrarzMUR3vDgBXPd64B53DGyYxXaqTqeBwjfp-ehMq4wr9aJcrEMSf0vSlaWek5Bg4qWUnSKFTbh6hbX2RMgDxuHBZx8S3QUjhZ1aKYra9lJ5kIb5NagvDioZA1uT04qGLSdI2WRY1abLBuN_SuwO3mYkIpQhmc07acc-1X6A0v0FKcpVMWlmUxgEqcBxGuMR8RGwOZFUg2n9UJ-uaxDXQ463lEZA_q60xbl93MMB28IZJiWKgZmT7MkBPMpiG2T5ldlEUMbiKPhDFS5fmAEsDSMevgvDPr94wfPK7-PkOiaek0wRIX_nvUjnYDTv6-TisWiQA7MtVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خط جدید ارتباطی با صندوق بیمهٔ حوادث ساختمان راه اندازی شد
🔹
مدیر روابط عمومی صندوق بیمهٔ حوادث طبیعی ساختمان: از این پس بیمه‌شدگان می‌توانند با شماره‌گیری ۵۲۱۴۴، ضمن دریافت پاسخ و راهنمایی‌های لازم، روند پیگیری پرونده‌های خسارت خود را با کارشناسان ذی‌ربط دنبال کنند و از آخرین وضعیت پرونده خود مطلع شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/459800" target="_blank">📅 21:56 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459799">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5076db8a.mp4?token=UmgwXHGWYcvBTRNBAVCvJMkF7lNQ1mSjCHDMac2-9YGQQgHm5l22qvSbhLDWoCKnXXLGWjKQWsooFJQjkx68l22pDpAZfbPXkAoOOzxvbb2-eJxyypWkI4toBv6jrZ0KYGldkpfUZ7NX7dZLfwpMXE3AQ4UNd8MbCVQeISnGR3AlGBubrDoqPokS_S2UzRpxsA_7P-nEG6Xv8grArf83PpMl-1LnIbwh31Ds78UNuCSq98vlo7S_Llk3YU_-UAK7G9I12XKf_wt72HIKZs6awjl9ejI-tHmjsMcOzDeTGkcuwoZ_sKN0g1uVre8W9oPtk_LDcy7IdUSWtqUoKBGqEJkh-NjadhckVxXZPLQgRqybzkdZjY5aGy9fb-txqhlM4VNe32cQNFe361cnq8tQRYyrNXBOmNQXUDcqONm2TdfFnRhm3RtHNe8NyJMf9fiHPoQdMlRhIpuyBf0bB9mHa7ZuNsagRIEBjmcjsTSHExbVfpL4_yjfKpxnQALNq5mg8Swjq8ibDBspgqV0YFIpfoqd-_BgCPAp1Rbvgnp1o3d_WDG2ZDyc3YGK392QGhpdbVbY3OkApzxywKEAxIrRp--OUeEEVb9UQjD6zbefBjWZssfu3xzxmMb6vDWwWJ5kUVxWk1HUC2n1-Zajcg_euPW-HO0MbSd-YZopvK2zm8E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5076db8a.mp4?token=UmgwXHGWYcvBTRNBAVCvJMkF7lNQ1mSjCHDMac2-9YGQQgHm5l22qvSbhLDWoCKnXXLGWjKQWsooFJQjkx68l22pDpAZfbPXkAoOOzxvbb2-eJxyypWkI4toBv6jrZ0KYGldkpfUZ7NX7dZLfwpMXE3AQ4UNd8MbCVQeISnGR3AlGBubrDoqPokS_S2UzRpxsA_7P-nEG6Xv8grArf83PpMl-1LnIbwh31Ds78UNuCSq98vlo7S_Llk3YU_-UAK7G9I12XKf_wt72HIKZs6awjl9ejI-tHmjsMcOzDeTGkcuwoZ_sKN0g1uVre8W9oPtk_LDcy7IdUSWtqUoKBGqEJkh-NjadhckVxXZPLQgRqybzkdZjY5aGy9fb-txqhlM4VNe32cQNFe361cnq8tQRYyrNXBOmNQXUDcqONm2TdfFnRhm3RtHNe8NyJMf9fiHPoQdMlRhIpuyBf0bB9mHa7ZuNsagRIEBjmcjsTSHExbVfpL4_yjfKpxnQALNq5mg8Swjq8ibDBspgqV0YFIpfoqd-_BgCPAp1Rbvgnp1o3d_WDG2ZDyc3YGK392QGhpdbVbY3OkApzxywKEAxIrRp--OUeEEVb9UQjD6zbefBjWZssfu3xzxmMb6vDWwWJ5kUVxWk1HUC2n1-Zajcg_euPW-HO0MbSd-YZopvK2zm8E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش خبرنگار شبکهٔ سه از قشم: احتمال دارد تعداد شهدای حملهٔ دیشب آمریکا به یک مراسم عروسی افزایش پیدا کند
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/459799" target="_blank">📅 21:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459798">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cbe705fb9.mp4?token=Vopm46pZLa_MDbBPMJ5BZwB6siWCqfG8uvN1QnjR1mNDuJXfudEqEo7WMAdnbzckmbF5uw0xoAowAYm_WBSO90D7L2SUfmBKE7EeiDD1BDOWnmoHmtmL86oPjK2eN71WNTbuX1RKL6UP4sm2bXJHrkGDw4vtdmU6UDA5Ohs0NMMmNbklppTpNDhO0c9k8OsTNqlltzK4n51A2xBgD0AmKNHvVKngB3bigZ-XiGYXPmDbnHl866UzsYWcLKIhh4x-lMiVDDSoWCSzrTjvif7PiJG7oV3EgaMtLgCJenGcAP0niwfEZOetdOn7BpQuJo6-eNQib5NgddpcAcClHHYhJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cbe705fb9.mp4?token=Vopm46pZLa_MDbBPMJ5BZwB6siWCqfG8uvN1QnjR1mNDuJXfudEqEo7WMAdnbzckmbF5uw0xoAowAYm_WBSO90D7L2SUfmBKE7EeiDD1BDOWnmoHmtmL86oPjK2eN71WNTbuX1RKL6UP4sm2bXJHrkGDw4vtdmU6UDA5Ohs0NMMmNbklppTpNDhO0c9k8OsTNqlltzK4n51A2xBgD0AmKNHvVKngB3bigZ-XiGYXPmDbnHl866UzsYWcLKIhh4x-lMiVDDSoWCSzrTjvif7PiJG7oV3EgaMtLgCJenGcAP0niwfEZOetdOn7BpQuJo6-eNQib5NgddpcAcClHHYhJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جنگ، تحریم، کودتا؛ آمریکا دوباره نسخهٔ شکست‌خورده‌اش را کلید زد
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/459798" target="_blank">📅 21:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459797">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767fce29d6.mp4?token=jLJOMtRPUhRf7KnkSBsqJtSekChxFfZ05IfSCyQRbyI56UDRTxg7KNUxQhSbdWRctjnp1AqGepWDNJCPr9JCbTaeYVftaNzq-FK-MQClxmVNecRMwOZvAlNPQFbTGJ2PUBJJ8NQuR5VIfn1-tM8MXshQKhei4Z4Te0d7Gr9JixS9027pO1E0rQoTnxcxjPKlfGmMeh3cnhw8Ukv6REzKw_I9VjT5cbkBtGiFERzyVH85HI-IJe_XGEAr4fizSHk0Pwbr9eLSNBQaXaqblxN8oyS_A0S0HYiVO3ewB49Z5A1sWO-EfPtMs9FYxB8gIcGut_Utf82hGiU3Fb81M2Ddvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767fce29d6.mp4?token=jLJOMtRPUhRf7KnkSBsqJtSekChxFfZ05IfSCyQRbyI56UDRTxg7KNUxQhSbdWRctjnp1AqGepWDNJCPr9JCbTaeYVftaNzq-FK-MQClxmVNecRMwOZvAlNPQFbTGJ2PUBJJ8NQuR5VIfn1-tM8MXshQKhei4Z4Te0d7Gr9JixS9027pO1E0rQoTnxcxjPKlfGmMeh3cnhw8Ukv6REzKw_I9VjT5cbkBtGiFERzyVH85HI-IJe_XGEAr4fizSHk0Pwbr9eLSNBQaXaqblxN8oyS_A0S0HYiVO3ewB49Z5A1sWO-EfPtMs9FYxB8gIcGut_Utf82hGiU3Fb81M2Ddvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تارتار: استقلال روی اوت‌دستی کار کرده بود و روی همان هم به گل رسید
⚽️
هم ما و هم استقلال می‌توانستیم برنده باشیم. از مسئولین اصفهان برای میزبانی و از داور برای قضاوت خوب تشکر می‌کنم.
⚽️
حسرت می‌خورم که ۳ امتیاز را از دست دادیم. استقلال روی تاکتیک اوت دستی…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/459797" target="_blank">📅 21:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459796">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0826c8057f.mp4?token=I1OrAsNdFO6taPkvgYGOc7KI1iRr4dWAbDaK2JEjLvh-ABfk2Bj--z2Sz7hg4vLxr6RgQQxLxUuiAquIHzwAag3fbgcMuyuSCkFhUKo3dAHs67_nQe7KoLHtE_FJO4uF1vQz_hokhiBqV9eWiwiAb76z0DwrcrZILMhm53IK7ki9WDjGUUseY-0kaR-PYftI2s2yUgJdPpKraekGUdKWbT5TF-9EFZtFuMOBOK8ng4g96Os5pxUW2HU-Q_XEo2LE6RI_3k3MxfZAo_XLkIS97-HCbts001BFuWUdRwlIYp5EHf-Ma4lZPKDPD7jucDS-XTSzGHdRBD1fg5uLQYY_pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0826c8057f.mp4?token=I1OrAsNdFO6taPkvgYGOc7KI1iRr4dWAbDaK2JEjLvh-ABfk2Bj--z2Sz7hg4vLxr6RgQQxLxUuiAquIHzwAag3fbgcMuyuSCkFhUKo3dAHs67_nQe7KoLHtE_FJO4uF1vQz_hokhiBqV9eWiwiAb76z0DwrcrZILMhm53IK7ki9WDjGUUseY-0kaR-PYftI2s2yUgJdPpKraekGUdKWbT5TF-9EFZtFuMOBOK8ng4g96Os5pxUW2HU-Q_XEo2LE6RI_3k3MxfZAo_XLkIS97-HCbts001BFuWUdRwlIYp5EHf-Ma4lZPKDPD7jucDS-XTSzGHdRBD1fg5uLQYY_pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چند درصد دربی‌های جهان مساوی می‌شود؟
🔹
اختلاف چشمگیر نرخ تساوی‌ها در شهرآورد تهران با سایر دربی‌های دنیا. @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/459796" target="_blank">📅 21:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459795">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQfRltv6i7zqe-bb6cCBNPFtRxdD1Vgzi-mQQLlSVQu2ClCoOYMMFyiZ9INVIT4ZWKzLlPI8kUuMgFBL0lmpI_eyQ6A6InjCJR2cgE0SzfgrDxo-umx8SjJayGqpaS_jgvfyojknjjDsWsVWOxV0sRNBR7vpoTmnB1VgSqRvaEF4wsCwo713_9Rmga-bzEIQdaom7QyxP8l5T7nPaFy30QTph5_DVeVfgcRvVyNc6g6_t2YpuwgG5YFjmnSkul02giR-ru-LYM-ZQXajeqIVdKYayBALXKoVeedMlUdMhDLvo0wlgsDzGHg7-5VMSiwDpvXSIB2pCO6C_yZWXWbxsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روبیو، وزیر خارجه آمریکا: یادداشت تفاهم با ایران دیگر وجود ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/459795" target="_blank">📅 21:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459794">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ec4730608.mp4?token=uv7-Mjy2gZ83ni3AsjJfb_sGpKiM6QVz-7VfMrrgni5YUZpLeiyM3NRcmAWPs4j599-D_vdZzuZxn3Yd2n7Iy7E9l98kPxRCwN8kZu9SU3fBQsylKZu8jgo2Z5cDEB4LzBOVAqr3YxqUHmiuHFxs2MdNlt7ZWL1VMBshugD8_rvg5KGIBvjgLOK6w65aH1QqAgPONAC-MeRpSYfD3RQlaf1i6437t9V8FXvqPhv7j5uR2Mn-80pwCDn-bqqlVJvCj5wNtHxA_9jmC6uu279G6Re4j5_a5fjb7uOa2uDyEJAwTsYEP8ooyVVL6oTcuxjRWfLsV0Za2b5zSjtTCOK1ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ec4730608.mp4?token=uv7-Mjy2gZ83ni3AsjJfb_sGpKiM6QVz-7VfMrrgni5YUZpLeiyM3NRcmAWPs4j599-D_vdZzuZxn3Yd2n7Iy7E9l98kPxRCwN8kZu9SU3fBQsylKZu8jgo2Z5cDEB4LzBOVAqr3YxqUHmiuHFxs2MdNlt7ZWL1VMBshugD8_rvg5KGIBvjgLOK6w65aH1QqAgPONAC-MeRpSYfD3RQlaf1i6437t9V8FXvqPhv7j5uR2Mn-80pwCDn-bqqlVJvCj5wNtHxA_9jmC6uu279G6Re4j5_a5fjb7uOa2uDyEJAwTsYEP8ooyVVL6oTcuxjRWfLsV0Za2b5zSjtTCOK1ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دربی تهران در اصفهان با تقسیم امتیازات تمام شد
⚽️
استقلال ۱ - ۱ پرسپولیس @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/459794" target="_blank">📅 21:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459793">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c689a1f03.mp4?token=jTNbdw5eQdpHSaJODsLoDOA_xfAf7KIm7Liy4EiztEYLlHsxgJX4uKsHRVRPEBTsJa-nCQ-rhfaJsRA3GH3M6DbXe6Qto_TC-XSM6-8bSb3Z41mT_74gUNV253nhhP9Y4nARF45ots8_-iISLUNquEmNZGIcNlGugk5k18NmqOZDH6lyxb0KIEW_tYMc6AZJgWC4OeyuHtwAl84l_Do-cd0Fbzzs9HnF8osUrUWHsTjxhKb_DBa52kfsL_if_XYLdH0_Oa_B-PhZY_4Vq7O9KUGI9IkfmpJUh_VRt7k638tTaFp3nol0DhwhRdCkpgdX4esJFWvGhNgwM-88AU_hGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c689a1f03.mp4?token=jTNbdw5eQdpHSaJODsLoDOA_xfAf7KIm7Liy4EiztEYLlHsxgJX4uKsHRVRPEBTsJa-nCQ-rhfaJsRA3GH3M6DbXe6Qto_TC-XSM6-8bSb3Z41mT_74gUNV253nhhP9Y4nARF45ots8_-iISLUNquEmNZGIcNlGugk5k18NmqOZDH6lyxb0KIEW_tYMc6AZJgWC4OeyuHtwAl84l_Do-cd0Fbzzs9HnF8osUrUWHsTjxhKb_DBa52kfsL_if_XYLdH0_Oa_B-PhZY_4Vq7O9KUGI9IkfmpJUh_VRt7k638tTaFp3nol0DhwhRdCkpgdX4esJFWvGhNgwM-88AU_hGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تحریم از آمریکا؛ پاسخ از تنگهٔ هرمز
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/459793" target="_blank">📅 21:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459792">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-PAbX-DDA9qQaDpf-ptFGqeyGgjn7ia2l4yeKL7pQn0-ommfYWA4el9ODYI2fKMNY50toOoI4PpcT-t7eXj3miZ4mxgellyJoMM8RC07BatkFF2OQeabWXUWoBoeRd1e0uaV6F9K9_FfJv61qlc96XM3yDw5DVG4-N-ZVm1om_Y3LtNUfiVDfrUvSiJbwUeRb7lP8zYqZv1V8F4qwgrYDhi47p1U-tW30RdCNW6P61mtyaIwyvNP4VLfMg2neZSmuk-hZgXd-syAknVqOfqYA2891AQa35v4OVPY3OhD355AMbyBiUnt2QL2MbhbPey0KuiFHrFeSUPSmlP5EpSKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دعوت چین به نظم جدید منطقه‌ای در میانۀ تردید درباره ضمانت‌های آمریکا
🔹
رئیس‌جمهور چین از کشورهای خاورمیانه خواست در برابر نفوذ خارجی ایستادگی کنند و درباره بازطراحی نظم امنیتی منطقه گفت‌وگو کنند؛ شی امروز در دیدار با السیسی رئیس‌جمهور مصر این اظهارات را مطرح کرد.
🔹
این سفر، نخستین سفر شی به قاهره در یک دهه گذشته است و در شرایطی انجام می‌شود که پکن تلاش دارد همزمان با ادامه جنگ آمریکا و اسرائیل علیه ایران، نفوذ خود را در منطقه خاورمیانه گسترش دهد.
🔹
اظهارات او همچنین در شرایطی مطرح می‌شود که جنگ اخیر علیه ایران سودمندی تکیه به ضمانت‌های آمریکایی در منطقه غرب آسیا را به شدت زیر سوال برده است.
🔹
در چنین شرایطی، ناظران می‌گویند پیشنهاد شی جین‌پینگ برای تقویت همکاری‌های منطقه‌ای و مخالفت با مداخله خارجی می‌تواند نشانه‌ای از تلاش چین برای ارائه خود به‌عنوان یکی از بازیگران اصلی نظم امنیتی آینده خاورمیانه باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/459792" target="_blank">📅 21:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459790">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwnVmuHHgEgACJHxm9R4rYKxa85GBEzlbe4QYv_1G6DgdiU4SLrX2mOr3hh3BICkYFQS1lX8dFB6nrBbN1g_vu80XBI2xWhIOncFyJqUktG-2x_w5-iDHdr-uhEH4W4rrlr6rbqeGw20cYXtuUogoXBxR1Uawkj_KdrzIBGFAnfVIdnvfUT5RKOIUmem5TcqT-lcly5qfjxpNfwCByiIL3JUAMfOurTpX_t0Dv_e_eSVjMW0IOSLH9Q6Sc08bDuXMrBLwjDPnLhW70jpQa1D91XYJjKkQvAxdo5IIvgcV6Gs6WHRTJHQ7ecsejsPSyMt7Jc4MKjbvWF0s2v5gXQB6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حرکت دیدنی محبی و توپی که بازهم وارد دروازۀ استقلال نشد  @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/459790" target="_blank">📅 21:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459788">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8480d409cf.mp4?token=HAgyUkp5AzcSatYV2hCzg9oV4cLxWFCoH-egCZAmQuyrXHeDKeKZ2KF8eozZ59D42SBa9vS4h4CrpRYuzyLxNYyKNJSO-wEJZXxSbwSAmR_WF50iCCDSBxN7NAQdhN_N3Ytqhb8BezajZFfcALBbkA30xeXiv-A2bvfQwGHzyn8Goy-xuWTJ30nOIlU16pigYItA-pgtYOq68SAwwoxgXEwpRNPsMBdHwsKsNzi9PaRpPRzgtr5MTRapK2OEDh_Kj6hj9nWBQTKjZStz10yC4z7laY-Is94eoU2K_n3eIgTjCeKqYqZkURc3uPaH8s69yMGBOp9zaba8EeiessRhxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8480d409cf.mp4?token=HAgyUkp5AzcSatYV2hCzg9oV4cLxWFCoH-egCZAmQuyrXHeDKeKZ2KF8eozZ59D42SBa9vS4h4CrpRYuzyLxNYyKNJSO-wEJZXxSbwSAmR_WF50iCCDSBxN7NAQdhN_N3Ytqhb8BezajZFfcALBbkA30xeXiv-A2bvfQwGHzyn8Goy-xuWTJ30nOIlU16pigYItA-pgtYOq68SAwwoxgXEwpRNPsMBdHwsKsNzi9PaRpPRzgtr5MTRapK2OEDh_Kj6hj9nWBQTKjZStz10yC4z7laY-Is94eoU2K_n3eIgTjCeKqYqZkURc3uPaH8s69yMGBOp9zaba8EeiessRhxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت رسانه‌های خارجی از شبی سخت برای پایگاه‌های آمریکا
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/459788" target="_blank">📅 21:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459787">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f18211e5a.mp4?token=HIySaik5shU-V7bYcvGcqyfNOqK0ApOWfmTWbwS3ju4Gx2JiAzsnlI-o_pOH8ICePrOI0k6Rigi8p6aanccUXGcZEeoJQEjDcg50Jr6As2-YDc4QiK6EcmQAHX7lnwt-YtoQpMWWoPYF2MUVjWksIeVMN6ZfxswxFIjwlckTZ2mIpM527vUR-n3KZoe9W4JFtsvg5oJpo2vvKZscZtPhvs-rLqCppEcl6a-BTx5emTAwP-A_IMNLWXgeqgvyqPUQIHMzgzE_c-jiDAYy9EQ0Mmy1P05Bqe8b4s_GSmJ1J0Uj1ppzRj_VfRtzvQwcD5alFj1dvx-OLWnN_lIb4UTRy5B1DcZh1ZNNgK7sVTG_SKt5nR6DCl1Qod-6rOZvbdv5w6jio2Gp3TL2OxCCrZVVRo8LdlYNhRiOmP1tt7q7ZoKQZqj9ExV2QinwfKqMYMn_-IK4Nh4dmCpv5j8T8AMQRRAgfPW5UJ_pi6luwRki-qo757W_ZFP4vh81bS8ooz2lOhxF26Mfybq_s5V9CQ6jWg70zAzd64Q1en9t9PCjvSkWcsdsY-eWMp7_krGTqlcmkI7dkXNwgBzlnYafS_pCLzXDJp5VVWEjxm_2QTGsRkwhAHdvAoQZIZ0DzL-ePZ0X9vcy3YXlMk6nBaRzg8xqvNZSh7fGRCn5dCaYIiOhu6I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f18211e5a.mp4?token=HIySaik5shU-V7bYcvGcqyfNOqK0ApOWfmTWbwS3ju4Gx2JiAzsnlI-o_pOH8ICePrOI0k6Rigi8p6aanccUXGcZEeoJQEjDcg50Jr6As2-YDc4QiK6EcmQAHX7lnwt-YtoQpMWWoPYF2MUVjWksIeVMN6ZfxswxFIjwlckTZ2mIpM527vUR-n3KZoe9W4JFtsvg5oJpo2vvKZscZtPhvs-rLqCppEcl6a-BTx5emTAwP-A_IMNLWXgeqgvyqPUQIHMzgzE_c-jiDAYy9EQ0Mmy1P05Bqe8b4s_GSmJ1J0Uj1ppzRj_VfRtzvQwcD5alFj1dvx-OLWnN_lIb4UTRy5B1DcZh1ZNNgK7sVTG_SKt5nR6DCl1Qod-6rOZvbdv5w6jio2Gp3TL2OxCCrZVVRo8LdlYNhRiOmP1tt7q7ZoKQZqj9ExV2QinwfKqMYMn_-IK4Nh4dmCpv5j8T8AMQRRAgfPW5UJ_pi6luwRki-qo757W_ZFP4vh81bS8ooz2lOhxF26Mfybq_s5V9CQ6jWg70zAzd64Q1en9t9PCjvSkWcsdsY-eWMp7_krGTqlcmkI7dkXNwgBzlnYafS_pCLzXDJp5VVWEjxm_2QTGsRkwhAHdvAoQZIZ0DzL-ePZ0X9vcy3YXlMk6nBaRzg8xqvNZSh7fGRCn5dCaYIiOhu6I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مکتب این مردم، مکتب ایستادگی است
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/459787" target="_blank">📅 21:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459786">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7W7YtzYFG9_8i3iFisMf-1ZGW5_w0b5_CLmhc_vhsf1PFUxSDQNP23v82WEXZxHCvU0xH9JJVIa07JBkh-YspmO-Ffyp53gknx_miGXZZdaGAdF3SrII8J0CXNKiGJCtr5Yk_ucZCVmn2XPMtVtg-KHMf77kEncfFL-hj2s0Ut5H7x-Y5qdFOqa0IYZdzMIbePepVGOFAUmxti3CkGsk0XdDvZCSyWfwUWNBq8VFVRI9UBzuDZ-6GBfP4R0xAPPftdyXjH9nbFLilZiPucZGrMqRKj_E7NG_MZamucl8D7b2-6srjSNmfCGJKFnVE448WDX-Q9w_FlhkDcsHMg43w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار جدی مقام مستعفی ارتش آمریکا به ترامپ درباره جنگ علیه ایران
🔹
خبرنگار برکینگ‌نیوز گزارش داده معاون وزیر جنگ آمریکا پیش از استعفای خود با ترامپ دیدار کرده تا به او هشدار دهد که جنگ با ایران دستیابی به اهداف سیاست خارجی دولت را غیرممکن کرده است.
🔹
اما ترامپ در واکنش به این هشدار، در تمام مدت دیدار فقط درباره سالن رقصی که در حال ساخت آن است صحبت کرد و این برخورد باعث شد دریسکول استعفا دهد، زیرا به این نتیجه رسیده بود که دولت ترامپ «محکوم به شکست» است.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/459786" target="_blank">📅 21:15 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/hAc3jHeB84EP2kXLJH-vKiQXWTSupuXN1udmcpJWOnuenxt2B6UdPY9ZZHcXGlEfn2xvgudXM5csavpwOmio1DjapdfHxgsJLj5FIaUxtDhJTH_dQF636dFt8VTRE82KOHkKcice7QutT_4IKE253tqK7ZS5OSztNzoXM9V7uUOticNXtqibK75JdDHbTNRONnL7CRZWnX_zRUvMvqoL4ldJbTxys5Z0qtBDZpy5B2oBGC9TAkdPaie9c5SSnDJl3yFT3fa69YU-gq0LvWivTc_jlbrYDoPEkKY8K82VP_nKmUT9s8MOWnbv5kFibjsJTjGuAcK-VwD6et3QG4HvQA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 252K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-06 06:13:59</div>
<hr>

<div class="tg-post" id="msg-84114">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzeWAHnV56br6yYNF-Z1qAQB7OGvYqkgdY9HkIhP2pAx8yp4unH518IxnHbW2v6L-sS6kGw0N5kmaOtb7yNC5u4WntCuPso6x-z1jGj4qL9tjadK17ZG501Pkis5jEWLWtT88vU6hsa4mDVVmYAZo_pHwnyL20_m8PI0hDKUeTeTgHQvqS9S53YKeVCj_njznnx-gWswphiOBbxVU17uGivcniDYqiCjt2-SsqToQ6g5HJjjQIBJwmte3PetzPaEqgoNV7AGUrt2xSJqCdKT2lf2_SHQXyXA1Ib1vPLH2X9Y_ykcDBg_zS9IQVf9hqDS1WssV6Qxe3IhEc2nwP85DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر حیف شد وارد مارکت ترکیه نشدی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/funhiphop/84114" target="_blank">📅 01:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84112">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سلام بیایید چنلم
https://t.me/+q5Ml6Hl1Af5lMTI0</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/funhiphop/84112" target="_blank">📅 00:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84110">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/thq-3aaLuxUvqZAFr3LCW5U45Ei6Yn2q8lopfFQibscxV4uXZlkAPoNF67WcIsnekTStBDX5Y6DK2lzmXNzC5qXMqEfokDSKgBV0WiSuLwnfk_oy4ljLwiXW5J-SrkEsOrgLuFk8RmYAVrLb2V-JsBflauhG-0rt7OOsaBruVmvo1bPDS3XFJw65WxckqGt4P1pOF5DWlHZCnJ-7fJFXXsDiy3RD2Q8jeZ3V7mP2E8D50qBo2dZ2NI-lFX_uTTAJ3_AWpXyvf8j0_441sXbX4nxNVUeIKooaptKDkxP8sF7ti2QUm7NtRXnQuIHd_i6M_0XT7CKkfKdURgrW-AGAzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jJBszIRwsdv-wpF7-CDnZtMVTOdpUKm9G1eqx7u1k3j4Z29OL-dmM2xrJubwtEAvkdOi9fSJTLs7JvcRQt4dvkWbcsxJGFj7m0RLgbIhtmm0dkvQ4fncWp4s9T9ZhtWke6toW14mvu_88BhJu4YK-RAWkusyNK-JFWZJh9I-Q1ku_B5-Uwafityi31s8zpsHy4KSOcfbRZSyjjEZq9v2IJ9X96FxCGt-whL1GOzrANvso2vnaT3i56gPHuGZJIJNk7I8nd02P7FQfER7jgI08jWk4gqGjUhgSu8fw5sO70ceNJ8jhL6s3ERU9fDTePyjyxsemCX27sjXVllk-NRoOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به مناسبت شاتای جدید سیدنی سوئینی موافقید کیری اورریتده؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/84110" target="_blank">📅 23:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84109">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LoX6Q7uNpBtspPYzBkECXdk5YCXd3xdRXp0c-1_NuL20E8u-_bmOcDABG9KqbkB684CdxRX6Jo74jLApY-dopqiUdBDm8RIUprhbune0PiICObh2zpiIJ1buWjA1inVlEfrfb7XGwp22Ys7NNokMdEERrBlEPePa7AS2sK4BH5CPTAqp31DbAahDXEr1LyF2GdBAAuMiK88oS3n_tlydfnZlzMlbcnsp6ApJMYnmJRO4QOaCXS5MDhuFC5n_9ICQgY7_VxQojBu5467ZvodimPAp9DQWOrWxPJ-ovjqGmjrawt847DZeppQA0mr_qyj7QX9jaNhUfeOpS9Ap4EQa4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشبینی ایلان ماسک از آینده‌ هوش مصنوعی:
2029: ربات های اپتیموس از بهترین جراحان جهان پیشی میگیرند.
2030: هوش مصنوعی از هوش ترکیبی تمام بشریت پیشی میگیرد.
2031: ربات های انسان نما از صد میلیون فراتر میرود.
2032: اقتصاد جهان دوبرابر میشود.
2035: درآمد تضمین شده بدون نیاز به کار کردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/84109" target="_blank">📅 22:08 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84108">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔹
بدوووووو نامحدود اومد!!!!
🎉
بدوووو حجم نامحدود، سرعت بدون محدودیت!
🪙
بدوووو یک ماه نامحدود فقط 270,000 تومن!
💸
بدوووو 50 درصد تخفیف افتتاحیه، فقط تا آخر سه‌شنبه 7 مهر!
👤
بدوووو یه اشتراک برای تا 5 کاربر همزمان!
⭐
بدوووو هرچی روز بیشتر بخری، ارزون‌تر درمیاد!…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/84108" target="_blank">📅 22:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84106">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RF55owK6ZMcW6Q7ZtzVk3JbaAwAfT3Siu0sackYNTE67FrpCSWAue7T-bOGix7Z3z5_EIyX5V_swCDZerrf2lDvJPFhgs3QrH3ARs2IjdHiUqtAtHqNPWjUfvWuyzgdilU0pKI8RrewZQERTzZbJ36L4U_USjeqWlw81m389UXYrGSKZrUzaI3Fvu6aHjJOgyY-tNGbRzk6KBcUfAy898VEKkWEX1OiXmc18GYvsWFbD7WaTUWzhY3L7qY3oswC0svg0uhWS38Vdm3xi4cG3UhAiX0JpFYx5RwftnpANv9vs1ig8P854wuubKOqzwUpIW-2aL6gioSfq7oQZ2yvLxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
بدوووووو نامحدود اومد!!!!
🎉
بدوووو حجم نامحدود، سرعت بدون محدودیت!
🪙
بدوووو یک ماه نامحدود فقط 270,000 تومن!
💸
بدوووو 50 درصد تخفیف افتتاحیه، فقط تا آخر سه‌شنبه 7 مهر!
👤
بدوووو یه اشتراک برای تا 5 کاربر همزمان!
⭐
بدوووو هرچی روز بیشتر بخری، ارزون‌تر درمیاد!
🧨
بدوووو 2 گیگ تست رایگان. خوشت اومد، بدو بخر.
🔹
@BodoVPN_Bot
| بدو وی پی ان
🔹</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/84106" target="_blank">📅 21:58 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84105">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">عراقچی:
غنی‌سازی ۶۰٪ غیرقانونی نیست و برای اهداف صلح‌آمیزه.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/84105" target="_blank">📅 21:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84104">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">از روزی که وزیر نیرو گفته ناترازی برق نداریم و دیگه قطع نمیشه بجای روزی یبار روزی دوبار برقمون میره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/84104" target="_blank">📅 19:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84103">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3ce0419e2.mp4?token=QoMZWdOiLPgfPAcGBdIRWHMb9mG7kbobY6MyKlCcF6QWqQhm-G5eSfw0s8pKu7hB55sYjAH5MbXg2dlo32EfqKaSuTTxOshyiyLTtRWehRxaG-HJ7Hah0wm5u70khCX4Fyi2hjWax_AG9CMOgqsmYDLlv0mXHjWxrefExZadYhoV8wWo4HLuQYphCVCrC8hA0ZgfDdg8WOyEDL0wFimm03-H61fY_5DsgpetXXFrkQ7b_1DQqUr4oPRGW82N9J-Iytv2XjO0eYH1KTuanu7C4vZsjS9M2K6iGVt7VtYFtsuu0jD-vp8V-qUeF-nZ94t4GT57Tpd91lis6mFrm05EiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3ce0419e2.mp4?token=QoMZWdOiLPgfPAcGBdIRWHMb9mG7kbobY6MyKlCcF6QWqQhm-G5eSfw0s8pKu7hB55sYjAH5MbXg2dlo32EfqKaSuTTxOshyiyLTtRWehRxaG-HJ7Hah0wm5u70khCX4Fyi2hjWax_AG9CMOgqsmYDLlv0mXHjWxrefExZadYhoV8wWo4HLuQYphCVCrC8hA0ZgfDdg8WOyEDL0wFimm03-H61fY_5DsgpetXXFrkQ7b_1DQqUr4oPRGW82N9J-Iytv2XjO0eYH1KTuanu7C4vZsjS9M2K6iGVt7VtYFtsuu0jD-vp8V-qUeF-nZ94t4GT57Tpd91lis6mFrm05EiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی برنامه دیت ناشناس، یه دختر مدعی شد بلده یه طوری نگاه کنه، که باهاش می‌تونه مخ هر پسری رو بزنه
و در نهایت این شاهکار رو خلق کرد:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/84103" target="_blank">📅 19:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84102">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ritzobet.apk</div>
  <div class="tg-doc-extra">45.3 MB</div>
</div>
<a href="https://t.me/funhiphop/84102" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکیشن اندروید سایت ریتزوبت
🔥
🚀
وقتی شرط ‌هاتون رو توی ریتزوبت ثبت کنین ، علاوه بر ضرایب بالا ، هفتگی با کد های هدیه کسب درآمد میکنید
🤑
♦️
آموزش شارژ حساب با کریپتو
♦️
آموزش شارژ حساب  ریالی در ریتزوبت</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/84102" target="_blank">📅 19:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84101">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbeiXOpW54E46Mq-B789cQn3PcU5GSJ73PPt-Za_zwcIIxf6uEs-DyHD7rAhtpDdNbkPnft47u6-OH0wsMn6X1Xl5wD_XdVtw_r3T9zbL-BKFw0UBO3gBMewo_0YYtiSenBzhg8FueSTPnKWAQmfQOEwywqhrPRc61spEtoqMT_ytS4ChlxKG5b7v7uJd8QMc0D17iq9sxcpz-uTPJk30AlxMrAmTSU2vrWAGGT9GQ2uWfEvZLJBbLHAAUAfV56eUMV8xoOvfVO126Q1tlaLjdP_i-1_VE6d2XdCVFYkpWQh1fTH5GFVDUS6eRD-HwDSib03hTzHYhTv-oxwjCSyVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
واقعا چرا ریتزوبت انقدر در بین ایرانی ها محبوب شد
⁉️
➕
ریتزوبت اولین سایت پیش‌بینی فوتبال ، که تمام ارزهای دیجیتال رو برای شارژ حساب پوشش میده
💳
درگاه کارت به کارت امن ریالی برای کاربران ایرانی
⚡️
اینجا با خیال راحت شرطبندی کن و درآمد دلاری کسب کن
🚀
همین حالا ثبت‌نام کن و تجربه‌ای متفاوت از شرط‌بندی آنلاین رو شروع کن.
📲
اپلیکیشن موبایل برای اندروید
🌐
https://RitzoBet.com
پشتیبان فارسی سایت ریتزوبت
👇
🅰
g5
⚡️
@RitzoBetsupports</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/84101" target="_blank">📅 19:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84100">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMahdiyar</strong></div>
<div class="tg-text">کاش اسم منو میذاشت</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/84100" target="_blank">📅 17:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84099">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCMvsZaz0nxnjxaySHo2WvQrjkqewXw2SJA4D_9rvibl7iS6UqikyWcr5DHjcC3JBDQ-7qAHaJsbA2TTsA_HLDlG-swFZxj3nUoDRzYnNJez9kT-6mGk40riK-0QbBcb7Oio1zuYr7xthvbaOwuSDghgLkM0_Pfqlak5R5k6WCZq7o4dyicBkCFslX7jLeDjAQjMq1duYGV7ByowYByq6UPur39zsiD7QdHnnFqMxrtWZOvSfwiOCt24SR1kcR_mkaPtdwXthRoDfDwqqhTFi2ZGJ-VvVdbeAPkrD2A8WrpQP-ALfR99rBMviyU09XsPD9us6M8RBoC7mUuFB1DYww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ممد ناراحت نمیشه لنا اسم پتشو گذاشته تونی؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/84099" target="_blank">📅 17:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84096">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cmaCU0SmIy2zQqbaFhy9rcrKVFmV__gN7ooVlBUZnnBBEVzzUistgWvEtm9FF8-ZkUN63hL-VsbuHZbR05Vu-2LxOouzpKxAE9McXky3gHJmd9gTc9RCG7w0_XDVzP_01gDR8slcrDu0oOaGcFYwZMq-NExFfRm0YVGQ3DXnpua-QOr1cI9rIIi6Dy11ZASdfCsBILa2ajhyQbJm_jtOA26U_RbccBL8MtmTgM5HIFyrCMRQsmeslml_NbvAAhqEI23nR3BvEEgThcaSrB3orqISXPx8103kSJnbLEWrQ0blTgQqia0GRf9Oix2HxPym00PD2rhGaFjzwtKYvRBISg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DOhAwfJDhDCHwlOWWj4Yn7O-sqgRK0RbGrcJFOUNOa6q543b57yyVJRyTRcwIzyrFi3JcGF6C9d2Hy511XrATVpn7GEtqIcPWABrjQcqvQ07UNQ3BCLgf9Vl2bD7NWYWqsiBeFh7iT3nSsNVz-MyLXH_dU_fZbvPEmetVw1GmuoX7VAFnJwEcEeb8zdREH828e6f56ia4kSb0Rue0H1ZmiCYZ1ED4yk_N7Nxd4twMk3Wpk22i8pF6QbZwoz3oJmNND0x8y7JfpuZXFPNqUPtGCo5yJwhuXLwDYkXimEAXGxLg-GNTYrEbyyBm7v14SfZOGX7JLoOFuBWfK5CSlwWkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bUsrT0Dv4zjrsKyhQZGQQJcTwvHt3vJEG36G9aVpm3cX3tmBcCQZPGUt05e3XvN9V-uIG9cEVoibaSMu6kjW4J3ZgDToyGOKuxacY8GU0dDcU0zayCARcpRt613do48iPbI_y0PefQq4bOW26_EbwxqKvKvsw0fAhlf2oq4jWE86hkH_yElvEBOIf-XLaSBfZQr7VAnk_VPeoyWYxcB75mL1YDkLxp4rgFz5F0-_a6yzJBjb202k4nf8SYQ8Sc4OO7dFhjxTbXiaKA7pUDHf1QCyXQ7ZKufD5bV3qu7-oVv0NVi_48NS1AnWlXzjvjYZt0xeTuAyZqFgl7ebwUDAYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست جدید ریری و کامنت های فرزندان فهیم کوروش زیر پستش:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/84096" target="_blank">📅 16:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84095">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">هانی رامبد تو دایرکت هادی چوپان:  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/84095" target="_blank">📅 15:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84094">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqAH-YiV2TFD0bjB93Koz0NSqyL-HgaI8XhnZ1a5h4hMjiQfoDiXJxM4hq8DPt7DqendkcsVNW--3_M5NPvRPdBBg8Cz2S_sJ8dZzC9oXeoj3VWG2q_1b9RE1k_N8Cze-CS7nleS9DaLDy_PWnteFrcTPoBu1jBa3dQgVy4rxNbdIS8XDFtIazRJqT6MPlFgAhw1tLjhGgc89qFFbZBgAVvWOZGTE2xFX0FU3-MrcwQ7QpAf2s8aWztOomTjJo7TXpoTBdGyMJZ7DD-LpsFyUrVzyI8wK6UNL3obWFswRYlUwzq6eGPvXYppeWuq4g9dqxUvzgpngCJ6rusf5Pt3hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هانی رامبد تو دایرکت هادی چوپان:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/84094" target="_blank">📅 15:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84093">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b331c3393f.mp4?token=NVmQPcfUu2II0hLvOwo8ncvi8aw7fkaY4F-REyaLL0dLHOp-4X47PpO-fYssrD5674bWZ0OF5H-h8EGUlroTW_bH8IZVdXpk4yKcOkQZH7u0XWmujg0AgIaODjlflR0dPzEUcJK8UW8yr6_cpSD8-xgWEF7Zbzf68zsDMCntb3ziLV222c4aBydDIXdnHg8vTO5dtTnB-rOonsll2qts0YEd9LwgzAkDVszD6p1OWauJaUzSE-0W66hj94ZKqwiRKrsCJEewzox2QQA_tOh9kRriSB4wEiNOVbHug740Rqw_AUywbLTtdR3k0s3HqxsyvxKfK4X0H5nteDuRmwMEHIotmHuRZUbWQz0rFa7Q3CAR7AL339T-e9JtYcMve_1YweDXFZLBqR-KKrFpB0TY8lkK5F1Buu9mZBvzkI1ob_8wD9EOT4Zu2UrW7gxu0oFt2uJS3_fwGfanmLtwQU7YgF4fN5tmx3h_PPvW1O6wbXgu_fyr3XXIcu0NuqC3P_rxy4KYNd46gwNjLgy0xy-HYzJIJ_w8P8ayHbMX4V7g-SYUBYD_xAuWS1OmpVG7FHKojiwhz5TjHEJ9oPc6Tp17eZcOnI0-rUzXNDePswPNhpcIU6KPjtveKf3EjCzxsarVji3qTibCo_IEC2nSyafZ1PrBwY3Oz6gDC6j887vzZBE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b331c3393f.mp4?token=NVmQPcfUu2II0hLvOwo8ncvi8aw7fkaY4F-REyaLL0dLHOp-4X47PpO-fYssrD5674bWZ0OF5H-h8EGUlroTW_bH8IZVdXpk4yKcOkQZH7u0XWmujg0AgIaODjlflR0dPzEUcJK8UW8yr6_cpSD8-xgWEF7Zbzf68zsDMCntb3ziLV222c4aBydDIXdnHg8vTO5dtTnB-rOonsll2qts0YEd9LwgzAkDVszD6p1OWauJaUzSE-0W66hj94ZKqwiRKrsCJEewzox2QQA_tOh9kRriSB4wEiNOVbHug740Rqw_AUywbLTtdR3k0s3HqxsyvxKfK4X0H5nteDuRmwMEHIotmHuRZUbWQz0rFa7Q3CAR7AL339T-e9JtYcMve_1YweDXFZLBqR-KKrFpB0TY8lkK5F1Buu9mZBvzkI1ob_8wD9EOT4Zu2UrW7gxu0oFt2uJS3_fwGfanmLtwQU7YgF4fN5tmx3h_PPvW1O6wbXgu_fyr3XXIcu0NuqC3P_rxy4KYNd46gwNjLgy0xy-HYzJIJ_w8P8ayHbMX4V7g-SYUBYD_xAuWS1OmpVG7FHKojiwhz5TjHEJ9oPc6Tp17eZcOnI0-rUzXNDePswPNhpcIU6KPjtveKf3EjCzxsarVji3qTibCo_IEC2nSyafZ1PrBwY3Oz6gDC6j887vzZBE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی یه ویدیو از پابندش گذاشته با کپشن"یادگار دی ماه"
و حالا کامنت های مردم:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/84093" target="_blank">📅 15:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84092">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">بانک کارگشایی یک تن طلای مردم که دست میلی گلد بود رو بالا کشیده و میگه دست ما طلایی نیست، حالا میلی اومده به محسن رضایی نامه زده که پیگیری کنه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/84092" target="_blank">📅 14:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84091">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J8VVWgnuTeOptrgwxJwUbvqMmLeat8ysPG6-xSPKNUwqk-eCxtV7b61o-yt3jUz9HLxpDksvxtD-UuLLbhI-3lGNNxhw0xcUWgmAQOm9FKA1z2x2gI8xmH1nWfiRwlC0FDorjFo78g4PkOqtz7lrAyrfqT6jv9kEEXevYVb9Be5JmCCbgix0WiQQP3gO8JxvYSQoWYv8s5yUTwwlGFPkrWrstC9Bb6h30K1iFsgQw9NUKPijb1igMEfgQJEkXhwjtJ3dz5QRYAOi-TRIKTg3ICUoeH60xSazlIs-zPPJui3ZGnkc66LgtaCIHBp5fGkrWjQ3qSRWxjkt4eJyy4DM3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک کارگشایی یک تن طلای مردم که دست میلی گلد بود رو بالا کشیده و میگه دست ما طلایی نیست، حالا میلی اومده به محسن رضایی نامه زده که پیگیری کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84091" target="_blank">📅 14:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84090">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ed7tXJY8lkr5DmUaMhMTwwVpprgXOMoDK7dopQjw82VvFIqV4lHNpCv64EeIcMVldXsdyvRiPTqFmKFc2MXl_qrMPb4Kp9baMa5kG13CbbV5QNZtLLTQ_cOm1tsssAner0l46Yg88ME3g4sjQKzPlqhIJMnwr461tiJjkljp7vppLOGLlIQIhUWs1hR6DwKBZoJzjvqvlCfs_zc2GSCXYRe1RfD1MMeRuSrEFn__DG0Eu6S99Sj4iESGtyolHn0oIVpwimTd7vSyzEKc7JELyAwnrkjyNSY2Vb3QRaR44AJgZYYT9v7n5hpwmfr6nGMmOLywq-a-NIX9IX4nddWFuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد همین نیما و دارو دستش تا یه چیزی به آرتیستاش میگیم میان میگن نه هیت ندید و فلان، وقتی ما میگیم هیته وقتی اینا میگن انتقاد سازندس.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/84090" target="_blank">📅 14:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84089">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e6331f6cc.mp4?token=DfogsyLfCIU1jhlwc0ElaP-3OPts2bDGScpRemBPsF-V3YjK1dqCtlwIF9kcwHwaexAhcRyxytu2ZS-1N4yWbZQPJj3ADNZWHEM7xJ0XOJpXbJ9LLuKkmdBYAgG1blsptLhh5sbagZRNIVFvg1uubc2ROULi8_Jyyv9R0JnyMLhtfHA5B57O7HLxey5rsrk-Hbh2myJbzP0bEOv-icQ9zYiTwJ20Fwk9jVA4S7E4_IgodMolnZzLNUoQoyo_6SNgHXihHvMDgrszELCoG5PqfV8fQxklGkE8MYP3EyzFM5OGEnDDjD2R3AeFuujpRSKP2rACtt-PJpbH49Cp8jYAfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e6331f6cc.mp4?token=DfogsyLfCIU1jhlwc0ElaP-3OPts2bDGScpRemBPsF-V3YjK1dqCtlwIF9kcwHwaexAhcRyxytu2ZS-1N4yWbZQPJj3ADNZWHEM7xJ0XOJpXbJ9LLuKkmdBYAgG1blsptLhh5sbagZRNIVFvg1uubc2ROULi8_Jyyv9R0JnyMLhtfHA5B57O7HLxey5rsrk-Hbh2myJbzP0bEOv-icQ9zYiTwJ20Fwk9jVA4S7E4_IgodMolnZzLNUoQoyo_6SNgHXihHvMDgrszELCoG5PqfV8fQxklGkE8MYP3EyzFM5OGEnDDjD2R3AeFuujpRSKP2rACtt-PJpbH49Cp8jYAfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسئولین لیگ برتر به تاجرنیا گفتن خب قهرمانی فصل پیشو میدیم به استقلال ولی به کسی نگو تا موقع اهدای جام که نتونن اعتراض کنن
تاجرنیا چیکار کرده باشه خوبه؟ اومده مصاحبه کرده گفته به من قول دادن جامو بدن به استقلال، حالا کل تیما دارن اعتراض میکنن و احتمالا دوباره کنسل میشه و جامو نمیدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/84089" target="_blank">📅 13:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84088">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ritzobet.apk</div>
  <div class="tg-doc-extra">45.3 MB</div>
</div>
<a href="https://t.me/funhiphop/84088" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکیشن اندروید سایت ریتزوبت
🔥
🚀
وقتی شرط ‌هاتون رو توی ریتزوبت ثبت کنین ، علاوه بر ضرایب بالا ، هفتگی با کد های هدیه کسب درآمد میکنید
🤑
♦️
آموزش شارژ حساب با کریپتو
♦️
آموزش شارژ حساب  ریالی در ریتزوبت</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/84088" target="_blank">📅 13:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84087">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCPN8SZonrxTkfx4EkO2Vzm2bvsBCVRqs3LYWYCh41AFZ1TLMPeRuLue81e9QpvlfavJSw3F8XPKwAokFu7maHgQf6YrtnriKl_A2IWEsfBMIiHeCgV67PgXXLqomUBkdAg_MPCGjmAJeVlfqtl1oa9_SoM85aWyZ7JZ_6fxHCi8HRVrQRnUECDaQAYLJVCajQc21Pl6x_CNoSwAfbqWVxVVox8jtgb2TIPS6NqcO8csSPzpPNAu9cOmLH4wHjGRDmpPvIN5hhGUXGeXS935Wt5luGWmNjX-LeS4if5a-6ZSS3YPBZCyRHjdjLZfx6ur598A5Oy9VS66Th72mAmctA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
اولین پلتفرم جهانی و اسپانسر لیگ هلند در فصل آتی فوتبال محیط امن و حرفه ای برای عاشقان فوتبال و هیجان
⚡️
واریز آنی با کریپتو
⚡️
تسویه‌حساب سریع و مطمئن
⚡️
دسترسی آسان و بدون دردسر
⚡️
محیط حرفه‌ای برای شرط‌بندی و کازینو
🚀
همین حالا ثبت‌نام کن و تجربه‌ای متفاوت از شرط‌بندی آنلاین رو شروع کن.
📲
اپلیکیشن موبایل برای اندروید
🌐
https://RitzoBet.com
پشتیبان فارسی سایت ریتزوبت
👇
🅰
r5
⚡️
@RitzoBetsupports</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/84087" target="_blank">📅 13:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84086">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q16l01CFkXPAmYwNlcVvBnGDZNI4d-m3jQ6ukz4zBtPfV4b6frrAJE4BedjkPqg6M_ywJxpXkUE-dkdx5WoFtxQ-yVHXx870aaoQLGjunHNVFQi0ra4BkcGZfnGNKuTNl-4rjaf-imv7ufgMkhDatjEK3e7GmaaJSocPbnVSixQ6dSOYU6Pu9mM49GUFPwurDYsFFCrn70ES_xFBG3SgJNTrgXCl6l352wxaAzk9qcgcQJFGm7Zd-HPg2IIMQOXBbQDQz0qMc-qCBx7Hh1jqfYlN0fUJlyFVJaBgqdIjPO2QCJScut4V2sOyHdoMLKThqdei_Csl0-y5NyhY61e_Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسطوره حمید رسایی برای اینکه سال ۱۴۰۲ تو کانال تلگرامش به محمدباقرشاه گفته بود دیکتاتور، الان داره می‌ره زندان.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/84086" target="_blank">📅 12:53 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84085">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6182180c47.mp4?token=svi8uuGdpsVjGJUY0MaQolK1OcZonXlArvL9ZW2tE1-wXHtj9R-lS9EL_WlIGYuG_05c2Ujy4XdWX3D2WskHkvpMivFboTPDnaZihlRnJIyD8rhlYz5qkNfVFyQB9khfyINzpea--6DqKfKB53X7Lf6oRBIRD1BsQPLDWZyycw1TXec6JdMnZJirzpC5axmQELbMLAYivvW7GuoSV5F4uIZvpNDTTnaJ8TidyxB-QWCsFlu1--tbeVqi9YEiJteMllWi7yN7NQqV277EDeUiYn4od7Ad0104hWTJmt9ySwER-a6SW49hxNigAhFub7eX_xnfzUvlEp_SEA-rFOHTfH377R_db_HvgiLsy5OuGPfMKDJnOLCEuAvU84Cj_8pxKOtj48JeJ7SDAiPJqBfjzPCFgV_KOivQoav8FjIRjOk_iHgXm9Nb8TqfQZGXFPOM1YR1c4QmaAzMP87rumKwwi2Cfd0LO7fqyXE3P77uuGMKy9oEE-7Uzkaee6DxQazd0Zz1QGFAne6Ex2wgBrCKez0h4lzaVbPbEXuxQ80fVbgcpJZlShpQW1h35CLfMid4BjthzvmdE__UOv_R-nfucly1rhQaWAr52lC-cBrUDVbiqtfdG1Giur5WPzXcQITSnKSwnff7eLeWNA2W8UTPrWUk1MmsK1mzwWtvNm8AFZk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6182180c47.mp4?token=svi8uuGdpsVjGJUY0MaQolK1OcZonXlArvL9ZW2tE1-wXHtj9R-lS9EL_WlIGYuG_05c2Ujy4XdWX3D2WskHkvpMivFboTPDnaZihlRnJIyD8rhlYz5qkNfVFyQB9khfyINzpea--6DqKfKB53X7Lf6oRBIRD1BsQPLDWZyycw1TXec6JdMnZJirzpC5axmQELbMLAYivvW7GuoSV5F4uIZvpNDTTnaJ8TidyxB-QWCsFlu1--tbeVqi9YEiJteMllWi7yN7NQqV277EDeUiYn4od7Ad0104hWTJmt9ySwER-a6SW49hxNigAhFub7eX_xnfzUvlEp_SEA-rFOHTfH377R_db_HvgiLsy5OuGPfMKDJnOLCEuAvU84Cj_8pxKOtj48JeJ7SDAiPJqBfjzPCFgV_KOivQoav8FjIRjOk_iHgXm9Nb8TqfQZGXFPOM1YR1c4QmaAzMP87rumKwwi2Cfd0LO7fqyXE3P77uuGMKy9oEE-7Uzkaee6DxQazd0Zz1QGFAne6Ex2wgBrCKez0h4lzaVbPbEXuxQ80fVbgcpJZlShpQW1h35CLfMid4BjthzvmdE__UOv_R-nfucly1rhQaWAr52lC-cBrUDVbiqtfdG1Giur5WPzXcQITSnKSwnff7eLeWNA2W8UTPrWUk1MmsK1mzwWtvNm8AFZk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیک واکر با شکست سامسون داودا به مقام اول مستر المپیا رسید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/84085" target="_blank">📅 10:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84084">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmHfL-AY2C6nZjYfU_-5tAX_IST-7XlStX7Uqos5IAJU2S6eRtCqyEaWFL4509H5C4H2HT_csOh7PplWQwxdBlwWQHNHVbUn-RUFaAhKp9tMm3wrQjpNRcHrmTMNbiTRZE9qu-JFvq7i_wYAxyXzocqOHveDVsnOiGpF-ljfpojiNY3KyvN-3O_MjaOqfZa4IWYAlouvi4PrfAZT6xCij_hPXhK-R_DDMSGlpVet4042C90r-paqY4fctyj86jVT8BOVjvvpl1pReZNnjgslsI1Z4b7RPFSlDxZSb0Plk1jZSVMF80ihybPuINtw1d59Ri7RnkpdqvAyIF2t-ErNpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلخون بد جلوعه حاجی
ناخوناشو تتو کرده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84084" target="_blank">📅 09:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84083">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گوگل ایران رو تحریم کرد و دیگه نمیتونید جی‌میل جدید بسازید.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84083" target="_blank">📅 03:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84082">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">این باز مست کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/84082" target="_blank">📅 01:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84081">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVHcYpWKM6hSAH2hI5laYELEeg9wk4HhBnUgvoP2AzyvdBBhjns0CWohAu1r6il2xGHSjGWQmOVHvlhjWTD23QPbzyc7cWW4r6RUzuFp99dZ2pd3FzDsHAXM_6LVf8AW_wyWF851phVI91WZYKq0twKm3R49r3PFxND-NAfth80m7Xgxt8gMUIzlzR_DGAUGLXBqcOPBSZq3MtJl4ln7M7np7tMgOevWIE_drX-A4wU5h0LOfHx1fbKOi9kaWNcBCCurc_3XZuUKi34opTE39FjLHinQ5mBfVYV3pDYFLZKcYekZdX9IIdy0Q-4woWGrEqQHh9_VnB7jLLg0hDBaeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا رسما هرچی تیم اسم و رسم دار تو دنیا بودو تو سه چهارماه گایید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/84081" target="_blank">📅 00:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84080">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">تنگه هرمز بکن بکنه</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/84080" target="_blank">📅 00:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84079">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSEFdJ_zJRzb0z_Mp0VO0gQNfgiRHaAvSATxDq8yQoBXeWNoN2r9xz6A9CBxb3q3MbYwB0LOTmwTJKhuV2I0nXd2gAqXN8uGwyvOi_ZjwACfEHaHO_aKsIQMKdLI2a93zjCTbioM1rBbgzb8zJD6QFm_ad5YFHmoV_oDyln5fnP0x57tEsNIjcaHm-7ka68P7t74xac_VvPR1QS5QMV5pnUky5TPNvSlF-13a8JTeRXO0aKi_yXS0Iolxyuznsxc8OzQAIxKB0Ro_TYezB4mD3RNqz1CiossV2vHkwEZYZxklKPH3WCZ5DJvyyXiT-mVlmUNm1HDmSFtsnHa_0Rp7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مترو مناطق
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/84079" target="_blank">📅 23:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84078">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">کوکوریا زنتو گاییدم</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/84078" target="_blank">📅 23:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84077">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">آلبوم جدید پیشرو و تهی به نام "رفیق" منتشر شد.  YouTube   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84077" target="_blank">📅 22:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84076">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بابا کیرم دهنتون بچه ده ساله هم بلده که همراه با یوتوب از ساندکلاد حداقل بده بالا، شما با ۳۰ سال سابقه بلد نیستید</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84076" target="_blank">📅 22:42 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84075">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJBg6Rv0dhF_B36mGrSbJADQqwuZV4yzQyLRq1SqBfknZf03sz9cdl8lnYcXImsTItFguwRF2swfEVjq6snu_zcHMSYVtJr0OGj-OKiFJaKrO9fqSwReiNXWj9JPAxUjsCvkB6jvdg772mpJ0W_ml851XKUiU_BX-wJfRfLVv2kRT1a9zgNs7AzTQxtQ-7A8GJGJ7LxO1VSh5ajMGPpH5O6O2jHTa5XuKgQ-_DmahmROEpxl42-80f18_W2FYR1EKt31S13_roNfuS_dCaQkHAYT6PrltWWW8_pFrEy1peUJ2ASx8SvcC4phqaY3cy2yk6SdBCwHVhoR5fiQqOXmww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید پیشرو و تهی به نام "رفیق" منتشر شد.
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84075" target="_blank">📅 22:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84074">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">پزشکیان:
نتانیاهو زورش به غزه نرسید بعد میگه میخوام حکومت ایران رو عوض کنم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84074" target="_blank">📅 22:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84073">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/1a8faead30.mp4?token=VKFcTI8ND4vVc0BBCxOV-WqJyQjKg2PWkWjHthzJppI3PQGxI9Dd-LLNDMwpLRRGCLY5K2tO_yzgCb8pSgxH3-eagCHgij9WcZuEXLCkM-G6t2zgv3bXVbz645--lf5pKmCZ4Gzy3ZhpcKPyTOvubrgC1TyQfIsRm1ga_I_kPNBfUOib9XALfIUL60OW4azB7jZMq8lEBEHCXaSSHhWInIoCV7KL6rbKX6NwWHWcoR6e3ZAQk9LGKYi1vi_aUIwUIlVz9b2OOUH7THfY_mEyj2d7SYpKDQNnCWvMobHZXGaY0EyEcW5JIVFjrF_jS3FJfvJDGk8FKzPFd5DAMJkDPg" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/1a8faead30.mp4?token=VKFcTI8ND4vVc0BBCxOV-WqJyQjKg2PWkWjHthzJppI3PQGxI9Dd-LLNDMwpLRRGCLY5K2tO_yzgCb8pSgxH3-eagCHgij9WcZuEXLCkM-G6t2zgv3bXVbz645--lf5pKmCZ4Gzy3ZhpcKPyTOvubrgC1TyQfIsRm1ga_I_kPNBfUOib9XALfIUL60OW4azB7jZMq8lEBEHCXaSSHhWInIoCV7KL6rbKX6NwWHWcoR6e3ZAQk9LGKYi1vi_aUIwUIlVz9b2OOUH7THfY_mEyj2d7SYpKDQNnCWvMobHZXGaY0EyEcW5JIVFjrF_jS3FJfvJDGk8FKzPFd5DAMJkDPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو کرمانشاه یه مخزن سوخت خارجی F-16 Sufa اسرائیلو پیدا کردن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84073" target="_blank">📅 22:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84072">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گوگل ایران رو تحریم کرد و دیگه نمیتونید جی‌میل جدید بسازید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/84072" target="_blank">📅 21:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84071">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e520cf397.mp4?token=oH3bryFIKcHvObTfodCB3uqZMPU7p8PAjuVzOMd7aT8RqWc1S_diMFjRwaM77aEPN-bShNWDrTkibqZI47shlwiCFmqEAF6Xpq7qQyugehQD-KSUyttKtsoUd0u7RjvZ4I7HDEc5rCrXRN09m4pUFTLcfe66hQeVgw5_2QBqIETSgIsvYg7I91osfe0wwKPBhGGYOlDBdGipFzhIC7Lv1oQlIR3c5xQNGTtFf057c43bB0ZSpWELWpopGL2XRQc6LKKiWD6yZqEuHZuqtGLeFsBU0dne17wF-u_n1ncJmDeN_ckJi1tvCx84y2fO6SubeP6yZ3AkbU-VLSztVw5hTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e520cf397.mp4?token=oH3bryFIKcHvObTfodCB3uqZMPU7p8PAjuVzOMd7aT8RqWc1S_diMFjRwaM77aEPN-bShNWDrTkibqZI47shlwiCFmqEAF6Xpq7qQyugehQD-KSUyttKtsoUd0u7RjvZ4I7HDEc5rCrXRN09m4pUFTLcfe66hQeVgw5_2QBqIETSgIsvYg7I91osfe0wwKPBhGGYOlDBdGipFzhIC7Lv1oQlIR3c5xQNGTtFf057c43bB0ZSpWELWpopGL2XRQc6LKKiWD6yZqEuHZuqtGLeFsBU0dne17wF-u_n1ncJmDeN_ckJi1tvCx84y2fO6SubeP6yZ3AkbU-VLSztVw5hTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تروخدا نه  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84071" target="_blank">📅 21:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84070">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWIrA4YFSWDItUwLLIT8IabLPkIuRoWKxOux4vlIDpveMPmQnVOiUusFWMexxCcsaXCfqnQXRi9hE0Z258Bv_4P7J2QolWe82U1XG-8FGZ5da5hbXsloGkVBuxog6Ma54g4IJBf_OtBmw3UbH4d4KI9lQAhhkHtEbhx2vbgTuKcn1nFeP3wsRKGztKkHP3awL8j468lVGpoBf25zAnIEM9x8-lkNYa-h9D7M2ux9U614vmdThyqneP541pdPTYqb4wYy5BnHLQV7oO2ksoNi749w011jne1wGjkqDK6fnODWIHL2Hzkq9Uz7FCOjJqWtdxeu72pb1e7zQekoYwPWyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تروخدا نه
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84070" target="_blank">📅 19:56 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84069">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">یه مردی رفته بالای ضریح امام رضا گفته من ۱۰۰ میلیون واس زن مریضم نذر کردم الان فوت کرده پولمو پس بدید
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84069" target="_blank">📅 19:42 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84068">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/152539b735.mp4?token=SZjMuXpMoJxq6TNn1xabdDyq_0zBf68voRN_5tAGfExBIDKXhM0_7BgPpfsop5vJ4fkDWjEJwlVf0xRQrptP_4KXn3WG-zTRlnN3OxDYyz8PG4kSAuaFf9IqnvtPv1DPz-FvCnIS78uOUkNvbkO0EW9oEFaW_T0RgYOCgDthQsVEZBQdqa1SSU-dJX0qSPPuYAPOKj4zjcHZdRWNhoURf17ic9qi976DxmsdNAy5wUINRSuth_1a_FkHc8Y1zYTxKAoiOsSklBRrBl1maSMqc-O_T996O8TftrNAZWT5qr-1PibxLSAZlLr6ZNDFQrkLQ0B7F-sD4QmZUlHquYV6ok7218AvOEBMd63OA2hvCVtFupIUBeN0hSylbeUMrDRMIcoOeqET7YwA4RLx-pDnV03GLv-Eax3CXXy9V43XUd3L-HdZGvqeCwdNitIVKY5dpdCHtEYcw2VXoj40Bc47sKjKc7fCqDbeqK0IQ2QN7t9m3G-EYct3NBf5e4jrzLvug69R98ME59vdArdJDz6v0xoYfaSj6CZAkfYW9Kj7vNmoCrRSErmJxj_GzLJtWFeVyCgkBq4iHxaT4CgUSdNIsyElWbiXvlXpsJslcHWWajyWF8PeZLBuzsXz2LWY4w5xOqhRpxVCNKFfpzms-KFTfKx63cHD_e2LQHcPDTfoob8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/152539b735.mp4?token=SZjMuXpMoJxq6TNn1xabdDyq_0zBf68voRN_5tAGfExBIDKXhM0_7BgPpfsop5vJ4fkDWjEJwlVf0xRQrptP_4KXn3WG-zTRlnN3OxDYyz8PG4kSAuaFf9IqnvtPv1DPz-FvCnIS78uOUkNvbkO0EW9oEFaW_T0RgYOCgDthQsVEZBQdqa1SSU-dJX0qSPPuYAPOKj4zjcHZdRWNhoURf17ic9qi976DxmsdNAy5wUINRSuth_1a_FkHc8Y1zYTxKAoiOsSklBRrBl1maSMqc-O_T996O8TftrNAZWT5qr-1PibxLSAZlLr6ZNDFQrkLQ0B7F-sD4QmZUlHquYV6ok7218AvOEBMd63OA2hvCVtFupIUBeN0hSylbeUMrDRMIcoOeqET7YwA4RLx-pDnV03GLv-Eax3CXXy9V43XUd3L-HdZGvqeCwdNitIVKY5dpdCHtEYcw2VXoj40Bc47sKjKc7fCqDbeqK0IQ2QN7t9m3G-EYct3NBf5e4jrzLvug69R98ME59vdArdJDz6v0xoYfaSj6CZAkfYW9Kj7vNmoCrRSErmJxj_GzLJtWFeVyCgkBq4iHxaT4CgUSdNIsyElWbiXvlXpsJslcHWWajyWF8PeZLBuzsXz2LWY4w5xOqhRpxVCNKFfpzms-KFTfKx63cHD_e2LQHcPDTfoob8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ثمره های اون میلان رویایی ۱۹۹۰ تا ۲۰۱۰ دارن میرن دانشگاه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84068" target="_blank">📅 19:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84067">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ritzobet.apk</div>
  <div class="tg-doc-extra">45.3 MB</div>
</div>
<a href="https://t.me/funhiphop/84067" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکیشن اندروید سایت ریتزوبت
🔥
🚀
وقتی شرط ‌هاتون رو توی ریتزوبت ثبت کنین ، علاوه بر ضرایب بالا ، هفتگی با کد های هدیه کسب درآمد میکنید
🤑
♦️
آموزش شارژ حساب با کریپتو
♦️
آموزش شارژ حساب  ریالی در ریتزوبت</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/84067" target="_blank">📅 19:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84066">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e5a082c92.mp4?token=sXRGggI8Tpbq9AowJAAGaiF66BdbropU1Q4oHxc-mpkDzRxqycMWWM2TFrYVlPXt4TAa3we8UrI16CgVoT3a18h9MBx5jIOFT3tj-YHhZ3I4MYkEDZJjF2ZpMuIQZ8A3_MJnxRcE3G592CpTAxwupbK564c3jQmQ8Y-oD_VSIo_dpxMbbGjD0yS2WDOqduT9RE63_5Ief0Ms3uPn1fUiUfM5ecMG4U2fPY0qQl_m6yVnr3hj6CLHstqXeCwJycQPog2N_GG6WWttWmNSDgjqdApynQel19rO7_Fy_yjDRgvvOktkk4fQzW2ohDp41DXjJLaKW4X1pPxnnzuBascWc5OGcfRPr1TGkyQ_dhQnpEAopfqXGPg2aquS8-Q3up9sC9OAkYkWpNXYXDwob6ndcYDQWjhQX16hpSWMmb6x9EZkRtvG7pBYQcCCJ0sPxOmS7hn3e6d6JEoMLKsv2-Ul_qH_Dsx7hoCmOuRJELt29woE8WepQtv7FgdnHEK8FBz8JAJ8NhCbyrD-L6FD7kSXl214ReAGWXQz2FD3PAqmJM8MljO6RTCnBXxSGizQzr7i4-SjlgdpIvr_fx23HhK9fa6feVrgzR0oHJROJppwihgC_BrDswRv6LUSRgRvMyA9bBiKLaTOZTmbZ9HSZ6zqodHBzADrncgnyuV938--pgI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e5a082c92.mp4?token=sXRGggI8Tpbq9AowJAAGaiF66BdbropU1Q4oHxc-mpkDzRxqycMWWM2TFrYVlPXt4TAa3we8UrI16CgVoT3a18h9MBx5jIOFT3tj-YHhZ3I4MYkEDZJjF2ZpMuIQZ8A3_MJnxRcE3G592CpTAxwupbK564c3jQmQ8Y-oD_VSIo_dpxMbbGjD0yS2WDOqduT9RE63_5Ief0Ms3uPn1fUiUfM5ecMG4U2fPY0qQl_m6yVnr3hj6CLHstqXeCwJycQPog2N_GG6WWttWmNSDgjqdApynQel19rO7_Fy_yjDRgvvOktkk4fQzW2ohDp41DXjJLaKW4X1pPxnnzuBascWc5OGcfRPr1TGkyQ_dhQnpEAopfqXGPg2aquS8-Q3up9sC9OAkYkWpNXYXDwob6ndcYDQWjhQX16hpSWMmb6x9EZkRtvG7pBYQcCCJ0sPxOmS7hn3e6d6JEoMLKsv2-Ul_qH_Dsx7hoCmOuRJELt29woE8WepQtv7FgdnHEK8FBz8JAJ8NhCbyrD-L6FD7kSXl214ReAGWXQz2FD3PAqmJM8MljO6RTCnBXxSGizQzr7i4-SjlgdpIvr_fx23HhK9fa6feVrgzR0oHJROJppwihgC_BrDswRv6LUSRgRvMyA9bBiKLaTOZTmbZ9HSZ6zqodHBzADrncgnyuV938--pgI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
اولین پلتفرم جهانی و اسپانسر لیگ هلند در فصل آتی فوتبال محیط امن و حرفه ای برای عاشقان فوتبال و هیجان
⚡️
واریز آنی با کریپتو
⚡️
تسویه‌حساب سریع و مطمئن
⚡️
دسترسی آسان و بدون دردسر
⚡️
محیط حرفه‌ای برای شرط‌بندی و کازینو
🚀
همین حالا ثبت‌نام کن و تجربه‌ای متفاوت از شرط‌بندی آنلاین رو شروع کن.
📲
اپلیکیشن موبایل برای اندروید
🌐
https://RitzoBet.com
پشتیبان فارسی سایت ریتزوبت
👇
🅰
g4
⚡️
@RitzoBetsupports</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/84066" target="_blank">📅 19:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84065">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">حاجی جیبارو بچسبید پیشرو میخواد پک فیزیکی بفروشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/84065" target="_blank">📅 19:18 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84064">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDvjG7WeKP0iQg9dlabdgL_c7o6harLfyazFjd3zWBoHJEq_FwNIr5tbwPP-kiKtVm50JGmq8FR0y1w3aMbl5a-S1oucvtknLFy1dFHeChhlf_FQQsriDFcAUJpNL95hf6sb5G1DrGP1ELfcXCQFm17MtfCFOzJPhO7pdG2x5wFMFvU8gShlTxDYzV8Bp-1Glx2xabkoYHqx1iwqwgSPykIEN-8xcGoY_wOhBtJfh0Tu3XdfcYxyE-zvcR-cLzBOVdZ_98RC-9fgsU65ljlzeXOaj6Kuy2zDpJRhdlyK0VP4UrrCXV79Zz6fmxI7xb0QHo8hlX8DlpX794V4FAfzDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تورو خدا یچی جدید بگو پیرمون کردی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84064" target="_blank">📅 18:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84063">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">رضا پیشرو و تهی امشب آلبوم میدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84063" target="_blank">📅 17:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84062">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDYkEqLg6YnR8FWVoO_7se-XQM-xHiwEwcxYimVC45xJfLnGPObsUylYn1qp4dGdWnGDOtpThcR8_ErRwEWNUxCVGLbDb6xS0Is5Kk2W-5VGV1CJn934ytHdYt1O574hY7AwWon42_4JnQIAZCNdi16dr2f7-dHeu8CVG6wBK2euKJ2YQHVfdjBa1djbygkxlTl_kNHWuam4lysgmt9pBYflByi3mqn66fFT30pgQ77M7R50-JtfzgIrFFoYZRAELR1ek1umFn2hQeNQKB6Bf1PXrLGGH05TfmeFxshTMnQIeiYqtWbsT-pZx59STvTQh6JjehT-hD1-Ut7t2CTiNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست بسیار شوکه کننده و بحث برانگیزی که ترامپ دقایقی پیش منتشر کرده است.
طبق بررسی و تحلیل‌های بنده، حتی احتمال تعویق هم ممکن است وجود داشته باشد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84062" target="_blank">📅 16:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84061">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">داریوش تو فری استایل جدیدش تحت تعقیب کمپ اعلام کرد بالاخره ترک کردههههه
🔥
🔥
:
انقدر پاکم می‌گن نشیبولوسعتاااان
🔥
او همچنین در ادامه‌ی بیف قبلی‌اش با هیپ‌هاپولوژیست، به او چند تیکه انداخت:
کونی، دکی فقط داکتر دِرِه
🔥
راستی فکر نکنی لندن پارک‌ها سیفه (احتمالا به دلیل افزایش جمعیت مهاجران غیرقانونی در انگلستان)
🔥
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84061" target="_blank">📅 16:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84060">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اونایی که فک میکنن سیتی جریمه میشه یا قهرمانی هاش پس گرفته میشه، یا نمیدونن شیخ منصور کیه یا هم ایکیو زیر ۶۰ دارن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/84060" target="_blank">📅 15:54 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84059">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ری اکشن خنده بزنید تا من یه جوک پیدا کنم و ادیت کنم اینو.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84059" target="_blank">📅 15:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84058">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac6696481c.mp4?token=UA8PZJQ9m_FKjTZEf9u9RC8RxfUaAKm3tQ2gwFymOQrIKJFSK2KHStWx7BIVzTVD30Jno9ut9-Zxv7wKbCjGNolhpgKvkUI-TjfAc_MGVO1h0fi9zVg3M1FBtQegx6ImdouXFCZA5gABZGXT1NKGTx-Cnn8HKj3tIhgmk-QgrsyOrqJoRoY_tW5TpL-skvs7NG0yew2HjUJLvW5Rxh-5i4AHKZeP5O2pWLKdzAk-h7db79_qtRYOwY0iHEvb6JKRjXdyZdQkPxrGzounKhM--_fAUrHCz50Qbz8RXZ5PsT1SvMkO1GaJCyN4IXQ-zSOwJj9bEP7wHRN5dUroFzx6dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac6696481c.mp4?token=UA8PZJQ9m_FKjTZEf9u9RC8RxfUaAKm3tQ2gwFymOQrIKJFSK2KHStWx7BIVzTVD30Jno9ut9-Zxv7wKbCjGNolhpgKvkUI-TjfAc_MGVO1h0fi9zVg3M1FBtQegx6ImdouXFCZA5gABZGXT1NKGTx-Cnn8HKj3tIhgmk-QgrsyOrqJoRoY_tW5TpL-skvs7NG0yew2HjUJLvW5Rxh-5i4AHKZeP5O2pWLKdzAk-h7db79_qtRYOwY0iHEvb6JKRjXdyZdQkPxrGzounKhM--_fAUrHCz50Qbz8RXZ5PsT1SvMkO1GaJCyN4IXQ-zSOwJj9bEP7wHRN5dUroFzx6dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84058" target="_blank">📅 15:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84057">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cd947a5c3.mp4?token=girMi5O6buqW9rLT_DQstbD3ZBBqPF1MoYHQw1Zx22Y1L22xEDqvcIRRM6EKJTXgwi_vP8P1re8zp6HPIGp_3B2S5oYVGw7b5zyA1SJGBrGkqkQL87i-TbyQ0y-_6ugzXUOrdFrdsA62v7yoJT9PQl5pMo69blOy6eAiH1ug3Aijx1dNedRqa24gbayn2HTh4umXaFBzVCXTVXRpVR8ZGOMZDZU5qPBHZoKtgdeeSrnlBGKnfUM4LEvXB8HqTAkHxidl7rVGjRboHYVAg84XDZ9yy1cuUabibrLlUMtN1Kweou87cGv70h2QlepvsHkn87oGTbbuICwidrR_fFz5qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cd947a5c3.mp4?token=girMi5O6buqW9rLT_DQstbD3ZBBqPF1MoYHQw1Zx22Y1L22xEDqvcIRRM6EKJTXgwi_vP8P1re8zp6HPIGp_3B2S5oYVGw7b5zyA1SJGBrGkqkQL87i-TbyQ0y-_6ugzXUOrdFrdsA62v7yoJT9PQl5pMo69blOy6eAiH1ug3Aijx1dNedRqa24gbayn2HTh4umXaFBzVCXTVXRpVR8ZGOMZDZU5qPBHZoKtgdeeSrnlBGKnfUM4LEvXB8HqTAkHxidl7rVGjRboHYVAg84XDZ9yy1cuUabibrLlUMtN1Kweou87cGv70h2QlepvsHkn87oGTbbuICwidrR_fFz5qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخیر.  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84057" target="_blank">📅 12:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84056">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/534ba3e4c1.mp4?token=khfG3_Y6rH5xPJ-PqUTSp2lgupYozztjDd0AA5rzS89K1Wy6OUWYCb44CYFs7Kw_gSziQ4Iy0cEUP6ZD3rxj7t2VZ8rT3R-6emD8xMK5j168IdNJdMMXsowvcCHNRfN0QESEWyfRpv-qxcODGVAns8q8rLwqELuWCboEFf6m8NsRISSKTJlbj9zaZ9ndWC1St_qxoJaUDPWWgcjZm9b7Vb-2jQho0SSoj6qKgTdmxMEAcSE54Inr2kxXsn2WoOgvdibSj5ArWCBjV85YMruILh9At0-mKFYAgEWUn9Y6rATArzgkfEt8QvzoeCNL4eV8_j6FyvaOfGeZ9Ac7JY05ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/534ba3e4c1.mp4?token=khfG3_Y6rH5xPJ-PqUTSp2lgupYozztjDd0AA5rzS89K1Wy6OUWYCb44CYFs7Kw_gSziQ4Iy0cEUP6ZD3rxj7t2VZ8rT3R-6emD8xMK5j168IdNJdMMXsowvcCHNRfN0QESEWyfRpv-qxcODGVAns8q8rLwqELuWCboEFf6m8NsRISSKTJlbj9zaZ9ndWC1St_qxoJaUDPWWgcjZm9b7Vb-2jQho0SSoj6qKgTdmxMEAcSE54Inr2kxXsn2WoOgvdibSj5ArWCBjV85YMruILh9At0-mKFYAgEWUn9Y6rATArzgkfEt8QvzoeCNL4eV8_j6FyvaOfGeZ9Ac7JY05ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخیر.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84056" target="_blank">📅 12:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84055">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نمیدونم این چه مرضیه رپرا دارن، اونایی که تا سگ نمیشناستشون عالین وقتی معروف میشن یه گوهی میشن اون سرش ناپیدا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84055" target="_blank">📅 12:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84054">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20a8e0532e.mp4?token=j_GRz5s8MYkOJjv5vY8B70qgt8gT4q8_ZZOOm5okAoBypK8hajTI72lihFxr2rn6OwfokZTyR3xidiDNj7OmygbUBGOPdPt5Po8_PhoSxW-aay7ajprEjmHx6pcC2NoSIUIuhApmC5DEmV-1VkSWf03yRFPDQptAFLtRpdrwsLx8-T9PAR6xLLyU5j4C2OzKY7l0lIB36qGXQxPVBNA6fbXBvh9Yg8Hua55mQC1xEhVds_8qzLeCIdyi-3se5p5AL8uyRGHHnjk5emwhynFQraM0zmvpJuytneAwBHpK7FQLpl6DaoeNJEwCHZxfJ23hk4qxCRYQ9YtPmLS1Dt_QGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20a8e0532e.mp4?token=j_GRz5s8MYkOJjv5vY8B70qgt8gT4q8_ZZOOm5okAoBypK8hajTI72lihFxr2rn6OwfokZTyR3xidiDNj7OmygbUBGOPdPt5Po8_PhoSxW-aay7ajprEjmHx6pcC2NoSIUIuhApmC5DEmV-1VkSWf03yRFPDQptAFLtRpdrwsLx8-T9PAR6xLLyU5j4C2OzKY7l0lIB36qGXQxPVBNA6fbXBvh9Yg8Hua55mQC1xEhVds_8qzLeCIdyi-3se5p5AL8uyRGHHnjk5emwhynFQraM0zmvpJuytneAwBHpK7FQLpl6DaoeNJEwCHZxfJ23hk4qxCRYQ9YtPmLS1Dt_QGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مراد ویسی: بعید میدونم مجتبی خامنه‌ای بیاد بیرون؛ بنظرم مجتبی خامنه‌ای تنها رهبریه که توی تونل رهبر شده، توی تونل رهبریشو طی میکنه و توی تونل رهبریش به پایان میرسه.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84054" target="_blank">📅 11:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84051">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/syzn1DEOEGSQeeLlwOHDfRWIgYTqPaLiacFhdJWNWfCi59i3SQF4qsNPVdVJeURnKdQGyPZ6070hfYZ_iLbKj6ZqRx0f_fwZzVFyH9mgKzepAeoZy4IbvpkTosqLEUIlpwDSp8gzKUTbIfcmhF62bVFLZ6RGfFmZaBN2yZydHLLFoITxzq-mpbzkEo5HvLg0xFxl09E74SADO957PmuczrBPl3R5tUwzki9gXXRXP4xMiZTp7AJsdWOr6W_hAuw1Lylk7OBMGGJ69Q-CAWwidq5D8XcgOxlZ7XYcESp-wc6RiYW4wSZ0pf8ltq-ZBX2BDpRREHFRrd3CpLkkxl7yJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HE9OsrJBw1ZylWEneaH9RIl2YfuoYfuQeQqCYleGJ3Hmm1d0Met_I1dgIFdccTPhf7nXfP4CL1RVKtAiPoOVe8k3qMA1qBFapL49T9SLfy8Zi8p1HXSz9Wsl1KDBa6q6ZWiRSB2keYDpSRUMXLlwE70FkiG9JaXlNydyqsS_pPMktHmDvNBitkV4n4FyRUHIdmQ_XMlP1PrsbTtX_N2UbyLY6dQPaOPIAKyM3jYg8GT0LAqcmCwbpvg7Vb-a4pkHxOnqdC_nKWSezV4Tresut6aG3_X1XbvpZhUolQG2DAukkRy5FBGJLllFRgtskda1vtSQfJ27V4rxJLKGXqgLwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N65IGgFpAvMIX0-NqqVHD0UCzMdWbdIyruXu6_19RJ8x3MwIUHJh4QTvEHoHs6znTOTABpRVrwxsCwpEqQ72v-Zrt0_9M4s-4dRHtjOW8Oi-Et_NbbI9fv3kFbSriDYFgnCuqQxRwKU6GMccJ2OoHcSgtVfarpiOL_OSN7sqJtO27r0K9cqFF6cBmN-g7umQ6ooqm1be1OC_2A2k7YQRXo1BUHiZPxjY7oR_pxy_BjrWG3NZukWo6RbWAEMmNxCoYvdumO9G_MuXEEo0POrsuEFNrH8jcaLECoDLCvEmrhVMpd8B9UO1xD7ffJAtODnxRLPcMI0acMe8EXUK29vgRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کیت بازی آخر بهترین بازیکن تاریخ عجب چیزیه
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84051" target="_blank">📅 11:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84050">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ritzobet.apk</div>
  <div class="tg-doc-extra">45.3 MB</div>
</div>
<a href="https://t.me/funhiphop/84050" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکیشن اندروید سایت ریتزوبت
🔥
🚀
وقتی شرط ‌هاتون رو توی ریتزوبت ثبت کنین ، علاوه بر ضرایب بالا ، هفتگی با کد های هدیه کسب درآمد میکنید
🤑
♦️
آموزش شارژ حساب با کریپتو
♦️
آموزش شارژ حساب  ریالی در ریتزوبت</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/84050" target="_blank">📅 11:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84049">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkopugLXZ1n0NkFUEBNQqymbohWfb8Cv_IMo5JcxdL9sv5f7TDfSDh_pApb6Wcwkspf31yAHH4efwMuNl65s9tXBAQx67NZ4A9yFTAHaJtknKfPMporgxs9LsaylB9AimSd2tTj78aOeDhvosBFxFYQUSewfsua-QOM-pOIfPqVrjBm8qyOKtdliECv3pM6uQeXH9JDs0AgUA3v0-OAXuWFomIOAaT_x6ROSWuDPWzW7VdGr9ykVu1CVRYctIDaJU_g8F9-XAof68m4foC8La0WuZ3uFRcVgm8aEpCBeogYVCuYd-aQkfXlLsDXnm3UHM4K_i6rb18SALC3fHDYQ1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👏
یک بار شارژ کن ، دوبار شارژشو‌ این طرح اختصاصی ریتزوبت برای کاربرای فارسی زبان خودش رو از دست نده
🔵
اولین پلتفرم جهانی و اسپانسر لیگ هلند محیط امن و حرفه ای برای عاشقان شرط بندی فوتبال
⚡️
واریز آنی با کریپتو
⚡️
تسویه‌حساب سریع و مطمئن
⚡️
دسترسی آسان و بدون دردسر
⚡️
محیط حرفه‌ای برای شرط‌بندی و کازینو
🚀
همین حالا ثبت‌نام کن و تجربه‌ای متفاوت از شرط‌بندی آنلاین رو شروع کن.
📲
اپلیکیشن موبایل برای اندروید
🌐
https://RitzoBet.com
پشتیبان فارسی سایت ریتزوبت
👇
🅰
r4
⚡️
@RitzoBetsupports</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84049" target="_blank">📅 11:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84048">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYXWdlro0uiGLOhYYDrbe_PLpdvaBps7DbG84hs-bp3PgS7AzSseek3F2RAJWCD1x_hUzT57u8FceFEAh2eii9dhcQq_28zGHWgbxeHfmMu44gOravFBJvnRUBWchst7-YVzJm2_Bm_oaMKjUSvynwQB7xZ1MXnBwLwvvLfWYXzsTPIqQaNi2EYeTg7vdpblPnu4JDZLPZFJzP9F-TAJOfkhqKCA4pYI_XMwghjYRnTacRVXPCaXIe9VM-pPFT5yFBD5-sU_PhAKpWpbSTg7Z-djIRV76CwZvL5VLXIEZwYtfMt1dfTZow9KjGSOom3HiV2xnI1gVVylSSqaK910Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماشالا شیر، ترکوندی شیر
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/84048" target="_blank">📅 11:09 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84047">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729ba5bf0c.mp4?token=bO5F-s3HK8KUifmJ4MHzvDYc0sqTnSsOCZOOUeZg_Yclii6HWfxInq7YEtf_0E23mR81zgkp00sUAIo9bgs205vm-F8yu39ss6-q_zZkxrP5tbhws0D-b7wpLeKihDFdUXZ1skAaHA8A3_mdrLFD1FkCqggMlej_XzFO6Qi8J871EEKPhCztIo0enG4om1d4b-8M2fKlmXnMaCxdx1uCj8MnSIpJ9VUVzpQAuHKaDqco7dnROEFUiV6wf3TCs_816Ds-jY-I4kK9rxRqusFn_xt1i06iRU7sxLEbQNJucPnoNTttbBdrtImRaQoLeeTyb7tbm1arENwd00p1jdDxDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729ba5bf0c.mp4?token=bO5F-s3HK8KUifmJ4MHzvDYc0sqTnSsOCZOOUeZg_Yclii6HWfxInq7YEtf_0E23mR81zgkp00sUAIo9bgs205vm-F8yu39ss6-q_zZkxrP5tbhws0D-b7wpLeKihDFdUXZ1skAaHA8A3_mdrLFD1FkCqggMlej_XzFO6Qi8J871EEKPhCztIo0enG4om1d4b-8M2fKlmXnMaCxdx1uCj8MnSIpJ9VUVzpQAuHKaDqco7dnROEFUiV6wf3TCs_816Ds-jY-I4kK9rxRqusFn_xt1i06iRU7sxLEbQNJucPnoNTttbBdrtImRaQoLeeTyb7tbm1arENwd00p1jdDxDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لطفا همه خفه شید فقط ایشون بخونه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84047" target="_blank">📅 00:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84046">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MAksesnBsbX0qYFAobNjQNENQtmuPXHe8XYOwDMtVXK_SUz2LHha30yc048iVHtRvEiuM86LM408fMbmqQIFuDUGW4ptD48JO7A-iobLW77KD9BkkbnOBxJNTgdx6fg1VZjv3TF_1mhYFZqH5VRqQt-VFjQe2biAx5mW59LPRBzx1YRMfX-hgoRBvMLW8X7hSEc_kgHOHaHjKeKsQzsm0vRJ3DSB8pumJ-KRvm-LQdGWjNU33sB262jguIEuFBx0I_6l7XE5U2qBj-OROKgdRQqSsgQdTOMxFnHa4yv5mQRbqWE-Fw4A-64X3IqMbhpS0j4_hbeAypoRQbEMose-rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خستم کردید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84046" target="_blank">📅 00:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84044">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ETu4JKuIURmQJqX6vSXHk-cUCfw-Uqr9TAhWDNqQD6m8keJQYjKQngo41EdZZwSgNXnm7ojwK6icyrhvBEYm97YOlGeI7xW-jwY_hQaYYaxuxvLdSnmhFNd7LYKsBucQljlkYEO68Lgqhsljpg3raBx5EJdXVOPIREz7untkuKEwAYXNvDKzrph50CcNaN1gp4NrFcGS39RpfDivNm6Nd3LjWCa1-uWpCaqEHK_xNCDW6emRqaREjquhn7hYjSFCAm6GpY7oHStnYMrg3rlRjdns7xHhvhs8_96_uXf0x71bfRgAZl8_EjkkA1WYIO2pdL3CccVoREIOZDJQlsRlhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MJnm8hZGTN0z7ik_YmiWNGO8JnH_3YjOTwM5Ro-kwEsZgckF_bAyngzpKFG2vTW3Uxwx0HDJJSQBpM4eDTw5gWdzX1iBYI6RlVC3ro5qsCSIR4dmzqRvbQPh5F2p6AoovJO8ZfIUQ32CrURELncTrilgq_zXnZdy2E7jzsDVvhR_gqvLz8h0hZwPhdnCAcZ9uBPmhLBni3AMMxZvwK95lX6zDbTQrM2A20ERZf-1jw-HYzCGZ9Zj1h-ykYvsu5yBwrlxIm_O6ZeP8gk7by8zyOlHlCBkNiOK-fyeN8O-tJqIWJPwLDgRACh5Ev71wxVb1CFavaFxBrmU8cM3NLxcoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فقط نزنیم حرف خالی
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84044" target="_blank">📅 22:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84043">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfCS2FvYS3M1boVwb6AiBSROwJNBYio0-QQ5cZY4mZscUIbRoEiklWa5HQOtb6YkkyQFsGP4P01Sd6ZxdlybruGIBJXhtcNigWwa0Uzig0C7ytalHeqC7iPLyAc_R7zzW_u4r_qWm551aa5sFrwSIY8QJAq7bvPC-d5rQLrokTKQYqn9IiaLJvnrqfVTlJ9k87XiZR9-BBkvHi6cLnkeVtZ2M8dmurWl5jYat4zblwe0WwPC6Sj79aVjV_oCnVIacmwIoZZh8908pXZrwbhw0Q28AlB9suQYR2EevNpdTpStQ-YfH2noscMk-cnTpBoGiIG8LGcceoqUoU3zFERQuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بعد از اینکه پزشکیان بخاطر سخنرانیش تو سازمان ملل حسابی بین تندروها محبوب شد حالا بخاطر اینکه تو مصاحبه با فاکس نیوز گفت اورانیوممون رو میدیم دوباره داره ازشون فحش میخوره :
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84043" target="_blank">📅 21:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84042">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YD926_JiJdIfCQmb4W8mxuQxyTx4yTSqmZWiDkyaTw9UwN_xAtZV1Dt2f8BueCIZsB1vfnBYWTkirwX5hgikIamd1EQ6lKX8GdGLTJd0O-Y3uPUvRWoSSLERqqX1wFVC6GH2zvAoOXKwVxPYEXofaesFX1qNYDi_6CO2JC7Rl5OM_7JaQjUBjJKPJOnGytFKjK1cFY8cZ-Pj7MA5H-5HbzM2YVJ1xYj7tlvvsbDrAIaaODdeJmY9eDh7fJPrjJzWlQCTQh3M4t4Byx_ZbpJd5hbXv6DP6AKb_TDrEFAFzzLn8sF3u6Cyt9qIqCKDZpqJs_2w1iSWnboL8tD2J_OxSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رپفارسی دیگه پول نمیده فقط یوتوب
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84042" target="_blank">📅 21:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84039">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترک جدید عرفان و دکی به نام "ماما کشتمش" ریلیز شد.  Spotify  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84039" target="_blank">📅 18:00 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84038">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترک جدید عرفان و دکی به نام "ماما کشتمش" ریلیز شد.  Spotify  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84038" target="_blank">📅 16:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84037">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVuHYellYocez7cld4yUxHLq3DgW7xEexae_KeNuu9M_N_hulWuncikLKnM8kWxJLz-z8uDSHWZxluzHdD01Vxgrr41ZHP3fYBhQyzk4XTfaVKvY0Hf7ne7qyRt6jwSiJmEuNfw4rfjFtyxp36DL7YCl3Vgc9aw7lAj3DaDJts5OdbxWN7YjZadhLEogf1Jsh5Jfo5UV5IH7CarD8mlVgoOOtbOKiAAFenxcrmxd_3W0lwRbWSIXJIpi9_bJb00-JRDHkqRyFusXIV-WtVFwNY39XdRX-x9HsaktoqIjgS66Wdp4o94Axx68Lz7Oqsd6pIwvpJeI21K42qgImkkqvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید عرفان و دکی به نام "ماما کشتمش" ریلیز شد.
Spotify
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84037" target="_blank">📅 16:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84036">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03c7b6e9a0.mp4?token=l_lfsLjLRozt6sJv1tfMd6n5k9wmICDB9sYu2Zzta8xLVwMZPlXQH2xa2TWSXVFB_47nithm-Jwv9Lb_VurVMadYxC7Gmin24k7RrCAGPZiC-a8VNxYWtvJzl05-gnbdWJG7MmI2exl4SpWMN83l4eqt_uLhNUsXrRRiicJIKCPU6DJxhMLCuXV1osnxzzYHxG5HAq9wrxm4SxiyH_8HBE83dgU7xNGu4D-abiE3N1HNhsXBoodysp_QJkOed59EfX9dLJ4vD6SkfvDC8QHtTGPfqPkjz5SGzC9SeF9XH2SXipfzYDMTKkDf_EojfKhKoUaZbnY0zNWTB_cg5EB41w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03c7b6e9a0.mp4?token=l_lfsLjLRozt6sJv1tfMd6n5k9wmICDB9sYu2Zzta8xLVwMZPlXQH2xa2TWSXVFB_47nithm-Jwv9Lb_VurVMadYxC7Gmin24k7RrCAGPZiC-a8VNxYWtvJzl05-gnbdWJG7MmI2exl4SpWMN83l4eqt_uLhNUsXrRRiicJIKCPU6DJxhMLCuXV1osnxzzYHxG5HAq9wrxm4SxiyH_8HBE83dgU7xNGu4D-abiE3N1HNhsXBoodysp_QJkOed59EfX9dLJ4vD6SkfvDC8QHtTGPfqPkjz5SGzC9SeF9XH2SXipfzYDMTKkDf_EojfKhKoUaZbnY0zNWTB_cg5EB41w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون دختر که دریک سگش شده بود گفت استپ فادر ایرانیش بزرگش کرده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84036" target="_blank">📅 16:08 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84035">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">خدایا این کارتون ساختن با هوش مصنوعی چه کصشری بود دیگه</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84035" target="_blank">📅 15:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84034">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خدایا این کارتون ساختن با هوش مصنوعی چه کصشری بود دیگه</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84034" target="_blank">📅 15:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84033">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dtj48o_usjmzolFoB3_ZKpBqCVU3961xmb3v3I1lcKrTS89_PywpoNMdfuODc56d6VxbJGIKC-n-wC-cI-iIVCPrdMt4BSFYjH9HonEett-TodMOqmkYRml5u7uKRt08xgqdIoT_uLjGzBvXMXsP8VorvEDrzL6PltGNu-IIa09Aid0zSdcXv3Pgsk6sHSviQKzxQ5gOl9cp35DHbkMyCQJiPwDE7w0xbofYvkhCORxe7lQNAfarYMhgtasvLcE3ax4YrpZJqeO1_Qp5mdbtmOGwk_wL65BLQTxNdZvLKLvWSSuQgh8OFr_2xBZGA8TKNHwlDryoyposzijItJxhOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو با اون بیفی که کردی یچی فراتر از این حرفایی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84033" target="_blank">📅 14:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84032">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SV_nFNuV_hzJXBWlWyKsx4gfAPBsIaxyNHWfmNYIfm-l-LDwf1kc-MWN4ItMRgeNLXRq2cr6Z9-bU8or5SIaaV6kJkMM88fw4LNrUyhjBtuTFuDLiSo9h9ptXS_Z-ANZrZUqWzwsmB4yidCA9hber1849wdg6qFmRGYis8RI_YgUM42XD0psO696lo8r0R3xD9n1QalezqQX8qUjhaoqdc6VLpS27aOng0B2aXzJBEnpGxExrzzcnnIhTTC0ARTvhTXtPQoFRF58bwFHft9chUl57GpZyZBqXssWeR9oaQO1zI-_ediCE_jZVKr5rv3TS-0APvpNBlZOdQxz3P16Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این چه کصشریه دیگه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/84032" target="_blank">📅 12:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84031">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">لایو دیشب رضا پیشرو که بیشتر راجب کصشرای کنسرتش صحبت کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84031" target="_blank">📅 11:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84028">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKC9UFz87eBBX0ADHRvztukjBw7nvfiX-DozEw4Ie_K7sSKWjUW1wRHNh5L7fRGYikfPd1dyOiriBQ5An7Hj65pjWpPGeMwgImLSzbMQOIznq0m3IPcHlRDxBIo9069t78y4K1rNzsfggn2nQyTLo8BrFSUB8U0EScObB7kH0ofR2NH6LXGS6oC0roMxcKmURgbBCPFCjuuRh-e-4_FobjzJGGc72wQwjHWu6glpwOplSAcMKunFS7eB14YUBVAaTQFWPX7sARlKjBwe_nsqMqS7rayS8howR2UFlueqmsVLoNujUy9Ozx1dQOUjI_XhhJat0X3QHIrkUnuledSTqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بی‌همه‌چیز من این فیلم رو واقعا دوست داشتم.
الان با چه رویی برم دوباره ببینمش و به بقیه بگم سلیقه‌م با بیگ‌شگی یکیه؟
(اگه مشکلی ندارید فیلمی که می‌بینید رو شاه مشهد دوستش داشته‌ باشه و هنوز این شاهکار فرا بشری رو ندیدید، همین امروز ببینیدش؛
اسمش: Léon: The Professional)
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84028" target="_blank">📅 05:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84027">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07c419d7c7.mp4?token=l61uV44OQT4uzHOohypu5sPLa5Pax09BOsOSA4A2-j-lpBcSWQ1-UzwmYlDDYWvbBUKbhkgYMlpVob-eH5NGkoDfQUfs7wRbfXNWItE2b7BxJm_eHj63Amg3NchcfJU2H29M0UIaMpnWTT1dR-6jeDmbzG-GZMeAgTYM3In3LRqF_U-uXA3I1UJ663v-lqFDotSpMSUcZ8wkAypFENAlvCnXMLSNbx0z6N8nEpoRlLVAslDI45PAjcTwZBza4bs_nFEdF9XTkRDCHcYoX3xW4Qio4H6MJqvLKgDMaE2rwSagkyCzbtsIRI2-UWtxdoWsCTotenNvRr7OnAB5o0ideA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07c419d7c7.mp4?token=l61uV44OQT4uzHOohypu5sPLa5Pax09BOsOSA4A2-j-lpBcSWQ1-UzwmYlDDYWvbBUKbhkgYMlpVob-eH5NGkoDfQUfs7wRbfXNWItE2b7BxJm_eHj63Amg3NchcfJU2H29M0UIaMpnWTT1dR-6jeDmbzG-GZMeAgTYM3In3LRqF_U-uXA3I1UJ663v-lqFDotSpMSUcZ8wkAypFENAlvCnXMLSNbx0z6N8nEpoRlLVAslDI45PAjcTwZBza4bs_nFEdF9XTkRDCHcYoX3xW4Qio4H6MJqvLKgDMaE2rwSagkyCzbtsIRI2-UWtxdoWsCTotenNvRr7OnAB5o0ideA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دورچی بالاخره دوباره مواد رو شروع کرد
🔥
@Funhiphop | Nima</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84027" target="_blank">📅 04:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84026">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dz4gnwE4prLrUkVAQIMIJ5V-0c_7cZD7vrTdpGqmxKmzV-FW09umrVFF5y17sfntoONXdW5KvjMFC6SxiiLImU05N5P-Qf92jEAR31HZ9BouGsqYq6fqBmObFZYN9Sw6oTufU2Lf5PsTA0TQGgUx03V71Xx2YrGgFOZzd5XsrjGxfvXZPNp3qxHkbFhwU6qxEC6bVX7OIevRM8RWuiOqumlepYgx5yGdddUnDr1hYYFwBE5TuqGKP1WJwPmkMC63bvzBR54fsd2XbWEbRBWAhsREK18VZncJgVniy5QvThJOavM5eVQPI_NuxTju4XSFo5iafZA8gJAPRvOwxzZT5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگیرو رو استیج عصبی کردن  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84026" target="_blank">📅 03:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84025">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">پزشکیان: ترامپ مدام می‌گفت: "من می‌خواهم هدیه‌ای به مردم ایران تقدیم کنم"، اما هدیه‌ای که به ما دادند، موشک‌های هدایت‌شونده، سلاح‌های سنگین و ویرانی بود. آنها در واقع می‌خواهند با ایجاد حوادثی در کشور، راه را برای فروپاشی نظام و دولت هموار کنند. من عمیقاً…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84025" target="_blank">📅 02:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84024">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/195d939cba.mp4?token=c9NQchNZozLO5pISQh5f2cEjBDlB-IrCGSJHMqLKv8klR-ZwdZR1jHOEUeA4pkRq8ZbxNRx219jvdHxTbdcbrNNi9PzDfbZF1lieWV5onKDgskaFfzwuFwROYF6Qkb8fRbchHKVw2Y6d7ickp8lomj-XKGOWgpo4LPrLjQ8fhzJgEeC6VUVCNIDTKJw9DpWq3qoRUfCW-iuqAkWQbxMt7h85tHGCLs-E3_q8L22XAHDC6lcbuzOn_-EDWz-azNVGFUMxEnQXocxPOkdk1LOQGFKHg7gdJoAW3TBCcZc-1YXxG-vWRWLPxjqGiVj_ADG1C_d6WdV-sDSZBy8FRE3Eqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/195d939cba.mp4?token=c9NQchNZozLO5pISQh5f2cEjBDlB-IrCGSJHMqLKv8klR-ZwdZR1jHOEUeA4pkRq8ZbxNRx219jvdHxTbdcbrNNi9PzDfbZF1lieWV5onKDgskaFfzwuFwROYF6Qkb8fRbchHKVw2Y6d7ickp8lomj-XKGOWgpo4LPrLjQ8fhzJgEeC6VUVCNIDTKJw9DpWq3qoRUfCW-iuqAkWQbxMt7h85tHGCLs-E3_q8L22XAHDC6lcbuzOn_-EDWz-azNVGFUMxEnQXocxPOkdk1LOQGFKHg7gdJoAW3TBCcZc-1YXxG-vWRWLPxjqGiVj_ADG1C_d6WdV-sDSZBy8FRE3Eqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
ترامپ مدام می‌گفت: "من می‌خواهم هدیه‌ای به مردم ایران تقدیم کنم"، اما هدیه‌ای که به ما دادند، موشک‌های هدایت‌شونده، سلاح‌های سنگین و ویرانی بود.
آنها در واقع می‌خواهند با ایجاد حوادثی در کشور، راه را برای فروپاشی نظام و دولت هموار کنند.
من عمیقاً باور دارم که انسان‌ها نباید باعث مرگ یکدیگر شوند.
ما باید موجودات برگزیده آفرینش باشیم.
وقتی می‌توانیم مسائل را از طریق گفتگو حل کنیم، نباید به خشونت و کشتار متوسل شویم.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84024" target="_blank">📅 02:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84023">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c4f14c5fa.mp4?token=aQ4fUOTBx3iasqZmkPqjF7MUFQ-p7RgR0wTbwxEclIODuVrOwdSruCyZ5ungs8DlcR29alyf0DaLmOyXEDOUWRDdHN_lQ3dD4zwfBZgFR6hgbR5tnWuBZKJeOKZ3nbuKn8NI6YvuttFqfE8QfUP8FL48Pk24t67LFiXmzGo-k6pc70c8DrCxdDYi6NH6KQXOAvL-jurb_hBic1-SWc_L3MkAhCFenW_TIBHKH4FepJfgg-RjXMGyNI_R_KTw9iGsOMwOzAWJeVgkR7iCuX3s08i1xKfA_mrDaF1A-eEzg_NRMsSk9nBKhD50NiLZUeE6kCEC2x9FwCnlqnpIn0Ggig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c4f14c5fa.mp4?token=aQ4fUOTBx3iasqZmkPqjF7MUFQ-p7RgR0wTbwxEclIODuVrOwdSruCyZ5ungs8DlcR29alyf0DaLmOyXEDOUWRDdHN_lQ3dD4zwfBZgFR6hgbR5tnWuBZKJeOKZ3nbuKn8NI6YvuttFqfE8QfUP8FL48Pk24t67LFiXmzGo-k6pc70c8DrCxdDYi6NH6KQXOAvL-jurb_hBic1-SWc_L3MkAhCFenW_TIBHKH4FepJfgg-RjXMGyNI_R_KTw9iGsOMwOzAWJeVgkR7iCuX3s08i1xKfA_mrDaF1A-eEzg_NRMsSk9nBKhD50NiLZUeE6kCEC2x9FwCnlqnpIn0Ggig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
ما هرگز به مردم خودمان حمله نخواهیم کرد.
مجری فاکس:
اما شما این کار را کردید.
پزشکیان:
نه، نه. چه کسی اقدامات تروریستی علیه ما انجام داد؟ چه کسی به مدرسه میناب حمله کرد؟
مجری:
در تاریخ‌های ۸ و ۹ ژانویه، شما قطعاً نیروهای امنیتی داشتید که به شهروندان ایرانی حمله کردند و آنها را کشتند.
پزشکیان:
خیر به هیچ وجه اینگونه نبود، آنها همه تروریست‌های مسلح شده توسط آمریکا موساد یا کردها بودند که به قصد سرنگونی و ایجاد آشوب می‌خواستند کاری کنند و فکر می‌کردند ۳ روزه کار این نظام و کشور تمام می‌شود اما ما مقاومت کردیم و نگذاشتیم اینگونه شود.
آنها مردم عادی نبودند.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84023" target="_blank">📅 02:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84022">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">مجری فاکس ‌نیوز: آیا شما هر معترضی که به خیابان بیاد رو اعدام می‌کنید؟ پزشکیان: هر کسی که بخواهد اعتراض کند، به طور کامل حق این کار را دارد.  اتفاقا ما با بعضی از این معترضان هم نشستیم و با آن‌ها گفتگو کردیم. اما اگر کسی بخواهد به خیابان بیاید و بر علیه سیاست…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84022" target="_blank">📅 02:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84021">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5add83729.mp4?token=fb4-2Mli1vey6NFYE94pahkmsbJ6zlgJPWbIjmkmG6IKmhALfnm4VkQSzR0gfXmk7Vu8V712KB3rNwDNzsmjuGGQhkvSYPugsYaB5RqfknqCWi5EE1NEvsfFSf1KnvKZmotinCAesc9pBNj7XcLTkOteTnJ_pImCTp7TAQQdeMVo_dRaUEemuOAQZQ3SievCkjYxOeTzAwjvgINdB-Q7Ied-qYz3ozQLylUJ-wHgvbpuXcqEJtOaZr5h6X8IhlaThbBrxC2cCblZ0Bx3Co_HpGqKqn11c41davlMnq_KYKhPOfSAIHJkOJ23KDXSvNgdRI_LWiGzECS741uJD82bXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5add83729.mp4?token=fb4-2Mli1vey6NFYE94pahkmsbJ6zlgJPWbIjmkmG6IKmhALfnm4VkQSzR0gfXmk7Vu8V712KB3rNwDNzsmjuGGQhkvSYPugsYaB5RqfknqCWi5EE1NEvsfFSf1KnvKZmotinCAesc9pBNj7XcLTkOteTnJ_pImCTp7TAQQdeMVo_dRaUEemuOAQZQ3SievCkjYxOeTzAwjvgINdB-Q7Ied-qYz3ozQLylUJ-wHgvbpuXcqEJtOaZr5h6X8IhlaThbBrxC2cCblZ0Bx3Co_HpGqKqn11c41davlMnq_KYKhPOfSAIHJkOJ23KDXSvNgdRI_LWiGzECS741uJD82bXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری فاکس ‌نیوز:
آیا شما هر معترضی که به خیابان بیاد رو اعدام می‌کنید؟
پزشکیان:
هر کسی که بخواهد اعتراض کند، به طور کامل حق این کار را دارد.
اتفاقا ما با بعضی از این معترضان هم نشستیم و با آن‌ها گفتگو کردیم.
اما اگر کسی بخواهد به خیابان بیاید و بر علیه سیاست و قانون کاری انجام دهد، این امری متفاوت است.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84021" target="_blank">📅 02:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84020">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">پرزیدنت پزشکیان یه مصاحبه تصویری هم با فاکس نیوز کرده که الان پخش شده و با دیدنش می‌تونم به جرعت بگم که حجم و سطح طنز پرزیدنت ما، قابل قیاس با هیچ پرزیدنتی تو تاریخ بشریت نیست.
واقعا الکی نیست که چهارم شدیم.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84020" target="_blank">📅 01:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84019">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">جمهوری کلمبیا اعلام کرد که روابط دیپلماتیک خود را با جمهوری اسلامی قطع می‌کند. این تصمیم به دلیل ادعاهایی مبنی بر ارتباط رژیم ایران با گروه‌های تروریستی و قاچاقچیان مواد مخدر در سطح بین‌المللی، نقض حقوق بشر، مسدود کردن تنگه هرمز و همچنین جلوگیری از بازرسی‌های آژانس بین‌المللی انرژی اتمی از برنامه هسته‌ای این کشور اتخاذ شده است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84019" target="_blank">📅 01:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84018">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g7mnRCLszqQvigX3jmaRzhK3nvUfpFvRyDTj_133Z10aPh4HVGOeDcbBkxol8WZr6eUFvu7zYt2T8e2bz5mNicxyGFShZQ17o7K6pcfrYmbDAUbA0d--52veTZ0IPrsecKS3z41vxWwXpL4ffMn06u15BlO5jezdhoJ3El_Qn7v5TkZJ1nbLsxPbxku6Wx8nyOotnfOvIxpZupjCZzPVPcQlNI3B7s1iS4BlX5fkp3nv9-E_k-AnWy93JpTlXeIJ4gn_uck7jO7IiaItHsq5m3J38P3lxJbhb4AEyxCo8k4foiNeGB_5FejAtvecUaLLBrUbwVplBc17bOMIY5fi9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرزیدنت مسعود پزشکیان در مصاحبه با NBC News:
ما به هیچ وجه قصد ترور ترامپ و یا هیچ یک از
اعضای خانواده‌ش
رو نداشتیم و این پروپاگاندای یهودی‌هاست.
برخلاف
ادعای روبیو
، ما اصلا دوست نداریم جنگ رو تا انتخابات میان‌دوره‌ای آمریکا کش بدیم چون هر چی زودتر تموم شده بهتره.
ما هنوزم به توافق اسلام‌آباد معتقدیم و امیدواریم آمریکا هر چه زودتر و قبل از انتخابات، جنگ رو پایان بده و به این توافق برگرده تا ما هم بتونیم بهش برگردیم.
ما آماده‌ایم دسترسی کامل نظارت بر سایت‌های هسته‌ای‌مون رو فورا بعد از اتمام جنگ به نهادهای نظارتی بدیم.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84018" target="_blank">📅 01:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84017">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf00916eca.mp4?token=RHnlbCnSDzDuivIdpB6Oi-LOoA44rcrGGIipT_9mvyyiw-0CAPqlr21E7tnv4Uq0nfjsNe_ltQ0-9llSot-fLDIqm6crgmquuf0x8RG2nA7Vjq2hgV67Q6G3knidxej9By1WGlXgZ_bb_IuHkdWLiii7eMkTORGzConx4nuCilL38K8BvSuAWTaysmvSj3l5Bdl7d06cQa267zC93SiVXlOrrVNFzwj3iexE6GAmigBy9wyQNc9e82HVqiXAf0Rdc_TFlZ4V3SWhsr4vRZr9lIvqAO6ldAy8qXEmj07M0ZBa1vQPLo5_vpGV3V7alyr-A3FaqL45Adp_IkD7ynxh7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf00916eca.mp4?token=RHnlbCnSDzDuivIdpB6Oi-LOoA44rcrGGIipT_9mvyyiw-0CAPqlr21E7tnv4Uq0nfjsNe_ltQ0-9llSot-fLDIqm6crgmquuf0x8RG2nA7Vjq2hgV67Q6G3knidxej9By1WGlXgZ_bb_IuHkdWLiii7eMkTORGzConx4nuCilL38K8BvSuAWTaysmvSj3l5Bdl7d06cQa267zC93SiVXlOrrVNFzwj3iexE6GAmigBy9wyQNc9e82HVqiXAf0Rdc_TFlZ4V3SWhsr4vRZr9lIvqAO6ldAy8qXEmj07M0ZBa1vQPLo5_vpGV3V7alyr-A3FaqL45Adp_IkD7ynxh7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده‌ی اسرائیل تو سازمان ملل اون استارلینک نتانیاهو رو برد پیش نماینده‌ی ایران تو سازمان ملل و خواست بهش کادو بده که بیاره ایران اما نماینده‌ی ایران قبولش نکرد.
💔
نماینده‌ی اسرائیل در سازمان ملل: 1
پوریا عرب: 28929853059-
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/84017" target="_blank">📅 01:00 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84016">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نتانیاهو یدونه دیش استارلینک اورده بود با خودش، به دبیر سالن داد و گفت بدیدش به نماینده های ایران
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84016" target="_blank">📅 23:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84015">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a45f24bb7.mp4?token=WW0Lsjk_lojmoBskbYjR4XaPWw5fK3wN1_KRwUs_phJVfxDoGu6qGo7gSfwb0WJfMsuUynj3tdXnIIMT560ly_RalPaSiwj-HjMjwZ3BscTTzreA2Q8hXIZ5IKuWQdi5GxHQ_ML0Uchhijt0gsaem3hR2e0lKCDZnMtMntfhEO1FqIzc9CMgMnLG7jr1K6lHt7jBEAi3D9PROBCmljzFf1SGF1PtOaa0m4grSvAD48HXRXDGdYXxvx17Lt_UsxI3pCj1SHwEi1z-bE1SH8nvLnJGG6UEZk2AJthQbc-m1pHWAK9QRqTsdE4Gp9mIBt4l0Ae3TAAlmamae-60toL0cYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a45f24bb7.mp4?token=WW0Lsjk_lojmoBskbYjR4XaPWw5fK3wN1_KRwUs_phJVfxDoGu6qGo7gSfwb0WJfMsuUynj3tdXnIIMT560ly_RalPaSiwj-HjMjwZ3BscTTzreA2Q8hXIZ5IKuWQdi5GxHQ_ML0Uchhijt0gsaem3hR2e0lKCDZnMtMntfhEO1FqIzc9CMgMnLG7jr1K6lHt7jBEAi3D9PROBCmljzFf1SGF1PtOaa0m4grSvAD48HXRXDGdYXxvx17Lt_UsxI3pCj1SHwEi1z-bE1SH8nvLnJGG6UEZk2AJthQbc-m1pHWAK9QRqTsdE4Gp9mIBt4l0Ae3TAAlmamae-60toL0cYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنرانی بنیامین نتانیاهو، نخست وزیر اسرائیل در سازمان ملل درباره پروپاگانداهای علیه اسرائیل:
🔺️
می‌خواهم چند سوال از شما بپرسم؛ کدام رژیم نسل‌کشی، یک میلیون دوز واکسن فلج اطفال را به جمعیت دشمن (غزه) تزریق می‌کند؟
🔺️
کدام رژیم نسل‌کشی، توزیع 2 میلیون تن مواد غذایی را به غزه امکان‌پذیر می‌سازد؟ این یعنی یک تن غذا برای هر نفرز متهم کردن اسرائیل به نسل‌کشی، بزرگ‌ترین دروغ قرن است
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84015" target="_blank">📅 22:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84014">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7315b22a6.mp4?token=Lrlr_5cIoXMm1oCbadqUUG9cq1oiCOepw-xZmsT0U5e2h6TW_iXJjTsmMb4yuXty0mMk_CpwlSCuJinlrijwfGQMXzS5Sv4OB_B1hn27cvQGqMpcD1tbI3riuZ3hQKOqcTYXxb4M3V2Y-aFG0bkLfpSYWzd0pwIRxJEX0Gc3O2kPHDpTzTN1XRi0zWde-hHzXoLtAXj5LXNOd26etUsCATb0IsavCpTumH4yULMU_YxRX4kOmqRE2wZIvx0Ze2cC2ZrRhadXiBeeoU8lmZA2wPqXBUq3vY-JJR98bP7a10ptiGDhj4w3MdIROXw2C5cifXiAWTE4hcRxQNJCGIhoiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7315b22a6.mp4?token=Lrlr_5cIoXMm1oCbadqUUG9cq1oiCOepw-xZmsT0U5e2h6TW_iXJjTsmMb4yuXty0mMk_CpwlSCuJinlrijwfGQMXzS5Sv4OB_B1hn27cvQGqMpcD1tbI3riuZ3hQKOqcTYXxb4M3V2Y-aFG0bkLfpSYWzd0pwIRxJEX0Gc3O2kPHDpTzTN1XRi0zWde-hHzXoLtAXj5LXNOd26etUsCATb0IsavCpTumH4yULMU_YxRX4kOmqRE2wZIvx0Ze2cC2ZrRhadXiBeeoU8lmZA2wPqXBUq3vY-JJR98bP7a10ptiGDhj4w3MdIROXw2C5cifXiAWTE4hcRxQNJCGIhoiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنرانی بنیامین نتانیاهو، نخست وزیر اسرائیل در سازمان ملل درباره جنگ غزه:
🔺️
در حالی که حماس تمام تلاش خود را برای قرار دادن غیرنظامیان فلسطینی در معرض خطر انجام داد که اغلب با استفاده از زور و تهدید صورت میگرفت، اسرائیل تمام تلاش خود را برای دور نگه داشتن آن‌ها از خطر انجام داد.
🔺️
ما میلیون‌ها پیامک برای هشدار دادن به غیرنظامیان برای ترک مناطق درگیری ارسال کردیم؛ ما میلیون‌ها تماس تلفنی برقرار کردیم و میلیون‌ها برگه اطلاع‌رسانی درباره حملات پخش کردیم.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84014" target="_blank">📅 22:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84013">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">نتانیاهوی جنایتکار بد در ادامه‌ی سخنان زشتش:
می‌خواهم خبرهای خوبی را به شما بدهم.
اینجا فقط مسئله زمان است که چه زمان این اتفاق شگفت‌انگیز در ایران رخ خواهد داد.
قدرت مردم، قدرت حاکمان را سرنگون خواهد کرد!
می‌خواهم شما با دقت به حرف‌های من گوش دهید. یک روز، و ممکن است این روز خیلی دور نباشد، مردم ایران آزاد خواهند شد.
رژیم قتل‌عام آن‌ها، با دروغ‌هایش، با فسادش و با ظلمش سرنگون خواهد شد.
این رژیم شیطانی سقوط خواهد کرد، و همه ما در آن روز جشن خواهیم گرفت.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84013" target="_blank">📅 22:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84012">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bde372e04e.mp4?token=DqWR6r8IpP1P28wXyPETpQKS5CpvE_eWttA3pHhTZDyl2l4S7pL43MWehTsd9uVipxoUztMDAYHUcONBrwTYxn_VShHOvEs94-8Wz5jlqqxxU9YyvuDGwlcQJQigJb-PFend0I4pzmvoSyAnZQ62qxW--Y01KZ_VRz0tkYpp1Jq-urkB7SFGmQz-rmx2pJOlbej8-t1BtMlHC6ylhRiSPeCgB1SytT_z8-XPCOfb3elHGMZAUAtXXW2jW8DMJTBUl0kbPIkRz6cxjJWw-mPFnx8C2y_4eTfL83IQ7XkBETAYS-cf6EdZsMX6VZyyC3l2kfkRd6-IFQUwT2Jk-n77Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bde372e04e.mp4?token=DqWR6r8IpP1P28wXyPETpQKS5CpvE_eWttA3pHhTZDyl2l4S7pL43MWehTsd9uVipxoUztMDAYHUcONBrwTYxn_VShHOvEs94-8Wz5jlqqxxU9YyvuDGwlcQJQigJb-PFend0I4pzmvoSyAnZQ62qxW--Y01KZ_VRz0tkYpp1Jq-urkB7SFGmQz-rmx2pJOlbej8-t1BtMlHC6ylhRiSPeCgB1SytT_z8-XPCOfb3elHGMZAUAtXXW2jW8DMJTBUl0kbPIkRz6cxjJWw-mPFnx8C2y_4eTfL83IQ7XkBETAYS-cf6EdZsMX6VZyyC3l2kfkRd6-IFQUwT2Jk-n77Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنرانی نتانیاهوی جنایتکار بد در مجمع سازمان ملل:
از آنهایی که اکنون (به نشانه اعتراض به وضعیت حماس و غزه) سالن را ترک کرده‌اند یک سوال دارم:
شما کجا بودید وقتی که ظالمان ایرانی، دهها هزار شهروند غیر مسلح ایرانی را به قتل رساندند و سلاخی کردند؟
وقتی که آن‌ها هزاران نفر از خود مردمشان را به قتل رساندند و سلاخی کردند، شما کجا بودید و چه کردید؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84012" target="_blank">📅 22:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84011">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_r8A4x9bKj2cM13XNnpDNf8fLwTIsiLUFbu7hojyqU5VBLPvPczKXKbIKU7FOqN4VlNKeIEuAXnDlIHyw90D793Mg3_HDxZlmPoG6M329CNAPuW2gyxeZIZS3WyuZYlYJ0Z77zBfDJFjTU__bPdvpPUH7jpJFfawzt6XiMrNyNtj9pQsYwIoWNtZIpUjSitfGZL1Uj_ATsbLN38m5QTC9sgG2sOoFCdjqjUm7gvo3sqxTzXpRaXHnfSpLtDYIJDP9_NjS1jBsbPalNL9GQcJHJ0uPwpF2yj_SxsdYahZpdoZ1qP-bnfFCb5j4rySkGHOJAqUeNE9AKiOBUXEVp4lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین گه نتانیاهو رفت بالا نماینده های نصف کشورا پاشدن رفتن</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84011" target="_blank">📅 22:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84010">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">همین گه نتانیاهو رفت بالا نماینده های نصف کشورا پاشدن رفتن</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84010" target="_blank">📅 21:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84009">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">همین گه نتانیاهو رفت بالا نماینده های نصف کشورا پاشدن رفتن</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84009" target="_blank">📅 21:39 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84008">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wz_JAnejzgLUb6vVxzsxm5lhqxp5bo82NP43XKsnmvHrtz7HWLEBjN02IZ0upWjZ50XBFNUrmEI0JkdKyfJdO8Tg6llVWPviHI-mDDjI7z5W1RSBN2AkQqpEHqqqxCQ9Eegio68j2WSdLasbyyEiBmKv_uNa2CTaNT9bvlwFZtnXSpBj61BbnCmI4hTr18QOiVrplewO0UYTha1eK4mjTzERsNiFEnMfoD-2PVCSKEUiyutRay68UjGvGYZjBDIwDOZg9GUKip4Do4LcGl8K2DoJuo5GT8B75t1k8aKPos60ZquxOVMel4c8Bf7y7tn8zvzjZlUL_Aq1-0e_K6zU8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز:
تیم ایرانی به رهبری دکتر عراقچی تو نیویورک دارن با آمریکایی‌ها روی یک توافق که جنگ رو کامل
(با بمباران اتمی)
پایان می‌ده مذاکره‌ی سنگین می‌کنن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84008" target="_blank">📅 20:11 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84007">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">امروز پنجشنبه‌ست و طبق روال پنجشنبه‌های هر هفته، موزیک ویدیوی جدید محمود ویناک اینبار به نام "Jolly Chimp" ریلیز شد. SoundCloud YouTube  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84007" target="_blank">📅 20:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84006">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpHhBWzzcFgf1FKno-pZxkhLZqYO9G7_HpM4sI2JXdKOP37ht0HkgV5yyx6WkBWvnnpzTMeInLz-4qKs7g7sfsKr9t5vgNwjZvxasCurxRb7MjQhqGvs1EZriAw9zJmfQ7uj5i-Zho91XA3AVPaT2Js2UmVw4rUt79EG1W2SsZ23GoEw9w3JpQ9w8F-La2bCXs0RsvGUAUwTLWaVo4kStX0GlJ80gWBdACIOZLjRjPoEQMGGGBTbZ39ITcS_Eb4xrSLDa7c8ZlKDscSzA6yiq6YxOEFNUt1VMShoEsBAgXsfWrlDDkY5J1FIonaWizDooS_--i5Akg4ZV4PkSEOyHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز پنجشنبه‌ست و طبق روال پنجشنبه‌های هر هفته، موزیک ویدیوی جدید محمود ویناک اینبار به نام "Jolly Chimp" ریلیز شد.
SoundCloud
YouTube
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84006" target="_blank">📅 20:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84005">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gs1oiiaa-Ng053WH1MPMO9OF-sK1AZqZ-z3GMe52tzBx0i_7AYNx8zsQ-NRHE4W7OP2ONMFgCKCPXba77ajtjEmjVXkFxIfs7m6nZQOqWEEHCGZC73YBzWtaz7K3srysv9UAlA3TLnxyzNx8uwm9AgcCxZ2vkFgnjvGaUX-VJhXl1fcYQO30jCy12yk1Zqm6GEhgymVLE_3kL_ta2Hc0TKC1Y0Hf2w40Ntp_Uz_8WM97XoSzB1ruNxlm1ZN_wznJPfRx79uSTUGDtBYsn3nol0RJyUbKK-gUoeik56ljdEUk5R4iESn4i4x1WQ8aNOeBLz9coRNazJ-1nefS88BvWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا امیر محمد یک خواننده ها
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84005" target="_blank">📅 19:44 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84004">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7Z5j9-eCfJqmJ5SoIalRK_J8CKzJF5cq_0ackW4fP2Mo-_2b_Pug1jQYAANz0PLuZN_6BIMZpff33A3dupsVnZtGwEuAFI-5gvKhvr2RKAV-jC0QBBSqnX9DE7s4nXfhbtzstQMEAFfTJgGQGTkbDEubBQWBFjxWfgp5XeVp1F__XgLrCJ0elhJTjOReHQXUTJfK5FiJHU1a_4OoV5PL5h6WAcB9xQoV5wC-b7yr8E1nuMc_kmX17n-zeOcoupyCak18Vj8i8ep3TKeneV-srpG_J8itgflfSq0inTqfoPL0aU97iTuco3XJ4JBpeaHZWUvlqtCm9ezd5Zc_KfqjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران جذاب ژنرال.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/84004" target="_blank">📅 19:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84002">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb2cea4974.mp4?token=bNaOqFloDi4SumUcjpe9mwnQKPB3HCWwi0C7XID23Moijin_KIDthIO3OhpeJbEIUfhEZlEvaeNEer3RZsxczGnKj2YEjBdrJ38P3XG8diSBixj2dFb9qKLCXZRRVwxTcWQV3gWRKIm5YDxxbbOrkHkG3_USxkyec4knP5gcu4XUcii5h4uzZ8s13cJze-HrD1UFdeNuzNiluObQiqiyym7mPxWI8DoRjHXmMIpwXZB08qYp41rm8vijejiBCF55LjkGrI01JdWU1duFz4SkgEyHdtyzpAXmjnJQ9lK1yHGOqu8xQHL2m_VygR6tqx1ZbRak4GBuJoGsKUZ5KNHqoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb2cea4974.mp4?token=bNaOqFloDi4SumUcjpe9mwnQKPB3HCWwi0C7XID23Moijin_KIDthIO3OhpeJbEIUfhEZlEvaeNEer3RZsxczGnKj2YEjBdrJ38P3XG8diSBixj2dFb9qKLCXZRRVwxTcWQV3gWRKIm5YDxxbbOrkHkG3_USxkyec4knP5gcu4XUcii5h4uzZ8s13cJze-HrD1UFdeNuzNiluObQiqiyym7mPxWI8DoRjHXmMIpwXZB08qYp41rm8vijejiBCF55LjkGrI01JdWU1duFz4SkgEyHdtyzpAXmjnJQ9lK1yHGOqu8xQHL2m_VygR6tqx1ZbRak4GBuJoGsKUZ5KNHqoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیرانوند مشت زد تو صورت بازیکن ازبکستان تا نشون بده مشکل اعصاب روان داره و نباید بره سربازی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84002" target="_blank">📅 18:47 · 02 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

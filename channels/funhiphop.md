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
<img src="https://cdn4.telesco.pe/file/n9iJPeezaSCVqPqH72PRo_RSHDKX6w9IhrFcY2Pr2yLf3GmMYpBjtIcUTtUYnfUJOGVPs7Lw8F4Zk8Utn-vXKLmgZr84bTP1CgsTeYK9IztmZI0a_ffAJyIUOpP-5tIhbzSj6gMsYWAtT8JX9F-5mqyvDU02mbtIx1ehzrQ94mPho09S24qWjZKS-3vg-CYeAcI3qzm3F2c7UnWR_JaWYuq-P3UCalT9X7V2u9WYe2C7GaR86f_yCFHP9RDyCJ4v4monxygSP5CC5XZ7SahfQYadFXxTZU1JWT1ut74_N5JhbIPqvGW2X_FuRN81m47YD3SV4Y34vrEWmbKYkxd2VA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 226K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 22:22:45</div>
<hr>

<div class="tg-post" id="msg-81551">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترک جدید مهیاد به اسم چشات میگاد ۲  ریلیز شد    SoundCloud  @FuunHipHop | Mmd</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/funhiphop/81551" target="_blank">📅 22:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81550">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWnYZ3Zvr6g-E9WT7DkdxVB_hzLcR2Gkuy71_PD9FGkPITDfKo0bo8RFiAQpn1XktablRIBv0IZFccl7aPPQKQJN6BjMOll2rIQhjzwLr1R6-fu7S4Fvo3nQ5XBxv1UlR5qt-k7Ffg4jd-G4GsN0Yf43hKlJZOBx4flP4FKqMF5hjHw-zMbBYPvi9AhBte7juI7Jc8OqOAXFD5mgcF7HKbEe923J79XsyrRiD-RkY055w89mUBJ3-FbW1-CD_qW1Wq3Yk_ktqJ9zOLd9n3RJ7J-1KeeKS1-y_cpHUhYsv0H84Peh6cP-Z8NsFuF4roBTMhyP9fT1KZ37VtbO7nIfrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید
مهیاد
به اسم
چشات میگاد ۲
ریلیز شد
SoundCloud
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/funhiphop/81550" target="_blank">📅 22:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81549">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZ-Z4N3REbo9xE8VKTc1xZ5akvPD_jf3vWYnAx0iS753r_u2A1BCEf4lVzutMJS3Qp3CSY__pyR4Bfh8WGiTH8YGkuMZ6DNanzzZXQ81ZYz0xOMNNPAt-vHTVup1DhmCThn-PC-aPPquKu7s22LmHDrvCuypagKWAcyYSj4V1HzeSJkcZ193cZtYN7ZHABArNWHMxkehPtKcO_yqIrRuxxpEn4psIYclKUbz27yUeHmNTgLQq8o-9la3eLI9zeEvs1NWCdCPExMCttrl4WcV65zqYSidWvkpm21182qB0Y8z0sN7DtyjHeF6klDgvo-ZPHzcppsy647D52DNVw7uRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یتیم گیر اوردن کصکشا  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/funhiphop/81549" target="_blank">📅 20:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81548">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">پیج اصلی سروش ولی زاده برگشت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/funhiphop/81548" target="_blank">📅 20:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81547">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNrecDBjt9hlR2Hwb8-3B-aeSGnmFESMKgJ-IFq9tF7MDTHN8b1LEw2_LAr7tF7yMULM2KOcTiw_95C-GRgncArIv-zqut_wl3R08Hr-2ZZZpNeAwverVAYAqUG45Cph9McV0nFJxPfG2MMEr0ilxk2f4I_Wk-cbvr7Kl_RCIBcAn8_JnR2t9mO8c_StdFknAaEHLodmyGwychJ7oFEF3pA_tOrDNccjfIvwelWaixv-8BX0Vew0ZinoDWbGl3qPSF5doyT6sRhmS3TMeF1R-7YaeTGZhq46ky007jeHaQIG7gMugYDBnCuZfsbmHUs2c04j0zWgD4ja2ZeyEk8TUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروفایل پاول تو تلگرام:  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/funhiphop/81547" target="_blank">📅 19:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81546">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-JjDpRMl3Ur8HlQxY85zQqmykni1qkjffldUd5qBDqdnHLwqwmkG6h5_7oxjBSMvUkt4e8DRsoaD4Q4EONm8sjragAUN4rqYC45RqG3-oCtBG11iF_NwfVNbGFdkhRGG5bWkU6Ds-GQsKK8QjcLro5bu0iFOYaX3km7oe5NxOr7ZjVx71S5FHp2WXzLbPs_h8WXhLj6Kh-FumEklnTnmQ3_lFdpxmcBzWXKukwJ5DHgj0FrH5RYzmeEGQv-YDBEpKC0oIwP41x5wKW4PyNPJtlbsUxgKdxRs7Er43F5KfFbOuz30nozOuhSoQT0mY8NE55qF2JxwmhGi3HXQ48dOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بازی شاهکار رو از دست ندید‌  @FunHipHop | Jenayi</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/funhiphop/81546" target="_blank">📅 19:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81545">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PA1KdzsiuB7jphOv-MF4GzR0ya3Dof2S9QYix_JHkQQTPtVKxwTQKSObsfC2sg-AXebnLkXFGrP-pkUJrUByl0nopFcJEud72ZNdGI4t1onB6g5Yw9JaE0pp5SfXG0Gfk5z_Z7-Bitwn1Mt4AcWC20y5vQKlKw8YRFlQ0C8JKnBW4m6RHhPhp1GDjMVr2qkOCc4_lGxoHa8UiSEMhw7LAoLwUG3L3GkylGBDpr4jnQx_8ngxmcYPiyhLzOMAwElrRWF6sD93WnCErCFhR1h65PNzM83oGwkBjWpK9UInz0MxIyTAlEkUVCSc1xWio9k2FfVy2thZF-WatnOe0m2hrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بازی شاهکار رو از دست ندید‌
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/funhiphop/81545" target="_blank">📅 19:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81544">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYpRvI9xc-GtD15fX_xAaRIwDbkbRsO1zhNw1Ba9xw2bffrFl80q516tmZr3g8uDXt1ROqPk3mlwB8FV8iu3gqODUsBMFu87OHbWpv-FF0TTVSY0KvyWvYbGwZBnBBSavDJwxQjmPXAM5gM71FNW1XuEtbuTCJWtxHe36W5jb0hvXQv0HmvUUq4XYoDmkx_aYkJScx-wbGYTKHazNHEY_KhMboeckFA4ydsuwH2BLc2cLqsaCbVvewYKf0x36n0AvJCpomspKI0hmNBKWBsNCJWYUAeW-R5qWh8soPpcGviKesSLK1mcS2l8TxjhobHpaZjyWby_D3iEXWLbdMyDCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
بنفیکا
🇵🇹
-
🇨🇭
سنت گالن
🏆
مرحله مقدماتی لیگ اروپا‌
🇪🇺
‌
🕔
پنجشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه استادیو دا لوز
🎲
با بیش از ۳۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
بنفیکا در ۵ بازی اخیر خود مساوی نکرده است.
✅
سنت گالن در ۷ بازی اخیر خود مساوی نکرده است.
📈
میانگین گل در ۱۰ دیدار اخیر اتلتیکو مادرید ۳.۶ گل در هر بازی بوده است.
‌‏
⚽️
نکاتی در مورد بازی‌های رودررو:
در دیدار رفت، نماینده سوئیس موفق شد با نتیجه دو بر یک بنفیکا پرتغال را شکست دهد.
🧠
بودجه‌ی تفریح از بودجه ضروریات زندگی جداست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r8
💻
@BetForward</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/funhiphop/81544" target="_blank">📅 19:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81543">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehoX6TkFOJj0kgPXVq5vGONfy4mPg7bD_FTxJfeY2cd-IeWJhDpmWyu7JH60lVxEZ8QLZ-yfPe-NHNxJWnJugjDEepwK51DOT2QStHk4v8nWh_IbKzbduN0Ko0CTVeqm_AbUWOm_nz3tHXXY8l_KLUnu3NK4yVs3B8aPmwH5ng1C8E_l5S5UsN7BOjF0ScSOxSudvYJFwoRiDjQZyUf_XiLrd_5iMAhNugte_jgijdwxK-QmAIRXDN_Kc8iQdkAn85DhDAV3hSnx9f-2xtomFf0gf2E_bU2JT-JsxGvfC1dSRUt7UiZk12O5kBOY8aSZtqzqt7M18kXNidxLeDS81A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران:
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/funhiphop/81543" target="_blank">📅 19:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81542">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxOykL7OLvvKfb1fzms3DnDCwKA3Az2yiMfANyv6mAeJi-OwcQUUNoIrIQHOUc-wMb-mpuH--BU7HrFwMObc7k3-639VwmZuVaxy1aJ_5e3VzLPpx7Oanh3FlERLz7dUBX022z0nDp5m1kRaIItfMo0cAKSz6_NYgPOGjbmaXZbEeFHI55FqUnR7xC2WkNSGYN7bT_Ct3KrSucoDJ6e_FoM3H6fXTXV33NDp5Eg09uFkZsRz0MUH22oH55tTDG3NXk3BMQqPqx3h0PfxpLP2aULzv_bQ1fskM8nV48uOpgKB6nPcckr13xeoVqD49ZdLUm8qqOxfOHpqdADpxQnC2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلشیفته چقد ترسناک شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/81542" target="_blank">📅 18:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81541">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFqv-2NJwU-MsfhWuq1wnbH3im9qq4mrv6JmlWSm_jKIB1OFaUdtKysCoLSUWdWurqO2GXFTnJxxYNaP5CMMZqzKNHh2OzOs6Mikt7tu2jdGAxqztjEicu5MAerqz2Lf08GTemXzg0v0mrGDrlbXm0TSrUW3IVKd368Er_OmVJOnU1WxmSmhTs2-teiOwtZlXO0w6tzPzk6i-DMux7w3Ehn4OTzpG_UljmbuXRkK6M2NO4o90c2sSn3JtrU3VaNVSbljottwufImorfTCyJk5gjKKIPuCM3bp0b1Jj4923NAARS08Q2crtvMnbE8UMcr-I6ZUPwML3AjTkVX2rYE9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام بنیامین نقدی، جوون 26 ساله و از معترضین دی ماه صادر شد.‌
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81541" target="_blank">📅 16:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81540">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sykDJ4ItBp9wrUGLlocxt-fBq3oDvpeOAO2n6qHjtBEGi8EfeFnhIe1vMffpzHAJwIqEaDwCWqj00A07h9u8yqAp9nQkDc1M9RBrr5nU9Df5ExA7K3U4l8hNbLYHZl2Fu1WfSARWkQKyGfCWhUCqSFT47NJgHzL2_-4d_dEfOLp9vYRoysheKfZyYZUAMNDB5lO4dwJyU0Os82kUhBRmPaHWt2YHpLFazmkoPqUkppJpg1pekN2GO_x3jMajKuLQ1RUY5MBLtN8sXOMjfnjTHEbI1aGlmnmIAA1RlwSlFG5ci9No4ZHtExNVvZXhN6n20iZX1-x6lvnDhmGphRpIog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیج افشین فدا بلاگر مازنی بخاطر استوری که برای سه جاوید نام اعدام شده تو اصفهان گذاشته بود بسته شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/81540" target="_blank">📅 16:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81539">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">از نیرو های مسلح درخواست دارم کره‌ی زمین رو منهدم کنن دیگه زندگی کافیه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/81539" target="_blank">📅 16:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81537">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGuidskOVLpNpUWDu5JMxRfhjt9loDq22EC44GwUkBfPi3v5GMBRU9na38y_vGSVaj8t2eCcfPzQY1jeZDrscToKgcYNLwnNfAbYbyl4x86D4ILW4OsfF8DJVmaQ3a-c-92NvnNozqX8OeGd8XV37ee3P5xe_49_mZ6nNHmS7151a-pqFsYG3KjqqBE3qfzYjReVbz1aeeeXhWx630j9qd1_4EB3qj0XEoAy22bA8T-rfVAYngWlpigqb42yMuzwvoVmUpLRsk1QH_TvvmkdCRaPfHqxnC1fy-jKu_QmAUFBiH4C5coK96555WMN4VXCy3SR-LPe4uwnbnT6UCMSRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آفرود سواری در کشور ممنوع شد
تصویرم از وضعیت یه پیج آفرود که این تصمیم دولت رو به تمسخر گرفته بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81537" target="_blank">📅 16:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81536">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اشکال نداره چین میاد بهترشو میسازه
🔴
چین گزارش‌های منتشرشده درباره برنامه‌ پکن برای تجهیز ایران به سامانه‌های پدافند هوایی را رد کرد و نادرست دانست.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/81536" target="_blank">📅 15:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81535">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWpJlySxe-p6wUyzWkeqQt-H-qAZ-wfJlNaKBZrNxzELT5GXTC0htjUyMO6erjuOInRu9Hf5KMSpo-lEUItZA2a5JCWQX7QA3hs-MffOrEdPC362AyK4CEuemBDKAN7YY7pUdY8_la0ABEqPZ5rxSKj421lq9pHlMZ3to35CBnIqCtyezbqeZpvZhA2gpkQmPJD9rcFwnFxGSfrTsmLRicz4jIbFVjdx0jCYblRbDPMDHdj7QAStXAYXtofNPFqWtLvMpEgy7VQT0GLy1eLbMIwFJr--jrJjVbbz-hF8q-CJrWGvJrfLUzFukUG9EapNLf_JMOXdQjJGd2m_TuuB5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده اید؟
صداوسیما: امروز صبح در پاسخ به حملات آمریکا به ایران، 6 تا جنگنده F-35 رو زدیم 3 تاشون کامل منهدم شدن، 3 تاشون هم خسارت دیدن چند تا از خلبانان جنگنده هم کشته شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81535" target="_blank">📅 14:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81534">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qS1t23kUxwAsMK8wwApqJymzPYLmUKK_XCky0FJyr_6FWe2wdwCBsm8GKQnBdBatXYuH6OfkhcsEgionMa7aw0kIpSIPejZwhFuoeDNYfcSkLVWPVOpvXiedNpFC9Lrpl3LitlvBYD2EvaobpYcQH7dFUD-DPgzMpRHVqwg95A4ll54add8bNLn_OzcqqkmTo7NvObnJcLk1VEJyIb8srqCEdcTBKxA7WiMiHlogls-8akrC6FJjjBAsY5XhXwaERW9ZtjQbSaEEVjjs6vNhTgxYHYMulKuTiD1Cs6xb6pj0ny11lhPkymF5RQUwHj9-GaWEs1-7P6F6ePu3Bwffzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دایرکت یه وکیل دادگستری.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81534" target="_blank">📅 14:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81533">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/533f3ca2cf.mp4?token=iRn7TOYLpr2q7MDQG3FYEpVAZFPnP1oxfBoC8CEkGM2Ux_LEo1OSoHBP_d-F3mi6cckl3RktDhOWseJI1bpdvJsOH-_M5xh_PS_6336xTB1lrWtrnNByw2uJ40GnwG5m_e0yZfMKt_37kFiLWTDoJ7e05tbjaD9EfESzvIrK7V6pF6RRgcGSv2UPG4tL7nudMGcKI48AXX1LYedlPx46eGZyWZlpPDyt-R37GaEsJ2VMu_aX22eriw6eG5ZFbqBXMtQMOPNx6Pg4uQ-h8fhjRfh7PneIRe-3TfB7m_4EifrschvKbNPicFBtF4_ZZAKYEMxjqehFE1MVPrmA-mGpnBgYajAonkkN8mZRaTckxncTVbfA6z1H259RHoS-VnDidMA-ZbmTLFnjb0BHYuYoGShrjODF1renEfx7JZLEYgWW45ssOQzY_zccZCagCQB5jyNzRm0VNIABJMJn505B4Kdo-iXCKtFPWVGWuv53qeqtEFgwjBD2ZU6tqNcRXrEF6raBEIhltBDaItk9ajKDSaXQ6llXF3LDtc3WMHBmQH0MEHBofYxHB6Qr3w82xfk86dIrNUqBmdrJ70OJcFu-RrrvFsL_brsNqJy7QkHr4Cwm5P55W8sdQ5ezJpJGjN7wtow0g9BZ3ovZHcNyl6whx97nRRfUfoPw7cIO8Crk6Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/533f3ca2cf.mp4?token=iRn7TOYLpr2q7MDQG3FYEpVAZFPnP1oxfBoC8CEkGM2Ux_LEo1OSoHBP_d-F3mi6cckl3RktDhOWseJI1bpdvJsOH-_M5xh_PS_6336xTB1lrWtrnNByw2uJ40GnwG5m_e0yZfMKt_37kFiLWTDoJ7e05tbjaD9EfESzvIrK7V6pF6RRgcGSv2UPG4tL7nudMGcKI48AXX1LYedlPx46eGZyWZlpPDyt-R37GaEsJ2VMu_aX22eriw6eG5ZFbqBXMtQMOPNx6Pg4uQ-h8fhjRfh7PneIRe-3TfB7m_4EifrschvKbNPicFBtF4_ZZAKYEMxjqehFE1MVPrmA-mGpnBgYajAonkkN8mZRaTckxncTVbfA6z1H259RHoS-VnDidMA-ZbmTLFnjb0BHYuYoGShrjODF1renEfx7JZLEYgWW45ssOQzY_zccZCagCQB5jyNzRm0VNIABJMJn505B4Kdo-iXCKtFPWVGWuv53qeqtEFgwjBD2ZU6tqNcRXrEF6raBEIhltBDaItk9ajKDSaXQ6llXF3LDtc3WMHBmQH0MEHBofYxHB6Qr3w82xfk86dIrNUqBmdrJ70OJcFu-RrrvFsL_brsNqJy7QkHr4Cwm5P55W8sdQ5ezJpJGjN7wtow0g9BZ3ovZHcNyl6whx97nRRfUfoPw7cIO8Crk6Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
دیشب مامورها ردِ نوید زیادخان، همون فردی که خانم‌ها رو‌ تو لایو کتک میزد رو تو خیابون خرمشهرِ تهران زدن؛ بعد که رفتن دستگیرش کنن، این مادرقحبه با قمه به سمت پلیس‌ها هم حمله کرده! مامورها هم اول شلیک هوایی کردن ولی دیدن تاثیری نداره؛ به پای چپ ، پای راست و…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81533" target="_blank">📅 12:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81532">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7XthsLGAbueYTke__O6EqA1OfNJX7qRRxRkneRRLeQd_t-Hmg_-8Fbvq5VUU-2cOHTmdWd0weaAvTBhOGM-p56BL8po1f93TN1Z0NbSmAC2EYoAUB7eOrFfGYwTyZ_q9FzNJhLkH_zZxqnq6TstEvrohjg3V_WUqHJDApDjuAmTNKucJCykPIQzCbC35ukmowrgCXTIkVehNoOcnrVpBdRzRiyYyFwQhYq_8K7jNsOMeHtZECvJsfPc6AyiZ_nCPszZCpVyeXBCasmjEpT6wTSwTK8quH4zzeHo23n7Ish3D4zPoP0Spvw9or1j1rHCKjrYSHJNYB07sS_9QubGBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دیشب مامورها ردِ نوید زیادخان، همون فردی که خانم‌ها رو‌ تو لایو کتک میزد رو تو خیابون خرمشهرِ تهران زدن؛
بعد که رفتن دستگیرش کنن، این مادرقحبه با قمه به سمت پلیس‌ها هم حمله کرده!
مامورها هم اول شلیک هوایی کردن ولی دیدن تاثیری نداره؛ به پای چپ ، پای راست و دست چپ نوید زیادخان شلیک کردن و این گراز بالاخره زمین‌گیر شد.
این مادرقحبهِ 36 ساله، قبلا به اتهامِ "ایجاد مزاحمت، دعوا و درگیری، سرقت، ضرب و جرح، مزاحمت از طریق فضای مجازی و تهدید به قتل" زندانی شده بود.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81532" target="_blank">📅 12:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81531">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7zHFqk_Ub_EO65X0K-bk-pwuIHw2w2l0R-QfyPEfwcSUbGS_GuFg7PHBTcEBOCzZtSY017x058p8Qw0ZcD1n9GTgV7D073eZciBDORSSjyuf3nUpPOBsiYitYqjIg99GcSXSNGXzcBubHvYmTX6Q2evfH9ZdU0bpkI4J7-WiC0W8HePLJdhclobeM6E7fzagQM3uLHgKcMI1aRx4ARnTe3IH3aaVaDNV6-Fs9O-hDyPZrNhqoxqKISfJdSC06NOvSn3brTJamYHJE62RyPkMDwbaVnbNmqBnA8pnMXIctFmk_3pz7q_jTKsH44TxFoDm-RFXzq70U5MIEpNyP3mVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
بنفیکا
🇵🇹
-
🇨🇭
سنت گالن
🏆
مرحله مقدماتی لیگ اروپا‌
🇪🇺
‌
🕔
پنجشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه استادیو دا لوز
🎲
با بیش از ۳۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
بنفیکا در ۵ بازی اخیر خود مساوی نکرده است.
✅
سنت گالن در ۷ بازی اخیر خود مساوی نکرده است.
📈
میانگین گل در ۱۰ دیدار اخیر اتلتیکو مادرید ۳.۶ گل در هر بازی بوده است.
‌‏
⚽️
نکاتی در مورد بازی‌های رودررو:
در دیدار رفت، نماینده سوئیس موفق شد با نتیجه دو بر یک بنفیکا پرتغال را شکست دهد.
🧠
بودجه‌ی تفریح از بودجه ضروریات زندگی جداست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r8
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81531" target="_blank">📅 12:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81529">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">یک منبع آمریکایی به شبکه "i24NEWS" گفت:
حمله شب گذشته گسترده بود و تأثیر قابل توجهی داشت. این حمله تقریباً دو برابر قوی‌تر و گسترده‌تر از عملیات‌های قبلی بود.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/81529" target="_blank">📅 10:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81528">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81528" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81527">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81527" target="_blank">📅 10:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81526">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81526" target="_blank">📅 10:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81525">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnAJovXw7p8fhqCwAXxSQx2eP3HUx3QGVxDuCo97TLQdihNm5EHtyJLJXmOnlCrzY-BQ3vL4X8i78HUhbA2x2YqlErO5gXrpHJEa2eJ_-rz3001iMgTJp5HiR16hsIAaJbp5XKmeALtGHRlXid5TnWht_jXtPYzrQrmY_FtUsUYSV7eAuHqUT705auVKv34jPlRvCw1vAz_72pkl9bvUxYu4gd-0hmrY-A-t4RsVEHorHpu3duyF51esBGvDUlZFWABtrdgeF-358DCJYoDPmgXh6qwH6R0QyX0pWCA3F2lv4PBzp_9nsUNOJFZrMw18hM2652ekgY4ZEbs5BKLBhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای کیرم تو این اکسپلورم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81525" target="_blank">📅 08:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81524">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اینکه شب گذشته آمریکا مسکونی زده احتمال داره یه پیامی باشه برای ایران واسه جنگ های بعدی که احتمال داره رخ بده، که امیدوارم کصشر باشه و این برداشت صحت نداشته باشه. (اگرم انقدر اورانگوتانید که فکر میکنید آمریکا کصدسته و مختصات اشتباه به بمب و موشک داده و صرفا اسرائیل نقطه زنه نظر ندید کلا)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81524" target="_blank">📅 08:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81523">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b757b219d.mp4?token=G360l9NnA7kOt7mjmSCdMQS4fh9Py5TukuhVCHfkyhs3kF4VfuZzH1ssnJn20gE-xCT3ZUVvYm6bCXHOLlDdfMWpoQk0SQ7GW6V_Otg6_GVih__V_hNW3Ks1Aiy9iJ4gRFcOL-71pt1viVjYO3qtg53HCttzGvG1kitpxX2WJYLoGsH7rLojHLm5KBoPG5O37JdOWXcJxxkoQDeuMkf--865QrGq_n9mJB2kwol_e7vq5dOPT2CKd1wsEg836m86cnlBH3Iq66n7DFah-4DheM7BGIN5xKiQD2kqaX5rSPGfOPkVo2OESbw5M8jMjmaBTGRbUP7TYrXmKeSxIZNiNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b757b219d.mp4?token=G360l9NnA7kOt7mjmSCdMQS4fh9Py5TukuhVCHfkyhs3kF4VfuZzH1ssnJn20gE-xCT3ZUVvYm6bCXHOLlDdfMWpoQk0SQ7GW6V_Otg6_GVih__V_hNW3Ks1Aiy9iJ4gRFcOL-71pt1viVjYO3qtg53HCttzGvG1kitpxX2WJYLoGsH7rLojHLm5KBoPG5O37JdOWXcJxxkoQDeuMkf--865QrGq_n9mJB2kwol_e7vq5dOPT2CKd1wsEg836m86cnlBH3Iq66n7DFah-4DheM7BGIN5xKiQD2kqaX5rSPGfOPkVo2OESbw5M8jMjmaBTGRbUP7TYrXmKeSxIZNiNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">متاسفانه شب گذشته هم:
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81523" target="_blank">📅 06:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81522">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">نتانیاهو:
نمیدونم دیپلماسی چقدر ممکنه اتفاق بیفته، اما نسبت به شیوه رفتار ایران بدبین هستم.
اونا همیشه دروغ میگن، همیشه تقلب میکنن و همیشه برای خریدن زمان بازی میکنن.
آیا ممکنه این رفتار با اعمال فشار کافی، از جمله فشار دیپلماتیک و اقتصادی، تغییر کنه؟ باید این رو امتحان کرد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81522" target="_blank">📅 06:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81521">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">تسنیم:
برق برخی نقاط اهواز قطع شده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81521" target="_blank">📅 05:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81519">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">انفجار های پی در پی قشم و بوشهر و بندرعباس
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81519" target="_blank">📅 03:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81518">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">بوشهر آبادان کیش
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81518" target="_blank">📅 03:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81516">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a76739cd9.mp4?token=iZJhU2WN2IKP-Lm_1GdZIKoO43g8LXmLmTWmI1Xf45JrFOechf5n0EF2UFL9PCk2Asa7k0_2i6ms_-uoJJXAvi5pWJop6oB0IW4rnGGDUJlbmU0v8xnO0bYSf-BgB4otaqrBgDCIUTJgBwiM4dZrXvIZhYV9pmmGqapAAGh4V-OAS4dGn4q0wHJo4YyR9dyK08aV04XVlpok6TNUTyKqcEj0_ki56HxFpJEEZXAnSLpaZ9j8cS9bCtfkwC_0JCpR94eERuGEYryYWV41JVhn5wDWF7buyn3lgLp772yAUCHUoNdpsKRWtuCVndscsEtmbe4blo11hmRhHYdWeoPhFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a76739cd9.mp4?token=iZJhU2WN2IKP-Lm_1GdZIKoO43g8LXmLmTWmI1Xf45JrFOechf5n0EF2UFL9PCk2Asa7k0_2i6ms_-uoJJXAvi5pWJop6oB0IW4rnGGDUJlbmU0v8xnO0bYSf-BgB4otaqrBgDCIUTJgBwiM4dZrXvIZhYV9pmmGqapAAGh4V-OAS4dGn4q0wHJo4YyR9dyK08aV04XVlpok6TNUTyKqcEj0_ki56HxFpJEEZXAnSLpaZ9j8cS9bCtfkwC_0JCpR94eERuGEYryYWV41JVhn5wDWF7buyn3lgLp772yAUCHUoNdpsKRWtuCVndscsEtmbe4blo11hmRhHYdWeoPhFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان مراسم اکبر عبدی، عادل فردوسی‌پور در کنار عباس صالحی وزیر فرهنگ و ارشاد جمهوری اسلامی نشسته بود میخواست دستشو ببوسه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/81516" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81515">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">Game started</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81515" target="_blank">📅 02:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81514">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">Game started</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81514" target="_blank">📅 02:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81513">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">بابا کصخل بمب افکن نیست که رادار خاموش کنه، سوخت رسانه</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81513" target="_blank">📅 02:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81512">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">بخواد بزنه ردیاب سوخت رسانا رو روشن میزاره که مهدی ادمین فان هیپ هاپ بفهمه؟</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81512" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81511">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">حاج زدن حاج
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81511" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81510">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">تلگرام کانال روابط عمومی سپاهو بست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81510" target="_blank">📅 02:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81509">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">کصخل سوخت رسانا بلند نشدن که باهم بندازن، بالاخره میزنه دیگه</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81509" target="_blank">📅 02:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81508">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ مادرجنده ساعت دو شد چیشد پس؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81508" target="_blank">📅 02:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81507">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترامپ مادرجنده ساعت دو شد چیشد پس؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81507" target="_blank">📅 02:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81506">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">فعلا چیزی جز صدای پدافند شنیده نشده به فیک نیوزا توجه نکنید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81506" target="_blank">📅 01:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81505">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پست آدرویت تو چنلش: این روزا انقدر اتفاقای بد و عجیب میوفته تو ایران آدم نمید‌ونه از کدوم ناراحت باشه
🤧
🤐
🫤
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81505" target="_blank">📅 01:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81504">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">تلگرام کانال روابط عمومی سپاهو بست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/81504" target="_blank">📅 00:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81503">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">تنها اپی که سپاه و نیروهای نیابتیش میتونن آزادانه توش کار کنن تلگرامه</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81503" target="_blank">📅 00:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81502">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ این جواب سخت ما چیشد خوابمون میاد</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/81502" target="_blank">📅 22:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81501">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOVXNiqfelPd6eyKu3hNYR2AWcaMjvZjUNHrldiRoSW1HehVRADiNV4AatQhoIapkUWjFZTzaOY5N6njMWpL57G7LGPSCUWMVirKcOLjedaGOnDX5d-sHjgnyDUilfREChU7K9w5Ph_sb3zdIaPc1eRrO8KSoxXQu6BEVTi_Ba-WJnqScgHJskcJaVBzuw6eHnVhbr87ZDVx0vk-eqiM8jxoNhNK0l1WAnva6EOSR1YLMlvorOYROID-14XwdpaoPuV_Pd31fgWX-b_Bju8WJpc4Y8Oal6QeGS4e8vgXtRMGOwiAGi1VRf4__7YnVoE_s4rprr-dlPSSG9GbsHXNUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برا دزد شدنم ۲۵۰ میلیون سرمایه اولیه نیازه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/81501" target="_blank">📅 22:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81500">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JiaTJSdvJkFM7tV_83frg2db3SdIY2-mRMX37UNzodPMO3B23iibKbfbhE_vIesR9QffX2CIts5oNgaRETuGw5rtiHp0bEmEB9E4AV-Z9lfcR9G5vVZOw7OMBPAAmO0SLGwPWpwn3zLD1t2-j5ZzKLmHzXX6V8sBOVLljZT1PA-3sIPIqJis8JvCcBr8ulY8Xz7xJs9WU8Nyj05nCL3Pzddj6vGhF7q8iV4z4i5nxJQVx_StLwIvQnbuSlsx6X_UpbRSuG3j8UFWd-hPekVbvMCF2i-2TIJY6rwOHS23UuZZMk7JcNilxMo9tUx2fuTlqiCWmfa5UMgWnDhECdNaHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
با نایت موویز، دیگه سینما همیشه تو جیبته!
😍
دیگه نیازی نیست اشتراک بخری برای تماشا و دانلود فیلم و سریال!
🤖
تازه نایت موویز یه دستیار هوشمند هم داره که بهت فیلم و سریال معرفی میکنه :)
💵
با خرید اشتراک خداحافظی کن و به نایت موویز سلام کن
👇
❤️
🍿
@NightMoviezBot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81500" target="_blank">📅 22:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81499">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نتانیاهو امروز با رضا پهلوی دیدار داشته
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81499" target="_blank">📅 21:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81497">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMm6qxgnbW2kuQiNhoVfr4DFDoq3T3XYHKG3OGyN9EDv_nTtKADQBnGhz8kBHwQ-EHA4HOmZB-RlbPjygt7RJX7JlIlUe2QC8socqfuyj2zZyEvMaX7sngTrcY4dKyViaVN0z6WxYYJ4wOIoxHFXgD6tBUa9nNWBuXToS9fLZl25N8SVEjgXBV9Qry9mUYDbXETDB6ouNIZuznKuLwp4zRsP0Jp7UkWlJtqUU-nQ6yNyRlKPxFENCYHyr7vFdk5QwMaEya9H52akk9XcGwA3y5HgCF1t0e6MKEL4VNPJjQCB903Rlh5qbQIr4itKF8uSJ-AXMTO78RHqvg380nS13w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام چه بامزس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81497" target="_blank">📅 20:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81495">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYyRvIIPL2AG_pGjo8cXtqm01wrK7D5yPGjYXQZTfS92xqHL3YcqHbH9jam_SXgfsQNlzbd7Tb5fMqnEUtEVFHIPQ4xi-Kwr6K8Eadf4GRKQof8X1dFmK6k0El9_h2FPcXW9AdeR71zTtiCg81eDA5zPC6CHrV5iBlXbXyAqijAWzCMrC8eM9lq-IIafelpx-J45wFMnULhJS46p08aMm1Lz3g4OfGKV7fj7wBundj5PyvsLbCPTzf3g-ezn_aTAHR2J15cps9AOb0zTK0Dw0shvRQtEhoTx4pj3pBQhsxOMOGVmOkPMbEwbGXWT1T-N_ocm3P5ma04dRlGlzac-rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی بچه اش رو دوماه زودتر بدنیا اورده با عمل که فقط تاریخ تولدش روز رند بخوره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81495" target="_blank">📅 20:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81494">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXTdRpUWU3zmlfeb57cjZdySgo6r-gTF7tM3cG5F5NdWRX3kJ0zTSkV4AtjS1e8kJEpV6k8t7UxJA9Gn8VH-NVuOqPhtZNASpQmloKKRwbBTfbeBzsRg5a_tvE3InEJpx2sbsNIELlalPBlKyiylXULhTevQX4jYm73m9awpPAe-oKd5ICxg2D60LEoye5fsLTkswlgw7ZNIxOZ-6aLkBMJyWpsfkc0NY2tu7gA72iWXs3LxwqEBWQ1UEZ1NHaYQXPE8GNWi_7Cx5g5rxZQMyqvDXDLjGI_YozGGMeD3BC8xgiO4VWd9G4jY7DrWno8VrgZdjpTAQQZwrS__kSI2Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوتیسم پسر کوکوریا عود کرده، بخاطر همین دیکه موی بلند جواب نیست و باید ببافه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81494" target="_blank">📅 20:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81493">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پرایم هیچ بازیکنی اندازه رافینیا ۲۰۲۴ بهم نچسبید</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81493" target="_blank">📅 20:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81491">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">از وقتی تلاش نکردم برا باز کردن پیچ خوردگیا هندزفری سیمی کیر رفت تو زندگیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81491" target="_blank">📅 20:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81490">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پول ایرپاد نداره؟</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81490" target="_blank">📅 20:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81488">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L1v4FgTVioRcP9xov2OYMqMnMFdbxFMxD8yBBh-MN7j7Bbo0zifSEgxgXUSzOgrhiM1yi4vDLaZQvehBz5LaUw3pEXIOk3QXysqNfSP9X4pDS0R2qjXRSsKPCcy_27nCzf-kWdtq4YyB5yyH2s29dPzzev2YzJ4qX7pADhiabhTf6yMP1eqMtK0cGEBE9LCrJVN2OdGIMrlWKxTtGr2tnOrnZI4xEhUiL9gkQbpxjpmKb_OtdZ4sP29vKHbkt8vgAYpbJANrBVPk0ttloH2y-WlHBVEKlAcHlsHhV1yOhi6_XHkGXh1ZoCdJq-qtE-ZX_vG_qs1kASGmzbY-DqF-Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b2x3xb3cS76DXSDN9k97__1O9LjHNrG6qn7M4-5PPBr3ezAFDAGZkrQd-EO2lX4DqN2473jCwTWXUj-13wbdREmdSLd6flIuY_fH2fsOfS1EiQOUc-Uk9s-Cmw66tGOtz1D3geHT7t8wTKTWriaT2Yq7ItIcGoMZpIM_QtV4Yx-EH0YfdL5MXxELEPxXVd_NGjko7157G0gssfm1AxXIxPuh7AuMZgja1we9WYw-66MyggxVoJ_QWHpfPPSZRSNC3RfjI3q3ZyG_WFqQPCNC8Lc5CnlHZ_kVw-POVhlbXWmFlYNvq1LqTlnNx7RYc_inAIfx5ZvaaPLqXq41UH6_DA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رافینیا شبیه زن جنده ها شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81488" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81486">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e2m8Qu0fMwbZ2OxlxmR-WbwALoFN4OibzlupFheGlKgwZn0A9IRaoXObVQUgUwooqKhmXs45XINSHNjifzDis9m2LGDrjMgETYp073HbSf-aXzLwmnBhY-J-POGbYIgJLRVSrz5mspkX5hi0q12fagbpPrvN6uZzNyh218cMPW-w5XnpqLwCqOCd1lhQ4E5Iaz18ahcdry-QwdS_OPWD-LVp1wpWz-29-ao9QznGRJNcCEF_Iz1YY1BmPWwKWcRfKSD84u0889HHDNzSz_JvEPaqtsBIUgxybc3ELWW0qOYZETAq4xAHcJxB58RCSgl5s78IPc92IITIjiiKKALcPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QfQOjhw-14w6BTjVXT7hCceqDq-dS8YTaD3ZhbGADVeT0N_Au_l96gllCbYbQvU-6xxyxO_1mm2pfDy5veK9AGA2J_xSHMYV2ymXviOiiaeQ7ItLD8E_BEZXeRBBGyGe19RV1kDxZgNGH-HZ9tfiVAQs2XbThcv7J2LRDXmBV4X98tzKi-laRQQ4iVTUC9C1-WbLAeu7Li1wkLdNsiKOzwW_jI36Z9Wurq_AXuenKUO2f1RzYW0rRVFm7al-KGKDSbSrn_shx7kFHjOXsmF4XSu8dNZ6_CDq8a5T3_zrgsPjpk4vcdoa3eQhAAc4BXQ2WvUiRh56s2xjX_e1ta21pw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هرکاری میکنم نمیتونم با قیافه جدید وینیسیوس کنار بیام.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81486" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81485">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMZcAsKLwyMWO814oSR8tNehMmMfCqHhX4WHw3L7EZgW3z9NcHDn_FWQHUHdYayaY7gVsCqoKk7On0xMhck1V7XJS6ut-_cW9BkZQ-iFh_OVpfQySjyGX3kg-AoRujVvAO2M3HyDS3nAN9Sp0z1G3QpGbxAeVChFlYhhueYg5KCw5MZVwYWhaZ1hOX2h0vaETFakpBynlBNzUzxkKy3WRYV052Z8UtqA9-jAPhp_1nKn9iO_dwAqQrRyt9w4dmeLrAMrw6CZhbLc2JnMvIuWQBmOw03crm0b30fRIe0xnwU8h-X25Kg2w3vP_uPmzzhDoY3QkSOnLlsB1wsA4d1-dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چی بگم والا.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/81485" target="_blank">📅 19:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81484">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHh1kzLpS5sR7TtHCXxJyB0Au7FsoQiDRJPTvQMxwljjQC7Upd1muh6nkVldgAYnt_O4Rm07z5DFN3gLg5A-csmbQfKwk1Er1MNqb-jXBeBY0Lx4B94UpcfKJ8ZpXRNLdvV4F7AJ3O2U103vP8dPMCba2eOjAdG4LKShYG03vXtsldMjyiZXQtt_nx78A2OADlPtvhkyIcj5wESnNx7BZytJs959f-Ekc065XG06P1GZNvVgTyTjmkkIP1CsrcTR-a_c2qR7nkhJ263E5QssjA4ShCRtOC85PyynvXaCS8lR4vaRd9GUjh0S5gU534P7KO4x86kkjjM5lBNGUUU7nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
اتلتیکو مادرید
🇪🇸
-
🇪🇸
ختافه
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
چهارشنبه ساعت ۱۹:۰۰
🏟
ورزشگاه سرو دل اسپینو
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
اتلتیکو مادرید در ۶ بازی اخیر خود مساوی نکرده است.
✅
ختافه در ۴ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر اتلتیکو مادرید ۳ گل در هر بازی بوده است.
🧠
تحلیل خوب، آغاز خوش‌شانسی است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r7
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81484" target="_blank">📅 19:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81483">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHJym4FaDdAPq9YRfBvrKrAF3Vdns4FbcpSBj-OTrXAPSR9Iw9H-bN0VvaB-US0aLqDh7XBIHNbcMoNv6fx6oSw9eH6HhHAEz38cHM0sg0XY0kRvy_wwvBz785z-e88r0YNGNLX1rE03DTdCnR7QfwBG_-IuwmfHvhOuxKC6IdrPeLh6xvg9Q3V-2lQ_mqCEa65N0Jwh2mOLwSFHBBPLVNCFfBVs4MD6QAhqaHKqtvFEJ4rR7loFvLlltJsRaxdIC6j89JINFT20bbj3_bEPRuHBrmhVJ0DRzEJYaUJjPVKkKOfq9xNn9i-rpLPKVsf8atLTMOrjcIaN4JAMxnBzBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس جدید صابر‌ ابر و دوست پسرش.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81483" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81482">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gaq_oXBW9DXXruESBGccafllxOdoqKQJR_csW-0ejI1x2yR-ffFka3_RGUPYBrJmB2Y26nIL5b83SkiNJ7zWLclwqY9KH4AvLv0aQBuGB-FxlhYvNYJLoS9whrVg4wMn8_qiH--x1MbAAJ0fWIv9UO4zASGALg2RTZXnvDqshRyYwlm1hhHkP16qquyUr7hGOw9fCsEBSg6OWZ7UZC5BbSMBPEs18AoBurZ1I2Y_4pTmmvlbSRwm-cupbBl4CWAMMcT7yL8jvoM8gB7lSZSv3x2lNM4wp29IkXRxSxiVdbO5cSKGxE1ejcZYTGw4UkXEaKxow0Mqj13RJ8G1liOTaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروفایل پاول تو تلگرام:  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81482" target="_blank">📅 18:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81481">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVJzPx803VrADx-ce4tJq9rVeNNhdQ-ZFvZ-3vpyaOqsjnOYewouHW6WfwbxF2py60HwyjLw73t5HOBoBna9c8cC9nseEMU6pIhTI8S6HIVN8_5VInLw_qwXeVCga0GiVLn1qQxVgia0QlFJWkGS3OmeRU7Z_wBTJ0j9h3lmWVH_jdCSUyZr-L6y5t2Zge2REwWnFQdSrUh1g3E2Ylaoq-GryA0XleTYtQdAuC-NXQedhFJUlYmoYWj-Cy49hsyjJYxmxzUFaVvzp-WjH9qXRsypuda5NFMj0gBonf9wwH8bAFUMV150lsF6OX4DPd4q1rlTyrNbvwygD9-UCfviHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش دورف:  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81481" target="_blank">📅 17:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81480">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">عاشقانه‌ی جدید عرفان پایدار و شاهین نجفی به نام "داشی" ریلیز شد.
🎵
Spatifay  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81480" target="_blank">📅 17:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81479">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZLoVKRgNOKGk9F8ZEEBM3SARQtkrAKmehUplBVc9j38wuJr2I3ojGI91zYBVjk1KQVfbXbSeA6xZcGX9pFMB6gYx3Dx72tzJdMVeOmSsmYSiQTnyhXQKEszQNsjetGBJiWJXHosKb8Al5j7IgLKuWlnGhEtJrHsR7mhRiRYw-66wvqMUQDbn7j_B4G9oEE-osRiIVRepAytnV1HgogGTeaACUKP0IVordZxs_NT3n7CpvrkM0zxZD2S-oFfyA5qmxlnhs-FXef6l8zzE1PZi0yqKMw_CWYFu-CvbdYIy8sHYd0tafl4qKdmL-cie6E26kPwf86218d78EvNRNoKhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاشقانه‌ی جدید عرفان پایدار و شاهین نجفی به نام "داشی" ریلیز شد.
🎵
Spatifay
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81479" target="_blank">📅 17:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81478">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8ti4Aa_Jq2LF2-SWy1RDK53El8YUMw2IzbnLbDaWj_VvSC63BNpFAR5jfWF5PUYCj_W__aISTg7agnh2lu_bjLpP8-Yjh14jv2Zt2-zU0Fp7-hpgTH0Wpw6nJ8NTh7vlcpcAhu3RyzA_znExOefefpps6RVDEfeaCqxVYs10LbO7mQC_QEfsSxhuj7Ptk13peJ5ncqgYkuk92eD448YmX9DqCi4-M2Luxwuc7PaLDKyMRE-Yc8qeVjCfIIrfHusvzsrkrzapV891vtw_YANqQ5dlVmbzoIGDvFi6E17ChKUPEOAyokY6vAM_0fsTtNeRWADgtmsgRIacVFrgTOM2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاول دورف داداشم، به اتهام تسهیل فعالیت‌های تروریستی، از طرف سرویس امنیت روسیه تحت تعقیب بین المللی قرار گرفته.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81478" target="_blank">📅 16:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81477">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ: ضربه سختی به ایران خواهیم زد‌‌.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81477" target="_blank">📅 16:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81476">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">منابع نزدیک به سپاه میگن در نتیجه حملات دیشب عربستان و آمریکا در عراق، تا این لحظه دست کم ۵نیروی ارشد حفاظت اطلاعات سپاه کشته شدند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81476" target="_blank">📅 15:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81475">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اسپانیا با پخش اذان از مساجد تو بخش هایی از کشورش موافقت کرده.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81475" target="_blank">📅 15:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81474">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اسپانیا با پخش اذان از مساجد تو بخش هایی از کشورش موافقت کرده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81474" target="_blank">📅 15:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81472">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWZYoXSKQa5XCjFRxJz0D59bBggpaCZ_-lLF_jgpguN8y1wr2TJuF7vq-hc6xD2ql1nUEXQsLNkq_rAiZmiD4-ZMcFjGZ3blVOhd9PktxskIQdZZp45Rx9slCM_et5vvYTQ2-oQ45bZjRKcT4VxDrGwmctnxJhL5ZP2GaUcfN5UZbgAzSiTydVVInJwQ9zlAmitf2969ANIw02Rhloc4AmeFzqgZN_rV5wdxdIy9RLN4cW78oFC_J1vpzLsILmOPomV2Aj7EyL_TtveqYfDdEaPUFFgbTRbf7bfT3X-9CwVUkUWhpRK3jnKqnXv1JcV_sgFUnz2arv0GwCQQcPupMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچکس نمیدونه چرا این پست انقدر ری اکشن "
🤣
" میگیره.  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81472" target="_blank">📅 14:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81470">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lpaGbcs--4nKvbnf2443LdWKznlGIyBQUao1XhszSsdx6QpL1Mu9wUYVL6ZBxqfVMgBobCG6v-AfPqbbX3bhuOJqx-uI5hKD61D-JpHBNgKzH1ruDgLunx0QvJSTB18vgyPm9jMLfRaMFkU_53lAYZrwD_ag5rJzPXrTO947CHEhTLCnvlFXkh_fKGmHJ58_c1Ec2sXRb9CrozAOJWNqUqlQ2NJuSwMVfDlOZIX05liWQxbC2uVImCj9wVXQhi71lsYHWmDFLGYkZMg6-wE4jlOJgDwcxpazw5ZXHsB_BSjf7e4rbakQsechj0j23-uETDTTZf1BGvxAIpinCLT02g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e1yatLwGIlSvKxgo6yXeapVL9X0YMkOhVLWdraaCK0WiaJG3uilAoxLgiN55TiBiteFIeae5p0PgeZ0GFwcGBhS-IXGlL4KWtWVwFFAJ6J695TcD7d-6imw5sfa9OWx9aTHB7pmzzWmVCyzmJGw1CORl-E2cpwCnPDN_o_6zYmN9-yb-uauXpYkTGhfAKsyfEj5vkcktVAJ0Ps0QCAUGIV0OeTqfQHMkDlDRSznOb7gvoqsRrfrobX6HBmRnBe-Z2bNOYTg-vl8y0TesV-5dGD1PuosByiYiQ_UABAzWkh4HyvXd3nZFtyLuWLiOx8pJkEaKY28IPIWpG2SxI7YwAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پینترست چرا تبدیل به کرج شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81470" target="_blank">📅 14:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81465">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اگه این با سپاه همکاری میکرد که الان همه تو صف اعدام بودیم</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/81465" target="_blank">📅 13:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81464">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پاول دورف داداشم، به اتهام تسهیل فعالیت‌های تروریستی، از طرف سرویس امنیت روسیه تحت تعقیب بین المللی قرار گرفته.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/81464" target="_blank">📅 13:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81463">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">دلار 193
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/81463" target="_blank">📅 13:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81462">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcvVeUx4wuthOoiWHVBd08QS4ggqRmSvgzUu-fTuAVQVXzi_SSNsUxhQZFGDhGnqsqH4Xd7DyHQu3Sohf9DD4TvPiEucZPWhfSuEl4kh5gxg80nPAUDWEx-af90Uz4Ob3KgLXJjT134FKiq_nSfQRGkNCeEMxfTqqUx8-E2vguagTn9382Gn24LdINoUpc4LoZvOGIqDJyc5YIXzPJ41Q2jzvIhe5IeV--TWOt2JpTrmo3k9swWqFbbZ1W2-tRNfCkl0vfEH1zD5bRvb_BJXLjpwYc-bzWH_nsYu_N-fqaYcjbK_qY44nw92LD066HkVctu73d7OWJbAdopmUQ6MUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری پیشرو
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/81462" target="_blank">📅 12:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81461">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9SfAU2WOhfsH0Xck8r3_o4cU9q2ykoR1dFkrwy3_1_jzDx0kCUg1AAektx2DLmIUTRzI3yVNd0w0cmmPaUsM3YLgfPWWUPoDfwNrHL4lBfLrnh0w3u-XkrCirdiKJ7Lywk2LTGkWj9IcU1VNSQEhQNRMSr4NXTBf2K2xGT0NoSYXGBDHfYyTiJLTxn-65Yybyzr-Qo05nVDSBWVgn3xSvi5KAvj9IXpQ83_HCGmimrouJ87uBqBfMVKdoeR_n6iBoc0HJ0W050DWZDaXPnSvGk2VapZtTljXi_GstrUdcckxO0Pf3J1ogk-okAGiZ8WWLKyulmONBo6ewrVfDqR7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
اتلتیکو مادرید
🇪🇸
-
🇪🇸
ختافه
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
چهارشنبه ساعت ۱۹:۰۰
🏟
ورزشگاه سرو دل اسپینو
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
اتلتیکو مادرید در ۶ بازی اخیر خود مساوی نکرده است.
✅
ختافه در ۴ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر اتلتیکو مادرید ۳ گل در هر بازی بوده است.
🧠
تحلیل خوب، آغاز خوش‌شانسی است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r7
💻
@BetForward</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/81461" target="_blank">📅 12:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81460">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">از الان تا ۶ سال آینده هر اتفاقی بیوفته ربطش میدیم به جلد مجله اکونومیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81460" target="_blank">📅 12:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81458">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">هدف یدونه پایگاه آمریکا تو اردن بود فقط
💔
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/funhiphop/81458" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81457">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">تروخدا اسرائیل باشه تروخدا این یهودا خیلی راحت نابود می‌‌شن بوم بوم تلاویو اسرائیلی‌ها مجبور می‌شن از دریا فرار کنن تروخدا پدافنداشون ته کشیده ۸۵۸۷۴۳۹۹۴۴ نفر ازشون مفقود می‌شه کلا اندازه یه استان ایرانن ۹ میلیون جمعیت دارن کلا تروخدا تروخدا اسرائیلو بزن سردار
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/funhiphop/81457" target="_blank">📅 01:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81456">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ببینیم از لپ لپ اسم کدوم کشور درمیاد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/funhiphop/81456" target="_blank">📅 01:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81454">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ml1UZJiPYW32YqO-XjnvDU5nEDdqrE00sYzrENLqkw_D-0IYaq_ybF7pBlhC8ahk4DMepSSEtWTlNl1WxXQ7H-rpO3ahwbi7oOKVGFewy5zq52-62Fe2ZpfeQTn38x3j6FEJjly4_WMExs4gWYWR8B7etiWdt53OlktjxZ1CTnYVq9BEagMltflexFrJxbtNjgEjKMKNEkxpv1CSjghbXdpMu4o-BvNndmKMr8aJRMLDmYKxUdHtz-pwfLRJUoGqq1lasVQBCULYd8QmSBb85dvNFgCRolYFBhrZ-Z4FJtV8biTHCtUyus4wmljn0wh1vv7QoUR8HISgV1sVqdZd_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/funhiphop/81454" target="_blank">📅 00:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81453">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Auu4OuDEVdvgEyWteuiXjGxv3gkR-OhVnlvmkN7Y3H7r3psyr0Hm88uIidD1IxrLImfwYfCi_yDRsbXEHBiYbDZPkWoj05J5Vn4KMyt1Wgby2xqMkGntj0LvkmOs1fYk4HaoVO3_1owsiB6yKSpNv6GYoJHqKpcwnjxjX-8CzpesMpKg2LeW059HSx5lCZzIvUjl5pwRxJLp4Et7Kw1s0ei1XuSNO08hXlgebhMo4ONA5KcmRVAnN1Nwz80vn4XHmH_rYMe3TG5cKVALc3_tvQOex1NFWDR5kd0Fw70lEviOmMZo4JgNUL3iYRetbuFBSGASDYQVy0j92rbUr_7MFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچیزی برای تعریف ساده کلمه نیاز به یک توصیف ساده و فراگیرتر داره، مثلا خارجیا وقتی میخوان بگن بی طرفن میگن "من سوئیسم" تو ایرانم هرکی میخواد به یکی بگه "جنده" دیگه این کلمه زشتو استفاده نمیکنه، میگه "شیما کاتوزیان"  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/funhiphop/81453" target="_blank">📅 00:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81452">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7lgmzCTl-JpRMbojahsvD7DTgD8J66uyUEEQk1ngJZPXvH_Jv5KVdeBK9zoAFw3R_61zxWpO5lFtNAaC5dZeGE79DwNxlvfOV5-MHKRXSI3dat5dHaz5rudEBo7wTbsl03jdAZlP7CTx8rGhptK4Mi8G4zXbkDREL7uSnvK7i6NzNWbC_LGPJdJjDoHHlu30qTGoyE2Od2CTGpoIBi1yer0qhMsO1o2YTYbBOzl5srr_w-dL-d1DHZgJSa-ZQaIPstD8ugt6XevN2XChyW_1TQCWhc4Uze1HZEiCJQ8KVqmol1NKoROcq0FBIyid18WzIYZoitIvQOfVR5GEEvPbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچیزی برای تعریف ساده کلمه نیاز به یک توصیف ساده و فراگیرتر داره، مثلا خارجیا وقتی میخوان بگن بی طرفن میگن "من سوئیسم"
تو ایرانم هرکی میخواد به یکی بگه "جنده" دیگه این کلمه زشتو استفاده نمیکنه، میگه "شیما کاتوزیان"
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/funhiphop/81452" target="_blank">📅 00:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81451">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">#رسمی
داریوش ترک کردهههه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/81451" target="_blank">📅 00:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81450">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ShtFUMxAtoJvY9M6oOq_weiU8hXnp75VBGMg9n9kksXPs53sss_S2OakP_EuZNHqiieR6o4C85zbBmVxlCJ2jvKN5ugH3DylB88dCuJmtuf2qFRH4FqVb-obmnEs54iFrw5leUHA1kEAkuhKdCOJ_Cu-HmHHw0NH7D670tB2XsXfMbjQHz6E1Iyd1GlkEL9hwMfcFpdYh-pr9BS02O2CTBYLMqa5qKjaUphHh8QUxDPP1rQQ2QrpBCqc1EeoE0manu_oN0gVOglogtoxXedlpnTecl5qjo5eaq0uPvlYlB5hHf1ZQHJykDFU3XWJsdbavryciJOKVPKX2Os7EbWvyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور شاهزاده رضا پهلوی در مراسم یادبود لیندزی گراهام
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/81450" target="_blank">📅 00:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81449">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">یعنی جدی عملکرد ترامپ رو تو اوردن نفت از ۱۲۰ دلار به ۷۵ دلار تو دوماه ببینی و باز از گرونی نفت بعنوان یه موفقیت حرف بزنی نیازمند خیلی کصخل بودنه  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/81449" target="_blank">📅 23:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81448">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8b3FTBI6xOTcz1WpKabSYPvsCKUi3Xt0YkfAkD5X9xIJaSo8TSZlUkmyomyVgs6SQd7jFMr1_CmihygPPgH__-QtxQWk8fZVIGWIdbxfT7FbuHhz4FeAbWIsJfTq6QxazSnQuZWm3Wc2L4ESamjdz_NZrtPxlKeSjAHe_A0_K56DK6KrS4pvd0V8WrPxPAz_HwMD0Yd-JRPFReblAs2RFNGwzfDrZIFaX6exAzEPRQ2xO9uUdjcmL83NbZ65nZbRiEyvFZv6roo_P-Qr5_foQwShYy-UM6ZqOsc_YQAoD_I-QwEUmYJrCzU29I0ewcLWj1wgc_3xlfLx1KZ3u4BGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاپورتا سکته کرده، اما اعلام کرده که حالش خوبه.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/81448" target="_blank">📅 23:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81447">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">قالیباف: دنبال بهتر کردن
زندگی
مردم هستیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81447" target="_blank">📅 22:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81446">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gILct-06E91kEID6nGgKCOrErN10RjCPIf6pAB-YKEEQSupWAUCV2oBtpawnFwQir3dv0NSWaWZk4DvSsYaIWfhUZTklfSXtqy3iLIxtWwAQAadJ6AkukAvhDFWYpUj1BxPfDVLy1nWWi45jsyr1giVF4I7RiUl8wWdoF-MbTfGC32ERDjwSpNOQjpxvMh6ym87EDwedXw-zSzHYynISOYCsHGzPFYhbrgjtevTHnsOxSSSniAX57vvGvwDb8LehJYawmERJDkqD3FQoYzwcEwHfPupJ8I7Uk6kYDl7G2fezxQDXJ3QAJBS_Rucwe3QKeqZ_GlVBSLyjvsW3Bhav1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جعفری دوباره منیجر حصین شده، هم پرایم حصین هم شایع با جعفری بود، با هر کدوم قطع همکاری کرد بگا رفتن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/81446" target="_blank">📅 22:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81445">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromApexNet Shop | اپکس نت شاپ</strong></div>
<div class="tg-text">🏳
سرور مولتی لوکیشن ویتوری موجود شد
💎
🟣
لیست قیمت سرور ها
⬇️
🟡
سرور 10g - کاربر نامحدود 90 روزه - 45000 تومان
🟡
سرور 20g - کاربر نامحدود 90 روزه - 95000 تومان
🟡
سرور 30g - کاربر نامحدود 90 روزه - 135000 تومان
🟡
سرور 50g - کاربر نامحدود 90 روزه - 225000 تومان
🟡
سرور 80g - کاربر نامحدود 90 روزه - 360000 تومان
🟡
سرور 100g - کاربر نامحدود 90 روزه - 430000 تومان
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81445" target="_blank">📅 22:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81443">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pTNHh5nuQYm9if8OxvOWJBcVMmRiJJzYZFJ_Vm_H5dQUIBVoRomOjRYm94hMaGCLIHQlDiqh8vtx5Ipewu7JmxaIXTjynqlOcJGSoIpTou2y8p4DaoU7AcvQgrS4KindX6TwhSNWd4YI9_RHnGGJ4a922TTdQ73wXeO2enOrdrqwmzIAB2_XuqKqiSlC_pY4-Ov0oOZLOiZy_PM7FieD0r2ZDvXwXPXaOrbddMn9bGOUQnD3mVHeDc5K47b8hld5iFehpkPoYg1yzzy__qX-KbicLMaG9BLVO1qNmG1w-3IupKaAusmBrE-6D4wR6ZD0Xc9P_3fGojisQYosNk-aVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vxIMVXRNfzGi29uGYJXMhhJ4-PkJyXN_j91NwPUFo5X9U1kfjyH68Wsp4TGIC8WYwjP6RMED7_VYyVX_mnCXHmrF9f4OWGA6b3QkQWR3tVllxNCluCVDHwBEE8lyvP2NbbzKB-3f6ABlzf2SYQXRgjCH6JqEGhL5GdJnKdIqc2HTPfKGwBqLQCk5KRst2fuqkyRaaJqsqPNF9Drcvsu2_entJs0aFVJxAZo2FB332s1exYb4Er-S6c_cDNrx32wrowC_BPHZjJRF8-wWtaiJ3GwYDHkfxGmclzeh-Q4Ikmt_w05NByKsuRyDaKi0mtQLlFGjA0qdP-k6V4R9n93GqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">استوری های نوید و بامداد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81443" target="_blank">📅 22:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81442">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5beb4b7c70.mp4?token=tBhJDT_5z9KPbQHstqP-47T087AuSoNKrfizFc0_GpSMwz-UopLdHE3YzVvYr21fztG1hJpfnglr8zbwL8NzcMlCTfCrO3svg9YaHzjQyMGpxagoTgM6w8UyA56B1a35Im187II8rM73Yipb1KhfbtHU3MrR97XVxHTpkWdACDFxYI15FHGyNpnCGog33Kxj3QDZeK6ZoBprTMwEVRmyYhFk6y0qe49lrQKc0FodNlZTlnD4Guk2QbEFDRHFKOxJwQoyLM2tDUY61YydaOLRHatpWk5Xmx1Tgig7LdRZ0YLedURbHiOXr7Rh84PLs9--oTs1PNiPfdpambTjybIKhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5beb4b7c70.mp4?token=tBhJDT_5z9KPbQHstqP-47T087AuSoNKrfizFc0_GpSMwz-UopLdHE3YzVvYr21fztG1hJpfnglr8zbwL8NzcMlCTfCrO3svg9YaHzjQyMGpxagoTgM6w8UyA56B1a35Im187II8rM73Yipb1KhfbtHU3MrR97XVxHTpkWdACDFxYI15FHGyNpnCGog33Kxj3QDZeK6ZoBprTMwEVRmyYhFk6y0qe49lrQKc0FodNlZTlnD4Guk2QbEFDRHFKOxJwQoyLM2tDUY61YydaOLRHatpWk5Xmx1Tgig7LdRZ0YLedURbHiOXr7Rh84PLs9--oTs1PNiPfdpambTjybIKhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهوی جنایتکار کودک‌کش تروریست صهیون:
آقا جلسه‌ی خیلی خفنی با ترامپ داشتیم، وقتی می‌گم خیلی خفن یعنی خیلی خفن دیگه، ما تقریبا سر همه برنامه‌ها و اهدافمون به اشتراک رسیدیم، از جمله همینکه ترامپ مارو پاره کرده که ایران سلاح هسته‌ای نخواهد داشت و یه سری چیزای دیگه که من گفتم و جاش نیست اینجا بگم زشته جلو جمع.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81442" target="_blank">📅 21:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81440">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q6atF8VVnO7HmVW4yNZA2HlHfd2dbfSbuEHgbU3CTba4lu3_atvYE5VrNT-5ig2m60pLYQ7Fl7fPMZXCNwHA0JH9g6rZyEC8lpAu3nruOvXpghPtMeEjQ82B7UZyG9RgFBRziLJRXJG-9Gqwrfz3h31RgB9k28qkigOOa-Et1Tryl01E9LcVCeSGwZdCDcPZzVWPq-4wvLZq9GiObQE_T2FHyB3Ff2WfU8mk5c7s1Wm6KP1JtnZQb3jl-dlnpLekEP_1vrvQpwlAWvCXynaDnCw6Mts3zgXx8thXx61ofxDmVGn506izh_3B8qtK53VlxDjsEnFM2Woor-XwsAbn6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MqgVtazS_NBaGxgjUcNMeDRxbQZbwGf2S2DuzFK1gKyMozJLs5fLKELpUZUItaVRJ6mddJbu8wmY6UgM1EIgHI58WDa9yzNJF-GnfgBJYuLsBndnSUqLE1uQ9xeQ2zSlIvd4GStKPtoyeP26tqg35aY23NB6S1fGmGqUHMAiAJ_QbuRMBKpq6wDg_pKFwIDQm9nxy3Vditu6U2SG5ueeOnDvPL65Has-BhKYFg9SzR3itxXGToxEoC8l59OaBN6QT6w5TF3i1egmufiU_HUN1pA9X0oMbkYXCUi50NzZo-Un-tz4XGUNupsv-m_Q0tCYGNjxmROkgnsU9xG2VhkFFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کوکوریا قیافه دلافوئنته رو تتو کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81440" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81439">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_OmuoHMDt18G2Kgsmciou09hpbByQsF8d9CwfbgBpwGuOy03UPBy5RHrkxaL3HOVDPfr_IjhPSECwLw8tHiMmoctRxEgdRJYw5O8LrGjxKdEdbgthaaAKH5Y4WNo1WcemV8o7z84OqNK4-mqtrRwSh1kLdgbaETksfwJbLiIdxyb759ADeMK_i0q-YalGca-ii7xzIlN_8E60BtTYNm-0X3QuIFwnPsWHrhHo7uzzviGjE1gOPUXI6bBjc2gleIWpSrRWkipCYaiWCU3sRIKxrUw1ccpyrKId83fncaG4wWeQFXius8whUvbSZe6s6zuRLlVyhtdQawILzlnqwPvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشماممممممممم
😂
🤣
🤣
با هوش مصنوعی فیلم سوپر زن رونالدو رو  درست  کردن  اصلا ببینید پشماتون‌میریزه
🔞
یجوری داره میده انگار  ۲۰ ساله توی پورن هاب داره کار میکنه دهن سرویس
😂
😂
ویدئوش رو اپلود کردیم بات برید ببینید بدردتون میخوره اخر شبی
تماشای  ویدئو کامل
https://t.me/CONFINGMeliShkn_bot?start=3126b54d70f9</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81439" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81438">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بعد از اتفاقات دیشب شماره مادر سام صابری رو گیر اوردن براش فیلم سر بریدن فرستادن گفتن سر سام رو داریم میبریم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81438" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81437">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">شاهزاده قراره با بی‌بی نتانیاهو در مراسم ختم سناتور لیندسی گراهام دیدار داشته باشه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/81437" target="_blank">📅 20:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81436">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmziGjB_mesf9Zj0iffXBd7luGTDotMeVw9pcnk6i57DV4GNc3IdbECO3p5ZfOUA6ZirvkB0MCqjbmE14Y4lML0MYdrqt7lkiJzY8Gc22KTOmqYWSaY5QYFrW1wM48U_YU3IG8x6PVAcGsowkpTbUxSvwmVI5v4E4z1-qljxaIlgXumvuR-2IBLtxGE5zBePBH4UL1grNK7Ksn0tw9VKk_PicGvyk6CZnPcHKLio9O2AicqUYlUmfHVuqv7iFUHErq7CXEPL3FIXbsBpOxzAbd5wC6k06vZm0aZbA3d2VwhTU-wXlyHbsB4qFs9iqkGSQL3T1jQJbU8-c9isAwZA9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ماه گذشت
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81436" target="_blank">📅 20:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81435">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Numb 1 - Madoro</div>
  <div class="tg-doc-extra">numb</div>
</div>
<a href="https://t.me/funhiphop/81435" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81435" target="_blank">📅 20:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81434">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORySqhVoJwOpRXpreHfc-sBBu93YdaI3iYeOrK9ITEeknAtd84oimiXaWrTYIviVdQ8_TNZmjCqSb3MaczeyhbpwylJXF2F4CSoXT4xuSh85RWmQUYx8E2zHYQP5rx0q4soacS08BL0tn-o76D2yARCQRxui7EYZQlEq5s1jkrKdg_sz4ZKvhkvI31mj2100LKym6Wp8w2jASYXLCcVfKpQHwpsOFMYW2PkZnDVzsa3f9tP4dwKml08khk9r5Sk93agIstNWkpYYniF2YcN49THcW0aahtSo3K-kGkHi5qpvSD_wTdcP0SiqjdkosLennmS7l2TaFN5U4xvPrtlImA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آهنگ جدید numb به نام مادورو منتشر شد
📺
Telegram</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81434" target="_blank">📅 20:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81433">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">این که ترامپ دوساعت قبل جلسه با نتانیاهو میاد میرینه به نتانیاهو یعنی یه کاسه ای زیر نیم کاسس.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81433" target="_blank">📅 20:10 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

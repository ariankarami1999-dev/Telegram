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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 20:46:10</div>
<hr>

<div class="tg-post" id="msg-81548">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پیج اصلی سروش ولی زاده برگشت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/funhiphop/81548" target="_blank">📅 20:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81547">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNrecDBjt9hlR2Hwb8-3B-aeSGnmFESMKgJ-IFq9tF7MDTHN8b1LEw2_LAr7tF7yMULM2KOcTiw_95C-GRgncArIv-zqut_wl3R08Hr-2ZZZpNeAwverVAYAqUG45Cph9McV0nFJxPfG2MMEr0ilxk2f4I_Wk-cbvr7Kl_RCIBcAn8_JnR2t9mO8c_StdFknAaEHLodmyGwychJ7oFEF3pA_tOrDNccjfIvwelWaixv-8BX0Vew0ZinoDWbGl3qPSF5doyT6sRhmS3TMeF1R-7YaeTGZhq46ky007jeHaQIG7gMugYDBnCuZfsbmHUs2c04j0zWgD4ja2ZeyEk8TUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروفایل پاول تو تلگرام:  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/funhiphop/81547" target="_blank">📅 19:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81546">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-JjDpRMl3Ur8HlQxY85zQqmykni1qkjffldUd5qBDqdnHLwqwmkG6h5_7oxjBSMvUkt4e8DRsoaD4Q4EONm8sjragAUN4rqYC45RqG3-oCtBG11iF_NwfVNbGFdkhRGG5bWkU6Ds-GQsKK8QjcLro5bu0iFOYaX3km7oe5NxOr7ZjVx71S5FHp2WXzLbPs_h8WXhLj6Kh-FumEklnTnmQ3_lFdpxmcBzWXKukwJ5DHgj0FrH5RYzmeEGQv-YDBEpKC0oIwP41x5wKW4PyNPJtlbsUxgKdxRs7Er43F5KfFbOuz30nozOuhSoQT0mY8NE55qF2JxwmhGi3HXQ48dOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بازی شاهکار رو از دست ندید‌  @FunHipHop | Jenayi</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/funhiphop/81546" target="_blank">📅 19:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81545">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PA1KdzsiuB7jphOv-MF4GzR0ya3Dof2S9QYix_JHkQQTPtVKxwTQKSObsfC2sg-AXebnLkXFGrP-pkUJrUByl0nopFcJEud72ZNdGI4t1onB6g5Yw9JaE0pp5SfXG0Gfk5z_Z7-Bitwn1Mt4AcWC20y5vQKlKw8YRFlQ0C8JKnBW4m6RHhPhp1GDjMVr2qkOCc4_lGxoHa8UiSEMhw7LAoLwUG3L3GkylGBDpr4jnQx_8ngxmcYPiyhLzOMAwElrRWF6sD93WnCErCFhR1h65PNzM83oGwkBjWpK9UInz0MxIyTAlEkUVCSc1xWio9k2FfVy2thZF-WatnOe0m2hrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بازی شاهکار رو از دست ندید‌
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/funhiphop/81545" target="_blank">📅 19:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81544">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/funhiphop/81544" target="_blank">📅 19:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81543">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehoX6TkFOJj0kgPXVq5vGONfy4mPg7bD_FTxJfeY2cd-IeWJhDpmWyu7JH60lVxEZ8QLZ-yfPe-NHNxJWnJugjDEepwK51DOT2QStHk4v8nWh_IbKzbduN0Ko0CTVeqm_AbUWOm_nz3tHXXY8l_KLUnu3NK4yVs3B8aPmwH5ng1C8E_l5S5UsN7BOjF0ScSOxSudvYJFwoRiDjQZyUf_XiLrd_5iMAhNugte_jgijdwxK-QmAIRXDN_Kc8iQdkAn85DhDAV3hSnx9f-2xtomFf0gf2E_bU2JT-JsxGvfC1dSRUt7UiZk12O5kBOY8aSZtqzqt7M18kXNidxLeDS81A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران:
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/funhiphop/81543" target="_blank">📅 19:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81542">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxOykL7OLvvKfb1fzms3DnDCwKA3Az2yiMfANyv6mAeJi-OwcQUUNoIrIQHOUc-wMb-mpuH--BU7HrFwMObc7k3-639VwmZuVaxy1aJ_5e3VzLPpx7Oanh3FlERLz7dUBX022z0nDp5m1kRaIItfMo0cAKSz6_NYgPOGjbmaXZbEeFHI55FqUnR7xC2WkNSGYN7bT_Ct3KrSucoDJ6e_FoM3H6fXTXV33NDp5Eg09uFkZsRz0MUH22oH55tTDG3NXk3BMQqPqx3h0PfxpLP2aULzv_bQ1fskM8nV48uOpgKB6nPcckr13xeoVqD49ZdLUm8qqOxfOHpqdADpxQnC2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلشیفته چقد ترسناک شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/81542" target="_blank">📅 18:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81541">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFqv-2NJwU-MsfhWuq1wnbH3im9qq4mrv6JmlWSm_jKIB1OFaUdtKysCoLSUWdWurqO2GXFTnJxxYNaP5CMMZqzKNHh2OzOs6Mikt7tu2jdGAxqztjEicu5MAerqz2Lf08GTemXzg0v0mrGDrlbXm0TSrUW3IVKd368Er_OmVJOnU1WxmSmhTs2-teiOwtZlXO0w6tzPzk6i-DMux7w3Ehn4OTzpG_UljmbuXRkK6M2NO4o90c2sSn3JtrU3VaNVSbljottwufImorfTCyJk5gjKKIPuCM3bp0b1Jj4923NAARS08Q2crtvMnbE8UMcr-I6ZUPwML3AjTkVX2rYE9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام بنیامین نقدی، جوون 26 ساله و از معترضین دی ماه صادر شد.‌
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/81541" target="_blank">📅 16:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81540">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sykDJ4ItBp9wrUGLlocxt-fBq3oDvpeOAO2n6qHjtBEGi8EfeFnhIe1vMffpzHAJwIqEaDwCWqj00A07h9u8yqAp9nQkDc1M9RBrr5nU9Df5ExA7K3U4l8hNbLYHZl2Fu1WfSARWkQKyGfCWhUCqSFT47NJgHzL2_-4d_dEfOLp9vYRoysheKfZyYZUAMNDB5lO4dwJyU0Os82kUhBRmPaHWt2YHpLFazmkoPqUkppJpg1pekN2GO_x3jMajKuLQ1RUY5MBLtN8sXOMjfnjTHEbI1aGlmnmIAA1RlwSlFG5ci9No4ZHtExNVvZXhN6n20iZX1-x6lvnDhmGphRpIog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیج افشین فدا بلاگر مازنی بخاطر استوری که برای سه جاوید نام اعدام شده تو اصفهان گذاشته بود بسته شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/81540" target="_blank">📅 16:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81539">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">از نیرو های مسلح درخواست دارم کره‌ی زمین رو منهدم کنن دیگه زندگی کافیه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/81539" target="_blank">📅 16:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81537">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGuidskOVLpNpUWDu5JMxRfhjt9loDq22EC44GwUkBfPi3v5GMBRU9na38y_vGSVaj8t2eCcfPzQY1jeZDrscToKgcYNLwnNfAbYbyl4x86D4ILW4OsfF8DJVmaQ3a-c-92NvnNozqX8OeGd8XV37ee3P5xe_49_mZ6nNHmS7151a-pqFsYG3KjqqBE3qfzYjReVbz1aeeeXhWx630j9qd1_4EB3qj0XEoAy22bA8T-rfVAYngWlpigqb42yMuzwvoVmUpLRsk1QH_TvvmkdCRaPfHqxnC1fy-jKu_QmAUFBiH4C5coK96555WMN4VXCy3SR-LPe4uwnbnT6UCMSRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آفرود سواری در کشور ممنوع شد
تصویرم از وضعیت یه پیج آفرود که این تصمیم دولت رو به تمسخر گرفته بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81537" target="_blank">📅 16:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81536">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اشکال نداره چین میاد بهترشو میسازه
🔴
چین گزارش‌های منتشرشده درباره برنامه‌ پکن برای تجهیز ایران به سامانه‌های پدافند هوایی را رد کرد و نادرست دانست.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/81536" target="_blank">📅 15:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81535">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWpJlySxe-p6wUyzWkeqQt-H-qAZ-wfJlNaKBZrNxzELT5GXTC0htjUyMO6erjuOInRu9Hf5KMSpo-lEUItZA2a5JCWQX7QA3hs-MffOrEdPC362AyK4CEuemBDKAN7YY7pUdY8_la0ABEqPZ5rxSKj421lq9pHlMZ3to35CBnIqCtyezbqeZpvZhA2gpkQmPJD9rcFwnFxGSfrTsmLRicz4jIbFVjdx0jCYblRbDPMDHdj7QAStXAYXtofNPFqWtLvMpEgy7VQT0GLy1eLbMIwFJr--jrJjVbbz-hF8q-CJrWGvJrfLUzFukUG9EapNLf_JMOXdQjJGd2m_TuuB5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده اید؟
صداوسیما: امروز صبح در پاسخ به حملات آمریکا به ایران، 6 تا جنگنده F-35 رو زدیم 3 تاشون کامل منهدم شدن، 3 تاشون هم خسارت دیدن چند تا از خلبانان جنگنده هم کشته شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81535" target="_blank">📅 14:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81534">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qS1t23kUxwAsMK8wwApqJymzPYLmUKK_XCky0FJyr_6FWe2wdwCBsm8GKQnBdBatXYuH6OfkhcsEgionMa7aw0kIpSIPejZwhFuoeDNYfcSkLVWPVOpvXiedNpFC9Lrpl3LitlvBYD2EvaobpYcQH7dFUD-DPgzMpRHVqwg95A4ll54add8bNLn_OzcqqkmTo7NvObnJcLk1VEJyIb8srqCEdcTBKxA7WiMiHlogls-8akrC6FJjjBAsY5XhXwaERW9ZtjQbSaEEVjjs6vNhTgxYHYMulKuTiD1Cs6xb6pj0ny11lhPkymF5RQUwHj9-GaWEs1-7P6F6ePu3Bwffzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دایرکت یه وکیل دادگستری.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81534" target="_blank">📅 14:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81533">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/533f3ca2cf.mp4?token=iRn7TOYLpr2q7MDQG3FYEpVAZFPnP1oxfBoC8CEkGM2Ux_LEo1OSoHBP_d-F3mi6cckl3RktDhOWseJI1bpdvJsOH-_M5xh_PS_6336xTB1lrWtrnNByw2uJ40GnwG5m_e0yZfMKt_37kFiLWTDoJ7e05tbjaD9EfESzvIrK7V6pF6RRgcGSv2UPG4tL7nudMGcKI48AXX1LYedlPx46eGZyWZlpPDyt-R37GaEsJ2VMu_aX22eriw6eG5ZFbqBXMtQMOPNx6Pg4uQ-h8fhjRfh7PneIRe-3TfB7m_4EifrschvKbNPicFBtF4_ZZAKYEMxjqehFE1MVPrmA-mGpnBgYajAonkkN8mZRaTckxncTVbfA6z1H259RHoS-VnDidMA-ZbmTLFnjb0BHYuYoGShrjODF1renEfx7JZLEYgWW45ssOQzY_zccZCagCQB5jyNzRm0VNIABJMJn505B4Kdo-iXCKtFPWVGWuv53qeqtEFgwjBD2ZU6tqNcRXrEF6raBEIhltBDaItk9ajKDSaXQ6llXF3LDtc3WMHBmQH0MEHBofYxHB6Qr3w82xfk86dIrNUqBmdrJ70OJcFu-RrrvFsL_brsNqJy7QkHr4Cwm5P55W8sdQ5ezJpJGjN7wtow0g9BZ3ovZHcNyl6whx97nRRfUfoPw7cIO8Crk6Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/533f3ca2cf.mp4?token=iRn7TOYLpr2q7MDQG3FYEpVAZFPnP1oxfBoC8CEkGM2Ux_LEo1OSoHBP_d-F3mi6cckl3RktDhOWseJI1bpdvJsOH-_M5xh_PS_6336xTB1lrWtrnNByw2uJ40GnwG5m_e0yZfMKt_37kFiLWTDoJ7e05tbjaD9EfESzvIrK7V6pF6RRgcGSv2UPG4tL7nudMGcKI48AXX1LYedlPx46eGZyWZlpPDyt-R37GaEsJ2VMu_aX22eriw6eG5ZFbqBXMtQMOPNx6Pg4uQ-h8fhjRfh7PneIRe-3TfB7m_4EifrschvKbNPicFBtF4_ZZAKYEMxjqehFE1MVPrmA-mGpnBgYajAonkkN8mZRaTckxncTVbfA6z1H259RHoS-VnDidMA-ZbmTLFnjb0BHYuYoGShrjODF1renEfx7JZLEYgWW45ssOQzY_zccZCagCQB5jyNzRm0VNIABJMJn505B4Kdo-iXCKtFPWVGWuv53qeqtEFgwjBD2ZU6tqNcRXrEF6raBEIhltBDaItk9ajKDSaXQ6llXF3LDtc3WMHBmQH0MEHBofYxHB6Qr3w82xfk86dIrNUqBmdrJ70OJcFu-RrrvFsL_brsNqJy7QkHr4Cwm5P55W8sdQ5ezJpJGjN7wtow0g9BZ3ovZHcNyl6whx97nRRfUfoPw7cIO8Crk6Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
دیشب مامورها ردِ نوید زیادخان، همون فردی که خانم‌ها رو‌ تو لایو کتک میزد رو تو خیابون خرمشهرِ تهران زدن؛ بعد که رفتن دستگیرش کنن، این مادرقحبه با قمه به سمت پلیس‌ها هم حمله کرده! مامورها هم اول شلیک هوایی کردن ولی دیدن تاثیری نداره؛ به پای چپ ، پای راست و…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81533" target="_blank">📅 12:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81532">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7XthsLGAbueYTke__O6EqA1OfNJX7qRRxRkneRRLeQd_t-Hmg_-8Fbvq5VUU-2cOHTmdWd0weaAvTBhOGM-p56BL8po1f93TN1Z0NbSmAC2EYoAUB7eOrFfGYwTyZ_q9FzNJhLkH_zZxqnq6TstEvrohjg3V_WUqHJDApDjuAmTNKucJCykPIQzCbC35ukmowrgCXTIkVehNoOcnrVpBdRzRiyYyFwQhYq_8K7jNsOMeHtZECvJsfPc6AyiZ_nCPszZCpVyeXBCasmjEpT6wTSwTK8quH4zzeHo23n7Ish3D4zPoP0Spvw9or1j1rHCKjrYSHJNYB07sS_9QubGBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دیشب مامورها ردِ نوید زیادخان، همون فردی که خانم‌ها رو‌ تو لایو کتک میزد رو تو خیابون خرمشهرِ تهران زدن؛
بعد که رفتن دستگیرش کنن، این مادرقحبه با قمه به سمت پلیس‌ها هم حمله کرده!
مامورها هم اول شلیک هوایی کردن ولی دیدن تاثیری نداره؛ به پای چپ ، پای راست و دست چپ نوید زیادخان شلیک کردن و این گراز بالاخره زمین‌گیر شد.
این مادرقحبهِ 36 ساله، قبلا به اتهامِ "ایجاد مزاحمت، دعوا و درگیری، سرقت، ضرب و جرح، مزاحمت از طریق فضای مجازی و تهدید به قتل" زندانی شده بود.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81532" target="_blank">📅 12:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81531">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/81531" target="_blank">📅 12:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81529">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یک منبع آمریکایی به شبکه "i24NEWS" گفت:
حمله شب گذشته گسترده بود و تأثیر قابل توجهی داشت. این حمله تقریباً دو برابر قوی‌تر و گسترده‌تر از عملیات‌های قبلی بود.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81529" target="_blank">📅 10:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81528">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81528" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81527">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/81527" target="_blank">📅 10:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81526">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81526" target="_blank">📅 10:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81525">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kW0wuwx5wpxEj0qfFSrWPY--QIoL21plRkJs2TygsHFF2-btPN2dPlFPmIsbCO4QcdDhcOKqpcJGZcXhufTIrnF3VF9V75uNWeKQQKztADEPn5eaviv3anx86FIpzWmwcquvsQq4qJy1rI4YwUJA-1XU1n8-L2u8-TO208GFKs2k3GaT08sj1flILFN1kHDx_DSf-VObq5z8IeKasrvEtA7kzQrlALN3F-rjwH0WQy8hsbKu2xGl1nVBm_oAMLgUCiqxeC_DXafzYLFOSRaNCuRKZT0A-CuF0WIErBvkt9RixZ88I-ZGMT-RirIjDalpY1RqZ8wkTVvcssLdKglPAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای کیرم تو این اکسپلورم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81525" target="_blank">📅 08:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81524">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اینکه شب گذشته آمریکا مسکونی زده احتمال داره یه پیامی باشه برای ایران واسه جنگ های بعدی که احتمال داره رخ بده، که امیدوارم کصشر باشه و این برداشت صحت نداشته باشه. (اگرم انقدر اورانگوتانید که فکر میکنید آمریکا کصدسته و مختصات اشتباه به بمب و موشک داده و صرفا اسرائیل نقطه زنه نظر ندید کلا)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81524" target="_blank">📅 08:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81523">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81523" target="_blank">📅 06:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81522">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">نتانیاهو:
نمیدونم دیپلماسی چقدر ممکنه اتفاق بیفته، اما نسبت به شیوه رفتار ایران بدبین هستم.
اونا همیشه دروغ میگن، همیشه تقلب میکنن و همیشه برای خریدن زمان بازی میکنن.
آیا ممکنه این رفتار با اعمال فشار کافی، از جمله فشار دیپلماتیک و اقتصادی، تغییر کنه؟ باید این رو امتحان کرد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81522" target="_blank">📅 06:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81521">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">تسنیم:
برق برخی نقاط اهواز قطع شده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81521" target="_blank">📅 05:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81519">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">انفجار های پی در پی قشم و بوشهر و بندرعباس
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81519" target="_blank">📅 03:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81518">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">بوشهر آبادان کیش
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81518" target="_blank">📅 03:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81516">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a76739cd9.mp4?token=tSlHr2XqjNDSna37uezYrixZy9tXeodm9niFKVZkoQuF9FDfHFRNgttnvGwPsg2KckwWb1gE26zIQjdDiGtd_ibfsyChHW6FJQFf-p1_ik1g762lPM_sLDtSGhL6p5-yh_nmUe2O8rik0Hmzt58OgXwMrTXBu6EFwcCZZxTGFTdoJ0qTE-eF-aA6xes-EP2eoHGH5lVNsCUTqyc7E0z40wXT6lzUFi2DwxXYQuQzaPruxE_KcwxxUIfsOnSiB04HMr4KbkOjQ-dX0qJ9FuaFq_E9pev4bnF4xMXbZjOd5AocimSza2tr1fawTEEQqCPDhHSl1p9v3-0T6COu74k-zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a76739cd9.mp4?token=tSlHr2XqjNDSna37uezYrixZy9tXeodm9niFKVZkoQuF9FDfHFRNgttnvGwPsg2KckwWb1gE26zIQjdDiGtd_ibfsyChHW6FJQFf-p1_ik1g762lPM_sLDtSGhL6p5-yh_nmUe2O8rik0Hmzt58OgXwMrTXBu6EFwcCZZxTGFTdoJ0qTE-eF-aA6xes-EP2eoHGH5lVNsCUTqyc7E0z40wXT6lzUFi2DwxXYQuQzaPruxE_KcwxxUIfsOnSiB04HMr4KbkOjQ-dX0qJ9FuaFq_E9pev4bnF4xMXbZjOd5AocimSza2tr1fawTEEQqCPDhHSl1p9v3-0T6COu74k-zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان مراسم اکبر عبدی، عادل فردوسی‌پور در کنار عباس صالحی وزیر فرهنگ و ارشاد جمهوری اسلامی نشسته بود میخواست دستشو ببوسه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81516" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81515">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">Game started</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81515" target="_blank">📅 02:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81514">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">Game started</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81514" target="_blank">📅 02:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81513">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بابا کصخل بمب افکن نیست که رادار خاموش کنه، سوخت رسانه</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81513" target="_blank">📅 02:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81512">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بخواد بزنه ردیاب سوخت رسانا رو روشن میزاره که مهدی ادمین فان هیپ هاپ بفهمه؟</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81512" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81511">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">حاج زدن حاج
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81511" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81510">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">تلگرام کانال روابط عمومی سپاهو بست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81510" target="_blank">📅 02:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81509">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">کصخل سوخت رسانا بلند نشدن که باهم بندازن، بالاخره میزنه دیگه</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81509" target="_blank">📅 02:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81508">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامپ مادرجنده ساعت دو شد چیشد پس؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81508" target="_blank">📅 02:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81507">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ مادرجنده ساعت دو شد چیشد پس؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81507" target="_blank">📅 02:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81506">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">فعلا چیزی جز صدای پدافند شنیده نشده به فیک نیوزا توجه نکنید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81506" target="_blank">📅 01:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81505">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">پست آدرویت تو چنلش: این روزا انقدر اتفاقای بد و عجیب میوفته تو ایران آدم نمید‌ونه از کدوم ناراحت باشه
🤧
🤐
🫤
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81505" target="_blank">📅 01:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81504">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">تلگرام کانال روابط عمومی سپاهو بست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81504" target="_blank">📅 00:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81503">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">تنها اپی که سپاه و نیروهای نیابتیش میتونن آزادانه توش کار کنن تلگرامه</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/81503" target="_blank">📅 00:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81502">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ این جواب سخت ما چیشد خوابمون میاد</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/81502" target="_blank">📅 22:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81501">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3h3AOG_IjQXQ3ByYXWESdvzR6zIx-LaHWWXzsDnQuFbAlerJF7r4DIUSJRteryxjSRXszVdppCBQVWJiFwA_2Jpy-c5b1l33xS9XowFFixilGo18Qr9yj7eq1KPcxAXP0WDIi48Y9E7J36ZktGWLB0DDot32CoklguPQlwVQWjUkGZciM1FS7qDzQSXAOsi6aNnbGkdPoVJJX1hCxPOYwOKF0ybXfa_Nf4YNGzr1bflCKJ7fOAxI3QdMXPIL3NaZdapih80zwhZ_Nk5HS2e9_sw2GA7j2gCTIsgSEPD7JtsiimlawwTI3oqlF165z0EMyVnU9nHuFLr6Jt8-30c1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برا دزد شدنم ۲۵۰ میلیون سرمایه اولیه نیازه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/81501" target="_blank">📅 22:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81500">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJRNvuuLg_FcbaoE8F-WNYN9EdwEU_Os3lPiYGCP8iK3B_rXf6KQXEdBmN06iKAu6Eyn59XXQyoyk8OlaGslLYl2PT6Ni4wX85hggbxCPVbuTMD7bNl2RT1Wq-Q63E8K3Sp74hXZr_Xw-jaqlSiPEw8cK7gwUKNoFxVny92SKlONuLgZLhhRIr7cwz8N_g9jXXkCmuWaGZvG-6gPoNntJM8PcYzET0c-Gx9GnLTbot8-mrA6Uht3RWcETNQVSAPWoNa_T5LZbM_49jUGlPzbvgYSoa6V28dtzZMxAmGAn5-sMaxCKektHn8uLwwfaJK9EayjnjEWWHO-ietfgmzFeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81500" target="_blank">📅 22:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81499">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">نتانیاهو امروز با رضا پهلوی دیدار داشته
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81499" target="_blank">📅 21:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81497">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYNbHtJeFcfZ7wgSnavp2wqZ54lg94hsX4yYEzm_sIlaTrj6w-it0Ud4Tj4NVaYdaTdNrRP2Md9Io0ImkTav80RU_BdPurDJxdaZLxqIVhF5Fe1M-6Ky_uNBM4WGDrkk5_M9RL0DT17_oAq8sYVyLNNSEcIV92ktKnItvATJidTpjcdXUhaUnzPY5TlC6PzXHira2_8idOgcCOuVjO34-hklrUxQsvTTdYTr3VjbxMgpEnwQjSZFAN7PGL2uaC-LI0-pETVWokreXxK6Iuh2z-FnZriHR3FEQc5ONuAc7AL6oUuZZThG5-CB7aVFtxpPHM9UI2xpvmRawxIzy_Aneg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام چه بامزس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81497" target="_blank">📅 20:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81495">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDKtoPbZpVoiP_I2FBF4Ibhu54OlQgRu4HEqnv6IdZBcT9jEKRI0-KHWnIXcKew8ii32z9g1HbG0h1FEF9CaiLXt0jFoFrGUCJNNkR6iHmng1SZbjz4FrvqvD5XHhigYe4UNMQSLgROAiPwa4v9MO33X1QPGExPZqwQVwYMIHN7AzyR42tSo-XACGX0rxHrPF3MZiU2JjvwU3wYF4D3w5ygmoAvedmSanrjKAggeJS_j2-6DBN-SEZqVvFftBdM0tdggjhrdx67iiY3VbhY8M6xi06rOoW9PWagh5zFkhTFl5o7SjX6zWQipQwP1QwhLJSSpgNW9sFN0e1eMujK9xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی بچه اش رو دوماه زودتر بدنیا اورده با عمل که فقط تاریخ تولدش روز رند بخوره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81495" target="_blank">📅 20:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81494">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/neGe6dWmRGkYpzzDrhWe_bgrsAdXpntqhJqZA56aptV4NzV1mYPAmqu5u1dz-2BtFd7XyS2lvrp1Munybq5ItSVujJxLWVmLGi08m9E70t_khyEa9_FiGD0Gsk7k5z-1DLsxQONKiUVXOkrKhVBX4t7XmdN2VFgMgxXqyhQYGMmjxkFrbWh3hYJIRQZ7D2MlvKXWBzUhnneFW7ntL3_s_cMNhw-aJFUfFbUBvjc52mtJQQAB_GGPTOVTmA2rShKW8E-RKyIykeyK8yp8FK7p7v9qysaSyGeuQ_Jkc9weX12-b8X9cTbdvDQS06HsgBPBtBnhBFJ3Epk5uKpIzUOwVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوتیسم پسر کوکوریا عود کرده، بخاطر همین دیکه موی بلند جواب نیست و باید ببافه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81494" target="_blank">📅 20:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81493">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">پرایم هیچ بازیکنی اندازه رافینیا ۲۰۲۴ بهم نچسبید</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81493" target="_blank">📅 20:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81491">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">از وقتی تلاش نکردم برا باز کردن پیچ خوردگیا هندزفری سیمی کیر رفت تو زندگیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81491" target="_blank">📅 20:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81490">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">پول ایرپاد نداره؟</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81490" target="_blank">📅 20:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81488">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RgeTpc5JjVWQvFdvmkEfU4krUKVwzqpmVDyrdmp2APdM2_zOh2pDbASF9VJyRHvwu01a3SYZAk_uU9zCRVYti888lBl6BhJQ-Okk9BXNS7jTdEJVABDgqGNk7lUEfizb5tsuKUdr5Dt-0_Z-riCUZXKiI3Q2DeVFLcbtQxKqONOU9IIpfaUlyjMSTmWfiPwQ8jtlBhw5UNhQ4bbHbF459tTFUD36UFk5ajGHJ1MMZX8fL8_dKFlUogsBRa5M08NX8VLA1jVnZgiBBZcxx6vJBrepWHya80Est2RD1pbGA0uSrJWYnBQMzk2CDAMRi4JzUH9DJ15DGAeFMQU-lpQ1SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a4zuRfcIqJDAqQsxJIHIZaf-qJ2a0outVq6rVcklwDM98uXSNv8ix5f9PkJYP51szuZnIsqqseg7cty16LZw3XzbHh48O-LA2exM1oJ3xr43dNm25p9zytVc2g6A0d8vge0fIDsJIx95C4A3tK-_s-CcuffIR21m2P7rR2fQLSRnzX_d1PBmDWnldsg_tCuyE6PgDBjIfdQhpFuxuSgPxjuOlaA0vaRknZM21u8emTgubNmAaJc4OUV-YdDAllonrhll5f3w3we969WOTMK2qNxd5F9EzJnlbFqRtHU-GWCoYLRGdu71T8AeXKHI3JdJGQ0yPjaaubbMKVmwVnzHxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رافینیا شبیه زن جنده ها شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81488" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81486">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ln4xcyc4nqVxpmP1lpi-6GoHoMY7Bwv8fS1kOqkeKrcMnUUGcf5Hi96VrYu0NPAQQ6emlzLLOpK55FX7-18ylo-gdeyY7vKjYp2eYag02_yo6ZQf44Wv_qljgH9n8VtIsC7jsSelnvRSp06l7Bu4KBkoMkccot1L0DY_rF2lBEazs3U9avoDzakDSwg5w2HN-bIx1KR2d1I2l9r6vwC1i0U4p-Bm4UFwhJ6OKXRs1_uyMYIahydo1KFd8jsCOvSdiz3vgElQmsoIk7TmVLv1JJdGdITaNVyGj5G491LqYl-EYQQk6hxr1sUbaHIZSHWrmg_cgA6DIuoZxe30DAoV0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dj0NkY10PqsaqyGvpoWYiRXgcNiFUMfsPBvTV_Wdfd32uCEV3sDILtSJtZhRsDOBtL1utwFlHwTwN3NK81_YWaM0ash4th-B90QFwZ4JNHqWtiZR1CWyzlXiDr6Qk0icj1dNw6kCDAOZpspHx402pRTDGbKXU3rgNlFw-iN7Gw9WzlOnQkQod0osgWnRhT9QV2w3a_-q-gpHHA99H88EocgowYblLg2psqAZExDSAdmq_rKfZoLdLwCzeOypJK7CvXDhUeUrbzaC3VrcqFDSYugu4QKSvpj6DfsFNnhGTNgpWN6ZO2I29vHGnE2WI3jTM6KVcw253IkihRYmRwKgaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هرکاری میکنم نمیتونم با قیافه جدید وینیسیوس کنار بیام.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81486" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81485">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKarIW3N2Ohr4I6lF7o4AsagBbNXM_e-ehubk08X43CvIK6PwCwOw0LNbmyA_B7nN8AqCRToinF7q-63329jYHa3Am2OjcJGg_cXVO1K_a13Vhn4l6jGsla-kZk7fCokpf02veb1L6sWdrDAn-_Zn4oq76fpDo-qNypawGioIeldjMELp0VfQUW4SUjekEViJ_S0oYqipiqQt48rK-ivMbDdWoUQWUYfbMH0AmQZO-TvEIAHk7yTLKuvxED30b0mPOAgYfQSEM41HFMwOX0iGwXTD0RgpfrFx9bS-fqZZj6Rv8BuOsVrqypzuTgrpL9hfDS9DwKd0dtjyXlyL9TCYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چی بگم والا.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81485" target="_blank">📅 19:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81484">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAO5f_C71dmyghQ28ciQy5J00hWvZHL6Rgu9Ofp6gObypSnl6YqMs_wrSEy-4tFXMTqeUQ4gOQbdEIIv1lIspojaiMG89tWs_axt_zogUY4yxHwtfnSJf8FGpITtgujLxUP2GpJwGwRQ-e4AfGMB-MQ9wna4O6DBwZdBxViqleqmXGKofJ_PinULkKKBw1s339kQJVxs4z5lK0RAwdsrwF9gDLtYKpSuHnJ1L7G485iDsGjGXBssCysUFob_AuZUumTBGvOiAHRNBrEdGd2wujQGbR4H7hf_F3BOff1o8ItAzF9_o5YNDpu8syFBuI0etIfmGhFASt7V402KOUpx7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81484" target="_blank">📅 19:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81483">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rU9jYYPmR1yskr9KyafU58QFNUFk-FEp7lV6H6oHGwbRnVrID_9pTUydoG-D_rrjpIn31UhSdlV8Sxhmv2mmE5kZ8XSSetZDL3EgFH36BFPI_VabW7RIDpFVcuB3FYr7clqVo0IcKJh5i_6WDOWdNe5lB-ZtZZ_tNw6Z_ma3wA55xJQF7fdlYU_JdajWJ3iu44We3HcE-Zhvy6m3PFGRP59_C-qQ6zJqRuyEbuCJZ7a3sv35Fr6fuo-JiXuuCaH9aMBM_k20WEsZhRlmOowmOxaejqZqtIcqai1zYrxwUXOzkICVrwx1XUGfsOVSR6eZMaA0_IAsU9RsmnDuZCUpcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس جدید صابر‌ ابر و دوست پسرش.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81483" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81482">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_m1aYKVemXVCfJIBmcFBsV4B_OASkipmOImM63mH1eWv7UtfvqsKenMZXgNUQYmJXDV1yg6ZVnsRIbeQZ_0a8202f6PifSDhK_ZOHba1FuotNZweITbqWyhnzW5ZP8-4j45W8X6ocH_-Hqve1cIHLyf9VEzQxCLBjQizEoLs94gS-nybd_GdBCv2Jz_tiDoB3WKNnVV0kJFNLw0Atnyh1gb-OVOjM6H18BZ7DoQh3mpeykNgQHX7Uz-bSn4RxGzzZZjFhl4sIFbwcKT_mSGb14Ol_44AXBs0MB-u2HYWVOaIhPE2YWbOVHeLypXcyHSqahtC0DgbPUYTgG62CktKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروفایل پاول تو تلگرام:  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81482" target="_blank">📅 18:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81481">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2Q8RtB1tOE8QakL7ClgRfwfvoxZMptgV56CvMLWNo2ys-1iSvrrRpKrB_gKmGwPp6QKSQZpK2iNXKIqccbpvXRp8X-65479FFAejpP6t1CV-qllzHY8ihV8q19misg13J86TGg6nmxHZRHUqZbNXCqVJGQK35cD1kGBF_AT0Ec3pdJOw2wRmhOZXdXou-oIDASqcqyoy0FD9xUNHuGvSsiEkQz7byBXDA_VBTQDzmAGQurNi4OFv3ZUOWWaDH2Bl74GLnqE59Ix6e10wcfb9cE_Nb6vObssDRhg5j1xM1g3XVN-5qHene14FXJFJ-BP6RW5RmkEZHC2dRyCJuWL5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش دورف:  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81481" target="_blank">📅 17:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81480">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">عاشقانه‌ی جدید عرفان پایدار و شاهین نجفی به نام "داشی" ریلیز شد.
🎵
Spatifay  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81480" target="_blank">📅 17:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81479">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNvSJ7s6g_WAFIlQ8Xnq52w9cHF616xXAePCzhyPX0GfTu6StdaQjcLu01oCt-O-nXKuePoWdoFLPC20EvFLUSM6oGHl9vl2B53RmAvFYXNkWX4oxaKDF26ExhYv6zuYOpO40WELYaH1B03nmGQ2EsfBiYy7hgI4O60XQ8z9STeFH-EF75ZhYif8dGQtCW_Jh2e5U_KNY3uqOB6bfWJ0peCxt_jeZHAon_dyIQ_NU6RpBrPIpuDpkIMIXtk0AfF5R8Ay6gUE2mBgtMqQoy8Nq8vA_wu8oZepv4EgpybIZGPz0T6VV8rknYNY9QDvaMdamsTv8L2Ea3TjUHrNjx5yaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاشقانه‌ی جدید عرفان پایدار و شاهین نجفی به نام "داشی" ریلیز شد.
🎵
Spatifay
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81479" target="_blank">📅 17:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81478">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCTS5xjyN9_EpmKe8ysVKDPMkFsQrz8kmj-A8SReu0nV3tUOXNmu-Kd8bYQsyxyAHe-U8bv8ZaTJfqUtFXGm-fVv7-R5B2FDgciyK6QwqTuTQdCp5GYQ0ZOmJhku4Udz_MVHMmNA4k4UeENqlfcK3YHDmHA2Qi14iiXH3tbcE-SrDWmvBTf5rIb3OfTAPhe3rQGbYlhFtQJ8_KT7y2KtpZNqYTH3ZSfxfoR4i-_1hc3eFADOnudqbEiLro9tsKzH4qM62iDOpFbWx9gRbQ-HL8W8uxhitcg3U7RTy0fKQjV-Y_TX5oALfrDEc_Ad4eYl_SaOo-FB2HWyfzMsM24c5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاول دورف داداشم، به اتهام تسهیل فعالیت‌های تروریستی، از طرف سرویس امنیت روسیه تحت تعقیب بین المللی قرار گرفته.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81478" target="_blank">📅 16:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81477">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ: ضربه سختی به ایران خواهیم زد‌‌.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81477" target="_blank">📅 16:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81476">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">منابع نزدیک به سپاه میگن در نتیجه حملات دیشب عربستان و آمریکا در عراق، تا این لحظه دست کم ۵نیروی ارشد حفاظت اطلاعات سپاه کشته شدند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81476" target="_blank">📅 15:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81475">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اسپانیا با پخش اذان از مساجد تو بخش هایی از کشورش موافقت کرده.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81475" target="_blank">📅 15:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81474">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اسپانیا با پخش اذان از مساجد تو بخش هایی از کشورش موافقت کرده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81474" target="_blank">📅 15:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81472">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifZgs8mZ0AdkU7V-EsIkgXIdbltG1-SNAgXRUIodO-SjkEBXaPtNa22a3gud1sE-JrzOe8NhryP1wvZPjGEAFrMeym8eFpvi8Hh7i-3dUvj2v3sZ1jXtfMCjdPruF8yyHQSWHJ2NP_HonG_vh26Bp15xE65sfgDx0EHwD3LhYuNgLHi5jMPX1lUm8iqDgPxGabDOZ-2lahZzY8HpWuVAcgxaiXhAVih9gSSu84M_YI30Xbe-qt2BugOgFJEHyCxMolBJw301mC4D-qWyfNgL6x-oBORjOarx63xssWAOG1OFhDNd9lTBOpAKGvsWGwxs0sgIMbaD2vPlxIrdTWQvhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچکس نمیدونه چرا این پست انقدر ری اکشن "
🤣
" میگیره.  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81472" target="_blank">📅 14:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81470">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lG0sV0sIaq5V6CZYtnaNJeB3HVcA4ZGXv3H5VpLu2nmIWoqZbPnpQ36Rgg4QGr6l0Ry4IFR1rDoZ_TckvQDEMt__Ex8_ITotdgBf7lyOEGXy-pQ7ikj2eoZDn7ZeGlyJPjlYEK1FMunRg-kN2wrlr_aYldsXPxX5xREYnO08mEGXR0yY3kugOKJrDFq16NWdVtenRpQDye1IOMe4W6txZABnlPMpkST8p420Ix7b2M2yQTQVBjEoVTCLVEfAl-5Lwef0V95dHW-_3MYF8Jol90Jt1sjiCtbiLOrypElFxFN_qKWYrHMX6AKk7CbXyP3qVS8-jm_qA4MP-bPMy1xEMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ChpXqb5OC-mp5GmIBJHKv0UXB30XdbhOtCOxLBMr9EuEv70gtx_4Vi80wL13zhfp0bIcjigkOVPYfheHYpNMsKBpoKxYKIRw01UdSUf6_Ljb-79J6bzBMAynylHR_XiWNAtrpMSnrxlahuxGIm4PhvvspC041jwgiEK4BYoBrq7Sb77DET6VRBOMZMQDxeMTAnYqAIwOqMVstcVxShaJF_8OSPUOm6A6iKLFcHxzVKOHQpma1r5zZHFvjlguFExCQ2Xp_2pKkuO1nHOqKqiCJWZgpo8a8t6BAZGqmLdNOVTSoBW8Jq7OnIjWAmanP0Ry0BkXTZefW9U_bVuvzJ7xfw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پینترست چرا تبدیل به کرج شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/81470" target="_blank">📅 14:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81465">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اگه این با سپاه همکاری میکرد که الان همه تو صف اعدام بودیم</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/81465" target="_blank">📅 13:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81464">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">پاول دورف داداشم، به اتهام تسهیل فعالیت‌های تروریستی، از طرف سرویس امنیت روسیه تحت تعقیب بین المللی قرار گرفته.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/81464" target="_blank">📅 13:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81463">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دلار 193
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/81463" target="_blank">📅 13:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81462">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmiRBJ0o9g4GbGg5lyuxcidJMDIv1soFVQ8PQdTaD2mEOIN476wcTmeN27qg5I-YfUx7bvsSILFd57_20YJfEpMmFGVjdLrLIkGaFs5JbHdG7JD89QN_hN7n6bTA6tw4UmVh1fwG-Dd1BDwPcdpSzlw-5Tq2UB1uPXJiP1zeSdSMuPaIY7ECnETp_ah06Cq2KKB7j2sp6Z4Twq3dDSYSkKeEBM4pM5AceFhlzn_2YrRlHQUxXQg8PGqAfcREN5aJ4tZbPQbmu24SZWXpNaLK9k9vUl4thb-NaRo5NOGhcdpWkpOyAz2hrZDtxVczw88yAPVWfx-_JIKWnJtmti1n7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری پیشرو
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/81462" target="_blank">📅 12:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81461">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgaBo8dO5JscyGJhMIZOKldI9k1VtXLCbY_-P7QR13M_YlBAIkol8vAJIkhnQvOQ6_JnnwjlsEFHdU8K7NPPbXL4pvz3YYg-B5mNd2u1TtVQgrw-u-MtSB67nEZbClEC2NpI8Z9qYc2uQ3zs2EkjQvAkILyptxmnDZCGZUQuBq3WJ7JDYxhMcHFhQSTGqFMstWDPOqFqVblEwe9YIrgXJRgtgIwZADdDPCW1UO5mvzDq00g5WfnHUCRi_J89mmbJdRqWpf2NxIXYicJfSb855DvRCqlhhf_WUBmhEj8xxqRpXxzq_BSMM3MHPMcXHfzI_piuOTlvR763HoYn_fbz8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">از الان تا ۶ سال آینده هر اتفاقی بیوفته ربطش میدیم به جلد مجله اکونومیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81460" target="_blank">📅 12:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81458">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">هدف یدونه پایگاه آمریکا تو اردن بود فقط
💔
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/funhiphop/81458" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81457">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">تروخدا اسرائیل باشه تروخدا این یهودا خیلی راحت نابود می‌‌شن بوم بوم تلاویو اسرائیلی‌ها مجبور می‌شن از دریا فرار کنن تروخدا پدافنداشون ته کشیده ۸۵۸۷۴۳۹۹۴۴ نفر ازشون مفقود می‌شه کلا اندازه یه استان ایرانن ۹ میلیون جمعیت دارن کلا تروخدا تروخدا اسرائیلو بزن سردار
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/funhiphop/81457" target="_blank">📅 01:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81456">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ببینیم از لپ لپ اسم کدوم کشور درمیاد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/funhiphop/81456" target="_blank">📅 01:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81454">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyjUxr5vr_PhovkOKA2OCWxO4lrdTxh30fgUGe0MEurW72g2aiJ-ttbnjXpJPBKGz78L0b95zgf1nvIE-oPjPuK0CPaSBtCHhUvn1k2X-kka7S6VTmRt58bRKxCms9Ww-uRJ0nfzcDu23hTmvGV2OrL2GcuBneSolduRLiDIsIEZ6gqIh3PBzOp5W8RKia8VFCZDkG3uBM_jveryYjUAUGnVg-fqdbEIbZksD8IROvHy5qvCLNmtO-dOUlaXYGo5B5-K45Pam4S1LU6eRV3x-XxsgZVYjM2rw3CBnNRKRjhvzcg83ChZ7tkFNidOL2DX1ho1PncwYRDReSLUfcbDlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/funhiphop/81454" target="_blank">📅 00:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81453">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4kO4hXC8ERaqF4fls1M3qtHYhKFS_KJTZPSGTyHrAdLxqq44anmqGukbxC0_ICHjCzPBiWo5E9iACZe3PfcH_XJasImCEZupDJWK-kMCHKZsPhuCTZwVFKJx_JE_IYkarKutAHS9YeQI2HIOY96412GJsUvkIDWDyrEClga_Sz_TWelk_VIs0ctvdpk1D2q4Kv4-cZfb4uZ0I4KQ8zJpT9ioeqxczVsWilKujaklkjpV0ycp2yxWJMSlLXgQRRXkfOncjecz7y_DBU5-i62NpSikJY4Z0nsNc93DG2MVOkVIxcSPYLLuLIn6GQnePxunfHEnqOLtr4i-tgE8-zztA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچیزی برای تعریف ساده کلمه نیاز به یک توصیف ساده و فراگیرتر داره، مثلا خارجیا وقتی میخوان بگن بی طرفن میگن "من سوئیسم" تو ایرانم هرکی میخواد به یکی بگه "جنده" دیگه این کلمه زشتو استفاده نمیکنه، میگه "شیما کاتوزیان"  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/funhiphop/81453" target="_blank">📅 00:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81452">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vE14A3bB0K6NE4F-Au_FmoMrSnrSI5oUE4ylOMZgPw1R4Dwk8Jt8sWkVIhCrbKpn8-4cmUz87OOXonzXrt47GXHPkEKuubdDjfli0uOdK0UAxcM2YjUnXesiTTQ7OVQcpI6LydxKDvUCKs6yVGXfg1wBLt4Qq6GnlFd3cGlR82Y0PHvZLdTNy_up1Tq-vA5iJdC2VcciUfSPRL9rp60SyOy9Kf1W6PwfpALbsOdLWKVxzGi1ySPddBU1ZCcayjl1dvikvVA8zOcrMnyhEnk5IiCOjXXhhF06vdgyhzKRSw7L7Mmvod3EhNhJc0ZI0ZQ7QYc8nR0IuQIWa7UxkSYX_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچیزی برای تعریف ساده کلمه نیاز به یک توصیف ساده و فراگیرتر داره، مثلا خارجیا وقتی میخوان بگن بی طرفن میگن "من سوئیسم"
تو ایرانم هرکی میخواد به یکی بگه "جنده" دیگه این کلمه زشتو استفاده نمیکنه، میگه "شیما کاتوزیان"
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/funhiphop/81452" target="_blank">📅 00:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81451">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">#رسمی
داریوش ترک کردهههه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/81451" target="_blank">📅 00:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81450">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGDR6qvjD8-MahPjPnHD4tKrYMWZmyOZvnTzT7mfT_FfbUD8jpnCOY3XsdvztfmpCI5n_Np3a_sGDvb64ALhRCOOyv8IYBinGe_aYeR3Q0qyJzsLOl-UZ5GftVbfPpA7P3ghkydXF8Fk7eFbz_JZ0tMxi5Jr_vfA4csuJ8rLmwSzmBVVL0yI3BrjXuc0e1NlnoVSDY61OMlfARkB4c16n3t0yz89LyScVHaojYWtcHPhB8_kNhA_DPuz6jWTR9m4XcB37wDMXN4zWaSsBpXH0leUtSaO-2Bjby1YFQzuzPIGENvR8PmO1dRq0emFbvvgeyDXSs3qSLAdPYCCshAzzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور شاهزاده رضا پهلوی در مراسم یادبود لیندزی گراهام
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/81450" target="_blank">📅 00:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81449">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یعنی جدی عملکرد ترامپ رو تو اوردن نفت از ۱۲۰ دلار به ۷۵ دلار تو دوماه ببینی و باز از گرونی نفت بعنوان یه موفقیت حرف بزنی نیازمند خیلی کصخل بودنه  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/81449" target="_blank">📅 23:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81448">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHKI0fgSxQR5Ml817mwJTW54bPt-bxZOJVOTMad5q1vt8clCiXCQuSmaetR8mVUk6SBg8jT3z2-PaFAOfWCXj0pPQ2hjkdsXdYqen5xFLg_vY0vI8iuPwAa4UoEkfVEUpi2G8HBB98as2xAjA1sSTGxcLBcDvOlMY7MX6RCT923hANan6BJiMtHoQnzXaslXfaKz_6V-8K7TJx7gm35iTXNE7XFnOTCWAFWi4f4oDDZEysSoGs0yyEd51RWWVHOJNiVDtL1MJ8IkPg3BBH6Vxi6H7MJhicY1_PK6CbwGFUmObg8cIuinkbckowUD8lGy4f3Mt1G33GtspRJF31OjXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاپورتا سکته کرده، اما اعلام کرده که حالش خوبه.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/81448" target="_blank">📅 23:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81447">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">قالیباف: دنبال بهتر کردن
زندگی
مردم هستیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81447" target="_blank">📅 22:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81446">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJQCb-JQUSJextmwewwflV1-thPNF9TE0zayfdlddIlZy3semN8tsXqMeA-DcAro-fu_-BS2cKDKBOnzmcg8YWlLeq7Jrk-PxGKdGc9Y7S5Nba4TMnQ3AUibIuceL9OlviUWeJWcpDyBPXQHXXlqNVlm5FNVcHkgItltfbaj1y9BREQSBNAq-ZbwxPc6pTDu5KkwkJee4dAW_60-PCTo96D-VC3LvYv4pIbX4ZD4qr6BktJlMojWGb98cGmmX_ZhiWgZupqZzbi1YPWGr5zNGNoZgpgBJwJhHINx2yqWS3Ij9cpkmUv9pcsAFWXT_3E7kzJ94NXfvuLZJG48OjtIAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جعفری دوباره منیجر حصین شده، هم پرایم حصین هم شایع با جعفری بود، با هر کدوم قطع همکاری کرد بگا رفتن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/81446" target="_blank">📅 22:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81445">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AzQo5YpkHmnQ_2JzCtCsetSRLABjevVr4hN3ejNHTB3XORTFa3rEP_WFwrW-u0P-qr6MA4Ar9dH81sKWMd5rPDOj3cJ_y6-UVlvgl18f0_j83k6ySt3vlvdqwrQ6-hPhC8UMUDBUP9tzl4asGJGtkMGkUEtrVSikc0ZG8Mak_yvvwtyAXL4McqhUNGh4FlkSthSZjT5RNwBxAQRd0CCus_8eKdmQXRXVJtrdYoeVl8Hb5hFDBNJkJLbrAzDEGFHVFJsXIi3RYvJGoQ-zQj0pljYKh6Os6ruC7kHU5XPofVCVwGTlxvSfP2jLiYnnmPXnQbVRx_wc2VdZkgwOHWmU_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jeGTu7nGTR29A9bXbvLJ--AwZmA9ytRjczFCHfZ0qYai-LG_QOAkulsxrW3sCCZZ74onKAISdP8QRFNBY11QzGxub8dVOlnfOsYYnEZHuipX5Cgs4-76ODtFxsHw4Z4hRMnbfa-RUdj73MJuocEGQI4NW4rFoji9zXz5PVmqGk-f9obXu4bZcj9_vmBUQ6LxgrrtmNpvIOcwopdE5hzQ_TrlS_jAAqDVtI8q8MUXAzm8m1Zz_N5pbmUYyPj8moNG0iaaHIRjI50dHa_zu5aPfFxT4bKWSG4TdIWqerjOnv_TVlX-EXjWZTzjB7rjSm5Oz8qSH_noeViLJ1228FD0gg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">استوری های نوید و بامداد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81443" target="_blank">📅 22:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81442">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5beb4b7c70.mp4?token=nq8m15xPcpL5dY4_EKvD_nJTvxlzGjWdIWGMMAqL4w9yP9O6W2ReGQz-UqxbidHfl-tLFydk2iJinAx1RWxlJb5A79AF9jg8CrEB0-x0rvhS0mLzCGBGDrEM3lVn6aqZSYV1Qoq4gWDIdyj8bU4HKF6YrxtKsJLvtkaDwkrfLT6f5ACnw5cVMXWsORI3HaCoGnufiRa-eshn-JNEj_s09hWRfr_6yO9MSzuKpYbL5BdwCGR1VeTwpV35djkwhxM21Woxj88TK8dAvC5Os83qcyKiu5iWNPq5NDErBNMPQ6u2l5Qy5KfVUa_5DQgJewhpOGSATQFMnh0UjOm37y9-qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5beb4b7c70.mp4?token=nq8m15xPcpL5dY4_EKvD_nJTvxlzGjWdIWGMMAqL4w9yP9O6W2ReGQz-UqxbidHfl-tLFydk2iJinAx1RWxlJb5A79AF9jg8CrEB0-x0rvhS0mLzCGBGDrEM3lVn6aqZSYV1Qoq4gWDIdyj8bU4HKF6YrxtKsJLvtkaDwkrfLT6f5ACnw5cVMXWsORI3HaCoGnufiRa-eshn-JNEj_s09hWRfr_6yO9MSzuKpYbL5BdwCGR1VeTwpV35djkwhxM21Woxj88TK8dAvC5Os83qcyKiu5iWNPq5NDErBNMPQ6u2l5Qy5KfVUa_5DQgJewhpOGSATQFMnh0UjOm37y9-qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهوی جنایتکار کودک‌کش تروریست صهیون:
آقا جلسه‌ی خیلی خفنی با ترامپ داشتیم، وقتی می‌گم خیلی خفن یعنی خیلی خفن دیگه، ما تقریبا سر همه برنامه‌ها و اهدافمون به اشتراک رسیدیم، از جمله همینکه ترامپ مارو پاره کرده که ایران سلاح هسته‌ای نخواهد داشت و یه سری چیزای دیگه که من گفتم و جاش نیست اینجا بگم زشته جلو جمع.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81442" target="_blank">📅 21:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81440">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EMWNfdZIN7xvn8GOw4lzkbqPidiw2zgC8s85tWCHnwv2SUu1iv7RpbKYbuBzS6LZX1L8mCXRn1Op-bwuWw6c9WgFCZJN0nkXzTm7qgnfTn3VE2h1EKftXmLmUqD40aSjf6AQv-KRTv2bulFmyAEo53pfevtEcrY4-bTbtBbWd9JEUKTDEex6tS2P7BC_IXLZiwHN6OV-tGDld6D7wKEoct9khzJIqfmessyC0kGFtU3Nhg-rGnDBg7msLDKTQSzap0lk6hYRQL-d4NZvb3302uaYZoEyIGmWcXfpciiFNeyj0vcr6h7xmnaSAtz1hKHKAH1AnWz3kaxHGs9RaS3H4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jbbXme5i4EE48BsAlawxyuVS_DwpgjIlqtmyuq2nWi3JTww393h2amH04kkxLpYIw3LxM-7FpHu1TfOdzCJO2XNnkY8HsFf392plCv7NN0KgyWWB7y4ska4QUOmBpEnsFw8Q49UlSuf5opRYaLLn-QawWALBRLts2Yth1sdYrsqy9d8bm1iQYihAsR8LwMKwW0wTuhq0JnAwqNCTnHJJdRjWthlrd5DuM3XgezBE16xkk9S8XAS5fZa-rwFJ1aZ2gStOh5XflzNUYbUKA_2xyJ_0J23bp1pFEsR9WSeKzKoiGWCGV9A2mVrmWe4-8j2njhrpdgUBcm901A1kwr5Rxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کوکوریا قیافه دلافوئنته رو تتو کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81440" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81439">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eu-nvszR_uXRhVDEtOo-hEvi_CbpzO8rF7SMmyssXeKjBAqqhP10k1bOUdda_3wZOMVez8XbvfKCmnTHjE66YPVrooY3xGdCS0S_aq3gvDgis7--pVX69yL56PELhMzIyDQAT6WDI5iiQOmsU-5T-Se9wrFSdaBxJvU1LOY40XhoriWrPnvKoMd-EsO9IiDbNW7GKXVkVSj8J1MboSNNDO-OQhXQbdWdni2HqzvYjVU9gfPodjOd4qsEfM6TkoFMubFw5eVASwhrYst7Nacb-C0IobRKB273mzX6UQ0HxY0Livflafzd2zWjvVZW0El1xsNQsI-NphJl7NftJMA63A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81439" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81438">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">بعد از اتفاقات دیشب شماره مادر سام صابری رو گیر اوردن براش فیلم سر بریدن فرستادن گفتن سر سام رو داریم میبریم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81438" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81437">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">شاهزاده قراره با بی‌بی نتانیاهو در مراسم ختم سناتور لیندسی گراهام دیدار داشته باشه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/81437" target="_blank">📅 20:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81436">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BI9u92e1uX65AH7v_o8QRjLpvX4X7GOs2j0ghlyWqjxZ6EFg5AShs_RGK8mMfB4dBSbjMUJDr-av5Gw6LVVtR5hXOwDU_ukC0IaVnZ_shqWkpXewAPBrULr8AYOUrrHzP569P-p10_d1fwn1DDkYilb5TaLWYynV6JnTH4_ZM81ILB3nszHyvAtliVEKBuUNwr0nHoY0h1RIBjxYlJIM_q2XOxNQRVv55ShYCBEw3y6ZFcPw7ActfGI8BAdByBef5NFKVN8B82j3_CkjmhgHPIP4Myvzc4rlm6ZmyL2JdQPGpKWNgtHdgvRE6INzId1Fa1RqwdF8J00_NK7zHt-avA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ماه گذشت
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81436" target="_blank">📅 20:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81435">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ua_AbdtEbTuP15wCPRiGgljP8BY-ePFkaP5relTtrF-d6kTi6uraHtskl1jDvk1C5i_IEZOGNJW7BmnRObRwQ3SU7-mrEevRbaeN3fLeVmfYu9haaf-DKMzZHco4stOH22CKgw8r222m_JhcdTLRG1jdm4MHsyl1uWCJpRK0SGGneqKQDOvqtSKBpmWcyyuO3Yk6w6F5lFXHqDsfj2SNxuoFx3Y6q6OeafddyXaujygKrLs_9yuv5gRYLlkSRs9fKq_JDIMs6f3kuTizF5WkUq0kmmfKUZ652Er5zm4lifvFt9HxoK4F1fWiejELjTRFCppRAtj_8p55jPpry7HZCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آهنگ جدید numb به نام مادورو منتشر شد
📺
Telegram</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81434" target="_blank">📅 20:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81433">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">این که ترامپ دوساعت قبل جلسه با نتانیاهو میاد میرینه به نتانیاهو یعنی یه کاسه ای زیر نیم کاسس.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81433" target="_blank">📅 20:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81432">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNfOXxfpKf1MUOvjJczbLe55TZX69u7WK2VAHnhZHGhm6SxQiIvkf6_JsVaT6pPV5Q7vye_Mr4Mzn8D16OXRbqRGPNQUgkOjskLh7HoZNfj5j5vuvNAvJKROjuYg30rSu89NY8jUvht6WdqBWIoFaalATEOA_hWXGn_ys8B-Ajq3-JuAHEyYPgw9_IuOD2bh-mAKNGyNOryp8Ah9hMlXUD_AUCi9WhQ-Yj0sKnTmV1UnVfY3TwShbKyML-mMw55Za0Ha5NNZ5Ah1rwqNsl8mCObx5VYtigPCY_ej-zffXFUwFfX6A5GHYMHlMXQ_tt0xi6udHnr6DiD22_Vkzt_ePA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این یارو تو فصل یک عشق ابدی رفته صداسیما
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81432" target="_blank">📅 20:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81431">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWF6vtQhFawjx7e0tva5BwYaznaHV74oasiZvciugdwRqk6xZ63nmjGBZqcF_K4-r-A6U6Lm-sWGigD47y0IaNpJ2nMXnCx0e6ylOHaat0Izfcg0nAALGyKv17XIsDk2Edcz1XdV1DGt6TGVBBKtO5W0y8cFXZi2CLs_S9It3SkRIXjX_ZpIw5YF5BaYn69cDt0E-Tk70vKwpjsQB8A-iV0y_niCPLjTTCc-ms_SUlaH_B6agDo_PzHj0cpDc4dwvEQOm4WBKP97R6kHjPl0Hj00go8weT6LyIP2pQsH7qxFxUUspijqOAUgQMyZbYYKqDT9__J23UC_JaaUEc-73g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو و دو تا از طرفداراش
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81431" target="_blank">📅 19:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81430">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sH5gXzdQW1KIZkVIi6finCyMWIch7NADQMvC9WI8XNd7PjVpVVAAVIQm__rFKSrXB9Ji9lWEXfcMjUcbq7nLeKSpQN7mIGihUUbnvJGM9b718YEffWXZHK0xbGIceD12zjxI3i-B4T8ndkzBx3DbLCZMoi-QtMV-9v_qvo8UTLm69RrTZlEPt1FfHMQooBZ46UdQPZbHHCIEG_Scw_oOlDuCFt5vzIpLSzdUdY65Xtm4Rj-pCXruT_xYzhvBRvFdr1sGm2U3LCNCv8vyCbjUcvPiCtdfKkP-PgdKMKRbPsZrBJfF6udYBB9s-5KBoEr4hA2roPPkeRGRVEuxZnXgyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توپ فصل جدید لیگ جزیره
🔥
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81430" target="_blank">📅 19:00 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/gngm1HJShIsWhL-kDfd_CknNuwYsk3G6nXPAzBJMw7e88oBKgJOyY312oEjCOaTJF-jPJKKjsQ_JtegOV8dDqGDWJpP2dtdN1aVRId_8tQYNCHbYFbPDsW6awe_6K0LwEh6IbHe4Hlv3wSqcXv-wBj_kedc10mtXb4LxHwUMNKeYTbl0vzuc3wTUs6I3N-V7fyIK2-BHoI6Sv5TDHvupmz7YSfQ6a-Q2WwUH35X71PFOv1XdNDEaF3rkHnUhShL0C9Tn6zNDC5SXCwC2rGM-SozECB_9pUnAGHctlzpP8FWHzVgSth9uueYRbMX32HOOBaNiNLQeEXBxN_KBHB4oxQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 192K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 01:11:19</div>
<hr>

<div class="tg-post" id="msg-80679">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">این آخرین نبرده، فرانسه برمیگرده</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/funhiphop/80679" target="_blank">📅 01:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80678">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">انگلیس سومی</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/funhiphop/80678" target="_blank">📅 01:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80677">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">حیف که دیکتاتور ها گریه نمیکنن سقوط میکنن وگرنه رو گریه امباپه میبستم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/funhiphop/80677" target="_blank">📅 00:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80676">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">آره داداش</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/funhiphop/80676" target="_blank">📅 00:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80675">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دشان جان بازی قبلی اینجوری ارنج کرده بودی فرداشب میدیدمت</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/funhiphop/80675" target="_blank">📅 00:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80674">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">انگلیس دومی</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/funhiphop/80674" target="_blank">📅 00:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80673">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">امروز مهدی داشت می‌گفت دشان باید این ترکیبو جلوی اسپانیا میچید</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/funhiphop/80673" target="_blank">📅 00:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80672">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">گل دوم انگلیس که آفساید شد</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/funhiphop/80672" target="_blank">📅 00:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80671">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">عجیبه توخل جلو افتاده ولی هنوز مهاجماشو نکشیده بیرون دفاع بیاره</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/funhiphop/80671" target="_blank">📅 00:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80670">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">فرانسه چه کسشر بازی میکنه</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/funhiphop/80670" target="_blank">📅 00:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80669">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پشمام رایسو</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/funhiphop/80669" target="_blank">📅 00:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80668">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzoQ-a7g0LN7aN9wvDLzk87ojdXKJrIbwc-RsoRjYc_92yMQwW28XLPFLgTSbKF7qCqXlfssl2XnwV1MUKybBchmTXqU9ouBSZroLhc8FdlyUGQAcvaxyWHBd816LaexUSUPa5T4n6cov84XCyRaNbvdVyOCn0aMYXf9LdG7rxVofbrbrIH-xP51sxDpCI3eeBYnl_jQSM1p7qqUSdG3gynv-Evw9aUf813_sdS46CTjn1ufczuvXL6q4vnkVB93J2kfqPGUp10bzuKJbUTFz4zY6tfDsDqH6J1i7AqxLhwXL_s0wjyV3Z5htZPYM1l6vLpocbkoxbtLXcOi1HBu0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امتحانا تعویق افتاد؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/funhiphop/80668" target="_blank">📅 00:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80667">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">من دلم نمیاد تو حساب دمو هم ۱۴۰ میلیون خرج مورگان راجرز بکنم، چلسی چطوری انقد پول داده پاش  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/funhiphop/80667" target="_blank">📅 00:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80666">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">من دلم نمیاد تو حساب دمو هم ۱۴۰ میلیون خرج مورگان راجرز بکنم، چلسی چطوری انقد پول داده پاش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/funhiphop/80666" target="_blank">📅 00:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80665">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">حدود ۲۰ دقیقه دیگه نبرد بازنده های جام، امباپه و بلینگهام شروع میشه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/funhiphop/80665" target="_blank">📅 00:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80663">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kANaEd8i4xbB0x19a9mrjyn9czNdHsPo6qNrXqWId5vavPC6P7FAwyhJEdULKOcR_4IZ7x0EUIk6uUVRYJ-PzIJcnNfEd8HIXJTbtG8MzYf-xyBY3EmCC_HozrSrQyx2UOpxRkudZSRe9exHFi9lcXZQt031zVC-1DMkyik1VBRdTcTAhbu3j9AWZ1t1bzUxWj2HesABMe54ugklaD5JDkN2Sr-1vo7mV3FzhxvkYFEuyCMhV8x8DM4kDZHnDn3E4caVFLLgLiq_Qr3EsQlo3G-e0OyBmHnu44zriVPWhGa7n5wxXHO6WRjjAdVJh8ekcqShMqefAUkR0F6x1qe3HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقدر زود ترسیدن میزاشتین حالا برسن بعد انصراف میدادید
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/funhiphop/80663" target="_blank">📅 23:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80662">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دشان جان بازی قبلی اینجوری ارنج کرده بودی فرداشب میدیدمت</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/funhiphop/80662" target="_blank">📅 23:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80661">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دخترا عکسو آروم باز کنید  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/80661" target="_blank">📅 23:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80660">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ol8FSpDMge8jEgFUvaswNSqSVO28GIk5U8mETiLvTb669sA_sSfaosoLoZYF-YPiMpJmF2GXsxrHl2t_2uR4mYIn38OpsRl9acsZ04bYKdhjzWeNUeOjj_hhGZtXCqe-D9era7EJQrulMGWhF0xVL3jt9yPLxFg728vBp-1r4i_q-GrlWUytSB9FxFGBoRUA-AoeKwfdDybYqAMdwFEFlELpelBXvvcFxc-5w9lQ3DZ1AJCpXNOAEoWAtE7L3_rMT20njArRxICnNNnFisfmpHBiluiTYzA8Sb5hBcz09dWhOeZtN5E7SH-_AUX06TTjwgS4jxEqyV9Kfz6OUILSKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دخترا عکسو آروم باز کنید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/80660" target="_blank">📅 23:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80659">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">دوستان مگه ایرانه رئیس جمهور مملکت بیاد برای جذب نیرو فراخوان بده و چارتا تازه کار بردارن بیارن خاورمیانه برا جنگ، این پستی که از ترامپ داره پخش میشه فیکه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/80659" target="_blank">📅 23:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80658">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">فرانسه هم قشنگ معلومه فقط اومدن برا آقای گلی امباپه، خط دفاع رو ذخیره ها بازی داده خط حمله همه هستن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/80658" target="_blank">📅 23:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80656">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">انگلیس یجوری ترکیب دومشو بازی داده انگار بعد این مسابقه میره برا فینال
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/80656" target="_blank">📅 23:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80655">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ولی جدی قطع نکنید، این پولدارایی که وصل میمونن خیلی یبس و توکون نرو ان، حوصلم سر می‌ره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/80655" target="_blank">📅 22:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80654">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اگه نت قطع شد بدونید دوستون داشتم، اگه نشد هم که کیرم دهنتون ازتون بدم میاد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/80654" target="_blank">📅 22:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80653">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">یکی به این کصکشا بگه جام جهانی فردا تموم میشه نه امروز</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/80653" target="_blank">📅 22:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80652">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7QgudmJE1ePi4FwNXHvwWx6MwTX8urZuc3i0N1PUEk2qY0OGWEc3ZZWzJ4QDsLaqTeLsK1aSakAkwyaKD3p_lSLaAVFDN4RYQJf9Wgf_VFjMt-mJN83GnGuX2l1SA06yaw3ydjGQlzQo0MeYjZDVSD28FGCinBcyorxPuCDgYRlz0aoYZs00Bc3ixZ7vJdmVcQgxfwDm3Qk419zW_G-Wa7oSNieVEgyt3VEPBMzdMuLVQheQcm4YSzvsgZDC4XRABFO1WQESq7yLc73Jy-DISxlyXaTyKkl_Rmr3OuXsy4EJyn4J1ojQbgldVCMkkcCu8Lxwptce9zTeiT-F_2K8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمایت بنیامین نتانیاهو از آرژانتین
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/80652" target="_blank">📅 22:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80651">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اسرائیل به آمریکا پیشنهاد داده در صورت شروع مجدد جنگ تهران رو به اسرائیل بسپارن و بقیه شهر هارو آمریکا مورد حمله قرار بده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/80651" target="_blank">📅 21:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80650">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">امشب به احتمال زیاد حجم زیادی از حملات به زیرساختای اقتصادی کشور انجام بشه، اگر جنوب کشورید از پل ها و صنایع پتروشیمی و بندر ها فاصله بگیرید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/80650" target="_blank">📅 21:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80649">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🌎
اَپرا | سرویس مولتی لوکیشن
🔥
زیر ۳٬۰۰۰ تومان برای هر گیگ
✅
اتصال هم‌زمان به همه لوکیشن‌ها
✅
اتصال با ضریب در زمان نت ملی
🎮
سرویس گیمینگ اختصاصی هم موجوده
📥
خرید: @apranetbot
💬
پشتیبانی: @aprasupp
📢
کانال: @apranetwork
🚀
سرعت، پایداری و قیمت؛ همه‌چی توی…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/80649" target="_blank">📅 21:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80648">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromApra Network | اَپرا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YtAFByfnCcu2UJq1LFPkTlgMpY1mOeZaj72tkRqAUxMNmne9SUc3udpoegObd59BpvC_i2tz37l6TWV3dPeqAFpBcyyxmvp43QG5JBoIgkM-HaUMm_L1MuuUiyIJneusL2aBqIye0EB5SanCAXafTa-7xOmSNDyRKlJFxkNW7qlRA25GVcVeLRCCI-pnmDWzWJWLX1T89cSUsLm1WTBVWFzvh4s9X-WBDVpHzcq-M7io5ZQMp6niCU9p7PB8yB6XA6r3ZUE8ASsGKNFJArBCMUn1g7wubKE5B9bATRAlXwKGcqUEkU8r3uWLGVI44Dd_C7JDsX_HNXvMN7M-9tI4Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
اَپرا | سرویس مولتی لوکیشن
🔥
زیر ۳٬۰۰۰ تومان برای هر گیگ
✅
اتصال هم‌زمان به همه لوکیشن‌ها
✅
اتصال با ضریب در زمان نت ملی
🎮
سرویس گیمینگ اختصاصی هم موجوده
📥
خرید:
@apranetbot
💬
پشتیبانی:
@aprasupp
📢
کانال:
@apranetwork
🚀
سرعت، پایداری و قیمت؛ همه‌چی توی اَپرا</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/80648" target="_blank">📅 21:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80647">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ کونی حرکت کن
فاکس نیوز :موشک های ایران مستقیم به نیروهای امریکا در کویت برخورد کرده و حتی جسدشان پیدا نشده است
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/80647" target="_blank">📅 21:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80646">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">یکی از سربازا هم مفقود شده   @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/80646" target="_blank">📅 21:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80645">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">عاصم حرکت کن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/80645" target="_blank">📅 21:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80643">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سنتکام اعلام کرد 2 تا سرباز تو حمله جمهوری اسلامی به اردن کشته شدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/80643" target="_blank">📅 20:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80642">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سنتکام اعلام کرد 2 تا سرباز تو حمله جمهوری اسلامی به اردن کشته شدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/80642" target="_blank">📅 20:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80641">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">یونان اعلام کرده ۶۰ مسجد رو در این کشور تخریب و تعطیل کرده و هر کسی که مکان مذهبی اسلامی بسازه رو از کشور دیپورت می‌کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/80641" target="_blank">📅 20:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80640">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_XmAaQQaAih78wqEhNP4SFMtyfO-yEBw_A6u_zwu5RGsg21v88K_4VXYmEV35bWWRqm9NT8GbK5dUTQZqrI7CyZYbxLtaEOF8Yk2q0iiOU6EXse8XUEwNXgfEZ9XhjgTaXRwE-QdhKoiKWs0gyd8C5p_IyGDBUvkqd7lGi_CLqiYdB6mIUtVVsNPI5rR5rfr1ntzfm7NmCXaAQtsQknt7N3f-yy89emp8EQTVJyssX3hUsPeOr7WtVQvW_dXi3lhkPNxUY_MhkJvxEmt7u7QHvaEdTL8v11xu9cVBIAQYcxOT9K0N7kRBh-Eo0vPK70uA3xNAjAZJTisi8W_ShoUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا چرا ایران  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/80640" target="_blank">📅 20:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80639">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2v-ty7d-y5Rr6dRGd19yv8Z9JbXkls_9GqDcuboaOBIaePb0MHW1zmCuteDpl5Bw9flFS7RiinQJ3zsQEsk261o_FnXr6mvevL_8yHZdHzcMFsnhenlmQO_4jjJ6ACa7U4bwIIBGDdUUmv1u7XwGZbzh9uQyyiSFjDPiv9VoRdZcxXnsu0HZuUUMuhpYQFQ9AlRlduMNDv92zxwXxXPmNp6yaKjzBkJ_qpH0rBM8tmisOK06jiiHXTzkKFSzbENgCIbP0ugk6SW7i9HxkJhI5MpFvyh5mA0nucSYeg8hqce_inJK2uSs37mqgs4LX5J6Qg_iW2UrAWCDAjew3HJTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا چرا ایران
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/80639" target="_blank">📅 18:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80638">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzdFqGrSCiffUbzy5gr8-iatz1UEWidBii6p4GlJ6QQSLeKmM-hNZ1G6DAas2_O7Ynl2JQjANv9OKUa-EdgJ5NzDwryKVLndKs8pXQ3dCtsD4c4rPwn1-kzH6KZYq0B9CcxinLV0K6589baxGyRJDtwLb7JLZiDuht6ddiZ7-cgMcHeaCADWbg79nloYDvhtKJSRWqq8OfBfxZIdVQfBgukXN7OtJRzJ9twMjd1qxtK3mNLDLV2eABn6PMT6FKlL7bVdyBOGX_O4BiAynfmlZPf-FSt8AXrnWvXE-nHjRPe0spTg05FEXUpwDEccrOeogZsgSGQmR4yH3FRPiyWiHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
فرانسه
🇫🇷
-
🏴
انگلیس
🏆
رده‌بندی جام جهانی ۲۰۲۶
🏆
🕔
بامداد یکشنبه ساعت ۰۰:۳۰
📍
ورزشگاه میامی (هارد راک)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- فرانسه در مرحله نیمه‌نهایی با یک نمایش ضعیف، با نتیجه دو بر صفر از اسپانیا شکست خورد.
- انگلیس نیز در مرحله نیمه‌نهایی در یک دیدار دراماتیک، بازی را با نتیجه دو بر یک به آرژانتین واگذار کرد.
- برنده این دیدار، مقام سوم جام جهانی را کسب خواهد کرد.
- با توجه به قدرت هجومی هر دو تیم و عملکرد دفاعی ضعیف در نیمه‌نهایی، گلزنی هر دو تیم گزینه مناسبی برای پیش‌بینی است.
🧠
وقتی از بازی لذت نمی‌برید، متوقف شوید.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g27
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/80638" target="_blank">📅 18:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80637">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqMXIaj_ZZK3DHWGLF30rvxPtqIIuQzQ9jDS57DF9HWlv4dRy9WAzElT3nMlVMi4pDhe6FymuqlR1cGg06c3bQaYqygVvFXea1SYYgpIlZR7s9K4ktvqDCN9ModUrB7FrG9ENCMzXL9NTG1mbBhKTcZIuz2TN7TvuwhfpfuFTGSSnIzhTuKaGMaBJVIrs3M3sooiwZNIS_mnc3ccFLJG4URWO78pAIQZ3rmY5-aWQoH2LQGkb5Bcf1EzHtxKbZw2T2QfTq_FCT8WYRllcfZIgh4oAVmPjDUDyU-WGKGgbTjZJVIDICh31yt-mPNBkazTQpROQVlmKPi7FZkRe43rxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوکراین خار زیرساخت های روسیه رو گاییده، کل اصرارشون هم سر بسته بودن تنگه هرمز بخاطر همینه که نفت بفروشن بتونن جبران کنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/80637" target="_blank">📅 17:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80636">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">جمهوری اسلامی ایران تعلیق توافقنامه و مفاد آنرا اعلام کرد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/80636" target="_blank">📅 17:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80635">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwtmnXljKYq26_z6__s8PYwuyzc3HrHLbEElogtfrd7GsynXmwwLgfTwTy0ql9puQ4Hj_lqOCdTMn-FEuAdaq1ALXmUBeTBmBwrJHCkCUZ49auzN7WNwVVUXc5L-9It3QQGBJ3IcMwM6HFsjK2FlRNmLlb0wcyUHhWn9ED3ec63B7TSyWodt39SlTCM75wezJhXSJPO_zPPetm6GCB1h7fw6784Q2mRtUbF-wk14qnMmqbRokjBsu8I1Qh189g_3q1-EpMOXSy3p60mwJPym-c6EgeT11ApttMPgfuJeMULAAre_6KDSY0mUfub6TRJdIUjLTQce6hIKttponXBZ7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عشقتون برا فینال کاستوم آرژانتین زده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/80635" target="_blank">📅 17:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80634">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">این قضیه ۳.۲ اسپانیا جلو آرژانتین چیه، چیزیو از دست دادم؟ چرا همه همینو میگن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/80634" target="_blank">📅 17:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80632">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzq-WyzNQgT5iFMy_6KebbBKaPIuzvsXoErxBadJbo9eqhUdaoqGYHir0MkRG5dcov0LPFFgPMJX9O96rS5T52PllNL-eCrozLN8b-oc45x36hp-pAuF5TtCK4vwm5kyUAB8j-uX0ObQnlGSOX8cZnbYJ3N-mVXsUy0hk2c2QxLJy4ytk0daFGH49hlBYrz9ZS0UP4ueQTysMy21R-wufWa0nvtHE2zG4FFfk3w0EoJ5UTPCChYITyOOQBxUHhXJWXmtj8VTJGUr77fyA60aHf0GQqLddf9tXH300Pj2pUzE6IXe602bjRo2lF_-FOfDTz2WZYhwmoYfTH3ldVmksw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا به من ربطی نداره ولی آقای حیایی یکم شک بد نیست.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/80632" target="_blank">📅 16:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80631">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اسرائیل همچنان جنوب لبنان رو میزنه، آمریکا هم جنوب ایران و آتش بس همچنان پابرجاست.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/80631" target="_blank">📅 15:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80630">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c8c64445.mp4?token=gOR4PaaFgMXEPdqr5QINXPtHEd9Z-HORFpKmZvku3U355friwA3ltGfYIJe66G_ZYo1zbVhJM066-DZfnbaSIl50s-fF_tntHzv1PkMhe3MMYUItS2gxKimv94_ZA2dczldZI6-mHQpCk9mRv6DujzNYUznST6aNiKQJU-iO4AIpDyksGLjP1htH14CEMQiUfy-5blUw54mzOPgbqbiii7TjqDHCzqD0J1AR3nULyvkZJYrYMC0OoLH9PphRreGLJQ6DGT0qyOfoMlIwNWv_QhrvlOsoRlFD_Yq5R9RlMQlq9daO9tRRBtOm0Y6HH-25IguU1Sdgc2Lut6yXknfkvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c8c64445.mp4?token=gOR4PaaFgMXEPdqr5QINXPtHEd9Z-HORFpKmZvku3U355friwA3ltGfYIJe66G_ZYo1zbVhJM066-DZfnbaSIl50s-fF_tntHzv1PkMhe3MMYUItS2gxKimv94_ZA2dczldZI6-mHQpCk9mRv6DujzNYUznST6aNiKQJU-iO4AIpDyksGLjP1htH14CEMQiUfy-5blUw54mzOPgbqbiii7TjqDHCzqD0J1AR3nULyvkZJYrYMC0OoLH9PphRreGLJQ6DGT0qyOfoMlIwNWv_QhrvlOsoRlFD_Yq5R9RlMQlq9daO9tRRBtOm0Y6HH-25IguU1Sdgc2Lut6yXknfkvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در آمریکا به دلیل پخش «اذان» از تلفن یک مسلمان در هواپیما، فردی دچار وحشت شد و پس از شکایت او، هواپیما به صورت اضطراری فرود آمد.
پلیس های مجهز به سلاح وارد هواپیما شدند و مسافر مسلمان را بازداشت کردند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/80630" target="_blank">📅 15:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80628">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dDQ_J3YzbzpvaDmum8J6hM8ihbjys8ssMDK39DdUnmMcxg1XXo6XVF9TqfnSzVw_Tawz4m5h2gpJ3ducuAHzCVw8UP42cgs2p_AMt7p7DYjNPT95dU2F4TBSUOBkE6AxENcQKWR4kY236i5wOk2rLxnHRughhSnGRoFPvN-nCkear1C7BY_WTlnorGoQxLeuwQePl249pjbNJ2QekBa1Yvh8ahZDOb8HZlU48QxxtMqJLtW300SOdnfmqlZ6nsNr8jkRM19XiCaJfciFLOQD6R67W1nttEUoZeaCAzOq3uBUTPm6jd4nTs9_T7L5c5VwtcqLpW5OgBbdgHYWQ33xGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hNrAg8IumMZBaBBVstebxvBG9NJCI9WIvVasnpyrxoa8s-NecnzYmx0kSsUCOEetbtdEMho2DeNjsplOL-mbSFThCtPh8SThOBgGZ8s7Xh9xjxA-9tOyt7v7IPw_HF3Ow_Ohj035zvlZO8VvCa7rD_BXSZT2WEpU6uQmdOiNB1E-vEBjWQFSjbDhsxFJGB4aC6OZZqASEqwMJcf8G6_JfsOjRuSXrJE6Ls5vH0qCq7ktMLmcbRyeageIt96ccY5ovilKl1k_qLoxMqiVtmK9lwkGaftGt6-HQPe0dDeyr0YtIV_3H3TmaMRGXTXBYCVtlAoICLD2Kgw0Ctczd6F46w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این سگ تو فضای مجازی خیلی معروف شده، چون همه فکر می‌کردند این سگ نابیناست، اما آزمایش نشون داد فقط آدم‌ها رو نادیده می‌گرفته.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/80628" target="_blank">📅 14:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80627">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ولی خیلی حرفه بعنوان کسی که دوسال نتونسته تو لیگ کصشر بلژیک دووم بیاره به کسی که تو فینال لیگ قهرمانان اروپا بازی کرده و قهرمان آلمان شده بگی رانت خوار
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/80627" target="_blank">📅 13:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80626">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">خوش اومدی به بلاد پاری
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/80626" target="_blank">📅 13:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80624">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31fa509f3a.mp4?token=NHq8r-kXNHaGbPfnEfObcIduaAqrAbS9A-nFKCGw79nyli1blbHZegAcTaTBqSYwMllIWVUfNL1d2dYk9lRi79fjujko88W1PbbJepjRqzUNDsgptyuBfdWF9S2vAqGM44HvEFlSPpwmvfCIWwafTuC7fgFDkcqo_c-Qz5RkDviBanj0DxOFjjkSIPYU3p_1_gQOWetOzfIbw-2t0MHiZMiS4PbE9CzTmv9UI5SGRBzfoPZG2VqzWFTjaqpoguVgf7nLA_S6nT-UjwSlrhSxMdDqbR2lrpNwiiiurglaeuXVQTFCuLwXgUpPYhs3OXMCOFgmll7mO984eMF-OjQzSzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31fa509f3a.mp4?token=NHq8r-kXNHaGbPfnEfObcIduaAqrAbS9A-nFKCGw79nyli1blbHZegAcTaTBqSYwMllIWVUfNL1d2dYk9lRi79fjujko88W1PbbJepjRqzUNDsgptyuBfdWF9S2vAqGM44HvEFlSPpwmvfCIWwafTuC7fgFDkcqo_c-Qz5RkDviBanj0DxOFjjkSIPYU3p_1_gQOWetOzfIbw-2t0MHiZMiS4PbE9CzTmv9UI5SGRBzfoPZG2VqzWFTjaqpoguVgf7nLA_S6nT-UjwSlrhSxMdDqbR2lrpNwiiiurglaeuXVQTFCuLwXgUpPYhs3OXMCOFgmll7mO984eMF-OjQzSzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قبلا مسئول شستن ماشین علی دایی بودی بعد الان خودتو در جایگاهی میبینی که به اسطوره فوتبال ایران حمله کنی؟
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/80624" target="_blank">📅 13:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80623">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NR-m5vvEbH_OVLH25WQHyDp8rBXGnMJIKdyR-dmLwOb9OhjbmIUwemsY4Y1mPDuBe3hZNnre4P9bl3z-WPo_SejDSCZ9lyYmvbgMYoD-cNaJJW91yxDPoDA8XoxvY7rz0D6nZ9n9D7LcfPWxUED3u8n7lZbQEofMlqIx6zm7EspjMojJhbqtlgtajooRq38Mq4tfpSlLMHXl_zIJmbkdEnzZhgFaBfIw8Ui9KJxKVGs0RWugKmhsLefpDtDwx4ToN9xGwBYzuGo2rPG8kkfiGxfxlbQ2wMJqCZCqK4G5w2XcSFBzaVzCCCR81dxy4VnwJboxcVFthenIZ6GMpobgmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باخت آرژانتین قطعی شد، دریک رو برد آرژانتین بسته.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/80623" target="_blank">📅 12:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80622">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سخنگوی قوه قضاییه: برای ترامپ و نتانیاهو پرونده قضایی تشکیل دادیم و کیفرخواست اونا صادر شده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/80622" target="_blank">📅 12:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80621">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbfbfbbd0e.mp4?token=JGpNp-d4oPnVwm9zWTfQO197T2drDkcTJndkp2djekqizxXuGwk7gzFZ1LR8TF5a1YBmqVQkyqjtqK2gDh94PdRrHtsP8NmPwyIdk8u-cudNZtRt0e_wXtPqEpRiD0SeFEPuUXqUm5wNH7nI6YulzrAioWrULIKA7nZ8QX47gjuhinnqo36oeah18M94l3PZEatAuYngXIVXzq_sMFkyAzHa7gmZPLyMyVmk6ZJgSlSmK7DdsWJGOzGQt7_OPN67-DlH5zps12dGPjO1qZN_lEf-jT5LXxuF3pI9xVpliXhAdjMLuORvfiBjiR7ZTUcfL7Ky0JlTl6bWEFVi_3pJ4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbfbfbbd0e.mp4?token=JGpNp-d4oPnVwm9zWTfQO197T2drDkcTJndkp2djekqizxXuGwk7gzFZ1LR8TF5a1YBmqVQkyqjtqK2gDh94PdRrHtsP8NmPwyIdk8u-cudNZtRt0e_wXtPqEpRiD0SeFEPuUXqUm5wNH7nI6YulzrAioWrULIKA7nZ8QX47gjuhinnqo36oeah18M94l3PZEatAuYngXIVXzq_sMFkyAzHa7gmZPLyMyVmk6ZJgSlSmK7DdsWJGOzGQt7_OPN67-DlH5zps12dGPjO1qZN_lEf-jT5LXxuF3pI9xVpliXhAdjMLuORvfiBjiR7ZTUcfL7Ky0JlTl6bWEFVi_3pJ4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تشکر پرسپولیسیا از علی بیرانوند برای استوری های دیروزش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/80621" target="_blank">📅 11:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80620">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSG_bvbZ6BqwyAMPvELeG5K3VWmo-yD6wAH5sHm8dw-FEKOfqB5RpFuq5j211xorOgDmfcoDOc9gNFis2-Bks_Iufuc7WeltDoS6-OiV_qFj5wmV7WhEXB0iTWBi6VjVTpJnSroHOIHAi5WPcMQckHeuSXJ5fdjIQnNC-B1MIz7M_LuIoCAip-lfdcmtgVCheBXNWnVmf8EyiDX3uVMgzgPgile8_nSst2Y4euvY0q7KEVbXGuzN9a3Nrps88ce3ltrQBFd1I2y2OL4clJmdotykFjWUmo67grSRijsKwjV2wYUTIOUy5MQ8FImsI64uLM-ogzpVKh1ejeeZvkLCLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه تو یه کشور نرمال امیرمحمدو میکرد میفتاد زندان.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/80620" target="_blank">📅 11:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80619">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nue1yjE0e97TnNMSWKY3hEw6uf1MFOgXrLNm7hoUpYT-Hku4iv0kvIzaufT0mDVuGrHH3Q7w7tntE4fGLQ4MryjXdpKTqkxZJyDG8uB4OgVBftn6E41ixIxy290hZRLhaT1t07-zwQzx9v35O71LygW3xH7XVbJ3xVzCX0XoWvbNKNkpyPslD3V0j3TtP13m4slJSff3t6y5vsE1m2Cjint_wBKm3v3keFF4eqJ3pBI0rbNLzOXf5ZHcBiMbMGGfy-COjG8iAKyB3vFYEJQSngSSdD-yvvyd1r-dn3OZE92KmByghpBRFk5LCz5UqS1CKly9KT9aEnS8on81bP6GOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
فرانسه
🇫🇷
-
🏴
انگلیس
🏆
رده‌بندی جام جهانی ۲۰۲۶
🏆
🕔
بامداد یکشنبه ساعت ۰۰:۳۰
📍
ورزشگاه میامی (هارد راک)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- فرانسه در مرحله نیمه‌نهایی با یک نمایش ضعیف، با نتیجه دو بر صفر از اسپانیا شکست خورد.
- انگلیس نیز در مرحله نیمه‌نهایی در یک دیدار دراماتیک، بازی را با نتیجه دو بر یک به آرژانتین واگذار کرد.
- برنده این دیدار، مقام سوم جام جهانی را کسب خواهد کرد.
- با توجه به قدرت هجومی هر دو تیم و عملکرد دفاعی ضعیف در نیمه‌نهایی، گلزنی هر دو تیم گزینه مناسبی برای پیش‌بینی است.
🧠
وقتی از بازی لذت نمی‌برید، متوقف شوید.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
27
💻
@BetForward</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/80619" target="_blank">📅 11:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80617">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1XXXusMSgb1BFu91oABhtS3CqTaLcXtT97EspLbk5NgjWZLlOTXbpyXp0KBcDL7dvOgjR0TxHuw-U7m5FLYAoG1OTjwKgNVH3vusPUl_KxLEMMGAEeGhNsVyC7qvYLOr8Ec2sRgCwPZPZeEoTAWPcdZsvjKbQxyD8shyjPAssZT7sv61WMGW-gGqJi5wCMYPHEepdqyTKHz4GS4Ahw42Nx7SRw-Z7jGxswtisAFG0Z98H0lb88H19sbJwB767uf8oNLvLslxyaxD2Vuu3GWJ8oofvg7YASEijaWcyGi9oFufRUoJCZ_EwqiUYRpdlZ2F0GD9IcnjkrLW3GS_icCOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیشرت ایمان صفا تو ختم مادر عمو پورنگ.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/80617" target="_blank">📅 10:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80613">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOlSa64LfnS1neMlpi7l4hVrl3EoGZX6r8IXvlWfFnVtaC10aYGEV3J0UEkakA9y9FQH9w_-w3hhAnBR84B-Cqw7MhQrDAPzBwFmNPjLnj2I9lQL9bZNE0BfSGWhd2vscklDnEXuFPtg_cWvqEuJjzjQDj0FkrmNwvhsxVCr1f3ea-HdTsWadmVYsopdPdG53yYEa4seyOec3gXYZq7rzCA6Iru_YAeDlIY9IOHvXUAeBnV9XU4AHD2lmR3rQsMaT51KTPCgpZxceViq97W0TusVvMQQAFYto7ZFAUGoj9pHVA123O1GiKv2gSaUMAdtR3WE_z3YBt2TpNqWs1TiBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیژن مرتضوی قراره تو فینال جام جهانی بین دو نیمه اجرا بکنه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/80613" target="_blank">📅 04:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80612">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">از الان شدت حملات کیری میره بالا گفته بودن بعد تعطیل شدن مارکت جهانی (3:30) شدیدتر میزنیم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/80612" target="_blank">📅 03:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80611">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پایگاه الخرج عربستانو زدن، محل نگهداری سوخترسان‌های آمریکا</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/80611" target="_blank">📅 02:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80610">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">روزتون چطور گذشت؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/80610" target="_blank">📅 02:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80609">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نخندید
ترامپ
: امیدوارم یه روزی برسه میزبان مشترک جام‌جهانی آمریکا و چین باشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/80609" target="_blank">📅 01:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80608">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">حاجی این قرارگاه خاتم الانبیا که هی میگفت اگه اسرائیل حمله به جنوب لبنانو تموم نکنه میزنیمش چرا تا الان نظری راجب جنوب خودمون نداده؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/80608" target="_blank">📅 01:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80607">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/278e4b296b.mp4?token=k_tTfczPzahncZHyFw8iHlzhhFdcV9AF4DgMrLocsz2hrdzkP7ZPN-pPAHckT95lT_buLXxA_d086EcJc3AQi0VOqDMtZ1O71vJ_Y3flElixNxhhmpcErMmi4F-Yrr4JU0MFh0F7fm5kzNfoDqqnZZgxHTztlZfmor7S9seVtItBlbvW2VG-AurB1vmwbCuXma7yZgVeJn-9GfqNnMWCrLsV8rr53ZrViZ1Zv337BIWS7gou5lg54hDuQu5xu8PI2lxPCzMYK-i257kXieiOWvmH6NX1pFdoGhaYl7JciyVeaCoSto4odrkYUNdql2Dv2awC45gKl3N16Q8e3-aAow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/278e4b296b.mp4?token=k_tTfczPzahncZHyFw8iHlzhhFdcV9AF4DgMrLocsz2hrdzkP7ZPN-pPAHckT95lT_buLXxA_d086EcJc3AQi0VOqDMtZ1O71vJ_Y3flElixNxhhmpcErMmi4F-Yrr4JU0MFh0F7fm5kzNfoDqqnZZgxHTztlZfmor7S9seVtItBlbvW2VG-AurB1vmwbCuXma7yZgVeJn-9GfqNnMWCrLsV8rr53ZrViZ1Zv337BIWS7gou5lg54hDuQu5xu8PI2lxPCzMYK-i257kXieiOWvmH6NX1pFdoGhaYl7JciyVeaCoSto4odrkYUNdql2Dv2awC45gKl3N16Q8e3-aAow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استانداری هرمزگان: تا الان اصابت و برخورد پرتابه به بندرعباس گزارش نشده و صداهای شنیده شده احتمالا از منشاء دیگه‌ای بوده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/80607" target="_blank">📅 00:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80606">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">حداقل نهایی دانش آموزارو کنسل کنید این همه عذاب و استرس نکشن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/80606" target="_blank">📅 00:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80605">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">انفجارا داره نزدیک تهران میشه، دقایقی پیش صدای چهار انفجار تو یزد شنیده شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/80605" target="_blank">📅 00:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80604">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">گروه BTS تو کنسرت جدیدشون به این شکل یاد جاویدنام های عزیز رو زنده نگه داشتن.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/80604" target="_blank">📅 00:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80603">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Soyu7UTVWQKG8JB-IVFyidqWvr9BxYJ5tbQP6q1RJyobragORqj4xqwjatEMQqAAi4BOLq8pVPgUIMjrqdBvkRs-mPrUZYtlRqD364zz0lCLkkH2AHeqg1v-SjHRdXqq9AYE0YoMdwdorOd2mVH_rSlxW91lkMnq-uue21cbttIy3_qsO0o7sS5Fb3v6NSXxFTiv20bafc7VAYVP05FDNpFNM9mKUhV4QazecR00S6XLE6967jrUubEJ_pagHsXed1KCiWZwUIiS7ov7iuqhdxavMWQ832aHK3Kn5MvkL6mOLaJaMJFnB0WDhKBbOAsxZywcRVCJnDfRs0e9MoROfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گروه BTS تو کنسرت جدیدشون به این شکل یاد جاویدنام های عزیز رو زنده نگه داشتن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/funhiphop/80603" target="_blank">📅 00:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80602">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1W0mw6Ttus7dGIQwPUF7F8-CcJe4JbtDYMlhCBvHeZGL6gMs_T2tin3pH4DiAhR0VtYvJl6gezqyzICxa7tEAyjFaVP06WzdnuaFLK6PZ9NZturlvmIEQnXq1lqNOs0NU8_HSxjPHwfjWN2h7pLkNR9aQy3UmC47GACSEpTGJ8iKbWKgbBAeorZxe0k0g4JttkYWgdJyjOhFcVq9PMG_ghczeLY5fsxzLFtwjiHttLAGPFbLPoZSQP24Q363xgloAjYCuC5UZw1tLXNAE5sPijSDFW90LuGaLOd9bAkTaILZ4-TPQPmICWLKKI6DrlUv97AQP9Tn1Uxk1FE-u3xOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی بیرانوند شرمنده زنت گرمش شده بود مجبور شدم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/80602" target="_blank">📅 00:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80601">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">امتحانات تا الان چطور بوده؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/80601" target="_blank">📅 23:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80600">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">موج جدید حملات آمریکا شروع شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/80600" target="_blank">📅 23:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80598">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uSVR1owWtPgMXGx7IYKpiqJT3--QHKN1Eenn0hRRfqV301OoU0jWxnTl65fHSyfQ9xY8KuFauq98EM97wPIB3icR_U8GhOGpfrY9Ehzbth9jSdbMUugEsT-s-2xLB6JWcakGsc3msnOiteCS9h8Shw_8AHmUkeVbhp6zXPhw_UHhRqlb2IDQryk2WEtrSFUEaaK6axcL2CzDwj2g9DYHEeIAjF214tRLaoRZ20IlmuesZ7ZtsEz56zsDmQ2XqGoAzTW26jDs0_33KU98EGDVwOGK0TMXF2UR_eZbLGHZdMasAdZQr3YETZiuvV5wfp5y85pzKzSYGvO8K1R6S3WYMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bufdRFgeyLL6FrLf_4bhJY8prB0ZCjSPud9JENzd1qa9keZvbBmDjxia6NGexfn7Nmn8H11NT2yQ4MRfKCShO4SoZmfmd9x-N9O1gIkeyjvtWnkJvRlUf236TOQhbqpzwh0pdaNgrsaQfzi7M6QzxU4mCdqzbyvrsjwODd7cuDMppXO031R8xXZ6O6ZOHFQCQm1GjwEXuPdDkvwFer3McXpRWfBrlxvHZQvZt9DV0kjQgrtmpVaLg0bdCd7P6fpuN-1Fjf2C3D0tfuY66CesfjIYEPBrnXlS80ZObczjqhbIqBqEo1uva2p5COU8XUoUIL7xsNs5lGEV5Rzz5lt9qA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کیر علی دایی تو کصمادر همتون
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/80598" target="_blank">📅 23:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80597">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">یه روز ادمینای فان هیپ هاپ پست رپی میذارن یهو میوفتن میمیرن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/80597" target="_blank">📅 23:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80596">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">رسانه عبری  از جنوب حمله زمینی اغاز میشود ناتو و نیروهای کرد و اسراییل و کشورهای عربی و پاکستان نیز وارد میشوند  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/80596" target="_blank">📅 22:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80595">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vh0yqLd2CjCk7y086TUju54Zc78DnA_PQCriD0h8uQqYBaITq-nJQvfhnvhgrCqPitZ_vaXXFlgW2GUVHzzDB-DXbNKesg46y5Kp1yd4enHsMC5ESEqBfL2g-1cEWZrifyHBtm7L01YGzhHeSzfjvBlsuXWQucDDIwIryRwwurxw6ZqKeUX1HSOs1vIgqxzIZGEfnCq3UqwP3ovx9ZRS3YsuFYOvC7zBr7JEd2_96g7J8Do9HNghVq-8pOjaYwDg1-uVbKrJkpoJ_5zv5uNnUqwdc6Xdre3lxbVblMDgLZDdX-XIhlBE-E5XrVEsa4RJKL81g3NIUsMlTJyiwj9dTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه عبری
از جنوب حمله زمینی اغاز میشود
ناتو و نیروهای کرد و اسراییل و کشورهای عربی و پاکستان نیز وارد میشوند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/80595" target="_blank">📅 22:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80594">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">توماج شیر دل، پسرِ اکثر مناطق ایران به جز نصف جهان.   @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/80594" target="_blank">📅 22:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80593">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/280efc03ab.mp4?token=CVKremBlVBDShFs8mh91FS9-cy87OpqlwYXVmwsqSWJE6gAdQxN91kAfF1cM70-nlxcfnH3sFJVPQLRVucyhVGsTLWWxq3ngycy4tpMgRIQork2dyC-iJ9T3mghdFPDYSTQ6oA2WzHeRBqTxmfS4WvrF9RjGCmfI0iPnpEWBgXz7s9SAEXuEDIpb5uxbzaeDiOk0VUXKb3Ww9SrO2uqdmxdLbZwp4huo947zaG3aXcvnkt-gZDKyf8A2kOdhjNhzoRTRK4Phgfb2VStl6mt76CMnbYFg2ADxh4pTfAfw75dbEiV_jZAXMvjrulYoJaE03jTtMBSWmWeXJYYq2KGyFg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/280efc03ab.mp4?token=CVKremBlVBDShFs8mh91FS9-cy87OpqlwYXVmwsqSWJE6gAdQxN91kAfF1cM70-nlxcfnH3sFJVPQLRVucyhVGsTLWWxq3ngycy4tpMgRIQork2dyC-iJ9T3mghdFPDYSTQ6oA2WzHeRBqTxmfS4WvrF9RjGCmfI0iPnpEWBgXz7s9SAEXuEDIpb5uxbzaeDiOk0VUXKb3Ww9SrO2uqdmxdLbZwp4huo947zaG3aXcvnkt-gZDKyf8A2kOdhjNhzoRTRK4Phgfb2VStl6mt76CMnbYFg2ADxh4pTfAfw75dbEiV_jZAXMvjrulYoJaE03jTtMBSWmWeXJYYq2KGyFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توماج شیر دل، پسرِ اکثر مناطق ایران به جز نصف جهان.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/80593" target="_blank">📅 22:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80591">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اگه خدایی نکرده زبونم لال یک درصد اتفاقی افتاد خواستم از همین الان تاکید و یادآوری کنم که این جزایر ما خواهند بود که سربازان آمریکایی رو محکم درون خودشون جا می‌دن و به عبارتی به اسارت می‌گیرن.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/80591" target="_blank">📅 22:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80590">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اگه خدایی نکرده زبونم لال یک درصد اتفاقی افتاد خواستم از همین الان تاکید و یادآوری کنم که این جزایر ما خواهند بود که سربازان آمریکایی رو محکم درون خودشون جا می‌دن و به عبارتی به اسارت می‌گیرن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/80590" target="_blank">📅 21:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80589">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcNd4IR3sgAMIsykQO9njum9ADy13bdDToHjMxyBmVWWS901o25FlWtht1ThRvfMa9QsCJDAZVWFdpvg-1Zl6e3PaVPjHRy7QgHyTDMIlcVJ6AdMGEqVMRPErfOa6T3SPPkhAQzvu4XKQjTBtA5Uv9lXkXj-0zdN62FQaAigMOR5CIWvRbVHb4NziBBVOkWRfVVgZpF4gdYkIMRHK-vz7MmbyH8hhTA3HL_ap66QhFAKMmGInSdSIg4ymMIQjryCh996ZMKBl8vIIWMsALB_7M2s7jBtIFGr5BOeAmvBWWf2nhDTs-hHxoSQ_gRinWMlJatXFWYfZo4pGTJUAEmRYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا رامین هم رفته بوده اسپانیا ساشا سبحانی رو ببینه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/80589" target="_blank">📅 21:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80588">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jmn4SFuYsbug2Xo1FCOf5DOkjGBMBcfZWdJmJbcRgZN7QMK7VxTW20cXIu2hk9seRSFCyqSptOR4JzvAnKbABl1ATwnboKCGWTOMy2AlBCmHJFNtL5VW0WxatB4rncU2DPOtSvwFZhrKs_lnOIp_kPSitHm3laMxVVcFj4Gf9klKHxmKus2HO0cupmTRfTkhAR5F2OANmrtkvSTMZEpuGw0Vj7QppvH0D5R-uIJKsPOW1jZNbo7qOwpsQLjJMWSXlImOSVVfJF73qU14H3h6ldZTuBIpAH1mtZG4kqYc4jhBfcNhJe_nfJO7TKKSa_CROt8qpUcod2TdvwqArjd5FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار برنده توپ طلا ۲۰۲۶ رو یه مرور کنیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/80588" target="_blank">📅 21:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80587">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHappy Smile VPN</strong></div>
<div class="tg-text">🔻
HappySmile VPN
🚀
🔺
فوق سریع
🔹
فوق پایدار
🔻
بدون لحظه ای قطعی
✅
متصل با تمامی اپراتورها و نت‌های خانگی
🔺
تمامی سرویس‌ها آیپی ثابت هستند.
🐱
مولتی لوکیشن واقعی در 7 کشور
🇩🇪
🇳🇱
🇦🇹
🇫🇷
🇸🇪
🇬🇧
🇺🇸
🚀
10 گیگ --->
❗
فقط
40 تومن
🚀
20 گیگ --->
❗
فقط
79 تومن
🚀
30 گیگ --->
❗
فقط
118 تومن
🚀
50 گیگ --->
❗
فقط
198 تومن
🚀
100 گیگ --->
❗
فقط
388 تومن
🚀
150 گیگ --->
❗
فقط
578 تومن
🚀
200 گیگ  --->
❗
فقط
768 تومن
🟩
تست رایگان
♻️
ضمانت بازگشت وجه
✅
خرید فوری از طریق بات
👇🏻
✅
@HappySmileVPNBot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/80587" target="_blank">📅 21:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80586">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">از دستاوردهای آخوند اینه که بندرعباس و جزایرش از جایی که همه آرزوشون بود توش زندگی کنن تبدیل شده به جایی که همه ازش فرار میکنن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/80586" target="_blank">📅 20:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80585">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3bm0NTlDwBnsPccgNh3peDHESlxdNMYbCxFgEK7Z7oLjIwtFjYwPoXRxNKngdAC28g2PiKxcyOeFdUq-dSvIbZMIEqrvbsuIfXAfWHOqgnDU2f00yUSny9GPFtkDLsBU_xr1vVWxrh4WrG1AxAjwFvGGmufvIM4kYXGSDxk4p35in99RTtBjW4nYXt0esDEBzB7urkqUQxzFXbNwTDsHDj48u5MjMLur4DLbraRyOKwA7VypKp7xsWR9ZPIAxYfuIQaRpDWaQHo9txbZyt1zZRZjoRYyUSTwt_0VhpZ-a1ns-cJG5rYFnptqDifeMq5uVvNyY8QnAenoaj3LPqLXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا که بحث حمله زمینی هست برید فیلم warfare رو ببینید که بر اساس واقعیت هست که تو عراق محاصره شدن   @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/80585" target="_blank">📅 20:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80584">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIHlqKWMuUkJfcCZk0uwwxxEqCS6SNP334MgpHT6ZPDKvALTVW-Nq-NONcmPl3bZT71-TYy0QIJvWrx27Wg-tUZlotv5gSfT-nGjgUj2y8DRILCSbH5WyaXkOKZfjZ0m2SnvBjRzuLEtdxKluJOzAL87HQ9RRsHa7h26nNG1RxnBmXVuDGkP0328DDNwwVSOBblf_9f9ZFDANMIvtsjhwWWiTjAhCbTlF6YgiF3G6RPmj1fXLlW-_68SQIuI1brKCZVoXQtA25aHsxYAtOGqBXGDkdD8B7aZ22sTwSHtvwDOT0ZkxpBQHaz9cQyc0SDBiL5sXBsb6ql2FVhmYjjamA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا که بحث حمله زمینی هست برید فیلم warfare رو ببینید که بر اساس واقعیت هست که تو عراق محاصره شدن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/80584" target="_blank">📅 19:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80583">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">رویترز: پاکستان به جمهوری اسلامی هشدار داده که اگر به عربستان سعودی حمله کنه، اون رو حمله به خودش تلقی میکنه و وارد جنگ میشه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/80583" target="_blank">📅 19:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80582">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">علیرضا جی‌جی چرا دست از سر رپفارسی برنمیداره، بمیر دیگه کصکش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/80582" target="_blank">📅 19:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80580">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1OFpflkyx-PtWRFvmHxb6U67o4o9MfJEY_EIhoKidp-JA9b7qqTnR3wXDYNSQkfc9A1VRD8UYPtYeNIEkyv2i12DNUeDRfnNpI0K9R9B1vsx87MDpVs3rIKLN3ygzuwpoVvPx_nCUt4GJH162ciOIEAomvEOG3blj0YXbjPDqHnatBMVUwJlnKwYO8KpsckVjqhKHB0tFevqgEpXyRCxmI6ecu0aPnKQpupPXEIUWfxTKHeGHIuzyfI_C4W78MKofpdf-jhpK5lXKvx-4HLo2tsktMgOdUTzn72Wb06nShaM0yJaDq4machdy_ksG5bviO1t9GREEMN3PtYjXxQ9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3d51fa3abb.mp4?token=n9g_28Ma6uPrEYqgAp4QTY-aLy_DjBcPQKfis6_ww4bSMhmE12eQ0Dgl9Dvv9oUTiJguPkVd6B36KLWfKA4CJbuR16J5wkXcGzxHfLQO48G9UmS_nnt2kKKZduFOP6aJYa6n6Cpkg52W4PmAKIPmmKoFHTDbh2BqpKCDXpD8mRh8p01RlusF_DpELdWU3i5WfzhBRj8D6iqwpjT6yL0gHiuYtPpdaoEsR4fk5VTstIzBGOLzKeIoW-0u_SauJ5rBjlhAnAmJLry0PKYYst1iu6nSgqiO2gflgHUopxS2Pk6BwmZR0nqKfI4yefdr7OB44X5bnvM7fmXmw-ExUbvG0w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3d51fa3abb.mp4?token=n9g_28Ma6uPrEYqgAp4QTY-aLy_DjBcPQKfis6_ww4bSMhmE12eQ0Dgl9Dvv9oUTiJguPkVd6B36KLWfKA4CJbuR16J5wkXcGzxHfLQO48G9UmS_nnt2kKKZduFOP6aJYa6n6Cpkg52W4PmAKIPmmKoFHTDbh2BqpKCDXpD8mRh8p01RlusF_DpELdWU3i5WfzhBRj8D6iqwpjT6yL0gHiuYtPpdaoEsR4fk5VTstIzBGOLzKeIoW-0u_SauJ5rBjlhAnAmJLry0PKYYst1iu6nSgqiO2gflgHUopxS2Pk6BwmZR0nqKfI4yefdr7OB44X5bnvM7fmXmw-ExUbvG0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی تبریز یه نفر بخاطر اینکه کل پولشو رو برد انگلیس شرط بندی کرده بود و باخت، خودشو از طبقه ششم انداخت پایین و خودکشی کرد
.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/80580" target="_blank">📅 18:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80579">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/liC_RL8ELBX6N4fKq3t7xxKwl_yPYk_uPcUX71Pg9jXoL-rgrRf05igCrGUI1S7mBz1GD8vcxBRC0bYo3zJ5-JxutM-qr9tfCTw5bxtn15Ss30C-H-jtySDTAcN-pJLCQwZwYA1nm9Pq-nmrguGRYFb63ur_HTYLasvgWZ5GtUQ1CqiswV0U2sF8uD03pvmYyZLZLoVjUJnnac4Ho5xYdLnYGyEHpOvsPNveBB-jAAupe7Ejt-X7oU6pS8Yfm0W9WhsK_56nWLUqhaxAZIbiYjqbp2sMmm74Vvenwkzg6bNBrn6QRdko8znSwt5309tMlxOK5QxmMhKjtmG7jS4Tkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسخوش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/80579" target="_blank">📅 17:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80578">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1d29960e9.mp4?token=hh7P6a6z-aWIIjBVGL1cvi-n_qnRURwnFpeAPcEL5IhyTuwRDUL3zS0Ih0BucKw9HEPKjU6zUzqIh50t3PlM2nA5uM5GgmkB8t4EGHDUPeexO9zQYtvFdVJJo13K5zSwUVFkH5-iY8XuAbpAhTHQAviNUuxV1G7qRP0uj4UakPkPGcv3PX70RiwLhV8Fl8HvpUV-rvcalXbPSaTl1tucKbLT8TfCOaouSFRn9JGBDhcIYl3LCCNN574bmbDIcya24TFWruedPXV-lHWXw98EFiJGtUX2x_2apRd3eirEcriOe_uUH0G_TEybc3pwhFM63d2EBpRBikVnKvVcc0cOHSb9a2gsQsKfz1RJB0Lglq3cqfytBYu_8yMWvf-o3M3FleJd90bBkFtFhZWDwsRyIMoMJd06oyD1vU1um1LFYw1k-fAU64r0LiPl-bPX-ekVhV-Yv3RKu8LXwe0AxrcCcbJl0d4kAr5obnuiEbUKAO7BOxjlYcs_skj19_4KSlrA0I3x9o5V8gVnpww0mLjfPoGu0GZOmcB5a90Pn2ii72SU3nnpt55i87QiOG6qecSP-T660sLXoahgHKgPW-Wf0q1Wfe__FHh0plMDJbmGlBOcv9LwvzROFj0XnpaweycIquUkMDsK-Ic0FVowcV2j0Pt4h_8dbHBCxgRf9YxDZAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1d29960e9.mp4?token=hh7P6a6z-aWIIjBVGL1cvi-n_qnRURwnFpeAPcEL5IhyTuwRDUL3zS0Ih0BucKw9HEPKjU6zUzqIh50t3PlM2nA5uM5GgmkB8t4EGHDUPeexO9zQYtvFdVJJo13K5zSwUVFkH5-iY8XuAbpAhTHQAviNUuxV1G7qRP0uj4UakPkPGcv3PX70RiwLhV8Fl8HvpUV-rvcalXbPSaTl1tucKbLT8TfCOaouSFRn9JGBDhcIYl3LCCNN574bmbDIcya24TFWruedPXV-lHWXw98EFiJGtUX2x_2apRd3eirEcriOe_uUH0G_TEybc3pwhFM63d2EBpRBikVnKvVcc0cOHSb9a2gsQsKfz1RJB0Lglq3cqfytBYu_8yMWvf-o3M3FleJd90bBkFtFhZWDwsRyIMoMJd06oyD1vU1um1LFYw1k-fAU64r0LiPl-bPX-ekVhV-Yv3RKu8LXwe0AxrcCcbJl0d4kAr5obnuiEbUKAO7BOxjlYcs_skj19_4KSlrA0I3x9o5V8gVnpww0mLjfPoGu0GZOmcB5a90Pn2ii72SU3nnpt55i87QiOG6qecSP-T660sLXoahgHKgPW-Wf0q1Wfe__FHh0plMDJbmGlBOcv9LwvzROFj0XnpaweycIquUkMDsK-Ic0FVowcV2j0Pt4h_8dbHBCxgRf9YxDZAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏩
کانفیگ فیلترشکن و پروکسی رایگان در ربات بت‌فوروارد
🎲
🤖
با ربات رسمی بت‌فوروارد در تلگرام، تنها با چند کلیک فیلترشکن پرسرعت (V2ray) و پروکسی تلگرام رایگان و امن دریافت کنید و بدون محدودیت به اینترنت آزاد دسترسی داشته باشید.
🚀
سرعت بالا و اتصال پایدار
🎯
کاملاً رایگان
🔓
دسترسی سریع
👍
برای دسترسی به اینترنت آزاد و بدون محدودیت، به ربات تلگرام بت‌فوروارد مراجعه کرده و سرویس مورد نظر خود را فعال نمایید.
کلیک کنید
@betforward_bot
کلیک کنید
@betforward_bot
🅰
r27
💻
@betforward_bot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/80578" target="_blank">📅 17:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80577">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">توافق اونقدر خوب پیش رفته که بزودی هزاران شهروند آمریکایی مهاجرت میکنن به ایران، فقط لباس نظامی تنشونه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/80577" target="_blank">📅 17:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80574">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">لاپورتا چی گفته باشه خوبه؟ گفته اگه داور خود فروخته نباشه اسپانیا قهرمان میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/80574" target="_blank">📅 17:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80573">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ولی بارسا جدی بین اینهمه کون بچه به دوتا بازیکن با تجربه مثل رودری و لاپورت نیاز داره</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/80573" target="_blank">📅 16:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80572">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">نقش من تو قهرمانی یورو و فینال جام جهانی اسپانیا با پدری تقریبا یه اندازه بوده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/80572" target="_blank">📅 16:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80571">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrKUh5Cz9SgFgTWhLoE6y-VPKOxf-aezWTyVA4MJN7ty0O7IMM6jm0Z_gt8NRtYWlN2D-2BGduLyWlSycmMDbnZgSzc2VFfCxpYkwj8veMJN7TjMhJKHlABXMK6mqb8869DFdru7wvNGv69PWkgwNq4oAFVFWUACr6IVJ8vSHNLbI8slXtcBXYo9-7_VyuOxkFlisNTy931rFfLT01xQU-NtkZYxVxTvHu5THSL_T-6mGfUOpb8OZBVQGvJQyHmIujxMNz2s4u2SJKqHuA-1fJVuuRW-3z5Hq2MJNoCYj4uN4LQQuJk-F3oqGMY-JpqZM5qJ4SjuCTUC43qsh32xOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکسای مسی با بازیکنا کنونی بارسا یجور عجیبه انگار واقعا خودش پدرشونه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/80571" target="_blank">📅 16:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80570">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">باز خدارشکر این اتفاقات جنوب پیش اومد، وگرنه این وسط بازا لال میمردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/80570" target="_blank">📅 14:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80569">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">کل زندگیتونو ببندید رو حمله زمینی آمریکا.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/80569" target="_blank">📅 14:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80567">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">قیمت دلار هم شده 190، صدشو بزار تو جیبت ی نود بده بهمون تا آخر ماه پست میدم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/80567" target="_blank">📅 13:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80566">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">لغو عضویت جانفدا جز بیشترین سرچ های گوگله در حال حاضر.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/80566" target="_blank">📅 13:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80565">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پخش جومونگ شروع شده؟
اگه شروع شده لطفا ساعتش رو بگید
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/80565" target="_blank">📅 13:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80564">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYXwqy48u3n9IX0ZLlwxUYqjvRZalFwOvaNCP7cDpItHV36OmMmoVYF6jexA8esjQMECcIBP7xKN4cJMVs6X3_zy1RL67tc4T_WJL9ZhUgcqDQN6UIv5pRRMpuJXepj-odhA1cYdaFyJiBrudPehhbJ3CiwSyJAvZ-QO414fL_pO06KiFsYPevaC_uT5BUDR_oVYjOMMCQqvHiaSJwmpeoan01G4b6QM8LcwbXERCZdUSJZlqWVWcf_QJ-hrOPCjqYtAmVzU1Ke9e98tmmEOlB0hY-C_NkMvvaf-nzjMQhJM_Xje6bhNIpM2Uc4Wxitl31-z1ptoQyzyvXiWbeUzCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/80564" target="_blank">📅 12:19 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

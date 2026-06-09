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
<img src="https://cdn4.telesco.pe/file/Wnddt4d1UHGbXjSYSQL33owErkEaAUxMdSx03aFpSPMjgVIN0J-8sPQTfo_y7Yxw9BmqaaUaVnTIhEyGtaj5qtaKUjQFMu9bnj6Vqtu-bqYhqjeNrNO1aE_OFf5Uo21W4KfavVRiDrgoZsS5vLV3TtXQO7mbjCrvKvlLgqXaHa9aRW3pXLrZnGVsGMrQClxITzoXAc1_kfm1a1cVoOy2-a7Ilj6M6OWoPPD8HlaYnQm3Np4mq_vCqMn6DLv1Gcvx6d0qCUvFT7gxndjr0k4f-1y0gBfLmYeN55wSkF2gzjPRyjNTcJvdSuCUdvLedpp1riLKOigX4dee9dPySGELrw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 173K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 23:56:59</div>
<hr>

<div class="tg-post" id="msg-77357">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNhgNiu6rc5xjIdn2_vAjPqx6tJtLdN12-KNnNXnpadZJs-U5RQRk40c9i0aUnysaz--eLMEoJce-o0OvLNA9ifW9VcbdvTt8V5qiqkLltx_luPTxzmSZ7CG7PizKIFMEn4CtLRCFzTrAR0cEZcJwMwhuBbeuQpeF_7zNBf39H1QhhIzFhyLrFYnhBXcWmDSK19TgfF8KJ4-0kL6oZQ13gYhvaqT7v_RNnI8gqPNDWYioIniZup64vSttIdyQxlvgqXGzot2uUEFlBCf_UOhQtdclmHLxcCfhSHj7zjYnvloUJTqCDiHxKOv_vpcSURLPxz_raheM-y-4BvDq8Q_Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر ورزش:
به قلعه نویی دستور دادیم اگه وسط بازیای جام جهانی کسی پرچم های غیر رسمی (مثل شیر و خورشید) رو بیاره یا شعاری داده بشه سریع بازی رو متوقف کنه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/funhiphop/77357" target="_blank">📅 23:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77356">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ به وال استریت ژورنال:
حادثه هلیکوپتر آپاچی موضوع بزرگی نیست و خلبان حالش خوب است و مادر بنده هم جند.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/funhiphop/77356" target="_blank">📅 23:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77355">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پاشیدم به در و دیوار
معاون دکتر عراقچی در مصاحبه با الجزیره:
ایران پشت حمله به بالگرد آمریکایی آپاچی در بالای تنگه هرمز نیست.
این احتمال وجود دارد که چنین حوادثی به دلیل فضای پرتنش در تنگه هرمز به صورت غیرعمد رخ دهند.
هیچ هدفگیری عمدی از سوی ایران علیه بالگرد آمریکایی در بالای تنگه هرمز صورت نگرفته است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/funhiphop/77355" target="_blank">📅 23:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77354">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLRDkD2OqbTZ2v6tCHBVLlVxa_XNvkYsTKHrO5xu_o-zIqLivllCY0QDPV1cygmXiuELYtFd5pm1Roa0ld3b4LHjlzuB1GjEiXgeqHmxP-H0f-DmD7LtXHdBboSrzXIrDeW1qfrTjBefUW6uA3CLUAEyuWqN7_tXq5HgEJlEtVxxJ-d6_M6yXtGqJb_gYnO34NKB0KRuztor0f0U-Y647QGaHYlRWKaGaruY69UoILrncjZA4KscYbF-Gj3qqU8LlcXqZXF6QsaI_IeEQsEBR72LMxwV9c0EaZEJdA0WYAwQ1-nseaQHHY4YoBqGlC7E-9edWbMU7e6fN5PlQsGDow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/funhiphop/77354" target="_blank">📅 23:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77353">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YF1-91u8vwDRGJrvUlEbqtXkq5eGsk7CIlNaBgSueRcnnLnvqBTm3W_5pCrB8skDeeUqHQnuDx6VB79qxjBc1_9jSy-yb3d97SzweIA-E6XlSx4L2mIoavpQFyXLCAuZudJkLg75xvcNOfMkcrum4bjjbio_zz44dfGvHsG7GZXySh2wjoarc7LvkeIvx6uLQbPXbqYfAm2j8M04V9ZysaYbnyjIGYJ0WbXPoPidIysPrSsiG5Kjs_QWyL5uRyAPpGxwvaAmoTecJfG4Rp1jmsfbiBErRZDnHD9nM0alMOe5Iw9exFv5ECMPwjBhGF_8Ly3eqarY5-CzmquMGlvU2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلایه ی پزشکیان در توییتر از نحوه ی مدیریت جمهوری اسلامی و سلطه ی سپاه بر کشور.  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/funhiphop/77353" target="_blank">📅 23:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77352">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxd6rrP4zKmVCHjNe0LZg0YxULbIyMXqg4GgEgiTXoAQUxoHoWetgwAhRmqi4JO9uOBviIYrdvj2VaMbyWdrA4WdXXeX_lU0k4p0z-CG4S8gsDNlqpXrOQYW8QO15tKe0OZvxysMP369UUOwutmDKFcbeR4LZyEyPLAM_GAI4MSYMRMidS_ZBLykEL8rxSN3fvn7k8W2Wfsv0tNK8qfLvtlL_14dpr4gu89nZFwuM-C74r5-y3iUeRAhpbaeJ32DUAWI7jbbgODZ2JBKP4gsMedS9VLa0kF4zUPj_I-sCKnAnIe-vXljtnj0p5ja6HqQFjAjV92v3bkEQII9OaWUsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلایه ی پزشکیان در توییتر از نحوه ی مدیریت جمهوری اسلامی و سلطه ی سپاه بر کشور.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/funhiphop/77352" target="_blank">📅 23:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77351">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">داش بمولا این سری، این سری دیگه میزنن
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/funhiphop/77351" target="_blank">📅 22:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77349">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">خب امریکا میخواد بزنه ولی ازونجایی که ترامپ دالگخیزه تبادل اتشی بیش نیس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/funhiphop/77349" target="_blank">📅 22:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77348">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNCPU1IdRxZgdD6DpUTDCYAa8R4OxYCxGQ8Bn-wBGg7zxs9VZOlibbJs1gnlYr-OZx5i0KPlwIERb2chiVLSYNFmEuzKFbe39fPYEaxFfILnTHckZ3-OfbHA19iG3-Rm2E1J2niaaHExDeM6RPvzvVwOY66-dIyogfxu4VDflWxOQ9n74nGPXhQMfYrpummNHQ_Sa3IKHeLhu2pN_RnHqTaZNe4EyAgmUxMt0UsTgSe8xcoxBMJus2BgJBVitMqtEve08d0HHo9Qwps_288XoKdLA0tyMYs7aIs6Vv5fEA-RFsE-gL6Hh-YHERf53yKK7639k0A7tbPa6UGpURUe-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/funhiphop/77348" target="_blank">📅 22:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77347">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپارس شو</strong></div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/funhiphop/77347" target="_blank">📅 22:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77346">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRCjKE4ttkBZu1lBUUggswgBB5Q3r5KoepfZsWUDV7rQOLWfV_mBzZ10QKmUN_wkcm_MfhH4K5XsEx3ncocEkz7joubgq836phUdM1Plf-3S1lE47kZRKrieiwffyKMwfaxo3Az7gVvcOmEAsdNEBhGVLKm7kGoy_GT7hVjqnlhkWsa35S5jnBxi-bYAIq646Tagb-WM1P_RQ8dxlcv7d0jvhAE2qEaVS4DA2ViQTbmsF5c6L2LWDOa-eA7MvOxyW1RR3vP-dXHjXK7Htl6-C1pDY-qZ83OVzhXUIAkpkQjSEog2n0kI9uzYQ-BSZSXvAJ3GuLSDP2yjkI9JGF85TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قدرت مذاکره:
نیروهای خارجی در نزدیکی قلمرو ما به دلیل اشتباهات انسانی خود، حوادث ساده یا احتمال گرفتار شدن در آتش متقابل، همواره در معرض خطر هستند.
برای کاهش خطر، بهترین راه حل این است که آنها منطقه را ترک کنند.
ما زبان دیپلماسی را ترجیح می‌دهیم اما به زبان‌های دیگر نیز صحبت می‌کنیم.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/funhiphop/77346" target="_blank">📅 22:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77345">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ به ABC : اگه یه عده بخوان احمقانه رفتار کنن
ممکنه کار به جایی بکشه که مجبور بشیم کل زیرساخت‌های یه کشور رو نابود کنیم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/funhiphop/77345" target="_blank">📅 22:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77344">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دوسی خبرنگار فاکس نیوز: «او در دفتر بیضی شکل بود و از او پرسیده شد که آیا خط قرمزی برای از سرگیری یک جنگ داغ علیه ایران، کشته شدن نیروهای آمریکایی خواهد بود یا خیر. و او گفت که این دلیل خوبی برای از سرگیری عملیات نظامی خواهد بود.»
«در اینجا هیچ نیروی آمریکایی کشته نشد، اما به نظر می‌رسد ایران واقعاً، واقعاً تلاش می‌کرد نیروهای آمریکایی را بکشد چون یک هلیکوپتر آپاچی را سرنگون کردند.»
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/funhiphop/77344" target="_blank">📅 21:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77343">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">آکسیوس کاملا روانی شده:
نتانیاهو پس از سقوط هلیکوپتر با ترامپ تماس گرفت و از او خواست به این اقدام ایران پاسخ ندهد و حمله نکند.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/funhiphop/77343" target="_blank">📅 21:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77342">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خبرنگار فاکس نیوز گفته رئیس‌جمهور آمریکا در آستانه دستور دادن به یک انفجار بزرگ در ایران است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/funhiphop/77342" target="_blank">📅 21:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77340">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پرز برا آلوارز پیشنهاد ۱۵۰ میلیون یورویی فرستاده</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/funhiphop/77340" target="_blank">📅 20:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77339">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پرز برا آلوارز پیشنهاد ۱۵۰ میلیون یورویی فرستاده</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/funhiphop/77339" target="_blank">📅 20:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77338">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f69d28ab16.mp4?token=NgmxtmB1Y2BrQFuRafTNr9RtNuDKeJiaE3quZHVsmA1hA3lv4OuRAuabhsS-UGi4TS7tbf86yb3GfkyoZZ7b_NHJScsnSMFvC3faJnqNqqjnxOETXUfzUvmmjwrr9PATZbN3dMLqInW-M9n0RdvodEYMTNTeZ-qjVSzZ0ryIFRXuNcWJhCm3_ICFPVtOZiHFWpxgeuWrER2f8pLe_GBvY3Akf3RMd-E9fh2Eax_LDhbZfbGf_X3gmwG-67F9WHlRQ7ikD2WzW41HtGycub4JY50_943-bW8U3FiWhXAm7JcrJ-grD3SZEvJoAMd4SpMjGuEAolNiikk_d-bJHFCPcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f69d28ab16.mp4?token=NgmxtmB1Y2BrQFuRafTNr9RtNuDKeJiaE3quZHVsmA1hA3lv4OuRAuabhsS-UGi4TS7tbf86yb3GfkyoZZ7b_NHJScsnSMFvC3faJnqNqqjnxOETXUfzUvmmjwrr9PATZbN3dMLqInW-M9n0RdvodEYMTNTeZ-qjVSzZ0ryIFRXuNcWJhCm3_ICFPVtOZiHFWpxgeuWrER2f8pLe_GBvY3Akf3RMd-E9fh2Eax_LDhbZfbGf_X3gmwG-67F9WHlRQ7ikD2WzW41HtGycub4JY50_943-bW8U3FiWhXAm7JcrJ-grD3SZEvJoAMd4SpMjGuEAolNiikk_d-bJHFCPcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دالگخیز ۳۷ بار توافق با ایران رو «قریب‌الوقوع» اعلام کرده، اما هنوز هیچ توافقی حاصل نشده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77338" target="_blank">📅 20:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77337">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JC6g0YvhfFNAvCzv6ccFCU2hU8cNcOpSkuiyig9V26oFy0TUb9MOeZHVTKldalu60NX5ffeKsHo8-ycc3QW3E1S_ofnu9pYJ9xhv4KeETo51S448n4DBjmbFX65sddwn9zUd25qcHRo3hlcqUNxjXnPqZ6RqfFZNLo_npLtJUsLIxj2fEs3wak1C6EvIYzwP0oBQSX0cHdgFeI-L692sRZ4MbZYjeAWjhj5sHSUBXk9cII8CjnhX9eSlCas__EOI76YZSeipWgn2HSJl1NiFU-GpgOkpZD_KSvpPlEgokrYQpYcVgp_rLNTi6cCpmG6Ot8xZrYRU_0dFZKahz6iTFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دالگخیز:
ارتش بزرگ ما به من اطلاع داده است که دیشب ایرانی‌ها یکی از هلیکوپترهای آپاچی بسیار پیشرفته ما را هنگام گشت‌زنی بر فراز تنگه هرمز سرنگون کردند. دو خلبان در این حادثه دخیل بودند که هر دو سالم و بدون آسیب هستند. با این وجود، ایالات متحده، لزوماً، باید به این حمله پاسخ دهد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/77337" target="_blank">📅 20:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77335">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kzit9HgOsUGaNqB8e5ZNH7bwUTvioR5G8L5yXsD0lnggsWBofGBR4GfhBXLWbjEYY_2U4ohSYaOB6SPteUa4VhTwU58JVmTC0CakJJmtAkSAq0QrCYU9q_xU6fNPJNyWZGh-XvOwCRL3VuJNuN_5aoAyHElhBBAvEm0R3D09LeYVA2_Ix7-uZ7hqx-FvH-0J0P-eNNV7nQZeMmlDlvHSpNcUbYzigWumkvx7JmMODoCrPfzuXVvtRaCHamg10sHXLpDh-lymc5TtWO-IU1SmnVZLOps8HM4vZZAswDCMSSPV-s2uMhssy3Raw6kfjFgJVj0BxT6BoyBufNYocoi2Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوپر تخفیف گیگی ۸/۵ رو از دست ندید
❤️
🚨
0️⃣
1️⃣
گیگ 100 تومان
0️⃣
2️⃣
گیگ 200 تومان
0️⃣
3️⃣
گیگ 300 تومان
0️⃣
4️⃣
گیگ 400 تومان
0️⃣
5️⃣
گیگ 500 تومان
تخفیف ویژه
0️⃣
0️⃣
1️⃣
گیگ ۸۵۰ تومان
مدت محدود
🦋
سرعت عالی
🫶
بدون قطعی
🫶
با لینک ساب
❤️
📩
همین الان پیام بده
@wevpn_admin
🦄</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/funhiphop/77335" target="_blank">📅 20:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77333">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کان نیوز:
تو درگیری اخیر آمریکا به ایران ۳ میلیارد دلار از طریق یه پرواز از مبدا قطر که تو تهران فرو اومد پول داد تا دیگه به اسرائیل موشک شلیک نکنه و آتش‌بس کنه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/funhiphop/77333" target="_blank">📅 19:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77332">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اسپانیا قهرمان جام جهانی میشه این پیام بماند به یادگار  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77332" target="_blank">📅 18:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77331">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اسپانیا قهرمان جام جهانی میشه
این پیام بماند به یادگار
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/77331" target="_blank">📅 18:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77330">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMnkKRzTyiQA2_VkEcJtDZUER5CT-11Q9oNvHIsAKAqdWQ1wEyATHq9-Lbc3q5Mtudd-DZv3s-8Wj1KC495_XsKocSuo-RHxoKUcK4Y1Ve--fG1DC8keBii3qXy07_ZOwSyN-XYWonCNe7Gyygq2Vv-XmiWJOUkc-w3JDDk_GOehve9RIH2rypdv-QrUfaN_9a7GdbRFDM64QbVfF2zERaZUoIgEUGwi2RMTA0nK-Ig5btzja-8vFcuy9JWQK_4s4NS2ar0nh5opAft4BItT_NsKRlYKX_o3nGUfhNGzAXA-6mPcKMDRYmeIQbVVx22-zMFqjSOT1dwklq08Asn7og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه عملکرد مهدی طارمی و رونالدو توی جام‌جهانی 2022 :
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/77330" target="_blank">📅 17:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77329">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/funhiphop/77329" target="_blank">📅 17:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77328">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9l9CIvZ1TTvnoD5RAUjgds23GuvHnFQ3crjpz6MW35c13urgEBDZaA2GL7pbMdFaJTMEJYvugok2ebTb0HmSX1-Hj1jpjEgO8c91SUwkJDmi6QFc6qpU4lH4SW0nxa-OCEz0lsFOOTHksx8vvpAEknDcpQZoEru6txt7rI8Q0-fWzk9mNgpkC-VAWOc4vlD9UYPEWpZtdUyx5-039wtjBK7YvVrMxzUDaLnYv9GV-5V3ZDB4GyKB_FukvZ0hNmsxwXPkoOBftE0YDZHdTXXJeQ5bM-AWic5I9abs1m0B4lv3zQ_6kkt6SaHMgWdqIiFoP3YtvILW4oXl7hBBT6AKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی جام جهانی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
برگشت باخت هفتگی
🎁
هر روز 100% فری بت هدیه
🎁
هر روز 20% شارژ اضافی
🎁
گردونه شانس با جوایز بی نظیر
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
🎯
ادرس بدون فیلتر سایت:
✅
https://mafclub.online/fa/?btag=260368
✔️
کانال تلگرام سایت: g19
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/77328" target="_blank">📅 17:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77327">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سخنگوی حکومت طالبان:
صبح امروز عده‌ای اغتشاشگر علیه امنیت ملی در شهر هرات اقدام کردند که نقشه آنها شکست خورد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77327" target="_blank">📅 17:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77326">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">تاثیر معدل یازدهم مثبت شد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/77326" target="_blank">📅 17:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77325">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">تاثیر معدل یازدهم مثبت شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77325" target="_blank">📅 16:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77324">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">یوتیوب قراره رفع فیلتر بشه.
@FuunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77324" target="_blank">📅 15:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77323">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">میگن تا الان یه نفر کشته شده 22 نفر هم زخمیه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77323" target="_blank">📅 13:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77322">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/c0fbfca63c.mp4?token=dlTAySJzy6dQL-h6-x-LLhKBs1B-Y9CqISGxJd4SaBi958QGntda_CzbXeFD-Qg5V52GBk_3VMzgdGvBwEZW_c33Fcsc5OyMoiURTeUeQ3Mpw_Jk_l8ZMfZhXRQX_voPF2IMaXVjLcrL1sNUHRv3xKjXg10eId-jviD2LYG8DZilKAJeDzXP9Sgl4zMnEllOt-oBpKHfs_aQkNH2Q43s93Jd9T_hi-jTu3HYbSY_lyB5UTA21sW0CIl_4gdvdiBfJ5xq6vB8GjgrF1EPrEAlzNj1h1K2Pyd_Xj2bG1loBKU3QH4ke3weIzdmZ4s9CNAf7aikWpLkOD-ETPpO-LFoAA" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/c0fbfca63c.mp4?token=dlTAySJzy6dQL-h6-x-LLhKBs1B-Y9CqISGxJd4SaBi958QGntda_CzbXeFD-Qg5V52GBk_3VMzgdGvBwEZW_c33Fcsc5OyMoiURTeUeQ3Mpw_Jk_l8ZMfZhXRQX_voPF2IMaXVjLcrL1sNUHRv3xKjXg10eId-jviD2LYG8DZilKAJeDzXP9Sgl4zMnEllOt-oBpKHfs_aQkNH2Q43s93Jd9T_hi-jTu3HYbSY_lyB5UTA21sW0CIl_4gdvdiBfJ5xq6vB8GjgrF1EPrEAlzNj1h1K2Pyd_Xj2bG1loBKU3QH4ke3weIzdmZ4s9CNAf7aikWpLkOD-ETPpO-LFoAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگن تا الان یه نفر کشته شده 22 نفر هم زخمیه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/77322" target="_blank">📅 13:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77321">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">تو افغانستان اعتراضات شروع شده نیرو های طالبان هم هر که رو میبینه مستقیم بهش تیر جنگی میزنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77321" target="_blank">📅 13:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77320">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V39X24VsdozWzno3xT3-1XU3OIJhYWipgBXqsk-8jlSNxIsP7O5oaA-og3hV8dBeV0UnE7SXkAMiw7-CJl_EOMyRv98Z2EWyAMM0j7ZTc2mIz6LReo_IdbZW1wB83iLyAbIY5Y9PQh8sYChXYz62WDDWHrFzPeUNzvLIlH9EgIG41WzD_fE6vWTgEVEhW44vG9Fj0Q8ZKqNsiUuM5_lucEhAA1gn8_pHY-WK2zVZnREYKG9P-DLdHcIKBPscRCzU0SeGuA7aj4rjBpwJKufT1XueN4dZdp5uzacwxbIM3vjT1u1E_kc2610km7Y-asHt9xLeYg4dFR7yXOLcy3PFBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین حق‌پرست، از معترضین دی ماه به اعدام محکوم شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77320" target="_blank">📅 13:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77318">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">آتش بس vs آتش کم
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77318" target="_blank">📅 11:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77317">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
ترامپ در واکنش به سقوط یک بالگرد آپاچی آمریکا در نزدیکی تنگه هرمز اعلام کرد هر دو خدمه آن سالم هستند و کسی در این حادثه آسیب ندیده است.
به گفته او، جزئیات بیشتر این حادثه در گزارشی رسمی منتشر خواهد شد. هنوز علت سقوط این بالگرد مشخص نیست و احتمال نقص فنی یا عوامل دیگر در حال بررسی است.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77317" target="_blank">📅 10:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77316">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">شدم مجنون مشهور میدون شهر و کیرخر دهن مارو گاییدید.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/77316" target="_blank">📅 09:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77315">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bd5c51779.mp4?token=p_dIOzsuvf-L9CU0tu8REy0xOfP8toHGrPWy9Eq3YSCHk0FR2eUy8t6sU-2hOrSce8WVznBqzOVWLLwP0USVNrC6S4zgCiwetTgjJ6ISMUwc7rFK_1S5c1-T_tcZehSeFBnrRne0_0rKAWJDAANYvLa8scyalweWDhXmdC4Dpa8BQeGx7Rq55L0E2pawS8CvS-786ddQReIpM1WQxc1V1IGhe33kHvg-njNrW7Mu4-0vLElRu6J-YZ9mQlJQlY-mdvXsfdQADT-to909YuW7ZfiKdv1hMQsSqX1V9fg6QnKgin322K4JrClFIMhky4laM9RzcxMYFlU6p3hAFjnS1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bd5c51779.mp4?token=p_dIOzsuvf-L9CU0tu8REy0xOfP8toHGrPWy9Eq3YSCHk0FR2eUy8t6sU-2hOrSce8WVznBqzOVWLLwP0USVNrC6S4zgCiwetTgjJ6ISMUwc7rFK_1S5c1-T_tcZehSeFBnrRne0_0rKAWJDAANYvLa8scyalweWDhXmdC4Dpa8BQeGx7Rq55L0E2pawS8CvS-786ddQReIpM1WQxc1V1IGhe33kHvg-njNrW7Mu4-0vLElRu6J-YZ9mQlJQlY-mdvXsfdQADT-to909YuW7ZfiKdv1hMQsSqX1V9fg6QnKgin322K4JrClFIMhky4laM9RzcxMYFlU6p3hAFjnS1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از پیام حسین رحمتی به برنامه طبیب :
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/77315" target="_blank">📅 09:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77314">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLIGYwFTUYlHosLIRdQCcWYczGWlAktkndN0RHF9lQDTWDdvrXiGzc-3xZMJLA3oaRPcbgCKuXoYqBnXKUHS3IGfw5kdFEKZDMrf3kWydS9l4XDITLodlytQHQ0BUfm01yGxdb3wIGlVpLTNUP3RbiPbQEMMgO4eAAavcQ4XrZN-b0yQyb7zQ1t8iw9aUwaUGWp-rGpO2L42NdGVWGxC4Ipj-nNQhgo7kZPLjQARCG7XOtAL9nOny5d1Kol5vEtJ6WVnWEzWFv2CMnunhPSXVmhPZau9SyheSmXQy49HAQv_WE7RUWUt65egrndyjVbqRj3nJsRjVURpcsSWSBvPRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
آرژانتین
🇦🇷
-
🇮🇸
ایسلند
🏆
رقابت‌های دوستانه بین‌المللی
🌍
🕔
بامداد چهارشنبه ساعت ۰۴:۳۰
🏟
ورزشگاه جردن-هیر
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
آرژانتین در
۱۰
دیدار اخیر خود،
هشت
برد و
یک
تساوی کسب کرده و در
یک
بازی شکست خورده است.
✅
ایسلند در
۱۰
دیدار اخیر خود،
دو
برد و
سه
تساوی کسب کرده و در
پنج
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر آرژانتین
۲
.
۶
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر ایسلند
۳
.
۵
گل در هر بازی بوده است.
🧠
وقتی نتیجه از تصمیم مهم‌تر شد، تفریح تمام شده است.
👍
ورود به سایت با فیلترشکن
R19
🅰
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🤖
ورود به ربات تلگرام ‌بت‌فوروارد
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/77314" target="_blank">📅 09:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77313">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-jqy_AvzKm-oqe9Z9RYt6wYT81mInYWq8VTGyQI1nZs59K-d6zWK0ddOw6Ycj4oqI0GU65jRMgl6SNAWyaIQHJxsUj270yBQfC0ZEnlCtNIo4bK4sDht2hz3KJAagCz6lu-tCgryD957LEMNUQvMbtyItwotz_PKvpoqT7TlQI-O6lcMxKMGJEjzXgRnUVLxCc0z9Jhkfo5UFYqh1v8IqDv_r54_a8dWJ4BmlCakH2qDp9-5omr3eifEVYd_5_3dyQTy_kspRwQFy8Q-2DndBNLgVb9ZNynzJQ5sni2Lx9sZD4YFxO9eNWE6jPWARcJ3AbO4Qv16gmreMn_vacPMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کصخل این که ایتالیاس
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77313" target="_blank">📅 09:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77311">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اعزام لشکر  82 هوابرد معروف به شیطان آمریکا به اسرائیل
لشکر ۸۲ هوابرد ارتش ایالات متحده در اوایل آوریل به طور مخفیانه به اسرائیل اعزام شدند، به عنوان بخشی از برنامه‌ریزی مشترک اضطراری بین اسرائیل و ایالات متحده که از فوریه تکمیل شده است، برای تصرف جزیره خارگ تحت کنترل ایران در خلیج فارس و ایجاد قلمروی ساحلی در داخل ایران، طبق دستوری که کن کلیپنشتاین دیده است.
این دستور که در ۷ آوریل ۲۰۲۶ صادر شده، به چتربازان از گردان دوم، هنگ ۵۰۱ پیاده‌نظام، لشکر ۸۲ هوابرد - گردان معروف «جرونیمو!» - دستور داده است که به طور «ماموریت موقت» به اسرائیل اعزام شوند، در حرکتی که پیش از این توسط پنتاگون گزارش نشده بود. وقتی درباره تعداد نیروهای اعزام شده به اسرائیل و مأموریت آنها سؤال شد، پنتاگون سوالات را به فرماندهی مرکزی ایالات متحده (سنتکام) ارجاع داد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/77311" target="_blank">📅 01:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77308">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArwnO61HUio5WnV3-tRFxebeENEYAuoPnfGJ5noxITuA1vUZfvmFAfZWRYKeBDw0BDYLxrIWFMRaw0YlJJl5EVuiAJYdA7Yva5i2a8-R0bttl6IMXjUEaTGqEPKbA-nhOWMh4Kevdh-BUyZVs7hGjxp1tZJ197TtsWjOZK4Pm3nNKAUU6HxociKkhfu4elOxTXEN4RS8bwGXcD4hgT9e2-qHE62hdIL-huJWaQzOd7w6R5sCAbPnhatWUxSmrqD-yEtYAnU2i0EqO3ikRXd8gL2gZIBrGkp7DXnTMG8S7Bag_kddBHgqzb2P9LAVxTdMUvv_74MkBcNRXD4gY5z_aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">والا خواستم یچی بنویسم یادم افتاد چمن و مهدی میرن گونی خودتون تو کامنتا جواب مناسبو بدید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/77308" target="_blank">📅 01:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77307">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ به آکسیوس:
ایران به شدت خواهان توافق است و ممکن است به زودی توافقی امضا شود.
این توافق مانع از دستیابی ایران به سلاح هسته‌ای و توقف غنی‌سازی خواهد شد.
این یک توافق فوق‌العاده است.
ما همه چیزهایی را که می‌خواستیم به دست خواهیم آورد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/77307" target="_blank">📅 00:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77305">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">یک مقام خیلی مطلع و بلند پایه ایرانی به الجزیره:
آمریکا مدام پیش‌نویس تفاهم و خواسته‌ها و شروط خود را تغییر می‌دهد و این باعث سردرگمی و عدم پیشرفت مذاکرات تا اینجای کار شده.
بدون آزادسازی پول‌ها و رفع تحریم هیچ توافقی انجام نمی‌دهیم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/77305" target="_blank">📅 00:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77304">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یک مقام آمریکایی به آکسیوس:
نتانیاهو برای بقای سیاسی خود در اسرائیل نیاز دارد که جنگ ایران ادامه یابد، و ترامپ برای بقای سیاسی خود در آمریکا نیاز دارد که جنگ ایران هر چه سریعتر پایان یابد.
این تضاد منافع پیش‌بینی آینده را بسیار سخت کرده است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/77304" target="_blank">📅 23:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77303">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اردوغان خوشحال شد
سپاه به مقر تجزیه‌طلبان کردستان حمله موشکی کرده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/77303" target="_blank">📅 23:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77302">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5f6-CHivmw7IUZTkWtjGd3WYQyacQn47owwJQy5JFeufb3fo6of9BTaeOlT48DLkkV1-0izjC1rzb-kOfyPtp6bIWTGM7qUAJeQgx6BB82zbAlCgKCunt6Z4qyXRmQDhRZVdld_Z4CcYQVKv8K9a7f5DnHiYQ2BJjKnpCp-LsYepPHSfwAfX7mF6x9rhzt3bs-A__Loo4Xya4DTySxqRXCr0ZQrEwyuiS8AErzouzdSxMM6pTd5f2BoYiEQ3kmeuPwEXxwB4zAJcKyuNeoU-XQdBSqq83BBgfqIj0Zf6ipnSzb8pcPAsYYspNXgNi5qG-qz3lQ3UwyKKP0qlsaEXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان هر چنلیو دیدید که اینطوری میخواستن خودشونو مردمی جلوه بدن و بگن ما پشت مردمیم
باور نکنید، اینا مهره ی نظامن و هدفشون اینه تفرقه بندازن!
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/77302" target="_blank">📅 23:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77301">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">تنها جنبشی که از نظر علی خدابیامرز درست بود جنبش سبز بود
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77301" target="_blank">📅 22:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77300">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">یادتون باشه که تمام جنبش های مردمی سالهای گذشته هم راستا و مکمل هم هستند
اگه کسی خواست این جنبش ها رو در مقابل هم قرار بده بدونید که به هیچ وجه طرف مردم نیست
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77300" target="_blank">📅 22:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77299">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0pDo8m01_r7I8yFIwfxwbM_4_su_haSJ_N1B_van9Vl5qyMqrsMV4TBhnzxXKINZ_PqmEhCmnRQFbbeqo-hNaGCCQ2pLtdWCFmz1fnZVmVM_slfVrVoSKm8iLwFb3FTcOh5e-ZU0UZjceC9WlbsZdb_kJySphSCVSuT3q7wehC8M0bPZRkRYnJaeYz34623BS7Wl_uQkrVqfGt_o_rDXFCD5j4rAJf7HWw-Jhri9j2t56RkyOk1ecoicL80Y2RLkyXFDWLhDEq_Udt-R4KGPn4YqORSAVmWF4_lbQTzC33mnGRzCglS-tVR7mJ_t8YaXaJS-kpKYT3lzsRlYgp39g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیل اینکه که گفتم جنبش زن زندگی آزادی درحال‌حاضر مورد استفاده ی اصلاح طلب‌ها و امثال فردوسی پوره، یچیز مثل همین اکانته
🎒
و طرفدار وطن پرستی با بیو "زن زندگی آزادی"
که همون قضیه ی ملا به ماتحته‌
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/77299" target="_blank">📅 22:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77298">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">شهید واقعی زیاد دادیم سر جنگ عراق
که اتفاقاً اونا هم جاوید نامن و جاویدنام باقی میمونن
حالا عراق کی بود؟ دشمن ایران
۵۷، برنامه های انقلابی از کجا پخش میشد؟
رادیو تلویزیون حزب بعث عراق با مجوز مستقیم.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77298" target="_blank">📅 21:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77297">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">رادیو ارتش اسرائیل:  ارتش اسرائیل قرار بود در ساعات آینده حمله‌ای بزرگ به ایران انجام دهد که شامل ده‌ها جنگنده نیروی هوایی بود که آماده برخاستن و هدف قرار دادن اهدافی در سراسر ایران بودند. این حمله گسترده با فشار ترامپ لغو شد.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/77297" target="_blank">📅 20:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77296">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ به کانال ۱۲ اسرائیل: به نتانیاهو گفتم اگر جنگی تمام‌عیار علیه ایران آغاز کند، او را تنها خواهم گذاشت
من دیشب از نتانیاهو خواستم که به حملات ایران پاسخ ندهد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/77296" target="_blank">📅 20:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77295">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پدافندا بیدار باشید باز ترامپ داره می‌ره بخوابه:
یک مقام ارشد امنیتی اسرائیل به کانال ۱۴ گفت که بازگشت به درگیری شدید با ایران ظرف زمان کوتاهی تقریبا قطعی است، احتمالاً در روزهای آینده.
هشدار بالا در هر دو جبهه دفاعی و تهاجمی تا اطلاع ثانوی حفظ می‌شود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77295" target="_blank">📅 20:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77294">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">می‌نویسم امضا می‌کنم آمریکا برف امسال رو نمی‌بینه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77294" target="_blank">📅 20:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77293">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPo2N384w3di4Ow7lytoVBTkmQMpMIK5dmCHsccCvXYQUTDI7YpiH-4PfJt9Kbf9e6UAG6iICuO2bAd-2tgbFiN_D815GChymqs2uT_HnFXzj4ZQ-eCBLs2FjtmO1selcWq3aNap3mL5T4MWNV43tl6c2r3NRvUrXcGo94gMu5zKrhLGSvbDE0fbmvXHRx3aVOUGpplqwnyFofSdkwrzRSiWHkItZUE7DfnRC0kF6HzyOMVuakfXL0DX1Qu03rmVNwAM4Kp_zQ4b9kbi67bDAAVRkc_lUoIj9UjcA_Y0aBVovuBwvYujwAIry0Aacb2tOG4u4bbYJ4MINuPp295l7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان عجیب پروفسور بقائی، سخنگوی وزارت خارجه:
تحقیر نهایی آن‌ها زمانی فرا می‌رسد که درمی‌یابند سلاحی که برای تسلط بر دیگران ساخته‌اند، از بند رها شده و اکنون اراده‌ای مستقل دارد.
در آن بیداری تلخ، فقر واقعی قدرت آن‌ها نهفته است — و آغاز سقوط اجتناب‌ناپذیرشان...
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77293" target="_blank">📅 20:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77292">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">رادیو ارتش اسرائیل:
ارتش اسرائیل قرار بود در ساعات آینده حمله‌ای بزرگ به ایران انجام دهد که شامل ده‌ها جنگنده نیروی هوایی بود که آماده برخاستن و هدف قرار دادن اهدافی در سراسر ایران بودند.
این حمله گسترده با فشار ترامپ لغو شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77292" target="_blank">📅 19:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77291">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامپ:
حاجی نمی‌خوام چیز کنما ولی انگار یه احساسی درونم داره می‌گه ایالات متحده و ایران به توافقی نزدیک می‌شوند که راه را برای مذاکرات بلندمدت هموار می‌کند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77291" target="_blank">📅 19:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77290">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1AeoQN_O8g8TD9AJLKvXSZIe4wUocZdney_2TDstV0YZ9TB5OTQ96_QkZizk_AC8u1bYBqvK6ewi2m5xm5KtBAm1mwb5uMpy1aK2HyqJHrJ1hmKcdtgV0aKychX2KzhT9vPcDt0QGf2qvqtyUQ6oMuT8qoFzViTlgrbQJiG7Dox_EzDga5ZUroXJq5I_2B5gdp2_DsmzT6NuBkrsmAk-Fcijw0-tdcsTE01NwUu2oegd8qtJascMTEUpxh1zREUSTmPGmQkRxs4xFPYvb_aVEXiZg0k0I1m5jG0wmg_UsuvOxYt-e6alHuMGvnMPAm7kZlLkY-GuL3cMgRNOXcX-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77290" target="_blank">📅 18:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77289">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">انگلیس از شهروندان خودش خواست به اسرائیل سفر نکنن
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77289" target="_blank">📅 17:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77288">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JpuG8h9eK-VGKfvMKN-lOWnBZjZzY55HKFlasEYV8yoq18GhxdZWdGJP7aMoXslfBvDFRuuhBZeb4kkP47mpiXQSQf8UKAooeUDK_4uu-YPhnxfoDWwy_vtlJ8QBM84AO3r_fCxGwLfvqiFSWKWbCUqPligETDmc4gD4ctfG39LCxzui4pgZPLTwie5Pn3s5fEIbLBRv1eTtuELlNW1lgTo11wCiiLlJNAeg4pBQfqv1hFYGty2Ej6bvoG6S9zjebiYaHh9vgCsh-JYVflCMpDJJtnS-FJFTlo7b-YiKzT6w8Qg-acfY3kainEEkMV9s9hO0-6nYSN-ZvDbfKl75_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنوب لبنان
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77288" target="_blank">📅 17:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77286">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IvJjrtygszKCKXPjbaGmIUMZFEeqMCSRBI4sC1f_IWeL7iZ6jPMfS1xdgQutaWN-mN3wVCEXqGPwswCnT4nUHboJJBc2TeXb_cRZDLiH_9STUVEfNEufLiGntUrDKTaqVlN1dYnwwUrOfCezGsviAeRyluI90sjGRgvGPgWsX-_Rtt43hM-hyt_2qVgAaljFFZjqLHjLSBuCShOuVl6ViQN956zLHqzeQwwB7npCI5mt1i05Q8lPp6A8dl1F3vYe6cvQAFivkTa-58EaqKv_tK0cJp5mtTGR296CecslrCEND6CsBGVUaBJEumjBYHp1AApdX2WLuZeC_X8QDhxc4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u6SxIkUzWVD1orFHg2bw8LES6NBUOuVQavYKD93nBG_jo6Eh8PxZpmJsmxuagoMTlgGi3eeZMNXcjJ8BNVitrmxrDUGzp57iApyAcT3nkt9-gS8lUnSWbOzqOQlLQH4jI878JcrAl3Mihaeh83Gi0d78G9RYXrd3sUlNRruUTKX16HXCOElCuLlLtRRFV4i-l1wvjBNiMHcrHStqh6LXF9SqW8YbFTeCmrJFlJYzjGaa8mrOD3CvwJM_pvfHRVrTS3BOoXM03GK-o_9eiv8cSyLeiiueUPnXh6LcFILwZ0DRYfi9_yxA8bCCZd4kFcFv2YG5MbMobNEpVsMDCU3wbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نعمتی که از دیدنش 10 سال محروم بودیم
🫠
🥲
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77286" target="_blank">📅 17:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77285">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app.apk</div>
  <div class="tg-doc-extra">51.3 MB</div>
</div>
<a href="https://t.me/funhiphop/77285" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📱
اپلیکیشن اندروید بدون فیلتر لنز بت
🔹
ثبت نام آسان و سریع
✔️
🔹
نصب و راه اندازی تنها با چند کلیک
🖥
🔹
اپیکیشن را روی موبایل اندروید خود نصب کنید و بدون نیاز به vpn وارد سایت شوید
💬</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/77285" target="_blank">📅 17:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77284">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/P0f0J-b92onPRqym5cjehJM6utkEXMNyhIJlJVId2MKk1VQJyIgE4pHV7PHIviAaatE0HwVrg80BVw4B492xM45wkuMMmGFKXw-zly6YReuu_sICcaU1wa5RBdXgVGAaTXpXNch4ZXADlZ-t-QgEIMAav-xIWPWit-u2jXUOFs1XtEVWxvpm8iQXElHuO8lNZILtdg1B3vcV86GEU09Op6DwHLmthGLwQeFdgJbfs9pfhSsSzGetenbGvlHnkWXdY4dvaFkZhfDRtHjRyCkWBGhqk0R-Fq9pJcwvQsqcCwpiCAsn8qJeLJNr0CL36C9aiDhmulou-KWHFE7dgbpbcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎊
با لنزبت، دنیای واقعی پیش‌بینی رو تجربه کن!
💳
شارژ فوری با کارت بانکی و درگاه امن VIP
💰
برداشت لحظه‌ای تا سقف 10,000 دلار
💯
بونوس
🔣
0️⃣
0️⃣
1️⃣
برای هر واریز
🎁
جوایز هفتگی مخصوص کاربران فعال
💵
پشتیبانی از تمام رمز‌ارزها برای شارژ و برداشت
🪩
امنیت جهانی و بیمه شرط برای حرفه‌ای‌ها
🔤
🔤
🔤
🔤
🔤
🔤
🔤
G18
🅰
📱
http://Lenzbet.cloud
📱
https://t.me/lenzbet_official
📱
https://instagram.com/lenzbet_official</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77284" target="_blank">📅 17:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77283">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aR9WAFAk9KTkr8vkXhOTcYQMgzzqCtuI78f_Y58edwukBxLaRgFklneJLrZUmWrqT6zLmcVGGDNcY-iuBaVd0mIYBcJ-rySIhAksA2AVoboSThcnz6tqIqTZ9Q7WOwhg6Ty5AntahU9LopOupwH90xcMMg96U3k3NVPYmgftd0zEsUwVoHiUQ1sMz0gVEMNJY_-ib6bgHrI8_C102OD6wrU5dgA09J4QVYOCAAARAsg6vbrJf_Z-C29EJp3ZA5psH6eG4oBh3T_hDZaIhirI4QDr_e_XcW_5aGwfGnUTSO5Oadgxe3_TqVYHwVOqUA9yCtJJcO822xwvsvxvsEX4Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قصدم این بود برخط باشم، دستم خورد رو زبان ترکی تازالیخدا بیردایمیش شدم
@FunHipHip
| Constantine</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77283" target="_blank">📅 16:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77282">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1pDmiVlhRC3hsKpWerByZRTAAlGcrunPb1I1gGuWxeHxm5e7D6nXa0Dp8gS0w0Ew7-rmmDGhBIDgKT2sbjG_oeXBfpAutFhKFEMLUe9FVAjdjx1Nwmcf2l4mZA1A8UyOXDTfBw8ShRC8HigOYLCUuMUHJ6sGCgOTVaw_xRqsPVLRibDzkNdDmp2-1zzRaKz4zRTkiNdGv_KmmGCzODknCqCdPyMby9T5AJdoVdY2UGeaF0W1UG-3zMfnhurO03svCdvbrSJJrp0ieU7hTcGey3N32tL3Zm7rUAelbkLZOX4ztmfo82jXviDpPr6AMFQHf0m1UxPS3hkiYV0l4b50Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استهلاک کمرم هزینه بردار بود
آب هدر می‌رفت چون بعدش باید دستمو میشستم و از مایع استفاده میکردم
هزینه ی عمل دیسک + ۱۵۰ میلیونه
و برا همین خم نشدم که بردارمش
فروپاشی اقتصاد ایران به روایت فان هیپ هاپ.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77282" target="_blank">📅 16:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77281">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بچه هایی که خارج از ایرانید شبا که گرمتون میشه پاهاتونو از پتو ندید بیرون چون ممکنه ی موجودی به نام سروش ولی زاده برای اینکه خنکتون کنه بیاد پاهاتونو بخوره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77281" target="_blank">📅 16:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77280">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s40UAhPdU3-Nc97DBenZHhKEXLQfC8TbTkX3PLwOn-TAKe3mrr5U4Cl5B4mFkHPBPUyeRqEerwKBbsONw-RBIrDxKh1WFml1j2bfqK5PXjOUrMFu1MnsypoeaXnB_KGjavHYsyqwB-gyPcBUG3Cy-HlRnlDr9ISWwIbyauwNVzQX1Yi-3YrGa0tVL2WFWSELDTzWvsHeFKkHmu_9sSqXRScW5kbhSN5FHY3PHVTTc1IT4FZgfI8MQkq1ZAs4yhyQ4bs2nCD_UfE9EJllEqj741enMXjXFTB1b2hMpEjOvtYJdjoErDPABIh1zvCESqzoxHWAkc9ESVAz1O9y8sM9Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان حاجی پاکستان
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77280" target="_blank">📅 16:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77279">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">الان ملت چجوری به کانفیگ فروشا توضیح بدن مودی نیستن شرایط و تغییر میکنه فقط</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77279" target="_blank">📅 16:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77278">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a41_DhtHmntamXfsYeSCu3tOrrt6W-T4tq1J_vBYVtrh0KXuRpG4VUNl8GmBWtY5MDl7tnu0HdQ4TB2JA0b_C5PWWUpPPhvKkDAjAgr5pqGMuVjX7SzHaoKhe1Zc8eDLMwM3twLrlbqDgTcjk6JTs8xaHAMAupe6dqsZdzwEX1WXhs5uxcwwJdYpeNJbzDR9fD5OJfnJjV6jqAZ9l5CCM6ZOHElvROHvCQo-Q7pfIgnz-u6y2x-MXdYT2_4FdAqHhORsER9Ovkvey10wqavMu7AOEsJ0k7pO5235uZqW9pMNzDPlH3qeJxsYps5Fvu9AOsE-q5Tb5Z_79GjPvm9UAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید کوروش به اسم
تهران 2585
ریلیز شد.
YouTube
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77278" target="_blank">📅 15:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77276">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اسرائیل
⬅️
لبنان
ایران
⬅️
اسرائیل
ایران
➡️
اسرائیل
ایران
⬅️
اسرائیل
فردا از اول بخون همینو
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77276" target="_blank">📅 15:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77275">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9scdoydn7XkgQtEgZqL5GDjb-sBoeveqHZWRbjSUecbaWeYFUMdIHi89NMOTYVHv9KBGO9erOUdOgMRTIZaeZD21aKkiIOunjM2cTKj4FXGGHNI3hS_erMhsx31YOHgPSBrmyrMafy2QHakEy4QWVwACxCOD_jePQUCQnRbBFFFMQ0xvXG9VSFR3OHr4tOjXTfnBoPBG5KjM_c6FksV7mtKgrmVZNJgKA1OkWqwKjUu0wwXm-_bPXtb4clSmnGsPlOWIQo76HCa8Viztf46foS7bf_W8b2xLsfLRreNvhoJDjzPO39L3Uyr6UeWyqM8UM7Q6ugvkhPB2OgvqorcVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرارگاه خاتم الانبیا: از این به بعد درصورت هرگونه حمله اسرائیل به لبنان (حتی اگه به بیروت نزنه)، ما خودمون موشک می‌زنیم تو اسرائیل.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77275" target="_blank">📅 15:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77274">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKfm6O5ZnIGg4WbYqj2PGw6J34EilEO2vcEx5LAzMRJXst0ezzkOwOo-qFNE2UNqFyhgxUInaDdPCdl37IgjA8Vc3JXr_C3e7I6fxYrMRcgQnLG1yGFZj_FgvdgWZomHKy5zTh7VXtgGVATQ7DnWrzfkzZNtrBVHDyfjNNPMTGteyYHpfQG0gAh9sK63pttr9sN8lQXiyFYuwoSQfqw3fGGhW11-Ljcnwi7pnBL5sosq85cBs92BmXQQtMYNOfRBWvq-Xu6szduL1stHwN2HEgct7MNOGPv6WvH9lXCnYP1PJ1oLNn4hIlHyzEVWhflKWSxF6r-eaNNC3BgpfRloQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرزیدنت پزشکیان:
اولویت ما امنیت ملی و آرامش مردم‌مان است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77274" target="_blank">📅 15:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77273">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">قرارگاه خاتم‌الانبیا: فعلا عملیات متوقف میشه اما به جان مادرم اسرائیل دوباره بلند پروازی کنه یدونه موشک میزنم.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77273" target="_blank">📅 15:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77272">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اسرائیل هیوم:
اسرائیل و ایالات متحده پیامی به ایران ارسال کرده‌اند که نشان می‌دهد اگر ایران از شلیک مجدد خودداری کند، حملات بیشتری صورت نخواهد گرفت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77272" target="_blank">📅 15:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77271">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ولی واقعا جواب دندون شکنی به یهودیا دادیم، بخصوص اون بخشش که مقر پلانکتون تو بیکنی باتم و خونه خانواده سندی تو جنگل رو زدیم.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77271" target="_blank">📅 15:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77269">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ولی واقعا جواب دندون شکنی به یهودیا دادیم، بخصوص اون بخشش که مقر پلانکتون تو بیکنی باتم و خونه خانواده سندی تو جنگل رو زدیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77269" target="_blank">📅 15:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77268">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">من کسخل‌تر شدم یا پزشکیان واقعا داره چهره ی محبوب جمهوری اسلامی از دید عوام میشه؟
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77268" target="_blank">📅 15:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77267">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">میگن پیت هگزت به مناسبت این جنگ نصف روزه ۵۰ تا شنا سوئدی رفته
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77267" target="_blank">📅 15:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77266">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">قرارگاه خاتم‌الانبیا: فعلا عملیات متوقف میشه اما به جان مادرم اسرائیل دوباره بلند پروازی کنه یدونه موشک میزنم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/77266" target="_blank">📅 14:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77265">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">معاونت ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور:  نگران نباشید نتو قطع نمیکنیم  @Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/77265" target="_blank">📅 14:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77264">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">معاونت ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور:
نگران نباشید نتو قطع نمیکنیم
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/77264" target="_blank">📅 14:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77263">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqusHouwEra3FjZDIXzDb-Y78N257cKa6_SJggwSPyPqj5AYafW-MN2wX_FjgfMWijS0P1yhrJdNDCAMvepav3ujmSQgvWxnAYCK_0GQz14mZu7Td1axfxqMolI78XL2vy_ghhQd37ixKioRyDRjaQJhppStmYmBm1xywG0TzW7xQL5yf5_4h993eULfE4RstMBu7mIkEqFApZpLxPxgpkkGi9DFPG9Edc-3tVTQTTD5hy5rtMdGYgZzielt-B_gZ5yIOuvJ0JqHHyWW7yOZztbZVvQ-LB_2efmcakIEw5P9oHPRolr-91U3qSODH7HxbNQJDW7VOTmkIkSpDawanQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:‌ هر دو طرف، اسرائیل و ایران، به دنبال آتش‌بس فوری هستند! مذاکرات نهایی درباره «صلح» در جریان است، مشروط بر اینکه نادانی یا حماقت مانع آن نشود. محاصره تا رسیدن به «توافق نهایی» برقرار و به طور کامل اجرا خواهد شد. امور باید به سرعت پیش برود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77263" target="_blank">📅 14:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77262">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">منتظرم جنگ امروز تموم شه بتونم بگم این جنگ عین کاگان بود، کوتاه و کصشر
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77262" target="_blank">📅 14:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77260">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVMaUGmTICYJkx0OKG3zjjg1jEDp5EygVtcWQ6fZltPObDDq14clddni8qzzV9fnX962s4V6PeMcl-wAKCsh1gvcadTks_wN73ti59VayIJOelIwkCYg5pCvsLmkNax7cCRrn2P0g2jv6TG2Vn3_LfhWNJ5B5Ugo6I4A3IeM2HwjZJTlQCLo8s_Ejw8IB2pNv5oyDAJdsaxMCmdxWgRppWhHsf1DkQeemrN1jjpfUEIflvYjfVKZzR8BkWgs8By4e58-vAwpgnF43zEAL3XOUiQn7fVzvRhndfpu-tKv5N0f03e0CJ5lXUEpNi3C9vUrX1FB2CuJUjGBGyQwzZ1KSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرا امروز خداست
😂
شهربانو و الهه منصوریان چون الهه تو مسابقات انتخابی تیم ملی باخته حمله کردن به خانه ووشو و الهه منصوریان با چاقو میوه خوری خودزنی کرده
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77260" target="_blank">📅 13:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77259">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">آموزش پرورش :
جنگ تموم نشه نهاییو مجازی میگیریم
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77259" target="_blank">📅 13:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77257">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sXOQv6YrhfrLcLrO1IuSLd_WL4S--9jKjMKAquxUVXNP50ceiewlvAepdJF5cD8trPiYDGOI9XKwgXDyGTQw5vIz8yp3OwOQB6Ds-bMUIPACLuBHKdjXZJg6Fialm7fXyK1IkUCjAWx0UcgF0t8AYXCb3jVsXOsd7ifjN6xFubVPfew3v5HSmKAqY_sbd2U-zUdhsf1d-A7qBjUFYtTtEeuNcGfF8D51AICQ0EVhRlQRXV5TAsTGTEN_jJRgD02cJwBsHTBx4OCeDS08Sm3Xno7HWJM4OCpRyahFcv6MTVyI2ReAoAUYIAOD1U-FF0_W6r6OeyXsVhdtNVx68FO16w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fS5Kwy2JCCm1p3tpDE7VNz15b98vapxQa8C3ik22D1PxX8xib5ZwoZ8oW77glC6rJZzcAuCpal0A6f4XYxfkwIcySJXkqxTpryoxcaNjpUWConrelkUsHIeJuZPHFoZm5EqIWdzjr2P2qR5BqT_OAr3EmMkaxxg8f1qWcdFhlrRt0xNJhpHN5zoMs66mxD6q_A0SpnbcUEvonOsnIza4Xg-Y8BXDwLG_Nq-Mvc3Errg_XaHOb1JAw1MhdPiIQKxnc6MssKBfcB0Cv8Gq2UdxJC1uh178ATUXiLLhU06Ih6hF1LjS6hfsb5PhmntqpohuMb82Fe0wevNrTUfqeNvekw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دارن فضای جق زدن هم تو اپلیکیشن های ایرانی براتون میسازن دیگه چی میخوایید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/77257" target="_blank">📅 13:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77254">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">خاتم الانبیاء :
زدیم دهنشونو گاییدیم اگه باز بزنن میزنیم
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77254" target="_blank">📅 13:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77253">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اگه میخواید بفهمید کی ترور شده کافیه ببینید تسنیم میخواد از طرف کی بیانیه منتشر کنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77253" target="_blank">📅 13:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77252">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Gashtam Shab</div>
  <div class="tg-doc-extra">Alireza Roozegar</div>
</div>
<a href="https://t.me/funhiphop/77252" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آهنگ مناسبتی برا کانفیگ فروشا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77252" target="_blank">📅 13:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77251">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اینکه نتارو قطع نکردن مشکوکه، میترسم بیان گوشیامونو بگیرن ایندفه
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77251" target="_blank">📅 13:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77250">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترامپ :
ایران و اسرائیل باید هرچه سریعتر جلوی شلیک رو بگیرن
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77250" target="_blank">📅 13:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77249">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e98d055a5.mp4?token=HeCTEcai91LHtOsGMPS1miT2Tm7J3hQrlBRcoJqiJzyv3nzavt8e3SO04bvZzwGvJIJzFcZxs51XYxITi11F5kEcXCuhKDq56X1w-CKxEZy2GRi97sgSDBBTBR-bkCPRD15J_TJaQsdhtEUabVRpBZT_VWuS6kXD-7Grbe7_hcMRU3lbb168-XvBSbPnKpkeRdZd6GNzsyhz6ahMqaq7lNrLNcIP-KrL_b3Gs6t87fbb_tzKlBNXb9RyZ5JXyzLrjgQEnLPQme3rJttJksHdgXgz-XaqXxGOhtKR8KoonefuuaoZlyT5QHvAwS-qeYe4Fi-qJ5dgljFeqyi6c_yNvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e98d055a5.mp4?token=HeCTEcai91LHtOsGMPS1miT2Tm7J3hQrlBRcoJqiJzyv3nzavt8e3SO04bvZzwGvJIJzFcZxs51XYxITi11F5kEcXCuhKDq56X1w-CKxEZy2GRi97sgSDBBTBR-bkCPRD15J_TJaQsdhtEUabVRpBZT_VWuS6kXD-7Grbe7_hcMRU3lbb168-XvBSbPnKpkeRdZd6GNzsyhz6ahMqaq7lNrLNcIP-KrL_b3Gs6t87fbb_tzKlBNXb9RyZ5JXyzLrjgQEnLPQme3rJttJksHdgXgz-XaqXxGOhtKR8KoonefuuaoZlyT5QHvAwS-qeYe4Fi-qJ5dgljFeqyi6c_yNvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو دوربین مداربسته از حمله خواهران منصوریان به دفتر ووشو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77249" target="_blank">📅 13:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77248">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ بیداره و واکنشی نشون نداده فعلا به ایران و اسرائیل
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77248" target="_blank">📅 13:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77246">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">رسانه های اسرائیلی خبر از ترور سردار سپاه، احمد وحیدی میدن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77246" target="_blank">📅 12:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77245">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">رسانه i24 news:
ارتش اسرائیل تصمیم گرفته عملیات «غرش شیران» رو از همون جایی که متوقف شده بود ادامه بده، به‌جای اینکه عملیات جدیدی رو آغاز کنه. ارتش این رو روز ۴۲ عملیات «غرش شیران» محسوب می‌کنه، اونم بعد از یه وقفه بیش از دوماهه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77245" target="_blank">📅 12:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77242">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dqDr4Rvm4j8TOWUfXyRGjbxX_t1LVEUhkIIKtHmiDXerkN2r8mBju0KDH3xOA8ijG6w7mkdeokM-H4Xi9rXoeu2US-kfp7a60ftfGD7yo1ZP9PeXb-tdLz63x5oofL2NQWRm_EEF_wwvNNnNQfk2RXI8F06H9tXcMkD596VJxfSOKVnmm0RtFRsHAnI52UjTZxn9Ajkffq25ikFUikVT--sulZI2ZzkEaQZneh_oX8PFGnDZ00WU6wvXAil25d3Vv6A4dowCURtXVdyCRIgtzZXDMYIQ1wq1sDO5S33XBhab7dtAH_LXYXjNSQFOVP9_FQKdkluQ9aJpvCFgBc8IjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/inaSsMgkuHpezb2HKrRnkFMic6BAa_oef1CyxwfqdDfpLBOsuLubjF5CeZjG36I6Ux_WwiC3a9RB6034Xcdx3wWAEqDK8S7frcenT_xh1T4Jr72Lw5XAJHlI_h1E5_YqedqElNXvwqL0Uvb24M_kDMtLbHnm_8h9_VaCavIKNvzTH2uwshI3xXHTuDzAMCLKSWSm6DLR-yVuJXNXFCJniu40xFiigcFnmfwDuYPdKoIqogZdZ0t9ENl7jlQYL59wtgC5GRldDr_cWRHCQTP9qT7xkMoNOY4FUviC30EuVR9YFVeqnIaCeIgD_dG-1Ii2YQn5y1LpFQgHEMp_6Ie22g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TKDQo5h995pAShke3Rng8rkUJ_ibQZnZ_-YX7EtgRBvrlOPTMZ6qhGXsyCGxRh7c8dpGpk-EJQQE_Yxw7B2DUUeLNB3ry2Uv_PbjJlLTw2j_Bujw1lIC_5hnbD5jm1nDQFIAJeINu4djb8nk7Xas9SA-BRrRJugx2vxSc84pfAnxp1HlR5I7GXWJRtDqlSALQT3b3Rdk8vuk9zY2_stke3CkuYjrBg5HYOvetj0Nlxot6kzj48cxNQFXJBViEHnafl-aiwFG2fnlNUpxv878BiMpj2x4P8bcLSB3cNPOP-E0IFH2fRw-efewYIR-f4Z48Kwc9sBOeA5t8BPMPsw4gg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این وسط که اسرائیل داشت ایرانو میزدن، خواهران منصوریان فرصت رو غنیمت شمردن و اتک زدن به دفتر ووشو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77242" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77241">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">رادیو ارتش اسرائیل:
ارتش اسرائیل برای حداقل چند روز درگیری با ایران و احتمال یک کمپین طولانی‌مدت آماده می‌شود.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77241" target="_blank">📅 12:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77240">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سازمان ملل:
we are nigga run
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77240" target="_blank">📅 12:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77239">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پارکینگ های زیر سطحی به عنوان پناهگاه برای شهروندان تهرانی در صورت تشدید تنش ها در دسترس قرار خواهد گرفت.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77239" target="_blank">📅 12:26 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

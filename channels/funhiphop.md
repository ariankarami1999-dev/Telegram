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
<img src="https://cdn4.telesco.pe/file/OFbmYhHh9HamxCIBwieuc4OvK-9MRtbaT8u24o0sLXBZeVl7fcFAkxbY-lZHLVti4kQ_6SLRhm1fNk5F9jezHTsPU71KDoisVP3guItdxZ_2gsnJwhPA9cmGQsVRVuNBV6sU1FC4AtmxlKMl2oDABqY4NJgxo4DwWLKwu-af3n6fyaDTodNabZodYMoGID_ixeTdToyO5_UPhD5sQ2TpMWrEDnS0UUHpDNJaIKyCa_VoDhvyZuiFB8bONn5XC6JI-TH7Gik4N9SRPiGOedbGoNRpq-XAI9tW-pjuDizTadMgtxXAiR7pfF-Mda039x3WLxGG4m6uMnBSuw2mR_RJ6Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 174K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 22:38:20</div>
<hr>

<div class="tg-post" id="msg-77100">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">علی داره تهدید میکنه که یا دوباره ادمینم میکنید یا جنگ شد وصلتون نمیکنم</div>
<div class="tg-footer">👁️ 17 · <a href="https://t.me/funhiphop/77100" target="_blank">📅 22:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77097">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">خارکصده بدو بیا بگو اینم نقض آتش بس نیست  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/funhiphop/77097" target="_blank">📅 22:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77096">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">خارکصده بدو بیا بگو اینم نقض آتش بس نیست
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/funhiphop/77096" target="_blank">📅 22:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77095">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">یک مقام ارشد اسرائیلی چند لحظه پیش به رادیو ارتش اسرائیل گفت که پرتاب‌ها به سمت خاک اسرائیل از ایران به معنای «اعلام از سرگیری جنگ» است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/funhiphop/77095" target="_blank">📅 22:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77094">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ریدمممم</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/funhiphop/77094" target="_blank">📅 22:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77093">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">حملات موشکی جمهوری اسلامی به اسرائیل شروع شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/funhiphop/77093" target="_blank">📅 22:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77092">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">زدن</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/funhiphop/77092" target="_blank">📅 22:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77091">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">الان کلا یک هواپیما رو آسمون ایران هست اونم بزودی تو تهران فرود میاد  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/funhiphop/77091" target="_blank">📅 22:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77090">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اختصاصی از ایران اینترنشنال:
سپاه پاسداران آماده حمله موشکی به اسرائیل است
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/funhiphop/77090" target="_blank">📅 22:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77089">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smyiPcl5keAduB8PXGJRl3G2bp1G4y9tJypzpSbRDzlg5GjUz0frHGax-K5-c_mEPLqjdLLy2LpE3HrlzJCaRyhpcDkgV-5Vu3nDJaUtgAR0RDmnR3NohGfZJh9OkBIgnxH6EAJPjONI3p2R7xKTYAgjHP9NzAv7Oj9wu3Yg04GMHtZ8mcx3qYXUtfwgORDDrJKs311rdfEuHVx5EaL627_gm4d8TwlyG32sf8ZXKyVNeLLBen3hgbEQTJohBk7NtwIWAnhc93UVw0b_mqDfuMC2seoP7co1h-vhH4nCihKiudpEiX3UT4tYjF49Ph1EgzbEej4jaZB60rYuqa1ppA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان کلا یک هواپیما رو آسمون ایران هست
اونم بزودی تو تهران فرود میاد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/funhiphop/77089" target="_blank">📅 22:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77088">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUU43TIIV4-vWh8Vv9OBpS2AVZ6wcsfPPtKSnZFRlAdHNFFRlmp6wxF4gcJeHEs-hF41Z9OkexCjCTr4jZqIaL4vOnJ8SkaJSaf6O_DbuiJFLUWmFiBoVdHoWxktEhVeIzGTb8C56l6jLvs-bZFK6qTSt1ilSnKiqa6dFmoFFK-Bb8p0c1I_ala8iiPHUmhobMshEmWg8R4eYgYSogEPvRsJKmuideZWiF-BQJQL5dwJ940httccxeYcQ09Qv7v1YZPeBHnuk7ywbhQG0a_LEhUIILb40VXqvbyQgoaG-nD2iCCMo0um6GptR2HlY68_lboNEzrUSonTRNnMC1hzZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات لو رفته از اولین خلبان ایرانی سوخو ۳۵.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/funhiphop/77088" target="_blank">📅 22:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77087">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">زنده مونده دوستان
نگران نباشید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/funhiphop/77087" target="_blank">📅 21:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77086">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کریستین اریکسن باز هم وسط بازی دچار حمله قلبی شده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/funhiphop/77086" target="_blank">📅 21:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77083">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMNZTomnPJoSOAKu0LF9a9tpvnhXcMeg4qL4481l4h8A0_gMWr6T-Vh18RCLYNNxQmKgEVUWt-sndM8V96ggCmV8cYRpvFRVtP0pqHE6vwJ-cZuq2s-1LYidswsL6A_E7TmFEx_nTzn6LBIyQn54RkSy5Aq3j4g0XZAi_pGJQO04uS92vafGb7Dw5a9UxTB6r_uVzrr1OSTm74NlDyH-opNQCblr_Eflaxob2n5geSRxiRRuyYUx2g43OC4Pqj0I0FRjCmJMlterQlr6VEpim4muhGJ-Mxs1azux1Tjd9vOOnHkyeRYzKfnllvmVACrqs9wwx8A_ymHnQCHQX9SfHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید گوچی فلیم به نام TXICLUV ریلیز شد.
🎵
SoundCloud
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/funhiphop/77083" target="_blank">📅 21:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77082">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbEHy8vjpm1FRcPzieeUzTdY3yQoSTBRe7-S-kxM01eOfy7XAE_bAEkrILwfWNYncn2Y9Uso4nR-LUD-TorGd0-x2r0o6umVd-S44rclqOJaQsJj8mf9CWngS-rr2qKaz2bujZMxNY6fAtppXW55D_0qq1rj6FapFZd07ly2M3QCHbwM5mJRIbhyELhJyl1nWba30PSrT9IgnZWvfL9S3w5QS9880eU2yEXMg-ixDmi1c8FDrqQLx3n3kfkynu8tmqMO9LFlq2UZ6YmsKhqte2mzRBmhVQkrzfpU1f5PL_gaP5YLS74BxjVp9Pj6c66evHA8WAK7EZ6x2Otsr9PwcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود کلش از صداسیما کیری شده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/funhiphop/77082" target="_blank">📅 20:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77079">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_bNqTnscjaBKBvXqsXjIy0fa34jah7YcI0A8vPIrkvmgEKYKsEebcw_7BGq6B2f8-nm9YqFmw45lJkJHpgYCCIz4w7qPOi0MHlNHtEku9qkGVEPbWpb5tsf1J8jmIY0Sk9--tYof7jHTRbJtPQ5E5ICZdepCZKgSzOmSDv4RZR7oF3f-CfVGAOu8ZG04CH9l-kHSfuj6wEi_kckLbJcTwOvQ52jJWc_Q4G5rH0mU4FKueUqspJCURPHXW3ugWee8xW5nkkeH0ciJ_buYSBHb-Vv4rPvvT4Sw-ENTx4RSAMzojv2dTbn2d_vUqZjPcCyZikd40X6TQZireC8Jh8PoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندبار افعی کردم خوشم نیومد، این سری کبرا
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/77079" target="_blank">📅 20:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77078">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">چه عکس بالا، چه این پست یک چیز رو نشون میده: مادر جندگی  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77078" target="_blank">📅 19:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77077">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pXGC_pEgkRjyUG4X83v4sdrwslMmh68miMFmPf1_Km9CHlYenvZiAbr1o_oqvwh7TqHXHC1TyKBd3-7FEYoonDDIOuBH3SiTZ0SzD4VFxWwkxDaARyaWHwX_nHJarZ0gz_FbVn91JyAijsNLqs7qGgmyGzWmz9s7IltBgBgl9yAZ31pIvqcjWdKvf0KrnsYU8WMPY0U8tjKZgjIzorRWOv7J0I3HLqqkxNYS33dKk1JDLI24KGe6JrTUkaQgKWjJ7LdV1YeDkyAl4QUmtfirJVOlKY1GGICHBqNiwiF_aV47Ou3MetiNtkPHK-tEaKwb3KcU0frRQ-Nge1j0jFORrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوزرنیم‌ها در خاطر باقی میمانند  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/77077" target="_blank">📅 18:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77076">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUa1tAPd8zLHAWed9sXTSgZwBMo-_igfBAP0UCB2TVEj0k3DMvilDk-qaKZBl6Ul4S3hKT62yFOikuYGzctiAoURk6_6k0c6p9e3FeIbU9zGFJ4hRiSZqlbA8aikxmm24wbWeAgGzBC9FezyLux4WAY3DiPFMtLK05qeRVKI4pO_iMEHdI2xYL7mN1McBPbCGawk7qdZT_TVE4QEZKgQdoaW0rKTZMvaKpKDsuG_yH7J7JlaVanjhw4QK5XYg0Us-DyqrqHyh7CqGMIl_2oFwLxig2OLjX6Doh2ldcEnU4f6hmoUVVUsi6X_T-AbhtL3mw-7nKcCccDxD5M2yExC_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوزرنیم‌ها در خاطر باقی میمانند
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77076" target="_blank">📅 18:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77075">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">مقامات ارشد اسرائیلی به چند رسانه‌ی اطلاعاتی منبع باز اسرائیلی گفته اند که احتمال بالایی برای «آتش‌ هماهنگ‌شده» بین ایران و اسرائیل در ساعات آینده وجود دارد.
(با رژیم غاصب و جنایتکار و جعلی صهیونسیتی هم هماهنگی؟؟؟)
@FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/77075" target="_blank">📅 18:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77074">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سخنگوی کمیسیون امنیت ملی و سیاست خارجی رژیم جمهوری اسلامی، ابراهیم رضایی:   ما پاسخ قاطع و دردناکی به حمله رژیم صهیونیستی به ضاحیه خواهیم داد. این سگ‌های هار باید تنبیه شوند و به جای خود بازگردانده شوند. امشب به آسمان سرزمین‌های اشغالی نگاه کنید.  @FuunHipHop…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77074" target="_blank">📅 18:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77073">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">خب مثکه باید کم کم رفع زحمت کنیم به ثوپر عاپلیکاطیون های ایرانی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/77073" target="_blank">📅 18:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77072">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سخنگوی کمیسیون امنیت ملی و سیاست خارجی رژیم جمهوری اسلامی، ابراهیم رضایی:
ما پاسخ قاطع و دردناکی به حمله رژیم صهیونیستی به ضاحیه خواهیم داد. این سگ‌های هار باید تنبیه شوند و به جای خود بازگردانده شوند.
امشب به آسمان سرزمین‌های اشغالی نگاه کنید.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/77072" target="_blank">📅 18:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77071">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ: از حملات بیشتر اسرائیل به حزب الله حمایت میکنم.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/77071" target="_blank">📅 17:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77070">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdUrrEXi7jne7zNxZikAIvD1kcU8ZC8KJfwhf56TPtEgB8oat6Fzrv2Dt6Esyi9VguhvJHz-mUbZV9MRjS61TA1_ISWRpYrt9cJaNy4YtGycccWzpxEF8T-RJKerROuwP3Mfez3xUZt3WJm_VOCXCFX7d0mRyT25orsvQzFMdvLo8cn_nzzsbMHbr6O1R37LjNEEMxROvU78m5MV4NqXkDZ4C7BLhE6qOs7Oh5PJvYgBXKj5B4HMIzSroPtYXHNcB20l9vMtmtVK5C-gBLKHq3qXaxFguKjM2O2Tp4Y5SxWDqLI9POc_9eY18VhAbmapNBmYuNuqXGlTtp0K4CCiMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیل اینکه چرا نتانیاهو اینقد قوی عمل میکنه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/77070" target="_blank">📅 17:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77069">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">رادیو ارتش اسرائیل: ترور هدفمندی انجام دادیم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/funhiphop/77069" target="_blank">📅 17:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77068">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سد مجید نقطه زن
این همه گفتید اسرائیل لبنانو دوباره بزنه مام میزنیم
وقتش رسیده پس جان عزیزات تلاویوو با آبگرمکن بزن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77068" target="_blank">📅 17:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77067">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ:
هیچ تحریمی کاهش نخواهد یافت و هیچ پولی برای جمهوری اسلامی آزاد نخواهد شد
اصراری ندارم لبنان در توافق کوتاه‌مدت ایران گنجانده شود
اگر ایران به توافق نرسد، ایالات متحده نیروی نظامی ایران را بیشتر تضعیف خواهد کرد تا زمانی که نیروهای آمریکایی بتوانند اورانیوم را به‌طور ایمن از کشور خارج کنند.
این برای ما جنگ بزرگی نیست.
آنها محاصره کردند، پس ما آنها را محاصره کردیم. ما محاصره نهایی را داریم.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77067" target="_blank">📅 17:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77066">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ یسری کصشر گفته باز که حسش نیست بخونم و پوشش بدم</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/77066" target="_blank">📅 17:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77065">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">صداسیما: منتظر پاسخ قرارگاه خاتم‌الانبیا باشید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/77065" target="_blank">📅 16:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77064">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">شورای عالی امنیت ملی پس از حمله اسرائیل به منطقه ضاحیه بیروت، جلسه اضطراری تشکیل داد.
‏آنها قول دادند که در صورت حمله اسرائیل به بیروت، به اسرائیل حمله کنند و آتش‌بس را لغو کنند.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77064" target="_blank">📅 16:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77063">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2AePaoDL9JamVDpij3MTIyPiZFqJBdXoL95sygTTXp8tpUa794xyL4iAx-MtZHkjE3QvAtf46GNnmR2435KVYlSCNO5W-ah3XaoGyVlQKwp-CX3DhVk_QjrttGYPfi7baO0uvVjhabbioTFAo94PkOSOI2AEjo1t4R9jsQ9Mv95iWTZP1iNsnDhvfivqkfZW1EQ0VDMux3sDtt5ab0P1hOQK24UIB-clmngJjLI-77zUPQSslp0izQOzw7BAKL4YRgeekmZhB--MtcLgk6OocruRW2DMf8qCpYdjNpOQw25uhhpKDX_2OrRu9ss_UoERnbV4Ag57DtKJ0Kg24-E6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رادیو ارتش اسراییل : ما یک ترور با ارزش بالا انجام دادیم
+ شیخ نعیم قاسم؟
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/77063" target="_blank">📅 16:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77060">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app.apk</div>
  <div class="tg-doc-extra">51.3 MB</div>
</div>
<a href="https://t.me/funhiphop/77060" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن حرفه ای لنزبت
🤩
۱۰۰٪ بونوس اولین واریز
👏
اپلیکیشن را روی موبایل اندروید خود نصب کنید و بدون نیاز به vpn وارد سایت شوید</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/77060" target="_blank">📅 16:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77059">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIVzyfB2FVKWuvfzF7CIO_S-ymjInZ4YK9Q5PGlKU8qy91ebVqkRqRoLk7JNmZeDfb09sOcOYOHlnL_ukwLE2y0AOSNBAanguwUxIdecc711apG6VoSSzqaUkCKl_oLb9MDDST_fc-7w06kIar5S2G8LNUj2RxwhEMcmGlwZhfHYDh06l_GBsxDBOwz-ec548kSFleIGpGLz2tq50ROWUOqajUylWRcls_LrsaQX_Gy_ovs3einQNI9_n5DY6S1e0aOacETqNWPK9w5POsxY42VyFQ_JlGVPmWYQMvZTKfrvkvpV8tVnOsyYm28nmlu3pnhJhYkP5prLJaKDZMi_Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
لنزبت بهترین و حرفه ای‌ترین سایت پیشبینی
🔥
🏆
↗️
بالاترین ضرایب و متنوع ترین آپشنهای پیشبینی درلنز بت
↗️
🔣
0️⃣
0️⃣
1️⃣
بونوس برای هر واریز
💳
شارژ کارت به کارت آنلاین و درگاه
🔠
🔠
🔠
🔣
0️⃣
3️⃣
کش بک هفتگی
🧑‍💻
با انواع دیلرهای فارسی زبان
🪙
واریز و برداشت انواع رمز ارزها
💵
💻
همین الان وارد لنزبت شو و از جوایز ویژه ما لذت ببر
g17
🅰
🔠
🔠
🔠
🔠
🔠
🔠
🔠
📱
http://Lenzbet.cloud
📱
https://t.me/lenzbet_official
📱
https://instagram.com/lenzbet_official</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/77059" target="_blank">📅 16:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77058">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
حمله به بیروت از قبل با آمریکا هماهنگ شده بوده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/funhiphop/77058" target="_blank">📅 16:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77057">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_Gfn39MBpbSahUSPCHnQQQaV5jhOT9iWOhAY5PTZ2zAs0525n_a8cu9bwvCyWXPciDtuRiicJgIZn6E_1pqhf-667H7PmfrEqb1emJ-bXFCulRysDSyhvw_Wp8KFfKHdjxc7Il0mWdladujFk4_BMeR2OXYk5OtEqmo0LiJnhZ0m62mW31mt-cfuHkOjT0LhAneyps6hVnV6ks9O-eVanQu2GpHpfPyKRvQejdjB-yecbrz9oqYUyMwBwtuk4L5xMbdV0GLMq2wJw7yI2jsDCA7M4yQxL4JcfpmRKTKE8H4qFFizg6_8shK7620bW0L-ASiuJN8OmpzBVjx4edryw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو
مردی که یک تنه داره سرنوشت خاورمیانه رو عوض میکنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77057" target="_blank">📅 16:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77056">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">الان ترامپ عصبی میشه خودش اسرائیلو میزنه</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/77056" target="_blank">📅 15:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77055">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سپاه گفته بود اگه بیروت بمباران بشه به اسرائیل حمله میکنیم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77055" target="_blank">📅 15:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77054">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">پشماااام اسرائیل بیروت رو زد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77054" target="_blank">📅 15:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77053">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">کالابرگ افزایش پیدا کرد، دیگه میتونید روغن بخرید با کالا برگتون
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77053" target="_blank">📅 15:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77052">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">مردم مادرید در صف رای  پ.ن: حاجی منم با سیاست های پرز مخالفم ولی الان بحث، بحث رئاله  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77052" target="_blank">📅 15:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77051">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPEPKnJlXgp8GFLcYU6MV4cLFelZ_kZxQzH_asYKcpcdatznhAum7Saeg6fPcrCilt7-RZ2RRo-HwSD4YioeZv_CwjjARy0WJtL9vxCyf5u8AF5k_JpkpvjAHozsgvYtYwEOXkeDSm73I89A1o3EZXzioEJ3KfPbka6JVlHjiASCcprRtH14pTXcpBt-GEXn3bwvxGsidogjpMbSUIBx0QFeS9qKaRIqiS1WJ_liFrU_nRCXJ10-toiN7jGgP7bYN2VakeTYdFhKUizyLDrr-JW-iia90Mh7RD0eAzCEjY7CsM525ElJTEIXOqF-sjW0oCKLBTgVBkdi7TZLZlb02Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مردم مادرید در صف رای
پ.ن: حاجی منم با سیاست های پرز مخالفم ولی الان بحث، بحث رئاله
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77051" target="_blank">📅 15:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77050">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJPdCxc24lHRVcXw_F-60Ep69Z-8egP9smzoFVekGWwKRinOdoop4ZcfZDRUfz2MIl10lkEEHNLpET-jENqrKnIzLi5XuTTJeeEqPYjYmQrgVEVSoDbyGgJvq0hL5FH2rgRKMNpnSlZH4PJIkzq3NZi4X5wQLc7hc8LT4GzB6A2VBFncSbYR9fPA5ihkbbCu0GYPb_EAXyGcTl45W0eA6eku7Dpz5mnokbstZOcq1P-FTZKvDbbcGYVI4K6eXJE6VC7KMBmceWd_MGMFnmjfJstStRl9uvlC7nmIguzA8i1PSkha1mXmpnvGUNjvmf2Z2f3sdHgWsSCIp-cX7ocSUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیموتی کصکش زیدت کایلی جنره بعد هر شب میری بسکتبال میبینی؟ کونی تو اصلا نباید از خونه بیرون بری  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77050" target="_blank">📅 15:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77049">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وکیل تتلو: امیر تتلو واسه ماه محرم درخواست مرخصی کرده تا بیاد مداحی کنه.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77049" target="_blank">📅 14:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77048">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yk8BvYrD8WzJyiJlk0nHSm6f9czBSTSwwqjNeOtEJtfO9sgiSR084Zq747a3NGd5H1emhXWbbmabVXCYOKHZoPNdctJt791DoZ7SJ0CMuousMZyz2HD7KIkcjiGRuvmfSNgKWa9C49fvAEzh00E132iG6Slwyp4U-PV-G5Juq6tJGdEEjFufXp8H3ky1jCrxxtWMom0H77pMX5eVUcRnxYVoLAO4ofBn-W0skvsJU9vk_hirBpQJL4LraVUDiuM-z6tm0rKvaDceIT-sxTjCQwB7YRShEbGQAI0VOCwE3Px1udUBumREpEvRDVUCwAklchAHRSGI1b3o-IEjNXepcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آیت الله جوادی آملی :
ترامپ و نتانیاهو باید فورا کشته بشن و همه باید یه کاری بکنیم تا کشته بشن چون این خواسته و دستور امام زمانه !
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77048" target="_blank">📅 14:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77047">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHunter Vpn | هانتر وی پی ان</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F__wdScpi3cWb-tf6oWu9hNEyDkjBzU0kMzwva1haO3ppzaGp6gOsEkQo2bOdKMXXkP5hhy9o0_6QZ_YwcUAtRVt_IgTnCUVRAuQCWqwI8rlXm6iZpiAN_Jf6A57n_OQbA6yO2uXPPD1AD3qABAMaj97CC8SXO7U7NC2lKHZ3KY9JLCUtIsUIMVdUZYYwyAHG1fUrdKH8m4tWj8In0wz9pBK6wzso7AUdVuZejoNM25OHZWMLkflzwV_WhYicfeVnIN0etVIruz6ZuOGqr0_cxrKHkQ-p938DgMD25Mv6NJ1md7Lv-JTOLCkJHPeMEiyWkhzuv-rHhuJ-GjZYRhnyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فروش محدود فقط گیگی 2/800 تومان
💥
💥
💥
به مدت محدود، ارزان ترین قیمت
❤️
☄️
10 گیگ = 60/000 تومان
💵
20 گیگ = 99/000 تومان
💵
50 گیگ = 180/000 تومان
💵
100 گیگ = 299/000 تومان
💵
200 گیگ = 560/000 تومان
💵
بدون ضریب، همراه با لینک ساب
🛡
کیفیت مطلوب، قیمت عالی
🛡
پشتیبانی تا پایان سرویس
🛡
⚡️
جهت خرید از ربات اقدام کنید.
🕶
@Hunter_VpnRobot</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/funhiphop/77047" target="_blank">📅 14:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77046">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اینهمه ناشکری نکنید، درسته قیمتا نسبت به سه ماه پیش سه برابر شده ولی نسبت به سه ماه آینده یک سومه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77046" target="_blank">📅 13:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77045">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">هنوز جام جهانی شروع نشده قلعه نویی حامله شده   @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77045" target="_blank">📅 13:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77044">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCSuTJCoJhll6yeAO-DyPWJJ9nhTwUIO5N0-4KTirEE0ykcrY-uojTkfASqpiQn96sjzyKuBACPsOiVQ1wHRHAb7Ms_ErzN1Z45JEq0o6sSz6bLsccdnLHPK580j-j83mEtvfjCPTQm3q3TT8_VBtu05fS8r8CCXvPobbsqEFHASQMvSUfawEA1jKunFjvr6TPLmaF6YGUtIovJ6DEbLOpxiT0t95OX1AiN1Dd49PLeZWoaWnB6U45gjDiNd_-H3q7o-8fUlJu4ztu8938uIw7iNzQAEvmBmT2OcLHGN1XhPV8LYHKcHdNsj351R42qbBnpHGk7T-46OkE2dX4aXSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز جام جهانی شروع نشده قلعه نویی حامله شده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77044" target="_blank">📅 12:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77043">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lz3agGh7jbY1VsIPJAsUW2bk4b8i1HTZM0culb9lsDYC3bPEHLaZROsEJzeFvu7NyBHlM8o9nw6xhWaAvyZ_SCUfbOTE67U89TAbFc4-9WLyTenGkXew8ptUgQmSop737xaiHtZqOs_SYm27jajz0N5LEavYVc3JU7PXWiv6vDbHA_dysWfAT0dHFnfKqAMcCj6Uv8ow_omCk44Aanep6LOrKRqSvE5iv-_LBpiUQDIj_3KglTGTPg2GsuSfaznSI5txlUARkfRQZd51OJVHg3VovSAiDE9tXpmoGA6ZxIks0_A8J5xbkW-pZi3IMKjftn1ejCm4XB8lvAhGhzi61w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وا
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77043" target="_blank">📅 12:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77042">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">مراد ویسی:
نام جانباختگان مدرسه میناب را جزو "جان‌فدایان وطن" مینامیم؛ زیرا آن ها نیز قربانی سیاست های نادرست شدند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77042" target="_blank">📅 11:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77040">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VD7R5zdKE-uglCeXJAq4_BtVchoS-Bdkm5rJHmHHZUDGHStVqtxb1EnMLWEFu-Q989L8fuznBQyw_d-9BUc6ew5ZRpIwB-O9455MFoc3YPQWFziae81_nlYaR1IKgpxsdC2zFYWSHqsSDAGs-lKSdbHETfqEiRFUQmzfgXqARwA_daMK104QkYy5FIpJ5YpMkSi3Q_GeUz0qO3bqi4YhMyiLYGleO0hmmW_JU9KAe03b21r2tRmds3Yfrmi4Y3blsbxvp7d0ncrrvUNy8u5Sy5jmKfJVGM4fMPNKowiQN-mHZfb_XIuohaR8xGjqhmXdMY-1aHkNQ9qUhdg8l-CMmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77040" target="_blank">📅 11:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77039">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeIo1KATJ_fnHSdQ4mkDA2Jn9XU4xY8oI2s2Q4FqpFCoMgUya2pY_cEWX0ThpG-Tbdwtjz8Y2xhJkYfnm9V8mkC-YKQQxh8wbAjqCmHTP7-PBgCBktrdVcWXWVQTRl5q0wTkgJMRp8Yu6OXv4a3zPRoiEwO_9_I1Duu5yBRQA9SXes0hKlIRJ7E0Dk9n9chncPLQThgUN1AMvJyqBvlPex4NxeXVxQC5Vr1n-oCWNHEl95aA23AQszQDJCsAkbEMQvR0bqS9RoGheX6ty0LNJ9BnFKi8thT1oN2ggl47IitiJK1vufit46lAnaepYJ1w4KWfDWqkF6yxHpNPIUwCAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این یارو میگه رای بیارم امباپه رو میارم فنرباغچه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77039" target="_blank">📅 11:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77038">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lP-ex9SjUUjDJ59Uv-SFwsbZfe6JMTH-xXO_S1QE5diwwU9dJEZ6_06Pa7cCDRfzw7UJsqeZRc5Mm2lfYcdDTaiBz-gB30wApaRJSHTQwwmwg2LEwRxTk_bFVI4eqGva5GLwD9Yp1yoZJXYAU3Mq82dY5kDz7EVTMYXAoWX2o2b0eEEZROC08lbijDAPAjFvr82y2Gd1LaCvH3d8bPKtafVzl2sjKQzR15O592dJ-XMn-OmQ_rYBJiDavb64MIuopL0VRvact4VfSSUDfGXTA0SlNLeN8sNH1C7C8jnkVy4UdMrqZilsW1103fKfJl3LM-Kl8OL0VjjM66Aj28mGJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الهی آمین
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77038" target="_blank">📅 10:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77037">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oqoul19XJqYO0xSrM7GLWkS7T4REw3F9-A2yC4vNxqmF6bHNi11_XavhZNRg-CmHRygVA5lG-_FmoJL37cqlNPtwOLtKdVybROEWqoMO9FX7By8jilKLLZ39XKTmB57Q0e6UfMjbg-h9HZAjhpoPH2L2uh8pt1LpX092TF0SGinCR3_-61ZmIrc94xzNB4GgTQOgx54jAskwDX9EYxaRdtRa_HBVqHG6gUPN2Fa2QRW5Jt9pmYkNsZb4NkGTqLQUzziLCWMQF3yHJlwQI6OdglCEN05LWu9hKbMzvdWDR6x6KM8pQFIzlPBvf5yR6Dn7lg5T-aJeSUSvI2d_ueMKvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیگه حتی به اینا فحش دادنمم نمیاد وقتی این ضریب هوشی رو میبینم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77037" target="_blank">📅 10:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77036">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JrteetpukhtglCf6gSH4YkVnPm0P33fLMV-glyYWP848p5MTDOEgOknhxtn_-aK_0LIqokGGNjd2H_TerWV8yVn5HbpidhA0HzZxUfoeZmiYZPT0wcmEDBqDuHFKsTxoV1Rk1Ogs_VSoiY5lJDKKtd8mP2rxNaQ31gSsbPBlZvYzh0I7S4NdtKZCVlZh9zNRudb7QLcVvxnndF664rDZOsVadkTEZl-zRTEsUnNvZI3Z2GbFkuUzGQ2r_uFtbeQsHyS18ZU20U7viEX_Umu7kgdYM5WZMs7BfrHaGhhv55-cRMOpx2rhC5kfZ7jO-Rxw4QhUVwto8vnbmzqfGtS9mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
مراکش
🇲🇦
-
🇳🇴
نروژ
🏆
رقابت‌های دوستانه بین‌المللی
🌍
🕔
یکشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه ردبول آرنا
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
مراکش در
۱۰
دیدار اخیر خود،
هفت
برد و
سه
تساوی کسب کرده است.
✅
نروژ در
۱۰
دیدار اخیر خود،
هفت
برد و
دو
تساوی کسب کرده و در
یک
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر مراکش
۲.۵
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر نروژ
۳
.
۸
گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از
۱.۵
- ضریب:
۱.۲۷
🧠
وقتی از بازی لذت نمی‌برید، متوقف شوید.
R17
🅰
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77036" target="_blank">📅 10:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77034">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سنتکام:
دو پهپاد انتحاری ایرانی را که تهدیدی برای ترافیک دریایی بین‌المللی در تنگه هرمز بودند، سرنگون کرده ایم.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77034" target="_blank">📅 09:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77028">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntGETX5y2MoLtf8gP1UCmr9yGA4VeXEJvrImngakp6THxZTJHnr0wUssjo2XexggmZplG1hOK5JTmWZHCUMi7X0iQ0nl49dHOeqO913Ly_n_9Gvgv-rC-cXzaePttwqp7TidkrxdljGHw7NEgmK5Yf0dmBts3IwRmpogcvPvLGWPNIiab9EizDdSSBOpuKvWf7yh2FvJdMugHdKznmWrFGYvePu5o2uva8jr7DQHqmMv6-wKDg-2q6SFqXfmJseuunp_b6oxjjJN5_ZrcS9LAzJhR1ss2FvosFLk_KE7KHx5_styfsDQon-LM-ru_Sy7zkR6FTSSL_8rJY6rKTkxiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش CNN حکومت کوبا شروع به پخش سلاح گرم به شهروندان کوبا کرده و از آنها درخواست کرده برای یک حمله نظامی از سمت آمریکا آماده بشن، حکومت نظامی در پایتخت کوبا برقرار شده
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/77028" target="_blank">📅 09:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77027">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KFR5ix3yzHjp44206KgfO56zGZlXqRGIVG6hDzHmfh10JS4cvHyyEKYV5AYYltLcw5-Goc5W7Ya6_RyIgBwDCq4H-REXas7Eb6tjAXGrTPaeZ_yw9rbNFuJHlC7JQHkOpq-RKV8N8FFKO6z_foBzl_NDI-trY0wLbCw040H2R1kfKN_DZTT8N4dg_vNDhowJnZlpmet23zosZ2suUOHrCZIiReB_CkOLI3byyi9QkJlUiT72_KcCHM26PHqT2Ct6ReM68iirLKoTIPSw9R8zqDgg_VuJ1R4rP6sxvvuqpnShdxEMJd1Dbn6jN68JCTch9K-Xuq5pMZn4hSg4p7em6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب قهرمان جام جهانی هم مشخص شد
از سال ۲۰۱۰ به این ور ea هرچی پیشبینی کرده درست در اومده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/77027" target="_blank">📅 02:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77025">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">درحالی که مذاکره کننده‌های ایرانی می‌گن تا پول بلوکه شده ما رو ندید مذاکره نمی‌کنیم؛
رویترز گزارش داده وزیر خزانه‌داری آمریکا می‌خواد با اون پولا خسارتی که کشورهای منطقه از حملات سپاه دیدن رو براشون جبران کنه و داره طرحش رو بررسی و تدوین می‌کنه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/77025" target="_blank">📅 00:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77020">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5uV5XkOYgCH60g51cElI_cPoWStucdUg61MSdFIgl99UwRe2Vk3icRvundPl2w5jLde2bGLewAG13Jqy63vuXqhrmJHIlDD0OlZlxjr39QvS0yRszR9HRAuQu9P6ehmNqskmMFkigg3cxkG6J3dkAsjWIyR85X7vxjMw122mTLzSTmS6JwINtrl3k1AERJvlTovPL9UO3yq9GK7MKMjNjLh3adteIeWTovIR7MuKl5Bhw4LyxGt45IqR3Cureud4gs2VIgA_s9uxBJJCZfuI2tyviYAgB74mP_y3B3pDX1kM18ynz9NvW_bQFX5FnJKr3mGrxQvaTCKisCc2bKwuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر به من بود قانون فضای مجازی استرالیا رو تو ایران اجرا میکردم
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/77020" target="_blank">📅 00:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77018">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-wwo4kYrwzASI729PdMFCoPcwuPeVbM2EshW3FqR3OpgvEF2Sjwl9-Mk0bHUoD4qn32Lfjd2nKRwxy4gdctFMijFoNKo3YepT5BE9uTPfcBdZc7dPIBLNnkZBeVAHpbvqGe9Z8_VloUAjoWUW6xqIUplEdCreZBhA5KOlLUynPUx3UPr6YFzW31-OdV3La19PE161nwy6CmKpeL-Gv4JlVfSE0STq9CFwZhU1tP7JeR203vwfG9SVz3Wj-pgy0iupxB31fB79KhysewFJ-hvIier5KX8QtxWOnfr0f3x4JCaJERnbFouyIEL57yEfT6FoQxDufQHx3vlB5Rsn6nMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمب جدید از CNN
اسرائیل تعدادی از نیروهای آموزش دیده خودش رو در کشور آذربایجان و در نزدیکی شهرهای شمال غربی ایران مستقر کرده و از سمت دیگه در مناطقی از ایران عملیات مسلح سازی مردم و تغییر رژیم رو در فکر داره
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/77018" target="_blank">📅 00:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77017">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">محمدجواد لاریجانی (برادر علی لاریجانی) در صداوسیما:
رفتن قالیباف به اسلام‌آباد غلط و یک هزینه بزرگ بود. ترور رو با ترور متوقف خواهیم کرد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/77017" target="_blank">📅 00:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77016">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJIH1Z23uB4OCTG5Kgntle0DSKAC5xvKB8uXTf9KY2GHa21pmaosqwRLWUVYoKAtK5UWHTqiVnEDOsKOnbnky3aJEKJM-3utE7872ezCWehxex-6Ma3tGFOWn0bmwN3_B6h246sC8aHs6A4XlKp37c6PoKIAa0uQSpQ7_1zDZ7qbd-IrgbnjXpKDNab7f5EsB54uypcQKkBhScgNCvNt9WotKGnvIN_3Py9WK541Rl7bb33bX4n_aUuBF963s_pydl4a8C2O1FMYos7_L7qKw1KMN1zfg7iUcczJ4aQ_u5PKSF0diXLy6pzp5UfslQZ_ylZsww0lXva_JCjyERecxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک عده هم هستن مثل تصویر که تو جریده بهشون میگیم "ملا به ماتحت"
و به وضوح خایه مالانی که وسط باز نیستن
از دسته ی اول بهتر و قابل احترام ترن
درکل چه جاوید نام های دیماه، چه کودکان میناب بچه های همین خاکن که فقط دخترای میناب سپر شدن واسه یک عده، همین.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/77016" target="_blank">📅 23:28 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77014">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSDwsAF8yz_qPL_GICMdZKMx2gqhIO7hCN3I6Up3Kwj_AtLuoxwfXSPWAB5Qvzfjg4cMS6IhYo3tMhMeBGYceV_9MsU-zSZlYd2DDGcoEcZUQhlWUgoAy2Ehy5mCC67ceqiHEtTdG67LAdTCJNJn45sSYG8y5uLRc5HZmR_VzyV27eFHrFs-6lWTB9D-VRYrpImYttg7r6d2PrURPvnNeP-OrmkVgpzrKtRq-5mko0ic7N3stJuOJZfSMkcvOZ_8FKl7IHoEU5DgY4G04BC3Uo9pGkf18OSXFmZC5zHzAtgXNb0kASCc2nH3FXqCr95sBWTuYth2cztzi5IBQ9gwtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یا ایران بوده گرفتنش
یا دیماه اتفاقی واسش افتاده
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77014" target="_blank">📅 23:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77013">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQKMGqBiiNM42R1WDCMYFrl8z8LeiDq7pe0Ys3T1hq2EvD8kvk1Dj8llhVA4Dp5iGN0Ma6N1gPMhVBF326OXtM_rSz6dH9d66P2O8O9AfY-f9dTsiVUGym2cIc46ms1pdH1jzICuLitAIIKqUCOPdPoINLR25ZmttXq0nB4kkPBh4O2wzl9hvwToSX0xQsV_Xq_dE7XfEtjWHDMcFgJJNXA7blwfjspNDl3NpaJcHah7NhfdfBnCQVmo25CVj1ZLrSG10utgmCxqkOhGIAIt3qX-TH2p-GxJXHFNFfspYOgV1JggiJZNLt8rpw3eeH2M7VCzG8DonVs8uu059I5A5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیپهاپولوژیست به هیچ عنوان این عکسو باز نکنه.
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/77013" target="_blank">📅 23:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77012">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXfnlnoKcRUepbdm5CdpicTmdvIkUOs3ifgrRQiiURqPTbLp_xr0gaz3K8Mh1kr4FdY4x7vtJQP1APUH-ZKdBRnxeXh5CpJjlG4iWZc-JSYzrYZktwmFblWT2P0eSTg9HRpgy7dJQIsXDaltUUpjd9v92SXk8N-QmQRrIntJFGLOo0LOVjbAYHYkyrJ91sanXWOspQdi07zdiUFZwxRtnsZksj_zquwXrc9v1sHcpgjSGn2uF0TfJvce7XqjAipWJkXuy0Z3OCsd_8eRbP8BlK6ya08AP6UseKsbtOGnEYtzUQI4ZFReAvfSGsxaYlwN9nFgFi47owwIjn3UjOmPpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این مادرقحبه ها چرا دارن اینجوری تبلیغ میکنن.
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77012" target="_blank">📅 23:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77011">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app.apk</div>
  <div class="tg-doc-extra">51.3 MB</div>
</div>
<a href="https://t.me/funhiphop/77011" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن حرفه ای لنزبت
🤩
۱۰۰٪ بونوس اولین واریز
👏
اپلیکیشن را روی موبایل اندروید خود نصب کنید و بدون نیاز به vpn وارد سایت شوید</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77011" target="_blank">📅 23:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77010">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIKJ32ckMx8hZ6MMFVTxYCWGx2RCvPEtEjY3fyGriIlH0tTd8uVFNcwJuT827Ev3NuFCpYGxNvERR5iOMYEJJIlRMhBXg6tK5D0fndVr71Vaxmg68Dvl7CmqFlYgp0Jduu_OrbnIIK4981ELuji_KVrRNgtgJuPUHPnBvvd5qVP1brttGrgSFsl9tiP_S56NoZQH2eHTquPiE0PKqEo9QV9yTOMhJexcYRpqrKPmltCEfI1ZLwd-kvjyHq1pJFPSxt4bQYQMPjoDlxlRV6jfwI5HfzSXRlpVHwRr4LsYoRYcJftVsGve9-IVYl2fAEDgK8-AtsmG3xktVb3cRQY4tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
لنزبت بهترین و حرفه ای‌ترین سایت پیشبینی
🔥
🏆
↗️
بالاترین ضرایب و متنوع ترین آپشنهای پیشبینی درلنز بت
↗️
🔣
0️⃣
0️⃣
1️⃣
بونوس برای هر واریز
💳
شارژ کارت به کارت آنلاین و درگاه
🔠
🔠
🔠
🔣
0️⃣
3️⃣
کش بک هفتگی
🧑‍💻
با انواع دیلرهای فارسی زبان
🪙
واریز و برداشت انواع رمز ارزها
💵
💻
همین الان وارد لنزبت شو و از جوایز ویژه ما لذت ببر
g16
🅰
🔠
🔠
🔠
🔠
🔠
🔠
🔠
📱
http://Lenzbet.cloud
📱
https://t.me/lenzbet_official
📱
https://instagram.com/lenzbet_official</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77010" target="_blank">📅 23:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77009">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUz5LOrHbiI_Jra9acIbt2ZaROHag0KA_E9lVTv1GxJLCjad-q9RIGV2CaRQGvtyvmlR6YBG5JJDFRjbfTCIFUGN7HfTv8q6-JHT9HHHGqhwVzYrFgJlK0H4iJBoMfFLrof8gSXNNUl3pZh0FYx1hV9VjuCmtJ2XEFF4bJTNpwywoKxszCvZ517oz9Z9hz9vRa38sIFybRjMTYGb3zeImFqP6bbpXMiBK8YIGXw3FT9214s8VcPj2zPi1ERRuJvIMfreXqCzE2IbPpdL6_sSkiqr_qQ-TeOxWZBUxE4GEzKKIB2bGVCqmighAl6DyUtUIp-WDIbGhZYNauWD_66tjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسهال خالص
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/77009" target="_blank">📅 22:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77006">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خواستم این رو برسونم که اتفاقات خوبی قرار نیست بیوفته
هرچی جک و جنده که تو خارج بودن دارن برمیگردن ایران و طرفدار حکومت میشن
جدای اینا بعضی افراد هم که حکم های سنگینی هم داشتن دارن به بهونه برگشت به آغوش باز ج.ا دارن برمیگردن به ایران
بنظر من همه این داستانا یه تله هست برای کشوندن افراد بزرگتری به ایران برای محاکمشون
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/77006" target="_blank">📅 20:28 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77004">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYM-I9YATE-FMJhUEnz1K542NhgvLR-6oOT5qERJ8EaTsUMdqpWnRTIsK-mHSEwklG1y91WPzsFgNpR_AJQd-a2k-bHbVeiU5SFmLPwOpb5Cz4CJEN2CfsE0i5i7CCHpWtr9t5NM5ePBh8gk2wz7Rayzk8k2Ao-raZr646eDcicrRSyvY2nNDCwvqwZXbzQ4oU_sj5crQZ3BXoO8qEudWxmNl5F00G-cMmQN77tsAMuiv6a_h3PSRx-PONRuaDWmXUA2dCjgJLhwHtbWQESlMyvNSdPIIuZqedeXMDJ0nOPsiJtZjfqJyfmPCUovzmVZlTZlV5knNd0cX5TGnuie4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باور میکنید comatozze سالم تر از نیکا فلاحیه؟
ایشون هم اکنون در ایران حضور دارن
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/77004" target="_blank">📅 20:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77002">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGeWYZupfm9pXKKUiyoQm5DcdoqIy_ZdnnvX2Cne4A3AvvmI_pb61NSsZ04Uxcd0G-r4kXAU6PgiKCo9idgR4iDZBuHdK-lQfxmh8BgjkgHUp1QsuaFkffKH1GxjL1fOYp9qi6WsejkloeZ-nXrcO53WJl3eI2-TECXiAimfkz2LMT1UDN1w27pm8MejjWtXV6jj5LmHCOUOpCN_5Aqqrpv0Av5nF76mu467ZPTj-o5rmVnC68JKwg78jQm_rBnqkLNQFQq6fbiDleJcMG7Ko7tR7doXZl02xP-4gbbzR9GqjXejH9zETaZ1_Sn8ETNckPWLX1A68ps1akACjQwBYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز فرداست دنیا جهانبخت هم برگرده ایران
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77002" target="_blank">📅 20:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77001">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">من بین ویلسون و خلسه "و" رو انتخاب میکنم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77001" target="_blank">📅 20:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77000">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔥
ارزان شد
🔥
هنوز بابت VPN هزینه‌های نجومی پرداخت می‌کنی؟
🤯
ما اینجاییم تو این شرایط سخت اقتصادی، حداقل سهم خودمونو انجام بدیم و با قیمت منصفانه سرویسی پایدار و باکیفیت ارائه بدیم
🇮🇷
❤️
💸
پلن 1 ماهه نامحدود
⚡️
(
✌️
دو ‌کاربره فقط )
❤️
🔥
249 تومن
🔥
❤️
لینک ربات
👈
…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77000" target="_blank">📅 20:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76999">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9Ut6NCnmSpohXcqX3MFNdOkiNbXA9I0bj-vPOmLQmv4Q9JzaCAErHFifFpM9sL3lOmDN-sGMA-ZiLnL0ezF9SzpOxVQn4jERuNS-Dl6KZvm6zBRhbLC8ZhvpiUA1uhYp13pa7Vp10_Cx0qyK8GWAlyfvTPFUDThtDtUU2X_9VzQT7HBOEOA8kQLmFcjadShW8Lsv9BslyTnxqxcFg2O33dXa96w0fHrv9b0-pk61GNwoZ4JHpBI5amawWWYMecGas_SwZRdMTxA79BFfaM61eFvay0gcvH_luaYOu9WmKkyyy9wCXbb_uCMHsoWajARXcATygOb7zu4PJVCenIdcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
ارزان شد
🔥
هنوز بابت VPN هزینه‌های نجومی پرداخت می‌کنی؟
🤯
ما اینجاییم تو این شرایط سخت اقتصادی،
حداقل سهم خودمونو انجام بدیم و با قیمت منصفانه
سرویسی پایدار و باکیفیت ارائه بدیم
🇮🇷
❤️
💸
پلن 1 ماهه نامحدود
⚡️
(
✌️
دو ‌کاربره فقط )
❤️
🔥
249
تومن
🔥
❤️
لینک ربات
👈
@Window_VPN_bot
💻
به همرا پشتیبانی قدرتمند WINDOW VPN  تا یک لحظه هم قطع نشی
😉
@window_community
:کانال تلگرام
🛫
پشتیبانی:
@WINDOW_SUPPORT</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76999" target="_blank">📅 20:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76998">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9652823ca5.mp4?token=eVpVzf2Uigjm0-DJ99ZoTTRZXPawZ5nUUzakQ5wx2r8_HsCoBxxtRKJPDZtgyC_SH6ExjFkjzh2j-ootJbmDG0Ar8KUdxR38M-glQtfmceTDJ9j73B00oxCjPvvc4L4MmYGXkUVnPQqrR0wNUF29RwBpU0JOvGfi2OVLDZOMZuB8OR-p53mpIqBHG443pQhii2hNLzGf9p8s-Gyj4b0Y6wbJ52mNR5Cp41M4gT9pvs3NfvQhFfWJwhbaJWl8ATl5iOIU15z65AuO9UJj3pfPIOmJplH6IxEK_MvC8hlcVkvDmvO56sb_vjJHFLYWYUIkz2sh-FrUTTPC_WcSl_aWZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9652823ca5.mp4?token=eVpVzf2Uigjm0-DJ99ZoTTRZXPawZ5nUUzakQ5wx2r8_HsCoBxxtRKJPDZtgyC_SH6ExjFkjzh2j-ootJbmDG0Ar8KUdxR38M-glQtfmceTDJ9j73B00oxCjPvvc4L4MmYGXkUVnPQqrR0wNUF29RwBpU0JOvGfi2OVLDZOMZuB8OR-p53mpIqBHG443pQhii2hNLzGf9p8s-Gyj4b0Y6wbJ52mNR5Cp41M4gT9pvs3NfvQhFfWJwhbaJWl8ATl5iOIU15z65AuO9UJj3pfPIOmJplH6IxEK_MvC8hlcVkvDmvO56sb_vjJHFLYWYUIkz2sh-FrUTTPC_WcSl_aWZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو کامنتا بنویسید
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76998" target="_blank">📅 19:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76993">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XYUT9VJaVOuq9PBvvwUo36U28od54XQEkubcEEaRpsrklumKAQlK-Hiu7XAQmtYnN4CM6DJn2vMRuISpPEapnV1_MHNG-3VAt6-Tc0TzSoYjiRBuFOH3x087kEqGlulXeDJXek113G4NDaPmbC4og1whu0o2zgSi6hVkiKQetGd-lL92gohr1ceACvpNpXDUWovDv1wmQn2_dGGJQEuAFyC0pVfdpLl_BucBNbHk1EeTapGklte5KQjF5Sg0iDYwPI7JrQ8l0DOTeP0dJCbII-EltlV50_Og_WFNYOrPjb6uX214uQYNY4AIdEXLcjm4g4MLSavRtTShXoe6TW4hYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dqa94Pb8OhIDggBIdT7sLu-b9lx0T2hwy3PSxdpFezp0wJpnntgkA37AOoYHAvoumct3eS9FWzFWfP6apOTPA2XKF736VRBvcHxYbfa-QFMAlYnfB2BFR7P8PHBLKo3eOnaCHObB2DsWyQ3T_13AduwjS52YVFuCdyzU_7jS7d4lC1M6B2on9kg1zodj1HWeaWhGhbJZ6lsKjTGAMwJ3mjM4p7-N4EbPTPOjGxKtRBn21bPvGk8WfUaHxCAs3agdRhAlLloh0eETMk9W-5AQxrbxqq0XNlXBO1KhqyDBfLcd3g0w1VCyJWPpDpYz9yu4sb_qist9RfwPvRpMMIysVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q3ni_ctF_2klrqW9YAAA2mWP01X24qkUVkLsVGAKRaqn5FyQSGiHiObXQg9iBEd5XTQF16PcsGHOCCEmKMFQ4hwr_2WlIeykwknULYQD4jA7m0qiAptTL4f7jRA5_7ip_umHthvGcLBu7TNqSI3cR35GB_7Z8L_g8bn0MUSOoiCawPKEhMwXbozinC7Cn3nXKMR8Nrepg2T3mNvAUfisxZVWhPzDbnYOE5ZjIp5i2_T9BoNE2xu430tSjA-gi9OH5ig_wTGsYiobw7VHqMoMvRFu4t5iJcYlOviwbUYgi1XKlrfX3jY3qDZOgeQIq1s2KhO6N23kTEZZGywIOraQpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EvFJR6G4Cv8bJMy3TJT6tseG4_bwL-bIb9g2232L3aFq99Y93McmpyOBLmnY8Nk-BOhUOaC--QXDbEFzY8jt9Qw61w5UkOzFEc1E3Z4d6OLkqHnXfC985tGJFueYnAkwCgr2LslmBdx2tnwezvzeYgYpketFo5sHz4BARcmFcdpOgbGPpSSzpsYVC3JnNkSj1lz1czBTdCRL3fHT7lclRKzXfrnqcBIjt3kQRg5aNLkFmPcviclpEAEhF8QXUgh4BhUlepfDiCjrpOEvqjC7LQmBtN945gXVuVq0jKf_VYAddfd5ogkmSxcFWRo3PGuitU_TkabPNK4wugvyzq9bDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بانو آنا د آرماس ببینید.
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76993" target="_blank">📅 17:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76992">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LgR43qavzA44oYdra4lRq9J9asAETgbn_61NYjvGMUm6UEDkDRMjQywbVwsPfCa-prigdHeCYoaPJ7IOmHgBWeCfD7PMFWXyBC4AA8PfKRpRuveoqQL7_TtCT_ZqepRhaqvI-ealqZYK9QrjfwK-v1UucYCw0R_zqVcMUjPKuOaYzo-YgJpf9Ik5MkEJ9K78Q4-YzHE1j5r9bOzWA__CMN3ZOdjC9vVv2rCG0OIg52jURlwOl2-sTsBR8Yuw00SMeXYpiSMgQU1D40wE5M7XF6ykhPQewT-bwiR3GFg27FdeW1fKlBwIOEJ7feuiER7p1w_G09WFXN4tVrn_HlfJng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر خوب برای ممبرای ۱۵ سالمون؛ اسکین وینیسیوس جونیور به بازی فورتنایت اضافه شد، برید عشق کنید
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76992" target="_blank">📅 17:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76989">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/771a0a778a.mp4?token=NgohDNM-1OK9iIBBslJWC2Amnp4HXTTlt_NNq_mRtiOWrEcW00T6xTgvvxLVLjVjv0ACO36IZx2vr6pB2nSlgg1QGB2Y-3xcW8g0tS9yRfiX2xiqkIrQEG2vLgFHRHaOnxir_x9iQUh8OY4Nm8-MdeyKe-H6AeE0XTgEIJ0AN_yCBa5koWuqbHwyfnC5n-_vH_a8O9vXRXvAKQARRLOZ0sxsMxoUNqCqm_EKDSbfd-e_ocNMmVGhg33xGiSEFWUSU1d-tR3EwiMCBvUarhNud2uB5vupiSD2-L3-AFujVQwKHSJW5UMgt9QBeX-qrZvcrejSBSXI36MA-XuiixmpNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/771a0a778a.mp4?token=NgohDNM-1OK9iIBBslJWC2Amnp4HXTTlt_NNq_mRtiOWrEcW00T6xTgvvxLVLjVjv0ACO36IZx2vr6pB2nSlgg1QGB2Y-3xcW8g0tS9yRfiX2xiqkIrQEG2vLgFHRHaOnxir_x9iQUh8OY4Nm8-MdeyKe-H6AeE0XTgEIJ0AN_yCBa5koWuqbHwyfnC5n-_vH_a8O9vXRXvAKQARRLOZ0sxsMxoUNqCqm_EKDSbfd-e_ocNMmVGhg33xGiSEFWUSU1d-tR3EwiMCBvUarhNud2uB5vupiSD2-L3-AFujVQwKHSJW5UMgt9QBeX-qrZvcrejSBSXI36MA-XuiixmpNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگ داخلی پارت 2
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76989" target="_blank">📅 17:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76988">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خلسه هم آدم جالبیه، به ویلسون میرینه میگه وصلی، بعد همزمان با جی‌جی هنوز رفیقه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76988" target="_blank">📅 17:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76987">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">جمهوری اسلامی پاکستان ۲۰ هزار نیروی سرکوبگر به مناطق آزاد جامو و کشمیر جهت سرکوب معترضین ارسال کرده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76987" target="_blank">📅 16:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76986">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/duami4pcXsirKBWF5U2sBh0wfEyhf-y1NV8OLxQWA_YPpGn_uG5FrvbFtoNIc9mcj1a-cOuj--9HBrOQWDI-3-hvQYztLe67G1Uj1adM2ZB5LDlWFQdwUjCJAC06M5bJgiyWVLy2lwQyJi02IrR-rkJ0z9LNGK2Jc2mGC5h29-244bu8-4sQLBBd97LSiWTQ0hHSZuukgm9TLuriOrQXmsk6hPgSAjC5CIXe5H7SlWG25jFl8mx9SOFzR05Zi5rqNK7kJD9G9ONE5CHHBcf_JEwDWvIuFJBQ4HXw0DLfMTDvoUDm21sNzBtNX38XDBx5O1LqWcKJypI1bK1rPKIU8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان عزیز سلام و عرض ادب میخوام یه ذره بی ادب شم تو این ویدیو
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76986" target="_blank">📅 16:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76985">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">او اینقدر بزرگ و قهرمان بود که حتی دشمن خونی او یعنی دونالد ترامپ
اورا "سان آف اِ بیچ" یعنی خورشید ساحل به معنی بینهایت و قدرتمند خطاب میکرد
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76985" target="_blank">📅 16:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76984">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HYZI80dYgaL3fEK6tQJruewGSw9Z7zJsdCD4xtfbxCzpCIj28_xCmwYSM7Y510ci7YU5LnhCs1aXoUeWhhIv1fypvfA7mgdyzC35d6rfjknG-6Z58WOy7b2X2gtHBgQSc8o8vR_KlT0sF17B2JG8Ao34k8ythQHb5aHMMUVajY3dvVS_grC4a_3WO2em3DKh-FWenIQBTd379i18gkt6FW-klnpdZe40VUPBN9WGopQ9bI85qIXio91TIJ4gzEZsqpY-qaZdp1XPkizLCupi1fNNLcfjvjLu37W5lcx9iA9KTb30LU51wjiH_pCh4CEDPPHIfY2NSCdFoP_wE2xL5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه زوج اندونزیایی اسم بچه تازه متولد شده‌شون رو "علی خامنه‌ای" گذاشتن.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76984" target="_blank">📅 16:12 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76983">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🗣
تجربه‌ای متفاوت از اینترنت پرسرعت از جایی سرویس تهیه کنید که تو نت ملی شدید هم باشن
🛡
🔺
سرعت بالا و پایدار
🔺
پینگ پایین و ثابت بدون پکت لاس
🔺
مناسب برای استفاده روزمره و حرفه‌ای
🔺
پشتیبانی سریع و همیشگی
🔺
ساب‌لینک برای مدیریت مصرف
⏱
اعتبار یک‌ماهه
🧑‍💻
کاربر…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76983" target="_blank">📅 16:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76982">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3JZCxW30YTlYH0M6nTGeNTkwOzBIiBmPhnHhiuFXo8oTtqzoWuS5YZJcGUdkHiSThSWldgc3achRqrhmUd4E4Muk8FuQ2F23DdlUOopEwe7ULuaXV9u2adEO7xPoZAgwFJqkI4NJ8StLpAg6bMQ9Ks3KgOQ9USxqSjQJid7xwzeA6g3NU2kFoUsjBc4SzeTeZFH9MPwmv74agqAsOdEIl4If-hhorsbCnIc5fpb8AnQwP_7Y0bIaC5n0YUiVFd4IBYY_UgwSuTc6a4MihBmqxLDq5n-w0kdKAy1pGUF5eMC80Us-YBp2FoZCvY1Kj3ozdRTdhVORnvkvaKt4JP2VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
تجربه‌ای متفاوت از اینترنت پرسرعت
از جایی سرویس تهیه کنید که تو نت ملی شدید
هم باشن
🛡
🔺
سرعت بالا و پایدار
🔺
پینگ پایین و ثابت بدون پکت لاس
🔺
مناسب برای استفاده روزمره و حرفه‌ای
🔺
پشتیبانی سریع و همیشگی
🔺
ساب‌لینک برای مدیریت مصرف
⏱
اعتبار یک‌ماهه
🧑‍💻
کاربر نامحدود
🚀
با زرین بدون محدودیت وصل باش
🤖
بات هوشمند
💎
رضایت مشتری
👤
پشتیبانی
📣
کانال
🔸
زرین وی پی ان
🎤
Zarin VPN</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76982" target="_blank">📅 16:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76980">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">جام جهانی رقابت بین هافبکا اسپانیا با هافبکا پرتغاله</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76980" target="_blank">📅 15:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76979">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">به مناسبت نزدیک بودن جام جهانی خاطره انگیز ترین بازی که تو جام جهانی دیدید و یادتون مونده رو این زیر بگید.
- خودم هفت یک آلمان برزیل.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76979" target="_blank">📅 15:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76976">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L00dzncCPXoa-Yvu5NIpmrdnKQvszN60tN8Acwoonpj571Sr82INDl0Q44ihpWENCqriMoFwJmaO01KxmaYeWVjRWbg92zPf9MFCuh5mP8-W7NimbTmpllxqkxAeWOgW9-ri7kv3LQthbB9NDp09U8G5004ssa1pnzVffhtbRB2PhRAI8xRniowgdyF6qsSZH9dwX2nYY9Qs8TjRzHrBUtT6dpRoA2KlB8PUoSnYvj9FT1LO6PEGHhlhmdEaXZx6HQYIT360zbaD9U_uuCX0aSU0XUGWvPPWjg8uA9IiK_5EDZx1kbSv1AEK28aKhYpitYJePAzKvUgY9pc-o5iuuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری جدید امیرحسین قیاسی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/76976" target="_blank">📅 14:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76975">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نت بلاکس: اینترنت پاکستان داره قطع میشه  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76975" target="_blank">📅 14:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76974">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">بهترین خبر امروز هم اینه که وزیر خارجه پاکستان یه بار دیگه داره میاد تهران قلب بذار بنویس خدایا شکرت
😍
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76974" target="_blank">📅 14:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76971">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ادامه در پست بعد.  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76971" target="_blank">📅 13:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76967">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oTwVo_uzwhBN6_sZyU2ENVx1oQUxx8DhWkNJ_Wb0DJX4gsf1mzxTMX6uy_g84gjM4BkJal7_iHBv4f_uzPM9ZSIeD7aBluXkT3O04DBqaiiBHeeRJwro6NJChEZHJNsbXAWzg8rL9YPCszIebZGABJGyTtbP_qUkKH6fSvc3MQVWfLhjQQlk5wcSjfrozRHpEHqbz5B9OPc5kaj8ekwada61M_VIul0GrDB2iwzBvLWB_cFHMSqF4o5EU-8TXktH18CdHtf0Ha94s_vBIWnOpzwBj4egp0SwTM6ZRii9eFozAuIUlfz8fbqMu2dyZ55iW6NNHVOJQEhV1dENd4Wcsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kCg-ZMU0UOEboHvyjj4FdB7rJKFE5nlhMpMmk7F7PJqyin4HEEJOC0n5iqRc9qwJWbSUjoWKoaj8nilVTODfv7O0iNqE9j1xzt-OAZPo2m8qpH59LuMEzld8ODBaAwsiw6lDu36LUAbtjjXtmxJ2v8s5qk11DVtlXV7OUaZKlTOdVnTFO1A_-6qSfZV-pVt8HNWPpspLTN1_ZEBiAkouRM7uKnd_erhNQH_1tWuLHAqLbwwyCT3mjnlp2R0JmTYnPte-dS9f1Rl79Y5MOB6acYKGHJ_SlsfeMdKGRrYtp-ANVTmDjohmKV4SFtUNH3PEG6MvnbXFMSBCxTPPlOYfvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TpnJR---IwCJW7vDz9uCv7gzzQuU5KiiTmGD-9q3LRpTJ6aBHzykV5zQmyVImubEP2bKtVczZvDGhwoimjaGb2eyrEYkd4JQBcKbjUw1CKJI4WF24JIqwTsdJCHxzr7qGENhg-5Ccz-JiaLVLJcVkV1LRJSzQxfo9J3laP6V5D3t0Uhnon6y72dxwF8IWmmaknl__99EwRs2mSUMRaq6Fcv-SDgBt4IQDODoW117lZ1sLHhWB1lbBQbIzhujn_oZAk3-hyEMFtyk-IW_C7IaTdOEV5xycI-5lfqeDgVL_nyF5LKSJKdS_5-WFi1kj8BrB7J--AaCIu5KbAv5pFFkvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QYxrrs6fBGbDAv1YPmstJJ9VmLIdnbiZ3qJ0-9Q-z8zB0kdb7RnMcXNbrqiUn-AB_4U-pSGQ0M7rTCLB-tq7IwkZ3jZK35I6To-6R2smxwk2hO0QJ680IYbASzBEVODtl03zeEa-Tkq5ZzSC7SOSy3GmQyNyJxIo24qjXlxo897aQeF7YB1mO7IO0BQq6ozrsk-E2NXYqW2zT59-hYh8bZbDyNW9yEnJIBjbmBEL39wYMbhEu6yzhbB70LhgZoHICKIRv-4t75KGpNgGO1JuvtXmP81JCyLFBHs5cOCLDZD6BZsdSGUinmHO_n2sz2Fv2hjlCA1DYsBbHTiP5xc8hA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ادامه در پست بعد.  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76967" target="_blank">📅 13:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76966">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ST1AQ1VYs4OoE81lNeAfx31keFt1E42mN7WmDD3_JcBpxuuoljg6sKcJnFgw9ciwOUI6EvqcbXsUYd-nQA-_4gt5oeSO9H0nOz76pBQp1Y34At9Sm-WovW6LgIalgcoEXHYU0Qvu4eaF4ycO7jy-ytMYAehfELjiPJ8pQkj4guZEfdyDfsVWsVWBr83RF8VPhizNCft3FqW-1JtJ2Br5UiaMTemUt6tandxwYLl20Q6S870kTmBC9SKqi4YFGbva-h8sG2WCQL9pydsH2n25lQYcD-v21ZY70jfZUduLfNSXX5WWo7Xr37iw9e9tauFYKddGgALuRbbv34S25GIDpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادامه در پست بعد.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76966" target="_blank">📅 13:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76965">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDG66QDDFMgWhJ6rhGTXxHd_PutUApkg64HUd3srzdVcRCqv0DBPKKFUg37uZ7kTdOZRTIk08fUmjjXiM7OXajZltQ9zMK7dYc17jFjczbe2t3jOim62sJSsgWm8Jmd9IdFWkHfwLa7NuoiOfWxuKbUA-5TPaLjePK6ei_-qbCe-OniXJhhuqavYnlUkuhJ-dl_oKaQWMMEkvkvoGHcve0gwS2l4xIae6XW9sbukLzSaHqHvBdqWVQ16KENGsQv_PjkL2nlnYBGAestVDgcJ8ePhJeXmNj-J6RxAV2d_O0Fy6ykWzs5GPn0qsJDrYhjA69CR5IfB2RSslxwAddcUng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان چجوری بیاد تهدید کنه مثل جیسون استاتهام
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76965" target="_blank">📅 13:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76964">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">میگم وسط این اعتراضات مسالمت آمیزتون چرا کِل عروسی میکشید  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76964" target="_blank">📅 12:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76959">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یادش بخیر امتحان شیمی نهایی ما افتاد به قضیه خرس و شهید رئیسی، ۲۰ روز به تعویق افتاد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76959" target="_blank">📅 12:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76958">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vofxWjW1JI3ERXZRenWlPVnSU4SyALapHj-eKTV3ENX2hW1gBygT2r0qXIXIM1rcA5zp1ePXoBXB1Su25z-mLNcFLxdwXrDoZuaiFROWOCDBX0-wZyrKao2MEvSbDh_tJGfcyIfQ6unp2eK0DabvsBYl5JprW78FzBcteKFeK2Q5E94VAHWHlTV1KAoYA-rHpzUVTbOQjAE_GJI2YaCAYE95ZMfTZzcQRff83jma0Jbppd4Kq5TMJyxbUj0zzVsRt7NriJbprHY1bHCN_BOI8vC2zwGCMBsmJQtHBMKB5YpHRWLH5rMyItWrstt6ykiKhzx0doW5pJSuEXI_UUcmUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگم وسط این اعتراضات مسالمت آمیزتون چرا کِل عروسی میکشید  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76958" target="_blank">📅 12:16 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76957">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69ce83d7ab.mp4?token=XtfCLhjuPLaJXjZExFQJbkKJopOkmKEwMOrhRldulUk4IdDoe-r32zHdmVohz7XwW5p9hF8USqLsCpDlMkDshwglKmabl6_m27Hq772ROTvlPc6OJGSLUvL6sJvr0_STv9d_jjFxMWpR3GNwKBoFvsF7QmLWjH4Dx0Rgx-HMwhuHdAzQpqOq7ilI4Nw10I3E39UbQBC_OgszWktJQA1Lubys3DJJVWmFoErH6-vrVPB_f7t4MuucjuJ4upiDM-_c92yvFiOrSZ7rBzEaTdfKGfUBwZk92c56ZMX0Dy0-jSS_UwIPuRcT41sUJSEX_ZBcxyw7rkmKmcykvcHwQL5Vpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69ce83d7ab.mp4?token=XtfCLhjuPLaJXjZExFQJbkKJopOkmKEwMOrhRldulUk4IdDoe-r32zHdmVohz7XwW5p9hF8USqLsCpDlMkDshwglKmabl6_m27Hq772ROTvlPc6OJGSLUvL6sJvr0_STv9d_jjFxMWpR3GNwKBoFvsF7QmLWjH4Dx0Rgx-HMwhuHdAzQpqOq7ilI4Nw10I3E39UbQBC_OgszWktJQA1Lubys3DJJVWmFoErH6-vrVPB_f7t4MuucjuJ4upiDM-_c92yvFiOrSZ7rBzEaTdfKGfUBwZk92c56ZMX0Dy0-jSS_UwIPuRcT41sUJSEX_ZBcxyw7rkmKmcykvcHwQL5Vpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من که میدونم نصف پسرا برا دختر بازی رفتن  @FuunHipHop | ALI</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76957" target="_blank">📅 12:13 · 16 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/t9QXv6BYYmt70VnVtIEQ32Bnz_lxVUiQmJZfUjEj26KTCNhCiJ-6UTUS3r7FLrS8C5blGXkETOPgBlc3GavOQaBwC2hsVbOPjQqyxEjRXPVET1P5PX5zRkb6BsVhrq91DMH05zDQQSZ9at4ffa6NhW36ZgZnLqwFVRWc4tsPE_i-DV8OSQ4yW-0rUdVkhYfBluo-OpTXX2AbfOnSZh7Kf6pkaE8eB9tTXFXlshoUfbbibGK4GisGAgT1tjXQ5c8Mo3G86WkbR3e6E_iftWO9SQsy6X-GRBTCJzA1dhhAlTZy4RHdlsHH_Qz9ZyExbWapaE8iJOkAA3rzCPxAhELNXQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 545K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 19:44:47</div>
<hr>

<div class="tg-post" id="msg-26304">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FoVDrE2BZcH5fTLEdGoGuK1NkMf5CSSYE0Dw_w67gE1WdzZVeLSMWiPWepAfSIr6CNUsiMDQf19i7cQ9_ObLEGnpO4rLK5NEq6DJS8msQAyAv7cia03V5xjEszX3nE_l2Re66vO1CRGxiTC5_GA6BStNBJGxQVR6vf7i03eceBhSTaTrlDqDXinMnCmXQZh-Y7hdpCLAP0EnnmOYjElwUc4ueWAAzu4dlI3LXNa0wm0eR0QjdWO7J8al8KvWFz_SqGd4m_P3q71RZE48-er-zY62_lHvFd8nrUTC5MYMToqBodijIsAqViacHLKbEpU9pwwJNRzCPPG8xJWADIdgBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم منتخب جام جهانی 2026 از نگاه فیفا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/persiana_Soccer/26304" target="_blank">📅 19:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26303">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgPedxORJXwDG9JfYk7d-GB75b8JOe9BwA0JX-lw-t6gjp_eZ_tJQoGHDq3USBi79JzDBI5-MweLEonR7WJyAKyiDK3tDT_3_xE8E4_KG4jhpfJWeaFQ84eZJAtyWvNZUcdWyHohgipMlN1V59zxVgz70gYLEh4w7PODBjQGr00h63WJj1CtaE2ZtiEaUOEY6gbDE21tUCsi379ggO3V3f1pQavWAIykre7PXg21AoM60B5hEJ7E3enK5yfIsXcr8BEAYE_xepQGfm-xC4UKx35T8-diB0xY79ji4TrI2jPDeOi3mDhsUwxzPztXVxju4V7gK2therWAjFspnTF4Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ‌جام‌جهانی‌ و برترین گلزنان این دوره از رقابت ها؛ کار لیونل مسی برای آقای گل سخت تر شد. لئو اگه آقای گلی میخواد باید امشب در فینال برابر اسپانیا دو یا سه گل بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/persiana_Soccer/26303" target="_blank">📅 19:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26302">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMXFxXOvcoWSARqD8t6JkM4YxYM5Yq2eBYz89Bc_Hk9iB-i-RWLeuKoOjjMwfyr4pRDyAyv_hSggP8hR_iLOuBSa2T-BNH4QYxI0PdEZjkopRGpDy5o_rbci4WtZlCIQyeag6CQ0vUfgS3UIYdc8vVvRuobF9G7p_WQEEd790-J5Xv4M-ePdKZuRRP06RyYVZ7-2_dH9zxIw72kL10vB4AyCAfoFZFc6Qz0zKmB1SkYHnjALd9sdKEH8pigHyW9r__jGhjJY4-1UVbxK2ZvYVDBDigGw2WrKADiWAaCaKaDl231lCZuaThNF_OCeRcJoLIXjt6QlrpFkM9voGkNA9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: کدوم‌پلشتی‌خایه‌اینو داشته سایت داداشم عادل فردوسی رو ببنده؟ ناموسا من در جریان نبودم و امروز صبح دستور دادم سایت عادل رو باز کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/26302" target="_blank">📅 19:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26301">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_pV1ROFZ2gQ220_2ya6NYHWwuqYT5T_TXsplIjniRPDopBiewOyssEA2KRvfOYO_mhwAgB2bLFQbqSZO9rxC502So23jk97JUMiTrtY3Eocnsa-dR0vLtQEMOigVVVzEL7DpoAqSNIjqeSfZUi1pOXyGLo-yWCHVM-IwuIFcnitc2WzSaXOcHVKkh-aFh1YIIdMDj7NQ05X0yWFF1ghQUOfSCHFRrLOtZb_KwKF_K_4ogsCfxzXXLIAVPKtCvFR5dTfIMLQ5amcSZxqxnGLuh-Czu6ZdyJp4rCVD9U_dD7bHuAYA_0-c_9dMxsDOfMj1qlc8TTKDIUr37YXiC9xjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ سهراب بختیاری‌زاده سرمربی‌استقلال بجای محمدرضا آزادی خواستارجذب حجت احمدی مهاجم‌تکنیکی 22 ساله سابق استقلال خوزستان و پیکان شده. درصورتی که باشگاه با این بازیکن قرارداد ببندد و پنجره باز شود محمدرضا آزادی از باشگاه استقلال…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/26301" target="_blank">📅 18:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26300">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tx9LXdV1H2SKcYt-WsvjNAOwgnaIVozCBFIZDSOHc918-g9sRfXsCnOG5eKpeXlJ8MP50OCpuoIGEy_IWXLcl_vh0NQxGLC0VR4192fLAZCKthgZPoVTTyPE6Y1oJOoRnGvs1gtE3tsNg4tEiR2w7aRGkFKQlOrFeHB2BcderLEnaWuQhUl8-XL98x-F2yOOXgfZ5aODfpTId2pCLcvoqxLHDIZ3tFIFEL1k2TL2UdggokekCH40vgkRd3JLOKN-xq-yqaYu9OwiKMLr3I4Zow88bhhOoAj_gGA6emrqZxWt8RpbiL1MRK83aE0DNCB7UTw2LxkJkWtzfL1vCu9aYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کمال کامیابی نیا هافبک‌سابق تیم پرسپولیس در 37 سالگی از دنیای فوتبال خداحافظی کرد. کامیابی نیا قصد داشت باپیراهن پرسپولیس از دنیای فوتبال خداحافظی کنه اما باندکاپیتان سابق که خودش این پنجره مازاد شد باعث که کمال کامیابی نیا در اوج فوتبالش از باشگاه پرسپولیس کنار گذاشته بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/26300" target="_blank">📅 18:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26299">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQ1rHbkMoBOmHlPgc_lt-JrSLNZECPCIftHu18-DyybZ0uWGb1N-g5Jv2vp18Jj6UQXP38GRK5fYV8u-lNlHkgasyw9i408yUAiIfCsdBEsdLs55DCHZibxdbHiXNgnHfImeihYth5EEaUicAHIg5vyPSbAeIrfGPa_5GNTFEt6ZFuSBDRvf-gm2pZHrgNJQ1iFPb-GhBZ9lExNYklMjsY6eLIPwfuKtimzpnfRLcTU-AayGF9l4qHMc8dCIQXNRoceWGC9A4KkOzH9bkt5NWgcvZBvtMon2PYkRR0sJ_owJYZOzhNx6UE-CGx9rI3_-odELKJohzsLDqvfbYBfZ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ فیفا ظرف72ساعت آینده استعلام باشگاه‌پرسپولیس‌ونساجی رومیدهد. اگه پاسخ مثبت باشه کسری طاهری بزودی با عقدقراردادی چهار ساله رسما به عضویت باشگاه پرسپولیس درخواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/26299" target="_blank">📅 17:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26298">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OemgJYU3j0XvuRE6JrISGeYLvj99pf8sOMMWJh7VFxxdw9Lf6dqQhL-1PtWv6LPqYdrvdDTOoiY1xCIf60V44PaTioIrLPCpD3KVQuUOvYBuwOUFofqjixsXX00w2nqGr0_BhPGNOu6OLoe5hqnvv2pfMclt3I19lj9InBP8fRM43v68SYEmvH7lKsOJCXm6596BeljD5sF9N5_98mYopXsEy4Bri5LoZpo7VQejrpPshZWqx9JydWOzPnArqg3URX_YXDzxt28l6NX1FVDoYOxstDPsfDb_x4ldALc-AhTHtV0UUvtIHl51WsWKoagLVEsh7fRyfvG1ovWOcp7wSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/26298" target="_blank">📅 16:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26297">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1Lx0u1mLBx76hVLN1jM0V0n-6U0J5H5JG2MzkKlGXwRxZZJM_5naeoJdNoLc2E83RoCteNBq38maEMxHoU0K1wNCoCJ9urYUo4dcBfch-OfzUUilPDU6t__cDTRLF8Q0N15dM7i5PDG6HDNm1adHKgtsQyfwp9lQLzrife77SVwTlJ9vaYYRJY7-BqyIlObuckenffcq-1xkfFxBe8Ons-YwUaWwGIRVx3QcIQAQDa8p2FKTuKurxFFx1AeOICQNIZU4RzJeh_oQ12XDNShGbYCM3IwvDul7pIQVVI-QwHKmh5qC-ylZqRx1G1ALTFL6GndfwWpI3qrJsUGQ2LbnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط 7 بازیکن در تاریخ موفق به کسب قهرمانی درجام‌جهانی، توپ طلا و لیگ قهرمانان اروپا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/26297" target="_blank">📅 15:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26296">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUjuyaV4yXw6UFmpuUkZtGOEUB3prV_gqndkMXM5U3Pe-GzNC1eLJIrBWb9gbeWO7Oshvn5bLQBmldPDR5nB3csXniBvQhJkjq0jyhHQlwC9L1xcWnb9Hma0UR0yp18sOS67oOPqBhLJ3Fikeurx5FyuvM49cDN91dICgZ9fabcpv3wjFEg7BzAqvxRdcstV_ugzSUFo4NVP-jLKjF6rJak6mtaVj8tsV02qbziNTiD-1bMeqXv4zpLK_Viqk9BJeU-5nDKSgs9Bvs3kME-ZZbGeo207EsX1QtQnfGjNfdtOh6SrRI_GOAxIDcHEMaNzAUEp5-kDMVIKfMwUTKmEew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#نقل‌انتقالات
؛رضا جعفری وینگرچپ‌سابق ملوان وگل‌گهر با عقد قراردادی دو ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/26296" target="_blank">📅 15:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26295">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwvOzMokkoLYNAotFP2S7_AZBkYVoZs1bDiDefzSnC9FwEiEt71aCSvEbrt0fmYM9RY8veF5kbm3NJkj8CqDKOYVPlHteuoDhrMzi2VVNWYIo92QLQ71dRd_7nQBoAyrZMIwg_RfIVB5pvmcyJTMhb5zN7shGS1XUR-cdf18pRABzmrc2RJd2AHdD2ynDwSqcghpsxvSlPHc810-hwm8IaqrIZN4ML8kubFtX3UqaseiIgkGlObpR0agkOUcgwSnnUgtW6VbrV-NH9du5twx53PqLkY481C0cjG1FU3lgLlhOEW-D0FJaFjxWMI5aU6pZVo60TL0jrmlvB_mlY1MIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رسانه‌ های عربستانی مدعی شدند؛ باشگاه الهلال پیشنهاد مالی بسیار سنگینی رو به فیل فودن ستاره26ساله باشگاه منچسترسیتی داده‌اند و قصد دارند این فوق ستاره انگلیسی رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/26295" target="_blank">📅 15:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26294">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvEr5QPWrew8lrEJpc95xgK-9DryBZmMVF0EIXwETBLudX5Oeztl3qTZlZcdl8jqYNQe2RVAsyVzS6DGPXQ5qD3jJF4OKaJDrKevZqlTDQyfSCeHD4eaMON_e-jsxq_wXvpPQe3TolTXp6u1LVrvvnGTAfa34bP13CsMo_4hReALLALTvfDm9Dl36AKtF5PlA-C5h52XBXnWM_4YoQhIm-r6x2x5f6LJAjl5AjrTzK4i86cykM9tW5fLByY4xMYQKPLI2nt3FaJuvbA6wBzWpyBaTtcoyaUX9auvrUjAxCj4n-v1Tbm-NUJBuY8jA0SKxZdkST-SB45IPzweVdk7Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اگر اتفاق عجیبی رخ ندهد؛ باشگاه پرسپولیس ظرف 24 ساعت آینده از محمدرضا اخباری و دانیال ایری دو خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/26294" target="_blank">📅 15:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26293">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olteHfHhY6FAGPyNwYPVpjyNozzi1-b3pQhxs0CNhfKf95ngvEx7XDfWulWNJz9GPEYUDRZN9ogw-xZkhNCXIYVWOY2ckts0SlonmYlBoKa85ajFlEgbrspQ4bI6MYPpdLXxqTA2aSFnNoAjTRFhXaF1tAmOkdKyWesraXweIV5dhEDE-HwKgaROIDUYHtL2mCpmrlvzz2ehGJta0PVpuzePRfxBOe37fV_PZl1yVwYRM48NwuMlt75eBl1EqX6RQ8pcMj-QZrIADsPvWpL1k8If4tzRV5-atp_Ap-1Y73_Ie5h25ygNiGnXsUPOTplelVnJou-Sdz7afHBrr7nLvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌قوانین‌فیفا؛ درصورتیکه پنجره استقلال باز نشود این تیم درپایان نقل و انتقالات نمیتواند سه بازیکن آزاد جذب کند و تا نیم فصل حق عقدقرارداد در سازمان‌لیگ‌رو نخواهدداشت. این‌درحالیه‌که رئیس هیات‌مدیره آبی ها امروز عصر گفته بود که حتی اگه پنجره باز نشود ما…</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/26293" target="_blank">📅 15:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26291">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D0F2hCZWzazsyCu-F5KGXkjlmCkR6NOvd9fO8f-rQqTBLWqjYBnroHbqDbteYu0b_2gtmu7UIXHzW502-UBj9PhDehMa542M8rbaZNLbMa4_HLtZPheOCe6FWkeyYV6WdBY4CX71KRATXkths2jXAIMnMo_zj2FdToctS3FGQWaChQwBU_tuTKDysjcPsw-1WEbzwayt3xycCZG0_YWto0NQ_FVFw_vwg-1kEqvapi9KfDVb37lnqVDxOO5zPABggnZACAyq8Jhh7iBvCSZroWWGBBxJ6z5W7cgGo9DgqOVYx5k4lJbD7KgN6GIJQs8GZ7dUPH36eaBw-TnsZPHXzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F4PgX-FlcV-_-wihCwlTbrQ5IrHNrA6VsDg8HNH123FdXmhrffNXINdXKzwYEob-oBdk7w34p5xPySSfQzYirOjVMEoqJl-QXF7I2Zxam69wkX0kbmj984FlnMcSz2UJIaAUi3B9xIk1yij7JrmUunE95H1bcX5hwR5aI1xtFZ9tDB2f9A1sMeQh9QyfnDqGBMpjqJS3xPFVzTTxX7zrzEUQrJeVxEXWp_bJQhONbVaIBTlnaWz7EfeU5LaI5-K0_Bok8CZ8bnWwATtJ-Sxva8ecbfG-ps4hucPZk-zSG5oINd4m8H0Sg5nS5jM12lUyBnwo7zXX4v3SN0x6uN7nBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🇪🇸
ملکه‌های‌آینده اسپانیا فعلا دارند با کاپ جام چهانی که بروبچ تیم ملی این کشور گرفتن عشق و حال میکنن هرجامیرن‌اونم با خودشون میبرن و چند شات یادگاری باهاش میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/26291" target="_blank">📅 15:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26290">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYIED3fY3wavwMaHP3UZLkjHBpfCaaDRswfwff2c4Yd0r-xbbxJZAOJ-LffKrSn7W0CQ8m21hWIo0JjSsW-bXKLhzaiwPz4wwCCO4FMOeyzxqZBdueWcq8EtClaRmZ2Iis9wVMFIrPHRpor-u6s8HGxwnHfkq24VCf-Uz5hhPt8FFl2UwFOZC2TsHmLJwG7134JIRfvcIK9S1ZQ0D-W0aKxSW1J2cjWXLCrJxUs8-_bg6Jy32R54cXSuVbgaPhK6e7IYZhT5hP9n_nwex_4tOQ6ISL-dPM4LEbnjH25d1iYAGRZgEflPi3vINDerBuEHVRaDgtR4JFzhMXkLpGrfEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
خریدهای لیگ‌برتری پرسپولیس تا به امروز: مهدی‌تیکدری‌نژاد، سیدمجید عیدی، پوریا شهرآبادی، ابوالفضل جلالی، پوریا پورعلی؛ هر باشگاهی هفت سهمیه لیگ برتری و سه سهمیه بازیکن آزاد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/26290" target="_blank">📅 14:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26289">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKqFDAKniYAtGC5HhYFlo8SqWZFsdT8PvEpjD2w9sEf82o0hcc9zGXtFuZIASHO-69PRyvISzz9iyfwpkKqPboKkfTnADCZq-pTCzzW8oXZgQq69I5k1Gy2mZZX_c7781u0vlSXLzU5EzxWT79XEnd7CNxtfIXd2trElQXCB49TGphWw3eDFyh-uSLdC8MvHvRdAGOh17Kl0THrQ-veIwEqFE6aeNMaRJ5lZRIL3qfmFJ7wzDZ3yhdyS1S_TCl8eRevoUfTiAVEfolNW1FLljPyXQdBw2Ogy-WExtUmivEcleWDtTIiqJMDyfTMflU5_iNoPyxhbvyNFAbGtmSHItg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیمایی‌که تو جام‌های‌جهانی اخیر تو جریان بازی نباختن؛ ایران 2026 و نیوزلند 2010 با 3 مساوی از جام جهانی حذف شدند و شکست رو چپشیدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/26289" target="_blank">📅 14:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26288">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmFyLCClfnA97WjL4SxLwCGT5BUfKUGYrV25O1L9gJQuQOxleuLbGUTX_Bil83lQa2BXPhxyfgrS93bogN2ZKiqSsds59-J4f0fysbS0RmRBusHa27og1P-_JsfKLXo7gAfXAty30AJFYs9-8L8IQaEO4-33kp7DWZhgbZsHUT6PWWt2ID2PWweEKPo55AIwDh5c1ussKgZ03grf20KnmVNd4hPFJVRgTGPDn--a8Th3IGUkVXgtPUpgUu8YUnwUgPgXAchdIGc6uid_iZsJFbkNkpQ6vReBWpsy2_1PwAC3s7Q1Sj0DRdFs3s-b7x1eHyKq7nfX17ytUdkFmoXI5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط 7 بازیکن در تاریخ موفق به کسب قهرمانی درجام‌جهانی، توپ طلا و لیگ قهرمانان اروپا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/26288" target="_blank">📅 13:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26287">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eT77gQuzeTLN56X5pdBpJw10ZzRu4kKByKWBiojAbBdIFLiOJMCSGeYki18JCAWreFgEMOhSavXNcEV9AvFuUgs7Ws1CUkLN2ufUBwmLs0wEoJKvdb6-C5gLUHAeWCc26zE5rA98aCxrGlOFf3Evs5G6LdP5nyt_6IFWHTX7gnrDe8X5mJZs-zRobzbPGPFGiCMKoFgyzwU72Am_S4V610AfeJaycvUPAsemL_QJF9LHv4FfeezVDk1bLydtPPp_c26wk8WUYYJ0p7BA3eLFJxFgl_Qtbj8a7KVQyT4_emDj2rJ31aaKAS4tUv1zuyV2_qIYviDxV-VDGtwWWVQuBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ بعد از رفتن محمود بابایی و مجتبی‌فریدونی؛ بزودی علی نظری جویباری نیز از هیات‌مدیره‌باشگاه استقلال برکنار خواهد شد.
❌
علی فتح الله‌زاده یکی از گزینه های علی تاجرنیا برای مدیر عاملی تیم استقلال بشمار می آید. تاجرنیا نیم نگاهی به حل کردن مشکل…</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/26287" target="_blank">📅 13:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26286">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h41pbYvhb9e0DKRwl4nmkMylfjR-L_tw-Q_u1kgjrIAa-zqEKnIpLdrsXeEsv4NaKUUyLpzbZUnogyAG8nrPyUxHWEjTejJBgChTLoF26tDq62oMlN9rggeq-HnNLHq1xbsdgLGAQd1Uz23i0J0pCAAL_U8wmX0_ARuoNMvHyQv-DDyU8JrYXMyfBPprca8m0c1Jv8g3xWdzEWntvrDOMsWvDi4IA1_VnsilREud0LNmu96zrOoNtpPS4rzBz9zjVlBqEuVwK5VVzueshEg-U4zst7Zrdb99BALFund44B6QeO6SNd-fvUSw0ZCegQaC_xZxyRK5UiCPR07rRHVDWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
رسانه‌های‌آرژانتینی
: لئو مسی بعدِشکست مقابل اسپانیا در فینال جام‌جهانی به هم‌تیمی‌های آرژانتینی خود در رختکن گفت که این آخرین بازی او برای تیم ملی بود. و شاید پایان دوران یک اسطوره در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/26286" target="_blank">📅 13:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26285">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHSV551QYiaa7lNxeZyZHdoqMT5rVTZ2Mp_QqLo7WTBaFO3W3E1VFTfTT3j0P53qHoyERa1sirBfEfeYaYiB15LtHussL6SMdUEloOrh0KhkK8Thn14Bw-eGzIjDW1WbWK0BPNtSHB4eGsCjKSB0XyF-35NKkFlQy2X_ixysDWAN1KVjjWjRiLztEmR-2v5pJL4g-mnNWeUg6Dyrabb6dwT3qInXbxspQmbmhdYiTnFWj71lwwgRwRbHTru1IO3i_exbTlJBLDKBk47k8niROmoK0mvgDwG3brHc8CUnDotlSe0y86SCFbjuYT41KlrMKjmac5UjCvjabQJgq3tWHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسپید، یوتیوبر معروف که بشدت فن کریس رونالدو هست‌ شب‌گذشته حین اجرا در اختتامیه جام جهانی مقابل‌چشم‌ میلیاردها بیننده رو کُتش "فروهر" نماد ایران باستان و آیین زرتشتی داشت و به شدت مورد استقبال ایرانی‌ ها قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/26285" target="_blank">📅 12:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26284">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jwia238aa4jtjgpwphxxdxOofx8yCqM494SeCF9gezarIaXY24YO-Z_gvdeT8j_P8nWI95Hty8ZESwACWdIGx-_hbvFMG-R-FfVMWpGHujFpjNTikQIDhjq_fJmIsMqnj-SSyDNSMIEtoySBtyLDMv2hY1zS58MVf_GylbWWNSf2erursHIpUxI8BIYQjLeIZoJG8lnTKgqdHA3BRCJBu68HhysftgiUhMCid-6sGsuqxNaJDujOnSq05tQJIq0pahUccHgdkCXl6Sea736ZlMBcqykxjjJ3AGDWlnaw1NGPz85rX4uSPuwjVivPFVvC2OrPr0HF3vMbf0j_2PdLXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
با اعلام باشگاه منچستریونایتد آندری سانتوس هافبک برزیلی سابق چلسی با قراردادی پنج ساله تا 2031 به جمع شاگردان مایکل کریک ملحق شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/26284" target="_blank">📅 11:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26283">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfbTxnVOObZtKHadnNtxCtZtdBr67DUZynwZBbegv863QHo7DJRrN4GT1-KpPcUqcbcuP9iAFKUW5HdocjXct_GJouLM6IE11LJnpaqE1LCiCiubLYpF_z8KSWaJwr28LZxjsJyQAnnV3IThy2ELUUCroidbFVji9lFQUrTJmP5W72mnuVGxdtupRThGoZSSNkL7gmI1mlgGRH59_ZOxE1KtcWsXHmVvRzCAlDQIuCV4kGoVvA1NqdASSzwaUOszNx02vbsm4Z9Mgp-iWXAgKGEfiRVVF46hxfVMKkKb8eme1Khveo7yB6yYYw_so6mx7C5yhtDUrThh3OUWIO9LIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پوستر رسمی باشگاه چلسی برای مورگان راجرز فوق‌ستاره‌ انگلیسی‌جدیدخود؛ چلسی برای این انتقال 137 میلیون‌یورو به باشگاه آستون‌ویلا پرداخت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/26283" target="_blank">📅 11:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26282">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grPzqcVyce5MbcL6MKBQ736WntDNNSBCCHlGV4yXv-f6hY9aL9KUptZhGMzt8G1Pfc1clCX_i-89Hsc7T6fyZsvF1hINQT9AH_W0MOE4VI9vlSqndsQCAH0uN1eouRxmaGc5vHleMy7eNpSwdJh5AClTqbRTGEai1NgKnIGzaf3bJDS5V-zwaxbYwJzVVTs-wXq6ks3kXsstP23-W-vDJJdMXGXViybJWMkOT6dkhCWRTBgjCfOn6Fvcf-yRl2ApkEOZNMJL4ohDWF02auUlvzvFKKsD8MC9qU0XATooNq4ikSY7rY3U-fy7FDUWXeglXY-YhDVgkvAeQabvm2E2gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب‌کهکشانی‌وبرگ‌ریزون رئال مادرید در فصل جدید درصورت‌قطعی‌شدن حضور اولیسه و رودری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/26282" target="_blank">📅 11:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26281">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FueuJqDAvtTTLVmIuUP2sqMzu9BsTxqfH9b3vV0p2UFwih48yP6fdly-jBfFDRE5zUpO8BcBm5m7A_XtAfbXJPe2D2I9bAaAn7kF3BETpxqxBKxmKmr3lfgTeBtGQk01qEW6pCttXT9q1tDJZOOmb4S0gUEfM1KFFhuomVTax5JlgkPDOPSY2N3UdbS5SHrdL0_YIqArda-7nOE6VPMb-oeLXvn3MupFX8XwdFhCjFAk98AL00gQCl-EVq0XPzmYaHlViHaFkpgrk3-AaKYIBPIE-Za0GfNMN4QDyP2WO20IfOKlKuANLFI8SGKTzT5zQc0ZwRk_fSOr-vAAT1p9_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تکمیلی؛ دیمارتزیو: مالدینی مدیرورزشی تیم ملی ایتالیا مامورشده‌‌که پپ‌گواردیولا رو راضی کنه باقراردادی چهار ساله سکان هدایت آتزوری رو قبول کنه. بایستی صبر کرد و دید پپ قبول میکنه یا خیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/26281" target="_blank">📅 11:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26280">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxAjgqSl2SB1YeWhbuLTig2G-bw7zrV_xlUArawlnZ6fRv0SdEEHxp0A9z9q28hck0olb0ty8F4SyEHlh2t30blDhCu9uIZHWbC2qWugYc1zpuMlDLMKwVZZrs4ZwHuxrExRmYMhQ68PV-S164IVg-HrQyYxxUSP5IHVKA0BpI0nKdpMuIQfsHg4sTk6hp4xtkxJjH2lOm_RlTyMhITMXWrMfNeMya9nNToe04o1rnvOdSq81fF7EsZoevY920xS1RyS4Scuk5MT2D_RduxWbpPZ4V2cgh4ibuylMgES-D6N3a6ug1zAHR86NO-vNoPVf2dzjpg6nWtxhq7kjRIuig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
1️⃣
میلیون تومان واریز كن
3️⃣
میلیون تومان تو وینرو شارژ شو
🔝
🎲
سوپر بونوس
🤩
🤩
🤩
درصدی وینرو
🎲
✅
مخصوص اولین واریز
✔️
🎲
برای اولین بار در ایران
🎰
متنوع ترین بونوس های را در وینرو تجربه کنید
🔊
با وینرو همیشه راهی برای برد پیدا میکنی
🎁
🚨
اطلاعات تکیملی بونوس
⚡️
✅
✍
️
ثبت نام آسان و سریع کلیک کنید
✅
🤩
🤩
🤩
کش‌بک هفتگی
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده
!
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
r31
📩
@winro_io</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/26280" target="_blank">📅 11:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26279">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ct_sCUJoYKCSkrv7FheNNZqS-RNvF_O_ORHUpCZ9J1TkFd9KMbFXRsSJVfplWs6IIi0Qpl6ARsCITny2-CfJYSQdWYszNX5XdAFkfpE96sy81oyaKX4rxXexB5wuWYPeWnfV7F8rE3L_zuSW6gQZjBFUqWOt5uE785dHXlnWJoAB7uip1Hm0qNChrPM-RSvsm1-FShQNw3syvvpQeT7zTODI3GBY2XI9YaT5gMKGmToLejEz2yI6ogvzPItpupOHtZ77yi-I5UjWnOSTMN1pFOVvs_OWeBbvdtL378j8cr1DBNpkZiGgMdRwM8KDBGrdphF9RsOwHZOEHDVOrvC8nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ بعد از رفتن محمود بابایی و مجتبی‌فریدونی؛ بزودی علی نظری جویباری نیز از هیات‌مدیره‌باشگاه استقلال برکنار خواهد شد.
❌
علی فتح الله‌زاده یکی از گزینه های علی تاجرنیا برای مدیر عاملی تیم استقلال بشمار می آید. تاجرنیا نیم نگاهی به حل کردن مشکل…</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/26279" target="_blank">📅 10:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26278">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJ4MLLjWdRgOBjKMbQsnZM-ZQplz1RVUefYK15X-gnKPg3lrpoNjIJYcCL7zHpNfnfIjMKAy--Cq7OSxjJSt3pvkTG9-rox6CpQVZwnT4HOIkPu3FTW7CMaGvKBX0jccUpQtnsZqbNDmKVwZSxVVM1clkOfVlQIN7jKq835CYf__gGUEljnDL12XFjt50GoOhHiSC840EveP7L8DnUIWcbTWhaleq9F8FaxWYADmVB8PzPMS4w13PZib1oqWdm62ndPlWWFrUKZCj29q4TvKUZ4aue_tBTVuf2R96UNWab_eqw2yGyluD7Bh-Pu6gi85xLVm6Xws4w-ZlMAEvEwZcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/26278" target="_blank">📅 10:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26277">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2fwQEkDyLVzJCxMXqJVrgoXOr1JZN8wdH5eoVbmVExLp4vUnPZMUhjyFbPKDUp4aTqa9YJT7Mxwir8EzfuKU3R99VghS6DlkYsZcU5fwooaJB8E6o8G-aTGXUm4wyq_ICUTn2xDa1daRLFnJT9Ml6Aqm-69mfJC6QHjz6BufnqePkRLKhkUxrJ7FWtZ4A7ZDajKg9CuSRewC0m3CefYR2BAQhIcuv7mbmfgwd58BBuKbabkWXwTXIr7zW9uUlQ-NexarlQvsq6_GjfOwqA-7b4aBVTijjfMo-9idfdzl7JGxTIH-5n3Ko3PxAMet2EjTS7c1vMpPgfzE0y9OUAwmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
شمارش معکوس برای بازگشت فوتبال باشگاهی اروپا آغاز شد؛ یک ماه تا آغاز رقابت‌های لیگ‌جزیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/26277" target="_blank">📅 10:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26276">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKwO7R2uEbyelP6p_iFbqZPOTheYL5Ln5osouHvObuD8PyPO9ybvA6rqdpR-gW8cL54gXfZkZn5KH_7GBCQyBJVsn1jMUtaDbVBIbiXQd5RnrC7pTg1LL--AUOOUo7WZbkGNHoIxxOusjofXxlGfwHZymj-ztHdJHBtG1LkraP6zYmmX0CxmDHOE6isyV3qo9L0cgstJM5G9YFhuEYbBRfMJkA7Yu13vuU-jRrgQ_5r0R6o_UpiMLuLgRHubavH_tfy9BnzwT_T8s8g7o9VMhTA2cuhzPwX37AbBLm7TTl96hTuHgnQWZULzN_IgYS9dR5d446On3eNcdohMbeQh1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
#تکمیلی؛ باشگاه خیبر خرم‌ آباد رقم رضایت نامه مهدی گودرزی رو 500 هزاردلار اعلام‌ کرده. این مبلغ از سوی استقلالی‌ ها پرداخت شود گودرزی 22 ساله با عقد قراردادی 4 ساله راهی استقلال میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/26276" target="_blank">📅 10:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26275">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ScOyWttHrXssh489CemT9klkbMv5NBrlKwxIqCjfXmADmwKVTuwPEq92LYVDddba8O_SXMPL7CFSJZ8Vl-BXufWPfbDYLX2Bj5CTeLrXicprgSJazowOrn512oK9Lo8StgDhQv4KkXNJZPXtoLUF2egfxDD-onIp1D-llFPygWIAmM9lkZVc6UKkzd2VBfWR8TaQNB-kTCdPef04DXVpQ22nAd5D5o5xf9Bl4PnTzS-w4AlliaVyiHhyWY0rxECUhwpxa6-6zoqIOqtrrMBMZRJeGZJ5PC1MnA3_M7iAjNQkXpUmdnXZAH33DRqIjaOh6XzvAKTkdbluFNKaq08d0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد خلیفه امروز عصر با حضور در ساختمان باشگاه استقلال عکس‌های‌رونمایی رو گرفت و بخش رسانه‌ای باشگاه استقلال پوسترش رو آماده کرده و فردا در کانال و پیج باشگاه منتشر خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/26275" target="_blank">📅 09:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26273">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZVNy12ewHbhCUdaC1vp6SCeub9gkDCqyO8dxvnt-_DtLIPhRzALXi7wkfaqM9DIqwhW3JcKXAIPDCBt0svN3T-nJHG7fUSGWSHtx6Hhx1g0YN3cq-1p4PCpaFn9XGkAtS3HsZ90abq0vTz8OAzjbWEHMe7gOsN-I8NU5yB-N2eEwFBy2dg_td3dpdvb4oOjcwaqPXUNGsbsLLleqXfVliM5bYJ_PiGWcBeO1iwvKFLcecYgYd1x4OH0wGfWe-QEWzZ3oUQDYbQxnSc8r3mifBqNhx7kqFqbNS2fVY6trjj1n-p7X0kr2prMcXQrw1zVK-sA6ImsNSBjQ4qcR108XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
رومانو:رودری ستاره‌اسپانیایی منچستر سیتی تمام تلاشش روبکاربرده تا در این پنجره راهی رئال‌مادرید بشه. رودری حتی دستمزدش رو به شکل قابل توجهی کاهش داده تا این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/26273" target="_blank">📅 09:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26272">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/955b39f6d5.mp4?token=CAvNzNLVKtv5m0czf3dwjpglNRex3Pmtr5wxgbDLbjsagTZN6vtm9ON1oQ_H8rLEMHAr2WMubGu0iQO9bcD4f4xlBrlq2Md3zaipE88OFsm7lN1dAQoLlhQhPihfmgptCqMWDcu1HjagGOXxLdCi_GxVKDGwv2JFynHK46N0swr6Z2lNaPuCakHgucURcezcO4twW5Qt-r7tX3axXBSLT11zMk5zv4JMR8jp28gfX-Tyv7NQfn8cVnQPz_4RLbgbe8v1D6NCvQ8_0atSiXaaZvvsvHZbzqS1zD3n9LCadKx31JbarmsIHDrPJmb5A8F_bAovp5tGA5nOx7Z2UNAnzYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/955b39f6d5.mp4?token=CAvNzNLVKtv5m0czf3dwjpglNRex3Pmtr5wxgbDLbjsagTZN6vtm9ON1oQ_H8rLEMHAr2WMubGu0iQO9bcD4f4xlBrlq2Md3zaipE88OFsm7lN1dAQoLlhQhPihfmgptCqMWDcu1HjagGOXxLdCi_GxVKDGwv2JFynHK46N0swr6Z2lNaPuCakHgucURcezcO4twW5Qt-r7tX3axXBSLT11zMk5zv4JMR8jp28gfX-Tyv7NQfn8cVnQPz_4RLbgbe8v1D6NCvQ8_0atSiXaaZvvsvHZbzqS1zD3n9LCadKx31JbarmsIHDrPJmb5A8F_bAovp5tGA5nOx7Z2UNAnzYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
پاسخ معنادار و جالب جواد کاظمیان به ادعای «بدشانس‌‌ترین‌نسل‌تاریخ» توسط بازیکنان تیم ملی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/26272" target="_blank">📅 09:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26271">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZLYPVuCsc3uCwoLqVGll0Va_CyfcGCSof4WqclGwHbsi_uJT_zpKjZPwewZ4i6GI9yIjrWTWndvQ2668gjMVB4yZ3au1OJnMfykbp3PpsDUkJ3KnF62k9g9CuxHK3WRTDRAy-0LCn-ASkjYvZLP4ZIUnQXedXUiIhdsSWpu_hLRIAz6wG0XN57T5segytFSgDC_3uzNJtqaJb1T3zS4kZBN0p6OCiKlnVkjfyX_T_MGwWYXdp6MJ_bK9C8nurYuy-SG_bpJMNYo-iqMHW3u4HFgAphGVahf46jzDV-brlU9Cq6J82B6ZDNMSa5V4jbQid0X7bibdwLUiFXHpnsLUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال در روز های گذشته مذاکرات مثبتی‌روبا مهدی گودرزی ستاره‌ جوان خیبر خرم آباد داشته و حتی‌ توافقاتی‌نیز بانماینده‌او برای آبی پوش کردن این‌ستاره‌داشته و حالاتنها توافق باباشگاه خیبر خرم آباد مونده. درصورتیکه‌ برای‌گرفتن رضایت نامه با‌خرم آبادی‌…</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/26271" target="_blank">📅 08:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26270">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab82c054c.mp4?token=pe7Yqk-x4bIIFz4csY8y53VRcjgAmRAOJfDLda5wZ1C6fNMliSZ5THEIMM-_doAUxE9DxLjkl5TTPEl7ocSdgkcB107OyZvXyZ8DBGxlV0FmaPxwSJ_aKYMoK6KEWl6L5e1zIw7f61ijrucG9nr42TE7To6bJ2DcrMwQDjlpdcKz2q4HiCBE2LrljoBu8X-KiRlOi8sCzaPmBsxW_MMZqy3dvlN0gMUrZD1qb3RpUgfiI0y5mIaDJTN3nOBC1Ceq1RHHraEofQqXoxB7AD3qQ0XUpkxvXME7rcFV8vJRART0ywAnVY4Di6tBJ1TYDAkLwcoCwCvPjIn85Opf6HbnIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab82c054c.mp4?token=pe7Yqk-x4bIIFz4csY8y53VRcjgAmRAOJfDLda5wZ1C6fNMliSZ5THEIMM-_doAUxE9DxLjkl5TTPEl7ocSdgkcB107OyZvXyZ8DBGxlV0FmaPxwSJ_aKYMoK6KEWl6L5e1zIw7f61ijrucG9nr42TE7To6bJ2DcrMwQDjlpdcKz2q4HiCBE2LrljoBu8X-KiRlOi8sCzaPmBsxW_MMZqy3dvlN0gMUrZD1qb3RpUgfiI0y5mIaDJTN3nOBC1Ceq1RHHraEofQqXoxB7AD3qQ0XUpkxvXME7rcFV8vJRART0ywAnVY4Di6tBJ1TYDAkLwcoCwCvPjIn85Opf6HbnIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
پیش‌بینی پپ در مورد شرایط رودری در مهر ماه ۱۴۰۴ که در ۲۸ تیر ۱۴۰۵ به حقیقت پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/26270" target="_blank">📅 08:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26269">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5wlPFNd6oXaMHrDlYTIsb-mY62t29f3j-YlqfLJjTOB-cHjCgTV_TbWCXInmEUwuKGaRvzDTPREzSXfURdadlnnkcemCSEbILl6HjDtK4Wqh7umDkp53K-DaMU0kev8kJX_UApsf-w6ZV0xD0gJ7PwjwI7Zsx-liZwKSMN-Wu3t63MVbI4pRdiC-Z7sU5LKZ0y6-MDeu6egLY7AZmFb1E23sSpDoXfA2f-onNmcZvVtPD1UQyF7peAg8VVFLaHpfdPuf5Q00SqBMUrrbQYpr7dDXJFo8TejNIMoNcXNT7_O_fX0omghTIVaI5Uxc3TBmnMj4_--rGmTF3BIb2uW5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ رودری تموم‌پیشنهادات منچسترسیتی برای تمدیدقرارداد ردکرده و منتظر آفر رسمی باشگاه رئال مادریده تابلافاصله پاسخ مثبت‌بدهد. پرز بزودی آفر رسمی میده... قرار داد فعلی رودری تابستان سال 2027 رسما به‌پایان‌میرسه و سیتی میخواد اگه قرار دادش رو نمدید نکنه…</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/26269" target="_blank">📅 08:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26268">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRm0WPA8_GrpEa9FTZBx_ASPFwlVeLevO76Or60agZqVa-fmiG1cHQwlXPp5CfFkUBoFp6oqnaEHMtEmorIMXVs1X_Y9LD5RxTHi7GZmuI0C2XxMx8jdF-963SWuhF4RzbMi-0bOwMv8BKFD2b5GhZyO0RbPaasCzO4uHguq4wrppO85hz0BKigfmf-uXXmF-HeYjz7MYyUXvU6e_pwVfZIw_zjyey1TlGcXYNo7LzEGlAt0GyEAa3B0zsXYVPx04scT4aqXrSwnUeSCDqKUfujCqn_AjKnrXi6_ecf9zEJkUNEmnUgrvLumo0jqgFKy9gTUxrXicDcZWMDxPxJFag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ به‌ احتمال‌فراوان بعداز رونمایی از محمد خلیفه؛ باشگاه‌استقلال از مهدی گودرزی نیز در صورت‌توافق‌نهایی رونمایی خواهدکرد. گودرزی فصل گذشته یکی از موثرترین بازیکنان خیبر خرم آباد بود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26268" target="_blank">📅 07:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26267">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c41630a748.mp4?token=sgj_hfKU9DUGJQB3koSEXAwXb0iXPTDCVDwCjoxITcjzhwdeh5ssKzjlk7hRPl3WTGtbSc-843j5CSBEc_4yXjD2uQZ8z9AXp0pG5tLAckKn1iAGkUqxXMG_m6qbsoP3-ezSxEhNvdsLazNxThZgpQ6eoU_wpRe6CKQ_fXJpIpbpZ95rWL5mjVm9lSBxEtyENEFmWMA6hlMQVDlwdiHPzRNgSlhDT3iI3UahmQDvwUeJ5TlvbSmdkTLt6bTA9QAkzt2lyWKP2wMayTCjNnwSWAAgFtsaQYs-wsk2AaZO-KhkjyrOsLwpEmxkZPXWKuySChEsIBpn0enCjabU6LcRwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c41630a748.mp4?token=sgj_hfKU9DUGJQB3koSEXAwXb0iXPTDCVDwCjoxITcjzhwdeh5ssKzjlk7hRPl3WTGtbSc-843j5CSBEc_4yXjD2uQZ8z9AXp0pG5tLAckKn1iAGkUqxXMG_m6qbsoP3-ezSxEhNvdsLazNxThZgpQ6eoU_wpRe6CKQ_fXJpIpbpZ95rWL5mjVm9lSBxEtyENEFmWMA6hlMQVDlwdiHPzRNgSlhDT3iI3UahmQDvwUeJ5TlvbSmdkTLt6bTA9QAkzt2lyWKP2wMayTCjNnwSWAAgFtsaQYs-wsk2AaZO-KhkjyrOsLwpEmxkZPXWKuySChEsIBpn0enCjabU6LcRwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
صحبت‌های رضارشیدپور مجری‌سابق صداوسیما در حمایت از عادل‌فردوسی‌پور در پی حواشی اخیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26267" target="_blank">📅 07:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26265">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WKTEYnfYTKLEAqg3KzR5I4_CBeGQotohlBt4hRQVko0bPMmasvpnsqXHj5uq8Oow5p0D99W_gKf8tmVjcqYdEEcaGevIo6v0MNkX0bGOV2S67Gj0Pq2dDL84VMOYdPyZMKeMppTn5f4gcQY2UOztqviZbZpXnEW6fla6jPvXFGeR0aPtHmd9wLxNkkRgfxt2HKGFpu3ihWvtgTvqQx3oslrKqYbl0vly3PvVj1gILXW3HAOU6gPOJMsFAjhTqdQRxRBsv0TPADZUBApidkVJrUjg2GOw0OekOlp1DMBol5uRYD3O1Wx-mtEca_BDFOM_aDt9MeL2b2Fbry-xSCiflQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lCvQ50ZdPs3rJrFlZXzLwf_Jpm7xmx0y_9z35IIkq2sVjC9HWsBRI2ZQ8vX9t81wuPF52-chFR5pY46bqvVTcsW1KLJu1g7-mA5YKdeh3crIsIqpY1AY6vPk90_lH4a2XAq3Swvl4_cMgJxFR4fH860nEIVhhF3FD4LtaqFjRAgM0OIKPHsD8Vimlib_cDN4B2SULcdAf9C3d5ZBolLMDRoHuMPmmAyYXid2pBd-1-TRkhGZio1TDp_oNI0Gkh746_cqEO3TQJjoaDpZS2yv9IMp4-Jp330os0p_hMh11J5iRga6W_QP3p7Jy_5er_7rmgPxqSAAi-pARL3pk3lGrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
اگه بخوام یه آماری از لیگ ملت‌های والیبال بدم بهتون؛ ایران بابازی‌که امروزجلوی ترکیه 3 -1 باخت درمجموع بین 12 بازی 9 بار باخت و 3 بار بُرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26265" target="_blank">📅 01:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26264">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-Ew5uGkTu5s-PSwI00O4msN0e3tfHAyrWzvGX0BPm6XmoMu6b1GNiI3jKZoHTEonpVQlbdqAhUZKImw5J0IVa4HR8gEAJZQfPCkb42gzqizyvnIWWH-EomoHEzx2CmDmqO242KIGr83CFxi2SNRGasHDspnpAV19sL13nVtWzxVFH_fMqvrh1LfYD_whwgDWK7315qG6abUl6LUV0cGPLG2HctAGvdrUCraf6SaDSgXDRHPtU32-UWBvWygYgCnXEHSKuOZOz4Q3EHUs2ccxGGAfUXywow60tGU34ir5CnZaD9pGOMU8BZxvDj0oRPKZof7K6H7Vje8s9c5az6xcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رامون آلوارز: بعد از ابراز تمایل شدید رودری به پیوستن به رئال‌مادرید؛ حالا پرز هم بعد از مشورت با مورینیو علاقمند به جذب این ستاره 30 ساله شده و بزودی آفر رسمی خود را برای او ارسال خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26264" target="_blank">📅 01:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26263">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6052d2abc7.mp4?token=ES_y0fd_jz1ULZnr2UPbpl4wpbl--GzG6PjUeAY3XyX3YAcT6ZOtUHDNZxPwdXFoqklhbTdc-xqBpp8Tww5fj7qrlLlIMu-sEUl_1SlYwTRG3-yhKRXoC9dT3RmrlDQRNHUHuWXdP22eLZ0qrE9PhMQWIFbJrq-aB-XmzA0YWXzzzJshtYEsNGU5_Va6TVjz17yGBFbRO5xE_h0g_kmMu3pXKy8D0E9FOCyzu5y4VoQbxJs2Fwfj32SemQQpF9Nhka9bXyeck5zqeKxe5dguGh_805kWxkZg7DXUisYQL_t8G_sQTetlY6IrZlT6EAXXE6uKBC9AJouT465xf1xbkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6052d2abc7.mp4?token=ES_y0fd_jz1ULZnr2UPbpl4wpbl--GzG6PjUeAY3XyX3YAcT6ZOtUHDNZxPwdXFoqklhbTdc-xqBpp8Tww5fj7qrlLlIMu-sEUl_1SlYwTRG3-yhKRXoC9dT3RmrlDQRNHUHuWXdP22eLZ0qrE9PhMQWIFbJrq-aB-XmzA0YWXzzzJshtYEsNGU5_Va6TVjz17yGBFbRO5xE_h0g_kmMu3pXKy8D0E9FOCyzu5y4VoQbxJs2Fwfj32SemQQpF9Nhka9bXyeck5zqeKxe5dguGh_805kWxkZg7DXUisYQL_t8G_sQTetlY6IrZlT6EAXXE6uKBC9AJouT465xf1xbkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26263" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26262">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ea272dc59.mp4?token=BzWCbRqlqBcLLH1h0AMxXCaFcXHO5Q4PTuBzee0aBumRjaMBiqmsb3j30wbMeR85TzmpDembSncvzNF2pj5VtanRSknOMzqlPPBuONWhqtBcUH5tmVuS9nLTUdrce2WzWiztPk997LRYwe4CP9QKE4lx_B60bGD4izbg57GVTliBTHe1Jk23-FMjgPtVat7KZOHd_eniKqXf4X_MnMG079qBXu6Vxunp64NN8IEbNJapltxEL4hrRgUVL1jpR6qqLd6uvsJINd4NQtpJpxjtHtQIEMjA7o7rEfKO9jqAoSGEDpINo3jRrsZiE222-tvOUWTiOUA8MOej23xpPh34Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ea272dc59.mp4?token=BzWCbRqlqBcLLH1h0AMxXCaFcXHO5Q4PTuBzee0aBumRjaMBiqmsb3j30wbMeR85TzmpDembSncvzNF2pj5VtanRSknOMzqlPPBuONWhqtBcUH5tmVuS9nLTUdrce2WzWiztPk997LRYwe4CP9QKE4lx_B60bGD4izbg57GVTliBTHe1Jk23-FMjgPtVat7KZOHd_eniKqXf4X_MnMG079qBXu6Vxunp64NN8IEbNJapltxEL4hrRgUVL1jpR6qqLd6uvsJINd4NQtpJpxjtHtQIEMjA7o7rEfKO9jqAoSGEDpINo3jRrsZiE222-tvOUWTiOUA8MOej23xpPh34Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بجای مانده از مسابقه فینال جام جهانی؛
لحظه بلند شدن کاپ نمادین این رقابت‌ها در وسط زمین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26262" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26260">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnsMc5xwQ2zTNs8Lqr3anvq8KdQDEu_pYIhMyIkixdx00V0tCuy9n7J-zBBW3T4OOZQOYC3JB7xgLv5R_TLgksYvIFK2RLsjt89Ej3spVpY15fgO-m8m0gKl63-d_nNKDyrCJ-9ER8r4nPoLS6egpDKs5CybC_uydnqOkUoQOSM4hF5BGW6lth0BA83qNSKMFtPfOlNDd1ntehazTdg2fLz6ftz69jdBnvhvLnBguzLb3KkwiRrTsgpriSbhOfo9oRWxCLsg7DI1vm8YM1D-fzGydwiNhji01z3F53FxjJs9Rjcwc17HJhmkeOFcycL--U5g5PyjlUkJ886nOcfV7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوری؛ رودری فوق ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی که بعنوان بهترین بازیکن جام جهانی 2026 انتخاب شد آمادگی خود را برای عقدقرارداد چهار ساله با رئال مادرید اعلام کرده و به نزدیکانش گفته پرز بخواد میاد رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26260" target="_blank">📅 00:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26259">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c47a31e55.mp4?token=C0vUxMbBti-P-onlrnutorbQojywm8GGwyMOESCbv2f4azaqdKlfT_lh-EQQp6Kl1C-oNmnEq9Uyz0IU5zS1Lfe7Bi05DPt1HDZjFyC9WzLwMtNKU5TNyHET9aa39cVcvQJ3sqNdtvyDIIlvBqFDSxGyl44tEO9g5wbFfRp4sxNvbBq3eqNIjbdxL3j7RHIOU468YZdSpaX91S7_jxGUsR38q0dRxbv41QTJapA-Ky-eu6aKJVWD5y-s-yXIOzQq1LgreUzFcuFtLVcHAuyw6BVQ-SDcV4Rc_ZODFqb-mjI5NQUaZN4RJlpVbJdnhAG8hpyXW7GsPn_rVE3ln30Kjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c47a31e55.mp4?token=C0vUxMbBti-P-onlrnutorbQojywm8GGwyMOESCbv2f4azaqdKlfT_lh-EQQp6Kl1C-oNmnEq9Uyz0IU5zS1Lfe7Bi05DPt1HDZjFyC9WzLwMtNKU5TNyHET9aa39cVcvQJ3sqNdtvyDIIlvBqFDSxGyl44tEO9g5wbFfRp4sxNvbBq3eqNIjbdxL3j7RHIOU468YZdSpaX91S7_jxGUsR38q0dRxbv41QTJapA-Ky-eu6aKJVWD5y-s-yXIOzQq1LgreUzFcuFtLVcHAuyw6BVQ-SDcV4Rc_ZODFqb-mjI5NQUaZN4RJlpVbJdnhAG8hpyXW7GsPn_rVE3ln30Kjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏این‌چجوری‌هرروزکل‌بازیارومیبینه‌اصلا میخوابه چیزی میخوره؟ چجوری به‌این‌سرعت جابجا میشه؟ منی‌که‌میدونم از اینفانتینو دو تا هست ولی نمیتونم ثابت کنم‌. مگه‌میشه‌به‌این سرعت استادیوما رو بره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26259" target="_blank">📅 00:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26258">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnsOSFTpnheIMnBLHywXpS9hhNMg_cixEbFXmJiutl0WtOMl-LvGNIluIKL4EDK3ba0HQzr0E1I8TZ9Ji1YA4tQpeteflBdDpUy0mz3LI2pmWyEWXCUbXS3a1EQxb9DrmGhJeXaTWTLEetZ8_fnqkSmimyGD-Y6Z1Oqi-TiASbenOWoIthaHsDr640lKuTsXCCEwn4rWpQ50TjgKY3_daz1nzgMjTa22GQlntdXDZVuHzlKezgJQPnXW6a9YIdq8qaWkagG3EE9n_Q0j9S1Ep9OBXC8oCuvE3js1fYl-S16uAAJpx_isA254w5Rt9o25mj_H-q4CYNF7hgAOS59Yaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
سیدبندی فصل جدید لیگ‌نخبگان آسیا اعلام شد که در آن استقلال در سید نخست و تراکتور در سید سوم قراردارند. هر تیم با ۲ تیم هرسبد بازی میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26258" target="_blank">📅 00:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26257">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxjQBOzVyOqJ5dVCBznf_Z0qUqUuG0JH7m3ZiXssyf3zmez6OWEynd6VGczs-TWC5rrwXqk-UI_3AhcZFPrDQ3kEkstFB_tTmJfUpAlcIVzTvfsWNYdR1SFndpoTWWSMFQdKkeNehuBScB1UEz5Q926x16JK4PzBtRskBH9f9kQJ_19IHaIdW_VsugyeSY1bppQAHV_ATM7uesUa2B6gHGsC9vRDTqAlZKOE7fmUTBgScuQJzOZS_zXR3sOtO-kNiWLI4qX9SzuX8cvsOlrATP83SBFRMVBFMI_xKU1LzY78el_EAAnANHwXM9yGIjuO6s4pHpPilJExfkLhr8F7Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعداز اورنشتاین؛ رومانو هم تایید کرد؛ مورگان راجرز ستاره آستون ویلا رسما به چلسی پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26257" target="_blank">📅 00:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26256">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJPIW0F38-whcPbIR7mrbFokbcAywKaXyC10bpWaft46L33OVsx7meNG4aahHtXgUYYo7fLsL5RuSOd97cfXjqpLAyE7Kal9XZhjI_saWWqTykEssUsmyVKSJGkQyTsmIKEVL1NU3EJEGxdH2AxJmoYAXXFer-XVljUGAV2yPSODzl-7rInOnHjS0DhSEDFReyVaTi6QLjDJq00jYCmCPTZes-konqab1lskm7uanZK5h5wh8uu81fpvmX9B3PsoyD1s9s2ohatr4zFBmoYQV1UMY9uzGGFRTWiimSU3hDl6i8simJgsgv3jwQWwB30DQeSGkJ6NUlJMOsqlUwqD0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ محمد رضا آزادی که یک‌فصل‌دیگر با استقلال قرارداد داره برای جدایی‌‌ازتیم‌ خواستاردریافت 20 میلیاردتومان شده. آزادی درلیست‌‌خروج بختیاری‌زاده قرارگرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26256" target="_blank">📅 23:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26255">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPWN9928nxTwdUqA21wN3_J7sI9QTW43AQthOhLLJGbjEGxx9Cjy9UFMXMuhO69OrRm5WvG059RIFghx4-8z-vVBa0p5YwGRqU30zXc0-sVuA5-4Jybx5j9MEyWnlkIfkswZZHiS6e9WAbs0nphkFCHZqXye1s-u6Zh0YMAby4zEOd3q5WG-MryjnxJoGYjQPVJY1R52q7ycr6rpIlfts-TKx8JLJ1pgHcaXIyhcEHVoEgWsH1AQckdxZQH_rboRQs-NqhXDjLIBwhGwcR-GUv_GDSIiwGTXzmIlFvOLGdfwsXceE4asqQmVmiEL7wtGb5xt5LsjUP65PPZTD82HnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیلیان امباپه کاور EA FC27
؛ نوجوان و جوان ایرانی باید ۱۱۰ تا دلار ۱۹۰ هزار تومنی برای خرید این بازی خرج‌کنه. تازه‌اگه‌فقط بخواد آفلاین بازیش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26255" target="_blank">📅 23:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26254">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUEUlzevl4iUXt5ubwwiZW8WUNdTpuCD6DE1VZzvqqtjGa-01K_V7XJGK6C-1zge0dkPLwNpbFfk0xzA5K5y4JEbctwUvTm1vBJx9fCnirz8MdLMYXXNLZe8TQ202r77634LaKKZo7YnqfcjT-LzRbYwM3hmq7IMnxLZp2zpvlTGXBlgj1FSwlmWVPRLLUDuU7miW8dmON2dYPbPVctpI_vfN03tQBWKpeCnn8reYlo_d_RxpI_3vT_ExmmcEdaSQYq3lJLAP_2Ggb4clbWb6pdw62PXYDIz_AUonz-FUh5lCyKr5j_wkjJTV64EpvFoogcyzZRc3oG5iiy95vGQCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26254" target="_blank">📅 23:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26252">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42bce1c0ee.mp4?token=qCnViodlusH3AMPDQhXSllcvfzsb1WAMdDk51ZRI1z7IlQSEqvjAs1Ifhql7pn8dhHDNqjSXPT5BBIXYlB8WZ-TL0fFd_7T1XN8VyDWr8yedR6MGn7BxupTHCbCYvopRBGqHP5BKp4GL64IJ20m4ll3G_0YV36P62W9HGNRDbzKeBd9JS0XfdbFUPIGleqkLSMBKvPsBrpbM0tvhsQUD-5g_B--AJif7t0C_RQUeqsm6sL1BT8GUBlQmeJNvpXVVRIsghtaJUlmDSIBjtWK-qkUgk_mVmoSsRWel1gRwSVoRYfQlYHKHUVB97hBApE-btgvmPBfhTTYMDw99P-Dzag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42bce1c0ee.mp4?token=qCnViodlusH3AMPDQhXSllcvfzsb1WAMdDk51ZRI1z7IlQSEqvjAs1Ifhql7pn8dhHDNqjSXPT5BBIXYlB8WZ-TL0fFd_7T1XN8VyDWr8yedR6MGn7BxupTHCbCYvopRBGqHP5BKp4GL64IJ20m4ll3G_0YV36P62W9HGNRDbzKeBd9JS0XfdbFUPIGleqkLSMBKvPsBrpbM0tvhsQUD-5g_B--AJif7t0C_RQUeqsm6sL1BT8GUBlQmeJNvpXVVRIsghtaJUlmDSIBjtWK-qkUgk_mVmoSsRWel1gRwSVoRYfQlYHKHUVB97hBApE-btgvmPBfhTTYMDw99P-Dzag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویدیوجذاب ساخته‌شده از هوش مصنوعی؛ خوندن عو عو برای عمو ها این بار با حضور لئو مسی فوف ستاره آرژانتینی فوتبال جهان.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26252" target="_blank">📅 23:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26251">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b149394bb5.mp4?token=eeXCYa_9GlXfa2HAE409ZIpNslXvTwVJz50gpgRrKCl8rWtWnGqkRXuAuPuS0-Sk3PqLkv5IzmGs-jRUxKixcSvk1l2zg1x2cbJOszxMDAyI_eyxgUENCoPSlJKIJESF7IsIwpE2KQm5gbe-y-jFps2lTKHlTmnqtb9_m1YTchLakM5lQ_J4t2Y5GQxu9Vgc6JMgcOHrLHWhE5vXtOfiiIT_hj1UeI7uNOxqdGyq01ipboDitaEgORgMjTEZPlHylXSzJMEjxFqTBzEIbDoexotXJT3dyJYaEMWCbrCELCHGVEhdcy_IslZGgrAMC0DVG7GqWcUXfZHgPQxpFNvlJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b149394bb5.mp4?token=eeXCYa_9GlXfa2HAE409ZIpNslXvTwVJz50gpgRrKCl8rWtWnGqkRXuAuPuS0-Sk3PqLkv5IzmGs-jRUxKixcSvk1l2zg1x2cbJOszxMDAyI_eyxgUENCoPSlJKIJESF7IsIwpE2KQm5gbe-y-jFps2lTKHlTmnqtb9_m1YTchLakM5lQ_J4t2Y5GQxu9Vgc6JMgcOHrLHWhE5vXtOfiiIT_hj1UeI7uNOxqdGyq01ipboDitaEgORgMjTEZPlHylXSzJMEjxFqTBzEIbDoexotXJT3dyJYaEMWCbrCELCHGVEhdcy_IslZGgrAMC0DVG7GqWcUXfZHgPQxpFNvlJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو آخرین قسمت‌ویژه برنامه جام؛ خداداد عزیزی وسط عذرخواهی از خیابانی با خیابانی دعواش شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26251" target="_blank">📅 22:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26250">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFANXUm04LlT-gxEevZWZUiNSKk8nmkvjpsLBXDO60arp0lFJmyzI3REZqbZXJ44U8UGUrLYbopl8Bm2zpV-HlikqYg4xBGWZlVSv1Wzv26NifSOLMQ7qNwWxMb9ncLgTYaD_I6vo9WMen1S-wOmAzTQZ4bKfb-96KxjlUkx1AlTmrUBMU-zQ6enZRI6rAW8IXK0HhjGuMyg0qASWGrvj9jb8pwz3BW1A1TG2i9rsyfD5Pikp6dgxQF9bdKMrZH3ZY0BBTOUeZlIUxuV_jXC-_jIaLdN9dUgf7br65GzuQFUnPixsBp1RtlIxtAKmdsIXf0_0bBvI217Ag6bEj66SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ویدیو باشگاه استقلال که به استقبال رونمایی از محمد خلیفه گلر شماره یک جدید خود میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26250" target="_blank">📅 22:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26249">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2d1e4b083.mp4?token=e_mEmnBV0lERxiLWlme7t5v06_CGHDZiVM5IicqUXKFBNhrD3Wa3KT7W7LtaKb3ZAyO6D9gZhQ0NZ1sYpberujPar-0z-PnjtwIQ-iyOkla8Uw6nbWTJLzqySO7RpYFt94p7tib0uPeoXU_R6-KkEp4vqAiwl2ERApEn2oo71WxfYeDqzMzkyA-TUSozZ9daU0uaD1-zhjftUVZrYyIZrbMexVnRXk2V4kgL0EGsYHupR2BSZbd8UQJu5Fa6TX2OeXRLDmhZEvWq67mvwHun7E-1G1IRQb5oM2GVIrqLY--jr2x1f_oisnrDaf0zDG80gZB4QRyTH0YW21NzWXnEuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2d1e4b083.mp4?token=e_mEmnBV0lERxiLWlme7t5v06_CGHDZiVM5IicqUXKFBNhrD3Wa3KT7W7LtaKb3ZAyO6D9gZhQ0NZ1sYpberujPar-0z-PnjtwIQ-iyOkla8Uw6nbWTJLzqySO7RpYFt94p7tib0uPeoXU_R6-KkEp4vqAiwl2ERApEn2oo71WxfYeDqzMzkyA-TUSozZ9daU0uaD1-zhjftUVZrYyIZrbMexVnRXk2V4kgL0EGsYHupR2BSZbd8UQJu5Fa6TX2OeXRLDmhZEvWq67mvwHun7E-1G1IRQb5oM2GVIrqLY--jr2x1f_oisnrDaf0zDG80gZB4QRyTH0YW21NzWXnEuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه‌ نویی‌ گفته بد کردم ایثار کردم!
آقای قلعه نویی‌محض‌اطلاعتون؛ «ایثار» رو سربازی کرد که تو اوج درگیری و جنگ، با وجود همه خطـ..ـراتش پست نگهـ..ـبانی خودشوترک‌نکرد تا شما الان راحت بشینی پز ایثارگری‌بدی! «ایثار» رو اون پرستاری‌کرد که توی اوج دوران کـ..ـرونا با وجود خطـ..ـر ابتلا، دو شیفت دوشیفت توی بیمارستان‌میموندکه‌انسان‌های بیشتری رو نجات بده.. «ایثار» رواون‌آتش‌نشانی کرد که برای نجات آدما وارد پلاسکوی درحال‌سوختن شد و دیگه هیچوقت برنگشت‌ آره برادر؛ نه تویی که ۱۴۰ میلیارد تومان فقط پاداش گرفتی. حرف نزنی نمیگن لاله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26249" target="_blank">📅 22:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26248">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8899308b74.mp4?token=CNBUUrS2AHUR4ajPT-AN5JuPDPuuROucyZxMgN4_7twIMMp4iWkuEWThE1UPcSzZUKSvUUeNAx9Lp466gEccBnpUJgEajanH31oNo2-MBmgIwNwivPF2P75ch-rhBhE_YSEK40lrLRr3PqOmS9WvLOOV5QvibMDagqfLlFfKP9FkKE7hgdLoBPmEfz3hT4tf5lowvIEeMRepdFFru4bdeha8jXzzbJQyyYfKujl8vk7eBg--g5kpnJUwise7ncd4bx_l0fUexa1-_x43aF60AGlr4xnCRSFTuKOS2TII-M6sQkvHvQYVe9Y44sk1vJzvLFed-8oY8TnLV2CB2ZdbfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8899308b74.mp4?token=CNBUUrS2AHUR4ajPT-AN5JuPDPuuROucyZxMgN4_7twIMMp4iWkuEWThE1UPcSzZUKSvUUeNAx9Lp466gEccBnpUJgEajanH31oNo2-MBmgIwNwivPF2P75ch-rhBhE_YSEK40lrLRr3PqOmS9WvLOOV5QvibMDagqfLlFfKP9FkKE7hgdLoBPmEfz3hT4tf5lowvIEeMRepdFFru4bdeha8jXzzbJQyyYfKujl8vk7eBg--g5kpnJUwise7ncd4bx_l0fUexa1-_x43aF60AGlr4xnCRSFTuKOS2TII-M6sQkvHvQYVe9Y44sk1vJzvLFed-8oY8TnLV2CB2ZdbfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26248" target="_blank">📅 22:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26247">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tq2nGF0m-YmkR41QU749L2Xc25VQQQ_gHCMGOvLoxgsOmcNhWFDl44jD-M9_MwsvbuOF_DN3PlfWqEJCKU9ymS5VV0XcVSPt2WoP6S9G-AdaSCzD_nBUwPeOGpbP3JcDjJCoRRQdM-nx9xZTymeUfguHR_iE0AWwkoJwGCVdIwtDOR1KTf82YcOtyERn1RFMcXw5RkoHDWCLh8qvFpEsHsd7h-rbGF_W7FeLrjXQRbyweezkb-upDMd7JxXeEZTGiYVWa5U1kJjPMNTdy9TPXeB_4P_9-a6UvRV7X6J0WZLe2wjjkgJB__YgG2JbYR_Gy5vDF7iS4hOGfubpN03ApQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛
برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26247" target="_blank">📅 21:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26246">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXZc9CK0Mf-2Dk4tuq9Yiu9ZWuB8oa1f8iJoTabX8UxZ_luf4yyoZpcwrvpTcEqI2sx7EMxnec6RWsf2K1-V5ilQQtubfmLC7TIrd0URcQT7WNr8vFZ-7Tkqm60YVuGJXSD7Gseq7az2q_Rmd-dZPSk2cne_TitnXNDTVsCA9Gay659SKrjBAFInAgFunKI37uAD5IXXJYJmcxQ_THjI1pdKbfBMw3ZpmCL9EphRG5MRz0ELkiTEu1kbJASgy0uhM_7CEmKU0-IdQYQn3yRdL5H4a9TCoQEakYAkeFRRbq4cxtl7KKYuPNuNfL2YboPZ3DA8gOBqVY2UD5e-um20QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
متاسفانه توی همدان بعداز شکست لیونل مسی و آرژانتین توی فینال جام جهانی، یه پسر نوجوون نتونست طاقت دیدن اشکای لئو مسی رو بیاره و از شدت ناراحتی ایست قلبی کرد و درجا فوت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26246" target="_blank">📅 21:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26245">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGDoOOERaUa9Rgpjxs96Di92G06nGVEofov4Tazbp_4XiHcWhZb-UurwsIctG23Lcoiz6ZU_sb9z4DHWA1C0OicAJyl2sa9h6oAX8CkAv6FegkEFG6vR9e6ZPTEO01q1HNgungbbwlBdQxDZPxOJJnABEFqGVKzeDRpbaecmDEbRLdDQI-X5V7RS7zp9_I-DY-QnFBlWqyQ42Cse9zX1hIj7tfZ-rBT_olToyJbwBTx66wplGH30bML_sQAWHLV6jBkbjQkZ4ZSK4QAC53AmCKpezIPM8QlS67bCNIB59AWILjAixXzfa1pbfTHRa1vTZvTasAirpgH6NESbfwZhUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇭🇷
نشریه گاتزتا در خبری فوری؛ لوکا مودریچ فوق ستاره 40 ساله‌کروات‌سابق رئال مادرید و آث میلان تصمیم به خداحافظی از دنیای فوتبال گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26245" target="_blank">📅 20:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26244">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/512d886ac4.mp4?token=qKWLrlEN035lObuMRoc1D6_WrbrGRAen3zylWPR3fNnEvYUR3Y3ObDxaqPb4Y65C7SRMPJevOg8_b3nuH-xGSc_Yp6F1P28Um4ylAKHSqX1cnstlRmaQkaMFuyIPQqaxnjK0Wyp5nFRQr-VghvsQhpX3nV7GxfJcZMFZkLX1ltrdG6c1FPpyqZL0r_8Lq4i-c3RTRr3mRrW7gVdkCiT2FW6ng_Vb7_znDWuTEtiMYdV9H9UytXhUdLBhqthZmf-H-UtY25rrWqVtD5s9w4AvjkGLb1L6jb5_yDtV0zGt-Nbqg2GlQV1ThJNmcKvXeGQkzYmmJ1iq37qlD1ABdMYLwRGoHOes6_KQJlHyR_Bf3lxyPWrY-jgMO0ncSFCX__Vv2jQy_dEEAymyTXQh-WBL8gET268OjsJms-Q7mQMBCV7qytzFyfF3tlH5oUiKChseZ7QHxQ4okoH6I8mRzIp-ZyGKq3SUjaYdJ2clkeRqsTfLwUX9OTqMmsI3erjOkBTIJ73gKc_z4pQz7P9GZANLttDsqRHIu0_Da92gOiNy58HOZ49nv2aYdGGptSnnIQkUzKKAPa4LTKgOlTF36RiaLgis0znk6bGz37fTzFoPZoLyG8zzRN-UP0MS-Lu0WJnFyLzZKCxMC-iJ3vXQCd75wowFqHxeb_h47dzP_PNz65s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/512d886ac4.mp4?token=qKWLrlEN035lObuMRoc1D6_WrbrGRAen3zylWPR3fNnEvYUR3Y3ObDxaqPb4Y65C7SRMPJevOg8_b3nuH-xGSc_Yp6F1P28Um4ylAKHSqX1cnstlRmaQkaMFuyIPQqaxnjK0Wyp5nFRQr-VghvsQhpX3nV7GxfJcZMFZkLX1ltrdG6c1FPpyqZL0r_8Lq4i-c3RTRr3mRrW7gVdkCiT2FW6ng_Vb7_znDWuTEtiMYdV9H9UytXhUdLBhqthZmf-H-UtY25rrWqVtD5s9w4AvjkGLb1L6jb5_yDtV0zGt-Nbqg2GlQV1ThJNmcKvXeGQkzYmmJ1iq37qlD1ABdMYLwRGoHOes6_KQJlHyR_Bf3lxyPWrY-jgMO0ncSFCX__Vv2jQy_dEEAymyTXQh-WBL8gET268OjsJms-Q7mQMBCV7qytzFyfF3tlH5oUiKChseZ7QHxQ4okoH6I8mRzIp-ZyGKq3SUjaYdJ2clkeRqsTfLwUX9OTqMmsI3erjOkBTIJ73gKc_z4pQz7P9GZANLttDsqRHIu0_Da92gOiNy58HOZ49nv2aYdGGptSnnIQkUzKKAPa4LTKgOlTF36RiaLgis0znk6bGz37fTzFoPZoLyG8zzRN-UP0MS-Lu0WJnFyLzZKCxMC-iJ3vXQCd75wowFqHxeb_h47dzP_PNz65s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇪🇸
🇪🇸
#فکت؛ مارک کوکوریا مدافع جدید تیم رئال مادرید درمرحله‌حذفی‌جام‌جهانی تا فینال حتی یک‌بار هم دریبل‌ نخورد. یکی از بهترین‌های این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26244" target="_blank">📅 20:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26243">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pt43oeGtEECsu9iEJ76w6L-_BBS8WxBME3A8otl6lTa4rH8AQIVbmhoYd-UcDu4IRwCujiVjOGFHOGAarQbEEX6pmdK1ITtqVQspryPWjsdRJiSOLPYRTTv6XfSngJXP50iewXsdinf7Vn-XSVuHmxM9b2mSczhSqY-ZewJGqFBkbeR7lDC4xz4hhDt25dXfXPn_wI9XFa7iIjLDnbF-jQVFIWmuelp8ME1DGOQd_9uSyXYFXoIken6kCsFt-ME55Ha4HG7w56Gl82EnL02OI48zN97ZBaHRetHaG9MjcMSgnIBDstK9g2snMAs6rsbbpp31tArA26aVYvLG2tq7lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/26243" target="_blank">📅 20:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26242">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqEexu369dYC7Kgct8mrStkKPxWhnZxn-5G6goY1GAXAlMOcTrbDvqn_0ZMDsycAgw-803PZR3f-5v4CORZ81eWHStxwOIHVhNPLW4jrvWCLsWurFIosEQ4LE69XMTLssJas4neojAa-afWH-YE4xPeGeDfhXsXl2LsegHK7YL1gw_CuDVglBRxKJLYe2uMzDbb-Kq5ccxnD89OxN1P4LaJOE76enBpWreLmzPPumHXsTeYxDNUAySh8jmU4qGHymkMkat3-k_UWB7QjAV_SvFLAng07Knypumiph74UT0fQzRUzkxNNLKrlqs12WRq68EqiwOQaXNnfOPIbdkOLtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ رامین رضاییان ستاره آبی‌ها ظرف امروز یا فردا راهی‌ساختمان‌باشگاه استقلال تا تکلیف نهایی‌اش مشخص شود. اختلاف مالی بین طرفین بر طرف شود رضاییان در استقلال ماندنی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26242" target="_blank">📅 20:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26241">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUQePDt-48sOWNvgggYWYo4e0Ny5QF20gK6MCPq7B_46Nu-Fw907FuYLls18sO3fRP0-1NTJdY7lb0NlltD2s-B4xxUsJIGCSmXZZDFCZk3dhbxlY2lVBcz9CoHB12Dm-Axu3B3yBluE9GMtL-RjuRiNkdL28lAatINC4or28OCy91rWyM6LzdshOFBvh6OrQKEkHhXoYFzqR-4PRYhPwSvr5WFH2duVCUMG_PbaZvgffIRr6v1R4SU35PpYcotTJHvjRnc8nejGiBH5u0VwMmkp5qDu1w0nQUQorTqvTAOBmxRnJmAM-5CrgFj9ToAdquIDZ3Q3S90kql2lBTrLGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/26241" target="_blank">📅 19:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26240">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1VOlXO-WXlKz0ezWBduNzugif-MMypo7-5xAAwrbuT4bR7Y_Jgy4E9NeZ2HppQ0L-FySwRedJzRPxyaQhJgf0m8Xo2yVOmDduaPNWAYR8xpSNKxNr3RQBTBJXosNy-4ZRPP7xyWK2Dz-yrqtQ7kAD9cytby-MFNnw0EaP27OCdrUtIfg_CmzYp-roanbo45MfKXUGeJ0GidaclbrFQNPeNe0lP4bc9BoTjvoPqE8XqGm4AjBW7NgV9Hy9O79qZVIilr6RfLwTE6weZAD4UICFwpd1tc5v1dKmiwF3VglOETBbHqAftuBbRGboKeb32yYjsMpu7oqYvZAqSitmpmvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/26240" target="_blank">📅 19:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26239">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUczqIJgy972VD4d8ReOgbA_1qAb9sgUrlgv1TLAC865Dp-9VAVLOU4D-5uKxqCVnbJtL8bsQ0zPXfOh9KQoeXW3zRiHn7__ECfi9tS0-qo_Mqdp0Whz4YNsbYNA-dnuYOrq_wVOb32Y6IWIBJh6IMLiGXyJZhZrqy8CHk0d_pSJGEohPHnkAcQj9FYLDil1opvEAYO-ZWuo_5QWfdY0H-g-0dtkAm-qdvbBGfkST94NRwPhE695Gw3jNu_aOC5S_08y3tTFwWbaTqIccMqvCA2Vr4-bg61NF9cv9exFyp25FGG4YV1ggj4uVW4514Q6iruwILEQ-bYX_7fzU9VJfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
تیم پرسپولیس امروز عصر در بازی دوستانه بادرخشش مهدی تیکدری 2 بر 0 از سد خیبر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26239" target="_blank">📅 19:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26238">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fe98fee7a.mp4?token=AC--MzBuA_2bd5zZ4rpFrsEm9YmZZPWkBm1M5WZXwqu7y0vIXpeWk86x33ImiOqazYAbufZE53R9VKyA-tWu-JTNvCmLQGgZjr7ZQ2Ppq8mOCxZdbk-QN1MRXF2mfjjVpvl8VO-naamFhSZDLQrUr932N20s6Ihv3QkD1nhbD6HCPVAjkhdsn8BsLiVn7d9DeOUEJfbCXsmIkr3fMv422IXrI4JNBVvjtC87UnTLMWSYzfwzPbo0xvgidvW6QiZdbBBJFGfR7m467PJgqGc2PLQ0Iv0JYA2qrrUInrjUknEjiB7loq6VZeeOK42cjU13pCmm8sxIQ4-cnmJbdtG2cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fe98fee7a.mp4?token=AC--MzBuA_2bd5zZ4rpFrsEm9YmZZPWkBm1M5WZXwqu7y0vIXpeWk86x33ImiOqazYAbufZE53R9VKyA-tWu-JTNvCmLQGgZjr7ZQ2Ppq8mOCxZdbk-QN1MRXF2mfjjVpvl8VO-naamFhSZDLQrUr932N20s6Ihv3QkD1nhbD6HCPVAjkhdsn8BsLiVn7d9DeOUEJfbCXsmIkr3fMv422IXrI4JNBVvjtC87UnTLMWSYzfwzPbo0xvgidvW6QiZdbBBJFGfR7m467PJgqGc2PLQ0Iv0JYA2qrrUInrjUknEjiB7loq6VZeeOK42cjU13pCmm8sxIQ4-cnmJbdtG2cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
🤩
انزو فرناندز ستاره تیم ملی آرژانتین: بعضی‌وقت‌ها واقعا خودمون هم از خونسردی لیونل اسکالونی متعجب میشیم اما او میگه من یقین دارم که‌دوباره قهرمان میشیم. همدل شده‌ایم که قهرمان شیم و لیونل مسی هم نهمین توپ طلایش رو ببره. حقیقتا لیونل مسی رو بیشترازخودم دوست…</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/26238" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26237">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBBsWgCVM1J4qYn0abZ8XuifIQR82l8nHjwUobLQdw2VF6SOIkuMg_9z-7V73eIoOueyPFC2mlcdKrSovR8ZZv9j6Vhp1Cu-C-g3FwlOvVHdKFYfnwIIBbL24I-jS7cK5GU2h2QuKipefLI0ujq3Tpe8cr6yA8W204SXyAnWbX4Uf_RsHwIzSKohvJ0rwe7lOMOSe71vsRFk92aG7TwbB6MPodcE6UfolJfIE92nKlj4QxGEAVkgS4J-d0BBPETNSf__ncZDxbCVw_lEhsabjSgGXr2Re2ECDrF0zqIBYkalMjcs8lAAI2TKBjyfBucVBbpWZpHzT0DYV6_B-TTDgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باشگاه گلگهر به‌‌درخواست‌ مهدی رحمتی خواستار جذب امیر رضا رفیعی دروازه‌بان جوان پرسپولیس شد. این احتمال وجود دارد که درصورت موافقت خودِ رفیعی، این بازیکن با پوریا لطیفی فر معاوضه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/26237" target="_blank">📅 19:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26236">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TjxMrEjtvd5NufZ5BIabHv0_uJtNoNdaN6y27Y4rWO2at8CU0a55ybdUOE00rlJXxm8oFQNjZnjCLppy5F25ZmmhUSayBe64u0h1rs-4aJV0a0yTbnVvpHje6k2F-X6Q2p9ZwxyOs9b-EvY7Tcd5smZf5N4eVi3qZjUMWzezo9zfazycMFE_Icul1MupEzacIeeSBY9ryNilT8ZJvn3hJx_QK8pB3cj7k4DWnIYGyNjkocc6xPdJxLUfuX3rrGUB37Q7D5-KzZ1sUNVhMfTslRVJvobMGXkDbeL_H-8MaaMso3Q0wN_u0ClgFtcGilQKw0-onplGWCFFzqNre7mlWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/persiana_Soccer/26236" target="_blank">📅 19:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26235">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDJiZ7qGl7bebz89KB8X_ZE_yVBQ7Tc8w_lfYd2K-ikimj0Mxex7RTmwigU78gnyb6jlqc6q5uqjTETSMVYC7X_EBQjUbg59QKwHk9ayhOom-OOnTRIXOcysIarzDaHGRFGRCC4OpZKUVBTu7fsta0SmCp-wWOINmLXSY4kVNB__4v6Ltlc7indoWYoRdIZsH1mG0XV0yvp-318m2-PXllP-009lOS3tnZTAEnIEkTRZ8BtBu43hVbSBEnBTn_rmYAnpbTRmLMcexA6GcceB6kC0G2aU_ifeeDY76yzesTH93U9rv20Y8Q6Z7l4WBSpa2XJ5y2z1hYNA5URKqzhEVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه پرسپولیس دو هفته پیش با ارسال نامه ای خواستار جذب فرهان جعفری هافبک تهاجمی 20 ساله ملوان‌انزلی‌شد که‌درکانال گفتیم. باشگاه با خودِ جعفری به‌ توافق رسیده و توافق با ملوان باقی مانده که باتوجه به‌فشار بازیکن به باشگاه در روزهای آینده رضایت‌نامه این…</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/persiana_Soccer/26235" target="_blank">📅 19:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26234">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59137224b2.mp4?token=G9KUTSFx6BmOEjB9Yh19gDKbaeOyK2CzYUdStZFnwNFq4fr3GgOwFUq5xsDX5_fkNw4Zw1XbDYM1vgjiB2J9ZBMmy1daYFk3eq2HVNEiyvEolL2drT_D8-yIAFfM8GysACzJrJgLn3lFtWaJ3LhF59P-U9RNynaN4lzMbeLgqErlPy7x7XrsqBfxsjOl13k1NfRR7_P1lkn6GeJD4lgE7i7mfZhB5QrJvk069yMw69kKrsvLXr3fhqnorQGqeGteN5JUxCyYzo-LWES9zDLH1027aGL2uu6t0NUv_7hCKfSAcWF1Pa0cAN5WiZ-UOZ4KT9NjOB4HwLFAeCBPm59J4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59137224b2.mp4?token=G9KUTSFx6BmOEjB9Yh19gDKbaeOyK2CzYUdStZFnwNFq4fr3GgOwFUq5xsDX5_fkNw4Zw1XbDYM1vgjiB2J9ZBMmy1daYFk3eq2HVNEiyvEolL2drT_D8-yIAFfM8GysACzJrJgLn3lFtWaJ3LhF59P-U9RNynaN4lzMbeLgqErlPy7x7XrsqBfxsjOl13k1NfRR7_P1lkn6GeJD4lgE7i7mfZhB5QrJvk069yMw69kKrsvLXr3fhqnorQGqeGteN5JUxCyYzo-LWES9zDLH1027aGL2uu6t0NUv_7hCKfSAcWF1Pa0cAN5WiZ-UOZ4KT9NjOB4HwLFAeCBPm59J4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
راز ساده‌ داشتن بدن خوب در کنار ورزش کردن مستمر؛ به‌هیچ‌عنوان سمت آمپول زدن نرید تا دلتون بخوادعوارض‌‌داره. مستمرتمرینت روبکن تغذیت هم خوب باشه بدن خودش یواش یواش میاد بالا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/persiana_Soccer/26234" target="_blank">📅 18:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26232">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d4MFs1ZQnIqcnWvzr3X3oo-CfM_gbNknVn4Iv4o3fXDZRzS3DiyxBVQnpiNwqDMDaSZi8xlLa4BGVZW56SCmfNNj6v-BFTfR0SAtGdB-SG0ANx373gKVumZpPvSQS1cDuQdhmQ71v9Q-MftuFlJYqdQ58pdzuqhVuK9VuKpQPP3l2Y8l09BNmss1JRz0etPHSuEFh4OHLaGuGlSkRLJ55sq0kfylDM4mBt-hB0e_bR-0LEuDK3p9LxFVBK7Ij9b6dCknl7qjAQcEAHNOup_-i_3DBYuNS9Jf_E0LtgLC7AxfEJtR-FDJmTj6Yj6CVQW4eEu59Mk4z9A2DiRHjTyQHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bJMoh67bGhtGlYW1dbdh5-nV2pjHGZStfSIsN2_4pBxKyE5E0BreJGIEoVxEABkiFsSx9CEO5-jkTUzYd4foLTwU7EpIGXSqSsXfTa4CjPgubD7EM2UYZtDCjdQ7tNdlJhkCUMNcq-AslU9BQgGK-gZfIHb3KBN10rUK6j1zZaTQe5ZbzfuLMB6gAisElapv5bMi1I6jSYT3eAnrThKbEfGIVuMLZYke7teVmb2SrhrpHaHtASviNoQVq7Cy5Y9z82FtvANGn0_ZbJvORYKyhbQ2ORTfEfY-fT_7Qh1Z6G5kIvTDVKk2YI6Ipk7h0Y4ScUbRuauVSTDpUvKgerdL9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
نیوفیس وینیسیوس‌جونیورستاره برزیلی رئال مادرید درکنار پارتنرش؛ بعد از ترزیق ژل زاویه فک و چونه‌ اش خیلی خوب شده، اون غبغب‌های زیر چونش برداشته شده. فقط این ریشی که گذاشته‌ قیافش‌رو تغییر داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26232" target="_blank">📅 18:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26231">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cs9UMVUSDt5uH65_WmUmqCYBXMeXkqbyVBLS9ddCim10PdKfmiWV8ZMB__dNmlaoLpcNguwSCgmCyjy8vgE9wPZK9auvO7yWRcIGpvZYPF6h1hkjNl2bUs9yn6pcc-hMTdFBPJ1kIk94dnENHW0TeVwNmwEkA04lBX4BijZyqeShSTsX1npXDeJOSoqsxg5uhZnRgrkuGN5FQoD_V515Hnwpdgyrekd4Bfy8IymsVfljuXQpN1AVQPYoR_CSuu5PGRIaY5cuOCzEetv-4CCODPRKfhPqViGovXVFR55V3Jrbq6QL1htpqa0gNTMBgnTgiHX4VeK2_T-l9mwAzaVl4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
تایید شد؛ با دستور مسئولان هلدینگ خلیج فارس؛ علاوه بر مجتبی فریدونی، محمود رضا بابایی نیز از هیات مدیره باشگاه استقلال رفتنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26231" target="_blank">📅 18:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26230">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXaP4egmmDVMC8Wha-VTDFiluyR6QgnOyBj1vlFrPS0ITP8yK_3wkspCnyeNv4aDyPgEE_mwdP9NhVWHZxg1qkqTz7tVtFa6pOdP8fem1y25e68B_hon4609LVJ3Y4cORXdb2WQoo3QQ6tI2uyHhXQKyPGWuj-S2KSFJmnJYp1XrLpNrcOjkbUm2PgUK9a-Ci-Z5aorlfx_IWV1dSh6q-3MbCCKMm_nuvG3bVcbyxO38JfoXZckKtYjt_x1D3HvPRtw1wr2g3V9Vw21CfQkyI4MpvRz2hET4nS4jrfQW9A9957LqxLxDKU7sVZAVYLLln2TsZ5u5nemD2giTi7urEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین گلر شش دوره‌اخیر جام جهانی؛ بوفون، کاسیاس، نویر، تیبو کورتوا، مارتینز و اونای سیمون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26230" target="_blank">📅 17:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26229">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IE8T0cGmsoAKje0TaT8Ros-xtWIFmH1Io8YqNopgSjij8Ldf6TJouddXGxjIJ8zNMBITeVQD34SD98d8Oknw-aoxSY2uBcXTwiGr2E9YuMFUXr44jbf_nRBqY_UTsV0yDw3WWqLGIgT68yijWnYf3qR4Fx6lCTfGRTineCTg8S_jR8w-lkoscrc9w7aGjwlpudRYqz1Bo9WecNugjrsXXjl6C4KvZWRYB4aFnkZeAgvu5uCnCJjDZlDPcj38DlTP1_EQPcNSVV01daEq1VVQ_XCvdD2dReRQGdmPGMgZFq-NcxqNH8W6GASxFeOKR9uq5Wf6mtLYaykAqRgDv4Vhmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت رده‌بندی فیفا پس از جام جهانی؛ سقوط ایران و صعود اسپانیایی‌ها در رنکینگ بندی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26229" target="_blank">📅 17:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26228">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3639cfb2fe.mp4?token=vGLpI8tL4QknxNB3BLh_7qUzC0mvG4wKWAeqSRHyL3gsJhfnIjtEZu33mQxtJuHsI0wK9tJ9-GGpXjhfrazI-9_WyqAy1YtDQzoKKM9VpWn5jUvh7i1nSnfOYhgoP9L_pkt3APHHkBMoEYcMfS23JaXX5V7fCp3-iiMv-0VJaxUsCTIQzD80-rs_8iONmfmaS0laxLXQK_s4nLE2HPz2-swv-HskClQJY2HJlVrcpTOP81xfmNwGZmJAZI7XJnC2y66WP-wSyIVcBgevK6ORZUg2H5G_3LbJ_gkXN0Ho5XMKEKiM35YXllHPItnl5Xplu2LZK2lofdGP6DsWLACKWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3639cfb2fe.mp4?token=vGLpI8tL4QknxNB3BLh_7qUzC0mvG4wKWAeqSRHyL3gsJhfnIjtEZu33mQxtJuHsI0wK9tJ9-GGpXjhfrazI-9_WyqAy1YtDQzoKKM9VpWn5jUvh7i1nSnfOYhgoP9L_pkt3APHHkBMoEYcMfS23JaXX5V7fCp3-iiMv-0VJaxUsCTIQzD80-rs_8iONmfmaS0laxLXQK_s4nLE2HPz2-swv-HskClQJY2HJlVrcpTOP81xfmNwGZmJAZI7XJnC2y66WP-wSyIVcBgevK6ORZUg2H5G_3LbJ_gkXN0Ho5XMKEKiM35YXllHPItnl5Xplu2LZK2lofdGP6DsWLACKWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بعضی‌صحنه‌هاگل‌نیستن امابه‌اندازه یه قهرمانی ارزش دارن. دفع‌توپ‌کوبارسی تو دقیقه ۱۲۰ از همون لحظه‌ها بود؛ جایی که با یه اشتباه می‌تونست گل به خودی بزنه یا پنالتی بده، اما با خونسردی کامل توپ رو بیرون کشید. این فقط دفاع نیست، یه اثر هنریه.
و یادمون نره؛ فقط ۱۹ سالشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26228" target="_blank">📅 17:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26227">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ec8c45572.mp4?token=lsbXYuYPktEjjYjMcrXB1en_63NKFrA9JJ2fTl45ERxoKYBr97JVTbkIlTEJI2GP3RRR5M27UeXD1thXCGEEXz0mqOh1Yp21VbqRKQBPNJe_oQZeNA0W8nBURNcRkt94CfFsRUHK5Q6AqGOzu5vhI7x-HvoK3yFYBPXVEeHA0qquluPAVrkxa12E1Z0UFvhQv8Vb_Iq4l7E-bieA4UbJ1KON8kEcNnk6ba073mV21CBYHPyUYz4ur7IGvui2Hsga5g9jR_x4CZQyAPS8GdIlnbg_7XPUSa7wRrYVndCT3pdGqpiaIub6FqL8ABMgMUtZAEmWO4h--1Elazd21djB6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ec8c45572.mp4?token=lsbXYuYPktEjjYjMcrXB1en_63NKFrA9JJ2fTl45ERxoKYBr97JVTbkIlTEJI2GP3RRR5M27UeXD1thXCGEEXz0mqOh1Yp21VbqRKQBPNJe_oQZeNA0W8nBURNcRkt94CfFsRUHK5Q6AqGOzu5vhI7x-HvoK3yFYBPXVEeHA0qquluPAVrkxa12E1Z0UFvhQv8Vb_Iq4l7E-bieA4UbJ1KON8kEcNnk6ba073mV21CBYHPyUYz4ur7IGvui2Hsga5g9jR_x4CZQyAPS8GdIlnbg_7XPUSa7wRrYVndCT3pdGqpiaIub6FqL8ABMgMUtZAEmWO4h--1Elazd21djB6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حرکات عجیب لامین یامال ستاره 19 ساله تیم اسپانیا درجشن‌قهرمانی‌شب‌گذشته؛ چرا یهو کشیدی پایین؟ یه‌درصدتوپ‌طلابگیری میخوای چیکار کنی؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26227" target="_blank">📅 17:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26225">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8b008c54e.mp4?token=te300zMb0lIOmqLAUDt6mKNzv1hCYaTIZok_N_YJKoFqnrqBvIlDhL33Eq85jJ8qKxWwPvjdQFpLwo-sGkvV3csebJEffOSX5_4za2Yud3qMQKS3YtxvywgIrhr7qtd_S6asLN12uXFjmrC72NJ-ffQo86c8YmUeDzGewy2HTRU_1KYaeydjpflvp3ct2fQY42mbbmyLbSsh3yN9vV9tnlMyVZBOqvvg74OS22y-uDIfJ19Cr0HsmVOhizEZQNfaTNP2lUIfshwFwj2dsGFBhfhTM6DkRGeOVsgFLTMyGQw317sOlXGnqGMV-WCAAnG5rRdm52WOfnHmKVrSpSaBUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8b008c54e.mp4?token=te300zMb0lIOmqLAUDt6mKNzv1hCYaTIZok_N_YJKoFqnrqBvIlDhL33Eq85jJ8qKxWwPvjdQFpLwo-sGkvV3csebJEffOSX5_4za2Yud3qMQKS3YtxvywgIrhr7qtd_S6asLN12uXFjmrC72NJ-ffQo86c8YmUeDzGewy2HTRU_1KYaeydjpflvp3ct2fQY42mbbmyLbSsh3yN9vV9tnlMyVZBOqvvg74OS22y-uDIfJ19Cr0HsmVOhizEZQNfaTNP2lUIfshwFwj2dsGFBhfhTM6DkRGeOVsgFLTMyGQw317sOlXGnqGMV-WCAAnG5rRdm52WOfnHmKVrSpSaBUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#تکمیلی؛قرارداد محمد خلیفه دروازه‌بان 21 ساله جدید استقلال پنج‌ساله امضا شده است. باشگاه بزودی پوستر رونمایی از خلیفه رو منتشر میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26225" target="_blank">📅 17:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26224">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSwt5AaKvEbmbD13PK0GLr-S2rlFUYH2TdOD2Ocn47tMUR-6LOE_lXLQqXirAi0MU3xazRcX3p-VQ3Ud1vsiSQS04rpQdOgaCSmipiQzpHiWw58vlmiQ3mh7CSjsuXP3Ye3ttsMCgR4VM0ZSwzMZy36lxLUvR0lnv9LI67r4nrHURrqOd59bgE9wpNbNRb0BsHLZWkuPpJEnlJ_5D7ICGptzbA9sMsf1ShpGJ1YpLnJyFwzMkfWjhUxqj1MYiFFz0XpuVdhX5r65fx0R1-lGFIu_lvnICUFqUZMK3mWylFTZg0GwbXGKcIpzByRr6feLCjxOrlEw4URejfA6eJDFXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
◽️
👤
#تکمیلی؛طبق‌شنیده‌های‌رسانه پرشیانا؛ مجتبی حسینی سرمربی سابق‌تیم آلومینیوم اراک که در روزهای گذشته مذاکرات مثبتی رو با مدیران فجر سپاسی داشت. امشب بعد از جدایی رضا عنایتی از نساجی مدیریت این تیم با او تماس گرفته و صحبت‌ های مفصلی رو با او داشته. حسینی…</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26224" target="_blank">📅 16:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26222">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kiFU-tPZAySPVxMQD2e22g8q6_Y9_ipEwlfWNPOzMm7xWmAoykq8LaM2nZUHH4qmZUv5XcQ9VYelY6nsLO5lFJFz5NmqPWE-g8lhcBgRzNTLSjP5XwRkXBOwqjWJJoX_ZbhqwVHHpPacUMDIWIH-ixJBtF5NLSRRVOUACk3fAFZudGJDd6THvCHpDWUR3n-ce0Iqcpk-b4XLifZMSNA6ES6jRu8SdldJ_1l0GKTSCNUt_-am-XmDLpop4kPYUQ05-DFmRRbTcBZFLxXnwPCZY73OXT0y2ySqdtcPQkyGBd8ypKnoQ5BA-5QIQAP2enUBeypddxzV4kf9gqbgd1JgqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AURUrJUSO0no64s0I74sif3cSs0lI1GPmYI7EyeWTraUvsfxgDu2rC_Gq9bSQgNwvS4SX9iSl4H1KO9G7LTHiRLRDOAQul9_2QhM2GITnCtY07bMT6E0VfTMcUdqoQbtItUMXSUUKmArIM7z-iM_Br8uCkTSZXQ1WsO8QY0c82S-fZc_kdudIHVeu8rw3aNLxZVcIzJ4uMeoXm9WlDgen88swSMcF0Sl8cktibX3TgmLGnN-NieFbt7yuNEQkv1u4q3OPWS3TKQujOT8uUndzLEAUGZs8NLmwnEfhuZJsZMxnomcX_IjyL2n1GPW7CnRDAYemAvRCpGoDWvNrKqyVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
خواننده‌های جشن قهرمانی تیم ملی اسپانیا بعد از موفقیت در تورنمنت بزرگ و ارزشمند جام جهانی.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26222" target="_blank">📅 16:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26221">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPaevpZiqmM5rjimYw5XcFGsYN2yj7RgXCkcJFgiW2d0vM0Q19pP4qBM5xjBYXOlo4yVERxVBPUXpcuyUC7aFDDrn-ccMPkTRi2kbZwd107xBesaKl_pXNKUgsxZhkxgYRbSIp41L9ds_-SQNl5DRc3AXSuo8pYxa4Vy6acVfpiCZC-LJAcY1xEOZ5l2ovqE-TNM4Qbui5VmyPPtd-_l50YwNOS9Pdx34c2qajF2BSn1veKc2eVVaIw6dZ7KWAUUzndWJFNdnmCHHl9_F532eTfnObSXm7hrmSraf5ZDXOY4PlSAwfq_MQWd4nqElzTD0mv9LJMu3eMIE6Hnarp8og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26221" target="_blank">📅 16:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26220">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKwIyGq6USTve6EWky-PHRQ4nPZvgkZK__7WKE5MU3Pp4Itn3LVNnIObNSCZneHBH2X0YPIbDy8kxdNNRkpEXYIF3C3CwqVYsEqCX70YoGnpJTRqUgEvgS2FVN7agBYYeLBY-6CjpV9hhpNW763TKxcPKE4FtXMJiAIjXfB1lWUMX4jFcm9mUIabOllDbcBKpCugj9YHbR81z-0c4qyMUUsq7OywsJ1YMahMWTbdOrySpX3T1StzgywTEjIUpMJ9bpOHFBwVRI_uhLvtrQ19K5N6sC1nqx2IvHWDsffM57Gdhtn88Mazb5FAdwhvIxs-4kVprWf3Aq2uXs7XqruDng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
درحالی که با قهرمانی اسپانیا هیچ گزینه قاطعی برای کسب توپ طلا دیده نمیشود ، فرانس فوتبال در آخرین‌آپدیت‌خود درماه آپریل "عملکرد فردی در تمام مسابقات بزرگ و مهم" را جزو ملاک‌های مهم انتخاب برنده توپ طلا در سال جاری اعلام کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26220" target="_blank">📅 16:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26219">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZVs6t-3AyCnK2jAvXHU6jqBHBVjm_ftfM9PTERCHRpLP_-kinfR48o2QESUyf1qxoAyFn_RzFIY7jAnACT921QQk-QZ3IGdKbSDbKxjUC38-2DSpQlDVLbgkHCBQFhnuDN6JH2UQhTQLRhlDbEvCYwbJLmJrDkKAt3cVDxgNk5CsKpovaOeplqkK54fe8tEu_raFjYzG7s9cJT28bphLtMHI1fd1mQTmuwt2LXMhfftMp2rlthd519pvtYInPTRQMthaToEKWMLPtzI4weweBtPbosQdmWKPmVU5kWf1CW5C-e3Jv3ivGa3NQHImRtwsEvBLRlfck7Am8bWPAQQ_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رقابت‌های‌جام‌جهانی 2026 با 655 میلیون دلار جایزه نقدی، گران‌ترین دوره درتاریخ‌فوتبال شد. 50 میلیون دلار از این جایزه روفقط اسپانیایی‌ها بردن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26219" target="_blank">📅 16:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26218">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBc9ZNVqpvsdwPa4LDlaCMUmvJAdLwXTE9bxpqSiLeFB0Y1fEB2t4ZZRS05L4y0w-TPYlTMpnmDX_pPDWkvZ1Mvx-esyJyot35Nv060R62A8iM4FNR58dMwnGD8QzXnZrgVI4ddOhvs50rExieJkvl_DzEezRBBBvtf_mOeW5HP0saWXM6ShEVZ_OCR71pX3KR1PZu1mR-eK_yTzcWWRxBE-fIUBDXNqLsVwgErvjiHQfJvOYhNtugo8oWqlQeNWIgziQq5mF9Ku1D9pjwaDX4pDytbNehbA1K0EGLU22D6jx9s87SG4fl0LsqF0uqRenfX0yPjKNM4KFUD1-JminA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
محرم نوید کیا سرمربی سپاهان؛ علی کریمی هافبک 32 ساله طلایی‌پوشان زاینده‌رود رو در لیست مازاد این تیم قرار داد و کریمی به زودی با حضور در ساختمان باشگاه قراردادش رو فسخ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26218" target="_blank">📅 15:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26214">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRQ7scWmFawJdv-xxUfi9_J_LJm1E_QA8_sXo2UidU0dPKTsUV8T6fy82PU2ag8PFg9vgAyGqzDiscwGOqoiDRpTXdCpRYvTAEsnkKw2XZ4Rrv4xrAOD2ulWs5owG62C4cZ8Pr37A-HMmfhfYvy5mPINQ6QKr7Iln11wkJaKETpauLxloU9dI3HjzNfvN6Ljuboymhw59PK1YJENK9DNdATYxWomJWZLwW-2Zp_eDFCY5TybzLZiLWulJyAMTlBH1yDxoex_ghA09jb-Rvd1LUiGOmqg-EhoPrj92X8XbKc4lmoQQYen6uUVWgc_cIiEOUM3TpYbgT8d0d36Tqx36g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوری؛ رودری فوق ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی که بعنوان بهترین بازیکن جام جهانی 2026 انتخاب شد آمادگی خود را برای عقدقرارداد چهار ساله با رئال مادرید اعلام کرده و به نزدیکانش گفته پرز بخواد میاد رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26214" target="_blank">📅 15:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26213">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEbB95RE_qlf788BLqrvu6XjOJ9dUwqDN3ACgyNTQbBXL71E4Zyv8DmT2A0CGPGQZcDmT_utR6eTJfNsdheYcrE6o2wuXMUzDO935ia-VIzeFffEhBX6cK1WF3yBsoiSi7tMd22NDDv3o31RF7oUX0TvL3xHyXyK5LFWkK6N0xj_D592ccEn8uF4XkMpn7gaDTEJBNi3vAJsY-QAKAB_aw5q33xDwmSGeC5rKVyCoGIc4Z_pXLyDTyCMKV-kYI_VwLhImNng17JE77luBwqVIpfmOpsFLg9ampBeE-HMzO_tB6onjrceuuI37-giaa0fdkA42kcj3NMiI3Fe-vvGgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26213" target="_blank">📅 15:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26212">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfG4HWMl0Wnxmx_mDHAhpoR0RiMZL_rT729QE5iSQkvYTIfLiqmdBZCKSxT8Mmwvq1EP8OAnLyTAWJCn7ZfbJbGuELzFsX8RIeJ7vriQUcuzAL0iTUsgtqNk-XIUNAEK2JrC0nQDlBZSW4YYcuj4GyUE3ZfRkwDcrFLucL_7IMth3-fRTdekxd0dzOTPDLGTj14U66KvsJfOO_hYbMxeCEZwnEpWEd9uLwho5_Ctxs3DIJScNjyNE5-BOYZWsmHU0io3H5m1s7YYEPm6MG_HUe2HSWY87Tovmkonhj5qXlb60XhrkZuszy7NWOUv3YK6IVOwkfd_8KCu0raZCfzUlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال ساعتی قبل باباشگاه آلومینیوم بر سر انتقال محمد خلیفه دروازه‌بان ملی‌پوش ایرالکو به جمع آبی ها به توافق‌نهایی‌رسیدند‌. باشگاه استقلال بزودی 60 میلیارد تومان به حساب باشگاه اراکی واریز خواهد کرد و رضایت نامه خلیفه دو…</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26212" target="_blank">📅 14:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26211">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_Op2kePYv0I0-shFmr30iguedpFYMZjG3S2mFq7_b7C3VzygLKqG_eg34ACdP7WD8r-Q2LAkrKHzIaxE0LP25_5Gt0O6Qa1XsoTwM-etmvhcerGxqACoQQDmSqQ_fLVQJTWC3xWLAjt-7KeBRfncK9NRUV1M2S-F-p54WwVU1Wn851X5_5FJBK0IYjNVRtE6hsuU_M-fDK3p8zTc29Zn1OGoH37bgPWKFVUp9dDPlkgiHsejGA5uGTMGDegLb81eWQuRV7k8QC5fwY2Eke9mjOl5E2lLYknle5PxT8Ewh3zF6uqaZGnITNaqK82tYv9SAuftAtTCCsFQ03JqHR74Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا؛ علیرضا کوشکی فصل آینده در استقلال خواهد بود. تمام‌توافقات برای تمدید قراردادش‌ انجام‌ شده و بزودی‌راهی ساختمان باشگاه خواهد شد تا قراردادش رو سه ساله تمدید کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26211" target="_blank">📅 14:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26210">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UknvtdaahcvHOpSfcD-UXQ-MuX79dEZHJZfmCli87HcFy_8UtXZlrbi3PbC05lFo-R_Qte0fb7919mZh3ljGAqqUs0RyMqsuk8KEJJFCRN3cRxOKukkjGlrl4oLgFzVkQuvlcW4WQPklqsCkboG-lMPlg_x7ePObGyVl1zRFtwG05azxgnScuJ77onuEltnFh1V5zkOxo0pfzLs3UivKOwK2ndd8ooRfAA2WYfEss3RyF1mTdsYGsD4Gf3i76vsQj9YSpzUa_vjE3Uf4X6GJoylKVWDBiW6eejJ4UlMC9ByPGYN48fpN9qZvf4hL45PL8hQ_Vw-JFPNE7RqhsWgF1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
جسی بیسیوو وینگر 18 ساله کلوب‌بروژ با عقد قراردادی 5 ساله‌رسما بارسلونا پیوست. آبی اناری‌ها برای این انتقال 8.5 میلیون یورو هزینه کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26210" target="_blank">📅 13:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26209">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4MPwDoEWlROLcKzoXBzl7gWqueU_3WICV6NDiwpCYhJ7ouZtuIrGx53ohBSXMc9vcg46z4raQgG0944lQyB2VP227WQguDtdP4ynzDd-VVbZt-3tve8ACyGLUlHc_JaP__fGFWY68D2s7cqVQ6QwRSBgpkYO6593t4S4Su-5fiGNRe-s1_yMcFquzU_AKHVc4IwcrbRlVhMH5TvR_ylUY4Lk2tIuEoV3yJJr_4fuLlLgPChd8ZYzA4AjC3UbViKJryMYV-pt_w_TaLyCdUcxIknypyp4Qr2pMD2Y8ArN7lYuwoKc5TYvjkoKbDtiH0KeKey5QaX8jUdT64gQ78GaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوری
؛
رودری فوق ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی که بعنوان بهترین بازیکن جام جهانی 2026 انتخاب شد آمادگی خود را برای عقدقرارداد چهار ساله با رئال مادرید اعلام کرده و به نزدیکانش گفته پرز بخواد میاد رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26209" target="_blank">📅 13:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26208">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8XbSs-XsTCoVLZtRBGlMbdtBrqznBeXgRULZBy2HN63IcNzH-K0hIz6W-3SiFxcoGfh2AIfi2W07J0AfSAkLgKvdJ2FL9LzE3M4CyCDrXZ-KCldlsy3RrWt5tk2vyqgkH6tETQA7mgyU1WbJr-XI9_iOg4hXI4kISwDm4EOM12kSSairQ6POwBP6AQ5gpKP-CC2pdnYuOgKjYLHbFxLhh8mMF53I3O2xFzqs4r79dVp5-KuwGUEkMz2aNsNVxzsd7TfvyACi0HzMS8oYgqG1eG7QqzONPBiksGvFtEOL38w_P5nWP8EWtPvJ7e10lOXzeF33OFPco6F4kYtZwH9ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی 10 روز پیش پرشیانا
🔵
بهرام گودرزی مدافع‌چپ‌فصل‌قبل آلومینیوم اراک باعقد قراردادی پنج ساله رسما به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26208" target="_blank">📅 13:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26207">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4GIJTWeIa_yXlOhG9BKlu9bU014ta6NyBIoDnfpB8EIBZMQpRCLsl8D9lsGOLtI8Uy9AfWzpll6Qm1-eLXjK_cBhDbLMEuEd4blScZqNLqxieHBBqdQFituitIOTeCLx0NjN31VqFCHDvu7-dnhyByOcYUv8PsqGlKDi2PLCYXrXNzCECs0wG9GEwrU036wbzAzYE-iBt2FV1eCdH4BGUOPuI8uDi9spukmLrLTXIq-M_5D7nrP57a0T5MZ9WZVDGfgTmIKgByKyfCL7pbzK1SaGhIY5CZzN1JoDIS4dqRFLW6a7Z4XeJAHaJ0j-tdOPkZN-WnqGJRLGvPLcnCf5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق شنیده‌های رسانه پرشیانا؛ مدیران هلدینگ خلیج فارس از عملکرد مدیریت‌فعلی باشگاه استقلال به هیچ‌عنوان رضایت ندارد و در هفته پیش تغییرات گسترده‌ای که مدیریت آبی پوشان رخ خواهد داد.
❌
علت نارضایتی هلدینگ بابت هزیته هنگفت برای جذب ستاره های خارجی استقلال در…</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26207" target="_blank">📅 13:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26206">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ydgk4YJiAciRPOTBOqlCn4qxRNvlYtzAQbftwAwx99xSwM0YVtQQe5W7N9MqXj0IFtRDj3oBu6XFnDGG237xHMlqBnpYm7uyN3O2YmWXu5TG6xI95la0liwy5LnyVctgIfVcB_tSQ6Qqpr-SYIpMiuXhIVPMWMkdybtVWYK0yAR33d3S02oepupUfY2p4dKw3OATPIeGjYjeTSIbWhTm7e5yCGwUExEytVny2NNifKCkpicYkPvcofc5K3kiDUZSdKUa8VhWvvmxIKkzb09lUVgX7AahAopLWU0m0dpS8pRc7LZ9tY_d5tUTs291y7POFqcnb9OKPyPI1yFBrfFJCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
#تکمیلی؛ حمید مطهری به مدیریت باشگاه فولاد خوزستان اعلام با هییچ رقمی ابوالفضل رزاق پور رو به پرسپولیس نخواهد داد. مدیریت فولاد به پرسپولیسی‌هااعلام‌کرده بود اگه‌مطهری اوکی بدهد این‌بازیکن رو با دریافت 80 میلیارد بهتون میدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26206" target="_blank">📅 12:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26205">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9LOl5REJGG9yjxWw4uIbgnkYKyD5cSMHl4xg4qBI3Xx0IuXAv1B33QNmVkUubHSoA-6LvsJF-r8bRfHrsr9zN5Ou96zc-Z8OwU6gn8YN6rKpZpquoK2CgJdk8C20Rp8w7UwJijuZ5iE4nh15NM5k8hmhWEs_42Zm2Hph3EAt-mdq_KZ1xBUAgJN_nX9733oOtIfEcPc6z3-p4q2d6MZd1LeZl3TNBmaRvhvX640uFk5t6-LL73oPUNb3Pfft7H16vJQbUPdXMuCEhcKlQgUHmmml2ImREx01qpIRaq7Ix60cRL0WGvqlbsrlEV52FS2p-EzmVdUy_H8DcHfyo9n3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
سیدبندی فصل جدید لیگ‌نخبگان آسیا اعلام شد که در آن استقلال در سید نخست و تراکتور در سید سوم قراردارند. هر تیم با ۲ تیم هرسبد بازی میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26205" target="_blank">📅 12:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26204">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">▶️
هایلایتی‌ازعملکرد بهرام‌گودرزی مدافع‌چپ جدید تیم استقلال در فصل گذشته رقابت‌ های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26204" target="_blank">📅 11:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26203">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vldGXEq6dkM8LTY5txKei_05PFKlFfeib05130FpFiweQDiWPSYbMxphQ1EYpAG0UIlJV_GxBy_8aDuFojwTuDMaiI_1dIwvJveSfy03TD3tT6aCtq46RgzeDX4L3MJi613tPSDJtPrmOysq5YxUGiRfbkpz829MsAmiQiHGs9fvczc4CKEWlqe_fig3GfRScZyqh18Y2dUOijlUUpOfW33JV4-nQaK259KJEKrcvvszRa-hmwwux6D6-n7cp8fa2yLRPbzFRW03-GRUFf4G1dB1clAILxoXLeLauOa1RKC7gkr9kxs6GIBQdtuLUvGcqoVXRtRk2tbdIx2dH_32gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ باشگاه استقلال بعد از محمد خلیفه؛با بهرام گودرزی مدافع‌ چپ 20 ساله باشگاه آلومینیوم‌اراک برای عقد قراردادی چهار ساله به توافق کامل رسیده و بعد از باز شدن پنجره نقل و انتقالات آبی‌ها بلافاصله از او رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26203" target="_blank">📅 11:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26202">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6cc5dfc32.mp4?token=HeNXiQ6ON25HUs3jLFR9rWZotKXDRWicoIiqZs29E9Sj3UD47OkWaHuKgRmvi0iWbNbBXgbTHtnx6FGGsGQAWUanxhoD57WGqkNhRkZJL3TNuU8YwqdK9W3ihDJQ27ONWrPfTHR3n_eQv_XTwkVM7LZPlSNuZk3f9i6wQC_GQ14mM6zczQEIZd-kpZLUzDVObPn-evu_kT0FX-t56BsdnYHl8pyEl57LEPCeR-5TEBxhTFcP1hL9OCoqH2GGKBOKVYHZgw8EOcYiypJqhbSohlRx0xZ69rOZcfV2na3a327tOzEcwWuA0dHdd4X5Ub4nWBov-b83_k46XT6b0xXnjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6cc5dfc32.mp4?token=HeNXiQ6ON25HUs3jLFR9rWZotKXDRWicoIiqZs29E9Sj3UD47OkWaHuKgRmvi0iWbNbBXgbTHtnx6FGGsGQAWUanxhoD57WGqkNhRkZJL3TNuU8YwqdK9W3ihDJQ27ONWrPfTHR3n_eQv_XTwkVM7LZPlSNuZk3f9i6wQC_GQ14mM6zczQEIZd-kpZLUzDVObPn-evu_kT0FX-t56BsdnYHl8pyEl57LEPCeR-5TEBxhTFcP1hL9OCoqH2GGKBOKVYHZgw8EOcYiypJqhbSohlRx0xZ69rOZcfV2na3a327tOzEcwWuA0dHdd4X5Ub4nWBov-b83_k46XT6b0xXnjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/26202" target="_blank">📅 11:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26201">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0oXKpo1U-UfLpLaBF8qjTb3BoWc8jiuN1He2MGtvONAIM6dAXt_UwbgYPDqUcxoWF-6_rTJcbm_gg0dcFpiIgE63EaJTJTi9eM8uGYT3ckxjcyO8sxoCNSGZHOIB8HwC_8y-IUDkHcyW8r7eevzTHuYqsT765mQvctTpwJcBEIhDJuYXRIzNwTGndVquqwaFxQdLNeSYIUKONfYe9zfzcZPFa_x8sOcBgKaJ9XWBfQ0fwXNUvJBg3D3ldTolBR6248oVOR0DIuQ5gbPjSixb0lsW3Ujs6IqbHqQ4AXblXfVVDmuDjeimqnCNRwsV0bbLT9UbPZuVa43GgRNqpf0vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد محمدی مدافع‌چپ‌فصل‌گذشته پرسپولیس باعدم تمدیدقراردادش با سرخ‌ها با عقد قراردادی یک و نیم ساله به مکس لاین ویتبسک بلاروس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26201" target="_blank">📅 11:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26200">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLTd-6lxN87uG5lNEdzNaO0epPkx_lOyv7WlQZf9YwCLlNjEITDT5Q6HrMGNAlUTzRDkFCCSD4G0RNkgZmxHrKpGc_WkVP1oBSmp8l4EUeTAWigZkO8bgpVAE2YmHk0irOAXprYjucfN0JYt6xT1UVRALfoqAzutoYZ7vdgYzIfFVpItjlHid5ZWfiWkVWBSXLOea9iRfmrTMQIfDAXWu9u_IrEC3aB6rZnYpDQ2hNdgdppnN0Mix2YKKmfkuGYmNKzuUl3psYJDfxt-XufoOKpc_rmFmxpAHiF01TXkYTiJLIxa3Ozkkrpaicnwanlm8x9-2StCq2N9VQ4GefsN9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
علی تاجرنیا باز هم تاکید کرد: انشالله تا آخر همین هفته پنجره باشگاه استقلال باز خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26200" target="_blank">📅 10:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26199">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dy3yvRpg0WeYksFJ_AJQo3FWZ_pKofOZCcsdYv9KIO5KxVT-vQmDTh6c9JBSyab0yzxo8vGLfc1jTdLm1ZXniqdclk5lbl_4JUGagSr-IUjVoHjYjKvkYko9R7HuxR__PThcDGDuIF7APhPFGQWyKsWnWWlVc4TJrw9_TYZcEyjHER9VrRUsB72WG68-qPIaEwD9QS0HAHPvNPn3FkDxdCRrjK3WFddpDrJbBUWFBLqXjUKHgOvJeqs8wnYqQfHh4mUH0FmKG7ffLtuASfqg34_ks4ascLupLA66skw0UHbg7yg9BtSwF2UIFuHdyJnItEXDQ2C_85RKF7BrgAONmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇭🇷
نشریه گاتزتا در خبری فوری؛
لوکا مودریچ فوق ستاره 40 ساله‌کروات‌سابق رئال مادرید و آث میلان تصمیم به خداحافظی از دنیای فوتبال گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26199" target="_blank">📅 10:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26198">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a3189b48.mp4?token=BoalYiH23FmEYTjTTLMuPltd74RSaKwo1G2C2JZvZdti7nx1wjkuLUooFb-YKWVH5HoL00Hzbo9RwY81jUfMDFFi_jA0aoxVrv27ulqEC6-X_2qxwe65mjUq7Sql0CnoB0KQFvAb5e0KtjCfKX4wUsM8dU_wBn9F1ygEPFVcUzyfDuYEnbfmixmP5VlcsW8W0ibCpgtC8bD1961znKpfEbxpk8SgJilgADQjsfekBAyZ7SsA0DSBqCJ_k1aZ6XjQV-GIUWKB6MFNbAe26oFqu4FApeTr9_-OAiJcLaYuUiNEvxPcV4cLJLuYy9Tb9cZTlzNqez7Kl_VNkfW7Zv0c8jdkY9GX5iLD-A1vTptmxt42JT4A6VPox1dK9Y_rBC8c0cX7xkUFNocRK12ceZET5VZkuwjzKQB2pveaTcHEBTLT0WS5l6ShUGuEMOi3eo_FD9bKMAMWZs8cuDJvbUJhSwLDLMh5xHPCS_DbdnmhTCoRB8jxooh3sxq3TMsHboBnQTCcavzW_sX9zaYjbS4dgnhjod8eEF41b6S8TxJXNnmTZh9JZpEdid_iNCeFnVZFSJn9BrK9gzQhiwETPHUZJGoZVz0R-VCUzWVfIjRNrWJJfz4DypIhJfe-mZyFTcOMt6t1p-vJ1D8zqIemVul3w90X2LDpK0-B9IKNQfEfURI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a3189b48.mp4?token=BoalYiH23FmEYTjTTLMuPltd74RSaKwo1G2C2JZvZdti7nx1wjkuLUooFb-YKWVH5HoL00Hzbo9RwY81jUfMDFFi_jA0aoxVrv27ulqEC6-X_2qxwe65mjUq7Sql0CnoB0KQFvAb5e0KtjCfKX4wUsM8dU_wBn9F1ygEPFVcUzyfDuYEnbfmixmP5VlcsW8W0ibCpgtC8bD1961znKpfEbxpk8SgJilgADQjsfekBAyZ7SsA0DSBqCJ_k1aZ6XjQV-GIUWKB6MFNbAe26oFqu4FApeTr9_-OAiJcLaYuUiNEvxPcV4cLJLuYy9Tb9cZTlzNqez7Kl_VNkfW7Zv0c8jdkY9GX5iLD-A1vTptmxt42JT4A6VPox1dK9Y_rBC8c0cX7xkUFNocRK12ceZET5VZkuwjzKQB2pveaTcHEBTLT0WS5l6ShUGuEMOi3eo_FD9bKMAMWZs8cuDJvbUJhSwLDLMh5xHPCS_DbdnmhTCoRB8jxooh3sxq3TMsHboBnQTCcavzW_sX9zaYjbS4dgnhjod8eEF41b6S8TxJXNnmTZh9JZpEdid_iNCeFnVZFSJn9BrK9gzQhiwETPHUZJGoZVz0R-VCUzWVfIjRNrWJJfz4DypIhJfe-mZyFTcOMt6t1p-vJ1D8zqIemVul3w90X2LDpK0-B9IKNQfEfURI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
این‌بخش‌از گفتگو عادل و علی آقا دایی و کریم خان باقری در هفته گذشته بیشترین بازخورد رو در فضای‌مجازی‌داشته‌وحدود 50 میلیون ویو خورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26198" target="_blank">📅 10:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26196">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pN4ZvBYwE3bhM7Uye_QTdrQ8xvtxCD-nfiXaMfB4nhEMLPPzT-RJI8fUvX7gVdyzvBHVdVFTlwX_i4tbVUvPRTMTzMJ1c6iQ-ATdD8qaol3nEneQTEDXi3XtSTe3giyRGlh1Rm-Zowb-K6oCTfONkAj-MNiOU89YMjlolF6TTfNxFH_LOoxBmJQZ8VFnh1PMom3JpRHqdh_vSEFUphGOJY0PwqLCK79NqUwangGXXc4d3S9flbuOU2oFHOneM1Pi1S-tvDkJWWKR9lebZdV42DaLOnFrNWi1gPzBFs7qm9SJpHvfYLY6EJruOw10VOMgEbhVQyWszRBUavePqAnmTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برسه دست مجری صداوسیما؛ تیکه‌ سنگین رضا جاودانی به میثاقی در گفتگو شب گذشته با عادل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26196" target="_blank">📅 10:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26195">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTtrcKafik6tg7SdO--VRzXoOpFqYXNez5QEQ7tF0YatDCBpLHeuQVcdvTKIctHb_u5NL-AkWOX-4rqWAO0edODrc-FBQV8yzQd6-wGboofsS8ANmvfV6j6lSY0fy6Q1ql8V3UsfEeE-uxOgFpdksAccvU3gZG_Ro2J2l9E133I1VSUsN8EJG227l-_OpussFPJyUiNdhh99msPadvMbBjAWg4Cw201p1vfH0tdxwTMCFLMwHBk9uN_hf-zPEnfc8EaaRZiVWPwcr-AdbGc36Gs4ycoSgFp9REHjusfWkh2NeGdhrqk5IkW2KyV7bDetXZbe92t1jaFl1_yIcfUCPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛پرسپولیسی‌ها برای‌جذب ابوالفضل رزاق پور مدافع چپ فولاد خوزستان با مدیریت این باشگاه تماس‌گرفته‌اند که گرشاسبی به حدادی اعلام کرده درصورت موافقت‌کادرفنی‌رضایت‌نامه رزاق‌پور روبا دریافت 80 میلیارد تومان براتون صادر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26195" target="_blank">📅 09:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26193">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/944a94e4e2.mp4?token=ksGBWQpz2IvLjyeMm4iqHW-7p-JwnnazX0-xJe6PDja7omw4Fe4Nb_6x1dbFRNJ4tD8Aco_1l4JgK7k8rvpozeFhiQvWg3No7Y7KUH5VBcZEcuXfSGzG42qRNvu2OcbqEk_IZVL7rNaYEtNQbBsjSON0yiIc1dPayYl5gm_FjwwPJ5c2RIt72aa0tn739tPEixjXBa4PLL4rK2cQb2L34H_T7trDaj7uzmdngoQibuQ5-iiaVjwv8CJGBl0k4Tpj4qvGl_LN61EBvc0TL9pAaVgNQ9f_d6-1exVP4LNInJofy5_GmolQyQ87W3QZpHbYmK4JEi1BqVaxjnRG74X02w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/944a94e4e2.mp4?token=ksGBWQpz2IvLjyeMm4iqHW-7p-JwnnazX0-xJe6PDja7omw4Fe4Nb_6x1dbFRNJ4tD8Aco_1l4JgK7k8rvpozeFhiQvWg3No7Y7KUH5VBcZEcuXfSGzG42qRNvu2OcbqEk_IZVL7rNaYEtNQbBsjSON0yiIc1dPayYl5gm_FjwwPJ5c2RIt72aa0tn739tPEixjXBa4PLL4rK2cQb2L34H_T7trDaj7uzmdngoQibuQ5-iiaVjwv8CJGBl0k4Tpj4qvGl_LN61EBvc0TL9pAaVgNQ9f_d6-1exVP4LNInJofy5_GmolQyQ87W3QZpHbYmK4JEi1BqVaxjnRG74X02w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🎙
عادل: من هیییچوقت بلع قربان گو نبودم و نیستم و هیچوقت هم اینطوری نمیشم، اگه میبینید با من مشکلی دارید بیاید دستگیرم کنید و هر بلایی میخواین سرم بیارید ولی من بله قربان گو نیستم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/26193" target="_blank">📅 09:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26192">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a85e23671e.mp4?token=AuI-dsEBuzKYYrC5B_aVIi4XEk1FdluULptEDQLKDQgY_sS0jQWY8lHHo-rzkbmiyAYfptUXk8WGHyRt0zFdFr4ZU8E0nym6322uO8tgIdxxMifHCNMGVKL99nSw0Q0443nNuEi3WWs5ig4L0cYWYPJODQOUEB-8MaYfFft8Z_S-vOUhKf7gKlnPJ3wirQiG6MMWUryOcZEjqSC5dh6Cz9wCUqdailp8RJwdB3psDztnqASPEI51eopoOKJdXrVcYzSVetjDEf3MJ93HxEhd0XwZw9h6M89KrAV1gF2XfEf6oGttlVnHRv7wpxnogAf1PHKi97wbVKrVaA8iQ-NToA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a85e23671e.mp4?token=AuI-dsEBuzKYYrC5B_aVIi4XEk1FdluULptEDQLKDQgY_sS0jQWY8lHHo-rzkbmiyAYfptUXk8WGHyRt0zFdFr4ZU8E0nym6322uO8tgIdxxMifHCNMGVKL99nSw0Q0443nNuEi3WWs5ig4L0cYWYPJODQOUEB-8MaYfFft8Z_S-vOUhKf7gKlnPJ3wirQiG6MMWUryOcZEjqSC5dh6Cz9wCUqdailp8RJwdB3psDztnqASPEI51eopoOKJdXrVcYzSVetjDEf3MJ93HxEhd0XwZw9h6M89KrAV1gF2XfEf6oGttlVnHRv7wpxnogAf1PHKi97wbVKrVaA8iQ-NToA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26192" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

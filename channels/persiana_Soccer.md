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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 18:01:49</div>
<hr>

<div class="tg-post" id="msg-26299">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQ1rHbkMoBOmHlPgc_lt-JrSLNZECPCIftHu18-DyybZ0uWGb1N-g5Jv2vp18Jj6UQXP38GRK5fYV8u-lNlHkgasyw9i408yUAiIfCsdBEsdLs55DCHZibxdbHiXNgnHfImeihYth5EEaUicAHIg5vyPSbAeIrfGPa_5GNTFEt6ZFuSBDRvf-gm2pZHrgNJQ1iFPb-GhBZ9lExNYklMjsY6eLIPwfuKtimzpnfRLcTU-AayGF9l4qHMc8dCIQXNRoceWGC9A4KkOzH9bkt5NWgcvZBvtMon2PYkRR0sJ_owJYZOzhNx6UE-CGx9rI3_-odELKJohzsLDqvfbYBfZ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ فیفا ظرف72ساعت آینده استعلام باشگاه‌پرسپولیس‌ونساجی رومیدهد. اگه پاسخ مثبت باشه کسری طاهری بزودی با عقدقراردادی چهار ساله رسما به عضویت باشگاه پرسپولیس درخواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/persiana_Soccer/26299" target="_blank">📅 17:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26298">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OemgJYU3j0XvuRE6JrISGeYLvj99pf8sOMMWJh7VFxxdw9Lf6dqQhL-1PtWv6LPqYdrvdDTOoiY1xCIf60V44PaTioIrLPCpD3KVQuUOvYBuwOUFofqjixsXX00w2nqGr0_BhPGNOu6OLoe5hqnvv2pfMclt3I19lj9InBP8fRM43v68SYEmvH7lKsOJCXm6596BeljD5sF9N5_98mYopXsEy4Bri5LoZpo7VQejrpPshZWqx9JydWOzPnArqg3URX_YXDzxt28l6NX1FVDoYOxstDPsfDb_x4ldALc-AhTHtV0UUvtIHl51WsWKoagLVEsh7fRyfvG1ovWOcp7wSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/26298" target="_blank">📅 16:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26297">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1Lx0u1mLBx76hVLN1jM0V0n-6U0J5H5JG2MzkKlGXwRxZZJM_5naeoJdNoLc2E83RoCteNBq38maEMxHoU0K1wNCoCJ9urYUo4dcBfch-OfzUUilPDU6t__cDTRLF8Q0N15dM7i5PDG6HDNm1adHKgtsQyfwp9lQLzrife77SVwTlJ9vaYYRJY7-BqyIlObuckenffcq-1xkfFxBe8Ons-YwUaWwGIRVx3QcIQAQDa8p2FKTuKurxFFx1AeOICQNIZU4RzJeh_oQ12XDNShGbYCM3IwvDul7pIQVVI-QwHKmh5qC-ylZqRx1G1ALTFL6GndfwWpI3qrJsUGQ2LbnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط 7 بازیکن در تاریخ موفق به کسب قهرمانی درجام‌جهانی، توپ طلا و لیگ قهرمانان اروپا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/26297" target="_blank">📅 15:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26296">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUjuyaV4yXw6UFmpuUkZtGOEUB3prV_gqndkMXM5U3Pe-GzNC1eLJIrBWb9gbeWO7Oshvn5bLQBmldPDR5nB3csXniBvQhJkjq0jyhHQlwC9L1xcWnb9Hma0UR0yp18sOS67oOPqBhLJ3Fikeurx5FyuvM49cDN91dICgZ9fabcpv3wjFEg7BzAqvxRdcstV_ugzSUFo4NVP-jLKjF6rJak6mtaVj8tsV02qbziNTiD-1bMeqXv4zpLK_Viqk9BJeU-5nDKSgs9Bvs3kME-ZZbGeo207EsX1QtQnfGjNfdtOh6SrRI_GOAxIDcHEMaNzAUEp5-kDMVIKfMwUTKmEew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#نقل‌انتقالات
؛رضا جعفری وینگرچپ‌سابق ملوان وگل‌گهر با عقد قراردادی دو ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/26296" target="_blank">📅 15:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26295">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwvOzMokkoLYNAotFP2S7_AZBkYVoZs1bDiDefzSnC9FwEiEt71aCSvEbrt0fmYM9RY8veF5kbm3NJkj8CqDKOYVPlHteuoDhrMzi2VVNWYIo92QLQ71dRd_7nQBoAyrZMIwg_RfIVB5pvmcyJTMhb5zN7shGS1XUR-cdf18pRABzmrc2RJd2AHdD2ynDwSqcghpsxvSlPHc810-hwm8IaqrIZN4ML8kubFtX3UqaseiIgkGlObpR0agkOUcgwSnnUgtW6VbrV-NH9du5twx53PqLkY481C0cjG1FU3lgLlhOEW-D0FJaFjxWMI5aU6pZVo60TL0jrmlvB_mlY1MIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رسانه‌ های عربستانی مدعی شدند؛ باشگاه الهلال پیشنهاد مالی بسیار سنگینی رو به فیل فودن ستاره26ساله باشگاه منچسترسیتی داده‌اند و قصد دارند این فوق ستاره انگلیسی رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/26295" target="_blank">📅 15:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26294">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvEr5QPWrew8lrEJpc95xgK-9DryBZmMVF0EIXwETBLudX5Oeztl3qTZlZcdl8jqYNQe2RVAsyVzS6DGPXQ5qD3jJF4OKaJDrKevZqlTDQyfSCeHD4eaMON_e-jsxq_wXvpPQe3TolTXp6u1LVrvvnGTAfa34bP13CsMo_4hReALLALTvfDm9Dl36AKtF5PlA-C5h52XBXnWM_4YoQhIm-r6x2x5f6LJAjl5AjrTzK4i86cykM9tW5fLByY4xMYQKPLI2nt3FaJuvbA6wBzWpyBaTtcoyaUX9auvrUjAxCj4n-v1Tbm-NUJBuY8jA0SKxZdkST-SB45IPzweVdk7Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اگر اتفاق عجیبی رخ ندهد؛ باشگاه پرسپولیس ظرف 24 ساعت آینده از محمدرضا اخباری و دانیال ایری دو خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/26294" target="_blank">📅 15:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26293">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olteHfHhY6FAGPyNwYPVpjyNozzi1-b3pQhxs0CNhfKf95ngvEx7XDfWulWNJz9GPEYUDRZN9ogw-xZkhNCXIYVWOY2ckts0SlonmYlBoKa85ajFlEgbrspQ4bI6MYPpdLXxqTA2aSFnNoAjTRFhXaF1tAmOkdKyWesraXweIV5dhEDE-HwKgaROIDUYHtL2mCpmrlvzz2ehGJta0PVpuzePRfxBOe37fV_PZl1yVwYRM48NwuMlt75eBl1EqX6RQ8pcMj-QZrIADsPvWpL1k8If4tzRV5-atp_Ap-1Y73_Ie5h25ygNiGnXsUPOTplelVnJou-Sdz7afHBrr7nLvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌قوانین‌فیفا؛ درصورتیکه پنجره استقلال باز نشود این تیم درپایان نقل و انتقالات نمیتواند سه بازیکن آزاد جذب کند و تا نیم فصل حق عقدقرارداد در سازمان‌لیگ‌رو نخواهدداشت. این‌درحالیه‌که رئیس هیات‌مدیره آبی ها امروز عصر گفته بود که حتی اگه پنجره باز نشود ما…</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/26293" target="_blank">📅 15:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26291">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D0F2hCZWzazsyCu-F5KGXkjlmCkR6NOvd9fO8f-rQqTBLWqjYBnroHbqDbteYu0b_2gtmu7UIXHzW502-UBj9PhDehMa542M8rbaZNLbMa4_HLtZPheOCe6FWkeyYV6WdBY4CX71KRATXkths2jXAIMnMo_zj2FdToctS3FGQWaChQwBU_tuTKDysjcPsw-1WEbzwayt3xycCZG0_YWto0NQ_FVFw_vwg-1kEqvapi9KfDVb37lnqVDxOO5zPABggnZACAyq8Jhh7iBvCSZroWWGBBxJ6z5W7cgGo9DgqOVYx5k4lJbD7KgN6GIJQs8GZ7dUPH36eaBw-TnsZPHXzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F4PgX-FlcV-_-wihCwlTbrQ5IrHNrA6VsDg8HNH123FdXmhrffNXINdXKzwYEob-oBdk7w34p5xPySSfQzYirOjVMEoqJl-QXF7I2Zxam69wkX0kbmj984FlnMcSz2UJIaAUi3B9xIk1yij7JrmUunE95H1bcX5hwR5aI1xtFZ9tDB2f9A1sMeQh9QyfnDqGBMpjqJS3xPFVzTTxX7zrzEUQrJeVxEXWp_bJQhONbVaIBTlnaWz7EfeU5LaI5-K0_Bok8CZ8bnWwATtJ-Sxva8ecbfG-ps4hucPZk-zSG5oINd4m8H0Sg5nS5jM12lUyBnwo7zXX4v3SN0x6uN7nBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🇪🇸
ملکه‌های‌آینده اسپانیا فعلا دارند با کاپ جام چهانی که بروبچ تیم ملی این کشور گرفتن عشق و حال میکنن هرجامیرن‌اونم با خودشون میبرن و چند شات یادگاری باهاش میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/26291" target="_blank">📅 15:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26290">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYIED3fY3wavwMaHP3UZLkjHBpfCaaDRswfwff2c4Yd0r-xbbxJZAOJ-LffKrSn7W0CQ8m21hWIo0JjSsW-bXKLhzaiwPz4wwCCO4FMOeyzxqZBdueWcq8EtClaRmZ2Iis9wVMFIrPHRpor-u6s8HGxwnHfkq24VCf-Uz5hhPt8FFl2UwFOZC2TsHmLJwG7134JIRfvcIK9S1ZQ0D-W0aKxSW1J2cjWXLCrJxUs8-_bg6Jy32R54cXSuVbgaPhK6e7IYZhT5hP9n_nwex_4tOQ6ISL-dPM4LEbnjH25d1iYAGRZgEflPi3vINDerBuEHVRaDgtR4JFzhMXkLpGrfEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
خریدهای لیگ‌برتری پرسپولیس تا به امروز: مهدی‌تیکدری‌نژاد، سیدمجید عیدی، پوریا شهرآبادی، ابوالفضل جلالی، پوریا پورعلی؛ هر باشگاهی هفت سهمیه لیگ برتری و سه سهمیه بازیکن آزاد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/26290" target="_blank">📅 14:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26289">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKqFDAKniYAtGC5HhYFlo8SqWZFsdT8PvEpjD2w9sEf82o0hcc9zGXtFuZIASHO-69PRyvISzz9iyfwpkKqPboKkfTnADCZq-pTCzzW8oXZgQq69I5k1Gy2mZZX_c7781u0vlSXLzU5EzxWT79XEnd7CNxtfIXd2trElQXCB49TGphWw3eDFyh-uSLdC8MvHvRdAGOh17Kl0THrQ-veIwEqFE6aeNMaRJ5lZRIL3qfmFJ7wzDZ3yhdyS1S_TCl8eRevoUfTiAVEfolNW1FLljPyXQdBw2Ogy-WExtUmivEcleWDtTIiqJMDyfTMflU5_iNoPyxhbvyNFAbGtmSHItg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیمایی‌که تو جام‌های‌جهانی اخیر تو جریان بازی نباختن؛ ایران 2026 و نیوزلند 2010 با 3 مساوی از جام جهانی حذف شدند و شکست رو چپشیدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/26289" target="_blank">📅 14:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26288">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmFyLCClfnA97WjL4SxLwCGT5BUfKUGYrV25O1L9gJQuQOxleuLbGUTX_Bil83lQa2BXPhxyfgrS93bogN2ZKiqSsds59-J4f0fysbS0RmRBusHa27og1P-_JsfKLXo7gAfXAty30AJFYs9-8L8IQaEO4-33kp7DWZhgbZsHUT6PWWt2ID2PWweEKPo55AIwDh5c1ussKgZ03grf20KnmVNd4hPFJVRgTGPDn--a8Th3IGUkVXgtPUpgUu8YUnwUgPgXAchdIGc6uid_iZsJFbkNkpQ6vReBWpsy2_1PwAC3s7Q1Sj0DRdFs3s-b7x1eHyKq7nfX17ytUdkFmoXI5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط 7 بازیکن در تاریخ موفق به کسب قهرمانی درجام‌جهانی، توپ طلا و لیگ قهرمانان اروپا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/26288" target="_blank">📅 13:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26287">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eT77gQuzeTLN56X5pdBpJw10ZzRu4kKByKWBiojAbBdIFLiOJMCSGeYki18JCAWreFgEMOhSavXNcEV9AvFuUgs7Ws1CUkLN2ufUBwmLs0wEoJKvdb6-C5gLUHAeWCc26zE5rA98aCxrGlOFf3Evs5G6LdP5nyt_6IFWHTX7gnrDe8X5mJZs-zRobzbPGPFGiCMKoFgyzwU72Am_S4V610AfeJaycvUPAsemL_QJF9LHv4FfeezVDk1bLydtPPp_c26wk8WUYYJ0p7BA3eLFJxFgl_Qtbj8a7KVQyT4_emDj2rJ31aaKAS4tUv1zuyV2_qIYviDxV-VDGtwWWVQuBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ بعد از رفتن محمود بابایی و مجتبی‌فریدونی؛ بزودی علی نظری جویباری نیز از هیات‌مدیره‌باشگاه استقلال برکنار خواهد شد.
❌
علی فتح الله‌زاده یکی از گزینه های علی تاجرنیا برای مدیر عاملی تیم استقلال بشمار می آید. تاجرنیا نیم نگاهی به حل کردن مشکل…</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/26287" target="_blank">📅 13:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26286">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h41pbYvhb9e0DKRwl4nmkMylfjR-L_tw-Q_u1kgjrIAa-zqEKnIpLdrsXeEsv4NaKUUyLpzbZUnogyAG8nrPyUxHWEjTejJBgChTLoF26tDq62oMlN9rggeq-HnNLHq1xbsdgLGAQd1Uz23i0J0pCAAL_U8wmX0_ARuoNMvHyQv-DDyU8JrYXMyfBPprca8m0c1Jv8g3xWdzEWntvrDOMsWvDi4IA1_VnsilREud0LNmu96zrOoNtpPS4rzBz9zjVlBqEuVwK5VVzueshEg-U4zst7Zrdb99BALFund44B6QeO6SNd-fvUSw0ZCegQaC_xZxyRK5UiCPR07rRHVDWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
رسانه‌های‌آرژانتینی
: لئو مسی بعدِشکست مقابل اسپانیا در فینال جام‌جهانی به هم‌تیمی‌های آرژانتینی خود در رختکن گفت که این آخرین بازی او برای تیم ملی بود. و شاید پایان دوران یک اسطوره در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/26286" target="_blank">📅 13:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26285">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHSV551QYiaa7lNxeZyZHdoqMT5rVTZ2Mp_QqLo7WTBaFO3W3E1VFTfTT3j0P53qHoyERa1sirBfEfeYaYiB15LtHussL6SMdUEloOrh0KhkK8Thn14Bw-eGzIjDW1WbWK0BPNtSHB4eGsCjKSB0XyF-35NKkFlQy2X_ixysDWAN1KVjjWjRiLztEmR-2v5pJL4g-mnNWeUg6Dyrabb6dwT3qInXbxspQmbmhdYiTnFWj71lwwgRwRbHTru1IO3i_exbTlJBLDKBk47k8niROmoK0mvgDwG3brHc8CUnDotlSe0y86SCFbjuYT41KlrMKjmac5UjCvjabQJgq3tWHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسپید، یوتیوبر معروف که بشدت فن کریس رونالدو هست‌ شب‌گذشته حین اجرا در اختتامیه جام جهانی مقابل‌چشم‌ میلیاردها بیننده رو کُتش "فروهر" نماد ایران باستان و آیین زرتشتی داشت و به شدت مورد استقبال ایرانی‌ ها قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/26285" target="_blank">📅 12:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26284">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jwia238aa4jtjgpwphxxdxOofx8yCqM494SeCF9gezarIaXY24YO-Z_gvdeT8j_P8nWI95Hty8ZESwACWdIGx-_hbvFMG-R-FfVMWpGHujFpjNTikQIDhjq_fJmIsMqnj-SSyDNSMIEtoySBtyLDMv2hY1zS58MVf_GylbWWNSf2erursHIpUxI8BIYQjLeIZoJG8lnTKgqdHA3BRCJBu68HhysftgiUhMCid-6sGsuqxNaJDujOnSq05tQJIq0pahUccHgdkCXl6Sea736ZlMBcqykxjjJ3AGDWlnaw1NGPz85rX4uSPuwjVivPFVvC2OrPr0HF3vMbf0j_2PdLXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
با اعلام باشگاه منچستریونایتد آندری سانتوس هافبک برزیلی سابق چلسی با قراردادی پنج ساله تا 2031 به جمع شاگردان مایکل کریک ملحق شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/26284" target="_blank">📅 11:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26283">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfbTxnVOObZtKHadnNtxCtZtdBr67DUZynwZBbegv863QHo7DJRrN4GT1-KpPcUqcbcuP9iAFKUW5HdocjXct_GJouLM6IE11LJnpaqE1LCiCiubLYpF_z8KSWaJwr28LZxjsJyQAnnV3IThy2ELUUCroidbFVji9lFQUrTJmP5W72mnuVGxdtupRThGoZSSNkL7gmI1mlgGRH59_ZOxE1KtcWsXHmVvRzCAlDQIuCV4kGoVvA1NqdASSzwaUOszNx02vbsm4Z9Mgp-iWXAgKGEfiRVVF46hxfVMKkKb8eme1Khveo7yB6yYYw_so6mx7C5yhtDUrThh3OUWIO9LIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پوستر رسمی باشگاه چلسی برای مورگان راجرز فوق‌ستاره‌ انگلیسی‌جدیدخود؛ چلسی برای این انتقال 137 میلیون‌یورو به باشگاه آستون‌ویلا پرداخت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/26283" target="_blank">📅 11:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26282">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grPzqcVyce5MbcL6MKBQ736WntDNNSBCCHlGV4yXv-f6hY9aL9KUptZhGMzt8G1Pfc1clCX_i-89Hsc7T6fyZsvF1hINQT9AH_W0MOE4VI9vlSqndsQCAH0uN1eouRxmaGc5vHleMy7eNpSwdJh5AClTqbRTGEai1NgKnIGzaf3bJDS5V-zwaxbYwJzVVTs-wXq6ks3kXsstP23-W-vDJJdMXGXViybJWMkOT6dkhCWRTBgjCfOn6Fvcf-yRl2ApkEOZNMJL4ohDWF02auUlvzvFKKsD8MC9qU0XATooNq4ikSY7rY3U-fy7FDUWXeglXY-YhDVgkvAeQabvm2E2gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب‌کهکشانی‌وبرگ‌ریزون رئال مادرید در فصل جدید درصورت‌قطعی‌شدن حضور اولیسه و رودری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/26282" target="_blank">📅 11:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26281">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FueuJqDAvtTTLVmIuUP2sqMzu9BsTxqfH9b3vV0p2UFwih48yP6fdly-jBfFDRE5zUpO8BcBm5m7A_XtAfbXJPe2D2I9bAaAn7kF3BETpxqxBKxmKmr3lfgTeBtGQk01qEW6pCttXT9q1tDJZOOmb4S0gUEfM1KFFhuomVTax5JlgkPDOPSY2N3UdbS5SHrdL0_YIqArda-7nOE6VPMb-oeLXvn3MupFX8XwdFhCjFAk98AL00gQCl-EVq0XPzmYaHlViHaFkpgrk3-AaKYIBPIE-Za0GfNMN4QDyP2WO20IfOKlKuANLFI8SGKTzT5zQc0ZwRk_fSOr-vAAT1p9_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تکمیلی؛ دیمارتزیو: مالدینی مدیرورزشی تیم ملی ایتالیا مامورشده‌‌که پپ‌گواردیولا رو راضی کنه باقراردادی چهار ساله سکان هدایت آتزوری رو قبول کنه. بایستی صبر کرد و دید پپ قبول میکنه یا خیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/26281" target="_blank">📅 11:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26280">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/26280" target="_blank">📅 11:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26279">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ct_sCUJoYKCSkrv7FheNNZqS-RNvF_O_ORHUpCZ9J1TkFd9KMbFXRsSJVfplWs6IIi0Qpl6ARsCITny2-CfJYSQdWYszNX5XdAFkfpE96sy81oyaKX4rxXexB5wuWYPeWnfV7F8rE3L_zuSW6gQZjBFUqWOt5uE785dHXlnWJoAB7uip1Hm0qNChrPM-RSvsm1-FShQNw3syvvpQeT7zTODI3GBY2XI9YaT5gMKGmToLejEz2yI6ogvzPItpupOHtZ77yi-I5UjWnOSTMN1pFOVvs_OWeBbvdtL378j8cr1DBNpkZiGgMdRwM8KDBGrdphF9RsOwHZOEHDVOrvC8nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ بعد از رفتن محمود بابایی و مجتبی‌فریدونی؛ بزودی علی نظری جویباری نیز از هیات‌مدیره‌باشگاه استقلال برکنار خواهد شد.
❌
علی فتح الله‌زاده یکی از گزینه های علی تاجرنیا برای مدیر عاملی تیم استقلال بشمار می آید. تاجرنیا نیم نگاهی به حل کردن مشکل…</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/26279" target="_blank">📅 10:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26278">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJ4MLLjWdRgOBjKMbQsnZM-ZQplz1RVUefYK15X-gnKPg3lrpoNjIJYcCL7zHpNfnfIjMKAy--Cq7OSxjJSt3pvkTG9-rox6CpQVZwnT4HOIkPu3FTW7CMaGvKBX0jccUpQtnsZqbNDmKVwZSxVVM1clkOfVlQIN7jKq835CYf__gGUEljnDL12XFjt50GoOhHiSC840EveP7L8DnUIWcbTWhaleq9F8FaxWYADmVB8PzPMS4w13PZib1oqWdm62ndPlWWFrUKZCj29q4TvKUZ4aue_tBTVuf2R96UNWab_eqw2yGyluD7Bh-Pu6gi85xLVm6Xws4w-ZlMAEvEwZcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/26278" target="_blank">📅 10:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26277">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2fwQEkDyLVzJCxMXqJVrgoXOr1JZN8wdH5eoVbmVExLp4vUnPZMUhjyFbPKDUp4aTqa9YJT7Mxwir8EzfuKU3R99VghS6DlkYsZcU5fwooaJB8E6o8G-aTGXUm4wyq_ICUTn2xDa1daRLFnJT9Ml6Aqm-69mfJC6QHjz6BufnqePkRLKhkUxrJ7FWtZ4A7ZDajKg9CuSRewC0m3CefYR2BAQhIcuv7mbmfgwd58BBuKbabkWXwTXIr7zW9uUlQ-NexarlQvsq6_GjfOwqA-7b4aBVTijjfMo-9idfdzl7JGxTIH-5n3Ko3PxAMet2EjTS7c1vMpPgfzE0y9OUAwmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
شمارش معکوس برای بازگشت فوتبال باشگاهی اروپا آغاز شد؛ یک ماه تا آغاز رقابت‌های لیگ‌جزیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/26277" target="_blank">📅 10:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26276">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKwO7R2uEbyelP6p_iFbqZPOTheYL5Ln5osouHvObuD8PyPO9ybvA6rqdpR-gW8cL54gXfZkZn5KH_7GBCQyBJVsn1jMUtaDbVBIbiXQd5RnrC7pTg1LL--AUOOUo7WZbkGNHoIxxOusjofXxlGfwHZymj-ztHdJHBtG1LkraP6zYmmX0CxmDHOE6isyV3qo9L0cgstJM5G9YFhuEYbBRfMJkA7Yu13vuU-jRrgQ_5r0R6o_UpiMLuLgRHubavH_tfy9BnzwT_T8s8g7o9VMhTA2cuhzPwX37AbBLm7TTl96hTuHgnQWZULzN_IgYS9dR5d446On3eNcdohMbeQh1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
#تکمیلی؛ باشگاه خیبر خرم‌ آباد رقم رضایت نامه مهدی گودرزی رو 500 هزاردلار اعلام‌ کرده. این مبلغ از سوی استقلالی‌ ها پرداخت شود گودرزی 22 ساله با عقد قراردادی 4 ساله راهی استقلال میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/26276" target="_blank">📅 10:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26275">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ScOyWttHrXssh489CemT9klkbMv5NBrlKwxIqCjfXmADmwKVTuwPEq92LYVDddba8O_SXMPL7CFSJZ8Vl-BXufWPfbDYLX2Bj5CTeLrXicprgSJazowOrn512oK9Lo8StgDhQv4KkXNJZPXtoLUF2egfxDD-onIp1D-llFPygWIAmM9lkZVc6UKkzd2VBfWR8TaQNB-kTCdPef04DXVpQ22nAd5D5o5xf9Bl4PnTzS-w4AlliaVyiHhyWY0rxECUhwpxa6-6zoqIOqtrrMBMZRJeGZJ5PC1MnA3_M7iAjNQkXpUmdnXZAH33DRqIjaOh6XzvAKTkdbluFNKaq08d0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد خلیفه امروز عصر با حضور در ساختمان باشگاه استقلال عکس‌های‌رونمایی رو گرفت و بخش رسانه‌ای باشگاه استقلال پوسترش رو آماده کرده و فردا در کانال و پیج باشگاه منتشر خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/26275" target="_blank">📅 09:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26273">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZVNy12ewHbhCUdaC1vp6SCeub9gkDCqyO8dxvnt-_DtLIPhRzALXi7wkfaqM9DIqwhW3JcKXAIPDCBt0svN3T-nJHG7fUSGWSHtx6Hhx1g0YN3cq-1p4PCpaFn9XGkAtS3HsZ90abq0vTz8OAzjbWEHMe7gOsN-I8NU5yB-N2eEwFBy2dg_td3dpdvb4oOjcwaqPXUNGsbsLLleqXfVliM5bYJ_PiGWcBeO1iwvKFLcecYgYd1x4OH0wGfWe-QEWzZ3oUQDYbQxnSc8r3mifBqNhx7kqFqbNS2fVY6trjj1n-p7X0kr2prMcXQrw1zVK-sA6ImsNSBjQ4qcR108XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
رومانو:رودری ستاره‌اسپانیایی منچستر سیتی تمام تلاشش روبکاربرده تا در این پنجره راهی رئال‌مادرید بشه. رودری حتی دستمزدش رو به شکل قابل توجهی کاهش داده تا این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/26273" target="_blank">📅 09:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26272">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/26272" target="_blank">📅 09:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26271">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZLYPVuCsc3uCwoLqVGll0Va_CyfcGCSof4WqclGwHbsi_uJT_zpKjZPwewZ4i6GI9yIjrWTWndvQ2668gjMVB4yZ3au1OJnMfykbp3PpsDUkJ3KnF62k9g9CuxHK3WRTDRAy-0LCn-ASkjYvZLP4ZIUnQXedXUiIhdsSWpu_hLRIAz6wG0XN57T5segytFSgDC_3uzNJtqaJb1T3zS4kZBN0p6OCiKlnVkjfyX_T_MGwWYXdp6MJ_bK9C8nurYuy-SG_bpJMNYo-iqMHW3u4HFgAphGVahf46jzDV-brlU9Cq6J82B6ZDNMSa5V4jbQid0X7bibdwLUiFXHpnsLUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال در روز های گذشته مذاکرات مثبتی‌روبا مهدی گودرزی ستاره‌ جوان خیبر خرم آباد داشته و حتی‌ توافقاتی‌نیز بانماینده‌او برای آبی پوش کردن این‌ستاره‌داشته و حالاتنها توافق باباشگاه خیبر خرم آباد مونده. درصورتیکه‌ برای‌گرفتن رضایت نامه با‌خرم آبادی‌…</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/26271" target="_blank">📅 08:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26270">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/26270" target="_blank">📅 08:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26269">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5wlPFNd6oXaMHrDlYTIsb-mY62t29f3j-YlqfLJjTOB-cHjCgTV_TbWCXInmEUwuKGaRvzDTPREzSXfURdadlnnkcemCSEbILl6HjDtK4Wqh7umDkp53K-DaMU0kev8kJX_UApsf-w6ZV0xD0gJ7PwjwI7Zsx-liZwKSMN-Wu3t63MVbI4pRdiC-Z7sU5LKZ0y6-MDeu6egLY7AZmFb1E23sSpDoXfA2f-onNmcZvVtPD1UQyF7peAg8VVFLaHpfdPuf5Q00SqBMUrrbQYpr7dDXJFo8TejNIMoNcXNT7_O_fX0omghTIVaI5Uxc3TBmnMj4_--rGmTF3BIb2uW5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ رودری تموم‌پیشنهادات منچسترسیتی برای تمدیدقرارداد ردکرده و منتظر آفر رسمی باشگاه رئال مادریده تابلافاصله پاسخ مثبت‌بدهد. پرز بزودی آفر رسمی میده... قرار داد فعلی رودری تابستان سال 2027 رسما به‌پایان‌میرسه و سیتی میخواد اگه قرار دادش رو نمدید نکنه…</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/26269" target="_blank">📅 08:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26268">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRm0WPA8_GrpEa9FTZBx_ASPFwlVeLevO76Or60agZqVa-fmiG1cHQwlXPp5CfFkUBoFp6oqnaEHMtEmorIMXVs1X_Y9LD5RxTHi7GZmuI0C2XxMx8jdF-963SWuhF4RzbMi-0bOwMv8BKFD2b5GhZyO0RbPaasCzO4uHguq4wrppO85hz0BKigfmf-uXXmF-HeYjz7MYyUXvU6e_pwVfZIw_zjyey1TlGcXYNo7LzEGlAt0GyEAa3B0zsXYVPx04scT4aqXrSwnUeSCDqKUfujCqn_AjKnrXi6_ecf9zEJkUNEmnUgrvLumo0jqgFKy9gTUxrXicDcZWMDxPxJFag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ به‌ احتمال‌فراوان بعداز رونمایی از محمد خلیفه؛ باشگاه‌استقلال از مهدی گودرزی نیز در صورت‌توافق‌نهایی رونمایی خواهدکرد. گودرزی فصل گذشته یکی از موثرترین بازیکنان خیبر خرم آباد بود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/26268" target="_blank">📅 07:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26267">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/26267" target="_blank">📅 07:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26265">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WKTEYnfYTKLEAqg3KzR5I4_CBeGQotohlBt4hRQVko0bPMmasvpnsqXHj5uq8Oow5p0D99W_gKf8tmVjcqYdEEcaGevIo6v0MNkX0bGOV2S67Gj0Pq2dDL84VMOYdPyZMKeMppTn5f4gcQY2UOztqviZbZpXnEW6fla6jPvXFGeR0aPtHmd9wLxNkkRgfxt2HKGFpu3ihWvtgTvqQx3oslrKqYbl0vly3PvVj1gILXW3HAOU6gPOJMsFAjhTqdQRxRBsv0TPADZUBApidkVJrUjg2GOw0OekOlp1DMBol5uRYD3O1Wx-mtEca_BDFOM_aDt9MeL2b2Fbry-xSCiflQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lCvQ50ZdPs3rJrFlZXzLwf_Jpm7xmx0y_9z35IIkq2sVjC9HWsBRI2ZQ8vX9t81wuPF52-chFR5pY46bqvVTcsW1KLJu1g7-mA5YKdeh3crIsIqpY1AY6vPk90_lH4a2XAq3Swvl4_cMgJxFR4fH860nEIVhhF3FD4LtaqFjRAgM0OIKPHsD8Vimlib_cDN4B2SULcdAf9C3d5ZBolLMDRoHuMPmmAyYXid2pBd-1-TRkhGZio1TDp_oNI0Gkh746_cqEO3TQJjoaDpZS2yv9IMp4-Jp330os0p_hMh11J5iRga6W_QP3p7Jy_5er_7rmgPxqSAAi-pARL3pk3lGrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
اگه بخوام یه آماری از لیگ ملت‌های والیبال بدم بهتون؛ ایران بابازی‌که امروزجلوی ترکیه 3 -1 باخت درمجموع بین 12 بازی 9 بار باخت و 3 بار بُرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26265" target="_blank">📅 01:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26264">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-Ew5uGkTu5s-PSwI00O4msN0e3tfHAyrWzvGX0BPm6XmoMu6b1GNiI3jKZoHTEonpVQlbdqAhUZKImw5J0IVa4HR8gEAJZQfPCkb42gzqizyvnIWWH-EomoHEzx2CmDmqO242KIGr83CFxi2SNRGasHDspnpAV19sL13nVtWzxVFH_fMqvrh1LfYD_whwgDWK7315qG6abUl6LUV0cGPLG2HctAGvdrUCraf6SaDSgXDRHPtU32-UWBvWygYgCnXEHSKuOZOz4Q3EHUs2ccxGGAfUXywow60tGU34ir5CnZaD9pGOMU8BZxvDj0oRPKZof7K6H7Vje8s9c5az6xcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رامون آلوارز: بعد از ابراز تمایل شدید رودری به پیوستن به رئال‌مادرید؛ حالا پرز هم بعد از مشورت با مورینیو علاقمند به جذب این ستاره 30 ساله شده و بزودی آفر رسمی خود را برای او ارسال خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26264" target="_blank">📅 01:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26263">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26263" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26262">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ea272dc59.mp4?token=nKo98cItl3Cqt9kZ1hsA5eRFbcHQXVXsl_oLHqphXgjAc6UOjhzy5ZtjdmGdnzUn3jBFjrraRrOnVD6QhQeasoOikLwYxWuuG86Mel73XkkQ_oFK3u_52sADIkDC5fQtYBkbVaNVr4sMnEiV6BkhGbAlsmdaPd7CMs32DB1KxB8aAhpmOSRj1eB-cqSZ9u14-ITfe3n9X-YcpqhR8ktJ14DrG2PMDakegsxBT_NjuyyGYn42uOgv-a7jrvyTbxHgCS0H_Y3fFjqkBusXNlJAfkVXpgN727nNSc1c9MQFmAZv29VxCZCXL1oEK-uIKvhEqoz1WZsR_Zqpo-tbKEOEVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ea272dc59.mp4?token=nKo98cItl3Cqt9kZ1hsA5eRFbcHQXVXsl_oLHqphXgjAc6UOjhzy5ZtjdmGdnzUn3jBFjrraRrOnVD6QhQeasoOikLwYxWuuG86Mel73XkkQ_oFK3u_52sADIkDC5fQtYBkbVaNVr4sMnEiV6BkhGbAlsmdaPd7CMs32DB1KxB8aAhpmOSRj1eB-cqSZ9u14-ITfe3n9X-YcpqhR8ktJ14DrG2PMDakegsxBT_NjuyyGYn42uOgv-a7jrvyTbxHgCS0H_Y3fFjqkBusXNlJAfkVXpgN727nNSc1c9MQFmAZv29VxCZCXL1oEK-uIKvhEqoz1WZsR_Zqpo-tbKEOEVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بجای مانده از مسابقه فینال جام جهانی؛
لحظه بلند شدن کاپ نمادین این رقابت‌ها در وسط زمین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26262" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26260">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnsMc5xwQ2zTNs8Lqr3anvq8KdQDEu_pYIhMyIkixdx00V0tCuy9n7J-zBBW3T4OOZQOYC3JB7xgLv5R_TLgksYvIFK2RLsjt89Ej3spVpY15fgO-m8m0gKl63-d_nNKDyrCJ-9ER8r4nPoLS6egpDKs5CybC_uydnqOkUoQOSM4hF5BGW6lth0BA83qNSKMFtPfOlNDd1ntehazTdg2fLz6ftz69jdBnvhvLnBguzLb3KkwiRrTsgpriSbhOfo9oRWxCLsg7DI1vm8YM1D-fzGydwiNhji01z3F53FxjJs9Rjcwc17HJhmkeOFcycL--U5g5PyjlUkJ886nOcfV7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوری؛ رودری فوق ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی که بعنوان بهترین بازیکن جام جهانی 2026 انتخاب شد آمادگی خود را برای عقدقرارداد چهار ساله با رئال مادرید اعلام کرده و به نزدیکانش گفته پرز بخواد میاد رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26260" target="_blank">📅 00:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26259">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26259" target="_blank">📅 00:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26258">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3kWLyvKZzNYfq6b2UyAc2DSoZ-GcD38sGBCkFsRCr38zQ_iP9IzQ3-uzFCUr1x05vencE9kyRXFYbcVScriM-oHw54WV-Rn4tx3qTeBDK4jA_CP0xOiHxlC6OzfN8E1WZ19ojq8xFzLBNyiNEzHUFMLdM1xgy8J2qELNq5VsAYpJ-bEbVNyoW6O4iFGiKpumHRwTpageSj9NwwHI8JUCClZDOCDVavm9JCgGUUfzuFRxFNNkbzlvIDWk1s4JzmfCtPUJrptNLG98VQnzPkfQfzWubqWcYzxKJhwYREBs6orywFCAK1WvtgPdCC3_OV1fCRjZSzGaoIWYoTKVl7Jxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
سیدبندی فصل جدید لیگ‌نخبگان آسیا اعلام شد که در آن استقلال در سید نخست و تراکتور در سید سوم قراردارند. هر تیم با ۲ تیم هرسبد بازی میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26258" target="_blank">📅 00:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26257">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxjQBOzVyOqJ5dVCBznf_Z0qUqUuG0JH7m3ZiXssyf3zmez6OWEynd6VGczs-TWC5rrwXqk-UI_3AhcZFPrDQ3kEkstFB_tTmJfUpAlcIVzTvfsWNYdR1SFndpoTWWSMFQdKkeNehuBScB1UEz5Q926x16JK4PzBtRskBH9f9kQJ_19IHaIdW_VsugyeSY1bppQAHV_ATM7uesUa2B6gHGsC9vRDTqAlZKOE7fmUTBgScuQJzOZS_zXR3sOtO-kNiWLI4qX9SzuX8cvsOlrATP83SBFRMVBFMI_xKU1LzY78el_EAAnANHwXM9yGIjuO6s4pHpPilJExfkLhr8F7Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعداز اورنشتاین؛ رومانو هم تایید کرد؛ مورگان راجرز ستاره آستون ویلا رسما به چلسی پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26257" target="_blank">📅 00:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26256">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJPIW0F38-whcPbIR7mrbFokbcAywKaXyC10bpWaft46L33OVsx7meNG4aahHtXgUYYo7fLsL5RuSOd97cfXjqpLAyE7Kal9XZhjI_saWWqTykEssUsmyVKSJGkQyTsmIKEVL1NU3EJEGxdH2AxJmoYAXXFer-XVljUGAV2yPSODzl-7rInOnHjS0DhSEDFReyVaTi6QLjDJq00jYCmCPTZes-konqab1lskm7uanZK5h5wh8uu81fpvmX9B3PsoyD1s9s2ohatr4zFBmoYQV1UMY9uzGGFRTWiimSU3hDl6i8simJgsgv3jwQWwB30DQeSGkJ6NUlJMOsqlUwqD0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ محمد رضا آزادی که یک‌فصل‌دیگر با استقلال قرارداد داره برای جدایی‌‌ازتیم‌ خواستاردریافت 20 میلیاردتومان شده. آزادی درلیست‌‌خروج بختیاری‌زاده قرارگرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26256" target="_blank">📅 23:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26255">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QALO-1pOBDww_VC4jYHUm-xd8rFeo6RkQoV1APWoGnmdFC2inlK_N0hZbWv8gnr43x0WnQwrPcizAhGItFr1lwJHWhQy6MxZqipQ3_YMDG-z9PMA02BymC-2Rbekv-hEYA-86Yv682pnB2G7CnVfaQzJvjrMhbsToJoQTLxPELUR88TI7SfJ8EAZdebMq5Yu-BIMD7OY0nlgd1DoeU_2pZ9nOrYmnMelf3wJkbqfYXj3NpTfwBvb6csZ9nERUrrcC_3ZKVEklleMJRi2ReVLyoXdKY36C2wju8u8IhAG4OUpBI6aRux8pjcw6cbP6cCjPosQ_QoEFT1cxRJ6dwqqSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیلیان امباپه کاور EA FC27
؛ نوجوان و جوان ایرانی باید ۱۱۰ تا دلار ۱۹۰ هزار تومنی برای خرید این بازی خرج‌کنه. تازه‌اگه‌فقط بخواد آفلاین بازیش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26255" target="_blank">📅 23:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26254">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUEUlzevl4iUXt5ubwwiZW8WUNdTpuCD6DE1VZzvqqtjGa-01K_V7XJGK6C-1zge0dkPLwNpbFfk0xzA5K5y4JEbctwUvTm1vBJx9fCnirz8MdLMYXXNLZe8TQ202r77634LaKKZo7YnqfcjT-LzRbYwM3hmq7IMnxLZp2zpvlTGXBlgj1FSwlmWVPRLLUDuU7miW8dmON2dYPbPVctpI_vfN03tQBWKpeCnn8reYlo_d_RxpI_3vT_ExmmcEdaSQYq3lJLAP_2Ggb4clbWb6pdw62PXYDIz_AUonz-FUh5lCyKr5j_wkjJTV64EpvFoogcyzZRc3oG5iiy95vGQCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26254" target="_blank">📅 23:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26252">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42bce1c0ee.mp4?token=KBzJjuCH9T5wOvnUHcA-VX-Odm8yK8E-nlBooSzCwVSw-a7Y7ti4EQG3e01tJwOUuOaI9tLMrmn7e2CubHSO-yNI-OaYpVoVQDoTDZ5zPqL49pEK1bDk2MrO7wHFiT0dicd_JIe4tIAZpI4OnuHajf7W_qG0CVUjMaSbq3UTCcFJevu58llFCuijtqya4jOJwxM7Rk7EYw4QmAWbyPMYB1soyhKeQXzsyBSlVq9NuZbnBw53-_cSs2k_9j4CYilrGa1lzUpoiV1RcXUibGgpHhrJnzguoQBNfKU4FkWasj_cIXpfw2H97dbUAo215a5IFJbH22h-lwCLe7Xb5WZUSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42bce1c0ee.mp4?token=KBzJjuCH9T5wOvnUHcA-VX-Odm8yK8E-nlBooSzCwVSw-a7Y7ti4EQG3e01tJwOUuOaI9tLMrmn7e2CubHSO-yNI-OaYpVoVQDoTDZ5zPqL49pEK1bDk2MrO7wHFiT0dicd_JIe4tIAZpI4OnuHajf7W_qG0CVUjMaSbq3UTCcFJevu58llFCuijtqya4jOJwxM7Rk7EYw4QmAWbyPMYB1soyhKeQXzsyBSlVq9NuZbnBw53-_cSs2k_9j4CYilrGa1lzUpoiV1RcXUibGgpHhrJnzguoQBNfKU4FkWasj_cIXpfw2H97dbUAo215a5IFJbH22h-lwCLe7Xb5WZUSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویدیوجذاب ساخته‌شده از هوش مصنوعی؛ خوندن عو عو برای عمو ها این بار با حضور لئو مسی فوف ستاره آرژانتینی فوتبال جهان.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26252" target="_blank">📅 23:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26251">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b149394bb5.mp4?token=Z1ZwwtStfzU5HbOEAxMQy7EWvjvFBHiSG7hVNcCclcIXDg3bDi7AhbjaFOdrmfqRT_TUkYmqrDVHXtp5o61R3mtmZIiUVfaZoj6aqKwZOih_lOR2UgN3CPBu5h57dm2jhJOqrKMMiGTP-I0e-Q3eyPt6C8jxnQaM5WW3O23ulBBKdL2FNhHz416RzmCMJN46m_iieBg1LRaHbalo0eiwYMItw4LTuz72gCDsmtfBMBvcokK6HlS2HdPxz_lTUJz8bUcSe8OEig1qy5UycMQe7yP9RqFwwf7U5JaaQ0yuZslP1dIuAyee0GO2fPWA5TgsCXR2FviU0nDx31OKrnifDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b149394bb5.mp4?token=Z1ZwwtStfzU5HbOEAxMQy7EWvjvFBHiSG7hVNcCclcIXDg3bDi7AhbjaFOdrmfqRT_TUkYmqrDVHXtp5o61R3mtmZIiUVfaZoj6aqKwZOih_lOR2UgN3CPBu5h57dm2jhJOqrKMMiGTP-I0e-Q3eyPt6C8jxnQaM5WW3O23ulBBKdL2FNhHz416RzmCMJN46m_iieBg1LRaHbalo0eiwYMItw4LTuz72gCDsmtfBMBvcokK6HlS2HdPxz_lTUJz8bUcSe8OEig1qy5UycMQe7yP9RqFwwf7U5JaaQ0yuZslP1dIuAyee0GO2fPWA5TgsCXR2FviU0nDx31OKrnifDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو آخرین قسمت‌ویژه برنامه جام؛ خداداد عزیزی وسط عذرخواهی از خیابانی با خیابانی دعواش شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26251" target="_blank">📅 22:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26250">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmAZPMO5cRw6m91wx7N93XaLhzYF5al7v_QVyMRKt69CxaPk-DxX8ysgax7LEdFco0GZS1xXgkPskhdeeVE7GtqpoXUCxodrzKVqHnSnSANxvVVDk4elgG6Azi1DFW1xg_Y41Jq8vQy88j1exrS3FEpudD-4aP4AqRYz3eG3ZYm88_-Oq6SnmkHmLCt6bO7OFdxJCEbZtuYyOjWYyfxu8Cwd2aseowbFowgsnash4HJV-O5U2Beh7O6rvjuWcAuONiUIJC7-fft9WKjfaL71NFX1ukUxou6Z9BVN0BeXifoY6FWWlDYeLy8AZbHDm8RFarDxjYqKROLEM8OYFFLGvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ویدیو باشگاه استقلال که به استقبال رونمایی از محمد خلیفه گلر شماره یک جدید خود میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26250" target="_blank">📅 22:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26249">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2d1e4b083.mp4?token=nm5sJGhP5yPSEZFt_ZBYOCguA8lCzZFH00G7Cjb6gFwjpcO6CikbtSlp6928sMlx1BP2_6Ae4-Zy02xJgG23kG2VMwjxtpeYU4EXfJrpQISlgte9YHwOEPBb8RdQarDl-rCrnHGGo9Xt1ug9dOoPgMSiPxKJQmuqQq6UmpNUO37b_i6yWCiN6rqA6LuElHmF3waOaY6lnQ-hdKOCrYmVj1Zi7JB_w48TjNNRiYoHtGqdRzmdCjb2tVPDhpdFgca4614mMDyWCpp6qU9GBgLezJEGDNB6JzZygGMw68GPeTHMiWWZBKXcMCy0J8TVLgQYhXxW1V2hUC1hhO2EHSmexQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2d1e4b083.mp4?token=nm5sJGhP5yPSEZFt_ZBYOCguA8lCzZFH00G7Cjb6gFwjpcO6CikbtSlp6928sMlx1BP2_6Ae4-Zy02xJgG23kG2VMwjxtpeYU4EXfJrpQISlgte9YHwOEPBb8RdQarDl-rCrnHGGo9Xt1ug9dOoPgMSiPxKJQmuqQq6UmpNUO37b_i6yWCiN6rqA6LuElHmF3waOaY6lnQ-hdKOCrYmVj1Zi7JB_w48TjNNRiYoHtGqdRzmdCjb2tVPDhpdFgca4614mMDyWCpp6qU9GBgLezJEGDNB6JzZygGMw68GPeTHMiWWZBKXcMCy0J8TVLgQYhXxW1V2hUC1hhO2EHSmexQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه‌ نویی‌ گفته بد کردم ایثار کردم!
آقای قلعه نویی‌محض‌اطلاعتون؛ «ایثار» رو سربازی کرد که تو اوج درگیری و جنگ، با وجود همه خطـ..ـراتش پست نگهـ..ـبانی خودشوترک‌نکرد تا شما الان راحت بشینی پز ایثارگری‌بدی! «ایثار» رو اون پرستاری‌کرد که توی اوج دوران کـ..ـرونا با وجود خطـ..ـر ابتلا، دو شیفت دوشیفت توی بیمارستان‌میموندکه‌انسان‌های بیشتری رو نجات بده.. «ایثار» رواون‌آتش‌نشانی کرد که برای نجات آدما وارد پلاسکوی درحال‌سوختن شد و دیگه هیچوقت برنگشت‌ آره برادر؛ نه تویی که ۱۴۰ میلیارد تومان فقط پاداش گرفتی. حرف نزنی نمیگن لاله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26249" target="_blank">📅 22:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26248">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8899308b74.mp4?token=GQsP26b-sMQzmBpIohOZ_-ZWiwGErCXS48_9Uo9rc_HS9UJT9ZF3c7TFTrCgvLUFA_9mMezWPO5fAKfeY5p9jw0E5hnST5BAps356nUkRQF9Rdk44ohYb_FDVaWF_Am-TjT_IOHDTz7EABrwxVCzPSrrklxGNYySELUg3T6h9C5UtioXckJCMmB6G5jHa4xFMCwBkO0e6M8DB_KS9tH5CxMn1gBmTvF7M_PokI99mr4uHSbphB6RFok4kBoN2QpH82Qao3Xre0XR8tH4k6RRZyZBhO0J-O6gNnbh6GgeCY22y1P1NC52Jc4l-cAf4uhxRmKxnzfJ9Dhl3piYp-xJBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8899308b74.mp4?token=GQsP26b-sMQzmBpIohOZ_-ZWiwGErCXS48_9Uo9rc_HS9UJT9ZF3c7TFTrCgvLUFA_9mMezWPO5fAKfeY5p9jw0E5hnST5BAps356nUkRQF9Rdk44ohYb_FDVaWF_Am-TjT_IOHDTz7EABrwxVCzPSrrklxGNYySELUg3T6h9C5UtioXckJCMmB6G5jHa4xFMCwBkO0e6M8DB_KS9tH5CxMn1gBmTvF7M_PokI99mr4uHSbphB6RFok4kBoN2QpH82Qao3Xre0XR8tH4k6RRZyZBhO0J-O6gNnbh6GgeCY22y1P1NC52Jc4l-cAf4uhxRmKxnzfJ9Dhl3piYp-xJBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26248" target="_blank">📅 22:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26247">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5Hc7ecu-xYmKMhMBqU9zW4tzvc1vNI9g2WVa1aaRMoK_HYGQYV8U1lVXgSn3bOAUReYAitoMGHRFEy2_gAnaeerksrG8p-0mbYmRyuJ6AOaa9fTsyboDUaSU_J05zVjq4kRBMm7FPqbOSxl2bMXRRkYIdsNom0Kkr_6gIK9uNL1UOz1uAJA-sclJmeVnPsUJHQLLM_ZkU1SvdG7bPbbGEgjyzhEig-uyfs5yhN8CI061YmvuXo9XIqQG_Zw4oOi3o3LAM5KvhfDkKe_Q5T5SG9arqqYnurlPiDKJ5WQB3GFEBWmba9PK9NJOpLH_ckhH3Eysbuox2x-n-FTEsdisw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛
برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26247" target="_blank">📅 21:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26246">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIdjzdTzKa7oLzTGCNNgQtTLef1MyBh-4NFKzD8havK3PLmgKGG4SSjSAv87hTwkn4YozYk3ArbcAENTIZWVz03R-Ntj1esTpDHEc3uBFYKkRlOqvwKNkvH8g0TveoH8ljApLH2U8kTG0TPXtTbhLEUQJVZiHw5Hrp6or9El_Rr0ch0H8XY2GI6ytTUMuw8JhEaKEIyR3Yt5WORi1lWtI16h_JIgQhxHAQxP-Q2PZiOpWJLuQOA-NXHZ1_EgTajS9ISz4SoFec7i2Dgf1-2mT01OfmufhP0LPMyLoBTXVswYk0LSnPEiOl_LIZ9ezi2eu_Lh2VogZJVqJnfBvQo7nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
متاسفانه توی همدان بعداز شکست لیونل مسی و آرژانتین توی فینال جام جهانی، یه پسر نوجوون نتونست طاقت دیدن اشکای لئو مسی رو بیاره و از شدت ناراحتی ایست قلبی کرد و درجا فوت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26246" target="_blank">📅 21:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26245">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfYqtsD7wiclOhqbOGx4OFOnOccHqgIT0UCXF4X0vaZbORc5pxkXea6GgkDAor9v2guHgZi73ultg8vt3NYK6NaQPJJJzDbeD09ND2Z284okpl9UvqN3bvN5BYPhITR08Ch-bLLo6H2UU0_yoqUU8xipwu104231Os4SxqWjR5VvWx0ZzxqhkqGtrEOWkjpmj7WpGjHyMMbSgK5nce7TG43dRoCw43ZsDx1u5XqjDCUugLf5d9VPeg9fhfJvJWJsnfc8XkhrTCC-MYS5Cl-k6GZ0w0o6lvofWSYXvkwqDqapBmnJ4F1ZX1a4yS2HeGoetFecuFmvXmMpi94G_dHqag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇭🇷
نشریه گاتزتا در خبری فوری؛ لوکا مودریچ فوق ستاره 40 ساله‌کروات‌سابق رئال مادرید و آث میلان تصمیم به خداحافظی از دنیای فوتبال گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26245" target="_blank">📅 20:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26244">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/512d886ac4.mp4?token=aYuatHGzfLDcpiBcxrrfXvO-NsMJwVXMcDUOcaZjultxEJYa5XJTSWslwO1036YLBW3-VO28sJ7VmfEU0-o28ZWAKdXXN0Ma6hEc4B2Z5z0RXZM6K_zL25x3oS61bCQ6zKHK70VV3zNr6yGYnrciH9X4EhgY6CimoAH80nPk6uRScmrWS7ruLfQcvoolPqDuTpsUYNYTtMQ_kdXyFba8cxfmPgQq2Ufx2hxRUDf4z2vxKxdKDXcIhKnNNLyvU6glqMvAAzfvs8w3U_CzyObCfFEop_9Ic-GRa4-0I1QMqEKDjeRouIMxg2MSQpHH7_7XWks-_iurl3l6yWH24Tt_riO46abxN6ef6vjEMXEgwUSIzaKpn8U_EyZr0EcRMIPwSctE0v1brFPo6euZNO9UQfjEK2qQ8X_UZtFh2fSo8mVSN1dNLOvoIZ2L8ErwDvkQmF5xNSEYJJLenCsRFanVws139zRlr6IVvNzy_VSu-H8Ml6mor3Y7Iwo5FLJRjRogzt5Ct52zX_joxEj5C7Ahhp4z5oFFmTEiP3OwMohZOmh4baaYgfjG2XjQJVgoHtlcQ5HjoyNVAqRqxquuRO6IuAYFHE_fLeHRJM5gcxqUdcUtLfnY1ZAqjyCi2LN9FBuLeg8fn8OQP07X7B4NtpUJua4a2ca0pcDOQaygsbPontw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/512d886ac4.mp4?token=aYuatHGzfLDcpiBcxrrfXvO-NsMJwVXMcDUOcaZjultxEJYa5XJTSWslwO1036YLBW3-VO28sJ7VmfEU0-o28ZWAKdXXN0Ma6hEc4B2Z5z0RXZM6K_zL25x3oS61bCQ6zKHK70VV3zNr6yGYnrciH9X4EhgY6CimoAH80nPk6uRScmrWS7ruLfQcvoolPqDuTpsUYNYTtMQ_kdXyFba8cxfmPgQq2Ufx2hxRUDf4z2vxKxdKDXcIhKnNNLyvU6glqMvAAzfvs8w3U_CzyObCfFEop_9Ic-GRa4-0I1QMqEKDjeRouIMxg2MSQpHH7_7XWks-_iurl3l6yWH24Tt_riO46abxN6ef6vjEMXEgwUSIzaKpn8U_EyZr0EcRMIPwSctE0v1brFPo6euZNO9UQfjEK2qQ8X_UZtFh2fSo8mVSN1dNLOvoIZ2L8ErwDvkQmF5xNSEYJJLenCsRFanVws139zRlr6IVvNzy_VSu-H8Ml6mor3Y7Iwo5FLJRjRogzt5Ct52zX_joxEj5C7Ahhp4z5oFFmTEiP3OwMohZOmh4baaYgfjG2XjQJVgoHtlcQ5HjoyNVAqRqxquuRO6IuAYFHE_fLeHRJM5gcxqUdcUtLfnY1ZAqjyCi2LN9FBuLeg8fn8OQP07X7B4NtpUJua4a2ca0pcDOQaygsbPontw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇪🇸
🇪🇸
#فکت؛ مارک کوکوریا مدافع جدید تیم رئال مادرید درمرحله‌حذفی‌جام‌جهانی تا فینال حتی یک‌بار هم دریبل‌ نخورد. یکی از بهترین‌های این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26244" target="_blank">📅 20:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26243">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pt43oeGtEECsu9iEJ76w6L-_BBS8WxBME3A8otl6lTa4rH8AQIVbmhoYd-UcDu4IRwCujiVjOGFHOGAarQbEEX6pmdK1ITtqVQspryPWjsdRJiSOLPYRTTv6XfSngJXP50iewXsdinf7Vn-XSVuHmxM9b2mSczhSqY-ZewJGqFBkbeR7lDC4xz4hhDt25dXfXPn_wI9XFa7iIjLDnbF-jQVFIWmuelp8ME1DGOQd_9uSyXYFXoIken6kCsFt-ME55Ha4HG7w56Gl82EnL02OI48zN97ZBaHRetHaG9MjcMSgnIBDstK9g2snMAs6rsbbpp31tArA26aVYvLG2tq7lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26243" target="_blank">📅 20:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26242">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ckc6EvE_irc_0CMP3NFbGLY266aPOBrIoBzY7PzzUWzARYqQThvE0d0Kd6DaHKSADB6LRFItLT6FdPUiqFbsdLllAdcAf5PzOwe-syHozxfvxfVjEyKt5hrKti_H7P4fIToBgnGQRfIrWZCrqJH-EYHV9iLpvV7g3R_1BdmXDbiCXRGB2EmmRXkLdisvFVav54bNBP1-rbqMYLG1dOV09D4eca9HjMbR6hfjbTT7-l6hbaEP_rOsaO1q7nifC_DIAyO7E3t5rNr6iRLw6jqtq9Duw-jPGJ8bJ1gB7Xeh9P379qz4eA45_Uuh8QHsmTiDtiVVIrcEgD3Gx-OxtvuKWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ رامین رضاییان ستاره آبی‌ها ظرف امروز یا فردا راهی‌ساختمان‌باشگاه استقلال تا تکلیف نهایی‌اش مشخص شود. اختلاف مالی بین طرفین بر طرف شود رضاییان در استقلال ماندنی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/26242" target="_blank">📅 20:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26241">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufFO7qWCRguYLobmgFmM1zQCEtim-ncNii662mhbopx6R7XroNE9wuh0xJAlTcXnYoP0QVaHuWIs1mqrBIXmL96SJ1kfJSSgV777Oted4HItq0Su3-SR0311Xh2cCpP1-aPfBoccwd7nh0AHHl0HmNGL39DnJpGkqm9pmcAsJrj68j3I3u5PUnxtYk4AAqwO8kQD463zlt1jpQTy3R_cwnhNEZu4fkQ8BLNYr1PHBkrGednJ9Smf6C2mXdMEv5jfo82GARxDZYDkwzYUOlVvhhiedEg5-x1AOW_-Z15LnYoO6Ycv1fmvSar_zbm6qQ4quYVaK-s_xr8WLik8F9wweg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26241" target="_blank">📅 19:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26240">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOoKDWepeHPMxHbqtKkvtEaoZGd1RhzC-BQnf1UzyTW_VSNlbgx7lnQCTQMnh0uWmS3f5JS-F3yl9V3AC8cOS7Z18aM4aDjK6hChAxRsIQIgj7Nn81bAX9AI4_C-RTWOMvk2DIHQ-6J5Yq5aKcfCB2eqfih-W9pFEtbR1qZPz1tGdTiyKL2te7RJrckMRkr7ICt_IpYbXlqtGftUxxyD2Zt7mmep6HYSogvnLQss4mDmZ7kG932NjRyDcInj72wfPQyAgJHD9gv_BvQTdUAvlHfRNCkbUUBZyxW7LEzsDhsa1mnO1XHpwA0V-d6Nkw6rYe56tTkPN3D-EmyM-sWzSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26240" target="_blank">📅 19:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26239">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbgIfxC3YBTDW7zd6K7Op24GCFWXcCw2ejWza4sEnxyu8d-2FvG-FY_teK35qt8FWYm3pwpHbzzqAB9H2hIGwIXdYrZc3tcyRPALrGdsUgK-_2lb4SczdjBddzQ6-gESelDyLb3u9FWWB6m-y4P7R9xU5b2ySo6vpI1sWOD0_6m0C8OxQdCmnKtTdC_JWJrGiS-fmHl9o3HOil_pyLKJivQtZTjFceGLdWUgIfrNEqBWLwuQFv53gxRIjjAnVLgdoqJTiKEr0X_cR3GBksuGiws5bH0rfDO9uIA-BCaavKnBU1p8rGuKzCxT-AIIiolY6ZDpE-qxxGgXk1EaiccU-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
تیم پرسپولیس امروز عصر در بازی دوستانه بادرخشش مهدی تیکدری 2 بر 0 از سد خیبر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26239" target="_blank">📅 19:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26238">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fe98fee7a.mp4?token=ipbvhfCtL05f5HjEWN6J_CQgnBWIjrEJjJzLL20BK2zaeA_izALvvIdg6jnyXOCCIgjJMI8PV_ReEqCn-__VoQCjPqrdUsOV2PD9ZBOruT1lhThtff9csQYvyfraTW3Am7iJiTbOYwwCtBT2j8VG1wNf3t8K4RrgsoifQolNsFK_1xgsqMFsi4309AqVRBboe-yn8XJelYFHmegdXntKjkXLVnKz4kMOjnbERu_WtyVWEGkWJBt5NFToA7-WieP_HuaT9wodWwwf3ATaJxLONEmjUZD8xm886xQlD-UOGN0oUqEP4ob72HlgbDYNH7DCbR-eW2cKL5OP4I9nJz5sPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fe98fee7a.mp4?token=ipbvhfCtL05f5HjEWN6J_CQgnBWIjrEJjJzLL20BK2zaeA_izALvvIdg6jnyXOCCIgjJMI8PV_ReEqCn-__VoQCjPqrdUsOV2PD9ZBOruT1lhThtff9csQYvyfraTW3Am7iJiTbOYwwCtBT2j8VG1wNf3t8K4RrgsoifQolNsFK_1xgsqMFsi4309AqVRBboe-yn8XJelYFHmegdXntKjkXLVnKz4kMOjnbERu_WtyVWEGkWJBt5NFToA7-WieP_HuaT9wodWwwf3ATaJxLONEmjUZD8xm886xQlD-UOGN0oUqEP4ob72HlgbDYNH7DCbR-eW2cKL5OP4I9nJz5sPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
🤩
انزو فرناندز ستاره تیم ملی آرژانتین: بعضی‌وقت‌ها واقعا خودمون هم از خونسردی لیونل اسکالونی متعجب میشیم اما او میگه من یقین دارم که‌دوباره قهرمان میشیم. همدل شده‌ایم که قهرمان شیم و لیونل مسی هم نهمین توپ طلایش رو ببره. حقیقتا لیونل مسی رو بیشترازخودم دوست…</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26238" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26237">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sArB9_ptgAaAgToxoT1ze2RkPFPlQYpDMbzA0yOjImJIexLCj6REBMzxdHIg9dYmZuLUkmLpUSdIjBUHLR0Twc-wvjPR_X2zQfX5RxDVAILv3Pj8UcoErFnIrmXR1QlOWomKuzNEAVlkCQkDJEo7Ks6uJaD45fscLwaot6oMLIRdZKEHHn5tKX9Ka21sZzwRx8-G9goHFwB29Mf7_43n9uVPLayrv5VNAWOWxif15mJ5UBm4n3G0d6TZpvUKHmJyEqlZgk0Dl1rIeyvbdxkWj3inYoB_JrVa7YzFUKJBRm0fogM_-9VHXgoTgYmx0ZImIsBzxF8TaRbmWkC28vrNWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باشگاه گلگهر به‌‌درخواست‌ مهدی رحمتی خواستار جذب امیر رضا رفیعی دروازه‌بان جوان پرسپولیس شد. این احتمال وجود دارد که درصورت موافقت خودِ رفیعی، این بازیکن با پوریا لطیفی فر معاوضه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26237" target="_blank">📅 19:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26236">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-JdNPZMNFEISZhuB3ikKbrpFACIXlfwZw32C-408kLoRtH8f896ZmdPziHpbQktwQYWkW5lS3DRwMC-fYp19gDuuQLjtKGd77diPou3wzpy-qvgDf6wYClrU5CnAB1ow2v0aKhaUjzXEFwzA7UB2pupA4mxsz2Vcebh29ReUysWSknN_8uVYw1yCcg8DQvGOLaOKbwzFdYG1w8Hhvp4fyxN4U9xBIsoHkMnWzPXy6rrBQNwjVngTTRX9gQ5N2qbrDMgNxzsCylXBYuUPLqDPnhaf_WRppMRlzQeMOXmYHVR-zkwWnY7vDNghCrOhbOAVB-s2tpwF_xC0_09GISGzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/persiana_Soccer/26236" target="_blank">📅 19:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26235">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDJiZ7qGl7bebz89KB8X_ZE_yVBQ7Tc8w_lfYd2K-ikimj0Mxex7RTmwigU78gnyb6jlqc6q5uqjTETSMVYC7X_EBQjUbg59QKwHk9ayhOom-OOnTRIXOcysIarzDaHGRFGRCC4OpZKUVBTu7fsta0SmCp-wWOINmLXSY4kVNB__4v6Ltlc7indoWYoRdIZsH1mG0XV0yvp-318m2-PXllP-009lOS3tnZTAEnIEkTRZ8BtBu43hVbSBEnBTn_rmYAnpbTRmLMcexA6GcceB6kC0G2aU_ifeeDY76yzesTH93U9rv20Y8Q6Z7l4WBSpa2XJ5y2z1hYNA5URKqzhEVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه پرسپولیس دو هفته پیش با ارسال نامه ای خواستار جذب فرهان جعفری هافبک تهاجمی 20 ساله ملوان‌انزلی‌شد که‌درکانال گفتیم. باشگاه با خودِ جعفری به‌ توافق رسیده و توافق با ملوان باقی مانده که باتوجه به‌فشار بازیکن به باشگاه در روزهای آینده رضایت‌نامه این…</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/persiana_Soccer/26235" target="_blank">📅 19:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26234">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59137224b2.mp4?token=UoIhuhm5VZbr7WxDzjv7WY1ESLKXAle9KrNCpTPydonzn-SgqjDuC7mmge7ccuVnSzP7kuKgj6IW35vo4_Y9yzlrITXpnZP9JcrwAXmtpVsZS9PLH2bzBTVNStGqISS9FGP1b-XtiP11CeBLlmeaXZ1OfXdYBASvlP0yfrfi2WiOdF9c5ds2lSvzKFDJpyuZzvNP7YWs0xE_C6dnMfvwrNiAl49aJlejOiHMFvIUN4K6DXgJGc-8B_l4x2oO2zO-Esu_72pBpP_4HE72zVRKNpUvbz5Azu-Vo1b_eRNDWJ3vvLALZdQYlGw-YxEFxSqJGh75IlsZx-FxWrO8DqFGuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59137224b2.mp4?token=UoIhuhm5VZbr7WxDzjv7WY1ESLKXAle9KrNCpTPydonzn-SgqjDuC7mmge7ccuVnSzP7kuKgj6IW35vo4_Y9yzlrITXpnZP9JcrwAXmtpVsZS9PLH2bzBTVNStGqISS9FGP1b-XtiP11CeBLlmeaXZ1OfXdYBASvlP0yfrfi2WiOdF9c5ds2lSvzKFDJpyuZzvNP7YWs0xE_C6dnMfvwrNiAl49aJlejOiHMFvIUN4K6DXgJGc-8B_l4x2oO2zO-Esu_72pBpP_4HE72zVRKNpUvbz5Azu-Vo1b_eRNDWJ3vvLALZdQYlGw-YxEFxSqJGh75IlsZx-FxWrO8DqFGuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
راز ساده‌ داشتن بدن خوب در کنار ورزش کردن مستمر؛ به‌هیچ‌عنوان سمت آمپول زدن نرید تا دلتون بخوادعوارض‌‌داره. مستمرتمرینت روبکن تغذیت هم خوب باشه بدن خودش یواش یواش میاد بالا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/persiana_Soccer/26234" target="_blank">📅 18:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26232">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m82BLN5LzHvuy5DLdj3cAJ6xQOs8t849bW1YCSHA5QhZFTT2xpKMVYFkzICRkOXm4ZT3DgvjIX-4qaCPBQDveBOP8KZm6DUT_E3jMovloON27o1bUwppF2KshB1RrbZRLmutaXe2jt9iWzRWX7PvdjAUqsQc4j85pPlSmf-1hLtSZr-D5BY2Z9CSkhhpxFT_zSSERGqGFrlYrUpluDds9LOXzfGl0f9YZeYF7PPC0jm_qiB8i4shTPyRbU4i0sRt9Yt3xDtKv4oF371yhUrsit-eGqQWLZxjpzBHiYPS5jHLAXwhO3yAqoAzZHl0GAf6aXbX3sy_8q7W5IZy3CHcIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EbATQIudk654tOBPFMhh10CtbT5Tpvw_6mc8XCHO6SAkKTEltG32k1-8idFzpq5gA7VezAdC0I0EbeaLMXR4T-zSVlT1WPHk3okVvcrZiTGmGMxDCLLHMKG-5oALI2zK-ysIno243q3QcFnnTw1OlpA72ga22c5Ck3MrAq0xtkz_h-LpXavrtA_N67QB32lT-Uuhrw18_VR0oZxmVsBGHlwrrn8597P5E53ubyCBAjZs053FF7nfnKqEs-90JSKfkiv-cOeMNREu2_DlLtGNkVLCIcD2DUyw_btF6ROeG4krFTwwuMTt9QpWyLcFzj1M4B0U0EWicIFjXY2YR12njQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
نیوفیس وینیسیوس‌جونیورستاره برزیلی رئال مادرید درکنار پارتنرش؛ بعد از ترزیق ژل زاویه فک و چونه‌ اش خیلی خوب شده، اون غبغب‌های زیر چونش برداشته شده. فقط این ریشی که گذاشته‌ قیافش‌رو تغییر داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26232" target="_blank">📅 18:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26231">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhbnYkLKJ2-G6CdczbkZYqjrPb8jOEgJfuzpB8-DS1qkx7e7pYb6XlIP53eDdO_bNEmO3zlP7sB4XJJ2F52Po84Eu511rhlyBB1FivLW8_yOWicZ0GuEmrFYEjGszl5_YgYxlWZy9tETa-4IE8fLVIzLBUBMGFuss1DSQGnYbyx8T-vamgnl8HGJpVunKXAxd0FdvJNOKKesRJ9wcF84s3pOr1itHTaEAB7Rm-wbI2T4iA5ONcIBcWqGiXtVRayXXQEdC6M8jN0LAwt5pB0F0-0buNupBeQBCR9Zh4R9elOgOs02J5fToUzr_TkblMGmNXJGacCWrYarxNUgQlXVCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
تایید شد؛ با دستور مسئولان هلدینگ خلیج فارس؛ علاوه بر مجتبی فریدونی، محمود رضا بابایی نیز از هیات مدیره باشگاه استقلال رفتنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26231" target="_blank">📅 18:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26230">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k97RaNzcnx1vXVLnJZ0-VVAc9POXYOZ8BAvfOxMclKqDOi-u_yP6UYCAFqPN9CyogFAgTrDhR5z1l3IUqxfl87usPMbaULcLuABMw9lqS-KChfzJI7klu6xsP1j93go1I-Q8MZceukqp6ze3Yaz7nGy1y2YKKeV0eJ-Emm1bA2uxSncqLMhmvZotnq1oFf7xR8mUb_UPKfs6Sx3G87x9It-w-ceWOwtd5jxh-4GE7NcomY2CBoBjkLAiN3SL_n9SZMiWbEe4atvjKi2kj_IvDl6FcYn24XOv4UvJyurBGJKoJVawJ5FUvggme-YhUuW7MJcIiIup-kmwuoMr2C2wMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین گلر شش دوره‌اخیر جام جهانی؛ بوفون، کاسیاس، نویر، تیبو کورتوا، مارتینز و اونای سیمون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26230" target="_blank">📅 17:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26229">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwEILN9Z_U5VIxynsnN3YmnVhfL5-MNoardaN1rdppj6M3HlYtckXxjRcSIJO8tvDxa94N6ggJJuW5IhCd86Y2Nhv1QPbhVtNWrZg-StN-MKzTy2DS4m_e5sFBlc_8AjPlc1nIY-EuFrljEhVRfVSERwi7eFF6jZ-SgOK0vv_vKuXr8Wrwn-KDDNEkbblZknUAColw2BFNzqvB4TGbMeLOmrLnVmLZHQpupeVQSefvQxWYOLgDt3AbiTPmWHUVzoQtNox23Qk1j1oCjoH4gNif1bdjKrsb379X24F_v5kwxNVWHKPpwq6cWA6mS-C0P3rdvfH1AUw_j1wo8b8b9IFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت رده‌بندی فیفا پس از جام جهانی؛ سقوط ایران و صعود اسپانیایی‌ها در رنکینگ بندی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26229" target="_blank">📅 17:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26228">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3639cfb2fe.mp4?token=kWx5TsltHWVtQvTKXOhDYR7ZC_1ed_ev_FVOreAW3rnMAjC1JQtUCG62Xmcs0a1b4IqBfZFIXhZy7seiwuSIu00WVtk21pgMDPYsSjJOnwu7D8Yi_mCrTk5LfexLZMAE0RU9She-uOTp1uHNs2IVvHioeaYWRIMrsEW0EFYso5EqLrrAnfbuCbCMrWJq8G5aKQkG_hwSuAXXlrpBFxD9RBE9EuR8IhLeaz9G0C565Z18NaitpfZz_UIdaWoD5wZmWeVoOD-4mbF3iFzMLXDw7BlGmC3oKlJ2fzMYexLsCkQgeTfY2HF1Jv2ti45pxlMPeodVnNYJBYOc3B1TDbuYBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3639cfb2fe.mp4?token=kWx5TsltHWVtQvTKXOhDYR7ZC_1ed_ev_FVOreAW3rnMAjC1JQtUCG62Xmcs0a1b4IqBfZFIXhZy7seiwuSIu00WVtk21pgMDPYsSjJOnwu7D8Yi_mCrTk5LfexLZMAE0RU9She-uOTp1uHNs2IVvHioeaYWRIMrsEW0EFYso5EqLrrAnfbuCbCMrWJq8G5aKQkG_hwSuAXXlrpBFxD9RBE9EuR8IhLeaz9G0C565Z18NaitpfZz_UIdaWoD5wZmWeVoOD-4mbF3iFzMLXDw7BlGmC3oKlJ2fzMYexLsCkQgeTfY2HF1Jv2ti45pxlMPeodVnNYJBYOc3B1TDbuYBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بعضی‌صحنه‌هاگل‌نیستن امابه‌اندازه یه قهرمانی ارزش دارن. دفع‌توپ‌کوبارسی تو دقیقه ۱۲۰ از همون لحظه‌ها بود؛ جایی که با یه اشتباه می‌تونست گل به خودی بزنه یا پنالتی بده، اما با خونسردی کامل توپ رو بیرون کشید. این فقط دفاع نیست، یه اثر هنریه.
و یادمون نره؛ فقط ۱۹ سالشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26228" target="_blank">📅 17:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26227">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ec8c45572.mp4?token=PhPgQTVM5qPUu-bO5-fz0XhoL9ZWUHPz2OSsco8QUu-5KSspd1U1O-9Yo6haLXmKo0Ilwb-MnZ4a2HNr3aPTClcnLf868x_dliu1a8yPAxqATD9gS-wmT9N4oM7Qjs3KWAneB77uxYICbfoANBjTLvA9rjQ9oh8L85C0dWGPmxP1VVrqPnAySPnv7yYFaixBnsJia0QJ1kQubS1bQSQYYY4JL4TDhF2X29LYehTj2a4WsLwDRKVelBBeOsT-5gClhQi7fi07PaVFIagV3fHG6E6OmQp7bgHR81SXNAhAat_NSYAp6y0sdHveLFhrpNEXTq2aF7S8skAJpKc8De577A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ec8c45572.mp4?token=PhPgQTVM5qPUu-bO5-fz0XhoL9ZWUHPz2OSsco8QUu-5KSspd1U1O-9Yo6haLXmKo0Ilwb-MnZ4a2HNr3aPTClcnLf868x_dliu1a8yPAxqATD9gS-wmT9N4oM7Qjs3KWAneB77uxYICbfoANBjTLvA9rjQ9oh8L85C0dWGPmxP1VVrqPnAySPnv7yYFaixBnsJia0QJ1kQubS1bQSQYYY4JL4TDhF2X29LYehTj2a4WsLwDRKVelBBeOsT-5gClhQi7fi07PaVFIagV3fHG6E6OmQp7bgHR81SXNAhAat_NSYAp6y0sdHveLFhrpNEXTq2aF7S8skAJpKc8De577A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حرکات عجیب لامین یامال ستاره 19 ساله تیم اسپانیا درجشن‌قهرمانی‌شب‌گذشته؛ چرا یهو کشیدی پایین؟ یه‌درصدتوپ‌طلابگیری میخوای چیکار کنی؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26227" target="_blank">📅 17:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26225">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26225" target="_blank">📅 17:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26224">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dp1XMM2KoiLiZOV24Dve6w6pl55Fcv5ClaXoucGxfW9TKWovBHHmwq1U8p4ikT8hIpqCr52sYGWi8fy4EIaLl1mRruc-rkX732ddf2lyU_ku7D5vuzaYpgqaG6KIHX3QlCcln1blM7tkj--e31GL-wi1dfXY43yvSbeD8xqmhjpADPwIoaByL2w8rsgAXtUi4ndOCAjicjqg4lUga-eKZ0O0ionjKiY0o5TKDiwvUJ8b9Nfk5FX5OVGXtU11MzqNjYqneOqC2SdJBluF6nmHbnrMfxGC5pWcBQRGVQV1Z-T5hVl_N8dPxiNkxgIGttt4iY6vmvKCLv1BlEZDTbxB3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
◽️
👤
#تکمیلی؛طبق‌شنیده‌های‌رسانه پرشیانا؛ مجتبی حسینی سرمربی سابق‌تیم آلومینیوم اراک که در روزهای گذشته مذاکرات مثبتی رو با مدیران فجر سپاسی داشت. امشب بعد از جدایی رضا عنایتی از نساجی مدیریت این تیم با او تماس گرفته و صحبت‌ های مفصلی رو با او داشته. حسینی…</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26224" target="_blank">📅 16:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26222">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kiFU-tPZAySPVxMQD2e22g8q6_Y9_ipEwlfWNPOzMm7xWmAoykq8LaM2nZUHH4qmZUv5XcQ9VYelY6nsLO5lFJFz5NmqPWE-g8lhcBgRzNTLSjP5XwRkXBOwqjWJJoX_ZbhqwVHHpPacUMDIWIH-ixJBtF5NLSRRVOUACk3fAFZudGJDd6THvCHpDWUR3n-ce0Iqcpk-b4XLifZMSNA6ES6jRu8SdldJ_1l0GKTSCNUt_-am-XmDLpop4kPYUQ05-DFmRRbTcBZFLxXnwPCZY73OXT0y2ySqdtcPQkyGBd8ypKnoQ5BA-5QIQAP2enUBeypddxzV4kf9gqbgd1JgqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W-nRr2qQ6k3ZbVYNKCgiegZ4f58Sp1uJeZ6f_jIPSbBfSqGm9xfzfhfDGLkQX2K8iKniZdZdNJOl0GhCjLNHqKAbhzErO_0WlIx25L5xZbnut3-J_OoLNZFsbzqPk665uWN0sE_T4Z_ohSpIpa6IciYk5jGriupY9M3sOaxhiDyFI8NzwMEEMYd9D2_4pX2klJW_tLOrwhkj_UvTShM_Og_tdoPaFieBlM7klxRdF1UgZa2Yx9EGcK71O5edhfPVHMVeWV-9ZVHm8olG0DRx7Kx19NnBENhMfAI0_UG-XAK-0Hh13K808okYDhDII_etjRYG4zbp6upuGHhiaGEPiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
خواننده‌های جشن قهرمانی تیم ملی اسپانیا بعد از موفقیت در تورنمنت بزرگ و ارزشمند جام جهانی.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26222" target="_blank">📅 16:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26221">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAmPOsZMbqEXYrRFaTOolF2MwYEtGIm6WWoU6gfiLk_kUoe13O6wMlXHsuQhG5os5CBd8V-PEk6IpRo6kowl842dA8lLYCMpek88gYNQgEtbOAd9OHH58p_DiSluSv3gqgP3oeE-UI--wRtT3iCi0yA6n-ZEiKSKrH44adN34IlL8t-zCoyD0sW0omBMJaEAWuIPepN16DGIGT2Z0AVv59jaZjwgNKzVMl0DkNqx4eI8Ifxu4lLdmjyX3b0jsSBbTOlc6kDI7EE0SvTEnlW8artGILZfDeC1VkpDSBNba8FrdxJkcdS9WEVqtABjogvcrV9k5PFzsH_m9MQ2CZgtDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26221" target="_blank">📅 16:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26220">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKwIyGq6USTve6EWky-PHRQ4nPZvgkZK__7WKE5MU3Pp4Itn3LVNnIObNSCZneHBH2X0YPIbDy8kxdNNRkpEXYIF3C3CwqVYsEqCX70YoGnpJTRqUgEvgS2FVN7agBYYeLBY-6CjpV9hhpNW763TKxcPKE4FtXMJiAIjXfB1lWUMX4jFcm9mUIabOllDbcBKpCugj9YHbR81z-0c4qyMUUsq7OywsJ1YMahMWTbdOrySpX3T1StzgywTEjIUpMJ9bpOHFBwVRI_uhLvtrQ19K5N6sC1nqx2IvHWDsffM57Gdhtn88Mazb5FAdwhvIxs-4kVprWf3Aq2uXs7XqruDng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
درحالی که با قهرمانی اسپانیا هیچ گزینه قاطعی برای کسب توپ طلا دیده نمیشود ، فرانس فوتبال در آخرین‌آپدیت‌خود درماه آپریل "عملکرد فردی در تمام مسابقات بزرگ و مهم" را جزو ملاک‌های مهم انتخاب برنده توپ طلا در سال جاری اعلام کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26220" target="_blank">📅 16:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26219">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1HWfE7EJMV6mZJVGJVBhoChV_iEJknqoIC4OQZG2WosfBGhDRPLGgFw7zVWI_5t6QTOZNNhxH64AWYUxctgWnTGJicEB99feP1eqwdVusB3oIl3IMVha0hh-kX-Wkj1WtNR76cWlId-Fmf1tKNhFn71L3VLcz1qZNiodybe0HZmmikdaPlp2CY3zWCP_jSNEaCz5oHXWdhLlgbazZIc1YNbhJlS6bdBc6pN71MFBPrcuNExfcxkhzz0uiD-F-If8bkZriMUvf52by9oav7eo0FyYFE_1oizGgeus9MILAUUZK7KJBXrMwxziSpbV6lBqTopfCjdI0HT7SaY9KU1Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رقابت‌های‌جام‌جهانی 2026 با 655 میلیون دلار جایزه نقدی، گران‌ترین دوره درتاریخ‌فوتبال شد. 50 میلیون دلار از این جایزه روفقط اسپانیایی‌ها بردن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26219" target="_blank">📅 16:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26218">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxTaK2WGBL4qvAw2doyPGXtt41PevdPQ5XMNsQA8pu0Bp8OO0LZL-zMeUsNG7ACYAOlfLYPMl2UV9YihcyqopgyqsNBpkWO0ro2wfRx89M930qKJFEU5075fUmBwFmUu5cIV1Lm_LQqcBpt7QtZyjEEj8-JwDlACeKrKGm2dnoatgP0BU2EcLsvN4kMg_KjGKwgpjdpYOD4WjNkWKnBzu8_3OxqUeE-_qzuntBktqW5RXED5LF9opobN7gav3J_ePP1ipERmIyvfxvaLrJXdKg6L1ip9EaNihTpVt4tOZeOuXxJtKlCqtPJwjMrN39NSBQH51D3BFDc5JhNbiGiheQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
محرم نوید کیا سرمربی سپاهان؛ علی کریمی هافبک 32 ساله طلایی‌پوشان زاینده‌رود رو در لیست مازاد این تیم قرار داد و کریمی به زودی با حضور در ساختمان باشگاه قراردادش رو فسخ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26218" target="_blank">📅 15:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26214">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0GNkyp0MmLQjXg9Df1a79vzMQ_3_LmWTBXdfVBT2rfv0M8Q-bD9KoJzNFVYDMbKngziTbTabZB905g7Ka0_gUjgMkAUtYNCuOhpeKc-nmxBWWXGmfhzDRQCPAm47O4HLgYmFSNfI966_zHbQtbsM_p1Pzy1U66cjZsb2U_hmyr4ZL0w-rT0gJ4e2js8dY3a7xVbgvsFPv5RPnXBLZd3wl_OhcgsgSQcfKabxGaT0dqUjBaFeRm0NJE0jG2bCCTMtyiYPdhPdMoyPKNypkfJ5TIOYHzXdkHGWzdvmo8AbFMomq-sP2AA0gKcik-hXOXvXNpLdNFtLj0NHVRVrRWt8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوری؛ رودری فوق ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی که بعنوان بهترین بازیکن جام جهانی 2026 انتخاب شد آمادگی خود را برای عقدقرارداد چهار ساله با رئال مادرید اعلام کرده و به نزدیکانش گفته پرز بخواد میاد رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26214" target="_blank">📅 15:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26213">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcJ0hzZducq5BsxPR9HRvjfENWOdat6mUBWODDbe_m25skEWNJmfdwMWSWCITHZpX3DDLuoO9ZHnOu1QUa_lIDTWtWc_B8UEakLtmk5OjrEsfoa2mhiLxXFiMwYZVsAY5rGtsTj4cynkIqPWnKR7w050--edG60Fr02mWI_wZ2webfu3nBjf_fVKrgS7DSa9b4CQ_eC_C45VD7BB99ubKQ9QTxAwtMb_Zi9RQV-r5jENKUmSAkHPMJBIdWiCecSNbMWCO07al2649AZE2ZnT8M0HcxjRowqrL1cyhNEMJPKFSN90Wq-j3IWsyK1_Mck9wi7gW0UxdY9pzInp1klrRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26213" target="_blank">📅 15:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26212">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfG4HWMl0Wnxmx_mDHAhpoR0RiMZL_rT729QE5iSQkvYTIfLiqmdBZCKSxT8Mmwvq1EP8OAnLyTAWJCn7ZfbJbGuELzFsX8RIeJ7vriQUcuzAL0iTUsgtqNk-XIUNAEK2JrC0nQDlBZSW4YYcuj4GyUE3ZfRkwDcrFLucL_7IMth3-fRTdekxd0dzOTPDLGTj14U66KvsJfOO_hYbMxeCEZwnEpWEd9uLwho5_Ctxs3DIJScNjyNE5-BOYZWsmHU0io3H5m1s7YYEPm6MG_HUe2HSWY87Tovmkonhj5qXlb60XhrkZuszy7NWOUv3YK6IVOwkfd_8KCu0raZCfzUlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال ساعتی قبل باباشگاه آلومینیوم بر سر انتقال محمد خلیفه دروازه‌بان ملی‌پوش ایرالکو به جمع آبی ها به توافق‌نهایی‌رسیدند‌. باشگاه استقلال بزودی 60 میلیارد تومان به حساب باشگاه اراکی واریز خواهد کرد و رضایت نامه خلیفه دو…</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26212" target="_blank">📅 14:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26211">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOycX0uCJfv9Ji070YsdebnPrqgGB6znwoFRuHbPOoHPOGYuTCIPPRixMESsqgYJtb8LUgjLAkMCJ8udA6phWadwpXAVU5UeyzvQ4H7Ymp3tPr1QJ90_hHS0T0YjHKeb1AedYIHiTviz_HzuajIoKuw1eMlGfUgwbOvu4RsRWY4eWh9B2cmivIlYlNaQR0rGvu5lOinB5BNWtWDfQx3_QYZFlCGx3jYaGSZSdWG1YyNmLos4VxUw5kJJLgI2JZrOAZXN_jrHfB79rxzmkN5lcVAKDkmEk5g1S06DF7KrKVHRFZ_XGwTDr1P3cwIqmT9Vs1-wONJ9ip2AFjpnQpV54g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا؛ علیرضا کوشکی فصل آینده در استقلال خواهد بود. تمام‌توافقات برای تمدید قراردادش‌ انجام‌ شده و بزودی‌راهی ساختمان باشگاه خواهد شد تا قراردادش رو سه ساله تمدید کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26211" target="_blank">📅 14:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26210">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e65zJiwAk2pFYlVMBaSjdSJOZUzbZbbGEC3_5-20UOYeU4P_PZZofL6272cu6bjq_3MV6XxOAxEel4Puu8OUThdZtTVDaxkNS4aa21N5GUO2UK2FPWdtNj1POQLBSdluzx2J0hL9bt7EK2R_d3E5mtg_Isglqec1HB3OQe7p8CSsZcD3SIyep8XN6e0Hhp0lZ54I6O8CywSOEhQkHupDW6l1Q8zooSljyfr-m-dZ6G87AvF2ImwBjBBx37IOht-6KcQbGHsPhOPNNlzNE4vFLBmIV4PaWiRUZaB5DyuBqCrYhAloHOQ-CvzYH_nP9IT4EL1M8KeZwIzzgP2h9ddm8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
جسی بیسیوو وینگر 18 ساله کلوب‌بروژ با عقد قراردادی 5 ساله‌رسما بارسلونا پیوست. آبی اناری‌ها برای این انتقال 8.5 میلیون یورو هزینه کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26210" target="_blank">📅 13:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26209">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqBDlD-xCUeeI_wBDqAh6-n-twn5SMcxdfanMn9TARQkU4E-zeNSTaJwDOqsff7_zD1CiUXdPJDm7Z70kQgInnv8EefWuDO_ZFObTIJ8rSbB7xGfpZrxKXb3jjV7_2H8rk8WcnG4BaTLBoiNnjxTpsEPk0zLcK8C7olLTwtOEJZh-fK3lP_l8zBA3WXRpoCKD2N4OJ480VfXSVpm3EFPX-yYXh4N-dFLObDrYsCUXyJINVa7dxFZUVQazuk-I8JL69WQVHQnHFZmBKNT4HGbWftyDBkihSuM77_jzK9abl_ZwvhqRb-UUe-15Fj2yl9RMGdSEb8hw-ZnEMWzHz6AGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8XbSs-XsTCoVLZtRBGlMbdtBrqznBeXgRULZBy2HN63IcNzH-K0hIz6W-3SiFxcoGfh2AIfi2W07J0AfSAkLgKvdJ2FL9LzE3M4CyCDrXZ-KCldlsy3RrWt5tk2vyqgkH6tETQA7mgyU1WbJr-XI9_iOg4hXI4kISwDm4EOM12kSSairQ6POwBP6AQ5gpKP-CC2pdnYuOgKjYLHbFxLhh8mMF53I3O2xFzqs4r79dVp5-KuwGUEkMz2aNsNVxzsd7TfvyACi0HzMS8oYgqG1eG7QqzONPBiksGvFtEOL38w_P5nWP8EWtPvJ7e10lOXzeF33OFPco6F4kYtZwH9ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی 10 روز پیش پرشیانا
🔵
بهرام گودرزی مدافع‌چپ‌فصل‌قبل آلومینیوم اراک باعقد قراردادی پنج ساله رسما به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26208" target="_blank">📅 13:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26207">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AwkPARDP2_K7QzKr9-xxTLvf8ChOziNJeOdoE0505nA-fup6Q-D1DRK7K2M1_147SxbL-KM2wbb5qcxL_jEhsNhc73hbPpM5jPOHIeCvDLbKW2KxCF731zU3ItPxlF8wJH5CyvqMbKAVfDdgSlnJZbLC47d1mo8zC3hcCjKgAbzvxQ0QQUrTaps7_h5vP3FZXmfZAXzd6Oq80SNZvjP_3KqqDUxZS7HUGxGNLvYwPeEgPs1b5j-03zC2xh0f-YHiYeu1G-l3pBxg-k-kkDNBp_wwCup0eOg22rwIGBF68pW094PT8NhOZ0zS_PDY_VQX9iVjZAQPjjLEbU8qpCKZhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق شنیده‌های رسانه پرشیانا؛ مدیران هلدینگ خلیج فارس از عملکرد مدیریت‌فعلی باشگاه استقلال به هیچ‌عنوان رضایت ندارد و در هفته پیش تغییرات گسترده‌ای که مدیریت آبی پوشان رخ خواهد داد.
❌
علت نارضایتی هلدینگ بابت هزیته هنگفت برای جذب ستاره های خارجی استقلال در…</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26207" target="_blank">📅 13:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26206">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ydgk4YJiAciRPOTBOqlCn4qxRNvlYtzAQbftwAwx99xSwM0YVtQQe5W7N9MqXj0IFtRDj3oBu6XFnDGG237xHMlqBnpYm7uyN3O2YmWXu5TG6xI95la0liwy5LnyVctgIfVcB_tSQ6Qqpr-SYIpMiuXhIVPMWMkdybtVWYK0yAR33d3S02oepupUfY2p4dKw3OATPIeGjYjeTSIbWhTm7e5yCGwUExEytVny2NNifKCkpicYkPvcofc5K3kiDUZSdKUa8VhWvvmxIKkzb09lUVgX7AahAopLWU0m0dpS8pRc7LZ9tY_d5tUTs291y7POFqcnb9OKPyPI1yFBrfFJCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
#تکمیلی؛ حمید مطهری به مدیریت باشگاه فولاد خوزستان اعلام با هییچ رقمی ابوالفضل رزاق پور رو به پرسپولیس نخواهد داد. مدیریت فولاد به پرسپولیسی‌هااعلام‌کرده بود اگه‌مطهری اوکی بدهد این‌بازیکن رو با دریافت 80 میلیارد بهتون میدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26206" target="_blank">📅 12:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26205">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ASeLZKXd-73v4MbO0KoZTP8aGSqTVN03I_BXLGRl-b7ZDCVO6cW54mM6tExPpq5AxPyfxHXC3WNsJdSdfcvlsDFzouWYKHAqeE_qpQZvqsHZrIReJkFGTjxjrAsH1Awm8sHSfZF25PWtNepaW_wa7A_zyHjysQ5qgGx4gBhCrW9EqzTkHccQdjlxpFKYIjK0McPRp-0NzMxpnPU1dH2iWT8HVVd0go_lzDeJJI55iy27-YB8p5qf53esdS1aQBMEUcDYUUp9uAwO42DfTOS8ZBx4y--flCbOydd5BBAr9yVYrdv210IO0s_Di9BiCpoYlUAstn7uCEAp3UVwZkzY6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
سیدبندی فصل جدید لیگ‌نخبگان آسیا اعلام شد که در آن استقلال در سید نخست و تراکتور در سید سوم قراردارند. هر تیم با ۲ تیم هرسبد بازی میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26205" target="_blank">📅 12:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26204">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">▶️
هایلایتی‌ازعملکرد بهرام‌گودرزی مدافع‌چپ جدید تیم استقلال در فصل گذشته رقابت‌ های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26204" target="_blank">📅 11:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26203">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FkVPcJm6oTcxd6xwlzW0DNsFBq2LIl0pee_PytzgQmrRfRS9Z8zNhUWJc-0JsRiT_WhaqARZpseZ4wVnC97WlbRYQK9W_UWeLZpz6tYnZbhA-iqkFmjZEXu6L7SGdV18PSPvUGAfQf8t-phHbYYlrtqkR8N10gEzPk244ElNzwlsAsRADCXYAObQmvo8tvO0XnU6_93tCi5-PbYQX4seIkuVbI-g6TK1NDgiecBQ3APEMaGakbO4schf2bc8r4gGcmBB33Ol5P-CWzIY1rfv8gw3uiBuWvFROWJ5HNtNWJsszv41-TM31VxB3atBDLcvctna27djAIkUZPXXFmfKFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ باشگاه استقلال بعد از محمد خلیفه؛با بهرام گودرزی مدافع‌ چپ 20 ساله باشگاه آلومینیوم‌اراک برای عقد قراردادی چهار ساله به توافق کامل رسیده و بعد از باز شدن پنجره نقل و انتقالات آبی‌ها بلافاصله از او رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26203" target="_blank">📅 11:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26202">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6cc5dfc32.mp4?token=rMZgW5GCQueXjaAz2Yio5NkAq8ijpi87_qJYt4IThmq8e7uAhwJiANOyK_8HhqF3ofMeC0W5rmwd0lOp0Crl59a2tWpStJSz9RemNgRhQebBo3dFGbI79KcneoXJWHoix_Km1daNz9KSF2T6ppQpvoK2avTbHyR6Ej9JCbebxx9rhdqbGRpio_nFIO5RDAs4-sLaKjD9ItVDfFx6bk_FX5jPJBllfdEpR5uztaH4UDCFOmOG1XYvUmBRv5e-ldUkwB_zg2sxLstZkYd6493e0uNrUXrAz5Ctu0gkURllKXmExPYmB03tliYgnbnVxi1zOpvxWX9q-K-7bo_ord-lrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6cc5dfc32.mp4?token=rMZgW5GCQueXjaAz2Yio5NkAq8ijpi87_qJYt4IThmq8e7uAhwJiANOyK_8HhqF3ofMeC0W5rmwd0lOp0Crl59a2tWpStJSz9RemNgRhQebBo3dFGbI79KcneoXJWHoix_Km1daNz9KSF2T6ppQpvoK2avTbHyR6Ej9JCbebxx9rhdqbGRpio_nFIO5RDAs4-sLaKjD9ItVDfFx6bk_FX5jPJBllfdEpR5uztaH4UDCFOmOG1XYvUmBRv5e-ldUkwB_zg2sxLstZkYd6493e0uNrUXrAz5Ctu0gkURllKXmExPYmB03tliYgnbnVxi1zOpvxWX9q-K-7bo_ord-lrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/26202" target="_blank">📅 11:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26201">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTmy196qypOs34UYjheZ3g_5jiuhBHhio1LaAYOR2xl-UNB_h5XVooKcRT0WXtxTOMn_Tp8K3i7QT-xTFMF5_tbjFctEWk0QPF7coT04yCDZLlbIWyh7UM6ATlhjMyx_Mf9Isy7J0XPYZhiThFvytsA7dpYcVf4JKvmEdh-fGq1j3M8SMwLSeB5M-aqLN1DlmuJlITQZeZRSTOwUXhh7PHFdB7fdH5zv2cJ_UKC_odrmWbGCdbuEeqTkHB84HEPvAAJz7U7eQZzjTMwFBgtRcCYeI61WaoQHdAWYEaR3rB3Rn_40VTOueh5rboGqLrcVP7EaxHXTiLtQ0ZfdP-CD4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد محمدی مدافع‌چپ‌فصل‌گذشته پرسپولیس باعدم تمدیدقراردادش با سرخ‌ها با عقد قراردادی یک و نیم ساله به مکس لاین ویتبسک بلاروس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26201" target="_blank">📅 11:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26200">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZAf0t-cun2ew5S5bSwckTUecZnzOUb0b_iHk3aJgPXaURBBIBpwgpKSt5N4c7vz8FU6cW6tInOu8Ahz4n0-iBofwkB72226SqfCuhYIE99FmofTW0oMJ3yIJojpzofVrIzFr59Y0ib6hyZbpn7Y_MUtAG-CJPLCDJowPt8ychmJiugTV_amSmZ4IBSPEA5jpSSyYvO-q5ne8eTrEU1iiNXESyr2A2heZWARRGI3G5i2L6qEw0elC4Dw6r4gMoOv-ngUtQkVEyPm0jBb-5cAtTFlyrmcGIXHOZTU-cuW6xY4D6uWrmG58CTdVJdtzC_6GcCHK3OUW4HHKqRBCRPV4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
علی تاجرنیا باز هم تاکید کرد: انشالله تا آخر همین هفته پنجره باشگاه استقلال باز خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26200" target="_blank">📅 10:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26199">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljXvGzfCQO-PU_Fmg-wEWsY_q77nV5xrxRYMLrIoys7U8rXi1vEi-1-LVOJBPbx9UafstwAvpU7tgLMkPYtU0X_8Qkgky1x9V8GZ2QcsZwqvhGT5M7ef7LKYE9HD7Euztl_9rVrs62JZ0LatbF5u8xtTjDBCWRMgfFNPlulsjyMbhi46_UjX1kKYcg-N18Xcf2vwANoIiwWZpAY7H-2MWwyWpy3pvG_tex5P01k9fjg7OlbXTkUWesNPZyoQrHBhF9RZKdeUdfKRMIQBo6xufobfRP-OumU35I0JUUV-GAlKGKmQ5OBn38D1CPi2-R97fknMk_gUmwhPVkuslmAWVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇭🇷
نشریه گاتزتا در خبری فوری؛
لوکا مودریچ فوق ستاره 40 ساله‌کروات‌سابق رئال مادرید و آث میلان تصمیم به خداحافظی از دنیای فوتبال گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26199" target="_blank">📅 10:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26198">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a3189b48.mp4?token=S0_DYphxV01hR8608FDq7z6cFCTESIs4Q_0IeHPN4bNplCY1k1nJzdsO76bHTGoCZ6vQkEihnfT2aSIemdkWyOkv16lqneDiBOzOhN-_CKkB5TGewOCgIVlpKz9Z5dehZ6f_5ZO_t6ZEnmCwD0YzT9XApw2qXx2dYwSu1JpBU91yybx-0qEpV4QTIgZr2g009a1P4ME_7IOhHj12O3t_B2YmmDAXCkFZMlTeli8bVn3mqNBqwGDDqavD-mgXqLvp5INuifIL5tyR_szrK8Ud-Xmtl43qlZLxjhOEYj2CFgRTcu61onergs4GEggRwh7RTntKaCBB4ucK8q4SCX8agij0NQzYwp2USOZ8A9N9wWSHIxAN3UpaI8ftyEpeScahqQfBFiTxlpGc1UUQL9tVKfgiX0M9JtZk2BsocNy9eqs5pHod0uMATYZcxhXLx6t5T9SyzwIQy0GqzFHtxctuLGykZ10F8Dyc2MIPRXhjy9o9IQNCCnwwn3zUE5YwevliKI1-UTmOMvUDlwEi2KVB_eSgUacHLVTQ-nFmn31zxWOmnjWuxVWLkMCoc8rWNJo7b1NBMS_xpdIWfbEyMU2ovq4om9uZQkH4cCd3XyG6OxCaycTYe01v356J0qfae7YICFGWvpizFdoQo-lgnqajK0nMpnXgxVnKmXglREbDEXo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a3189b48.mp4?token=S0_DYphxV01hR8608FDq7z6cFCTESIs4Q_0IeHPN4bNplCY1k1nJzdsO76bHTGoCZ6vQkEihnfT2aSIemdkWyOkv16lqneDiBOzOhN-_CKkB5TGewOCgIVlpKz9Z5dehZ6f_5ZO_t6ZEnmCwD0YzT9XApw2qXx2dYwSu1JpBU91yybx-0qEpV4QTIgZr2g009a1P4ME_7IOhHj12O3t_B2YmmDAXCkFZMlTeli8bVn3mqNBqwGDDqavD-mgXqLvp5INuifIL5tyR_szrK8Ud-Xmtl43qlZLxjhOEYj2CFgRTcu61onergs4GEggRwh7RTntKaCBB4ucK8q4SCX8agij0NQzYwp2USOZ8A9N9wWSHIxAN3UpaI8ftyEpeScahqQfBFiTxlpGc1UUQL9tVKfgiX0M9JtZk2BsocNy9eqs5pHod0uMATYZcxhXLx6t5T9SyzwIQy0GqzFHtxctuLGykZ10F8Dyc2MIPRXhjy9o9IQNCCnwwn3zUE5YwevliKI1-UTmOMvUDlwEi2KVB_eSgUacHLVTQ-nFmn31zxWOmnjWuxVWLkMCoc8rWNJo7b1NBMS_xpdIWfbEyMU2ovq4om9uZQkH4cCd3XyG6OxCaycTYe01v356J0qfae7YICFGWvpizFdoQo-lgnqajK0nMpnXgxVnKmXglREbDEXo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
این‌بخش‌از گفتگو عادل و علی آقا دایی و کریم خان باقری در هفته گذشته بیشترین بازخورد رو در فضای‌مجازی‌داشته‌وحدود 50 میلیون ویو خورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26198" target="_blank">📅 10:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26196">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5WZF_1xGSk4y_3qg3M-yQpcXSS0v8o-x47gqLw2aL0icPwL9t1_M638W5ItCmRjSrgxD7XVd5W7nZVl5WpH-Fhckgk3HOsUKbRLx3NB_TotCbrv08XtcejW4nOgs5WKoEsRBIQysGYePgrgWhWDIiQpQ4vbvMIarufF2YU158PWurGeq8PSv2nM4o-MqLE5T3_5cR16AZgVA_oUhHAgn4K_atslJnp7kg1Zxvt_SzC40q_wdxkpF7TLv1ReXORjBIz6nAU0b7xD8BYjBMbklwkcSwgj-fVTDV1EHiozI4xUZvZFMwhq61FGgUtBCj4OeaUUDf9bMlyuyV4QK87vSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برسه دست مجری صداوسیما؛ تیکه‌ سنگین رضا جاودانی به میثاقی در گفتگو شب گذشته با عادل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26196" target="_blank">📅 10:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26195">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTtrcKafik6tg7SdO--VRzXoOpFqYXNez5QEQ7tF0YatDCBpLHeuQVcdvTKIctHb_u5NL-AkWOX-4rqWAO0edODrc-FBQV8yzQd6-wGboofsS8ANmvfV6j6lSY0fy6Q1ql8V3UsfEeE-uxOgFpdksAccvU3gZG_Ro2J2l9E133I1VSUsN8EJG227l-_OpussFPJyUiNdhh99msPadvMbBjAWg4Cw201p1vfH0tdxwTMCFLMwHBk9uN_hf-zPEnfc8EaaRZiVWPwcr-AdbGc36Gs4ycoSgFp9REHjusfWkh2NeGdhrqk5IkW2KyV7bDetXZbe92t1jaFl1_yIcfUCPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛پرسپولیسی‌ها برای‌جذب ابوالفضل رزاق پور مدافع چپ فولاد خوزستان با مدیریت این باشگاه تماس‌گرفته‌اند که گرشاسبی به حدادی اعلام کرده درصورت موافقت‌کادرفنی‌رضایت‌نامه رزاق‌پور روبا دریافت 80 میلیارد تومان براتون صادر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26195" target="_blank">📅 09:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26193">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/944a94e4e2.mp4?token=km5yq4YWQgEFQmgDpvl0ekhO3Tlm1hfSXNF0UaNOswBZJ3W66PJIcRzS0uCEIyCt85Rw12qdnsqs2-57a8w-jo9goOJA0-peGOn7I-IpJnGnfpnbtSeQrXv29JPDbd5VBUjvYXWvjEkq_JBnYxh6Z-QMPxZB_LFBQHM7BLZ2PhmBADcAmPduyEffkQnMxwAxRhVEg6v4EMxYwfvnWlpgXX_nUqP5ZK2dVN6v6fe0zenKP48vDfGTv1FwUXBAIsaMmVSZv7mRyJc231SxsC2W0lL7OrZFTqrVWxrHumax86kQOpr8ZUBsqB8d-_F9wXXrLUoD7QDn12oKn4JvHgepfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/944a94e4e2.mp4?token=km5yq4YWQgEFQmgDpvl0ekhO3Tlm1hfSXNF0UaNOswBZJ3W66PJIcRzS0uCEIyCt85Rw12qdnsqs2-57a8w-jo9goOJA0-peGOn7I-IpJnGnfpnbtSeQrXv29JPDbd5VBUjvYXWvjEkq_JBnYxh6Z-QMPxZB_LFBQHM7BLZ2PhmBADcAmPduyEffkQnMxwAxRhVEg6v4EMxYwfvnWlpgXX_nUqP5ZK2dVN6v6fe0zenKP48vDfGTv1FwUXBAIsaMmVSZv7mRyJc231SxsC2W0lL7OrZFTqrVWxrHumax86kQOpr8ZUBsqB8d-_F9wXXrLUoD7QDn12oKn4JvHgepfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🎙
عادل: من هیییچوقت بلع قربان گو نبودم و نیستم و هیچوقت هم اینطوری نمیشم، اگه میبینید با من مشکلی دارید بیاید دستگیرم کنید و هر بلایی میخواین سرم بیارید ولی من بله قربان گو نیستم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/26193" target="_blank">📅 09:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26192">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a85e23671e.mp4?token=EORTwlxZussHVuscVzTzBsvp9WM5e5B0xRWrzZdZA9CwQbxh7IXHh_cDJStp-qb7xHOF7RFqBP_XiMCyJg67X6Ha2uILr-JSDi8iz8dHB5Cv7y0rxhqlMOptZJgjMWdBCfqr8dnoFBH_pQP27L3yDNiOWhkYxH9fGKdyWl5SDRP3kkhcbuzK1bBSrU9PwdTFAgMRfF_36qVo-J189ncpHWBNQ5Cwg2n0zmyTY2DPYIm6BVCahjVJXQT4W9NhLcirSzVAM_QPo1ys_jvbm9sKCuGH6An4ec--PUoP1bRyVs0MICpju1f9K0IAWcIY51TVR6z4fG4TQv-R1rDDrFCHTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a85e23671e.mp4?token=EORTwlxZussHVuscVzTzBsvp9WM5e5B0xRWrzZdZA9CwQbxh7IXHh_cDJStp-qb7xHOF7RFqBP_XiMCyJg67X6Ha2uILr-JSDi8iz8dHB5Cv7y0rxhqlMOptZJgjMWdBCfqr8dnoFBH_pQP27L3yDNiOWhkYxH9fGKdyWl5SDRP3kkhcbuzK1bBSrU9PwdTFAgMRfF_36qVo-J189ncpHWBNQ5Cwg2n0zmyTY2DPYIm6BVCahjVJXQT4W9NhLcirSzVAM_QPo1ys_jvbm9sKCuGH6An4ec--PUoP1bRyVs0MICpju1f9K0IAWcIY51TVR6z4fG4TQv-R1rDDrFCHTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26192" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26191">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72d81bfda.mp4?token=Pv_JOBRty3hP0ZAcsUmFqz6Bl1OlK32MFxLfl_fgADJr48ld7G0awJAb-aFWliYMUCD05K4yt8XccyBkyTpE_De5dq_rjvxf3JWqC7vif6fAVcKrkrNZgRK83VDeoL8M4TcY2oieW3a4CJCCgiTjElRSRGdXXbdycENAi5SztWRNVknzRL6YumkfBbDk1ciHVHW7i9hzumAMq4H1ws1ww9UF4OMORshCMVQyYM8ZAaM00HaNOKozFgAa26gTrahdaCsYMtlHSo0jmqHPPnD-4W82goyzHTK1n2KOpT-P52VHg3a_nvxtKlICu_AoA4b06ezHeKlHXkPB22jb7LgLag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72d81bfda.mp4?token=Pv_JOBRty3hP0ZAcsUmFqz6Bl1OlK32MFxLfl_fgADJr48ld7G0awJAb-aFWliYMUCD05K4yt8XccyBkyTpE_De5dq_rjvxf3JWqC7vif6fAVcKrkrNZgRK83VDeoL8M4TcY2oieW3a4CJCCgiTjElRSRGdXXbdycENAi5SztWRNVknzRL6YumkfBbDk1ciHVHW7i9hzumAMq4H1ws1ww9UF4OMORshCMVQyYM8ZAaM00HaNOKozFgAa26gTrahdaCsYMtlHSo0jmqHPPnD-4W82goyzHTK1n2KOpT-P52VHg3a_nvxtKlICu_AoA4b06ezHeKlHXkPB22jb7LgLag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🎙
عادل: من هیییچوقت بلع قربان گو نبودم و نیستم و هیچوقت هم اینطوری نمیشم، اگه میبینید با من مشکلی دارید بیاید دستگیرم کنید و هر بلایی میخواین سرم بیارید ولی من بله قربان گو نیستم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26191" target="_blank">📅 08:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26190">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkZqT5XqV8j0va1pB5ItzrRiY1Mfhtsx-o6EmzW8BG6jlV-XSBCICW8FoeiRkP2k5ohJfGzJZHF1SyINqxQoyasnnUbHFkpYmXykJs4d-qbvHyxxJr_8eVAZ_GB0F85gMXvmUXXrbyH9nmOm9NTBg5btwPfR2ctoYumq-SKMSDdS2F9yAyw7fC6R41VAu5nqeJbJHzCgY8XiH6v-iVnZthin4ilJkZbGDAB64_p_LzZtdz-P5z68Ut9e_NIo3Tt2u_JSkBgMYsZ1yaMx7djinA1Uf6nvqh6gthrRjCteVASm2bklEQoZV3iNvRytPPhINz4k5VpidxmEH_IsAQzATw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26190" target="_blank">📅 08:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26189">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWetJRHy__0qv794XPi46gH1TetxMmxbSw4_AyEqMkMqju_ohnJwUb-2Nvq0WfvwfoAzl5ESmWooBBBB2YUpn04kNpkuqJfOnqoPc0Rdr_Wx9sgqjbjQ9vtGhHYtpaUqqUbqpc1fX2luGn-yzl43UB74HiCJdDb-keuPtOAAO87FH8hq6OisGrF9OBhwiJEZwVZEcn_PIlVoj_-7SRD830qhnRL_BM4uOmlwFI-r4KFs-bPOBFQIXEkwTwnOg_Te7B8SbgeAgolmA3Q5l94irspdCCiZfv6qQkC1o-CKTGe3dEEMGoiKbaTbfKD0S0Cr11RSCoi0Wb_OCCNhK_9-fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی #اختصاصی_پرشیانا #فوری؛ محمدرضا اخباری گلرسابق‌سپاهان‌بعد از تماس مهدی تارتار دقایقی‌قبل موافقت خود را برای عقد قراردادی دو ساله با باشگاه پرسپولیس اعلام کرده و اگر اتفاق خاصی رخ ندهد اخباری بزودی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26189" target="_blank">📅 08:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26188">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc5216b419.mp4?token=dm3-kiHxq5nFF429blXvgZcO-QBTu4oy82HZ8B-iV17OlSslF27UloCoxAQpxoSEb4NiScnHfRU55hDJRAkuv5NeMZJ7UaptXdMN4ej9aTTaF4IninbocRYpkl3I2xDpdH7AN3L5Ar3mofASotbaho-Fkb5ttQnErhUC9FclcXr6dtGst3OqGkC46X3tEXoWvdnW2HVLGuvOjtN8Dk4WjNk-9Xakw-lWLkTg-cnuwQJDirirQ4DlE6I5OK5yEBNbyOURbYCOxMu9GVgEW97RQhcry1s6lAksxq1gj05F2BbJRvF5HjrcUhqI3PsZzoF2WoH7y_0oAFWIwwqE_RVKUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc5216b419.mp4?token=dm3-kiHxq5nFF429blXvgZcO-QBTu4oy82HZ8B-iV17OlSslF27UloCoxAQpxoSEb4NiScnHfRU55hDJRAkuv5NeMZJ7UaptXdMN4ej9aTTaF4IninbocRYpkl3I2xDpdH7AN3L5Ar3mofASotbaho-Fkb5ttQnErhUC9FclcXr6dtGst3OqGkC46X3tEXoWvdnW2HVLGuvOjtN8Dk4WjNk-9Xakw-lWLkTg-cnuwQJDirirQ4DlE6I5OK5yEBNbyOURbYCOxMu9GVgEW97RQhcry1s6lAksxq1gj05F2BbJRvF5HjrcUhqI3PsZzoF2WoH7y_0oAFWIwwqE_RVKUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
بغض‌عادل‌ازصحبت‌های حاج‌ رضایی بعداز توهین های بیشرمانه امیرقلعه‌نویی و فیلتر شدن پلتفرم ۳۶۰
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/persiana_Soccer/26188" target="_blank">📅 01:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26187">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e8c2669f2.mp4?token=YGis8AQBx69eB1bQRG-7gEt4U6myK3XDSkRCauos4dqePnzO_BSOBuscqUu1Y54WSMIgoZkkcabpjEMVsxv51-1vVuxxWNV_qGh80OI3AmeSLE0FYCHmxZrPBARHKtM_mqFUUlTmRnCm8aUxV5Z3oBdYt-vGiz4_FNf31B0DrvRuOxfaKmXBepaK6YMMqJiJfS_E6Ju_6eDuOaLIK60l04eE6ATHfMmbVczF7sWMCt6ZDZEgCi3p3V15F-jpyJDHhljLh_1m0GrJwXIl6txXyXDJ4Gun_zS8ufZKyj7V8aMDNKvhrhvbFN1cDcinYWwCv-4f6iiPRh-68G5Wc6yZ2l-SKI4t7nBD5al4mI1kZcoweHZmDIcRlTGjGeLjmhKe6GvMyO-u6rLlxgXpwPkvoWYNcWd4p-Nmmkt3rxeK9tQ6pMXrg94a-Y4lQkslG0_J_12Oe0irx0LHWd7Nx_UgNeZvQKXb9e9qi7qWUnbYTALSa2-QD9z9AaPy0xapnEyp8QfSYQGVNnfUubgNVNCrOYGDQH13PaMVo5GgGB7yhNSiEfXgCK6BLLoNB7HhBhyKdI-msAnhstY0GMl9m5jfwUrdSXdrHt_sC8oF6fS7Mmg6PTOM4hGz-rm_QczJ7_NX8o9fcJ9x4hQK8XSIP2LZn0ymd9VHOj98T1--jBHc4AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e8c2669f2.mp4?token=YGis8AQBx69eB1bQRG-7gEt4U6myK3XDSkRCauos4dqePnzO_BSOBuscqUu1Y54WSMIgoZkkcabpjEMVsxv51-1vVuxxWNV_qGh80OI3AmeSLE0FYCHmxZrPBARHKtM_mqFUUlTmRnCm8aUxV5Z3oBdYt-vGiz4_FNf31B0DrvRuOxfaKmXBepaK6YMMqJiJfS_E6Ju_6eDuOaLIK60l04eE6ATHfMmbVczF7sWMCt6ZDZEgCi3p3V15F-jpyJDHhljLh_1m0GrJwXIl6txXyXDJ4Gun_zS8ufZKyj7V8aMDNKvhrhvbFN1cDcinYWwCv-4f6iiPRh-68G5Wc6yZ2l-SKI4t7nBD5al4mI1kZcoweHZmDIcRlTGjGeLjmhKe6GvMyO-u6rLlxgXpwPkvoWYNcWd4p-Nmmkt3rxeK9tQ6pMXrg94a-Y4lQkslG0_J_12Oe0irx0LHWd7Nx_UgNeZvQKXb9e9qi7qWUnbYTALSa2-QD9z9AaPy0xapnEyp8QfSYQGVNnfUubgNVNCrOYGDQH13PaMVo5GgGB7yhNSiEfXgCK6BLLoNB7HhBhyKdI-msAnhstY0GMl9m5jfwUrdSXdrHt_sC8oF6fS7Mmg6PTOM4hGz-rm_QczJ7_NX8o9fcJ9x4hQK8XSIP2LZn0ymd9VHOj98T1--jBHc4AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
اشک‌های تلخ عادل خان درویژه برنامه امشب؛ مردی که پیشنهادهای وسوسه‌انگیز رسانه‌های ایرانی اون آب رو بدون فکر کردن رد میکنه حقش این نوع برخورد از سوی مسئولان دولت نیست واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/persiana_Soccer/26187" target="_blank">📅 01:29 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

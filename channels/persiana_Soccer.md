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
<img src="https://cdn4.telesco.pe/file/peoXE9vanxvysLb0_stXpi1BlvuRyLxwVF5e7TR_N3vGE1ytQtS3Exn0n58MdQa3yb4HRbjdO2Ts_aH51m7bdHrB6oZG5ZMyxnR3H3EgHK7guApVMjeQRrZFEmJ2f_1R1H5U0fKQlUHm62WTq4PiNKlXfL271Tn9ZzSKIe6IBztl75_LaHFIpEa6dPA57UPuz6yCzaRhsQBJMabDBn15lxVSjwmTVu8Xy573AhqlYr3qhoUimX7_UPIzcQ2Y1U91YLScDXOuf3vq2OsRAWFcNhw52CAjRytfL-TC5SKesMN1SQRML-YhNdWc-jS8oh5fQ11uf7AV4Upo-sYzT-0BRQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 444K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-05 16:40:44</div>
<hr>

<div class="tg-post" id="msg-30551">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFNY816gG9GwlA4koRwSRO3wl1l6rVoUqNqDtnT5v5fET_CgoS8fWfukE04WcKBszrJFKvur9i7QFuaXCPa_bTlAFgt3RHW0XSxbaJlyq00SM3MDL5pb7GfUpQ9syuuu_wyTEnWBs11-IUwy_FHRRsZUZE24oODPsS8rN14_GDrhHT7E1AXXS1yE233GEIDQUtPCa0LMbnfxlbrpD3VSBWDBla-2qlnKfv0J6NXk4_yu9OF4xV9MALE82yjr50VjzXE5tibOdH0jwlJtMSisObEmHKp2o7mQRXYOqNygIgPfSLIimcSdYzlzKqdgFV8T5B3fGplJehaAunaQ6Tx8Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جما اتکینسون، دوست‌دختر سابق کریس رونالدو گفت که بعداز جدایی‌ بهش‌پیشنهاد پول داده بودن تا علیه او صحبت‌کنه: وقتی‌از هم جداشدیم به من پول زیادی پیشنهاد شد تاپشت‌سرش بدبگم؛ ولی من قبول نکردم، چون واقعاً هیچ چیز بدی برای گفتن درباره‌ش نداشتم پس دلیلی هم نبود که ازش بد بگم. هنوز هم کریستیانو رونالدو رو از صمیم قلبم دوست دارم.
​
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/persiana_Soccer/30551" target="_blank">📅 16:27 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30550">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‼️
#تکمیلی؛ مستر المپیای امسال قهرمان تازه‌ای به خودش دید. نیک‌واکرآمریکایی قهرمان مستر المپیای 2026شد. سمسون‌داودا، درک‌لانسفورد و اندرو جکد هم رتبه‌های 2 تا 4 این مسابقات رو بدست آوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/persiana_Soccer/30550" target="_blank">📅 16:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30549">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUIjWO6nnW0odS0FHaouc5_06G8t9Jyn2ctvKkpJk-WQuCpS3i7TFWXyuQBJI16VqJWz5jJI7fcs37yLh2-OBCjj52VhMim5ZxXtdRnMZXSyk7_jYU3eZ2_Hor3KvE12CFhmbZuC9QCkIu68Qr4XejKLSBFV9wq1yc2lpq0q_oN0TJ6WceYjl7lb4P1lQfKZGNTGGrsrXe0eMF0sdHrshz-Q1K4gepBjFkS0lT5o3Il4bWEikfTxT0mKEJnmGzPlh8aBb_jCVMp9kB8Pb3j7cwk7XyRFOOmQJf3F2__hAKkcyn0KpGQZDXXWOLGkMuvju_OTV6G6bGtuE8amSAgJpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
حجت کریمی مدیرعامل تراکتور: هییچگونه مشکلی با اهدای جام به باشگاه استقلال نداریم و این موضوع رو به مدیران فدراسیون فوتبال گفته‌ایم.
‼️
رسانه‌رسمی باشگاه تراکتور: بانظر حجت کریمی مخالف هستیم و مخالف اهدای جام به استقلالیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/30549" target="_blank">📅 16:08 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30548">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8b814e56a.mp4?token=DVNB5AZdVez3AHB_aj0uMReuG9cPsdH7_5UISqG11f4WWan5Ue8tYkhr1Dz8TQcRRLzPXxyGjoRlZe3XZHuIBPF-RyvHYALVHqFwakqAfrvPblWpVTlAWe_Xpko96YSSYmUCzH7YktZBbtPQRg3BC4RXLZJWCxs0LQLJv18lrr8Wj7Iz3joE5iJAVHMXy0Pb5cmsbzuzUVIOYAjFTdVcNGL0EGy8446NVsBJpUqlnFmh1goIVQDaXZAC4CGqTDsEyM7ZKX4MhZLuvH9wLcERbol1GZvU_6pNlv77b4GdPXopia-OEPPeanIYN2hdf4b0Ed_bVKD6iUmX-_i1D3qCAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8b814e56a.mp4?token=DVNB5AZdVez3AHB_aj0uMReuG9cPsdH7_5UISqG11f4WWan5Ue8tYkhr1Dz8TQcRRLzPXxyGjoRlZe3XZHuIBPF-RyvHYALVHqFwakqAfrvPblWpVTlAWe_Xpko96YSSYmUCzH7YktZBbtPQRg3BC4RXLZJWCxs0LQLJv18lrr8Wj7Iz3joE5iJAVHMXy0Pb5cmsbzuzUVIOYAjFTdVcNGL0EGy8446NVsBJpUqlnFmh1goIVQDaXZAC4CGqTDsEyM7ZKX4MhZLuvH9wLcERbol1GZvU_6pNlv77b4GdPXopia-OEPPeanIYN2hdf4b0Ed_bVKD6iUmX-_i1D3qCAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ سازمان لیگ مجددا کارت بازی علیرضا بیرانوند رو به مدت یک ماه تا پایان مهر ماه برای تیم تراکتور تبریز صادرکرد و این دروازه‌بان میتونه که در بازی هفته هشتم با استقلال تیمش رو همراهی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/30548" target="_blank">📅 15:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30547">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnvjytxZ8GFREhe0-l9mJTAM_MNWpzCi-V647q2B50YsFv8_7v7KfG-heS-y1EVmpAnwnlBEuJYwmcOTLIdsqkKpsgkZrreZPiJ61HTz3A8-tlACZJq0DYu8ryEi67urr01XWHOve2cV63P3-sMTStBuSRVrdhCTNsJ9lBlZ0b1HGzmBiJwE6fW0j10yrRIy8joHLncEt_iYPKsGqUwF-zw264rwOyEyzJQzCMWdgYSuYkswqemiXDMzNdnqkQNaIlQh10cCJ4jiRI5gXxenWMWH5sedM_qZ1TxlA0jHhJDPT8plDN5O0u78NhFUqh0BRwn0XRfZp6G-PbpW1XsT8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد خیره کننده ژائو فلیکس ستاره پرتغالی النصر دراین‌فصل: 17 بازی، 15 گل زده، 4 پاس‌گل، 9بازی دریافت‌جایزه بهترین بازیکن زمین، نمره 9.1  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/30547" target="_blank">📅 15:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30545">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k8PxtsqpRS_dR7vuX6E_B23qVM6Y0VYUiEmV2YUhXQZFEJ8SxOPT9DYRIznpni-OEuzV-7YG_ZvS1bmlHqbST5lxTVBVUN7T76b8mcvfeC0qihOrTEuoyoDqTPo-WxUMsOlybfLyXLycXaObsYl7fxoL0xd181sjfN6POkyR8rhUC7aZbVeq3f07HOgjJt9L47iBfjp0MbEURIbK6i4Q8UbuufJTlPwVdOktCoFpEtgyhu7MXS4jxJuzd23geP55C0EhZb-IXItJzC9F7Ysj_vucyMTMds-Ms1Z54ik_rz_J6gpoFMH7u8GD9b83A9acnD1Meeyt3-alT8XfvxzvoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SRpZ-ur5LnOz18IByL_VbDmnnuRhYPad0kqbSCC2RYJH3PMF9iD3Q8Afh0Mcc1jb7Wj0VQ9cVCYS-FE38SITjrHvMP0XLJgkFxAM14UYHdJGx3GZ3jJGlSVtyXHwMjl_ggSLU4qWs0XwzOOpYOPeLp9aLJg9k23HyrL9RquUlDiYgCjc5myolbUNGsmUsDLj2VdjAufMYoiLKo8_LP_SXmidN46PQ4Ih-I1vRf4BhSMjrcPwu_E63Mo0F0P_ln36_WxJGi4IltILJaR2qx9T26IpU-ywL7ELwxiiIPu1GAjxsvANPZsuXVHyuOlL_UCURwrE2Y8LHYPeKJWG_Rpuxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
#تکمیلی؛ اسپانیاباپیروزی 3 بر 2 مقابل انگلیس در ومبلی، هشتمین برد متوالی خود را ثبت کرد و در این 8 بازی 17 گل زد و تنها 3 گل دریافت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/30545" target="_blank">📅 15:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30544">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C53bDhRV_1G0eZDsxSU43AxMYTt-zkrePN4a2Qo3L3aP-m7BQKuMGHjApy0P3GxDm3eWiZTCnTu7S37thmnCbKkrax4wZOvNrc87Y5-cmz42CcWvg8NrXt_Z_-A9dgDEroFUMj7cHqiNNXlqDtPLVGxn92oBHlgJ393JF0SXbQ20RsNIhLLcEl74VjNFOjD0XTaHnI-jBjN1QKVERYhmSI04ZNJOmD1GsaR_ZqOxz3cFHP3BNaetwIhOeinfjlof6oEf8gf5MPILsjG8s_FaXotzVgQi1ZeYJn463Epk6850WAwX7HLufyGMliQfgxkVCb998no4QnPIDx8wEzKkGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ تاجرنیا پیرو خبر اختصاصی پرشیانا: فدراسیون فوتبال صراحتا به ما قول داده اند که جام قهرمانی فصل گذشته لیگ برتر رو به استقلال بدهند و ما منتظریم که فدراسیون به وعده‌اش عمل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/persiana_Soccer/30544" target="_blank">📅 14:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30543">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKB16l8LtLenIQfSxpmQvtrzHyL59LPleTC1h_yVuXo1jdlN3wGqhasdSzBZ4DAvjRy40F3rxjI-B9cISEcAQu_KlnGRBloGlKcMEv6tA7H5HMNKDLUKJcB4LoKOxVQI_jxZTZWS2Mw0MJnvNGQXf_X26E2X8BhbkfZrPgm0WMNVT23S5_vu4K97kTGoRKmhLqsI_LsgBBqTOsVRqVds6RA5uCwEgoJFFqFepDUMGk3LvTRG4Mg5RZxx7k2IS2LaBGHtWJiqc8A9Jm8XE-dOFrrJ8PKIT5HT1bXd7GJ4JuhC0SGAfKZI-QSNUq5hEc3C-IhhbvyWFtBsnNppbagEYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تابانی‌به‌فینال‌مسابقه‌مسترالمپیا 2026 نرسید؛ بهروز تابانی درجمع ۱۰ نفربرتر مرحله مقدماتی دسته اوپن قرار نگرفت و از صعود به فینال رقابتا بازماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/30543" target="_blank">📅 13:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30542">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc0fcb29e0.mp4?token=s5qNO1h4olFrhvnLDKHBzJ6ZSo7j-DhOvZEr8JvNJ3Ng8mYKVRXVWkKRL8W-jTuOaEEoZOzLWMTctSGLQsrgAXeY-gjBvazAtnj_PXQIMGi4-3V1XxXt9ifEdf0hCnbEEfTh30Kbb9RfBfHt4S3E4uhuNmXEf1pePSdPhKoLK4XMmtBQVl4DdUfoTo_0ghVMy8LcAQ1V1TeGHKOX8xlKs1A6beSBW_pF8AmsqDSvGZz0DaLX5EhCgdTdZSFtnffs2HXxX597Vcimogl6gdRhaTjtyYFOnUepERLNvbE0Jd7ChYiXZfPupcvuCmp_YIomx_EnojiWY00FAUq0klhr5pgUR3V3VH_PSScQdUr9625GfNsbVypsuZXMyVB2WLgUfIEdZyIHWin_aTBq6wqoeuGBGGGwqhQ2gmye3pg2yleiERgBbuBvUPn5sakVHoq0JA0cB0-Oi4GtCnEr0wc6wkKTRzKGQZduQ_iDSXW_FeE96Jq8D0vS80ym9BpgxdDvdrQyzmyAGEGH7XS2sxWuK9b9nrPZJ3MnCLc5FanIlvhvM49F1HH3XrHBnFOoh_LKofjK5C0MBRJZ7ePwpEhrNuH2quafAac2zDvGLB3ye-RZb-101b7Zvc6bOLddjKG3RsvfDo-bHfICSZeKW0ZFN9Qrk1vYJT-rIWs0surS-CE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc0fcb29e0.mp4?token=s5qNO1h4olFrhvnLDKHBzJ6ZSo7j-DhOvZEr8JvNJ3Ng8mYKVRXVWkKRL8W-jTuOaEEoZOzLWMTctSGLQsrgAXeY-gjBvazAtnj_PXQIMGi4-3V1XxXt9ifEdf0hCnbEEfTh30Kbb9RfBfHt4S3E4uhuNmXEf1pePSdPhKoLK4XMmtBQVl4DdUfoTo_0ghVMy8LcAQ1V1TeGHKOX8xlKs1A6beSBW_pF8AmsqDSvGZz0DaLX5EhCgdTdZSFtnffs2HXxX597Vcimogl6gdRhaTjtyYFOnUepERLNvbE0Jd7ChYiXZfPupcvuCmp_YIomx_EnojiWY00FAUq0klhr5pgUR3V3VH_PSScQdUr9625GfNsbVypsuZXMyVB2WLgUfIEdZyIHWin_aTBq6wqoeuGBGGGwqhQ2gmye3pg2yleiERgBbuBvUPn5sakVHoq0JA0cB0-Oi4GtCnEr0wc6wkKTRzKGQZduQ_iDSXW_FeE96Jq8D0vS80ym9BpgxdDvdrQyzmyAGEGH7XS2sxWuK9b9nrPZJ3MnCLc5FanIlvhvM49F1HH3XrHBnFOoh_LKofjK5C0MBRJZ7ePwpEhrNuH2quafAac2zDvGLB3ye-RZb-101b7Zvc6bOLddjKG3RsvfDo-bHfICSZeKW0ZFN9Qrk1vYJT-rIWs0surS-CE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
ماجرای بسیار جالب و شنیدنی سرمربیگری دلافوئینته در تیم ملی اسپانیا؛ این ویدیو رو ببینید برگاتون میریزه که ایشون چطوری سرمربی اسپانیا شده و هم قهرمانی یورو رو گرفت هم جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/30542" target="_blank">📅 13:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30541">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5d8oqfWu-ixP-vhsNRSSR0jJo1xG3ZGDST7EJ7s4wLDqPTZPZe0EdaE9xkMFXhFDs3b7wk3Jdo7oq1Aft20oKo46b_65Iq_r4pa_oShMtR-D7LTfxu6mbohEYGSB1nIDwFdYi2MTqtuVCelzNq-ehi8PRKraSBfWL6I8yaUzEPNzo-7Nn2VASVV-v8O1EuvcR9SKD8VbecxsqhgO0dGx-WEJgrInOAxkffQyJqb61dX_AqktiefvzaFImDMBif2sif2O_MZOknIsso6NBABmQkgUTsAjgF3ixiWYn_gt0ZeJRBZz23FfOyDnfi5Ri3pbCUBaJ9rOo3E94cPpqrCpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ‌ملت‌های‌اروپا؛پیروزی‌ارزشمند یاران لوکا مودریچ و کامبک‌تماشایی لاروخا مقابل شاگردان توماس توخل؛ سه شیرها نتونستن انتقام بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/30541" target="_blank">📅 13:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30540">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZR0gPiP027PM5-3tmKaE54fw20t2WbIKLvIJPNXyfARfKJb8tf0peyqUipve2CW2wOn4EJeW264TuxvGvd6LeYXaOQVxb_c7hwujPbr456BbgqnQcf-A39dL1yCsIW7fRh-qXPhXRFyYCEp4T2nagH8WOSPwGSjczfNWOlLKL0hhX-r9K5aVhYckEL8Xx57rvF-hkOqwq8zFQOXmqkirk9ZFBVfF8kOoDbmrIPhc_R_68D8PwtNXj_MQ-xfBMO5njhs0uyo6vTR5bDWSLqdUDyZpFo8BEIeo0VqvltKxqx-iGB7hqavdFothG0-6jC0elykQtQ8DNzFf650-7nTBZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛علی‌رغم‌اینکه‌فدراسیون و سازمان لیگ گفته‌اند بخاطر فشردگی مسابقات لیگ، فیفادی و لیگ نخبگان آسیا احتمال برگزاری رقابت‌های جام حذفی بسیار کم هست اما باشگاه پرسپولیس اعلام کرده حتی حاضر است بدون ملی پوشان بازی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/30540" target="_blank">📅 13:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30539">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9a7ecd973.mp4?token=mALj6g1IxBJoxOG-5FOMRz1lJ4Zy2fS4ggrkYQuBQwyYaa7eVoDgVcI0lqeawFMo9wJUUQV51ElaXpdzGRd6EyUD1lLzYm8VvCWJ6UU3bbPFaXizOdiPvT52--VrNBvsgcrQD8aoKldunzOrMRVwc3tl6lDuowHzNtefXKr3GV0xshjefOPqme7bCWHXBA-q2UHbjl_v7XYaivEk1zPrpH2q7HHDZN7WRMGrjPO4KFgRmvepYinlM2NUis46oHH0SaXScwhCQ0i4f9l5OxWdE4VHaDavmRvjEfWSelLfsm1F9eSCrMB9N1GckwvI6wQZGmQotUJiNQUGor7IlvAJKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9a7ecd973.mp4?token=mALj6g1IxBJoxOG-5FOMRz1lJ4Zy2fS4ggrkYQuBQwyYaa7eVoDgVcI0lqeawFMo9wJUUQV51ElaXpdzGRd6EyUD1lLzYm8VvCWJ6UU3bbPFaXizOdiPvT52--VrNBvsgcrQD8aoKldunzOrMRVwc3tl6lDuowHzNtefXKr3GV0xshjefOPqme7bCWHXBA-q2UHbjl_v7XYaivEk1zPrpH2q7HHDZN7WRMGrjPO4KFgRmvepYinlM2NUis46oHH0SaXScwhCQ0i4f9l5OxWdE4VHaDavmRvjEfWSelLfsm1F9eSCrMB9N1GckwvI6wQZGmQotUJiNQUGor7IlvAJKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای بین دومجری زن‌ومرد تلویزیون روی آنتن زنده: دفعه آخرت باشه که اینجوری صحبت میکنی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/30539" target="_blank">📅 12:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30538">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U55gWnKBg2vrdwJkFg5WQB5w7g6iCr4hbapusRv5SXjyY-pNPtCHExgRBsFcKx8l0iwxvkKCgw24LAUTHYvcqLdGZEdKujuuptSj1_Fu-sqOK4KHYtYM7_jasMZbSmMU7kMv5KwAABfWgWh1-32xRo4PehgWnzOQzHBe3bfv1vWlcx7xXZ1O-bjG_-dKCmMwYWxWVrkdoeeC18cgqZLQDceZ_h4Uxnzp_WrALhHpmI-0sWhZX6zwm-8-bmYe-en9g7e-6c4EAIhzLP52rf1mn8pFFY2ALwNM8O6OU_5dcMFb6crMsoYfC9LRtl8MZiPUfds6j5I9jhIdDEBlR7SDlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ فکر کنم تنها کانالی بودیم که بارها گفتیم که رئیس فدراسیون فوتبال به باشگاه استقلال وعده اهدای جام قهرمانی فصل گذشته لییگ برتر رو داده. حالا هم طبق شنیده‌های رسانه پرشیانا تا اوایل هفته اینده فدراسیون رسما در بیانیه‌ای استقلال رو قهرمان فصل قبل لیگ…</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/30538" target="_blank">📅 12:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30537">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DnLyAi6L-BdynR_NuoT3_MEtjP_ToflxCT3N07fgwW3oXurb9XPlG7Mv7siabaN-ISL2ss8QSBA3yCJoK3ker0WCkz1fVdgPtQX3JpeKK2RAOepLji1lIAhjogd_DGNILfdsXABQbAaKgMmLaDJgRZxpM6Se9mmZHB5lRKy5p8N0G1waomJcMxrKWs1dTnArDY24lO3vUuwn5Ge0sWqX1EHrBIVRWV8je-7n74bUzQEkMCVtxuD87ely5guwnk4D6ln0k0Trqmw6ajZ_5RMhHzngIkXfbCHoj7DI41SKBhlmR6S5W7jxa9-TS8bSlWodkBCiMJLTXHf9e95joPDTJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حاشیه دیدار دوستانه امروز؛ کنعانی زادگان و ابوالفضل جلالی دو بازیکن اصلی پرسپولیس دچار مصدومیت‌شدند و اززمین مسابقه تعویض شد. هنوز میزان مصدومیت و دوری این دو از میادین مشخص نیست. فردا بعد از MRI مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/30537" target="_blank">📅 12:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30536">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">📹
👤
شیدا مقصودلو همسر29ساله خوزه مورایس سرمربی 60 ساله سابق سپاهان و الوحده امارات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/30536" target="_blank">📅 12:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30535">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6zhj9JnKE4kjhz0Dy4A9Z2ugvdzPm2PSdbC0hroBOoyI4PQFXGcnMqEZETaZzEYosAlcO71glcbVlIN9essXI8NV1h29bDAiCQZnRlpkcc7TFeme3cuVGlZqScT6AU6C9BK3qwWmarJo3lCXnqECdKPuN6fZljXObMFV_V5leVRQaHSjrFtqX6-XwaommHrn-DCYFR4gGvIFDDZm549BmVpNeKUj7-zvn1SwYRxLyeQFhnhD8VJl1VjBTok2yNRBbssSI0njgHnhuszk59zruxKASzEXdJSQlVn2FX4sI-zdj2ymfLl652j5OEO0ofXNZ_xpqH3X_LmZU7ZX1-SJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
درصورتیکه سهراب بختیاری زاده تاییدیه رو به‌مدیریت باشگاه استقلال بدهد؛ سید مجید حسینی مدافع میانی 29 ساله تیم ملی با عقد قرار دادی سه ساله به جمع آبی پوشان پایتخت باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/30535" target="_blank">📅 11:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30534">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Upzpo6sfOJ3EljhhmxLGJIvDe9EbH3VOIEyUu7ZR0-tDmgwIJKRpYSxry5My2BZ7ScSrnp1f-Xevs2pCSKD6ieU4_SaoawVObCXdvcYXdVWng_xIIEe7oI1ScydRW5nD-gEYtLDQIJTgANQGoUbrh-iSm01THvinAs99G8R23xRn5T4Ii7RIVNSNFJso8OfiPOreM2LIdkweOA3G4qO8YC7NlQpCzNH5nyBhbKu6hLOotL6g4Mh1u6rvUZZNEjXZS5QsLNMYvTNYZYiCLFnpXNhPjEdTjVGqMiBaMzKSF6zQMBeOXsDkAdRl0rM3xgbm4RCkqe5QbPP7t3drmFWScg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو بازیکن تیم فوتبال پلی استیشن ایران که مدال طلای بازی‌های آسیایی روکسب کردند به‌ عنوان سرباز قهرمان از رفتن به خدمت سربازی کامل معاف شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/30534" target="_blank">📅 11:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30533">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdZwbntPlEQFJr60Bzzlvx1TFtRSATl2IkWzJw0QW21p7DhZ6VJt_NteGIN2hJtANiHSOIHxtnPlS57__Hyal5AuqLDJAyyUJfSMZlSwwkl4_WQz4P0pqcs9SsJHl4oDYHnMojkYa3UukOoODIFueBYT_k9dOFySuaVv2jgBSN1bGy4pJAL8Cx_TBK0MJohfi4pg5uF0nw6A5GnNj_ypkkBr0zuewbB8fEz3etQNsJOyP4smSJD8rSfczWrOL-NuOi3RWdOOvtmfAJ-UXkjhmNoxxrMEuFh75lxF1-Hv4MRRuBofVRR1ueDnaUW3DnAS20AePdNIUOpMcIzsurZG3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقایسه عملکرد لامین یامال
🆚
هری کین دو کاندید اصلی دریافت توپ طلا در فصل 2025/26
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/30533" target="_blank">📅 10:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30532">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIDJm4iE7rmeJBx_vvOfIoNaaRfWCJo-mysxp02vkBIfi5Qw1uaFFZ0l0P7IR8J3XWDAr_V5_pvaHiqAeYf6YBorysxJRtd8NyPcyHYQvbXh4vylbYaY_aeJJqTDubx0f78AznnWG6Lw_n3c-5-11jrByLH2OOvIWsUpnUzhQV_6ThaagCYdAFcECDYzIzEwGmmGOpShanl2mqGglBAkETY-oY-gFPoWPJjqfB83EGV2cT9egZJ5esfY4x5XIsw857gcNUhx60PtNK1MCYFiJlpOfZr3KQB7xZo6VJqMKxcdFLYjiACt5vK-Doi4MXLKNjRNnYwvLB2y3wkp7fDgsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌جدیدترین‌اخبار دریافتی رسانه پرشیانا؛ اواخر هفته‌آینده احتمالا "چهار شنبه" باشگاه استقلال قرارداد یاسر آسانی رو سه ساله تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/30532" target="_blank">📅 10:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30531">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/os_TQkfStR-grFn_xguWlyWZf_4hQZVUg56lRtls9Qw3alc48iJ9O0JI_By8AdHqyOtKaCFWDxVRQ88qjPH7oqKqd7dS60uq83HKG4xv_Yam_aAsOOKCkFKn7cPR1Hey6qPjQNAAFvUqCinb0i_QngiN3E31nOz4HCel6IrrD41o-4FsqMF2G19Cp1G0NGZ099oYy0lB-LEli8l4TxXcnsPrQAQNBfDZsQdWFHJIBG4yhrwYR1MMshiyN0iKtz5a3rPwD6hOFuKfVZ3laIFaud28_65ek1aCv5DynZLl5T-NxLZIr1_BMGMa4hc7B3JCVg91mS2t3ACV0WUaOe58ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
🤩
#تکمیلی؛ تمام85هزار بلیت مسابقه خدا حافظی لیونل مسی تو چهار دقیقه به فروش رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/30531" target="_blank">📅 10:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30530">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari.apk</div>
  <div class="tg-doc-extra">46 MB</div>
</div>
<a href="https://t.me/persiana_Soccer/30530" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
جدید ترین نسخه
اپلیکیشن بدون فیلتر wepari
ثبت نام آسان
✅
📝
🖥
رابط کاربری راحت و سریع
📲
کاملترین برنامه موبایل
🇪🇸
اسپانسر رسمی لالیگا و یوونتوس
🇮🇹
🎁
بانس 100درصدی  اولین واریز
💵
Promo Code
:
sport100</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/30530" target="_blank">📅 10:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30529">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmznZY5iiRTj90u1mGZXxGY4AWOEa4xAQbBPAyc8ttL7L40wIkqfMK6n1-WOBjqrUHUsD1vGyJkd8x7AdL5VkL1xup5ezwXmBmc-U0OwLQgAXNlpYpf7KBlRQE-bJVrO16bzT5kAGSuQodkHjkG7-5WMU6C_fa8j5bB7v7nh6IVNcjzz_keywJhym6FviyI8aJl9I9COf46obEwEiWbWieMQV754ChNdQKdVzNXf8yxnmpr-YrMSp_vea-OVkDyNvUR2OzLM4ygE8_hUUtMtC6Cdvnx--JsTifrsc83FFJjnGWPAgUUsmxiS5WFltXlKskLIx6GKrCFx8lbaN2-viQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
بازی های مهم امروز را با آپشن های تخصصی
در
wepari
پیشبینی کنید
👍
💵
امکان شارژ یوووچرپرمیوم ووچر ترون تتر درگاه مستقیم بانکی و...
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
🎁
بونوس ۱۰۰ درصدی اولین واریز
🎁
هر یکشنبه تا سقف ۱۰۰ دلار بونوس هدیه دریافت کنید
📱
کاملترین برنامه موبایل
🇮🇷
پشتیبانی از زبان فارسی
‼️
لیمیت نکردن اعضا در هر شرایطی
برای ورود به سایت
فیلترشکن
خود را
خاموش
کنید!
🔑
❤️
🖥
Wepari.com
🖥
Wepari.com</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/30529" target="_blank">📅 10:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30528">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYPMGGlYOBFaaU8_ZzidyrWCft-jWRviFvj1Y-6WzvHCAvDPYeorAT-8XcD-a3Mdq0zG3wp0diZYb7A-vKRqJ_Ie07okYdYJdKpT1xC2hMlIqGwe-ipnBg-8ReF-xrMTB12Q8vchYP5UgCbKd5jq9qE_2sTATrIBf_xELTbtvpmYAqrkajTRWwXiarzRlPg7P6O-Ykpj8gbV1gsgE6TciACQXxj2CG_zQ9YdhZ5fk441rBXW9kUzRR2SkThtbfZR3738Ttf0CfkrUDFizJZeBcRfLxczGx87EkrjgXLvt6OSuDYIHvsgQzyXbFxfcV5XPUfBFn7LV0JRBj-5p_QmMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیرعامل باشگاه چادرملو اردکان:
بایک مدافع چپ خارجی که سابقه چندین فصل حضور در اینتر میلان رو در ‌کارنامه خود داره در حال مذاکره‌ایم و درصورت توافق نهایی اسم او رو منتشر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/30528" target="_blank">📅 10:29 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30527">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifkhEDkexTeFRgOagTFF890cfO37qlPcmfhJGn-WmV8qO3nBiwB39i-8wqksClMdWP7RE1EZsTP4eEEUUV811q7yM67CXhUdbhKrJKqIjjR8LRQ-mM9apgg7gPd7e3J1CDVFBYISRFOgL76UqhA0R6Qxl5fysSBgZuFQcS7be3cwYmhWJyrB4wUXdIMN5PHWQIgF5B8QlZWpOWdznE0l2f2WvqAJ0CbI2aKCn0e74SyQTuMFiyk86w4eMzQt5KT3Kg0AY1waLLyZbjUY2QZ9UtgiAmfu-D1GWwx28tGNmJqbRC_RxTrv-Xosvb8IttJwfRSOSr9NSdaNT9TqJLvEmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ اسپانیاباپیروزی 3 بر 2 مقابل انگلیس در ومبلی، هشتمین برد متوالی خود را ثبت کرد و در این 8 بازی 17 گل زد و تنها 3 گل دریافت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/30527" target="_blank">📅 10:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30525">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eo_3Qh-rxZJz0vdR9dWXaKwZCTqDuYZtWa9aUNgGdlOQ8qXeRTJIblI40_GNwyGE4bnq_2CpOwpE75xlqyn7rTBkRlKl_RW4xwKzXtdox_0gAF2HazCe5wB15TR1Ec30MLyJdDzD43Sc8WMVbLOPicaDWN16_RIv9du4itMOmIKyxWc9TCV4y3mziEjuqI2ckfvEx8jzK58S5ceXDaXzxM3oq8jQSEsNeqgScXozvs3RbkeqDPrIIppgGjEnwaMuik7ndtCTRqjDtHtFUvCPuilnpfU5Jxi3GxF2EEEckaQO5eFaiv6BgofleAfK8VlyL5BMsWOfpkKGyWzDjkF4_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
گل‌های دو دیدار امشب اسپانیا
🆚
انگلیس و کرواسی
🆚
چک درهفته‌اول لیگ ملت‌های اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/30525" target="_blank">📅 10:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30524">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAtiXx-twKRGBWc8XHi4iuLlFfbXw_dDscS1rvhyqFwRHgcbE0SFKCZHr8HUMSJM9oK3jwFoZMAJ2im11-iwaXCCDqqpYs2zY7znUKJe9XMnVJP2soLnY1SrzROkJSphLIymy3GWCIwny8C9eoKMC635oQq-a1ijn2tWZY-o8zQll9ZFjc_BAnN45VbmWtFmgvAuZclg_je9dUsJrLc0yQ9fmUrSx8a8nDqlOFzOafD_VzUmA8EP3OlsXDf8yF6Vs-ANCoMuBoLzoPzPQEOPJFDlDYEXkNvFJTKDCSn4SmfAsTMJXg3F6wSUZKIwAQ5yr6iuid5J7n27dU9MJyheGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🏆
درخواست کتبی پیمان حدادی از تاج برای برگزاری جام‌حذفی!مدیرعامل‌تیم پرسپولیس در نامه‌ ای به مهدی‌تاج رئیس فدراسیون فوتبال برضرورت به برگزاری مسابقات جام حذفی فوتبال کشور تأکید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/30524" target="_blank">📅 09:27 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30523">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/826b26c676.mp4?token=gnSVHQbnAGUfAHKnNmkOa1uXtLQ3HhxiXLUfHavM8WuumMikYbkzkU71z9e_5q2WyBFKHi-mIXtffctEVh4B79bsgS9xRlCVlxMpbw3e8bJ2RPy1T2e-HGRGBCmoOUc1KMfu0a7T2EOoM6ZzyX5QdtznjlX33laq_JrMddmFfnv4bTxlUphEMzRuW3efw3CQUvDGCBAHIAosW_MgkG4U2YNdh9xP_JlIdsNeM3n_1O0XMaSEj9rjorWCCGKRDsWn7jDTMgAXpkbNzsrfj647O7JtV34PLDKkgKsA9TN2jLo-7n9MWlI6kSC6O-a-MypK3T0AEHLMevjSq8xe58yxYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/826b26c676.mp4?token=gnSVHQbnAGUfAHKnNmkOa1uXtLQ3HhxiXLUfHavM8WuumMikYbkzkU71z9e_5q2WyBFKHi-mIXtffctEVh4B79bsgS9xRlCVlxMpbw3e8bJ2RPy1T2e-HGRGBCmoOUc1KMfu0a7T2EOoM6ZzyX5QdtznjlX33laq_JrMddmFfnv4bTxlUphEMzRuW3efw3CQUvDGCBAHIAosW_MgkG4U2YNdh9xP_JlIdsNeM3n_1O0XMaSEj9rjorWCCGKRDsWn7jDTMgAXpkbNzsrfj647O7JtV34PLDKkgKsA9TN2jLo-7n9MWlI6kSC6O-a-MypK3T0AEHLMevjSq8xe58yxYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇦🇷
آنخل دی‌ماریا: اولین چیزی که من با حقوقم خریدم 206 بود، اون‌آرزوی اونموقع من بود و بخاطر همین باتلاشی که کردم بهش رسیدم، شاید میتونستم ماشین بهتر هم بخرم ولی قبلش میخواستم اون رو تجربه کنم و بعدش برم سراغ ماشین‌های بهتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/30523" target="_blank">📅 09:14 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30522">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDD4pAtpUgNx-UVXplRwMSMe85IdzYFt7vhpEbjIg7gRpox9vLHSgmT28Vt2Y7t8od4J-Af-kt128-rCLaTyO1cucK6loC7kCHd2ffQ2JU9tYoo6C0SY4W3p0rIVlnyH6YQovS4Y02NPCbdmYFykIAEOJ8Kiix6gmZfc0MlB5HsPLndRxwBHtepI0HYjH5fxkIJ-YWIx3XqQhiqa7PoVB9pN-OpK6Byjvwrc_K2Vg2YyJECL852xs7z9YDjxTAcPW7pGDkzvxXzStne2wHvGOxFqTRELRSKpNdHahk1IRNNCwxOML4zhWI5LsTkr3OQnzI1J6-GaKmAJjc2xPOGSrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علی رضا دبیر رئیس فدراسیون کشتی: از تمام قدرتم استفاده‌میکنم تابیرانوند ازخدمت معاف شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/30522" target="_blank">📅 08:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30521">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khPVRNmTH6brIPYKPOg70xGaaMJwsUDfJaGV7yWCjMOT8bCitPlwh7plnk-2NFCaUSCIgR3w-DrrPAGJola8R01XCrgU7Q8QJMZLovYYnzna8iLL-qpPoeStpUm5tW-hiPvC7f8aiWT6kiKxoSDGh0OaYBtTvQ4xJhgw247wXpf2SbaTWYOMXsnYJXbpTkRIHSLJoOcu3f_skVuc7-z_RCxkQI9rqBXhjUW8ClDGvYX0nnHAL5Nc_M6ryVt1o8JjglhZnGmIWud999ndqqlBIT2zszXE_s-lgRyzDfmGbMsbMNcb40IQJcScN5RCpHK0Cy8nzrljZroIbwr5UAn3qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گوگل رسما ایرانی‌ها روتحریم‌کرد و از این به بعد مردم ایران دیگه نمیتونن‌حساب‌جدید جیمیل بسازن!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30521" target="_blank">📅 00:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30519">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/009c394c65.mp4?token=bWkXF8aB7DLBwDbvyp_KdPl1IuQBmReqE5uB4iI5Dfwg1bOJAh8BT2QRtqhYVfKSm0n070NPUe0kaVcImBSfjI3dIdQQLedbFqXjk9tfsBetTfNFGnY5MF1_LWslQQWaYcrCCC9kTtNpz_TVC-1y3W341_iYVOhSnohQzBvRk1T6KbguWx2rlYII0t1QKvW5d2RIehFz1F1r5OIwQbhP5Fc4lKHlRtPwIDHcUlPpLO9c3vSxg2oT_6tQYak4shnlVeX2PItHGnVzm-O8hHZWHC3ODeVcCOsr5aZyrmS_4Rs4RSta3l99-vziJA7Ry1JC1-r3dfzaTJGCBTggEnxmLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/009c394c65.mp4?token=bWkXF8aB7DLBwDbvyp_KdPl1IuQBmReqE5uB4iI5Dfwg1bOJAh8BT2QRtqhYVfKSm0n070NPUe0kaVcImBSfjI3dIdQQLedbFqXjk9tfsBetTfNFGnY5MF1_LWslQQWaYcrCCC9kTtNpz_TVC-1y3W341_iYVOhSnohQzBvRk1T6KbguWx2rlYII0t1QKvW5d2RIehFz1F1r5OIwQbhP5Fc4lKHlRtPwIDHcUlPpLO9c3vSxg2oT_6tQYak4shnlVeX2PItHGnVzm-O8hHZWHC3ODeVcCOsr5aZyrmS_4Rs4RSta3l99-vziJA7Ry1JC1-r3dfzaTJGCBTggEnxmLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌اول‌لیگ‌ملت‌های‌اروپا؛پیروزی‌ارزشمند یاران لوکا مودریچ و کامبک‌تماشایی لاروخا مقابل شاگردان توماس توخل؛ سه شیرها نتونستن انتقام بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30519" target="_blank">📅 00:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30517">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5NfZeaNRNaMgEJd5nCKQFMfFei-wgpHwUxU4lhGvrqVLL5LlGyMebzuTY5odBy72cscFaPgvj8G1YFmRORxLlVANzXk2i3MswnbtyCcwkTvs9rvXhkhxqtmi1VkooEg6SVbgB0GJ8Ch0krs3nZM6Urmtqbjp0aVsHgwwKrPPIMK9qbZSJFTwX0ZqmBJmvC2DwFUZkggAtnXqggVecfMZNBQaX0AzNQydkKSjNVQ24G4NSZsd4IVdKiemslmjxtUvYNwt5ntnGlxDccneWXQ7aqpSw3MGEam5WTNCZPvnhF8-1ksOPja6d6Ofo2iOgsHTBYEVaLTsiVirIBb9241Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ اولین رویارویی رونالدو و ارلینگ هالند با دوئل جذاب دو تیم پرتغال
🆚
نروژ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/30517" target="_blank">📅 00:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30516">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hr6XWJUtxJ2TFfmjoCQ2-14xkuD7OkIH8fB3BiXmJLCGLdZBvPJQuwFERSWDs1zEUyE-dsqF1Wtty0nOTRntsatrJLffS4o5k9SU9nBXR_NvRMYh2aMn8USvEk87cDLJdNEtIaccmijT7QRXRhU9DMGMaO2lp8LT4Xw6psLCNy82m9nj9Lqh17sIBg2AuaU7ChDBrU75T2tehhY7TcchXggl6qC8oXGEbQAGkke18cX6Ta9M0DpVBijgVa4XHNmEMX5qaULS-ewOdr3pyOBrkG9vrYJbWiziHnpI2594CaU54ngdGo-kZu6qykBmRZ5qLBiYAWjAqt8OrGBlyUVm2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌ دیروز؛
برد ارزشمند ماتادورها در خانه انگلیسی‌ها بادرخشش‌الکس بائنا و لامین یامال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/30516" target="_blank">📅 00:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30514">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVSCnzPtMfwxXPcBOtqS5g5SCLo8GS3jYvZpXn2tuChj18IBs9dXMev8CPRMnR5UD5Bv8fFvG9kQqiO7qOopXuNnwSZNK8NOBltgbKtketLe1qlZinRR6y0zN8BQ06zPI7wuQ4j8gFfsiNk6SjEmrsM2V1IMqnUmhuBPmx5R9WEzfWZKMjg4elwKTKpe69sWmxuwfxV_nNwaNjfpBj39gp8KMW2B1BXQI4gNQag23QUXDncJIaEnJ0PmxP7UM8MYHDzEEFXeCdMEX88lIZUVtmYhbgsj7NA0G7dR7jCZ09WrRc3pa7PNQnR9VArTKju1XnYKCyx2u5c1-TkLvIXkAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول لیگ‌ملت‌های‌اروپا؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
اسپانیا؛ ساعت 22:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/30514" target="_blank">📅 00:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30513">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wl1sriCXIXS2dmxciH6stRtet8POl83ApHl-xIZwHwxQR9F7bJs_aUbp-tdQGu-oHWDpUyS-PsXr9z84SG1Kj-FnoN8oqABu4YMJc9XyuFHzoOdR8b1vXJUbbCeOv0UQEq4qFnqC-xZKJWPCL7gkK_BS4vuBYfRlEClhyNj6PyMNe1WOmR20_U-kz5H6L0JT48DQhuCkeZgXdfS7q-G4Exy49B85is_TLv5td0o7VzcYqKgknHEpHhjpYiFe51HH6XAzFR0hccMv8zpiyY2ZBuSOE0Pw5sKPQkSyr70jMzO9ouxQeqJWiosqxbw91jMrhJOMksjM0-J1zIktayzIWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛جام‌‌ملت‌های‌‌آسیا آخرین‌‌تورنمنت‌ حضور قلعه‌نویی درتیم‌ملی‌خواهدبود و بلافاصله بعداز اتمام این رقابت‌هااز تیم‌ملی ایران کنارگذاشته خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/30513" target="_blank">📅 00:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30512">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SR9q3GvWf57OOz9z2G8LfTPkW0eXu5Z_rJTIN2Dc_Px_xzSWS2HC8Y3Au2D3E2nIfKUfpb4owXQCjJJbm0N8hrSIROjIJ4SWMW8SOPtw3oP-ZA2x3XsOaRycN6hfBdyhwKzS-Wey6NKZQ_cCpzxnQHEW9z9sgVDbYWx6dC_8vuXW2gXcWqV7ds5v_8uVbHGZxlRmqoTiWNMFV8c2OGKOrGdAyLJ9f__K8ju7AAuqtp62lUvyHyOq7k9IeCl0Xn1MOX0dxgn9TCh_L15-8Iz4rrvz8BGmU1z8V68P8nTdgYS3gIcyTM4bdH2GTKmhyKVfotbf_WtyW33tPgNURCYVPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ تاجرنیا پیرو خبر اختصاصی پرشیانا: فدراسیون فوتبال صراحتا به ما قول داده اند که جام قهرمانی فصل گذشته لیگ برتر رو به استقلال بدهند و ما منتظریم که فدراسیون به وعده‌اش عمل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/30512" target="_blank">📅 23:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30511">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2_nCCmU1u7welLvWvssxOCwufQANd5JwEgcDoxl3Pfq9XKfmN-9LudJDI9qYmz9ebB4Nre6yt9IfdQ9vfDolvbrVLwliOF9GAjjSJFhZ_J3XUWJZ7XNB6QEPXZY5nXHRjUjAZL8GdFwJPRpfM8bWeZNLRB5iAIdVLxi9kG2Uv2aP0ho_poqyA9fzCGuB8AgZABlbnpP65JAz7tEwRCkEOhsCAqh9GNSrRx4TqvShpNhNoVEBeBtSidsJ6AKKseU0RxX-JMLu5NDXN-0EdZUe-HX10KKFFMAitSr5R2m3HAbq1Z3ndyE8qvx_5sL1CTgm1V0Fk9VCXsGzE8uG7OrbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
#تکمیلی؛نشریه‌کوپه: بعد از آزمایشات گرفته شده روی‌زانوی‌مصدوم کیلیان امباپه مشخص‌شده که مصدومیت این‌‌ فوق ستاره حاد نیست و امباپه بعد از دو هفته استراحت به تمرینات رئال باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/30511" target="_blank">📅 23:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30510">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLMyPVImZjlIun7YN2JpiMdHsQXRykUqW5SJGJTnuAcqsU387FtwzcAZcXzmUOb7qgnsXOeFn3EDd4HfcfgoILv9sSI7wBI-i9PsZkhTvBZE3MooIcYvpAqdAlWDpCVctDgC-dHJUzawcWc61m12vDSfyM2WSGV2uLeYhBjBiohjHKolbP0Vr5QCFSPsx1u003jog4bhLwclFHIfx6VAdkTxuxHegN84C5XCj8s4V7qWGBMXgPNscN06RIiS-XHtY9Ncb-GR2rNJyrT1yg3lzwW_kPWUZc5pDEeKIkV8HD5Esp3xXsAjaEt83kaJ3fHFj2NuMT6wCgQ94D6n355xqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ ادعای بن جیکوبز: خطر این سناریوی فاجعه‌‌بار وجود داره که باشگاه بزرگ منچسترسیتی به‌طور کامل از دنیای فوتبال کنار گذاشته بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30510" target="_blank">📅 23:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30509">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igkozzQ_wKlCj0hs6rUn8j8IjgPARTsY7PXj1GaI_BwXRds2VD7TAZkmhMymyLuZKu0NWelaXQqC0YxStHEps-_tqFvUJfTFa7wcR347e1KMlbYuJULtjjZq_d8_XzPhWKwAJrs_MT3yBoFwhgINXxhZsiQecpgvJLb_SWknqS-zICLoJv7Az5eo6jlBu3SaI5xWy5w0hJYVlMiBIRUBFniVgHvbefuEsZ8T0PY4i4KHLaXZ1SkBCvF57b1oU3Dwu3BD3GU7q9YUBR4I5DInIOaW49ma1n7yrMjSnuHr9Fjp9-walJhi7FHhMdU_B1zY4rXuD2zLwecBN0eBJYow_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه تمام هشت قهرمانی لیگ برتر منچسترسیتی از فصل ۲۰۱۱/۱۲ به بعد پس گرفته بشه و به تیم‌های نایب‌قهرمان‌داده‌بشه این شکلی میشه. تو سایت‌های شرط‌بندی احتمال‌محکوم‌شدن منچسترسیتی بسیار بالاست و ممکن این تیم به چمپیونشیب سقوط کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30509" target="_blank">📅 22:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30508">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSQEroSlMuSrvOdmBXHHmJqccqzwFRPBhBj_46PQCGZP8VjSTv4KHDYGMM3ZCkegTKf4FH7sSHdwwQ8r8fkJScO9QOOVn_SyN75K07Gw6upIAZm02oTTvo5aEa5wWg7oKmslK14Cz8lXzRifQVLb5v7Z0xTs60fSNeW0UKye9jiFGIFebPlihw3w0CSGulAIzHL3P_B_tJKWLruqBcKel4BW6oKwqGwVrFoxEfJE9u7GaWB0RySQ9Edo9hVFcOMCrQL3CYaCRBLygBOssOfIR9mpvlqdM4NAzm4Q2ctwYAcBP7jH9Ttbq5rR3dbjv26FcDfEdXPhXhlnZsl5ucZvJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری #تکمیلی #اختصاصی‌پرشیانا؛ مهدی تاج رئیس فدراسیون‌ فوتبال عصر امروز به مدیرعامل هلدینگ‌خلیج‌فارس قول‌ داده که روزچهارشنبه باشگاه استقلال روقهرمان فصل گذشته لیگ‌برتر معرفی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30508" target="_blank">📅 22:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30507">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMdKsoQCEKYBld4ct-0QSaFewYUwGZc1GNmNdiEdSUVm0Ub9dFkMFKHFi4C11GL27s9bH5ef2Ldeogr24uYqt9QqeTXsPlvDAlozTHyVCB4nM_Y_br3QMOSGX645_Jm3DftdpBT5eX6vw0gee5orcrKr4IEj9TKBQwVq5YkLZfwKA85ORJtplDkfXGrAiDwe7vEHk3M7vZTw0LsE0vAYJBB_E0GyQ53aobe4DRHqt-jR1kPfcFtLNbm_F2CFAOP5Oyzubwx1Y7DMHshRFg1az_7SaZ_VoGiG5y7NDUNaZ6_tLRlRPWlgn1Rc8kljykrb3CMIe7BphNYQuyq16fwJZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا دبیر: مهدوی‌ کیا یه گل به آمریکا زد و از سربازی معاف شد. حالا به علیرضابیرانوند که ۳ دوره جام‌جهانی‌بوده و پنالتی‌رونالدو رو هم گرفته و مقابل بلژیک آبروداری کرده نمیرسه از سربازی معاف بشه؟
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30507" target="_blank">📅 21:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30505">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E-ZWPwSz_hMImVtKapUChW4TzJoqGlcFu2jfA1EbX7-EOFWqNXU3edE2xN7B1vh_ZrbTXKfu7NCSJR0r5tnDE6hDIbV2F4FCgTID97Hgq-mqrDwC7wcBul8ZjTszSSPXrri1hDM6BGINE0gadfeeiH8RMMB3Wo0XpRms-5UR7CEPMrA4hUJBzUbES0iVT_WYd2c3AKGsemxN95UM0D8jlAz_Nt5zB5Q5QDZo7Rt3RfAJ9MiZ3jiFxDruROaK-npmKLU9QwHJcO7XK-magUKCKDV-ScP0eeWTZkyZrN8dVE7Jy09ZnN_aapIkrguymhSXAY_iFryXqJrlDfaQDlfB-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IFHr03HlYp9NqTezkeUf-k_K0yhQvYBLNxGqe0Jvew70OGkfbrKW4t64GsqUuluzu7WDQVW2fB7rURTVspSjb-mail0KbtIzU2eI-_8VgESbM8aniStFq_GZuflhoulRE8-1-nYrklx8jqQNlXccNAUinn7KuIbAeri8RDVJ5Z_8rm9DFsMezRzGyl04iPFLSBhiTxD9KDJTfMRrCeLQX8Wz0zKC290e2HRR5_4rdC3d16-V2HY3BK3A483Op0KDr2xZw5Fczijq5dBN0Sxv12bXOIChQYY0L4_RD9DZA0BXoD1qJrqNkKA19m8qJGKfxZkgBBw816Rh2CVcs38WzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌اول لیگ‌ملت‌های‌اروپا؛
شماتیک ترکیب دو تیم ملی انگلیس
🆚
اسپانیا؛ ساعت 22:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30505" target="_blank">📅 21:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30504">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vruW-sC8zfnD2KQn5yMl0M69jOzMMdzQR7Uys7wXlI3998dAgg-qMgKQIuBM4nFUxRBtUa5pWkN56myAn1p4wwpQopImjjS_Va2Tqxx9dwYG2yg73lPAWf2kiL9gtADm04zaKba4O_kjaIzl3wmtv265wJcHqJrbQ1hNe7HXYB3ZLCiyx2TryvBu3Jl9nPiekDi5_A6Ho_bmNFUEHzp0IwG8E-DAyVIlkcQ4J7nN0fVERVv2Fn1-X-UdmfUCm1dQBFB-i6oTjfdo3wVPk9G9bbtFIb7s2diPXn9bQyYS-5yyKKI50WlNBJ4IYrWZuc23nvdgJ09ogoSgC9x9z8lhSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا #فوری؛درجلسه دیروز هئیت رئیسه فدراسیون فوتبال سه نفر موافق اهدای جام قهرمانی به استقلال بودند و دو نفر نیز مخالف. مهدی تاج تا پایان هفته تصمیم نهایی خود را در این باره خواهد گرفت. احتمال‌قهرمان اعلام‌کردن باشگاه استقلال توسط فدراسیون فوتبال…</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30504" target="_blank">📅 21:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30503">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJ5Qj7FHakh548Qy41Qy7Gy2xzz8VpY6zHFcdunYj_Sw3DZ0ogn5_-VWHsRRrodI2g2AlQyVCtyAJlL5gHPaeT2nTU164F3oe-yP6XSXyOVvFnAEgXRDFqvTy1ZV7L_jIwpd5RD6KslFLeakKUmkH9ZnPX02o9a42Hf_ijERubxMELfEzLMBSf7sRdyxu5JeSQM40OndEc_TvWQuRDzcV1rOUP2cU40sf7m4YtDhHL6Ddrsy1si_v72ERMJkKM4JLPlTSWNvg-ixxi3JiQRzqhV4MEtW-9eRDmQ5DZn_maASyPdeqrjJTKWqLMvXakxuD_uYyteeu1YUs2ZDXWhU3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ علیرضا بیرانوند گلر33ساله تراکتور به دوستان نزدیک خود در تیم تراکتور گفته دیگر برنامه ای برای‌تمدیدقراردادم با تراکتور ندارم و بعد از اتمام خدمت سربازی ام به باشگاه استقلال خواهم رفت. با توجه به این‌که محمد خلیفه نیم فصل به استقلال باز خواهد گشت…</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/30503" target="_blank">📅 21:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30502">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ee53107b.mp4?token=NxD0zeNjBv8RwDtzDj76D4iGjtl_Sjw6nd6JtV16giXJJRhQcuuAF9fI5JD-0Gq5lpRYYCS0L9qhyeEqfExFKchW1qeTYY9AF2MbKkb-cXHXREY89qL1y3N6jVKyYcxG2HBIdMS5WI7GzwBf0xFeLv_cK7-EDH6WSMq5D5-1dhpQJ5seu1XJEVWOpIJeFuosGl0Dy5J4MQ6LCnDfpVEDVG0TCSXDLrQMDYSgNKt6t6AZgkzsEylMa3tdUVmv-j8uf78iJ5aEmu7YVB7y7ps1AeJXKAbU2p7Af8OGi7HEwET1UPdsb_arDrzpYeG8YxztnZtbVUB-eS1iBH-DOMXOKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ee53107b.mp4?token=NxD0zeNjBv8RwDtzDj76D4iGjtl_Sjw6nd6JtV16giXJJRhQcuuAF9fI5JD-0Gq5lpRYYCS0L9qhyeEqfExFKchW1qeTYY9AF2MbKkb-cXHXREY89qL1y3N6jVKyYcxG2HBIdMS5WI7GzwBf0xFeLv_cK7-EDH6WSMq5D5-1dhpQJ5seu1XJEVWOpIJeFuosGl0Dy5J4MQ6LCnDfpVEDVG0TCSXDLrQMDYSgNKt6t6AZgkzsEylMa3tdUVmv-j8uf78iJ5aEmu7YVB7y7ps1AeJXKAbU2p7Af8OGi7HEwET1UPdsb_arDrzpYeG8YxztnZtbVUB-eS1iBH-DOMXOKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جالبه بدونید که نستوری ایرانکوندا و خانوادش وقتی سه ماهه‌بود از جنگ‌داخلی در در تانزانیا فرار کردند و به استرالیا پناهنده شدند. برای آدلاید بازی می‌کرد و در 18 سالگی به تیم اسپورتینگ پیوست. تو20 سالگی به تیم ملی استرالیا دعوت شد و مقابل تیم ملی برزیل یک گل فوق العاده به ثمر رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/30502" target="_blank">📅 21:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30500">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMXc0mO32oob9yxiup2LEwwn8Qd5R-IY7K5Xyw3c-BiFPdMT5h34k62CoBBTEvGR1wDVrMO6k6vhEEYb8-x3O-dRWXnS5G1GjqfVKS6lN9aNT4hTns6lUu67QdX8R8sjCQ3T6q1BXxO9MJ-TTINMnSafS9YQR9-u7Xwd6zjOwOFonKxEHK7cnbW26KjlLx138bwlVM8zaliDzkUtQDXRj5N072CszmkWXkX9T2ED5QLejcdl6iOoBe-BzakDXFzHBhmvEzFzwoa7WEtnIqWxYQx-BeoleabKs4Dkxk8zcrSqEe9IiJdvfQPtMQ8QCc-VpHT511X3gelsbjeXrjH_SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇫🇷
#تکمیلی؛ بااعلام‌فدراسیون فوتبال فرانسه؛ مصدومیت کیلیان امباپه از ناحیه زانو هست و بدلیل جدی بودن مصدومیت امباپه، او بزودی به مادرید باز خواهد گشت تا روند درمانش آغاز شود. گفته میشود امباپه حدود 3 ماه دور از میادین فوتبال خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30500" target="_blank">📅 21:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30499">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ac5gD63m8aHXxxAJgmXhNWWB6zNBWqCGBLZomocUSv80gOk5xn9gfaqzPSeMLOKiJ7WeyZGrDGK65xKmbY20ZuJHB57ei0FZOhexTnyGPxOonTZ248rkEd5pYak7Oi1N3GeopWT6iigTdd4QzXGN4TzHrDdNPyyrEy_EcsPIrh2OYZbniRkgdynIyBfwHue-lOjr3ujt6V5lqPEvMviVUjOqanfjnJ6gdQktbPt8D9cr4J8CrhEevOYQBw2BLfvDpVkxMCuL6uOapAZ8MQ1w_hbCIp6QIgu1Ra4_6BPW1gT-ky4lLagLnOFn5ulPoPokFxpwbyeN-b4lOyPTsBpAow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صحبت‌های تند و جنجالی اللهیارصیادمنش فوق ستاره ایرانی لخ پوزنان: میدونستم قلعه نویی هیچ اعتقادی به سبک بازی من نداره. تا روزی او سرمربی تیم ملیه هیچوقت برای این تیم بازی نمیکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30499" target="_blank">📅 20:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30498">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srDMFlAjqKU8hTwh6RKMtr3wP526PeIMJDwnymhUmtmbMntqsqAsKDVhG0AMtXh5lttnPTGa43mDVFBWf6ElwRf6IznfmrBz6HHsl5RUkT8L6NLOA_097sQt8iqgK8328EOpMl71S2nzIQ7iokj5XJWXon9ax7XYUvU32NBOqe_XDg2POlPRKssIGLrFd-unia1oo2deRJ3vCPgJ4TskOUpt3kERV9ItxOyRnvZi6Dx4ovH3zRFREiIYIbe2AAsn3csU9nflnuXTusdVK0FeGA-LZSwC_loZp_g6zQB1ygoOr1cZ3bGWgf2xp7aKO5SGjuY7JZWvIXYsbdkPxYTngA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
81 سال‌پیش درچنین‌روزی؛ باشگاه استقلال تهران تاسیس شد. آبی‌ها باداشتن دوقهرمانی درآسیا پر افتخارترین باشگاه ایرانی در قاره کهن است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30498" target="_blank">📅 20:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30497">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1d9a03df6.mp4?token=crmurWFevo65Hn3JmTiwQ2uz5VljG92u-NcAOUTquf1sB_pLr98kNKrQEQ61yx4sNNvDuy-JzARWWvnk_t95Vr0zy3t_9dEr0klTXSJ2PWFfX3RqCQHo0fIHJGPqLBw1zpPpY4c63WU9kHfGq_Y0r1E--Kuw18MLAXnHM8gQNFEDz5axAQhF_9EoWa4v4LjCgSN6zS1tDWPHIN6Rww8gxE7d2xEUIhrMDdLBAbXc4oujmO-g2ir86o1nrXg5LIxntkzlkC01CMNhEZKB1OPDW4SplIjMr71Feb-N-cV5_OZh3s33g0fHQnIAypkKSo85WHZHJBvFMrMpNuRnPPqYUg6gKO-DjMljK0x3OE8K1TkoOBsYnsAJYEoMJLadA8Fu2df05XrwkxVu0BGV94NOmvHAdsmsBshP7Eek0pkXvDkBdsQXxOhMSc3dXsUAL06srjgBnLcqKyuiLDMsNwHEY752pPCKoeZYzznQfXFDw2o1gfVVd3WHIAQ2_sBW7RzDJh9sC15FftuRP39SVLrsZxUO7Ujv3mfPAzPd2dmR11lPsYBGKesI-bk97QZs28ZBl30bFVmEJyPjhgQ1ZTvDNuk6J3Jc6rTd1cafgc2Pwm9GJDuABIQPsTRNUYKGanl9dXVLW6QV6bn5ZkEqYgZPV6yVGrwLLt1cQpzSSYzkURk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1d9a03df6.mp4?token=crmurWFevo65Hn3JmTiwQ2uz5VljG92u-NcAOUTquf1sB_pLr98kNKrQEQ61yx4sNNvDuy-JzARWWvnk_t95Vr0zy3t_9dEr0klTXSJ2PWFfX3RqCQHo0fIHJGPqLBw1zpPpY4c63WU9kHfGq_Y0r1E--Kuw18MLAXnHM8gQNFEDz5axAQhF_9EoWa4v4LjCgSN6zS1tDWPHIN6Rww8gxE7d2xEUIhrMDdLBAbXc4oujmO-g2ir86o1nrXg5LIxntkzlkC01CMNhEZKB1OPDW4SplIjMr71Feb-N-cV5_OZh3s33g0fHQnIAypkKSo85WHZHJBvFMrMpNuRnPPqYUg6gKO-DjMljK0x3OE8K1TkoOBsYnsAJYEoMJLadA8Fu2df05XrwkxVu0BGV94NOmvHAdsmsBshP7Eek0pkXvDkBdsQXxOhMSc3dXsUAL06srjgBnLcqKyuiLDMsNwHEY752pPCKoeZYzznQfXFDw2o1gfVVd3WHIAQ2_sBW7RzDJh9sC15FftuRP39SVLrsZxUO7Ujv3mfPAzPd2dmR11lPsYBGKesI-bk97QZs28ZBl30bFVmEJyPjhgQ1ZTvDNuk6J3Jc6rTd1cafgc2Pwm9GJDuABIQPsTRNUYKGanl9dXVLW6QV6bn5ZkEqYgZPV6yVGrwLLt1cQpzSSYzkURk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
👤
ویدیویی‌فوق‌العاده از آنالیز مسابقه شاگردان امیر قلعه نویی در بازی هفته اخیر مقابل ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/30497" target="_blank">📅 19:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30496">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/777a222aa8.mp4?token=mbasBEvLzd3wHuhyz0jvJSJ3JrkSxQKzxe8JU8NCE929UCuLPGdw1LHS09TdU9Gn6sNzL7MWFpbCDg4C_KsnzaGX19ed0Qa9FKMwRLN4txyA51oI4s6aTbIs7ZKXPfkhBDeanZn8jkQbiQRek77Wnf9Fpy9Osw8pQ31DuhHf1_QXNUVWhe6UQoFYtqih0oRcLhBenZR0QhZ3-C8s_gBp2dhJh1HaRyERwdeJV4esfSDq37QzcQXZS3iCYiGBzLClp79IVmmwIK4hLWtk7E35cu8GpnBsjL_6NdDBwwxzy6Ca3y7zb90uXaM2ntAknzBe9g39jrkDuVLUcyG3pJkOrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/777a222aa8.mp4?token=mbasBEvLzd3wHuhyz0jvJSJ3JrkSxQKzxe8JU8NCE929UCuLPGdw1LHS09TdU9Gn6sNzL7MWFpbCDg4C_KsnzaGX19ed0Qa9FKMwRLN4txyA51oI4s6aTbIs7ZKXPfkhBDeanZn8jkQbiQRek77Wnf9Fpy9Osw8pQ31DuhHf1_QXNUVWhe6UQoFYtqih0oRcLhBenZR0QhZ3-C8s_gBp2dhJh1HaRyERwdeJV4esfSDq37QzcQXZS3iCYiGBzLClp79IVmmwIK4hLWtk7E35cu8GpnBsjL_6NdDBwwxzy6Ca3y7zb90uXaM2ntAknzBe9g39jrkDuVLUcyG3pJkOrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇧🇪
#تقویم
؛ هشت‌سال پیش درچنین روزی؛
ادن هازارد فوق‌ ستاره‌ بلژیکی چلسی این سوپرگل دیدنی رو در ورزشگاه آنفیلد وارد دروازه لیورپول کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30496" target="_blank">📅 19:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30495">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsMtbpaqwLNtTVl6jHgKTADUJYZZk6xYpOJ-Nqy4_jbwnA-pn-T5QsB9n1EUaFkKTjd6nCpGi2qJiP4zIK6zZ1n3dTAGFERO3E_9Ub3jEC0sWNIbR6E8cmoYCvmUATgN8j3gmEWJ1l5FEYTlSz8_ACvy0d5pugPr4rA6Mlo568nBX84Ir_d5mcFT2UnT_s3pltyljW1nM6HVZTiC0tNVaPq0FLPd6_LeyylgX3JwURe1jrGzwfe_UpPp0MNLwnLxWK9Rgz7B-rBFcAmqZ4i6_5soGPHVUUacfOZsTZgXeukYB_dxxtZQXYq468WUVRGFhQu3mqyZPZdySgsJmZzLpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی فوق‌ستاره تاریخ فوتبال روز 14 مهر آخرین بازی خود را برای تیم‌ملی آرژانتین انجام خواهد داد و در پایان اون مسابقه از دنیای بازی‌های ملی برای همیشه خدافظی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30495" target="_blank">📅 19:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30494">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇪🇸
🇦🇷
تعدادی از کاشته های استثنایی لیونل مسی فوق ستاره آرژانتینی در دوران حضورش در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/30494" target="_blank">📅 18:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30493">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwmG9Yt1tRp5bxbbhPjfmT6rXusbwE6RWqpmsDgjY5h42kxSvMrXYJXsSD0T5ew8dEKslB41uhI4wHOsx8k0RPuQJLAyGAHH04zDp7hTn1ngtXR_F-mHeu4Ydkjkav1m3M5MZ6eqB29DsjhJvuJJD_L72KuIjTBKIhnyrJ83Hck46GCB_CvkY2FoL8ht_Y8VYJ1mfbzDGFbUCvgQjLBwIAtNLTKH9Gdbd47-zxe44eQtmOH53TWkT-x6CsGFf0tMTEtbH1bOZ9PBloDTW6oSr1o8cyq7Wu7FIKibMsySMCmQZG3Kg1Vs1SveOIoSyyn1ohFmsXRoBE7np7wrS8-ISA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇴
رسانه‌تلگراف: قرارداد هالند با منچسترسیتی بندفسخ نداره حتی اگه این تیم بره دسته پایین تر باز هم بند فسخ ندارد مگر اینکه سران منچستر سیتی با فروش این بازیکن موافقت کنند. بین رئال و بارسا هر کدوم 200 میلیون‌یورو به سیتی پرداخت‌کنه تمومه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30493" target="_blank">📅 18:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30491">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d6KQoDgP-2GpzYN43ZjTw3Dcn18g0xWZQlKeV1iSDaIkcgo0PKE07MQSPQ3cGRpH-hfbL6XIOGn_yL-AWUbCWoul8fLueZx5vTwqkzlH1OeXRrnmWPl2KaKTjwONKnJGeCzucXO1SbWbdioiFtCfBW7HNQcy_4Dc9JgxJ7UlohST8h_5FCh8lB-mto6gJ8RFAba9x5AYM06Z-rk8riLq3g56qQRwRL5OT6K9WW-Oqhch6wUvwo9B6zQzbxWUG2tiAHmg0JtgXA60_plybH-0CbShGv2NC8d128LL5aTtCSpkSiWa0hXc9qurxDRQU3YDzc0CQRjpp6uom19J-g2w6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LN0mztnn54mq_EFbb9JePTnc6MBVF4hxwmK4ofwxALseS1zjCDfhvsNirUlbpDQthjyReOEpADbyofsyWPDjmVasHHa_fDpC8bDdpVh6TtwZOqDT3ISfigYJqJHs4HoVfrjxGl2s15VwOnnA-xHqH9fMMxTTP9m7eveq55Q3tVdY5P4QZ7UbTRxEhfeaaLSwCQ17EdDpkVp_sZvGaEMhMSnKLZejxA08pvTwj-M12lhvgJokz7jwHkTtwynlI8_qAgSXiaU_TfDauoc648SAicN_slwogSS4U9AnoHpu7oGMKyVJVhsyH6Y0f6xVyFVJfxfzoq3nTrzoWDEVUlV7IQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
رونمایی باشگاه استقلال از آیتک سلامت ستاره جدید خودبرای‌تیم‌والیبال این باشگاه درفصل جدید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/30491" target="_blank">📅 17:56 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30490">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E28XIHSJtSlWpQWu2xl1XsXLGWzJWRw8TEEPUrkSDbv-wDwN412FPxr4AcmLTPkPVITYpRbBgYRxqNjIXHFC57f_p4vVGHagX2gW3jfWZeCLckmaHwBishSkGdUY3heY-qy0c8_AgixlcRu0iQSiXgkBIdPPTiGL9DQJVgtjS_D2lekaWfRdJ7iJ9Pe8pulUK2u7jBiMMTnsGpaxBKOadDnIRqx041fqM9GaKQESEUHuw1rvxUQZTifMPpjewj1Y4tWNP7U9Qhq32ZAAJjpxw2l111mCRqZJ4Me4Qz71NrP_fqaJbjUFMBSVM2CkLFi4DZBJ-eLE78gR65ZEPbvSTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقایسه عملکرد لامین یامال
🆚
هری کین دو کاندید اصلی دریافت توپ طلا در فصل 2025/26
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30490" target="_blank">📅 17:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30488">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5roCUt0B3pT8dyjilvwoaO-PWklojVQkHjXUYadwUIFiXYuGpQYOyBU7b98dLpmQvnSvT9lXMXk6xxNHrtzQ1ZWIJSABSuDGFitEvQLg8Mz8UJHmGEDUlhfEEJyC954vwp6BDZpEYQ1CSG_dnoRJ-T9veFfcRR0QhUPrE7CJJe9TjqkAQZEXPSbcx1ZAkyJheZBs3J_HGjGg86YE5Xp5cxiz7O9TxhTdN8ssogKSB120KtGO-wUrZG3eq4yEKHhRPxxRA_j1EE5pziaKC-f_EcvFU_M3yj2mv1FqVCSmA5MTjeLKFfdc379O6k0k9oc1m5_zWwES564k0sq1oEGyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصاحبه جدید دونالد ترامپ: پیشنهاد ۷ شرطی جدید ایران را رد کردم. مقادیر زیادی نفت هر روز از تنگه هرمز عبور می‌کند و شب قبل ۲۹ کشتی از تنگه عبورکردند. ایران می‌خواهد تنگه فورا باز شود چون خسارات زیادی از بزرگترین محاصره متحمل شده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/30488" target="_blank">📅 17:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30487">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKoJxWfc8qEO6oPW7PhB9vSySJpFELQtWcOS0iqZm0ORmQpw3X3dtParC1uki--V_I1b2inn-W5n8ZC54Zk96BZ-COvMes5swJ4sV8mB_fZVlZ5kOLcZLQWlyGYwYcyMlTGIobYHnDkoXBoWNS7PnZlPSVb7l8pHGyXcRlJaEnAJ5gFeuiA9rnXoHqNFS9JnDBrOw5jrXjmZXJPvPl2ocV05m-JnKfc2vx6emN8rTu-3yI3kDdxStED1Yy-SGoBzeiybsl9BYVDEuqJu6LMo-O9-jX3zRqbrXU48v447IwFhrfyI-Qlw5gKbOlabq73XzzS9Os_d_SPxi69fFhkkyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
یامال که قهرمانی‌یورو و جام‌جهانی داره: من دوست ندارم برای بهترین بازیکن تاریخ با پله و مسی رقابتی کنم، همین که سال ها بعد بگن یامال بازیکن فوق العاده ای بوده برایم کافیه! ۸ قهرمانی لالیگا، ۳ قهرمانی‌پیاپی درچمپیونزلیگ و ۶ توپ‌طلا برای پایان دادن به فوتبالم…</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/30487" target="_blank">📅 17:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30486">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6HdwBPrHOdBmV2hoSTEw-4B2Za-6DWg3X-uhVIxqAr_dKBqAE7GDQB2v5WZIZ6pITzFYUNWiqn90ituf5Hg3Ov4G5kgqL6cJ1sJRxQevL8mdd_CnYkCxelNs2ydnyMLFNW7SWN4_LHw05ZfPkCqA90hoGf5o-InFZzm3LfcNiQYyEn735KlJG8MM1JYtdrjSoS-dxLOjRxV6CSk9sg1DoSUbO2RSAna_y5xnXik5EA91TnFs75CXhp_UixopuHE4IV6sWDhclimnZqAlNNmyDJyO_yfPOmewdpOmfnIs4r1-eb9f6tJxm7aTKVL_gUX-UOKmf27sxEir_lLrPtk9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برسی کامل‌ودقیق سیزده سال ناکامی امیر قلعه‌نویی سرمربی تیم ملی در رقابت های ملی وباشگاهی؛ وقت بازنشستگی فرا رسیده ژنرال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/30486" target="_blank">📅 17:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30485">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rp4w-Kq4wOjl8R3Hba-_GMSoiHqFPaBelt5Vk-soEpSfZMDhbINaFMJIFK6yQJI3PCME8uY9J_to_4_l4sAsYRcRwaDDNI4C-l2rFe85W2zECJylVZN6Yc7H_glDmQA8TxKyf4jjZZxWrLM4b4SSbFZMdNtr7AGpVja8jcTrlnH6ThMV0_9kQNwAjgseAO9qbebQXplf4wEmuuSMA5WQn73-psOwcbQfMOgbpLA3Y5sbJyzAzITh0i1uOWBPrWU6eXgAbQV4Gau3ayDngu-VDdbq3hpliFdMmRjNmftylGcH3RIhMAdfLamLSFFLykvjr6lK-8Rmy61ZjJ7gzlNWpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبرنگار باشگاه‌فنرباغچهه که امیدواره هرچی زود تر انتقال کریس رونالدو به فنرباغچه نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/30485" target="_blank">📅 16:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30484">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqWA0j3AvNvf4qEPM5F-8QHrzky3sFrbn-TXMf-2L84znW72IdwKisKUSfduTevj7fMIR_-7wW7vjrh2nycGnktkv-skpRxxwrTvYMfL4-w27_QNcFILpmmGNdELdjzxPJmvt-3ap0fR8kpc4Qhon7ruOQvOniZLMR9aqp9teggVaoxXANaJqQ-0-D5qaV7X6zVEf77IRlQtRbi3s3rfVJURiiORHFT-FcE7Tx6txlaBd3rl31poUi393Ln0iWQ5gORCkbzZDOqoea__P9AWDN4ui9Lw5yEXFQ6UBRzXpUqRfoUw7eJPrO_1AKuTC8vMCuJVQw8L9O5bVKz1VCsYjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام حجت کریمی مدیرعامل باشگاه تراکتور؛ معافیت تحصیلی علیرضا بیرانوند یک ماه تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/30484" target="_blank">📅 16:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30483">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfnDTDdMMS14YsYMyxv2RCZrOIyqvWKj6f803aFjaIbEJ9kFtAbq3PvoBSTn6-MAt6ZQm51pTGPGUOy9fei98tmuYj8EognwDwqQWz28y98ZaVK5ZK9lpTqRGgOfliJ0h7zW-vM0E2TbJ00R1Jx0VIPmt5fR0iyucfgjRGkYTeXIyHUN6yznoz7M5uBuFOiAoUZe4zVyqgpKc0RXawzgtG4WNM9x5l13WYvTpKKpGLd8pZkp86Pq554M23FVkty31pUnnlHJEwF7hdVdW7AajMjjuVKIBU3JdZiNtJA6OBSQmzmqY15dclSYQ1tVax97sYqg82krWiruLRuMdMEQgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
👤
مصاحبه دو سال پیش علیرضا جهانبخش کاپیتان تیم‌ملی: بانهایت‌احترام بازیکنان ازبکستانی هیچوقت نمیتوانند خودشان را با مامقایسه کنند آن ها نه در لیگ معتبر اروپایی بازی می‌کنند نه عملکرد خاصی داشتند، آن ها توانایی شکست ما را ندارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/30483" target="_blank">📅 16:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30482">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/enBO3GoC4-K9hHCBHbAMKPcousZ0M3-woEFJ01P3f3EkkINV63h9crK7g_4nDrL_Ml_PqDIBPQkC2H2_kuabg5O5FbnxEQLNME8-92Q0xLRa3slzCM3biACjQhhB4js-3Qe7wVURK_UIKTIphquVCPzFgiN5iR9VuCmYPpFgrOaHuL-MVaejwAJFRqvfFwvLGCSk2xg54SFz2HGzU1IH-KWV2ebjHc2d-WNHTtRhQdIJgoAcvoQFsbV1r71WBLzvAc1Ajhl_pRSzhdejFPPZuF_i4ZSZcVU0o9SN2wujWyU2Iu00So0PRfQ_jh0WMOFMgNuPxFS5DDy3m1qLuJ06Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کارشناسان AFC؛ سعید سحر خیزان رو بهترین بازیکن دیدار امشب استقلال
🆚
السد انتخاب کردند. سایت فوتموب‌هم بانمره 8.9 لقب بهترین بازیکن این مسابقه رو به یاسر آسانی ستاره البانیایی آبی‌ها داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/30482" target="_blank">📅 15:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30481">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcDwHVbtN5y6DhRxl0lugpK8tr4UaqFZl562JAVlmFXxFrIR-gehCtApAHnfFc4SmSibtd7HxjumrQ372Yr2_pZa9rzsYdqm07Szb2mLzGWGYlon3APA11vqTgcr1BChafz6Hg4Tx9bkJ_hzUK8BeRSE-2vCwmyyg60fpAL0FTgpCdQerIHa75saVqhsmBAE5ifDLpyWXw0Tgli6YJUwtlRal6r6_qVkh8l-dwgeXble0y7oBVkDwj3hPNZilWQrH5gfASzYXipOnXhFycWPjgzvPZKeiILu758bR6o7UFG3HEV95oQL0uC_Tc68qftL9Vy032e9GGLHCvQ4Ecbs9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه تمام هشت قهرمانی لیگ برتر منچسترسیتی از فصل ۲۰۱۱/۱۲ به بعد پس گرفته بشه و به تیم‌های نایب‌قهرمان‌داده‌بشه این شکلی میشه. تو سایت‌های شرط‌بندی احتمال‌محکوم‌شدن منچسترسیتی بسیار بالاست و ممکن این تیم به چمپیونشیب سقوط کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/30481" target="_blank">📅 15:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30480">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✅
تابانی‌به‌فینال‌مسابقه‌مسترالمپیا 2026 نرسید؛
بهروز تابانی درجمع ۱۰ نفربرتر مرحله مقدماتی دسته اوپن قرار نگرفت و از صعود به فینال رقابتا بازماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/30480" target="_blank">📅 15:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30479">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFpnkdJ0zekTidHiNeqoN2yCySY75N1e6C1Lp19Dy9DSVF1lLXbKIQWMzRXFtSzai9pb6ieV0vSfTX_I3qLZH9WsRjkUkXRjYe8Fk_UB-7h0wjN-haZCS0icWdzOa-0Kubk84HP1R1XOBxpq1_M1BMrumr2JGxG7wTAH4nh8-LRltm3vIfrtdLUAhzmp5SIsuEgAF1GqTgLHX-I0uaHoPDdn_7bg2JJZdfEDQasExEx2RmZGGCZkoVfvTPe2kDxwGeL593zMYHtzqP6ZZfJvUthdNEIu2Zpu112--IUjAsY-4T7Plp7XQO-nISkGJQatHtmjSn0y_tMPg5LRccgcPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
مقایسه‌تعداد جام‌های تیم‌ملی پرتغال قبل کریس رونالدو و بعد از اومدن کریس رونالدو به تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/30479" target="_blank">📅 14:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30478">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPMdaAST57PgiUd-dsGM1Wtbq6HheCOPA2ntEwkZhu7Fo-j9HGp7HBxoZrBsOQhEc4oUQ5W_EN0chucYEMy3H0jGRae0PvqkglC3oC4VTzD__TRxSssXr9VPw2gRQnfrz4nLtdPsIDB_xWK-9TyhhO4UabiId3ysxD4uIVVnc_Rc9VaArXe7S4eQw50h8KQyCGUkjME59uk2u6gD0KTzcqUn7mirUFPGw6tTsqSw64Sp8OV-zc5kHRhLRKSX1T0Ndr4Ma7fHR7PBs69SPpId6CbzilVPc5Q2LIKsYwy75cDPGqjOzhGYyTT9QWhIVF4Mam2ibj6uH878LJGS30V2LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مدیریت پرسپولیس طی روز های آینده و تا پیش از نیم‌فصل‌قرارداد اوستون اورونوف ستاره 26 ساله‌ازبکستانی خود راتاسال 2030 تمدید خواهد کرد. توافقات بین طرفین انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30478" target="_blank">📅 14:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30477">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJMilpup2qpRubrAVSRse_GMsCXp_rYvrknjc2A_k0EYvvqo0Enb4degSzqEtg-WamY5q-HsZIXvhqvWV-oRoq6RSQP8-34-_4liXeOqTzNUmZXg0UjlUGO9lO8l7RfAfIQVwlHE749rkTztvIwOgmAwIdlnQ0nG7I--lpBp5ZgIbb0U4F-FXyXTtMJcYNtEhR77MSqbEC_0VB14wXwvQCfOgnUfwdyovgKQKOqtg02UMPtzyZmBSLY15_wL_ONhRpNzRjSPuNNDl9VOSgzmZsT1FiQiPg0Stzdjc4f_Nf-aiWFXXSofwrcIBFrV2QerXpZKmMl7x2IDxfdbQi6wUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سلیمانی وکیل علیرضا بیرانوند امروز صبح بعد از کلی رایزنی باعث شد که سربازی‌ این گلر تا اوایل آذرماه به تعویق‌بیفته. او به بیرو قول داده که تا آذر ماهی راهی برای معافیت کامل او پیدا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/30477" target="_blank">📅 14:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30476">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0ZojyGelI1bdS08keripYe5cSGx4bjeIQk3ppw9ZDkS0qxuhfq5pKTRjY-e7DBcdyU2VQN_XOEKdCgYLq1LzVO_pOv4_9JdUTTMbBe5QxOhZAfYO_ixU4JnmjFFe5uDsrqtPC6Cb3zZlPa87pfuyqEcTIp_5ip7jwFj1z0sWYXG0eM7TupQ8LT38SEBSfWQLcVR2oMLuEi0PXyZYigJy5_2PC1ky4SlhURvOi56ezaLKoAfcgJn8HJSHJfs4Y8ajvS4unnPtCff7C7j97QDtuWONIQ-TXNSrCp58kpH_UWhxdi2hYzNsKIQTARuaqVQayh7ilFlEacxPvxbZknPUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کول‌پالمرستاره24ساله‌چلسی:
خیلی دوست دارم که یه روزی درآینده نزدیک شاگرد ژوزه مورینیو شوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/30476" target="_blank">📅 14:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30475">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">📌
قیمت روز خودرو/جهش قیمت خودروهای مونتاژی در بازار امروز
💢
آخرین بروزرسانی قیمت خودروهای پرفروش پلاک ملی طبق استعلام از نمایشگاهداران و دفاتر فروش خودرو تهران،/ ۴ مهر ۱۴۰۵
⭕️
این رسانه هیچ نقشی در تعیین قیمتها ندارد، بلکه صرفا اعلام کننده قیمتهای کف بازار…</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/30475" target="_blank">📅 14:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30474">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZMuVBmtdWqK-zVm60y3P_zQ_SYLVK2nJQo2ePOiMmB328t3XmUQKZAgqqfijxkEvYsEko9WUdEkSkHMJfhHNAtyA9zQOF3lJwPaBzFvFx-lEhZg-xKIojZz8zCEf4YKF5XgA5t9twnZ78enMYq-CVx4JzAiT3pO_-jaRBJ6Y05Zqc1IBP91Wxhug2vvMenDuwxD2Fy4JpSvqZd0s6Aqd4Rnm-lP_RpOvYreMoRQmGaLMksJ-PWNSmSQv-wqYE1i3qMwCwwAv5B1BVjYimhNIX8SWfZWdh53A-L_EhjCUKz0ufB5rx6VmAXB2609bzEygVYRHLjG7LuZeYYW4K8L8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برسی کامل‌ودقیق سیزده سال ناکامی امیر قلعه‌نویی سرمربی تیم ملی در رقابت های ملی وباشگاهی؛ وقت بازنشستگی فرا رسیده ژنرال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30474" target="_blank">📅 13:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30473">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n40Pcado8b9ZN47Gcv3uu6AXZCegy3shO5dBjatME7vbl-G0wpwAtcFDnZDx3fDktAQPQx71TMxfc5qIP8J-4Tho9bUgqtf60ihB9IpvZGCQR3XlLyuo2GJgGC-VZ0bxbnaXTdz1WsDh0QnpaePSeLfQN4K1kjK3TX2xTLHpv9Wi83MVPFW0v_fCBTGcd6-K5UARZ9JLU1M11-gYdqnNZtj8JsXBisFuNfqvnqEbwkj4ifLC8tJJhRps9oO61k86GIW0SVTnjiJHkMCeYQZ4f9d1sZvTwxHgmJ5fpuGZX3D_2EOW6oHeQIweg6bhBTKburYSmCiZC3QwM5Yj6HHw1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🟡
#نقل‌انتقالات|فلورین‌‌ پلاتنبرگ: جیدون سانچو ستاره‌انگلیسی منچستریونایتد درآستانه عقد قرارداد و بازگشت‌دوباره به تیم دورتموند قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30473" target="_blank">📅 13:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30472">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63e94cf509.mp4?token=MnEsFsuuyF6I-suuExGoG4BGR8GMvkxRSZG5OadH3GA_oK7mANF8skjryodeFQy9sza4d2zNNSLXjTB4jOGOUmlDcM4OHPP9ypR5HLmqH6KwHz9CiTndM5cBsaNcL6k0SL7RMsd0SXz4qYemffd2E0P6FTf15QUhpiIQbCmRjicopYSbp7YV4QS0rBVQPGqm1R20D4eTTL_6gRCM10KjKGzV6A738BMUx2MWkUrP2_4sjlAl2hT_AGaWTfSgznqm9zhchsoOv5CSnSxeLyIaDCvokBXOOMMnSwKrAajMZzcHsljwZO3UAFlkFK8cjWF4w6t-FlF0Sieaow-kdqiNjEZcgUgnOBhnfKgnH_SoyNsJ9pUnbHALqHOn1Nw2nkqvQZOGSXQHpD1_KFRXg334HVbR2rwrjMVgql_jGtnAzjfEMK6XwYYxjJl9gBKTcFBIwugjCq1DH4jgrNhENHYi__pFkQcg-c2KvtYeLpTehC9OMl0Cw_T6SpSM54fbpzl2mFtDlEYTObS9FUQokMs4cVkAe-mf1CekfQl1R7SlsP_E39LPAU2tdAYnlh-54mqmcfK0iKfhnamXKdeq9L6RS7oDAkDYjSTbJbrMnRbBQdLncD9w-EJLHMZaGj7RliKqy7gpB76CsxZWiJ88QcZbEIgCtr1BEZzh0nGOsKTDcJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63e94cf509.mp4?token=MnEsFsuuyF6I-suuExGoG4BGR8GMvkxRSZG5OadH3GA_oK7mANF8skjryodeFQy9sza4d2zNNSLXjTB4jOGOUmlDcM4OHPP9ypR5HLmqH6KwHz9CiTndM5cBsaNcL6k0SL7RMsd0SXz4qYemffd2E0P6FTf15QUhpiIQbCmRjicopYSbp7YV4QS0rBVQPGqm1R20D4eTTL_6gRCM10KjKGzV6A738BMUx2MWkUrP2_4sjlAl2hT_AGaWTfSgznqm9zhchsoOv5CSnSxeLyIaDCvokBXOOMMnSwKrAajMZzcHsljwZO3UAFlkFK8cjWF4w6t-FlF0Sieaow-kdqiNjEZcgUgnOBhnfKgnH_SoyNsJ9pUnbHALqHOn1Nw2nkqvQZOGSXQHpD1_KFRXg334HVbR2rwrjMVgql_jGtnAzjfEMK6XwYYxjJl9gBKTcFBIwugjCq1DH4jgrNhENHYi__pFkQcg-c2KvtYeLpTehC9OMl0Cw_T6SpSM54fbpzl2mFtDlEYTObS9FUQokMs4cVkAe-mf1CekfQl1R7SlsP_E39LPAU2tdAYnlh-54mqmcfK0iKfhnamXKdeq9L6RS7oDAkDYjSTbJbrMnRbBQdLncD9w-EJLHMZaGj7RliKqy7gpB76CsxZWiJ88QcZbEIgCtr1BEZzh0nGOsKTDcJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ناراحتی آردا گولر ستاره ترکیه‌ای رئال مادرید از مصدومیت کیلیان امباپه در جریان بازی شب گذشته دو تیم ملی ترکیه - فرانسه در لیگ ملت‌های اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30472" target="_blank">📅 13:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30471">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cj4PcZ7R4GG91FuMbSg2bgWa2p8j4IdDc5v4nvFK-3WNYCygg-xjhYuiXQ1_5qGBTinSgBgQyCSchkaPkLa_udjJKEJi57f8S1wfBFKcxFCNmLXGK-Hs3IhKQzLeWO-m87p6zfuSnvD9tSXGcHPLzBzy2uORvBVQDF2iKzdAROrsHnbsWL1ZpHJN1RDNCn4Y4rMyyU6NpFedJDbtNIxVqJ_ZD-C99GNlAv_5gITgkye8Nk7f4kdY4q6WhYj_P63egbsx4xAWfmAfnI8ZDG8Fp3ipNPJdk1aDuFdNg-WEn1-kr3QA3bsBCkQlR1ReMetGRXfgWHs21CNjej4J1WFzZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درصورتی که اتهاماتی که به من سیتی زده شده ثابت بشه جام‌هایی که در لیگ گرفته به این صورت بین این باشگاه‌ها تقسیم میشه: منچستریونایتد سه قهرمانی، لیورپول 3 قهرمانی، آرسنال 2 قهرمانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30471" target="_blank">📅 12:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30470">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jblR2ipHxLhjKSS_4uGwFXnj1gqTS0jtmxLrwhu2XB5nf3z_5yBVb7YzOb3elATGNWDsPl7VHllT-gH93EWoJ3JTsx1-vn3wC41wDI40tJeeHuGD-yCV3mEbrJYMqoboCJhF5ylh7lnWGoXahPx0rCwXTF5cHTKyIBm4hRBFdSx-lfmh2g4W3V3zFC-zRSxBTyVwxxgMhx0e_hq8ichQRhU7Dzam7MnXDQfKtB2FcmmWNzXZeJYQI6WO_2A_v65OMZw88b4lebCYbMtMwiw0IdSbQ7H0BsbVawNyhp63q9iJ0fB_46i8OHbYyuF1_C17Gura75FjPNHeIDil5wPKdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇹🇷
باشگاه رئال مادرید برای تمدید قرارداد آردا گولر ستاره ترکیه‌ای‌خود تاسال2032 به توافق کامل رسیدند و فوق ستاره به زودی قرار دادش رو تمدید میکنه. پرز دستمزد آردا رو حسابی بالا برده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30470" target="_blank">📅 12:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30469">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHsVMHc9S-VAJDf-IIgadz5ESu1gr_Az1mxZyDfsMMr_ViSudFFeIJJL6zBcVqxO0t8Bku6XbqbRFLCfI3B9KtMTFYkbnFGPqVWla0j71yoN9yUcwgOFaXs_yHBuVCWgHYCbxg1hkhS62MAZfgaOiy7m_i9MRoG1O4SNUazTYUeYYHRJ3-ltB7YjvxEQJelyTvYcEAE7MfgI2ae387B9viBPHXht56UzjPOFQIa7pK53NHNM7wuFkS0V5lpoWmDas75_wYYGhLbFaOxL5_Wp91AtYCRJnncGH1z6OLWdvKP86ngAyDeSDi9Bw-OILVT7MIiJmJynOKRh1Mc_1kL55Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
شوک‌جدیدفیفادی به مورینیو و رئالی‌ها؛ در فاصله یک ماه تا دیدار حساس با بارسا؛ کیلیان امباپه فوق‌ستاره رئال مادرید در دیدار امشب خروس ها از ناحیه‌کشاله‌ران مصدوم‌شد و زمین بازی رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30469" target="_blank">📅 12:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30468">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea4b13e0d2.mp4?token=pli_1bA8I3M2WdvbM-8wj81ECFZ-c7ZjgGvAQJpiEOnrfiTC3fz513Fi4OTW_9EYYUWFf3LkI10AyfVWp0YvVLWYUqixPSXN30WYU4ixedIPuYX-u8Y9OKhZzS39jFVMg6vhyxLRTfsay22nVPbH93oPtyi13c8ggsW1MWvYftlwh1S-hBWN-WJ3QL_BT7ok_kIXuAG9e5vEvWxEU0m5_V2NeT79SkZcRrTmQS-iTaL-4YLkvUqv5d9sYGbMDIMQGUA7rOuLVcjBwy8PAjJ81RmYD1pj1XcdxbVfZwrVF0EutcPWJTUcRl2yfkZQ5kS4e1BuGnk7__3NG4gYS0O2tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea4b13e0d2.mp4?token=pli_1bA8I3M2WdvbM-8wj81ECFZ-c7ZjgGvAQJpiEOnrfiTC3fz513Fi4OTW_9EYYUWFf3LkI10AyfVWp0YvVLWYUqixPSXN30WYU4ixedIPuYX-u8Y9OKhZzS39jFVMg6vhyxLRTfsay22nVPbH93oPtyi13c8ggsW1MWvYftlwh1S-hBWN-WJ3QL_BT7ok_kIXuAG9e5vEvWxEU0m5_V2NeT79SkZcRrTmQS-iTaL-4YLkvUqv5d9sYGbMDIMQGUA7rOuLVcjBwy8PAjJ81RmYD1pj1XcdxbVfZwrVF0EutcPWJTUcRl2yfkZQ5kS4e1BuGnk7__3NG4gYS0O2tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
تعداد از کاشته‌ های استثنایی کریس رونالدو فوق‌ستاره‌پرتغالی در دوران‌حضور درمنچستر و رئال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30468" target="_blank">📅 11:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30467">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c87985ff1a.mp4?token=TGC7sPip9LVM7g5003YDFaF3sU4n2F0ODa0ntKDCj-92QHAn9MBWiuV7dCzRlPw2LQpBcXkeYY_TQYj5M_QyO-Ft11mJc6vdpPXni4deD3BAm_OR7ji0D74qBEhBhzh2Mt-jyQWFNWOWW2D5-sdIBiB79oeTsM7fMBRfLbliXFC9HRStgXlgyp26N7gv4cYjCsl0TvqXPukNfM1eoZYyoLZnaK7aEmiobURBXHgyvtldipnNO9lA85oowQVkAtMvba20ulEXDXcPUsyy_4nMuMCkANPAiztgPzqzUFRz89k2GvCuOnQFLdYSEQa2Ei4AbIsFe3cNUMF2VboOVxaVUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c87985ff1a.mp4?token=TGC7sPip9LVM7g5003YDFaF3sU4n2F0ODa0ntKDCj-92QHAn9MBWiuV7dCzRlPw2LQpBcXkeYY_TQYj5M_QyO-Ft11mJc6vdpPXni4deD3BAm_OR7ji0D74qBEhBhzh2Mt-jyQWFNWOWW2D5-sdIBiB79oeTsM7fMBRfLbliXFC9HRStgXlgyp26N7gv4cYjCsl0TvqXPukNfM1eoZYyoLZnaK7aEmiobURBXHgyvtldipnNO9lA85oowQVkAtMvba20ulEXDXcPUsyy_4nMuMCkANPAiztgPzqzUFRz89k2GvCuOnQFLdYSEQa2Ei4AbIsFe3cNUMF2VboOVxaVUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
چهارده‌مهرماه شاید یکی از آخرین شب‌هایی باشدکه مسی را باپیراهن‌آرژانتین می‌بینیم. شماره ۱۰ بعدِسال‌هاافتخار، جام و خاطره، حالا به‌آخرین فصل‌ های دوران فوتبالی‌اش‌نزدیک‌شده؛ جایی‌که شاید هر بازی، آخرین قاب از حضور او در زمین باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/30467" target="_blank">📅 11:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30464">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c60d4945a7.mp4?token=d1Na-rP-KT0RlpaVRw_Zwbw4PAsRU0p3WY4PexKPh9V1c1tdnBCCosJt4378UXYFK23EgCRIz9pnGgIa7gsmND2qgRyLxS5r1UXApZSpNbMjURMlgqJ3ejj59owo7YxxdBINrOH-Rl7cJ-1zyzbjNPhamGfeDo7tLQiN6Fbe4cmLRFmDJRmbQAnBmI21ushTif-_ozJUH-wCQ6h4fNH3j2_Ro9QpbjE8B7q-OcPGCupR2BHE95FescbmxPH9nJJOlTjOszy6hUdDt2X-qM-ZqbiTsqJPmYWJjfYGur85cAUWUSwUUQyJSbtdHB-ttnQZNsjamFriDeTxRRCXZBrPq6CB0tNps9wX2Hqi8g9TQIFrnMReZ6b3cNDgxRBdrF3NlwLrhrISJvaMScMyscQnEt0MoK4LWPmAwN8zYTCNHsnjigLFK7zn72R3brL7gdEywDek0P-5j9-pI7osEEKTE8v4NaWu6ddpRdN07EGGbJvGffk0vO6IBR_-SBW0X-v0_6b--PkD-z_U3nozygO5XzLuH1dpV0nsNTovIUET5UTRr8Re9HboKu-14t_O6V1wY2BIuGmoev38YS-JD9Cdz8u0AMCH9U-iUEMY_p6Ea8Yeujus_PmAqYztIYSXEEd8gNPEZdqMzcqdLJ3DJDHKTLl0OY4JT7rWG39MzN9T5Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c60d4945a7.mp4?token=d1Na-rP-KT0RlpaVRw_Zwbw4PAsRU0p3WY4PexKPh9V1c1tdnBCCosJt4378UXYFK23EgCRIz9pnGgIa7gsmND2qgRyLxS5r1UXApZSpNbMjURMlgqJ3ejj59owo7YxxdBINrOH-Rl7cJ-1zyzbjNPhamGfeDo7tLQiN6Fbe4cmLRFmDJRmbQAnBmI21ushTif-_ozJUH-wCQ6h4fNH3j2_Ro9QpbjE8B7q-OcPGCupR2BHE95FescbmxPH9nJJOlTjOszy6hUdDt2X-qM-ZqbiTsqJPmYWJjfYGur85cAUWUSwUUQyJSbtdHB-ttnQZNsjamFriDeTxRRCXZBrPq6CB0tNps9wX2Hqi8g9TQIFrnMReZ6b3cNDgxRBdrF3NlwLrhrISJvaMScMyscQnEt0MoK4LWPmAwN8zYTCNHsnjigLFK7zn72R3brL7gdEywDek0P-5j9-pI7osEEKTE8v4NaWu6ddpRdN07EGGbJvGffk0vO6IBR_-SBW0X-v0_6b--PkD-z_U3nozygO5XzLuH1dpV0nsNTovIUET5UTRr8Re9HboKu-14t_O6V1wY2BIuGmoev38YS-JD9Cdz8u0AMCH9U-iUEMY_p6Ea8Yeujus_PmAqYztIYSXEEd8gNPEZdqMzcqdLJ3DJDHKTLl0OY4JT7rWG39MzN9T5Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعدادی از گل‌های کیلیان امباپه برای رئال مادرید در دو فصل گذشته بعد از پیوستن به به این باشگاه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/30464" target="_blank">📅 11:18 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30462">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WJoBVY68Tc9d9dDi35klgPz57PnIg4vEzfzxQuxkFkeWD0WDUT1JKJ5eLkw_nCWby2CGorAI5KDydJQ2UlZj05D8Ho1ZasHOMhHeGODryhma9Xgkg1oh5Ee3Qm_86EOeRgox42KK4zoAGwAw6bcIzXP5xMuGbpCh14LVEjMAOeM4CvSXIiuUhk3QCBF-6qiUGEtfING5Gd8LiabrTXVsXEGpMli8vdUhf_LuaY4qPuOvuhqtnmcIZqsftJukQni0lCmj5h0JbWnhw9SqTb5IJ4s6TvDcKEIYAb0O0kHVRBuUxnY8vh9xQx1EbwzN5D13NEA7Y1x-Ndy_BI8khGW3Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mzPANDyhj-tEiR-5twSmskVgpsqSUZ-ZYe_ivdz_g0XvR9Bx_MfV7XSITvac00nBgSl81U8taMHsOYr97zkkz-4VoFMX3nH0Wse3gRsasZcFpr8MQMgv6miQN73Ki5jb7PhffAz4a9pSHEtlg6qPLsLTKnJR1Sjwt8V9CaWD5Zqoj1aBQbV1_bCeLnXA0QYoaPuuCg2bwQE-9GfR4QAzanoltvrXw9zCmsLOl7n89c-WHhTmUwEBdR28lfSLJdovDFz0linLtfr9a3f7EGNQonYzfaM_UUFU3Ho7LG0V8AVgFNaY3z1gm2TyraOXT7rza6lcVDTh13YCASQmSR_VQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
برسی کامل‌ودقیق سیزده سال ناکامی امیر قلعه‌نویی سرمربی تیم ملی در رقابت های ملی وباشگاهی؛ وقت بازنشستگی فرا رسیده ژنرال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/30462" target="_blank">📅 11:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30461">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه‌استقلال تاپایان‌هفته جاری 400 هزاردلار به فابیو کاریله پرداخت‌خواهد کرد و پرونده این سرمربی درفیفا بسته خواهد شد. نظری جویباری پیش از عقدقرارداد با ساپینتو با این سرمربی برزیلی قرارداد امضا کرده بود و حالا بدون اینکه پاش رو تو خاک‌ ایران…</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/30461" target="_blank">📅 10:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30459">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6160de2528.mp4?token=e74cgiDcT8pBP-O7LIQEQbee8AmWhG18SC5_Ksm23Pe5T2gBeChejoqu4bsB68xB8fzrr-W1r9ZkSRfJBu7G2NoT_OkqWkhKCeR56mfp-w6NhzsRvw9i-z_Kp01JR3rbgOz0eLycESuYfF0LuE5UKoKLO39MLEigGegwbQiTMO3bchIE7DHyA7W3zSaCeUC-ifm7eYx9pRICibTWCrxqNKFjqKoD-hej1I8oyiw4uQxwNkaQNaKFgJBZ_uuDqiiixqN6-AaDLCAsrsbUXbHEFjCEhGCg_2SKp01-6Lb5-FdVUwwsCzwxoWhDGKpoOjYLZ38ubo9NvpZfx4bUsUN3WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6160de2528.mp4?token=e74cgiDcT8pBP-O7LIQEQbee8AmWhG18SC5_Ksm23Pe5T2gBeChejoqu4bsB68xB8fzrr-W1r9ZkSRfJBu7G2NoT_OkqWkhKCeR56mfp-w6NhzsRvw9i-z_Kp01JR3rbgOz0eLycESuYfF0LuE5UKoKLO39MLEigGegwbQiTMO3bchIE7DHyA7W3zSaCeUC-ifm7eYx9pRICibTWCrxqNKFjqKoD-hej1I8oyiw4uQxwNkaQNaKFgJBZ_uuDqiiixqN6-AaDLCAsrsbUXbHEFjCEhGCg_2SKp01-6Lb5-FdVUwwsCzwxoWhDGKpoOjYLZ38ubo9NvpZfx4bUsUN3WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آلیشالمن بازیکن‌تیم‌بانوان‌کوموایتالیا با انجام این فری‌ استایل در اینستاگرام کریسمس رو تبریک گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/30459" target="_blank">📅 10:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30458">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0F7QmKuW6rrSITRxICtPK7VQGa2L4go7n1DbIqxx3maU3cYKiQg2iXEvx8z6_YBQC0ql9IqeBOzAotJa-mpnY0YBWWlTGGVGZSDSRhA0CVNC-cFuv2wa4SY6kuLDgz3rRaXECZw2bCS5vH3ZPDIJ-KyGPoF1MJxBl0GRlVt6uc4RQKT4mhuZRUI7ruPswA_GYt0W23zLHh0navMb8GKOHv2GUbOgj_fIZv3dbHFZ5V8rUlFMz_XKWbx6q-0-Rxr7AJ84V2hEyC1w0lqCrbgzgbuqGD3QgwPFFcKD6hGw-w_9aSxTyLab9oEscRDzRqWqTuza3sLPWKOl6UzWPn2bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال مذاکرات مثبتی با فابیو کاریله برای تسویه حساب و بسته‌شدن‌پرونده او پیش از شکایت به فیفا داشته و بزودی با پرداختی مبلغی این پرونده بسته میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/30458" target="_blank">📅 10:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30457">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tN_K2gIfVuM5yC6wYgEnGXVkXlpi9OxALCF-V9nJFlNS11mFqEWolGSNtPDMDuqZI8rdRj8-e1108Se7w4MdvUkHT8P_8n0mTYekEJ__LUO16rG5RpIqd55eL8jhphwB5DQm8pdVWCen1JBExW2ix2xFlnZCOPGAmQA8xxgFrofswA2b9HBoB178ylbBzhgqXg0fRAwWmPyHcfLukO_v2H8WsbetC1PdK1QfbpcvmkPiYdF3qt8xR7RkkzBtPsNLlO0KmJIybyu8Wp0HnEjjAVeJQ2ef9YpM_YdCCukLT--MH_E0deVcUwSUYZXMuadOHtVYp3IxnwkR7HPu1ohTEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درصورتی که اتهاماتی که به من سیتی زده شده ثابت بشه جام‌هایی که در لیگ گرفته به این صورت بین این باشگاه‌ها تقسیم میشه: منچستریونایتد سه قهرمانی، لیورپول 3 قهرمانی، آرسنال 2 قهرمانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/30457" target="_blank">📅 10:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30454">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f59d54b38.mp4?token=TV5uhkzX8yjGNiOZn3grUpDaCye6IwpSeeUgWZABUDY-Zczjtn7kVaSLHtxj8rdN9vPIHyDKBBhaRB6kHZaIJmLHMi63wS_KHv8qym6cg13UCe2gJsDLrZxhTfP0vMWtfQ4KE_k521H0tScuEGAIRnDTYMIPCTeRQz1mbc1VXGMZ_LsvWasyuKJdGFiuQcEQur9s8Vj8Un30UenYsd3K0EQ6borIQmXhrT6K9hHUioxorc_6mKdoXGWonLQwhUT_si5jpovc-SPcZwG11x5WPl9IKNRw04okhhao55EO4NNhxhFcjHN5PH0zaoBe_78_6x1Ed_tEZajiD1LvTknzlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f59d54b38.mp4?token=TV5uhkzX8yjGNiOZn3grUpDaCye6IwpSeeUgWZABUDY-Zczjtn7kVaSLHtxj8rdN9vPIHyDKBBhaRB6kHZaIJmLHMi63wS_KHv8qym6cg13UCe2gJsDLrZxhTfP0vMWtfQ4KE_k521H0tScuEGAIRnDTYMIPCTeRQz1mbc1VXGMZ_LsvWasyuKJdGFiuQcEQur9s8Vj8Un30UenYsd3K0EQ6borIQmXhrT6K9hHUioxorc_6mKdoXGWonLQwhUT_si5jpovc-SPcZwG11x5WPl9IKNRw04okhhao55EO4NNhxhFcjHN5PH0zaoBe_78_6x1Ed_tEZajiD1LvTknzlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مورگان راجرز ستاره انگلیسی تیم چلسی:
کریستیانو رونالدو بازیکن مورد علاقه منه اما من در نیمه‌ نهایی جام‌ جهانی در برابر لیونل مسی ۳۹ ساله بازی کردم و باور نکردنی بود، تصور کن در دوران اوجش چی بوده، نمیشد در برابرش کاری کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/30454" target="_blank">📅 10:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30453">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b295745c6b.mp4?token=P1HHx1Etqh2DcAF9bICRx_F0s4JR-rsE-r81gNtGbogNwacIMyiiVkmhTMNA0DY8f_RsxwtJSzFM9YFxXOfKwXlq699gkQGGXZeYczfApBTfVwDsy8-1wRDp3rG17OiPvvnQeKL6wnZSTBTACbKSNQf5cVQ2bzw8dTNGo19Q4er5tCY_6xrOlyC_bEIFYYFEh2pBW8TwVpQIw29T8bY_WUZN15CROwUF3p1QM-vOcnqaP6d8GrJJeofqyG0bSH25kK0efoiwARNqHUP0fbWx6bGJ-6nkra4cMOYfaeJpWpwg2xNjtZRRnTDIoh66OrRpwtq8L0D6N7owRG15nm6HqmQFOLaer1CWy9Gx6RAolEzdCuMwqqZjEZTiX92LRqxDce4EkeaNWlnxJk3Z8BZoiZP3zmWT1SeIxpfPf8aoqXkDJTfzkq2Q8Dq4CaTfUhPrrLATYy6KN6l3Wu9Vi84XWpR9AmkFV9QzB7F7vwQ9mutO7217aGUa4OpOS5UYbzMeO-toioNb0pB0ukgWZfyAoQPodJl5SQwEyhTtjMP5-2FqD4ePGt_gHlxDorrmat82HOUi6MNzo3nB3UacvB8bFD88J-mmdZ5yPjgNYYeGOylYzfx8gpHWCLs7eclUc8cKYcjoXOxgnrmnu3LNhETagdiIdQdmEPH7seL3KPuqgKY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b295745c6b.mp4?token=P1HHx1Etqh2DcAF9bICRx_F0s4JR-rsE-r81gNtGbogNwacIMyiiVkmhTMNA0DY8f_RsxwtJSzFM9YFxXOfKwXlq699gkQGGXZeYczfApBTfVwDsy8-1wRDp3rG17OiPvvnQeKL6wnZSTBTACbKSNQf5cVQ2bzw8dTNGo19Q4er5tCY_6xrOlyC_bEIFYYFEh2pBW8TwVpQIw29T8bY_WUZN15CROwUF3p1QM-vOcnqaP6d8GrJJeofqyG0bSH25kK0efoiwARNqHUP0fbWx6bGJ-6nkra4cMOYfaeJpWpwg2xNjtZRRnTDIoh66OrRpwtq8L0D6N7owRG15nm6HqmQFOLaer1CWy9Gx6RAolEzdCuMwqqZjEZTiX92LRqxDce4EkeaNWlnxJk3Z8BZoiZP3zmWT1SeIxpfPf8aoqXkDJTfzkq2Q8Dq4CaTfUhPrrLATYy6KN6l3Wu9Vi84XWpR9AmkFV9QzB7F7vwQ9mutO7217aGUa4OpOS5UYbzMeO-toioNb0pB0ukgWZfyAoQPodJl5SQwEyhTtjMP5-2FqD4ePGt_gHlxDorrmat82HOUi6MNzo3nB3UacvB8bFD88J-mmdZ5yPjgNYYeGOylYzfx8gpHWCLs7eclUc8cKYcjoXOxgnrmnu3LNhETagdiIdQdmEPH7seL3KPuqgKY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌از این چالش عبور توپ از اشیا؛
هیچ کدومشون نتونستن کامل توپ رو رد کنند تا بالاخره نوبت به اسطوره تاریخ باشگاه رئال مادرید رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/30453" target="_blank">📅 09:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30452">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjgT2OyJs0cBydjoHaHwtchYK4h5M-5cgOpCWGVlOGRtTmucfBUZtZbXr2_ZCK_2XX810_IgmCf43XZHv6DJlvnGpcK0EOQ514DjNLH4HYvyKrbJwn3XaM4Mf93Y_F4Aeezpk8dCmnmYvVjDSiX87hH5z2hK02VSBSwfo4hb1kJOcZEAS8_tpH7QsFupqh8kvZXdoJ2KpqnZq9kCqrWJ4QMLiD7Qkwff-CWA3PN41ktiPGj5lWDSlEd5MdHnfWxps56cQbHdMlOMIc8WPPlpHPrE4IAOP8eNJlCdpBfSmOnreU04G-rnlRDojDfe6H1w42sKUh1SQLt76n_FYeIXPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇫🇷
#تکمیلی؛ بااعلام‌فدراسیون فوتبال فرانسه؛ مصدومیت کیلیان امباپه از ناحیه زانو هست و بدلیل جدی بودن مصدومیت امباپه، او بزودی به مادرید باز خواهد گشت تا روند درمانش آغاز شود. گفته میشود امباپه حدود 3 ماه دور از میادین فوتبال خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30452" target="_blank">📅 09:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30451">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHuJzHqXpGGJxG6jTOyCuM2n68I3gmiJUXvw4mIYfctdnfZkQpA7ZwMu5I8fSk0SNN0Oh9DvpvbybEV9vGmZ2v2fATME5vaOeOFGM9VLlUWkWYxWbzNVUfa1c6fYgnCE-NA44ht7nUuIEQGkbRUhCvBFkZj2qtZx4nqC4k85tZEB13ropk2cfnr2Gn2qoVqxYrCoi8GYOVX2GsmORmCoCA3jLOU1ZB4SeDkMBwvGqEWdd8ONP1eVP0QfgzeKPwb9lVSBum5CX2IaPhYcwzIOaIZrcDwlvg53S4xyn7rJN_m1FiHE1zxMh4RMeGk7MQ5zyTE9nzGF7KINmeY85WaaIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇳🇴
رسانه‌ های بارسایی در حال مانور دادن خبر انتقال ارلینگ‌هالند به‌بارسا درتابستون سال بعد هستن و قصد دارند بافشار به‌مدیریت این انتقال در تابستون 2027 نهایی شود. از نگاه اونا پرونده انتقال آلوارز به بارسا تموم شده و این انتقال هرگز رخ نخواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30451" target="_blank">📅 09:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30450">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqsHCxUxiMavmyO7LOhmqOIIbLbOPBzMcFuBi0GGtJua_juAVA9VKU-q-MzoT8y4KN2D1k17HCygNSeazLLRRxvNAG8g1-s0wMK4mHkxkKLNF2QSsl-8p25fZach7m1mvxm0z0FMZGQffE0F3U_ljSP2vzOSyKfsEP2f81Uj8ABALnNwIcFbY4SWEG6fTHFL6N5F3bcfxTtz27gJiqpgqgHa3gu0e8E-sULDYpwvR4hVvxgas5pwcZzm9YPWP0d8z2mkavH_DHS2uC76hx0oyx4dLiMdLfN2MxISUf7slVk-ivVURAReGgNwug3DjDmpt-bTylSqBkWvY-23Za-A7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
شوک‌جدیدفیفادی به مورینیو و رئالی‌ها؛ در فاصله یک ماه تا دیدار حساس با بارسا؛ کیلیان امباپه فوق‌ستاره رئال مادرید در دیدار امشب خروس ها از ناحیه‌کشاله‌ران مصدوم‌شد و زمین بازی رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/30450" target="_blank">📅 01:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30449">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34b91abd7e.mp4?token=Rr7dTjS3qJhfA9jDCsW7H2Y35z8L6JZpo1bJc_ZtLVXCphp19d-hDWmQI3mjI4hv0B2lg5blKsaMOjB8NrF2o358M3BrUO4CrXDG9pnfHeEKgYGfIOKHMhHNd1IgMDFwI_GQKABmlx5xowC4LyFWSy6yiQw9VLMNZFOfZPmwBnrGaCQGAdwLZ7VTvhQAQ-rb_rDXENDCby-hkojbYPFHT7X7F-7yovWUmMVI34oaXAzqhBPXiSUzDwirxtRFgp2LZG4bXfs9xwkc9iR9i7WyicIwF6BiVoGVCWean1nXcGcUE-kTJTen8N5-EApoGmgYELHbB8STyWWdWOJ0tblRrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34b91abd7e.mp4?token=Rr7dTjS3qJhfA9jDCsW7H2Y35z8L6JZpo1bJc_ZtLVXCphp19d-hDWmQI3mjI4hv0B2lg5blKsaMOjB8NrF2o358M3BrUO4CrXDG9pnfHeEKgYGfIOKHMhHNd1IgMDFwI_GQKABmlx5xowC4LyFWSy6yiQw9VLMNZFOfZPmwBnrGaCQGAdwLZ7VTvhQAQ-rb_rDXENDCby-hkojbYPFHT7X7F-7yovWUmMVI34oaXAzqhBPXiSUzDwirxtRFgp2LZG4bXfs9xwkc9iR9i7WyicIwF6BiVoGVCWean1nXcGcUE-kTJTen8N5-EApoGmgYELHbB8STyWWdWOJ0tblRrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش بازیکن شماره سه تیم ملی کبدی بانوان ایران بعد این اتفاق خیلی خوبه. اول برگاش ریخت بعدش رفت ازش عذر خواهی کرد بلندش کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/30449" target="_blank">📅 01:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30448">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZbVXL1lnyStswIvBYCCFVq1kSjom2OOfYjWv3ade2eEmNFUnE43qZOAlkx417PQQmkXMg0RbxRCoyjFMaCxsao38C4SmsKyjIEGj7fPFyXPZ7PXxNp0YG-jrV6ZsxKodIjvRzNEeDQJgk-NCLmvToW9GPOjDhgztnOLmHHeqgyVZ6q0CaUXBcCWcM21k8kj3a7UIYfzki3gTpD5ogDJ1iUTJMpAzlB3VmC4k5DKlFG7EkhXxcF35x8gDB9Nri6wFtQZo1iOX89BoLMfV4TP73BaWVKCslvyeH-V6xiVl0i-jPp-SrqQierGhdLxY0avskk_Sn4W0Ve2pOr-5glqPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛تاکیدچندین‌باره سهراب بختیاری‌زاده به مدیریت باشگاه استقلال: بین مامه تیام و فابیو آبرئو یکی رو در نقل و انتقالات نیم فصل جذب کنید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30448" target="_blank">📅 01:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30447">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDn9C-ywi0hIdAP1DokyyEGcSc8SISjGuALUGmWNf-k9bug1pm3MRuQVKU96zOrHmYbdeeABkupNHjfh512KINEKiMMzzvbVzB6CJni4SSxHm1IS9rYAwxMoUhmnf2f3ehQ0GITphRGGX6Oe5jaQMCVbXDkY2oVHwi5OsuuKs9WbBcZKcCgb9EMWtZuVNTsWCOpjpRiH3DxIKNR8KbAyB5nV2mywVTBxcga5tzJfGboSLNn3BwnwWpQNWwSvyMaB5vxzki6R4fEqg2_xJbRPh7SRGqnaaybxrtlVIQ7SJzkQv0LEq0HbGsWsXXtvyKuSrBkpv8H3mGNgJinVgA7npg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ تکرار فینال یورو 2024 با تقابل تماشایی یاران هری‌کین و یامال در ومبلی لندن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30447" target="_blank">📅 01:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30446">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKlOgxZXG6uOxiqcsRaS_jxAhCUieVK9wQeYbN51ezFnfFUq1ntCLjTrWy0iqYXj8KnGmckkQ1NmS_X1FX6cU5zEIL3F7bOgi626Q57j0KG5X_CdowKoeTSAzMk8g4wcCWgyukXZpLiMRrZDda6RmBoMZUwjRndkJs9S5e5De60pJe5nYat6PAL4RRma4Ne9LRWPo1qKQAQ3uAjKCx8PBpXTU_Nu_xtO-4YSGRcNwrfpssfuiBBGyxswTKtRfFsH3dQFFc1UmNVMe3S6zao7nK-_CQKVoxJyxXj9_nhwr2DUKwKmprl8_iKTgMP713n-UFyYMBhiW9kCSPyqHEADWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌ دیروز؛
برد فرانسوی‌ها و شکست ایتالیایی‌ها دراولین تجربه زیدان و بازگشت مانچینی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30446" target="_blank">📅 01:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30444">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoiF-yvlL_XsdA1T9SPssxdPX4VTlxJBvm7HQ6gvRtMovH5leyLtQf5P04Kfx8ul6CCrLGKb6yARKGE6tE4jKvBE-6sQl_9-dPZ5GaKUeE6-SuIHV9YMc5d7ecztRrJODY2-ZsGJowSUi2RZpGIcyXC4HSAH0mIcycVe-EDjrl1XkIdXFYa1vvqNWWGY3MYfT5Ev1LpWDOHJ6SHvrFIaiHUdMqQ5Y3gU5y0nGp6ovV-nPrkoQ2-nuU-4T0qU0IEXLakw3Bruxs0NcTWwaX1ING1mv-FJudsU14YOUdFFltVIU9dwPTZcxHKxsDtMOOooyXRYQgL-lnnFIdDkKHnsdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازیای امشب هفته اول لیگ ملت‌های اروپا؛ مانچینی با شکست استارت زد؛ زیدان با برد. سوئد با درخشش گیوکرش و ایساک سه امتیاز رو گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30444" target="_blank">📅 00:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30443">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B65wWZKt_ApIDNqh9suFIWq35WVODbmeiU9HGxizqjQDkyIwk9CcSEOOKKNwoWbUCjEZjzv2Uzr4sqjK7N6m7X2sQaV3leMLcaplh28uX9w-2AekCF7d_0YDbGtTVMuCfwBkjgxEet32civjB2tq1wzWO0rzdZzZv5gotkTiB1wCkOEX68twkIlOlzC_TYGLthGRXTm5X3A3LmyVoahs4fEr0rmDr5zzXnWvL_a1R7oWPIcA-7wTTJjG3F-dM-DfjMj4xv8xT1h81bvUnGJHboCcX5rrGovfIDXWcFPT9dGpLMDwsiYXJEnacoEhjlb5RETeqOflRVHMZxP1EeYl8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز؛ ازبازگشت زیدان به عرصه مربیگری تا نبردخانگی لاجوردی‌پوشان با یاران کوین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30443" target="_blank">📅 00:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30442">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3J0qWEVX4G12njHT0z_1ePKPBwU3MKcU0chGlfOAtUTmPbI8JKEkWAEsdFbUQvi0DDl0UAXbkEscLKXR_dMpsKPrpOj4TT9GOKBP585LhN8qNpHYLytMyQbNvvvSkQbmY6o2W3OMwuNgAR5brsLH5hqGnFtP8O5ysZKnytwr0ZxZM4dtIdDFNiGWjnKB3fM_UIBx1jboXoyU9TjuFSCd_9GckQvYfAVMODsMjywleEMVqUKQeyUO57rOBXpWXSlfoXAIiHXGLTJIg3-8svRDsdUE7NYnMTvsxQ69n9azNVd68U2QZ2EXFNlFtBESZbN6WQfR5vyO__svOCJIhD8_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ قرارداد مامه تیام با تیم چوروم اسپور ترکیه تا پایان فصل جاریه اما هر باشگاهی که او رو میخواهد با پرداخت 300 هزار دلار میتواند رضایت نامه این بازیکن رو از باشگاه ترکیه‌ای دریافت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30442" target="_blank">📅 00:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30441">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWADoNPKMLvJf4YiPcn8ruRYxnbLFYJJsgANRjnkUKG-CqHn1ttNa29y3YTxcZJRwb_LwxO3dOLO6Jzbd4gPdNpi7Xb8ArkmtGYjzZ7DuqYzC16TLD2_hP27BY4QFGQFP6OVZvd2Q-zpfpac5KeoGSm-nmN2oP3kyL2Wbtuz2BS628qavnYR6rdnvPN_8AbRw6S73MeeUCcApo7F8iEs_rsFJQSzf2MpyTbMwAPgMm7n2KvgFAUBZ480B3mQVloJ0vhOscScOunOtC3diFHBUfvsV8KTbewFCvyXu31BmLCe67RWl3NU7_mz9IE7i3Gd2ElD43Ozvjjr0-D0Cfa6SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج نهایی و جدول رده بندی رقابت های لیگ برتر بانوان در پایان مسابقات هفته دوم رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30441" target="_blank">📅 23:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30440">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XG41zGVf7AXLbH9Bt_lK_cZ7tO6uukd59pKynTkv3K_U-X2gYeSAbqgzYTmZS2DfeF01yMBtNFu-GS6kit6mkEOPsS3IMsg1OfF2jDwQgyR_qKeRQ7375tUkrJLNF-21tRYA9bzsIG_vWQG8xfXB7jZNCNQfbXnQkgtGBnUVcfR6HT5PE-rOUpPi_nzHvWCHy-edsmUH4PWOoZEPPG21m3k6g4m4wo2Iyk9rFJW8P8GvTS_iAoIxljx43czaVw_REX3j_e-Rqlo7WLJ6e3aE3hkMwrawKx9kvPT3OWjxjxjHNn8IknvcGLE7K96WznTJp-MnmClCWMJupMFN12zhhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت مصدومان پر تعداد باشگاه رئال مادرید درفصل‌جدید؛ فده والورده و ابراهیم کوناته به جمع مصدومان پرشمار کهکشانی‌ها اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30440" target="_blank">📅 23:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30439">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔵
👤
مهدی توتونچی مجری شبکه ورزش خطاب به حسین گودرزی مدافع‌چپ تیم استقلال: مطمئنی استقلالی هستی؟ فردا روزی مثل جلالی نری داخل یه‌برنامه دیگه بگی نه من نگفتم استقلالی هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/30439" target="_blank">📅 23:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30438">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vm8E2sgsj74P8Lcs19Q_EE9W9aI9Yk2yRpPNwleEMmANvtGDPYsYJ5t43yCFfQZMy0BxZUBH7VVUk-IqdWBBzvxxk2o5qi5_1RSXJ_8nPAM9Lgu31--OtmfbfqS9aWhxG4bTlgryaz9Pn2MRKmLNf_CDbix6PM7tGeaKhELMfjLjFF30xeWVEdj-Ir1gcczifgN3tRRcEk7akkAd4SGr8Ssq-4KxWbZ8QqYm8tmQNSu4shiwie0L2oHsu0f5dRoLi71Mu9xgqZ981rK9ks0ERvprZ-cyUYCL1ePHjjz4idm21Xk7bgC_i0BVJz9aKR0sdNBW4Je4mDqHVGyNOoSIAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شاگردان مهدی‌تارتار درپرسپولیس امروز عصر در دیداری دوستانه یک‌برصفربازی رو به چادرملو واگذار کرد. علیپور بدلیل مصدومیت دراین‌بازی غایب بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/30438" target="_blank">📅 22:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30437">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNIuJYQ43XIEod8GLkuWoPbAhBmNhkd6UWNdl0rAOHGT-VN1lTvVIIrAlpl2Wwe_BV68G7MStfUfpiyhT6wie2ISMPBJQpJtHE0zTEtUP8DEw5m6tO2d9NL_HEFPdr5kYcfya7IXTJfJjPugrkHKRwElB4KqosUU5mZnQP0d4quPUPJLlr3hxcCbHzrWxn8Yh2fNk-Y4_65ViZBkALgFuzXzTsCfJosokoq4v5f2c8MoUDk53MVTesAN8J6VQf4txQH1vksBFOFODk2Q1ltoTMHfs2tzlIdK9If9Exael_UvkL8XyHHHQ3IWCxQuJG4NoAvt-2NQGSrPyI_8cKfeUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🇳🇴
#تکمیلی؛ باشگاه منچسترسیتی انگلیس برای‌فروش ارلینگ‌هالند ستاره‌نروژی 26 ساله خود در تابستان سال‌آینده 200 میلیون یورو میخواهد. از بین دوباشگاه بارسلونا و رئال مادرید هرکدوم این مبلغ رو پرداخت کنند بند فسخ هالند فعال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/30437" target="_blank">📅 22:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30435">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U_Peqw6UGwnba2_GflQuGX_C7n8N9gADqAP5A4FvQY1KO7Y6aD-wtGb1NbA4Mx-0A-ClgCMdj2t_B1aQkLvRF85gUJrF1nnagh23WcitJIekpc4Atx5iGlWhroitgO8c20RKdohZ2yeWhtrryKYviCgybUcwTH3hRSdKnXAsP1jSmXSA6vhJbvUBzjYC5Uj7TQXExpiBxuKHPTuKbRKgSnRtQKCYG7aq_5IcpHjvaH1rjDcBDaN3NpPlz9dHZwIRs1hZ1W5SS1tBjYWLSNAbRQ6Kq6ebMVrI0UyCwI-CRSlVj6-pbU_xNvCYympkZv6zBpEzA1t9dQBgrEwuDwRhuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CU01ZhcECri-jxzvvAdl5pkVwpqGtJALFIzjbMnJ9ivH5ldNUUNZdjqymaRdvGYmFu7JqYEBACrp9Vd1ckiWia1uusZqb5a8dBa1Ez6cPeHyEs4wG4B0E-duky31mdC6HyHon3_Bgb08NAzTnI7Om6wqR2yqL8aw2P6-0cda74lSrAUlUuaR8mLKrR6YlyzzCGokr5LdAty7wRD3iD6kLiDJAZDP0N0WoT1wTdtznw8-cL50WWXfeeTKwfhPM3CJpd9_BeHjrSDaRHAtSXFN8b4t85I73J3IXwRiM0G4wIm1cbMYoxZC6ZRb8HgnJKx6XUXlKlyS-QEvhUOa5zIpNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول برترین گلزنان تاریخ؛
ارلینگ هالند ستاره 26 ساله منچسترسیتی‌که تا کنون موفق به زدن 370 گل شده گفته که هدفم اینه تا سن 33 سالگی به رکورد هزار گل زده در کل دوران حرفه‌ایم برسم. در حال حاضر کریس رونالدو نزدیک ترین به رکورد هزار گل زده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30435" target="_blank">📅 21:52 · 03 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

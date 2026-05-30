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
<img src="https://cdn4.telesco.pe/file/pT8HOGHVuCVSfA5O-723fw6kpoBl_zlCm30uJ__4aq07XKyHAZh9SjpYLjFjtll4F4LTJfiBn22HgYke_GzCNqRdkDDdDTrgLwcJcwxx929aTM4veEqnFxDTxcQYPpLE0N5gpIM3qBoJqG1z-74Etd00uR1zth_QbD8SuneDCjTurAQIk20U8P4S2YL2BwBlXnT3vRBc3VBIGA4eZElLGtHeWdJOkOEexcTwTgomf2t-WuPB7lL50YsooApRwHmMuxL0fsO86Of-MUTdzud54dz6sDRNP84C22rqSXD86h_qRvfOcNsoE8kaBHXhnVlzGaoL5ReJ01G2m1Z8kCrX0g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-09 11:30:51</div>
<hr>

<div class="tg-post" id="msg-438752">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCIzfB4aK9zziAzwUW-P_25PjeftBS5MKOVY0UebJwLs4yF3s3Onrmta7FY5PMMls9eC1SfoEsoxcEKdEputiXDnrBvu9IfvD2Lhm_Rl3sgTk0LVjz2kJ7QbU_9TaTyPFPbPF7h2LVd5MyHPf-3RExCjemetLsOtKfwSg0u14w5ckQsM_7mtLwd7B9JskJ5Kwb502Rgll8zWecg1uvBe8UP2IQvYYtol1fRQbEK8KnTO7D1v47MdWKceGHexhpOrym_ZwGDb298qX05DU9PL9SUX7JcyqytfNgP3u3e9GYsGGGOtVw24JsXAMClS1Gj-I3KUD7ojU_7p5qLD58tBGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارت سفر در راه است
🔹
مدیرکل توسعه گردشگری داخلی وزارت گردشگری: تا هفتهٔ آینده کارت‌های سفر در اختیار مردم قرار می‌گیرد.
🔹
مردم از طریق این کارت می‌توانند هزینه‌های سفر خود را در درازمدت به‌صورت اقساطی پرداخت کنند.
🔹
اعتبار این کارت‌ها براساس سابقه بانکی افراد و بدون سقف تعیین خواهد شد و سودی به آن تعلق نمی‌گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/farsna/438752" target="_blank">📅 11:20 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438751">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FY9p6CfWyS2gE-cI-AQ1lpwMw8yXZxakqA8HYGfISAsm0fZfiJ_1wcEF-o_suSnxh88mnyPlAPaEBnCDY5QOfo0FTssYBFxO5aO6CuVdQj9YxqtOEjOlBWO9GieNPGx5aQZaLKevrN8G1i5I2qhd40fWEFzdg8C14FJ4twzo1YKadsQOmJ6Kb66eOa2xqufL6W3TS1ucwCZozmzIMtm6qsMCaPyw3KeSDTDrvoLEJgkscS1Jz7TDfEB4xMaM9Dapt4y0aetYLwGIvjdjPtDKkrkQ5LkH8GCx6H8h5lKazq-5ZmxGVmL9ylyXRLz4FkzONcUeqxBWeXG2GrCYYD2TfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان جای خالی امارات را برای ایران پر کرد
🔹
پاکستان با کاهش تعرفه‌های بندر گوادر خود و پذیرش اولین کشتی تغییر مسیرداده ایران، تلاش دارد انحصار امارات بر ترانزیت ایران را برای همیشه بشکند.
🔹
این تصمیم درحالی عملی می‌شود که مسیرهای مرسوم واردات و صادرات ایران…</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/farsna/438751" target="_blank">📅 11:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438750">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5746a288c.mp4?token=uCoJfx9_9JAcCJ_dwXY_ohbFDfEtSa1XRdb8UIypDSnKlbd9LM7LUth4zRabh6hVJJi3SwEY6A9YJZcfq2HfhiFHd-SiyBNmSXRFA3Xr_sqDLZKfUp_vEjjQP3D37f2VvrDWGheIa505xS18VIGdf76BLvSyrZ-20rc2UMJOKKvYVAwG7tUU3Vn04IoJ5J5Id7VngPazjMrT1uLfTJbn6t-i86SSm1QD5o_R2kGGSBw2xKzKASE_1uVwQWUtXd0ZL_QNsjnspmoa6-28nAkBAZQ0WO0XITvM0mSIT8USOu5Xcl7cbaROhVrUgpr45BMMJrzcnav60c-hbTgpvfdKtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5746a288c.mp4?token=uCoJfx9_9JAcCJ_dwXY_ohbFDfEtSa1XRdb8UIypDSnKlbd9LM7LUth4zRabh6hVJJi3SwEY6A9YJZcfq2HfhiFHd-SiyBNmSXRFA3Xr_sqDLZKfUp_vEjjQP3D37f2VvrDWGheIa505xS18VIGdf76BLvSyrZ-20rc2UMJOKKvYVAwG7tUU3Vn04IoJ5J5Id7VngPazjMrT1uLfTJbn6t-i86SSm1QD5o_R2kGGSBw2xKzKASE_1uVwQWUtXd0ZL_QNsjnspmoa6-28nAkBAZQ0WO0XITvM0mSIT8USOu5Xcl7cbaROhVrUgpr45BMMJrzcnav60c-hbTgpvfdKtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روضه‌خوانی محمود کریمی در منزل مادر شهید مجید سیب‌سرخی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/farsna/438750" target="_blank">📅 10:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438749">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUyEsvYYJ5j52BveoZ6vlp53CUpqfc_TD1xlCSE_uaqt3HvhyQKxQTdWwKCLKERiqMFN5KVwL5QmtoqPHcEGpqoYmncFzHlSjv3Jzsiecx8bTsvbDkWqsgIo5e_IH91G0eoOQPsyoMOjkUzEpfkVDmsVX__gOjwkS9tlmyz1_XRVTWlehShmj6-H5bkH2GGIjYetHKhpnt3TEltokjntg-XwpMATIqpFPbCAOMU3gzjjci_R5B5PXPZVhNaJTcFYAlRMtpkYwACjwhAZzc9i_kCMOrf4Whme9pUwlL_fM15fEwfGn4tigDxtSGW2xRnRRYmq5qT5ZMnyNi6Ml1ACog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهلت ثبت‌نام کنکور تمدید نمی‌شود
🔹
مشاور رئیس سازمان سنجش: مهلت نام‌نویسی کنکور امشب به پایان می‌رسد و این مهلت تمدید نمی‌شود.
🔹
داوطلبان برای ثبت‌نام باید تا پایان امروز به سایت سازمان سنجش مراجعه کنند و ثبت‌نام خود را انجام دهند. @Farsna - Link</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/farsna/438749" target="_blank">📅 10:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438747">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">زمان ثبت‌نام و برگزاری آزمون‌های دکتری و ارشد
🔹
سازمان سنجش: ثبت‌نام داوطلبان برای آزمون کارشناسی ارشد از ۱۶ آذر آغاز و تا ۲۲ آذر ادامه دارد. آزمون ۱۶ و ۱۷ اردیبهشت برگزار می‌شود.
🔹
ثبت‌نام داوطلبان برای شرکت در آزمون دکتری نیز از ۳ آبان آغاز و تا ۹ آبان ادامه…</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/farsna/438747" target="_blank">📅 10:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438740">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QmE8MogJ0SWuHZKysj0XhyhF-hCUss7Y-VrCzF__rwwTtxYPN878Ce2Yl0y7nMWKB_80MFB8w3VmfaxiTvy0QSVXmo4u3XeMSLqYNOhBQHhkOrISTtqDYVMoPME2FtjmsOCKFuqiRzW-9JdjaUxFSOzJclbGJ9eYU97H1lHJIcCWGT1O-wmX2bmIK8gA5JxywCG5IfgXKiPdf_1Dxc_vLrauYZ_obkTMnMuasVHfM_ulJJj3q9-CnxEfq2Lo0TX2vbvxVIm3g7a2WRC30iVOBthdZNcoMtfem5G6AS7FUBi-79niLI6ZRud8FfQU_aN3Xci1M1rIlKl_34lnK4sQAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/agChAWKKIUWUEGi1-_7pOGCnUKGhyFUyyI2OyvM5rqsJTYwR_P2gVlIneJxYUsaPCHIXGuJP9CfFEVehdC1mo64d37gX_UnpM4veSUKC2RXZDz1FLnb5RXNCqSn7R6eRBFRoNWcSr9hHBiwPjd3BtBqKmVWzKhdTK2GF5OlV76IwBFdz4Dp86T2zb76LcwVWaSS2U80xnGjHsUWmQ3mgN0KvxjAyMCXt8-b4NGjkuQDoylFFsoiPBzGKKIyTkDirQxHoQ0syKcGCbpL2L_zXLN0iFBtQrz83Hx7nyMlA2So3u7jg2Yj4p4rUTwS_VYeizgBihGjMvzCSWD-A6b3TKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jqdf2FirN11xaJQHQqJj7LeEfG9hpzDNcO8B03PlRS0Buq1YSdVdDzBoZMfNv9m85z2GhpaObFVwfPz5hE54L-rxVSw5DsB8ymRg0qNLfLSjXyMYqJEo89S9MnL0NLTw7oK6V4AGDGKAtHeRKHnvb7oIcIBWddlb-2TCyjIvKF51MTHqof_fXmia5c2xSHSfSeGvg4S-LNFjDgEqdVJLeOKHO9SVt9ZJoJNW0RnZpUat-wO5KJ8CsQmOWNqdjI3xR7KvFxknNSk-x3QvKnCTqAGOODn_PR7ctQU58AheMJRT4nmTODwgicyM7kEFqKuZ15Fo5p5UA9QLEzBeN9lPOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/riIDh9-8x8buivv9g9fGxh-JpZ_MI_xdbqLwVQsqsOcP7l8psv1YCQSec1yBy94m2HLKJmksYkzR5kl5HF-EGmOIQmUd11gzUPfN64hO2i2wedsEbmw_ERdBflwUQBhbm6K2lGfyuQB3DbFr0M8I5tr6lSYs-hu_AUKlkSuF3YIUHQHA_Y7FtJeEc9mWME3Ir8oYCyFATz8v9MWOwZa2kVlSO7enaZ3X01ppWWtxZodkCdF0_nVITP87w0gW_DSSsoMNE39AjDOTtLzdy2uTF-58TV6Vl2kbthNVKsduzGj39Tp5g4jj4fcW5LG2s-KKQcxj1VhP8BmldvXYJIcgqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WqKBEWcCGNU4H3vIKIXGSXvKTS13z3Sd3MM5F24PUV-ERJ5odWvnL3SDeTOEjkGhd-0zHcGkoSKKHm35q3SUBqMwfcDWQJAWl9Hy5rJNZr0IhCHi-EJAziaBaImXk6TUIoE5Vond2a8VQSY99pDxDjtv9O-dMR_uxODQpn10CCOiI4Cw_SHGWLxvQg7vScd7iydO9tMiK06CF-NZXAo9hHKFYBLRyQLqGgw87mGzlsZyoC7L2n8lzO69Cp08MazO2LlxbtTW2f9tgtbXcCOZOIY1tj2Q-sQ6h-YH61KxuxAQhNb8-xDVGZTxRkQh_FzS-oPd2Vwtfs04Wx76gicqCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GapsgjkoYvN5WJb-GZqVf0Br_cFW-zAv0hjJv4dXXSuDv8HV_6jb3w7cXQpXShzLnzRIvtDwH5_XHBnbLuWi_uZPbuiwfXD3k3KDU6yjGZeKv-molymknp2sP6HfITcCRGZcXNZwPYV5rp2hsQ8Dnaugh-WEdCPNiAX0NWcwU5qGuo_zyuZwZ2LumlcXsfzs_9Ww8FiqrRLf7gtZu_1jlcqMK8D3Xc2L8xB1B2oNaACbF0lJxyKvvX4gY9k_1wkilHLW8A7x_NEDDQV03sKICdLJO8lp8jTLzvkp9sKjYi30VuXnzz4p4iLtT2OcNgoGH-qIiCI5flxsnRvn6DvTgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tLcldDvp1T22nhKdTaYsy03n_yghhI1ypH8TX5A2iwMdeykRAGHQdyk4tko-pwUhTKC7knpp0VDYqGhRkjLj1mA6-WzyQaUwJXXTrfP-yyuRWsKJ-vegKMtxKe7s5QJ4vzL0dxZjzBKaTtKu2LW207mR2sOIfmX_bEVIh7l5LlfLALpY7P-2E2niWl9XMhKYA_7VkOpcmUcZhmkVIJVhd7cvYooBKht_CUTiK26rAMcm3_qzS3rvlLJc8D2Yal_b9DO9izzhDSNb86kRQlGIjxuIQq6XewPmyZ3KqwXiM1-h2jQRadwqwG_xG_E_c1PSZ0cmHhEOKW8Z2r96AA2P-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نبض توسعه در جوار حرم سیدالشهدا(ع)
🔹
پروژهٔ عظیم صحن حضرت زینب(س) در جوار حرم امام حسین(ع) با تلاش شبانه‌روزی کارگران و مهندسان، از جمله معماران ایرانی، درحال پیشروی است؛ طرحی بزرگ در توسعهٔ عتبات‌عالیات که در آینده میزبان میلیون‌ها زائر خواهد بود.
عکس:
امیرحسین ‌رستم‌زاده
@Farsna</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/farsna/438740" target="_blank">📅 10:31 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438739">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">احتمال شنیدن صدای انفجار کنترل‌شده در اصفهان
🔹
سپاه اصفهان: به‌دلیل انجام انفجارهای کنترل‌شده تا ساعت ۱۴ امروز در جنوب اصفهان، احتمال شنیدن صدای انفجار در این منطقه وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/farsna/438739" target="_blank">📅 10:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438738">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lirSboOxXpLt5lm3mX-rzZ3kRTkp_Lsq9pIsCHDiElv53IlhEMaPfPcZwG472yuWTKhU1xiUF52HoOAX80yiQsrSjPhT1_VJ3mgC2FGFRtLE7py_zIyBoQaWS5AmQensE5_2zGuhkco9t7RyGNksrEzMtIvuX_bovgseQ-K0fftO2lwRk7Hqg4PoQvZJhKO8DnplVFO8wWsTJuinEZ5TzfwbQXURnH7MeMauZKJ_ZbBbP-yec-hstaqQ-oPyzVytapz7vh9G9DJBfixCG_fyd99QSUwVxjWCGbuksA-RT4TbyTZk5aSHNl-m4stvrcn7NxlqKuGaTrIvd-rpgvY2IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سپاه یک پایگاه هوایی آمریکایی را هدف قرار داد
🔹
سپاه پاسداران: به‌دنبال تعرض سحرگاه امروز ارتش متجاوز آمریکا به نقطه‌ای در حاشیۀ فرودگاه بندرعباس با پرتابه‌های هوایی، پایگاه هوایی آمریکایی به عنوان مبدأ تجاوز، در ساعت ۴:۵۰ دقیقه هدف قرار گرفت.
🔹
این پاسخ…</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/farsna/438738" target="_blank">📅 10:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438737">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bf7dd4b5a.mp4?token=vtgtSWsk9e-U2me3ae1r1JIm9I8zeTyKX-EMQo4MGxlecpysjL6g-rOAsca6suBu4BogPDVbUL1WDT9XyhmpyOnxLiZ0cN02g6opsSiTOcxuxqoEyAM71kGIaYhGe5lmZjY8OGAxYYtGXe4CXoMsS6H8zxcd0Ft6HyQSPnAfr4mMAgadsBkO8lXls66TT5aeJiefrApQ42PmpRb0iCDI7yea5yP0nAYcwLXu9-yG-w7OOEIfVErQEwzLsk1sdk9XKtSMkY9VQLueoHiMNWRJv0rCDzt_jkJZRD2tkcQTGVwfrAM8VpZX3NZtOE6790yxwxT1aKe28zz-vBMrZTIj5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bf7dd4b5a.mp4?token=vtgtSWsk9e-U2me3ae1r1JIm9I8zeTyKX-EMQo4MGxlecpysjL6g-rOAsca6suBu4BogPDVbUL1WDT9XyhmpyOnxLiZ0cN02g6opsSiTOcxuxqoEyAM71kGIaYhGe5lmZjY8OGAxYYtGXe4CXoMsS6H8zxcd0Ft6HyQSPnAfr4mMAgadsBkO8lXls66TT5aeJiefrApQ42PmpRb0iCDI7yea5yP0nAYcwLXu9-yG-w7OOEIfVErQEwzLsk1sdk9XKtSMkY9VQLueoHiMNWRJv0rCDzt_jkJZRD2tkcQTGVwfrAM8VpZX3NZtOE6790yxwxT1aKe28zz-vBMrZTIj5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرمانده نیروی زمینی سپاه: شهید پاکپور معمار امنیت پایدار بود و شبانه‌روزی برای امنیت مردم تلاش می‌کرد.  @Farsna</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/farsna/438737" target="_blank">📅 09:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438736">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtgfpJRDBDiANDv9o3EBakybGuZqVd5Ld5bLRFdgum5Q9eV51vxke3kYW4NctkZJ3qyJGgUN4t4hWn1D9tX7yVeOdmy2A5q-w0xA0YUvTmMtkV9m2qJ1jfCMF5nDi72XJosS2EqkuzgNDP-EliCKLuoTsGYM5647XR10sZ6X2_mf6YNKA_cKWpPZtR4vOYpUlW6tn8XCOOhwRHQeaFSO8flIt3C-mrjWJX-P0ucg8qVNUF-odmx_Vet2ebL5Zym0WCiz4vdhJDmsR7u8CZ6q3OV5aJcZZOmmOJJh2Q3imc0YR10ND5kd4DMItLyrV5Ki04Q55dzt1qvWVNpxWqnliw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هدیه ویژه کاپیتان پرسپولیس به مجروح مدرسه میناب
🔹
محمد شرفی از دانش‌آموزان مدرسه میناب در جریان حمله به این مدرسه دچار سوختگی و جراحات شدید شد. این دانش‌آموز در این واقعه، خواهر خود که از محصلان همان مدرسه بود و همچنین خاله‌اش را که به‌عنوان معلم فعالیت می‌کرد،…</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/farsna/438736" target="_blank">📅 09:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438735">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNWlFYztNYiTrBkdE2q9ORDbV_eXsoRiG_FDGGgdN0aA8cnjXOy8YFM_exLdbkugz7KKuG0fBdSUzoIWHrYR7e58x1R42Cs0Hi7krsgApb3Pq_ggNWjBL7aZM3nrljd_5qsaeCsiQNt0VpvKUUHwhyZNWZdDpfVHLapBNKFqY5Dv5NxQJwnQu-j-fuosqmJOCuTS131PNNa6qR7vF5uwzy2KqCA-mLHCL0vnfMGmfxO8d-J5z0gOXSCTaHjW-qxpVH6M6n_lq-ATVOy0CkWwnP1ctcL0hwReUy-2Dyrki4gesUfi48erTOjopsPRRy0vgAG8HNtQtWyVUWqBVaaI-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادامهٔ تلفات خاموش تنها پستاندار دریای خزر
🔹
در روند پایش‌های ساحلی مازندران مأموران یگان حفاظت محیط‌زیست ۴ لاشهٔ فوک خزری را در محدودهٔ بابلسر و میانکاله پیدا کردند.
🔹
طی ماه‌های قبل شاهد روند افزایشی لاشهٔ فک‌های خزری در سواحل دریای خزر بودیم که مدتی متوقف شد و این روزها باز هم شاهد افزایش لاشهٔ فک‌ها در سواحل دریای خزر هستیم.
🔹
فک خزری جز گونه‌های در معرض انقراض است که در فهرست سرخ اتحادیهٔ جهانی حفاظت از طبیعت ثبت شده.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/farsna/438735" target="_blank">📅 09:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438734">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfdWaIulayzOGRNQ6Wruv4MzTlmHHCR32X56gFVYTpBJYIME5kfNJ0Zo7AWIlasjj5SQzoi6RNIk8lEvHhDPYUmYreS_IusFsd_lXG-wspHiYldPqyUHgS9kJipfBON6DBMNEec5i82yd-zPPZnTvTlDzn6BpUV16dWUcPZ6Zaz5VZ0_A9R-Pti6S2zCyoXImYNbJOdV2gHto6o1D2vkyIjUtBWEXRVt0G89OUJaq7sI81BukIABx2-h0I9To4n3422OfddkVlBQgzagwxaxtGrwHrb1zYEyEwDXAG5mGn2c2kfzmEgyRLWOC4PwdaslTNRoRGtrei__ab2zoTn-MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعمیرات نیروگاه‌ها، پاشنه‌آشیل خاموشی‌ها
🔹
تا ۹ خرداد امسال پروژهٔ تعمیرات نیروگاهی برای تابستان ۱۴۰۵، ۹۷ درصد پیشرفت دارد.
🔹
تعمیرات نیروگاهی طبق رویهٔ سال‌های گذشته باید نهایتاً تا ۱۵ اردیبهشت هر سال به اتمام برسد.
🔹
کل تعمیرات نیروگاهی در بخش واحدهای حرارتی ۱۰۵ هزار مگاوات است و هم‌اکنون بیش از ۳ هزار مگاوات از واحدهای نیروگاهی به‌دلیل تأخیر در پروژهٔ تعمیرات در دسترس شبکه برای تولید برق نیستند.
🔹
میزان ناترازی برق در خردادماه و پس از شروع گرمای هوا حدود ۲ هزار مگاوات است، رقمی که به‌اذعان کارشناسان در صورت تعمیر به‌هنگام نیروگاه‌ها در این برههٔ زمانی به صفر می‌رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/farsna/438734" target="_blank">📅 09:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438733">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">۲۲ عملیات حزب‌الله علیه ارتش رژیم‌صهیونیستی در جنوب لبنان
🔹
حزب‌الله: نیروهای مقاومت اسلامی در ۲۴ ساعت گذشته در پاسخ به نقض آتش‌بس از سوی اسرائیل، حملات به غیرنظامیان و تخریب خانه‌ها و روستاهای جنوب لبنان، ۲۲ عملیات نظامی علیه مواضع و تجهیزات ارتش اسرائیل…</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/farsna/438733" target="_blank">📅 08:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438732">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8cf218009.mp4?token=VOgimyJUxHoEiJSWFHeVPOKfvC2rpxpOqqU966wmvjV_mJJdyLW5c53CSWQL0DNiWQM86vzDYFyltd1b7J9UPDp0WyPR5cQoIKgs3jujYb7YHyhWT1s0PPz5RlwmKsd19MCkhbkP5ctYj-jQ8kvwpUCBVsuU_2eqQ07aXlfBr4VFAA0f63C99JAhloUddyFXM7D7MnPW-MIwJg40v7-2HgopdZMReznDPBBc3_5q0cbLqANPVLrKVCzI1kaRroR4QsyLUZAf3zJG_sJiCryNg0TQd8QOL3XpR8XPPpAy8xQON5r29ROd7dkcReYcVLXenP9HNM0s_evbYH0h01FzEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8cf218009.mp4?token=VOgimyJUxHoEiJSWFHeVPOKfvC2rpxpOqqU966wmvjV_mJJdyLW5c53CSWQL0DNiWQM86vzDYFyltd1b7J9UPDp0WyPR5cQoIKgs3jujYb7YHyhWT1s0PPz5RlwmKsd19MCkhbkP5ctYj-jQ8kvwpUCBVsuU_2eqQ07aXlfBr4VFAA0f63C99JAhloUddyFXM7D7MnPW-MIwJg40v7-2HgopdZMReznDPBBc3_5q0cbLqANPVLrKVCzI1kaRroR4QsyLUZAf3zJG_sJiCryNg0TQd8QOL3XpR8XPPpAy8xQON5r29ROd7dkcReYcVLXenP9HNM0s_evbYH0h01FzEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: از پارک کردن خودروها اطراف درختان فرسوده خودداری کنید.
@Farsna</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/farsna/438732" target="_blank">📅 08:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438731">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aded35a14b.mp4?token=Xqpd0OLtcfcea_iCvdUrXbq2zY-u2cJ-vSdg_F-_nsZpYPBOKmn55H_w7-ZjtuZslwKK90fe4uhal4H67-R5FMxnlFveJ4Gu_obdhfT6WJQsH3HrJ3Ml7DuXKAgQFXpc6bDaHWysGUotPw9krFyfVLUk_eU4gw2OIwSPcc2-r3xUawNbIpnUPq1dw0hc8tLKvrGH8UTYFX7FNjh8BKVnvX2xc0LFzYNIww9i7N8dJuhmb_2smEJOeoGxTAuLDPpFg5AZNWdaDcGTSSkZ2e-LEPOQ8z_idPtxsNd4LSuLXe-flBCQRlqi8e087oT-s4OBE-nU3DLvu0n70qNbs9T1y3psmNVN4OcSLigdSA5lAu2KXgQ8sR2j-QgBRpNr3UUXefKduM86Pty8LqjnNv436xRMJZQReTI8rQCNzEOofBU3w4YcOBXd6EpGGcXSuSx3pWjfxyUer-NU6u2yRsrOu67soUj8naBewEVrLlrzSFuyIm4gI_jGloXUg6TMYV_VyeSG8Gs6RoDC6LQtrZ5AQc29XfAlVRlgKVXJx9FMywDyhVTatNdV7vFzJMEzQ4ijfpEBMtZAWXmzQeH85KCMTPBnAw_-927Px_068KGMhTeFEMKuvx0d-MTbz-OixVg_wjqtuwqrRBexk9VVHXF8tBIFhG5U_U5lYES9GTef6sM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aded35a14b.mp4?token=Xqpd0OLtcfcea_iCvdUrXbq2zY-u2cJ-vSdg_F-_nsZpYPBOKmn55H_w7-ZjtuZslwKK90fe4uhal4H67-R5FMxnlFveJ4Gu_obdhfT6WJQsH3HrJ3Ml7DuXKAgQFXpc6bDaHWysGUotPw9krFyfVLUk_eU4gw2OIwSPcc2-r3xUawNbIpnUPq1dw0hc8tLKvrGH8UTYFX7FNjh8BKVnvX2xc0LFzYNIww9i7N8dJuhmb_2smEJOeoGxTAuLDPpFg5AZNWdaDcGTSSkZ2e-LEPOQ8z_idPtxsNd4LSuLXe-flBCQRlqi8e087oT-s4OBE-nU3DLvu0n70qNbs9T1y3psmNVN4OcSLigdSA5lAu2KXgQ8sR2j-QgBRpNr3UUXefKduM86Pty8LqjnNv436xRMJZQReTI8rQCNzEOofBU3w4YcOBXd6EpGGcXSuSx3pWjfxyUer-NU6u2yRsrOu67soUj8naBewEVrLlrzSFuyIm4gI_jGloXUg6TMYV_VyeSG8Gs6RoDC6LQtrZ5AQc29XfAlVRlgKVXJx9FMywDyhVTatNdV7vFzJMEzQ4ijfpEBMtZAWXmzQeH85KCMTPBnAw_-927Px_068KGMhTeFEMKuvx0d-MTbz-OixVg_wjqtuwqrRBexk9VVHXF8tBIFhG5U_U5lYES9GTef6sM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۹۰ شب است که مردم بی‌آنکه قدمی عقب بنشینند، ایستاده‌‎اند
@Farsna</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/farsna/438731" target="_blank">📅 08:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438730">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44a5ea9dfd.mp4?token=tMZDTpm2fE8FJ-M0sFWFNU80OuYORljsBNR_yGlAR9Tt8mz-vGg2_6oTsXzxA_ddahmo-FNoYeXjr2Z3yftezrc6qZiYebLQszO2hdnXsOu0QLvGAKrGauOw-j3D-ZBEEnS46UKvkfkqSBbTOwBzbBfYMvtt0sN4AFPUSQ2Eklmp6YrlmY6bSdAnIdHzeFBhZDToDmrHrzLN8sJaPt4AV_GdZFY6E3W7N2JsIaUsFYhfai-1Tn8-mRHRh5sf3bwhEFd6EcDSGzAq0MU52tTuV1BkcbERA9UBRUDx50pX2kuus6jZoWkRVq3SVBAvhUSXsQAWEfWfNDCZC-o26yV4xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44a5ea9dfd.mp4?token=tMZDTpm2fE8FJ-M0sFWFNU80OuYORljsBNR_yGlAR9Tt8mz-vGg2_6oTsXzxA_ddahmo-FNoYeXjr2Z3yftezrc6qZiYebLQszO2hdnXsOu0QLvGAKrGauOw-j3D-ZBEEnS46UKvkfkqSBbTOwBzbBfYMvtt0sN4AFPUSQ2Eklmp6YrlmY6bSdAnIdHzeFBhZDToDmrHrzLN8sJaPt4AV_GdZFY6E3W7N2JsIaUsFYhfai-1Tn8-mRHRh5sf3bwhEFd6EcDSGzAq0MU52tTuV1BkcbERA9UBRUDx50pX2kuus6jZoWkRVq3SVBAvhUSXsQAWEfWfNDCZC-o26yV4xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حمله مرگبار آمریکا به یک قایق دیگر در اقیانوس آرام
🔹
ارتش آمریکا در ادامه حملات مرگبار خود به قایق‌ها در اقیانوس آرام به بهانه مبارزه با کارتل‌های مواد مخدر، به یک قایق در شرق اقیانوس آرام حمله کرد و سه نفر کشته شدند.
🔹
در بیانیه فرماندهی جنوبی آمریکا در خصوص این عملیات آمده است «در تاریخ ۲۹ مه، به دستور ژنرال فرانسیس ال. داناون، فرمانده فرماندهی جنوبی ایالات متحده، کارگروه مشترک "نیزه جنوبی" یک حمله تهاجمی مرگبار را علیه یک شناور تحت کنترل سازمان‌های تروریستی تعیین‌شده انجام داد».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/farsna/438730" target="_blank">📅 08:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438729">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83c176406e.mp4?token=DuWtrQcS2ObzcuQNW0_A9B_FUW412TifsTMnum106brhLUyzgWO4K7NEa91n-0U8iIkKGLsA6vg9bjU3cmCP6llk65L-nlcfddC2elEHvRZg1ID0Z6Tbt-w8q2xkAJI1XwLDwfMZSOAX2J_Yh8wjI3Qm7Spj1r3GlMJRogJMYaMRQ0zPKYYjLlkPC8nfSr02ffRdbGJhVxbNVd1AzIocL_8kHDZdpIhdzhTEOciQyjW6tkUwUkSt82xA49S8FXbZPA4f1btDf30f20CNjs41pt60v0ig35PCeNgBFD7dj2rBOr5ptOxkdm58Jf8h0klQvzXOEHNCIlEnxUq1yko-9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83c176406e.mp4?token=DuWtrQcS2ObzcuQNW0_A9B_FUW412TifsTMnum106brhLUyzgWO4K7NEa91n-0U8iIkKGLsA6vg9bjU3cmCP6llk65L-nlcfddC2elEHvRZg1ID0Z6Tbt-w8q2xkAJI1XwLDwfMZSOAX2J_Yh8wjI3Qm7Spj1r3GlMJRogJMYaMRQ0zPKYYjLlkPC8nfSr02ffRdbGJhVxbNVd1AzIocL_8kHDZdpIhdzhTEOciQyjW6tkUwUkSt82xA49S8FXbZPA4f1btDf30f20CNjs41pt60v0ig35PCeNgBFD7dj2rBOr5ptOxkdm58Jf8h0klQvzXOEHNCIlEnxUq1yko-9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فراجا: زائران اربعین گذرنامه‌های زیر ۶ ماه را تعویض کنند
🔹
امکان تمدید گذرنامه به‌صورت حضوری و غیرحضوری فراهم است.
@Farsna</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/438729" target="_blank">📅 08:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438728">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">آغاز امتحانات دانش‌آموزان از امروز؛ اکثر امتحانات مجازی است
🔹
رئیس مرکز ارزشیابی آموزش‌وپرورش: سال تحصیلی امسال به‌جای ۲۹ اردیبهشت، تا ۷ خرداد ادامه یافت و از امروز ۹ خرداد، امتحانات پایه‌های اول تا دهم آغاز می‌شود.
🔹
امتحانات دورۀ ابتدایی غیرحضوری است و بر اساس ارزشیابی تکوینی و تشخیص معلم انجام می‌شود.
🔹
امتحانات پایه‌های هفتم تا دهم به استان‌ها تفویض اختیار شده و اکثر امتحانات مجازی برگزار می‌شود.
🔸
امتحانات نهایی پایه‌های یازدهم و دوازدهم از ۲۱ تیر، به‌شرط عادی‌شدن وضعیت با اعلام مراجع ذی‌صلاح، به صورت حضوری آغاز می‌شود و احتمالاً تا چند روز آینده برنامۀ امتحانی این پایه‌ها نیز اعلام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farsna/438728" target="_blank">📅 07:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438727">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">رگبار باران و وزش‌باد شدید در ۹ استان نوار شمالی کشور
🔹
هواشناسی: امروز شنبه در استان‌های آذربایجان‌شرقی، آذربایجان‌غربی، اردبیل، گیلان، مازندران، شمال کردستان، ارتفاعات قزوین، البرز و تهران افزایش ابر، رگبار باران، رعد‌وبرق و وزش‌باد شدید پیش‌بینی می‌شود.
🔸
امروز آسمان تهران صاف تا کمی ابری همراه با وزش باد، در برخی ساعت‌ها بادشدید، همراه با احتمال گردوخاک است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/438727" target="_blank">📅 07:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438726">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtXzvIi03sX1VmjjnXz9XFoOwg-dkjKO2Dc41fRgjdpZSJE9_f3T8JjBV1QI63UEgRdb5EP_3u0i84oYlCLn8vyW7MzZZe0xVOj66nM5jxn872Q0-ELWmjjtP4TnwvakgpbMwAeF_F2MdasLS8FQBEQT0bTRcDLt-uXyZhkbovaOt291NLnGXVA1M05h6MGDMUzHfUiYBg5gGMyylYWpCHJ2hNmTmEpM13p2Xvcm81k1-j__UKwRsZy_TmEBkXxTXtzJeLIqT1CAbRoKobbTrbhAeJputIczfhBcMwN9a0j9GkaRYM4G2-CMko4wFgSi5pNOZBt5fOLXUd8tyFM1NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدارس سنگی و کانکسی جمع شد
🔹
وزیر آموزش‌وپرورش: حدود ۱۷۰۰ مدرسۀ کانکسی و حدود هزار مدرسۀ سنگی وجود داشت، که اکثر این مدارس جمع‌آوری شده‌ و می‌توان گفت کار جمع‌آوری مدارس سنگی و کانکسی به اتمام رسیده‌ است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farsna/438726" target="_blank">📅 07:20 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438725">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-2ydkR2OGft2W903badJ4Jo1GTUZEtIGmiEOT5H6_fDKLGbz5Qherf2HuilKah9IkSvzpKpg2z4kowUtKBgUQ3CRrgcZygvhASSf_DSmRzxTSDG9me0nSO1cEv5ZvpyA_H70OJ4IUNGOP-mrr5jI2Q48UMxlG0kGNjMgN_jOj8Cvk_kE0zP9er_erwuWFS22bjgXW6mFQZWJcb5sdinFIRI5wc-5E5hP-QCT-vs0fbQ2FttJ-xQ4Ez3BXjF0lYWn1lP63Ip9H6ct7-QpRjgwPi20sXbWHRubgRcJZOb9TEpsqNz_IhRQnzo5cdNopvjllqr5czZmYkHRptgSsYvkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیر استقلال در آستانۀ جدایی
🔹
مجتبی فریدونی بیش از ۳ ماه است که به‌دلیل اختلاف‌نظر با علی تاجرنیا، در جلسات هیئت‌مدیرۀ استقلال حضور پیدا نکرده، به‌نظر می‌رسد در این مورد قصد کوتاه آمدن ندارد.
🔹
طبق آخرین پیگیری‌ها، فریدونی با وجود غیبت در جلسات هیئت‌مدیره هنوز از سمت خود استعفا نداده اما اکنون احتمال جدایی او از جمع مدیران استقلال پررنگ‌تر از همیشه است.
🔸
هلدینگ خلیج فارس هنوز واکنش رسمی به غیبت‌های فریدونی در جلسات هیئت‌مدیره نداشته‌ اما به‌نظر می‌رسد به‌زودی جدایی او از جمع مدیران استقلال علنی شود‌.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/438725" target="_blank">📅 04:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438724">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🎥
کرمانی‌ها در نودمین شب حماسۀ حضور
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/438724" target="_blank">📅 03:54 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438723">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPd51HbprXqr462Ch7ZfPAf10VbBmWAjayTPkQS09UoC-uDlAmuq-zdzOpQowBal61CM9G_LUesBm-pIJei22fj3zu_j-MbKM27jLnGJtLi0DHXqqrFHpxUiE2DC4bGy0UD_FbZZQspNwKoO0l1vssCPFd5kvvdSiR5t7yVaYjB4YQmq15VeFffYGmRv6s8GCRdLbT6FCm3a72YVWoE0j38aQfHrZ0tPE2hqsUl5P6sinHvWbKgsGxVw06CE3G4tUjt1wb3o8z9q1iBHI__SZ9Fhx5vL8XFxjfI04rdphOX-d9MdpHeGzyySObXSJcWuWps9imFMGLtPQIJWZ4QuCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحریم‌های آمریکا علیه یک شبکۀ موهوم مرتبط با ایران
🔹
وزارت خارجۀ آمریکا که این روزها باردیگر دست به تحریم شده، این‌بار به سراغ یک شبکۀ ادعایی و موهوم رفته است.
🔹
این وزارت‌خانه اعلام کرد تحریم‌های جدیدی را علیه یک شبکۀ ایرانی اعمال کرده که به ادعای واشنگتن، با استفاده از روش‌های فریبکارانه، شرکت‌های آمریکایی را هدف قرار داده و برای دستیابی به فناوری‌های حساس به سود وزارت دفاع ایران فعالیت می‌کرده است.
🔹
وزارت خارجۀ آمریکا از اختصاص جایزه‌ای تا سقف ۱۵ میلیون دلار برای اطلاعاتی که به مختل شدن این شبکه منجر شود، خبر داده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/438723" target="_blank">📅 03:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438722">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a761d6e0d5.mp4?token=gBGgqmIbpQcyExr9HoX1twhqHec8MNLD5MNp0gbOP9LENJ7l7OCtkS1hYbBYmT7cdEhE1FH8Q_1mjQH_b7Pz4AYM67IINjc4dgRFiLXm3VYh413p_PY4JnAjhmwlukBwZxU_r8AVpAR4uSyTyF6I1HgQeUzNCkdfZk1X4FGE3ZNuPN1mfP3GV9p7zg4xTgXqY-e6WKsN_wURnzD3h3uMxPH7v6DMDd7ZERJoHFAxZzsmuQtgikUz3Dk-g9HzOGYRw6t0uCSEQfBTULY18dd996-REqghiD6QSjNvJTrZ7bwVZQxpCA6QPMeoL37v0ry4RsarE7DZPyKSJq4OVAazXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a761d6e0d5.mp4?token=gBGgqmIbpQcyExr9HoX1twhqHec8MNLD5MNp0gbOP9LENJ7l7OCtkS1hYbBYmT7cdEhE1FH8Q_1mjQH_b7Pz4AYM67IINjc4dgRFiLXm3VYh413p_PY4JnAjhmwlukBwZxU_r8AVpAR4uSyTyF6I1HgQeUzNCkdfZk1X4FGE3ZNuPN1mfP3GV9p7zg4xTgXqY-e6WKsN_wURnzD3h3uMxPH7v6DMDd7ZERJoHFAxZzsmuQtgikUz3Dk-g9HzOGYRw6t0uCSEQfBTULY18dd996-REqghiD6QSjNvJTrZ7bwVZQxpCA6QPMeoL37v0ry4RsarE7DZPyKSJq4OVAazXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نود شب اتحاد و حماسه در سرپل ذهاب
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/438722" target="_blank">📅 02:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438721">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">مقام کاخ سفید مدعی شد: توافقی که خطوط قرمز ترامپ رد کند، امضاء نخواهد شد
🔹
یک مقام کاخ سفید در گفت‌و‌گو با خبرنگار شبکۀ الجزیره مدعی شد: دونالد ترامپ هیچ توافقی را امضا نخواهد کرد مگر آنکه این توافق مطالبات آمریکا را تأمین کرده و با خطوط قرمز تعیین‌شده از سوی او همخوانی داشته باشد.
🔹
این مقام آمریکایی با تکرار مواضع طوطی‌وار و همیشگی، افزود: «واشنگتن هرگز اجازه نخواهد داد ایران به سلاح هسته‌ای دست پیدا کند».
🔹
به گفتۀ این مقام کاخ سفید، نشست «اتاق عملیات» در کاخ سفید دربارۀ ایران پس از حدود دو ساعت گفت‌وگو و بررسی به پایان رسیده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/438721" target="_blank">📅 02:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438720">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">۲۲ عملیات حزب‌الله علیه ارتش رژیم‌صهیونیستی در جنوب لبنان
🔹
حزب‌الله: نیروهای مقاومت اسلامی در ۲۴ ساعت گذشته در پاسخ به نقض آتش‌بس از سوی اسرائیل، حملات به غیرنظامیان و تخریب خانه‌ها و روستاهای جنوب لبنان، ۲۲ عملیات نظامی علیه مواضع و تجهیزات ارتش اسرائیل انجام داده‌اند.
🔸
طی عملیات‌هایی در جنوب لبنان و شمال فلسطین‌اشغالی، ۵ تانک مرکاوا هدف قرار گرفت که ۳ تانک با پهپادهای انتحاری «ابابیل»، یک تانک با موشک هدایت‌شونده و یک تانک دیگر با سلاح مناسب منهدم یا دچار آتش‌سوزی شدند.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/438720" target="_blank">📅 02:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438719">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47d3db0548.mp4?token=tqxtviWtcCDpcblbdMj5Yadk2Cjzrz0RWGYEMhGCT4pCsVdoKAfrnd9ccZmLt5ed8oWXJDrUrWzHm4H5cLKHWBQfOnfwCjFiL8_2DBEecuUYEK10dmoTkdTYpbXNCk0Xi7517RB-wElGVVNF55FE-PacHK7qXrSWX9cKFkuoHDPcpmqp3Tk9u17aT8NidKwbfOyqt-cYTdzy_MqmxvpwLBXJFwIhtgVVKulL3KJHZWY9sXIyY640LCF9fKE5xvMW7DSInL0G0coWhSRlWokf_303uVYtZGeenTFpHKdCCljNwk2eaxvVg2w5NDlQrcuXl1NcssenmeHLKx2U9f6OdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47d3db0548.mp4?token=tqxtviWtcCDpcblbdMj5Yadk2Cjzrz0RWGYEMhGCT4pCsVdoKAfrnd9ccZmLt5ed8oWXJDrUrWzHm4H5cLKHWBQfOnfwCjFiL8_2DBEecuUYEK10dmoTkdTYpbXNCk0Xi7517RB-wElGVVNF55FE-PacHK7qXrSWX9cKFkuoHDPcpmqp3Tk9u17aT8NidKwbfOyqt-cYTdzy_MqmxvpwLBXJFwIhtgVVKulL3KJHZWY9sXIyY640LCF9fKE5xvMW7DSInL0G0coWhSRlWokf_303uVYtZGeenTFpHKdCCljNwk2eaxvVg2w5NDlQrcuXl1NcssenmeHLKx2U9f6OdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک ریز پرنده در آسمان قشم ساقط شد
🔹
به گفته منبعی در پدافند هوایی جنوب شرق کشور، در پی فعالیت پدافند در جزیره قشم یک ریزپرنده مورد اصابت قرار گرفت.   @Farsna - Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/438719" target="_blank">📅 01:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438718">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">منبع لبنانی: مذاکرات لبنان با اسرائیل در واشنگتن به جایی نرسید
🔹
یک منبع رسمی لبنانی به شبکۀ المیادین اعلام کرد، هیئت نظامی مذاکره‌کنندۀ لبنان در نشست پنتاگون نتوانسته به خواستۀ خود برای برقراری آتش‌بس واقعی دست یابد.
🔹
به گفتۀ این منبع، هیئت نظامی لبنان در جریان مذاکرات بر ضرورت توقف آتش‌بس پافشاری کرده، اما با مخالفت مکرر طرف اسرائیلی روبه‌رو شده است.
🔹
این منبع همچنین افزود هیئت اسرائیلی با خروج از اراضی اشغالی لبنان مخالفت کرده و بر «خلع سلاح حزب‌الله» اصرار داشته است.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/438718" target="_blank">📅 01:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438717">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THYbMuSYXEW-Qrx9YZN5r-PdqYNBCrX8npcAiVKL259ShLH6Jz2SsUUkvhglHKSOm2HXe1EcurZTAi68a6bcV-8UfVagbtsrxw_aeBkYmBdNAWIzoQ0Ly5G-Q-2cOtSH84R3-m5IQxArWjE94AS-Ns-N79PndOBIIi1g_Cv2t-p-UyN_kOUiPu4OVi8TNHOF0OrLFZ1xL6Fdp3eYXJZXqLcZ_ZiqY-DXRZeMELTZIFdLznNhisadFu4GXK8u1MJADKfXAumS35RG3EciUXv1RV62cGUnh5gajueOwwx0z6EZMhIjSnWj4nq2hWj0rFHcF2mosHpN2Z_tloDUJOIo2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان: ابداً قرار نیست اسرائیل را به رسمیت بشناسیم
🔹
وزیر خارجۀ پاکستان: شایعات زیادی درمورد توافق ابراهیم در گردش است. بگذارید روشن کنم که موضع پاکستان در این زمینه بسیار روشن و ثابت بوده است.
🔹
تا زمانی که فلسطین با الگوی پیش از ۱۹۶۷ به‌رسمیت شناخته نشود و قدس شریف پایتخت آن نگردد، هیچ انعطافی در این موضوع امکان‌پذیر نخواهد بود.
🔹
پاکستان به موضع دیرینۀ خود در قبال فلسطین و غزه متعهد است و هیچ تغییری در سیاست اسلام‌آباد نسبت به اسرائیل بدون برقراری یک کشور مستقل فلسطینی رخ نخواهد داد.
🔸
گفتنی است چند روز پیش ترامپ اعلام کرده بود که چندین کشور از جمله پاکستان، عربستان و قطر درخواست کرده‌اند به توافق ابراهیم بپیوندند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/438717" target="_blank">📅 01:13 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438712">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NZcAOBvzYyjWcYHEE4qByM7UDaN5sG4iSBV9aO5bo0cCwRhZZbwoPHc_4URCiuhrJ-BZkqWgW6Z01ZhBX3jw6p1xy0naMO2igwVB4bQYYXt5jVs8kA0DyiQ-k3Q8u6duaEmPm4142e2X5yrLokJNnvt7t9g1w77pI0oWRZBu_Hpafl32Di2FUCsTktVvcTmzfufvhpvzh9lDGZ68jmdYGWpCBncjlnbqK6FJCgRegGtv65HENCY3sHC83QA5_DEz_NcPgdOti2TYWFj9mCe4DPL7E_kBQln3S2EO3WODpK6lYst-DxVx1c-slEh6b5kBBu4BVaQiLOWyevWC6uiI-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gCk6gexFNb8c0XwYLBnX4X6xnHknGCwTo9xzqC2cqCsgRxvstnJUf63mW-7ZgH-ZeH4-9KZtjTabNrRwuvs5WkHBjDa9H367GlBkqzSeAug7oD7Pe5gsxzW0DOIpyxyXUDeQzuew3m-3-hQSUN6ZJa_ZLHa1zOG4YOWxWNFujLEzuXwKtjU487b3opiuM0Rqi11136v7_107RNtaxNdEhinorQP-S_7V-31QNKaCs62G6dY7mJ0rX8vTGu0qde078-QJpM3rcZiriZN4-EK7KGOX0NLetbGJwROHehGBB7X3THcTRdlgNHycfMoK_7fmHIquy_K7E07qdODAwafUPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dc3fNMwK1m5BV4hah8Ju1Pj5hOuZ51tKiBvj4KE8orlErEb5-MRmFMXaaAG71-eJ--e1W8i-yZFhHF37bhRAMxK666dBuln8DaNU1T-t4fE0ZFT6-o5Ngp2wyajcSpL1JohrAdgD-whKagaQ28FroSi5FYQ-6Rv03b-O6teytKX4ye9ACe8Axq4HxQW-tvWUTRbDDaA2xHbR4vejHcfBRtFQ3rnCrHserRL_sgG8mdD2S2LuGvMk53WHBTDh4ylPhbhjA9H-KrUeV5LaDMn85iAZDHvbDF-nsRy0ps6-s27M10UEWmhqXPYXX4CzYPQJBXglgo3AkNCqlgAV8KaEEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KUIHZkkjQd8uhD3DzgMEcsNb206rQHdm2xxeiQ1hnyU02_75dyHTvOcNlN6frHAwTJLkyZIE7pvHyVeJvIsNoxPLXJQZ_ZDytOZjDVCFmU4563t1g5CqeAECuhT_8kV3F51mT2ElngNXL9ZHF4DJHiAyh-hli9v2HLlIAVQv1ifNC51lOgDOTtRNf3mEucSZBnripUaa5w5ikoC6oKq1YrXJIvzAz-QebSp1XyVzR2Bl1qdBO_L0hDNK22Elu2No4avJt81g5DfHaeOgfVqnxv6jiRwtue-NDM9XCfDEy1lyAdPyjK74SUjaZFzqpvUP6jqR6v8zW55QDYwYjtulIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mp1cvCTcOY2UzeuSut2DClpUxd3DU3jDmVy7bSndfzk2LYmuQC1YVkQvB4xOyAVK5eolm1bz1Vewp8luZUHQ0I0dYefO-b6TWyrVE1dkp4ylkZ6CDW3N8fcGRQKafGqRvT40EMCOYJJP17Llu1HS1-IHNFdJ8ZPKn85d7ud6ZN98r2WMAlNZUWrY5UX9FZjZG73VoYI9RP_P8GwO89ydFxwgc39BOKZzEh95A-h2ciYsaEFKiA4Zt4AgPG9yp-i5Kj8HxUbwD8bqaGji_cCO7FD7AVEls2EoSjk5ULwBrWhiyFq70xiShTRluzQZXmsnV7fu75KLHfpREkY4f_SE7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | شنبه ۹ خرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/438712" target="_blank">📅 01:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438702">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r9WtJ3-YDBVGrFLsl0pDK1pvJ3QaodVEDIwYrGqNvoeUazITO1X8Jhk8ZCFVQ7G1Z3rYQgVP2E3ZPC4Vh9MclkeFtb4eNN_dnZG-XglIDM_OhnstWs6nVBRj6NNrotJD4YcfOiLcakxJeVgbCswQNpQh1zZjFyunT4WTiJklIZGl9i5OmOdBYRWKlzgPuVbpZnVDtMj0jkyILLzHYZ1Uh79CW747Fn2FLS8JyNJJxv8vLozsv_AY3cwmisFwHdIJwke7f4rhCRRytpWGCe9xVONBY51_slnfRa1cXpGT-2LxgegW7t4d6pcciRyCcGtDRLUrWfjoGappcAzw20QsKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZY_Pledfuos3RiIoIHb0xYK4uhx5fnGlkayQnTAP9hI5gcZDo7kjo54k2_Qtc0TZY-aLh9SD-0QMLgDTsqEpkvvyxEyPDg6vmYb0wofCdCjxeeop6Wq6hyIUDAy2og7e2i0TiCuStXU0PApDNFXOuhtGeMMmuChZsGyZEXH5F0hYcBLj1CA-HNE4sRkVnu42N97UTiHCwO9pEQb01reE3TNq1jgBw3MSbaT4AmgFFrAu550fIpA57dUYLu6UIyPAEhmjvw0ghJJxI5a-oXNLygMw8zMxS2rW41eoZJozc9-5g4pemNI82gfsoWpxbCP0YImAiozH_aFsT6B4vpUHEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZMWFLOBJ5UKPtbvLmVmbVnMu3hZJ8Y2YBcHTSQQKnqkEQH0mndSBaZdDEcSilyz9TswPwyfiuBtOTTosbupWncqXJOqOdspbQ_Nxr81V-nT8kBGyeT5GKSoPMhFzFAnhqJo0Tdei9hk5x4-nfZ4qQ5ye0KLyGVZlA_kUt98AYdGuXxFeUPxLlXj9QDQ76dvQpcOJsXLjl2e0bwqpIs4JiUXQyXeC-TfpbICQrs5B_f4gzb0qZNFnGX5SmFwcS9bcZ9bLua4JxPhM-hjmytD4QH92puSG2AC2IHvRQaTY9U5uWt6P1kmTSlsldJ4wzOq20QXa_ntCTOw_pbpsOq72iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZGl7Y3QZoF3K-dpshiCVhF7f86R5aWlvG0Bn_J1xRw_UTOP_aIAKEtv3qB1GpDR9Cr1EKX6Xegsgykm0SEr8lK4W6xkGDa6H9CbOnKNOWoQdSdgY5vP-i-sQ_SixUu8aTMMHBO53qTo-ORSOPuDcSnU0RPfkpzc4JRPh-_NYMqgEwKjgbiOsOtTh6wrxrCWJ0JhWYdo0TnaH38QtY_mPyFC7cyqhWBSax7df6IOgZihQYUJuFepoFtTaqCCvO1amQyp3msN-eabN1FsGy8SsEKeTFKQ90lfcQqiWdMlE6Ln_e7lJLAqwUYoU2dPZOji7y5Hc1cAcw7uGFJdhwhGdQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oyICtu37vwQBZI8Lka7PzOFH5QDjdciwVREFB85J_RQhgkLHdXVWf58DcATOYV1exYSP-ACsSDr3YPVh1LmIFV60WPCSaLU99TeH4AgyQSrHVzAcEvE6BHVZf5LHo0b3dVoz-D2AkwQdwUR5EtWPsrZUdy215B1jLr6If3mNIgcKIhkXvDrACsqHEBNQS8KIb8bOYGvGqK8kB8DMez_KsvpKx8_pW1CoDfSGXAkS8fv4K1sbLjKdFZvmPMSmVUIC4tqBvlwaPs-dp5w8eZHpJhPezWIdBC8mOKaPcoPOiCZ-OiEt8DbEoRFUs-AoHn4upwaDAx0ZW7g59qC_MBA_tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WkPnw_pHnrXS4smtVn1N-aTj5sZj52nM21k74Z-s-FdXbfBoZFQx2MK1D37oc8qOyHn2TMQnGjE7kjgkVl1V8NVpUpzBdXTMRP9bdzQikNyXSfIcyoJ8FjIBbAJehsEFQ7M_xJjTBq9OWKomAn_KRPGE4BXMdZLtmQCucWgGfppEmf-2yUW3mWdKBLKSBH3u0XihGiqkwhdhy9il0eqW2VMWtPIbhfowRiZpQlt0QWr7HdnkZrmIxJgNbog3x8l0Zzc9GAtHyFWJIler1vmK0ao5yFXZQbUtyLqGv3C9JTSAc3qZzNShsKJafHYURZ4svIkFGhXLICiE9krDSscbvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oArB2-Uw8QTjEM_EKUyo5ocdP7bDEF58LA82BGUcwqmwhO6i1ddDjHXSKA1y1DxUzXHos-ssucG28GpM7xz5lWbqXLd6Z5R80P5KJlBxblYmgabgFGuGa0GdZLKOt2hiHDbb4nPQXAWEoWJYfOcusJK1Tq3r6bJzMWJZafuDaM3wmQIJOwWOWb-ENi9gh19HsUyAXYGG8vnal4GUO0LJJ61hn6XJZUqMw6vax7LEzE0IYUsJfJUg-Zg4oZiTrqay0p_ivdLyWPyqc89UBKPmaKtpxFasJwPo2dxOl5S7yy5rbqbv9tIVc-q7UkFV18lhE7Mg2e_d0wpFlHE6QtSnwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NuWvXfsHXoN47tYzGZyGROVKv1XbJ7EQkRpfCzpKhZwMmWPf1LB_c0Ii0WM8G_lbyzRxwPd5OpMmyvpuPbSLMDqfOUTUbZrUUtovmQkU8r3PGUEuMPlpNwoBRU01E5NLL_fEd016-O5JoIpGsgGgQRGF8VoORZpscZan8KAaTuLXfly2A6E8db8bFIct8XghqQr7r3P1XDH1bQubpiP2noe6FdmuTrJwdJ9ibNev1o_qL05eavYWcIXWGxrXA7dBIDuIePIvWZwda0LVvHuFQARb5MfVUVN64e3QK5oTlepTWvX8BNdS_SzsecSK_-ZO1LW0fQQrIjlTvC9NSym0CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EZi71fd1tLW2tC80j2A3qNaHTK3RxK2qO45a_2QQMORzK1ApK5pC4qHfgidBXqoCfJnoeHqVvliy-N0yfMSi1ecwsegpDBO0at_wJHJSmFc6vmzePIpBEY_NbQKJ-g9ec21BGWRonKELCUrnl2UPyk3sYimWmT-Egt2Sx-BcI3go4tEdj0D8vfMjvTTD0DjGPz64O9pnKHxP-5X5-E79PwbnQlRy30XpBogdcBPRqpQ6UDBlwwSnX7icMBh9r4a6x4v08FyndylUrd9yDhj5PjY60Z5fs_EeZnfSYB8Pe_FxJF4iJjQgA6slQjEmG5YZTMbkESG5gnKhAdwoHwlceg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S9t8ssAukeQ9NmUmK7citnzd4oB9TVrlk6jdZFH4T9ki0vOn9_IUwSMJ8LMBo5Pi57piiGCNfPv6YrpnX6IA5iMiiilRdVYuA3zd5iWob7AAcjSS1-xRmjkoLLnPQx9ym0aBcRhCc1w8MWlRpAoZTgzIudt8szsxRroORF3_PMnj020oSmPAWqfVhQeBOVAi-YYRIOrwfN2-r8UjpAGoRq55e5u0TzFP6fM4bvnaCpet4vkbK7H0HXbuxzmU5IUN8bCxDuqK91nhEXdciU30RPZ_XlMnhdSYuO5wAT4W3Zi4B9tCXJ1alGLoz3PKXQ9WyVyPCTAI0CjB0rTeG60oDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/438702" target="_blank">📅 01:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438701">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJLvBAr-9WGRU7QdDS2JYpmQ7asOzz0cePsiuPnJ7n2Yg9T-1fQ0LXISznaOhVUSprgxHQtpHNmXOavN7x75Br-oMFagM_w3Mjr36VyXYnGwBOBKsM490VGk2VIQXEewKqyTRuZLj-CFOHyBSFPu3Cz_oKSqMZDlsiRQvBUcVEMzxszMlHPAQw2BmNe2docNriIy1ZRuw-rwoORg9pjIMliIW0Hf0nBBp8trMHwaDWBtedGGdvUVgYPkcF7yMm72Q-8RQHc9cGSTOxlaz8_vOZ7ocbY22CdX8tbSpzB8EY3tY32nrRGa9iRRjAMMp_z361AsYSVpxQD5EEgUjt1dtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهای موفقیت
🔹
روزی فریتس کرایسلر، هنرمند اتریشی، در پایان یکی از کنسرت‌های بزرگش با تشویق بی‌امان و ایستادهٔ تماشاگران مواجه شد.
🔹
پس از پایان برنامه، کرایسلر درحال جمع‌آوری وسایل خود در پشت صحنه بود.
🔹
در همین لحظه یکی از طرفدارانش به سراغ او آمد و گفت: «استاد! من حاضرم نصف عمرم را بدهم تا بتوانم مثل شما به این زیبایی ویولن بزنم!»
🔹
کرایسلر گفت: «من هم دقیقاً همین کار را کرده‌ام! نصف عمرم را داده‌ام.»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/438701" target="_blank">📅 00:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438700">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🎥
نودمین شب حماسۀ مردم در کازرون
@Farsna</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/438700" target="_blank">📅 00:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438699">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">نتانیاهو: عملیات‌های ما محدود به جنوب لبنان نیست و به بیروت هم می‌رسد
🔹
در حالی که دولت لبنان همچنان به مذاکرات مستقیم با رژیم صهیونیستی دلخوش کرده، بنیامین نتانیاهو نخست وزیر رژیم برای اشغال بیروت خط و نشان کشید.
🔹
نتانیاهو به صراحت گفت که عملیات ارتش رژیم…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/438699" target="_blank">📅 00:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438698">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3X3I1lcXzSu3mek9aXipDNg8YeUI5bYzzt70kpQYzvWco1SrpTcjujd5M3eofeBP0WW81_fkJuxxudkWKjAbIOST9Nf6xDUjWyD923Z0t2YfH_QQo6nWc7P_Z8_JYkCsq71wY7loLVdkomuLcUPSw2hYX4hp_dMM-sa0lPCvLplONPJtOyMjtnSLOVkdeFxVsyhXOIjCjc8WCOkB3Kv5K65clv6XYGk2l23lQk1E41xmEy0yy1Izrt8tiVYszKTXA-3hUTPk-mfZDLyPy_5oOoTwX_SpN9_t4Lnq0ZWFl0iFcNGpYyq3kgsaC_lizVmG0GeQt5Vin985ulvKx_brw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ باز هم خواسته‌های خود از ایران را فهرست کرد   رئيس‌جمهور آمریکا در تروث‌سوشال نوشت:   ایران باید بپذیرد که هرگز سلاح هسته‌ای یا بمب اتمی نخواهد داشت. تنگه هرمز باید فوراً برای تردد بی‌قیدوشرط کشتی‌ها در هر دو جهت باز شود، بدون هیچ عوارضی.
🔹
تمام مین‌های…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/438698" target="_blank">📅 00:13 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438697">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EduCZZFPHBEh9lMCAe3tF6szMQ3T3fZNZcUQ3yLc2pqQHJ0FoNDyCuqcDawld17nY3CvQo9ia7Q7dIdqLXyY2qIHNMhs6mvwlqOPGzy1PJsHqZLRW1whaV1BOY7C1LMOviPyztK6PqBTeu4eGve_l2PgnGvyKkBi6mT7ef8ftnpmunf5axIWRH-7zVfu9ufVFGQHTKSTW0RqMccr4LAogiPFk1REXzRqqPSaKapRlGbTk53qoDqvTcdnARoCAlNxJJ39DIZhXAF9tV_V6KSmSeKBMmawWcmHEMyMF6knsygvZ1uw7OftXaA3MB7qGKvzTocJMMnKt1NqMDNNefolzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ثبت‌نام دانش‌آموزان غیرحضوری شد
🔹
معاون مرکز فناوری آموزش‌وپرورش: والدین با مراجعه به پنجرهٔ واحد آموزش‌وپرورش و وارد کردن کد ملی و تاریخ تولد فرزند خود می‌توانند مراحل پیش‌ثبت‌نام را آغاز کنند؛ این فرایند در ۶ مرحله انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/438697" target="_blank">📅 00:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438696">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aae8e40244.mp4?token=bHOlCeF-2xUKApLic5aTbcRDqbPoo8O2VW9M7SCZSv5dJUUH-49f4lyTjXNbj-Q9ThKNWRKF1-TNER1qqYGOa1JYKZaxM9-ruXL9DsDLMRn15bau5h4XHfjhJhnU-1l--qqKvDwZ5PDqhrSCRAhDZf4kAjYgk80RZ9Ww5TgiK0ETX6cZtrA9fbShmEzI_o_6bh8YLCTmFYtKgpwPfOFxp0fCSBGzH0zC-pKLn6oon8au-iZMZHnS9otdLOE7iMmlel2ubaTN-RxlBweTmPHK8U4M35c63wWf57yulrPgnDllpRlh1kn2BW3FtJwbzhcYJ75su4ZJRzn5kkmf24qFGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aae8e40244.mp4?token=bHOlCeF-2xUKApLic5aTbcRDqbPoo8O2VW9M7SCZSv5dJUUH-49f4lyTjXNbj-Q9ThKNWRKF1-TNER1qqYGOa1JYKZaxM9-ruXL9DsDLMRn15bau5h4XHfjhJhnU-1l--qqKvDwZ5PDqhrSCRAhDZf4kAjYgk80RZ9Ww5TgiK0ETX6cZtrA9fbShmEzI_o_6bh8YLCTmFYtKgpwPfOFxp0fCSBGzH0zC-pKLn6oon8au-iZMZHnS9otdLOE7iMmlel2ubaTN-RxlBweTmPHK8U4M35c63wWf57yulrPgnDllpRlh1kn2BW3FtJwbzhcYJ75su4ZJRzn5kkmf24qFGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع مردم سروستان استان فارس در نودمین شب ایستادگی
@Farsna
- Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/438696" target="_blank">📅 23:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438695">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‌
🔴
حزب‌الله: ۳ تانک مرکاوا در شهر «یحمر الشقیف» مورد اصابت قطعی پهپادهای انتحاری ابابیل قرار گرفت.  @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/438695" target="_blank">📅 23:47 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438694">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2Phf02xTLYOZxMKcj1_9Q88JlptXH7HTXm8i0LDf98sCWqT2-rsygZz21m_S_EGFPnk9kwrdUma5Luf_LyB7zBYvDCcWuVuMddUEgf3HgpRBHD8soTow32pd9-IidLBj4j43SaNvLj_yyQJO2z-iJQsUfz9keaTbrYpKjek1hi3uC6ytjDhKBHoLn5PNqWvmFXEy9LEhRqzfJb0FGkH3EyQqTzg2f7XgNz3SSM1X9dgfg7UhmTiPlVZxmdTAgrVffLlgfrNVe597B3qhg1Xt6cNo6WfFsRvqU5_Y1bRF9X-b9XgKIqGIY_ynHHmVBmvWXw0chK5ATzSqAl5GcHKjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمرهٔ مردم به عملکرد قوه‌قضائیه در برخورد با وطن‌فروشان
🔹
پژوهشکدهٔ مطالعات و تحقیقات دانشگاه جامع انقلاب اسلامی در یک نظرسنجی از مردم پرسید که «عملکرد قوه قضائیه در برخورد با وطن فروشان وجاسوسان داخلی را چگونه ارزیابی می‌کنید؟»
🔹
طبق پاسخی که مشارکت‌کنندگان به این پرسش دادند ۳۹.۴ از مردم در این مورد عملکرد قوه قضائیه را خوب و ۱۳.۵ درصدر از مردم نیز این عملکرد را خیلی خوب ارزیابی کرده‌اند.
🔹
همچنین ۱۶ درصد از مردم عملکرد قوه قضائیه در این موضوع را متوسط و ۲۰.۴ درصد نیز ضعیف و ۵.۷ درصد خیلی ضعیف ارزیابی کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/438694" target="_blank">📅 23:47 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438692">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YlYcdISbgOXp1pmPWuvl5OdLnaYK2A5jq4H-hDJszaWcawyMooeaQcuuq_6jRzt8_cCqyqV4Be4qU6N2Wdz1sySF39kfbQ3QACw-3elDlco9Q_KxtH9LCOte1wKdPomJZ9Fe_Bt4zNjcvzH7_Y6yiwOERFWG02sk4c6nEK6eC72AnxtuueXcQrcjUSvvtctM9fCgG_VyairLbuwQ7MgPMjISGfPCDnzAT4UHLqlqXyUjkmcNqJFvkt2NDm1CQrUWG_LIOL-w_MKWwPCjmcpIMJTeJfp8k6RcRf3oOvsFRH1BkxGjGUGtVi2n8MIJZ7_SmNKRSjiE7NHAG3Ds0jwdMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CTC64SY_rmvFR4MyGrWEMMxGs_DNJygESCErWO6Sau6yrOaazKtE2FIpLdqOjH-3wB7yF5qAHZV0-CiMVoKUT_U7wrtuY0qMrIpOsWpkLppM0tr_s0tZHz6XAAjWG9v1I9Y9JVcYPh9leyUrvGmqQNaQCLRv1u7-ECFVCKJtgLXLAVgR7mh7JSAstnEkpTGKTfJ__HFGcZkCsfZDXHuw02pLyVbFgQAC7Cxj9VwmEepQmMr73j76sPuUW62m9OuxHRedalDGyywVCtgPnpOHDvSPhgCws4nZX_F2fEdOhv5WTOcbcfXpz5qBke3dMMObzab3M-cx8cZBXPlxy1OjPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نهاد مدیریت آب‌راه خلیج فارس: تسلط بر تنگهٔ هرمز را که در میدان و دیپلماسی به دست نیاوردید، با تحریم هم به دست نخواهید آورد
🔹
وزارت خزانه‌داری آمریکا اخیرا از تحریم نهاد مدیریت آب‌راه خلیج فارس خبر داده. این نهاد ضمن محکومیت این اقدام، تحریم‌شدن توسط کشوری را که رئیس آن به دزدی دریایی افتخار می‌کند، نشانه‌ای از عملکرد مثبت خود می‌داند.
🔹
علیرغم اقدامات تنش‌زای ایالات متحده در آب‌های خلیج فارس و دریای عمان، این نهاد در راستای تسهیل تردد، بی‌وقفه به بررسی و ارائه مجوز عبور به شناورهای غیرمتخاصم ادامه می‌دهد؛ به زودی آماری از ماه اول فعالیت نهاد PGSA  منتشر خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/438692" target="_blank">📅 23:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438691">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbUIcBo_0k18xqJ-g-ywmXj1qOA-NM37v50hfa3Hb1Q41Ht1_-VMj75Qt_nRqOwsV15aXhnoO7x33aQyTakbnmcFhXOFZMUvDkRCCaso-xaR0z-8QIJ1F3j6qItW8vCV6NM_Yhz6kYqUgdZUzz1y5o_GEfFmY6CyUT4eT5TrcEVPwfCRdkofNkM_JYnh5WiXmI7L4_GlZHPX0tN5WMB7_DO6ald_lzPCVwnd0GD2Yx48BexTP8Uj6t1orTqBfuiwDOxSlkVkjT76MqBRVTjkDXgBRsOB55t642YmP2Z7zGNF1Tk4fHSauGC4mA-4r3AAnWNzaXDHdaQeieQ3johTQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سرمایه‌گذاری با صرفه‌جویی در مصرف برق
🔹
در طرح جدید وزارت نیرو، مردم و شرکت‌ها به ازای هر مگاوات‌ساعت یک گواهی قابل‌معامله در بورس انرژی دریافت می‌کنند که می‌توانند آن را بفروشند. @Farsna</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/438691" target="_blank">📅 23:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438690">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🎥
تجمع بندرعباسی‌ها در سواحل شمال تنگهٔ هرمز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/438690" target="_blank">📅 23:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438683">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h_FhYYlj32xMIgRunSfVcg5PDEFXLlIThaTaKaq6Ah-la9IOJJLQKmU8wpLCAoAH73ooE_7rV0ignQNS6xTQGpHT4uhoZLPVmJQ5GEWRrRIMmTTvFwFMpMO4YCTB8FGd1l4Hlg5aYjyQR4ZT81vD8RO5GyR_2O--2cqrr7T3e_GNl-NsCSev_HVlmG3LKfXbVMBi5T11F4L95Yo10o55f5Z-gC_6093lPFlGG45DAnKHKiN3UiONJcpvutTI7mOgBfCuDKpAyGXXS2L2vEGPZMDvn7nRS60ETjF7GoDe6zeTNxcfkS8KIR1RY8QJVnhfOZKa_WZrxH92Ox2NBTNHng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m1RFd-MEAOdSih9_gjYkVReD3K0CzWf1RECa2eUwg_c-S73zF4cJQD7OjawDtjXEZS7J_j8JqnlQawDRjrLai4Hr6Cb-Arj14XT4by6tuya7T__MhYxpNcf-Sr7LjfUFvJ7oM-u0IB-eeqq0hDGowjkokPgRGKQ_sunE4GubtZ6uOXe-TqRMqr98Ourpd99c1El5gqUBJAeF3gFFabp5tGm5N1l9saNrFim9nEa3S70hkH3vtxGGcou8V2EYD4IcqdU2OxSeDCLcEa4FxL487m20zk8V5ZUtgnMHoul0zO0TsSPzFiRbbHO_tT4ONhAaeU13a73QUyjODWrrexMdLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VeOSu_Tl2Ukb4qzwERFCvpEIKqBOo6ReLTPlQjKXsSjHXmvjsr0JAAnJURaW5Za9AchafhMqvtVpW0akmDG6GxoL7blEI3cdnH3_AYrDR5F_d3rw9ba0TULME9Pf-eaaft8YZSytdkcvd-_C4rpvaVeL6McigL4ZfJxKkR1HMMDW9JDhzSOyIDJBjogAycS_9H1ebvYf98aEonz6zCHnlDu3BlkTnyzJ_Zv0virWQupdiPwy46qMYNfALc1E6wA839Wl3YHSoNlfu29lQGHHC8_Aj1_dXkSoOmPp_eB3v8RDqURpftLBZnAuq8ozwPF56fFd3Qv8kF9HmpNpw-XA5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yh46PWQiZHP0Om96uZyjCgskZ7jRV9UM77nTESPSvMtirfcKqxQwkG6-OUFdvExMpLXRwLbKVAyGBrUZm1Px_lAm4qVoR6EZDIXgc2pz_eSC0xngzQky2G5h-goNk5QmyHq-eg4llIPFNB6_R1x79kfJ_Kj2cDeonif9Id5M33y2h-29eBguGac0tD1WB815H2cjxUCKWG4V8eGUplHBbQKpcUP8GynlKagFC0o0dHyDYSW7LOQhym7lXRyPqpOAea4EpFJ6x0Ptuy2pyI1zYayYyFp6pHFnd2cpX1IWz4X6_nlKnqHomk08kvGB0cKbuODxil7CdLvvBpmsSLRIfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qKKp778jgyxLnf-9MXqo-mO6_eGyeRR0hUgda6KNpY4qm7c6blewkdqUHWB-zjNkU3wuI6HPCvGPP9R606bhtzNOg0MzdemxhbLiGJ9q6Aa7F56L8oynXW8zBsfTBXuhuSCD2GHoghio1FM88FxYNyWMZoyK6SovFt7DfPGrVXefsjx7eKoNFdtc0vai0S036aA4u2x8R8s7buAtVJCFayzEa9a4hBB9vXcUwXRBqHNLiRRmlrW-MuCu2kd2qulNBKsqLwYYamcJjhWhKZnq_p5B-iOD-QMomnVaBAWguWzHfJe2ibIJgOWz97xP_4Z4o6m9XtstNdYRhx53fwE1QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KyS7-3Z8Q2bjrNKXQb3MJfQh9o3lvkh3VOrTJgYvq_EnppIupYmuR5ZSdeMdIf-5nGgHfUSe5qxgPO51A9AjyFeObO9G-hEVb-moU66eI8DaIOW2bWmHa60gLgf33Y6VwuWH40npofFUXy91DMRKM8JVNQ7tKkkFctIA1H1tScCVcVM0hgh-lZ1LkB1rVA3GcNvtRGSeppNOHIe4ymOOQnPnGWCtnh6aRfdm7I91IG9FP4cWz6nSkaV7AXrY5cxJVJu_td4zqGBkX46x4yqtcDv7cp0uo6Du20rDvBdtx9YmbUcG4ko7-yGQS3Q-r0sT-MrlpcQtOeVCPBRCsOB1RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e41V1aJDeuXUuD_XCWlMKS7DJLVT_eSViB_Bo9Hi2TL4Uxj3yOKz9Qlm32FekW9EV4B-pp29Kggq7hfUnkUcYS233ceuMItfB0O5I3ZVnkKcZbUzSlU1CRMSUYOyfn9fRjNjec8VWQOUBpTrx7lQsdH5QR_-ygsh0JqhyElfnuSbSWR7e8x-6Gwq2Zak4en49KKByyyHRU6YUyTVyYWvOwp0hRgCjhycBvljwgmyvmULCszHaXYWisL7J8ax0p3dKvCUquaeMliVx20zLDPqnLSnjHZlxYVOQQgnUk0QpWrHNCLR6yOru4mlacC0qGaJVve23mGBs9QjwlyFyG7xtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
قاب‌هایی از مراسم یادبود شهدای خانواده رهبر شهید امت  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/438683" target="_blank">📅 23:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438682">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/051d3936e0.mp4?token=Op4kzBbBSiB02ZrBKr4FuhQKZ8t7OjPE6R5Pzurh7qo4R3y5vLn_Zohl1C6ddBq2aA6zkRu20vAvMJlFZLlgKMmUHab2LjdPogeIxfDuCue98NoDMAxNaJAM_YvawCaoxMU2BFdnii2fzOjVghNYvfyB6BbTC0z4qIDO2DPtkdbdWMpkBYh5tJ2TtMmrbqPo-VQPq6DP57JtHPr_d-2tqbMBDyjiVVWC8IpASyvpwjFCA9_60o2y0Z_q78HeIAqHsJIXdKXfC5ohYil1we3lOAcRxnT8r6Xj_dHa-51Gw92y0hPKyFpMqu-cUxWBG34vZ3yMa-hilXp704JIbX8KCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/051d3936e0.mp4?token=Op4kzBbBSiB02ZrBKr4FuhQKZ8t7OjPE6R5Pzurh7qo4R3y5vLn_Zohl1C6ddBq2aA6zkRu20vAvMJlFZLlgKMmUHab2LjdPogeIxfDuCue98NoDMAxNaJAM_YvawCaoxMU2BFdnii2fzOjVghNYvfyB6BbTC0z4qIDO2DPtkdbdWMpkBYh5tJ2TtMmrbqPo-VQPq6DP57JtHPr_d-2tqbMBDyjiVVWC8IpASyvpwjFCA9_60o2y0Z_q78HeIAqHsJIXdKXfC5ohYil1we3lOAcRxnT8r6Xj_dHa-51Gw92y0hPKyFpMqu-cUxWBG34vZ3yMa-hilXp704JIbX8KCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گرگانی‌ها در سنگر خیابان نماز استغاثه خواندند
@Farsna</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/438682" target="_blank">📅 23:14 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438681">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🎥
بذرپاش: استحکام درونی، جنگ رسانه‌‌ای و ادراکی، جنگ اقتصادی و تغییر اهداف آمریکا از حمله به‌کشور، ۴ عرصهٔ پیروزی ملت ایران است.
@Farsna</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/438681" target="_blank">📅 23:08 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438680">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا امروز مدعی مصادره
ٔ
حدود یک میلیارد دلار از دارایی‌های رمزارزی ایرانی‌ها توسط ایالات متحده شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/438680" target="_blank">📅 23:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438679">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/902d8966f3.mp4?token=j-F6B0OfB5wf4V2AuzRGog6hzqkcvxY3BfD2tzJtiXN8Co2rXRVtwCT1HRf8K-HLGELdKoSlcolmtggFWhevBgESttGImiWg7COQkaiidet41Y9VGqC3PH3s4MOyn4XZI3ivbd_hJkrHK6c-fYKxJ3RpjLdMME_QXriSk9sxCWM4alLrayXsa-USlRSz9IYfSMzkAG7Zy1SRlMWmDNjqZTtloNj8D0GhEi3uAEwj1v2sckfdqZWM6L3gmKjKlXX8coUwJ1xuch9bv7ZMyCeTqisHSwbCSptuX5D8cjrnvRVIOcCXCX2gZ2o_D5Bp4-tLwMT5SwvoBNy3Y_5NVe9wnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/902d8966f3.mp4?token=j-F6B0OfB5wf4V2AuzRGog6hzqkcvxY3BfD2tzJtiXN8Co2rXRVtwCT1HRf8K-HLGELdKoSlcolmtggFWhevBgESttGImiWg7COQkaiidet41Y9VGqC3PH3s4MOyn4XZI3ivbd_hJkrHK6c-fYKxJ3RpjLdMME_QXriSk9sxCWM4alLrayXsa-USlRSz9IYfSMzkAG7Zy1SRlMWmDNjqZTtloNj8D0GhEi3uAEwj1v2sckfdqZWM6L3gmKjKlXX8coUwJ1xuch9bv7ZMyCeTqisHSwbCSptuX5D8cjrnvRVIOcCXCX2gZ2o_D5Bp4-tLwMT5SwvoBNy3Y_5NVe9wnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مسابقهٔ یک آهو با قطار در میاندشت جاجرم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/438679" target="_blank">📅 22:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438678">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0AXEqLUEMD6nsCaYLIeAYQnMR4U3Nu2jVjlSVWQorU_kW8fxeyvdaycSXLL611MR6s1n3N6XuukjKCpmdoLcPtsr9WWLAi2O_InS9WDJigqrRigKXMaslLJdBOK_ddE3DWzo68wxmWE2K3QjbUtDAlvRv8gegmlHSg6DQw0D-54qOj4TnPnfACyP6CAzQLEhj9UVnq3r6wrNOqUZBRVb7K3SP5ez5htdfG6tlHjwiR4IeLSug1EEdCQK42GwoTj8t4Uw_pD4GCZQrkisXEqtEDG9RBU2Nd6HyywV60wzQNL8JyynXtHqShrG4uXK727F14pnIiHEgtOVokov7xRIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو شورای‌عالی انقلاب‌ فرهنگی:
امسال تغییری در تأثیر معدل بر کنکور ایجاد نمی‌شود
🔹
سعیدرضا عاملی: طبق ضوابطی که از قبل اعلام کردیم، هر تغییری در قاعده سازمان سنجش باید از یک‌سال قبل اعلام شود، بنابراین امسال تغییری در مصوبه نداریم و همان اثر قطعی معدل یازدهم و دوازدهم پابرجاست.
🔹
دراین خصوص نظر رئیس‌جمهور بر بازنگری مصوبه است و از این‌رو در اثر قطعی معدل یازدهم و دوازدهم برای کنکور سال آینده بازنگری خواهیم داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/438678" target="_blank">📅 22:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438677">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80b9aba9ed.mp4?token=JxTEPDfs6BP2xLjoCgRQN9PkLgjjzZXzE7WCCqGgalEQgW8StAMh1O3Xn7voRCBYzumjPoYaA71P5Y9yZLJo9VJggVj5PMuaXqt8suonEwORruRYzl2j8V82G-Kqma_NgJKYyGuYW_jpwiNasV3UOpaqPjAmc1CyKOVNg5bhGjqkQLHCNfOm_T2OQjmKJ079Wsk1gNwd6T2DkbsIsanwDEg48QeYkm2JXau6uf08gw6taO5_zChyVsxE22uvGTb2iNEuctHl_3YhIGbgPYa8Y0oF_yq2FQfnvu8noh44RrRU54W98Q3QW38HuRLpEusIqanuEOwKPbc4ciZky3R_iSWHTb6pY1m54OtpgThMxmMBUGhG66UrFnnISKV-U2rvJ0xfhTkJxr7Em7uMUyhTEin-htp00QJ00iLewTrSxFsW6sMZHaTCNGYLAQGpVYMc_GHVMqD1tnX1O9QAsAF9O2_uoxu2AsRsyDdivrJGcs2us6YN72v0pa202mDFVj7N4gPbD3QxI60Uoxw6ldbHjksXbLvy0_lVlRQz8YcRC_RYtbYkg_ySCCMkDI1NtBlcCaj-X9FExBEagcpUuHyUCpqqGMdv06iOILIFJEIPvCHH6Y1WHAtuIYFHuH1OUX-sU4-3rPdtUgXl8_RLoOaDHg0f2ywFwKt6RLnly6KFXV0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80b9aba9ed.mp4?token=JxTEPDfs6BP2xLjoCgRQN9PkLgjjzZXzE7WCCqGgalEQgW8StAMh1O3Xn7voRCBYzumjPoYaA71P5Y9yZLJo9VJggVj5PMuaXqt8suonEwORruRYzl2j8V82G-Kqma_NgJKYyGuYW_jpwiNasV3UOpaqPjAmc1CyKOVNg5bhGjqkQLHCNfOm_T2OQjmKJ079Wsk1gNwd6T2DkbsIsanwDEg48QeYkm2JXau6uf08gw6taO5_zChyVsxE22uvGTb2iNEuctHl_3YhIGbgPYa8Y0oF_yq2FQfnvu8noh44RrRU54W98Q3QW38HuRLpEusIqanuEOwKPbc4ciZky3R_iSWHTb6pY1m54OtpgThMxmMBUGhG66UrFnnISKV-U2rvJ0xfhTkJxr7Em7uMUyhTEin-htp00QJ00iLewTrSxFsW6sMZHaTCNGYLAQGpVYMc_GHVMqD1tnX1O9QAsAF9O2_uoxu2AsRsyDdivrJGcs2us6YN72v0pa202mDFVj7N4gPbD3QxI60Uoxw6ldbHjksXbLvy0_lVlRQz8YcRC_RYtbYkg_ySCCMkDI1NtBlcCaj-X9FExBEagcpUuHyUCpqqGMdv06iOILIFJEIPvCHH6Y1WHAtuIYFHuH1OUX-sU4-3rPdtUgXl8_RLoOaDHg0f2ywFwKt6RLnly6KFXV0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رزمایش اقتدار مدافعان امنیت در منطقهٔ غرب استان خراسان‌رضوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/438677" target="_blank">📅 22:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438676">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b359eeb3f1.mp4?token=OxismQkym7fH0q3R3WFKxDb3lj6TqSUyK_iyQ_oMdnEq-LMRIkhtldzdIDu7ZFdvBlu2nCae7kW5RzttF5P3X06n7WvoDzxp91HW4bDqsuM-OlYbr0Uz6hpByzLbzOmgNy1JA-gDJZsUZcd8pWpgBjX8AFzd0VC9Yv6AU5aFfwnr1P9jKdUddhsC8c8ictEFgsWy-kw2c8cuyUUwtWHNpeCczlmoQFLqM-0GT7zPI6slYcMKvl9FwTtbEv6fgGLWrGiR4qIAJRu3jp6Kak44tk96_hmXFEqaIJG8QgItcTCrA1dhNEaA9NtBXBbYuFus0HXbBbUHU4FmdSKDcn1tCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b359eeb3f1.mp4?token=OxismQkym7fH0q3R3WFKxDb3lj6TqSUyK_iyQ_oMdnEq-LMRIkhtldzdIDu7ZFdvBlu2nCae7kW5RzttF5P3X06n7WvoDzxp91HW4bDqsuM-OlYbr0Uz6hpByzLbzOmgNy1JA-gDJZsUZcd8pWpgBjX8AFzd0VC9Yv6AU5aFfwnr1P9jKdUddhsC8c8ictEFgsWy-kw2c8cuyUUwtWHNpeCczlmoQFLqM-0GT7zPI6slYcMKvl9FwTtbEv6fgGLWrGiR4qIAJRu3jp6Kak44tk96_hmXFEqaIJG8QgItcTCrA1dhNEaA9NtBXBbYuFus0HXbBbUHU4FmdSKDcn1tCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوحه‌سرایی محمدرضا طاهری در جوار محل شهادت رهبر انقلاب در رواق کشوردوست
@Farsna</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farsna/438676" target="_blank">📅 22:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438675">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f6e4ebc61.mp4?token=uK54b0YOJ5e4QQun4bhGAVypGhG8ro4iBEOMqcq4AcQBbWOwgc-FHm-fokClx9Z0YcAz7Ya-tGRH_HSxbqDQ7dMOTNt1iCcMZFksjEi4z1LHdWIejYHe7OB5RFkfUiwtifkuDQ9TjGiItd87Y4BlwsoOkk-GE1Qtt2NwT6HnFHmTMIB--eWh-qbJOMqLSqh3whcCRKPZ9rlSo5qMHq1L25B5OujttnyFFhNNwzTFAM16zm5Wk0xLi6JUqeuFVf2anxAdPTCY48N8-NP_6thp9340YWcNmBRkcKL9qbc4vs1Px_pj_mi17kzRZ_ykKjwmD_7sZNIgbiiQ9zzLT9ADbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f6e4ebc61.mp4?token=uK54b0YOJ5e4QQun4bhGAVypGhG8ro4iBEOMqcq4AcQBbWOwgc-FHm-fokClx9Z0YcAz7Ya-tGRH_HSxbqDQ7dMOTNt1iCcMZFksjEi4z1LHdWIejYHe7OB5RFkfUiwtifkuDQ9TjGiItd87Y4BlwsoOkk-GE1Qtt2NwT6HnFHmTMIB--eWh-qbJOMqLSqh3whcCRKPZ9rlSo5qMHq1L25B5OujttnyFFhNNwzTFAM16zm5Wk0xLi6JUqeuFVf2anxAdPTCY48N8-NP_6thp9340YWcNmBRkcKL9qbc4vs1Px_pj_mi17kzRZ_ykKjwmD_7sZNIgbiiQ9zzLT9ADbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«شاهد ۱۳۶» این‌بار به جمع مردمِ میدان در سنقر کرمانشاه رفت
@Farsna</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/438675" target="_blank">📅 22:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438674">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c9039a3e3.mp4?token=TGa_BHWJOYdq-TBIq9LgP1b4jln2tOHA6Tj_3amE6PUk4zdtAhUVXCWzQj_hv2H0No8maRWmqK_HBSinUfdwOcxsTkgT4giw3TQSzRoXhfAH26RjwAj_ddFvLZF_Yl-E4eAIi4frjQMxzMKL771nSYFNElUVMlKzwe2AIyXoE2rMMuvQ3rWpujekGDWil7kAKWO0jZBfWwXd4DRgXGnV1DDIE7D1cGMR5ZM2VRPMmLwKDTM-1RnKdIgeVdlm-b7uGgAPP3Ed1cMCN-_lFQolrlUMYku7GiOtdLTu87Hey89pT3hpSBY2caktTsS-_Lt1CkTTI19cuuf7jqAKh8Kl1Rro4BnGUT5RGPCDmGX7IwS1fVAVfcctBLvrOMJty1GE6Buazbgmpk4sNxZb9nuBtsD9P-2QUQOA2tE30bIkxvEVeSpuyd5fBF4ZGbmooPLM8f9r6dE-h3S9_GeQfQWuuO-YruU8k-jDoYEubHlRXZR-oLjseqxA4tRidx-CLPKZNlVHoy-YFrK4-FqHroCX2a_PG3_MUExDQ4pcSWBccRrRBQPAI6iDcvEFDoGgt4h5WzBLfArB_h0P3Zvj4wDHL_eUVedYsUKqIY4mkc45kDFu3IoWcYJpr3ef09_kYQL4qyjCYvYHbhfKVmaOmku-YezTOpZQR-5IJOccuYtEPB4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c9039a3e3.mp4?token=TGa_BHWJOYdq-TBIq9LgP1b4jln2tOHA6Tj_3amE6PUk4zdtAhUVXCWzQj_hv2H0No8maRWmqK_HBSinUfdwOcxsTkgT4giw3TQSzRoXhfAH26RjwAj_ddFvLZF_Yl-E4eAIi4frjQMxzMKL771nSYFNElUVMlKzwe2AIyXoE2rMMuvQ3rWpujekGDWil7kAKWO0jZBfWwXd4DRgXGnV1DDIE7D1cGMR5ZM2VRPMmLwKDTM-1RnKdIgeVdlm-b7uGgAPP3Ed1cMCN-_lFQolrlUMYku7GiOtdLTu87Hey89pT3hpSBY2caktTsS-_Lt1CkTTI19cuuf7jqAKh8Kl1Rro4BnGUT5RGPCDmGX7IwS1fVAVfcctBLvrOMJty1GE6Buazbgmpk4sNxZb9nuBtsD9P-2QUQOA2tE30bIkxvEVeSpuyd5fBF4ZGbmooPLM8f9r6dE-h3S9_GeQfQWuuO-YruU8k-jDoYEubHlRXZR-oLjseqxA4tRidx-CLPKZNlVHoy-YFrK4-FqHroCX2a_PG3_MUExDQ4pcSWBccRrRBQPAI6iDcvEFDoGgt4h5WzBLfArB_h0P3Zvj4wDHL_eUVedYsUKqIY4mkc45kDFu3IoWcYJpr3ef09_kYQL4qyjCYvYHbhfKVmaOmku-YezTOpZQR-5IJOccuYtEPB4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محبی: از مردم می‌خواهم ما را دعا کنند تا نتیجهٔ خوبی در جام‌جهانی بگیریم؛ امیدواریم یکی دو مرحله صعود کنیم.
@Sportfars</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/438674" target="_blank">📅 22:27 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438673">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21f190dad3.mp4?token=sL87mAZRL9X0fiDD_Q767QcUCx7FlK1kTLgnHLWkuqZetQ-CHGtp9gDKARUb2pBZ_cvZl-J8Vu7YZO0uiAsilePahlqt-msy-xWcpi7PtDEDOm3dk6TcEZcG8LWGec4wrauQZtcC3lKtK1IFTG9NqEN0r3NzMFdF8hIxpUMlU-hnQl2l7A-M4VpGzDTLzA1wTTgUIKUuguMrZy1D3sUqtG0zt3m5Q5ERCrgOS2ynQaHUpQWQueWtIScZ0K8ZCsruCPu9-bu4kJeskKpjPWDBbTFmHd7EpVqEO01ys5WnFWog70_nE4mSXdr1XyD3Blj9IwSxRjSr2E26zsPgzzKHdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21f190dad3.mp4?token=sL87mAZRL9X0fiDD_Q767QcUCx7FlK1kTLgnHLWkuqZetQ-CHGtp9gDKARUb2pBZ_cvZl-J8Vu7YZO0uiAsilePahlqt-msy-xWcpi7PtDEDOm3dk6TcEZcG8LWGec4wrauQZtcC3lKtK1IFTG9NqEN0r3NzMFdF8hIxpUMlU-hnQl2l7A-M4VpGzDTLzA1wTTgUIKUuguMrZy1D3sUqtG0zt3m5Q5ERCrgOS2ynQaHUpQWQueWtIScZ0K8ZCsruCPu9-bu4kJeskKpjPWDBbTFmHd7EpVqEO01ys5WnFWog70_nE4mSXdr1XyD3Blj9IwSxRjSr2E26zsPgzzKHdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وداع با شهید سراجی‌نژاد در حرم بانوی کرامت
🔸
شهید اعظم سراجی‌نژاد ۲۳ اسفند سال گذشته در حملهٔ دشمن آمریکایی-صهیونی به منطقهٔ مسکونی به همراه همسرش به شهادت رسید و پیکر او به‌تازگی کشف شده است. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/438673" target="_blank">📅 22:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438672">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9ec753f90.mp4?token=HOODlZBq_CmNrUYDVnga8Kejr1X0qyggiSUJ1Wa9CUVkBEllVQfQqd3Ju35Fa7T1kWn_LLzi6ol3DcpYyJm2a2wb343CHai2vTT58cbw_z3JkJ2UEAlM9VK_zms6NLuCfZhtPhGVmg-IAbpTzHrQCoi1Jambelauv5H5FPVTsRH-2tNA2xn0x95OsYRBDQISvdDZZRG6CekfpSzlVi3knemtt1jbq0WrB7_SYNRFbDD5rC_R4kBtKd1sP5bmBCOzYqXllHL55F7yFwOCiUxhpGg1yUaGtopXQ4onFY97ZCpvGDAukxnvJREN-XQI21moP2nhppZ-AC6w20MJl5x5xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9ec753f90.mp4?token=HOODlZBq_CmNrUYDVnga8Kejr1X0qyggiSUJ1Wa9CUVkBEllVQfQqd3Ju35Fa7T1kWn_LLzi6ol3DcpYyJm2a2wb343CHai2vTT58cbw_z3JkJ2UEAlM9VK_zms6NLuCfZhtPhGVmg-IAbpTzHrQCoi1Jambelauv5H5FPVTsRH-2tNA2xn0x95OsYRBDQISvdDZZRG6CekfpSzlVi3knemtt1jbq0WrB7_SYNRFbDD5rC_R4kBtKd1sP5bmBCOzYqXllHL55F7yFwOCiUxhpGg1yUaGtopXQ4onFY97ZCpvGDAukxnvJREN-XQI21moP2nhppZ-AC6w20MJl5x5xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور دشمن شکن گنابادی‌ها در نودمین شبِ بعثت مردم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/438672" target="_blank">📅 22:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438671">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ul-svUyj31Ew84U2Z95NJf3C5oiULdmElx9I4Xlav6i9yBrG-E4yT_bmggf49Xan0ipvTJr-2Ha2ncosb_LXACvYfwe6t2_F1e3Kg3NejHeqfL0DpXUyU5wUpz4N9TMWhxmQKAmAnxkCsgKj6tCzt2Bz4atdkkueESsGeEE1OAJPW_6PDeNB9dc__CKiic9agTxhcuO-Kt91zQ2BG2vWN8TFti10RTuK-mbvNixRzMpXne5esDYZNoSq1YHeQQMeX-KQCgH4PijtyELv_IDJOrvZa4WWY8y3_nXGgAxWFb7UNHphUSzK2k9T8QOw0H1T7CBtDV2NAehCMZ7GHfiSog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سقاب اصفهانی: صرفه‌جویی منابع کشور را به سمت توسعهٔ زیرساخت‌ها و تقویت اقتصاد هدایت می‌کند
🔹
رئیس سازمان مدیریت راهبردی انرژی: صرفه‌جویی هر خانواده ایرانی، حتی به میزان یک لیتر در روز، در مقیاس ملی تأثیر بسزایی خواهد داشت و کشور را از واردات میلیون‌ها لیتر بنزین بی‌نیاز می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/438671" target="_blank">📅 22:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438670">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">یک ریز پرنده در آسمان قشم ساقط شد
🔹
به گفته منبعی در پدافند هوایی جنوب شرق کشور، در پی فعالیت پدافند در جزیره قشم یک ریزپرنده مورد اصابت قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/438670" target="_blank">📅 22:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438669">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72d408fca9.mp4?token=e-amzalnbwmrppJ3A_YIVpEPyfV7MKsrpv0HRZX1s3XZmxf3n6MvUUnAlrJrZg3HtA9rMCzclrBQQokLiaN3pXoyYH1lnQ2-SuLFIVMf2UwOjUQaQuISCUAuk0pcYzZctXsBHfMCib1djhe7sY846GFyeUOac-9IRwDpxMXsBChojNfoY3_PAbu00xviNdAakjJhLqm2vsUvRmLAk2RxbI5nVAmGJ9qtprlUDIeeGy_sHfL5mLd9xapYlHqUIUZZus3LYR4EBGSu_F0xzc2XOmSFSsAqV8IEcgafoNY8Pf1MbWorjDmffxK50w5xvxSw1iwYQ7l9AZ9zInZotvyi5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72d408fca9.mp4?token=e-amzalnbwmrppJ3A_YIVpEPyfV7MKsrpv0HRZX1s3XZmxf3n6MvUUnAlrJrZg3HtA9rMCzclrBQQokLiaN3pXoyYH1lnQ2-SuLFIVMf2UwOjUQaQuISCUAuk0pcYzZctXsBHfMCib1djhe7sY846GFyeUOac-9IRwDpxMXsBChojNfoY3_PAbu00xviNdAakjJhLqm2vsUvRmLAk2RxbI5nVAmGJ9qtprlUDIeeGy_sHfL5mLd9xapYlHqUIUZZus3LYR4EBGSu_F0xzc2XOmSFSsAqV8IEcgafoNY8Pf1MbWorjDmffxK50w5xvxSw1iwYQ7l9AZ9zInZotvyi5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ضدِّ انقلاب با عددسازی پرتناقض دربارهٔ کشته‌شدگان دی‌ماه به دنبال چه بود؟
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/438669" target="_blank">📅 22:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438668">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🎥
وزیر نیرو: به رهبر شهید انقلاب قول دادیم مصرف را کنترل کنیم
🔹
در روزهای جنگ رمضان علی‌رغم حملهٔ دشمن به زیرساخت‌ها، با تلاش نیروها خاموشی را تجربه نکردیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/438668" target="_blank">📅 21:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438667">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c9bba9e4d.mp4?token=vKOthK5_lFnTJi2CqIxnjG08HKgpArMMMfj5nLn4Ay--hc8veLdr8A9P7nPJmV0kzBS836twrDd98gA6MMoyWiDxl8dAozN92xBfuDG6mQVvPDJUZCc6-TpYlwHR_7-07-7vzfxLOsqOKgcrTlNI0rMALC4DdoJRzHZxkAyxBMtRVfRm_MMYNqknhC5H8VBy7-V0Up0CyP8nbnX9___2cLQA4FC0fSEf0-XeHeqCdBUzh6I3E9L0ihkw948n6AAAPsa1lPl0Vib-Me7Bpdgx9qgW8VuLOltn9yARqG5tdYtPipcF42FUtEwpUlqm2snb65fdoP9W-K7vwXAb7OsHBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c9bba9e4d.mp4?token=vKOthK5_lFnTJi2CqIxnjG08HKgpArMMMfj5nLn4Ay--hc8veLdr8A9P7nPJmV0kzBS836twrDd98gA6MMoyWiDxl8dAozN92xBfuDG6mQVvPDJUZCc6-TpYlwHR_7-07-7vzfxLOsqOKgcrTlNI0rMALC4DdoJRzHZxkAyxBMtRVfRm_MMYNqknhC5H8VBy7-V0Up0CyP8nbnX9___2cLQA4FC0fSEf0-XeHeqCdBUzh6I3E9L0ihkw948n6AAAPsa1lPl0Vib-Me7Bpdgx9qgW8VuLOltn9yARqG5tdYtPipcF42FUtEwpUlqm2snb65fdoP9W-K7vwXAb7OsHBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قاب‌هایی از مراسم یادبود شهدای خانواده رهبر شهید امت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/438667" target="_blank">📅 21:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438666">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🎥
«قدرت ایران»، پیام ۹۰ شب حضورِ مردم به‌دنیا
🔹
خون‌خواهان رهبر شهید در شهرستان پاکدشت استان تهران در نودمین تجمع شبانه بر لزوم تبعیت از رهبر انقلاب و حفظ وحدت تأکید کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/438666" target="_blank">📅 21:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438665">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YjrdP2tuLmBFFd7DrT7swmWSwi5d1OiZmd94dfVuDPXXji6CYcoz00BlAFVnW8OxsHlG7VmVdblH9SGDXpBbsP-1dEQBXUmr4AAhb_oXF0Si0So1heNMo0hRXUb7PygXclhVA9S-IrBUpQ8XAp2Am9X-7y7_IZk93VrBbK0Hipi14BB97F9NKRPfHQ_ihARigX5THKvpH62FkXURTH1-11sV-kKrRmaJYVtYgc19AxFSV3Y5ikGMycjzZEKswlsC9KizRVi45sh-cYpuGgiosE3r6Wo2JD_J14KtXeGciOmda0lRyV5qVFShZG1BqpWjqC9T7094GhAFV7roYs_5iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوان گم‌شده در ارتفاعات آبعلی پس از ۷ روز نجات پیدا کرد
🔹
هلال احمر استان تهران: فرد ۳۰ سالهٔ گم شده در ارتفاعات آبعلی، پس از ۷ روز تلاش نیروهای هلال‌احمر شهرستان دماوند نجات پیدا کرده و جهت اعزام به مرکز درمانی، به نیروهای اورژانس تحویل داده شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/438665" target="_blank">📅 21:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438664">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd01d1fb90.mp4?token=Bil0VaKaSJ2XMgXKYUe59kt8UOdheoHbe677FJuGYR-CyphzAveoSFrlHRk66FZEaYtDp5GkaIYhLeWf_bXIj2S43ldI5E0xPLxvmqsOjOlpXZYeyz3vmzlNTcFcDAZ2GmIunMgDrOn18yLkviJtQpZUqn1P39Y0WYl73wj3rxr0D-PTEjvz2OUwOufpva6P37fbNbN-ZtusAVwqH9R0y8h4ZvQc1f6hoX7Ax_ZRRiZwUbldMfk3MOP0W7tLmc7NtbpS79m6zYdEQI7-Ujo2bCMtjqbT1fdpdCvI1CUlROApFbI9hOooLoydGyPcxKjbwNoPeuiOKK7iPtE3lu1VBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd01d1fb90.mp4?token=Bil0VaKaSJ2XMgXKYUe59kt8UOdheoHbe677FJuGYR-CyphzAveoSFrlHRk66FZEaYtDp5GkaIYhLeWf_bXIj2S43ldI5E0xPLxvmqsOjOlpXZYeyz3vmzlNTcFcDAZ2GmIunMgDrOn18yLkviJtQpZUqn1P39Y0WYl73wj3rxr0D-PTEjvz2OUwOufpva6P37fbNbN-ZtusAVwqH9R0y8h4ZvQc1f6hoX7Ax_ZRRiZwUbldMfk3MOP0W7tLmc7NtbpS79m6zYdEQI7-Ujo2bCMtjqbT1fdpdCvI1CUlROApFbI9hOooLoydGyPcxKjbwNoPeuiOKK7iPtE3lu1VBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازگشت پرندگان مهاجر به جزایر دریاچهٔ ارومیه  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/438664" target="_blank">📅 21:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438663">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXzMoj1kNukoMAeQ0-Jk1PmwVHZtk82m3s9yCdu4vqexDJnXDbxQnEZK_GrP9UzO4XBaV8zZ7CHw786cHcYHTJ0B6wZJlwyo9qthLYAzkCIcF1WfBIBglAnU-ay65mVIFonJmjmR70SdJPtD9URa2I2q86OQGixNG8edK0kMM7tDEu-kfLAXHk57C-9x7Ay_FlHCUyWI6Q8DGBjfDRv1GceD0Dlr_jgmEI8wsHHqmOpjnVedlcvsg6aoSXHLSp0xNzBU4X9GBamLgrLasfbXhoxy4cqAKkkCmMQfDY5LhuuTxB7WrP-zb5DU-4f39Lac2p7dCRBYTGRmmWE0tF4oig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
گلزار شهدای میناب، میعادگاه جدید عاشقان  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/438663" target="_blank">📅 21:11 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438662">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NnGZdhmSNtgdLP8u62Dx5L2J7-pVO7rYiV-QUSRgdfq_sEIS844VCbtmbwrnGSmv8GLUBm98KrrA6ISxKqTQJqxIAUmYZuYKbOq2njy2w_8AE5dhFHvWVIG2v98HmYjzl_L5du3oemmL74XIdgYc8_g8mYUjjKzknE9f-FPxK4i8A82-jgSvMK-q3PZba8Cv8fo70g2riM3fTxEvBwyZkVpd7vc88VSPQBoR0RaLAtLlBfEwwJDUeuk5WhkYZoDOuf7Y0meKlBY1_E6X4LFfc8VZ-NVkz5LncBA12BDtmk2wjOeDt6dc3D3H1UgdSqeh-KUNSCidzGdagFAjG5fy6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیروزی سه گله ایران مقابل گامبیا
ایران ۳ - ۱ گامبیا
@Sportfars</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/438662" target="_blank">📅 21:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438661">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‌
🔴
بقائی: آنچه آمریکایی‌ها به‌عنوان محاصره دریایی از آن نام می‌برند، از ابتدا یک اقدام غیرقانونی بود؛ هم نقض آتش‌بس بود و هم اخلال در آزادی دریانوردی بین‌المللی.
🔸
باید ببینیم در عمل آیا واقعاً به این حرفشان عمل خواهند کرد یا صرفاً یک ادعای تبلیغاتی است؟…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/438661" target="_blank">📅 20:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438660">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: ما با زبان «باید» ۴۷ سال پیش خداحافظی کردیم؛ هیچ‌کدام از طرف‌های غربی وقتی در مورد جمهوری اسلامی ایران صحبت می‌کنند، نمی‌توانند از زبان «باید» صحبت کنند.
🔸
ما براساس منافع و حقوق ملت ایران خودمان تصمیم می‌گیریم. این یک نکته است. @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/438660" target="_blank">📅 20:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438659">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: تبادل پیام‌ها میان ایران و آمریکا ادامه دارد، ولی تفاهم نهایی نشده است. @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/438659" target="_blank">📅 20:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438658">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwYu_j3VJP5EXbTh5wGuju2YlZuPEGCDuNfC4mtTjEeDbZZf91o9U4giYAYGlU5sCACfa6ciM1bhb3pZzkVB548lbMFEbftY-PDy0grH3EoZl1-TMYItPhWhTfAMQyMJr57kckqK3yYy4py7OVWLQ14c_iGjIUbY8KYQaQzlcHomyRwKblo0dD7Sjvc08uTctukD4vAR6PmIuWdmq8R-eXL3y72irPMOG9e73yrEtqNfOwOM2GkyDctnNw1SjBjqylqc5Cm0kWN1f5x-yqfUw7G5jZj_GnfIn8rdKRn2AP9YkKk2oZIJHJs4MXiMZZq9aOD0Lgg2mBXlg0s9gSyyVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو: عملیات‌های ما محدود به جنوب لبنان نیست و به بیروت هم می‌رسد
🔹
در حالی که دولت لبنان همچنان به مذاکرات مستقیم با رژیم صهیونیستی دلخوش کرده، بنیامین نتانیاهو نخست وزیر رژیم برای اشغال بیروت خط و نشان کشید.
🔹
نتانیاهو به صراحت گفت که عملیات ارتش رژیم صهیونیستی محدود به منطقه جنوب لبنان نخواهد بود، بلکه این عملیات بیروت و منطقه «البقاع» را نیز در بر می‌گیرد.
🔹
وی که نظامیانش با ایستادگی اسطوره‌ای نیروهای حزب الله مواجه شده‌اند، مدعی شد نظامیان صهیونیست از رودخانه لیتانی در لبنان عبور کرده‌اند.
🔹
نخست وزیر اسرائیل با این ادعا که نظامیان رژیم، «بر مواضع استراتژیک مسلط شده‌اند» گفت که صهیونیستها در جبهه البقاع هم فعالیت می‌کنند.
🔹
نتانیاهو بدون هیچ اشاره‌ای به تلفات نظامیان صهیونیست در جنوب لبنان، ادعا کرد: ما حزب‌الله را بی‌وقفه مورد حمله قرار می‌دهیم و عناصر آن‌ها را در هر رویارویی از بین می‌بریم».
🔹
صهیونیستها که به شدت در حال سانسور تلفات خود در جنوب لبنان هستند، اخیرا به هلاکت هفت نفر از نظامیان خود اعتراف کردند.
🔹
حزب الله لبنان در هفته جاری موفق شد دو فرمانده ارشد نیروی هوایی اسرائیل را به کام مرگ بکشاند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/438658" target="_blank">📅 20:47 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438657">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‌ رسانهٔ نزدیک به منابع صهیونیستی و آمریکاییِ آکسیوس مدعی شده که توافق با ایران آتش‌بس با لبنان را نیز شامل می‌شود.   @Farsna</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/438657" target="_blank">📅 20:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438656">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خط-50.pdf</div>
  <div class="tg-doc-extra">3 MB</div>
</div>
<a href="https://t.me/farsna/438656" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خط-49.pdf</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/438656" target="_blank">📅 20:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438655">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdbXA6ntjuerU48Zhp3Glwe0wwhFirarK9BiKy2P7r5qsMpNotj4tCKAZuUaQuZt-8L59nWQic3BDRx0yQUkewB4HkPoafpuAUkYQCwaeQlULNnvbyhRHtnEpQ3ZiH-c1KD3xOM8wTXEB3RNHxOL7leipYPJpw3OuEr7YDX8kTmMFJQ2A8GI4dQaFTMi5Am_nnrIN1b5Tr41kkeAg2pn2LF5osnHEra2T-TPu4Jo4uoyzX-beX0kElbY93mSIVpNUwhozbZgbewMZGcChvzxaiDNOWvtaLUTQYSwz-H2MO-t5DxNNYWdbFrJdGJRFG4Ov0m0sYNkzTbADVU4GXBtaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جبلی: استقامت و اقتدار، میراثِ رهبر شهید انقلاب برای ملت است
🔹
اقتداری که در این جنگ به دست آوردیم، ثمره خون رهبر شهید انقلاب، ثمره تعلیم ایشان و حاصل تربیتی است که این ملت را مبعوث کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/438655" target="_blank">📅 20:35 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438654">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPSegxBb2B5moye2-TREwnbl_tBsRhumOO1flxAopUkmMDlDYWIigQWnjyXkUfJWrVfB6BaT-FkSrxzgSnNQpjAoKXMl3Hu5AZ8k8tWDyYtujWTvHvYlRjSzWsCKA-dBl7fYnvHphstugcEW77fc5kxM3sqfqK97dPoZSDDVK__H6VZ1w4L7Imb5QjBvK3YY9GLT7eH1CwZMdJtXexza16RGBxJYE-FrhEXjeZjfuSIYxRxtR6xcHx2zlMoryUMGBBDHk5LBgL865usU9iBMQ8i8ECN2ZuSsbBDvUPwB4zUyoZwXG_qoT9MiFbiqftmkkpDF7lUiPje1neyRoKplPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تشکیل ستاد برای برگزاری مراسم تشییع رهبر شهید انقلاب
🔹
رئیس شورای هماهنگی تبلیغات اسلامی استان تهران: ستاد ویژه‌‌ای برای آماده‌سازی شرایط یک تشییع ده‌ها میلیونی برای قائد شهید امت تشکیل شده و مجموعه‌های مختلف در حال انجام هماهنگی‌ها برای برگزاری باشکوه این مراسم در موعدی که مشخص خواهد شد، هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/438654" target="_blank">📅 20:24 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438653">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90312f5aeb.mp4?token=KpEZBIbXqzCdXVUzPaYTnYwtxc4SME8_C_ls_KmjO1eXsmWJIWuAKJvikzAvXcH2C2n7U6QlmW88kxxhYkTfdYG_zX66YdxwtpIYAEsw1-lHkSHSyiucs2Py8463m7WsrQb3ERHka0n9NQeWTqj2Cai5UH04IvhhN-Z6fVKWA9gGtKX2I2CFTgaHyg3x9GAg4DHvc7XUe5G1kllybQMP68tY9blMctaYpVGFg5E98jJsx0ClDnUiHnvf0R82DjxOVexsyH1Ji6CfBgaOJXK14Ne7qFrIGQi2EBmhXo9Cj4yw_1IplesF9jJRYzHg9tgcey3mRwfaXt8PuFKPkn7uSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90312f5aeb.mp4?token=KpEZBIbXqzCdXVUzPaYTnYwtxc4SME8_C_ls_KmjO1eXsmWJIWuAKJvikzAvXcH2C2n7U6QlmW88kxxhYkTfdYG_zX66YdxwtpIYAEsw1-lHkSHSyiucs2Py8463m7WsrQb3ERHka0n9NQeWTqj2Cai5UH04IvhhN-Z6fVKWA9gGtKX2I2CFTgaHyg3x9GAg4DHvc7XUe5G1kllybQMP68tY9blMctaYpVGFg5E98jJsx0ClDnUiHnvf0R82DjxOVexsyH1Ji6CfBgaOJXK14Ne7qFrIGQi2EBmhXo9Cj4yw_1IplesF9jJRYzHg9tgcey3mRwfaXt8PuFKPkn7uSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول ایران به گامبیا
🔹
آریا یوسفی در دقیقه ۴۷ این بازی اولین گل ملی‌ خود را زد.
ایران ۱ - ۱ گامبیا
@Sportfars</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/438653" target="_blank">📅 20:17 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438652">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‌
🔴
حزب‌الله: ۳ تانک مرکاوا در شهر «یحمر الشقیف» مورد اصابت قطعی پهپادهای انتحاری ابابیل قرار گرفت.  @Farsna</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/438652" target="_blank">📅 20:17 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438645">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RbEJfb-saiKEtDIFnFLQ0cGUDHhvUzRO4wjP1UWwzMgonWoCtF47omMECAN71sRmATjNp1RTlQSnvp2zNVcU1L7i8yGXp5LqpdcexrtWBavrj9hf5DZ-LDEWYSEtrWF7-3MrbVg8jdT0fiK_HOcJPVyhWIO5DaJ3-8GyERy2K7lI12Gujsw_qAQjaP2fRdSZYv7_KeNGQd66Zhd9hZcj-rS0kB94F78Am_AdKb-otzQbc5lPWd7tyrZVuVcW2Nz6nJL9T9tKixUuHPbQ1eDbrhQVNxIh4tPT4-xEarM7k9k_EtznKft4yOvwps2ZgpJwMCIvnov3dnNnWIggMKJSJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hJVzRuA1rmG-OdgL36Zr4TA9cmx91_lyPOMWSLk9Yyv2-EKt_Ri2UkcVV0LhyAPqetrqs0sXFnZAkn2Y5pTsStGn04D52cGsUVctaQlYLXZOapPaQyUCH18ppxN36kFyAbENDGB02uVy2zNfRQ49rVC9w4L90buuWsa87MZJZtxJox7H_7m6NSIHDdwNfoNRxX5aVxUSPREvUxlR32VPOHet5WIHekrMWl_QSfvYLZNhdfcU-kBu7OHZuOcsk0wzrWTxhcjL5xk6Ia__lMOy7UOCgsSj3fQ7mPnyNfjIX9tVkKNreGejtmxg5sOB7Yr0kLi4IB_SYK7BoxwHJaGCcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q878ufrD1zD6KDKwxWo3XfcEmrKOjFlEtiTTOjKTFyveEgINLSs2bI5A_ek-LL3I3uMHgu_RJRo96gadoYD3UAtmV6nGStNPLTj0VhcoJbxgHIOFtdYltLCVRmDh2cgoMDb9S9XedMySOjU2NfofHKSditEQzPLa8mczbl1Fh-hxb2sRClvD4-4TwKCIE7-mMgfamS1Jny2-1B-Pyt_1199U4xE-8Ie3sOBPnEUFlAG5xFHfAQp5-r3nOq--S3XpV-etyekiuWMLMzQ_f1Z8NFAb0Xp_t2UwvgI7iPR2rOSeVjn6tKrRXzDGk0qNKT9aB5wTyTRWWL89aoisx6YhNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J0hCPfkAdDd3xf1BuqMzJ6uG8qCb8C-Kf-shi59Q-hzOPDceE11ZGHICyD5WRLdUGlkIFBa5Mvvw-n7IrkhsPKxSO6Cebvq9LQb8cRlpcatNp3aS46m1_zg6ObH4z2DEcazwwjuH32jXfNAIz3ciHm_RsVm4vRLq6s5NnBoheGzWCTQzWrni7h-cIsq_Ifoki2i6yAyg2vFVqAleGWONOnJz42ITxGFjfOYI3JqhTqqjnHPLPyF9qwgp5MeblilNmRqnF8PWiZ_0JAwLbr4lTj5S14rX8vz6NKYkZxsQgQ_eUt_SrU2u-Ka0oQnxx__Vc_wc4tLLAvjhGX4HFla-9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P52thu3rnzkuPLrAyeZw3ahIhjHdRp_WhirdQsoQDztisU3lGiVBz_TZLWr03Z7he5Pza16uiEL5YKvXuHEp9r8IuZpecIW85WCrrRVc9Qao019e04FFZ3K74Kd3cSjT_yPL2h9C0_dXisGmdm1gah3HPhqYs3aRE_11GXoQlPxYTckVeKxhUHUPSmj0xgAVSEaS7sp-ETyN68RkV_zWAoKeheNC88hOsldoeY5UxTwSY3gGm-rfwzCeQniyDtavEpCIYQRKWBcBgosZZGQgto3DIuSe6MZZBttUF_OdFoqiJHc0mgzKy8_5W3u8XeWMV3HMAw0s0bNSOkC--SLpqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YyBdyPEHK3e2pMRW3wSF_EFSUr9bADZ5dwjJTgXAkN-woE4wnZgticJhqa5v9triBM-irH8JMF7gZJWeNSl7H45QT5I7VMacduTVJffry61NqSrG222p2kb7eSBnGU-h5VhF_YbJ7S2j9mpy1qFShwj6xxunlllTq0hdBQwlS2lkhmb6Rsg0QFYk0Y5vYAp3qhh-ypbrnINyZ2jd45XDbZL_GPmlHrvriUcev-ImEfJ7i8mQGOzkkLlu-7CQ2Y5phl2Cv5dNWzQiytX8BEuTiukgnT09l6HV3Kl5lnaRpiZvtEK6d3BQZgZEYzCC1Zjv290O0SUZ0rqCn1g_k3U1rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rA6l0UgSnH3XDgBkomXWhRejEInFbJQdAS3n_cKgx_VYLuLnkC8TC5GujgI3eOranOTyv60BqpiZ1eNypDDFtapSQ_yiImsWBun1cuqLiVlGsP6lafnpSxg4yrD7ZhbuLL8LQsLW3TaMv7RGvUHFddl99O0eiG_WvJZSPWXtN6D1yPzMuVgB4mKMavW6d6BhBYMQu4YXpuojKQ7Bo3p0M-dyVSrBwq8JMdIt2oFSGEBDe2TRvcY_bvTsSeB45OPEhJ7DVDZHF4uFx1Q-g4bPQ9ckuYyj2sM00E8ok72OzwQujEpLGjTO2WmOES1iUL0tKBwOoaieRHYNwP0Didub9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بزرگ‌ترین پلِ معلقِ خاورمیانه در مشگین‌شهر
عکس:
حسین حسین زاده
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/438645" target="_blank">📅 20:11 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438644">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ادعای آکسیوس: خبری از جزئیات هسته‌ای در متن نیست ولی ایران تعهد شفاهی داد!
🔹
رسانه آکسیوس، نزدیک به دونالد ترامپ، رئیس جمهور آمریکا، به نقل از مقامهای آمریکایی مدعی شده است که از ایران درباره برنامه و مواد هسته ای «تعهدات شفاهی» دریافت کرده است.
🔹
این ادعا…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/438644" target="_blank">📅 20:10 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438642">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ادعای آکسیوس: خبری از جزئیات هسته‌ای در متن نیست ولی ایران تعهد شفاهی داد!
🔹
رسانه آکسیوس، نزدیک به دونالد ترامپ، رئیس جمهور آمریکا، به نقل از مقامهای آمریکایی مدعی شده است که از ایران درباره برنامه و مواد هسته ای «تعهدات شفاهی» دریافت کرده است.
🔹
این ادعا…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/438642" target="_blank">📅 19:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438641">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">آزادراه‌های قزوین زیر بار ترافیک پرحجم و نیمه سنگین
🔹
پلیس راه قزوین: ترافیک در آزادراه قزوین_زنجان، محدوده کنارگذر قبل از عوارضی‌ها و در آزادراه قزوین_کرج از عوارضی شمال تا محمدیه نیمه‌سنگین است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/438641" target="_blank">📅 19:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438639">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ادعای آکسیوس: خبری از جزئیات هسته‌ای در متن نیست ولی ایران تعهد شفاهی داد!
🔹
رسانه آکسیوس، نزدیک به دونالد ترامپ، رئیس جمهور آمریکا، به نقل از مقامهای آمریکایی مدعی شده است که از ایران درباره برنامه و مواد هسته ای «تعهدات شفاهی» دریافت کرده است.
🔹
این ادعا در حالی مطرح میشود که ناظران معتقدند آکسیوس در آستانه انتشار متن یادداشت تفاهمی قرار دارد که به نظر نمیرسد محتوای قانع کننده ای برای پوشش ادعاهای پیشین ترامپ داشته باشد. در چنین شرایطی، طرح موضوع «تعهدات شفاهی» از سوی ایران، بیشتر به تلاشی برای جبران خلأ محتوایی یادداشت تفاهم و جلوگیری از نمایان شدن بزرگنمایی های گذشته شباهت دارد.
🔹
بررسی الگوی رفتاری ترامپ نشان میدهد که رویکرد او همواره مبتنی بر ادعاهای پرشتاب در فضای مجازی و اظهارات بلندپروازانه در انظار عمومی، و سپس عقبنشینی در پشت صحنه بوده است. پیشتر نیز مقامهای آمریکایی با واسطه به ایران پیغام داده بودند که نباید به توئیتهای ترامپ توجه عملیاتی کرد.
🔹
اکنون چنین به نظر می رسد که با توجه به فاصله زیاد ادعاهای اولیه ترامپ با متن یادداشت تفاهم، تیم ترامپ در صدد است با مطرح کردن ادعای تعهدات شفاهی از ایران، از فضاسازی سیاسی و اغراق های پیشین خود عقب ننشیند و اینگونه القا کند که در مذاکرات اهدافش حاصل شده است.
🔹
منابع مطلع می گویند انتشار متن یادداشت تفاهم، با درخواستهای پانزده بندیِ اولیه ترامپ به قدری فاصله دارد که روایتهای طرفداران ترامپ هم نمی تواند آن را توجیه کند.
🔸
لازم به ذکر است ایران هنوز تصمیمی برای رد یا تأیید آخرین پیش‌نویس ردو‌بدل‌شده یاداشت تفاهم نگرفته نکرده است.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/438639" target="_blank">📅 19:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438637">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oIDFrvzhSkLOHai0ey63sYJKJZX29jNF09dmrrjfpJkwh9R49UR64HySuRSXrQ5_Ep69unN2CVYGQ9DG74qqEk8aziaQqCmhjD2_OUD3GySuqwADajwb_LDhKiaNphb9Wc4Qthd1Tl9TWaZ8vTVIC3hZ26Bg3iwjhoRL2cG_TD2QIn1Y3ILFTzA9PwjuNMo5_mt33QEnNN5mBYf9BwbpBS8ZtWF-Ee8xFTvbhO5gyoNByIHijv8Pfq7O-iP_4fZw1-KwRXn4O499efRWwAv6t6JkgnBPqnPNWVaJTwCNV9P_MVP5SK2eDQ2aS2EwcCwAOWcOWCYfaLUzPN4KG0y0Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر کشاورزی: در ۳ماه اخیر هیچ برداشتی از ذخایر راهبردی نشده است
🔹
در ۳ ماه گذشته با مدیریت هوشمندانه بازار حتی یک کیلوگرم از ذخایر راهبردی برداشت نشده و روند واردات نیز بدون کاهش نسبت به برنامه پیش‌بینی شده، تداوم یافته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/438637" target="_blank">📅 19:24 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438636">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ باز هم خواسته‌های خود از ایران را فهرست کرد   رئيس‌جمهور آمریکا در تروث‌سوشال نوشت:   ایران باید بپذیرد که هرگز سلاح هسته‌ای یا بمب اتمی نخواهد داشت. تنگه هرمز باید فوراً برای تردد بی‌قیدوشرط کشتی‌ها در هر دو جهت باز شود، بدون هیچ عوارضی.
🔹
تمام مین‌های…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/438636" target="_blank">📅 19:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438631">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UUilRszRWTs-ImBw_EPv4OVR-AD44hL8yUDOpAd6oxWIYS-nZDbNa3CNdaTBsRr4wHBW0118x62qSPAjjISSETcAu917qTBc2wDeNkTr2btzDxUc6XS_CmoLzTOKjkCF9niQpYIb4_CScXCzgO2D0FhEv-QEwP75dFytZK_lDZsF9DGP_ugYumoYYK4iCXoq9-AFn3ngHVl9ee-rZ11FA_-PtTxeZFuBhd17rUKdOU5Ar0v8VkW3PimtVWdru7HcIskSdBMKdAKGSS022iD5uwlRncD9Y652fOhtyfIeJBMQG2-goKoD2IAIpQ6l_Ufthz3JLkrRah51cRjK0VdHFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JBPcIT1F5MrPeLqnOJtA2vVRBAlk2VWJelCBJimIGu-ceO9uiNGaQJawqxLLbe5UDX1vURawZIayGAOfgfy5E_Fkev6dwV5XwT0xRHrw4Pe-nA0x5vcLyul5PY_flgFp-b67J_EpsRfGDR8YOnaHuVhFMgDdf3u-7zKS92kP4k63MsPJXcED8cWVxlDDArkyj-Yo6ByqqO-AUtsqUrDcLdL1bBC03AGNukOIGVJqUANSg66Y4SoJReGH9k2bTKt1bLOrpYQi18h_QBtujbPMd0A0qKFO2UqStMrcgWdqzDmpFnPTl8roPVw6i9__YnJ1RnGI8k40v92HH-RpAVFMbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DFwIJMLbNFQ2WXcTWgjMWA-iwl9ZeHaGrTJZlpy_n2cetRYJDWAkMnvw0Hr-3ldz9haK9dZjp3BGqbMOEJ5XDILBT-vw_rnyDA1OJDgSdCfEe1hrE_I-SvJ9VAJGXGrKmTdazqWMoJmvPb0Xw3RM9oAecx3psLfZKSfa7oAuMXWnJZo4qb59O4psZe8tYpfJuVY6uQW5mDUU5IP2kPtyI_KZbEB1ZZvYOd2XAO68sPM2N_I_zbNRlE7_5k7mOzy8RnsCjuzczf4cY3J-i3cu6bYJQzMes3RspelxPQYTcfgjR3o5XVzhJWJ1Plf-XCBqoEhUjqoeBPko6A6BT9NL9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NT6s_-7ZidwYJ5mB022RNOpdRHM-L4UKY9EGYxfTwP3TvyMc5B0I0yOmz4Db75nqzmOzSRz4lalWyGXZIIVwMVIBqzhWVJztR9oBuU09K1dcd86rRemE5C658D8r6LSm-W8rtQbq5wJ4pz1nj-mepMwPfV1ZkyVfszck0w-fhGUcbuKfnKTph0_vH1ob4o0879KAdqkwkCYKGaRDWpgErp3eRc3ktojsZRbfv50V13asBuOLsMjsJn5ShbTw3AD1CRb3Rq5z-SjQnOQNplivULG_96soZtKB06bbsmo0Azc4yikgWYa_e1Hmhyr4Z6zCq-5zjMxrAEWqrRyOoIsKpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SOD1Vc6fAqwxXRLc9LsX7yCdWrG8qsDWBRFSSZSvMtLNVjLg7_CC8QjPVid_xSk8ugzHuTVIjMPEsOwG3iDDeRH7HFyrbT5gT-I6zu-suy_waECuwlRY57wgNBwnA47XCRSGSVJWp8HDA94vgsO1JaqI8KR3vqhckwo2mXFb0Qgi7tsTsxxvmyycrTWllSENovvy3WGIcT_HxDi4A9tzlzP3fNdzBUberFoOKw3AGW_a8Fy5VNYeVbmMh4hEwXo9YOGp4zbaathME7tMhNuTt5HNIZARlT3YHUY1nXx6kHkNNEOMpax1jVYMDi-7Q1q6U6tO6Rn9_zXgsR2kjuMu5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشنواره فتیر مَسکه در بجنورد
عکس :
رضا خبازان
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/438631" target="_blank">📅 19:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438630">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jam_xWfppqXSX-7lQV_FIcqJcP83Z8yxVLbVZ-VHc3gMwt_3d-DtfDx2fuxaw3MnKGwliTss_b2thl4kRAqOwpnxsKO7fug_9cUGbPWMNxtjQO_cvC1wXsYgimRdlFCT41r71ymftmS-sCRqbfivSGBc_ibDH30A2qf1dD7vrDZGmY1lt7F6VTOeLcVILvXPtkQ-jqxDvqvIpG9COkcTAQQEMuFCqkzGwIz_19aA6XQQQrMcIHqT0c6HfV2AVwEZPo4_pfwJDpKCawA8kBmfw8QbGTWr7Kau7EMn3ljWwHJYS-Zb86lWulhs-ed1TYC-fQpdwOtQsy1hSMtIQesJHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم: رویکرد ما برگزاری حضوری کلاس‌ها و آزمون‌ها است
🔹
سیمایی صراف: هنوز شرایط نهایی اعلام نشده است و لازم است ابتدا وضعیت عمومی کشور روشن‌تر شود تا بتوان در خصوص جزئیات و نحوهٔ دقیق برگزاری آزمون‌ها تصمیم‌گیری و اطلاع‌رسانی کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/438630" target="_blank">📅 18:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438629">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🎥
تصاویر انهدام ۲ تانک مرکاوا توسط پهپادهای انتحاری حزب‌الله  @Farsna</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/438629" target="_blank">📅 18:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438628">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlE43ZzXmJcg0DM-LlhXXYGI1DKnfyHDaMfemcXmEJ4yPq5Iwi5sBlogKnTN1WrvbTrVl0gQ4ADN7KfAxBnDKf8KEq_n53aHrBJcZgQjYXMaQvOI0lwG5dfhdkAE2AFuZ_5m-2NdjHyOpWNFQOlNdIsYmGHp7UTnTru0s2m7eDaVT2nHPqIezcO9r4MCm5xRXBbJPPQvZPjQQEqV40UUnwVc_4AqKXuju8ENbm7TGf25kEbSwL7rpRsDcR1tLSZlHP1_s549s_7wN4Jj7rA-gP120nEXTfD8pHXx-GdWcHY13DLUmcEIGXMHX7QoRwSHohchyGUfjPzegx_-jti9jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مخبر: حفظ انسجام ملی مهم‌ترین پشتوانهٔ کشور در برابر تهدیدهاست
🔹
محمد مخبر مشاور رهبر انقلاب: در صورتی که انسجام ملی حفظ شود، هیچ تهدید و توطئه‌ای نخواهد توانست کشور را با آسیب جدی مواجه کند و ملت ایران می‌تواند همانند گذشته، با سربلندی از دشواری‌ها و بحران‌ها عبور کند.
🔹
حفظ و تقویت این همبستگی، نیازمند همراهی همه‌جانبهٔ مردم، مسئولان و نهادهای مختلف است؛ این وحدت، سرمایه‌ای ارزشمند و ماندگار برای کشور به شمار می‌رود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/438628" target="_blank">📅 18:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438627">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4535660a4.mp4?token=Dw-N09njJ_6U8aZdRGLn-zSILipATIHhf8PdHyzpwmGtQp9KNxgEzK7v6hNoLU-XeL1RbeIA9hgfqEEjABwOfA1sTXswgUQgSj6gKQv30W0vninpE24vZUk8lpMmlRle2QUVevOdl73Z1jt9OoqFXsxeIjQNiczHKg6Qg4YNoVBN9LY3wZMP3iYDVggMHgqirIlN2kY8X71uxiYw3IsCaZOtd6S60ErGtLxLnwtN404AZqSTOKkf5INeqvbjDIAq8Z2RYj3pLYSjKLp0x6hfbfu4K9dXGgd5brUbO_LeKzaIywkn5hDemMnHHfRT6FnEC4sDl-ISfWoFS7IpAJ1Bf7SlRIEerLd1XR-2cQa_2awJsyhffEFjBh9pYEMnTvsiKqVtvF9EXnjnrzDMte5RXvn59RF2tc-0vIb-6Xru-cmzTBmrKUsFtAh8HiKS_1W24mZ99QiGt1OfxpKry-7SUCadCwuJEGppGBLcmoG0U1ApTk8j-eGz3UHX2-F2HKDvAhbQaFVyGg1Hu6qOkiSM7PXsy-Iy5NCYOlvw7cylyLKAMHueNQjVH_-2Hb_rdybAWvnxyWg7iKuNP15CmuRXlWuDdMKO0tqB611njsSnwitkQ2FWuH6mRG6of4GFcLyHIoUeRgixbAyKL4Roe1P1phqqqi6ZxWJ2_8FWZ7As3nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4535660a4.mp4?token=Dw-N09njJ_6U8aZdRGLn-zSILipATIHhf8PdHyzpwmGtQp9KNxgEzK7v6hNoLU-XeL1RbeIA9hgfqEEjABwOfA1sTXswgUQgSj6gKQv30W0vninpE24vZUk8lpMmlRle2QUVevOdl73Z1jt9OoqFXsxeIjQNiczHKg6Qg4YNoVBN9LY3wZMP3iYDVggMHgqirIlN2kY8X71uxiYw3IsCaZOtd6S60ErGtLxLnwtN404AZqSTOKkf5INeqvbjDIAq8Z2RYj3pLYSjKLp0x6hfbfu4K9dXGgd5brUbO_LeKzaIywkn5hDemMnHHfRT6FnEC4sDl-ISfWoFS7IpAJ1Bf7SlRIEerLd1XR-2cQa_2awJsyhffEFjBh9pYEMnTvsiKqVtvF9EXnjnrzDMte5RXvn59RF2tc-0vIb-6Xru-cmzTBmrKUsFtAh8HiKS_1W24mZ99QiGt1OfxpKry-7SUCadCwuJEGppGBLcmoG0U1ApTk8j-eGz3UHX2-F2HKDvAhbQaFVyGg1Hu6qOkiSM7PXsy-Iy5NCYOlvw7cylyLKAMHueNQjVH_-2Hb_rdybAWvnxyWg7iKuNP15CmuRXlWuDdMKO0tqB611njsSnwitkQ2FWuH6mRG6of4GFcLyHIoUeRgixbAyKL4Roe1P1phqqqi6ZxWJ2_8FWZ7As3nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
راز یک ذکر که رهبر انقلاب به آن اشاره کردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/438627" target="_blank">📅 18:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438625">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">ترامپ باز هم خواسته‌های خود از ایران را فهرست کرد
رئيس‌جمهور آمریکا در تروث‌سوشال نوشت:
ایران باید بپذیرد که هرگز سلاح هسته‌ای یا بمب اتمی نخواهد داشت. تنگه هرمز باید فوراً برای تردد بی‌قیدوشرط کشتی‌ها در هر دو جهت باز شود، بدون هیچ عوارضی.
🔹
تمام مین‌های دریایی (بمب‌ها)، اگر وجود داشته باشند، خنثی خواهند شد (ما مین‌های زیادی از این قبیل را با مین‌روب‌های بزرگ زیرآبی فوق‌العاده خود منهدم کرده‌ایم. ایران خنثی‌سازی و/یا انفجار فوری هر مین باقی‌مانده را انجام خواهد داد – که تعدادشان زیاد نخواهد بود!).
🔹
کشتی‌هایی که به دلیل محاصره دریایی شگفت‌انگیز و بی‌سابقه ما – که اکنون برداشته خواهد شد – در تنگه گیر افتاده‌اند، می‌توانند روند «بازگشت به خانه» را آغاز کنند! از طرف من، رئیس‌جمهور محبوبتان، به همسران، شوهران، پدر و مادر و خانواده‌هایتان سلام برسانید!
🔹
مواد غنی‌شده، که گاهی «غبار هسته‌ای» نامیده می‌شود و عمیقاً زیر زمین دفن شده و تقریباً کوه‌های فرو ریخته‌ای – ناشی از حمله قدرتمند بمب‌افکن B2 ما در ۱۱ ماه پیش – روی آن قرار دارد، توسط ایالات متحده (که توافق شده تنها کشوری است که همراه با چین توانایی مکانیکی انجام این کار را دارد) با هماهنگی و همکاری نزدیک با جمهوری اسلامی ایران و آژانس بین‌المللی انرژی اتمی بیرون آورده و نابود خواهد شد.
🔹
هیچ پولی تا اطلاع ثانوی مبادله نخواهد شد. موارد دیگر که اهمیت بسیار کمتری دارند، مورد توافق قرار گرفته‌اند. من اکنون در اتاق جنگ جلسه خواهم داشت تا تصمیم نهایی را بگیرم. از توجه شما به این موضوع سپاسگزارم!
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/438625" target="_blank">📅 18:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438624">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9555b5f01.mp4?token=X8gIiH_vI_9Sc3AyouPFGDSFSXIu1SRWK5CVBpKYMnTGAdlxHBozUcfdREGI5ZRejmGnXEAfNKMEe1lebqfAxOm3VVhL8CUw7uhrT0FYnPdBXgZJatuuLaO6HyKxrxpscymC_Ksd-DcLqp2-deA9M29CaQ-Bt2GaoTKE5ypOJTVJ3cdeZAc7SGnf2B0K2T7CX2w_1cpQ0C2u5Wk_V3m53xKH_Er_3YuxSEazOZibU2waMILizWP_TUa6VWRp_Uy_HdtK30NEJ7Nec6gwXcC0qLZBMqBSaDL0WNZAELINVhSviJQr-4XLg5JBScjS92O4zfcBvuybGbyKRAr9AM6KNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9555b5f01.mp4?token=X8gIiH_vI_9Sc3AyouPFGDSFSXIu1SRWK5CVBpKYMnTGAdlxHBozUcfdREGI5ZRejmGnXEAfNKMEe1lebqfAxOm3VVhL8CUw7uhrT0FYnPdBXgZJatuuLaO6HyKxrxpscymC_Ksd-DcLqp2-deA9M29CaQ-Bt2GaoTKE5ypOJTVJ3cdeZAc7SGnf2B0K2T7CX2w_1cpQ0C2u5Wk_V3m53xKH_Er_3YuxSEazOZibU2waMILizWP_TUa6VWRp_Uy_HdtK30NEJ7Nec6gwXcC0qLZBMqBSaDL0WNZAELINVhSviJQr-4XLg5JBScjS92O4zfcBvuybGbyKRAr9AM6KNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
راهت ادامه دارد، این پرچم پابرجاست
🔹
نوحه‌خوانی سیدمحمود علوی در دومین روز از مراسم یادبود شهدای خانواده امام شهید و رهبر معظم انقلاب  @Farsna</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/438624" target="_blank">📅 18:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438623">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxqCwwfJ9vYhzPq48xYe6hiRW0MGR_eLqF_j9vlgba8o-MKF411DVQjsx9Mw9V6iNSVRYaBpAozmah0jfhZZzb4JQo7xjZCAJhih2xFaXbACSXMo0vVlWcksmY6BHwrbj4aG2Exlp8tVY4CgBApsZuIqC4vZKCRadncxOftPQZ8ZxsbC3xdLxzGMKX2FLuUz67Afq7YyyjhDh51ICQKHPrVISc74pZzZ2C9F2IQweDP64I5ZGLb416Hub31sjgBRo97z5YCbJNo7JtumTM09QEK9-yXzvQa4M59DCQX8PnFSiM-ZYCF29kesT05fsiDRsQgPXAjNWmjcD5XgVdeeNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آبفا: حدود نیمی از مشترکان آب خوش‌مصرف هستند
🔹
معاون برنامه‌ریزی آبفای کشور: ۴۸ درصد مشترکان آب خوش مصرف هستند و نزدیک به ۴۶ درصد دیگر مشترکان نیز در بازه مصرف «الگو تا دو برابر الگو» قرار دارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/438623" target="_blank">📅 18:27 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438622">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🎥
نوحه خوانی محمود کریمی برای میهن: به روز سخت بلاها بخند «ای ایران»  @Farsna</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/438622" target="_blank">📅 18:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438621">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRztDbLEjodYderYppCPdOS8EwF-xDSuqkhjpAqfwgEw-GfP1nwACMqZgAQYMd87JFeHGD8bZ32LXur3TmyuHI6MxuCMKqGlU06wcY4N86HUetf96-WDggY76se_Zslp0NwYBoV8Pm2yCJeBcfCM1x_W57McXJue_WdqnJMmGG869B9EXQRw1Tc6zmOIpTwkf2EFl2ba9GUWn3QCP7W_-sJasEJewpBVb4U_t9Uqr0dZZCEgzkRVReN3qG2DLBCkuSRwu2ewdqb8rsnir5oPDb9KnxBeAfhQy6ISatRMY9f862L3G8zy8UTA4TJdFHTKIe-R_r5yuJ7jI4auLbYVVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ترامپ عمان را تهدید کرد
🔹
ترامپ گفت: «تنگه‌ها به روی همه باز خواهند بود و تحت کنترل هیچ کسی نخواهند بود. ما آنها را تحت نظارت خواهیم گرفت.»
🔹
او در ادامه گفت: «عمان هم مثل همه رفتار خواهد کرد یا اینکه ما منفجرشان خواهیم کرد.»  @FarsNewsInt</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/438621" target="_blank">📅 18:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438620">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/866a84959a.mp4?token=jBOJzFuKwwPtmnz2aIhNAl_qI_iiHZ3iunOA56zw-C5C-IJBL4bsPxZvDF1V4SGls76WkXXTQJfeAsWqHIiYkCJwQmvlyadXRaT205aD1sFvWb_0FIg669bBciRArRwDy3LiDsaqJsV-nWwL_hv-qdpiYeNH8rZNsdBFTewLlN4PDKrXjDYWDWf-ewmZZcOGGpp7Dn5kQTPtq1zPcr-BKV80rDuOLCpKgCIvZx6ecj9YdD4acqSs34oD0sWW99U6-FGithBVT65LkXZ1rQtiO_HPrhEoQgg_9w3znRTiCUyhbG-Nphj6FB4ZsOZgF7_mgK3Dv5Obdxs0N8TM6vFgnIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/866a84959a.mp4?token=jBOJzFuKwwPtmnz2aIhNAl_qI_iiHZ3iunOA56zw-C5C-IJBL4bsPxZvDF1V4SGls76WkXXTQJfeAsWqHIiYkCJwQmvlyadXRaT205aD1sFvWb_0FIg669bBciRArRwDy3LiDsaqJsV-nWwL_hv-qdpiYeNH8rZNsdBFTewLlN4PDKrXjDYWDWf-ewmZZcOGGpp7Dn5kQTPtq1zPcr-BKV80rDuOLCpKgCIvZx6ecj9YdD4acqSs34oD0sWW99U6-FGithBVT65LkXZ1rQtiO_HPrhEoQgg_9w3znRTiCUyhbG-Nphj6FB4ZsOZgF7_mgK3Dv5Obdxs0N8TM6vFgnIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر انهدام ۲ تانک مرکاوا توسط پهپادهای انتحاری حزب‌الله
@Farsna</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/438620" target="_blank">📅 18:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438619">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🎥
طنین شعار «لبیک سیدمجتبی» در یادبود شهدای خانوادهٔ امام شهید و رهبر معظم انقلاب اسلامی  @Farsna</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/438619" target="_blank">📅 18:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438618">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcmHJPnJzGDUhV5NlyvAI0n8aWjOb_U8iUx2ka81YaIaVrrOUPIkI0TFGbIj-JdhzJgaE-6RnnE4pw_ecf34DNP_DBEqWzXcTBoGT3JSwI37WDQhGwp-X911BIN-p9a4SD6EIRTIsXsFte4QEwQ1T0wjQLjfO3mr-iNC-LK6vqoeOhAG6GfNG0eCZ7Eyvrp-v2SBjTIyVAU4l31jLV17cfnssancG3sSHPj1ieohIteNMH-VDOJ3A2qus0OeK-S6qn5z6QlsbmStY1O0vu2Awd3reVKESGcR6RCttKI0eh-sd2yW2tCIOalj0_vbE9-dG2kEGUOpf11wt3532ny1bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رانت ۱۳۰۰ شرکت کاغذی در بازار لوازم خانگی
🔹
احسان فدایی، کارشناس صنعت لوازم خانگی:
«انبار کارخانه‌های لوازم خانگی پر از کالاست، اما قیمت‌ها پایین نمی‌آید؛ چون مواد اولیه در بازار آزاد ۳ تا ۵ برابر گران‌تر شده است.»
🔹
پس از حملات دشمن به واحدهای پتروشیمی و فولادی در جنگ رمضان، قیمت لوازم خانگی جهش شدیدی داشته؛ مثلاً قیمت ماشین ظرف‌شویی خارجی در فقط ۲ ماه از ۸۰ میلیون به ۱۸۰ میلیون تومان رسیده است.
🔹
این در حالی است که وزارت صمت، هرگونه کمبود در زمینه‌ تأمین مواد پتروشیمی و فولادی را رد می‌کند.
🔸
به‌گفته فدایی، درحالی‌که فقط حدود ۳۰۰ تولیدکننده واقعی لوازم خانگی در کشور فعال‌اند، ۱۶۰۰ واحد از وزارت صمت مجوز گرفته‌اند.
🔸
بسیاری از این شرکت‌ها خط تولید ندارند و فقط مواد اولیه را از بورس کالا می‌خرند و در بازار آزاد می‌فروشند؛ اتفاقی که باعث شده تولیدکننده واقعی، مواد اولیه را چند برابر گران‌تر تهیه کند.
نتیجه چه می‌شود؟
🔹
تولیدکنندگان اصلی ناچار می‌شوند کسری مواد اولیه‌ خود را با چند برابر قیمت از شرکت‌های کاغذی تهیه کنند.
عکس: رسول شجاعی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/438618" target="_blank">📅 17:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438617">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed853f6f00.mp4?token=YQYbkbodRJkFTDs12Djv3ptTcnTiIzK4ljC8qizg7QjVgyM9M1ERPkTwSbWz5AyZbK6Mj2CBLjSkvsuej3bgCHdg_xirk3Oz0krzxCNYfKcENV0BBg8Jg6U1ndEE6hxETKsl47BYeIPhYqtc9GncLmaIkp2eNMqhVEW03jEjmBg0Qf6A0LG9y_dpfSp-9Tq4WSgtvtsoxD2j28JZgc84nAzJuDdWu4n1wFMokS-s-MaoM5hgwAeSXWpcLadNPAkoWS22kXxtqHQh3mfBwhi9FevJLh8Eu_c-_BPltFQkS7_AujRJ21-echVhgz9nC9p6_JsHrhPqCTTuOBdcedP-uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed853f6f00.mp4?token=YQYbkbodRJkFTDs12Djv3ptTcnTiIzK4ljC8qizg7QjVgyM9M1ERPkTwSbWz5AyZbK6Mj2CBLjSkvsuej3bgCHdg_xirk3Oz0krzxCNYfKcENV0BBg8Jg6U1ndEE6hxETKsl47BYeIPhYqtc9GncLmaIkp2eNMqhVEW03jEjmBg0Qf6A0LG9y_dpfSp-9Tq4WSgtvtsoxD2j28JZgc84nAzJuDdWu4n1wFMokS-s-MaoM5hgwAeSXWpcLadNPAkoWS22kXxtqHQh3mfBwhi9FevJLh8Eu_c-_BPltFQkS7_AujRJ21-echVhgz9nC9p6_JsHrhPqCTTuOBdcedP-uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حامد کاشانی: امیدوارم دست قدر قدرت امیرالمومنین علیه‌السلام ما را در برابر صهیون پیروز کند
🔸
دومین روز از مراسم یادبود شهدای خانواده امام شهید و رهبر معظم انقلاب اسلامی در حرم مطهر حضرت عبدالعظیم حسنی(ع)  @Farsna</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/438617" target="_blank">📅 17:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438615">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oI0oIQOjG_J_ICQQhFWerLJrKwNt5u3XNqQvr82_5fPD-KTgsGxQWopJUbJlQODA93UOgvYCyMBxI2Maywaj-f-NmCmPWqTWou5aBtuvUBBFAoTPf_LHUDqyw5zTZHywAPhwCI52z2-JMpDUS6WF01vxEE4RQe8GH-ycw0u5W21DFGFZRCkOlpKAPAsB-smES74xQSZw1DQh6O_c0cpTrMngwNrSIsfSSojrXnoz3tpiPLSyvlg5q9LdA9kLczwM7xtsL_wCr6y6GuhZSBxNquvtUYhnZYLdpFxyom0C4LcR9pkwdD-r8StTEe3-AFIlZjOWM_1YqaPFh9CDnd36CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ مجلس یادبود شهدای خانوادهٔ قائد شهید و رهبر معظم انقلاب
◾️
شهید زهرا حداد عادل
◾️
شهید سیده بشری حسینی خامنه‌ای
◾️
شهید مصباح‌الهدی باقری
◾️
شهید زهرا محمدی گلپایگانی
🔹
جمعه ۸ خرداد؛ از ساعت ۱۶ تا ۱۸
🔹
مصلای حرم حضرت عبدالعظیم حسنی(ع)  @Farsna</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/438615" target="_blank">📅 17:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438612">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuqDXgcBENBZy0sOrHVGu1tdU2bDT29UdwPQEPFQ8EKnOzOe2QF2Y3IBrqVMsttAVRVbVFpUtgwom7zwQx2EnclSWRObFNbGtgSCKgJjS4Qa_LSXRiS7W0pDcmyR0M-mDafiH1yZ_GABLNNcsb5-o9PojYN0dzOxiFrTzjzMXRr1w3loo5hwlFLBmlOI24DAeYlzcB1PQ4vHAGpl9-pjxh4g4Ap2B9oq95Tv9iNLaX__6U6MC-lc_YR-1G75QerUhipdbiQ5Qf9A3VjTHRcvQD6wwDxMtl3urHqK2O2zjBwIuMfHOzA6Pkw5va7bKawVnr0Y05Q7EMoOLViViJiHQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهلت یک‌هفته‌ای برای مرحلهٔ مهم ثبت‌نام کلاس‌ اولی‌ها
🔹
آموزش‌وپرورش: پیش‌ثبت‌نام کلاس اولی‌ها از ابتدای خرداد آغاز شده است و تا ۱۰ تیر ادامه دارد اما برای نوبت‌گیری سنجش سلامت فقط تا ۱۵ خرداد وقت هست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/438612" target="_blank">📅 17:27 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438611">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🎥
حال‌وهوای حرم حضرت عبدالعظیم پیش از مراسم یادبود  @Farsna - Link</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/438611" target="_blank">📅 17:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438610">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dc9478a14.mp4?token=H6ONdpRAd6elHbrADkjtSK6x3Zu7GP4hItc1VZQAAgIMKZ8E-0EtTwHStORL8DMv-DQJ5t_kIx_2Jd7i3IILc92MWhJFjA6OmF-4EMNylCenzwQK3bbgKaSzpOXm5__PPawSUvXYKEa__PMERtiSGlaast8arxSoB9-PZ0kolGceNOuZEm1EU-tqyFtJkoQZkqp-KYQkNgbStkm936TnjKumhK7MU7Qm4hY7cptlmKOhhYs9ijTddLXWlDfDVgIintmZ0Nht29YSPfeUHJVbxZHxmRxJ4niR7USceTfGsZDYCqgOAcWq_QlTvzSLn3sQwGt3bHSFKiceUrUrxOJhOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dc9478a14.mp4?token=H6ONdpRAd6elHbrADkjtSK6x3Zu7GP4hItc1VZQAAgIMKZ8E-0EtTwHStORL8DMv-DQJ5t_kIx_2Jd7i3IILc92MWhJFjA6OmF-4EMNylCenzwQK3bbgKaSzpOXm5__PPawSUvXYKEa__PMERtiSGlaast8arxSoB9-PZ0kolGceNOuZEm1EU-tqyFtJkoQZkqp-KYQkNgbStkm936TnjKumhK7MU7Qm4hY7cptlmKOhhYs9ijTddLXWlDfDVgIintmZ0Nht29YSPfeUHJVbxZHxmRxJ4niR7USceTfGsZDYCqgOAcWq_QlTvzSLn3sQwGt3bHSFKiceUrUrxOJhOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ال‌پی‌جی‌ ایران به پاکستان رسید
🔹
محموله‌های ال‌پی‌جی ایران از طریق خطوط ریلی وارد پاکستان شد.
🔹
نزدیک ۵۰ روز از محاصره دریایی آمریکا می‌گذرد اما ایران از طریق خط آهنی که پارسال افتتاح کرده، به چین نفت صادر می‌کند؛ تعداد قطارهای باری ایران به مقصد چین هم سه برابر شده است.
🔹
حتی پاکستان همان فردای شروع محاصره، مسیری تجاری جدیدی از طریق ایران راه‌اندازی کرد.
🔹
بغداد هم دستور داده تمام گمرک‌های این کشور فعالانه با ایران همکاری کنند.
🔹
حالا درحالی‌که صادرات کالاهای ایرانی به آسیای مرکزی از طریق پاکستان تسهیل شده، این محموله‌های ال‌پی‌جی با تانکر‌های مخصوص وارد این کشور شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/438610" target="_blank">📅 17:16 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438609">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvIBDsXks4fDAkENgrmAA4gD8jcWdfFWOy3uqllJJ6CFhgxiLORTlFxlYRYkpCvMo-1WfZh-SaN0V5rTQIc3tULDYbBDt3pHgAah6yyyHY5WtHcgIwoLD-cF3htD6Q-URKA7BOhWOjXoPed9l5Fh4CN9B-vI78CdcOqHNWpHqOBMbP_sbN0s46aE9fdHN0un1npoRNdzLzIMNkFVIT6YYit024ZHxKxG7FEQsAhg1Bn93FGiBRInGhuqnDb33Sw4nQzPIBTAy8BvOsT9-eqlyeqG6p0DMuMXa4H6aAPfBdyEktmVyFMY6xy_UsVvOeEMxRZS9dxNZQqAcnQqvk-Omw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قهرمانی نوجوانان ایران در کشتی فرنگی آسیا با ۸ مدال رنگارنگ
🔹
در ادامه مسابقات ۳ وزن دوم کشتی فرنگی نوجوانان آسیا در ویتنام  در وزن ۷۱ کیلوگرم، اسماعیل ظاهردوست در فینال ۹-۰ مغلوب بایل نورالیف از قرقیزستان شد و نقره گرفت.
🔹
در وزن ۸۰ کیلوگرم مهدی غلامیان در رده‌بندی مقابل علینور تولیوگالی از  قزاقستان۲-۰ پیروز شد و به مدال برنز دست یافت.
🏆
دیروز هم ۶ طلا برای ایران ضرب شد و با یک نقره و برنز امروز و مجموع ۸ مدال، تیم ملی نوجوانان ما قهرمان رقابت‌ها شد.
@Sportfars</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/438609" target="_blank">📅 17:11 · 08 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/BmCTUcrabdTrpcjKLd0_GrR-Y2ZaWa7NbIXqmXOKND7PTUYW5VVZj_w2fOkGmzFf3v9x78k4QFLdk6xQUf_jUcG0xPqqrH3eHFGhnQCvlR3L2k21QxCQ6rca5-9xBrx-EGMa-GE6uIirPwBGu39ieFmn0PLupRSM7pbxNU3AMlcaJYjF4jfUUzni-lukD5w4HRS0gl-LzRGPMJaJzg1QrknzCgjLkI2oERLxGQphOXp8rYOTbnaiPNKqrhfCdNTdByxP9SvFzj0SGKcj4dOxRWJ4zVlq8L5IkCjSERi0NA25avgrrnqyBA-jNH9c5xvsAXR8lfIIdQfF-wc3tUIvdA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.85M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 08:43:32</div>
<hr>

<div class="tg-post" id="msg-448199">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USfx4oTaxbyDf-4HjRXcgkC-mNzOssiZA6IuKqpxsooDlFacj3WIwX067aq9VPymvIow7O6zz1GkOeYLDyF1-k9u9G4TSiv26wsTkZj5IHTph7kxC2A3t37G6XRE5_o_HiIx_KiGLjzTmfG-6Won5RI4s6gwM3z-bboOTk7DxkA3o_WzddVM181Nw8ebBESbIQtZEePxqvVk_q_yuCnc0DMiLCuACISKy1GsaYflGN7EpchIulalxgSGb0NKB_JahWNfjYSCt26dOVRorEmvo4e5JWb80yez53m5oP3ZqYQrMF8QHEDVGJCKStIxtHNH4IT6O3_tnaOC8Hr_KpXVsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو گروهک منافقین بود، اما حالا در تشییع رهبر شهید اشک می‌ریزد
🔹
«حالم ناجور شد، دوام نیاوردم و با اولین پرواز برگشتم ایران…»؛ این‌ها را زنی می‌گوید که پیش از انقلاب در آمریکا روزگار دیگری داشت...
📎
ماجرای تحول این بانوی ۷۳ ساله را
اینجا
را بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/448199" target="_blank">📅 08:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448197">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FkOy47wc-fMttwOjY210kF-ILQw5QzcNwKtka889SgBktnh_5wUaOgrHnmLLTO6mN4SkizH65OGNVlNEurasVttL3rXxQyMTorUTnB_BFw5OpTevMl0vmsd89q19OZI0a2xPfC0a7YSx45cCAaZCimd_b8Ord05ASA5IAxAx4oSRZWR0XlWMFsXndeMSyPY7D1MZQkiNcU_jDeetyseTeBifbLcPEb-5Kv9AKL6rJm17KltDsjPE_13zxGs2a6F9shF6KUuNksHvzxpv_W7h9DDQDqtyWsOkflB_Xx0sZA0phbb7xC1TlZGAHAzGgvICepaI2yINMjLX48z2HVnSrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">التماس رئیس‌جمهور لبنان به ترامپ برای خارج کردن اسرائیل از این کشور
🔹
رئیس جمهور لبنان شامگاه دیشب ملتمسانه از آمریکا خواست که برای خارج شدن نظامیان صهیونیست از جنوب لبنان، به تل‌آویو فشار بیاورد.
🔹
جوزف عون، که تسلیم‌شدن به آمریکا و اسرائیل را به مقاومت در…</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/farsna/448197" target="_blank">📅 08:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448196">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chgN71gykqYJG-Uvkjomax_W2rBpq51FYRxkJVNSQjBYW7F6VO5KqjvHGtjTKqyrJG9nGsfekXbkFplvZXuQALuzf4K28ilADcYn8fMp9h_b6lCD23HNlsGjzYF217L2G0AYW9-RqlUtfF2WVmfgmqdIgbnEv3OPRw6MUEGeDK4LPjSoeq4g4G5xJt6a0vqAKd-5CfVVG-_G5ZjWWyxcPVx9YmOq4qN36XgnO1MnM0RS3m-jAeCRAXTyQeL3WVCKckrcoJbiE5CGp8-X6VbSXLrStdJfRsYtLUC88r2nmpHxIApjuORwMTqIPfGyMmMQ8eVPx9HnvWCrHsHTwbUQKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قابی از تابوت رهبر شهید انقلاب در مراسم تشییع نجف اشرف
@Farsna</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/farsna/448196" target="_blank">📅 08:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448195">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
پاسخ اولیۀ سپاه به تجاوز آمریکا با هدف قرار دادن ۸۵ نقطه از تاسیسات مهم نظامی آمریکا
🔹
سپاه پاسداران: به دنبال حماسه‌سازی ملت بزرگ ایران در تشییع دشمن شکن و پرشکوه بی‌سابقه یگانه دوران و قائد شهید امت اسلام، رژیم متجاوز آمریکا که روز به روز ابعاد شکستش بیشتر…</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/farsna/448195" target="_blank">📅 08:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448194">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5b86b1890.mp4?token=Kp8QsahTIqSUDK-sibVobhUgYVineg1kgJz8jXJ7_fhhsDTGNZBfRZjonJnvRv3vsn9_AC03M85m6wxgDAuDz5nJNTEIjkJSi07XzATEKk6bjHScWstZdIl-O8n7eeocGtOsB3Jtcxr27s1HoZx4Gc4fKyGj22UQllWpBBaF6YYNLiOxbIjz6oXgQoAluQu0Zpf6xEC-eG1iX8oo-FGSBzNSgNaApMZrNtG8JFELPg-gmFAVMZQQfjGWFxdVuHRFUH7YZsoJl26j-bkzYSpjt6Wkqiy3wrUEstg_4gU_CjDpsBI3DgI4VZFsFDJ1stLQgD7s9oQoarFjQq9Ol6HRMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5b86b1890.mp4?token=Kp8QsahTIqSUDK-sibVobhUgYVineg1kgJz8jXJ7_fhhsDTGNZBfRZjonJnvRv3vsn9_AC03M85m6wxgDAuDz5nJNTEIjkJSi07XzATEKk6bjHScWstZdIl-O8n7eeocGtOsB3Jtcxr27s1HoZx4Gc4fKyGj22UQllWpBBaF6YYNLiOxbIjz6oXgQoAluQu0Zpf6xEC-eG1iX8oo-FGSBzNSgNaApMZrNtG8JFELPg-gmFAVMZQQfjGWFxdVuHRFUH7YZsoJl26j-bkzYSpjt6Wkqiy3wrUEstg_4gU_CjDpsBI3DgI4VZFsFDJ1stLQgD7s9oQoarFjQq9Ol6HRMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ندای لبیک یاحسین(ع) عراقی‌های حاضر در مسیر تشییع پیکر رهبر شهید انقلاب در نجف اشرف
@Farsna</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/farsna/448194" target="_blank">📅 08:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448193">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">◾️
المیادین:
استانداری کربلا حضور ۷ میلیون شرکت‌کننده در مراسم تشییع پیکر رهبر شهید انقلاب را ثبت کرد.
@Farsna</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/farsna/448193" target="_blank">📅 08:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448188">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MORhSp2xPAGqnk2b3ckylnplSt6rgSP5_Tiv3GFIRgCZgsk8VwLvZFnCDYtZcloGD-_onKVbHdayC-yPoz8hQMOCAe4cjMF4SVbB77yK-DP4V4v7P4nv797ibtBe6umP0IqZiU5_DstRAVXPXylsM7oAfy4LNVM-aIulYRPJkn0UvsoVZZDgZlEm77VE40Y0_0GRgj54f89qwr-KH8WRjAOGH5k6x0nYySSKONkPYqSSOxhtEfDIBlLqkzZvCaNZUzs7mDCqcKjxvqE0JOxcxzjDdqMk3KcH2rmn5hCEOFXccVnlbfM8sPU37IX7Dodnzsn5tChOLiSyfj7DcPn9ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UKLIarKs3GLtnu5mnYFFP1zP7S9OK00dYaI1LniSoGy3aPxFosJiIzxdNy622ykbAZkmRcKsk-Y7na_24oIXoKKbvOxWAIO6uUV_Os6AwEKxwIcP5AeOGhZMEMKvNxfsOj6NKUwPrSzFY3wt_7Dn5M2Y_s7jp2v6AHq-orgZR6qKIChnjDpOJKYUSfMfi8BgOBMERWMBiVjaZV66nYW04bcCCGUOv1Y1e7CSOmjJJc0qHTxWCqiM-6_FGz_UtbaA3NVS7vZKu4P5Y7-ZdDQThFAPZATBrV_miOcw8SFHRb-iwZJ1LF7athrJdvgv432nj0JPc4GBXi0M8-ZCHgIYAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SDP3pcaGLFRBvnHqecNpqwUXtO2grDvtJJ5If5kAWDFESRStQ1iamj2HsgJoDIRQi88BFKi-BWzN1CwsZQ122lhLn8VArudGPoitrOehfsd0qegW6oNdRbW-kiOjHAPdN24qNwPt9t19kgHjjTLkBMsLmq-pv4o0usARDTp21opJ9M2jp449wGou5gkafKS_MLWIvp097dHjI8pZTuD4D8PLTntXlLzWPXDU8i_ruo_puNEFc3-X35cGsq52Whnrcx4UrtQkD3NLIlS97cl9AZUYzfCZHFLJxG2BeE5yISdIuVMutxEmc5sjiNlN_l7MROaBr4wfi3Ut4WDhT9QQSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a3TXd9hnu1M1XsuG9ql8A2-WXBtjOpScLAXOjV5HI_n8ukMT9B7rOlT_0TI1B7QBOG30GYyy5v-omgCUF-MQqWx1WhkpS1-wBek5-LjOPZHQGaoQtNrrxibqtIhipB5OJ8u7f9In1ZWLAeYcTfHBlstuNqcjCDWdlJxuYvDCDpZ0hJeVQh7wT6NO5tfHYrGg4TDSO1uyNwp_MKll5TIPsJANK9DBjXBNHeEOrACLxww3nu0V1AQVvxnD9-m9JDdj1N3ofdsetsXI0oeMiStN16ejgviW3kfZnvU6UVlIOgZ8GyWyz7fczssvZKcOUp3OiWzqf6-ZdTtpC1b5fiqtCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TAeEDdoIfZN-vjhp0AkRhz9h-gnp0FNiy0eGmQ0UMi8JHRmwfEzAsoWjR4ihaOyGdf41I9mmVNptLpgHZ1vsI9ULNPKWFgrE6uL9hfN4pQjusjMdXySJQ79ArY-5oqqhnvgLFuKMAa-8m9MosaLQi51lXpl-kOlV5rQDUmJvSRFgguYfcUSM7hvh6O_w1wQZOHA90UNwdtjRrV_3j105vaTHZ5HGToUO2XOZUn7RuUQLjBe59UBB-Vs3EZWQH0GIVYni06se3gLM63itQMjvqrSzN6Oea2n5GNRLGPbgGmuUgMpGamfwGMs-dyIbqk20y04_jYmwBT24lY9o68mihA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سیل جمعیت عراقی‌ها در تشییع پیکر رهبر شهید انقلاب، در نجف اشرف
@Farsna</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/farsna/448188" target="_blank">📅 07:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448187">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9800658183.mp4?token=ncWI-TyQD1PwKzE8E8hEiRV-xcNkIZOuM-_5pd_8VAyCUi1nyXl41HMkF8uw9KwzPJ1tIPe5G9hpEA9H6hjuViyZUaGR-m5552Vn1MidUNI4IY8NkyQdb_OtqEaWUk8d_TzrPZPksdVV41-5mUJ2ZFGzgwhpqxvZ0ehAIXduYkKyPtpNmtVf9xtl4nWgpVJCwVJmaLlOUAXgHfoosSoE4L831Rdg3fHlVHsmgXdqyIQQUJdxTldFIewo0otCGb8kR-Gp_JFVYEqBeScifnTm4nU66K7WytS_42JdyxEI_35Q1ljjj3s2YY6yAtuzwjjyszIhcLoKfIIWigx9aK3ldg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9800658183.mp4?token=ncWI-TyQD1PwKzE8E8hEiRV-xcNkIZOuM-_5pd_8VAyCUi1nyXl41HMkF8uw9KwzPJ1tIPe5G9hpEA9H6hjuViyZUaGR-m5552Vn1MidUNI4IY8NkyQdb_OtqEaWUk8d_TzrPZPksdVV41-5mUJ2ZFGzgwhpqxvZ0ehAIXduYkKyPtpNmtVf9xtl4nWgpVJCwVJmaLlOUAXgHfoosSoE4L831Rdg3fHlVHsmgXdqyIQQUJdxTldFIewo0otCGb8kR-Gp_JFVYEqBeScifnTm4nU66K7WytS_42JdyxEI_35Q1ljjj3s2YY6yAtuzwjjyszIhcLoKfIIWigx9aK3ldg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر مطهر رهبر شهید انقلاب در بین خیل عظیم عزاداران عراقی در مسیر تشییع نجف اشرف  @Farsna</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/farsna/448187" target="_blank">📅 07:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448186">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22d414d1b2.mp4?token=Cb3LS_LaFTkyxv21iSHGZZyG7rSGZwzxlvw60ikilIVJP6YzWDhCWkliApvKORgitKxXeUX26OuCvCbIIUGrwbvmWmdStQ0LgZ7qGhQCyRQaTpAlQCEzZA8KxVpU-ZSsGj6S7tlk_jqldbK7mdNt5MFngQqTS7tglmQlrVZcb9KzCA-tUBlxKSxxWOCR7clzEClKCuC_gehh70NHMAcegv09xmsPPS4wpzVKWLZYyDM5USgWbEMvUYGbknMDSORJaEmr5-OsgJTwYojFFktpC6yx3ozS8Y0trgOf_Jjl3cJ0ObJhJ78MfxRaQPuqeDadsHVfePWNPd0bA5xeSIPYsh3TFruuTmnbapoc9V9JQHB2WhnipUkTUkx8gJNNSMBqd9UzIDCFh9sEAfyEWlJSftUDMvhm6BvRQmGB8keY1m5tGXR12fWHnHNjEMIQeEqTPnWxooDJM6XWumckv6Yja3uqYlm3wvycaKpnrFMPq_HPxEENStSbI0WYzmZd5Ddv1StzEYxpnmjMHpUhY88iOmkFKTXLqWODMuXs6G_zb79_Amlwnoa_7DmkCVvdOU43kNifLJWGA2pR_h2oSw2PFZVzad5FkdGClaXMnqrIIM2CVuyK6isWLG1VL93JaS-t8WlmKVcdnADyaxCyxVtZPbAfu7zt973OTgtLdj9c9T4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22d414d1b2.mp4?token=Cb3LS_LaFTkyxv21iSHGZZyG7rSGZwzxlvw60ikilIVJP6YzWDhCWkliApvKORgitKxXeUX26OuCvCbIIUGrwbvmWmdStQ0LgZ7qGhQCyRQaTpAlQCEzZA8KxVpU-ZSsGj6S7tlk_jqldbK7mdNt5MFngQqTS7tglmQlrVZcb9KzCA-tUBlxKSxxWOCR7clzEClKCuC_gehh70NHMAcegv09xmsPPS4wpzVKWLZYyDM5USgWbEMvUYGbknMDSORJaEmr5-OsgJTwYojFFktpC6yx3ozS8Y0trgOf_Jjl3cJ0ObJhJ78MfxRaQPuqeDadsHVfePWNPd0bA5xeSIPYsh3TFruuTmnbapoc9V9JQHB2WhnipUkTUkx8gJNNSMBqd9UzIDCFh9sEAfyEWlJSftUDMvhm6BvRQmGB8keY1m5tGXR12fWHnHNjEMIQeEqTPnWxooDJM6XWumckv6Yja3uqYlm3wvycaKpnrFMPq_HPxEENStSbI0WYzmZd5Ddv1StzEYxpnmjMHpUhY88iOmkFKTXLqWODMuXs6G_zb79_Amlwnoa_7DmkCVvdOU43kNifLJWGA2pR_h2oSw2PFZVzad5FkdGClaXMnqrIIM2CVuyK6isWLG1VL93JaS-t8WlmKVcdnADyaxCyxVtZPbAfu7zt973OTgtLdj9c9T4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
#فیلم
|
قابی متقاوت از تشییع امام شهید در نجف اشرف
@rahbari_plus</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/farsna/448186" target="_blank">📅 07:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448185">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81706a78c5.mp4?token=Z4CxIMQQ2ctiXz0o-pN9VjNdLUhqCEt-6hLNXdyMMOQ6PYZcg9RbFr-L7ZxWtTYochFaWmpfnlxgP7yVkE-oRrBc1vECT5ItyVoXNNnbuI7zkttayQnJtvCUXQbLYYNMW3HoXifiVjFOvf_2gcJf5BgyQRK6ADs4Q14hCAjNBVr0jHhaOnxWURs4fgXAuiHObUnMGUHBnIF8yM0OdpjcaN0BR4TjI8QUGLPRrF4h4hbRinqjnL7OW3mhM3nxXP11NAe-rLO83neIOEPx41gEJJC21FC-ULeVsW3XPsoGT63HonQFyY7rEGuSwMbyGgwLxWRV7IlJT_EBK8yEQSGfkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81706a78c5.mp4?token=Z4CxIMQQ2ctiXz0o-pN9VjNdLUhqCEt-6hLNXdyMMOQ6PYZcg9RbFr-L7ZxWtTYochFaWmpfnlxgP7yVkE-oRrBc1vECT5ItyVoXNNnbuI7zkttayQnJtvCUXQbLYYNMW3HoXifiVjFOvf_2gcJf5BgyQRK6ADs4Q14hCAjNBVr0jHhaOnxWURs4fgXAuiHObUnMGUHBnIF8yM0OdpjcaN0BR4TjI8QUGLPRrF4h4hbRinqjnL7OW3mhM3nxXP11NAe-rLO83neIOEPx41gEJJC21FC-ULeVsW3XPsoGT63HonQFyY7rEGuSwMbyGgwLxWRV7IlJT_EBK8yEQSGfkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر مطهر رهبر شهید انقلاب در آغوش خیل عظیم عزاداران عراقی در مسیر تشییع نجف اشرف  @Farsna</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/448185" target="_blank">📅 07:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448184">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ff90c9a8d.mp4?token=nqYO_54gnLq_CEj3ZiBaS2wO-imo0awCPaxCQcs_Gb4_f1eDgId-wON5W2LEmv4-hKTorkNSeMGXjz7AkjpklLNwr5U6jZe9HaPLnaaynTiFecoTx2gh07Qmg8XeKvyx7gX2wxF35kk8rat70P69eoPy_L3KXnoKuFDGAYOLHXqUarchsdSx1bokxmcIRCXqs1zAfmC7nI8SU3UKmPV7sAe_7nnWcBLs2QSC1gBzrRMxIkw_yxZY2u6fHpJp_aLvLPHx6cwdmRVGAV2gly8TE3BeFpxtuiPqRpCDHGWlNoAyeC_Sgh7IRrK8vpuPLG7t4YmzraPmwVNOreNwWGBcKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ff90c9a8d.mp4?token=nqYO_54gnLq_CEj3ZiBaS2wO-imo0awCPaxCQcs_Gb4_f1eDgId-wON5W2LEmv4-hKTorkNSeMGXjz7AkjpklLNwr5U6jZe9HaPLnaaynTiFecoTx2gh07Qmg8XeKvyx7gX2wxF35kk8rat70P69eoPy_L3KXnoKuFDGAYOLHXqUarchsdSx1bokxmcIRCXqs1zAfmC7nI8SU3UKmPV7sAe_7nnWcBLs2QSC1gBzrRMxIkw_yxZY2u6fHpJp_aLvLPHx6cwdmRVGAV2gly8TE3BeFpxtuiPqRpCDHGWlNoAyeC_Sgh7IRrK8vpuPLG7t4YmzraPmwVNOreNwWGBcKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکرهای مطهر شهدای خانوادۀ رهبر شهید انقلاب وارد حرم سیدالشهداء(ع) شدند  @Farsna</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/farsna/448184" target="_blank">📅 07:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448183">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5e5d36e50.mp4?token=QSuu238B9PcrmRC_5_iBoJGyzWKYWckxIpDsA8uEA31cx0L3U9ZItjNSfVSUJGuAxkVU6dweoI5B3e9H7KoQF7MEzSpB9-1VHjf3-32exKr9VUESRhXdpoY7ZFJhaPhCJRuawakvOEZDoU4yolbTkaLR3_HHHEKzHD8IwlQuCINW8JuGm7oH2adYH0v9LEdPSDBc1FAr5Np49U1slcJ6V0WnaCsspUQlWPWFr1ZiyE9Y7QNF2Z8KufEHQaQ_oJkrFqD4FX4DcKU-kZS_KRTCA4NMIPNmcVAH438LWEY86cOTD8Ip76dr4YR_vw2mUH-QiKw8LED31ZijhiC9y66vVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5e5d36e50.mp4?token=QSuu238B9PcrmRC_5_iBoJGyzWKYWckxIpDsA8uEA31cx0L3U9ZItjNSfVSUJGuAxkVU6dweoI5B3e9H7KoQF7MEzSpB9-1VHjf3-32exKr9VUESRhXdpoY7ZFJhaPhCJRuawakvOEZDoU4yolbTkaLR3_HHHEKzHD8IwlQuCINW8JuGm7oH2adYH0v9LEdPSDBc1FAr5Np49U1slcJ6V0WnaCsspUQlWPWFr1ZiyE9Y7QNF2Z8KufEHQaQ_oJkrFqD4FX4DcKU-kZS_KRTCA4NMIPNmcVAH438LWEY86cOTD8Ip76dr4YR_vw2mUH-QiKw8LED31ZijhiC9y66vVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکرهای مطهر شهدای خانوادۀ رهبر شهید انقلاب وارد حرم سیدالشهداء(ع) شدند
@Farsna</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/farsna/448183" target="_blank">📅 07:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448181">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yky9SwtjtC5QVsmj1x0dTrr5fRJVej69ZcAWolEqfio6KSBVwJsSuEQ47dBS6qIROCcB7CRnVDoUrGk6PBhlntD9vRxXKdAYPFAArQT9N3qepnIuFNLAzsJs_LsDkuj87Azmi-ZpJNQLsLn9-NW8gknJvSW-NxjBhMgfxWv8flNpjJoT-LxajvNRClfCj-zZazm5UlTl7HosQf6t6GRXhOrY2d2jbOWkGAEUIjMYGjbPO5LSbSnXu_8xApCdtIpG4cgYAMNsrE6yA24u3ILhNcbd_cCoewQK_K3QPTTroJLzZYWKTIqH-KXouYn6lY5WdyqD5c4XZme2EkDa__0EZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ej7mx6NAM620RpTqjYnWNE2cZKBY2enWCwE601J6u69LfhxD0ZWbQKyzdRJyYrhlp9qJrf4yzeaZ8ZYBpi2WJmJBzkW37_6A-vECfUETy3JqQWJtzU_TKcJstDQRm9xtqizbelXJqZaJFgQwr_Sc3MHR8ucBRITnh82K0h95TjgIublek0Ztw8amahnkdDUYQ8tf3ecuDVnHGQPFZFZCSkFtbC29W9RaQwkfeaetKlwBPSwB9WkGGzlIf1piFunlPGtsaOorQnf2dAkPuGzPY4ShLUSydCOdJNO_-ZT66R0mIKdj5pRfYGjc8NabGazLg2mZBUR5J0T2q5HvqM_h3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور شیخ ابراهیم زکزاکی در بین عزاداران رهبر شهید انقلاب در نجف اشرف
@Farsna</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/448181" target="_blank">📅 07:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448180">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
پاسخ اولیۀ سپاه به تجاوز آمریکا با هدف قرار دادن ۸۵ نقطه از تاسیسات مهم نظامی آمریکا
🔹
سپاه پاسداران: به دنبال حماسه‌سازی ملت بزرگ ایران در تشییع دشمن شکن و پرشکوه بی‌سابقه یگانه دوران و قائد شهید امت اسلام، رژیم متجاوز آمریکا که روز به روز ابعاد شکستش بیشتر آشکار می‌شود و بازتاب جهانی خیزش عظیم و میلیونی ملت سرافراز عراق در بدرقۀ تاریخ‌ساز رهبر مجاهد شهید را شکست بزرگتری برای خود میداند، بار دیگر عادت پیمان شکنی خود را تکرار کرد و وحشت‌زده برای تحت شعاع قرار دادن این رویداد تاریخی، ارتش کودک کش و تروریست آمریکا در ساعات اولیه بامداد امروز با تهاجم هوایی به تعدادی از پایگاه‌های ساحلی و ایستگاه‌های غیر نظامی در سواحل استان هرمزگان و ماهشهر به طور آشکار آتش بس را نقض کرد و تفاهم اسلام آباد را زیر پا گذاشت.
🔹
در پاسخ اولیه به این تجاوز نیروهای دریایی و هوافضای سپاه پاسداران انقلاب اسلامی طی عملیات مشترک موشکی و پهپادی، ۸۵ نقطه از تاسیسات مهم نظامی آمریکا در بندر سلمان، منطقۀ پنجم دریایی بحرین و پایگاه هوایی علی السالم کویت را در هم کوبیدند و یک پهپاد MQ9 دشمن که قصد دخالت در عملیات را داشت، سرنگون کردند.
@Farsna</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/448180" target="_blank">📅 07:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448178">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5gzUFBdpRwq6D1PhZQ9ACu2I85b2Hkvqud8FPlM0H1N71GFbSOJ-rilMiKFQ5Mc0BwWtx_9WaXwlj-Yfj0RMhHTT5QRb_DtlgErdnv_BCO3r58c3FISbBs0I37HacBFDd4R_4rCbiXddrpuuzjs4yAQGTDh6eD5lNdvvVho0Px9RTlJ6xdox0sq2TvAYzQb683CDGkasRRVRalHn0wVuC2c8XhAfViBdHhLTET3iENZZeeO0iWqZZ9q7lGZAD0DbtQx53XZBE5LBd6C72b1HP2_uPOLJ2NH__obJjBZrFB8twqK7JDOUh45JvligS1Z10eDQMACkUa6eCQIE0bp8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00fdf85d21.mp4?token=mySI70RcU0uoJOT-vgYNrvy4yxV-jH8GYhU5mu9HWtakDgDUvEbPpitdZR4tbTHAmAIdZn15JOu6N2AhahJSur19Pn145ney25MuXDoatIctzcho-jTkoIs5fCYcUq5m4yBmvQJadygGCM1hx2Z9oGt0uL9rk6oX2-R1SCiuRkZ2aRxAQpyeiO6lnO4asLTL8zeApPGhDs2PRTvyADSxsTGcJiEfqZWp_JiPHWgpMGcvzq1JRthlvZERasCNi8D7Sw-A8UOLrY83N7Tc5hRYrevU4G2SMqW4wwsh2HPvkJUUJCoIgKkwzdFekGDDGK4zZdxwnVnb4ScvMqpG6lMyeIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00fdf85d21.mp4?token=mySI70RcU0uoJOT-vgYNrvy4yxV-jH8GYhU5mu9HWtakDgDUvEbPpitdZR4tbTHAmAIdZn15JOu6N2AhahJSur19Pn145ney25MuXDoatIctzcho-jTkoIs5fCYcUq5m4yBmvQJadygGCM1hx2Z9oGt0uL9rk6oX2-R1SCiuRkZ2aRxAQpyeiO6lnO4asLTL8zeApPGhDs2PRTvyADSxsTGcJiEfqZWp_JiPHWgpMGcvzq1JRthlvZERasCNi8D7Sw-A8UOLrY83N7Tc5hRYrevU4G2SMqW4wwsh2HPvkJUUJCoIgKkwzdFekGDDGK4zZdxwnVnb4ScvMqpG6lMyeIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خودروی حامل پیکر مطهر رهبر شهید انقلاب در میان جمعیت مردم عزادار عراق در نجف اشرف
@Farsna</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/448178" target="_blank">📅 07:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448177">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4707ad6fd.mp4?token=jtcFxM2LH_9uDgZZW8VzjeAj3FeC2DXgDmfOs0j14E-AW65RAQPo7WzWt-AWZpWoj_ec3xGw1UwBxxUecsYtkMvRtur2Vrf__e6bGMRBBnCPR1gLwqJ9B7PhJxHsntbNM9CLdsFnxHm253RfwVe3lCPhLP2DZKtICGqsIS47SJGBhSR8nHA9kMHZmh2d-pMwbjqPyaAsbW7O5vHY4I5ifV9YtxT9zxRGOVRouSaxCrIZUSp52hAnvIf08xy2Kspq4kLo5iAj0q9b3Aey-dYaF_YXaho6zMIcQXkpPftfAh5nmN4LUIp80LyDGhtugLDtAkkYV-ExJd9QWpdJPmg6iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4707ad6fd.mp4?token=jtcFxM2LH_9uDgZZW8VzjeAj3FeC2DXgDmfOs0j14E-AW65RAQPo7WzWt-AWZpWoj_ec3xGw1UwBxxUecsYtkMvRtur2Vrf__e6bGMRBBnCPR1gLwqJ9B7PhJxHsntbNM9CLdsFnxHm253RfwVe3lCPhLP2DZKtICGqsIS47SJGBhSR8nHA9kMHZmh2d-pMwbjqPyaAsbW7O5vHY4I5ifV9YtxT9zxRGOVRouSaxCrIZUSp52hAnvIf08xy2Kspq4kLo5iAj0q9b3Aey-dYaF_YXaho6zMIcQXkpPftfAh5nmN4LUIp80LyDGhtugLDtAkkYV-ExJd9QWpdJPmg6iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمای هوایی از سیل جمعیت عراقی‌ها در تشییع پیکر رهبر شهید انقلاب در نجف اشرف
@Farsna</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/448177" target="_blank">📅 07:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448176">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🎥
پیکر مطهر رهبر شهید انقلاب در آغوش خیل عظیم عزاداران عراقی در مسیر تشییع نجف اشرف
@Farsna</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/farsna/448176" target="_blank">📅 06:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448175">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
برخی منابع از شنیده شدن صدای چند انفجار مهیب در کویت و بحرین خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/448175" target="_blank">📅 06:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448174">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یک فروند پهپاد MQ9 در آسمان خورموج ساقط شد
🔹
سخنگوی سپاه پاسداران انقلاب اسلامی: در پی تجاوز هوایی ارتش تروریستی آمریکا در سحرگاه امروز، یک فروند پهپاد MQ9 توسط آتش سامانه نوین پدافند هوایی سپاه پاسداران انقلاب اسلامی در آسمان خورموج استان بوشهر، مورد اصابت قرار گرفته و ساقط شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/448174" target="_blank">📅 06:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448166">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vr0SiGClrTaz65Oxn5rK5Af2-7mhnHL-0indNGRf7iQ3XDz_ncc7RFJpQZXExtYFPL5O2fTMMLT1neCE35LN4nyt0IK0Rjmx5xa7T6K6YQ5r7r0_zHMsf7MhRDAygi8zZsOzjKdGRoO8s3WNsmb-RjB32bM9YRhdpnS3PJxuTezqyKdJqTGeAf3YUn3wKO4C9hokiglglEVUKQiFsg6c6a3S3uUy0tnjIrNIkQhJnf0RZRYqL-R4ubMT53XuTJcP-9k8ePxFUQ3sWZHdYW_TE2d6PAcIgiqpLcaE9Rt6MjIZ6G6psHz8AG25st42fzovhrVCPjlV48NHGNxOBiY8fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c_IV8Gi_X1nzgrbOO1FwJzdW63f0ysaxlBGpKXtIB9HEXPqsRmXQYyukceAUvFjGEWcGQb9UzyTXb0enRQLXeWQI3MfD4WJosIyeTvEZm4VXEpDsWHF2GI9BrNZs36313ljmcs1tXr8uoCn4q-5jFiV9bFiM12GfG1EyhxGg3KNQBbGMBDVtDsxwCqIWuaH6btFV0i9Lh3wdjqpNOaZmluiaOSyN3PioNpHBfT3Q2auyivszCz_YL4QkuJZa9NBYKJ21GkZnRkdsYYK21KJsYfrpi0lL7R31vpU6ZQV2Jt08IwKq1OT4qXuTDcjdnjhKDrw_rZYgOzegQHVmvMRSEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NBazNGq-9ulab6pi_FJCqZU2BIPra4lFe3lAGyxKlJcYA5dVC6rg3j0cNrEZjPba1r6gVnu6C0Whil5Co2c9XbFDdpn1NdGVpSnMoQtMtPBI9qLSE1EqpxgohNkcyMyVmfr_hCtZqbQtim-Gs4B3Bb4YQMDXL4eSxxl5vmwpQZGOhoKrmE5d4-gnjnwBE6NXvcDf6ptEGm0UQl6TQeHu7KfaqSNBgSWtrxsnbXTHQr3C9855K_oNup_XuPOReXcz8lMl3XqKRgK7F_8UVRaagKTe35H725ob-P17PYQzcOLLYu-3QSD1wZh4cnR57RPcgErdc5sOYCnD4iYnCc8-UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bc_EbFu09aJ6FWbRYD9UjHFarMLrkxUOq4JWPoCnpNWPAZBM8TbuzUCUsC0l7UMhpZo7ZEjkhViY6Gnbd2GUivaiAh9LiW1LrcvBuGCa4zEvY4A763jq1VmanfnGg7Ec7yQbP5YPjc1nYRx43vUXRQ6Tb6czQrhg2m2mxmEhuPSx_HRNRoVgiszeY0X2MjZDzI8neA_A4TCItuWwpxx0oBCoUK1Rdxmsgb7YEdJ9ulcsjHnQ4jyWJZxtM_3HpoXs336TEYHL2RDHZM6QdWxj3aBPrRLqcBUXgxRFZplVOYY_P5ic-fohmrenc0ugmp9Lidf8TlHHEkVLlayG8xyHlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NtUqmJkW_Vs7IgiaZ6r6JY9WGdYyjELK_FRxXnsSLnVhfVn71kmW_VEgo-ai6QZh8NirDLVgi5i3xbjKRK12OUYukMZjRZw9tXqJYaaOsBBxi511jiVsMBTqdZDalvxnaFJ_orx5fckHS5hxsjbBCtLA-iIID3m2RZYgRcB5v2X_JUGmZlq16RBxuHiQH1ZNLbvWM1yE83eSbHeedQAO8GTM3vY30cgX4bYV9zcd1T43XwbILQswVzidVKFvqmlW9nl4kKXhqT0bI6muiGsiQt51hjN9sl-wUw6T_h0biqOyQFPP5zlREfzjX-32fWfXaeom78G54aPte2Akb3TMgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GQ_IR3rmmEOEveGCrypQtnjoZcsYXEwv4ygpZZul7FJjfG__3geG0baJiB5vc-19edfmFdFlNhj5d1yUtrRSX7sbm3CNCDSARuuBq44gJKBzBE6L9TrADiNaSxIxCfp0ZJAS-21gfMRExOFJtQ-T-jugiYfqp3SMOHCwtyOW3NI3xd9_-c5EB_6BNaTNsNJBkt-jl8urCtFQrCTNfUTOOUXf37PVKoRkiJil57T_hTHAGPb5rM5OeT_94JKkhiQrJAeWWcRgK1gTn11P973GL9ncr2o4WArzfpOyZOZFdu3EtAq4TsN9NXPOtGd7tlPklraJAdOMeKz1JYbI54ZGOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rg2JcC4GYv5mzrERzR8H041QE43L7VE4DlARI-fdBZdZQ-0L9OfN0brv2wNo2vL2Ig_-qKAQt1BtlYNquc-8ReiQb2S0PwxTy6eGoOtQj5_bXUcvsNdUmoVa8dVfQuxn7-YrG2k2sOp3AO_EUCaFvyEPvRayz2ALjKf_JaPWqlRvnhUwsgqoMLjD5vs0VGa4-T0y7ATsln4ftlLHtGVE87rGA9A2s9XAcm57L3uSX_UmGvqyvGx4-cxDnGhVRJ7NkrU9MEFomZQouhyEwCskYikdBi3pk7zh1P_VuNm-0RO8uyorIIX7b7FyJuVy9GYRIW77a9F_jWirz3QZ6aDUiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E1TEYm3r5TFqhpd_Q7crYBq9I98b8dKXXDbqBqwRNg6NOYTrN5Ofr3FNOr6vznoRjd-u6NqzOMUT0joMMaGVFMlzKlSAwcZANESPZKWklTxSBHNFvxs8n4fa6gDY-nbEOa6bqoJ0g4JcaAHzP0Y6DAGHHB6EMUZY1KiYaCF2CTpfPW-9we5v9GnJvwaRJaYh7bV7EhdA0qbN3e06zmCXl1HJrqI1E-8J-dCCotRBJbMJOdOUTSo3aoNkt_JV-thQHy3Jj5376aTJ9UsYb5tmMNXBx3-gnkMaTIeb4UQZIT1fQKPD0DZ5J54HRNEV93I14nJcTQXocM-W2HZZoOvENA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تشییع و طواف پیکرهای مطهر شهدای خانوادۀ رهبر شهید انقلاب در حرم امیرالمومنین(ع)  @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/448166" target="_blank">📅 06:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448165">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7688a9660d.mp4?token=Z2Kbm60Hq4SbY75lqCc5k5-JQYo48CnTYmEhtNE5lyip6ivSUzfqG-R0tWISBNGmPUuvVyHhHG7IxEFXQgQZ9WHHb1HE3ssMZ35uBUaBXXZFfrVF-Ex0SF75II5dRIYXgmlA6ECQ3sCUbeHY5FlsuesVv8VW9XnQnUVearwVWloqmpiXVmfuCgMT2mLW2vnYngWcbq8oKGD5vuZk-I5kfdkinhdI-0X92PxDFsd8QetoeFH45m56iNZY70DNfabhLqHaQm_cvYEGkf0IEGShuogAXpmhwJlV-zL_VXaIXuKU60PlcB-RKkBmaxaPE2boBVAervQDaHkPkKgVG5FKIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7688a9660d.mp4?token=Z2Kbm60Hq4SbY75lqCc5k5-JQYo48CnTYmEhtNE5lyip6ivSUzfqG-R0tWISBNGmPUuvVyHhHG7IxEFXQgQZ9WHHb1HE3ssMZ35uBUaBXXZFfrVF-Ex0SF75II5dRIYXgmlA6ECQ3sCUbeHY5FlsuesVv8VW9XnQnUVearwVWloqmpiXVmfuCgMT2mLW2vnYngWcbq8oKGD5vuZk-I5kfdkinhdI-0X92PxDFsd8QetoeFH45m56iNZY70DNfabhLqHaQm_cvYEGkf0IEGShuogAXpmhwJlV-zL_VXaIXuKU60PlcB-RKkBmaxaPE2boBVAervQDaHkPkKgVG5FKIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آماده‌سازی خودروی تشییع پیکر رهبر شهید انقلاب و خانوادۀ شهیدشان در شهر نجف عراق
@Farsna</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/448165" target="_blank">📅 06:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448164">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsI-LkcH7iNTVDD1aJb2nrwkcmKvaCAeAAVUJoiyniGHLC7kNehyxK7Q5nfi5Km4Ffso5FoDhLw_WWUwSMBKngTurqzIRHSq2ptr_w_5357M5i9pE1wHS91id2_EA3a4YJmgBWyAJCjcxBeaBiZmNbB6eNrp6sMzLdlx9nmp6GK0X-DPvUvxjSTgtmPvXfdIMraup8J9jueIlScVSP89B_zre_F4sYCxPVSuIqX-FrBCMXEjrF9rQ4pG84dGjwI9ubY0Vt45Ur6p1eXF8-2h-f9v6vZSolX01z2sDZn8az2Cr8IrXznDMq_JY_WtwnBVJWlwLCaDFDzU4wwGaAodlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: دورهٔ قلدری و باج‌گیری تمام شده است؛ ما اهل عقب کشیدن و کوتاه آمدن نیستیم
🔹
کلیدی‌ترین موارد نقض تفاهم‌نامهٔ ۱۴ بندی توسط آمریکا:
۱ - نقض ترتیبات ایرانی در تنگهٔ هرمز
۲- تهدیدهای مداوم به حملات نظامی بیشتر
۳- حمله به مناطق جنوبی ایران
۴- بازگرداندن تحریم‌های نفتی
۵- استمرار تجاوزات رژیم صهیونیستی به لبنان
🔹
دورهٔ قلدری و باج‌گیری تمام شده است؛ راه به هیچ جایی نمی‌برید. ما اهل عقب کشیدن و کوتاه آمدن نیستیم.
@Farsna</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/448164" target="_blank">📅 06:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448154">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n5Tl-bt8jUctIc0I85K9EqzbRz-xDO6FNH1LysN4R3WenIe3w5ucA49O74YLiHpvBWM8GtTMpNHghE9GAwicdcNMX22UkUWfq4hqI-bcOBMAvihZkMNzyj9ssfLN9aZIuJ4V6SU_Efu3L9FnmbdaPvFWvEe1vr-JF6AbhL_sLFlyiDcPSOtE4O9KbygU6fhTTSX2oCsblrSVxu4ETgWppj5IF5_zVVX-WVKc6hu2QhFTQ7E4Rd91LRunj-2Z88tqolnMJvMIHskh-UeXRuizN8X9jpHhN2EIm2kqorSFsFo4SGE0qG0Htjtgi9L56yEj7CMbNPuQuYq-nwBktblq9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CCP1hoerR212W7PZistAvWAwz5GTRkyjC6N1OFZYDr05g-1B8lD7TzKqKAbFzNgRttm6HE5gb12gjInbctOJLyLtu9Umbval5noTCa0G1L5kE0p6DBOkquvIBNxVD3TLNF6sQxqnLO_S3tWfLryu_98EVBXxy-IKrDO33U6PP20NNepZCbojp3WREC-FOuLKrT758yJuWTCzWjw7uy9k2RIjuHD0qtgE-4aRFOf8danbioU-SQN7V0XoY4xwibmXhXotHxayC_z4plDbRIpdJ7kjWPdOneiqXcdjV6YTSXevUpXdm1QqEY0LJTwRFs8y7Ti9XOJHI1gnAJAjbPOocg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XDpkRV7OWoaLuegJ8vN6Vr5BR7il5g-PfYyMrvdtqMAYRXi9KsJV_HvsYa2Sw_eXIjQDHRIHzXqLS87vQDPiwyyjzBgDuJmh-HIEojeMyG0Kax2Pf7LpyTXT8SQY7PrbururDRlEpO2Io6EF4UytqSI7lh2EM7wOqP_xuiS8pC29SUWtwus34MCiVd7jxW99SqDgYRfbFXZCotnRBpMe9fmnsuc4EsfuOaXFbv1oF6XUaTYN9OcVpTQs-TddUjH2-tkMnecf9LO1qIu2qxJPUP0uUm8VtPhslfegGgCvzbEdsWR_fwuc79GJRqUVy67cUbHAqwbbTGB_lJJoEqYh-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HEBohpGv-LzVEBmXDVJGprJ-H6hg4Auk2NxIOJ9CXx0x3yzBU7w6NA09IWIEb4u2w9xBjErKRiMC9cLWwjPsMlfR3hQpZZYLAZ_lD-bvtm85sgA1btJWBzRPLXSPKvnCML7RI-4Q56iceoptFvZ-KV88Jjs488NPoKJ-4J0xejCcoF7nNjWqV_Db-jTNgMjEWZZc8Iv4pV6rKcQdNSI-NYt467nC9Fg22StYGCUej8bW8eflfJ8GcWc5CW_dicfkvGjd-NRaEsjy8oXMgf5ZypRz5EVwGVtod8BrKUqfo5SQ7B-Y3I5Re3pCsmv6LzDUP_koMI7zuc8F-wvQ4lnREg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BJ8YdG_I5v_nnzx6gT0zmZ-y6AxCPuOGuXyc-oX0I5TnPsbwSjduanEsK1nZdsoUXRw4tU6NI8uDn1PTzChyyinmNKhnHXwpts5r8-lawJOW6itzWX8F7-G7ZcstOAwsV9N4Ep4C1cFL6p9PZ-8kPJCv99t5H7XsZtfIHg5BbsoaXrVaDj8UlTKAxNs-W-0EJZuUa2NWdJTCdjUuInj4J2cSzFBC5I9WhGAFw3IuokIjDnLdurfwuFxBOtrAuVICef8Y9QBhPEl5iV842q6TpUy_mzvcnxbKphjJBTxJPcgkDYOH_A4mmOda5ieloBQk_pYZabfv7a5vcOmPmWkybw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dFxN1tovVz0p6sDbcTa-3VGQyFb7roFlPioGQqmbyHoFwAEwgwQ5XJuoLkn1j4r6UYTmxdbqfSb7uTkKyxX4YwunyRYPBro5H5wkAuoCHFxar1OR-31xmAiv0BY17Xy19WZh4rq1nSe6EjeLVCHNG4OGuQr7WaImQ35roaUot9MMEjM71XRTQ3VV73bsac5zlCEe3hZpCuek8z7EUV8uknVK_L6Byh9V0BWMPshDT85v_CL_S5tOYhhEnmUL73vRhMbY9wUY6d83yu5PxW5E5Q1VMcJoJeumfjclU7UXS0j5FJ1dwoH8PaJq2_UpQ5kd0Ar8hfhCuu80A85YdTeopg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jqC3PHt2u6O6Oa1frf7GF6yQ78spvOfaMLG1q8SosJN_YVtLW74L2cpaO1meAClVq-Sr7-5gmnraTpChYHesZpgAhKO8RVo1CigHC7LO4vNN48-Ry6KCStny5Lw4aNZscQnojH8031v6tbYCtP7e8uxa00j2vxL5UWEdZyetekSe-XSS-qEpCMYW0NC_sABhEqOA0XKkpC_OXJk5Bp14I3LAbKLkODIZpa_goKRXGocjKmPZioCrvIgPj78ZmHk4OBNQRm3PfgvI_UGe-v0SrT0BYO2tgiQ1oPJuP5EhJXHBHTLX-0tMwy15Mia4tmL2BIXsOFCrzjRNu6GkLXZi0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lMQGXGtHvgAtWI293YgGja0QLeXIX05gzOJoJ670zStmmSL4ED2n9Ddo01J7J0mGqd8yxETNvxzRxFcFMU5_ov6aBa9maynsEmQcYeGb4VXiG47i4J1khhVHTLVquFHWqpdqG2yBacLuRA3Rhgy2cpqIEG8UUvNoilnIMdS6h6RKEgXj4JtaZO7iHMlcB4DwkT5Xla00ByoKLMXmTN50Wsf94gDfEGUdW9KNTbImj4P5f3LjgaIrrzgGxLT3qqmXl9mgx42qP1sisxF4i-rSkr4Cxz3DAJ_J7wTo_A-c8qko5k5j326uHD46CIvgJzbbyA2fH9Te1oWKxt0ocfQtdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rymv4ZWoPYdA-5IrqPDsxSdiJ-zCLtMIVPVrSBZMFYkcDOlTJw9diOIl2DoFfgmptlDL4XgVjrgsgGZrK4G3DZZGZnVQ5aGcc-sk_lwlMql6ytA-TLtX1t5-rBpSREdvZFlVaNiIg_qR1SiEf-xpDFr7Jp5Qcc9gfGHK1LIx1iAI2wZwfbldouNQCOM9W_KU5sC6trr_0kB3adM6Owh1n0OanV5xmIRpOLVx2HiRpR94GkACdoi6j-XtC8_Xd4Xjh-1SyfU3C4Q4XfaIH5N-W-vFtse2QAq7T69a2OG-0CPV-N2gfvTBiqrVrmJqSqES_ZAl8_Y5twTlBjDMHdfMiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jI_6Xz_ckkJY6rxS6Gla_lbHoreCAwaO3oOPVC9L-hMX5ctM12sROoBtQqS0rs4Hg_z4iP1qmUJTF2ESdHl5I9yJRrAK7ul9XssVpS-ji-ekcianBAhZBTWN-QD6_xTuIVVe-E_XqPGn9BrQYylFrzVwkUydiao-mgZKpH7L4CIl1Yo46c8vLIvydNrGpDOUsUrCrrBlKfX636e4kSzNP6AjQJtcLSChZkfpDQoG1ukreG16hhWLRrNOzoE4ev8KCus5pLr6q09OgoUMuHHqXFESEZKrpsm4l_ryrS_I8bWxrODArRJWntfS3jcAoLc6e-hnvVpqPlWINJyuz6beRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
طواف پیکرهای مطهر خانوادۀ شهید رهبر شهید انقلاب بر ضریح امیرالمومنین (ع)  @Farsna</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/448154" target="_blank">📅 05:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448143">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf867b1801.mp4?token=R001IhCLOxgjJ3DGK_warQynCEbwUDMeWmqdEinP7YhoF6QHEtuFWj0L_jOqIs2X8SW6YULlpanXh9d-sJ6-uGXR-Xr0RYy0MeJmQ4o1GSNJ0YNTxKej2m2f4A-nmbSzA3nfry9Vl0pRwNn8pslvETl3IvY6c2PPUH0nPLY41uXgmRe5kpW8-R6vL63rfAUCfg_8ARWARyfdvoiWdvbiVjLE7QdbyDJW4o-ki6F80gWxrBYZb1K1Y1IyZEQf5R_LUHBmM5rS3lO059XfxnLmS7oZbgj1uVDpBe5QHAO506Ib0EXQoHAo8hqYkenNvXVML6HrDraGd2IJeTHtLl65tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf867b1801.mp4?token=R001IhCLOxgjJ3DGK_warQynCEbwUDMeWmqdEinP7YhoF6QHEtuFWj0L_jOqIs2X8SW6YULlpanXh9d-sJ6-uGXR-Xr0RYy0MeJmQ4o1GSNJ0YNTxKej2m2f4A-nmbSzA3nfry9Vl0pRwNn8pslvETl3IvY6c2PPUH0nPLY41uXgmRe5kpW8-R6vL63rfAUCfg_8ARWARyfdvoiWdvbiVjLE7QdbyDJW4o-ki6F80gWxrBYZb1K1Y1IyZEQf5R_LUHBmM5rS3lO059XfxnLmS7oZbgj1uVDpBe5QHAO506Ib0EXQoHAo8hqYkenNvXVML6HrDraGd2IJeTHtLl65tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خیل عظیم مردم عراق، دقایقی پیش از آغاز مراسم تشییع پیکر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/448143" target="_blank">📅 05:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448142">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JB_NZU48MszmLl5mPPhRMblUObYSL_HEGdjBtvn5mDU1ze3DIrfZJk71qcE_sputapmuu72XjS5GjdxGmXOyIwGjgZtUVzwl4yOQDXbjV2ib3rk3NGBSTAlqZr4YG9GcgMvIK469QkoGMQrO6jajJOelGlW9vumMoLOBwXaEQPU8tXFYpGZCRVCc0qUD4I2oYJ8tK4tSMUDD7s9OmyX3AOwNwtKsK6hLtHyNMV7qhcx5Bv0RcA0JKSedeOVR6h_0ocvV6fjbB0G5YuFabZqMzjw3jyqFEPKr_O5X3gNcAQ6O5irSih2FXX-HN7KYWpa3EGQxdNmhjkxzpbUPyKCOaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
خیل عظیم مردم عراق، ساعتی پیش از آغاز مراسم تشییع پیکر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/448142" target="_blank">📅 05:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448138">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UyoFgmTAOReSoqdJbNh8deMf6JC9shXcxisvWZUl-E6H--6xEOnUHT2JES83j_OApbOAtKnFGj_kvQzbdzwahqz8zPn_d9Fs_EZTiTOlCUW0_fapi6QhHZQ4uwcGjNzvOm-LA1weStVMNeMrDAr_k9YKew8C4msemYKfTzQzETvbKPb8110Z957xwVCyrjUs-IdZfiD0-NgKHvcOoLZIaRHSI8IsTPFnWP8TILrIYcFsGI8LpBD3pZDSBRzt_dIKz1PV7TsC-K6xD-PdbvK0MDy2Cc0dR3po30FfhI5NQbh2ve2XggIn2WK0jiOfG-M9tyL7YHA2sKl-LxUq0m8MTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pqf6ZpTSAl6TtOSNnVGSEQAx45F3goSgOW61Njv50C_vqt6c90wOZAEdUieNXe72TXxOc4bbECFpu9ybI1iLJa-nlU2fUkn18IEwJ0Kq6R8iGkZ-CIfO2wkjGnnC9zAUWTju9bq9kMVdC8oyjDmHx1U8M8Ex-iqZ6TJY6Jk5caJXpHFC-1YVe0iPbzpgnAZ_6d9qBwMvesVXaFE3DRkyg-QxfYDySYIGoX13I0AYdR6OLpDGuj40trTq-g5OFWiDZe8FjcN8AAvYPBr_8LaiW3A9l3NPL-zPpW2SSSy8pdN5BMspQXm7Il9pOzQLFSwrm_TI20AEoK1MC74YEjWpOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TyY9ScAkj85QBXv4ynXS_kNBSoXCrfa7rEuQWP6KJzHF7Jh9X6bAD_3_v0FnPMt07edYUlMRPAa6S1MkKANSEsSpI1IhrO5nO4VjSycHqW0Jh90dsW93E0DGWg2jPREtrD6DbnpK2RofNuQAqnD8gHWGS6cVq-OtPEvSHYKqRe6OqL21_rwHsi3SwXwL5YOlgBYLW5RexHJzXCmlkjLqXXs1SKj7w4JLqMvCG0RMEroolwe-6Uxg1khSxHp0g7huTAP5y4xj5syMqA3fPwRJm_s9T7bFDDSovxpW7nFMVAJDMZ-lC4A3qJMNLO9x9hF0AsuHjObBcasF72Eu5ovmmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HWFkdncRsx8aNT9WkiNq3swGoxxpb54ud59SxyauRJgaS841ifQNdNZQU5K2whBWLBQ_vYmPuaawJeneUFPumW8h6bTd5_Ny2gvXMa2cgSKzvVxErH8dnXD9D4TV6NQyQS9mV9xFfTeN_B1Ez-6f5W2LDQ6KHLse5kWeqa6P0XvUhOabrz_QB-8SAf7jwmhaWkKiVk3Ql7cRwqT4U4OM3cb_log1EaTH_d9WznmD8BygZYoBaa6oeeFc3h5Sn5ZMq9pMP8ttXhppjDMtEAtouPsV9_525rASLDwTCqh2eB5ANuw7iygyK1f0IShqFTbbTySrYluWpowidyLhs-HLcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حال‌وهوای نجف، ساعتی قبل از آغاز مراسم تشییع رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/448138" target="_blank">📅 05:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448137">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">سنتکام مدعی پایان حملات به ایران شد
🔹
فرماندهی مرکزی ارتش آمریکا (سازمان تروریستی سنتکام) گفت: «ما دور دیگری از حملات تلافی‌جویانه علیه ایران را تکمیل کرده‌ایم».
🔹
در این بیانیه ادعا شده است: «ما بیش از ۶۰ قایق کوچک و بیش از ۸۰ سایت را با مهمات دقیق هدف قرار دادیم».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/farsna/448137" target="_blank">📅 05:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448136">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">قرارگاه خاتم‌الانبیا: اجازۀ دخالت در امور و مدیریت تنگۀ هرمز را به آمریکا نمی‌دهیم
🔹
بی‌سابقه‌ترین رویداد و حضور مردمی در تشییع و بدرقه قائد شهید امت اسلامی، شکست خفت باری را بر استکبار جهانی و آمریکای جنایتکار وارد نمود.
🔹
ارتش تروریست آمریکا بدون هیچ گونه پایبندی بر تعهدات خود و در شرایطی که پیکر مطهر رهبر شهید مسلمانان و آزادگان جهان میهمان مسئولان و مردم سلحشور عراق می باشد در تجاوزی آشکار برخی از نقاط جنوب کشور عزیزمان ایران را مورد هدف قرار داد.
🔹
نیروهای مسلح جمهوری اسلامی ایران به تجاوز و اقدام تروریستی آمریکا پاسخ کوبنده‌ای می‌دهند و تحت هیچ شرایطی اجازه دخالت در امور تنگۀ هرمز و مدیریت آن را به آن‌ها نخواهند داد.
🔹
مجددا اعلام می گردد تنها معبر ایمن برای عبورومرور کشتی‌های تجاری و نفتکش در تنگۀ هرمز، مسیری است که جمهوری اسلامی ایران آن را تعیین کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/448136" target="_blank">📅 05:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448135">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1b85abc28.mp4?token=B98xWirdUyNGYLJT1Yv3SvOrH70DwsXWmBpsTuor6_WaLH4l8ESIrO8L83Vm9bPHJUl3I7vmh-Ik9wBAbJvs0xRsDfibFETVWhlxtbXcUScfaq8eiGH4zu0rFnggf7g8MGEh7hqR5t6KI8ShP_U4xuEQ2sTTtlMf-FkIPoJoMm4mhA46R9fvZi-6JU_29_AtiANHgObXsOsMDiQoquI4wRfVLIzU8u_w8F_CFPObdiIYgw_cHEeeIvRP-PIi73ppL1u4Bw5dc0Is98u5IJMrQNofauPZG7l_vRUnKsDLsUa3T-jD-I7rNsWi4y6CuclGx5LisDBwbEm_ct_tv-JmyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1b85abc28.mp4?token=B98xWirdUyNGYLJT1Yv3SvOrH70DwsXWmBpsTuor6_WaLH4l8ESIrO8L83Vm9bPHJUl3I7vmh-Ik9wBAbJvs0xRsDfibFETVWhlxtbXcUScfaq8eiGH4zu0rFnggf7g8MGEh7hqR5t6KI8ShP_U4xuEQ2sTTtlMf-FkIPoJoMm4mhA46R9fvZi-6JU_29_AtiANHgObXsOsMDiQoquI4wRfVLIzU8u_w8F_CFPObdiIYgw_cHEeeIvRP-PIi73ppL1u4Bw5dc0Is98u5IJMrQNofauPZG7l_vRUnKsDLsUa3T-jD-I7rNsWi4y6CuclGx5LisDBwbEm_ct_tv-JmyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر مطهر نوۀ ۱۴ ماهه رهبر شهید در جوار حرم حضرت امیرالمومنین(ع)
@Farsna</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/farsna/448135" target="_blank">📅 05:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448134">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
شنیده‌شدن آژیر هشدار و انفجار در بحرین
🔹
برخی منابع عربی گزارش دادند که همزمان با فعال‌شدن آژیرهای هشدار در بحرین، صدای انفجارهای متعدد در این کشور به گوش می‌رسد.
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/448134" target="_blank">📅 05:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448130">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b404af873.mp4?token=ZxO93g9Nf0hKNpc5CM9_Kx4iEC6gwXSSJFgjm088Glgv1fETImjJsxu4C-TwBPkr_Esa-mLW8RxcifRRgLgOTSAotyOFX8Ey4tHQ2ue35SdxuNKxFMx2LTGF_P93Y5sdrKgj0S0o--Lhb_o9sjtQnV4X-t6q1IiMHs4X7MeavEfgp11-zMYW0h-A9A6p8p2BBUF7OUjISSUqjQYrdZ_rP9fUiRTVe6BRUeicyFHT5VcfNKOj7spQUy98XVO2cU14l58ZMeUnWkc7V5r7VDEGWgJrqv9eKFF-Z1i0LaN-iPHKV1gotbnI6GNSO2RV87SrPfjjIetTRoM7w6N-shOgjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b404af873.mp4?token=ZxO93g9Nf0hKNpc5CM9_Kx4iEC6gwXSSJFgjm088Glgv1fETImjJsxu4C-TwBPkr_Esa-mLW8RxcifRRgLgOTSAotyOFX8Ey4tHQ2ue35SdxuNKxFMx2LTGF_P93Y5sdrKgj0S0o--Lhb_o9sjtQnV4X-t6q1IiMHs4X7MeavEfgp11-zMYW0h-A9A6p8p2BBUF7OUjISSUqjQYrdZ_rP9fUiRTVe6BRUeicyFHT5VcfNKOj7spQUy98XVO2cU14l58ZMeUnWkc7V5r7VDEGWgJrqv9eKFF-Z1i0LaN-iPHKV1gotbnI6GNSO2RV87SrPfjjIetTRoM7w6N-shOgjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقی‌ها از جای‌جای این کشور درحال ورود به شهر نجف، برای حضور در مراسم تشییع پیکر رهبر شهید انقلاب هستند
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/448130" target="_blank">📅 04:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448129">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac39b4df86.mp4?token=T2KrT1uTmKqA9XnA0SwKqprvrvmFgUrIeeCiAR5pSjgUFumNt7epOrepZpDLFVBV8ZCdcTv9MOKt753MH8728e8loeCz6rubZECErxclLSvWYW01AbcsnwralIr9ColEspoYaOg1xvjph2Qa0-dsGXof7wZZ7yGHoC3NYfYLGSTkqNJh5L4wzJbt5IwwU1038xfug1OsdaQ75OxbtgCKpdtjjCCn-DK--NXP4OIIKA91Nh2ibpo91gfGmVCmeQi1BL7H70-eORz_gMLg2svuRsNKGeBetbm39jjMgPRzQ9raG4EmCitFW2SBJZ_jVdqavX7bHnKwcVT2NFDlr9Kn1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac39b4df86.mp4?token=T2KrT1uTmKqA9XnA0SwKqprvrvmFgUrIeeCiAR5pSjgUFumNt7epOrepZpDLFVBV8ZCdcTv9MOKt753MH8728e8loeCz6rubZECErxclLSvWYW01AbcsnwralIr9ColEspoYaOg1xvjph2Qa0-dsGXof7wZZ7yGHoC3NYfYLGSTkqNJh5L4wzJbt5IwwU1038xfug1OsdaQ75OxbtgCKpdtjjCCn-DK--NXP4OIIKA91Nh2ibpo91gfGmVCmeQi1BL7H70-eORz_gMLg2svuRsNKGeBetbm39jjMgPRzQ9raG4EmCitFW2SBJZ_jVdqavX7bHnKwcVT2NFDlr9Kn1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای اربعینی مسیر ورود عراقی‌ها به شهر نجف برای تشییع رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/448129" target="_blank">📅 04:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448128">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6519ae9688.mp4?token=aJhOanGu5a-txj670DMOlfEJdxdt3TVsq1wlkvWozShPtIyCFjMAD8R1LnxX92VwWAfmSSlQoX6BwjPlZOO8g6z8crwd8D0HOSa1DFQauSivnwyKgZPnXXcZpxa3pNQ3cqcapAb9d0kSX6C1MdiSUxO3ah9tf0h-N2D3U4fLBgF5b6yZNN1fTBY-86CWBG_xoJoyXyMPPLHU2ZSfAFNj6qnIMFMemINJ-qWSsmRIX1G6iDCkEiszehZUwwqj6jzOPXaKDRRuBm8Q9gc2R-a2TH9Ve1WUSmbozxFANvBz76wrqg5SmaJkBcKZnia9PD4cb0ud-9mtyeSHMgoZ8hzGcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6519ae9688.mp4?token=aJhOanGu5a-txj670DMOlfEJdxdt3TVsq1wlkvWozShPtIyCFjMAD8R1LnxX92VwWAfmSSlQoX6BwjPlZOO8g6z8crwd8D0HOSa1DFQauSivnwyKgZPnXXcZpxa3pNQ3cqcapAb9d0kSX6C1MdiSUxO3ah9tf0h-N2D3U4fLBgF5b6yZNN1fTBY-86CWBG_xoJoyXyMPPLHU2ZSfAFNj6qnIMFMemINJ-qWSsmRIX1G6iDCkEiszehZUwwqj6jzOPXaKDRRuBm8Q9gc2R-a2TH9Ve1WUSmbozxFANvBz76wrqg5SmaJkBcKZnia9PD4cb0ud-9mtyeSHMgoZ8hzGcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وداع عراقی‌ها با پیکرهای مطهر خانوادۀ شهید رهبر شهید انقلاب در حرم امیرالمومنین(ع)
@Farsna</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/448128" target="_blank">📅 04:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448127">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33045a6887.mp4?token=us_blHiypx1gxzcK16l_4BKnS9temvU1gvCey5WYGM67glnuIhttwMNOep-YJLO_0exCld7DePUsKur9b0av31S3qI6ghC080l4zsWEMRJrocyNxpGKKa7_IIU30WYJYHsbNZLwp6a_qMOc7IC0qIcFkAkyl9aiYzS3vXSmh9sbv0I3_vEsVIfHfb_VxBd2X5a6l4pD3GBJ97bVLxaZuIKE9GiNIgVIlN7wi99xob1S1ViCtZicQvWTyxhIcwUly7LPGC4iYPzlOySWnwN6hSbRp9TxK4t1Lc9n9N6y3JL5iAMyIOHb0iQvLck9aZ2hPMQSpx3Elek2c-2sOJEwuLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33045a6887.mp4?token=us_blHiypx1gxzcK16l_4BKnS9temvU1gvCey5WYGM67glnuIhttwMNOep-YJLO_0exCld7DePUsKur9b0av31S3qI6ghC080l4zsWEMRJrocyNxpGKKa7_IIU30WYJYHsbNZLwp6a_qMOc7IC0qIcFkAkyl9aiYzS3vXSmh9sbv0I3_vEsVIfHfb_VxBd2X5a6l4pD3GBJ97bVLxaZuIKE9GiNIgVIlN7wi99xob1S1ViCtZicQvWTyxhIcwUly7LPGC4iYPzlOySWnwN6hSbRp9TxK4t1Lc9n9N6y3JL5iAMyIOHb0iQvLck9aZ2hPMQSpx3Elek2c-2sOJEwuLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقامه نماز بر پیکرهای مطهر خانوادۀ شهید رهبر شهید انقلاب در حرم امیرالمومنین(ع)
@Farsna</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/448127" target="_blank">📅 04:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448126">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f19c0afbe.mp4?token=Lyouef88LoegDc3rQLvQh-gsv9i-CArR4y34qsBUzC3Gz1psOHGwUEz9RVFjlm3z36SmTU3viekTYAEDIqOANW-zPJx0vajJL8Q0U4kuJTIexe28keWVQNkkw3K6Mg7NUszzVNbwAoT8H7hfYEAPMxpSrsNHVz30xFqBXC2K0kWzY6g7Gcy5rWn_2Le9FJSBTKzh-x_7fcAitwuCV6gZ5Y0dLrtLt0u9iPH50LN0ZxJLBnBqfPMNZ_6EQeWWrO72MwQU8ZlD-4fSRcy2m6EWmdvBQmHKl6iGDyX4-LWGb6GL1rE3y9f6k83Wvc_glz97iqZ8lscfHBvjHvDKLPxe_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f19c0afbe.mp4?token=Lyouef88LoegDc3rQLvQh-gsv9i-CArR4y34qsBUzC3Gz1psOHGwUEz9RVFjlm3z36SmTU3viekTYAEDIqOANW-zPJx0vajJL8Q0U4kuJTIexe28keWVQNkkw3K6Mg7NUszzVNbwAoT8H7hfYEAPMxpSrsNHVz30xFqBXC2K0kWzY6g7Gcy5rWn_2Le9FJSBTKzh-x_7fcAitwuCV6gZ5Y0dLrtLt0u9iPH50LN0ZxJLBnBqfPMNZ_6EQeWWrO72MwQU8ZlD-4fSRcy2m6EWmdvBQmHKl6iGDyX4-LWGb6GL1rE3y9f6k83Wvc_glz97iqZ8lscfHBvjHvDKLPxe_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظۀ ورود پیکرهای مطهر خانوادۀ شهید رهبر شهید انقلاب به حرم حضرت امیرالمؤمنین(ع) روی دوش عراقی‌ها   @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/448126" target="_blank">📅 04:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448124">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c29e340931.mp4?token=hIqlQuYPIeVY8K2TBU8tKo29ijcNYtoTqQk7pIARksfv6aTYukpXgc8jxL0Y9DPE8SBFhh_cMiZJyZZD-iO0hGXHdepptu-z2W_ELg2g4UPmTJFxB6i3DQR4ErJ9CdqZrdqsgqnZdKWotqqcnGIApo7bjckzx3rfmB2m36QgLmhyRv0mEipVpV_ck654cEBBUEkYj70N1SvtkckxECrgUX2AXRdyWwwspehq80czuFSLMNxj77xJg7Mb0bvZnDvI-Ytnb1QbejTllpQFBfaHPstj_nAa7Jn1UupfeOPA65OeLY0oLEKHXEeBVtXn5PKNfIqueggE5SdLDdXdbcFVAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c29e340931.mp4?token=hIqlQuYPIeVY8K2TBU8tKo29ijcNYtoTqQk7pIARksfv6aTYukpXgc8jxL0Y9DPE8SBFhh_cMiZJyZZD-iO0hGXHdepptu-z2W_ELg2g4UPmTJFxB6i3DQR4ErJ9CdqZrdqsgqnZdKWotqqcnGIApo7bjckzx3rfmB2m36QgLmhyRv0mEipVpV_ck654cEBBUEkYj70N1SvtkckxECrgUX2AXRdyWwwspehq80czuFSLMNxj77xJg7Mb0bvZnDvI-Ytnb1QbejTllpQFBfaHPstj_nAa7Jn1UupfeOPA65OeLY0oLEKHXEeBVtXn5PKNfIqueggE5SdLDdXdbcFVAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طواف پیکرهای مطهر خانوادۀ شهید رهبر شهید انقلاب بر ضریح امیرالمومنین (ع)  @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/448124" target="_blank">📅 04:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448123">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c199b2f2f.mp4?token=ZYJqCLPtg01oAEcnQINNyeA4tj51gabe2kUCj2bbrFCkWzqXYNY0e0Q4zY2T2XNzV_LuDPHA7vDkq8yiW9QSCZB9iP7-u4IzEvAYqa9nmhmSHgWIwq045_XQcV9tyKF3bDrSWSCD2YYAZkzUbPnxpyGRMgpJ0iaJbBBzZT-PG6HZ8-N1Ua8AR_Ke3ShaIiPjQEqQS6qaDMnGifaDRB8BkyLPGklZVc8pkUIg8GkMpe024_cssteSBG_LYa6DKCtHm61q_CSGvPoBvWy8U0_K1-lsj0d56YhmgOIQjgZnXp0pHOaoVPpP5iNCvwybpuip4stB6H7aR6M677mQ4ohVKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c199b2f2f.mp4?token=ZYJqCLPtg01oAEcnQINNyeA4tj51gabe2kUCj2bbrFCkWzqXYNY0e0Q4zY2T2XNzV_LuDPHA7vDkq8yiW9QSCZB9iP7-u4IzEvAYqa9nmhmSHgWIwq045_XQcV9tyKF3bDrSWSCD2YYAZkzUbPnxpyGRMgpJ0iaJbBBzZT-PG6HZ8-N1Ua8AR_Ke3ShaIiPjQEqQS6qaDMnGifaDRB8BkyLPGklZVc8pkUIg8GkMpe024_cssteSBG_LYa6DKCtHm61q_CSGvPoBvWy8U0_K1-lsj0d56YhmgOIQjgZnXp0pHOaoVPpP5iNCvwybpuip4stB6H7aR6M677mQ4ohVKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طواف پیکرهای مطهر خانوادۀ شهید رهبر شهید انقلاب بر ضریح امیرالمومنین (ع)
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/448123" target="_blank">📅 04:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448122">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">شلیک موشک از ایران به سمت ناوهای آمریکایی
🔹
رسانه «میدل ایست اسپکتیتور» بامداد چهارشنبه مدعی شد که ایران چندین موشک ضدکشتی و پهپاد به سمت شناورهای جنگی نیروی دریایی آمریکا در دریای عمان شلیک کرده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/448122" target="_blank">📅 04:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448121">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/037f55cd4c.mp4?token=lQeTrOkeO_0CEeYVYubjZltLaSuWIs3SKDf7V377kNe2yTLW4Qpo1jbARgIZGlFgqTz2Yeee1ZUauek6jicDmSXaULdOSb62t0BgJT_bSl8NJE8IdkWPYUF2-0B2JuIvMUKUIZahmVjiBDRm7s0TvGBGwsC0iDeAOzROZK4e8XUq-nI40xVwdSmdQUMOU3RxcE_oB69FZxLX3QBdvBiEHTbkzgxb7b_MySeSPse1MLQvjBe_VP0_0da8yRU0VOW4ZBsGrcHkWQbEvAoXB4EkFVNPgRA9q2tkwoC2gAta0CMI_NsVu5BcRFAIZ7M0s-0OsnGogqG1A1-BSRiiG-p_1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/037f55cd4c.mp4?token=lQeTrOkeO_0CEeYVYubjZltLaSuWIs3SKDf7V377kNe2yTLW4Qpo1jbARgIZGlFgqTz2Yeee1ZUauek6jicDmSXaULdOSb62t0BgJT_bSl8NJE8IdkWPYUF2-0B2JuIvMUKUIZahmVjiBDRm7s0TvGBGwsC0iDeAOzROZK4e8XUq-nI40xVwdSmdQUMOU3RxcE_oB69FZxLX3QBdvBiEHTbkzgxb7b_MySeSPse1MLQvjBe_VP0_0da8yRU0VOW4ZBsGrcHkWQbEvAoXB4EkFVNPgRA9q2tkwoC2gAta0CMI_NsVu5BcRFAIZ7M0s-0OsnGogqG1A1-BSRiiG-p_1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور گستردۀ مردم در خیابان‌های شهر نجف، ساعتی پیش از آغاز مراسم تشییع پیکر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/448121" target="_blank">📅 04:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448120">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">پزشکیان راهی نجف شد
🔹
رئیس‌جمهور، به‌منظور شرکت در مراسم استقبال از پیکر مطهر رهبر شهید انقلاب، دقایقی پیش تهران را به مقصد نجف اشرف ترک کرد. @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/448120" target="_blank">📅 03:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448119">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d7aff7c.mp4?token=L13tEOV29xNacQMfrKGGAgSREphIc63yeQoEUCVwKwLXt9gHlqxoq0O233APhldKrIoxucJe5DrvrIc7qbhe1HJsr-ZjQv-yNJ9_sGQeyLQFS2c0iBKJxoinrJrxUyZBxNo3MVhAV_e9Gng6ZTd-kMuddqguKx9TOVLxp8p1FZ3yWyF0gbNpFzzVHolUJ7y1BTqkKp4ekwnAw9CuuwA_jCJzXHFOb8qIrJVLpKoUmp1cpNEgolS8wq0OTuJjztnTintjiZbiwm5h72cNE6M-0Lfgm3fpMDd2-87KO-emKxBm2qakzN0aDnBmWoIfQfC1dvFkFyAVhLajM0J-KGJWYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d7aff7c.mp4?token=L13tEOV29xNacQMfrKGGAgSREphIc63yeQoEUCVwKwLXt9gHlqxoq0O233APhldKrIoxucJe5DrvrIc7qbhe1HJsr-ZjQv-yNJ9_sGQeyLQFS2c0iBKJxoinrJrxUyZBxNo3MVhAV_e9Gng6ZTd-kMuddqguKx9TOVLxp8p1FZ3yWyF0gbNpFzzVHolUJ7y1BTqkKp4ekwnAw9CuuwA_jCJzXHFOb8qIrJVLpKoUmp1cpNEgolS8wq0OTuJjztnTintjiZbiwm5h72cNE6M-0Lfgm3fpMDd2-87KO-emKxBm2qakzN0aDnBmWoIfQfC1dvFkFyAVhLajM0J-KGJWYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود خیل عظیم عراقی‌ها به نجف، جهت شرکت در مراسم تشییع پیکر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/448119" target="_blank">📅 03:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448118">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/619796c58d.mp4?token=BhMQNvZISy3D3bC9AvIuV80NEzL4yAmTOEgnF-TZzuEHw7X0cqiFu0v26LTBNxMK9JhI1u1yx4V7byB6hrHtZGhLqukWmZzVgnJ0sF_4gTdV4zRcr4rmISH2XAffslwX4eWIofFhC5VDYa8DkLAplbb8MLJ3g0jcACJWfSLcWZ_XQmeDbHD4xp-O5e7mGHStAX3RYtK-GoXf2iMXSRPOC8TKM0iPi17adbWQyC2IUduOTXm9g_VaUsfVrV_PQl2JataGfx0HHFOA5B-UUhkU4HuZPTJzUthnmNIB9J7pVzlfB0kgPO-IB1WT0WC1HsYP_d-jU8LYKMwFZapdSDdq1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/619796c58d.mp4?token=BhMQNvZISy3D3bC9AvIuV80NEzL4yAmTOEgnF-TZzuEHw7X0cqiFu0v26LTBNxMK9JhI1u1yx4V7byB6hrHtZGhLqukWmZzVgnJ0sF_4gTdV4zRcr4rmISH2XAffslwX4eWIofFhC5VDYa8DkLAplbb8MLJ3g0jcACJWfSLcWZ_XQmeDbHD4xp-O5e7mGHStAX3RYtK-GoXf2iMXSRPOC8TKM0iPi17adbWQyC2IUduOTXm9g_VaUsfVrV_PQl2JataGfx0HHFOA5B-UUhkU4HuZPTJzUthnmNIB9J7pVzlfB0kgPO-IB1WT0WC1HsYP_d-jU8LYKMwFZapdSDdq1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یزلۀ عراقی‌ها در محوطۀ حرم حضرت امیرالمومنین(ع) با تصویر رهبر شهید انقلاب  @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/448118" target="_blank">📅 03:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448117">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🎥
نتانیاهو: دادن اف-۳۵ به ترکیه تعادل قدرت را در خاورمیانه از بین خواهد برد
🔹
ترکیه اهداف و جاه‌طلبی‌های تهاجمی دارد. آن‌ها می‌خواهند امپراطوری عثمانی را احیا کنند.
🔹
امپراطوری عثمانی فقط شامل ترکیه نبود، بلکه خیلی از جاهای دیگر را هم در بر می‌گرفت؛ شامل سوریه…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/448117" target="_blank">📅 03:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448116">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bce9bc8fdb.mp4?token=rKvuAHNzHd4O15aNdklGkZU5SeV_-BGpGgNcb909ctm-yix6x6QZs_08aI8GqcWzo5z_gRhqqcNNKq7aJ6KIyEJyP7Tch-P7LaTkKm2_k4O154Vu5GuHLvihu0cKjBYuSe_2k0fVjMDWAOlwOXhcI9CkSXVDqnMsFFZuCS-UvXBjrAHkkitjLyuHHUN3E4rHcvDyoQYScG03IXUmL9KVH6xeXV-UmY0kO1hCQapefgpDqdvAs4yyAv-R5krUFYGN22ZhhrAAk6GaDTLnTbQ282RZ0n0WH1IKZ0TZ9065AMk5DdHHqxJY1OJzGCmt8hr26WWRspD6gxdbNjSV55kLfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bce9bc8fdb.mp4?token=rKvuAHNzHd4O15aNdklGkZU5SeV_-BGpGgNcb909ctm-yix6x6QZs_08aI8GqcWzo5z_gRhqqcNNKq7aJ6KIyEJyP7Tch-P7LaTkKm2_k4O154Vu5GuHLvihu0cKjBYuSe_2k0fVjMDWAOlwOXhcI9CkSXVDqnMsFFZuCS-UvXBjrAHkkitjLyuHHUN3E4rHcvDyoQYScG03IXUmL9KVH6xeXV-UmY0kO1hCQapefgpDqdvAs4yyAv-R5krUFYGN22ZhhrAAk6GaDTLnTbQ282RZ0n0WH1IKZ0TZ9065AMk5DdHHqxJY1OJzGCmt8hr26WWRspD6gxdbNjSV55kLfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
#فیلم
|
عزاداری عراقی‌ها در کربلا و دعا بر آقای شهید ایران
@rahbari_plus</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/448116" target="_blank">📅 03:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448115">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52d30bf222.mp4?token=nAsYvAFos4CKag5HMuD-BG6hMSew7XTeci8I0VFCnhQyfi7806B9-CyrY2pabNWGiqovkG0z1PXy5IaIU9e2NStVC2sDdPvUZqL7HirgpQ52Uj51qg5lYljVOlhjcszRl2vt9JT16qTzq3kn9DDGrEt-aCJhL-Q--r1PJqmM7b1Ysbocm2KkieqcqHyTbukeVGzSnQvKASwf6FEeyOu-R1fGS1yPifD-WjVwhLDH5ntJN0_mL9hGzgs-mnx6JCp7x5QTlucPfSUkxPAzl5OqkIXSVJ1a9vs1elLvdk37zCFBl6uiY2s-iS7GT00pYDY-7HHMM_B_uWeOSYs7YpvB1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52d30bf222.mp4?token=nAsYvAFos4CKag5HMuD-BG6hMSew7XTeci8I0VFCnhQyfi7806B9-CyrY2pabNWGiqovkG0z1PXy5IaIU9e2NStVC2sDdPvUZqL7HirgpQ52Uj51qg5lYljVOlhjcszRl2vt9JT16qTzq3kn9DDGrEt-aCJhL-Q--r1PJqmM7b1Ysbocm2KkieqcqHyTbukeVGzSnQvKASwf6FEeyOu-R1fGS1yPifD-WjVwhLDH5ntJN0_mL9hGzgs-mnx6JCp7x5QTlucPfSUkxPAzl5OqkIXSVJ1a9vs1elLvdk37zCFBl6uiY2s-iS7GT00pYDY-7HHMM_B_uWeOSYs7YpvB1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار هیهات مناالذله عراقی‌ها در حرم حضرت امیرالمومنین(ع)
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/448115" target="_blank">📅 03:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448113">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fe2e701a0.mp4?token=c1cCYrJs3NU6u1purTpJLALmIbD0mPTO0phd8fnLihvNm7HNbtCSAVMq-d6KrW-iXw2_qgfl6og5DibOYCV165WgN5VI0N7pRyZjCiH29NFSUzYr1BMSFT6Jd9KN4K-tJowYj_utw-kPrTJ37nlrBXa9Ga7jBlRbndlBzmtb9f5c7dIwMCSSV4f0YOLaRaScUqWasYQh0KZG9b72lodE-WhPs4SW8be9gikfa3Sw2yjdaX8T5fdBwsQYbX3YFlnklgM-qZ-RuuiQbzr8uaZgUTI9bFlNXqj_5HUAPTnZ0lbFWx5jyi0Nhn_GIVT9Ilpfj-w6740l8VDwKeffgwreGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fe2e701a0.mp4?token=c1cCYrJs3NU6u1purTpJLALmIbD0mPTO0phd8fnLihvNm7HNbtCSAVMq-d6KrW-iXw2_qgfl6og5DibOYCV165WgN5VI0N7pRyZjCiH29NFSUzYr1BMSFT6Jd9KN4K-tJowYj_utw-kPrTJ37nlrBXa9Ga7jBlRbndlBzmtb9f5c7dIwMCSSV4f0YOLaRaScUqWasYQh0KZG9b72lodE-WhPs4SW8be9gikfa3Sw2yjdaX8T5fdBwsQYbX3YFlnklgM-qZ-RuuiQbzr8uaZgUTI9bFlNXqj_5HUAPTnZ0lbFWx5jyi0Nhn_GIVT9Ilpfj-w6740l8VDwKeffgwreGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خودروی حامل پیکر مطهر رهبر شهید انقلاب به محوطه حرم مطهر امیرالمؤمنین(ع) رسید  @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/448113" target="_blank">📅 03:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448112">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‌
🔹
خبرنگار صداو‌سیما: براثر اصابت ترکش پرتابه‌های دشمن در بندر صیادی و تجاری شهرستان سیریک، چندین نفر مصدوم شدند. @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/448112" target="_blank">📅 03:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448111">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a4d8e44b3.mp4?token=sv9yCk1G6I1MMwtlYpn9NJhlp8ZhX26Ad7y2mYmCRnoHXyfsR1NC2CQUky8QuMyk_P1jU_mIn1V3CnJTMnc1nbl_7rL8eUIXvkLqRA_yxEea5A-Nzmq1BjC56QOj7EH1_akcIJpa8toR1KJGBASq7KueZcWtnVywVL9Yxl7aVBp0Q3UVBXtPRjGGNYSkrgf88guGcv1XqAzC-A4CzKqbf4kJBT4eYf2EAUS4AaE38oYRQMV5UxOvO4uxV0-aS0szuBFJJvVU6kjY0usM6NllQ6QRR7NUBDsC-YhVkbx--CPlmzxODWr01Y9lsgJ0P_JAn4BYfgEycnlQ8EfXLY7MTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a4d8e44b3.mp4?token=sv9yCk1G6I1MMwtlYpn9NJhlp8ZhX26Ad7y2mYmCRnoHXyfsR1NC2CQUky8QuMyk_P1jU_mIn1V3CnJTMnc1nbl_7rL8eUIXvkLqRA_yxEea5A-Nzmq1BjC56QOj7EH1_akcIJpa8toR1KJGBASq7KueZcWtnVywVL9Yxl7aVBp0Q3UVBXtPRjGGNYSkrgf88guGcv1XqAzC-A4CzKqbf4kJBT4eYf2EAUS4AaE38oYRQMV5UxOvO4uxV0-aS0szuBFJJvVU6kjY0usM6NllQ6QRR7NUBDsC-YhVkbx--CPlmzxODWr01Y9lsgJ0P_JAn4BYfgEycnlQ8EfXLY7MTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درهای حرم مطهر امیرالمومنین(ع) به‌منظور آماده‌سازی برای استقبال از امام شهید بسته شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/448111" target="_blank">📅 03:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448110">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ffdade163.mp4?token=oNJUusqQ0a7jZjMyvpyTrUohZNpTbP-XxNcA_lIJ_K1dH-w7QEmCW75ArYdKwBP0zWjCXFNYGFUxfSvM-11-8n2M7n7qfkl-OX7O6vU1CRO8Maus3xJxqtp57CszONRasyORjtVXnQYfpiX9fznvLEglZlBknjrP_xvduMlIEZSTyJulS6zYR3h48UuHO79LWyQPGvhBxieWtdv-lChq_UwNeahqoeHt6FU_6ZHPc24dzgKmAo62EqeGJh1YLOsCZvGGfefqT5qPOePEXacc4qyja5_63ttCaH5LaMbh_SXeyCrub7_IMEqip44ntubcH8MCLcTERSZ_YSenxHqPpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ffdade163.mp4?token=oNJUusqQ0a7jZjMyvpyTrUohZNpTbP-XxNcA_lIJ_K1dH-w7QEmCW75ArYdKwBP0zWjCXFNYGFUxfSvM-11-8n2M7n7qfkl-OX7O6vU1CRO8Maus3xJxqtp57CszONRasyORjtVXnQYfpiX9fznvLEglZlBknjrP_xvduMlIEZSTyJulS6zYR3h48UuHO79LWyQPGvhBxieWtdv-lChq_UwNeahqoeHt6FU_6ZHPc24dzgKmAo62EqeGJh1YLOsCZvGGfefqT5qPOePEXacc4qyja5_63ttCaH5LaMbh_SXeyCrub7_IMEqip44ntubcH8MCLcTERSZ_YSenxHqPpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یزلۀ جوانان عراقی در سوگ رهبر شهید انقلاب در بین‌الحرمین  @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/448110" target="_blank">📅 02:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448109">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a6142117.mp4?token=QQDYeN-4Q_fk9alo0flbCi_L_QZBLoAk8qqO2nK2Gi530l20rlf6Wxis6_vutKLuyME__Za8q5nasUu3zkpo8X-TyoqoigidJBOy4SEQaH3utvYNFszRozn1cffETefJHAIg_SMaUcEzBtox5dTlA-aKM4SSfLGql5rBPAfJS_5b2jSPHkqO37xJgztQE7p7LKI4aHaK3o-3dsYDiAfpqoz4bO_kyp8nAUMOnczHT2YOQuOp7eaNsitxhKVtave7G8w6Ob00PAZ_qGqH5xGnAKT_UMnxWAmTbKfwMLqTfIHZi4y6i0SligY0qKuO16G-CY4dfd9YSfOnGmfgIc0NOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a6142117.mp4?token=QQDYeN-4Q_fk9alo0flbCi_L_QZBLoAk8qqO2nK2Gi530l20rlf6Wxis6_vutKLuyME__Za8q5nasUu3zkpo8X-TyoqoigidJBOy4SEQaH3utvYNFszRozn1cffETefJHAIg_SMaUcEzBtox5dTlA-aKM4SSfLGql5rBPAfJS_5b2jSPHkqO37xJgztQE7p7LKI4aHaK3o-3dsYDiAfpqoz4bO_kyp8nAUMOnczHT2YOQuOp7eaNsitxhKVtave7G8w6Ob00PAZ_qGqH5xGnAKT_UMnxWAmTbKfwMLqTfIHZi4y6i0SligY0qKuO16G-CY4dfd9YSfOnGmfgIc0NOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقی‌ها با پرچم‌های سرخ انتقام راهی مراسم تشییع امام شهید می‌شوند
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/448109" target="_blank">📅 02:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448108">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a12f091e5f.mp4?token=kOUO16beiMBcjjzj695WfK11eV8KqxgHXOFTiJptD_062AufONiKv2gfFBrokZPTpJMhxmkMiNQ-Jt773mBVhlBlZu7JXEfVCWPklhpCh_day483wbDY-cV9t0oDCc6Jv14zTfJLjEqnGhORvX805n63NAxrYfycvlRr8dolC73sq26cq_GyDHU98KHODZs7h0rxkBNYa1qw6x-pFJh4ynHCwTkrtNQ9sWucc5sqeIvA42j7xiO9cE2B18MV8AO823jOKNy-C4LMFu7khL9pefUWlgoqzFygYVxcNSiTVaKHEuUaClik8bhOohoLgH_CrVjD2rsfJAvMAiVXrGPNEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a12f091e5f.mp4?token=kOUO16beiMBcjjzj695WfK11eV8KqxgHXOFTiJptD_062AufONiKv2gfFBrokZPTpJMhxmkMiNQ-Jt773mBVhlBlZu7JXEfVCWPklhpCh_day483wbDY-cV9t0oDCc6Jv14zTfJLjEqnGhORvX805n63NAxrYfycvlRr8dolC73sq26cq_GyDHU98KHODZs7h0rxkBNYa1qw6x-pFJh4ynHCwTkrtNQ9sWucc5sqeIvA42j7xiO9cE2B18MV8AO823jOKNy-C4LMFu7khL9pefUWlgoqzFygYVxcNSiTVaKHEuUaClik8bhOohoLgH_CrVjD2rsfJAvMAiVXrGPNEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای خیابان‌های منتهی به حرم امیرالمومنین(ع)، ساعاتی پیش از آغاز مراسم تشییع رهبر شهید انقلاب @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/448108" target="_blank">📅 02:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448107">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2c0b2f180.mp4?token=f694QWk5wJKixWXH2i3OC7YUekUUW6w02dKVM_KvkJt8Iw70-buZQZcTPsSRmECa9ZwCvctsZpyoYazC3Kz24wL5NJH8Z_hkU2uHZdBkHyd2F9CYDE_L6BFk23jmE22g5donSaJk5wI9X2L42MMe1mglGQ4SwgTgYCCm6mbZPGtoL5XapZQQlP0pw7ot6EX9fepM7Y9mVTUjdPYvDROthVaAdkiLHwqR8l40nvEcaJYMy8cQDAFGKw-DP3-S3tLoTnNwJBMKF32eWxtEehUeRBkjp0qVkrnv11Q-8aReMAXrfw_RD0vraTdL57QjDnF_d6xPfxASl6yDgOdp7yE_dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2c0b2f180.mp4?token=f694QWk5wJKixWXH2i3OC7YUekUUW6w02dKVM_KvkJt8Iw70-buZQZcTPsSRmECa9ZwCvctsZpyoYazC3Kz24wL5NJH8Z_hkU2uHZdBkHyd2F9CYDE_L6BFk23jmE22g5donSaJk5wI9X2L42MMe1mglGQ4SwgTgYCCm6mbZPGtoL5XapZQQlP0pw7ot6EX9fepM7Y9mVTUjdPYvDROthVaAdkiLHwqR8l40nvEcaJYMy8cQDAFGKw-DP3-S3tLoTnNwJBMKF32eWxtEehUeRBkjp0qVkrnv11Q-8aReMAXrfw_RD0vraTdL57QjDnF_d6xPfxASl6yDgOdp7yE_dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای حرم مطهر امیرالمومنین(ع) ساعاتی پیش از آغاز تشییع پیکر رهبر شهید انقلاب   @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/448107" target="_blank">📅 02:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448106">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">◾️
صابرین‌نیوز: هزاران نفر از عزاداران عراقی در پارکینگ‌ها منتظر هستند تا وسایل نقلیه برای انتقال آن‌ها به کربلا فراهم شود تا در مراسم تشییع پیکر امام شهید شرکت کنند.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/448106" target="_blank">📅 02:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448105">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‌ ادعای آمریکا دربارۀ دنباله‌دار بودن تجاوزات به ایران
🔹
یک مقام آمریکایی به شبکۀ سی‌ان‌ان گفت:‌ این حملات تنبیهی هستند، نه متناسب و به این زودی‌ها تمام نخواهند شد.
🔹
آکسیوس نیز به نقل از یک مقام آمریکایی گزارش داد: اهداف در ایران شامل سامانه‌های پدافند هوایی،…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/448105" target="_blank">📅 02:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448103">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f14ece7277.mp4?token=ZTE76aTxjP2mgPWSttLximZVPLal83SJfxuwM2WgriqXbsLEd8zfqNJpQq1FhT0KgUtv3jHVzOzj89rLFsUvhM6Lvro6fEqlf9vgyFvtO56UZaaCJyR70hurep2i74uuAtFFw5J6H2DOnFpNC7im_GNzk02rVX-IfQLUWc8tyQv_H74GNsiD5fvzVBeXOiSykL8K-k31PnBIEQi8flsXfijF3516WXsWuACGTibG0pqt3ejYRmGS312CBs3qHLOorShmyPHGvsS3mDIGDI0HQRkYP_cgwLQzjxSFokRqgb4q0G44tqjRXmBn0gZLG0TTTWHEYmL8TDGCO5aNqUzquA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f14ece7277.mp4?token=ZTE76aTxjP2mgPWSttLximZVPLal83SJfxuwM2WgriqXbsLEd8zfqNJpQq1FhT0KgUtv3jHVzOzj89rLFsUvhM6Lvro6fEqlf9vgyFvtO56UZaaCJyR70hurep2i74uuAtFFw5J6H2DOnFpNC7im_GNzk02rVX-IfQLUWc8tyQv_H74GNsiD5fvzVBeXOiSykL8K-k31PnBIEQi8flsXfijF3516WXsWuACGTibG0pqt3ejYRmGS312CBs3qHLOorShmyPHGvsS3mDIGDI0HQRkYP_cgwLQzjxSFokRqgb4q0G44tqjRXmBn0gZLG0TTTWHEYmL8TDGCO5aNqUzquA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای حرم مطهر امیرالمومنین(ع) ساعاتی پیش از آغاز تشییع پیکر رهبر شهید انقلاب   @Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/448103" target="_blank">📅 02:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448102">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🎥
آخرین جزئیات حملات به جنوب ایران از زبان خبرنگار صداوسیما
🔹
وضعیت در شهرهای بندرعباس، سیریک و قشم عادی است. @Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/448102" target="_blank">📅 02:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448101">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c86877093a.mp4?token=ETiYtFCaBUhszCHxFU-DselmUCUj5nWZwYJz8Q58vlNMvbkFnnq9gNsmsyV3p9dMiRaGs5WAKQ2FKFUc3hX2-IumR0eMojpXiLhjcKAug1eehOmI1t1JJHdjoFc5D5c7IYat9iPYuC1CKwesK9qUgID6Hw0C9b8KkdWYLiKoblWS7HURBCaOgtrbqR7c2Ne3bp_MfCcsS9mosAb0tLNd6xrTiYXYW-Gd5XL-T0GDwKZ8rUdypEhthS4loU-IItD6k8-u9zL55wzuOfwYFpbJnhVxHO2j_JxACc0QGGAKF6Xr2GKyUYcvv5e3keetAU0mHuxJuG7Bl9qH-lb2_dm2zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c86877093a.mp4?token=ETiYtFCaBUhszCHxFU-DselmUCUj5nWZwYJz8Q58vlNMvbkFnnq9gNsmsyV3p9dMiRaGs5WAKQ2FKFUc3hX2-IumR0eMojpXiLhjcKAug1eehOmI1t1JJHdjoFc5D5c7IYat9iPYuC1CKwesK9qUgID6Hw0C9b8KkdWYLiKoblWS7HURBCaOgtrbqR7c2Ne3bp_MfCcsS9mosAb0tLNd6xrTiYXYW-Gd5XL-T0GDwKZ8rUdypEhthS4loU-IItD6k8-u9zL55wzuOfwYFpbJnhVxHO2j_JxACc0QGGAKF6Xr2GKyUYcvv5e3keetAU0mHuxJuG7Bl9qH-lb2_dm2zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیل جمعیت عراقی‌ها در خیابان‌های منتهی به حرم امیرالمومنین(ع) برای شرکت در مراسم تشییع رهبر شهید انقلاب  @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/448101" target="_blank">📅 02:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448100">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07c3c6f556.mp4?token=KBDPcjvl1zqok54z5Y5gkWnP7Feqjw6O8Z3-PyjVDK4gZjskuBv6P3p0KCeqdyuZaYNvl1nrrBDS7EIJy91Z1wEnUpFDRojopOBAI6kwJJEHOyKqieHawXBnr2TzNyEIfpqzJqDbptrHlwTXHcJbnLlrxqGgZ_cKo0yU_o0IfPwpDWJaV9-WSqvPt24OZWNE17wjojMCjK7lZYjMTTVYn35M-V_EnvcTNAp84l1cwTwX_9DsVxSQpit2snhmH6WbfeimRFf7xWKh5bX0vfgpaKfhaXPobdqqpH0iYf2Bz6MRjCmgKlyE4N1_IlshCWzHpnsKIX6JxgKdbQMT7LjBfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07c3c6f556.mp4?token=KBDPcjvl1zqok54z5Y5gkWnP7Feqjw6O8Z3-PyjVDK4gZjskuBv6P3p0KCeqdyuZaYNvl1nrrBDS7EIJy91Z1wEnUpFDRojopOBAI6kwJJEHOyKqieHawXBnr2TzNyEIfpqzJqDbptrHlwTXHcJbnLlrxqGgZ_cKo0yU_o0IfPwpDWJaV9-WSqvPt24OZWNE17wjojMCjK7lZYjMTTVYn35M-V_EnvcTNAp84l1cwTwX_9DsVxSQpit2snhmH6WbfeimRFf7xWKh5bX0vfgpaKfhaXPobdqqpH0iYf2Bz6MRjCmgKlyE4N1_IlshCWzHpnsKIX6JxgKdbQMT7LjBfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
وزارت برق کویت از قطعی ناگهانی برق در نقاط مختلف این کشور خبر داد.  @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/448100" target="_blank">📅 02:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448098">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44e6b6e6b8.mp4?token=vVAbx-qD5jsPArCCOLfGFysfY67aPjsUeOxlrP2cenSAcTBvcIUdPVtYg9VaccgDd3tM3n_5ZUAyVgSJOgD8LZClNfoq881EwEP4UoweCgIZV3gCiZfah8z-9w56pTeT6ICo1Hd09EykMaTL7z_2JJ0uYQfvo08PaQ9aoA5SU6sqQsezq6yIvjp3cnp8icMfoXPgikb20omb68254vUG-D3x5eexPpZ41w2-ie_Hb0fjhIxZX3j1e521eZOU-BQsRyxbtTI04V1VWvSYBnG0TTofuWjViVcYPOp9TCeexIxDYcVhYJhnQNbX0KAtzO_3NIr54C25CAgmcx7BCQrzVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44e6b6e6b8.mp4?token=vVAbx-qD5jsPArCCOLfGFysfY67aPjsUeOxlrP2cenSAcTBvcIUdPVtYg9VaccgDd3tM3n_5ZUAyVgSJOgD8LZClNfoq881EwEP4UoweCgIZV3gCiZfah8z-9w56pTeT6ICo1Hd09EykMaTL7z_2JJ0uYQfvo08PaQ9aoA5SU6sqQsezq6yIvjp3cnp8icMfoXPgikb20omb68254vUG-D3x5eexPpZ41w2-ie_Hb0fjhIxZX3j1e521eZOU-BQsRyxbtTI04V1VWvSYBnG0TTofuWjViVcYPOp9TCeexIxDYcVhYJhnQNbX0KAtzO_3NIr54C25CAgmcx7BCQrzVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور و عزاداری مردم عراق در شهر نجف، ساعاتی پیش از آغاز مراسم تشییع رهبر شهید انقلاب  @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/448098" target="_blank">📅 02:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448096">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roJ-Y2IKEHi1VT9cI8OqEBhN_mvEzWnKYT6sZ5aLzunwlXk6NGkSRl7S2-3bGTTHYAtckuYk6eZBD8AbsLBssTsn_7SZmmYG6AtkhdtaZgVdlzvdQ6qpqYkcp5SZ3o7Z4yxy7deqNpf_nO5a-QRe4TdAoV47p2B1SMhVKaCTQQ_LTxXCVyK4kNWoU60HCIrMOVCe5EO69sZLoB2kPLbsX7ACPvKcaTTaXkC3D1VP7wYGP3biR4VJy8XsKMvRXUtGRtEDbt0j7_JQrkfx_wLVCCiXsoUx3hM9mzWMvT70YXvCeuQvmkbBLwbuuzHFtMVELOrVBQFs-mb1riWzs7e2Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوئیس فاتح ماراتن پنالتی‌ها شد
حذف خامس و دیاز و رفقا از جام‌جهانی
نتیجه ۱۲۰ دقیقه: کلمبیا ۰ - ۰ سوئیس
نتیجه ضربات پنالتی: کلمبیا ۳ - ۴ سوئیس
@Sportfars</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/448096" target="_blank">📅 02:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448094">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9161434e0c.mp4?token=HKD85E1C9E_yEz-gqZzsoTVIKaySWxIlLI6H01ZY8TswWRgUeFLTUENHT_2lJj1twgPKUY5WXrpcZGINhShvHzPjUJgAjfcI0Ns2EPmpLH77FCfyjdtp8eB8yApaCZfOU21CMrBwRZ6jDVG68CKlCRX18oZNtNhHqCyP3ECf15uuq3A6vGz8Ymod4b5pv0Y5d2RXU0rEptXdjUFzURvV5pnqh0sbULnj8mH733efaYDttc3icRqJIjy8iwaHt7ssPN3PS5wau-B29UY6JprUSeb8UblT8INDlYScP7G4kvefADzv79R_49Q16AVmAPVWXBnDjl1jhIflKqcUmVaKRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9161434e0c.mp4?token=HKD85E1C9E_yEz-gqZzsoTVIKaySWxIlLI6H01ZY8TswWRgUeFLTUENHT_2lJj1twgPKUY5WXrpcZGINhShvHzPjUJgAjfcI0Ns2EPmpLH77FCfyjdtp8eB8yApaCZfOU21CMrBwRZ6jDVG68CKlCRX18oZNtNhHqCyP3ECf15uuq3A6vGz8Ymod4b5pv0Y5d2RXU0rEptXdjUFzURvV5pnqh0sbULnj8mH733efaYDttc3icRqJIjy8iwaHt7ssPN3PS5wau-B29UY6JprUSeb8UblT8INDlYScP7G4kvefADzv79R_49Q16AVmAPVWXBnDjl1jhIflKqcUmVaKRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور و عزاداری مردم عراق در شهر نجف، ساعاتی پیش از آغاز مراسم تشییع رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/448094" target="_blank">📅 02:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448093">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1491c00885.mp4?token=q6_gBkWP0ehTg5Fi0fZUngSEPo4xO1CqpLx7Gv4fnunQU-t0r94tg3xlatQXRuFxQOaxZJJz2fUM0pAWZwQZm8ckvwhk8xj-n-qjq0nX0LxRWoe7BwwVy910E4Cxl8AEEvtnERM73B__9IzXlwStn5qF0thvB-rSM2st3JLIam7AYv5ZFftYZtkneCXrRRgXpsO3k2ytE0wyqD85sPwkiM8ahULdhrTM5-eonzMoGU8xV1HbeB4aizZxTxno5PHN1YAhR4udyj7pwoC0yihqEYjYwHmUp2y2JIHOTs4fPo_8SVRbN3YFDKIS_ZfSMm33Ppe36kjMkbLsRtXwIeGsCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1491c00885.mp4?token=q6_gBkWP0ehTg5Fi0fZUngSEPo4xO1CqpLx7Gv4fnunQU-t0r94tg3xlatQXRuFxQOaxZJJz2fUM0pAWZwQZm8ckvwhk8xj-n-qjq0nX0LxRWoe7BwwVy910E4Cxl8AEEvtnERM73B__9IzXlwStn5qF0thvB-rSM2st3JLIam7AYv5ZFftYZtkneCXrRRgXpsO3k2ytE0wyqD85sPwkiM8ahULdhrTM5-eonzMoGU8xV1HbeB4aizZxTxno5PHN1YAhR4udyj7pwoC0yihqEYjYwHmUp2y2JIHOTs4fPo_8SVRbN3YFDKIS_ZfSMm33Ppe36kjMkbLsRtXwIeGsCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملات شدید رژیم‌صهیونیستی به جنوب لبنان
🔹
المیادین: مناطق گسترده‌ای در جنوب لبنان هدف حملات هوایی و توپخانه‌ای اشغالگران قرار گرفته است.
@Farsna
- Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/448093" target="_blank">📅 02:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448092">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f16a3b5be.mp4?token=NF-oLghiwvG5SZITnp5U9C8V1hLxj4SDevLfO5hAmFHcyL3q-YcDZdT604hXEvsoobxdmZPEYNelj7mrRfxoqWut2YItv4jEolGFGr9qpc7o-0lpy-ubzPw6UWFKqw40rSmqzx6TnqllxSj9PbHdvIOG4sDSbgz2PMEnfen3qbv2fk5IqCJKoplYBNhgCdevVmKIrCqwqYqcG8vNL6kelbwZ14iwmmcAw03-q3O_DwVHIEuhAy8FNOk9Mw3ukoainwOKIgrm-miLga2nVUNDmdsdZcpbmDGt4yVUewjGwh2lbTi52oKHlDU-pjEnrgGapzdZY-9oBT2jx_w0WluG9DFQQ9ZCfZSz1haPvEQDZBsQmPpgZwzy92fQbG-7HitQni6KgoeH4n_h6BNTk8PwrXIe2VQswg7MBGOWR59_yHl882TMyLWJ_f2Lp68Cpn67ZrMcIiKSnn01FeD7eln56eYuqTXMEEHzMAlask8ZpDpnJlNB4rzY65dLJPVn2Mvbh8VSWniCrDVFnLfXUnSc93otUbqhAkvZn9tv2RF6PEfrAYWsqVlZ75z6PugyhApKgmu9TrQX9xI6z-QFBcsmDAnMX68EKEt0WnGDwwruDqaVKRlsO2qGw4SIKRBUm-pKel6HJGYS17GS4DiwOTB-UsA6S8HWEdcUsLxJsgMuf6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f16a3b5be.mp4?token=NF-oLghiwvG5SZITnp5U9C8V1hLxj4SDevLfO5hAmFHcyL3q-YcDZdT604hXEvsoobxdmZPEYNelj7mrRfxoqWut2YItv4jEolGFGr9qpc7o-0lpy-ubzPw6UWFKqw40rSmqzx6TnqllxSj9PbHdvIOG4sDSbgz2PMEnfen3qbv2fk5IqCJKoplYBNhgCdevVmKIrCqwqYqcG8vNL6kelbwZ14iwmmcAw03-q3O_DwVHIEuhAy8FNOk9Mw3ukoainwOKIgrm-miLga2nVUNDmdsdZcpbmDGt4yVUewjGwh2lbTi52oKHlDU-pjEnrgGapzdZY-9oBT2jx_w0WluG9DFQQ9ZCfZSz1haPvEQDZBsQmPpgZwzy92fQbG-7HitQni6KgoeH4n_h6BNTk8PwrXIe2VQswg7MBGOWR59_yHl882TMyLWJ_f2Lp68Cpn67ZrMcIiKSnn01FeD7eln56eYuqTXMEEHzMAlask8ZpDpnJlNB4rzY65dLJPVn2Mvbh8VSWniCrDVFnLfXUnSc93otUbqhAkvZn9tv2RF6PEfrAYWsqVlZ75z6PugyhApKgmu9TrQX9xI6z-QFBcsmDAnMX68EKEt0WnGDwwruDqaVKRlsO2qGw4SIKRBUm-pKel6HJGYS17GS4DiwOTB-UsA6S8HWEdcUsLxJsgMuf6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش زندۀ خبرنگار صداوسیما از آخرین جزئیات حمله به جنوب ایران   @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/448092" target="_blank">📅 02:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448091">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8eeb1e037.mp4?token=lJbeCHwg0lMR4I4QwYhoj38NQ2-LgXRI9YdbOPmGfsMSnY979autktPWTSWZkFyCNXpEL_3N2jpSoAXeBnxD6pi5xGoSRp3Yt87ICzU2P_GmaV3oHoO4gAgSTPlytnUuSi0--O2psj7kPlcObeCAqbcmGgyj41fJXrR_p-KtTXPPno3hQBy7n6AWefF41Z-huX26XEx4aGQ6EZdqmp1rE3ZXSlndvXllJcC3Y2_jDZy6wcEgYKYXkUtMAcnD4_7sc9rpqNd3oDuYXGvs7Bz5q7JmOo6QaO3sA2YUxEHPSfMHkJ0-gFf-s1Oaue2W_dq_Nm4Sd_QgCZsEkq0JLIVDww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8eeb1e037.mp4?token=lJbeCHwg0lMR4I4QwYhoj38NQ2-LgXRI9YdbOPmGfsMSnY979autktPWTSWZkFyCNXpEL_3N2jpSoAXeBnxD6pi5xGoSRp3Yt87ICzU2P_GmaV3oHoO4gAgSTPlytnUuSi0--O2psj7kPlcObeCAqbcmGgyj41fJXrR_p-KtTXPPno3hQBy7n6AWefF41Z-huX26XEx4aGQ6EZdqmp1rE3ZXSlndvXllJcC3Y2_jDZy6wcEgYKYXkUtMAcnD4_7sc9rpqNd3oDuYXGvs7Bz5q7JmOo6QaO3sA2YUxEHPSfMHkJ0-gFf-s1Oaue2W_dq_Nm4Sd_QgCZsEkq0JLIVDww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
وزارت برق کویت از قطعی ناگهانی برق در نقاط مختلف این کشور خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/448091" target="_blank">📅 02:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448090">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
قیمت نفت پس از لغو تحریم‌های نفتی ایران به بالای ۷۵ دلار صعود کرد.   @Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/448090" target="_blank">📅 02:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448089">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QG-kSwf7fqfC3UOIbV1_WrRE7d5nVSvzSTaZCwkLYQcIcPFJcGDHAiw10Kef0ZHPUIsRDhUSkw0vhOaPcV-tkmwHvv70wY0vnASKB9hR6FVaC1DLbKSz_jgitBa-KAviJplNH5K7LtjmDNg-iVThKh0Z3KVBfPN-EYiHgn657K3ZHkZdCZ-GJIf8bVoMF0wn_-PDyIfGeABdT8iYMOMzw9e5H-0EZ2AwiJVPGWCczs4Dm1JF2t5s35xc16BEZ9_sofqVlvUFE5X4pfXgefJj8y3gmBu2IM2sfJNA9jx9H4BUo8FVvXZ9t5kYdOo4BEMyEKHKGm1j7zn9TIgIYZqs6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ستون دود بندرعباس ناشی از حملۀ دشمن به شناورهای صیادی مردم است
🔹
مدیر بنادر و دریانوردی شهید باهنر و شرق هرمزگان: دود سیاه در پشت بازار ماهی‌فروشان بندرعباس ناشی از اصابت پرتابه‌های دشمن به اسکلۀ صیادی بندرعباس و آتش گرفتن تعدادی از قایق‌های صیادی مردمی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/448089" target="_blank">📅 02:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448088">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce85279956.mp4?token=B8ymMxCA2xoGCG-HpbSLnE0ywigL0YBHoQcfEO7RId4HBXdQElWSLXukWNjmH_HzcsjSm3ZsR9lFybpSoU0Sg2uyfDhpbuyS_mxddP4Gfpc-9ozfF8K8CuvD5gM-sNRQEvKKaiJjvDnnXSj14a_uJv2kxaPmSUJOQt-d7l8mxqrdtRLFq2MJb-VaKtkGewQHgqvCWodU75K_7Jak4ECqUvE51C052SqWsCA2WkB0EF_aWCjbMJrB3bs8NeH3cREC4oU6Guy4HhC_k02feyJvW1XMx_G6kLDyeZmpYQMYWUbgiTNyCyMpqcNuH3wOzsLOBb91xExSD1NDsR83LYH83Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce85279956.mp4?token=B8ymMxCA2xoGCG-HpbSLnE0ywigL0YBHoQcfEO7RId4HBXdQElWSLXukWNjmH_HzcsjSm3ZsR9lFybpSoU0Sg2uyfDhpbuyS_mxddP4Gfpc-9ozfF8K8CuvD5gM-sNRQEvKKaiJjvDnnXSj14a_uJv2kxaPmSUJOQt-d7l8mxqrdtRLFq2MJb-VaKtkGewQHgqvCWodU75K_7Jak4ECqUvE51C052SqWsCA2WkB0EF_aWCjbMJrB3bs8NeH3cREC4oU6Guy4HhC_k02feyJvW1XMx_G6kLDyeZmpYQMYWUbgiTNyCyMpqcNuH3wOzsLOBb91xExSD1NDsR83LYH83Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای حرم مطهر امیرالمومنین(ع) ساعاتی پیش از آغاز تشییع پیکر رهبر شهید انقلاب   @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/448088" target="_blank">📅 02:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448087">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-txul2pQd3R0Rd5TkFOhWK4JKINmwFiXJpsg-PabLtAqk3qIAmYmvRoWFLxYWH1nY4fMwh7BT0Z4MOcKzTSbyHFXam9bg__IURYwTpkBGbDxWfJEO4WV4fxWM-tZTZChcIKf5ZstR3XWaZGp978_3kUDPbirXWcZclu8UcXYCUToZ1M36dNPveXbT6Xy2w0i-bZmzJ0TaCsEl7lkDogfWNc0CC0yXF969kuXUGWTZYxLAo3AUDinOiV9o2kU1rDJ8Dl2oq8R73fcsaiqLKWRG7o9BI8KV2QZGERyQphQuRqiNDD-pnZf9AYbKD3B4pRq10-ekwLqDw1fkkp43269Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
تصویر رهبر شهید بر لباس جوانان عراقی: دشمن را به زانو در می‌آوریم
.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/448087" target="_blank">📅 01:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448086">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
شنیده‌شدن صدای چند انفجار در حوالی سیریک و قشم
🔹
دقایقی پیش مردم در حوالی سیریک و قشم صدای چند انفجار شنیدند.
🔹
هنوز محل دقیق و منشأ این انفجارها مشخص نیست.
🔹
پیگیری‌های خبرنگار فارس برای مشخص شدن ابعاد دقیق این ماجرا ادامه دارد.
📝
اخبار تکمیلی متعاقبا اعلام…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/448086" target="_blank">📅 01:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448085">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgij-bTKJ3Nd45iUEFQS3gXj0fQIFcWp9ddw164l6DWQieX8b8tkMWdUgFCkOr4VbsG3NchJV3vYvemHdqFsvem_EjJ0l5npF9-YKVG1Uhzd-wB-EG1qPVi83xCj7p6Ho1gL27kDbeQuSHjODU-Up-n8Q6WTZ8gYv3RqoRA5d9KyOvw1nH5WlfKjnoN1m8huVWueZgpIQL8hj0zgpcqCwstMU8CMNLkWMY_-zeyVduISFlKeSaZbjm4rFxbiaJkt4VTP1_szbZnfN8wuTeAomK21-6M4CIN23wzXWWoOVd2EK-ZpSu3SWqT7iPCrA0mKHdL_RQTHsk1q71tRiq3pkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هدیه رهبری جهیزیه ام را کامل کرد
🔹
برای آقا نوشتم برای عاقبت‌به‌خیری من دعا کنید و شماره تماسم را نوشتم. اصلاً امیدی نداشتم این نامه دیده شود ولی...
📎
ماجرای هدیه رهبر شهید به این زوج را از
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/448085" target="_blank">📅 01:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448084">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c29967f321.mp4?token=C7rUG-51yahsDzRriyU-L02VU7pLUiWoSChoNtYW08I7Lpymvg22wMIqVn7W_86erJSDIyqemUkQWxqRlTUsqnzhyt8jIu58tKjOr9kEkNnZsKg5qUX95ERRBhG19qD2mpbeqLYXKSYmEH8lrNfxsN_YBtq0HyHY5ObOaCp4VwM5LGx9awv3XaPPr9Tie_k_iN5w05O2JqfMZYwaMN6bcw5aORguLvSf_GQgcNHX3TpDwZAu_xm4l2agOcAsf8XjSrlWunpPxJQuQZCHfAo_tuB2zBUpmyLi4Rhc3-DhXHbQy7E8oaQYYTycI39A42LZy5DEcteHfy4IjiI5XNG5zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c29967f321.mp4?token=C7rUG-51yahsDzRriyU-L02VU7pLUiWoSChoNtYW08I7Lpymvg22wMIqVn7W_86erJSDIyqemUkQWxqRlTUsqnzhyt8jIu58tKjOr9kEkNnZsKg5qUX95ERRBhG19qD2mpbeqLYXKSYmEH8lrNfxsN_YBtq0HyHY5ObOaCp4VwM5LGx9awv3XaPPr9Tie_k_iN5w05O2JqfMZYwaMN6bcw5aORguLvSf_GQgcNHX3TpDwZAu_xm4l2agOcAsf8XjSrlWunpPxJQuQZCHfAo_tuB2zBUpmyLi4Rhc3-DhXHbQy7E8oaQYYTycI39A42LZy5DEcteHfy4IjiI5XNG5zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خودروی حامل پیکر مطهر رهبر شهید انقلاب به محوطه حرم مطهر امیرالمؤمنین(ع) رسید  @Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/448084" target="_blank">📅 01:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448083">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e178f191af.mp4?token=ZKS3G_-2YncugBLDUYY8EUMyUqBTC-9qMhMBFjU3zwAq7ZjxgeEHbDhc4mfpWTmcK5nSS_K2UQ8GHY8wxePD9yjklmLz2cWHhvUq6Q2-bEErDVUXus8rgUsnkyBRnuL1dQCUmKMBbjiJJd2EyHoZldDB2nsbvRFeKd5cgOctaZ98k4WvDZKD1XQoIJbY9xDbdu8lDxFEnYiY1PzIsIi8lLkUzntpwQVfjk0c0uK4hjH4qi_pcAOW42bk8z7tUKolUlDxuEAKlLQGrOyYtsMaT-5saXCM28Uyzf8iTVTMGcOtTPPX6VnS_3s6XEbJ2v2i-2ZntNULMWuZyeCkUo13YUavWyRQ3e4DoR9AzblC4MxhcJQ7R8Ut5IcoFRzZETWlHHXIhvLcX08rLGb9c2_BRAWUVF-7DdsgPFIMPk3eqZcHSbF89xtxOiOq1ho7VOlEaJvUgCv96jrHj4Hyp_SXLabtSbnagxewAOv8LSgkTyJHVJ3zjK_JEUK79gMSFGh33My3XJTa06QUufayho0Nr7t2ytsmLOcPqrNblvPLBbbW2YaFDyClFjCSFtvive4npTLFQh-gaueUDjqmLZGhfJqEDVFomsC_FdP7Xtbj_syZRbpijAX9Y0iX9iSFjm72FVbJ7TecjhRuEfsxDUgAkbuaagmCtOKMaw0KgEJTNBs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e178f191af.mp4?token=ZKS3G_-2YncugBLDUYY8EUMyUqBTC-9qMhMBFjU3zwAq7ZjxgeEHbDhc4mfpWTmcK5nSS_K2UQ8GHY8wxePD9yjklmLz2cWHhvUq6Q2-bEErDVUXus8rgUsnkyBRnuL1dQCUmKMBbjiJJd2EyHoZldDB2nsbvRFeKd5cgOctaZ98k4WvDZKD1XQoIJbY9xDbdu8lDxFEnYiY1PzIsIi8lLkUzntpwQVfjk0c0uK4hjH4qi_pcAOW42bk8z7tUKolUlDxuEAKlLQGrOyYtsMaT-5saXCM28Uyzf8iTVTMGcOtTPPX6VnS_3s6XEbJ2v2i-2ZntNULMWuZyeCkUo13YUavWyRQ3e4DoR9AzblC4MxhcJQ7R8Ut5IcoFRzZETWlHHXIhvLcX08rLGb9c2_BRAWUVF-7DdsgPFIMPk3eqZcHSbF89xtxOiOq1ho7VOlEaJvUgCv96jrHj4Hyp_SXLabtSbnagxewAOv8LSgkTyJHVJ3zjK_JEUK79gMSFGh33My3XJTa06QUufayho0Nr7t2ytsmLOcPqrNblvPLBbbW2YaFDyClFjCSFtvive4npTLFQh-gaueUDjqmLZGhfJqEDVFomsC_FdP7Xtbj_syZRbpijAX9Y0iX9iSFjm72FVbJ7TecjhRuEfsxDUgAkbuaagmCtOKMaw0KgEJTNBs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش زندۀ خبرنگار صداوسیما از آخرین جزئیات حمله به جنوب ایران
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/448083" target="_blank">📅 01:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448082">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57392b21c6.mp4?token=TaHzTKdqsSx88kR4aS6dcL7P0NzdiokNowlpCe2mr0Uzi6_xwde_VdmRfS4UrvViWfAdcxSup8uXuK1p_p4xp0l5Fg5DAzg5WfCGUHYpi98rQxvCCI4cdw-mJxZI9TOCCixq_TO2d0yEKXjCXjgGXlxUywhJZBek-XfpaiZi5oJI-iKWLhyEi6l3BUn4_PczuIXLMb9bDuw0cp44a69slltCYExxou_DsTmjmUex-qNg4cIA7M1KxkThbehUJVyLNEfWzobRbulAqPfx7Epb6yZZ452mT-MsyJj6qMyY36D15s9_q4Xgz0bfEOoT_-dQwkYVB4x7TMbcq57NuY1DzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57392b21c6.mp4?token=TaHzTKdqsSx88kR4aS6dcL7P0NzdiokNowlpCe2mr0Uzi6_xwde_VdmRfS4UrvViWfAdcxSup8uXuK1p_p4xp0l5Fg5DAzg5WfCGUHYpi98rQxvCCI4cdw-mJxZI9TOCCixq_TO2d0yEKXjCXjgGXlxUywhJZBek-XfpaiZi5oJI-iKWLhyEi6l3BUn4_PczuIXLMb9bDuw0cp44a69slltCYExxou_DsTmjmUex-qNg4cIA7M1KxkThbehUJVyLNEfWzobRbulAqPfx7Epb6yZZ452mT-MsyJj6qMyY36D15s9_q4Xgz0bfEOoT_-dQwkYVB4x7TMbcq57NuY1DzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقی‌ها در داخل حرم امام علی(ع) در انتظار پیکر رهبر شهید هستند  @Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/448082" target="_blank">📅 01:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448080">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1f3f14c10.mp4?token=RRf33ESjbRB8W5vzjJTGjhMMZNdpBkPJNt_2dk_7XdGempEAavAFmiVDlwnXnk5CrG8DuVX18Uu6JTGAir251Yc5KJ_12CWzwMa0dEneI8PQqesb9MC3yJiAOII63nZDAC2vUWp7UvLbbYADnZAfBdlMrsFYk0NBsLFqCYivARcAkLwXg0hcBw6vq5IuSHW9F-8riTD1Z7VR6yImiI-GDPyHxpriROsr9KX7S2r-9tcOjkjyu_9msQ1aQfV21bpYst_HLR1YpgpBNLDjqkna1eU-TQi065iUlCpYJG3HXxnX7V95F2NRJMZVJI6wbK8pNia69H7tY8KhUAPFKsPx3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1f3f14c10.mp4?token=RRf33ESjbRB8W5vzjJTGjhMMZNdpBkPJNt_2dk_7XdGempEAavAFmiVDlwnXnk5CrG8DuVX18Uu6JTGAir251Yc5KJ_12CWzwMa0dEneI8PQqesb9MC3yJiAOII63nZDAC2vUWp7UvLbbYADnZAfBdlMrsFYk0NBsLFqCYivARcAkLwXg0hcBw6vq5IuSHW9F-8riTD1Z7VR6yImiI-GDPyHxpriROsr9KX7S2r-9tcOjkjyu_9msQ1aQfV21bpYst_HLR1YpgpBNLDjqkna1eU-TQi065iUlCpYJG3HXxnX7V95F2NRJMZVJI6wbK8pNia69H7tY8KhUAPFKsPx3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور پزشکیان و عراقچی در حرم امام علی(ع)
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/448080" target="_blank">📅 01:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448079">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🖼
آمریکا نقض دوباره آتش‌بس با حمله به ایران را تایید کرد
🔹
سازمان تروریستی سنتکام اعلام کرد که در واکنش به حملات ادعایی ایران به کشتی‌های تجاری در تنگ هرمز، حملات تجاوزکارانه‌ای را به چند نقطه در جنوب ایران انجام داده است. @Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/448079" target="_blank">📅 01:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448078">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2ba5b25c.mp4?token=oJ4V10S1OQgGQDA9nUOOpZ1LF2Ptuw5oWfigHiDwrzluEx9tH1yvjx4nEXakYHywn1M6hQ2jrt-wpX29VJattFloJ1NOWLzS0UrphWHDvoRpu9en6Ae4JCpNTZdIsJglkzfCUKVgO7LsbLBUNzq0SzAavI090aAZyQ79QnFHA-KJd65AjzBp8M97ca1vIIA19xCtXlkH32WnFnHB-bHtBdcHnaI1NrlGM_jiadQ2o4MtgNza1HS3gJ22RdyO-dl7pyPMfRET_5oTAqcrXKnq8HBARyZ7Q74HQdaAOTqM5BF9DnO9H2q0vwLcL-gr6rGp4NKxNKSPac2RDWwt_TMbnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2ba5b25c.mp4?token=oJ4V10S1OQgGQDA9nUOOpZ1LF2Ptuw5oWfigHiDwrzluEx9tH1yvjx4nEXakYHywn1M6hQ2jrt-wpX29VJattFloJ1NOWLzS0UrphWHDvoRpu9en6Ae4JCpNTZdIsJglkzfCUKVgO7LsbLBUNzq0SzAavI090aAZyQ79QnFHA-KJd65AjzBp8M97ca1vIIA19xCtXlkH32WnFnHB-bHtBdcHnaI1NrlGM_jiadQ2o4MtgNza1HS3gJ22RdyO-dl7pyPMfRET_5oTAqcrXKnq8HBARyZ7Q74HQdaAOTqM5BF9DnO9H2q0vwLcL-gr6rGp4NKxNKSPac2RDWwt_TMbnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یزلۀ جوانان عراقی در سوگ رهبر شهید انقلاب در بین‌الحرمین
@Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/448078" target="_blank">📅 01:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448077">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e515634f6f.mp4?token=PbLlkH5xYLjYTorbj4vbve4Dy6Ecn1gzhHxriCwbGi4SGYNEquhEcY48pUFn8GSQRtgD0Svnd6Z8eyH0dYjTEVDx9RFvsA1rY6hS815IsFUBcM_LbYs0-U6kFiTArxlewYRO-4qt4exlfazcykkI165rQ0ghQ-plLS2ztA14zOu6xMXkqSawL6_78SCvL58lgXUmaNGh48T4KdAstJhJGXSYINdkR1dRFc-LQhoc-jdZacqXlhGmW5l0Awf6kGJIva2qk9TIWGWUlrFsckrGezSPz3dM9Jm1hHx_ulZCAb5DQ61A_Pa4HLSpTjOcZZYYKpl33fSTYIDs8MN2ROkDDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e515634f6f.mp4?token=PbLlkH5xYLjYTorbj4vbve4Dy6Ecn1gzhHxriCwbGi4SGYNEquhEcY48pUFn8GSQRtgD0Svnd6Z8eyH0dYjTEVDx9RFvsA1rY6hS815IsFUBcM_LbYs0-U6kFiTArxlewYRO-4qt4exlfazcykkI165rQ0ghQ-plLS2ztA14zOu6xMXkqSawL6_78SCvL58lgXUmaNGh48T4KdAstJhJGXSYINdkR1dRFc-LQhoc-jdZacqXlhGmW5l0Awf6kGJIva2qk9TIWGWUlrFsckrGezSPz3dM9Jm1hHx_ulZCAb5DQ61A_Pa4HLSpTjOcZZYYKpl33fSTYIDs8MN2ROkDDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای بین الحرمین، پیش از آغاز مراسم تشییع پیکر رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/448077" target="_blank">📅 01:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448076">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‌ ‌
🔴
معاون بین‌الملل وزارت خارجه: حملهٔ آمریکا به ایران مصداق نقض جدی بندهای ۱ و ۲ یادداشت تفاهم اسلام‌آباد است
🔹
آمریکا در ۳ هفته گذشته نیز به‌واسطهٔ اقدامات رژیم صهیونیستی در لبنان و اظهارات تهدیدآمیز علیه ایران، بارها مرتکب نقض بندهای ۱ و ۲ یادداشت تفاهم…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/448076" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448075">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🖼
آمریکا نقض دوباره آتش‌بس با حمله به ایران را تایید کرد
🔹
سازمان تروریستی سنتکام اعلام کرد که در واکنش به حملات ادعایی ایران به کشتی‌های تجاری در تنگ هرمز، حملات تجاوزکارانه‌ای را به چند نقطه در جنوب ایران انجام داده است. @Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/448075" target="_blank">📅 01:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448074">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_m8YqrK2oO6usbbbl_53tqQxc83pg0BCzCmhxVQYTiezGBz0jMe4XruxqXD2hIN_bZuklwx8WekqKFcT_-s0tsxB8vlfOSrdE0ZBT2P4ObjZ_Ds1d6TmN4ONEkDuSdLyIvSaZKOCXh1Ib049vTtFlBwiQQv01wIxR7dIR4nGbXFTuUrJfK_Gh-1pb2rSa8bhKA48Uw35GKNgWSJ3cpl0heg6ZfudFV5nBRiHqmmYwkSPFA2k_FlDJjcV6kzl0V6_vtKG2NEkvL131toIexvOX3F_RQ40SezBisju0nts1oh4VBoM9CX2LhQqNTj1trdZTEuv0NqzTC9wQDsHEmCzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
بدعهدی دوباره آمریکا؛ مجوز لغو موقت تحریم‌های نفتی لغو شد
🔹
دولت آمریکا به مجوز موقتی که امکان انجام برخی معاملات نفت و فرآورده‌های پتروشیمی ایران را فراهم کرده بود، پایان داد. @Farsna - Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/448074" target="_blank">📅 00:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448073">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGTmWDbfW1VB38KPvslPdIo3OU6MPtmgOHc8iFqfahZqHv2xrI9eUuSfBpqld58aeV-412I64PxE9LwBMtEVJPgfjU-c6kOPDKbjrGyGVqvJwlcjikkBllw0p5tnKVgAoPKaxLbdyZesifF6z2rkeItcVuGDJL7VQwFJqAN78TlBSk3p9BjmI6-u3Om2pJ8_vHvBlqwX5LogpQcqmpvslWODit5TM1nXHxx9D58K-nsFi8a3pP1FG2fsyjAtwQD4E3M2LwBBx8h5GpDmHGVZzImxZUT4oI1ky_NFyaSSV3ArUdS3JuH62MouY_oXvf6O1eb0PrWzzdO6wtItntejJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
آمریکا نقض دوباره آتش‌بس با حمله به ایران را تایید کرد
🔹
سازمان تروریستی سنتکام اعلام کرد که در واکنش به حملات ادعایی ایران به کشتی‌های تجاری در تنگ هرمز، حملات تجاوزکارانه‌ای را به چند نقطه در جنوب ایران انجام داده است.
@Farsna</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/448073" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448071">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
شنیده‌شدن صدای چند انفجار در حوالی سیریک و قشم
🔹
دقایقی پیش مردم در حوالی سیریک و قشم صدای چند انفجار شنیدند.
🔹
هنوز محل دقیق و منشأ این انفجارها مشخص نیست.
🔹
پیگیری‌های خبرنگار فارس برای مشخص شدن ابعاد دقیق این ماجرا ادامه دارد.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/448071" target="_blank">📅 00:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448070">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">🎥
مردم تهران در آخرین دیدار به رهبر شهید چه گفتند
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/448070" target="_blank">📅 00:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448069">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54805647e3.mp4?token=ZTpECbQw4I0hFdKih1qjjvM8QDtn4UbMJqLEYsYOwsT6tkn7jOw5jPaqKe6X-zX4Wk0FpXpXR9xh0gVbeV1pXyJpuk3g16MFl6WyJh45W-Ki4EJFKPHMZ2MKadwmWhq_k3Q9qno91HgYgDxvuxw2IlZ7_S7zVX7peDD6EFKvmpom3GPr92VbOvyhLqDh8NtNR_KGsEbq6XZYs46OuQH5VnPOSL7CBA--1DWucdelGp99UqdS7uMU_xt9UHgkhRDTznUauM980oBX95aIAHNovx_yWxkZuNwpCLaGbe6YFQOoXx45HcS6_bGst21eJSzHpgnyJMBsGMwS2avOL-Xalg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54805647e3.mp4?token=ZTpECbQw4I0hFdKih1qjjvM8QDtn4UbMJqLEYsYOwsT6tkn7jOw5jPaqKe6X-zX4Wk0FpXpXR9xh0gVbeV1pXyJpuk3g16MFl6WyJh45W-Ki4EJFKPHMZ2MKadwmWhq_k3Q9qno91HgYgDxvuxw2IlZ7_S7zVX7peDD6EFKvmpom3GPr92VbOvyhLqDh8NtNR_KGsEbq6XZYs46OuQH5VnPOSL7CBA--1DWucdelGp99UqdS7uMU_xt9UHgkhRDTznUauM980oBX95aIAHNovx_yWxkZuNwpCLaGbe6YFQOoXx45HcS6_bGst21eJSzHpgnyJMBsGMwS2avOL-Xalg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نیروهای کتائب حزب‌الله، برای تأمین امنیت مسیر تشییع پیکر امام و رهبر شهید، در مسیر بین استان‌های نجف و کربلا مستقر شدند.
@Farsna</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/448069" target="_blank">📅 00:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448068">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
سقوط مشکوک هواپیمای پاکستانی در دریای عمان
🔹
ادارۀ فرودگاه‌های پاکستان از سقوط یک هواپیمای باری با ۵ سرنشین در دریای عمان خبر داد.
🔹
طبق این گزارش، این هواپیما ساعت ۲۱:۱۸ به وقت اقیانوس آرام از شارجه به کراچی در حرکت بود، که مشکل سیستم ناوبری را گزارش کرد و بلافاصله توسط مرکز کنترل ترافیک هوایی کراچی راهنمایی شد.
🔹
در ساعت ۲۱:۲۱، در رادار مشاهده شد که هواپیما به‌سرعت در حال کاهش ارتفاع و تغییر جهت سریع است، و پس از مدتی تقریباً در ۱۵۵ مایلی غرب کراچی در دریای عمان، ارتباط و تماس رادار قطع شد.
🔹
این حادثه در حالی رخ داده است که فعالیت‌های نظامی نیروهای ارتش آمریکا در این منطقه طی ساعات اخیر به‌شدت افزایش یافته است.
🔹
تعدادی از رسانه‌ها احتمال هدف قرارگرفتن این هواپیما توسط دستگاه نظامی ایالات متحده را مطرح کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/448068" target="_blank">📅 00:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448067">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bab243fe1a.mp4?token=Mfb85bIj_w0XsY9ANjbTWzsGGokwbn_w3o4ACI8XXf1XYKVXd3LFqnonvb2PITtJDulJ03g6KnMbiONMtGbYqJlZEB9mK71K0IavH63gX6pBriBOkKsEOGyXrfK2Ui8pMb8ASymoB1-1TStcGlTCJZtRVncnuxiSwZmWDIaFKh3Zqj0F1F1NM8x6g1jHNs_utfqvLgaq74thmis0hEu7G9GBsvWNAWrAVQpm5zy1nf-_sOAn626C6mBmNJ1-HCPWElZ1DhSsATqXbf_a4d5lnV4OTCuw1As4DctEZjZNOOCzMO_VDoeO_-rfA8VVUKOxOP6HCq96LjiBG_L3MCdsXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bab243fe1a.mp4?token=Mfb85bIj_w0XsY9ANjbTWzsGGokwbn_w3o4ACI8XXf1XYKVXd3LFqnonvb2PITtJDulJ03g6KnMbiONMtGbYqJlZEB9mK71K0IavH63gX6pBriBOkKsEOGyXrfK2Ui8pMb8ASymoB1-1TStcGlTCJZtRVncnuxiSwZmWDIaFKh3Zqj0F1F1NM8x6g1jHNs_utfqvLgaq74thmis0hEu7G9GBsvWNAWrAVQpm5zy1nf-_sOAn626C6mBmNJ1-HCPWElZ1DhSsATqXbf_a4d5lnV4OTCuw1As4DctEZjZNOOCzMO_VDoeO_-rfA8VVUKOxOP6HCq96LjiBG_L3MCdsXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصویر حضرت آیت‌الله سید مجتبی خامنه‌ای در دست عزاداران رهبر شهید انقلاب در نجف   @Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/448067" target="_blank">📅 00:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448066">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDq_LnOLKrKlaGME5F4dblg_Ze6gqmgLBEgtenW-m0EQrToGezsQZHgBsKqEkSl5EUR3-75OSfM4YDP7yfwqEKEVBr4jot3YRBZqZTC-LnjVUF702_3ooyEyiS_onA0JC8qA_Y2p1LMchdqVYSD5Jmx_z4hmty2PYz9Bg-r_Sxu9Vag4371FyxUYF1h9A8Kwek30BWa7Q0zQ4tsHVkxNT68x4Ea6As7uxxbpYo9JQuN0MTfc2l09uhCG8QuYN-2sx58YtqM_BmgnKos9fA3qhHB1nO_D-n0bNz44E32DKaYcwF_kSr8p22kOw6imGAO4T8YOe5M41I_-FAiwp60NNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حواسِ آقا به این خبرنگار بود
🔹
سرم پایین بود. داشتم می‌نوشتم. توی ظل آفتاب نشسته بودم رو به رویش تا آن ماهِ تمام را بهتر و دقیق‌تر تماشا کنم. اما او متوجه رد خورشید به صورتم شده بود و با اشاره‌ای فرمود: «کی این آقا رو تو آفتاب نشونده؟ برو زیر سایه.»
🔹
آن روز، آقا نگران این بود که آفتاب روی صورت من خبرنگار، من مهمان جوان نتابد؛ و من امروز اینجا هستم تا اجازه ندهم آفتاب، مهمانان آقا را در آخرین دیدار آزار دهد...
📎
روایت عاشقی این خبرنگار را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/448066" target="_blank">📅 00:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448065">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ae004bfed.mp4?token=nStFpgo9Ufiuo3hHpZ8esqGjSUI3wyhiOiiH9BpJTJEnp4yi8uUILBrPaVVlrcpQHO-OS8GU7j1dzuYkmJFWVU5xEd0vXozzpyS6ecdcMWzvZa5EJl69wNKD-wX8E9sbJWUlbAnQC47Jsg8wQyr8cgfV2-zhqFvkWUonjd_pAMc97QvY9eoEZpv3oezdclp6smVdfp6qjUaYbHt5wVMwlS5VbV5M05F2rUul4tIoBFKf0RktwC9IEB_-6MFrGZVxUYLmJPAItowEVs2Ma8hMuEv1ISAp4kuv9RNt22FF63u6EJFqhOYP8eX0KmsiMgR-jNK6fJ6UfHoTa8GV1BAFLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ae004bfed.mp4?token=nStFpgo9Ufiuo3hHpZ8esqGjSUI3wyhiOiiH9BpJTJEnp4yi8uUILBrPaVVlrcpQHO-OS8GU7j1dzuYkmJFWVU5xEd0vXozzpyS6ecdcMWzvZa5EJl69wNKD-wX8E9sbJWUlbAnQC47Jsg8wQyr8cgfV2-zhqFvkWUonjd_pAMc97QvY9eoEZpv3oezdclp6smVdfp6qjUaYbHt5wVMwlS5VbV5M05F2rUul4tIoBFKf0RktwC9IEB_-6MFrGZVxUYLmJPAItowEVs2Ma8hMuEv1ISAp4kuv9RNt22FF63u6EJFqhOYP8eX0KmsiMgR-jNK6fJ6UfHoTa8GV1BAFLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کلا کلا آمریکا، نعم نعم بالایران
🔹
نه به آمریکا و دفاع از ایران و جبهۀ مقاومت در شعارهای عراقی‌ها در وداع با رهبر شهید.
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/448065" target="_blank">📅 00:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448064">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Amd2t0lrG3QxU5PRbtGlqAgufQC4BATZtLi1lUuy1FQyll2WcBsBfanRNSvWnnCk1GSCcZ0h5h7MLVT60t17lHigmFkf_phZQdWhM_lFUfSHJVdEXG5bedaU0tELUz3N6_gBUQ2jx4g1psyrRglNcUoH09UOGRFo6opUuQA6MoJ5U2F24NpX3fLeCsO2NoBQeDVQRPdLfFSVvA3ls6Kq-OYwv8fT5J33p__kl4ctD607qOVqu_V4M2ssieB2i9MSNMgl-gBwG25zfFEJ-sn61I7xeSYTADvxFbDkgKSr1U_eposj1wkemEkOaRQhX1bZvpuwZt3606oieHBKBSOa4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
| چهار‌شنبه ۱۷ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/448064" target="_blank">📅 00:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448063">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e1fa65d60.mp4?token=F9oELCZKBG3PQCnO5BBXieEAPWRhVsEB--d0zRTCQ1d4WL3o_qI7UdVUqXkkWYSMax6-NPqj7yBvQOhSyqm467bGh-pXLjAiomdPq6Q-vEV3uZNKQ15KUhkdhVjHoMgVNXuJCpA32c2wQkr27gClcv_lkY3L7O5DUkCVU6_uTDqujOImJ-LhC0j0evrN4mR3Z_PSJXOm1OTwbyUVHapSDqONEHN93NfRVm9Phl0-jTd4FEH69wpAnt3Nm7vKU1pd5orwIbQaMdkVRmUIFrQlACGO_AcFKcJD0dsTN-zSyjpcUVyxKrbo1CrdO7PjHdYgaJWIVlmtE1rysFryoe16FFFRDLON7hMP8xsaIKXYDZK9ZiVRdWHhSPo33Lbz964C1Hpq1YKVFuX7epfzzejjqDf5PZlOY8mLSek9aSsqbrUejotGQTiOrkCCUoYvO_lLIK-AxuVBPdyUi8zKVK7AcKYFSKKT8RKqup-uS0vmnHppGIQdxSQ84Hj4PDxA7hlAkHyoRbdVsUb2-2julNuSC3k19RyoKTEkeYRKxDoo7HqP8GMpi_qg88nqzwfgoppg7Wnu4MZNYIbd1ZoimKc0dW79r_2tVidvdyra4fDkF7P9PhnGje-N7WrLP3wWX8DvgxKjUwmcrvpEI7o4Jc6yQ55XLi1ehpDfBcqIFUfNafc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e1fa65d60.mp4?token=F9oELCZKBG3PQCnO5BBXieEAPWRhVsEB--d0zRTCQ1d4WL3o_qI7UdVUqXkkWYSMax6-NPqj7yBvQOhSyqm467bGh-pXLjAiomdPq6Q-vEV3uZNKQ15KUhkdhVjHoMgVNXuJCpA32c2wQkr27gClcv_lkY3L7O5DUkCVU6_uTDqujOImJ-LhC0j0evrN4mR3Z_PSJXOm1OTwbyUVHapSDqONEHN93NfRVm9Phl0-jTd4FEH69wpAnt3Nm7vKU1pd5orwIbQaMdkVRmUIFrQlACGO_AcFKcJD0dsTN-zSyjpcUVyxKrbo1CrdO7PjHdYgaJWIVlmtE1rysFryoe16FFFRDLON7hMP8xsaIKXYDZK9ZiVRdWHhSPo33Lbz964C1Hpq1YKVFuX7epfzzejjqDf5PZlOY8mLSek9aSsqbrUejotGQTiOrkCCUoYvO_lLIK-AxuVBPdyUi8zKVK7AcKYFSKKT8RKqup-uS0vmnHppGIQdxSQ84Hj4PDxA7hlAkHyoRbdVsUb2-2julNuSC3k19RyoKTEkeYRKxDoo7HqP8GMpi_qg88nqzwfgoppg7Wnu4MZNYIbd1ZoimKc0dW79r_2tVidvdyra4fDkF7P9PhnGje-N7WrLP3wWX8DvgxKjUwmcrvpEI7o4Jc6yQ55XLi1ehpDfBcqIFUfNafc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کودکان پاکستانی با عکس رهبر شهید در نجف سرود می‌خوانند
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/448063" target="_blank">📅 23:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448062">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84b32253df.mp4?token=Kr7asDO5w8PMSubKZvSkOZ2n10gnrHURMvTqINax0VOe-85tdIG7lwZYN81jDS9XD3Z37ObZlx0BqcJUYR6oJWfmrDnbri3qQcECyos0g5DDn26IEKfiDxlhZlfL4G--wLiN0BqhmIrKuKAKQJ28PDsClusFBtk8egfK8R0KaGp-Fm9n9fyEiKAlzGRi1D5GlGRPTlwX8LPWRK--P6VROj_yy40Ws-4Zivbbc1y6Ugmcuu1ZvNPkoT1HsTHdWt9ZVL6LAure8KnmnWz-iIon0DN2XqYwLkA3F198QkiZMMoEF0G-9K8fPDVRUSWxPG2jNCFlNizTjgTijsfTy32_fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84b32253df.mp4?token=Kr7asDO5w8PMSubKZvSkOZ2n10gnrHURMvTqINax0VOe-85tdIG7lwZYN81jDS9XD3Z37ObZlx0BqcJUYR6oJWfmrDnbri3qQcECyos0g5DDn26IEKfiDxlhZlfL4G--wLiN0BqhmIrKuKAKQJ28PDsClusFBtk8egfK8R0KaGp-Fm9n9fyEiKAlzGRi1D5GlGRPTlwX8LPWRK--P6VROj_yy40Ws-4Zivbbc1y6Ugmcuu1ZvNPkoT1HsTHdWt9ZVL6LAure8KnmnWz-iIon0DN2XqYwLkA3F198QkiZMMoEF0G-9K8fPDVRUSWxPG2jNCFlNizTjgTijsfTy32_fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداران عراقی در کنار حرم امیرالمؤمنین(ع) در انتظار پیکر رهبر شهید انقلاب هستند  @Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/448062" target="_blank">📅 23:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448061">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18291d12b6.mp4?token=pXwbaxMpqLEy9fzzUgIHwl7tk2g7d0br0LvJSGvyooOCsunRTwhAyC7VUU4vwj99zKsUoEI1BoR3eCu_mV73ZrnwI2pBw7HQCgYSZK1viZwjQuW3BZt1fm4KhqwzF3W2F6hqQc4KVcqGL0eASjqJPuM2nuMysPgYO54eZKi92pDzUQluQP1Azuh_p3uCr8MqnJ9RcdQYKkqGMOn6_KuP1_w1zV5hIwMniEQPJmX-OMeB5kERH1fgyWsvvCgQXzMpy7_Twwnyq-1BuMvYkqN-Dt71j79HNp0Lbi1-UZjPycXqRVgDsByTorZFHKOkBak_oJUkLBRTY5Jv2IU4nc5mHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18291d12b6.mp4?token=pXwbaxMpqLEy9fzzUgIHwl7tk2g7d0br0LvJSGvyooOCsunRTwhAyC7VUU4vwj99zKsUoEI1BoR3eCu_mV73ZrnwI2pBw7HQCgYSZK1viZwjQuW3BZt1fm4KhqwzF3W2F6hqQc4KVcqGL0eASjqJPuM2nuMysPgYO54eZKi92pDzUQluQP1Azuh_p3uCr8MqnJ9RcdQYKkqGMOn6_KuP1_w1zV5hIwMniEQPJmX-OMeB5kERH1fgyWsvvCgQXzMpy7_Twwnyq-1BuMvYkqN-Dt71j79HNp0Lbi1-UZjPycXqRVgDsByTorZFHKOkBak_oJUkLBRTY5Jv2IU4nc5mHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از کجا اومدید؟!
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/448061" target="_blank">📅 23:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448060">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e263d4003e.mp4?token=ENqGYRN6mD0kuiXq8WVkwJloB0NO7RxE1suad5To9yWemKF_3C34lnkYv3-CY822rjXmDaucP8d1BXxF9EodzkNbj_c31zpcOLYvvQe3bdQ8-MWMSOw9Mt7OWHmgaBaWlywPH1EPnCS56TZ79jmtPCFJJpQ3E4xMgMbfgo8nKcspvPPd-jpiJPjzTTgOKbGwkGTHvbBI96rvbNx0vtJPi7xHZ43lEXGtpzNnFULHCAbJKiT8UDystrikR-5J9ZKaZnFey23BJw1xU_6LateR9Bkxm9nWPgdJEXeQxBgLCJnWNYzMH1H4KyktqZL6fzPvJ6col9n6g5uembnpZIMTYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e263d4003e.mp4?token=ENqGYRN6mD0kuiXq8WVkwJloB0NO7RxE1suad5To9yWemKF_3C34lnkYv3-CY822rjXmDaucP8d1BXxF9EodzkNbj_c31zpcOLYvvQe3bdQ8-MWMSOw9Mt7OWHmgaBaWlywPH1EPnCS56TZ79jmtPCFJJpQ3E4xMgMbfgo8nKcspvPPd-jpiJPjzTTgOKbGwkGTHvbBI96rvbNx0vtJPi7xHZ43lEXGtpzNnFULHCAbJKiT8UDystrikR-5J9ZKaZnFey23BJw1xU_6LateR9Bkxm9nWPgdJEXeQxBgLCJnWNYzMH1H4KyktqZL6fzPvJ6col9n6g5uembnpZIMTYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر رضایی: هم انتقام مصداقی و هم انتقام از اشخاص باید صورت بگیرد
🔹
انتقام مصداقی به معنای خروج آمریکا از منطقه حتما باید صورت بپذیرد تا مسیر پیشرفت ما باز باشد.
🔹
اما به غیر از آن، ۲ قاتل رهبر شهید نباید از انتقام در بروند. @Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/448060" target="_blank">📅 23:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448059">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eseBM-tjCc1iGFSNML7wf2hL1UlwWP6ax-hOztUJ9qOrVZls12CSTYouAVs9vtthlE3r1_-cct8UCs_Pu9jBjTm8nV5lRWRcrvliw6sSj8Pw_U_x7won7AgVUVE7er52ZK3AztipPIIpiTZLtl7uWrAwBJGqbgVCK9g2UVk9oSas4lgfM89U_shvckdpMbH9Pb15RhcLoizDc4iyiDUYiaPzZ-1BszgjiRCfKW491ILtJGSMJFTcOGeUfRcKPDj5VoDqsEGuHdEmUVrMVDQqpZMxn-2AHSOqmUxR88asVChH6Hdy3L5rlrpkzSsDh50J88QdpJ191lXO76r8n_fp8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
حضور مسیحیان عراق برای استقبال از پیکر پاک رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/448059" target="_blank">📅 23:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448058">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b795f6a88c.mp4?token=S5IOnDjgbwg_Mh2I5UzB1arLmtso1fYe8RHC1TqQAtZ26Et-edQBdTcphlI3sfV58VyBwFMNLGyPuR3Fa2yEv9BXmmGeBrJoUKdxRDG110w3yF9X9-oafJEflxK8IYo2th2BAO6QOTlNu3zXer9ylKD5-idbGkjeCgGGNrahgiDY_eSbRq2_pDV_uIFW91pnmbBMl2a22RUvkIRFnbeG1BVmoRKHrdjKvg3iB6H9iEN0Bld2Jqwf7R3N1KsJpCqH23Ve9BNgj0KVOODJD5UfLsffilTEohLbR6eJJrvU-b01katU7VPTJFxKFVeC7sfAzDkiHQtYbw9aroWJBr6Muw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b795f6a88c.mp4?token=S5IOnDjgbwg_Mh2I5UzB1arLmtso1fYe8RHC1TqQAtZ26Et-edQBdTcphlI3sfV58VyBwFMNLGyPuR3Fa2yEv9BXmmGeBrJoUKdxRDG110w3yF9X9-oafJEflxK8IYo2th2BAO6QOTlNu3zXer9ylKD5-idbGkjeCgGGNrahgiDY_eSbRq2_pDV_uIFW91pnmbBMl2a22RUvkIRFnbeG1BVmoRKHrdjKvg3iB6H9iEN0Bld2Jqwf7R3N1KsJpCqH23Ve9BNgj0KVOODJD5UfLsffilTEohLbR6eJJrvU-b01katU7VPTJFxKFVeC7sfAzDkiHQtYbw9aroWJBr6Muw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زاوینی‌های کلات به عشق رهبر به خیابان آمدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/448058" target="_blank">📅 23:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448057">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5767505733.mp4?token=d1gK7_ZbOzEDhsmuWTcM7-k19bZZe4jp8J69_70PKGbqDYjNusosJkU-wddU2QA8jIvh88l78IqwKH0X7GpasyvpwidSnsjDz71wuvmRP-om24xuY606TvhH83j52x0fhftDpkiBqRPn4JUVn9d_me-eIr0B9juZYlQkC5qc4vFAVjHFw2NrQKdr85gMhlvdw1-7Kb2r7gc6OC00hS-1e_olQAraZgNLBM031PbBS2J0RHmbknivf-Ag9HNlYX7GKNSpms9PdRRO2KwkCZTtFRrPxrP8FKoT9p9LOd7i_rtXtt1ppPRBs4ZTeO5mEOHh9_wgquuILYB0IxLem9Uw8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5767505733.mp4?token=d1gK7_ZbOzEDhsmuWTcM7-k19bZZe4jp8J69_70PKGbqDYjNusosJkU-wddU2QA8jIvh88l78IqwKH0X7GpasyvpwidSnsjDz71wuvmRP-om24xuY606TvhH83j52x0fhftDpkiBqRPn4JUVn9d_me-eIr0B9juZYlQkC5qc4vFAVjHFw2NrQKdr85gMhlvdw1-7Kb2r7gc6OC00hS-1e_olQAraZgNLBM031PbBS2J0RHmbknivf-Ag9HNlYX7GKNSpms9PdRRO2KwkCZTtFRrPxrP8FKoT9p9LOd7i_rtXtt1ppPRBs4ZTeO5mEOHh9_wgquuILYB0IxLem9Uw8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقی‌ها با نوای عزا از رهبر شهید انقلاب استقبال کردند  @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/448057" target="_blank">📅 23:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448055">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/940ff2ee8b.mp4?token=NWRVFgrU4cUmEu-B-NtcEFrJ-Vk4zV3c9V21y3rrTR1YXfyfd7dSGJVuyX5yacEO-2OEaKR0sPRJaeDUu-GU1USxFE4nr8bDR8coEQ7nu2S9lh43CRx6XPBGLIS8lyAz__uzJ2CB8KVcVeNAdd9XgHTjeI-HDdSl3Ff9c_iet7bPwqGMSlEZtgl1O_myrg6C2L-r3Yu_Xo1ubz6c_hU4yawX0CyDKBDnJvxPNQLTNPIOxaR2m8bpd0H7-PLqEmceu3jvTdlx-2DfsFBwdpUs0hfSX3z_FF9lr6kiR2G6dee-GMtd2sJRavPAI5ajBX8d0xk0LO15n5dNxbkdeNjltw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/940ff2ee8b.mp4?token=NWRVFgrU4cUmEu-B-NtcEFrJ-Vk4zV3c9V21y3rrTR1YXfyfd7dSGJVuyX5yacEO-2OEaKR0sPRJaeDUu-GU1USxFE4nr8bDR8coEQ7nu2S9lh43CRx6XPBGLIS8lyAz__uzJ2CB8KVcVeNAdd9XgHTjeI-HDdSl3Ff9c_iet7bPwqGMSlEZtgl1O_myrg6C2L-r3Yu_Xo1ubz6c_hU4yawX0CyDKBDnJvxPNQLTNPIOxaR2m8bpd0H7-PLqEmceu3jvTdlx-2DfsFBwdpUs0hfSX3z_FF9lr6kiR2G6dee-GMtd2sJRavPAI5ajBX8d0xk0LO15n5dNxbkdeNjltw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر رضایی: دوستانی که مخالف مذاکره هستند صبر کنند؛ خود آمریکایی‌ها این مذاکرات را ازبین می‌برند  @Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/448055" target="_blank">📅 23:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448049">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H80R8cwgLcnvWvVt10FpgQaXtT5XVaKegkzHfTPP5rFKRfiLEMtsBgMlu0hF9XrsO-qeeT-A6hmdCH01V-eMA9lz1gli1UKAbW599v8UxrqOL8ax7bB8cljiOdiH6xCdf3xjjbWds0KZrD2rda521w0EBGK8VIQPU0n_2IPfepnEeQIUMWP4pHoJTcTnBjoyDSs7Mq-qvcPPVvDoz_KMU9G_LNTcrPVEw0ibEtXxJm9EeUkL2FYO_kwogxB1zSdMmjRJrB6__iDCwXw9WDCCJ2YCwuY17QP3-y9OqG2wHFfvXuzrYDZCWp4ocNCrup92obOrkWcV0v8lMESMvyt_Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EkgSmngaqhB_r0tRKxtNLiBbpwYLc1d67lzmyUjibrF1hv2_z-ag-rWuUvmE5a6D23U5PP40bYlLGK1PLBnySnNDrCPbHNmeeI3cOR1u8FdUYWjus1kv15TbkbpsrQkYrWSlbnMQm1304UBckHhnkPRC2LIid7yUUBAPp_tcuqQ4IEzLyhBhODDAoT89Rhx4IyMb0fGfEhKQqiy51qi3YcFaI80eWCR4n_1LAwPPbU-bnL4tfzBxeY0ffulXaFSWZD2oJOa-tcQDMzXNX9psweV8pUilLhPgZE3POQo40G-6fOZcDlHxGOloH9PRHAnM1sHGCkF-H81UHhVvv5Cjww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ioELsRFigNktqtaSDGUbl5wL5GbNxd3o3zdXxn249ebvNHzoI8c3IAaUUrzL2HoS23fwsmmI7rNMircGPvMtFLrcKnpYBdD72XYJN1fBsf4LRF3F7ae5kfe1O6NyZTI-MBxBtZyD7_2TeUuRcezcxsO5eHb-nGtpG_5cLg7CzX9Qn1PjySLf4U9WDmKcPBHWXvgfxUrNwy-aGUJhC4JEaA3Yjru9WUh5n-UgUaCeiBsvKct6D8RMSVgxL767jFHLQ2QDmKugpabJfEo_XMBugicWSJ3B1tDZG3BS_ioXo954cwPtHjQOyKVG8TDxr2PdApyYUnN6mj5uZL0ERtOg7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mPcMyrA0uHr-I55oRm6A3lxNEq8M5KQ2Cl_1u1nUyhVr944_7jqnVGOE_0C9CpPp99udRUb_ykbvc_0jbkZMAMLlRUvVwkS4VDgCAW8lRQpNUF6roqhlTz3_-m-pkRUizhVAVVusjW-hsQLiJe_ef3l8lbnPUmX5vnSKlVtW7C27cIkMOXc1Gl3OeBADI87w1DeQvYeLz_eSF0ROat3ADmV-TMvOXCr7Yp4dD3qwVsHN0BM48oepnJpUwbMcwQ6dRNuYrya-QlKa7v2z7c-e9w_aiCRysrKt3oCLP_2lekZRly53L9Ysrg36Lh9jCQfYNzD7pFC659Oc4KBbMyvnLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n6Jrff2Ygu9x8j2sd79Hz9u2432LowGTl3OlwrlkaRHpEnzKm9nyW2pq7hdQ2d4WmCSLOi2k7BS1uhCTKKfYJGNjL-Q2dZBAkn9eeKp0l3_y_6s046QLaZNrTTW_ZnQCQRM4uqh24RtNYINF2JM2bFxKjGDk1vhvRPdjHmbzKJZxsqy_DRqeK5lGyCAZ69auN5QnbyOGlRxd6t57EpvudkT0OWrnppgQQNK_ii1Dhod3w8EReg6ytKhQfMqab6kc23oo6NztgYhcywvXGNc3FH1yd4mPLvvu8Z3eNfzd92AjwaeM-5p21m2pifqeo1u4esMwowOLmfLHxH4jYD3Jjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حال و‌هوای کربلا پیش از مراسم تشییع پیکر رهبر شهید
عکس:
محمد آهنگر
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/448049" target="_blank">📅 23:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448048">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d765e01d85.mp4?token=n82YM_tpYVnF9JqxzPv5-nT8Mf_OUlRIGarcAz_gMfsTNQWjcS5Q0ezutyaoWAbU0FzabELLsButwjWhLjdh7-nPzBJKcHY1FoHL5z3wwekt14Jp0-g8llrFw0Lg-IaUiHekvj9TF7fgWMzDTBFCfoqcme56SpfzKequLQv167fDKyvB7Gowfxz5YxnR6lsAJrXEUAmgP4l1RwiFOqexAY2v4Mzy2tK59y2YhZVLtww0PKWxPumo1EczChp7z_6vqzSNPuAVH2wdG8E1e1JtnS1kdMOeKz1PhKG4O1pCvg5m0RlhKOFWrw_9mRDt2eVZEQDs9Pv9vR3a0eJ4OZh7CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d765e01d85.mp4?token=n82YM_tpYVnF9JqxzPv5-nT8Mf_OUlRIGarcAz_gMfsTNQWjcS5Q0ezutyaoWAbU0FzabELLsButwjWhLjdh7-nPzBJKcHY1FoHL5z3wwekt14Jp0-g8llrFw0Lg-IaUiHekvj9TF7fgWMzDTBFCfoqcme56SpfzKequLQv167fDKyvB7Gowfxz5YxnR6lsAJrXEUAmgP4l1RwiFOqexAY2v4Mzy2tK59y2YhZVLtww0PKWxPumo1EczChp7z_6vqzSNPuAVH2wdG8E1e1JtnS1kdMOeKz1PhKG4O1pCvg5m0RlhKOFWrw_9mRDt2eVZEQDs9Pv9vR3a0eJ4OZh7CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۲۹ شب مقاومت گرگانی‌ها در سنگر خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/448048" target="_blank">📅 23:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448047">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/219dc4d8ed.mp4?token=iLQpR5Q8iStwVB3PavoSehUPmBs3NRh6CVK_JjjNi4gyVfwvfwJkIy4pO2OO2cn9f7TG0Kjard-GJ0RW--J5l66qDO2gBSVU7uzmaZd49rLEnjfFs4mgrEw13Kv-p6VDPJgaM3sYVorpWVJ_f2ceR9ZFLKb3Q-rQ75VpidTQDplfO2u8J2Pk1218G3CVIOFpDwjivRiJyeaMD1sV8e0DthuvICK1-8x8922xnS0pjxzIruAiM00TjNPYGXH1cCHHyIyLYaO4USzBSGQYqnKctKlsV8LxhhMYJc5ZB8am4iVr7iUI7QvVjmQqD9AEJbx1tAZrgr3CfGkR0adSk401HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/219dc4d8ed.mp4?token=iLQpR5Q8iStwVB3PavoSehUPmBs3NRh6CVK_JjjNi4gyVfwvfwJkIy4pO2OO2cn9f7TG0Kjard-GJ0RW--J5l66qDO2gBSVU7uzmaZd49rLEnjfFs4mgrEw13Kv-p6VDPJgaM3sYVorpWVJ_f2ceR9ZFLKb3Q-rQ75VpidTQDplfO2u8J2Pk1218G3CVIOFpDwjivRiJyeaMD1sV8e0DthuvICK1-8x8922xnS0pjxzIruAiM00TjNPYGXH1cCHHyIyLYaO4USzBSGQYqnKctKlsV8LxhhMYJc5ZB8am4iVr7iUI7QvVjmQqD9AEJbx1tAZrgr3CfGkR0adSk401HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۲۹ شب حضور عاشقانه مردم تربت حیدریه  در خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/448047" target="_blank">📅 23:33 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

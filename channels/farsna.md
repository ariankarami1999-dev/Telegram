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
<img src="https://cdn4.telesco.pe/file/r5kromcne9Nj0cZiR-SZRkIKjSK-QyDxwMynKPhCn79eqt8lo0uTxd7vQlbPbkgjVZw9hfWzZHXd-mRXl63H4WQBinBEa1rEa63r7J9wtik4DMJq9kLlLgpeV6aXN_JDk65mBeIQTW41s9MF3hkJzgBO7HPNaT-3MPiCEesuHt-vm0GGDHOfzeOkyan-orJvTiblcR8_3r-i31kcBl_8lAGGAIFmhEsPQkGVg6K50AG75pNXqSkNWYN0jFfNGBOqpzsYyAHR29d4ASHaOlbTisb_uwk2ETqkpJXjWi7CZJ-Lu3RqEUPt003Vm-ZK3_ZR78ucdrcffkFpVoVaQaMyqA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 19:23:40</div>
<hr>

<div class="tg-post" id="msg-451159">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NXYTIn6yl8Nyk6f_yINuerpjv8tTVKsoZ2dvk73eGa-JZqNaZ0XObauYw7zIrGNhziQo7bAClClSbJqfwHW_0OwBqsF0YYMfzTVihgUHEHFj7nLrfbJOEOyojcMSHY-WvcDxueybM_3XRoqKl44aKKdfEFAopwd6f8RX62ttyYI9foPGPdcEflM6mLbcATIQtC9cZEa5W9uhvmqfdCVaq9W3FZ5nxuWaXrrDoAjJYprlzgeeq1zkW78k6Gl9aphMG0RBKMi8fHTdqSUpgGveUdf0WBY_mwZq_M-LQs4FSo13D0bcV6-v_Jv9XDR6tLuhTO3skb5Xaqo7gA3O6DWozA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gae8B8REBhq496Hy5J7Zo0XuqH-cCKuCE-Uj7mkvp0_g0ZKNp_U4595gt6XAZvo9liqmA_IljH5cZCa7r95gNbC0MukO9oDXWGtpvueye5fwFZEwJQaSo3qin8AcOg3MNuH2Mnsst3s448XOdmioupmciz-CZU10dca-7oBHPvz7Xqa8QDzPJDxG_lXZXOb-ywQw28SvdPLUJMAgPHM3ou7SAKYi8tnd5sRPwe5fwJ83JYsA92VSqlZiICuEa5ny2VwOlYRAC09ELJnXxLzynyDYl9i8CbKiyPJs5kvRDFhc-zQIaIsQJI-kZ4Cw42iGwG7LLYzl8L5k0xeg-RmCHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‌   سپاه: سامانه راداری برد بلند و چندین فروند هواپیمای راهبردی سوخت‌رسان آمریکا منهدم گردید
🔹
سپاه پاسداران: در تکمیل عملیات مقابله به مثل شب گذشته رزمندگان غیور نیروی پرافتخار هوافضای سپاه، در موج ۱۵ عملیات نصر ۲ با رمز مبارک "یا اباصالح المهدی ادرکنی" و…</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/451159" target="_blank">📅 19:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451157">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AniKjaGlKQyb67CjKZOUf64JpsAxjPjAb9L4bf8fqdnb0_o73lEon-ONuTxW-VY0GeCJeOUDrZDwhdUaGqHw5AsQZCEq0-JjUxsEHYayujCcsF48qZKYXKgs3asJiU2Vx8Fm-gqBqlWyE7SzHRXWC823INgQdPr7a7GOyiVSXWVk14KTQdjKwVouTV9axVPkC1MoP3aQ8Xce4dzaJ0jXboS51Sh0KsRyImbdp_c1bgMBPt-aUDZPpoOTx9-DBamtvaPC3tYPOHzHjX3U-4dUH-jP0tvRNdHMrZ53pVva7hodpsq6jo3RBBEo68Lg1-JSncEd86Htfxx_cumo_6wM8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W9lcDx_J8rEao9OXRjqbJrwDxGg96x4zenxfxFsTWUZBdDq2FtNKOg0fD4_y5wBgoKCEc2ZFePhzGg9AeMLZE-PVtx7yvb76mXzZZqUarA2fDrDjx6k8Vj9EK8HAMDaf2JzbDRnFRi4P-Q6ILRpuarVWa2wtW1950QMwHnOaxBPw-s9Tog20VQmGrSqXM9eRff-fXup-vuBuDYqcPi8z2xq5JejbrelpCg3G7eQPGF0Q40UTJBYqT6I3nTaV-c_drtK9qCNDan7PL325w0sijoIhKROrqe5szI45B52ymUhBZ_6Wx7yoWD_jOmQGlpB3Kj1SEPKbJOlHXgwpA_gzRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همچنین مرکز اصلی هوش مصنوعی بحرین که در هدف‌یابی دشمن برای ارتکاب جنایات جنگی مورد استفاده شیطان بزرگ قرار می‌گرفت با چندین موشک بالستیک و بیش از ده‌ها فروند پهپاد به طور کامل تخریب شد.</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/farsna/451157" target="_blank">📅 19:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451153">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89dba6c54c.mp4?token=GxvQyvHrCHLAO0RI62tZe5vdRvCz0RaGLiwNfA1hCpejUiw66hLmWWGb2E8OydEWJtvX3BFneGjcWBQ35-rL5zGFHltVHWAQsTaQ8ZJHS6Ns9BmlcwFiH0aWx6igBN2xNo_deIETTXLo9u4gzLQD_rBxRctjFV89hBVfzzBMfDq46JKXMXQxUODycH0k14JHd-LjKZRjwX80VemnLRplbu-UbAUdb_bEygU21nFUgxRI9S55DNZrCI7DN01a-w3_WXNeL--_5foVTfsrYThAoL24AUNMZ1q1ytAFfo37FIDyhBL5sNlukMMCTUNHiHWMjYDF26Xk8y-BtXDgFWVIkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89dba6c54c.mp4?token=GxvQyvHrCHLAO0RI62tZe5vdRvCz0RaGLiwNfA1hCpejUiw66hLmWWGb2E8OydEWJtvX3BFneGjcWBQ35-rL5zGFHltVHWAQsTaQ8ZJHS6Ns9BmlcwFiH0aWx6igBN2xNo_deIETTXLo9u4gzLQD_rBxRctjFV89hBVfzzBMfDq46JKXMXQxUODycH0k14JHd-LjKZRjwX80VemnLRplbu-UbAUdb_bEygU21nFUgxRI9S55DNZrCI7DN01a-w3_WXNeL--_5foVTfsrYThAoL24AUNMZ1q1ytAFfo37FIDyhBL5sNlukMMCTUNHiHWMjYDF26Xk8y-BtXDgFWVIkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
آتش از مقر گروهک‌های تجزیه‌طلب در سلیمانیه همچنان زبانه می کشد  @Farsna</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/farsna/451153" target="_blank">📅 19:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451152">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pp80RF4XkatAW73VusUeXyt16EBHplwURB5Jl4HVTVDuqVJh-nkh5znuMTIUOOll4Qy1887T4W-JSnE349H7PF80XOZ5GEWt2xRwqxoaFc_fDPze_SuKOmnmHadd2zykQ-3KEDcNXp0GXWaOAhHdyJ-B7hI-Wbea5XKQwYKHyvhR-TmxAhFULy54V9Ug7z_hdHQEYP-DsCrLLgD6bGxHfPUkG3BMXOuI3K1Nwxd2grgQjmBlwB7_R6_drABMAOlP5ZWgxK90otTYHAUHxqHP6llMCF0ekdQ80gs5tQKJqzE_Vh2qdCqcgXhAdnMw5y9jsSK8WuBtzkU2EX2J3jOyow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منابع عربی از هدف‌قرارگرفتن مستقیم یک نیروگاه برق در کویت خبر می‌دهند
@Farsna</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/farsna/451152" target="_blank">📅 19:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451151">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1ac9f0f42.mp4?token=WAI9u0xF6Kya4AvEGW3f5ekTM1GycXUX-74_1Xb72NxLA2xHfzeIdp-D2dAsW-BSdA3I0CcOA9tyQF9YGEbA12sw4tpYWaq57AO_6_lHpyP4_WpMLPVj-rt5JyhPtsTXnrhxRuP6R-JMDIbGM2lSIackM2ZaXDlhDxAFgLJjn5DgJvxCGkW9lTFBHEKAHnOpydruwf6dMu68QjalmAXX1CLPpr0O3wq3iSkjDbHn_7cmChsIj9ZxW5Xo91L3w16TQO7kkKERZKS5gyBrWaccLZ5Puc1QVE7qH4zpaxjio1nna1hET_eUQ_zMPzY93tGgn9-BiaH5u7nfiQplo3xRdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1ac9f0f42.mp4?token=WAI9u0xF6Kya4AvEGW3f5ekTM1GycXUX-74_1Xb72NxLA2xHfzeIdp-D2dAsW-BSdA3I0CcOA9tyQF9YGEbA12sw4tpYWaq57AO_6_lHpyP4_WpMLPVj-rt5JyhPtsTXnrhxRuP6R-JMDIbGM2lSIackM2ZaXDlhDxAFgLJjn5DgJvxCGkW9lTFBHEKAHnOpydruwf6dMu68QjalmAXX1CLPpr0O3wq3iSkjDbHn_7cmChsIj9ZxW5Xo91L3w16TQO7kkKERZKS5gyBrWaccLZ5Puc1QVE7qH4zpaxjio1nna1hET_eUQ_zMPzY93tGgn9-BiaH5u7nfiQplo3xRdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زاکانی: در شرایط جنگی ظرفیت‌های خود را برای خدمت‌رسانی به زائرین اربعین کم نخواهیم کرد
@Farsna</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/farsna/451151" target="_blank">📅 18:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451150">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDKIm0XLA-Ile98jLRXB1PPcw5duZ5T_-DDsyBcB1n9V58lQFSDT1t8f1mvggHxvv0Zl7Y_hehwEwlukv_K6SFse9pXXSo0inwVlaJIr8eUlueWWAxsBMUJ4Nasnq9_BaWFHMzZQCgFZ8Wnl2FirmnXBk9jnEbTpYDrOv_VhA-Sacr1sMB0iZejEPZSSKV9ebU1iAgekEmz12yvmmFwC-opfGU9_ocoZulnRRRDyMBmfG-vOxcjcEKlefcHWXH1TCTC7DZ8E3i1Tb3gfR3J37hFLEHnAwoGbtxQ8MsTZzsZd7wp6NJluQzCHTyWUjuMIs_7mFsTo-aZ8X8oIBGNRWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلار ۱۵۰ هزار تومانی هم صادرکنندگان را راضی نکرد
🔹
قیمت دلار رسمی در مرکز مبادله از ۱۵۰ هزار و ۴۰۰ تومان عبور کرده، اما معاون سازمان توسعه تجارت امیر روشن‌بخش قنبری می‌گوید صادرکنندگان همچنان از نرخ بازگشت ارز رضایت ندارند.
🔹
معاون سازمان توسعه تجارت می‌گوید دولت صادرکنندگان را ملزم به بازگرداندن ارز با نرخی می‌کند که با نرخ‌های غیررسمی اختلاف دارد و همین موضوع بخشی از سود آن‌ها را از بین می‌برد.
🔹
در حالی که رئیس سازمان بازرسی پیش‌تر از بازنگشتن بیش از ۹۴ میلیارد یورو ارز صادراتی خبر داده بود، معاون سازمان توسعه تجارت تأکید می‌کند ارز صادراتی به کشور بازمی‌گردد، اما الزاماً وارد مرکز مبادله ارز و طلا نمی‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/farsna/451150" target="_blank">📅 18:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451149">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40aee3acff.mp4?token=j6MvZg4JIKTi3ii92TqW4RVQqJNO_IR7uHLmgjoNATwMIjw1aWhFYXLbbzZUaQ4hsE62xdeWubQ5HTg1Nk5z0hY_x5cP8jOlDndYMWZhktKylywV8WhK7qH5Q_te8qDYnxd4B9Nuq1OId5AnnWFszbybZ-FiDVM7USQIzGZgKXJl_nifjcq9MzlFgkbtgNH4rjy0JwNFDF6dO1yrCKUsanLOZieI5vJgVfVf9eT6WdMSY0dGlZ3KUQ2EHYaPZxryLdgDZXR489pBsyFX_GWWtKOE0FvRxdLeeH7H0-uKx0FNEpnChgPbHaFBcNan2bUcsgWlyZin1a_AqDkOpm7Hrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40aee3acff.mp4?token=j6MvZg4JIKTi3ii92TqW4RVQqJNO_IR7uHLmgjoNATwMIjw1aWhFYXLbbzZUaQ4hsE62xdeWubQ5HTg1Nk5z0hY_x5cP8jOlDndYMWZhktKylywV8WhK7qH5Q_te8qDYnxd4B9Nuq1OId5AnnWFszbybZ-FiDVM7USQIzGZgKXJl_nifjcq9MzlFgkbtgNH4rjy0JwNFDF6dO1yrCKUsanLOZieI5vJgVfVf9eT6WdMSY0dGlZ3KUQ2EHYaPZxryLdgDZXR489pBsyFX_GWWtKOE0FvRxdLeeH7H0-uKx0FNEpnChgPbHaFBcNan2bUcsgWlyZin1a_AqDkOpm7Hrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نقشهٔ سلطنت‌طلبان برای جنوب ایران!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/farsna/451149" target="_blank">📅 18:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451148">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TFoD-ExAfbpDF2Z5ewUCO5sXABdcGQnEqfLbohIvIMbV-5i1aKWyt_i7EFROJt7Eb6EUsusYRQEjn6N_2uYD-yHX-nNhBTUZ1HJfgW8GWLhDf8X0HQuqM4n7iDJzkaAXhRMyR3cC7C0AsW4m3Xf6pv-ELyjK-JU1si0yrsCuLSOg8R6gwQElvNpFVSsJVtDT63WaBfxrEBWm3XMef4dLfI_5kCfDnxs_ayMHkrXWt33RybCLc37b5Wosfrkbkq2TMwMB9De064XbvYMhnBC1CwBBZrm9Id-s6qTmRJxGCqQ1GAd91gckF_s7hNQ3dCd9v-MzkNIqpx8UJed5HUXL2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر نیرو: در هرمزگان خاموشی نداریم
🔹
در جریان حملات دشمن ۵ خط انتقال برق آسیب دید، اما این خطوط در کمتر از ۶ ساعت بازسازی و وارد مدار شدند؛ هم‌اکنون مطلقاً در منطقۀ هرمزگان خاموشی نداریم و همه مناطق درگیر کشور نیز در اولویت تأمین خدمات قرار دارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/farsna/451148" target="_blank">📅 18:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451146">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">جزئیات طرح جدید بازار جدید انرژی
🔹
سند ۱۰ صفحه‌ای به دست فارس رسیده است که از تولد یک بازار تازه به نام «بازار بهینه‌سازی انرژی و محیط زیست» خبر می‌دهد.
🔹
نسخۀ نهایی این سند تیرماه ۱۴۰۵، توسط معاون رئیس‌جمهور اسماعیل سقاب اصفهانی تدوین شده و حالا نوبت کمیسیون اقتصادی دولت است تا آن را بررسی کند.
🔹
ایدۀ شکل‌گیری بازار انرژی که هم‌اکنون در دولت تدوین شده، پیشتر در قالب طرح وان توسط سعید جلیلی مطرح شده بود، هرچند این دو طرح در جزئیات با هم تفاوت‌هایی دارد.
🔹
طبق این آئین‌نامه ۱۰۰ درصد سهمیۀ انرژی مصرفی بخش خانگی به صورت سرانه و براساس بُعد خانوار بین همه خانواده‌ها تقسیم می‌شود و هر خانواده در صورت مصرف بیشتر باید انرژی خود را به قیمت آزاد از بازار خریداری کند.
🔹
این طرح یک دگرگونی ناگهانی در حوزه انرژی است و عملا قیمت‌گذاری حامل‌های انرژی را از دولت به بازار آزاد می‌سپارد.
🔹
در یک سوی میدان، کارشناس انرژی رحیم احمدی معتقد است که برای اولین‌بار، کاهش مصرف نه‌تنها جریمه ندارد؛ بلکه منبع درآمد می‌شود. به باور او، اقتصاد بیمار ایران به همین داروی تلخ نیاز مبرم دارد.
🔹
در سوی دیگر، کارشناس اقتصادی مهدی پناهی زنگ خطر را به صدا درآورده و هشدار می‌دهد که دولت اول شوک گرانی می‌دهد، بعد پاداش؛ او از دست اندرکاران این طرح می‌پرسد، آیا مردم اصلاً توان کاهش مصرف دارند یا این طرح فقط یک قمار بزرگ روی توان فرسوده‌ترین قشر جامعه است.
🔹
مرکز پژوهش‌های مجلس اما پیش‌تر درباره «شوک‌درمانی» در اقتصاد هشدار داده بود. طبق این گزارش اقدامات شوک‌آور نه تنها اصلاح نمی‌کنند، بلکه با آثار منفی اجتماعی، راه هرگونه تحول را می‌بندند. راه‌حل به اعتقاد آن‌ها، تغییرات تدریجی و کوچک‌مقیاس است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/farsna/451146" target="_blank">📅 18:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451145">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea066cca8e.mp4?token=XWtEVwEGTxaWNI6yeC5g1XaLbun2hSxAjPJeu6RdrdVKYNKcKlzgFZ3fX6KrCMfC7OniRMMantOe-KWeVdc3OGqYAA5zMwJ_LL1PbEEYYdkckwStrBaNRQnW8-KeIy-Hevd69fF2La8k2JaDBayr7Avteie_pG-I5fR7lKU_-wVYZMgwPbEGfPDbUMflbQ8OT4hZgyWxAFoErqsI6R0_CPuvNRsndiQIePszNZRAbUg_oeVTYiJkTtCscBJ6ZrIEi1VhZ1KZliso1AJNzBVdKc8XqJECKO255bINn3yPUTb3EkRlD_B5kABtzjcT0hg2OKb_IbhWu0wqQZF7VoBLrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea066cca8e.mp4?token=XWtEVwEGTxaWNI6yeC5g1XaLbun2hSxAjPJeu6RdrdVKYNKcKlzgFZ3fX6KrCMfC7OniRMMantOe-KWeVdc3OGqYAA5zMwJ_LL1PbEEYYdkckwStrBaNRQnW8-KeIy-Hevd69fF2La8k2JaDBayr7Avteie_pG-I5fR7lKU_-wVYZMgwPbEGfPDbUMflbQ8OT4hZgyWxAFoErqsI6R0_CPuvNRsndiQIePszNZRAbUg_oeVTYiJkTtCscBJ6ZrIEi1VhZ1KZliso1AJNzBVdKc8XqJECKO255bINn3yPUTb3EkRlD_B5kABtzjcT0hg2OKb_IbhWu0wqQZF7VoBLrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌  تعطیلی بندر العقبه اردن و فرودگاه رامون اسرائیل در پی حملات موشکی
🔹
مقامات امان امروز محوطۀ بندر استراتژیک العقبه را به طور کامل بسته و فرودگاه بین‌المللی رامون در شمال ایلات اشغالی نیز پروازهای خود را متوقف کرده است. @Farsna - Link</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/farsna/451145" target="_blank">📅 18:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451144">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/venpTkL2dPFneiVKbJQEofBPNxUaRH6SYXcyergMvC6TRi9RbTHzzGWIZH8kynCwHqRMh3imvdNpPQBMBGujSU3TYU8d_wWYHfjoyQ_40Ut5ozY9YcDvai9OsvI8jI855KtFxqDQGwkQzPHsPcz4RIZC2OpUPwBkrljFgzJNzy1b0h9OOmrcr9Zq42U2uuAO6D6wnKqWF4kc6oiASkWWz4GDwWzPKZ0CDG465jLLm4sno3oWrZLv2fS2n4iOOV-t0IgGHdjEsmWq0Z4on-pirgcGgpXUMy2M-b7K0LN1v7JCnkBle3j_-XaQ6f5mTMfpzSE2XY40XDKFCP5izL2O0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سردار قاآنی: در دورۀ زعامت حضرت آیت‌الله سید مجتبی خامنه‌ای، مسیر نورانی و پرافتخار مقاومت را ادامه خواهیم داد.
@Farsna</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farsna/451144" target="_blank">📅 18:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451143">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87473a57e.mp4?token=iPllPF2vfv9xsQKkdv1aBg4tgDcc0dq_A-erxrKXCB0dD3dYdKAV-EzVDse6weu96ZSZPVY-1ob32YiJv4rkSRxo2827geD0blGet6xrbscDARMEvWOE9nznm1_qYWATiXoxsGN0ShOWBJkGZbxPn8sUIx7AMeoGidB_x7O2DZ-BmNY9nCl11s4GLuo4Juy2-Ynnfmo6zmG_kqOYAqAfAArrgKyPU-M-yDcZhFI-yMh0UXX-wrsgvA29baCIlp15NlQAJAJS3DPYi_oHL40fwY5VuY4Qi7ZZho-VGq_F6DQm-vGT5XuzbBnI2iJanlGngvz_HUHgNHhgrdE1atI51g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87473a57e.mp4?token=iPllPF2vfv9xsQKkdv1aBg4tgDcc0dq_A-erxrKXCB0dD3dYdKAV-EzVDse6weu96ZSZPVY-1ob32YiJv4rkSRxo2827geD0blGet6xrbscDARMEvWOE9nznm1_qYWATiXoxsGN0ShOWBJkGZbxPn8sUIx7AMeoGidB_x7O2DZ-BmNY9nCl11s4GLuo4Juy2-Ynnfmo6zmG_kqOYAqAfAArrgKyPU-M-yDcZhFI-yMh0UXX-wrsgvA29baCIlp15NlQAJAJS3DPYi_oHL40fwY5VuY4Qi7ZZho-VGq_F6DQm-vGT5XuzbBnI2iJanlGngvz_HUHgNHhgrdE1atI51g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر راه: پل‌های تخریب‌شده را فوری می‌سازیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/451143" target="_blank">📅 18:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451142">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10883cd0fa.mp4?token=mMuH7WgSP9mP4eCVlTueGy0_lIKyZI978zOmshwWJB12ZFqfBpFPxPHzBgnAjrN2jOtftIQlnENHZBkiRz9N6eCcRZINl0gTIzUN10ma50dIG3RmSKtj6v6_Y9pLvq08N8gEdjyrOZHLowIZ-J8y2cLWmneOmgcdQrsEpZ1Qots_E7FYCNk7_YQArRZqF2LKUy9x_DGjN2KL87KiXH-crw2hZeLlG4WR94NP7l1UrC_PrYKEsJBHV-SuZmhEyNu18wEfs1yaK-nNvt5wNolXDtLHCN4Fe1G1pX8fwtvuYKZeWyc7XuAmmPEU5uIpXZfXSpMPT52sDCDCxmzU4U9gFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10883cd0fa.mp4?token=mMuH7WgSP9mP4eCVlTueGy0_lIKyZI978zOmshwWJB12ZFqfBpFPxPHzBgnAjrN2jOtftIQlnENHZBkiRz9N6eCcRZINl0gTIzUN10ma50dIG3RmSKtj6v6_Y9pLvq08N8gEdjyrOZHLowIZ-J8y2cLWmneOmgcdQrsEpZ1Qots_E7FYCNk7_YQArRZqF2LKUy9x_DGjN2KL87KiXH-crw2hZeLlG4WR94NP7l1UrC_PrYKEsJBHV-SuZmhEyNu18wEfs1yaK-nNvt5wNolXDtLHCN4Fe1G1pX8fwtvuYKZeWyc7XuAmmPEU5uIpXZfXSpMPT52sDCDCxmzU4U9gFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زاکانی: عملیات نوسازی ۲۵۰۰ واحد آسیب دیده در جنگ آغاز شده و طی ۲ سال تمام خواهد شد
@Farsna</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/451142" target="_blank">📅 18:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451141">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VW742tcQa_suSApGFm1TgbusgpCLrVl21bfJFJoMtz3bIOo4_zqZne4FWiFPWpaWM4mZKQ9oVaw2fEhwwZceQSo-v6OiFh8ehvihOUBI9j9eYeYMNQBxWwO2sirAE4zNjcQDto5KcnEZPH1JoNPHWCo0SHExe0FFiBL82aXYXe2kQmjPOH8WdS-dZehrGRx_AR15h6smojXLNPnJf4foW4xhAF3nGKzh0oxQN62titKIDXAtEDim2zuJU-BclmI2bqYsTCltsDr01dp4fcjqw1b3250VsZHzxQhmRMHDthvvByJMQBm-B5SVmGQ8HIeMqhuwU-_DtVlLopPhmopesg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملۀ آمریکا به سایت نیروگاه هسته‌ای دارخوین خوزستان
🔹
سازمان انرژی اتمی: رژیم آمریکا بامداد امروز (یکشنبه ۲۸ تیر) حوالی ساعت ۳:۳۹، با شلیک چند پرتابه به سایت درحال ساخت نیروگاه دارخوین حمله کرده است. @Farsna</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/451141" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451140">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4176f63ab3.mp4?token=m9gjVgPP2BBfLHya8Q-SYP2LGVR5Q-mKkrSWKfQ5CagPG3elMwRzfBClOThipSrEkddkyv6bfy6QjvPTzospOYbifL7wQxd1cs4fF_igAHYorhsoMjNkMKJ1iYyUynX_VN0PvWbSGfWguFqqS44QdhJ6hoiq4bMx_wYDbQOGNWg4OItRrh0qWPfiwIfwS1ZecLto_P54GMNG-GSpy-FN6MizJVzn-j8HrBPPaTFdAr2ZqqAE6kMvKM74g_nXbhIOkRSwlS6VisNAt2Uwl3XVB_EM7o5zvLavVArg9pp29p3hqFLq0fgp0M40r9GCCZMHCgDJ5pw8nd3ibbQvYYsOuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4176f63ab3.mp4?token=m9gjVgPP2BBfLHya8Q-SYP2LGVR5Q-mKkrSWKfQ5CagPG3elMwRzfBClOThipSrEkddkyv6bfy6QjvPTzospOYbifL7wQxd1cs4fF_igAHYorhsoMjNkMKJ1iYyUynX_VN0PvWbSGfWguFqqS44QdhJ6hoiq4bMx_wYDbQOGNWg4OItRrh0qWPfiwIfwS1ZecLto_P54GMNG-GSpy-FN6MizJVzn-j8HrBPPaTFdAr2ZqqAE6kMvKM74g_nXbhIOkRSwlS6VisNAt2Uwl3XVB_EM7o5zvLavVArg9pp29p3hqFLq0fgp0M40r9GCCZMHCgDJ5pw8nd3ibbQvYYsOuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکایی‌ها به این کودکان سرطانی هم رحم نکردند
🔸
جنایتکاران کودک‌کش آمریکایی_اسرائیلی با حمله به بیمارستان شهید بقایی اهواز و بخش کودکان سرطانی در شامگاه چهارشنبه ۲۴ تیر، توحش خود را کامل تر کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/451140" target="_blank">📅 17:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451139">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxI3ProAGIlHSLX4bZnPLjQKPvUSlgy4c2eyii0dvW_fm2O53bypaI_moiLzH1ea56Pv-HcrXoDXx9VytPAoqQBR52ZJGPpBSAGrEK7JlL2TVWeUd13ftnpN3GFpMna6sgD8LtVyuCpZFs3vjSIyHaDCvGVzfQAgyx7rPLuXlxv1OnmXv0rP11JlUBm2Ki77Mpz6uaYnQcIT6HDnRtZ8pSVuFcapylEs1_AC4lgNqQj2cUNisLZaM4T5ENJjucMWKocwFCyV6g0S1VTUFwdsm3ypenf2-xVKNX4-Q353EeutB-ObScgPHK_Pt9U6O8SAuQNWSJI2uVCZEwHQqMNJsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار پلیس فتا ایلام در خصوص لینک‌های جعلی درخواست کمک مالی
🔹
رئیس پلیس فتا ایلام: مجرمان سایبری پس از دسترسی غیرمجاز به حساب‌های کاربری افراد در پیام‌رسان‌های داخلی، با سوءاستفاده از اعتماد مخاطبان، از طرف صاحب حساب برای دوستان، بستگان و مخاطبان او پیام ارسال کرده و درخواست کمک مالی می‌کنند.
🔹
هرگاه در شبکه‌های اجتماعی از سوی اعضای خانواده، بستگان، همکاران یا سایر مخاطبان پیام درخواست کمک مالی دریافت کردید، پیش از هرگونه واریز وجه، حتماً از طریق تماس تلفنی یا راه ارتباطی مطمئن، موضوع را با شخص مورد نظر بررسی کنید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/451139" target="_blank">📅 17:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451138">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMjfVzWPNe5nzNUIeCrWi2Yt1mkiBp4yzx-o84BLXWGlxXuJJbbH4KLG8pAf70O-W3HoMqrO5AVi34oA2QnRDtIjU_3YS2P74Gc-MkQhjovUDtDqw2Z3rcIYX3xSWG4YetRxB4hRIgkjwHFi3fUWprUbzmaokSgMiDtUwz7iY20kPB-UyNus2QrA7iZD3SpCUU_d2-gsQQr-5qAZk_2SAA6fnjwM1-C_2cYUFj_hD0sRW3uV_gOwbRw3Z58X2hMHl5_3XzrHNYadmYyJen4PI8_kb6kVmfHkXQLGe-WftfdLMPGwtAjPpqa6SDIJOFWlS9MD0MHQkjVC3ETE82Sm2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت رسمی بلیت پروازهای اربعین اعلام شد
🔹
سازمان هواپیمایی: قیمت بلیت یک‌طرفه از تهران و استان‌های غربی به مقصد نجف یا بغداد ۱۲ میلیون تومان و از مشهد و استان‌های شرقی ۱۴ میلیون تومان تعیین شده است.
🔸
نرخ رفت‌وبرگشت از تهران و استان‌های غربی ۲۴ میلیون تومان…</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/451138" target="_blank">📅 17:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451137">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJNrzBixQf6DiiMFZxDeFs8sa8bIluhDFIlIW7eNH7-wgU8O_Yg039W5t-YftNiM07vwLoO2-N2wOt-PHkCLEoxL2tfCOGUleHP52IKb4ueCoOGEBVN7_QXhr5j4q-C9IpTsNjhC0Ckpj_ZlRxPBdVmmDHEc6FPI_o1DDcb0I9XsdpornVQoxK4rFJc29jmRlTIjeBIkPKBBFz4Ri-tu9cCLEVh95l8hvReWrSveMlFRO3wf5LhYO4WGDgb5DyRI2T02v87JTg3_mQVYbLD14TCYyQ_3HKIK_jt2iYDhHnjl2v_aYBJdWLSVxoCAVKlIWP-_Fr2n5FMiJoTG8YsWjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
برنامۀ «طبیب» شبکه سه امروز از بیمارستان شهید بقایی اهواز روی آنتن رفت؛ بیمارستانی که طی روزهای گذشته هدف حملات موشکی آمریکا قرار گرفته بود.
@Farsna</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/451137" target="_blank">📅 17:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451136">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22ba567704.mp4?token=IkLE75xFrcJ7EoSuUmUfuEpQMmyre-PmnTM5-XRtoSdDZz8DGmS3aVw021QXCVt--ZWeahnWOFw_gciHx9TDk7HQHkKRdzvAGP91USJ-ZCvNrEsZ2L4ZbXFxa6bGVDJD71aAE3cKOMU1Pd5NWNKf1b08T9azFj51nsXzGoo5ZiKWlGbhiTLv9FbT3BUczw8ggGnNGHG4jwe_P-HC-1sn59ekaLV4jya13v5MuBJZc078Be5Abk_BtxwIQAwHSNjzdIZd2zAfxH4B90tpXE9OHZ9VQCIWyow454HCDCRhpaNdjrd1jX3fSx9MW_tsA6oX3C8egJBPJnDpZgygtGBy-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22ba567704.mp4?token=IkLE75xFrcJ7EoSuUmUfuEpQMmyre-PmnTM5-XRtoSdDZz8DGmS3aVw021QXCVt--ZWeahnWOFw_gciHx9TDk7HQHkKRdzvAGP91USJ-ZCvNrEsZ2L4ZbXFxa6bGVDJD71aAE3cKOMU1Pd5NWNKf1b08T9azFj51nsXzGoo5ZiKWlGbhiTLv9FbT3BUczw8ggGnNGHG4jwe_P-HC-1sn59ekaLV4jya13v5MuBJZc078Be5Abk_BtxwIQAwHSNjzdIZd2zAfxH4B90tpXE9OHZ9VQCIWyow454HCDCRhpaNdjrd1jX3fSx9MW_tsA6oX3C8egJBPJnDpZgygtGBy-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاری که مردم نتوانستند برای رهبر شهید انجام دهند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/451136" target="_blank">📅 17:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451135">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1lCjIQrssJ_4RNFUYj3c3GTF8hNAjIQ-vK5ZanrjDbZJmGA_7gGzOKqHjaT1Oe7k7oXl4FbO64K5Sp_DDf31mg5f-pBvWtoHBNbC_erSQ3Ok6AU-y-LQOYvbiLs_TEI27D8k3GWvTP4uR21pFdhWssDAOa0Vu3klG0cRUmxFX-b0xJl5mAN0BQL0txK-yVH28MmD9lHyma0CAMinzJS4GEC12k94eooLRAKWPofyZLa3rJQoqt5kXmZjg9sOu2LwvJVEkRnA8P1bS1amxZjdIFVfED97-MTFiPOVfnDu3sml1DZL0oVefANJFYv3OHDRZ8vlxPxDeASDZnrs-L9Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انهدام یک فروند پهپاد آمریکایی MQ9 در همدان
🔹
دقایقی قبل یک پهپاد آمریکایی MQ9 توسط سامانه‌های نوین پدافند هوایی ارتش هدف قرار گرفته و سرنگون شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/451135" target="_blank">📅 17:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451134">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
حمله دشمن به یک نقطه در اطراف آبادان
🔹
استانداری خوزستان: یک نقطه در اطراف شهر آبادان دقایقی پیش توسط دشمن تروریستی آمریکا مورد حملۀ موشکی قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/451134" target="_blank">📅 17:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451133">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dde07cfb07.mp4?token=MBn3rQBUeKtQPLFZSvurXxuyIGDMSU8NjZhzMD66sAi4JgCYk37Jrh4qY6bJaEpe3R_MnqW0zzC8I8020c9CJxWAQwZl9wyfVPca5mJdpcyhps4kXSgfk5BlUyO3pgmOmeijhxk9CDT4s6qfs9JbJxJpsbvd9AvXcA6gyZfSZaIILUIr-MNUzGSt-vacxfjF3QeRmv0ORDjELYofHf7mRAasX9iUXjMikEe4KE0MoOq0M05i08wbP9trAkXbU9z1IvD0eJJfKO0gTQJ823ARyCc5SEWM7ftlct0xfxQdFygRXbtfaFVn7Ma1k9aT7KtPS3sAF-dl23HhLFohwfT0gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dde07cfb07.mp4?token=MBn3rQBUeKtQPLFZSvurXxuyIGDMSU8NjZhzMD66sAi4JgCYk37Jrh4qY6bJaEpe3R_MnqW0zzC8I8020c9CJxWAQwZl9wyfVPca5mJdpcyhps4kXSgfk5BlUyO3pgmOmeijhxk9CDT4s6qfs9JbJxJpsbvd9AvXcA6gyZfSZaIILUIr-MNUzGSt-vacxfjF3QeRmv0ORDjELYofHf7mRAasX9iUXjMikEe4KE0MoOq0M05i08wbP9trAkXbU9z1IvD0eJJfKO0gTQJ823ARyCc5SEWM7ftlct0xfxQdFygRXbtfaFVn7Ma1k9aT7KtPS3sAF-dl23HhLFohwfT0gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، کارشناس حوزۀ مقاومت در مناطق مرزی جنوب کشور: ما به لطف قدرت نیروهای رزمنده فهمیدیم باید از چشم در مقابل چشم دشمن عبور کرد
🔹
پاسخ حملات به پل، دیگر زدن پل نیست؛ ما از زدن تأسیسات و نقاط مهم میزبانان دشمن ترسی نداریم.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/451133" target="_blank">📅 17:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451132">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqpEJ7iqd4CgkCmusFw0DcWkodAjaaSshLD4lB2B3UeEYd_hKhgC1vw6HxbVI41K8krxmT3BU9lLtOc7hDLMZuCjPzbFV4JZQIq225nLGQjI65shAepPLuPQUERw_wMzcbNGGPazlpqM0BtUJ7Rz2juM-x0yzc7ZdC_cja8s5nGTB9cjGrKvhjDXZmTMKTUROIsYcF_rCG_ey4oH9CqItMi7UM2FJsAj1U426AtmYmiJzstpeKQJF5zIo-BJfe3D5HXMsb4sy4GZ3iGhsvL3lO_VGrwUoCN2n7pq-X-TZBY-CulYGranWweH3Qi0LIk5z-KjuCIK1ppLpLPxdSoOMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تکلیف زمین‌های تازه‌متولدشدهٔ خزر روشن شد
🔹
سازمان حفاظت محیط‌زیست: اراضی تازه‌پدیدارشدهٔ در سواحل دریای خزر که درپی پس‌روی آب ایجاد شده‌اند، متعلق به دولت و غیرقابل تملک هستند و هرگونه تصرف، واگذاری یا ساخت‌وساز در آن‌ها ممنوع است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/451132" target="_blank">📅 17:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451131">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGaA-syrqEnyeXLCVisAaJInN51wDw41H-tkIu6-oWSfZd6Y38H4P6hKj28C3jD11oOAwipOJOQiDPZW1femhVP4HPQO_ZG8FcaUexxeyE8UlIXxj15fYMv4qUWvyrRnptrmiRCzfKmVdgKNdDAZRPjnxJHM49lwQqCK78odChcStHmLYA9v5WqegBzLsVXRPxIDpE2y0gkwp_sNRuNVeAgwoOJMD7G6eSzMVKiSnZudAMuvFZ_52hTB-8apeZqzm8sXmYcbuzzGQZ9OVCqqyCqiaGQyrhSiZxxXZ09K5e45FaEdHPuxZk7zoUl9NS9cX8_fzYVjlNG_hvm0OqAHYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین پرواز برنامه‌ای هما در مسیر تبریز-باکو-مشهد انجام شد
🔹
هواپیمایی جمهوری اسلامی ایران، هما، با راه‌اندازی اولین پرواز برنامه‌ای در مسیر تبریز–باکو–مشهد، توسعه شبکه پروازهای زیارتی و منطقه‌ای خود را وارد مرحله تازه‌ای کرد.
🔹
این پرواز که از امروز به صورت هفتگی در هر یکشنبه انجام می‌شود، با هدف تسهیل سفر زائران جمهوری آذربایجان به مشهد مقدس و تقویت ارتباطات هوایی میان ۲ کشور برنامه‌ریزی شده است.
🔹
«هما» پروازهای منظم تهران-باکو و باکو-تهران را نیز در روزهای دوشنبه و پنج‌شنبه برقرار کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/451131" target="_blank">📅 17:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451130">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db42a1728d.mp4?token=WTsyqvtgq2yHgE91WwyeKAPf0HJwTBsZgGuoijaKebPGUXpgadtd7KD9LtM6nboCTqZkt_n38A1MN3OjGhrONsaHbIAX5GHWBXYng8-_kSmttThv2Se7ZtNRAxSaqGbOBw7hx0n0fRSaX2ph92lyLwrFfl1GSb-4ObXWBYqJu8GoYZISqnUJaCOyJOTbt4dEqjJYmwzWeDg9Cig4sCSVnC7X8nvHPg_ya3YWjVnIuFF0QFs5d_PrzUXwa5gXAExoLubbG-8MRkuD3Dtto90i1Gey7RwJV2eIz4RGC3aTgyLHFpWFB-EjGVctKi0Z3iR2XiKe_Q2j9un5L24Jdfe-UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db42a1728d.mp4?token=WTsyqvtgq2yHgE91WwyeKAPf0HJwTBsZgGuoijaKebPGUXpgadtd7KD9LtM6nboCTqZkt_n38A1MN3OjGhrONsaHbIAX5GHWBXYng8-_kSmttThv2Se7ZtNRAxSaqGbOBw7hx0n0fRSaX2ph92lyLwrFfl1GSb-4ObXWBYqJu8GoYZISqnUJaCOyJOTbt4dEqjJYmwzWeDg9Cig4sCSVnC7X8nvHPg_ya3YWjVnIuFF0QFs5d_PrzUXwa5gXAExoLubbG-8MRkuD3Dtto90i1Gey7RwJV2eIz4RGC3aTgyLHFpWFB-EjGVctKi0Z3iR2XiKe_Q2j9un5L24Jdfe-UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
داور مسابقه سرآشپز در مناطق مرزی جنوب کشور: آمده‌ام و حاضرم اسلحه دست بگیرم
.
@Farsnart</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/451130" target="_blank">📅 17:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451129">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrCY_qbfAfoGRV0jCLFEOWG3JRauDOpLXboNeenyJD3YThMCJV00C5GmFekGc4vUQzhOxNqYXjqr4FJwszqz_wPm6096zhMT0wWdIyNtE5MK8N7nYFfzONBfP0Yu2xWQLT2kIZP8RNm-BPTtvQ-hqu3QUCICfD9cD7PCKhA_CZ0RWpPXavU66BPkFRZT3x98woYUGczwwYN9zhFC-UkiFycXXJmJm6NC1_ZHS47bI5et_dpFhUUeQQzHVu0MU56IuxVXCW4LJuLOuzmdaVaTkZWI7deK9iXoD767Emzxf1dnv-sgXJUIGwMkiKThEyg8VKLSEtMYmZDv8uIAOyErNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
قاب جالب شبکه ۳
گفت‌وگوی زنده با ۲ عضو کمیسیون سیاست خارجی و امنیت ملی در نقطهٔ صفر مرزی و روی شناور در روزهای پر تهدید مرزهای جنوبی
@Farsna</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/451129" target="_blank">📅 17:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451128">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">هشدار قوه‌قضائیه دربارۀ انتشار محتوای خلاف امنیت ملی
🔹
درپی تداوم اقدامات خصمانۀ آمریکا و رژیم صهیونیستی علیه ایران، انتشار برخی مطالب، تصاویر یا ویدیوها در صورت احراز شرایط قانونی و تشخیص مرجع قضایی، ممکن است مشمول قانون تشدید مجازات جاسوسی و همکاری با رژیم صهیونیستی و کشورهای متخاصم علیه امنیت و منافع ملی شود.
🔹
براساس این قانون، انتشار اخبار کذب، تولید یا انتشار محتوایی که موجب ایجاد رعب و وحشت عمومی یا برخلاف امنیت ملی باشد، در صورت عدم شمول عنوان افساد فی‌الارض، می‌تواند به بیش از ۱۰ تا ۱۵ سال حبس و انفصال دائم از خدمات دولتی و عمومی منجر شود. جریمۀ نقدی این جرم از ۳۶ تا ۵۵ میلیون تومان تعیین شده است.
🔹
همچنین ارسال فیلم، تصویر یا اطلاعات برای رسانه‌ها، شبکه‌ها یا صفحات مجازی بیگانه یا معاند، درصورتی‌که خلاف امنیت ملی باشد، بسته به نوع محتوا می‌تواند از ۲ تا ۵ سال حبس، انفصال دائم از خدمات دولتی و عمومی و سایر مجازات‌های قانونی را درپی داشته باشد. جریمۀ نقدی این جرم نیز از ۸ تا ۱۸ میلیون تومان است.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/451128" target="_blank">📅 17:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451127">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28df5059a2.mp4?token=TaRgoI3XIXhQPs8OSSppMRFZ51ykTGx4TgMgAgyg_airhlSpCUqg5Rtr7us4gO9zGwK11C_jy-jjA8Tk0HnyKTdPaVxTgBnPu5cLw6UKcU0tPDsKVBOSMbUhuV4F77Ww7DYo_1VYjvAhyuBbGxJ9OluoqYVoDQXz4_nDcCSUdbQmcJDNOBTj1towQyg7ql7jtuyvBaBQxYaov9TiTQrx4YR_VbW4j4q3KIrW6OcsgioLJUQFbbDRBjVZ-89KZaQ5mwJQWY29VcjKkTbIX6rPy-u3KSWTnA6gxltEEAPNUQU_VZb5VbtDCpL6ZukF1RcAmRZl40svJ1w4trAmxNH6nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28df5059a2.mp4?token=TaRgoI3XIXhQPs8OSSppMRFZ51ykTGx4TgMgAgyg_airhlSpCUqg5Rtr7us4gO9zGwK11C_jy-jjA8Tk0HnyKTdPaVxTgBnPu5cLw6UKcU0tPDsKVBOSMbUhuV4F77Ww7DYo_1VYjvAhyuBbGxJ9OluoqYVoDQXz4_nDcCSUdbQmcJDNOBTj1towQyg7ql7jtuyvBaBQxYaov9TiTQrx4YR_VbW4j4q3KIrW6OcsgioLJUQFbbDRBjVZ-89KZaQ5mwJQWY29VcjKkTbIX6rPy-u3KSWTnA6gxltEEAPNUQU_VZb5VbtDCpL6ZukF1RcAmRZl40svJ1w4trAmxNH6nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ساعتی قبل یک پهپاد لوکاس توسط پدافند ارتش در جنوب کشور منهدم شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/451127" target="_blank">📅 17:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451126">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a54d87d9bd.mp4?token=oUTNXsJxMvlw4hOUzppvB2PiRtV3iKrBFwIukjCRfUNXTpX069nD_nhVQdHJPAKgBOJPuljJciAaBbBuyMVOA1lnd1AnoG3effS8QpqMjo-hj1KE0pCUQbefqf1kYVRDAPkEWhVb27ebS7KogpwsAoBRzVNxOIqWvOxkltaCYjYbX3YE3EEqQwsPci0SXI_ski4_Km1yWkVVgz5eLjEZK018CzdYotnXQN8I9OiGy10Hdsn-HmBZ3L2Ef59Lveu4P1-0XdXeJdSyBmsTtKuOfwrNHGuEmCj2H2H-wNZ0h1nfNuRuE4lqzV-9lAkuLFS7HFDx2r6v1hlA_qzRzSa1RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a54d87d9bd.mp4?token=oUTNXsJxMvlw4hOUzppvB2PiRtV3iKrBFwIukjCRfUNXTpX069nD_nhVQdHJPAKgBOJPuljJciAaBbBuyMVOA1lnd1AnoG3effS8QpqMjo-hj1KE0pCUQbefqf1kYVRDAPkEWhVb27ebS7KogpwsAoBRzVNxOIqWvOxkltaCYjYbX3YE3EEqQwsPci0SXI_ski4_Km1yWkVVgz5eLjEZK018CzdYotnXQN8I9OiGy10Hdsn-HmBZ3L2Ef59Lveu4P1-0XdXeJdSyBmsTtKuOfwrNHGuEmCj2H2H-wNZ0h1nfNuRuE4lqzV-9lAkuLFS7HFDx2r6v1hlA_qzRzSa1RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله غافلگیرانه به مرکز فرماندهی عملیات ویژه دشمن در منطقه التنف سوریه در قصاص خون سربازان شهید ایرانشهر
🔹
سپاه پاسداران: مردم حماسه آفرین و شجاع و بصیر ایران اسلامی! در پاسخ به شرارت‌های ارتش کودک‌کش آمریکا، رزمندگان نیروهای هوافضای سپاه در موج یازدهم عملیات…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/451126" target="_blank">📅 16:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451125">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">از آغاز تیرماه بیش از۵۰ نفر از هموطنان در حملات آمریکا شهید شدند
🔹
وزارت بهداشت: در حملات هوایی ۶ تا ۲۸ تیرماه، ۵۱۷ نفر مصدوم و بیش از۵۰ نفر از هموطنان شهید شدند.
🔹
در میان شهدا ۵ زن و ۲ شهید زیر ۱۸ سال، در میان مصدومان ۳۵ زن و ۱۹ نفر زیر ۱۸ سال هستند، تاکنون ۲۸ عمل جراحی انجام شده، ۴۶۸ نفر ترخیص و ۳۲ نفر همچنان بستری هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/451125" target="_blank">📅 16:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451124">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای انفجار در کویت خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/451124" target="_blank">📅 16:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451123">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5143cb7b64.mp4?token=oSxyJdwx9Mv7Ce85oq0HvZdTlHC8fxn37MSMOfqFmYwZTNxYzp6pFdA88bPmp-mejU3XdMdkukaLXAS4hhO-wCAiSydsh6Fmn0ocFV4NvLe4quWQ5UvI1XQJpKpQmYUqmzcjeHQn0qRy43drBm81fpzAHUKIh9QqKnjzJkKmwk7D2GPzUJAibxCzzBcZjGbvS0OuMrOlT1H2Bnl9IaShspqnEdIiJsrDNY93ID2Gw81DIyZWgQs0Sv7y4dwMpEC0VZbSfTdjVWhS2zhwP8NymbgpCPH5IXYNKsSahYeRW08kgKGsMz1dIwv0WBbRdWsZ2QVfpasY1VQAKuOekmGelQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5143cb7b64.mp4?token=oSxyJdwx9Mv7Ce85oq0HvZdTlHC8fxn37MSMOfqFmYwZTNxYzp6pFdA88bPmp-mejU3XdMdkukaLXAS4hhO-wCAiSydsh6Fmn0ocFV4NvLe4quWQ5UvI1XQJpKpQmYUqmzcjeHQn0qRy43drBm81fpzAHUKIh9QqKnjzJkKmwk7D2GPzUJAibxCzzBcZjGbvS0OuMrOlT1H2Bnl9IaShspqnEdIiJsrDNY93ID2Gw81DIyZWgQs0Sv7y4dwMpEC0VZbSfTdjVWhS2zhwP8NymbgpCPH5IXYNKsSahYeRW08kgKGsMz1dIwv0WBbRdWsZ2QVfpasY1VQAKuOekmGelQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خانعلی‌زاده، کارشناس مسائل بین‌الملل در مرزهای جنوبی کشور: ایران برای جلوگیری از اقدامات متجاوزانه احتمالی آمریکا از طریق کویت، نابودی و تصرف پایگاه دشمن را در کویت در نظر دارد.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/451123" target="_blank">📅 16:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451122">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">انهدام بمب‌های عمل‌نکرده فردا در شرق تهران
🔹
ارتش: عملیات انهدام بمب‌های عمل‌نکرده جنگ تحمیلی رمضان، در ارتفاعات مسعودیه و مسگرآباد تهران، فردا از ساعت ۱۰ تا ۱۴ انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/451122" target="_blank">📅 16:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451121">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d3a523db6.mp4?token=DwwyzmW1eXqLFrWs3hr-Uah-yL34OORzoRWTFOZyLK08BXHN0fTfdtwdzSS64UuzXR4tQz8YKw5oHzrcsLMK1FOZuzbGRtMxwIaCROtWs12OPmGx6z6dzjUS1-KkXv2CjjjjN1JIz2mf2mGqOvfI0mjF6h03X3MJ0RjjTtIB5YHnBuo7AhWlNJPB5JCqRY2Jkn6H2eiYzExEpmeozP6Td2Sg_l2Fdgd9hEAthd-mhFITo1GYdM-ONY1iRnXGu2bmyqnBxluoPCJrrHLHoTZ4PpZQe9YCAKODmnOcRjte09-flurgk26VEfh1RLllq8CJHT8dgU_qfvoyFPDQjnTHOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d3a523db6.mp4?token=DwwyzmW1eXqLFrWs3hr-Uah-yL34OORzoRWTFOZyLK08BXHN0fTfdtwdzSS64UuzXR4tQz8YKw5oHzrcsLMK1FOZuzbGRtMxwIaCROtWs12OPmGx6z6dzjUS1-KkXv2CjjjjN1JIz2mf2mGqOvfI0mjF6h03X3MJ0RjjTtIB5YHnBuo7AhWlNJPB5JCqRY2Jkn6H2eiYzExEpmeozP6Td2Sg_l2Fdgd9hEAthd-mhFITo1GYdM-ONY1iRnXGu2bmyqnBxluoPCJrrHLHoTZ4PpZQe9YCAKODmnOcRjte09-flurgk26VEfh1RLllq8CJHT8dgU_qfvoyFPDQjnTHOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🎥
در والیبال حریف اسلوونی نشدیم
🏐
ایران ۰ - ۳ اسلوونی
🇮🇷
۲۵ | ۱۹ | ۲۴
🇸🇮
۲۷ | ۲۵ | ۲۶ @Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/451121" target="_blank">📅 16:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451120">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🎥
دود از فرودگاه العقبۀ اردن به هوا خاست
🔹
رسانه‌های صهیونیستی تصاویری از بلندشدن دود از فرودگاه العقبۀ اردن درپی اصابت موشک ایران منتشر کردند.
🔹
منابع خبری می‌گویند چند هواپیمای سوخت‌رسان آمریکا در این فرودگاه مستقر بوده است.  @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/451120" target="_blank">📅 16:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451119">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">پیش‌فروش بلیت قطار اربعین از فردا
🔹
رجا: فروش بلیت قطارهای مسافری برای ‍۱ تا ۱۶ مرداد، فردا از ۸:۳۰ تا ۱۱ صبح به‌صورت اینترنتی و از ۱۱ تا ۱۳:۳۰ از طریق آژانس‌ها انجام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/451119" target="_blank">📅 16:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451117">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fb65cb441.mp4?token=kLNMUgvQe5EqLZnLeLCsZ-O5858O80rA8vwe5hN1Ymd9qiogkfIAjIKIET6H7PyQal3tE8zMA3yhxQMNSF3J-jSjzJnPE_j6XPy-JbN5AtbGG2n8-etZbHl3aonqssdWwvMVD3HTA0Jz_V20HEGnii35mzo2pexdQ3t9cMhR3_xlEj0aREyAk4gzAFYjILdE4kaeLSyBN3KNH_4dG2jEtDmIhY3Evxw-ileFThtmL34lsSmrOSG_e4nhRaxy8O9tGCnuoLZac7JEe1smOZ3tdSygn2dpZHQnfB9IQBWpBQGOTlAh1iBLneUDBgBXUwTbM1m0uN36YhTOlzMkymIJjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fb65cb441.mp4?token=kLNMUgvQe5EqLZnLeLCsZ-O5858O80rA8vwe5hN1Ymd9qiogkfIAjIKIET6H7PyQal3tE8zMA3yhxQMNSF3J-jSjzJnPE_j6XPy-JbN5AtbGG2n8-etZbHl3aonqssdWwvMVD3HTA0Jz_V20HEGnii35mzo2pexdQ3t9cMhR3_xlEj0aREyAk4gzAFYjILdE4kaeLSyBN3KNH_4dG2jEtDmIhY3Evxw-ileFThtmL34lsSmrOSG_e4nhRaxy8O9tGCnuoLZac7JEe1smOZ3tdSygn2dpZHQnfB9IQBWpBQGOTlAh1iBLneUDBgBXUwTbM1m0uN36YhTOlzMkymIJjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
شهرداری ایلات: صدای موشک‌هایی که از ایران به اردن شلیک شد، تا ایلات شنیده شد.  @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/451117" target="_blank">📅 16:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451116">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWupaFmyGvirNhPRWouhlqHq8RJwl1yom1-w45bTa8dIBhh5FfYCOpuaTPyRIdkdDlUN4SnjMO9VZa2_TIqAKj3nMrFfjc9HlwrLqypbFFgZhC26p4-eA9eCLrB0DRMp8N8Z1Uh254Y65wt2eUljiCgXQnuK26KDxTTpBrcK6x7ewgUQU_rkbulgqaqbDtoeR8fNnIh5ntTduOcjGc-rfp-lrWDK0HhrPO4eW1Vsj4KA4XX3yV6WRBixrjGj_szF7osI8jZXn35qK8tqPl1p4em6IG1405c-w6teZSOIcPoHLxVOFGLWUhIDicNqV9HQJlM4PhGPoXzsoNwXQ2mn_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت رسمی بلیت پروازهای اربعین اعلام شد
🔹
سازمان هواپیمایی: قیمت بلیت یک‌طرفه از تهران و استان‌های غربی به مقصد نجف یا بغداد ۱۲ میلیون تومان و از مشهد و استان‌های شرقی ۱۴ میلیون تومان تعیین شده است.
🔸
نرخ رفت‌وبرگشت از تهران و استان‌های غربی ۲۴ میلیون تومان و از مشهد و استان‌های شرقی ۲۸ میلیون تومان خواهد بود.
🔸
این نرخ‌ها برای بازۀ زمانی ۳۱ تیر تا ۱۶ مرداد اعمال می‌شود و برای بزرگسالان و کودکان یکسان است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/451116" target="_blank">📅 16:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451115">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🎥
بازگشایی یکی از تونل‌های آسیب‌دیده محور بندرعباس-سیرجان
🔹
مدیرکل راه و شهرسازی هرمزگان: یکی از دو تونل گلوگاه شهید میرزایی در جادۀ بندرعباس-سیرجان بازگشایی شد.
🔹
تردد خودروها از ساعتی پیش در این تونل آغاز شده و عملیات تخلیۀ ترافیک این مسیر درحال انجام است.…</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/451115" target="_blank">📅 16:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451113">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkJCMHGHe_JORsQE29u9mBKFbR_l_TAt0Mk-ktLGvzaEI5T2MKjobz5a7DqSdBzr27QeUm_L3EFRyeyBTCR-B_z_Igrcm4rHfK8heZSfQiCm-9-WjFRg_86LfWt1nrBCrd9jrcWHeTOB7QglgSGUSAWj22QVVD5UvLWFvltd8GH8k7Rm2fcpmx41_V2v436oaHJ-vvvFXVFqzdf3p0gys6jjfDhuiH-0sNjjKP-KUSmN8SCtCqmiJzVloU42xPhcQ-cOMzGjFj4-xXlgpXSxccpWGLc4M59QyJEOIHsDj1_tUCbjltTXet6qG-ZjEncUta5OxI7or58Xs4elT5PdPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ مدیرعامل خبرگزاری قوه‌قضائیه: هیچ زندانی آمریکایی با مشخصاتی که ترامپ گفته از زندان‌های ایران آزاد نشده است
🔹
خانمی که مورد بحث است نه زندانی بوده و نه اتهام جاسوسی داشته است. ترامپ در شرایط فلاکت‌باری قرار گرفته که نیاز دارد از هرچیزی دستاورد بسازد. حتی…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/451113" target="_blank">📅 16:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451112">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0NfEfxh2ZeFaojKhT6k5pNR0yhmMiJ8Ljc2byhUJcK5A2W_SoiGSK7psZfVcsfuUv8RGkqVNcue4bCUfmMXVGu16dMvSi0s5rLBJi-Q9ov7Cp3m7pgOZLZYONN1dMWimoN2PfQvbI0t_8Q1KCePao7uhfKJMBTJvNdZGZd7zn0MteQYepfWz4FWdmyC11_lcjuyOScSRbaTD-KcEEEhNz_dqedkGgGjCQ2o0XSKjX1gnDaUNk0SBk5hDmMJxi0fzbqwU3HTpJ7bnofzEhpae4CSFkjVK3I8WJsX4VpT-EadbsdCj8Yhnbl20zLTp1kz9-9p1XeDD5Zu4L_dg22peQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار جوانی: عاملان شهادت رهبر شهید آرامش را به گور خواهند برد
🔹
معاون سیاسی سپاه: خون‌خواهی امام شهید امروز بعد جهانی دارد. بر همین مبنا نیز رهبری در موضوع گرفتن انتقام و انجام قصاص اشاره فرمودند که مشخص است چه کسانی در این جنایت نقش داشتند و این افراد باید با خواب آرام و آسایش خداحافظی کنند.
🔹
این تکلیفی است که بر عهدۀ همگان وجود دارد. شیوه‌ها و روش‌های آن نیز به شکل‌های مختلف از سوی آزادی‌خواهان، جبهۀ مقاومت و ملت‌های آزاده دنبال خواهد شد.
🔹
طی روزهای گذشته، نیروهای مسلح مراکز آمریکایی‌ها را در کشورهای منطقه با قوت و قدرت مورد تهاجم قرار دادند و ضربه‌های محکمی به پایگاه‌های آمریکایی در اردن، کویت، عمان و دیگر کشورها وارد کردند و این جدیت ادامه خواهد داشت.
🔹
آمریکایی‌ها تلاش می‌کنند شکست خود را در این جنگ به نوعی از طریق اقدامات نظامی جبران کنند و تنگۀ هرمز را به شرایط پیش از جنگ بازگردانند، اما قطعاً موفق نخواهند شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/451112" target="_blank">📅 16:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451111">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7e62084b5.mp4?token=B-6a5D9IvS8J5OSl6g_hh5odwcyn8elOjHhnHRMR6fsQ5AR8hXK4vdeq3apzyrGKuhDOYwivMrAo3yAKIEjDCPTcPf7e0H4jmLZ0j1IvKBEfW9dfRYqn_ux9EdcmA-7NA5QLLOI1wHt4TyA0kSnpkLaSd3yRXT1maN4J7Y-gQqm8sqN1VDoIv_yeGkwx_BPEHA9rRMDtwOuOICk3vreOr_eAGdSE9rMms4dNzI7fILhNXGtbrUeYMGDxgniaIeiw-FbRS_jxiN_XRVNtbs87fCVPukw0V3rUudu0N1sMEoe9dQkBGxQVj-dvaegwTTYPAEmN-g0XgIHYhDzuZRdh-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7e62084b5.mp4?token=B-6a5D9IvS8J5OSl6g_hh5odwcyn8elOjHhnHRMR6fsQ5AR8hXK4vdeq3apzyrGKuhDOYwivMrAo3yAKIEjDCPTcPf7e0H4jmLZ0j1IvKBEfW9dfRYqn_ux9EdcmA-7NA5QLLOI1wHt4TyA0kSnpkLaSd3yRXT1maN4J7Y-gQqm8sqN1VDoIv_yeGkwx_BPEHA9rRMDtwOuOICk3vreOr_eAGdSE9rMms4dNzI7fILhNXGtbrUeYMGDxgniaIeiw-FbRS_jxiN_XRVNtbs87fCVPukw0V3rUudu0N1sMEoe9dQkBGxQVj-dvaegwTTYPAEmN-g0XgIHYhDzuZRdh-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: اگر یک عضو از خانواده جرم کرد باید طوری به آن رسیدگی کنیم که کمترین آسیب به اعضای دیگر خانواده وارد شود.
🔹
وقتی پدر خانواده لغزش می‌کند، فرزندان او چه گناهی کرده‌اند؟! چرا با چشم دیگری به فرزندان خانواده نگاه می‌شود و آن‌ها را جایی استخدام نمی‌کنند؟…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/451111" target="_blank">📅 15:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451110">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‌
🔴
کانال ۱۲ رژیم صهیونیستی: شنیده‌شدن صدای چند انفجار در ایلات گزارش شده است.  @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/451110" target="_blank">📅 15:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451109">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‌
🔴
ارتش صهیونیستی: ما شلیک چندین موشک از ایران به‌سمت شهر عقبه را شناسایی کردیم و برخی از آن‌ها ممکن است در اسرائیل سقوط کنند.  @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/451109" target="_blank">📅 15:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451108">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
آژیرهای خطر در پایتخت و مناطق مختلف اردن به صدا در آمد.  @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/451108" target="_blank">📅 15:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451107">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/038807f0ea.mp4?token=AbImwAfttYKE7cgjV3zsPo97nkIlRMgDaFUMj3vCyepKCI6Z0uMVsY7xJRRTbZdOr5rR_ZPIwe8HiBPfAnWjx5Ia0MfVhmUZOc50XuvyB5RmLyK39U9wO8CHcUOmUZ3bZiV0wpFOJGgBECQrqOj-G_iCjrvoS8Fkj9ijjlCLLllcyPwuohtum-Wl9eWL4s6HON2YGYGr7MzeL4ATMoqH1kbR5orV3LSmn9D5_LicX-DeLjGoAb9zh9iQiV_so0V9aV6cnMypCUyj_EWuI-HuF3_N5ERXWKikBjyTyW7ha1QsqN4bmi_T5dzFgDSy3Ln1uLsEGvY02_Xqz2QQazaOnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/038807f0ea.mp4?token=AbImwAfttYKE7cgjV3zsPo97nkIlRMgDaFUMj3vCyepKCI6Z0uMVsY7xJRRTbZdOr5rR_ZPIwe8HiBPfAnWjx5Ia0MfVhmUZOc50XuvyB5RmLyK39U9wO8CHcUOmUZ3bZiV0wpFOJGgBECQrqOj-G_iCjrvoS8Fkj9ijjlCLLllcyPwuohtum-Wl9eWL4s6HON2YGYGr7MzeL4ATMoqH1kbR5orV3LSmn9D5_LicX-DeLjGoAb9zh9iQiV_so0V9aV6cnMypCUyj_EWuI-HuF3_N5ERXWKikBjyTyW7ha1QsqN4bmi_T5dzFgDSy3Ln1uLsEGvY02_Xqz2QQazaOnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: چه ضرورتی دارد که ما موبایل یا کامپیوتر متهم را بگیریم و تمام اطلاعات آن را ببینیم یا ثبت کنیم؟!
🔹
افشانکردن و واردنشدن به مسائل خصوصی افراد باعث حفظ حرمت افراد می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/451107" target="_blank">📅 15:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451106">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اداره‌های استان فارس دورکار شدند
🔹
استانداری فارس: با توجه به پیش‌بینی افزایش بی‌سابقه دما، تمامی ادارات و دستگاه‌های اجرایی استان فردا به صورت دورکاری فعالیت‌ خواهند داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/451106" target="_blank">📅 15:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451105">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7aPSW-S7mypuvxfpogCZzp7H55SkytaAQhTlq7-PNqwM3dIZ7MSU-9kZR6DVNLCazch_Xjg1k6ctA5qIb6VMaiMGuW4RfZfRvlG28YfsDqRGdZQURNjMECaVDWjdGkdR7XEXnTBiwFF6IV3-bbcMti6Dfjxk92pIpjva7exdFi_B4BNt8-WfpZMLL0cohMX-jwe3bOopWVf6rhHnU7tqeszCg999uRDHyjSTpTiaWf9CRjW11dPGqxedhTxHLudRc7ZSRwV6cmcPKAL_zjEfVJwdO6Sbll5bBvloDlpliBBxrZ3oaPDZlwp6h4Il4B9VSBYaxSJVP12D7s2sX7juQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایران باید به لایحه تحریم‌های روسیه اضافه شود
🔹
رئیس‌جمهور آمریکا در پیامی در شبکه اجتماعی «تروث سوشال» خواستار افزودن ایران به لایحه تحریم‌های روسیه شد.
🔹
دونالد ترامپ نوشت: «جمهوری‌خواهان باید ایران را به لایحه تحریم‌های روسیه اضافه کنند. این همان کاری بود که لیندسی گراهام می‌خواست انجام دهد و قرار بود عملی شود. مهم!!!»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/451105" target="_blank">📅 15:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451104">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/597f524daf.mp4?token=q-9ULy1tDo_RS59vLKMEAZWKPAQziopBsfoIdZ05nmYk1tG1mXBnlYhtf9vRrXdulV0mq1VaoWm6OuV5toQjdnudTzbicDBWoCnK3jPWyTJPmmd2UFhoS9zs4r9WnqKOeIUptYwhaUgVx9Vf33RBa9h5PcOUgbpjGTiHfBR92PBWbwnB5tEERBHfCSA8fT20LA81bnHrTPm1wWERm3lKN58hrwqOa2YjwHAgSBX9nfhlQnirlEllGHJKXSZFsXysh8M3r4AQ87mMoMECa8Dgq0Mosxj7I4eq9bfWAVxaM80AKu5DGuVr1ZIIa7IkosBrF0zyvwcAYsAR7xMw6o_sUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/597f524daf.mp4?token=q-9ULy1tDo_RS59vLKMEAZWKPAQziopBsfoIdZ05nmYk1tG1mXBnlYhtf9vRrXdulV0mq1VaoWm6OuV5toQjdnudTzbicDBWoCnK3jPWyTJPmmd2UFhoS9zs4r9WnqKOeIUptYwhaUgVx9Vf33RBa9h5PcOUgbpjGTiHfBR92PBWbwnB5tEERBHfCSA8fT20LA81bnHrTPm1wWERm3lKN58hrwqOa2YjwHAgSBX9nfhlQnirlEllGHJKXSZFsXysh8M3r4AQ87mMoMECa8Dgq0Mosxj7I4eq9bfWAVxaM80AKu5DGuVr1ZIIa7IkosBrF0zyvwcAYsAR7xMw6o_sUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: چه ضرورتی دارد که ما موبایل یا کامپیوتر متهم را بگیریم و تمام اطلاعات آن را ببینیم یا ثبت کنیم؟!
🔹
افشانکردن و واردنشدن به مسائل خصوصی افراد باعث حفظ حرمت افراد می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/451104" target="_blank">📅 15:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451103">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d2e116197.mp4?token=HvtS87KN-LmJD705mBlxKJnbnfGp5ME7hP_EtTABMfiGpJjqMMD9OgCXgMWIIaTR1H7B-ZwbS7_fK8ai7q_gjUCQWYTvE3m-g-NNQkxRfDUYileP1ad4vxWxDw79L4zBCId-jSKftBYMzR7gcJvKyLq1RHnzoHy9Uv_iCxmy0wR7bq9xuPO5E1Ohs6Foyk7uuhopai0rNNDB0haeJKNvhzAn2lCINUkjYbY9cCA1CRGXkz8BQyRz_EPd-AVPwne2qDbggAraGHICg60OqHQEWCcmzB3UppFRugUrFZnn1Z5fm5HZPejnNcs-mMj5_tNlPO3dUBEk9OUG-4MxEByNVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d2e116197.mp4?token=HvtS87KN-LmJD705mBlxKJnbnfGp5ME7hP_EtTABMfiGpJjqMMD9OgCXgMWIIaTR1H7B-ZwbS7_fK8ai7q_gjUCQWYTvE3m-g-NNQkxRfDUYileP1ad4vxWxDw79L4zBCId-jSKftBYMzR7gcJvKyLq1RHnzoHy9Uv_iCxmy0wR7bq9xuPO5E1Ohs6Foyk7uuhopai0rNNDB0haeJKNvhzAn2lCINUkjYbY9cCA1CRGXkz8BQyRz_EPd-AVPwne2qDbggAraGHICg60OqHQEWCcmzB3UppFRugUrFZnn1Z5fm5HZPejnNcs-mMj5_tNlPO3dUBEk9OUG-4MxEByNVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
آژیرهای خطر در پایتخت و مناطق مختلف اردن به صدا در آمد
.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/451103" target="_blank">📅 15:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451102">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24a0ea3252.mp4?token=tIS1U7g-mprjwh7o8yRPNUIDd-CuvqTKpu2J4t4uVfP6po1VFgvcILkg_3DRRd85cAIfoRsJfvJdhJbLPx9jw_7IBgAkqlU8JpUlWaFbhTQZOz1GQVSPPlrteSuOZY3NWwpWbqDZlgVaspMN9iISr1LjwzhC9mfX0DGMQXa4hfgn6ie_-PZEEpF5Hp1FBNcA1QqkGKZGkjOoJJr7OQRMojEU4Vz_NYsZU5ub3E_nehx_RFZ-zfToDV8euu_ELyRxmD40cMIEvg1ooWoNV0gSNWaF3kjsx8RLXoaVDr0D7t_N24epPFK_yeR_CvXJsK-c_fW9dhQNKO9V6cAxjuoZng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24a0ea3252.mp4?token=tIS1U7g-mprjwh7o8yRPNUIDd-CuvqTKpu2J4t4uVfP6po1VFgvcILkg_3DRRd85cAIfoRsJfvJdhJbLPx9jw_7IBgAkqlU8JpUlWaFbhTQZOz1GQVSPPlrteSuOZY3NWwpWbqDZlgVaspMN9iISr1LjwzhC9mfX0DGMQXa4hfgn6ie_-PZEEpF5Hp1FBNcA1QqkGKZGkjOoJJr7OQRMojEU4Vz_NYsZU5ub3E_nehx_RFZ-zfToDV8euu_ELyRxmD40cMIEvg1ooWoNV0gSNWaF3kjsx8RLXoaVDr0D7t_N24epPFK_yeR_CvXJsK-c_fW9dhQNKO9V6cAxjuoZng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امیر قلعه‌نویی: برخی افراد در دوران جنگ برنامه‌های خود را تعطیل کردند، به غار رفتند و حالا در جام جهانی دوباره پیدایشان شده
🔹
سؤال من از مسئولان این است که چرا به چنین افرادی تریبون داده شد تا علیه تیم ملی صحبت کنند؟
🔹
می‌گویند مردم تیم ملی را دوست نداشتند،…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/451102" target="_blank">📅 15:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451101">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0X9mCbqWXhvtVpONU-YbJv-7xUUPQjgDj43fio-FweV5jZ7rOnJi03KsOqn78Wz1i8tLX0_dqMaO4hCFkDpt2bKt2yTDw5wK-LNLGiOK4VogExuKZC_iYLTsPPwaRE022FhH-VRxPu51hvp7ptnsaqukjpREYdpb2dWeISu0C8ArX5IrpG-RYl-SR5uhih8jWiQh49pXK4GHMMThwqutI40HRzv_CeWK6LgGh-8AB2b7mSmSB7IJM2iEmN1lidYjPoLZ2ltkrrN65JXm4CnGRrgiEDjRivM2exVB4L5WgFihxQabvJ4C8Wu6pJVhHLwp65fxdfnjm4MUcucy1vdZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
منبع مطلع: تا زمان ادامهٔ شرارت‌های آمریکا تنگهٔ هرمز مسدود خواهد ماند
🔹
یک منبع مطلع در نیروی دریایی سپاه در گفت‌وگو با فارس: درحال‌حاضر هیچ ترددی از تنگهٔ هرمز انجام نمی‌شود؛ هرگونه تلاش برای عبور از تنگهٔ هرمز، به‌ویژه از سوی شناورهای متخلف، با برخورد نیروهای مسلح ایران مواجه خواهد شد.
🔹
تا زمان ادامهٔ اقدامات خصمانه و شرارت‌های آمریکا، تنگهٔ هرمز همچنان مسدود است و هیچ‌گونه مجوزی برای تردد شناورها صادر نخواهد شد.
🔹
در روزهای گذشته برخی شناورها که قصد داشتند با حمایت ارتش آمریکا از این مسیر عبور کنند، با واکنش نیروهای مسلح جمهوری اسلامی ایران روبه‌رو شده‌اند.
🔹
در شرایط کنونی، تردد در تنگهٔ هرمز به صفر رسیده و این مسیر تا زمان تداوم اقدامات خصمانهٔ آمریکا مسدود خواهد ماند و هیچ مجوزی برای عبور شناورها صادر نخواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/451101" target="_blank">📅 15:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451100">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c0f6f3e05.mp4?token=l0PNuoxjspHwn2-SNzAO6lwxqyBSk0Th9grC77PK1NWl_w5givEs1kGm0Dm5Ib39ytGd5cKzfDOSPvkhb0iQgxpCwq_MrxlSUXwIsKz2LIBrUdVYPYci6JPqgDmcIBmSN8cpPkuCBNWm_YayaNxMNmQEetpyPfPuDmxB4eU0WJ76BfpsYgQT-9b1G7IlTmZ5LAp5DNE9AdfVNk-3MlA8R3QRBnwGAabcKfHGPQHAQmRNlaq81OyYvYcjZVC-SuSDMXUD25M65BVQhXuKinGdyDX6g4eg08VBy6eIj76nAjCF4HVNJHxolaTS3cbyPLo3oSk6OKPWozsx8tTLEg_I4jGlmAqtJS-nfiCrisQKSpi3fD_ZJiDcTOj2CNbezGCaC-N2c4YBn9u15oO-DOujkhzXOSx9uUYSGyTy0nrtl3jouhyfF4XssXIxVdtCiD8N0SteBNJjPScKhFtqunl9ADGaHXDtwlPpe0dbP03fG_KlDc8iD0M89BzriKb7BOCrFonmjpfzD4e-Enh04J7PKxMgbbIIKsLbwb5T1ECSsYWc0z2gF816Z3vLiIHTBAQMSnDliF8i51vQr7kQR3PnoWp84g_Yie9nynMt4LsTza-NK3jQDdSDaMG859FFG-8R2PHLBXsbV_NHqagahLExOAwZ4EukCcxjXzDTswlAqsI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c0f6f3e05.mp4?token=l0PNuoxjspHwn2-SNzAO6lwxqyBSk0Th9grC77PK1NWl_w5givEs1kGm0Dm5Ib39ytGd5cKzfDOSPvkhb0iQgxpCwq_MrxlSUXwIsKz2LIBrUdVYPYci6JPqgDmcIBmSN8cpPkuCBNWm_YayaNxMNmQEetpyPfPuDmxB4eU0WJ76BfpsYgQT-9b1G7IlTmZ5LAp5DNE9AdfVNk-3MlA8R3QRBnwGAabcKfHGPQHAQmRNlaq81OyYvYcjZVC-SuSDMXUD25M65BVQhXuKinGdyDX6g4eg08VBy6eIj76nAjCF4HVNJHxolaTS3cbyPLo3oSk6OKPWozsx8tTLEg_I4jGlmAqtJS-nfiCrisQKSpi3fD_ZJiDcTOj2CNbezGCaC-N2c4YBn9u15oO-DOujkhzXOSx9uUYSGyTy0nrtl3jouhyfF4XssXIxVdtCiD8N0SteBNJjPScKhFtqunl9ADGaHXDtwlPpe0dbP03fG_KlDc8iD0M89BzriKb7BOCrFonmjpfzD4e-Enh04J7PKxMgbbIIKsLbwb5T1ECSsYWc0z2gF816Z3vLiIHTBAQMSnDliF8i51vQr7kQR3PnoWp84g_Yie9nynMt4LsTza-NK3jQDdSDaMG859FFG-8R2PHLBXsbV_NHqagahLExOAwZ4EukCcxjXzDTswlAqsI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امیر قلعه‌نویی: برخی افراد در دوران جنگ برنامه‌های خود را تعطیل کردند، به غار رفتند و حالا در جام جهانی دوباره پیدایشان شده
🔹
سؤال من از مسئولان این است که چرا به چنین افرادی تریبون داده شد تا علیه تیم ملی صحبت کنند؟
🔹
می‌گویند مردم تیم ملی را دوست نداشتند، اما سؤال من این است اگر دوست نداشتند، پس چگونه در زمان برگزاری بازی‌های ما رستوران‌ها و سینماها مملو از جمعیت می‌شد و دیدارهای تیم ملی جزو پربیننده‌ترین مسابقات بود؟
🔹
در سال ۲۰۰۶ در جام ملت‌های آسیا در ضربات پنالتی حذف شدیم ما را دادگاهی کردند بعد آدم‌های همین آقایان آمدند در پنالتی در همان مرحله حذف شدند و قهرمان ملی شدند.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/451100" target="_blank">📅 15:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451099">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🎥
تصاویری که گفته می‌شود مربوط به شلیک موشک‌های بالستیک اتکمز توسط نیروهای آمریکایی از کویت به‌سمت ایران است.  @Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/451099" target="_blank">📅 15:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451098">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">قوه‌قضائیه: هیچ زندانی آمریکایی از زندان‌های ایران آزاد یا تبادل نشده است
🔹
بامداد امروز دونالد ترامپ در مطلبی از آزادی یک زندانی آمریکایی که به گفته او در زمان دولت بایدن و در سال ۲۰۲۴ بازداشت شده بود خبر داد.
🔹
ترامپ در حالی این ادعا را مطرح کرده است که…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/451098" target="_blank">📅 15:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451096">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABcccIQEMBCR0US8VkNrfFU8j3uyOUOYpGSaimRbMXar8qj_nSzLeZcvRSDilZDT-w8KZ-yiZLIeiO6doRR2eOHcAYnXmg9jhV4-3ppljQAFYk9W7JJbdeX-wAaxuD_yeXrX8-2CEBXYNJPaHeODoJuc1PQJ6kS2tE6Mph-Eia_wFsOvsk6O6DiXSELrpMiZjdxPXeaOYtSngZI3l0yTJlEMcBk_KkFUZarL5EVzz7BQ7T9H7m5cEXBY9oe2xQg8HjTd-QsYps4siLUkqOpGFLEdWJoTOIHFBYhIKQVpT-gCHwqnqdD8mgQOKgr67g8fTMYFLeCBepRChj3otWFRBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حملات موشکی شدید روسیه به کی‌یف
🔹
مقامات اوکراینی اعلام کردند که روسیه بامداد امروز «یکی از بزرگترین حملات موشکی بالستیک خود را» به پایتخت اوکراین انجام داده است.
🔹
طبق این اعلام، پایتخت اوکراین با حدود ۴۰ موشک بالستیک «اسکندر» و هایپرسونیک «زیرکان» هدف…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/451096" target="_blank">📅 14:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451095">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20d32dd0ca.mp4?token=JQld0p5HeqmsKkmPaDZh72MMbZFlb1lm7Ue9md-y9E6lbVweR-FUs_kI90BCpAoLBZFiihBotAGyRTUBSPPzr2c1cw-nK5yci6-GyNQPMcvpu6f5wTyViknftqifLlBGgh_zinHj1251tA1vQgFLxvgPkiONsCZa2k_XqQSZdo2BcboxJmg0RfZI2nV6luYgWxYksZUWEVdRXEQ6sP57a3KfEzH5mOQjgnbLJd3i4xkLRGysCcIXX7QwSzIAIy_su8MswJ0ofqiEicNM1hIJJ9zYajM81pV6BMLbYLbLFX2jKtCPWAwLc6edENyIo9qwW3vV5Np7qGNmhThYM84CFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20d32dd0ca.mp4?token=JQld0p5HeqmsKkmPaDZh72MMbZFlb1lm7Ue9md-y9E6lbVweR-FUs_kI90BCpAoLBZFiihBotAGyRTUBSPPzr2c1cw-nK5yci6-GyNQPMcvpu6f5wTyViknftqifLlBGgh_zinHj1251tA1vQgFLxvgPkiONsCZa2k_XqQSZdo2BcboxJmg0RfZI2nV6luYgWxYksZUWEVdRXEQ6sP57a3KfEzH5mOQjgnbLJd3i4xkLRGysCcIXX7QwSzIAIy_su8MswJ0ofqiEicNM1hIJJ9zYajM81pV6BMLbYLbLFX2jKtCPWAwLc6edENyIo9qwW3vV5Np7qGNmhThYM84CFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون اجرایی رئیس‌جمهور: به دستور آقای پزشکیان برای بررسی و ارزیابی آسیب‌های ناشی از جنگ به استان‌های جنوبی کشور آمده‌ایم.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/451095" target="_blank">📅 14:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451094">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e729cb684d.mp4?token=ZJhGsEkZRoLvxBGzsbAw0BJyvSC0P5PqXM7OYIivpoUFPu372kvn65hIetgw7Au0p2d9_lAK-Uza3URqC0vpAQQ4BeYHCF2MfqPLAH2rD30ihp9jhjEfwcXbd4MRuU4iWq7jLo9He4baZSbQmncP9pCxPstiTau2urE8Wr99XMOURN-hjtlAKSUHJGhOu1Vp0QgzB6E4SC3nUI37dedHL59PdJ7UjdM7tJza6yrqU44uj0WNx1HEgpNq7yLUudwA1hfsyuzyl4hbiLG9VYWYt0R_LnqQpoPQ9bUTNGePkjsDgbolT-Hdwz0NYVzFO3CT9lI-TxSguZjx7GTbSD6lsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e729cb684d.mp4?token=ZJhGsEkZRoLvxBGzsbAw0BJyvSC0P5PqXM7OYIivpoUFPu372kvn65hIetgw7Au0p2d9_lAK-Uza3URqC0vpAQQ4BeYHCF2MfqPLAH2rD30ihp9jhjEfwcXbd4MRuU4iWq7jLo9He4baZSbQmncP9pCxPstiTau2urE8Wr99XMOURN-hjtlAKSUHJGhOu1Vp0QgzB6E4SC3nUI37dedHL59PdJ7UjdM7tJza6yrqU44uj0WNx1HEgpNq7yLUudwA1hfsyuzyl4hbiLG9VYWYt0R_LnqQpoPQ9bUTNGePkjsDgbolT-Hdwz0NYVzFO3CT9lI-TxSguZjx7GTbSD6lsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آب‌رسانی سیار به ۲۵ روستای شرق هرمزگان درحال انجام است
🔹
۱۰ هزار نفر از ساکنان روستاهای سیریک و جاسک از ۲ شب گذشته به‌خاطر حملۀ تروریستی ارتش آمریکا به ایستگاه پمپاژ آب از دسترسی به آب آشامیدنی محروم شده بودند.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/451094" target="_blank">📅 14:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451093">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5ad108936.mp4?token=bC2rXzkzZvz3U5X8VFA5XmqoX7s7KwfL8WrUm1LQdiDDYMNlNxeCoKz-6jn-1_7HUBOhHUX1GFtSFhtsS2BTjo0N_9Xr_xF0zNcsG9Lxq4COXwYC0xOlLF59rWH_7JLJK06bE9GrmzwFGbnRi6sB4KqzzqfVFeT041YOeuwSpVH0pzusdqosmwVKm2Dtx0g5sExLtA97cKXxQszgz_1-woJkhYmAQpv-V5D8G1n7grTD9ou5s7RkXO-obimjs1G-GdmRzHdzne_iJcFvTZIo6GQeMb4sK_j2HHPb-mGX7ovlxS0qOqlnhQDxiWaafvwx3HjT8_kl_wey6TdmRZ3QVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5ad108936.mp4?token=bC2rXzkzZvz3U5X8VFA5XmqoX7s7KwfL8WrUm1LQdiDDYMNlNxeCoKz-6jn-1_7HUBOhHUX1GFtSFhtsS2BTjo0N_9Xr_xF0zNcsG9Lxq4COXwYC0xOlLF59rWH_7JLJK06bE9GrmzwFGbnRi6sB4KqzzqfVFeT041YOeuwSpVH0pzusdqosmwVKm2Dtx0g5sExLtA97cKXxQszgz_1-woJkhYmAQpv-V5D8G1n7grTD9ou5s7RkXO-obimjs1G-GdmRzHdzne_iJcFvTZIo6GQeMb4sK_j2HHPb-mGX7ovlxS0qOqlnhQDxiWaafvwx3HjT8_kl_wey6TdmRZ3QVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نیروهای آمریکایی در پایگاه‌های کویت درحال جابه‌جایی‌های گسترده هستند
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/451093" target="_blank">📅 14:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451092">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQeOEIbYQCdJLqcuZnLOL3DLGwCrsmIo-3A3BpDJpdk2UgE7nTMmsxy4ts8HWFWlyPJRFN1sdaIaGYd-Mv6GdmZ5Ig1CiH9fap1y4NA4HYx96hGf6pRkvxH64QsSjBqrVnj9auQoNuTjmAIsl1O0CpaBUDrCb_Sa6bbrEa54GAJna67Qlvcl-UMiv6GRIOXAVbQmwk2k-KiuLt3Z1vOuVqqY4CT2lTT3HuGVTYB7naRS79sBxzpCsHWh1udxR9-IMtvRNCBIZGw8o5OuleQa6oloO41YBzYJ3imaLJmAIgcIFSV786K-EFZ1FbFQQq_rXG3ARklS23qgrcIEbQsyFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تامین‌اجتماعی: حقوق تیرماه بازنشستگان بدون تغییر از فردا واریز می‌شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/451092" target="_blank">📅 14:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451091">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدرگاه فرهنگ</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d950307861.mp4?token=apVuQ4HEO3ejNI-s-XOByYJiJH8OB1ig1BK-xQzX0YUxMqBBEhIxBFnNclpx1dfXIR8npeaokQ3j9ewn-yHDBLgAf4f7gEBM7jkWxrqZ9n2T4h30GacUvmSkn3rg0w50GSw_lhWhThQgTusHF3DJOnNKi9_FlOoTvUbttvHXCMacwY8nhokgRd-5CHlVTZQNa0w4Bvp9Wj25_guQxuW47MOKvW8Mz08V266o502ls8VoQsDNWoTFFrdQIul9t65MUwRz6RxPf1B_VnNcOlAPZF_6tl9SJep3VVZoIiuBG_7KKDeWS-22ShNzmTokLUHQBx_UcEHdzPvWmVMpQ74IYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d950307861.mp4?token=apVuQ4HEO3ejNI-s-XOByYJiJH8OB1ig1BK-xQzX0YUxMqBBEhIxBFnNclpx1dfXIR8npeaokQ3j9ewn-yHDBLgAf4f7gEBM7jkWxrqZ9n2T4h30GacUvmSkn3rg0w50GSw_lhWhThQgTusHF3DJOnNKi9_FlOoTvUbttvHXCMacwY8nhokgRd-5CHlVTZQNa0w4Bvp9Wj25_guQxuW47MOKvW8Mz08V266o502ls8VoQsDNWoTFFrdQIul9t65MUwRz6RxPf1B_VnNcOlAPZF_6tl9SJep3VVZoIiuBG_7KKDeWS-22ShNzmTokLUHQBx_UcEHdzPvWmVMpQ74IYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
#پوشش_زنده
|مدیرکل فرهنگی شهرداری تهران:میدان آزادی در این شب ها میدان خونخواهی از مستکبرین خواهد بود
مصطفی زیبایی نژاد در چهارمین نشست خبری سوگواره آیینی «محرم‌شهر»:
🔸
محرم شهر در میدان آزادی یکی از میدان هایی است که 139 شب هست در مقابل جنایات دشمن اجتماع دارند
@dargah_farhang</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/451091" target="_blank">📅 14:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451090">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس‌ پرس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6yfFCvf-qzxyJnve6t7aMah-KpUcZ6yI1IMzu8KQ5HqKGbmNg02wP9DYLuNG35x1F8KPEi2yXl03kqovR7d_aUlyFkbjLyuV5W5rIaGhZxxFpsxpcEeDgc3QuqzNyMzbLn51cGvDlxbhKlxfiWFNJxal7dvGIrk0_ZEvA5F1i8NEgUVcJnFJx6urI9HDavHZoSVNzSwTgJO4-czZZFRYlIcLAFdp-gHXe7ywYpCZOcDO6g-T743ZFYhfubrrf24-9sfARH0QusX0bOW-xtCSXRlGK_k42g-zIwSD2Tt8gjAm0lZ7avhz7sPRwszTYSniqaz12fVdVkHZzb3p_BWOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔰
پایش میدانی پروژه‌های راهبردی مس سونگون توسط مدیرعامل مس ایران/ تأکید بر شتاب‌بخشی به طرح‌های توسعه‌ای
🔻
مدیرعامل شرکت ملی صنایع مس ایران در سفر به مجتمع مس سونگون، با بازدید از پروژه‌های کلیدی توسعه‌ای و زیرساختی این مجتمع، آخرین وضعیت اجرای طرح‌ها را بررسی و بر رفع موانع اجرایی، تسریع در روند تکمیل پروژه‌ها و تحقق برنامه‌های توسعه‌ای شرکت تأکید کرد.
🔹
دکتر سیدمصطفی فیض در ادامه برنامه‌های پایش میدانی پروژه‌های راهبردی شرکت ملی صنایع مس ایران، از مهم‌ترین طرح‌های در حال اجرای مجتمع مس سونگون بازدید کرد و از نزدیک در جریان روند پیشرفت، چالش‌ها و اقدامات اجرایی این پروژه‌ها قرار گرفت.
🔹
مدیرعامل شرکت ملی صنایع مس ایران در این سفر، از پروژه تغلیظ فاز۳ سونگون، طرح‌های ذوب، پالایش، تولید اسید سولفوریک و اکسیژن، پروژه بازسازی واحد هیپ‌لیچینگ و تونل مکانیزه انحراف آب‌های سطحی سونگون بازدید و آخرین وضعیت اجرایی هر یک از این طرح‌ها را مورد بررسی قرار داد.
ادامه خبر در مس‌پرس:
https://mespress.ir/x6RL
@mespress_ir</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/451090" target="_blank">📅 14:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451089">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/451089" target="_blank">📅 14:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451088">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLzDOjCK9EH9ebM3V4WlCRfsrfIQlbtW7Q3XVoPMnCqlcJ14uaAaB5IeX7DybDZRqRBCBRuhra2DXwnuEvgWgVG5PS27aQQGkVZPyuJttKY-GJiza1Q6o0ueLmIxClgeE7ele8QLJtzw8uxqca_7TzfAhANXniE8h_aINcyvDpvG_7EQLe1RmJ9JkwCtMtGwFsgjegZue5tIgTKKtCKeFnDpYtrd3AkkF8REj59X6hVs5YxAQQ02Cs8NgRNg_fBrgpq_09dmd63KwgsZ0BcEblfdIT6xOP33H8NAz7Fg_x7rOgqTEBcnFq6BEx2O0-8V8zeYJaDCYZNV7qGvb_rwYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک مرکزی: فعلاً خبری از افزایش سود بانکی نیست
🔹
پیگیری خبرنگار فارس از بانک مرکزی نشان می‌دهد این بانک فعلاً قصدی برای افزایش نرخ سود سپرده و تسهیلات ندارد و هرگونه تصمیم در این زمینه به شرایط اقتصادی و نتایج بررسی‌های کارشناسی وابسته است.
🔸
بانک مرکزی پیش‌تر اعلام کرده بود همهٔ سناریوهای سیاستی دربارهٔ نرخ سود در کمیته‌های تخصصی درحال بررسی است.
🔹
این بانک گفت که زمان مشخصی برای پایان این بررسی‌ها تعیین نشده و این فرآیند ممکن است ۶ ماه یا حتی بیشتر طول بکشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/451088" target="_blank">📅 14:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451087">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">حملۀ آمریکا به سایت نیروگاه هسته‌ای دارخوین
خوزستان
🔹
سازمان انرژی اتمی: رژیم آمریکا بامداد امروز (یکشنبه ۲۸ تیر) حوالی ساعت ۳:۳۹، با شلیک چند پرتابه به سایت درحال ساخت نیروگاه دارخوین حمله کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/451087" target="_blank">📅 14:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451086">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v35f1SvMN-zZAPwix7MM6gal_thc0VXD0x3B848wajFGelu0DznsJBnxXaoQT2aTNox5aFcI6qKa5nKka5joj29_2qw6jtqU5XF8MN8FfFj8hdMKNsrmPyPIixzHSa7N8gAoqyNs5gW-dUhSDsm6Fx74ZZY-XlvQVLhWVrnd0Bo0za8__6lnGlvX3b2k8mwN9TW0TWK-JHU4IsRrThKzyvx6_bDHoLwWf5dgQ2n0uZBWp6Zvvy2-tztogUYMCqzwlqDB8RJUqlfjBu7tlqGddWgf5PsD6MporL2uQoeIF2NTNtHW672Zd0LPVUfd77j159vadGna4783W-5pVo30ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدال مسی و یامال سیاسی شد
🔹
دیدار فینال جام جهانی ۲۰۲۶ میان اسپانیا و آرژانتین، تنها یک رقابت فوتبالی نیست. رسانه‌های صهیونیستی این مسابقه به نمادی از شکاف سیاسی بر سر جنگ غزه و روابط با اسرائیل معرفی کردند؛ تا جایی که نشریه تایمز اسرائیل آن را «جنگ نیابتی سیاسی در زمین فوتبال» توصیف کرده‌اند.
🔹
در هفته‌های منتهی به فینال، دولت آرژانتین به رهبری خاویر میلی، صهیونیست که روابط بسیار نزدیکی با اسرائیل دارد و بنیامین نتانیاهو نیز رسماً اعلام کرد که در فینال از آرژانتین حمایت می‌کند.
🔹
در مقابل، دولت اسپانیا به رهبری پدرو سانچز طی ماه‌های اخیر از منتقدان اصلی سیاست‌های اسرائیل در جنگ غزه بوده و بارها خواستار افزایش فشارهای بین‌المللی بر تل‌آویو شده است. همین تقابل سیاسی باعث شد بسیاری از رسانه‌ها، فینال را فراتر از یک مسابقه ورزشی ارزیابی کنند.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/451086" target="_blank">📅 13:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451085">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🎥
دختر این افسر پلیس چند ساعت بعد از شهادتش به دنیا آمد
🔹
شهید محمد همتی چند ساعت پیش از تولد  تنها فرزندش، در شب ۱۸ دی‌ماه، در میدان علیخانی اصفهان به دست اغتشاشگران به شهادت رسید. @Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/451085" target="_blank">📅 13:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451084">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d813ddecf.mp4?token=U9ViRnkVv2IVhwr9sW6ek4bNIIwYYmJp2Cfo3Y-7Mokqr5BHhtH_a9wioyo40IfRlvvCjMvwHeCkuOQzmyeoEmAweUU51FqB66FCR7NQnQpc0WSD3PkufLv6jNHZ2ftVPyoVWdnekiAADBbJCPUHOcqdrasRm5Cvv6cKYz1OjnfUmvFD2eqnR14iBC5kyleAl6Dn1aCsghbksgcPf1b4CGHp4_vgIXg43Z7Tt3j_jbvUQfW3IncaO2IxLuERo3-vOB8LYnDTsKJANlICgoGL8czb2AhBSh2lIkyNf7hhgM_x2M73vtIuepGT6w3cO71BxifboICDZ5zKjiX_CkCC8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d813ddecf.mp4?token=U9ViRnkVv2IVhwr9sW6ek4bNIIwYYmJp2Cfo3Y-7Mokqr5BHhtH_a9wioyo40IfRlvvCjMvwHeCkuOQzmyeoEmAweUU51FqB66FCR7NQnQpc0WSD3PkufLv6jNHZ2ftVPyoVWdnekiAADBbJCPUHOcqdrasRm5Cvv6cKYz1OjnfUmvFD2eqnR14iBC5kyleAl6Dn1aCsghbksgcPf1b4CGHp4_vgIXg43Z7Tt3j_jbvUQfW3IncaO2IxLuERo3-vOB8LYnDTsKJANlICgoGL8czb2AhBSh2lIkyNf7hhgM_x2M73vtIuepGT6w3cO71BxifboICDZ5zKjiX_CkCC8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: آتش‌بس اولیه با آمریکا در جلسات کوچک‌تر از شورای‌عالی امنیت ملی پذیرفته شد
🔹
وظیفهٔ تحلیل وضعیت برای جنگ یا آتش‌بس با شورای‌عالی امنیت ملی و وظیفهٔ تصمیم‌گیری دربارهٔ آن با رهبری است. هرکدام از اعضا وظیفهٔ ارائهٔ تحلیل دربارهٔ بخش خودش را داشت. …</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/451084" target="_blank">📅 13:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451083">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1c6f5985e.mp4?token=K3DInE2isE1pzcGJwHmDzOU8b-pdgxRjGL9sFyRdE4Edq5k7WHSIJvgcgYCrObTi94ooFI3cZV2Rzdf3MLKz7xPIWNlc9A3mQse84NPiS5ISWtglMpPvO_FO2lJd3mOogXYe8FsLkV2_-hQA1Uikn0vFjefgFgHnzAU1t62fS682FvHqhWEA2B3qoyvqdNYu6VNPumBO2vsfX0_n1P1vKDqUNGkCus5IVi1Llin68kYhbbcJNclCPts5b0UaEDslK5gjha9MTTtb7wTW-1IGnfUnnq2POoaToSXPGZNTZ8yfj3diXryPvufvu0ZNJESMWFa0prZFPJEILwXekftdOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1c6f5985e.mp4?token=K3DInE2isE1pzcGJwHmDzOU8b-pdgxRjGL9sFyRdE4Edq5k7WHSIJvgcgYCrObTi94ooFI3cZV2Rzdf3MLKz7xPIWNlc9A3mQse84NPiS5ISWtglMpPvO_FO2lJd3mOogXYe8FsLkV2_-hQA1Uikn0vFjefgFgHnzAU1t62fS682FvHqhWEA2B3qoyvqdNYu6VNPumBO2vsfX0_n1P1vKDqUNGkCus5IVi1Llin68kYhbbcJNclCPts5b0UaEDslK5gjha9MTTtb7wTW-1IGnfUnnq2POoaToSXPGZNTZ8yfj3diXryPvufvu0ZNJESMWFa0prZFPJEILwXekftdOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک میدان نفتی در کویت دچار آتش‌سوزی گسترده شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/451083" target="_blank">📅 13:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451082">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Flo3Wdrx9CEKyW4Pz2fobBlGJd6FlJtK1D539gN79WqiDsEy_0WS65ahh7-oFDuasV4V8kFtMO5h2i8HIsgK7zdslkCfkgyv0SmLc9lhwbWucAEMvBhSsT9AyCz9KZeYLysr-0pfU5kJOsckt2dJcs-r1y_kx2gaDQRi3NOsNfEgRU_Tecy1TSzerOEEDNWSEctDRVXOHVUadAqd00hjaHjmyVxdXnVeu3pAV3Yhu67MBAT4V7Qvx1tkhq9g-y2LUXNnKRtEQax0StxxvwW7g0gjT7EKdlbOENueaYZxPbxKt_md6w7JSGKYOEKG8vW1k-SCquLXDc9gFV_nMjjtGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
رهبر معظم انقلاب: از اصولی‌ترین امور، اصرار بر اتحاد مقدّس در همه‌ی سطوح است؛ پرهیز از تفرقه و تنازع وظیفۀ همگانی است
🔹
لازم است به شما مردم باوفا و سرافراز ایران عرض شود که از جمله اصولی‌ترین امور در این برهه، اصرار بر وحدت کلمه و اتحاد مقدّس در همه‌ی…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/451082" target="_blank">📅 13:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451081">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aef42aff8c.mp4?token=mWd6NmHc_Pu4FafrmB-kGdhLPJRcFpKb8vy3wVnWsR_qSoa53xKWeysO1Wp34RoSXiGD8tJW0_oUypjFLjeozZ4v2n0Iy_5w-XQlr8JvU1hgzEirxxtIRcprVsrkMOOxrxz_0OuLsYjI6-rfjdWBFVI8fDYI9xxsyC6wzK-KhOklNlksfe729UT-Cs9QM4NqZiyRH_llrrACnAEXH8Qps0e5isOQmFssDTQOR1u1WJKdgXa_GHyb3LkVxYWK7thcLGlk6Xu8vUnbVSswOYYzDSRcc-A3LKhn8t2IYwyHLfkc7f-pbHfFqHH_3uEhyO3WxWkEneoc9zOdkCWU6ATTFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aef42aff8c.mp4?token=mWd6NmHc_Pu4FafrmB-kGdhLPJRcFpKb8vy3wVnWsR_qSoa53xKWeysO1Wp34RoSXiGD8tJW0_oUypjFLjeozZ4v2n0Iy_5w-XQlr8JvU1hgzEirxxtIRcprVsrkMOOxrxz_0OuLsYjI6-rfjdWBFVI8fDYI9xxsyC6wzK-KhOklNlksfe729UT-Cs9QM4NqZiyRH_llrrACnAEXH8Qps0e5isOQmFssDTQOR1u1WJKdgXa_GHyb3LkVxYWK7thcLGlk6Xu8vUnbVSswOYYzDSRcc-A3LKhn8t2IYwyHLfkc7f-pbHfFqHH_3uEhyO3WxWkEneoc9zOdkCWU6ATTFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: آتش‌بس اولیه با آمریکا در جلسات کوچک‌تر از شورای‌عالی امنیت ملی پذیرفته شد
🔹
وظیفهٔ تحلیل وضعیت برای جنگ یا آتش‌بس با شورای‌عالی امنیت ملی و وظیفهٔ تصمیم‌گیری دربارهٔ آن با رهبری است. هرکدام از اعضا وظیفهٔ ارائهٔ تحلیل دربارهٔ بخش خودش را داشت.
🔹
جلسهٔ شورای‌عالی امنیت ملی برای تصویب یادداشت تفاهم با آمریکا از ساعت ۹ شب تا ۳ صبح طول کشید. آتش‌بس اولیه در شرایطی پذیرفته شد که امکان تشکیل جلسهٔ شورای‌عالی امنیت ملی وجود نداشت و شرط آتش‌بس این بود که مبنای مذاکرات، ۱۰ بند پیشنهادی ایران باشد.
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/451081" target="_blank">📅 13:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451080">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">۲ کشتی متخلف در مسیر ناایمن تنگه هرمز دچار حادثه و ۲ کشتی دیگر از ادامه مسیر ناایمن منصرف شدند
🔹
نیروی دریایی سپاه: ساعاتی پیش ۴ فروند کشتی متخلف با شیطنت و حمایت تروریست‌های امریکایی و با خاموش نمودن سامانه‌های ناوبری و بی‌توجهی به اخطارهای پایگاه کنترل تنگه هرمز نیروی دریایی سپاه، قصد اخلال و خروج از تنگه هرمز را از مسیر ناامین داشتند که ۲ فروند از آنها دچار حادثه شده، در جای خود متوقف گردیدند و ۲ فروند دیگر از ادامه مسیر منصرف شدند.
🔹
نیروی دریایی سپاه اعلام می‌دارد که کنترل تنگه هرمز در اختیار کامل این نیرو است و تنها مسیر عبوری ایمن مسیر مشخص شده و اعلام شده است و یک قطره نفت و گاز و کود شیمیایی همانگونه که قبلا گفته شده، بدون هماهنگی و اجازه از تنگه هرمز عبور نخواهد کرد.
🔹
شناورهایی که تحت تاثیر صحبت‌های دشمن آمریکایی قرار می‌گیرند و وارد مسیر ناایمن می‌شوند مطمئنا دچار حادثه خواهند شد.
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/451080" target="_blank">📅 13:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451079">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e24b3ea8cb.mp4?token=TmMIQV9mWVT4lUdvi9Ab1nv7GDusCL4iKQp8OZnak1bp3VPC3bnbfzNCH6RvZ02uwU3Tk1lxlyNy5n5y79pmMKjOgRNRy39qz1UUqfP8bFHMPMd4dGr8t_ufqp33hsIc5fOw0cvRawXweUfPIcV5pYPww9jRSTsMfQCPvjYFqnxjYvN60PMzB5WuoiPc6UKaQef2f4t31l7tg9eh0WsJd55WuRLx-59Y3mLnuPiSiXA9K5tCMlfhwQiXFmIVxUdNa-wGY9YHXqPhldOrLmhtIoaNKeIEB9lA6FM3HUcbchPnjwMNlGTg1OPusGxCkdYKy_Mff43IiuUJJ0QmYTfdtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e24b3ea8cb.mp4?token=TmMIQV9mWVT4lUdvi9Ab1nv7GDusCL4iKQp8OZnak1bp3VPC3bnbfzNCH6RvZ02uwU3Tk1lxlyNy5n5y79pmMKjOgRNRy39qz1UUqfP8bFHMPMd4dGr8t_ufqp33hsIc5fOw0cvRawXweUfPIcV5pYPww9jRSTsMfQCPvjYFqnxjYvN60PMzB5WuoiPc6UKaQef2f4t31l7tg9eh0WsJd55WuRLx-59Y3mLnuPiSiXA9K5tCMlfhwQiXFmIVxUdNa-wGY9YHXqPhldOrLmhtIoaNKeIEB9lA6FM3HUcbchPnjwMNlGTg1OPusGxCkdYKy_Mff43IiuUJJ0QmYTfdtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خضریان، عضو کمیسیون امنیت ملی: کویت بداند وضعیتش در پایان این جنگ عادی نخواهد بود
🔹
حملات از کویت را حملات مستقیم تلقی می‌کنیم و بدانند که به‌صورت ویژه ادبشان خواهیم کرد. @Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/451079" target="_blank">📅 12:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451078">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2f58528b3.mp4?token=j-Q_0c8W5Bkg-v7xfpatYyVfO7MMiM21RF_rdjUV-ZmriQozShP1Pb_SaEAFX4lEjZmzsAGckBGGTjzYuVS-M7qw68L_VLklu_4LVA3Pc_gWJk-5sKlzjCX2EyUfsiAyrH2ZF5mWYPGz9UUDBNOSv8gnqxwUNHbVHnZL_oecpw7oUzi086vMiYwd_JD2HU_lbeRLU552N9NXppxV4tnbSOkgjj7Rf3_lLFGQG-tOm-y31un5j44PimDd8No3jHaj-PH5jOYv35bQUzDMCNwe-dDd2R8kiPWswK1fpICZe_bFZthnHOAwfJoJgPwgXgJFSb8CjE8EbywcNF9LY29CYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2f58528b3.mp4?token=j-Q_0c8W5Bkg-v7xfpatYyVfO7MMiM21RF_rdjUV-ZmriQozShP1Pb_SaEAFX4lEjZmzsAGckBGGTjzYuVS-M7qw68L_VLklu_4LVA3Pc_gWJk-5sKlzjCX2EyUfsiAyrH2ZF5mWYPGz9UUDBNOSv8gnqxwUNHbVHnZL_oecpw7oUzi086vMiYwd_JD2HU_lbeRLU552N9NXppxV4tnbSOkgjj7Rf3_lLFGQG-tOm-y31un5j44PimDd8No3jHaj-PH5jOYv35bQUzDMCNwe-dDd2R8kiPWswK1fpICZe_bFZthnHOAwfJoJgPwgXgJFSb8CjE8EbywcNF9LY29CYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خضریان، عضو کمیسیون امنیت ملی: پاسخ ما به حمله به آسایشگاه ارتش در چابهار برابر نبود؛ بلکه حداقل ۳ برابر بود
🔹
تلفات آمریکا در سوریه بیش از تلفات سربازان مظلوم ما در چابهار بود. @Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/451078" target="_blank">📅 12:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451077">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3595950301.mp4?token=t-szDELbs81mJwHLuX_9dZtNsZZUxCbcwGgRZZbDCBJHA1IH_Z4mGwNaHJf7wdJxMsYrUK_WT5NToArLSCRhmRw8bpbcLW4PRRvaJayziTwmw_2gqeYGzatsJlOEchcFE_NOfcmrQyeoxPFFwWzHrJjl9opyNhjBnKxVkk_EuI7rwNOcivRtIZljUyNvSL5_jTjAz1wtSYq_KF2Q4kLQP5GEVQld8qm2vaKYME7oANSAk_SeO8c0Qlvyp09XqL2l8meYyn6PPsX522QO8lM6cHPm8rSmBW7qcm5tIdz2s_ASPOwjjg_12X_zhkV6GoXfy3e6C6Evwy6vXAyfsljQUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3595950301.mp4?token=t-szDELbs81mJwHLuX_9dZtNsZZUxCbcwGgRZZbDCBJHA1IH_Z4mGwNaHJf7wdJxMsYrUK_WT5NToArLSCRhmRw8bpbcLW4PRRvaJayziTwmw_2gqeYGzatsJlOEchcFE_NOfcmrQyeoxPFFwWzHrJjl9opyNhjBnKxVkk_EuI7rwNOcivRtIZljUyNvSL5_jTjAz1wtSYq_KF2Q4kLQP5GEVQld8qm2vaKYME7oANSAk_SeO8c0Qlvyp09XqL2l8meYyn6PPsX522QO8lM6cHPm8rSmBW7qcm5tIdz2s_ASPOwjjg_12X_zhkV6GoXfy3e6C6Evwy6vXAyfsljQUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خضریان، عضو کمیسیون امنیت ملی: فلسفهٔ حضور ما در جنوب این است که به آمریکا بگوییم «ما آمده‌ایم که پدر شما را دربیاوریم»
🔹
حضور ما فقط برای دفاع نیست. طرح «پاسخ پشیمان‌کننده» درپی حمله به زیرساخت‌ها درحال نهایی‌شدن است. @Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/451077" target="_blank">📅 12:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451076">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7n1deLXgs-R9m_dTFq3mVFqo3BEJhO41DfTbRZxBZGgawYILHPFygWts60j3NWPkcFwnjoVrGSbvJQV97KNVlweXiATWAvGMUZe3EmNAdPZUn12ct_Voajp7zteCiluMVEMB27qT_XJMy0IXhvx4uYg4mun4vtqrtStguIeZaPRTYmSJSdbzue5qZGRN4_eencH3C9X4Hj8gLYGxcNj3L1iGItH39OQL1R7TVPE7mJvB9-ymzIa6QRDjl-l-0nsqWusFXv2znRjUf7pVLrBK5pnihk8-x2zKFGlo1afQ_y-t7R6qZ2QtEAuLidWd5vnfxDkKrdaskT5JtchcyEyGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با کاهش ۲۲ هزار واحدی به ۴ میلیون و ۷۵۵ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/451076" target="_blank">📅 12:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451075">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b7a1178d.mp4?token=eCkjRPWpNVeXdMZb0z2eC_d3iq_OQVdIMkm7Oay9rBd1MNfoeYMiUF4lMViH7zueKIwW242KZNWYW7VtXMGauaP-fTuYAL3LMXMLz0cCDSTFMhp9DI3fcBQ67ERtSfzyZPFiQVSe9lFUUCSSn7d4l9jzTbJZ5Ku3redfGkSucuPnx0u9JdjOvdyH2Xb4cIikIATSlY-AKHEOUrVa3BUL7jSeKsnTkOiMGTCch1GM3uUGItkESx5o48VxR6pvhP2Sq6oY8u3L6NSd8XYmp4m-L5jDsghG0UWHEbKpY5HNfuj-3RM4mVEy4qTF2GMVh0k-BIxUeGrG_Hv5SMOzboCxjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b7a1178d.mp4?token=eCkjRPWpNVeXdMZb0z2eC_d3iq_OQVdIMkm7Oay9rBd1MNfoeYMiUF4lMViH7zueKIwW242KZNWYW7VtXMGauaP-fTuYAL3LMXMLz0cCDSTFMhp9DI3fcBQ67ERtSfzyZPFiQVSe9lFUUCSSn7d4l9jzTbJZ5Ku3redfGkSucuPnx0u9JdjOvdyH2Xb4cIikIATSlY-AKHEOUrVa3BUL7jSeKsnTkOiMGTCch1GM3uUGItkESx5o48VxR6pvhP2Sq6oY8u3L6NSd8XYmp4m-L5jDsghG0UWHEbKpY5HNfuj-3RM4mVEy4qTF2GMVh0k-BIxUeGrG_Hv5SMOzboCxjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شریعتی، نمایندهٔ مجلس در مناطق مرزی جنوب: آبادان نماد جوانمردی و حصرشکنی است
🔹
پالایشگاه آبادان نماد حصرشکنی نسبت به تحریم است. آمریکا نتوانسته و نخواهد توانست این کشور را محاصره کند. @Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/451075" target="_blank">📅 12:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451074">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
وزارت کشور بحرین: آژیرهای خطر فعال شده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند.  @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/451074" target="_blank">📅 12:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451073">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9704386c34.mp4?token=tZJVR2N9UyPwH38zItcS_cTz-jaQZavFiv3tnR1HE3yWuMfYJU-cjYiWo3CKOEJTzfOouGIw3BooHDo8fP_eiNDLc8voAdLjQ2J3j-x5UCkeoxJ2bK8L-hm0XanpZTVHyUKB2bfX9mxAiASUeXCpo6oHflIlBl8W6PbSadmHwCm7dLXRAea4Rm5ZW3RuNAdwwl33h7VY7iHeGOr3cHXMprVL7IVpIsDldutNA3u16GXZ7aEmKumWuysVH1jTpbqSpOmHdIjqqLqpjTH1PnbsIkOAde94p1EQc1kMXMx7Ksci36d5LibjJn3LggyIDvIlL2Kq63K1e5trPUBrZHBLUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9704386c34.mp4?token=tZJVR2N9UyPwH38zItcS_cTz-jaQZavFiv3tnR1HE3yWuMfYJU-cjYiWo3CKOEJTzfOouGIw3BooHDo8fP_eiNDLc8voAdLjQ2J3j-x5UCkeoxJ2bK8L-hm0XanpZTVHyUKB2bfX9mxAiASUeXCpo6oHflIlBl8W6PbSadmHwCm7dLXRAea4Rm5ZW3RuNAdwwl33h7VY7iHeGOr3cHXMprVL7IVpIsDldutNA3u16GXZ7aEmKumWuysVH1jTpbqSpOmHdIjqqLqpjTH1PnbsIkOAde94p1EQc1kMXMx7Ksci36d5LibjJn3LggyIDvIlL2Kq63K1e5trPUBrZHBLUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاک، کارشناس جبههٔ مقاومت: وظیفهٔ ما حفظ جبههٔ مقاومت و پاسداری از خون حاج‌قاسم و شهید نصرالله است.  @Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/451073" target="_blank">📅 12:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451072">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50a85689b0.mp4?token=ChGRRTw19gZJYDz5wHXaPcH4XVIosWNU_8s8A-gXlhLO_jZ5E1c8ajG49-eZviKkfmFAdWygdbxBlDSeToljBhbDPgAmSlKZkizEaQVSyNAdaL1-54bw--i3AUO8CdRZIiRsS_xi_OPF-NPTdYqvFvFutGBJ3-KBkeYSSoP7Zqmr6lcx9fvIfGmfIC057XR6Y3u9CE3icDOF2eQy9aDb6BYgooPIHtDIBku6iqzR3OfdtMXDtEjATy8FvzuwBpdSW86L21T6Qo-2UUXiU1uyTL3AoJQYzjgMD82SUdhM9666F8qwqF4LVx97RCz5mNZqBOOY0bOCurcn5cJixAWCCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50a85689b0.mp4?token=ChGRRTw19gZJYDz5wHXaPcH4XVIosWNU_8s8A-gXlhLO_jZ5E1c8ajG49-eZviKkfmFAdWygdbxBlDSeToljBhbDPgAmSlKZkizEaQVSyNAdaL1-54bw--i3AUO8CdRZIiRsS_xi_OPF-NPTdYqvFvFutGBJ3-KBkeYSSoP7Zqmr6lcx9fvIfGmfIC057XR6Y3u9CE3icDOF2eQy9aDb6BYgooPIHtDIBku6iqzR3OfdtMXDtEjATy8FvzuwBpdSW86L21T6Qo-2UUXiU1uyTL3AoJQYzjgMD82SUdhM9666F8qwqF4LVx97RCz5mNZqBOOY0bOCurcn5cJixAWCCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خانعلی‌زاده، کارشناس مسائل بین‌الملل در مناطق مرزی جنوب کشور: آمریکا که قرار بود امنیت کشورهای عربی را برقرار کنند، امروز توانایی دفاع از پایگاه‌های خودش را هم ندارد.  @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/451072" target="_blank">📅 12:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451071">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59e2f40d35.mp4?token=g2T6R9B_1uEBM9x-DIh6vtkMJI-hWCMLxykpc9OkiPTVBQ_YvhzFN6L3EUf1O7mF-usdbJaVdLewRwO2uidPDV6HCsZzdGHgFqx1jgwHkPYsil1YOx5T9GoxPqdkgl81Yghzx-XMlWHLsqxLfPeWqrDYYCosT44E1vXgh3rT44CxUVPzz29wiGz7fedZWkrb_-AR097JaFogHztb8pIuAYdRfDJUHiPtYk0uw1oa92blTjh0XcdePOCuH5z7y3M5owjzv5FyN1gjJxpxU1R1qoKRilcvVVmyoQkx6RrYQLS66SemVe5Bgfcp6o53smwN4wvOHw6XRT914eYPWqUYMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59e2f40d35.mp4?token=g2T6R9B_1uEBM9x-DIh6vtkMJI-hWCMLxykpc9OkiPTVBQ_YvhzFN6L3EUf1O7mF-usdbJaVdLewRwO2uidPDV6HCsZzdGHgFqx1jgwHkPYsil1YOx5T9GoxPqdkgl81Yghzx-XMlWHLsqxLfPeWqrDYYCosT44E1vXgh3rT44CxUVPzz29wiGz7fedZWkrb_-AR097JaFogHztb8pIuAYdRfDJUHiPtYk0uw1oa92blTjh0XcdePOCuH5z7y3M5owjzv5FyN1gjJxpxU1R1qoKRilcvVVmyoQkx6RrYQLS66SemVe5Bgfcp6o53smwN4wvOHw6XRT914eYPWqUYMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حدادیان: رهبر امت به ما وعدهٔ پیروزی داده
🔹
مردم‌سالاری دینی در دورهٔ رهبر شهید به بالاترین حد خود رسید و کار را به ملت مبعوث شده سپردند. @Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/451071" target="_blank">📅 12:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451070">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767f04b69b.mp4?token=oH6hwtBuIiiGClSfEgrwJR9T9Sl3OstAYSlXX4BXjxafBbslyAP9f0yqyERmNSh2p9vlAeiX-1rHCKLicvYyUmMkXfcLa7mAhwfROEu7lJrsjHk9xQ6BjqR5MKjDCq7dB19hdu4bi318KaNrAbv4cNJPsVd9jnyRCPyvL5YCEf6Z6RpyMC25KxSQqqZNZePMxwsVYqW40Kr9T5ZNE9Vw_NbesLp7eVZVpmNrE7JIjdm_X5SjizwStvip-jbjaCNdaGecTl2UbJ3ZgQ1_O0EG1SQ0aGNBMKGc0s_wyjIW__bj7saX6a38f8L4UEh9rOmyimN0GTrPaiCAP1RZRZd8ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767f04b69b.mp4?token=oH6hwtBuIiiGClSfEgrwJR9T9Sl3OstAYSlXX4BXjxafBbslyAP9f0yqyERmNSh2p9vlAeiX-1rHCKLicvYyUmMkXfcLa7mAhwfROEu7lJrsjHk9xQ6BjqR5MKjDCq7dB19hdu4bi318KaNrAbv4cNJPsVd9jnyRCPyvL5YCEf6Z6RpyMC25KxSQqqZNZePMxwsVYqW40Kr9T5ZNE9Vw_NbesLp7eVZVpmNrE7JIjdm_X5SjizwStvip-jbjaCNdaGecTl2UbJ3ZgQ1_O0EG1SQ0aGNBMKGc0s_wyjIW__bj7saX6a38f8L4UEh9rOmyimN0GTrPaiCAP1RZRZd8ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دعوت حدادیان از سربازان آمریکایی: پایتان را به کشور ما بگذارید ببینید چه بلایی سرتان می‌آید
🔹
آنهایی که می‌گفتند «نه غزه نه لبنان» خوب بیایند جنوب ایران!  @Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/451070" target="_blank">📅 12:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451069">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkZ7aBkaLt7fv4Bwgg9JGRqpCPlu-XCJFIfVsUdXBtjTpc3PNr2Sw8N-3O6Ah_YX5i_vpb1Mu2ck2YPghU7WXiSL3NAT9ZOcme18NkYsWJC9QHcDJOEkN-G_O-lSSbb5Tsk5I0Mh7CsIfWVR-XubFUKhTy7IR4q6M3x3ld07kw9eW8CD1y8MTyjxE8_EsjbzkH0h173vstiNSxLSB_fiLYX6hFBlHAiC4m7NpD0nCqkJxQdRkVXZ8M1K9IMgaD3FKPLkCsmX2GiRRzer0ikSX1g5evLeN0_CsRmrXXie3K6UTET9ev38MLVQtvFeZWVyOwiBai_8Jom1HLc17-l_yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار فرمانده نیروی زمینی ارتش با خانوادۀ شهید موسوی
🔹
امیر جهانشاهی: اعتماد امام شهید امت در انتخاب شهید موسوی به ریاست ستاد کل نیروهای مسلح اعتماد به ارتش بود. امام شهید، شهید موسوی را یک فرمانده بزرگ می‌دانستند و در امور نظامی او را تحسین می‌کردند.
🔹
یکی از ویژگی‌های شهید موسوی استکبار‌ستیزی بود. در تمامی توصیه‌ها و سخنرانی‌های شهید موسوی نسبت به مقابله با استکبار تأکید شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/451069" target="_blank">📅 12:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451068">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZecLq3yddwsPMvCZkdB3Jmdb1yrp7DOYwdVzU365f_c3BlhKSOYjMBDBKWNqmzOw_icLF3Y9DeUuZypV1m1KP66uvXMa-auqF493XL_NNWntRJft43zIWcRdJhW15_NR8PPb6D6otcPSgu2GQruMTKDsXAp-IP2LeK6XpgeA5AoDtmxkwa-O2hPC3gUOmHw2e5SsTjRZa6M3kjb-8ptluhcF1JDeozMmKsSlDzvhGM9uIo5CcQHqfl-KmfJvhXNCjocRY2gYLPkF6XZiKDCmDBSFGs4xs_eW7wKmQT3dPIW7Sslizf5kz5U6tekmWV0Xb7XrSkADr3CKoqrvyFxXBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب آزادکاران ایران در بازی‌های آسیایی مشخص شد
🔹
۵۷ کیلوگرم: علی مومنی
🔹
۶۵ کیلوگرم: عباس ابراهیم‌زاده
🔹
۷۴ کیلوگرم: یونس امامی
🔹
۸۶ کیلوگرم: محمد نخودی
🔹
۹۷ کیلوگرم: امیرعلی آذرپیرا
🔹
۱۲۵ کیلوگرم: امیرحسین زارع
🔸
بازی‌های آسیایی ناگویا مهر امسال برگزار می‌شود.
عکس: رسول شجاعی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/451068" target="_blank">📅 12:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451067">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLkbY9SCGHilqFtACyS9U_RWcHQ_b95foj7tieRUtKH7kFgHenvJCKqX7Z-1Bqk7F79rtQuY893gqps6r-xeKhyZyZS64skZNH-vjVNEE2U9KP3h2qivIdJX1eEnHxDGkCD9DIKEONUK7B6spKZGmWclLBR0kSGMLl17nQQJkdmFfFoYjuXSYcNscy3Ao-aVTmRyX3TVJXRKutdclKORiOEN5ZksqFQosJ1TdIXImou1ISgmAYxuaMevFpK-iCVvq3oYo4YhN74v47xPw5Q0_EAkw0PoOE1SbU8yEphuxNuEhBS_SOd33LHNkBs9nGU4z4FcfuokPh1MesZQB0l5Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین برآوردها از میزان شرکت کنندگان در بزرگترین تشییع تاریخ جهان
🔹
مراسم وداع و تشییع پیکر رهبر شهید انقلاب، در یک بازه ۶ ‌روزه و در ۵ شهر تهران، قم، نجف، کربلا و مشهد برگزار شد که با حضور حماسی و کم‌نظیر مردم، به بزرگترین رویداد تشییعی در تاریخ جهان تبدیل…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/451067" target="_blank">📅 12:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451066">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e06a001e7d.mp4?token=uoIP5Gm2b6yqhlsXhkSToNtXcNNDnJ8HQAA3tzRwzNhynn_JbmRdPVjiQDSe2U9DwXG3_eUzLyNbmAuaqZ49ZhakHgZHrA9OjhVZml6avl5PMGi4z4oYZwAEKX9N-Q5-9RuL645kAaxjkAfnN_nh4Tngyzibg4FDrSh2zBr61MLl38kyR8Zaux5PWLtUPQ87VHUT4n9U-fjtzmrsom_MJ_7dsGlof3naOWl7ji1Gz-l0UfRqgQ3IDn24O5DZ1iBRwXf-ADMjsFDYz4ga5opfYXD8N0H_cBhzfp33FyJzyBj_OZBV8wHV49o-lo76GEX7ycADK4ujr8A53_gY1_NpdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e06a001e7d.mp4?token=uoIP5Gm2b6yqhlsXhkSToNtXcNNDnJ8HQAA3tzRwzNhynn_JbmRdPVjiQDSe2U9DwXG3_eUzLyNbmAuaqZ49ZhakHgZHrA9OjhVZml6avl5PMGi4z4oYZwAEKX9N-Q5-9RuL645kAaxjkAfnN_nh4Tngyzibg4FDrSh2zBr61MLl38kyR8Zaux5PWLtUPQ87VHUT4n9U-fjtzmrsom_MJ_7dsGlof3naOWl7ji1Gz-l0UfRqgQ3IDn24O5DZ1iBRwXf-ADMjsFDYz4ga5opfYXD8N0H_cBhzfp33FyJzyBj_OZBV8wHV49o-lo76GEX7ycADK4ujr8A53_gY1_NpdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
انهدام یک فروند پهپاد MQ9 در آسمان بوشهر
🔹
لحظاتی قبل یک فروند پهپاد MQ9 با آتش سامانۀ نوین پدافند پیشرفتۀ نیروی دریایی سپاه در آسمان بوشهر رهگیری و منهدم شد.  @Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/451066" target="_blank">📅 12:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451065">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHS7FVrytWnDFDrakJsnj5ns_hCqWg1s9qiUU_zvE6Dn-XRq6XTDjT_zqLC5-XPD_2EvshN6mI1ZIafwmrOOwK-LaPjI51Ddk8fQ_BO6vEYr2fPJVgJjFiwp0BvvGf97owcIQ_F66QxyolW1BiS10UYejX8YtqwztQeBSG9-rTFlCWAASMDocgnT9Hu5iENb9UGrjUb7hQuY018pvpivSO_bFUOg8t8m7vZjzVG6Ippve8nWTilaGnXIzxzgC-L5u8bMpQjFpQQ9eM58vCNTpxGxK7KqzLWzNyfX0gNJFyXtTJXdA3sA-YON2X9ME1bE4p4F2_YaoODyiXuzfEyLrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا فرانسه ۶ تایی شد؟
🔹
شکست ۶ بر ۴ فرانسه برابر انگلیس تنها یک باخت نبود؛ این مسابقه به یکی از سنگین‌ترین فروپاشی‌های دفاعی تاریخ فوتبال فرانسه در جام جهانی تبدیل شد.
🔹
تیمی که تا قبل از این مسابقه در شش بازی تنها ۵ گل دریافت کرده بود، در یک شب ۶ بار دروازه‌اش را باز شده دید؛ یعنی بیشتر از کل گل‌های خورده‌اش در طول تورنمنت.
🔗
دلایل فروپاشی خروس‌ها را در
فارس
بخوانید
@Sportfars</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/451065" target="_blank">📅 11:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451064">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1f69b8faa.mp4?token=snLnGI3W08Ib94Tv7XMfY9sUyl3xdTE8vcAm7kAkrKQsfiIplQzd2TEZ4g66m6A5SOb6TmfQFgbmULm4TrPjoQqAscYJHD-DPPDc_VYEKBk4MMdcb2ZOxbo3M2aS_qLjqELEHdrT1t1SqBg9AEcVe3zUnOOzNbXQMvAYSUDSHjjpQEzq6zqaOG0wGz1EGfDaZbNgzSf4-P9SlsVAo6208f7I8YFNdv9u-wA8NOirH5YpEUP8_mAEES_quhPG-GxEh8765YOeSFBsQR6zXg-4P5egSfrKc-250SvKeaDz-CmDz3z1UcyWjVG4CeC6lLEpl6r2darDpWRV6G69B-u76g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1f69b8faa.mp4?token=snLnGI3W08Ib94Tv7XMfY9sUyl3xdTE8vcAm7kAkrKQsfiIplQzd2TEZ4g66m6A5SOb6TmfQFgbmULm4TrPjoQqAscYJHD-DPPDc_VYEKBk4MMdcb2ZOxbo3M2aS_qLjqELEHdrT1t1SqBg9AEcVe3zUnOOzNbXQMvAYSUDSHjjpQEzq6zqaOG0wGz1EGfDaZbNgzSf4-P9SlsVAo6208f7I8YFNdv9u-wA8NOirH5YpEUP8_mAEES_quhPG-GxEh8765YOeSFBsQR6zXg-4P5egSfrKc-250SvKeaDz-CmDz3z1UcyWjVG4CeC6lLEpl6r2darDpWRV6G69B-u76g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ثبت حضور یک قلاده پلنگ در گچساران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/451064" target="_blank">📅 11:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451063">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
وزارت کشور بحرین: آژیرهای خطر فعال شده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند.
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/451063" target="_blank">📅 11:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451062">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/167d0f36a1.mp4?token=Af_p7uTEj1ZDtSgB2ska_qzdvvCPZPZQFF8oqSB1V_-0oZxm_LTojRAXyqEA_SXoaXqdzpXKbNwO6g0s1I4ykZquMYv_RjV99KtrkC8UC-XFbzMxgw7F5c1a-s-VR3k_V8OjbPL4_Fzv4Kf_Z4tWL73A-XgSm_AxsMBCYnf2lLfh6njZUBufdwmoy9mnppNXE0EB01JJu8w_S6DkTwmcTnuHiTHu5vjhXUS7MN3YJdaO8fe7LtqDQzdrir4N8Djsxeh-yXrfn9YqBq65tr3WPlZnsKDuZeZV6cT_hTyDVAAWmMYeHyhLyCuY7aM0ACbP3cWnyxnmxQ1n2S6u7vBeYRFPBD23tTpfxlIToBYhwS7eF9c0NpkwDArvx_nbwNJkG_12uDJXVvzwSKVrGCVt3gH2ta_0kJeOTZRem2VnRFeS5Nip-EfQgInulFRnQXu9pyz8sp68LwI7DQM8ShpciuRme9L22Pojk6YNMHNzD4-inLcKuCTN6F7RXEcPtoNukWgncIdd_MDlJFQr84eIpvgqz4x_8WhVyvdQ7bkW57QizTR7eFB17a00blyyU5es81W4zBnNkBtoCBmSNqSBNeaepy29aZONf7R1shUaRKuo1OYVUYyzHEiPZbef3WmSkP9HIWELUyqIk4EBzwUrmrnhBgemxCf3q2mEQiLlOrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/167d0f36a1.mp4?token=Af_p7uTEj1ZDtSgB2ska_qzdvvCPZPZQFF8oqSB1V_-0oZxm_LTojRAXyqEA_SXoaXqdzpXKbNwO6g0s1I4ykZquMYv_RjV99KtrkC8UC-XFbzMxgw7F5c1a-s-VR3k_V8OjbPL4_Fzv4Kf_Z4tWL73A-XgSm_AxsMBCYnf2lLfh6njZUBufdwmoy9mnppNXE0EB01JJu8w_S6DkTwmcTnuHiTHu5vjhXUS7MN3YJdaO8fe7LtqDQzdrir4N8Djsxeh-yXrfn9YqBq65tr3WPlZnsKDuZeZV6cT_hTyDVAAWmMYeHyhLyCuY7aM0ACbP3cWnyxnmxQ1n2S6u7vBeYRFPBD23tTpfxlIToBYhwS7eF9c0NpkwDArvx_nbwNJkG_12uDJXVvzwSKVrGCVt3gH2ta_0kJeOTZRem2VnRFeS5Nip-EfQgInulFRnQXu9pyz8sp68LwI7DQM8ShpciuRme9L22Pojk6YNMHNzD4-inLcKuCTN6F7RXEcPtoNukWgncIdd_MDlJFQr84eIpvgqz4x_8WhVyvdQ7bkW57QizTR7eFB17a00blyyU5es81W4zBnNkBtoCBmSNqSBNeaepy29aZONf7R1shUaRKuo1OYVUYyzHEiPZbef3WmSkP9HIWELUyqIk4EBzwUrmrnhBgemxCf3q2mEQiLlOrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دعوت حدادیان از سربازان آمریکایی: پایتان را به کشور ما بگذارید ببینید چه بلایی سرتان می‌آید
🔹
آنهایی که می‌گفتند «نه غزه نه لبنان» خوب بیایند جنوب ایران!  @Farsna</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/451062" target="_blank">📅 11:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451061">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/976711c4e8.mp4?token=CLD4nXtQ0LbcezWFCKYE8XmHBHKa5np5L-AjfE-h6q3nEzJfqHHpGb2SiG6WCFrvS4VeUtidnsmaQt7SDI7-gnNbOZB-aK5993PGof5felOKlEvxZzgqbOPD-OkVwrwwnKofZnaR7bvLwD8PoaCK9Y2SZwuGmA3433V11S1zOm2maRAIsqnEf6skVQLxKW_HIkzi_b1abPkYbBcrrKk6r6y-tuotmckX-v5Fwde-zayjtWIP3f8UZGgAJf13-iVb9iBgAP1tjwTLGSmlfT-baYHqRMyuYx0A-RhAYTjzrpOF5OOuZhyhhUfSDHh2leiWvw7Me3LFS6VAj7_JyKMmyJi7WeXfmnkP9kFFpFE2MOTKA7XAJs8UIox-lxMj-Fto1dSaepWsJkePOTtdzl5FHuNJ9WksXkaygwV77yfG1dfni8oqJCtTUNSdJYqbd0EcrPy1TtngpLhOPz3wo0iVCbAJfQFFKdia5rbr2T4S9wSmoxmwYq-_O5MZG6qWgrAp5PIoB9tdhhXidbjYtAUWLFbkB1sf2dYSViDMuiv_HsuvQlb2WqZpdfxLWVo2g4M5BOe9UoOS2dcFh-bCNj6hnGQXs-HZSC5-v1l7qMK4_pUm8Oqux_aaH69rJzTnXe51HqS5StUhegyLE2SeYW22rVye2QyZLoWgaZJ5DIs-IMs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/976711c4e8.mp4?token=CLD4nXtQ0LbcezWFCKYE8XmHBHKa5np5L-AjfE-h6q3nEzJfqHHpGb2SiG6WCFrvS4VeUtidnsmaQt7SDI7-gnNbOZB-aK5993PGof5felOKlEvxZzgqbOPD-OkVwrwwnKofZnaR7bvLwD8PoaCK9Y2SZwuGmA3433V11S1zOm2maRAIsqnEf6skVQLxKW_HIkzi_b1abPkYbBcrrKk6r6y-tuotmckX-v5Fwde-zayjtWIP3f8UZGgAJf13-iVb9iBgAP1tjwTLGSmlfT-baYHqRMyuYx0A-RhAYTjzrpOF5OOuZhyhhUfSDHh2leiWvw7Me3LFS6VAj7_JyKMmyJi7WeXfmnkP9kFFpFE2MOTKA7XAJs8UIox-lxMj-Fto1dSaepWsJkePOTtdzl5FHuNJ9WksXkaygwV77yfG1dfni8oqJCtTUNSdJYqbd0EcrPy1TtngpLhOPz3wo0iVCbAJfQFFKdia5rbr2T4S9wSmoxmwYq-_O5MZG6qWgrAp5PIoB9tdhhXidbjYtAUWLFbkB1sf2dYSViDMuiv_HsuvQlb2WqZpdfxLWVo2g4M5BOe9UoOS2dcFh-bCNj6hnGQXs-HZSC5-v1l7qMK4_pUm8Oqux_aaH69rJzTnXe51HqS5StUhegyLE2SeYW22rVye2QyZLoWgaZJ5DIs-IMs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شرایط اعزام به جنوب را فراهم کنید!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/451061" target="_blank">📅 11:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451060">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7Zg6eh9Fymx3012fGxPAl8KwQNfAgsHQufje5AVSHgYW6Fe9aYkxFAPL2e-sHjvgA2e0GlQJYVgWJXSjlQ8LKkQykoGEYEf9QXQTb87SYCzLlh8Zsw8O38PmKOQgrJ5-wwC_63ZEx8N-kjfXJ7IGo_eL_1epWtv0aHmuD70w6imT8ONm0O1ODjwkD0cmHUJdoWrTXn2nwZD2hQGeJKkbtrPfNgWCx4iJ-7ewRUq6nhywISl-cU-zVqpizjOuzZZr16Wjv5U2opRZHmqMxZf9OdYgQwWRpDAwaYFX9dbei1tX5-tTyRW03gmolAYx14m4zZnXV57s3clncdjjIkCLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ انهدام چندین هواپیمای نظامی آمریکایی در حملات ایران به اردن
🔹
روزنامۀ وال‌استریت ژورنال به نقل از مقام‌های آمریکایی گزارش داد که در حملات موشکی و پهپادی ایران در روزهای گذشته به پایگاه موفق السلطی اردن که با تلفات گستردۀ نظامیان آمریکایی همراه بود، چندین…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/451060" target="_blank">📅 11:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451059">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d92f76bf7c.mp4?token=OkopyrOA37r9IH8QPh7jUSkcUFNdcfDEE3dBftd4DMyto4Dgd14sFA2fW9nlG9wDuHqbrCF5GeQh-MrwWH7OeHsLeW8GCA3TEvzZL_ZrPScFXzOLILWTr8myJgJKHJFJoMFw0gylSAtpcZOMCEE1rP2EB7rj1pPpLAOKFzlb9LxQqPgBAu5f8zMQGlIBcWXV3Qa-A_DM7FJGKdk0gELW7YvPALkWED-GJKwaxxm2brp-7-BKZhRpIfXWFikvxQc0HwW4IOQyxuU1OKa1Vb02RaYUGJGF1cQUa3iyqLvPTfAVW-Qmb2QqRuAMuaHrH_LrrUYxCIfHHlMjBaoO_XpQZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d92f76bf7c.mp4?token=OkopyrOA37r9IH8QPh7jUSkcUFNdcfDEE3dBftd4DMyto4Dgd14sFA2fW9nlG9wDuHqbrCF5GeQh-MrwWH7OeHsLeW8GCA3TEvzZL_ZrPScFXzOLILWTr8myJgJKHJFJoMFw0gylSAtpcZOMCEE1rP2EB7rj1pPpLAOKFzlb9LxQqPgBAu5f8zMQGlIBcWXV3Qa-A_DM7FJGKdk0gELW7YvPALkWED-GJKwaxxm2brp-7-BKZhRpIfXWFikvxQc0HwW4IOQyxuU1OKa1Vb02RaYUGJGF1cQUa3iyqLvPTfAVW-Qmb2QqRuAMuaHrH_LrrUYxCIfHHlMjBaoO_XpQZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
علیرضا دبیر: ما به جنوب کشور آمده‎ایم که بگوییم نوکرتان هستیم
🔹
من جزو کشتی‌گیرهای ایرانی هستم که به آمریکایی‌ها نباختم. آمریکایی بردن خیلی راحت است، شومن‌های خوبی هستند، ده‌شان را صد نشان می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/451059" target="_blank">📅 11:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451058">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZ_SztFPMsWjXHcIzcSIyrtU_NuaSWN6lSOWqhbwRPg7DaY8Bs-LggNGhx3JCmA2nQcVyF7mwcN3Ag9noeiouqRw79bSAmGD6HMCQe0ac5mXkEeIu159rCD6WzUycme0td5YdaWsfor2LREtPm_Z7hLUjMADoRcd33e0E4i2ePCHpHvTsyjDaNVjHtjJNQAHqPvy4hYhu0dhhz6wmH1bbTSOsSFHt0ElU3vDixEwiCoTZALPlYT2FHQv3H8FRq8Yp-r-uApYdNxlR6ZrJ5NDwUOtEYBHAAuYugQSnRSJAmOIN0iduQ8TRpiB8rpE2sBQn3x2luTItxQ9E3yTvvGjSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به‌دنبال ممنوعیت پرواز پهپادهای شخصی از ترس ترور مقامات
🔹
کابینه سیاسی-امنیتی اسرائیل در حال بررسی طرحی است که بر اساس آن پرواز تمامی پهپادهای شخصی به مدت شش ماه در سراسر اراضی اشغالی ممنوع می‌شود؛ اقدامی که به گزارش رسانه صهیونیستی اسرائیل هیوم، پس از هشدار مقام‌های امنیتی و با استناد به خطر حمله به شخصیت‌های ارشد اسرائیلی مطرح شده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/451058" target="_blank">📅 10:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451057">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38efd958d1.mp4?token=A3cgmdKUrYAkp3LcQfQ34Adbt59FT4D5pjxqEn1LPyBjWQYNE-i7s2yu6FsNWI1_uXOmp-VdAeW8h0WNzPYkTfzrVUehn6PZXLSGa94QJeQlT7WgJnPyeuwYT48LGv4EKGUdGlApqW7WaVN_n5NfXgXS3W8gwSWph6j0e6uK8Yg3KmIiQVMtQibWM-kF8bXzZlK16zns6C9y5SfPaXfpWjGsSkQ2MhwDyKEo8X6Ep2tvJN0UX_nIxc4CV_TiQ3in0-CX4v8pHo8oTiSLh3ySQVQqFwmA3KDd1FNRASms1Q2UhcZbQePRE4jfSKXPuQM5ZIt144lgIpCz8zseGwopbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38efd958d1.mp4?token=A3cgmdKUrYAkp3LcQfQ34Adbt59FT4D5pjxqEn1LPyBjWQYNE-i7s2yu6FsNWI1_uXOmp-VdAeW8h0WNzPYkTfzrVUehn6PZXLSGa94QJeQlT7WgJnPyeuwYT48LGv4EKGUdGlApqW7WaVN_n5NfXgXS3W8gwSWph6j0e6uK8Yg3KmIiQVMtQibWM-kF8bXzZlK16zns6C9y5SfPaXfpWjGsSkQ2MhwDyKEo8X6Ep2tvJN0UX_nIxc4CV_TiQ3in0-CX4v8pHo8oTiSLh3ySQVQqFwmA3KDd1FNRASms1Q2UhcZbQePRE4jfSKXPuQM5ZIt144lgIpCz8zseGwopbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
علیرضا دبیر: ما به جنوب کشور آمده‎ایم که بگوییم نوکرتان هستیم
🔹
من جزو کشتی‌گیرهای ایرانی هستم که به آمریکایی‌ها نباختم. آمریکایی بردن خیلی راحت است، شومن‌های خوبی هستند، ده‌شان را صد نشان می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/451057" target="_blank">📅 10:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451056">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">تردد در جادهٔ هراز فردا و پس‌فردا ممنوع است
🔹
پلیس‌راه مازندران: جادهٔ هراز در روزهای ۲۹ و ۳۰ تیر از ساعت ۸ تا ۱۷ برای اجرای عملیات لق‌گیری و ریزش‌برداری سنگ‌های ناپایدار به‌طور کامل مسدود است؛ رانندگان در این مدت از مسیرهای کندوان و سوادکوه تردد کنند.
@Farsna</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/451056" target="_blank">📅 10:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451055">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e97d26e7e.mp4?token=QhSW7y4j4vw-YoIGmoovWRrePSExnAVxidOKvzJz9I2GjLlzBnrdslEsZkYhtNXM1IJy-P3PwkGGTtGHe-PAquJFFp6v1UwoLmiSYE6lOPViSX5zlEwZ4biMzI55pW27FtsZVg32gsZ5egrKh30fLOHGA_fJ071px5ij7lvvFvPe1PMsqHWN63BrLrx5zQoW390HVDFehnXs-j_iSyOXu_-bAOQpbb0egqxQTshg2JNN9CEMSiPtJUd7oMLCAt5712zxWmLuhUo4KrjXsWY66DccsU9-ZsWHQ0NE8oapNzRUss44sYtFJjlKzBATuQlG3X0ATajXjY0jbmH-l1Orxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e97d26e7e.mp4?token=QhSW7y4j4vw-YoIGmoovWRrePSExnAVxidOKvzJz9I2GjLlzBnrdslEsZkYhtNXM1IJy-P3PwkGGTtGHe-PAquJFFp6v1UwoLmiSYE6lOPViSX5zlEwZ4biMzI55pW27FtsZVg32gsZ5egrKh30fLOHGA_fJ071px5ij7lvvFvPe1PMsqHWN63BrLrx5zQoW390HVDFehnXs-j_iSyOXu_-bAOQpbb0egqxQTshg2JNN9CEMSiPtJUd7oMLCAt5712zxWmLuhUo4KrjXsWY66DccsU9-ZsWHQ0NE8oapNzRUss44sYtFJjlKzBATuQlG3X0ATajXjY0jbmH-l1Orxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی جبهۀ پایداری: مشکل ما اصل مذاکره نیست، طرف مذاکره است
🔹
متقی‌فر: این جبهه اصل مذاکره را ابزاری قابل استفاده می‌داند، اما مذاکره با رئیس‌جمهور فعلی آمریکا امری بیهوده است.
🔹
مذاکره با ترامپ نباید صورت بگیرد، زیرا او فردی قابل اعتماد نیست؛ انتظار مردم این است که مسئولان این موضوع را همواره مدنظر قرار دهند.
@Farsna</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/451055" target="_blank">📅 10:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451053">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">انهدام یک پهپاد MQ9 در اهواز
🔹
دقایقی قبل، یک پهپاد MQ9 با آتش سامانهٔ نوین پدافند پیشرفتهٔ نیروی هوافضای سپاه و تحت کنترل شبکهٔ یکپارچهٔ پدافند هوایی کشور، در آسمان اهواز ساقط شد.
@Farsna</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/451053" target="_blank">📅 10:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451052">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سپاه چهارمحال‌وبختیاری: به‌دلیل اجرای پروژ‌های عمرانی، احتمال شنیدن صدای انفجار در امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/451052" target="_blank">📅 10:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451051">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvGLv_0U1JcNpgQRYIYcHJ9Trln_xANV0u_u-IlMoIWpjn7oa4EYIxXZTea54WuxgPZoHo14xO6H9YSX1FGt6J40g20l1S75HcOstpVsNDv-I0mW5eCWB9jNekbmYxdR2gw7t5ojmJcA8ZLxnKw1b9t1kbSGBPdinhi-KZjTBPhKLTuvHShWSkYaaFMUYwEQ08YAC0gzLw2wtOd1h3ERO6-hYoiS-jbLLlLCnEPrefqHj7wo3HH6d6imU1dYQ0tEWxJtuufca6EkOAvN9lEVrcdm-UDIcs0lG4vnr0x16C1ths6KnSFjtyb3aLKcQn5KZQZt_2uk_QQ5bPNv2Um51g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درس‌های فراموش‌نشدنی</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/451051" target="_blank">📅 10:14 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

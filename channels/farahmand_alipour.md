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
<img src="https://cdn4.telesco.pe/file/aaPt-8xAmPi-41IyZ36nIUb1bLBm0GJr7i2RwcFFr8WV4iLHwk9y7kMXH7zlDVSOYXqAH7p5uVW-tbLCjOkhG6-bjK9zpNBaIcd4QNpQRjWWrRJU800VLxwnYflsGT_vWGhAWcKhDo3nj67Xtip7exGJ-19Fie5A4GM3mb1_DvFfnROEB8GoP9TfrOJ0o07V9EGDhvFCnj41C6_fRUFdKaP-c96ze4KzBz0forCA6zxt5eT6h_82Y0bA2Cxyn-rD6AiOD2ZJGDNAHPhZEKPkwYx7598bP1yHi_dS-ETiUfIcUyG4Mb7mzN-YFRGwUrlLGJF4prXh7Wq0zdNwGujO-A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 60.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-23 05:55:22</div>
<hr>

<div class="tg-post" id="msg-4943">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwRqMTYb_KXOG-0cHGdtcTq-WKxzgDNRVxhK5GRMeUGNsicWW0Y2thprOfz6hB_ljpH-o84LYy_btaKHey22uriiKVxksAxyVti3qvhhSEROlUBs2RrQPpz40GZnYMwdM65PeWIyslhgPA0Uv1_6wV2AqUibnJO0PgMFg0FVl0VZNJxOZlnIZ-MYzN5CxbwcVqNVGbUSES5_QL5TEMKqm3eCfpLOKesrkmkU787A3a60rDpSiRjZ3BAblsCLHRzuIztWtSj3lNGh5r6Fs69iBzRPdV-0-5AAXCa4XsXRaEIukVTsWevl6QxTpa1dDLiAXXxCLVofZ9GEZwx6YeBsCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وقوع زلزله در تهران</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farahmand_alipour/4943" target="_blank">📅 00:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4942">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
وقوع زلزله در تهران</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/4942" target="_blank">📅 23:48 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4941">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
پنتاگون در حال تغییر نام عملیات حمله به ایران از «خشم حماسی» به «عملیات پتک» است.
پنتاگون میخواهد به این شیوه از اختیار قانونی رئیس جمهور برای دست زدن به یک «عملیات نظامی ۶۰ روزه» بدون نیاز به مجوز کنگره استفاده کند و با تغییر نام عملیات، دست خود را برای دور تازه درگیری نظامی باز کند، بدون محاسبه روزهای عملیات قبلی.
بر اساس قوانین آمریکا رئیس جمهور می‌تواند فرمان به «عملیات نظامی» دهد و این عملیات می‌تواند تا ۶۰ روز ادامه پیدا کند.
صدور «فرمان جنگ» اما بر عهده کنگره آمریکاست.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/4941" target="_blank">📅 23:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4940">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZY3WRKHzG0hrN59VXw7vzHz-VTkOi02VsVAwWm5hUsviPpe3dB44aof3gKoDbiG_aZkoEtLZw8_fSlLI8J2gwtR16O9yDjGuQt9G3yJjfO4mx-8jDB7yvUdYUk_ZKyUneHrlqyfHrOQn_9_4AxruRNJ_dWqAO4dfssvvHHKdponmuGIAHk0ZuJmrUkrLLO55_GSPigDQZuYns4JfpKdnR26ulOWLB23ioD7wFzicph-5Ixk6xyoZLjviSewkA2Mltq2RKMz9x3_e7DuArLZhReEoPvilDHGas41UKpTLOfE9oDDPanIQiDphS7d7XruHJOaA4LZxYeukMzTAp412Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
وزارت خارجه کویت با صدور بیانیه‌ای  رسماً جمهوری اسلامی  را متهم کرده که گروهی  از نیروهای ۳ پ  را با قایق ماهیگری  برای عملیات خرابکارانه به خاکش در جزیره بوبیان فرستاده و  در جریان درگیری  یک نظامی  کویتی زخمی شده است.  کویت که امروز سفیر جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/4940" target="_blank">📅 23:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4939">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JI9q5rdwcJUeO1q4OPP2R46cq6VyDuMvBoZBg95KumGBqnn0aamz_dxIEw1NiKZaY_BmSkd4dwtpxLcyPZLMZ81nkBDipxTReMBaXusFhbjK8PTitbM2YIQBGx3dyrp857hyqwr99fVIoBPNCGUpGlITL0ZBgfe4txLSXrD3Djxefy80PgZpj67X5sN7285UoSYu1hW8c4wJ-g9_JT804h78u370KVNTWTdGNOjONgWP-Wnq7y-xXq7WQot0OyS1mQ_sH11CQjiayi6BvDfC-wVU8f2pb3qPg1jsquXZuTzNuXReaUqzn09VSxea6cO5RaysobI-pw6rqlsWUX4RNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان اما در میانه جنگ دست به حمله به ایران زده، در واکنش به حملات مستمر جمهوری اسلامی به عربستان،  نکته جالب اینه که رویترز میگه عربستان حمله کرده بعد به جمهوری اسلامی گفته حمله کرده و هشدار داده اگه به عربستان باز حمله کنه عربستان بازهم به ایران حمله خواهد…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/4939" target="_blank">📅 23:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4938">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rc_a65LkOJR7lrJVRY4DzO1FEFZVG4sHtfcK3Ewar0WesqGFXbbbkWnPKoG0WXR45sXbuTozFYE0gbjqRaDUErogDY_qyobSmxVukfOUDMavVm0UAa5i-8a5sozZpwfgF6B4qXIkcFV6xGKFtKBYhpYWzUOGEdVQ0S1lswoH68T95m4EhYrzYIcYNQBywWXpqM_8atlJd3t7UIjSIO3q2detmum16YmaC2_OZQnA90l9Lr0MDwYkGqpobip_vZk08UP13bxAe-HkGlabhTwDcIVl_zQkumNCQjWTsMqujwV3YNm-87zZ43ySLK4HGm9vo5ReGBHKPYN3jqTWi7Iutw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در دو روز اخیر مشخص شده که دو کشور امارات و عربستان حملات هوایی  به ایران داشتند،  امارات بعد از شروع آتش‌بس دو بار  حمله کرده، یکبار به پالایشگاهی در جزیره لاوان و  یکبار هم به تاسیسات پتروشیمی عسلویه.   امارات در صدر حملات جمهوری اسلامی بود حتی بیشتر از…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farahmand_alipour/4938" target="_blank">📅 23:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4937">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrlZWmRaI4F2W325Uo61AjrX6nL8gJ6TX6FKHArpmlK0ME6pXajdwzhsn44Fwp0vdz_vUPiS65xxHmgt1L-nXH03DvSfaKi1invsD3g16S9jLdpJZK0NsatmDqG9nDsXBCYs7hcLZgIqLRXL-yYyLHS8UuguKURhYiqA9k41hEaYxvq9n2BrR2GzcUf6SbRz72nLHyimjgLLR8OYBc-pKHUEaZZlOrntznBGXtn3uKedNm09pcUGfAmDb3TLCxkJFNVvlpqDpQTq2oUrQ8RKryguVmY_nKhbHn8HVyj5CyypjM5Gq1uq_xDYoimSMK5iSmw7Mbs3fo_EuGFISq9S7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در دو روز اخیر مشخص شده که دو کشور امارات و عربستان حملات هوایی
به ایران داشتند،
امارات بعد از شروع آتش‌بس دو بار
حمله کرده، یکبار به پالایشگاهی در جزیره لاوان و  یکبار هم به تاسیسات پتروشیمی عسلویه.
امارات در صدر حملات جمهوری اسلامی بود
حتی بیشتر از آنکه اسرائیل مورد حمله قرار بگیرد، امارات مورد هدف قرار گرفته بود.
امارات پاسخ خود را بعد از شروع آتش‌بس
بین جمهوری اسلامی و آمریکا داده بود.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farahmand_alipour/4937" target="_blank">📅 23:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4936">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e0ac8ea1f.mp4?token=h4c6SAkl1hrBw3hYEWtFetVv2kObGPwREl6Ybuwh_Ijv0WBcgvsDoiXzwEsGhoIiOQlx-16Mw5PYcsYqPO9_RyBGWGpSaL5ahqDp05e38GRIRTczsDI_HYkIQRfO2ZX5PHZ0mzmG0SMQ0tCFidApQfeRSu0QS_lZuthPuzdo2EPiW5eiG9eDh9pJsW4kJjalZnBMriX7Zc4nLky12CSWXaXH0Ath2QAUa_SdXzt23muNOF-SWS_53GQOF4mdxURUuQ7CyB8S6E_1zPg1tloTF_2rlcpCQbyv7vPpwobhtrodc1k1uVYHZXVFcIRhaxNFmWF4s8NaLweEpIynwrj_qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e0ac8ea1f.mp4?token=h4c6SAkl1hrBw3hYEWtFetVv2kObGPwREl6Ybuwh_Ijv0WBcgvsDoiXzwEsGhoIiOQlx-16Mw5PYcsYqPO9_RyBGWGpSaL5ahqDp05e38GRIRTczsDI_HYkIQRfO2ZX5PHZ0mzmG0SMQ0tCFidApQfeRSu0QS_lZuthPuzdo2EPiW5eiG9eDh9pJsW4kJjalZnBMriX7Zc4nLky12CSWXaXH0Ath2QAUa_SdXzt23muNOF-SWS_53GQOF4mdxURUuQ7CyB8S6E_1zPg1tloTF_2rlcpCQbyv7vPpwobhtrodc1k1uVYHZXVFcIRhaxNFmWF4s8NaLweEpIynwrj_qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ راهی چین شد.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farahmand_alipour/4936" target="_blank">📅 22:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4933">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XUEvpQkdJQ1kko-eAX3nh3iRDmB_W9gYl8lmG6ckSFAHY-_iwXN_NAtMYf_oWAj4uF7ZMtsXzUJKo-gPvjDnYT9kIZkh1hRHmt5d8iCe9SRhbH2oRG4CqkgdJXnztDhyPLxQsnCBSC9T0VXJAmIE1Eos_RHSjIBVWPq2-fRqzgh5I99cgyzv1qUda8wk54c_KKJS0M26KFmIZyIlET6u3uP5VoCJ3irSUhmr9HK0xWusKuwzZSz3TPje6W2qs-TOW6dEYJigNN6hATvY20PLSt1_MTBf-xTFm4Vd3X3UTMGLJJJD7qcxqeJD6S6vv-pbgCOKUF2iFGZP3EU9fIG_dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dkY8HbU4F2w0EKYb4IJrCsj1DywW08BEbpBHvtmYPZ00MJCtjIv1TKPY-qgJO8S24CWWHa1_9Uhuahlo84TRhTMmEi3xmyqt-z2w-XNIbC4tFJHV8jdtrpPGECR_eyO3zc1e0MWmFbbQgzOZqzyENQ8tyds3AbqKPLJEwuZ8aOIPjyXGabEM94DlPEFhlHVReNpOr633sX72eDvyZx8qzOkelqxAZRXJKm6BUK1c59fgWvKRYGYojlcnaXDsiblTzGavg-VZZvMqIuqDykves-Y16h7MQQTNZgWXxYnQIiz64rNrG9iG031XHMuqNz55zgTsy4Ek5rMoFDBfmwipBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kPdRdTqdKMJVwUTDtAwTfJtGtNeZuiPK5TNhHG_NObaWZ11gn0MC7BS1vJaqyE68ywJ_Dbpaxt2svsiFP3mZwWEXtQPRgSq79w7EvuRDJQ47G18wyEqvdrVvWLP58w3jWBhLlJLZ_xlEgtyUFGSaMycsnS1M6UeHZI6AQ2n9VbR02pX88Ura4okK7UYYF6fo9ETz8k21yndccWCPTpEh0Sno7ijYmM2FgDycxOtPWNvxUkWbiMdPqgqps8z2MQEc-UtwRaueLsf9Q3AJr5s5aO7qdkYPN0AAy-lqRP_TknN1dVEpkglyrLq7d6wJVoT75DayjiqzOJumZpJPvkucfw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">۵۹ دانشجو امروز از غزه وارد ایتالیا شدند.
ایتالیا در مجموع به  ۲۲۹ دانشجوی اهل غزه بورسیه تحصیلی و تسهیلات اقامتی داده که امروز اولین گروه آنها با یک‌ پرواز وارد رم شدند.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/4933" target="_blank">📅 22:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4931">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kt72FRG-vLEqP0RkduuNnq1CjfG6nRjI41O3KIekigwoJhXuVcfXrZOd47MNeZ8gHxEaKTzgEbPM4ZD--dSi330Y418MBZ2IVdHSbfhsvKmlHMD57qdaCzilFp1B_A3QF1QHjHq6beg4mPL8SWcIeeNJDeqyPtBhvK1sbpTeVPBPag2RR0tn01Z-TyvAcL925TvKFl1P7OcyLgrmSi7UXfXzeLzUI-RD6oZ8_Vh4cFyBUmVhREmm6eEKZSXp6BVKlv5A5GRwbEtWQNyNGzCMDaQ6JOb7byDxB40Wcl4xaSi0KZp4BACzRQrQqCOqccBDi4_nRGVQ6RiSDfjBCbl9og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
بر اساس گزارش رویترز عربستان در طول جنگ، مجموعه‌ای از حملات تلافی‌جویانه و بدون اطلاع‌رسانی قبلی را علیه ایران انجام داده است.
🚨
🚨
آمار رویترز نشان می‌دهد که پس از واکنش عربستان و حملات عربستان به ایران، حملات جمهوری اسلامی به عربستان کاهش یافت.
🔺
عربستان سعودی به ایران در مورد انتقام بیشتر هشدار داده بود اما کانال‌های دیپلماتیک حفظ شدند.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/4931" target="_blank">📅 21:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4930">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
ترامپ در آستانه سفر به چین: نیازی به کمک چین در خصوص ایران نداریم.
🔺
یا ایران مسیر درست را انتخاب می‌کند یا ما کار را به پایان خواهیم رساند.
🔺
‏من به یک چیز فکر می‌کنم: ما نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد.
🔺
با فوران نفت در بازارهای جهانی مواجه خواهیم شد.
🔺
همه زندانیان سیاسی ونزوئلا را آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/4930" target="_blank">📅 21:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4928">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f-YI17qibGupoAmWmJgbCv2lvDR2yxsKNeITXmoyV6ldokWF08k_3bk_KBSVZ0ksRA831RUYl_6WMnlTKTnTddEi3k-Afc5JebiyGUP5gbxeU993FbQT7DEiqyBH-8cyJ2IbOl7uwC_DjS-EnqblXE_goCgDEz-4zdgcphdn9H9X2QyPOxkYW7nZEG12-g0T9sPZMKEpG9856-UxlBF7WX75LjSprVUXtdl_zu9s5QO-K87cb2Gqu00Q1jkulQ9U08Qyr1sIeKBIfs-il24XyQUC2XTu5dYvpoL5P7Jt_bLBukqe9Lfm7gvUBjDW21aJeu1i-GlA6ZPsgnk6VT1wZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eSnGiVVT_TSvVKpIGYFwzSDK5vZgv0G2X-vD8_vKOD3RgG8Ux3N8XrMslwat0seYBfWy2IGROVfmVjTeeysctenjZneLnoC8ybGJ_CcoKB6T9g54Ad9Zek__x9IyqZ6drlsAQ_HOODlhglFiUjLYyYKSsDs4FgS4tr7bXfjAjR3FSB-8ayvXe8H_YbtXrltsRd6dHvqIHZ2t-xmxYYCkB5QeBqeP0ISGhwhRYaPWt-vqXjDnPhRProbXt55zCBdqSJnNs9BFx6nCZkZXgjx9Ur_wrjgZHMzyPzD_hfZez7TwtEWThYu6bqOvqt_gBy1or5mjZb7mZORhU-g9Lk1HiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
وزارت خارجه کویت با صدور بیانیه‌ای
رسماً جمهوری اسلامی  را متهم کرده که گروهی
از نیروهای ۳ پ  را با قایق ماهیگری
برای عملیات خرابکارانه به خاکش در جزیره بوبیان فرستاده و  در جریان درگیری
یک نظامی  کویتی زخمی شده است.
کویت که امروز سفیر جمهوری اسلامی
را نیز احظار کرده گفته که ۴ تن از عناصر وابسته به ۳ پ را دستگیر کرده.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/4928" target="_blank">📅 20:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4927">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اینهایی که آرزوی مرگ یک نوزاد ۳ ماهه کردن، عمدتا عزاداران کشتن کودکان معصوم میناب هستند.
همه چیز این جماعت دروغ و خدعه است!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/4927" target="_blank">📅 13:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4926">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfId6hOwL6O1Oj1QYlVXwGQSiDirdWr9w77D_tcM8GqPoE97IQ9GhYITms4cyf5Hn9aevyc_0ZusR9A9Wk4W9oT4viPgNhMi1fUI5rU5czYwrLH3fRkiMMPghgry5maMg5uL01IopSAW817tAi43_upqEC14wzagkQk6OLm66Vg2C1xZfU_L01lBfD-qLBqObgBOZkytbAzhYjUd4Z0Ro4BDfltrptXi8DODRsCt86bWvvw6O5F3dOu8JmMq5qEqnlsczMt09nVS8opCNu9iXwRQ8nRicInlLTTlqRdDuVnwDH_UXf5EJqPuoUCSgu8obUlLpjElORWJQUN-Ucx5Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آرامکو (شرکت ملی نفت عربستان) :
در سه ماهه اول سال ۲۰۲۶ به رغم جنگ در خلیج فارس و بسته بودن تنگه هرمز، این شرکت افزایش ۲۵ درصدی درآمد داشت و ۳۲ میلیارد دلار سود به دست آورد.
بخشی از این افزایش شدید درآمد مربوط به افزایش قیمت نفت است.
عربستان از طریق دریای سرخ روزانه تا ۷ میلیون بشکه نفت صادرات دارد.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/4926" target="_blank">📅 12:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4925">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
خسارت قطعی اینترنت توسط حکومت جمهوری اسلامی : ۴ میلیارد دلار!
اینها زیرساخت نیست؟ سرمایه نیست؟ یا اخوند اگه نابود کنه ایرادی نداره؟</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/4925" target="_blank">📅 11:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4924">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
سی‌ان‌ان به نقل از منابع آگاه : پاکستان مواضع جمهوری اسلامی را «مثبت‌تر» از آنچه ایران بیان می‌کند، به آمریکا منتقل می‌کند!</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/4924" target="_blank">📅 11:25 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4922">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bm_lhC3KUc9f6Z1C_bIGzej-gxF9as82zNgBv-Fqj45ywrg_rzRWrVYekLcX5pYNgBjC3QzqVjTveEHEfkojLLmsQGGKJxg-uOuKFp0qKVeIFNBLKbj52lTytb22gbZMrhkhrKP2729eqtsGusJlVaixOHxhhHHujPlCmvc5t04Rbm8hQhWewLtqiTfrhP6TgIc9RO23S8ug9vpAh80wIOy1h95QcWFw1GfKrAzj7BixYilerY-LdnES5yewLW25Q1Ahy135y3ykzzwZEATS3Ga5nVWMQGyWRrWj24JaINWtFGQDKHYmqU9MCfsUgxmSAkScU8sahkeAqP0c1OsuLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b194f425f.mp4?token=B2yBDq_vBTbo1VEX0zDQsXAJhQJYE7W8xUfM8TzhXcN6rSedGugOhUAHBTum5K6LjB98id-T_1Yl_f1QMXZYdwY7vt84SrYLUThxuX9ohUqEXGhMPyI1_mD3IJ6uKCy4rv2aW1leZLenhOu95gLz3lcWGlLFvQWEWUncKn5O65sDEqc3z2nU6KIssv42vEvGi6jjiuegzlzj-yDq1UL9EjbgF_uIOxBDzsDm0UHF-gvDGZ2zGtPD63dKjaqOyJW9itOEGI1-mItpQvSZCpn0yZUN6Ia0eMOTatXzLyjYjuPsjT9X5QGjEtc7VuOf8rigoljFLwsxVVg1bd9ujl_XZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b194f425f.mp4?token=B2yBDq_vBTbo1VEX0zDQsXAJhQJYE7W8xUfM8TzhXcN6rSedGugOhUAHBTum5K6LjB98id-T_1Yl_f1QMXZYdwY7vt84SrYLUThxuX9ohUqEXGhMPyI1_mD3IJ6uKCy4rv2aW1leZLenhOu95gLz3lcWGlLFvQWEWUncKn5O65sDEqc3z2nU6KIssv42vEvGi6jjiuegzlzj-yDq1UL9EjbgF_uIOxBDzsDm0UHF-gvDGZ2zGtPD63dKjaqOyJW9itOEGI1-mItpQvSZCpn0yZUN6Ia0eMOTatXzLyjYjuPsjT9X5QGjEtc7VuOf8rigoljFLwsxVVg1bd9ujl_XZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلویزیون جمهوری اسلامی، اعترافاتی از «عرفان شکورزاده» دانشجوی نخبه، پخش کرد که بگه : القا می‌کنند که در ایران اگه درس بخونی آینده‌ نداری. که ما در ایران بدبختیم.»
بعد بردن اعدامش کردن! تا اثبات کنن درست گفته بود! ما اتفاقا بسیار بدبختیم که اگه نبودیم چنین حکومتی بالای سرمون نبود! در جامعه‌ای با درس خوندن میشه به جایی رسید که اینهمه اعدام نخبه و فرار نخبه و دادن سهمیه و پذیرش و… وجود نداره.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/4922" target="_blank">📅 11:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4921">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oj4Gwb6nVMM0pAWc5h0CyM5pdgLUduCx690xp9x-seOD8_5FroI_OF-CXkbUOtcH8ND6ZvC1N1VqRdPZs-CSUmd4LFkZaMv2sfis7Gkh863-k2WTOqwnQ1kIbGWJ-lrVBzWDqPVxfbw9lYPObF1TAQimIVKK-kl-OkdP1fGi0_jcIhSV906qVnyiP-gnOG7k_WmyzXFA4eHuo6nRoe7TVOq4M3zs6BxTx5O2Gnb_u00j3H-eIQ5MKRZ8iy8WUenBhl9GsdSjfyFJ2MUl5toSN_RW-MhnIbhZ5TJJXCuuzonhcG23Bs0C5uThDs6-5GVa6ZDnLzpg6TRN2EDO9uCYXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جمهوری اسلامی تهدید کرد که در صورت حمله مجدد آمریکا و اسرائیل سطح غنی‌سازی را به ۹۰٪ خواهد رساند.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/4921" target="_blank">📅 10:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4920">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JwEgQmHuEJ6lFE3RRyBu1dZL95-pe36yfFv7ztIadQDzBgM-GfHrutfWAfgjZK5LDhv4HgnUJ06fQdgBzPaV2EOIUQ8oRaRBB-rggorlTVfxRyt7P_NsWayPYh5g6WpQihRS-5ufwrqfxDi7zuguGd314_Fd0pKv0cU07-fxN3utKR6sjePpMxXTfSKnQhUhyLKg4bRR-M7JadPHUysoCcjiSNqbYwX6hTx2DqAltS1QjHICq00E0YbGRdpbMVYfV2jtl0_XCt-6z-UWJtQRhkPAUATaRRPsUexz8w72x_Sh-adYja86n5f-ZGkMJ7_HapT4JR782udiIi0IeJPqIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/4920" target="_blank">📅 10:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4919">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال: افراد مطلع می‌گویند امارات حملات نظامی علیه ایران انجام داده است، اقدامی که این پادشاهی حاشیه خلیج فارس را به عنوان یک طرف درگیر فعال در جنگ معرفی می‌کند   ‏این حملات که امارات رسماً آنها را تأیید نکرده، شامل حمله ماه آوریل به یک پالایشگاه…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4919" target="_blank">📅 01:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4918">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouJl-md3A7dsGdbN10575WX0VDVFzh3Gs18oJJyKsPHHmiPIdeX1O0Aq7z2aToBXU7uRIPbtVfSHAHAjAiTPlpPSgUyE9VHTtGqlaMLGBec4kgctnenNdsYym2N4b-Q16e7ddESxB-_fZQacg6LVQLIWE8iWYXmgDV81lAi4L6uPr900UGmiJCP5F1b9sUNYGTrp7WYw868bHF4fhd0sGXPYNIs9viGmllr-39VGbOqiPDYZ6ld9p0dl6g7ZeMJTFcFv9NaLY6cjovHxE-Prk5bHfi_8xIMKEIJWuHNG7kwTXQr2s1XNiG6kvkf4FsnfVDvU95jU5aalWPEg2ljxPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال:
افراد مطلع می‌گویند امارات حملات نظامی علیه ایران انجام داده است، اقدامی که این پادشاهی حاشیه خلیج فارس را به عنوان یک طرف درگیر فعال در جنگ معرفی می‌کند
‏این حملات که امارات رسماً آنها را تأیید نکرده، شامل حمله ماه آوریل به یک پالایشگاه در جزیره لاوان ایران می‌شود.
‏پژوهشگران به تصاویری اشاره کرده‌اند که ادعا می‌شود جنگنده‌های میراژ فرانسوی و پهپادهای وینگ لانگ چینی (که هر دو توسط امارات استفاده می‌شوند) را در حال عملیات در ایران نشان می‌دهد.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4918" target="_blank">📅 01:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4917">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">در حال حاضر : جلسه ترامپ با مقامات ارشد نظامی و امنیتی آمریکا در کاخ سفید برای بررسی سناریوهای شروع دوباره جنگ با جمهوری اسلامی.
🔺
یک منبع آمریکایی به اکسویس : جنگ احتمالا قبل از شروع سفر ترامپ به چین (پنج‌شنبه این هفته) آغاز نخواهد شد.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/4917" target="_blank">📅 23:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4916">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏منبع ایرانی به الجزیره:
واشنگتن در پیشنهاد خود خواستار دریافت ذخایر اورانیوم با غنای بالا (۶۰ درصد) شده است
‏واشنگتن انتقال ذخایر اورانیوم با غنای بالا به روسیه را رد کرده و کشور ثالثی را برای انتقال آن پیشنهاد داده است
‏ایران انتقال ذخایر اورانیوم خارج از خاک خود را رد کرده و آماده است تا آن را با نظارت آژانس بین‌المللی انرژی اتمی رقیق کند
‏ایران آماده است تا ذخایر اورانیوم با غنای بالا را به سطح ۳.۷ درصد و ۲۰ درصد کاهش دهد
‏واشنگتن خواستار توقف غنی‌سازی اورانیوم به مدت بیست سال شده و ایران آن را رد کرده است
‏واشنگتن پیشنهاد پرداخت جریمه به ایران بابت خسارات جنگ را رد کرده است.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/4916" target="_blank">📅 23:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4915">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_JfenSXwcqdSdB6b1d5ClBCStukjBrlg06BRp2R2r7x4w_yRbVNs54LETRU_ZwGggCBL5OrZeappwlCgEh8OVurgFRvPMXJWBcf5iiseQ-gt9R8l3mdmBhglQjBZ2kvLtCcA_p4XpmoF8A50COjCVgdm2-p5v9oSTSKhFoeutqDeua_CCRdf6Vo-K4tlft5mn3l1Fk1edWWCFZ9STeXYoWqJI9NQabC7ZL5ZRrYk1wr5MOMKn-Y9pUdykvs9K-7NLTdwCF2662Myav3eoWjR5eGewFDkQfnvF79LWhOqPfMKj9LV3hlgW12PcGpG4v2Qu_LuXVA1Qel52MUTOaKwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏قالیباف : نیروهای مسلح ما آمادهٔ پاسخگویی درس‌آموز به هر تجاوزی هستند؛ استراتژی اشتباه و تصمیم‌های اشتباه، همیشه نتیجهٔ اشتباه خواهد داشت، همهٔ دنیا قبلاً این را فهمیده‌اند.
‏ما برای تمام گزینه‌ها آماده هستیم؛ شگفت‌زده خواهند شد.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/4915" target="_blank">📅 21:54 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4914">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‏ترامپ می‌گوید قصد دارد در مورد فروش تسلیحات ایالات متحده به تایوان با شی جینپینگ، رئیس‌جمهور چین، گفتگو کند.
احتمالا ترامپ قصد داره غیر مستقیم به چین این پیام رو بده که دست از حمایت از ج‌ا بردار!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/4914" target="_blank">📅 20:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4913">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
‏آکسیوس به نقل از یک مقام آمریکایی: ترامپ تمایل دارد برای وادار کردن ایران به امتیازدهی در مورد برنامه هسته‌ای خود، اقدام نظامی علیه این کشور انجام دهد.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/4913" target="_blank">📅 20:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4912">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">آتش‌بس به صورت باورنکردنی ضعیف شده، در ضعیف ترین شرایط است، بعد از خواندن آن ورقهٔ آشغالی که برایمان فرستادند که حتی خواندنش را تمام نکردم.  ‏باید بگویم آتش‌بس با دستگاه تنفس (وضعیت فوق‌العاده بحرانی) نفس می‌کشد.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/4912" target="_blank">📅 20:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4911">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : آتش‌بس با ایران در وضعیت بسیار شکننده‌ای است.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/4911" target="_blank">📅 19:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4910">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : آتش‌بس با ایران در وضعیت بسیار شکننده‌ای است.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/4910" target="_blank">📅 19:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4909">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ به خبرنگاران: «اگر اتفاقات آن‌طور که باید پیش نرود، ممکن است دوباره به «پروژه آزادی» برگردیم. اما این بار «پروژه آزادی پلاس» خواهد بود. یعنی «پروژه آزادی» به‌علاوه چیزهای دیگر.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/4909" target="_blank">📅 19:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4908">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به تندروهای جمهوری اسلامی: « آنها در نهایت عقب‌نشینی خواهند کرد… آن‌قدر با آنها برخورد خواهم کرد تا به توافق برسند.»</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/4908" target="_blank">📅 18:36 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4907">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به تندروهای جمهوری اسلامی:
« آنها در نهایت عقب‌نشینی خواهند کرد… آن‌قدر با آنها برخورد خواهم کرد تا به توافق برسند.»</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/4907" target="_blank">📅 18:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4906">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUo9O3vC0f_NuV9jzc6l9MKYlL_SEmDjJNc7tzFKO3lAxBfNFwQ9SmbKKv-2n4gu3cKy02vzcIz2n-_hD4h3Paz-zhCb7ffiOhguESjehe9UAjOFhmx_SUlxfeRYM1hQ0IrBJxnM-SXVmXBJdOiHH0oWwTb9mO81ANBu7Y4fI5nAYFMd4sV2m_rPx4a1_EYB4ZXX6jJJKEcOhOyudgqbBF_6lHfU5CbDnUuA0qKfyU4inIjM3MpcK3fAhTFbU-1dclbeWCmIHmuqP1j-RUZtuEy9v_78yb265SzijP27vJO4zy_W0i4ngqZWR4lH0QjHm6FO36e-gJNT68B8ZZok_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
روزنامه «گاردین» در گزارشی از ارتباط اسحاق قالیباف، پسر محمدباقر قالیباف، رئیس مجلس شورای اسلامی، با یک مرکز پژوهشی در دانشگاه ملبورن و سرمایه‌گذاری او در حوزه املاک در استرالیا خبر می‌دهد.
🔸
آن‌طور که در این گزارش آمده، او از طریق «اجاره دادن دست‌کم یک ملک در این کشور کسب درآمد می‌کرده است».
🔸
گاردین نوشته اسحاق قالیباف چند سال در ملبورن زندگی و تحصیل کرده و طی این مدت با بازار سرمایه‌گذاری املاک و نیز دانشگاه ملبورن ارتباط داشته است.
🔸
این روزنامه نوشته که اسحاق قالیباف، ۳۸ ساله، همچنین موفق شده بود اقامت بلندمدت استرالیا را دریافت کند؛ این در حالی است که کانادا دو بار درخواست ویزای او را رد کرده بود.
🔸
در این گزارش این پرسش مطرح شده که علیرغم اینکه قالیباف، از فرماندهان سابق سپاه پاسداران و رئیس سابق پلیس ایران بوده و به نقش خود در سرکوب و کتک‌زدن دانشجویان معترض افتخار کرده، فرزند او چطور توانسته از املاک در استرالیا درآمد دریافت کند و در این کشور اقامت موقت بگیرد.
@RadioFarda</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4906" target="_blank">📅 15:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4905">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsNr56xyzZsDaPUOCVMN403ECk4hTzePq8ifBiVO470A2fgRIdBV2wTse53aEd8WtZMWoOS72lEY_LzQy0fSMmdrbVWIG61v4QExaw-Ap9-o8uU8lEDlwLoluR6Umae-AFBUvwPLlbAMKUYZZwSbU0lydBP4ewXYoa4q352AFO3affhytUXum0VWkTVoD9ez-v8pGj9FB9xTJvwszni_SUZSZZ8UJEWct_6b3SduorABOtuf19qGj2n7YlNo0PtsxsP8lL5drrs858KNjeiXsGlCaZ8MF-THAWALg625o9FkHNAwDjybYJswmfFjIWQEs5Xxg9VvxbPR2JxKGdpHYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هشدارها رو جدی بگیرید</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/4905" target="_blank">📅 12:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4904">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwxzeUw6k80sjBVUOkc8krzz_WA6sGTucXjPmlokOz-aFm_cZKj9qsDW0zdfwvySigYT_WZs1CLB0nNBvHAepUGwkKJsrbQd1LguL9bJwfKHlL7DcJkCI1PpWpTZUhSV13w_TIiD8laUB1C3x0fdlgqF7YOSyF_woc81u1_CCgGetNagnXuGWUFyfWNViDNzYZy24JQcMcgrIyGdLpxnZuwlBVT60Z1ggpHoNeNBIQ37D-BsnCzoPtK-GyBPJOATC-DfI9SXQSDAlsRaWzkJydab_IigC39kv8-HQJPBHNAfbMolenWstGjhd5N0HCZQXO6pvhHPh9k7A8_LZFW8lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری «میزان» وابسته به قوه قضاییه جمهوری اسلامی از اعدام «عرفان شکورزاده» با اتهام «همکاری با سازمان اطلاعات مرکزی آمریکا (سیا) و موساد» خبر داد؛ اعدامی که در ادامه موج فزاینده اجرای احکام مرگ در ایران پس از آغاز آتش‌بس میان جمهوری اسلامی، آمریکا و اسراییل انجام شده است.
لعنت به جمهوری اسلامی</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/4904" target="_blank">📅 10:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4903">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pg_xnKTWcgdKXADLW_yMclp56QnNcj6kK9X1DIRznUvcm6WeBDxBk58BGQAIFbsf1d7DWt2nM3jJ09TcrMQMLPpZzkprUIifZP6Wr9iLSiALHx1RtxI8jjq0QkexO3Pp8mUnlw72mRiLHGmFUWTvzRHo02D2PqTQFMU2GC9tp7Re00xqIF0jybWyCDs5oVIy_c2FWSW03JV0VlGz4HpzMsuoorlS4gOSTmvUnUtcwYGF8OHEtLDRBiNFvCBduEn55Shwd-kAkMsOw5OODVrlMdgOVS7Tvp2qhjqP26SOeCSasKoXaut2-p5drEKShC_UqzGUPW_I2ZuxDwsujyg5kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به اکسیوس :  پاسخ اخیر ج‌ا را دوست نداشتم. کافی نبود!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/4903" target="_blank">📅 23:48 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4902">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پاکستانی‌ها ۴-۵ ساعت پیش طرح پیشنهادی جمهوری اسلامی رو تحویل آمریکا داده بودن.  مشخصه که ترامپ از طرح جمهوری اسلامی راضی نیست.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4902" target="_blank">📅 23:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4901">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">پاکستان طرح را برای آمریکا ارسال کرد.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/4901" target="_blank">📅 21:47 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4900">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
دونالد ترامپ در تروث سوشال:
«
ایران ۴۷ سال است که با ایالات متحده و بقیه جهان بازی می‌کند؛ فقط وقت‌کشی، وقت‌کشی، وقت‌کشی!
و در نهایت وقتی به “گنج” رسید که باراک حسین اوباما رئیس‌جمهور شد.
او نه تنها با آنها خوب بود، بلکه فوق‌العاده با آنها رفتار کرد؛ عملاً به سمت ایران رفت، اسرائیل و همه متحدان دیگر را کنار گذاشت و به ایران یک فرصت تازه و بسیار قدرتمند برای ادامه حیات داد.
صدها میلیارد دلار پول، و همچنین ۱.۷ میلیارد دلار پول نقد سبز، با هواپیما به تهران فرستاده شد و مثل هدیه‌ای آماده تقدیم آنها شد. تمام بانک‌های واشنگتن دی‌سی، ویرجینیا و مریلند خالی شدند!
آن‌قدر پول زیاد بود که وقتی رسید، اراذل و اوباش ایرانی اصلاً نمی‌دانستند با آن چه کار کنند. آنها هرگز چنین پولی ندیده بودند و دیگر هم نخواهند دید.
این پول‌ها داخل چمدان‌ها و کیف‌ها از هواپیما خارج شد و ایرانی‌ها باورشان نمی‌شد چنین شانسی آورده‌اند. آنها بالاخره بزرگ‌ترین ساده‌لوح ممکن را پیدا کردند؛ در قالب یک رئیس‌جمهور ضعیف و احمق آمریکایی.
او برای رهبری کشور ما یک فاجعه بود، البته نه به بدی جو خواب‌آلود بایدن!
ایرانی‌ها ۴۷ سال است که ما را معطل نگه داشته‌اند، مردم ما را با بمب‌های کنار جاده‌ای کشته‌اند، اعتراضات را سرکوب کرده‌اند و اخیراً هم ۴۲ هزار معترض بی‌گناه و غیرمسلح را از بین برده‌اند، و به کشوری که حالا دوباره عظمتش را به دست آورده می‌خندیدند.
اما دیگر نخواهند خندید!
»</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/4900" target="_blank">📅 21:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4899">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kh1q1d5fbfRp0eGC8m-4iCBJy9JRkrGuRTXxKPcMmelQmLb_044EsXGkGhB_BxzA1O9YO7O7xLi7aEFbceBc-ZZRzjk2kycFgD7q_M3PxUromeMfz18U90PlKGxk0wLUhAV9rSswEhb7R1_Jq1NtQfbmChmRJzDaBH606mD_6LYqwrNqb0mtmCg_Ao5RWbeA8qVRDy-B0haXdjdkx5XPBo9yrIXwjEKTNBJl-1Nc1fY8RNS5M-q1v2BOaGhjEL7x04n8zsh4IFTj18bGWBk8exjcm0jyl3K0ybKGhem2iAzc8MJjv32vx-H_o4Gllqz4RyOWmzboxCrhyLxGhk357g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید براتون جالب باشه چرا کمونیست‌های ایتالیایی نخست وزیر ایتالیا  - الدو مورو - رو در می ۱۹۷۹ کشتن!
چون گفته بود : «باید قدرت رو با چپ‌ها تقسیم کرد!  اونها هم ایتالیایی هستند! نباید مانع شد که وارد دولت بشن!  دولت ائتلافی ایجاد کنیم اونها هم باشن!»  کشتنش!
کمونیست‌های افراطی کشتنش و
گفتن : برنامه داشت تا ما کمونیست‌ها
رو از مسیر اصلی که مبارزه بی‌امان
با لیبرالیسم و سرمایه‌‌‌‌‌‌داری است منحرف کنه و ما رو به فساد بکشونه! در حالی که وظیفه  ما «انقلاب کمونیستی» است !
و نه سازش و شراکت با سرمایه‌دارها!
و‌ همین چپ‌های افراطی (در ایتالیا، آلمان و فرانسه)  که به خاطر مبارزه با سرمایه‌ داری به کشور خودشون رحم نمیکردن و دست به بمب گذاری و قتل و.. میزدن، بزرگ‌ترین حامیان فلسطین شدند (چون اسرائیل طرف آمریکا بود)
چپ‌های افراطی آلمان حتی می‌رفتند اردوگاه‌های فلسطینی
کار با اسلحه و مبارزه رو یاد بگیرن!
کاری که چپ‌های ایرانی هم انجام می‌دادند!
خلاصه ریشه این داستان‌ها و… خیلی طولانیه!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/4899" target="_blank">📅 19:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4898">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736c3c8edd.mp4?token=t6GddzlbC37KcJjQtwgTYEEsgSJbBcMNkWrsOifVtc_3ltb-BhSaTeQFcl24oZsF84TQIn6pO61OW_oaHQVuZ7UIHOcRGZusG256QP87r7bh7wnSzrhs8xiBH5pYx7DBXa6-BD7nI08eiyVbxVSRdky-yw16itoSyWNB64fprhMRC6Ku4l7MvV2TVRyNmK0qv5hbeQAtKEaUKo9fXxsALTchsiUocaurrgFMQCX04Of9YhAzKMbWkQilZJg4aomWNFFAOQKw8hyb7zLWZoAn-6hA6S3167zdAEn_YQPNDG2BOtAf-L0mLAFbbNTyaFoDqlhs3anMmSmXMH9s-qrYsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736c3c8edd.mp4?token=t6GddzlbC37KcJjQtwgTYEEsgSJbBcMNkWrsOifVtc_3ltb-BhSaTeQFcl24oZsF84TQIn6pO61OW_oaHQVuZ7UIHOcRGZusG256QP87r7bh7wnSzrhs8xiBH5pYx7DBXa6-BD7nI08eiyVbxVSRdky-yw16itoSyWNB64fprhMRC6Ku4l7MvV2TVRyNmK0qv5hbeQAtKEaUKo9fXxsALTchsiUocaurrgFMQCX04Of9YhAzKMbWkQilZJg4aomWNFFAOQKw8hyb7zLWZoAn-6hA6S3167zdAEn_YQPNDG2BOtAf-L0mLAFbbNTyaFoDqlhs3anMmSmXMH9s-qrYsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به مارکو روبیو در وزارت خارجه ایتالیا
سند و شجره نامه خانوادگی‌اش اهدا شد.
خانواده مادری او ایتالیایی است
(از منطقه پیه‌مونته - تورین)
و خانواده پدری او از اسپانیاست (سویل)
او کوبایی است.
در این مراسم گفت : از طریق یک اپلیکیشن ایتالیایی تمرین میکردم. همه رو متوجه میشم! (به خاطر اینکه زبان‌ خودش اسپانیایی است، متوجه میشه
و نه فقط ا‌پلیکیشن و تمرین ایتالیایی)
هر چی وزیر خارجه (ایتالیا ) میگه متوجه میشم.
اصلا نیازی به هدفون و ترجمه نیست.
دفعه بعد که اومدم ایتالیا، سعی میکنم که بتونم
به ایتالیایی هم پاسخ بدم و صحبت کنم.
باید اپلیکیشن زبانم رو هم تمدید کنم.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/4898" target="_blank">📅 19:20 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4896">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jfi9cCpVdpdjqM1mH4FnraKBQtdYvN3NmflUR4Q1kZPVSutpHWhZ2ieH2-YADdpAvtXKk-nhCoQ9R9jtqOccpq3nyRXDkMkW1GWFJPiMB5RNTYCBOceYuB8-waNHEL5bZvajp-zoiAAbNUKboAt4bskWVqPpZVZAigVmtVTSLsYZ-pKpidcE2yRfv8U7A0RMulkNQtT-ehvWKv1Oszs7b_JJlpvxc97IZAlrTz6a62c_6jJeKRc5ciYXzz3pybmCBp7cBdyvJSOcryxVeF86JAugZy8F2PwqhsS4tlYrH1U4GwZ1do2lSCK7O9LZweP7uVhZt43fBxrkBg6qUSNQTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p5PBVGiCWxT1NZ603E-lWiHvR7zCWaVnFhyN0srRCe8O0032Vo8zC09LOdhVnG4kA5ctNfW30324p63FGVcIbaYl2TOXNYKN2bY_dmyc37keH9VgiGY4p6Ea7s5L2oddCqvTTbpkCr2sM3Ie-gPsFNr0uQpnlWmcWXHBNZv5389kLN77ciJVq3IAD0g_v26F2CsLUE99MKk_gmuv7JwBageEHYd4I-aHICnNsBib7cJSPXKmlyT5SSo_Q50vrjP9DFNaubJ6wxrmciTkT9KfG5FnARXKNNy4PFMDEQLrPyEnHwPNT9D3KnmY-oKueqPBItwF00voxLEvfXLTARPjOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معاون وزیر خارجه جمهوری اسلامی :
‏مقامات فرانسوی اعلام کردند که ناو اعزامی آنها ماموریت مین زدایی و اسکورت کشتی ها پس از بازگشت آرامش را برعهده دارد. به آنان متذکر می شویم که چه در زمان جنگ و چه در زمان صلح، صرفا جمهوری اسلامی ایران می تواند امنیت را در این تنگه برقرار کند و به هیچ کشوری اجازه نخواهد داد در این قبیل امور دخالت کند.
‏بر این اساس، خاطرنشان می شود حضور ناوهای فرانسوی و انگلیسی و یا هر کشور دیگری برای همراهی احتمالی با اقدامات غیرقانونی و خلاف حقوق بین الملل آمریکا در تنگه هرمز، با پاسخ قاطع و فوری نیروهای مسلح جمهوری اسلامی ایران مواجه خواهد  شد. از اینرو، به آن‌ها موکدا توصیه می شود اوضاع را پیچیده تر نکنند.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/4896" target="_blank">📅 18:37 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4895">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/126410d252.mp4?token=p4ljMuSK4cfpjxHAqgxqtWcSOu_ArvSgQzzlzJtkFq30fFyWsoVpeIPrCSrqET2tHeHyBEbDioIr3LPq66m1kQ1nicWsFYmtWGzf3SxUyMSJDqe38EcFw_jlif2x0l6RDz3Dlkgd3nVZEasd0FlMJp7BUprVGHM-YKFl4yr2QEZiGVYOnBUVRAsigfop6Jg4kBKkBeHZbjqrisuNF94Wv55nzfQ4Eadw_QXLIgGC6WbSoESF3MVDcAVN5q2zegltlFpqUtC24gGu5X7i4FcQ0T-VqwsA5TogySY2yagSJ1tsoM60Z_FGFjIz-ELs4Sjw9g0cF3NXShFJQ6JLOV7a3zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/126410d252.mp4?token=p4ljMuSK4cfpjxHAqgxqtWcSOu_ArvSgQzzlzJtkFq30fFyWsoVpeIPrCSrqET2tHeHyBEbDioIr3LPq66m1kQ1nicWsFYmtWGzf3SxUyMSJDqe38EcFw_jlif2x0l6RDz3Dlkgd3nVZEasd0FlMJp7BUprVGHM-YKFl4yr2QEZiGVYOnBUVRAsigfop6Jg4kBKkBeHZbjqrisuNF94Wv55nzfQ4Eadw_QXLIgGC6WbSoESF3MVDcAVN5q2zegltlFpqUtC24gGu5X7i4FcQ0T-VqwsA5TogySY2yagSJ1tsoM60Z_FGFjIz-ELs4Sjw9g0cF3NXShFJQ6JLOV7a3zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رهبران آنها رفته‌اند، تیم A رفته است، تیم B رفته است و احتمالاً تیم C هم رفته است.
‏ما با افرادی سر و کار داریم که قدرت خاصی دارند. خیلی جالبه
توافق می‌کنند و آن را زیر پا می‌گذارند
و دوباره توافق می‌کنن و زیر پا می‌گذارن.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/4895" target="_blank">📅 18:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4894">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‏
🚨
نتانیاهو در گفتگو با ۶۰ دقیقه :
جنگ با ایران تمام نشده است زیرا هنوز اورانیوم غنی‌شده‌ای وجود دارد که باید از ایران خارج شود.
هنوز سایت‌های غنی‌سازی وجود دارند که باید برچیده شوند. هنوز گروه‌های نیابتی مورد حمایت و موشک‌های بالستیکی وجود دارند که می‌خواهند تولید کنند.
ما مقدار زیادی از آن را تخریب کردیم، اما هنوز کارهایی برای انجام دادن وجود دارد.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/4894" target="_blank">📅 18:12 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4893">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
‏ترامپ: «ما هر سه رده رهبری در ایران را از بین برده‌ایم.
ما ممکن است دو هفته دیگر به اقدام نظامی علیه ایران ادامه دهیم و به هر یک از اهداف تعیین شده حمله کنیم.
ما اهداف خاصی داریم که قصد داشتیم در ایران به آنها دست یابیم و ممکن است تاکنون حدود ۷۰٪ از آنها را محقق کرده باشیم.»
‏ترامپ درباره اورانیوم غنی‌شده در ایران گفت: ما بالاخره به آن دست پیدا می‌کنیم، ما آنجا را تحت نظارت داریم. همه‌چیز تحت نظر است. اگر کسی به آن محل نزدیک شود، خبردار می‌شویم و نابودش می‌کنیم</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/4893" target="_blank">📅 18:09 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4892">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
از طریق پاکستان: پاسخ جمهوری اسلامی به متن پیشنهادی آمریکا ارسال شد  ایرنا :«بر اساس طرح پیشنهادی، در این مرحله مذاکرات متمرکز بر موضوع خاتمه جنگ در منطقه خواهد بود.» [و‌ نه هسته‌ای و اوانیوم و…]</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/4892" target="_blank">📅 17:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4891">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
از طریق پاکستان: پاسخ جمهوری اسلامی به متن پیشنهادی آمریکا ارسال شد
ایرنا :«بر اساس طرح پیشنهادی،
در این مرحله مذاکرات متمرکز بر موضوع خاتمه جنگ در منطقه خواهد بود
.»
[و‌ نه هسته‌ای و اوانیوم و…]</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/4891" target="_blank">📅 16:27 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4890">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-rfdyEaczPbP7wja8oFc8G4mfb71RMWrV10pWo654S2RrTrkuwEg2qRJr0S3Dv-41zxcPcn_hoCT4yi8Pys6_jIDZ4T1gPBxKxXXq2IuJtJcthoyzvRIVh2LFDA_bmdjpBvktZbbC0P2v1aMS06dsegug_Jo7b32aTxe46L2yGYlIOm1gkxbJf_C5P6QD6eCx9ECp_vVqxT4vjDufmBC2KlX47oD5VhQcXhC6g7Ro09kKyM3m9Om66ngZ6pD78PQ3Sg_aCcv42eIq6QeT4Oc2ld1BDoajpJCoIDdvDOFD3LFLc6Pi90uS8F-JYsggwWRd3hu7WBtl9k1f36PGQmnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابراهیم رضایی سخنگوی کمیسیون امنیت ملی مجلس جمهوری اسلامی</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4890" target="_blank">📅 15:39 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4889">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
وزارت دفاع امارات : حمله با دو پهپاد به امارات و دفع آنها</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/4889" target="_blank">📅 14:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4888">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
‏وزارت دفاع قطر: یک کشتی باری در آب‌های سرزمینی این کشور در شمال شرقی بندر مسیعید، صبح امروز هدف حمله پهپادی قرار گرفت.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4888" target="_blank">📅 13:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4887">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
‏وزارت دفاع قطر: یک کشتی باری در آب‌های سرزمینی این کشور در شمال شرقی بندر مسیعید، صبح امروز هدف حمله پهپادی قرار گرفت.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/4887" target="_blank">📅 13:14 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4884">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVWzbfVPtX-PhDuY5CLXaBhZh2vzkezPVJKzXnZnwZ6vo3u-u_FVuG40NDG0UFosbmFW2rawEpRzoTauWk-52g-fXSPbjwPwBe6-KV5C8lhgeY-Pc0i5fsloxFyIMJjARWq38__CIjNBNGateDig7l5tP55wXJPpjveYDmFM30NlroUONyWCcWJNYIsoG1RYzLWxxv5H_HAGxr0VG3AGApI9JsSso3lV7ftJQgQHgwcPFcTUZ5esdD5JqS23yJP1AZigibNitJ_ystMK0JmQHiQpG1jN6ZCRIJvYFPof-sGTN9-sxvvZ6RDmBAW_A0QJM-8kKxT_coKVw5HMCCeYiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۹۰ سال پیش در ۱۹۳۶و در آستانه برگزاری بازی‌های المپیک برلین در آلمان نازی دستورهای خاصی صادر شد.
مثلا گفتن که دامن زنان در این مدت
می‌تونه ۵ سانتیمتر کوتاه‌تر باشه،
گفتن یهود ستیزی باید کاملا متوقف بشه
که وقتی خارجی‌ها و خبرنگارها میان،
بهشون بگیم این حرف‌ها، فقط تبلیغات
دروغین خارجی علیه آلمانه و واقعیت نداره.
یا مثلا دستور دادن، بخش زیادی از نظامی‌ها و پلیس،
با لباس مردم عادی توی خیابون باشن تا جو پلیسی و نظامی به نظر نیاد و عادی باشه و نشون بدیم آلمان نازی اصلا با تبلیغاتی که بیرون آلمان میگن واقعیت نداره.
حالا توی جمهوری اسلامی این چند روز
زنان بی‌حجاب رو ویترین کردن! و طوری وانمود میکنن انگار ما اینها و سوابق شون و دستهای خو‌نین‌شون
رو نمی‌شناسیم.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/4884" target="_blank">📅 10:12 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4883">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‏ایسنا - فرمانده نیروی هوافضای سپاه: موشک‌ها و پهپادهای هوافضا بر دشمن قفل شده و منتظر فرمان شلیک هستیم.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/4883" target="_blank">📅 23:41 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4882">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvBhT2IxUVGvoF0NZBtcALo9ZGiefT4rZok9TBSNmjunZMAYW_tQ1OuinAIUKO4fnwXXNuABwWHKp1h8NsM5B6vbUbF0IK9i1MGopw9iVQd7jlVxeI8sRTKoPs8MUzBf7ZBiWxl52KV4Wkj0ts6GT_QAk8LpQRu9LzTn0V-uF7z0Jnp6BGuZOtpMQfUOWQ2CcSm5laePL1KR5JBdt-joFdUFfURyBeinyQPRBn2KikcvoghaiSWrXfKXcZVwg-seVPcBoWSdJn4pOhwiqElXCW-SuyN0sWyFwh1iEw8-DeMlhAynvpp2c3pQw3uwEvJSSsr5r84dvSMd2BobWYEkxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/4882" target="_blank">📅 22:35 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4881">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AChuH90xUDsTDGm5c55IMap2XofuZGLBngO0-2l2b43szNSGY1gwtD2WPOEvapIUYcu9xysLooXOoWMb4kIcIXSnZwp2MjToMBOwa7LQx2_KAxK0sObEXl-lolWaSsyBlh327h2gwcDndJHxLMOl86nUo8Ltb7Of1S6Ir70O40yfRn62KHlNCVwhSBQDn7I0SNpFID5oaelNxKd1ZORH2sGSLnzaNLm4oUTlhqbAwsIRSN-PHr4Sr8CgyIl6Dk1MSq3SI6urE79Q3i-5aZGxWF4gFKclTzVE1A4cM0nVyyUQAayGqI_wsmrsx9mYmN_JJUBAZf_RV24in-X-LZvQFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با شرایط پرتنش منطقه، رویداد «در امارات بسازید» در ابوظبی برگزار شد و شرکت‌های تجاری نزدیک به ۴۶ میلیارد دلار در امارات سرمایه‌گذاری کردند.
بر اساس اعلام اوپک، این رقم بیش از مجموع درآمد نفتی جمهوری اسلامی، ۴۵.۳ میلیارد دلار، در سال ۲۰۲۵ میلادی است.
النهار گزارش کرد این سرمایه‌گذاری شامل صنایع دفاعی و تکنولوژیک، دارویی، شیمیایی و انرژی است. این رویداد چهارروزه حتی در شرایط جنگی تعطیل نشد و توانست جایگاه امارات را به عنوان یک قطب صنعتی در منطقه تقویت کند.
https://iranintl.com/202605091828</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/4881" target="_blank">📅 16:01 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4880">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odNsV5rhPZVEHyQ29E_q8IUpL4SBJFzxQ3Ai14c_mMgdmhNlanmJPXcPHH1dFVawMeWsg_aM0EkYjfKj9jU6WAPVdPH0abkYDITWdBxMISsM5F5k9EOqWTjpzXSABjgobNrpze-joC4xjRHpmdz7LxEGOG0LdfCOiZDMjSafH1f-s1lOhQsSgsJPUAYJmn9iQu7W6S-X9xDk1CwdzgyyXw6tmm9SEb85y22O2fxGifRyI9Z7alR0hIkBZ7X3YQYq5CWWpS5u1fwUSaQcCZ0KzmKSqeUDY6_wm4a3W-UYm_eb5aOCpGKGrG0L4kpDRZPz51EmOA2C_zeH0YutO01SYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات ‌دست به اخراج گروهی از شیعیان پاکستانی مقیم امارات زده که برای جمهوری اسلامی تبلیغ میکنن.
🔺
امارات چند سال پیش یک وام ۳.۵ میلیارد دلاری
هم به پاکستان داده بود، که چون پاکستان
آه در بساط نداشت، هی تمدید می‌کرد،
که بعد از خودشیرینی‌های پاکستان برای جوش دادن معامله بین جمهوری اسلامی و ترامپ، امارات بهش گفت سریعا این بدهی‌ات رو پرداخت کن!
که یک شوک عظیم روی اقتصاد پاکستان ایجاد کرد.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/4880" target="_blank">📅 12:23 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4879">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">مارکو روبیو : ما در خصوص لبنان فقط با دولت لبنان مذاکره می‌کنیم. لبنان ربطی به جمهوری اسلامی نداره.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/4879" target="_blank">📅 19:12 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4878">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiuiabuTfxYWC0OFlBGCP4HFoZKq_cS910u4kEqeRYFZBqIalVBRH2UdMqOHTwo0Ha4taWKEqrWDA2_w3nbmgVHaslNxzaMhWLtty2T0qkqENi5Xvw1kU2Xp-I8C0jM9j4rkP_mWWRONdAUSCwfQUtaNDyngQT7q7NELIvRNrBP57KlWNSPmVrz042AvkO5BUORrK650I-61eBO3MHItdRm29hqe9p5zYrq-x-mEbfjytmqoGDYy_AXUbwlSPgCn1upTg9NKrDVCVB6vqHohDPJ0skOZIAo8M1oPIXhxW0Fy9VNdsBm_Kr0NsDWZ0ZsghY-EmGmdp5nGlBMJZjEeBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ملت «مبعوث» شده :))
این هندونه رو  این چند هفته حاکمان
جمهوری اسلامی زیر بغل عمله‌هاشون میگذارن!
که منظورشون چیه؟ مبعوث/ برگزیده شده برای مبارزه با آمریکا و اسرائیل!
«قوم برگزیده» لقب معروف و شاخص قوم یهوده! برگزیدگی هم از سوی خدا بوده!
اینو فقط تورات میگه؟
نه! قرآن هم اشاره داره بهش:
سوره بقره، آیه ۴۷:
يَا بَنِي إِسْرَائِيلَ اذْكُرُوا نِعْمَتِيَ الَّتِي أَنْعَمْتُ عَلَيْكُمْ  وَأَنِّي فَضَّلْتُكُمْ عَلَى الْعَالَمِينَ
«ای بنی‌اسرائیل، نعمت مرا که به شما عطا کردم به یاد آورید، و اینکه شما را بر جهانیان برتری دادم.»  بخش بزرگی از کینه مسلمانان به یهودیان از  شدت «حسادت» میاد!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/4878" target="_blank">📅 18:46 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4877">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgxjeX1ne5mRjgl9Pjq_HfKazeE4TNcotXIDzT5L8T5t-vurO8gpov8wl_PTRHpKv0H2dkoKnv7tSqxORGU82TOsG0pYBL1Frl846A4_Tyud7-_8tbFRrxjtW6lPLr6tq03UirjPbTEEXjNqGYKP7gPV3D33dVDm1-ymA6bFeE1lLEjMGbFOZ_NYy1gfb1wdeo2vfwKifRNxZ0lyzIDu0nC4g4VICvbttHmgQ-uR6wq7gSLZZauI3i0T_2fJnDeRjah7jTYiBDsUTJhMDAmGImR7MgZlwPhrWxLKIczWliLN5t2bjPtfsTrfOqr2DP8L5qi93orRoIikwwQGe_zOpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط واسه اینکه
روزنه‌ای متفاوت داشته باشید :
در قرآن بیش از ۴۰ بار واژه «اسرائیل» ذکر شده! اما یکبار هم اسم فلسطین نیومده! حتی به روایت صریح قرآن (یعنی
آیه ۲۱ سوره مائده
)
موسی که به‌ دستور خدا رفته بود قوم بنی‌اسرائیل رو از مصر خارج کرده بود و آورده بود تا «سرزمین وعده داده شده» (فلسطین) رو بهشون بده، میگه : « ای قوم من! وارد سرزمین مقدسی شوید که خدا برای شما مقرر کرده است، و به عقب بازنگردید، که زیانکار خواهید شد.» !
يَا قَوْمِ ادْخُلُوا الْأَرْضَ الْمُقَدَّسَةَ الَّتِي كَتَبَ اللَّهُ لَكُمْ وَلَا تَرْتَدُّوا عَلَىٰ أَدْبَارِكُمْ فَتَنقَلِبُوا خَاسِرِينَ
بله! پیامبر خدا، موسی، به روایت صریح قرآن ، به قوم یهود گفته وارد این سرزمین «
مقرر شده
» «
از سوی خدا
» شوید
و خارج هم نشوید
!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/4877" target="_blank">📅 18:32 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4876">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‏
🚨
🚨
🚨
خبرگزاری فارس:
وقوع درگیری‌های پراکنده در تنگهٔ هرمز
‏از ساعتی پیش درگیری‌های پراکنده‌ای میان نیروهای مسلح جمهوری اسلامی و شناورهای آمریکایی‌ در محدودهٔ تنگهٔ هرمز در جریان است.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4876" target="_blank">📅 17:50 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4875">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مارکو روبیو : «انتظار داریم که جمهوری اسلامی امروز پاسخ پیشنهاد توافق را بدهد و امیدوارم که جدی باشند.»</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4875" target="_blank">📅 17:39 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4874">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1pnwgQB21uvW8Oy73oujEOvdtuka8UrCPEQeHoKbnTYLf6Nd0c6Zxny1lj58yKeCZH3LNWUAZBZGue2wZ04Z045n9-QQmH4AxfLiiucIE3yBlb3h8aBrq92obG5xLZzED47TGVj9koTq8KPX3HmTPQ0tVAqwdis3q-jJPb2-5F9BESlshzpw4hD_VOJ14z7wzllCFw_K3BoPiSfg9NDZBbo0ddQNL8mdqOzK6dga8T7ZvggyU2UIZXYtBJfUuM3fvG10cSFpVhyC-6lTVG--_Pkht4b_10pdU31CG87P6TdtbIv6yPdN-NXDCdBDAr7_3TjDRCWyp0HLit8Z3AXSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«یه هفته وقت داریم که بزنیم
زیر آتش‌بس و شهر رو بهم‌ بریزیم»</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/4874" target="_blank">📅 17:27 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4873">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1KS3-zlAUbZvmyvx1tHgevMxLUV9qHJCTi6m9I2ace_69h491Wljjry217JRD2tqhhw--rAvYBzRu8W2eR7CO6gZJevUJm-8Vb6dJ2bst1wXolb1-VzARaXQudv9pQT5viSv2_dBF7IOslmlK_WVh8YNGjcs-Jhlbk55xcdQ1ZqJRh9WJnFbfAiILVMM3nBpKqgX4_bFrYuTL8gQlWOMxDBoH3BFtiGYiezFQtI_a7ejb3w6CncXamqHcqdDRgotmsgWSVzP-WtdWcNr6iYO6Rv8Yds_34BPiuFNzsBwRe45okFzSl-PWuaTkPYnVEX2BnNSEoafYHWN-bV6ycO1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهریور ۱۳۶۱ !
در بحبوحه جنگ عراق :
وقتی می‌گوییم اسرائیل را میخواهیم نابود کنیم، خب آمریکا به ما سلاح نمی‌دهد!
جنگ با عراق، مقدمه جنگ با اسرائیله
و با تمام مستکبران عالم!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4873" target="_blank">📅 15:32 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4872">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrkSelp8w-pSj5angcHOgi_T6jrzxLkO1rA8IevPenouK8hxDat8x3X1Xpnz6aJxUBQwzIziwMfC7wTNZZRoq-vpGo0YrxdDYgQzE2LK8RsKRr0CrstjBzz6TSmgUUav5gAYoWuQlU3lyY_0VlFeQ52IWt6e0uttLL0H1cLr5xBclMOAsR_Hch1379gyjOyi_lDwDwcCYCFRBFeXg7aQ15n_E9t4pXCeOpleZsRs8wPGiy6mRiv6K_RKIYL-hpJ4TMjKBRvF0YhyEt7q7GKcJtBypjdQtQzIrpcQ0Jtpoz51RnklSbMjHaMMpKUSP0AIB0p1SsiLt8ccgxAoC0yYCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکنون ….. حمله با موشک و پهپاد
به امارات</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4872" target="_blank">📅 14:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4871">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ex4Lk3qDaZUsJfWAdJPO1DrWBoH8hF_-QKIb83InoPFfksyAMkWWBlylPxBJuRgXWUCHCRV9DUjwrgacT270HWuIR4FD_DjJHEaGuXZHNh1lWxiw339KJ1TedQnQN18zo7nWFUlamFdGqgunlFWX6VS2Lgtukx_nbQtmm_4SzRMbc6diNxkWdlQ7zA9EJhjt-nLacB6v1AbbHs39Qgb8c2FAjiAwTu5Jcc-xc63W9E5Thh_m6fSbo6ZWNoNTtennvFspS5_Az4SroDOoZJ4lSp1yCjprm6vz6RmNgToZ77-n2QhM-wXo1s7b5dp-7lVqzel4OoZ5xdtsWJZDjqkZxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروپاگاندای کره شمالی
برای بچه مدرسه ای‌ها،
این ور موشک، اون ور موشک.
بالا : «رهبر ما شماره یکه!»
می‌دونستید جمهوری اسلامی
ساخت موشک رو از کره شمالی یاد گرفت؟</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4871" target="_blank">📅 14:51 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4870">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
جمهوری اسلامی میگه یک نفتکش رو توقیف کرده.
احتمالا متعلق به کره‌جنوبی است.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/4870" target="_blank">📅 14:07 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4869">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
رئیس جمهور مصر به امارات رفت،  یک اسکادران [ ۱۲ فروند] جنگنده پیشرفته رافال  نیروی هوایی مصر را برای حفاظت  از امارات در این کشور مستقر کرد  (همراه با خلبانان مصری).  رئیس جمهور مصر گفت :  «هر چیزی که امارات رو تحت تأثیر قرار بده، مصر را  هم تحت تأثیر…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4869" target="_blank">📅 12:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4866">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m63rzK733zjQJpfih5Z9dqe1p3gxAgGn0DEuytny0BvWBl3_cM7dx1q51eqFZBOp392uYFmUd9gSSnZQfstN_mzYHocuf6hdIfaedVpuwGMK7RQXwrOdDbRBIK8Q0GF2ec_re-ISSGs6IezYe6lfwjYOSafQQjAgtCSkvXDa1BqLZHBXGI7go8hPOJvIkQiev1wYdfgOTxfqpBZui7sJjN_0lwH24ldbUr1gAsTCKtLqEaQobCBs5dfe4xBJhMdpVPT1oDtXVa20ce-Ksmqp2VOgDwENPA8csQxlmGtWGNHFaAgrrQLw4TZGhuG9SCnuh-kWezHEB-ywtMdCm32wdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A15UqGDtp2pvq5RpDM5DD-lS0MXXoabZauFGiLu-Rnka5fEimCXY5O4eDT72yCQqVfepGqbXPHu9OXgSE0IdHPISBMY4KBPl4FcDnXCRrFW-4hRpZ25BXA3_1_zeMSjxa-rpojy1yZYC2-9BvtXiWURZyevtXbdcfFDqbvoCNfmFTketHM9JdWmsfsSXdiES4sRujwC_Xb5WpILziw0bOpNC9rXpYM4LNlv3Omkzkc0tOn8_QVeD61hzIyGt_nBVoCb1KuTeAcxirm7K7Mip8B1QdByf3GQECBkZAtnMM3IPZDqMsMveo-7mZorlHzpikElnlXtED5sxaJVGs5H-0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=Inh5bXWbBx_BGBFGnuNgT4pbMqn3v6whwcf9viG4ZCiUCTw9mDivSld6uIrceaI2-RzKMjGvqSNWO2OwcKLBXgZZEZs_E9tt4V1GUqIfP7S1iBLOZeCVL7fC2LLMCH3n8d65GQUfeL2DeOuA_zk9EHIgwBo7pqVczH1Nxn500JpvKP6k3pl9goQWP9n2QdqFmZ3txnPzlemETtzq9sZwg2R1bPoS78rM6KXIjLT3ZeetV-Z49gsQOja11gKMoQcIgLrqyPEF_wiJdivlx7blask3OPl98g8WqLNsw-GrQhV_a2jT8t-jNsxzqEF0mL5KSstzdy22KyV1kT9OD7IchA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=Inh5bXWbBx_BGBFGnuNgT4pbMqn3v6whwcf9viG4ZCiUCTw9mDivSld6uIrceaI2-RzKMjGvqSNWO2OwcKLBXgZZEZs_E9tt4V1GUqIfP7S1iBLOZeCVL7fC2LLMCH3n8d65GQUfeL2DeOuA_zk9EHIgwBo7pqVczH1Nxn500JpvKP6k3pl9goQWP9n2QdqFmZ3txnPzlemETtzq9sZwg2R1bPoS78rM6KXIjLT3ZeetV-Z49gsQOja11gKMoQcIgLrqyPEF_wiJdivlx7blask3OPl98g8WqLNsw-GrQhV_a2jT8t-jNsxzqEF0mL5KSstzdy22KyV1kT9OD7IchA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
رئیس جمهور مصر به امارات رفت،
یک اسکادران [ ۱۲ فروند] جنگنده پیشرفته رافال  نیروی هوایی مصر را برای حفاظت
از امارات در این کشور مستقر کرد
(همراه با خلبانان مصری).
رئیس جمهور مصر گفت :
«هر چیزی که امارات رو تحت تأثیر قرار بده، مصر را  هم تحت تأثیر قرار می‌دهد.
ما از امنیت و ثبات امارات حمایت می‌کنیم و تجاوزات ایران را رد می‌کنیم.»</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4866" target="_blank">📅 12:45 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4860">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fTaEpXOW7XoNaINpF4EwxZuGIs6MbgA2dZbdgRp7dA0UGJXxBiHKwMfAnMkKrsEt7UguNPERv7-GMMPbpWK9sjPIK8Iw3IJWOSbnbeuonZ2oCZV0fayDceLKSWO148NkCJ3NZAAlHdXFbt9jirknr0XhdOtb5jv5UYaJvX_fSsYS0gEs6K3ViBygv3i6X59c6lxdrqztVSQM4U3-XauHdx9GppURb_8nTxOKUJdQhMOFLg__qiOrdopxOqj9enVeoFsdEq2k46bwnxzorSdkLD5B_970Oq3_oYQhiFRAqMNrwFsMk8BxlSDgTc_O88q-rWux2C0Lb0c-_jcOIPAsWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tXWCQ4UBkN8PqMt08Ol8YGO1Sj9VXfLct53wRyPshQWXZ4C1XP-6IlPt1c-0luAzC5LCo8cmzyqo9Hs6ZzSjfpOyQUnSQ7jEvmYbohBuiC6Jmrg8n4rCRixWty-zq_FyhEeK1qaKixY1lUfBB9dVWJBVNoOEo9A04zDgphUj6yd7BbR_a6MjjfHX12DYiPGdbJ0l-dn8PWgqB_dPwlHb_dgJhbuqdwtvpedpiVQGYr1OEDBxem6o4eSrOtDllOOv_by7hJ-yoF0DbpB4-86P1LMsopfyL1jsK20Q_NikaW44EDBANOH1aQqpWF6srcTAfkjTyq2f16e934QrnkN37g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ktMmgrGTBWwK0sRXh-qDzzH7thn61YV7hz-u8NNyB_LRO56Scu-UZVYlBebznE9QiXJIKVPL_eyerI-8yRWz4mynH0fGRaOSWbpv-QjDmq9SmCgYWb_DgGOs5zZIjSlHsrNkLO0NXDNZ7cmmbvBIU4lyakHvZQFTeLu9Oe7iO3isjk9cxhHSj-ZBPi_Cw3a3-EYawJc8cZq20h-GGK_ofJwLZ7IagWoCY0Zks6RzvY1RVwnOJJdTUSvET8tM914sayhvBw-dV3QaZSdgclt4tvdIUZfg7O8Yi8Rbt3ay0oa7rcmYNOWsaruug0yyvhZCu5NpKffgRXgV0YDHYSw5MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fqwM0WhkkvsNUGJvJdWaJkPuEkXOu-IvW2dOe3vVyagEFmmBHWTLI8jbllN9N0uRPZ9FfEvcq8fU6T2XSn0DzkxD6cjTNY-7C6KANTWs7wgSKUnMRFcpVCREitbWZYYfK1dvZgvinfYtgoR4NJbbNcmBMXIcM6mU8-N3YXbENZEXRTYh3ae2pPYn1TGZedS91oN8ihpui5HS76YTTNKeSVdqVzQuF3EanXtVr1fU5R8GVvTrmHM3Pk-W0rimPSbc-IhhYFgBF2CdIVB6DdMS9LB7lg7Bvmqy_6t7MsChIGCcfvMPIQWpe4A97Hd3PjdddK-cXQZxGHMEDH9nSJraNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SvNPG3wtmCVqr4LiNqFaoB5omH1b0S0XTQ5ma8ILOzi4dahLY9I0OGrNOFvdYgZXo6QqaP4YqGCSzSJMMdsj2pe69agMkFyAspqpjNiV755_C8q9Rd5SDUo80wUo8A8QuacPRhUK6_vj-ZjGvodwyL4kLX1wcv_8SxchyOe4-HH1LOj6Bh-T9mavjij-wPtKO34fQDFMpOovOwCDlhDA-itPvpb_T2o2nyUJmmYViVh28qyPpcJRrsN_Lsci1SzJ6Ns_5V67ndsc0uZcmAmTB9OEqHBZGLwEFBes06JauUVB3zjJnmkLOXBOiOCQZyTLWeBP0r1NK7q6UrgtIZz3Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/plnqlGwd65KvtmTZA6CY6TNGs3LZfZHwDdRY9qdt3bKTj7rKtAEMKBZXiaKU0T2184HOodGWhYL0wdD9FKrzc3qEoj5-qqNJtF6K0mhNjep8a-LmzecyxvpC4j5CQe9WIng1Qqt9_1_EopRwU4ZpefNToyhHDuFCEJXMbGplCdwO-BLySpQNizl1TEEk6Mp4ECJO1vVXqvI6-OkpU4B6Wr7rA9Umixfl2f3HE1iUSyoDj2ftGofWlgPKEyLinUx5NDKvNtdHZy2WKh91uKfc4k2FKNB8UuqtQikq0kFdDcRl02YwqS7C0jzznDoktXdWZteoEBzdr8o72BWmz9N7Hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">موج تبلیغات حکومتی‌ها علیه امارات
اینها از اسرائیل بدشون میاد، چون اسرائیل به کشورهای کوچیک همسایه اش حمله میکنه و به خاک اونها نظر داره.
اینها ندارن!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4860" target="_blank">📅 12:34 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4859">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwivpSJoyzWpQ01DsQM8iiAlsqj6Zxi6g0tl9Xe1lhzbm0CYLaQBQUbkRH452hS-429vNzF8tMaW2nqpBBPo8fAZGQjAnPry0B4imtiGL5h4gxVqTq-jy43aW0KUBEyoHMYfp67hIv-kH5Vr8nFOI6iNTgVx8Hw-gimbdlXSrH3fPyyGLR0Q4pCXs7i2F9WDaculdZgCTJBxOyntqUyZWb_kGlv2UgeGwex7wKd3q3RaqnlIcN7HTk7QQxV2hU90yZmrbg6qW-FTz18WcPx2wNBTtgoHd5q2suISfp3DJqI4JW-kq_Z3N3uuSi34a_2AWYL0Tqm-CP5azySCCyassQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
🔺
سه ناوشکن آمریکایی درجه یک جهان همین الان با موفقیت زیاد از تنگه هرمز عبور کردند در حالی که زیر آتش بودند. به این سه ناوشکن هیچ آسیبی نرسید،
🔺
اما به مهاجمان ایرانی خسارت عظیمی وارد شد.آنها به طور کامل همراه با قایق‌های کوچک متعدد که برای جایگزینی نیروی دریایی کاملاً سرکوب شده‌شان استفاده می‌شوند، نابود شدند.
🔺
این قایق‌ها به سرعت و به طور مؤثر به ته دریا رفتند. به ناوشکن‌های ما موشک شلیک شد که به راحتی سرنگون شدند. همچنین پهپادهایی آمدند که در هوا سوختند. آنها به زیبایی در اقیانوس سقوط کردند، مثل پروانه‌ای که به قبرش فرود می‌آید!
🔺
یک کشور عادی اجازه می‌داد این ناوشکن‌ها عبور کنند،
اما ایران کشور عادی نیست. آنها توسط دیوانگان اداره می‌شوند و اگر فرصتی برای استفاده از سلاح هسته‌ای داشتند، بدون تردید این کار را می‌کردند اما هرگز چنین فرصتی نخواهند داشت و همانطور که امروز دوباره آنها را شکست دادیم، در آینده بسیار سخت‌تر و بی‌رحمانه‌تر شکستشان خواهیم داد اگر سریعاً توافق خود را امضا نکنند
!
🔺
سه ناوشکن ما با خدمه‌های شگفت‌انگیزشان اکنون به محاصره دریایی ما می‌پیوندند که واقعاً «دیوار فولادی» است.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/4859" target="_blank">📅 09:00 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4858">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPvhjdOOE5D3CMVcoSihX5wd6b91DX1vII9Vd_ixbbk_EwoCJCoXGSc5V4HRettuNn5LX0qHlXVBlOJa73OqQcg4kjkJLPUBpQfjBBKtBM8D_z9xd1blKHkbjJzhwIc6PVdtdyXpOIOGVREAj_KJrACqDs3qgAfAvel7mL3qcODcXgcW4nxOMQVOMs0faiXiw-RM6Aw8YVmM7Jk8rXA9o89qotyEMbD3iUc4Mm3pVwEvT0ZbzPPt-SWv05CZOFEFeqLxvVnatI6mSSmyX8Np5PHP6Y6_mC_6x_2ZYdU5YqqbSghyImZ8Zjylj_umUMtOg_Pc5c5SNnGiHlkYrgPxsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4858" target="_blank">📅 08:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4857">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/maXnxs49OnlQvoxOnJEHuFV2L1hO4fGnC2AimK5PN0YgdL-m_bLWoObxyPSf_N7CRT9BGy2KuEogp1DrJ7FBd4Go1CvdxsZ9ihcTq7-3CCdvX2kPDVDhmrolSoHQbxVjvNG5RIcZKzWXoc6UeW-Gd1AtCQ9DMHENlbokcYG1D28JytubMx7sUdxdky5wY49O5pED74N6u09WtXLzRIFg-pyZDUcoepZAfqhXF2rtry6QW_uxXo_48YPBAt2yEHOiBx2d27UzY0wxPTX9pB5bHvqDy7Sbp6My1Tmp3oagomY9roKTPzY5K7yMcq-jwqIlhB4NILMTyWyG9mGL1kqWRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیانیه سنتکام : سه ناوشکن آمریکایی در حال عبور از تنگه هرمز به سمت دریای عمان بودند که جمهوری اسلامی به آنها با موشک و پهپاد و قایق‌های تندرو حمله کرد و آنها نیز به حمله پاسخ دادند.
سنتکام در پیام خود افزوده که به محل پرتاب موشک‌ها و پهپادها و همچنین به مراکز فرماندهی و کنترل و مراکز اطلاعاتی، شناسایی حمله کرده است.
بیانیه تاکید می‌کند هیچ کدام یک از ناوهای آمریکایی مورد آسیب واقع نشده است.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/4857" target="_blank">📅 01:11 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4856">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
تداوم درگیری های نظامی
🔺
گزارش‌هایی از حمله به بوشهر
🔺
گزارش‌هایی از فعال شدن پدافند در شیراز
🚨
حمله آمریکا به میناب</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4856" target="_blank">📅 00:58 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4855">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXyyjyqIs-p80aIUl4RO1uCcy7eLER8E2x166wB3_PR2U9-KVJPhCtrbwdfKHZ3SKJVYZtn4kRL387i_QqVQLh3yuDB73vWWDlr5PHTDjPLzDbr19O1iN3C1IEKmjNH6wxlR0RXjw4GSdf9h9b2kLD07SvX82nSAAi9Gb6XgCH9A_CFJ-HyeCtRE1-7nkE2ukFyaXqmZMZ3xOgz_XjrV4XCcgaLF7LJrNF-ye5EBkKJe0BcMTbc7rMxu53py1r3FMUPzdShA2H425KmuO_CKFx222-G5MmC_iQW_PluV3yUQnjkQ_E_P_ORMHNHAcaJnX7qqdy6HuaJgOW4VUrbq9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: با تلاش شهدا قیمت نفت رو بردیم بالا و به یک دستاورد راهبردی رسیدیم،
ولی با یک خبر باراک راوید در آکسیوس [ که خبر توافق بین آمریکا و جمهوری اسلامی رو زده بود] قیمت نفت اومد زیر ۱۰۰ دلار</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4855" target="_blank">📅 00:49 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4854">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
‏سخنگوی قرارگاه خاتم‌الانبیا:
‏ارتش آمریکا با نقض آتش بس یک کشتی نفتکش ایرانی و در حال حرکت از آبهای ساحلی ایران در منطقه جاسک به سمت تنگه هرمز و همچنین یک کشتی دیگر در حال ورود به تنگه هرمز را روبروی بندر فجیره امارات مورد هدف قرار دادند
‏همزمان مناطق غیرنظامی را با همکاری برخی از کشورهای منطقه در سواحل بندر خمیر، سیریک و جزیره قشم مورد تعرض هوایی خود قرار دادند.
نیروهای مسلح جمهوری اسلامی نیز بلافاصله و در اقدامی متقابل شناورهای نظامی آمریکا در شرق تنگه هرمز و جنوب بندر چابهار را مورد هجوم قرار داده و خسارات قابل توجهی به‌ آنها وارد نمودند.»</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4854" target="_blank">📅 00:37 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4853">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی  به نقل از منبع مطلع نظامی: «
حملات نیروی دریایی ایران به ناوشکن‌های آمریکایی در دریای عمان ادامه دارد.
ماجراهای امشب از تعرض ارتش آمریکا به یک نفتکش ایرانی آغاز شد و پس از آن شناورهای نظامی آمریکا هدف حملات موشکی و پهپادی نیروی دریایی قرار گرفتند.»</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4853" target="_blank">📅 00:36 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4852">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
تسنیم: «۳ ناوشکن آمریکایی
در نزدیکی تنگه هرمز هدف حمله نیروی دریایی جمهوری اسلامی قرار گرفت»
🚨
خبرهایی از شنیده شدن صدای انفجار در ابوظبی و‌ دوبی</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4852" target="_blank">📅 00:30 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4851">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
فاکس نیوز:‏ ایالات متحده حملاتی
را به بندر قشم و بندرعباس ایران انجام داده است، اما یک مقام ارشد آمریکایی می‌گوید این به معنای
از سرگیری جنگ نیست.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4851" target="_blank">📅 00:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4850">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">در حالی که خبر فعالیت پدافند در تهران منتشر میشه، جمهوری اسلامی هنوز دقیقا نمی‌دونه کی امشب بهش در قشم و بندرعباس و‌ تهران حمله کرده!
فعلا میگه اماراته، اما نمی‌دونه!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4850" target="_blank">📅 00:11 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4849">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ea8130ce7.mp4?token=J_NcT4Ne_puRuNdb4N5AxiBRkpiiBiTOayDzFHFFFdhH1ZDpCJT8xejfgNaMmNmh3QK1h0uYl6HFV82wzE0JTsMWQ7pLtkJiwVmAD3o5nQnwp4tU9IhxLioIVwZ4I_LOQRyzE_IRPTLT-hN_YJC3kRX93_hCLQ9N0hdTKeEMQZhNJE5cqo3OMCy_pVTUMZllXZOAK34gDCNxELixH2TO-ePP0U4VHMOg7sYgyqUzhX-DrUmw8ZrrUVl9NqVqpf9ADT5PlTz9V6t4z-4v1_haALEUoy-ulPTA5VM7RVivBeOg5TRnK_axzetmjRQZx6Do6dI7f3Br2ljpetBmWvuP1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ea8130ce7.mp4?token=J_NcT4Ne_puRuNdb4N5AxiBRkpiiBiTOayDzFHFFFdhH1ZDpCJT8xejfgNaMmNmh3QK1h0uYl6HFV82wzE0JTsMWQ7pLtkJiwVmAD3o5nQnwp4tU9IhxLioIVwZ4I_LOQRyzE_IRPTLT-hN_YJC3kRX93_hCLQ9N0hdTKeEMQZhNJE5cqo3OMCy_pVTUMZllXZOAK34gDCNxELixH2TO-ePP0U4VHMOg7sYgyqUzhX-DrUmw8ZrrUVl9NqVqpf9ADT5PlTz9V6t4z-4v1_haALEUoy-ulPTA5VM7RVivBeOg5TRnK_axzetmjRQZx6Do6dI7f3Br2ljpetBmWvuP1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش صدا و‌سیما
از درگیری نظامی رخ داده بین ارتش
آمریکا و نیروهای نظامی جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4849" target="_blank">📅 00:09 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4848">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌ها از فعالیت پدافند هوایی در غرب تهران</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4848" target="_blank">📅 23:57 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4847">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
پایگاه هوایی بندر عباس، کشتی سازی قشم، اسکله بندر قشم و چند ساختمان اداری اسکله قشم ، امشب مورد حمله قرار گرفتند.
🚨
رسانه‌های اسرائیلی به نقل از منابع آگاه وقوع درگیری نظامی امشب میان ارتش آمریکا و جمهوری اسلامی را تایید کردند.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4847" target="_blank">📅 23:50 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4846">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‏صدا و سیما به نقل از یک مقام آگاه نظامی:  «به دنبال تعرض ارتش متجاوز آمریکا به یک نفت‌کش ایرانی یگان های متعرض دشمن در محدوده تنگه هرمز زیر آتش موشکی ایران قرار گرفتند که پس از تحمل خسارت مجبور به فرار شدند.»
🔺
برخی رسانه‌ها از شریک  ۷-۸ موشک خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4846" target="_blank">📅 23:22 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4845">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
منابع اسرائیلی : در حملات امشب به جنوب ایران، اسرائیل نقشی نداشت.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4845" target="_blank">📅 23:05 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4844">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌های تایید شده از انفجار  در بندرعباس و قشم خبر می‌دهند،  و گزارش‌های هنوز تایید نشده  از شنیده شدن صدای انفجارها  در میناب،  بندر خمیر و سیریک خبر می‌دهند.
🚨
برخی رسانه‌ها از احتمال  حمله امارات به بنادر جنوبی خبر می‌دهند.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/4844" target="_blank">📅 23:03 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4843">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خبرگزاری‌های داخلی از حمله «دشمن» خبر داده‌اند، اما مشخص نیست منظور کدوم کشوره، آمریکا؟ امارات؟؟</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/4843" target="_blank">📅 23:00 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4842">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
حمله به قشم خبرگزاری فارس: در جریان تبادل آتش میان نیروهای مسلح ایران و دشمن بخش‌هایی تجاری اسکله بهمن قشم مورد هدف قرار گرفته است.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/4842" target="_blank">📅 22:51 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4841">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kaMtkyPsDhNufotTDu95s3giSkA4nR_5hFCusHWlYtC-5laLEAaYsRF8I-6RXacYHOaHQPK2mX0uKSGIygdFgEyk1H1b_NdBVzQCXE-pAf8lbp99fC5y-JAhgDYePjp6vd8BdKJ5JPc7zRt9p1jRw9iZhMNUABgloAWD153_-qKzVOzzRReEM3Ek8H_a3zXRcZvg8AZmpU_wcH7mWQrhrWP0MQyAlU4xHCCijz4H84o4ADwjdiulqfENPu4ujPZ1p4dkDdtMaxAmzGAdV5QJn2dhSZyxeIUo7HRz2CQDeWAW1FQ12-Tiza9ngsuCJsvjHnAoB9jRthp9POfZw9fZVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله به قشم
خبرگزاری فارس: در جریان تبادل آتش میان نیروهای مسلح ایران و دشمن بخش‌هایی تجاری اسکله بهمن قشم مورد هدف قرار گرفته است.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4841" target="_blank">📅 22:49 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4840">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
روزنامه وال‌استریت ژورنال به نقل از مقامات آمریکایی و سعودی نوشته عربستان سعودی و کویت محدودیت‌هایی را که برای استفاده ارتش ایالات متحده از پایگاه‌ها و حریم هوایی این کشورها وضع کرده بودند، لغو کردند.
روزنامه آمریکایی نوشته لغو این تصمیمات، مانع بزرگی را که پیش روی تلاش‌های ترامپ برای عبور کشتی‌ها از این آبراه حیاتی قرار داشت، از میان برمی‌دارد و مسیر را برای ازسرگیری عملیات «پروژه آزادی» در روزهای آینده هموار می‌کند.
مقامات آمریکایی اعلام کردند که دولت ترامپ اکنون به دنبال ازسرگیری عملیات هدایت کشتی‌های تجاری با پشتیبانی دریایی و هوایی است؛ عملیاتی که پیش‌تر در این هفته، تنها 36 ساعت پس از آغاز، متوقف شده بود.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4840" target="_blank">📅 22:08 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4839">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNHWZ39Kyqb7OM4itEisVShm6wjjcNEL8miweAdHnK7n1aqcQCZ4AJb8tR2SdkyskcTHO0-4uiBVkdgOZBxyF9O1ut7cxzuCE9KQ-rHIi0iZZntIhE20-hU9eVtqUtNriJ9aSPYtz563TZMqPVM0TPRxECjMhaCZCRY8pMpLvlwC3g-RXB-0cwsRWBuBjj5lGHGL-oTkg4K20n9IMOoPdd_jl-pPZ3su4bhuAyQ12tsGexkb6rGr-L_puB7aihz5RaHR277M_Sy3s65cnQIsVYHAQG2swd5U3Z0JHMoKZL9iujzmr3X3OMFBgCoTmUvmGOSOpdwo5YcTayhh2b0gNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی
منبع شرارته! محصولی جز تولید
نکبت و سرکوب و عقب‌ماندگی نداره !</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/4839" target="_blank">📅 16:24 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4838">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9CPrKLAhJDDBY5s-SPzd78puxXXbQIf-qTxC7h7J3t6RGeXEVDD5TbNsLn35hNyREER2932E9_bIZlpJbBzui0mcgK0-7iaDusV192-OXANoIJ00kJhxuH8gNnYZ2QFjPusQU8241aKduu1JeQpZjeq8jLd-aadww2NYyq3VcAIPDwuQpLa1MhzxWmfenbzne_6MGp26T_evoKoUAPgH0zGmxeX1ZNOJyWRATxrjVt5S4tPDFNbGal9nipiJ-id6mA7NN1tB5tsHNZUJ4THLnEX1rY6PberuSBvfHVlvSnv7tPkFH4INRWHcS2vie8La3havI17Ep_jjhUPp7tQLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل هشدار تخلیه فوری چندین شهر و روستا در استان نبطیه در جنوب لبنان را صادر کرد.
با اینکه اسما هنوز آتش‌بس میان حزب‌الله و اسرائیل برقرار است، از دو روز پیش درگیری نظامی میان ارتش اسرائیل و گروه تروریستی حزب‌الله لبنان افزایش یافته.
دیروز ارتش اسرائیل در حمله‌ای به جنوب بیروت، فرمانده نیروهای نخبه حزب الله موسوم به «تیپ رضوان» را همراه با چند نیروی ارشد نظامی حزب الله کشت.
طبق گفتگوی آمریکا و اسرائیل، قرار بود اسرائیل به بیروت حمله نکند اما فرصت را برای حذف چند عضو ارشد نظامی حزب‌الله از دست نداد.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4838" target="_blank">📅 13:34 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4837">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZdgZEvCL8840LbcmVcB3PjAU2UaZkdyzwc2-BiqkaxyiNLCldNnxO_vilqirvYrlTJZcxcOWgVLVn-H7zd89zsBHlPwLFTxUsyIqZyDgfOx0OROm0E_cQJyw77LTebHsx9Vn6L1KQPw-B1114pcdZt9PAH3y8wIQLIq77iJ3ZJ3adF1E2iDyMKNj0oTFni75fjHDSCSousKBmNE47jfMLwwP8lS72ahbY77pTsGmt5zIUBdcziNiRNuk1xVkpQPyb0ORwMdvENKLsqw7RQM-9jo5ET4lWm7ASLbM80ehAxy4l1ZrwKFB8XQvMSXx504L5A5szEtO3L6VOyfON0YjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه امروز وزارت خارجه پاکستان
و زبان اردو :))
بهتر understanding
سفارت کاری یعنی dialogue and diplomacy</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/4837" target="_blank">📅 12:00 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4836">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSooriLand</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fb8db45e7.mp4?token=r7MyKiZhWmIY_qgAiUVS3iYE2z6x4wpEijfCyefYiXJgok0SYdS1j_ETiI4SjhQXpQn0phkILgy8vX2xcDCON8kTLLxlJDcfOaGCoTAXnP34fs7qi2Fc5KofrDL3SooLDts65In-Qiq9gqVYd5Nr4ioQJ19JthFYOfl7zAonKObDx4QO-7xu-3D1ESw_h7MOP64hB2b3An0aZ1fJlAetGaA8Fdvligtf9UxHBTxG8-Qg_tWftqBj9haCmGMaAIqxw8tvUbf2TTxZuk3THjKvhLnmIHDf8hhyO06lcOh0qHEKbG0dvG2-gYUDlG28Lr7oaAdNB2QpRe-U9xiT14mqzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fb8db45e7.mp4?token=r7MyKiZhWmIY_qgAiUVS3iYE2z6x4wpEijfCyefYiXJgok0SYdS1j_ETiI4SjhQXpQn0phkILgy8vX2xcDCON8kTLLxlJDcfOaGCoTAXnP34fs7qi2Fc5KofrDL3SooLDts65In-Qiq9gqVYd5Nr4ioQJ19JthFYOfl7zAonKObDx4QO-7xu-3D1ESw_h7MOP64hB2b3An0aZ1fJlAetGaA8Fdvligtf9UxHBTxG8-Qg_tWftqBj9haCmGMaAIqxw8tvUbf2TTxZuk3THjKvhLnmIHDf8hhyO06lcOh0qHEKbG0dvG2-gYUDlG28Lr7oaAdNB2QpRe-U9xiT14mqzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبقه اشراف و طبقه رعایا
@sooriland
@sooriland
..
..
لینک یوتیوب سوریلند:
https://www.youtube.com/@SooriLand
https://www.youtube.com/@SooriLand</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/4836" target="_blank">📅 11:13 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4833">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qjVekb2uWUiibUQ5ZN_BZpab16R6xmpF40NOUjrZxPl9JiQSCbmUidLjSkE0-RNkMLHEcdNT928pKS2naL-DtMRLRlYBiyQ58wx4htpbyvGpx2XcrJPgsVSICi4jv7AAhn_ilSe8CEOjCOUmbWPz1jXGMHWk2sKjl70iBmGoNBPMhnxUZ50MH-eI3po2WAZRg3UeyDCAg9-R_UKNIpAnHMJk_Ex2adDpEBrvYcOSGWaSho4yXv7Wqxp865cXWY08xwqqv8S9DKuaq-gRpe0dZUMw-_KmUL7_AqTikEhjUTafSCOHjLxV2jzY-kh4J-bkkhh8hmB18ytEKr4XAHjnUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cSDjT2LCLjAVe8yyvc4PJL-E7CdGL_hb_nBldwyi5co4WjZqetm7a4QQlsxSc5S8pfh1_WSPn8gIQXGJvJEvBETWmBqbIwrVZfSfpN604zhj1eCIbW2ed7m7bay39putcXvGXdk1B9e_7rlAngPOpTYv14y3oVVTHSLdzC-7JoEzI-aLE2gMCgEbCFg5880B5fDFzCr_DB7ZNbthjNTUtM8clfa3XI_NR2njnmjpQTIPeaEvK9iJGxspWmVl9v-6eFJXAIFuGN_1zYR-7LygQzXIXS7tI9SWD-qxVH-9LXXyeRjcb4SBCMa-cWBsfSZIYLDB9Nmj-ckW0kECqxPkog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Brii9BWO6yZqcBrqybWA28eQf5BXc1n9Zpd0iwuU8lBfBE0d_myiw3kCfr286nVLTS8seBiEVST9-uag790Xa3TKgXFneTTygm5YTSGnU8YSqE10Pcqn5Hoe4W13IxhI-GZo_98fsJrBAcNooGaeVnQkmpm8Vvv5c4LQ7sGLzF7yGNs6YdP2xohOISwUYd4xsVl9qsenoOZHBouIMmvLVcoEgXOGv-gI3eE7ORdwlpM3RswoGBj21r5jMWyqRlB49UFA1-jcTEqO-ModhuuuNgN1BVZqYSM2Y0e-VBQtEfE1nvuLwRKDFwBmj8PWEbipbs05ASRx1NdRYrpsxhCAiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پاکستان بمب اتم ساخت، کسی کاریش نداشت!
ترکیه موشک با برد ۶ هزار کیلومتری ساخت کسی کاریش نداره!
امارات در عرض چند سال ۴ نیروگاه بزرگ اتمی راه انداخت کسی کارش نداره!
جمهوری اسلامی اما از بس گفت و نوشت
و هزینه کرد که آمریکا رو نابود می‌کنیم،
اسرائیل رو نابود می‌کنیم
میخوایم عربستان رو بگیریم بقیع رو آباد کنیم!
دنیا علیه‌اش شد و ۳۰ سال تحریم
و رنج به مردم ایران تحمیل کرد!
اساسا این طول دادن مذاکرات، که ۲۰ ساله روی هسته‌ای و….. انجام میشه، برای جمهوری اسلامی یک برنده! یک مسیریه که عمدا انتخاب کرده که به حامیانش و به دنیا بگه : ببینید من چقدر مهم هستم آمریکا ده‌ها ساله با من مذاکره میکنه و ما حتی حاضر به دیدار رو در رو نیستیم!
و ثمره این سیاست تحمیل انواع تحریم و انزوا و فقر و فساد در کشور و سرکوب و جنگ و نابودی ایران شده.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/4833" target="_blank">📅 10:52 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4832">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XccR4dEOMhAiZhwUoq1Ez4wCvkBXt0IW2FoWBIN0xRfZUWthDMCQuRGX_Oc5iesbeqHiaYT2WRIVu8i5SAMCLJ7qbHWqYrxdZfNnjirpw0UIH4c1VyNILgNTaIDEkAQexSQAiJK2i85AZFWzUbHmrHRa1wFDKzHNqmTx_vDuRew3cr5I3m7fclN_-z_V0f2Zjpm8AWNqI2QB-rFW8dO8ez6Oc66gmX7gxhJsdfnkbXWMvQdeRmtTlhuK8Wd-nd5YHoeJFGqVuvdejuZFmsIn1imFRmBPqpbjVwt1r8dkiAL2ZkhkOcq4cVbwLdZPo1jgMHO4YEKgQw59OhDJyK4aIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🚨
🚨
ادعای اکسیوس : کاخ سفید معتقد است که به توافقی با ایران درباره یک یادداشت تفاهم یک صفحه‌ای برای پایان دادن به جنگ و تعیین چارچوبی برای مذاکرات دقیق‌تر هسته‌ای نزدیک شده است.   ‏در ۴۸ ساعت آینده، آمریکا انتظار دارد پاسخ ایران را در مورد چندین نکته کلیدی…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4832" target="_blank">📅 09:53 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4831">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
اسرائیل : تمام اورانیوم غنی شده باید از ایران خارج شود.
🚨
امارات : هرگونه مذاکره‌ با جمهوری اسلامی باید شامل رفتارهای بی‌ثبات کننده جمهوری اسلامی در منطقه و فعالیت‌های موشکی آن نیز باشد.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/4831" target="_blank">📅 23:42 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4830">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivsQWkjVz0ZY7m3osNU66v6lO0OeAEr_3fGuEAWBmKM7qF7WpBzt-Iozc5DFgeWBhT-sKBJX3Jy-zGLBBPM2HF7vdqN5_v2_DSmt4rvEnJZQ2e80mQf-FFzkkG5xmLVEtXmn6JOB7-qPE-vA3CR7u0MOYdZqIhz8k1rE8qVl9zAHNOinsylDf7EaL2Z1Pw-wBT-Pe-WSgG6M-sxlZfRvkwMPmXUQ5P3rJemufWYbe_MBOzyCD18rcIFt9FT1W1HZ5DTVbsWyjOIp3f_1sClP3Ols2KB8yVlDMs0_JWF6LLNFvJs26ioJggjHtpMEm3-D5lgGUb4Tillx3eMxd8atWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
در حمله اسرائیل :  عزام الحلیه پسر خلیل الحلیه، از سران ارشد گروه تروریستی حماس در غزه کشته شد.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/4830" target="_blank">📅 22:48 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4828">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GngHeCEnIm9bp4_RnW6ZX87n9ek2jl3o2Ug7ANKw83x8S_7kyTrh5M8jB3g_U5BTWcC56rdGgk7rhaZQl6vcZz35aL9omBowE1Idsy8-F0zFUTNVsgpYmVwhdhm5gab9k6zpT2MtX3QZ04HxJZCFLialQy4vrzuxNVK-VCc1g29zwDhEOC6OBAQa7wmhQ3LE4tx2xb2qwDHuE05_Hm0qLtyk_gh7fQ4EQ2dGE9Gcw-07z1ZyhcXHNIkRmYb086KlPmWt_pLEZcp5K2B7sXgtkb39cOq9GiH1v8lKQcHaByhgneDT9ZUOPlM9wi07Q4j3Kfuvy_6leR4_WBIuGqSo0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZFH-wce1gnGMmctAJDxdaRcmb6eDIBHTwae2htfhQxzNe2e-j-jVuuSNaVc8wP7gocEVTCsuBr-b8QMM4W-frvYfG_ElKkMZsGgX-m3GEbOrqwn8IkuABbJJG5Q5jemxn2BFQLd8El2kZ9j27iKON3nt6O6BiR3nKb6yatKb8ITcx75Bzg3KZoda_J0JY9IdJ3j64awUrccT0k6dyNjsgwZgEXCAWf1JZa6DMWID-K72EBXIa87Oa4zGLSl5hyCim2eE3XG6HGl2te2SveVtwkpTyCHiiVyJntbc73T_tczZDld-rDdTfEaAtSLpmbVaJNF_cRt_5k4B3vvV_oX74Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
در حمله اسرائیل :
عزام الحلیه پسر خلیل الحلیه، از سران ارشد گروه تروریستی حماس در غزه کشته شد.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4828" target="_blank">📅 22:44 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4827">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JT1Tgl8-mpFNhV0rL9FjiO4aGdJHI6k36uvpqDRR7HtkGfZhPmx1U324K6563j95eGs8Qv11R--xIXwSEvijIw6Ek8cbDJNk54QL3jQoDOtRhFUk14Qlwz8Czo0ngjPMluDhXK8Px3Dx_LUzzcVkadXl8giqO7_EUFbtJnIaE9pjGjCY3gyUlpexly6iJr73_60hPW6QweBxLjGPdsA3GvaiwKc9cksyFukp-jkcKFgcZcRE-6paxgYKfMjK-McyCqCY1KeGbxi_hgehI6NhGUqyo6LsjtRqyflZyg6SkduOMdswrWvv8SdQSmJSyPnR4vYu_aCHgCECdMzth8mW2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
درگیری شدید نیروهای حزب‌ ‌الله و ارتش اسرائیل در حاشیه رود لیتانی،
جنگنده‌های اسرائیلی نیز دست به
حملات هوایی پیاپی در این منطقه زده‌اند.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/4827" target="_blank">📅 21:47 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4825">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pzxfae4BCUVSm2ELoIxJa4ZNMSbYH_Fl7_KpvgWUIQuMygD5p9vBMh3ZH-85fHbJLRAhas2oP69_HzH7m2Fe7oVUOV89_C5R6xAUtmMQKmbWKe0sryTyD6hKQfBXkRtE-dT6z-Pxl-HL5S9j9g5GAHSRA3WJqkR59eUtGdlQ3JqNxxvM1DDos6VIbSp39PpKjANJip3jaQZKGu7j1TZkscCPW8h9FEAXsr6peRafamnCfcVt-y5Tyv6xKBWlZBhB7qKxGYogUo731HfUAZQjw-N2M7Kn44TX-LsyrOmXnNkE9liO1mitrHCc6IsgAOL35dBdOaO0u7Bje3swBXMNSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R93jzoyLC3LrMem2ndtes6zHJhOfANDV4Yi_tz_EE-Ke9n55VMIzNnZ3fvlb28H5Mp6hgiof3KYwMOiri76zHqESjOzkcdbm9om7Kye0wmmNuCvwJmo0QJMzI_mlnEHI1tUGOAcVwJrGphRfko-HFGMblPbYVYIPuA2OBaygpfFpzdG0Chc9t5Dq_tLHwmhDzjKBuZsRQS1vBNPlKv4e_0EQp_uGVrJAGUI1724oT0xtpXZg68ALxXMtAu6Me5fCoOTSs_PQKT4vTnAfgvAvXa4w1CjH89Yq0PvULNyJ29XBTD_Gkq_POKYQUqpwbGdpfBs7XWjooXCMMIsCHFfSWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
در جریان حمله دقایقی پیش اسرائیل به ضاحیه بیروت [بخش شیعه نشین بیروت]  «مالک بلوط» فرمانده «تیپ رضوان» گروه تروریستی حزب‌الله به همراه معاونش  و گروهی از چهره‌های نظامی ارشد  این تیپ کشته شدند.
🔺
تیپ رضوان، تیپ نخبه و قدرتمندترین بخش نیروهای نظامی حزب‌الله…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/4825" target="_blank">📅 21:31 · 16 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn5.telesco.pe/file/FcIsEUqwHUiJMiI4h-c4KPWeEfQJidd04r6LyLlTyPFUmqCVNeNjl2O2piStDSqQ7s7Clk8rn6EE509w8Kh-LXW8ZZ9N7ezY4wzSN4B6X-kSBf3zKWZl0UsIH63SjdFuhq77asCF-0qhMSlwFrM44cL3QATVLz7hUFdrnvMrxUhjePK2khVGYq7x4jPPAfwGmedZ84uM4YquNKN0jbNuyUVmZg3CkvhjVdtfQRlLuKfa-mp6mL63x9PpEyMss0Eniy2EUhBSnv1SaLNrAR_KKziS_16b5QOXnXhhHaL8JZxSrI2gilfogjPKoEDcaWEz0jQrdkgei4HBlRV2TVk3Ug.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 504K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 23:36:25</div>
<hr>

<div class="tg-post" id="msg-102530">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twqWlLkXVmKF1HQFMYrOnd2M8-fpmV9WSGyrIMl6hGwsBLTrn6zG70Djl1EQrcNolES4wCcRvXg2eGr657y1dtBtL3nxVtTOr0tsD5Es95fg2BvsMDrnImOIkHNARe6vD2uLjtk6nvQij2YXZuzawRhLXXf3u07Dc4vsbozYmDT_o1tmmlYpIe3SZRCC51MA1frdZhX7BhBGOgxe8fa6ECoBSzc28x7cPwhUrM6koOO-Y0wedvytFict-PAFR-LjWItuCJtWz-1awPJB8U2jOAtj9vcf843JWQi982sSWLNMrYaNrGw1z-voNym3zt6Y19A8mY0N6zz8mV15s9CfPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
مورینیو بعد از مساوی امروز.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/Futball180TV/102530" target="_blank">📅 23:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102529">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kox515Y72BUGgFGGtEmFNSzZbDrjvWxSK5rX-YSopoZD5N7Fh5amIHuZ2BjRJVyP-1d_yFQVx6Eh9QNed4JXq7T_ax_kUNB3nz7OjhpxXyhsLkBXSOvXIKGrkR6fS2Gs52MCh0G9UC_KO4soAmzkDGW50VSMPr9uB8T03MQBYHlUgRjIlkMhq8rN5ulvDPQTPmwEoH7ralFi23CdWORQ8nU9aSw-tU7JAYj4oPEYFjJXs8NJ3zOFs0sthtkUfOxb_iS1JghscVbGoeMRLswbcEErsZJfv0l5QHAqRkjcH7P1NPWOUuaSP1xTkm_I5DWAzDeblw4QBKzu-PgENQF_Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
تیمایی که ولبک در اون بازی کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/Futball180TV/102529" target="_blank">📅 22:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102528">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRVqbnNpHD82jytaMXYvPdEMMyjlnOVqez-NFRFrtKB8REuqGqT8D6_xeAfJfnqaXx3egKW-iVpUBE08_Jb0MvhG6AtPbZ96Z5DKSBA4ohfWfzbsGCBgQ9UeL5b2_Xsg15m9dxWheU-na4FyGCa4lW6gj5CqF_hQLOmlt09KZW6OU7BXB1A73SD8DakWUUOCHnolDco79YxN_Znj2ThJMz0tJRBkEvFhpjWybHzukctKwcP0FlswGoQZRDC0VgHPaxZskxVWyOYFO5qxQkXlBt5vF5-lrgHEAjrx6Jv7tsNpCMzCMCrOiH2mjMJGcwShdcNvPGAG3l7RQ73Qh_dPjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
رئال هم تو بازی دوستانه از فیورنتینا کامبک خورد و بازی مساوی تموم شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/102528" target="_blank">📅 21:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102527">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRE_f7iurJeg7UcLCDWdQl7HyCsig1KRk13BAUCRiiuXU7mJpdnR-dmJej0olDVOYd3e1WtcUkt3K0DR_vV77uma7jBKwxF9fYp8bINTyPaf-3w2Q7DAOItV0LRuJXeBrJ3qa3qoaGzZTbkQAiGU1LJUHlnYqbn_6BU7NoXaQPSzMLgKB8o9pz_LpWou605CaQEtKRhwaFLtyE4kEY9ggevURgkCWXu1LK6GtrK99RsDEah54TIzLK-1D1C8aQNrJ6tJYZDrSS5bk2ZcW7TKAG79ZqfZMeEPXToWf0Fc7ZI21CqKa-jLS1qXl6KBLGRwzPHBI1IMqDIlRsJ10iMJFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کارلوس اسپی:
🔺
پنجشنبه: بستن قرارداد.
🔺
جمعه: اولین تمرین.
🔺
شنبه: اولین حضور در بازی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/102527" target="_blank">📅 21:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102526">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEnPaJgz3m16Vbtf754c1LGe-_CKH2KRjk4YV6Yh5NeSBqt30gkRPkVC2ugjVE1EyfVqNumHcYXRs5-cuqNIDAgw0vK8wl01VcxXNBRked29UAh-7g821rTliAGZlXWD-Pmg3pfAE7gxdcq7LvxNoM1i8_DlfNJAzmftmv7ZgetaGZSG0aM1-6Y7suXwkuVbcf_c9ooI26gMy33jD6Rxy3GfFzDD1RDfT95_FCMaB_eoGDIXD79dfJ1cm6C5YhOqDAMMP_prxIYEDnMpxLPa0PGi11MJKn_mKX-O-nYchJQg8jctIUENMkPBAqNPim-IgZdLduqU0xyhJfNW0UAmrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بازی‌دوستانه|ترکیب آرسنال مقابل ژیرونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/102526" target="_blank">📅 20:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102525">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpLdDLned7CzrS_MMladjmqit0-LdwOVRcp0KaHAFWW8qRDsCG0D4Uq6DjNFGmekvc1OtKiMIx7EpQFW0r35JmUkRQPYELwztUec6OBhtYh5rcMDrjHgVy4nNEM2Md-8taupAe7kLeE3bbzC_KbHVDpYUZqE31QeMsliqOPvU1_uNmR-Gr4YJGc-AkPJDO0UUY-gRUKcK6WWYWcLPhqe_r4HjHYdjk7Z8lCxSSzNucj3vYyvith0EmrvWo8O8S-nlXT9tyO6jnMLnBUM3z7tupRNfD77kl59HaPLx2DrRr5I7q3KPOV0GzFJx3Py799fmoiRgMEUS1OPgqDZGHMVjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامبد جوان با زنش چیکار میکنه اینجوری شده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/102525" target="_blank">📅 20:17 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102524">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jl1uYlRzxyT4LaYjkNF-c-hYYGHo9f3n4JhvqGFg1KOsvwfg2mYvs0yv26GE0LcxtPIqvO_5wRxXDG6YQxh32rf61vgbBNDI9I8gW3Z5mrrl3Lw-U-Tp0M3LomiQGg4BOqYnhiSWmsDlCYDDz0y1Aeh76Gje9h0wb0UgGGax2w8qvLJ-HnEX_6bbUv-huz-SmoHSuBP8AT4xztaeATtu2VqiKJjWfCCpVzL5452sufIVJve3zC3yi7DUELxqtiKesNjwtCaccyIlsH7Fq8GnU14QlNhiGkKYDMMRzZxGB_SOBqtk3ZEhXizzTAjwHlC8Q8oayL-qrc67UVw4BKE9Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
دنی ولبک رسما به چلسی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102524" target="_blank">📅 19:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102523">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glkDk1TpHpEH_xI-sRKyRRbYSdVAPGvp5uZhuaUjCA0Ni01uV68MJFhU96aInrStqNoKPKOhhFq0eQK7i2l9sK-yhHg0aUMNSyUs-slpmY4HeTUJrXvyDG1fBcg5tPXmrI6oeZmO2OQZB7haBDMKmDGtkPNXSP_mnusiyfxLVdB_zMc0ZMwAeGRj_j_bawtAAnkXc1u60CDQ25WKO2KsIGimlXNFBRNoPAzQDX6cF4BdC9a7jeJzqk6vvfzVh1fkWy7a5l98Kj9NlTx7nseurKkXooGPjghwKdNZqfKEUWPJwYtAKm3M5GnTDL8CRSq2AuojX481gmm3LNeb0WHCAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بن جاکوبز:
جایگاه اینفانتینو در فیفا بشدت در خطره و احتمالش زیاده که برکنار بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/102523" target="_blank">📅 19:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102522">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFzJwqHhULAWRh4mjkvDg-mSh8MZ5CBQVM4ZuC7ZXAqMM4waIbq5heXz4ZCS5_yxzy1tjmqb8Hji9lM9yOVadbYZAltbD84z_7CeV--3EUDQ-jVUsiWGJXfxBVnnYVqtamQro03-r8ZAagzCRSxn2VAo91E1Kp-AedJlOkm5JsjWXtH4FJE1jPZayj5eWUESHEKEpmPQvvq-pDTMy4KI_ojeRtnDSchjZjRly9AU2vvfIWODFWF59xcHFufHFetmj7sg1lvmo7hdc8JUJNuaglaT1lGd0H3p0WWdiSoBbNdvcSMwk6OLt32Ll8HawAbMmmXuGZ1MWPOHiarodDleBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
🔺
انتقال های رئال مادرید به آرسنال.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102522" target="_blank">📅 18:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102521">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aK3mt4c64I8ukYlsSRD0ghwoS5vi2dQtRPTmeoA1x1sVuJHDbqezeR0bYsq72FXhMiIYcIqo4wJrzLg70ibny0xXo-QKdOntZHQzTuXKzvOPKecHn9q9WaJHva1DcMQc4VDHwctheG7s1tIKSjsSCuGZxHqJskIcZWi-ys_3__B750lS5k-l-a8z_HjpEScw6h7OByq40zVac8VH8EgMDh9yLiIGIcXCsmZTJUzSvIeGg46r8WWAB-bnGkjzMk9PvzWfW9YHWTKIh1IRzetJSaW-AeboA4no0Q-LeAVrKNxlAV99gUkh5E03CuS8AGpOIP7xrgjyqz2PWXdDFOWAag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
ترکیب رئال مقابل فیورنتینا در بازی دوستانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/102521" target="_blank">📅 18:17 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102520">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHbGciny2o4HtLespz4FhB8Y5pJIrPAV9O2yhc5IF2YCe9oEobjcNcyiycmtPjAnjC9PQrRoTz8F88rT8EYdYCRpW_nu_0Fk2g9CwFLTOTcWrcz3Z6zYCyi9WqzeQRV0LGEedEZf1R7ikJ45bm9P1PR4_tFEWWlGGltMTGM24lN9vRvf3qjtUXxAKmeGdW_4HDYpCGaU83Vv2eGo5ssP-fZA0FkcdS2nSIB9t5YDzP-7dQP39ga2CzWJtRy3XvRSiyhVbwzFcm5MKMrTQwHt1O3WPIeIw_mYIGpn5dqDxHy3rdoPkAbO600l9fpTywF-I_rBFT081gOrY-Zyin3FfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوکاسل رسما لخت شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102520" target="_blank">📅 17:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102519">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDLtTZskk0arUtgRSQDD3Ged5rlHNDTgTowXMFpA_sdJuyhuEY0GYYXScMfnZitTqytHGpp5KHMjdtdKEOZJQFNAVaif4EzJjESvqy4yHGP72tLNQtrQmkXIuo62rF058KoATdrOyxsM429SkQfSwDfGDGyIvp_RzfLgspb3Y9phW9mTBuisehbLhUDMVGMhFC9xEO9JSHmsSxv94kyc3IB7V-hBLEA5P4S9Xc8_DrUnHHkzNAgftil8ta3UiTz4_LGAuizfAnx8BRMII6F3sp0Z9GMODKFrGDGi-yprhalo2c_h-S9h-5yxpeytpZsDi76yQQEvXDaymM-vFMajaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فابریزیو رومانو:
چلسی پیشنهاد سه باشگاه اروپایی برای جذب ژائو پدرو را رد کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/102519" target="_blank">📅 17:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102518">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSTe5GUpPpf36_5jQhP8745vJLVaF57zuojfzGkbXRmgI5YzLacmSCxsiR16b2PW3lLkVLvm6RgxL5s36Tqzk1lqEnRvlUo1eUwidvhMmSnEpanPd4diDL0Rx3Og6OdaJqabekdc2_rU7cb52qIUaT1ZeYHOXuC8aD0oB5NGoMvxusU8ofM-iIstOq6Hibxbi7WblZv810pSaCYGIMiVzmDf3-kIIoK1C0j4d0K2B37EM2BTZ233VmewSsXLIZQYswrENwwbDAdPh6ILJ5wiA3YRz5uUFatoI-qlEa4m6QIO08HPyN5dAJaIYjwh9ox1Yxg5XHR0OmTn-NxxIbx8XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس طاقچه بالا میزاره و ممکنه بره آرسنال؟!
من یک ایده دارم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102518" target="_blank">📅 17:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102517">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fb462e454.mp4?token=Jx5uPb2Nyl_48mk66BoRJeD7YsjMeNd3W9kDJp4_4glTi7Xzh9yPVrkr6MwF2oqgs_EBThO4KlrRQULCu-Y1oXPScnqpoJlNQll4dA7jSbt3L3Tunalef1Oo4cbmy3YL7GWCCTJC9H0dPznSMV7s-ukKlD3LfTEs6HF9Ay2tIH_7BmAqW7GB3GlenEmH9AgNrqcI0NTo_RRE4MB5LhwAylLslLu73UihjIQLZKM-XKPDRkR2bEXlXgdPEbp4sx0bVm3IB8sWXcg6_58YTU5TcXJio_qVQ-TTx5-pPCxHlnJXr-c1edIETTxivVprrIBsEkUPJavqVjJNeezOKO7VgyjT91wW6SSiC9v2PfrKyo7t2ywUe29hWjEfUCchfHhRkSna2gQhdLKZacEZOPu-qICnV_8ziebjPW89r6zzKJMXDm3BLqXW7f5sJ-O9Dp37dKrnJZNxUoSTzo2H1ZZsf_wryuitA8kQcP1e2Dt90C5eP1NAdXecDipDzZ2Nab-b4_lPU4Ic9gTVSwrA_mt0WnEnjCrUhwVklFUGMaVIIVZLfvSLazbtiO8fpRIQc_MXT91ZMs3KJZp_3BVWVyYlXjUBy0W8gliKhaBCGcTXSxCHyHPNSA6T1SUlpAlSwPHmKwz02eXL1bF5V38CfaRf8Q1jaDlsIB6B6McIcM7JmDk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fb462e454.mp4?token=Jx5uPb2Nyl_48mk66BoRJeD7YsjMeNd3W9kDJp4_4glTi7Xzh9yPVrkr6MwF2oqgs_EBThO4KlrRQULCu-Y1oXPScnqpoJlNQll4dA7jSbt3L3Tunalef1Oo4cbmy3YL7GWCCTJC9H0dPznSMV7s-ukKlD3LfTEs6HF9Ay2tIH_7BmAqW7GB3GlenEmH9AgNrqcI0NTo_RRE4MB5LhwAylLslLu73UihjIQLZKM-XKPDRkR2bEXlXgdPEbp4sx0bVm3IB8sWXcg6_58YTU5TcXJio_qVQ-TTx5-pPCxHlnJXr-c1edIETTxivVprrIBsEkUPJavqVjJNeezOKO7VgyjT91wW6SSiC9v2PfrKyo7t2ywUe29hWjEfUCchfHhRkSna2gQhdLKZacEZOPu-qICnV_8ziebjPW89r6zzKJMXDm3BLqXW7f5sJ-O9Dp37dKrnJZNxUoSTzo2H1ZZsf_wryuitA8kQcP1e2Dt90C5eP1NAdXecDipDzZ2Nab-b4_lPU4Ic9gTVSwrA_mt0WnEnjCrUhwVklFUGMaVIIVZLfvSLazbtiO8fpRIQc_MXT91ZMs3KJZp_3BVWVyYlXjUBy0W8gliKhaBCGcTXSxCHyHPNSA6T1SUlpAlSwPHmKwz02eXL1bF5V38CfaRf8Q1jaDlsIB6B6McIcM7JmDk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه چرخ تو اکسپلور میزنی میبینی پر شده از کلیپای عروسی ورژن ایرانی رونالدو و جورجینا
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102517" target="_blank">📅 17:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102513">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S9mPog6CqJWD24_nDW0t33EgqaNDkRe-MvIEKqSIqiOc0IFz8L1Z9zG1tLSwds4igbXmL33RpwsBm-d6iaR3J5id3QbsBmBeHartAqaZX5s_MlX0brRsCPadrmmPTW0CK5R7s4wfKDZqcFv3rV3jiifiTTE0Pjtau7SlgyX28w83iTRVW8OP5I54aHHPmHC7ghlHBCA9TBuHQDL5ezlUnfxCm411HBTvpKYl_QTPtbVtXwzH8Xgeq-bJV_ZoOkrARc9LhB4fyomXuvso7JxN2jUi5dFS7JTvgxWlMTk397Vc_GhyKba0TAWWqTian2by4uXew5LQpS3OfloyUFaI9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/et96n4ctRLLvGR_7CTPF97BW5lp2ZDUzRG-KaQANdhDWICDuvSrQJdW5bIE--bBD4wsU4iPKlkhtnT_155WvQXd-RQESbam2hvs2tAAfA00H4Cv1NDbAoT6U9HnMbyAK0aQkx7PYszDQSBu_K_ayFG1WVqhL5q-Wt9AV3gueQyHcGltHjeFAJTCvCLG_BPpjO-NBNktrlHQmDgUw6rpec3BlyHxvNQwEG3vqj7Mc06bNsQPREQLCUUOo88q64VylLKNooMBSULqxdkrF6UEEIVzsw0hb3tZn7aCqH117gAjx0abtWb24MibNYGjk_RKgW96DX5eRKFgY7ZDsK4XmOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z2zxW45bJ-6YE8gVkIj46lJZSheQOEY0WA3VtNyw2fDfTtrnI0QIEHZwTcDcndeLIVBLzcg8jL3ZdyDvgMjjZmEBXSyGgmku0_X2boZlqdIn0BPjdZI0i__Su42zsbb6IM-bjD0s_nWpxJHRCZ2ezEYfUJIjgVBPLn9ZsSz7lntTZNv-HtUljoT3YXouU5yEBzAzuYpPVDuV3dlVK46avhvMHOY_GwSBOgkcwtI476nqwbINrTB1CrOxvyqnV_syBjbTg9UhH0f09G56D3lA5BLxoi0wJKLnBsYwTbimDzt_gN8R-PkWEiYYyo_VJOLsYnWqWbZK-OiUXX-Jfw44Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l61Lkd8Uz-GcPmg-QHGLj23gRPH0XPKsYSTpMCe5_JK3nnMDswdc-3eRYccL_ibp2IQwkKIp0h5XbW1a1MN2jUH5vDm8OhHPPgJzYcVVLGka2MmDEYXeXLuq1RsDlOfPLxK8wPrfz6ob5BEq9g4DFyy1LFvQENqktkzyih8a78G5hEUI-4GTQ5wE7wyhJQUOdAwRpzMbULwO-ciW18rNy-UMGmCaQm_sfOjdAgVlRWN4uVOWfo8m3gd0AwHigP7QM1xC4J5i4ialRb71d9GXxWB6Kd2oGOLSYSbwyHxwukEDg_vca4odq5a1M_YjvcH4eEa9GMDa0Ornn6s5gotQDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پستای جدید جورجی جون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102513" target="_blank">📅 17:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102512">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LF0ozzzbzSoPRX8D-DFhceHe4U158gTJNqe1q0gEP8nimrbzEua6XoFu7kC1uBf-_5cjsyYwXrHJH5b9y7pZR2ZgaEdBRzwTNZaa8zWEDz1hOOxT0LVjfPQZgH4Xyc1mucCkI0TIuL3eugFV9lBOWvT43nuQKmBBsdXhhCUCexmEqhSxCVCd1VpOfcbCza6OlEMBNBRUN6_uAclh1IpHV7NBwa9IcshcNsliLBWTmWZdZWQHLpmoF-dsc-H6wpEiTq7OssVi9rCitF3AJvs6XTr9wtsZKrT0QdZ3HhJqcyi1PBjtMYuV8DDEZPQlGmtxgk_nDyHice2sEaH17BAijg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🔵
اینتر با نتیجه [3-1] در ضربات پنالتی مقابل منچسترسیتی پیروز شد. بازیکنای منچسترسیتی سه پنالتی رو خراب کردن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102512" target="_blank">📅 17:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102511">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f1ded84b.mp4?token=vKrMMnb0bUQgs82qoy-dIzJU35G2R4gW1OSGZXfCKgbD8uJhZDVmTXWXLOpaHD_YnIXKDHSN5mRz_qpZe8w3I9Ed0UC3vx-fzQhIPNbdefh8jSYKRFAS91rIPDWyM8V2PPNxipxNhf1HylcXdgAbMqEqg_oXtRYelVYGgL497yGmVQJDqM59fMOQq5OltA6J4QfAWiM0SPCdnU1jgPq7pGT-cX1M0sJMD7pN1Gp3AKC2e7iNP_j9RCtIeWRmC4j8uM3p5ZoA3m35rOTbYBa8LOZ1PnXIkErffK_l7gvARV3yHK9lCx5jX19hw6mw0lhiXNAxz2vqz-IbPuLuXTZFEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f1ded84b.mp4?token=vKrMMnb0bUQgs82qoy-dIzJU35G2R4gW1OSGZXfCKgbD8uJhZDVmTXWXLOpaHD_YnIXKDHSN5mRz_qpZe8w3I9Ed0UC3vx-fzQhIPNbdefh8jSYKRFAS91rIPDWyM8V2PPNxipxNhf1HylcXdgAbMqEqg_oXtRYelVYGgL497yGmVQJDqM59fMOQq5OltA6J4QfAWiM0SPCdnU1jgPq7pGT-cX1M0sJMD7pN1Gp3AKC2e7iNP_j9RCtIeWRmC4j8uM3p5ZoA3m35rOTbYBa8LOZ1PnXIkErffK_l7gvARV3yHK9lCx5jX19hw6mw0lhiXNAxz2vqz-IbPuLuXTZFEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
اگر پاس گل پوشکاش داشت، اوزیل بیشترین رو توی افتخارات‌ش میداشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102511" target="_blank">📅 17:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102510">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GK8fXXuEYGP_r2-UEq176jm0BFwcZ8ygKyjH3YK07C4UdzdXXZYsaNCK8_AvPJmOP8d1BRRRJTpcnl2DqqDcasD4z4_bs3yy1vlHu9D-9_e9ltwYxuCwJBhWbxVRXOyCr48sM_pfr4NyzC1R3C5oIanTcbuV4TWHbFddGPOY45DY_L-D39AgyYpuRam43CHW-HDbEutFkxMq1eY7M5yhRmiCEmFzHxhwEQ2oMoCv5Nc3YJn3oa6Cv2guthKF0-6sntIxShL4q7A9847JtVyb7nGOocEgp5V2NrQFArmaWMAvb2oT_bgKwclN7dpL2OlOUHX8SK7XClsnI0-EhbJAww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اورنشتین | اگر وینیسیوس با رئال مادرید به توافق نرسه حاضره همین فصل به آرسنال بره.
ماریو کورتگانا: آرسنال ماه‌هاست که برای جذب وینیسیوس به طور مخفیانه حرکت می‌کند. آندریا برتا، مدیر ورزشی، با اطرافیان وینیسیوس گفتگوهایی داشته است. چهره‌های کلیدی آرسنال نیز به نمایندگان او اعلام کرده‌اند که او مهره کلیدی یک پروژه مستحکم خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102510" target="_blank">📅 16:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102509">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzcNNldFcRO37RtUz2tcIwp3nSSb9hLmeez-FoGIMHSEkWnDSm00A6LTb9kWagrmPvN8VHRUataONxhwZF2RXETRRQgyzBtNJ7Fs6Lz0ON9EIbReQfID1w3c84_Ix3vcxiecx0DW7N1s0OXE_auB1icgfP314sxuRgwpLikKNbmPd0gfyb4g4jUlFjDiS17fkUJtchKZSNKZoZawFX3dqZAycmIVqXmR-6Ucx5US4WaRoqSCCeM6RUokzWiBkOaXP2FJOLgBZzQ3mmv2f6r2Y4HmTLg_HoZfbOqG-ErmJG7BwWF-UAKXrORN96qi2jRTreEc0PGsBKutmNpFJZa-XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رودرا - ESPN:
طبق اطلاعاتی که به من رسیده، انتقال یان دیومانده به رئال مادرید با مبلغ ۱۲۲ میلیون یورو + ۱۰ میلیون یورو بند پاداش نهایی خواهد شد. همچنین انتقال رودری حدود ۶۵ میلیون یورو هزینه خواهد داشت و باشگاه در حال حاضر منتظر نهایی شدن انتقال بوعدی است.
⚽️
@Futball180TV
‌</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/102509" target="_blank">📅 16:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102508">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDK3XyaCOYOh_Nki8LUYkP-O_Tsa1meXZRuVmd-3dGDNztCiJrpJ1zDBGnauhPFySh1eey4UZKOEcyZqRLZXTL2nQ0fXQGDPxlG-86z3VXjzByz9zT6_TSNwlhQ0QBU-IzRACZ6eYA8xRNeDVVZ-Xclse_8mp-_gDO70FE6bu6pcDqimSMcFqlmuJvdrOHbPUrtRrIdWHT0HPv4sa6E35nAgGS7F8yJ7aTAfA7o1VaP3q_WlgjCmaKfgyBWGlYZHmPO2qLGSEXYxOCf5O1aBCzoVlOOpfLC-52cbrFqwMuXPwgDnbVdoN0wg67emi950zvK7q9tQhQhnWj9O02GpxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین شات از عشقتون وینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102508" target="_blank">📅 16:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102507">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qC3NNI4nfvTJ3ScMGpePfWP_Slvtaj-3lwdfl-llb7agLlRBLfvh9q1xxhrTwcnpHT8ERkwqhEptynD598-_KzveJUjw0dRwLWPB36ROzQHr1KwSJZXZLtI-hbAi5cBLOdHbf2DLhFI23bhzDOu0U7iyybMiHgjRbtwtnlzt1BKy5LtNDGOzFBTcLvwkwemssK54ydRsz3ijCgjsm4Ca-OAklRSo9zfMGtO7VshmSeVUyhhdoTMZ66Mjm13S4VW5iOeRe-FF0ENWLhs6S8AMyxiJ08aijYarJz2_7Z1AX6xqf0AdUcHhfomRnZxNcpgs2z5TX2FGlkGg3ceQAHvNpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚪️
چلسی در یک دیدار تماشایی موفق شد به تاتنهام 10 نفره 2-1 ببازه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/102507" target="_blank">📅 15:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102506">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WO9vUjGapsWCIWXRupkCvy5Rt35EAvfvxudd6BAZGz60IRsT7vqwTwW8Gpe4pnzlyfjkrcU1flB_wRLH3hpg5axaj0BklTZwj6KzWyQVKFLOkQvfmafGke4oyCe318rgKa3Ji70aM8SYnsRfyEosvJq4pzFipL6GpGB-RAATR74zgbe6W-avZzB7zAemf7wdIgNwmAuPULlNFZ67QEEdyGfT2f5niFd1Z9B6OPJ_GliooaUAYu2532BB7-GsIeH7RqCzMQ0ZvlyXMWJAlqT6Gm8estDgglMpPLcj3Q8V19XD2sbNIlBz5eqbv1eXMoN4GYijzF5NfuC3cLKHm2zevQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
تام هالند:
بدترین تصمیم عمرم که خیلی ازش پشیمون هستم اینه که طرفدار تاتنهام شدم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102506" target="_blank">📅 15:07 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102504">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a1fTku8wXouns6Mo_HDXaJEzmQaxqI_1vWgkHxiITZRzBISgpPmErvuYolpHQlAJCaZvY18XE8btor6ZtH2ZjoB1NQOJAYy01m73cxXnO6qZmiiQGtWQi-CKtByFUKS60mARMXdJVog6Xjh5haUcBa8_oOL2Uu26rklt2AnL3rUYrhTQT1o6OtNHLHZMyyu3ZGvxt1Jj7zM1g1bIzq9rdZfqFEk0XRORq3fqLAvrYqSISJE3fIy-l73rZjUXnhpQQv5_tFU_WBHbwewvwloTsGh2oSYaNlxliFW2G-cCfESsSbUZEfYQP_cZ20918UAPey1VGDv97kzU9QdDPFloag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c8hRvbnrxQ6JicqOV-REYPrUXFHeTGCbT6aOGmaFD5abVYlSqRZreCk981cRB6GRBcg3EXrhGgMJzoBhiJAbaU-uIO7sMM-tFQNlVOKM9gDb1u5HZC3sKd3C2IrEwwxK_EWSluI2vf0JytYTJfkh02SQpKelu_mFiXcs8lDg3QQ9EKTsNrVkKlb-uz7Otvu1e18Arj-SEYfzB1c3TulZPtk1XaaB_Ha7qESiipxTnnRx6PeCSX3t0PebIrjIv_yDOzP68IeP_C1vyUvypl9xqaIk9kiq_kSoh7krSHKt5rADd3mBbksFCVYLiW5zpsK5gfMD68Cdbh5P3CAJAC8Wkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
یه پستچی رفته بسته‌ کوکوریارو تحویل بده که کوکوریا نه تنها باهاش عکس گرفته بلکه بدین شکل یه عکس هم با مدال جام جهانی ازش گرفته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102504" target="_blank">📅 14:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102502">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rySRZayF4adT-0-oh0JNzBjdI-FfAX0BlTBHthvJp9cQ-gFIqmwEKXX9hgkBKRMmZB4HIPTKGFBx_Li_95ZGmEaFg1u-EfuhpLnjDWq3LubQDz-KSyfKFnwa4Z_EiVs1FhbwT7m9IE6nKit8MkEIwpSM9QYzY5O-s2DJXD-x6vW2yTbfNmd2y5aGQ8JnmiLBO7_hCKZCorkIhXBnHddkhteMmB2lxvg5o0V8MJFE_OripxdOY6eNmAVqPxibxuanS1oTt-taDukTl7LvyQ1lRUdie_Y-EI6R7V12LGLJNtU4RArqb2YUFAlbJI3d2B8Q5_BoPDanFrzdSESHK6ol_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Du80yLNkx_Q7p_wgn-PwHpOhnBWTopFUGhaKxi59HValggMwMhz1eIu5cEcm5Jjr9ziGAjx_hUemx1_mpphuRMxtpbZ02bMdJKaQIcUC7Rr_xnNvDqu43f3UJC7lxfuNzIrBQaN6yaqPTTDW_AJ0rRiNfjvfFFvmaUHstColpHQFz6FXjmK1vAz9_St8DsC7eXEE8nRbtuJGyTU1H7lXXL20z_sruyifNWcQ5rBUH2x6fsPqlihW_dwUWXuKSf9VxTdzrhzuYWRIs_hY2ZYtfOAFfkBC7SzUJahtX0gAOrRsE99og_DuSI46v9f7N-jHBXHU-Vf0I1f_EwSIDnuINA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
⚪️
نقل و انتقالات بارسا و رئال تا به اینجا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102502" target="_blank">📅 13:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102501">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5_UNSbE9Qu_pK2H1HNcqfmW2R2dCCRogR-IZFVCOAfymIzGPfs1GPv_HXK1eP7nzMZvtinc82IvbFDKYWAQETBrgu-RYhIqjLirTEpNcC_71Vkb1hA-Ers9yE9BeH9fwZCG2TI8IWLIaYsxT0axQrkUp9BCDfPITOQGIEvn-B65wAA4MOXJhR8DochNeg0AcYZzxcavyAa_FwmrLR1lLeVWXGZ7L7M63zqjQuje5biHYelo_5fR13lg1fiCgFjQcYjgR7yYkZiF7XQtqA1JDRPk3XPZ13ne5UohziO1lG9cUr__qeb7jXn37BpNuyUL_ifgjGmZvxkjGNhZXLqLiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رامون آلوارز:
اطرافیان وینی هرگونه توافق بین این بازیکن و آرسنال رو تکذیب کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102501" target="_blank">📅 13:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102500">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sf8w7pDq2_8_iBSSw5wv16uoA9yT5S6kXwFj3SzB9CIKis46zEBUWTe0Rjd2EM2lGWbuNV1RKl50NYMWH11UtJtshaLIZ719Wvtm6Rfi6C_y0Tf0eSu6qntsHQtS-2gpHVTLRFEremGlfyxKKTk7SUaHgNdQSaMH5AtOXR5GurqiezDJPR3RewaCCIZ_5YIxYlZTY4nvs90m_6-UIIRAXHpPeS1VbnhiDk7VzS5gcwFdoV3sRAol70mTciHq9nhsadnENZeFxGptaY6lZW9k8RqxTIP7c874gwhif5ZxbxRgQvahv_d_fq6BT8U0h8-cG08pChTizNuQUzwg7avobg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
• کریستیانو رونالدو به یک ویدیوی کوتاه در اینستاگرام که او را به عنوان مشهورترین ورزشکار تاریخ معرفی می‌کند، پاسخ داد:
"خیلی ساده."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102500" target="_blank">📅 12:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102499">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29d00a9ff8.mp4?token=EPU1o5fERphSWmF_tivMYhXKcppVtdQ1eLpFmfdbXJX2wExCLcwnQMchsOy4SvvvTSMwA-780dtZIlYPumG0ns-GlVZaESXYdYaZ5DE0q6YMzUUhNYadKxZwH3cm4u5J5KQ2HiDF450FXU_cpVe_kmBGjZRFSNCef5fc47Z4hTTZyNeU_ASHfsg5TTT2YP7NDjDVdXSzXa7uk0vbX1iMiSUBb2OtWkyCaX2mjDJslw8D8Iiq1mYFo_nLYDTO3kq5g1dmx6uQYOkfL_n2Uu_uFGTbhDrFzqgK1No9p6n6p6Dc9kO-IzcoRgpwBbpy86dEhdhW2OOt75SgMa_F2jpYq4JPRCJo5URfRwdCNT0QisLzn_EVknaQz3gU_uMsOsdtfUPSmn1Ocivzl7NacTSJORdyE3w8gqX-Xb3C5C4o7GO3GAFOEm1R5ATCWF2V6rMsld4MQzamYTGDbqxdvg1n8B47mvB3khayPe4rPRfmY4w7-cZyOpFLoZXwYAZY52_5WSiMc8YCCQWtQ8r9_sTkvIk50AIjngdKLdZv1mQat8rwZ8c9VEqt_uUh5jDK28HBwOxjZr29GTZI-_jhLLt-YCYocHtX7peTYREUJfHDewWhSRLO-A5oXFHv1OyBK7Fv0i17hRi9WPZ4vneJ5zquSX0VfMRDVrfZ24jLT1bW1G0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29d00a9ff8.mp4?token=EPU1o5fERphSWmF_tivMYhXKcppVtdQ1eLpFmfdbXJX2wExCLcwnQMchsOy4SvvvTSMwA-780dtZIlYPumG0ns-GlVZaESXYdYaZ5DE0q6YMzUUhNYadKxZwH3cm4u5J5KQ2HiDF450FXU_cpVe_kmBGjZRFSNCef5fc47Z4hTTZyNeU_ASHfsg5TTT2YP7NDjDVdXSzXa7uk0vbX1iMiSUBb2OtWkyCaX2mjDJslw8D8Iiq1mYFo_nLYDTO3kq5g1dmx6uQYOkfL_n2Uu_uFGTbhDrFzqgK1No9p6n6p6Dc9kO-IzcoRgpwBbpy86dEhdhW2OOt75SgMa_F2jpYq4JPRCJo5URfRwdCNT0QisLzn_EVknaQz3gU_uMsOsdtfUPSmn1Ocivzl7NacTSJORdyE3w8gqX-Xb3C5C4o7GO3GAFOEm1R5ATCWF2V6rMsld4MQzamYTGDbqxdvg1n8B47mvB3khayPe4rPRfmY4w7-cZyOpFLoZXwYAZY52_5WSiMc8YCCQWtQ8r9_sTkvIk50AIjngdKLdZv1mQat8rwZ8c9VEqt_uUh5jDK28HBwOxjZr29GTZI-_jhLLt-YCYocHtX7peTYREUJfHDewWhSRLO-A5oXFHv1OyBK7Fv0i17hRi9WPZ4vneJ5zquSX0VfMRDVrfZ24jLT1bW1G0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
ویدیو جالب و وایرال شده از رقص امین‌حیایی بازیگر محبوب سینمای مملکت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102499" target="_blank">📅 11:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102498">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86343d5e54.mp4?token=XdwSfD6dNBMR2_OxBaDXyzAcNumdMAIsJPQ6LJmlqzslHWUSt6gK_fPCjZQ-PUNKg2NirMCcjyXvKucbcuXVhvwaNbjNda-uW-lc4o-aD_si8vtO1Ri23ahk8rRzVo5kXXu0OpMfgzNRkIH9LCks4UzhzXDJ2qCUb4hOqRYGEib_m9gfgViDX_t30cDFj1AQzI6I7n9Hv0mX7fkQCLKo3eTkYK2dBt9rrJGrXD5TYyAMD2mIKQOMRbz7K0_rfrGhjdkZUNjd3llAKWvkNC37W7VuP_fhl39Bo9WypeM8fkC0UOfPKusehcL-IGLYqL1hL02GZbSmK8E7Jt5z8kEysRVmFT_E6XL1YZHi3znjOvpAaGqR1qNjOKkjrtmUNIb7InRGmkXWvQVIatwqRE_lH_wEBuTCLGLO8u9TdTBBW49k74PryfJBNeGcOJxmXZhXZkd18lN7DmQaqL6u6pT2R3nZFyfRmUQ_pQZ0e4nZPMLWuh5vruPikwt4ExiLUfotNE85iwDLKUGu_DLExAZHubpFILbK43RSh-9R6GJnEmbKzHJ8rcOM_eZ-RYZbLcnniRJoPqmDuYiCc8Hz6tSzMHo5qMTVXrrUdipa0vI3bas7Dq7HCWZFgUEBp4Z5Jd0Vlbv6WQMmYKFWETMXASPVXt7DLwujtMR2BiPOszW6Jmo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86343d5e54.mp4?token=XdwSfD6dNBMR2_OxBaDXyzAcNumdMAIsJPQ6LJmlqzslHWUSt6gK_fPCjZQ-PUNKg2NirMCcjyXvKucbcuXVhvwaNbjNda-uW-lc4o-aD_si8vtO1Ri23ahk8rRzVo5kXXu0OpMfgzNRkIH9LCks4UzhzXDJ2qCUb4hOqRYGEib_m9gfgViDX_t30cDFj1AQzI6I7n9Hv0mX7fkQCLKo3eTkYK2dBt9rrJGrXD5TYyAMD2mIKQOMRbz7K0_rfrGhjdkZUNjd3llAKWvkNC37W7VuP_fhl39Bo9WypeM8fkC0UOfPKusehcL-IGLYqL1hL02GZbSmK8E7Jt5z8kEysRVmFT_E6XL1YZHi3znjOvpAaGqR1qNjOKkjrtmUNIb7InRGmkXWvQVIatwqRE_lH_wEBuTCLGLO8u9TdTBBW49k74PryfJBNeGcOJxmXZhXZkd18lN7DmQaqL6u6pT2R3nZFyfRmUQ_pQZ0e4nZPMLWuh5vruPikwt4ExiLUfotNE85iwDLKUGu_DLExAZHubpFILbK43RSh-9R6GJnEmbKzHJ8rcOM_eZ-RYZbLcnniRJoPqmDuYiCc8Hz6tSzMHo5qMTVXrrUdipa0vI3bas7Dq7HCWZFgUEBp4Z5Jd0Vlbv6WQMmYKFWETMXASPVXt7DLwujtMR2BiPOszW6Jmo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
پنج گل برتر فصل‌گذشته لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102498" target="_blank">📅 11:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102497">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwRvnMfsoc2UOnS7sJYlnX2akiSBMBc0dyqn0aG4vBr4tAfdpH5zs_nYESkqgn23gWdC9cqQrA3q76StUgtE7RU-kdrEYzIP7ebH-UyKCnae8IYOrxnU9oZyb-UglwpFLq7KcuccWIn4PpVBQgc1Y4Za-X4L6s47B0xN84AWaqzCyJDTtsPrmWheJ09Mcxuc9fMh31KqKfayqpPWcvvK9rQZRHMJzjZW74zO8YW7U6ewewxNtx4UqYrUj5NU5GJOVRRoxRYHFR4GqLgidM7lJyiggDTsvTSIDgnMsfvnkyuNZx_2g-oGcPIm4kp1Tj9vzF7ONQTPm0C4wFGjcYjvRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
اینفانتینو با انتشار بیانیه‌ای اعلام کرد که طرح فروش بخشی از سود جام جهانی به شرکت‌های سرمایه‌گذاری خصوصی، به طور کامل لغو شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102497" target="_blank">📅 11:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102496">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e324940235.mp4?token=Bl5voWHdlRCMsZ-ZFpE1PTscJ5x4F9yWPvOCfx1on-oS829a8DktxJlcrOpFwlhvNrstCmVqipJ1HUlxMG35vrI0ulaIl00_GF1kS2lTlLuyF6AVyB-0o1J5rW-V-12L0-GwM-jUecW49JbAIwQVWOYrg9NdzraEtbue6c8C_ptAn5l0KOl3X4gNitRYw5DiVaJrWvIZCgdCH7AhqELVSSXsyLzPl9YpfvCU6XE3Nh1obV8NVd7fWu7s7xUAR5zDwXbAr-K-Naedt_-y3irYBeGRTNWMzRjJ2csrQ5nSFGOcjNb5WELPXNrkPuwWaAi33dy2gyNh9mu0P3JLyw39nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e324940235.mp4?token=Bl5voWHdlRCMsZ-ZFpE1PTscJ5x4F9yWPvOCfx1on-oS829a8DktxJlcrOpFwlhvNrstCmVqipJ1HUlxMG35vrI0ulaIl00_GF1kS2lTlLuyF6AVyB-0o1J5rW-V-12L0-GwM-jUecW49JbAIwQVWOYrg9NdzraEtbue6c8C_ptAn5l0KOl3X4gNitRYw5DiVaJrWvIZCgdCH7AhqELVSSXsyLzPl9YpfvCU6XE3Nh1obV8NVd7fWu7s7xUAR5zDwXbAr-K-Naedt_-y3irYBeGRTNWMzRjJ2csrQ5nSFGOcjNb5WELPXNrkPuwWaAi33dy2gyNh9mu0P3JLyw39nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
و بالاخره تحقق رویای دوران فوتبالی کاسمیرو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102496" target="_blank">📅 11:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102495">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👀
🔥
هشت سوپرپاس‌گل ثبت‌شده فصول اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102495" target="_blank">📅 10:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102494">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LuDUKzJs5mE5KePnwIeMi_1iQ9AbhKM0KCULlVIXto517-6VTVbIIQ7QUsAJe9EMj5aQXrvlYEePC0PCAU1_GhBElQfz9LrfibsU1vw6y8s19JnUW_5BjUJg2Fy366aKzrkTfVRJ5Fn5rW0RkBpLt8IKGJRurQEF_bhjpxmHbxksR23HjTxhQvb9lQ6o9PBYyuPc2lWnbmbhHONDBxCAl6C3bCwHHAxtNTmPr3aSLQG1GstnubTJwqVy-FloBtnD5En1_N59tbJwAiU-hPBubG5H5cW0rL2kT56CKIB6BxF0Ss-p19ygQSPCyUm8HH98GIYLZRlPxdqf5Jg_KzsQTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه آمار مسی و هالند زیر نظر پپ‌گواردیولا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/102494" target="_blank">📅 10:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102493">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvfujV1Z40npbDQYKOnmQyKyWhpoGRO_5YZ6ts1LZuQCHpVjwCfDi2YFbhq-HSrVhFhiet9LKjwQo6Qijo19cCBF42ohyO-IRJ54e1qbSeoWyfQf_EKTHU7Logz87Nx7HaM1KA9_s6GWfpmvzYHy_Ga4IsYa1aCY5KoSSjciSvpHLaDnO_s2eUK7KBd_bkc0PwQDSn6r7LieHLPO7zmqs5La6bXPpah40y0-8_yXAkpbwWoOhKKLECW8IXxpBtoyRn4eXtyybgAEpqK_xvzmbdwaaHGb6CGAvbCmFu98pWeaipP1De8y2c1Dk74d_mBR4kv1PJKf38pcfIO0S6tAhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تمام قهرمانان ادوار مختلف پریمیرلیگ ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102493" target="_blank">📅 10:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102492">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBunBdXNXRojB0gaIfOTwYOI3alXNeX7sh3dnTrF0jZ4cEvPpubAyAS7tDj0D2OaxOfgZC-Um99Ql09OVG9Np3qG0YSlazTTcCwK3RCKR8NS5g9_qurQjkdBRVcxhwL_Hohp8fyyDWt-rp1UJ3VpZ1qPJM4fxV57JCzXlvWl2IwutaJ21SwX67242sz7kfAvDKhtjvmgazeAdmrnYwQ8ZYOLYTQh_azq4kkNqG21P-K8R0DTWm3BSbNDY3UXOsG84DogSxrTdcN4jtErrQa6Q6h_ifE_pDNPsiB7C9z3W43Z_EShS4RyPOyKrb5sEO0km0Nudro0NGnCevKAqzLgwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
باورنکردنی است که برخی از زنان چه توانایی‌هایی دارند!
💪
ژوستین وانهائورمات، هافبک بلژیکی تیم زنان کریستال پالاس، در سه‌ماهه سوم بارداری خود همچنان در حال تمرین کردن است
❤️
او ۷ ماهه باردار است و همچنان با تمام توان به تلاش و فعالیت ادامه می‌دهد
👏
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/102492" target="_blank">📅 09:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102491">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5RQ4eI3U8Fm-COxxW8lK1aodHNFLoJsLSt-zgbKJ9NA5SVkfnQJKSv0MthjWxovUGeEbjZZqEULNyV6719LQzuVPli2ZhCXyJzChLHuUVeSjhKF0jnippBB0D48ALHSyhJ8QbTl2CiGIHRK5Nib5vG7ZRRQkzKQHyQW96CtHBlBeNZMCcyIk0q_n3pXEbCxBH7r74iZo9b92z0RT_0eDMyTn5zSEw_KCRr9VcC22t2uTNbMC2eKfLMgHKszWErD9xKlKzti6_MF9ZxpL6sUcX_ObiFtI5-5ic-ijmtKfmQdYqXb1kHYOXcpoG0IfadL2vmVbd4KjeYskQUgdbnOXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
🇫🇷
فوریییییی از فابریزیو رومانو: پاریس بازم وینگر خرید! مگنس آکلیوش، وینگر راست ۲۴ ساله موناکو به پاریسن ژرمن پیوست. مبلغ انتقال ۵۰ میلیون‌یورو و تا سال ۲۰۳۱؛
هیر وی گو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/102491" target="_blank">📅 09:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102490">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b17b2ecad4.mp4?token=bzBR6DKt9lRKeumx9HAdkUIxhjQg70eXGvLLwmJU6X-5JFMCTlECl9-c1TWTJYbjV5c1GQHOz0D2oD-1l0VTbHsWrKAqt1WqtoIX2kR62kcxFWp1x1S316KOY3Do-DpRBTOzqwIoCrzZ1sD9L3mgww5V4w9h-PtTL3uHDyFeccWSvOl9cy8nC5mepI2XgvDiK8hD2qmO3J8GAd7EGxMVT8j908AGnS0KyV0Mi5pdgBbR8Yo1J_7g4juMjlJqQPB7rv7IOM-SLGPzyLzIAj-rfwiLbWRdsFNKSJSQJs08__VPwTBBngwlbaS1fhx2byuIhYO1uXELzZtFZA63iSJnXpssTbXQOMTAcpziOsyDRr3kNIITDfoRXgLLMob9wK8ZE5fEUHS7M6zAzYTWoR4_0Eot5f37jGyj_rFElGcI4DmdN1Xfae__KFC1Jcwhbm8QOg0yMp7iUkWPpgvXVoaxxCcW2CCQ9y93ZGWBM8vForzuMb-YX1IJ5iKgL_B75mJi6e-frpvoUs614nlZ36DSOowM7zXmueHCvpKnbE4zvKCELYFgoXyLYwmFib-Th-FPR8RR1SfELHgsIl7axPSysI89HJ5YVHL8B_CVrIMQ-Foq25Ejn0Tagu-_VR470Nnn2ehMs5rJk-8VdQiQNAym1E8wvufJok9-vbDkj_50WVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b17b2ecad4.mp4?token=bzBR6DKt9lRKeumx9HAdkUIxhjQg70eXGvLLwmJU6X-5JFMCTlECl9-c1TWTJYbjV5c1GQHOz0D2oD-1l0VTbHsWrKAqt1WqtoIX2kR62kcxFWp1x1S316KOY3Do-DpRBTOzqwIoCrzZ1sD9L3mgww5V4w9h-PtTL3uHDyFeccWSvOl9cy8nC5mepI2XgvDiK8hD2qmO3J8GAd7EGxMVT8j908AGnS0KyV0Mi5pdgBbR8Yo1J_7g4juMjlJqQPB7rv7IOM-SLGPzyLzIAj-rfwiLbWRdsFNKSJSQJs08__VPwTBBngwlbaS1fhx2byuIhYO1uXELzZtFZA63iSJnXpssTbXQOMTAcpziOsyDRr3kNIITDfoRXgLLMob9wK8ZE5fEUHS7M6zAzYTWoR4_0Eot5f37jGyj_rFElGcI4DmdN1Xfae__KFC1Jcwhbm8QOg0yMp7iUkWPpgvXVoaxxCcW2CCQ9y93ZGWBM8vForzuMb-YX1IJ5iKgL_B75mJi6e-frpvoUs614nlZ36DSOowM7zXmueHCvpKnbE4zvKCELYFgoXyLYwmFib-Th-FPR8RR1SfELHgsIl7axPSysI89HJ5YVHL8B_CVrIMQ-Foq25Ejn0Tagu-_VR470Nnn2ehMs5rJk-8VdQiQNAym1E8wvufJok9-vbDkj_50WVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
بازی‌خاطره‌انگیزمیلان و یونایتد در UCL 2010
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102490" target="_blank">📅 09:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102489">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">هایلایتی‌از بازی‌جذاب الکلاسیکو در فصل ۲۰۱۲/۱۳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102489" target="_blank">📅 09:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102488">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7q3yDIgOI6aD9ghFxhJoTVh4n0mdf0EeF7cgAIfUN5UaLBoPodJQ7fABvyAn0A2_IgWzidZd3yq5DiHSmahw9bcm1nB38TQqsMUkKNQNcA_0MuuDDfNha7Knt32VAYGrrEZvbmKYsxg6MYEwnMuARJij9-XoaotDAR0ExOgGsUY5Rm6vwpUbbpXfu8NP-tLVuY5MYgB8Ihzi5rs2f4-K4q-49zAwKwT8Bt4a8htqvVmlWMMK2OvNvvPZt6ZuNJsZwb5iMZDPRK7Q1JLYmS4wbrzCgG-d21RNsksDExh0clfkcjk5TlfLY4LJWfazfydvawqu-mfCFJNPie0lGxpuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیکنای اون ترکیب لجندری بارسا چی میخوردن؟
مسی عالیه :)))))))))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102488" target="_blank">📅 05:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102486">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVTBcPfyetQUBD6bmidKfiIGhua_y-HyODdsogg8bwbag2vRIeeZJRuQzkrgyGEfkAQpFgk1bSOmqnQjgfH4z9b_I_9zeth6ozBsJbs9QkOZd74oB00iiQ5NzqBhgQSx2op4YXyRb_mCrAe-OU_L_hVchom41b9RRb-jjRBocZUgD5fBB_8tlATHvT-V_pw1uxRBRTtQz48e7YezwnUyxuSHZyu7x7nmR6n56SNv4kSSYoy6s5y1fFIJPAG7QSs8tXo_c7wIQ62RPdGA0u--d4rCXyQu1W_taEFAgySqY1cKmJr7rHgaixHu0fssGM_tCTyQuYU1jWx976Ek61tFpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
گوئدس ستاره باشگاه آژاکس با رقم ۵۰ میلیون یورو بزودی به psg ملحق خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/102486" target="_blank">📅 02:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102485">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
🇮🇱
کانال ۱۲ اسرائیل: نتانیاهو در دیدار اخیر با ترامپ موفق به راضی کردن رئیس جمهور آمریکا برای بمباران زیرساخت‌های انرژی ایران کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/102485" target="_blank">📅 01:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102484">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIXgLYHQo_7b-Mz0J8nW6ZeV7q5LFPQhUM_Be0r0Anl7LNdCJ1otIeHWeYzFJnL1HvEiNU0DXAHikMo08T1qYiQR0EnWORq_cDFvMSdIJSVmBy0e50FFkgzMgaLkJI9K81KfAryImJuFQtq8-nGRqWPL1fPot3LfC6UNqV_z5mHsT6o2tOlKTdKqdAXlcPm6j1K1CiZAyZJNrdSTV6AXDKg7OPdzKEFU8kyAUk_9AHMzgIann7mOPwIUhlzhQsRAeFKsy37Q1nE-8LV3a1ie0za7Yy_-3OL7edDAFaQGQVdPGAGt40Nn6_KJEKdrcDNVsbkSHcDZNmuvYJUin6Dlww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب بروبچ محله تامی شلبی حسابی واسه جود سنگ تموم گذاشتن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/102484" target="_blank">📅 01:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102483">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔝
وال استریت ژورنال در خبری فوری از صدور فرمان ترامپ برای آغاز یک حمله نظامی جدید آمریکا به ایران خبر داده که می‌تواند بزودی در این آخر هفته (شنبه و یکشنبه) آغاز شود و چند روز طول بکشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/102483" target="_blank">📅 01:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102482">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edBSh1GaeRuz_SnJxCe5heoOIidGWrOlkBi4pdNa_Ybi_mWeqsTS61lTv2C0PauZ9jUPilccCnod-EgQAlFJ6a63Y-FItjqTHRJTaBGqcl_PQPJ8BMT5vx3n9WJS2XIoRgKL2YpY6R6XYm5qT2q-wXY2osRlAT0jxsdnigDNibr5sVcfp4SINpnH3W4nmZEb7yEVzehx3nWVJ1LwsAcaRLnSv5WskzD0mi3SIRY37VRlYAY8s5QKyYaxwymBJNjeqmUma0HB62tBaTy-NU_if1q2Nin74ynFXTSoM4LnJ8tWZa_93tmBU-J3-dbTdRdvULplIIrpoJRq7y35TJTtKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔝
وال استریت ژورنال در خبری فوری از صدور فرمان ترامپ برای آغاز یک حمله نظامی جدید آمریکا به ایران خبر داده که می‌تواند بزودی در این آخر هفته (شنبه و یکشنبه) آغاز شود و چند روز طول بکشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/102482" target="_blank">📅 01:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102479">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y1lY4nX_NS_1lGl76WSpFtpCttQvzASce0ln1DlP_oDEJRzHqR35SfCbeLIGQft_dvHjRD78kE2boANSDaMPuUAnytaSs2ajyFz1dUnqgSBYFDQlFdUPmBrIxhNbWkKiNwTydXBXV9nr4y8pm7Eb5fng0BZIFpNzmCLykbYCmPIz_ViVBYbC_j-1Qq6aVOQckY6iwK57oFiWo2Bo4_kUW8XPFFOL__cE1ugKDAQB69KslFTRKYVkrDzLpYnruDPxpqcsSZ9kzod1yjt586HPLm8aCKhSz5LFQ1I-dwacSA8c3qVsSlhTBUSCk8prnu7qHS5JCHdbVQHPxkB2VRhMXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iim-C1yAFr6WptGSNUeEHDpMVnWjUe6A2XkpuaCVcsHBghnaoRT75hraA6xfJFJC0WguiuboBvmJafGwUE1GSKWsWMupVtj0k_QdEsBlgeRs_hW5uEfpBP_fFo5eFUlvqVN4OyYZN5iquAs-M1my36BYPES06dXTavWyTcwH-QY2WQXeF93covsRROnyAdJmRc7NJtqQCbmKAym2JEcQScUKxiONui8VKARdF5En7b-AYtAU4V06l801c5gWpZWWuwTDsgxILc0Ax3ZgjYr9KcW3G13L6ZfeblyDUUjA2tC7XeHN-iYQ23AdDcnvLvRtmIaeJEUk55iNVRrs5tdxjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j6deKlP5xYjwdAoUOsYZWyb2kHDXxua9_mr4Ds00_R3I7P-MnO48rYPvWKHBQS2XeHUiEt_XhdDbGmlL1o9UVEd-wc2zPXhaSdFxUyw2j1H4kNVJ_IhausjpfkPpfGG_leRxuIzdbcKOtvRlBAto4CigvJphR9QpkBjMNXIW5JoigvLLTn_3JvvyVlk0qDqr-hW47z1ndexKD_KvMb-Qp6nk6RYoD8p6_m4Koq6mxh-CFl7bYEcQAVmkJjdzzmjrkTA9Tusxm_Xh2xNXAbmNsuBZN5AAb7m-T_srYURCjqm3RgOjPWfCV_ZclsioqPyDjaKLccOJhdHXWV6CmBW9Qg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
باشگاه فوق العاده محبوب آگزبورگ از کیت خودش رونمایی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/102479" target="_blank">📅 00:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102478">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpyEIXGlZM_TfOpyoNyW1XduKNYlTojlz14KCTOkALMpFn1mwI2TrFJDruIoeIAgDPIO1nk62FxRTir3WUu5JaSN1XtloQXgIkvQwFSU1k4WrbJllrvDIVw-O41GoqfMePMkI31PaQcc_wHsrch3it2fej9qto164gBwZQBC74gUQNBxKmh1c1CcCgDuiC-OnxcxhGGscZyhselkqcs9MWsxj_zCTZzxusmUccRwKIR436waDuhMfx1rATve7jVE84HpJ48eeg9b3uZ1XPAYcFrjaqW14KpnRcxnDwQh1gWAXL7v0tL1hJdtLKiTBIDJNAJnsn38nrt3by_RRxU3oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
هندآف آرسنال رسانه نزدیک به آرسنال:
وینیسیوس شخصا با آرسنال به توافق رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102478" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102477">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی،…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102477" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102476">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=eSfk7NpZmP72jvOQ23EsgLqPtsJrQe2GCl9Cs3vIgeEWyrBpBfa9FIkFhAwOuBB14Ns0i3dEShcanI9ErQEm5Q60wpAqQkB4mH5I6ij-MF8MUJ_Lspgeh1Gt4WSraVIiKu_znmYV3Sm6LTk24AooS6HwGXwYUmz8QXQk6g2CYeO6C-hWwI-xojl8Mq_0hCyZytg0CYlW5OwE04Ty1H-zIffSWlY-uwyDnD-5jcwQezWtGKqVhTKEiWaE0j4veN9VE2-VvesPSbvHiTnrK5puh3txf9pFYycen2dgofOAvlGBVE4KYikNu8sHD8ZAPuHEZEN1IJA-944NyDy-9jputQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=eSfk7NpZmP72jvOQ23EsgLqPtsJrQe2GCl9Cs3vIgeEWyrBpBfa9FIkFhAwOuBB14Ns0i3dEShcanI9ErQEm5Q60wpAqQkB4mH5I6ij-MF8MUJ_Lspgeh1Gt4WSraVIiKu_znmYV3Sm6LTk24AooS6HwGXwYUmz8QXQk6g2CYeO6C-hWwI-xojl8Mq_0hCyZytg0CYlW5OwE04Ty1H-zIffSWlY-uwyDnD-5jcwQezWtGKqVhTKEiWaE0j4veN9VE2-VvesPSbvHiTnrK5puh3txf9pFYycen2dgofOAvlGBVE4KYikNu8sHD8ZAPuHEZEN1IJA-944NyDy-9jputQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی، باشگاهی و دوستانه)
🔹
پیشنهادهای دقیق گل بالا/پایین (Over/Under) و گلزنی هر دو تیم (BTTS)
🔹
بدون ادعای واهی ضریب ۱۰۰! فقط سود مستمر با مدیریت سرمایه.
آمار ما در ماه گذشته خودش گویای همه‌چیزه. فرم‌های امروز رو از دست نده
👇
🔗
[
ورود به کانال و دریافت فرم‌های رایگان امروز]</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102476" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102475">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GC599jkIGJX1-QzQ0iP293sqGM9ZPI2S3b799DCbIlm7Foj-P0d_uB5GzO8nfKE_hYut2-k0mwT38Mo7z7BKwn07afE02Y6bLz6GdiVozzTnwb5NubcY_d82yBlhNk3fN8aAdNrfYNRcH60gIYyJbaR-FaJ1EVlwErLiyturZpYQG_4R-3wxt0V6sV-Rz-6HEo8lqKFGaf3h-CePim62NBQqfalxpLGXVt7UaxiLIx-tOWmCxpJgnlPJIVXv1VZyLQTB1_rZRIWxPg5Y-3oNBrTCW3MGDDNOBIr5MUSrcGfGzdolQ7P4W6mKQ9ReGfYSuDPNM7DtntLyVNeUrI5n9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
بارسلونا در یک بازی دوستانه مقابل بیرمینگام شکست خورد. بیرمینگام با نتیجه 3 بر 2 در ضربات پنالتی به پیروزی رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102475" target="_blank">📅 00:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102474">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GaySU_x72ruMbOaULlzU2_-KZ2-jhB2nl-v4OaFPqkdTZsb1S737v01xy2SIfXzvcjVjA1Rk1oIabQ6EFEvDPFwRqj2mrvVrnuxWVEtG4dLU-kKc6YbP7XQJcavUM7NZg1nqDNli-XQfkpChaFxT5vjzGLmjsfrwV7qFEPA2TfLnanIx0YEY02C03k-sLyzY5BGBMd7UQWwlN16p0tfDWxpbcneG7mQ3tpd4LnQKUjvGy0UkMhTSmHek7HG2I0dMabz1tQObMf3Fl6S_QZqIJG4q3ZuJP_qLRsar2OS-UxDY_BuMYMefOXRruG0dlLK1aUG7db5xubqG6VIgs23HWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری دوست دختر یامال
😦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102474" target="_blank">📅 00:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102473">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDvcY2P7FCfLBUWcV9DpYOe8qcelfJ77TP1pRx1Jk-1D30ded8zcZHZm1-TdcXzXeERfDaDT_KKfAkjJXA5LIgSkkvNC6IcPZM_GD0tybTuuOhzHYjW3NULOITG-TjNeEG3qo8N0a2J1B_wW9mY39LB01zXimnnNDK2OpggJBQeakYcQ4zxNnWAgAAFaDACPyZythGgQBl9hn9wiP1T3w0A2NYpvcSqR2KOzqdS13-RGxGKqZHp_iIiwHaz1LAp5HVBt1mPuaeSbsQF6_j4J37B4M_TJyTeK5zCTwTe_f6YUbcWTB8x6w65h7yRpdvo5w84bJpBxP-FJUw5rkeACaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟥
🤩
خداحافظی امید عالیشاه با هواداران پس از 13 سال حضور در پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102473" target="_blank">📅 23:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102472">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzEsf9B1PEdkCcZemn7zdHZqI2w6uwFVoReTBDG1Y31l7bZ6grqx94T4Qcqy9QhYPmpWX7Sk-TOMRobba6AACvkCFfVLwtguwDACL-6TxBB4_LTfY6YXhY0S2BkAbSHzacLN1ulrVssoYv5jSOfoYNwvFzR_qPpXSF00C_u2sXHS_XpCYJV5gX6aBCSDJbgX6eaZxBpTSt18pkkOgdUc_3Fpz7juSmvK1DLEdpYF4Ir-fKKNg6_yBNd43SDTHvxbQhahcHpQfN-DWW4WA-EHVfOIyxKdWC1OYA78o10jp3tc5DHfU_bQe1nEL8nLAMqfp1elE9GtQ_9vAC2RzirBUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
مسی و کاسمیرو تو تمرینات اینترمیامی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102472" target="_blank">📅 23:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102471">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26c665525c.mp4?token=emlA_8UBQn-dioXa2gCueytfFpv0o0ltK5s9mf56Yx1JxuAM2ZbsISaZqjjvRaq-ToYUWW4dZ29CNVC417EYEzQPYyWHqaTduXYgZyhDeETuGs0MTYkz7cWYuK4249QS2TV747417CNMajpcVQB6B4Pwf4tyUVMSqqMLrrzApnoHO3T_1P6tjeCUmOAigIAv8seury_Xm9izM3MKhRmhT1om_DCICiRqYdue7ZoBUp3CnzPfuEMunL9FchOPkI_YfUP7uF3rUhF35tE99EPSCIFFM5NVFvQAUptijQEFk9SOAhgUGNjOJ4vrPqnAsoIssHn7YEGDnLt6x2CP48nziQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26c665525c.mp4?token=emlA_8UBQn-dioXa2gCueytfFpv0o0ltK5s9mf56Yx1JxuAM2ZbsISaZqjjvRaq-ToYUWW4dZ29CNVC417EYEzQPYyWHqaTduXYgZyhDeETuGs0MTYkz7cWYuK4249QS2TV747417CNMajpcVQB6B4Pwf4tyUVMSqqMLrrzApnoHO3T_1P6tjeCUmOAigIAv8seury_Xm9izM3MKhRmhT1om_DCICiRqYdue7ZoBUp3CnzPfuEMunL9FchOPkI_YfUP7uF3rUhF35tE99EPSCIFFM5NVFvQAUptijQEFk9SOAhgUGNjOJ4vrPqnAsoIssHn7YEGDnLt6x2CP48nziQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین ووزینیا که تو جام‌جهانی تک تک تیما رو سرویس کرده بود، جلوی علی علیپور اینجوری فحش خورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/102471" target="_blank">📅 22:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102470">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpeGs3nx96bvmOx8f9GFjcFC8y1JtVXkjfRmXIvWA56bPTPjYTJRBOslQf-VdoBrlY2WseCUIVNPh7Ius80WwyWihwimB2izgJX9K0hjw_jROPrrcaDinLMRFU5zIRnCNpUaoobyvOSP93OHEBn9FpHLwj35NjKqud2s14RWqgjqVGokH4pDSP0nN6jdsOzkWxRSqPubqGa8x6q6c9vce716axmT-UJ-MZp0cuUy0u6Wfx1ueX1qtu52FDiHDtBW-9xjMoteUt6LWs5RDwig_ysxxBphjYZJWI-2x9XurK4dZQ01Qj3ZZY8iIzkZoaInVmdBXSrxc8HBE3FYJEP_2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ار‌ام‌سی:
مندی تو وضعیت مالی بدی قرار گرفته در حدی‌ که مدال و کاپ جام جهانی خودشو 54 هزار یورو فروخته.
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/102470" target="_blank">📅 22:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102469">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/261dc7eb19.mp4?token=DfqT5Ly_XxlFiNqpWGz83y3QHwaG1U1XlA-X3MwzJsTSP8N5TtYLsw2I5vhAFDscEVFCtQeFbK69RPh85c9Bp9ttif6Vq1zip3OnjDO0zFtpxzwB6PIGXjuxFNh-MgSLSQCt5J539PwIfaZ9_B3xgX8ce9zunzYKx7OnNKTi24fRf6qE3t2TnTuGnf2Hvcka_NBnKqxsHCQWYSkD2j7Hdb3hEwOtILyWnDUGXeUoGpnQQE1XV4gsc-VkpVLrp1DAfIcMHiyRn1uU7L6KEf2QsI5yNibHcnBGwJTo7rMGdZsqxAUEwZPb3S6UNwY3kEnmbzn1ownJIgwjiK7pLCVbXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/261dc7eb19.mp4?token=DfqT5Ly_XxlFiNqpWGz83y3QHwaG1U1XlA-X3MwzJsTSP8N5TtYLsw2I5vhAFDscEVFCtQeFbK69RPh85c9Bp9ttif6Vq1zip3OnjDO0zFtpxzwB6PIGXjuxFNh-MgSLSQCt5J539PwIfaZ9_B3xgX8ce9zunzYKx7OnNKTi24fRf6qE3t2TnTuGnf2Hvcka_NBnKqxsHCQWYSkD2j7Hdb3hEwOtILyWnDUGXeUoGpnQQE1XV4gsc-VkpVLrp1DAfIcMHiyRn1uU7L6KEf2QsI5yNibHcnBGwJTo7rMGdZsqxAUEwZPb3S6UNwY3kEnmbzn1ownJIgwjiK7pLCVbXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
تام هالند یک‌بار به ارلینگ هالند دایرکت داد و از او خواست به تاتنهام بیاید، اما ارلینگ اصلاً متوجه نشد فرستنده، بازیگر اسپایدرمن است. بعد از اینکه ماجرا جنجالی شد، هالند برای تام پیام فرستاد و توضیح داد هیچ قصدی برای بی‌احترامی نداشته و فقط او را نشناخته بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102469" target="_blank">📅 22:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102468">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ssdmCRwsum6A7FZnIY22vXn4A_v884UA25b5PrzfyBs6x-XRtbnPrnBjYBbRyqYREXZ9LGKUFRIrnfHkv3ydJy7jKgfODZKLErW5gB6bDWUWyzuuDhHLBjUv_uczo6P2qOB-BcZ5M1A9nXQDAhrCuV8a8rLmMXPHGT7HxltUXT6BtmPHEV_nTeRVvQ-ahmTMwTQ5S5Q-eljxOxsmgtE_8pRq9pGPhVKN9xkwlqU7eBcPNWbyzyL2XFlioA2TXIk00JhHumcRGnd8SD9YB2CK3tmwk5Z04_HCwm7Y-1Aji-3oniaA_NUU0iOggalDhClqQf_v0DajphRFURlS4NNHyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
💣
بمب لاپورتا ترکید:
جسی بیسیوو، وینگر بلژیکی کلوب بروژ،
به بارسلونا پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102468" target="_blank">📅 21:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102467">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dEdhMM_Sni63hqOSFWD3xR3JL1P87E9U3aHGaZvA3x_W34VAEj3gmeNaVPGvfQSJmrl9Ck-h7rWJGgsRpS6by_dKU2Yk4zLgTmModGOdVeGuVm4URHoMO_LG1kGz5O0tJHedP2pGOQwUDXLNlPNP8Xo-iBtyGYm0BDYduXXTlizQAHd8xyGXozV_g-jlcK3fXtmoInLv7vllLA2SSNX4VqyTtEZJCcIJX2euRvv2mov8pRTNtJLYbx3e5bGrd0urANldZZRy1LtoIr0ZTce3tGG3xf47sO7LoY8zBvhFzYaF70BfiTPFy4EIr8EA93jFQEYOPx84AUc7zNrtw4Jbfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب امشب بارسلونا در بازی دوستانه مقابل بیرمنگام‌سیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102467" target="_blank">📅 21:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102466">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f4d6d3d7.mp4?token=Ty2s3P2zIHU_PM9e1FuHd_5rCTODBD5eV1JsSvzUJcS01kxGbwtgeoEWOUkYCpVMAmzElP2R-4SRblhvMXBacp-gKBP2j2rYhUufx3ZbH3raUhCg-3apt1Fbv_Eoiko9nxutK50hDaGuZkp1234S4wgWM261iK76zG4mNToKOZSHbnT5ioG629ax-5KtEe_CcdjvCMzUwMuVFam-edYnsDYaRv7gSNf9lcPiT4aYpYAJe_7ab8b8OfKFd6neJf6yuDqh6mmEKz66twWaNwNFNs7sXQipfhIsvZZtYe5uoCiJws5UqoQe943GtIV-ouZu71VBvxAgStJ_1F7YGb2H3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f4d6d3d7.mp4?token=Ty2s3P2zIHU_PM9e1FuHd_5rCTODBD5eV1JsSvzUJcS01kxGbwtgeoEWOUkYCpVMAmzElP2R-4SRblhvMXBacp-gKBP2j2rYhUufx3ZbH3raUhCg-3apt1Fbv_Eoiko9nxutK50hDaGuZkp1234S4wgWM261iK76zG4mNToKOZSHbnT5ioG629ax-5KtEe_CcdjvCMzUwMuVFam-edYnsDYaRv7gSNf9lcPiT4aYpYAJe_7ab8b8OfKFd6neJf6yuDqh6mmEKz66twWaNwNFNs7sXQipfhIsvZZtYe5uoCiJws5UqoQe943GtIV-ouZu71VBvxAgStJ_1F7YGb2H3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔹
وقتی منچسترسیتی حریف پیکان نشد! سال ۲۰۰۲ پیکان با سرمربی‌گری ذوالفقارنسب برای آمادگی در رقابت‌های لیگ برتر، یک اردو در انگلیس برگزار کرد که در بازی دوستانه مقابل منچسترسیتی موفق به توقف این تیم شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102466" target="_blank">📅 21:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102465">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bcb0e2d66.mp4?token=ELxuLMsGL-Q59ehbCFMYjZIMWTCP1fgY80tk4N1zREV8oIIloGMAatvLTXLqbfSG8DPDAZ855gH7v5x83iVQfVSVrbvfImeAYgSAzFasu4BhW29AwzQ1NoEDkPIa8qGJ3qgo6XgQpJGhyrtNq7z-SCP-cBGXImpuRG-BiKab32BQE0Rh5L_-FTwVq6rtiih6pt3XVZOUbAXDejG9a0ujetec3mzGheOHfz8yFAW88iN4cHBbSXEgZZcEZGoJYQwpvve1UgwUIABOj8wkFMjKAogMoW1BKQqZxXYLVIatrHkyJMcnn6xN1MBsGYStWJGsM5M-p3TwouJeIJ8We-IXfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bcb0e2d66.mp4?token=ELxuLMsGL-Q59ehbCFMYjZIMWTCP1fgY80tk4N1zREV8oIIloGMAatvLTXLqbfSG8DPDAZ855gH7v5x83iVQfVSVrbvfImeAYgSAzFasu4BhW29AwzQ1NoEDkPIa8qGJ3qgo6XgQpJGhyrtNq7z-SCP-cBGXImpuRG-BiKab32BQE0Rh5L_-FTwVq6rtiih6pt3XVZOUbAXDejG9a0ujetec3mzGheOHfz8yFAW88iN4cHBbSXEgZZcEZGoJYQwpvve1UgwUIABOj8wkFMjKAogMoW1BKQqZxXYLVIatrHkyJMcnn6xN1MBsGYStWJGsM5M-p3TwouJeIJ8We-IXfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⚪️
رونالدو چرا رئال رو ترک کرد؟ شرح ماجرای جدایی اسطوره فوتبال از زبان خودش.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102465" target="_blank">📅 21:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102464">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00ed94c011.mp4?token=ojxfj80bpN5-KMMLdBvnSqnEmgLJZBTir7sDJHS4Lq8xAHI_Cf5-aX-D0KOUVJdGhaMrGYmgZhJatFPd_4_bLqCXNbJ0lw1NIVuZspeI8TaXVHknAGAV5RYoZjlcR4rsBI2JIsq2CLUpn3fW62JvFHRRcsPkckAblRAQgkhonBwWRrl3GY0Tv35H1Xt1MeGd3cS9pprUkrnNCAuo1mhfrHjbv76IiPdFT3dITyYeB6qLSv8MeB_QIqwpoVNFvoTsLkMJ2MTpWQhwz4uRmyI4g6PVOn3WB9lgWpseF4otOuWOhkTBHFEaWuiiGVwYVmDIlOTvZTgEP0XymUoQ_FO-pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00ed94c011.mp4?token=ojxfj80bpN5-KMMLdBvnSqnEmgLJZBTir7sDJHS4Lq8xAHI_Cf5-aX-D0KOUVJdGhaMrGYmgZhJatFPd_4_bLqCXNbJ0lw1NIVuZspeI8TaXVHknAGAV5RYoZjlcR4rsBI2JIsq2CLUpn3fW62JvFHRRcsPkckAblRAQgkhonBwWRrl3GY0Tv35H1Xt1MeGd3cS9pprUkrnNCAuo1mhfrHjbv76IiPdFT3dITyYeB6qLSv8MeB_QIqwpoVNFvoTsLkMJ2MTpWQhwz4uRmyI4g6PVOn3WB9lgWpseF4otOuWOhkTBHFEaWuiiGVwYVmDIlOTvZTgEP0XymUoQ_FO-pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یک تازه داماد پرسپولیس را حذف کرد!
از ماه عسل برگشته بود و چهار ماه حتی توپ به پاهاش نخورده بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102464" target="_blank">📅 21:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102462">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🔵
🟠
استقلال در نیمه‌اول مقابل فولاد با تک‌گل ابوالفضل رزاق‌پور شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102462" target="_blank">📅 20:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102461">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f8b6948d3.mp4?token=WoSzwj54o4GAK6WP9JlbYd1W1jsH4WoRWbuSJ5PXJJMXPz-5e-YAcDDCCcgF2z3dL3LDcIQoBQNzoMPG9jnWcjhjZdIRDqZPG3tjQOLza8of7J0fICAUDv_5fxnJNqMO_7_Dlma8UD7i52JE-rx-oz_aHhRPw_RFvyNCVFZrcZWPHKZlyOFhWOC022qE2k1EKeDIovSC6sYeP0yomdhgbYFb34xXysArpY3G39BGnZ9uxH4j-7gIvwV-sdsU-Xk6WaADmzGQY4ouQlyQeYI-t33AcuqgvD-CqDWyrM7Br2BD3JkVBCEiWqY1IBg-fdvIHi6GKQcg6CwA2vj6Ldgz4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f8b6948d3.mp4?token=WoSzwj54o4GAK6WP9JlbYd1W1jsH4WoRWbuSJ5PXJJMXPz-5e-YAcDDCCcgF2z3dL3LDcIQoBQNzoMPG9jnWcjhjZdIRDqZPG3tjQOLza8of7J0fICAUDv_5fxnJNqMO_7_Dlma8UD7i52JE-rx-oz_aHhRPw_RFvyNCVFZrcZWPHKZlyOFhWOC022qE2k1EKeDIovSC6sYeP0yomdhgbYFb34xXysArpY3G39BGnZ9uxH4j-7gIvwV-sdsU-Xk6WaADmzGQY4ouQlyQeYI-t33AcuqgvD-CqDWyrM7Br2BD3JkVBCEiWqY1IBg-fdvIHi6GKQcg6CwA2vj6Ldgz4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شزنی جنس رسیده بهش و مشغول دلقک‌بازی تو تمرین بارساست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102461" target="_blank">📅 20:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102460">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ace3163b65.mp4?token=EXzOx6DMFDQq7KI42tPImcPLtWn2EI86ZZJV2cP31a8w6vO61huomMnmjdNA_a6Oa1ZpVJfWeKavqxf_cA5Drrn4YVXzd9Qwns-soe-_RdvA-3vhHxXa_Dc_MguC6ecpq6nqyrx08glnQUhkh97gTVBtvcrVa4URgONjdxV94Vg9vdzMc9N6QAwe7DzVk_bfUaz-C2gBwPpFnhDxKDudUxKP2g7tyfE3JkY4zp4-7Ak35M4Zs69mbg4ky1i3LJg5MFrqivXIIjxCHFao2XFaez90z6DqJ8KeW6wGHqIWL6AdtdJxienK07oN9Ymi70JfZv4fjsMVwaCRq53WUKGyfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ace3163b65.mp4?token=EXzOx6DMFDQq7KI42tPImcPLtWn2EI86ZZJV2cP31a8w6vO61huomMnmjdNA_a6Oa1ZpVJfWeKavqxf_cA5Drrn4YVXzd9Qwns-soe-_RdvA-3vhHxXa_Dc_MguC6ecpq6nqyrx08glnQUhkh97gTVBtvcrVa4URgONjdxV94Vg9vdzMc9N6QAwe7DzVk_bfUaz-C2gBwPpFnhDxKDudUxKP2g7tyfE3JkY4zp4-7Ak35M4Zs69mbg4ky1i3LJg5MFrqivXIIjxCHFao2XFaez90z6DqJ8KeW6wGHqIWL6AdtdJxienK07oN9Ymi70JfZv4fjsMVwaCRq53WUKGyfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کول پالمر:
برای بازی مکزیک - انگلیس بیدار موندم، ولی بین دو نیمه خوابم برد!
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102460" target="_blank">📅 20:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102459">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5IoXpsHmWnWAIMAF6uRxhJ0q9cvjqrJ5RvzHwQrlXNk15Dg5KjR3bS6jTh6PKHr7dkWesmvPUKojkpLBPvq8SE87klk-hZGREDFJPRKr7PqlTiIW0BX5atc9SNaRz5FV3sczq0ALHEkAq8jJ8_cAAaGnF4W8On5TMNAU3LGEfrqfNv9iPCC7p-kQlBed7lhjD8idrpt24tERaJGFFSd4GBtA_wqgYTZsTKF3MwzuHUAFpngtQ4lv6HcZ1spu9Q1_6XNcAM3Ei5D6_0pgji65575V9x8zk7t8r_yNIJ-_n88u1MmBn4QVPT053e-Ra6_Apez9q64aL3bgKr-_vajbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
دیوید گرافسون دبیرکل فیفا تصمیم گرفته که علیه اینفانتینو کودتا کند تا وی از سمتش برکنار شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102459" target="_blank">📅 20:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102458">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMlG67V5ph98IkNEzZzTeuM73f_0wwIVT1MyXnxmdvhoVAEmDkz3R7NLW_NyIpSYu5bKjKrTju-4z9BQ-zib-8y0tcxL35bcN3eBs3RMdWrpFgzzEvfb4GlMmFuXm9GOmtmTKEUIXdRYyebGJHy_8B15A5Sz5WGAIvuwJrz2QoKtLDGGegMDiiVTK46DX1BmLs4jDE6wWpw-0v_fXvZyAqJscNHP9A3UzrNyEbf3Wmo0IVzUIVuncHs0opSF6v8m08mZ5g50bo5M5sdx8yOAxwM2qM-XlJy9JN-mHOu-QEMouLUQJrI1Nckc1Iw91AEJLCuCHFftmD2FMN-9S0doeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
📊
فقط سه بازیکن توی ۱۰ فصل اخیر تونستن در ۵ لیگ معتبر اروپا هم بیش از ۲۰۰ گل بزنن و هم حداقل ۵۰ پاس گل ثبت کنن:
😀
محمد صلاح
🇫🇷
کیلیان امباپه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هری کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102458" target="_blank">📅 20:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102457">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOFCiqfIXAFbFh0G47pOliDRbLA_aI1ydI_wFnCCmUwUu8_lO-6dSZDxtV8ZvgkaGm8rRC5NcjdmiR1ei9IE3YaddmnyZU1mqJo9LKuk7xmfb03BFJSDvnlL5zAeDF7hZFroeCZaobItq9RfRWrTlndhJ-P1EgcNMawfUt8i4GrrqD90euC1YXq_WUsVQylqXyfn54salZ85g7OK6SrHROy4jHosMJFg28xstbC18MDDXW23lJajhc_E4I3LaPDpfGxIxCB8cc2-Vx6z1aW-1GzdorYq25NsQ56jq5RkYKlgMk7OAKnXoxZ_ZestAFZtR4zjbxpVJWOvgIHBWulGow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
دیوید گرافسون دبیرکل فیفا تصمیم گرفته که علیه اینفانتینو کودتا کند تا وی از سمتش برکنار شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102457" target="_blank">📅 20:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102456">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🔵
🟠
استقلال در نیمه‌اول مقابل فولاد با تک‌گل ابوالفضل رزاق‌پور شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102456" target="_blank">📅 20:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102455">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J54j5D5UGheCa2ySVfXoNQWsSlps6uEFRxbFFpnWnmeSZRRV_SnUCieOHL7NDCUS2mW_PyjwgodQ4xPVLeSCf8KntknvmCNJI15fwJSAP26WyxWoOt_Qs8xqDN7IMkgMHfyV97gUtEN-KAAFBx0q8fvh4DRajf1jOHrx02EW0ElSNOZEpS-1HO_spKXO1pwtcRNLRz9Uj8b4Xg5UC4tj1EHdm8CmJINLst0g35LcJg38-7sptGScktqqk1XJXIEWzvFWzjKNzwXr_OAd4qy1NAz5aq0iU0cVE7-HItruh0ARQ-Ms-fVqDtJjEZsK5nmlXIMVlqPUjlyLotN5oPYYMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟠
استقلال در نیمه‌اول مقابل فولاد با تک‌گل ابوالفضل رزاق‌پور شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102455" target="_blank">📅 19:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102454">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqVK2D03pqqGWZ2c4_ycJmEqZkjiYnEJMbawVTKLeNr5BuuqZR1-8NXtAE7HQcPxwpy-px_HtKGLyhPPUR2j9Eh-is_-VraGkTanrBZTY8m8cHBgT3YGFBIzYToW6Brk1VA1uZVyFF1NM7A-8Nu-kwF8HKYWydSPvMTv8GDLn1dFiq6ascHpsz9eALfhtoS_dv6SjwoyLly9s9NXQOfH9EQFOrAxDU8ptqcnzP2vN4Ldx6ThQ6EZCgCixK_u9hsJpF_m_wY9il6-7z9bt548tqgoPVItxdrAg2DK2IbuUBE3g-0lKxVjvyAcfewTfwY8RAxXayRSwcFSLbY3-8qpEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇯🇲
وینی و عشقش تو تعطیلات در جامائیکا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102454" target="_blank">📅 19:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102453">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
📹
🔵
🟠
پخش زنده بازی دوستانه استقلال و فولاد ساعت 17:30 از لینک زیر
👇
https://t.me/+E5pLb4kNVJZiOGI8</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102453" target="_blank">📅 19:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102452">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">کاسمیرو به همراه خونواده که دیروز به این شکل بعد از معارفه عکس دست‌جمعی گرفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102452" target="_blank">📅 19:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102451">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A72nYCc9qOR_GJlg0TO7RnXarQcPpIHQFdsozH5CLcYg50Xegir8CbSwCcHb8GNVZ3GAOsrNrwkuFGcpMXZmTml-pm5fIBM8jeY-NKYf24jGvR7sF0wxz6Bgwo6x1Usibjv3GtWR-vSh_tfhEkT8POzO4I8dMQXIBA3q5UFXRt2G_c4DoxWd8_-jNrax58RAf8ovXqMtyFo-h4U3lrGMyJspPlxtouoHFX8q2es9LzV_WRvJvebXFiEVP7Lwx2RfjnLPmgM1P99Lj_3L-K46KCqZZCakIA_C67m4Yg-xfk3kHCqTtTVnDclyEBD17A2mowhS9pobqtojjKmXQDLILA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇪🇸
رسانه ESPN برزیل: رئال‌مادرید هیچگونه افزایش مبلغی در پیشنهاد تمدید قرارداد به وینیسیوس ارائه نمی‌دهد و پیشنهاد فعلی همان آخرین پیشنهاد تمدید قرارداد است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102451" target="_blank">📅 19:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102450">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tggUg8x3jXMxuhVCVnHBLjW89AbD91DPEXxxdcn26yMahSqx3hQtklp-D4JGSAK2N9Pv9jSR7-9INGUMqR94Uu9YA2mPU9X1g7eMeiQK4Fh39Z-OtLSfV0al4FHHvWRhJjyBq2Pg3_Yxyoa_C0NSX1rdvJRoS-ZIpIqF8ft7g1PrH2tqSXLGgKwv1XyWu-O09x-5akg0jNGnAiJdcffRDtS8eVHScKxs32Sw7CbySy6BRRTVA2WA98Gb0g3XLNR1VjrGheRcYE16eEZbhAniuiAJuWagcpRsqBxi5RRozLUxekSemm5WQwVg__Ponek3137ZEi3Oo5GMEM3sHn8DNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🏆
اینفانتینو: جام‌جهانی ۲۰۳۰ بهترین دوره از تاریخ این مسابقات خواهد بود چون در کشور زیبای مراکش برگزار می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/102450" target="_blank">📅 19:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102449">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jq984OOIdN0TeAY3t8y_4kp_fJtenORdwzT2KBpZcxCqQcONkdzXdiB56MTPnNCMN2mq15fa7-yp8p7pqYKAXccV6mBntkr6UR6FRebw9ky-aI6R92aCBku8eXUBCSqhOhfDYkIoCzOFJdacYYPFxpVh0y9H1acM06N2R5SFjKvRS-eVVPUKZyAsJ5nuuU9x9DAbe_HoFP7L2YAOe8DNrpPvXjRCzNCxRP-O4mk9FgsXbhtlruF7hZepruIGDPOcy1VgxiAGsR3MhhhD0eRS6ogZDiC6KxK6yFzHnkH8-bzMO1SN1HYp4mLsYqRdI57_EdT4CWAsFPSLxJ1Yg-PPxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوفیس تعدادی از بازیکنای فوتبال
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102449" target="_blank">📅 19:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102448">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JF7mHXJMDPn6pj1D7bO2cn0sk-4PaCyj5ucabMUfiJontnf9KZE6gxVd8AdPYvAqcRzZjCHOMrSA4Th8gaLUeFxHjxWjb3ACvIh-oJPcop0iQnQdiDRy0OQczo9zli10oYewbVIsgORVkKGT24wjHUT5WeLU1dLI9XxurH-Nsr4JYJyCmI9weJcqCSL4gulEBCjot3GGuO17aScmNuoitIvgxPAAdEeiLhzVt66gF_ikBR9u0Rd_7VZ4jQEY4_vL0M-3ME7sVQVIUdt827aH_3sJohN9Iovsgzs9dBZo0Q-JJGXClpL82qAh83vYhvd4T2w_MnzjqHG1LT8DrLbXeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
اسپی:
انتقالم به مادرید خیلی یهویی اتفاق افتاد و همه چیز خیلی سریع انجام شد، رویایی بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102448" target="_blank">📅 19:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102444">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WRmqtRXhw3FWo5SJXdj3iz0oU3AIMrjt-MqizQ9L9P4DF2Xzn21l9X8fn0aA3SXMwFYoMphtFRpe3KMInQ8vJYlvq1JBZz6Odm589Mty1gAaUD357my-4xB3UO7ybb78DUH3m4vNd4d6_VFEkOo0CfIU-xsWsHE8PuClefZtrdIRyH_L3LhN_5BYMLu9xam4zLfLhi7odfGFJYc3AuU0K5BF66xao4zbJQrUS3hVC4L_FHNGmP_hSdlGO-kja6sHxoqMa0_yqIF83F8HMj1I1kqa9fkdKSFzdCwn8nev1BThVvkogkCWaWwqTSPV9o6GHWreNaRq9yyaZc7tR3E34w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kz_Nb75cUDe4R8F_Y2_Ac7oJJc--bwxhjgPyS_EuiVlOrJbqEnzt_gnJvxwANPjukOQV7EobBBw1l_L52Lr442pVgn0NW3uPFWUutxB1I87aFlzrglNIdEXedeDa9-WxAVwsLKXsUxAq376k73UxdDU43hIVo7EKebzI3ErILBoWlRCVrQ3mJc4qYx6de3qz3bab8_nO43K82d0fAisIBKX9u3UOEvmfUqDpScDMQiUDG7cYkqfdViwfD0RvFg_dNVRDRh0FQuPyXzyWb7xepfw19eulxhDUj0TzK-ST7Msya-0sa68XNgjyWjYZ0jxVu9-S6JFkqI3EhS7Q98sdfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZzbVM0bpaZ3epshDwHXyGH5u8tQlhPlo1CYi_IdEJClde5v5h_NNIOe7qWxpZLwmVSbjzHwxFnopZ1P2g5J_60bzAoMa1UwhFjQJpD-688Yvq90ib5KEMa0L1dFScnxevvYltGG-kI47s9ebph1t2JOiP7I82t8JwqHXuTniruqWOW96K-PVE6AcRPtGEp41VrhmrnfxnZwDjnR4SViibgx0oN9wWtGG_FfGFTl-RQdtcME9Fz5x5ddqXcFhCIJcK0bIfRa9jsh7aA9GzPbrKi6zdx2MJMJoS6PzeCCbaCEZ014WdcXDwElLO4iLmBwdNdSvgmInfuxo5P2L7Y-S5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y5XJjcRte4T84H8NRzsYIafSCfCz60dhxqLNMIhTr1TES3grBqIgr-t3Rg5XOHr0luuL9NGIiV0i9vJz3HkhyeOyZa3Lys-k8q4wOYJsckWo-BkmT_EBX_bhUlw1xszpCHaxk3h_AdFSvSRs1_4I7QMMayxANwPQmHBsZcV-TjnRBKUJ6NDYoJ-XRrDymaGyGwUEnk7tp7bRNC7i_xx-OAsZUOOFTbX8eFsQIVxffY6w9Ij-Qoth_ibLimk3W3M_-NbIInXz2GlnaJOy9m9uvmMHjP_eNzF_PiYd5eki9KfPVT1FCuUT9g2WsQ1lPiNDSiFYay7VndNFNwcx_hVw5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
عشق و حال لامین یامال با دوست دخترش اینس گارسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/102444" target="_blank">📅 19:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102443">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4mJw-sSkRFS8Me-W2wFP7ujpAHv0ko0c3vLjDjP_o_4yGtrDARtFc89R3q0rnXE9NcN0vDlIRQpTQQgHYqsO2OZ-Zik8TSjTt2-82bpV5Ny4LLbQhe4Q3-ezuwe0c1-Obh9e6YHqYh1PNRn4vDAiw7ZFFu4ye-fZHUUrDHCwKV3afN0RVaFD3NxqActq4KcjQe2CBpNkqTt-pdWUOfxFt_VFWpccNPqSH9wZa4CGCvz8s3XH-us1f2OUNLHrsgaoNMe4JxXVSQXkTr_w9EmdwXIG999wXEM81JCGZyoPhzjTD5rMWuSzB8s_lj1gYrUH5m5OAhOEen0krGTOmxyJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی دوستانه مقابل فولاد</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/102443" target="_blank">📅 19:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102442">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKJnRjv9F22KWSbDm7pLPy4MtCF1M402jBlf7aJ4ps-FLStxbAc4WyV59ewsH0J9HTyprkAMTTgrGn1DBoh6lphzWxNkGb2tp1R4RbMdHb4Olu5yqs4oZ4B2q8960xPp14NyKN57iHt_uEBzj5iZ8IuPv5IRJGX8cvkCPoBMsQPZAghe98JlfkgVYz-x3dHqq6agRWI8ePBhs-q8Mf-a2k_7uuIqsfqxsheKT5wS4mXqpw_FXB0qDoSdKmFUo9RL2WAINkvxhhEaJCrhyNgY4thE66PV3VBZw-hJXYdv8mQg-juv27hFT8h51sEZaQZLCypK5QYZVuEdXrHQbEp9vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فوووووری محرومیت دوپینگ میخائیلو مودریک لغو شد و او به زودی به اردوی چلسی در هنگ کنگ ملحق میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102442" target="_blank">📅 18:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102440">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bqgwujLTyBqnsa0fUYBlc_n2FYw8fGd4gD2KlimD5O6nZ51Q_XvLqyoxXM1moD1poJrNOwQoKNVV2CZ1PJH1eJ0NuqB1w_7poPZqUgSAGvFKMDusQaVK2eFm5-RF1e_etVymBjnuv-8q_YseBbN-OvK2VolqZ4-F9gK7pDAbrcioSfmH0yOd-GUwt-3bsqbJIEI5-brHm2rSIl25HoY07NlYGt2_j1BX8A1tnJ4q4hRTX7Q2M54Mlg4n7cI9EJ0TQfykRPPChIGM0m4Uz-SObXbNnO-D_boMODfssqATQDEWEMiTfJceipHD_cIk53lNNBjLJWbYsWm5IiFQJLpsbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BI0SY5fjimfQBUC8riXxAYUU-upMMF_-VG37rcyF-8eVZ6M0-kk-_c8Pv71k3xnaKj-JapCiF7JSPw0t4Fx0qHtPv0uwYcTxeQpYC1bq4M5IAPWvupjF0b3e8qg3_wZZlcb47Gk9CvfbcWkKMIA39egRleyoTAKX6Dvro1E-nnYvc02lfI8s3UeLGN0j0t8sds-wsQSaE_JAQBYlTaaRVN9CWGidX0zKotp_irj2cW7ZH3cztLIhwovkRMjPuAQlzjTFGUYNtOYTFrfo4nV_VqroPJ_EB961vtmCdh4lL7Bsk7ldgWVuSA3U1H6cmNxGldXaN0fbYuXdWdhKCPa9QQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیر شدیم و خودمون خبر نداریم..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102440" target="_blank">📅 18:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102439">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5d65b7222.mp4?token=NL_bosH61kRC2OliQOKGXbnz_xk0GVXwl9yJ9NrbBPlhsmBQmC-hItNhSEYs2tuEbzADxJ1uBF12f0Ou7qJ2yjglFsKD64XkqBRABV6jgaY88yh8F_myjzaj2deIC9SoHp_qqT6eMvXNHXViVA-4pEA4EPaP300M5ypiykZVAkgxAuCkADlmWFRy9sQadwi0hNPIrpGTDCywg1p5YPjl8rdw3WAgauf1u7dj7MpR-tvaw74Zf8MrDrW0plLXtAPEupRDGdCtN1NqBvpGsXT3kakoiywEUKRq-KXFhH6FSxEieuUZhPJqLm8mxfeeXxk7OvzrGn__xn3nVPMLX1wyPoxTHIq_7w1_jy4dVw42qWLhtnppkfjD72UTbrXRAOc01Dpaij189TD3WWS-pXaOoYoyxDsqkymFanvNPSFRCshViqFvtM02T9dCrtqUpg8CyFXGYKWwNB8_0nEFEicUP4wpnLlWPiR7cC5almaiPZZF2ajYSklkW3nurUStYTFZ4cMQ_c3IkTLzGbcU7yyTYQJjgjJduHhp_qBfIEplaVkRcyAXiVS1hOpMYmNozRdRRrQWHa3APKahY4aaOkpMefR1jWH3MlRJawt1QKBxdxdo8cDc_ucO4uKJIDDI-LStu-fM30iFumBFRKEcFARwo0RahitzZNKnJ6-Mg3TvryE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5d65b7222.mp4?token=NL_bosH61kRC2OliQOKGXbnz_xk0GVXwl9yJ9NrbBPlhsmBQmC-hItNhSEYs2tuEbzADxJ1uBF12f0Ou7qJ2yjglFsKD64XkqBRABV6jgaY88yh8F_myjzaj2deIC9SoHp_qqT6eMvXNHXViVA-4pEA4EPaP300M5ypiykZVAkgxAuCkADlmWFRy9sQadwi0hNPIrpGTDCywg1p5YPjl8rdw3WAgauf1u7dj7MpR-tvaw74Zf8MrDrW0plLXtAPEupRDGdCtN1NqBvpGsXT3kakoiywEUKRq-KXFhH6FSxEieuUZhPJqLm8mxfeeXxk7OvzrGn__xn3nVPMLX1wyPoxTHIq_7w1_jy4dVw42qWLhtnppkfjD72UTbrXRAOc01Dpaij189TD3WWS-pXaOoYoyxDsqkymFanvNPSFRCshViqFvtM02T9dCrtqUpg8CyFXGYKWwNB8_0nEFEicUP4wpnLlWPiR7cC5almaiPZZF2ajYSklkW3nurUStYTFZ4cMQ_c3IkTLzGbcU7yyTYQJjgjJduHhp_qBfIEplaVkRcyAXiVS1hOpMYmNozRdRRrQWHa3APKahY4aaOkpMefR1jWH3MlRJawt1QKBxdxdo8cDc_ucO4uKJIDDI-LStu-fM30iFumBFRKEcFARwo0RahitzZNKnJ6-Mg3TvryE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
چند تا از شوت های کارلوس رو ببینید، زمانی که فوتبال تا این حد راجب کسب و کار و پول نبود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102439" target="_blank">📅 18:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102438">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d5590fc67.mp4?token=TMku10MMu9u1SrluTejV7rvqV3OY7-sOI2RDkgUWdmubEMGo1UtNlE43uVpzsuJcqyzSk5F4ucq8FwJyx5Rv73MjqPYYPayTchJF0oRJDEnb7ymKbFbrIOkkjDomGG3eFiLvO6VxJeUQv3fCSACq97gkFEVwCiU61FgxgQI84hp2wIQc4-BdXjjXogEBgc3G-kPe0mnvIlPUAxSz9SpB1fEw2gAPqu-z2b7cFg9n5GHyDrNmnDpXIVZ5jNraVMmHsS6XBp8KPisRWWDOkcXADNiRpN0TEuokU1FKm1smfLUBJxMFCUt2GQ4Uc_-DkTPIU5MAReji5nJyo8aVxlTssg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d5590fc67.mp4?token=TMku10MMu9u1SrluTejV7rvqV3OY7-sOI2RDkgUWdmubEMGo1UtNlE43uVpzsuJcqyzSk5F4ucq8FwJyx5Rv73MjqPYYPayTchJF0oRJDEnb7ymKbFbrIOkkjDomGG3eFiLvO6VxJeUQv3fCSACq97gkFEVwCiU61FgxgQI84hp2wIQc4-BdXjjXogEBgc3G-kPe0mnvIlPUAxSz9SpB1fEw2gAPqu-z2b7cFg9n5GHyDrNmnDpXIVZ5jNraVMmHsS6XBp8KPisRWWDOkcXADNiRpN0TEuokU1FKm1smfLUBJxMFCUt2GQ4Uc_-DkTPIU5MAReji5nJyo8aVxlTssg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ویدیویی‌از وینیسیوس‌جونیور در سن ۱۶ سالگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102438" target="_blank">📅 18:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102436">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N0A209k5pXZDiCK_M6BPLr2E7kAb2KBYfZZLp85BtCk4PxDSEBtCwBdFRrQzytvDQCIGTj9JBk3OuJ8k30VzfxeyosFt-kTVOREkGL_a3Bw6oT5xAh1ZNjkzDPHE1aERc8dNgmSrfN4jqFT_5nxpJ4JhFVeHOchIfA0O8bpU-5Yj0sCTW4wuQoo7Tcx-FP34nfo9RfLr55eHprYz9q9m1PiLhbOSlHZmV8CsAME9q9hVUcSgprbVHmfboV3pule_vG7CX-duhHfGK7oKCY1lAhxSqTNFzTv9x5bEfpDyApthOGWCac0R9nZexb8vxhy_5X0ZMGcOzgJMvXPL1ingmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P2DhUDEbzJaQxnMIgtGYTfUXZZVWZVH9udPDBzRCWTH4brC80UROpxROY0YYTUjmliG0Y0wycUOlwj7lx3P2bg43Nl0IQRTOdspGtAWGrKXBnjNSZFSKR48BU-fXm7vXf3ZIZhJPWAyOnnaRfJAfuepV4eTJzjSsDfpPFbHJnSalO3Hw1oknmuw8Cf4hcm6wsGP4vIS4urtk4s1nFvBklaLUd3jt5TUgZ4VSof4ywMmpmWWONHJBF2V00I-nOe2zDdk6u9Mk-cZXtny2eQuGbUV3KSRMYbD3aUXLYQtI7Le8ICdm45vrzRA17GYMgsIWccLjXHZTc4pa2g2Miywv-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔵
فوری، محرومیت سنگین چلسی:
🗣
باشگاه چلسی به مبلغ 10 میلیون پوند جریمه شد.
🗣
همچنین، به طور تعلیقی از ثبت بازیکن جدید در دو دوره نقل و انتقال محروم خواهد شد. به این معنی که اگر بار دیگر خطایی انجام دهد این بار پنجره قطعی بسته خواهد شد.
🗣
در ابتدا 6 امتیاز از مجموع امتیازات چلسی در فصل آینده کسر شد، اما باشگاه درخواست تجدیدنظر داد و این رأی باطل شد.
🗣
این رای بخاطر تخلفات نقل و انتقالاتی در دوره آبراموویچ مالک قبلی باشگاه صادر شده است. مالکان جدید این باشگاه خود این تخلفات را گزارش دادند که باعث تخفیف در حکم نهایی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102436" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102435">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68f9e38a71.mp4?token=JbBlOe56VZrWdjuQDbg7y4Y8ucT95k_yA2wR1fQAELI594XyQr0DSBPgq9Ih0IhgaR54qj2siwc8s1jPXfCZjySX2i09axLf02iefJkzjI1ad1D4DsLriXIVrCpmmXg-AubLju-dXVI5Anroz6phh6IfQoBhXIp5Tvawb4ccz8UJ_ptFq-CkkhmEW0rtPSm_klWv5Ak_rpWjWafG4OmzsmIJxrUlCyh5NVyoQ-ikqCIr0k8cKXzT27DCyxTWVlPlYQfiGVHGZ7-vy4J72BikAyTKNGAEr-SWc8SCqYMVXEGbwxuF8I_4tEx6XoxLXv-X4mjqHi4zt5elDHXyDZmv0YU8gIHGMXSDRzcB6g0clia-8hGlmIMlFv8kkbhSRfBiT3VJLlzLD8hU4f78LgUYwh2q9zRj1f1lXgnWRcW1qqyHwXnMcmOA0U_FG3i_sGaiH8C62A7TCYWM9pTCSxO_EvCZrIPDKMB7q2JgIFLijXYkeXOxIJJU8S4cmc3thJFIX11ZD_M1SNXmdG83DjnX63bAtplxRbE2fN5ZJErY3bUWAehTiXRxR7BEVH-d1TdjBm3oNjs6STjwwDjdkkUOMkJfMmm75BnBaF6Gx7-TG7Go5GrTktomjJj2AI8vdu5sF_6quD7JCfbKjncMNNPq76UQ06YFFJftCyUMC8zojdI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68f9e38a71.mp4?token=JbBlOe56VZrWdjuQDbg7y4Y8ucT95k_yA2wR1fQAELI594XyQr0DSBPgq9Ih0IhgaR54qj2siwc8s1jPXfCZjySX2i09axLf02iefJkzjI1ad1D4DsLriXIVrCpmmXg-AubLju-dXVI5Anroz6phh6IfQoBhXIp5Tvawb4ccz8UJ_ptFq-CkkhmEW0rtPSm_klWv5Ak_rpWjWafG4OmzsmIJxrUlCyh5NVyoQ-ikqCIr0k8cKXzT27DCyxTWVlPlYQfiGVHGZ7-vy4J72BikAyTKNGAEr-SWc8SCqYMVXEGbwxuF8I_4tEx6XoxLXv-X4mjqHi4zt5elDHXyDZmv0YU8gIHGMXSDRzcB6g0clia-8hGlmIMlFv8kkbhSRfBiT3VJLlzLD8hU4f78LgUYwh2q9zRj1f1lXgnWRcW1qqyHwXnMcmOA0U_FG3i_sGaiH8C62A7TCYWM9pTCSxO_EvCZrIPDKMB7q2JgIFLijXYkeXOxIJJU8S4cmc3thJFIX11ZD_M1SNXmdG83DjnX63bAtplxRbE2fN5ZJErY3bUWAehTiXRxR7BEVH-d1TdjBm3oNjs6STjwwDjdkkUOMkJfMmm75BnBaF6Gx7-TG7Go5GrTktomjJj2AI8vdu5sF_6quD7JCfbKjncMNNPq76UQ06YFFJftCyUMC8zojdI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
درگیری کورتیس‌جونز، سیمیکاس و سوبوسلای بر سر بازوبند کاپیتانی لیورپول در بازی دوستانه اخیر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102435" target="_blank">📅 17:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102433">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hN1Fho1bSJyAo8xlUADVnsAoTUcCzDHl_-_yawGrbqEEYk6CwENmTYN9VJSszOkBJ10QhYKPeUGbmEIYm4qI-_udwVUgdr0-GMvXS0sxCbstiHz8raHjDLYw3lYUw4vUDJ7cSqftRMEHwPpmVQbNG010-NMQCLz78KEtjPQC8tzAsrDgjmatI5toDUD1mGyvmJjGSNFaaUinKLv85cMmTGCTVf4Msz7sJPREqB6El1-bXdLrFWWfyRD2OgWhSjM0WYHyMMvSxZK9rIhllfq5xjmsLubcHwH3pcUfOwOkwoc9oecUV4AHCFmPEaAYhj_5CZ_BMUY8cJEQlGlBfFfLHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LeUvXR58uywhPZ7Id9t6lSs-d_EseFCycR1XPBgnysDXkqhm41X3AxShoTwxeveX0lVnscfN6p1shRD7LjCjixL-iL9CSzPNqu5mo1sdqmBr9Zc-fskYIWZ_dqdST4FgODVwYtAp4cmJRDxMbz65OiEH53QDMfArHfas7il5Wj-YExurE76TYS359luLgimbzZhvE07CIaGXBy3T5M3WlCeVtTSEN9Qe7uMdft_kJRmwPF2kRvGpLZT9dDhW0kQ-f3_nX7r6DQbv1RRDO8b3x7wDCNotf72asaSc0ukq8rEBXQtzq6ibcXCe1DlBsyg6NZFHHko29kR8o6gYqLj02Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
ال اسپانیول:
پرتغال و اسپانیا اعلام کردن اگه اینفانتینو پیشنهاد خصوصی سازی جام جهانی رو پس نگیره از میزبانی جام جهانی 2030 کناره گیری خواهند کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102433" target="_blank">📅 17:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102432">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96363baca3.mp4?token=vMsU_AOlraaiMkZ4rMvrSeojLw206PdaQ0eVT1_1_peBX46tUz2HRkz1pa0G1YZV1nenD_DU-G7rpeyhEM7mc26MLzaaOmo5nG15pPir-x2wGQQ53_wBO7cwXcsXcTZw1quh454PaJiB5tKIkLXqmQpxPcA4xY7XysMK9eJ6l5tyNI4kVv5er-iZIlpcjzrmYtffM0_005G8nQj3p_0ckyM2YDqsE9tQglufnWRdL4ODIlDGMJn5CBf4EkIRYMmkKEJKyTdw9qA0Re-CYW2VL3DDS9JgDRPx_QTp5LyAmPJl0Ov_hvt3soiKLtwiXCCXBWKdmv6t3HyN6dt4hpOZiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96363baca3.mp4?token=vMsU_AOlraaiMkZ4rMvrSeojLw206PdaQ0eVT1_1_peBX46tUz2HRkz1pa0G1YZV1nenD_DU-G7rpeyhEM7mc26MLzaaOmo5nG15pPir-x2wGQQ53_wBO7cwXcsXcTZw1quh454PaJiB5tKIkLXqmQpxPcA4xY7XysMK9eJ6l5tyNI4kVv5er-iZIlpcjzrmYtffM0_005G8nQj3p_0ckyM2YDqsE9tQglufnWRdL4ODIlDGMJn5CBf4EkIRYMmkKEJKyTdw9qA0Re-CYW2VL3DDS9JgDRPx_QTp5LyAmPJl0Ov_hvt3soiKLtwiXCCXBWKdmv6t3HyN6dt4hpOZiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
مرزها برای میزبانی از زائران اربعین آماده‌تر از همیشه
🔹
در آستانه اربعین حسینی، پروژه‌های عمرانی و زیرساختی در پایانه‌های مرزی کشور با هدف تسهیل تردد زائران اجرا شده است.
🔹
در مهران ظرفیت خدمات و زیرساخت‌های برق، آب و روشنایی تقویت شده، در شلمچه بازسازی و نوسازی بخش‌های مختلف پایانه انجام گرفته، چذابه با توسعه امکانات رفاهی تجهیز شده، باشماق به سامانه‌های هوشمند مدیریت تردد مجهز شده، تمرچین توسعه زیرساخت‌های خدماتی و ساماندهی محوطه را پشت سر گذاشته و در خسروی نیز سالن‌های مسافری، پارکینگ‌ها و فضاهای خدمت‌رسانی توسعه یافته‌اند.
🔹
همه این اقدامات با یک هدف انجام شده است؛ سفری ایمن‌تر، روان‌تر و آرام‌تر برای زائران اربعین
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/102432" target="_blank">📅 17:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102431">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">💥
🧐
رونالدو، پسرش و جورجینا درحال عشق و حال در گرمای تابستونی اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102431" target="_blank">📅 17:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102430">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e703311f9.mp4?token=NomUq26ADoshROQSHh08Pd2s9bJEmh25SSpSQHS0yWTtOZARAMMotftI_JlWngLVJALkL3-cr9LT1NcHv8HKhJ36ZH4ZcfFY0NwjyzktQgm0f2mC7UJT0Z9vwRGAxCvz7V_gtCSCt105eenkOELX348T7y-bzXwJAfjI-UXZIW8326bSEqVaQ8Oye0LHhT8z0VCXxdmKXmdARdPSTfPq8AUQsDB3jY1ZT6UTm6grKmPodukE7vh5zPssSEMit0D40Uy-5qnGwXskQaUyYT8JulK7B3oPV1zd6BnTpGkeAJ2pg62MdovD86B55ZQc2cpk7AtjKpi6wuwqenqidLu8Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e703311f9.mp4?token=NomUq26ADoshROQSHh08Pd2s9bJEmh25SSpSQHS0yWTtOZARAMMotftI_JlWngLVJALkL3-cr9LT1NcHv8HKhJ36ZH4ZcfFY0NwjyzktQgm0f2mC7UJT0Z9vwRGAxCvz7V_gtCSCt105eenkOELX348T7y-bzXwJAfjI-UXZIW8326bSEqVaQ8Oye0LHhT8z0VCXxdmKXmdARdPSTfPq8AUQsDB3jY1ZT6UTm6grKmPodukE7vh5zPssSEMit0D40Uy-5qnGwXskQaUyYT8JulK7B3oPV1zd6BnTpGkeAJ2pg62MdovD86B55ZQc2cpk7AtjKpi6wuwqenqidLu8Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
🎙
تمجید جالب کاسمیرو از لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/102430" target="_blank">📅 17:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102429">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b472a6619e.mp4?token=ocC96I5aY8gsnqiUO0KQCJ0USWqrMvIgZcpN0X9k_Bp01LVentvUIPlYPRipX6FakF_DadaNwyKgfAeaSCF3MrwDdiE9rkYcXJpKqeylmBNDvHs9YhKLN6vxSPJNC9a9bpZxczJxG1IAng5TST2xUESJu6_F0x4m8fCvfhGyjojnfzaEeuqCY9iq_ts7xkFzKbSiGYx_7gSTLGEKLwnsnjjYpmqIPEmxp_2w4vklmMmUgFzxTnxhnGhOVlEl0e6QaMWwPE9FcHacNbco8i0Ix71XZ2RA733sqBtWTDwMF1MKwhSfSSQEVgapNzICU47xd1dg0eF2E98mYVJkIRL6bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b472a6619e.mp4?token=ocC96I5aY8gsnqiUO0KQCJ0USWqrMvIgZcpN0X9k_Bp01LVentvUIPlYPRipX6FakF_DadaNwyKgfAeaSCF3MrwDdiE9rkYcXJpKqeylmBNDvHs9YhKLN6vxSPJNC9a9bpZxczJxG1IAng5TST2xUESJu6_F0x4m8fCvfhGyjojnfzaEeuqCY9iq_ts7xkFzKbSiGYx_7gSTLGEKLwnsnjjYpmqIPEmxp_2w4vklmMmUgFzxTnxhnGhOVlEl0e6QaMWwPE9FcHacNbco8i0Ix71XZ2RA733sqBtWTDwMF1MKwhSfSSQEVgapNzICU47xd1dg0eF2E98mYVJkIRL6bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
یادی‌کنیم از بازی تاریخی ایران و قطر با گزارش جذاب عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/102429" target="_blank">📅 16:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102428">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfd29d0ef7.mp4?token=d6WFclSKqy1JVBvdBvWoL9cpzYkGivkDDjXc7y3uQpm70guObhJbr1L9k3TQje4zsaSJ5zOszvmj-1QkZAcm0e61a6qRFbwsOBFGuP1ATojJO3UEEwWBfcLY1hdHoTrjOP3f1qTSNR-fPXRnvyaqNqvWkAZ7HOg6lv0pUWuyk1rc8YHMtsCFwxvvvmui3aCQd-y9ETR4smMxeJfiz382aEcspKJ_HrG0dob28UQ8jMo6aMlFzS3BLyil61NFMcDnl-Hlgp0bRNUYcCJthN2Oi2mzU1fLyhYnVgrbLcWQDbh0QxPRJUgM89IXmhg3LO2yjuqXxADxKNMYZDYNV0YuAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfd29d0ef7.mp4?token=d6WFclSKqy1JVBvdBvWoL9cpzYkGivkDDjXc7y3uQpm70guObhJbr1L9k3TQje4zsaSJ5zOszvmj-1QkZAcm0e61a6qRFbwsOBFGuP1ATojJO3UEEwWBfcLY1hdHoTrjOP3f1qTSNR-fPXRnvyaqNqvWkAZ7HOg6lv0pUWuyk1rc8YHMtsCFwxvvvmui3aCQd-y9ETR4smMxeJfiz382aEcspKJ_HrG0dob28UQ8jMo6aMlFzS3BLyil61NFMcDnl-Hlgp0bRNUYcCJthN2Oi2mzU1fLyhYnVgrbLcWQDbh0QxPRJUgM89IXmhg3LO2yjuqXxADxKNMYZDYNV0YuAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیاز بود یه آیتم جدا برا لحظات تاریخی فیروز خان کریمی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102428" target="_blank">📅 16:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102427">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d17c8ef3f2.mp4?token=g1ANX80bFjLD6qTsXEAD6OY-upxth2W7GxrangKiiQZ6-0UrlUUAQIKoW7RO0OFJZflalrSoJ3uNgPhQiTpZT0L0WflBMir9oe4sB2iLapBjALFVlSVlbbzEPpT8u_k8sw5NMreusocrer8cFBXpp0_CEdzumbWtXcEqeTJr-3Zvt4zcOV348zFfQVcVSnBshk5bbhk3czd48fTqPc6da44cjxSE8mlpxjfJGHsybpnLVYcNtYuvlUBzr753i43Bfr_wHKeszmayQIPjTgO85JjzRFiz8wmxRnP8ZSYfC4Tewo85BQ2cDZVnM5WlpBStcjfbpsFxiTt11APWqSyEMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d17c8ef3f2.mp4?token=g1ANX80bFjLD6qTsXEAD6OY-upxth2W7GxrangKiiQZ6-0UrlUUAQIKoW7RO0OFJZflalrSoJ3uNgPhQiTpZT0L0WflBMir9oe4sB2iLapBjALFVlSVlbbzEPpT8u_k8sw5NMreusocrer8cFBXpp0_CEdzumbWtXcEqeTJr-3Zvt4zcOV348zFfQVcVSnBshk5bbhk3czd48fTqPc6da44cjxSE8mlpxjfJGHsybpnLVYcNtYuvlUBzr753i43Bfr_wHKeszmayQIPjTgO85JjzRFiz8wmxRnP8ZSYfC4Tewo85BQ2cDZVnM5WlpBStcjfbpsFxiTt11APWqSyEMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
▶️
رکورد پرش سه گام جاناتان ادواردز (۱۹۹۵) با ۱۸.۲۹ متر ثبت شد و ۳۰ سال پابرجاست. این دستاورد استثنایی در دو و میدانی تحسین شده است. ادواردز در مصاحبه اخیر بر تکنیک منحصر به فرد و هماهنگی قدرت و تکنیک تأکید کرد. او پیشرفت رشته را با شکستن رکورد توسط نسل جدید ورزشکاران مفید می‌داند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102427" target="_blank">📅 16:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102426">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/543e2ce52d.mp4?token=paayGEfUCrFqFpLJB1JH_evdJQjuRsO19z-GQr4Wks5-RbZAxVxr0BLG4ePesQHoK664zrtk0gSGwJs0TnjYqCF-P5vnvHg26_18SU6Je1KI8rkL0avib_k8srhjZYJea8sOypxlP0bTraRHbPDZm998J-A_70wxln1yuE7ehyAU9oISUf4dyQy-SVCxcv5NoV56Slb4mOIB7dcdF1PxlwqIAgW75yi_ULg5qY5ifyIH6OPtdjv70AjC74fQqlBmTLbn6Ueu86ZFUx11EZuZE-M_ZoKqMU7Ukcofy6QgfT1YEVFENmzsO6V7ju-y2q8JRDTmUx7gNbPsCj0lolWyMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/543e2ce52d.mp4?token=paayGEfUCrFqFpLJB1JH_evdJQjuRsO19z-GQr4Wks5-RbZAxVxr0BLG4ePesQHoK664zrtk0gSGwJs0TnjYqCF-P5vnvHg26_18SU6Je1KI8rkL0avib_k8srhjZYJea8sOypxlP0bTraRHbPDZm998J-A_70wxln1yuE7ehyAU9oISUf4dyQy-SVCxcv5NoV56Slb4mOIB7dcdF1PxlwqIAgW75yi_ULg5qY5ifyIH6OPtdjv70AjC74fQqlBmTLbn6Ueu86ZFUx11EZuZE-M_ZoKqMU7Ukcofy6QgfT1YEVFENmzsO6V7ju-y2q8JRDTmUx7gNbPsCj0lolWyMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو کمتر دیده شده از مارادونا و فن‌پرسی
💘
💘
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102426" target="_blank">📅 15:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102425">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e43f315425.mp4?token=P1wiS08FP0ObnoSPH1B23JJmkXthyTOP89M8wDpWRgDyJSjckiDgTfa8Zd0RV12a8K8Uy1Vpo1_gwaxys0AOkCDi8URif3JGEpteLzLMxT_d9A0YtqGHsczM0Q4WTuFfQAVnTGJQjCPHLLunNFLbGQkb0uoLpPkwbB2AOQLtwkq3YEB91eDFRWZ8lyNtLBgBLvprwpMcwAnt_96gcTtuQ27eGXEB7FQf4Hf2ULhe6s_sxgEdbKIixY1nL76jlZzKtaTJ8pI2Myvriz3tvOi_4G7FqwO2MGMQUgtRfmN_7J39taZHMTfm74_XYcsQJBRQwwmo9KXGVBY5srTqfkGbmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e43f315425.mp4?token=P1wiS08FP0ObnoSPH1B23JJmkXthyTOP89M8wDpWRgDyJSjckiDgTfa8Zd0RV12a8K8Uy1Vpo1_gwaxys0AOkCDi8URif3JGEpteLzLMxT_d9A0YtqGHsczM0Q4WTuFfQAVnTGJQjCPHLLunNFLbGQkb0uoLpPkwbB2AOQLtwkq3YEB91eDFRWZ8lyNtLBgBLvprwpMcwAnt_96gcTtuQ27eGXEB7FQf4Hf2ULhe6s_sxgEdbKIixY1nL76jlZzKtaTJ8pI2Myvriz3tvOi_4G7FqwO2MGMQUgtRfmN_7J39taZHMTfm74_XYcsQJBRQwwmo9KXGVBY5srTqfkGbmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
⚠️
تجسمی از المپیک اگر تهران برگذار میشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102425" target="_blank">📅 15:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102424">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea1f4ae5ef.mp4?token=r1IHsPWJFEHraRIBXHOeZhfrpP3wiQOX_Cv8XuzwdO7QAvvAy1jjGBJ7B_-_ttxXlAxSBKz_8j_EL2g7XwctrGNLLfU3xfse6Yyg7NgEPwVPFMFQy1T5wfq9XqT-VA815_QCVlFkstJizasppXNM7D0HmTQ9toWXY0rG6xAd5zRfBmsA3BQwqrZCWKqky8zBvcxRY0YWjRHueNhAckrf3Yq48j68kR9SLD_b5pE0Wjt-QQCeoXLiyzJ69ff9EOsybSDjsTOVZOR_V5V89hfJzEwKXEnAjSw_Y7fTnCVGY3spVq2EIaRo1yH0BUrjSVwjFVv-mDXfhI6-GCOQKpSCGjXXlXxhViYSUxi2UdZO3oG1NIKHR_bHM1P_ibNROKQcaWpz8Gn-zMAbYSisF0eYLuhHrBZvR0AM8sMa6veCRoq9zg4BTuwwY1YvwKTvJQVLMIS7fEm4a4Usas58fnSB-QrDiV-ZlzDgGcL_eii_pra5lxHLpL2ySTB3JKSzO4_9OyyM0c1If_1JKOtsdcL9XuZf9VMUQMajy3sd-vOrzIY72b8_hbk62BquwdSbl45jklrZEtHl5NwQi6QbcCsRDys0ZZwb5347uYSoesLMCPvP8xaqOwX5-FaiP65qL3m7Y0l93LNZ_RwyVdXw64P2kFxlwxZxst6toaVd5emmKT8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea1f4ae5ef.mp4?token=r1IHsPWJFEHraRIBXHOeZhfrpP3wiQOX_Cv8XuzwdO7QAvvAy1jjGBJ7B_-_ttxXlAxSBKz_8j_EL2g7XwctrGNLLfU3xfse6Yyg7NgEPwVPFMFQy1T5wfq9XqT-VA815_QCVlFkstJizasppXNM7D0HmTQ9toWXY0rG6xAd5zRfBmsA3BQwqrZCWKqky8zBvcxRY0YWjRHueNhAckrf3Yq48j68kR9SLD_b5pE0Wjt-QQCeoXLiyzJ69ff9EOsybSDjsTOVZOR_V5V89hfJzEwKXEnAjSw_Y7fTnCVGY3spVq2EIaRo1yH0BUrjSVwjFVv-mDXfhI6-GCOQKpSCGjXXlXxhViYSUxi2UdZO3oG1NIKHR_bHM1P_ibNROKQcaWpz8Gn-zMAbYSisF0eYLuhHrBZvR0AM8sMa6veCRoq9zg4BTuwwY1YvwKTvJQVLMIS7fEm4a4Usas58fnSB-QrDiV-ZlzDgGcL_eii_pra5lxHLpL2ySTB3JKSzO4_9OyyM0c1If_1JKOtsdcL9XuZf9VMUQMajy3sd-vOrzIY72b8_hbk62BquwdSbl45jklrZEtHl5NwQi6QbcCsRDys0ZZwb5347uYSoesLMCPvP8xaqOwX5-FaiP65qL3m7Y0l93LNZ_RwyVdXw64P2kFxlwxZxst6toaVd5emmKT8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🔥
👀
۵ گل زیبا و برتر اولیویر ژیرو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102424" target="_blank">📅 15:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102423">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a3bfea056.mp4?token=ZypYvgHol9BG0O-R0mvVAcjxpGl61bo1l7kpCTFAPxI5lE-_uluy6RebK4-nfagyNQ0oAC0QlIJxQr8POAWVcvLf8ZUG2PkKBtmXFEIdY2L37muR8ZOgpU-_1NTHeIMy6SGRAAmICJvfQrbpAEVjHurQ3W2l-QBLuZkCx1ZeMqIVWJA1QzrbKik1FpAqL_TciBI8Z0RVgv-a9omwwXCdqm9hk5AelaXF6Fv8t81BRlOLnjShTEK4pysXU0C9VRQetCkZ7QYYsML0eHIIp43S-PlMuVIuIfeJaNu9thQbVVqgRY_rsFrVGRjwgCHO6CZRMb4mUlhcRnDCLO2L24tkOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a3bfea056.mp4?token=ZypYvgHol9BG0O-R0mvVAcjxpGl61bo1l7kpCTFAPxI5lE-_uluy6RebK4-nfagyNQ0oAC0QlIJxQr8POAWVcvLf8ZUG2PkKBtmXFEIdY2L37muR8ZOgpU-_1NTHeIMy6SGRAAmICJvfQrbpAEVjHurQ3W2l-QBLuZkCx1ZeMqIVWJA1QzrbKik1FpAqL_TciBI8Z0RVgv-a9omwwXCdqm9hk5AelaXF6Fv8t81BRlOLnjShTEK4pysXU0C9VRQetCkZ7QYYsML0eHIIp43S-PlMuVIuIfeJaNu9thQbVVqgRY_rsFrVGRjwgCHO6CZRMb4mUlhcRnDCLO2L24tkOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
سه دقیقه با لیونل مسی ورژن 2014/15
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102423" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102422">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqJw03-bflXY21XnmFMQoK_hxarEbX_04_Js8LPhjcdhowqp-3EWiB2T8_d2Qhjfeb9AXnxwIyfLyAG2pMnS5uuvFBQIRqX3uVyhIcp7Gz8MclZGZdsuHNCQwLYGU0d4L59F5Um76rPVJz5uv_K6AVrCrkGlo2XVXja4g3GO6OA-gcvFJNgDke39SUDap8DFMtlrKxRQl83haa5aEt5O3aLQD4s5HW5xXWcot_aK-lzizExVJM5Lu3a3mGAj1Ep5R5yk9MrIuydFeVb6lYp-JBXMss-Y_hlO67hXduFFgu8vfP3fTiLqYTHXvXjKcdq4rJLHj2YYQMcvn5igxQ2xyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
لیست رئال‌مادرید برای بازی با فیورنتینا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102422" target="_blank">📅 14:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102421">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMiLJfwEpxvTb1xkKmuXwY--FTKL2Ne8wfSEuxSSisIDAEbOdKUKBqby-Vg0WpdlN4AjWtALc0l5EvevBse3Y-RgNH5bBMuCkiwQIam3CxYBGOXoLFUKTWoqNAgY7E9BvtLjVAFFvvXXagr-MZqR_nsjCHux-XHqiyv_x5tQsCGnQNAUrlrQ_iuV6zMnGqtEkrfSrh2ZvXGgnenfKDeyRRyv1s5zyKotfEuwQxz0vhDDgTEty8rK0k2NNJ3yP3qFnXeFc7JNXQQUmxbmNGLEESUFEdTeJVW2tFoe-oQgWbeCrysSa-G5vUlgfb5ECJWOlOsxKKM-HMefDPf6v-Dfaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
#فوووووری
از نشریه اکیپ فرانسه: آرسنال با نیوکاسل بر سر انتقال برونو گیمارش به مبلغ ۹۰ میلیون یورو به توافق‌نهایی دست یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102421" target="_blank">📅 14:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102420">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/529b07ca6f.mp4?token=QRLPkadPFgGOugfjkXega204omSH7SUX1E_M7SsuWWkvICITWXI8gOUwYF6xrXOQi1q0XQvExbpZ7Zze5WPzhMEo5ys0eDDVacp5iRY13YDv58bz1nPQAa35ot-3gRgBKG5iWMxKDBfz-ISKVb29rDjOvVeuuDOksVtczEdAU208iF-Vf28wtKKEAbx0RusOCqq0J5MEDsc0eiPKoLUbql4Pow_rSoH4qp9eTZw53c-EoIPlHWLunrdiZkup3TfeApj3EYTwJ7zVfXw40sFumWLcg7souy_IECZql_TdRLywQu4yCsrdwqB340iT_u8bvElIZiU8tP1xQ82j4ofB-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/529b07ca6f.mp4?token=QRLPkadPFgGOugfjkXega204omSH7SUX1E_M7SsuWWkvICITWXI8gOUwYF6xrXOQi1q0XQvExbpZ7Zze5WPzhMEo5ys0eDDVacp5iRY13YDv58bz1nPQAa35ot-3gRgBKG5iWMxKDBfz-ISKVb29rDjOvVeuuDOksVtczEdAU208iF-Vf28wtKKEAbx0RusOCqq0J5MEDsc0eiPKoLUbql4Pow_rSoH4qp9eTZw53c-EoIPlHWLunrdiZkup3TfeApj3EYTwJ7zVfXw40sFumWLcg7souy_IECZql_TdRLywQu4yCsrdwqB340iT_u8bvElIZiU8tP1xQ82j4ofB-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
✅
یوسفی: زمین و تماشاگر که ندارید، لیگ را پلی استیشنی برگزار کنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102420" target="_blank">📅 14:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102419">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9889076a09.mp4?token=jxe8iA9kZ44TI3w6pkrksdvp538MH_xXK8jQXHeJrv7nRoody_Sx6wWj3NrvD_iUVgdTWDm9Xdm5vpQjGT0UV_UD0NnbiFmO4ivKCk-ACR5pxXzk01kFoKzuGQZSsVJduTzSxPb8mTmT07fB0S2PWzS4MI453BP3TxMFRHc3ubAZy-o82KflkAkI_WwZ7xevCE4noTZwmdRIH30ni496kaJUKKpi8CclOGPD2DOJ5dZLRNNbSxeGj9_ZByaOn9FwgyyRTtsfAE9uiT-uF9mVEtSiLhycT-ODHRpJKXaL0KQDSZvWzMw4_sN80bZhIjsrGULHL8_9koVi-6NoUglPDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9889076a09.mp4?token=jxe8iA9kZ44TI3w6pkrksdvp538MH_xXK8jQXHeJrv7nRoody_Sx6wWj3NrvD_iUVgdTWDm9Xdm5vpQjGT0UV_UD0NnbiFmO4ivKCk-ACR5pxXzk01kFoKzuGQZSsVJduTzSxPb8mTmT07fB0S2PWzS4MI453BP3TxMFRHc3ubAZy-o82KflkAkI_WwZ7xevCE4noTZwmdRIH30ni496kaJUKKpi8CclOGPD2DOJ5dZLRNNbSxeGj9_ZByaOn9FwgyyRTtsfAE9uiT-uF9mVEtSiLhycT-ODHRpJKXaL0KQDSZvWzMw4_sN80bZhIjsrGULHL8_9koVi-6NoUglPDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
💥
روزی که پیتر چک آماده ترین گلر آن دوران فوتبال میخکوب شد و این اثر هنری شاعر رو تماشا کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102419" target="_blank">📅 13:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102418">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DaOVQ0x7BjBdIYnMCj2T_trY8BXWuRLDDTQyTWWx1eid0EkZSQirz8XqI2szgFCV-zlU0ozDPRZPiSwiShcie3gRddQtgsI26k-Rtu7M0hLEEEJNauVuyh4Io5xnr2T2k_9Eys8viDcuDT6AxNcOTq9PJmtCt4U_soBYg-qY1WZndug8n_pULwuqE3xD_JYJ4wEUHX6LhoPitoUt28Nd9oVja4R0AzSVjwCTm70qIJQjbm2aVb3g9DMvd_gX0bxBL9Q2riWeWe9h8qbzFFkoj9Y696WoW5WpXRKc9F-RhrIK8FulL144xd2G81kcMtPoxUDIvBI9n34JBHNQBOHGMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
کارلوس اسپی تو تمرینات رئال مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102418" target="_blank">📅 13:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102417">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZec6yzFIECgPjvTKFRqVAVWTO9yWP_-hVDDvXlHXYqAi2KCdYXZwsUpfz8ew6N27q1u2hm6kYZgrPNgJy2s1UZnr-kTwNgWYtXHHt-fZRV1cXKNaSKbfmHOiSjiD8Po9dL-8pF_qfItxHwo3kewP3fw2zaX16I0WeqKksIgLxFjGao-o127xXId4EMeIovJ6voeEjpWa1FvCjbgCDMa6MNHdCcO8ZvlOdotQbQjRNJoQ47sO5CP4pca73kxBLn5n_fq0yINlIRTF_QnUp3MQTc-MW4lsyWquS5HwW3F3CFi9bv70ta8pM_x8Ws34TzTeoWv_lyRjztAJs-P3ZvnHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
روزنامه اسپورت: دو باشگاه آرسنال و تاتنهام به رقابت برای جذب فران‌تورس پیوستند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102417" target="_blank">📅 13:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102416">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4938ae1d8.mp4?token=WLwIYy-zy9IoVyW-xHioseEDWTEHI0FKug8qrr1IkgRYOLCNRr8tCCp4ZyF3Y0dB-5QrXI5RBTOG91fC7wyw9ixJpj-eYMYqcEYrlPjQv9E7CurU6XWi4yrh5wcW8YeyVjli35G8jnSbpLxbWM-ggrHQzl18u4P6XD4Omfgtp3vn0SLV0JcmbrspnEF1OQrbIsjg4ZcLogyU4yYi9qxa0nJvQ5ZrlPMM7mW4Zw7YPUJFZ3ZEb4-pW88sgJTEMK_NYKNji6YuNtxQ0TWD0unfTW1-Bb47pCyx3pJIJBEqBdxI8JdtzP5BNoNgVQiOlwTQ42tvxOMccSLOFU2_GYJ4Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4938ae1d8.mp4?token=WLwIYy-zy9IoVyW-xHioseEDWTEHI0FKug8qrr1IkgRYOLCNRr8tCCp4ZyF3Y0dB-5QrXI5RBTOG91fC7wyw9ixJpj-eYMYqcEYrlPjQv9E7CurU6XWi4yrh5wcW8YeyVjli35G8jnSbpLxbWM-ggrHQzl18u4P6XD4Omfgtp3vn0SLV0JcmbrspnEF1OQrbIsjg4ZcLogyU4yYi9qxa0nJvQ5ZrlPMM7mW4Zw7YPUJFZ3ZEb4-pW88sgJTEMK_NYKNji6YuNtxQ0TWD0unfTW1-Bb47pCyx3pJIJBEqBdxI8JdtzP5BNoNgVQiOlwTQ42tvxOMccSLOFU2_GYJ4Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های بامزه رونالدو از ارتباط صمیمی با پسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102416" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

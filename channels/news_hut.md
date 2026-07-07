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
<img src="https://cdn4.telesco.pe/file/gJQfLE1ObTYugu6coPDEtmI4T1wK2lBUZ2fCCR0nfpWzrVIID7RAWMTxZaIVfAUzFXGTjeAi_PVDYTfST4MzvAuA5Y4eA061t7PcWUOAacqYLx1WB-bdpgfN53anaD6stYg-JGLk0wI43ly0Tm7CVlxLHCwo2BHjyjJ3Yaoa4HFM2OZUn2MZnJFvZ2-w4BDUgVlGDWoDxI5UjV3AhUhQMMtv4EjetPDAfPfgGFNNX60yn9Rq9LbNouwRBg_3_1dNJCWAuGJoU7mfDPaUC644Er_YPdxbFkWOcWLNi2RHXwqcyvyVmEgI7RUoKZA-ZgdmB_gPIM8dwGqHaOIPffyCUQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 196K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 23:52:11</div>
<hr>

<div class="tg-post" id="msg-67435">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‼️
مرگ ژوزف استالین و نمایش سه‌روزه جسد او در مسکو، اسفند1331
@News_Hut</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/news_hut/67435" target="_blank">📅 23:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67434">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvvBw4QBM_gMZJonbMtT9ETJ8wQn0LRJv-78LPV7XfWyjIB36mwnsrdCPmhsUS58Z8aL-3EZunaWpEdVz9E9irnGEf8870Wyoo4gFw1wmqTMG1ZqYT7pkGQ96Yzf8xKA0ooVP8Mvbkuoi4tjtfuxNmrffWWxtR3VfICdN9sIlVdD5hAosO9NfGs8hY-l6_nq3gyiyUMbNdNuIrFG5gOn4kwkV39DzTk7n90eMGDzTa8nduPs4MqTHKYnIb-KIPmm58F4MD52fF8cUjJLRE5NhtbpA8eFgj4MbFOcKdaYkTZOqAuaNjwkONvqyYHnH9Flheg8eckDZFr23agjwUYBkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو ایتا چخبره؟!
@News_Hut</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/news_hut/67434" target="_blank">📅 23:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67433">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
ادعای مقام آمریکایی: واشنگتن مجوزی را که فروش نفت ایران را اجازه می‌داد لغو می‌کند
یک مقام آمریکایی اعلام کرد که ایالات متحده در حال لغو یک مجوز عمومی (General License) است که فروش نفت ایران را مجاز می‌کرد.
به گزارش خبرگزاری رویترز، این مقام آمریکایی هشدار داد که اقدامات ایران در تنگه هرمز «کاملاً غیرقابل قبول» است و «با پیامدهایی روبه‌رو خواهد شد».
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/67433" target="_blank">📅 22:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67432">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
طبق گزارش ها یک نفتکش بزرگ دیگر متعلق به امارات نیز مورد اصابت موشک در تنگه هرمز قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/67432" target="_blank">📅 22:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67431">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfyhFX9D5znAsE8eNpgIQ7rnhS7O3mLvFFjMpit_DKsYJjcAo_5oTl7QiXHRa5AcV_BrimWMfO89YrA3fgQGyadtHUTgndBDLOZtpkqKhTOpyNaQRbaFtzzdT6moFztxUwpiZnW9UTZV_gX6VPjRQv8lCB79gO1x2t8FDg8ZRezQS14_VpumiWh9hsfIkE0MsSt_CH4M3haX1kVSq18bz2UJvSdLsb6jKdpww3F3TeEyBr_aRf0uQFba4ru5pbmMpa0_dlmfbwgvY52D1ztL0DUaW8px4Vk9SXq4G85wSf-Davwn4ejav-O5YaJQlvAGcm3DiwZgwj2dHef5yRjJIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/67431" target="_blank">📅 21:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67430">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99630c1014.mp4?token=cCGQDMf7msqb5HQTGRpvf23oq2n765gSVLG-_iPPzN_crXRAYwl-MDVd9CwxSv3yH5pq2f1VXe4YfUYE-1ZpsTLSYxNHL1Kx4Ti2G5a5RnNpjZB-q7SEvm0XR4ZRQxxZoqMN2eq8_-CkFiPoYKl4u9QBm5ly68WRHT12LAhr_pNarV376S9oTdiHjU3SlXZNOJ3If_jwNccNyu8hWU4ROOy-PjWdd8FNPzCfbPSLow1vY_QUx0kh8CdLLqw86LHxioEqlfcG_W7u_HQdSIYyB9DrOM-UzC5oskDKI7eijjuczQrRZzjwpA81G5J3rQLZOeVCMJVYN995aZlcsDJauA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99630c1014.mp4?token=cCGQDMf7msqb5HQTGRpvf23oq2n765gSVLG-_iPPzN_crXRAYwl-MDVd9CwxSv3yH5pq2f1VXe4YfUYE-1ZpsTLSYxNHL1Kx4Ti2G5a5RnNpjZB-q7SEvm0XR4ZRQxxZoqMN2eq8_-CkFiPoYKl4u9QBm5ly68WRHT12LAhr_pNarV376S9oTdiHjU3SlXZNOJ3If_jwNccNyu8hWU4ROOy-PjWdd8FNPzCfbPSLow1vY_QUx0kh8CdLLqw86LHxioEqlfcG_W7u_HQdSIYyB9DrOM-UzC5oskDKI7eijjuczQrRZzjwpA81G5J3rQLZOeVCMJVYN995aZlcsDJauA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو درباره ترکیه:
من در واقع چندین بار با ترامپ درباره فروش جنگنده‌های اف-۳۵ به ترکیه صحبت کرده‌ام.
به نظر می‌رسد همه درک می‌کنند که علی‌رغم دوستی شخصی که رئیس‌جمهور ترامپ با اردوغان دارد، این موضوع ترکیه را به یک کشور دوستانه برای ایالات متحده تبدیل نمی‌کند.
برعکس، این یک رژیم است که با اخوان‌المسلمین آلوده شده است که از ایالات متحده متنفر است. او حماس، تروریست‌های حماس را پناه می‌دهد. از آن‌ها حمایت می‌کند. آن‌ها را تأمین مالی می‌کند.
اردوغان دقیقاً یک متحد الگویی برای ایالات متحده نیست. او نیمی از قبرس را اشغال کرده است، یک کشور ناتو دیگر (این یک کشور ناتو نیست).
اردوغان تهدید به نابودی کشور من، تنها کشور یهودی می‌کند. ما یک کشور مستقل هستیم و قصد داریم مستقل بمانیم.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/67430" target="_blank">📅 21:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67429">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUP2BOpSR0KD9442XTCpCSm3G27ahAcY_U8PmAwJ7e52EHHwX_lX_80uLEiZZ3rmGHMB3TBaoF2zQvJHKzDW-eQoOTyt7B7Hz1qIrCp4WkPC_pbwSPcRcp2KVeapHE86Pek1GUh0sSssRLFGkTm6xP1XdQ4xXvDUpnuFRjZbmIWQwU4mdhQjzDz5OByzprg51ZJtnMB_Ae9RCEuPCD_P-SNqnlNcFrN5WxqdRRwgmdUi3vvxrVhLE-GsFfW08LrcI12UN24Qv03tNuqOvTGdqiH-nk5e7WadI9uENG-Gc3jaAFe1u2h87pMM9avENh4i6fYwDsJbRdtgnqcG2RMMCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشه یه دختر ۱۸ ساله از فشار کنکور و امتحانات نهایی و بخاطر فشردگی امتحانات رگ خودشو زده و خودکشی کرده؛ این پیام رو هم قبل از خودکشی منتشر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/67429" target="_blank">📅 20:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67428">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDbMvRfgkISvMuZd03tzaAkrLA5Dlacc_A5GcI1WksB8aPUrkqbS3g-7UIXRuLgQevU4xNTX0M0PyCB6bAqQV5BvoByLaO_Or1ATnNuhggC0T5LYhIot4fiQ1QFLbccNbIlOoSn1IJ7rCOnxYihgfhrKRT2lce321N0VnhXJP_cLdlbhagDYiYyZil1QMW-lr-kSj9KgPLxdud-gww4XkBemRC6kUuCpj2vpsI7FXjLoadWLAV_SQ_Zpb6qxgw_oV0HBhpSPeyVazUA5dFCtIHwolCyXwOOns9XKaaPtOJlzoroScl9wHjTpCDA84iA566RMMb2S0WDX_a2tPMwqVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ان‌بی‌سی به نقل از یک مقام آمریکایی:
ایران شب گذشته با استفاده از دو موشک که مسافت کوتاهی را با سرعت بالا طی کردند، به دو کشتی حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/67428" target="_blank">📅 19:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67426">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GqbLTE-BTczhtrIIoBKAZ2_6dQWaru8Tsu-6SGzJdeZw4_Uz4HbTFjLc_rJ1YQFm-1aDndtDWS-2IqEOxa0rnlZ8BcN1A_qMUYkhEFqgueeZmJI6CknGwWrvMAk9ir0EsID1y5PIn7VVDAaAMGF2z0OKS67AGCcxs7VQ73yvpbYV8Dwdmd6iD3Av5IKL9GjwRcEI6gQCXk1yn9JjDS0HO81JZIpeFPD8MeIeR44KoOZkJGD251RP47Xp3XvrqoVOmG52wdtjSgluENVQ6WuK3NBCGsHrHJAsHGkLM8s6Vs4E6B8eVDlmMkt8tb5jsc8IC7FXSqAziJD70RKaXmM5cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rpWhV9hOf7672TONyWDvUCiNIkb824s9mLLUx0KE9r_U_aq7vGRpO6cnjYwANQ8sd_MATEpmCouGorNMhSq6UjquIqyFfgLT9C7Q8op_FzACzrzUJ5wjjIiKEZUlGPF5-cbw-zwp3EVdI9Plmmbb-ct80nSuznQqSRshxot59n5Ul0NoZm1AtZ54Mg9a5VtYX2ajcQKBnxXGUMY9yJ_nt0bo9Z73VQp0Ap1P16FLnsjQngZqReXEqkixnwSubSyTv5_WA21XSA9eCFrvZg2xNiACsQj4cYVc-e9FG4TaLfmZB35HkKffV5JnDkKGY_TB15Bt3rejFTiWtitv16s5rg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
صدا و سیما این تصاویرو با زیرنویس جمعیت میلیونی مراسم تشییع منتشر کرد :
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/67426" target="_blank">📅 19:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67425">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3431abb0e.mp4?token=qvR_AGW3rXc29IS5zvtBTo4_7GMiCZHz0KVv-sm8Sa8Y_lwAcBsXZP9eqKzHvioDVvNM9h7dPtQ8ofDdzC08vxJqzYqKvW_uY50VeC6BBDrwuYOJ22jwnIQAEbq0GNmnB5ZPphC9gFZhlM-2Xuxdis97tsfhMTTtEcqmz8zdNngDlE9GRIpLxbE24A3PH_MbOAOcRcQw-BWoEwlWOBLs1pCkhVnYi-vQsAIp_hGDD-RYuhG5_LldoGCvtim1Bu1-nH834hg37piLz3KkyuimY6tKhSqh3nBxXC-osaLQpLHtElPj2FuaOsQqlIbQPQGYAf0Qdg895uz4F0m2HXaxSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3431abb0e.mp4?token=qvR_AGW3rXc29IS5zvtBTo4_7GMiCZHz0KVv-sm8Sa8Y_lwAcBsXZP9eqKzHvioDVvNM9h7dPtQ8ofDdzC08vxJqzYqKvW_uY50VeC6BBDrwuYOJ22jwnIQAEbq0GNmnB5ZPphC9gFZhlM-2Xuxdis97tsfhMTTtEcqmz8zdNngDlE9GRIpLxbE24A3PH_MbOAOcRcQw-BWoEwlWOBLs1pCkhVnYi-vQsAIp_hGDD-RYuhG5_LldoGCvtim1Bu1-nH834hg37piLz3KkyuimY6tKhSqh3nBxXC-osaLQpLHtElPj2FuaOsQqlIbQPQGYAf0Qdg895uz4F0m2HXaxSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمزه صفوی، تحلیلگر سیاسی و فرزند یحیی رحیم صفوی، از فرماندهان سپاه پاسداران و مشاور ارشد رهبر جمهوری اسلامی:
🔴
دلیل اصلی ناکامی جمهوری اسلامی در دستیابی به اهداف هسته‌ای «برتری اطلاعاتی طرف مقابل» است و مسئله اصلی، نداشتن بمب اتم نیست، بلکه ناتوانی در حفظ محرمانگی و پیشبرد برنامه‌ها است.
🔴
برنامه هسته‌ای جمهوری اسلامی یکی از پرهزینه‌ترین پروژه‌های هسته‌ای جهان است که این برنامه «نه به تولید برق منجر شده، نه به ساخت سلاح هسته‌ای و نه به کسب مشروعیت برای حکومت».
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/67425" target="_blank">📅 18:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67424">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GOB3J9qdHkd1ZKazpc7lmXW5lY14nQdpWQEDNaorB9T9dizWADwADq_We5BzSqrs5VB08b7Hj00mRbaAsca1KCx2sM7N26IufXlvv5l-2xoqTmV8P7CrKCGEAn10_nGeKLPUarnGKzGEEJ1FyJmRBkst_Sak_LLqwKuGgjCRlls-CAAdcJ44gaFddj5pm05G-1Rj-RyF6tinivRUdzEG0CGRVFGe6J0RYCll-U0rvTz36LjAbjuaMqKK5PYJbg9xBVs1a0bFCxQyQk_MaHuVJ64idDZDLX6t1eOLi4Wrdi9rxQ3nAph3LGOkl4wKiqrkXEcNvtOlLvA9hqYX06JG1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سازمان عملیات تجارت دریایی بریتانیا: یک نفتکش روز سه‌شنبه ۱۶ تیرماه هنگام عبور از تنگهٔ هرمز با یک پرتابهٔ ناشناس هدف حمله قرار گرفت.
این نهاد اعلام کرد نفتکش بر اثر این حمله دچار «آسیب سازه‌ای» شده، اما هیچ تلفات جانی یا آلودگی زیست‌محیطی گزارش نشده است.این حادثه یک روز پس از حمله به دو نفتکش، یکی حامل نفت خام عربستان سعودی و دیگری حامل گاز طبیعی مایع قطر، رخ داده است
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/67424" target="_blank">📅 17:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67423">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a07aeb18ec.mp4?token=T_PxOHuayfH5c1QROdGVAipA7O9Pr_735hoKfq86Vxo1T8QgqRdPRIAxDUMEBSAqxF8GlnEndhkbyuUs57UcU3eAmOhsmaqjQs9LdZa36tEPzoPnsyKMJUhh17EzrRog-S4tCxynCkflB2VNDIy1DahW2pFL3hUeHh_hjJm0vV12JPfkClJ2elF868qsWBeyR5pE1gBRkpA2MCq1Yy7t1u5Y1-qP-2ZSVcLJ70PfNs-3f77wY0DIEe3bJFQyoKL3gHrsy9epjMFIWzSG8_hiYOllJxglokj7JR59cnTXYC5ujsTrnsNqvyx6DWJv8NPdMXWg-x3aUAtVmhjvFu2qNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a07aeb18ec.mp4?token=T_PxOHuayfH5c1QROdGVAipA7O9Pr_735hoKfq86Vxo1T8QgqRdPRIAxDUMEBSAqxF8GlnEndhkbyuUs57UcU3eAmOhsmaqjQs9LdZa36tEPzoPnsyKMJUhh17EzrRog-S4tCxynCkflB2VNDIy1DahW2pFL3hUeHh_hjJm0vV12JPfkClJ2elF868qsWBeyR5pE1gBRkpA2MCq1Yy7t1u5Y1-qP-2ZSVcLJ70PfNs-3f77wY0DIEe3bJFQyoKL3gHrsy9epjMFIWzSG8_hiYOllJxglokj7JR59cnTXYC5ujsTrnsNqvyx6DWJv8NPdMXWg-x3aUAtVmhjvFu2qNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تندروها عباسو گیر اوردن دارن بهش اشیا پرتاب میکنن و بهش میگن بی شرف
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/67423" target="_blank">📅 17:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67422">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f260072fd0.mp4?token=N-2OTgl8xcbYnexWj5VfzqZVAFINe-VdCoQXgR2vnk9NNaJnwWHLp3eeqD3ecM35O0878-1rTiq4XmcZuXa0TJW79gQxZLzXmlAPsZrcSxUrwaT07otxAp3GcfB5IiC8z_-4Os1tLIOV4HYpWvmeeMWP0wuqLM_D-lU1B0L0Bvru93c-fRQhTJoiZcjv5snyYbZjgzZlUnR4ZZIiPSLyqh-izLyYAgfsn68XKRRhK4kt2hQ5XQxs-nPcczXL7k9inKzgk94890p_29LqE8IECwszT4ZZE5yjR0MbSoq7BcM5m26xCKOPTXt8nWmDwnMrOPyL2aWN4UnY68fx-f7HbzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f260072fd0.mp4?token=N-2OTgl8xcbYnexWj5VfzqZVAFINe-VdCoQXgR2vnk9NNaJnwWHLp3eeqD3ecM35O0878-1rTiq4XmcZuXa0TJW79gQxZLzXmlAPsZrcSxUrwaT07otxAp3GcfB5IiC8z_-4Os1tLIOV4HYpWvmeeMWP0wuqLM_D-lU1B0L0Bvru93c-fRQhTJoiZcjv5snyYbZjgzZlUnR4ZZIiPSLyqh-izLyYAgfsn68XKRRhK4kt2hQ5XQxs-nPcczXL7k9inKzgk94890p_29LqE8IECwszT4ZZE5yjR0MbSoq7BcM5m26xCKOPTXt8nWmDwnMrOPyL2aWN4UnY68fx-f7HbzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توضیحات واعظ موسوی فردی که تصویرش به اشتباه به اسم مجتبی خامنه‌ای در فضای مجازی وایرال شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67422" target="_blank">📅 16:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67421">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6696a22a99.mp4?token=VfMMQmohHgUdruhzRgg7XuyMHAV-Mjmj3oIZwbysknfMAh3TCHUjK5ZXvOaqz02aWBzdlmyweEDeVvjP6MDX2twLyeUXfBZqbinEblWHM0Xs7ge4JUrcbs-uEjVx_U-fYhv4d4I-97S-2ekG7iTyBmoVPmKhuD-97gbVUnL9HzSbG0zA1rmRo5uQV7ck5hsOTqX8A2KJ-BHuYmC6leJ8jwsKMs8pC4mD4m1pdnFEazfsBzsAbr5hiPfK8SsClef3GGcDOh6Ksg_ldrX5NTgMji2bpllRYXQU6NSJdgAF4uqb1EzoIPXjTsOH-_uY5PabJtZ5W7gsLzu7WoJGC0syiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6696a22a99.mp4?token=VfMMQmohHgUdruhzRgg7XuyMHAV-Mjmj3oIZwbysknfMAh3TCHUjK5ZXvOaqz02aWBzdlmyweEDeVvjP6MDX2twLyeUXfBZqbinEblWHM0Xs7ge4JUrcbs-uEjVx_U-fYhv4d4I-97S-2ekG7iTyBmoVPmKhuD-97gbVUnL9HzSbG0zA1rmRo5uQV7ck5hsOTqX8A2KJ-BHuYmC6leJ8jwsKMs8pC4mD4m1pdnFEazfsBzsAbr5hiPfK8SsClef3GGcDOh6Ksg_ldrX5NTgMji2bpllRYXQU6NSJdgAF4uqb1EzoIPXjTsOH-_uY5PabJtZ5W7gsLzu7WoJGC0syiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های اخیر علیرضا فغانی از ظلم‌هایی که فدراسیون فوتبال در حق او انجام داده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/67421" target="_blank">📅 16:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67420">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLAXqWArnxmMdoLI8Fl8jf_6XaNbwcgmocPEEvBrDIBPt-0PypG0BDgPjr8i_ZEtys3myqXSeUHgAmKYyJNyT_DHJG-GAXJ17mswryhXtHxkDSGQlSFA-9mS7OZqy8iWCOIWhmVD2qPP_rBrlTwSzf1nMZ080sCkNWT51H6XYu0wLvg8P4d12CdtJe1jVoKvMEcfjYE8vSA6W6MgdMamE8hOfPhJfTk6h6UITD788vXgk5ws6OjZj0Z30xVChAP5iXDJ43TrTeqZR8HrIyA2ZJfAxzj6cz70_ILNbyz45J09yL09LKsZDHogvg75O48RmCDYIqkzck9GRThpXg9khA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خبرگزاری
CBS:
علیرضا فغانی قضاوت فینال جام جهانی 2026را بر عهده خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67420" target="_blank">📅 15:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67419">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aca7d1936.mp4?token=SCCFwtMj_NuQKa19AV5__Q9ezOq8jUHi7hCyJADhftFiGbL8SbOSUeAOzC25wNfeXZ7EMk98Fhhrzzbf8tdZpRYsGPOPLOsEVRnSiXv7LWUfiIrno4fqKcEBwPT-IWaYHeW7MIm0wDnr8vDxNRQ0isDHKOrbI9cENk0uZ2FkPmfukgPxqqEpumyc8Flln1ncipx3qTbWeiVEz-bxbxHjn3XRtuCvjfZMpoDUac6-t8XPO_AF3zH1FJH2JH-v6f7MwEjzKy3J7sF4iXGoqj0Q_dRs-lSZxZzt30pgGfKh0fAShpgW90VcN3sNd0rDICZJlyFcK-KiRlhNEJXJwzxvNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aca7d1936.mp4?token=SCCFwtMj_NuQKa19AV5__Q9ezOq8jUHi7hCyJADhftFiGbL8SbOSUeAOzC25wNfeXZ7EMk98Fhhrzzbf8tdZpRYsGPOPLOsEVRnSiXv7LWUfiIrno4fqKcEBwPT-IWaYHeW7MIm0wDnr8vDxNRQ0isDHKOrbI9cENk0uZ2FkPmfukgPxqqEpumyc8Flln1ncipx3qTbWeiVEz-bxbxHjn3XRtuCvjfZMpoDUac6-t8XPO_AF3zH1FJH2JH-v6f7MwEjzKy3J7sF4iXGoqj0Q_dRs-lSZxZzt30pgGfKh0fAShpgW90VcN3sNd0rDICZJlyFcK-KiRlhNEJXJwzxvNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ برای شرکت در نشست ناتو وارد آنکارا پایتخت ترکیه شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67419" target="_blank">📅 14:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67418">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FufM9s0BnbhzEk_jQm9Q0Yl9GCV6tV1GCMCTG-VTMkGOfUR5RV8Ej4dF_9TfN9OYUuwvZJ3TxNH6hUZ8WQvriA-ma8hgvJtk25sYC1r9nepws5BkrvjKBKImA7pE7-6Sg-Xo7cUXCfjsskgAj5XFxceJ_X-cgvLJLseEbc0NsMuMfKtMBecyPWtzWae8tsjOavMAoWcnNYaddiII0BSH_hTi1SYb2KEJs_Zyb2Yzi3UrSud-NLwFmviw7bkFyxjj8sNTzWQFgK64r4jwC-m4WQHNNPyPRjqznIgHNg03Vw6K5ah9-mJiTPiHzAkwZCc5JWO7oF0UU_8khlOZ8FkNmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری رویترز به نقل از چهار منبع آگاه گزارش داد نفتکش حامل گاز طبیعی مایع «الرکیات» متعلق به قطر، هنگام عبور از بخش عمانی تنگه هرمز هدف قرار گرفت و آسیب جدی دید.
🔴
به گفته این منابع، این حادثه پس از گزارش‌هایی درباره شلیک موشک از سوی سپاه پاسداران به کشتی‌های تجاری در حال عبور از این آبراه رخ داده است.
🔴
بر اساس این گزارش، پس از اصابت به سمت چپ کشتی، موتورخانه آن دچار آتش‌سوزی شد و دود غلیظ امکان ارزیابی بیشتر خسارت را از خدمه گرفت، اما همه اعضای خدمه سالم هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67418" target="_blank">📅 14:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67415">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/la-EsNavPi8ioUicveS8bGTT8T1lU6Nt4ggs0j0yiQkyfXQxAsQ2KImlW1iTMmJ-BnFeTccdvqwRmOQdA3jDL5gURBh64aVwhOAw3zs7XAk3XQP8zKfv1rE6b0_xwGsY11-4kUp-oSzWpoYIL_hz9kFMyNro2kl_GvYqpWmPHH1nlxvNEbjPRWlH563nHsQLUbAsYNGwm-yKvBwWJShIsKqcC6XOjkIpX6clhRYFbElvzUi5JZWXPxtAZu1aF0hGhEy5YDMZvw7ug7-dz9nG-4z6LPgC6SK6maz4QpxlDg5yCxom3MmTlK4cMuuM4ZXcBMmff11Xuk4m8S2I_Wi_Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c0b1a540.mp4?token=f-LHuAXtuItTRBOF1J36KFVybI0sS6BG_XFRXJI8sQOLA8QNP2mKHlzjg6y--JwkD5g9p8e1u6ViHFia7xQ9z_L1Rm-GY4TB-P7dAK0ZrnSlOGSWe9cjzNdovsde4TTDsKGKlGVGI4p2wiNoSm2ha7_mbDitSKi4ZoEaCuPRMAm2oZXTXnDKsBJ9kBWAMGiFMURY8aY0xigfVtfbbN6t3ogGfeVIh7dsXMfqTN7djetuXUOVV6ovXxPtN0IDiMFNtSDVV8G2fvXEsUNTPinMOp-0BT1JYkyBR_l61v-k8uUOU-M-TxSSdND0Nbg-veYOUH3bAv1v1kMYPZ17Wk7DMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c0b1a540.mp4?token=f-LHuAXtuItTRBOF1J36KFVybI0sS6BG_XFRXJI8sQOLA8QNP2mKHlzjg6y--JwkD5g9p8e1u6ViHFia7xQ9z_L1Rm-GY4TB-P7dAK0ZrnSlOGSWe9cjzNdovsde4TTDsKGKlGVGI4p2wiNoSm2ha7_mbDitSKi4ZoEaCuPRMAm2oZXTXnDKsBJ9kBWAMGiFMURY8aY0xigfVtfbbN6t3ogGfeVIh7dsXMfqTN7djetuXUOVV6ovXxPtN0IDiMFNtSDVV8G2fvXEsUNTPinMOp-0BT1JYkyBR_l61v-k8uUOU-M-TxSSdND0Nbg-veYOUH3bAv1v1kMYPZ17Wk7DMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رویترز:
تصاویر ماهواره‌ای نشان می‌دهند که هزاران ایرانی برای مراسم تشییع پیکر علی خامنه‌ای، در پایتخت گرد هم آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67415" target="_blank">📅 13:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67414">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28f2d062cc.mp4?token=v_ndpivhsS0hVLt3YBn0H8aQ0sZLrNebi4gbchlpEyMdKBKetgt-dt3q-KX28wfR2ffNDBjOQ7B-gipL_Sq-zM1OTAVuHJ9u0sAhIo02s9J7OzdpZFQYqs0c2Gx-n6L056QG6VOVH2hyHVlLwiCRwC3_6g1uBj-7ge3xXpGHMrlw6RQZU31OMysaQ8txef3Fo50rZcLuGMrpnqBbEASQjTmwJB9UDA4DuGoyXxAOv9pagmFMnpFmDjAnat789YD1yuh41QARo2lks06zRfxZHA361MfdzDA9KrZGDWUm6v9ZSSMp36yLATUgHQtEt45xtwL_734i400TJywHuMknqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28f2d062cc.mp4?token=v_ndpivhsS0hVLt3YBn0H8aQ0sZLrNebi4gbchlpEyMdKBKetgt-dt3q-KX28wfR2ffNDBjOQ7B-gipL_Sq-zM1OTAVuHJ9u0sAhIo02s9J7OzdpZFQYqs0c2Gx-n6L056QG6VOVH2hyHVlLwiCRwC3_6g1uBj-7ge3xXpGHMrlw6RQZU31OMysaQ8txef3Fo50rZcLuGMrpnqBbEASQjTmwJB9UDA4DuGoyXxAOv9pagmFMnpFmDjAnat789YD1yuh41QARo2lks06zRfxZHA361MfdzDA9KrZGDWUm6v9ZSSMp36yLATUgHQtEt45xtwL_734i400TJywHuMknqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جکسون هینکل فعال‌رسانه‌ای آمریکایی رو بردن میدان انقلاب و خودش داره شعار«مرگ‌بر‌آمریکا» میده
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67414" target="_blank">📅 12:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67413">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/440a1d9ab7.mp4?token=UWcRJN8H0x0swhDwITLP-VWgZmcGBaD-Z6rcT17yq_kNU6Xl4iPPGbV9z-wwvlSrdtrEP0EKI70dRk5Q08Oz38BkTIikde4DauaOJhGKJC9s2E7SQXq6zQb7x_3L8y1EJHSoJiFjhVpyQruAzueKbbypNjmpgQDArBdbIxBLnWzIoh1-1DpkDLhFhaGvRWV_YkJYS1w-Rng04tC8T4rRTd5AKkaSZ_LS9k-t3W_14w1dMXpzHeKNestjQz-2J3HjVLONGC2wyXT-1K1f4uXBWP79CsXnq4oBIQZxTf1ek1ZuEdLzURAFkQBDEdLwmOr95mUCzhcol-deMZxNgrv6pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/440a1d9ab7.mp4?token=UWcRJN8H0x0swhDwITLP-VWgZmcGBaD-Z6rcT17yq_kNU6Xl4iPPGbV9z-wwvlSrdtrEP0EKI70dRk5Q08Oz38BkTIikde4DauaOJhGKJC9s2E7SQXq6zQb7x_3L8y1EJHSoJiFjhVpyQruAzueKbbypNjmpgQDArBdbIxBLnWzIoh1-1DpkDLhFhaGvRWV_YkJYS1w-Rng04tC8T4rRTd5AKkaSZ_LS9k-t3W_14w1dMXpzHeKNestjQz-2J3HjVLONGC2wyXT-1K1f4uXBWP79CsXnq4oBIQZxTf1ek1ZuEdLzURAFkQBDEdLwmOr95mUCzhcol-deMZxNgrv6pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
محمدباقر قالیباف، رئیس مجلس شورای اسلامی، در حال دادن شعار «مرگ‌برآمریکا» (12بهمن 1404)
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67413" target="_blank">📅 12:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67412">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYlP_uxCncPxCbLRD_hf-J3niwf2NZG8kIwQoxINOHOzJah1uwQv3eQ1dPi3NFgh_ntAgz4yX3Y7YkLllfv54cv9_AABve-sL70W5Sss7VhNGlMI2Vz5n8nUEXtaohq97tis50oeQgp05uyW1a9UQC8JXM7DG6VOdDxZMyUzuyMKP_friAOvNAvPmjqrYAmLemgcjd5ZgD54EYQoxnm4ItfDI95euOYGpIcuvOnv3d-BU-yigvV9yotansQp7s0yyGv3vQFejXMz32_y82-EqBXK4W_GiVH7CZ5-3m5dS4_I0PNZf3Sp44rTgfLBjz2TCgmV-8QoBRZr9ebkG6lx3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس:
دو مقام آمریکایی به «اکسیوس» گفتند که ارتش ایران دوشنبه‌شب دست‌کم دو موشک به سمت کشتی‌های تجاری در حال عبور از تنگه هرمز شلیک کرده است و دو کشتی مورد اصابت قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67412" target="_blank">📅 11:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67411">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‼️
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
احتمالاً نباید این را فاش کنم، اما ما دو تا از بهترین نیروهایمان را برای محافظت از قاآنی در مراسم خاکسپاری فرستادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67411" target="_blank">📅 11:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67410">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/64666ae825.mp4?token=niuo_6rQ1ZcI2lLPhwikCm-4VhydqV-gFU2CLM2d2GzosGCXVpf2Cm3E1n5OQ0kFQskXHXgc9XpUZdiRbgnjFu8_EMfvx8LMTpdAQnHKjlg2Nz-H7Avq5oCxl70IUittsGuVA9-ZIo29Q7Fh3v0jTYTEVf8AHE6eR40krvdchTmGE6BcotiOKWwkFkLiwHwAnV4r-la9DfjoMFt6eJh20jtWCrAxRzeSGauAX_ntHGLYPbv5FgFMAHPavFwOUBYFHf2gSP6DWsj52n1OHPLgoDaEMFSaVrQjCztszvJg772aQVKzzsaYiwUsHmzX2JDvebQOzMbxDv91L68EdF68UA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/64666ae825.mp4?token=niuo_6rQ1ZcI2lLPhwikCm-4VhydqV-gFU2CLM2d2GzosGCXVpf2Cm3E1n5OQ0kFQskXHXgc9XpUZdiRbgnjFu8_EMfvx8LMTpdAQnHKjlg2Nz-H7Avq5oCxl70IUittsGuVA9-ZIo29Q7Fh3v0jTYTEVf8AHE6eR40krvdchTmGE6BcotiOKWwkFkLiwHwAnV4r-la9DfjoMFt6eJh20jtWCrAxRzeSGauAX_ntHGLYPbv5FgFMAHPavFwOUBYFHf2gSP6DWsj52n1OHPLgoDaEMFSaVrQjCztszvJg772aQVKzzsaYiwUsHmzX2JDvebQOzMbxDv91L68EdF68UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گفته میشه این شعارها علیه عباس عراقچی توسط تندرو ها داده شده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67410" target="_blank">📅 10:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67409">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbee8c865f.mp4?token=lOlgik0_XL1sMPxiLLHSgifb2MSbyJGLbT2tOywqg0t0RJ9xUHr149WKbK7tU3QaDN0o3zxsayeDpAsjqHxrsO2IhHq6kgYeD22x5idnp4XuQv7gNq3-B7Q_mttD2GmG0r3COhg8NqCn1ps14sMBcWJLZV2wV9oVRd3LNMA_PvXky8vhRsmd0MKgLeaLluMGDMq7yjp2MvVoq9rhAsGO-JQDahyxqunQtHRAC3LKygTRhn2T49Rtq95Zw4QRR_GnPGHdn9HsV3hH7A0tobArIzDa-Q-5u9x1QQvrvjmIGIVM5HgXtYcZcYGJM_yCXV9ElKny__mCVKi7NfxpCl9RygXKBDqmevhqzdYHtJz2WpCiDLBihGm0wtJw5Tpa2v-53JUjpSGVvQzLlRF7q_SU89EC0sfxjG0MOZhCF9E5Yv1JcVcNdNfMcUGqAnv9K52RIR8KYaFwauDluI_ELvblQgdjxKx5Ryo-woJks6laN6CAv-Wy0GKBx7WTO4_KabsjNQscIeCPn4ftfoP2lsSkQbG2yUI6GQShstHl7Kbft4qqLLVC2Wo1ntLQLqs8w9hHppQ2zCaekSlt6pu3M35Z4UpzFsfQDIiSs9PtsEuYs4cHJwWzF4_jsgqqMcItz7GUW3JLoqzNWmy67MI0xhhOD5TI8Sd9U1qS-elxVpqAmk4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbee8c865f.mp4?token=lOlgik0_XL1sMPxiLLHSgifb2MSbyJGLbT2tOywqg0t0RJ9xUHr149WKbK7tU3QaDN0o3zxsayeDpAsjqHxrsO2IhHq6kgYeD22x5idnp4XuQv7gNq3-B7Q_mttD2GmG0r3COhg8NqCn1ps14sMBcWJLZV2wV9oVRd3LNMA_PvXky8vhRsmd0MKgLeaLluMGDMq7yjp2MvVoq9rhAsGO-JQDahyxqunQtHRAC3LKygTRhn2T49Rtq95Zw4QRR_GnPGHdn9HsV3hH7A0tobArIzDa-Q-5u9x1QQvrvjmIGIVM5HgXtYcZcYGJM_yCXV9ElKny__mCVKi7NfxpCl9RygXKBDqmevhqzdYHtJz2WpCiDLBihGm0wtJw5Tpa2v-53JUjpSGVvQzLlRF7q_SU89EC0sfxjG0MOZhCF9E5Yv1JcVcNdNfMcUGqAnv9K52RIR8KYaFwauDluI_ELvblQgdjxKx5Ryo-woJks6laN6CAv-Wy0GKBx7WTO4_KabsjNQscIeCPn4ftfoP2lsSkQbG2yUI6GQShstHl7Kbft4qqLLVC2Wo1ntLQLqs8w9hHppQ2zCaekSlt6pu3M35Z4UpzFsfQDIiSs9PtsEuYs4cHJwWzF4_jsgqqMcItz7GUW3JLoqzNWmy67MI0xhhOD5TI8Sd9U1qS-elxVpqAmk4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش‌چشم، کارشناس مسائل فوق استراتژیک:
باید هزینه بالایی برای خون خواهی امام شهید ایجاد کنیم. کانال ۱۴ اسرائیل می‌گوید رهبرشان را شهید کردیم و هزینه‌اش فقط ۴۰ روز جنگ بود و دوباره می‌توانیم این کار را کنیم. این بار آقا مجتبی توانستند جایگزین پدر شوند، اگر باز رهبر ما را شهید کنند چه کار کنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67409" target="_blank">📅 10:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67408">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7142559e9b.mp4?token=W9U9HT3RZssBHCaEO_LW6wmAYVV6dnP5FlgsI-s8R5CqrZOGl4_wOA1r8U5qATQ2OhnsA1NRoDFQiL55mjIxVuRETCNghm7nwwLBzpCJ20VNpcQSeaOHJHuZ2nui3qeMkOQm_Eqy_A3IMwy9JU89QEAAKue0mHkTsQEUD5yg3fnjNBSYfEYbyEkleXBNkRmEdQ1-q59XE-iT1ld73vS2Gj_jNFCaKCPYEk7NXldEZG4_yiDLd9NQLcRFiLxJhHAzEwRei7yEug7cZtBMzZze6Wgi12efWj2m0vSY56SfAmoi7SAURVOGl8F_psa2--xr84r0QO7-s-DqpP_dzfTQIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7142559e9b.mp4?token=W9U9HT3RZssBHCaEO_LW6wmAYVV6dnP5FlgsI-s8R5CqrZOGl4_wOA1r8U5qATQ2OhnsA1NRoDFQiL55mjIxVuRETCNghm7nwwLBzpCJ20VNpcQSeaOHJHuZ2nui3qeMkOQm_Eqy_A3IMwy9JU89QEAAKue0mHkTsQEUD5yg3fnjNBSYfEYbyEkleXBNkRmEdQ1-q59XE-iT1ld73vS2Gj_jNFCaKCPYEk7NXldEZG4_yiDLd9NQLcRFiLxJhHAzEwRei7yEug7cZtBMzZze6Wgi12efWj2m0vSY56SfAmoi7SAURVOGl8F_psa2--xr84r0QO7-s-DqpP_dzfTQIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش جالب یک مازندرانی به حضور سعید جلیلی در مراسم تشییع علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67408" target="_blank">📅 09:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67407">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adGwCLx9eEh1FygU73EM_ZoPQJd4VYbC55Ro8NihT-eWJk-YhmKiUqOixndjv_rISnBb9vKlRibov0VIfz8lXZWgjha8XgJG4jZLF8OCylvHL2V2VuJ3D3w39665yW06NGRn0EQGwktP5AM8XfqDYNXDtwESF8l-g3WB7tTs9Uabu9FZ9e0IGzeNEcEUnGbJmjPnFIBP9vB94ZCQ4gJQOJPRjlnXTDRbp2JDX7ybNr1jW8bW68ZFFivPNoetmfnnTNutjyGFLRxwgWtf1-6Tl9-7Tl-kKu6IMXQ0HeNewfW_bn6ffrCtt-IjyFGwThdzlSuc-NMKOAqvfrcLPjgwwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
❌
مرکز عملیات تجاری دریایی بریتانیا:
یک نفتکش ساعتی پیش در فاصله ۸ مایل دریایی شرق «لیما» در عمان، در کریدور جنوبیِ تنگه هرمز، هدف حمله و مورد اصابت قرار گرفته است
بنا بر اعلام UKMTO، این حمله باعث آتش‌سوزی در سمت چپ کشتی (port side) شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67407" target="_blank">📅 09:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67406">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67406" target="_blank">📅 03:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67404">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dF2R21rBKMnHVBzd-0DSLbG8arzibz_NOlVVQXHhp7TqiCy3C35gyVO_ujomuXh1c-AO-2b4u9z9MxKWFwstxFtU0MvWFtlG3eT6f2nQqfI3lpuqurZkV7ineblz-uUE7D-6agjwlThAAcMef8x-_cTKQgBkPlGH5gI8tk0DolHUqPt2xFiDtz1YGo0YW6mJjK73w5GhbrG3Aq7uMSgp_7cXWCy8mnGQWfHyqJ4hHmovshC_2Labw-onfNBE3gQQ_DgSoYDoZ29dRxat9R9hCb8_bk3JtCxy7SvQ6K_oOp-XgAFyxLZT853UxvKDs-tjOoZyLrsT6_0taOakZDn4lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67404" target="_blank">📅 01:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67403">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcKnfvUD0Q_wtXR201axM7XEKfyT3veyRPwM1wqyf7uboerwJQwsuUwT8TDp8jcFXEy0jTDALXqyjLeYLXLDqJ5ysxzG8nsGLRmdHyAiSIFguaoTklISlxNU44BsL_MPVWzZXoLr4YdBteWVWKOO8lKM7RRgO_0C4WsKJFXspbHPmKDDpZB48WvMea2GuBXf3GJ2kKkd8Y1uG8kw_WXSbjXF7Dv3T1fQSCkdK4MpNpeHOHyFUPiYsXG2syWEQru8n0q9i37nsB_6np25HJUxEYiBFLFUjHQLPKOWi201ccpPp0RC5UCniwVtSc5iXg887A8IJTNKv7UnrvP2l2JNeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی 2026
| حذف کریستیانو رونالدو و یاران با شکست مقابل اسپانیا در دقایق پایانی
💔
🇵🇹
پرتغال 0-1 اسپانیا
🇪🇸
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67403" target="_blank">📅 00:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67402">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1Z3D6uDvAGkTzI7MItqs08nAsolMq_msqCzudSx3SIF0Cnbo7FaDgp1nWNMRWF78Hc5lrC4zfw3Tq3aVCM7P1N9aWVlUko8_T-4rdXOrGL2wvPCTWN-NVqQVrc9ZXPC5rcPqJDX5prv8CpreMUBSQCEZvBLdvyd4nll7ZlA8OO4lR4UWuP3M0rENum51fV53OF-M6Xm5y-u8a6HwIUHXNWPp8oWKOnzSbOCf8sB1_Ffql772jDh9_cPpZvgJhtwWBLnkXSHsx9qz0bJqtYSqzkNuJTWI854EeJjrMVdCeDuTInigZfD6hrg1_fjy2WDCcgbYyAb9sNoV_JOiNfW7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ادعای کانال 14 اسرائیل:مجتبی خامنه‌ای در مراسم پدرش حاضر بوده.
🔴
حضور مجتبی در مراسم تشییع تأیید شد
🔴
مأموران اطلاعاتی خارجی، مجتبی خامنه‌ای را در جریان مراسم تشییع امروز در نزدیکی میدان آزادی شناسایی کردند.
🔴
گزارش‌ها حاکی از آن است که وی با پنهان شدن در میان گروهی از دانش‌آموزانِ حاضر در جمعیت، تلاش کرد از ردیابی بیومتریک بگریزد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67402" target="_blank">📅 00:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67401">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/781360aa4f.mp4?token=ANLfUzZrr_UGrTsuvMS60ffPuWqBUhqbfS7_Kteb2-nOcdNJexeIiEhOv6EdaZ3Kwp2iGJdM7d2N186DEV45eiYwHm2rY0Kemk2Nd_8f7P_Q09ZUGSxt-A3lnD3X0LhTM8lNR9RVIhmWtN25OqNtyP8MjZ-ymNQil6spN-5ODaspF7p9reGF_jYUEwtx1G6RAUJvg3vyVdcyidstDZNJfs8f4hiGUFzUBcSrkZjhP05luZbe8ZydXmSCx3I0ua7zuG2WivuWgMHJfsXLxAMWQoNJ0TQ5Q0Xl0tGzEoil2hBkWzW-p0bf7yGaguS0YsG-zIUPyFFHo1zS1vip54eFiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/781360aa4f.mp4?token=ANLfUzZrr_UGrTsuvMS60ffPuWqBUhqbfS7_Kteb2-nOcdNJexeIiEhOv6EdaZ3Kwp2iGJdM7d2N186DEV45eiYwHm2rY0Kemk2Nd_8f7P_Q09ZUGSxt-A3lnD3X0LhTM8lNR9RVIhmWtN25OqNtyP8MjZ-ymNQil6spN-5ODaspF7p9reGF_jYUEwtx1G6RAUJvg3vyVdcyidstDZNJfs8f4hiGUFzUBcSrkZjhP05luZbe8ZydXmSCx3I0ua7zuG2WivuWgMHJfsXLxAMWQoNJ0TQ5Q0Xl0tGzEoil2hBkWzW-p0bf7yGaguS0YsG-zIUPyFFHo1zS1vip54eFiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعارها برعلیه پزشکیان
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67401" target="_blank">📅 00:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67400">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتلوبیون اسپرت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwmTtm_zOUMSUaaV-xbjAZVuCYEtOCMlL0E9jXgaxM78x5shcC8zkFy6-al58oPvP3mYixuLgaUTSF0-veoNlaBVF5qIebExgPwoPy2h6iW9zOh59f28IHUZRUjhN2igf7NgVwlKYy1EUAwQGFu2lfUlxhQrDljfCWJ3KwdpFLGFouKsxnrMVRGSB26nUWt8FZq_EIut7U3o1OQ7cIHaBIOmQMuWiiu13OLjdncrZzNKBFOS-FlMn6TZha_o2qnP7UP7HaYed2IPVP06wtdzFIHQc1MaJizrOu0AeAc_c0MoP6jTscWMw8Uxs1gUnHT8_FIjV01TC7Vb0hLWuy7gdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
اسپانیا یا پرتغال؟ انتخاب با توئه؛ تا از رقیب عقب نیافتادی از تیمت حمایت کن و پلی‌استیشن ببر!
🏆
👇
👇
👇
👇
🔗
همین حالا حمایتت رو از رونالدو یا یامال در لینک زیر اعلام کن و با بازی کردن پلی استیشن برنده شو!
👉
Https://tcup26.com
👉
Https://tcup26.com
📢
این پیام رو برای دوستات بفرست و به این چالش بزرگ دعوتشون کن!
🤩
@telewebionsport</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67400" target="_blank">📅 00:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67399">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/733e727650.mp4?token=P2JtOndQAcR7vFx6BgqBOCo3zk-YWTwziBh90xjcQ8afs6FPmuUhCe6b3nC8d86AzjyOMhxfjTahcguMaCZLtz2oUVO_LTodDwUhKerQ1U5j_POz1cDXLEQTaZXVSYylpNrwkedkTQJIXR3Bj-2Xi9YSuKotqe07Ja3bTWlgP7u42xkm94xw5Q7K0Tf-Uzv89RfZK3ieUj3PkTJhCi5tnr_4tNrM1WF9JHZwI4ineMQFDIC1kl5KxG_siVbGHR34zYPxYkgycTPtSfqxOL1SC4jvUfsRRSBlEq43gwbCf_KOwcEYKQq789dWxm-oNRo9AkUf0JnQ7yf9hHGrgFqTew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/733e727650.mp4?token=P2JtOndQAcR7vFx6BgqBOCo3zk-YWTwziBh90xjcQ8afs6FPmuUhCe6b3nC8d86AzjyOMhxfjTahcguMaCZLtz2oUVO_LTodDwUhKerQ1U5j_POz1cDXLEQTaZXVSYylpNrwkedkTQJIXR3Bj-2Xi9YSuKotqe07Ja3bTWlgP7u42xkm94xw5Q7K0Tf-Uzv89RfZK3ieUj3PkTJhCi5tnr_4tNrM1WF9JHZwI4ineMQFDIC1kl5KxG_siVbGHR34zYPxYkgycTPtSfqxOL1SC4jvUfsRRSBlEq43gwbCf_KOwcEYKQq789dWxm-oNRo9AkUf0JnQ7yf9hHGrgFqTew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
عجیب‌ترین چیزی که امروز میتونید ببینید:
نیسانی که با یک چرخ جلو بدون مشکل داره حرکت می‌کنه و سگی که داره راننده رو قانع می‌کنه تا دست از رفتار‌های کصخلانه خودش برداره
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67399" target="_blank">📅 23:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67398">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aad6611348.mp4?token=nIE_xATQ0TON17pvu43XJ9wBcjOMLjRARjXYMYH1yxTafPqJN18MC22zQWEMumklrBC7lFz8Ua4uO281z3BF_tECVr90NjRB9_7Q0fvwcwx96BJZQ0AwQDziPVAJ3yuh8qWOHg8KpSn0dSBKMM4YdFcKa_5jBDDG8Kz6LXeJVWl06FpBkok2hWzRDQMGRRnYoP8cdadt40Y13Al0W1PmOFoHQrFU0H52bm2Q9MysOaA3BYvmAq8ZnyMhI3wb1xNGvbFGu06eABQpxc62SIlb9up366vml3OfDuP7N6SlbfW0-stUDCzuSpf3GXYeoEYnImy5rtjsmq-fhnc4gpwLLzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aad6611348.mp4?token=nIE_xATQ0TON17pvu43XJ9wBcjOMLjRARjXYMYH1yxTafPqJN18MC22zQWEMumklrBC7lFz8Ua4uO281z3BF_tECVr90NjRB9_7Q0fvwcwx96BJZQ0AwQDziPVAJ3yuh8qWOHg8KpSn0dSBKMM4YdFcKa_5jBDDG8Kz6LXeJVWl06FpBkok2hWzRDQMGRRnYoP8cdadt40Y13Al0W1PmOFoHQrFU0H52bm2Q9MysOaA3BYvmAq8ZnyMhI3wb1xNGvbFGu06eABQpxc62SIlb9up366vml3OfDuP7N6SlbfW0-stUDCzuSpf3GXYeoEYnImy5rtjsmq-fhnc4gpwLLzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فحاشی وحید خزایی به خامنه ای
رادان کلاهتو بزار بالاتر!
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67398" target="_blank">📅 22:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67395">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CvK60NnMc1WeCqSQ0a6As4wOHzmmgiGwSbS7i63jUS95vt7JXwWXqgddTz8FGBsGKMuKpXx7jjCMIfEVkfNCgU1djxXIwnN0YDk4RF6VgNUpBeN0Q0S-vIXkIW2VlqadrraGtoftJjHfO_uLs9YQF3U7BWA54-9K5SwqXNA4tWHCyloZGmrW0YQgPzjmDHmSQ-Z-mqWczrjSJe0koCVscNodzZV0c2JqO8FkBoeGI3cYqFGZD8EY2TLijWOW_03khkjfLyD9iBHyDksSIsmqK02ue8GMq5qLhmmMwv4q6wRi-5qMd5zyb9Jx_2ZXUpYpi3nvF1t7ZVqQGbQHTpsZ1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nZO0fABu4fFJVmjmYp9EM-qv_7oPdxi8xFCEmGBwNnF6z-pmyjnWRFAzpBSGmcP9deFh5sVas0WxVm6x-omxdFJ4kyvA8F89zuIT-tghnHfgfn_EVvRhhKzPBX1nIenqsxGmARHKc12Ug6cCmvM00kEg5YZ7tY05R1SUsT2ncjj4Fzys7AVN1j0yKjqgRve6p40S8RE84hprsTPg5Iu_8VjkNMNxvpn0umTYxhLrY1etOoQXRyuZ6yeldlipma6YPRAKS3QJkM2qkILCXiaFagYfVefJC_m1YssWDcBeOD74jIHPRk1z-FSH3bVjxIVKgjf2Tep8ZPRZuwaf_BSXGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/886967cfe3.mp4?token=CADWoyJbDns4mjQ8ZbZ77bjCl_QenL8amEr4_Z35jXmybQNrdcDhqji47fVbZBOkv1ERI8lgOjqPAa73tTHGhOe_QAitn6nazEljTFWtPRqhnHz7SxjwoO5tNMLTTzoT-RmSyqd0q5pGiDK1qpZU4dWnNFEPoYFzgdXNDeZ8YuFJDZEJcdEmTRPiYruVaIReidHxDOMu6HhwEb340wNr3wqFAO434guuDGa7zBSN8UjqwYr_TIidP5e7UhhmARHeUGEw39v-yMOqy_SnzPX3Pcfm_aKZG2ZB3yXGvnhVG1DDn7Rl6ytt11fPP_cD-GK7jkyu2Xc8OzX3OizyBYs6CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/886967cfe3.mp4?token=CADWoyJbDns4mjQ8ZbZ77bjCl_QenL8amEr4_Z35jXmybQNrdcDhqji47fVbZBOkv1ERI8lgOjqPAa73tTHGhOe_QAitn6nazEljTFWtPRqhnHz7SxjwoO5tNMLTTzoT-RmSyqd0q5pGiDK1qpZU4dWnNFEPoYFzgdXNDeZ8YuFJDZEJcdEmTRPiYruVaIReidHxDOMu6HhwEb340wNr3wqFAO434guuDGa7zBSN8UjqwYr_TIidP5e7UhhmARHeUGEw39v-yMOqy_SnzPX3Pcfm_aKZG2ZB3yXGvnhVG1DDn7Rl6ytt11fPP_cD-GK7jkyu2Xc8OzX3OizyBYs6CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فیلم اول تصویر کوچکی از جمعیت یک میلیون و هفتصدهزار حجاج است که امسال برای حج به مکه رفته بودند
مقایسه کنید با:
🔴
فیلم دوم جمعیتی که روز شنبه ۱۳ تیرماه، با وجود واردات عوامل جیره‌خور نظام از ده‌ها کشور در مصلی جمع کرده‌اند
آن هم در تهران با جمعیت ۱۵ میلیون نفری!
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67395" target="_blank">📅 21:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67394">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1d208e49.mp4?token=pupcWDqAarNz2afeTdI_34LSxBN7t8tsX-uA9_rEU3ardpVc4utlXaTRc_vBcHN5aCReSozL290r4A5BuIApO-e9BSxIiu3Kq0Q8w3Rpguwt6pyqGjLmJePYiT6qphVdz0FAxh9uJJWr7bH-vgR03aibrLQPMyb8n6pbx2-izme2sBY8Ydl8UIcPMPEwVUxTxj4gO9FStik0XLSjvVJp49pcXyLPd8EpXRUdnHIDX689lvKBwsoZ4M-8xKyKBMH5Xm4ma1forLLNSP3gOSMG-kJtrcOZGDO4WwB2i7PD-6xmzqF0ExtCJ3gIM-ma2a_e6U1kYuYoPvQVeX8Vf0rOXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1d208e49.mp4?token=pupcWDqAarNz2afeTdI_34LSxBN7t8tsX-uA9_rEU3ardpVc4utlXaTRc_vBcHN5aCReSozL290r4A5BuIApO-e9BSxIiu3Kq0Q8w3Rpguwt6pyqGjLmJePYiT6qphVdz0FAxh9uJJWr7bH-vgR03aibrLQPMyb8n6pbx2-izme2sBY8Ydl8UIcPMPEwVUxTxj4gO9FStik0XLSjvVJp49pcXyLPd8EpXRUdnHIDX689lvKBwsoZ4M-8xKyKBMH5Xm4ma1forLLNSP3gOSMG-kJtrcOZGDO4WwB2i7PD-6xmzqF0ExtCJ3gIM-ma2a_e6U1kYuYoPvQVeX8Vf0rOXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره مقامات تهران:
ما بسیار خوب پیش می‌رویم.
می‌شنوم آنها میگویند که«بسیار خوب پیش می‌روند.» آن‌ها اصلاً خوب پیش نمی‌روند.
آن‌ها آن‌قدر شدیداً می‌خواهند که یک توافق انجام دهند. آن‌ها باید توافق درست را انجام دهند.
آن‌ها با بسیاری از چیزهایی که بسیاری از افراد گفتند با آن‌ها توافق نخواهند کرد، توافق کرده‌اند.
ما به یک روش یا روش دیگر پیروز می‌شویم: روش مهربانانه یا روش غیرمهربانانه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67394" target="_blank">📅 20:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67393">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e3a38b86.mp4?token=bNLCNwYFUpd1GKadWRc-tbBe9kZbOv9ZYcv4UTrfZN0XNcJIFBQtaL2OFDDFTtz4S035sEvJ57d5UnTE28_TI-xP1enlKJ3gN8yynF-Qa4FOFvKjxwivPWngAtZap-jMPgSiyeItFUPfn705pfQo17wAeh7iHy6beSxIMS_BoL5aYBCN5T_Ip27-YAMqf02hS-vnTXOh4nUnXhUALw3s742YSdfqlvBsgw6jFDOHQv5YsklC7d0TIlRm47yrVBOisfliZc5E7dmIOOG98MB0HhFL2F8ZGm1xXSHXeV8B6IAozpta4JVnN3efAyKphKwdX-Av01yqPlprmbWrIAfzqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e3a38b86.mp4?token=bNLCNwYFUpd1GKadWRc-tbBe9kZbOv9ZYcv4UTrfZN0XNcJIFBQtaL2OFDDFTtz4S035sEvJ57d5UnTE28_TI-xP1enlKJ3gN8yynF-Qa4FOFvKjxwivPWngAtZap-jMPgSiyeItFUPfn705pfQo17wAeh7iHy6beSxIMS_BoL5aYBCN5T_Ip27-YAMqf02hS-vnTXOh4nUnXhUALw3s742YSdfqlvBsgw6jFDOHQv5YsklC7d0TIlRm47yrVBOisfliZc5E7dmIOOG98MB0HhFL2F8ZGm1xXSHXeV8B6IAozpta4JVnN3efAyKphKwdX-Av01yqPlprmbWrIAfzqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سطح عقل عرزشی رو ببین
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67393" target="_blank">📅 20:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67390">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OXgEKvnPnZhTZMwCjbsrBRP9BjpxLfnMhYCbH9hzy352ZRgtsygYZIo9rC3BniuTQLsopNGUtR7nd6cGd-NFglX4qc8HkB2GVFmRu4-3SAkGiV80cSYN22FHcJOVMV2j4m0mP_srzwRoBjr5nv9vYyyPjsJU61Ehz4XcqkVMUY6GtogTsgrYO4SmnfCVjlIiDryumcyFbFZqLKuqFya-KC1OE6hnqCj0ZWtg8DKg1PiuXblMV8emrTRg-Lr-mFTySPIRmFcNsm2R0neFK3Hv4p__E9OAhYS7_YgmpnM672ARO6o1kfjyG7iEy23NgPHn7YcGz-IJffzkA5tPG9raLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qW2JhlJA1oP6ODQX-tZdsINsFv0dq5KroIaRIx8VT9MElaDEu5F-LpyzElQX0f4LATvfsXEMCWpdXl1dMUkKnTV-GlSG7iCv02VaBdZTsc3BSlNv2mQrvbR0VZVrYNAazv7_1jDdiCXSO_tnoymhQdK-7PoQUTaGl6nbcT5WPYjfuxECLgeMci8Rjkt8N6HnyfJbiJVbJ4_7-xdRdUF7hOiemeqGmmqsUGEsskXCpp49CgWsUJcflGAD_aVPRJ3fvjLOuVtzByaa72m8axdQJzVO0DzsQsrbllvNxbjAfPzSzbNwwihNTlXeE8NJklzbCK-8ICa3p-F9q38XwWp_gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bea0c04d9.mp4?token=Z6LAsedI3rDC5SnLSeqnEvL3P5e8KXeYNEogCRC1RiHrCeY_ZTD9B_TtRD-FR6LV_xL-FEm33wLkY6U5JpUVfY7Azfl3hg2i4AtE-TqYNd7O3avqdN2UCULPiYJ0TmT37ylAi2Ns-ZTwsiKfBeMXnk3M2hlbnjydQbsricaOUUSih573s46_EsRj_kg0NMvDNP9706OI71u07BasahvsVHsnYkDKswE7uKhLDaB2l5LA9ZLrHc-1IO_T4BE8CkOhuMd0hAaZP5yNHRds70VIfG0oyhiH1hkXD9DyIsfjxy1vZ52LJx0xOMgFsUV3CxAg_aN91nUIFOuZ_G13hks2FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bea0c04d9.mp4?token=Z6LAsedI3rDC5SnLSeqnEvL3P5e8KXeYNEogCRC1RiHrCeY_ZTD9B_TtRD-FR6LV_xL-FEm33wLkY6U5JpUVfY7Azfl3hg2i4AtE-TqYNd7O3avqdN2UCULPiYJ0TmT37ylAi2Ns-ZTwsiKfBeMXnk3M2hlbnjydQbsricaOUUSih573s46_EsRj_kg0NMvDNP9706OI71u07BasahvsVHsnYkDKswE7uKhLDaB2l5LA9ZLrHc-1IO_T4BE8CkOhuMd0hAaZP5yNHRds70VIfG0oyhiH1hkXD9DyIsfjxy1vZ52LJx0xOMgFsUV3CxAg_aN91nUIFOuZ_G13hks2FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
پهپادهای اوکراینی اوایل امروز به پالایشگاه نفت اومسک، بزرگترین پالایشگاه روسیه، حمله کردند.
این پالایشگاه در فاصله ۲۷۰۰ کیلومتری از خاک اوکراین واقع شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67390" target="_blank">📅 19:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67389">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee21b0d93c.mp4?token=cRFTt0hn1rfMPytM5DorVpaAz0vv7-6tFA4EnqGq3Ty4m96cVWwW9wUNO7MexO1rrL44DGzii4GcXW5nWAiATg7d5t7NyypwsiOmXTfTgPysVHP5tLi8gaL1Y9shbXvmdm4KDsPFT_w_YMajAjyh6PnVo0Mld7hXsXoG7wGoLuU0QnKSLZayW_uMQIN48ut14RmCOcsX3M6txjlaa5ILjBMj0Kfs1ZVYK7TxN_I59w3ykx-vBGLaR26qOjJjfDEip5nnN5o8hYpr7PMBZLdTpC2zFHlK-7P4wC1PMCL9DLHiAtiXHULbwXg3iZALX7J0bxujWKpqTzzTKRfJiGC8pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee21b0d93c.mp4?token=cRFTt0hn1rfMPytM5DorVpaAz0vv7-6tFA4EnqGq3Ty4m96cVWwW9wUNO7MexO1rrL44DGzii4GcXW5nWAiATg7d5t7NyypwsiOmXTfTgPysVHP5tLi8gaL1Y9shbXvmdm4KDsPFT_w_YMajAjyh6PnVo0Mld7hXsXoG7wGoLuU0QnKSLZayW_uMQIN48ut14RmCOcsX3M6txjlaa5ILjBMj0Kfs1ZVYK7TxN_I59w3ykx-vBGLaR26qOjJjfDEip5nnN5o8hYpr7PMBZLdTpC2zFHlK-7P4wC1PMCL9DLHiAtiXHULbwXg3iZALX7J0bxujWKpqTzzTKRfJiGC8pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ در مورد جنگ پهپادی:
چه کسی فکر می‌کرد که پهپادها به چنین عاملی تبدیل می‌شوند؟ آن‌ها ماشین‌های کشنده هستند. شگفت‌انگیز است. شما پشت درختی پنهان می‌شوید و آن می‌آید و شما را می‌گیرد. و من صحنه‌هایی را دیده‌ام که نمی‌خواهم ببینم و نمی‌خواهم شما هم ببینید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67389" target="_blank">📅 18:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67388">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02a06527a7.mp4?token=sIW_K6k6ci9n_owi7QQ53OKNnn_XzFz9Bibb87xAnGiy9SyFGBiYxySeOB09g-xRUthS5aO5225l_R8tSuZPbct3djWfbnmzdHO68ORJ8_duAKusCWy3ZF0B9KG0bnDT0CwdjbWRDQPNNSLIkQVzp2oVawCTYYFL5OCaLkVYbw6bVjgPLj_ZVfguUToHuu2lEBXJsgYXhlrWEx3ubwaYPI4VrI9SJtX_e7l0I-FiChTFvdlJCyfigxnAxJGHXEsnbUK6jxlMRYXoyr6h4tPtc1lEVPEq5nQaz246vcwnIoJnVIFwqbFXQylWIsaDdh9vXCGIgRNIcqOIiVIT0Jeo7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02a06527a7.mp4?token=sIW_K6k6ci9n_owi7QQ53OKNnn_XzFz9Bibb87xAnGiy9SyFGBiYxySeOB09g-xRUthS5aO5225l_R8tSuZPbct3djWfbnmzdHO68ORJ8_duAKusCWy3ZF0B9KG0bnDT0CwdjbWRDQPNNSLIkQVzp2oVawCTYYFL5OCaLkVYbw6bVjgPLj_ZVfguUToHuu2lEBXJsgYXhlrWEx3ubwaYPI4VrI9SJtX_e7l0I-FiChTFvdlJCyfigxnAxJGHXEsnbUK6jxlMRYXoyr6h4tPtc1lEVPEq5nQaz246vcwnIoJnVIFwqbFXQylWIsaDdh9vXCGIgRNIcqOIiVIT0Jeo7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ درباره کارت قرمز بالوگان:
من درخواست بازبینی کردم چون فکر نمی‌کردم این یک خطا باشد.
این یک نفر نبود که به صورت کسی مشت بزند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67388" target="_blank">📅 18:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67387">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e1e1775aa.mp4?token=r3skUbSH2vQviBgOhW2OkUrb2AKdJaCkchVVh5p9bAumSWrqaAf17lF5vV9EWW0qWlN2EmYLtVun4-uykguIcEps3Rj2Fw_qBuj5LFfGyVnFovE8gokaQESHnW1rAPOBBRnjlICyxPD2xI_T55yLTluF7UodRszKJwI_-P90sAl9SYwPWspMenpU1SQeMXcPIf-YWRRtp3I8uewlmz4vdf2_KPTAo3WXljcFiIe_00bMWkI2yuDDRzaop2quNE6RI7-fzn82Z-jzVsaZnS2E0fkZuCv1ZFW2X36zcRdw-sVpcJq7Zx6-jCoK-4gkXpG1mbT4Ez09J_7_wcB-HsQ7Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e1e1775aa.mp4?token=r3skUbSH2vQviBgOhW2OkUrb2AKdJaCkchVVh5p9bAumSWrqaAf17lF5vV9EWW0qWlN2EmYLtVun4-uykguIcEps3Rj2Fw_qBuj5LFfGyVnFovE8gokaQESHnW1rAPOBBRnjlICyxPD2xI_T55yLTluF7UodRszKJwI_-P90sAl9SYwPWspMenpU1SQeMXcPIf-YWRRtp3I8uewlmz4vdf2_KPTAo3WXljcFiIe_00bMWkI2yuDDRzaop2quNE6RI7-fzn82Z-jzVsaZnS2E0fkZuCv1ZFW2X36zcRdw-sVpcJq7Zx6-jCoK-4gkXpG1mbT4Ez09J_7_wcB-HsQ7Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ درباره بالوگان بازیکن تیم فوتبال آمریکا:
بالوگان بهترین بازیکن ماست. او کارت قرمز گرفت. من نمی‌دانستم این چه معنایی دارد، اما بعد شنیدم که به این معنی است که شما نمی‌توانید در بازی بعدی بازی کنید. این بسیار ناعادلانه است. چگونه او را برای بازی‌ای که هنوز بازی نشده است جریمه می‌کنید؟ من درخواست بازبینی توسط فیفا را دادم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67387" target="_blank">📅 18:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67386">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af665dba5e.mp4?token=ewG50ZMI3yQHZpcM3rNIpxiZ26xFcHyNwDWc4KbzBbv84Oez_2-HrF529L246akM1-m87cnuYZAA94fut2IMRakuqAJc9JwMJZXvDjRjFyfPhySPkb4n98xpV5CEvfZ_92o7d1IZ30Ns_sCXz-UVHYZ79mB2D2Xdxft0jk9gc41AyLadTA-WJyllvEG6GHyKSNaOKpRF-8FMBOsfZafhl5ng30mYtGkTm-gYSNxJBBK_qwxL2XuxkuxWwgOaMc-a9j8QNHY8PQyOwExoParaGPARbS6_KAODwkK3P5sQNL85nJ9gyUTZCGV6MLmMQ33N-eez5zPTHMRJ0Kc--sFK5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af665dba5e.mp4?token=ewG50ZMI3yQHZpcM3rNIpxiZ26xFcHyNwDWc4KbzBbv84Oez_2-HrF529L246akM1-m87cnuYZAA94fut2IMRakuqAJc9JwMJZXvDjRjFyfPhySPkb4n98xpV5CEvfZ_92o7d1IZ30Ns_sCXz-UVHYZ79mB2D2Xdxft0jk9gc41AyLadTA-WJyllvEG6GHyKSNaOKpRF-8FMBOsfZafhl5ng30mYtGkTm-gYSNxJBBK_qwxL2XuxkuxWwgOaMc-a9j8QNHY8PQyOwExoParaGPARbS6_KAODwkK3P5sQNL85nJ9gyUTZCGV6MLmMQ33N-eez5zPTHMRJ0Kc--sFK5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
یا قرار است توافق کنیم، یا قرار است کار را تمام کنیم، باشه؟ و تمام کردن کار سخت نخواهد بود. ترجیح می‌دهم توافق کنم چون نمی‌خواهم به ۹۱ میلیون نفر آسیب بزنم. می‌توانیم پل‌هایشان را در یک ساعت خراب کنیم. می‌توانیم تأمین انرژی آن‌ها را قطع کنیم، تمام آن کارخانه‌های بزرگ که ساخته‌اند، بزرگ، زیبا و مدرن. آن‌ها اکنون هیچ پولی ندارند. ما به آن‌ها پولی نداده‌ایم. می‌توانیم کارخانه‌های تولید برق آن‌ها را، به قول من، در بخش کوچکی از یک بعدازظهر از کار بیندازیم. هر کارخانه‌ای از بین خواهد رفت و آن‌ها این را می‌دانند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67386" target="_blank">📅 18:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67385">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f387513a36.mp4?token=IDnEmP1e895LY7-vEZ014RIziHnjwBncGlpqjzF49pGdwlNucfBA8OUAZrWmWzBX27x7sOGWHrgNHpM5yKuMWvX1eGKrXdzb3SC6P4Ag9OSdrvHpUiHpew-ck01uHs5S4xBZh3vyuwkPGW4BMJQo04RUE00A1qwW-pjwt1ve-3xuw0WRHiNF4Cwkv0-n8zaP1qRrlMok2zVedgJnNMI_fjPxMDItqzTFlSGHr9BqRg4kLtos98QropW4lvirAtiqVQj83qxL1wvj9RcQsFMgiDM-il-2Z3TRLXWFi5cN3PjuHsQHkE6UuGz49rKcok8qaWihwQk5_WDkhHZ50RyJaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f387513a36.mp4?token=IDnEmP1e895LY7-vEZ014RIziHnjwBncGlpqjzF49pGdwlNucfBA8OUAZrWmWzBX27x7sOGWHrgNHpM5yKuMWvX1eGKrXdzb3SC6P4Ag9OSdrvHpUiHpew-ck01uHs5S4xBZh3vyuwkPGW4BMJQo04RUE00A1qwW-pjwt1ve-3xuw0WRHiNF4Cwkv0-n8zaP1qRrlMok2zVedgJnNMI_fjPxMDItqzTFlSGHr9BqRg4kLtos98QropW4lvirAtiqVQj83qxL1wvj9RcQsFMgiDM-il-2Z3TRLXWFi5cN3PjuHsQHkE6UuGz49rKcok8qaWihwQk5_WDkhHZ50RyJaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
تنگه هرمزِ معروف؛ هیچ‌کس تا حالا اسمش را نشنیده بود، اما عجب ماشین پول‌سازی است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67385" target="_blank">📅 18:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67384">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b6983cd6.mp4?token=AnCgISqbuhNfy3Wg-zVhrmnuvhLD_7-rn4C51cMCxQiH26n0qP_aVmQTJXW3-bg035gg_jTIh0ngPrIETPvk5r1fDOmwVAyMb6xlGcFHrQmITln7zwPs9zNklmDfbAxGlBnBvVd0zI35tgyoeGPwiKUi0pL-UTyd2rC76wpUJTxIzG9yxteKpXMtlULGvT3AcBSjndxM98IJE5z-iAzINcg5tGfrX2LNJ3B6giuIgb_pALwg9WbuFI_c6WDwFZ2p1Ajs_BihCr5ltQqfydRAIxc7uPGEq9jI5ykdTpfH0VkqhOo_OPOMrB7fcM02zY-ML9FrERbE4PeWtYm_AYz_Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b6983cd6.mp4?token=AnCgISqbuhNfy3Wg-zVhrmnuvhLD_7-rn4C51cMCxQiH26n0qP_aVmQTJXW3-bg035gg_jTIh0ngPrIETPvk5r1fDOmwVAyMb6xlGcFHrQmITln7zwPs9zNklmDfbAxGlBnBvVd0zI35tgyoeGPwiKUi0pL-UTyd2rC76wpUJTxIzG9yxteKpXMtlULGvT3AcBSjndxM98IJE5z-iAzINcg5tGfrX2LNJ3B6giuIgb_pALwg9WbuFI_c6WDwFZ2p1Ajs_BihCr5ltQqfydRAIxc7uPGEq9jI5ykdTpfH0VkqhOo_OPOMrB7fcM02zY-ML9FrERbE4PeWtYm_AYz_Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
به یک دلیل وارد شدم: ایران نمی‌تواند سلاح هسته‌ای داشته باشد.
من به دنبال تغییر رژیم نیستم، اگرچه این تغییر رژیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67384" target="_blank">📅 18:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67383">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d6c7e39a.mp4?token=dEP7JZzPV1E65TM9PKrRiqZUEfanKUJgvvi-ei3IoP8h2qFeJyBTOYBPaFXQu7RZq9ecUSLa6SDC2-vIqN1i4ezZmdDyWypj8y-kn-As7xDBnAmhuBlDG4AJHtTFE-ed074MZ3jQSJs9jWIP_y4-OlNgk-g2yh3fwcr_vBnErqXf64d_u6DwbSXSY81ASQGnay3zcrbJxXcnbNNbZ5jcQFupp0heYE_-rMbJlzhrbRgw8kY3WL7gSQYm3VebKY7yigQN6hSuF8sZVfxrSpTTWVKAW1KQHgtNPCrcsW_j0FhG3C-D9K7SaJyMEaQmBO9Obve3IfGYEZ7zDNjyMLaDew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d6c7e39a.mp4?token=dEP7JZzPV1E65TM9PKrRiqZUEfanKUJgvvi-ei3IoP8h2qFeJyBTOYBPaFXQu7RZq9ecUSLa6SDC2-vIqN1i4ezZmdDyWypj8y-kn-As7xDBnAmhuBlDG4AJHtTFE-ed074MZ3jQSJs9jWIP_y4-OlNgk-g2yh3fwcr_vBnErqXf64d_u6DwbSXSY81ASQGnay3zcrbJxXcnbNNbZ5jcQFupp0heYE_-rMbJlzhrbRgw8kY3WL7gSQYm3VebKY7yigQN6hSuF8sZVfxrSpTTWVKAW1KQHgtNPCrcsW_j0FhG3C-D9K7SaJyMEaQmBO9Obve3IfGYEZ7zDNjyMLaDew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
مقایسه اجرای سحر امامی، مجری تلویزیون جمهوری اسلامی، بعد از مرگ علی خامنه‌ای (10 تیر 1405)
و اجرای ری چون‌هی، مجری تلویزیون کره شمالی، بعد از مرگ کیم جونگ ایل (28 آذر1390)
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67383" target="_blank">📅 17:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67382">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3237168e66.mp4?token=ckHmcgN23AzVuNwhdgPnsPc_u0LSil7Q8GI-wt7qtu-2cVgP8sHSgKE5j8CvCloRhF6KL29ocyao325EDoziCTILFkgIGoRtfbxYm9pgD3QTQ3fPuxh7lM1VA3h7wMEXWBqAZMKuqakQtAq7ns-lmtn9vPBbx9cyi0viG9SX1pON-nBhGKzlZYhkp2o4tJbuEH0_kr64pehXqAdTi9h-sNOZxS2e-Siv5S8CSjmEzn2R5yuYShvzxcXKVR61L4TzVx7dcMHGS1tmOjjT-02mP0oOrbWMV8MDhCU1N_VCD96ecGxsDn_VMGKPF46CnouevtkWD-KJBRC5OUPl3wiIVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3237168e66.mp4?token=ckHmcgN23AzVuNwhdgPnsPc_u0LSil7Q8GI-wt7qtu-2cVgP8sHSgKE5j8CvCloRhF6KL29ocyao325EDoziCTILFkgIGoRtfbxYm9pgD3QTQ3fPuxh7lM1VA3h7wMEXWBqAZMKuqakQtAq7ns-lmtn9vPBbx9cyi0viG9SX1pON-nBhGKzlZYhkp2o4tJbuEH0_kr64pehXqAdTi9h-sNOZxS2e-Siv5S8CSjmEzn2R5yuYShvzxcXKVR61L4TzVx7dcMHGS1tmOjjT-02mP0oOrbWMV8MDhCU1N_VCD96ecGxsDn_VMGKPF46CnouevtkWD-KJBRC5OUPl3wiIVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
مارکو روبیو: سوسیال دموکراسی همان کمونیسم با ظاهری آراسته است.
مارکو روبیو، وزیر خارجه آمریکا، با انتقاد از سوسیالیسم و کمونیسم گفت تنها کسانی که کمونیسم را از نزدیک تجربه کرده‌اند، درک می‌کنند که سوسیال دموکراسی در واقع همان کمونیسم با ظاهری آراسته است و پشت این ظاهر، همان ایدئولوژی خطرناک و ویرانگر کمونیسم قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67382" target="_blank">📅 17:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67381">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54408a1a4b.mp4?token=tFzmXJa0jMUQROTTTBkt2Qsb-sEO36x0C_y0iTexfqBF7B8n4qoSgD6H3Hs4X5mOlsV8vD_JUAexcqaigI04xATw7L-62pnrvkj42uSJLYAelwhIdPaLvj9KQdvIwdXv4A1WuF4B_SlNtKug5pvgTlCwckhsapsCFpJekOso4VN7ulbkie-wgjBTCmH1daEKSarrE3Dewtg0VJRt2w5eRcfjt60EakMbWEM6QUqdP2GFqllgh7QPLYr4_cbprUEKrmYGToN82nDFKqFEEHeoV9N40Ddot74uz2qnEdiCdvj2bR6p_rbS3wOg1goxC_B-WdOi2ZcA_SQggtKG211bwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54408a1a4b.mp4?token=tFzmXJa0jMUQROTTTBkt2Qsb-sEO36x0C_y0iTexfqBF7B8n4qoSgD6H3Hs4X5mOlsV8vD_JUAexcqaigI04xATw7L-62pnrvkj42uSJLYAelwhIdPaLvj9KQdvIwdXv4A1WuF4B_SlNtKug5pvgTlCwckhsapsCFpJekOso4VN7ulbkie-wgjBTCmH1daEKSarrE3Dewtg0VJRt2w5eRcfjt60EakMbWEM6QUqdP2GFqllgh7QPLYr4_cbprUEKrmYGToN82nDFKqFEEHeoV9N40Ddot74uz2qnEdiCdvj2bR6p_rbS3wOg1goxC_B-WdOi2ZcA_SQggtKG211bwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در برنامه ای در صداوسیما حدود بیست دقیقه کارشناس برنامه اسامی سران و مقامات جمهوری اسلامی که توسط آمریکا و اسرائیل ترور شدن رو خوند
بعدش مجری به کارشناس گیر داد که الان بیست دقیقه وقت برنامه رو گرفتی که اینها رو لیست کنید و در ادامه میگه به جای اینکه به مسولان و مردم دلگرمی بدی داری دلشون رو خالی می‌کنی.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67381" target="_blank">📅 16:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67380">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84629e4c7d.mp4?token=XKV0Hm7M-uBQFVy3hQ_j7T0A2MCj9zsQtJUmIVIv4VRSTY0H7OpKKlFd3kSrGcbyuGyxEt6cAi8DII8rOgzeP_Z_3_Re20Pbp7DUDtgY0STrUhdGJcby3xsZ1PfAeZx4x47iaCd67jS7YvdJF-MnbWQfDsmryF7eR5DhR17m3QkKK_N8FWx6Sz5jwGIIaZTkk4btkphHYe9mVNN6lucxiUe85wtf_B7p5pxGc9NayAj6X9JUBDoLfNxqZgfxT63G5O53ykkZjLZapwTOF9bJ6pQj615rcioYKm6KAw1CECI5QfolzGvL2qntCntjW8BdGBRwDMsLzvkABauN6oYUAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84629e4c7d.mp4?token=XKV0Hm7M-uBQFVy3hQ_j7T0A2MCj9zsQtJUmIVIv4VRSTY0H7OpKKlFd3kSrGcbyuGyxEt6cAi8DII8rOgzeP_Z_3_Re20Pbp7DUDtgY0STrUhdGJcby3xsZ1PfAeZx4x47iaCd67jS7YvdJF-MnbWQfDsmryF7eR5DhR17m3QkKK_N8FWx6Sz5jwGIIaZTkk4btkphHYe9mVNN6lucxiUe85wtf_B7p5pxGc9NayAj6X9JUBDoLfNxqZgfxT63G5O53ykkZjLZapwTOF9bJ6pQj615rcioYKm6KAw1CECI5QfolzGvL2qntCntjW8BdGBRwDMsLzvkABauN6oYUAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو در گفتگو با فاکس نیوز:
ایران کشوری با حدود ۹۰ میلیون نفر جمعیت است و حدود ۸۰ درصد مردم آن از این رژیم متنفرند. اقلیتی که شعار «مرگ بر ترامپ» و البته «مرگ بر من» سر می‌دهند نماینده مردم ایران نیستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67380" target="_blank">📅 16:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67379">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336146a8b7.mp4?token=Cg8uhlWBYYqghOzuohnSstWHFWHeiggqSXL8sSqiHc07PZiDf-lgl8mMtEAk9JnwiqCp42flibo-FPa7cDtmRXp-NH1cn66SPADAdrkqREmQ3Qp4TUGAjBKXXBwoGX0TxT59K3k-onk1pTn83AQYt-Fg14V0cheRjuQnzrVUS1NPe81RdyK9bE9cA7g2kyiOblGkGptv10Pa__mP31kqYT7Oq5ImxG9Kb62LMmVQR51lssKTOHVsm5d8-FXDK_llCucd5qONp7IUeZwebiK29qQVznSxh5HIKqmFXMIoFTCBbFot58S64ocVTGIzAbDXhHyOlpFrV0w-hfPjKo9Qng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336146a8b7.mp4?token=Cg8uhlWBYYqghOzuohnSstWHFWHeiggqSXL8sSqiHc07PZiDf-lgl8mMtEAk9JnwiqCp42flibo-FPa7cDtmRXp-NH1cn66SPADAdrkqREmQ3Qp4TUGAjBKXXBwoGX0TxT59K3k-onk1pTn83AQYt-Fg14V0cheRjuQnzrVUS1NPe81RdyK9bE9cA7g2kyiOblGkGptv10Pa__mP31kqYT7Oq5ImxG9Kb62LMmVQR51lssKTOHVsm5d8-FXDK_llCucd5qONp7IUeZwebiK29qQVznSxh5HIKqmFXMIoFTCBbFot58S64ocVTGIzAbDXhHyOlpFrV0w-hfPjKo9Qng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مجری:چرا آن دولت هنوز در ایران پابرجاست؟
🔴
نتانیاهو: زیرا چند صد هزار مزدور دارد که در روشنایی روز می‌کشند و قتل‌عام می‌کنند و در شب مردم خودشان را می‌کشند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67379" target="_blank">📅 15:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67378">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4W-oYzTsQLfTGh6D7EvCjd8-oOIHxkD6cH8uzEbAKOpT4RwPqe6JkxurWtkdKycy7Ui9Z_-79GnGTgDtMBaLhqzocGOJBt90TRQ4gnZ1R9Qtc8NbAU_w_q09iY4rzJEabp51dCTbje0WHNwe3eZHk2M3fh4WSjOt9575JTd02Uh-j2XfEMLn0zJgZB7jFWflfeUODus5YQa-j0rVMqvqs0MJw3f0gwWSLE0dont82VjIlYUVhgHvKtp-rmD0xa87HDxEPsvWiw_eBeIS9JEgA5_unvKlOglaUJPv5jE_ACMn8oJZKOUKPSPRHxGUx4WPyhD9Hj3l7Vbkabg-Ig6cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
واسه کشتن نتانیاهو وترامپ 100 قطعه زمین 2000 متری جایزه گذاشتن،آیدی رو هم زدن اون پایین و گفتن انجام دادید پیام بدید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67378" target="_blank">📅 15:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67377">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VF5iPxRwXe0NKoN-j-q2rTsNbwwUXz5_FhxpQdyGNpxBPbrzW9svpsRlEu3wM7kr9-NTYH2l9L3jIXimQimIJ1zEZJ7RAptTMsB15qt_dyZwyBJBjuF5XsKalK9D6AAByQ227XGnoN7fWiWR9JzOcRvHNtNECQxRIC2dw6XOX3KOqAPQLAOMT5SfeS3Uiqth4Z2gYrTUVJ_HHzu_OP3_2XRVEDFbcYAPYK1GPsvtL5SZP1n906x8ILuId7x2t9hFok51qKmOF2QmznTHNqEvsEP5BYroq8Pmy1XKjrG0AhcebUFeKO4qb5YczvrVcRdDZTwjIOCUdpf5s5bZU9CjrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دو حمله پهپادی هدفمند اسرائیل در جنوب لبنان.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67377" target="_blank">📅 14:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67376">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_OROSqVgomyCI2TIAnse-2W6nivU53UGKKeh3wKU0KQhoj92pb0Ls10SjPei4wV7WuRZQS1EAg-QDNWXRZvMEKqmwcxyOsPTLbkGSQRAfEHbUeMVY13uvUyr0oFoxUjsSgpP8wFPRRA7cBSSkKOP6kV0TsElFtciFTlBFEJQAkUK8GImWEQeeA7Xi7asG5QC_0kLggUPrIpTByYGvA1wTTVQiYDTkMj8doaMQaNiufbW6Evg_hkBNVlR84c7UQ92zhFBymYyMT43bCxuiMB1ODfcoauDB-my9hiZcHttamIeMudKOuTn3qrYkm7bzJl2n851yVg5XZ8vpfErX4vOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏شبکه ۱۴ اسرائیل :
سپاه قدس واحد جدیدی به نام « یگان مختار» تشکیل داده است که با کارتل های مواد مخدر مکزیکی و آمریکایی و همچنین ایرانیان خارج از کشور برای ترور ترامپ و ژنرال های آمریکایی همکاری می‌ کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67376" target="_blank">📅 14:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67375">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3IjJ5ZmVpISs4m878NwbSt0mOBObFvMsVDRHABnFwoMZqXSrsx_kJpR1uM7VmNTAkn7JjNltKjmVAtS-zvMATUvVKyTcWd-CdDQa2flXNvrv4JE2OKOOXJ2bUEBpGZtpUMpLIT98Mo-6GuBmFW3xFjUl-FogU2aE2J3_-t1sRmmzljDAnu1G3XWW3PIq2exPdDvQfVYYAUTL16_GklXOAGzacKxWCoH6mVx-fDTzSO0PGhn8OLgz0QxV1fVjhpi-usMf_Vc-bQ5fimfO4kq4GrBpSft5GiACEtZYibW3mZLUy5iVCc3E7kaKYirMBq-Psc4xPNzeoMpv6sEtem8hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یک بنر در مراسم:
دونالد، نابودت می‌کنیم! از توجه شما به این موضوع سپاسگزاریم!
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67375" target="_blank">📅 13:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67374">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3JbiWnNBIlIHhGiu_OArxQVv26Ysh0s1SylFdIN2E6vB5vTtdc3yKz3tbgIVg-Il0OmoNhZ767HEUuPEDPVKST4n2rt9yNddhzByPcb4-NlJYHtp1J0xPJIdw0XNeKUUx7dTSe58RpmJTUR-u4YZmG3rsh1baGP3AFEPCT7WNnhTYgunBIsvQu-WzW76P2GZ9SIDRmo5HjgwBN7JSujW1StZM_FtGqOb9AJ4dYseaa4N1gmQp50-DIz5_8DSnxHyy3ifW0uqmYxAM0_oNsh84DetmATC6QynjALSCcCH_BTpk9HEdk7BnwQDpiEN5z0iJP1zqA_CzYAQRWwLc4Oaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
ادعای
نجاح محمد علی کارشناس عراقی مسائل خاورمیانه و از حامیان نظام جمهوری اسلامی:
در مراسم تشییع امام سید خامنه‌ای رضوان‌الله‌علیه در تهران، فرزند ایشان، بقیةُالسَّیف، آیت‌الله سید مجتبی نیز حضور داشت. او پنهان نشده بود، بلکه در جایگاهی قرار گرفته بود که کمتر به چشم می‌آمد.
هماهنگی بسیار خوبی با نیروهای ویژهٔ امنیتی و فرماندهان ارشد سپاه پاسداران انجام شده بود…
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67374" target="_blank">📅 13:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67373">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ryxOt2wp5xbM5pMnw0K4DTpZvYaX0Cl0mBYsBptXdvvVoCsCDysCXcHJ5WXqNzEwakZoKGWH7KYRImjqLqLANybKsW8odVFKMe6JS2JqFdQdOo7jkDnVgu6ScruvjTwZdzY-PsbJqRz6P1oTZadSt7OqbJ7_NzoJhgsmMW9SbwwogboBeMKzLOIbD08-IXdSeG-LQ8o78JL85IohoSrce2a3wsZGOnuFrCnZSJ8GvAM4Qby00NKpHO9I6RFggAkKU9IjdRguGOS1Ddjzegoivz81mrk8Qh3i_An73m2iXj-uCwqaAX87G8RJuzZcC3LSvt2RqJPg4meDraROPZeSNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
«آیت‌الله خامنه‌ای که مراسم خاکسپاری‌اش هم‌اکنون در حال برگزاری است، توسط اسرائیل حذف شد. هر رهبر ایرانی دیگری که برای پیشبرد طرح‌های نابودی اسرائیل تلاش کند و اسرائیل را تهدید کند نیز حذف خواهد شد.»
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67373" target="_blank">📅 12:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67372">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22aca7392a.mp4?token=YVTRfHfaTEqTPwcHuXCjNzYysr5LkzyXDj9Af04R8_KFY-gNIxI89dMkLzzXi7wilXUN0CL4tOYn7ZxkQghrvpbwob8m2ZGtHyBd6Gy7zFQ0tvXkeNavoeQDQUc2uXdx6icd1gYhZFiKA_mCE2ioOexKskWXxvSiW3R1y6Xrbu9xOu0DxmmB3WOcU0FDBhcT5yVquNSkdivEjE492u679Xh9yCenpQ313EhplYuk7YOYsijLO5UAl36L0XSJEGmo_BWJr3xlSPBtDuGrCrHPNOq9sLWFsIjLuL3SIFnk4YEqYJ3j9hgvw_6Gy7MePzEqbadQvhDJYtisL3UB05Pz0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22aca7392a.mp4?token=YVTRfHfaTEqTPwcHuXCjNzYysr5LkzyXDj9Af04R8_KFY-gNIxI89dMkLzzXi7wilXUN0CL4tOYn7ZxkQghrvpbwob8m2ZGtHyBd6Gy7zFQ0tvXkeNavoeQDQUc2uXdx6icd1gYhZFiKA_mCE2ioOexKskWXxvSiW3R1y6Xrbu9xOu0DxmmB3WOcU0FDBhcT5yVquNSkdivEjE492u679Xh9yCenpQ313EhplYuk7YOYsijLO5UAl36L0XSJEGmo_BWJr3xlSPBtDuGrCrHPNOq9sLWFsIjLuL3SIFnk4YEqYJ3j9hgvw_6Gy7MePzEqbadQvhDJYtisL3UB05Pz0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حضور احمد جنتی در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67372" target="_blank">📅 12:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67371">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ad63d7f30.mp4?token=DlDPJ-P4057y86Y12xUfTORk4wmo-70fal-N_yC9GVyMytdvpYBYPGsZuw76b0sDn6uJjyn4cK6_tUQA729y0X7dmlNnalDQtinuDNdmZxgt48lnDxpgNJWC-h8bozIqEIlvy0-9V88Y-kl-ivqBtJ1-nSM9bUdkIjuhp4CY1LLpVDmu4dhaKGZHamKG_EzoIA8lvyFhW0j1gBUBSbnMSVEg_Kh_RuJKsUsToZLT9bTh2If_awEcn4-Gf2JFwBBvBLkQgeaZnjLtl8f0LuaWijFRSm7BZFJKp31tiqlnBjkRdxwQMTqVxHXxQZ3idwUzM1KSdJe_Qc2JIqeLFYOLPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ad63d7f30.mp4?token=DlDPJ-P4057y86Y12xUfTORk4wmo-70fal-N_yC9GVyMytdvpYBYPGsZuw76b0sDn6uJjyn4cK6_tUQA729y0X7dmlNnalDQtinuDNdmZxgt48lnDxpgNJWC-h8bozIqEIlvy0-9V88Y-kl-ivqBtJ1-nSM9bUdkIjuhp4CY1LLpVDmu4dhaKGZHamKG_EzoIA8lvyFhW0j1gBUBSbnMSVEg_Kh_RuJKsUsToZLT9bTh2If_awEcn4-Gf2JFwBBvBLkQgeaZnjLtl8f0LuaWijFRSm7BZFJKp31tiqlnBjkRdxwQMTqVxHXxQZ3idwUzM1KSdJe_Qc2JIqeLFYOLPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیوی عجیب منتشر شده از وحید خزایی شاخ اینستاگرام با سردار رادان که میگه کار دارم با وطن فروشای لاشی،ترامپ گفته گوه خوردم
من سلطان دختربازی ایرانم ،حتی سردارچندبارمچ منو روی کار بادخترخالم گرفت ! اماخداشاهده آنقدرمهربونه،هیچ کاری باهام نداشت و ولم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67371" target="_blank">📅 12:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67370">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a17dafc375.mp4?token=TkyNXTGRRVdLpeP36dYBPQd_pKZuBsJ-VUWaZiFJYszMy-vDb3iAlSQIBPOGW8NHgrBE30pMTHOhH_dYIdIrUPxpHPhNfBytN271GYw-izQcNdcvMXrCVIbRUqF--ONi9zK3YHI5C1kvHE-E-QfaNHEcgopU27n1DCh3sKSx293me7IkKZ8DFQvkEjXUKl60ONkViXDR0_5Z58TdqjHPZRF87KfqLo9zA-GRru8_uf9o_SpfzjQCsyelthmIVISCyz7RZ9g_htaHTGXn1VLDxfRWW3S9I55SNZ9eBjiB6yB6ml8JB5u-2RLHEH2BCGKxOxj7tSMc897Q3o6VITK3eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a17dafc375.mp4?token=TkyNXTGRRVdLpeP36dYBPQd_pKZuBsJ-VUWaZiFJYszMy-vDb3iAlSQIBPOGW8NHgrBE30pMTHOhH_dYIdIrUPxpHPhNfBytN271GYw-izQcNdcvMXrCVIbRUqF--ONi9zK3YHI5C1kvHE-E-QfaNHEcgopU27n1DCh3sKSx293me7IkKZ8DFQvkEjXUKl60ONkViXDR0_5Z58TdqjHPZRF87KfqLo9zA-GRru8_uf9o_SpfzjQCsyelthmIVISCyz7RZ9g_htaHTGXn1VLDxfRWW3S9I55SNZ9eBjiB6yB6ml8JB5u-2RLHEH2BCGKxOxj7tSMc897Q3o6VITK3eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وحیدی فرمانده کل سپاه با موتور اومده مراسم
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67370" target="_blank">📅 11:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67369">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abfc46c7e6.mp4?token=tR4OqhwAueqWHqkJcg_MtGMjScMHmj61whaGti97s4hLIsTHn3DjrXD2Dp43gmsJLm0KD-99iG9J1tcm3ejmhIzmgHatpm0HGqdjdutTlp1FAn9imCh-2TKeSAgZpqpLVXC1MrJaU_Lk3YRlmaNQKt--tMsKeemy_M1t_4CFlpesnZxu-83MY7-D8yuUftkiQknxV3hCKx0xbmtJHmyaq093tkkRHQU6wuYxY0MJ6is2amWkCWgLsfdkCBbBR382Sd_5KGYnGlYPKR01PfD4onafWmtOiFvFP6HuztPFnRulNcFt1PGa5jhuknCDNtjxzA_nVsYSgnNYRs6wYmpKJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abfc46c7e6.mp4?token=tR4OqhwAueqWHqkJcg_MtGMjScMHmj61whaGti97s4hLIsTHn3DjrXD2Dp43gmsJLm0KD-99iG9J1tcm3ejmhIzmgHatpm0HGqdjdutTlp1FAn9imCh-2TKeSAgZpqpLVXC1MrJaU_Lk3YRlmaNQKt--tMsKeemy_M1t_4CFlpesnZxu-83MY7-D8yuUftkiQknxV3hCKx0xbmtJHmyaq093tkkRHQU6wuYxY0MJ6is2amWkCWgLsfdkCBbBR382Sd_5KGYnGlYPKR01PfD4onafWmtOiFvFP6HuztPFnRulNcFt1PGa5jhuknCDNtjxzA_nVsYSgnNYRs6wYmpKJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عباس موزون، مجری صداوسیما:
چند بار [روح علی خامنه‌ای] از بدنش جدا شده بود و تا ارتفاعی بالا رفته بود.
«اصلا بعید نیست آنهایی که علیه بشریت عمل می‌کنند، از نیروهای شیطانی کمک گرفته باشند.»
چی میگه این
😢
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67369" target="_blank">📅 11:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67368">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MN49gMU3cyJuwgHjVAQXDDhBj2UTZGn09u599Zv9IRlAKwNkGyjjR9SJJMM33vz-_DqZxwCGKnlDOKJyGQD0oKCktyEHIPtrkZ2aRHpZhNSmsnbCg-BTDM9JtZCIh6esGBda3SG1QaTnkTfJdv57xXsyrxx9ZGJI1jp4mY7lZ3ypSRANBnb6MjC-BGUK3BY5r6Ql2zwht1ElUbL71oXXmGMk4Ezn32jHTSKRhIsbukfUz4VxsEYq-Ovc6uZhzWEsLbaf5d9-a_RmHzvxyjSrNYiJ5KGWXY-VoW4-8W4vDAjbOmsD_lg458kwJ59n63SRNL3cFRVdy6G6pbktxiaKew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اکبر هاشمی رفسنجانی،24 اردیبهشت 1370:
سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67368" target="_blank">📅 10:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67367">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38c47b7b97.mp4?token=kuDTBpkjmId0jUq69Z7U6NA9_EaDsSIw74LUvChRPvTTOHkS31dPvDmyiHrfB5r3xn6IeVTzAJqauPcZvY-c9DeMWgqi095bxQmHicOZpQfJOte1D3auzlAPEcvgZBGEFCQ0cki3Xv81MtmE145FHAcTwa-PAOh1XM2fiKzOSkwQIzOjNcUKu7MTm6v7Iz-d5j8WFA4VlHWcpqEIbsfz8xXhfLGaSUVKmvZsbfEpDF83k5i2G4pBTRoIgnwjq4K3xhW2Ctvpmh4uQmldFS3-xYledC8CP5kMEEntj_UhUHB3DgvTxG8W6IgnbQsMepa10fc47hkhpk7-YbiLtiemKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38c47b7b97.mp4?token=kuDTBpkjmId0jUq69Z7U6NA9_EaDsSIw74LUvChRPvTTOHkS31dPvDmyiHrfB5r3xn6IeVTzAJqauPcZvY-c9DeMWgqi095bxQmHicOZpQfJOte1D3auzlAPEcvgZBGEFCQ0cki3Xv81MtmE145FHAcTwa-PAOh1XM2fiKzOSkwQIzOjNcUKu7MTm6v7Iz-d5j8WFA4VlHWcpqEIbsfz8xXhfLGaSUVKmvZsbfEpDF83k5i2G4pBTRoIgnwjq4K3xhW2Ctvpmh4uQmldFS3-xYledC8CP5kMEEntj_UhUHB3DgvTxG8W6IgnbQsMepa10fc47hkhpk7-YbiLtiemKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان:
خرافات پدر ایران رو در آورده.
آینده ایران در یک جمله است؛رنسانس.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67367" target="_blank">📅 10:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67366">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33573d06e9.mp4?token=d0DM-GnFeJmqU0QkG0RMq0Gk3q-xOfOZdt-D5X8wuI9cLTFABaF0HWuMlhr44LrHVCpBD28OoRUhjOFKLk6Zv_OtCYXNjb1Ds2q1rOXYulUFhY-joMMHIF4hpzS8AgkUfbFJXAfY0XWxlEMpUdFa0MfY5rRT5EoVtqg2-UtpWqgCZt6iNyU23Ixd4akULRYhE9xIPNyKszJORmLL9N-hmC3CJJHEF2o0_R6L7B2TaJVsOU2O2GzO2vrDZbkUbFsssq6bPaq_hIpC9lkVfG2lc42udXteO8MptcNRNsD5wY8bg0LPNXEpW3O9JtPM1-1Wu3en3eKq05p3SNa_B6pBbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33573d06e9.mp4?token=d0DM-GnFeJmqU0QkG0RMq0Gk3q-xOfOZdt-D5X8wuI9cLTFABaF0HWuMlhr44LrHVCpBD28OoRUhjOFKLk6Zv_OtCYXNjb1Ds2q1rOXYulUFhY-joMMHIF4hpzS8AgkUfbFJXAfY0XWxlEMpUdFa0MfY5rRT5EoVtqg2-UtpWqgCZt6iNyU23Ixd4akULRYhE9xIPNyKszJORmLL9N-hmC3CJJHEF2o0_R6L7B2TaJVsOU2O2GzO2vrDZbkUbFsssq6bPaq_hIpC9lkVfG2lc42udXteO8MptcNRNsD5wY8bg0LPNXEpW3O9JtPM1-1Wu3en3eKq05p3SNa_B6pBbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو مراسم وداع با جنازه علی خامنه‌ای، وقتی نوه‌های خمینی میرن جلوی تابوت سید علی خامنه ای، قاری این آیه از سوره نساء رو به کنایه می‌خونه:
آن گروه از مؤمنانی که بدون بیماری جسمی در خانه نشسته‌ان، با مجاهدانی که در راه خدا با اموال و جان‌هایشان جهاد کردند، برابر نیستند.
اونا هم برمی‌خوره بهشون وسط آیه ول میکنن میرن.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67366" target="_blank">📅 09:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67365">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BlwynubbNSE1zuGS8jjL9Ln5PidtfdIzKwrPT1T8ANVIgc8xF5YYPr5Wsd7FAOyv8H2HD-OYQ-2QgEgHblq4RYaG5t_hCzXfCyIDpr-gIWrgb-A0e4b6HE3Ui5JHkWo6NFFLyTH9Svvk-DeM9NVOtwHovviot103a-dMgPQEGqdwmSrQEmpFa6JWLwKt9DOhC0p5g1x0EinAB9Ktjeh62piNThEfCklrE3NthHu1z_cw9biTSWMb3p7-xyBwJC8yQ2RPzMGcI19NQOtKVbXqDYfGk5SZhZHtOtOnx4OkkHcI7-NaPkJR_bLb9lDdvl6wYeOiXp6dJskV9Ktuhk1USw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
قالیباف در گفتگو با محمد درویش، رئیس شورای حماس:صلحی با آمریکا وجود ندارد و اسرائیل را به رسمیت نمی‌شناسیم!
🔴
دیپلماسی باید در خدمت حفظ و تثبیت دستاوردهای نظامی باشد.
🔴
مذاکره زمانی موفق خواهد بود که کشور همزمان آمادگی دفاعی خود را حفظ کند.
🔴
ایران بر حفظ تمامیت ارضی کشورهای منطقه و پایان جنگ علیه متحدان خود در محور مقاومت تأکید کرده است.
🔴
جمهوری اسلامی صلحی با آمریکا ندارد و اسرائیل را به رسمیت نمی‌شناسد و حمایت از جبهه مقاومت را در قالب‌های مختلف ادامه خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67365" target="_blank">📅 09:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67364">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67364" target="_blank">📅 03:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67362">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pDLqoKKJ3TH19Si8iS16xoLlCVWAjt_3OQf9y1tSFvWQSwEA2Ib3oHh3H-AwYM3f_4Oaa9p_DKMj-uPrKDTFgcqO4XwrgJpYNCm6krZTIoNRISXgw-fxt1v2H_w9d2Vs2a5i3keVhAlNZmbWs45bTCax0JOdoZ8z8xfbSEEcMEwdx30zEFV1xtBPIc9bOZ1QUjG0B0xb45LNiL9viJ02ikuTxJUY7fWqVDECGyLdkj-xK40ojOm0lYx59lKbGuY3QRWegRIiTQFL2TUeJ_FfmczkV992Mww-OKSL74OM2E3rrYqzkrh7DFeXpdPjlzt_eeMeZ2_s9Ug5cG2SghvzJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/67362" target="_blank">📅 02:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67361">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1fe48304.mp4?token=EDIY9MVNxYmmR8Y0QlX-dGB_n6kB7EhjuGlIPKHvcAmg1Ynx6vLdncAWKfKIodcB5jiS4zwPIX_ZdslGQuDXXsw9UcSqJLAbTE6x2QiHssoy6UNHRdLq7rp-qUtWRMEGBUzh3nkINzldFjzW-joB5uYU8DBLdBa9fTYF_esyJE9xvDxHDAnYB29zGKCdBCCNLXKZZZBvOxZi01YEhUEULrzrst6PUXnpzltt5N5JgElNhQLC0S1dY42AcvlKOSkYEahDy-6PJJBbskyVSZ4uv2vwghCLrF3yrWcxQDb8fk6A9e9GHbg3gkWd_c6Ld8KIJsCLDH7AlkObl2y1PzaX3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1fe48304.mp4?token=EDIY9MVNxYmmR8Y0QlX-dGB_n6kB7EhjuGlIPKHvcAmg1Ynx6vLdncAWKfKIodcB5jiS4zwPIX_ZdslGQuDXXsw9UcSqJLAbTE6x2QiHssoy6UNHRdLq7rp-qUtWRMEGBUzh3nkINzldFjzW-joB5uYU8DBLdBa9fTYF_esyJE9xvDxHDAnYB29zGKCdBCCNLXKZZZBvOxZi01YEhUEULrzrst6PUXnpzltt5N5JgElNhQLC0S1dY42AcvlKOSkYEahDy-6PJJBbskyVSZ4uv2vwghCLrF3yrWcxQDb8fk6A9e9GHbg3gkWd_c6Ld8KIJsCLDH7AlkObl2y1PzaX3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
ارتش دفاعی اسرائیل:
پس از فعالیت در نزدیکی نیروها: ارتش اسرائیل یک هسته تروریستی وابسته به سازمان تروریستی حزب‌الله را در منطقه العقیده هدف حمله قرار داد
امروز (یکشنبه)، نیروهای تیپ کماندو یک هسته تروریستی وابسته به سازمان تروریستی حزب‌الله را که با موتورسیکلت در منطقه العقیده، در نزدیکی منطقه امنیتی محل فعالیت نیروهای ارتش اسرائیل، در حال فعالیت بود شناسایی کردند.
فعالیت این تروریست‌ها تهدیدی برای نیروهای ما محسوب می‌شد.
پس از شناسایی، ارتش اسرائیل در یک حمله دقیق، این تروریست‌ها را با هدف رفع تهدید هدف قرار داد.
ارتش اسرائیل به فعالیت برای رفع هرگونه تهدید علیه نیروهای خود ادامه خواهد داد و به سازمان تروریستی حزب‌الله اجازه نخواهد داد به شهروندان اسرائیل و نیروهای ارتش اسرائیل آسیب برساند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67361" target="_blank">📅 01:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67359">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjPW4Vp2HxolA_BPbP5iqb0V-D4F1s8x9qf3zwMYNp6Rmo50VfzZ0Ks-HxFmsivkPorzgWYQAlgRPGwmCqqK0qLi0eGme5nFmFvnlDqsPwR2oTIP5kRWLajNFgrljpRJZLJdg4uHwyOvaQoLks6y8hnC3bmz4LUc9vWoO5ytJu_NTMSYGd4cR_b8xe8SIlm7Fhp8gOQ2ZwhTZpOD9iMdE7wf3h1gqmPePv8ivHXItDS1AzoEmUyMFUdGCPzAiIGVrllM2Jvj2GYMOjiq4dZpXlE1tm076KABRpNxHzDATqxlAAefmTjcBT3OIEZyhfUXTpMrv1rzSwE2joQQH2NBPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کانال ۱۴ اسرائیل:
انتظار می‌رود نخست‌وزیر اسرائیل(نتانیاهو)هفته آینده برای دیدار با رئیس‌جمهور ترامپ — که هشتمین دیدار آن‌ها از زمان بازگشت وی به قدرت خواهد بود — راهی واشنگتن شود؛ دیداری که در آن برنامه هسته‌ای ایران و خرید احتمالی جنگنده‌های اف-۳۵ توسط ترکیه در صدر دستور کار قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67359" target="_blank">📅 01:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67358">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6d2fa6e6a.mp4?token=uWnb2gnNrraFKtnPabZ_YChordEOUTezuVDWU9WUyyFPMZYVEniRvaxErHDtZ_54QDFYbMsWFJe28AKfYqLTTsoNHItPHP50aCfug4VTsyPXhCiMT_D9duP9REEXeiXceOEQpPWpF6TS1nyLd4AA0al4_I97gVoZhswx8NNhvWAp1eKMKP3cW7IbqjEIJkEQjOLUnBDvAszIV4mwXuiQerHuURbnFhF3Bb7gj1pvNkS0NPR17zHFaQi0gFmgSgRNyf6cKuhtBJBN-D-eXriujBQLcoH1dB_rM3mll2_PVYFokc0CQir8rkKuMLTCkkXeGWl2JyEhvNMcUlnYaOo9qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6d2fa6e6a.mp4?token=uWnb2gnNrraFKtnPabZ_YChordEOUTezuVDWU9WUyyFPMZYVEniRvaxErHDtZ_54QDFYbMsWFJe28AKfYqLTTsoNHItPHP50aCfug4VTsyPXhCiMT_D9duP9REEXeiXceOEQpPWpF6TS1nyLd4AA0al4_I97gVoZhswx8NNhvWAp1eKMKP3cW7IbqjEIJkEQjOLUnBDvAszIV4mwXuiQerHuURbnFhF3Bb7gj1pvNkS0NPR17zHFaQi0gFmgSgRNyf6cKuhtBJBN-D-eXriujBQLcoH1dB_rM3mll2_PVYFokc0CQir8rkKuMLTCkkXeGWl2JyEhvNMcUlnYaOo9qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو ای که فرستادن به صداوسیما از لحظه حمله به خونه نتانیاهو و ترامپ و گرفتن انتقام علی خامنه‌ای
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/67358" target="_blank">📅 00:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67357">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/237c10defa.mp4?token=ucJ5ym8FEM_O6XR3EOxsWqlrYI-ytpO07Wbej367BFLUUKV5PRBYkEveWA4MJ1oh4BYfOJyM2_UDAiN0FwlZpDDOKF5vkYbuTjWxZe2o1UUe3RUsAa4QMrhA3juD7SYaC9w3KT459K7wBgPau-oFA7xW_MPPNnKd1CHbRMKg_9U8WmRBOC303GQKEULBk6dVVjzsKsZQrs9_eOfDzNf-wKiAK71IlhbsArPitjXMgF7ZTtS-8-kKDpgS7QEGcqrMC3mhIPoMGC6nkVuy_ObYgip6r4Yj18SavpvGIoSuz6yET03Ya4tTFnZeOuv6c75T_2q4MxFY-Q1lYq8yjMLmWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/237c10defa.mp4?token=ucJ5ym8FEM_O6XR3EOxsWqlrYI-ytpO07Wbej367BFLUUKV5PRBYkEveWA4MJ1oh4BYfOJyM2_UDAiN0FwlZpDDOKF5vkYbuTjWxZe2o1UUe3RUsAa4QMrhA3juD7SYaC9w3KT459K7wBgPau-oFA7xW_MPPNnKd1CHbRMKg_9U8WmRBOC303GQKEULBk6dVVjzsKsZQrs9_eOfDzNf-wKiAK71IlhbsArPitjXMgF7ZTtS-8-kKDpgS7QEGcqrMC3mhIPoMGC6nkVuy_ObYgip6r4Yj18SavpvGIoSuz6yET03Ya4tTFnZeOuv6c75T_2q4MxFY-Q1lYq8yjMLmWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پهپاد اوکراینی یه سرباز روس ـ افریقایی رو تو یه مزرعه تو شرق اوکراین بدون شلوار حین دسشویی کردن گیر اورده و افتاده دنبالش
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/67357" target="_blank">📅 23:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67356">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFp83hpHl9I4tTp_vwazO-LbFe7XgO9PdK-cLUDzon7-4qgDOJK1OyQjA-oZgVvhyzsnnP9AJ4kPUD_t8wJFGhe4e-i5opnnwr_tKVKb1aXeELQHP3H6c9RgudQzv1gXvrTJWpjiDhEaW13y-WN2kEVAkw1pR_qz0EvEc_-PxNdrT9-GLgrMS_ys1kwa6DhIW_yf9MrzoE3QTQynMgjVt5_PFcvvLTukKdbfIH_HB9D0nRik7DRdx-lTF0Q2Bv3n-qXed-wYzr1zZ_rVbLMec2jFqP89NiKV0ipFRsVyhEnNvZe3i1A9dUyi1eGXO6P97V0Wgapqtm_53JUUTh6qLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سنتکام:
یک چترباز ارتش ایالات متحده اعزام به خاورمیانه، آموزش تیراندازی انجام می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/67356" target="_blank">📅 23:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67355">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb140a8f9.mp4?token=B7YTzy-yWwmr0YB05oxcPWlmoEriNBL_qe91NCiD8vrWBXJaoBZQSv_pXS3EK8I87zG-xkUiu2kBDxzq3rZjZAmFMRPscUPiRqEMus6n89cxf-7oRxMB7NYl4FtEUVGZ7y6VoikZji1bRKJ473ySFkcL55V6la4Czdltmr1utGZOkOru08_HrkdFzZa7F7bhl69WhnPjRYfz-KM4f5_1o9ATkjD5bhkmg-3tmZYFEH1VfKDYLaEq_18ZBnfgj0iMfIdJ0mRE34TmmqOxapWtgiOO74-UuIxYeBuT0PyDx9wiBt43b5pTgl6ns5Nzj9_yAQTaFA_b-_pkoe4GfJn5Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb140a8f9.mp4?token=B7YTzy-yWwmr0YB05oxcPWlmoEriNBL_qe91NCiD8vrWBXJaoBZQSv_pXS3EK8I87zG-xkUiu2kBDxzq3rZjZAmFMRPscUPiRqEMus6n89cxf-7oRxMB7NYl4FtEUVGZ7y6VoikZji1bRKJ473ySFkcL55V6la4Czdltmr1utGZOkOru08_HrkdFzZa7F7bhl69WhnPjRYfz-KM4f5_1o9ATkjD5bhkmg-3tmZYFEH1VfKDYLaEq_18ZBnfgj0iMfIdJ0mRE34TmmqOxapWtgiOO74-UuIxYeBuT0PyDx9wiBt43b5pTgl6ns5Nzj9_yAQTaFA_b-_pkoe4GfJn5Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خایه کنین؛ توی اردبیل چند تا آقا نشستن با یه خرس نون و پنیر میخورن
🗿
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/67355" target="_blank">📅 22:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67353">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AymqkP4PJS8lWQlso3p7-nFoHPRIEQsZFhyi_eyK3lQMINQIVjwZ843f4ABclJfJebBtkfyaqb-mp5FffmRcLzUYttQleCd_VukJHTekm_bZDhz0GqLUtPu5dpDOCSu7t1UPcRT8ECqmoo-QKwFMLgPCeVzfSjw9De8bgrVdcHxnvzyIT9iE_yJnsLM8SS_nuvRpBU-JdA3v1abcxJ8OxXImXkBVT6grDXZPzRWmIcNf6HzCBsgqOxrAFQqLodWEzr9Wx3y6q2U9jarT9OG8fA255cqYwA9hvDIQFlZRxYhADf5POZDDHk_0arBFroVYn7UoNrIsCDnouCyeW5VYhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسرائیل به فارسی:
مثل اینکه مجتبی هم بوده
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67353" target="_blank">📅 22:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67352">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc47a54d3f.mp4?token=CCZ5mQSM0yHhcnOGP2oKPGDUBPz2f5GKpxf7fKLZ5nJrd0jZnS0k_HiJpXLyIJFcldLt-lZnq1SizPN3QlNU7ZRcNZ6bev84TzwEgML8XyrPlLq5NbUvEcnRRI-qK2giGC4SyHBbXeD62J9ZSP2wVuY8O3W3PKjX_4Z4P51BuyfxlgnkN-8WrtUlEkebJWglNOqAxMB8a6XB5hhIlGAPkkn_eZrrzKyC208Bs4y77n6ibzRD5zUIKry3pkoQz9YrWoZBYlyIOqGAw7lrfTtRs0ZBCwQhMEInVZi4VRd4862n96LLJY-dkIi5kBd1hTOP6kVFVk0251Z4Cm6xRK6dtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc47a54d3f.mp4?token=CCZ5mQSM0yHhcnOGP2oKPGDUBPz2f5GKpxf7fKLZ5nJrd0jZnS0k_HiJpXLyIJFcldLt-lZnq1SizPN3QlNU7ZRcNZ6bev84TzwEgML8XyrPlLq5NbUvEcnRRI-qK2giGC4SyHBbXeD62J9ZSP2wVuY8O3W3PKjX_4Z4P51BuyfxlgnkN-8WrtUlEkebJWglNOqAxMB8a6XB5hhIlGAPkkn_eZrrzKyC208Bs4y77n6ibzRD5zUIKry3pkoQz9YrWoZBYlyIOqGAw7lrfTtRs0ZBCwQhMEInVZi4VRd4862n96LLJY-dkIi5kBd1hTOP6kVFVk0251Z4Cm6xRK6dtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمزه صفوی :
یکی از گرون‌ترین سیستم‌های حفاظت در بین رهبران جهان مربوط به علی خامنه‌ای بود، اما نتونستیم اونو حفاظت و پنهان کنیم و از دستش دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67352" target="_blank">📅 21:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67351">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
ترامپ:  از فیفا برای انجام کار درست و جبران یک بی‌عدالتی بزرگ سپاسگزارم!  @News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67351" target="_blank">📅 21:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67350">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmK_Rci9koXcS4N3p9eLpapR6Fp5fzdxvD4YhuU54GtDpxiOlrsn7G4H-a3ahsxZwXJOUCoWGFTDjFXA42yYqqmNxteZbYipmypkyDnOuSvA0tlDhSdtH5Cn0yA23x4ao-A-PMfoGF4k_9YMmBNCbjSvtvYDmDUB8gkc6fntKwG67iL156FhNiqRGUQjY_ZY6d7O0q2qvmMpJ-LvxWh31Hm_h-8VM_TStxIqjvsJtRaP0a_w5qTS9_kGLVfXrjeADGgy3drNJMH8IGi3H8GPmK86dXFss0df6CwTmSHXjxFAlBHYnw65xEmwF-V4XnnX8-pe1s5dQxvuqmfGth6Rkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ:
از فیفا برای انجام کار درست و جبران یک بی‌عدالتی بزرگ سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67350" target="_blank">📅 21:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67349">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d12e972bb.mp4?token=az2vNLY0r4Huq-FO75iJlgXmpIR0d-beL2tI-zVFc2Uf3c45cuYc0zFNOLcjFyuhbrwyuzRixC50uGZmrH0cJ4gxQZ6NforOt___EJplpluPKqLJa82fekCOwZkENEvnKiVzDwefhYPnpIjlEKh44_oUK5qpURJMuPU7SkmdJIgUg8xORbqXtdA7jQ-lLnkKTysEuIOuARtm2SpgI78mlgZLaaXHWM8362i_u-U0imcrgu-KlmHiHakIxsKr0tOYGOWJqvpjAEM4wpYFvcVt50ajFWPjRfVvY87Rp66HouMf2zHDmYjlFGJUGtfUDQm1jpdV1EeTqq8tjS3Crd1_1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d12e972bb.mp4?token=az2vNLY0r4Huq-FO75iJlgXmpIR0d-beL2tI-zVFc2Uf3c45cuYc0zFNOLcjFyuhbrwyuzRixC50uGZmrH0cJ4gxQZ6NforOt___EJplpluPKqLJa82fekCOwZkENEvnKiVzDwefhYPnpIjlEKh44_oUK5qpURJMuPU7SkmdJIgUg8xORbqXtdA7jQ-lLnkKTysEuIOuARtm2SpgI78mlgZLaaXHWM8362i_u-U0imcrgu-KlmHiHakIxsKr0tOYGOWJqvpjAEM4wpYFvcVt50ajFWPjRfVvY87Rp66HouMf2zHDmYjlFGJUGtfUDQm1jpdV1EeTqq8tjS3Crd1_1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمد مخبر مشاور علی خامنه‌ای:
قاتلان امام شهید به مرگ طبیعی نخواهند مرد و نظام آنها را به قتل خواهد رساند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67349" target="_blank">📅 20:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67348">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5503b743a2.mp4?token=V5n3Q43ZiPfr8gLjC_i_lR9RlR6gVluM_4yozte9y4sxeocsfEQkfRXOwo5Y2SGsCkN9FkDctxPgMo8PnzNDVBeMvWIUtU1wabkYW5iWY0pcvRty9l85GimQVzRwWmvQ4rZ8lAUWtwcxw-PS0PAUvHBtpiChHIUSIsrmE7O1dsZjEsS8sgyNdx0ohBfEU81L5M2shp9aMFd240Rp9gBaMdzVl_TF2rZKvC7_rYZFSwQzuo0P1xG0ToAxxYO692KznFyRG74BXJXuockrhksGzw8xDBHTQ537GP8cxQc7JhuEMa3RiQD7PYUCLw_gcFG_3Fvup7EB-5Zr8ZBNJltZCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5503b743a2.mp4?token=V5n3Q43ZiPfr8gLjC_i_lR9RlR6gVluM_4yozte9y4sxeocsfEQkfRXOwo5Y2SGsCkN9FkDctxPgMo8PnzNDVBeMvWIUtU1wabkYW5iWY0pcvRty9l85GimQVzRwWmvQ4rZ8lAUWtwcxw-PS0PAUvHBtpiChHIUSIsrmE7O1dsZjEsS8sgyNdx0ohBfEU81L5M2shp9aMFd240Rp9gBaMdzVl_TF2rZKvC7_rYZFSwQzuo0P1xG0ToAxxYO692KznFyRG74BXJXuockrhksGzw8xDBHTQ537GP8cxQc7JhuEMa3RiQD7PYUCLw_gcFG_3Fvup7EB-5Zr8ZBNJltZCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
قول میدم راه امام شهید رو ادامه بدم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67348" target="_blank">📅 20:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67345">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s6Z5D28CcYpOSEGsPwwniscc2WavcF4s9mlSl3yomF06i47v5C9gyVlX2cDMusnur_vzDhfTWqUHqYqGkvju6Q8A9UuJAeasVpur5qeUM9wV-rbea-DnGMnn6GnpyOM1YCkJ6Puypn8-tsStrP6BeYZ5ATL5YK-7NlsDU5HhgLnRL3wSzxEjaec3-pQ0F5U6t6I7su3j6a2kO23W_E6rTmFWqM3074tKJkjLwYxMflJ_spO6GwGebUXsszBFtsYgTZSwFwW6yPdPOQaZz9UIU-3FMcebIi0lMwFxBsAfS95Z6CdEB2L-6RTs6ZhgPWnhQlCcIVDv50tpJS_4YZLC0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FiEvPhPnDTIMoAd7eVdaFab3xPwFbz7YKbS6zGX-57i1hJH5DZRcc4Jf7u5LmoGvB5MibdZpCMW07CVZZkAzahajtRPu5ayLN26CdSqoqFbJrljObnuq-npV29gP1d5ol4X1KBHKQgHuWunxjYY88VmqGLGofrFeHL6Lxjxg0CEiFu8zaqO7aCMGgMQdvV-hy1_EpaWmKNNFmVty0f5jj2G9dGd6WEZPiE7mvByVkDHxOcaXXQ-JLAwJukB_MXATO7oOropH-Ky_03eKfY7bw5bkOmQUDKvNnTh0ckBeCztoXgHhbZvRULmqquHbrkK7SbzBpOUSNcq4ChNE5V0fMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a975887416.mp4?token=M4W3EUKBRE3M4GmkUuJDgWANC4gH9oH5Ts3_IQAdEb_cwXEYs1V9QvV9QpZ9ajkMl9hTJTefoz6SUcKlDS8ru9FH3bWn7pB8V2ASTfzJhTarBzkbpkCeQSDCTmSBfklueRDvskEPBHQ2LqnVrp-tgv_DpcGfi5Ckjm-ljFIUbBFXk3jkFXMN5e_FQwyN48akvODopVFmCbL2jsQrvrcrGLyJFMgOHyXTiW8YaXxvcqaNz9iWQfninVEz7_gdSLxqbtd-jK1D3xT8FzWHt397U-2PLRBUqNoLP0is17wu2WcZOmDxWBwW0zwz2KHcmZH5HFPt6wFswXCbV8CWHrf6Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a975887416.mp4?token=M4W3EUKBRE3M4GmkUuJDgWANC4gH9oH5Ts3_IQAdEb_cwXEYs1V9QvV9QpZ9ajkMl9hTJTefoz6SUcKlDS8ru9FH3bWn7pB8V2ASTfzJhTarBzkbpkCeQSDCTmSBfklueRDvskEPBHQ2LqnVrp-tgv_DpcGfi5Ckjm-ljFIUbBFXk3jkFXMN5e_FQwyN48akvODopVFmCbL2jsQrvrcrGLyJFMgOHyXTiW8YaXxvcqaNz9iWQfninVEz7_gdSLxqbtd-jK1D3xT8FzWHt397U-2PLRBUqNoLP0is17wu2WcZOmDxWBwW0zwz2KHcmZH5HFPt6wFswXCbV8CWHrf6Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
حملات ارتش اسرائیل به نبطیه الفوقا در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67345" target="_blank">📅 19:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67344">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4c05c580.mp4?token=imokjy9f9JnjfHHf81MHBaYlQxEwvBOwqzT5m19akCR9wmFaT-YDB7aNBc5heGsIw2WtSZgkzfFGMiOXTukJa7zJEkJRb5WkZlPwlPl3brbGB6ULjlCvYXYjVTChoCiOgg9WRTbdVwfb6H4J7A78pF0o8VfSiTOjegcrE-q0RMux271fKrTxzPjhmRBw92HnUON-EXuME7_lyQNV-G3vG0DQW9FuBkVsL6u9sCsAMtLpVcbrdXFvIuhNZWqKwNeAJWaXlNC6EzkLzeO96-xcfCm7iKszbGgw26badR3pU13gmVwqbfyA_5J-6UTQBHyLMVR5EGabV30TmZ-OwbnBQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4c05c580.mp4?token=imokjy9f9JnjfHHf81MHBaYlQxEwvBOwqzT5m19akCR9wmFaT-YDB7aNBc5heGsIw2WtSZgkzfFGMiOXTukJa7zJEkJRb5WkZlPwlPl3brbGB6ULjlCvYXYjVTChoCiOgg9WRTbdVwfb6H4J7A78pF0o8VfSiTOjegcrE-q0RMux271fKrTxzPjhmRBw92HnUON-EXuME7_lyQNV-G3vG0DQW9FuBkVsL6u9sCsAMtLpVcbrdXFvIuhNZWqKwNeAJWaXlNC6EzkLzeO96-xcfCm7iKszbGgw26badR3pU13gmVwqbfyA_5J-6UTQBHyLMVR5EGabV30TmZ-OwbnBQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
ما در وضعیت دائمی جنگ نیستیم.
من خودم، به همراه رئیس‌جمهور ترامپ، چهار توافق صلح را به پیش بردیم.
تنها مسیحیان لبنان نیستند که از ما درخواست حفاظت می‌کنند.
دروزی‌ها هستند، مسلمانان هستند، مسلمانان سنی هستند و حتی تعدادی از مسلمانان شیعه نیز همین‌طور.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67344" target="_blank">📅 19:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67343">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a4244b191.mp4?token=fuCSsku3oVm1cTX9HuMxMbcZU3IiVt_6vYB0rs6YYrSMcXmg00PW-K94LMuHCSl6BkS3_lyNFlQAdFPVUDRaQoiMzTjcCeDO-4c6x_SBwmGMhOyfRxAZld9FpY1gUZMs-HILiWIJWJTZ5O_9gcCkNrKywPVy4bb09twuCBH-HvGi-qfCluoq-ic8n-zou4LVJOQgsAtIxZVlhN9sPKNF_Qr_4JDypssXuPMj40vFUVpHS9jsUTq3JVmUUmgv2nDcUHjFQGdB94NnkXowj5GuXfWuJr5G_z4Sa2ayVE3ZDZyHDcNywSky1tblFkL68L4ow706P-rnx4s_d70X3cAg7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a4244b191.mp4?token=fuCSsku3oVm1cTX9HuMxMbcZU3IiVt_6vYB0rs6YYrSMcXmg00PW-K94LMuHCSl6BkS3_lyNFlQAdFPVUDRaQoiMzTjcCeDO-4c6x_SBwmGMhOyfRxAZld9FpY1gUZMs-HILiWIJWJTZ5O_9gcCkNrKywPVy4bb09twuCBH-HvGi-qfCluoq-ic8n-zou4LVJOQgsAtIxZVlhN9sPKNF_Qr_4JDypssXuPMj40vFUVpHS9jsUTq3JVmUUmgv2nDcUHjFQGdB94NnkXowj5GuXfWuJr5G_z4Sa2ayVE3ZDZyHDcNywSky1tblFkL68L4ow706P-rnx4s_d70X3cAg7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
روستاهای مسیحی در لبنان...
برخی از آن‌ها در واقع درخواست الحاق به اسرائیل را داده‌اند زیرا ما آن‌ها را در برابر حزب‌الله محافظت می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67343" target="_blank">📅 19:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67341">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd048f948.mp4?token=ijOnShUzKEeZ_ChVgWhu57pzdJuoCNpMQhel1jr8gslTnW-xCbndkul6myKZT2DZ3_7NoS9DJtXqo5HqOLD7kzSsEiKVdtMsTX8IfAyZVl9uA26lZ_t2RxuoghNTHHculwxwZKRoH0aCkMwVGL1rZBNb0PXWBnpFvF9pxB-vH21xCZkSwyyausGdnx_iSfwAUK9LHkALYOJW5fAilKDFDRoNvmLZMh0YxtuvT3VXQahpnB1ko-q3dSsZ94uL3CnOkv-JyJep3ulKBOTct31fBCfDQ8agAQjBeT9btLIyDtJHb80l7aYVGlov60DLScEXyDWohyR9glJGaZwy_dxH_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd048f948.mp4?token=ijOnShUzKEeZ_ChVgWhu57pzdJuoCNpMQhel1jr8gslTnW-xCbndkul6myKZT2DZ3_7NoS9DJtXqo5HqOLD7kzSsEiKVdtMsTX8IfAyZVl9uA26lZ_t2RxuoghNTHHculwxwZKRoH0aCkMwVGL1rZBNb0PXWBnpFvF9pxB-vH21xCZkSwyyausGdnx_iSfwAUK9LHkALYOJW5fAilKDFDRoNvmLZMh0YxtuvT3VXQahpnB1ko-q3dSsZ94uL3CnOkv-JyJep3ulKBOTct31fBCfDQ8agAQjBeT9btLIyDtJHb80l7aYVGlov60DLScEXyDWohyR9glJGaZwy_dxH_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار تسنیم : نظرتون درباره رهبری مجتبی چیه؟
🔴
زن عرزشی : چی بگم؟! نمی‌دونم ما که همه منتظر بودیم مجتبی حداقل برای تشییع جنازه پدرش بیاد و حضوری باهامون صحبت کنه، ولی بازم نیومد!
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67341" target="_blank">📅 18:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67340">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c05464482.mp4?token=ebdZvISeCzSLzhQRu3VL1dNXVzr-zrp0eGXhuIiYpdoq5GZe2TP1Zzz6yDIliZM4oqBaQqQomHzELVyakMhbWKS90ulvbguxfZ0XNvLrxu9v2YGZO8kLLQmrBHm-Adj-TAnbqHOwc-wNBTRc4fY6uIFTIsNz-w5QH_UhuvHn5ejdOt58kJKcMz_X2tgAjj4qBmA2tevLurxUP5EreNeODtxQuiT1L1k_onOzIGEclQDg2sQJpVFC57fGOS1cS4Z_mkngPbyq3Vds1AbmEyTLE9-wb8Q7fU_WhUFZLtwCHBbvrW0UwzmzRqUZ4Yh6sSnZM6FjVZii2wMoPc5BSpTR7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c05464482.mp4?token=ebdZvISeCzSLzhQRu3VL1dNXVzr-zrp0eGXhuIiYpdoq5GZe2TP1Zzz6yDIliZM4oqBaQqQomHzELVyakMhbWKS90ulvbguxfZ0XNvLrxu9v2YGZO8kLLQmrBHm-Adj-TAnbqHOwc-wNBTRc4fY6uIFTIsNz-w5QH_UhuvHn5ejdOt58kJKcMz_X2tgAjj4qBmA2tevLurxUP5EreNeODtxQuiT1L1k_onOzIGEclQDg2sQJpVFC57fGOS1cS4Z_mkngPbyq3Vds1AbmEyTLE9-wb8Q7fU_WhUFZLtwCHBbvrW0UwzmzRqUZ4Yh6sSnZM6FjVZii2wMoPc5BSpTR7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زینب سلیمانی:
شهادت آقا برای ما سنگین‌تر از شهادت حاج قاسم بود
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67340" target="_blank">📅 18:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67339">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVKJT4Vu0ywxF67trSwH2PuYc-ozCTMn7YxHowwWLZXW-SCWdndNkPclaWUm3znhRGtKz_1OYEAYSeP06xc56UhikSCFVkBgU09gNZfYSnx_i9Mrro1w61bZC68mPdFB9KV23q37pZvr21WWTGkQxZ01xr07IVIFSg9UnauxWDQJLNRC7hluya9HCg9TRM20WU35-bz4-sr-vnCEKjzo0AUCj_ImqmsztvSvkk6Fk74uZ4ZdQMXWE8-0At8fBrG2CURmv7Cn_Y4maMv5peJChbmuhAlIGly2mPpW5xVcT_Cek4pOoSXPSlrfH1m6b0fSSpm1WMGEg4nKaUMFbGDz_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دفتر شاهزاده رضا پهلوی:
🔴
‏تلویزیون بی‌بی‌سی فارسی در صفحات رسمی خود، با انتشار بخش‌هایی تقطیع‌شده از گفت‌وگوی شاهزاده رضا پهلوی، تصویری نادرست و گمراه‌کننده از اظهارات ایشان ارائه کرده است. تیتر و متن این پست، با اتکا به نقل‌قول‌هایی ناقص که پیش‌تر نیز توسط رسانه‌ها و حساب‌های وابسته به جمهوری اسلامی برای تحریف سخنان ایشان بازنشر شده بود، به‌گونه‌ای تنظیم شده که به مخاطب این برداشت نادرست را القا می‌کند که شاهزاده رضا پهلوی آغاز جنگ یا تصمیم به حمله را به سفر خود به اسرائیل نسبت داده‌اند. برداشتی که هیچ نسبتی با محتوای کامل گفت‌وگو ندارد.
🔴
آنچه شاهزاده رضا پهلوی تصریح کرده‌اند، این است که سفر ایشان به اسرائیل، در کنار تلاش‌های گسترده میلیون‌ها ایرانی، به روشن‌تر شدن این واقعیت برای افکار عمومی جهان کمک کرد که مردم ایران دشمن جهان آزاد نیستند، و از این رو دنیا در برخورد با جمهوری اسلامی باید حساب مردم ایران را از این رژیم جدا کند. اینکه مسئول اصلی بحران، جنگ و بی‌ثباتی در ایران و منطقه، جمهوری اسلامی است. ایشان همچنین بارها تأکید کرده‌اند که هدفشان پیروزی مبارزه ملت ایران با کمترین هزینه انسانی ممکن است. چنان‌که در همین گفت‌وگو نیز تصریح کردند: «تمام هدف من این است که این مبارزه با کمترین تلفات جانی به نتیجه برسد… هر انسانی که جانش را از دست بدهد برای من واقعاً دردناک است.»
🔴
این‌گونه رفتارهای غیرحرفه‌ای و تحریف‌های آشکار از سوی بی‌بی‌سی فارسی در حالی صورت می‌گیرد که چندی پیش، مدیرعامل کل بنگاه رسانه‌ای بی‌بی‌سی و رئیس بخش خبر این سازمان به دلیل رسواییِ دستکاری، جرح‌وتعدیل و ادیت مغرضانه سخنان و مصاحبه‌ها ناچار به استعفا شدند. از رسانه‌ای که هزینه آن از مالیات شهروندان بریتانیایی تأمین می‌شود و با وجود ادعای راستی‌آزمایی، به دلیل نقض مکرر استانداردهای بی‌طرفی با بحران جدی اعتبار مواجه است، انتظار می‌رود فوراً نسبت به اصلاح این گزارش مغرضانه اقدام کرده و سخنان شاهزاده رضا پهلوی را به طور دقیق و امانت‌دارانه منعکس نماید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67339" target="_blank">📅 17:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67338">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d7e9ec8c8.mp4?token=gjqc0V_OauHWXeHacWQ8jVE_ycUko3RV3QpchH2PcbOwWqQ_t54Kd1y1D444FLW81eTBqS1Xv4_AX8gcpJy6tE9-e-wRV8RH_CfmZdT7dk9aE6VcVw4xfiaDmzYTGlOgOHtIR_VHoe6iviDDXKeN-KNzZMBd4inUG0WQy3Ynvip2AxDT8fxDGYVXdKVNJWLQwRcAVIMlO2AXkc6bvDXH72D7rZJTcnHzsTWgh1zSTJHRfh_uqBF7R8IVaX8tfdplvvyGr-XSJTZdyX5Uy2RSUY2FrW8q6p9B30CPO58AkVWIoHY3uin7pNym0uyQYGS4Ugth4h5ak1WGHcQJeUn2Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d7e9ec8c8.mp4?token=gjqc0V_OauHWXeHacWQ8jVE_ycUko3RV3QpchH2PcbOwWqQ_t54Kd1y1D444FLW81eTBqS1Xv4_AX8gcpJy6tE9-e-wRV8RH_CfmZdT7dk9aE6VcVw4xfiaDmzYTGlOgOHtIR_VHoe6iviDDXKeN-KNzZMBd4inUG0WQy3Ynvip2AxDT8fxDGYVXdKVNJWLQwRcAVIMlO2AXkc6bvDXH72D7rZJTcnHzsTWgh1zSTJHRfh_uqBF7R8IVaX8tfdplvvyGr-XSJTZdyX5Uy2RSUY2FrW8q6p9B30CPO58AkVWIoHY3uin7pNym0uyQYGS4Ugth4h5ak1WGHcQJeUn2Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بزرگترین آتش بازی تاریخ آمریکا در واشنگتن دی سی به مناسبت ۴ جولای روز استقلال آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67338" target="_blank">📅 17:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67337">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VnJqgmA16tVSR2CQ68gppcYxBijw5gdPkZ6nXW9iTGSG1KuDB4_l5UEEibAAmsOh-t3cRVP26hQajjw26B1TdeV0t9InWtOC2XEL2eXehtPyQndkMPwVGe4Z6a89HY7s333WPJxqKfmvhAzbI3c0poaGKLzWzbZMX0j1Qoc3xv3_leUSYymjTgDvo7-wSYSjR_TjrgWzXKJ7TSXqoVgKxrhJb7rGIqEfPu2TKpx2zfvqDqK-q_iYc3aiOwz_wFVEtwZwjfxhVGTqc2BDxEUac2zSbvbZp34x-4Fob6yChNSiGhG2NQUspTVAZ1PfFnHB4OGpvdaZdY65SGgf0wIXAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❌
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
تنها دلیلی که ما امروز تشییع جنازه خامنه‌ای را بمباران نکردیم آن است که 10 هزار مأمور موساد در میان آنان داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67337" target="_blank">📅 16:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67336">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e644784ac.mp4?token=T1lCt0eWohjHxp28D8-NGTLFb-bFyW7p62u7aC1B6RUo6GnxvuBKlq0KmWqOa_1efrXVE5RbDrz0v_JWfDvneCZPqxAQ1Ky3PE4-yyRo8Xh-5CJ2ntUPf91cpm8ZJ-50TnKsY_Pwjcy5dS1yOKOXSMrOxsH1pmtLG_xCk1P5GltJn8X2LhUOnWMevYPDEvZUf_kEHyYfimXnUxgf0rdePcfh6miHWDhqvQ41JZ5b2_YKX-JWhWlq14ipFh0gNOLfjPqAqzq_9B2hGZW8AhpbsN_zfQ9mkmcvI2TCE_P2qvzP3BwGQKw6FKDJYRtKvpagCU94aneojTyA2A0jR4g2QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e644784ac.mp4?token=T1lCt0eWohjHxp28D8-NGTLFb-bFyW7p62u7aC1B6RUo6GnxvuBKlq0KmWqOa_1efrXVE5RbDrz0v_JWfDvneCZPqxAQ1Ky3PE4-yyRo8Xh-5CJ2ntUPf91cpm8ZJ-50TnKsY_Pwjcy5dS1yOKOXSMrOxsH1pmtLG_xCk1P5GltJn8X2LhUOnWMevYPDEvZUf_kEHyYfimXnUxgf0rdePcfh6miHWDhqvQ41JZ5b2_YKX-JWhWlq14ipFh0gNOLfjPqAqzq_9B2hGZW8AhpbsN_zfQ9mkmcvI2TCE_P2qvzP3BwGQKw6FKDJYRtKvpagCU94aneojTyA2A0jR4g2QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اگه اهل دعواهای خیابونی هستی، این ویدیو از استاد طِقه زنی رو تا آخر ببین تا به امید خدا پیروز میدان نبرد بشی؛
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67336" target="_blank">📅 16:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67335">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/67335" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67335" target="_blank">📅 16:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67334">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67334" target="_blank">📅 16:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67333">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbADiWIb8tETxKQ6OeFCAxAdKEYl9Gtnwq6FFuhSiKwbUXTW3ltIPnB_ESOtTa92ntOXJpVGnHmBw2JOxCtnR1SYA5mW0n3GwQgopvsWp1r00kKI-c-ERHRqP-XdWP3oR5GPERZppi6P1x66awfm40clMg5xnAlS_hdrq4XBK8cvp6WWJ_7AC4ToCqtUtL79oYE4JHRZ4E4zkWV0vmqajCLkZlbxIP2bf3lRk_Cwc7xHQRtpRBkTI4yPoJ0TfIS_iH5vKzHLE2EA9vRG573fD-YLy_LCJ5x4CuUgQ2NJY0QmFl45Ozozm1le7J57QtwT36WvFpYJWXGONqke2PT78g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گویا کامیون حمل جنازه علی خامنه‌ای مبلغ2,298,000 هزار تومان خلافی داره
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67333" target="_blank">📅 16:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67332">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8zmFvg8xTkLiRtpxMFw2WPm_rIOk3osem41ZJ54UPS7sIpZbKVJFb6ngimmHq-ydrL9kA_R5ic9ACpducQn71dcGy6wNAu4mm556tvUDhnsP8V44a6cebfUtKr_rmBzz4NXaS5155b_vk8OdtGu6nEJ7wILsbI75BnlypaR8iwv-yrNij9rI-kKlzvXtdk2SXYyqF4iCCsVgOc2cD-VoWdggQuTsEyhX4Wna34oxVesl7jcYV_mG_ZPohkriAVr8P2hQ_cgSC4-AVSOg_iiQYCwdIQfZ28Sb-V0Lsi0ATURQhyPhI6rfX8w0ljGGNqLzNebURhHeV2yj3YlacD1SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
محمد اکرمی‌نیا سخنگوی ارتش:
«هرگونه اشتباهی از سوی دشمن، با پاسخ قاطع نیروهای مسلح ایران مواجه خواهد شد. ما بارها اعلام کرده‌ایم که از فرصت آتش‌بس برای ارتقای توانمندی‌های رزمی خود بهره می‌بریم. ما حتی یک لحظه را هم هدر نمی‌دهیم و تمرکز خود را از این مأموریت برنمی‌داریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67332" target="_blank">📅 15:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67331">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو در جلسه دولت:
شنیدم در رسانه‌ها گفته شده که رئیس‌جمهور ترامپ خواسته علیه تونل‌های تروریستی در لبنان اقدامی انجام نشود. این یک افسانه و خبر جعلی است.
او حتی یک کلمه هم در این باره به من نگفت و من هم از او چیزی نپرسیدم. ما بر اساس ملاحظات و تصمیمات خودمان عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67331" target="_blank">📅 15:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67330">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRrsCDgOO33ak7fM3_3A66Lp9Da8pbFMI2ZZnn2rDXHfKzR-NyD1Supd6ROGIJvtk00yaWLgFIFXQZ1eRZVtNL7XRn2BKBXUUB_ApYZaBJ-6rh3S6p4WbEe7T2eT0QajmJcRPmxVQcEThGslrK2qJnEZAx8ag_lbVFXNkk0hR0FJp1TWRAzBGN6e_joE9EdzLXMFYPd793Y07vmhBVhRoBxCDv0d19r8M26ukhoH_u7mC17_Q6nJOkLtNjVxCbmaeDAR5rpfLHA9ju2RDJ7jCuEg--LmFpuyAANzLY3d15v0srYTgQ2vUFYdpjxPnSu_L60BW0FPJiqH8yfBZouYHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویر ترامپ در مراسم وداع با جنازه علی خامنه‌ای که روش نوشته شده:
خواهیم دید چه می شود
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67330" target="_blank">📅 14:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67329">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unVSNpRV0QhackQiqYxP_fai1qzBxXifUgtsCvBsjn3otqHikoVZIz1C8IOsPfKxmuqrlg8X92y2zYgVS5erlA0C04NaNEsP8u2FE8X827uAnuxsmp5ocm_I79LE4M627iq1AfZBK19NekV3f8p0ccpshsNoZh8USWMVBr4LgQCVRAwVZduak6xl3s_ploY_yHObUVgEsIo4Jpmsvab9dIe37rDXWW1LSLYfJDWQKG5nEduQQIVlka1vGfMVSmYB0KyJg71taTgY7SE6j6G_eNfqHweOWoZgyBqVIW9zqPqcXAXJoSYx_LdziRbO85v8gRJJlO_2wRC6rUdiWPNeiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسرائیل به فارسی:
بهرام که گور میگرفتی همه عمر
دیدی که چگونه گور بهرام گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67329" target="_blank">📅 14:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67328">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b8ead8806.mp4?token=bHKHczKUXq0RXZ2S9h0I_27sZcrE0us9OrTuV4J9f1lSb5pmxFCpiLX1QQ4bHQdCNAVmpV_hEDLXSHp9DWYsaMouzv2vKs-ruWNnpuXLC_OLzL3J_YsZ5tz5ZPo4Sa8rImhl-u-Pq6IdSWyFO6QuhvgDMapZQRek8KjPgoyIVXitgTJZT1Nugodp3kAz5U7MWpqIRzCTsC0UlWzGJOg0j8i1JTm-Oxo6D60DSH2m6N9yU3uvxQV1tJhvT-5jy6_nBxRvjV5sgQLgbI_cWqk5b1MVbfe_s55X6QvXWsibR-FpCH7-kNjrGtCHQ_1z9bn--1dWVhBjPJhyZLqadsRPrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b8ead8806.mp4?token=bHKHczKUXq0RXZ2S9h0I_27sZcrE0us9OrTuV4J9f1lSb5pmxFCpiLX1QQ4bHQdCNAVmpV_hEDLXSHp9DWYsaMouzv2vKs-ruWNnpuXLC_OLzL3J_YsZ5tz5ZPo4Sa8rImhl-u-Pq6IdSWyFO6QuhvgDMapZQRek8KjPgoyIVXitgTJZT1Nugodp3kAz5U7MWpqIRzCTsC0UlWzGJOg0j8i1JTm-Oxo6D60DSH2m6N9yU3uvxQV1tJhvT-5jy6_nBxRvjV5sgQLgbI_cWqk5b1MVbfe_s55X6QvXWsibR-FpCH7-kNjrGtCHQ_1z9bn--1dWVhBjPJhyZLqadsRPrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این بزرگوار که قبلا گفته بود بخاطر یه تیکه نون به سگ دادم اومده داره ترامپو تهدید میکنه میگه بیا کوت عبدالله ببین چیکارت میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67328" target="_blank">📅 13:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67327">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
❌
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
تنها دلیلی که ما امروز تشییع جنازه خامنه‌ای را بمباران نکردیم آن است که 10 هزار مأمور موساد در میان آنان داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67327" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67326">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0be756a04.mp4?token=F_cbSD_X3qpXA2LaVJlkfi_lhtMRXVJFtKv-ftkaW6zY3AeE0zIomYi60CbSOlZcib2h5iezil2xc0-o1wKeZspC3zSAYpS0imXF2tOtLkYm6GwgVC1OK30Gl2MrNGlT4psA3kzjkte1mKNgtS6PH5gyYvvruR_5gdioWKW7E6ggXeU1T2lofpy1ZukaFG1cC6w6inwkiDsDGdVU8FpClUD2DY1uhk4SHehw7pUieIe1B9rxsgLiCftnvvbFNsViJ_CQgOyA0yPZtL4mvRBNKOfWrSCXVL_I3t-4GkN4cnEcnMYawHnYoQa64EH3WIPUscRNz0vkO4CjuKKzyUUl3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0be756a04.mp4?token=F_cbSD_X3qpXA2LaVJlkfi_lhtMRXVJFtKv-ftkaW6zY3AeE0zIomYi60CbSOlZcib2h5iezil2xc0-o1wKeZspC3zSAYpS0imXF2tOtLkYm6GwgVC1OK30Gl2MrNGlT4psA3kzjkte1mKNgtS6PH5gyYvvruR_5gdioWKW7E6ggXeU1T2lofpy1ZukaFG1cC6w6inwkiDsDGdVU8FpClUD2DY1uhk4SHehw7pUieIe1B9rxsgLiCftnvvbFNsViJ_CQgOyA0yPZtL4mvRBNKOfWrSCXVL_I3t-4GkN4cnEcnMYawHnYoQa64EH3WIPUscRNz0vkO4CjuKKzyUUl3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جمهوری اسلامی پس از ۴۷ سال در مهم‌ترین رژه‌ی خود حتی به‌اندازه‌ی بند پوتین‌های ارتش شاهنشاهی هم نظم نداشت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67326" target="_blank">📅 12:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67325">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWKKmN8XBWz4-mCwI3lD25RluxcvvhgRGu-V_eiJ6sQekX56DNQrDLsomvRwgitTCXh9ugWBzyfWQh2gQhs27XDRLeLQceQolO3DDwKZLeA4JtL1LtlL2cyHeK3mQvCLc6NEzdzjyCmK31ctJx4vZCiBjTB14vCLpH9D4ljLMvap8rIaFqrhN2k1z2ymkmLKLMdjDrf7eu3fvG5Ft9kM069gZArsqm8I_PNy40PLV20KXDSdwuC7dVPa_k_oJ39ONUIfHKensl-jhvA16ueHAB8zwzS-fopygQxaXPr_r5N-e6nNJ-RfIy5sT5_eIzT99eYKWCUX3lvmtrXjVAItKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هرمزلتر:
🔴
نیروی دریایی سپاه با استفاده از قایق‌های تندرو، کریدور مورد حمایت آمریکا در تنگه هرمز را به طور کامل متوقف کرده و در نیم روز هیچ شناوری از این مسیر عبور نکرده
🔴
سپاه صبح امروز از طریق بی‌سیم به تمامی کشتی‌ ها هشدار داد و همزمان قایق‌های گشتی نیروهای ویژه را برای اعمال کنترل ایران بر تنگه هرمز مستقر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67325" target="_blank">📅 12:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67323">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgtGeQEIh3x73ZGGCGAjh9NWhA9lpczb4BwMKYQISAG6QK51rH51QBs-4WwhJPbtkASRzMcLwXeIbpvEFdeX1YdqPGH0uA1kk-7e9SC22C9k_nf5CkYq0GVnTz2UoYuo0ghrxodqxR0J2TzjcMw3HlEUjyaCspNip4Awb6xrKr-JhzuWI41qCHA34Wy7b3ycBl4yzBkUwHC4k2-JdWJ3dbBRSF5O1FL71lBkMGXrUeVwTXXSiFDGgVp7kwNDv1ZwBVohBFqhw2Af8e6qxJD50GM4vdssE6hVSQ0rCLF68A2LEZWgPMydGtTkvGf4MHXuuk5hQ4niXQIwaZR4u4kwKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f22dc07ca.mp4?token=HF-M5xhFOycAGfEJqmEdZemUcn1aG5c84cIufHlXS43WU_HO0Yp_ETxdTcHqzw7mFEh3n7boUbgFljbeDNCuv6XhTUrhCJ93ePbvN9cU87MmLQgxBEUOCSb47Ak7wUuxQwNln6kTqe8QHAkWsdNKBEtNeszbDH9riBSWYvTQWiYxZXfUOJ-SVYzxDN1ToyrIA7YxVB7IfM7-iCNakdgR4uzGrx7WGQpQ1MdaJutlkP3c-SuQ_oNmH_s_Nyujzw1Utmbw_xlC-9oDIn6MvsYKBGTSFeT2KWNIts1fyGgAhAeH6IXdczZY-wlEw6kMftUOu9bT-PlZmjw-PercZtWc9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f22dc07ca.mp4?token=HF-M5xhFOycAGfEJqmEdZemUcn1aG5c84cIufHlXS43WU_HO0Yp_ETxdTcHqzw7mFEh3n7boUbgFljbeDNCuv6XhTUrhCJ93ePbvN9cU87MmLQgxBEUOCSb47Ak7wUuxQwNln6kTqe8QHAkWsdNKBEtNeszbDH9riBSWYvTQWiYxZXfUOJ-SVYzxDN1ToyrIA7YxVB7IfM7-iCNakdgR4uzGrx7WGQpQ1MdaJutlkP3c-SuQ_oNmH_s_Nyujzw1Utmbw_xlC-9oDIn6MvsYKBGTSFeT2KWNIts1fyGgAhAeH6IXdczZY-wlEw6kMftUOu9bT-PlZmjw-PercZtWc9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
و بعد از چهار ماه همچنان عامل این جنایت و قاتل فرزندان ایران چال نشده و اجازه چال کردنش رو از قاتلش گرفتن!
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67323" target="_blank">📅 11:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67322">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5f6d58549.mp4?token=hOeWFiQOren9oMZpOX0wXCfQein_7C0PU-Wb6s8LrxvaXUc-I4-rDbiNjgUg_9bi25xXOh0VMzBcNQwc3vlwqL91UZ5WufoR3sesByl6FO95U9H87xezRyat1_3OPOIW60oz7aY55lVfoCM8bBo1mN9Nra2G59aVXAmn3EVapADLT0g_4qgakwtnLsQkWi8S1P04SFjvk5rHRTQjD8GGI9oDdTpus9By0vaI19nM5FWHaDdzI99R43XjSRvv3GtFSCHEXf-a96RWld99HWxZVLIQu9wJlj_y5UI-M5VhVamrKvXojRVA1aMxNFMoyFZ0IT6ojVqi0ezhW_H3mzMM7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5f6d58549.mp4?token=hOeWFiQOren9oMZpOX0wXCfQein_7C0PU-Wb6s8LrxvaXUc-I4-rDbiNjgUg_9bi25xXOh0VMzBcNQwc3vlwqL91UZ5WufoR3sesByl6FO95U9H87xezRyat1_3OPOIW60oz7aY55lVfoCM8bBo1mN9Nra2G59aVXAmn3EVapADLT0g_4qgakwtnLsQkWi8S1P04SFjvk5rHRTQjD8GGI9oDdTpus9By0vaI19nM5FWHaDdzI99R43XjSRvv3GtFSCHEXf-a96RWld99HWxZVLIQu9wJlj_y5UI-M5VhVamrKvXojRVA1aMxNFMoyFZ0IT6ojVqi0ezhW_H3mzMM7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی رسولی  مداح بیت رهبری میگه برای خون‌خواهی اومدیم؛
شما هنوز خونخواهی سلیمانی و... رو نگرفتید بعد میخواید اینو بگیرید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67322" target="_blank">📅 11:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67321">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5807c7f54.mp4?token=bieGEUlbpXw3lEKz_CrclZNufyAbXcKUpB7IomASeV6PkoYMtTSSirMtdZnLJs1gk1teAeU415dhBtt3b9JlY6LH7DBPJfpol63EUIGG9e4G_JGsYDbRC7B86Rhc7jwvcvKcNuYSBUG0xtOVwLeAAaOwRubqLWpbh8AV5awLjnw6081vceGFi8cf1mopBi6EntRNOF9YB3w8CTf5I5JQZexWxoXNg7lp-rSOZN_48MLSD_rlVUYSik-wn9bWdN_zigtFOzyTrVsJpUDlf7e0NmtRsIHOLMAALPy3nPUKHWKMEcMiHoyBNBECN8QWeqUgebRGW43l25Eq-oQMXaDRww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5807c7f54.mp4?token=bieGEUlbpXw3lEKz_CrclZNufyAbXcKUpB7IomASeV6PkoYMtTSSirMtdZnLJs1gk1teAeU415dhBtt3b9JlY6LH7DBPJfpol63EUIGG9e4G_JGsYDbRC7B86Rhc7jwvcvKcNuYSBUG0xtOVwLeAAaOwRubqLWpbh8AV5awLjnw6081vceGFi8cf1mopBi6EntRNOF9YB3w8CTf5I5JQZexWxoXNg7lp-rSOZN_48MLSD_rlVUYSik-wn9bWdN_zigtFOzyTrVsJpUDlf7e0NmtRsIHOLMAALPy3nPUKHWKMEcMiHoyBNBECN8QWeqUgebRGW43l25Eq-oQMXaDRww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف یه 20-30 سالی هست درحال گریه کردنه
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67321" target="_blank">📅 10:45 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

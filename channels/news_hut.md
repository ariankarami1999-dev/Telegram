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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 21:55:52</div>
<hr>

<div class="tg-post" id="msg-67431">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfyhFX9D5znAsE8eNpgIQ7rnhS7O3mLvFFjMpit_DKsYJjcAo_5oTl7QiXHRa5AcV_BrimWMfO89YrA3fgQGyadtHUTgndBDLOZtpkqKhTOpyNaQRbaFtzzdT6moFztxUwpiZnW9UTZV_gX6VPjRQv8lCB79gO1x2t8FDg8ZRezQS14_VpumiWh9hsfIkE0MsSt_CH4M3haX1kVSq18bz2UJvSdLsb6jKdpww3F3TeEyBr_aRf0uQFba4ru5pbmMpa0_dlmfbwgvY52D1ztL0DUaW8px4Vk9SXq4G85wSf-Davwn4ejav-O5YaJQlvAGcm3DiwZgwj2dHef5yRjJIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/news_hut/67431" target="_blank">📅 21:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67430">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/news_hut/67430" target="_blank">📅 21:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67429">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUP2BOpSR0KD9442XTCpCSm3G27ahAcY_U8PmAwJ7e52EHHwX_lX_80uLEiZZ3rmGHMB3TBaoF2zQvJHKzDW-eQoOTyt7B7Hz1qIrCp4WkPC_pbwSPcRcp2KVeapHE86Pek1GUh0sSssRLFGkTm6xP1XdQ4xXvDUpnuFRjZbmIWQwU4mdhQjzDz5OByzprg51ZJtnMB_Ae9RCEuPCD_P-SNqnlNcFrN5WxqdRRwgmdUi3vvxrVhLE-GsFfW08LrcI12UN24Qv03tNuqOvTGdqiH-nk5e7WadI9uENG-Gc3jaAFe1u2h87pMM9avENh4i6fYwDsJbRdtgnqcG2RMMCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشه یه دختر ۱۸ ساله از فشار کنکور و امتحانات نهایی و بخاطر فشردگی امتحانات رگ خودشو زده و خودکشی کرده؛ این پیام رو هم قبل از خودکشی منتشر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/news_hut/67429" target="_blank">📅 20:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67428">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDbMvRfgkISvMuZd03tzaAkrLA5Dlacc_A5GcI1WksB8aPUrkqbS3g-7UIXRuLgQevU4xNTX0M0PyCB6bAqQV5BvoByLaO_Or1ATnNuhggC0T5LYhIot4fiQ1QFLbccNbIlOoSn1IJ7rCOnxYihgfhrKRT2lce321N0VnhXJP_cLdlbhagDYiYyZil1QMW-lr-kSj9KgPLxdud-gww4XkBemRC6kUuCpj2vpsI7FXjLoadWLAV_SQ_Zpb6qxgw_oV0HBhpSPeyVazUA5dFCtIHwolCyXwOOns9XKaaPtOJlzoroScl9wHjTpCDA84iA566RMMb2S0WDX_a2tPMwqVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ان‌بی‌سی به نقل از یک مقام آمریکایی:
ایران شب گذشته با استفاده از دو موشک که مسافت کوتاهی را با سرعت بالا طی کردند، به دو کشتی حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/67428" target="_blank">📅 19:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67426">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GqbLTE-BTczhtrIIoBKAZ2_6dQWaru8Tsu-6SGzJdeZw4_Uz4HbTFjLc_rJ1YQFm-1aDndtDWS-2IqEOxa0rnlZ8BcN1A_qMUYkhEFqgueeZmJI6CknGwWrvMAk9ir0EsID1y5PIn7VVDAaAMGF2z0OKS67AGCcxs7VQ73yvpbYV8Dwdmd6iD3Av5IKL9GjwRcEI6gQCXk1yn9JjDS0HO81JZIpeFPD8MeIeR44KoOZkJGD251RP47Xp3XvrqoVOmG52wdtjSgluENVQ6WuK3NBCGsHrHJAsHGkLM8s6Vs4E6B8eVDlmMkt8tb5jsc8IC7FXSqAziJD70RKaXmM5cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rpWhV9hOf7672TONyWDvUCiNIkb824s9mLLUx0KE9r_U_aq7vGRpO6cnjYwANQ8sd_MATEpmCouGorNMhSq6UjquIqyFfgLT9C7Q8op_FzACzrzUJ5wjjIiKEZUlGPF5-cbw-zwp3EVdI9Plmmbb-ct80nSuznQqSRshxot59n5Ul0NoZm1AtZ54Mg9a5VtYX2ajcQKBnxXGUMY9yJ_nt0bo9Z73VQp0Ap1P16FLnsjQngZqReXEqkixnwSubSyTv5_WA21XSA9eCFrvZg2xNiACsQj4cYVc-e9FG4TaLfmZB35HkKffV5JnDkKGY_TB15Bt3rejFTiWtitv16s5rg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
صدا و سیما این تصاویرو با زیرنویس جمعیت میلیونی مراسم تشییع منتشر کرد :
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/67426" target="_blank">📅 19:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67425">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/67425" target="_blank">📅 18:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67424">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GOB3J9qdHkd1ZKazpc7lmXW5lY14nQdpWQEDNaorB9T9dizWADwADq_We5BzSqrs5VB08b7Hj00mRbaAsca1KCx2sM7N26IufXlvv5l-2xoqTmV8P7CrKCGEAn10_nGeKLPUarnGKzGEEJ1FyJmRBkst_Sak_LLqwKuGgjCRlls-CAAdcJ44gaFddj5pm05G-1Rj-RyF6tinivRUdzEG0CGRVFGe6J0RYCll-U0rvTz36LjAbjuaMqKK5PYJbg9xBVs1a0bFCxQyQk_MaHuVJ64idDZDLX6t1eOLi4Wrdi9rxQ3nAph3LGOkl4wKiqrkXEcNvtOlLvA9hqYX06JG1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سازمان عملیات تجارت دریایی بریتانیا: یک نفتکش روز سه‌شنبه ۱۶ تیرماه هنگام عبور از تنگهٔ هرمز با یک پرتابهٔ ناشناس هدف حمله قرار گرفت.
این نهاد اعلام کرد نفتکش بر اثر این حمله دچار «آسیب سازه‌ای» شده، اما هیچ تلفات جانی یا آلودگی زیست‌محیطی گزارش نشده است.این حادثه یک روز پس از حمله به دو نفتکش، یکی حامل نفت خام عربستان سعودی و دیگری حامل گاز طبیعی مایع قطر، رخ داده است
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/67424" target="_blank">📅 17:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67423">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/67423" target="_blank">📅 17:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67422">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/67422" target="_blank">📅 16:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67421">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/67421" target="_blank">📅 16:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67420">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLAXqWArnxmMdoLI8Fl8jf_6XaNbwcgmocPEEvBrDIBPt-0PypG0BDgPjr8i_ZEtys3myqXSeUHgAmKYyJNyT_DHJG-GAXJ17mswryhXtHxkDSGQlSFA-9mS7OZqy8iWCOIWhmVD2qPP_rBrlTwSzf1nMZ080sCkNWT51H6XYu0wLvg8P4d12CdtJe1jVoKvMEcfjYE8vSA6W6MgdMamE8hOfPhJfTk6h6UITD788vXgk5ws6OjZj0Z30xVChAP5iXDJ43TrTeqZR8HrIyA2ZJfAxzj6cz70_ILNbyz45J09yL09LKsZDHogvg75O48RmCDYIqkzck9GRThpXg9khA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خبرگزاری
CBS:
علیرضا فغانی قضاوت فینال جام جهانی 2026را بر عهده خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67420" target="_blank">📅 15:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67419">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/67419" target="_blank">📅 14:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67418">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FufM9s0BnbhzEk_jQm9Q0Yl9GCV6tV1GCMCTG-VTMkGOfUR5RV8Ej4dF_9TfN9OYUuwvZJ3TxNH6hUZ8WQvriA-ma8hgvJtk25sYC1r9nepws5BkrvjKBKImA7pE7-6Sg-Xo7cUXCfjsskgAj5XFxceJ_X-cgvLJLseEbc0NsMuMfKtMBecyPWtzWae8tsjOavMAoWcnNYaddiII0BSH_hTi1SYb2KEJs_Zyb2Yzi3UrSud-NLwFmviw7bkFyxjj8sNTzWQFgK64r4jwC-m4WQHNNPyPRjqznIgHNg03Vw6K5ah9-mJiTPiHzAkwZCc5JWO7oF0UU_8khlOZ8FkNmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری رویترز به نقل از چهار منبع آگاه گزارش داد نفتکش حامل گاز طبیعی مایع «الرکیات» متعلق به قطر، هنگام عبور از بخش عمانی تنگه هرمز هدف قرار گرفت و آسیب جدی دید.
🔴
به گفته این منابع، این حادثه پس از گزارش‌هایی درباره شلیک موشک از سوی سپاه پاسداران به کشتی‌های تجاری در حال عبور از این آبراه رخ داده است.
🔴
بر اساس این گزارش، پس از اصابت به سمت چپ کشتی، موتورخانه آن دچار آتش‌سوزی شد و دود غلیظ امکان ارزیابی بیشتر خسارت را از خدمه گرفت، اما همه اعضای خدمه سالم هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67418" target="_blank">📅 14:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67415">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67415" target="_blank">📅 13:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67414">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67414" target="_blank">📅 12:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67413">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67413" target="_blank">📅 12:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67412">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIA5PEyeosPnqgWlH5qmCrtBek7hBza7JBiTAu4_GyrZwrBXTUaSKOfmJUiBeeHXBW6Mca9trsyQL4uSSHUEsI8bxSU2oEgIT6MVf1ceBJwmiXrds0844OfRqLH9ee67hGmUtsq9vIhJWPWEYHkYOls4ZAHD_u2iAptwaQFuQKSDlqtriyE3CskKEq92-ot68rQfbJnacXD7RUmrlCNntpNr92Wq4zeWrFXTT4VXa7cN6ah0byNsiTzW7WQR_0iYI6QfMVcDMlINUF6BocIm3x8oqhRtYhBoVHht6r1dwmI-gCV1G-Xpa6SgeMl-h21kt9O9jB7EdzCv6X-tiZPKUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس:
دو مقام آمریکایی به «اکسیوس» گفتند که ارتش ایران دوشنبه‌شب دست‌کم دو موشک به سمت کشتی‌های تجاری در حال عبور از تنگه هرمز شلیک کرده است و دو کشتی مورد اصابت قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67412" target="_blank">📅 11:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67411">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‼️
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
احتمالاً نباید این را فاش کنم، اما ما دو تا از بهترین نیروهایمان را برای محافظت از قاآنی در مراسم خاکسپاری فرستادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67411" target="_blank">📅 11:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67410">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/64666ae825.mp4?token=InoN07M2isUWRtnChPAxmn_FaS2se88-MnBwMqg2x9gSDgxksSuSymrt4SQMkNK4plajGqwkhg3wzS7ku4yNBwO-uqwNgY9Ms4i0yuQ1Rw1nhMDk1Yfn6oKB_Jh7vT6xqQVvzaLShVLCPaqaG2XmAkW3ULZ5bk0vU2w83bTUgjmaDpYhyN5QGU83QiZnUi1PORmFNzE0P11JKoJUtrSC5fHMC8d85fXfczures1k-hRvtrq6ZDjfBAoJUYxDl-bTajCI0Ow_pNiwP4upztD6Jmi9wtpABWT3Rc5Fjg73zMZy61zLlFsR2lMjjqhodB78xEyVuhqlQyT8nvYhZgWUYg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/64666ae825.mp4?token=InoN07M2isUWRtnChPAxmn_FaS2se88-MnBwMqg2x9gSDgxksSuSymrt4SQMkNK4plajGqwkhg3wzS7ku4yNBwO-uqwNgY9Ms4i0yuQ1Rw1nhMDk1Yfn6oKB_Jh7vT6xqQVvzaLShVLCPaqaG2XmAkW3ULZ5bk0vU2w83bTUgjmaDpYhyN5QGU83QiZnUi1PORmFNzE0P11JKoJUtrSC5fHMC8d85fXfczures1k-hRvtrq6ZDjfBAoJUYxDl-bTajCI0Ow_pNiwP4upztD6Jmi9wtpABWT3Rc5Fjg73zMZy61zLlFsR2lMjjqhodB78xEyVuhqlQyT8nvYhZgWUYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گفته میشه این شعارها علیه عباس عراقچی توسط تندرو ها داده شده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67410" target="_blank">📅 10:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67409">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbee8c865f.mp4?token=J1uE3oupNr9E0v4jfY_casFy3B9zoCrjxbV6gSFOmNuCtT8c4kgvlbAWTMrTpTbr4amGYz8H0ih12U4gyEGyQ8gQpv5vhv7CC9pwoiS7688E77IrTgZsWF8MjE0n-PH4rQtftEF7YEOp9bdD-C4dmi6P7C2O0cdv6hn2OHg7HeiFMv5zQsEFg0RmiSgLneEXcMbUbQAz5r2UbI2oliTrwXtsvOyhG4_JBUaOJ0WnRu5mf8SPXJku-4bDUi_iWn3IMEzy3jl_LmP8_rkdZwWXgDcCsHt55bjtEwLzGW5NyUO3oyMlrgwc0A3tQ1fgU6aBYE5kinrDttyJ21aio6-yTiMJaINge3LIK7J5R97eOPcXrxscUc1HlVWYYDFPYDlOqNGxiu_ndic6X4h1b3ycEtN0cie_1XqL-4Ssp4KxUZlX1iDRAlQiTCyvFJ3i9-0R0kzkKG4nj4iAo9xXhLV6YUUbUm8zXesRa2Z384b6swuprWlM8dmdaQ8sqd_mh1O70gS0epLqhSdoSxlroZqFLAVmhA6fyg7B3XvSM0NGUf4EcbyIEu1h-pfKUU1fm7GgpsTZUwhpZZayulbl_ZkuB3kl3O72L0yz76lHkGlittYJNH4pUazo_2RdHXO4rR1mGru19XEVn5CPWN8FY2MS6ifaB8WbnIm3DlpVzkbqE1U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbee8c865f.mp4?token=J1uE3oupNr9E0v4jfY_casFy3B9zoCrjxbV6gSFOmNuCtT8c4kgvlbAWTMrTpTbr4amGYz8H0ih12U4gyEGyQ8gQpv5vhv7CC9pwoiS7688E77IrTgZsWF8MjE0n-PH4rQtftEF7YEOp9bdD-C4dmi6P7C2O0cdv6hn2OHg7HeiFMv5zQsEFg0RmiSgLneEXcMbUbQAz5r2UbI2oliTrwXtsvOyhG4_JBUaOJ0WnRu5mf8SPXJku-4bDUi_iWn3IMEzy3jl_LmP8_rkdZwWXgDcCsHt55bjtEwLzGW5NyUO3oyMlrgwc0A3tQ1fgU6aBYE5kinrDttyJ21aio6-yTiMJaINge3LIK7J5R97eOPcXrxscUc1HlVWYYDFPYDlOqNGxiu_ndic6X4h1b3ycEtN0cie_1XqL-4Ssp4KxUZlX1iDRAlQiTCyvFJ3i9-0R0kzkKG4nj4iAo9xXhLV6YUUbUm8zXesRa2Z384b6swuprWlM8dmdaQ8sqd_mh1O70gS0epLqhSdoSxlroZqFLAVmhA6fyg7B3XvSM0NGUf4EcbyIEu1h-pfKUU1fm7GgpsTZUwhpZZayulbl_ZkuB3kl3O72L0yz76lHkGlittYJNH4pUazo_2RdHXO4rR1mGru19XEVn5CPWN8FY2MS6ifaB8WbnIm3DlpVzkbqE1U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش‌چشم، کارشناس مسائل فوق استراتژیک:
باید هزینه بالایی برای خون خواهی امام شهید ایجاد کنیم. کانال ۱۴ اسرائیل می‌گوید رهبرشان را شهید کردیم و هزینه‌اش فقط ۴۰ روز جنگ بود و دوباره می‌توانیم این کار را کنیم. این بار آقا مجتبی توانستند جایگزین پدر شوند، اگر باز رهبر ما را شهید کنند چه کار کنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67409" target="_blank">📅 10:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67408">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7142559e9b.mp4?token=qF05nh8tcTnLZwYpjmWt_twS5nYNN5d8Is59v0wffqp7vA9OkadxxSo-5-_dFBhSdX3QFEVo-EV4oVjSivyYB2Hl7Sa03m7sniiQq9rItnZuw51NezcOieTQz2z3vB_O16p2_GqevFL4O1KmbMYJ24IfJrXWWT9Gwz86OsdxCJjaOYUJvHqc6KdBcY5D4Tjocce2fRgRDNz8NNto1HEVhugehwJ1fM3AUU9DtEmkISGUrwgGr8gnGeC2_j0JZBSIHXJxmqFRzp3XdCc4_fBy29jWe0t7rLVxHo52GrTfNLOovtVobPDZIu61jBMDyNH68k0NhTd0QEnbkpL3aH31Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7142559e9b.mp4?token=qF05nh8tcTnLZwYpjmWt_twS5nYNN5d8Is59v0wffqp7vA9OkadxxSo-5-_dFBhSdX3QFEVo-EV4oVjSivyYB2Hl7Sa03m7sniiQq9rItnZuw51NezcOieTQz2z3vB_O16p2_GqevFL4O1KmbMYJ24IfJrXWWT9Gwz86OsdxCJjaOYUJvHqc6KdBcY5D4Tjocce2fRgRDNz8NNto1HEVhugehwJ1fM3AUU9DtEmkISGUrwgGr8gnGeC2_j0JZBSIHXJxmqFRzp3XdCc4_fBy29jWe0t7rLVxHo52GrTfNLOovtVobPDZIu61jBMDyNH68k0NhTd0QEnbkpL3aH31Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش جالب یک مازندرانی به حضور سعید جلیلی در مراسم تشییع علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67408" target="_blank">📅 09:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67407">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcgPScQ9Kw0-gIVNE0tm2LQs_1-3T2ZSsW5JvC3lBLcvPUTnyI8EY-8LJ1Mbtqaq7UuW-yl74brixxvknrqxvdUPSa3-VnsdsBmiiDMDiDZliSOaVPubSkt1ixBfOQnqqcm1GwlaA3BeIveiVZM0uiDoo8DP9hqT75sRoy8ruMLxw6WxDbhazdZTCcNT4WxndWpHwgT2omrsdWaBpu2jqdwDGwydKyNdgEOZuZjeDF14NHQvzALVgpPSMppdKfTwVMiWFeR_7bxP4RBQsLGq5aEq6-WfX5ORbY8YM3G3LDMzWeF9wEDp8pkCqsZc1E4kETav_AXGAB-8mpQZWULBxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
❌
مرکز عملیات تجاری دریایی بریتانیا:
یک نفتکش ساعتی پیش در فاصله ۸ مایل دریایی شرق «لیما» در عمان، در کریدور جنوبیِ تنگه هرمز، هدف حمله و مورد اصابت قرار گرفته است
بنا بر اعلام UKMTO، این حمله باعث آتش‌سوزی در سمت چپ کشتی (port side) شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67407" target="_blank">📅 09:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67406">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67406" target="_blank">📅 03:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67404">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B6-aCKVud-Qyhng2GCgOKILBfJZKheMmJVI5R8jEx2nUE3FQgak31dZv3PUWDu4ucSiOPtq6sylBe7yYA5wqC8Vx8-xQtIeQptT6KdkIlRDU4pCNuWDSbqJEB694ZsM0jRKFhgbWJ_DBPk2bSd4MBaDYK_4Nbwd9gSBfhROWixgWRvbZZaZdQQNOIAnJCm2k9rlSqf3h5apkgcCEK8BeAk7Dsu_VXjvpA8Pgw6aQ4XrdYukxOUTOj_n3RzIfB1u5gfBrnXD8-4ybroGWVNGszr0-7d_NMraJjaTdlx1Ylj2p5WAY3oIVoPsHjSBHoM0-YmwiWazW46Z-t0F55R5N_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67404" target="_blank">📅 01:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67403">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiVWJX3yL_B7UMwGBgz2cGtIFfHB7SMTopjKIwww7MoglXhRWfHsRjU7pQ2k3BMc59q0p3TUNHS0iaQY4mmLdiQnIIbqOO9akhhNKwIio66tbdBp415WzE6RZfNx1VVQh4AT2uijUhvWMgWdeIb0eAB3cbagCFSbMjlcp4PSwxxhdLGs8SkuPsp2s58M_Q8unGVlmjQ4uxa0HTTPbW8pa3EHOobKRqwnAu9UoXnY5bwN3dJESWGZQMb4FW25wN4A5_T71qfsZuvmP2_ZsXzlqBJiI9lDeLiBciW0gUEKCeKsnl6lanoGscCyUCMeWsAJcPBEMvuaIhcdAULzzB1low.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی 2026
| حذف کریستیانو رونالدو و یاران با شکست مقابل اسپانیا در دقایق پایانی
💔
🇵🇹
پرتغال 0-1 اسپانیا
🇪🇸
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67403" target="_blank">📅 00:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67402">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mps1SnQLG6sDAPxu3IzydfuryEl1uOnUJNWF2CKu2-XreClwZhWxrgA6km7m0_Zowhly5HcNPBS34posu_lEfFnS5aENxDC9oyd9aJefhQ7yr6_ESJgFGyjxFtLUDcCqzuEyeLuEYEYZHfDrwR7OjkVXYeRUL7Nu1M9h8PIdRQ6besIxPxDnYNQS5AJJOsp-wEDv-GrYD3qM6kQAlx9o5f6iMyqjisL4RsvbC1oeDXziD9BB9cZRkF_2_ZXn1cmhDLEF-iHDYCA3oVzhXX6ntrcgc9a7SeL-_3WIobH79lenZUUzkoO8v7ll1wqAcrw8swU7w4O_AOIiRd_Uy9qr4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67402" target="_blank">📅 00:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67401">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/781360aa4f.mp4?token=pdHWIDYMEjsaOHlgVTGKHnL7EmxycbsHlgq5GDqRu65QPAGBcoV03Vzbap66RdyyGCcgy1na6kvyWnrXLqhxgn8u1-XrC7vJhEKzp3oncSnZuodc02uwA_ylxhRBfWPpEQ2r3f_nGfSNFmMtq35U5Qmpl_nmsaFIsjrrDV_EXRPlE-vcGBJ-jcboD5QKb_jiwRrdKPJzbYcdbvnzUNZpbQwmuJ5bRfc9sNvDjwKhrs0a-h0EQDUg74an88u-nY6ETS3zQXGMcrUoqvsQvC62GLZ7jkCPuYYrWE2DkMDOY-x9T2MuncYXjZe3b-tE7m3Qod5k6vqU-CG8MDMOE4ug4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/781360aa4f.mp4?token=pdHWIDYMEjsaOHlgVTGKHnL7EmxycbsHlgq5GDqRu65QPAGBcoV03Vzbap66RdyyGCcgy1na6kvyWnrXLqhxgn8u1-XrC7vJhEKzp3oncSnZuodc02uwA_ylxhRBfWPpEQ2r3f_nGfSNFmMtq35U5Qmpl_nmsaFIsjrrDV_EXRPlE-vcGBJ-jcboD5QKb_jiwRrdKPJzbYcdbvnzUNZpbQwmuJ5bRfc9sNvDjwKhrs0a-h0EQDUg74an88u-nY6ETS3zQXGMcrUoqvsQvC62GLZ7jkCPuYYrWE2DkMDOY-x9T2MuncYXjZe3b-tE7m3Qod5k6vqU-CG8MDMOE4ug4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعارها برعلیه پزشکیان
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67401" target="_blank">📅 00:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67400">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتلوبیون اسپرت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m10NHq1jQ8oEyuUoDXPeMn-H8GGQrGwDaYyuJkPBrMnIYg2WI1xY2kVxFyBKVl1VP_5iZPOJEVPB7y4ajh12lQClF9EwohX2H1mQcUu6z6n9WMnrp_DZvQv-aRyYbWFJvKszuyfI0P7MgY41T0XNOttvOBug3ljXn-3JeHAnzHCWw9WmdSryWQnp0oT1kE4FiZdn0RHhpFpAP_mkbmmgmKAuRRCWrq9lJmgvZ6pJzFNe7rla2FTIjbj8oGEnno7siOnJNo6GFhnLWtR7PlmwfDWnddLhTJyVjD1_1ZWhvCCaIdFPAvY-R25p9gp-1lut7i-AnscYSY9XeZaqBKWQcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67400" target="_blank">📅 00:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67399">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/733e727650.mp4?token=VCRNO2aossKugLX2kpfJF45GGc6skKBDDZMXjmR65-beiJbH4q4DknHjQCSCPnEHeKXCV8b4d-gkOJFIIO7BhCn8UzR0JN_EQD7LRM13-PxcNbUSDzkQiBHHkPvhTPSWItoAujiSTJfkCUaDwF5dsmcn8FnayvxajbehQvXCYCvhrR5eTJJ8sksls0x6oVJ9qpN0TwiI2t6gkFgZNWbGUdxxVKd9f55K7e2Cn_0NwJCYtIQAeI5ot23RulhOI7VYrXfXw06lAntIO8fvZaoJrhPeNraqeG6eA3TDdzDI9eYtSRT84Xase1nKLkSM-Dfem8_URH-_dtnj48dOxzVaqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/733e727650.mp4?token=VCRNO2aossKugLX2kpfJF45GGc6skKBDDZMXjmR65-beiJbH4q4DknHjQCSCPnEHeKXCV8b4d-gkOJFIIO7BhCn8UzR0JN_EQD7LRM13-PxcNbUSDzkQiBHHkPvhTPSWItoAujiSTJfkCUaDwF5dsmcn8FnayvxajbehQvXCYCvhrR5eTJJ8sksls0x6oVJ9qpN0TwiI2t6gkFgZNWbGUdxxVKd9f55K7e2Cn_0NwJCYtIQAeI5ot23RulhOI7VYrXfXw06lAntIO8fvZaoJrhPeNraqeG6eA3TDdzDI9eYtSRT84Xase1nKLkSM-Dfem8_URH-_dtnj48dOxzVaqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
عجیب‌ترین چیزی که امروز میتونید ببینید:
نیسانی که با یک چرخ جلو بدون مشکل داره حرکت می‌کنه و سگی که داره راننده رو قانع می‌کنه تا دست از رفتار‌های کصخلانه خودش برداره
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67399" target="_blank">📅 23:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67398">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aad6611348.mp4?token=JtjgRYw22oOp0oVaNaPB8rq3IpSu5vHoD_C4cazfdOhwcrTRW2ek3t9EEIrgY3SCTy5pLorBiY3MXA2ZncRYkXuWvqY6bRgrs-wvUwMMBMTb97BEnGYVQipXDY3HuUG26eWe5EE5ZOT2MrqIX8bNhMLJ--UQn8J9W-0T0ySY9BjWzpNuVqDrWd9pZzQByGi1SCV1XHSPD8jxGZrMDdMKzIRzcr7WUHQKAEc-Zpq3yGhQzbyKmUbN1VuHHnRYC15073-uytkg2wokv4_kbJpOOc-RDXk_wDoZNUxglxZt95HtKThG0MTdCTMCw9n3k4F2oLpd-8EeWqkAwTJcbgTSrYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aad6611348.mp4?token=JtjgRYw22oOp0oVaNaPB8rq3IpSu5vHoD_C4cazfdOhwcrTRW2ek3t9EEIrgY3SCTy5pLorBiY3MXA2ZncRYkXuWvqY6bRgrs-wvUwMMBMTb97BEnGYVQipXDY3HuUG26eWe5EE5ZOT2MrqIX8bNhMLJ--UQn8J9W-0T0ySY9BjWzpNuVqDrWd9pZzQByGi1SCV1XHSPD8jxGZrMDdMKzIRzcr7WUHQKAEc-Zpq3yGhQzbyKmUbN1VuHHnRYC15073-uytkg2wokv4_kbJpOOc-RDXk_wDoZNUxglxZt95HtKThG0MTdCTMCw9n3k4F2oLpd-8EeWqkAwTJcbgTSrYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فحاشی وحید خزایی به خامنه ای
رادان کلاهتو بزار بالاتر!
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67398" target="_blank">📅 22:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67395">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nNGTdw4IXvMd_8BRvg26DOJt7vOJ9E_adRWnNaQqO5XwB2j84tEnWfEipVqTZ18FBb9l9WQJgOAc6zow2wvLDCYnzus0kDxbmU_lGSOeQVnR4UJRt_Cbey3VzgGQBi5MkB2kkxWZ7nvKqEBCmR37b5QzJVGH2CbpvRxkWk1U16Yi1yNJF0UJ1iENqr8XSSb2nxUXN0ozNOXEzlyb8GErXV-rqlOCqVWKwrbRnYdINFP_AZxtkQA1nDe7UE3XxJHBnqQKcZ0DQzZsrsJjHkiEMDxbku2eDCG-P2RWq0IbXi10jdRG_qsbgXaU_tmExDprF949ojEfNs3nhHdm6j52KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AoBkSgGr36DfVYr9Bf1AEUdCITgyQgf4z85jwHeLF17lNsqXs3j3iDJw85GqZsLGh3ig_heVHIOOKcaXYEXF-RzhFOBcWcQ9HZMuCIEXynsrCiuXseI7ZQUPKhJEexFBsn-oS9ggejveJ9_-kKcBycb5gLPETDFajefDMYvLZcqnMe8YzxsreqePs9qXT_kHWQnDaxGjpn9PvHHMgxGUeHAWOtL2KOFsvaABDEObuqXceUMSC9xexE9GQaFDBZYMQWRUrr5M0RZBKFs7CDg30F8hgNZmyOUgDyvXgx7gXJ3bwu40tqETg_zd5o_twgQwnud3XrW2El-5JoTH-ZUbnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/886967cfe3.mp4?token=V_NxyWIRtugn7dSy0CGO1vW0mG3jnUOoPD_j-VUIfrxAcqGxcTa26MaweVdVLrvBmfY9faVSsx7YqpWK5NXxHbwO6JLfKe_5XLknik6D1lHY5huBYZ4P3qqOS5Y52sVXbP3Xd_v4BrVHTzwpNPrqJFm4jpc1OjvT3zTQX6sZZWS4MM_guXbhpuGFE2YKcODooxepMbSoPNk-KjuQ9_J0LCmd1VXC_zArX6kY8q9QpVskxIZroVQd_4pevFOi-0iPQOCcH4ujg9li7FX9GxRlb4tzKsJUhXtazLAfLTloRx9bDLpkonsH7kNsqkiUrKghWDiKuxHymu8yRpkiHDQ-7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/886967cfe3.mp4?token=V_NxyWIRtugn7dSy0CGO1vW0mG3jnUOoPD_j-VUIfrxAcqGxcTa26MaweVdVLrvBmfY9faVSsx7YqpWK5NXxHbwO6JLfKe_5XLknik6D1lHY5huBYZ4P3qqOS5Y52sVXbP3Xd_v4BrVHTzwpNPrqJFm4jpc1OjvT3zTQX6sZZWS4MM_guXbhpuGFE2YKcODooxepMbSoPNk-KjuQ9_J0LCmd1VXC_zArX6kY8q9QpVskxIZroVQd_4pevFOi-0iPQOCcH4ujg9li7FX9GxRlb4tzKsJUhXtazLAfLTloRx9bDLpkonsH7kNsqkiUrKghWDiKuxHymu8yRpkiHDQ-7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فیلم اول تصویر کوچکی از جمعیت یک میلیون و هفتصدهزار حجاج است که امسال برای حج به مکه رفته بودند
مقایسه کنید با:
🔴
فیلم دوم جمعیتی که روز شنبه ۱۳ تیرماه، با وجود واردات عوامل جیره‌خور نظام از ده‌ها کشور در مصلی جمع کرده‌اند
آن هم در تهران با جمعیت ۱۵ میلیون نفری!
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67395" target="_blank">📅 21:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67394">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1d208e49.mp4?token=k8WB5T46hOGtv-7v7AsUEbNDm8mRUo9EZwUAHzntCGk7DQf5rJViHlEj7_DXcCXTgH8KMDPprFrA2-er8R3GJgKnKldzVMjWVTu-12Xvc5NuoHy8c-CJFTaPKudhXx89DtOn9Y1dpoJjZOSCaKOprdkAJrN1o3mQ3sgAQCLX7S90t28m2u87nYsOUk8wYnOJKffnKiNEuIKiQ-z_ps-CWtKTdj1t2skuvW5VGvjPb3NQgSqe7Emx3RyGnh5iJQgmQNvsn9cwRcSgo4JAJvTW4GqySWYm-iCOg7g4yFOPsnLoLrYartxU4gF6i6ah-Ep3sBXSgSEhs3s1XxvJpawUCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1d208e49.mp4?token=k8WB5T46hOGtv-7v7AsUEbNDm8mRUo9EZwUAHzntCGk7DQf5rJViHlEj7_DXcCXTgH8KMDPprFrA2-er8R3GJgKnKldzVMjWVTu-12Xvc5NuoHy8c-CJFTaPKudhXx89DtOn9Y1dpoJjZOSCaKOprdkAJrN1o3mQ3sgAQCLX7S90t28m2u87nYsOUk8wYnOJKffnKiNEuIKiQ-z_ps-CWtKTdj1t2skuvW5VGvjPb3NQgSqe7Emx3RyGnh5iJQgmQNvsn9cwRcSgo4JAJvTW4GqySWYm-iCOg7g4yFOPsnLoLrYartxU4gF6i6ah-Ep3sBXSgSEhs3s1XxvJpawUCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67394" target="_blank">📅 20:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67393">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e3a38b86.mp4?token=kGyVyh8eP_Vq_yBTBSZnTLVBG1vNedlKTDHXwSMk7nuWLN7koymREPoWZycxp0F-rzop2fcGSpQlOt5n6Iyof-8PRLK-Fa9v_PNJ7UJwIAp6ghtX4upnBKEpDk1dF51nDctexP2TNP5nDcpGFthXaIvTS75E1zG2m_JO_9HKDPxKpMBLoO_TYeotHkXhKT4zFAI5Tv9Xp1JDkmhAKPTtdbXL9UChR9ztfjPaujVVtn4jPqVf2IeeCZFM7L9dSRHlOB8m-hbM38Ekx196j-beg6546lgMgI0m4JQoHfDL8f8blSkrgoRT2KbkBdhGM5NfBcA6zrXpERIBrJbzO90INQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e3a38b86.mp4?token=kGyVyh8eP_Vq_yBTBSZnTLVBG1vNedlKTDHXwSMk7nuWLN7koymREPoWZycxp0F-rzop2fcGSpQlOt5n6Iyof-8PRLK-Fa9v_PNJ7UJwIAp6ghtX4upnBKEpDk1dF51nDctexP2TNP5nDcpGFthXaIvTS75E1zG2m_JO_9HKDPxKpMBLoO_TYeotHkXhKT4zFAI5Tv9Xp1JDkmhAKPTtdbXL9UChR9ztfjPaujVVtn4jPqVf2IeeCZFM7L9dSRHlOB8m-hbM38Ekx196j-beg6546lgMgI0m4JQoHfDL8f8blSkrgoRT2KbkBdhGM5NfBcA6zrXpERIBrJbzO90INQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سطح عقل عرزشی رو ببین
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67393" target="_blank">📅 20:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67390">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vDCZmWszgHCPNKqCcQCigq_qzMMcxV9-jHJyTasO0T4Vq6TdOmgrPNGHxdbpXHZsWtnEjBh_ZbFN-r-r8AYUsATp-d9aXsW86OVkjdGQRl5h5RoBP3l6lQHuxFa3gaImHMK173ap8h7OzYriWgX1kHxgaQbgMTsoxRa-4wWoWskXLCCIqh4ndUqxxlo-bdCFBBURXXZxLWufsQ7NPQaMcsbKicTs56DW6KP2wYAhsdaGOgHzuWIG5_SqZnF1e4CUVAhMKi_DTB7f4PsOVfabKCTJm6rr4pq0gEOhqcbsYAMW6bTfIA3Zey8MZEQcbu_QokW9-nD08I-I7Zh2X09gdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HhSZWkCkejJzV2OXuTJBVEMkAfH5PgZT5pmRs3U-9bXufEAfaJIOTiadE3JDLwG7wwLi6sZpe21f4daFfszcj99BuGi_jpEfKPwOMH1RfjXcPB3bS0-EKPtVwKIAAJXx2XdKg_85E0AwxThDbXG_hJ8LS7aRQfNYgvweLHsLH41JyzPonfalQ8cDDiebLf5EARGDo28yCQIWU7UlHzSzmQ4jBBAnaa2Ai-NVaPcu3gaiMMN8ni_gSENgTy5GNFq0mMY4KbgiXi0_2OF6A_y8A5qU_7t4FC6rzg6DPYldfUoLLh73B8F4Ekp-6uEdZxcUCW7K9hNNkcDOPYHTI0aQJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bea0c04d9.mp4?token=arKAChI4Rqxb_2Uzqv_9e8w-flQZig6wuRCWgNVQcd4alFNznSUafwaYSRTzr2v0kmsfVHE8-aEvt3eEymCR7qj702UD_0TntKSFZWffzZwrMp2P9PC5gMWrHgKY58_ZNYbtILaiLQg_LI452kHsZqpVfUdLjL20DvsImVqjBkNhGWAJ359u8JMe1WCGEALu1lTOe8XO1a6Ocw3s9wTl_q168h2ZFpazL1AwGm1F-HIoXGJ-plWK9KMI3rXpwhZPyu-KxVpAI6X9TOBWLemVQ3ZYdiufUzJxEYXPyeXdDd_sI7Os8pLu1IUn4M1SthdbJaw27n-REL4GJW4NrAWgCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bea0c04d9.mp4?token=arKAChI4Rqxb_2Uzqv_9e8w-flQZig6wuRCWgNVQcd4alFNznSUafwaYSRTzr2v0kmsfVHE8-aEvt3eEymCR7qj702UD_0TntKSFZWffzZwrMp2P9PC5gMWrHgKY58_ZNYbtILaiLQg_LI452kHsZqpVfUdLjL20DvsImVqjBkNhGWAJ359u8JMe1WCGEALu1lTOe8XO1a6Ocw3s9wTl_q168h2ZFpazL1AwGm1F-HIoXGJ-plWK9KMI3rXpwhZPyu-KxVpAI6X9TOBWLemVQ3ZYdiufUzJxEYXPyeXdDd_sI7Os8pLu1IUn4M1SthdbJaw27n-REL4GJW4NrAWgCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
پهپادهای اوکراینی اوایل امروز به پالایشگاه نفت اومسک، بزرگترین پالایشگاه روسیه، حمله کردند.
این پالایشگاه در فاصله ۲۷۰۰ کیلومتری از خاک اوکراین واقع شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67390" target="_blank">📅 19:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67389">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee21b0d93c.mp4?token=gepntNXHGWewf4efH9oCLEz5_bCS6kHJy4AR83bQfhHw0lmgJAlns3XSZYwPW_5TmFu5YRDN-jqHOVxzMuGAmVDA98tHryfLDe4OG9_oCVC6W4KoChxWKDnHtSaBQB4wvu3lFZmHmtOqhRJCBauN8pGRth1PcOxh5u_2ailcJtC-lIEsVBwoD1Lc4q1ONY-7YBkNppyirxwg29dVuS_0YKQh3tJX8efWCEPNGCNFO6DhAUhBQvLAY9HDqB4Nnipotj8jAseZjfARD2mHY6mjNCAzZI6_ZnIVgWqFDe-SJ0q7pJvvYPDjfY0VYefUYNAgtcEvCG5GXyBm1Vj36C70lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee21b0d93c.mp4?token=gepntNXHGWewf4efH9oCLEz5_bCS6kHJy4AR83bQfhHw0lmgJAlns3XSZYwPW_5TmFu5YRDN-jqHOVxzMuGAmVDA98tHryfLDe4OG9_oCVC6W4KoChxWKDnHtSaBQB4wvu3lFZmHmtOqhRJCBauN8pGRth1PcOxh5u_2ailcJtC-lIEsVBwoD1Lc4q1ONY-7YBkNppyirxwg29dVuS_0YKQh3tJX8efWCEPNGCNFO6DhAUhBQvLAY9HDqB4Nnipotj8jAseZjfARD2mHY6mjNCAzZI6_ZnIVgWqFDe-SJ0q7pJvvYPDjfY0VYefUYNAgtcEvCG5GXyBm1Vj36C70lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ در مورد جنگ پهپادی:
چه کسی فکر می‌کرد که پهپادها به چنین عاملی تبدیل می‌شوند؟ آن‌ها ماشین‌های کشنده هستند. شگفت‌انگیز است. شما پشت درختی پنهان می‌شوید و آن می‌آید و شما را می‌گیرد. و من صحنه‌هایی را دیده‌ام که نمی‌خواهم ببینم و نمی‌خواهم شما هم ببینید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67389" target="_blank">📅 18:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67388">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02a06527a7.mp4?token=UPT9PeIT3LVjNHLq4IR82FyyZzY08f3n5Qy-4ddwmspIVAz5yJQwBFRlBI0Zd-XJyuqQu-1icv0_gx6xxQlic3FxUM-86bKgrQm9vm9cN0lem5K7A5-EtqV4uTCWfvN2pHkQVQG-zsFx1pdOFGBQ6fKQwrv6bRTKRUXAcxOvvVU39xz1yqNoaF741RzqRWQ2MxqHBj1-mc7drdRzbuk9eTSS5e0yuE-YgW7-5tUFlC3dZQHx1_SqoSUwpfhBysLzVRDzqtNjrfSVJFTGowqcq9xACVPSFV1MNqgJjG55apziWOayVrI5W-GnOLwzMG0l8QWibdm2lCvcHHSnvt9hGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02a06527a7.mp4?token=UPT9PeIT3LVjNHLq4IR82FyyZzY08f3n5Qy-4ddwmspIVAz5yJQwBFRlBI0Zd-XJyuqQu-1icv0_gx6xxQlic3FxUM-86bKgrQm9vm9cN0lem5K7A5-EtqV4uTCWfvN2pHkQVQG-zsFx1pdOFGBQ6fKQwrv6bRTKRUXAcxOvvVU39xz1yqNoaF741RzqRWQ2MxqHBj1-mc7drdRzbuk9eTSS5e0yuE-YgW7-5tUFlC3dZQHx1_SqoSUwpfhBysLzVRDzqtNjrfSVJFTGowqcq9xACVPSFV1MNqgJjG55apziWOayVrI5W-GnOLwzMG0l8QWibdm2lCvcHHSnvt9hGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ درباره کارت قرمز بالوگان:
من درخواست بازبینی کردم چون فکر نمی‌کردم این یک خطا باشد.
این یک نفر نبود که به صورت کسی مشت بزند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67388" target="_blank">📅 18:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67387">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e1e1775aa.mp4?token=JF6dfrQqzQky3oXdsV4zW44_dpD7dyCtXeCaEO7EUpgY5-kPH3zkVYGaidGMNvNMoRgnIlnukFcEwooz85TGEXmzfEmw4kjSNAKFpVlR_UcSiPuQZ7fXL9xLzWPCOPriqpq07JUYYjZ4DZSu3ikVcXuy0KUO47_bKyqPp0xTurQocInP7W2szPJpbiD3TZwP7YOjHcqIKOXn3-kvpJ_ZFV7saRsUme1lHQiQb1_QzjKf_NJLG9PZEIwcKjB-PwnU_ToH5-lhwr2mopFsgGSoJblLHAoShdvoZaOuUWsD-MwxCY2Y14FghOzkoZHR-15-jM3TZwxnBs4rDPLcNqip_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e1e1775aa.mp4?token=JF6dfrQqzQky3oXdsV4zW44_dpD7dyCtXeCaEO7EUpgY5-kPH3zkVYGaidGMNvNMoRgnIlnukFcEwooz85TGEXmzfEmw4kjSNAKFpVlR_UcSiPuQZ7fXL9xLzWPCOPriqpq07JUYYjZ4DZSu3ikVcXuy0KUO47_bKyqPp0xTurQocInP7W2szPJpbiD3TZwP7YOjHcqIKOXn3-kvpJ_ZFV7saRsUme1lHQiQb1_QzjKf_NJLG9PZEIwcKjB-PwnU_ToH5-lhwr2mopFsgGSoJblLHAoShdvoZaOuUWsD-MwxCY2Y14FghOzkoZHR-15-jM3TZwxnBs4rDPLcNqip_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ درباره بالوگان بازیکن تیم فوتبال آمریکا:
بالوگان بهترین بازیکن ماست. او کارت قرمز گرفت. من نمی‌دانستم این چه معنایی دارد، اما بعد شنیدم که به این معنی است که شما نمی‌توانید در بازی بعدی بازی کنید. این بسیار ناعادلانه است. چگونه او را برای بازی‌ای که هنوز بازی نشده است جریمه می‌کنید؟ من درخواست بازبینی توسط فیفا را دادم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67387" target="_blank">📅 18:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67386">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af665dba5e.mp4?token=NT9pnKPH7flBin5L2Sq-Jee46GcmisqNaPbaRsQzBnHA_CzEdeh8Vw9UfFhDFb_x3ROhrxEfsT0hK0d9bAnFg_REVCmMyfoaI-hf1HozUT9v5NsFKV_NvpZ1MhOtyvDTBTxwhzu-ps0qb6RPrLqf75O-v2gzHXsHI8AMvhQ3MsU8oS77x6prJrjiLVzBz5Ix_UVpMPlMhW6cxejwLYaGIZXDY6iGhOWQPr9wzSEQ6-oowhxjVu39JJVrDxWTGcQUXHzZHhMzbvNV3PwFAnfCG8bAVmPXGm4mLsQ-FIHhXS7KxdzdRi_bIVh6SGolBhlRMUuBPl5efJEmc502LDdh5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af665dba5e.mp4?token=NT9pnKPH7flBin5L2Sq-Jee46GcmisqNaPbaRsQzBnHA_CzEdeh8Vw9UfFhDFb_x3ROhrxEfsT0hK0d9bAnFg_REVCmMyfoaI-hf1HozUT9v5NsFKV_NvpZ1MhOtyvDTBTxwhzu-ps0qb6RPrLqf75O-v2gzHXsHI8AMvhQ3MsU8oS77x6prJrjiLVzBz5Ix_UVpMPlMhW6cxejwLYaGIZXDY6iGhOWQPr9wzSEQ6-oowhxjVu39JJVrDxWTGcQUXHzZHhMzbvNV3PwFAnfCG8bAVmPXGm4mLsQ-FIHhXS7KxdzdRi_bIVh6SGolBhlRMUuBPl5efJEmc502LDdh5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
یا قرار است توافق کنیم، یا قرار است کار را تمام کنیم، باشه؟ و تمام کردن کار سخت نخواهد بود. ترجیح می‌دهم توافق کنم چون نمی‌خواهم به ۹۱ میلیون نفر آسیب بزنم. می‌توانیم پل‌هایشان را در یک ساعت خراب کنیم. می‌توانیم تأمین انرژی آن‌ها را قطع کنیم، تمام آن کارخانه‌های بزرگ که ساخته‌اند، بزرگ، زیبا و مدرن. آن‌ها اکنون هیچ پولی ندارند. ما به آن‌ها پولی نداده‌ایم. می‌توانیم کارخانه‌های تولید برق آن‌ها را، به قول من، در بخش کوچکی از یک بعدازظهر از کار بیندازیم. هر کارخانه‌ای از بین خواهد رفت و آن‌ها این را می‌دانند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67386" target="_blank">📅 18:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67385">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f387513a36.mp4?token=q3mRbfvzmdL6hcjlRjC4pYzvFjtnQvZnZwlUAlwGFix0vLQw-OFdCLV1IlnH-2FdSZVr9AMSdNaMuTLqaSmIZqocgjVg7McKIbsq_KrUAWUeEoxmn3qNz1lhNdB515Ah9eL9Y5aZ8-lvxU0ToLUjdKBFhKPfTYpkE8Xl42wHgwBU0cVIfL53yYit2jvcN81wG26WZ5X8hHP9HhbRiBUuYgb3KQiSa70cG7gpAUDb-lx4fqXZ_ctMAm4enqRRhgVXNcMuRDVO-9RJcTbC9CDGc5I6ZMP-44MbJ5YfWA5IrVbzwRs_hozczj2GbNMgpOzJgqENfu0VzssCU5OdWXDL-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f387513a36.mp4?token=q3mRbfvzmdL6hcjlRjC4pYzvFjtnQvZnZwlUAlwGFix0vLQw-OFdCLV1IlnH-2FdSZVr9AMSdNaMuTLqaSmIZqocgjVg7McKIbsq_KrUAWUeEoxmn3qNz1lhNdB515Ah9eL9Y5aZ8-lvxU0ToLUjdKBFhKPfTYpkE8Xl42wHgwBU0cVIfL53yYit2jvcN81wG26WZ5X8hHP9HhbRiBUuYgb3KQiSa70cG7gpAUDb-lx4fqXZ_ctMAm4enqRRhgVXNcMuRDVO-9RJcTbC9CDGc5I6ZMP-44MbJ5YfWA5IrVbzwRs_hozczj2GbNMgpOzJgqENfu0VzssCU5OdWXDL-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
تنگه هرمزِ معروف؛ هیچ‌کس تا حالا اسمش را نشنیده بود، اما عجب ماشین پول‌سازی است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67385" target="_blank">📅 18:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67384">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b6983cd6.mp4?token=MfxOP9A8FWrkGBBHqi2L1O8ObS7JLL03hU9oT5eczgQ5HjUo632Vf02MUXVzf0f4bSVKf_vPEq-VZUK5AfBtPZ3HLrlhz3JpK_5d5lyczoRLTsrW7q_Nnonks2B9l2CBxk1HNRaJbKGIDK4rkG2eQqxwE3OdJmH05rircQSkcZIs9pMV62VjqBJAPseg-Pumdy34DcsS5qNY-jQFkOz2MXWLCsM86AWj0KJcR5IYjlo2aWi8hZFjUD2r5d-on2ouqyh371lIZ0y9mlPfeDQg9mpaXQD2SbQigyBEKUOhJ5AE6TODtFm174gV2t4r7cVnyDS02ye0NC22GUTKRpgK3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b6983cd6.mp4?token=MfxOP9A8FWrkGBBHqi2L1O8ObS7JLL03hU9oT5eczgQ5HjUo632Vf02MUXVzf0f4bSVKf_vPEq-VZUK5AfBtPZ3HLrlhz3JpK_5d5lyczoRLTsrW7q_Nnonks2B9l2CBxk1HNRaJbKGIDK4rkG2eQqxwE3OdJmH05rircQSkcZIs9pMV62VjqBJAPseg-Pumdy34DcsS5qNY-jQFkOz2MXWLCsM86AWj0KJcR5IYjlo2aWi8hZFjUD2r5d-on2ouqyh371lIZ0y9mlPfeDQg9mpaXQD2SbQigyBEKUOhJ5AE6TODtFm174gV2t4r7cVnyDS02ye0NC22GUTKRpgK3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
به یک دلیل وارد شدم: ایران نمی‌تواند سلاح هسته‌ای داشته باشد.
من به دنبال تغییر رژیم نیستم، اگرچه این تغییر رژیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67384" target="_blank">📅 18:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67383">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d6c7e39a.mp4?token=Jmg_3wDKDzQr0R_LpJI9Ntg_uWvc0Hn93uDncM1g8VSOtUZ9TGsHvaNK7eV_rbFCciKfbNb2n7g8R1kT7pL7ST9L8ctIz-X0-G9ANw3TWEhA31CqqEs8B3sI42aVfotiEHTxjELdakx3HhvAhxCSSq11jyMsvcjvUxnzgSsOHICFb5NUgfA7tOq-u6PjyOUid6dmlZpNmTxyOo39dBsC2FX1OCxztgYQfpieIoBNA3OfP9PypRX820nIpLcDeSXgzCSRQN3RaHZ4jYT_Lcq0GXT28Y9YsjxOfFKY4fkSolHAO284LcZFTUvwHm4JWeO8carvjEDpe1q22qf7VNtLjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d6c7e39a.mp4?token=Jmg_3wDKDzQr0R_LpJI9Ntg_uWvc0Hn93uDncM1g8VSOtUZ9TGsHvaNK7eV_rbFCciKfbNb2n7g8R1kT7pL7ST9L8ctIz-X0-G9ANw3TWEhA31CqqEs8B3sI42aVfotiEHTxjELdakx3HhvAhxCSSq11jyMsvcjvUxnzgSsOHICFb5NUgfA7tOq-u6PjyOUid6dmlZpNmTxyOo39dBsC2FX1OCxztgYQfpieIoBNA3OfP9PypRX820nIpLcDeSXgzCSRQN3RaHZ4jYT_Lcq0GXT28Y9YsjxOfFKY4fkSolHAO284LcZFTUvwHm4JWeO8carvjEDpe1q22qf7VNtLjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
مقایسه اجرای سحر امامی، مجری تلویزیون جمهوری اسلامی، بعد از مرگ علی خامنه‌ای (10 تیر 1405)
و اجرای ری چون‌هی، مجری تلویزیون کره شمالی، بعد از مرگ کیم جونگ ایل (28 آذر1390)
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67383" target="_blank">📅 17:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67382">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3237168e66.mp4?token=HyMO74nAJsoXW2qZY89qG09sRwABoVVWXfApce-kqv4JLADOVwQJDOpHajtMRzW8nDilJKEvW7yhmJ5qQck4VdObOAwIRi1US1iPb0_ZP8Ay0h1n6KmFiyNzoe3-2hWoodmb1z72sLEP1DjdThqNtHIKL0AD76-wmOcgJYvYbd5kWhVVQKLlV3E2GaN0Q3zzpRpIz7zmt4tgWHGz_g6mE5rdjUrkwsrgWRJKwuku08I-ZrJs6vGhV9hrjELmsZoBoA4IOyaNPx3vlCVhhMf9vWZRVwbmp89vV_lQlOOr0CKj7FeAgm3NBLYllhilie8qo3O_hvAjIQIdWAJz0iwQIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3237168e66.mp4?token=HyMO74nAJsoXW2qZY89qG09sRwABoVVWXfApce-kqv4JLADOVwQJDOpHajtMRzW8nDilJKEvW7yhmJ5qQck4VdObOAwIRi1US1iPb0_ZP8Ay0h1n6KmFiyNzoe3-2hWoodmb1z72sLEP1DjdThqNtHIKL0AD76-wmOcgJYvYbd5kWhVVQKLlV3E2GaN0Q3zzpRpIz7zmt4tgWHGz_g6mE5rdjUrkwsrgWRJKwuku08I-ZrJs6vGhV9hrjELmsZoBoA4IOyaNPx3vlCVhhMf9vWZRVwbmp89vV_lQlOOr0CKj7FeAgm3NBLYllhilie8qo3O_hvAjIQIdWAJz0iwQIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
مارکو روبیو: سوسیال دموکراسی همان کمونیسم با ظاهری آراسته است.
مارکو روبیو، وزیر خارجه آمریکا، با انتقاد از سوسیالیسم و کمونیسم گفت تنها کسانی که کمونیسم را از نزدیک تجربه کرده‌اند، درک می‌کنند که سوسیال دموکراسی در واقع همان کمونیسم با ظاهری آراسته است و پشت این ظاهر، همان ایدئولوژی خطرناک و ویرانگر کمونیسم قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67382" target="_blank">📅 17:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67381">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54408a1a4b.mp4?token=Yw4Bdr0e5TDrCCHn0ehpulSizHp8TfhQjjKxrrkN_MNNEfe54rYK8BrrnGWI--ZRQIQ6VzqQ2XiKukvs_nkBn5e85A2zpix9wN2Fc0jVA9vRodhbpoW0Gj_NT_jtle9fI04yC-EYAKT2EubGGPLdbbLcgrTbMM_6UQdwdpJb8Z4KyqtfnkYEu8FkpfY1B8K8B1bGiPuwPuKFiu-lwIUcRtWYGp0P3cc7nolJJpI6CmE9BAeKKwnSg6Z73NCU-2MPWsyGKNPcqDiWPFop3VyttQexs7c7sNo4FvdzENgPmvDoULiyulW11gL4hPTXBSpmNBdmcwKHPaMXy-qCyzbAnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54408a1a4b.mp4?token=Yw4Bdr0e5TDrCCHn0ehpulSizHp8TfhQjjKxrrkN_MNNEfe54rYK8BrrnGWI--ZRQIQ6VzqQ2XiKukvs_nkBn5e85A2zpix9wN2Fc0jVA9vRodhbpoW0Gj_NT_jtle9fI04yC-EYAKT2EubGGPLdbbLcgrTbMM_6UQdwdpJb8Z4KyqtfnkYEu8FkpfY1B8K8B1bGiPuwPuKFiu-lwIUcRtWYGp0P3cc7nolJJpI6CmE9BAeKKwnSg6Z73NCU-2MPWsyGKNPcqDiWPFop3VyttQexs7c7sNo4FvdzENgPmvDoULiyulW11gL4hPTXBSpmNBdmcwKHPaMXy-qCyzbAnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در برنامه ای در صداوسیما حدود بیست دقیقه کارشناس برنامه اسامی سران و مقامات جمهوری اسلامی که توسط آمریکا و اسرائیل ترور شدن رو خوند
بعدش مجری به کارشناس گیر داد که الان بیست دقیقه وقت برنامه رو گرفتی که اینها رو لیست کنید و در ادامه میگه به جای اینکه به مسولان و مردم دلگرمی بدی داری دلشون رو خالی می‌کنی.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67381" target="_blank">📅 16:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67380">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84629e4c7d.mp4?token=E17FvwT1eB7N5B0La9vnxHJHk9DiIY49BJ0YiftLtBNjS8Hjk5BDbPHh96ANJSqFymnNii9qDveWWXqRvStgO3LsdGitdh9TClbR9aat7-i-8CKb8GKfRZUBWQRf60IgBMXSOr9dIBXJa75gktUYElUC_NAMIkdODcfcREtQG9UGZURHIPm280jUbNLF8Y7NwTwLhTlcElJMNchY6XLTcKmvsmmV51DT_Pm76vnDfk9AjKIMzyGXs_f7l1exTZwrP36EQ72mAQug0SxXG-bcjcr6MQcVS9e6mw_j2-7cEp5yTN8l5iXd3PM48JO1zNF_gqxnjOK9gl4llcJcwV0_0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84629e4c7d.mp4?token=E17FvwT1eB7N5B0La9vnxHJHk9DiIY49BJ0YiftLtBNjS8Hjk5BDbPHh96ANJSqFymnNii9qDveWWXqRvStgO3LsdGitdh9TClbR9aat7-i-8CKb8GKfRZUBWQRf60IgBMXSOr9dIBXJa75gktUYElUC_NAMIkdODcfcREtQG9UGZURHIPm280jUbNLF8Y7NwTwLhTlcElJMNchY6XLTcKmvsmmV51DT_Pm76vnDfk9AjKIMzyGXs_f7l1exTZwrP36EQ72mAQug0SxXG-bcjcr6MQcVS9e6mw_j2-7cEp5yTN8l5iXd3PM48JO1zNF_gqxnjOK9gl4llcJcwV0_0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو در گفتگو با فاکس نیوز:
ایران کشوری با حدود ۹۰ میلیون نفر جمعیت است و حدود ۸۰ درصد مردم آن از این رژیم متنفرند. اقلیتی که شعار «مرگ بر ترامپ» و البته «مرگ بر من» سر می‌دهند نماینده مردم ایران نیستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67380" target="_blank">📅 16:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67379">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336146a8b7.mp4?token=b77RtJE-GZYOfFBdY979G_K-Rf-hASc6dqdsWALbj_s3t2CDSkOzcjOVO4XXyAlAfQqKTfvKZf2dBl_vHFv4Y8-IqJMzsASO1ijOmdEQX8DXb2TeeLodSnPtHvYt_93P6ZDDfPelQm36MK-HP972UfZfxCpwgu9pbaC94gEb5KHqcLq-EYqkecIqnhOftv4mmt753JJhI7cLHv8v7Wqk3VG_8hQZULT14EFPGsbNo3cpAV1_pQi2o8znQ3hJJA_JmI-C4ErAQgV16UdkE8rORNdhQyVsg_8Qdm598gFx2G0PZqpcwLjVYIVMr4REl5yZcmqDpYLIIy_Jn0xQ4M2EjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336146a8b7.mp4?token=b77RtJE-GZYOfFBdY979G_K-Rf-hASc6dqdsWALbj_s3t2CDSkOzcjOVO4XXyAlAfQqKTfvKZf2dBl_vHFv4Y8-IqJMzsASO1ijOmdEQX8DXb2TeeLodSnPtHvYt_93P6ZDDfPelQm36MK-HP972UfZfxCpwgu9pbaC94gEb5KHqcLq-EYqkecIqnhOftv4mmt753JJhI7cLHv8v7Wqk3VG_8hQZULT14EFPGsbNo3cpAV1_pQi2o8znQ3hJJA_JmI-C4ErAQgV16UdkE8rORNdhQyVsg_8Qdm598gFx2G0PZqpcwLjVYIVMr4REl5yZcmqDpYLIIy_Jn0xQ4M2EjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مجری:چرا آن دولت هنوز در ایران پابرجاست؟
🔴
نتانیاهو: زیرا چند صد هزار مزدور دارد که در روشنایی روز می‌کشند و قتل‌عام می‌کنند و در شب مردم خودشان را می‌کشند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67379" target="_blank">📅 15:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67378">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWxY_78dgcgjxTJ3g01pr84v2Ou0uJAykjunzgBRbx8x-mNYIGAWm1Drp-25ExLgCcI5I3niVVbu6oTaXxplYGIDsWEfGtkfVbkcCpqPemZtqS4YKSKvbHzkACokY-QG5LmB2clvAKrMU4SeW45oXVoVGILduDKbC787V8-FoZnsdvQk2Clt0w08y_HF7x7kLe87JdsUbCJtUwWdTgCdnE3BHSpd0HBlMqiaS6X_Y8LYef4fYJN4Ubqnp1PWYsSFVyf2KX8JoxKTkw4-EULlQcGV_jig2Gs3Qk6f-YztNu-A-WY8StRR1GkxB6kH_fMZ9rWJ1vdrx9SKorDiz-KZ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
واسه کشتن نتانیاهو وترامپ 100 قطعه زمین 2000 متری جایزه گذاشتن،آیدی رو هم زدن اون پایین و گفتن انجام دادید پیام بدید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67378" target="_blank">📅 15:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67377">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fvv7kccRVvH77AZzKlSeditjFM1BwxgAeVTT1MISgESLBNn3XmnTZ7dTmeEZ6JMJgBP_NL1lc5MjdV4RU0-qZfzDRkEfCVvLDLQo0nd6-WM4UxfIE0qqwqeiuFUabYdE2MGbo9y6tdjEo3aRJ2XlK9_DPxef2b0S1lpumtA3x2j8Xrfh4WWMLDRqSlf6uHj1oFVULNVsHZxeM4KB_Pppms9ScSioJ7_oxxivWCXzHxeV3LAF4-zC-VGsXAgO2haxds4lwqq13eVYRC5brXObOvQDPwaaudFo0xKHSnnzncXBejJvjuTXqsFtYw1mmscbLOvX0yR7EeebC_2m-KPD0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دو حمله پهپادی هدفمند اسرائیل در جنوب لبنان.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67377" target="_blank">📅 14:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67376">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUXKK2e7woOL767QgYceZ-xB-aADUvfGqnV_Zz2VJkcYmGrqKYtJ5lZy66QobYU6l5EkimfSBHCoZdy3-yd_Y2ImZYUR6oNMaNWF2TIm0aPBp2IlYbsg2NG7OfUceKS3OikWEI1QQHO7oGvaGu4rIhVqL7NkJGDC6Oc6bjuRiV9b81maAGcJEzZZ9AWnyKbIh2h72iKWixQNQjCxk92LP239nsaFmdl6j7FFzjV0782UjRgv3IhAe_VBWNx_37a8Tc0N3kzXrn0njVVuQ0AkUDXoEml29pNxrmxijsve5Q8OhvlYcb3lUtPb2c2bJAdyCuQXPj8CI34DX2FDOEy8vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏شبکه ۱۴ اسرائیل :
سپاه قدس واحد جدیدی به نام « یگان مختار» تشکیل داده است که با کارتل های مواد مخدر مکزیکی و آمریکایی و همچنین ایرانیان خارج از کشور برای ترور ترامپ و ژنرال های آمریکایی همکاری می‌ کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67376" target="_blank">📅 14:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67375">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-RDety1n0voKxWjAR61SrPXUNYMIEB2gH29_nBa8qzEbvq2bQrGfp5ivpfZBN3E2RGoNY0J9pHuBBu25Aa7ug2a0jMyaCXBzh23Yke0Z822Wh23thiLPcHSWNHRt7XhrUqz8Fp51y-tRwHHZhd250HBGHnKM9-oe_t19l5PaWalb91FvTOSJlSQqFJv30DZENvWvcme0T3YJGhU7CL8AY_ut2E1lJZzqlSdpTeAalBkxUAxC9VskJ6gNvxrQhFTJrFoBLQyR7IaYmaH4YWl_LtQs78s8GkPgcnAj9zI-ZSQ6wSPJKmf4gYJULiX_WCcDQKAD5PtgO72fBOWJhc8oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یک بنر در مراسم:
دونالد، نابودت می‌کنیم! از توجه شما به این موضوع سپاسگزاریم!
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67375" target="_blank">📅 13:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67374">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0hNzTaas7SEn4GqvuUPGPFrMQbdbJ-jWRI5HEtbwURDv5Eg2uACG-CF3rho5rW52PbO4Mbwd0qhuM43WmoEcAH9aYU9UDkUry2LM7rlpHfhxZ1Ub7I1Q7Cx8TxS6u2oVvRLXTkZBeSPVYKTWFtfYpNAILzsjWdwFv3D9rbNtAxIaL16cOL8kEixI7NURGPsZeo0yWlcjNAtiInKz99x_sizkFhKYMu-OYYPaOnaVqQ249AK3CHBI7jAm7uhhfFpnw4f0pjuxusJtlb4m9AqOvYtHfzl0TblliwGWxCSHrEwM_c7IpgF8jD1oM2akD18fz-kmnXgX-pX6JtTXz-IKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
ادعای
نجاح محمد علی کارشناس عراقی مسائل خاورمیانه و از حامیان نظام جمهوری اسلامی:
در مراسم تشییع امام سید خامنه‌ای رضوان‌الله‌علیه در تهران، فرزند ایشان، بقیةُالسَّیف، آیت‌الله سید مجتبی نیز حضور داشت. او پنهان نشده بود، بلکه در جایگاهی قرار گرفته بود که کمتر به چشم می‌آمد.
هماهنگی بسیار خوبی با نیروهای ویژهٔ امنیتی و فرماندهان ارشد سپاه پاسداران انجام شده بود…
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67374" target="_blank">📅 13:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67373">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjSiUml1Ck-Q0NsZfZs0RDKffIrPCgAe6mC82DMW_rj7T9tKA4oG4C5na0wdC8KZz3lZOct7ifk0vW4SeT5b2j0Cz3KKei7Y0pVlbHSLjQc7vOocZIit6-TrxMWgjduMP1wZRFXDQhB2tOVOsDgjnlPoCsjOT7VGV5TtBqZc0JZP99KJLqTEMbHIC0vdpiNiot1ngDxi1FHv_CYd1pCW0JjoUSpSLKBNhYAj-7DMQFAhCuhuEqg355a7WWbNYEsTIObWHNdPVl_GMR4rMr2oZ15oSL9ffJxqxEsz7A1FqCdjhW4ju_2HBytOlPnLEXFuJXDwlGm-EmDWuLbD6ZDT8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
«آیت‌الله خامنه‌ای که مراسم خاکسپاری‌اش هم‌اکنون در حال برگزاری است، توسط اسرائیل حذف شد. هر رهبر ایرانی دیگری که برای پیشبرد طرح‌های نابودی اسرائیل تلاش کند و اسرائیل را تهدید کند نیز حذف خواهد شد.»
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67373" target="_blank">📅 12:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67372">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22aca7392a.mp4?token=h3HwwrOV9LJr43fKF9npTE8i64bDXe7QHfmZtedZKShWu8pIbKz1bbJOjR0FC2ZjPGiUEyQoykvrKyyytsVg6oAA9Llvu1wzwz8fq0zyWcaW0Ffj7fjpPLwiXI3IvqLd9Vch13sCK0CauXfIq5pCyS9L8e0Glu1YzFFyodt-oR2pGtPKM4AeKBXmg4rNEX_9HHPiOUOLXMnhfaiJhluwjkFDnCgj5Aa-3YhyN2KqKFPs41HrOIOJeL1-8h8Lnis5flsJV_azmKsVbzqeaQJUuBwlcABsycVvJ9h0Yn9hoK8yWceZR3sbAF74WVKe-a7JnMa8NYcZA6DnnSU0peewSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22aca7392a.mp4?token=h3HwwrOV9LJr43fKF9npTE8i64bDXe7QHfmZtedZKShWu8pIbKz1bbJOjR0FC2ZjPGiUEyQoykvrKyyytsVg6oAA9Llvu1wzwz8fq0zyWcaW0Ffj7fjpPLwiXI3IvqLd9Vch13sCK0CauXfIq5pCyS9L8e0Glu1YzFFyodt-oR2pGtPKM4AeKBXmg4rNEX_9HHPiOUOLXMnhfaiJhluwjkFDnCgj5Aa-3YhyN2KqKFPs41HrOIOJeL1-8h8Lnis5flsJV_azmKsVbzqeaQJUuBwlcABsycVvJ9h0Yn9hoK8yWceZR3sbAF74WVKe-a7JnMa8NYcZA6DnnSU0peewSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حضور احمد جنتی در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67372" target="_blank">📅 12:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67371">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ad63d7f30.mp4?token=rJ4JDJju__5vhZnCYsG3VuSLhMIThM4BKNgMrOFyn5G6namkAnrm-du-Q3NO4_mWoMDC1EfFi6gJDgml5u1peilMuQLbh2GtTEEgHk-DEoLX630A6ezjiwFy7o4SG4NYlDwH5NNvIjnX6-CJ5lPQU8wC59yCAbU_pN2I39Fv457oO5S0uXHClVfWafeZr6qj-KyK7hdvg0CRFI5tCymV8bFV9N3Yng6RftdlHQ-ugHdquWQXCPBguDu4hUsB9NmQUqJ9lp17NWrx0SALW4z9n7xjo-PooUf7p9nSj8qF9aEJHl8WwpeM6rSSpq2CrWFviin2pmOXYVD_7CcX_47ABA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ad63d7f30.mp4?token=rJ4JDJju__5vhZnCYsG3VuSLhMIThM4BKNgMrOFyn5G6namkAnrm-du-Q3NO4_mWoMDC1EfFi6gJDgml5u1peilMuQLbh2GtTEEgHk-DEoLX630A6ezjiwFy7o4SG4NYlDwH5NNvIjnX6-CJ5lPQU8wC59yCAbU_pN2I39Fv457oO5S0uXHClVfWafeZr6qj-KyK7hdvg0CRFI5tCymV8bFV9N3Yng6RftdlHQ-ugHdquWQXCPBguDu4hUsB9NmQUqJ9lp17NWrx0SALW4z9n7xjo-PooUf7p9nSj8qF9aEJHl8WwpeM6rSSpq2CrWFviin2pmOXYVD_7CcX_47ABA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیوی عجیب منتشر شده از وحید خزایی شاخ اینستاگرام با سردار رادان که میگه کار دارم با وطن فروشای لاشی،ترامپ گفته گوه خوردم
من سلطان دختربازی ایرانم ،حتی سردارچندبارمچ منو روی کار بادخترخالم گرفت ! اماخداشاهده آنقدرمهربونه،هیچ کاری باهام نداشت و ولم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67371" target="_blank">📅 12:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67370">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a17dafc375.mp4?token=odTwKqPZQMnZWjnvKO4JntnZY5TPVaCMXI0ucoqY6v17Wzto-76P8x-Zmq6JdMrd5JkPKk1iUYG0feNMS9Xuqa-zuGiCG-MAk5SVVFIa4DnfOpB2FCdZfxpprFpp8nx3wvUB8QANjmpWMmBL0YZ_IFqgU2Dd2fdIzMzB7eAKzRZIRAbvURTRJIfHjeNVVSMZQCr1Ug3YWJyVOG9afg2Tl8Nce8WmaX6YGVbVX6Ye6MlokmtcmE2GjyL7Q6bGUXlNl31_Ee05z1j3QpsioTHM58Vlc0yMOYUUWKy_gATI_Z3zfyb7Vm4XI5wVfPGYlEP6frLIImKe_ynN2MHTjdQM4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a17dafc375.mp4?token=odTwKqPZQMnZWjnvKO4JntnZY5TPVaCMXI0ucoqY6v17Wzto-76P8x-Zmq6JdMrd5JkPKk1iUYG0feNMS9Xuqa-zuGiCG-MAk5SVVFIa4DnfOpB2FCdZfxpprFpp8nx3wvUB8QANjmpWMmBL0YZ_IFqgU2Dd2fdIzMzB7eAKzRZIRAbvURTRJIfHjeNVVSMZQCr1Ug3YWJyVOG9afg2Tl8Nce8WmaX6YGVbVX6Ye6MlokmtcmE2GjyL7Q6bGUXlNl31_Ee05z1j3QpsioTHM58Vlc0yMOYUUWKy_gATI_Z3zfyb7Vm4XI5wVfPGYlEP6frLIImKe_ynN2MHTjdQM4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وحیدی فرمانده کل سپاه با موتور اومده مراسم
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67370" target="_blank">📅 11:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67369">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abfc46c7e6.mp4?token=kPjQ85RMK2wX0dCl9LsMmEtWJvzBkQglpHR_dS7eusKBvHdu9UoDRsJ_9diRn0RgsBl3dE16Pow6yDT9Ax94XrAJzgEDdVyHuZybUOZ69QbPhCpKC-1kAU6ZiWmhmsjTUUHPNcx11k0FoFPwS5xwGjPOwax9tKOw_MogyJ8b7PPqDL415qDWIt7fHJ8J6qies5_vDRmpPeh9TdRiKwC2mXqLk8a3eKqXEH8xsksaljgZCd1aAI4J5dfrne0Hgl2btVih5LFxqRkzgGFRqcWWY83WHcAIkRqfCz3Smv6mwiY6xdOKs5jaTnzWdKoiusSOXnjkr7Fp2JCHBxDYDxOlNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abfc46c7e6.mp4?token=kPjQ85RMK2wX0dCl9LsMmEtWJvzBkQglpHR_dS7eusKBvHdu9UoDRsJ_9diRn0RgsBl3dE16Pow6yDT9Ax94XrAJzgEDdVyHuZybUOZ69QbPhCpKC-1kAU6ZiWmhmsjTUUHPNcx11k0FoFPwS5xwGjPOwax9tKOw_MogyJ8b7PPqDL415qDWIt7fHJ8J6qies5_vDRmpPeh9TdRiKwC2mXqLk8a3eKqXEH8xsksaljgZCd1aAI4J5dfrne0Hgl2btVih5LFxqRkzgGFRqcWWY83WHcAIkRqfCz3Smv6mwiY6xdOKs5jaTnzWdKoiusSOXnjkr7Fp2JCHBxDYDxOlNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عباس موزون، مجری صداوسیما:
چند بار [روح علی خامنه‌ای] از بدنش جدا شده بود و تا ارتفاعی بالا رفته بود.
«اصلا بعید نیست آنهایی که علیه بشریت عمل می‌کنند، از نیروهای شیطانی کمک گرفته باشند.»
چی میگه این
😢
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67369" target="_blank">📅 11:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67368">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxlcA_PxqhwYlAsqrZjUiBu4yxbyO2ryi3q3yxkMrnm0FcXPol9qurgiUpBdKW6e5ch75-1FtCtuRSrt_-wXJFHuoJICt7fIycp6XTnqLIhg8NoAvc9ObelY3aCBizcQnF7SJvfGXgSHG8PcgRwbmHeTxD9iG9vdgML1bACc_uwJNpNMNohadfpqOeAdeHAQsETTYUKnS1E_4Fd5JgTabCHSE7pEOu7n63Dzv4iMSryM-yYIq_HXXzkZ-3llVHWRK-5rbDy4U5ASef4wCmw_jJM-WKbk_adIctwsMfLzr34Qi6Xm8CNELonmDa0VaFtNKBrRS2OcY8O9YTkJYFpfKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اکبر هاشمی رفسنجانی،24 اردیبهشت 1370:
سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67368" target="_blank">📅 10:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67367">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38c47b7b97.mp4?token=idN_c8sYAK21ZfPgeRwm43SvVksG3fYbRxG9arRHrxvLO_Y1X2nvPLSOKdJSLe4O72_HH4PWSXnnntEu9OCwSO-QZe2vW96yGsm0Fti-Bl7N9IKN4B64zPoDU-Mu40Wm12OZI9glc-HrUs52Df8b6DWNtiOqQnBwyw6UbV3xD8sbVOEvGQwQwx9PV9gX6UEtxThowOKvciFgoxtndKFcXhX2F1Eyl-SJ6bn2v9KD1jBE31qzkT_k1UB1EnkUk8MSUAhuaq7CnhGlnLWzkjxjdJRsckYgYIID8AZismlP34aYeWANoJdOsf9KqrS8RWb7_TDAvnnhc6xLeOGyR0XlaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38c47b7b97.mp4?token=idN_c8sYAK21ZfPgeRwm43SvVksG3fYbRxG9arRHrxvLO_Y1X2nvPLSOKdJSLe4O72_HH4PWSXnnntEu9OCwSO-QZe2vW96yGsm0Fti-Bl7N9IKN4B64zPoDU-Mu40Wm12OZI9glc-HrUs52Df8b6DWNtiOqQnBwyw6UbV3xD8sbVOEvGQwQwx9PV9gX6UEtxThowOKvciFgoxtndKFcXhX2F1Eyl-SJ6bn2v9KD1jBE31qzkT_k1UB1EnkUk8MSUAhuaq7CnhGlnLWzkjxjdJRsckYgYIID8AZismlP34aYeWANoJdOsf9KqrS8RWb7_TDAvnnhc6xLeOGyR0XlaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان:
خرافات پدر ایران رو در آورده.
آینده ایران در یک جمله است؛رنسانس.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67367" target="_blank">📅 10:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67366">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33573d06e9.mp4?token=AFJ0f7S3c-hUghnf6QLXIl219czghas4NTMDErAitjACif3xuXHax5ncxsKggbVAim3COJ1Duxq9mZreJvdS6QFNDxCrVXkKXEYEWsJrvyf9g0hK2PszJl-c1n-bEYD4dNCLP9PlhQs2xBI_kHTgTVuyPQp3FDHrNTs-kSDOHli-s6itfey-SshUsjPoHegMIAOVeXGb8WDKx7lcWPdCd3mtxJQkCx1ioNl3E8MGl3sT2b2Nu-ZAyjETNY38ppVDvFYwdn0yxGDPIiabVVePl9_2rXO22ehizXnKSvRcp09yJKVzDotX1EGezcK7iXVgYfF-dqAa5T08zuvRA-QUOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33573d06e9.mp4?token=AFJ0f7S3c-hUghnf6QLXIl219czghas4NTMDErAitjACif3xuXHax5ncxsKggbVAim3COJ1Duxq9mZreJvdS6QFNDxCrVXkKXEYEWsJrvyf9g0hK2PszJl-c1n-bEYD4dNCLP9PlhQs2xBI_kHTgTVuyPQp3FDHrNTs-kSDOHli-s6itfey-SshUsjPoHegMIAOVeXGb8WDKx7lcWPdCd3mtxJQkCx1ioNl3E8MGl3sT2b2Nu-ZAyjETNY38ppVDvFYwdn0yxGDPIiabVVePl9_2rXO22ehizXnKSvRcp09yJKVzDotX1EGezcK7iXVgYfF-dqAa5T08zuvRA-QUOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو مراسم وداع با جنازه علی خامنه‌ای، وقتی نوه‌های خمینی میرن جلوی تابوت سید علی خامنه ای، قاری این آیه از سوره نساء رو به کنایه می‌خونه:
آن گروه از مؤمنانی که بدون بیماری جسمی در خانه نشسته‌ان، با مجاهدانی که در راه خدا با اموال و جان‌هایشان جهاد کردند، برابر نیستند.
اونا هم برمی‌خوره بهشون وسط آیه ول میکنن میرن.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67366" target="_blank">📅 09:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67365">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9XLh14B3nVeMTJ46jjro56VIfxFpZ4tIZkHlsnFOL0EUpvjGD4PEkP-CiwOfYsnkyP2Jhe0S3UylzJ-GNeoAlJ6cgaEgRDA35z-OfmKyodQCTBJjYCgNFiryqo7cXzUaW-Jho7rNo3Mb67Dus4BOEXSrF8fx7L-VSZFyexANRcOUyNMC31OIa6c_Z8l4ZU0DzDFve3toeTxbP_mb7A_2iMmqpBCe0pH8p7Y_bOlBQytqkjAnjDMD1T9OJQk4eoexDvZAtsG2doOjA5LtjCh8Re6Rj4Jd3tQ916LmBPcr6JZM-InXxsDhTEi-n1E6Iedy951gQTafT5wRzPLUVAjMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67365" target="_blank">📅 09:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67364">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67364" target="_blank">📅 03:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67362">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xtey6hWHQEj8vAu2yF0LI3rAvBSd4WxAqBEMl1JHDL_HJpBLx7cwNuKz2sEa0Vw-LGAs8QX0UL3-EB9MZBLA9HXXXvPFsrBNfx0ztC_wkSKAuAAZf1OJ3_BTqAjZFV2mh6vP3yiR8JUEnVnlQZY1wOz3G0DU3giK63g8gl-4Faokj9DA6_-uEo_yYxgwqmt_gx65glJtvmS0Ac7rbgaV27HliZqUzzg2sexPgDugJMszXF-Yqu4Z8KYggBodnNDBY85lMIzxrUUZMv5CGHbAkB5f2rUYEVFWWzzy5frGdXPeL-u6kR6QB-M7w4aoKnMtBbbc2jrFVEamvj4f7hcLXQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/67362" target="_blank">📅 02:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67361">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1fe48304.mp4?token=dI1YZ9_Lbp8_k4VEld2i1cUXjUIYMm-_nXV9LQ9CjP8_fg85YofrjwPHv5ySsz6422LllHjI9alrKHQhDyAsXmS_gWEjGWPYlUAnMEb0XJoG9kKb9wfRE7YloWrF-Ybq2K5mY0XpfKg61TWqesEMruRF4VT_KFb86GcKIeKlbMk5h3v5c0EZZJQgU5_p18Ml6mvhbGfd3b5U_w78GmVtxLjRTH_FmEcJ5rg9JU1-t4KjVCpb3oSiwdmvqgLEjg3ldGliTi6bYO9mWpvOW7-p2796xxlgPqadnH72dX8DdsXTDtlOPdYM1cb7UP47BfP9sIp-Cp8tOTdIIZlvZy6Oiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1fe48304.mp4?token=dI1YZ9_Lbp8_k4VEld2i1cUXjUIYMm-_nXV9LQ9CjP8_fg85YofrjwPHv5ySsz6422LllHjI9alrKHQhDyAsXmS_gWEjGWPYlUAnMEb0XJoG9kKb9wfRE7YloWrF-Ybq2K5mY0XpfKg61TWqesEMruRF4VT_KFb86GcKIeKlbMk5h3v5c0EZZJQgU5_p18Ml6mvhbGfd3b5U_w78GmVtxLjRTH_FmEcJ5rg9JU1-t4KjVCpb3oSiwdmvqgLEjg3ldGliTi6bYO9mWpvOW7-p2796xxlgPqadnH72dX8DdsXTDtlOPdYM1cb7UP47BfP9sIp-Cp8tOTdIIZlvZy6Oiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67361" target="_blank">📅 01:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67359">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4vnbEQr6gn0eM7N9pVpvsHubMrRjKgkWDy7gaTZZUAGmdCR7Sdj2wbhPqR5UdE148WoOzYaoIGO5NrcEX95DFF53Itff163PeMeQkx003QC9iwdeoyXApAcoJPKM8TmphUZM8pox_qNGZdw11P2mKe1l_ZLgPqDIDkNCMj6NQK8H4LBwQl__PRnTGkjfReWpiplKkgOtnZVt8oVwYxS0uYWm6fNYrBiXsAjXnrFIDXkyONdiz9iH9F4srPyfbdq-qwDFnolXfonJ5yuiJKyg2cIuD4ACfpy6arlQ4lorTKBW3qxGWtfHH_oQW2iNvGoPtg1yGBLK2dJG1hsWNdkMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کانال ۱۴ اسرائیل:
انتظار می‌رود نخست‌وزیر اسرائیل(نتانیاهو)هفته آینده برای دیدار با رئیس‌جمهور ترامپ — که هشتمین دیدار آن‌ها از زمان بازگشت وی به قدرت خواهد بود — راهی واشنگتن شود؛ دیداری که در آن برنامه هسته‌ای ایران و خرید احتمالی جنگنده‌های اف-۳۵ توسط ترکیه در صدر دستور کار قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67359" target="_blank">📅 01:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67358">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6d2fa6e6a.mp4?token=tmFU7MsFhxLcnC8mhAPhnT3KpiEIE2uXVyoPa3hAXcTlTIY3dqwTK41jbrO4_ZS6WClyp7UR76Fr68FIve6ASNuZVrUKEnvHLgXT0Ut6x1eGHhCCWqVZ8Ly7WfQF44bFAC83VFbel1BERlF8QLC7RDkYSqLcBM6ECLZTNGXindUxLQ-nH9nqWPqs9SYiZK3o7j9CH3lp8HQV1xiyZU01Z4vc2mLu2lzEmjWH9Iq05ZD__1zR-TXYkaYHwFlLrTAVLO-jMA6EhkYzpt32q7aFSPcI1X_OSONQtDjaqTx2ZGH1iES5iYeYJ5rRHkDk_-U2ILxoaHyxw6YVFsAQKhgY6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6d2fa6e6a.mp4?token=tmFU7MsFhxLcnC8mhAPhnT3KpiEIE2uXVyoPa3hAXcTlTIY3dqwTK41jbrO4_ZS6WClyp7UR76Fr68FIve6ASNuZVrUKEnvHLgXT0Ut6x1eGHhCCWqVZ8Ly7WfQF44bFAC83VFbel1BERlF8QLC7RDkYSqLcBM6ECLZTNGXindUxLQ-nH9nqWPqs9SYiZK3o7j9CH3lp8HQV1xiyZU01Z4vc2mLu2lzEmjWH9Iq05ZD__1zR-TXYkaYHwFlLrTAVLO-jMA6EhkYzpt32q7aFSPcI1X_OSONQtDjaqTx2ZGH1iES5iYeYJ5rRHkDk_-U2ILxoaHyxw6YVFsAQKhgY6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو ای که فرستادن به صداوسیما از لحظه حمله به خونه نتانیاهو و ترامپ و گرفتن انتقام علی خامنه‌ای
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/67358" target="_blank">📅 00:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67357">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/237c10defa.mp4?token=oPHbxiWqc0re3E9sYbCIJjrXo3W2NuxtpKtasweI2Nt4sf3JJQtor8KkKusRZ-blpQuPBtv4bXSgNlncmBRSXlfymyu0UQu37EnUXsGjTcBxK0B5MMcT3deJVmeAMwc6KYN8evk4wtYsClXijl66iWJw_l4o0k9hvplAS7VbmNzbIazTHEuzsLnvV7x16dGvyA-emolS-LPH8Z8cLyA2xqnODM_GrR8BX1a2d7S4dJkuIxuXx7VP0mlSboqY2NAniAgF-ZnxMxBfNDFn3Xxp8sMeIa1_N2EeW0-KAWj4ZBIEVGXPf7v2MtWFc5fVwbTHLFWBpe6VPXZvWtSnwSNh2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/237c10defa.mp4?token=oPHbxiWqc0re3E9sYbCIJjrXo3W2NuxtpKtasweI2Nt4sf3JJQtor8KkKusRZ-blpQuPBtv4bXSgNlncmBRSXlfymyu0UQu37EnUXsGjTcBxK0B5MMcT3deJVmeAMwc6KYN8evk4wtYsClXijl66iWJw_l4o0k9hvplAS7VbmNzbIazTHEuzsLnvV7x16dGvyA-emolS-LPH8Z8cLyA2xqnODM_GrR8BX1a2d7S4dJkuIxuXx7VP0mlSboqY2NAniAgF-ZnxMxBfNDFn3Xxp8sMeIa1_N2EeW0-KAWj4ZBIEVGXPf7v2MtWFc5fVwbTHLFWBpe6VPXZvWtSnwSNh2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پهپاد اوکراینی یه سرباز روس ـ افریقایی رو تو یه مزرعه تو شرق اوکراین بدون شلوار حین دسشویی کردن گیر اورده و افتاده دنبالش
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/67357" target="_blank">📅 23:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67356">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rxx-tJgmM07cvSd-61bgLkUiwII61rt6cxmNjQgOw4nhwlWrokEsOUWivsWjlGZ17cvf5oXJRjsvmSnJ7sM9eDUsaZe_wxZuRd2qXVUvzpsVgjfWCjyxYA0gaXR6DBy6QvEte67zIoVjXjjJYEwMYcOAgY-zF4SMBDwBKi9YrBKNGZTtZ_Ec9Le0JaRDwi20Scwx6VBar2x6FmvKaaLdD6gxUAXGMgWp-SL3PS2n5nD7XRUeFj3cEBOIEpMiyEmzlp7ATNL3wq0kv0OIRWMebUrMa6Tk0pCK5EExBH7Pa7i4ZvST0ID3l5Ozcb0LYP0r8te0dS8wUVPg4Yim-BX6vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سنتکام:
یک چترباز ارتش ایالات متحده اعزام به خاورمیانه، آموزش تیراندازی انجام می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/67356" target="_blank">📅 23:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67355">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb140a8f9.mp4?token=E8xPwA4jUBgzFJPAqfV3zAB6TZpLE8ahPlaWRY_nxHzsHj2Wp7GAtB-2w1Uh3UWiw5E7pvHn_YejaxKH3XvMeiGw834EIrIr0HlNuszQKorwTvhfaky5soHX7LtydGJTeFhPRIt1hbFSkiF32BZ8zk6KYOZ-jTT1QVDDFIJqTzGGPLuDaDkih0zL-R1TYeRAuOHwL4q0zSG-OdwcV7k4WP8nBVCVjzylyu_3cF0CJWfOqBV8SU0SLWKtGnSPwV81lz8WiuEr1DMddcIeyqMPc0c7oyTyQzRBgJ8hJIaxc3-54hYmI7SX4ju1Y0JstFVGRV2LUfTVctOKZetFF7wsdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb140a8f9.mp4?token=E8xPwA4jUBgzFJPAqfV3zAB6TZpLE8ahPlaWRY_nxHzsHj2Wp7GAtB-2w1Uh3UWiw5E7pvHn_YejaxKH3XvMeiGw834EIrIr0HlNuszQKorwTvhfaky5soHX7LtydGJTeFhPRIt1hbFSkiF32BZ8zk6KYOZ-jTT1QVDDFIJqTzGGPLuDaDkih0zL-R1TYeRAuOHwL4q0zSG-OdwcV7k4WP8nBVCVjzylyu_3cF0CJWfOqBV8SU0SLWKtGnSPwV81lz8WiuEr1DMddcIeyqMPc0c7oyTyQzRBgJ8hJIaxc3-54hYmI7SX4ju1Y0JstFVGRV2LUfTVctOKZetFF7wsdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خایه کنین؛ توی اردبیل چند تا آقا نشستن با یه خرس نون و پنیر میخورن
🗿
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/67355" target="_blank">📅 22:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67353">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfgoPaUAH5WuowVzyIZSk4PxEeC9vQbVINi9ZucBImZSJONnAmNy0v1EXvpZMiugNZPaNRjRNLyHiY7dOk6GbV6dLFLVgC5GeLK2eMvvDHu5r-Z9Fk7dDCsDBRYwW2FLnTUxmiz8NY1AlL4u5qmQVRXPUzwdfuGGGxwBEeooUKHD5DdFXVcimf6VOJZpZcCDXsikXj1x1sJL5ieWAFcZvU01YSHBdPs_oAuhuJkXdfRn6r_5g52MfIMntM6CEfvTfO3ZGQSDLkFKhp02Ww2AY9g6bHdyygPJJOdSy4JVOdtBH7KiPuVPutP7tvs4cFSiifNbg2oAVMdRFFXAD9Aapg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسرائیل به فارسی:
مثل اینکه مجتبی هم بوده
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67353" target="_blank">📅 22:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67352">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc47a54d3f.mp4?token=fhS-BRIWNK0kjktVOaAHbVEzWSicSn_fgZ-1UXU3FkOusEpYeTUyFny_pU1UviwR74Lo7tR-ZNGXCk4I-_AzUu_quSU6oYAeo8z_WRyz8CmgfWT4yz1Q8D0I7GthIqxvBDCTx16gy6_njZWbMEhSx1ddW6_0eDgOCgIiNlyREbO_PJZZjZctfaWrhZGHmwSZUaeUAp7CMA_2yLmoEa_Fm_2AR7NrNNGbQnsphhYapFZGFoZP4viYRZCTJWlUL1GaAUVAW93zZjTgwdWT7PRGN7OnGvluTXlrGgugA_26QLhlQ5_HLy_VjG69oqsKsK_nHJlJcjKu115KD7-f73cONw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc47a54d3f.mp4?token=fhS-BRIWNK0kjktVOaAHbVEzWSicSn_fgZ-1UXU3FkOusEpYeTUyFny_pU1UviwR74Lo7tR-ZNGXCk4I-_AzUu_quSU6oYAeo8z_WRyz8CmgfWT4yz1Q8D0I7GthIqxvBDCTx16gy6_njZWbMEhSx1ddW6_0eDgOCgIiNlyREbO_PJZZjZctfaWrhZGHmwSZUaeUAp7CMA_2yLmoEa_Fm_2AR7NrNNGbQnsphhYapFZGFoZP4viYRZCTJWlUL1GaAUVAW93zZjTgwdWT7PRGN7OnGvluTXlrGgugA_26QLhlQ5_HLy_VjG69oqsKsK_nHJlJcjKu115KD7-f73cONw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمزه صفوی :
یکی از گرون‌ترین سیستم‌های حفاظت در بین رهبران جهان مربوط به علی خامنه‌ای بود، اما نتونستیم اونو حفاظت و پنهان کنیم و از دستش دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67352" target="_blank">📅 21:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67351">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
ترامپ:  از فیفا برای انجام کار درست و جبران یک بی‌عدالتی بزرگ سپاسگزارم!  @News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67351" target="_blank">📅 21:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67350">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1qORM1XXbHkTpbVAw3WdDiAcPgKNuYs6JeBZfAlrpX9k1rs18erTiko9Nh7uUKm9ZFaP6ggebxb1a85PXupSAu0JCETPUpm1ZPz23tyqgMZ__ylfpnsdQXifHbClk251MpPxTcbbBB-W4gRW0pzRNWLfVfJR-iapLAcbjV25CSz7c33Ofm3S-oOrMbXp4NCrAXh_oNHeB208Qe7PeDl0JUblAeSWI7BeWP25jxyFy8O6dj-YEFw0-soTd_SACcZpEKjSYX_iwrA07hUWA3Q2ft11hU6O1M7vhErBOSMuijDX9n7BHJjScpD3UMIhA7Df8qjiWrhKt2T96l37N_72w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ:
از فیفا برای انجام کار درست و جبران یک بی‌عدالتی بزرگ سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67350" target="_blank">📅 21:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67349">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d12e972bb.mp4?token=TA0W6xv3wrCfHYPlHQ7jctUH1ubSRroX4CGv5pPSJHL0hLNTry9wTmVeRT6mtmp6X0k5fWWnhZadVOw2RXzDNpTOE8_5IX-N6becV3w58LZRfownk-RrayA16skxdb74HVpOSEKNP0-dqwMYMx6FRiG8Pws2dAXLCmANx1CDYbu-T-xKZ1_ggafP5t6JwCzf5TygWp_h9J70JLXSDZDhBHwxBdCiGg_pc96pfo4LfxwwI14Hge7x2xGpeeiCBG94d8voeK6ayigWDe5W3EA1Mf1Si7M1MRjDuqdhfSv3ZM629o-6Dnc_Z4PUoZ-f6ghEZVCZ5RSw1ja_PzZLL86dCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d12e972bb.mp4?token=TA0W6xv3wrCfHYPlHQ7jctUH1ubSRroX4CGv5pPSJHL0hLNTry9wTmVeRT6mtmp6X0k5fWWnhZadVOw2RXzDNpTOE8_5IX-N6becV3w58LZRfownk-RrayA16skxdb74HVpOSEKNP0-dqwMYMx6FRiG8Pws2dAXLCmANx1CDYbu-T-xKZ1_ggafP5t6JwCzf5TygWp_h9J70JLXSDZDhBHwxBdCiGg_pc96pfo4LfxwwI14Hge7x2xGpeeiCBG94d8voeK6ayigWDe5W3EA1Mf1Si7M1MRjDuqdhfSv3ZM629o-6Dnc_Z4PUoZ-f6ghEZVCZ5RSw1ja_PzZLL86dCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمد مخبر مشاور علی خامنه‌ای:
قاتلان امام شهید به مرگ طبیعی نخواهند مرد و نظام آنها را به قتل خواهد رساند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67349" target="_blank">📅 20:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67348">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5503b743a2.mp4?token=obZBd9YZdGJaRVhHYDsuUzgC78nCRvmUsqBimK6HSsAC3zAnW9_OP1tg7oyu38ZbRDOSAAFdRUV2g7PYr7yqx0scuZSaPFCVYOwereNFo3k7_VpExbmrvACy9DMxR_qwlWiWvkksZOElWngAvaFN5WPQJGtfpNc97E5iRRYWeBrk_qe1kdSnj0tE12AZXPp4PtcvJocImWLewDhNdJart4zRyA0Y8_0cmqDya-CDMPtxc0gPevlieTagUCP2CT8KECXXJyZgacedBTskI-3pV9mDwGVFboSCgIhFJDZvw4D6IiRqB2lODkeNqEklHkPXOQYT8Kf5drZUVMoIdE8xCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5503b743a2.mp4?token=obZBd9YZdGJaRVhHYDsuUzgC78nCRvmUsqBimK6HSsAC3zAnW9_OP1tg7oyu38ZbRDOSAAFdRUV2g7PYr7yqx0scuZSaPFCVYOwereNFo3k7_VpExbmrvACy9DMxR_qwlWiWvkksZOElWngAvaFN5WPQJGtfpNc97E5iRRYWeBrk_qe1kdSnj0tE12AZXPp4PtcvJocImWLewDhNdJart4zRyA0Y8_0cmqDya-CDMPtxc0gPevlieTagUCP2CT8KECXXJyZgacedBTskI-3pV9mDwGVFboSCgIhFJDZvw4D6IiRqB2lODkeNqEklHkPXOQYT8Kf5drZUVMoIdE8xCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
قول میدم راه امام شهید رو ادامه بدم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67348" target="_blank">📅 20:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67345">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kiyGqON3ufbsTQOgBYjtNXklpKbsYmu6MGZs0ItKAWCCuCl-26lR8IYLPoSHofbYDOVO-B_mQSm6rA2h6rPGy2VGaBhrSN6B6Ix_uWD8DCrIzJf9_W_D9CJmtRpaSQnZ_wouFuW3GJ2ZZ_DNDWwQr1wEcKMFcNwdXEiJQS24O0OIPE5Gob7uKKrCJr2NahaaD6rPKtn_PE6SAEU2-_hNoHDlZSnw3aOQAQxVdVz_xt4_6fPduLvM8uGPADWf31r9DP1KjEuI2LV60zeXrp7cwOR6OWFhIyRXi7yqPey36mdQG7mEmCuxgXtJyBrF3AK0vi_lwa8DC2zDlnKRanHf-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PNg5zW6XKdjcr9FdhTKzl0khMFsJOI-MYPVZblEIRUbapPz2nrWgPkfLJfJu5AOZpcnAwNeGSwhNfrmMLa8Bs84jf4fq8t9dr2klZq4S1m_Th7MHjIoVJNOS_5GjbFv5kN-CB_MiAk8KXnKeubvk0rYTiUzQdz7wp1DY41SSSSDwGmL-VGahLyaTq97cyR49nW-Uq-woLjCmidsPlU6w-T0NPWdhZnvTqEWjbPoPtLkG_k9qtrlN1f9AR8fQMgQ_na3hkCU3zyxS12fPgsWx4D_GRpn2bOWeOwrxndWnojyO-h1Xen2aHuxoMCvP9CeRB07oejF2onF9h99WU7h1IA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a975887416.mp4?token=dtQJLrMfCu6ai8o_3jaQndlwUzRStkwDtwo657ADue5KB2pmtfEFxGXHlHfuBG4lfWruJ51w9HZcPemQ98N9KxqSziyF-AYGZpbAD4J8rSRHdbBYBKe5ZoM3ILAW9k87PYaCELHcDDfv5VLzx4xrB2DrKMHiNYOllWxldFo81WNLxyE-9YQoeXAKywLc1HFiyBtNtOJZ90vAlk7Qb9bks5OMzOq4WHbTcvh3v_lAP8e5wRCJCVzDZXyUUy9ZCsBJfxqFZFl5BA9cDpg6UBgjOpyfodmXE1L2DWHbau_6xnf_F4aYVZjtt1XJB0qDAafsq1vDcIZrsX5p4ZCVu-UigQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a975887416.mp4?token=dtQJLrMfCu6ai8o_3jaQndlwUzRStkwDtwo657ADue5KB2pmtfEFxGXHlHfuBG4lfWruJ51w9HZcPemQ98N9KxqSziyF-AYGZpbAD4J8rSRHdbBYBKe5ZoM3ILAW9k87PYaCELHcDDfv5VLzx4xrB2DrKMHiNYOllWxldFo81WNLxyE-9YQoeXAKywLc1HFiyBtNtOJZ90vAlk7Qb9bks5OMzOq4WHbTcvh3v_lAP8e5wRCJCVzDZXyUUy9ZCsBJfxqFZFl5BA9cDpg6UBgjOpyfodmXE1L2DWHbau_6xnf_F4aYVZjtt1XJB0qDAafsq1vDcIZrsX5p4ZCVu-UigQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
حملات ارتش اسرائیل به نبطیه الفوقا در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67345" target="_blank">📅 19:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67344">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4c05c580.mp4?token=hNiB56Wt-nFnU3Coz3nvhwndUaU_pqpT1d-C8FZHHo5GZbuwtoekuNWLFLPuqjisnoMerbkQBRqr8k74AwQSp3kqEHZxZq8z1q0jGa8lml_ZJWnfWMIlw53HbdzMVoNCjIvvol_6rk5Fm1XjTnRS5Mct5rFCcQxYW-PUqLGbPC1KG3PUL2AC-3IRhGeiMKp5uSVUqV2HiW4-75zDjCgB8_Yui6lTapVOiE-4OgGdU6FkxkY5ccIgNgOnnkiUfJvYql43wCqqIm26k2LX54zv4Z2nWxs0h327zHu_yFQWP7ABldpv0gFfWQnvryUuiTKS5wVSNWQjqUQzDnQg4XG9jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4c05c580.mp4?token=hNiB56Wt-nFnU3Coz3nvhwndUaU_pqpT1d-C8FZHHo5GZbuwtoekuNWLFLPuqjisnoMerbkQBRqr8k74AwQSp3kqEHZxZq8z1q0jGa8lml_ZJWnfWMIlw53HbdzMVoNCjIvvol_6rk5Fm1XjTnRS5Mct5rFCcQxYW-PUqLGbPC1KG3PUL2AC-3IRhGeiMKp5uSVUqV2HiW4-75zDjCgB8_Yui6lTapVOiE-4OgGdU6FkxkY5ccIgNgOnnkiUfJvYql43wCqqIm26k2LX54zv4Z2nWxs0h327zHu_yFQWP7ABldpv0gFfWQnvryUuiTKS5wVSNWQjqUQzDnQg4XG9jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67344" target="_blank">📅 19:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67343">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a4244b191.mp4?token=fA-oGSxiP7kdd1IVQvetKQK_IZkmvm7Db9SSbus2UfCuH0W5I7XZdFRbab2oQmcNtgJL-BgQtJmJrJDd1zZhlXthPBrcqKx75dDbIMT1gOgUXg0uOpxxT6voXLQaqKXTJeqReFZZUlVx8vUmDomhqbLwiXrkoF6e8puXqibsavT6kI7fYUXSEGN1sW47kk8NSErpNE1NiLfpTKTn1NUbiilt7oZC8klq3dYIC7zZ3hXvGHm_H-H0iWrxWtPPSw7jN7OElYF5vsmPhsTKH5u7pC4cR7soVpQ10HDRD8X-UG_ffTwMdTEIv90K8WpN7XOpjuzgeszom8vgkCWu4YPu1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a4244b191.mp4?token=fA-oGSxiP7kdd1IVQvetKQK_IZkmvm7Db9SSbus2UfCuH0W5I7XZdFRbab2oQmcNtgJL-BgQtJmJrJDd1zZhlXthPBrcqKx75dDbIMT1gOgUXg0uOpxxT6voXLQaqKXTJeqReFZZUlVx8vUmDomhqbLwiXrkoF6e8puXqibsavT6kI7fYUXSEGN1sW47kk8NSErpNE1NiLfpTKTn1NUbiilt7oZC8klq3dYIC7zZ3hXvGHm_H-H0iWrxWtPPSw7jN7OElYF5vsmPhsTKH5u7pC4cR7soVpQ10HDRD8X-UG_ffTwMdTEIv90K8WpN7XOpjuzgeszom8vgkCWu4YPu1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd048f948.mp4?token=jCQ03C-tpfSJ1dfgNsBHUw-fcwnyNtparcjlOO3mXwXdRpVF8sE5R-b_Q3zTb-kPERIM3JaeP-5uYroyN8AM0ROIw2Z9rW-goo_nP7_HrbXym2Lz5rko0cY3QeTjjObFVgMZ22QiHX72Pm7uD9mdGZVsw9Ew8eWvEaGTbUO6H8wdJ4j3GpRrvZ_UHulrnoBna1RLjPBX88MLCsKte1Qh9Q4CLfHOwkkw5R6QCjgMzeBFnPdVXvRtPQIHfEHtdq9766rnQDcAEAY3IHyfxPoAjQmzWvE6rDhdNCSrykyS6anp_AAWJWM96-NlHBzsmDwoIsHhRBFN2mtnZXsdTnKR2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd048f948.mp4?token=jCQ03C-tpfSJ1dfgNsBHUw-fcwnyNtparcjlOO3mXwXdRpVF8sE5R-b_Q3zTb-kPERIM3JaeP-5uYroyN8AM0ROIw2Z9rW-goo_nP7_HrbXym2Lz5rko0cY3QeTjjObFVgMZ22QiHX72Pm7uD9mdGZVsw9Ew8eWvEaGTbUO6H8wdJ4j3GpRrvZ_UHulrnoBna1RLjPBX88MLCsKte1Qh9Q4CLfHOwkkw5R6QCjgMzeBFnPdVXvRtPQIHfEHtdq9766rnQDcAEAY3IHyfxPoAjQmzWvE6rDhdNCSrykyS6anp_AAWJWM96-NlHBzsmDwoIsHhRBFN2mtnZXsdTnKR2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار تسنیم : نظرتون درباره رهبری مجتبی چیه؟
🔴
زن عرزشی : چی بگم؟! نمی‌دونم ما که همه منتظر بودیم مجتبی حداقل برای تشییع جنازه پدرش بیاد و حضوری باهامون صحبت کنه، ولی بازم نیومد!
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67341" target="_blank">📅 18:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67340">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c05464482.mp4?token=aBVQfrcyjmd21b2QBMWQATvleTspVqxQhQznTfCFJGSw5W2u0DLDsOREzFcnfqZwbhTjB_LgHwnxr5XpjSSOiBzhgfPtVlo1oObPjaPxhdzIa1y6O0KRov-oP1ziUnHu-7Fj344MRa9oRQVjUF9wf8bwwSsarVw5fEO5g3sXhTRTu4NdLIT15h1-h22I8pWhde7OgJHOVRRJTFiIfioXq9sgysMCDKRVP-AXOtsEIeKCITrGOuSny9iM0a3FeyWfCG02Ep2eq1rOSmywTTaCuKFxeoBpifQgYebgDXSCN7x8qpw2U0OH1FQT7M8YdUExQGfMNgQteRXMR4mCBDLS6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c05464482.mp4?token=aBVQfrcyjmd21b2QBMWQATvleTspVqxQhQznTfCFJGSw5W2u0DLDsOREzFcnfqZwbhTjB_LgHwnxr5XpjSSOiBzhgfPtVlo1oObPjaPxhdzIa1y6O0KRov-oP1ziUnHu-7Fj344MRa9oRQVjUF9wf8bwwSsarVw5fEO5g3sXhTRTu4NdLIT15h1-h22I8pWhde7OgJHOVRRJTFiIfioXq9sgysMCDKRVP-AXOtsEIeKCITrGOuSny9iM0a3FeyWfCG02Ep2eq1rOSmywTTaCuKFxeoBpifQgYebgDXSCN7x8qpw2U0OH1FQT7M8YdUExQGfMNgQteRXMR4mCBDLS6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زینب سلیمانی:
شهادت آقا برای ما سنگین‌تر از شهادت حاج قاسم بود
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67340" target="_blank">📅 18:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67339">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBvIaIGb_9oVnfDmMtqnKWbP6alRXzQMx--CnuRCvho3_jR_iBVviF39hZHfjqYbqf_L18y-BZDlUPrtiMMPoVtC7tcuXAcCueN5fb-hW3fuqf3aEMGZFPaziNHsWyOfYBfjTb0eDKNqXhokqb8pulFo-4g9jqwIuwDzYmCfDwG6GI2sIbHfjD4sV8-cIPVuJdtGC0aKf8KcjiBX-ANBtlQwcC0i-ojbzYoD-gnNQnypEwPYgXCnvmjDzYSIwhF6Dk_e7u_UdLKhGp7pm_ig2SXPNgRXV0szUwf6vhKRoIGfC9BQ73Kn6HUoqwy0Md5WjRKC9wNmBRN-9EZv13QP8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دفتر شاهزاده رضا پهلوی:
🔴
‏تلویزیون بی‌بی‌سی فارسی در صفحات رسمی خود، با انتشار بخش‌هایی تقطیع‌شده از گفت‌وگوی شاهزاده رضا پهلوی، تصویری نادرست و گمراه‌کننده از اظهارات ایشان ارائه کرده است. تیتر و متن این پست، با اتکا به نقل‌قول‌هایی ناقص که پیش‌تر نیز توسط رسانه‌ها و حساب‌های وابسته به جمهوری اسلامی برای تحریف سخنان ایشان بازنشر شده بود، به‌گونه‌ای تنظیم شده که به مخاطب این برداشت نادرست را القا می‌کند که شاهزاده رضا پهلوی آغاز جنگ یا تصمیم به حمله را به سفر خود به اسرائیل نسبت داده‌اند. برداشتی که هیچ نسبتی با محتوای کامل گفت‌وگو ندارد.
🔴
آنچه شاهزاده رضا پهلوی تصریح کرده‌اند، این است که سفر ایشان به اسرائیل، در کنار تلاش‌های گسترده میلیون‌ها ایرانی، به روشن‌تر شدن این واقعیت برای افکار عمومی جهان کمک کرد که مردم ایران دشمن جهان آزاد نیستند، و از این رو دنیا در برخورد با جمهوری اسلامی باید حساب مردم ایران را از این رژیم جدا کند. اینکه مسئول اصلی بحران، جنگ و بی‌ثباتی در ایران و منطقه، جمهوری اسلامی است. ایشان همچنین بارها تأکید کرده‌اند که هدفشان پیروزی مبارزه ملت ایران با کمترین هزینه انسانی ممکن است. چنان‌که در همین گفت‌وگو نیز تصریح کردند: «تمام هدف من این است که این مبارزه با کمترین تلفات جانی به نتیجه برسد… هر انسانی که جانش را از دست بدهد برای من واقعاً دردناک است.»
🔴
این‌گونه رفتارهای غیرحرفه‌ای و تحریف‌های آشکار از سوی بی‌بی‌سی فارسی در حالی صورت می‌گیرد که چندی پیش، مدیرعامل کل بنگاه رسانه‌ای بی‌بی‌سی و رئیس بخش خبر این سازمان به دلیل رسواییِ دستکاری، جرح‌وتعدیل و ادیت مغرضانه سخنان و مصاحبه‌ها ناچار به استعفا شدند. از رسانه‌ای که هزینه آن از مالیات شهروندان بریتانیایی تأمین می‌شود و با وجود ادعای راستی‌آزمایی، به دلیل نقض مکرر استانداردهای بی‌طرفی با بحران جدی اعتبار مواجه است، انتظار می‌رود فوراً نسبت به اصلاح این گزارش مغرضانه اقدام کرده و سخنان شاهزاده رضا پهلوی را به طور دقیق و امانت‌دارانه منعکس نماید.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67339" target="_blank">📅 17:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67338">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d7e9ec8c8.mp4?token=Ba7FPDrd3gpfCy44GOc_cQmqEj4nHwkXh1rQVdg70MbtfoA9YSuByP8iAdo9MefXR_-PgThcPAXxNOnzt4y2qAVU8iZj9Yp62onCx3r97Gsh4HfgrKRenIheZsPiKL1bEP-BOXin5b7rYRdR-MmRnqVOtakIxqwa3Zw3CFIeeKyf97oAyedo1FLKq46doRBTKezv_3eNj-E7Fw8ddbtMZeThHv7EbiRwmPHdWXv1ugROAULDJyhSVO9R2cn8DEWTpOUre377LnU0tfVU8Jjzx98Wc-foP_AxFFv18GTu6BrKGiM5K_x_N5maQ6Q82K8b_oIq-fn4nDrlh_AOzGtZFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d7e9ec8c8.mp4?token=Ba7FPDrd3gpfCy44GOc_cQmqEj4nHwkXh1rQVdg70MbtfoA9YSuByP8iAdo9MefXR_-PgThcPAXxNOnzt4y2qAVU8iZj9Yp62onCx3r97Gsh4HfgrKRenIheZsPiKL1bEP-BOXin5b7rYRdR-MmRnqVOtakIxqwa3Zw3CFIeeKyf97oAyedo1FLKq46doRBTKezv_3eNj-E7Fw8ddbtMZeThHv7EbiRwmPHdWXv1ugROAULDJyhSVO9R2cn8DEWTpOUre377LnU0tfVU8Jjzx98Wc-foP_AxFFv18GTu6BrKGiM5K_x_N5maQ6Q82K8b_oIq-fn4nDrlh_AOzGtZFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بزرگترین آتش بازی تاریخ آمریکا در واشنگتن دی سی به مناسبت ۴ جولای روز استقلال آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67338" target="_blank">📅 17:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67337">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TUA7tCTL27RXp3xUBYxGmkFXG75eKfhDMmyZS3Cka1TPgbHTZbqHc2rByMJDt7-E6xcMPdqUGRlv9cNLI35NFdk0lm3FzUshWnx-BdYhLhx9hbx0J_lDvG48CPrt0RdiUwa9tmUuAY4GreQwz9A7XWK-T9FUOAfVCls1_KEgIJFciMGjosXiYHb65t9KwoI1OcS__-9x4c0JSVWToEniD-RBeqkAoOgB_2ACeoSTDFK7iej7KyvTisM6i4uMKaK28JcjuOA38P0lQ59yPDsM5BqWtpMH47tzgM00ykU8vHKbsG1fEY3YsIpEG7XYYAqJrWczjrhJpy69aIwCZAcvUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❌
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
تنها دلیلی که ما امروز تشییع جنازه خامنه‌ای را بمباران نکردیم آن است که 10 هزار مأمور موساد در میان آنان داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67337" target="_blank">📅 16:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67336">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e644784ac.mp4?token=q70Tw66BV_n5WH3j_qqEairGCEZNr8iydyIjxue9Ajf6KOx_iSdgujNG0eDvO4H77yV6wJI4eVGPe6o8E-m2yr36mINxAMQDC9_Ck0DFHmHvAV0zP2ut0B0Rf4a0OGdcjJqgge13lkbvbuJ3HLNw3aTa_Vyt9vrjem6EYvV2mKRc-I4r1sd6BFTsr1zSCySwL7KkWV7DhusR3DfUG6J8FzgA8-vR62vJgO0fTd2sWG0d7zsw1OsJdH30dfQM4uAn-B-rEYZ2gefdpNm51rBUM_mH_kRd3x4OlWwLa8hWIno4Pb6VESIA0ejehPehc7JJWSsyEnaQYdfSEVZEzjTbng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e644784ac.mp4?token=q70Tw66BV_n5WH3j_qqEairGCEZNr8iydyIjxue9Ajf6KOx_iSdgujNG0eDvO4H77yV6wJI4eVGPe6o8E-m2yr36mINxAMQDC9_Ck0DFHmHvAV0zP2ut0B0Rf4a0OGdcjJqgge13lkbvbuJ3HLNw3aTa_Vyt9vrjem6EYvV2mKRc-I4r1sd6BFTsr1zSCySwL7KkWV7DhusR3DfUG6J8FzgA8-vR62vJgO0fTd2sWG0d7zsw1OsJdH30dfQM4uAn-B-rEYZ2gefdpNm51rBUM_mH_kRd3x4OlWwLa8hWIno4Pb6VESIA0ejehPehc7JJWSsyEnaQYdfSEVZEzjTbng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اگه اهل دعواهای خیابونی هستی، این ویدیو از استاد طِقه زنی رو تا آخر ببین تا به امید خدا پیروز میدان نبرد بشی؛
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67336" target="_blank">📅 16:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67335">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAuzH58qb7iuh_3M_n5sxH-xRVqe1dG--iwzyj-BEhLQbqVAfZcV75VeYNQI69ATzuS-8ypoXGMilkQVvKeOFuH15fBxIQzr5k-ArZmgjWMQO6k5zoYtTWEQY97b3Hr4K8l8v3DXZG4kXWkXEkMUvrj9sBNvSV5cpEiKGRXBojF0ai5UgDokVse2u_Fak8yCM35m6YlxLj6mqZL-rr_8fDthTysgMB1-tG8RVSHOkaXaJvkq-46yA3oWYrXPwkjuUFEChbgYzyOBroDqOPRqupaq2q9MLZmbn_c9n8bnDiaTwUt8Jx0HMFnilF9ReJmmcQI5PJtXj8x6fcWWcp78Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گویا کامیون حمل جنازه علی خامنه‌ای مبلغ2,298,000 هزار تومان خلافی داره
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67333" target="_blank">📅 16:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67332">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_hgAq13VJbyvStIbnUF81mvELW3hetypFAJjRTFM_0q5VyX9KvNFiljkG40u3-7O0aLRsiMKuiWnfKzJAucTDH7vi7tVxACRw-pj67St-RA5YR6VtTqGaELo_vXP8hiO3E7M3EACEe16ddj_VQEfpEbjBkDWMto416UAr4nnE8EwM4PW8E3kifZ0RtFFJ9tmcfhKglxRTE2ndt5du5lvHtahOlKeSQzbLjYfOLRWEGfnE-HsyG60qqpUpgXoQZtPwLeogH76ycMhv2dk4PAd2HqQBi8NMflkKX0V8RH40rSVsZJgahiXM7HR6XRwM000wPfrJWkp0AQPP6C1sZdCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
محمد اکرمی‌نیا سخنگوی ارتش:
«هرگونه اشتباهی از سوی دشمن، با پاسخ قاطع نیروهای مسلح ایران مواجه خواهد شد. ما بارها اعلام کرده‌ایم که از فرصت آتش‌بس برای ارتقای توانمندی‌های رزمی خود بهره می‌بریم. ما حتی یک لحظه را هم هدر نمی‌دهیم و تمرکز خود را از این مأموریت برنمی‌داریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67332" target="_blank">📅 15:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67331">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو در جلسه دولت:
شنیدم در رسانه‌ها گفته شده که رئیس‌جمهور ترامپ خواسته علیه تونل‌های تروریستی در لبنان اقدامی انجام نشود. این یک افسانه و خبر جعلی است.
او حتی یک کلمه هم در این باره به من نگفت و من هم از او چیزی نپرسیدم. ما بر اساس ملاحظات و تصمیمات خودمان عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67331" target="_blank">📅 15:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67330">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWj3gIZrNxlD6REdVykmGNbuad9ideTRf6vva4W21U7Hlu_VmAMnmYwB7dgFdhKau1PuHLaeUxJ6sxqzCMgygB8X8W7g1DA9Pn_aqGPTph2JVDRtFne9_a51HfXsdWPgunHm9oBOGC-IEdF58qmxEr_LKCW_LlI5ySZXB-0b6Dnk45DCm869oEUY6oGwug0ZmmbkuJ6VjDPZXHG5QTVACqMBMMWbs644Erv4AQUT6urS4Vu1T0p2Gkzkhc1_nV9w-1lWp7o27JV7QvuUyEx69y4zPYvo0O48EVa43dU4c_G2U6FKJSjrLXZxFHSxVRNrbnCqeMR3qUkWNoi-IvBKpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویر ترامپ در مراسم وداع با جنازه علی خامنه‌ای که روش نوشته شده:
خواهیم دید چه می شود
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67330" target="_blank">📅 14:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67329">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VL5WtwZQcxY9FISi3P8MlxQMUs3eqF-mcYrIwAD2tBCqwWpCggLaqsIurueZs8M2t77yMMKZBKvKKLdVsgni2R0VQsTQC5_f93U22xeKvCtFbPs3ja8L-01eQk09B9t-Rg5TyeE24p6mrQNrts4Oe5rBfwPsNs_uSnR5zPhQYy_a1O1mqC35E0jRN83c2FZcKtl61Z6mHlqjGMiB9a8j_BZrcG05sAJMaI81eS6Rrnuo3grnbXuz8ovFgd-V9CrRyL2N8QvRULyn85vvgSvuxX9grmTlJgIpx7J-7eDbtu2MdyG7r0uBAfzPclJ0IH9DkVKZyaqA7bazueFN-urnmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسرائیل به فارسی:
بهرام که گور میگرفتی همه عمر
دیدی که چگونه گور بهرام گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67329" target="_blank">📅 14:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67328">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b8ead8806.mp4?token=bFdkAMaeLC21mmHT8gKvG76eHCP4KaFfPsPQsWkD5mKbe4v1zn7efHrcurA6CZaXOIXuZ7LahDDe_mejCyuuKjYs0JoamSWj2a2_aOCDQ7nytnyRCHdfP2oo18wvengLlCT1Pp_pGfELqyVQ3M2whh67MV2q69AcOxaPp8eGbiEnTteCDtEilfiQb4ETpziK6BNmFhKVNN68FeYW1ks8xbufdASLrZpsLC0JGRz5M-NkGvUgBryRLL6PF7oYDmDJDFKd5RLIhnHTOTQAvavhLrXVr4RkIGXLDEPQvGpU9zQYbgjPWhRRKM71XegjrKx3zUfvNxTXzLEvNaeRQ52leA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b8ead8806.mp4?token=bFdkAMaeLC21mmHT8gKvG76eHCP4KaFfPsPQsWkD5mKbe4v1zn7efHrcurA6CZaXOIXuZ7LahDDe_mejCyuuKjYs0JoamSWj2a2_aOCDQ7nytnyRCHdfP2oo18wvengLlCT1Pp_pGfELqyVQ3M2whh67MV2q69AcOxaPp8eGbiEnTteCDtEilfiQb4ETpziK6BNmFhKVNN68FeYW1ks8xbufdASLrZpsLC0JGRz5M-NkGvUgBryRLL6PF7oYDmDJDFKd5RLIhnHTOTQAvavhLrXVr4RkIGXLDEPQvGpU9zQYbgjPWhRRKM71XegjrKx3zUfvNxTXzLEvNaeRQ52leA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این بزرگوار که قبلا گفته بود بخاطر یه تیکه نون به سگ دادم اومده داره ترامپو تهدید میکنه میگه بیا کوت عبدالله ببین چیکارت میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67328" target="_blank">📅 13:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67327">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
❌
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
تنها دلیلی که ما امروز تشییع جنازه خامنه‌ای را بمباران نکردیم آن است که 10 هزار مأمور موساد در میان آنان داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67327" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67326">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0be756a04.mp4?token=jhfhZCOaSHgULCVo7SfJLCMspZDLSiUK3VdsQZlniMPJX3-o8-1Z71-ZkBLgy8YlPZPISuPIxaDwp1FOzOPxlazSDeRAYtf_MMvxtWA7GWm8D5_pPye-7PFXz5YneLqLZU1TzzJVTtJVg8BN8G5-1lrf4_MrB1W1Heroq3dE7uuydHXd7YYPHrFoNyAR26YkXZD7LrBIWFrAF75PBn8HkR0_1f-l1i4NvCf2spvHth8W7G538g81xGwFeIydWCgyMhd0R0Cm5oPdb0mdFKa_U3p82p-S6owHxwFLS-RHqP_UDf80z2CeLG50ZooCT5pLfErk1aB9MG2AGxfIMWshuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0be756a04.mp4?token=jhfhZCOaSHgULCVo7SfJLCMspZDLSiUK3VdsQZlniMPJX3-o8-1Z71-ZkBLgy8YlPZPISuPIxaDwp1FOzOPxlazSDeRAYtf_MMvxtWA7GWm8D5_pPye-7PFXz5YneLqLZU1TzzJVTtJVg8BN8G5-1lrf4_MrB1W1Heroq3dE7uuydHXd7YYPHrFoNyAR26YkXZD7LrBIWFrAF75PBn8HkR0_1f-l1i4NvCf2spvHth8W7G538g81xGwFeIydWCgyMhd0R0Cm5oPdb0mdFKa_U3p82p-S6owHxwFLS-RHqP_UDf80z2CeLG50ZooCT5pLfErk1aB9MG2AGxfIMWshuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جمهوری اسلامی پس از ۴۷ سال در مهم‌ترین رژه‌ی خود حتی به‌اندازه‌ی بند پوتین‌های ارتش شاهنشاهی هم نظم نداشت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67326" target="_blank">📅 12:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67325">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCAmB4TKeBMiWdZEz8oGgTL2OhCVPsjMb2rUSwAeiZZsMVTbSJbj8J_TSXfoEBmJAcT9vYj6STrrZ22lzlWM9spx95clEG6ZYZJcvEYOb5STmGOtu09ASv9wGAhWWLTVkfOIAuYG4DnxNC0csLp-Jd7SXE1lQB3dDJAWeVmkjHRHMLgAV6t88NMnpEq7yGd3s8GtHtj1mG_K359TZbCBv6tiiJU6eY0E22OmQj_Wyz-6IpipCVnldK-t-9JHikg7Yz8XDN4bZNCzSuI_4Lf1usSx-YHO91afm7rSBremffxi0sKDeJltNAo_H_Z1GgxyXr49nyTQgHKbxO_lqaMI0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABIfdTeaiSj-0O3YnG-pecYkKq9bBi7tf5E3n3je9TMrbJ76IHUJp92W_mqdOYt1ZTx44a00_4rkCFDnawaHzSJ9kHvfXcRtD8ch6wuldvWK5ofbdavnWUOiDNRPL_Sd3zARFriYU9uBka_iG5tFxdefsIpfbJLHFEJyXfj7uRbPlIjUCHR6LWpt_4PSK4JkTqKKMECL2YxSB8qpogjMjl6VGx_R5qv5BlG2aY7oRjmoy-stqBfsEVq2AVUWbKqGfOb4FlYTSdf9zW8B_igAuDPNxDJWJJsWj1dCE-O9qLMDlqn4gBEYpDZpEahegus5XZGJKRXL5u8w615Oqh38XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f22dc07ca.mp4?token=rYIXEvLgWCnKTetIylNSJD-FKjyYKeHP3orOGaifGA6Hqb8tHAteOFiz4WCuxOFfifR8Fqu7zczEaOUgXBoGqGaplO9HrbUAQudPsyR5ukBrf6L2zRynfFQf0Wywi0dFDwnWEjAllMtyL0J_z10i_8BBBirqIDOPKuwfzujWdSPvmqSZ6QHY1RMv28W1g5EuA0fQxIxjdI1p3INUzjD4tAlm9PLimj3Maee9BQkiu7WZLAD1u1jsR59oulm-er5wyt5bW3RzcIQaIkRz1tOzuZ8yC1ysVDM-Ja6nKu9sDUgopzZyIeNi5dl_xShAVJbrrHW305ruDmS_JLHuEReXhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f22dc07ca.mp4?token=rYIXEvLgWCnKTetIylNSJD-FKjyYKeHP3orOGaifGA6Hqb8tHAteOFiz4WCuxOFfifR8Fqu7zczEaOUgXBoGqGaplO9HrbUAQudPsyR5ukBrf6L2zRynfFQf0Wywi0dFDwnWEjAllMtyL0J_z10i_8BBBirqIDOPKuwfzujWdSPvmqSZ6QHY1RMv28W1g5EuA0fQxIxjdI1p3INUzjD4tAlm9PLimj3Maee9BQkiu7WZLAD1u1jsR59oulm-er5wyt5bW3RzcIQaIkRz1tOzuZ8yC1ysVDM-Ja6nKu9sDUgopzZyIeNi5dl_xShAVJbrrHW305ruDmS_JLHuEReXhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
و بعد از چهار ماه همچنان عامل این جنایت و قاتل فرزندان ایران چال نشده و اجازه چال کردنش رو از قاتلش گرفتن!
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67323" target="_blank">📅 11:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67322">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5f6d58549.mp4?token=X--53I4URX5FnONNR9NLurCgeMiLv7okeoOHsmna0O273D1Lc3FnOftSkUOgTVXmuLmWG_j_mg2292NMuUEEa0ZGTsdR7dfZ0ygb9qyTYsRWdf0SrsurUKW2S1GKvCmziM99KJwuA2uUJqGLuF8IS5ew1bV7FKQaRfcBwp4dxA4uZMtv7sUl4W99NvxQu0Dv1lLLRaxhX31vN5rHebjqWNbmHCaxml8U5w_sWO_YUMGMMkqK_Ci0rzwgVb_H_vfJ3CU4bjhGMjkb17UItop2OEBbqFn26OzVwzGbnjTPigRZdZ0zb4Qkgt-_8D4EoJaBs_D_JxXsn3qXFsi_YQTSeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5f6d58549.mp4?token=X--53I4URX5FnONNR9NLurCgeMiLv7okeoOHsmna0O273D1Lc3FnOftSkUOgTVXmuLmWG_j_mg2292NMuUEEa0ZGTsdR7dfZ0ygb9qyTYsRWdf0SrsurUKW2S1GKvCmziM99KJwuA2uUJqGLuF8IS5ew1bV7FKQaRfcBwp4dxA4uZMtv7sUl4W99NvxQu0Dv1lLLRaxhX31vN5rHebjqWNbmHCaxml8U5w_sWO_YUMGMMkqK_Ci0rzwgVb_H_vfJ3CU4bjhGMjkb17UItop2OEBbqFn26OzVwzGbnjTPigRZdZ0zb4Qkgt-_8D4EoJaBs_D_JxXsn3qXFsi_YQTSeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی رسولی  مداح بیت رهبری میگه برای خون‌خواهی اومدیم؛
شما هنوز خونخواهی سلیمانی و... رو نگرفتید بعد میخواید اینو بگیرید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67322" target="_blank">📅 11:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67321">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5807c7f54.mp4?token=jj2kidKifTRciB-pdD98P6f7Mh-_NuXfifxXASs6EHe3vMNR9fXa2paTzX6CMuoLXVlhR9onBHMtUhr7v1Z8P6iT4zZMoxW-cbZakJ5Bc6Ml_42q_8MNW4UFSGob_Sk3mNxZHcOKQiMFqxpfh1hMPUG_EpvhRC7pDJT7R0ti0IkP7fsQBEHlWjMf8sRktCpEF0T0QoutJI-uGpxo-guML_JZxUjSk1DCiK0gpRn5RuCRenWeBlGCzt71UNwynHp_1qa3Mu0wFurfjJbyAv7-QIPQGxOZUUCcSd8X9zcXPPqtpVTxuVCj4RydkfkxMyCIyqUHdrg2MPoKRvGKzLPYLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5807c7f54.mp4?token=jj2kidKifTRciB-pdD98P6f7Mh-_NuXfifxXASs6EHe3vMNR9fXa2paTzX6CMuoLXVlhR9onBHMtUhr7v1Z8P6iT4zZMoxW-cbZakJ5Bc6Ml_42q_8MNW4UFSGob_Sk3mNxZHcOKQiMFqxpfh1hMPUG_EpvhRC7pDJT7R0ti0IkP7fsQBEHlWjMf8sRktCpEF0T0QoutJI-uGpxo-guML_JZxUjSk1DCiK0gpRn5RuCRenWeBlGCzt71UNwynHp_1qa3Mu0wFurfjJbyAv7-QIPQGxOZUUCcSd8X9zcXPPqtpVTxuVCj4RydkfkxMyCIyqUHdrg2MPoKRvGKzLPYLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف یه 20-30 سالی هست درحال گریه کردنه
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67321" target="_blank">📅 10:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67320">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/810ada8a67.mp4?token=G75UxUcrLx8BL8oVtu1lDzVNCQ5GVGktstxG76EP0vdpfp1eRI_ixHyB4zQ45mGduvuO91RnQY8PEGlWAL04peyWXqRA5KxKn_gPstB_BAWGIXuSwZOTErvJCmAcniZHcoRaUo7zhJHRcdEeO4gCkJb9jNOwCkTKv961K7CkWdDcG5s8VoZ8Q-vCPs9qTr5l7Zpn68hcuo-oro08Agt3AFWI8QkXkT43U5ynfDi9teilxlZ1PsWo1ybaefklNOdd-yUWIJBGv6As5tGE2OWcnHxT0VCNdHVJw4C317tnZlDxWRKiVnMKvY3qRzcIq93It09u1wzsdDK4Pye8UQ19wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/810ada8a67.mp4?token=G75UxUcrLx8BL8oVtu1lDzVNCQ5GVGktstxG76EP0vdpfp1eRI_ixHyB4zQ45mGduvuO91RnQY8PEGlWAL04peyWXqRA5KxKn_gPstB_BAWGIXuSwZOTErvJCmAcniZHcoRaUo7zhJHRcdEeO4gCkJb9jNOwCkTKv961K7CkWdDcG5s8VoZ8Q-vCPs9qTr5l7Zpn68hcuo-oro08Agt3AFWI8QkXkT43U5ynfDi9teilxlZ1PsWo1ybaefklNOdd-yUWIJBGv6As5tGE2OWcnHxT0VCNdHVJw4C317tnZlDxWRKiVnMKvY3qRzcIq93It09u1wzsdDK4Pye8UQ19wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در جریان مراسم افتتاحیه مسابقات «فولسوم پرو رودئو» در ایالت کالیفرنیای آمریکا، یک چترباز پس از آنکه پرچم همراهش به درختی گیر کرد، تعادل خود را از دست داد و به شکل خطرناکی روی یک چادر سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67320" target="_blank">📅 10:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67319">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ca0cec0e0.mp4?token=W1Dz22H-G4lvArw8fsOF-dPJYWETWCCg_5lvLEr6-VMvR8pbFbYfsXuPNIRoMhA-BuV9IkyCp1DReKW6BhM9IsIM4_KFEMtT5VYJM0w_hncaa2-VTH0CKvxeniIS9gSmj3vTKQ03UgPNhfd-X6cTjXvGmwtpC3W91URf2bexOnjp1xm8f9Hhj0H_K6y9y08SKFcV0BmhZyfFmtKfEUifGMTpNYh28cdKo9Fiefv0--F5RVSX3IwI6_VHaESUVFsE0s6_D2_w3qzcDZHreQYjuUaccHVvWSQv0qj9_-7izu0l4f4Jdk2yEa9QfpqL_UyzX4q96Qq9lQuAZB_YoTYI1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ca0cec0e0.mp4?token=W1Dz22H-G4lvArw8fsOF-dPJYWETWCCg_5lvLEr6-VMvR8pbFbYfsXuPNIRoMhA-BuV9IkyCp1DReKW6BhM9IsIM4_KFEMtT5VYJM0w_hncaa2-VTH0CKvxeniIS9gSmj3vTKQ03UgPNhfd-X6cTjXvGmwtpC3W91URf2bexOnjp1xm8f9Hhj0H_K6y9y08SKFcV0BmhZyfFmtKfEUifGMTpNYh28cdKo9Fiefv0--F5RVSX3IwI6_VHaESUVFsE0s6_D2_w3qzcDZHreQYjuUaccHVvWSQv0qj9_-7izu0l4f4Jdk2yEa9QfpqL_UyzX4q96Qq9lQuAZB_YoTYI1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین حضور عمومی مصطفی، میثم و مسعود، سه پسر علی خامنه‌ای، در مراسم تشییع او در مصلای تهران.
مجتبی خامنه‌ای، جانشین علی خامنه‌ای، اما همچنان در انظار عمومی ظاهر نشده و در این مراسم غایب بود.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67319" target="_blank">📅 09:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67318">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd6157bafc.mp4?token=Zrg6SUFaFrglaSkpmkZ8MoPAZiUN8xffJs_ADDj6X71R_vMP4M3V0m-ikfcnOC7oP6kpvzwr_txNFCQiZaUUn_Z32vOEXWkZ6t9nEszoLK8ny-JO1lcSoVzUMcsFNcbctuanAWIE_92uPGRrQ1qBtB-yLECMkAjB3UQBAq4DVxFvvfcJC63CJk-y9_RhYaWqbwBBuV07815xlS1jtIir77M2CcfCIA-_Ts2B2ai2tzIMBOcFm7RlSw6hjdWejvqPZC-erPfHekPkDRQ08nrVy1EvnEarlw7l72emDT0BTXtKU_uwfiH1afPj3-bhKSn7u7O-jOP5UbP25ltrbrvUyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd6157bafc.mp4?token=Zrg6SUFaFrglaSkpmkZ8MoPAZiUN8xffJs_ADDj6X71R_vMP4M3V0m-ikfcnOC7oP6kpvzwr_txNFCQiZaUUn_Z32vOEXWkZ6t9nEszoLK8ny-JO1lcSoVzUMcsFNcbctuanAWIE_92uPGRrQ1qBtB-yLECMkAjB3UQBAq4DVxFvvfcJC63CJk-y9_RhYaWqbwBBuV07815xlS1jtIir77M2CcfCIA-_Ts2B2ai2tzIMBOcFm7RlSw6hjdWejvqPZC-erPfHekPkDRQ08nrVy1EvnEarlw7l72emDT0BTXtKU_uwfiH1afPj3-bhKSn7u7O-jOP5UbP25ltrbrvUyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زاکانی و برخی از مسئولین تو حاشیه مراسم رفتن چلوکباب خوردن، عرزشیا هم اون بیرون زیر آفتاب، صف وایسادن تا تخم مرغ آب پز بخورن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67318" target="_blank">📅 09:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67317">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekkBOWwLsi9rwIeEXAM-k-RehBvfUh_TBYO0S1iyaG44jvhpI3Bdznvj2V-uXwEhzFip9q97F55HnNy70_2YegMc9u9YKUkjAYpOpzE530X9vGbx4fgOWnhzlmvXCnTPT9Fcr5r0C_RvIz6D2RehgGoFO_3siybKbDJnhIPebSqoR4Xncthr2VhC9qZqzEUPi2SvtkLGWKCGJMNJCrvbKD4Vwq_PoQ4B0SPVQySsszZN9QUQuFrw5WhqyyDKcdxV3mXKjnTiOI9Bi-fv8KWGEj4D2njlO1Kgj55DO3u0uZ-uOAK0z-kRrZBkUr7zRCEzgPCTLjX3W4dtLWaV-qI0LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
8فروند جنگنده A-10 Warthog در پایگاه هوایی موفق سلطی اردن مستقر شده‌اند.
🔴
این جنگنده ها برای پشتیبانی عملیات زمینی استفاده میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67317" target="_blank">📅 09:02 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

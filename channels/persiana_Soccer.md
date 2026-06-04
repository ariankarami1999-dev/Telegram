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
<img src="https://cdn4.telesco.pe/file/nzACfbbfWWuyfUW4wktyxUZfm78Pu0BAtQnk6gccbfvKiWAVG85Eh0sJolt7qcdkfMJv2iARB8jX8xLN9wbjgri89-X9pzMcDub6u2T_tbN7gaA6KxJlDUFw7MXQMvbnmbY-hfJBUx7pR5GB8kSAUrtfpBl-MsXmNtk9tBkXAkWZSz0H3KUM1q2XkFD5r-xfYkSP0yUUc_3N-KWzQxO8-2OoVuKfQ_FErAVcJLvjk9GDVo6PzO740p9t3mKXbmyjFNZplS_iHiSOvK1SX8-YZLeFmyl5Tx_vb0kxdgn2_G7lWXadQu8ndDBn8PRyPZln-0ShpflkeSK902EHNAwEVw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 175K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 17:08:24</div>
<hr>

<div class="tg-post" id="msg-22770">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10d92766a1.mp4?token=cPVjOy_BvUU2Bzeo2zPMZBVw-yWE3UeLMOXvslRu3XmZMX6_smFrtybMH984rzUzasahvsttP7zdY0oudewMiNz46Jeg16geuKg23wEEbdGwhA1G4P6RO49NIGxYC--a4tgTWKptZHggINyenV3ARtIQbTyRbxEWEKDOThArFK4cfX2bpOQU3bl1EyuIBjijGNLNrt2nHBUyaIu_-DiwOwltM5N9aRWAWdjCy0AfDUAslQsz5GlAiPxoBQQz6QKgkV7Z6inf-bxgA01QyR4TYOQgw1l3yW8QCu0-ZQl_M7Z8T15V3qxbzqxam8cICblLXZUAKLGpQkEI6IeQ7x2Id2_1q4fkvrxmi8yn0zlc20IzjTOHcdJZe2beE7Pdj84YBX4sjB0cNyoDR38NyBc1rLEzMYCOCLECnUG0vpq5Zs06QpeebkV_4rmWi8OoAg8EyW1F8RnoplPGu9jJDs9JI5dR0_8gMHC2TltTNWmFoTak5J19AHeG-VrEFJBFwZm1-veCr0KBFG-Wf8tVsDsa95dDVrq7U_hQgiaqDuJn5oO72drjPZpBKTUpwuh2v8huiFObkUQ5Mlyv6o2-qntxqkZMoYC_Z7z-8bH2LgR7EatJu6HvSuVqMpW1QoDXPMbnF8vC6OSR1L0HbGVuQRaEKfLQBba6sr3NEx_Pj9DP9YE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10d92766a1.mp4?token=cPVjOy_BvUU2Bzeo2zPMZBVw-yWE3UeLMOXvslRu3XmZMX6_smFrtybMH984rzUzasahvsttP7zdY0oudewMiNz46Jeg16geuKg23wEEbdGwhA1G4P6RO49NIGxYC--a4tgTWKptZHggINyenV3ARtIQbTyRbxEWEKDOThArFK4cfX2bpOQU3bl1EyuIBjijGNLNrt2nHBUyaIu_-DiwOwltM5N9aRWAWdjCy0AfDUAslQsz5GlAiPxoBQQz6QKgkV7Z6inf-bxgA01QyR4TYOQgw1l3yW8QCu0-ZQl_M7Z8T15V3qxbzqxam8cICblLXZUAKLGpQkEI6IeQ7x2Id2_1q4fkvrxmi8yn0zlc20IzjTOHcdJZe2beE7Pdj84YBX4sjB0cNyoDR38NyBc1rLEzMYCOCLECnUG0vpq5Zs06QpeebkV_4rmWi8OoAg8EyW1F8RnoplPGu9jJDs9JI5dR0_8gMHC2TltTNWmFoTak5J19AHeG-VrEFJBFwZm1-veCr0KBFG-Wf8tVsDsa95dDVrq7U_hQgiaqDuJn5oO72drjPZpBKTUpwuh2v8huiFObkUQ5Mlyv6o2-qntxqkZMoYC_Z7z-8bH2LgR7EatJu6HvSuVqMpW1QoDXPMbnF8vC6OSR1L0HbGVuQRaEKfLQBba6sr3NEx_Pj9DP9YE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
مهدی تاتار سرمربی گل‌گهرسیرجان از طریق دوستان نزدیک‌خود درباشگاه پرسپولیس اعلام کرده درصورتی‌که اوسمار ویرا از این تیم جدا شود حاضر است از گل‌گهرجداشود و راهی تیم محبوبش شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/persiana_Soccer/22770" target="_blank">📅 17:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22769">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQmt-KCO99QsYt_WmYdsrBwjF0-j-bD7h1X9xav2-dWOnVkTmIN-91HW0Jet9k5DH-4gV7tOKKFLCOUQjRqxKtIZA3t01hSmZehjl_nV8fIOlcGni8kQqFh2Gl4PJtEpnjon2WHlhj9wNqE-Nf7R4-ckYn6rTuhaJHWhDi8U5sQCmNqX_AfLbIEPS6OS4Pc47KX4timMLCxczETCZgo2zkqxacVgiS7vodBMHPbNlE1c5HS3u7F_RxOpp1TdUFAZF11LXYD9rsPS0BBa4BEf4RF-MEhXZ3SQcgOP19DtFq-K5xedweyQDm46L_Q3eHzCl8xKKJU9tKovM-EZ8xGXZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/persiana_Soccer/22769" target="_blank">📅 16:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22768">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Brajad58XsQu_voyhH4E0enBj8jp34PbnLK_fB1qV6U5aHOeHZ5x9sL7tHVPxNk5JYdTn6aIF9JEAb6KBWruy2RErIyEQSrvMK9pYH28UqHjwh2ezo0Tg5qNlQ_p1uZgpVeK9r-tHKtZUS7Yff5fRq3O32mTsoqyLX7vT81G20A7X0EIvh02bboOgHcTVTqZKJKf9XWnth4ZLUd8HQlggUMwRlEcdeMA9mRe_ccVeXIAIay8Ryxb8obVHHxU5pUHxOPQU4nfxc-ue5cdewj-zioP9QWp1DrlRnrj_Lzj6RUSxij9-ChNRjB-mWNEgcsdsjq6xmilKBlJ3QuRSHs-0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌آلبانیایی 30 ساله استقلال شب گذشته بدلیل‌عدم‌پرداخت‌حدود 3 ماه مطالباتش به‌باشگاه خود نویس ارسال کرد. هلدینگ قول داده تا 72 ساعت آینده 250  هزار دلار به او پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/persiana_Soccer/22768" target="_blank">📅 16:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22767">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3QuBfFAldHVQbNf-cNoQEqhmeD1PyhX4cBMUgmqzF5vM4cUpgK4vQtr0XqsH5FBwefbEPWWM7dUpjkFb5fGZ3vOihQ-8RHKdvBmJJ6zoYTgtb-dwGgjeWNUhOMLwcG9BN1fSd5WHVzmMV7uxYGmEXNNX2xMxTZFu0RthBtt6QpgKr-0x-_L7sRFvDQMo2YwyCx3G1cnRwBXRmnhJ32pDx8ykFseFxgsO38at67VueOfLY8Er71ZJba_eq47EMg-6t-vxDQhxIIGZarPqo_OFVykMH7dvtAYU8aWygHFaXSsM9qfbqGapxAUwmZDxyHcsrzXzTX7fq2jTwgPDhn-Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/22767" target="_blank">📅 15:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22766">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCcO3RAWfbm7nd2K6_1nzAyJiT__4qQWedLxb3MUXkVoqP8RFnoRCip8kpXpxk62B12uQwm8p5qZO_FdTu-ARPnY88UeMgr7UW-IN6flcXoMHH85RYN84o4aYMroXBpqt8NgSPNsnHEYkrKOn71zDOhaZd4QwAH7Q7BlmK4MwGWm_Smmsi0z9BTkHuHTENFQuChbcIMVWcX5VncTat_QRl72isBjejxBr3vMRTpFA2zCQcUyLNpATNBf7NiJCwMMt_h8jqF3cO04N0Rhk7OjAYFeROft54mAzzoWVftyZ-KbxjBQlqBKTuQ0b6uGmttsCJGAv0GSTyyuKPnwRwfqkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
علاوه‌برجذب‌قطعی‌کوناته و دامفریس؛ ژائو نوس ستاره پاریسن ژرمن و یوشکو گواردیول ستاره خط دفاعی منچستر سیتی دو بازیکن دیگری هستند که هفته آینده فلورنتینو پرز بعدانتخاب‌شدن بعنوان ریاست باشگاه به تیم رئال مادرید خواهد آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/persiana_Soccer/22766" target="_blank">📅 15:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22765">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔵
مسابقه جالب بین کیلیان امباپه و نیمار جونیور زمانی که هردو در پاری سن ژرمن حضور داشتند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/persiana_Soccer/22765" target="_blank">📅 15:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22764">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qshhBdHY3mFxrS-O2739Y_OhYUiuLZY3FRpCqklgSXIybw5xz8K_e7FhUZ0_i3ucA16bpyKcrjZg4oGLCDp_YIcAB4F57dtBV2PBsv2umuoyo6YYOZinQ-mjMMhENhKeDfmBh0fQNmXXTKlHvGEyEWRLfmDF1uHjCeczpacvStLfpccUQmRLfAxpZ_l_mf_QFMW_DPBh4BCGILLlxeLBw7AUNVLOPbqTor0PgGNRqdcbg3jrK4MZFSVmIzHYLFLZl4Cu4_3bTEcW-B07h7HnF5JmHw0_R2r_0wC1MEIgnku8LP3NHDAfeFVAvk3mep6Z8OSyLMhw6fUDr3bNNANkPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛فابریزیو رومانو درلایو اینستاگرامی خود: مایکل اولیسه ستاره فرانسوی بایرن دیگر هدف اصلی پرز برای تقویت خط حمله رئال مادرید است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/persiana_Soccer/22764" target="_blank">📅 15:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22763">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsElsNA9V7CFN2_D7p9Rx0q3xo2ibCxGzG_Gv3axFj2_bkd8rMRNg0q_5iJntNqOdb5WyVzyzWyNSKB3efJN_DuFDgyXagrb2TbUQaieq2Zx-oKJcp4z2JWGZ2GX-Oc59Nc-rblOye9RsfpX2XOeue0znSoJ2L-1XGNbhQe5HzTeei8TU-wXBcUiRjs0uHWsmKd6TRyvIf8xl3gPlkCc27M3Be6xHeX-d_7spde4A3VrWcGa4Tsa4tP66ulSGM6qAfw1iXhPt9_AcKHuf9hdFsZg2NfLYZsq5GmU63j3UtsOpdJKWQtzFUnlUkUC8YSg_eUajZOayVFShyM3VJalaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این چهره که زندگیِ سرشار از خوشبختی‌اش رو درکنار زن و بچه‌ش مشاهده می‌کنید، همین چند روز پیش برای دومین فصل متوالی تیمش قهرمان اروپا شد و خودشم یکی از بهترین فوتبالیست‌های جهانه. عامل موفقیتش هم نه مربیش بوده و نه همسرش، بلکه فتحعلی‌شاه بود با تصویب عهدنامه گلستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/22763" target="_blank">📅 14:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22762">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXJY7nXhfLduGfduPaTBgxVjLVqoaC8LG_o5Q3eYLUxNL47dyBntYGpDAmIzN8V8WQL3hnW6UDY5_ERppSYqs0_1c3HAkrFToOQ7EVpgMzDEjh92kR2SlVouUx5bFDjh0mUXcNeZvG7m7MqQhuiQ5gVWrsUjvwQacsRIEjmpgWZCkqYg8hhO--EmaEg4I6m6Bb-TyDkw4OMYD8OJ3NyZ5l3vDj2bCs9-cnHfKejd9pD0bQeuuSkILb4mC8gPzA_waWPyUaIjRBMRRRs_HXNpboCqatqgH1xNHfo4kyn4NSreorTZOesMANOBXsaHT23jhGbn01vLAGmdQEeSRW6cGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
رسانه‌ معتبر اسپورت 4TV کرواسی: دراگان اسکوچیچ سرمربی سابق تراکتور از باشگاه استقلال تهران آفر رسمی دریافت کرده و احتمال بازگشت دوباره او به فوتبال ایران وجود دارد.
‼️
پ.ن: اکثر رسانه‌های‌کرواسی خبراز مذاکرات ابی ها با اسکوچیچ‌ میدهند امارسانه‌های حکومتی…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/persiana_Soccer/22762" target="_blank">📅 14:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22761">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fI5vC0zcRhMAnsxHcqvlrO3_2codGMWwNKMqBSmKomy2ote9pSxxlLHTMDuoW-pQZmiO0saogGu4dU8_O_q9Gincki02rMtoYx4bDpYa9gXPD2ecnlSnZ5QdolNkd7TfPg9uWecvDDANE2K0OpsE5Uyw3-3QhK8bVEN0_UGvwA2cMwBsPjfkcP4qPoKQ5xlCF7w9ZYOmkgeEQcABZ8qybxj8OwDNTTP_cZwMGDFC_ymKh-WlqM6HDP9VLpai66Uz6VG5q7T-1RpUQJXKarvixGhkLcDzMvtA8pWFk0t3Zh8Dnya3Inidb8oS5nKVjnAuKUpxxG3T6nPEn9sPTNcw-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ سرمربی‌کروات، موفق‌وسابق‌تراکتور از طریق ایجنت ایرانی نزدیک‌به‌خودگفته درصورتیکه تکلیف مذاکرات جمهوری اسلامی با آمریکامشخص‌شود و دیگر جنگی رخ ندهد به قطعا لیگ برتر باز خواهد گشت و به آفر مدیران باشگاه استقلال پاسخ مثبت…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/22761" target="_blank">📅 13:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22760">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etwe8mqwMf5FRXkAeU2N1wIlWHFGfdNE4sJXz69Sn9ubIqo2_h0DA_eCjINIqNuDUL1Eo6L_qhkdDlfBLbisbOA2FQIZvup0-fHSjuFA4H9jJvAK3kmpDwm98pegXohD3U_cVa5J1p7mHfZnbn4guApqPCKxz9keECOAarZ2t3VcO5naksex6K077Js2MZc4jpR8T1ByLuec3WxUjAI7av_BwTZr7OF2OcQUEmhCwODIZtn265DKPidWOnlMZVGkP5Rfa9BUhe6WYp3E0rfPH_L4Kx0CKKPf6fTROkpJTMeLATku0hLbgi4XCgf8FGRXd1d8hl-2nycmM9J3cEV5Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ اسکای اسپورت: ریکاردو کالافیوری درلیست خرید مورینیو و فلورنتینو پرز قرار داره و حتی مستقیما با او حرف زده و به زودی پروژه عقد قرارداد باستاره‌ایتالیایی آرسنال کلید خواهد خورد. کالافیوری خودش برای پیوستن به رئال اوکی داده.
‼️
پس تا حالا لیست بازیکنان…</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/persiana_Soccer/22760" target="_blank">📅 12:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22759">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wq_yUa7D6ejNJxOLsZy1JbpayxQ-amh3xGMJ0-tfsZoc3vzl5YcVZgSu13rpZK6PEt2LJOf7gO2Cp70j6--nH6mD8QTzYJBhOVOynHOeU7bffMIl_seF5rC_obEWfF6rw04CZGyKSVWouXDmoJ3kNR-st9q5Jxl63v6yphsndGlLtoP8RxiQsenVuSxlzHbJQJ_x-EgUHqkF1lpNXlXRyjwCDI543y0hFSdnxrUlytQQ_-dwiiSBHJLUyF6mIyrpCXx4YZLJfkIi71-3OL1s3xbNyQVke7LZd6jpXdMHz2vbPCFRM2i08g0QugEF6gdbTfHwniuFRlA6XsSpanVKhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
باشگاه‌های رکورددار بیشترین بازیکن در رقابت های جام جهانی؛ منچسترسیتی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/22759" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22758">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee451d1e8a.mp4?token=MMgGB1Yr9QBmfr1siEL4Ep9TYYEVWokNKzT87H0gDt5A617N5wPYbxYUQConXP3pYbQ7O3TKqMUCPZhP3WgRsQEzAN6T9ALALolPKcNGNyurXAuTiEZvMxYZjKzdCZZj6naar9Kr9OJk5hq1UkX_S-dqVItHxuFk6EwfGSinjW6bc5ozJdxRV0_LFmHOxjpz3f0ciKzxYEYI08sxcB4waHq2rleAWhn_lcEJoRlZH2Aw2dUo1uZUuMzQuOoB9VAwgmro0_Ma4FZxoqXi4vEkHsyzLnhm-jPgTyjyEPjFxxYfGfQTfhYT20tyFyxLLudG2-h-s4yTa4G7FT1sZKttTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee451d1e8a.mp4?token=MMgGB1Yr9QBmfr1siEL4Ep9TYYEVWokNKzT87H0gDt5A617N5wPYbxYUQConXP3pYbQ7O3TKqMUCPZhP3WgRsQEzAN6T9ALALolPKcNGNyurXAuTiEZvMxYZjKzdCZZj6naar9Kr9OJk5hq1UkX_S-dqVItHxuFk6EwfGSinjW6bc5ozJdxRV0_LFmHOxjpz3f0ciKzxYEYI08sxcB4waHq2rleAWhn_lcEJoRlZH2Aw2dUo1uZUuMzQuOoB9VAwgmro0_Ma4FZxoqXi4vEkHsyzLnhm-jPgTyjyEPjFxxYfGfQTfhYT20tyFyxLLudG2-h-s4yTa4G7FT1sZKttTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
تعدادی‌ازسوپرگل‌های این فصل آردا گولر در رئال مادرید؛ شلیک۶۸متری آردا گولر مقابل الچه، به عنوان بهترین‌گل‌فصل رقابت‌های لالیگا انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/persiana_Soccer/22758" target="_blank">📅 11:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22757">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPmef1jUSRjPyHA_1hV5fMV2h-GPEM3jR9IsqYbpQmsTfehzPh3VSPfQEANLSWaDAU9oa6FnnsaJtnPR4mCPXY-pN4Z6WBDZTF8_zb-DhgsB96WKTSm-KPjiLSlL1pL7RSWXzWsUu8iUdPKQYscCqPOPMu85LV2O5ThfU30DUIRotekUjTC93OWN9PfoLT061mFP4T14n8uSikpBbVLhusiqVUw16x7vskRJQ2ZFdSfd6gA0WSIE_ghhJsNr9QRLj4njCtvftw-hmPxMa_Mn4Q6SPNSOvXY2P-PolWlsWCfxDi4auCTH7BNupwrIyno3SdM5TAZ4jpFiE36N-VROOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/22757" target="_blank">📅 11:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22756">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nEZ2M-IASZew-09f32TUsx0QZlU-HMRLFyx1NuBEQPdtXWyy8zEmVEPCUXq1Zkl3MtpLMidl0ge0Xw77ostbkh6aNNJC5ThjhYx7Dd6li_9BGjHeovNU9xEGHt5yB2DztvMZrfN4nZLTyyRGEK_vOLJR0lQ2qoQ53S2XsuYNKa2K6-hm9I3SehyZnFGBLQ21kGtbQppksYcw7AuzOCiDPnBj3cxH8MTqckcik4e5jABIVlSuz5_186Uxvqm23kLnFEhfJJIHP9R6G-SSI15Oo7GKBS9Xd0h-0hqj0eOk8FQE7Pb_o-p9HD1moj7RHSuihUGvnZhSxxaezvYkdxQvFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یادآوری
؛شبکه‌های رایگان پخش جذاب مسابقات جام جهانی 2026 که از 21 خرداد استارت میخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/persiana_Soccer/22756" target="_blank">📅 10:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22755">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLVL_SyEPoFNLgH15YZkLkkGYtSIhyVK4LanIYau2qA5k6rIsx2dDTEBYWVteLXifJ398XBGVxtgvBX3GowHcXLeWxpQrp_aleicF5dPdDMoZYFj5h3RVqlXVgtKcW3TXR_vR8NQLVccwAemHkd0KOmpetsnhbIwe8Uuy7RFK1gIgoK_Fj6WhseDG-sm0Ang8yyEE8n7B0tU4KKQskvKdz2rWB5hgu2FkmCDF2kt6w3ufnx-Z6yXpw1aafHNF69bn87fR-ea24G3VyrInEFEbQWMRpGivfNt84NOS6Z_sSesKMGbB6NC1RrdNNKyc3rAnkq9snuScRQT9M5xAnmeCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دانیال ایری مدافع‌میانی‌ذوب‌آهن‌که دو فصل گذشته بعنوان سرباز در ملوان بازی میکرد قراردادش با گاندو ها به پایان‌رسیده و بعداز جام جهانی بعنوان بازیکن آزاد میتواند راهی باشگاه جدیدش شود. ایری هم از استقلال و پرسپولیس پیشنهاد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/22755" target="_blank">📅 10:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22754">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ede7c22d43.mp4?token=op4qT547l2shPakDBoHLtRbTn_63ncEfZeAT6E8df1t2DeZbyh5pVQmn0d_IZjn1DzSA0j50ZSopkOcoJV0AtCj9vK7uEjs80yPOrqxclGCQC9-bp-DShExdcS7MI0ohJfQEb0Ku8WcyyMDqg9kHXzPtgvJW5i6bLtO9syxjaydFWF0uneZ_gx6ke9yPelqqrpvikWVgWHEzyWPJsjEcwO6cijnsRit1OJWQL_q5xi502hjzG8-a8-tP3hhtDsgdKZDVK0l2D2xHNBwNupPIO2-qJIPV3go96QAN4QGUvZyjcSiOKJcic1Y_gDoiLAuvxVm91wOFkAoQcMijhLcriw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ede7c22d43.mp4?token=op4qT547l2shPakDBoHLtRbTn_63ncEfZeAT6E8df1t2DeZbyh5pVQmn0d_IZjn1DzSA0j50ZSopkOcoJV0AtCj9vK7uEjs80yPOrqxclGCQC9-bp-DShExdcS7MI0ohJfQEb0Ku8WcyyMDqg9kHXzPtgvJW5i6bLtO9syxjaydFWF0uneZ_gx6ke9yPelqqrpvikWVgWHEzyWPJsjEcwO6cijnsRit1OJWQL_q5xi502hjzG8-a8-tP3hhtDsgdKZDVK0l2D2xHNBwNupPIO2-qJIPV3go96QAN4QGUvZyjcSiOKJcic1Y_gDoiLAuvxVm91wOFkAoQcMijhLcriw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
تکل‌فوق‌العاده‌مارکینیوش در فینال چمپونزلیگ ونجات PSG؛
ولی‌واقعا برام باورش سخته که فقط 32 سالشه، فکر میکردم نزدیک 15 20 ساله داریم بازیشو میبینیم حداقل‌تو ذهنم 38 39 سالش بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/persiana_Soccer/22754" target="_blank">📅 10:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22753">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔺
بانس‌های فوق خفن مل‌بت
🔺
🫴
100 درصد پاداش اولین واریز
😀
100 درصد بانس یکشنبه ها
🎁
100 درصد بانس چهارشنبه ها
🔹
هر روز 1 چرخش گردونه 1 یورویی
😀
3 درصد باز پرداخت نقدی
😀
بانس شرط رایگان 30 دلاری
🎩
10 درصد باز پرداخت نقدی کازینو
🎆
بانس هدیه روز تولد
💵
و چندین بانس دیگر از جمله بانس خوش‌آمد گویی، بانس شرطبندی طولانی مدت، بانس 1750 یورویی کازینو و...
💰
هنگام ثبت‌نام با وارد کردن کد هدیه Sport100 بانس 100 دلاری رایگان دریافت کنید!
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/22753" target="_blank">📅 10:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22752">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYuO2L-BeZWs2T0lY4eyU49bWopc8zDMdDwL31Uiokyu3-n-XsZyKQxrWebZu7TN-gk4tjSyowElh_uvHz230F82x7xBk3WIS_CjBvX0FXA9RAYDbhvU0toGCkX4YJbxeD1Q1K9wjt7LYpf4OP_DLO9iVnt0_vArQYmg3VDPbqqsj02hznQrVzu9kqd6aJOUw_o4WO-xxL2UISOaVJN4B3A4cY3j5hJKoAgTZaB1yob9CQr_qoy-bOdXgv1ixmMaBan7Qk6kAnBmX9H0LJ433tmJH4S7EiFX5e972Pf7bc9P07RX8ZYdSpU3fcu60G89ulvhqioyw6jRn7pbosAQxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
درسته برزیل از سال ۲۰۰۲ جام جهانی رو نبرده، اما همچنان پادشاهان بی‌چون‌وچرای این مسابقاته و با بیش از ۲۰ امتیاز در صدر جدول کلی قرار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/22752" target="_blank">📅 09:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22751">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lF8kNm754rXiNs1QK0quCTA4S1dQPeElj4KxFLtAmuFl2hOFsDPD4w_eFcxqBHUVjw_Wp96iY4vnm2hV4_u5eagDeC_Gi1_SenT5y0Kz_3DKwS4Th9UAWEVed-EDONehg2eUj-5SrUZX8kDkAHE-R69TY0lN3VjzeGUNgAJS_hXeicgtlE1A_-PVK0vxuc-eMAjUgRX3TgtkbT7gYfl2rAVdQEkOwLzK0HnleWNHHPwajlNQWiOA2gcbpDPtm-waO7BCdtOX1AEYRvy9LP9FnoZv8K64W0T0Yg37KZ0NvkjiJeeNQaUPPMxWQ3N2eFvo0CwGpQOalkhinBZa0kSyFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جوان‌ترین سرمربیان جام جهانی 2026
؛ یولین ناگلزمن آلمانی‌ها با 38 سال سن جوان‌ترین سرمربی حاضر در رقابت‌های جام جهانی 2026 خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/22751" target="_blank">📅 09:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22750">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcR-Q8MXuC2mAkmqnbb-Ww3Lr9lcvvvw2l9UDOA8MDlk132C15zpvaYRZ2HtCIrkQjznKxkbf6EWJPa5NFe7LZp-vIdGlL2_yNzvPGMUSq9JgSQTwVjZqV3KsdnvW12M6j7ljt8IPODYZHuW_RV_itEPrQLadR0-JYrsrPIaaf4Razg8gNCUGyeEcJtq-WXDnNUMa8zqcckigX0d-Qjv_PCt4igTW7wHWentFgAa9SqruuGQWDg0bg9n3IGuBipJumwO1_K1h3T3qoPXk8oTyLO1eHeUTNXc21P1760NKZ3DR6jqLi18SW9cPodUQ5OUTw36X8ezbAcqZtZOyQOCgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص نحو سرچ فرکانس شبکه‌های رایگان ماهواره یاهست‌سوال‌زیاد پرسیدین. روپست ریپلای شده کامل ویدیونحو سرچ فرکانس شبکه مدنظر رو توضیح‌دادیم. الان‌این ماهواره‌خودمه شبکه‌ها سرچ‌ کردم مرتب پشت سر هم قرار دادم که هرکدوم رو خواستم سریع پیدا بشه. تموم این شبکه‌ها…</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/22750" target="_blank">📅 09:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22749">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oR-t5_rs7NOYy0Xh0sYI4xFzEP9E4F57DDWFWNoLFB_go2z8L00lwnuWkVxj0bZbT3QfVZLBG_7bqqd7hSFEwQrpkezZyvmCQNO0sS2XEbyBh9Uce36xdRwAL-FNh_sYsgG21aoUTJl79iRxMbn_d-MvpKahfjaUYH0gWi18nMf_BfKodHg86FACSZrOFia1h0iyU98e-E1tiOqn9_lLZlQl5o1Iu4h99N3vFTX6hv7wlTOcuLEcnZ4eGtFTRzHGjoAs_-qiq-lNVNGHFHQGryaYf7_RsJKk7JQVFcBmRqGGdsQqexUWpfPWqkksfPHvlU-lkho4PxbzPp-6fWXbBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
فابریزیو رومانو: رئال‌مادرید مستقیما به ریکارو کالافیوری مدافع‌چپ خوش‌اتیه آرسنال تماس گرفته و میخواد این‌بازیکن‌ رو بدرخواست ژوزه مورینیو به خدمت بگیره. احتمال این انتقال‌جذاب‌بسیار بالاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22749" target="_blank">📅 02:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22748">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQC_U9WD-VIGuFyG5tazb5DElHVIk5a2wZWs4nkbOITxXP2ftvr92jrwyhyzYDTqooiUoXgyOt97dIJFXc5zgAQ1NqJzw2YKfSsMZALVWTYPiZlc6uRLPhWAr2iwu0jVeZ9OcH3s6mT5-TyXDlZecQx0daH9T88zGg_J9jYow8s61zURTrguhJ4zcl-E7HRxXseizS4QVtjVTww2kapRnP0IHIz9ioc6jnokdYfRG5nLsZdpAplZ2hdCKABuGyYufKMOVv4Sg3H30gfIIcOcQzfHpCeEr6eROygxvLYi5GCSqmreTLjqrFKoLlzh2fPATGbH-CZt58UU87_w7SeI7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22748" target="_blank">📅 01:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22747">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQjOFqb9Merrxhis8QZYnJI6ZvgFF1SBF-wJbMdoesEbgyZevrwNN8_qyBN8kT0_LX6MfLqI-539bprOJcAROoVpBXzNISOz_U365qWjPI6H_S3DjQKVC44O2yKqmbUz0G4Ekd4JbTD1I85kdAq4LAo_W7jaXTDme4gRAFvJfYg1KTYUmim6kmp6DTwvIJ_aAbk9-tjwA7qoPUZsQ3rc60Atlxxzg0Kr-Ng2h6-8dw38jm0fww8UalW8c5gzrymR5ZsGDSQuvBfhJwcVZnAHy1SNx_ve4L4QQtHfsROFE1RBseVDHL01WW1s58qOD-vZzFL09gXboZBOFqE13HkoPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ مدافع‌فرانسویی بالاخره به آرزویش رسید؛ ابراهیم کوناته مدافع‌میانی تیم ملی فرانسه با عقد قرار دادی چهار ساله به رئال مادرید پیوست.
‼️
کوناته در ژانویه خیلی تلاش کرد که با لیورپول توافق کنه و راهی رئال‌مادرید بشه که سران باشگاه انگلیسی اجازه ندادند…</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/22747" target="_blank">📅 01:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22745">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMG4qBvKc49199hfzY1IbmfMcXqPe3MLCaXeFhODXR-CtyIz_UGcHzJs7uRy8oeUMNW3dwblR-nliamfG6STEHoiyXgdVN7wkUZCPzEqivlM4wfgJXkg1EP93ReR_hURFPAwqnAnmYStFQ7ZBKo-V9p7mokwf_0qIlpiKQuMpn_vcwE383EKeHOcZ-fCSuYHqprWEJPe2pfXw8oywwKD0mkQOnufJPBOocGxV-uIkMaSXDp9dZyyiSDeOYDqb1dhrtfCUIK7lTiZAO1sHy4mqH9O4jubea_gW5SPkFPiE5pQxON19ZQqJJI5yDaQfCPLrB8dSIQe_yc02OBCPth3SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a98b9e9ac.mp4?token=hd-pSajsQqQPXS1BGLS7hRPsYQhpCamtu8fR18Ly-fFgtYfMZrAUfuyCtX4O5ijg6dC3v6kUtStNPmyQA9BJtwJv9QReuOUa5Bfy2VBxBihRkALQDut_wo3aWXeD8Ab6ejHVOenD-Dj8nCjVTN_0k_W0c-R74fV6WrUbZYTAo1IFNqn9udCjmeFTbBEbStOQGDwkB9FJSwh1I1_LoLTLuvzxB6UFsEDuG6Z8Vn0-KzUqDwkgb4cK6FWdQaOudOweXAyApYsjitE2oq9SAtwziMd25EgUSVEMlT0mmzJI1hqxf_ZIih3AOMk-dOYUL5xz88VnUMiIm7EvBhbt_3OiYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a98b9e9ac.mp4?token=hd-pSajsQqQPXS1BGLS7hRPsYQhpCamtu8fR18Ly-fFgtYfMZrAUfuyCtX4O5ijg6dC3v6kUtStNPmyQA9BJtwJv9QReuOUa5Bfy2VBxBihRkALQDut_wo3aWXeD8Ab6ejHVOenD-Dj8nCjVTN_0k_W0c-R74fV6WrUbZYTAo1IFNqn9udCjmeFTbBEbStOQGDwkB9FJSwh1I1_LoLTLuvzxB6UFsEDuG6Z8Vn0-KzUqDwkgb4cK6FWdQaOudOweXAyApYsjitE2oq9SAtwziMd25EgUSVEMlT0mmzJI1hqxf_ZIih3AOMk-dOYUL5xz88VnUMiIm7EvBhbt_3OiYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22745" target="_blank">📅 01:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22744">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svbR7vC-96L4GaFPKD7njr-lHrD7cplek1oNP8qSytfQ-4rLXVp2766vInjuc-xznOAqvO7ehjYzi5eTOJGFe2zaRdgkGke3KdtQsu6z4lPFkc9DOeMcytf6AP5BSqo44wZ9xfvRkiWCLv3F_2zdr0_rHNSPJ4aQAHDQAf6c4GgY2h1LVKa842stlcXCgggoxGScDBY8_zsEjjh9_d8ek113rkUtwzXou94CnhiSjjdzb8njoJ-BMXpXXBvJcXnaLv8-oZWUR6LgF6hqWqOyIH5_79QJjzus3JAHQsX3GAg_sJT7H5oZ1rDR3XvC9iTT7Eo7QBm3Y5_IZ0Q53GR7zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/22744" target="_blank">📅 01:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22742">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PoykqZrWzb6lKz8Jnka4ZDglPFtFRzvlqdTzybpwO6mFK82TOry8ZExtwB4Ox6hsN8wDTFy0cX2rnVUVGxTq8VxJS3gaf6eqz8z1IXCGi2UORKcrPpdb2AiusnEdAC1-4Sg3SyzIdy2LFPas6ZaG049HpZELjElsn7s69_4BztQ-EcfSptKyQRSDlFbla75_oNM1Y2gCeTTVgtsdqabPUw2mrHqOezbnEEtrvq07vESTCcGklsByVmedthY7rIMo9z5EBjaTAXvDmE5f_ge37mes5mmwz7ZgiYm7r5CYd7md68josVhmHa1h5Tg-syDOYBQLKVfYI9cJgx8sDlh2Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارهای‌‌امروز؛
از بازی تیم امیر قلعه‌نویی با مالی تا مصاف عراقی‌ها با تیم دوم رنکینگ فیفا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/22742" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22741">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AaEr0WJBGKGOo9fknuongQ7uWE7J7L3lknXbWJOFrkzBpfPmPL1xKBgsS-21QcShvEfAq-pZPBZxafn0Lmz6dkNf-6y7_qT3QUA7X_tO_zPIDZFRtA_bUXQF_0zMQGPI8Aj4oOg4nCaJNE9EIIgpMggboLUOp02qnXQ3kINll_DIlu-i9VCZT0oHFVCfrU94xRp-IKkGLw6iioZiDf8MsK-XxwYIcLyx_GQXaLd8qrsmErslDFs-vWvTo_l8tKyoTpRBFRGYqxZ1TLqcwa7gnaqcqHZcGe5qPlFZoj-zVK1K4sEKHDqfs7v0WoeAu-5S4ECmcI3Z8XF7J0PBago0Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نتایج‌‌دیدارهای‌دیروز؛
شکست سنگین نیوزیلند پیش از آغاز جام جهانی 2026 و باخت غیرمنتظره شاگردان کومان در دیداری دوستانه برابر الجزایر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/22741" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22740">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgpjmvCxUOtkVdUXxnxaIDBJ4dR0C04yTBThT-RNUoz_0R-mICOCTW-3hmfFmNgENEmC9UgmrlOQAx01N2nVMdAH9GzzZsWOLCgxql6N9GDo1h3tN9dXU_UI5uJYYumKI784tP-bXSIUBtcH08kq45yCrRUfFPOWh8V6tdx3fmHqr6SkCEDcg1fhxi1nLxxJQhZhIpASZDqF-uj-Fx4M122Is4MUnFmvV-kpq4BVix8mKSsVYdcDg0Ey16TjFp9CeS7Z-GZI1LQXxTdJl-7OODdfweZxgZWx9uNgw7QnVXb9J-B1humjqEQXm6n3B9Z49f2iVhDNgLiUhsnOJJCYIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛انریکه ریکلمه رقیب انتخاباتی پرز: اگه در انتخابات باشگاه پیروز شوم قول میدهم 72 ساعت بعدش با ارلینگ هالند قراردادی 5 ساله امضا خواهم کرد و فوق ستاره رو به برنابئو خواهم اورد.
‼️
همچنین‌سرمربی‌مدنظر من مورینیو نخواهد بود‌. همان مربی خواهد بود که همه…</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/22740" target="_blank">📅 01:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22739">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDgKXmO_XuJ97NWPXvTx0Erg4wlQeEkFqYKGBeoZ6sLinLclAJw4JKuyiVKuxiLDrH92mmaau2zVGmHPYlI_McbkJQthCMov-vA7nTnE-JE1SXrWru1fDz30RhQ5vAlqmYaWWves8o929LJWo1KpDBje7uwJsxHmRzUDiUI_bvHIcYA4ahp-6lHTZ3CfGjQWObjeNNpT7I5tHiDZ4gEZqcdKVj_YPrTEtn47k0_HakuI0eP3BjSdWKBV7gJqXpw1p7CUtl4Xa7Al8vvu427Axf_5r3AT_TpZGtJz6g5v_XzakIrOpG6gXwTkV3HqczJnd9H_GrTQtZkpzm6iIVmxvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛انریکه ریکلمه رقیب انتخاباتی پرز: اگه در انتخابات باشگاه پیروز شوم قول میدهم 72 ساعت بعدش با ارلینگ هالند قراردادی 5 ساله امضا خواهم کرد و فوق ستاره رو به برنابئو خواهم اورد.
‼️
همچنین‌سرمربی‌مدنظر من مورینیو نخواهد بود‌. همان مربی خواهد بود که همه…</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/22739" target="_blank">📅 01:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22737">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAt33RujyxzBVJtpp19lhwx-nsDw-XKbKLUeHv2oOEipu0WwC3Avz2r6fy5FaVBPddjs3eNsXK-G0-2fePZy2_rLftd8i6LUd3Hx2gRL27U1tOWW7-vQBoLs-M0siHpi1GV2EJ9L2uzuiyT-oQRMiwvzVPxnq6TMsmx07oP2Kx6mwCCK07PxA2rhQ4rSRFwwrlIxvO2Rte0_TAmWoMo4vgowTjk8pdsXEkYCj1yjJIXy0ecLcONGG7m3Y07G_Yj9V7NbPtiUTCzNsbWU-dKtQqXGplgEcZbgGDqeXslAecxSFvHv48DEuEgR2jvalVwPaIg2g6HcYfO3jucQA46FIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ 2+1 رونمایی رسمی باشگاه رئال مادرید درصورت‌پیروزی پرز درانتخابات روز یکشنبه هفته آینده. بجز این سه نفر پرز به آقای خاص قول داده بزودی چهار ستاره دیگر جذب خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/22737" target="_blank">📅 00:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22736">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1314be179f.mp4?token=K0MaG0cOU08AZOGT22Io1OiPiE5imCmfXqCeZ2FXHoa8Ka6Cg9naK--SB2WsNzNLuRlohpR8mPXTfDEqNJZASQCYD-meCx3zGwSbkP-J501USCxQx6V9j2FvUJj3t7y2dktHGIpb5afKscyrZUoNv-p84tb-x4N75_J3va8ilvXvrevfZthprSQgc0-I_yruSqX2qB86E7ZbqS9ebUBTCElt43L8AsOrnbNAKbHxlpJi-mAqV8FhHFtJKYB2ZbzYWujPKGry7HEzMBHC-c0VZotXS5g0ri1I_aVDEMxYqvGhxOFwO8sEEWwoip41ajnnKdCyQWmKNf8iT5Y8cdTHdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1314be179f.mp4?token=K0MaG0cOU08AZOGT22Io1OiPiE5imCmfXqCeZ2FXHoa8Ka6Cg9naK--SB2WsNzNLuRlohpR8mPXTfDEqNJZASQCYD-meCx3zGwSbkP-J501USCxQx6V9j2FvUJj3t7y2dktHGIpb5afKscyrZUoNv-p84tb-x4N75_J3va8ilvXvrevfZthprSQgc0-I_yruSqX2qB86E7ZbqS9ebUBTCElt43L8AsOrnbNAKbHxlpJi-mAqV8FhHFtJKYB2ZbzYWujPKGry7HEzMBHC-c0VZotXS5g0ri1I_aVDEMxYqvGhxOFwO8sEEWwoip41ajnnKdCyQWmKNf8iT5Y8cdTHdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
اسطوره‌آبی‌ها50ساله‌شد
؛فرهادمجیدی ستاره و سرمربی سابق‌استقلال وارد دهه 50 زندگی‌اش شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/22736" target="_blank">📅 00:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22735">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d55442a50f.mp4?token=i-32rQ3Cot6QiQ3FXVW86zhcHZ7oCTihgEF08STIinvF8mQer3XK828lE_xWgAddxCX1i3cP1qGKQnZ7M7MpvnbejxYQP-mM6-pErErS39DyNSAZMICNO-6NoJfmrkCulY12kaeKP0xHmpsGh2MaX3j4fdjNUrXe1ufMCweVWdyK7dgHXzVCVFGvZfEiDYVtkZxr7NeAH5Ny9YlLm4QLuDuzLfWkUshFUuCB18VhyG7KIM0ulRhvlj2c1c604b-z8wzF-0MJmMpT8Hd8l0ACpDQjxcqUQxFwdD8t23w0c6ukS5OT_8BAksCLlLSYQNx_1K0t4JuBfxEJndJ9fVdw84WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d55442a50f.mp4?token=i-32rQ3Cot6QiQ3FXVW86zhcHZ7oCTihgEF08STIinvF8mQer3XK828lE_xWgAddxCX1i3cP1qGKQnZ7M7MpvnbejxYQP-mM6-pErErS39DyNSAZMICNO-6NoJfmrkCulY12kaeKP0xHmpsGh2MaX3j4fdjNUrXe1ufMCweVWdyK7dgHXzVCVFGvZfEiDYVtkZxr7NeAH5Ny9YlLm4QLuDuzLfWkUshFUuCB18VhyG7KIM0ulRhvlj2c1c604b-z8wzF-0MJmMpT8Hd8l0ACpDQjxcqUQxFwdD8t23w0c6ukS5OT_8BAksCLlLSYQNx_1K0t4JuBfxEJndJ9fVdw84WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پیروزقربانی سرمربی‌فجرسپاسی:
امیر تتلو یک اهنگ داره اول تااخرش فحشه ولی خیلی خوبه. قبل هر بازی مهمی اونو چند بار برای خودم پخش میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/22735" target="_blank">📅 00:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22734">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_04-Hxwnhiqss8LE8ckyQ1wfQcHxqk1PrNkKV6HESMNN87Es-FDZp_FqtcfvKJOPJ5TXzTUFmd-a5oXxitZGucGbODD__PrtQQ9RSqhYyI4WvoAG1Ocf38nMv4MEzBTNdgXUIomrjnopxpfFKsVC1HpnMdaBTi3PBIDv6OiV4z37ziljzEOdl097oL1fSCuAuZFXj3_lZ8TMonLuKWy11K-F25tg-_esTh1HoDLSd3VwiPQc2pIQA21eaD7czJ9PzcoEL2-JQDSSIyzbFdxfxEnf-yYhXPeTECWWmL2FhaU_5uKcQAinJBcG0J2IM7hQ4lISPQXgE4F6eCciVJx_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فکت‌های جالب از جام جهانی 2026:
1️⃣
۲۲ قهرمان جام‌ دراین دوره حضور دارند. حضور ۴۴۹ تیم‌مختلف‌از ۷۱ کشور جهان. ۳۵۷ بازیکن حداقل در یک دوره از جام جهانی‌های گذشته بازی کرده‌اند.
2️⃣
۸۹۱ بازیکن برای اولین بار حضور در جام جهانی را تجربه می‌کنند.»جوان‌ترین‌بازیکن: خیلبرتو مورا از مکزیک با ۱۷سال و ۲۴۰ روز سن.»«مسن‌ترین بازیکن: کریگ گوردون از اسکاتلند با ۴۳ سال و ۱۶۲ روز سن.
3️⃣
کشورهای کیپ‌ورد، جمهوری دموکراتیک کنگو، ساحل‌عاج،کوراسائو،سنگال و اروگوئه هیچ بازیکنی ازلیگ داخلی‌شان دعوت نشده است.» «۷ بازیکن با سن ۴۰ سال یا بالاتر.» «۲۲ بازیکن زیر ۲۰ سال.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22734" target="_blank">📅 23:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22733">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OoRTXPiVUtRbjgt8wpWLWJtdF56cXze7SNsRhmmyHf1WELkhQBzInrjbkeUlIUeoCbRUfniPJ1nfqJunwZv_kSXxRP0y-9aXawAaOI3LX8138QagnOK55yzpVZmhisEH18We28Lipd-0xPoJKXQ95jJhqCoCw7JteePyLL9V2Xzat5PdynLan6GA1HHymwYQVPeo3AAJu4g6OYyRhpXve9pn5kOobenXXY4e4vg9Ts5Bpp3G2AeWS4r3J1XHMNmOe5CwJ6FAttph7zjKmdUTDs4a4_0o4KukEfqpSuGRxp5APdohuO2guVKcfEhcyQAFALhtqwUVGRkN_0Z4_u9Jww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
قرارداد دنزل دامفریس با باشگاه رئال مادرید تا سال 2030 خواهد بود. او ساعاتی قبل تست های پزشکی باشگاه رئال مادرید رو با موفقیت گذرونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/22733" target="_blank">📅 23:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22732">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0k8rMuwuTMf-47D2cKUCkAdVvlFDJ-qy-BpHW6caJWVYfpg2xfTsum4M7g26FF1-W7wBBaG1W9ce8NAFd8CgSR85nzKWDqkglywS3rdqhv3PcHIK9Pg83nCx6qV1iTwstHlcjjaHtabSbKRKnN4mU5x_IT9Ldcqzq7UKfljjja-wRucTDN4IcBZUKmHBGHqYYYdSxKv7A6lS_oe4NAv28NA7ptN4yOr39-NB_WEeyOwA1hlJRPa8DZo7Qpumd6___7w7m7Rw7iwVCdhhBvnejmJn73RAP07grjT0d1yBqz-fqKHpR5sVS7JmwD4Mh6ieTULGH6588x6sjgZd0PinA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ دنزل دامفریس مدافع راست جدید رئال مادرید بزودی در تست‌های پزشکی کهکشانی‌ ها شرکت خواهد کرد و سپس باشگاه به شکل رسمی از او رونمایی خواهد کرد. رئال هم همچون بارسا خرید های پر تعدادی خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/22732" target="_blank">📅 23:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22731">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dddc4505bc.mp4?token=q_-rrlK567rBTcJ79vqtRgySOLPzK_6QvH_RxIYy3zcSckR0XmYpWMRA9kDN0P9TJ08qAudnQj9br6g0ZKYoOurqURBk4m6OUbbt3tfm2KtejaX5bUTmV37MvScZmBd34PMGkcOGnrgXYqxyzm-e43S6g1yVtiG-MuO0JWF9Pev4HptNixg4icZlbQHTzw8ZXtJjNs7ehqrtLWODs7SW4rG4gqBi-KCoaKooBY87-18ApZoeJCJKcPuuKkyOJEIoTMOdOPMa1UVTDBxh-p7nuUAz9hrneoYvgITSipBA-ufUpDKihuv6hJD37R4hvXxsP-kA89xR1IvVRDDGTYJaxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dddc4505bc.mp4?token=q_-rrlK567rBTcJ79vqtRgySOLPzK_6QvH_RxIYy3zcSckR0XmYpWMRA9kDN0P9TJ08qAudnQj9br6g0ZKYoOurqURBk4m6OUbbt3tfm2KtejaX5bUTmV37MvScZmBd34PMGkcOGnrgXYqxyzm-e43S6g1yVtiG-MuO0JWF9Pev4HptNixg4icZlbQHTzw8ZXtJjNs7ehqrtLWODs7SW4rG4gqBi-KCoaKooBY87-18ApZoeJCJKcPuuKkyOJEIoTMOdOPMa1UVTDBxh-p7nuUAz9hrneoYvgITSipBA-ufUpDKihuv6hJD37R4hvXxsP-kA89xR1IvVRDDGTYJaxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ژائو نوس ستاره‌تیم‌ملی‌پرتغال و باشگاه PSG که در 21 سالگی‌فوتبالیست‌حرفه‌ایه، 2 بار قهرمان UCL شده، میلیونره و با دختری که عاشقشه زندگی میکنه؛ برادر در داخل و بیرون زمین زندگی رو کاملا برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/22731" target="_blank">📅 23:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22730">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R67oIncbEAROoPCc7VVqRW8u3RL-qxqgJFh61fKxux9ngLn_-4UJORqq3Zd_Jk8GyIfpoVe2YRH1Ph8IvIIrk8iOrYspo0s9IMGG3STUEmwv7U_E5mqV5osTggS5xqxv5-tZLrzz55LMlop60eA5pO_wSDb8rL6TPDjuX_0f2Oq8OQW78EbnQLBE311PMj0wbSUYXLCiz2n-WHpkKLbSl2LiI2btEu2_rWRiAmcABE3vQstVoF8ht_LCeiQ8ZaMQvLOi4AZ1-IPdoujWAv7fNk8afMVXMSKgyMMQUv2vPEul6_HUYLoU2AFlZYbaLamRyTVxZ34zHZKSJjqn99oZnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تغییرات‌جدید در‌قوانین‌فوتبال برای جام‌جهانی:
برای اوت و ضربه دروازه، شمارش معکوس 5 ثانیه‌ ای در نظر گرفته می‌شه. بازیکنانی که موقع درگیری دهانشون رو بپوشونن با کارت قرمز جریمه میشن.
تیم‌هایی که در اعتراض زمین‌مسابقه رو ترک کنن، با مجازات روبه‌رو میشن. بازیکنان مصدوم باید حداقل یک دقیقه بیرون از زمین تحت درمان قرار بگیرن.
وار اجازه داره که خطاهای رخ داده قبل از شروع مجدد بازی روی ضربات ایستگاهی رو بررسی کنه. VAR همچنین اجازه داره کارت زرد دوم اشتباه و تصمیمات نادرست مربوط به کرنرها رو اصلاح کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/22730" target="_blank">📅 22:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22729">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGdhnZ3mB9AhzFaZ2FwhiUtWPrz7S9I2MURby-qDt15XwIbm23WYgYP45o4OGN7NDVgKITlZaxWbeG0svX5PBoPQGObpDiMJlg68QcCME7_mItWYCw2DoN8rnKCOZy4UPO1VeElKPaLPnWO6_1hRZln9pIbPQj7cB_GUdOr4yWHqcmKFDL3yNQTmmU-ILQEtPOhHMqeaJRjcWIWg1y3DvNyEVRYBngromEx8bv2o3x8Fu263D_vXnpP6g45e8-mDHqB08eJJj3Rg0BF28rhSJ0v4CE_6WOq_feYJ8-fI9fAvPCQWv5fKGc6QprKO7eoX9YjCi8qY5gs5-fYxDJ-bfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برسی دوپیشنهاد برناردو سیلوا ستاره پرتغالی:
🇪🇸
اتلتیکومادرید: تا سال 2029؛ سالانه 18M€
🇪🇸
بارسلونا: تا سال 2028؛ سالانه 8M€
‼️
ستاره تیم‌ملی پرتغال آفر بارسلونا رو قبول کرده و بزودی این انتقال به شکل رسمی انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/22729" target="_blank">📅 22:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22727">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrKQrFcl_C_riJFgkzgEH5shHzHxj0Cj9N8GtOCLcOoTHw1ByC6GRwgq_Ol84kYBr8yZUe4sFM7At_te5fY7ZKlnfki0ekZOvfkyw7hPb2KaKRBdf0xewZjMg5h4OrA-68rOpvY7of1l4PsJPufvOOHuD_49YR4pSllttNA0kx5ZCdmO5P6DD88BBiJFXm6cgwBfuq2u4B2nxoOy5QRBcaau1JPKTTpGV1esoRX0QSwT8ZYMqACyQqeqC8cs860QJ5kulPO0V6zvTFIf9LA79KIhBj8E4s_4ty6ZmaFWN6cd3zSipHXpiNKwsFbIYtv30PF6jpjzA6uCmJntxpEGeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ دنزل دامفریس مدافع راست جدید رئال مادرید بزودی در تست‌های پزشکی کهکشانی‌ ها شرکت خواهد کرد و سپس باشگاه به شکل رسمی از او رونمایی خواهد کرد. رئال هم همچون بارسا خرید های پر تعدادی خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22727" target="_blank">📅 21:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22726">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQKDvhPyb8fkPaFgdnWgluwrXfsDbwAPi7A2Z2x6C8ckBPI0AEKyeS7ZzFvJrw7ZPtecOASQtf02HmzAduHO2USiefg6cGSkRJh2pxuHGQYQyHqMdW3nYnKkqBXoMdeNejTa30T3pQHePDOqlMrrw3nuCgAq3-Fmur-MQ34X0Bmai2HFaRYLEPl8-ZjiMlHyVuKTlwOaJ_kIdALNnDupaMuZGQ_bI8OP7kqAOQGpJBQlTLKiJaKtWRVVAADLU-RDlYdJooj16qifVo191R2olqpKHStqV7JKQek68RFbqOdJwkCqgYic_ltJpsdbTdCIomPPIKSQ-881f9o0Tk_Jng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
طبق داده‌های سوفا‌اسکور، دیگو مارادونا در مجموع ادوارجام‌جهانی باکسب نمره ۹ در سال ۱۹۸۶ رکورددار تاریخ‌شده و‌ تاامروز هیچ بازیکنی نتونسته دریک‌دوره‌ازمسابقات چنین نمره‌ای رو بدست بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/22726" target="_blank">📅 21:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22725">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oe2DOnqW-a9WhIZavjka8glgKkxbJ3GvdG3l4rnWP-kSaXs2lgMy1mDIoa6FjKvpWDKk8ZdiDlqQIk1H5i8havpH9zBFLIhDM6UM2sy_duspyYEudKxvzHQ8fwZDRU0reaD5l1z3O9xhbqBHYfb2SIVZFfLaka1QOtoNRb-EwunyfUSlxONw35XPOnabC3wKUtaIRPWp04G_6ijdcBrZzp3Z_qiJRm51oeQMPfb_MvJAPuFtvRiNgaFt7CPOHyX-sXLXx7LKIHJVPFqpFrh09HRWW7LOIFu0b2GwF3tN-OyvoF0dnN27ucXmy9HiQ34fdwRO2bf7rLZBrgnDnLJxGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دیوید اورنشتاین خبرنگار معتبر انگلیسی: دنزل دامفریس به احتمال‌بسیارزیاد بعداز انتخابات ریاست باشگاه رئال‌مادرید باسران این باشگاه مذاکرات نهایی رو انجام خواهد داد و راهی این تیم خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/22725" target="_blank">📅 21:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22724">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">توپ ترایوندا آدیداس یکی از پیشرفته‌ترین توپ‌های دنیاست که فیفا برای جام جهانی ۲۰۲۶ انتخاب کرده. این توپ میتواند در هر ثانیه ۵۰۰ بار سرعت، جهت و چرخش توپ رامحاسبه‌کند و داده‌های خود را با اتاق VAR به اشتراک بگذارد.آدیداس‌معتقداست این توپ می‌تواند بادقت میلی‌متری و زودتراز داوران آفساید را تشخیص دهد و به سیستم تشخیص آفساید نیمه خودکار کمک شایانی کند. این توپ بدون سنسور در فروشگاه آدیداس با قیمت ۱۵۰ دلار بفروش میرسد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22724" target="_blank">📅 21:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22722">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1amXcY3S5KfDsxyTAb8U2R68JspFML1ycRpMLOu0BWng47jicT7dyHgjaZ1UuqbaGSj73RhQoL6FlkuihkWs8_TSs6wfar-iVcO3MaavtWlM0a4KOsjKGLyjmUmMqGGex3vaLpuSSrI5MS_jo4YztVZz9OlmGOKiuEDga4bl40p02pTSQqqAYyw3nkFSREHMdfvq9KdCE8ki9RUXyfV2-zltSWKf3Xh-cmwRLpQcUT6C59zUY71jt_bCGDqnfQwwVncLJ0bPHdzFVGt1RB8RmLWvRinvotX3_S_FoFa-H6jIXa2ftaLTchglbvl7cNNPcm5edkyV2qfcotHQgfFig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
لوئیز فیگو اسطوره‌پرتغال:به‌جرات‌میتونم بگم که اسکواد این دوره تیم‌ملی‌پرتغال خوشبختانه‌ یکی از بهترین اسکواد های تاریخه که امیدوارم با کریس رونالدو بتونند به قهرمانی جام جهانی برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/22722" target="_blank">📅 20:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22721">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIxOl-KnZ7MiLio86xABXuhRDiEx-ClU7A8c8QirsvlFwH_DHxjEq8Wic3TNy7xzCHbfIhTfX1jE5RIPkgBNEy3JxQ50wkNbU9B4P75O13muEtx2Mnxnr3o9Ehkzg7wPkgTg5NlIFhoWdMFReAKvftPRleK-C5hn4C6KPSZw-1FOH4K0ZPhi3Orf5c2UCJbxdnVHcde_4K_jG1vt0W7Oe_J9qk0Pq1zmFZg6osYfNq1zc4HNi0jAu4lSDJjGHQa8nuK3gIqB_fBhwwk4Mu-ah92qrGvbs63RGy6TEbrMt1Ofjp0XH-bOqvQ9uytijllrLlq8cZWOvoJ3_0l_nGcUDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛اتلتیک:انزو فرناندز ستاره چلسی به سران این باشگاه خبر داده که قطعی میخواهد در این تابستون از این تیم جدا شه و راهی رئال مادرید بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22721" target="_blank">📅 19:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22720">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R21VPaJQTUx0rUNdR5Ex8rKHNxNqt8XswZHuJkRda_3ZfITgzWYz8dpcOCUQuK5Uywjni8-u0ZvqlIhc0KJm9tANpqDph6IvhnHNtDPiWSJaY8-IWGKKmYBLy9ekU2es1S8tyuAwCdfTryx_Z29Ujif7U5gnTJwS9M9jb4q3p9sYysqBFH_TGjaZ9Y4uC0A2fDCdmWxJDC5P96ex0WQhUsNCZOvzpW4g0sHK4IdCL6NhdXw1FXzAqp3Wwy-8JuTd_Mrpeuq9rxirCWoxIHmQ_6dS4l_vHfG6JQLpMnWY6njOxRZ4DMh_0BhHvr6L7BIzi3FT753fRxvty1RRgQSnJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌آمارمثلث‌هجومی PSG فصل 2025/26 و آمار لیونل مسی به تنهایی در فصل 2014/15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22720" target="_blank">📅 19:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22719">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KzcQpghcsmh0Tb7r8qne_azx6NeI_X-pouYsXmgrZcrW83enVMJHdJeiVp5FixA4-_H6hvChl7u0OocOmLtQjaIuo5xRviejcUzFOaHOJtGWj-UC2J5Pd6a5VH-rVPWHRgkNlHpe8psQT19TH-J7ErKvbAHkfA0H90GdPR07krn-NMx4GWhnmstHyiiFctXuPn-VVob5oB9w9x5g9TbT7Gn8XGU9BoHI9xjQP_sALZiUfflHIarh2EiCYvrdmnV-NRoQcfzmUeEIyVPRCoMM5KjwOQj72W2jvBfL1FNUC_fJYNqzZLYACw_PHtIg6OXSUZn04b8kL5_Nan6FrGjRVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#تکمیلی؛ بافعال کردن‌ بند تمدید قرارداد اوسمار برای فصل‌بعد؛ باشگاه پرسپولیس به بازیکنان این تیم پیغام رساند که هر بازیکنی که قصد کم کاری داشته باشد قطعا در پایان فصل از جمع سرخ‌ها جدا خواهد شد. ضمن اینکه تا این لحظه جدایی عالیشاه، رفیعی و پور علی گنجی…</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22719" target="_blank">📅 18:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22718">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GijbqhpHzmJosBCXp8_3pWBBSCro4IbIWM3qV0hY72bVeIzLrO0r_kSC9bN0hzijZClCvJbyrTI8UwbOH7iD_Kf0gLfKNnxebm-nCL2bkbz4ZPiAnN5WgvgDGwWJcUQsJsOCUnMj94D_NI2CrPmFe0XUdraDGk6zI8_elIGFofbY-w31m3hXNUQXvRxW-aQZ8c88l6-cN9Fonzu7KwyDRRn-bqjiFrU-TFxFsJRjXdPzTplDpBWG6O8hVq5HynfXDZAzBJEONRMNpDGRWUnAOyPf_Sz9S5FsD_eb2zYLPgacNjORLf_7h-2agJfJEOe9tNGE4T5QR_YSN5KTJEixyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات
|با اعلام رومانو؛ دوشان ولاهوویچ از باشگاه یوونتوس جدا شد و قراردادش تمدید نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22718" target="_blank">📅 18:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22717">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyaOEA3aQcVbBF0eIW8oer8s2CjztaKqgLvOoFAQk8OPAy9S1RALl0i2qN7AJgzpXncYU1p2YKA6TvEgdQAM9ctO8iAxU6b-CcI12xokRMxMkoB1jcE9_N82vxDHKpRWKok0HdeGRkarJg8oWTuxUQXmiaa4yHuvrnwFparUcdWlcfYqaRkF6mZl2DIBGlRIf3EYbkKoGmNYModiHq_9i4RfPNPTz-0WtSX3v884oAgl8OJHPYsbaeszNL7RSXRPOj5vqReK1_nx8aFBbBRKh8nTVE8zBwjTkgyXGarc4pIrDQro5UoMTh0DXqHZEAzlCmy2ZoSoN52B6jg4NVuIdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسپورت عراق با انتشار این پوستر؛ خبر از عقد قرارداد دو ساله یحیی گلمحمدی با دهوک عراق طی ساعات آینده داد. هنوز قرارداد رسمی امضا نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22717" target="_blank">📅 17:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22715">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uoQ9AL8LMLPrQnZoL9u-i2kEHA2glNqXojB6OYYDlfiCsv_-gjlC0OP1qw-teNrKH2CMbV5RN3WmTEs_Ii2e6ngm911eqJnhD5perXWGWoEsHKf8m3tW5RbglVpIqUWeEU9DZ4ZjZHjogF0wiVfu3BMrvTLXSZWUPon-NT2sJkn0jDfccnXlH9Z35eTaWAhlGLB2XXlZ4Xs2n0hNW1vQsqrNG5qT5fU9iZDXKIsyVjJlWP6stSIhSAYBlRnnLfvx9cVSw7pCgN3GQBQDsnrpKiw1nPXod6F7iXkBl30-mhEZyt3_Xe06M7FTxZ1bxOWaSPDnHKh_zToQ1_39b_-TRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ufslUVk7oVHOGVN6YBUvxjTkbLeJKiab9RZ1PlE2Ndax_WaoQmF0GUvVa93SKryQJhhF8zw_fzg8IM6nPdop-4keQRGI7BIRVRSsbLxaZzsvyF6DUpBRh3d9Q7UCx23m7NIKnFqKeo6hGxbSxdXugj14ybxAnzUwq7Mjy18k2YqyEcs8TByTXATsqlVlHC9hckMdlsIEq8-ZvNDOcNFnc4vZ5RMdXH-ztNpKBQVe3AT7ns2Alt4cyTYoNSESAbEIjdWQ9aFm_jQSIE9IRSnVXqUvqyDqQjCftCPejGN_PJDp1LYMtUdZJfVOUv5SFmsoAETJVs2AtWCmOdBvPbspRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇿
🇮🇷
ترکیب احتمالی تیم ملی ازبکستان و تیم جمهوری اسلامی برای رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22715" target="_blank">📅 17:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22714">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e93182b0f.mp4?token=XrQMkJWY0Zoy0dV5l3ud8M9nS7dU3Qw8SDVFP_rEgpmIOuEZ5tMZSs8XAF76WuUADW_kSWFa6teOSBN9kZdXL_4YpPYQYhnHBqJJVIVKoJFLPNbvtqF9i2G36Dg5LyMGYaGy7o7m3Mq43mkTO6prBFOZF0aZbfk3qtL9CzbpauW7ZnccEpYtZOPCoA6l4puP5Y6-ys8Zv-eWSmQ3TPGR6CA26TzteYLyrbWDsKZAaBcQPjFTw0dZMYwtqS0Xwmz7PBfFBcOW-rfxOsOvv0CM5eCkompSpgpa7QnIuI3VIk_llZCL-P08Txg1ayw-DRZlVYPQgj53Ka2_IJgJrZYn4TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e93182b0f.mp4?token=XrQMkJWY0Zoy0dV5l3ud8M9nS7dU3Qw8SDVFP_rEgpmIOuEZ5tMZSs8XAF76WuUADW_kSWFa6teOSBN9kZdXL_4YpPYQYhnHBqJJVIVKoJFLPNbvtqF9i2G36Dg5LyMGYaGy7o7m3Mq43mkTO6prBFOZF0aZbfk3qtL9CzbpauW7ZnccEpYtZOPCoA6l4puP5Y6-ys8Zv-eWSmQ3TPGR6CA26TzteYLyrbWDsKZAaBcQPjFTw0dZMYwtqS0Xwmz7PBfFBcOW-rfxOsOvv0CM5eCkompSpgpa7QnIuI3VIk_llZCL-P08Txg1ayw-DRZlVYPQgj53Ka2_IJgJrZYn4TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ازشوت‌های فوق تماشایی گرت بیل فوق ستاره سابق رئال مادرید در دوران حضور در تاتنهام
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22714" target="_blank">📅 17:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22713">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pINf0KEr-2fe2rXupbC6MyCfqgAGxzLWA990f_xw8jLegnHCOQdOggR0rGmH38egQ_zN9bcI8v-NQE4Ly_XjbZs4or5NndrOC5XqqTzTu6KB3pPXWaRDR-SvQsjLUfaAPQ9J2oU8xHhPZYQnyEM0ofdmXyyoIGENjAIjvV7V9JXGozv-Q4kjUlvFveDLfbVhv45_M4AQJ7nmPmQfDKLmv6eiq_hG1-6YByjgUo7sA9-fz4P7TpzkT55JYzbrSdEZj7NvT8oO8VrupeIh25XSW3N4VX5DPMgYuW_BsGumMiiQcTpQApROvN-WENrPR7ZtdK_SNoaXEAiH-Mh2oJEq9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ یحیی گلمحمدی در روز های گذشته مذاکرات مثبتی رو با باشگاه عراقی خواهانش‌ داشته و حتی توافقات لازم بین طرفین انجام شده اما منتظره تا تکلیف نیمکت پرسپولیس برای فصل بعد رقابت ها رسما مشخص شودتا درصورتیکی بنا به‌هردلیلی‌اوسمار از…</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22713" target="_blank">📅 16:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22712">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3iiVwfI5fMc2CmFmG5OoVqrsBnMgGKFxnpqMSneSWKOi65NBopm-6Cbkha9RewE9Y4OjB3oPWXW1GHOdu0D9zMJSxOASvoL3Y3qyRDFgDAzlFODHxH7y9-GwrfvSt5a60vIHdpXjI8MQEaSMSFlnSieNmmlq_kPU088ZzFzy-Xks4ONzBvClYNeGC88FrNX2KNr-4XeztG1L7bcP5mICG8VY-E5TPyWcYewolyPrwNL9xUYasm45cihhM3UlA8F2lWSyytNPIm3iGrhE-C_K1oXQpdjSnlPaTtRqb1DSRD2Z_tlx0jW43VGlJzTOyOQk50mSUvX3HbFpyAmoO92dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
#فوری؛ بعداز توافق‌ نهایی با ابراهیم کوناته؛ هدف بعدی باشگاه رئال‌مادرید برای تقویت خط دفاعی این تیم، یوشکو گواردیول مدافع جوان منچستر سیتی است. پرز به مورینیو قول داده بعد انتخاب حداقل پنج خرید تاپ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22712" target="_blank">📅 16:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22711">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6cb529dda.mp4?token=YyuUtkg8Uf3ZQMtJme3bXu9Hm10Vh_2cBmULrna0PH81mm3B4RI3xaQ3E7lAzBRCKDV9O7GkaMMZnAEkcF1udFpY0vsLFVCYZ-TUtVVR2DTK2IRkfgOVGMCc7Bz5ubAdJbNOELN-Oo1xPHb_PMzzQ0vZoPWS264rG0Ib__tCcVPt80sJq278y5lyozcwjWW5W9f0etQnYz5UMBxcG5qjndd-5jLQ7SfP9KZz2mgIH5YH_vYfI38sijSavuHTpHyYDL_qL_8wSEMNtXaUFhUSMPjgqKvQuED7Kxa-4UVer_ePTJyWloIr5_b2vXrfrK7kMoOyi6_bPQ2arNdo-RgnZIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6cb529dda.mp4?token=YyuUtkg8Uf3ZQMtJme3bXu9Hm10Vh_2cBmULrna0PH81mm3B4RI3xaQ3E7lAzBRCKDV9O7GkaMMZnAEkcF1udFpY0vsLFVCYZ-TUtVVR2DTK2IRkfgOVGMCc7Bz5ubAdJbNOELN-Oo1xPHb_PMzzQ0vZoPWS264rG0Ib__tCcVPt80sJq278y5lyozcwjWW5W9f0etQnYz5UMBxcG5qjndd-5jLQ7SfP9KZz2mgIH5YH_vYfI38sijSavuHTpHyYDL_qL_8wSEMNtXaUFhUSMPjgqKvQuED7Kxa-4UVer_ePTJyWloIr5_b2vXrfrK7kMoOyi6_bPQ2arNdo-RgnZIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
توپ فوتبالی مجهز به هوش مصنوعی که به تشخیص آفساید کمک میکند در جام جهانی استفاده خواهد شد. توپ رسمی مسابقه می‌تواند داده‌ها را با سرعت 500 بار در ثانیه ثبت کند، به این معنا که هر ضربه به توپ تحت نظارت قرار دارد.⁩
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22711" target="_blank">📅 16:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22710">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/htkiiji3wCPVF1UUgURK7xtYOcOEstE8xGU2w16YrJF31tRsMpurxcW8ouzbJaJw9IQ8RcNhx4FK7PXZr3NhIheJzzRxjTWrqUUOu-qxuG8K4KrP7SRgMpTXuoD1R2JGnB8lrRg30whrypNaEFGvh8cHxLB4b0QKz786HxHpxeyyUTJUyFOD45Y4-quRXNjkjF0kJvsBiFApAVsFSxEB1pFHb4awGYZcnPJJQWlPdkpHxginJb_igPTtJvLIx-VaCXFNMJh77Et3XPPORqesKiFTSnb5xOjv1rr-skJ9sO82qq-Bdvuy45JKWoJH10RyJL3WOQp98oj1kvh_eCRuYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
#فوری؛ بعداز توافق‌ نهایی با ابراهیم کوناته؛ هدف بعدی باشگاه رئال‌مادرید برای تقویت خط دفاعی این تیم، یوشکو گواردیول مدافع جوان منچستر سیتی است. پرز به مورینیو قول داده بعد انتخاب حداقل پنج خرید تاپ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22710" target="_blank">📅 15:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22709">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdXVQWp3lQv3LlBKdW76yCQcmsvRo6RmUDy66nI3pZ-Evq1djNnCTCyI9Yr_EBO3KJ8ViJeIOBZBycUMsMlQ80Hmenc5nUya5uK6GdUEN9YVTUXKhaFwViLSLySM5LpdwNMD4o0uFBbfaQsa1z1yjKHdGV8Z4TcUM2TtDG0OjoQc_qFXk-YJpJmnOQl_eGcpZ4XkRMMughvJgmo9Hu6mEfCunCcdffv2JGvgL0dandfpYH9pAdWu025dn1zl2az_Bxua_BpRpPwnpqA1C0dTEnSxtc8oyQVGn4EV_8BrQhiFKfIgjQFJrwJVhDU2g85sulfqnWDr66_8JGCVuR20hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باحضور دنیس‌وسامان‌از تیم جمهوری اسلامی؛
لیست کامل ۲۸۹ بازیکن در جام جهانی ۲۰۲۶ حاضرند وبرای کشوری بازی می‌کنند که در آن متولد نشده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22709" target="_blank">📅 15:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22708">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rega3B7bNisuHDGq2Aqat9d1nxXftJdMJnMg-TVcH5nVO1IsZ65H_w_POnP-7T7NPAhC2tFyY-pZnNK7xvpqhUeJgANdKtEtGAvI7Kx6_biAN9dwKl0skFzO67zP7wieAdcD9H-39wqaDj9MAh_CSGeNIyQyBGgiiP1wcYcp5QdQMTGFML9CwstlFzo5ggGrs_IcMpMcghRdjIK47Jp-47ku-n4-tbEVcv-Wfw2kR0GwD3B51-3x5FFygu_PiICFqGMts_xiS7ut-i8wa1_CjR5Rc84kIXxzzpzZQW5RJXqElEpgIMx3TGPkqzyyV0v1mPkK1Wv9WBlrm0-7uYb0vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار هری‌کین‌مهاجم بایرن‌ و عثمان دمبله مهاجم PSG در این فصل؛ کدومشون لایق توپ‌طلاعه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22708" target="_blank">📅 15:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22707">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfWwQ-7s4VBrPDxmlapRwFM-4mL13QAukxSmu6tDVYWvuoLojyVAWMXZypiW0TMcXPJaTNoAchi0kUw-IS7wdvrblzOwSrBNbmsPcz7j_CX9dpGqgBrZdth_d3zb55kEqEjJFj5-P_023Fl1ufbSYCkE_n6hjgreDN4f4jbokWusSkJkbaiXQKDjl5Y5OnyKQ-E7M5s5boErHzHbb9UXPB8gu0UtNq3WV9Z4jCfNwkhJ2TFlYcBWinMxkJuz9AfL8l6jQC-AN075g1os0gd3mrKm7lz3eelBwKiQRf3NMU4VVoaPzP17y6syf9b8wBFYsRz3tSMXrsqvcHhP-NHtyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔵
راسمون هویلند: امیدوارم‌که باشگاه ناپولی در پایان فصل بندخریدقطعی من رو فعال کنه چون حقیقتا دیگه‌علاقه‌ای‌به‌بازگشت به اولترافورد ندارم. برای من بهترین بازیکن تاریخ کریس رونالدوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22707" target="_blank">📅 14:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22706">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0jX3kegPrHhaEQA1BKAFxcmESNKEvI9Kdc-GOHag963Ta9lXt7rKs5V5thJilLMsODfgPPbXbJ3Ox0er4IdAYeFSNdfQq62wx1ZNtmZSQ16GFqVtbz3eXEYK78UTfjPVqdSqTaaQ9U_EUJTQ6xkGjSUOoPX_vbh3o_stDUK6QWdykkqITDPPEPI2KS39w7SUTy9dQJ-vQ283rXndiKlLMMf1NcEm_7JyY4qUnV33r9vU8K8p3zmrAozHDyM5ufzsSkAMCdlcdv0L_J6O4SQhqCsF84CPKmzC7wbcVD4tgFQUsCmjccHobFlMqfu25atyPiW6JOrAUqcqJcPrwoffw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💣
#تکمیلی #فوری #اختصاصی_پرشیانا؛ یحیی گلمحمدی علاوه بر دوباشگاه‌عراقی؛ از باشگاه تراکتور تبریز آفر مالی بسیارسنگینی رو برای سه فصل حضور در تبریز دریافت‌کرده. مالک پرشورها قصد داره یحیی رو جانشین محمد ربیعی سرمربی فعلی این تیم کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22706" target="_blank">📅 13:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22705">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e0818cf5.mp4?token=DdjCWJz32nQPH1vwxz0q0kkFeISoBWoqLFCzec6quDiBMYVub43-yXf_l50YsS2cdtYytQRlVm8yebbh9fq5Txr6fv-jq5P-m8CAi-tTZV9YipppeqoWn2N9iC2eDM8osSLDsXAF2kBWOXjaEKgV2ENdRCWZSa00SwRrTZ89V4h0MpzDwv8LEOTr1JPE8SuyTc7G596F31zbNRoNBNG08OyQ6lhZtvYjHibqPGK2u3AF3-BfMds_WPprkcX-K05AlgIZQhQSCIiB_gnJwOseGBuMCtZCYMqUPGxI7bxp-bDvXqFwVRj45QMiJIP6F3_wpi1k4PvsmbYd3VthXSOHJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e0818cf5.mp4?token=DdjCWJz32nQPH1vwxz0q0kkFeISoBWoqLFCzec6quDiBMYVub43-yXf_l50YsS2cdtYytQRlVm8yebbh9fq5Txr6fv-jq5P-m8CAi-tTZV9YipppeqoWn2N9iC2eDM8osSLDsXAF2kBWOXjaEKgV2ENdRCWZSa00SwRrTZ89V4h0MpzDwv8LEOTr1JPE8SuyTc7G596F31zbNRoNBNG08OyQ6lhZtvYjHibqPGK2u3AF3-BfMds_WPprkcX-K05AlgIZQhQSCIiB_gnJwOseGBuMCtZCYMqUPGxI7bxp-bDvXqFwVRj45QMiJIP6F3_wpi1k4PvsmbYd3VthXSOHJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تکل جسورانه تیاگو پسر بزرگ لیونل مسی؛ این چند ماه که اینترنت نبود احساس میکنم از همه چی عقب افتادیم تیاگو کی اینقدر بزرگ شد، آخرین باری که ازش ویدیو دیدمش دقیقا نصف الانش بود
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22705" target="_blank">📅 13:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22704">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UqwfdHqLTWevTDFY0ORj38cAf1bjJZkSVNwXYh8hIJk33fUdPISQqHKSk3PAVcZyurucLLbtjgFbjNWG-YfDO8pmNQBlajf6q4PJ9x5SsqOUPSUgoO9H24FqHAaaKRR3N9_YYOJJlfhK_Ob-eNYWo_x6bSzqnmSEoJxdWcphePmTGcGjWA3PEGay2sVl1gcox-JIsGlXwN3eu4V7AG6IlrrH7Cbp3ybP9IjMCcjMReT5pJ4LFlrKg5Vwy3C7HtChb_elMDOyRLiMmGsP9UprXV-PEYcy-BaD3MYwaZtP-Bftg91V3kfrHLgRvke4ebTzyZ2H9OJJC9aSGHxBlepswQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌انتقالات|رسانه اسکای اسپورت: ژائو نوس، انزوفرناندز، یوشکو گواردیول، ابراهیم کوناته و باستونی‌فوق‌ستاره‌هایی هستندکه‌علاقمند به عقد قرارداد و پیوستن به باشگاه رئال‌ مادرید هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22704" target="_blank">📅 12:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22703">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9GYt-4ovKcPBabDL2EuUhdKDbfdBJD9zGUJbOxkAQ1oOW8pdlV1AttpXrNjhp6_hSNWTRE-19YaL8NIwlwYcnHyfk0_7TcC-XI3j_OpL4kbjelG2j9yTMFozJI4uvvamBFxDhPDgwR28TelEMaROaaSPBZIMy3ed8ZzHqbTQ9vntEGzw2x5EhS9NtjGdaR-NLjNfQVlj9nAIiKd82TKZHbyxi-sbQGgmt6AnQapCit5pU_lRtbyIujiOaK8cq3UycCT4DZX2bm1PPvofIle4g_jS95YP6OCnKCpKOrwburR5q8IJvOCSbCpBHz_hry8THMp060rk2SYi_sxY5wHdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ طبق آخرین اخباردریافتی‌پرشیانا؛علی‌تاجرنیا رئیس هیات مدیره استقلال تماس های اولیه خود را با دراگان اسکوچیچ و نماینده رسمی او برای عقد قرار داد سه ساله با آبی پوشان پایتخت بعد از جام جهانی 2026 آغاز کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22703" target="_blank">📅 12:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22702">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZDKLdh17AxLLLBS1p8sFp38DUZxxfBQzAScuNHgW8EtdhQ3QzQpMUqvN19arU-1GGZ7UQpJd7is8lRu78IlH70rk5lIrEDhguqAXdIMVcIopiDzGyZpKOfkjYXqDpjAwOcpi0jpLXgJ2mmdCwYXoUItV7NQ9zthEZauYWcbzXXiUlSJ-e9RFJA3xPpHloWs59lq2ADiQrUFcOxV1LTnZwrxEoHi2ryzE-UzFKsAjXnzyk_plgCVjJx2zXGpzh4HgetGDCE6xYzqVCadQULsiKJ6FQ6gIxg_IzjZfl01gDWb98Kt2KirC0sZL-GUAqPnPBVQq4xfoep6X9FnlyJuxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
هری‌کین‌درباره‌تصاحب دوباره کفش‌طلا: ‏«این یک افتخار است، به ویژه که فکر می‌کنم فقط رونالدو و مسی بیش از دو بار این جایزه را برده‌اند.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22702" target="_blank">📅 12:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22701">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHPuxkJiv-BFfxzh2F7lfd_DNb64rW2YvWX5FRccTBkewIrK9R_5przvdhkRuKU4hE-bV5gxg60v8ZI9OH1fxO8Fr7YKdUA643iX1arb0kFggBoWYbk-PW2NmdcykJ7DTIYIwReaOUk7YJ-wathRL11LEIkPK1r39gLpj7pi2xKDPz1BU3mLOGzhv1qUan-UZLBgH0zgH_9wN4tnjrfMECcgdGhPimGLrLTmtskIrr3zGKEz20UVMmPMAvCFYFzLM2F8c5XGpu2C9YkkQjKfZEhzVeEJH66d8_ORXCiC4mPpQFQkLk5wh9OLOQqdbG4_DJ-PYswYWmeR_Nj3_mWQcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
۳۲ باشگاه با بیشترین بازیکن دعوت‌شده به جام جهانی؛ بایرن‌مونیخ با ۱۶ بازیکن‌درصدر این فهرست قرار دارد. تیم های پاریسن‌ژرمن، آرسنال و منچستر سیتی نیز با پانزده نماینده در تعقیب صدر هستند.
‼️
نکته‌جالب‌این فهرست، حضور دو باشگاه ایرانیه:
🔵
استقلال با 8 بازیکن
🔴
پرسپولیس با 6 بازیکن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22701" target="_blank">📅 11:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22700">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c4ff2b5a8.mp4?token=TNk_H4aiLKZJDDQr1svWVWmSySvwLzf4sol9HCQ49vVdczvstfUbrbFBmB-6TJxOnEXKtPQUYswybaNQk9Tm4CYYXyerttwZdVkpKtLENHrCIIgyZEimjlYHvMOF_nqjQh4n8PcdrcgaZpX8j7_0109xW7QhpUlBud056U7RkMToXo3H2Tnv9519fFZXOMj8h2USKuiTl2pknV6UQsyY8D0_lWLxDbehzdOZrBLEAs9sTPILfqNPywAUgRnP7jGpeKpeRteS86YVzEu4kESW8aYuWdX3krnGbZWEbpOLOiMQIUOXocS3z9I0BOpy8G1pzeXKXWY_WSwoCzosxQZ9xAgijh1HCQHYrwSBv1kNY17u_JagPL4NitOtOiA3KdH3qwpNGrgQW8M8RLOEH7hUgR8GE-6dhvL9uREmaCJKn7qp6jjsMl01O-2zcbVIqFxL1frJr0LGWobc8I4ckANWtEqI9HogZ5GSz8mLBdKp0AZE_G2RuquXycHCuyodLnytYv6yGLafxHReLymmsm3Z2SmViaWUb4-uQOShqFABmClkUa9TwnIhyNdF6fqViSGK1jjBaTEXHKym39XeLHSIGMP7kPsMyR4Cp8y0pOI9fJvhAmNytKKm9iAnf230ZUeJR_2cu0LDNThy0z7MgCk0ewTXzrHDHc_iIwjUwF5GpNM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c4ff2b5a8.mp4?token=TNk_H4aiLKZJDDQr1svWVWmSySvwLzf4sol9HCQ49vVdczvstfUbrbFBmB-6TJxOnEXKtPQUYswybaNQk9Tm4CYYXyerttwZdVkpKtLENHrCIIgyZEimjlYHvMOF_nqjQh4n8PcdrcgaZpX8j7_0109xW7QhpUlBud056U7RkMToXo3H2Tnv9519fFZXOMj8h2USKuiTl2pknV6UQsyY8D0_lWLxDbehzdOZrBLEAs9sTPILfqNPywAUgRnP7jGpeKpeRteS86YVzEu4kESW8aYuWdX3krnGbZWEbpOLOiMQIUOXocS3z9I0BOpy8G1pzeXKXWY_WSwoCzosxQZ9xAgijh1HCQHYrwSBv1kNY17u_JagPL4NitOtOiA3KdH3qwpNGrgQW8M8RLOEH7hUgR8GE-6dhvL9uREmaCJKn7qp6jjsMl01O-2zcbVIqFxL1frJr0LGWobc8I4ckANWtEqI9HogZ5GSz8mLBdKp0AZE_G2RuquXycHCuyodLnytYv6yGLafxHReLymmsm3Z2SmViaWUb4-uQOShqFABmClkUa9TwnIhyNdF6fqViSGK1jjBaTEXHKym39XeLHSIGMP7kPsMyR4Cp8y0pOI9fJvhAmNytKKm9iAnf230ZUeJR_2cu0LDNThy0z7MgCk0ewTXzrHDHc_iIwjUwF5GpNM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
استفاده عجیب از گاز اشک‌آور توسط ماموران در بازی این هفته دو تیم بندرعامری و شهرآرکا البرز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22700" target="_blank">📅 11:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22698">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYowLgYiXu44AoyMNaQRro9Oa1otbGvOgXG5XT2FYx79mDE77S6nJJdlt_T4D_7674sYoEEbXTOw1j1QLc7V6DYOn6m7TBtN18xbR08fGk-cu23zFYdz7lJD66e_mO99S2L84P5R2vqgQM0iFS_QRuOwtjl-uYVR_ALc1p__4aaQpjHzV1WtcPidvf1x5SAUZ503d-pA08M18XDLPeHIFweuXQ_Qb2nWAjwON8_5wH6x16uyJIjglVmlxIlaaKHsA9Vr5JBM9n81MSTQwVRARZ96w1QgGReeZO-QT3g1fzYJi1x3TEyAZWWluoNG_61DO7kUJcw5udLWu-xx-RELfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ دانیال ایری مدافع 22 ساله ملوان اصلی‌ترین گزینه اوسمار ویرا سرمربی پرسپولیس برای جانشینی مرتضی پورعلی گنجی مدافع 34 ساله سرخپوشان در تابستونه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22698" target="_blank">📅 11:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22697">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">خلاصه بازی سوئد VS انگلیس؛ بازی‌‌ای که زلاتان یه سوپر پوکر کرد و اون گل مشهورش هم پوشکاش برد
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22697" target="_blank">📅 10:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22696">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ct5DhQ5rPb2Gm9tTq0jp4d5QN3xCaNVkd6MIhTIpPQZaGDFI3Jl7rlJBSTmgmZO4Ico6MAn0FI7mh3QIOYkJCcIRy7O0SzyUcNtFudsDmVr5HXIleTccDgsXEibCbJ30HhYuKEDwNVPDcVWCfON-N1WZks58WR0Jd6hcYF7WYlR0CEJYjinvX9OO7_Up02AIgPI4U9kBQG-twDkg3cd3KVPCu6ZOPasS4ebYCJNR08F63zvcQXtOsiZeFZFCv8VaYOJwJvAIaPQMBYxC5XqXsGWNmQhMjNbTnALjUlRsip6olOwIpKznYGSF8VM4kgugDQ-md5O_Ck21iDPFam0Cog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسکالونی سرمربی آرژانتین:
مدعی اصلی جام؟ بنظرم تیم ملی اسپانیا قهرمان رقابت‌ها میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22696" target="_blank">📅 09:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22694">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jdg95EFbXT6fTvjkqhWu2Np9gHlAsKbEE0PyeEFC8RWzZ7Yw0XOKr7I4-yfiMJE6Ztu97EmixOLGfnY6H2yaOfnfD2EkVpmQ0xndgNPpr9_IVYRUa_KxbOpgsjYj2zpfjgIqg3Yt4BYZgMPAEjtpSmPNPl8Bjkok37tMhh6sQvz1VjL1aFZlHEuNesur1mIxrvYzl4d7x0HX2kfUGSa9z-FazTAyhjL_w_QkUbY8j3uuqXxTFTLnUrB-C4J5IoidC2LnbdKBjJUrrbrwo-nbnbMDJ-K73eTHfCjLy2YetFvs8T3rq-np5jT-HHC-46yw3STBZt-hUoR3nyNw0C2dxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اینفلوئنسر برزیلی کارولای شاوس لباسی رو که قراره درجام‌جهانی ۲۰۲۶ بپوشه به نمایش گذاشت؛ اون با پوشاندن بدن‌خود باصدها برچسب از بازیکنان فوتبال این لباس رو طراحی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/22694" target="_blank">📅 01:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22693">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTT-vZDLEWUaZj8M21f6kokiZ9PXyX00Ucb26jaYe1xA4vZXpaD1Utf29WQoh80Pn9p3r1W0NlJ3JI4V8eY_xCkaqaTe1Ly2GJBJhMJYxXUJBKUyTmNupEEWiHDdvc7x_8Fj7g7apWThWCR8bh2Xmdzv816RTpZke6kOveFp6Ua5DRUqZ9FMjEbbkTdCpVz1S77dx8_zbosZhw4HbWzcHNe7meheQTA19N4GEV7GQWP-ogCx2jjUrDcJRpUBHvN19mC_G4LS_XJ1hW6ry57KQQwjB92vtX9Keb8qS-SkDQtd-x6-LDhnxaJwZ-9cYb4nNi6NZlimt3ysRyuiqlbihA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدار های‌ امروز؛
از تقابل یاران نازون و کریس وود تاجدال دوستانه هلندی‌ها مقابل الجزایر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22693" target="_blank">📅 01:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22692">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HF8o6X3weqeMhJR5D6hwQDLrlsXfVvTPFvexZE-dOLvj62eLTeTKJGW8PRh2zR4t8_C13l_98TLb-Eap5Y4E-VPtYf8hAqzDAfxxc7YrybQeIHSFRUCAJWT05um-kCma_1B0PRRnBoUP23t_Jmx-AuME9xsBX89a_naqfOKdZarWJuJ7r-CvdihfY8pwy9hmhY_cv4hNq_IbSJ7fKvqssK-kDgvCipuX2RHqLOO5V9gCAFNzmokpRNltUl-lQVKz6JmGQF1a0YUOfWsSVjI8pfi7iLwJf9oYPqYo7Z6Fc6hnlt-PoDBhNnX3zeWkQ-DNU3vpYtnOsmk6nDRl-2QnWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نتایج‌‌دیدارهای‌دیروز؛
شکست‌شاگردان کاناوارو برابر کانادا و برتری بلژیکی‌ها در جدال با کرواسی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22692" target="_blank">📅 01:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22691">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vm_CQPB78ObtnIPAt3K8LvCQwJQ899cZ61d5uWXpav92QnEBt25flDF0IRU61JjOHdoveaXRDkWgk8tkNGIa-dAcs_Nzws06WwPzql6QuMvX4ak0-49pSCSFgytNv8oE5jakq4jXQJVUT8Sesb921kCX490ZLEPATzPvrux8LA0ll_QuJZ_nE-glV-z-4RyyoaDObfUfGN0z75c52VRSbG-NLRIR0dWpGHSka6HukVdIyjoYKsC1scGvQ02Fq8LefWNsn2qsInA1xvDXqeGiv70kjV9dKG0qcjiIbAUSoHBx00U_69WAC9s7-7SVR3p0e7c3MpRZdUPzTIp6ZrViTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|ادرسون‌سیلوا هافبک 26 ساله برزیلی آتالانتا در آستانه عقد قرار داد چهار ساله با منچستر یونایتد برای جانشینی کاسمیرو قرار دارد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/22691" target="_blank">📅 00:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22690">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIn3o4UU-bk85CSa15vZULEjHtg9DRuFMnTnwUhspS_8gl_5UcWT8yJmnUdknX7nveLvLr6fGPA2gaolfPvMKd-EvaBz9hdvdJWjA0gUCbYbKesP2l_uw1M_MZ3N29xOGGmf0ByYWnbueryBioKbK7_9ICHmAw-9dCL196tMgCxds6yDNReOB0BOlLfJZpGW3OBxYnT535oy_XcnylEUIxdNhOGpGpmpAGdxn40JagW8q4AWRM3L6zrjbSp0O7inp-lvwWk_UEoNDwN0VGYxZtskPPE6nTGpvl4bl9_d35pkVYgy_S8PZz-P-94my5CsmSJLbdu-XgzlTriCamnbpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22690" target="_blank">📅 00:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22689">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a506ed7ce.mp4?token=cVKv1U8Z_sUO3ZSZyVmSLrvUSeZ7clFVFUQs87i_zk9aBH1eL8-2uxsoYYHky0x9cuzb0ZMC1FZLsyAzQsz1AAdMz2ZjWC_zG9uJYiSz_XKgqdAm_A7BJqJ20AJ98sm59zXZTOXyS1o71N3EW664kxm7XgxtpihDuz2XpoOXh3t2nT84a4J6vOvGdaayZVDi6hMqttQ7c4A8mc2k9htsyalxY0MOggf3hvYGCjLhJzwJGFD_6uxFjgQFrCgGP8Yt6enUJE6GrzdPtwOTi_3_7S_kiVE5T_aA_BWYjJmcz13qvQYlXhS8eNVP49uVPZizNW6sDbvBo2F4MAjVtU8t3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a506ed7ce.mp4?token=cVKv1U8Z_sUO3ZSZyVmSLrvUSeZ7clFVFUQs87i_zk9aBH1eL8-2uxsoYYHky0x9cuzb0ZMC1FZLsyAzQsz1AAdMz2ZjWC_zG9uJYiSz_XKgqdAm_A7BJqJ20AJ98sm59zXZTOXyS1o71N3EW664kxm7XgxtpihDuz2XpoOXh3t2nT84a4J6vOvGdaayZVDi6hMqttQ7c4A8mc2k9htsyalxY0MOggf3hvYGCjLhJzwJGFD_6uxFjgQFrCgGP8Yt6enUJE6GrzdPtwOTi_3_7S_kiVE5T_aA_BWYjJmcz13qvQYlXhS8eNVP49uVPZizNW6sDbvBo2F4MAjVtU8t3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحنه عجیب از خوش و بش آنجلوتی و اعضای برزیل؛ آخه چه‌وقت دست زدن به اونجا بود.
😒
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22689" target="_blank">📅 23:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22688">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OeCOF3BHrtgcbZKYDAbVLENBXQuR51xiYMoTVUjbxSIOV8_r9F30DthfbmSGcAnj84NKv4QXTmyczRIBHWiDO-ErQ8oiKvuGLJ1vYDpJd0Et-FUPCCPl_jUROyRSSVXbhBSUuurow6E533bt84D3eMQ4iY1sFrzIajPd8SMLNZoZbTFkj88ThcFl2j0HPoPqcsoTeGrKkSPi4VR8o_N8yEHmG1pJ-pmU01TGPS54bUocYqfrl0RNxEFG-UmgipjLrhA3Srw7WdO7mrMC6Wdx0iRZnyqcjHXRDBBmOM2x4FZ8MwA72bQULCgk-oZWh6N6WpA_OXWm53REqjx3zA6MCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
رسانه‌های عربستانی:
باشگاه النصر بدرخواست کریس رونالدو پیشنهادی سالانه 85 میلیون یورو به برونو فرناندز کاپیتان منچستر یونایتد داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22688" target="_blank">📅 23:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22687">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXziArTwqPAddJ3yay6-WIEyHXhadetpDHYWNm70WOgJoAfun3naTI8DQT94mSLmKFHMzjWW6B0rbSNNTZlhBZNugf40ntvnhX98TWyiP8ObrENP9ZlxFrDZa9eirfDUXWVFfrLkPDCwLYn7tGQyz9E-53rg4VvnMGs5Zm_j-8b6JtZ7GFhwy-zk7C1M8cvYXxg1P7wpZfqVAfimRRpS7IqNmzN-kcLbZxe-inv1DdaSh7e2HSACMD4-_0pjyDnKdmiEKyz_Dt9Zpbck5KL4TA1wMoDvNXqfFaWx1PgaoBe0r36EVP72hTZ9Tn5kElJi7sKfQfOIfTa8S5w1saYWhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌ملی‌بلژیک‌درفاصله 19 روز تابازی با شاگردان قلعه نویی، با نتیجه 2-0 کرواسی رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22687" target="_blank">📅 22:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22686">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skHrIJZ-A9f03dcoyhA_P6VgTp1b-VUH2Lh4BURrXBYEvlvFUOwuSh8FMK_QCLAgX09CZOnTUnEQopzjavWnjrEZdgkzur1FOtf6MLP-uaZJYaHJD9vgS_WmpbjlXcDGT2ukZeI1JhZNsokjyQlliwu__LZiznkHMLeItjCave_93nMcJFvSD--HdyYJrCosO_po-WSb78rrlNwnoRb43QQVbhKIK0PE26iiBxK6TQZhtT41AQi3WtBz-yfNv6abwMrCYrVfxewNjyBGARLJl6lnbiYSUahtEJ2n-58y_bhbKl8sXlDMNWki0d8STjjLaO_8v_bfxq0v2YwSvvvbog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#فوری؛ بااعلام‌رومانو؛ باشگاه PSG بزودی قرار داد لوئیز انریکه رو بلند مدت همون دائم العمر تمدید خواهدکرد. حالاخداروشکرکریک با یونایتد جا افتاده ولی بنظرم تنهامربی که میتونست یونایتد رو بدوران خوب خودش برگردونده همین آقای انریکه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/22686" target="_blank">📅 21:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22684">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5291786993.mp4?token=B0ZHbjfoxLC7R0OrRY6jocPj3SlF0D99n1BudIubE-twNJfIov-zw0ck5mJWENU_t-44nJ4_6sFTKFBfE2awJmb4PHQ-NFmf_SsgU9VZXuJLxqotfdwyD0GJu7t6B6qLBHUNzztrEsC8L1Eg530zq70FPaG2ZdbE-Olpj5IfZoLhyKgIJsEToiNH_dIbTpqeezPM-xG_0oD0ZzxcfAqOvgu53nSZNiGDXH-tXBrY4KQPP-XmYZaTOIHMcl7PGJlJg3ea4HgxNxludw_cXnev_o8hm9ug1qqkQe4ewsB1QpbDxIgr9hIaOsv3sGp2g6iMPIR7JuOcCjLHw8xH7Fm6wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5291786993.mp4?token=B0ZHbjfoxLC7R0OrRY6jocPj3SlF0D99n1BudIubE-twNJfIov-zw0ck5mJWENU_t-44nJ4_6sFTKFBfE2awJmb4PHQ-NFmf_SsgU9VZXuJLxqotfdwyD0GJu7t6B6qLBHUNzztrEsC8L1Eg530zq70FPaG2ZdbE-Olpj5IfZoLhyKgIJsEToiNH_dIbTpqeezPM-xG_0oD0ZzxcfAqOvgu53nSZNiGDXH-tXBrY4KQPP-XmYZaTOIHMcl7PGJlJg3ea4HgxNxludw_cXnev_o8hm9ug1qqkQe4ewsB1QpbDxIgr9hIaOsv3sGp2g6iMPIR7JuOcCjLHw8xH7Fm6wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بدل‌های ایرانی لئو مسی و رونالدو پیش‌از WC
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22684" target="_blank">📅 21:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22683">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgI0F8NpRlFgwUlfY9t9eNPLdMsfofITleEjzf5lSzd7nAzfZPLafku9s39Haix-0KqpbBgu1eyg2OeFCBmWxys7Ak-67wPayH0Sel431XWhGXsH8QfkWSj_RfdsW5Q1InAwDQ7NWuojDcBvQ79lZuL3r3311KjGR3GPDvzIha_Kdb9JplbnK-1qO8GC-i1Gs9t0xzgfyR2R2oJB4ZqyT5cf1EuDvV_08sRGKnaWYrBXGEkUuhR1bT28dk10WfN6JbHhBcG1RbPiPBoJqwt5Blqy0QTvBbPZJWNwbTXds-UYJx3Xuu2i8dMceA7AVZPTK571oTzf2lt4Xrv5h8uexQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
فلش بک بزنیم به سال ۲۰۲۰ و شاهکار پدری درسن ۱۸ سالگی که تونست طی یک فصل ۷۳ بازی رسمی رو بازی کنه و قیافش به این شکل دربیاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22683" target="_blank">📅 20:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22682">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/739be8e1c9.mp4?token=cF5ONDjMy2aGxgq9ZchdEg0KBg41nMm5S3w84ShB1X-WcfwKDnzzXKKOwMyL0FkbXpwv3Cw4_fNq5oVuIZF8lTO9KtHkFjD0oaGDDo_KKZ1QEdNoMHiJzy0qBFiJbtPXdp76xThnlcajGpTLTVsEfN2YN7zGss-r9sFOdz-3iFvmfIfDDOFjMohhgmlepiJFNwm6DsmRRg2xKAvWuOACzR6doU8FFkLm_E9q3HgNkDT6mzD6iOnM8N0HnN5zXWVaVQlnXi7EzzCF_GzHpbRCK0vTMT2Ryp77j6BRiTz2TmIhIJGDH89FxJxFGqWNlO_SoeT6jVeomnI8bABR1VdHng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/739be8e1c9.mp4?token=cF5ONDjMy2aGxgq9ZchdEg0KBg41nMm5S3w84ShB1X-WcfwKDnzzXKKOwMyL0FkbXpwv3Cw4_fNq5oVuIZF8lTO9KtHkFjD0oaGDDo_KKZ1QEdNoMHiJzy0qBFiJbtPXdp76xThnlcajGpTLTVsEfN2YN7zGss-r9sFOdz-3iFvmfIfDDOFjMohhgmlepiJFNwm6DsmRRg2xKAvWuOACzR6doU8FFkLm_E9q3HgNkDT6mzD6iOnM8N0HnN5zXWVaVQlnXi7EzzCF_GzHpbRCK0vTMT2Ryp77j6BRiTz2TmIhIJGDH89FxJxFGqWNlO_SoeT6jVeomnI8bABR1VdHng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شادی‌جنجالی درلیگ آزادگان؛ سلمان بحرانی پس از گلزنی مقابل تیم نود ارومیه، در شادی جنجالی و بچگونه گل خود حرکت گلر حریف را تقلید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22682" target="_blank">📅 20:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22681">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCovSQSmODUddIUdRXNJaMwm4es34yD3VtwfQDh1yF_NETwAvhCfEvAZlz0c21nG85Wl7NIwOHnNPZvhDvFZ_2B7OZm7Ivgt9FP7VWWOa9ws3dOI1Ap0eer4qxM4dlykITRp5Rd9ODG0FmKN-HCU8GSAdXO1ZQz9VILpat1Cw8KI_Flyklguq_OLq0a67YQD9jhqupL7g7wm14UJBUEr1VtK-n8wCPFzTGeAZJiLYq1mf5Di2Nl27uBybihfm_pHBnRwC-3H4oXOaaAJR3rt3J8K97tovEqrScatlhKGMnTRhedQ9JPnX7F5HzPJmQddjr-GJp6FDF1lpv12LOP2HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریستیانو رونالدو 25 درصداز سهام باشگاه آلمریااسپانیا رو رسماخریداری‌کرد؛ 7 فوق ستاره‌ ای که سهام باشگاه‌های اروپایی رو خریده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22681" target="_blank">📅 19:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22680">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5549cd5855.mp4?token=FRvnm3kub0w796W-CoL9BVW1gcL9eJYQEIN9vb4IuF0D_TKztaKWyvt8mm1MRDpFArLb4Sbc5xGOPQSwMAJHO34350rGrytyTpU3Tr6c0bZ8qJh99brXxf4_R_UfVHtXfADJRkbHaLCL04JShIfLqiuD3xgnuT_ad79HIuasB0LAJkQYfDFuZLtfPLr9jB6OIN1V9_BmbOYIbhMlO2XVcVOq9DjZn3htLVN7OmljiiMXoOvVOb27fC3ABdw6SUukNXIlLN-SQ6WxjzF5Y6SFFXFTfcLoKjGGg_ss0SjvIwsD4UbQb3FZamQPBmrQVA-ptYnUCKJix8EYmT7tu9rsDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5549cd5855.mp4?token=FRvnm3kub0w796W-CoL9BVW1gcL9eJYQEIN9vb4IuF0D_TKztaKWyvt8mm1MRDpFArLb4Sbc5xGOPQSwMAJHO34350rGrytyTpU3Tr6c0bZ8qJh99brXxf4_R_UfVHtXfADJRkbHaLCL04JShIfLqiuD3xgnuT_ad79HIuasB0LAJkQYfDFuZLtfPLr9jB6OIN1V9_BmbOYIbhMlO2XVcVOq9DjZn3htLVN7OmljiiMXoOvVOb27fC3ABdw6SUukNXIlLN-SQ6WxjzF5Y6SFFXFTfcLoKjGGg_ss0SjvIwsD4UbQb3FZamQPBmrQVA-ptYnUCKJix8EYmT7tu9rsDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این پست برای رفقایی که تمرین بدنسازی انجام میدهند. بهترین‌میان وعده‌های‌قبل و بعد تمرین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22680" target="_blank">📅 19:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22679">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_V7VlwXcthY2aY9uI7X66EceiIQLsrGEmUOaZTQpZB4q1g4dgLDz_xfH9lTL7GPpmUw_Ciu9T6pKRml_1qolHeG-9e7sN-Xnt-e7oGbIvW0cS2h3djIkUPqsSxflcnckQrtXCEA44tXKy5vXvFUzR5L8yj-JRfv_92ULN1Qq6Q8ghnJ-K4cakJmIsFf3MZu3fai24Cgyi92UxUx2NGmYj7xiDfTKGs5D4DlSbuQupQSba5SmhVLpcrvyXZSjJKyK9NSoXfsVWcVYff2u48UU_KU-ZE21iUwaDmjxCvG_w462P4K7KQLF0B1nPIjgjKjGtZAvSBcOqUugYS16EHM_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ تمام‌رسانه‌های‌معتبر بجز رومانو میگن که بعد از ابراهیم‌کوناته؛ خریدبعدی کهکشانی‌ها برای پست دفاع دنزل دامفریس مدافع راست اینترمیلانه. ممکنه بزودی خود رومانو هم هیر وی گو کار کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22679" target="_blank">📅 19:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22678">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XW8C5tERbZhoMtVh17-KKVb4LRfQk04Kc1WLqjXapbHaVM_sAAuJDuhzOya7TUAhojckEH9gk5MbwzpX43wTW0dI9LyLVzGCIL9z-xW2LcPwFuiqLTCv_m18HZ5q2JZlLq70Tr-C-YoF_l37C6cBZ6IGLeN5vpqhoawCBncWKpm1X5C2Zpu6E3tFeYEuWllex_QikIZ4MUMjdYRkgVrR43KDayeVZjdAfP1ATIAsXTh97vHNrh9VnZTyeHqsApXGYDXQ-eY-nnRmpXRwmvndqI_-czB09hggANDHkyl5bc5uq0tyTsdlsfh0cU1y9V32DlKBju-mhR3gD-dU5gyeIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزیکه لوئیز فیگو پرتغالی به ورزشگاه نیوکمپ برگشت اما این بار با پیراهن باشگاه رئال مادرید که هواداران بارسا به این شکل از او استقبال کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22678" target="_blank">📅 19:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22677">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbeLU7t-0kaDSY-l5I5U6QtowFLlbWvJHQoNOrhBsduMM02jUcIb73SvY3qj_8i2g6cqmmPcNwGJzYYLfrlqc2D8I5tLTpFLEI-21QNONgWizZUqED3QyEjahUS0LQ-EZpUCmgfl71FxxNJ2nfcg8f05O1q4i4d9Jya87Jg26gmgvqwzAsAVgCuh3XVEDv_daFkX0YJvg9t0O5hEu0tjzwQuG4g5chydD14J9SEj8o0DecSVLfS6CrlcsaPgdMmRHTwtucb8NIcl-BigPOEgNGfoV-4bb_0RctUf3t7SpXNEYNqA6JU3bR0a9HFRCQi1hKfnOlJrt9PIwlpyv4supQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمارفوق‌العاده ویکتور اوسیمن ستاره 26 ساله تیم‌ملی نیجریه که درتلاشه در ژانویه و یا تابستون سال بعد راهی تیم بارسا شه. امشب هم عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22677" target="_blank">📅 18:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22676">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqfiLSwWlyF3xmLFdND9Rc7bzkd1NAOKIXeGVqVnmGqz70k5gDp04qelX9zSA5MXBaXHi80t2QHfxr9zaU1jBrH1vEVzOgTqvAqbCHKC30uBgwph-oAOqD9WKXGXOlamwXqav7u4ZWlFLPbfxnfegfXEMI0219l0DROefe4SsvbfEe5tAsaSIZZh_FN5OPebDQLbxpVnGxbqPJQjagsUH1w95NrrseAS9eNYKxf48VgvuOCtmU4ofW5SLXdYgYh1x9AEb0yr2Qu044ilZT7r5uCUhCgzq-u-wt0PEZSA9c1VuRTRNhPKTFfgGl3F4mCEXAlHUjv3zZSbDG6YYV0rgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بااعلام باشگاه فولادمبارکه سپاهان؛ انزو کریولی، مهاجم فرانسوی این تیم از باشگاه سپاهان جدا شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22676" target="_blank">📅 18:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22675">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64c124dc30.mp4?token=AoZVqOua4p_4vD3i7xCI_gh-juHHBtItA7Dl4fPYAD_NOu0XvNYWdeVRAS476khctSzalD8KD_RzGBQTn5zQRNK_6841rLdd6NQZJjbqUAU1jw9mqLMqxurJVbqgLnq7R2_9a3M_EeDegQCEKT9W-FGTfjgcApziYJuEhv5g9NhvGvYoZOiqs88_l31Ei1MyKPBuaXNMwj-YSZL7pWchQq2V6S__zQfp4fFjTu6hExiFfNYxiE1SMvrmRl2zVxNq5r2w3KpmQ6Js43uhRp666XJsYa_kHnSk3xewbcUiuxH9nkzosTP398jqumYSAOBMTFFVK0YBMnCHaqDQrNNLew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64c124dc30.mp4?token=AoZVqOua4p_4vD3i7xCI_gh-juHHBtItA7Dl4fPYAD_NOu0XvNYWdeVRAS476khctSzalD8KD_RzGBQTn5zQRNK_6841rLdd6NQZJjbqUAU1jw9mqLMqxurJVbqgLnq7R2_9a3M_EeDegQCEKT9W-FGTfjgcApziYJuEhv5g9NhvGvYoZOiqs88_l31Ei1MyKPBuaXNMwj-YSZL7pWchQq2V6S__zQfp4fFjTu6hExiFfNYxiE1SMvrmRl2zVxNq5r2w3KpmQ6Js43uhRp666XJsYa_kHnSk3xewbcUiuxH9nkzosTP398jqumYSAOBMTFFVK0YBMnCHaqDQrNNLew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی به ازای هر مهمون پنج میلیون دادی به تالار چشمت به‌پسرخاله‌ت میوفته که با لباس بارسا اومده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22675" target="_blank">📅 18:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22674">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZWk8pF-CpPQ0vsBzmqgYdI6MPQ4_XSIPZHih-fxNsj3NuBmjQi0xGggTdbWNqlo-PXTIBhmvrKcmA9fHVnZEGCTNcFGdy61IDcQa2m4GdUXTgiY3Go6WsuHj7WVtZQUIcd_vVVbZ0jzEdRS_B8Rfg5YPRSDc-h1_sclFy1-y3zpvnxh63Q-ai9oR8qBseovJsoTyFVuGMA7vzqWB2lyai1LktQXoLcuOjIZ5frSubD53026z-WKJ6wO_Su5LSc1KokTO2g9JzERQkzkvSiP3uM-k4x7KjQaujpPca5hg7XLJfO7JIK59oIoafAuQs2CMQSAY8BOFxXol748r_L6qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیم‌جونگ‌اون رهبر کره‌شمالی تو یه‌حرکت کاملاً منطقی اعلام کرده طبق قانون جدید خودکشی کردن  ممنوعه و هر کس خوکشی کنه زنده بمونه خودمون اعدام میکنیم. هیییچ تعارفی هم با کسی نداریم:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22674" target="_blank">📅 18:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22673">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XszLZtRARhy1f18YZ8wgkI4Y4KvubRoJ56gcVnfRy1eP3d4rKxr6zwG2omslYM8cvQ_2e32vH2JJdJJbHiv97Y4kh02OVl-jKtNsuHootuXVIOn7vmNbUrF1em_SPcH-unpubhPlXIF_mZwkyWDFRHxEO90PfuXQWv_eugNDdle_RFwmPdyO-LudFTQZpod7J6IupZlKMgM4DjMkkShO4sB33dTRvvbMUOie0rjT_be45P6Rv15z0k1YwmU_aZRs5PBT1j16-Am4INhXhbneb2E1WqVZWus_0e1L5uQcAMtL8zmeLC5Y4GEAt_KTJ0kfhZlFn9WFLvQCvvMvJszJag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لیست ارزش تیم‌های حاضر در جام جهانی؛ فرانسه با ارزش ترین و اردن کم ارزش‌ترین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22673" target="_blank">📅 18:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22671">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdcqSaGwp7VSFGnAk-evzgHdcLCpO6KYcTbifwUxZqScAhzW1V_KjX3zVRknqqJwbPddqr8XqhJZwr-8xmyQFa1z21VhUVuT3kXZ4EBZWzofFNgIDn-wxz7jFQPrJmJUE905V-Uy4WhOD-oli9F8hJPUdAtofNVWeCmQbpawhgqd5Q4FyCaEJOPIUF7idGpaq-vagHSKgS1A5doGf_4ZBfk4E9nHHbDV36g-iUZpf3K4YmFMVkFK0ppsFauTDDfQNZ7QJTH7ZF8R3Dc59y1N_MF4wWc3Ay9VPW_ZoMQdkUOH6g24dRODDFhT9u1lZdEzF7pOUk7lvFGwIUsJiu821w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
دیمارتزیو خبرنگار اسکای اسپورت: بعد از جدایی دنی‌کارواخال؛ سران رئال‌مادرید بشدت دنبال جذب دنزل دامفریس مدافع‌راست تیم اینترمیلانن و میخوان تو همین پنجره این بازیکن رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22671" target="_blank">📅 17:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22670">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2wS-WQE3TGDttdjegE2aDThVpBSaLg12M83cbYRxKxPdzWU6XjLWTEct5LPB_-n1IhR0cx_a6pI1HV2Sh5ibWzgGv462QMzjhQmOztpIm7G0FtGScAwd9qtg_tGaAe7Bt2dN-gNGiLSgukJ-oiajTczogyA-CQUYYnB2ZpdUeLFI6VarXHvcxAK71bUPPEY7V9iDzMNzj6vOl9LaNfKAJX0-G_5gzDdBHqSmwAn_JLON3TxI7isOKe1_rUOMJvi6XJOhujMN5Z70ZPdsg3C-nFG84Cyjyft3dalrkJh4UO6ffFyaQT1R4KxYQZv86Y_2GSoK4a8SX6wmJpO6Iw55g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ روزنامه آاس: ژوزه مورینیو سرمربی جدید رئال مادرید موافقت‌خود را با پیوستن ابراهیم کوناته به جمع کهکشانی ها اعلام کرده و به احتمال فراوان بزودی این انتقال بزرگ رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22670" target="_blank">📅 17:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22669">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQ_QHUFUBkAaNEniXFl07Z9SqcH4EXzwFLt09xWLjRZ2Ybadm6PITWp5Keub-tUr32zO0TlRS7MNCCQwGfPMxfSTB4gSyvTTBAoURzt5DZq3PGEnxPsQ6xhdotoycAoiJH_OyoPO_DTmNctONcClCa_7l2--1oIzwrQBR_f96CHO1q3YyPPA63jl8PXR9-yVWZ-Oni16NxIwut_Oj3fQd2pkesc-Pmv4HDsOVWwFsgdg0a4Ibdfn_WByYl8kDX2NNZDXsAWIxjWoQKAKYTdLBlzFeT9ZRACrRqJCC2GrXAP04XpKhHvb3F4H_NAQOG1g2AXHtaD_ImKrKVkc9jhwCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سلام و احوالپرسی‌رسمی بین‌بچه‌های کره شمالی وتیم ملی ژاپن، در مراسم پیش از شروع بازی مرحله یک هشتم نهایی جام جهانی زیر ۱۷ سال.
😳
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22669" target="_blank">📅 16:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22668">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcduG4nQWv1ad5afT3EG6HNfjDmxLUlC7taCqp4S1pUVz6tBnrlfOarshyTZRDNO6AfiVhzbLlsRDoqp-9STI6z_LSAqtlL1zlvLi5pebf2K6EsDWTnSUPvDtg1iaJB1zLpGY5hpaWYSBLe6w1xJOWoHPVPobEbormPsIQ-dkLDHTyFP5KhSuBTtFEsh5ZgtViSGs5yzl97lpLmCxVAlBaWodb93QXSV-rET6W3I1Arjig6TmJlndvTSHp5Y9rPmFCcdJhLwcqia2kNLtrvgd57urW8kdcXtClyCsGbU5YXNbnB0ruRKbdySBZ24ncdDnrUI7HgqA7mk17cB_2wcRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی؛ علی رغم تلاش علی تاجرنیا برای گرفتن مجوز رسمی فعالیت فرهاد مجیدی در لیگ برتر؛ اسطوره باشگاه استقلال به مدیریت این تیم‌اعلام‌کرده علاقه ای به بازگشت به ایران ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22668" target="_blank">📅 16:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22667">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_3gQX05WV5vhMHbsDxlPjMtM5dlOznp4hHzvNoxWCvEgRbYyf4voaTxXpF5Je8d1h_xJmC6cNrMQySHl61nZHBXzZ6O3HfwLJS09ggxR6wAJVVsHhz0o7-oByLMMBxmOFXnCwbElcXIa74sR2yrlRqU-EGPUL8YtUAXoZFlUoIeVgOGCcj5MdQLF0TS6uhQ4K_C5JZSPGOL3BzqYGYSaKIAd6_9McgMNmoBKijomTIk8hsnFBeLOPc-s6cl5ZtxRyKYeYzwpLml6uI7x3UIhHjrlPT_byWUmZ0EZvfnPpvOcZi4_FOdXCqBt_ggA7Zyrx_YYi4cm1ES2ozgId02KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇨🇲
دراقدامی‌عجیب؛ کادر فنی کامرون؛ وینسنت ابوباکار و آندره‌ اونانا دو بازیکن با تجربه کامرونی ها رو از لیست این تیم برای جام ملت‌های افریقا 2025 کنار گذاشت. ابوباکار و اونانا در این فصل در تیم‌های نفتچی و ترابزون اسپور عملکرد درخشانی داشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22667" target="_blank">📅 16:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22666">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4NPxuCOo8Gi49AEk6r3x2nDZgbv7OI-_1hz2xaq85N2N2_v6eoQx_w4MU9oVlYynm6rbDBjm8XIfnNStwFKaemx2ttKMUv-hozpl3S-tCJ3RXLNb8q1qnigb_g1ux5O-gtXiBDSSOAWEFfapbODK1x6F86-kWQWeHHRfDBcl-L80HtoXwPtNkbsKoeAuDbZADriJYwumLbcrJOj25n16DwdULun8pnPq7JR_xtxo2Hy_pxljGX41tAyZxJITuxM90-Ybx4KAOA77bYcMtZ6DmiRxvqST2DSbN_GKXz_Uzkemw4OjIUgt9jfnytASM39Gv_Q0R4xKfdcuisLjRJFgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|انزو فرناندز ستاره آرژانتینی باشگاه چلسی درپایان‌بازی امروز آبی‌ها با هواداران این تیم خداحافظی کرد و از جمع آبی ها جداشد. فرناندز از رئال مادرید و منچسترسیتی آفردریافت‌کرده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22666" target="_blank">📅 16:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22665">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Issbl04TfOQfwYZ8arGyDQ0WWEbPJTTkMUIGim7EjN8xN5wtVYspSENUTdicm9gO12NZ8YMB0fxKtgj4Zi1l2tD3M0WmA-3xsFnY7MId5r_ictCQLkI34T88zbn_RtkDHhdee-8DkvV-juoJ3c8Edq5oHDDQ9sjYYv2sjh33heimzDgNinGZGoqRQmevTAkXZnbyP5g9X7iOvEgLJdnbgz1YGtl5KtLW2QBIdW0sCNSM2gwvHjALLp-pvNFwrJPLxWwRYQbko14OpHaRA8tsGT7fc3zGK_bJxqMTxOvoYQeGWtico1DUlEe1Wh0JgxGLIvLfIX4nahYpFUoYI0-lxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا
#فوری
؛
سران کایسری اسپور درتماس‌بامدیربرنامه سید مجید حسینی اعلام اند قصد دارند این‌بازیکن رو در تابستان بفروشن. رقم تعیین شده برای فروش او 500 هزار دلار میباشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22665" target="_blank">📅 15:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22664">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roRqNRPyuzPvCa11o1puL-W4KnYhTPfWsSAcCeiIc7cfDMcVS5dHcrLEi7jSB7sY7MuRnAf4eqyypkTlBKEAZ3Ht34xkgWzViOTi4rda6DQ3vnBdSQHb0RyfG6yC2h_y_7wxDsqty7PSLCMMVIUDy4K8R-7JNeDnvaFTJnR4aIl4Mka4hjFC4UI6Oddl8dKmOW9SBXCQkn9f3c5cCc5SbHda2jTA0BZe_h9zuGiAbX-1vM4XqHOxn9esP-hDcZMNk-QEEYlNzX6VEdb7LkNBffj7m-cOwlVCEJ-B5kk9Co3qX9JTqNWKVkIZ3olJixOp5OWm_KxMxgwLi2gLd9jk9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
شبکه الچرینگیتو در خبری #فوری؛ ابراهیم کوناته مدافع 27 ساله فرانسوی سابق لییورپول برای عقد قرارداد 4 با باشگاه رئال مادرید با پرز به توافق کامل رسیده و بزودی قرارداد منعقد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22664" target="_blank">📅 15:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22663">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-ljBp66Ph8Edx-k27nBhP5h2fGwIsWG9Ux8WsHo2kivzw_mZz8sZjSH34Q4pSWKlqena_Mc22gcYQgv7PDTcyxqRKYg15paywPI6Vjyy73RBLR--3eGgrjYn4OJcPunuab4x_YpPfyYigP6o33WvsuinxvgjwJ_IrtVqyJMqmonjEnm2SFLg5jGdDvUxTEBhPhm0Os-BEObyIzD7E-E4dpsjgPVzRlHw2OEPcxLUfbi-Rq-io_Y7Rg7CxSRmdWABWRyXsUjmtOZ7o5Vb5-vsH14XViGdDPlA3jvpleoNq2orKBnEAjGTNxsOOCMFyJhJ7hBDTzfgTvNjTTka5piSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری
؛ باشگاه بارسلونا به‌ زودی با پرداخت رقمی بین 8 الی 15 میلیون‌یورو به الهلال عربستان؛ قرارداد ژائو کانسلو مدافع راست پرتغالی خود را از قرضی‌به‌قطعی تبدیل خواهد کرد و قراردادی جدید به مدت سه فصل با این بازیکن امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22663" target="_blank">📅 15:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22662">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNNwYR0DReN-8yCT7rYcG7bj7thP0XFhy5tdmJTRBhW0r_61AGTbzQKX1FtTRP6KflTCeeDybPbVtUjI0h0-RN_-q30fQ1ID2Pj7wH-YRNOkXtzmhf5XPCQF6rg0IqxhKQ4fvhIPoi-dD9-92gj6mA3gG_7I9569gUEiU1c4jPzDzWNSe-mbKisYd23Les3EVTaw7nhsuj7gJF6mOLa2iSp8p-iXkqp_-Fx2x_fC7UeOBsjmfFAxiFjiGLZxethJ7E7hMey7gKiY7g3HCPcYbnfSz_3URbaUGQFh53X3bvQ7jII5g8jfcnJI7J8DC__B6LK1nhwvsryQjTOmRMEFaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا
#فوری
؛طبق شنیده‌های رسانه پرشیانا؛ محمد جواد حسین نژاد ستاره ایرانی ماخاچ قلعه بزودی از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22662" target="_blank">📅 14:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22661">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqUQAer63Z1u0wOcFaW6BR0QTBMAEwbDWxnKnNGq_voY2-9cwplOp269sEA3ZmzqP0gFKZ_ymPavRpuVS9kf92oJG2STTYiURfrVHF2z_TbKB1D4BKwl446QMw3mHBR75yK_SJcyfuc2S3CHHEwBVDgaTa1nhlt9Bgo3UChSjaE9b-aFDfOAfR1jt31y3PINkFij-ToRWyn4ZLLSwKzZl7k3QZMLtzFqstdrdNoLbXnkk-EWA3_OBLyKZayG2n2sjeVv9HbWRTsLKCCJPM2I2RukSYyAw6uqnED5bXBhbV505XSpWHdkeTYu9aKcVIiIG9my2hkHb7aZQgBrtm2Svw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری؛ درحالی باشگاه پرسپولیس در تلاش بود که رضایت دو باشگاه گل گهر و چادرملو رو برای رفتن به آسیا جلب کنه اما دقایقی قبل زارعی رئیس کمیته صدور مجوز حرفه‌ای خبر داد: تیم پرسپولیس قطعا نماینده ایران در فصل آینده آسیا نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/22661" target="_blank">📅 14:00 · 12 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

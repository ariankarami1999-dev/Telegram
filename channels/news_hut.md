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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 19:49:56</div>
<hr>

<div class="tg-post" id="msg-67428">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDbMvRfgkISvMuZd03tzaAkrLA5Dlacc_A5GcI1WksB8aPUrkqbS3g-7UIXRuLgQevU4xNTX0M0PyCB6bAqQV5BvoByLaO_Or1ATnNuhggC0T5LYhIot4fiQ1QFLbccNbIlOoSn1IJ7rCOnxYihgfhrKRT2lce321N0VnhXJP_cLdlbhagDYiYyZil1QMW-lr-kSj9KgPLxdud-gww4XkBemRC6kUuCpj2vpsI7FXjLoadWLAV_SQ_Zpb6qxgw_oV0HBhpSPeyVazUA5dFCtIHwolCyXwOOns9XKaaPtOJlzoroScl9wHjTpCDA84iA566RMMb2S0WDX_a2tPMwqVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ان‌بی‌سی به نقل از یک مقام آمریکایی:
ایران شب گذشته با استفاده از دو موشک که مسافت کوتاهی را با سرعت بالا طی کردند، به دو کشتی حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/news_hut/67428" target="_blank">📅 19:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67426">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GqbLTE-BTczhtrIIoBKAZ2_6dQWaru8Tsu-6SGzJdeZw4_Uz4HbTFjLc_rJ1YQFm-1aDndtDWS-2IqEOxa0rnlZ8BcN1A_qMUYkhEFqgueeZmJI6CknGwWrvMAk9ir0EsID1y5PIn7VVDAaAMGF2z0OKS67AGCcxs7VQ73yvpbYV8Dwdmd6iD3Av5IKL9GjwRcEI6gQCXk1yn9JjDS0HO81JZIpeFPD8MeIeR44KoOZkJGD251RP47Xp3XvrqoVOmG52wdtjSgluENVQ6WuK3NBCGsHrHJAsHGkLM8s6Vs4E6B8eVDlmMkt8tb5jsc8IC7FXSqAziJD70RKaXmM5cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rpWhV9hOf7672TONyWDvUCiNIkb824s9mLLUx0KE9r_U_aq7vGRpO6cnjYwANQ8sd_MATEpmCouGorNMhSq6UjquIqyFfgLT9C7Q8op_FzACzrzUJ5wjjIiKEZUlGPF5-cbw-zwp3EVdI9Plmmbb-ct80nSuznQqSRshxot59n5Ul0NoZm1AtZ54Mg9a5VtYX2ajcQKBnxXGUMY9yJ_nt0bo9Z73VQp0Ap1P16FLnsjQngZqReXEqkixnwSubSyTv5_WA21XSA9eCFrvZg2xNiACsQj4cYVc-e9FG4TaLfmZB35HkKffV5JnDkKGY_TB15Bt3rejFTiWtitv16s5rg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
صدا و سیما این تصاویرو با زیرنویس جمعیت میلیونی مراسم تشییع منتشر کرد :
@News_Hut</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/news_hut/67426" target="_blank">📅 19:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67425">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/news_hut/67425" target="_blank">📅 18:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67424">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GOB3J9qdHkd1ZKazpc7lmXW5lY14nQdpWQEDNaorB9T9dizWADwADq_We5BzSqrs5VB08b7Hj00mRbaAsca1KCx2sM7N26IufXlvv5l-2xoqTmV8P7CrKCGEAn10_nGeKLPUarnGKzGEEJ1FyJmRBkst_Sak_LLqwKuGgjCRlls-CAAdcJ44gaFddj5pm05G-1Rj-RyF6tinivRUdzEG0CGRVFGe6J0RYCll-U0rvTz36LjAbjuaMqKK5PYJbg9xBVs1a0bFCxQyQk_MaHuVJ64idDZDLX6t1eOLi4Wrdi9rxQ3nAph3LGOkl4wKiqrkXEcNvtOlLvA9hqYX06JG1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سازمان عملیات تجارت دریایی بریتانیا: یک نفتکش روز سه‌شنبه ۱۶ تیرماه هنگام عبور از تنگهٔ هرمز با یک پرتابهٔ ناشناس هدف حمله قرار گرفت.
این نهاد اعلام کرد نفتکش بر اثر این حمله دچار «آسیب سازه‌ای» شده، اما هیچ تلفات جانی یا آلودگی زیست‌محیطی گزارش نشده است.این حادثه یک روز پس از حمله به دو نفتکش، یکی حامل نفت خام عربستان سعودی و دیگری حامل گاز طبیعی مایع قطر، رخ داده است
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/67424" target="_blank">📅 17:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67423">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/67423" target="_blank">📅 17:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67422">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/67422" target="_blank">📅 16:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67421">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/67421" target="_blank">📅 16:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67420">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLAXqWArnxmMdoLI8Fl8jf_6XaNbwcgmocPEEvBrDIBPt-0PypG0BDgPjr8i_ZEtys3myqXSeUHgAmKYyJNyT_DHJG-GAXJ17mswryhXtHxkDSGQlSFA-9mS7OZqy8iWCOIWhmVD2qPP_rBrlTwSzf1nMZ080sCkNWT51H6XYu0wLvg8P4d12CdtJe1jVoKvMEcfjYE8vSA6W6MgdMamE8hOfPhJfTk6h6UITD788vXgk5ws6OjZj0Z30xVChAP5iXDJ43TrTeqZR8HrIyA2ZJfAxzj6cz70_ILNbyz45J09yL09LKsZDHogvg75O48RmCDYIqkzck9GRThpXg9khA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خبرگزاری
CBS:
علیرضا فغانی قضاوت فینال جام جهانی 2026را بر عهده خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/67420" target="_blank">📅 15:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67419">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/67419" target="_blank">📅 14:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67418">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FufM9s0BnbhzEk_jQm9Q0Yl9GCV6tV1GCMCTG-VTMkGOfUR5RV8Ej4dF_9TfN9OYUuwvZJ3TxNH6hUZ8WQvriA-ma8hgvJtk25sYC1r9nepws5BkrvjKBKImA7pE7-6Sg-Xo7cUXCfjsskgAj5XFxceJ_X-cgvLJLseEbc0NsMuMfKtMBecyPWtzWae8tsjOavMAoWcnNYaddiII0BSH_hTi1SYb2KEJs_Zyb2Yzi3UrSud-NLwFmviw7bkFyxjj8sNTzWQFgK64r4jwC-m4WQHNNPyPRjqznIgHNg03Vw6K5ah9-mJiTPiHzAkwZCc5JWO7oF0UU_8khlOZ8FkNmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری رویترز به نقل از چهار منبع آگاه گزارش داد نفتکش حامل گاز طبیعی مایع «الرکیات» متعلق به قطر، هنگام عبور از بخش عمانی تنگه هرمز هدف قرار گرفت و آسیب جدی دید.
🔴
به گفته این منابع، این حادثه پس از گزارش‌هایی درباره شلیک موشک از سوی سپاه پاسداران به کشتی‌های تجاری در حال عبور از این آبراه رخ داده است.
🔴
بر اساس این گزارش، پس از اصابت به سمت چپ کشتی، موتورخانه آن دچار آتش‌سوزی شد و دود غلیظ امکان ارزیابی بیشتر خسارت را از خدمه گرفت، اما همه اعضای خدمه سالم هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/67418" target="_blank">📅 14:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67415">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/67415" target="_blank">📅 13:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67414">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67414" target="_blank">📅 12:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67413">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67413" target="_blank">📅 12:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67412">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIA5PEyeosPnqgWlH5qmCrtBek7hBza7JBiTAu4_GyrZwrBXTUaSKOfmJUiBeeHXBW6Mca9trsyQL4uSSHUEsI8bxSU2oEgIT6MVf1ceBJwmiXrds0844OfRqLH9ee67hGmUtsq9vIhJWPWEYHkYOls4ZAHD_u2iAptwaQFuQKSDlqtriyE3CskKEq92-ot68rQfbJnacXD7RUmrlCNntpNr92Wq4zeWrFXTT4VXa7cN6ah0byNsiTzW7WQR_0iYI6QfMVcDMlINUF6BocIm3x8oqhRtYhBoVHht6r1dwmI-gCV1G-Xpa6SgeMl-h21kt9O9jB7EdzCv6X-tiZPKUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس:
دو مقام آمریکایی به «اکسیوس» گفتند که ارتش ایران دوشنبه‌شب دست‌کم دو موشک به سمت کشتی‌های تجاری در حال عبور از تنگه هرمز شلیک کرده است و دو کشتی مورد اصابت قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67412" target="_blank">📅 11:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67411">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‼️
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
احتمالاً نباید این را فاش کنم، اما ما دو تا از بهترین نیروهایمان را برای محافظت از قاآنی در مراسم خاکسپاری فرستادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67411" target="_blank">📅 11:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67410">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67410" target="_blank">📅 10:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67409">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67409" target="_blank">📅 10:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67408">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67408" target="_blank">📅 09:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67407">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcgPScQ9Kw0-gIVNE0tm2LQs_1-3T2ZSsW5JvC3lBLcvPUTnyI8EY-8LJ1Mbtqaq7UuW-yl74brixxvknrqxvdUPSa3-VnsdsBmiiDMDiDZliSOaVPubSkt1ixBfOQnqqcm1GwlaA3BeIveiVZM0uiDoo8DP9hqT75sRoy8ruMLxw6WxDbhazdZTCcNT4WxndWpHwgT2omrsdWaBpu2jqdwDGwydKyNdgEOZuZjeDF14NHQvzALVgpPSMppdKfTwVMiWFeR_7bxP4RBQsLGq5aEq6-WfX5ORbY8YM3G3LDMzWeF9wEDp8pkCqsZc1E4kETav_AXGAB-8mpQZWULBxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
❌
مرکز عملیات تجاری دریایی بریتانیا:
یک نفتکش ساعتی پیش در فاصله ۸ مایل دریایی شرق «لیما» در عمان، در کریدور جنوبیِ تنگه هرمز، هدف حمله و مورد اصابت قرار گرفته است
بنا بر اعلام UKMTO، این حمله باعث آتش‌سوزی در سمت چپ کشتی (port side) شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67407" target="_blank">📅 09:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67406">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67406" target="_blank">📅 03:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67404">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cBtE8Oq7qdCNA_z8-N74SdgSUpYRZaWHJ9U89xZhuS2Qn-J8KLKKiF6sXB387TtRi9no_g-rLioy5yHRlgEWd3jeQPEDL0jgYW5CqF4sgP82OFkTPVRhM826m-KAZmbIRW2ZKoI2Tc-rcsy5CAkGehLi8aMiiRN5vSAg3dmKxwlHLzmcifLHoLIzslUVGMSmwBqV7QFJ-onD_tFvfUtyTl8b9N5ZVp6vaYuVX8dy9h-paasujLfrclUyzCpahmz2EwlHti9zntRha2ATLMACUcm414eiP_iyvwpd4lwNprss1Bwsc7Afh-EOE1kdxYz1_6-dh87x8fllmc75hkcfFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67404" target="_blank">📅 01:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67403">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iO2u3ezbkNjeOvLrQo6gnY-0cEqKmpadxxk12Ek8Nkh9-AT81bUv8Nw2dj7a9gRTkMTGNEOy6VCvirCI9VcHwGn7M2pMdHDKlOpiyYb7oxmANrNVWfsv_FatVu7gnBSwwjpR3lmvJWjiH-HEhzgpdE3SZSLZsNTAYgoFWo3UY3JcqIkhHNNELevMZInPVadfrzEEwF4QDXqWIVlMHtmgDpXel6VAFjlnYBrFJrvqmqtjfe5rx4cWuMCq6zOoeVdCLGjOOiEc3ENZQvvOZi6JLLUrqxVCqOWx45tro3iE_-coT8KCtwbJR5Fy3-WgxCGYFJtFcpJ8ULHHWYWgGeVu0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی 2026
| حذف کریستیانو رونالدو و یاران با شکست مقابل اسپانیا در دقایق پایانی
💔
🇵🇹
پرتغال 0-1 اسپانیا
🇪🇸
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67403" target="_blank">📅 00:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67402">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67402" target="_blank">📅 00:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67401">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/781360aa4f.mp4?token=LOo2kdRQKOrgpny9dD57CSCRQQKTbbsH8MmHL3ZPcJB4LsCPMP4R_35ZtDUCjNLtyMANb8z92vJgWmn3b5xKFKMBR5U6V32417R0jM7n8_zz8Euz9bI39TldPKA0zkoWGcVXGHMRF0HXIo2wvXHvLRkCqT-Elc22iw6dlp0QCiY9niOQuPdIBwBTkenKATcuD6-trn8I9Bvrw_rCcxwNos_D73rNweHYmTtUT_gQ8y8y59Zfn_5v64rPxLRPNYDi7OwThMX1_KWefRB0WtS2O9RbcZEzqH2VNwdO3Uu0YBC_ystisQagw3du7K5GG-XNQDukjXsinCx3CO8hz52FWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/781360aa4f.mp4?token=LOo2kdRQKOrgpny9dD57CSCRQQKTbbsH8MmHL3ZPcJB4LsCPMP4R_35ZtDUCjNLtyMANb8z92vJgWmn3b5xKFKMBR5U6V32417R0jM7n8_zz8Euz9bI39TldPKA0zkoWGcVXGHMRF0HXIo2wvXHvLRkCqT-Elc22iw6dlp0QCiY9niOQuPdIBwBTkenKATcuD6-trn8I9Bvrw_rCcxwNos_D73rNweHYmTtUT_gQ8y8y59Zfn_5v64rPxLRPNYDi7OwThMX1_KWefRB0WtS2O9RbcZEzqH2VNwdO3Uu0YBC_ystisQagw3du7K5GG-XNQDukjXsinCx3CO8hz52FWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعارها برعلیه پزشکیان
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67401" target="_blank">📅 00:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67400">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتلوبیون اسپرت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCOp5fq48bUooF9JIGJ3EngDVNXHIG8MoQpVixtI0QBMlq5qWhgiJ-fL-I2xiqJXLtVEzhiwsv6_ebSWmSqZTDyCb6HZ2Drs2ayx2PdBcPUAVWn0ghpnfrms0Wa88fSFlyJr71Tb_H67NgI5NgRxpf53LJLtSFkXaEoz38jSHen_x91HtLc1F22S0HH_4-xdrt9cDb3441DDFcA76BZ5PD21v3hLrUWcBeHHPxDwrJ3NCRteXykjV5sKyAZSRToqLQ4csH668ei-hCNA1O6cyV7b3lhFOQAc47BkP7l4KJRkoq-2VtocwPp3vu9pbbt6EI-fGNlimUG7gkPH_CKlyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67400" target="_blank">📅 00:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67399">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/733e727650.mp4?token=OKXLjpGva2VMJa7d94SYGH3NxjZHsJaKTGEpv7Xa8_bmWHlUkNkOHT3sn7H9sCisLAKmzm4hJnfZx9NrEhlr5O0lN0HdcNO75ob3KFmQsLDRHaoVncGeVs6-33FA00Z4OYZ9wcZ1mu5sYp1e4EXx-LySgzjfddWTVh-OJWliIZI1zF37MZhACXjHESleeepUy8QObs3KhzFl-6qMFQ0bpxek8nvihRRVHNk2qvkCax_E-PmHeysVcVM-U2T7LrzjjPpNvrAYXwMEjYjXHGgha95p2zPWDIxOhXY-GxxaEtHnGfMzsLeSOwVaackweqxL__hW20ao-AVGnq7Re2WVjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/733e727650.mp4?token=OKXLjpGva2VMJa7d94SYGH3NxjZHsJaKTGEpv7Xa8_bmWHlUkNkOHT3sn7H9sCisLAKmzm4hJnfZx9NrEhlr5O0lN0HdcNO75ob3KFmQsLDRHaoVncGeVs6-33FA00Z4OYZ9wcZ1mu5sYp1e4EXx-LySgzjfddWTVh-OJWliIZI1zF37MZhACXjHESleeepUy8QObs3KhzFl-6qMFQ0bpxek8nvihRRVHNk2qvkCax_E-PmHeysVcVM-U2T7LrzjjPpNvrAYXwMEjYjXHGgha95p2zPWDIxOhXY-GxxaEtHnGfMzsLeSOwVaackweqxL__hW20ao-AVGnq7Re2WVjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
عجیب‌ترین چیزی که امروز میتونید ببینید:
نیسانی که با یک چرخ جلو بدون مشکل داره حرکت می‌کنه و سگی که داره راننده رو قانع می‌کنه تا دست از رفتار‌های کصخلانه خودش برداره
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67399" target="_blank">📅 23:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67398">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aad6611348.mp4?token=CstntrfU1NInkY1BD_z73FCp_qFkGgrS5Xl4RZ3E9_qYTdB5g5Hri_dzNxP_wwZ3xF2Wdle3dhGVWqjxbVXLmDpa19q5RDNjn4aUdLzTXLNOGhm8OqJU_0VZzSjoJnp1CTePy83RDc71xDeZaXpWXvaHubknPnlGwC-ngAxdoxzboKpaigyIp91sTcmGvczi86eWNN2hJCWw6WH3vCj50VJSDTDekrUJiJRACcPlwiz4vvoW15xPXkyNh_Mh23P5iDDS0bIBKjjeDtD5LFD5gzE3F856fv8tl5Ww9F4ZZD6-CQ-TgSeWHUbQC8_LLFETMrWutSieo-f8v0QcYNhRFTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aad6611348.mp4?token=CstntrfU1NInkY1BD_z73FCp_qFkGgrS5Xl4RZ3E9_qYTdB5g5Hri_dzNxP_wwZ3xF2Wdle3dhGVWqjxbVXLmDpa19q5RDNjn4aUdLzTXLNOGhm8OqJU_0VZzSjoJnp1CTePy83RDc71xDeZaXpWXvaHubknPnlGwC-ngAxdoxzboKpaigyIp91sTcmGvczi86eWNN2hJCWw6WH3vCj50VJSDTDekrUJiJRACcPlwiz4vvoW15xPXkyNh_Mh23P5iDDS0bIBKjjeDtD5LFD5gzE3F856fv8tl5Ww9F4ZZD6-CQ-TgSeWHUbQC8_LLFETMrWutSieo-f8v0QcYNhRFTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فحاشی وحید خزایی به خامنه ای
رادان کلاهتو بزار بالاتر!
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67398" target="_blank">📅 22:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67395">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tZacixuBk_Qqp8vSUyRuWvXf2JWFS6dzKHIpK_Aw0IH1mBdUYGwzLWvwp4cjUCTDFvGPv9xLee9hJv8kbIScwkdWFl1cAyuehlOeoidLNZ1TTWlGc58DOFQFxC-yV8JA-tZwNLezlQCGiG-hvnsxlmi9TASmaBlMpHhpaMZpMF69fmwlhAq3twyEyo2Gz2RSyqMtgaWRrKSKGWaBjQXYyjDZGgTO5XFDmabs0JNepn-VX6aDwPPFys81eyg589TI5iilnMG5P4oOVMuvp1_tyh5ppPriY0Li4FoaceYIRdusTIoucL6A5imQ2XeTNxLKWcAm4XOFrGckVpOsDOuOuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AoBkSgGr36DfVYr9Bf1AEUdCITgyQgf4z85jwHeLF17lNsqXs3j3iDJw85GqZsLGh3ig_heVHIOOKcaXYEXF-RzhFOBcWcQ9HZMuCIEXynsrCiuXseI7ZQUPKhJEexFBsn-oS9ggejveJ9_-kKcBycb5gLPETDFajefDMYvLZcqnMe8YzxsreqePs9qXT_kHWQnDaxGjpn9PvHHMgxGUeHAWOtL2KOFsvaABDEObuqXceUMSC9xexE9GQaFDBZYMQWRUrr5M0RZBKFs7CDg30F8hgNZmyOUgDyvXgx7gXJ3bwu40tqETg_zd5o_twgQwnud3XrW2El-5JoTH-ZUbnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/886967cfe3.mp4?token=UIUMKXgqGcKnZAz3UkkDhkalN2794KYmmEAsK8YZ7YqQ_ES5thmt6VMyaNvTI8_vYYQADU-qbl5bpBc03S45egZcLtfTt3MfIw0KqFK5odYZ82RPFNU1zmIyo8NNwqVYjjfEs11TXyF_Ugwf4VXAJSPz8M8DESawjIF0BbsdcHy57IlVqk4J-OJBUckQ4cLA5oI8lxuUEfGrjurb-PaEivDNhg62TmJY-nHvOoTYDtoWpIPuUABt7WS8S1rViAXOKpMU7ovL3cbA5K4DCAHCvteswvibdNGHMerI2H-9vI6M0BftTzAbqZjLTwfUReD7iK1xbZih3GADukaKlxb5og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/886967cfe3.mp4?token=UIUMKXgqGcKnZAz3UkkDhkalN2794KYmmEAsK8YZ7YqQ_ES5thmt6VMyaNvTI8_vYYQADU-qbl5bpBc03S45egZcLtfTt3MfIw0KqFK5odYZ82RPFNU1zmIyo8NNwqVYjjfEs11TXyF_Ugwf4VXAJSPz8M8DESawjIF0BbsdcHy57IlVqk4J-OJBUckQ4cLA5oI8lxuUEfGrjurb-PaEivDNhg62TmJY-nHvOoTYDtoWpIPuUABt7WS8S1rViAXOKpMU7ovL3cbA5K4DCAHCvteswvibdNGHMerI2H-9vI6M0BftTzAbqZjLTwfUReD7iK1xbZih3GADukaKlxb5og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فیلم اول تصویر کوچکی از جمعیت یک میلیون و هفتصدهزار حجاج است که امسال برای حج به مکه رفته بودند
مقایسه کنید با:
🔴
فیلم دوم جمعیتی که روز شنبه ۱۳ تیرماه، با وجود واردات عوامل جیره‌خور نظام از ده‌ها کشور در مصلی جمع کرده‌اند
آن هم در تهران با جمعیت ۱۵ میلیون نفری!
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67395" target="_blank">📅 21:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67394">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1d208e49.mp4?token=Zx7cskdGB_IuGrNIOoUWbq7YkTzSXA-XcdA5qy_EifP6g-k2Z_OaCi-w_fcea-gtf7f8KtsQExiUc801j3ShPq4luTqyXyj-vojM5f8P0EQ2GojPqwfZGNz4u-xwS8C5kMzbSI_jwCtBL7Kuffq5c2KVjtMKKxszEQymP7oKHlfvxzAVyggFdnUIsyU8gmgNtgdqjokAneTUyvmG9MyvBO8DJvz9uIJmyNEvKuxICiWqBMbygYbKLESGo2pJtU3FiqWrzDGSh2CxTJf_aBIMc0axjfI0ZR9tMdRAw4oLLDMR2tiEPH0f6R97XdYIyOo1fGqBPE4TP17nX68dgRLvPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1d208e49.mp4?token=Zx7cskdGB_IuGrNIOoUWbq7YkTzSXA-XcdA5qy_EifP6g-k2Z_OaCi-w_fcea-gtf7f8KtsQExiUc801j3ShPq4luTqyXyj-vojM5f8P0EQ2GojPqwfZGNz4u-xwS8C5kMzbSI_jwCtBL7Kuffq5c2KVjtMKKxszEQymP7oKHlfvxzAVyggFdnUIsyU8gmgNtgdqjokAneTUyvmG9MyvBO8DJvz9uIJmyNEvKuxICiWqBMbygYbKLESGo2pJtU3FiqWrzDGSh2CxTJf_aBIMc0axjfI0ZR9tMdRAw4oLLDMR2tiEPH0f6R97XdYIyOo1fGqBPE4TP17nX68dgRLvPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67394" target="_blank">📅 20:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67393">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67393" target="_blank">📅 20:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67390">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lHmOWb57ESvwD1lmnh8AGJT2yhqYa7xogtro43tpW4TUHbE7tVf2bvuHue2e4pjEiP1VSGuoHBwl9bygk0ZnDrD7l3FKaAYEZDgq_Y3WquMFIjXTAc3eZmsRWDtGYmOhfe-YB86rptFKLPHwj9Pg4ys2MpEvptkY6ypkp7r5QNURDKzpGrUkcN-WaaVUnEA8Ee9UbjT6KIB5OlW256XtlveNmsKo0MS6Z32Sr3Pb-FGlBIZ3dKpc8ailCtSsIi0DQ0XwCqYilu2b_sqszgg-_9YQ9xVd4nNDdwlV7drEoQP_x4a5RgmhnzAqRzaSJZ2RogZJmFxM4DspXzyB8pdy3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h-78030nbKsBC3oTqufbu9BKHgHnqSgZxKLM-XB_wbZOp3XbOmmVSeDIYEcHRSZ8UBH14xejAGtXaHjc2g0TQb5jfdnc38gwEbFAwMqau8S45BnWrvrmMMtO8UMlyrDGnCDreCOxpzhgcGyUhAhiO-rtA4S95IhJmXhYaICnaag9wgs_Pl5ALZCq3twzAUbIfFdtGAGN8qI6lOdhfZgi3N9_sWd_JOqJRCT4bqd73cPajsFlOkjeUycIrN8M-7j0b2vCh9VZEqkx7kP8zJ2VFUOkWo6d3-fCAf-p5Pk27xHaD8Kcuq3wVdeFuP-Q1fMwEpoR2b-uj25bEEiwLq6Hrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bea0c04d9.mp4?token=LT9_mXb80HrrrB69mzXENS6qLbkY1ljzuuX2BqzKXCuYlGmvWj45vObBOHBNCpyOjIuwdUEZoymtLmdkmXS4zYBVD3qzPZh-Jp_9xF9RQHCw_q9ilVKrxlgOt6VILhHNr3VKMuDHFj2AwYSfAKMMam-2lMdCKduaw47caY5Wo2IbFYidyUp5IrlzZnklk_y2JlW82zbnbg2ea9pN5T072utFwPwVx9ZdkqaFNR1wjX0XjWXQUeDJfgjDFR6NRJ4wzoCQ4wPZ8co_2VDNNIQ8g4BNBfXQlCRXBYFMJZ67Q-lJ9tAJG2-AY2LcW9r-ugwnLoqH_PnMnvkIOIZmjQYl0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bea0c04d9.mp4?token=LT9_mXb80HrrrB69mzXENS6qLbkY1ljzuuX2BqzKXCuYlGmvWj45vObBOHBNCpyOjIuwdUEZoymtLmdkmXS4zYBVD3qzPZh-Jp_9xF9RQHCw_q9ilVKrxlgOt6VILhHNr3VKMuDHFj2AwYSfAKMMam-2lMdCKduaw47caY5Wo2IbFYidyUp5IrlzZnklk_y2JlW82zbnbg2ea9pN5T072utFwPwVx9ZdkqaFNR1wjX0XjWXQUeDJfgjDFR6NRJ4wzoCQ4wPZ8co_2VDNNIQ8g4BNBfXQlCRXBYFMJZ67Q-lJ9tAJG2-AY2LcW9r-ugwnLoqH_PnMnvkIOIZmjQYl0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
پهپادهای اوکراینی اوایل امروز به پالایشگاه نفت اومسک، بزرگترین پالایشگاه روسیه، حمله کردند.
این پالایشگاه در فاصله ۲۷۰۰ کیلومتری از خاک اوکراین واقع شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67390" target="_blank">📅 19:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67389">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee21b0d93c.mp4?token=Cp3SqfpTUG71i5lqzRQxOOXNhywC1xFpafEy5x7NaBmU0BeGrXE8RWOLECQZgjMb_Y_ZxTPpP8hhrTqu7HMIQ6qdL7xGKqj9qdOpV6mfdSbceV0W2_QZLdwtamPiajVy-6zac-FvmJlMQs_qgDmYHPHM2JWOfQqyEUt8JzlaZCYbla86VrMqqKclKju_tHEpwPcrzJoR3fJa4M5k2kGZGMvB6ghbivFJXvyyZjQOZULqUWMpgLI5LZx4j15Oz_q5AYFBMvsmp3BBklIbt_xu35QYoFoqB_pdWOe9p8RRaSQa7CggslcoNa-lnlAdWRU_QBlcL9qhf0lCnTztBEJ-Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee21b0d93c.mp4?token=Cp3SqfpTUG71i5lqzRQxOOXNhywC1xFpafEy5x7NaBmU0BeGrXE8RWOLECQZgjMb_Y_ZxTPpP8hhrTqu7HMIQ6qdL7xGKqj9qdOpV6mfdSbceV0W2_QZLdwtamPiajVy-6zac-FvmJlMQs_qgDmYHPHM2JWOfQqyEUt8JzlaZCYbla86VrMqqKclKju_tHEpwPcrzJoR3fJa4M5k2kGZGMvB6ghbivFJXvyyZjQOZULqUWMpgLI5LZx4j15Oz_q5AYFBMvsmp3BBklIbt_xu35QYoFoqB_pdWOe9p8RRaSQa7CggslcoNa-lnlAdWRU_QBlcL9qhf0lCnTztBEJ-Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ در مورد جنگ پهپادی:
چه کسی فکر می‌کرد که پهپادها به چنین عاملی تبدیل می‌شوند؟ آن‌ها ماشین‌های کشنده هستند. شگفت‌انگیز است. شما پشت درختی پنهان می‌شوید و آن می‌آید و شما را می‌گیرد. و من صحنه‌هایی را دیده‌ام که نمی‌خواهم ببینم و نمی‌خواهم شما هم ببینید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67389" target="_blank">📅 18:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67388">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02a06527a7.mp4?token=iamJRIARGsa3I2QyZ6DXG2klzD9PKHHSDpxgbrNIGLSaGZpeCcAueweWQAnGxd9tikYheFX72RofVvjeHjqAaiZRixRoKAIhaKUg9w1QJmNoG4nYkwi1WUtO7d_pGD5NS7RVPMXEw-dESs5QS38wa8JM3WowEzp54w9dLETbVPwy1pNNn1N0WkSNPtdSZ1GnJtTvcdCD0YIW3dFK51AfDaRip2X-ZfHNrfxaKOobwl_wDI5Ke8E7auS2eYgL7gfXLgtMVwCuqkUk3lI419LHg4izTsKMUIV4LUf8YAbck-Ykl85CpQPhv7pHlaTg_tuqbVVi0l3YkSSkj7jxFZD93g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02a06527a7.mp4?token=iamJRIARGsa3I2QyZ6DXG2klzD9PKHHSDpxgbrNIGLSaGZpeCcAueweWQAnGxd9tikYheFX72RofVvjeHjqAaiZRixRoKAIhaKUg9w1QJmNoG4nYkwi1WUtO7d_pGD5NS7RVPMXEw-dESs5QS38wa8JM3WowEzp54w9dLETbVPwy1pNNn1N0WkSNPtdSZ1GnJtTvcdCD0YIW3dFK51AfDaRip2X-ZfHNrfxaKOobwl_wDI5Ke8E7auS2eYgL7gfXLgtMVwCuqkUk3lI419LHg4izTsKMUIV4LUf8YAbck-Ykl85CpQPhv7pHlaTg_tuqbVVi0l3YkSSkj7jxFZD93g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ درباره کارت قرمز بالوگان:
من درخواست بازبینی کردم چون فکر نمی‌کردم این یک خطا باشد.
این یک نفر نبود که به صورت کسی مشت بزند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67388" target="_blank">📅 18:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67387">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e1e1775aa.mp4?token=Ix0EcNdN_cFq48gFgu4OfuUxKKK7uOiVwJYqF-BpDol1ixEUfLpcUNwdROc-o4jVR9FY5uuLD1QZSlML6B5l_jPBWCkHVrKjQf1t4WHyx9WemcsSFvq0p1q1JWWQ3sxVA5D1Nlh-fdNpNwVvwY3vbhRXkSaGzrfCPLRlBzTjKS7FGYkcQahbkkcciMpEDTSlK_lrGbulxC4NXc0K6T5E5ntTReVLh995uCzuwCAYpvLcJP_Qx6KC-n9HljKiSmKBX2ukaobRspJi1IznPVNE0_Q6nezeh15DkEf8tgKtNenOsIkMxrealCLHfp1aERFfK3hMlDTgVnup8bnqDChKaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e1e1775aa.mp4?token=Ix0EcNdN_cFq48gFgu4OfuUxKKK7uOiVwJYqF-BpDol1ixEUfLpcUNwdROc-o4jVR9FY5uuLD1QZSlML6B5l_jPBWCkHVrKjQf1t4WHyx9WemcsSFvq0p1q1JWWQ3sxVA5D1Nlh-fdNpNwVvwY3vbhRXkSaGzrfCPLRlBzTjKS7FGYkcQahbkkcciMpEDTSlK_lrGbulxC4NXc0K6T5E5ntTReVLh995uCzuwCAYpvLcJP_Qx6KC-n9HljKiSmKBX2ukaobRspJi1IznPVNE0_Q6nezeh15DkEf8tgKtNenOsIkMxrealCLHfp1aERFfK3hMlDTgVnup8bnqDChKaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ درباره بالوگان بازیکن تیم فوتبال آمریکا:
بالوگان بهترین بازیکن ماست. او کارت قرمز گرفت. من نمی‌دانستم این چه معنایی دارد، اما بعد شنیدم که به این معنی است که شما نمی‌توانید در بازی بعدی بازی کنید. این بسیار ناعادلانه است. چگونه او را برای بازی‌ای که هنوز بازی نشده است جریمه می‌کنید؟ من درخواست بازبینی توسط فیفا را دادم.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67387" target="_blank">📅 18:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67386">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af665dba5e.mp4?token=u16F4FhLhQNHZijthpsEkD065sPfezV_iSF8DxYSmWpFsG0fmixD5qYtBFb1fjWg1IFwgLBhNbX_71AsszEWNq8m9hEg5QLg3awaEdTEBbD3WO6yAMqAyaRarE-9hMZXnuSyjLVm6Q8yuv7BPscADrj70KPIc4CNWxTWaAFPAYIJq1882ZYS_lE7PAnfihXHRuG4y_73QV74qltSiHQPUrPgV6Ji-ycmyzRlJ1PFRaRnSzk-L5-OygOR4QfPS_rI7uSdqiWdm18xGlXyDDir2H7WUPIkAuXX1pi8NzDX_r_5Yz2ZKYkw6y3Ba8z-92SNgItQ1pt0a39NGcWxdWRZnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af665dba5e.mp4?token=u16F4FhLhQNHZijthpsEkD065sPfezV_iSF8DxYSmWpFsG0fmixD5qYtBFb1fjWg1IFwgLBhNbX_71AsszEWNq8m9hEg5QLg3awaEdTEBbD3WO6yAMqAyaRarE-9hMZXnuSyjLVm6Q8yuv7BPscADrj70KPIc4CNWxTWaAFPAYIJq1882ZYS_lE7PAnfihXHRuG4y_73QV74qltSiHQPUrPgV6Ji-ycmyzRlJ1PFRaRnSzk-L5-OygOR4QfPS_rI7uSdqiWdm18xGlXyDDir2H7WUPIkAuXX1pi8NzDX_r_5Yz2ZKYkw6y3Ba8z-92SNgItQ1pt0a39NGcWxdWRZnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
یا قرار است توافق کنیم، یا قرار است کار را تمام کنیم، باشه؟ و تمام کردن کار سخت نخواهد بود. ترجیح می‌دهم توافق کنم چون نمی‌خواهم به ۹۱ میلیون نفر آسیب بزنم. می‌توانیم پل‌هایشان را در یک ساعت خراب کنیم. می‌توانیم تأمین انرژی آن‌ها را قطع کنیم، تمام آن کارخانه‌های بزرگ که ساخته‌اند، بزرگ، زیبا و مدرن. آن‌ها اکنون هیچ پولی ندارند. ما به آن‌ها پولی نداده‌ایم. می‌توانیم کارخانه‌های تولید برق آن‌ها را، به قول من، در بخش کوچکی از یک بعدازظهر از کار بیندازیم. هر کارخانه‌ای از بین خواهد رفت و آن‌ها این را می‌دانند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67386" target="_blank">📅 18:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67385">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f387513a36.mp4?token=J1aP8CBBIqoaYhGs8PHSovbpQD2k8nEvgifaRAwncu2V1iIZabYmzrcRA5oxt2OQBeojR9ZD9sP8pDOj8pNjzJYYuTYf4-yllTsWjEnAMXA0hnGIXmxlpW2oQdZkw1u-5uwddHEs-j1QMMp9M3z0ovU2GjZGmJROsGRWwrbOfuPR6_6RYfXrLu4qGqJoU5Dsxbcehy3hdG1tEZKA9kuGnV4MIqIGYcWSTb4OP5MRGCwDzbkx-6lyNcOW_TfP4r7NJSYDa29XlfhE6iav_CA7pRcLw-thRK3-Yz8iJEhE4YK9q33FB0rCG7j9jtN5k61SICi6Zkzgor36G9Zc8TN0OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f387513a36.mp4?token=J1aP8CBBIqoaYhGs8PHSovbpQD2k8nEvgifaRAwncu2V1iIZabYmzrcRA5oxt2OQBeojR9ZD9sP8pDOj8pNjzJYYuTYf4-yllTsWjEnAMXA0hnGIXmxlpW2oQdZkw1u-5uwddHEs-j1QMMp9M3z0ovU2GjZGmJROsGRWwrbOfuPR6_6RYfXrLu4qGqJoU5Dsxbcehy3hdG1tEZKA9kuGnV4MIqIGYcWSTb4OP5MRGCwDzbkx-6lyNcOW_TfP4r7NJSYDa29XlfhE6iav_CA7pRcLw-thRK3-Yz8iJEhE4YK9q33FB0rCG7j9jtN5k61SICi6Zkzgor36G9Zc8TN0OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
تنگه هرمزِ معروف؛ هیچ‌کس تا حالا اسمش را نشنیده بود، اما عجب ماشین پول‌سازی است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67385" target="_blank">📅 18:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67384">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b6983cd6.mp4?token=n06uBrhdFbpg6BFp3nJ197b80Ld9OnA2G2RJizUT3qosBZbf5rWPjevcTRKpW1Q-S46w_aHcqAL4PFIhhu-NjgCiqJsC5ep0mCD7iGviGkhvD_38lbC5QT58e0zykwwe1-2H6bBzI6RGvC38QcWxF8ajEV_VcUcyJd-iMCthAvDlBwbXRGdeHr6xkItSCv7JNFJVx-2GgcOY0DRXrc3osK4buTBP7GcSRRkvezC1bKTLDz2wCPmhO4VwZDwMgzScHwhO58lWjk54T3IAs7CRAVWm-nyj4uaLQ0y2KEhWWeNb_ttaKn6HfJt6-ZX3RhmLlTfqEboEyFZfx170rRBrsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b6983cd6.mp4?token=n06uBrhdFbpg6BFp3nJ197b80Ld9OnA2G2RJizUT3qosBZbf5rWPjevcTRKpW1Q-S46w_aHcqAL4PFIhhu-NjgCiqJsC5ep0mCD7iGviGkhvD_38lbC5QT58e0zykwwe1-2H6bBzI6RGvC38QcWxF8ajEV_VcUcyJd-iMCthAvDlBwbXRGdeHr6xkItSCv7JNFJVx-2GgcOY0DRXrc3osK4buTBP7GcSRRkvezC1bKTLDz2wCPmhO4VwZDwMgzScHwhO58lWjk54T3IAs7CRAVWm-nyj4uaLQ0y2KEhWWeNb_ttaKn6HfJt6-ZX3RhmLlTfqEboEyFZfx170rRBrsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
به یک دلیل وارد شدم: ایران نمی‌تواند سلاح هسته‌ای داشته باشد.
من به دنبال تغییر رژیم نیستم، اگرچه این تغییر رژیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67384" target="_blank">📅 18:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67383">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d6c7e39a.mp4?token=H2q41KND9GnX5w0ACSxv6qNOxMtMwBxYy7-g3ZCy6oFsi9x8vMwRUjvfAn5kW4YHuWPiHx-ZNVUsAvMmiyntPGJrBhPVm4BdAxopnva6Moz-ofs22xlnc-a42wo_j-Tk7lZD81kj9lRZvw8JkGOHzPmhsbNdoJBatFMa9lFWHHGc71CBQeWMWoCtTFW1Nu3zi75BQFHLyukMj-og3zZmMhhIuhoYAadmQpDSacziGR6Y4ERccDmkmyc1B6f9X-74I5IX69jGhurU1l4QmzkNxPzk0-t9aBHUB8ARldG3rlODg1KuZOeSmuGKnj5_97vr1agJsGbwaJslyhp2nMNtEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d6c7e39a.mp4?token=H2q41KND9GnX5w0ACSxv6qNOxMtMwBxYy7-g3ZCy6oFsi9x8vMwRUjvfAn5kW4YHuWPiHx-ZNVUsAvMmiyntPGJrBhPVm4BdAxopnva6Moz-ofs22xlnc-a42wo_j-Tk7lZD81kj9lRZvw8JkGOHzPmhsbNdoJBatFMa9lFWHHGc71CBQeWMWoCtTFW1Nu3zi75BQFHLyukMj-og3zZmMhhIuhoYAadmQpDSacziGR6Y4ERccDmkmyc1B6f9X-74I5IX69jGhurU1l4QmzkNxPzk0-t9aBHUB8ARldG3rlODg1KuZOeSmuGKnj5_97vr1agJsGbwaJslyhp2nMNtEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
مقایسه اجرای سحر امامی، مجری تلویزیون جمهوری اسلامی، بعد از مرگ علی خامنه‌ای (10 تیر 1405)
و اجرای ری چون‌هی، مجری تلویزیون کره شمالی، بعد از مرگ کیم جونگ ایل (28 آذر1390)
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67383" target="_blank">📅 17:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67382">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3237168e66.mp4?token=tX_cC8OeTbNo3RcJp0wU2J_-LkKlek2B6U-wANiDIxdx8kMvyiEeaMiWbwPxaWClELng8YAFDWr2LA2oibALUBxZelP7CB1WuDLU9h6nT41EXJlSsEht7YKPOdmKlF1rGjqOv-rxBMkPjmcHuwu_8chEkqlEVhgDKP5ivUIQ0TZ6zz5dNhIl85bPL4tyzGYwQ7U7RNdgPR_0C_JurIQZq9u_28QFZVNLXDSr5CsRu7UzqEU54QJ3Igbsp0slCEEYLi7m7BRwInNPvPKtLmcc9RdkMu48zUoynE3Fa8cSRf0W3aHUTwsgma2hoTlBlviVN_ZLf6ZgBkY3u4f1T4EppA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3237168e66.mp4?token=tX_cC8OeTbNo3RcJp0wU2J_-LkKlek2B6U-wANiDIxdx8kMvyiEeaMiWbwPxaWClELng8YAFDWr2LA2oibALUBxZelP7CB1WuDLU9h6nT41EXJlSsEht7YKPOdmKlF1rGjqOv-rxBMkPjmcHuwu_8chEkqlEVhgDKP5ivUIQ0TZ6zz5dNhIl85bPL4tyzGYwQ7U7RNdgPR_0C_JurIQZq9u_28QFZVNLXDSr5CsRu7UzqEU54QJ3Igbsp0slCEEYLi7m7BRwInNPvPKtLmcc9RdkMu48zUoynE3Fa8cSRf0W3aHUTwsgma2hoTlBlviVN_ZLf6ZgBkY3u4f1T4EppA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
مارکو روبیو: سوسیال دموکراسی همان کمونیسم با ظاهری آراسته است.
مارکو روبیو، وزیر خارجه آمریکا، با انتقاد از سوسیالیسم و کمونیسم گفت تنها کسانی که کمونیسم را از نزدیک تجربه کرده‌اند، درک می‌کنند که سوسیال دموکراسی در واقع همان کمونیسم با ظاهری آراسته است و پشت این ظاهر، همان ایدئولوژی خطرناک و ویرانگر کمونیسم قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67382" target="_blank">📅 17:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67381">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54408a1a4b.mp4?token=bhqI9fRkxv2qL37JtBYBzLhnN8Zse_nUJouz0lTgmhnh8uSlifOhVH7G1N4Sqa1QrebrahbZbyou38_Pj4Q_X7FhEiTxQwijWohFrpUwse95A7zTv_x4uIQkY1wQbb8T04GZkUnmZTTYSL_Bf2HM9hzvfiF5khNIOoROD3SnYMl6M3Zr9xMmdOA0r2d_UVl2ko8RajKk6hnbQEJNHLy4hgJe6qlo1UP48lXx5_wYf4Y-L37mdOIanM85F53eGdiyYkj6OhKyYiz48R5M2C17VjIx0C2NVyDTrR9R3B-CoDFJhnu1wQRG1ZrCpVSABsSmJ9blEHJAn6C2o9F17TmWZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54408a1a4b.mp4?token=bhqI9fRkxv2qL37JtBYBzLhnN8Zse_nUJouz0lTgmhnh8uSlifOhVH7G1N4Sqa1QrebrahbZbyou38_Pj4Q_X7FhEiTxQwijWohFrpUwse95A7zTv_x4uIQkY1wQbb8T04GZkUnmZTTYSL_Bf2HM9hzvfiF5khNIOoROD3SnYMl6M3Zr9xMmdOA0r2d_UVl2ko8RajKk6hnbQEJNHLy4hgJe6qlo1UP48lXx5_wYf4Y-L37mdOIanM85F53eGdiyYkj6OhKyYiz48R5M2C17VjIx0C2NVyDTrR9R3B-CoDFJhnu1wQRG1ZrCpVSABsSmJ9blEHJAn6C2o9F17TmWZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در برنامه ای در صداوسیما حدود بیست دقیقه کارشناس برنامه اسامی سران و مقامات جمهوری اسلامی که توسط آمریکا و اسرائیل ترور شدن رو خوند
بعدش مجری به کارشناس گیر داد که الان بیست دقیقه وقت برنامه رو گرفتی که اینها رو لیست کنید و در ادامه میگه به جای اینکه به مسولان و مردم دلگرمی بدی داری دلشون رو خالی می‌کنی.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67381" target="_blank">📅 16:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67380">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84629e4c7d.mp4?token=pyFRUfkbFcMaDFbh6mra1o_TexiGs48dRoA8F8qfgD-MMxWZq2x_VnEndFCDcizeb-Xk57ycdZsK9zC0qSRA3_AvVtmHQqAhM4MU0OsmtYCXuirniPTqBfDnb4CuibOCn7bBYlKhKIHzaKpVWi0TCqFkp7mgqYsmLYOXngW05Z8SmpgiRqyx_iXO-6DsJ7FBRTJpc622gVHDaLkxvYdFcVrLdBlAFyEgycm6t36ZcPikEQnVd0arJYwc3womRifEj-6CF2mw8olp09IX5Woh6rmdYGeOWz1f5Ptjh4KRaI2VVb1W2p2ZtfoMmJP7gX3YywlCm6D9gtylfPwFRW0-4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84629e4c7d.mp4?token=pyFRUfkbFcMaDFbh6mra1o_TexiGs48dRoA8F8qfgD-MMxWZq2x_VnEndFCDcizeb-Xk57ycdZsK9zC0qSRA3_AvVtmHQqAhM4MU0OsmtYCXuirniPTqBfDnb4CuibOCn7bBYlKhKIHzaKpVWi0TCqFkp7mgqYsmLYOXngW05Z8SmpgiRqyx_iXO-6DsJ7FBRTJpc622gVHDaLkxvYdFcVrLdBlAFyEgycm6t36ZcPikEQnVd0arJYwc3womRifEj-6CF2mw8olp09IX5Woh6rmdYGeOWz1f5Ptjh4KRaI2VVb1W2p2ZtfoMmJP7gX3YywlCm6D9gtylfPwFRW0-4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو در گفتگو با فاکس نیوز:
ایران کشوری با حدود ۹۰ میلیون نفر جمعیت است و حدود ۸۰ درصد مردم آن از این رژیم متنفرند. اقلیتی که شعار «مرگ بر ترامپ» و البته «مرگ بر من» سر می‌دهند نماینده مردم ایران نیستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67380" target="_blank">📅 16:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67379">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336146a8b7.mp4?token=fwx6TItobztZlvmrOMtHid6qhmnRCjJ7XhrdffXEYPYR7W9MRSHCSi4o-1KEkFMawWUR_JRhIqPoNqiW-TUhLsWvEHOiTc6COGhHBHHNfUliUIKmfyhsKFXYFTdOkBXWOVx1w-KSfW6zEdaq8rH3_9MC29gvmim8t8W914_SFcazC1amSAy9qePwNz0D8iJ1tExIVyT9eQ8EwzkWDrQtT2w9_LsIXIRFCE-b6u1MZ0S3ZZKwHIAhVWiKQUsG9jSBIz6PJuyNVp2DZAQjTlOQMtKu-5dTQ4gMJ3W25ltFyxyUgPwvObPm2zHYjAxZF36Fcb7QgeE8GlcoQ34ngtC4ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336146a8b7.mp4?token=fwx6TItobztZlvmrOMtHid6qhmnRCjJ7XhrdffXEYPYR7W9MRSHCSi4o-1KEkFMawWUR_JRhIqPoNqiW-TUhLsWvEHOiTc6COGhHBHHNfUliUIKmfyhsKFXYFTdOkBXWOVx1w-KSfW6zEdaq8rH3_9MC29gvmim8t8W914_SFcazC1amSAy9qePwNz0D8iJ1tExIVyT9eQ8EwzkWDrQtT2w9_LsIXIRFCE-b6u1MZ0S3ZZKwHIAhVWiKQUsG9jSBIz6PJuyNVp2DZAQjTlOQMtKu-5dTQ4gMJ3W25ltFyxyUgPwvObPm2zHYjAxZF36Fcb7QgeE8GlcoQ34ngtC4ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مجری:چرا آن دولت هنوز در ایران پابرجاست؟
🔴
نتانیاهو: زیرا چند صد هزار مزدور دارد که در روشنایی روز می‌کشند و قتل‌عام می‌کنند و در شب مردم خودشان را می‌کشند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67379" target="_blank">📅 15:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67378">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mmt5adNqU0EjtyljsI-DgIp-U1P7jVn7hwjjGMeV1ptM7gihxZXI4T1PMm-1fxRxwtkZjfUO59buUSn65l9sQYD90-v01oUYMK7cQyZ1WMk1uWBmiy1avANMCnIstUP-Pvyi-FedjVF16xjrzl6KLYtteHyz3lFPrzxDb0n1xuzlKbRTI9LrIRFSOJ5G5Ncdjc6YpmgoNzSImcdWNdAuSzDvrYVOa5hGo-KZH-_nO5Hi4jvSIl6OHYq6DSV6U9g-LD1aEEZzIfW5B8jFZhI5pZrBx5g4Hqjk5Zktu2niclTSUed4Hb0QV5ftvCvR6HV-N3moVcW9yk7UnPvxPxogdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
واسه کشتن نتانیاهو وترامپ 100 قطعه زمین 2000 متری جایزه گذاشتن،آیدی رو هم زدن اون پایین و گفتن انجام دادید پیام بدید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67378" target="_blank">📅 15:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67377">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vC_-wATR3BAPDoK6FOqTpuHy1Gpcp90bzdbL7r1ELug2avXvlPOnsxbGvSLGPD-hiasUoBIyPDVERInoI0Ceqol-LHwmykspHIHNpAOrkPXm_Z0lzV78TvjagKVkaz21oFCwiXoikpXmoWx21GW6pnaiuFXFd8TPJHWgL3uGKUtUDSWpeIxrb4oY-p86rhT_ad81BNv_QTn29mDzxaUDqH_6lXenzYSNTiT0I47Xx3tsuQL6mSmhR1MPf88vdZ34arAqLnuHWhcBJdiik68tv5nvrV8Xtgd8EOZV_4jsE0_FJAsugK353PBSwoPuzZ4YPwTlUI9I-16rtv0RW7uDxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دو حمله پهپادی هدفمند اسرائیل در جنوب لبنان.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67377" target="_blank">📅 14:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67376">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORsx2qkqI_OmelbpoC3VBftwRnz-0VeJbJUyFWLVYTid-9YaWE-jiTAq0nj_EBW635dp2DPTCvrs3cDwdbxHjT5SGoWnxW8Jm8k6EONN-pV6znaTbD8G1EySf_U-aNkFMITz5xLwQUyhvYJiC88B9QtD_jJiYMTcQqb9cHYXEocV-ealv4ZvzlOiBiqVhLh2CsnXDmVnAMNUz5b20H_HtkPi4lk9VBgP_NwK2uUiA3-SuuLinZ-22Aqw32WLnIpNSwN83IjP79cQdp9XZe87pdv6SCB0ZXjlOyIQc5wgO4uaz-x8iyZEqqBAY4Y-WzbHhqqbqY-VFR33t4NGpFyuAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏شبکه ۱۴ اسرائیل :
سپاه قدس واحد جدیدی به نام « یگان مختار» تشکیل داده است که با کارتل های مواد مخدر مکزیکی و آمریکایی و همچنین ایرانیان خارج از کشور برای ترور ترامپ و ژنرال های آمریکایی همکاری می‌ کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67376" target="_blank">📅 14:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67375">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCQvMMFdZttjpr0_f6xwEFkKoPpUvaihl4K0Y5LWsTaVr-ZdE0FObH2JHOfkEfXlyGE6Vzyc8r-mSgfAxuRXf9NiDHMIwfAqsKgN01DyEhlsA5ORdoF9PLcb4UjwSj7sOwtWrFObCcxBBD8HEyGJoXwcLCbVqsThieidOF3sukSFjaTRiJPWTJsm2J_ECNO0xl29AgzXZyrRjhx5JElPydscKqD44761iQdZXI1bJFAJKeCzFdfcq4KyVLJcRTyEZdwwSyExjJykYCIOr1CqqPXEecq2dx0LCcFD9voi2Wzcht2OkGTX5FdX4maO8RVZpbWlkaseI3F-TZZeDpDbjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یک بنر در مراسم:
دونالد، نابودت می‌کنیم! از توجه شما به این موضوع سپاسگزاریم!
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67375" target="_blank">📅 13:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67374">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsq0wCmyMO22ygwbVWWkWZqJF1FhsHz0Xv-Pmuey7sw8Hi0_tp2mIspGwRyx2FxAlihnmLXsBzyzgfW8f8JeYGVMscGRnHMqf7aUjDST1GBtA2in4AhcoC8oY7UyxK1KYwem5TFcz-TecEmBViBBWeTed2kTCAG5XH3K_ZqyxIHXMgEAK76DLJyyDcDklz3PbaIak-vBlRd-GcKFzvIm82bVGmECIT_cFsOEMejTBBfFurpQoh_ZWJvfYsA9N6yi86duRGtwr2Z1XKT-WSHytkvWDEMW2PY1NpDPln2gsKOwwJl24Svs7POwDHqpgBT9xIBoUJBT4LV9ol0b_rhi5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
ادعای
نجاح محمد علی کارشناس عراقی مسائل خاورمیانه و از حامیان نظام جمهوری اسلامی:
در مراسم تشییع امام سید خامنه‌ای رضوان‌الله‌علیه در تهران، فرزند ایشان، بقیةُالسَّیف، آیت‌الله سید مجتبی نیز حضور داشت. او پنهان نشده بود، بلکه در جایگاهی قرار گرفته بود که کمتر به چشم می‌آمد.
هماهنگی بسیار خوبی با نیروهای ویژهٔ امنیتی و فرماندهان ارشد سپاه پاسداران انجام شده بود…
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67374" target="_blank">📅 13:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67373">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUKikoy2tzNfnEF3xhKFwBsECZupZ6BWhVdmb5vQX-SExwHuUdsy_t-2YAGHwNy7aRfMSGguBysVskpYE_lI7ZvwJzQC0ztVLWka_phQjTSfhMa-JpZayR_AoymQdXI5G1hfKdY6SGeMmmX1f4Jsf9wcrrifPudkwYj0nDpeseb4ua6kJTFtBsKbjFZQLfFaoB_8LW3YQO9fdMMds-vVNt2TP9-f5YK0EhLrwfOdyFhZny4F-0JAF07VY6hDLJyqFOvYhMJJBbmaf8pOVTe5KcZ-StxjlMaa9bMGv_bnd1S4BWmewFh9UZqvPnwmJdRShC4wSXk2TsrOxfPp2dnhZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
«آیت‌الله خامنه‌ای که مراسم خاکسپاری‌اش هم‌اکنون در حال برگزاری است، توسط اسرائیل حذف شد. هر رهبر ایرانی دیگری که برای پیشبرد طرح‌های نابودی اسرائیل تلاش کند و اسرائیل را تهدید کند نیز حذف خواهد شد.»
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67373" target="_blank">📅 12:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67372">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22aca7392a.mp4?token=MaHLCG9BNv9wsvF8m9Z1vLs7ileJDJDjQoQJdY_1LEk5aoH74S3JSwv9wMJxDDF4dJrAs4z6BFXQlef4afb-DktKDOF4rmNLBcYC7K0gPIUlvwFFQqAw0t4Z7M8i_s9_Wed8Nh-uv__hCPW4XxFvsMJewsiuWIMjM_bfZPDrGH-z3i5NvkVSaiENLCRR3Vzc1azQOK6jS5At8QIDxAYy9SiQKvorSM3o1FH5CwJAXFB9RoOP6JL6lPJc0OO6Wo8ZOhr-y4P-3g5orGfDSpxAsCs_QqhJyqcsX9aeZOlihRywbGUYO_1N5lKBARALh-KuAeWXI1TRU6OJqcbBzBMeyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22aca7392a.mp4?token=MaHLCG9BNv9wsvF8m9Z1vLs7ileJDJDjQoQJdY_1LEk5aoH74S3JSwv9wMJxDDF4dJrAs4z6BFXQlef4afb-DktKDOF4rmNLBcYC7K0gPIUlvwFFQqAw0t4Z7M8i_s9_Wed8Nh-uv__hCPW4XxFvsMJewsiuWIMjM_bfZPDrGH-z3i5NvkVSaiENLCRR3Vzc1azQOK6jS5At8QIDxAYy9SiQKvorSM3o1FH5CwJAXFB9RoOP6JL6lPJc0OO6Wo8ZOhr-y4P-3g5orGfDSpxAsCs_QqhJyqcsX9aeZOlihRywbGUYO_1N5lKBARALh-KuAeWXI1TRU6OJqcbBzBMeyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حضور احمد جنتی در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67372" target="_blank">📅 12:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67371">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ad63d7f30.mp4?token=q6rcimTWSukmFyjBwZbV3XL_SlG35PPSc8nCKyvZrbDjEWMaCXOE8jUVCxRxt3x2uBIxIVeI347upw2-2UarFm_w7TVihCXAA0MSalVXooeSdMFvJxezji4chS2eC19BuDKZ7LxU8cK-lUJ0u1H7g4uRO1De9RSI_R0wLOah4Lh77TnjZ4syy0dnJ4RPuPqf9PHdNmOx9aHnsy78vF7UWDH_xFq5XcxRZSkrjHndO2XfMWh6FMK2BvowsozyvPzZ1eiFN7UWC_s7E7BcErOEU57B59b-Ucrc4cnUGCt5s2C768bIFY8xV1pYVx3agAgFOEMJfsOw6oPBka5NCqD1tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ad63d7f30.mp4?token=q6rcimTWSukmFyjBwZbV3XL_SlG35PPSc8nCKyvZrbDjEWMaCXOE8jUVCxRxt3x2uBIxIVeI347upw2-2UarFm_w7TVihCXAA0MSalVXooeSdMFvJxezji4chS2eC19BuDKZ7LxU8cK-lUJ0u1H7g4uRO1De9RSI_R0wLOah4Lh77TnjZ4syy0dnJ4RPuPqf9PHdNmOx9aHnsy78vF7UWDH_xFq5XcxRZSkrjHndO2XfMWh6FMK2BvowsozyvPzZ1eiFN7UWC_s7E7BcErOEU57B59b-Ucrc4cnUGCt5s2C768bIFY8xV1pYVx3agAgFOEMJfsOw6oPBka5NCqD1tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیوی عجیب منتشر شده از وحید خزایی شاخ اینستاگرام با سردار رادان که میگه کار دارم با وطن فروشای لاشی،ترامپ گفته گوه خوردم
من سلطان دختربازی ایرانم ،حتی سردارچندبارمچ منو روی کار بادخترخالم گرفت ! اماخداشاهده آنقدرمهربونه،هیچ کاری باهام نداشت و ولم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67371" target="_blank">📅 12:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67370">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a17dafc375.mp4?token=Uu8Kowgdeb4d8G6A4hSxJreYi5M6-MbHuP_53ZEHSZXZvnCQ5KZaQqIvyAxvD9TrmeFloXG8Kial0N_1kL8RxcOf886HK4V7cisd1iSjOsuL_DGVSmGDcqCcG4w1fkvLLvDMPlWD12KyLowkp_P9bwm-Lo2AoFeqbyLfXRil3I4BZWcX_uFos7lmGxeTsSHVI7HYVPeMsWninbl2uSKt8HtaNu9pEx2t5LqJpO-fZzvnAfj9gmaRiaTiT-_zFy_aabBVOBpPGJP44ZzcbIrHsoOoXjsgXDmYjVF1cLx-ysdIAXyRaK5XA6SQrAnq9bF3_hqjaG3V4m_oQLLiImKdUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a17dafc375.mp4?token=Uu8Kowgdeb4d8G6A4hSxJreYi5M6-MbHuP_53ZEHSZXZvnCQ5KZaQqIvyAxvD9TrmeFloXG8Kial0N_1kL8RxcOf886HK4V7cisd1iSjOsuL_DGVSmGDcqCcG4w1fkvLLvDMPlWD12KyLowkp_P9bwm-Lo2AoFeqbyLfXRil3I4BZWcX_uFos7lmGxeTsSHVI7HYVPeMsWninbl2uSKt8HtaNu9pEx2t5LqJpO-fZzvnAfj9gmaRiaTiT-_zFy_aabBVOBpPGJP44ZzcbIrHsoOoXjsgXDmYjVF1cLx-ysdIAXyRaK5XA6SQrAnq9bF3_hqjaG3V4m_oQLLiImKdUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وحیدی فرمانده کل سپاه با موتور اومده مراسم
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67370" target="_blank">📅 11:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67369">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abfc46c7e6.mp4?token=uTX6nrB9LEJVZ3W8AWLfsP_f6JCop8zIZZQUpzL0eSO2kUarIDScri0z5B7JlCvjn3OMdK1v7M0PszW9HSTwwb-4Dj9V2rjUVPrhRJK-N9ZWPcw02km5oobCjqokRPldUKcFfFbioNOCkfPajLIIEXkiWl6JlMMw_p5w9SRXXMIJxcv5gAyvlks08O6heZRsuMcw4pj4wCGc1aTnsD3m6v8_PMMCqXCIjlOrPInq0cNuz5KFAFxV5a2JIRcQ8R6Syqm9VcKoHMBR-6tG0c608BYvtLe3Xfx3u7SC-c5UGkQzQFgJwrGH1yCuHgz6RBHtQVmYFJTtQXNCQ3fqLxO0iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abfc46c7e6.mp4?token=uTX6nrB9LEJVZ3W8AWLfsP_f6JCop8zIZZQUpzL0eSO2kUarIDScri0z5B7JlCvjn3OMdK1v7M0PszW9HSTwwb-4Dj9V2rjUVPrhRJK-N9ZWPcw02km5oobCjqokRPldUKcFfFbioNOCkfPajLIIEXkiWl6JlMMw_p5w9SRXXMIJxcv5gAyvlks08O6heZRsuMcw4pj4wCGc1aTnsD3m6v8_PMMCqXCIjlOrPInq0cNuz5KFAFxV5a2JIRcQ8R6Syqm9VcKoHMBR-6tG0c608BYvtLe3Xfx3u7SC-c5UGkQzQFgJwrGH1yCuHgz6RBHtQVmYFJTtQXNCQ3fqLxO0iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSOD09UcdUbxlpBtPmmE66g_FrMRmIKm8DTRCLo7mvn0J5Bk9hz6W11pIdx-CfK801Wp8IqueZYezf8oDNHKlej6vSQ5Ss08UqkCu-mhkRG6-e9yF4y5KHS6nnC6ftgzH7i9LQS2jTg3mk7Sj0Ok57tA0GMNpNHoelcn8Tr2mLi8MROUIkxxTCCdemUeCRbxBRherEFGl3ovC0JjramDzH1zRbIRfpVZeBynhFL3OdagdC-G4oQemPw_UwXvkF0YJwz5qadar0r031U_lyCeVTb7FpvPjvONrkYz28CV-7gRw6LnKDN1vr9xVNDjiUf3Up_n27EUtAeSFnhMKjdIDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اکبر هاشمی رفسنجانی،24 اردیبهشت 1370:
سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67368" target="_blank">📅 10:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67367">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38c47b7b97.mp4?token=KLwZJWKvux5F9C5_QDk3QHJT6hEaabhH51oDliMqAaepw9dFvjESvUSWx0EE-gIk0Vz2-16d0_Gbv_nqR0XbNrKEFJTQGdo0MpFX4UrzbwiovzPRBv9jAaHqq0GKRwJ7kMn2Buun7X6L8YHX9Z8sUUl0m7BaAEt69Ot2jGi59zjADErO3XxkQLqFCIpKYmlZV4hFZ-WrIxHmfA8P39a86iEyhUlXXaMx0rjnnrR0_E_p6NPFw4PByXn_HtgD91JzW8qGNDACBPQdMOgN4LY8nWDHo6nOLIhro3RffZ-JFRAeIsPJvkY-lxK0RIXy04QfcXcGcK_eLppdxvVi1W260Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38c47b7b97.mp4?token=KLwZJWKvux5F9C5_QDk3QHJT6hEaabhH51oDliMqAaepw9dFvjESvUSWx0EE-gIk0Vz2-16d0_Gbv_nqR0XbNrKEFJTQGdo0MpFX4UrzbwiovzPRBv9jAaHqq0GKRwJ7kMn2Buun7X6L8YHX9Z8sUUl0m7BaAEt69Ot2jGi59zjADErO3XxkQLqFCIpKYmlZV4hFZ-WrIxHmfA8P39a86iEyhUlXXaMx0rjnnrR0_E_p6NPFw4PByXn_HtgD91JzW8qGNDACBPQdMOgN4LY8nWDHo6nOLIhro3RffZ-JFRAeIsPJvkY-lxK0RIXy04QfcXcGcK_eLppdxvVi1W260Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان:
خرافات پدر ایران رو در آورده.
آینده ایران در یک جمله است؛رنسانس.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67367" target="_blank">📅 10:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67366">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33573d06e9.mp4?token=Fkt7t1HRxAPiGrEGCssXiqKaXGGv6lmPx4I8TMZdnQ03gkSNWd6-yhdPG4-eUNHN7j85Nd1L9TN9S5Iw-rNlpzCXiuwdj8XqdfQd2z9jWJMgrqgc9TwfMUA1jZT_vKGwzExt4iKMTg7TOdKIru3aHMjhuX_zXaL79rAlnTx6RPZp1KCBKeEuiWJ7UUOZF1jwfkb9ccQQwN88MX-yuPUgelZNzBlnUTSNb4TTt9omSadBjvAHQRQTcdTDnpdDQDrCRTwP3zHJQSiK6gmZp-AGHpVJerO9dqm48cucsYSS-bSNBLtFkIxQeRNg6JoRQhT5Q5mGhDQJYAcLh-uoeYbRZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33573d06e9.mp4?token=Fkt7t1HRxAPiGrEGCssXiqKaXGGv6lmPx4I8TMZdnQ03gkSNWd6-yhdPG4-eUNHN7j85Nd1L9TN9S5Iw-rNlpzCXiuwdj8XqdfQd2z9jWJMgrqgc9TwfMUA1jZT_vKGwzExt4iKMTg7TOdKIru3aHMjhuX_zXaL79rAlnTx6RPZp1KCBKeEuiWJ7UUOZF1jwfkb9ccQQwN88MX-yuPUgelZNzBlnUTSNb4TTt9omSadBjvAHQRQTcdTDnpdDQDrCRTwP3zHJQSiK6gmZp-AGHpVJerO9dqm48cucsYSS-bSNBLtFkIxQeRNg6JoRQhT5Q5mGhDQJYAcLh-uoeYbRZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو مراسم وداع با جنازه علی خامنه‌ای، وقتی نوه‌های خمینی میرن جلوی تابوت سید علی خامنه ای، قاری این آیه از سوره نساء رو به کنایه می‌خونه:
آن گروه از مؤمنانی که بدون بیماری جسمی در خانه نشسته‌ان، با مجاهدانی که در راه خدا با اموال و جان‌هایشان جهاد کردند، برابر نیستند.
اونا هم برمی‌خوره بهشون وسط آیه ول میکنن میرن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67366" target="_blank">📅 09:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67365">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jah84uaU2udeR2MnHIHtPAO4fKD3klBIJT0anjyTrsn_JNwhjItsNJbgGMtinZUlCMIcVSPjUzyZt9BDFFbEguB21wPQ28SRloYPT5ppQz9uk4yoGO7GyJ_DcTCbnRPBMQThN9OwfgQpuuwcS4Cbhzfd_FdF9rqyVjTEfipeJuiCaJ0zFjvQm9IoAm2HvFTa7a8A1HJB_3ygGZ2gxwaFvrk-k26_fXUQpRGHo3r5-N6vIYh3CLLL4VhPlgdVup_XTw4MD_KHihlIk7roPeqviiUc1IM-CgiRoEupELcOTIgBdjDLs7pjqR1YeiudJvmIL89DBqOWseMahZMvdgchpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67365" target="_blank">📅 09:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67364">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67364" target="_blank">📅 03:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67362">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r70PUhZmeh3J9qh7ezAygeAX2iPtc1RNCbvChELXjjUoI7qCSicEGZR5i0G5D72_qbMY6vQxB2J9PhSIzYtlZTBcD20tElFMrkG1QPr-PluG3FEQW4hdoE7Oh4u7rMZZTk-Aw7YdXIWZeP8zBBaJmX5Pa8YEsuPS-A34S0dltL6t3AAdYzxuSNJtOvL48MtkDJ9wsjQ37GJ6STLMfdh4DEzwsS4hN5LmwARAzWI8cRhPtSfzNSeoCTe5DmvKsyuzRcxr2u4ZFxJaG8EkwXpMiVN9pp1ocAFxqhaL4CCo2l03AxY7UfGDkGpmK942zzfPV7ZRhgmLGL3WEFPzD6Eoyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67362" target="_blank">📅 02:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67361">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1fe48304.mp4?token=U_wMf2dIZzy7zBbB4ZpC6zsBeLWdMlmgXoSoK4r3ZdTI6tJLHpg3alFVsU-tblFmTBkBj630F7tRfKnuHT7yD_945onbfdDgTcszlyca0KxPmWiIJVQ6fjImgjZL79O2x4mNLvHwDsfAPbg5NSe2wYlVjY6iEJaiNz6K1mCljcfxWJqwQyJnPpp3c8-_tCeidUiNGuEhhRnzuCczdDJ7amYtKg3177yOInTBGMexEgzOXYI6ItZY3blpFX118GJTlSOkycJZ6zBRRUn3_DP-4kLMXDfc22lnwbwQJPjHyLW7EwnesIzRpmkPc6gu8gJKN7SbOXyFuIWaznbeR8jgeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1fe48304.mp4?token=U_wMf2dIZzy7zBbB4ZpC6zsBeLWdMlmgXoSoK4r3ZdTI6tJLHpg3alFVsU-tblFmTBkBj630F7tRfKnuHT7yD_945onbfdDgTcszlyca0KxPmWiIJVQ6fjImgjZL79O2x4mNLvHwDsfAPbg5NSe2wYlVjY6iEJaiNz6K1mCljcfxWJqwQyJnPpp3c8-_tCeidUiNGuEhhRnzuCczdDJ7amYtKg3177yOInTBGMexEgzOXYI6ItZY3blpFX118GJTlSOkycJZ6zBRRUn3_DP-4kLMXDfc22lnwbwQJPjHyLW7EwnesIzRpmkPc6gu8gJKN7SbOXyFuIWaznbeR8jgeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67361" target="_blank">📅 01:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67359">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k89p_oPYiYoYFvmLJ-YsstgVMRONk7vL782-sgOwpWAA_QTXWlO6qW9bQNJRUjryPdre1OAClvtGywm1n1ZnrlNEQFyYCW8lswE6YBCc0m0GwdQs-Gkqe7Wn2l3Cymjad77Djs5s8XIIExMvzWokqaRkgGRDYunwQQS0qUL90reN4yzm5Lm7LG8ekhXvnxrVTBnNXESe4HEH1BC6NNeEd1IQRVrexBbVkWq6wuS8jvBMvXRazKJdtmctmDUbbAmKFbY1XRX267uk6drnvW8K6g7RgjY8kGVh-e9DVLl2URtzjuaqQbgahv6y3mV307wblbwC_VvBsJnsgU-yNKqqgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کانال ۱۴ اسرائیل:
انتظار می‌رود نخست‌وزیر اسرائیل(نتانیاهو)هفته آینده برای دیدار با رئیس‌جمهور ترامپ — که هشتمین دیدار آن‌ها از زمان بازگشت وی به قدرت خواهد بود — راهی واشنگتن شود؛ دیداری که در آن برنامه هسته‌ای ایران و خرید احتمالی جنگنده‌های اف-۳۵ توسط ترکیه در صدر دستور کار قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67359" target="_blank">📅 01:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67358">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6d2fa6e6a.mp4?token=q1AwsunayzMvHtqJFJuPdg3R8Nv3aFyeGZjntpycA7GwoZWzWvK8Y-yzovBPsQKg73NbXwURL3wpEUNjchQ5yenvq9eNUaorTwPBO0GdQRr_dwIQyhJQCD3NFazK29YaZfFeqKL49-U-1BUDsFSzynock-ThiFTZC8WGaEEWqdxkq2Td_1DY7G8sv2c2muccjxMUTVYJ_BXgKmkUVBLr6gw6vovdRv1AIT5E_y-43Z4-GCA1Qb4p8iK8HbxxgPDNTtAKxYD4tcsxNGW7RMnB_f9ebT1XvWvF-BcuidJ0JTAJdtZOvkl4sc5YoSyhpQjagtv5nDtjsoG6vS-XyQvpEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6d2fa6e6a.mp4?token=q1AwsunayzMvHtqJFJuPdg3R8Nv3aFyeGZjntpycA7GwoZWzWvK8Y-yzovBPsQKg73NbXwURL3wpEUNjchQ5yenvq9eNUaorTwPBO0GdQRr_dwIQyhJQCD3NFazK29YaZfFeqKL49-U-1BUDsFSzynock-ThiFTZC8WGaEEWqdxkq2Td_1DY7G8sv2c2muccjxMUTVYJ_BXgKmkUVBLr6gw6vovdRv1AIT5E_y-43Z4-GCA1Qb4p8iK8HbxxgPDNTtAKxYD4tcsxNGW7RMnB_f9ebT1XvWvF-BcuidJ0JTAJdtZOvkl4sc5YoSyhpQjagtv5nDtjsoG6vS-XyQvpEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو ای که فرستادن به صداوسیما از لحظه حمله به خونه نتانیاهو و ترامپ و گرفتن انتقام علی خامنه‌ای
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/67358" target="_blank">📅 00:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67357">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/237c10defa.mp4?token=k6RF3oufIEtgCVRURn3MIni3NWlMHeCDdl2Uo5Va9LNndmEr83zDUYy8sVF6eO3YR1ugrASRLeqHgwdSEi-YADvgk6Iq7-3HtV9uE8iIFY29kulupvob6YRavl9VH9U01mSp0TTKWmSdBQ2Wm_QQZZaOuA9TRvbjQzw9Xuj4ytbe8WD7YVUp3v2i5IQCCgFlEqrU3tSwbcqb0fisfji5vqAKE1hg4Jib9Hs3NREuHv0S7xu4UrnBfYoXFNBi5oemxqI5Ms6uKU2CxWdHzkqnwat-Bo5MkblFdXwYHqIw9CMLIwmDHipGehCyOsH_4gqPtGOpfbR-O7gEkwhmg3AWWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/237c10defa.mp4?token=k6RF3oufIEtgCVRURn3MIni3NWlMHeCDdl2Uo5Va9LNndmEr83zDUYy8sVF6eO3YR1ugrASRLeqHgwdSEi-YADvgk6Iq7-3HtV9uE8iIFY29kulupvob6YRavl9VH9U01mSp0TTKWmSdBQ2Wm_QQZZaOuA9TRvbjQzw9Xuj4ytbe8WD7YVUp3v2i5IQCCgFlEqrU3tSwbcqb0fisfji5vqAKE1hg4Jib9Hs3NREuHv0S7xu4UrnBfYoXFNBi5oemxqI5Ms6uKU2CxWdHzkqnwat-Bo5MkblFdXwYHqIw9CMLIwmDHipGehCyOsH_4gqPtGOpfbR-O7gEkwhmg3AWWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پهپاد اوکراینی یه سرباز روس ـ افریقایی رو تو یه مزرعه تو شرق اوکراین بدون شلوار حین دسشویی کردن گیر اورده و افتاده دنبالش
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/67357" target="_blank">📅 23:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67356">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pogdZww8Wv6Wp4ckoh6N9iO6ZJl_3jA4WPfI-d7BmcXTpEoVIfOspmKvKJ9t3tTihyi_AoofSGr28LoLLNIBI3gJk11git4M3wDrXmdkVTWdtxIzB5ez-xudVlvNX9nEBMwc0vFnl-2rkSIsE9rAZH7tN3O68L84449Lqpni2Hw60wKxrrn2MojNxjmbn1Am5YlASlye7mt2RQ_owxtlmwvhStWHZ9YoFWqyWzibNBc2oEbhQZJFiBPvDkZX9OBadJS2Gx9cMuco5-f9CHa2iCTfVsGV_jcOTJHSU0lc3KYPwxrWmQLibhi0iRxIX3NqOjP-o4CsIantslvZSNtQTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سنتکام:
یک چترباز ارتش ایالات متحده اعزام به خاورمیانه، آموزش تیراندازی انجام می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/67356" target="_blank">📅 23:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67355">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb140a8f9.mp4?token=lMNIa8B4lX--40LqAyOB6jbkzKnqpTR5mtW00Hkl0L1T0TDAhZvvi3DW2ntJN52ECSqxLdhBqo6VCikio-E66dqaJ_hFMiUlssmKloxIwjJiEgVs1zdLtnVGszORXm110t2Us8iQErI8PB6zFvX99CTY22y-L9NPii-qYtoD1CvwlmnRhd7SMuwuIhOa1vIlgBABwlXGiOpYnMtJeMExwRBE5i0wpuYgquvKY06aiv7kGh23_9uyHBAAInwGbuYimcmOBAo1BRydKHuG9Rs3nemvQniWrnQ3T3f2lOmTMhKOclA4klMvXg4ogy1p0VJ1GmWUnfOuFhvn8p-ZBu1elA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb140a8f9.mp4?token=lMNIa8B4lX--40LqAyOB6jbkzKnqpTR5mtW00Hkl0L1T0TDAhZvvi3DW2ntJN52ECSqxLdhBqo6VCikio-E66dqaJ_hFMiUlssmKloxIwjJiEgVs1zdLtnVGszORXm110t2Us8iQErI8PB6zFvX99CTY22y-L9NPii-qYtoD1CvwlmnRhd7SMuwuIhOa1vIlgBABwlXGiOpYnMtJeMExwRBE5i0wpuYgquvKY06aiv7kGh23_9uyHBAAInwGbuYimcmOBAo1BRydKHuG9Rs3nemvQniWrnQ3T3f2lOmTMhKOclA4klMvXg4ogy1p0VJ1GmWUnfOuFhvn8p-ZBu1elA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خایه کنین؛ توی اردبیل چند تا آقا نشستن با یه خرس نون و پنیر میخورن
🗿
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/67355" target="_blank">📅 22:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67353">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0RviqqQ5jFI2hqKGbBX8fA80lq-UYXsGHs48K0XnDyHA7o_D5b1EskP5WdkSkTLY7TUTd4x1wbd-8BOr9JKpKTumVv26N788iVTIWp7fmDpu0_YAjiyRLp0joxqZoWVR7WsaK7fR6puogGTbniwWu8UM8e9jAIYkyCbRG2KlmN_eofpmuwVdCE3qKXK-l8bSbzuWkv7eZDrl6bX370duuEQsjsNgxkxcbrR0apA7Fk9w1JT12O9vdxeID1ZiCTDcqjxwua3hIBffRIV197LtrIeu4K9_x6L0r4-z2QQDN6MKUcPvZ0JUYB3qZ-ZRQfAamxkVDmVpsVZewMImhkGpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسرائیل به فارسی:
مثل اینکه مجتبی هم بوده
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67353" target="_blank">📅 22:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67352">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc47a54d3f.mp4?token=GBGtKUhopUe3PzQ7PE1E3qvCW5PIYvg8uOxRxIXJYlalHridGPS1xEaotE6D62yGVaw724OuWO4mxf7EbFMYJT9kywwZYcChDW7ubXKaSxVr65_UI5cg02QyrIBpl-fjKQ_mYpyBU4LBIU-Ym4z3NAPvZFymTcpevLEjg-T-kZPYGDzO3Psu15TyUd0rvrgLKSgi9nryAb5-ol8sFW5PMGkDGpHcBvvtUp1OpyHuBnQVNNosMoPwGBKaNhELWuvtXaIFuCtnYktSmmiqgSwqLcXOTYIBG89QNPxdWADy15i0jQkY9O6hPZO-f5-MiiB6VSebyQdovZwqbzzlUNFXRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc47a54d3f.mp4?token=GBGtKUhopUe3PzQ7PE1E3qvCW5PIYvg8uOxRxIXJYlalHridGPS1xEaotE6D62yGVaw724OuWO4mxf7EbFMYJT9kywwZYcChDW7ubXKaSxVr65_UI5cg02QyrIBpl-fjKQ_mYpyBU4LBIU-Ym4z3NAPvZFymTcpevLEjg-T-kZPYGDzO3Psu15TyUd0rvrgLKSgi9nryAb5-ol8sFW5PMGkDGpHcBvvtUp1OpyHuBnQVNNosMoPwGBKaNhELWuvtXaIFuCtnYktSmmiqgSwqLcXOTYIBG89QNPxdWADy15i0jQkY9O6hPZO-f5-MiiB6VSebyQdovZwqbzzlUNFXRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمزه صفوی :
یکی از گرون‌ترین سیستم‌های حفاظت در بین رهبران جهان مربوط به علی خامنه‌ای بود، اما نتونستیم اونو حفاظت و پنهان کنیم و از دستش دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67352" target="_blank">📅 21:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67351">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
ترامپ:  از فیفا برای انجام کار درست و جبران یک بی‌عدالتی بزرگ سپاسگزارم!  @News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67351" target="_blank">📅 21:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67350">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPf03fLynPs2rwTPLimE-LcA3uDr0iEd9vJe0X5SB8BHcOU8DCb_QJYQyEx89auRFB2kzMUJx8mWuayYTMfvyVx3ckUVEiZNmroxpnQ2eOaS1la2eCal-FY_8CbklvQsOwHeH-xShAgiby_cNKQOhN86lb2Qz8G_xsKFAMLurmzmWM-pEhy9VPOFtSU-LXvY15820rgnCuB8BRkI1tmvqEA3V3TwQNQQybl6RTkc4BMhPqZhTxei7d1MkTO0OdEcNI0pEQ9GW35jXdRclKPiTenQd-oPVnwDIGXkxD4IwqZRmbeEa0VnTjWwliW2NYnP7RKnTulbekONvG-qHAtypw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ:
از فیفا برای انجام کار درست و جبران یک بی‌عدالتی بزرگ سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67350" target="_blank">📅 21:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67349">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d12e972bb.mp4?token=fF-_EEPTzdyyisPX3BnmhS9o3zmrnOoiFeZn7WK8vB9RfMaCpbeesWPjsesUhdzHfbmluEp0oSUzCqCWfbaKhlZ2_sjFdxPa_JSwPT6TlPUiKhIOqlZZQ79in_IE6e1t4NBCFO4rCA8AysH90qczrSp76coqX28pPySvTKUqVLuJksmI3lWSAmz-DL8dlQhYS9HkK3wRsOHduZ0bQ_VRcTR6NSdJz_JiBx5pEVEDdNeTGbwX5WdvvMBOtQveOQ2pHIwn_0ypAlsqGSc8kic9cP_dGIufGP-a8Miiz5o5XGQFGlMWMyD-3Wx8SCm3xBiqqES14UdemsS1RPwv13efOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d12e972bb.mp4?token=fF-_EEPTzdyyisPX3BnmhS9o3zmrnOoiFeZn7WK8vB9RfMaCpbeesWPjsesUhdzHfbmluEp0oSUzCqCWfbaKhlZ2_sjFdxPa_JSwPT6TlPUiKhIOqlZZQ79in_IE6e1t4NBCFO4rCA8AysH90qczrSp76coqX28pPySvTKUqVLuJksmI3lWSAmz-DL8dlQhYS9HkK3wRsOHduZ0bQ_VRcTR6NSdJz_JiBx5pEVEDdNeTGbwX5WdvvMBOtQveOQ2pHIwn_0ypAlsqGSc8kic9cP_dGIufGP-a8Miiz5o5XGQFGlMWMyD-3Wx8SCm3xBiqqES14UdemsS1RPwv13efOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمد مخبر مشاور علی خامنه‌ای:
قاتلان امام شهید به مرگ طبیعی نخواهند مرد و نظام آنها را به قتل خواهد رساند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67349" target="_blank">📅 20:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67348">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5503b743a2.mp4?token=YLL3iTqLE5EeJkZKywdo5WMNCTtzajUnqIWFpvewhPFBSCE7jaXVaseL8Ql6UdNFfPExW9amGlBeoDUKbFZ5-B1Q1Zml2Tdx6XvmHfPbAHb_OTcVnItdQ4R99PltzEANlPvsHFtUn_KE-Y9BXjKyX4ldgHu5HIodPJLBQYsXREu8meWHmx9ssSNZvD7vRfT1VT6VsHiOaNII5uNbaYuR0ma_KRMTMyXwgPARUecFlXpABXWA1ej9fozfIzEePqxrnRl9bHZ7fRbspj5YshMD-CqfDs3H7U-BHpWJlhlWNIHOKBt_wPJ_wG3PpNE5_Hz_Y0_XdskX1O0f3D8K3rXiMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5503b743a2.mp4?token=YLL3iTqLE5EeJkZKywdo5WMNCTtzajUnqIWFpvewhPFBSCE7jaXVaseL8Ql6UdNFfPExW9amGlBeoDUKbFZ5-B1Q1Zml2Tdx6XvmHfPbAHb_OTcVnItdQ4R99PltzEANlPvsHFtUn_KE-Y9BXjKyX4ldgHu5HIodPJLBQYsXREu8meWHmx9ssSNZvD7vRfT1VT6VsHiOaNII5uNbaYuR0ma_KRMTMyXwgPARUecFlXpABXWA1ej9fozfIzEePqxrnRl9bHZ7fRbspj5YshMD-CqfDs3H7U-BHpWJlhlWNIHOKBt_wPJ_wG3PpNE5_Hz_Y0_XdskX1O0f3D8K3rXiMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
قول میدم راه امام شهید رو ادامه بدم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67348" target="_blank">📅 20:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67345">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PStcpG9vO2mwTqr7kNlijWuR1VaXeagMvH_5nMiOUp5nhnQ6sNHva6ROm2hQBZwSufFsTpLGQt4-0XTxdPQuQgX_6Wsw3M4OEgIpjttImimM5otbpv07PHOwQ5VXHwyZxqOjVM1V7_nbbpG2Ucf8H9SdApIPHEzfnlmNjyCYhU1YZd9mBIObYbxrtdMyoJeXNNP_ltQDMhFfP24D6sYQSIZy-_kG1RUjg0A1n8tFQoJJniJcmYCKPKrjx9CWatRAmmeWyapNg-xrsN3Kq8MF2USjjwGch7jZy38Y-b0QSnaFZD0sTVvS2oDjRKnfNpbNGfMfgcjyHuNNDd46cKEyaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rx1pd5JlhKIJoWbgWQ7VOPuSxiUnCazxHpX2XapyC4mqJGl9lqTGuixG3gJstFKX0xDvhHJX5fkn58MuSNWUuA0i59K1LeEnmAMWFx2mAgm-_EegfPlDHFoMuwlpI4XrHubAISn9IA-YoazXZmM1pbWAmakmmIpD5xwVWCe4YWJX1Kf19jRF45WgmmP8VGwgtSmrv4pznUETSN-2ylT0RoevBSR_9F7U4TrOp6bZcwh_VBi6p3cVPsgeSZx5Kl2nFKlCmLcpzYxNAHnaoxaISxD8LFl-xG58ZNF4Wykv-_kX4B2OlvJ0oxOcJu7giIHOsr7dYV6I_oC2nrEw_xex5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a975887416.mp4?token=R_xp0sziHZ7ModDhX2PHqjr7AkwYPXXdu7iDPg2Nmz6ihZmCBE68Y49vUEDiUSA6ewS8h-8G_H5UM0TQ1F5VjS87qBVMDV3WkXSqjclvo1tt6c01XzKXgmaBdD0KSTxu_31njEuQ5gTG-BgRa9inQgvMj3FeobLF7SC3jfAGTukEo-RpDH0k8Gl0b0PQ0tiGtF0wizkJEmwlHCcL3Ovzelf7KLh6bnVbSxALqdofp1QFFOv_BMH6-gnEMwIxIGbm6IA6rOuwVS3XxBL8FGX1yz9wV3vpVpGXTJwYN-KHLuozh3QvHE2eXT8-BaQ_jN7_LYNlJ8dJVkm0HASgoXhiYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a975887416.mp4?token=R_xp0sziHZ7ModDhX2PHqjr7AkwYPXXdu7iDPg2Nmz6ihZmCBE68Y49vUEDiUSA6ewS8h-8G_H5UM0TQ1F5VjS87qBVMDV3WkXSqjclvo1tt6c01XzKXgmaBdD0KSTxu_31njEuQ5gTG-BgRa9inQgvMj3FeobLF7SC3jfAGTukEo-RpDH0k8Gl0b0PQ0tiGtF0wizkJEmwlHCcL3Ovzelf7KLh6bnVbSxALqdofp1QFFOv_BMH6-gnEMwIxIGbm6IA6rOuwVS3XxBL8FGX1yz9wV3vpVpGXTJwYN-KHLuozh3QvHE2eXT8-BaQ_jN7_LYNlJ8dJVkm0HASgoXhiYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
حملات ارتش اسرائیل به نبطیه الفوقا در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67345" target="_blank">📅 19:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67344">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4c05c580.mp4?token=X8e_ewo7ZJzjxZqk4mvN_wCJd8lnvcRnm0gi6rlm8UzOMb_VgCN35hfR3xM7Z4v81q_fYT0Bkav7O0CwB3OuMsMVLJ_v4coW2xCFgRWwGy6G_sJtS5yqELdtnPHxXaVonwfKMtqb0Dqtz-vh56bvTUx09Maht8rSipId7epOstY8H-h36oYB9uqKYx-RY8PlxEm2O3tuyH8yqg1A_83HpeS3IiJkaTtUIRaBm2KKUyod3o3WE4hYly0gPYHdL-38LDo7bixDmsEI_JZ_TOUudw16q8eaH6WXc7rhmppgW0qh6io-8nDjtu4eDDW3uppxVybouBM-00pA-OQdVNqNVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4c05c580.mp4?token=X8e_ewo7ZJzjxZqk4mvN_wCJd8lnvcRnm0gi6rlm8UzOMb_VgCN35hfR3xM7Z4v81q_fYT0Bkav7O0CwB3OuMsMVLJ_v4coW2xCFgRWwGy6G_sJtS5yqELdtnPHxXaVonwfKMtqb0Dqtz-vh56bvTUx09Maht8rSipId7epOstY8H-h36oYB9uqKYx-RY8PlxEm2O3tuyH8yqg1A_83HpeS3IiJkaTtUIRaBm2KKUyod3o3WE4hYly0gPYHdL-38LDo7bixDmsEI_JZ_TOUudw16q8eaH6WXc7rhmppgW0qh6io-8nDjtu4eDDW3uppxVybouBM-00pA-OQdVNqNVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a4244b191.mp4?token=v257ZSzUD202ERoeIjMirxCpUEbubrv4kpSc9GJSaaV_j9vGrUFJzovSNZNb0h4I0sukJA8rhtMRMZKUTAQf-esgnkDzmG-9AJgEaQvFxFk2yO1prk1aTHbytctr6f04HTXRqt0iJgYcgNUhpYXGMGeLNwOdsu7EuKfsIpYhH3YfmOCkD_QqTAaq78I50rltivFdteS_8f0YksfrpCqJHOf9yY2F_4BoF2qXiF-mOqZLhbRKy26RTghgkUttEkh89s7oTu008rvCpwh6jmqz_qo4rsuF4_H5GJcb7GAVKbHJXW3O_HBNuB-nAW4IPA-kWNHfL1drDP87N3M2QRI8Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a4244b191.mp4?token=v257ZSzUD202ERoeIjMirxCpUEbubrv4kpSc9GJSaaV_j9vGrUFJzovSNZNb0h4I0sukJA8rhtMRMZKUTAQf-esgnkDzmG-9AJgEaQvFxFk2yO1prk1aTHbytctr6f04HTXRqt0iJgYcgNUhpYXGMGeLNwOdsu7EuKfsIpYhH3YfmOCkD_QqTAaq78I50rltivFdteS_8f0YksfrpCqJHOf9yY2F_4BoF2qXiF-mOqZLhbRKy26RTghgkUttEkh89s7oTu008rvCpwh6jmqz_qo4rsuF4_H5GJcb7GAVKbHJXW3O_HBNuB-nAW4IPA-kWNHfL1drDP87N3M2QRI8Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
روستاهای مسیحی در لبنان...
برخی از آن‌ها در واقع درخواست الحاق به اسرائیل را داده‌اند زیرا ما آن‌ها را در برابر حزب‌الله محافظت می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67343" target="_blank">📅 19:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67341">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd048f948.mp4?token=mrfhi-hKN70-aK4YIlX_R3aDCpQm3xQc6kuUAaUAhMrxR0fWj_EpPC-TpdysaJxR1fQ0kYYtJ4o8HvFK2fleS69bz-Bz4Wc7Kq6N7W7j-oY3p29LlPjWy0y9pFpVDW9drEUMOzzCrLL1STOxe1yJr8nvFScGomrkvQxCCai4yBzanNUNGCvP8amCXcIHGx_446iPFu4QrB-9czpf0AALgBLiW8e4bpWSzhjYSPNp6W2FqwZg4-sTONhJIaHRDxlRIt648opdVnO6chebfHIaNpJLtJgCZ8vREByFkhicBYXQALfQDg3obsAJSjFL78NUmkHySwRxjMTtK2Sq1_nOnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd048f948.mp4?token=mrfhi-hKN70-aK4YIlX_R3aDCpQm3xQc6kuUAaUAhMrxR0fWj_EpPC-TpdysaJxR1fQ0kYYtJ4o8HvFK2fleS69bz-Bz4Wc7Kq6N7W7j-oY3p29LlPjWy0y9pFpVDW9drEUMOzzCrLL1STOxe1yJr8nvFScGomrkvQxCCai4yBzanNUNGCvP8amCXcIHGx_446iPFu4QrB-9czpf0AALgBLiW8e4bpWSzhjYSPNp6W2FqwZg4-sTONhJIaHRDxlRIt648opdVnO6chebfHIaNpJLtJgCZ8vREByFkhicBYXQALfQDg3obsAJSjFL78NUmkHySwRxjMTtK2Sq1_nOnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار تسنیم : نظرتون درباره رهبری مجتبی چیه؟
🔴
زن عرزشی : چی بگم؟! نمی‌دونم ما که همه منتظر بودیم مجتبی حداقل برای تشییع جنازه پدرش بیاد و حضوری باهامون صحبت کنه، ولی بازم نیومد!
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67341" target="_blank">📅 18:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67340">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c05464482.mp4?token=h2ZfVtDYojyZwqBGZGIEPhWWyjed_3rnkT7w9CSR_p46qeEFaaxaSnac05Y5NmmGba0s6X-IUTakR3PvQFUS6MjNHPweRZQfapL2w6T8B_RJgt1Z3T-0JxqvIpyLwOBfdCLgdhA2leJo53Wz5ZRLCMseFb4qZlCbygDb2E2wUAMTUoVFSKGEYIcSqDQVqUz4IBrXCB_RsWL1M_axwcruGTwqnGnhclJFWicLMeFR9d0asqt41LjTRIyOF2v3cLwC6u6Tf5cga7J-YdPz2VE0rAOSL2Izd6kjbY4Acg3xAT42amjHBlKukgoEdCnbz2e5DG8pv70y6Yn1VJUhuHm0bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c05464482.mp4?token=h2ZfVtDYojyZwqBGZGIEPhWWyjed_3rnkT7w9CSR_p46qeEFaaxaSnac05Y5NmmGba0s6X-IUTakR3PvQFUS6MjNHPweRZQfapL2w6T8B_RJgt1Z3T-0JxqvIpyLwOBfdCLgdhA2leJo53Wz5ZRLCMseFb4qZlCbygDb2E2wUAMTUoVFSKGEYIcSqDQVqUz4IBrXCB_RsWL1M_axwcruGTwqnGnhclJFWicLMeFR9d0asqt41LjTRIyOF2v3cLwC6u6Tf5cga7J-YdPz2VE0rAOSL2Izd6kjbY4Acg3xAT42amjHBlKukgoEdCnbz2e5DG8pv70y6Yn1VJUhuHm0bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زینب سلیمانی:
شهادت آقا برای ما سنگین‌تر از شهادت حاج قاسم بود
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67340" target="_blank">📅 18:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67339">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYI-1hUSOTyQokexZXdD6m_XrMYaj8P2o44XrmF8qMzeaC4ANgyfP8YSf6Podq-L9325NbfDcaSzhV5W8FqLeP0pDD1tzLaudb7pWXsybyUUf0Pp8ejeHUb2WhGVr_2aRcvIIKC2FmtXwG6ImMHy9wdeUxiLKF18iu_9-LC0Pfk239-u4PeNsj9crU-bprhtJaY5mE-Jl6UXrIgEtnXV0-XAoMZOM4MRtAZe--Q19i1dn6dBJAi9QAO5pfNfka6VNkz6P0FwUNugbKQSc7NiXREQBj2jIgTxohFUygcUe0DV8EuAxpTFEhOp1cc1m16cMMWfObI0SwPy47MMk7cyrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d7e9ec8c8.mp4?token=TJ24SSUyCA3OcTFFxoXd4qWnfSSzyW_7QVyI8-kS4J2EZVH1twDMHItRAtPj1z2D6CXZ3-uFW2RXjM91MQOtOu56Oj99Y_0gXWKoAB6QK5Ev6NCKMFN2fmc5tmUEU-DP0VS4a5XaBOAJatZbH1PFD790p0LefSDeOJ0E18kxOxp2UsmkQi19ZMs7yFGoCzYV6tjDvrukih0eW9fGtGQe5v5k64QCsGOL8w7ho89IvQSqk-r-JwhhBkcnc_9aCWbTLZkebwWFbkR40byUpxe2JD76N-u4qXX97ksloxRmdobTwGyhFSGwVGJf9mvA-zU27dzFYwqv8QFiJNZDOKB05g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d7e9ec8c8.mp4?token=TJ24SSUyCA3OcTFFxoXd4qWnfSSzyW_7QVyI8-kS4J2EZVH1twDMHItRAtPj1z2D6CXZ3-uFW2RXjM91MQOtOu56Oj99Y_0gXWKoAB6QK5Ev6NCKMFN2fmc5tmUEU-DP0VS4a5XaBOAJatZbH1PFD790p0LefSDeOJ0E18kxOxp2UsmkQi19ZMs7yFGoCzYV6tjDvrukih0eW9fGtGQe5v5k64QCsGOL8w7ho89IvQSqk-r-JwhhBkcnc_9aCWbTLZkebwWFbkR40byUpxe2JD76N-u4qXX97ksloxRmdobTwGyhFSGwVGJf9mvA-zU27dzFYwqv8QFiJNZDOKB05g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بزرگترین آتش بازی تاریخ آمریکا در واشنگتن دی سی به مناسبت ۴ جولای روز استقلال آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67338" target="_blank">📅 17:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67337">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ap9JORVmieQJ6q_xGGULOZbq5tj0vOlMFZtykvMe2Tm2n4Scso383x2yayvAyJPPKF9yLfnaWgf4eMFG90MWMhtB5rd5-gh4tcM4YW0uuPgucG7eo0kdioFtwUKehh2MOWc0kbN8Rndsux5NzieJvpT_08yrxR87qPQSivcnRvfLQotVR6q03-FX51V-rMRrPV9rY10SnxI11qglF04hwiAjvAn4KXahwwu3DWklpPpJYUlU16Sji2fFskCsshQPAoMyMi3fqoBclb9iB4Cemhkgkzf4h4vNB2hacYWGqY1m6TUK4AM13HBfv-6uEC5ZjDImbpujl1mvdvA2CWB7Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❌
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
تنها دلیلی که ما امروز تشییع جنازه خامنه‌ای را بمباران نکردیم آن است که 10 هزار مأمور موساد در میان آنان داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67337" target="_blank">📅 16:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67336">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e644784ac.mp4?token=SOj7UxrAnymq7P2mVyt-VRfp4wp8UC3nvHozeStZECQvfrPPehci91cqnKnmQCP3tm0Z8x2ltCFV0zXk_Vqvm01mW0fUyeifzuPgdG_Cut9sgvP17pwAKeL0gJHbWPjGitNU7DZnpdnTl-7S32_LbkwfX4_yskgVM9aSVXPSZd2pGf18E0hUMK5tXsdX6fNhtv8uFHWqhu_vITAgYTJhua7rbv2uybn0xrQzZV69sV1BbzWgNtdW3-qiBI7q0uUcXinDYkbV8X9Tc3clXKIPWtGqrWo__xmfMmYBOvwDEpeJVfBQGip6bC5ZFN0Fd5ZiIX0JiqMehxO8qHeu2qmaMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e644784ac.mp4?token=SOj7UxrAnymq7P2mVyt-VRfp4wp8UC3nvHozeStZECQvfrPPehci91cqnKnmQCP3tm0Z8x2ltCFV0zXk_Vqvm01mW0fUyeifzuPgdG_Cut9sgvP17pwAKeL0gJHbWPjGitNU7DZnpdnTl-7S32_LbkwfX4_yskgVM9aSVXPSZd2pGf18E0hUMK5tXsdX6fNhtv8uFHWqhu_vITAgYTJhua7rbv2uybn0xrQzZV69sV1BbzWgNtdW3-qiBI7q0uUcXinDYkbV8X9Tc3clXKIPWtGqrWo__xmfMmYBOvwDEpeJVfBQGip6bC5ZFN0Fd5ZiIX0JiqMehxO8qHeu2qmaMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اگه اهل دعواهای خیابونی هستی، این ویدیو از استاد طِقه زنی رو تا آخر ببین تا به امید خدا پیروز میدان نبرد بشی؛
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67336" target="_blank">📅 16:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67335">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67334" target="_blank">📅 16:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67333">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnB6RkWHa2ldYTzX5CEZA0vzDB1tusjqS2i1JWyX6uutwWPoTd3ywBKaynLZGQw-nNshYNugsusTTBC-u_W8rodX6-KwDaxGxLr6LsMDq4B94uE_k0oNpFghc7kR9w8rnfKtjSXOxEKobsYn69rSHMpARFOANZ3xghCXF-1X5XMT-pw37osygXt5ZJdVs89zDY4KUJgr4pWE4JJFgYpb2syyPxDQLB1tP5YoWDJIzzB1su9CFUxoEGcnUgbXJn3pOG4uU08JwJjzyZKwVMBZRtz80mSMxpIHVL2Dc0pvgmvJjmnZy0ZrCBj1cuUQqiENMsB5denU9jaGYPp0kqCnEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گویا کامیون حمل جنازه علی خامنه‌ای مبلغ2,298,000 هزار تومان خلافی داره
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67333" target="_blank">📅 16:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67332">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzdXLNmHPkQoQgEMcKnaN6r4Tb-9W2XwqhLWPBT1Nn7_JRxf3OO6r2iwR1D8KFCGy7VCaRn5df6PjLv9ZjnY9TKmPBDaBKK8DT0zpsR1ZFb2u0bAKtwotzVkogggWFu9v4PjeFzdQpP5WZo6krw8L3ZNhvIh1UbbRDQZYqTGUTingpHZ9VePq4JTG5-Hx2QdWESEtpyjMOhubqQ98W546CCX3M-hjhhm1O7-u-Dh2cdw6JOmQzMDunrSLpWHYdqyKehA5IoRs8N2zzb8-iYVSRpRpOVXNssNKcAnkFB5U6-NREVS_VGxwJon4qPMQbVfMS65eWCzOs7MhBQn0u4L3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
محمد اکرمی‌نیا سخنگوی ارتش:
«هرگونه اشتباهی از سوی دشمن، با پاسخ قاطع نیروهای مسلح ایران مواجه خواهد شد. ما بارها اعلام کرده‌ایم که از فرصت آتش‌بس برای ارتقای توانمندی‌های رزمی خود بهره می‌بریم. ما حتی یک لحظه را هم هدر نمی‌دهیم و تمرکز خود را از این مأموریت برنمی‌داریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67332" target="_blank">📅 15:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67331">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو در جلسه دولت:
شنیدم در رسانه‌ها گفته شده که رئیس‌جمهور ترامپ خواسته علیه تونل‌های تروریستی در لبنان اقدامی انجام نشود. این یک افسانه و خبر جعلی است.
او حتی یک کلمه هم در این باره به من نگفت و من هم از او چیزی نپرسیدم. ما بر اساس ملاحظات و تصمیمات خودمان عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67331" target="_blank">📅 15:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67330">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHl_76IWCL3gSgPGc7nE2lwuU62Q92mhNOwxzt3IUYKxomWAE37DVNLmSlhNhqRIMAPodXh2-XtRwwiGAOY0p5CN8WrcQOxb-aHyuZGLApz8jQ-WGIB6qVLTrPmMTAsmYfOv-rkZP2s7gKXvNqjuyiczo3d1Vfuw8JEAjBmeUiFD8S-Q8VDPPvTPC99h3gtxh4wdkLapd1TU2BE-OJ_CbevpAkhIRW32OnXWn0FXrasob6CUpjZ5YbBlbmBtXGMk-mG0ZPSao1-Z2Ri-Z0bvxincEJ6uFv8cGDA8aVr4J_eYLvtAEee8TSLMcowSix1v2AnwgbYhLIgYXJGs6qZwhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویر ترامپ در مراسم وداع با جنازه علی خامنه‌ای که روش نوشته شده:
خواهیم دید چه می شود
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67330" target="_blank">📅 14:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67329">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKCeTb5oCjN1v2wV9TKzEh0BD_WMNS2_jA8dFgPqmWsC0oeqgZkdsfFHaSdZfIsGlViZmI_mVOIdEKbaL_KG6f_bwDFJjtetDrFWEAHw0GzBIdb6e7W0I4eMzoU2chqXCwItpQghwT90MEts-Dfl5sW6b--6n5CTU2wFBR1HBWZN4I6eAP7F77BrUMzQQHiySpDdAebhSqKGUfLQeT5SGelEqKAj-9C__tjWxWWJ-ygKxml8z_hlnEznbIMWo-lbp69QQHqhoR8HgHwDv2R-hBiXb6brertrW-RN0QJ_QxhOJ6-VG9tynW-OQuMciElEvPG-F8ew1s9_wyOY-ROYdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسرائیل به فارسی:
بهرام که گور میگرفتی همه عمر
دیدی که چگونه گور بهرام گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67329" target="_blank">📅 14:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67328">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b8ead8806.mp4?token=pgyBOow77QkO8zJ9mRD2BKq-i2SW4TqESCl99NgE9umXKUqQEnbbXD2F5RsqN7eCo5bPYPr_PZoP0UHW1SilKHXjepNcyRZnNRZa_pIEHNvkGY4a4p2fVuf7K5-8WWWK_qSliZQR2olYbaIC3r5eykpmXUJLakD3fdYnE9cFj5rVM_eOm68ut1U2wGXvhmbZ50Yq5zEZWddrVv3yJSquvG14yMJ6eF-J5VvUkDTtjLAe4E7YuytFfxqk0S7lF8s5RvRc17EYgHaLEnjf6q6yI-ZZfEsf_UDaLGKrU4Pt6WReODHxfT3E4d1F5PLmEBTMs7FWYNKELhJrmpQnbgILIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b8ead8806.mp4?token=pgyBOow77QkO8zJ9mRD2BKq-i2SW4TqESCl99NgE9umXKUqQEnbbXD2F5RsqN7eCo5bPYPr_PZoP0UHW1SilKHXjepNcyRZnNRZa_pIEHNvkGY4a4p2fVuf7K5-8WWWK_qSliZQR2olYbaIC3r5eykpmXUJLakD3fdYnE9cFj5rVM_eOm68ut1U2wGXvhmbZ50Yq5zEZWddrVv3yJSquvG14yMJ6eF-J5VvUkDTtjLAe4E7YuytFfxqk0S7lF8s5RvRc17EYgHaLEnjf6q6yI-ZZfEsf_UDaLGKrU4Pt6WReODHxfT3E4d1F5PLmEBTMs7FWYNKELhJrmpQnbgILIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این بزرگوار که قبلا گفته بود بخاطر یه تیکه نون به سگ دادم اومده داره ترامپو تهدید میکنه میگه بیا کوت عبدالله ببین چیکارت میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67328" target="_blank">📅 13:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67327">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
❌
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
تنها دلیلی که ما امروز تشییع جنازه خامنه‌ای را بمباران نکردیم آن است که 10 هزار مأمور موساد در میان آنان داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67327" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67326">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0be756a04.mp4?token=dukNQ-UknZql-F4ZWdre7WmiGdctVPEq59joJWFHgvXFJNWwPeMh6EwgB2YEJoSGAZ0NMbf2-2JOCGwYctXgeXmbALNBwe7AZFBziLALU8azWioMHDQAPya_HhC0Spg154ndxkMPsPpDbW8dM9m9CFpgTdvKoc63YwyQ7T6eQiOCZ_ZsN1X94tIE21fFRZndkTciFfuJJpWgwnuRPiAnmcqiP2MIWzST54C89lBNTnLqetr_C5BRBuiTKLLVDI4JRArwqjj_Hogj9feoYRMfbeyHTwoUofNH5qPZ81Oxc4_F_t3oTaNTGu2RtX4OVA_Izlez6L6OtSvhLuvbZQCn6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0be756a04.mp4?token=dukNQ-UknZql-F4ZWdre7WmiGdctVPEq59joJWFHgvXFJNWwPeMh6EwgB2YEJoSGAZ0NMbf2-2JOCGwYctXgeXmbALNBwe7AZFBziLALU8azWioMHDQAPya_HhC0Spg154ndxkMPsPpDbW8dM9m9CFpgTdvKoc63YwyQ7T6eQiOCZ_ZsN1X94tIE21fFRZndkTciFfuJJpWgwnuRPiAnmcqiP2MIWzST54C89lBNTnLqetr_C5BRBuiTKLLVDI4JRArwqjj_Hogj9feoYRMfbeyHTwoUofNH5qPZ81Oxc4_F_t3oTaNTGu2RtX4OVA_Izlez6L6OtSvhLuvbZQCn6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جمهوری اسلامی پس از ۴۷ سال در مهم‌ترین رژه‌ی خود حتی به‌اندازه‌ی بند پوتین‌های ارتش شاهنشاهی هم نظم نداشت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67326" target="_blank">📅 12:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67325">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCUpXbYgTelhfkLK9ndjxqTlxGk9xlj9DujvH7i6GrtcpMee2uq7lqUt2tIU8ocXt2QumbMUP07z68vtzfyeWBqFEWmgH9qJi5Yhny4lMyn00XsFklb9JAip7jfHWjx0maUT2l-Noxb-inMAeRwttbUmGKVXPQjV7zGVQkJa6Y3dhROAQbOs6BtSR6_XUzslzwu_5R0ftJzR3UZ-xfUE6bNsxvT3w4imNfCBJdCSU4V3vy4PwI_hyWQz-lQWRZKb4DODhUEjN7Astw2Y6OIdsbbaNBnXnV763FIbvWBAF3d8RS7uv4dXav1nQyZBi0x9I7M6n8RZkCTCfuSptgzHJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0YQHRmNIcdGGQKDE6EZLdHL8JFeRoRMEg6z_iPKWbJsv2-U19uS2ID19x5fzoWbIsk06akH9IFbijzuWlOkCBvZ14lKdkPJr9yi3pHvbgsfnA7uwDZMRcJ9ESl1WyAn_QUSDHIui4QXgVH9mXQVnn6v0BA__39NkMOB-pT9aJz1262WGt-TMfZ3sHpnKUp33hHc0lGcI8YDrQbWFinHtUvX1m3mq3IA2vbfzOHuQzbkp6qxjux2Pj5CaPFxiIepV0GJNpW3WTB13SH1pvotxDxdqdaa-4HajEbK9-wndjJXQGFHN71Vp9GL8kbADRr7vcmGUfWBl4VQC4DZZI97aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f22dc07ca.mp4?token=h8kU2iX8m09o-ITwSzK-sf0KNTrArarrIo5CaumVtCIlV7DvZzgb9sj0dCqYndkFw-5UPzPexI-7OE5h3angRtpWWZl8OD35JKfyGyPs0EILmJ6HWtGBrYnd2Y9xM2txBtZtqio1val72LQYl81JqW5l0tRLtOxvihImW-uwWjTPa3vKqXdQS3f1t8pbkxl6hTc1xV8b8PXVa6qITc9OtS4SVBC3q-c9E5fNbDl_-TqYY1bopbh2AwRx31b2NOywwKf-ATlSmo1n8moXaoF6xJRuemGTCovKYgpFiKDy5JtnAoEY90PDY28NMbFlni1qrLhMkHH7cyWbZb7ubARbvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f22dc07ca.mp4?token=h8kU2iX8m09o-ITwSzK-sf0KNTrArarrIo5CaumVtCIlV7DvZzgb9sj0dCqYndkFw-5UPzPexI-7OE5h3angRtpWWZl8OD35JKfyGyPs0EILmJ6HWtGBrYnd2Y9xM2txBtZtqio1val72LQYl81JqW5l0tRLtOxvihImW-uwWjTPa3vKqXdQS3f1t8pbkxl6hTc1xV8b8PXVa6qITc9OtS4SVBC3q-c9E5fNbDl_-TqYY1bopbh2AwRx31b2NOywwKf-ATlSmo1n8moXaoF6xJRuemGTCovKYgpFiKDy5JtnAoEY90PDY28NMbFlni1qrLhMkHH7cyWbZb7ubARbvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
و بعد از چهار ماه همچنان عامل این جنایت و قاتل فرزندان ایران چال نشده و اجازه چال کردنش رو از قاتلش گرفتن!
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67323" target="_blank">📅 11:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67322">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5f6d58549.mp4?token=YMYtp9o0V9E7j6VccMqJt2UoVSLBSerSXgh6bW3DZIRJr_NqToiFHdUYVu-NlYFFv8DOuZG3CezHyYavcnwAac6XDyGnhAxTGote7VUQUtpSaLxjYRmgwi8JiA68wKBwayhYHTqKeI3ZCDc2qizapcm1TgMiL7fyVgwhBpiItKXuJnvDRVm35gCe50dezrbU26XSMHHVqNrHmlO1y5UKiPb4zgBM2sPzpTQYgQrs29QAhBRAUI08BrtBGVdqPrjLLz7-KD5H2PqAW52oMM1FQVP05yzw3sl4mNDVBiB3S6WAS3EpPgkjWDoPpwwvZupMC0Zsnt-KUK-mvGqUoJpn7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5f6d58549.mp4?token=YMYtp9o0V9E7j6VccMqJt2UoVSLBSerSXgh6bW3DZIRJr_NqToiFHdUYVu-NlYFFv8DOuZG3CezHyYavcnwAac6XDyGnhAxTGote7VUQUtpSaLxjYRmgwi8JiA68wKBwayhYHTqKeI3ZCDc2qizapcm1TgMiL7fyVgwhBpiItKXuJnvDRVm35gCe50dezrbU26XSMHHVqNrHmlO1y5UKiPb4zgBM2sPzpTQYgQrs29QAhBRAUI08BrtBGVdqPrjLLz7-KD5H2PqAW52oMM1FQVP05yzw3sl4mNDVBiB3S6WAS3EpPgkjWDoPpwwvZupMC0Zsnt-KUK-mvGqUoJpn7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی رسولی  مداح بیت رهبری میگه برای خون‌خواهی اومدیم؛
شما هنوز خونخواهی سلیمانی و... رو نگرفتید بعد میخواید اینو بگیرید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67322" target="_blank">📅 11:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67321">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5807c7f54.mp4?token=DYHLWbsTlYG7t99N50Jk5zf4-gXmRazP_iiVpYB-1wt9aKYf2NV-BKWVjFnB_nA0YKiDRqfDHbqhXjsW0UruD7IM0kcy9hIANWYr7XnnQen8Q56dwEp4x2NpVB7vApillaiZrkQrlaRkSEuRh2w6a6c0SFZgIFwHE_xDvr9AQStZS4PeUnH8XHcX0Mnf3lC8WheyFctt8OsbNPhFBlvigY2tAAlxtN8P_ulXfcKgYHn9NRqeE4ESxzedOpFJkrWOwt9QnvcZiidjym0klJchV9v4Z70dsZBHrn1nNiRP10eCPBJq3FWKTazJIrDGAlQ9VRK-ovRcQDJR2epKEKzpBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5807c7f54.mp4?token=DYHLWbsTlYG7t99N50Jk5zf4-gXmRazP_iiVpYB-1wt9aKYf2NV-BKWVjFnB_nA0YKiDRqfDHbqhXjsW0UruD7IM0kcy9hIANWYr7XnnQen8Q56dwEp4x2NpVB7vApillaiZrkQrlaRkSEuRh2w6a6c0SFZgIFwHE_xDvr9AQStZS4PeUnH8XHcX0Mnf3lC8WheyFctt8OsbNPhFBlvigY2tAAlxtN8P_ulXfcKgYHn9NRqeE4ESxzedOpFJkrWOwt9QnvcZiidjym0klJchV9v4Z70dsZBHrn1nNiRP10eCPBJq3FWKTazJIrDGAlQ9VRK-ovRcQDJR2epKEKzpBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف یه 20-30 سالی هست درحال گریه کردنه
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67321" target="_blank">📅 10:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67320">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/810ada8a67.mp4?token=OotSekjeWVmWyVDtvnPcxArEgZvX57is668KXtl1igrLpkDPHwmu_MxmTY0a_C_GpmVlL3JPBf5ObRnuhjrsNYOst0NMoQiSaQVsDxj4lpv96UmZKo5yA_BZyE_1wO0r1OzBhGqmOaKyIjoCaWt7matwglUElPc9ZfMm-6tt86vps82kxoVY6aHqWlWl5hjzqeouXen0hfph7Api60Hd1KWNs453dKiMAco-smhV5pODhHdfX392E3YZLPbgdgTmUJPBaP2bem1ByLAnuY02N77f-XsJgMbzA379t5fY3lLEH_5Xdbg0SGweX2llQOoxWx1uIFu_47sjMb5Yh5f_qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/810ada8a67.mp4?token=OotSekjeWVmWyVDtvnPcxArEgZvX57is668KXtl1igrLpkDPHwmu_MxmTY0a_C_GpmVlL3JPBf5ObRnuhjrsNYOst0NMoQiSaQVsDxj4lpv96UmZKo5yA_BZyE_1wO0r1OzBhGqmOaKyIjoCaWt7matwglUElPc9ZfMm-6tt86vps82kxoVY6aHqWlWl5hjzqeouXen0hfph7Api60Hd1KWNs453dKiMAco-smhV5pODhHdfX392E3YZLPbgdgTmUJPBaP2bem1ByLAnuY02N77f-XsJgMbzA379t5fY3lLEH_5Xdbg0SGweX2llQOoxWx1uIFu_47sjMb5Yh5f_qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در جریان مراسم افتتاحیه مسابقات «فولسوم پرو رودئو» در ایالت کالیفرنیای آمریکا، یک چترباز پس از آنکه پرچم همراهش به درختی گیر کرد، تعادل خود را از دست داد و به شکل خطرناکی روی یک چادر سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67320" target="_blank">📅 10:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67319">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ca0cec0e0.mp4?token=pNdguG0uDP13TEhZtJz8wgqbn0SCzVtIVf75YpW7WZXS-yMA3a2rWCk4NTkh2qe7sTS2pHwyaV3dtTuI1sJp7w3o8KmU-8gzBCDyWRLOtQnVSJyvE6k4VEoDvWdC6foL4uOSLdGic9dDObO8TccDoVGjnX7GfIoph36XMUqxvu8ypPbcC09R6fQ9gRRPwmm58jBfSR0lCuRAAvS-mw2F12TS4vK75VwP_sYiiJ3L-rd4KntVyHO50u9wAnts4Oea1weqbMYXpcFzur9jkFvaqCqPxwx0XtSmrSxapmzPxeAaXpFV2iWsUcuOvPvcY8HQDVtMWwlKBqmBeu6MEEwVBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ca0cec0e0.mp4?token=pNdguG0uDP13TEhZtJz8wgqbn0SCzVtIVf75YpW7WZXS-yMA3a2rWCk4NTkh2qe7sTS2pHwyaV3dtTuI1sJp7w3o8KmU-8gzBCDyWRLOtQnVSJyvE6k4VEoDvWdC6foL4uOSLdGic9dDObO8TccDoVGjnX7GfIoph36XMUqxvu8ypPbcC09R6fQ9gRRPwmm58jBfSR0lCuRAAvS-mw2F12TS4vK75VwP_sYiiJ3L-rd4KntVyHO50u9wAnts4Oea1weqbMYXpcFzur9jkFvaqCqPxwx0XtSmrSxapmzPxeAaXpFV2iWsUcuOvPvcY8HQDVtMWwlKBqmBeu6MEEwVBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین حضور عمومی مصطفی، میثم و مسعود، سه پسر علی خامنه‌ای، در مراسم تشییع او در مصلای تهران.
مجتبی خامنه‌ای، جانشین علی خامنه‌ای، اما همچنان در انظار عمومی ظاهر نشده و در این مراسم غایب بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67319" target="_blank">📅 09:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67318">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd6157bafc.mp4?token=aKqL_WofyvK3NmA6MF8FrHEvkyD7GstF95KHn66jp3YJ4xS6cIEWKI0PdsSCV51L0H4_fwcgiPNkX9VV_dIH2nrkx9YDFKeGjp8AY3qdtdQcslaiGv4w9nQJMcYRxf7XOTX3-WtSZ6LACFTfxaRMSsS0YYcT6pckrZcGZ5XJTcLCeoy2b3_PPbfYNzEu_7QZnAnDD93lWOvUZ8P8bm4wdDNjC2xfeNvzaMZQHLl3snsgZRj9iWSeOEza30xxRubtnmFHDZIczZMELkF67Uir0hn3xw8xN29kS-O1YGhPEz04efbFq2NM1qXRTj-_F10A6apRvcwIg1-jW4Z7Of5G-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd6157bafc.mp4?token=aKqL_WofyvK3NmA6MF8FrHEvkyD7GstF95KHn66jp3YJ4xS6cIEWKI0PdsSCV51L0H4_fwcgiPNkX9VV_dIH2nrkx9YDFKeGjp8AY3qdtdQcslaiGv4w9nQJMcYRxf7XOTX3-WtSZ6LACFTfxaRMSsS0YYcT6pckrZcGZ5XJTcLCeoy2b3_PPbfYNzEu_7QZnAnDD93lWOvUZ8P8bm4wdDNjC2xfeNvzaMZQHLl3snsgZRj9iWSeOEza30xxRubtnmFHDZIczZMELkF67Uir0hn3xw8xN29kS-O1YGhPEz04efbFq2NM1qXRTj-_F10A6apRvcwIg1-jW4Z7Of5G-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زاکانی و برخی از مسئولین تو حاشیه مراسم رفتن چلوکباب خوردن، عرزشیا هم اون بیرون زیر آفتاب، صف وایسادن تا تخم مرغ آب پز بخورن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67318" target="_blank">📅 09:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67317">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUd5aNAJdBRfRTjfHXh2aYsGbtvK9vtytGNUFO4OOgrA-pivTA7MQpB64xwZnT0p8nlwwPYoRRRX-k9xxFvhmPPewQChvBiJeGRFV2fd6MLighNmKvRzVYygqjY9e1EWpV05ConqRsmg9Sr489H_2r9bVYr9sQReAqPPu1Gci5zW8rnywNoCMS3EHOOUem-RSqZSWlnEZzMhxH_eCbMs8ZeFE7u7gMqYRFLJqoHLukMNzz0mI7d9TJ7sI-du4UKzej819MLOblvzP1N3p5uNUoXeRLVUSXcFK-80qUkEyzv1UdPyY0mly22eiNkeA8GdI69ickcpTP9zqhqbKTytFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
8فروند جنگنده A-10 Warthog در پایگاه هوایی موفق سلطی اردن مستقر شده‌اند.
🔴
این جنگنده ها برای پشتیبانی عملیات زمینی استفاده میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67317" target="_blank">📅 09:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67316">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67316" target="_blank">📅 02:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67315">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kiWOGg-bN2wLPozGAFnTUIpNmkvxxP_kieyRJW-CZ6I3apCQy8n7h2VVLaR8qUvdDimnO_QH80_6u-KGPYvsG8vGt3DouZl6AXLApAeehq951BHFoj9MYBY0bkGLPxcuiEWVjIogXUfHMKgJaC5qI2sEqccMvZ_2OjsBXwmx4_nJNlSdzPTBh5uXZpZ9WouF0hp5UaGAAwPot4etkoZ06-QB4rM44qRixXU4JXPMkz_bUJUpMyjfU8LmLP28whoObX7LHA2mEwnzgM2CmV5N9BCC5wmJAtj_uyVTNjgw5svwSUbvJeG49GSZsCPR0DAE3PEDMwzeTNkn1fu6r-AjzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67315" target="_blank">📅 02:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67314">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l23hAfZaId0Vk5ifp9nyNudA4Ub7BCJ8Z5vhalNlr0Hyx-117k1wX_R-4uH9kvE1OJ04ezbI0L4PhCpb3mEZc2pGsCc6Ur63IOxu9_U_YdWNly6IXGq_xlyyHJ6bvtEs_06zfW1recNGny1ivocljwxzZiYp2ba_W1eBHeb4lwl9dyvJVegiEVjM2af8LaQ9Uf5QTB8zuFCs4iZpaR0kuo35N1j7vBqXsrqfHqOe8Oep7VnFzIU1Sop-Uqbt1VwNESCMBZ1-9zWaB_PPkmILUwis3QhBBrs-Mi3zBq20j2iu3cIoqGcLobLMk5aU0_GpS8hOPHv1eqVOM8NKEYrTRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
ولادیمیر پوتین، رئیس‌جمهور روسیه، با دونالد ترامپ تماس گرفت و دویست و پنجاهمین سالگرد استقلال ایالات متحده را به او تبریک گفت. کرملین اعلام کرد که این گفتگو یک ساعت و نیم به طول انجامید. پوتین از ترامپ برای سفر به روسیه دعوت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67314" target="_blank">📅 02:06 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

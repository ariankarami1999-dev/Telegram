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
<img src="https://cdn4.telesco.pe/file/QxbYo3GoczwfkbD4gZCtl2dWB-8RKPGH2FS8rVQCuKwt_rUNNbW1NTvXSTiY5mTklEQYzeT7G5xKIVXkL26Iy92Iu9mX080k4QXMJ2S01vBcub4f1fDE-igTunWPn4Wf8SZK3_hgbivtL8GLVQltLzold68MOxNLGJkvuavRBzpfm11IYv_9Hh15DFF6BbOiRmbXJyrn3lWUgGWKQgOSC3CmTt1V-MhK8-h4AwgZJpbonB7k2NXAAnBmvveUI6Rp3wmOwxtKBCIhx6qT0kTkJdWNwfesMgxMHNtVvbeNglN-EAzDuokdeiF1LC_swcmYBBSCNbS6GZAwbBaOgMaECw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.5M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 21:43:22</div>
<hr>

<div class="tg-post" id="msg-660213">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">روضه</div>
  <div class="tg-doc-extra">حسن خلج قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/660213" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">پک هیئت قرار  ویژه شب دوم محرم
🖤
#محرم
محتوای مذهبی ویژه محرم در این کانال
👇🏻
👇🏻
@Heyate_gharar</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/akhbarefori/660213" target="_blank">📅 21:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660212">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
برخی منابع نزدیک به تیم مذاکره‌کننده ایران، ادعاهای شبکه خبری العربیه در خصوص متن یادداشت تفاهم ایران و آمریکا را تکذیب کردند
🔹
العربیه پیش از این نیز گزارش‌های نادرستی در خصوص مسائل مرتبط با ایران منتشر کرده است./فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/akhbarefori/660212" target="_blank">📅 21:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660211">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
ادامه اختلال‌ در ۴ بانک؛ وعده حل مشکل در سریع‌ترین زمان ممکن
🔹
شورای هماهنگی بانک‌ها بار دیگر با انتشار بیانیه‌ای از مشتریان چهار بانک ملی، صادرات، تجارت و توسعه صادرات عذرخواهی کرد و به آن‌ها وعده داد که در سریع‌ترین زمان ممکن، اختلال‌های موجود در این چهار…</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/akhbarefori/660211" target="_blank">📅 21:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660207">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hua77jGuq6_sJ7kJx6iaJPXTDzledHWL9zwbAt9aLY78kfDan2UxkJAZveYOJSYnV52d2YMfA6fhTtnSf3VFYhsMr08v-ZCLQH-zHrOWUWBmSfEMUt15j_mL430fuz_fFEWlXgr6MSs_Y02lkEtQB6ZGTI7yPp3gybs8fMIxUGbItnRA5zcQ8itN9vP-2X6XYc_x-0Xqg8BGuUJlBu70z4_28y3IGae6S_3C0sRrWzXFq7cwIVCB6WnMEKuaEDNHcwjRlYA8OPbeOjiD0Y3xsHnAbOrJg811douG2yp8tYkKoqVjHWull6OtAesG_3Lb6ZW77tTfQrWLgoW-s8WHGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CdfFwLcbdt6mqZdKiAOZA1dfP-pgsMznKrE8l1U44qaGm5I82OwqJEj7cRqvZrpwrlrHm99M3O-Ceia_tzWZ4zq-udZhilDCO6fUVoLnrtXIL9oI5HHK09lV3Istv1S8fHdIsHOxx9HJ2FyqltZ75hyKzsvA5hk5YHfhJbeMgbsKhXJZM5AJWRkFJ_sCekeEXFXoGylkS2sVDXaqYOUMwuHNUCg6t90A3Z16W5PRnMbA6NWzmpOBgY_CI8hjjEgd_mLL-og5Q3V0q7YeO-QHwZERP3co5VWCYns4pN4CA-CBMqpAlrAv_eIhXdX7QUlQgd9tvmBzSzSX_OOG26CsDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xf-YpJNyN9fpDfnuUW4RmuZmaE-WacjRnMf5ejxE9p9zvw-1dS5KmgvSuMz_8gT0EOP2d_JnvV9-T-NLnz6oTgNzM5mlYlxDBMlPapy67wlB14T_Yr2zVffCsRuHbYRPVtCBzftyDk6tY94Rfa1-M4wTn_T6zV-Uf8pibn6D5NtG7VYgpR5iI6BwYKfVPHVU_V7noKD1SLlAGqo6J24gUFomwSU2QyeMQWCUuix_WbzXKCquIIOBOzP-D2ItYIorDZFfe6NtwRT-Pp99ziAQFjVAfFRNYUCAFChfMZ_0g2pos7lE91Cfs9gk-TfZ4lX5UzTouT2Wxi38WkeGPoYapw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iE0fd4y1UMBxMkotrS8JlgmzTKT7xZds1hlLg63VtiZ5ajHDyacGvxE4yNIZIHOJqON9xKSXqykbe2sH_ZJcrffqlmrtOcoJ8vrnuwdizVUVYRUO07Nuqh7x6R5TS7WoM-p0M_lQOHOc_xXgY4Cft6rwhNSIokHXjyaGGvKPcSSaMiBAn4o7_JA9xCvMQ0O2vvHN7NbYBL2rzlCKTFKuJCIbVVxj9KL_bzWvG4Qbuw72yCsfEAcbJTGSK7tZz9F280S1nsDK67YzCqGejOAV5q8OnXi6vAyNfvsfCka6gvyqtSYx-Y7uPH9k-d51fPRwzoKDYijX9JPJyCzlbJxNQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از بین‌الحرمین در شب نخست محرم الحرام
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/akhbarefori/660207" target="_blank">📅 21:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660206">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
اسرائیل هیوم: نهادهای امنیتی اسرائیل به دنبال تدوین استراتژی جدید در قبال ایران هستند
🔹
پس از توافق در حال شکل‌گیری، از نهادهای امنیتی اسرائیل خواسته شده است تا استراتژی جدیدی در قبال ایران تدوین کنند.
🔹
نگرانی این است که تهران ممکن است از این وضعیت برای پیشبرد تلاش‌های خود در جهت دستیابی به سلاح هسته‌ای استفاده کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/akhbarefori/660206" target="_blank">📅 21:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660203">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z4GU7b7OHNtI4zC5VoRucYlA1xwR-1CvPycZI6CMAEZC-oLfm5mdblBEeXQAJVjY70FeWXQhmaaTMZJ448OCaDb8JyUuR6rXJHKfkRTF_CEx6OMcECnPf2nTWoSYCEb5KKfnNkiy7VZE6tDCS3cdeqFyXHwwEYvVNTj7NivwU9xFtgIi3bG3G7QGIT4CxxY-xA_8mOyRImhZllLBASjJvXiLMavEK2oQc_IH9-Q9lIJ4VcR2xRTxOCuXmrdey5SjLL90d8bEdsPERAe4a1RqZQt9cBf5Ybk3btkLccd0D1MQvInQBbspMcm6DUk0PKKSq16gLF2x66Yqu7IjdQu8SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q184OdzqGS6ME9gj00ypyk2alF_XULuhU_pjSwsxxGKBcz_dj-TZROqF02-T2Cq0b3eDSxPF-RHChxmSSk5vk-VdDCIs6vvb7AbGpbgIdHpZhgStHBiTjCB32I-7q1t8uyeXlrKzyqDFL4HHW_3X7xOU8Z7pctHrIxUwAAIVHe2BbiObJf7G3p1c8TSPKv2vcrVqws0GjmOTdqOdDXEXwVAtaN8CW0zzDfQDXL9tSrQUPQ-XIEXeQFSlfkYrv1ZmQrIQAne-6lMEX-4u_r2sMpBW0I41vKvNXaRR22bi-oeZnleKtd2u_DEfZ6cftAVtIOVCIAie-qPmmCQYPaocGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cEOCtQ-vRoxtT1XoCoK-1I-qKsBvmuOU2w8KvthN-wOkQ3lD4vpJmW-GCpFRCb7OFHyw7TqiQ6sns9-PHbAEOF5Tht-W7XrStTxQwSPJYFNVyRUwawFCTzr-7iS-SZMFYW-tTWIqjzXhNRPwX2LOviA1oBvDCVzZ9qpa2hwdNwJB_PCdsHlfR4Zcy3qbq83e_xOevz2WMkfTfPuLLckoZQcPzV9nlZwN1NGtKEtxza3a_0JVYkA7BofYDIKXX7rZiZC9HjonAOT3qwN3jAspZGzI4M2Shd6r3vksmac5yuLg3Eh14dBLR_hodo0VuxOgdmftjpt9BSEgokOZ6eVITg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عکس‌های جدیدی از طاق‌کسری| پایتخت ساسانیان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/akhbarefori/660203" target="_blank">📅 21:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660202">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3BWtspgdMDXuDbPO6Ahjp_MPFRARDKpEUc4j4TlMKtj0rkKrSdy8r_9Ji9P8DqWTTiMN-acuDsNYx1fSH9AFLSp-MjXsKKL97mM6IMzfe1pa4xhj45BNU-p_aFC7N9QAtmxiaB8Noztup1VbI86XPaQ_vBkYbnyLC3SUI7Xo9p56N0z2WSbxbDVnMixdzbrpitGm5VOP0zuCow5xmmSA3qH7iVNiQROiAVEyowUXP-ngbAoluN5F5lEVZzputBeRBnu9BpLi1XuhSRal24GIMcxmUdJBIHjKEcjTQ91oXOHh-q4ANq3l9Vy1eneWTgYfB17hDiSbD-kXVctfMcssg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی: در صورت بدعهدی آمریکا، پاسخ ایران، نظامی و کوبنده خواهد بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/akhbarefori/660202" target="_blank">📅 21:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660201">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
اطلاعیه شماره ۴ ستاد بزرگداشت عروج خونین امام مجاهد شهید آیت‌الله‌العظمی خامنه‌ای‌
🔹
هم‌زمان با آغاز ماه محرم و در آستانه مراسم وداع، تشییع و تدفین آیت‌الله سیدعلی حسینی خامنه‌ای و شهدای خانواده ایشان،
شعار محوری این مراسم «باید برخاست» و نشان رسمی آن «مشت گره‌کرده»
اعلام شد.
🔹
بنابر این اطلاعیه، «مشت گره‌کرده» نماد استقامت، ایستادگی و تداوم مسیر ایشان است و شعار «باید برخاست» با الهام از مفهوم «قیام لله»، بر ادامه راه، حفظ آرمان‌ها و تلاش برای آینده‌ای قوی‌تر تأکید دارد.
🔹
مراسم با عنوان «بدرقه آقای شهید ایران» برگزار می‌شود و هویت بصری آن مبنای تمامی فعالیت‌های رسانه‌ای و فرهنگی خواهد بود.
🔹
در این اطلاعیه همچنین بر جهانی بودن این سوگواری و همراهی آزادگان و دوستداران در کشورهای مختلف تأکید شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/660201" target="_blank">📅 21:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660200">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHuvSE5pUaoYWLX8_vhSnCY62D0B2UHCw7geiinLf3FHqknYB4w4HnuI8EhRFpd37Fz_F7SWxHWYMpsXQQmCAbyJsDu9nfL6Wfp29vVYG34g8LUKwT0SEhvj3tCM4EzF3bai0SyAIowCX5xOGHQjcXfs87T_OSbOXGDjuvEwnoXGONJmG6OzVUnVQiDIrUh5P-VZedet3-HhxGMrivkkJT6cx0yPfNOFUKqjbWE2wFN2cGgg27wrQHmF8hB1v0U-J0wBnrAdfL57fyXmvf2GGpBz67_BOaLErhprP7E-TOZ1ZrHHW8CG6N1FaYeW0LkPeWE3F-Vpsq4BdGA0yN9naA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهنمای مقابله با هکرها
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/660200" target="_blank">📅 21:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660199">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
پرونده جنجالی اپستین برای جلوگیری از هرگونه توافق ترامپ
افسر سابق اطلاعاتی رژیم صهیونیستی:
🔹
نتانیاهو ممکن است برای برهم زدن توافق احتمالی آمریکا با ایران دست به افشاگری علیه مقام‌های آمریکایی بزند.
🔹
یکی از روش‌هایی که ممکن است نتانیاهو برای جلوگیری از توافق بین امریکا و ایران به کار بگیرد، انتشار مطالب و اسناد مرتبط با پرونده اپستین علیه دونالد ترامپ است.
#جاسوس_موساد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/660199" target="_blank">📅 20:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660198">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9fSDb9KCihTFxUDVymufCzi3P-p3pnYtdUO9KG38RvjAAUOu7iLzcjvNv8Chign9LwyGQVturGaXe-P3qlt0_vSK3RfkOW2KYiOsCiYzFUdpbJXo50z-L6Wnj-7ABy3ZHJ5PDHomre2kGOj-vEsv1PCqVxuwZjXDYOitg7ymeXS7Je3bbkNWr8uX49ofvKajRah_9FO1N_xZ9Yow2XnCIjqlv56KCEs4F7ElGel5XKf1-S9uHESpFNdVsFR6BQZnbkU2g2VhiUMA8hThQtheNqzDxsodsEKjLMQR8PPYDVaiEzv6Kmkv-dvBXYPvpvAoHeqn3orAh_avz1NtE_QfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قدرت نرم سیاسی: کدام کشورها بیشترین سفارتخانه را دارند؟
🔹
چین با ۲۷۴ و آمریکا با ۲۷۱ سفارتخانه و نمایندگی، در صدر جدول قدرت نرم دیپلماسی جهان قرار دارند.
🔹
ایران با داشتن ۱۴۹ نمایندگی فعال، شبکه دیپلماتیک گسترده‌تری نسبت به کشورهایی همچون سوئیس یا امارات دارد.
@amarfact</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/660198" target="_blank">📅 20:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660197">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
نشست اضطراری در دفتر نتانیاهو با موضوع ایران و لبنان برگزار می، شود.
🔹
وزیر خارجه ترکیه: اسرائیل با حملات به سوریه و لبنان به دنبال‌ آغاز جنگ‌های جدید است.
🔹
صدر اعظم آلمان درباره توافق ایران و آمریکا:  ما همیشه گفته‌ایم که آماده مشارکت هستیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/660197" target="_blank">📅 20:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660195">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XEnfEvRn1sZ_aCoqrHHx_Dw3f8xNQXslrukhrYfXJUzG6UquTXIfDZvkQCRZASabduVlPj-dJDTsAZS7zN-tXbBYFKMd8dTIWCy7etIdfQkSNpzMuDvF4c9j4HVipkZotcWfcggJUZR3PiIpp418BF-FWShU6kz636u2Oqmo5jCwz-ZoiqDUuRxqQQyEblpwX38n54SI4GwmjQ6rl8rsFZiGzUmnGd0xs2eoHmwy88_j_ie8fP8rtglpSMc7o1AtWq_ywT9o-gEJ3VI29mLT1_pm-yfJ4AvP9izk2d-T5PQD8Ktw4HbAB_lzFWGyMw3GXQRy53k2ECP9XKqaEPAsqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y3h8XsA5gfFor5sdOKEJaN4FixzqqkeOWLPQO__6ZN9nZaynh75Cna7cd5oy6Pi-fIXvVyoOhJTHlgB9JWJ5ZhMTrVBdbtThU8OB3w8cf8kcL0x1NF91OeTrDA9LPjXKyTjkdIWpmVEkSwD0x7Is92MuD1eg8kIq16YGKcT-uJbATYUHvpyDWtGyzU5q2hD7XEt-CDYHtjIeqQlVnx5l79pOo31a2M8ZlwaTN-NfAQa6-5CQc3WS24MnHDAd0KjYMv-HZNIGZd_zNdsD07geo747oKJXOBbpsZjtC9fejWFVF15pJUbhUlNET8sn4IzKa3smr-3KrHiEGngJ8Rs0hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📚
نام کتاب: سفر شهادت
🖋
نویسنده: امام موسی صدر
🔹
این کتاب، سخنرانی‌ها و نوشته‌های امام موسی صدر را درباره عاشورا با موضوع تبیین هدف قیام امام حسین، آسیب‌شناسی سوگواری و بررسی نقش زنان، به‌ویژه حضرت زینب (س) گردآوری کرده است.
🔹
مطالعه این کتاب به تمام کسانی که می‌خواهند آگاهانه‌تر عزاداری کنند و عاشورا را از رهگذر اندیشه غنی امام موسی صدر بشناسند توصیه می‌شود.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/660195" target="_blank">📅 20:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660194">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
اختلال اینترنت ‌بانک پاسارگاد برطرف شد
🔹
پس از اختلالی که طی ساعات اخیر در سرویس اینترنت‌بانک بانک پاسارگاد ایجاد شده بود و دسترسی کاربران به خدمات غیرحضوری را با مشکل مواجه کرد، اکنون این اختلال برطرف شده و خدمات بانک مجدداً به چرخه عادی بازگشته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/660194" target="_blank">📅 20:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660192">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
اشک مادر، آتش برزخ؛ روایت تکان‌دهنده‌ یاسر از دنیای پس از مرگ
🔹
00:14:20 درک افکار درون قلب و ذهن اطرافیان
🔹
00:22:10 متوسل شدن روح به امام زمان(عج)
🔹
00:31:20 طلب حلالیت روح مادری برای فرزندش از من
🔹
00:37:40 تأسف همگانی نسبت به بد اخلاقی من
🔹
00:42:10 رؤیت اعمال دنیایی با جزئیات و بازخواست شدن در مورد یکایک آنها
🔹
00:48:30 چشیدن عذاب برای دل شکستگی مادر
🔹
00:55:20 غیرت افراطی من دردسر ساز شد
🔹
01:03:10 شکستن استخوان‌هایم در فشار عذاب گناهان
🔹
قسمت پانزدهم (حلالیت)، فصل چهارم
🔹
#تجربه‌گر
: یاسر درخشان
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/660192" target="_blank">📅 20:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660191">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/890b5cbbd0.mp4?token=k4vW8wFVAa6KbvqdCdmEISkgHo0Jjpb3nlPoqyg_-ajf8I9ti-gcHTEIfVzRjppaKzn1xCHJA2yAmVpHRLLzyPKWsJCsCf7RRVeWIfSe79odF5-_vklfJLglHN7Q7e9uSvIRCaoydcHW-VJMQ1CIE_LIOEsstmGoe3YTlGvt7GdLKDqBsfFQ4ppAccM6siN1mKjKrtbwK8AY9QTsA7qmLOexrBUmY-CZVoEjhNAkZ3QsdKGw6j4ctvoI6TpNH7FzFQvykOlpMNg2wmQKwFNwnpw1lapSexq-RLWCDtiPzvRdsMJe4VBeSlYBx0PRffU7Awp9ZAUgglukQB31qGpENQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/890b5cbbd0.mp4?token=k4vW8wFVAa6KbvqdCdmEISkgHo0Jjpb3nlPoqyg_-ajf8I9ti-gcHTEIfVzRjppaKzn1xCHJA2yAmVpHRLLzyPKWsJCsCf7RRVeWIfSe79odF5-_vklfJLglHN7Q7e9uSvIRCaoydcHW-VJMQ1CIE_LIOEsstmGoe3YTlGvt7GdLKDqBsfFQ4ppAccM6siN1mKjKrtbwK8AY9QTsA7qmLOexrBUmY-CZVoEjhNAkZ3QsdKGw6j4ctvoI6TpNH7FzFQvykOlpMNg2wmQKwFNwnpw1lapSexq-RLWCDtiPzvRdsMJe4VBeSlYBx0PRffU7Awp9ZAUgglukQB31qGpENQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کمتر زحمت بکش، بیشتر نتیجه بگیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/660191" target="_blank">📅 20:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660188">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
کانال ۱۲ اسرائیل به نقل از یک منبع امنیتی: عملیات ارتش اسرائیل در لبنان بصورت محسوس کاهش یافته است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/660188" target="_blank">📅 20:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660187">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jg3vjn-VRaLLvK2EILQeM84_N8O8KAEYe4OkVmzv2knNuR_kfT-Y9iwm4f0r_o0G60HDBuOtVwuNSHutliGh1430NF_Lqg4wFoqegw1MyieeFkzJykkRTNdDPBVF8QPCcUrnFELIHxL1LL7xHVv9muKyACkimJ2KFM0E7raGT47k7ZnzkZ3T2qJDoEPb07iB-f4BON-pHpBstOl4Hm7VWbhuu88RVBBnOxc8hHfXYcXgXx56fOdUF5C74mG08z0Q47PkSouBiJMxi28wjTjKjYdhm5M9NdE7ch_P0N6Xf9Vs3DcXN6yyVnKxCoxhFC0WTDVIVqU5rc9KgH-1e6LWZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استان‌هایی با بیشترین سهم خودروهای فرسوده در کشور
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/660187" target="_blank">📅 20:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660186">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
واکنش عربستان به تفاهم ایران و آمریکا
🔹
فیصل بن فرحان، وزیر امور خارجه عربستان سعودی از تفاهم میان آمریکا و جمهوری اسلامی‌ایران استقبال کرد و ابراز امیدواری کرد این تفاهم به بازگشت ثبات در منطقه کمک کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/660186" target="_blank">📅 20:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660185">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
ادعای وال استریت ژورنال: واشنگتن به تهران اجازه خواهد داد تا بلافاصله فروش نفت و سوخت را طبق توافق پایان جنگ آغاز کند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/660185" target="_blank">📅 20:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660184">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/184de72b1a.mp4?token=KgwErSKZ-xz3Ab0qkNYSuCrHp6aUX7Ym8bPyu1bCZQtjWPK-rF5tnANjxTO7MPFNFBMZl-A3RgC2D1DOnRNTsJ6Mi1udl8yMWxrEsgPhv1CDXYAPh5kC_MzIIfZ9VBeR0Xi5iVboKqIC95cnXd612uFxkfPy-Jw4q-yFBe7BBicWnupYTNaf4W2scTUsnrzyLUbXpEnxj7VDTb2OG4xy8uFHyLbe4jl2szCpMKJKLumqiCI7Z1w1rDB5r_q24gRa1bELOQcBA6_rl5Au9OdmFLnrX9EA7aaPHoC9Fm4z-KdK9t745iwTNqcHxqgMGQxULVpYoiaLOFQdV1gpVnxlgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/184de72b1a.mp4?token=KgwErSKZ-xz3Ab0qkNYSuCrHp6aUX7Ym8bPyu1bCZQtjWPK-rF5tnANjxTO7MPFNFBMZl-A3RgC2D1DOnRNTsJ6Mi1udl8yMWxrEsgPhv1CDXYAPh5kC_MzIIfZ9VBeR0Xi5iVboKqIC95cnXd612uFxkfPy-Jw4q-yFBe7BBicWnupYTNaf4W2scTUsnrzyLUbXpEnxj7VDTb2OG4xy8uFHyLbe4jl2szCpMKJKLumqiCI7Z1w1rDB5r_q24gRa1bELOQcBA6_rl5Au9OdmFLnrX9EA7aaPHoC9Fm4z-KdK9t745iwTNqcHxqgMGQxULVpYoiaLOFQdV1gpVnxlgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رامین رضائیان به خبرنگار خارجی: مسائل داخلی ما به شما ربطی ندارد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/660184" target="_blank">📅 20:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660183">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccMXeYjze9JsmsHgfnt4AwFs1H6nW2olYWyAH0yV07GMzRaVOi5iDzTG0hTfmOGxIg5qPr7BE8yfxMt4n7XGHNRn5VsINj6eUogToOrsZcWhMeuGd-g3SmpoU2qTIAv6cdpcTriS1g87gRPV8AVMvGTOrz7hZtUBjNMMC1cZHY0c9IZcYYqTU_bpeQ58xDthUn6AKniSZnGnIX7rjAE4eEtntPsNoEYQa5XLjbCwwucBHs9_UJmFd6HNmmJ9ap-6ufWFUZK4MwD4uxRvmr3rOwujoI56kVhrZQeGCN8nNTDXF0aDh2308xYyaFwunDdEReDFJCkJ6tRr6BpFXasjVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔔
اطلاعیه پیش‌فروش بلیط‌ قطارهای تیرماه در علی‌بابا
بلیط قطارهای تیرماه با تاریخ حرکت 1 تا 31 تیر
از ساعت 8:30 صبح 27 خرداد
در وب‌سایت علی‌بابا پیش‌فروش می‌شوند.
قبل از تکمیل ظرفیت، رزرو خود را نهایی کنید
👇
https://albb.ir/pS1ODe</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/660183" target="_blank">📅 20:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660182">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
سی‌ان‌ان: ایران می‌تواند هر زمان که بخواهد تنگه هرمز را ببندد
رسانه آمریکایی:
🔹
جمهوری اسلامی ایران در نتیجه جنگی که آمریکا علیه آن به راه انداخت، «توانایی جدید و قدرتمندی» به دست آورده است.
🔹
ایران ثابت کرد که می‌تواند دسترسی به تنگه هرمز را در طول درگیری فعلی مسدود کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/660182" target="_blank">📅 20:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660181">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
ادعای وال استریت ژورنال: واشنگتن به تهران اجازه خواهد داد تا بلافاصله فروش نفت و سوخت را طبق توافق پایان جنگ آغاز کند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/660181" target="_blank">📅 19:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660180">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k73-4Phv_XcExj0X_rqjD2C2V7Wi2UjVVGSlm9_bdXkRHI61rhmvXKOh6MWs6-X5NBTLqqMjUWympmdEzxiD0Q8UGu05DRuxE6nES-mx7WnQpMNlwfkJTh-wAeEXKDb3st-S_hdbAu7JUv7KjsYIe3sBt3s0Gp-YpykIrTuTdWL__QZPJ885nCQovG8ZKMLIBkI8tJroBQwymBs4hwutKN0VWJliAA1NkUmc7byNpfQIM-bWttR0dC9hLBuBOQy4q3ooEJphfxanp92TNrWIjlwT9uML-BFIWY9J8XqqHnagC1GFkO6E5n-UAP-QkDzZ-GkFPVVxy0gCvw-UokUsYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فارن‌پالیسی: تولید و توزیع و ذخیره نفت همچنان با اختلالات جدی روبروست و راه درازی تا بهبود وضعیت باقی مانده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/660180" target="_blank">📅 19:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660179">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
زلزله‌ای به بزرگی ۶.۳ ریشتر، استان «چینگ‌های» چین را لرزاند.
🔹
قطر: هیچ بودجه‌ای برای چارچوب بازسازی ایران اختصاص داده نشده است.
🔹
سوئیس: توافق‌نامه ایران و آمریکا در «بورگن‌اشتوک» امضا خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/660179" target="_blank">📅 19:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660178">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
اسرائیل هیوم به نقل از مقامات آمریکایی: ترامپ در حال بررسی برکناری برخی مقام‌های ارشد مخالف توافق با ایران، از جمله وزیر جنگ و مدیر سیا است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/660178" target="_blank">📅 19:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660177">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
ادعای وال استریت ژورنال: واشنگتن به تهران اجازه خواهد داد تا بلافاصله فروش نفت و سوخت را طبق توافق پایان جنگ آغاز کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/660177" target="_blank">📅 19:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660176">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311cd4ff7d.mp4?token=b_ORnkoj9-iJgZrcCG-v6NghuQh-YSkFumOoRlzhDKntzflnjJ6Uj9Q0SFcFQpmi0RHgU3A3kB1ClOGKVGEgtfAoLGj4XosSAbw18_dBSLmWt_gISPXciKsY7892GWjAhGluYt9ATZz83ebD2jEgVX8mmks6xJyqtlhuapWZ9XQr4qQ0VpNLvL3FRfcXdognSJqPQuN1ALjTIaVUorqNC-SblX-9IqAS7oYV4EzSY7S3iccdkkGMEszhb5NoqnK5yZHMnYwQ5aMB154t-qz40xU9SOC7AfpaYH8E5wgPCqXu2TugAsnqbLzE9l540PFGIu2IWCXAP1AjCr2IgomDrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311cd4ff7d.mp4?token=b_ORnkoj9-iJgZrcCG-v6NghuQh-YSkFumOoRlzhDKntzflnjJ6Uj9Q0SFcFQpmi0RHgU3A3kB1ClOGKVGEgtfAoLGj4XosSAbw18_dBSLmWt_gISPXciKsY7892GWjAhGluYt9ATZz83ebD2jEgVX8mmks6xJyqtlhuapWZ9XQr4qQ0VpNLvL3FRfcXdognSJqPQuN1ALjTIaVUorqNC-SblX-9IqAS7oYV4EzSY7S3iccdkkGMEszhb5NoqnK5yZHMnYwQ5aMB154t-qz40xU9SOC7AfpaYH8E5wgPCqXu2TugAsnqbLzE9l540PFGIu2IWCXAP1AjCr2IgomDrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گاهی یک تصمیم ساده پشت فرمان، می‌تواند تأثیری بزرگ‌تر از آنچه فکر می‌کنیم داشته باشد
🔹
این انیمیشن کوتاه، داستان انتخاب‌هایی است که با مصرف هوشمندانه سوخت، به نفع همه ما تمام می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/660176" target="_blank">📅 19:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660175">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyXVvzYpEQN5_B8uw-gxN0Bo3kySZNKQlnlcZMKkYbANdHgG6wqwZtPcXKEVYrIeRoW60nPg4jUl9AutZmpPPVIg8zqzHeZpA369TQo3jLFzkC94dNyflmgB6roG2tJK93o9tBurU1RIEzaAdnHo6Vxkk5yOYoc_3oOqPDbwYvFsXHxvI6Vit5qF_GsL7kaFc1xxAOdGhxGNxPIHuOSHhzJse2uPrLoW7yVdvKQErXD867giSjx_Eh5gPnHuIWtAvJnOalp9i6P5eNp2FvvgRatugoKuxguqydRi8dpY5rP9_gcrGQHV8fadqznjjN8vjCwBQKI249q_7dXfvYuM0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری متفاوت از رئیس جمهور و وزیر بهداشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/660175" target="_blank">📅 19:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660174">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfV_QB3SSfdcKQvFLlNKYYOr3cAOyeOq9x_9CYsQBmqgHJP5rDmHpUXE7wXOrhLOJGdubNCVcF9ui1nfgHmRCgKkltNy1mTSeKUKXChjCpXTkHWOOBZchNj7iIa8j7mkU_6bru4h4fVNGe2ng8n5GNx0nyy4w1lHJKgKddy0nav--L2HPMQBZEGFId8rurx3WrSEf6tvWrnkXbDIkqxXU-ypZSl6wYFD5K_uC90wApRyRByavHoabdl7cmJw0tSTHDQ05dBcjpTvEjGfgfoUe1XgJCf92Gb1hNwUby7H7k69HoSnsGaAVNJAK8mXKFr-5ISkfwmbkxusv_qmWAv8Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توافق لرزان «۶۰ روزه»/ ۵ مشکل اصلی تفاهم ایران - آمریکا/ از سرگیری جنگ یا صلح «دائمی»؛ با این کار می توان «تفاهم» را طولانی کرد
🔹
مساله ای که باید به آن توجه کرد، مساله مذاکرات هسته ای است. طبق متن تفاهم مذاکرات هسته ای باید طی ۶۰ روز انجام شود اما آیا این بازه زمانی مهلتی است برای فیصله یافتن مذاکرات یا نه، مهلتی است برای آغاز مذاکرات؟
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3223225</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/660174" target="_blank">📅 19:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660173">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
ابلاغ حذف تدریجی چک کاغذی به شبکه بانکی کشور
🔹
با ابلاغ بانک مرکزی، بانک‌ها مکلف شدند نسبت به کاهش تعداد برگ دسته چک مشتریان حقیقی در ۴ مرحله و مشتریان حقوقی در ۲ مرحله با فاصله زمانی حداقل ۲ ماهه بین مراحل اقدام کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/660173" target="_blank">📅 19:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660172">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/530d0872f8.mp4?token=WjYocO0PTIh9R-Xb5oYAfO1q7pfmS_hDpIgJihZ8QssI4iJeWqa3mQOEuwWU-Qmjlz6HdmH5CSF_0a7SpxeS2wQPd5hW8ECaLBJsq5TU4XY-BdNvxrahUDLj6p3RRkAJLWw7Yi08sFkyAwHDykOLlbvHyvYKRAH-GNxsxEnYo1OsLSQDDv_HMpRYrUXDjx2ZW_fcsYTaVmkUEbk73bayVGSECGDs5XkmVVmPD3qMuDda52O8WXsnx3nIWCAdu3UcTar03TJeMt01VGipMQW_RkntgmDns5vuXDKlXGoXb9jGFAyY9xHc75_o8HNdoZMdUz6Dh3Mauw_yJPtJBqwHPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/530d0872f8.mp4?token=WjYocO0PTIh9R-Xb5oYAfO1q7pfmS_hDpIgJihZ8QssI4iJeWqa3mQOEuwWU-Qmjlz6HdmH5CSF_0a7SpxeS2wQPd5hW8ECaLBJsq5TU4XY-BdNvxrahUDLj6p3RRkAJLWw7Yi08sFkyAwHDykOLlbvHyvYKRAH-GNxsxEnYo1OsLSQDDv_HMpRYrUXDjx2ZW_fcsYTaVmkUEbk73bayVGSECGDs5XkmVVmPD3qMuDda52O8WXsnx3nIWCAdu3UcTar03TJeMt01VGipMQW_RkntgmDns5vuXDKlXGoXb9jGFAyY9xHc75_o8HNdoZMdUz6Dh3Mauw_yJPtJBqwHPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مثبت و منفی تیم ملی بین تیم‌های جام‌جهانی
🔹
عملکرد تیم ملی بعد از بازی با نیوزلند، بین سایر تیم‌ها و بازی‌های انجام شده بررسی شد.
🔹
در این ویدئو خواهید دید که تیم ملی در کدام بخش‌ها بین تیم‌های مختلف عالی بوده و در کدام قسمت‌ها افتضاح!
@Tv_Fori</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/660172" target="_blank">📅 19:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660171">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUs0oZXXtse7w8MD1FqlXkcamohKRNGAqw5IxbnmxfZZmiskRgIWz7D8UzOG9T4APD9c9x9CwfHDZVgHpFQq42PksVDesnwTTfbPiPTgSOlEDtiOI65xhU9bmr0rBpwIHn5WJ_IoCYRb4_On8pJiW8tXVD7v9BwqgfluV-fwDc5O3FT652oZYIAbFOUh4o1IKwtIFwrSOaM5buBUQyOcC77NHRZGtmd0JmYq3y6MzM4LGT03MTPq0akGNKG06fqeEwO9VesBzUfO2vpj8OY_0qQEOZpFf79Isd1K7FEEQhIdlI8dtAVD0fv7kMqT2MsAOhE-CvoAWxeZZRz3W8l40Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💸
آخر ماهه و حساب و کتاب‌ها به هم ریخته؟
ممکنه برای یک هزینه فوری پول لازم داشته باشی؛اما یک سؤال:‌
چرا باید داراییت رو بفروشی؟
اگه در ملّی‌گلد طلا داری، می‌تونی به پشتوانه همون طلا وام آنی بگیری و یک ماهه وامت رو تسویه کنی.
✅
تا ۷۰٪ ارزش طلای خودت
✅
تا سقف ۵۰ میلیون تومن
✅
واریز نقدی و آنی به حساب
✅
یک ماه فرصت بازپرداخت
یعنی وقتی به پول نیاز داری، لازم نیست از سرمایه‌گذاریت خارج بشی.
طلات سر جاش می‌مونه،
پولت رو می‌گیری،
و بعداً وام رو تسویه می‌کنی.
✨
اینجا طلا ضامنته.
🔗
دریافت وام آنی ملّی‌گلد
🟢
ملّی‌گلد؛ پلتفرم امن خرید و فروش آنلاین طلا</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/660171" target="_blank">📅 19:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660170">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dx7CKNEJz_BBtgX4idgNxA_OCMoha8fpCkzG886cmnGC3-firu4yqy8ExmA707OiqyXQr3fa5qMNWekKY9RmsPmTWXlp5xjQvcpHdEoQLBPksjnf0adl6Ft0_p8EUMVH7Kwp1Fr0z2vrUeXDUKBRg-w-QGPKbtC5j4kbyuFkPGTJNMyxMA3QA3FwAxR2JNCsXVXfj3BoHWbgefSPz6MnUrMbe4i_fzLFTHbQbw9FJTPxFwPqs4tA2q-70kYHk0DdLO5uD4dWz9BSU4RI-PydgLd6rfCFZ9cxKI7u4mtG_GhThctFhjhMsQTT2AS2Gor9xeK5jwSkAc2q8z2uGdrwwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/660170" target="_blank">📅 19:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660169">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-text">✨
آیین سنتی صلا در حرم امام رضا(ع)
◾️
در نخستین روز از ماه محرم خادمان بارگاه رضوی در آیین سنتی صلا، آغاز عزاداری حضرت اباعبدالله الحسین(ع) را اعلام کردند.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/660169" target="_blank">📅 19:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660168">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
چین: در مذاکرات آمریکا و ایران نباید به عقب برگشت
وزیر امور خارجه چین، در تماس تلفنی با محمد اسحاق دار، وزیر امور خارجه پاکستان:
🔹
چین معتقد است که در مذاکرات ایران و آمریکا، نباید به عقب برگشت، چه برسد به استفاده از زور.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/660168" target="_blank">📅 18:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660167">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EfA3aNFaId5IBKpsLlhoyynZYpGm9SDdOfsdDWVptg_jcXq6Nh1N5vcurTUTp_UWI9NFfvZ2aCBpAFa7pDbStyDoyy2Mdzdiko9O9UXNnf4zjOmafXlSk0Yn49zFKomUZB-TeTtB72GVXGG8xlOLlh9jK1Qc1zSJf1gO2PGwmSUUd53KUzF384t6t4QfX1Tl_SVJ1MRyzppFdb3feIzcICidfBckP9V267x0s-U_C66-dp-aqc60mZ9lcZ5lzDL0BwVP0XWHsrZMkz7hkymbvxPls9RbvemhslL_-fdOErr4NXURq4PwKzkDDb19B21Yxo0fnXDXRSjLRWE4tVOYog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولمرت: توافق آمریکا با ایران خیانت به اسرائیل بود
ایهود اولمرت نخست وزیر سابق اسرائیل به شبکه تلویزیونی RTE ایرلند:
🔹
توافق احتمالی بین آمریکا و ایران می‌تواند در اسرائیل به عنوان یک «خیانت» تلقی شود. بعید است نتانیاهو علناً چنین چیزی بگوید زیرا او «کاملاً، کاملاً به روابط و حمایت» ترامپ، وابسته است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/660167" target="_blank">📅 18:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660166">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmV9l47PDl3mV4iYt_yAvrcHHZvwaD8xn-C62-YAow0E8AV4HKBPTbByGMcatJT1LhjGSb9jo_YPfyJU_XUZUiixzU1BZULR54i3WBCKulihX3M11FC7IGR4uWrSB0xw4kigiHxI5tXhDkL68VKap7o442YpjpQefI0N-KDxjVvI-P0JE5240hfzI09q1PBY16VId7Ln2s9FZr95BEYCmZ1sCDum8N5KomrdvgWURb07g-l3WiPbKNf46KlxyU6OC6RexcS1otlk04KeJugo6-KDZEdQi_4Z8n51QKuKnqLebqQFYRNlqjHLtwEFCxM3EhHH5h2RV-LQq-q_GaI6OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: ‏آنچه تفاهم شده، گامی مهم برای توقف جنگ و شروع مذاکره است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/660166" target="_blank">📅 18:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660165">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cec2c4256.mp4?token=vZuE7m0rXxpvGZihfXK_jfSB22ARnqdESyfEshWF_unBDZ1tQnZmoMK0_AB0KojywHfhUmhzoi1Pz77ZCM6lFtmUz-sH7d3oR_2yVCEOL9GmDPXI9shAkm7Q1g0I_VVY3_nJPUuRPN3uT6a0JFUPd8HVV_28VcK7L3vTJcwxCUmZT4RZIMPDOceL7vAqknqN_nMnfcsHERczsV4ZRt9F_RfO8y7V4nkksbkJYpBoPEk9_Pho66seKFw32xYiW9Cj3Ui_83iC7JhrUKapCS_xCrvEe6UY3jQ-p6W-erwCKSI_T2kEeeYGa2McCQw4H5S2I0YV9C1XwZV4rVVjXtAs2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cec2c4256.mp4?token=vZuE7m0rXxpvGZihfXK_jfSB22ARnqdESyfEshWF_unBDZ1tQnZmoMK0_AB0KojywHfhUmhzoi1Pz77ZCM6lFtmUz-sH7d3oR_2yVCEOL9GmDPXI9shAkm7Q1g0I_VVY3_nJPUuRPN3uT6a0JFUPd8HVV_28VcK7L3vTJcwxCUmZT4RZIMPDOceL7vAqknqN_nMnfcsHERczsV4ZRt9F_RfO8y7V4nkksbkJYpBoPEk9_Pho66seKFw32xYiW9Cj3Ui_83iC7JhrUKapCS_xCrvEe6UY3jQ-p6W-erwCKSI_T2kEeeYGa2McCQw4H5S2I0YV9C1XwZV4rVVjXtAs2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از حباب تا صدا؛ داستان علمی شکستن انگشت‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/660165" target="_blank">📅 18:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660164">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
گفتگوی تلفنی وزرای خارجه ایران و عمان
🔹
وزرای خارجه ایران و عمان در گفتگوی تلفنی با تأکید بر حفظ امنیت دریانوردی در تنگه هرمز و تقویت فضای دیپلماتیک پس از تفاهم اخیر تهران و واشنگتن، بر گسترش همکاری‌های دوجانبه مبتنی بر حسن همجواری تاکید کردند و طرفین در پرتو تفاهمات جدید با آمریکا متعهد به رعایت قوانین بین‌المللی برای عبور آزاد کشتی‌ها از تنگه هرمز شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/660164" target="_blank">📅 18:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660162">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
محسنی‌ثانی: محاصره دریایی برداشته شد
محمدرضا محسنی‌ثانی، عضو کمیسیون امنیت ملی در
#گفتگو
با خبرفوری:
🔹
از دیشب محاصره دریایی برداشته شده و کشتی‌های زیادی معطل مانده بودند و الان دست ما در خلیج‌فارس و دریای عمان بیشتر باز شده است.
🔹
در صورت عدم توافق در این دو ماه، جنگ دوباره آغاز می‌شود و نیروهای مسلح با قدرت بیشتری به دشمنان پاسخ خواهند داد. پول‌های بلوکه شده نیز قبل از امضای این تفاهم آزاد خواهد شد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/660162" target="_blank">📅 18:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660161">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FfokkrZPuNOFcAxI3ojn3plVxnpygjm9Chbu-mG5r7GXNs1401wetSDPc0VPMIEgvCMdF79WoqZl7TBHlNCOUHtoCyvJ-fcFvP0sF1udLKLUMkssOuq_K5xSFfTsl7GlkhSjHES-XKEvf92SGQk3nrYfKIRnQk5OFBjSLj2JoCmGKUFk7vAebwL4K9sKL9ehCBW59c7h1IIdB2T3K2Zge7P4v9hRQtH2aRlflpBfNMq_e2QAUKP8drYNiUuGbasUXwSA_SeGH4fKJMXUoFpEawOCPqoVX3Gd7gvZw1sA3JNhmlXSYzd7MmRuTCcivO6ONGni1gAddSNBIy_W_ifm-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نسبت مذاکره و توافق با خونخواهی
🔹
تضعیف و شکست دشمن و تحقیر او در برابر جهان یکی از وجوه انتقام است و اگر توافقی صورت می‌گیرد باید بتواند به طور ملموس و بی‌سابقه‌ای به این هدف جامه عمل بپوشاند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/660161" target="_blank">📅 18:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660160">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
بانک‌های مرکزی دوباره طلا خریدند!
🔹
طبق آخرین گزارش شورای جهانی طلا، بانک‌های مرکزی جهان در ماه آوریل ۱۹ تن طلا به خزانه‌های خود افزودند.
🔹
چین در هجدهمین ماهِ پیاپی باز هم به خرید طلای خود اضافه کرد. لهستان و ازبکستان همچنان بزرگترین خریداران طلا هستند. همچنین ترکیه، روسیه و آذربایجان صدرنشین فروشندگان شدند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/660160" target="_blank">📅 18:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660158">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GR0JeYMp_vvAULWP8lEJl5CDKPLFI9UlU00SyW_U8I-WFhN0UB7GhaQgZDn6LvfvgC-5iU4IrmPr3jrxULqlA5bHLKbwvITxEr8Deuq7ln89Ot3PHsrStcy3eHNlb7GDAj9YQbrc6bkXV6DLIixIpK9P2OkScDGGD7R2RCLh1eUey76CC6si7v_Sf-pb7N-EORi_WsVAP2t53J6NwoBhSSoBNeSuXuBR2P73aUPPs-0gabUyjr80KfepJdoxnMcNrj7iAD2MBEKfzC4Fy_1aVan-nSUNR8-vXb3Sb8NDrUR88RHUolZXloAxJJYwbtXVmyzejRwv6ISYium9TNt48Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محتشم کاشانی؛ شاعر مرثیه معروف عاشورایی
🔹
محتشم کاشانی شاعر چیره‌دست عصر صفوی است که از خانواده‌ای برجسته و تاجر پارچه بود؛ اما ورشکسته شد و تا پایان عمر در فقر و تجرد زیست. علاوه بر مرثه مشهور «باز این چه شورش» است بسیاری از تعابیر  رایج فارسی چون «عذر…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/660158" target="_blank">📅 18:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660157">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
نتانیاهو برای چندمین بار روند محاکمه خود را مختل کرد  شبکه ۱۳ تلویزیون رژیم صهیونیستی:
🔹
دادگاه رسیدگی به پرونده‌های فساد بنیامین نتانیاهو، نخست‌وزیر رژیم صهیونیستی، پس از رد درخواست وی به دلیل «ناکافی بودن دلایل ارائه‌شده»، با بررسی مجدد و با استناد به…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/660157" target="_blank">📅 18:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660156">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/615a222da0.mp4?token=O3SHPWvOo3Lin6S-ahjDPbmdX8RJwpXTv98_xIr1agGykZ3qf3hZPkg4ccywAOsGAZpCzgzwScCs1zvqSn8URADIRmqPhUvT7OYvQqHibF4hnTAnvt_BKYpmsl6XAdqbKPuL_kL5bCxoO2NeDOCN_vutruVQBepPFpBQqkx-k9kQgIGqJJJiSbD9Djfz8MoBoXA4mlkSfZ9f7WURoYIwzytqXLLidHvrEfKma0fPIOMed-PNRX0qt54zLfaqj0PSkEA04HFA3lksHo3TCjLfKQnR7vZ6aZvP1HKXPC-zDKt7y7YwfKU4ebgq_WcjCxkAPZSxP_qeZ7MB0WopFnIe-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/615a222da0.mp4?token=O3SHPWvOo3Lin6S-ahjDPbmdX8RJwpXTv98_xIr1agGykZ3qf3hZPkg4ccywAOsGAZpCzgzwScCs1zvqSn8URADIRmqPhUvT7OYvQqHibF4hnTAnvt_BKYpmsl6XAdqbKPuL_kL5bCxoO2NeDOCN_vutruVQBepPFpBQqkx-k9kQgIGqJJJiSbD9Djfz8MoBoXA4mlkSfZ9f7WURoYIwzytqXLLidHvrEfKma0fPIOMed-PNRX0qt54zLfaqj0PSkEA04HFA3lksHo3TCjLfKQnR7vZ6aZvP1HKXPC-zDKt7y7YwfKU4ebgq_WcjCxkAPZSxP_qeZ7MB0WopFnIe-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک روایت جذاب از مسئولیت‌پذیری و همدلی
🔹
این انیمیشن یادآوری می‌کنه که صرفه‌جویی در مصرف برق، یک انتخاب کوچک با اثری بزرگ برای همه ماست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/660156" target="_blank">📅 18:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660155">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13126b7b73.mp4?token=RpXaohRBG4tfqIZjuX1QszddJMmYNY_O0Je0X0GGoNkOKfd_BJGNsuTR3oBnkto7TPvnjs7DKbpIarq4aM1SPfxuKr4D-PL-T94IPaxC1MIqRADZAEs1_Rk7Sh3bxUf7-kYAYvLvLAvaMFZwuSsQpMjJxPmWcjfbXydysZ0SXvl5Q4Fm0onw8ljVnfO_F9evyhynHXGNMGy4FTmAM2rF2iJx__dlGV_EEizZSPC1aK_n7WSf5dr5TO2kmDziajE14vXgnaLWMIshBedL_1emgm43ZSVzN6bZOnSwJeiZwzIfVyEEBQFCxPTvgAYD3bTZCJNeFIKhg6nUr2Dt83ALd5fZaXUC0Lft0odz4E6uirwGg0jZA0wv6oSE9inP434eQSIeOOLGqnjk8cqTXr_Bg2abEW3DPsa5J5oNteCuGOgPum6MGaG37KzlaUuoCyQ8H95hSfkCpcSj04WTm0mTEzyDNN4YoiFO1wACMmq4OoGBgQHIYe9IxqG-NjprHwoLCrB4i8O0SqUKGvjYl_Wvw8NVOq3GRbRO2Bvtqz5oNeautl-lYt9jsdAo8sImgaRLPslOW5PBW8FauwqmzuP35m3CKWlgCx8c2kI2TzQNUtPX2kiOrJN7I1dfFbMib-vINpSS0PaiPXF5h1x2YtxLjCAzoMVGpVidEcrL1vNSorM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13126b7b73.mp4?token=RpXaohRBG4tfqIZjuX1QszddJMmYNY_O0Je0X0GGoNkOKfd_BJGNsuTR3oBnkto7TPvnjs7DKbpIarq4aM1SPfxuKr4D-PL-T94IPaxC1MIqRADZAEs1_Rk7Sh3bxUf7-kYAYvLvLAvaMFZwuSsQpMjJxPmWcjfbXydysZ0SXvl5Q4Fm0onw8ljVnfO_F9evyhynHXGNMGy4FTmAM2rF2iJx__dlGV_EEizZSPC1aK_n7WSf5dr5TO2kmDziajE14vXgnaLWMIshBedL_1emgm43ZSVzN6bZOnSwJeiZwzIfVyEEBQFCxPTvgAYD3bTZCJNeFIKhg6nUr2Dt83ALd5fZaXUC0Lft0odz4E6uirwGg0jZA0wv6oSE9inP434eQSIeOOLGqnjk8cqTXr_Bg2abEW3DPsa5J5oNteCuGOgPum6MGaG37KzlaUuoCyQ8H95hSfkCpcSj04WTm0mTEzyDNN4YoiFO1wACMmq4OoGBgQHIYe9IxqG-NjprHwoLCrB4i8O0SqUKGvjYl_Wvw8NVOq3GRbRO2Bvtqz5oNeautl-lYt9jsdAo8sImgaRLPslOW5PBW8FauwqmzuP35m3CKWlgCx8c2kI2TzQNUtPX2kiOrJN7I1dfFbMib-vINpSS0PaiPXF5h1x2YtxLjCAzoMVGpVidEcrL1vNSorM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تظاهرات گسترده مردم یمن در محکومیت اهانت ترامپ به مکه مکرمه
🔹
هزاران نفر از مردم شهر صعده یمن، امروز در راهپیمایی گسترده‌ای، اهانت دونالد ترامپ، رئیس‌جمهور آمریکا، به شهر مقدس مکه را به‌شدت محکوم کردند.
🔹
ترامپ چندی پیش در پستی نوشته بود«کتابخانه اوباما ده سال دیگر یک مکه برای کسانی خواهد بود که از آمریکا متنفرند.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/660155" target="_blank">📅 18:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660154">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
۱۰ هزار تن حبوبات تجار ایرانی در امارات حبس شد!
ارشاد طالبی، بازرس و رییس کمیته فنی انجمن حبوبات کشور در
#گفتگو
با خبرفوری:
🔹
حداقل ۱۰ هزار تن حبوبات تجار ما در امارات است و هنوز آزاد نشده است. در حال حاضر در بازار با توجه به اینکه مصرف مردم مقداری کمتر شده، قیمت‌ها مقداری کاهش بوده است.
🔹
اگر ظرف یک تا دوماه آینده به این موضوع رسیدگی نشود ممکن است دچار کمبود شویم و ثبات قیمت‌ها دچار اختلال شود. در اصل قیمت‌ها تثبیت شده و کاهشی نشده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/660154" target="_blank">📅 18:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660153">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14addb21c3.mp4?token=XR35QvJ_S9DO89TBT_Kia_nAye2A2a9vb26HX6L11-aFHI5vlEWQBwgacQQjV9v0mnNGMSAqw2t50zDCNCqwdHOO6feyy9zqVVkO4IFvAbkRbkPsCuyPQun27gRl_hKwSlZP0Lnbj9ouS3awh9-ycIvXY0JkTAQ1_-t4rWweVlRnUgSiwcHDPDY0yVpeqLIikgGrZrvlIV-0gCSFjIlymICKudlx9inlIowWiizvMwTxALwaJo7iAA-ITYl42em3hb9D-q4dsHJbasFS2YXC5IndYaN_CrRkM_6Q0dzv6vqCdFo4bXyFCXL2hFWq1aNiuMN0aicW4k98hGeicqdS2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14addb21c3.mp4?token=XR35QvJ_S9DO89TBT_Kia_nAye2A2a9vb26HX6L11-aFHI5vlEWQBwgacQQjV9v0mnNGMSAqw2t50zDCNCqwdHOO6feyy9zqVVkO4IFvAbkRbkPsCuyPQun27gRl_hKwSlZP0Lnbj9ouS3awh9-ycIvXY0JkTAQ1_-t4rWweVlRnUgSiwcHDPDY0yVpeqLIikgGrZrvlIV-0gCSFjIlymICKudlx9inlIowWiizvMwTxALwaJo7iAA-ITYl42em3hb9D-q4dsHJbasFS2YXC5IndYaN_CrRkM_6Q0dzv6vqCdFo4bXyFCXL2hFWq1aNiuMN0aicW4k98hGeicqdS2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملهٔ پهپادی اسرائیل به جنوب لبنان
🔹
در جریان این حملهٔ صهیونیست‌ها، شهرک «میفدون» هدف قرار گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/660153" target="_blank">📅 17:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660152">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/auMQzBuOf1I12-A0ZtIE4zzITlLMgFU4otk8vvhJ02AyCPyLrPDGIXg_qhwgjmz4xDHlJwti-wS7Z00XHZFV41X9p5vaJLE6oloTVixtknlNbDPT6tZ_wPmGrc3QcqCE1kILBfFPWEfVOXtxj-j7K0vEtw5hCHQjHtfJwtPYgVQiMroxo8xeFFQKGFqKduDhyaCGMWEMzR9jWqqDoQmV1w9gsdIE-zShSW6K0YsMfo_o4UTZHDL9a8tfMtq_Q_z2HD2Us1x7p00iwBAa7HvYJrya3scsjsPUIz4JN7elkvjxIXrI6aw6eAlI_vdtar0WF9zk-3mqEzbOLsfVc0s0vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مراسم عزاداری محرم در هند سده‌ نوزدهم از نگاه نقاشان اروپایی
🇮🇷
✊
@AkhbareFori
|
link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/660152" target="_blank">📅 17:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660151">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خرید آنلاین کالابرگ، جای صف‌های طولانی را گرفت/ اسنپ‌مارکت، رتبه نخست استفاده آنلاین از کالابرگ
🔹
گزارش‌ها نشان می‌دهند رفتار کاربران از خرید حضوری و صف‌های فروشگاه‌ها به سمت پلتفرم‌های آنلاین تغییر کرده است.
🔹
در روش سنتی، شلوغی و اتلاف وقت و نبود شفافیت در کالاها از چالش‌های اصلی بود.
🔹
در خرید آنلاین، کالاهای مشمول کالابرگ مشخص‌اند و خرید بر اساس اعتبار موجود، ساده‌تر انجام می‌شود.
🔹
امکان خرید در هر ساعت، حذف هزینه‌های رفت‌وآمد و استفاده هم‌زمان از تخفیف‌ها، از مزیت‌های اصلی این تغییر است.
🔹
تحقیقات میدانی خبرنگار ما نشان می‌دهد اسنپ‌مارکت سهم بالایی در تهیه اقلام مورد نیاز خانواده‌ها از طریق سیستم کالابرگ دارد.
نحوه استفاده آنلاین از کالابرگ
نحوه استفاده آنلاین از کالابرگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/660151" target="_blank">📅 17:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660149">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j_jZPXgdtZSo1NwiFAdN3Mdo-cb5Oi76nO-G-Q5ZDH3YKmALNk6MLtq8XNAfUv9r-_0Nrolt1a24Q1p2SIBzxt-ygade_pKWV_mQp5-UrOccW6bdrkxRDf3sCKv4Ta7f5mMlqjeucyHo0Anrpie5Bc3Idv1A30DtHADcWLW0OQIghyFH4cG3baTUk5O6rKX_bTikWlYJdwlpa6kJIhstdIR9O_ArERztG3QlTJLWeBpJci6oVLKbGotJjsRshxt1VXg7zhgaVNItpBl4QeixTR8m2JkZVDN0uz__vJV1FM73R59G0sbFKDWEwoMjkHHloxQaO3jrKYgTxgAxq6poJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QFsgPm7CzbtjJ9ZSjnjnbh-CM5Jp1_Jq9L4_hqaK-fjY0oF2KiWWh6SGe0pCHLEa_CwzABF_5F4Yot3CjWL7o3KI42ZpOGFtrET9y1JeqzkxynXKN4B7kbmaNze-1A1YViAPDf4DGkGg5q5E_wYnY4tKL_n_o9QKDOS8BtkvyYERTP2WOWNhFOOcieQhvqNlr0USFRHtLhmz5vomU-YLW3Dn2hBV97PdMIMv2v7_pBks-YvtKmTD3MVEmWo9B7xyr86tf9VYWm10aHA-k_8x7Ls6tOFBLge_BPlekfhM6qK7hdwtm89h97AZzzH6liZ8DtS_OEd_BNyKaVG8zghD3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
واشنگتن پست بخشی از مکالمه کوشنر با قالیباف را منتشر کرد
مقامی نزدیک به مذاکرات:
🔹
کوشنر به قالیباف در مذاکرات اسلام‌آباد آوریل گفت: «اگر بهایی مثل رولز رویس می‌خواهید، ما هم محصولی مثل رولز رویس می‌خواهیم.»
🔹
به عبارت دیگر، اگر ایران با باز نگه داشتن تنگه هرمز، توقف غنی‌سازی اورانیوم به مدت ۲۰ سال و متوقف کردن صدور انقلاب خود، به تعهداتش عمل کند، می‌تواند انتظار دریافت صدها میلیارد دلار منفعت را داشته باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/660149" target="_blank">📅 17:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660148">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b33f1d089b.mp4?token=vu24leWpCv8SHguxYGXiezPm2QDebl9zSOmdI9kqRtZF-4fOEHyZj-D2wfYxWpPNKsQzcLuFD1ZGJuKILI6lhgThpYXy08ytvaoGHCHkvVmJw2axi5QLh0HYC-fU7c-if5m851gMqCH5gK4b1zSYeIxmQa52ZOmYsVT9Wn5DCzYB09K7i6CKlYYmlT23hhAswkBIJOSfm3d9w9TufYjxOfkL_GJb3WVgVyUhCFcZmUfz-Jx7YnzChW7G2ddByzRb0BzH5TV3WFju0w68TI9xPb-tbP3yYalyux0bdwqUGWOCK9Ki3xxHCxg8Gq1E1nxnGLTpWYYIzvRhnC6ku7ZDCZDJpBshmxZrk9eDpJl30Wl_epmaL2w_7meTMwvWh82gIY1pnekpAQHfIs5wUeHF0RwT37QF6gySJgidKgOS51aJKklLbFsjT7YrbZq05DDBtcSlVqyoMXOedO6H8OpV_juz29o8rUmrwzQikgFjrFk3K8vC_rMij-reCkfN6-LmmcR8SYcint1ka3fHH4i9_KmZaLHmpyW1gEwrIfT_Qrf56z6yEZWQMSpBBtjeE8vOKCQeQzR_jXVsfmWwNDKebjRExJI0LIY0Ptc_vtOqdLAm6TjdJ7BJZRJrm0M_QeJSaFd3JsPcD14TUgftLSkw2PFalbGRH6XeivFPXgqa-AI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b33f1d089b.mp4?token=vu24leWpCv8SHguxYGXiezPm2QDebl9zSOmdI9kqRtZF-4fOEHyZj-D2wfYxWpPNKsQzcLuFD1ZGJuKILI6lhgThpYXy08ytvaoGHCHkvVmJw2axi5QLh0HYC-fU7c-if5m851gMqCH5gK4b1zSYeIxmQa52ZOmYsVT9Wn5DCzYB09K7i6CKlYYmlT23hhAswkBIJOSfm3d9w9TufYjxOfkL_GJb3WVgVyUhCFcZmUfz-Jx7YnzChW7G2ddByzRb0BzH5TV3WFju0w68TI9xPb-tbP3yYalyux0bdwqUGWOCK9Ki3xxHCxg8Gq1E1nxnGLTpWYYIzvRhnC6ku7ZDCZDJpBshmxZrk9eDpJl30Wl_epmaL2w_7meTMwvWh82gIY1pnekpAQHfIs5wUeHF0RwT37QF6gySJgidKgOS51aJKklLbFsjT7YrbZq05DDBtcSlVqyoMXOedO6H8OpV_juz29o8rUmrwzQikgFjrFk3K8vC_rMij-reCkfN6-LmmcR8SYcint1ka3fHH4i9_KmZaLHmpyW1gEwrIfT_Qrf56z6yEZWQMSpBBtjeE8vOKCQeQzR_jXVsfmWwNDKebjRExJI0LIY0Ptc_vtOqdLAm6TjdJ7BJZRJrm0M_QeJSaFd3JsPcD14TUgftLSkw2PFalbGRH6XeivFPXgqa-AI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری: اگر شما رئیس‌جمهور بودید، هرگز این جنگ (با ایران) را آغاز نمی‌کردید؟
🔹
کامالا هریس، معاون اول رئیس‌جمهور در دوره بایدن: قطعاً نه.
🔹
در نهایت به همان جایی خواهیم رسید که بعد از برجام بودیم و ترامپ آن را یک پیروزی معرفی خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/660148" target="_blank">📅 17:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660147">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
ترامپ قمارباز: به اسرائیل گفتم «بگذارید سوریه حزب‌الله را کنترل کند»
🔹
من فکر می‌کنم آن‌ها بهتر این کار را انجام می‌دهند. #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/660147" target="_blank">📅 17:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660146">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromشرکت گلستان</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhoZdWGjKgYnIFOVMs_7Q2BvCg00PpMdbZOqXXU7UGS2UoPzyHI0Ab4EUnxHRcQvbjDEzdJ_61r1aj7KTjD4h7nkE-JgqzRZc1vev8M_uwjWZNhAlGWH0yCmt9j8VsaUdS3iwQGmJeXiPFCP1dxDg84zkIylEHs57i3qyw9j1CShVSUJMb5fU1ip4YzPNV5f-TU_qPkLxY0X99QLjeDEDyBldqiogfkEreBHI02AtnrKO3W1zacurid1PnEyq5PDYTIzlEs7fMVvdkg1bYc3AdPMP_aQwJ40SfuNZBoeXRfj3Hfl-SP-zUQp4tTqgeK03Ydv5RZmyIvFzJSKbSqWhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مسابقه پیش‌بینی جام جهانی گلستان!
⚽
نتایج رو پیش‌بینی کن، امتیاز بگیر، و جایزه ببر!
🎯
ثبت‌نام و شرکت:
👉
www.golestan.com/worldcup2026
@golestanco
#شرکت_گلستان
#چای_گلستان</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/660146" target="_blank">📅 17:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660145">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2412cf3eb8.mp4?token=IDWfz5iCShjzWYzr3_EP5g2JDjn6nq3vAtu4-MmUR8X95pjkJDkD2boxuT5D5rdJP1pefmFQTJOG33rpVFc5PELBk5B8Ge6u4xIhdcZbYsIAgiks_4ED5io3lPqR9RN_CfEpkHOmLGlmeNoqCD_DKWM6r0How9yLZ29h7sFCIXdJIpIMGksYmH8H4ooNdNRk6NfNUXWYJmHxRmCu7iIo3SY-uGLIMBQDd-Ze7xNLM9ibb6FcqfiHT85CaHu-3qeoQEOvVrarE4uRczRYQahhfFLYPxhYqJX7_1hFpqsiXJECn3iQ0jv1gU0HttZWS08U63wRMv_F4EomemhUL4fidHqqc4E3QucFBcSlwxn-yZyhP2o_7Q_HHrc1UCXf0K3b65D31HdvXFG8SXnkqM4BzRj2_8ZIDXSxzaUkExnQUCkoJe7-Wqf7m-HwfckvAscsOL-2KiWCqon2msTkYdoh7lST2xRTckYq4OsRKH4czq4_tj4ccgDxLWJXzxyyaOILkOu_EII4edTLOfDnUqev9b_ePg1eFE9UGlZk6sOVJkKCjVuevMXarFwr3PLKLLR-MHEX9hI2NvGhzKn8LU3PlN5CgatmrMkPdS_vq7yPTzA6E27TxEouxI4PswNFuYhpI_7QG8l0KkoMOQXCSQMN-VBl3uhwi8BjaUTX_mxcbHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2412cf3eb8.mp4?token=IDWfz5iCShjzWYzr3_EP5g2JDjn6nq3vAtu4-MmUR8X95pjkJDkD2boxuT5D5rdJP1pefmFQTJOG33rpVFc5PELBk5B8Ge6u4xIhdcZbYsIAgiks_4ED5io3lPqR9RN_CfEpkHOmLGlmeNoqCD_DKWM6r0How9yLZ29h7sFCIXdJIpIMGksYmH8H4ooNdNRk6NfNUXWYJmHxRmCu7iIo3SY-uGLIMBQDd-Ze7xNLM9ibb6FcqfiHT85CaHu-3qeoQEOvVrarE4uRczRYQahhfFLYPxhYqJX7_1hFpqsiXJECn3iQ0jv1gU0HttZWS08U63wRMv_F4EomemhUL4fidHqqc4E3QucFBcSlwxn-yZyhP2o_7Q_HHrc1UCXf0K3b65D31HdvXFG8SXnkqM4BzRj2_8ZIDXSxzaUkExnQUCkoJe7-Wqf7m-HwfckvAscsOL-2KiWCqon2msTkYdoh7lST2xRTckYq4OsRKH4czq4_tj4ccgDxLWJXzxyyaOILkOu_EII4edTLOfDnUqev9b_ePg1eFE9UGlZk6sOVJkKCjVuevMXarFwr3PLKLLR-MHEX9hI2NvGhzKn8LU3PlN5CgatmrMkPdS_vq7yPTzA6E27TxEouxI4PswNFuYhpI_7QG8l0KkoMOQXCSQMN-VBl3uhwi8BjaUTX_mxcbHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رازهای باورنکردنی شعبده‌بازی فاش شد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/660145" target="_blank">📅 17:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660144">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
رشد ۹ هزار برابری صندوق‌های سهامی در ۱۵ سال
🔹
صنعت صندوق‌های سرمایه‌گذاری ایران در ۱۵ سال اخیر یک انقلاب تمام‌عیار را پشت سر گذاشته است. صندوق‌های سهامی، از ۳۱ میلیارد تومان در ۱۳۹۰ به ۲۸۷ همت در خرداد ۱۴۰۵ صعود کرده‌اند.
🔹
این صعود یعنی ۹,۳۸۰ برابر رشد، عددی که سهامداران را به وجد می‌آورد. قهرمان بی‌منازع، صندوق‌های کالایی هستند که از یک نقطه‌ تقریباً صفر به ۶۶۶ همت رسیده‌اند. این یعنی ۷۴ هزار برابر رشد!/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/660144" target="_blank">📅 17:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660143">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
ترامپ: کلمه به کلمه متن توافق را برایتان می‌خوانم
🔹
من نه تنها آن را منتشر خواهم کرد. احتمالاً یک کنفرانس مطبوعاتی خواهم داشت و کلمه به کلمه آن را برای شما خواهم خواند تا مطبوعات آن را به طور دقیق پوشش دهند زیرا این یک سند بسیار مهم است. #Devil
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/660143" target="_blank">📅 17:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660142">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Um9x7V9nGQmGpanN4x_4_Fd6AfnCZ08xfq_Q-OUcayMkEP9u1zsOoKmte9z9phUaLe7FgIG3oa05HuqvDfOcDhO-wrB-eTXKTlUgxGrgkovI16pcEx75hXfnNDtMMgJQsbDvvR9ZpoG6_cVpfKf6pTtnBzsff_LqJO1pvCj1DSQiUwpWUo0L8Jy3wGrDD8mGIaXmioisOrUDoWZKrj9CzV9tO_g_-4rLyHGacAbzzx1IuqabyaJtfhKazSqmq2MiH_pe9kAuvZPodisi-8pDBfD7ZqSC0ppdJYoYVVOdCqu914feR7iUTOqdvyhOzFdOjGzI-s8_L8CMPqzvDnYywQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
زرگر سرویس سپرده‌گذاری طلای ملّی‌گلده.
شما طلای خودتون رو برای یک دوره مشخص سپرده‌گذاری می‌کنین و در پایان دوره، سودتون رو هم از جنس طلا دریافت می‌کنین.
یعنی بدون اینکه طلایی بفروشی یا از داراییت خارج بشی، طلات می‌تونه برای خودش طلا بسازه.
✅
۱ ماهه: ۰.۵٪ افزایش وزن طلا
✅
۳ ماهه: ۱.۷۵٪ افزایش وزن طلا
✅
۶ ماهه: ۴.۵٪ افزایش وزن طلا
✅
۹ ماهه: ۷.۵٪ افزایش وزن طلا
✅
۱۲ ماهه: ۱۲٪ افزایش وزن طلا
طلا برای خیلی‌ها فقط یک داراییه.
برای کاربران زرگر، یک داراییِ در حال رشد.
🏆
و یادت نره؛ تا پایان خرداد هر هفته به قید قرعه یک شمش طلای ۵ گرمی هم به یکی از کاربران زرگر هدیه می‌دیم.
🔗
زرگر؛ به طلات وزن می‌ده.
🟢
ملّی‌گلد؛ پلتفرم امن خرید و فروش آنلاین طلا</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/660142" target="_blank">📅 17:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660141">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
سوئیس محل امضای تفاهم میان ایران و آمریکا را مشخص کرد
🔹
وزارت امور خارجه سوئیس با صدور بیانیه‌ای رسمی تأیید کرد که مراسم امضای توافق‌نامه میان ایالات متحده و جمهوری اسلامی ایران روز جمعه برگزار خواهد شد.
🔹
این مراسم در مجتمع «بورگن‌اشتوک» (Bürgenstock) در سوئیس میزبانی می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/660141" target="_blank">📅 17:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660140">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
پارلمان لبنان: نقش ایران در برقراری آتش‌بس در لبنان غیرقابل انکار است
🔹
قدردانی پاکستان از نقش چین در تسهیل گفتگو بین ایران و آمریکا
🔹
ترامپ: ممکن است تحریم‌های نفتی روسیه را دوباره اعمال کنیم
🇮🇷
✊
@AkhbareFori
|
link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/660140" target="_blank">📅 17:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660139">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 به نظر شما مهم‌ترین سرمایه ایران چیست؟</h4>
<ul>
<li>✓ مردم و سرمایه انسانی</li>
<li>✓ فرهنگ، تاریخ</li>
<li>✓ منابع طبیعی</li>
<li>✓ ظرفیت علمی</li>
<li>✓ هنر و ادبیات</li>
<li>✓ موقعیت ژئوپلیتیک</li>
<li>✓ سایر</li>
</ul>
</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/660139" target="_blank">📅 17:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660138">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a279890145.mp4?token=GqapVkilYfYJtxcfdYWY9vTe3gbJ5wcKRznQxYfQbhhsXWmxv0YMGZiNT_VMWIroJj36ex-SsOEcsx4QSG6DT1LRrohnEQN7hIHfde7HwWGKomFBXueIjzDTATfqFsU_WwO-b8nL3Uf7OlWSmiWfBh22zkZ8dyPBdTT-kSgvRiwFHg8m0HgajQYN5mWN9jLm8JWHrJHcnCF9hpyFdDNM9Rkyk59lYey_d4BQtVmj5fPjeRdlvzOxWav3NQ3OHC1tdME2TOxmO93XvXATwUBh_A55ySAH_ULpPsAJY8E0kxq9av_JKOXbz-uJ5iWZaQWTFYpME45yqZFZDV7KaNqWsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a279890145.mp4?token=GqapVkilYfYJtxcfdYWY9vTe3gbJ5wcKRznQxYfQbhhsXWmxv0YMGZiNT_VMWIroJj36ex-SsOEcsx4QSG6DT1LRrohnEQN7hIHfde7HwWGKomFBXueIjzDTATfqFsU_WwO-b8nL3Uf7OlWSmiWfBh22zkZ8dyPBdTT-kSgvRiwFHg8m0HgajQYN5mWN9jLm8JWHrJHcnCF9hpyFdDNM9Rkyk59lYey_d4BQtVmj5fPjeRdlvzOxWav3NQ3OHC1tdME2TOxmO93XvXATwUBh_A55ySAH_ULpPsAJY8E0kxq9av_JKOXbz-uJ5iWZaQWTFYpME45yqZFZDV7KaNqWsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: کلمه به کلمه متن توافق را برایتان می‌خوانم
🔹
من نه تنها آن را منتشر خواهم کرد. احتمالاً یک کنفرانس مطبوعاتی خواهم داشت و کلمه به کلمه آن را برای شما خواهم خواند تا مطبوعات آن را به طور دقیق پوشش دهند زیرا این یک سند بسیار مهم است.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/660138" target="_blank">📅 17:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660137">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVEkQJfxkMB9aAu-S2qg0M5Rt_z0G6uZbH5kbArXzDgeif1MnoAd1Tn8NfzdfU1hhtIU181fWvwNAvSO-LUqhoQMZQ6YJw9YhrVJIpQe7muxmq2capYXoBz4UbakYYsaAbqDPpEGUglXWHZjsQxL_nwulEApT_v3cw3afI_HOFO2OnI6jWDhXW0ElCWBLKrCkb5A5qUiPrdTAweX8Ok-TxJfochxfAZkyTrKTixquxgMp4jcz1B2jleWXuNbaJvDEyDOlSyHPVg3B8b9zkQnjLzG1biWe8-vld0J_8tU8hO1KSY9PAUEGZ3eP1EBfyNh3pCqvPvDJcyumF9W7m7D0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقدر فوتبالی هستی؟ ۵ گیگ اینترنت رایگان ببر!
🧠
⚽️
همراه اول واسه جام جهانی سنگ تموم گذاشته. به تمام اونایی که مسابقات رو پیش‌بینی کنن، ۵ گیگ اینترنت کاملاً رایگان هدیه میده؛ بدون هیچ قرعه‌کشی!
فقط کافیه وارد اپلیکیشن «همراه من» و بخش «زمین بازی» بشید و نتایج رو حدس بزنید تا بسته‌تون فعال بشه. تازه به جز این، کلی جایزه هیجان‌انگیز میلیاردی دیگه هم واسه بقیه پیش‌بینی‌ها در انتظارتونه!
📱
لینک همراه من:
https://www.mci.ir/-4S0XAJB</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/660137" target="_blank">📅 17:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660136">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
پلاک منطقۀ آزاد تهران به چه خودروهایی می‌رسد؟
🔹
در مرحلۀ نخست فقط خودروهای
حمل‌ونقل عمومی
می‌توانند از ظرفیت منطقۀ آزاد برای واردات و نوسازی ناوگان استفاده کنند.
🔹
این خودروها با پلاک منطقۀ آزاد و با هماهنگی پلیس راهور، تنها در محدوده و شعاع حرکتی مشخصی که از سوی مراجع ذی‌ربط تعیین می‌شود، مجاز به تردد خواهند بود./ فارس
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/660136" target="_blank">📅 17:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660135">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QibrtOhh-ay9IYwGdtA_RhrYHe-8KbSLGbERT2MTtZtu8BskPLyP82Twh3r8VkvgUyaH2VfxeUBjje3165Cz6Fmjtkeg6V9NVQaY_AdXtl5yyLJXgDjCKwcg1awxr66lCKYcynYxNDpw6dJiItiNw5ruIjLKI-5_f9r85Ju5SDsxcIYfp-QJzVOi5nIQRkGtwvbrXMfCn5vM6IEbsqLJLsmwDdYCeUs_M6D1dLetj0d3CicuiZKEfkM0lwdVlXPWr6AvkS1mlZl-gePeZ1JZ6S_s6W7kjv8zAxQZxcyaopPryrixX31en9qMGqGeeeW18w3Frfh_iYuGH5Tk7msquw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این تصویر قديمى ترين معدن دنيا و گرانترين غار ايران است؛ معدن فیروزه نیشابور كه سابقه بهره‌بردارى از آن به بيش از ۵۰۰۰ سال مي‌رسد
#اخبار_خراسان_رضوی
در فضای مجازی
👇
@SedayeKhorasaniha</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/660135" target="_blank">📅 17:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660134">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سعیدی:
به هر میزانی که آمریکا محاصره را بردارد، تنگه هرمز باز می‌شود
!
بهنام سعیدی، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
اگر ترامپ بخواهد یکی از این بندهای تفاهم را اجرا نکند یا ناقص اجرا کند قطعا روی کل تفاهم اثر خواهد گذاشت.
🔹
آنچه که ترامپ یا معاونش درباره بحث تحریم‌ها مطرح می‌کنند به نظرِ می‌آید بازی‌های رسانه‌ای است و گرنه مفاد این تفاهم مشخص و هر دو طرف این را پذیرفته‌اند. به هر میزانی که آمریکا محاصره را بردارد تنگه هرمز باز می‌شود.
🔹
نکته مهم این است که این موضوع با ترتیباتی همراه است که جمهوری اسلامی ایران مشخص می‌کند؛ یعنی مسیر و نحوه عبور از تنگه هرمز را جمهوری اسلامی ایران مشخص می‌کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/660134" target="_blank">📅 16:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660133">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
ادعای ونس: توافق ایران و آمریکا مورد حمایت سران منطقه است  جی دی ونس، معاون رئیس جمهور آمریکا:
🔹
طرح ترامپ برای حل مناقشه با ایران از سوی سران خاورمیانه مورد حمایت قرار گرفته است.
🔹
ونس در ادامه اظهاراتش مدعی شد که اگر تهران به دنبال سلاح‌های اتمی باشد، آمریکا…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/660133" target="_blank">📅 16:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660128">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TShSenGa23Y9Gr-oXHbVj0wjkCpyDEqaPfe-UT1KOWAw0jzAv-_UowxkenV1MwnWxJJW_PCOyPpFUf75p-PKsCSFxZ7kAQyRL9ZxG5qKWOiVnnFIxoqZ4fOlLZbzr3udw4cM4PvvqGFCeJ9s-lOc23LFkqCMv1C_9PsrP2ILm5gFOebX9dkpVLn-y5-rp7PC9WbgMYMrxJD3f9zjC-Gl_kpPRIksYurOksfMmznxf-XRSIwu8AXA2V8itRRWx1ErTdy82KnUbGHDGvCdQVWNBVE44_jKrdkjZ9ZRvH-5dUPO-1V5lV_g-0whoIBqmpXTLxb7MioxiWhLrXxjX6FaEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ev0XfawUb70kh16pFWWPmq85nbF3HcEvvL8W7JxR_CstST6B4HEion0pHLviQiJyhs7F1bG33adJ3UpgK8hyHujx-fmjn4x6rNyY_JcFSUsyPz9BBf3rWwOVbNGZwjNrHHaxLFe6tiRdht17SaAXHl2zEM7dKpkxunBkBmc2l0mJL31LUvMvcCe5vKBiX7Cg3RMXDJCTrA8dYOn8AdPEUbcEUp3XH-URlVD4hLmT_fTm36WSiEF_sdeCsnPTGHWhxx3f9eIcs5kMWI6KVplH0xlCVHoOzIGdRfZxjQnqFinTDiHntXQBZF_JV1FbXVmFWLekb5lH17rtfZJutzJCkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eA9fi2Rp5CwoTdjPsd8pwzUFQRXb_zTDmrwkRh5vAOsalu6MASbW48E-3cCM4-adEzyqylu73iE-THAMypKjXDk5fXwhNL4ayjaECMtn4YyVi6wARrX_BZ4o2ZBulAX2s0Db4uCfrm_w7sNIg2-HbJiJf5mkpLD_RXcvsHdmIRZ6UZAffsenZZ880QHWuh3cWnX3-WN_eRC3tUEKJHi3Gm7a0fz6b7Hsv3238mYEfg9vJwn33OllxvBCH_iMxYCLj4lUgO9eThJ1mFkIUI9MZb7Kh8z1vu3jroYE9sAwRU9GCkWXP3nKTD8VVSPYHoS3l0V-UELyld2eFVJXJaRNdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l9IbwUSrfUUAsDbLaTBL6puvKgCNRuwb4lYWCjWc0HYoWEMHsfWHv5bKxJ3aDIaKcUY6S4p5XefMO5axysHUx1mBmMqbdboJrPTtrRJ4RjWybc8J31nmeorD52cq-xsrdjiKWLBv5O96sK71D_rbU5dy5QVqcEbsQ3-JCBIlzHprOx99_5-Kw0MUwmPBHzQwf_mK6fDuIoXtyauFkhAKEOuQSihzL2eadEY1vkHyWSUpJGDYvDFh-RlIcX7Tal39XC0n2OYRxRtW134MmY0WbUGwFOlwHX8eHFYoO92QrvBsAS4TAQClbzWbK18OfzCytGUY6XJyR6JYj-Fs8ftxyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r3JYON_-4jD2EOTX8QR5GDhLJZ7Jt3CQ7DYw_KepsKM2SWARziWlae7stxgM6Gfxr1l8GYVKlMh_nBKkAtIC1ATDPV6pwe_x0AyiKmfFtrWix5h1XfkwlcugcA_uHh0-NgUmO-qLzGC4H2F9ro3I9LTvXcFmltYtsY7QTzUVY-dlDpmu9M-MaQhRKILGbi8fcKxTbczeLR3OoqRTPRXBOL8EtRt_p51cGGXEYYrpJIPXWcYOzzhCgM6-3z0OGTFpaWs-rUdNLaBbbgdSNvy0FkzFR-3uJ7ztL10GduubS1kht46hJypLGIwsJGRavBMizixo4nr6iP9IS0dzgJQnmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
با این ۷عادت ناخواسته سطح مالی شما تغییر می‌کنه #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/660128" target="_blank">📅 16:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660127">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
مخالفت آمریکا با دسترسی اسرائیل به جزئیات تفاهم با ایران
شبکه ۱۲ تلویزیون رژیم صهیونیستی:
🔹
علی‌رغم فشارهای مکرر مقامات تل‌آویو برای آگاهی از محتوای یادداشت تفاهم اخیر میان واشنگتن و تهران، ایالات متحده با این درخواست مخالفت کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/660127" target="_blank">📅 16:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660126">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
ادامه اختلال‌ در ۴ بانک؛ وعده حل مشکل در سریع‌ترین زمان ممکن
🔹
شورای هماهنگی بانک‌ها بار دیگر با انتشار بیانیه‌ای از مشتریان چهار بانک ملی، صادرات، تجارت و توسعه صادرات عذرخواهی کرد و به آن‌ها وعده داد که در سریع‌ترین زمان ممکن، اختلال‌های موجود در این چهار بانک حل می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/660126" target="_blank">📅 16:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660123">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHI1CFWbXN5F8cCDplkhvgoPiPFbj-nkKGf0WcbivnSOvXBdd6EukVDi5R9cVNjg6hTZEeWchWYT5kKZGRCH_oMHcmyYU7hr-oghKIvkTGK43oxalZT2DBAz4J_IQdbxVNwpGFELv1TXNqDiJL1PwUrkamwroAQ2CtaiE8KyJsyHhvmAveMdY6gFazeCIAP10dEwq-DEbNSEAjIEl9KvEhtiyNhbW8CQxMdG9h2NAjGdKrv112nXAOL0iUJwNtW5NhOrZ_CKq6Ic1l_UN_EydHCubOCPKdfhVqVPn-MK_PRSqk8HPiPf0t1OPkM7ttdqw9nq-EIp2UZCA4eXkv44qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/756924cbaf.mp4?token=E9DstI_NdvAsPinNynoEMsAtzVgozoOTIPE4FXDqve7OVxram9ToZixgSV1cxbWHRqRNPQjAoSHsxweoPTuHFjqZ2hmv5IBQt0ZYKfTFYDxZeIi9pgVDWU-kYZ3b-JX-F1HGUTaveDMi6JQSSn9buTXq_Pv_zD2XHGRrnPusxsK3GPnlogsaE0WnbWK9CGzHt-FEakhdJQ262h7lrlFennkMsRpuNfaXORLgQkN-GsVz9NfdQLKcIOArL3DeMGYlcCEctLR_7E8W_N6TjWhA-D_grCYqIK2pjFWaITLiPGBlFZSeOz_PHntOiqtre9yNx0s5XkZI_7BEwN_d7ZJFaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/756924cbaf.mp4?token=E9DstI_NdvAsPinNynoEMsAtzVgozoOTIPE4FXDqve7OVxram9ToZixgSV1cxbWHRqRNPQjAoSHsxweoPTuHFjqZ2hmv5IBQt0ZYKfTFYDxZeIi9pgVDWU-kYZ3b-JX-F1HGUTaveDMi6JQSSn9buTXq_Pv_zD2XHGRrnPusxsK3GPnlogsaE0WnbWK9CGzHt-FEakhdJQ262h7lrlFennkMsRpuNfaXORLgQkN-GsVz9NfdQLKcIOArL3DeMGYlcCEctLR_7E8W_N6TjWhA-D_grCYqIK2pjFWaITLiPGBlFZSeOz_PHntOiqtre9yNx0s5XkZI_7BEwN_d7ZJFaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«جنین جنین»؛ مستندی که دوربینش از گلوله‌های اسرائیل جان سالم برد؛ اما تهیه‌کننده‌اش نه
🔹
«جنین جنین» (Jenin, Jenin) روایتی تکان‌دهنده از عملیات ارتش اسرائیل در اردوگاه جنین در سال ۲۰۰۲ است. فیلم‌بردار و تهیه‌کننده اثر اندکی پس از پایان فیلم‌برداری در جریان حملات اسرائیل شهید شد. این فیلم به یکی از جنجالی‌ترین اسناد تصویری درباره رنج مردم فلسطین، مقاومت آنان تبدیل شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/660123" target="_blank">📅 16:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660122">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnF-s9CFOUaG3-94ZJOpXkcFvkw3ifHznvbFfRBqa1PoLDY10-Bun9rLptih14IAw0ycYaQOu4TLovbqXzAP2tjk9ol49wj5RyAiYgxL5pODhEOx87FEIVe3_UNMvPxQkiEeSvkVqAaPIOAz6wxX2ZJuojsKkZSdiAxK6Rx7aNc4ggRnVYUOXZ1eoaZ4ivbbSCAh59cuDewU5DUNzgH14e_yhqFHtSaOS0bfYD6baOE5vKY91dBQv_gslBpNXyMEaxKINXG3Alj_PB2oRecDeacQ81OkM7U531R_43YsL8_o5EkyGdTEaqqGqtva0tJ_TKcx-K9xTWbFgUtoI7MXvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا ۲۰ درصد سوخت‌رسان‌های خود را از فرودگاه بن گوریون اسرائیل خارج می‌کند
میدل‌ایست‌مانیتور:
🔹
ارتش آمریکا پس از توافق بین واشنگتن و تهران برای پایان دادن به درگیری، در حال آماده شدن برای خروج ۲۰ درصد ( ۷۲ هواپیما )از هواپیماهای سوخت‌رسانی خود از فرودگاه بن گوریون اسرائیل است.
🔹
کانال ۱۲ اسرائیل: «این اقدام پس از آن صورت می‌گیرد که واشنگتن و تهران بر سر یادداشت تفاهمی توافق کردند که راه را برای پایان دائمی جنگ هموار می‌کند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/660122" target="_blank">📅 16:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660121">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
ادعای
ونس: توافق ایران و آمریکا مورد حمایت سران منطقه است
جی دی ونس، معاون رئیس جمهور آمریکا:
🔹
طرح ترامپ برای حل مناقشه با ایران از سوی سران خاورمیانه مورد حمایت قرار گرفته است.
🔹
ونس در ادامه اظهاراتش مدعی شد که اگر تهران به دنبال سلاح‌های اتمی باشد، آمریکا به توافق صلح پایبند نخواهد بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/660121" target="_blank">📅 16:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660120">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
خبرنگار الجزیره از حملات هوایی رژیم صهیونیستی به چندین منطقه در شهر النبطیه در جنوب لبنان خبر داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/660120" target="_blank">📅 16:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660119">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a799d3ee3c.mp4?token=aV4OTRRc13bdXrjtaXd-SJcCqhulXxico1CgbIBwSmMNF815sCmaNGAqkQrx7UzNy8Cu2dcI61tW8CAEw7tBGjX8kyuQS39omvNDwBWxSPXSYXQI_iR4Gp83MQnro7lSyBD7G3qyau1RQOiR_qZka14sAm7ymFblQBdC6eI4X7zSPPq08lkyMSKBt6Uy30udYnGKtaS7Me1NrplXOqyLkYqSIp9tedzEl_-NAMKglutj4DFze5f6RGqCVMhQe9XHtwDDbX1v76NuLHwP-aqfrPG_zz8Grl4WgZ1d5H-zUNcxk2wpMv6flTiCmzYgNGgBH7WejtNJ0j0hKWifyuxUyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a799d3ee3c.mp4?token=aV4OTRRc13bdXrjtaXd-SJcCqhulXxico1CgbIBwSmMNF815sCmaNGAqkQrx7UzNy8Cu2dcI61tW8CAEw7tBGjX8kyuQS39omvNDwBWxSPXSYXQI_iR4Gp83MQnro7lSyBD7G3qyau1RQOiR_qZka14sAm7ymFblQBdC6eI4X7zSPPq08lkyMSKBt6Uy30udYnGKtaS7Me1NrplXOqyLkYqSIp9tedzEl_-NAMKglutj4DFze5f6RGqCVMhQe9XHtwDDbX1v76NuLHwP-aqfrPG_zz8Grl4WgZ1d5H-zUNcxk2wpMv6flTiCmzYgNGgBH7WejtNJ0j0hKWifyuxUyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ: توافق با ایران را برای بررسی به کنگره خواهم فرستاد #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/660119" target="_blank">📅 16:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660118">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
تردد بیش از ۴۱ میلیون وسیله نقلیه در کشور
🔹
بر اساس آمار پلیس راهور فراجا، تعداد خودروها و وسایل نقلیه درحال تردد به ۴۱ میلیون و ۲۰۸ هزار دستگاه رسیده است.
🔹
در این میان، خودروهای سواری با بیش از ۲۲.۴ میلیون دستگاه بیشترین سهم را دارند و موتورسیکلت‌ها با حدود ۱۳.۷ میلیون دستگاه در رتبه بعدی قرار گرفته‌اند. کمترین وسیله نقلیه در ایران آموبلانس‌ها هستند که تعداد آنها ۱۵ هزار و ۴۳۹ دستگاه است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/660118" target="_blank">📅 16:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660117">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUN0ZBkmcF9oe-GLM0AodAwC-SzYu8HHR7hszO-jQjrbxq-_FMV7HQ22rOY__4JPAhGV9_nif9ZOdpbdBE8Ykko2t8Y886ZgShOHJLIqgdKrqY87d4D2r7piY2Qhmi1PeKF7_L7_W-44ZXwJdpwJfmY-3jIYDC7G1U_nn-VluwRFf8Xzz_70etOn47Ci_qU45Vn_rRbm5hbAi9T82kztv3J2cO_OsijypVjpCjPik3i9rXFEotfSckXoZb2ao_nrEncuYgGyeeYe9DJUeC0XkPil7P_d5lSHm656BG1EdzqbKaIc8SuY9jQMWktz-Ecs5ifEInuBdEbsY_iryw4row.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ثبت‌نام بیش از ۳ میلیون نفر در بازوی «عدل ایران»؛ ارائه خدمات قضایی قوه قضائیه در اپلیکیشن بله
بازوی رسمی قوه قضائیه در اپلیکیشن بله با عنوان «عدل ایران» با هدف تسهیل دسترسی مردم به خدمات قضایی و حقوقی و کاهش نیاز به مراجعه حضوری، تاکنون میزبان ثبت‌نام بیش از ۳ میلیون کاربر بوده است.
به گزارش روابط عمومی بله، «عدل ایران» به‌عنوان بازوی رسمی قوه قضائیه با آدرس
@adliran
در این اپلیکیشن، تاکنون چهار خدمت اصلی شامل استعلام اعتبار معاملاتی، پرداخت شناسه‌دار، دستیار حقوقی و دریافت گواهی سوءپیشینه را در اختیار کاربران قرار داده است.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/660117" target="_blank">📅 16:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660116">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
تشکر ویژهٔ شیخ نعیم قاسم از مردم ایران
🔹
شیخ نعیم قاسم، دبیرکل حزب‌الله، در نامه‌ای به محمدباقر قالیباف از حمایت‌های ایران و گنجاندن بند توقف عملیات نظامی اسرائیل در توافق تهران-واشنگتن قدردانی کرد.
🔹
وی همچنین در سخنانی تأکید کرد که ایران بدون هیچ چشم‌داشتی، تمامی امکانات لازم برای مقاومت و آزادسازی لبنان را فراهم کرده و اکنون با تحمل تبعات مقابله مستقیم با رژیم صهیونیستی، نماد عزت و شرف است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/660116" target="_blank">📅 16:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660115">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: تنگه هرمز تا جمعه کاملاً باز خواهد شد
🔹
ایران می‌خواهد این کار را تمام کند و به سر کار برگردد و رابطه جدید عادی است و فکر می‌کنم همه چیز به سرعت پیش خواهد رفت. #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/660115" target="_blank">📅 16:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660114">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
چه کسی می‌تونه ترامپیسم رو شکست بده؟
🔹
برخی دموکرات‌ها از همین حالا برای ترامپ و تیمش در انتخابات بعدی ریاست جمهوری آمریکا شاخ و شانه می‌کشند.
🔹
به نظر شما کدام‌یک از چهره‌هایی که در این ویدئو می‌بینید می‌تواند از پس آنها بر بیاید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/660114" target="_blank">📅 16:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660113">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
ادعای
اسرائیل هیوم: ترامپ در حال بررسی پاکسازی مخالفان توافق با ایران در دولت خود از جمله وزیر جنگ و رئیس سازمان سیا است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/660113" target="_blank">📅 16:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660112">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
ادعای
اف‌بی‌آی: طرح حمله به کاخ سفید خنثی شد
اف‌بی‌آی:
🔹
یک طرح گسترده برای انجام حمله در کاخ سفید همزمان با مراسم تولد دونالد ترامپ را کشف و خنثی کرده است؛ این حمله قرار بود در حاشیه رویداد ورزشی UFC انجام شود و شامل استفاده از پهپادهای انتحاری، تک‌تیرانداز و یورش موج دوم افراد مسلح به دروازه‌های کاخ سفید بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/660112" target="_blank">📅 16:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660111">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: تنگه هرمز تا جمعه کاملاً باز خواهد شد
🔹
ایران می‌خواهد این کار را تمام کند و به سر کار برگردد و رابطه جدید عادی است و فکر می‌کنم همه چیز به سرعت پیش خواهد رفت.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/660111" target="_blank">📅 16:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660110">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoboaUTjwCUXtbdaTCngaeiP86-1lUpDrEFTHxSM8n1PGRW5e5vladNOvo5dE4E-DzhaRgVj8nkL5uFcaKfZdeO6WRR0LA7-_vjSOTWeU71VtDzA3hhzEdf3CFatQhtZB8noeMjqjOhHd08bnD2aYS0P8TYbJiruXo1FQvpzFwpGXSeOBH0uf1M8VdZdg4QsY7Rr0GawCKo1RFIZriOaWwkFrn3_nbW00V_CfIS13_PYjlkcjz4-PB6D6Jvj-s7QKC4O31E_Qs4kpF3RHECrASyJQDL5_iAlhiH1KmEqsJp96-N8u3BVqX5F27FGILNRNKvI2Y5uUEXKSc4eqnkKyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مایک آدامز: ترامپ ناخواسته ایران را به قدرت جهانی تبدیل کرد
مایک آدامز، نویسنده و فعال رسانه‌ای آمریکایی:
🔹
ترامپ در تاریخ به‌عنوان رئیس‌جمهوری ثبت خواهد شد که به‌طور تصادفی ایران را به یک قدرت جهانی تبدیل کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/660110" target="_blank">📅 16:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660109">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-hilBBT5N1TIVxbUzc0mnmUbDFRHthHy1Et151viMsKcD4eXLaKQKvKFusrbtHiBEe-qDjuPSiLYLUpkyi7t4_S1eKesjHd16w5cZhKJybVwq8s3l86M4MYrYfOzEWuFU4iKUXJppEniYo_7cD8sRvwF86_bCFTympwy5snDqNpEwBR8rF4Yk52sag8ta8Qe9PnV1CuMV1qieHypss34OMMwoIH-_DI5fkGmOLImEPVZTmzp8ptNT3CGqUpvhkKXOa10datKot8g2mmc14luTawPBs-5SHrhu99GZtKzQp98lpVwHAcR3-NTt68lP34YfA-rZWWUZ9lKgrq-33XLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط یک ثبت‌نام تا PS5
بین 1000 نفر اولی که در سامانه کیان تریدر ثبت‌نام کنند، یک دستگاه PS5 قرعه‌کشی می‌شه!
با «کیان تریدر» دریافت اعتبار برخط، ابزارهای پیشرفته تحلیل و نمایش دقیق پرتفوی در دسترس شماست تا مسلط و بدون پیچیدگی تصمیم بگیرید.
ثبت نام:
🔗
kian.trade/kt
#کیان_تریدر
#کارگزاری_کیان</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/660109" target="_blank">📅 16:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660108">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnJPblc-9RA9KdaldcacdgV7qSzG6uspm3fgeJ6YCk87MVYlfeNf3xlgQVET1Ku1TOyMjXzDIHX1U-ikhOxO7e242GtzEsWZ1Tjdi1lhip5XJUM6OlYZm6CjI3puBZ3Y_abzrbsBxI_uzxlmnbKkgfllI6UHxw7i653AVxYoS397zncReChuRVs_kXAfzAHaLHb_NfDmhcloc8lK3euBukZwqZGw12C1oPHo0peKkZaksrHBFyVExqcocbMnSTWS_WeAgxLDNYunolxqiVEqmGix2NStShNCuIPPBrlmKSfW7Wa_-i1txjIoPxxFvdOilcpC-Yb0deIy1MQNgC_bwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«تراز تجاری» رو زیاد شنیدیم… ولی دقیقاً یعنی چی؟
#واژه_کاوی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/660108" target="_blank">📅 15:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660107">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMtDakpJ3SHyQDuXGPQFphKZK6FkF9HFS577OTysbTXgA7PTq1RhQIFi-G3xSbFjlKSwJASjmDLWhiATIhKC377r1PMPy00S46gOizj-ibflHO9-w8uz9Twq1feD8ExGkdMw_pjeS3yoEWvPRbkPMbzYJ8tsL2Zz7rF30VWJzii5HXcoJFegmo9mKhMWIJZML-iybKP_EtSzBDn5ydzMku965iRkBUZNfugR6Zdehnfe7FGaAYuKNco8cZNdjmU3CLnlfp_XSuldzROH2U7W9zzWh4KI9xvmevjIq8Zrgeqd6xr2yJYhxdP2AWfvNobl2b7gqSf3V2vjPStg4yNolw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تغییر در الگوی تماشای فوتبال
🔹
در این نظرسنجی بیش از ۳۷ هزار نفر شرکت کردند که سهم تلگرام حدود ۱۲٪، بله ۳۰٪ و روبیکا ۶۰٪ بوده است.
🔹
بیش از ۴۵ درصد شرکت‌کنندگان بازی‌های تیم ملی را از طریق تلویزیون و شبکه‌های داخلی می‌بینند و حدود ۳۰٪ هم پیگیر فوتبال نیستند.
@amarfact</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/660107" target="_blank">📅 15:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660106">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
احتمال وقوع سیلاب‌ در ۸ استان کشور
سازمان مدیریت بحران کشور:
🔹
از روز سه‌شنبه، به‌دلیل فعالیت سامانهٔ بارشی شدید، احتمال وقوع سیلاب ناگهانی، طغیان رودخانه‌ها، آب‌گرفتگی و رعدوبرق در استان‌های آذربایجان‌غربی، آذربایجان‌شرقی، خراسان‌رضوی، اردبیل، گیلان، مازندران، خراسان‌شمالی و گلستان وجود دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/660106" target="_blank">📅 15:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660105">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KoTRk7k2CLq3z4l28FsxEO-s9q6vzM3hMtkme2vEzkVo1U1fK9r4-C3gky6qJqJRrgcNIuvnTbxCvzWfwoFpWl3BTNwS1ISfjD_3eiycv8n7Dq4ImiCdUhBYcCgpgkZMyzleHa3Css68K7qCPdiQNEQJkoWIzMLaKGF6WwNGeMI7L6XrVDnbafbxcWrqA9LXh2ydbm_XDKK26oK6lQ55a2gVog_DK3hOreRT10zbFMj0sZGQzUXUta2JiQJOV8ogwPRAWVcM5_k0IepO5knzl6aKzv7kKATEdr0rxyrzUnrqccZhQG4Mu8pNlIHxyveTkdTHOEB-cLJXRwHutnmIfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک‌تایمز: ترامپ به ایران باخت، بد هم باخت!
نیویورک‌تایمز:
🔹
ترامپ با آغاز جنگ با ایران مرتکب اشتباهی بزرگ شد و این درگیری را در نقض قانون پیش برد.
🔹
آمریکا از نظر نظامی، دیپلماتیک و اقتصادی تضعیف شده و هزینه‌های راهبردی آن را برای سال‌ها خواهد پرداخت، در حالی‌که ایران از جنگ چهارماهه به‌عنوان پیروز راهبردی خارج شده است.
🔹
آمریکا با وجود استفاده گسترده از موشک‌های دوربرد و سامانه‌های رهگیری، نتوانست ایران را به‌طور کامل شکست دهد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/660105" target="_blank">📅 15:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660104">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1Yyo9VOPcvO2RF4vi6sLpRFH1JRgajzocTHeMgcLhOjkYxqsohC53RVqIspc0nqLkdgPPQtT4naL6lKx2eoKu78GMN_9JUbKDF5nIVpLIlURKKFOIzXdIqVuMIV4OcJX8m2zarNJqaPFygTcXZrhI_LImvgrHk5Bhhb-HDHJ2QXDlU3Wy9IhC4R-FLMyB_glekiuU6VjpviGeDN8vX3SNUoJMnoRBoVTs684-gVywdpQtKJpPDHG7ZGtPbeQSamPLo0jvN-PeTlSUfHpYokyU0fyjDa56I1nJyEHZBPMryG_847d-z2tCtbxOs4r3f30sw7PJs4lXQxoFOqp6mPKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور رامین رضاییان در تیم منتخب جام‌جهانی تا به اینجای جام
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/660104" target="_blank">📅 15:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660102">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfmQ6cOKcmjFZEVvsJpWwJ4vWymWWB-Ga-PbCb5xfegh1xXNKeMHwRaysPhHoRoHLbGizAFb4JED-nO439zsKpsUKzoa-fRqCSKi8oM7ZG-UY73ZZFW4bEx6mVODMlS0c_2gu183A4-OQiZHg4mY4M8AVRTUi_qN2ATd9_jzVeID5lIuHRnbVlQxNbl3kzqFHgSvbY6MABmg_bOejkycquv0exbVrv8LzhzYgpcoC9YCMcByLkK7dW_JAiWJWCcA08TDJ70rGSkbdo4ica-5gKz9ixc5FmwZKPrBBMVqjGGuumj1WfG3TW_-CtYUrfgCb-5RIdn8k70OJrVLzb1Z8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنایه توییتری کاربر آمریکایی به ترامپ
جکسون هینکل:
🔹
ترامپ اولین رهبر در تاریخه که یک کشور رو ۶۰ بار «شکست میده»، و بعد مجبور میشه ۳۰۰ میلیارد دلار بهشون پول پرداخت کنه.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/660102" target="_blank">📅 15:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660101">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
گفت‌وگوی تلفنی قالیباف و نبیه بری
🔹
محمدباقر قالیباف و نبیه بری در تماسی تلفنی درباره تحولات منطقه گفت‌وگو کردند؛ دو طرف بر ضرورت اجرای تعهدات یادداشت تفاهم تهران و واشنگتن و نقش بازیگران بین‌المللی در توقف جنگ و حفظ حاکمیت لبنان تأکید کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/660101" target="_blank">📅 15:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660100">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e9d19be41.mp4?token=dQLF3Pz3_2vUes9BPZk8uhturaosTyqf4_vy_MHoD-u6-ebst6sq17K03H5h47STOJOh7NePj6m_MAmvnr9IxbT-lpvIuIXmeZl4-5jDhqEZVAgHJrQFCjmlgvK17RQchec0cDvhcyebbMLyqN4bzlJrvWkFEtR0ab24JPWO8SzMtsU7JuKDSIu2HFyJKjUmrcTXWAS14uPmTpVi1wMaLnAjgJPP7ckOebYx3MORIjFV2Ts2O4H3oucEy3kJy4TGda6WQheBceeezVNKuI-UL1MOupKmy6OEXL0HhM-yYSwqKrhtlHdZxBDpgBxhfjYLVjNgQmwspm99SNvbSVtp8ZHS5FJ76stS_9aWDeXR7-ZK4rxJCaZiRSJ9EPfPTfKgG40psR_7ECoxi8-jEVlGmctLceXU7bzz3UN6lGBs6udX1z8lxZpdBGl_dSiiQKnaO8bAjnwaTKxLUZAOd4BQAf3SwMseqNJCJFF7dbt74qKipxDA8WmS_a4t9nk_jCwrmkcRaNxN3a9-hlMtYSLmhETp59CGgMOD7SOg40mYin3ebKToMO8LB-NJP5Ni9hMFN3dOpcpnA1Fyj2RRqqx1mhDuyrCypwiUduBziPywWq7oGJ8o-pemPz873iNWvQ1MAqArbSMg_mJ7veqxPZlvNochJz6Zu097oOiTUYIj3b0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e9d19be41.mp4?token=dQLF3Pz3_2vUes9BPZk8uhturaosTyqf4_vy_MHoD-u6-ebst6sq17K03H5h47STOJOh7NePj6m_MAmvnr9IxbT-lpvIuIXmeZl4-5jDhqEZVAgHJrQFCjmlgvK17RQchec0cDvhcyebbMLyqN4bzlJrvWkFEtR0ab24JPWO8SzMtsU7JuKDSIu2HFyJKjUmrcTXWAS14uPmTpVi1wMaLnAjgJPP7ckOebYx3MORIjFV2Ts2O4H3oucEy3kJy4TGda6WQheBceeezVNKuI-UL1MOupKmy6OEXL0HhM-yYSwqKrhtlHdZxBDpgBxhfjYLVjNgQmwspm99SNvbSVtp8ZHS5FJ76stS_9aWDeXR7-ZK4rxJCaZiRSJ9EPfPTfKgG40psR_7ECoxi8-jEVlGmctLceXU7bzz3UN6lGBs6udX1z8lxZpdBGl_dSiiQKnaO8bAjnwaTKxLUZAOd4BQAf3SwMseqNJCJFF7dbt74qKipxDA8WmS_a4t9nk_jCwrmkcRaNxN3a9-hlMtYSLmhETp59CGgMOD7SOg40mYin3ebKToMO8LB-NJP5Ni9hMFN3dOpcpnA1Fyj2RRqqx1mhDuyrCypwiUduBziPywWq7oGJ8o-pemPz873iNWvQ1MAqArbSMg_mJ7veqxPZlvNochJz6Zu097oOiTUYIj3b0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آمارهایی قابل تامل در خصوص وضعیت اجتماعی ایران از زبان بطحایی رییس سازمان امور اجتماعی کشور
🔹
طبق پیمایش‌های انجام شده سه چهارم ایرانیان به ایرانی بودن خود افتخار می‌کنند
🔹
احساس تعلق اجتماعی، ۲۰ درصد نسبت به سال ۱۴۰۰ افزایش نشان می‌دهد
سرمایه اجتماعی در سطح خرد افزایشی است که این شاخص جبران‌کننده شاخص سطح کلان خواهد بود
علی‌رغم وجود برخی نارضایتی‌ها ۸۰ درصد جامعه خواهان نظم و ثبات اجتماعی هستند
🔹
جنگ تحمیلی سوم موجب افزایش اعتماد به نظام، افزایش محبوبیت دولت و همبستگی اجتماعی شد
داده‌ای متقن که نشان بدهد جامعه ایران افسرده است، وجود ندارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/660100" target="_blank">📅 15:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660099">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a063c7aaee.mp4?token=veGDpgr1HOWSGOUWJLsmkVhc8D3qoDv1lZkdYNdJDhIdLjEhaEYbO-9CsOH_-WNfOxB9kJcAmRs9YLGwBjAt5l-uilnhGQSFSp-0k0999p5EThNT2QHbL2Sw2d_3mbfL4cVuwQ_wjLJdoB4Yqyp3BFMNd1vtA2nFm7fakFmgpx_87PlZzZQbmfKOeahE7YI_0lhlsoQP0Ld_rc-ULZjowKchg7H6iVcpeoVsgcc0k4FZqDRKoq8EU23dpFwA9EBJdrbtA3yz0CG_6cS_p9SLzncU43PL7qxQGvbh6RMWlfaumX6_hTVrxP3wkqaBxdV1qYqCoS_NA0foekSe3BFcvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a063c7aaee.mp4?token=veGDpgr1HOWSGOUWJLsmkVhc8D3qoDv1lZkdYNdJDhIdLjEhaEYbO-9CsOH_-WNfOxB9kJcAmRs9YLGwBjAt5l-uilnhGQSFSp-0k0999p5EThNT2QHbL2Sw2d_3mbfL4cVuwQ_wjLJdoB4Yqyp3BFMNd1vtA2nFm7fakFmgpx_87PlZzZQbmfKOeahE7YI_0lhlsoQP0Ld_rc-ULZjowKchg7H6iVcpeoVsgcc0k4FZqDRKoq8EU23dpFwA9EBJdrbtA3yz0CG_6cS_p9SLzncU43PL7qxQGvbh6RMWlfaumX6_hTVrxP3wkqaBxdV1qYqCoS_NA0foekSe3BFcvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ارائه اسکلت خواهر به جای گواهی فوت به بانک در هند!
🔹
مردی در هند به دلیل نداشتن گواهی فوت، اسکلت خواهر متوفی خود را برای برداشت حدود ۱۹ هزار روپیه به بانک برد. پلیس او را متقاعد کرد اسکلت را دوباره دفن کرده و مدارک قانونی ارائه دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/660099" target="_blank">📅 15:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660098">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعای سخنگوی جبهه اصلاحات درباره احتمال رفع حصر موسوی
جواد امام، سخنگو جبهه اصلاحات در
#گفتگو
با خبرفوری:
🔹
رییس‌جمهور پیگیر رفع حصر میرحسین موسوی و زهرا رهنورد است و این موضوع ظاهرا با نظر مساعد مسئولین مربوطه مواجه شده است.
🔹
بعد از این که مجموعه بیت رهبری، ریاست جمهوری و مجلس خبرگان را زدند، منزل میرحسین موسوی هم در پاستور بود و با توجه به اینکه منزل، قدیمی است، آسیب دید و به جهت محدودیت‌هایی که داشتند، از آن‌جا خارج شدند و در مکان‌های مختلفی جا به‌ جا شدند.
🔹
میرحسین موسوی به لحاظ سن بالا، وضعیت روحی و جسمی، دوران سختی را پشت سر گذاشته که منجر به بستری او شد و بعد از دستور رییس جمهور، خوشبختانه رسیدگی‌های لازم صورت گرفته و امیدواریم این حصر هرچه زودتر رفع شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/660098" target="_blank">📅 14:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660097">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
شورای هماهنگی بانک‌ها: سپرده‌ها و اطلاعات مالی مشتریان بانک‌های ملی، صادرات، تجارت و توسعه صادرات امن است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/660097" target="_blank">📅 14:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660095">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SoGKAAHsBv2em3iej9H9rINSLAGNj0VxXAr4NE_r01fjIRwD20XzHPmdgvXYDtrgSw9h2klMqckOTdAqHYnGfT7aIa9Q43hA-f82wUAp45AdUC5XYCHsMw__fv2YhxYwcWOi935bRuTBz4Db8wsIxdPvGakVgnT2aVbyi_qSq1zJh8jyGq-P-3Q1Z9c5r8IX59qzq8pN_hF-XtiNsDNBU1KAzMWFNafs0fPIFHSWyJFSTYZpxirOzqkZ7CDDRMlYEvI4opclxD-dkVyW-WNmJm9jqfJYX432_8gYufYlQ97bIqxD8N0h3j8FSaN9K3TMkpDw-BL0mfsiOJRnP8G3Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازی ایران و نیوزیلند در رتبۀ چهارم پرتماشاگرترین بازی‌های جام جهانی تا به امروز
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/660095" target="_blank">📅 14:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660089">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/879cce3a3f.mp4?token=rQze-uIgJ1SQQ9X_eZip9dHmVSSHGSuDLPjjJkJyUQpJpN8XQ7X59BuQ5sibimL2nGDQ0dCWMHhDJic9m8SBV6y005b_pSDP0cjHWTQtmgoUD2WM7-7oAg9agH0Y2-u_UUMI4k4QHDCqeHNZdxLjLreLgRHn84AZmOCch18bhAtOIbiiQQKpfdqm-aR6ZVxB4klzMU6IE8_IXA7uMRPXa0QcxsI-Nz602Jleho4bsHIv66vu9JEkBC0E9Cj1prUR85JLGYnT-NjHEx-tP8uEJsKSJbmAZ9aFMUL_RWlgsvsxo_bVbsGUFx_rf3SsA0N8SuZm6R7K_h68CASEaytZeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/879cce3a3f.mp4?token=rQze-uIgJ1SQQ9X_eZip9dHmVSSHGSuDLPjjJkJyUQpJpN8XQ7X59BuQ5sibimL2nGDQ0dCWMHhDJic9m8SBV6y005b_pSDP0cjHWTQtmgoUD2WM7-7oAg9agH0Y2-u_UUMI4k4QHDCqeHNZdxLjLreLgRHn84AZmOCch18bhAtOIbiiQQKpfdqm-aR6ZVxB4klzMU6IE8_IXA7uMRPXa0QcxsI-Nz602Jleho4bsHIv66vu9JEkBC0E9Cj1prUR85JLGYnT-NjHEx-tP8uEJsKSJbmAZ9aFMUL_RWlgsvsxo_bVbsGUFx_rf3SsA0N8SuZm6R7K_h68CASEaytZeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥀
#استوری
کلیپ های شب اول محرم و آغاز ایام عزاداری سیدالشهداء (ع)
این خبر را برسانید به کنعانی ها
بوی پیراهن خونین کسی می‌آید
#محرم
#امام_حسین
(ع)
@Heyate_gharar</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/660089" target="_blank">📅 14:42 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

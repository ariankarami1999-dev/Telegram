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
<img src="https://cdn4.telesco.pe/file/m7bCQLEfXHB3TCwQgHen6R8sfZ8XWSGlfBfgWbKqP7KQ7drigxpzcb86KKN5P1iOzueWl_7twW9QnzLsmMXa_JfvJTC0Q_tKFZVnc4TWOP4snIDY02DWBPgzoGmE3ks5WuPcdcqcq1wr5-b951ELjR57nL3iMdnKiTsmswV9CMCc7d4v2U1LEWBrLfMAqYiuNeCDF-qhkfhPlXMxs8TNtEjNg5CvxPfM1I0tH3XZA5ngtVS9aJz4bIyU1Ni_FDLWyfx3foVrfVOyuB1YcG9XCxbOv3sJApkHu1ZfNVO_su1CkxxZG1q2Z2REaQqE0-PX_IkC1hlHsSUIiEyLrsuEfQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.4M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 19:28:02</div>
<hr>

<div class="tg-post" id="msg-667553">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abdb8761f0.mp4?token=TBBVBOheuCRy0XVyloGOgjHubqSBPO-t1uQQiz__ptWJS5_9m5DZXQ7Gnc_4pAjgxr7g5fgeKtFQN6JRpOGRlmmvq7nSBB5_Aq3kgOkid27X6LWNeL7FpgIn228x2m1DfGlk6KelC8ljcXrTE8rM22xbYTn-nJABZsEjdqVu3XPKcQPYC5sxExedhPNzx8haBSUze6hkXulfWkPfhlmu9v0_LoAuBfbuE6tcR9u4iXuvZVClifLM1P4p2h4IRMB_37iDof_ogj7e8ujabPNOpoXbB3timlB-qkRIxAsAw8X4gGBYklNK3JGdVLVWJzL9nari0K3nWAIPziQhO_p14iov3jt0LgUc4-GenZbKWfLyaET7744zsVpgbNSVEv_DqlX0mMnLF1timYHY0ge_l9_Y4Q6hRb9j8CegtJ4YTbPn_cnyhfWF-yAHhKC8UVJMCMVlH6u1TK-To9LwMNceBBtM_pb3zok-4q8aM0P7YcU0d1BobLLDZvZ5LbsKJWF-4bI8LV7q_PzCeBOcUe0Cc0rJoMpDkpBikhlzjlEQp_CUVSPzRvkV63x-zLpOC89eKi97R_O8ngdUT3Zg-tBOU0HNjS2Sw4h991eqi7EXASNAj701o6GfSAFGqWUl1MhIHP6s481tM3UGVaMp-cWSKzn5YaUTeqwvaulK3At_E28" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abdb8761f0.mp4?token=TBBVBOheuCRy0XVyloGOgjHubqSBPO-t1uQQiz__ptWJS5_9m5DZXQ7Gnc_4pAjgxr7g5fgeKtFQN6JRpOGRlmmvq7nSBB5_Aq3kgOkid27X6LWNeL7FpgIn228x2m1DfGlk6KelC8ljcXrTE8rM22xbYTn-nJABZsEjdqVu3XPKcQPYC5sxExedhPNzx8haBSUze6hkXulfWkPfhlmu9v0_LoAuBfbuE6tcR9u4iXuvZVClifLM1P4p2h4IRMB_37iDof_ogj7e8ujabPNOpoXbB3timlB-qkRIxAsAw8X4gGBYklNK3JGdVLVWJzL9nari0K3nWAIPziQhO_p14iov3jt0LgUc4-GenZbKWfLyaET7744zsVpgbNSVEv_DqlX0mMnLF1timYHY0ge_l9_Y4Q6hRb9j8CegtJ4YTbPn_cnyhfWF-yAHhKC8UVJMCMVlH6u1TK-To9LwMNceBBtM_pb3zok-4q8aM0P7YcU0d1BobLLDZvZ5LbsKJWF-4bI8LV7q_PzCeBOcUe0Cc0rJoMpDkpBikhlzjlEQp_CUVSPzRvkV63x-zLpOC89eKi97R_O8ngdUT3Zg-tBOU0HNjS2Sw4h991eqi7EXASNAj701o6GfSAFGqWUl1MhIHP6s481tM3UGVaMp-cWSKzn5YaUTeqwvaulK3At_E28" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁨
♦️
هزار بار برای نابودی ما تلاش کردند؛ اما نشد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15 · <a href="https://t.me/akhbarefori/667553" target="_blank">📅 19:27 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667552">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16e92de0e9.mp4?token=nM_-yRAEziiV_U57JPMDK-NouE1YPmN8bl4RKRIGQvya0rkuDKjJdTFe59SK8-nMY6Ov3N3TuN11NlQBnjEJXIU82cNRCfOcFi3Mm6B6g4RuS-oj_AFdmGFNwU116mSnMQvKBETcD7XoE6SB14VaW1SnNmeOhleFr4EwJxgW1VzXdLKLjRhmLrDG7gd72kJlWEkz5NMqQ3N1FJlytiRxWRKwxqe6eX6e8l36Y2oh5v-HBbYMpfHJ3r4lswBcsr1Xd45m4Zzghtzvv-gV5BzrME6djUO7trwoMfPIPELGKrEInNX9qqsatTP6ZLfgOOLtW24tDKeCFXldD9W65P9MNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16e92de0e9.mp4?token=nM_-yRAEziiV_U57JPMDK-NouE1YPmN8bl4RKRIGQvya0rkuDKjJdTFe59SK8-nMY6Ov3N3TuN11NlQBnjEJXIU82cNRCfOcFi3Mm6B6g4RuS-oj_AFdmGFNwU116mSnMQvKBETcD7XoE6SB14VaW1SnNmeOhleFr4EwJxgW1VzXdLKLjRhmLrDG7gd72kJlWEkz5NMqQ3N1FJlytiRxWRKwxqe6eX6e8l36Y2oh5v-HBbYMpfHJ3r4lswBcsr1Xd45m4Zzghtzvv-gV5BzrME6djUO7trwoMfPIPELGKrEInNX9qqsatTP6ZLfgOOLtW24tDKeCFXldD9W65P9MNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتانیاهو: مردم ایران پیوسته شعار مرگ بر ترامپ و مرگ بر من سر می‌دهند
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
#Demon
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/akhbarefori/667552" target="_blank">📅 19:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667551">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
به‌منظور تسهیل تردد زائرین در مسیر بازگشت، فردا ادارات مازندران تعطیل است
استاندار مازندران:
🔹
جهت تسهیل تردد زائرین در مسیر بازگشت از آیین با شکوه تشییع امام شهید فردا سه شنبه ۱۶ تیر کلیه ادارات و دستگاه‌های دولتی به استثنای بانک‌ها و دستگاه‌های خدمات‌رسان را تعطیل اعلام است.
#بدرقه_یار
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/akhbarefori/667551" target="_blank">📅 19:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667550">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cec1d25ee9.mp4?token=KcXGp2jUawTlhNvy822hzeyWC7Io6DN9qW0qIgD-rAkwJwN-i-xw88zZveyqT8Z7L8feJncHRE0qLku4eKUuU6oZBc9a97yJB5E3lpUaOBnYFaTFAeNlNeCZmJyTiFsnzTaloVmLw1iRh5RE0OJ-RqHSPB5iy7gmecKo0Phs4OBaa1XzulJZHettWidfYY5C2jU0D2agSZUy54vle-yr_CHT-2js72oihxdFYhmcbcUQphZhbc8fvPNA1eVcXG3bMTLslvyHPFYoE_8L_chmPOdSWXlmYcpWlrWyCt0y80lmPGsz02uR9CACRqJKTkzEV3rxoNn2fn-JjgHXLgBPDTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cec1d25ee9.mp4?token=KcXGp2jUawTlhNvy822hzeyWC7Io6DN9qW0qIgD-rAkwJwN-i-xw88zZveyqT8Z7L8feJncHRE0qLku4eKUuU6oZBc9a97yJB5E3lpUaOBnYFaTFAeNlNeCZmJyTiFsnzTaloVmLw1iRh5RE0OJ-RqHSPB5iy7gmecKo0Phs4OBaa1XzulJZHettWidfYY5C2jU0D2agSZUy54vle-yr_CHT-2js72oihxdFYhmcbcUQphZhbc8fvPNA1eVcXG3bMTLslvyHPFYoE_8L_chmPOdSWXlmYcpWlrWyCt0y80lmPGsz02uR9CACRqJKTkzEV3rxoNn2fn-JjgHXLgBPDTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مروری بر توصیه رهبر شهید انقلاب به جوانان: اگر این چیزها را رعایت کنید از فرشته بالاتر خواهید شد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/akhbarefori/667550" target="_blank">📅 19:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667549">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
بازگشت ساعات کار متروی تهران به روال عادی
🔹
پس از پایان مراسم تشییع و توقف فعالیت ۲۴ ساعته، متروی تهران به ساعات کاری معمول بازگشت.
🔹
آخرین حرکت قطارها در خطوط شهری ساعت ۲۳ و در خط ۵ به سمت گلشهر ساعت ۲۲ تعیین شد.
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/akhbarefori/667549" target="_blank">📅 19:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667548">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
تعطیلی دو روزه ادارات استان سمنان برای مراسم بدرقه رهبر شهید
استانداری سمنان:
🔹
منظور تسهیل حضور مردم در مراسم بدرقه و مدیریت تردد زائران، تمامی دستگاه‌های اجرایی، بانک‌ها و ادارات این استان در روزهای سه‌شنبه ۱۶ و چهارشنبه ۱۷ تیر تعطیل خواهند بود.
#بدرقه_یار
#اخبار_سمنان
در فضای مجازی
👇
@akhbar_semnan</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/akhbarefori/667548" target="_blank">📅 19:06 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667547">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa6db0b54b.mp4?token=ixdwe5FknJzRR7Q5ESRfvTknZUqdXJ1cSKnl2eKFTxVfgW1q0zC2Kyh3VG_bAYvmfdAbkJeww4qPUKYza9tuKHcmkOaN8jKAmrgCK9vj4Qk9td7DR-4EPHEvAPookxHQ2pjDEVEs0SA7_O1p7tIs4Y_yDZ4s6uDuA7Sa-hf8206hmNvD7I3-ZmdV8hHmHVsmoRcBrQlZ3sUFjRIarCwiXGjJ_7ItLF2LPOvt6snVl8r0PGi2D3jMcjvU2SYQ9QTVSTkYRZAunQx9J7wD5W9fRGr0z51bQCYdolfzDjTnEDhhLBjIV7xQ1vrn8Ca-AL48YTJQupmXpQdtB39t8VSiQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa6db0b54b.mp4?token=ixdwe5FknJzRR7Q5ESRfvTknZUqdXJ1cSKnl2eKFTxVfgW1q0zC2Kyh3VG_bAYvmfdAbkJeww4qPUKYza9tuKHcmkOaN8jKAmrgCK9vj4Qk9td7DR-4EPHEvAPookxHQ2pjDEVEs0SA7_O1p7tIs4Y_yDZ4s6uDuA7Sa-hf8206hmNvD7I3-ZmdV8hHmHVsmoRcBrQlZ3sUFjRIarCwiXGjJ_7ItLF2LPOvt6snVl8r0PGi2D3jMcjvU2SYQ9QTVSTkYRZAunQx9J7wD5W9fRGr0z51bQCYdolfzDjTnEDhhLBjIV7xQ1vrn8Ca-AL48YTJQupmXpQdtB39t8VSiQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تارا اوگرادی قهرمان ایرلندی
ناوگان صمود در برنامه پرچمدار: مشت گره کرده آیت‌الله خامنه‌ای در هنگام شهادت برای من نماد ایستادگی و مقاومت است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/akhbarefori/667547" target="_blank">📅 19:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667546">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e55eddf3b.mp4?token=GEfulC_8NJFjO3d9TNL14FVbs5qqQ3kQeMs2CAjshvyQznqEhulHP2_ZUwOEgHFf0GA0NOCYTnnO2oZ6ntyrGYAxjbrroxMAOHXLJsOW50H-_ym_4xvxL9IRi95TUe942eBSdHQBMIQKFVgqsje5CV8w0FOzesZFPZLu7ZSGTdclsQBLz00jGVlu7pIBONYMK-4uQsgguuYz1l8F5gVlT6DduYBQFG2gf5_n68ABGJtCjcahzJJzLAvJISqg2ZlGdFVRmqakjP88nn2mPAHJpN6gu0RUPBKK7rDYc0Nhp16gPZJVjvzaaexnXKNor2uBaPpwR5aE1CEFuZRqItS-LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e55eddf3b.mp4?token=GEfulC_8NJFjO3d9TNL14FVbs5qqQ3kQeMs2CAjshvyQznqEhulHP2_ZUwOEgHFf0GA0NOCYTnnO2oZ6ntyrGYAxjbrroxMAOHXLJsOW50H-_ym_4xvxL9IRi95TUe942eBSdHQBMIQKFVgqsje5CV8w0FOzesZFPZLu7ZSGTdclsQBLz00jGVlu7pIBONYMK-4uQsgguuYz1l8F5gVlT6DduYBQFG2gf5_n68ABGJtCjcahzJJzLAvJISqg2ZlGdFVRmqakjP88nn2mPAHJpN6gu0RUPBKK7rDYc0Nhp16gPZJVjvzaaexnXKNor2uBaPpwR5aE1CEFuZRqItS-LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: تنگهٔ هرمز یک ماشین پول‌سازی بزرگ است
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/akhbarefori/667546" target="_blank">📅 19:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667545">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPtEl2UR53nuaRAQ5fiudN6xCAzC5C6XByb-xD3IdKiXUUKjgAoJSPUoCt61BZkFgtQpBdejcVmffMsPGOWSngkhXTGdiXYQSPWj0oYJPxLfS581tw4OuK7roaLLGhkK6RPYUgc1Z54_AuC_7iahReh7BBXiPH_C46Fk-vuhyWuV3Cp6JH0KWAv_D_pi7HWnBXQyp0L-jKW8_1eeFS3MLxIxGHYOI535b-NEXTVll_QmBMBn9plO-eza6GoMK-J7Tr-2FYrMn3tY1vBx4Rs92zvMm5VgAh4Afs9fMQ6eVtISZO8x9-PTdrX6Ic9WE5Ab04z-tycOWQQaWnTVxwltmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/akhbarefori/667545" target="_blank">📅 19:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667544">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JrJ_eybo-9UgnTm3hLhBk16n2ivbX03c_XQ_hJaUszoz2KW1MKecE-ZjkaHst5w6rH40sKF0GAatNcWNHdLCGxxw1XfPalLcs2TdVZnOHYv5i6W-32FXvTwsNbTwWkdesaA3j-Vm-7pN0lb7g2dTJMUOxdRLbESDExqou9OhmiLhaWNovHtIRzv2p5T-FXtSR3GHgYRjvj_gLTFvvDv0YxaCvXcHFLrrchIYxZXcH2xJOgXoxUqgrIAm5tpRWSyp5o-u-Ew0Buj7y1KJmaPVvAdAlrwT9wWniEh1mKUVlRioTm4s6RZeUAdwlMue7y7rR6-Nf91LE01XGv1hcJyEjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر متفاوت از مراسم امروز تشییع رهبر شهید
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/akhbarefori/667544" target="_blank">📅 19:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667543">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iet6uFs4N4e6WL6TLMnG62P_3NiFym9vjdcBaNWeCrAKaHhk8-bm7sLmeN1ghGhX3oWaEzvQ648QZmeV5td8iAM2XsnkFFlb6aHMHJUDnD0_IzsRTkDafWdA-KkNvdHuCarcc-q49CO8OM9fP0XiVmZMz0_PSggsIVO14ID1DRh5Wq-In3UWyEqAY5QpwGapag_HaQSV5NFLD1ruIvfUWDs0qv-WlAe-l-Ua1fdDuB_Hd4EiTz_SeTAm12s3kMTMR3BKicAOhvutoXKXHfJ9K4ARnK41uosO0mBTbWtAoovDhlLC1gXvbHuogUGzkLvnfZAapZos0sE1F9P1vmaQOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رفتید سوی بزم شهادت به‌سادگی؛ خوش باد بر شما سفر خانوادگی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/667543" target="_blank">📅 18:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667542">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
از سرگیری پروازهای مهرآباد و امام خمینی از صبح سه‌شنبه
مدیرکل فرودگاه مهرآباد:
🔹
پروازها پس از توقف یک‌روزه برای تأمین ایمنی مراسم تشییع، از ساعت ۵ صبح سه‌شنبه از سر گرفته می‌شود.
🔹
با توجه به مراسم تدفین، اولویت برنامه‌ریزی پروازی با مسیر تهران-مشهد خواهد بود.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/667542" target="_blank">📅 18:55 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667541">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
بی‌بی‌سی عربی: مراسم تشییع در تهران «تاریخی و میلیونی» بود
🔹
بی‌بی‌سی عربی این رویداد را «تاریخی» خواند و به حضور میلیونی مردم در مسیر ۱۰ کیلومتری کاروان اشاره کرد؛ این رسانه بدرقه پیکر رهبر شهید و چهار عضو خانواده‌اش با اهدای گل توسط سوگواران را بازتاب داد.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/667541" target="_blank">📅 18:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667540">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
پیام مهم فرزند ارشد آیت‌الله سیستانی به دفتر رهبر معظم انقلاب
آیت‌الله سید محمدرضا سیستانی، فرزند ارشد و مدیر برنامه‌های حضرت آیت‌الله العظمی سیستانی خطاب به دفتر رهبر معظم انقلاب:
🔹
درست این بود که پدرم، آیت‌الله سیدعلی سیستانی، بر پیکر رهبر شهید انقلاب نماز گزارد، اما وضعیت جسمانی و سلامت ایشان اجازهٔ این امر را نمی‌دهد.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/667540" target="_blank">📅 18:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667531">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QzCx3LGGYutBonPL3spXQ9RdLkN1o_cVy6XcmlRRNbQy_c1BfgLkcyvXpJLk1auD4QQwR8BwbvOpbectEEX_xKB7wjBXWPRwU9zbTwqheljnzfhQ26TC9xt2o_GmX82vXYptWVYwlcO46gz0nbyUvqCk783TiOlHoeRNg8GEjDVvviRbTRZlYlOvFOq9oRUmc3f5PkqWEoTKsVliHOBl7FPvqVDIgpzAbWkZvXAMAJ82N_Bgz1qKSH5Fn6ZIX9KZ51DLoZrztKh0OWVOebZQ00Q1gXqp4XdKV_Uiul53DGxJYn09oPMcezr6rooMjZVSwvHZtRZKdydfp6Ukza0zYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LDAcXc55OQB4QaBXp9TduFDd5HDJTd0DlSdPmK6v2RDtJYus_z6Qu0f9r0G_1G7JszFsah_4DV44xIWXYDLn4ZDn8aoo98VwbX_syCIL7w_O7Nbc7lN1lqXo6AglIC3woiCEzfeRgcLjx1wFNWc4iKxx7kV3zWichzIilN6qXwvRaJa9zWk56RjfvIC6AdHWVuCFRnMkq8xoPT6KjA9QzjohGopQH1A4-aJVYTsgk6mZjc4I4d-V9Q75jX3uAODuJow8s9EPGZjRf4hhRgAybgXAuQFa8jomOeE2upOazQNRl-Q-eCtxMfH63EoAr2L7yMxw2VtDHXsw5u9NaG6lBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nNMC2IiFccLJ4_9LjnP0ApQ6oMPfQru0EQyAHGJoXIMls1uZl_fe9dCA2XXoUcksE5fVdPSadP1Kke03pgd5-RJU2i99sk5djlXikEyst9aT_SE-sFgvPD5eCUixstTj6CQn6gGlDb-ecMWvY5Vu_W9WuSbYwNLgYkUy7eNOE8ZWfpBIqK_Qao3y_IJVfZbfz9gBLyb_4mSRx0sAz9ZpuUfsxFoxtDxogsXMQK1s2m5a0MeO4Nh9-uz4Oa6XODZE6YORQ-_J92p0U6ycADgz7UM62pJTlcvxt42lKF6N9MfVHqVoIFX166CQ126dAlZXTQZlIeLNB7ryFSwlDGWj_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/coQGZhte65ylQKeFaCKBp5Y_X0H_rx7tlRAHCOP4xvKZNWlQwzGwnp3hmDPcFu1G7qd_t9RDwxvtmUWbpxWt-JFtK9HcQRjBVZERCxzGtl_mjqIERIJ7rnGkQmqyz5RXTqLgso6E8cYPNHHeTRO-jINZmIoUZv8ITpXrQpbpMgijnsrRJBbuGggqFpWiq75Hy_IL4-RPniB3mMorJVS80PDVgodcy9FIJccIobuB8RUqUnqJdjj4z6XSOWYZN3H4D37MSYwKcp9fp5RxNhiq7V5P7H-0AbCoRfPwVbu_ro6xNSiSfZGITDMcdv6mT-fUxPuP2Tjj8IuAmRltpazL0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ys8fmbEULL3TBIppFMN9YM9JB8wqTH_RXDRJfR-mJKEKFW3k-j9AESCSgRJH6eBQjzEAR7Wsm6-xyiW-5RUNgKzyg3aa1io_BsiGmEkD5iBIqfnZhaTyB1rQy7O6mPF45kudIMnbLrPRQF8rlm9mtsvW-_8UyiisXiZarUpSEQ_qA2YZPHuVE9mqGk7Dsi71yUQk56rcD0nqzMqbtY2etpaU_ewQR1hn3AwNHi5wb10fDuDw7Q1gambSjFPmO4B-hXM6lvW3zyVjgrDQ-LdHtkZdnsEB4aU0dwnylt_96F6TopLaWYSJr_Lq0mtb3Lt4QTAPYrIzHf2KnSqce-MAMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G0N5EnOGLMCiXlxx3BqplC3ojNE_yX4f12CAFituu81PYNOFT0RYzy3-FHwxKldm7HyT7UeQcA8eVWX-Otet_wnPuzAw6L7h8JqWg9Fg7K9x5HxsfVoHcr2NB0NyEXNmMLxcwM65oWwvBKAHsmM_rOHzeTkETpxyySF9FGpmQRLMYPw8FdCSF3fhDVlpElCVmm6sA8VPcq19AZwip151qKmw_OqmgBA6JvnAZ4-DlygxcT_ggNQ4WIrkHSubRP2dNBBQlkyuQkyGtPRLV6ZkFYTBWohy6g-0ZKRlwD8dgIoLWAxDoKPKp74_abOZPyHviArT635BGTvuPAkdoOf5zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JDre-IJ0cuI5rMbVW-zUDzpvMmT55ubKOpRyG_erHPCk51qZp4JvzVq92oMC6lyma6DT2w_XVddr92OtdBMDuBDhLQZ95mctZ-F-B_e7rsiw_QK3Y8SFIcRco2He94ThPu4hsYbKWvdPCvbABts1Hbnf9nwwpr-Xxfha5z7R5vHmwx9VPa6ZL5KYcPNWEJUsiZSu_7DFymmFZRDIefCWh8LNq4exS75e7fYhoa-GovrbDrQaXbeuFVbGHaLqIvFFlf8STBfQkzaMFg4Uj6xjMVm91tkIjQ5ooWsiYOKfN9vWJof_Rlxvpj8xFoR738UCwGLIJ6PycU562la3GGZcEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mHf6986YzAnwHA98t4kL0xEscgO1O7Ux3HWsBctfdSfx5ak2g7HwEvhppo9K_fF5d6Zq5_7eCFJkbtO48O9KPz89sXk3rCnMHYvQdGca0rrNdrYMlZBx4KvrgxCbikvm_v_gmWUWkOBAnfBubvLLrOfwE6JACedKyVJESXgeN4X3pAghemCM0f5zKnM2h6v32DhjNBkGVuwJdk7B652YLSloM8prOSu29NG_9kDKaNnilImaka56xwJiH4cWDRcH78dfbBGKkoNoNfxKdDO9--ni10rTmMTov2dOZldmtOztj0LyP9PPgTgMQBc7JHmb8W9sarV2QDl2XJUr18NbuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/msXvrWyPjaf8mKTH0KelXjYCjqPKYZovCKc1qrxJfK8hlvL3VXlEbxrbbk0O1BeVeZdkDbO1eTOQbslx3-6aJlJdx7ZDWaY--Jc_CJkylfTotoZk2UMuQTWV027w5SWX0xSLZFFkslATB6gHspKU6v-5r4zGN65wqDnSdG01SJX44MR1Lxp8NK64Ca_HWQ7GL8czU2K_vZ9ffNrghL3JAS6z1IsV-oKMqbjbkWHCCTY_JxkejTCywmRq6viz34dr_ll7vPzSwk0e_x34glDlnukF7Sg71GZu-G_Im09MkYJqKxqPhAmEPd_x9FfNOtxtvt_tZeiGpHbcB83Gbf324w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر خبرفوری از تشییع پیکر رهبر شهید در تهران
🔹
عکاس: فهیمه فرخی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/667531" target="_blank">📅 18:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667530">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
خبری سنگین‌تر از واقعیت
🔹
امیدمان این بود که بگن همه این‌ها خواب است و آقا زنده‌‌اند...
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/667530" target="_blank">📅 18:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667529">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13492af301.mp4?token=QVmkt7d4vzDlXHH6PDsx3O4Bi6ALxWH3uPPoTnvhLlqXtixYQDOmg9V79EdnfHD54XwOXOXMgD-qR_DEUUCphm6x-A7nqcz4xYYrcDPgf7Z2gr-gErG0kRjC4DxigKL5mUNFILSSau-ZeFQENjKKebU73c9AtyzynYzaJjEmQfB6vtSZxKG3IKJTcCfH_lfypimzOspNy2Q1MUok5nh7vczli5T86BfojIR0eQ9JmlP7fNpZ3XE4BNL9XJuOxRQ5dpUDLpkz1IfQFN5aIi-ut-hkdbzkaihiNwtlE2ctNcCxaC1Qu6iBIiCe-XbdfKKzu3khGuqHAGdbS7bxcMZxzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13492af301.mp4?token=QVmkt7d4vzDlXHH6PDsx3O4Bi6ALxWH3uPPoTnvhLlqXtixYQDOmg9V79EdnfHD54XwOXOXMgD-qR_DEUUCphm6x-A7nqcz4xYYrcDPgf7Z2gr-gErG0kRjC4DxigKL5mUNFILSSau-ZeFQENjKKebU73c9AtyzynYzaJjEmQfB6vtSZxKG3IKJTcCfH_lfypimzOspNy2Q1MUok5nh7vczli5T86BfojIR0eQ9JmlP7fNpZ3XE4BNL9XJuOxRQ5dpUDLpkz1IfQFN5aIi-ut-hkdbzkaihiNwtlE2ctNcCxaC1Qu6iBIiCe-XbdfKKzu3khGuqHAGdbS7bxcMZxzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پناهیان در برنامه پرچمدار: در تاریخ اسلام شخصیت جهانی مانند رهبر شهید انقلاب نداشته‌ایم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/667529" target="_blank">📅 18:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667528">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسازمان راهداری و حمل و نقل جاده ای</strong></div>
<div class="tg-text">🔹
برای راحتی سوگواران رهبر شهید انقلاب در شهر قم، مجموعه‌ای از تدابیر جاده‌ای و حمل و نقلی و خدمات سفر پیش‌بینی شده
‌
🔹
قبل از این‌که برای مراسم تشییع رهبر شهید در قم راه بیفتید، به این نکات توجه کنید.
‌
#باید_برخاست
#بدرقه_آقای_شهید_ایران
#چشم_به_راهیم
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
‌
🌐
@cheshm_be_rahim
🌐
rmto.ir
🌐
141.ir
🌐
https://ble.ir/141_bot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/667528" target="_blank">📅 18:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667527">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
نتانیاهو: تضعیف ایران مسیر را برای توافقات جدید هموار می‌کند
🔹
نتانیاهو در مصاحبه با یک شبکه آمریکایی اظهار داشت تضعیف ایران به نفع توافقات جدید رژیم صهیونیستی خواهد بود.
🔹
وی همچنین با تأکید بر اتحاد با ترامپ، ابراز امیدواری کرد که در دیدار احتمالی با او، پیشرفت‌های مسیر صلح با لبنان را ارائه دهد.
#Demon
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/667527" target="_blank">📅 18:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667526">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سخنگوی اورژانس: مراسم تشییع بدون هیچ حادثه‌ای درحال برگزاری است
شروین تبریزی، سخنگوی اورژانس استان تهران در
#گفتگو
با خبرفوری:
🔹
همه‌چیز طبق روال، به بهترین شکل ممکن و بدون هیچ حادثه و خطری درحال انجام است و همکاران ما تا اخرین نفری که در خیابان باشد، حضور دارند.
🔹
گرمازدگی وجود دارد اما حادثه مهمی رخ نداده و مراسم در روال عادی خود طبق برنامه درحال پیش‌روی است.
🔹
درحال‌حاضر ۲۵۰۰نیرو در قالب کمیته امداد و فوریت‌های پزشکی در آمبولانس، موتورلانس، بالگرد و نیروی پیاده در جمعیت مراسم را در پوشش می‌دهند.
#بدرقه_یار
@TV_Fori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/667526" target="_blank">📅 18:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667525">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
فردا شب پیکر رهبر شهید به نجف وارد می‌شود
مقامات عراق:
🔹
پیکر مطهر رهبر شهید فردا شب وارد نجف می‌شود؛ برنامه‌ها شامل مراسم رسمی در فرودگاه و تشییع عظیم مردمی از نجف تا کربلا است؛ همچنین صدها موکب و زیرساخت‌های ترابری برای مدیریت جمعیت عظیم زائران آماده شده‌اند.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/667525" target="_blank">📅 18:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667518">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KVpzDnHcTLrMw0pcq5WGbkB9fapcoQucwtnWt1YP87wgPle1uLZHyhaLDaHbO4owkIetnA-TYsPbFQ014mf9t4P3fRufVZklNKWKplXDjDMLW2hW57A9aSfTvTFkmUlHYicbbeb2EpqnQiAd-924ad0sGeIxyJBO0swddJamcyUlbEtut6dbxm09ycDp9PmnA8BWZq08woo5MLkCR2L5z4HOQTaD7Cdki5OD_z_71sJlHp8cOSHzc6ZSgA-I7KWOLWVWiJFlxG0tJVKEzMLeB-NX_7e6Ka5-Yiuw4tUfD2W_K90L9mie4ktuUH3sqAxi5Lq0cAu6pDI2doo2vjcXIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gUw5zmzyOqyQXyuCZe1t5gON8WTWyYBs0OwvDJSE4_g_k3ZfN3nQZrIOAZRrRK08NgfTpc-5QTqxWnKsKIo0ibw7jvJtfbI6rXtwr5_l20b6OL2JkAhdy77E1TIumafJ16F1D_Jqid9W0eSeyYuZ8IK7dNC_GVAulSu5USx6NCdDC0j2etDgsEeTbkPAfVGZEYACYDorShWk6PO71LrrSkiPoOTwcpRjBXmVqwRpDGp3NiHwi9wb8SRiA-_gwH1YWSqh9Fg67qn4UK03JonQK6xIrIaZxmntbBcagOkeMYJTrTCZpLp-OxVzpff_YMQKOqqFQKEbWk-ny25zGgZgdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mIyUu3wDkUe2AbFs_u88ds4A1_6zSh9wixcS0vNufg00j3HD3EwPBl1sagjP2og0hKgp1fZOU5oO55XnrOF5uZaUsgupKZFvYEuEFYb9xmh0TH8Mx3JA80PfH8kEYEIkolHwNp0iIBc19q_khlVGEYxnT4KDVK9P2h_dfIiq8GyBhh4SPi1pntG2AOThrcaF6oeHalwUQzbgngFgr5aZfW9Z89OxDpDyJ3GH2XNEKow5CvpOitiqdXQWNGQECthb5ynFeWGgOriRmfjbgTcjz5-0sOqjB03-AZjoQYm1UrfCCm0QVaqVvRFAEOG4hHahucgL9XNZ_r6b7w6nwyPmFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O505Hk94_isrLjkbvSg2lQ1baljQrCBCb9ByJv0bac2-gn59O5RL18jm6sxeT-JAbyfszUwXHr6WHyj5DDOC3ii8BrBb5N_1YLS276hxfOf-x2Ro9bqZC_nLFvGKgU7RIRgY8INxXz3uCk1WQ_nvIHSSg5b7p1JLIL33mLUWGWoG_6lEhjpgd6oFRNXO02SvRLUwvYqA_vNgxCJb-JxQQ4xHr2bF_r310loUOquNvJfjISDaytHqvaP6QoggBUQDzeKDJCUSbJlB9G5bBhPf9Scs31UY7mRLzgoLW2yqQajm3VHSLonT5W5liE41734flzOk8IkI6ThEtN_tEwZVSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FPhIkv-tQDoyGDYzS4Pvn2APfR_IpxZKTrt-Y5TkFJolVHAIXMz2RgwqheOVOkqEj6lDWN0krVHgw0qPu_hh-j7qEDHDyDnV8Qk9LIu8bKYeuAkMJUIUbVBcYOEJG05BXyQADeBqHc4jeDyXgKPslvZse7BaZBz-M1KU20BS0PKLglg_TkY0KrpDf9KYSE77UA7tUgOdVJ2M0YOT8zWWXsJQdpHgtd0KWx3qQRec6zNz4itvmZUJBFN0qfxdVWc14l8ImsD47Ivgak963j_CQ5cqqoPWrbJHRqvnKmf9KRuEC_vaXj7i752vhiqq53nu3jaiur3XG1ALhO2ZzYbEBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uxOIRTx3O-pAF-7DnCsoJk0bpAlsfk59lwD8yuVibHJ5f0yfg94pFkXsF-d-ScgfM8MrGlWdq5g3XQ-uMvPSMm_ZCN9Ab_rMQaBsl00v5euYPRmKuNq0u3UBY6q9LpBwatGsodz20_eehNuMai7RydcFcaCPAXEyjekvcFCG2DJAN2K2GDmc4YzbikzPAUQM_HnYY19DuKu07YwmiLb4GBCMsfj7iRc4AspxP1SLfDzjByl7EEo0I8vqDhbYrrjTRLHPasl4c1SLCBJbhActdgCmm5C4olwCsrL6EUeDnlBBMIWzSeF4IPpOVsHAtTlMzXSFiezzHliB_eGxlAlygQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UWMhlndsdj6l1fXwcU4n7NXWqX9Zm9pI0_DR15nKvuT4twhJOQyDF-bR0j5HFqgZTE2WRx2TyiJ3ZnBWIHqAmj1_OB2NkAJNLD5MMFNHnnMLwS0yZ3sXqBY82gjnHJwAXICtIuvtVSaXc6bX1Qu2UuoIgrw6L5We-i0Ma-Wlf_XkWJBgY5E0f5FARAjhsZj8DddCA6iB51231RDMxDWbych485q0jXefOob0gzl7suEbtsDZeBlRogBz-oqucu0vUgRapUgTfu2urUbC4i3DMbBS83S5kin-viRMqhZhJ8t-Fbamo_F8uBbFF14k77k-dBJLbhj4m3Ae2DvWcgBbWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پویش مچ‌بند سرخ
🔹
حضور مردم با مچ‌بندهای سرخ در مراسم تشییع رهبر شهید؛ تصویری از پاسداشت راه شهیدان، ایستادگی و خونخواهی رهبر شهید است.
🔹
شما هم بخشی از این روایت باشید...
🔸
تصاویر خود از حضور با مچ‌بند سرخ را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/667518" target="_blank">📅 18:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667517">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
آغاز مراسم تشییع رهبر شهید در قم از مسجد جمکران
🔹
مراسم تشییع و بدرقه رهبر شهید در قم، فردا پس از اذان صبح با اقامه نماز بر پیکر ایشان و خانواده محترم در صحن مسجد جمکران آغاز شده و سپس تا حرم حضرت معصومه (س) ادامه خواهد یافت.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/667517" target="_blank">📅 18:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667516">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
خراسان شمالی چهارشنبه تعطیل شد
‌‌استانداری خراسان شمالی:
🔹
براساس تصمیم اتخاذ شده، تمامی دستگاه‌های اجرایی استان روز چهارشنبه تعطیل خواهند بود تا مردم بتوانند با سهولت بیشتری در مراسم باشکوه تشییع پیکر رهبر شهید در مشهد مقدس حضور یابند.
#بدرقه_یار
#اخبار_خراسان_شمالی
در فضای مجازی
👇
@akhbarkhorasanshomali</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/667516" target="_blank">📅 18:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667515">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ee2d813eb.mp4?token=navNOQGdFHIvXUnicUPmAWHlXFSIaJsxbX0rFp9Oi-j-RvlAFLmMoxT2eYeDL39FoeHJlcOjsxS-TZgONi5i1SaAT-wpxfsUcd6hFoc7q3n8c_ktk1FSOPGWhldFbqtBvD2mC_C3_O4pVe0AtOEWIKAaLB5AlPRkwsd8sNLug2QdMcvxlfSGvwAy7YPJkmJI35LD4uHHmeho5WVtIYyFYXqlt77J-TQ_uS4vTYwDGJe_D4Dz5e2tbjXuIj7YunMWNezclNdvotiJUau0hdm7A7eU_MvnPNXUvXcI1Fmwd5TCJ4iFTJgDghPJrOSVVnPyOYy2PhOv7RInsft1Qgej2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ee2d813eb.mp4?token=navNOQGdFHIvXUnicUPmAWHlXFSIaJsxbX0rFp9Oi-j-RvlAFLmMoxT2eYeDL39FoeHJlcOjsxS-TZgONi5i1SaAT-wpxfsUcd6hFoc7q3n8c_ktk1FSOPGWhldFbqtBvD2mC_C3_O4pVe0AtOEWIKAaLB5AlPRkwsd8sNLug2QdMcvxlfSGvwAy7YPJkmJI35LD4uHHmeho5WVtIYyFYXqlt77J-TQ_uS4vTYwDGJe_D4Dz5e2tbjXuIj7YunMWNezclNdvotiJUau0hdm7A7eU_MvnPNXUvXcI1Fmwd5TCJ4iFTJgDghPJrOSVVnPyOYy2PhOv7RInsft1Qgej2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دکتر باقری لنکرانی، مشاور پزشکی رهبر شهید: تنها کسی که در سال ۱۳۵۸، در شرایطی که دانشگاه‌ها جولانگاه گروه‌های ضدانقلاب بود، شهامت حضور و گفت‌وگو با دانشجویان را داشت، رهبر شهید بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/667515" target="_blank">📅 18:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667514">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4z0Zk3gTYG6vOGS0ZdydQe0rQo_3YkxtDEZ9da0SAfZpO9tlL7iA6sNCVgrFP3RajUaoAaQhuXb6BsQQW8TpZxcL_l9PkGbk5zROy4EUpctGWaO9tAKiAEzVxBnpkYaQEwOpcECWSlsCJWdNI1DvpdNtaLzEX7xu-gUrD_pGNoqM6vzYRgClMKvuPdjRxBwO0pqAOvjWCuqCBmL15O7Yyff0kfrOSBson1R2xj4LXx8pWR4JyHpAdsH1g6TLyIUcI_zhmiSQNtoSRQyyeLR6rPLxUxcNeHQl_jCfpr7JeU_B2NTcDlTAn9tfIQcKUk3lMLpTuS1o65JtgdqUSyK9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استوری پژمان درستکار برای بدرقه رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/667514" target="_blank">📅 18:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667506">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A-MNmAwEeCLu8cjyrBRPvgoOrRNjXKNvmSHKp6qsWWVNjj9i90YkK1add1INGs2jUo_3j7KPSmlt2lrpUJim1MJNNZsn0OH2NGz-f_EJZzxFhEJ4ithXunpGo9zR5rzW1qMozGFTVO_v6lAmRSO7udTCzOev03bbdV5PVlTDRA-efCLaNvBkvvmYBGhd6u9HeA0CZwvRBXEUZW9PRcGusz3qtFX61fWpArb1KpN6LYB14JPGhxJSWApA4tUKjXBUz49_Fa4T1SOAwmmmbYsvMMNAl47hnKAlvF0aobyuFowwFmIS5VGuMIlWJYHfuzgbNYXj_4zdZ4jq655tCyjsiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L5UQEPlPD3vGAZX3oN_I23RS5CRybliR0sZzcoW0_IfkzM2g77A2sw7g8xAjgN23YPmNrA9mxQsnPu_Fj38vVm1AqBAov0WbLCkDGBpDT3p0nSheG3JTlDCge-HmjTE16wKYIGgZmxQu03uVjkf7N2sqHxtofbYJyYciRiHSBHpSo_gK331hu1iRCNUsF4Q2e-K7bfNAtwYGn-GwquqLATzoLoxWPu5JSvG6Z7-sJhuy8TgcBMR9LIuLBi2Nr5F5rYZSu2D9GSqnTsvFsFUAGz42tXhN033FHgSW36T54_1SOVKs7w2VJF8wgdIrdp2uVfdFl_-B10oZgx-wTPXQEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hQvNTmlQHZDQopum5zYlcp7D95qf_I4Ac_Qtwl7OMnFljWP1JkjLC057OOUq3mw-7fULYCLb8XQSyFRAfjo1BL76_SMS8UoeoXjXpj92_gFnEyjT1HCzI77_wr6M8R1l5-1U32R1HYSzk6XbqpAZvQQsu39L0ZEHCmG4Kn37lZhWMfulnal9ntGpkHhvuKpyCl__CgYAbi9nLEARMa_pj_wJeXtZGLLsG7BYXLiQka5oT_dX_WsjkM1RpRm9mMHZsW_u7uVUGCaJc0qHa9P5lRl7lry-FGKLzPaJ2LET91tyJYJkK-zYS-bsK9foLGqttK0nbYN3SYlzf1VJo2cfJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ng3O1MrwWSY7ddWc_6eU507Y-77jYaMMvbzdvuldhd5BsvM7Agk-RKbBWa_xpSb4ACgkVNrMKQsawjgycqDVjvc-QFsSofik49WGBmG8umCLBBzQ8IN3mvrtgQOWFr8kklkr3bK0Xzd-sxxnBDKb3glB4WWOv5KxOWZceRZ1FHIfuPMbklLvaYQcaO6PQz_II1AV-5LJwqxyvBjLiZQifjHZg2dfnZC_tNXJJDlR7qhDUMu9swUggXNo0xBoCVnbQPDjFKEkHClwP0QPXNIBORXNb4NjZtKn7BMYU9ubDxSVK-3cjlTDt3g17KUPGVxxHVL0wXRUMA7mrLD6qxjIRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FkQPHXrV7syr-kyu66qIe2fa8qxA2hA2P_UwAERo9CWohmoK0TYpQtAPnYA7bcVRRA4-8rCn3ZBMX1NlUREgWk-Z1lg5wxSPeeX_iUHFdFODoDKGsYSyPMGwmbZ-9E0HQU97lGSXFDHM9t8iGTLu3LGylXxtbVCEJfTDQ86gzFz89lRqApuUGtfccoxRzVFk8Rjki14SezwC6EKfXSk6LgUnnI4lTsrKt-3WCClSet9mff1TdcSSAx0LnftXo9CKSaZQ7ABAyDR9nNYBUDJi5RJgBnq7Y4pAllbG0EY-EnT7BBYTE0Gc0oAcFfhR3r2ub_nhB48Y0DCYPXSzjnaNQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tQJ5ZVtvlYHw6PjPoUkDqy3vfY5doq9gWxm8ZJzHxx6jvVbNBdfLk5pNv1hJKiFEt_4-LMZSAMzMeMxAN_1cHpYz2EkderypNslkWvcfBiiO_Exw8SugMaeD3Jp0Ym4h572G9K9BiV_zEoRJjfwln6VQqPxVUfZYBghByR3OebP0YCjGmCwgRZDQzKU0Uh1X8tU4fkPVHqbzgMc1qchG5fuFawXTcUFfsjuy3nEeZsgyTIomrdNXPrLCU5NWIQglCxl6VahNcumK1lx31MatoR-4cJsDv8jBoOcimvIRW4R8dSH3AeURNoqLYp5Z7Ti18UyRl9QOyZ5E9fMCB79gcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pr5yiX598tCD9s4EFrMYXZxc50rhpTaE3QrqiGoDQAXCoPRjnXF5qRpoGBt54U2SH8VwONtIaSY2D82g_Ztlh4NllHGIVAr68-pd8um5I45ZN-DoO52dFoOouu92G-4oI1TzS8G8Q1IKpNuo7lzgpLeOQIaSj4zhXl7aDowrznmOdTfpyPyqFFNyFeVYim0B_CVWRNovN9q1pPa1A-6uQn4Yev-hvw_RIECal03ncI-Xv7zsnm5g6p2-HuZB5mpYVptx81dg2o31xb18MFj9nk4pKCFH2o8t5P5E5q0OExnMU3TFawD5DY7GO_GZNNIutQ9lEv0Gc5dezscUYF5Agw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">◾️
عکس‌های ارسالی مخاطبین خبرفوری از مراسم وداع با رهبر شهید
#بدرقه_یار
@Badragheyar</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/667506" target="_blank">📅 17:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667505">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bfed78a86.mp4?token=Vkpqr1gpHW7p-eIzm1LLlPxgufZLeos30DI7mn6BRv896b7LQ0FtGTDGikNzxaMlETVHA75pWk5eKJbrMmf4lWc0kmPQW8huazxJQSP994AzkflGMneMS8LV9n2LVDg1aveqxfrTt_CZuCkDWRvPnJgaNTs_SVOYE5zN0vU6PtOaEMaLCFwcd40NzdhVwVZZTUs74zFos3t7ZZ_BN403nRzYC8jiCsmdhqs-g1cnv_Q4JzZPxxAI3Ika5tQe7Kpz6rlzN-xFJbwj9ldk1xiQoZvbaCJuN00_07Hp0sIApDitzagY6J9TdEXGaq2b3JaOUtp7xXvw3SJuoYEzhI6o-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bfed78a86.mp4?token=Vkpqr1gpHW7p-eIzm1LLlPxgufZLeos30DI7mn6BRv896b7LQ0FtGTDGikNzxaMlETVHA75pWk5eKJbrMmf4lWc0kmPQW8huazxJQSP994AzkflGMneMS8LV9n2LVDg1aveqxfrTt_CZuCkDWRvPnJgaNTs_SVOYE5zN0vU6PtOaEMaLCFwcd40NzdhVwVZZTUs74zFos3t7ZZ_BN403nRzYC8jiCsmdhqs-g1cnv_Q4JzZPxxAI3Ika5tQe7Kpz6rlzN-xFJbwj9ldk1xiQoZvbaCJuN00_07Hp0sIApDitzagY6J9TdEXGaq2b3JaOUtp7xXvw3SJuoYEzhI6o-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعاهای واهی ترامپ: یا ایران توافق را امضا می‌کند یا ما ماموریت نظامی خود را کامل خواهیم کرد!
🔹
در عرض یک ساعت می توانیم پل ها و تاسیسات انرژی و برق آنها را نابود کنیم!
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/667505" target="_blank">📅 17:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667504">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‌
♦️
آزمون کارشناسی ارشد ناپیوسته طبق اعلام قبلی سازمان سنجش در روزهای ۲۵ و ۲۶ تیرماه برگزار خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/667504" target="_blank">📅 17:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667502">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55393f65b4.mp4?token=uf5NiIWbXQoBt7kKKRbeiFXfbbql_yUCzTZMisBDFtNW2JcX6YrgbL643-_dXsvIbsjAg1qHI-OgVBvVM7pYZpMkdvoQ7Qz3kyNrM9Gr3BYAUagMiD-XSY_bIweBTrZuDHJ-8aJf3l9BUWIAL4iaDj84XXwZb3zDK36EgdEQdo4qzEuHbp2iXrp7z3OYkMPJ6u9sMrtFqX6uIcbr8A2wo00cVceytFMVCSOsVsp1SjBV8YRKatmYQ7HizFumvvsE8NSUVu0doT0IACsGqWkt-2ehFEAHmXOFK9iDdymWDgJ78ThCi1OWj6pjUssxTzvyuPfCNq7uF8zisx8D4ApxuZ3kd2Q-fBRzAn1gL9X5v9H5uW3HE1Os8hhL60gzuErLZ_akX3HuN0FSX34QBsfr4VmBDyCohSFBmtBQ-CVQjklHqx4gLGd4NloHCCOP7_3tEdF3vMqynrraBLFHhc_FJJecMKOYU3-7_VDd-M7shlJKWjlrh5t3d7AGYZLnsyU4PimTXPEgzYbpysBWrnNK5kkxxO2YCWmn6EN5oX1W3CxH_KPbqJWNB_trf_T5dtmcnn627OSINrqGzQ9Psq5ft8MiuZWt5VdEpWB5Fgh6fU8eIM4yjvPAnRUvIN73xfpkmHBnOLdhS43pppMucld3cQITuJ9Niy5vgnKLugs3yXc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55393f65b4.mp4?token=uf5NiIWbXQoBt7kKKRbeiFXfbbql_yUCzTZMisBDFtNW2JcX6YrgbL643-_dXsvIbsjAg1qHI-OgVBvVM7pYZpMkdvoQ7Qz3kyNrM9Gr3BYAUagMiD-XSY_bIweBTrZuDHJ-8aJf3l9BUWIAL4iaDj84XXwZb3zDK36EgdEQdo4qzEuHbp2iXrp7z3OYkMPJ6u9sMrtFqX6uIcbr8A2wo00cVceytFMVCSOsVsp1SjBV8YRKatmYQ7HizFumvvsE8NSUVu0doT0IACsGqWkt-2ehFEAHmXOFK9iDdymWDgJ78ThCi1OWj6pjUssxTzvyuPfCNq7uF8zisx8D4ApxuZ3kd2Q-fBRzAn1gL9X5v9H5uW3HE1Os8hhL60gzuErLZ_akX3HuN0FSX34QBsfr4VmBDyCohSFBmtBQ-CVQjklHqx4gLGd4NloHCCOP7_3tEdF3vMqynrraBLFHhc_FJJecMKOYU3-7_VDd-M7shlJKWjlrh5t3d7AGYZLnsyU4PimTXPEgzYbpysBWrnNK5kkxxO2YCWmn6EN5oX1W3CxH_KPbqJWNB_trf_T5dtmcnn627OSINrqGzQ9Psq5ft8MiuZWt5VdEpWB5Fgh6fU8eIM4yjvPAnRUvIN73xfpkmHBnOLdhS43pppMucld3cQITuJ9Niy5vgnKLugs3yXc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آماده‌سازی جایگاه پیکر مطهر رهبر شهید انقلاب در مسجد جمکران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/667502" target="_blank">📅 17:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667501">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aiVm1hKa52qykFcwydThuYnmuGaJYSjQkAZnzyyinbOLS-bLhcbHe0ocjNyu3GV9AySazsjXm2KmB3o3rgXFuDVJlEAkN06dRM12ppAYMVcLcRCo-uQeuOt4uy45caDZ-o4DqloeUtyLcKNsv8EoSj0Q1k5yx4e-KE65UKXlLBV9TwWm3fGwwSlIrhs1uPYkkt9_HlN_Q40X4q-DC7sR_8E5DgTsu1RK7_EeROyk60B3jo1Al-IMf5SNCnzSaHi9h_151HyrYuL2GYRVvf8Uybv3IBpaxVHcMdCrUluREycc-d9hirucLktm2Z3mE07Gu3EsTE5UOXH4vgKQNJTpcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران؛ یکی از معدود کشورهای دارای توانمندی گسترده فضایی
🔹
تنها ۳ کشور؛ آمریکا، چین و روسیه در هر ۵ شاخص کلیدی فناوری فضایی به خودکفایی کامل رسیده‌اند.
🔹
ایران در ۴ شاخص از ۵ شاخص توانمند است و از نظر تعداد شاخص‌های محقق‌شده، در کنار کشورهایی مانند ژاپن و کره‌جنوبی قرار می‌گیرد.
🔹
اما هنوز در فناوری بازگشت و سرنشین‌دار کردن فضاپیما به سطح کامل نرسیده است.
@amarfact</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/667501" target="_blank">📅 17:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667500">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJQ-SPS3NuJ2hr9gzbjCcPkrzg-9EaYbNMUgqOCZFLyT_RzOHwdr9f5HvcClYUdH9WHm1mHPZbElEgDdTCPd40x50qcaIFbO6vukKibR3Mfd8rNvGm78sQ8WQFeocWSUhSas0rRuVZV3SNaesyS1sK_WWDRhq00bFQ_9jdlXbamBrcTKvw9erWXsiYFmItTNCrPsNIAgy2tNbG7WWPk2TXsZBsQINDykO39_FMta6mV5L3gWJXFxI89z-lhGTr3RxJy0Xu3tKOMOZcFSZq2oyHYYy6NopXhIN4--Q_Se5eqNlVDtn5CLdT2OwArUH2GLTW7OvwyhSe2XB3gazooDKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهدی ترابی: اینجا نیامدیم که ترس از خطر کنیم؛ ننگا به ما اگر که ز خونت گذر کنیم
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/667500" target="_blank">📅 17:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667499">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
ترامپ دربارهٔ ایران: ما با ایران بسیار خوب پیش می‌رویم، اما فقط به‌اندازه‌ای که شایسته است، پوشش خبری دریافت نمی‌کنیم #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/667499" target="_blank">📅 17:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667498">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MP3aKSOmgenbE7DHQaCabHfaUwHm4Akz9GykU8Shm59v4645U0Mo--SfnneCo7Vh_8VMg7jSR7K3xI0SUj3LdsghY0pYzVcqXnKrT7S0GXH_zbuz5E8fpdWZoo-hYYdBKyPojL3yDfStZ44bNx6QEVvvWWw5UgdM59wb8Ac1R8nZ1z2xPWkigO9Z3E1S9dRoYIXHy1YTKi4N0dPQmJmuqP08fhtm4re8GBwuzsWT-ddxA_rO1PkRHyOsVEnId9QhssFf8iTjahzMDWmHp1DhdxAhj-V6KPVSVeQM4LOoLKUqFGdYP2EK3iT_tfRO5Ek1ohHtpbJhtu3HZpro2kXVJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فایننشال تایمز: تشییع میلیونی پیکر رهبر انقلاب اسلامی، او را به یکی از بزرگترین مراسم‌های تدفین در تاریخ معاصر تبدیل کرد.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/667498" target="_blank">📅 17:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667497">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی: تمهیدات لازم برای حضور ایمن مردم در مراسم تشییع فراهم است
ابراهیم عزیزی، رئیس کمیسیون امنیت ملی و سیاست خارجی مجلس در
#گفتگو
با خبرفوری:
🔹
مراسم وداع و نماز رهبر شهید انقلاب با نظم و امنیت کامل و بدون هیچ‌گونه خدشه‌ای برگزار شده و دستگاه‌های مرتبط و مسئول برای این مراسم همه تدابیر انتظامی و امنیتی را تدارک دیدند و جای هیچ‌گونه نگرانی نبوده و نخواهد بود.
🔹
همه ظرفیت‌ها پای کار هستند و همه مسیرها مورد تقویت امنیتی قرار دارند و به بهترین شکل ممکن این امکان برای حضور ایمن مردم عزیز فراهم است.
🔹
حضور میلیونی مردم را در یکی دو روز گذشته شاهد بودیم و بدون شک، این حضور یک نمایش قدرت اعلام خواهد شد و می‌تواند زمینه ساز تولید قدرت و اقتدار مضاعف باشد و دشمنان ملت بزرگ ایران را مأیوس کند.
🔹
بالغ بر صدها خبرنگار داخلی و خارجی دعوت شده‌اند و الان هم در ایران حضور دارند و گزارش‌هایی که دریافت کردیم، حکایت از این دارد که تمام دنیا مخصوصا شبکه‌ها و پایگاه‌های بزرگ خبری به این موضوع علاقه‌مند هستند و این رویداد بزرگ و اقدامات حماسی ملت ایران را ثبت می‌کنند.
#بدرقه_یار
@TV_Fori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/667497" target="_blank">📅 17:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667496">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسازمان منطقه آزاد کیش</strong></div>
<div class="tg-text">در روزهایی که بغض، سنگینی می‌کند و خیابان‌ها میزبان قدم‌های استوار و وفادار مردمی است که برای وداع با آقای شهید ایران آمده‌اند، قاب‌هایی خلق می‌شود که تا همیشه در حافظه این خاک می‌ماند.
اینجا در موکب عزای رهبر شهیدمان، همه فقط یک نام دارند: «خادم».
وقتی پای عشق و ارادت به میان می‌آید، عناوین و منصب‌ها رنگ می‌بازند؛
سازمان منطقه آزاد کیش نیز با برپایی موکب در مسیر تشییع پیکر مطهر رهبر شهید، آماده میزبانی از مردم وفادار ایران است.
در این مسیر، همه ما یک خانواده‌ایم…
🇮🇷
🏴
◾️
موکب های ویژه: آقایان | بانوان | مادران و کودکان
📍
محل استقرار: خیابان انقلاب، نرسیده به میدان فردوسی، خیابان شهید موسوی، روبروی مدرسه شاهد.
@kfzopr</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/667496" target="_blank">📅 17:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667495">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59e62eabb8.mp4?token=GmHtV6Yxa60PBTVZcWKEEm3PFLIuPYzoAnZ1TUtUrPajQlhmxCXrkmuLKqi6fPqxBaN2v6pxeE9v_XcYglhFOr-_4dxbkv6LaHOsLOdvzwaVe466pV4HcrYTUvPom4W4uVCjU9IT203EzT2wLwFYvVWBdFSm5o0xf-_CNCO7cxSl0oE_dGbwyGPX3Y57I7xAd-F60tcgYf0uqYxmCURMQ2SgI0tTJ4WZtlkvnHpwefB6RkFLz3cHaUV5A1TwH56QP5bxcx_-CoBug2uI6pj_swK2YJk9dEqT-hiuaq5Zohrwmlhx2f1doL-MGPtlFaKUbfg_a1gtHKOeHmbTXd1oXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59e62eabb8.mp4?token=GmHtV6Yxa60PBTVZcWKEEm3PFLIuPYzoAnZ1TUtUrPajQlhmxCXrkmuLKqi6fPqxBaN2v6pxeE9v_XcYglhFOr-_4dxbkv6LaHOsLOdvzwaVe466pV4HcrYTUvPom4W4uVCjU9IT203EzT2wLwFYvVWBdFSm5o0xf-_CNCO7cxSl0oE_dGbwyGPX3Y57I7xAd-F60tcgYf0uqYxmCURMQ2SgI0tTJ4WZtlkvnHpwefB6RkFLz3cHaUV5A1TwH56QP5bxcx_-CoBug2uI6pj_swK2YJk9dEqT-hiuaq5Zohrwmlhx2f1doL-MGPtlFaKUbfg_a1gtHKOeHmbTXd1oXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار خبرفوری: در ساعات پایانی تشییع تاریخی رهبر شهید انقلاب هستیم؛ همچنان مردم در خیابان‌ها وجود دارند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/667495" target="_blank">📅 17:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667494">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Op75TLXVMsl8CXAMJBK-JeaFoPteN7zOcM1IaZX18-mmPCIM18g3mpHXh7IlMhPfgPQXlVBmrOPsKPy9vIIuyo3ikQIPToVlJuuqVACt-b83PKJV2nTXquRbVyO1AevXeKTIMkWmsTnMGW_x7Q7FrJVApva4Xg0qCQ9xPaN_zB0OA-T-jE2H-KHI4a0UIQlw7BDhxmuiiiTCsQ2BxudX0uJqQO6g384BSEMJ1_es9oFhqOJv5Y1akX4DoQiXN6M2dmSisn-HUKPdvLkLpafGPmN-0mZR5beNMr1Kfh2Qh_riXxDMlOLsJfTUH_tKRewwjy_bYD4BqA13IjTpk6QByA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارتش رژیم صهیونیستی شهرک «برعشیت» در اطراف بنت جبیل را هدف گلوله‌باران توپخانه‌ای قرار داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/667494" target="_blank">📅 17:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667493">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwiBg5LKx2SszBrB6z9i7s16Y-PnC_qrgVD5dH2XIYUHQ3yapTQiL9317UNPUZhRdJOPeCqxgo-hhBWXZcMW1lScUFBKUL5W_9CAv2r_0C7e98dl9SXa5nB6STW1R5gPGnvMr7iUaZILSFVZFAxCI0CPAWdT12byduo1OX2eYPd42V7t1tyIq49EFFQq14EDPm-wdZaPv1j8l5k1b_oXMMyyiXtF1y7dKUACEvfFt5ZRigF6y1z7WQrB635RiuTxD5VpNhJcnKkjasVvAd5vV11KTKmbKAodoeiW4VlD8SdcoYta2Im92j4pVeiER1JpqeEo8cRkRuwL3SaCuoLk5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از حضور میلیونی مردم در تشییع پیکر رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/667493" target="_blank">📅 17:27 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667491">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
ترامپ دربارهٔ ایران: ما با ایران بسیار خوب پیش می‌رویم، اما فقط به‌اندازه‌ای که شایسته است، پوشش خبری دریافت نمی‌کنیم
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/667491" target="_blank">📅 17:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667490">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WThRSef8odzCzuAe9Pl5cdUMTU1t5JtUWWluiCEP-uzzQsX-SzM6RzEQSQYzx07VacVKPSHgZg4sZIh7fPP_sqPb8asYiih5_wDuOjP5SBROwVbCiyVUKALF3_OEoRjOPPdXYB-f3MiDLEVuR_3AFci6c1bCx2taVRaYCEORDdf4Mec1327vL8Auw58Qvqh4lElIa2pvvxvEX7SA89umtQ8UYP_iahOVLR0MMVcMJ_ppxi1m21vKfxFYOgR-fb01iTs4UPG1SdSEVDE_Ve8LWBMxOgo5ydxZ7qBudpYJSM1yDVXalxZOaDz8tj04jkVgIIVF71PLmyVMz2vb5SPERQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استوری پردیس احمدیه پس از شرکت در تشییع رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/667490" target="_blank">📅 17:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667489">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
لحظات پایانی مراسم تشییع پیکر رهبر شهید انقلاب در تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/667489" target="_blank">📅 17:06 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667488">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbOJzgoaINujRpotDJnoX07oflnX2F8u1ut3xpIGc9tUpRYkZUC0olmm8cyDtwpxFjOwfOW1ks8mQUPRu3Xxrxm6uqcvRV3Jplv2UBDKSEbHpXwXreXwWp3Q6GIfytPTfCQlmQWqUmcEztrXvf9BREGGP16RDXrgmcF1jhouAYo1jJ31A0YxnukXv6AAjzbTrXB_jbcsSeD8_BhTqj4koP9mM5CngYO8lVIslP2MLiQxMcuap402IVY5wRxbT5yNxWpeQkVsBO24BZ4kmkX92MS8ya5vXAsZbieB2rUJP298PV48XJg0xRfYG9LxQBByO65qA19P4wKECb6IGAx6RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آتش‌سوزی انبار لوله و لوازم ساختمانی در خیابان سعدی
«ملکی» سخنگوی سازمان آتش‌نشانی:
🔹
دقایقی پیش آتش‌سوزی انبار یک‌طبقه لوله و لوازم ساختمانی در محدوده خیابان سعدی گزارش شد.
🔹
عوامل ۳ ایستگاه آتش‌نشانی به محل حادثه اعزام شده و در حال مهار آتش هستند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/667488" target="_blank">📅 17:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667487">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ir3eOQbWEBLoDJ60-Lc5wtH90h46-_Z2SN7IBOcqUphcJzxjBhajinaPMy9d7AO1pNgfJg7CThRe5q6lnsQQyOgOpPRrGaxkc20OGg7_fMyERtsAdxOqnT1KS_jEKGMjYwbTg_fqs4N0d30BVLZCPle5CSakphVO3iTLBgLKnYFMY9LmKTOF-1t4QXzO4-f9gI1QEsmuIT9d_Lxk-G0fKGY6H8UBUTPvUVZodexoDoHCdL_xEeXJ64zcrTX8tJAMJ4aKDq4ZuZduQprQMiuvriaJtyuy_pJSusLG-7_bRaoSkM78Sf6Zxz4WxQjV0wtLNRp4wYkOBSyF3co-015KQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور وحید شمسایی در تشییع رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/667487" target="_blank">📅 17:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667486">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93e4ca20bd.mp4?token=huIYnYIJuk_S1y6y7NPNKi1May3fxSHtEdc8M5n4azcbBM3Crym9mgZ2694hqFNh-S6LIGjXg9fR6-E5Ye0-49EawOW7-Kwa7fhECLiy5qe2AfTFwjxm3H8e1Kq7SSpajOr6A0XO1XFkY19DLN1kDIXq5-UDWKVCn5Q2_PrbNwwzsxde7vAn2WVoXfnfQ7-5GpmGKRnaNZQDHkxIYV0d5YheYqnaqueqhTNT3zYDE5usFwwvz8q931s8th0aF-VOQoCTj0p3ioQ8TYs45hR1O-iNYxy4QDnoKlGEYO5S9dzrTscMLPTZ8hXQDHZoJaxypNnmSU63JeGrqM_aiUT_SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93e4ca20bd.mp4?token=huIYnYIJuk_S1y6y7NPNKi1May3fxSHtEdc8M5n4azcbBM3Crym9mgZ2694hqFNh-S6LIGjXg9fR6-E5Ye0-49EawOW7-Kwa7fhECLiy5qe2AfTFwjxm3H8e1Kq7SSpajOr6A0XO1XFkY19DLN1kDIXq5-UDWKVCn5Q2_PrbNwwzsxde7vAn2WVoXfnfQ7-5GpmGKRnaNZQDHkxIYV0d5YheYqnaqueqhTNT3zYDE5usFwwvz8q931s8th0aF-VOQoCTj0p3ioQ8TYs45hR1O-iNYxy4QDnoKlGEYO5S9dzrTscMLPTZ8hXQDHZoJaxypNnmSU63JeGrqM_aiUT_SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امروز حسرت تهران جاودانه شد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/667486" target="_blank">📅 16:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667485">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2b2cc71a3.mp4?token=BIjyVvZnAd_-EUHICDIjN7WQ0b8Csw4Fii3Mn19rrASTabAC5OYrzMCKACCdtMzmcBLOVhXEtDlaSc7mWaRGwzWv5adx0CJPylNcQFmOADH6NTkoGozQ0qB-2XTUb3urbvcw6Bt9xzl7rUDL92ka6GBPAP6GHD6-9ywRKMF1kAL4OXUDNk9ENO25v0EZMEe9F1PZ8fU-XRI32xtYyPHQy-MNVyIxO8u_PEQiNFiaEj-AFCazh7q11-iYbrT-A5ZGIHYfunce3tgxS2j-INnVR-boRKEtwUIsoTUTWxKiYJyrO3dhirye1B464GzmkL3CChPbn0Sk6tyMF88MtI-hOVGbpaVhJDfaYBDZwRKTu4c_NCnMu7WsgCTIW2EkZvBm_nFykNyKsxQt2I7qgNaSCfvUNxoIr6PyexMbQoRFOJQP4EBlNAID7CZrz31WLAH8N4cFrjIaf0jiuo95-L1qPozl0RjYmoAQSMAc5ByNFqxLV-PFiiqgQE6JIjaksAd6T8dUpmDeNTgmgl6wKou0pwUoLYGbZfweH6gCmMT5q5_tfbL_5m1RD5yF1Hd1OH0nZdlPV9HhWBVX_9-cpgYayY9JXcwGZkzQI0yqT-XywuNqWWX6B2iNDbJI8Tjc_OZjDHHgDQpWqauqLIWYRVTZsZVylNNASJcb-JTBp42eeXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2b2cc71a3.mp4?token=BIjyVvZnAd_-EUHICDIjN7WQ0b8Csw4Fii3Mn19rrASTabAC5OYrzMCKACCdtMzmcBLOVhXEtDlaSc7mWaRGwzWv5adx0CJPylNcQFmOADH6NTkoGozQ0qB-2XTUb3urbvcw6Bt9xzl7rUDL92ka6GBPAP6GHD6-9ywRKMF1kAL4OXUDNk9ENO25v0EZMEe9F1PZ8fU-XRI32xtYyPHQy-MNVyIxO8u_PEQiNFiaEj-AFCazh7q11-iYbrT-A5ZGIHYfunce3tgxS2j-INnVR-boRKEtwUIsoTUTWxKiYJyrO3dhirye1B464GzmkL3CChPbn0Sk6tyMF88MtI-hOVGbpaVhJDfaYBDZwRKTu4c_NCnMu7WsgCTIW2EkZvBm_nFykNyKsxQt2I7qgNaSCfvUNxoIr6PyexMbQoRFOJQP4EBlNAID7CZrz31WLAH8N4cFrjIaf0jiuo95-L1qPozl0RjYmoAQSMAc5ByNFqxLV-PFiiqgQE6JIjaksAd6T8dUpmDeNTgmgl6wKou0pwUoLYGbZfweH6gCmMT5q5_tfbL_5m1RD5yF1Hd1OH0nZdlPV9HhWBVX_9-cpgYayY9JXcwGZkzQI0yqT-XywuNqWWX6B2iNDbJI8Tjc_OZjDHHgDQpWqauqLIWYRVTZsZVylNNASJcb-JTBp42eeXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زائر کازرونی رهبر شهید خطاب به رهبر انقلاب: آمده‌ام که بیعت کنم؛ مثل ۱۵ خرداد ۱۳۶۸ که با رهبر شهید بیعت کردم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/667485" target="_blank">📅 16:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667484">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e931922545.mp4?token=RZyMa7mx9ejTlm49Cx-PxFBl9Vtq5jZaW4_fiscvczZ9zBEToSbyJN-b8OFHR7OBQO_yQnE0J9QnBg-7GudZxrEXYsAznSC2ZHqdFsNrOTuioQM5XYBS1GGtBN3pp1ae77egqqLd3ZfaQdO4iiyq70Jdq7ksy-cl6bE214CnBTUy4qzc7WlkJXLWqRjPfyNKEzrOHY1w7cqbNFA0UZiIeEpBhwhkR3qMuf3zrD8JBZ9AYjUCb7Bvvq7FFHsmj7U6g2glazMuLHxSHTQ4qc0PuxVOiso-iU1UgFAQI9m_0W5FmbW8FMCNiQHF4370Ym19rAq8DlkIUxSbBlCCkYGweXDtYAytT9yXrih1smi91Nsip6K3m9ro4a467BYAN7906W_A9bU52TkbTHXUP9he18afxHF8J7jB22ZVX1GHkwcVF8V7LEK8LLm0yn60yqcoOnnX8kq3q4RKLXLXXlt8Hi7t4ktYLLcWkt_Kk8pWKdpYExW8PCTVvIUjO3LidcL9h0BAq0in8_PJLhf-EW-gowb3SG1emzUFCMpWMIQop-acJYBs4MmbDyGSM7KiGbb30b12ybSYOtyD-UYApGEyZfBFmTMcQpIW3mAPwm_NdyRWnsorFsfRdGL4vZoa9TjiKw52vDcEDD8a0ktsh2LzNabgPgZD4dUZB_0Y-2TFfRE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e931922545.mp4?token=RZyMa7mx9ejTlm49Cx-PxFBl9Vtq5jZaW4_fiscvczZ9zBEToSbyJN-b8OFHR7OBQO_yQnE0J9QnBg-7GudZxrEXYsAznSC2ZHqdFsNrOTuioQM5XYBS1GGtBN3pp1ae77egqqLd3ZfaQdO4iiyq70Jdq7ksy-cl6bE214CnBTUy4qzc7WlkJXLWqRjPfyNKEzrOHY1w7cqbNFA0UZiIeEpBhwhkR3qMuf3zrD8JBZ9AYjUCb7Bvvq7FFHsmj7U6g2glazMuLHxSHTQ4qc0PuxVOiso-iU1UgFAQI9m_0W5FmbW8FMCNiQHF4370Ym19rAq8DlkIUxSbBlCCkYGweXDtYAytT9yXrih1smi91Nsip6K3m9ro4a467BYAN7906W_A9bU52TkbTHXUP9he18afxHF8J7jB22ZVX1GHkwcVF8V7LEK8LLm0yn60yqcoOnnX8kq3q4RKLXLXXlt8Hi7t4ktYLLcWkt_Kk8pWKdpYExW8PCTVvIUjO3LidcL9h0BAq0in8_PJLhf-EW-gowb3SG1emzUFCMpWMIQop-acJYBs4MmbDyGSM7KiGbb30b12ybSYOtyD-UYApGEyZfBFmTMcQpIW3mAPwm_NdyRWnsorFsfRdGL4vZoa9TjiKw52vDcEDD8a0ktsh2LzNabgPgZD4dUZB_0Y-2TFfRE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زائر اهوازی خطاب به رهبر شهید: شهادتتان مبارکت باشد
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/667484" target="_blank">📅 16:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667483">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPy8kiE3HhlMOFtWaNGkGh1w4GdWjSoPCy3dholsOvc32R6eEqgt41qU0R9x9o18dwww9aJRSDOMHGqqz6pIyGHJWagnVtt4ECoB0BuJHSnlCP85YVa2XtYbacQdTQ3imqwPfGZqk8hceG0AcG1zFSRB0hflh7PtaP2kMKIAHirdDXVDlzBXNyGIM9dDhx0pK6nxg6O-lQjRtsP5ePiMn6vmg8IM_B1qpR4IIW6e5YfytTp3omeRD8H-Oks6ohFUeUXX71CV0gIQcR5jvgZ3Ff1nuFy6rMcSPj0ZSN6ZtvmjnHe5EkM3Q875-4u5lr91uURLsXD7IHxuJEX90ZLY6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری متفاوت از تشییع پیکر رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/667483" target="_blank">📅 16:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667482">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4rcgwJAExC_0jk563ZK-_8_IzpEgBFb1yvC4iCS6F54y_XjvVlbHGEUelGrcWPk4u5Vlx8kU9CywBMKNld79wwoY3AFmHB53LGa4pymLHYq9PccNb0sQ0IbUd2Fxb4nwJwbvHqfvidaPjVnQbWV4D3FNCGnh_SyqePbuAs3l2ZEk4AlwY7t5zEZ8O16aMteH9jrg3oO3vt8xxGeXtMuK43Qhx1f6Q2h4Sp2sbl8Ppu72bUwIwEdP-yRIGSlMAsod0nDr9fTAGXjZ8sEY-mSQQV78_E-HP7susUbpGad2T8sp9wrUV_5FsZaXQx1OVntwhA3FzJ1f82FRkvmUDcZoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عارف: تنبیه قاتلین رهبر شهید مطالبه برحق ملت و تکلیف حاکمیتی است
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/667482" target="_blank">📅 16:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667481">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
زائر کوچک رهبر شهید: مردم ایران؛ این خاک‌را با تمام وجودتان نگهدارید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/667481" target="_blank">📅 16:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667480">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ولایتمدار: دولت عراق مسئولیت کامل امنیت مراسم تشییع را بر عهده گرفته است
سالار ولایتمدار، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
شهادت رهبر انقلاب مانند شهادت امام حسین(ع) یک بعثت جهانی ایجاد کرده  و این خون پاک، نظام را تثبیت و تحکیم کرده و دشمن را در محاسباتش دچار خطا کرده است.
🔹
دولت عراق مسئولیت کامل امنیت مراسم تشییع را بر عهده گرفته و تمام تمهیدات آشکار و پنهان برای جلوگیری از هرگونه حادثه دیده شده و مردم عراق با اشتیاق فراوان درخواست برگزاری این مراسم را داشتند.
🔹
با وجود گرمای شدید هوا ، مردم با صبوری و عشق در مراسم شرکت کردند و این حضور نشان داد که ایران برای سال‌ها در مسیر تثبیت و تحکیم نظام گام برخواهد داشت.
🔹
شهادت رهبر انقلاب، مقدمه‌ای برای گام دوم انقلاب و جهشی بزرگ در حرکت نظام اسلامی است و امیدواریم این حرکت به ظهور امام زمان(عج) منجر شود.
#بدرقه_یار
@TV_Fori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/667480" target="_blank">📅 16:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667479">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
رئیس سازمان اورژانس کشور: تاکنون هیچ مورد فوتی در مراسم تشییع رهبر شهید ثبت نشده است
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/667479" target="_blank">📅 16:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667478">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1SwF6_wJdGUff4WYfreNrGx2KMo6geU7eexucxVk6LxFYu_jk9gwbv0kPCd7fU2jNFOdc3Bs-ICdHoA7ciIst916c_VpIfCvKUcHS-G9QWR511LWf82fKD80Nk1wHZv7NpRXU7dqmb_e25IOpE0zrglMMJ0KUGwff6SLz2NaxursoGbGo5HdQXbh2ywNKBCI3SYDn8DbNj_sA9uJmmOJeu6MnbV9rFufwOonMrc5LU9Q58xKJCN1jFzkaaq7uWZf0HPXezEKh9SrzO7KudbLtG5ZGR3wO-NgOO7XLJpEl0CuwswWbbba2OmBrwsyfKAzzBLKQ1s1nIlq6bWJUSwYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ از فیفا به خاطر بخشش کارت قرمز بازیکن آمریکا تشکر کرد! #جام_تایم۲۶  #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/667478" target="_blank">📅 16:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667477">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n22Br_NZ2rltXlvlLrV4PC4nBuYQhDbXzGTC74_fdRfdMDc4U5dxceAevgyCOGt0wzOSzp7vjGKRxjsW2q3_1et2SxIteafT_0Ifokt7XhpDBrY0u3F9eDk3RsRrD8Rhem2-F6-7lEOpIoJ4ucGXkWq8Rc_dlMTYVd7muOptcpxUVT_5fFGgumlvTzZutuzyDyDakJ2KpMGi-psmkHK9r4tPPyZwhvd6MBe4b1fH1trSbdwoqjbX-4t4_Nfay-nGhqj0V24c8xqtb9JJtu4iXD71QAEGvv0GaKL1Zo-C6EbXN_NU2zw-VVWBFwg-78PVCQGY1fNxmBkAR6XAcenOmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
استوری هادی چوپان، قهرمان جهان هم‌زمان با تشییع قائد شهید امت حضرت آیت‌الله خامنه‌ای
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/667477" target="_blank">📅 16:35 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667476">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
نجف آماده میزبانی رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/667476" target="_blank">📅 16:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667475">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنیرو آنلاین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rU8ACcXCN1erJuZsfzPg9g44bk683jBOyKf9Ih9cjnTRzyzeVcTLs5LbI49fDW0xC1K_fZaFzKNdUrv77ajLw_A8WJrHhrGiGfF0off8SYGFRC0eDnm36-04gUpjOVe-bn0w24_mK7ekhzul75qLdh9acu5ks98aonEX3ROReM-9wATbW5dQMWJNj5TS2Hz3oSeFDberzhry0ZX76f5slqcpkviunX_NAm_7hN69HkTrWEhMzvl39gNlb_eufp5RbOfxaFrh6KuLyV_TiE8xanYcp2yf5P5R-TEdIhln4G_vrh2bDZCCAWMOPSASzhxrgeDYRI29ltNEqPphw660eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر نیرو در مراسم تشییع رهبر شهید انقلاب:
⚡️
💧
ایران با هدایت آن امام شهید به الگویی برای
آزادگان جهان تبدیل شد/ دست خدمتگزاران صنعت آب و برق در مراسم وداع و تشییع رهبر شهید را می‌بوسم
🔹
وزیر نیرو روز دوشنبه در مراسم تشییع رهبر شهید انقلاب و خانواده معزز ایشان در شهر تهران، با اشاره به ویژگی‌های برجسته آن امام شهید و دستاوردهای بزرگ کشور در دوران زعامت ایشان، گفت: جمهوری اسلامی ایران در سایه رهبری حکیمانه آن بزرگوار، در بسیاری از حوزه‌های راهبردی از جمله صنعت آب و برق به خودکفایی رسید و به کشوری الگو برای همه آزادگان جهان تبدیل شد.
🔸
عباس علی‌آبادی در حاشیه مراسم تشییع رهبر شهید انقلاب و خانواده معزز ایشان در شهر تهران گفت: رهبر شهید انقلاب با ایمان راسخ، اخلاص، شجاعت، آینده‌نگری و اتکا به ظرفیت‌های مردم، مسیر عزت و پیشرفت ایران اسلامی را هموار ساخت و روحیه خودباوری را در میان ملت و به‌ویژه متخصصان کشور زنده کرد.
🌐
[
مشروح خبر
]
#باید_برخاست
#عزیز_ایران
#صنعت_آب
#صنعت_برق
@niroonline</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/667475" target="_blank">📅 16:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667474">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boj5TZSSNo5HOA-_E-UBYGPskXcn6jTdrng68QY1YoVBBvzTcWvLSmkPVDjaLBcSCAgIZL7Rqh6xDOaup9-S6Hp_A8tjoVzMpFhO6Kv8oIJUsb-_1rKvNf78HZqLaiA9r5m580wFneTlMOqATU3hjppIZvnsiMR4-dZjnA1DKKoFRycGZa71u1mVY63e_7n0JGlbKgoTcsnb-AJlt6N0mMl9iApNwSqo-eHKOxfuPThC-QbSm5jKMT91kYY9tLHkJJZivZ1eKGnSgo-LHwwAMVKSYVCHYtvAwv8xEu8JUOLxjpjFlkMxNBaS5WI7ItRsSIYpIyCvh592j5boxhFAgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش محسن چاوشی به تشییع امام شهید
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/667474" target="_blank">📅 16:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667473">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqnI9UaImI6ijJhmUvIFcoA5KUPhRFB2oVADpKGHC3hhnKZ58Rp6n84ZE1xkp6E3RD-f__ynxi76qtY-MgPyyaEjB8lYmA23-0PvOb9Zh_sqxHHe8eqt7C4ghpA-10YwjBIQbqzW0doerf-pwpCUCHwmeXykRfOhWjg4aC5X_6nOh_qzj1Br9ketAf23C_TdeeEXKgpld9v2BW02Ipmz3rMTrMvtLNenpXSi4MYiafl0qICuMdWI77Nsb5ssn6_F0-i68EdRGw7ELsaDMrBO657OuZTMvhHrSpIX6aOrdody5XyPwLj8vaVQ9N-eA2F8dXhLl8JcJUDUvAkNrZF9OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت مراسم تشییع رهبر شهید؛ پویش مچ‌بند سرخ
🔹
مخاطبان عزیز خبرفوری، برای شرکت در این فراخوان کافی است با یک مچ‌بند سرخ در مراسم تشییع حاضر شوید و تصویری از حضور خود با مچ بند سرخ را با ما به اشتراک بگذارید.
🔹
مچ‌بند سرخ، پارچه‌ای به رنگ خون و نمادی از عهد، وفاداری و خون‌خواهی امام‌ شهید است.
🔹
بیایید در مراسم تشییع با مچ‌بندهای سرخ حاضر شویم تا پیام ایستادگی، حق‌طلبی و عدالت‌خواهی را به نمایش بگذاریم؛ پیامی که نشان می‌دهد یاد شهیدان زنده است و جنایت و ترور از حافظه امت اسلامی پاک نخواهد شد و همواره خون شهیدان خود را مطالبه می‌کند.
🔸
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/akhbarefori/667473" target="_blank">📅 16:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667472">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مدیر فرودگاه مهرآباد: از صبح سه‌شنبه پروازها با اولویت مسیر تهران-مشهد از سر گرفته خواهد شد.
🔹
دانشگاه فردوسی مشهد ۳ روز تعطیل شد.
🔹
اکسیوس: ونس را باید جانشین نهایی ترامپ دانست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/667472" target="_blank">📅 16:27 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667471">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
۳ میلیون و ۲۵۲ هزار سفر در مترو تهران ثبت شد
هادی زند، مدیر ارتباطات و امور بین‌الملل شرکت بهره‌برداری مترو تهران در
#گفتگو
با خبرفوری:
🔹
درحال حاضر تمام ایستگاه‌ها فعال است و پذیرش مسافر انجام می‌شود و هیچ ایستگاهی از مترو درحال حاضر تعطیل نیست.
🔹
از ساعت ۲۴ تا ساعت ۱۲ ، تعداد قطارهای اعزامی ۱۰۷۵ حرکت، تعداد مسافرین ۲،۰۳۳،۰۲۸ و تعداد سفر انجام شده ۳،۲۵۲،۸۴۵ سفر می‌باشد.
#بدرقه_یار
@TV_Fori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/667471" target="_blank">📅 16:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667470">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bwh3aTTGhABQFt4RSp507zUKr20yHCLomCwiMaowd2TyhvWSEzwN8Nhogon_1yLcpTEsbSrVxDq0_mlGVOc84pc1Ohb7nPPImF4Hz3rD_gsrtFWEBwBszQ5ywtSRSNJ_X_wv2RU0aVd6sA-ZQejZ9FIXCtAgIajnM04kDFf55Y7dW_wWjq4t4uc2TjF2uh3SRVKNoz5jGgMF7kE13LNlULFfbCUwSZ5BM1SodXu5UDIOS3sUYPsHPzUg7qCTJ31eBBHy4CHHUPg9W1gzFLYJxWzPjXt63slIlQWl2w0Ehxxx3VLL5oFQbnfSvSvJpkBJHJoAksD6NpI_sLyUFU8rsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری متفاوت از مراسم امروز تشییع پیکر رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/667470" target="_blank">📅 16:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667469">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_c6GUCbRpA4VaVM_gzXnLqXnO8XVzq3QGoNnTnsV6JorlGHWuCIGTNKfLem2TaCjiCEbuBbM-ieKN_zmG2F6kouFRJmpm8cyrPCifCpZz4wASfHsiATauUH7Wj5U4r171okWSExqu89KDn0ayRfJzo6qK52WMYAQ0bIICotFhE-4AJxUw2P5za8w0lQLR_OThfWLcC9CkCO5M1YjBcepfib_rgk3Bq_6YP82mmNuieQgEdBsfqAPqymQgk-ftL-V27IgNPmOI_Owkd7DnCPTwjlcmngaZYXWqkmrYuO8NHXq3l-5rdV_5PWq9h-ADdUyC8p0x-LmBqfca_MuGNcCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از تلاش عکاسان خبری برای ثبت لحظات ناب آخرین وداع تهرانی‌ها با رهبر شهید
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/667469" target="_blank">📅 16:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667468">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085a135350.mp4?token=Bctb75nqur4IgSsQRHUfbkzNVDtF2kQkQXnA_GqSelwzb_fJ9T3wCYOFVe8Lb13njCcH0Xb2zrKux6On-gigZZK6iTDXiy5i-iTeqsn6VTYfM7xEE-XNauanU9UXBRSFnrBkR0YQW0mKyK8S02OZy1ybRvicTUdmonl8gdoS94M3PWQ5w6v6lEM9gl_E0aaNSUauB7v5nRNmL7BkVSncxhKwlaci6zc2AmvEglpUHga_r2y5zP-kJaAsgwe0j0xgiFzS2XROMDWRe8eh3r8l77icJerwDwR-ZhERR1kORchAwY2XPz7y6gr-aITC3WDN_kpwdUJadgfTb5CnrXlonw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085a135350.mp4?token=Bctb75nqur4IgSsQRHUfbkzNVDtF2kQkQXnA_GqSelwzb_fJ9T3wCYOFVe8Lb13njCcH0Xb2zrKux6On-gigZZK6iTDXiy5i-iTeqsn6VTYfM7xEE-XNauanU9UXBRSFnrBkR0YQW0mKyK8S02OZy1ybRvicTUdmonl8gdoS94M3PWQ5w6v6lEM9gl_E0aaNSUauB7v5nRNmL7BkVSncxhKwlaci6zc2AmvEglpUHga_r2y5zP-kJaAsgwe0j0xgiFzS2XROMDWRe8eh3r8l77icJerwDwR-ZhERR1kORchAwY2XPz7y6gr-aITC3WDN_kpwdUJadgfTb5CnrXlonw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام شهروندان تونسی به قائد شهید امت
🔹
جمعی از شهروندان تونسی همزمان با برگزاری مراسم وداع و تشییع پیکر آیت‌الله خامنه‌ای، با حضور در برابر نمایندگی فرهنگی ایران به مقام ایشان ادای احترام کردند.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/667468" target="_blank">📅 16:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667467">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bec9d18c6e.mp4?token=CATaOZxvGDOMI5sYL8c-VCoTVAGiuemC9VLa8Ul0w40LzYiemTOiyiJyVnN-aac9u3_2CXbOAeLn1A1w3kTrMvy0kRvNvjusGqNb1h5oorFBjIKxg-EuDX6GrIDZTlGUE6xZR1kf5QCHWzzjOfgsomlgiSuchrs_VmlsQI3A7AhT8o8AD-DSzgPKwo-c7OaDVL5TlQvto6XUhlag03zRH7Ic19CcSRKavvPYdQkOsbxNrJe-pkCHGCSgTd1abJtlXgEjG0e8nFRnS5rSjAyHw7DEQvcE1KeXb4fQ6cUBVUMTOarOlLCPXYR4Zp-SL6GOLJ36O9Ua2L47B1T8-n0Gu5zOPKv3jh3ZUEqjfNhHgHtJk54irDrs0X8mZ_X6v_qMb-bKt1L5fkd_psCyAlpRMC9WH02ksXd1zfG-GY3M9ojLjGiOpSu-EEcbdpPNWP-B8NXBydArU72cBwd-1LiuPrkI5-ARk49yyadLvMyiTCZtD37CuBW63u-HYAFGIekTLPRlUZ-XyOy8voJ_Bplzg0oxI9dqiQVQeqcp0ZxL-aAU4gBwGIpef7cYFs_QoEFLX7k6R81n_zHLPYoFT2nvFPXIIyYep9Ywm_GxN76fwl54PbCPtONLVe70beONf3dlnX12_zWWSeY1lak3TGsUQjf6YOKjWrE_0nJb2H6aw0Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bec9d18c6e.mp4?token=CATaOZxvGDOMI5sYL8c-VCoTVAGiuemC9VLa8Ul0w40LzYiemTOiyiJyVnN-aac9u3_2CXbOAeLn1A1w3kTrMvy0kRvNvjusGqNb1h5oorFBjIKxg-EuDX6GrIDZTlGUE6xZR1kf5QCHWzzjOfgsomlgiSuchrs_VmlsQI3A7AhT8o8AD-DSzgPKwo-c7OaDVL5TlQvto6XUhlag03zRH7Ic19CcSRKavvPYdQkOsbxNrJe-pkCHGCSgTd1abJtlXgEjG0e8nFRnS5rSjAyHw7DEQvcE1KeXb4fQ6cUBVUMTOarOlLCPXYR4Zp-SL6GOLJ36O9Ua2L47B1T8-n0Gu5zOPKv3jh3ZUEqjfNhHgHtJk54irDrs0X8mZ_X6v_qMb-bKt1L5fkd_psCyAlpRMC9WH02ksXd1zfG-GY3M9ojLjGiOpSu-EEcbdpPNWP-B8NXBydArU72cBwd-1LiuPrkI5-ARk49yyadLvMyiTCZtD37CuBW63u-HYAFGIekTLPRlUZ-XyOy8voJ_Bplzg0oxI9dqiQVQeqcp0ZxL-aAU4gBwGIpef7cYFs_QoEFLX7k6R81n_zHLPYoFT2nvFPXIIyYep9Ywm_GxN76fwl54PbCPtONLVe70beONf3dlnX12_zWWSeY1lak3TGsUQjf6YOKjWrE_0nJb2H6aw0Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر امروز، روایتگر حضور گسترده مردمی است که از نقاط مختلف کشور برای شرکت در مراسم وداع با رهبر شهید گرد هم آمدند؛ حضوری که به یکی از ماندگارترین قاب‌های این روز تبدیل شد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/667467" target="_blank">📅 16:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667466">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfaf582995.mp4?token=gfhczFSDYCWLOgmAjrMvfaKBlLXr8jTcXExQK8sExWHZsMc3xncVrUyHziFQvDWjjGZfr30KE0Ap5_3qTpgdwoUXIK4Vzk5GOogBd-0ErKdxp2n2hD4YN67Im9q2edYCsPIAYszzsExUUGbxMMkvxG-NJl1la_Zspt4HoKkufcNXMHv-4VjRo0cNwbhTX7kADXxmc-6MGMkktO8Zb3VS8aIbyuU67UO09JhbWKyO8amzsnRSFswgai0ICHRab7S5eOqMwvfgM9u8soSxNIB6JvlU9Bb9UFcDr7g9wpclPZXsmfB9Srd1JFIOT7vpvcAd9-3ikmbyJ6bu8bi4FhAD4Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfaf582995.mp4?token=gfhczFSDYCWLOgmAjrMvfaKBlLXr8jTcXExQK8sExWHZsMc3xncVrUyHziFQvDWjjGZfr30KE0Ap5_3qTpgdwoUXIK4Vzk5GOogBd-0ErKdxp2n2hD4YN67Im9q2edYCsPIAYszzsExUUGbxMMkvxG-NJl1la_Zspt4HoKkufcNXMHv-4VjRo0cNwbhTX7kADXxmc-6MGMkktO8Zb3VS8aIbyuU67UO09JhbWKyO8amzsnRSFswgai0ICHRab7S5eOqMwvfgM9u8soSxNIB6JvlU9Bb9UFcDr7g9wpclPZXsmfB9Srd1JFIOT7vpvcAd9-3ikmbyJ6bu8bi4FhAD4Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظات پایانی تشییع آقای شهید ایران در تهران
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/667466" target="_blank">📅 16:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667465">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d72c272a90.mp4?token=eXVR1pE_nz9yYS2w7m2vMr_sDgM6CzwytR59amqdRxeAcxEaWTudp3d-rH984o4VQI61H_zWwA7XhV_op9zAyOZV4h9-IuVUMEL_IIlhhvI7ZxkVqiNTQxdgL05hE4JFn9CzM1bIgj4dwWQon9kHVnINxHJJoDInDujhAC2FKler46is1_CM7QUrWlva8tod6KRwsrY5h6b52A0tPKL6ZLmUHmVvFAf0B_S-kOeDR8_8Rna9hAoCfcY_RdsD8y1argoaJb2QPADjJiXJgqcbRR3eptWNHD1AmWKTGyQT08jhNkEZQ4TvhsUpMx-2HPwQztvaUAoAR4pDaaQ4Lbfs9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d72c272a90.mp4?token=eXVR1pE_nz9yYS2w7m2vMr_sDgM6CzwytR59amqdRxeAcxEaWTudp3d-rH984o4VQI61H_zWwA7XhV_op9zAyOZV4h9-IuVUMEL_IIlhhvI7ZxkVqiNTQxdgL05hE4JFn9CzM1bIgj4dwWQon9kHVnINxHJJoDInDujhAC2FKler46is1_CM7QUrWlva8tod6KRwsrY5h6b52A0tPKL6ZLmUHmVvFAf0B_S-kOeDR8_8Rna9hAoCfcY_RdsD8y1argoaJb2QPADjJiXJgqcbRR3eptWNHD1AmWKTGyQT08jhNkEZQ4TvhsUpMx-2HPwQztvaUAoAR4pDaaQ4Lbfs9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این سخن رهبر شهید انقلاب خطاب به همه جوانان کشور است ...
#بدرقه_یار
@TV_Fori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/667465" target="_blank">📅 16:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667464">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1450789d7.mp4?token=VbYLN8SVAkhrS3twOKa5yXu-C-HxpEN9aWxuXKsAmGtaX5gEhuLoX4KGqdEf9DNN6mXj9KIOvE0uuossjjklxcH3GdIkeh_CJ2Zda8M59WcRNpyq24gfRvnn_8Y03WGCOvtnBV3E5FOlLx4mxQF-h7ZnyTL2K6ITOgncVUAb8-1cnAgej2m1r_fevO2qUycx-YZNP7hk_w-m-ie21vv4GM0Zt-fkQ9wnq-SZhGVQBrERbVpysAr2B3nL62QmOwOWu849CCiMwjmWgJWsXXeUM7JtorSAC4Kvyx2EP1byBvu36ysjyBkfwprjEP8bdWeLzMIIu_4biM_YskaJIuIDfIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1450789d7.mp4?token=VbYLN8SVAkhrS3twOKa5yXu-C-HxpEN9aWxuXKsAmGtaX5gEhuLoX4KGqdEf9DNN6mXj9KIOvE0uuossjjklxcH3GdIkeh_CJ2Zda8M59WcRNpyq24gfRvnn_8Y03WGCOvtnBV3E5FOlLx4mxQF-h7ZnyTL2K6ITOgncVUAb8-1cnAgej2m1r_fevO2qUycx-YZNP7hk_w-m-ie21vv4GM0Zt-fkQ9wnq-SZhGVQBrERbVpysAr2B3nL62QmOwOWu849CCiMwjmWgJWsXXeUM7JtorSAC4Kvyx2EP1byBvu36ysjyBkfwprjEP8bdWeLzMIIu_4biM_YskaJIuIDfIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر صمت: ایستادگی صنعتگران در جنگ رمضان، نشانه وفاداری به نظام است
🔹
وزیر صنعت، معدن و تجارت در مراسم تشییع آقای شهید ایران در پاسخ به سوالی مبنی بر پیام ایشان برای صنعتگرانی که با وجود فشارهای ناشی از «جنگ رمضان» تولید را متوقف نکردند، گفت: «ایستادگی صنعتگران در شرایطی که کشور در وضعیت جنگی قرار دارد، صرفاً یک فعالیت اقتصادی نیست؛ بلکه نمادی از تعهد و وفاداری عمیق آنان به نظام جمهوری اسلامی ایران است.»
🔹
وزیر صمت همچنین با اشاره به نقش کلیدی صنعتگران در حفظ پایداری اقتصادی کشور در شرایط بحرانی، حمایت از تداوم فعالیت‌های تولیدی را از اولویت‌های اصلی این وزارتخانه دانست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/667464" target="_blank">📅 16:07 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667463">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3CvNSGDH8dCISXIWtV7Zin06r3CNPDR2M2X6Gv1oJfpMX8joycxc7u4XDgTrP89L6fM8I_urgM0_nHGiq_G-g4FipD9VFs2tteC_bxUqRSbhg-rsYxb2STlCyWN-DrjtKqAWHZrfb500P12CaxrxcYt1GRJcerMHh5gfMH1Sk69sXU4dlYJlKuxT8a19GdjYOg_iT1sXu2pawytVT5f_MWnSl4ihkk2hFdcXKln_Ia8JapNctEwvZ9ag9g5R5ZTQGofUBGgWu7WlJY0aO_jjQ1zj3zyRhYan4izze3DGlq0dG2MdLjwgUOW-YoCkCk_VlqOHj0GPi-Gx4euTBEYyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش محسن چاوشی به تشییع امام شهید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/667463" target="_blank">📅 16:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667462">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mckMqoMFl0SFNcELSer4KRwCn1KVC0WEq4Kpaaksw_G826f7_zPOAUcwI1UoDejsqTOkn7YNUf0klykLuGTXMQHJpKQWPGRrM9m7x7oWB3clngwba_MYpQW3X-uw2xNa88qe7rLbCYz7d0FUkdtnIPOU21de-F2unHbA2paaKN6wPryE1Trv1wEZiMmJywgtbWIxG9O0TGpucypqQU9KX0xAMCrmtB3ihKE-3q7cRHSXoJsvh2BABiBWmB1RLTHbyLRJZz1DTxQftXR4HzIGp2Px7LJ3NaXA4XBagJ856NcUx7Mn4RyZUOm885cYt4IjpK70M3TKuCZQAtfXZ92pKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
قابی از وداع؛ اشک و اندوه در مراسم تشییع رهبر انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/667462" target="_blank">📅 16:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667461">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFsFlUk02uXoVBYzPRkNagrwQtIp4tmlFiyhngOnkrrPHEXQOGCn_nZ53JKH6rL4D9D59wWoubHCuPUjNFGu9XOwJst6SVQ2ZJ_CvkN2qjTf4as2_YVetdhj5QSetkbn-QOmJrcmGajuXkHgGfd2s3CdCFRbILpqQz5f7xV5dM0EXEfI2ci2O4MH0w-LIuVSUoQExwWKfsln7Hpm93f8MZmd6oa1ltJ-BTdC8Liy5ygtO-uI2BV4wXnEO6q-XJe2Vi1NwYpJn9ksHwBnD0dqCAHDQuEFX-ebjbAYdESsAZ0nB7wFVPLUeUm4MIy2Y08tyikPmt18IjVvfKp-JFSDJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روایت آسوشیتدپرس از مردم حاضر در تشییع: خواهان کشتن ترامپ
🔹
خبرگزاری آمریکایی آسوشیتدپرس در خصوص حضور میلیونی در مراسم تشییع رهبر شهید انقلاب نوشت: عزاداران سیاه‌پوش به سمت پایتخت ایران سرازیر شدند و جمعیت زیادی خواستار مرگ دونالد ترامپ، رئیس‌جمهور آمریکا بودند.
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/667461" target="_blank">📅 15:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667460">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc380907b.mp4?token=hSqTDiBppef9fDfZoV5n1ny771x9UfRIAxSW6XwhEPAoMZeH4d9BievIS2BcCuifUumHeRCEHKNDdlUs1vjsJR5kMU23A8JVjpuF9zUSyXhQYAECnbf8IEJtbl83-MwDjd8e_uERbD_IJv65ycXHKi0VsV_oTUIQ4LdSPVSPhXJIOAOhsJ5vh50qCF67ZU3XlpfNMXooSnT69zMoJivdWLPEs1qlvvpZk2wtgfPipmoNQXzQq3Z-R2c8c01XkGagMeVbyweCK7lhxm-Sx5rZHdOo4sFcyzy7bt8DK_-hvk0PN8FRl2x4bnq0HMMmet3WZ6h-k5TPdGPbVvOxDAxB8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc380907b.mp4?token=hSqTDiBppef9fDfZoV5n1ny771x9UfRIAxSW6XwhEPAoMZeH4d9BievIS2BcCuifUumHeRCEHKNDdlUs1vjsJR5kMU23A8JVjpuF9zUSyXhQYAECnbf8IEJtbl83-MwDjd8e_uERbD_IJv65ycXHKi0VsV_oTUIQ4LdSPVSPhXJIOAOhsJ5vh50qCF67ZU3XlpfNMXooSnT69zMoJivdWLPEs1qlvvpZk2wtgfPipmoNQXzQq3Z-R2c8c01XkGagMeVbyweCK7lhxm-Sx5rZHdOo4sFcyzy7bt8DK_-hvk0PN8FRl2x4bnq0HMMmet3WZ6h-k5TPdGPbVvOxDAxB8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیکر شهدا به مهرآباد رسید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/667460" target="_blank">📅 15:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667459">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58bf7348a8.mp4?token=BjRJlipiUXb8ELBfWGracLaEnCHWVXysQlXuETF1SOEtHMrTDdgrcUy_VZof_JoHAkWU2HUfXqz5Kd0MibgfUXSzdf0_LAjyGBtX0HnTKy3DaCQ2spwVlwu9nWVx1AoIH97i87n_AHO69m3jA1WkjJINJXf0QMoMWVl_DFY_Obb2yy-FFczeenZTurpPJLj7-Jl3nGBgcIePXqJ0ILIKd1Y--WVnJshqSICLoNRo-YfDCdu4A5KlmqX2vEX91PE967wpHDTNyLk8tl87zao63xc6e5Fne7vB6E4eY_v0ASgrb8sr7nx-t1RvkDVKX-Vxcit1PDfhHN0sRmC7MVv-mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58bf7348a8.mp4?token=BjRJlipiUXb8ELBfWGracLaEnCHWVXysQlXuETF1SOEtHMrTDdgrcUy_VZof_JoHAkWU2HUfXqz5Kd0MibgfUXSzdf0_LAjyGBtX0HnTKy3DaCQ2spwVlwu9nWVx1AoIH97i87n_AHO69m3jA1WkjJINJXf0QMoMWVl_DFY_Obb2yy-FFczeenZTurpPJLj7-Jl3nGBgcIePXqJ0ILIKd1Y--WVnJshqSICLoNRo-YfDCdu4A5KlmqX2vEX91PE967wpHDTNyLk8tl87zao63xc6e5Fne7vB6E4eY_v0ASgrb8sr7nx-t1RvkDVKX-Vxcit1PDfhHN0sRmC7MVv-mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرباز وظیفه خطاب به رهبر شهید: آقا راهت ادامه دارد با خیال راحت برو
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Lin</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/667459" target="_blank">📅 15:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667458">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AD0Ypr6kHDQv60QT4Z5vgfqVntQNNZ-5PQ2Xo7kyknLUGGeQLxgtao5Tu6kzvkz1BcTLqgX7T8-_SM7-_PpG42QwMAWlkrjZeVe8TibdQfFCxMMQh4HFN_fAl4sBPkZ0N7iWcMRe98np7ho26CskrHakUL7Lc4naai_9B9k0g8Tu886v2XvDZGFT3DtFD1-Ps7w1gdQbJ4we80On30eI4mO7gLDKnQXHCOEn5myFrEX1p4vm807pOEKBC3rffaZTbmKIM9IRKkcYUHQFpoOPG61LCq7-3iTybDmaSR6knbZKHcqMxyh0D-NeawEdH6bSu-8ZVgmDXFrND8QCOHSNWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عبدالرضا داوری حضور مردم در مصلی تهران را ۲۴ میلیون نفر برآورد کرد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/667458" target="_blank">📅 15:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667457">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
جوکار، رییس کمیسیون امور داخلی کشور و شوراهای مجلس در مراسم وداع با رهبر شهید: دو ماه بعد از اعلام قطعی جنگ توسط شعام، انتخابات شوراها را همین امسال خواهیم داشت.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/667457" target="_blank">📅 15:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667455">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
سیا: هوش مصنوعی «سلاح هسته‌ای دیجیتال» شده است
لوفیگارو:
🔹
رئیس سازمان سیا در اظهاراتی کم‌سابقه، پیشرفته‌ترین مدل‌های هوش مصنوعی را  «سلاح‌های هسته‌ای دیجیتال» معرفی کرد.
🔹
رقابت اصلی امنیتی میان آمریکا، چین و روسیه اکنون بر سر هوش مصنوعی است.
🔹
همزمان با تشدید کنترل‌های واشنگتن بر مدل‌های پیشرفته هوش مصنوعی، دولت آمریکا دسترسی به برخی از قدرتمندترین مدل‌ها را محدود کرده است.
🔹
به گفته رئیس سیا، حفاظت از برتری آمریکا در حوزه هوش مصنوعی اکنون در اولویت نخست امنیت ملی این کشور قرار دارد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/667455" target="_blank">📅 15:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667454">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDaWkNhiuL_YPPZy2xPP_ROqvmvVhRpUz0eTeJRCQhzTp6bkE6WOppjgPBDy-VY7PCADxi17NYhd_2hcPgh_FM7K1Pp9IsBkjWK2aV5fWRsQyN58WiwsHRcvJdiprfu7RiA8sFcOnCq-X0JM72GsROltUdGDtMeQIo3Z6_fJP6ySGBoycq3y5v5dD1HYhyKQZBFJdMDkMPiJGsgmvMLbrKSUGdzqFJO4f88vl1wB0ZoqaWBv0jZ7qomxpSR56OFaCwynirUU3KxKbGHnNgFTGEMZm03FRIlVo7lK9uMr8sLSmVAM3KgZ5_n2xV2Fg_0dM-eY_1oqNmjkGvKARX330g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازدید وزیر ارتباطات و فناوری اطلاعات از موکب خدمات رسانه‌ای همراه اول
🔹
سید ستار هاشمی، وزیر ارتباطات و فناوری اطلاعات با حضور در موکب رسانه‌ای بزرگترین اپراتور تلفن همراه کشور، از نزدیک در جریان فعالیت‌ها و خدمات ارائه شده در این مرکز پنج طبقه قرار گرفت.
🔹
وی پس از بازدید از بخش پایش و تحلیل داده این موکب، با تقدیر از حضور پررنگ مردم در فضای مجازی و شبکه‌های اجتماعی طی ایام برگزاری مراسم بدرقه رهبر شهید، این حضور را باعث خنثی شدن جنگ رسانه‌ای دشمنان و کاهش فاصله میان فضای مجازی با واقعیت جامعه ایرانی عنوان کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/667454" target="_blank">📅 15:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667453">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
استانداری اصفهان:
فردا سه‌شنبه شهرستان‌های کاشان و آران و بیدگل تعطیل خواهند بود
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/667453" target="_blank">📅 15:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667446">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SscTzt6-1-21xwd_Dy1SDEpk5gqROgFPqH5czdjgcKl1nD2_7T0hN5DeAY5ZvHLF523r3-OoGEJLaKlb39zX7s8cGtnmxEiAnpl8UESrBcTbKCrYuRELWALAgZKyQBZzfALq5voONX0yAT57UW0tCNBxNsCliNerVc9ezRZDV-8BXqt2tJp0j9s05wn4eLH4s6LNRzDVi0DLulPYese3Ox-xcWNEYH7fHIXKMXPK5Y-DCQTV31oSGSDaD5_4MDsFztA0FlV3pcJFAJ5ObEgryafQo_bqFIohDlDwhpwg4m_hfyVGNqCGQUeVNV-ph8jFwYWZ4RRYEHASOrMN5phAWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CveorGCcrkn4aIwnic-Kjt2fdqri3JlPZVKLv8-aHzOTxmgRGcdT0ez3ftSS9VgjHkfXIAkhtAAY6qx1DDm3uo90cDydqzghKRkFG5vOusOYoV2Z77eVON_GQpB7AHZ-5pVJTLbntUfVzKa0vzuGrhu9GXfychHl5NELSM8uYP0g2u-TnQ2RfV1wvVvXYJMZ5EDD5MYuHW3bcPzAQXnucbZ2e3lMpBbPt8mvSaoAmQrye08s5G9G6hG9l3iFY38CEQXtBmCUt7QtFzCj7DmUW5hb8dtlNOA1nXsChHlv_vz1YSRCnnd-2UN1kKjbXokK0QFCTCLsWWtWwzIoAbErww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bxvNpeAvHybZjY7ioBC8oSBdWmbFY4y0OinQhLJb9NN9gq_prI3xSM24enElzObJHjQCfS2gz3KQdPY--k6ELkgprY8hDVSBEMpBbt3LhSlJVO3mAC49P12USwGeywjlmK7nQZam0xSMwVPmrkYEx8J1CpTZ2d2zboLNRAHM0n2eYtCodp4PKWhqzl_mV-HF0RXOT608luivRMadV1xLv31YrVrVTey7xaDi1yvSm__J89yXRDhr0r2koVNm1bRQYy6-lay7B2AYQBG2hMuyBBkKdJ4SVR68WkaKm9D5vgTsADj2cf7TcL4L9oIxeQaQuLQ4AooQM3MAzgYNETajHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MdeY1dGhFQ__PthQnP1vYnokfNPgcCUGKO6d22TmncGgwb06ieJeAq_mBkwPPKhukubL7efscO_1rtkLCU34VcWpTM1-Fcz5NQxYNQw1PIWzMGI-FTGuFHY6oIFgbJ8gAl6ln9X5wbhDKQzbf2IsB_twPobn0-DwSZesovuxVEihV1M-oVbtMpgu35NfBLcBMSLHgEVRmdF9gg1n1kPV44AddA3uBrXoVrpbAzk5mLR6B9h7GisDHzC31IRi5jFDK-RNR3hFMsBiPzQCuWsjRVJVDAboRwWqbOwfZueFAGPtfurMXKl5kUt9esanX7mHPgkmu_xMCNdu0YjondX0hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EzFXgl_ycdDUwlpeLQoqMDNBGvYKb4qqjrbnaliJNoaqN6_2B1tOYynooOX52_5AtUlBGfhcRNS8QNNGrhxexBHMj6MIX-X0Qtu3DNAZoCyIRxIGHNl1iZlrAzY-5u_uIw194nX4902WiZ8MEf4e3MYFMJKANzYksZD9yeVLjITvtqq0T0iXYfNF7pq79OmIoYjzqQLxdKEzz7FSamH6bz9YBtKBBERTOflE50HqIytiAG5nu9nI3eZeYFz1g6RpX_5BYIeZNvM5QffL2tXSneP5gU1TYoNU6TPeK4ya-GXy3kdMx2dB9oJOR-0tiGXwXzbn7fJUhT8aj6dM0Gkngg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T3aykSQmM9R4JBipkGzTIR8XYqQE1MtXLxFd442qqqKQb_3VSHlF1FHm0GBJMI7MlUs161M6IHP0dD1eDLrqOAAwCWgDt92AZ1wx0x9nh-lRbvq3GIEKyHwvTVlI65rdYJlkO_1cChv0CtRI-fBV6_CjbEjVG5PcEg7jXuoukRGfrxsvPaSQwczY0U-zyuOObDDCXgoC4_FWW1PdR1FRTmIqBQcaoxG3vQV8QbIMpRB_9Y7wFVdvjcUHclviJQXBLwIJ81li9ejPUdf-mppQYS6_7rwTAirl2UmAUn312PJWmttAmJfYdST6Cs8qzHGY9bcwPCpxc9kU-e3jX75PEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i1FaSEhmNzXHRIQCGd8OqyWqwDVM0VMM1PL_Go9fuoIU15XRo2j0YFRkgwIZr_CSqXkjv8GNWQh10T1jm1_vF4pU4tIS2GzsnpaHNlHw5MsigTFKq-JrYCc4Bdic-ydxewkwzU0ypDWQ5gxS77Y_QbwlUXhBlnMjQs9Z2UjsHaZVN6Fvb-ngdK6jYuxA0V1Qrnj4k0vQudfSuYd49u8EPQkYsxFSC47TVgQA75wByOeZqBM7x3FsXKggtT1Fl2kogzbikRlz48OHg1tdZJNlUD0DI3vWOv4nLGd5wFgkczRRgUwpxbsIRxpX7h2Fv154j7YOIo7VPGJOKll0eR0FJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ایران کوچک، میزبان زائران آقای شهید ایران
🔹
امیر اشتری، رئیس سازمان فرهنگی، اجتماعی و ورزشی شهرداری کرج در
#گفت‌وگو
با خبرفوری گفت: موکب این سازمان در ابتدای آزادراه همت با افتخار میزبان زائران رهبر و آقای شهید ایران بود.
🔹
خدمات فرهنگی، اسکان، استراحت، پذیرایی و... در این موکب ارائه شد.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/667446" target="_blank">📅 15:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667445">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f6aa542cc.mp4?token=S1iQRdownBcuycwpW0bjAZ82oBT5mnYuwqPAqJBdi0aH7VewY8q749XxIFqnNJdZJOJEgYDKa7uSL3CJmL7yDDu_AaLG4FWWyeVLHcAropD7JFkZCBAm7uxKgNoWwPuwmdQ4QIZjbS_7K1ydu6kcO9qBBvzO-nDryCxgd7qxotQU1NjWNMOnTfIxJIt3fztitwJs5VVEnROrSb-DYzWL7qzz6WfBx1kSLs05uW1JFuUKWOtI6ubCadjuq8xax-lhmNW1wyffeUpBgjm67rjfKQgQN1UTSgNlsfNsTsIcmiYjACG9SkIlyMRyxiEj3GRsobWSwHbjWYB4hx3NUsYXaDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f6aa542cc.mp4?token=S1iQRdownBcuycwpW0bjAZ82oBT5mnYuwqPAqJBdi0aH7VewY8q749XxIFqnNJdZJOJEgYDKa7uSL3CJmL7yDDu_AaLG4FWWyeVLHcAropD7JFkZCBAm7uxKgNoWwPuwmdQ4QIZjbS_7K1ydu6kcO9qBBvzO-nDryCxgd7qxotQU1NjWNMOnTfIxJIt3fztitwJs5VVEnROrSb-DYzWL7qzz6WfBx1kSLs05uW1JFuUKWOtI6ubCadjuq8xax-lhmNW1wyffeUpBgjm67rjfKQgQN1UTSgNlsfNsTsIcmiYjACG9SkIlyMRyxiEj3GRsobWSwHbjWYB4hx3NUsYXaDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعار لبیک سید مجتبی در تشییع رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/667445" target="_blank">📅 15:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667444">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
حرم مطهر طبق تمام سنوات خدمات خود را به زائران ادامه می دهد
مهدی شاد، سخنگوی ستاد تشییع رهبرشهید در ستاد رسانه‌ای هلدینگ خبرفوری:
🔹
۴ مسیر اصلی منتهی به حرم میزبان حضور زائران خواهد بود و به طور مستمر تصمیمات به اقتضای شرایط اتخاذ می‌شود.
🔹
تشییع پیکر شهدا به سمت حرم انجام می‌شود و نماز نیز اقامه می شود و بلافاصله تدفین صورت می‌گیرد. در مشهد وداع عمومی نخواهیم داشت.
🔹
حرم مطهر طبق تمام سنوات خدمات خود را به زائران ادامه می‌دهد و همه صحن‌ها در خدمت ارائه خواهد بود.
🔹
از صبح چهارشنبه محدودیت‌هایی در بافت مرکزی حرم مطهر محدودیت‌هایی اعمال می‌شود که بلافاصله بعد از مراسم تدفین به چرخه حضور زائران باز می‌گردد.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/667444" target="_blank">📅 15:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667443">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
موسی احمدی، رییس کمیسیون انرژی مجلس در مراسم وداع با رهبر شهید: در تابستان قطعا قطعی برق نخواهیم داشت و در زمستان هم احتمالا قطعی گاز و برق نداریم!
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/667443" target="_blank">📅 15:06 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667442">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b5e671d06.mp4?token=tP9-4gm8Zn2hW2AA_B7D2Bqg0Nxhcs-dVaSrbUeG-OFKcVdPMdsE1GVu_sxpsgrZ0SF732NaFzvH_7w2vX88COOQhPVY5KONVLgUJdp0picOuByS_pznfAyuTtt3jRzeLYsz4FNR1SBYDMOaWApu8rgyM_hFSU0f4EWrGjvRoo95pOoHEXRAI7aZ5petLnVdDIga7-XIPLW1ZXeSnL772nEbvxzBI-guoBoeEe2pwP27OE78J9d0mgeGHmY7nmEBDGryVMhG8NQR0HVXJtS7621haOViJjDs0Pn3UB5fYjvr1LmoVk4-MuprWa4nMABy3d7yGJCo1fnToTU-Y14HCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b5e671d06.mp4?token=tP9-4gm8Zn2hW2AA_B7D2Bqg0Nxhcs-dVaSrbUeG-OFKcVdPMdsE1GVu_sxpsgrZ0SF732NaFzvH_7w2vX88COOQhPVY5KONVLgUJdp0picOuByS_pznfAyuTtt3jRzeLYsz4FNR1SBYDMOaWApu8rgyM_hFSU0f4EWrGjvRoo95pOoHEXRAI7aZ5petLnVdDIga7-XIPLW1ZXeSnL772nEbvxzBI-guoBoeEe2pwP27OE78J9d0mgeGHmY7nmEBDGryVMhG8NQR0HVXJtS7621haOViJjDs0Pn3UB5fYjvr1LmoVk4-MuprWa4nMABy3d7yGJCo1fnToTU-Y14HCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عمری مجاهدت تا شهادت
🔹
ذره ذره این خاک و پرچم ایران زمین، مدیون تو است ای پسر فاطمه، اصیل‌ترین ابرمرد آریایی...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/667442" target="_blank">📅 15:06 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667441">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">رهبر شهید (گروه موسیقی بین المللی ماه )@</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/akhbarefori/667441" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">موسیقی اختصاصی وداع با رهبر شهید انقلاب
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/667441" target="_blank">📅 15:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667440">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
واشنگتن‌پست: ایران جسورتر شده است
ادعای واشنگتن‌پست:
🔹
ایران از جنگ جان سالم به در برد و اکنون زیرک‌تر، بی‌رحم‌تر و تندروتر شده است.
🔹
پس از ماه‌ها حمله توسط آمریکا و اسرائیل، رژیم ایران جسورتر از قبل ظاهر شده است و این موضوع با ادعای ترامپ مبنی بر انجام «تغییر حکومت» در تناقض است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/667440" target="_blank">📅 15:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667438">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTHhZKKpBVguahHS5l1lWW22eO1m5hn-RByRox6hQ5aTj04pA8iv7BQ6ekxCO03DJTRXknaSIrv8bLMuNe7KfGyxO6HJXBlUDugt1FnX8hrbZWNob3ECbNT2BJQrqNQ0_P0avUMNzz9ATlqV5SvgFZBAKbxOT8DuRYQ0prx4XLEJMzGmnXdJ4rm5VgEyDGPIRaLCLspk6s_CAETm5aqYlevJ8vuSUwoMwk-iy_Fh5U2yzk_enPzXfYtQseGxqvRLhMsjUQeoW5BDGPAagyC5W78mi6tYf1qJnI1yOqmBQqKbrSy0SElr-gHj9MQRerx3-ZREX-0mq_O1mT-qSR6Vsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محمدباقر ذوالقدر؛ دبیر شورای عالی امنیت ملی در مراسم تشییع آقای شهید:
🔹
ناظران باهوش امروز متوجه شدند که یک معادله جدید در تهران شکل گرفت؛
حضور میلیونها نفر از مردم با پرچم‌های سرخ و شعارهای خون‌خواهی در تشییع رهبر شهید، پیام صریح ملت ایران به دشمنان این سرزمین است.
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/667438" target="_blank">📅 14:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667437">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d12c6b29e1.mp4?token=J_38ctK--OTev9ukq5nCY9IzqN0rct-baZXsFptEiN9yceU2R--rzsd3Iwrx05H1dZDWlNZvLRp2uS4D-5f_4Dm4nYvURPO_p6UtqsnZ_az1EQF8hOGpuUlvUUeXpd1_rt7c_Q7M1HVgPonqRvXbXXPdAwFGe9giqEOTgKDvWefLo6OeEb_9S19lfpXsKnKuT7UD0yWanumZBP7n8yKqHeSMnfeW01JQwicHR8AEGXCLVnn86mg21ngoaUNs38duWnC16YNYLehVjKMAG99G6q5wKBA2J0rzyx9S8iu9o0qzkHAxiu3juI30MxuL8OJ6_aaQnLiq7y8I804jW3v8DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d12c6b29e1.mp4?token=J_38ctK--OTev9ukq5nCY9IzqN0rct-baZXsFptEiN9yceU2R--rzsd3Iwrx05H1dZDWlNZvLRp2uS4D-5f_4Dm4nYvURPO_p6UtqsnZ_az1EQF8hOGpuUlvUUeXpd1_rt7c_Q7M1HVgPonqRvXbXXPdAwFGe9giqEOTgKDvWefLo6OeEb_9S19lfpXsKnKuT7UD0yWanumZBP7n8yKqHeSMnfeW01JQwicHR8AEGXCLVnn86mg21ngoaUNs38duWnC16YNYLehVjKMAG99G6q5wKBA2J0rzyx9S8iu9o0qzkHAxiu3juI30MxuL8OJ6_aaQnLiq7y8I804jW3v8DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آملی‌لاریجانی:
حضور مردم دفاع از راهبرد عظیم امام شهید برای ایستادگی در برابر استکبار است
.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/667437" target="_blank">📅 14:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667436">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
ادارات هرمزگان سه‌شنبه تعطیل شد
استانداری هرمزگان:
🔹
تمامی دستگاه‌های اجرایی، بانک‌ها و مراکز آموزشی استان هرمزگان در روز سه‌شنبه تعطیل است.
#بدرقه_یار
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/667436" target="_blank">📅 14:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667435">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
روزنامهٔ «پاکستان آبزرور» از احتمال برگزاری دور سوم مذاکرات ایران و آمریکا در اسلام‌آباد در روزهای ۱۴ و ۱۵ ژوئیه (۲۴ و ۲۵ تیر) خبر داده است
.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/667435" target="_blank">📅 14:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667434">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a3a2bf9f.mp4?token=WZm0JRuOGTmvKHmnSG8DEHYL1Zsbe1tgDYx-c--sQ-cbUvSOXh8m3IrZipVwYcqX5IHHnqxW_6j7n_N5ECRVg9Hmm-7X7_vpZU23OYJwgsidQFmELRUSrEFTREasMkjqO4WIkpZbnTIHg6jy7_6U588IKJfxPA4Y9fH7hbNsaCrMj6zrDrk96G403QfH1JncMn7ixhEIOtz9KU2UFWowsDbpdM6MNqE35YkJQ3_O0HDnLlHnhLzjqhVXsa1KN_D6cA9nQjjoq4_T-IE8jWCx34PN6y9yP-5wJKC00XQsAU5HO_4l40nyw5Io_3safio9piHo3ZnZucXX_WKMT1ds5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a3a2bf9f.mp4?token=WZm0JRuOGTmvKHmnSG8DEHYL1Zsbe1tgDYx-c--sQ-cbUvSOXh8m3IrZipVwYcqX5IHHnqxW_6j7n_N5ECRVg9Hmm-7X7_vpZU23OYJwgsidQFmELRUSrEFTREasMkjqO4WIkpZbnTIHg6jy7_6U588IKJfxPA4Y9fH7hbNsaCrMj6zrDrk96G403QfH1JncMn7ixhEIOtz9KU2UFWowsDbpdM6MNqE35YkJQ3_O0HDnLlHnhLzjqhVXsa1KN_D6cA9nQjjoq4_T-IE8jWCx34PN6y9yP-5wJKC00XQsAU5HO_4l40nyw5Io_3safio9piHo3ZnZucXX_WKMT1ds5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیژن عبدالکریمی، استاد دانشگاه در مراسم تشییع رهبر شهید: حضور آگاهانه و وفادارانه مردم در واقع یک رفراندوم عظیم بود
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/667434" target="_blank">📅 14:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667433">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
انبارلویی: جنگ هنوز تمام نشده و انتقام خون امام شهیدمان را خواهیم گرفت
محمدکاظم انبارلویی، کارشناس سیاسی:
🔹
ما دارای نظامی هستیم که تکانه‌های نظامی و جنگ نرم، نتوانسته است این نظام را از بین ببرد و صاحب‌نظران سیاسی و نظامی دنیا علت استقرار و قدرت‌نمایی ایران را در این می‌دانند که یک نظام پرقدرت حاکم است.
🔹
در مرحله‌ای از جنگ قرار داریم که هر لحظه ممکن است شعله‌های جنگ شعله‌ورتر شود و جنگ هنوز تمام نشده و در ادامه این جنگ نابرابر، انتقام خون امام شهید را خواهیم گرفت.
🔹
نتانیاهو و ترامپ اصلا عددی نیستند و تمام هیکل آن‌ها به اندازه بند کفش حاج قاسم نمی‌ارزد.
#WillPayThePrice
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/667433" target="_blank">📅 14:27 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667432">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sf9-Z4Yeudfvqq73WlKvHtDEEgv44ckTFPrKtzfglZ-K6CuvWVx9uoA_V_3tOzYC0d9FXCOoOcbcN1dRhIKvALx4PZdh5r5pV42dzKoT54ATOtaJFTbWC8MP6ince5ktBJYAydWQO4y9jB1w1phgm_RfINvFoSWqfbADpWCqzuGZ7WmNkC7nXS2ZLwIWVJs57CqMy-8I2oclRY31mVziqOyJCCBGXkiloPWwNQIFoLqCUro9KjtipWlBBAaiZZHx4vHK3uFsxt4PMxp6Q3vfekimiFde_PexPvgzmocHKWj7LdDyNijrEklI56tzyYtnviA3_IxQkYDmJ6Tjbtx3gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
حضور عراقچی، جلیلی، وزیر کار و رئیس سازمان انرژی اتمی در مراسم تشییع رهبر شهید #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/667432" target="_blank">📅 14:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667431">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTTA1RO-YVdNN0uCLX33641ay4BnXCfFfo_fNe71qhIfNSN0bLoNsERojfE0HrcIfw2ybuu6NEw8ZlauMhUhhJ1nFedUQIgvsjdfg7rE5Spdes5012EWKra_HS71frbZj9B4FA0z-1Y-M7j7vqrMVSlf5sXvW-wZfpRU5tMDCosXiwJvdO7d_WY0k3dSGf6iStU3OBGdlxV0ohLrX6v7mU63BJzf0e1SIs-5-fnMsn8NAdNgfTY1gv45gfaDpV2SF81FGguva3OcudwMNpYJdhemr-__8ppVoRMtXPDQLzMxH5eLAixu-CI6asAIP1N7qJQg8yqY5A5K9zoqj0eRfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هیچ تجاوز و فشاری نمی‌تواند ملت ایران را وادار به تسلیم کند
محمدجواد ظریف:
🔹
بزرگ‌ترین سرمایۀ راهبردی ایران، فراتر از جغرافیا و نیروهای مسلح دلیرش، مردم سلحشور آن‌اند.
🔹
میلیون‌ها نفر برای بدرقۀ رهبر عزیزمان آمدند؛ رهبری که همراه خانواده و ۱۶۸ دانش‌آموز در میناب، به‌دست بدترین جنایتکاران، بزدلانه ترور شد.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/667431" target="_blank">📅 14:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667426">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B9mV_MR_F1CK43T5i8eLFw31A2CkFWemQ7DRSEusR02sm2uD_6-lj1hKni5RvknA__kCfHuPGwiMw9j65xfPDG-mn6j5Cfh0LJ6wndO20O6JdXsgfx5BraES7WXUaG6M1uYi3icy0RiOrVMaXNOkOl-9mi-KyjeoPTJz9WQXghS9TxPbS8IFpq7iVSz2HyHCEhXWI0xMWnGCRezYPaYAUDIF23Cz1FC-gXmlNv4-zrsmFFQJBtSuh6zSYVlUULiEsm6hrbT8l_Q7mS8l5LDEzEgivFGPZQY26K9gs0K8FFvpKCNnKQSh9yKHOxGQ23UYETu42v33SNuOh28oqcBI7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/otu4lZDE6iDl5wHruQod2-8cCVv7f4ExkOyY2DbqmKHMp7A7Rujq_JxymZMbL8RS-3Leqz2L2HG-50c4lm2Exn47Z1xl1OySnVZx8qOja7-1v7YHdq2ZD1_0vZdeiU8NIvGk6t8jS5cj3YPzHqQHDpBQUzP2PpmK84BI8Ob0-XM5QTyyWD1mlW1ENpjXyAm-h9T4iYTWPqv3hgROjLzMpSlL4_YXtjp7e_nDFYin5f7UJe7nBsZ88QYqhu9UX3Z0gUaYpTNAodR9SS7iIxi3KREnz2rkeZpjI8dKlcyGKJvlY2cdIpXsOt-9uuh8MVVMz0IEN0-VRK1lBGCyAwj6AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kr4sHDaHzVlvpxO1xM3INn7IX9MLcJXP4kcQM1nZr1brbOofFEaEAY27rgElyso-LdqigXDLBVpBElQq218Why38RjPR2XFKVlU3DVTmaGJFEhxbOyslzaT9rQTBXjSYx17w7FIjPdmJcts4bYrdJ1vrFW59ziFiv-zONEukvi2fW7L5lL1aXX9j_Ac2obP9LunI7d_CypdLWO0RKfz21-Hi6YB528QEZwoLOCmJwYjuD1s3nU_PoIlh-Q9jJ5EVtgDFo5Cq2cxngUZZfgBSO5DA38t-wndVH5648_Mfi4ilxHm8ponFfmk0S7QW1SWQpmipXgIPf9G3ML4E0aCPjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FeXWnWTFX7SipjiwEKyNJOs5bCYJdQVsZGsQZieZb4XHIXjXULMCrCpjxS36QXm5jJWLUenCx70LriARJIG9UFnTuJTcwGn6AGv5FfnYpqBin-7Rp-6IIPQ-beMabL0tEcVMC9My665pTgWOqV4PMtLNG-NeiXmih5fQfTd9vkGqlNHa5jvP1VZwxj0p8fvOKYmSjwtY0hhBUVJ8tyQQ7dKvwQGJwGpt1BY1XQXKMM91T8MCMzwLUH8yukCxdsF6YWtnB0Pw1bfJCrRuvM_koCqF1MkzGZkNByAszkWCciq8Q-PUbPFftYYWkn30eAcMqxXaNd4kbjykNgNqPOjIjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZWhxtbRGpDgfqQR-bHCrrPJsQ_Zqtnh22pwcWjaVGGlhq1cRFhWHECJj4YM7GHQ26MRHNLHcYf7JYCgVclXrObX7znp0ctxU5XnQ6NHj3xeRh674efIWU847KklUYC2n_JXlTnwcbXG3-ugFAMKjPizvTIC6KCSTQGSfuVSdfOq4ty5aRQTqo_A4WC3UyCTJUZJEBjxv0M2wvsU7v_cIqxY0C5PAFuW4HjYj5O_2m8q3WErP2YB4tnkNY_2hqUV6qUWcnuuIfQdcwVq-slDL8onP-7KR2jZDGXF9DmkWRcfyAuDjj25XTB6prSuvCUO1eLoS69Iov5gbKpj69yFJ3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چند خاطره به‌یادماندنی از رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/667426" target="_blank">📅 14:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667425">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b516a0f9c.mp4?token=CMpNWn67OHQBa_v5hKnn77v1mq8rbadabhXKcgQj2yT6SCZZVCv5JKW2dU3wAZT6F-dsXbKhR3FOZn0GoxSiFs0vQJYE1ng0kLGdgOEbXo8apMFGuPgRxm-YnemekCX-3Ev6FiatdJYk-WBvt7dLg3TveWH3cad6TXoTpvJ-MhqdyBMeHU_bXMtZ5hp1uUkEVMU3swmJqMkvr5_DXNXPcCCVFkLn02-73U2bKqyhJsZKlt6JOvcl_HO3J6OH1MVqIbev0IaI9VfalPM9SIJrbUNMLf2n1BubLkKNNg7o5j_vjbRaWdhAWR98fvaOFqnqe2dLx_B_zLf3bZ4eOr1eRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b516a0f9c.mp4?token=CMpNWn67OHQBa_v5hKnn77v1mq8rbadabhXKcgQj2yT6SCZZVCv5JKW2dU3wAZT6F-dsXbKhR3FOZn0GoxSiFs0vQJYE1ng0kLGdgOEbXo8apMFGuPgRxm-YnemekCX-3Ev6FiatdJYk-WBvt7dLg3TveWH3cad6TXoTpvJ-MhqdyBMeHU_bXMtZ5hp1uUkEVMU3swmJqMkvr5_DXNXPcCCVFkLn02-73U2bKqyhJsZKlt6JOvcl_HO3J6OH1MVqIbev0IaI9VfalPM9SIJrbUNMLf2n1BubLkKNNg7o5j_vjbRaWdhAWR98fvaOFqnqe2dLx_B_zLf3bZ4eOr1eRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زائر کاشانی مراسم وداع و تشییع رهبر شهید: دوست دارم به همراه خانواده‌ام شهید شویم
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/667425" target="_blank">📅 14:07 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667424">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
حماس کمیته اداره امور دولتی غزه را منحل کرد
🔹
دفتر اطلاع‌رسانی دولت حماس در نوار غزه امروز از انحلال کمیته اداره غزه خبر داد تا اداره امور را به یک کمیته تکنوکرات منتقل کند.
🔹
دولت حماس با اشاره به اینکه اقدام مذکور در راستای بهبود وضعیت داخلی و در راستای منافع عالی فلسطین است، تصریح کرد، هدف از این کار، کاهش مشکلات ساکنان غزه و گرفتن بهانه از دست رژیم صهیونیستی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/667424" target="_blank">📅 14:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667423">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f86ba91fc.mp4?token=nbuAZU9om0nUvEAD3-tetwxKIwKl6Nb6jPiUJCK9FcwuhA9QG5SAUjeftmdUXPBgMFRA6JO0bihso7qB_-fu8cLHpA-R-exS7tZrpakyJp7H4qudEBeu6xfA_b1bmsVTKrPJy-YRzoHqqqVIj5Y4ul8fN7JjetIWu8ZlrIHGO_4AbxHK-MOkYu8qgIGxeQr1JzPjrLiLpqEXsp9TRM7Spm8aJhtqAgeLWXxwwPuGAsNyXCUyiATV2S-HObqqL0MT_Tu_rB8a6XZUsQSVb30T1K_NGapzKtwGwrMadsCSDyUMKUw2NUvF-5NFcxvvm0j0z4spi3Q_ANcmulUjiR149jWopJKKSK4QciM266LJTZK5XSz8PyVnPfDsKq9xgbMOXg3HudUnpcJb4gwddgdmoi470eZNRg2ugSQDg3AbTuG1CGYiTYGdJZDroZ4_RN6Asv60OAEJAaQ4qx3huBOM6-Mw3ZTda-cELAs8PiYo7tKJYXApoBTHr8y9oqlTsEu_4nsSQT-lURzucGbpB6IO5C8gVJSwv1CyMMyta2iH-_YzmcpVxLsUG18bTDnanLjmkus0D_sjPE8TIqjK_f5W-ePoGYf6c1M0fSo312N6D7WAFhav3mJAr8TUCxyXALQVXPf9UV_mEFYOIh0ch5l3GmX_x65KmqPiH75N9xp-sYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f86ba91fc.mp4?token=nbuAZU9om0nUvEAD3-tetwxKIwKl6Nb6jPiUJCK9FcwuhA9QG5SAUjeftmdUXPBgMFRA6JO0bihso7qB_-fu8cLHpA-R-exS7tZrpakyJp7H4qudEBeu6xfA_b1bmsVTKrPJy-YRzoHqqqVIj5Y4ul8fN7JjetIWu8ZlrIHGO_4AbxHK-MOkYu8qgIGxeQr1JzPjrLiLpqEXsp9TRM7Spm8aJhtqAgeLWXxwwPuGAsNyXCUyiATV2S-HObqqL0MT_Tu_rB8a6XZUsQSVb30T1K_NGapzKtwGwrMadsCSDyUMKUw2NUvF-5NFcxvvm0j0z4spi3Q_ANcmulUjiR149jWopJKKSK4QciM266LJTZK5XSz8PyVnPfDsKq9xgbMOXg3HudUnpcJb4gwddgdmoi470eZNRg2ugSQDg3AbTuG1CGYiTYGdJZDroZ4_RN6Asv60OAEJAaQ4qx3huBOM6-Mw3ZTda-cELAs8PiYo7tKJYXApoBTHr8y9oqlTsEu_4nsSQT-lURzucGbpB6IO5C8gVJSwv1CyMMyta2iH-_YzmcpVxLsUG18bTDnanLjmkus0D_sjPE8TIqjK_f5W-ePoGYf6c1M0fSo312N6D7WAFhav3mJAr8TUCxyXALQVXPf9UV_mEFYOIh0ch5l3GmX_x65KmqPiH75N9xp-sYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
برزیل از جام ‌جهانی حذف شد؛ نروژ با درخشش هالند به یک‌چهارم نهایی صعود کرد
🇧🇷
1️⃣
🏆
2️⃣
🇳🇴
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/667423" target="_blank">📅 13:55 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667422">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
اقتصاد ایران برای چهاردهمین ماه در رکود ماند
🔹
جدیدترین گزارش شاخص مدیران خرید (شامخ) از تداوم رکود در اقتصاد ایران حکایت دارد.
🔹
شامخ کل اقتصاد در اردیبهشت ۱۴۰۵ به ۴۲.۳ و شامخ بخش صنعت به ۴۵.۳ رسید.
🔹
اعدادی که برای چهاردهمین ماه متوالی، ماندگاری اقتصاد در محدوده رکود را تأیید می‌کنند.
🔹
شدت رکود نسبت به ماه‌های قبل اندکی کاهش یافته است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/667422" target="_blank">📅 13:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667421">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBQAw4LTYMdfbN3cb7eiwqaZnVpWgFqPlKLYBvfaZPtC8kIa-kLtc3-HyYL54vvjmyz6afknn3rsiXH4WnwxmAQEpV6160XZGChSwZLYGyYzcM-R7XfIsYc5XLrfkOXZsUfkDRGe-r5bOUWhMcmvaP7BUVI77fl02QVqiTghRtyD00D4X_JqaM_dp96XX-px9pEp3a1zTTGkrQMmnaeOQR2HimyuACzB5kw9ugX_sD9-696iNUsg486d-IIjTD0OH6zreSCKirv8o6k9za_EpwOIUhf7Z_Mhlddi7MIZe0rEjTm9ZmKm87ORAoYDdmPH1XVgCvew9SvSM70LICe5Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنگ آقای گلی در جام جهانی
🔹
مسی، هالند و امباپه با ۷ گل زده رقابت سختی برای کسب عنوان آقای کلی جام جهانی ۲۰۲۶ دارند
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/667421" target="_blank">📅 13:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667420">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
سردار حسن‌زاده: طی ساعات آینده خودرو حامل پیکرهای مطهر از میدان آزادی بزرگراه شهید لشگری را طی می‌کند امیدواریم طی چند ساعت آینده به نقطه پایانی تشییع برسیم #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/667420" target="_blank">📅 13:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667416">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HnibOjOOfU02wpdNr9JCdLX1TvqKgPFGhDnZ4a5xk1V2xRSltdeJ-TzHKJ-Xuh3NhEEiuHWXfUi3N145A6EEby2zNGmXugnFhshDCRlLm20GNVyxYcIfPXmSfkX7xPGhiS0jdDhCVboazCPifWe8nIEmYCu87BuIlUyryNg3BLx9qr2jVVpJgxIYOzMIP68hAPB_ByRJeY0byMEdVdfZEQgifv2cNokN65Zw1_ERbBZnAEupH9abQj3qwI0PDcUyXbzz2PKpRmgy-JInsy-GJoVy1PqsNKNYw768vA5y-T1o53_0svfHCapwiLW0crytU0C-E7SyjMaOJldkapYJHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cCEQOqhFPb0hnqgoquMEsWsFri96hMoM7N7K3VnD4sbdWelBDuEKVEU3ALdat05hNs0z8Sl5nI0S3IlMLULouEBw5QJVF5tuHf5cNboWSueTw1EdJajeKEmh0ua-euLefkf_6G8syngqXUXgROql7i9M2A7MRYOnwsqlkxGpHuelVSkcZfcXv28JS2PyOpIs9vsMz01U5b-YZ8XOacnphFvJ4CYr9h-YeC48HOPaydJBLCZTSUB4Na2NrZ1703SZDVmFyr0iAi8opb9ZIK_pv-HDcWrWOFPbnwYv4V1s76eZ0pgZeoj3omkE9_xAacUcgsft2ttNpJ2czyKGRRhGtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UuMP2cJuqOoT_aTW_x_U7EBvfjfeUIb93ocOvavpyjIJyoXlkpAW5BaSLWOj87ybY5IzySClV1G0T_j9_KxFiHttL2PkJFbaPeAY_brV1xyLxnerQWnTe9NMYudP0N8u9e7Gd19FBC1vAXtriHN-K3zysvSZb-PqEQ7ybGF1n8lm76Nn96Vv4MwcIkUR0NCbrya8kYGwzuMUj2PzxxHLMZbVVALxY55U5IPVq7LqqurgVtd_94DG5CIZcJkav0Lu12SPu4bC0x_y4WHryIFAg-aXMMN0hE2oJ0I4jEHkft7BaDJJEh1PKlDeFMejxHeFRvsVGklB5Lo-Y6U09uaZlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DshX6D96_DSifmRbZT4LbFdb1J7WlvtV0Pa8VTvQBfw-CgwZ4Ibol8_Ql7ExY8Vyn0PgVdHZiEiQA3Qa4oBX2JIDP3eduPM2bWCOuHrhjR9B4zw2yR2KQPxa-Vov1kAOcKDkEHaK-1IMwrA_jxarjQk9tMO4fPNJYTOhVMGdwCmb15yvq2w7hmBpkElS1pWp3-HRoL_gYH5IerI0ltQq9mK4xvEuymAs6h4sNXXuUTHD69KAnFCWZHESRYPOxleqoTo_vgIgMGJ9pb_FKUgEFlr6tjPgvTUqYu5oFMn2lT86D4W1Ayt3GDpy8AuSDZH5rs7K10xJouGk64IxPqk5Lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور عراقچی، جلیلی، وزیر کار و رئیس سازمان انرژی اتمی
در مراسم تشییع رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/667416" target="_blank">📅 13:42 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

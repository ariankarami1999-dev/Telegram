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
<img src="https://cdn4.telesco.pe/file/PYvkd-GTfp9RNpmKWmsuepLgvDaLAPwRDvz7YXofKsG_C-LMOf7PppC9eW_AR1JjDu1K_zN3hSYYsV9ZmGs0Yvd9t9vJtqDQ2kyyeehLKb3SxEHnC2DC1ZTBOhWV31OlZ2_VOJObeSwD7RND4WcFRmHN-6gImuHzvbII2IVMA4DCYaneKJmq-OCEsQ8rB9lZ77kIVRFKR3aBTMjCWrpe6RkuDQ9_D03xAY7anW1INRYqyVoWhQt-8sjCmR_XioTG0M8xRlyi6QyQhaxWppCN4PquuF7D9L3iiRnocQRSCwcc72X2cDpSFRp02KffArMwGsL_Si4hIyiD1LZatzbH-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 148K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 17:54:16</div>
<hr>

<div class="tg-post" id="msg-69017">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hm0Jj9lN-z4W_ajLriiR0duhnv-GVsedoKabU3HUh_xVWPaaEiNHZP2pnE0E7Z5Wn1v3DBraNagsuc98T9koSw-IXT5uFD_DRDxkQUhUy_vj9eHNFLrxLfB6jd3yqeGTY8-fqSMdd17ra4PdyySddpgaC_FXXm2Yg71_58kdB6fhJJ4qEFwr0WYHs_NglLvAqRb1KM8jPhVlA4kE6kLQxlUKT328V5FsUBEoOZzLTNY_Wf0IjhoJ-pgVZkY2inqQu3K_0Q8wWFxOPx_RmaZWXEGW6s3BRk2mAtDZXJjbWd8yzrYyfmNd_Q22YXXnOUcQn0mv-j11SpdFBMAmhlkGzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
العربیه:
- ایران به پاکستان اطلاع داد که از مذاکرات خارج نشده، بلکه مشارکت خود در آنها را به حالت تعلیق درآورده است و تمایل خود را برای از سرگیری مذاکرات در دوحه، ژنو یا اسلام آباد ابراز کرد.
ایران به میانجیگران گفت که با ایجاد مسیر جدید در تنگه هرمز موافقت نخواهد کرد و به پاکستان تأکید کرد که باید طبق یادداشت تفاهم به مذاکرات بازگردد.
ایران خواستار آن است که مذاکرات ابتدا بر تنگه هرمز، سپس بر دارایی‌های مسدود شده و در نهایت بر مسئله هسته‌ای متمرکز شود.
@News_Hut</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/news_hut/69017" target="_blank">📅 17:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69016">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dcf952e60.mp4?token=BQ1Kl_QBWfL4UaDlToECrfqBqKIIzJbLsFgBe9NSieB1yFFBIIWVFy9ywWa5LSdknTDWi-PI6MPP-ADN8g38Qr1I_O90NEtKAW9EQNewHx7oT3iw2PpygbAcgZPpisb74Kw0NqGdUQ9Ngu2YRtYgJ2tFpOKTtuN9JkHsqPkDDn2ZP-medtUm0T5MIqfWwTVN2AwfqvID7ZqXFrqIK62CoAJM--bYx68MermWiVayfjAgx1tOyNMZb4x7aSqofA6QWsAFRFFuX3n5vCDRiA4t9vHjN8w6CF8_q5v7qRLVbxqEuWgaVJlJHRJriHul5DGMJWX28LF-coPQ_smNW87T9YE2QcWpyPkOufrymRIxsHLHEcv95wDFi4lkXj13cR0w6SFsbBSXeIGHtI1rRIa8KVEZDhC4VGalJUrPiD34Z5NGFgg4U5cp_byFaJMoADdFdJhQC9TQnyB77_738ZL9wRDuk4ahbVLqHB1-2-jF5cqMJzZbbd-eAhvnaNNtXNiWaOANZd4hiclRUHi1z4ZIfXVQouxwJ5F4S7CuYuIrlREb383iNQntAiMHFCWizpG6ZPevm2uyAxPj3OudlvpA0TmLNunx-GcLhoe1Nw_xce8KDLVAckK_L30FhTcoL9IBN1EpqfsKu4OROWI73ArjMr3Sg5QjFEbbVEgz_dQ-RbI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dcf952e60.mp4?token=BQ1Kl_QBWfL4UaDlToECrfqBqKIIzJbLsFgBe9NSieB1yFFBIIWVFy9ywWa5LSdknTDWi-PI6MPP-ADN8g38Qr1I_O90NEtKAW9EQNewHx7oT3iw2PpygbAcgZPpisb74Kw0NqGdUQ9Ngu2YRtYgJ2tFpOKTtuN9JkHsqPkDDn2ZP-medtUm0T5MIqfWwTVN2AwfqvID7ZqXFrqIK62CoAJM--bYx68MermWiVayfjAgx1tOyNMZb4x7aSqofA6QWsAFRFFuX3n5vCDRiA4t9vHjN8w6CF8_q5v7qRLVbxqEuWgaVJlJHRJriHul5DGMJWX28LF-coPQ_smNW87T9YE2QcWpyPkOufrymRIxsHLHEcv95wDFi4lkXj13cR0w6SFsbBSXeIGHtI1rRIa8KVEZDhC4VGalJUrPiD34Z5NGFgg4U5cp_byFaJMoADdFdJhQC9TQnyB77_738ZL9wRDuk4ahbVLqHB1-2-jF5cqMJzZbbd-eAhvnaNNtXNiWaOANZd4hiclRUHi1z4ZIfXVQouxwJ5F4S7CuYuIrlREb383iNQntAiMHFCWizpG6ZPevm2uyAxPj3OudlvpA0TmLNunx-GcLhoe1Nw_xce8KDLVAckK_L30FhTcoL9IBN1EpqfsKu4OROWI73ArjMr3Sg5QjFEbbVEgz_dQ-RbI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو رو ببینید تا از انواع بمب سنگرشکن و هسته ای اگاه بشید.
@News_Hut</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/news_hut/69016" target="_blank">📅 17:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69014">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ead75df70e.mp4?token=eCeyXEAS90Ms4bWk3r3oXJqZ-geH2lnQq1q9eYt8Cv6prDnTVR9N05lABubjnqTmZd2c3MBqYru2Yz9HiILcp-qZxeRhf2DddfodKWfRhhgIEVWGfxeHUxJWKQJqw5Q867b50IkfS9oMYzzA_lTshzpyaMjxY3zZFAUNZyoYVfPYJgykUwGvg3Pj5HgfZk6JGDqglVDBP2AhcFwAti_cBYYsS3c1OHvMLPdhNDRonAkHqsTbLlmcpvm5Py75mLG-hcdDEsDpUFxEXZLl3gsjNTkw2RbffeLB1UCjl2CSxFXBG183KOYMgvkZZ64Z0tNBNxR99ozHss3K3BsOvk5BjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ead75df70e.mp4?token=eCeyXEAS90Ms4bWk3r3oXJqZ-geH2lnQq1q9eYt8Cv6prDnTVR9N05lABubjnqTmZd2c3MBqYru2Yz9HiILcp-qZxeRhf2DddfodKWfRhhgIEVWGfxeHUxJWKQJqw5Q867b50IkfS9oMYzzA_lTshzpyaMjxY3zZFAUNZyoYVfPYJgykUwGvg3Pj5HgfZk6JGDqglVDBP2AhcFwAti_cBYYsS3c1OHvMLPdhNDRonAkHqsTbLlmcpvm5Py75mLG-hcdDEsDpUFxEXZLl3gsjNTkw2RbffeLB1UCjl2CSxFXBG183KOYMgvkZZ64Z0tNBNxR99ozHss3K3BsOvk5BjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👑
شیوه برخورد با آخوندها در زمان رضاشاه از زبان خمینی.
رضاشاه، روحت‌شاد
👑
@News_Hut</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/69014" target="_blank">📅 16:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69013">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g75wtzPZw2SblXu6oXv5BZ6InUgOfJGiJNDS6VdHetuZLJ77wDSsl7o_Q20Kk2v4W4U6ri0uz2DrjIBinIkSc3s3Ik-Vd9TqKtwMcYNL3Epxj6dhCKz2Ugmjot4AA_9G9360td4-p1TFkLN27Bj0JLgmTxb-gzuahMSos42sSYWuL7NeFwp7CxexRid0KLmW0QrSxXka4tfSMmxkregjXJssT1N2CwPw-gWjm6dlUHqfG8DA4vrtEpOETP5upkUbokYxGH4f88BjeK2Mb8ekMwYkaz_mhl68CfeJChCOtIeytOtriJAaR-ZuY76eRTu2aNIzk3FoOnkWr7X1Vxg3Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
العربیه:
آمریکا و ایران به پیشنهاد مشترک پاکستان و قطر برای ازسرگیری مذاکرات، پاسخ داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/69013" target="_blank">📅 15:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69012">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oH-NTtkv-Up4LkjTEf8KPckOUWDbxnriyLA65RRPt518bla9DVh14li0S9MDzsQER3PcDHiPudoI6M4KoZM2dVGSesa3Z8ETS24l_waza2LiJR2m9jBeENORsPlnQAbCSk2jvygpAbbH8cG0R5m9NYdJ8m4G2jOr6I3Jna1M-s2eGNhXr4Ewz2sl8k3-CWn3gR792ZZk6IjakKo4j_uNu3t4Si0IPQyIDxw1_IsnCoCGrNgbO3Z1BqftXM48FenACPR7_p5QcwBnNno2FCtHncE98frk6EkT2mdOKgV4u-V0Xf_YC7V20_Cr4s7f0GzrpSYQWkn_obU2JpqxbS8PZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
امجد‌طاها روزنامه‌نگار عرب:
ترامپ حملات علیه رژیم جمهوری اسلامی را نه به دلیل مذاکرات، بلکه ظاهراً برای انتظار جهت برگزاری جلسه رهبران اسرائیل و دریافت آخرین تحولات از سوی آن‌ها، به تعویق انداخت.
این وقفه بیشتر به خریدن زمان شباهت دارد تا تغییر مسیر؛
تأخیر به معنای توقف نیست و آخر هفتهٔ پیشِ رو می‌تواند سرنوشت‌ساز باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/69012" target="_blank">📅 14:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69011">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3998a4eda0.mp4?token=NbvSKvRjnN_HwY-a8jtZWyDeSfKANY9kv1huz5KGbphcfVLwFPxE_3BT2cwqowx7Eb0D4vgY9Xk_ArsMpQ4TbFMKvqviI5VaeaGOC0LNd80fi2Gl8AP_0cy_HpPuC5I-drxN1XKYHIBjbNAMBLxhLavwa22snLqaC_GnBZFRpVoMcxsKFP4kl9yKvJ-y-Ye98Nb0o3zA0iZtzkgm6LvKkSHZdoN0ats_RO4IYcgjtXq40UwTNWhLlttsl9ZCgohtUWnZkSNN_JoFmNnTy2wM3vhp1e2BT5Gq4q8w-IxvOku8Jl_rnj_0qdRn0R_2_gJWn06rUMOcZXUmMehfzJrjGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3998a4eda0.mp4?token=NbvSKvRjnN_HwY-a8jtZWyDeSfKANY9kv1huz5KGbphcfVLwFPxE_3BT2cwqowx7Eb0D4vgY9Xk_ArsMpQ4TbFMKvqviI5VaeaGOC0LNd80fi2Gl8AP_0cy_HpPuC5I-drxN1XKYHIBjbNAMBLxhLavwa22snLqaC_GnBZFRpVoMcxsKFP4kl9yKvJ-y-Ye98Nb0o3zA0iZtzkgm6LvKkSHZdoN0ats_RO4IYcgjtXq40UwTNWhLlttsl9ZCgohtUWnZkSNN_JoFmNnTy2wM3vhp1e2BT5Gq4q8w-IxvOku8Jl_rnj_0qdRn0R_2_gJWn06rUMOcZXUmMehfzJrjGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
نخست‌وزیر نتانیاهو:
فردا به دعوت پرزیدنت ترامپ به واشنگتن سفر خواهم کرد تا با او ملاقات کنم.
پس از آن، در مراسمی به افتخار یکی از دوستان بزرگ اسرائیل، سناتور لیندسی گراهام، شرکت خواهم کرد. باید بگویم که او از زمان تأسیس اسرائیل یکی از بزرگترین دوستان اسرائیل بوده است و شایسته است که این افتخار را به او بدهیم.
من با رئیس جمهور ترامپ ملاقات خواهم کرد تا در مورد تمام مسائلی که در حال حاضر در دستور کار است، از جمله وضعیت ایران، گفتگو کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/69011" target="_blank">📅 14:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69008">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LHRd6ziU10MYZnjCkxjDvNuFiNRsOj-aOyCzAUrNjbvjUMQhaZZ84WLOxJHPEo7Uzx57X4NuPAyMhpycLadJLe16etp81qA49RuoCtMFXsZ2EQ0sjb_hAOyC3aOPpJprHuUPYIyw0XA8bnc-ZmEz4UdExTHcejfp_5wl-oU9F8yHBTS7Cv9_a78m8Xdn0tgzEOqI8iXLm2QUkJQFX-iPPakMEa3osK6eLUGzyo_sio5s7VuRzfPu9vQLHY-VMmclYr9Bgd-nH-OgVOTLkwZ_0conZDDkAC2ukaakWa7labGcCnqIiMiCwbSF1h4eTsQA9E_f8jTV-XFTZMsPicRGbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VhM_LCqynRbZ266g7KnyCRJf15p8chELdYMfkhw7O-NrCFhIvTZnrZXaOmB8yCxUT-651pPxhDlBomOxB6vDR3MZZ3g-NciJK1f5yd40ZEuzige_0lmBbWmC7d1jFGbEG8x6_Xq5zT7yPmdhHXJ4mcS9H0x7cjnACicR-64aIgyxfg6LQ9g3QQtKszryCl5vO2-p5rh_Xf2EDXVJRd8ljP4P822trlz6lzQM6a-GPlf-3rU4DWTWgBIsnCeyXbYlWnoNNGTnOtN7WyV8vqMiZZA5fC6gOH4ZAxn4xm8FLGanscRTWdEVpvkdol6OxdmcQeFlL0QJhxBjYmbD8yXJvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eb51b8cf9a.mp4?token=ZdIxXiJCFaL4XZS92FtVJC5xM9j3FGyFbqKW2qNBMvoxCMl5AkclwiJzavpF6272f3nhgGpaZz-QBmOITzARcSrqQgtqssgd311r6rP5QRV8KAe2OfenqaeXQ4XtSun0Xi8poVMAc1700s7thEkHqAYK09ygf1nnhEj0I4n22Yi3U3IkhC3fztFguURofM_MEZf4-Fn2Y1huMlRs3RnANsEZBmAcV1oES679xrAqb5_iMbvD5BBXn9TpMQdw7a5j5oujQJOxYR4bej7Tu13oA9vmmhufe3Ro6ScsaFq_v6N3BVcM10VtG3UWxHSNWwK3nTggJktV8ynK1sKjUpaEOg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eb51b8cf9a.mp4?token=ZdIxXiJCFaL4XZS92FtVJC5xM9j3FGyFbqKW2qNBMvoxCMl5AkclwiJzavpF6272f3nhgGpaZz-QBmOITzARcSrqQgtqssgd311r6rP5QRV8KAe2OfenqaeXQ4XtSun0Xi8poVMAc1700s7thEkHqAYK09ygf1nnhEj0I4n22Yi3U3IkhC3fztFguURofM_MEZf4-Fn2Y1huMlRs3RnANsEZBmAcV1oES679xrAqb5_iMbvD5BBXn9TpMQdw7a5j5oujQJOxYR4bej7Tu13oA9vmmhufe3Ro6ScsaFq_v6N3BVcM10VtG3UWxHSNWwK3nTggJktV8ynK1sKjUpaEOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
🤴
امروز ۴ ام مرداد، سالروز درگذشت رضا شاه بزرگ؛ بنیانگذار سلسله پهلویه.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/69008" target="_blank">📅 13:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69007">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇷
محبی سخنگوی سپاه یه لیست از خسارت های آمریکا گفته:
⏺
در حوزه راداری و پدافندی:
۷ مرکز فرماندهی و کنترل
۳ سامانه ارتباط ماهواره‌ای
۶ رادار پدافندی پاتریوت (سامانه‌های پاتریوت به قدری ضعیف شده است که موشکها و پهپادهای ایران بدون رهگیری به هدف می‌خورند)
۳ رادار کنترل و مانیتورینگ هوایی و دریایی
۸ سامانه راداری کشف و اخطار اولیه
۷ رادار دفاع موشکی هوایی
۳ سامانه راداری EPS
۲ رادار EPS 117
۵ رادار برد بلند
۲ رادار پدافندی
۱ مجوعه راداری تاکتیکی
⏺
در حوزه پشتیبانی و لجستیک به منظور کاهش توان عملیاتی:
۶ مرکز تعمیر و نگهداری جنگنده و بالگرد
۳ مرکز پشتیانی و لجستیک
۱۲ مخزن سوخت
۱۷ انبار پشتیبانی تسلیحاتی و قطعات شناورها و هواگردها
۶ زاغه موشکی
⏺
در حوزه زیرساختهای عملیاتی:
۶ آشیانه پهپاد ام کیو ۹
یک سوله آماده سازی جنگنده اف ۱۵
یک سوله پهپادی که ۸ پهپاد آکبند در آن بود
۲ مرکز فرماندهی
یک سکوی سوخت‌گیری ناو هواپیمابر
یک آشیانه هواپیمای پی ۸
۴ سکوی موشکی هایمارس
۵ آشیانه جنگنده
۴ مجتمع پدافند پاتریوت
۶ سکوی پرتاب موشکی
یک ایستگاه پمپاژ سوخت
۲ مرکز مخابرات سیگنالی
یک مرکز داده‌های اطلاعاتی
یک مرکز هوش مصنوعی، پایگاه مرکز پردازش داده مربوط به شرکت آمازون
یک مرکز دپوی شمپاد (شناور مدیریت‌پذیر از دور)
یک اسکله سوخت
۴ شلتر جنگنده
۶ رمپ پرواز و توقف
⏺
در حوزه عملیات هوایی:
۱۱ هواپیمای جنگنده و بالگرد (روی زمین)
۱۷ پهپاد شناساییی و عملیاتی (۸ تا آکبند بودند)
یک هواپیمای جنگنده اف ۱۵ داخل شلتر
یک هواپیمای پی ۸
یک هواپیمای ترابری سی ۱۷
۸ هواپیمای سوخت رسان
۴ بالگرد سنگین
۶ موشک ذخیره
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/69007" target="_blank">📅 13:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69006">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">⏺
🇮🇷
بقایی، سخنگوی وزارت خارجه جمهوری اسلامی:
مقامات ایران و عمان در تهران گفتگوهای سازنده‌ای درباره تنگه هرمز انجام دادند و رایزنی‌های فنی و سیاسی در این خصوص همچنان ادامه دارد.
چندین دور گفتگو در روزهای جمعه و شنبه در سطح معاونان وزرای امور خارجه برگزار شد. در شرایط کنونی، هیچ تغییری در تردد کشتیرانی در تنگه هرمز ایجاد نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/69006" target="_blank">📅 12:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69005">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
ویدیوی تعجب انگیز از داخل هواپیمای یاک-۵۲ که در آن تیراندازِ صندلی عقبِ اوکراینی، از کابینِ روباز با استفاده از تفنگ خود، پهپادهای گران (Geran) روسیه را سرنگون می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69005" target="_blank">📅 11:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69004">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/739d5c9e05.mp4?token=nLicy3rafCJLsc3AxY-i47xiglqh5HAJKphrTAD1wZMMpOLba0HWtW2357NB0ELBFhal1YeTatQ3vk-THhJzsKN46jhxjgvseEE2DAEaWuyO6U6KMXCXwFD5HtDpPwfqpO9yY1niNwIAD82z2ZiG6RS2Suu4oPUD066stiUDqvzuQCf98FuWUpCRR1ZDBhfyfJnjCN02as6FOQtXudSbV5ABQ8WeXMYUnm_l0LurkLothAqh0f1_HbMLmd797tfRisDN2fzOVW9u9FzcXF4u4e7zvBTiuWl_dDSghQpusTY8C5VI1ltJkhWxPFgrB_z4gg-lD-JNMdNVf8HMmQOBjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/739d5c9e05.mp4?token=nLicy3rafCJLsc3AxY-i47xiglqh5HAJKphrTAD1wZMMpOLba0HWtW2357NB0ELBFhal1YeTatQ3vk-THhJzsKN46jhxjgvseEE2DAEaWuyO6U6KMXCXwFD5HtDpPwfqpO9yY1niNwIAD82z2ZiG6RS2Suu4oPUD066stiUDqvzuQCf98FuWUpCRR1ZDBhfyfJnjCN02as6FOQtXudSbV5ABQ8WeXMYUnm_l0LurkLothAqh0f1_HbMLmd797tfRisDN2fzOVW9u9FzcXF4u4e7zvBTiuWl_dDSghQpusTY8C5VI1ltJkhWxPFgrB_z4gg-lD-JNMdNVf8HMmQOBjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
اکبراعلمی: مزد خدا بود و پاداش الهی بود که مجتبی انتخاب شد
😐
خدا امسال سه ماه قبل از قدیر ؛ قدیر رو برای ما نهادینه کرد و خدا برای ما مجتبی انتخاب کرد.
شهادت میدم والله خدا انتخاب کرد مجتبی رو.
با این انتخاب خدا کاری کرد نه نام خامنه ای نه راه خامنه ای تعطیل نشود‌.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69004" target="_blank">📅 10:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69003">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1efc7d4c9e.mp4?token=W95ah6vXvS1e38BtdKTfRKVsrzhnUMEEzaAnJ2DdWH0QtETjQDtLz2truOJWa2BIiRV_EMWyY_uoWg9Cgekhl17XrVCdmLeovwyD5koiRTJtYCpaGiXopE2FyAmvoDGrTXby4qFd6wW1FRgMHwDFbsfFpbWw-SQCJEf68E0cUVUPX0TVRgHe2at-8vUz5KpzSibIuJjdOtrofibvSi4duAv4y1nprf0TDQC66lQcxZgiySLYFr7_AQlIhbqqFKuidbEYh_p8Lp8umU-nnVkzrb3ln_q8O9W0w0aT2q8jcezWq5c2R7u04gNYJb3-pHhHMi_cvVNfuQ5wTnaJuJJzpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1efc7d4c9e.mp4?token=W95ah6vXvS1e38BtdKTfRKVsrzhnUMEEzaAnJ2DdWH0QtETjQDtLz2truOJWa2BIiRV_EMWyY_uoWg9Cgekhl17XrVCdmLeovwyD5koiRTJtYCpaGiXopE2FyAmvoDGrTXby4qFd6wW1FRgMHwDFbsfFpbWw-SQCJEf68E0cUVUPX0TVRgHe2at-8vUz5KpzSibIuJjdOtrofibvSi4duAv4y1nprf0TDQC66lQcxZgiySLYFr7_AQlIhbqqFKuidbEYh_p8Lp8umU-nnVkzrb3ln_q8O9W0w0aT2q8jcezWq5c2R7u04gNYJb3-pHhHMi_cvVNfuQ5wTnaJuJJzpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قبل از مرگ خاطرات آدم میاد جلو چشماش
من موقع مُردن:
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69003" target="_blank">📅 10:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69002">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuT63B1GKxsVNAKqRniCAOCIUaGABCPKioWq0veF0wpQxRwTHMm6yPBV0vdUTlHocifarYQ8ElQsUtVhu63bzxKlG-Z_7mfp5OgN5AaJ54_h4u7Cupl9rgFSjPAZxU6QtIbvb2mfwj_K6_9x7ZHcilwXNxuYBtTpvJk7gFPr5ACnYCP2drwcV-bDDfAIPEH7pdzpi5a_2GHx0NRlHcYJtVTJJ6gm7QejECQ6My_r1932nS6XVRD1g47NZH-n-SodnHdVZVy92kFiUtnGbm-BHW8VsX5aGGx3GdLnkB5aIoNtq4e4NRlpwcY32lGxZ3XcbMW7bLH0j9J8wN2RinIZEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نیویورک پست:آمریکا طرحی را برای ربودن اورانیوم غنی‌شده از تأسیسات هسته‌ای ایران بررسی می‌کند.
نیروهای عملیات ویژه آمریکا در حال آماده‌باش هستند تا «پیچیده‌ترین عملیات تاریخ نظامی» را برای تصاحب اورانیوم غنی‌شده ایران از تأسیسات هسته‌ای به‌شدت مستحکم‌شده، به اجرا درآورند.
جوزف راجرز، معاون مرکز مطالعات استراتژیک و بین‌المللی، گفت: «گفتنش برایم ناخوشایند است، اما فکر می‌کنم محتمل‌ترین راه برای خلاص شدن از شر مواد هسته‌ای ایران — دست‌کم آنچه اکنون در اختیار دارند — یک عملیات نظامی است؛ زیرا مذاکرات پیشرفت سریعی ندارند.»
یک منبع آگاه از برنامه‌ریزی نظامی روز جمعه به واشنگتن پست گفت: این عملیات بسیار پیچیده شامل هزاران نیروی زمینی خواهد بود که به تأسیسات هسته‌ای ایران حمله می‌کنند - از تله‌های انفجاری عبور می‌کنند، از خدمه ساختمانی استفاده می‌کنند و یک نیروی دفاعی بزرگ را در اطراف این سایت‌ها حفظ می‌کنند.
به گفته آن فرد، از آنجا یک تیم کوچک از نیروهای عملیات ویژه، عملیات واقعیِ بازیابی را انجام می‌دادند؛ فرآیندی که «بسیار خطرناک» توصیف شده است.
این یک عملیات لجستیکی سنگین و دشوار در یک محیط رقابتی خواهد بود. ارتش ایران کاملاً نابود شده است، اما آنها هنوز از افرادی که از مادورو محافظت می‌کردند، پیشرفته‌تر هستند.
بر اساس گزارش رسانه مستقل و مطلع «های ساید» (The High Side)، این گروه از نیروهای عملیات ویژه می‌تواند شامل «اسکادران نقره‌ای» (Silver Squadron) از تیم ۶ یگان ویژه نیروی دریایی (SEAL Team 6)، گردان دوم تکاوران (Ranger Battalion) و گروهان ۲۱ مهمات ارتش باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69002" target="_blank">📅 09:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69001">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dt8n_TpB0cFjFBi2s1PaMRRl7PeUTtpqBFH-tTkq0ukwrlfIKpSJxcmGN8y-huDKaIl8z1c6C81fUyKW8TVDbL0wRwS2GvXHXXPojazRy2RjXhMUYgpwUuZqg0OlzsAHF4YLDAR-I5IbhwIP8rZfNty-kmGKl9aYX_vlFNLMEilg7YouudwY9vBCPnHHdGClvdeWc61AjJwwY5IO-y2QAsL0mDL5-1NDDcijEN4vxhcQgmeEGeWt89siWnFBvwgMRCHWPUfWRmUEdat0O24bLGL2pfRSIYHWhWlw3PwNKr7T6BvBRu3F3BcwDVOBYnZ3wVV85UeV0FIWuubvnIQmUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
رادیو و تلویزیون اسرائیل:
با وجود تعویق حمله آمریکا به ایران در روز جمعه، روند پیوسته ورود هواپیماها و تسلیحات آمریکایی به اسرائیل همچنان ادامه دارد.
آمادگی‌های نظامی آمریکا، حتی پس از لغو حمله برنامه‌ریزی‌شده برای شب گذشته، همچنان در جریان است. این تقویت قوای نظامی، بخشی از تلاش گسترده‌تر آمریکا برای حفظ فشار و در عین حال، تلاش برای بازگشت به میز مذاکره محسوب می‌شود.
در حال حاضر، حدود ۹۰ فروند هواپیمای سوخت‌رسان هوایی به همراه یک اسکادران از جنگنده‌ها در اسرائیل مستقر هستند. طی روزهای اخیر، محموله‌های تسلیحاتی و موشک‌های رهگیر بیشتری نیز وارد شده‌اند که یادآور تدارکات و آمادگی‌های پیشین است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69001" target="_blank">📅 02:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69000">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eae9373361.mp4?token=pRKZ04vyMhnhri09akDm1LPWReurQFVrzBBwIOcV7MfLIsmlOkOMJXWIvmdCcJyH3RwX7u7OlNPY081RkqkruGP-sv8g4xNM37Jdh83kmrFJoQ8sRVt3mAnFDYLLfazwnRfc205MYHPn43-T_twUCcy68UHwT4GQlOuYDZ_sGyVweYx3EdRGsph_cGZ4ULZ1vcuntExI0noes-i0IvayLJKsaHNJGXX-dHmYt3uGRqv9mqIB-QnR0d1IcQVb_I6B6YJM-8Ouu60wk8MnoyElCvB8s-c5ekhGa9SH4dTg4TLNQihOGFxITReOCsebZRtDDBXovv2wJ0P_dTvk2QOtjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eae9373361.mp4?token=pRKZ04vyMhnhri09akDm1LPWReurQFVrzBBwIOcV7MfLIsmlOkOMJXWIvmdCcJyH3RwX7u7OlNPY081RkqkruGP-sv8g4xNM37Jdh83kmrFJoQ8sRVt3mAnFDYLLfazwnRfc205MYHPn43-T_twUCcy68UHwT4GQlOuYDZ_sGyVweYx3EdRGsph_cGZ4ULZ1vcuntExI0noes-i0IvayLJKsaHNJGXX-dHmYt3uGRqv9mqIB-QnR0d1IcQVb_I6B6YJM-8Ouu60wk8MnoyElCvB8s-c5ekhGa9SH4dTg4TLNQihOGFxITReOCsebZRtDDBXovv2wJ0P_dTvk2QOtjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو خاورمیانه همه دارن هر شب در هم میذارن.
🇮🇷
واکنش عباس داوینچی:
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69000" target="_blank">📅 02:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68999">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c262408b6b.mp4?token=VbAC8Km6g0iw-dtMVHakNoh0kZ31HqXXWtp60VQ1BztEoBUIq-h-Wf9gykRv13WBo6BSxex5mEkqpvhV72SS_P_RD1sZZ11SthOdgchxJMCvt8S0GkJZPsXCsqAQ7h7JuFCuMHZxD1ILsOtPrKFAgiQ7NJUqsH8_wqQtzh5ARyw7NjOW1lnUrdz70rY1AMyA63_ePTl_eQ0w07rcgQVRfSgcnOr02hB29PhTgPbsgopdXS8zDBAoi2uJSDZHdOdYFptuXHPnAh6vhcBm5Z6q4mEsEpf5zG5Z8zlhDu0uQEybVw4RFJQA4-PSz5IcoHljVzY8tUXf-ZZVbq3xPvuHGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c262408b6b.mp4?token=VbAC8Km6g0iw-dtMVHakNoh0kZ31HqXXWtp60VQ1BztEoBUIq-h-Wf9gykRv13WBo6BSxex5mEkqpvhV72SS_P_RD1sZZ11SthOdgchxJMCvt8S0GkJZPsXCsqAQ7h7JuFCuMHZxD1ILsOtPrKFAgiQ7NJUqsH8_wqQtzh5ARyw7NjOW1lnUrdz70rY1AMyA63_ePTl_eQ0w07rcgQVRfSgcnOr02hB29PhTgPbsgopdXS8zDBAoi2uJSDZHdOdYFptuXHPnAh6vhcBm5Z6q4mEsEpf5zG5Z8zlhDu0uQEybVw4RFJQA4-PSz5IcoHljVzY8tUXf-ZZVbq3xPvuHGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
محاصره دریایی ایران توسط ایالات متحده همچنان با تمام قوا در حال اجراست. تا تاریخ ۲۵ ژوئیه، فرماندهی مرکزی ایالات متحده (سنتکام) مسیر ۱۲ کشتی تجاری را که قصد عبور از این محاصره را داشتند تغییر داده، ۲ کشتی را که از دستورات پیروی نکردند از کار انداخته و برای اطمینان از رعایت کامل مقررات، وارد عرشه ۲ کشتی دیگر شده است.
پیش‌تر در روز جاری، نیروهای آمریکایی عملیات بازرسی و تأیید وضعیت را بر روی نفتکش «چارمینار» (Charminar) با پرچم کومور در دریای عرب به انجام رساندند و این نفتکش اکنون به مسیر خود ادامه می‌دهد.
نیروهای سنتکام در تاریخ ۲۴ ژوئیه، نفتکش «لاوین» (Lavine) با پرچم موزامبیک را در دریای عمان از کار انداختند؛ این اقدام پس از آن صورت گرفت که خدمه کشتی چندین بار تلاش کردند محاصره را نقض کنند و هشدارهای مکرر را نادیده گرفتند. این کشتی دیگر به سمت ایران حرکت نمی‌کند.
نیروهای آمریکایی همچنان بسیار هوشیار، متمرکز، مرگبار و آماده هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68999" target="_blank">📅 01:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68998">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_grE6OHQBPvQvezozuJenYYGsYRXjuQknrzZPEc9mW5gvXTELXK_aSk-YtmRDlCjPIsst2tPyrdAJbInR1JWlIB3UvcdiKT8wUGxsA09eBBV-XHRhZyehHMmjUDfYlqQEQJKG_KsdC9Qb8ufsn4KCdU2EuVTn_KdEq8pmmSoUqv8U4ujFPyKYku8IKjEii_lBaFJvgfJ0p9aAWSJUjY0vi9Z2rcvjaNYOYTGmpRh09VE2543mmK4fnwnoiesIjP4TR5rjWdQuc6mALXba7Kgcq2d8wV0HjNT_vdDNCy_J5bWpw_VqKYtZzHBWfi5foN-eOGT8fP3E2Dvj7DsUcJ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷ فروند هواپیمای سوخت‌رسان آمریکایی هم‌اکنون بر فراز خاورمیانه در حال پرواز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68998" target="_blank">📅 00:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68997">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
اوکراین، یک کشتی متعلق به جمهوری اسلامی را در دریای خزر هدف قرار داد!
تاکنون مرگ یک ملوان در این حمله تایید می‌شود، رئیس جمهور اوکراین می‌گوید این کشتی حامل محموله نظامی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68997" target="_blank">📅 23:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68996">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0101d071e9.mp4?token=EqniXM4m6OMvdVX7nYhd37oSTOtnhjylTQz6K0iXvzlVTVz2QFVAjtZX-WAl79IaswW6c4iGHePJCKMSozZnk7xkFTz--Fkuoa4jVj3Leodf23bFlQsfY3F8idnhHcEikkTycY3HPsW95z_Obdx21euLYZFC6XpJKxSR58UX2MQICBYggEtOw2GTyCT2bhfymbctoyFFUGdFzl_v_B-Xkaqn0PZ8Mg62FnJAOfih4fm5SV3RLjohUktBNWtWJBQeGxRGIGKatOr6oFvekW-FoS7_FrAZLgyKS_CJvYxPzKc6AYAKJV9tS79B6xhtE3ZBX_L2Yl3oIGS8ma8InFjC2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0101d071e9.mp4?token=EqniXM4m6OMvdVX7nYhd37oSTOtnhjylTQz6K0iXvzlVTVz2QFVAjtZX-WAl79IaswW6c4iGHePJCKMSozZnk7xkFTz--Fkuoa4jVj3Leodf23bFlQsfY3F8idnhHcEikkTycY3HPsW95z_Obdx21euLYZFC6XpJKxSR58UX2MQICBYggEtOw2GTyCT2bhfymbctoyFFUGdFzl_v_B-Xkaqn0PZ8Mg62FnJAOfih4fm5SV3RLjohUktBNWtWJBQeGxRGIGKatOr6oFvekW-FoS7_FrAZLgyKS_CJvYxPzKc6AYAKJV9tS79B6xhtE3ZBX_L2Yl3oIGS8ma8InFjC2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پیروزمند:
تا کی قراره ایشون ( مجتبی خامنه‌ای) بیرون نیاد؟
🎙
مجری:
تا نابودی کامل عوامل جنگ.
⏺
پیروزمند:
خب اینطوری شاید ده سال دیگه طول کشید خب ما تا کی اماممونو نبینیم؟ اینطوری همیشه در موضع ضعف میمونیم.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68996" target="_blank">📅 22:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68995">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1C3-VgQcfcryqgOkebK_uQ365IIOulvJo-pLPGzmcngvq6gxp1Ex58Hfgta2j1xmSjLUHa_-E09v8344vGZhO2k5rDxbCwPLHG7lJ7aQqNZXYElPU-Lk0YA9GcJYyq8xMmN39iGmoEnE_tsIO1flK473XF3cPR-jqEERP3r7f2RaPP1-JejBJXklxqXGIa5eWLkMzzhJo9J9AE3xkElaN__iOA4Viec5x0uGRWfqGTP-JE8awT5hpXZ7pBrRUmpZdETrcqSmTZGuaJn13x6uWxiA-F_5SoeVuAp3SMnBSHp0lxNf4_LbSi39qte2zIazTLnqamE5MYVlB9VbEnb9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ در گفتگوی تلفنی با شبکه فرانسوی «ال‌سی‌آی» (LCI):
اگر «صددرصدِ آنچه را می‌خواهیم به دست نیاوریم»، «قطعاً» گزینه ازسرگیری جنگ تمام‌عیار علیه ایران را مد نظر دارم.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68995" target="_blank">📅 21:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68994">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUc1DqU0SAG3Uh48ed3v2uA0KRGQPwuHqVSNTxRri1oMwOgi8CNC6Ys20fKWryVrVCt1JGDJc2eXDvxQB3CiOIn5_qmiArDnVI0o3uN3db95SDRnjv0V_J3aO9B18yltNBgTNsz6syH56RvvFsmmWZiSJtZNTFAj5QhNdDPpZ9AN86vurG6ELLncSPKVcs8iy_sMabdUuSgjzeDQqvj79Pd5WO0hkhKkDu3w02m65vozczk0xQs4vay7TtG85eK3iI43-Gfx1fkzGmR1z1jWuy9ATegvdJPqZXEpzTl-xFu0TTVVk0gO4IyLsfmG1xvCBfHjRSuwsdzjJtOOwz3pOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
اکسیوس:
رئیس جمهور ترامپ روز جمعه به ارتش ایالات متحده دستور داد حملات به ایران را متوقف کند و به تقریباً دو هفته حملات روزانه پایان داد.
این تصمیم در حالی گرفته شد که مقامات عمانی در تهران مذاکراتی داشتند و گزارش‌ها حاکی از پیشرفت در جهت توافق احتمالی برای بازگشایی تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68994" target="_blank">📅 21:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68992">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5v7W5kj0oqKG-bbrFxcJV7DJvEZj-gIIAHfGSHvC-GfGt8c8pC4-DyUA2hF9hduInLEWCTTPkthdQrVVAfhYh8h8E5doXs8pVo0_IwqvHbmdSxjr6VoaJ1NnBxkQqzPST-3obnV7VmWD58EOoRUwvG3taqjKCS9Dkh_2rPNpKmYQPAeliJQAsogFhtmNdfL6JYw3o09DqGKhZikj_9PxXcFh9BHEU8L1a_r536lQYefYABXfiv8rRXwFdiwMgc97TnDRO8p2iGXL6S1Poxp1Yn-VGQssYE71ojmLHmOQ28-bLYYAm14JFYT02ML8jSbfUC8lcM8-taGDzpCM3YQ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d601f15a28.mp4?token=HJK6uHUOUXnzVoZ8JyvJz9fcP4_8_fqgDlKY9JAJVCTKLzp09VaMMnVtLhScW8A0Tl0dgdTgjfW45nCyO2vYJ8Y5qByuk7u1IcFHMfdpsDG1ud0WPh7Rogn9H-yvv0Xyiq_stj25tR3GT-RR7GRmR_7XptandDAwxCj9hTQ4nCLpo7Qw5rYqQgE658qyvuAP2knVUKq0waQHkCyXirdlZNPe6ORFVKG5aNnvBaOqGxBzFQu4g03pZEpaUQ87k5RmhGAV3VEN8UGRGWMLbYcBZPgpxvGI0PBT3k1UO_02ATBL7P7J3Ge-FnMcboSoFJyRrO1Qh7Xwvg5A04nCjOoFkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d601f15a28.mp4?token=HJK6uHUOUXnzVoZ8JyvJz9fcP4_8_fqgDlKY9JAJVCTKLzp09VaMMnVtLhScW8A0Tl0dgdTgjfW45nCyO2vYJ8Y5qByuk7u1IcFHMfdpsDG1ud0WPh7Rogn9H-yvv0Xyiq_stj25tR3GT-RR7GRmR_7XptandDAwxCj9hTQ4nCLpo7Qw5rYqQgE658qyvuAP2knVUKq0waQHkCyXirdlZNPe6ORFVKG5aNnvBaOqGxBzFQu4g03pZEpaUQ87k5RmhGAV3VEN8UGRGWMLbYcBZPgpxvGI0PBT3k1UO_02ATBL7P7J3Ge-FnMcboSoFJyRrO1Qh7Xwvg5A04nCjOoFkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ساعاتی پیش یک هواپیمای آمریکایی در فرودگاه جده فرود آمده است. به نظر می‌رسد این هواپیما یک هواپیمای آواکس مدل E-3Sentryباشد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68992" target="_blank">📅 20:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68991">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiNtDerKPD8-BH5ePc1HtFpadmJN-f8L_dc0KZEQL6FYCBtFLm_XQi7FgI3rDNO68uKjqsRWqsoUAiXID0pUrUhbK-nH2GHcd76dihjE1pLnriOLRnrwtAsKmdREu8jhgor3NTtzFg_nU3tYxN3zDszuBgkPtLVJZSIEvh3LlIL7jbR64HRAV2yJNJ3x9UbYevFe5cIG5ff_hUFcEllLSTN9JkFmhNAXO6TkdYRwWIYvxGAwAEqjVOvmz4MPrQoCPgJ1M4ZJALuCvsMe5OiWBEVlCT2YtPUP-9tJihEejyf0joj1S-hQ0YbINHK5OPdDyJG7s9v-A_4QCr9YRlQyeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
باراک راوید، اکسیوس:
آمریکایی‌ها دیروز برای عملیاتی گسترده‌تر در ایران آماده نشده بودند، بلکه برای حمله‌ای تدارک دیده بودند که از نظر وسعت، مشابه حملاتی بود که هر شب در طول دو هفتهٔ گذشته انجام می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68991" target="_blank">📅 19:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68987">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4bab692977.mp4?token=CQlwADdAL5l0bB6PXKMrOkbW0PPBpQA32yCRZLavwdDw7Z4fs9V3MH7Fo8o0OA5Su6FQpTtiBFI1xeiWpnaSuvXR6pSmlSaUOK0BM6qWfMfVDVj4oon7YT09XJSsT9knLFBVn4y375_2a01Aiq8dcqbzeFpw5LE0n0XLsQgCcXua1s6wD1U8zSbyX0KzCqqHoTGoUFQJGtFMUwzewOhA5_REMMSRpSWu5kbV9MTISM1a91NpzFnN5C14lgu2YTxN2jH4DFvOYiIPAbQ-XhFxjXkdVZYkMWHXio0yPItqgd2EpLe5TvRnX2ILuZsvS-Mtst3und3kUAhnlcL50WGm9A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4bab692977.mp4?token=CQlwADdAL5l0bB6PXKMrOkbW0PPBpQA32yCRZLavwdDw7Z4fs9V3MH7Fo8o0OA5Su6FQpTtiBFI1xeiWpnaSuvXR6pSmlSaUOK0BM6qWfMfVDVj4oon7YT09XJSsT9knLFBVn4y375_2a01Aiq8dcqbzeFpw5LE0n0XLsQgCcXua1s6wD1U8zSbyX0KzCqqHoTGoUFQJGtFMUwzewOhA5_REMMSRpSWu5kbV9MTISM1a91NpzFnN5C14lgu2YTxN2jH4DFvOYiIPAbQ-XhFxjXkdVZYkMWHXio0yPItqgd2EpLe5TvRnX2ILuZsvS-Mtst3und3kUAhnlcL50WGm9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلنج شکن معروف اینستاگرام که هر چی داف بود میاورد پیش خودش و نالشون رو درمیاورد دستگیر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68987" target="_blank">📅 19:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68986">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bef5afefe.mp4?token=ppppKPTccOL62CZawbdi_fa7NLwRoTnpH1MwCMZ-4bKnef6O9N83B4hnwATg5KbyBYun6LrOpn5P77Hwps9GytlgX1LLZCNFjexA4v8Bd_dcY3YbDoEkdb9YTPr_9_9ZnJyXMXrIfGGVgcrnHj4E89iWpoq8xw8dc_xpEwbKzspWVeDDK2bM-tgvAQwQGyX1cEtUaPSP7tGz1hTHqdmlTU7ghbhJXaI7xQdsOVMlHSUiNp9XaTdWmptrY_rGgYSwoYMdi-2d_cAtnBCO6n64j_-gyuKECA4AhcCv5hWmXgb2MQcDGTi4ctS6j79AOnsb0R8HgRAl5jp-rh2NAsbSKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bef5afefe.mp4?token=ppppKPTccOL62CZawbdi_fa7NLwRoTnpH1MwCMZ-4bKnef6O9N83B4hnwATg5KbyBYun6LrOpn5P77Hwps9GytlgX1LLZCNFjexA4v8Bd_dcY3YbDoEkdb9YTPr_9_9ZnJyXMXrIfGGVgcrnHj4E89iWpoq8xw8dc_xpEwbKzspWVeDDK2bM-tgvAQwQGyX1cEtUaPSP7tGz1hTHqdmlTU7ghbhJXaI7xQdsOVMlHSUiNp9XaTdWmptrY_rGgYSwoYMdi-2d_cAtnBCO6n64j_-gyuKECA4AhcCv5hWmXgb2MQcDGTi4ctS6j79AOnsb0R8HgRAl5jp-rh2NAsbSKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تیم‌شی‌هی سناتور آمریکایی:
جمهوری اسلامی گروهی افراطی و تروریست هست که 47ساله کشور رو تصرف کرده و ایدئولوژی نفرت انگیز خودش رو گسترش میده.
این رژیم اهمیتی به سیاست های حزبی یا اینکه به چه کسی رای داده‌اید نمیدهد.
آنها میخواهد همه ما را بکشند.
ما این جنگ را شروع نکردیم، اما تمامش خواهیم کرد.
حملات موشکی پراکنده به کشتی ها یا تحرک قایق ها در تنگه‌هرمز نشانه قدرت نظامی نیست بلکه دست‌و‌پا زدن یک حکومت در حال سقوط است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68986" target="_blank">📅 18:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68985">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9esvzNIcONC4nDcq0aFOW64uckWHK0D0RGGrp6XFurg7jSMAxzKQaU9h8tYv_o-uvDrez9OHZRi3gvVDzljrhXH0OGfeZ5qdt7D0WT6cVoaiPH4aphSUDI_dBFrLjfJBUdP481ABIw3qN8IrogosYTAimRWGDU6bSQrCw9rtbr7zBNx50IFYgvbBOth6y8oUhpk2Yn75UP5qOgVVxub_ThhRGEhOD5SIV4jMfGLtukxI-IWPSovwwkGbO_YMXj-JaKS1aKMc10lIm6lT6rZl2eV_vY0qKza4YSNqkeQiapqTgM2P1y2Yn06Np6Gb8NsFZMgA3mN4FWKgZ_Q6oPKrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
وای‌نت:اسرائیل انتظار داشت که ترامپ دیشب ایران را بمباران کند، اما در نهایت از اقدام علیه تهران صرف‌نظر کرد.
اسرائیل روز گذشته را در حالت آماده‌باش برای یک حمله بزرگ آمریکایی سپری کرد و انتظار وقوع آن را در طول شب داشت؛ اما سپس متوجه شد که ترامپ در حال عقب‌نشینی و دادن فرصتی دیگر به تهران است.
قطر و عمان فشارهای سنگینی بر ایران وارد کرده بودند تا پیش از وقوع حمله‌ای که تقریباً قطعی به نظر می‌رسید، کوتاه بیاید. برای نخستین بار طی ۱۳ شب گذشته، ایالات متحده هیچ‌گونه حمله‌ای گزارش نکرد.
یک منبع اسرائیلی وضعیت را این‌گونه توصیف کرد: ترامپ تمایلی به حمله ندارد و تنها به این دلیل به سمت آن متمایل شده که احساس می‌کند دیگر گزینه‌ای پیش رو ندارد.
ارزیابی اسرائیل تغییری نکرده است: احتمال دستیابی به توافقی واقعی صفر است و تهران تنها موفق شده برای خود زمان بخرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68985" target="_blank">📅 18:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68984">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=Wvq5R75fRhZ4DcJKVVQtzfbkJXU6xc6HlJ-d0d7CAiitLEyRX1V3GRE2u3H1SnR5LhgOECY4tk7ByzIrnKlNHviNO8QHyW3VUCiWGQAM1vJehAPnm4QzmYxy2M5VSlJtcCRDSdkEmfpgP_VIHrG2GPiKumlRULYWXzjIEHHUovIiLwHvxJ1E0fVrik7qvcSxpxSIQJjR0JNHGegLcRtqz4oma9-hMUfwMdt2XGAuXndZ1n4QBaXV1l5bl-rsqrU9nSvLiZ0fmMUbFk4vjAvD3hxv5WlrTcmX2s6JCj3pbqQhyGcdUc2kYBX4VJl_lXnOp_UXg6JIjMgp9ATQRoh03Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=Wvq5R75fRhZ4DcJKVVQtzfbkJXU6xc6HlJ-d0d7CAiitLEyRX1V3GRE2u3H1SnR5LhgOECY4tk7ByzIrnKlNHviNO8QHyW3VUCiWGQAM1vJehAPnm4QzmYxy2M5VSlJtcCRDSdkEmfpgP_VIHrG2GPiKumlRULYWXzjIEHHUovIiLwHvxJ1E0fVrik7qvcSxpxSIQJjR0JNHGegLcRtqz4oma9-hMUfwMdt2XGAuXndZ1n4QBaXV1l5bl-rsqrU9nSvLiZ0fmMUbFk4vjAvD3hxv5WlrTcmX2s6JCj3pbqQhyGcdUc2kYBX4VJl_lXnOp_UXg6JIjMgp9ATQRoh03Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فارس با انتشار این ویدیو:
مردم جاسک، اسلحه‌ به‌ دست منتظر اومدنِ نیروهای آمریکایی هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68984" target="_blank">📅 17:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68983">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f3b976f59.mp4?token=acM96Z_E74w0qKpUzkwm6sW9o0Mw-XdH-TorcDQG86V7zqt_rVAUC33Nbjt9qDEBCenaz7CNbvypw6NeIAIjHaaRk3I-_WoutiSo6DIl266BBiGhSX_Pg7TYjFwtLE1NE9Q3VEg26SCNLh6SoFi7nEenADB1KbSxqwd3BXE-WsQzPqHUEH9F2d4tgdWxToHJgYzxIwk8Yp4AhJvVIrbtn-XTVXSZQsFvWRnj7txTvtqtu7jNK1ioumkz0cjIFOuGQ4gJIOu3JW4pq5k_rAin7JZ8ulkZIX_8JT-kSWMuGAKmAAqgljqMuID0gM1Dobr8Qf1JHL-RmOTFEtLa_B7CTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f3b976f59.mp4?token=acM96Z_E74w0qKpUzkwm6sW9o0Mw-XdH-TorcDQG86V7zqt_rVAUC33Nbjt9qDEBCenaz7CNbvypw6NeIAIjHaaRk3I-_WoutiSo6DIl266BBiGhSX_Pg7TYjFwtLE1NE9Q3VEg26SCNLh6SoFi7nEenADB1KbSxqwd3BXE-WsQzPqHUEH9F2d4tgdWxToHJgYzxIwk8Yp4AhJvVIrbtn-XTVXSZQsFvWRnj7txTvtqtu7jNK1ioumkz0cjIFOuGQ4gJIOu3JW4pq5k_rAin7JZ8ulkZIX_8JT-kSWMuGAKmAAqgljqMuID0gM1Dobr8Qf1JHL-RmOTFEtLa_B7CTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی از طرفداران حکومت، با انتشار این کلیپ آمادگی خودشو جهت
مبارزه زمینی
با آمریکایی‌ها به رخ کشید
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68983" target="_blank">📅 16:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68982">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">⏺
🇾🇪
بیانیه نیروهای حوثی:
در پاسخ به تجاوز آشکار و جنایتکارانه عربستان سعودی، نیروهای مسلح یمن دو عملیات نظامی دقیق و موفقیت‌آمیز انجام دادند. عملیات نخست، با استفاده از ده‌ها فروند موشک بالستیک و پهپاد، تأسیسات حساس شرکت آرامکو در جیزان را هدف قرار داد.
عملیات دوم نیز با بهره‌گیری از تعدادی موشک بالستیک و کروز و همچنین پهپاد، تأسیسات حساس شرکت آرامکو در ینبع را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68982" target="_blank">📅 16:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68981">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e90df6b87.mp4?token=vFm66_OVeP9O_AiXpNxCNhVzY4vQrRlcABBOlzKpxNHKyHlN_zLk9ngB35PWCZ91RsAKjKpeOOo1OQW9LeR-GH5zQTioIVPJ9njX-lfWNNdAA8q-AS_-QukUEH3cBClPUvfkZT_KSZmbESn3QXQGSFyBlL0XXGRvNvWRrNfA6R2z6Mv2xE9BE0ViYr-Jro4MY57lGA4JDCMx9NmnTn09wV27xU9QqXKCZ_PhNSQ4XOPJPzWMoC3aj0W_Gi94Rwyu8ifS4kmG7BpXAY9MRgHWveKG6_e5GsC81I8AWDWVXw_Hmou9pJ3ke6pkxxgL3H6rgyBt-4R_l3ku-__575q_2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e90df6b87.mp4?token=vFm66_OVeP9O_AiXpNxCNhVzY4vQrRlcABBOlzKpxNHKyHlN_zLk9ngB35PWCZ91RsAKjKpeOOo1OQW9LeR-GH5zQTioIVPJ9njX-lfWNNdAA8q-AS_-QukUEH3cBClPUvfkZT_KSZmbESn3QXQGSFyBlL0XXGRvNvWRrNfA6R2z6Mv2xE9BE0ViYr-Jro4MY57lGA4JDCMx9NmnTn09wV27xU9QqXKCZ_PhNSQ4XOPJPzWMoC3aj0W_Gi94Rwyu8ifS4kmG7BpXAY9MRgHWveKG6_e5GsC81I8AWDWVXw_Hmou9pJ3ke6pkxxgL3H6rgyBt-4R_l3ku-__575q_2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صحبتای دیروز پزشکیان که تا به بحث مذاکرات رسید صداوسیما سانسورش کرد:
بعد از جنگ 12 روزه، علی خامنه‌ای رسما اعلام کرد که ما دیگه با آمریکا گفتگو نمیکنیم و صداسیما هم اعلام کرد.
یه روز رفتم پیش علی خامنه‌ای و گفتم خودتون گفتید نه جنگ - نه صلح، حالا ما چکار کنیم؟ گفتش که برید مذاکره کنید و ما به دستور علی خامنه‌ای گفتگو با آمریکا رو شروع کردیم.
تو آخرین پیامش هم گفتش که برید مشکل رو حل کنید چون تو حالتِ نه جنگ - نه صلح نمیشه کاری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68981" target="_blank">📅 15:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68980">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0e5554ef4.mp4?token=fPtRxmVGHL1u8IzZ1ioir-G8hCDmXEM7WeWnvne06qRV60u20klIqhi9bJkhPPHCehreZpC0oPvzJ4-7pbXWhn54gwrLjFrpG2NzE10YeMJU_37ZfuWRLJBGvjLfYWg4wizEdpuFZJ_yHTTV5Ul48UUCJEXw1L-IlsweEZQfzP4VD85dHg0hub5ckw1O7tWv611MEz-67ZBFYThBDzqENLQclW2RbR9yyiZGJJdAS_eUUlB5IME1cowQMMGR7KDST1yM-VNRTdLh8fMmx21MPH5aBJUUObaPeWtOiUbZMALDBYK8-_cshZprHjWG1PBbgDxyiM7YgOH_stKA0s3SIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0e5554ef4.mp4?token=fPtRxmVGHL1u8IzZ1ioir-G8hCDmXEM7WeWnvne06qRV60u20klIqhi9bJkhPPHCehreZpC0oPvzJ4-7pbXWhn54gwrLjFrpG2NzE10YeMJU_37ZfuWRLJBGvjLfYWg4wizEdpuFZJ_yHTTV5Ul48UUCJEXw1L-IlsweEZQfzP4VD85dHg0hub5ckw1O7tWv611MEz-67ZBFYThBDzqENLQclW2RbR9yyiZGJJdAS_eUUlB5IME1cowQMMGR7KDST1yM-VNRTdLh8fMmx21MPH5aBJUUObaPeWtOiUbZMALDBYK8-_cshZprHjWG1PBbgDxyiM7YgOH_stKA0s3SIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروهی از طرفدارهای حکومت با مقوا عکس رهبران ارشد نظام درست کردن و اومدن تو خیابون
😳
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68980" target="_blank">📅 15:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68979">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=dPjNpC3M51PUP8fuWL3nOCgI9wn0_07oazf6uHJqu11bNQ4ceTZMJS_a_mG0HxV1-8XPwpl41DrhPgi7PivH9HBgP0XNnwCJKWNzDCIdo9GV96JyXSubMWBNm1tzVVWKBiyDHOTe6_Dr8SPpQxUmC_fbjMYxs6swtmu_flui7tOBfxlOXvANfkD8_7doo4_-lS9E5FATL36UjPPwapGBVyZ_3jqPo_AvtSnSwxQ5JPSHKiSuH7sMbHhdFc86V03UxO4X75RdFjCVoZjVnX7TRuZUzXXtUmWtfY0dQr8zTd1TfzhSvIQGWi2q42-HoZN5gTJEwp2XJukK4AvhsAkyGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=dPjNpC3M51PUP8fuWL3nOCgI9wn0_07oazf6uHJqu11bNQ4ceTZMJS_a_mG0HxV1-8XPwpl41DrhPgi7PivH9HBgP0XNnwCJKWNzDCIdo9GV96JyXSubMWBNm1tzVVWKBiyDHOTe6_Dr8SPpQxUmC_fbjMYxs6swtmu_flui7tOBfxlOXvANfkD8_7doo4_-lS9E5FATL36UjPPwapGBVyZ_3jqPo_AvtSnSwxQ5JPSHKiSuH7sMbHhdFc86V03UxO4X75RdFjCVoZjVnX7TRuZUzXXtUmWtfY0dQr8zTd1TfzhSvIQGWi2q42-HoZN5gTJEwp2XJukK4AvhsAkyGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی دولت:
تغییر قیمت یا سهمیه بنزین قطعی است.ما علاقه‌مند به افزایش قیمت هستیم!
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68979" target="_blank">📅 14:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68978">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HkRWbQi0wciQ6pjm3ExB3mlJ8_esagyb3JSvgRrQ2em6e4UCWVLnrDye7tFus0_g3XHXU8AnRwiiaoYlJ-bDKMY68aBLdoMnEpZ3wRddEvJ0aT-SHDNSE1cLIQ-LRXRtNHp8JSHlNEoHlT7GZA3o3lYiQm2MdEYLEf2PHCv6AQxo-5W_AxILqtKnoSOO_7DBdGMoFMQ3lbJwQpe5XunRmEA4pO6JPkzDUxWsC02ebzoFA_xwjgpBGnLqg8ZPG0ALFssUXIBoEyx-0drsGirIkCp2mZv74zOUMMy3ZGkn8MctiFEAkZViPXPFldB1qHfoEC4O6ntPeKD5Vcjjs-Sl2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقچی:
در پی حوادث تنگه هرمز، طی مذاکرات سوئیس تصمیم گرفتیم برای جلوگیری از سوءتفاهم‌ها، یک خط ارتباطی مستقیم ایجاد کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68978" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68977">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97b75ab51b.mp4?token=A3QnCY3xh6Y6RJwRb2cf7LqartYX-8WCAioTIhJ7O_coS5znrERAjaFNiOjRMRINDZnvEdalH8GfXCymvJKsPcFH3_bG-q0bhDXmcXoxs6YsR2Lcz-oI9nJ_Fr-sibjFXvWeOQO5uYObEnRdZsGdVfZCccKMo5DXO-CAcoJXJbkZ5V9AreORkQ_o-ffFX3GH7qv9jk1oiFm0W1NQdqofiZL-R_OEbkp9ILqRwHZ1IW5sVsegqqAoK8K_mK15vO9fhLf0Gm9KZqrRhQZDnVxkQpfA8VpG1ppaA30NJ0hstwZ3biEfVyQAlRd84pzFSjWkSl8Q1QaEp1bEEE1Nvhwx-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97b75ab51b.mp4?token=A3QnCY3xh6Y6RJwRb2cf7LqartYX-8WCAioTIhJ7O_coS5znrERAjaFNiOjRMRINDZnvEdalH8GfXCymvJKsPcFH3_bG-q0bhDXmcXoxs6YsR2Lcz-oI9nJ_Fr-sibjFXvWeOQO5uYObEnRdZsGdVfZCccKMo5DXO-CAcoJXJbkZ5V9AreORkQ_o-ffFX3GH7qv9jk1oiFm0W1NQdqofiZL-R_OEbkp9ILqRwHZ1IW5sVsegqqAoK8K_mK15vO9fhLf0Gm9KZqrRhQZDnVxkQpfA8VpG1ppaA30NJ0hstwZ3biEfVyQAlRd84pzFSjWkSl8Q1QaEp1bEEE1Nvhwx-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حمله موشکی حوثی های یمن به پالایشگاه جازان شرکت آرامکو
عربستان
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68977" target="_blank">📅 12:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68976">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNM-hORStjdKJ1PROh1Vmlpj80S4_RIBmjWWbh74E2hVmxcdaDh_DCOHvzBpbRVNunTqNc8GnGrKPBhuYdUTuzIM9F6NzQ7H8tz4e2CGLSmKNrhgaSsKu60zY1CfqckUFdZlrRE_uNVXWGO3SxBaYY2Bz203qYPPIM2_7xttUQ3ZmaiKYR7A_vgmsQAso6IWyT4qpirbHWieo5U7rI-oyJkbWQtez6LMY9og1a4qAKCTLi5xEe_5z252wCjbe_vQgzmuUHJWf0o13th9FiE-_dx8q1G9baxQr2hRJCqsjfLNjNHh0821lWtD1jGjCgBEXJ1cT0U-okUvY064iyXeWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سازمان تجارت دریایی بریتانیا (UKMTO):
سازمان عملیات تجارت دریایی بریتانیا گزارشی مبنی بر وقوع حادثه‌ای مربوط به یک نفتکش و نیروهای نظامی در خلیج عمان دریافت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68976" target="_blank">📅 12:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68975">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb03afaeb6.mp4?token=lFttTOxWuSvR-gnQdVwWPExppQ5Rb-Rr59mLbCwvT2gya0YrxcXErYg2Wz1eJSKKGPtxsCMjzg1lfmlRURxkcrnDNeJ87UiId71u4y06PQEysnm_VmKEdBuZwuA2UEELR6sHwJVkpbkgvK_3zRdx5bMYtAdTovy5ldeBZd7r2OmUYv61TMHYeMTJOPubujkLyKLRc7Gd8VDlVOfwOrGGP3r49F9CpSfQK9NTd8iZkxgID5jROsuxxPCIIigWJrho81EH3OIEBRHEBQ0b094SVaNyjHi9H5inrPiZCnt3AaJh65xH-e8ylGuooW5VZWsP7cUInTHkfMos1qyykgUhrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb03afaeb6.mp4?token=lFttTOxWuSvR-gnQdVwWPExppQ5Rb-Rr59mLbCwvT2gya0YrxcXErYg2Wz1eJSKKGPtxsCMjzg1lfmlRURxkcrnDNeJ87UiId71u4y06PQEysnm_VmKEdBuZwuA2UEELR6sHwJVkpbkgvK_3zRdx5bMYtAdTovy5ldeBZd7r2OmUYv61TMHYeMTJOPubujkLyKLRc7Gd8VDlVOfwOrGGP3r49F9CpSfQK9NTd8iZkxgID5jROsuxxPCIIigWJrho81EH3OIEBRHEBQ0b094SVaNyjHi9H5inrPiZCnt3AaJh65xH-e8ylGuooW5VZWsP7cUInTHkfMos1qyykgUhrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
مجتبی خامنه ای چندماهه رهبر شده ولی حتی کسی صداشم نشنیده. اون حتی به مراسم تشییع پدرش نیومد. خیلیا هم معتقد هستن که اون مرده. نظر تو چیه؟
🇮🇱
نتانیاهو:
حرفات درسته ولی طبق ارزیابی ما اون زنده هست
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68975" target="_blank">📅 11:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68974">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">💢
ویدیو وایرال شده، پشم‌ریزون از گات تلنت
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68974" target="_blank">📅 11:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68973">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c123fd5ae9.mp4?token=AlMxkhk8d5P5sPYWb31rYHOz4cBGr-yPRY03b1SqxTLJ65RTR9GOlOsqNjW318gYlg39KZsSeZ3kcDiioPKiBu0YIPW-mZFO7qbHVR-cC-e1iyrxkNcGDVLuU888r9OOYPnwdb1-5_y9PUmQZM5Xyc6ALei4sZktjUnha6ilMMO_IIGCJPtFUhGyIwCPnI-J4jMh2QS2gae5MTfnNyRL13ozoi-who-OHKw4RJBfsAvJJUV9Aa1ySfmwkLg4HaaDxOIXSIDz4DTrgNlKrH23-0mEpDKvIGPNGi-OpmqT0a2z8IG2p52CKVQLNYndjbxwF1CkO8QML_tU5SaQo0sYMzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c123fd5ae9.mp4?token=AlMxkhk8d5P5sPYWb31rYHOz4cBGr-yPRY03b1SqxTLJ65RTR9GOlOsqNjW318gYlg39KZsSeZ3kcDiioPKiBu0YIPW-mZFO7qbHVR-cC-e1iyrxkNcGDVLuU888r9OOYPnwdb1-5_y9PUmQZM5Xyc6ALei4sZktjUnha6ilMMO_IIGCJPtFUhGyIwCPnI-J4jMh2QS2gae5MTfnNyRL13ozoi-who-OHKw4RJBfsAvJJUV9Aa1ySfmwkLg4HaaDxOIXSIDz4DTrgNlKrH23-0mEpDKvIGPNGi-OpmqT0a2z8IG2p52CKVQLNYndjbxwF1CkO8QML_tU5SaQo0sYMzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از یک تحلیلگر سیاسی که زمان پهلوی هم بوده:
یه نفر نشسته بود تو کاباره داشت ویسکی میخورد.
طرف کی بود ؟ قصاب بود !
به بغل دستیش میگه ما ک اینجا نشستیم داریم ویسکی میخوریم بعد تو ببین اون بالاسری های فلان فلان شده چه کیفی میکنن و چه بساطی دارن پس.
اینطوری ناراضی بودن مردم از پهلوی!
مردم رو اینطوری ناراضی کرده بودن روشنفکرا.
بهشون گفته بودن میدونید شما خیلی بالاتر از اینها هستید.
انقلاب رو روستایی ها نکردن انقلاب رو روشنفکرا و دانشگاهی ها کردن بعد اولین ضربه رو هم خودشون خوردن.
به مردم گفتن عاای شما وضع اقتصادیتون خیلی بهتر از اینا باید باشه ببینید اون سرمایه دارها چیا دارن که این همه خورد خوراک به شما رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68973" target="_blank">📅 10:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68972">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6904f498.mp4?token=qFhu6ACESnRh69pMNjY9DK3YugyA8H9V97ZsItZ2w6dV2qttHt7Mzyg498AOjjbfNuKbQ-gb9Veqm4Xa0PXjxdiF8CDAFOI4xQ5iWzfVSpRy5yzBceVJMwVNSz7mm85LnkbsYR04JJEtuNM7Mn0WhZMyrpashGvnHLHm1JRLSGPis-_PGWcm0yUpwebT2jw3hWvKlh_8zhaB3emo9IW6teUVvSjHWfvAJqBODGtGMHGVInnR-estIbxNgFXVB9zndMGAwwtw3_Xz8-FQWMfvRENHsEK3jK5KpFnOTL73iuFr3p9j69B9nEDfaBTfMSmJiZ2tebfG1sNE4UgwLnINWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6904f498.mp4?token=qFhu6ACESnRh69pMNjY9DK3YugyA8H9V97ZsItZ2w6dV2qttHt7Mzyg498AOjjbfNuKbQ-gb9Veqm4Xa0PXjxdiF8CDAFOI4xQ5iWzfVSpRy5yzBceVJMwVNSz7mm85LnkbsYR04JJEtuNM7Mn0WhZMyrpashGvnHLHm1JRLSGPis-_PGWcm0yUpwebT2jw3hWvKlh_8zhaB3emo9IW6teUVvSjHWfvAJqBODGtGMHGVInnR-estIbxNgFXVB9zndMGAwwtw3_Xz8-FQWMfvRENHsEK3jK5KpFnOTL73iuFr3p9j69B9nEDfaBTfMSmJiZ2tebfG1sNE4UgwLnINWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره رهبری ایران:
«حالا که همه اهالی رسانه اینجا یک‌جا جمع هستند، باید بگویم که ما به دستاوردهای فوق‌العاده‌ای رسیده‌ایم که رسانه‌ها هرگز درباره‌شان حرفی نمی‌زنند؛
برای مثال، در دوران دولت من، رژیمی که زمانی قدرتمند و هراس‌انگیز بود و بی‌وقفه به آمریکا حمله می‌کرد، سرانجام سرنگون شد
رهبران پیشین آن کنار زده شدند
و اکنون توسط یک دیکتاتور گی(همجنسگرا)اداره می‌شود که با اختلافات داخلی دست‌به‌گریبان است.
با این حال، من شخصاً برای باری وایس در شبکه CBS آرزوی موفقیت دارم. او زن فوق‌العاده‌ای است.»
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/68972" target="_blank">📅 09:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68971">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=t46GK2b6So-NbQNMYedsghVLqTL5h7gt_f7Om4EP51M5o2cfKSCdRDZexQ-XcxiaUuOUXByeWNKLQLgA8aoJSkKxJ4g7txQnAldClUGPyIEH5tmbfD8XBbz1z1VVYOWnJm0J4ANemaqLzkQfn2Ya8c1PhkSrIHtVGrtcxdgezlmTOObQ-lS-1dtU7nciQ4lsSgN5-sQ1E_8OvOT3RMEkH9vXJPeLiT2vQiPkSCdx8Ta7IY8pnLe8BhahFKHZjs9lTouAVqfD8KHDRC1H6plsSF46jBywTI0IZmkGO9S16fxN2WnTWB3nmrSkawmT4Inj3WiMwzQSbDzBPlwlrF0CbjfBUJD7tCoyI3h8i7wNEbExNr2feIqpzHvAWsngXzY_eHdhBrbL4ez6zZ3VOAgH75yFtSB_w3nIMYinF42fDOwVO_xtystOWhdBxZ56VBQj2_ZSHtilsIyxudk6DKeAh17eo63sgafL6I7O52uzq1UvbyN6OJTAY_RYQlHiJnD2VYvUITP5kOhatdWQlAQJ0m0mKEBFTKmAociB1yYdgcIwmMyIjVLV5lL5ed4tIlGFml67NtGD-306LHehj6NDyBB_7RztRTM4a6NSSa0b5Bjh6-xvWZpf9iHf_-OT09y7J413MK9Il4ys8QdUWsmKAwNzwT5CKWz0SxlK9VQc7u8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=t46GK2b6So-NbQNMYedsghVLqTL5h7gt_f7Om4EP51M5o2cfKSCdRDZexQ-XcxiaUuOUXByeWNKLQLgA8aoJSkKxJ4g7txQnAldClUGPyIEH5tmbfD8XBbz1z1VVYOWnJm0J4ANemaqLzkQfn2Ya8c1PhkSrIHtVGrtcxdgezlmTOObQ-lS-1dtU7nciQ4lsSgN5-sQ1E_8OvOT3RMEkH9vXJPeLiT2vQiPkSCdx8Ta7IY8pnLe8BhahFKHZjs9lTouAVqfD8KHDRC1H6plsSF46jBywTI0IZmkGO9S16fxN2WnTWB3nmrSkawmT4Inj3WiMwzQSbDzBPlwlrF0CbjfBUJD7tCoyI3h8i7wNEbExNr2feIqpzHvAWsngXzY_eHdhBrbL4ez6zZ3VOAgH75yFtSB_w3nIMYinF42fDOwVO_xtystOWhdBxZ56VBQj2_ZSHtilsIyxudk6DKeAh17eo63sgafL6I7O52uzq1UvbyN6OJTAY_RYQlHiJnD2VYvUITP5kOhatdWQlAQJ0m0mKEBFTKmAociB1yYdgcIwmMyIjVLV5lL5ed4tIlGFml67NtGD-306LHehj6NDyBB_7RztRTM4a6NSSa0b5Bjh6-xvWZpf9iHf_-OT09y7J413MK9Il4ys8QdUWsmKAwNzwT5CKWz0SxlK9VQc7u8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بررسی اهداف احتمالی حملات آمریکا توسط فاکس نیوز زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/68971" target="_blank">📅 09:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68970">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">بعد از سیزده شب، امشب جنوب آرومه و خبری از انفجار نیست، و متاسفانه این آرامش، ترسناک تره!
#hjAly‌</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/68970" target="_blank">📅 03:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68969">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQJhuI9aYKyLcAegvb0V5ZLTdQJO7_-PYcjbHMyIs89iH5fbReZm9pmiyvk-AJHtAv3pYk-7Xkitly0McHVBKfuq7x5Tl1ubFn0UUlw7UgbiuyibDi7KIkvfWhl3iWHuRn59GLpeYv4GtfQoXbqXWrrHUZrL5mRXUX1TzEmBK4SYxRtB5YlFcKA8i61UBFQR8tsjzd0q304INb6WMXWDZ1PfXOVE17Maxy5VeRyJJOsAu6P5fhfBw3goWpIzMcsH2ZhLezVsWM5dgWqZkXVjf0lb53OF7-iQyEIjz-9Z-L__Ncps9HtN4Zh0SthdE1qOfPfiM2x4g_p_vD4dD5U7_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شبکه فایتوکس به نقل از مقامات اروپایی:
در اروپا این اجماع رو به افزایش است که ترامپ پیش از کاهش تنش، آن را تشدید خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/68969" target="_blank">📅 03:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68968">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b03773bd.mp4?token=Xnuncfl5tGIcbeugQc5kOY18Uikq-fRQJk611zqFmEG4W4TkEd_Iv5eVRIWPWeR4FRdFxPs-7S3ZwM4WNoQzQTM9K4DqaR7E8Z9evNcCVOEwc-buDwWL9lfb_hyOrqCbQskA2nmfdbs79Xul4wh_nHAZ-1MZFKgQitKgRy3w3OSKsp29L3RimD_9tHyJoi8xMVey-Gwxo8zpdBZWQ8uh6zF0xzfIeKRo1NAP8MVzZePRjFcAdlKmoqIKJnSWG52_xGblvAGQNhxqq2Q82intTIY7V15ckzpCZpaCwxkmUA23mS16Rvw57ggMALYSgafJdWDWFDXRiOyFClobeHi60Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b03773bd.mp4?token=Xnuncfl5tGIcbeugQc5kOY18Uikq-fRQJk611zqFmEG4W4TkEd_Iv5eVRIWPWeR4FRdFxPs-7S3ZwM4WNoQzQTM9K4DqaR7E8Z9evNcCVOEwc-buDwWL9lfb_hyOrqCbQskA2nmfdbs79Xul4wh_nHAZ-1MZFKgQitKgRy3w3OSKsp29L3RimD_9tHyJoi8xMVey-Gwxo8zpdBZWQ8uh6zF0xzfIeKRo1NAP8MVzZePRjFcAdlKmoqIKJnSWG52_xGblvAGQNhxqq2Q82intTIY7V15ckzpCZpaCwxkmUA23mS16Rvw57ggMALYSgafJdWDWFDXRiOyFClobeHi60Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پدافند هوایی روسیه یک پهپاد اوکراینی را بر فراز انبار «وایلدبریز» در سن‌پترزبورگ سرنگون کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/news_hut/68968" target="_blank">📅 02:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68967">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CA0ZdAg4mT3i6xKuUpcEwvbQa0vaC7lXCptkGd4S5KknE_viZ1rkJqdtsoY4b8Ifh1ou4GGuHM5YxkgIOUb3xHN2_WRSMd2MWYjr-qpIARGd1mPQufBktLpJmBEZZI92wksaQsP-ghiDFgxg4o53QGxonjIDx3s9KoaHNbJ64aqOnX9GNV4q-nBsnA6wurkCL7Y0RYOGCgMSDprBeB-QpoXxh0D1FK2Tcim8mlvjHd_XRhsUTbHp1B-3osZbx1Frrnuj_lPgMhrHKZZIusyFMwON59f8Npswy6UcP3L7zSAwPW93hw-qYRxcjHjC6QRuVdum0253ronNuOaWzNtzEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ارتش‌آمریکا: یک‌کشتی مرتبط با ایران که سعی در نقض محاصره دریایی داشت رو منهدم کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/68967" target="_blank">📅 01:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68966">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjZo0KhxbcNDxR6uBAwwkyOwH8il4lS5WaQDjdQ9oiJxqjLK9KE1M3miWjB6kyUX5PZYfeKeFSITQEC5wJKavIcGUrl0E1uKj3sVUWKjXUr0dG8L8wDEoFG1KOb5cFahMpPqGUP42yVwNTbEmj7ms3DYm6uLJakkgNRtfT5CCT2Ums5rMC1mMZ9bfhPz2qLtkp94_cbE7aQu2D1n96QIR7-cCoAPhKhKQTeGAHDfkj4C10zXPvgyUGa49gSSVOZ85K1nBlzjQl_depRU5oqPbuG58-aptmWATwUuAfBl0DGLWlHFLYgQ-H9ak_WE1kCHMFfLZ0sDGittgezJvvdnJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/news_hut/68966" target="_blank">📅 01:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68965">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/poWhfSlD1siljrhp__2hJCTLZKBvAfjgGlMhyM2eNGZ9In6WSyM06jmTRb27XvujzxjVYx_yu2sKYkPBpb73dgK97iKUuM1xA4G_HPACPbvNr78id9En9O5OYo5W18eHTtUCYTNq2UPJ1pDgQ3oC4-VatFq_yYeo5q4xA9I6K6jW-mwhV4Ha1kI_WqjyA3ITZKBL0WOCcxAiXzTrLv4s5D3zSJiXBpC_Ms69ow3X-KhZaMqHcFQmYIJNS-0cMuDmqJjilznajOUoUXhWDHV8iOBdyNA1wOZuHM1mIBhD8dd7aGxdXuLDR0OXMWQ2pvHfG_1HWxLrVjF4E5ehArFo-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
رکوردهایی که ترامپ تو این مدت تو مصاحبه‌هاش ثبت کرده؛
«ما ایران رو شکست دادیم.» - 106 بار
«ما ایران رو نابود کردیم.» - 95 بار
«توافق با ایران نزدیکه.» - 88 بار
«تنگه هرمز بازه.» - 75 بار
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/68965" target="_blank">📅 00:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68964">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9fhXLEvbePUnokDNvR0SEhhGUr7UdCQCGp1wmhnKbhfcNehNxgGjVPPS0ckyguOfTJRo792LibGLbI3Ao9uyXl_T3v3YwqAc4enMxKU4cNH1sWinISJJDcFqMDJQe7OFtBWKPvuBomA6dg83W0v3SB_TI-eoTIVL0alAFowNdyU4c2JogokuNIO1KkQvzpgrhySWzyjsl9ZE-vDzRTEfWnbHyXzlfVrsZytv7kQwbcuoDbR6UEqh2Tp-NKe9raOTuQuzximMsemFTbWCt00mOOSTqJ_W1T6BJzotLEmtWHCy4qR3AdqYUkEnQOTmgBnyJGvBJV_fP_aBZ2Io3sqDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
عربستان دقایقی پیش به بندر حدیده یمن حمله کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68964" target="_blank">📅 00:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68963">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🎙
خبرنگار:
آیا شما در حال بررسی یک حمله گسترده به ایران هستید؟
🔴
🇺🇸
پرزیدنت ترامپ:
"ما آماده حمله هستیم. ما کاملا مسلح و آماده حمله هستیم. ما با آنها صحبت می‌کنیم. شاید یک نقطه عطف وجود داشته باشد یا نباشد... در حال حاضر، ما به طور جدی با آنها صحبت می‌کنیم. اما به نظر نمی‌رسد که بتوانند به آنجا برسند، شاید اکنون بتوانند."
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/68963" target="_blank">📅 00:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68962">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
بهبهان صدای انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68962" target="_blank">📅 00:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68958">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eSmu5rlqHY99vC2mpi7UKlurndUX_Io4qIAyhZq6i0MuUYFa4QT9W8rAWzZ9TTdGQvPkOwJlOdhq4VkXT6gPLgVnAoKXfzLmSLscdOIqqs_FT_TFrU-IRGmBtosqk5SmU9t1iczsbNEKqb8kPTvuZj8mgCaC4BN3rLsaRkpGOkl1NtcY3TAPhgv83rHRsBy2tGZQOIHX3Y2VnoK3aoJzAD_D6Se6lcwIOxXJy-5BhdMJ6DTymNkuLSVyWJqXOxa3-kB9kngFvh-Kg-o3IliOCU5THO18oFBlRfbMks7ydF73JxYQMayI6KBvCTaDsJTriLImTCH1xBY_KKDNpv1JNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JT8g5-SstVmH16Frl9QVwjk_-myWrgI7EwsTIYemZA4_qC9Q0m94VFudmCY8EQ4dGJNbRdK4QzxAQaXkODPq3c-eOuJrPNqJY03tl54eoTyZqmDduuorjOohQ547ou9g1rJXLVDK5plryRqTTZ2Y5n7EN7ZwyUd7-nLXKqo-L0b70hfI07HL9asU1lN_1J1pjDXWcV-2prmc5JlytJF5Efhu9sH7VIXVwVNegwQh6h79bkS21nlmxUc8NyhjC9G9ef0RC2EOw45P8wcoICuH_TN1saIvAlgPcd2xuwuqXQlWXx5WiAwawlswcmqW8Vh9kV-AweKhVCisLytnrWqP-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5123a793b7.mp4?token=UnswzijrN3jIotFy5TsOsQwTmijWAuKwNJpy4WZTK6JfqbnYDLCZqhhUmh9nVb48fsy3cnVP2VnxLwqW1yDvQJCHYso0_e5CEF5EK-0Cr4V8cspB4C1OcdH_WO7MTvIETnUD-K45O4ajuekRWGxPigTAOJkswBSQtfaupNVXcrx7semW89-KXb-UAxzZuUW8AsRudOqdwA4ZjjNjpab4eGxnGYrIBW-CE9dZAyX5hNrf_8O0_H8JW2UE5Aw0fy9KN9zCPC_Kr67XpdP_-AFGwHVIhsfsRJhcuuWh16CgM1Zb2LN_lP_C_ygRl5zh5WXKfL7IRL4ZsgnhHsEdWaLSQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5123a793b7.mp4?token=UnswzijrN3jIotFy5TsOsQwTmijWAuKwNJpy4WZTK6JfqbnYDLCZqhhUmh9nVb48fsy3cnVP2VnxLwqW1yDvQJCHYso0_e5CEF5EK-0Cr4V8cspB4C1OcdH_WO7MTvIETnUD-K45O4ajuekRWGxPigTAOJkswBSQtfaupNVXcrx7semW89-KXb-UAxzZuUW8AsRudOqdwA4ZjjNjpab4eGxnGYrIBW-CE9dZAyX5hNrf_8O0_H8JW2UE5Aw0fy9KN9zCPC_Kr67XpdP_-AFGwHVIhsfsRJhcuuWh16CgM1Zb2LN_lP_C_ygRl5zh5WXKfL7IRL4ZsgnhHsEdWaLSQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🚀
❌
🇷🇺
یک حمله دیگر با استفاده از پهپادهای اوکراینی به مرکز لجستیکی ویلبریز (Wildberries) در شهر سن پترزبورگ، روسیه.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68958" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68957">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=m9TBuBzhxVMmhxSrdmW3y2dTHapIpaXwRTq4FZgJM3psd9WHKMKC90746oczK2MGIkskf5pRekxhjOqadh7T5iQisGd2HLvqlMujhn1TX_EKUsD3OG6xn9vFmRbQm1-Rn97XOPb21Ha26CHvt7FNTTj29-kuXaDlzbO5ZmvjUPmv4ja9Efato4EtvNi-tKwpyjczxAqCRtzIQV5HE75qEuO6MtdE8LE2cJ-QnJpRAVG7a62bVLJVwbgJIycWGWN0_xknmGolPiRBHQbORHE5w8pAjwcttWDYh2Xo7fUxD6J-T4Qhk1azWvVu1wT-WAP1S-CsTvdj-PfYUFo93AcVJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=m9TBuBzhxVMmhxSrdmW3y2dTHapIpaXwRTq4FZgJM3psd9WHKMKC90746oczK2MGIkskf5pRekxhjOqadh7T5iQisGd2HLvqlMujhn1TX_EKUsD3OG6xn9vFmRbQm1-Rn97XOPb21Ha26CHvt7FNTTj29-kuXaDlzbO5ZmvjUPmv4ja9Efato4EtvNi-tKwpyjczxAqCRtzIQV5HE75qEuO6MtdE8LE2cJ-QnJpRAVG7a62bVLJVwbgJIycWGWN0_xknmGolPiRBHQbORHE5w8pAjwcttWDYh2Xo7fUxD6J-T4Qhk1azWvVu1wT-WAP1S-CsTvdj-PfYUFo93AcVJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ :
وقتی توی یه جنگ
داری قاطعانه برنده می‌شی
، باید چیکار کنی؟ دست از جنگ بکشی؟
ما با اختلاف زیادی
داریم این جنگ رو می‌بریم.
همین الان هم در حال مذاکره با ایرانی‌ها هستیم و اونا
آماده انجام کارهایین که قبلاً حتی حاضر نبودن بهش فکر کنن.
🎙
خبرنگار:
شما به آکسیوس گفتید در حال بررسی یک
«حمله گسترده»
به ایران هستید. نقطه‌ای که تصمیم نهایی رو می‌گیرید چیه؟
🇺🇸
ترامپ:
ما در حال مذاکره باهاشون هستیم. شاید اصلاً به اون نقطه نرسیم، شاید هم برسیم.
🎙
خبرنگار:
ایران کی بالاخره کوتاه میاد و پای میز مذاکره می‌شینه؟
🇺🇸
ترامپ:
شاید کوتاه بیان، شاید هم برن توی یه غار و همون‌جا قایم بشن.
اونا غارهای خیلی عمیقی دارن که می‌تونن توش پنهان بشن.
ایران، باورنکردنیه، ولی شروع کرد به شلیک به همه جای خاورمیانه.
اگه سلاح هسته‌ای داشت، حتماً از اون هم استفاده می‌کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68957" target="_blank">📅 23:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68956">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=rstwUWsXA6XnPIXXLtS73GTEAUl7lluQvYImD1ehYlm7H_Q2BtNxcfKyXoVa6_QqytSv7hGK3mZO4F6Nn6dcQBNiLLgxqlAkshwPyvu6A_HnAIJSF9iaw6ZXkDhuKLwVrAndZqDmzKTJ-a0lGlHRzJhCz6zt6oQ7Fo3EBub1S_y9itxhRHlNV0yIq4S6wBKvvmp8vXkqUQXtwtCGKYUVjrYPYXgRVhnEFEW4juOUcmeViQxqKRDw3CrQ-zuYe5sYx6BD1E4v3Gf9XQzWP8iiXayQ048ci9K1neiFKNOkk7wln5u4-LSiDGUqiQ6omdTS-1LpJ1ilQ1ZVHI28weG5gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=rstwUWsXA6XnPIXXLtS73GTEAUl7lluQvYImD1ehYlm7H_Q2BtNxcfKyXoVa6_QqytSv7hGK3mZO4F6Nn6dcQBNiLLgxqlAkshwPyvu6A_HnAIJSF9iaw6ZXkDhuKLwVrAndZqDmzKTJ-a0lGlHRzJhCz6zt6oQ7Fo3EBub1S_y9itxhRHlNV0yIq4S6wBKvvmp8vXkqUQXtwtCGKYUVjrYPYXgRVhnEFEW4juOUcmeViQxqKRDw3CrQ-zuYe5sYx6BD1E4v3Gf9XQzWP8iiXayQ048ci9K1neiFKNOkk7wln5u4-LSiDGUqiQ6omdTS-1LpJ1ilQ1ZVHI28weG5gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
یه انگل هست که باعث اسهال شدید مردم آمریکا میشه. کی دوباره میشه کاهو خورد؟
🇺🇸
ترامپ:
نمیدونم. بهش فکر نکردم. پیتر، زیاد کاهو میخوری؟
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68956" target="_blank">📅 23:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68955">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=oTaQb0Fj5MjEkUnteHwAzemC2G2_XR6DM7qa8iK6iLP1Fic9ItKap2lMM9I_olGe10Rq_ulgHb-zRjFSeqGCKJyafsk_1V3_c6oxxq_UZE3PnFEg0dIRTyakCMIHsZHXENOb0i07GPbl5B-jdFEt9PpcVYucFfMZrby0H12s7EzRyn6_9ab-L4pk1CrAzEbtRrgnCBSwO-W9MO9S_pVQEzI8KQ2jNpzNybB3Bu8uQpVqK4qSjxIvSUmYusRrFRNvCsCMNKhmPYcDeP1SMWfdD90t4pkZysGsIVnYlZNswuGB1G99FnU3oLKOyQLn0y1wQde_ai3M48nQ4SQaadh3Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=oTaQb0Fj5MjEkUnteHwAzemC2G2_XR6DM7qa8iK6iLP1Fic9ItKap2lMM9I_olGe10Rq_ulgHb-zRjFSeqGCKJyafsk_1V3_c6oxxq_UZE3PnFEg0dIRTyakCMIHsZHXENOb0i07GPbl5B-jdFEt9PpcVYucFfMZrby0H12s7EzRyn6_9ab-L4pk1CrAzEbtRrgnCBSwO-W9MO9S_pVQEzI8KQ2jNpzNybB3Bu8uQpVqK4qSjxIvSUmYusRrFRNvCsCMNKhmPYcDeP1SMWfdD90t4pkZysGsIVnYlZNswuGB1G99FnU3oLKOyQLn0y1wQde_ai3M48nQ4SQaadh3Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
وقتی من وارد ونزوئلا شدم، همه مخالف آن بودند. اما دو روز بعد، آن‌ها گفتند: «وای، این فوق‌العاده است.»
بسیاری از افراد همین حرف را درباره ایران هم می‌زنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68955" target="_blank">📅 23:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68954">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=GM9_Wr5MBqSzs9NuiXR4WA9E-7ewRMEIYOyF-IHgwBfG_pVO4vvqL8JtSi3FMlnsTGZ5fscRwDIEcwsT_Wb4VfFXlYDl2ZwqM-wC8dVFVobCA1Y7w1VoJE-SY3VnxftGmQCcZE0WVyipVjcf_wXp0D_xenWqoRxjZCWlCR6V2dPKdvo2x2w-YIciNbAnlP5uY4GOgNuKBuOKLiSEcNagVhWUkLHmKH2XNqnZnm43d3bDoWXCTxzRuFan3ueSXSeM61KBjB0yK7N9HSL51asdA654vYpARUUc5IAI1qkFFJ_cNITQ49n_1ulqOvz-DrMkG2y8OTG3zUD4vS7TzY_53g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=GM9_Wr5MBqSzs9NuiXR4WA9E-7ewRMEIYOyF-IHgwBfG_pVO4vvqL8JtSi3FMlnsTGZ5fscRwDIEcwsT_Wb4VfFXlYDl2ZwqM-wC8dVFVobCA1Y7w1VoJE-SY3VnxftGmQCcZE0WVyipVjcf_wXp0D_xenWqoRxjZCWlCR6V2dPKdvo2x2w-YIciNbAnlP5uY4GOgNuKBuOKLiSEcNagVhWUkLHmKH2XNqnZnm43d3bDoWXCTxzRuFan3ueSXSeM61KBjB0yK7N9HSL51asdA654vYpARUUc5IAI1qkFFJ_cNITQ49n_1ulqOvz-DrMkG2y8OTG3zUD4vS7TzY_53g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
همین الان هم در حال مذاکره باهاشون هستیم. به نظرم هر روز که می‌گذره،
دارن جدی‌تر می‌شن.
من معتقدم
توافق، راه عاقلانه‌تره
؛ اما کاری که الان داریم انجام میدیم،
راه ساده‌تره.
همه‌چیز آماده‌ست و هر لحظه می‌تونیم اقدام کنیم.
وقتی وارد ونزوئلا شدم، همه مخالف بودن. اما فقط دو روز بعد می‌گفتن:
«وای، فوق‌العاده بود!»
الان هم خیلی‌ها دارن همین حرف رو درباره ایران میزنن.
به نظرم،
ایرانی‌ها تا اینجای کار از همیشه جدی‌تر به نظر می‌رسن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68954" target="_blank">📅 23:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68953">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=eUtw0g-eAFIB19wDoOyEhXye2plLwNVwDYWtLdv715kBmp1XVlbYcTsBGJ6MuQNkSqomuy08GiFR-cBeuBJMADhQfihRbTUN_tR7tnfLqcfv6buLAuNehmYgoDN5Zy0y9FlfA1DcMT_qp6XsrW2OhyM2eqNpz03G_EbHp8sayImKNGErQefXWbJ4C5WAL08pBM2SFpgQQv-9HbBxOZDDGDSjDqdH9MezD_Tt0amt5B-aFXa9T77kdWAND9rLsxiH0OvOjaiQs-9uFZzEyzaM2h-rG1m-UuDy9J1FPHj73xZ6s4phPjEWc3gFCP-pvO-5onD5X51IHnPJvyciAofT_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=eUtw0g-eAFIB19wDoOyEhXye2plLwNVwDYWtLdv715kBmp1XVlbYcTsBGJ6MuQNkSqomuy08GiFR-cBeuBJMADhQfihRbTUN_tR7tnfLqcfv6buLAuNehmYgoDN5Zy0y9FlfA1DcMT_qp6XsrW2OhyM2eqNpz03G_EbHp8sayImKNGErQefXWbJ4C5WAL08pBM2SFpgQQv-9HbBxOZDDGDSjDqdH9MezD_Tt0amt5B-aFXa9T77kdWAND9rLsxiH0OvOjaiQs-9uFZzEyzaM2h-rG1m-UuDy9J1FPHj73xZ6s4phPjEWc3gFCP-pvO-5onD5X51IHnPJvyciAofT_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شما درباره بمباران نیروگاه‌های برق غیرنظامی و پل‌ها صحبت می‌کنید. بخش بزرگی از جهان این کار رو جنایت جنگی می‌دونه. شما هم همین نظر رو دارید؟
🇺🇸
ترامپ:
به این سؤال جواب نمیدم. شما از کدوم رسانه‌ای هستید؟
🎙
خبرنگار:
نیویورک تایمز.
🇺🇸
ترامپ:
حدسش رو زده بودم؛ نیویورک تایمزِ ورشکسته!
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68953" target="_blank">📅 23:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68952">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMna5aNOZ5dmLPPlx6qMNWilwJIjeV8pzIEBv7F9wTckPOB1mc7G79bNPDd1OuF8hWcnK_KvvLMo_BHRyjtDj527-Tk-RG70rO9TrfxSD75JNZoKQJG-hJSMgIyPwx2KAj0ovLQE_Emk8WV_D2L5CHFqnRaKyaZ8j-L6VZ8835UixT-UV2vGJUupIlwhcMROniej-bdVBBySjEKiTuCh-WsjLW2j9k-jFSTRJP18_vLcnifWiByHMQQNCwVml2iiK5GD_W3KoNQu_7GNPA4synxTbDImE_t9DM6RdJTKINHGr99jBQ0l5wU-jJ2UDSv4-BaT3odMFbpypEdYnqkPUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
صداوسیما:
دشمن آمریکایی دو موشک شلیک کرد که یک نفتکش (یا تانکر) حامل گاز را هدف قرار دادند؛ شناوری که از دریای عمان می‌آمد و قصد ورود به منطقه را داشت.
نیروهای آمریکایی گمان می‌کردند که این شناور قصد حمل گاز ایران را دارد. اصابت دو موشک به آن منجر به کشته شدن دو تن از خدمه و آسیب دیدن موتور شناور و در نتیجه توقف آن شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68952" target="_blank">📅 23:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68951">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">⏺
ثابتی خطاب به شهریاری:
تو دیپلمات وزارت خارجه بودی چجوری شدی استاندار؟
اصلا بچه شمال شرقی، چجوری الان استاندار در شمال غرب شدی.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68951" target="_blank">📅 22:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68950">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🇺🇸
نیویورک‌تایمز:
نهادهای اطلاعاتی آمریکا بر این باورند که رهبر عالی جدید ایران، آیت‌الله مجتبی خامنه‌ای، بسیار بیش از پدر و سلف خود به دستیابی به سلاح هسته‌ای تمایل دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68950" target="_blank">📅 22:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68949">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhtKdhaEpjfZvr5WEXsSYx-wnfNZlIc11y1HiAkNsF1j7bBYr3BWCZsV-MPjQ97rn_vwJXBO4j0pNThVpVjQjocwIOwKAdha5vhCwNauT5verfuCUYLB34Xcbz_NycPUTrLjtCKLwp-Sl5cAbow2lB4ZVW-mDoG24vH3lh8HwF4jH-pvdthYGnrMUSYa01cyc0VLSjLMLvbujMExBU8MfyY1iP9cw-B29BbK10JXr3TW24BBbV_va4MRyvtNTx5k47Q7xT3tqAWHQ7DtjdgOvl5J5Wwdmem17djfbHU95ycH_-Ifby3NZ42sg7DYwAvloa6XGidsd9t8lkAPB6LXDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیویورک‌تایمز:
رئیس‌جمهور ترامپ روز جمعه با مشاوران ارشد و اعضای بلندپایه کابینه خود دیدار کرد تا درباره تشدید حمله نظامی علیه ایران تصمیم‌گیری کند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68949" target="_blank">📅 22:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68948">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQIPvZHv9Gwm1_LzEyVn03nxE0Jo2M0blY64IrFpIngfvCYFXNXEI3Eybhgev2kgm6gTSW5JRB-25XwWZHlEnNNfuJDDmCYubm5PxwLIN3kxO4i6qScnQzfz5jMJXidYuFdW965xONWIySgtmrkzFc1Sd1W0RGfJfRtjo-uvzQ3Tkj4gJssiQpTOh58U1qyH3trN6OULrLKDgsOPpa9Q1faH_X0JcBDqM1JtuZGD4DJCDvuwXYTx7SDtoXJhDDsS1lr31Q3YXhUC46B6gVosmeefk-Qo3NBUMACn0oa4hcox08uOeq_jUgflm-rtoIzzajm3kKvazCdVX1zGsd_Brw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ در تروث:
تشکر از نخست وزیر بلغارستان برای در اختیار گذاشتن پایگاه هوایی این کشور با وجود تهدیدات ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68948" target="_blank">📅 21:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68947">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78c449631.mp4?token=YjZadZDCXXM8js-kSYD3M0AvvLJAJ5nYnkWN-po3-cVkXT5OJMwRue8ma520zHEN36sLqvW5yht5KdZV2gdElyP5k3fS-nKdez95VnByy5lf7wG9Q1SIzY8FMfAk5Vg8TUlvWW8_2IPjTUawGmax5lVpcdyPUA2OJzJohJPJjXtMiNrTfOu04PkGMQXVPkAguZtbUCfhWRgdJmzB0ErWW_5SsKZ3KIGhKPkRMOoul8Gq_qWhrE9tkeEY047FzXwBwXryk74iIcSDKgwD-8wc1HnCju0OkW5_bkiylix1J5WH4MKhEqkiVVBYTegcL3112beEGC6nKCYoGlmZGbk01A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78c449631.mp4?token=YjZadZDCXXM8js-kSYD3M0AvvLJAJ5nYnkWN-po3-cVkXT5OJMwRue8ma520zHEN36sLqvW5yht5KdZV2gdElyP5k3fS-nKdez95VnByy5lf7wG9Q1SIzY8FMfAk5Vg8TUlvWW8_2IPjTUawGmax5lVpcdyPUA2OJzJohJPJjXtMiNrTfOu04PkGMQXVPkAguZtbUCfhWRgdJmzB0ErWW_5SsKZ3KIGhKPkRMOoul8Gq_qWhrE9tkeEY047FzXwBwXryk74iIcSDKgwD-8wc1HnCju0OkW5_bkiylix1J5WH4MKhEqkiVVBYTegcL3112beEGC6nKCYoGlmZGbk01A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
آخرین مصاحبه اکبرعبدی با گریه:
ماهی یک میلیون تومن به خانواده ها پول میدن
وقتی روغن یک میلیون و هفتصده ، این یک میلیون روغن برای چی میخوان مردم ؟ برای جق جق در خونشون میخوان که بریزن صدا نده ؟
حالا روغن خرید ؛ باهاش چی بخره که چیزی درست کنه ؟
نمیدونم این خدا هم حرف گوش نمیکنه ، من با کسی حرفی ندارم فقط از خدا میخوام به همه کمک کنه
فرقی نمیکنه فقط به ایرانی کمک کنه
به هممون کمک کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68947" target="_blank">📅 21:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68946">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKjhrSQZ2pJLqtoYEJG9PrW5E_BgPfJNPvTeVMEkChgGYUbWLXuzxDB4slCUD2qGc9cwhqFnL0vh6uq8IehWl-dJd056aUI70olto-zEug5nQA72zBq0hITQQzFaxGXduerFSuL_wT7HLwK8W7pq87lEZz2SmP9OKqVUCsgpU84G2dn9-NoLZXugRAwx9FQ73WkHTYeqWxcyrWXRRXFyib0QguIlkac849qlvppjYcA-LUrAWFbZ8rZNn0Q2lqIVXW6by360IX_Gv5-uKiJm7b6yjdogX89L0el9FiVVIPYFPl3DeJ6Zc5FsHXxbSo8BuyuPKT2Gm-O-39DoaHoz4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکبر عبدی، بازیگر سینما و تلویزیون، در سن 66 سالگی درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68946" target="_blank">📅 21:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68945">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKKXOpt1I4ePpDGOT8mSw0jpcLfoy7eMbHuoeoslptf3wUbb37aDQtXuIkqn1s3bSSbNCE9bh2GauAIpGlQs_XlcZl9UoftDspgwuX3lTsyWcBX1SDqCKxkqfEuY5jVQpcRRAigO15V2ocOaBV3_oQiZ4ljQqlvP5iioAcRH1ojwpBUbMXJLlFf8yBd4UuhMTAT-rvcDuNvo3OAP8aNXKLYIhJEoF5rgldAKPxa-mzoOXSmoupH7oqeRgxQzAsQhL6B-tDrA72EQWVVYVer2MboLZXECCnJGWxr1b0tqoCviZymMQ_kep2sOGY-HyxHMsPm4zdT53hoZ5LHa7z4Bmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
علی عبدالهی فرمانده قرارگاه خاتم الانبیا:
از این به بعد به ازای هر شهیدی که از ما بگیرید یدونه امریکایی رو به درک واصل میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68945" target="_blank">📅 20:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68944">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2066d70166.mp4?token=aVS8mcGFWwbDuLN9-8EtkBb143Aa9gnR7s3C-sqrhiKnNCOMnq1NayJ0ExtI-c6Qr_24QFgmJpGekFcxJ7mqG-YhEVuYv2gYE9rgAPsUGemNn8DWouJga9fBhArFvsT10FLjAcyLgxG7nnCNk-h9bWZ46X_JzWmjFhKghJs_Wz8a5oAdD8B5RNFb5TzJB9eLMMtzCuAOPdCzEzUtyquIejnIZHg50j6WZs09vwsOVh1rQjT3_-XUI1TYe0xB_UlSi2og5kIUiCqrzDD9ZBXsyrsxeIzcUk37424xXajEMgDBFRxub4OrUcaqVQODR2MiTlt7GqUjhi_-pjlRN3Foig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2066d70166.mp4?token=aVS8mcGFWwbDuLN9-8EtkBb143Aa9gnR7s3C-sqrhiKnNCOMnq1NayJ0ExtI-c6Qr_24QFgmJpGekFcxJ7mqG-YhEVuYv2gYE9rgAPsUGemNn8DWouJga9fBhArFvsT10FLjAcyLgxG7nnCNk-h9bWZ46X_JzWmjFhKghJs_Wz8a5oAdD8B5RNFb5TzJB9eLMMtzCuAOPdCzEzUtyquIejnIZHg50j6WZs09vwsOVh1rQjT3_-XUI1TYe0xB_UlSi2og5kIUiCqrzDD9ZBXsyrsxeIzcUk37424xXajEMgDBFRxub4OrUcaqVQODR2MiTlt7GqUjhi_-pjlRN3Foig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما از یه بازی فکری رونمایی کرده که توش باید
بچه‌های جزیره اپستین
رو نجات بدی و ببری
بیمارستان خاتم‌الانبیا
😳
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68944" target="_blank">📅 20:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68943">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oquVteX4QXpujY3KHgtmnnQwYAuyCtAM_LlVBOmnn86WyTNyhgxhWFgQKpBMx61A94sQ9_Yn6QI1z9frJnGZ77DVuf9RtBOGP64CEzpWkFgxvHvNSGB2q2k_xGWLHuAp_Bm_XRgPXVCUr5EgfQVyq2T1nLjigoUKDK9onk0-Zm8q2QOOmg3cKvBXBZFk8G6k1c1GgHW45QIyN_qavnhdN1ZVoDT7lQ7BuvGtpMnVi3GQmXLxWuUbULMJnh-cXoa0K90iH_8WubmtzE_-duWJgCyKajbSCGdGITpT5kN8EdzEmOmjT5CF1lWeA7Dw5NyrxLU-IYjzYiOtzJFYNujgDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
رئیس‌جمهور ترامپ:
رئیس‌جمهور شی در دیدار اخیرمان در پکنِ چین، به من گفت که تحت هیچ شرایطی به جمهوری اسلامی ایران سلاح نخواهد داد یا نخواهد فروخت؛ و این گفته شامل شرکت‌های چینی نیز می‌شد. با توجه به روابطمان، من به حرف او اعتماد دارم؛
ضمن اینکه خودم هم لطف‌های بسیار بزرگی در حق او انجام می‌دهم.
به همین ترتیب، رئیس‌جمهور پوتین نیز با وجود جنگ هولناکی که در اوکراین جریان دارد (و روابط همچنان برقرار است، همان‌طور که با رئیس‌جمهور زلنسکی نیز چنین است)، به من گفت که به ایران سلاح نخواهد فروخت.
او درک می‌کند که من به اوکراین سلاح نمی‌فروشم، بلکه به کشورهای عضو ناتو می‌فروشم. آن‌ها بهای کامل را می‌پردازند و من هیچ اطلاعی ندارم که آن سلاح‌ها چگونه توزیع می‌شوند.
بنابراین، به عقیده من، دو کشور عمده‌ای که اغلب در ارتباط با موضوع ایران از آن‌ها نام برده می‌شود، در این کار مشارکت ندارند. اگر چنین می‌کردند، برایشان بسیار بد تمام می‌شد؛ و قطعاً به نفعشان نبود.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68943" target="_blank">📅 19:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68939">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wb9rQSARRipMh4WZyEp5_aN3KkMvJKpU810aCl-PqZ5Yo_lkdR_Tn3OTOkwVKDUX5zheWXe_TiHLlRW1jcABI82f1G57S8-jz49PjIasr3WVYTT2F51HjSmEzmPBgFFAtEtGcwKBPIZPhTg9DuZlFe6dHGX90fDN2DDxz2LbJD_9Luw9sciTgfNeJ3dK6ZwxO9BRQHzZaV5bNRzwMTu_QmJUR9xcelM6iVmJfJE1HxcNWuNX1q-PBbAvvPsO2950naYldTE9FbAem8o5ICBoNlcff6yjAvkXVojXUlvlKMsWabm2sB0xIjL4VkAykl_66s5WrLB5jFzCYf-Oqo0jfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jNDOMwJ9lFw9zS7ZaG6IF4Fsxu5SxLlgJLNJ9U-TOsgyr1uYToBq6sPJQUY45rBx7oFb8pciHNyVb-dhVhpJz7lDx4rmOxSTYzB9UG2HlAeRBteNIheEjH7hNLSKiA7puwqpeW1UEzhjdHg1ScvWz-NpqbjI9gPBNbfXKei35Va07e4BzyTR7MLexWVLdfAzmcpgVjj_PQpHv2FVNb6HYVYlXJSBOmo_J0cJLAKayCdV0ForAXH8uDwSNjE9Eu9Fl3xPrW67dGBOvn1kD00bxke2sqnueMUi2QLrBs3wgCOzoqtE9oyTR1c8gM0psEQB2Ak0nFcjk9PKGrUVL02yuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tebuGcPpIwrredaYChjAE6GhieFncYerV6FfoHeZcQ54t-oiAs34UAPbY9m7wxDlGjRTfEBP20AB6L7E0XH71cOXEOBLCWAI1rZF3ENtpTIUCWfvuVVDYlgw625VOzPVYtP7tLBKRq0bBeSQDhwM-LiyK22D4RL8ijS9XlLkz6Ky2VI2NcNJdM79sGHVPxomKM6MRjyGRhI56b0BHi1tgE2INmv_spJtIzPnTt4pwmimdiu52tiYu9ddK1m8P5wfwhe-UZnVcsdxuoaUnr90vHGn55LM7gAY1kMZoBtO-hGq4aFhj9k4MpE1f878ErbvnUtN_gGLqW2PfzMGHyaHEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=qNoaEmti-kwip7APV7fBc8G1fLg8IJ7nFbMH-iH448Z6-SOfX6yC5kiX_3BEyGr3Q_41316X8OjfvIBrFra62anb67dIFL8H6WCzGzDykHIKPBv562x45qTpuTIjPynn_tsSnvowZXm1-9bq7bREp-MaI9JNJbVXWOlCcB6RJrpgO0EwH-PAd_ZVouM6iZN1n6sL7EI57t9XgTRnwDNxWAesOGYvpdv5Wyi5vvehRle5hdax4OZjUOvvBW5z17qCYNFUVb4apw3PqCMw7th1csEGLtE2_JduLF0NFRXJagtKKC4Q3nTsWlNm0Dij7b6cjgkmWV6pp8-Y5KQM96WioQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=qNoaEmti-kwip7APV7fBc8G1fLg8IJ7nFbMH-iH448Z6-SOfX6yC5kiX_3BEyGr3Q_41316X8OjfvIBrFra62anb67dIFL8H6WCzGzDykHIKPBv562x45qTpuTIjPynn_tsSnvowZXm1-9bq7bREp-MaI9JNJbVXWOlCcB6RJrpgO0EwH-PAd_ZVouM6iZN1n6sL7EI57t9XgTRnwDNxWAesOGYvpdv5Wyi5vvehRle5hdax4OZjUOvvBW5z17qCYNFUVb4apw3PqCMw7th1csEGLtE2_JduLF0NFRXJagtKKC4Q3nTsWlNm0Dij7b6cjgkmWV6pp8-Y5KQM96WioQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ویدیو ای از بمب‌افکن(B-1 Lancer)که گفته میشه در حملات شب های گذشته علیه اهداف نظامی در خاک ایران شرکت داشته.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68939" target="_blank">📅 19:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68938">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecac465f34.mp4?token=pVebhfStDvEYftos66UzI7gOH4RKC_RTJcLIAAsjZEBt-D_Fspv4GhNmevQHxF8oripnrw4LdF2QDSO4gRovhXlE-QJF27Jad1Jom-D7OFCaGmw3_oePOg4QXFQWyPft-y2czt4oOLf9J1O9rMp6jMQ70CO_5mVKNSaJG3-FHa7SFO8M8YnzFSNUMe6vHEzDLFpIfbXOOy0_xTOb-NDQzVYRP1HTvZ8FU-02RAkVrGBKfyQAAZIFFzggfr9LI7YEXp3aSlS5uVhShqSK4zD5dCYu0mzQAr2IqDJtUfLRQVNINfjcv4U3knw6T36Gy7kwDfvi5EXWhYvVP89HY35J3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecac465f34.mp4?token=pVebhfStDvEYftos66UzI7gOH4RKC_RTJcLIAAsjZEBt-D_Fspv4GhNmevQHxF8oripnrw4LdF2QDSO4gRovhXlE-QJF27Jad1Jom-D7OFCaGmw3_oePOg4QXFQWyPft-y2czt4oOLf9J1O9rMp6jMQ70CO_5mVKNSaJG3-FHa7SFO8M8YnzFSNUMe6vHEzDLFpIfbXOOy0_xTOb-NDQzVYRP1HTvZ8FU-02RAkVrGBKfyQAAZIFFzggfr9LI7YEXp3aSlS5uVhShqSK4zD5dCYu0mzQAr2IqDJtUfLRQVNINfjcv4U3knw6T36Gy7kwDfvi5EXWhYvVP89HY35J3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
در هفته‌های اخیر، آشیانه خصوصی وابسته به سپاه در جزیره خارک هدف حمله قرار گرفت. در این حمله، چهار فروند بالگرد آگوستا وستلند AW109E که توسط شرکت خصوصی بالگردی خلیج فارس بهره‌برداری می‌شدند، منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68938" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68937">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpSwOZAC8-MjGSzIX7y4pHWm191QCHqWEB1krVkpakwCzUvFmIN-gV7Tkiw8ypj2WgK61WkC99QgFeDV5VoYEISWw_3pK6GP0Xr5HVVdVSX7fU6YBcdB-YArcIv3URklc27_AAv2Dct2bzR1WubdJTAF7s27NFRrFK7K9-BlxNfjisx5IV6hA1gQS2tRri5NCRYAm300OI6fuoV_sOMFwcPc_IBxsbgvBl9_xnzeYmmCYMMepXnelhyZ7XNK2O7F_xZCuzc8DbSVmyMJXohxVvQkJVPpwAKpueUJUrRNbleck3yrHx6zFYFvzfaF3Bf3h6ySwy1bVPsP0jH9stQiyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رئیس‌جمهور ترامپ روز سه‌شنبه در کاخ سفید با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68937" target="_blank">📅 17:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68936">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/887792c366.mp4?token=QMYUV3BGgbtA9C-3psh-cVcyh6ft1zJuuGsHOOsmn9Yx9NOC0CkTIpKhLEoDk2PFYq4bjERit_BjTrjhgemr3i1Ye5UbxFkc75_uS_euKzHjeOLr4wXOfTGWEhZmkhdFnI8dhZwUbqhfBwwiKX-C3ujA37c6TiKr1b8SHsagLrxMAYEaXoL1tg2lTboR86vi0H75sUQjWGHoWEfNIv2d0oZ5LXkD7l0wXWFgde7FlQJ7cCBUSSsX3yBScNeg6BKrk4ZdEEPfkurPslm1FbKamfOCg2Jp90Nq8MkOEy3JdZitN-Ji7DX_Gh82EqwWjr-T-T6_lknckT_PJqTIaX_6fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/887792c366.mp4?token=QMYUV3BGgbtA9C-3psh-cVcyh6ft1zJuuGsHOOsmn9Yx9NOC0CkTIpKhLEoDk2PFYq4bjERit_BjTrjhgemr3i1Ye5UbxFkc75_uS_euKzHjeOLr4wXOfTGWEhZmkhdFnI8dhZwUbqhfBwwiKX-C3ujA37c6TiKr1b8SHsagLrxMAYEaXoL1tg2lTboR86vi0H75sUQjWGHoWEfNIv2d0oZ5LXkD7l0wXWFgde7FlQJ7cCBUSSsX3yBScNeg6BKrk4ZdEEPfkurPslm1FbKamfOCg2Jp90Nq8MkOEy3JdZitN-Ji7DX_Gh82EqwWjr-T-T6_lknckT_PJqTIaX_6fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
❌
👑
مقایسه تسلط زبان خارجه:
وزیر امور خارجه کنونی دارای دکتری علوم سیاسی از انگلیس
با
نخست وزیر ۵۰ سال قبل ایران دارای مدرک کارشناسی علوم سیاسی از بلژیک
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68936" target="_blank">📅 17:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68935">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=RdUoaQWaQNPldViIX_T7TPDkvLmBN-PD4nuXleVjTKhhtM0_LHHBE7kcAXeWp5g9qbl6iEHqdvEhBMz1bDZUFQc-_J9eP4r02zEREIEIHa8GsPPH5l3DXpHAZXaKNdOpf6ut3CpcBNaIiv8dLQO0b9AgDkiURSB-zBiDjGrGjcI-91I-nJ5-pLmygjZuf2gZFnu7lL9HQp38hxa4RJmrKp3qe7sLwJdWXcJ-0dFqYTxH862QbudozELDQCF41FrJiYYnXkVuz55UmR8tgHx2BCYsNXiP7EkZnbc5ghmGQftBOo_HkdBLC1jyN1kPp9TIr_JWzSd1q7cGL1Q_Gee1LJvuUzdqZJ9yo-I1FTobPe9kVh2ImUJ5Br7U8V8qrFD5dsMG4RdMnYC6hA0SLd1JWttyfpM4YibWGL54HeWIPZ_BjNSDd3R1nTSXCiOKWm1Qt8wAaOA10406KGo7MZT6uqb7pIC8y4KLfOisop4xLTUunuPEIUucGQLFy4N3Hy9C3fAZ7mM5KADcSEOkyl_9kl-KtHc6uYLe8KQeKxco6OVi6YrlKWuKobeNXmnya7EKAmTWFeuCIcIBxBlA8v8Vx_m1NQz5cK241I1xGql1JWzTx_Kx1ZA4HDJ69qczKqBFf9ZRbbtQ2xYYein9wi4dsYVUg3d96Kgdt7YGsYEB5J8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=RdUoaQWaQNPldViIX_T7TPDkvLmBN-PD4nuXleVjTKhhtM0_LHHBE7kcAXeWp5g9qbl6iEHqdvEhBMz1bDZUFQc-_J9eP4r02zEREIEIHa8GsPPH5l3DXpHAZXaKNdOpf6ut3CpcBNaIiv8dLQO0b9AgDkiURSB-zBiDjGrGjcI-91I-nJ5-pLmygjZuf2gZFnu7lL9HQp38hxa4RJmrKp3qe7sLwJdWXcJ-0dFqYTxH862QbudozELDQCF41FrJiYYnXkVuz55UmR8tgHx2BCYsNXiP7EkZnbc5ghmGQftBOo_HkdBLC1jyN1kPp9TIr_JWzSd1q7cGL1Q_Gee1LJvuUzdqZJ9yo-I1FTobPe9kVh2ImUJ5Br7U8V8qrFD5dsMG4RdMnYC6hA0SLd1JWttyfpM4YibWGL54HeWIPZ_BjNSDd3R1nTSXCiOKWm1Qt8wAaOA10406KGo7MZT6uqb7pIC8y4KLfOisop4xLTUunuPEIUucGQLFy4N3Hy9C3fAZ7mM5KADcSEOkyl_9kl-KtHc6uYLe8KQeKxco6OVi6YrlKWuKobeNXmnya7EKAmTWFeuCIcIBxBlA8v8Vx_m1NQz5cK241I1xGql1JWzTx_Kx1ZA4HDJ69qczKqBFf9ZRbbtQ2xYYein9wi4dsYVUg3d96Kgdt7YGsYEB5J8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عباس:
چهل روز جنگ و محاصره بود هیچ کالایی کم نیومد
بله قیمت ها یکم افزایش پیدا کرد که طبیعیه
یکی از مهمون های عالی رتبه ما اومد ایران و تهران گفت من وقتی شهر دیدم تعجب کردم
گفتم این همون شهریه که جنگیده و محاصره کشیده ؟ من فک کردم الان بیام تهران شهر مفلوکیه
همه دنیا داره به ما احترام میزاره جز خودمون
من رفتم عراق حرم اونجا استقبالی که عراقی ها ازم کردن عجیب غریب بود اونم ساعت 2 شب
این استقبال از من نبود از وزیر خارجه جمهوری اسلامی اونا به من میگفتن قهرمان
عراقی ها این همه شور و شوق داشتن اونوقت صداسیما یدونشم پخش نکرد
یه نفرم اون وسط تو حرم گفت مرگ بر سازشگر
با مرگ بر عراقچی مگه مشکل حل میشه ؟ من اگه وزیرخارجه نبودم باور کن پشت لانچر بودم الان.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68935" target="_blank">📅 16:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68934">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🇮🇷
تسنیم:
حمله پهپادی به مخازن لجستیکی ارتش آمریکا در صحرای عربستان.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68934" target="_blank">📅 16:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68933">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUjU2sky-7IcWS5N9towGF3JT5EmM7zpYNtmmOcrgFGAichb4yzv5SBjtP9bRJyuAXmBJzs0DOq8rFJQAvJXRzSdPZANfw_IQIRpjNpN61i9aQRFXqM5qLx4tAqibeqdWAh-0hBDvbndyNNRjrJ4ZTcAPkWjZTXQXeh9nU_SGkV8lUnu9497r-NURdJMnkv4cYI8nefDTerShiQkY41xMse9r0AG45QqQOdwUytB2b6upx3nuEOJJ6NHCvP8_t3hcDJBXh7hwCKK5gnuw0wCpp9xB31Mnwk7FAEY0SnKRV-9oLZmzF3zrSnfF4W7ER4dLZDOfUjJ3BXDFv4OBKz3WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
توییت حساب وزارت خارجه آمریکا؛ سیاست رئیس جمهور‌ ما:
یک سر در برابر هر چشم!
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68933" target="_blank">📅 15:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68932">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipSIbUnOZs5e22TGqygmblDhU8Ch-dp7Pzjs0dVE8F5UAxkpi0j0dL38NqpGG3lKsEarGfvK_xHl_EJU5GaWNQPAh2AFoUpYw-l01yLNQpNbdYpOVMAAs0p1w-3OwtGW3QVDxauKQfjlJBMprt4wqffxRy6GwxKcVSl8GKMwefpoEX65ORuWLfbGpFWOjcnsAaek-clv7fwxKtQdFzdcT6J_hlSXSRQakmVaMIbueGvwFAUgcNlpzNNM6yemfc6F4Qb3oD6zJ9D8EPhz10WXDO6lc9VE53O4E4lDWyXL2x3UNviTgy2zwywizsURdR0j3ry8BCW9HApctd94bOv5uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
وزارت امور خارجه آلمان اعلام کرد که این کشور فعالیت‌های سفارت خود در تهران را کاهش داده و بار دیگر از شهروندانش خواسته است که هرچه سریعتر ایران را ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68932" target="_blank">📅 15:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68930">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L3a0aoToLUkG2PmOmWlb3Mn0sxek9YcKECR2IMg2hc_FLXI7-WiMT_4dAsVXvWb--hBaZJQoUpR_oSh4XbrbXTZrb7znXOrDNEoZQCbM7sf5-UPZxc2t-cyc1w4KX-RSzntQFIu00Fp4otOMcx7wSL5FQjwJOfnx0tZ1zAgKsQSGGCLhAOPDyfdmY6nzCuu1L0ZHiwI8vAK35mLztlbeYmyqWerqkJ1ikWETcuahRuZxMx5rJ-Tuyqwlll7IvzZMkiCymVA4nsMRWto2lYSUZZo214c9sfngeuPyecEd9rCnDg6NVkyfb9mi3vToP7DgNwUllJqNZ-WRYoBeby1TEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pTbQr-A8mwaXrtTYuEvxWm3rKF6FUEPDL5sHflY5AyHNTZLPuk0n5IjKXI_gzL69Gr6ESL1pTgPiCMS5mYddQXe4gTfzsQhy8MPwi-uJmYP7rhv6_DlWs-3yL9lJEg5tZd4nZS-ipy3iuRPX727dh82baUFnNLWpjZUCepqraxLWxJrPScogH3cXl36WQSPkIq1zedfD8z1MHAynfanzfDSh6J3uyeR4oX3zJtABX-U91oivYajVHCr67NqiCMyCcdjqep6ICJvshwJdVP1gprmcUswOOh3cjjcvozpd7OvVphmW1vrTyY5qGimeFCLdn1GmrWulw7w0gim3Sqp5xA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
تعدادی از هواپیماهای تانکر سوخت‌رسان آمریکایی به پایگاه هوایی شاهزاده سلطان در عربستان سعودی رسیدند، این هواپیماها از آمریکا به این کشور آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68930" target="_blank">📅 14:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68929">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=OE38z4Yu6zGNvVvQW2d4RAglQWjagJCjPmeSFY8mrTOLAqKN3LNVYM_0oreQbmiOgnBZLNk35oyBlVOmB63NjLSFN8B7ojtDgY_fLhULTdTqP4JDbvTtFoiMkIa25sxGMiNZcBWd9kpju1Lxdo-pQWBrpuvNgYhz88qMdpqjEZny2dfqxQvcR9YOu31u6uquxmuMD1GblQFNOxVUhuLW-1NcgsOesTZTMPn5tnkM5FqkOLXt6ngCWU79VoOtzvtLuQTMCMa1RDIByzpZwwCpNUdXazuYgT-F6wcSlfpbLatq1LG0UWufzPYdyQ2kI_MTyKBimR3Kr58I11CBEPHgnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=OE38z4Yu6zGNvVvQW2d4RAglQWjagJCjPmeSFY8mrTOLAqKN3LNVYM_0oreQbmiOgnBZLNk35oyBlVOmB63NjLSFN8B7ojtDgY_fLhULTdTqP4JDbvTtFoiMkIa25sxGMiNZcBWd9kpju1Lxdo-pQWBrpuvNgYhz88qMdpqjEZny2dfqxQvcR9YOu31u6uquxmuMD1GblQFNOxVUhuLW-1NcgsOesTZTMPn5tnkM5FqkOLXt6ngCWU79VoOtzvtLuQTMCMa1RDIByzpZwwCpNUdXazuYgT-F6wcSlfpbLatq1LG0UWufzPYdyQ2kI_MTyKBimR3Kr58I11CBEPHgnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عراقچی:
کتاب نوشتم، «قدرت مذاکره». نتیجه‌اش هم داریم می‌بینیم.
همین دیشب یکی از وزرای خارجه آفریقایی به من زنگ زد و گفت میخواهیم دیپلمات‌های مان را بفرستیم ایران، برای آموزش!
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68929" target="_blank">📅 14:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68928">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
«به اطلاع عموم مردم کشورهایی که پرسنل نظامی امریکا در آنجا حضور دارند، می‌رسانیم که برای حفظ امنیت خود، باید فوراً از مناطق واقع در شعاع 500 متری از محل‌های هم اشکار و هم مخفی حضور پرسنل نظامی ایالات متحده، دور شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68928" target="_blank">📅 13:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68927">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6vkO85YE__IqsXUjgPN4NW4vyYc98QpF1_IQOuEWDEVgwwEtV-Go-ZfyY_-ShbzwxceJiO8bh153e_Bj6oTvDUgZ8gETkeLwSreU6sBBXaj16gi90pMn1XXQw-9jNFtK8eXM5JDgP5AQMumzOKBF33hY1nu4uB9U5EI-y7BODVCCmdKriZ8W4qzdoUQ3yQnRuwttiBbZMzkc9HmLCR8bD5kULrJAXnVDYUT-sY0nh9YSDowViW0Lh2guEwwhM4qbClc8ADaflm69TB8TuR6xiYfqZhU0JBqDflL_GgiN1f8bQUjoPklJ7MegnGNWljYgrI8OZPu-r8vxn-LYSe38g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مناطق هدف قرار گرفته در خاک ایران طی حملات شب گذشته امریکا
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68927" target="_blank">📅 13:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68926">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpBGrAUCe0LdE98V0w3jEVe16QXbDo-_XBLDiwBhU5Ejg0ubqElGv93nJUpdl7Rv_Mn2ENY-3qVMDWoN25gCXqiB1Qzbv1H8l8ndid5x8wZfyAZMjHPyJN2Xj_NQceHbJPDnBSBa5GoGb5ZXal8A2X5S8Qm043fSFnjMMKgAFmDL8EUg4IYNE6wfRrNRXg2sYgEQP6lKGvCBXC5AgGvpRppCfRRkdgVXKSV1SkpkRHTybJNexi_hrx73jYL4xN5pluEt3_PVaO1FI4vIR529Kx6hoRAPosbOkz1rmPnGzK1S2nuC-xFqD23_qHsskYqbeB3SNlp1g9nGMrMJiVZ0HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
جیک تورکس خبرنگار یهودی کاخ سفید:
نمی‌دانم چطور بگویم، اما من در خودِ «کاخ سفید» کار می‌کنم. از اطلاعاتی آگاهم که افراد زیادی به آن دسترسی ندارند و با اطمینان کامل به شما می‌گویم که آمریکا برنامه‌ای برای شکست دادن رژیم ایران دارد.
آن «کارشناسان» حسابی غافلگیر خواهند شد؛ هرچند بعدش وانمود می‌کنند که از همان اول هم می‌دانستند، پس... بگذریم.
به هر حال، خواهیم دید چه میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68926" target="_blank">📅 12:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68925">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/899def3cc4.mp4?token=iA4loQmQlu5OtcCuabV2z9BqBEIcxwry-OGHdB-9SQpB_QjiNNQJ9KwkKiVSqKFfisrKgzhszMpyXFl_90lmwcURXrNJcxpMJCnT7TAvlD7MCXu8m2ypl7rnMZTyWmkia7_2msHQIqWZUUqxHwPqWOtrLdGiY7VduW5EKKWYkHX62wu7tyLHJGq1cIVavDSMXM0Zj9ayF7hbHIpw4SEqKCzigK_Lp1PzXq_ToYLiXSXjPmAsxdOMg2G3e0VGAXfUvOYqPsk2V7lkLMs_q5qbyO24gCCYhCeNiO0C6fFjZd6TDQWgsgWMMqcNIaIWy495yg1FVtN6GjHRTuvlHvhIkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/899def3cc4.mp4?token=iA4loQmQlu5OtcCuabV2z9BqBEIcxwry-OGHdB-9SQpB_QjiNNQJ9KwkKiVSqKFfisrKgzhszMpyXFl_90lmwcURXrNJcxpMJCnT7TAvlD7MCXu8m2ypl7rnMZTyWmkia7_2msHQIqWZUUqxHwPqWOtrLdGiY7VduW5EKKWYkHX62wu7tyLHJGq1cIVavDSMXM0Zj9ayF7hbHIpw4SEqKCzigK_Lp1PzXq_ToYLiXSXjPmAsxdOMg2G3e0VGAXfUvOYqPsk2V7lkLMs_q5qbyO24gCCYhCeNiO0C6fFjZd6TDQWgsgWMMqcNIaIWy495yg1FVtN6GjHRTuvlHvhIkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حملات ایالات متحده به ایران برای سیزدهمین شب متوالی ادامه یافت.
در این حملات، محل‌های گزارش‌شده‌ای از موشک‌ها در یزد، انبارهای سلاح در اهواز و چندین نقطه دیگر در مناطق جنوب و غرب ایران مورد هدف قرار گرفتند.
در پاسخ به این حملات، ایران صبح امروز چندین موشک را به سمت اردن، بحرین و منطقه اربیل در کردستان عراق شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68925" target="_blank">📅 11:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68924">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9dc866f375.mp4?token=V3f2Z2jngVc-RpTAY_iN98Mx6B0iR5RcgolnlqT-xcS6-vVO7ly1sA5A0MVxQK5ygFQ1ku7e724wSHc1_6IsU5xlyZ0qxpkCaydXIh79K7MueXRFF4LnaoBKrqjnkRLqczrEdnZRLdLs4r9YJPF-8Tq3auiI-0R_VEfF3KtgKKDplWdsPxbqAXMm6NoXloPq7GKyAq1QVtotBWV8-VeS-03DojLdbtciweF1o6DjDMnBG9mn6JyTYcwg12Gj4VN4DH8ZqYMQREIu7VNYlQ3zq81xAqJsIrH7-gmQ-vginEPb2n-wzOHh8_T6qSCocJh80m_Ry2erxERpIA7Tr3Ls0A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9dc866f375.mp4?token=V3f2Z2jngVc-RpTAY_iN98Mx6B0iR5RcgolnlqT-xcS6-vVO7ly1sA5A0MVxQK5ygFQ1ku7e724wSHc1_6IsU5xlyZ0qxpkCaydXIh79K7MueXRFF4LnaoBKrqjnkRLqczrEdnZRLdLs4r9YJPF-8Tq3auiI-0R_VEfF3KtgKKDplWdsPxbqAXMm6NoXloPq7GKyAq1QVtotBWV8-VeS-03DojLdbtciweF1o6DjDMnBG9mn6JyTYcwg12Gj4VN4DH8ZqYMQREIu7VNYlQ3zq81xAqJsIrH7-gmQ-vginEPb2n-wzOHh8_T6qSCocJh80m_Ry2erxERpIA7Tr3Ls0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر به اسم ناصر نوری گوشت سگ به مردم می‌فروخته!حالا مردم متوجه شدن و مجبورش کردن خودش بشینه تمام گوشت سگ‌هایی که داشته رو بخوره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/68924" target="_blank">📅 11:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68923">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=NXXdvCGgyTYxfTI0zuqyWIOHr41N6t4nmaYDMDCAGX5rT5Ruw0yIIREVqVEyj8qevWUJdKVH3rek3LI3Le0pRRxBXKno0avH7YWHMKNQZ_gOegK1H3YinvswQkt-tjG3OAQEn5smXIyZdKCiggMDib91hW0iMO__ny63x5EuaQG0xZnGE0ma_PxDOSXTx5LV96KjHlr4eLUVgrRrPIjYbVSgq9gFBj6RNKbTqzJ13OzSoffBN9PnEDDUOZ6uneOEjTIqnkDxhGbmHXvX7hU8VCfqcIOLqyZt-lOhJ12C1h8NO3HsP8CKPkBzu7kFuVWKn4Qr5ABOp6t_HXBHnoMAsjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=NXXdvCGgyTYxfTI0zuqyWIOHr41N6t4nmaYDMDCAGX5rT5Ruw0yIIREVqVEyj8qevWUJdKVH3rek3LI3Le0pRRxBXKno0avH7YWHMKNQZ_gOegK1H3YinvswQkt-tjG3OAQEn5smXIyZdKCiggMDib91hW0iMO__ny63x5EuaQG0xZnGE0ma_PxDOSXTx5LV96KjHlr4eLUVgrRrPIjYbVSgq9gFBj6RNKbTqzJ13OzSoffBN9PnEDDUOZ6uneOEjTIqnkDxhGbmHXvX7hU8VCfqcIOLqyZt-lOhJ12C1h8NO3HsP8CKPkBzu7kFuVWKn4Qr5ABOp6t_HXBHnoMAsjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخش هایی از سخنرانی ترامپ درباره ایران زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68923" target="_blank">📅 10:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68922">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=eyOQFChlQmeMvcFLcRyyEAp2zsjyiPg_vV9Fxpj9IIW8wnRHxkO602kGFstGjqPgKvXBAqcQg9SLrRg0GbMUS2hm7qVGn9RGlhfwzDHDDYx1aKZc0XUe1cnXEmd9y3fUCHF8uEgs0eecAZOso0OMBDK4gl9X7qyjKv57E_CL26sSMTzP-BxGTRcweqqQpygQVzFMANs9JTOePXA4jRnK7txcNkKpEEjEs6xmNCkPjoyfGZA5XX1ek-jr4JEj1U6zEuVniK97o4nH6t2I8lOX3SbhdY9q6jI3JZiC3y1LhyAKFrtXTz6z65HqNsDEg96OjrcnJqsfUFLt2pHsF-E85w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=eyOQFChlQmeMvcFLcRyyEAp2zsjyiPg_vV9Fxpj9IIW8wnRHxkO602kGFstGjqPgKvXBAqcQg9SLrRg0GbMUS2hm7qVGn9RGlhfwzDHDDYx1aKZc0XUe1cnXEmd9y3fUCHF8uEgs0eecAZOso0OMBDK4gl9X7qyjKv57E_CL26sSMTzP-BxGTRcweqqQpygQVzFMANs9JTOePXA4jRnK7txcNkKpEEjEs6xmNCkPjoyfGZA5XX1ek-jr4JEj1U6zEuVniK97o4nH6t2I8lOX3SbhdY9q6jI3JZiC3y1LhyAKFrtXTz6z65HqNsDEg96OjrcnJqsfUFLt2pHsF-E85w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
شهریاری به ثابتی:
تنگه رو بدیم بررررره؟؟؟ مگه مال ننت بوده که بدیم بره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68922" target="_blank">📅 10:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68921">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=WU-OvaH7ew4hgtA_NJc3-Pzy7SaxhQBquGz_7ubH_0kBWHzlncLYmp4iGzmXnJHiLOE3dUCVd8zCcF9Oux7SaluiKqnJrvdFuiiRExgO30Wpezj1gRqDA5mKEyUTufTjAvOonxM6ijg36CQtZZmxcOSr-_5lUvlXuZDtQZIWcM6MtDa2p9dT2UJ6EWoJqgQTGPRCC63xE8lfU0sCpOkdjJZEexrUpBuXLpQmtMHxzVaSP0I1o9MysJvj9Q9eq0eS5em45w9KjsVG0X9UA-tTz4CpnpuSmy7QqX-SDrP5m2sop3FHDWyn_sa3t-Qcf3QSbIcnEi6mYr4STHFjXW2mFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=WU-OvaH7ew4hgtA_NJc3-Pzy7SaxhQBquGz_7ubH_0kBWHzlncLYmp4iGzmXnJHiLOE3dUCVd8zCcF9Oux7SaluiKqnJrvdFuiiRExgO30Wpezj1gRqDA5mKEyUTufTjAvOonxM6ijg36CQtZZmxcOSr-_5lUvlXuZDtQZIWcM6MtDa2p9dT2UJ6EWoJqgQTGPRCC63xE8lfU0sCpOkdjJZEexrUpBuXLpQmtMHxzVaSP0I1o9MysJvj9Q9eq0eS5em45w9KjsVG0X9UA-tTz4CpnpuSmy7QqX-SDrP5m2sop3FHDWyn_sa3t-Qcf3QSbIcnEi6mYr4STHFjXW2mFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
جواد اوجی وزیر نفت دولت رئیسی:
ما ۱۰ خط لوله بزرگ و سراسری گاز داریم. در بهمن سال ۱۴۰۲، یک شب ساعت ۱ بود که موساد روی خط تلفن بنده آمد و گفت امشب می‌خواهیم آتش بازی کنیم‌.
از من پرسید فلانی ۳+۵ چند می‌شود؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز را زدیم. ۵ دقیقه بعد دوستان از دیسپاچینگ گاز به بنده زنگ زدند و همین خبر را تایید کردند.
تا لباس بپوشم، موساد دوباره زنگ زد و از من پرسید ۴+۵ چند می‌شود؟ من گفتم ۹، گفت خط نهم سراسری گاز را هم منفجر کردیم. سومین خط را هم زدند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68921" target="_blank">📅 09:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68920">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
انفجار شدید در مراغه
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68920" target="_blank">📅 04:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68919">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران  @News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68919" target="_blank">📅 04:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68918">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88c72c3752.mp4?token=QwWUR0AbER44P69FyOgA8TJyKv-3zRw3b_OloAxlO8ji-lM0bUiDwkeQ0tz3p7sS7JyvpXoFpw9w0UBy2eF1SoGVmbgue6puhfSa8ipIN00CIBNwOPk7iWlx2ysf1n_1d_mNgUqZtUCmifDfB_SLvEZz5C-WlaVckvAJEFRE_wKLWzI84RhZ1ZBPdlIE4hYqSlJr31l5njKie0kqonwWDG1LV6qQALgsv_1DOvhKuwSaw9n0RZ780R5jq45nSiTdxXW7VvpDmDzuh5LryckTWAkTzOTGqGzHShoaA1CYFSbOZS05qK68icQR9LUvANOQTmrFOVHMPIqKAwMv76oZDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88c72c3752.mp4?token=QwWUR0AbER44P69FyOgA8TJyKv-3zRw3b_OloAxlO8ji-lM0bUiDwkeQ0tz3p7sS7JyvpXoFpw9w0UBy2eF1SoGVmbgue6puhfSa8ipIN00CIBNwOPk7iWlx2ysf1n_1d_mNgUqZtUCmifDfB_SLvEZz5C-WlaVckvAJEFRE_wKLWzI84RhZ1ZBPdlIE4hYqSlJr31l5njKie0kqonwWDG1LV6qQALgsv_1DOvhKuwSaw9n0RZ780R5jq45nSiTdxXW7VvpDmDzuh5LryckTWAkTzOTGqGzHShoaA1CYFSbOZS05qK68icQR9LUvANOQTmrFOVHMPIqKAwMv76oZDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68918" target="_blank">📅 04:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68917">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">سرعتی.npvt</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68917" target="_blank">📅 04:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68916">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMA2DbWNjZrP0EfoMF-GK53L1SNJ2lLqvpJNkqiZKV2nNeMAoMtpLi69WjkNVeZlZ5HuizxGUufGU0Rienox9K2sg2D2p1Ac00-bEl49qqe-Kcx3STN_OvEaCsGj0h2kUpgCZCcpfNHhWVSpGbWN-h9lzCBU9bLo9d3M9Lm2Ll-4FWkBy46SS6YLh5otgxKmwvxKnheSfkW9bS2_YfBgQn-TEgKZumP--QFkb32Cwhpcq-lzJwkBm2f7Jd-NhVjtEdydxIu6JNPNdzKIfwanplcq675XBoS26bIl47gwRQWE9RsIqNqBSP2ylzVROQq25g-C_FzC-_P0IqnwNl26zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ پدافند تهران به دلیل حضور پهپاد های شناسایی آمریکایی ها فعال شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68916" target="_blank">📅 04:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68915">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcTKSmLyOxJv9_yhnnB2vj5dERLr-GgL3uz7roECA1ujtrXVx7z3G5_voM3-cVCObfTl19uHV1EC8bm5l3HCQgVFQFRejhTRWi8cf6flcWsuJU3ntgl2cBFcKNeQjCQ1EG8rewCJtMbUG_pP6M_iBcigkLFLbecRwVuJ88ATWwgG6UewcYEsBYcH3JV_WLruvdst4Q_zlYEzfCRrYCrNB3cs5Khd31wnUehK0qAddovygKogB7nkooT77mHkb1Y_3h67loCOZzZJa9JB-ykiNNsOi7SSJv6hsDCWdE9gr7d026HtmQAQUHdsyb3BR3noyRx0FUhErRBH6HaEebVbGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68915" target="_blank">📅 03:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68914">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
برق مناطقی از بندرعباس قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68914" target="_blank">📅 03:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68913">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Khn1wlmyGIMuCZUw5G0XynfLNqUP313Ebb5bYLg89mYV5PCIcGdxpDx1AOPSxf0N6Iy7uhtD2g_Ksz2aItKx3xvxfd357GnZxdi7_kmTwcIjzDI2py3_hEGdcVY4j2oKzJNokEQceLmA8hMm_98vbsgFE-CCjrllXvDVNXyNDztAYQ-uPz6JygfbshGJt3_S7uOqIjRWrYcVM587-OSnCFj-kxQWO1hJ5enCCeozHUsBzvnxbIgV3u_aFxTyhImLZG1WfpIkgopZPDHamAc_2GvLeIWOstGSdwB9mrbPDNtOaEYAF3iWxb-N2ptpAkARe-4pPq8TanbaUwNj5_W_sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بندرعباس؛ امشب  @News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68913" target="_blank">📅 03:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68912">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🇺🇸
منابع آمریکایی: ترامپ در حال بررسی امکان بازگشت به سطح حملات مشابه ابتدای جنگ است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68912" target="_blank">📅 03:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68911">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37ca8b5fd7.mp4?token=gjjWQnqjc74UcDHXCs5bUqwrQ8ME2N_RM8fvrfxH5Vgs37qztweOdbok-YZIizVHQJkuQi_fv76YSbhxnOfpyZxu--cnsq1Xgt8E5IQMmTzk3PRwfWUM5RA_tFuh8H2Eem7NoA1FoIYndvymEG06LFKvFsIOoebSm4ZEbacna1FHJSUDG4LxVzxVi1Jr2s0r0bkX_CtdG1v2h_SXGFgw3du51dywhDQjG9h85jxcna5QQokO4fdWHJzqpJk-RzDIurVldTlQaYaHSGUTJtKDlC52AC-ZwDYDecArw4_DvKyI3OTO4T8CblfWYXKT8-hVvqfNqkmJflrDj5xOG0GW8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37ca8b5fd7.mp4?token=gjjWQnqjc74UcDHXCs5bUqwrQ8ME2N_RM8fvrfxH5Vgs37qztweOdbok-YZIizVHQJkuQi_fv76YSbhxnOfpyZxu--cnsq1Xgt8E5IQMmTzk3PRwfWUM5RA_tFuh8H2Eem7NoA1FoIYndvymEG06LFKvFsIOoebSm4ZEbacna1FHJSUDG4LxVzxVi1Jr2s0r0bkX_CtdG1v2h_SXGFgw3du51dywhDQjG9h85jxcna5QQokO4fdWHJzqpJk-RzDIurVldTlQaYaHSGUTJtKDlC52AC-ZwDYDecArw4_DvKyI3OTO4T8CblfWYXKT8-hVvqfNqkmJflrDj5xOG0GW8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بندرعباس؛ امشب
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68911" target="_blank">📅 03:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68910">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
دقایقی پیش صدای انفجارهایی در قشم امیدیه و اندیمشک شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68910" target="_blank">📅 03:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68909">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=sGxPaKsHYUxFWH0CFbI9xhWfQr1vXLlLA4Bp10joAU_ul9OEnvXYH9vn4OgAR6eseC1SajL8iGn3RdFe2edjOVNSVJxDLhwC1H09k7z2LZBpzZ3t9ULmrwXOIoYifPF9GB0CyUYaOwGxImXHW81QI_SuE7EPuxg-0R1JTx5mvUnep2cUMWbTBGyEjPifHBiZQWYlFMz0IAh74WpMHF5OSGWMo2gGi8H3HC2l3YUP_yl7cVEAhBuWHb7CGWsXKyV-NHrsaXK-F6pnE02_UL2ABQ0SObj20YA1xZU2rg7NPFW-BWtLyXT-mFpQsKXYgAqONuZXIaK-v7Tpru4fwZvaYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=sGxPaKsHYUxFWH0CFbI9xhWfQr1vXLlLA4Bp10joAU_ul9OEnvXYH9vn4OgAR6eseC1SajL8iGn3RdFe2edjOVNSVJxDLhwC1H09k7z2LZBpzZ3t9ULmrwXOIoYifPF9GB0CyUYaOwGxImXHW81QI_SuE7EPuxg-0R1JTx5mvUnep2cUMWbTBGyEjPifHBiZQWYlFMz0IAh74WpMHF5OSGWMo2gGi8H3HC2l3YUP_yl7cVEAhBuWHb7CGWsXKyV-NHrsaXK-F6pnE02_UL2ABQ0SObj20YA1xZU2rg7NPFW-BWtLyXT-mFpQsKXYgAqONuZXIaK-v7Tpru4fwZvaYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
منتسب به حملات سنگین آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68909" target="_blank">📅 03:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68908">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28e6ff0ec3.mp4?token=bxbhTn5EMQeYHIaNP-v1wlGcCF6a2gccEOH14qBtFPKohsmMoZoJOWUfJjN6y8bawoTYRDtGaRcjuukGRx5NBc3p_Z6YNnPRgmPDEA7rC2ON3lUEhR7NEfzv0VpWiqSYx6bjWTjFa3gtrGvuCgkpU_pzsIY2PuMnRHycWdhqlsE5o1XXJ5216jQaKrYMaLfpE2PGCD1ihFhd2DRIpyJVm5QJYi7mPDakW3BqBfXVwD57vpNNvrCBidEBns_S7WURa0EjfW9LL_v2rGUyJs451nEpUfkziE5US6jSEwO845y-aWgP02WZFFutcQ0J_9GPHshHTXimFbhZr7deh5YKPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28e6ff0ec3.mp4?token=bxbhTn5EMQeYHIaNP-v1wlGcCF6a2gccEOH14qBtFPKohsmMoZoJOWUfJjN6y8bawoTYRDtGaRcjuukGRx5NBc3p_Z6YNnPRgmPDEA7rC2ON3lUEhR7NEfzv0VpWiqSYx6bjWTjFa3gtrGvuCgkpU_pzsIY2PuMnRHycWdhqlsE5o1XXJ5216jQaKrYMaLfpE2PGCD1ihFhd2DRIpyJVm5QJYi7mPDakW3BqBfXVwD57vpNNvrCBidEBns_S7WURa0EjfW9LL_v2rGUyJs451nEpUfkziE5US6jSEwO845y-aWgP02WZFFutcQ0J_9GPHshHTXimFbhZr7deh5YKPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
لحظه وقوع انفجارها در تپه الله اکبردر بندرعباس، دقایقی پیش.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68908" target="_blank">📅 03:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68907">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFD3SIF8y-EzLpTKiovbg4p3I8uI38kU_5ZsXuOR2zF8ue3FW9M6Unrd_yKoyiq2rfccQAyJszsZWkcz0mxIK04G2MTzdCSsyO5wz-plUgGOWSStz3-OocIHr4FKsAC8OHQlNqz1wXJlqPwPs2DV0kvv0XrFYoTZgtHOnQ_XnvSYD8JMVeNtORF6lxEiengcQ2GIJqwKAEMlZHm25mIVCOesGMK0IE_rluo5PUc3AD9vP1MPIkyVlIyY5ET-CrsFYNeWatUCt-R8NhVY-8dADLURQYLg6_ZlSQNg2DzyTwIEqgl4h29ojPJsuVXUq7MlR2mGnJeroJrW7TsCSKj8TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68907" target="_blank">📅 03:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68906">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
بمباران پشم‌ریزون اهواز توسط بمب‌افکن‌های آمریکایی  @News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68906" target="_blank">📅 02:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68905">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114f82e10d.mp4?token=neu1S7r2eR26QNn4wIzsrvfMBKeHhCp_vHGoMMouscX32tPxeAs_ch7enBklNMKjHEuIFz2a3EzWuEEvdp8wNdqiWLPyhBSR-rXLO7IPqZ69KQHMll5tqepUaX5UyDO3VlYn0OI8FRQ3OrXlFa1IFctpvh2MaqAr2GK7Jvm5G44AHrv7FPD4lTpz93BqibJBjDkW_EO8SlLxa59UNXlZ4sjAfkt5TARyscGG9bF-_tZjO1B_ACIPqpJdTNRqV-RHPRADrS3lEI5QIWyssWGt4wdmUS89FCjGlsYvzXF03iH_hXL7PYCDK0vxOLZomxP0m1KkjMnJWE9yoI4vBVlELw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114f82e10d.mp4?token=neu1S7r2eR26QNn4wIzsrvfMBKeHhCp_vHGoMMouscX32tPxeAs_ch7enBklNMKjHEuIFz2a3EzWuEEvdp8wNdqiWLPyhBSR-rXLO7IPqZ69KQHMll5tqepUaX5UyDO3VlYn0OI8FRQ3OrXlFa1IFctpvh2MaqAr2GK7Jvm5G44AHrv7FPD4lTpz93BqibJBjDkW_EO8SlLxa59UNXlZ4sjAfkt5TARyscGG9bF-_tZjO1B_ACIPqpJdTNRqV-RHPRADrS3lEI5QIWyssWGt4wdmUS89FCjGlsYvzXF03iH_hXL7PYCDK0vxOLZomxP0m1KkjMnJWE9yoI4vBVlELw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران پشم‌ریزون اهواز توسط بمب‌افکن‌های آمریکایی
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68905" target="_blank">📅 02:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68903">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd4f521a9.mp4?token=flH28e9nvWIp6rhYjFnM0OA4GgPisR1n8en7CbkUsjYOBQUJhyVbetz5O_df9mLhoeYcWaGWjohHXqPGTbjHB6cSob-PsLtWjWuSD4lt3y3Xfet6cfYGrN31mxWuP9a0gXhyWfpu9e2l0uT1f4xnCO3zVzS7VYyfEtUu2r9DIyI9GRZHdkxDJliWygjhG72BOjRcWT7g3Q2Oo-a0KTo-gn-yLUxSSC3DR0X5RBejCCFuEzmV1S3CCcrOdpM6KtZbktjSuQoAJOppevRU7JRFMkZbC7uQ5qR1aDzAYoDcvwNrI4yLf_5d0LKQ_2U51EFIv3DAEOR6z3FUdgii894CtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd4f521a9.mp4?token=flH28e9nvWIp6rhYjFnM0OA4GgPisR1n8en7CbkUsjYOBQUJhyVbetz5O_df9mLhoeYcWaGWjohHXqPGTbjHB6cSob-PsLtWjWuSD4lt3y3Xfet6cfYGrN31mxWuP9a0gXhyWfpu9e2l0uT1f4xnCO3zVzS7VYyfEtUu2r9DIyI9GRZHdkxDJliWygjhG72BOjRcWT7g3Q2Oo-a0KTo-gn-yLUxSSC3DR0X5RBejCCFuEzmV1S3CCcrOdpM6KtZbktjSuQoAJOppevRU7JRFMkZbC7uQ5qR1aDzAYoDcvwNrI4yLf_5d0LKQ_2U51EFIv3DAEOR6z3FUdgii894CtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68903" target="_blank">📅 02:54 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

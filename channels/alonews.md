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
<img src="https://cdn4.telesco.pe/file/nh5aeHiWNH1jU7Uic6mVf7nFzueFjz5ZEeBoT1fOnNEefMU-ZkUZ4OxWbdAqy8e_V6crzg5_6fHfSzOeRmeA8nevbivucJ1Y6qAf1I0nKmLw9Kxy7-CeO8QUtLat5bJVSLaGRHVxGwUVLiNRWWJSaIy_q-sxDtvv8ONj4JfwgsROBVw9uN4MsGVWqDV7sMhn8C7kJHOmNrmGRi3NJccFQIYhDUJKOdBGtUlmT74qIZWDP0BdL8NGwLP6iYQhavFHhDJmSFcLhMOPhT--cPR-NYJOr9rXZnkcWpen6oKyXbnMOKN_ccB7lOuUN_5EjFTC7i-fbGpVKjNVeIz_zdvpDg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 956K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 19:17:59</div>
<hr>

<div class="tg-post" id="msg-144950">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcd39f7dc3.mp4?token=TAFq5Jepaat1oprOESbxLCQZdqnGH9crfR2vhJVJjKjhmpS87Jpcx_abMsmBkrMfXDtXLP-v4yzfxLLyWLr2TiIHxeOpYtBrD6q5QyhH7UfANAMIkDOWKo0aeWg00HDV21LVThh0oe8zAB50id0Q4x1scZTfdqeed1DqWZhnGDnVZy_AhuFmFPxscgDLP77vIuwPtTH4NgqGmuL5salF1T9AUVtzSJAi9UE55bBYE7jDpwOm9s5skUll7srtdoPpagZGnAbMC7PPz3at4kSrcKcJNgIQWHd8-vTHLxYpdqI6DKiEpDmtNhcQKt_pJDgTxFTokKoI2gOAd3UEwyURCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcd39f7dc3.mp4?token=TAFq5Jepaat1oprOESbxLCQZdqnGH9crfR2vhJVJjKjhmpS87Jpcx_abMsmBkrMfXDtXLP-v4yzfxLLyWLr2TiIHxeOpYtBrD6q5QyhH7UfANAMIkDOWKo0aeWg00HDV21LVThh0oe8zAB50id0Q4x1scZTfdqeed1DqWZhnGDnVZy_AhuFmFPxscgDLP77vIuwPtTH4NgqGmuL5salF1T9AUVtzSJAi9UE55bBYE7jDpwOm9s5skUll7srtdoPpagZGnAbMC7PPz3at4kSrcKcJNgIQWHd8-vTHLxYpdqI6DKiEpDmtNhcQKt_pJDgTxFTokKoI2gOAd3UEwyURCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا درباره ایران:
دلیل عدم موفقیت توافق‌نامه، این بود که آن‌ها آمادگی بستن یک معامله را نداشتند.
🔴
وظیفه‌ی من این است که اطمینان حاصل کنم که آن‌ها مایل به بستن یک معامله هستند و آن‌ها مایل خواهند بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/alonews/144950" target="_blank">📅 19:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144949">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J4NGi4d1Gz_n3JuDaQ9mdybQC-DvvDGxLzofBaKhMlPeBzsr21i41HiiMswQRPP_jNZsj52KhYJYCrcKHUC7LgKrWmtm8zPtci9HEKfAlu5dA7aaJDsKzfOjtqlH98UINA-5NwFray-tUXNJUUxVi8R0ty10fFxoWxTyudVaHmYKWhHNI-dn4Cu0hGuMl5h5kA8VATbNnhLGk3PhaBWdEGY0vCOxLGlRuJQA_defGCfnA1C3bfwdY-seouAIjetiVKVwgUvDWiK55AuSQjwb3ZIm227IaZsls_LnQyMwgyy8Oy3_8Yepf2HMZVCbvQOUjaazNltMTawXth1YckMCkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرکز فرماندهی مرکزی آمریکا اعلام کرد که ۸۴ کشتی تجاری را به مسیر دیگری هدایت کرده، سه کشتی را غیرفعال کرده و دو کشتی را بازرسی کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/144949" target="_blank">📅 18:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144948">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5bbcb4367.mp4?token=VLOMXSvOMdVfO-lAyDWLudKqd2MfZ_yHow5V02LBTiD2aXWUvgdKrSpP91MrLuWhQzgCcP2g-7W6NEfU5H18JSszJT0nBydqYDFCSgw9pF3ZG2kqgcDdXDCSpfFdeH_9o_aRxcmPXMTBpGMZSXqFZ1_bUSFDor_Kv1lt2kVFmvmarU0WoEMm1_0Ike0T8VZKzdIGFQZjaNlcT0L18U5YPWxEmjGPny9TFdZXpi13vqcS-dlnBGucqy3cpWKwyCguPJ13xadJzsxdJ1M3VxFWrhwgD7oeDtweq0BNqWiPWKoWYjwtv0QYytTBg4poRdyrdhLek-Fjlj5cRhMHK06NMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5bbcb4367.mp4?token=VLOMXSvOMdVfO-lAyDWLudKqd2MfZ_yHow5V02LBTiD2aXWUvgdKrSpP91MrLuWhQzgCcP2g-7W6NEfU5H18JSszJT0nBydqYDFCSgw9pF3ZG2kqgcDdXDCSpfFdeH_9o_aRxcmPXMTBpGMZSXqFZ1_bUSFDor_Kv1lt2kVFmvmarU0WoEMm1_0Ike0T8VZKzdIGFQZjaNlcT0L18U5YPWxEmjGPny9TFdZXpi13vqcS-dlnBGucqy3cpWKwyCguPJ13xadJzsxdJ1M3VxFWrhwgD7oeDtweq0BNqWiPWKoWYjwtv0QYytTBg4poRdyrdhLek-Fjlj5cRhMHK06NMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا کشوریه که هر کثافت کاری رو میتونی انجام بدی اما اگه از حکومت حمایت کنی بخشیده میشی
@AloSport</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/144948" target="_blank">📅 18:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144947">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
دلار 214000 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/144947" target="_blank">📅 18:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144946">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
خبرنگار حوادث:
هفته قبل یه پیانو رو توی دیوار آگهی کرده بودن به قیمت ۴۰۰ میلیون تومن و وقتی زنگ میزدن به طرف پای همون گوشی ۱۰۰ میلیون تومن تخفیف میداده و مشتری ها رو راضی میکرده تا بیان پیانو رو ببینن؛ وقتی مشتری ها میرفتن اونجا بهشون میگفته مال پسرمه بهش نگید خریدارید تا غصه نخوره فقط برید کارشناسیش کنید و بدون حرف بیایید بیرون. وقتی میپسندیدن و میومدن بیرون؛ طرف میگفت ۱۰۰ میلیون بیعانه بدید و شب بیایید پیانو رو ببرید. ولی بعدا مشخص میشه طرف اصلا صاحب پیانو نبوده؛ بلکه خودش این پیانو رو توی دیوار دیده بوده و به صاحب پیانو گفته میرم کارشناسای مختلف میارم تا این پیانو رو تایید کنن. بعد خودش همون پیانو رو توی دیوار آگهی میکنه و مشتری های خودشو به عنوان کارشناس میبره سر پیانو. تو همون روز سر ۱۰ نفر رو اینطوری کلا گذاشته و یه میلیارد تومن جمع کرده و فرار کرده.
هر آگهی دیوار رو که دیدید قیمتش خیلی پایینه یا خیلی راحت تخفیف میده بدونید مشکوکه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/144946" target="_blank">📅 18:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144945">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80781901b0.mp4?token=SjHZ8i47K_q47feHNSEdVGEIUBr4jymHmv32Y02qaVJ-tY3VuKGDL6_dCl8hpxRWb2bPfsv0MU9-uebNIXpwAwxHlLEYo0mmi7gvbHKnHPENkRYx1P57LYfsxBK3RUC8tsqXHDzKx-tvmrSlhBmZgIIBy4OHE60MEOhnn2goKe-0WWLnvDditLpjx4NQPKpj3_mUGsI_uAa_8LpIjxIiw-MI0z2ZyaCyaRMRwsXFKKx25jJQqeVXmKBp-90nIxO-smkqfmVEFH-ZEwr2YJCIj2nVym81ChHMVtUIprTceM0Q-YF_oYjyFcv7VfILySFCLBWpNEQIpx5AeaQ_5EsDB5AeCji4k1EhUttUQwCC5cM9eTaA2slpbGPz42KAiPWq5XSPyCMio2df34wgeKF3jX1vsw7fdrvHzZXSNMohLdDTAq7emWdekTo5xr9CM8p3pY3ueCQQWk_ZVGtT8drxIsd_fCNDS3Vp4Rl4PG85fdr2jX_y7neV4QifWCdW10STI5DB3-GfT4SWcDfasBdmfNWQ-nhgCkmYKD3ZN-rw2mnSh3-bN4afJ-sZ91ILAcH2QVQvHnesrIb7jQiQghP_4psKvl9ayk8zy0LTsdDf8nGaLDnIdVEOR0zu9fKYhhL11w1wibIThE6phMQXO1EOLUhfB-MWjz90wUA4PYi-ERw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80781901b0.mp4?token=SjHZ8i47K_q47feHNSEdVGEIUBr4jymHmv32Y02qaVJ-tY3VuKGDL6_dCl8hpxRWb2bPfsv0MU9-uebNIXpwAwxHlLEYo0mmi7gvbHKnHPENkRYx1P57LYfsxBK3RUC8tsqXHDzKx-tvmrSlhBmZgIIBy4OHE60MEOhnn2goKe-0WWLnvDditLpjx4NQPKpj3_mUGsI_uAa_8LpIjxIiw-MI0z2ZyaCyaRMRwsXFKKx25jJQqeVXmKBp-90nIxO-smkqfmVEFH-ZEwr2YJCIj2nVym81ChHMVtUIprTceM0Q-YF_oYjyFcv7VfILySFCLBWpNEQIpx5AeaQ_5EsDB5AeCji4k1EhUttUQwCC5cM9eTaA2slpbGPz42KAiPWq5XSPyCMio2df34wgeKF3jX1vsw7fdrvHzZXSNMohLdDTAq7emWdekTo5xr9CM8p3pY3ueCQQWk_ZVGtT8drxIsd_fCNDS3Vp4Rl4PG85fdr2jX_y7neV4QifWCdW10STI5DB3-GfT4SWcDfasBdmfNWQ-nhgCkmYKD3ZN-rw2mnSh3-bN4afJ-sZ91ILAcH2QVQvHnesrIb7jQiQghP_4psKvl9ayk8zy0LTsdDf8nGaLDnIdVEOR0zu9fKYhhL11w1wibIThE6phMQXO1EOLUhfB-MWjz90wUA4PYi-ERw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان، به پوتین: قدرت‌های بزرگ، صرفاً به این دلیل که قدرت دارند، حق ندارند بدون توجه به چارچوب‌های بین‌المللی و قوانین بین‌المللی، به اقدامات تهاجمی دست بزنند.
🔴
اقدام تهاجمی که ایالات متحده علیه ایران انجام داد، هیچ مبنای قانونی، هیچ مبنای علمی و هیچ توجیه منطقی نداشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/144945" target="_blank">📅 18:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144944">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9df57a2bc.mp4?token=BbN-wZtcBifJ3lIwluV8ITQ0lRIhtqzDgnYRtO5lwreiC6FTr4AZ1F2o30Ic14IgFb0k4oa2o64bakCrglvN0328gB5pencch9GEhM4_3Rq9Xr3er2Q3nduSa7ckpCQyIE9mTSJKoWqi9Ue1q-Uch80gLSfGOLvtyFf64vDn6SPp3p5dqsQgtBno4Kk9xBlzKI0xnEWvZpxxWYrbto6HU0L2Pmgrvcey6bny8QFB5ayKHvdDdiWnQugfqjAC8KfX3Ny4aagWsBxotQyCLSTvIajnqkxG04BHRwVZB1CUTvDx1XCnWkKeHK2FM1Gtonl6UeGwizUUYFt7MTIbzexnbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9df57a2bc.mp4?token=BbN-wZtcBifJ3lIwluV8ITQ0lRIhtqzDgnYRtO5lwreiC6FTr4AZ1F2o30Ic14IgFb0k4oa2o64bakCrglvN0328gB5pencch9GEhM4_3Rq9Xr3er2Q3nduSa7ckpCQyIE9mTSJKoWqi9Ue1q-Uch80gLSfGOLvtyFf64vDn6SPp3p5dqsQgtBno4Kk9xBlzKI0xnEWvZpxxWYrbto6HU0L2Pmgrvcey6bny8QFB5ayKHvdDdiWnQugfqjAC8KfX3Ny4aagWsBxotQyCLSTvIajnqkxG04BHRwVZB1CUTvDx1XCnWkKeHK2FM1Gtonl6UeGwizUUYFt7MTIbzexnbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دکتر پزشکیان: در مورد یادداشتی که ما امضا کردیم، ما همچنان به آن متعهد هستیم.
🔴
اگر ایالات متحده به همان یادداشت بازگردد، ما نیز طبق آن عمل خواهیم کرد.
🔴
در آن یادداشت، ما چیزی جز حقوق کشورمان را درخواست نکردیم، و این همان چیزی است که ما در پی آن هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/144944" target="_blank">📅 18:11 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144943">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
قالیباف: اگر محاصره را تشدید کنند، حتماً پاسخ نظامی می‌دهیم و همه ضرر خواهند کرد
🔴
دشمن در حال حاضر در جنگ اقتصادی، بر روی جنبه روانی آن متمرکز شده است
🔴
بخش زیادی از تحریم‌های اعلامی جدید، قبلاً نیز اعمال می‌شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/144943" target="_blank">📅 17:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144942">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
یک مقام کاخ سفید به الجزیره گفت:
رئیس جمهور ترامپ تمام گزینه‌های موجود برای برخورد با ایران را حفظ کرده است.
🔴
ایرانی‌ها می‌خواهند با ما معامله کنند، اما مواضع آنها همیشه دیرهنگام است و از آنچه لازم است، فاصله دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/144942" target="_blank">📅 17:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144941">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: احتمالاً این هفته و هفته آینده، تحریم‌های جدیدی علیه بانک‌های ایران اعلام خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/144941" target="_blank">📅 17:49 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144940">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
اسکات بسنت، وزیر خزانه‌داری ایالات متحده:
رشد اقتصادی مجدداً در حال افزایش است.
🔴
رشد اقتصادی بهتر از آن چیزی بوده که انتظار می‌رفت، با توجه به تنش‌های موجود با ایران.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/144940" target="_blank">📅 17:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144939">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/914636c9fd.mp4?token=j16SRhA3959IxtvFrKc5Mww3bsltm7Lk-UpdXRfKmK58t_XOf_p4X6dYfBne3FCuV1-Fg4Up5XGRAWGYu6uRYZoUwmnDHMMyCvhEtnYjsRUA9HywW-AYxeUv2uSfACcKq1tgOJ1x6LxU-F92EgvsO6Zdettdmt--Fq35MNGkKtAg2Q1BxUYFOwOuHEJwN7Jbo6GW7hTHEtXpevMM_Mn6JIEw0yJxpTCcZ3RkxlsIxdgagecyVrIr9Glvu9kwKXxSrM0SLkKR2ZO-hDcdEuGELd-a9og93RbHnhDd61xHPqIVFIYC80OROA0I9SfGpxGp2Whipy_ERSM7dEy-puwMxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/914636c9fd.mp4?token=j16SRhA3959IxtvFrKc5Mww3bsltm7Lk-UpdXRfKmK58t_XOf_p4X6dYfBne3FCuV1-Fg4Up5XGRAWGYu6uRYZoUwmnDHMMyCvhEtnYjsRUA9HywW-AYxeUv2uSfACcKq1tgOJ1x6LxU-F92EgvsO6Zdettdmt--Fq35MNGkKtAg2Q1BxUYFOwOuHEJwN7Jbo6GW7hTHEtXpevMM_Mn6JIEw0yJxpTCcZ3RkxlsIxdgagecyVrIr9Glvu9kwKXxSrM0SLkKR2ZO-hDcdEuGELd-a9og93RbHnhDd61xHPqIVFIYC80OROA0I9SfGpxGp2Whipy_ERSM7dEy-puwMxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور ترکیه، اردوغان، به پوتین گفت: روابط ترکیه و روسیه امروز در سطح بسیار بالاتری نسبت به هر زمان دیگری در گذشته قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/144939" target="_blank">📅 17:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144938">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6df48cd02.mp4?token=rRdg2xQdHz6oOhmN2aAk1UyxLsYvkAPGCYVSygUZmaUj02pYkOd5jrJgIz4WatjXI3razy7djqicHSVsPm5-TO-7msDe_Z5PhLl8qxtySZ_wNRmb2dvDySCk3Xd1DAkFbz3Z8dsT2RWLOooV-PfksaksN6JOVms3P-uswurwFKp5hwZesuPxMhmguW9whVnp6KcMiXcATF-QV2qcH1-Q6dfDVqbQ1zwNLewnahP07iNsJyk3L6AqyH1K8tagKBBeZCH6k1Y1tLWoh-ehvYyS3D1VhrC2EOAxWEtKeZMUnulnVK9h-QD6_SwE-2AhGBgSJT6BzZ27IA4je1VCMwifrL_-l_CzO00gdwwZ70Ujs_XWsJnbys13YfbV0dTPueKGJ74UIAM8FbnDB6KGeZHQjkf-pFntnfTctUhLdmrpJXKR94EFH43IT9CYD5C9uNJWs6F5c1Wb2m6ERcrtYPyH0LjeNRSKnhhsUUkPRPquAWcqgXYWhEhRcYLHwiBmSuqbkLey3hdexfjPvaxttkZxxP7G2RKGDQn_ODPCTeSi70f-D6V9vtAsnK6AgtNNfv_Oka9d1caM2ZAYP4_x5zeKdhh-k-v-GXqbodPW5CwWqw99BLtLDZWxqJsjfPtiZmlkpygrXGBpyeGVbd5f_jtMqNeD-qkR_sEJNLf-8n5RlMo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6df48cd02.mp4?token=rRdg2xQdHz6oOhmN2aAk1UyxLsYvkAPGCYVSygUZmaUj02pYkOd5jrJgIz4WatjXI3razy7djqicHSVsPm5-TO-7msDe_Z5PhLl8qxtySZ_wNRmb2dvDySCk3Xd1DAkFbz3Z8dsT2RWLOooV-PfksaksN6JOVms3P-uswurwFKp5hwZesuPxMhmguW9whVnp6KcMiXcATF-QV2qcH1-Q6dfDVqbQ1zwNLewnahP07iNsJyk3L6AqyH1K8tagKBBeZCH6k1Y1tLWoh-ehvYyS3D1VhrC2EOAxWEtKeZMUnulnVK9h-QD6_SwE-2AhGBgSJT6BzZ27IA4je1VCMwifrL_-l_CzO00gdwwZ70Ujs_XWsJnbys13YfbV0dTPueKGJ74UIAM8FbnDB6KGeZHQjkf-pFntnfTctUhLdmrpJXKR94EFH43IT9CYD5C9uNJWs6F5c1Wb2m6ERcrtYPyH0LjeNRSKnhhsUUkPRPquAWcqgXYWhEhRcYLHwiBmSuqbkLey3hdexfjPvaxttkZxxP7G2RKGDQn_ODPCTeSi70f-D6V9vtAsnK6AgtNNfv_Oka9d1caM2ZAYP4_x5zeKdhh-k-v-GXqbodPW5CwWqw99BLtLDZWxqJsjfPtiZmlkpygrXGBpyeGVbd5f_jtMqNeD-qkR_sEJNLf-8n5RlMo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف: دشمن پس از شکست در عرصه نظامی و دیپلماسی سراغ جنگ اقتصادی و شناختی رفت و آن را به جنگ نظامی خود اضافه کرد
🔴
محاصره دریایی به معنای جنگ نظامی است
🔴
هدف دشمن از جنگ ترکیبی این است که در داخل کشور، اغتشاش را به همراه ترور و حملات نظامی کوتاه آغاز کند
🔴
نقشه دشمن برای همه مسئولان ما روشن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/144938" target="_blank">📅 17:43 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144937">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
کره شمالی، خواسته‌های ایالات متحده برای خلع سلاح هسته‌ای را رد کرده و اعلام کرده است که به تقویت زرادخانه هسته‌ای خود ادامه خواهد داد.
🔴
پیونگ‌یانگ تاکید کرد که "سیاست خصمانه" ایالات متحده علیه کره شمالی تغییر نکرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/144937" target="_blank">📅 17:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144936">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45fd2a26f4.mp4?token=nU-_H8BPzqFUBamVqmCkPe0Ex-BTNnd0Xp3CekRGessANm3P_PM1BQZ8hHZPPhZy3qQtgwolPo_8TxbbCwlV9iTvPwhpCLrGDE4ww5BNFUlWKPVFKiRp-wiyKr4C-AmoANj8M2xD78DjF3mHx4esqI0plCWx0YpMeQLMLfoYlSy3gMqklR7fnWM7sCltwaPX8FwICC4udDnFtHFlN5avQqO7p3D54ure1mRHs8VUfSXfp_IiAt150yIXgj7yGzVkxfVho_qrks5FPVrsuBMKmD7iI5dzS1uy2OCPh2NY5sqCh83kL4O96HwVzVEHjpD34pENnWvb1C4xjWShyDKFnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45fd2a26f4.mp4?token=nU-_H8BPzqFUBamVqmCkPe0Ex-BTNnd0Xp3CekRGessANm3P_PM1BQZ8hHZPPhZy3qQtgwolPo_8TxbbCwlV9iTvPwhpCLrGDE4ww5BNFUlWKPVFKiRp-wiyKr4C-AmoANj8M2xD78DjF3mHx4esqI0plCWx0YpMeQLMLfoYlSy3gMqklR7fnWM7sCltwaPX8FwICC4udDnFtHFlN5avQqO7p3D54ure1mRHs8VUfSXfp_IiAt150yIXgj7yGzVkxfVho_qrks5FPVrsuBMKmD7iI5dzS1uy2OCPh2NY5sqCh83kL4O96HwVzVEHjpD34pENnWvb1C4xjWShyDKFnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف: در تنگه هرمز علاوه بر اعمال قدرت نظامی،
در عرصه دیپلماسی نیز پیشرفت‌های خوبی انجام شده است
🔴
توافق با عمان، به‌عنوان کشور ساحلی تنگه هرمز، با دیپلماسی به دست آمد
🔴
قدرت نظامی ایران در تنگه هرمز حفظ و ارتقا پیدا کرده است
🔴
اعمال مدیریت ایرانی بر تنگه، هیچ منافاتی با قوانین بین‌المللی ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/144936" target="_blank">📅 17:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144935">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: در 2 سال آینده، تنگه هرمز به یک مسیر آبی بی‌ارزش تبدیل خواهد شد و نفت از طریق خطوط لوله در خشکی منتقل خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/144935" target="_blank">📅 17:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144934">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
وزیر خزانه‌داری ایالات متحده، بَسنت:
تحریم‌های ایران ممکن است بر شرکت‌های اجاره‌دهنده هواپیما نیز تاثیر بگذارد
🔴
ما گفتگوهای خصوصی با چین داشته‌ایم. ما در حال بررسی همکاری با چین در مورد مسائل مربوط به ایران هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/144934" target="_blank">📅 17:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144933">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3cdaf5608.mp4?token=dmRkCqQNvJyV8sBx2F1Uiq_meD2dg63MkU5HLyu57AciTNu_nBe4yQjfnrUPk6P6PJFILjaFoKEd1fTilrLSG8uHdhIMRbZ4w6qL3MUMQvw3Dbxgaxq5VVuwyxbzR0g2pWxt44LQ8EUA7Lo9dcY5Odg9tX9r1vh46l1p8CAm2ZeBCp5BFAHuRcbpxf_pHwbYGVLIrsIV8L4KG9NQzq5BUrpg5E-erlf0bDvl1Ingq3vLT63TMI7rzM4VoglO2_teJFeRRA5g1iC_O-SFOrGf5665DzOkONHGONzgCqCa-AQlZ7IA4acpbsnwGY0vOfnoxbpqFDcQWr8DSn95mmdOZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3cdaf5608.mp4?token=dmRkCqQNvJyV8sBx2F1Uiq_meD2dg63MkU5HLyu57AciTNu_nBe4yQjfnrUPk6P6PJFILjaFoKEd1fTilrLSG8uHdhIMRbZ4w6qL3MUMQvw3Dbxgaxq5VVuwyxbzR0g2pWxt44LQ8EUA7Lo9dcY5Odg9tX9r1vh46l1p8CAm2ZeBCp5BFAHuRcbpxf_pHwbYGVLIrsIV8L4KG9NQzq5BUrpg5E-erlf0bDvl1Ingq3vLT63TMI7rzM4VoglO2_teJFeRRA5g1iC_O-SFOrGf5665DzOkONHGONzgCqCa-AQlZ7IA4acpbsnwGY0vOfnoxbpqFDcQWr8DSn95mmdOZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف: آمریکا می‌خواهد برخلاف تفاهم‌نامه از مسیر جنوبی تنگه هرمز عبور کند که این اجازه را نخواهیم داد
🔴
قبل از جنگ، روزانه حداقل ۱۲۰ کشتی از تنگه هرمز تردد می‌کرد و حتی اگر یک یا دو کشتی هم از تنگه عبور کند، به هیچ عنوان قابل مقایسه با قبل از جنگ نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/144933" target="_blank">📅 17:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144932">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qC185cPi83w8BYzXx_ZlwVIePI8u5W0Dp7NQ819-24bVuxfJ2JGuANNifMehzphkGGXW7MuEMxe96NmUNLCk-Fv3xaqqEmmdz6VZ1SVzEJLosBqX4RN8MKxni9K5RpDjunQZ8BxwNSfItluJ9GhBjBIG45pHFrhhSnQbFb0-tiIDCRSBQuflagDHSQvQ4SLcqgMXTlG7wquFkvN5Lfqds_f9bRt38qxbqf5Ja47Fb9pb5TSBgPqA93vASZntL36uENMR50xVIQUDBm5le_Q2XXiCFdPh1lxDM7pFEOfL7-2tKoVwEhqSyePhpCvmNUqHY6dox94c9OZr1p7Xv0euBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: پاسخ و حمایت عالی و فراگیر از سوی هر دو حزب در کنگره برای طرح احیای صنعت فیلم، تلویزیون و سرگرمی.
🔴
ما این صنعت، که زمانی بسیار بزرگ بود، دوباره به آمریکا باز خواهیم گرداند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/144932" target="_blank">📅 17:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144931">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
ایلان ماسک: هوش‌ مصنوعی تا ۳ سال دیگه پزشکان و جراحان رو از کار بیکار میکنه
🔴
چون ربات «آپتیموس» از بهترین جراح های دنیا هم بهتر کارش رو انجام میده. دانشکده پزشکی الانم بی معنی شده و هرکی داره پزشکی میخونه فقط داره وقتشو تلف میکنه.
🔴
پ.ن: این ربات میتونه به جای تمام متخصصین تمام رشته ها عمل های جراحی رو بدون خطا انجام بده‌!
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/144931" target="_blank">📅 17:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144930">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
مدیر عامل توانیر : خاموشی‌ها تا اواسط شهریور به تدریج تمام می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/144930" target="_blank">📅 17:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144929">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
ماکارونی گران می‌شود
🔴
ماکارونی تا پایان مهر بر اساس نرخ‌ مصوب فروخته می‌شود اما از آبان و همزمان با آزاد شدن تامین گندم صنف و صنعت قیمت این محصول تغییر خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/144929" target="_blank">📅 17:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144928">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
قالیباف: در ۱۵ ماه گذشته، به اندازه یک دهه پیشرفت در حوزه نظامی داشتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/144928" target="_blank">📅 16:49 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144927">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZH3QPzREbYix1lIDQexMzTrqS333Z1UVZLzNVu5Xe0yNQo-NaR2cPG08AAgLZeKnMQTjb48rij_vTxuXTHhBB5I7aXesb4EK9VhzSFVq5V08P0ze5Zi09vftzhwnB8Yl80iqEKIjuxXe2CUqmUBLHEgqpnD163sBqy_LMMcYLjHW8_jUXqWGxeFu4RYQ-JXpNeZ2VfWBa7nM6YmDNEcWHpmjo8ttT0JlzmsYLWrMaGpa_s2SqfalZ-q8LO-eJQEeC5ffRBIWfqFwCWNT7KaGIXjQRukbFIyW4phhAqKgTcecA3ZqNB64-dVpO_fmghgDAoZ2Hj5ZPUqf4xT45BSag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت خارجه آمریکا با فروش احتمالی یک بسته تسلیحاتی به ارزش ۸۰۰ میلیون دلار به عراق موافقت کرده است که شامل بالگردهای Bell 412EPX و Bell 407M و تجهیزات مرتبط با آنها می‌شود.
🔴
این بسته پیشنهادی شامل تیربارهای سه‌لول GAU-19، راکت‌اندازهای ۲.۷۵ اینچی M260، حسگرهای الکترواپتیکی/مادون‌قرمز L3Harris WESCAM MX-15HDI و سامانه‌های هشدار موشکی AN/AAR-60 Block 2 است.
🔴
این قرارداد همچنین شامل تجهیزات ارتباطی، قطعات یدکی، آموزش و پشتیبانی لجستیکی خواهد بود. شرکت Bell Textron در فورت‌ورث تگزاس، پیمانکار اصلی این قرارداد خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/144927" target="_blank">📅 16:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144926">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6bd9cc20c.mp4?token=jPFEXFQEt2gwT154ZsPify38Fytni3r-NFNYnyu83G6Ui3NHPWtTwEAsTTxUMNTb9cXwt7WyBHAxMu7q7wUuW3m7CfWQNjeSmFR-OxNaqO0YeTwEMCsvcQLEgpnEWXMf51Av0lEf1XnKalIejNKgx4vfXsNgWErqD-I_VxmvKYbZGMms7taCHMzQuwz81CzHqkMID4g3fCMKwWs5gzmyFgQRKGSMIaGh6YOSeHT2nhbr8dVyNPS4AJSdpkboQ30EcMH_9lW6g49iir5IOssS9lvez29ngvQe0c6Fks3U4jm1rBE6T-5tbQgfIweZSJewNC-48M0XJe8n-qFIX3B9UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6bd9cc20c.mp4?token=jPFEXFQEt2gwT154ZsPify38Fytni3r-NFNYnyu83G6Ui3NHPWtTwEAsTTxUMNTb9cXwt7WyBHAxMu7q7wUuW3m7CfWQNjeSmFR-OxNaqO0YeTwEMCsvcQLEgpnEWXMf51Av0lEf1XnKalIejNKgx4vfXsNgWErqD-I_VxmvKYbZGMms7taCHMzQuwz81CzHqkMID4g3fCMKwWs5gzmyFgQRKGSMIaGh6YOSeHT2nhbr8dVyNPS4AJSdpkboQ30EcMH_9lW6g49iir5IOssS9lvez29ngvQe0c6Fks3U4jm1rBE6T-5tbQgfIweZSJewNC-48M0XJe8n-qFIX3B9UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پدیده عجیب آسمان صورتی در چین پیش از طوفان
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/144926" target="_blank">📅 16:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144925">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
کارشناس صداوسیما: آمریکا با بسته بودن تنگه، بیشتر از ۶ ماه دیگر دوام نمی‌آورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/144925" target="_blank">📅 16:26 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144924">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
نیویورک پست: پسر بنیامین نتانیاهو به دلیل یک تهدید «قابل‌توجه» از آمریکا خارج شد؛ پس از آنکه رهبر اسرائیل درباره توطئه ایران هشدار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/144924" target="_blank">📅 16:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144923">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/voeyZPv1aXbhpKev8RmwKUNIVkj1C3ZDVI-xwbZN6NYw8Bw-mqYVPKD35_kIszWQpQEm8-PSQcGjYWVtipiCsMHul46sMOcenDgaIiUl3v7RzS7ORCis6We2h14x1vURJpmTLyCYde_yI5q6iHqDBbT2D-zeTp5tiW3ZVT7cDkCA_yLnlWEheoYVjgudfSgmwDZdsuhkaZHbb7fN8XkVKjgC84SpcwJdFEtEb9P0Xwmh_f0MqOZoHDEtiLD82eawiG_CmedL4-NvZiIhZ_dCZh4FfRAgWVoTj5ag7EOMmNuwRTxJdDsVj0c3wvKasiP72_4Vs2ng9sO7oLT756U-BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مدیرعامل شرکت ملی گاز ایران اعلام کرد در برخی مناطق تهران قبض‌های گاز با مبلغ یک میلیارد تومان صادر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/144923" target="_blank">📅 16:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144922">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
شرکت ایران‌خودرو درخواست افزایش قیمت محصولاتش رو داد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/144922" target="_blank">📅 16:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144921">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: مبدا حملات علیه لارک، یکی از کشورهای منطقه بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/144921" target="_blank">📅 16:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144920">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
پوتین در گفتگو با پزشکیان: روسیه تلاش می‌کند به ایران کمک کند و در شرایط دشواری که این کشور با آن روبه‌رو است، کالاهای ضروری را در اختیار آن قرار دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/144920" target="_blank">📅 15:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144919">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f11c8c5cf.mp4?token=Dtv075-rJNgaSuLFTAlqkpALHdAIWbW9j6xGPga-4HME_kWyfR9ZPcH1kv8jKFZSUmGQEi4_63CX0XcEUQVNr1kp_zx9H3bh83ikuWQMhP9HNF8uLv6QdAweKDjUU5UFoegn6a98mjTEuaUdFWV0vbVyZ1xdFoPb5E_pJaV80gJ3VtaBaoF3ZqHLuwonXNcwLJkuTCp7SKGGWmY1zs6V1xsH4FyydcuW6isYpHVTwrG3AMtPQqtR72HQ9aYTq-iKHeuZYm4coTl4cAmxPbxhaOxzO4pNg2Up5B08Hv3vBxhX6RSJCOyvSICRpvynAhMPOxCS68m0sYgpgJv6XPcyxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f11c8c5cf.mp4?token=Dtv075-rJNgaSuLFTAlqkpALHdAIWbW9j6xGPga-4HME_kWyfR9ZPcH1kv8jKFZSUmGQEi4_63CX0XcEUQVNr1kp_zx9H3bh83ikuWQMhP9HNF8uLv6QdAweKDjUU5UFoegn6a98mjTEuaUdFWV0vbVyZ1xdFoPb5E_pJaV80gJ3VtaBaoF3ZqHLuwonXNcwLJkuTCp7SKGGWmY1zs6V1xsH4FyydcuW6isYpHVTwrG3AMtPQqtR72HQ9aYTq-iKHeuZYm4coTl4cAmxPbxhaOxzO4pNg2Up5B08Hv3vBxhX6RSJCOyvSICRpvynAhMPOxCS68m0sYgpgJv6XPcyxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار پزشکیان و پوتین در بیشکک
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/144919" target="_blank">📅 15:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144918">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: ما در شرایطی قرار داریم که اکنون نمی‌توانیم اصلاً درباره بازگشت به فلان تفاهم صحبت کنیم؛ دلیلش هم روشن است، طرف آمریکایی آن را نقض کرده است
🔴
آمریکا بود که جنگ را شروع کرد، آمریکا بود که تفاهم را نقض کرد، آمریکا بود که به بهانه‌ای ساختگی مجدداً حملات را شروع کرد و اکنون هم این آمریکاست که باید در این زمینه در برابر جامعه جهانی پاسخگو بماند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/144918" target="_blank">📅 15:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144917">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
وزیرگردشگری: میخوام کاری کنم ایرانیای خارج، حداقل سالی ۱ بار بیان وطن
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/144917" target="_blank">📅 15:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144916">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: مادامی که عضو NPT هستیم، خودمان را متعهد به تکالیف مندرج در این سند می‌دانیم.
🔴
موضع ما ثابت و اصولی بوده است.
🔴
در رابطه با اصل سلاح‌های هسته‌ای، سلاح‌های هسته‌ای به‌عنوان مخرب‌ترین سلاح کشتار جمعی، از نظر ما هم مغایر با آموزه‌های دینی‌مان است و هم سلاحی ضدتمدنی و ضدبشری است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/144916" target="_blank">📅 15:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144915">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه ایران، بقایی: آمریکایی‌ها بین مذاکره و تحمیل خواسته‌ها، تفاوت قائل نشده‌اند و این روش با ایران نتیجه‌ای نخواهد داشت.
🔴
ما تأکید می‌کنیم که هرگونه تجاوز آمریکا با پاسخ مواجه خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/144915" target="_blank">📅 15:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144914">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
اسماعیل بقایی: هیچ فعالیت هسته‌ای در کوه کلنگ نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/144914" target="_blank">📅 15:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144913">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه در نشست خبری: عاصم منیر نه پیام مثبتی داشت، نه پیام منفی
🔴
ایشان در چارچوب نقش‌آفرینی پاکستان برای
کمک به کاهش تنش
، به ایران سفر داشت و دیدگاه‌های خود را مطرح کرد.
🔴
این تلاش‌ها نه‌فقط از سوی پاکستان، بلکه از طرف برخی دیگر از کشورها هم ادامه دارد.
🔴
درباره نحوه ادامه تفاهم‌نامه اسلام‌آباد با توجه به شرایط روز تصمیم می‌گیریم
🔴
در شرایط فعلی باید بر دفاع و مقاومت در برابر زیاده‌خواهی آمریکا متمرکز شویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/144913" target="_blank">📅 15:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144912">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLL3trZhDJ_JLwmSeg3hr-AMYcMcisZYtmT6vDeV974Vf_7XboTbxC5YZQPGpkobv6j5ks8DHChlc3hFZmLzs3ntWZ8HC90Mo0nfRcgJ7uNQmbH--vou1PAQ1Z2LJcUlRWx1LPHIj5smSwUhoVA0kScVe-UIT7xAQFdfmaE1UX1FhgADT8trBHlzs0aZ-a8KynqkkwdueIzAFPukLNOzFiWX_scADOnuKwPoZEygTrOMpdGJs3gg5EWcSTUA8UYHJKr3savX1e8ERKbT9MOFSHrzhEOtXPCowMKGMdT79Po0_eA5mQ8vOHZtdjqSS38F84ZpCF9a_qpPl3FUfEG0IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شلیک توپخانه‌ای ارتش اسرائیل به شهر حولا در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/144912" target="_blank">📅 15:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144911">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
مجازات فحش دادن در سال ۱۴۰۵ اعلام شد: اگه در حد تحقیر باشه جریمه‌اش بین ۲۰ تا ۸۰ میلیونه.
🔴
اگه فحش ناموسی و جنسی باشه ۸۰ ضربه شلاق و تا ۶ ماه حبس داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/144911" target="_blank">📅 14:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144910">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه قطر: رایزنی‌ها با عمان و پاکستان درباره اقدامات برای کاهش تنش در منطقه ادامه دارد.
🔴
حل‌نشدن بحران تنگه هرمز به تشدید تنش منجر خواهد شد و به همه آسیب می‌زند.
🔴
با شرکای خود برای دستیابی به یک راه‌حل مسالمت‌آمیز و بازگشایی تنگه هرمز تلاش می‌کنیم.
🔴
هشدار داده‌ایم که اسرائیل از تشدید تنش در منطقه برای تحمیل یک واقعیت جدید سوءاستفاده نکند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/144910" target="_blank">📅 14:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144909">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
نخست وزیر پاکستان: پیمان دفاعی مکه علیه هیچ کشوری نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/144909" target="_blank">📅 14:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144908">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/shpch1BBY5q53dLJZqMavBtgOfpG6G__PVpAcIW_kHYES5nZAKe9FzY1QsJcgPFttPu53ljzZT5IYZgL9gb1eJNX3eHRXxcuOP-pE19U7QGt01DpKGCyuJZlFH6rmWYZAA9lsPhIIZNxkehupLNRZd4_fhhFURcW6qZdu0jGgRIZpIZ61hOftNhKbuqxY6NY463HEKQc8la1tDeaqYRzTZhZJVbXJLN4N4uHvmvr63izU2ls2N6dU34DjaRK8mULxX9mGy3RcrdWoMnGmJJOx8i-e4fXfnYw-_VBFyRbezfA0C4onuWyhofJpFybjXpXXpEOIQEl8uAp85QsM2H-Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسانه‌های آمریکایی: شب گذشته، رویدادی به شدت نگران‌کننده و قابل‌توجه در سواحل شرقی آمریکا رخ داد.
🔴
پایگاه دریایی نورفولک، پایگاه اصلی نیروی دریایی آمریکا و بزرگ‌ترین پایگاه دریایی جهان، به دلایلی که هنوز مشخص نیست در وضعیت آماده‌باش کامل قرار گرفت
🔴
به گفته یک سخنگوی رسمی، «دسترسی به این تأسیسات محدود شده و برخی دروازه‌ها بسته شده‌اند یا با لاین‌های عبوری کمتری فعالیت می‌کنند» که علت آن وجود یک تهدید نامشخص اعلام شده است.
🔴
نکته نگران‌کننده اینجاست که یکی از معدود دفعاتی که چنین هشداری صادر شده بود، بلافاصله پس از حوادث ۱۱ سپتامبر رخ داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/144908" target="_blank">📅 14:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144907">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه قطر اعلام کرده رایزنی‌ها با عمان و پاکستان برای کاهش تنش‌های منطقه‌ای ادامه دارد.
🔴
دوحه هشدار داده حل‌نشدن بحران تنگه هرمز می‌تواند به تشدید تنش منجر شود و همه طرف‌ها را متضرر کند؛ قطر می‌گوید با شرکای خود برای رسیدن به راه‌حلی مسالمت‌آمیز و بازگشایی تنگه تلاش می‌کند.
🔴
قطر همچنین هشدار داده اسرائیل نباید از تشدید تنش‌ها برای تحمیل «واقعیتی
جدید» در منطقه استفاده کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/144907" target="_blank">📅 14:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144906">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
۱۱ کشور اتحادیه اروپا خواستار پایان استفاده «مانع‌تراشانه» از حق وتو در سیاست خارجی شدند
🔴
اتریش، دانمارک، بلژیک، فنلاند، فرانسه، آلمان، لوکزامبورگ، هلند، رومانی، اسپانیا و سوئد خواستار بررسی ایده گذار از اصل اجماع به رای‌گیری با اکثریت واجد شرایط در سیاست خارجی اتحادیه اروپا شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/144906" target="_blank">📅 14:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144905">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0dSismnDvC7JoF5T04BXDEkEd7VtpqZ-ORVJ2vgMQbetYE47xkvaH_DFE3NKl1luDq6TLfERhPg8HI1xfRhVEUSo0W0BqWuXEbzgLFOVvThewotd34Gn5ojevmVOV-DtPcv42-1Sv_5SwX-l0ZfwvIdCx5rPAeCRo5ryYusPd8WJVCdVSuJfkGrlNm8uakWfwm1iwJP3xw_1EU4Z_MfS10T4CUrR1nnjxapOErC7bWL-vkebExcomvyRODxBg8zo1tHkc-cA-D39-KpKSKStkj-u3Sr8vl9eXrx4zks8K1iLtMyPDVP61DuNpFerlwqb0VhGdOAyDLulXeq7eLMmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امارات متحده عربی به تأثیرگذاران هزاران دلار پیشنهاد می‌کند تا علیه حماس تبلیغ کنند پیام‌های مستقیم نشت‌شده، پیشنهاد ۱۵۰۰ دلاری از سوی لوی الشریف، فعال در زمینه توافق‌های ابراهیم، را فاش می‌کند که در آن نکات کلیدی ارائه‌شده درباره برادری مسلمانان را به یک تأثیرگذار آمریکایی پیشنهاد داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/144905" target="_blank">📅 14:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144903">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/561954f020.mp4?token=HieCwXOxS_-ia95WVmx2eKfhfeYaO3fHOV-VR7-bJ2asvTD3agW4sk1c_nnyrhT3n98PH7_ihrBNWhHpqs3BByzuSdIWkK1VI4bdB9yltMtbSAnJlOHhMx1I5TB_hIJehPRiHKSrzioKvnOBVNHLLWt7PNGaKNUSaRJdhRwQx7pGSBCbAn02Rr9Cxjo81VUV4sZs6kv8qznfnjQdnVC-6SNbk4ovzb7-gn8WL5Lb-e6zB8y3U_cKnTdxtCR3axlrUN-E8OFv2Ohgz2_TTPIlbDLKrcfrvjCo6AyGrVoex9F5B0Pp_ikU_z51gs-RaWLRYEjLBqhF87HV8mQMz2GYNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/561954f020.mp4?token=HieCwXOxS_-ia95WVmx2eKfhfeYaO3fHOV-VR7-bJ2asvTD3agW4sk1c_nnyrhT3n98PH7_ihrBNWhHpqs3BByzuSdIWkK1VI4bdB9yltMtbSAnJlOHhMx1I5TB_hIJehPRiHKSrzioKvnOBVNHLLWt7PNGaKNUSaRJdhRwQx7pGSBCbAn02Rr9Cxjo81VUV4sZs6kv8qznfnjQdnVC-6SNbk4ovzb7-gn8WL5Lb-e6zB8y3U_cKnTdxtCR3axlrUN-E8OFv2Ohgz2_TTPIlbDLKrcfrvjCo6AyGrVoex9F5B0Pp_ikU_z51gs-RaWLRYEjLBqhF87HV8mQMz2GYNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجار بزرگ در ادلب سوریه
🔴
منابع سوری از انفجار در یک انبار مهمات در شهر «بنش» واقع در شمال استان ادلب خبر دادند که تاکنون دلیل آن مشخص نشده
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/144903" target="_blank">📅 14:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144902">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
وزیر آموزش‌وپرورش: مدارس حضوری آغاز می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/144902" target="_blank">📅 14:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144901">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilRJ-Zpa_pdyP5TT7h51kjLg72CR_x3BMJT6Wm8DVsiL2FR1dXS4Nh8L23mMkA-jVIYgjPPFcyglvnwXGLOom51XIyulpQvWi_6lfVJpiQcCDFon5viL7_4JvjX4Y51-6rKikd8DP3jxlQIWN3tDIm5VFYtVoshqEAZDro6CeLMCClGQAz9-D4a8CdkT37Ky-yiG-8Fw2Ngo9vsr9ugSDsR6Es4QYCdNf-3K0QvdBGo3eHVNPIiRwVIZOKW5y45TRBB_lnv_MRoLFMLLhRODHlOfpeK6ZRkMM0UGmCBmdOgYmfLAO-bKoej5ADtS1qB6tatTXZn9YPYDZ6F5biXyZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / پست جدید ترامپ در تروث سوشال : ترامپ قصد داره بعد از اولین درگیری و تبادل آتش با ایران توی چند هفته اخیر، قراره یه ضربه «سخت» به ایران بزنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/144901" target="_blank">📅 13:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144900">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
هر یک دلار 214,000 تومان شد !
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/144900" target="_blank">📅 13:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144897">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a32155ad92.mp4?token=lqeZkhBrZzDI25SZSw_X0gY9RsLoYkEXdMiULtzph1g46VncTZ9rL_F57XkieZBwhoztGMqPh5_MdAjPgNAjune04DvPpRunkChnGKjaMM5lRniF5M9rCHRJfTrlCRv_Sel9BmRhxi3ySHJUfByrOME527Ziai_uEde4FYZiTU5Hd2ayUBuUiwnD2qFExB30R2J3hmqWJgC9qgb0BnHzsEBARyecwB8JQBeUY8Jp5dVBXBS6aEh0Y2Xumc79_eCuZacfKSXD3LzKRtkdYcmrSarhE-Ga1IPzVj0idG6SO_mAD8qHwisrDYuFqDqkejXWBE-fpxrTRALjYD2nBuT4EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a32155ad92.mp4?token=lqeZkhBrZzDI25SZSw_X0gY9RsLoYkEXdMiULtzph1g46VncTZ9rL_F57XkieZBwhoztGMqPh5_MdAjPgNAjune04DvPpRunkChnGKjaMM5lRniF5M9rCHRJfTrlCRv_Sel9BmRhxi3ySHJUfByrOME527Ziai_uEde4FYZiTU5Hd2ayUBuUiwnD2qFExB30R2J3hmqWJgC9qgb0BnHzsEBARyecwB8JQBeUY8Jp5dVBXBS6aEh0Y2Xumc79_eCuZacfKSXD3LzKRtkdYcmrSarhE-Ga1IPzVj0idG6SO_mAD8qHwisrDYuFqDqkejXWBE-fpxrTRALjYD2nBuT4EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای دولتی سوریه پس از انحلال نیروهای دموکراتیک سوریه (SDF)، وارد شهر حسکه شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/144897" target="_blank">📅 13:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144896">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRPQltAcovhfviyzrdv3QKEQ-meb1FxJ45SvAD7dPMS2-WjIZpY0kmhjZkQcxOF0MldP0Fdb6aVqTLTU-NBJMuWUOsCjFxt0SeVqBkX91D-ql0gChOY0Z7-flaLvVbzTIE4UGizc5QCibNPfJSkPdHVKcYAmUfOxjR3UToVApm8x7oyW3lB0sfM49tB27AHypruBjjKAvtgflhCmvm_zy3BR2mzNMS1ZkaRHHBiGDankN7D9g3Kbb8SOPRjihrplwPVa2nE_7ha1XYT3Sz25U9yQxSjg6w8zT7VW3Lpkkvbgks-9x5wl8sv0YHPcxnLxsufyiF6m1diLa93MZhF9XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد مهاجری: رئیس صداوسیما در دیدار برخی مسئولان در برابر انتقادات تند فقط برّ و برّ نگاه می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/144896" target="_blank">📅 13:42 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144894">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60357d956a.mov?token=k1RI_0wwoijSvmlEm1oyyBnMWVyNDKp9AUSAqw4vxi6FpOCz-S2nkawKc8hTAt5aVFf6CBr9lwfbNIxvEfocy9TiQsKB9OJMm7gtSt6e8LCM_OC9pw5ihg2a1ySfLI7M1jByAXinHYAvE9Rx75HXVMjRZok5P2b-jIOp56Bv0xIQ0lGKKDDEIfsDYPUnDvdvCMzV3QT8vP6ysxWWfltUWHILGW0CsArBJg3Fv4Y1HMpt1KYmRSdfqKbOZngDgiWqZi0dCvbO1fYuAq6TJaA832bZFku0DKu4WKV1PdFJp4f2B75o14arpVpsUNLNz_LL9kAShOJNA-iktPYkUMKAKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60357d956a.mov?token=k1RI_0wwoijSvmlEm1oyyBnMWVyNDKp9AUSAqw4vxi6FpOCz-S2nkawKc8hTAt5aVFf6CBr9lwfbNIxvEfocy9TiQsKB9OJMm7gtSt6e8LCM_OC9pw5ihg2a1ySfLI7M1jByAXinHYAvE9Rx75HXVMjRZok5P2b-jIOp56Bv0xIQ0lGKKDDEIfsDYPUnDvdvCMzV3QT8vP6ysxWWfltUWHILGW0CsArBJg3Fv4Y1HMpt1KYmRSdfqKbOZngDgiWqZi0dCvbO1fYuAq6TJaA832bZFku0DKu4WKV1PdFJp4f2B75o14arpVpsUNLNz_LL9kAShOJNA-iktPYkUMKAKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موشک های بالستیک اسکندر-ام روسیه، مجهز به سر جنگی خوشه‌ای، کی‌یف را هدف قرار دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/144894" target="_blank">📅 13:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144893">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
نتانیاهو: «من نزدیک به ۴۰ سال است که با مسئله ایران درگیر بوده‌ام.
🔴
زمان زیادی طول کشید تا بتوانم نهادهای امنیتی خودمان را متقاعد کنم که مستقیماً با خودِ ایران مقابله کنند.
🔴
همچنین زمان زیادی طول کشید تا ایالات متحده را به این درک برسانم.
🔴
توانستم این کار را انجام دهم، چون نزدیک به هزار ساعت در تلویزیون‌های آمریکا حضور پیدا کردم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/144893" target="_blank">📅 13:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144892">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
سخنگوی دولت درباره هشدار اقتصادی رئیس مجلس: قالیباف جنگ را به خوبی می‌فهمد و می‌داند که معنای مقاومت چیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/144892" target="_blank">📅 13:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144891">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل: ۷۰ درصد نوار غزه ویران شده، بدون تونل یا زیرساخت، و تحت کنترل کامل ماست
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/144891" target="_blank">📅 13:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144890">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
نخست‌وزیر پاکستان: پاکستان در موضوع جنگ علیه ایران، قویاً به دنبال صلح است و به ماموریت خود برای میانجی‌گری ادامه می‌دهد
🔴
تنها راهکار دیپلماسی است
🔴
اجرای تفاهم‌نامه اسلام‌آباد به برقراری صلح کمک بزرگی می‌کند
🔴
مسدود شدن مسیر‌های حمل و نقل که ناشی از جنگ است، معیشت جهانی را به لرزه درآورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/144890" target="_blank">📅 13:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144889">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
وزیر ارتش اسرائیل، گالانت: یک مقام ارشد از جنبش حماس دستگیر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/144889" target="_blank">📅 13:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144888">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
رئیس سرویس فدرال همکاری نظامی-فنی روسیه: روسیه و ایران برنامه گسترده‌ای برای همکاری نظامی دارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/144888" target="_blank">📅 13:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144887">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAtxXMOlXeN6PSVEf5cBp19tRyg3iD4ABn7XRg7n49sUkIBC733PPqo4dV-6j-Ux17LliUutPaSm2uPI7HpoEkqrtDa0AgMhcPPVWUkTosaxyX1-V3kCsEtJtu1OLvpavzm1IwucYY5QgqfsXbL0mPt6ii7Wko1pBDVMlWuIScgMeOblgXCNJd6klHq5rUCwuMeGppuEbGLfzGLlmVslhyJZiORelD4mkwNkBwC9PQtThYCZ0kn_SgrlX7624tQ4mBDy4tZV4326y3YlZByv5b3Ly3PKZeRKcXx1mM7ZjBBBcATp75zHsSmpD76zxEkeNUdi9GhYdfEqy-vLb69p8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در جریان معاملات شاخص کل بورس با افزایش ۳۶ هزار و ۱۱ واحد در سطح ۶ میلیون و ۵۸۳ واحدی قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/144887" target="_blank">📅 13:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144886">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
منابع خبری از حمله توپخانه‌ای اسرائیل به اطراف شهرک «حولا» در جنوب لبنان خبر دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/144886" target="_blank">📅 13:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144885">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
وزارت بهداشت: کرونا دوباره شیوع پیدا کرده و تو هفته اخیر افزایش آمار مبتلایان رو داشتیم.
🔴
بهداشت رو رعایت کنید و در فضاهای بسته از تهویه استفاده کنید
🔴
پ.ن : به ایران خوش آمدید
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/144885" target="_blank">📅 12:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144884">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
کره جنوبی و عربستان به شهروندان خود ابزارهای هوش مصنوعی رایگان می‌دهند
🔴
دولت کره جنوبی در برنامه‌ای تازه دسترسی رایگان و نامحدود به هوش مصنوعی را برای تمام جمعیت این کشور فعال می‌کند. این ابزارها با اتصال به سامانه‌های دولتی در مواردی مانند خدمات درمانی، امور مالیاتی و آموزش به کار گرفته می‌شوند و بیش از ۵۱۲ پردازنده پیشرفته برای پردازش مدل‌های بومی در اختیار شرکت‌های مجری قرار می‌گیرد.
🔴
هم‌زمان شرکت ادوبی اعلام کرده که در قراردادی ۴ میلیارد دلاری با عربستان، امکان استفاده ۱۲ ماهه رایگان از امکانات هوش مصنوعی خود را برای بیش از ۲۷ میلیون شهروند این کشور فراهم می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/144884" target="_blank">📅 12:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144883">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5QmOaXRpLXMr9kI2uOjl2JQi0RqKqWmq8_16oxYLf32zWz9LrVtlnkK7bGXd4F1_iSo6h4-loCt4Ah13lbwbLxnopd4tk7wswqSBKNf7VEzAZd-XoGuUmI5C6_vqQipfQK7L4DGAtkF6HnIPJ2hhmtliwq3Ox5j7nl2Dn3s2AK4DaAB-1Fkv0sDgyRqkxpPW8i9QNKWHjwJqEpFqH5yn1Bb6R049HzraeVsBNN4Ny7wFM_BFL7snXdfzyZ9WLA6IRDQAGqj0FhG_CAKiNXkd-7-BpXelvuJYLP54BGpEoG5Zbyq_7k_iTg_Y-2qyrKJluhetqQWLY6b1HPu0KNLjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبویان: اکنون بهترین زمان برای حمله پیش‌دستانه به منافع آمریکا است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/144883" target="_blank">📅 12:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144882">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkjJbCpu595YtOXy0QnWPSXCjtZgf6BhCJ7v-Iv_QHe-P8zfXLjSYf7V-UN3okLdP8-CJaPUwAYKCmw9CICvbbQZ4C5B8sAnKTcTY94GKjcgSzuBHfQ9SVDleb0NcLKSFhfoZedlq6bf-NEMl4ag4yuM_r8jx-jlS24lZbgq4TnsktwjeU5V6FepF6UTWo7V3GN8TOlJ44pT_LTHGGgHSAcDuCL-R-_8asY3bSq51ZhuhLwS5CeA8GbfrcPexQe6k1dC8bdAzjoeNUiROoez9sLE-pfnKnd9b-dQJ2xnz-4N1EhqbQjjBNK0qtef5ogLVpe7pd7u-cVl7IgBWFbOLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری پر بازدید در ۲۴ساعت اخیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/144882" target="_blank">📅 12:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144881">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
دلار در تهران از 212 هزار تومان عبور کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/144881" target="_blank">📅 12:26 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144880">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvtbiJbEbC5_gdCIBIZAbuDjM_zl6KVuji0Ccm4SsPPqh7_fZbTHebBhs0-pNgOZfzzS76KHxn9vwTTiNaL5kouRvvv_mXyDXGFZlPwFbRF6CTrTvIiJUhq0s3o5HSL0dJaytjb_Z22QWfGbrVAVs2qeNIaVo8JtiwbLmNt26d58YKOgC4B_wUweI_fp7SNT_pI8gi6BqJ8ZjBMU39kb-58NfSrySq1TswUBV3Uau-eZ-scoNvZs52j19Q15FsWO3Mv_Qou5UhMP08N_eh3VaWxYJDkaWLWgjQ7Ney-qbfxnv3lXAEWwOcApoYXJ2jO4St1DnRdWRap9KZCwgFOmsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تتلو بزودی آزاد میشه
🔴
تتلو از زندان: از وطن فروشا و پهلوی متنفرم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/144880" target="_blank">📅 12:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144879">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f11a7dde2d.mp4?token=oZfwvw3dXk054KPGhkVqP9W0q0yHIEXEuwr3kPXG4_S51O3S4Rs4ISLuFIqGh7rj3odZ6ImoOdpWYVr-xoEAV0f2FMIHtgwQCfc9P_m2PVsdkvg8JsOw85i0bVrwpjbfST8H7Uj_hJF03yW7lPfED3__7cfWU2vEhgj3agLE3z4wCpBR6xudBlwyspkaM9vg902S_-nL8xiH9JxvDHqSi4SX3BnZ_ZbmhskOjL-QN7YQUo1Wo5p6lBwrFcyf2hL2WbH-H0mbMQM1pAkEcvcWHaynWKi8LfG5eQw6VS0kF6smM09kT_KkR9KC7zNwMGiY12KUk2eh139q7bxo1wP2ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f11a7dde2d.mp4?token=oZfwvw3dXk054KPGhkVqP9W0q0yHIEXEuwr3kPXG4_S51O3S4Rs4ISLuFIqGh7rj3odZ6ImoOdpWYVr-xoEAV0f2FMIHtgwQCfc9P_m2PVsdkvg8JsOw85i0bVrwpjbfST8H7Uj_hJF03yW7lPfED3__7cfWU2vEhgj3agLE3z4wCpBR6xudBlwyspkaM9vg902S_-nL8xiH9JxvDHqSi4SX3BnZ_ZbmhskOjL-QN7YQUo1Wo5p6lBwrFcyf2hL2WbH-H0mbMQM1pAkEcvcWHaynWKi8LfG5eQw6VS0kF6smM09kT_KkR9KC7zNwMGiY12KUk2eh139q7bxo1wP2ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه ورود دکتر مسعود پزشکیان به اجلاس شانگهای پلاس
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/144879" target="_blank">📅 12:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144878">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
وزیر نیرو: اگر جنگ اتفاق نمی‌افتاد و بعضی نیروگاه‌ها از دست نمی‌رفتند، امروز در نقطه تراز قرار داشتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/144878" target="_blank">📅 11:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144877">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
وزیر علوم: آغاز نیمسال تحصیلی نو ورودها احتمالاً در آبان‌ماه خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/144877" target="_blank">📅 11:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144876">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
رویترز: دور جدید حملات میان ایران و آمریکا، قیمت نفت خام را به بالای ۹۱ دلار در هر بشکه رسانده و نگرانی‌ها درباره تداوم تورم را احیا کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/144876" target="_blank">📅 11:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144875">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/737291ddef.mp4?token=b1tDyrdjCphlTORCLtnbgqS8GzZdvI2wUlXfjOqqj48pDnsIPPxTahMh_KlxS0jLz_mY79derP-ZKWGG05WeE_1um9ybkkX-2JCLXAJXQnbGWU9tp5z5AFgFLzMDm9mNFBaruli6teKpVe8iVI9Y5G8j4katDYgZiNox2nOvMk4xh9FoMjMqpiSvV7DRpgzj6tYrq1mGticWq1kpE-vZq1FU-2KFV4cqepMwNx8vvMcY8cSs-2XhgBythfibCWueVFtCCy4Ae-MN3OQrnAwm4oIYRzWtVGgI2hteoDajX7HbGZliqGyjVRg7qq5AtRasY0TFtxWnM0of9FCW2ToHrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/737291ddef.mp4?token=b1tDyrdjCphlTORCLtnbgqS8GzZdvI2wUlXfjOqqj48pDnsIPPxTahMh_KlxS0jLz_mY79derP-ZKWGG05WeE_1um9ybkkX-2JCLXAJXQnbGWU9tp5z5AFgFLzMDm9mNFBaruli6teKpVe8iVI9Y5G8j4katDYgZiNox2nOvMk4xh9FoMjMqpiSvV7DRpgzj6tYrq1mGticWq1kpE-vZq1FU-2KFV4cqepMwNx8vvMcY8cSs-2XhgBythfibCWueVFtCCy4Ae-MN3OQrnAwm4oIYRzWtVGgI2hteoDajX7HbGZliqGyjVRg7qq5AtRasY0TFtxWnM0of9FCW2ToHrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی دولت: برای تأمین سوخت نیروگاه‌ها و افزایش تاب‌آوری شبکه گاز برنامه‌ریزی کرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/144875" target="_blank">📅 11:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144874">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
سخنگوی دولت: افزایش قیمت دلار، نتیجه تحریم‌های ظالمانه آمریکاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/144874" target="_blank">📅 11:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144873">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
مهاجرانی: دولت هیچ برنامه‌ای برای واقعی کردن قیمت‌ها ندارد چون درآمدها واقعی نیستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/144873" target="_blank">📅 11:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144872">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e2e303fbd.mp4?token=DUkjt__SdwSb9aOPyIwxCFJnA7Ist08HbU-6MLacU8H88PhcLZXbjjsIOcP9sDMRIO05jApvx2YM7QgfOjJ54mLanNXy7OQn7L6WCyZHeIcWWDzffY3mhRACYw_3EqgynZf7XVqvinzBunaiHr-ub2dGbp4sDbEP4E5gnFMWq3L5ctBdiPTu5sSKdtn9_726Hz-AU3AIod2_0Vn0guXoOH3jYCcqkrJRK3DPHx3jPw7tVVZT5DRoXDJK4MQGoiMdhUFbNSPrudfU5hP90OXgcs6GKgi0YtqY1EMdoGWRkYuoj0kpsc7ZI8bsGYGjKbLlnX8j4gTeQx8AM9QbNPm8yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e2e303fbd.mp4?token=DUkjt__SdwSb9aOPyIwxCFJnA7Ist08HbU-6MLacU8H88PhcLZXbjjsIOcP9sDMRIO05jApvx2YM7QgfOjJ54mLanNXy7OQn7L6WCyZHeIcWWDzffY3mhRACYw_3EqgynZf7XVqvinzBunaiHr-ub2dGbp4sDbEP4E5gnFMWq3L5ctBdiPTu5sSKdtn9_726Hz-AU3AIod2_0Vn0guXoOH3jYCcqkrJRK3DPHx3jPw7tVVZT5DRoXDJK4MQGoiMdhUFbNSPrudfU5hP90OXgcs6GKgi0YtqY1EMdoGWRkYuoj0kpsc7ZI8bsGYGjKbLlnX8j4gTeQx8AM9QbNPm8yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی دولت: غیرحضوری شدن مدارس امسال شایعه است؛ برنامه دولت به حضوری بودن مدارس است مگر اینکه اتفاقی بیافتد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/144872" target="_blank">📅 11:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144871">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b2d996101.mp4?token=avN-iO4PydDNHWWfT_-MWlrtG6LhIgpJghT-D4z-XbwW1x4zX9yMI7CVnz3iI5Aqqt1ABusbHn94R20yhMsRi0dn6GML7axTDdtVnADA6f9twd1-ZiRuC9U6uHHPn-1qdPPmZPT_PD_UrZ1ZEM574eNwx9JPnUXCRAiu-bkKd_J-IKTDVIe4HqT9KPVV83R3pIluyeIbtTbOz8zgELtVpxR20gQgZSG9OpmGOjzS1W-S094YEqR_jR-UJFHb-Ok0bcv9RNw3PxX0hYnCaBxGqBVO1CspjCOSUqKgT4i7teHP75upKOw-657uspWUC51mke9pPgKsi11sxCgDxaMqPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b2d996101.mp4?token=avN-iO4PydDNHWWfT_-MWlrtG6LhIgpJghT-D4z-XbwW1x4zX9yMI7CVnz3iI5Aqqt1ABusbHn94R20yhMsRi0dn6GML7axTDdtVnADA6f9twd1-ZiRuC9U6uHHPn-1qdPPmZPT_PD_UrZ1ZEM574eNwx9JPnUXCRAiu-bkKd_J-IKTDVIe4HqT9KPVV83R3pIluyeIbtTbOz8zgELtVpxR20gQgZSG9OpmGOjzS1W-S094YEqR_jR-UJFHb-Ok0bcv9RNw3PxX0hYnCaBxGqBVO1CspjCOSUqKgT4i7teHP75upKOw-657uspWUC51mke9pPgKsi11sxCgDxaMqPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: ایران پیشنهاد ایجاد «مرکز راهبردی مطالعات امنیتی» و «مجمع پارلمانی کشور‌های عضو شانگهای» را ارائه داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/144871" target="_blank">📅 11:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144870">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
رویترز: داده‌های ردیابی دریایی نشان می‌دهد تردد کشتی‌های حامل کالا از تنگه هرمز همچنان در سطح پایینی قرار دارد؛ به‌طوری که شمار کشتی‌های عبوری به حدود ۵ فروند رسیده است، در حالی که میانگین آن طی ۱۰ روز گذشته حدود ۱۴ فروند بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/144870" target="_blank">📅 11:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144869">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
افزایش ۳ دلاری قیمت نفت و رسیدن به ۹۱ دلار در هر بشکه
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/144869" target="_blank">📅 10:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144868">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
همتی، رئیس بانک مرکزی: احتمال وقوع ابرتورم را ضعیف می‌دانم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/144868" target="_blank">📅 10:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144867">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/449457076d.mp4?token=eA1xVw4YYeFIyVH_tjWl2XNzlCGlDFT-e6t8xsM5r82aBn_Lc4XC_gKhQAIspiF1y7Egsox4LMzRB5sJ_7ZuU0db7Fo3jecERlBZS-217A58kTb3vH1svGvD0MSeT6_dNEBbSCPlt0lrIpQ-XCG1JMgnUnABd-_rjbSrtFYjzUAhbLVfAipTvAg2fBHcP7O745UYDol_vegtT-d4AaaxAfqsf_bw8IMHbFZzTFvEoE7P36nrFRy9fPC1OEQuLNAc5YbEyVDO7Pryltw_ZDXwwA3JT74ufle85cY_bzRPN9ZGNDIqE5xfDXQzMgMExQzRBF4zZ-U_1eQxN2BHu6iR_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/449457076d.mp4?token=eA1xVw4YYeFIyVH_tjWl2XNzlCGlDFT-e6t8xsM5r82aBn_Lc4XC_gKhQAIspiF1y7Egsox4LMzRB5sJ_7ZuU0db7Fo3jecERlBZS-217A58kTb3vH1svGvD0MSeT6_dNEBbSCPlt0lrIpQ-XCG1JMgnUnABd-_rjbSrtFYjzUAhbLVfAipTvAg2fBHcP7O745UYDol_vegtT-d4AaaxAfqsf_bw8IMHbFZzTFvEoE7P36nrFRy9fPC1OEQuLNAc5YbEyVDO7Pryltw_ZDXwwA3JT74ufle85cY_bzRPN9ZGNDIqE5xfDXQzMgMExQzRBF4zZ-U_1eQxN2BHu6iR_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امضای اسناد تفاهم توسط روسای سازمان همکاری شانگهای
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/144867" target="_blank">📅 10:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144866">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
فارس : سید مجتبی خامنه ای دستور عفو ۲۵۰۰ زندانی رو صادر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/144866" target="_blank">📅 10:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144865">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GaGNktn5ScROJmF4EVvRGf2d7i_lE4pyE94UPu8TkW_UIKjT-QG_ZEInL2IzgZSBPLTxwBCBMpQehW6cPgwEghu53auETTk-SeSm4U3y8i6kg6wV1B0wK1Y5ZqrYDw3puzqoMQurk_rpmN7V6kEjKyUc_TYdd2pS_mwGWV1AFlIJxkuR89B4X7ZfvH62WPhEtQMVJfQGniJXHC-uRkDFebXvs9jhW4FNv2GLbVnzgMxEkfLrB9WdtLZSX_50wvYMQk3VTrtU5LoLg2Euq5vmYkloIs8E4HGTpNMHV4EzdE3Lv5zjqmtdFAYazEoelV7R1KF2qWNVYQfDDOwxooY2Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: هالیوود یک فاجعه کامل و تمام‌عیار است! برخلاف اسمش، کار بسیار کمی انجام می‌دهد. هیچ انگیزه‌ای برای حضور در آنجا وجود ندارد و به کالیفرنیا آسیب زیادی می‌رساند. جان و بسیاری دیگر در این صنعت، پیشنهاد می‌کنند که ما مشوق‌های مالیاتی فدرال را اجرا کنیم تا تجارت تولید فیلم و تلویزیون خود را دوباره عالی کنیم، شاید بزرگتر از همیشه!
🔴
مقدار پولی که برای مشوق‌های مالیاتی هزینه می‌شود، ده برابر پولی است که به خزانه خزانه‌داری سرازیر می‌شود. جلساتی با رهبران هر دو حزب در حال برگزاری است تا این کار انجام شود. این کار باید دو حزبی باشد، به خصوص از آنجایی که پول زیادی در کالیفرنیا و سایر ایالت‌های عمدتاً آبی از دست می‌رود.
🔴
من پیشنهاد می‌کنم که جمهوری‌خواهان و دموکرات‌ها دور هم جمع شوند و فوراً قانونی را برای نجات تجارت فیلم، تلویزیون و سرگرمی در آمریکا تدوین کنند.
🔴
کنگره باید فوراً یک مشوق تولید فدرال را برای ایجاد مشاغل سرگرمی در آمریکا تصویب کند. این کار می‌تواند به سرعت، دقیق، کارآمد و مهم‌تر از همه، به نفع همه آمریکا باشد.
🔴
آنچه ما روی پرده نقره‌ای سینما تماشا می‌کنیم باید در جایی ساخته شود که زمانی پایتخت سینما و تصاویر متحرک جهان بود. بیایید این کار را انجام دهیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/144865" target="_blank">📅 10:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144864">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICXArrR9RNT_F7Q27GyV5hjojfPavLx4m2_rAockvum2tAA6LiTVOrY7hYmUy2oAaAT_GGQnpANZgdMiiW4Uwp_uE72w0fkt_eb8ojEXeNExFL70IqFOMk5FhMi_4-nF5nthcesbcRFAOABmpga1Ao1yVBgLKSjZygKlpx6xBMbsAyEIs0Ls-3KvalkhvrgJNwh84eH8qLPsf5yXZ97GRK_LjNJMc-vAZjz-YRIHrm_4y80zqae4hGU210XfjnFnBd4l84S7CB1e6SXd9JiYYGvLoVahleupF0wgeKIspqWh3SZiFeaAh8Aa1X3Z4gGbH-x_08d5fXnlAXvziaraJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برگزاری آزمون‌های تافل و GRE رسماً در ایران متوقف شد
🔴
مؤسسه ETS در صفحه رسمی ثبت‌نام آزمون TOEFL iBT اعلام کرد که در راستای رعایت تغییر اخیر در مقررات وزارت خزانه‌داری آمریکا (OFAC) برگزاری آزمون‌های TOEFL و GRE در ایران متوقف شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/144864" target="_blank">📅 10:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144863">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f8e698f2.mp4?token=rgDUH-Xt_NxFlZ0sNYq1o5tJqxtrKhS5LstVuSIAhPRbQeG0l_KwAL6cpItgxbZ10Cd8jjG9fiCaPwq1VYlIJrcPI4c5m96qkRpkTG64TpWR-vaZOpv7wR0zi0l_0LOeMNnZE4l5Tmbv9DltYnkgX5n1X2VqlMwsTPOJxAFt7d6lQqtP-NXAyLYhy_JQ7u6UhTp1MPWwzGqaykbf4cAbnE_UXJ6OQpVMJ2jeR5Y-O0nEzXDY22GZ0eRqnM0psj0yYgwKglBIFCsm-r0BwLZliJOkS7t7-5zsbTNJkZSJzDVG03IHz73QNd8fzFQ6pCiThEyPoYUk_gPxWiS2e5xOqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f8e698f2.mp4?token=rgDUH-Xt_NxFlZ0sNYq1o5tJqxtrKhS5LstVuSIAhPRbQeG0l_KwAL6cpItgxbZ10Cd8jjG9fiCaPwq1VYlIJrcPI4c5m96qkRpkTG64TpWR-vaZOpv7wR0zi0l_0LOeMNnZE4l5Tmbv9DltYnkgX5n1X2VqlMwsTPOJxAFt7d6lQqtP-NXAyLYhy_JQ7u6UhTp1MPWwzGqaykbf4cAbnE_UXJ6OQpVMJ2jeR5Y-O0nEzXDY22GZ0eRqnM0psj0yYgwKglBIFCsm-r0BwLZliJOkS7t7-5zsbTNJkZSJzDVG03IHz73QNd8fzFQ6pCiThEyPoYUk_gPxWiS2e5xOqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
منابع خبری اعلام کردند با کشف ۸۴ جسد دیگر، تعداد کشته‌های سیل ناگهانی نپال و چین از ۱۰۰۰ نفر فراتر رفته است و ۴۴۶۲ نفر همچنان مفقودند.
🔴
اجساد تا صدها کیلومتر پایین‌تر از مرکز سیل، حمل می‌شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/144863" target="_blank">📅 10:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144862">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGHND_ZqPgGm0ndrEEu4VUupKuIMD6ZmEh2dDCpApq4ohdl0J0tc7Ix8VKreAa8dSIW83hJTqkCTt6cOz-kmdmfdjPnucYaXW-RTTcxym2XM2XIShoVycgORO-GRb1Wpr6VY7kfk71hnlUtr2IOUHSFZrhjzysAXGvfL0GuH0DcaEfRAKNIoJwIJPkA6u9F4VXkYS1NARBB_4S8ytOMu5VWfdIOSdYEwDv8KncDLih2Ye9mcggcl5m8R8o2jeJW2AazmgghC98HaBFiEu-UqXZtdxwoHLCv7_vbF9z-DWMzzQ1P_W49I2YGX6rTu-sDLwqmKrpYy_7lDt41nYtaU_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک پهپاد آمریکایی MQ-4C که از پایگاه هوایی موفق السلتی در اردن به پرواز درآمده، هم‌اکنون بر فراز خلیج فارس در حال پرواز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/144862" target="_blank">📅 10:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144861">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
جبلی خطاب به پزشکیان: دیدن صداوسیما افتخار است، کسی که نمی‌بیند از این افتخار به دور است!
🔴
پزشکیان پیش از این خطاب به جبلی گفته بود دیگر تلویزیون نگاه نمی‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/144861" target="_blank">📅 10:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144860">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
کشتی‌ای که دیشب به‌گزارش سازمان عملیات تجارت دریایی انگلیس در مسیر جنوبی تنگهٔ هرمز هدف ۳ پرتابه قرار گرفت، نفتکش غول‌پیکر عربستانی «سیدر» با ظرفیت حمل ۲ میلیون بشکه نفت بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/144860" target="_blank">📅 09:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144859">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aovfPZAnJQlUqs__zJim6m5uobxL2zI59hOHBL0z2rCgeHDPNOPHm_82bBUAokRWRdDOy2V9vlryRXW86Nd6lyMIaEBqkDi4ceLNc2rM50eNSG1mva3xMXsO-FqELsECnbaoHw_arZSHuLQ0lR_YDJypPRrUOCAsgSEjjj4Pa8y_xnII722bSVj1aHRADr6hy8YffpAxmrMQLdG70Z-DVve2jRUT1ubrlERpCrLldvz6Xl8ep6AoJKLAtqrNV9fA7SPyomNXpPVPql1iT0O1Sm8ZJTeh-reI3QKW1RoopLMq0dBNFrb-Aq4Pzz4Ma73wJMJHUNyy3-Kz5nLOGXWZlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیتر هگست، وزیر جنگ آمریکا
:
🇨🇦
(این واقعی است)
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/144859" target="_blank">📅 09:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144858">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
المیادین به نقل از یک منبع بلند پایه ایرانی: در پی حملات آمریکا به لارک، ایران ضربات سخت و دردناکی به پایگاه نظامی ایالات متحده در اردن وارد کرد
🔴
خود آمریکایی‌ها بیش از هر طرف دیگری از شدت و حجم ویرانی‌ای که پاسخ قاطع تهران بر جای گذاشته، آگاه هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/144858" target="_blank">📅 09:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144857">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
همتی خطاب به ترامپ: ارز داریم، به قدر کافی هم داریم، بازار ارز هم آرام خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/144857" target="_blank">📅 09:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144856">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXNdLA1yAGf6IfkO5VNKYuCyke2JaPMCLigGk4apNsKezrt4eWQ3zYFooEfbPHCTCwgTWmPEZZlXYQH7C21cIAw3zTx3sIrMcgcb-8K2G0CKXhoVb5TuVR3KmN6vJC2Fe1P_rQWGU7Hm5Bx7DanGkzk9QH4WgqetXn5H0DI0r6yzZf-0U6klAW638ZF0FN0-90aHW3L9mqPdYPUO3N1R65fjuZgItojycwniMqyXhw2SxL4hgaHYkW3f2i8DwPrIJ1epaDzO-Dpv6WzJ19wiZ6RLnrI2kHuZ5z7-l36U5fZHABoJSpxlgGN6ljFbG3_qiXAYGkfE5gw7UKyoxKbHVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جنگنده‌های ناتو که در مأموریت پلیس هوایی بالتیک حضور دارن، در واکنش به یک تهدید احتمالی در حریم هوایی لودزا، لتونی به پرواز درآمدن؛ این منطقه نزدیک مرز روسیه قرار داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/144856" target="_blank">📅 09:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144855">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCkAoOii9VZUqyCloI47LY-8J5fJdyTlvuyK2tnVEc2yzkBvGZEScQfyZg5Hb96ISHWDSLrTPjEWjQG7s9w4sGyTx9XMEM-UaUFdnIML6I-vb-lLCWbtVpFvGB3bcRTLw0FfSR2lG-WVtEv6cLgvfMdV8FMI-xieSKGmde4QTYHa7yf9JXSIY6lrzbxHPa-LEsC-I359-4jpHo0ccRH-aRL-J58Z7r7AbTXNK9hEmd62MMx_2C7yNFhbyN56xrQhT5lou6Fn0hHyN_Dmj45I5_05kpTz-wvCBRUhCVwyLS5Ytq0GovbBwNOPp6d-iBxeIUG5L79ItJO-B6Rpdpftrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش وال‌استریت ژورنال، شرکت North American Blue Energy Partners به رهبری آلخاندرو بتانکورت قصد داره طی سال‌های آینده بیش از ۵۰ دکل حفاری در میادین نفتی ونزوئلا مستقر کنه تا تولید نفت رو به‌شدت افزایش بده؛ این کار بخشی از توافق نفتی اخیر با آمریکاست.
🔴
این شرکت می‌خواد تا پایان ۲۰۲۶ ۶ دکل فعال داشته باشه، در سال ۲۰۲۷ ۱۲ دکل دیگه اضافه کنه و از سال ۲۰۲۸ به بعد، ماهی دو دکل وارد مدار کنه تا در نهایت تعداد دکل‌ها به ۵۲ دستگاه برسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/144855" target="_blank">📅 09:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144854">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
پزشکیان در اجلاس سران سازمان همکاری‌ شانگهای: تداوم رویکردهای مبتنی بر زور نه‌تنها امنیت کشورها، بلکه ثبات منطقه و جهان را تهدید می‌کند.
🔴
شکست‌های سنگینی به آمریکا و اسرائیل تحمیل و پیروزی‌های درخشانی کسب کردیم
🔴
آمریکا به تعهدات تفاهم‌نامه برگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
🔴
پاسخ به تروریسم، افراط‌گرایی و تهدیدات نوظهور امنیتی، نیازمند تقویت ظرفیت‌های نهادی و کارشناسی سازمان است.
🔴
آمریکا به تفاهم‌نامه برگردد، ایران نیز عمل متقابل خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/144854" target="_blank">📅 09:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144853">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
پزشکیان در اجلاس سران سازمان همکاری‌ شانگهای: تحولات اخیر در منطقه غرب آسیا، ایران، لبنان، غزه، کرانه باختری بار دیگر نشان داد که بی‌توجهی به قواعد حقوق بین‌الملل و تداوم رویکردهای مبتنی بر زور و فشار، نه تنها امنیت کشورها، بلکه ثبات کل منطقه و جهان را تهدید می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/144853" target="_blank">📅 08:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144852">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gH1LBrQDC0XGsONRCLQJAavcD3su_FQHchaVHIWLvFVxAgptdyRNS3bbpz5QsM3LDesiJOnAUKIl_TSAkZXVEGeY9A9mNb_M9aauHaABCsbmxxXNDHWpFDBjPup4BN-n74M3eVw6GpbZDTmAvh_YjaqD4F3hHrCcSP6LNXKaJbB5eRqhDpmuqnUFUy6pZsxaOm3_6sulq5D0mL19KB_bZppXyuMCA1yej7qfHOm2HEaQaqpnnZpHqlDlhn5tVyi0z1lNYg1Ct2W-YTdolgxoXE_uT19lWvOVtV5KW7vRzc1MtJryTR5g2APtWYRmYx2bIsiWdbH2MJfAiSZ-Q-g7jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواشناسی: از امروز تو اکثر نقاط کشور دما کاهش پیدا میکنه و بعضی جاها تا ۱۰ درجه دمای هوا پایین میاد و کم کم آماده میشیم برای ورود موج سنگین بارندگی به کشور.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/144852" target="_blank">📅 08:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144851">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
جی دی ونس: دو شب پیش حملاتی در تنگه هرمز انجام شد؛ ایرانی‌ها در آستانه مین‌گذاری بودند
🔴
بخش قابل توجهی از اقدامات ما، با هدف تضمین جریان آزاد تجارت در تنگه انجام می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/144851" target="_blank">📅 08:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144850">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
آغاز سخنرانی دکتر پزشکیان در اجلاس شانگهای
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/144850" target="_blank">📅 08:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144849">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWXkb_dEtxHC5y3JBcjYFUHstqmdVvV-_4QWMesPJpZoJY15kmj_eouNWK6lDKHEDIGFRptc0AMwnfVkYCtiWxxdkgywZ3DLAkFDvHA2050EhMCSWxOUOwp9C831sTDqzS8Ec8h-Ds-0IG8IFsaF01iprwiwOpUsAuBzalc2ov0Jizr3t1PLkBNNWy1E4EChLW0Z5LdMt-HSFQeFPywmRj1ligh30gsJYKkuQl9iR9FKYr4ask-XEBmiHeRDoIr-A2PeeH8bIkniymkWZoCdc5yQPFzVU2qdrjk1vTxWk6ufPKYFJuXxQr5DI53VzprABOz-j2xFYZUoOocl0HbDPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دنیل دریسکول» معاون وزیر جنگ آمریکا در امور ارتش بعد از ماه‌ها اختلاف با «پیت هگزث» رئیس پنتاگون، بامداد سه‌شنبه از سمت خود کناره‌گیری کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/144849" target="_blank">📅 08:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144848">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFc02pHTJ6EBwjLNyl9WaGDSr5RoK35C6_ddYVbLTd3fVJkXpQvbO-6jG-FpYR1jSIANLdMQJzC9UxyBmy9mR4qV8LOeiyLr943xKdTR-Dy3i8UEy3D03qYqQ4FIkk8k1lTiA8TQ4LCN2Td2wSsOaf-jqlYKTvEnZa_Jn7Ob55ZTyAPu7vnBtGE8lsgNo0LB2mtvkgdZtwu-JnaDw8ZbIrc4qgqQm-F4N1Ds774hUh50vqM0D4KrBtZEF5ClJjhT101f56ZAYJmEx8OylCGo0KNmCaPjXAXg5DVifOdkS4ISjrkWr6ggyr2isHzdfPfPZZfR-rk0Upq1BgORNK5amg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک کشتی هم توسط ایران مورد حمله قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/alonews/144848" target="_blank">📅 02:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144847">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIkKWYyOqoTgyXEHtelSpb0Mh1MbGViYX9vNvuWZuUiWT5w1AmspFVeokkifp12PyjLcfJt9-ilacE_YVLzHZAlsda7dAmd9s1zHmgkQ5Shd6NxpHUJOfYS2yU9mXNN3js5Ts-2fQ2aEbjoqaHY72OAk4n7WxATiv3wnl9FbIIjJ8zCd_-qsAnxnUKJD7lu55vyJ_l3so8O2pgzGK3OSdMEFigj32Ep4UAkZZyJhNCgAiqa1t7OJDgynHxKQkgKNZPRYc9Nf01WWVAlFbNqNYAN8ulI-a3qcjPpvSdfyEAhn0ApHnSohUjOLrZbe7WNR09QQXoUBk7Q2MkoPEE6tkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کشتی ایرانی که از فرمان ایالات متحده سرپیچی کرد توسط  یک هواگرد آمریکایی مورد هدف قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/alonews/144847" target="_blank">📅 02:01 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

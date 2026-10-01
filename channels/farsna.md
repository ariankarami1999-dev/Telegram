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
<img src="https://cdn4.telesco.pe/file/FdIAWlFSCBICML9vV8hJlvgG7q5eTRbInBmhSXZ8CeCHBe-1Yn2uZo17fMFFT2FdIp3plK5Q2ZLL4lDSFc-7z-QuJTQEWREIve3hyqHfZUiOoJ5PvjhhKWUlGR0D9T9ro1BHsumxmM7sq6g5T5SR2OGen2q5mL-FYB93ckaz0aLDaKJ3OHfUbYFkzvYjIbGGY5zDHTF7whLr4fufr6Za5VH_jtoiwA7RIc98dCnJ0eJB219PKcHRqRjcd2AFiELjKe2TXX_957Da2e4CyV8W796AOe81JTjAl2hnng9W9C25k9qNrctRn_PrTnz9Vs2qYbiRc_N0M0kWdv9JLfbbGQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 22:39:44</div>
<hr>

<div class="tg-post" id="msg-465754">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feb3816caa.mp4?token=t4QeqUj1oc2N0yDbl7VAtui0wF0_CMRzEAUx7eOMa5PfPMGomjkOxg9z30EPnOAxwPmdZI_iADkBg2e_H1Xy2OpMco6ghbDzAnCysSVzLan-TTIzxH_AtjnUJ6FiAqeAWppWv-GKCQZLp_wUKS8wfvEStFu504eVfZTyeSC7NY_oW08RNVYIT11LuM9p8-OPl3kMWDvPBCf_LHOhbPmpB7bzZk4Dhe3G9rjTPZ_-UBzQK1dzjo7SindQWy1nuE4dXRpt5KN560j26GwFOJYJxzwE-QrIfh2KS5z5PeUYahzrbeN1eZkpmaDA4N1TzogN8RJY5Vr21tK13JLNyDKB3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feb3816caa.mp4?token=t4QeqUj1oc2N0yDbl7VAtui0wF0_CMRzEAUx7eOMa5PfPMGomjkOxg9z30EPnOAxwPmdZI_iADkBg2e_H1Xy2OpMco6ghbDzAnCysSVzLan-TTIzxH_AtjnUJ6FiAqeAWppWv-GKCQZLp_wUKS8wfvEStFu504eVfZTyeSC7NY_oW08RNVYIT11LuM9p8-OPl3kMWDvPBCf_LHOhbPmpB7bzZk4Dhe3G9rjTPZ_-UBzQK1dzjo7SindQWy1nuE4dXRpt5KN560j26GwFOJYJxzwE-QrIfh2KS5z5PeUYahzrbeN1eZkpmaDA4N1TzogN8RJY5Vr21tK13JLNyDKB3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خالی‌بندی با طلای مردم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/farsna/465754" target="_blank">📅 22:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465753">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‌ ‌عراقچی: مواضع ایران هیچ تغییری نکرده است
🔹
از چندین ساعت قبل ادعاهایی مطرح شده که با قاطعیت عرض می‌کنم که هیچ تغییری در مواضع ایران رخ نداده است.
🔹
شروط ما برای بازگشایی تنگه مشخص است. در خصوص سایر مسائل نیز موضع ما مشخص است.
🔹
درحال حاضر فقط موضوع تنگۀ…</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/farsna/465753" target="_blank">📅 22:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465751">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fbbcf0fa2.mp4?token=ShGszfMONgE4KCYCfwW2j9LCHuPropR3wulHtjLsVKcl0qnW_3TIYWj0H1o46A_OXVdjnbE87HMG8PAtKA-MdS4wYhMbBaSWpCuMdSGbkTj1-cB0hY0c0yGHlYTHJFG6__7QO_jhhDwHlYhUqlNV12vTcyqGp59DPN3B3ats6nfXFUrCCldHX_YZOQlSUH4xiy-ZhKxZmV9rtoVr-O5j92T54-QSYV3p7d2hKH6IRrXpaJzdlm9dxBcbGLAFNr_l0Y6mc5mHoeQp59FdD__RuV3ma6fTJYBUcoht66As1D08AjJGPqYmoD6odC1O6p5OR57oNsRQ3b5jcdZmRp7FwaNWi7SL2aY_6qpygVsePVao1Z4OrbXVErSWqLBQExP6gZLaYTMJh5G2vfXbm9fzXUgFEN3gXZVdr7WMOTa6s1bXB7aDMI47vHikd960KVrciF7i_BAWcbT2sjxJ--_sm46U6QYhN-jQy6NNKKdYjHhS0zsAGtmYnxo0e4KUenXyrvuXu8ahDiFIDSzWLtd60Bl8G6CnIFGbHJ1eSV2SuvWUdXEdMy2NzX8vAj3Q7wrjnjygGTX0YHquzZqO9-To2C1_RTZLdmuZPRbbxmWJc1mV4KPxNy5rWHA5pDIO2rOgufQy5lMImGC_uDkjakiYStFm7rlHQWvyYDbKU8dC6UE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fbbcf0fa2.mp4?token=ShGszfMONgE4KCYCfwW2j9LCHuPropR3wulHtjLsVKcl0qnW_3TIYWj0H1o46A_OXVdjnbE87HMG8PAtKA-MdS4wYhMbBaSWpCuMdSGbkTj1-cB0hY0c0yGHlYTHJFG6__7QO_jhhDwHlYhUqlNV12vTcyqGp59DPN3B3ats6nfXFUrCCldHX_YZOQlSUH4xiy-ZhKxZmV9rtoVr-O5j92T54-QSYV3p7d2hKH6IRrXpaJzdlm9dxBcbGLAFNr_l0Y6mc5mHoeQp59FdD__RuV3ma6fTJYBUcoht66As1D08AjJGPqYmoD6odC1O6p5OR57oNsRQ3b5jcdZmRp7FwaNWi7SL2aY_6qpygVsePVao1Z4OrbXVErSWqLBQExP6gZLaYTMJh5G2vfXbm9fzXUgFEN3gXZVdr7WMOTa6s1bXB7aDMI47vHikd960KVrciF7i_BAWcbT2sjxJ--_sm46U6QYhN-jQy6NNKKdYjHhS0zsAGtmYnxo0e4KUenXyrvuXu8ahDiFIDSzWLtd60Bl8G6CnIFGbHJ1eSV2SuvWUdXEdMy2NzX8vAj3Q7wrjnjygGTX0YHquzZqO9-To2C1_RTZLdmuZPRbbxmWJc1mV4KPxNy5rWHA5pDIO2rOgufQy5lMImGC_uDkjakiYStFm7rlHQWvyYDbKU8dC6UE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه پاسداران: در پاسخ به شهادت اسماعیل هنیه، سید حسن نصرالله و شهید نیلفروشان قلب اراضی اشغالی را هدف گرفتیم  @Farsna</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/farsna/465751" target="_blank">📅 22:19 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465750">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c68b1085a0.mp4?token=X-JwgNjphDKPlpjnU7jT9550xv4ycRTUZph6rWd6mrgQ1WR2RedZko3DwLkkL1AHB9COrmEFgHlPtt1UeNgqchZs9cFuqQzOVeNreeQYAF6ow2ImoKpIT-3OAD6D-qIkZfbOPdA-N0dnIQM15_zmALkSrPuulVyL5fy7p4MZofTP_xEJ5fPvmsL4nQdnkrJDmBzYwGlTpifmvrK0M-xE0sBdmCu1O1ItvqEEgNqEfHb5fy7Hi2vZBsr0en_gxuRjqQM8YCiTOeZunwL5uR9MVO9LwHD20Q_tdwuw1_EzNd3YrrgP1RCxig2aBU_aQRxu8p1hFS2_tjMFE-5xdwwd9YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c68b1085a0.mp4?token=X-JwgNjphDKPlpjnU7jT9550xv4ycRTUZph6rWd6mrgQ1WR2RedZko3DwLkkL1AHB9COrmEFgHlPtt1UeNgqchZs9cFuqQzOVeNreeQYAF6ow2ImoKpIT-3OAD6D-qIkZfbOPdA-N0dnIQM15_zmALkSrPuulVyL5fy7p4MZofTP_xEJ5fPvmsL4nQdnkrJDmBzYwGlTpifmvrK0M-xE0sBdmCu1O1ItvqEEgNqEfHb5fy7Hi2vZBsr0en_gxuRjqQM8YCiTOeZunwL5uR9MVO9LwHD20Q_tdwuw1_EzNd3YrrgP1RCxig2aBU_aQRxu8p1hFS2_tjMFE-5xdwwd9YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یمن تصاویر شکار مزدوران سعودی را منتشر کرد
🔹
یگان تک‌تیرانداز نیروهای مسلح یمن با انتشار تصاویری، از عملیات‌های خود علیه شمار قابل‌توجهی از نیروهای مزدور وابسته به سعودی، اعم از عناصر یمنی و سربازان سودانی در جبهه‌های جیزان خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/farsna/465750" target="_blank">📅 21:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465749">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10f37f482f.mp4?token=V55279ChSivcPMLH_l0Sm6fTvqE-aSjsGwJfYDO5-WZ1_UNme7i88g5PtoZozIPLHEYAkWKiqrmqRJFeEqqDFNcB9JWWHtEmTiQcpjOy-Ck6JObM31X8xH-2XjLp3vDmkEvQbt2xFxuZRAgRYvBrm5HQoOxmEY5ruwrGUQGQjUn-fABsVkg67-H5a1DrES0DdPFisyFP4n_voX9LfASW_3KJPwbtqtxgDHa37ftvToBJY9_xNSSERGgybrd6jbj23oQNfmR2ibGnpDgVbWb2lhDvQd8j1Xpk7qpUgMAnN9A7QpQNyajsuEqcJhXByAIFPompneOvn4QTham2LZWPUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10f37f482f.mp4?token=V55279ChSivcPMLH_l0Sm6fTvqE-aSjsGwJfYDO5-WZ1_UNme7i88g5PtoZozIPLHEYAkWKiqrmqRJFeEqqDFNcB9JWWHtEmTiQcpjOy-Ck6JObM31X8xH-2XjLp3vDmkEvQbt2xFxuZRAgRYvBrm5HQoOxmEY5ruwrGUQGQjUn-fABsVkg67-H5a1DrES0DdPFisyFP4n_voX9LfASW_3KJPwbtqtxgDHa37ftvToBJY9_xNSSERGgybrd6jbj23oQNfmR2ibGnpDgVbWb2lhDvQd8j1Xpk7qpUgMAnN9A7QpQNyajsuEqcJhXByAIFPompneOvn4QTham2LZWPUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین یکتا در شهر صور در جنوب لبنان: نگاه ما همان نگاه آقای شهید است؛ آمریکا از منطقه اخراج می‌شود و جوانان به‌زودی در بیت‌المقدس نماز می‌خوانند
🔹
آنچه امروز در جنوب لبنان می‌بینیم، روحیه پیروزی و مقاومت در میان مردم است.
@Farsna</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/farsna/465749" target="_blank">📅 21:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465748">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9ajTHBWCGTjVpKXm7HicwieBYj91qZF-PMrQgDDZ2jZs20OJ_WFdeO31O-FQn6rRnjmoVe-gdKNI69hx8XkNjdPCVIzVdIx_8mSrKrLfFUGHs-ZfwuuyJwEfsnXygOilC3AE5JXE_dpE89sZk1O5YA0n7qFlCwirpSuj30QiPQh895nBqWIpQ02lYcWPUIHdk6CFpuV9wtGZlt28Yioohok1LH9CN0hy09UMnhFwkAfWV8KTRM0tuOE6K9AjlZaDEpzlwOdGGkxHXYEJPzd6FjDCxhHf3ZnQZEIQep1U84HYJGvbe_7FD8osdjF1__bcAxv6HvTHTteMj3e5FJ5eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
پوتین: جهان از شجاعت و قهرمانی ملت ایران و مقاومت آن شگفت‌زده شده است.  @Farsna</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/farsna/465748" target="_blank">📅 21:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465747">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/465fb0908e.mp4?token=fbZfcWJFZ9kX7ye_b95c6h6FDBiOVz_Lny7j63qr-_Yj_XxYTJ0TmtTdnK0sUe-21yOFCK6r3eiiEBHQf9wbp1WpxNJvxryyiYrkcpahiZPEgHJte8EekkhZc1Bk0JGlHOOROvvXpruXYGVYwqXQXtir8kD_-KyueEO8qdQaqS1WuCa7nBReQKVdGDes1CM1O1XTx3IGA-_lGbc7IcB5KglzvEowNZi0_5oDjMxQcjSq9r9U89CN1-G7qQORCCML54Q_YNvlnYosG4Jwyf66jnfKSuRtXcZTsXUUqAsZU8w7qpwkt7_0KoNmQI62-JqW_aD0gMuYULw-9vwgEi7p1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/465fb0908e.mp4?token=fbZfcWJFZ9kX7ye_b95c6h6FDBiOVz_Lny7j63qr-_Yj_XxYTJ0TmtTdnK0sUe-21yOFCK6r3eiiEBHQf9wbp1WpxNJvxryyiYrkcpahiZPEgHJte8EekkhZc1Bk0JGlHOOROvvXpruXYGVYwqXQXtir8kD_-KyueEO8qdQaqS1WuCa7nBReQKVdGDes1CM1O1XTx3IGA-_lGbc7IcB5KglzvEowNZi0_5oDjMxQcjSq9r9U89CN1-G7qQORCCML54Q_YNvlnYosG4Jwyf66jnfKSuRtXcZTsXUUqAsZU8w7qpwkt7_0KoNmQI62-JqW_aD0gMuYULw-9vwgEi7p1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی بازگشت بدون پشیمانی هنرمندان به وطن، دغدغۀ عدالت و اجرای قانون در جامعه را بیدار می‌کند
@Farsna</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/465747" target="_blank">📅 21:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465746">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42b6b8f25a.mp4?token=FZJbt7kzFWjaVHccHs7MbRJCO74fcW5bGHAFrKaQmKxueFmoP0skcMhPuK8uhlO4x_WmE2Qlh3Zh8rpYw1gQqusKAIn9DaGCYc2j6FXzZ98-2evjHzz6fdxpA_Oi3LPZjUt9v7NbQkFhIioacfi8m-6aoNiLR5JK-fPHKb4OWOxKcqs-LUa3As-j8d-_hc7TwPkIUCSFm3wfgJhwc6O62Vqe9Ai29KB8XQRPqjqaIq2wU_n7ZS1UCVzFmVlMTKv-MeZvuDzSGUVJeMySGF3PExdpabHMEiAzzHPi6hZ_ctorQinNx90I3lM9e1nhaucbCKWm8TRf5MsXz_uAYAhGbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42b6b8f25a.mp4?token=FZJbt7kzFWjaVHccHs7MbRJCO74fcW5bGHAFrKaQmKxueFmoP0skcMhPuK8uhlO4x_WmE2Qlh3Zh8rpYw1gQqusKAIn9DaGCYc2j6FXzZ98-2evjHzz6fdxpA_Oi3LPZjUt9v7NbQkFhIioacfi8m-6aoNiLR5JK-fPHKb4OWOxKcqs-LUa3As-j8d-_hc7TwPkIUCSFm3wfgJhwc6O62Vqe9Ai29KB8XQRPqjqaIq2wU_n7ZS1UCVzFmVlMTKv-MeZvuDzSGUVJeMySGF3PExdpabHMEiAzzHPi6hZ_ctorQinNx90I3lM9e1nhaucbCKWm8TRf5MsXz_uAYAhGbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پوتین: پیشنهاد ما برای انتقال اورانیوم ذخیره‌شدۀ ایران به روسیه همچنان پابرجاست.   @Farsna</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/465746" target="_blank">📅 21:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465745">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba0e7d1f59.mp4?token=Dm-ax7P3VcYzWbmMAAT6yVgIIiZHnVFdNDRYESkJxd5taE_ouvWQDqzTCVzara7nqVW3Kgaj327gtUjW5DYoeRQum_03unz88KzXog-6ghB0uK1tDSNsP1NCPAmtc91gabFsLtn7st1Ziv0t1oYtieUcMFbe4PauQoZch5u2yBtpBM9i7POSVBIyuIwAFfJVFYeBfSCRQ_DKYLe9YLvVpZipEz5QmRMA0TU9zScYz8Htti5aWOSas2G3njw8spyfSmiPZXGj4I2sR5FcZcgtkgh1gyXHudXOw47LJDo4dLs_V8lpi-UuE_stvIlk4RFImEgXMmjAfHhHfBMuFIGjtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba0e7d1f59.mp4?token=Dm-ax7P3VcYzWbmMAAT6yVgIIiZHnVFdNDRYESkJxd5taE_ouvWQDqzTCVzara7nqVW3Kgaj327gtUjW5DYoeRQum_03unz88KzXog-6ghB0uK1tDSNsP1NCPAmtc91gabFsLtn7st1Ziv0t1oYtieUcMFbe4PauQoZch5u2yBtpBM9i7POSVBIyuIwAFfJVFYeBfSCRQ_DKYLe9YLvVpZipEz5QmRMA0TU9zScYz8Htti5aWOSas2G3njw8spyfSmiPZXGj4I2sR5FcZcgtkgh1gyXHudXOw47LJDo4dLs_V8lpi-UuE_stvIlk4RFImEgXMmjAfHhHfBMuFIGjtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دومین پادگان آموزش نظامی «جان‌فدا» در تهران آماده می‌شود
🔹
پس از افتتاح نخستین محل آموزش نظامی پویش «جان فدا» در میدان امام حسین(ع)، آماده‌سازی دومین محل برگزاری این آموزش‌ها در میدان هفت‌تیر تهران آغاز شده است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/farsna/465745" target="_blank">📅 21:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465744">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">منبع نظامی یمنی: اتهام حملۀ پهپادی به مدینه پوچ و بی‌اساس است
🔹
یک منبع نظامی یمنی در واکنش به ادعای عربستان سعودی دربارۀ هدف قرار گرفتن نیروگاه برق «طیبه» در مدینه منوره را بی‌اساس خواند.
🔹
او در گفت‌وگو با خبرگزاری سبأنت، افزود: عربستان با طرح این روایت تازه تلاش می‌کند ناکامی خود در پیشبرد روایت قبلی درباره حمله به مکه را پنهان کند.
🔹
این منبع نظامی همچنین تأکید کرد نیروهای مسلح یمن در برابر این بهتان سعودی سکوت نخواهند کرد و حق پاسخ به این اتهامات واهی را برای خود محفوظ می‌دانند.
@Farsna</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/farsna/465744" target="_blank">📅 20:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465743">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">تحریم‌های جدید آمریکا علیه ایران
🔹
آمریکا نام ۲ فرد و ۲۸ شرکت را به فهرست تحریم‌ها علیه ایران اضافه کرد.  @Farsna</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/farsna/465743" target="_blank">📅 20:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465742">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caf4a9a059.mp4?token=chkaP-BH7-K1ujZpQqLez-0GdgczBJjHkG8NFn1qSWx2xpeLcrUG9nVBFeARvUEdJ8PO0e7h0-HwUEPdoXofnJa3kuOMExVVXduGpOhMGnMKn5UFL2oMcT0kd6ZGQxYFQ_mLdwHJORg2xY4t2IQ2FxWBZup_imy9h0P84QIOdTEBHKrGkl6kccdHAMBP3a3fJikMMB3C52uAGrXg9Lj6nGlLPx3aq9FitdJaOC9XM6srHiFgjmhty8oYRCXGU508tPYcMPqyGddqmLw1zNnPBxyHyJq3xCPQjPKdH3lmm6ar5O856Tcwr2BdS-imnqtlr0vBeGok9BGhdDOTSMq2tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caf4a9a059.mp4?token=chkaP-BH7-K1ujZpQqLez-0GdgczBJjHkG8NFn1qSWx2xpeLcrUG9nVBFeARvUEdJ8PO0e7h0-HwUEPdoXofnJa3kuOMExVVXduGpOhMGnMKn5UFL2oMcT0kd6ZGQxYFQ_mLdwHJORg2xY4t2IQ2FxWBZup_imy9h0P84QIOdTEBHKrGkl6kccdHAMBP3a3fJikMMB3C52uAGrXg9Lj6nGlLPx3aq9FitdJaOC9XM6srHiFgjmhty8oYRCXGU508tPYcMPqyGddqmLw1zNnPBxyHyJq3xCPQjPKdH3lmm6ar5O856Tcwr2BdS-imnqtlr0vBeGok9BGhdDOTSMq2tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بهنام ابوالقاسم‌پور در لبنان: به‌عنوان نمایندهٔ ورزشکاران به دیدار خانواده‌های شهدا رفتیم و انگشتر متبرک آیت‌الله سیدمجتبی خامنه‌ای را به آن‌ها تقدیم کردیم.
🔹
تازه از نزدیک فهمیدم مردم لبنان با چه شرایطی زندگی می‌کنند و چقدر نسبت به ایرانی‌ها محبت دارند.
@Farsna</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/465742" target="_blank">📅 20:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465741">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTw7QJTjVhpkw-1PalkIJxcAxtU36eM4O71cl2HgfPvIyu-jW7w6I_OZu5mEKJ73gbvMevW3g_vBaGZzTNvCkEHhKOIZRrVJrWJ4a3PydAUJSnpq7P5GtZrJB8oxpLRJkH-t2qcq5x4FNWtRfrw8x56R-cM3r1pSXjE3z-Tk_1cYlncuMwaYo33Kgeqj7YRRwwgk0XngUHZ6MY5NfXzpGmovrjx2KN3rMdse_RnCFy5lbZ6FEGbx-VEU6TIbJrN5eWAH2QJ03hVUyTtfC7qbeJ_Dt4srA9Ev8wsPt-YN1jy-D6CDVuAkairB5jjL2LRO5Nsg8UV9yvY7q2vARyvWQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت دوباره به ۱۰۰ دلار رسید و ترامپ‌ حرف‌های تکراری‌اش را تکرار کرد
🔹
رئیس‌جمهور آمریکا: ایران نمی‌تواند سلاح هسته‌ای داشته باشد و آنها با این موافق هستند.
🔹
بعداز اتمام جنگ با ایران قیمت نفت افت قابل توجهی خواهد کرد.
🔹
میزان نفتی که درحال حاضر از تنگۀ هرمز عبور می‌کند بیشتر از قبل‌از جنگ است.
@Farsna</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/465741" target="_blank">📅 20:26 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465740">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd58b284a4.mp4?token=bT7kL4KwR8ZQdnOmyfOuH6heXV8dtIsb_rmQKpwKo8GiDy3oOGsUIGnCajvD5KJcdil5iJnD4SDW4iwjt7BsS9BYwcm3AZxDbsG9JDglm_i1yRB1iTptRSqrfn4Drm4SZOo_1Cxbcy3InhjKO6fT3r0yUezQfi9EB1w7-btuHdbZcVrlc813v7Scu8k-3Y7OhAbnr-yy9Fkz9IKTT1yKjoESWDkk6mxRAYtyQIfyiNkQXIkgB117NSsvc-z8r5BWOYQSXYwVgJHqhggPubv_KY0xWOZUGV5dCk5v64EY0kDw2bqUwkkzl6TsipPYCUVomGBjKU7dQgeKLNUeL7npkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd58b284a4.mp4?token=bT7kL4KwR8ZQdnOmyfOuH6heXV8dtIsb_rmQKpwKo8GiDy3oOGsUIGnCajvD5KJcdil5iJnD4SDW4iwjt7BsS9BYwcm3AZxDbsG9JDglm_i1yRB1iTptRSqrfn4Drm4SZOo_1Cxbcy3InhjKO6fT3r0yUezQfi9EB1w7-btuHdbZcVrlc813v7Scu8k-3Y7OhAbnr-yy9Fkz9IKTT1yKjoESWDkk6mxRAYtyQIfyiNkQXIkgB117NSsvc-z8r5BWOYQSXYwVgJHqhggPubv_KY0xWOZUGV5dCk5v64EY0kDw2bqUwkkzl6TsipPYCUVomGBjKU7dQgeKLNUeL7npkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پوتین: ما آغازگر درگیری با اوکراین نبودیم بلکه آنها درگیری را شروع کردند
🔹
ناتو نباید روس‌ستیزی را در اوکراین ترویج می‌کرد. غربی ها خود را مرکز دنیا می‌دانند.
🔹
اصل توسل به زور رویکرد بازیگران بزرگ بین‌المللی است و باید از آن جلوگیری شود.  @Farsna</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/465740" target="_blank">📅 20:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465739">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تحریم‌های جدید آمریکا علیه ایران
🔹
آمریکا نام ۲ فرد و ۲۸ شرکت را به فهرست تحریم‌ها علیه ایران اضافه کرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/465739" target="_blank">📅 20:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465738">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7b7e32e56.mp4?token=giSoGoxJbrXZAZerfdNaZLzdSTRdPgX4QAv7UIhaiJ6fmhAS7iCbGVJFQsfCVfYVRiBFBNIoee0YxEM6c2Q11DZjqYWAD3FaX77wau1lCTsaZ61ICT8qg4Lt5FZjHyD7zjSpL_1ambMhWxV9e7MEMEEgJOkisXIqr3dVYs9TyGA6FvBkYsRkYw0KyrLgYfw4J_zRAPkmH492qI6vhgrWSSZs-nrX4NKYaVhe6J8FOHFmXicG9JGtYUtVXkRieaB7o6RcvEQ4ouzhpoGrW_sn1I7_R-s2vDAqxJFdKFAiuFZmrVZc8n1XRsAR-ObkTtmzvZkCwrHROPVwqQ6gLJbJVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7b7e32e56.mp4?token=giSoGoxJbrXZAZerfdNaZLzdSTRdPgX4QAv7UIhaiJ6fmhAS7iCbGVJFQsfCVfYVRiBFBNIoee0YxEM6c2Q11DZjqYWAD3FaX77wau1lCTsaZ61ICT8qg4Lt5FZjHyD7zjSpL_1ambMhWxV9e7MEMEEgJOkisXIqr3dVYs9TyGA6FvBkYsRkYw0KyrLgYfw4J_zRAPkmH492qI6vhgrWSSZs-nrX4NKYaVhe6J8FOHFmXicG9JGtYUtVXkRieaB7o6RcvEQ4ouzhpoGrW_sn1I7_R-s2vDAqxJFdKFAiuFZmrVZc8n1XRsAR-ObkTtmzvZkCwrHROPVwqQ6gLJbJVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پوتین: ما آغازگر درگیری با اوکراین
نبودیم بلکه آنها درگیری را شروع کردند
🔹
ناتو نباید روس‌ستیزی را در اوکراین ترویج می‌کرد. غربی ها خود را مرکز دنیا می‌دانند.
🔹
اصل توسل به زور رویکرد بازیگران بزرگ بین‌المللی است و باید از آن جلوگیری شود.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/465738" target="_blank">📅 19:40 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465737">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e690d320e1.mp4?token=I77iL5DTQh_L8V_HqkGJnNVwv7QbB6X5UB8-NemE4NpHeD5Huh4Hc07PE_b4saYBbK4VEOHLrXm_BggxaTRf4wwzp2Ps2Z5fOO2SB3fzQr4T2sRrw8xzjNr6w32r7PgoxKY0OdDm96RnuK-4R6OZj-IXA9xZwgp4gUS1WE11ynknIAmRNeElXado8G2i7gMQAUa_Er7u6m-nk4ktEG8Z8wZjwCDrvD97x7AIqr6FvYrHR-kzKjgj9BIEVTKz1o5DnUMlRr0BEhdfyQc6AQ1j_Dqh6-0i1grlR03zQC0Pj2ga8nPOeMurZ1OGtmw2N-YTXmPV6rluYd_Jhckkn4p3Bn-RfDBs2f-S0kHlj88XjrRAqV_XyEYgkqC22Z0QHg6vhtXN74EGGsFZOhNBhkuu0RSPv4yHJTyHrjLg7W2-9W48FqgnoJrzMRiKIMvz1LuURXXYpDeWlMljXSSZGQ7Do0oVo-bOQvhYn0ZxgLC05ussXhrWyVquJHmt6Ka1M6Zv2NHLMOiVixHTi9i1oPE95ImB9vf8hUHGY5Y5DxKQv0FxTJF00h0LF0VPg28aKumfdoaKm0RCo7ZkK0nKDcRNcejg1Uy2Hc3d4gHCH7OK3UprqdkSnYXaPB7kDo0z7fO_MX7I82gmmBJr_lnSUbNWzbVmrVZqoKY9XKW4tcowHAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e690d320e1.mp4?token=I77iL5DTQh_L8V_HqkGJnNVwv7QbB6X5UB8-NemE4NpHeD5Huh4Hc07PE_b4saYBbK4VEOHLrXm_BggxaTRf4wwzp2Ps2Z5fOO2SB3fzQr4T2sRrw8xzjNr6w32r7PgoxKY0OdDm96RnuK-4R6OZj-IXA9xZwgp4gUS1WE11ynknIAmRNeElXado8G2i7gMQAUa_Er7u6m-nk4ktEG8Z8wZjwCDrvD97x7AIqr6FvYrHR-kzKjgj9BIEVTKz1o5DnUMlRr0BEhdfyQc6AQ1j_Dqh6-0i1grlR03zQC0Pj2ga8nPOeMurZ1OGtmw2N-YTXmPV6rluYd_Jhckkn4p3Bn-RfDBs2f-S0kHlj88XjrRAqV_XyEYgkqC22Z0QHg6vhtXN74EGGsFZOhNBhkuu0RSPv4yHJTyHrjLg7W2-9W48FqgnoJrzMRiKIMvz1LuURXXYpDeWlMljXSSZGQ7Do0oVo-bOQvhYn0ZxgLC05ussXhrWyVquJHmt6Ka1M6Zv2NHLMOiVixHTi9i1oPE95ImB9vf8hUHGY5Y5DxKQv0FxTJF00h0LF0VPg28aKumfdoaKm0RCo7ZkK0nKDcRNcejg1Uy2Hc3d4gHCH7OK3UprqdkSnYXaPB7kDo0z7fO_MX7I82gmmBJr_lnSUbNWzbVmrVZqoKY9XKW4tcowHAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازداشت مأمور متخلف به‌خاطر رفتار غیرقانونی با ۲ نوجوان سنندجی
🔹
دادستان نظامی کردستان: یکی از ماموران در شهر سنندج با نوجوانی که بدون گواهینامه رانندگی می‌کرده، برخورد غیرحرفه‌ای و نامناسب داشته.
🔹
با وجود اعلام رضایت پدر دانش‌آموزان، مامور متخلف پس از طی مراحل قانونی بازداشت و به زندان معرفی شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/465737" target="_blank">📅 19:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465735">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس‌ پرس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qt7pYnHby6TtF3AzlxenA7Xyapf43WlrY0THN3aq0rZ6pXoKAEQhSRouryBpLp2c5u4f1jt31MTPiIHNElnzdRewaRJ3utnYahUfXPphRzO3S3qEfNv4Tt8afo1yXn_hT9yC4VfwaqF3sHgpeUOVbxIskn2K8KXaY8uKnIi9SMUAoPyNIDFgskbQK8yjnKqEOatTiHJC628WsPME76lV_yjYMrHZB8Jn--bAgqc-4L_0X0ezUTZ8mZR6XRG7qg9a1BGc2Q7_GPHxufHcfSsVGBP-sOg3Pbr5ppQ6aaYQs0l5wyYD7iykbS6PVNtjm1jPQFelWdF9kQG7LvV03ea8JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gLlMvHVY34ncgKorAejV5_2UAPkLQd647dgp26Ul77g8pbfQBze3SgYCJn4XH-k9mhJcoaYfV7_ZyLpyIuA6fYv4-vKAHhdjGCDuVZoa3YnM25W_z97GDfba-WiEuCR8dJKJWaP-pqTXdKAIHuwpMk5PkPIXJJKAmC1wJc74OCv6wtmV3h3cQ3FLDu_TEhCJugZPtU0YkGo2FtIWwZDKnwaBh-OuJKqmNB6k6Y1v0LMJpr9H34ZUPrgR0bxxZb95U-1ZirhD-UFaHEcCiHjpYIsFEHow3dT00IN9I71EvHsMwcpCpohXbVevCV51zswLt12-iOvkoFV8U5msJL-QxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔸
مس ایران در بهار و تابستان | ۲
🔰
کل استخراج از ۱۸۴ میلیون تن گذشت، تولید کنسانتره مس از ۸۱۱هزار تن
🔻
کارنامه عملیاتی شرکت ملی صنایع مس ایران در نیمه نخست سال ۱۴۰۵ از رشد تولید در شاخص‌های اصلی حکایت دارد؛ به‌طوری‌که حجم کل استخراج به بیش از ۱۸۴ میلیون تن و تولید کنسانتره مس به ۸۱۱هزار و ۶۷۶ تن رسید و در چند شاخص نیز عملکرد شرکت بالاتر از برنامه مصوب ثبت شد.
🔹
بررسی عملکرد شش‌ماهه شرکت ملی صنایع مس ایران نشان می‌دهد حجم کل استخراج تا پایان شهریورماه به ۱۸۴ میلیون و ۲۵۸هزار تن رسیده است؛ رقمی که در مقایسه با ۱۷۷ میلیون و ۴۷۴هزار تن در مدت مشابه سال گذشته، رشد ۴درصدی را نشان می‌دهد.
🔹
استخراج سنگ سولفوری نیز در این مدت به ۳۵ میلیون و ۸۵۴هزار تن رسید که ۲درصد بالاتر از برنامه مصوب و ۶درصد بیشتر از رقم ۳۳ میلیون و ۷۵۳هزار تن در مدت مشابه سال گذشته است.
ادامه خبر در مس‌پرس:
https://mespress.ir/x6TL
@mespress_ir</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/465735" target="_blank">📅 19:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465734">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzGHotTjlHgciwaMD4Ad06nmhZxzaAadvAMLaPMUfyls8Ek-B2nl9VvbYJlGrz-VieSKib_dfqBveh7Lnrae9V6QldhMDt8LdPTSZDH48iuz3vFa_FXVLKCnlMsZNPs1eeAKgsCoqo1U0vHLELklVHC1_OotJNTEFEjIra8uLuFFLF36XI4IJDRTSIbX6R38UarlfUFSNcoBLR--XEq2skcfCQ87F2ZpoIK0h7BwNRM4v94q11JuZ_pQN0uf5PSMMYVki37JIUiB-c4lNeXB38NJr647fTNi9Mp92rZ_Ehtd5jXT1JxVM6O7mEx2DRKCBvh0ZhcmCQEM2Xsc0y3j6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرداخت تسهیلات ازدواج بانک پارسیان به حدود 11 هزار و 500 عروس و داماد در نیمه نخست سال
بانک پارسیان با هدف هموارسازی مسیرآغاز زندگی مشترک برای جوانان، در نیمه نخست سال 1405، عملکرد درخشانی در حوزه حمایت از خانواده‌ها از خود نشان داد.</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/farsna/465734" target="_blank">📅 19:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465733">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/465733" target="_blank">📅 19:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465732">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lG0mGhD5Er_eiczEaZPVV9q-6fp0ylga5H0xlcqMD0fmA3WvmUE_viJTTsgGaVp-veWu0RCqVYFnZ2z7zHdRwfRC997mEn6xQDtKKvtiPYXb4BLINVEqHjpifzbEb-J_-nwgACe_TsgrP5Y6tGsiJnFee807x0tEPJRxP2VEz92mRZaOWqgbdPq1l0Bti1IeAjWLxIeUu65ebUF0Gro93tntI_LJ5Mtlfr1y-oHiLfGgDR1gs5k3LlFQyJ6ioBdT1hjvjlNPb7k7oei6UggVn9M0OEEuMyycGSC_ytU3wQOmVclmCuiUcOPIKMpo18yRfaCbX5VlW-BlUk45G3Fcag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا مقداری از پول فروش نفت را به عراق تحویل داد
🔹
دولت عراق اعلام کرد یک محموله دلار نقدی روز گذشته از آمریکا به دولت بغداد تحویل داده شده است.
🔹
حیدرالعبودی، سخنگوی دولت عراق گفته این محموله در چارچوب تفاهمات موجود با آمریکا و با هدف تداوم جریان ارز خارجی و تأمین نیازهای عراق به نقدینگی ارزی وارد کشور شده است.
🔸
دریافت دلار نقدی از آمریکا بابت فروش نفت، رویدادی است که بیش از هرچیزی عدم استقلال مالی عراق را نشان می‌دهد، به‌طوری‌که آمریکا پول نفت عراق را در یک حساب در بانک فدرال رزرو نیویورک نگهداری می‌کند و اگر بخواهد، عراق توان هزینه کردن یک دلار از این پول را نیز ندارد.
🔸
ارسال محموله‌های نقدی دلار نیز به شکل منظم و همیشگی نیست و طبق سابقه، آمریکا هر زمان بخواهد می‌تواند انتقال دلار به عراق را متوقف کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/465732" target="_blank">📅 19:19 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465731">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa30ede670.mp4?token=lkJ_ronaArgU-LnwPARfxEbpRYpSRCUeRSOMcD4pi-hVGNxMBPBWWutsAQiSMGBkWQrMwXmH7-zFliM_1j11H5avdFV52yAGBuNPQEfnnE4BTJMQmg_QPKT_S4MqGpc2SbEoOWH5aVSCdx-06hF1dztGIb7r5Wy_skREiQbhi-3SwYY6vYIa8NMjXJyiA2hqlFZ0_nU2D4-MxrMBKZyijfFnTYF_xPv_QrgvqTX92qlqQW1negNVcNNK7v5f6rvzPqsRCSzxOYg7B5vQsVrapuCQFenBOms-c3eh0VnTQrmNaOUVvqpbf0G7IcILniIc4jPVGvuixkOE_4VCCKWzoIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa30ede670.mp4?token=lkJ_ronaArgU-LnwPARfxEbpRYpSRCUeRSOMcD4pi-hVGNxMBPBWWutsAQiSMGBkWQrMwXmH7-zFliM_1j11H5avdFV52yAGBuNPQEfnnE4BTJMQmg_QPKT_S4MqGpc2SbEoOWH5aVSCdx-06hF1dztGIb7r5Wy_skREiQbhi-3SwYY6vYIa8NMjXJyiA2hqlFZ0_nU2D4-MxrMBKZyijfFnTYF_xPv_QrgvqTX92qlqQW1negNVcNNK7v5f6rvzPqsRCSzxOYg7B5vQsVrapuCQFenBOms-c3eh0VnTQrmNaOUVvqpbf0G7IcILniIc4jPVGvuixkOE_4VCCKWzoIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ژیلا صادقی در مزار گلزار شهدای لبنان: آنچه در جنت‌الزهرا دیده می‌شود تداعی‌کنندهٔ اتحاد و غیرت است؛ در ورودی این گلزار مشغول نصب تصویر رهبر معظم انقلاب هستند.
🔹
امیدواریم جشن پیروزی جبههٔ مقاومت را در کنار مردم لبنان برگزار کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/465731" target="_blank">📅 19:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465730">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abfa3096a2.mp4?token=Gsrmou6P9qDFwe16s9jBVFPj0Z8cNZODJj8vfCfW9GpEIdvgypg6bt5P7Xa8psrYacfReL_Sn5tiM9eDIPZyG4CXhSvIK5ocuU6G7-USPcO-eY-E9Qg9r1-SQUwqYNgYMTN67ihu0262fi6MCJim_R-1KT9P0gg6pYB9coYzJEQ_mCk1yJstnZQ2EhzDYgh7k5NQwOpueiHYbXjpq8ZZxWPGKbuDrFvEY97-Z7m_RQcXaJMCuLouuis-ENwqjnxx1uGN6_plCdLfBWxu3m8xcJ4UcZYWG9zBVQGtgmyT9P4zC_bartwX7IepaMTCIyJUhLHLizkvxC1obPZtg2ITwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abfa3096a2.mp4?token=Gsrmou6P9qDFwe16s9jBVFPj0Z8cNZODJj8vfCfW9GpEIdvgypg6bt5P7Xa8psrYacfReL_Sn5tiM9eDIPZyG4CXhSvIK5ocuU6G7-USPcO-eY-E9Qg9r1-SQUwqYNgYMTN67ihu0262fi6MCJim_R-1KT9P0gg6pYB9coYzJEQ_mCk1yJstnZQ2EhzDYgh7k5NQwOpueiHYbXjpq8ZZxWPGKbuDrFvEY97-Z7m_RQcXaJMCuLouuis-ENwqjnxx1uGN6_plCdLfBWxu3m8xcJ4UcZYWG9zBVQGtgmyT9P4zC_bartwX7IepaMTCIyJUhLHLizkvxC1obPZtg2ITwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
قدرت‌نمایی جان‌فدایان در اصفهان
🔹
هزاران نفر جان‌فدا عصر امروز در اصفهان به خیابان آمدند تا آمادگی خود را برای دفاع از ایران اسلامی به جهانیان اعلام کنند.  عکس: حمیدرضا نیکومرام @Farsna</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/farsna/465730" target="_blank">📅 19:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465729">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4ade31890.mp4?token=htCoS-xeWs8y6gJL_RDGC0UrjDiCbEcf19HL0v2B3M4XPUBrKjIl5_OWQin6cc04F_jPCWa2Z49pfGF5K-c_dJrduDuKf2XnnYd-I8pKNkq4Im0M6fHI2cnF0d5ZdiR7l8Z36Mg3tSb78ZC4EBLX9OLGcRm2V5uaPjYPWbI5CHSXnmlZOHhjT74jREbCkPm83voJHgncD7uEt9qw4KFABDhSQNF5SPMdhTtdrzyzjb5PD-SauI1t7lhsxKX5HGkKjzWs4YjA4xj8F8W4YslQVVWrrdvFVTwOG5ILRT0rUzp_hyWPOoaIB7q3MnmbaevnGT4PyJ1az1Q9K-bNbJw18g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4ade31890.mp4?token=htCoS-xeWs8y6gJL_RDGC0UrjDiCbEcf19HL0v2B3M4XPUBrKjIl5_OWQin6cc04F_jPCWa2Z49pfGF5K-c_dJrduDuKf2XnnYd-I8pKNkq4Im0M6fHI2cnF0d5ZdiR7l8Z36Mg3tSb78ZC4EBLX9OLGcRm2V5uaPjYPWbI5CHSXnmlZOHhjT74jREbCkPm83voJHgncD7uEt9qw4KFABDhSQNF5SPMdhTtdrzyzjb5PD-SauI1t7lhsxKX5HGkKjzWs4YjA4xj8F8W4YslQVVWrrdvFVTwOG5ILRT0rUzp_hyWPOoaIB7q3MnmbaevnGT4PyJ1az1Q9K-bNbJw18g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام پناهیان در دیدار با خانواده شهید در لبنان: بدون اعلام قبلی وارد خانه این شهید شدیم؛ مادرش گفت «دیشب پسرم را خواب دیدم و امروز شما مهمان من شدید».  @Farsna</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/465729" target="_blank">📅 18:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465728">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDEdxxj2XUOm10RJE-LnMVr5WHSJeEGkaAiYDOKFS_qz098Ost4CQHAJiGj1GvLFkiFdD98ewoMdaLIsiULOBndq1H4mxI26judRLtWEiAzDNRHj6MHDi1hZoCmIxpJCkoJNTTtcaZEaK_lcj46rw-kYQcG3od2NuQx_a-hdr5dvfn7DDizwPBgE1ZkE9OZbmN3nAYNioiXhwpTToL57PYu_k0yXKADRmxmp2WqKj9ZHCc_Ge6ak2FOqaiFfcvJe9L7h8PJ1vmm-PKtx_PAskdyMCyuLs6bTONEJQyjuGe4wXpa_zY5IZF4ugKKzVwLgPhHriNy3-JNYOjsl18fOUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
رژۀ بزرگ الحشدالشعبی به‌مناسبت خروج ارتش آمریکا از عراق
🔹
بغداد، پایتخت عراق عصر امروز شاهد رژه بزرگ نیروهای الحشدالشعبی به‌مناسبت «روز حاکمیت» و خروج نیروهای نظامی آمریکایی از عراق بود.
🔹
در این مراسم، تصاویر و تابوت‌های نمادین شهدا بر روی خودورها حمل شد…</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/465728" target="_blank">📅 18:44 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465727">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuNF9E8CZT2cs2GIZH0vBI-LeQyVjt8bDZr4aqK8mTWjcoYqCCxxFDiMkw_7Ynfh3JtNhv0ofq1H2nwFwHVmVe6FqIxwN6qsD3rsj6mWjsU5zqeR3MzULQdwijr8ZNHV0aAKVccGXIrAiJebw5awXFBasRnkksvVnYO_TlubGaBUSPvWhAzaUjdWwNcXBMXvr6EKnWkpVhaNBzIgGr1VHA5bn-iioM0Fjkszvf4xb9bbasSABXDcKA2PV_nk8-UldAx9h5DWLqB0jz7DvweVHvMZMWFdmVsar-g86PJXoTpihZZevgrBtGo7lcEAbHqKQBemm1H24gC-x-JZMTMuow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرواز روس‌ها به خلیج‌فارس از آسمان ایران
🔹
شرکت هواپیمایی آئروفلوت روسیه پروازهای خود در مسیر مسکو-دبی را با عبور از ایران را از سر گرفت؛ مسیری که نخستین پرواز آن پس از توقف، امروز پنجشنبه ۹ مهرماه از آسمان ایران انجام شد.
🔹
سخنگوی سازمان هواپیمایی هم می‌گوید پروازهای روسیه به ایران و عبوری به‌طور کامل برقرار است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/465727" target="_blank">📅 18:40 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465726">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XouldBNB7-dO2YdUObs2vybtzCi5MumWdXAKWK9qZChgjJWBrBi3gDPAM7h1E24iORDw0158IffJ2W7eoXRyoKVEDPez68Wmoo8nU-dWaAk5yY9d527JbBmWeHQP8vy0C5Xu2GBOCKRP853kApcu8k-LjWYEwqyagKNSyImSPwA93ZELUFn-kz2kg_vgjSJjnLxmRphx0vV_oOyoeLXh_ATUqIeeD6sfLuURn5Z28lYip3Y-vpzT4llJ7wqO1QpD-TCrbKiVBsfORyASDJll6t3-UzoRc4icTYBZCoupboXPz24MoiIpKyOZJq-4DgyoIZIyxabZtd81rIpvtb8XWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائب: جان‌فدا بزرگ‌ترین پویش دفاعی در تاریخ جنگ‌های دنیاست
🔹
رئیس سازمان بسیج: بزرگ‌ترین ارتش‌های دنیا ظرفیت و استعداد مشخصی دارند و در میدان‌های جنگ، نیروهای دشمن با فرسایش فکری، روحی و جسمی مواجه می‌شوند، اما بسیجیان جان‌فدا در مواجهه با خطرات، شاداب‌تر و سلحشورتر می‌شوند.
🔹
پویش «جان‌فدا» انعکاس جنبه‌ای از بعثت و برانگیختگی مردم ایران است و این پویش را می‌توان بزرگ‌ترین پویش دفاعی در تاریخ جنگ‌های دنیا دانست.
🔹
این حضور، حاکمیت ایران بر تنگۀ هرمز را تثبیت می‌کند و به دشمنان اعلام می‌کند تا زمانی که خواسته‌های ملت ایران تحقق پیدا نکند، تنگه بازشدنی نخواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/465726" target="_blank">📅 18:24 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465719">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HD8q5RWXFmMb4GZflNDClmnrOaFMO2AJx3wGppkMrf0XYSocT1OLGtx_Xtv6YIawJADtNB9IVNz7ouIRDqbkLN4lZJgAgQ8OCtTEeXtxFZJJ7aOrAc5cIt0Uy6XXrAikAXQoL3blOXe3f_nDhgycJrq_pEyHkD8X4h3UHajfL_SdBAnVaJIi_a922sFK5vyysS6uhJLrmOdLG6VsQTS__-QjbA3RAiDxJ1mlDehxddcbGsOD7DmoCj-ZCwfBLiU1NUsb9GTDeNi2wwpc34GMUWye1Q0bdKiT6RltboediXoK25juZv1ngvNIqPGVOqEcYQ0E0x8-fF73_-zPkGu6LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iYICjclaF0z77HzUyvHp9YZSEV-MBNOFaDQCiy7tM3UWtR57vK_2wCllJEXiAXMrS21Kmv6hLYnG0_rxS5l9zfhwCQMd567sHfnbdGsRr2jq_1XQvXPAXPF4ONWwMCt7nBVW_mHS5pqeqV21uGMd9-WJTsVJbfRoa7-GVlAOI7S5q9ja1qw-GG1QNcoTAqCRbQqi_4BIC-XQ9kHnhtiW1yziY7E_OocbWec2WfZdO2q9OYfhps1ft4WOW8bHUKHJUnjmzBBYtQj46GNGCBxz0UEJuvKpFnH1TV6f8t3Lzn2WDyHOHCX5M75e5WY9mY8hkuAPOBW8StkrJi8DGwnHkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YINg-rdaDFbnC4sS2-zj1AqkiD-N0rdeM49TJhlP9iiMt87gunDaYLDG_Mnq0kNu36Unb_EMi2krOZPwe1yWAMa8_BOB4NA5sCaLwZFRMeUL2xhqYxd6RdKm2s8BqNcohYL9ATQwu6qhXKB1x5E_nsaOVGKB8aCZxvbZ7DNZwxZiagRqRFEmSsuFGs0ZsOuGuVuOgp_Rbf-3yFbeWuTi-xj--ep0WGGz_AriR42y_lCm-lJmfI9dtpu0aArXE1JP4G3E0V0Putq6VYBhrNTbsB6GVzD1LDrW3qRkIBVFC9PwsXBAQE76pzL6gtpCINwJe5Lh-2NdhgDOhA4IL9gLmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G_kUzuWu35ZSzdJJmuylM8oAxmnLPLN013biY4GUaEt-X4UIoa1XZL5y5uSsrIC_av2UPfoo77jnDm2fFAAeGqRyjD8g5QAM4pLsAKGTKYiHefRjcJm2az8diPq7c5vr_nAOcBkyviPgnI-10WOEM2MR5U8Jg7wJybC_RiDIXpsNZFlqiNYGPcqlWMF4CCo2cnqnPfKtuXOVOnMw1MCwGHAtdxaMErqVG_5wDEuyWsoFK7qwv9L3FG2M6N-8Usa09GMrj-phurFwerUIm9mjpg-U1oNLkLmO6_tufAyuwCmGK-EJGHw6ZufNSL15_bAlu22L3gkLm3mDvmAqhlW0Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ja2YujYzKaWZLRz5YxZr3QgUK26_2iWZRs1uYxs0a2S6p3Jr1-k0KaIghxKCmY6pG096_UOZWfRmvSWzL6GJia2YDTNq6SGos6LZiD2juOLA146COtfEGrLoL7E29zQw_rrl-hc3EJjPUE4FrIh85AkCQ-NJNqL4QRTzlEIwcJPUMY5B8aBITWuo5enSqC7_giEmFPiHSI238OgNzA178BaxUK3Jw2E2IOWbm2wqjbvZ6skbGlfGzBpQDysIsf4NY_dHrEZBVy0CtelvMZfZv00BO5rA9x8oejbpNppNJz1FJ2Ner4xsyLr0G_cDQifKpAvB6jvf9Gur4i-hk8t7hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hbysXjwZUz9BG5yGKGWN0In9XZtq4YZ7U51Qp3y7HoQfd25uk_EK5-DjcvFGo03eBEF-dYrrUAAyoMMggRl5K3SykGIF_YjCZ8Ji0kwxwf08CgwMBQzzJPzZjgJoWuZqHjJ7TmOrUFmy527Rq2XNaMC3mhwHgSuQXLUtrs8c-dPj7v1Yt-q1YNfx4FZggoWX1IyTx1sPaLtVFElz4W8kTb5Uo6iwD70WNISMsoE_nOBP5zau8QEIQrshl8JC88ghAw6h0uzo4Cxs_KzUo4WNQsZwmTqcrRWW5s7GmL-y05CwN2l00s6NJ3fvB2GdMXjNYMbrdVcJnXscODN8OVRlhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T2mvfOw8L4Eo8uyWrEAK-9oQFrUzh5rMU3BZnfMGItaq-GUbPb8ZDvPJoJoeqcWW0KXwcfR_MFrgYpIz_mH0TO0xiY1Dxuz1DIvXJ78XdieowidS4KCHBQTgEJdKtZXKJfuKeCZCzbQ3GftcX_mxHNJz7l1KGVo60UDjfL-dWxtoBrpk7SVwGjIcdRYAjuwRssx4y-RQ6-N1zAsy8pfgzGYVf9mUdDY3bNTJeBHJPWB3Z5kuU_vaefy8juqqaOGlw4oVuNFapmoFk-DyjslzeQRLqpE9atEqyhqAw-frdfTzIPcxZ_yFJAY1PcF9cYLCnXPeXUHu-xL4DD3m93yaJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قدرت‌نمایی جان‌فدایان در اصفهان
🔹
هزاران نفر جان‌فدا عصر امروز در اصفهان به خیابان آمدند تا آمادگی خود را برای دفاع از ایران اسلامی به جهانیان اعلام کنند.
عکس:
حمیدرضا نیکومرام
@Farsna</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/465719" target="_blank">📅 18:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465718">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGWzWvKe9Ct41Q91byP1bHXVi1vi-mZUqpgKoTKy3tCUrdSD35j48nmGxHIpicLXFjtCHjzopFVcmK6S26In12ig6ShSaK8FKG2T3dv750mhgFVgEgIjlH0qJ-jyOhjOGkDxZHsyXSIOtT-adIngO9TPBjLpKOkynBEwnvppoOgOo7HpcG8mDO7p2H4aqrzLrENwiZbrmuhfT90AkvXQhlyvn-rWR9vZS5FSdp9nHrh1f1iIcdYWXmhVR6uYFHlUj5xP1kFGbNysn0LnMcHhxo9aPxwNL_sOCg9cirvNvazq3IR3IEFhAZ6NeIc2VOrQNuO4E9iQuIwvy6ehW4Lc0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همتی: تلاش می‌کنیم مبلغ کالابرگ برای اقشار کم‌درآمد ۵۰ درصد افزایش یابد
🔹
رئیس بانک‌مرکزی: در حال بررسی و تأمین منابع مورد نیاز برای اجرای این طرح هستیم تا امکان افزایش مبلغ کالابرگ برای اقشار کم‌درآمد فراهم شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/465718" target="_blank">📅 18:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465717">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jde0Hg27os2ThEwB_TOvX1vSMZN8GPQE2muAZwDxU4OF7uNibMa7w5JKEDr0c-mq5ahSaYDqk_gNYnNyIuntM551NlAfk1dwLq5diGO-f-oBVjohhQtJcEeX9JkMuIAXiA3K_dyvkie06XWBCKA39JCZL4L5HbZ2i0wE4qsHkOkIgPBGmLHLI5yEvPEdoGHcgxT3ZQckQjp-Tx-EF2GXPQ9cT58AvVxZBbPZYzoVOC-9MrJjWhMxxw5l7VXC0k2XerACbI1K_7BOYlMlzULb3nLTHDcTtdJRHyTR45IIaefHEPmT3m91XtYo-bNb_hRFzD2m0XZWeHwxfb9voEBkzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار شکارچی: شهید شمخانی توانست رویکردی راهبردی در ارتقای توان بازدارندگی ایران ایجاد کند
🔹
سخنگوی ارشد نیروهای مسلح در آستانۀ روز ملی نخبگان با حضور در منزل خانوادۀ شهید شمخانی ضمن ابلاغ سلام رئیس ستادکل نیروهای مسلح گفت: بزرگ‌مردانی همچون شهید شمخانی با اخلاص و درایت، نقشی ماندگار در تاریخ دفاعی و امنیتی این سرزمین ایفا کردند.
🔹
شهید شمخانی از نخبگانی بود که توانست با مدیریت جهادی، رویکردی راهبردی در ارتقای توان بازدارندگی کشور ایجاد کند؛ همین مجاهدت‌های بی‌وقفه و موفقیت‌های راهبردی بود که خشم و کینۀ دشمنان قسم‌خورده انقلاب اسلامی را برانگیخت.
@Farsna</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/465717" target="_blank">📅 18:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465716">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a377b35550.mp4?token=kOWrUkQ6fNGoEskQH5sBcIBocXafiiw_roPQVGxj_zgM021jKl5D4gGjBaSYBTfLXyNbfpsV3bmmi1qI7lIi8rPhfEWWH_NmhWdx-C1EL7kdopf2Bmq3VbJdgyJnjWE7Xrg1o2JWqKTaKrBSfudFBZeMtWw9aK3ULaNoQgedcMTbGa4QI8VZBw5ryjlmTi8p-aSM8RejzGzisjn7C43hgHgNJxYReQ8IUbgdaZNwqpIb8t-IkrFeHpuc6ftDb7_YQX9QqU18AJHP00i3VRD9KF-Qv7ih46BHMhahjzI-CIBwscsgWmjvapMgYSC2NCdRyB0JeeAO0RDfCfjmOY2pqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a377b35550.mp4?token=kOWrUkQ6fNGoEskQH5sBcIBocXafiiw_roPQVGxj_zgM021jKl5D4gGjBaSYBTfLXyNbfpsV3bmmi1qI7lIi8rPhfEWWH_NmhWdx-C1EL7kdopf2Bmq3VbJdgyJnjWE7Xrg1o2JWqKTaKrBSfudFBZeMtWw9aK3ULaNoQgedcMTbGa4QI8VZBw5ryjlmTi8p-aSM8RejzGzisjn7C43hgHgNJxYReQ8IUbgdaZNwqpIb8t-IkrFeHpuc6ftDb7_YQX9QqU18AJHP00i3VRD9KF-Qv7ih46BHMhahjzI-CIBwscsgWmjvapMgYSC2NCdRyB0JeeAO0RDfCfjmOY2pqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
راحله امینیان همراه هیئت ایرانی در بیروت: پس از جنگ چهل‌روزه و شهادت رهبر عزیزمان، دوباره در کنار خواهران و برادران حزب‌الله هستیم به نمایندگی از مردم ایران به دیدار خانواده‌هایی رفتیم که چندین شهید تقدیم جبهه مقاومت کرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/465716" target="_blank">📅 18:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465715">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ai6LVKEI_wvJE5tZq8xv0MZoBfCNXlx86UM_DB9OBp21_1z8V4AAoKYHJp2-On3faY4DRDtm7A2t_vNJ1oJ0K7yRTfmY3m8HB2kLAj_G7rls1D0MdNGaRs0sUrrck7ReRddBQDb9nyQJlYVTB3q_gqLFGXeHS_vny-FYySq9JWKXbGqR10WfBYFbMBBcCgE-qWG2rHqfJg5fePaFu6BDIDihnbMxQELPY1o73bwL98Rt8eLfr2Bm72V-IPM7oTCHNX0lv6GQKuBtw2w8le9HDh0UEaYHTOMfr_RzugZVEmKxPepihfGREZ96NSalei7-Rfy7wUwv_ll21Qjx5SXWpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوء استفاده از برق شهرک صنعتی برای استخراج رمزارز
در حالی که دولت تلاش دارد برای حفظ تولید کشور برق شهرک‌های صنعتی را با اولویت تامین کند، اما متاسفانه برخی افراد سودجو در قالب شهرک‌های صنعتی اقدام به استخراج غیرقانونی رمزارز می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/farsna/465715" target="_blank">📅 17:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465714">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCw9Y3lPeTZtv4giFXdMDLr3SibYlDI3ZqV-WvV1Ztf6PNrHfx3KWiBm-SX_z5ssJvm5gCQdku2vsfIcBcZB5yGnfCVlT-8XDuu1wmAKy40Ji2pauRDa8QuZaxqta58srgyBC-b_QKAtrsYnu7i8P5KgUELCnpdlwgwgnn7R4SQ7CJnxBpdSQd-c5pT-pJ0JhL3OJU2eLZO2TOekNeu_wqbZsnk8ktYKXLqVqkx_SV3ILeQ2MOQmkpeIlnGyOB8W1zGUXyA9lD9Ha-IYF2e0GwgNEQHmDrt8yafR2VBwuRp-V5s2fcPJuhMwib0ZB_3iXWGEWYAvii6KDo7MGGCx1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یار دبستانی اُپارک شروع شد!
🎒
💦
شروع مدرسه رو با یه خاطره هیجان‌انگیز برای کوچولوها همراه کنید!
🥳
اُپارک به نوآموزان متولد سال‌های ۱۳۹۸، ۱۳۹۹ و ۱۴۰۰ یک بلیت هدیه می‌ده.
🎁
📅
۴ تا ۳۰ مهر
🎟️
کافیه هنگام مراجعه، کارت شناسایی معتبر کودک رو همراه داشته باشید تا بلیت هدیه‌تون رو دریافت کنید.
👇
برای مشاهده شرایط کامل و اطلاعات بیشتر، همین حالا وارد لینک زیر شوید:
🔗
لینک</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farsna/465714" target="_blank">📅 17:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465713">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/farsna/465713" target="_blank">📅 17:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465708">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sTwMmBNnyabpg-56nKOmtwHHglFNUXkSWJEyu5Xj7BQsNr9FjIR6RVMATQIoajeTg1WarZWQ55eCNnjXtChC31zLCK804Amy-SzgmEWVoQWHBwJlj08AY600btULZHz4wmrXpB5ZwOPcMOQtlKKArDTo6za0Y5vL_4PymCY6nE8LOoePFtwQnY7F0pQ2hJamZue6wrc3sz7JerJ-5WvxK7OgiphICJFgV17KyYIrFa0Ag9Ay0Ao00IMzOm83lobDKzfAn3pTCDg3nDNfYZJRGzcBbnP2ORdwpFDBSQsJq1cx3amF1trHhIbvDpmzCaUbsCP5x12EzROfHS97rLzjAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/droyU9-xzO1N2oTQqtXyBwqb9uiennIzSfbfDGtMu-c9H3fZ8yddoZH0s0xHO6GLvdbQRUrF1tY39KIUoW7qhc_DNZRojzvGqFqIGMkQGarL2YAfDZJCoizijs3kSiLJkxKEVE2s5OqUE_AVNMRXx4M81PtgzhdEdDJck3zlhOo36l-5PRr_5GksKO4PBfAOwooa_4ec9QafzdhZJAZPVG4cZNq8gYXGMLwBJOLe4bPB3NFhewGo0mxcZwaNb6sG7VN3dMQ30XUZ4YYgUhK9VB0z7sZ98WId5KKktRAYefCgY6PteobT2qjMFaBnWiJPHCfdv5b8Hpgy_c1OqFFXpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tchH1FYiTTLpmjIsI0Acp0IoHpnJEQYJ2aPBnIUD-gJNpXqmMB1MHISgcgXcngQx9a7JTF4z65eLDoaFwWpoYalh462Hq84BFc6D3kY8qeLSdeNYp2qpQWuax3VxXyIfiZNJ49WyT_f6B0C72i_xArr7A1CsbvaE9tc5IgvTraI1Kx1ftdBnw7WXqHVNwxMSR6eorDXLQ_0vmI09U5EcSbJOIa0Yildg-VJODrBqM1Nk7vHjIPvSPYumZFX0T4YoMLWPH3pt7b1dJRjYjfS_1BYQXFcf8DN2z1nlIftrNulhIoqKLrlQjNG5Mh5TlcIXp80DTSwlCLERfOmfMAPyhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N9JGptG2ceYJrtwR7G1SbVPJxzw9mj00TiOoxQLyqyZ0fVGv_fOFO3SOXi2qBo_sBsCw-vsRp2XmA6W1Evpvxbp_1iVPLdx7SGqNzTfmvd2v7251Xe6OpLuQ3SB2uyaDs1LZFJxSEmDQ7FOEDFP9FVlaaJJ2mGxlxT48iPyN5fpIgMqXAf2Yuw5A90xpys7UQdUHUOMs-GNfr28Clme0Q4DJU0ZFvMCH6zAPFBUa9mNzqwvHpWmy1AjpvqkeczYvTuBi4KcgafcP4h4mstMICHyVXYNL5N8w_4yaq2S0XkpEg91TbASY8gEL888KfQSzif7ScslNnGRu-kTY-w4eqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad9345050.mp4?token=C00b-JcSME25WpQUTk5hbS0jzpqF2coQssMP_DePwZ0RYFz7bsfZehu8mCISEUfalG_mKqHmXyflcbWLBcsZwJAdxUISj5gIY8Y3gLhJAnF_YbJIFRmawyi4VyOFqgVsD2vqosDO98K-epZyUXgHZs3sUEB4Lg5El03zQ4mSzTRPAf_SP147_lCytbhM6848-L1fcdW_ezPJgvb0V-8wCkTj6UhCbF9UECpbjMLF3U87yGCc7WxY3-ucQPrB8VHDHuKVsHCKeAWbU5vbjmWY5eMsMcSe5MDxZgnTUvIOPfJInj9vN-gsU4Xjjl2lPruS2EywvZ0PgFRK17j5KTv_-4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad9345050.mp4?token=C00b-JcSME25WpQUTk5hbS0jzpqF2coQssMP_DePwZ0RYFz7bsfZehu8mCISEUfalG_mKqHmXyflcbWLBcsZwJAdxUISj5gIY8Y3gLhJAnF_YbJIFRmawyi4VyOFqgVsD2vqosDO98K-epZyUXgHZs3sUEB4Lg5El03zQ4mSzTRPAf_SP147_lCytbhM6848-L1fcdW_ezPJgvb0V-8wCkTj6UhCbF9UECpbjMLF3U87yGCc7WxY3-ucQPrB8VHDHuKVsHCKeAWbU5vbjmWY5eMsMcSe5MDxZgnTUvIOPfJInj9vN-gsU4Xjjl2lPruS2EywvZ0PgFRK17j5KTv_-4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رژۀ بزرگ الحشدالشعبی به‌مناسبت خروج ارتش آمریکا از عراق
🔹
بغداد، پایتخت عراق عصر امروز شاهد رژه بزرگ نیروهای الحشدالشعبی به‌مناسبت «روز حاکمیت» و خروج نیروهای نظامی آمریکایی از عراق بود.
🔹
در این مراسم، تصاویر و تابوت‌های نمادین شهدا بر روی خودورها حمل شد و از فداکاری کسانی که جان خود را در راه دفاع از عراق، سرزمین و مقدسات این کشور از دست دادند، تجلیل شد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/465708" target="_blank">📅 17:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465707">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsM4BLOESOmQYuswte1AcOScJvFCQMc-Bat_gGlVNpQA66eF_E0A_P4QRAZJ7ZLQwKwJwh_IPd1-1PNW6NahsOatqhalupf8CbrwbRnUJrcAnTLeUNjC1AK6buCDe7gE-uTTKBtvD6UgDYQomIo69SLwCk02OcIVgAoDnCVLtCdgoHm9jtweSMqdu81SSWwV1g_5injpZBHD5napbGKYeE2aKRV0RectyVqPPKAF32nI0et9qMX7_KZl4pSJTepiw-sOCapv58q69zvLK2uZYk1bWpuVEO7-tSgMHB9WHvVUFxx7xXn4fwOKTu-GwiV8sWXsZmBlVFm-SyoIlm8zbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سرپرست وزارت دفاع: ادعای نابودی صنعت دفاعی چیزی را تغییر نمی‌دهد
🔹
توان و ابتکار عمل ایرانی را در میدان خواهید دید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/farsna/465707" target="_blank">📅 17:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465706">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRRj1samKknU10eWg93vluyenvHDW7XtjxAL231-70_1gBSY-I0Paoph-CYV6M-UoTHBb3g0ApeVENnRtQWDlDzTzmH1PzH-fF5vPQLwq8GjBqXZzSd8KP8oowMvQ_uoaMqfsPWRjHnun-nPaPLm_UIBpTU2aPNg63E9crx3IQ45FFmbMqFhKiFShvlCiBoI_kctQCBamJHroAkbks0AVbToyXMB6IwFWPKFHk_IAlNKbZXs-KPe49hkhIGnrOdHf0dyHPUNCQ51L4hinpmDfoHbnW9w0dG_CGo1CZhFW_ym26OxGUO0zC5X18xVT8cZkAPLpDiGFhcwG4gkCLc3wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر خوش بنزینی برای موتورسوارها
🔹
شرکت ملی پخش فرآورده‌های نفتی: به‌منظور رفع مشکلات سوخت‌گیری موتورسیکلت‌ها و کاهش حجم ترافیک در عرضۀ سوخت، استفاده از کارت اضطراری سوخت خودروهای سواری در جایگاه‌ها ممنوع است.
🔹
طبق این دستورالعمل، جایگاه‌های شهری دارای سکوی اختصاصی موتورسیکلت باید به ازای هر نازل، یک کارت سوخت اضطراری دریافت کنند.
🔹
همچنین در جایگاه‌هایی که سکوی اختصاصی موتورسیکلت ندارند، ابتدا یکی از تلمبه‌ها برای سوخت‌گیری موتورسیکلت در نظر گرفته می‌شود سپس کارت اضطراری متناسب با تعداد نازل‌ها تخصیص می‌یابد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/465706" target="_blank">📅 17:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465705">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اتهام انگلیسی نخست‌وزیر انگلیس به ایران
🔹
نخست‌وزیر انگلیس مدعی شده که «شواهد قوی» از نقش ایران در حادثۀ امنیتی در نزدیکی پایگاه هوایی آمریکا در انگلیس حکایت دارد.
🔸
این ادعا درحالی مطرح شده که مظنونان این حادثه با قید وثیقه آزاد شده‌اند و مقام‌های انگلیسی…</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/465705" target="_blank">📅 17:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465704">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25e71b1f12.mp4?token=alGzjiPSfo49dDmG0G2rUguiGpxXo1hm3KH7jaWEvsVisdEpYgKkvaFBfJmtnuCO2JV7zL2qxz2tb1WBJEP-ICNH6xsscz0PzJWXG8UxsrDhqE5-P-oBuXEg2m3GObInbEdJ5vc4F1GX13qLKXmI2Jf-aFDeDUM0z_gV6QSSfoWy4x4zXq3j_Fydwp_y4Qq_hCHZKMQbGIymE8srKq7cMYLk3MCtbdiUhq6u4XtngSNkkEuLCDmLNO79nuMdYnmpjS3fwp0vV-EjSi8xT_LjW-suLb9X3klTN1ZW6-YWnXShes57PjaIqXX2KJGrWBisiceL34pIxJl4Sk6ZRZjWZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25e71b1f12.mp4?token=alGzjiPSfo49dDmG0G2rUguiGpxXo1hm3KH7jaWEvsVisdEpYgKkvaFBfJmtnuCO2JV7zL2qxz2tb1WBJEP-ICNH6xsscz0PzJWXG8UxsrDhqE5-P-oBuXEg2m3GObInbEdJ5vc4F1GX13qLKXmI2Jf-aFDeDUM0z_gV6QSSfoWy4x4zXq3j_Fydwp_y4Qq_hCHZKMQbGIymE8srKq7cMYLk3MCtbdiUhq6u4XtngSNkkEuLCDmLNO79nuMdYnmpjS3fwp0vV-EjSi8xT_LjW-suLb9X3klTN1ZW6-YWnXShes57PjaIqXX2KJGrWBisiceL34pIxJl4Sk6ZRZjWZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام پناهیان در دیدار با خانواده شهید در لبنان: بدون اعلام قبلی وارد خانه این شهید شدیم؛ مادرش گفت «دیشب پسرم را خواب دیدم و امروز شما مهمان من شدید».
@Farsna</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/465704" target="_blank">📅 17:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465703">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vyu_YhRZye4SXSYYRQam5SC-xsJuoESzNGr2FLxj31XZyPtvbZ_70kSnsTj8XI1sMj63yfGH7k4vbFjvNC89mvMGeFUUyj3KtwJl7kosddKEByqonIf5LW1NvCRc7aA1qAH7oYWhj5vQMC7bA5fEaziq0ON5rVDxuhVkJKirKLcOlFv5w8ugWohi1YIsKVRyrkNdwo7H4OzsMTGwz8QZ9emGZ-HrxuBoOa90h-dwlC05o3lVgImpAf0uI6LGXHMUV1yhW_XyT10bgfmFoeZM0pB2TYtNUig7ksIpuMqxh0wMgTTkUd6vIMfcXiXb81alo_fQrsbB9b0v-TNRFtMn9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جایی که یک اختلال در آن می‌تواند گوگل را بلرزاند
🔹
تنگهٔ هرمز فقط مسیر عبور نفتکش‌ها نیست و بخش مهمی از کابل‌های ارتباطی و انتقال دادهٔ منطقه نیز از این محدوده عبور می‌کند؛ مسیری که هرگونه اختلال در آن می‌تواند ظرفیت شبکه و کیفیت اینترنت را کاهش دهد.
🔹
براساس مستندات گوگل، این شرکت در شهرهای مسقط، فجیره، دبی، دوحه و دمام ۵ نقطهٔ کلیدی دارد که بخشی از زیرساخت ارتباطی و انتقال دادهٔ گوگل در منطقه را تشکیل می‌دهند.
🔹
آسیب به کابل‌های ارتباطی هرمز می‌تواند با افزایش تأخیر اینترنت، کاهش ظرفیت شبکه و اختلال در خدمات ابری و اقتصاد دیجیتال، هزینه‌های قابل‌توجهی ایجاد کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/465703" target="_blank">📅 17:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465700">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BxeleqNYIGK8SbebSq6-9QyZLwQpgkvpWYmAV1ksamObeG9VbkzkUvTQN16Cu4qNt7RCqRItyDNHaLilcaDVA3HWnnqjHXqP3WKxyHu5zKkxI1-j7IwgrYsvphNA12A7hatQ66y679lmKqK0tA3bP0tVEvZzybXSAgEgMormdmf8mIaj_3ADJRk2cjPEUT9-HcA1CmHY4jSYvPgJGYtvDzd2ez-duAS6n0edEVFvpZorF92RNQKXDB18ip__K0U-TnYIFyT8eEN3yIYSabiZ9izmtJP6vur9trxTvjHtgFw2JMAxeaiDlyMmn3CmWFK1IJsU4YQ3Pp9todZXL9tbEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mUteLjya9Zx6J6jeJBGDXJQec93SDyUkZoCGyC81_D9aCtcaeqetlMj769G1F262Ik7A0kH9aMrwjQMMm4iMqKPi3tH_QE0aJCbYEJsvm7ulxclcqRhvKUSzcRR8LUyk6yZjkSNdISGzmNn0nfZuVLR9PBQdQGECqlybqSkYJK4pMJXvWM5sPa3tpvmB8r7_PALSFnYPkapO6Xxdnu4mOh-Xu2nLqCw267uO8WcjBZMpB3rHffWAH-OWR5frCupX9auKBbamiN1Yxr8BacfBsAMhgnuHEEEnqq5pwlwU-Hkc6gTB1QRUNZFE0B3xUWj6D_0MBLHGsi_adjOb2i7UVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T2OrYYmYkufRma6RSVH0s2DaTSee-S10e2y4CeM0X1rrPsw5o4dpDvsVGm07FDeUjnCbvrdeIu-Xa_u5uU4FvHACJxd2QXNOvkKmhrFGfacQZqN66wWua0ya9JhLt8cQMHfA7joTo-rvpNTkeBP0j7l4OIzm71YBPKBHQbZoDx1jn7bU4PjkJGdaXRwhGODVYn8NKo7ojrPBrf7uuiLX-_jF2rNvDwLsyhBugJ3AVmWkysLbXYDhedtuVtn3Qq1RW9tIsnT8Z86boQheYNVilg202Ckjd7UPifxpOQx7ghCLfWZAlPvs5PYVsuK38iPM1RLbRHeoGoyCc30MXUd0vw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یامین‌پور از اهدای انگشتر متبرک رهبر انقلاب آیت‌الله سید مجتبی خامنه‌ای به خانواده شهید حسین هاشم: دیشب را به زیارت خانواده‌های شهدا گذراندیم.‌
🔹
الماس‌های درخشان در خانه‌های کوچک در کوچه پس کوچه‌های ضاحیه...
🔹
اینجا خانه‌ی شهید حسین هاشم است‌. سه فرزندش در سکوت آمدند و دل ما را آتش زدند.
🔹
این شهید به‌خاطر اینکه در ویدئوی وصیتش مکان و کیفیت شهادتش را توضیح داده، در بین شهدای اخیر مشهور است.
🔹
با خود چفیه و انگشتر متبرک رهبر عزیز انقلاب آیت‌الله سیدمجتبی خامنه‌ای را آورده‌ایم.
🔹
هربار نام امام سید مجتبی را می‌آوریم صلوات می‌فرستند. همسر شهید یک کلمه هم حرف نزد، چفیه را روی صورتش گرفت و اشک ریخت.
@Farsna</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/465700" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465694">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tVV7XR6rs1yLsqxrMfnphVL0LTOv2j0xWT5envj3Fdpj6HxK7gM3ErkIZBAn87FvMq3n8c_y8nuFJ9Tbv_KPA0UTmPvDpTxhENbq71qyaPb_DgoXf35X4-JtWDYAcXZ2m3q3IpksZ4IjTTnHYb7OJSBttI7ZgL4Mn-4DywvvkAIik2Gzcyf2gjoNbZTHlCs64v6HKk5B7DmRrG9U5_AulDs22kHojifIgXrfAUd_duW4MFs9BQILTDftuDoFCWTyIMvzGX7mpDANMOBR5yiNH8K67E3Fv4xGrm88qpesAxu0E2XEwdF80Nlu2gMTe_DhcGBHtdBSh0ZyTKoQM9qs0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KtIMXaetCfBtyjbcy8L_CI7hRiyUBungCITRI731wc35J0ZozOhIbjf7ytlA4STytlSDyhW7ZZoGcarnQu1IUssEHCyUD-ENV6NFEzevCA1AkMJaVS5hMAh8cBB6Hjfh8pxfYoODoj-7MGpts0zbKDLVmGphP83esWdv0RSjD2GMssjzheZGzqYS6tgwLh_v9GqGiDk4PvBIbYuuvAMaI0tmk54vg64fyecMrHyQtBBgG3izovBFn0GBSoAVrVz_jE8TgJ5r1X1NGAHtJcQGfdBWwVbIM8wLgk1m5E6RIzz7VXkJopwCF4QEA6zSf4mBAHyHRIgmuCrGzkc6YV-cGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MxYd_ywfSTSDypN7ve1qPEtWEpdWvysP_Z9apNd1efLlIxwMMt2zUcpz5J5fFDV2127rlhmHuRsUilM1BYyQV6Hf4cmugjWqc260HuEmYKu7F1IfyjaORGdxfChRohhbc1-GT0GE3cGbW6eIC-jTIvhzqh-PBgtm5ub7JvdfSCQAb6xWwBGDSO-MeftjV2vCphx38QcB5TNqw6qpAA_VF1cAdiziRWJ7RnDTPbRcgk1edvrD_oMvk5WVovrUncv0osXG_iht8-H-sGZnExVRWiIhxR783wokyFMyGHbmABBFh7LCYE_PJYcDAnepWqE4ho1owcUmgj_O7TLdB1MFDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YDx3EXnc2qhAQgXXFTCpkTOiAeNnWkoy73guUmHZiuq_82n1MJ4neZZRG2WdMPd3z698zJyv7tGQ94yPANqziPJqS1g2CT16Bb1AjIEHZ2Kxn1yp8uNLsHBsLatKO16B-a-0IMV-pT9GjnweIrceL04F7oMzBgWUTEPjAagWpSZZbIqWdI4irBmp8HNifj_HW-Cg2WM5AVOsirdoQuLYFy-zoKH4NT2h64Idv6Ushoyvk1JcOjbT5LK6OAh6kZWoTzfEDQRXB5PeeTEN-9-VjO5bDER0t1dg7qvL0fOnmRC7lbbjmql9XU3tjCa0U0bOcwYQg2cNEP2evSPoKgsS3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ppXwy3I8poM2KDPcgy0jxqcUtG_4bZBNjdybueqB05HR6Uz_IP-uAGysRGsFeXKEvkeEvRrT_LOliDE3f27wqcPXEYqqZX6WFSzpY7BsTOXJaMmrtryVvmskPRjR9acSZTlx8d1qJBkRUiuZ6FI6vNqdAKWvxbFgttQlj5nxwyhVi-h8kief-na0X68Zt9y5TpxNCPbBsQUTci-Iz8iJm737ab8FxqGP60rtCurVoCxXNn9six_BkA0B91-H3xZsQctk5s8IYAIhMDrosoh8TSVT1SK7L2UBFdD97jwbyh1JTBS0nSwHc_WbC7NNplDKfR4ix6THDiA81LFBZ4Ii5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KDZY5khLzN6tXhZTKmSzbvnfc0_5PZOLdkpmlCrbsOjVVa1LvgSu2-mG9txZJEeQg1f-LcdfCESi0rKWpDNY9bsTkWyR_8I082rszLXLTbEqgSJ0zTgr15NrlzdeG8-fZ2HoeEkW8W7WHhHXoK1aBuWPKMrm-4C9-izpZMd0eJVu7Ku7vs_alLrF8rtksurnQuxNE9ekT_n89HoXFquIyAM3nqfPDCQvqDv3mwdu8m6jc4pZ0DWtYzplUi9wBdlmpYqOTOHAfPv8rtMxFgyzuqJZ7E-roEod24y5TVWSqFDXeMPUoPpwgI11EYC6ZjlB2IQmJ2__8jxBbmdajjgDPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قرائتی: مهم‌ترین جلسات هم نباید نماز را به حاشیه ببرد
🔹
رئیس ستاد اقامهٔ نماز کشور در حاشیهٔ اجلاس سراسری نماز: نماز نباید صرفاً در قالب مجموعه‌ای از مطالب و معارف دینی مطرح شود؛ بلکه باید در متن زندگی انسان و مسائل روز جامعه حضور داشته باشد.
🔹
بررسی زندگی…</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/465694" target="_blank">📅 16:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465693">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8093416765.mp4?token=USEQ3RLurVILBJp5VOIPh2XCJGV1YfTN4Qa34TNCnCNyr7Xrl4lBC1ARWdvIy6lrTz7EGShgZLledktno0afk-Kqei7Prcfy6KYx4obm2vag_lZOoqCTbFexk6kBsowFBca1SbnsNsfl0AmJKIhURImtgGORenWKT-uk1UmIQW2CB-YOKzxtWzsjqL4vWYwPjsDoyfgkDGB3gbqLAGFEBam6V8o0eCOKddp39_uJMrSsjmPxnfyI-N4hzhOZP-qkTNfXyWqa3kMb_sdskLOPqBiIshv4e3_R5A-i0x7CyAd3Pdxr2UxB7P4TGK2VEtzspGJ0k7C2y0PD14QUf7HZIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8093416765.mp4?token=USEQ3RLurVILBJp5VOIPh2XCJGV1YfTN4Qa34TNCnCNyr7Xrl4lBC1ARWdvIy6lrTz7EGShgZLledktno0afk-Kqei7Prcfy6KYx4obm2vag_lZOoqCTbFexk6kBsowFBca1SbnsNsfl0AmJKIhURImtgGORenWKT-uk1UmIQW2CB-YOKzxtWzsjqL4vWYwPjsDoyfgkDGB3gbqLAGFEBam6V8o0eCOKddp39_uJMrSsjmPxnfyI-N4hzhOZP-qkTNfXyWqa3kMb_sdskLOPqBiIshv4e3_R5A-i0x7CyAd3Pdxr2UxB7P4TGK2VEtzspGJ0k7C2y0PD14QUf7HZIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چه رفتاری در مترو سالمندان را آزار می‌دهد؟  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/465693" target="_blank">📅 16:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465692">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">۶ حملهٔ هوایی عربستان به شمال یمن
🔹
شبکهٔ المسیره از ۶ حملهٔ هوایی جنگنده‌های ارتش سعودی به مناطق مختلف استان صعده از صبح امروز تاکنون خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/farsna/465692" target="_blank">📅 16:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465691">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36647abbcd.mp4?token=tmZrEyMWgW7O1L5s4K3daCJIHMFnI54X5NLLZH6ww-6hfs-V9b6HPpKMeFHrBwzfuoZg0VuATMpDfBtDc72qugzRqtCMzMan-RkLCHQa32Bt9mEvSBIsoR98VDAOaW2BgITtsASoc4SMRiItX3NsVoVIVvQta1AsKDGJQUiw_fObneg388sS7VbBNSTza6u1s1afcEJbxDBhaNdFuqYGrCDcMUMl6ytsqLi_ZfGPb2pxvzWspvEKZdFvGoWAMSYBFnqUghGM-nCASmxUZzTtTNN8zsn5JBROFSmMBcZyzoaq25kGsg12Y2L4hn1ivu6dhPkOA-fjRTq87la3n6GpDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36647abbcd.mp4?token=tmZrEyMWgW7O1L5s4K3daCJIHMFnI54X5NLLZH6ww-6hfs-V9b6HPpKMeFHrBwzfuoZg0VuATMpDfBtDc72qugzRqtCMzMan-RkLCHQa32Bt9mEvSBIsoR98VDAOaW2BgITtsASoc4SMRiItX3NsVoVIVvQta1AsKDGJQUiw_fObneg388sS7VbBNSTza6u1s1afcEJbxDBhaNdFuqYGrCDcMUMl6ytsqLi_ZfGPb2pxvzWspvEKZdFvGoWAMSYBFnqUghGM-nCASmxUZzTtTNN8zsn5JBROFSmMBcZyzoaq25kGsg12Y2L4hn1ivu6dhPkOA-fjRTq87la3n6GpDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اصفهانی‌ها در رزمایش جان‌فدا حماسه آفریدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/465691" target="_blank">📅 16:40 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465690">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس من</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f49959e28c.mp4?token=UfS4vWn8pD-CpwfrhKZVOved1paJ8uWfEW2O08ftk5GpJdWDFswPfEGERZ3BMLPRUnCQuv7zljrKyw2t7UZXnq_72un7VroBoDzojWLhCEhJk-pr-3OyLmFX3Z39LGxPVpVfH-TL_8-qRiZvAqHq4u5EKK90rUDUSd0hcRQkHj9QrJZ-hGsS_H6dF9AjY-5KgEf-84xGms8bWP1uAgqhPwL_kDXtpBBVIMJ25QiCI83BrMuYSopDhKnvJQBkvFIW2KDYU_yJ3XBIy-z8atxv14Gmjpg5PafRKzqJFM4Ce6n_QCUVQKW4FUvRo8iyrhS11WeiuvbhYscE8rOeCOgtBnsIPN5OJiqp2wiuSNqMbzEckEP2BPl6vh33dFtWNpYRDt7FHHfeT9HqqkfFNFbgbXUDSCFjguqPH_eMxzhGV7FgUrMuYezIOR24N-ndRsrZlzNXxQuNZXkJsnllaI52hopbu0VdxNr1BkmfptnRz-9QJCnzFlUPS7xTJgIhY0mmamYCFNR0eEFqZIgLPIEjnw2JQpn8ULpohFDSx9sYQCkU8C7jR_5_Tczf1MJgFL5ur0vHmoH_QZ0DG8bfiqCQh_JJEVjNRCvUOKX_xu2lGyW9QE-H_zg6Z_NoyU6ymbaA2uVUzpZnuOBBmTCar2jwftIHrn1AD0JzK9RoHFzMy7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f49959e28c.mp4?token=UfS4vWn8pD-CpwfrhKZVOved1paJ8uWfEW2O08ftk5GpJdWDFswPfEGERZ3BMLPRUnCQuv7zljrKyw2t7UZXnq_72un7VroBoDzojWLhCEhJk-pr-3OyLmFX3Z39LGxPVpVfH-TL_8-qRiZvAqHq4u5EKK90rUDUSd0hcRQkHj9QrJZ-hGsS_H6dF9AjY-5KgEf-84xGms8bWP1uAgqhPwL_kDXtpBBVIMJ25QiCI83BrMuYSopDhKnvJQBkvFIW2KDYU_yJ3XBIy-z8atxv14Gmjpg5PafRKzqJFM4Ce6n_QCUVQKW4FUvRo8iyrhS11WeiuvbhYscE8rOeCOgtBnsIPN5OJiqp2wiuSNqMbzEckEP2BPl6vh33dFtWNpYRDt7FHHfeT9HqqkfFNFbgbXUDSCFjguqPH_eMxzhGV7FgUrMuYezIOR24N-ndRsrZlzNXxQuNZXkJsnllaI52hopbu0VdxNr1BkmfptnRz-9QJCnzFlUPS7xTJgIhY0mmamYCFNR0eEFqZIgLPIEjnw2JQpn8ULpohFDSx9sYQCkU8C7jR_5_Tczf1MJgFL5ur0vHmoH_QZ0DG8bfiqCQh_JJEVjNRCvUOKX_xu2lGyW9QE-H_zg6Z_NoyU6ymbaA2uVUzpZnuOBBmTCar2jwftIHrn1AD0JzK9RoHFzMy7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاسخ پلیس به ادعای میلی‌گلد
🔹
پلیس امنیت اقتصادی اعلام کرد نظارت بر سکوهای فروش آنلاین طلا، تکلیف قانونی این نهاد است و ادعای «کارشکنی» یا «محدودیت‌سازی» را رد کرد.
🔹
به گفته پلیس، اقدامات انجام‌شده پس از هشدارهای متعدد و در پی عدم‌تمکین میلی‌گلد به برخی مصوبات و ضوابط و در چارچوب قانون انجام شده است.
🔗
اگر شما هم جزو افرادی هستید که پول و طلایتان را از میلی‌گلد تحویل نگرفتید، برای حمایت از پویش فارس‌من
اینجا
کلیک کنید.
@Farsnews_My
-
Link</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/465690" target="_blank">📅 16:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465689">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJL1LNfHkmTUgLXzwCLiMpS2bstiyqM8VVlQ2eaGZsk1MZWZusOwH7tIJcmLeeQwBxvY9-MiyVpPJxaU8TYGGRYZguFbZbwDsoIe5DLpy9W1Dlw0heORWdVvVmE8fUWqBH2ZkVmxZcntHrg2wj4fx_cmVuLe0JHVqrh55z8UEpan4JkaAs6DUgWDWt4jgEKFCiY83IqNVLiiLSXVx2JJoJ368zCLDba2Fbf0iMRfIw9LvXB_P8Q2-MP8BB6sGO69DmnpL6K1JBAcOf6u3yZCCBcJrfP1waNItgoiJ9W5j2AHkGS-IUMtEUGWICFekvBHdk3tN51yZRpkQfc4Qw9U9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا اصلاح‌طلبان قواعد مذاکره را رعایت نمی‌کنند؟
🔹
مذاکره در سیاست خارجی صرفاً به‌معنای نشستن دو طرف پشت یک میز نیست؛ مذاکره زمانی معنا پیدا می‌کند که هر طرف با اتکا به ظرفیت‌ها و اهرم‌های خود، برای گرفتن امتیاز متقابل وارد میدان شود.
🔹
با این حال، بخشی از…</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/465689" target="_blank">📅 16:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465688">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">شناسایی ۵۱ صفحه و توقیف ۲۴ صفحهٔ مجازی فعال در قیمت‌گذاری کاذب ارز
🔹
قوه‌قضائیه: در طرح ضربتی برخورد با قیمت‌گذاری کاذب ارز در فضای مجازی، تاکنون ۵۱ صفحه فعال در این زمینه شناسایی و ۲۴ صفحه نیز توقیف شده است.
🔹
۱۱ نفر از گردانندگان این صفحات نیز تاکنون دستگیر شده‌اند.
🔹
در یکی از موارد شناسایی‌شده، فردی که در حوزهٔ قیمت‌گذاری کاذب ارز در فضای مجازی فعالیت داشته، دارای ۱۶ کانال تخصصی در زمینه قیمت‌گذاری بوده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/465688" target="_blank">📅 16:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465687">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f67b218df.mp4?token=FNE9RQNhd0Tn3UCKfRql7KvY6knK8LF6k7FSC9IKAOPoq_9uRDf0paj4Tigno_u73SF-OLEzlI-CXn6oTL3vXFBrq9yxlf3MiysBWx-nl65FLbrv-Rdx2jyfb4WzBau8vM1vj0la3jeDcmP049MEr3gDcAAtHvwW0ceNDKfms3HTpIoqOo_KE0snX8EuYg1_Qq3E5KRAuT0iuCLl6_CUyoWbL-dMUMKDQIBpwLHlRevfC9Zp6eqDLRpKBmJPkubzv8NCAfX3yk0LywmMqlC5O43PwL7gnYBsskWsTg_BiMXI-bjMCP5oOrSgxsLyQ2IyovOc5M0oHTWoN8HykGbpNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f67b218df.mp4?token=FNE9RQNhd0Tn3UCKfRql7KvY6knK8LF6k7FSC9IKAOPoq_9uRDf0paj4Tigno_u73SF-OLEzlI-CXn6oTL3vXFBrq9yxlf3MiysBWx-nl65FLbrv-Rdx2jyfb4WzBau8vM1vj0la3jeDcmP049MEr3gDcAAtHvwW0ceNDKfms3HTpIoqOo_KE0snX8EuYg1_Qq3E5KRAuT0iuCLl6_CUyoWbL-dMUMKDQIBpwLHlRevfC9Zp6eqDLRpKBmJPkubzv8NCAfX3yk0LywmMqlC5O43PwL7gnYBsskWsTg_BiMXI-bjMCP5oOrSgxsLyQ2IyovOc5M0oHTWoN8HykGbpNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بهنام ابوالقاسم‌پور در منزل شهید حزب‌الله: قهرمان‌های واقعی اینجا هستند؛با وجود حضور در خط مرزی، خانواده شهید خانه و منطقه خود را ترک نکرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/465687" target="_blank">📅 16:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465686">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c459f0d9c.mp4?token=evYBhDnm_yQJfcnX7q5rN0yeFjjeiSH-zdoQnDVDCcJy5afzD43Ij0Hqws5LQCQmMKulMRTUtpvJ2qKocH3JMhXr2t-pbdcA1t9FN6VK2rnb-zDBf50Vyws6MCJCNXzhATUYh7ZQNxVcpstkRuq1SZwTwru2m6CP1HWl9PG7kS3NHSFIq4NhOFhU_2jS1UIIz6WBE_2jwgWQ5CQV5BwK74W2p1J7CYw-F5h_Nvdn2mTwe0r39fPFxpfK3INOg4cwEN-d9h9bP6jkfkg6pdOyBepUj9PhMiDMLDg8NcbFKQpgjsTE6HUuqqFK8kjyHjejuLrYuHqN3sqBJK7sx1DUtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c459f0d9c.mp4?token=evYBhDnm_yQJfcnX7q5rN0yeFjjeiSH-zdoQnDVDCcJy5afzD43Ij0Hqws5LQCQmMKulMRTUtpvJ2qKocH3JMhXr2t-pbdcA1t9FN6VK2rnb-zDBf50Vyws6MCJCNXzhATUYh7ZQNxVcpstkRuq1SZwTwru2m6CP1HWl9PG7kS3NHSFIq4NhOFhU_2jS1UIIz6WBE_2jwgWQ5CQV5BwK74W2p1J7CYw-F5h_Nvdn2mTwe0r39fPFxpfK3INOg4cwEN-d9h9bP6jkfkg6pdOyBepUj9PhMiDMLDg8NcbFKQpgjsTE6HUuqqFK8kjyHjejuLrYuHqN3sqBJK7sx1DUtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روسیه یک پل مهم کی‌یف را هدف قرار داد
🔹
خبرگزاری فرانسه: برای اولین‌بار «پل جنوبی» که شرق و غرب پایتخت اوکراین را از روی رودخانه به یکدیگر متصل می‌کند، هدف ۲ حمله پهپادی روسیه قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/465686" target="_blank">📅 16:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465685">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9cXQ76y7gK792k8Axe9H7nWqS3aIToJVXJ75BlC9KhER0MDpBMYrf7ZrU8_LE2nBDoPeebX5Hl50-DqSb7_Q2y1xjVzj-Xnd1x-kudre7BlL-5mmXsfHm_QXiMviUd-gxrmU2q_5C80F0X75UHrN38fJJ2rOWiKno_fgtYOnsb3kzSMNElxJc5JiObiPK6ieRSvVOmSIwbNl05q4Gyw1V4bUdvrzBQ4sVr0TmSWvK2LB8HHo8kyxB9wRA-0kWB9RlUzmNp2sY_cDHAY45PCbDf3_kjciDxABdJh4HN3EQKTcftsMNI_sCv98PXocuPpJ9v7YcsCREHMuf1CE5IPQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعات میلیون‌ها نظامی آمریکا هک شد
🔹
اطلاعات شخصی حدود ۲.۸ میلیون نیروی نظامی فعلی و نزدیک به ۳۰۰ هزار فرد فوت‌شده آمریکایی در یک حمله سایبری به سامانه اطلاعاتی پنتاگون به سرقت رفت.
🔹
هکرها از مهر ۱۴۰۴ تا تیر ۱۴۰۵ با سوءاستفاده از یک آسیب‌پذیری امنیتی، به اطلاعاتی مانند شماره تأمین اجتماعی، نام، تاریخ تولد و سوابق خدمت نظامی دسترسی داشتند.
🔹
پنتاگون اعلام کرده تاکنون نشانه‌ای از سوءاستفاده از اطلاعات سرقت‌شده پیدا نشده، اما هویت مهاجمان همچنان مشخص نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/465685" target="_blank">📅 15:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465684">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/619042ce0f.mp4?token=rKvcQX9pTFBc__nHyofojd8Mvr5Emt3L1CGU9gfDPF3tTSCv4FLsy1X8-JiUXBCCNida8qTOgnDBGTEXMYLbaSeKgvHjGCEXnfOT8QTR6OPZv2qDpAbWsev_mj76yP3EFEE9sPEoAYtHWTpE34Emb3yxQpAWt0YjEsxrQSeS-AAe4MaRWx1VsM1YW-7tBy-nDYvFQJ8n5j9lLWrGTYqNYoF62GHGoRyVW6P8i7dFTG8lK6AoZ5WKmzTa-nPOt__QEQei1_lYdDU7oJ1G_hP7-Y1VoKj7QpE58yfupCsmu1_4KuIPE734r6z-IWN5xE-U7LNjjOv6JDE7Ri-Riod28E0SfJeh6X3MfBp1bVPpo8Mq5I3Ljfgd4SGShmU-3B5Qsk6lGb0qWC7JjqvaC-za6P5U9xBFiSm3ZmqD6vqAfoQ3RO3R2JgKp66UHHjnChz9gf2zUpg83fnARpgwiYyKH3kcekxi8s_Xeky3Z75RYfRgN_5lYOFM7_ZA6hBXVHt4Ji--vPicXxA30Io5iv0gPwT4ax_A_mPP1zcGJRS4FBsYhHZRFGaIzVRM3C70H74S9lXLbBDPxP-Tb8zLSdbk-LDoctHJhfI_tvKukz1uUqZ2o4Zln9sF4nwg7gPD3UwYAHxTRvTsZRTqavvNV87n-_O2NgJijnC4yMMQJkMpOt8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/619042ce0f.mp4?token=rKvcQX9pTFBc__nHyofojd8Mvr5Emt3L1CGU9gfDPF3tTSCv4FLsy1X8-JiUXBCCNida8qTOgnDBGTEXMYLbaSeKgvHjGCEXnfOT8QTR6OPZv2qDpAbWsev_mj76yP3EFEE9sPEoAYtHWTpE34Emb3yxQpAWt0YjEsxrQSeS-AAe4MaRWx1VsM1YW-7tBy-nDYvFQJ8n5j9lLWrGTYqNYoF62GHGoRyVW6P8i7dFTG8lK6AoZ5WKmzTa-nPOt__QEQei1_lYdDU7oJ1G_hP7-Y1VoKj7QpE58yfupCsmu1_4KuIPE734r6z-IWN5xE-U7LNjjOv6JDE7Ri-Riod28E0SfJeh6X3MfBp1bVPpo8Mq5I3Ljfgd4SGShmU-3B5Qsk6lGb0qWC7JjqvaC-za6P5U9xBFiSm3ZmqD6vqAfoQ3RO3R2JgKp66UHHjnChz9gf2zUpg83fnARpgwiYyKH3kcekxi8s_Xeky3Z75RYfRgN_5lYOFM7_ZA6hBXVHt4Ji--vPicXxA30Io5iv0gPwT4ax_A_mPP1zcGJRS4FBsYhHZRFGaIzVRM3C70H74S9lXLbBDPxP-Tb8zLSdbk-LDoctHJhfI_tvKukz1uUqZ2o4Zln9sF4nwg7gPD3UwYAHxTRvTsZRTqavvNV87n-_O2NgJijnC4yMMQJkMpOt8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ژیلا صادقی در لبنان: مردم بیروت عاشق وطن، مقام معظم رهبری و سید حسن نصرالله هستند و اجازه زورگویی به باورها و سرزمینشان را نمی‌دهند.
🔹
مقاومت ادامه دارد چون هنوز شهید می‌دهد.
@Farsna</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/465684" target="_blank">📅 15:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465683">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8aa171770.mp4?token=RMH1Jt20QLDBVNUNCMxjyjA9D9Rl_CE2WZTtCAERbWFpI2gmkC2C39R7I73ESJW8ML2NWfBLpIEpOj1cPXWAwlPU_JorNiSLrJe8Ki2AmtvbDNyaum0DEEMnvdbYcLO85Aac3wAeSrpHzgf4qdUAYVNDCleNSmYH9u5LSyTlTH5rSJgFx8NTeJUK-93VH9vrJQx0X-2-hY71ooakRbMsHb4lUT3kWOnv67zK6IuMSxf5kz4zjJNGv2Q1q5b4EjbnXSnG0Vh1axWDRuLVc6Wk1r-NSZ3QTOmne6m8ofC32p6IYABUks6yClFISD_Ih0mi51K2s-4k8JkWpcCJ_MTxiYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8aa171770.mp4?token=RMH1Jt20QLDBVNUNCMxjyjA9D9Rl_CE2WZTtCAERbWFpI2gmkC2C39R7I73ESJW8ML2NWfBLpIEpOj1cPXWAwlPU_JorNiSLrJe8Ki2AmtvbDNyaum0DEEMnvdbYcLO85Aac3wAeSrpHzgf4qdUAYVNDCleNSmYH9u5LSyTlTH5rSJgFx8NTeJUK-93VH9vrJQx0X-2-hY71ooakRbMsHb4lUT3kWOnv67zK6IuMSxf5kz4zjJNGv2Q1q5b4EjbnXSnG0Vh1axWDRuLVc6Wk1r-NSZ3QTOmne6m8ofC32p6IYABUks6yClFISD_Ih0mi51K2s-4k8JkWpcCJ_MTxiYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رضا علیپور پس‌از کسب مدال نقره: سرباز مردمم و پارتی من خداست.  @Farsna</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/465683" target="_blank">📅 15:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465682">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ca4b25d5.mp4?token=O9siD47w08NZ2fHky_89Fg0EDlUYCDstL-B9nH26zoJMqPKdxc4FSYUG33r8pxw6Rt3yTj4SsBkXn5wNbYWjY7srl3pKAc4iK4vRKhWpxHWea6OfP5ConX368Qs8GY0s5ISEHXXzewOwWb5HygLK6l9MDVx4ssFefyx4muj3Yp5YsWz5GIqbH8jhKdPMkwIi0_6QDMiODYqOK4g_Hy65tch8zwXA6aE9zVc6YRLAnBQpiUstLpI1YKKaDW1ylbq0eXcKAhCygDYT24Jbhxz0VktG6HQIxsnKASfmHxX31-_vmNsfdvKbOMrc9QLt5XpxcOGl4Ky3AtUNZvoVTVo8OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ca4b25d5.mp4?token=O9siD47w08NZ2fHky_89Fg0EDlUYCDstL-B9nH26zoJMqPKdxc4FSYUG33r8pxw6Rt3yTj4SsBkXn5wNbYWjY7srl3pKAc4iK4vRKhWpxHWea6OfP5ConX368Qs8GY0s5ISEHXXzewOwWb5HygLK6l9MDVx4ssFefyx4muj3Yp5YsWz5GIqbH8jhKdPMkwIi0_6QDMiODYqOK4g_Hy65tch8zwXA6aE9zVc6YRLAnBQpiUstLpI1YKKaDW1ylbq0eXcKAhCygDYT24Jbhxz0VktG6HQIxsnKASfmHxX31-_vmNsfdvKbOMrc9QLt5XpxcOGl4Ky3AtUNZvoVTVo8OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
علیپور نقره‌ای شد
🔹
رضا علیپور با ثبت زمان ۵.۳۶۲ ثانیه به مدال نقرهٔ مسابقات صخره‌نوری آسیایی ناگویا رسید. @Farsna</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/farsna/465682" target="_blank">📅 15:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465681">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">شاکری: از امروز تا انتخابات آمریکا باید سطح تنش را بالا برد
🔹
مجید شاکری، اقتصاددان: تا زمان انتخابات میان دوره‌ای آمریکا یک گلدن تایم ۳۶ روزه باقی مانده است و جمهوری اسلامی باید سطح تنش را در این ۳۶ روز یا حفظ کند یا بالاتر ببرد.
🔹
تاکید می‌کنم که این افزایش…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/465681" target="_blank">📅 15:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465680">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cad297dc73.mp4?token=amzPwvI4Jsv1dAQc6ye4yfjBsbfHwhDAX3jU-7F0UjyggiGHc4-IPdpUJ4iU5SDhfEFk_bJl7SOyiXyTdrFlnAxMSsGwTVUfagCBFzV7vKLtDyZg4a5lGpNjBpLDWSdpXpn9ZKTfVURgwJvwWuRsd_JTvpT7kqRC7vS1p-3Gc5UTiGWo1XvKw4QXTHEeZb7rAeyCbz7c1M89l5Lk1LkXwrpuwWEIyPHLLAeBoUGSSPfz5GDeSBAaxehjYxJ2xxeWbA8StnsXOA3lHTivRCLItCH2DRtu1pfiUXH1dk0mAF8pPwyF7x2k5OqB0KsWPYid8C_bUgJY0LReeQoJ2tJXhB-uzKfeGqWycOqBsJu_BP7bjiPHFAhpMHZ9PYJwfJ4oXg5PLb76tknG-1msU3mafOO2rE8U7qJdlXTZyaub65qvDYM3YVXSKKc0ndqCqZb8lsV_tD-v5PPD9rDwjgIez2pKwN0Ov6_LAl2B8Ck1XCK9Byq7PWV3FV8RTzxt87RkoEp_BRtxL9CnPBYMHKa4Jwo00ktAcilkdsN_KWlNiJpJ5xoN0rJ0TdUAIuCBm1PtIKgXZxKtpsDg50DXK8iH6dzMbfKFuKW1PPvR_iQXP9XK8JYroRMTor6qBn1reIeVSjLcOyRTLU7JzcM958KZjWeGjxPdpKnLWdnFPxDVnk8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cad297dc73.mp4?token=amzPwvI4Jsv1dAQc6ye4yfjBsbfHwhDAX3jU-7F0UjyggiGHc4-IPdpUJ4iU5SDhfEFk_bJl7SOyiXyTdrFlnAxMSsGwTVUfagCBFzV7vKLtDyZg4a5lGpNjBpLDWSdpXpn9ZKTfVURgwJvwWuRsd_JTvpT7kqRC7vS1p-3Gc5UTiGWo1XvKw4QXTHEeZb7rAeyCbz7c1M89l5Lk1LkXwrpuwWEIyPHLLAeBoUGSSPfz5GDeSBAaxehjYxJ2xxeWbA8StnsXOA3lHTivRCLItCH2DRtu1pfiUXH1dk0mAF8pPwyF7x2k5OqB0KsWPYid8C_bUgJY0LReeQoJ2tJXhB-uzKfeGqWycOqBsJu_BP7bjiPHFAhpMHZ9PYJwfJ4oXg5PLb76tknG-1msU3mafOO2rE8U7qJdlXTZyaub65qvDYM3YVXSKKc0ndqCqZb8lsV_tD-v5PPD9rDwjgIez2pKwN0Ov6_LAl2B8Ck1XCK9Byq7PWV3FV8RTzxt87RkoEp_BRtxL9CnPBYMHKa4Jwo00ktAcilkdsN_KWlNiJpJ5xoN0rJ0TdUAIuCBm1PtIKgXZxKtpsDg50DXK8iH6dzMbfKFuKW1PPvR_iQXP9XK8JYroRMTor6qBn1reIeVSjLcOyRTLU7JzcM958KZjWeGjxPdpKnLWdnFPxDVnk8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل در دبی زمین‌گیر شد
🔹
شرکت هواپیمایی «فلای‌دبی» امروز اعلام کرد که پروازهای رفت و برگشت به اسرائیل تا زمان تکمیل تحقیقات جاری دربارهٔ پرواز جنجالی دیروز به‌حالت تعلیق درآمده است.
🔸
روز گذشته پرواز فلای‌دبی با ۱۷۰ مسافر در مسیر دبی به تل‌آویو، پس از…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/465680" target="_blank">📅 15:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465679">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f679fd6ff8.mp4?token=GPjdAFuWZbN81qCVjd_WU_hJ8e9ztksXEdW70ksrY4sIZQa_xXyXf60wp3kQavRLzz6lE7mS8ghNC3Qd1tA6GIpcOO18rYkGWaow7sjwqBFzaUra6bdY_RRN43uzJhk-edZIM8B7-bokxzXvXyciTIgETne01ADpEcRBMT12NgazTGQHCOshpyU-i9zo8gSGClXRQgzbi9GpAGdd6GdYtNi-IJXzNXmVIDDBjnWuKUOmGRr3IQioYlE1eTa2xvaG3IKpb0Mc1znWla7MRHsKc8SRcrD6Q58o-dgk-rEurPTOot3LU9ZD1fyfgHJcY-ECz1f_zmqXb9MuQBu11-2BcY2LF92k-oHbwhRf_g5KDVu3VF5o4kfGNPLPr_4UnbnaNoc6rXpE087CCR56XM5pZ6rEEdWR0Fq9hEm-uWAK8v8Ei7JdZwXFbbY6KzPuh_P9rwt1p8orwK2z92Fh-Jme8osyHLgWT-dXfY6bYN61TTTRQ3yXy9B9zK0uLi2TTYX0e6ylK-UZyLqUs5BH_Om13-2gVuO3wMDFz8R_6oJusfzEET46lU8MyW5bwhhM5miGUADV9Qom0XAbj9LL54mH6rOgVXjTc3eCP6uKc0ds60a288oC9lEow-mhTk2yOFbnspprm6McObdI3mziqM00RkYJzJsfYSAYxecd8DNGCvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f679fd6ff8.mp4?token=GPjdAFuWZbN81qCVjd_WU_hJ8e9ztksXEdW70ksrY4sIZQa_xXyXf60wp3kQavRLzz6lE7mS8ghNC3Qd1tA6GIpcOO18rYkGWaow7sjwqBFzaUra6bdY_RRN43uzJhk-edZIM8B7-bokxzXvXyciTIgETne01ADpEcRBMT12NgazTGQHCOshpyU-i9zo8gSGClXRQgzbi9GpAGdd6GdYtNi-IJXzNXmVIDDBjnWuKUOmGRr3IQioYlE1eTa2xvaG3IKpb0Mc1znWla7MRHsKc8SRcrD6Q58o-dgk-rEurPTOot3LU9ZD1fyfgHJcY-ECz1f_zmqXb9MuQBu11-2BcY2LF92k-oHbwhRf_g5KDVu3VF5o4kfGNPLPr_4UnbnaNoc6rXpE087CCR56XM5pZ6rEEdWR0Fq9hEm-uWAK8v8Ei7JdZwXFbbY6KzPuh_P9rwt1p8orwK2z92Fh-Jme8osyHLgWT-dXfY6bYN61TTTRQ3yXy9B9zK0uLi2TTYX0e6ylK-UZyLqUs5BH_Om13-2gVuO3wMDFz8R_6oJusfzEET46lU8MyW5bwhhM5miGUADV9Qom0XAbj9LL54mH6rOgVXjTc3eCP6uKc0ds60a288oC9lEow-mhTk2yOFbnspprm6McObdI3mziqM00RkYJzJsfYSAYxecd8DNGCvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
علیپور فینالیست شد
🔹
رضا علیپور در نیمه‌نهایی سنگ‌نوردی با توجه به خطای ۲ حریف خود همراه با دیگر نمایندهٔ چین به فینال صعود کرد. @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/465679" target="_blank">📅 15:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465678">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ed9d34d24.mp4?token=CUPUOvHyAbl3JYYiVsSmMhrKTE5PZZnWT-qd05GMBTzdgOYoNRrB7KWmW_u4KYPlynGGc-VJ2kYRkUzTkwa0SoFiBoHs4P8X3_4E8VjkF0vD3gnStKl2nfJaT7pBaHxFnI0lAVyfw2r_SadJondt_SSAjBcscxk9MkNkPRxwxC4wojxq5z7gyO9AJNeo5RHwJRauATj4Hwmh6jKXiH4gmOl_3Li56Yv8NhvCe4pROj3Xn2AqQESSk-bUwvAkuNttcRoNh938XoF2lOop-74XeCmwblwVbe2HUBVS-3PeNtUyQgYFKilA-qp-5Qs6euiVbeIYnecRQJvwApYi8pO3azVoClpHFoi3Kn7vKAseXK0YNXbnlnl3tR9IHtlSuCvIW7rtMY1Ii9Wxai82BTUv3AxwukZvaPCaO76GW5QE6waITgHz832SQqzPvpnrFrVy6krVUd_ClRb3qKfeXpifgb6Cmu-Txf14QKfBhJiT4R96qIKrFwxCvqKNqpT5dhR_xJdxhIWsnohmF0MgiZDL5UR-QgEgrgtDOghrnmIE_T4-0QGjtKVslPLkFEFttkbTQTHOgtDq-E0wXmMExV_d-xjdrfs69EpDEa7USpyMsr3gPFryRhsIvjgCNn7N7D4toAiUvr-wK6hfCRAhSkbPYYgWjpaSzZnLCq_-0NWdqVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ed9d34d24.mp4?token=CUPUOvHyAbl3JYYiVsSmMhrKTE5PZZnWT-qd05GMBTzdgOYoNRrB7KWmW_u4KYPlynGGc-VJ2kYRkUzTkwa0SoFiBoHs4P8X3_4E8VjkF0vD3gnStKl2nfJaT7pBaHxFnI0lAVyfw2r_SadJondt_SSAjBcscxk9MkNkPRxwxC4wojxq5z7gyO9AJNeo5RHwJRauATj4Hwmh6jKXiH4gmOl_3Li56Yv8NhvCe4pROj3Xn2AqQESSk-bUwvAkuNttcRoNh938XoF2lOop-74XeCmwblwVbe2HUBVS-3PeNtUyQgYFKilA-qp-5Qs6euiVbeIYnecRQJvwApYi8pO3azVoClpHFoi3Kn7vKAseXK0YNXbnlnl3tR9IHtlSuCvIW7rtMY1Ii9Wxai82BTUv3AxwukZvaPCaO76GW5QE6waITgHz832SQqzPvpnrFrVy6krVUd_ClRb3qKfeXpifgb6Cmu-Txf14QKfBhJiT4R96qIKrFwxCvqKNqpT5dhR_xJdxhIWsnohmF0MgiZDL5UR-QgEgrgtDOghrnmIE_T4-0QGjtKVslPLkFEFttkbTQTHOgtDq-E0wXmMExV_d-xjdrfs69EpDEa7USpyMsr3gPFryRhsIvjgCNn7N7D4toAiUvr-wK6hfCRAhSkbPYYgWjpaSzZnLCq_-0NWdqVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اهدای چفیهٔ متبرک رهبر انقلاب آیت‌الله سید مجتبی خامنه‌ای به رزمندگان مجاهد حزب‌الله لبنان در خط مقدم نبرد با ارتش رژیم صهیونیستی در کنار رودخانه لیطانی
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/465678" target="_blank">📅 15:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465676">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8830ec81.mp4?token=fyXSqp3r0wmKjNIfreFe0I1bV1pMwCeAIva4395hsoTsi3d-gr7F86_bxBCbcHg6yVyI0ai6uwZiJoW8j_4leh4aMHsTJj2XhHZ5l2LeD-XvF5uEJg61dqtDMxudCEikJvArqTnwHAGCv0rqAm98ETz00ZnCXTaVVeo5YKbI7pRV5HhIcySIFBJUuLSwitRIiwLpsoOHjPyIMD9bwCrkhZvaWvPlCu8_NJ_LFmn3uW4o9D488fpoEz_cFAXtKW0qtkmNjquMH-RrbWanx8lPBphXVJvckRC4FVbqPdJ7jceE4nNXVnVYtjRnesimkqKatkwU32hn2mjhaBQVoi4B2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8830ec81.mp4?token=fyXSqp3r0wmKjNIfreFe0I1bV1pMwCeAIva4395hsoTsi3d-gr7F86_bxBCbcHg6yVyI0ai6uwZiJoW8j_4leh4aMHsTJj2XhHZ5l2LeD-XvF5uEJg61dqtDMxudCEikJvArqTnwHAGCv0rqAm98ETz00ZnCXTaVVeo5YKbI7pRV5HhIcySIFBJUuLSwitRIiwLpsoOHjPyIMD9bwCrkhZvaWvPlCu8_NJ_LFmn3uW4o9D488fpoEz_cFAXtKW0qtkmNjquMH-RrbWanx8lPBphXVJvckRC4FVbqPdJ7jceE4nNXVnVYtjRnesimkqKatkwU32hn2mjhaBQVoi4B2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
علیپور به نیمه‌نهایی صخره‌نوردی صعود کرد
🔹
در ادامهٔ رقابت‌های سنگ‌نوردی رضا علیپور، در مرحلهٔ یک‌چهارم نهایی ماده سرعت مردان، با ثبت ۵.۰۴ زمان و قرار گرفتن در جایگاه دوم گروه خود موفق به صعود به مرحلهٔ نیمه‌نهایی شد. @Farsna</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/farsna/465676" target="_blank">📅 15:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465672">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XGDcWYQbbIPFUVoiiSavKxp580f_K3NAau2wCufZMT8Us_MaAoLpPB3RUTfIz-ctp47aiaaN93e-x9850qS5ky-lHrgOkZiNoKbo_wPUIcaLVBe4pSDhjMY7IhMy1uXxILtRX72IakSrkQg6V_Bs9HoKho_B4o8zondsnNVxOU3r1ttwbGDV1eoMyulrShimtW9--LomR_S2F4saOEU6tQbFQLhruVZ9PR8xy2Ua4OjjObmBNc3mp1vckoPr1rUefbeo_P6FS4pFD4t4cBjtl7mzDkLen41NnHPHKr3QFD1xYsiA2Dxmk3FnLi8eb0Y1rfvl7POCaShFjUhTUkPRcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fzIJpDa8H6Ub-ows0VgtcgumrQs8bUvgHuDJTnmUOW4-_5sNT-LFBZ74JRcQtWkybEzRJSlV4fejzQQwWfvFcAhfpdfbuMtHvzjTYnrh7zFKrUcSHo0zsTFOp4ngdC3xFII7ZjYTLW8_HzjOGPAka1C26Wd8HEs6VsQ2PjYtphNAnI_7YXGMZpYe1stQV_xpSVzuFqDXGtwD3rhzcyOqyXaZijB_uCDPPqAqZqOQev8_kiBFQ_z1QAl_qcg_50zlq6ZRjC6m6vPkhZssF4g_aLYWMqd0hVEPSdJuH8SyXfIOwiI0UDKIekwKpVjevXrcxD1SblUIlkdy4aHy0LAWDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cXMWHRsLWWxT62rd0FuF5RWTL0aMydQVy44rzDk0Z3BRN_0WUPbWdG9Qklbj7t3WKbNf60uY5vLsiNuK2CR3gBy5qdbH6H1HwVZAF2zlNGe6OkW2CEC7_UXPHefe7vkKFbJBvg-93RBMYTZ2cz1ct31NnnqqB5Y2vIPwO9v9qEB_Sp0LkQkxj7MqH7silwvxK-ayeswJ2fwVY4pTj6CVkMliu7bS7ivl_B6JK4767DqdU0T2rbup8gbvgJ6fS_hSXC9u5_bgdjbpSklAFdqIEr1KEUxHH-C0D26xWkayQHcpBEewLpwRWGHzmyzWsBMscE5py_iIh_SNya4yXho3Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ns6qg4TmNieS4TRv3wbIx4uiHj3omCgV8NodQyEbEVF-vT6xwIkbvXnnYj10kxaoc3Hd5oHeOrVgY6N39kbzZG1hcaAnc6NOEHaBc6279vh4IXRTDcW4ByQsAtM7BDzNfA6Lh0ufbBypj4KTY-Xq1STWr-JxubGLlwt2Ph1o7Mn9jYwl4p8K2uFxC7TIwLHmWoG10KZaVC22Z7dpOdcaGSXu9Ev0UGtJ44ZZvZ_q6m7R-BdZ9n_9aOckY5PI8gTsNYqcFhBX8ezhiuOlyBVJCG8m1KBjURVEqjS7-PGaHEcQlbpOZyLz25Hr0yTcOgNeZzW4HFHwTF0GkX2XvA0NJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشکیان: به‌طور جدی دنبال برطرف‌کردن موانع کسب‌و‌کارها هستیم
🔹
رئیس‌جمهور در جلسه با کارآفرینان و صاحبان فرایندهای اقتصادی: مبادا تصمیمات اقتصادی و مداخلاتی که انجام می‌شود، خارج از حد تحمل جامعه باشد، زیرا به ضرر خود عمل خواهد کرد.
🔹
به‌طور جدی به دنبال برطرف کردن تمام مسائل و مشکلات مرتبط با حوزه کسب‌وکارها هستیم.
🔹
بیشتر موانع را از میان برداشته‌ایم تا با وجود محدودیت در دریا، راه صادرات و واردات و تعاملات اقتصادی با کشورهایی همچون پاکستان، عراق، ترکمنستان و آذربایجان از مرزهای زمینی گسترش یابد.
🔹
برای آنکه در مقابل دشمنان سر خم نکنیم، همه باید دست به دست یکدیگر بدهیم و موانع را از سر راه برداریم؛ با هماهنگی و وحدت می‌توانیم دشمنان را ناامید کنیم.
🔹
سران قوا به دنبال این هستند تا مسیر فعالیت‌های اقتصادی و بهبود شرایط و معیشت مردم هموار شود؛ بنابراین از طرف سران قوا قول می‌دهم با تمام وجود موانع را در راه خدمت به جامعه برداریم.
@Farsna</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/465672" target="_blank">📅 15:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465671">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4e7deded0.mp4?token=J5dYhYLvmk4Thrh1V62g0rLon4Qd1xcrH5V9KDb3lJrS-0nikSwP42G7gQfVmiq-vlZ7QDozjAqDPffmxph17gdeeQYetlE9JsTtgfCUavaAMiHQ-lVSu-9sfkQG6fnNrQQSGT63sjbeYj4-Z4zqxKkKE4D4D49b8ADIPOymGRorLBwa8x7yxn-aXwHfGHy9J12CavJJjHBaHssXvX29ZHh7T-D1caC9jIBLY5wMIRBD7jJSjZUrTZVuSFNNqjiURjGFI-3xoS2eJu9aA_ShM52X1NMN-MMwyrMtSYri7afCzhflycvGZHQwO2mOStHSlvHNauX0sXO2iy4W4nt-3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4e7deded0.mp4?token=J5dYhYLvmk4Thrh1V62g0rLon4Qd1xcrH5V9KDb3lJrS-0nikSwP42G7gQfVmiq-vlZ7QDozjAqDPffmxph17gdeeQYetlE9JsTtgfCUavaAMiHQ-lVSu-9sfkQG6fnNrQQSGT63sjbeYj4-Z4zqxKkKE4D4D49b8ADIPOymGRorLBwa8x7yxn-aXwHfGHy9J12CavJJjHBaHssXvX29ZHh7T-D1caC9jIBLY5wMIRBD7jJSjZUrTZVuSFNNqjiURjGFI-3xoS2eJu9aA_ShM52X1NMN-MMwyrMtSYri7afCzhflycvGZHQwO2mOStHSlvHNauX0sXO2iy4W4nt-3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
علیپور به نیمه‌نهایی
صخره‌نوردی صعود کرد
🔹
در ادامهٔ رقابت‌های سنگ‌نوردی رضا علیپور، در مرحلهٔ یک‌چهارم نهایی ماده سرعت مردان، با ثبت ۵.۰۴ زمان و قرار گرفتن در جایگاه دوم گروه خود موفق به صعود به مرحلهٔ نیمه‌نهایی شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/465671" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465670">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🎥
صحبت‌های شنیدنی حسین یکتا در خط مقدم و  نقطهٔ صفر  نبرد با رژیم صهیونیستی هنگام وضوگرفتن در رود لیتانی
@Farsna</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/465670" target="_blank">📅 14:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465669">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2906dbbe59.mp4?token=mfNBOLMoKnq69QzJJjXSxDtoFN-jpA4ksy_Bd25BW15rkwxVqLwaGRN1u82kBAYBASA3CEvvW1A78xtYa7lBxi8S3CKW_VdG066Q_8RYMvPScT5BIP5FjmGbpFZCuNefsboDHb8gA2fkwSOsIMKOyQRR5N7lsDVOSdXpuvORx9UlB0BNNnw4xH0oJGWcSXwClDT6PCrG0CqCsYgDBSoeAeJvEM-wOTuNSgbFGkRMdedpgQRR5stTYYx_qUYq0yCvBWY_efy2edTiQKMv4jYieTKxfE8lMwxaR7FscDxdUdmzUUXcNw8ddvPtB_hPlkWun6dZPvCqLQZYcYb_60mEi2rXSsjkkj243_9a8XvqHSb_SMsjb--ANc3e14iKMwC39vtKibLH5R5BuaKbkTuLXMsojBCrMBLSosRKhGsTDWMP59pDRt2FciA6ld7Aco4HUXZP6vLt6ObhuBrFEgC5swaUOGem73jQoyE-EsWJQThbgX-_sn7VTCUgBhn_ytLw_WwlIX7ST7SmqB8wXwaLPskf9CTBlASe1SHmJ8SFS8exGiayLDJ0Zg5J_hFlYsiZmQyP7Jrt_zKTmoXhZTeNBz8MTQ06XHs66thlf2k8nGVNh94hLV_k2VNOIIUfEpLBngrbOKaxP9qtzUTp1kYcCUZcpmNldND_dUP6jCW1__Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2906dbbe59.mp4?token=mfNBOLMoKnq69QzJJjXSxDtoFN-jpA4ksy_Bd25BW15rkwxVqLwaGRN1u82kBAYBASA3CEvvW1A78xtYa7lBxi8S3CKW_VdG066Q_8RYMvPScT5BIP5FjmGbpFZCuNefsboDHb8gA2fkwSOsIMKOyQRR5N7lsDVOSdXpuvORx9UlB0BNNnw4xH0oJGWcSXwClDT6PCrG0CqCsYgDBSoeAeJvEM-wOTuNSgbFGkRMdedpgQRR5stTYYx_qUYq0yCvBWY_efy2edTiQKMv4jYieTKxfE8lMwxaR7FscDxdUdmzUUXcNw8ddvPtB_hPlkWun6dZPvCqLQZYcYb_60mEi2rXSsjkkj243_9a8XvqHSb_SMsjb--ANc3e14iKMwC39vtKibLH5R5BuaKbkTuLXMsojBCrMBLSosRKhGsTDWMP59pDRt2FciA6ld7Aco4HUXZP6vLt6ObhuBrFEgC5swaUOGem73jQoyE-EsWJQThbgX-_sn7VTCUgBhn_ytLw_WwlIX7ST7SmqB8wXwaLPskf9CTBlASe1SHmJ8SFS8exGiayLDJ0Zg5J_hFlYsiZmQyP7Jrt_zKTmoXhZTeNBz8MTQ06XHs66thlf2k8nGVNh94hLV_k2VNOIIUfEpLBngrbOKaxP9qtzUTp1kYcCUZcpmNldND_dUP6jCW1__Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عبدولی طلای آسیا را صید کرد
🔹
علیرضا عبدولی در یک کشتی حساس در دیدار نهایی وزن ۷۷ کیلوگرم بازی‌های آسیایی ناگویا، با پیروزی ۵ بر ۳ مقابل قهرمان المپیک از ژاپن، مدال طلای مسابقات آسیایی را شکار کرد. @Farsna</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/465669" target="_blank">📅 14:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465668">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZS3E_bb6q5vI96EM2i-ckY1yVJ0CBSTeaJ4kj1mT6detJf12at6Pd5HCiwuvxjshbGTw5kOGZLa51-f5jiDLa0eSiQjQdS_ksAPVhIF9LxYnn3nbvPvWehd41EFQfy-GJTnH3f2Vbs2vOE0SKycDffLeW9lSOm1KH8kJU1Gk4mhdg7Vr8EGr_1BZWVB2A4nxUbLJjYFCH89Pffj4vKeOFTTkHmI4vg9FMwoM78nez7nmNYLRcAb-JXnEt1MXP4D8qlIw4wg6EBN1_lbSwbIhm5Vyovqz64MIawuFmpAb4Dus5MI4LgOX_E_wf8UizPVmlLDCspeI0RLqKrXehDsqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتراف نیروی دریایی آمریکا به خودکشی ۸ ملوان در پایگاه اوکلاهما
🔹
نیروی دریایی آمریکا تأیید کرده است که در فاصله سال‌های ۲۰۲۵ تا ۲۰۲۶، هشت ملوان این نیرو در پایگاه هوایی «تینکر» در اوکلاهما سیتی خودکشی کرده‌اند؛ رخدادی که بار دیگر نگرانی‌ها درباره وضعیت سلامت روان نیروهای نظامی آمریکا و شرایط کاری و زندگی آنها را افزایش داده است.
🔹
به گزارش «میلیتری تایمز»، این هشت مورد خودکشی در واحدهای وابسته به واحد «ارتباطات راهبردی یک» نیروی دریایی آمریکا رخ داده است؛ یگانی که مسئولیت بهره‌برداری و پشتیبانی از هواپیماهای E-6B مرکوری را بر عهده دارد. این هواپیماهای بوئینگ ۷۰۷ اصلاح‌شده که گاهی «هواپیمای روز قیامت» نامیده می‌شوند، در صورت وقوع بحران اتمی برای برقراری ارتباطات امن و فراهم کردن امکان فرماندهی و کنترل نیروهای هسته‌ای آمریکا مورد استفاده قرار می‌گیرند.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/465668" target="_blank">📅 14:39 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465667">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ec8467d36.mp4?token=sQsNsP6gMYx8v4eDDXb0_zYR17KlFTkPtkaxFEtsxWhEF14F7JjVVP7sFzfOEzVe6xw9J2v_Tp1-JrvXiAAqk7dPINC0FRrb_XYVm1yPkJA7onxulOp57OnT2EDlbVV2xwgk-oQ98UhZC0Ebz5g9UhWJZO9mDSCzV0NlqZldMGz9tAbRseWMDyyjMmjaCffmnh7mR4jl6fJlsfOJSSf21X5JZb-3lCq2etN0GtRwZlPKbde3R9DntgnmCyqFF1iOyfp72xXcr8-A9F1DsMYAQxorUe0AVZ3xtS6WXLhdULOGowj_Z5EHLgY0_XoPY3wU1ccwJhqYd1YU3azpBPPt_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ec8467d36.mp4?token=sQsNsP6gMYx8v4eDDXb0_zYR17KlFTkPtkaxFEtsxWhEF14F7JjVVP7sFzfOEzVe6xw9J2v_Tp1-JrvXiAAqk7dPINC0FRrb_XYVm1yPkJA7onxulOp57OnT2EDlbVV2xwgk-oQ98UhZC0Ebz5g9UhWJZO9mDSCzV0NlqZldMGz9tAbRseWMDyyjMmjaCffmnh7mR4jl6fJlsfOJSSf21X5JZb-3lCq2etN0GtRwZlPKbde3R9DntgnmCyqFF1iOyfp72xXcr8-A9F1DsMYAQxorUe0AVZ3xtS6WXLhdULOGowj_Z5EHLgY0_XoPY3wU1ccwJhqYd1YU3azpBPPt_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سقوط مرگبار بالگرد پزشکی در کالیفرنیا
🔹
سقوط یک بالگرد در کالیفرنیای آمریکا به کشته‌شدن ۲ نفر، انتقال ۲ نفر دیگر به بیمارستان و مفقودشدن یک نفر انجامید.
🔹
به گفتهٔ مقام‌های لس‌آنجلس این بالگرد اندکی پس از برخاستن از جزیره کاتالینا در نزدیکی لس‌آنجلس سقوط کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/farsna/465667" target="_blank">📅 14:39 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465666">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDtbewkIxLBTm5n-YG72m3QmiScOt17QIR65xcTdVBPB5dOJ5WtZeV887SzhRmgbvy-epOgBNBl6gY3O0UuScZ1HlMMwTrF_g7-goi-YgDcOvus0lPMR_bqu5bw5Nt76ee1Ds_BDlE76nCNmRBISW0wESRCWL059CI8zIqLthScL5wLn0G4HV38WaZHqc-R1ru6FyT9z075mCFzjNL0simgbUS2PllTmVsTS0DND1H2ftT1d4pIEAq7YbMmZBGGwcTeM5h2_qqPojg90NnKYtRZyNCzXQqjxoYx0SzwqSqn0eLXYO1PbC_hkhG948H_-iFxUe5q6QL9oSM3UUuxlVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
اجتماع گستردهٔ مردم زنجان در رزمایش جان‌فدایان  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/465666" target="_blank">📅 14:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465664">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9669fdc33.mp4?token=R6JEmsTnzVSPvae2cTR217rOwSEXDanEOVVHiihT-rbGJEEnvQ7VP5c6tVzhzCr9aXELvWwQEkIwy_9tXG6bpI_iYcwT9dyD7XWRfKTRoRZXtdiEfSBh_HJkocSonZzE1RXCBsql0EzrxDXb-p7ibJlS4ak1d1WlzzHXXT8jmxTuZ3M2T5b86bba0U4vt6pTpIhAodsQvnG0hn2qgg6Mhqa1ie73qNMBGBVpQUuCozL-83GSmlxjpGoJ7x6BmyM2PsbL9hSgPC8C6FBvlwyj1xCTtB6mN5ZwGsw1jTc9h5cHS0M5fDJ8OGfWjT14EsaZydQDcbg1jvi04cWWIA6JGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9669fdc33.mp4?token=R6JEmsTnzVSPvae2cTR217rOwSEXDanEOVVHiihT-rbGJEEnvQ7VP5c6tVzhzCr9aXELvWwQEkIwy_9tXG6bpI_iYcwT9dyD7XWRfKTRoRZXtdiEfSBh_HJkocSonZzE1RXCBsql0EzrxDXb-p7ibJlS4ak1d1WlzzHXXT8jmxTuZ3M2T5b86bba0U4vt6pTpIhAodsQvnG0hn2qgg6Mhqa1ie73qNMBGBVpQUuCozL-83GSmlxjpGoJ7x6BmyM2PsbL9hSgPC8C6FBvlwyj1xCTtB6mN5ZwGsw1jTc9h5cHS0M5fDJ8OGfWjT14EsaZydQDcbg1jvi04cWWIA6JGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ کشتی‌کار ایران هم راهی رده‌بندی شد
🔹
مهدی بالی در نیمه‌نهایی وزن ۹۷ کیلوگرم کشتی فرنگی مقابل ناکازاتو، حریف ژاپنی‌اش ۵ بر چهار شکست خورد و به رده‌بندی رفت. @Farsna</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/465664" target="_blank">📅 14:28 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465663">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DL-1Ik8oDlNCo7iuvMXdrEVv-ijWbnY7T_c5pqnQhi_boP2-f9jREM9DvWtlnKuPIQq2wuc3mudaP2uoixRqrsCF43hdXOAS9DE1dnvDXqpdh73pOYCaI1tTjXjy7O10WBQfkju66tLU26vwoGRA35xC3mub-jJLbGtnf03K0jSZj2oS_0bqtZKbzrPkJPl7M00q2UH2hyVXPfNl2ALkX3U-mJQFjCG2jBm6op9y9jldcwvI708O4P9_SMYzbSQT7n2OLbdWM3UoAOIMA7rIW9oFvFzmK6HVwafMx1Smq61jwk0RHiPFasTgstZrkraBpGxSoiEOm39tfNBE-rDXtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام قاطع تهران به بغداد: برای صیانت از روابط تاریخی فوراً اقدام کنید
🔹
در حالی که آمریکا تلاش می‌کند با اهرم تحریم، روابط راهبردی تهران-بغداد را  محدود کند، سفارت ایران در بغداد با رویکردی قاطعانه از دولت عراق خواست با اتخاذ یک تصمیم فوری، از روابط دو کشور در برابر پیامدهای این تحریم‌ها صیانت کند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/465663" target="_blank">📅 14:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465662">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb78d8f11f.mp4?token=ZN-VbZu3lVKWwHZEaMt9SGImrdXW4f5pq3NXTUMd8IOxBBBq57XaBLLouMv2IzmGYtboFw8u1RBpx1zNwBhXoiRmOdLlSEpl6riH81sBEzUZXtUo0X-BN69mX4eV5nxf-ZW7a-0qIZoP6DRR-mt5j3JRRNp7zkVVEOS8y3NsXs6TcwpXNYnlLsnxdqQIcAxOXN0dsedF7iIKqZr7p9DDx0-bjResePO_vf_Xu46UCx2gwLreEKV4eZtwbiPn6tkBkPjYP3HQ_sCSFrlmCrmhWZDSldc7Kw6jmv8CQNkDM-wfuJdAkl4HfmfoR_9THwx0jBRU77LZYkxRhH4sVdngYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb78d8f11f.mp4?token=ZN-VbZu3lVKWwHZEaMt9SGImrdXW4f5pq3NXTUMd8IOxBBBq57XaBLLouMv2IzmGYtboFw8u1RBpx1zNwBhXoiRmOdLlSEpl6riH81sBEzUZXtUo0X-BN69mX4eV5nxf-ZW7a-0qIZoP6DRR-mt5j3JRRNp7zkVVEOS8y3NsXs6TcwpXNYnlLsnxdqQIcAxOXN0dsedF7iIKqZr7p9DDx0-bjResePO_vf_Xu46UCx2gwLreEKV4eZtwbiPn6tkBkPjYP3HQ_sCSFrlmCrmhWZDSldc7Kw6jmv8CQNkDM-wfuJdAkl4HfmfoR_9THwx0jBRU77LZYkxRhH4sVdngYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هلاکت ۶ نفر از اعضای گروهک تروریستی در زاهدان
🔹
قرارگاه قدس نیروی زمینی سپاه: ۶ نفر از اعضای گروهک تروریستی تکفیری به هلاکت رسیدند و تعدادی هم بسته‌های انفجاری از آنها کشف شد. @Farsna</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/465662" target="_blank">📅 14:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465661">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4de848d651.mp4?token=KOlwfJlZtcFLHx1XiTrMkwB2ohDtNKRCKqgZUp8uThANQ_c9k8xuwDq1g8_HPRhWTqgG1d0LBgiJZpLvAPyy3zriJHdnsN5ybPFwSncev8YMq1UWrvgArrylGtKQBS-f6Q2VS-jyShoYTT10YRCkt4sxxAdGDJkVBfkqVRTfnwTiRskzxpPqUYISIlM8NMJ-Au0LRYvGJKLyBUjoXIP8L9P2OPVgX8501Ajd_xlQ-auaYYBQcFTI7imS3khqU_rBEvRTUqfKlzqiykxyf3XFZ1S_qzp2c5faGRERrl2SJal9EVn42M9TWX0vNiKkbCP0fxC5JTpqIi8BKO1eUDpeICutIs7lwiNLN15Rk-ZyYD6LM4UyV6-es54wYK5rKn_R4yqFQOdBj5Rf-rcC1qKWMEeT5QJdUG4XbwjKx8PHjv5WKG9KkZEA_bBtiErKMSuyfjVFmYrRGeac2bYSmpuQJV6D9wZG9r3poYNyx6GidUKhLLMwTf5zi2W7d_mK8qEauR4M_2ziAC0ruLofqCXi5YBrFrQowTgP3yilI5x_MkoTwBBG3KE0CkaEz5rZr9PMC6hszrOW18rcbUexlzaURCHsqB_QkM3Lzs3ONT2C1qSyPRWTI1rsYjcILcdsCNn-6ywp_7MkBtV4ct9j9cV-P94gRoABRr4U8fi2gurwo2E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4de848d651.mp4?token=KOlwfJlZtcFLHx1XiTrMkwB2ohDtNKRCKqgZUp8uThANQ_c9k8xuwDq1g8_HPRhWTqgG1d0LBgiJZpLvAPyy3zriJHdnsN5ybPFwSncev8YMq1UWrvgArrylGtKQBS-f6Q2VS-jyShoYTT10YRCkt4sxxAdGDJkVBfkqVRTfnwTiRskzxpPqUYISIlM8NMJ-Au0LRYvGJKLyBUjoXIP8L9P2OPVgX8501Ajd_xlQ-auaYYBQcFTI7imS3khqU_rBEvRTUqfKlzqiykxyf3XFZ1S_qzp2c5faGRERrl2SJal9EVn42M9TWX0vNiKkbCP0fxC5JTpqIi8BKO1eUDpeICutIs7lwiNLN15Rk-ZyYD6LM4UyV6-es54wYK5rKn_R4yqFQOdBj5Rf-rcC1qKWMEeT5QJdUG4XbwjKx8PHjv5WKG9KkZEA_bBtiErKMSuyfjVFmYrRGeac2bYSmpuQJV6D9wZG9r3poYNyx6GidUKhLLMwTf5zi2W7d_mK8qEauR4M_2ziAC0ruLofqCXi5YBrFrQowTgP3yilI5x_MkoTwBBG3KE0CkaEz5rZr9PMC6hszrOW18rcbUexlzaURCHsqB_QkM3Lzs3ONT2C1qSyPRWTI1rsYjcILcdsCNn-6ywp_7MkBtV4ct9j9cV-P94gRoABRr4U8fi2gurwo2E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار بلالی: هر چقدر لازم باشد موشک می‌زنیم تا دشمن ادب شود
🔹
مشاور فرمانده نیروی هوافضای سپاه: نرخ شلیک موشک‌های ایران به‌گونه‌ای است که حتی در صورت تداوم رویارویی برای چندین سال، امکان ادامۀ عملیات با همین نرخ وجود دارد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/465661" target="_blank">📅 14:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465660">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d49320b4a.mp4?token=d7Rp1m5WaPL8prqb34zsg-qOy4gyLETIWqmXHOWAfeS-MhLMUoMpYNy2GKHV9bQSxbxM_t-6t8jdwxMQ_FhFiD6qWHNUSQJQnDKakrP8p88HO0_I759XBtKV_h5QNqIVoC9b9rgqxCrY_zwKcrUFGIuA5FgsMg9Zr_GLXxkuTTnHjIazcUnxzCdWxUpBALd-wwE4_7GPDzrxutrTMwmRu_HHM4PPwfpot6-W9pSokTZ4XSZd7JOkOFqYUcsji4hMGO1VOYWk-AilK-6zX5tpXhziWBDHkXec-muap4fPCdBrheF4JV5yV7Gs8FovfJGBfTKYkqa_QqBU8D_3Lf28dR3TNY-hyVqy14J9WBok-D22PmG2EPvWN_4G7YOXW1BTzjuqA8vCtTqq2MYyvyesxymdhihUB8os2pTROUA559Db9I92rpjd0VxPxiANnrtnDsP2eKEB9wFr_XmfepaXiBIXmKdZyKmFJecJLI9jQKJuFzE0DYTCVbxl6jcFkrFkfaPNkugxKrM3-eBZR3eHPAc_hChr9KBsIVCAh_srQ66diqFI8Jb9-k0SL_bKkL3wxOM8DAbMBOSNDDuRzCnPqSJkRZ5q7rbBkGbUduWxDLCa0CjmRaYn-qbt72LJyIneiQbQ3AW3ki_WJJX0vPrTbUd-m1KTf0_kyRWNYytd4QM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d49320b4a.mp4?token=d7Rp1m5WaPL8prqb34zsg-qOy4gyLETIWqmXHOWAfeS-MhLMUoMpYNy2GKHV9bQSxbxM_t-6t8jdwxMQ_FhFiD6qWHNUSQJQnDKakrP8p88HO0_I759XBtKV_h5QNqIVoC9b9rgqxCrY_zwKcrUFGIuA5FgsMg9Zr_GLXxkuTTnHjIazcUnxzCdWxUpBALd-wwE4_7GPDzrxutrTMwmRu_HHM4PPwfpot6-W9pSokTZ4XSZd7JOkOFqYUcsji4hMGO1VOYWk-AilK-6zX5tpXhziWBDHkXec-muap4fPCdBrheF4JV5yV7Gs8FovfJGBfTKYkqa_QqBU8D_3Lf28dR3TNY-hyVqy14J9WBok-D22PmG2EPvWN_4G7YOXW1BTzjuqA8vCtTqq2MYyvyesxymdhihUB8os2pTROUA559Db9I92rpjd0VxPxiANnrtnDsP2eKEB9wFr_XmfepaXiBIXmKdZyKmFJecJLI9jQKJuFzE0DYTCVbxl6jcFkrFkfaPNkugxKrM3-eBZR3eHPAc_hChr9KBsIVCAh_srQ66diqFI8Jb9-k0SL_bKkL3wxOM8DAbMBOSNDDuRzCnPqSJkRZ5q7rbBkGbUduWxDLCa0CjmRaYn-qbt72LJyIneiQbQ3AW3ki_WJJX0vPrTbUd-m1KTf0_kyRWNYytd4QM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقدامات قطعی دشمن در روزها و ماه‌های آینده!
این ۳ دقیقه به اندازه ساعت‌ها دوره عملیات روانی و سواد رسانه ارزش دیدن دارد
@Fars_plus</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/465660" target="_blank">📅 13:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465659">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GI1odwbmaWuYzahdVz1C3QEnAoMZCMvYSMIJLcr0e_TaNZqvnt2gIbuQfsybjBko1-lDjLTriMjmKWXwQ6UoAl2fhVTBMgw7gz_rLDIdOMPTU9YKDyQmc1jNTSY_Ps6jIPyNISg25lLb6ZZxJ6e1nPUg_0JD3ujxXuMuOD2-ntHvazOHF1J5_uyAl6p5HwPwLTJf0uMY4qPhyl0Cmb0RGzoFDqlK4XQ0wxUIq7YzuIAGY4dCMBMpxa6WfpbqTvEcPm70SRpdB0SzsGz4n3arG8OKtGTWc2xv7Gz-dq_v81JBubZ5zPMl8jmYLqLUeEtvRdDLNvFF04dq2BlxsxUi0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
عبدولی طلای آسیا را صید کرد
🔹
علیرضا عبدولی در یک کشتی حساس در دیدار نهایی وزن ۷۷ کیلوگرم بازی‌های آسیایی ناگویا، با پیروزی ۵ بر ۳ مقابل قهرمان المپیک از ژاپن، مدال طلای مسابقات آسیایی را شکار کرد. @Farsna</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/465659" target="_blank">📅 13:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465658">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b271ab9f73.mp4?token=PUZmqd0TbXADQoGiFQySkoMQuTPTkIKOWlvoTiCnJFJuzqHLB7xu6i8SIslfol1DtODeU_-ixu4Gs9S4g-obtV69Nd4CENBoKJSMLJ1g5Vz1wKtUYwOP-ZGSI997--8WY8ubppLQnjd_BxgseF5ENypjzOeBSMulhcS2V9HZdWgfiDPUEowAUZ2s7xwbkgRzhnZDiBamTNzU78v8zLCQQMN0f4wSh4ZgwtuF4lYe1LNSzxXY9VCcJc7RWcgJRMOEjuTN2BNSs4APffgpk-vFDtO-4ILPkieCTHPayUjDyt1g9E-F5aZHjN3wFdWi2Hbns9e7KC6E33gxVGcbkgvY2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b271ab9f73.mp4?token=PUZmqd0TbXADQoGiFQySkoMQuTPTkIKOWlvoTiCnJFJuzqHLB7xu6i8SIslfol1DtODeU_-ixu4Gs9S4g-obtV69Nd4CENBoKJSMLJ1g5Vz1wKtUYwOP-ZGSI997--8WY8ubppLQnjd_BxgseF5ENypjzOeBSMulhcS2V9HZdWgfiDPUEowAUZ2s7xwbkgRzhnZDiBamTNzU78v8zLCQQMN0f4wSh4ZgwtuF4lYe1LNSzxXY9VCcJc7RWcgJRMOEjuTN2BNSs4APffgpk-vFDtO-4ILPkieCTHPayUjDyt1g9E-F5aZHjN3wFdWi2Hbns9e7KC6E33gxVGcbkgvY2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ عبدولی همشهری‌اش را برد و فینالیست شد
🔹
سعید عبدولی در نیمه‌نهایی وزن ۷۷ کیلوگرم کشتی فرنگی بداغی، کشتی‌گیر ایرانی‌الاصل قطر را شکست داد و راهی فینال شد. @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/465658" target="_blank">📅 13:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465657">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GOPuubrnGJSzNY8QWchdcC1U0vxwGdoNWkdMMvcvtO3a4lfkFp-4ni-HnJnOO3lBSW99J6b_UGT-8jMRdUfqoYjP8ad5yCAyhiZLmRI-EgHl9UG8aUPAO_TXKMRjZ9mxXgQqjdNtOYCmdypeXAQf71xRU58-r02Q6bGCa_6x9QZsJa_rUEWbBJu8O23nEc8J37uo3JhQmDitotiQPiER9p6TbQumilRdZfXYE5BZz1tHhpqFuInJTWJJ0oBn0sFOu6Sk5PazG8FLNINF75loTRZ1RRBy1j6iyVQwRnDSfB34NRh_fmWPZHL2bjR1VUPS4c8RlufaXqo5LD9tBN7QOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انهدام ۷۸۰ باند قاچاق موادمخدر و کشف ۲۵۰ تن مخدر در کشور
🔹
رئیس پلیس مبارزه با موادمخدر فراجا: در ۶ ماهٔ نخست امسال بیش از ۲۵۰ تن انواع موادمخدر کشف شد.
🔹
در این مدت بیش‌از ۷ هزار قاچاقچی و توزیع‌کنندهٔ عمده دستگیر و بیش‌از ۷۸۰ باند فعال موادمخدر منهدم شده است.
🔹
همچنین حدود ۸ هزار خودروی مرتبط با قاچاق موادمخدر توقیف و بیش‌از ۳۳۰ سلاح غیرمجاز کشف شد.
🔹
۱۹۶ عنصر اصلی قاچاق موادمخدر در فضای مجازی نیز دستگیر و بیش‌از ۴۶۰ کیلوگرم موادمخدر از این افراد ضبط شد.
🔹
در یکی از عملیات‌های مهم، یک باند قاچاق شیشه که از شرق کشور به‌سمت مرکز و غرب فعالیت می‌کرد، منهدم و ۱۱ عضو آن دستگیر شدند. در این عملیات بیش از یک تُن شیشه و حدود ۸۰۰ کیلوگرم تریاک کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/farsna/465657" target="_blank">📅 13:40 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465656">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a8da3574.mp4?token=OQf9T-E0qLJfF8NIcbpM2aVeociRbkoAJSMP6dhaIwA1I7v5z45Tla9krPGcFSTUyEvRH3WDNKIm7_NvODOZNmnuBx0vSjttgln0nFu5H0A_TmSUmsce35b1q6F-VrsVmRxXCZmimvtr1a80R9qKJMnkoAQtlc6ARvX1EIvroSei0ZsEeST1ruH3L8V9PvP0vTgZmraTKM-daI9j0n34HOKmciy6BVyE8oLQspDW7-k5RFUXBT6bwMp3JyBwYsZnOTvaqLhQSVQ9SycaeFyxiZt3xPGxg6-aKSY3ApAQ-ZjnYdIKdEqGjKAB8Gvgxi_JvrBNsQQWPX5jvDajijuUrUPYI88FYC85-yQUt_njXdkTBJ-zb64rFyAoXgW_RRbOuT3lWRSWqzfMS-JILKo8ilViqRl_X6hOOBTg66hn7De4XN9VYfSqC1OE_NDidXBIekrPfFoiRlh2w1qS1VUGbMMc3k1XctLP2lC2zynFIDM9RN36_Z-RVsqLY7-NCUNDDS17mSXAIaLZ32ZHLtv0-pTro45VQzHfUFMDf1SFsQAfuR9bo3avM1vLkj--I1r5KW-H5i-ZdhOxRAaMjufBwlxNbb6YG2Q8nVz_69qQs5_mvC6slDHYLsJi8ZlotAi3tXnplGiNCaPRBSEjcCDbbt9UTYptlJtyROMfgyDIsQM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a8da3574.mp4?token=OQf9T-E0qLJfF8NIcbpM2aVeociRbkoAJSMP6dhaIwA1I7v5z45Tla9krPGcFSTUyEvRH3WDNKIm7_NvODOZNmnuBx0vSjttgln0nFu5H0A_TmSUmsce35b1q6F-VrsVmRxXCZmimvtr1a80R9qKJMnkoAQtlc6ARvX1EIvroSei0ZsEeST1ruH3L8V9PvP0vTgZmraTKM-daI9j0n34HOKmciy6BVyE8oLQspDW7-k5RFUXBT6bwMp3JyBwYsZnOTvaqLhQSVQ9SycaeFyxiZt3xPGxg6-aKSY3ApAQ-ZjnYdIKdEqGjKAB8Gvgxi_JvrBNsQQWPX5jvDajijuUrUPYI88FYC85-yQUt_njXdkTBJ-zb64rFyAoXgW_RRbOuT3lWRSWqzfMS-JILKo8ilViqRl_X6hOOBTg66hn7De4XN9VYfSqC1OE_NDidXBIekrPfFoiRlh2w1qS1VUGbMMc3k1XctLP2lC2zynFIDM9RN36_Z-RVsqLY7-NCUNDDS17mSXAIaLZ32ZHLtv0-pTro45VQzHfUFMDf1SFsQAfuR9bo3avM1vLkj--I1r5KW-H5i-ZdhOxRAaMjufBwlxNbb6YG2Q8nVz_69qQs5_mvC6slDHYLsJi8ZlotAi3tXnplGiNCaPRBSEjcCDbbt9UTYptlJtyROMfgyDIsQM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رزمایش جان‌فدایان با حضور پرشور مردم زنجان آغاز شد  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/465656" target="_blank">📅 13:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465655">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdd59013c8.mp4?token=SkJY9qsmNRq3sPyiQATgR53AXXMSOHyau9wDO5Nq4izZoZZbWVBzqsQNkQ8q_fWxhg0awsh92V9SN6mDd7LHk-x2_j592Vwri-9DeU-1iB_ElLCZe_8w5yZdniMQPgvlPqUWluEPd_Lok090gKV5bTl6GUHtu_iFCK0nrFCmdJDTxAoa0rHdtHycdqDxqF6qGwU0N9qEkO6pzMsSZ8vnaOgUpV2jTz_gq2LF3aD43c8EFGHVhzECZVD1okBS3_uchqCdNNpyUIf4pcZtypFaYg96DKzjzZcoCTaLagEB1k-_E_50s_mIsrcWJwkZVWyL8KmMvR69lMrHUYQUT3E2RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdd59013c8.mp4?token=SkJY9qsmNRq3sPyiQATgR53AXXMSOHyau9wDO5Nq4izZoZZbWVBzqsQNkQ8q_fWxhg0awsh92V9SN6mDd7LHk-x2_j592Vwri-9DeU-1iB_ElLCZe_8w5yZdniMQPgvlPqUWluEPd_Lok090gKV5bTl6GUHtu_iFCK0nrFCmdJDTxAoa0rHdtHycdqDxqF6qGwU0N9qEkO6pzMsSZ8vnaOgUpV2jTz_gq2LF3aD43c8EFGHVhzECZVD1okBS3_uchqCdNNpyUIf4pcZtypFaYg96DKzjzZcoCTaLagEB1k-_E_50s_mIsrcWJwkZVWyL8KmMvR69lMrHUYQUT3E2RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امضای سند راهبردی دیپلماسی قضایی تهران و مسکو در کازان
🔹
در حاشیهٔ اجلاس دادستان‌های کل کشورهای عضو سازمان همکاری شانگهای، سند رسمی «برنامهٔ همکاری بین دادستانی کل فدراسیون روسیه و دادستانی کل ایران برای سال‌های ۲۰۲۷ تا ۲۰۲۸» امضا شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/465655" target="_blank">📅 13:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465654">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYqm1Iqe6Ta68BxeskHevnQ6oPGG3N4EaTDOTTvqFmkbv-iVPVeO1Q9FNEQamLx3vHLHPOcUclF7Fz4H0ts4XjR8BpatZeZbGLXFZer8JHEzBl6amfaT8Vzs-gvTMJ8B4fS8R81hdTjaNoobQJSq_HhlP5fCqvIH8W1EcJ4Kx7ev1WYI85C8VgkblmTdUoSf74Fmzv205MMhxMQx98l_9JJnnXwmP3tOgNJt7XjCBJNV897u5JlOYhdMnzbIZGGJXJ4UtA24suv6GQoyqKlYR_t1YQuxHiNJ6jBPAFI_UsNRanWlygK6Sd4vZ58eNzLdSbhn7AZlQfuwUMpwaLxe6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۴۹ سلاح غیرمجاز در اصفهان
🔹
فرمانده انتظامی اصفهان: ۴۹ سلاح به‌همراه اقلامی که در کنار این محموله قرار داشت، کشف شد.
🔹
در این رابطه چندین نفر از قاچاقچیان سلاح دستگیر شدند و چند دستگاه خودرو نیز ضبط شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/465654" target="_blank">📅 13:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465652">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9Ioxnal8dQa07_ZvCZbzFm6IN9qnx28U9ZEAZwglfNh-N2O27eADJ-CPvVmVVWdMR_Bc3H-BquHaqc_d770_HwcoZHoq08CoGnUIdwI_iic-dmKxOtREUM6WU1MggNzhG2M5KPkwWYFDW9mkayL7KiWRbsg5EB037AS-AtFYoz8xAVUyJjebvAvJyTdOSii6b7-QA_aHll0tsvG4U1EadFakW4iFqEa-P2K0J-roX9ZSFDxx_54Wek94r7x_AvVXWPQeDLE-S0gW8gl8opvhq_u7Ox__mMWdBexToPVdOaydGrgXnE6RtThLXlw5pDog-rBz6uoRqJgAAMuVwpnOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ عباس‌پور به فینال نرسید
🔹
سجاد عباس‌پور در وزن ۶۰ کیلوگرم کشتی فرنگی ۸ بر ۴ به گانیف، نایب‌قهرمان جهان باخت و به فینال نرسید. @Farsna</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/465652" target="_blank">📅 13:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465651">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBj0nVbZp1YsYg4SPPPKG4E06MQr3-J_CxvoON1lx6fnhwJynz_AknIxSFMI1fR6H67qTPXnG6C1-Au4WOG2toeENUd1ynkA10DmmTekQzDZTVqTtXEMmAmrlIczTjG4yfmpp9iAmGpcyxGL1GNHNxxB067yHutD2piM41XoZHf3WLHAvUVP5n0c86aNUxrMIjZiKRVe-c0WV6BwONv0hs3Ka-rJ_NWdTe936qaTOYBRPJR-crNbSqEq4u313l9Yf8V1uOlVSJBYKSYqTXHbli2Qr1aiFVu2CNDBXGaQma8s4dm5Vftssqf_xjcRkwtynyn7o_MUndOuKUZyG7KJ3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ عربستان، مسافران صهیونیست را راهی اراضی اشغالی کرد
🔹
فرودگاه تبوک عربستان اعلام کرد که پرواز فلای‌دبی با ۱۸۰ صهیونیست ساعت ۵:۴۰ فرودگاه را به مقصد تل‌آویو ترک کرده‌ است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/465651" target="_blank">📅 12:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465650">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqTvUmdNF0u4AxgIOImwq100uFtCEpcVgaJtRj57dEvTroHoH6UPSLMp23kbTvCtW24N809O8IHffvcctzCwouwW2XEgnfwBtk7b5czz6UL72g4OT6MNCYlOjNm5LIiSq7YTRCDtncfm6GW-PNiTkXsF71hJZnN7891cmOtkGPtAEK0PckqYA2L8xstFia4WQyL0iIxGyAJLEfjCQyfyCqOBaMS-FXpeESgkdZZCSDlmCrp-ZE__z6yOU4uzXRd1rSBGfztr43X1OmCaFld0x10pZHpWxZy2lNQ0dI0huESV3q-2fypQnoEQcy7KizmtWCnHF_oyScEZZE7bLz0k1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیماها در آسمان عربستان سرگردان شدند
🔹
ترافیک ورودی فرودگاه ابها در جنوب غرب عربستان سعودی امروز متوقف شد و دست‌کم ۳ هواپیما در آسمان این فرودگاه در انتظار فرود ماندند.
🔹
علت این اختلال هنوز مشخص نیست و اطلاعات موجود نیز بسته‌شدن کامل فرودگاه یا وقوع حادثه‌ای مشخص را تأیید نمی‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/465650" target="_blank">📅 12:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465649">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">بازی ایران و گینه‌بیسائو منتفی شد
🔹
فدراسیون فوتبال برای برگزاری سومین دیدار تدارکاتی، با فدراسیون گینه‌بیسائو مذاکره کرد و تاریخ ۱۴ مهر برای برگزاری بازی توافق شد.
🔹
برگزاری این مسابقه در ترکیه به دلیل تحریم‌ها و محدودیت‌های منطقه منتفی شد. گینه‌بیسائو آمادگی سفر به تهران با پرواز چارتر را اعلام کرد، اما به‌دلیل عدم پرواز شرکت‌های هواپیمایی خارجی این گزینه هم به نتیجه نرسید.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/465649" target="_blank">📅 12:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465648">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IB6oHkyf02LrdEXytpxJqa55tv2gL9-FbhuOR1YVUz34aFMRuQE4XarDZMRB6d5jYOw2XiLzA8LNMIlUh4V8IAt9SF6avlqlsMo7_iqZQgEJUJd8kG1QLvudNTgpRT53lum5T_6qA26PMYheB3hW9TZWLpjR-jhZecSPEV7dM9iLRgfcSgDUtEgyw0FBmketHoj44t3t8NGYzCI6PAy0vfNo7D2kTmpR_1A6QzOhE52QrOKI7BQw39oJhY4GhOq77ZUh5XOuM_IEk1TgMk32dgZsHMcYNEzrNVeRXu79Txlia646K_ZYw7NfwC5kzX3uqWr9JP0u0tsXvOAZB2T5OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش بزرگ در تاسیسات گازی امارات
🔹
تصاویر منتشرشده آتش‌سوزی بزرگ در یکی از تأسیسات فرآوری گاز شرکت ادنوک در جنوب‌غرب ابوظبی را نشان می‌دهد و گمانه‌زنی‌هایی دربارهٔ احتمال هدف قرار گرفتن این تأسیسات به‌دنبال داشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/465648" target="_blank">📅 12:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465647">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsrv5SnnNhamBwkWkiiW5EvqhwAwSNJWO-ll2qNmFYkfGoUcuVOhrk-IK-7IrLrGGblv4bvC9tl_NyvN5ppsAEN7bG6bv0O0f3MEkMzMzN1LYbslPvQSn-WzJuYDEyBFtK68nA2hTWgGxeCrLgQoujtXjfmX-hTs1Gv1J4cLKUvstlNF60ELc_0uR4AyH5YME9aO_tpYFc55xwNi10YVQADMnjG0-5vy7YcIgOrIe0U2uop5DGmin15kkkY3acfeEwyq7CIPpkg0stt8l-64vQ6t8nobXn_uKJlDqol3MOhfIKKWv9hlYkEBiYc366lVuYNK_UF0RAgbGq4tGT-hAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترخیص کالاهای دارویی بدون تخصیص ارز کلید خورد
🔹
وزارت صمت ۸۰۳ ردیف تعرفه را به فهرست کالاهای مشمول ترخیص ۹۰ درصدی اضافه و گمرک آن را ابلاغ کرد.
🔹
با قرارگرفتن این ۸۰۳ ردیف در فهرست ترخیص ۹۰ درصدی، واردکننده می‌تواند ۹۰ درصد کالا را پیش‌از تکمیل همه تشریفات و بدون تخصیص ارز از سوی بانک مرکزی ترخیص کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/465647" target="_blank">📅 11:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465646">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ceH6xfTSu7ChvT1haxjQSqDFX3OIthhJROgyIvlsHSt_KLoXmbRfzigO7lm1Ei7YitCT0hBrImnJgqDlODq2uBiWFduFalmYxxgwE7_9pzfqtLtElCVGAPnNWKnxfZTmj8jvSJrBr3KoDiSjENKWsxqTTV5jwmvuKnJHA7JliBfie-vKJOoHuxi_Cex8Mh_4SrJ9aK43qD2_i_veZgPrOuHYcUWcFrCBELIXMgXsqDGgublAU0wHgtx-iyN_dz9WOS6rMNFhGLArZp0uum9BRT7Gy2VxSrNLcdQN9WH0_EVWWk0YUWDq4CtZrgvNN2qWPIAD2s4DIN4zrBtWU85Q3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرائتی: مهم‌ترین جلسات هم نباید نماز را به حاشیه ببرد
🔹
رئیس ستاد اقامهٔ نماز کشور در حاشیهٔ اجلاس سراسری نماز: نماز نباید صرفاً در قالب مجموعه‌ای از مطالب و معارف دینی مطرح شود؛ بلکه باید در متن زندگی انسان و مسائل روز جامعه حضور داشته باشد.
🔹
بررسی زندگی بزرگان دین نشان می‌دهد که نماز یک موضوع حاشیه‌ای در زندگی دینی نیست و از محورهای اساسی تربیت و هدایت انسان به‌شمار می‌رود.
🔹
حتی در مهم‌ترین گفت‌وگوهای علمی و اعتقادی نیز نباید نماز مورد غفلت قرار گیرد.
🔹
ممکن است انسان در یک جلسهٔ مهم علمی یا اجتماعی حضور داشته باشد، اما نماز جایگاه ویژهٔ خود را دارد و نباید مسائل دیگر باعث کنارگذاشته‌شدن این فریضه شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/465646" target="_blank">📅 11:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465644">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6_fBb-FqfS-29cjs61BGw9Fv97nXwrIJyZYoxx74dPGq54ysEm9rdPdUFINfyr_DQeYanYxmwVJF8uWpQyvw8G775ggl_vP6PBgJwQ6pWeJZgZvjsxvAfFcZ7pv5iJSnC5I0AyRJoafSEKDiNY6YWF1aOn4QSbmIuHM-XS-cWvnTmgFEHGlF5sWCvtES8WVmTLewK0B2EcjMef7oDJ8e2vOhdk-WBZb2BY3UoXplC9KvkRLTJfPKJSr24ufk6kFq7c6mbxTzjbQ41FMI__7NH_rN-xON3e4wg4sUiY1fNrebIJQhHrNVhwt5lJ7m6cRE72KuIVlJPbiNBK0cojxgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ برای پایین‌آوردن قیمت نفت باز هم دست به ذخایر برد!
🔹
قیمت نفت برنت بامداد امروز به کمتر از ۹۷ دلار ریزش کرد. این ریزش پس‌از آن اتفاق افتاد که آمریکا اعلام کرد ۴۰ میلیون بشکهٔ دیگر از ذخایر راهبردی نفت خود را آزاد خواهد کرد.
🔹
پیش‌تر اعلام‌شده بود که…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/465644" target="_blank">📅 11:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465643">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RokarQOEPow1l7HnqAj47WiyVCZ74escDm5sQF4ya-1QsfvUbBx-L1Zw1lyNSjxlfvWli46s25x1_jutuvH8nHI0QJebvpEwlpEBAhcExRak-3b91pPN9x_UgKi1NwhcSVv7aLCrmBZ4ZEPRKp-FOoYZyKFflYl1-kX6w9xVip4AqEdJo33HG7wtJmiJiL6Uw1B2tLRN_FtVPzUeB3_-QD6B2E74lxjc6mVZGa99rN5WZ0Y9Ks_n9zUPcLHG3mzDyzvqJVzu9CFMjUwZsbLqlN2cfmbUWaPh4SQuw-QYOzS7wWgYJNAvGgdxBN7pxWRf_1pp4QI-4C9f568WZ_eKxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پکن قید صادرات بنزین را زد
🔹
چین صادرات فرآورده‌های نفتی از جمله بنزین و گازوئیل را تا اطلاع ثانوی به‌حالت تعلیق درآورده است.
🔹
این اقدام در راستای تلاش پکن برای حفظ منابع داخلی و با توجه به کاهش ذخایر سوخت این کشور به پایین‌ترین سطح در بیش‌از یک دههٔ گذشته انجام شده است.
🔹
در همین رابطه، شرکت دولتی پتروچاینا روز گذشته اکثر محموله‌های بنزین و سوخت جت خود را که برای ماه اکتبر برنامه‌ریزی شده بود را لغو کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/465643" target="_blank">📅 11:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465642">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMwby4cd0i9Tep1DqCzVO-GyoUV7ZI31oe8UPzkKWJpJr7ftJ0hMMnjrq8Io_9Nk0pB8JgvCby0a6599exrx6w3PgcxnrSHjh3kB7HznLhUqyR8bl77sBziUi1fMh95XZk9xbILJtlDC3gmf1v3Dx8lAAtKv7Nd1eCQ9VB8yTGMEeWPMaNFZBk4eLOCMIUmVmLEdlb-fchglEIdCthxNtM7KYczg2N9LZ3ceqLE_xp916j2o7a6_Y0PFn2esIFQl2rtv-ZAmUcs4B8booZRkqtZhmXmgRB6dSN-WMNw1uSC58LiOtl3Kc9xoPXnLGxyxnbJq_mPP2qrU_GAf3AyH5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
سیم‌کارت جونیور ایرانسل تجربه‌ای ویژه برای نوجوانان
🔸
سیم‌کارت جونیور ایرانسل، با امکان دسترسی به خدمات آموزشی، فرهنگی و سرگرمی و بسته‌های پرحجم ارتباطی، متناسب با نیازهای کودکان و نوجوانان عرضه شد و خریداران آن می‌توانند در قرعه‌کشی کمک‌هزینه ۹۰۰میلیون تومانی خرید خودرو شرکت کنند.
🔸
پیش‌شماره «۰۹۰۰»، آغازگر پیش‌شماره‌های شبکه تلفن همراه ایران و نماد ورود به نسل نوین ارتباطات و تمایز در تجربه کاربری است.
🔸
خریداران سیم‌کارت ۰۹۰۰ جونیور، نه تنها از این مزیت خاص و نیز بسته‌های اینترنت، مکالمه و پیامک پرحجم بهره‌مند می‌شوند؛ بلکه، به اشتراک‌های رایگان یا تخفیف‌های ویژه در پلتفرم‌های دیجیتال آموزشی و درسی، ورزشی و سرگرمی مانند فرادرس، فیلیمو مدرسه، تام‌لند، مکتب‌خونه، لینگانو، اپتیت، طاقچه، نوار و تیوال+ دسترسی دارند.
🔸
خریداران می‌توانند از اعتبار اسنپ‌پی تا ۱۰۰میلیون تومان و امکان خرید اقساطی سیم‌کارت با استفاده از اعتبار «جیب‌جت» یا اسنپ‌پی استفاده کنند.
👈
جزئیات بیشتر
@irancellnews1</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/465642" target="_blank">📅 11:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465641">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_aBPIZkT_lBDMdcBNFLjYSVuUYAFGi9E2PPYNHyv82hwxYB2EbULOLsvV5Gm1gCUO1puMwGXF0wxWn1U0sKYwEN3APUrNCXeiW7WKgcwtRcef6KHKocidzaBtySw1ls_TTbICz6vtzaD4UFiGEpv5KcbW4WR4Zf7EY2SeUpbj7r8_mulz3Z0drlbRYNRKhDopWLSbmlo509qeaZ8Ttvixorjq57vUmkbsuk1hqGDP_MwSfv7gvrxjvjKYJKC-1acAAZt9o2ufITjC-5NpUxUrLuAF9LFz8Y8Kl0N2pvWs6JUbQe5EiEXg6y0gfNsXYLRxt51zXqFg6dA3wzLhtLXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
نشست فعالان اقتصادی آبادان و خرمشهر با وزیر تعاون، کار و رفاه اجتماعی
دکتر للـه‌گانی: بانک رفاه کارگران بازوی تأمین مالی توسعه استان خوزستان است
🔹️
مدیرعامل بانک رفاه کارگران از آمادگی کامل این بانک برای تزریق نقدینگی و تأمین مالی پروژه‌های کلان تولیدی و زیرساختی در استان خوزستان خبر داد.
🔹️
دکتر اسماعیل للـه‌گانی طی سخنانی در نشست مشترک فعالان اقتصادی شهرستان‌های آبادان و خرمشهر با وزیر تعاون، کار و رفاه اجتماعی که در محل سازمان منطقه آزاد اروند برگزار شد، با اعلام این خبر به سیاست‌های بانک مرکزی مبنی بر تأمین مالی زنجیره‌ای اشاره و تصریح کرد: بانک رفاه کارگران با انتشار اوراق گواهی سپرده خاص برای پروژه‌های توسعه‌ای و سرمایه در گردش واحدهای تولیدی در مناطق آزاد استان و شهرستان‌های پرظرفیت مانند آبادان، خرمشهر و شوش، گام‌های اثربخشی برای تامین مالی بنگاه‌های اقتصادی برداشته است.
🔗
متن کامل خبر
...
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/465641" target="_blank">📅 11:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465640">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/farsna/465640" target="_blank">📅 11:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465639">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بغداد ضرب‌الاجل خلع سلاح را یک سال به‌تعویق انداخت
🔹
دولت عراق مهلت خلع سلاح گروه‌های مسلح را که قرار بود ۳۰ سپتامبر ۲۰۲۶ انجام شود را به ۳۰ ژوئن ۲۰۲۷ موکول کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/465639" target="_blank">📅 11:12 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465638">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NgBv1yns-6cNGkxjC7xqCzFc5JCNFuYHVYf-xDYGKvO4xPsHMUtI5ZNeA13_Um3pmUfXFAMAKpWW0pMU1qXnR7664Ls_Zb9WWg1CG1kIkix2VnV1eZc5mfoe7R00bYuYFy6qS4GuVVvN6-O7eU5UOhKVTuSKqmLpLb88GmmW8KYMS5QKnQ-7s46HgVFTFAFY6vf2baW_QYXB7DXAleZR5uj3m22f65KW48iFaZIjGEhbjLAwziCXGw5wubBiT2nr7gKkWZLSxOMEm0aMD6bMFgdMlbOTBpr1MVH-H-j3jnPCnIhSCvTVHDsRPsnUVCJ_mttbkUhSw8oSQVIYjsF0_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاسخ ایران به ادعای اخراج هیئت ایران از آمریکا: بی‌اساس است
🔹
نمایندگی ایران در سازمان ملل در واکنش به ادعای وبگاه «آکسیوس» مبنی بر اخراج هیئت ایرانی از آمریکا گفت که نمایندگان ایران طبق برنامه قبلی نیویورک را ترک کردند.
🔹
نمایندگی ایران در سازمان ملل با اشاره به گزارش‌های منتشرشده درباره اخراج هیئت ایرانی از نیویورک افزود: «وزارت امور خارجه آمریکا که به هیچ دستاوردی نرسیده است، اکنون به انتشار اخبار بی‌اساس و بی‌ارزش روی آورده است.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/465638" target="_blank">📅 11:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465637">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c74dc1056.mp4?token=jBp_cAi80Jdohi5Qxt-Ho6hKpGodKttXH8wqqZTTvtgyjGhykM3F8k6QSdYCEvhpORjtm682GFMFbh8r2h5JvOV1zcU00p1hRADxnj8vCDJkGh-UCTaR2_eyab4ikmmrFVuXDn4rmoVOWUEvNhMmchtj7djOXkBR2aXJ00QLa7eSNAZV0skac1uBigwx_jgFqkn_Z0P3g8yQtbzBEKiKWb-iJSsAS5cOfRhjAfSGwxUnU-rlLT1nr-hwB7lcOopUONWQj0RpiijjvuRCL0vLUiM6nGe2rX6GjCHhGgj_rUwR03KotP9yZ7WO5dJlHt-HPr-6bILqqONlRSUojuzHzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c74dc1056.mp4?token=jBp_cAi80Jdohi5Qxt-Ho6hKpGodKttXH8wqqZTTvtgyjGhykM3F8k6QSdYCEvhpORjtm682GFMFbh8r2h5JvOV1zcU00p1hRADxnj8vCDJkGh-UCTaR2_eyab4ikmmrFVuXDn4rmoVOWUEvNhMmchtj7djOXkBR2aXJ00QLa7eSNAZV0skac1uBigwx_jgFqkn_Z0P3g8yQtbzBEKiKWb-iJSsAS5cOfRhjAfSGwxUnU-rlLT1nr-hwB7lcOopUONWQj0RpiijjvuRCL0vLUiM6nGe2rX6GjCHhGgj_rUwR03KotP9yZ7WO5dJlHt-HPr-6bILqqONlRSUojuzHzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مادر همسر رهبر انقلاب: آیت‌الله سیدمجتبی خامنه‌ای در خاکسپاری رهبر شهید در حرم امام رضا(ع) حضور داشتند و ایشان در صحت و سلامتی کامل هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/465637" target="_blank">📅 10:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465636">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/707e140333.mp4?token=IeThW-dfkXKkL7DO8G87zJG6Q3eGKEIuGU7wUS1A9XDrTXc27nOMI64AL84LbkPWX84Vcf9cRPCZiZr4Eye6gzcbHYuZ_88pcRzu48VwzByZ7nylglZG6hqH9TiZooabDBqu_MOs5FL-xmgiufbbCG8LT1nOigrLBd6HPuW44zjK54hVaWnyT4HHHfsVcUdVUivyG9DmBVeu12cCa5UfVU7PLpBLBEfuokS_S-cD_bnq003NSxs_yIsZBc11ZOnzgLP8ZGPoWw16FVrLMOeD4srLVJqk0csd5m0Oh2wz-LR7BvgD0oDDxst_P3tH_ADnGTRNkyiSX7IJbd5Ijd2-2R87zuwHMDZqYGGwa69Zo8HY7obKle25zIEd001uY8OEwmiWHpX47ZzeRcVV1rQaSUjzzkr5K1OVWrQn2LSRNT5VxG5eAl2PZmPwHMm8ijW-glcPOaSvk_HdoxQoh5R2cKEdWM9y3eU9EAaFtGIztE5cKR8lXa1xmg-fuRzaWalNLtotJUyMXEHluLxK25766hsKVxjcCXSmMaTMkcL-H687z-etalF2BD8sApVXl_8ES8L3H3F8616-_03oNl0eR60zL_TR_Aw6u30fCEDE5kdu2Sedro652BICvIryxETEeF6DIhfJipvAe0nNw9k-EiM-iDZ-ym2lx_K1pUI7Wco" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/707e140333.mp4?token=IeThW-dfkXKkL7DO8G87zJG6Q3eGKEIuGU7wUS1A9XDrTXc27nOMI64AL84LbkPWX84Vcf9cRPCZiZr4Eye6gzcbHYuZ_88pcRzu48VwzByZ7nylglZG6hqH9TiZooabDBqu_MOs5FL-xmgiufbbCG8LT1nOigrLBd6HPuW44zjK54hVaWnyT4HHHfsVcUdVUivyG9DmBVeu12cCa5UfVU7PLpBLBEfuokS_S-cD_bnq003NSxs_yIsZBc11ZOnzgLP8ZGPoWw16FVrLMOeD4srLVJqk0csd5m0Oh2wz-LR7BvgD0oDDxst_P3tH_ADnGTRNkyiSX7IJbd5Ijd2-2R87zuwHMDZqYGGwa69Zo8HY7obKle25zIEd001uY8OEwmiWHpX47ZzeRcVV1rQaSUjzzkr5K1OVWrQn2LSRNT5VxG5eAl2PZmPwHMm8ijW-glcPOaSvk_HdoxQoh5R2cKEdWM9y3eU9EAaFtGIztE5cKR8lXa1xmg-fuRzaWalNLtotJUyMXEHluLxK25766hsKVxjcCXSmMaTMkcL-H687z-etalF2BD8sApVXl_8ES8L3H3F8616-_03oNl0eR60zL_TR_Aw6u30fCEDE5kdu2Sedro652BICvIryxETEeF6DIhfJipvAe0nNw9k-EiM-iDZ-ym2lx_K1pUI7Wco" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منظور: اقتصاد جنگی به فرمانده واحد نیاز دارد
🔹
رئیس سابق سازمان برنامه‌وبودجه: اقتصاد کشور در این شرایط به «وحدت فرماندهی» نیاز دارد و باید تصمیم‌گیری‌ها متمرکز و اجرای سیاست‌ها با اعطای اختیار بیشتر به وزرا و استانداران انجام شود.
🔹
شورای اقتصاد کشور هم…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/465636" target="_blank">📅 10:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465633">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qaaqXg-dEpj8GbqGws2ZW0wQPoX2t8iYWo7U1smVPpjI5se5OqTdFPg3_Ct1ZXR9cAw8EdvYa0x8qEMTOUNLoYH4eS24oPmQPkT7aLNsDe7O-vTMwOHWES4FX49jyaMi3WlZaChJlMSPdVZTrc5eTaH2yyDvx7CHrA6Fxe91wEt3_VcRwRw98VdrjsU8F9iO3demTlkvpF_nGJcG1HDgSCRvv8O4G7dYO8qfV6e3GYQZjdn2sVN-D98wGKdkaXM_huwrHB8r_p3tSv5zeKjKTad9_ygGi4b1Az6o4TYBEiIVLPKO5u2FwFeD8qxlfilT33PKSxX9pqKtRcioddNLYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/URnfSVEq2dyhD7y9GycMVJeSPQOVZMQzFt0jY_r0ub8o_WcnVVs3WLl2DczofjR11UvbIPEbPG_u2-mT_uE66LPQOjH2LyG8mruKzBcGdWKq-Pwv6V5LL6wcVVkCcB4gncxit62h12qrRDn2olbOHCzDpn93M5juH6tCtuhDPsZsrWE_vsSdnMdHL7GoO6fhpuEHBLzG4kZhANNixVo_fdtEAPNgyX6bMu509qX3FcPpAjv_6iVLW2na-9NCWaBkxfEp0g82ifce7hxnUEo29btayVjcHTAj1kvhyYeuw8RGnw9jxejj00q_y5fmltLEvdCxsV0xcBGm4KELSuiIUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bqy5jlGoCBPkzezPbIfzkABz3Zj8KYPVSaCxVNHm-RjLnODtyfZlEeRQp28sMF9Nujte_gnLYPOY5Mn9en0joGirptpWhTFye_IDjd8xV5YPPOlzX-hbx3_mUK0O9UvZEy8CBLeBpbt_gcPwmilKg7gkU7aExkZtbOIYhaSpWDcxqR7uS3XzVVdUw3rrs8NPtBYRt5-rfafjrGWnZDVU1VnQE6ofO4bty7iIwtKDWSJbgyCRfSV1JF_39RrlIR53gHsd_uWEmn-Zz7nygV04LFazCK-_SoLYybAdwKRtIsDdTfSeJHRWSJPL7NK2hunfJ924xN1s9WdqjvCnfgXwLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تقدیم هدایای متبرک رهبر انقلاب به خانوادهٔ شهید نصرالله و شهید موسوی
🔹
جمعی از فعالان جبههٔ فرهنگی انقلاب اسلامی در جریان سفر به لبنان، با خانوادهٔ شهید سیدعباس موسوی و شهید سیدحسن نصرالله دیدار کردند.
🔹
در این دیدار، چفیه و انگشتر متبرک رهبر معظم انقلاب اسلامی، حضرت آیت‌الله سیدمجتبی خامنه‌ای، به خانوادهٔ شهدا اهدا شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/465633" target="_blank">📅 10:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465632">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">سپاه: اخراج آمریکایی‌ها از عراق، طلیعهٔ آزادی غرب آسیا از یوغ سلطه شیطان بزرگ است
🔹
بیانیهٔ سپاه به‌مناسب خروج کامل آمریکا از عراق: سپاه پاسداران انقلاب اسلامی با گرامی‌داشت یاد شهدای سرافراز جبهه مقاومت اسلامی عراق و منطقه غرب آسیا، به‌ویژه سردار سپهبد شهید حاج قاسم سلیمانی و شهید ابومهدی المهندس، و همه مجاهدان مؤمنی که در دو دهه رویارویی با متجاوزان آمریکایی به فیض شهادت رسیدند، این پیروزی تاریخی را به ملت غیرتمند عراق، جبهه یکپارچه مقاومت اسلامی و مجاهدان انقلابی جهان اسلام تبریک می‌گوید.
🔹
اخراج آمریکا از عراق، نتیجه پایمردی ملت غیرتمند این کشور بر استقلال خویش بود. ملت عراق با ایستادگی تاریخی خود ثابت کرد که اراده ملی، برترین سلاح در برابر زیاده‌خواهی سلطه‌گران است. غلبه اراده مقاومت ضدسلطه عراق سربلند بر اشغالگری آمریکایی، برگ زرینی در تاریخ آزادی‌خواهی ملت‌های منطقه است.
🔹
اخراج اشغالگران آمریکایی، در حقیقت تحمیل عزم راسخ عراق قهرمان بر رژیم تروریست و جنگ‌افروز آمریکا و حاکمان بی‌خرد کاخ سفید است. آمریکا که همواره با زبان زور سخن گفته، امروز ناچار به عقب‌نشینی از سرزمینی شده که دو دهه آن را اشغال کرده بود.
🔹
آمریکا رفت؛ نه با مذاکره، نه با منت؛ بلکه با همت ملتی که ایستاد، با خون مجاهدانی که جان دادند و با اراده مقاومتی که هرگز شکسته نشد. اینک عراق، سربلند و آزاد، بر ویرانه‌های اشغال بیست‌ساله ایستاده و طلوع استقلال را نظاره‌گر است.
🔹
بی تردید این رخداد مبارک و تاریخی نخستین گام در خونخواهی شهیدان عراق علی‌الخصوص ابومهدی المهندس است و به فضل الهی انتقام خون این عزیزان با اخراج کامل آمریکا از منطقه تکمیل خواهد شد.
🔹
آمریکا باید از منطقه برود و مدیریت امنیت را به خود ملت‌ها بسپارد. تجربه دو دهه اشغالگری نشان داد حضور آمریکا نه‌تنها امنیتی به ارمغان نیاورد، بلکه خود منشأ ناامنی، تروریسم و بی‌ثباتی در غرب آسیا بود.
🔹
آمریکا پس از بیست سال مداخله نظامی، با حدود پنج هزار کشته به اذعان خودش و البته نه آمار واقعی و چهار هزار میلیارد دلار هزینه، در اوج نفرت و کینه مردم عراق اخراج شد. این ارقام، گویای شکست سنگین و رسوایی‌بار آمریکاست.
🔹
خروج نیروهای آمریکایی از عراق، رویدادی بزرگ و معنادار تاریخی و دستاوردی سترگ برای محور مقاومت است. شکی نیست که مردم غیرتمند عراق با ادامه این نهضت مقدس، به مداخله آمریکا در اقتصاد و نفت کشورشان نیز پایان خواهند داد و با وحدت و اراده ملی، آینده‌ای روشن برای خود رقم خواهند زد.
🔹
آمریکا هیچ‌گاه تکیه‌گاه قابل اعتمادی نبوده و نیست ؛حقایق و واقعیت‌های میدانی تصریح می‌کند آمریکا رفتنی است و این ملت‌ها هستند که باید کشورهایشان را بسازند.
🔹
با قاطعیت می توان گفت اخراج آمریکا از عراق، طلیعه اخراج آنان از سراسر غرب آسیا و جغرافیای امت اسلامی است.
🔹
این پیروزی بزرگ، محصول اراده ملی عراق، مجاهدت جریان‌های مقاومتی، حمایت مردمی و اقدامات مؤثر دولت این کشور است.
🔹
سپاه پاسداران انقلاب اسلامی در پایان با تاکید بر ضرورت هوشمندی و هوشیاری دولت ملت و نیروهای مقاومت عراق قهرمان در برابر توطئه‌ها و فتنه‌های محتمل طراحی شده توسط امریکا و دشمنان این کشور برای ایجاد ناامنی و بی‌ثباتی مجدد در این سرزمین مقدس، به عنوان فرزندان ملت ایران، قاطعانه اعلام می‌کند همچنان در کنار ملت‌های حق‌طلب و ظلم‌ستیز منطقه برای پاکسازی غرب آسیا از لوث بقایای پلید متجاوزان آمریکایی و نیز رژیم کودک‌کش و نژادپرست صهیونیستی ایستاده است و تا آزادی کامل قدس شریف از پای نخواهد نشست.
@Farsna</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/465632" target="_blank">📅 10:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465631">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یک تیم تروریستی در زاهدان منهدم شد
🔹
روابط عمومی قرارگاه قدس نیروی زمینی سپاه: یک تیم تروریستی که قصد اجرای عملیات تروریستی در منطقهٔ منزل‌آب را داشت شناسایی و مورد ضربهٔ قرار گرفت.
🔹
تاکنون تعدادی از تروریست‌ها به‌هلاکت رسیده‌اند و عملیات پاکسازی همچنان ادامه…</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/465631" target="_blank">📅 10:28 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465630">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">یک تیم تروریستی در زاهدان منهدم شد
🔹
روابط عمومی قرارگاه قدس نیروی زمینی سپاه: یک تیم تروریستی که قصد اجرای عملیات تروریستی در منطقهٔ منزل‌آب را داشت شناسایی و مورد ضربهٔ قرار گرفت.
🔹
تاکنون تعدادی از تروریست‌ها به‌هلاکت رسیده‌اند و عملیات پاکسازی همچنان ادامه دارد.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/465630" target="_blank">📅 10:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465629">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hn7q8GsED7N2JbCpY8fQQ8V2IH1s0edGexCx7160Udc2xBz96H362BP8y5M5bUkANzTvkVDSzEBfSB8VuxizxMfqjp-RFo0Gn4dfIv1EUEw6H5SW8gJZhXcQ7XqLcZPUlUZMLPODxt9GBkYn1obA6P5a22s7usm5iQlNDQwEQiHrRdfmwxzLKiBFhJi77vp2Xh3wr0PhqiOFwB-AYdfImeyfs335jO0Qhqmj-xvcXeb2KQDrGlWyowbLI11uxc0pkc-G6ma2T7A2f7lRIbXr2p-Yc4Z9vzlFeFtjS_rWUUz89zRJaCNPSwxCERlNMVFRIdJKtkMFyo_6VmOgQdX5UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائب: هوشیاری و همدلی همگان بیش‌از گذشته ضرورت دارد
🔹
پیام رئیس سازمان بسیج به‌مناسبت فرارسیدن هفتهٔ انتظامی: هفته انتظامی، فرصتی برای پاسداشت مجاهدت‌ها و تلاش‌های خالصانه مردان و زنان غیوری است که در مسیر تأمین امنیت، آرامش و آسایش مردم، مسئولیت سنگین حراست از نظم عمومی و صیانت از امنیت جامعه را بر دوش دارند.
🔹
فرماندهی انتظامی جمهوری اسلامی ایران با توان رزم و دفاع نیروهای جهادی و مخلص در طول سال‌های پس از پیروزی انقلاب اسلامی، با حضور مسئولانه و فداکارانه در میدان‌های مختلف، از مقابله با تهدیدات و ناامنی‌ها تا خدمت‌رسانی به مردم، نقش مؤثری در تحکیم امنیت کشور به ویژه مرزهای کشور عزیزمان ایفا کرده  و نیز با نثار جان خود، برگ‌های درخشانی از ایثار و فداکاری را در تاریخ پرافتخار ایران اسلامی به یادگار گذاشته‌اند.
🔹
امروز که دشمنان ملت ایران با بهره‌گیری از شیوه‌های نوین جنگ ترکیبی، امنیت، وحدت و انسجام اجتماعی کشور را هدف قرار داده‌اند، هوشیاری، همدلی و هم‌افزایی همه دستگاه‌های مسئول و آحاد مردم، بیش از گذشته ضرورت دارد. بی‌تردید تداوم امنیت پایدار، در گرو حضور مقتدرانه نیروهای انتظامی در کنار مردم و تقویت پیوند میان جامعه و حافظان امنیت و حمایت از مدافعین امنیت می باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/465629" target="_blank">📅 10:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465628">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">انهدام یک شبکهٔ قاچاق دارو‌های کمیاب
🔹
دادستان تهران: اعضای یک شبکه قاچاق دارو که از طریق خارج‌کردن دارو از شبکه توزیع، اقدام به قاچاق آن به یکی از کشور‌های همسایه می‌کردند، دستگیر شدند.
🔹
در این پرونده تاکنون ۴ متهم شناسایی و تفهیم اتهام شده‌اند و متهم ردیف اول این پرونده یک خانم از اتباع یکی از کشور‌های همسایه است که مقادیری داروی قاچاق و خارج از شبکه از وی کشف شده و تحقیقات از افراد مرتبط با وی ادامه دارد.
🔹
مشارالی‌ها با اشخاص متعددی در ارتباط بوده و یکی از شگرد‌های آنان برای خرید دارو‌های خاص ضد سرطان، خرید کارت ملی اشخاص و هماهنگی با پزشکان، جهت اخذ نسخه بود.
🔹
وی همچنین با یک داروخانه که اقلام دارویی را خارج از شبکه و به صورت عمده می‌فروخت، مرتبط بود.
🔹
متهمان پرونده دارو‌های خارج از شبکه را از طریق یک باربری به یکی از شهرستان‌های مرزی و از آنجا به یکی از کشور‌های همسایه قاچاق می‌کردند.
🔹
از باربری مرتبط با این شبکه مقادیر زیادی دارو به ارزش ۳۶۰ میلیارد ریال کشف و مالک باربری دستگیر و جهت تحقیقات در اختیار ضابط قضایی قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/465628" target="_blank">📅 10:01 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465627">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpZNF8u2E4ge2DVkckh7oyUW-gQCxS1qM-hcFFaYUpz-VgnYtQOY6llb3RyNxI8dToltUo_Y5juIh6JxoQSYVAfzZZHt269kj8uL865UOhYL3uW5RiRwv8F5Vngav1SxiY6gu9wxAWQS4S0uxiDLaypIxDhzquyeu5klZSmDw0wa6gSdDCpR3fkoOkWpS3KU0D1IS1KN_uhJ1MCti6wDfOuEkWOdLY4inzWPE7lxqA5zj3gI-Iwkao9dLdzIlfqNqyB5gnrFzpU48FZJy0BEVPAHDvqMxS0sSrH-R1OLx7-_hwAXqOiFRipAEBeSROyY0BlcMqBWT2RbHm_1NlqHOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی‌های آسیایی ناگویا
🏐
کامبک ایران امید اندونزی به صعود را ناامید کرد  تیم ملی والیبال ایران، ۳ بر ۲ اندونزی را شکست داد.  صعود ایران قطعی بود اما اندونزی برای گرفتن جای تایلند در رتبۀ دوم گروه و صعود، به امتیاز این رقابت نیاز داشت.
🇮🇷
۲۲ | ۲۱ | ۲۵ | ۲۵|…</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/465627" target="_blank">📅 09:58 · 09 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

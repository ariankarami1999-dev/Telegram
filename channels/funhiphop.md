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
<img src="https://cdn4.telesco.pe/file/IA4z8_mTi4qDtHN8pBhHo_jjKJYSkS7f-zWq5zV0siMUAMDdoir_PHax9LP3i9S09mMPlqs9iiBwz7xTd7u1mt5LbvVDlX71z6ZYkhEBSp5oO_ZaqhoC6Gnzb-RTORzgmP_c019I2Oc3jZv2d7OQpanZXR8BfPjP0fZVnGzD1ZIWEBsN-hXW28DC2UoIUjnvYHQvyCY9Nn7n-a43eY3dfZnwxNVdRlwJ_8FCSyMYsAOqPaYn1RyHrIYpNxTXpNJ8xQrm9mDV3MJ9EaBWBszKqdUnpkleGvLNnCDJKHoSi1sh58LpO-ru4299oj2hUkIe_EJKbVEdwfRqEED3ASIygg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 196K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 15:05:09</div>
<hr>

<div class="tg-post" id="msg-80203">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">جلیلی چه پولی داره خرج میکنه، کل تبلیغات فیلترشکن های رایگان شده بنر های تبلیغاتی جلیلی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/funhiphop/80203" target="_blank">📅 15:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80202">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qwlh-5PiYBSRqUAJ9FC-VdIMNkHd6xpYecdVdV4T9_nBBYOvo5AqLXRR_0erYoS3qzA0BgUd3nGyLMHhgkmiNFMKJjP3y1Y-_S4eSYZ6Hm-neuvrZMDUQkhdPHCtn_sxRLoWO2oQX3JemYqGmF4a5yUred4EhAEwjc7KT9XGt6_A1BktOYiB9lwB-ZtHLdg5rLr2zMxGDT0_AR5eVI0zE0-_uFVt0DEaOu6hz6wy3S9Y1Z6RKVzGT0rLb6sGCtIJZgT5U05HsQR2UZkDQCbB-UvvnnIZRMhAeGTJ8ConuGe6jA47dAqefFRLjzBQXn9PIYO-pFAcIIU4I5gwCnRIqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداش زدن مادر فرودگاهو گاییدن کجا میخوای فرود بیای
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/funhiphop/80202" target="_blank">📅 14:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80201">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">امتحان امروزتون چطور بود؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/funhiphop/80201" target="_blank">📅 14:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80200">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2c54c8a06.mp4?token=qu4GqTaw4lH0g3fv8Aj4RNmmdBFzchMXxCgAg1OREF2eOvHmNCrv15n6dDGdSjvP_alm2RHbbVBn86KfeQ9f8UmEVvf_cgj5kVMChFX2NdoYtn---itS3U9IKInPRvCH78CMK8bdvIJJC5uRt72PamAD58b9YnePnfwO2H7W7ZM9lpj9jxUqgCCRauGzzgXG68Swo0voKxpjOk2ML68oHKoASHocvr-rlCqPHjaL7Ic7Hm5Bc4D20rpshXbbjN1I4w0u1QEur-z4ILnx_4zjiu8c4MCeDsNPwM5b104vrhWSLY28IF2FrlzMmqaxy9pWD0pHm7ETJqpl1XUs-HOyyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2c54c8a06.mp4?token=qu4GqTaw4lH0g3fv8Aj4RNmmdBFzchMXxCgAg1OREF2eOvHmNCrv15n6dDGdSjvP_alm2RHbbVBn86KfeQ9f8UmEVvf_cgj5kVMChFX2NdoYtn---itS3U9IKInPRvCH78CMK8bdvIJJC5uRt72PamAD58b9YnePnfwO2H7W7ZM9lpj9jxUqgCCRauGzzgXG68Swo0voKxpjOk2ML68oHKoASHocvr-rlCqPHjaL7Ic7Hm5Bc4D20rpshXbbjN1I4w0u1QEur-z4ILnx_4zjiu8c4MCeDsNPwM5b104vrhWSLY28IF2FrlzMmqaxy9pWD0pHm7ETJqpl1XUs-HOyyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کصکش رید به حرفی که یارو میخواست بزنه
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/funhiphop/80200" target="_blank">📅 14:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80199">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmWfNQ0CnwBo2dg3rGerEexNutka5iILoX2xqU1dcg34YrcO0aEtbtGY-mpcGVMpIbclEab6vF6H-47eyG4q94n0P9lAt_VOb5-0yTaQFIjDa_t14l9cF5PWb9yk2o1Xn5QJTE0Pr_2kmIn_4BHmrl-XQg9CviibwjREth5M9F6T6xVuQn1QnTWk8cJRvgVaaQTSR9lsvlSfReNFXDLzmKjt-Ggbp8RwzJKl5uOZ1bk9GCi-Q_joThnUb0jTAGJLXSLY2M-0UGrpmVpBWC5kMw8XovP5BI8FCJCpO3dT3NzhC81aH9aefxYereVnkkDm7BPzJ36PUndIirdFH1mKqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فحش آزاد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/funhiphop/80199" target="_blank">📅 13:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80198">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E54Gy9wPVQkJU_6lezcR-xmnJWHV9uuHJt7CoKfkprewHkdf2jZC0ZtO95_7UrVjCscWXY7eR3wP6X3MIqIDi4f5ZALZjvoxUAgsJLtrox4psH_yMsdVsZDOouFYurq7l3AOSHb6pPcf9tbiZAZ1dmzrsgygbDDR0B_7PtlwZtXvZrafvLVLgnsHoENypc1iAlW2K-n8pzDoDGmkTa4ysy1p7DD06zDiozRmBP6cjmgnmxmmsRNDKxaiUNJKNZXEMPNLLuJ2EdWE0cS6CTBpyPuR9Hzt0skuS75KVOWL4YnCEcTzoF3ZJODW4a30obvXPs8C25a_5JOrd18xVXps0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضا رضا مچتو گرفتم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/funhiphop/80198" target="_blank">📅 13:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80197">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">باز زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/funhiphop/80197" target="_blank">📅 12:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80196">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3J_EZXPABftM51dXFnHnqZddZF2s72Bc9Yht1Jb1FyO7tON9K42YbHBjFqW129v1z0midl142DqHD3ycLnMrCalW4c_dwQvn9nq8dGof3W89SVOGCyXIsLb44FXv273XjGeM9alXNS7xSxBgI4Q0G8Rg_V_FI0eRcHAc1Q1t1T4O4BK9ndkCDLjdf_jVGLJeBCuMSa4okYlS0HBoEEQR2zRQ4_LKsVTqEmD8yDeLXSOPIDtMo5Cl4itdjZJbn__CzLgO_5DKC31cx1xZSzbHLLMTG5GaAsU6l_XXeH5M7JkQdv6mfk9oy4o3QXCd-0VuvXBl_YOdQTWv0KP9M39vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری تلخ هادی چوپان...
💔
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/80196" target="_blank">📅 11:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80195">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_ks6sMImEqwEZBnNe44Xm4V3T5ICpi9jVgF00l6gff_u6JRZVduTukzwqikozFwFrOs3o2hjuC_x6SlYD2ZhDMKBjncRPeH1XdosE93a7IiESLqgh7hlS1hoLAMaDMsGMgGq-WvfzgILSSfmSdIVMFKSxAKeFv-E2hOqtWDrw4On921cTJbveWI3WcfniugIc7t-xenJZXDPYhPHu0__AV00-9IioYCGQ8thZOEZIemGyRZhqKDD7APjltYVGh3FErFVqjd6tygE0sGKuCPglqtbYLvZKPKgi_vqOkazlb_B0fmPMb_8BkG_G3CoG91jPKSe8WGqozL1Jv2P4OKmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلم برا حمید سوخت پسر.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/80195" target="_blank">📅 11:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80194">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/826125c863.mp4?token=h1RPw_DCRo4smWlbuaEyJb9zTZDZ3OST8B2XCDwyNejAkkRwcSElosGBb-EtGumrnijcofFTi88sNGwmpZJLHAn4Rwc8uG3cDCPvsLZl7FT4ALUXdtjvhXJirxSOv2ctSISZAmY23EPWmqgY7t3PKzeK-rawmOzYRt3BfLmmDxIxADt_QAbQR7n7UAjCbVquBUu0v42526FJprtAqq98fQa39_NF9rmG60lNzoyYy-I2-DfGY3FDydVfrl8FvmmGussQZTvhoHSSWuPrFhBqEGCKGSWkyhrpKQPfP1LN2pdeisyaoMio43iETWlIk13FK4vYi3prQFu81pMqFTZ2Vl3NFHKG9MNioHGQJRi6DUTROuOYBB0G9KSIx80ofRXUfrX2DJvI5S3MctG-KACxBdkf2ytq8PpNI_mvbdjvaje9q7G8rTC1oIeiqUHuf4mzQxquEvPWkpkCIwoIavtAxWs5VucPASTa3_2LbNcyvL8ZmNWqayTMJgk59mFJYdh7LadD5BCNfKyUgiBDjE9PMIGPscLaSsXEEANRNElh409QHFccDegzp-jJaifI6NJExtU0svrar3Mc67Nw_Ff-E_7BjACJBOiGch4IFKvRIAPzx1vwgiZ3h8MJB_OLS3bWQGDx7jSpmm_Q8RtXYpNOFBXIcd18ZqhfW_sJOO9YSEo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/826125c863.mp4?token=h1RPw_DCRo4smWlbuaEyJb9zTZDZ3OST8B2XCDwyNejAkkRwcSElosGBb-EtGumrnijcofFTi88sNGwmpZJLHAn4Rwc8uG3cDCPvsLZl7FT4ALUXdtjvhXJirxSOv2ctSISZAmY23EPWmqgY7t3PKzeK-rawmOzYRt3BfLmmDxIxADt_QAbQR7n7UAjCbVquBUu0v42526FJprtAqq98fQa39_NF9rmG60lNzoyYy-I2-DfGY3FDydVfrl8FvmmGussQZTvhoHSSWuPrFhBqEGCKGSWkyhrpKQPfP1LN2pdeisyaoMio43iETWlIk13FK4vYi3prQFu81pMqFTZ2Vl3NFHKG9MNioHGQJRi6DUTROuOYBB0G9KSIx80ofRXUfrX2DJvI5S3MctG-KACxBdkf2ytq8PpNI_mvbdjvaje9q7G8rTC1oIeiqUHuf4mzQxquEvPWkpkCIwoIavtAxWs5VucPASTa3_2LbNcyvL8ZmNWqayTMJgk59mFJYdh7LadD5BCNfKyUgiBDjE9PMIGPscLaSsXEEANRNElh409QHFccDegzp-jJaifI6NJExtU0svrar3Mc67Nw_Ff-E_7BjACJBOiGch4IFKvRIAPzx1vwgiZ3h8MJB_OLS3bWQGDx7jSpmm_Q8RtXYpNOFBXIcd18ZqhfW_sJOO9YSEo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آنالیزهای اختصاصی بت‌فوروارد، مرجع تحلیل مسابقات برای تصمیم‌گیری هوشمندانه
🎲
📈
در بت‌فوروارد، هر مسابقه با بررسی دقیق آمار، تحلیل عملکرد تیم‌ها، شرایط بازیکنان و مهم‌ترین داده‌های پیش از بازی به‌صورت تخصصی تحلیل می‌شود تا با دیدی کامل‌تر و اطلاعاتی دقیق‌تر، تصمیم‌گیری کنید.
📗
برای مشاهده آنالیز اختصاصی هر مسابقه، وارد وب‌سایت مجله بت‌فوروارد شوید، سپس نام تیم یا دیدار موردنظر خود را جستجو کنید.
👍
ورود به مجله بت‌فوروارد
کلیک کنید
mag.betforward.com
کلیک کنید
mag.betforward.com
🅰
r22
💻
@Mag4ward</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/80194" target="_blank">📅 11:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80193">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">علت مرگ لیندسی گراهام پارگی آئورت بوده.
@Funhiphop
| Reza</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/80193" target="_blank">📅 11:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80190">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">یامال بالاخره ۱۹ سالش شد</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/80190" target="_blank">📅 03:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80189">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نه،تعویق نخورد امتحانت، بخواب ایرانی</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/80189" target="_blank">📅 03:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80188">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">امشب با اختلاف سنگین ترین حملات از سوی امریکا رو شاهد بودیم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/80188" target="_blank">📅 02:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80187">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سلام باز صدا پهپاد میاد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/80187" target="_blank">📅 02:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80186">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">تایید نشده عمران عقیلی، رئیس واحد ارتباطات عملیات ویژه در فرودگاه اهواز ترور شد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/80186" target="_blank">📅 02:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80185">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLsdn-L-r61msSi8Y6fyEgEgYfvPMrrQPdzQAdj25FK7LNOoTG9puiWnuEJe9BgRo8rvJxmXph5sqWoMH5VDIqVZnLYVYBW3HojkJRDHAOhCFXA5wSR70m3843SsSsoEDNax9DqNzEpZMzl-vcTA_suqGHBuof5tr_6GSCNny0BNksIbMQKXFkxOAt87T5CuUpAMLrRhC_3d03OYcgE7tQXFuumTwXwctCQpqT96lxtJ9Po0HRn6AvsfqXItY9Gf7SFFYyVpXLFXITgDEytWui0REX4ZwVKmLvqJrrJWhVniBy-VC2GAsD1mhINiorJs7OExG0bWg3ezHOrQbuMCjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوافضا سپاه بعد از اینکه همچین سرباز آماده ای پایان خدمت گرفت طول کشید خودشو پیدا کنه
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/80185" target="_blank">📅 02:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80184">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">راستی اینجا(شمالغرب) یه ساعت پیش داشت صدا پهپاد میومد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/80184" target="_blank">📅 02:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80183">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">تایید نشده
عمران عقیلی، رئیس واحد ارتباطات عملیات ویژه در فرودگاه اهواز ترور شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/80183" target="_blank">📅 02:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80182">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">این هیمارس هیمارس که میگن این لانچره‌اس که خفن ترین موشکش 500 کیلومتر برد داره فقط و برای جنوب کشوره  @Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/80182" target="_blank">📅 02:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80181">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">بچها شوخی نکردم اسمشو  @Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80181" target="_blank">📅 02:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80180">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvhtgaXeLRXVE50qeq-HyZ6VuhRIvLI2DAu035G5E9RamDVWzawDG_UkO7xgHT2P8xxdYZ9oZtb1s-bro8QGdcfbpa7SEFglZcb5A78qtFNExH2q1NrpiiLRZPFT9D9kJC3rpAdwnf3kt2AlGZls4L5MZ3mcS3J47_9Pr43kwk2vLYqmIVoLP1hlSB6c8F5EOskf_buEl0IMhjQNPvDN2B-rSJW1IUC1hQZRfHLw3AIx7uXwx2GtvoODnBrjJ_BShZWolkUtJJT7QRApMA3voQvWgJxXgrGfscmNv_1j4-yBgIFcby84daDF-UZP0pisdWFy5tSNWBzyoh8N-VqqoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدافند مجید در کرمانشاه فعال شد  @Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/80180" target="_blank">📅 02:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80179">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پدافند مجید در کرمانشاه فعال شد
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/80179" target="_blank">📅 02:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80178">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">یزید تو چرا بیداری دیگه
معاون استاندار خوزستان:
در ساعت 1:40 بامداد امروز دوشنبه 22 تیرماه نقاطی در شهرستان‌های بهبهان و دزفول مورد اصابت پرتابه های دشمن آمریکایی قرار گرفت.
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80178" target="_blank">📅 02:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80177">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHX5umPHRpS2atF-nHPSXIScgvqEOY-LcjDcoLGQeqBe2C-j0U484_Lqn5Yjaf_G8WB21fBNi8nrFEmbXPxwXaQ6o-9n6bm3VXz-pQwzZtpLQjaMb-Rz0-HGAN24X-wCnvSQ5gR7L_xiPpeK2c729SJweiB_wwSrxjyKQ1TTjGdoQRR4v4sqcrZHAqQ_q39XV8dCHpt2R6h5ph5WYUrjonrjF_5jCujRR67YOW8f5ol0nVCfmfgzq19WmLVhZlfeZmazaJtliEx3KlAvaXfUXAqxr5i9DO62uIGJS1v37Y5whmkaEi9XKpRw4QMcsXqyGgcxFoiCkA22ggaI6UKE9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هیمارس هیمارس که میگن این لانچره‌اس که خفن ترین موشکش 500 کیلومتر برد داره فقط و برای جنوب کشوره
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/80177" target="_blank">📅 01:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80176">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hp15-0ktuDFvTimLc-8kKF_NikkXdipDd74-Anatv5RH9GCbDq83I-T36XO5gL-b2-Uf9iM-p1M9eMTWccJNoSfNIZtUxW9dfkF5PRWeEuoOB2Bdtp3GeMNGVYxpO7zXLbKbXm9UU_0w1nc3ySkPqlwBLcnSOZ3uN9JCqA2KTFlbKP7-7rPx0BPGFJFaacwQmWpfMel6jWZGCz4ZEQ5Nim8k3DloqgRtdT7KbmDBU5QGG-jbVqHzXDyaKRjXyCZ6ebQeGbVtRf2gEwpaBJ1ayKpXgQ1QCvnXloBr7vvsozmeC5YMahCvgaTvIJm_eMK1MPNA4CIA3DNLaqf-M_hV9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی انگار باز داره جنگ میشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/80176" target="_blank">📅 01:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80175">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">جنوب کشور عجیبه
روزا گرمه شبا جنگه
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/80175" target="_blank">📅 01:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80174">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دانش آموزای عزیز سریع بیاید چنلم سوالات امتحان پس فردا رو نذاشتم ولی میتونم دلداریتون بدم.
https://t.me/salamkhobichekhabarchekaramikoni</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/80174" target="_blank">📅 01:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80171">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گویا اهوازو با سنگین ترین بمبا زدن
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/80171" target="_blank">📅 01:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80169">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">یه زمان به لبنان و سوریه و عراق و این کصشرات میخندیدیم که هر روز تو کشورشون یجا میخوره، الان وضعیت ما بدتر شده، ممنون از جمهوری اسلامی   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/80169" target="_blank">📅 00:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80168">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">یه زمان به لبنان و سوریه و عراق و این کصشرات میخندیدیم که هر روز تو کشورشون یجا میخوره، الان وضعیت ما بدتر شده، ممنون از جمهوری اسلامی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/80168" target="_blank">📅 00:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80166">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">شب شد و همون همیشگی و تو همون شهر همیشگی  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/80166" target="_blank">📅 00:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80165">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">شب شد و همون همیشگی و تو همون شهر همیشگی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/80165" target="_blank">📅 00:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80164">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بعضی منابع هم میگن 3 تاشون کشته شده</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/80164" target="_blank">📅 00:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80162">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7JTfFVIUEMUTTcV2z_iEqZprKHfEOHh6BpVYJCIrhR5Zhbf_YQzs3sYbiLS6wpCbj-pb7cs8kRXIbnTuAj0K4IIDrOB3puFw9PsWHQFd7AN95ENXXHqYwJ8TpETBv7FgMrOjxSEH1dcihiUkVDHF6JGoEQZvXjq4BflbrjDmAxpixFsMLOR1kd3PtadonLewOnYuxJg11l-9YcxgR5LHKf4W4WMJAIWmCsBJVPmsDq4b1ZWP4itiHtQJUV03XValn2oRc9kEMLh7bC9EwJBTm-d0rOq937Mi00dcdcl56DlOOl931v_0mW7uynXY8vE0OUZX_I4qgJaxf6f0g1LAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/80162" target="_blank">📅 00:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80161">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JErj-QzMO5DSzHUpaLnK2H8dUdkf-280ZYEDogWfVWE4jokOPiL848uGnFyEzEFbmYrZ1El5QY76WxPuawXSv4kT8fiph9yIn7IRFtWoN9cKsmTE1Mk7zrPdHIA9rtCCcMr5ObhCS8Sw2hRcbBxNVl2OijkA-dYg3hcV1InglxK8Auh31ZQKd2aELKNCnxhGV0X9-G9FJcIEuEyF0JBxnpj1FK6s8lNTvuS1XJvQHRMQigbKeQQ3OXO1kng-U-XhOBvYA8YGnT3CE19WSSz-6Nq-vZVo-CwCSO6uOUcluDVO7tQS_TSSkiJ-2voJH7uVQ78M0akPxDqfLisUpQJTKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرینو کصکش فقط گلر واینستاده فک کنم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/80161" target="_blank">📅 23:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80159">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vZb1sOKp6IQ1O6TmLKqH3NEB2qteL99_EZ2WYusqMidS6YjEspjLpJfZOk34Hot_kOPU_5Ps6xogSX_tXw9WwDz_JDXsF1Orcgw2sab_FuFUmKfJKsDp0teUJBCvImwIqC3vpg9Da22V4ZexfrciWSOf7U1HT-TYoCxkR7TWyZgP2g7szToUl8yNfqcqoGZuRJwfb3fvqFeAWy0KMXiCFxi-Fu00pjLkMlE0zjA81mTwMftEA76JNkv7CRK9Pn3ss2moWEQbWyLCjUwj7BaHSf8W5tgxMw54tORbxwt2kmdixZY9rAdq7DDCW11xQ_LoOIScSnMVnipxQDZb59IOJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CXUipmtb2degKroiOIGlwfAM0NF0eqSfu7_qQSi4a3YdaWUVS6bji-SaNAWv_cWQn2TTUOUOPxwULd9YHeTbYTg72lF4mb-7apHtFB1U_XcxL4unzY3LvIw0D4CIeZJ_C_sEgUzQTe-bjypCECbm6XL5oz2dphIMD73Tnv1ATkXnUdqGKSRs4s1DV9uvCBH5AaQDjrNgKsGpKgAK_g7MT-JPWtJDOJQMnkIC0YqxPj8nTINx681jtyI4-xfuFPDeyJ11s4BUAvE-n-HKh7tiQ3z0CZOv3EYSExGbABJbRXAYOX9oQaHgAycxN-6-F7mODvAii465BgY3muKNrpTUFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امشب بخوابید خیره
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/80159" target="_blank">📅 23:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80158">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">با اعلام دفتر رهبری، مجتبی خامنه‌ای روز سه شنبه در مصلی تهران برای مراسم پدرش حضور پیدا خواهد کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/80158" target="_blank">📅 23:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80157">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">راستی 021G زنده اس؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/80157" target="_blank">📅 22:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80156">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بچه ها یچی میگم نخندید، ویناک و منیجرش معتقدن مایی که زمان جنگ وصل بودیم به سپاه وصل بودیم و قراره بعد انقلاب اعداممون کنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/80156" target="_blank">📅 22:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80155">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">بازنده تمام بیفای دکی صدف بدبخته  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/80155" target="_blank">📅 21:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80154">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">بازنده تمام بیفای دکی صدف بدبخته
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/80154" target="_blank">📅 21:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80153">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ft2w_QIUMuf0ZaVWGsIpUxynWpNL6UmAMLYohlIZycAMO5GNVI2UBbbeTtV4mP00PJ-JImpRqN4iUkfgN23NTxuRxmoFQ3ZE1tX22rBZCxKWDj9a1BrTfeUPAX8yl4u_Wz72Szr4i40hTzf_8wvhupDEZmwpEVpqb7vMdNLPmaq5A8-GgfQz6QTf3pdyNg3TK45NQSeOrGuYLAsSMKPNRnR7XzzMUJlEWkn3ikCRly5XI2077oBmmUke_55S3Syi7QVLh6bgVg-4-3fP-9LknwelK5wMNEVMkIhGnEP3oGQ7o1DAlwVK4tX_rSj9yM-wADCrTALnn6L424uwm7sBAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیر تو جنگ و بیف بعد 6 7 ماه حضرت لنا رو بچسب پسر
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/80153" target="_blank">📅 21:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80152">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">این حرف ترامپ که میگه امشب بصورت ویران کننده ای ایرانو میزنیم فیکه هنوز چیزی نگفته
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/80152" target="_blank">📅 20:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80150">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">14 تا سرباز امریکایی زخمی شدن 4 تاشون وضعشون خرابه بعضی منابع هم میگن 3 تاشون کشته شده اگه سرباز امریکایی کشته بشه احتمال گسترده تر شدن درگیری یا حتی از سرگیری جنگ زیاده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/80150" target="_blank">📅 20:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80149">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e73f890bb.mp4?token=JoCblb5JP592G4adQflJa6nlniJgkLJy8S3jOg0KPp_h7Qkfv62IB6eEUksivYMezkDb7ZqoKJrFHlGungPn2utfHkEGvaOPy81QkEw3vJuhCd38czaiLJYPT_Ycec_00ImQmPWzVyBOqXsHLUqM5ciWKOuU290cU-6Jr7oXY5HJHohVPWK8vo0SUzBGeRRl0aPiEWfj_4YA5pTKP7SDbai1yWoxaUdedI00i7GLrQC-kpuX5tlUpTbS-BFz16a6i2WpbHBZBmReaJlupcDjIdE8fcSB7jG2LNYKeVj5AYBev20J5QEego_Z3JCMbppYclsZlDvXApwZrtLm5NU3Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e73f890bb.mp4?token=JoCblb5JP592G4adQflJa6nlniJgkLJy8S3jOg0KPp_h7Qkfv62IB6eEUksivYMezkDb7ZqoKJrFHlGungPn2utfHkEGvaOPy81QkEw3vJuhCd38czaiLJYPT_Ycec_00ImQmPWzVyBOqXsHLUqM5ciWKOuU290cU-6Jr7oXY5HJHohVPWK8vo0SUzBGeRRl0aPiEWfj_4YA5pTKP7SDbai1yWoxaUdedI00i7GLrQC-kpuX5tlUpTbS-BFz16a6i2WpbHBZBmReaJlupcDjIdE8fcSB7jG2LNYKeVj5AYBev20J5QEego_Z3JCMbppYclsZlDvXApwZrtLm5NU3Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/80149" target="_blank">📅 20:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80148">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4ozkK1Q2MRN2geNRASj5cEDv8skDIqY9lv9AETpv772-LU84s2HwqamHebzjtvaad11gHlx1JM8gqgP09rkrtjJYHedmrmUXWlff1sYQTKq4Zxl1PrQIUoQ7ZhZdhhJaKUm_UIPVG-Aw9IIeB6dkW9HWltuOBOqMhday1FiCl65yKsi8S0d4bXOSTb8OsCDtzkB9hNkIzHfdoMRClHMxoyXD2nHXhvOFXBJ8IDKo60bXbOAdAhnkdoXWR80UJ1MoBjCwjVLScOSmqCtmypUU52sZ4KGCtxAkgQwZjZZtmwW_Yf_7vwUGmA8XlnLNB7aeVrEGykJvn0f5u11M25aDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آره داداش تو عضو بلادم نبودی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/80148" target="_blank">📅 20:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80147">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🧠
دستیار هوشمند پیش‌بینی بت‌فوروارد
✅
🔥
با قابلیت جدید هوش مصنوعی بت‌فوروارد، تجربه‌ای حرفه‌ای‌، دقیق‌ و سریع‌تر از پیش‌بینی‌های ورزشی داشته باشید. این سیستم با بهره‌گیری از AI امکان تحلیل بهتر مسابقات و تصمیم‌گیری هوشمندانه‌تر را برای شما فراهم می‌کند.
🎯
تحلیل دقیق مسابقات با هوش مصنوعی
📈
بررسی آمار، داده‌ها و اطلاعات بازی‌ها
⚡️
ثبت سریع پیش‌بینی تنها با یک کلیک
🧠
چت با هوش مصنوعی برای دریافت تحلیل حرفه‌ای
🔥
استفاده از ابزار پیش‌بینی‌ساز برای انتخابی دقیق‌تر
🎲
ترکیب قدرت هوش مصنوعی با هیجان پیش‌بینی ورزشی
⏩
با دستیار هوشمند بت‌فوروارد تحلیل کنید، سریع‌تر تصمیم بگیرید و حرفه‌ای‌تر پیش‌بینی ثبت کنید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🅰
g21
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/80147" target="_blank">📅 20:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80146">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سلام فرید جان ما قشمیم اینجا رگباری صدای انفجار میاد تموم هم نمیشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/80146" target="_blank">📅 19:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80145">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">جنوب کشور درگیری بسیار شدید گزارش شده</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/80145" target="_blank">📅 19:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80144">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">فارس: شنیده شدن صدای چند انفجار در بندرعباس و قشم.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/80144" target="_blank">📅 19:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80143">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">وضعیت طوریه که ممکنه جزایر نشینای ایرانی امشب تو ایران بخوابن صب تو آمریکا بیدار شن
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/80143" target="_blank">📅 19:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80142">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">خلاصه ترک:
کس ننت
کس زنت
بابات سپاهیه
پدرزنت سپاهیه
تو خایمالی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/80142" target="_blank">📅 18:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80141">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دیس ترک جدید ویناک به نام موش زاده منتشر شد.   SoundCloud  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/80141" target="_blank">📅 18:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80140">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دیس ترک جدید ویناک به نام موش زاده منتشر شد.   SoundCloud  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/80140" target="_blank">📅 18:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80139">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دیس ترک جدید ویناک به نام موش زاده منتشر شد.   SoundCloud  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/80139" target="_blank">📅 18:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80138">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">بیت چرا داره هوس شد؟</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/80138" target="_blank">📅 18:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80137">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دیس ترک جدید ویناک به نام موش زاده منتشر شد.   SoundCloud  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/80137" target="_blank">📅 18:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80136">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دیس ترک جدید ویناک به نام موش زاده منتشر شد.   SoundCloud  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/80136" target="_blank">📅 18:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80135">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دیس ترک جدید ویناک به نام موش زاده منتشر شد.   SoundCloud  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/80135" target="_blank">📅 18:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80134">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">این که همش ناموسی میده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/80134" target="_blank">📅 18:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80133">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اومدم ختم کاکولد
بجا تو میکنم ننتو بلاد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80133" target="_blank">📅 18:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80132">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دیس ترک جدید ویناک به نام موش زاده منتشر شد.   SoundCloud  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/80132" target="_blank">📅 18:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80131">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بیف سر دقایق بیشتر موزیکه نه پانچا، کصکشا مگه پادکسته</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/80131" target="_blank">📅 18:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80130">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">دیس ترک جدید ویناک به نام موش زاده منتشر شد.   SoundCloud  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/80130" target="_blank">📅 18:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80129">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دیس ترک جدید ویناک به نام موش زاده منتشر شد.   SoundCloud  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80129" target="_blank">📅 18:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80128">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkVD5AMRKIsADY_d1AQzm7SSzleJt9gcVqw34UTp-u0mZjX5-uUnMdd2tDw_1JM0qBwXcP5nQVc_hCg5x5Rx5AYGhwh7kfZU6AViBI9BMCfRWeuyAJPUVDjrMUjYJRhC8CYZDbGCo8qvBT93A1w1Ev-ScFdECbr0-3HgAo2uoCfef6RQmdnNZZGyWTImIp9JRPgcug4PUY7J_vKqX-oDpZKWNk_6fFiPUf2QPq54GkRXv6F8SiHkRuSgcwI4lJqWgu797qXnERStPSKzqMzsohjd17unnJ5Dg9Gew1ni-GYv0ljLkLUTCCZ3zNBpEM8SHK365EucX886AzrOobdPQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس ترک جدید ویناک به نام موش زاده منتشر شد.
SoundCloud
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/80128" target="_blank">📅 18:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80127">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ویناک کسکش بسه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/80127" target="_blank">📅 18:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80126">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aiPobBzsqy6IXgQJ86V7971IND3_8e1HamZaTnd75fccyScBpaQI2mZUWwJ6DBRHWXFPVwDEeNvIcYxGUsVUUrmNggZiUOSMNMQCjerIDauAbiKMehxz4XrTzIfRMoUWChc6NxeOfHTqRtsoyxOtTVUPznOK9vJ_PIxYSEf_WgDceh6GFAH7ECkuj3vbIuwJbcNqcP--UZvwG0isonPcfhWi3x7h8OeoTJwJlqhYO0kQ9QHP1vIozgFjXRZrMwjMtB8cw4LadS1LGB5EgJTnvKtYV3jvflRu-IsvLx4bMY-U3XN1CYY_A8mfh4Jblq5lotUA46bdgGsj7IiQK-MGnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید. ۳  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/80126" target="_blank">📅 17:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80125">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ویناک فک کنم داره موزیک یساعتی میبنده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/80125" target="_blank">📅 17:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80124">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">حالا ما هیچی، کانر خودش خجالت نکشید بعد اینهمه تشریفات با مشت اول بگا رفت؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/80124" target="_blank">📅 17:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80123">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6869027e93.mp4?token=M2v76KK2n_HPzmrzMYJMwWykq04UNl4pC9nsR-X4MbgBpyVe4idKWBRqlW0dA6tH-5Vj-q1eU5xF5k4tMZKx3Mm-lHGfIg3LlYiIFdmCKjDdTr4ml83M7O-I99a06N374lFgEdlCxKh73AGF_DGZM8TCqsysF3ny2yiwLNccvwsyhrFtG2f5MBd0P43ePG3xtxLs24OZbmHdIUYE2JdkHzzAgN8R0Mze5JICGbxhFYIcC98_6dlCvcQCSJK856JjefO0V7mU_NrOwtw5TUqOCYYaRh6x56Lx2yI3tGlhhtgcgnGkE0Epu17zYE7KRg1_ikn008ypSwKlEwOP247lfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6869027e93.mp4?token=M2v76KK2n_HPzmrzMYJMwWykq04UNl4pC9nsR-X4MbgBpyVe4idKWBRqlW0dA6tH-5Vj-q1eU5xF5k4tMZKx3Mm-lHGfIg3LlYiIFdmCKjDdTr4ml83M7O-I99a06N374lFgEdlCxKh73AGF_DGZM8TCqsysF3ny2yiwLNccvwsyhrFtG2f5MBd0P43ePG3xtxLs24OZbmHdIUYE2JdkHzzAgN8R0Mze5JICGbxhFYIcC98_6dlCvcQCSJK856JjefO0V7mU_NrOwtw5TUqOCYYaRh6x56Lx2yI3tGlhhtgcgnGkE0Epu17zYE7KRg1_ikn008ypSwKlEwOP247lfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشاسین تیراختور
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/80123" target="_blank">📅 16:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80122">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ry6LH1V6_jzj2qx_nhJKYqPA2nJyo-NYSpTFMCQw3dOLqSDN-3DBgZETPkw-NXSpEcsKvLbWFrPV3iLidOlxnjwVyXtrU8Nq4ppg2VzNupNxSpCsE2Zyw29-0-JTD-YV9TgBa6l6Mq7qfiFl6gyJ0JzfX1J3B3sA0rNoeSEwqMZpLYmAJkQrpeVnqsIqBvjq2qDvDLfr_Qien3T6iBR4-jQopp-f0HxSZ-41XBUQfdqcRs3vrXnN5kneyB-t93Ps3GapwWwa5Qqj35Sw9fsanvU7VGkIrlJghB8sySfJxxygo56Cto7_RkgE9qt3fXNsgwg1CUezw3bdb6noZl-WaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادرجنده من تو این هوا بدون کولر چطوری زنده بمونم وقتی برقم قطع کردی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/80122" target="_blank">📅 16:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80121">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">دشان از تاکتیک های ناشناخته فقط یچی شنیده ها، اومده خبر داده بیرون که سالیبا و اوپمکانو همزمان مصدوم شدن و نیمه نهاییو از دست میدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/80121" target="_blank">📅 16:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80120">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKpXrPiWfiVbqhWl_JyyqGAAcppF1PPwthGRCXjP_Wiw_rG2b_YorLrHfzBZQ7eV1jpHOguTx8d4TRPDMYbRyMFpYs_s8oAYcdtYN7NlIVt8DQvlhDPDNtRZ1L9ti82SR-XNWJlH0Mr6bKFUiYErK-8RwM2Gt7RrEChp9OTP7imfhARDdIUVrO9rnjJz2lKXRxfPvTRMcEfJVNYMI4ON-X9MRDdbJVrlc7fS4rhEapAZJoM6S32zdpG7-OiSuugmVwUrEUPBlcSdTJ-kGWdwsiJHxO8kpy_VqBR3NacfG8t3NPaNA3IdsUEfXAS9gNcBFxi7HAA8fW6FjDdF1cNHlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریک جان کیرم تو ناموست
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/80120" target="_blank">📅 16:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80119">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دوستانی که امتحان دارید، فکر کنید موشکا ستاره ان
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/80119" target="_blank">📅 15:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80118">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">امتحان چطور بود؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/80118" target="_blank">📅 15:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80117">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">این رونالدو فنایی که به مسیر راحت آرژانتین برا نیمه نهایی اشاره میکنن خبر دارن که اگه تو گروهشون اول میشدن همین مسیرو داشتن؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/80117" target="_blank">📅 15:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80115">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">عجب امتحان پیام های آسمانی سختی بود.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/80115" target="_blank">📅 14:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80114">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">شبکه کان اسرائیل:
ترامپ تصمیم گرفته که محاصره دریایی و عملیات نظامی‌ از سر گرفته بشه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/80114" target="_blank">📅 13:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80113">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">شبکه ۱۴ اسرائیل گفته سپاه به کارتل های مکزیک پول داده داخل آمریکا ترور انجام بدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/80113" target="_blank">📅 13:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80112">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ Fun HipHop ](Mehdi)</strong></div>
<div class="tg-text">والا من هرچی لیست تیم ملی انگلیسو نگا میکنم تیم خوبیو جمع کرده، این بازیکنایی که دعوت نکرده فقط اسم داشتن وگرنه بازیکنایی که جاشون دعوت شدن سال بهتری داشتن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/80112" target="_blank">📅 13:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80111">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">از ۴ تا تیم حاضر تو نیمه نهایی جام جهانی بارسلونا تو سه تا تیمش بازیکن داره و فقط تو آرژانتین بازیکن نداره
ولی بارساییا فن آرژانتینن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/80111" target="_blank">📅 13:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80110">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">میچ مک کانل یه سناتور دیگه هم سکته کرده و به بیمارستان منتقل شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/80110" target="_blank">📅 12:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80109">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">اینطور که اینا گردن میگیرن، همین روزاس موساد ترامپو بزنه بیاد بگه خب اینم گردن بگیرید کار داریم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/80109" target="_blank">📅 12:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80107">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fc-f34Lu8VPI9ikm3tmaGVgvn3Ojv7N7r8Z0uPHgLNYAcKTxJ7mlAuJyYxx52DrPUi5-tswxvOm-ZFPLunIppszcba_vkD5malz3fVYJj700wwpgwhqf8jzPeFcbYnIwicVedgjslYn2Vhr12utCnVLJvNYeAfv6bUbYaWYFmyv49o4ypy2MhRxKgZcvNke5LmMOCHi_89MmkTQew_qd0g090_hBu3Sspw3jMykpUlMUqBZwQMGV2gYP1OFdXSsb30do_XVIKXYG2m5VrIzX0PXNDIOEHWZXCgl6xHHFs2SnsyBWrg1vU-aONeLql40_L05kW4q6DvxYPlvkkgMrpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84de9e91b7.mp4?token=kT3jEs-hXLr8NKCyDAitxm1bQD5XgZ2tvWDy9HXRJ5CRlS0jWtiw0QfvmnXRAKxTETwOvao6L848MwGa6aKzVKc_1wXMVMf-UDjheIu4ZTq5Cet6plE0yOkqY7Dy9PE4VQrTgcorxbQ_p0DS_byzlGksMSeQq_0Ouf_X4Gx83RhVGOezyWZO0YYqG5ZmKuuL9wGSESNunO14LLPLCyV3geKGqFu85d_aftOV8fJEcfEG6GFklwueDa9z24xouTecvkIzWc0xNbi1QtbmnOCiVZQxi2wZf0xE5FMcR_fXf7jp1H6scXBiq6C3Xl7Srlgk-foZZb9M7TpbGO_Y9-L2xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84de9e91b7.mp4?token=kT3jEs-hXLr8NKCyDAitxm1bQD5XgZ2tvWDy9HXRJ5CRlS0jWtiw0QfvmnXRAKxTETwOvao6L848MwGa6aKzVKc_1wXMVMf-UDjheIu4ZTq5Cet6plE0yOkqY7Dy9PE4VQrTgcorxbQ_p0DS_byzlGksMSeQq_0Ouf_X4Gx83RhVGOezyWZO0YYqG5ZmKuuL9wGSESNunO14LLPLCyV3geKGqFu85d_aftOV8fJEcfEG6GFklwueDa9z24xouTecvkIzWc0xNbi1QtbmnOCiVZQxi2wZf0xE5FMcR_fXf7jp1H6scXBiq6C3Xl7Srlgk-foZZb9M7TpbGO_Y9-L2xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداسیما گفت که گراهامو ما کشتیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/80107" target="_blank">📅 12:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80106">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اینطور که داره پیش میره یه ده تا کشتی دیگه بزنن از جنوب کشور یه خاطره میمونه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/80106" target="_blank">📅 12:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80105">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0f7af99a5.mp4?token=K4Q5i7eYKZR8tPwH5P5aoZ1etTbH9MG6qAvOqjbFJhVc_nn-p67zZIQtxvHWNlLleSmLWp_ZiKgi_kdQC7UbkfkbWxKfFdv2dKxLp2FN_xYNUCRXfN1IHKFEHYhBi6ojD0cY5OyjNJtmcX9ICWtuDUglWgbL0sWPb4P1cirs0iYufjCebsGgpRCOSVRdJMQX35rZt2cSDfYBDl88HNxQeNp4NpeucisfOmB1FUGeGz6VpWFE9JjUHRLy0F9eLKlnpy6dI7xLLtvMjVVsEjRzzK4D4qbU55-F6g_QFpcBRt0S_4ARwthUXbdmDATcnuhho9Pvn_yo87WhfLawdvgZog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0f7af99a5.mp4?token=K4Q5i7eYKZR8tPwH5P5aoZ1etTbH9MG6qAvOqjbFJhVc_nn-p67zZIQtxvHWNlLleSmLWp_ZiKgi_kdQC7UbkfkbWxKfFdv2dKxLp2FN_xYNUCRXfN1IHKFEHYhBi6ojD0cY5OyjNJtmcX9ICWtuDUglWgbL0sWPb4P1cirs0iYufjCebsGgpRCOSVRdJMQX35rZt2cSDfYBDl88HNxQeNp4NpeucisfOmB1FUGeGz6VpWFE9JjUHRLy0F9eLKlnpy6dI7xLLtvMjVVsEjRzzK4D4qbU55-F6g_QFpcBRt0S_4ARwthUXbdmDATcnuhho9Pvn_yo87WhfLawdvgZog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانر هم صب همین که وارد قفس شد مصدوم شد و فایتو باخت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/80105" target="_blank">📅 12:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80104">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🧠
دستیار هوشمند پیش‌بینی بت‌فوروارد
✅
🔥
با قابلیت جدید هوش مصنوعی بت‌فوروارد، تجربه‌ای حرفه‌ای‌، دقیق‌ و سریع‌تر از پیش‌بینی‌های ورزشی داشته باشید. این سیستم با بهره‌گیری از AI امکان تحلیل بهتر مسابقات و تصمیم‌گیری هوشمندانه‌تر را برای شما فراهم می‌کند.
🎯
تحلیل دقیق مسابقات با هوش مصنوعی
📈
بررسی آمار، داده‌ها و اطلاعات بازی‌ها
⚡️
ثبت سریع پیش‌بینی تنها با یک کلیک
🧠
چت با هوش مصنوعی برای دریافت تحلیل حرفه‌ای
🔥
استفاده از ابزار پیش‌بینی‌ساز برای انتخابی دقیق‌تر
🎲
ترکیب قدرت هوش مصنوعی با هیجان پیش‌بینی ورزشی
⏩
با دستیار هوشمند بت‌فوروارد تحلیل کنید، سریع‌تر تصمیم بگیرید و حرفه‌ای‌تر پیش‌بینی ثبت کنید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🅰
r21
💻
@BetForward</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/80104" target="_blank">📅 12:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80103">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">انفجار در فرودگاه بحرین.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/80103" target="_blank">📅 10:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80102">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">لینزی گراهام درگذشت.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/80102" target="_blank">📅 10:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80101">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">آرژانتین هر مرحله که بالاتر میره بیشتر به هنر و توانایی پروردگار بی بدیل فوتبال جهان پی میبرم
با ۳۹ سال سن یک تنه این تیم رو تا این مرحله آورده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/80101" target="_blank">📅 07:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80100">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گل سوم و تمام
صعود آرژانتین به نیمه نهایی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/80100" target="_blank">📅 07:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80099">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">لاپورتا ناموسا بخرش
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/80099" target="_blank">📅 07:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80098">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">یا خدا این چی بود آلوارز زد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/80098" target="_blank">📅 07:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80097">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دوستان تازه بیدار شدم اتفاقی افتاده؟
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/80097" target="_blank">📅 06:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80096">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIGfErMxjllfZxt2S-IZnE1daFtDkH0LOyU6XLVkB692iuiLDiQL1XnLCBUO1iVbsnAT_q0cftG_fmLzFDYR8wLLaUP0qqDxOy4JLz9P7B2b_ckjG2hWtbuqsJhntJTzPHxwYxLIS-gE0Ref8hrD_JjXGh1tzjID1WwyFViwGPInu1o29F2PsyX6Rsnf2czj5o-EldpLmJLEd6FL2aSTy_K4wix66wKVNPCMgpI4szSMzfZbu-EW9_9-2p8gJQ5dNJDlo7WrOYn_ZiZjWM8aTv86D_W71IG2sw6RhtZXV6Jtbry0QLX8bZn6B5KQZ4LVUExj5HhPiNJIfTLDHYNQSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب آرژانتین مقابل سوئیس
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/80096" target="_blank">📅 03:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80095">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">پیت هگست: ایران انتخاب بدی کرد، حالا تاوانشو پس میده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/80095" target="_blank">📅 03:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80094">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">فعالیت پدافند ها تو تهران
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/80094" target="_blank">📅 03:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80093">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a009afea3d.mp4?token=ae75XVVijPoeRgNvxIMJXoC94TPwcUXqddP47qxFQJFVuYrnafkVUKe6Z_PaHsh3tAvjVLk7bU2fnA8Gvj08lo8Prf-xQvyFWt5mK3SPE2Q1InnX-cLh7w_4K139YVvRQMQEbGQghgb_g15bYk1Dac0cLPHyOv0_jjNX00buKpzo1xJwWZDsoviTOBD7sCJuFtrgMGMdhjHxh5Dsnv_Sh3suGzUEQ-pEfOOoWEg8quABqIyRw-FqtnA7qhykIEkbdFm81ANBm-yc3p9EZWbUkLdiYN_OlQM0del7NOZAfsj4sk6n2z3LtzZzE5-XyZRi5TxwrhFSdTlPhNma56fvXC2v6V59MSlmaky2nKo9G8mkj7zw6B9iFUQQaGajP3dZ1o1-Mj3Jc99eRQRASNqzYYqODjPYU7uYChfEmxlbUyE1kIlpreNI7-8qX7NUb1dBWTdsZkSLAnf790vp3c228mz69FJe6ip18oBJCnxzMN026GG6Bx1fPLfkrv-7P-LKz0wljTSXQFrkq-mAxhLWtk6psv5bQ4TqlEU3VbnpRYz4hCG5zrBmzuaouk20UR1OaCJ-vVooM6qxnWtTY03B2SroOqmBsXlLM4HjqvNe0oX2_DkhaczalBSDTXIOoZgx3nKJt0feP-t-45lvVJydQZRfpW8gf8D615Dmzsp-rJY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a009afea3d.mp4?token=ae75XVVijPoeRgNvxIMJXoC94TPwcUXqddP47qxFQJFVuYrnafkVUKe6Z_PaHsh3tAvjVLk7bU2fnA8Gvj08lo8Prf-xQvyFWt5mK3SPE2Q1InnX-cLh7w_4K139YVvRQMQEbGQghgb_g15bYk1Dac0cLPHyOv0_jjNX00buKpzo1xJwWZDsoviTOBD7sCJuFtrgMGMdhjHxh5Dsnv_Sh3suGzUEQ-pEfOOoWEg8quABqIyRw-FqtnA7qhykIEkbdFm81ANBm-yc3p9EZWbUkLdiYN_OlQM0del7NOZAfsj4sk6n2z3LtzZzE5-XyZRi5TxwrhFSdTlPhNma56fvXC2v6V59MSlmaky2nKo9G8mkj7zw6B9iFUQQaGajP3dZ1o1-Mj3Jc99eRQRASNqzYYqODjPYU7uYChfEmxlbUyE1kIlpreNI7-8qX7NUb1dBWTdsZkSLAnf790vp3c228mz69FJe6ip18oBJCnxzMN026GG6Bx1fPLfkrv-7P-LKz0wljTSXQFrkq-mAxhLWtk6psv5bQ4TqlEU3VbnpRYz4hCG5zrBmzuaouk20UR1OaCJ-vVooM6qxnWtTY03B2SroOqmBsXlLM4HjqvNe0oX2_DkhaczalBSDTXIOoZgx3nKJt0feP-t-45lvVJydQZRfpW8gf8D615Dmzsp-rJY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شلیک موشک  ATACMS/Prsm و HIMARS از خاک بحرین به سمت ایران
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/80093" target="_blank">📅 03:18 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

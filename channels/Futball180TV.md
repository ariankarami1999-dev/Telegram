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
<img src="https://cdn5.telesco.pe/file/E8_LYLo-hCQryOrexXvw3KDvoPxcmP3YV9muPtyQ3U0fJywo3m848TXcePVBZUoZa3GSQeF9NbqOxV79NawiaoFphVQ26FdmVky-SrhnMi5-29KgDtf_rv3Okqk5qclU0sk67pc-5QQl-9mEVEHgweL91BFcqx-vDsEdHCTISe7LbYRfhUDjv0aUuCoFzdRDo3U0vxz6UIfqFfEXdhsbaiEvum07yVhpza0HARGh_JA3iCxutFjMw8_umTT3DvizO69MuHvyCKRg4UL9BO3MuhU3Gq7QUlJ-aCOxhPaRCHSutPoqyQfeGQFNn-qXwB9T222Yz71ohE8DtvGCsMunrw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 520K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 14:01:43</div>
<hr>

<div class="tg-post" id="msg-102137">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rZySUpoedLvmValKfuRzVO4_ywSpLcv1IxkIU7w_llg-lYT6zveoEe5kKzE8b231KRSxTl9cQX6Fyd7RAsrx8nhl8xRsfpPj2PaTqF1Z0HNj8QRyxcvvT4WaWWwJm1LtshCMzApAaNTRWdGS0CaQlCIi2nm5kM7mBq6py4B-lMZxquuHcfDpKxZSni3ROBI_WbfTcfCwdJGmw3Yj7_eUc8ZAj9O9FNXakwu4cnPslYXJW04ulorb4QWP15A6Q4EKViv3ldtiLHQ3zcRWPFekxZ-nnLdaWOCYfr_sm8gsCW-q6nhaRIYGK7Kfc4IdkCpRRUYfaCN43GFiiNpt18G1Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از دیوید اورنشتین: وولتماده مهاجم نیوکاسل مورد توجه بارسا قرار گرفته و به صورت قرضی در دسترس کاتالان‌هاست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/Futball180TV/102137" target="_blank">📅 13:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102136">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔥
کنترل‌‌توپ‌های ستارگان که منجر به گلزنی میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/Futball180TV/102136" target="_blank">📅 13:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102135">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iLiA7rKCKMSyb88wfeHFDBDLu0NvWpAG8WAGyYLr333ZzlvZ2efoHZhc8VUDi_bbiaNdj-CQarCbvCW-A-9T6seGWy3g5Twwnsy0ul-ANtgRQ9nJ1uvr8m0nirMn2W03kn7tT6NNZwoo08AxoLWnX4DP2n65sUBhCBIL_LU0KuxnRJCL91sFzbnLss2PMiewLvTkmCISEY0kKNHFA6Apc3YVUKic8-gsUlQGsUYGXeM0e_xNe0WISrfZ1CiUIDfm5sWYqe5Kjzo_bJ2F3Nu7tVoE11crd5lG4XO0U9DNPqRsmbMlF2enRKQfeyxHW4SVtJBfKAQAJ5WPz_ZNgWpacg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
باشگاه بورنموث علاقه‌ای به فورش جونیور کروپی به بارسلونا ندارد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/Futball180TV/102135" target="_blank">📅 13:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102134">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/792acb1bf3.mp4?token=HU5xeRkFhQJYTScjssOMLWveWDXYSXY6iFQUgXBhlmi-i3Jn_0NaaEys_EOBknkCcyDD7HqbMg_K4QNLei_V6p5D0pCABEMyCL78BC_NOhRj1SokEX1JQSyBXpSX-FU_8DbKU_lLXo1VsHri2A4dfubtVw1yobjA4QbUjEafUkjRRJsfzLUV6l7455bQOUn6pu2zJUMnsXUkS1uAbb64n6WPqxqU3Kl8Dr79TvZsyl84mlj0CLWBhrkWCTIj2zlwffBvbhoJRwu7t8vCCvk-rTSH8CbXkkwq_zG1RBVxoF6ZKNzDSnHyDOk0BAdIOfKVx4T-mCsqkSqL47bdJ9b_egji9M3qztq35_bVM7_ldChygf20QG-StAkTrTSKS5mHUB1z1kqE5uW_yHcXlpsQYlo-N36mN9eHyjwtcmUc_yxmRZKhRGd494aCMDSPmjkeJTfeQa5s22D2ouaOQaFuZD7pneA7kKnCez4u_yKU6FtL0laFOs8uRpPTmBYuSUM0axx6nBwCTT0t3OwK0qvFqxXAtBTjhQP010-cFeVCZg7bmf5dSu7QPLNNfiluqpNtLcsNEnSkjaHO97GvxvncBEZgpMdhj_lTSwG9iSFfPiYEn0NXvdT2iPtBWY_aGrCb52UrmZzA4NCyba3PemXDBv6a3SL8GPZ0HN7_Eo5bIo8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/792acb1bf3.mp4?token=HU5xeRkFhQJYTScjssOMLWveWDXYSXY6iFQUgXBhlmi-i3Jn_0NaaEys_EOBknkCcyDD7HqbMg_K4QNLei_V6p5D0pCABEMyCL78BC_NOhRj1SokEX1JQSyBXpSX-FU_8DbKU_lLXo1VsHri2A4dfubtVw1yobjA4QbUjEafUkjRRJsfzLUV6l7455bQOUn6pu2zJUMnsXUkS1uAbb64n6WPqxqU3Kl8Dr79TvZsyl84mlj0CLWBhrkWCTIj2zlwffBvbhoJRwu7t8vCCvk-rTSH8CbXkkwq_zG1RBVxoF6ZKNzDSnHyDOk0BAdIOfKVx4T-mCsqkSqL47bdJ9b_egji9M3qztq35_bVM7_ldChygf20QG-StAkTrTSKS5mHUB1z1kqE5uW_yHcXlpsQYlo-N36mN9eHyjwtcmUc_yxmRZKhRGd494aCMDSPmjkeJTfeQa5s22D2ouaOQaFuZD7pneA7kKnCez4u_yKU6FtL0laFOs8uRpPTmBYuSUM0axx6nBwCTT0t3OwK0qvFqxXAtBTjhQP010-cFeVCZg7bmf5dSu7QPLNNfiluqpNtLcsNEnSkjaHO97GvxvncBEZgpMdhj_lTSwG9iSFfPiYEn0NXvdT2iPtBWY_aGrCb52UrmZzA4NCyba3PemXDBv6a3SL8GPZ0HN7_Eo5bIo8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
امیر حسین صادقی: قلعه‌نویی هم مثل علی دایی جر زن است؛ کاش آن حرف را نمی زد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/Futball180TV/102134" target="_blank">📅 13:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102133">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9afeb8a4ca.mp4?token=Rpq06E-dnaF5Os_670zH6ivdVpY4kveHT7icSqpnU-sEgEVcO34Du_lxRWdQ2gzbmiL8Y4Aq9i_d9v9wuk8ngzaoRbEWsrUf84Y5l9Ur4J3PETCk9WVN0FWozZ2NMZNWS0_D7arGo_XYuYjUkxMU981Lakn-zll0Lrk1RkCek2BLIc0TzndGqDqfEIw96tvu2EecpJF2eaRBeSh6sBgZUvIJRh2lEjGOQzvIWagxIG9iNrX3Poq07PZcxNxv6iBSBxnfl8hrj8K6ZcqwRrl38a6KqrHQPTbYu1R3vV8zWB6S-pjnIaC3dTU_rhy1AtI2zUuxT8a6mm2GkNQfK5c5v37gTD_TyVHZBsanewtTgGTfkCNc4UQ8_RXCoofWmGaRD06S8e6hOE5NMTvgajK4XtsHB1qV0Btb95SL-FzvR-jNywHZU7Iw01b-x56fkDEbs0EpfS7pEFJb2jo5POZS9oBn5oUmdBqPw5FwefaLld4BOYqihZ_FXq1aIjtdBverDxjyb9sqThprlZWMIWYOE6NuYdBu9-1SV-52yRWZUHx4a5q_zVQuUvf-RDPDnkTgGp_3Uwi8aa9EqdE9d0Y7MZyfNDVFFWgG0SoqevciEgXChL4BG9zDyVxKGmvWPEvlQPCiGGXsdJuiMI22XIlYUqrK3ZEn2muL2Jp9KX3N9Z0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9afeb8a4ca.mp4?token=Rpq06E-dnaF5Os_670zH6ivdVpY4kveHT7icSqpnU-sEgEVcO34Du_lxRWdQ2gzbmiL8Y4Aq9i_d9v9wuk8ngzaoRbEWsrUf84Y5l9Ur4J3PETCk9WVN0FWozZ2NMZNWS0_D7arGo_XYuYjUkxMU981Lakn-zll0Lrk1RkCek2BLIc0TzndGqDqfEIw96tvu2EecpJF2eaRBeSh6sBgZUvIJRh2lEjGOQzvIWagxIG9iNrX3Poq07PZcxNxv6iBSBxnfl8hrj8K6ZcqwRrl38a6KqrHQPTbYu1R3vV8zWB6S-pjnIaC3dTU_rhy1AtI2zUuxT8a6mm2GkNQfK5c5v37gTD_TyVHZBsanewtTgGTfkCNc4UQ8_RXCoofWmGaRD06S8e6hOE5NMTvgajK4XtsHB1qV0Btb95SL-FzvR-jNywHZU7Iw01b-x56fkDEbs0EpfS7pEFJb2jo5POZS9oBn5oUmdBqPw5FwefaLld4BOYqihZ_FXq1aIjtdBverDxjyb9sqThprlZWMIWYOE6NuYdBu9-1SV-52yRWZUHx4a5q_zVQuUvf-RDPDnkTgGp_3Uwi8aa9EqdE9d0Y7MZyfNDVFFWgG0SoqevciEgXChL4BG9zDyVxKGmvWPEvlQPCiGGXsdJuiMI22XIlYUqrK3ZEn2muL2Jp9KX3N9Z0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🔥
چند ضربه کاشته تمرین‌شده و تماشایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/Futball180TV/102133" target="_blank">📅 13:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102132">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVf77KjXtwBH9q6JF5AsNT90x9Prs4Nes91JWtfpTKE8kd76X4c9ya00aVopC-1Ya_4uLExJnG_dQGze2ga_8fXQ2n9FmWiGyBhCTa6phJEJ1eP8KNCSLesHBUzlXsn7oCvXoE9c9PmcE-EqmYxN7F5NhO-SoOZWaZ4WEQeQiGSt4SIg9E53nQzlqpO6wVuVBK51hmRkRlAokCKUquodhNGnRvegGUyTixZCtSuM3QBzcVvAWMT4p5mlRR-L5Hi0GpcMqJjN8HETchmCi5u-61M4BlDtZMgTlT48fkVRtvkMl2LftBgkW-Qa2WLLZ4PRLat5t9Hh0h07f0squgKvwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دنی ولبک خرید احتمالی چلسی در فصل گذشته پرمیر لیگ بیشتر از خریدهای جنجالی تیمای بزرگ گل زده!
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دنی ولبک: 13 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بنجامین ششکو: 11 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هوگو اکیتیکه: 11 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برایان امبوئمو: 11 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ماتئوس کونیا: 10 گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/Futball180TV/102132" target="_blank">📅 12:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102131">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
✔️
#رسمیییییی؛ زین‌الدین زیدان تا سال ۲۰۳۰ سرمربی تیم‌ملی فرانسه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/Futball180TV/102131" target="_blank">📅 12:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102130">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKPGpCIyeI0o5nrw2pQ1OKWnUUBgAAv0PpOoLcbR_U0k_IBHzyBQWemXH5wm3BMZGDCE1CuN3QL-4Vj1dDlCMGEd9KKjZsZvIUg-eQ3uW-aqNpgaJ6cu7fEHm2cu8CDvb9KqfTtweSkyzknS6iuStj4RwMKN6rmPV2hPfmtkNkAQRNEboZgEWyDsNGk960jaSXIlsKkwbQ9u1SibmPYX868k_zy_5eEDmLJ2mVT4nErcqd2_Lecb9qpc4e8oKPoqKQrGQ_OOs0s6iGK3Koq4Q7QJi6y4S1SQ-UDSTTX_MXDWMDnv54zNChGrPbSEsea3MbwzIMnjqyYn0pKPxzubcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
#رسمیییییی
؛ زین‌الدین زیدان تا سال ۲۰۳۰ سرمربی تیم‌ملی فرانسه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/102130" target="_blank">📅 12:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102129">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/496ccbf92e.mp4?token=ZI0jhzCxfye7AKF8zcVgoqEbfGSTNisUxQerRi1jIWC4u_IsVGQO_DAfEPSMVrMQvD-70uCExwFM7S4FQi9ax__to90pWVnPyh7M9wD-stb8032QTF1LyxWLTJJPpW9k-1goImJUILFlhfsFct0LQ-_Sl5gkcgp3b0TR2YiDVSjQO2E2Tga1V8SBo3WEB95H7yDBY3PSUa9TSZUsIZXKSLA_azZISy9FIIF59kdu6KyawEDOPF_qZm7cmHNmHvSuHsYJ6DkxKR-TQRmh_W5uVKUu9pWeSOSFc2ZEvb9dC_CkxQdi-aaogeoNeLqrX-FyDK_QK_Q_jucthF_R4-JGmLeQh6J9Q6mzQNptqYL7tskSdlwNNokx5KEzo-V3kRTnIITXoFBEkHpPK1lmSUFRKxGbsgWb11JeHkuN_WObFLVfiXhnsjLKVRbGoBABDzzzOf6jmwLQlxFdEOs3QGijP5r3M26fkaEg9ivJZGxp7DFn5LqYwdRRqriV4LJUZ5C0bULwGu4XeGOtdKQuLqsbhZ_kyWrdpyuFxoaUbC3gtxQG23htifrgWRAGLk8zkzyu_PHBQOqycSxESSFpVD3l_fHRCyJ9EZgDtDtiy7GFGAb3HNts_W9UPDwleFFd4MGI2MsT4VllLWSgHWCl1JbRXjEesR_Kxiq-XNVvYD1l7qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/496ccbf92e.mp4?token=ZI0jhzCxfye7AKF8zcVgoqEbfGSTNisUxQerRi1jIWC4u_IsVGQO_DAfEPSMVrMQvD-70uCExwFM7S4FQi9ax__to90pWVnPyh7M9wD-stb8032QTF1LyxWLTJJPpW9k-1goImJUILFlhfsFct0LQ-_Sl5gkcgp3b0TR2YiDVSjQO2E2Tga1V8SBo3WEB95H7yDBY3PSUa9TSZUsIZXKSLA_azZISy9FIIF59kdu6KyawEDOPF_qZm7cmHNmHvSuHsYJ6DkxKR-TQRmh_W5uVKUu9pWeSOSFc2ZEvb9dC_CkxQdi-aaogeoNeLqrX-FyDK_QK_Q_jucthF_R4-JGmLeQh6J9Q6mzQNptqYL7tskSdlwNNokx5KEzo-V3kRTnIITXoFBEkHpPK1lmSUFRKxGbsgWb11JeHkuN_WObFLVfiXhnsjLKVRbGoBABDzzzOf6jmwLQlxFdEOs3QGijP5r3M26fkaEg9ivJZGxp7DFn5LqYwdRRqriV4LJUZ5C0bULwGu4XeGOtdKQuLqsbhZ_kyWrdpyuFxoaUbC3gtxQG23htifrgWRAGLk8zkzyu_PHBQOqycSxESSFpVD3l_fHRCyJ9EZgDtDtiy7GFGAb3HNts_W9UPDwleFFd4MGI2MsT4VllLWSgHWCl1JbRXjEesR_Kxiq-XNVvYD1l7qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🎙
رئیس مرکز ورزش و تربیت بدنی دانشگاه ازاد: علیرضا بیرانوند سال پیش فارغ‌التحصیل شده و الان دانشجوی دکتری نیست
+سربازی در کمین است؟
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/102129" target="_blank">📅 12:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102128">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxX90uO7T6MshIvu7FOR3gU-ovvc0yVVPM32mteDbyVundhx44bvYPchc5PCZ9yEm-sjn0IVEsPVOabRfCnaqGsSNNJVNSNrUoyiijWyn_QqIYPM1V3s_HxcvivH4avCkZLcedJ8u0-RrZpVOH_XqssHBDXOrl0ZGA4XPf-lYTDqyq9VFEnBAZQL8xJDY8DZ-gWbQTm2vtx9wsphjgJaoeTib4Z891QODX3FybZ4bpTS67iWFaxOiDPHBQOug9jR0KY9eabC_0FK-EIU9BP-FlcZsGNPvASxr056xh7nfISccQz6AMuwt_ywrd3zl6KS94TTFqt0jpBXMxaotcK81A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بازی دوستانه|ترکیب تیم‌فوتبال چلسی مقابل وسترن‌سیدنی استرالیا؛ ساعت ۱۳:۱۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/102128" target="_blank">📅 12:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102127">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04499b20cd.mp4?token=Th0LdFgnXKGiTfZZAd45W2uQHt49Z7J5X06GU9vaGM3mfmaPYb08NbuEpCC5fC0bQdojW-kHsqYN5ZaUrGy-w4VGmrmupfQ2TBZus-T9SQcLzkdhoMjBx_VZWSjwFV_EViDdnVcwDFInUaBkyY8-ellfoU4HSKnW1lxtIVuZ5ia-WbMuRfDs2o1iV66qklpsbwHtf4LRxiIYbEOK9gCCO__MA4BhJ5hmyIKZu5aIqS9VRPUXglrF7YcbkosgrJEt5KhnDvPNg5Xc_Mb7j5B1hfMOAlWC-03mxz3i2_ZyiOfRgulJaTM2IbuSBI4xQm2oye4XjF_2gA2Nyjw2FcYxPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04499b20cd.mp4?token=Th0LdFgnXKGiTfZZAd45W2uQHt49Z7J5X06GU9vaGM3mfmaPYb08NbuEpCC5fC0bQdojW-kHsqYN5ZaUrGy-w4VGmrmupfQ2TBZus-T9SQcLzkdhoMjBx_VZWSjwFV_EViDdnVcwDFInUaBkyY8-ellfoU4HSKnW1lxtIVuZ5ia-WbMuRfDs2o1iV66qklpsbwHtf4LRxiIYbEOK9gCCO__MA4BhJ5hmyIKZu5aIqS9VRPUXglrF7YcbkosgrJEt5KhnDvPNg5Xc_Mb7j5B1hfMOAlWC-03mxz3i2_ZyiOfRgulJaTM2IbuSBI4xQm2oye4XjF_2gA2Nyjw2FcYxPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
خلاصه که نگاه کردن زیاد آخر و عاقبت نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/102127" target="_blank">📅 12:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102126">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-X8xnqfWVgskM_qz3Y2Aa8OBr8WvYO08UIh3iSXXufuZUOui9wB0Ug2bkiehnMcorCEaP8oAzolDJ0pF9iS_m2-HJaT3sSmeefKtsfIpqg77dXFkw60aajQLxV7lS3NXQkPJTPuiLACzW7cHMcxzdBXEuKzY1BUWB0vZm1JBtXNHjMNc2ugXEWCQZPxQVv4OltlGGscGNKpc29VuzntQ6AQOJuzXknxq9gZ3MwOEvcdbs-fwPJeLbn30sDWwhuzYyLiaB-GPjAez9ZsWeGTmwnaddNs7czckZyakBUdhl2_JwaHIxhT34D91VW7AeZZSteS8YJKgbr6LkxKOtGbDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
‼️
آپدیت جدید و عجیب اینستاگرام که شدیدا مخصوص ایرانی‌هاست..
شما میتونین در قسمت «یادبود» اینستاگرام یک نفر رو مشخص کنین که بتونه بعد مرگتون در پیجتون فعالیت کنه، و توی بیوی پیجتون هم میزنه «صفحه یادبود»..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/102126" target="_blank">📅 12:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102125">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKGmlC5OyxO4AcjgRs_1YZ376tJwB8okr8aqyE5Qa33nOGBPTt0iyl5a8UjfDCDyoS4vJdDAq0WloGKjut3NSctXAncXOfsVpaDtgEXSy8gwgKqzXChYd6r5TkrrMlUAaNOCbtPHwZj29L67ors--6ACZh60kMETMMPpRJceT6Niu_CuVFWouWrzFQGQLqr66sXTk4Vwx9yD4gIHSNGEdEp7IhI668Vp9l3nPiQB2QiQqg74avcSeGMKPL96Gcwp800fRbgJ54sWsfGw4KHzaSIgku4rHgy6XEMzK0_pKqk23JAz1n7iM1r2uyW6VQm4gPb5DHn8vITxQX8Dm2JHaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشماتون بریزه که یامال تا الان که 19 سالش شده با همه اینا یه دور تو رابطه بوده
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/102125" target="_blank">📅 11:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102124">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/07378b8b26.mp4?token=Zyt-3n0eKjurPmaLJtMiTRtyyuOjiH77Qpv2eWvKVUnmX8127hM_My4U979SywY-Zg4N-vhstV5cLzVBCqn_FASW7DmQHQV_TWxGsz0z93g0DbO0mHn4bwFBkg__z4kcZdHSDIal7HUfZwkKk2EoVqQcM-Zxh5wYSIcj1a8FjDx1cheyDTfpybYQwr2ZIubK3HxitA8eOOtdA4-ttN7ZRdI5GQ13l80XC-vrmVY7GqKM0DUVUUmhyJzmU4xVSW79d1YSlTSIoq4LCy3uaAsVjvsFKan1vhO0OBj1xtORXIpHjhLrLWgGZfix8hdfmlG-zjOrRxyDpwmHpPXqoBv4sA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/07378b8b26.mp4?token=Zyt-3n0eKjurPmaLJtMiTRtyyuOjiH77Qpv2eWvKVUnmX8127hM_My4U979SywY-Zg4N-vhstV5cLzVBCqn_FASW7DmQHQV_TWxGsz0z93g0DbO0mHn4bwFBkg__z4kcZdHSDIal7HUfZwkKk2EoVqQcM-Zxh5wYSIcj1a8FjDx1cheyDTfpybYQwr2ZIubK3HxitA8eOOtdA4-ttN7ZRdI5GQ13l80XC-vrmVY7GqKM0DUVUUmhyJzmU4xVSW79d1YSlTSIoq4LCy3uaAsVjvsFKan1vhO0OBj1xtORXIpHjhLrLWgGZfix8hdfmlG-zjOrRxyDpwmHpPXqoBv4sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو با کیلومتر ها اختلاف آندرریتد ترین ویدیو سم تاریخ فوتبال ایرانه
دعوای علیرضا منصوریان و فیروز کریمی در یک قاب ، منصوریان میگه فیروز کریمی داره بهم فحش میده یهو فیروز کریمی از اون طرف داد میزنه :«گه میخوره»
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/102124" target="_blank">📅 11:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102123">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeee92fd86.mp4?token=mp95XPR_ahKJ9gZ9r4e5ELCid6cT6k-5lMgWC8knhFOxS-EBKVb4ZAfN7fa_iPMorrawEZEPr7eSmgeCzPYzkeqQPIKxC93paomEsmtMeZ-vWpUdR-ljNJHc9lJWSO8jXeIS-zcLv9ODlzBwP11EoujtWm8f7Zw8BwRWQ4jKBf2K0Oc32XK9JAT5fTOGB02o7rdHWf1MXbW0a0VoBiANssdWMT4YZbuM-tBnYcT2sHVEv6NQsqBHbGJ3C8H-oppNUOn-0FASjinOJCbRNS96u09fchXHb-M0ii-RLiiARkMEJMv8BUh07dYAKV6i2AWS6MIVB0zBRb6-UPsoqjkv1B7X2q4T24MyhWDiWtFze9GYnArArbLgJzGWkCYZzJEUF042N3v8QOuykIdxcxxOtr6fUg-Xh807He2FjtFFOgKsUOz7hXNe7hqjItrri3u820Xak6tqzaDoB_ueTIoFxDoxUNIQ_8hkUFHsYrCVH4EMKpYd5t7W2T8X4a0u3j0SlTrqjhCC9q3ZhmRe8u6RPfrbx_eOlivdTTrriVrhJ2PB7XyrTGN4hZRNMDTRU5Mb1p8C-Qgp-1hfnHIlpbKD6BeoNnMHXKGRQhUWCZ2yxO7ompbaHhmiMk1tE7vuD3Xoj3aVnNyxcAh68FUldwRfdL2F7E6o_y0rKxCouZHKLWU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeee92fd86.mp4?token=mp95XPR_ahKJ9gZ9r4e5ELCid6cT6k-5lMgWC8knhFOxS-EBKVb4ZAfN7fa_iPMorrawEZEPr7eSmgeCzPYzkeqQPIKxC93paomEsmtMeZ-vWpUdR-ljNJHc9lJWSO8jXeIS-zcLv9ODlzBwP11EoujtWm8f7Zw8BwRWQ4jKBf2K0Oc32XK9JAT5fTOGB02o7rdHWf1MXbW0a0VoBiANssdWMT4YZbuM-tBnYcT2sHVEv6NQsqBHbGJ3C8H-oppNUOn-0FASjinOJCbRNS96u09fchXHb-M0ii-RLiiARkMEJMv8BUh07dYAKV6i2AWS6MIVB0zBRb6-UPsoqjkv1B7X2q4T24MyhWDiWtFze9GYnArArbLgJzGWkCYZzJEUF042N3v8QOuykIdxcxxOtr6fUg-Xh807He2FjtFFOgKsUOz7hXNe7hqjItrri3u820Xak6tqzaDoB_ueTIoFxDoxUNIQ_8hkUFHsYrCVH4EMKpYd5t7W2T8X4a0u3j0SlTrqjhCC9q3ZhmRe8u6RPfrbx_eOlivdTTrriVrhJ2PB7XyrTGN4hZRNMDTRU5Mb1p8C-Qgp-1hfnHIlpbKD6BeoNnMHXKGRQhUWCZ2yxO7ompbaHhmiMk1tE7vuD3Xoj3aVnNyxcAh68FUldwRfdL2F7E6o_y0rKxCouZHKLWU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔵
نوستالژی خاطره‌انگیز از دربی دلامادونینا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/102123" target="_blank">📅 11:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102122">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7aafdb5637.mp4?token=WZrIMPGD7w6GIRtTmvX5o1OYNsMEPEZ1NJJ5dQ9w36-btM_DcHNZ1cpMielkyZKeo83J9_QW1XSN6NPcoTU3HLFxl4MEZfotZ7cbHlkW0_UFrO3SLoS_auDMb8qngJn3sh09Zrq6emBpoWfmPZj7VWMZqnMbeImgtG-EGY9r5EfKGH4mFXU7JWaVyKO5zb1B78ozJtuYo9fA0qIfqCZhM3C3gvBb79r0Y171ZYYxy38WMGHqIAr1vWV2Khk0eaJITdYSejMG13SoUEcSKkNOCkYXzVL4WmuOBRhz04uQiue_wQRzX6OaAL12Bgt1mStFCgZmbzmLuxZ-aspwcd9a9oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7aafdb5637.mp4?token=WZrIMPGD7w6GIRtTmvX5o1OYNsMEPEZ1NJJ5dQ9w36-btM_DcHNZ1cpMielkyZKeo83J9_QW1XSN6NPcoTU3HLFxl4MEZfotZ7cbHlkW0_UFrO3SLoS_auDMb8qngJn3sh09Zrq6emBpoWfmPZj7VWMZqnMbeImgtG-EGY9r5EfKGH4mFXU7JWaVyKO5zb1B78ozJtuYo9fA0qIfqCZhM3C3gvBb79r0Y171ZYYxy38WMGHqIAr1vWV2Khk0eaJITdYSejMG13SoUEcSKkNOCkYXzVL4WmuOBRhz04uQiue_wQRzX6OaAL12Bgt1mStFCgZmbzmLuxZ-aspwcd9a9oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
۱۰ گل خوشکل زده شده از مدافعین فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/102122" target="_blank">📅 11:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102121">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd7bc32139.mp4?token=usPwbeBJAJpl98QpXz5Ww80jG5pEIjd46LVcLWc9AxfF5f1ZbwV2DatN-3dCJNwc5j61Y-K0a45HE5hfw42RB7WR1Lk8iXtCNRzD8ZP2WlF0_-9LhPk67jwjQpLpXUyersjbiMsp7clrTd8Ha4pK96ur3pUxFtA0f7coFhWuJyNAuKvzQv8sL27GWR2mF4bIw9y6jXmrpMOCFleYmCNdOtHQqcNfyns9z4gnU_Hfk4lNwk9yeRkTmX52PBVEL99_q3za0Y2-W74_8Ce3uOg91jVWRFTqsqbFj9X-RELv1c3lfy5yFrNQiJjZGM-4brSpPLdA3d7cEaEq8gE-AuQfPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd7bc32139.mp4?token=usPwbeBJAJpl98QpXz5Ww80jG5pEIjd46LVcLWc9AxfF5f1ZbwV2DatN-3dCJNwc5j61Y-K0a45HE5hfw42RB7WR1Lk8iXtCNRzD8ZP2WlF0_-9LhPk67jwjQpLpXUyersjbiMsp7clrTd8Ha4pK96ur3pUxFtA0f7coFhWuJyNAuKvzQv8sL27GWR2mF4bIw9y6jXmrpMOCFleYmCNdOtHQqcNfyns9z4gnU_Hfk4lNwk9yeRkTmX52PBVEL99_q3za0Y2-W74_8Ce3uOg91jVWRFTqsqbFj9X-RELv1c3lfy5yFrNQiJjZGM-4brSpPLdA3d7cEaEq8gE-AuQfPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
خوشحالی‌گل‌های عجیب در لیگ‌های‌فوتبال ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/102121" target="_blank">📅 10:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102120">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">▶️
رضا نوروزی؛ یک فصل طوفانی، یک عمر سکوت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/102120" target="_blank">📅 10:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102119">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krmyyWtDOz7K2ain209BM225RtRZK_pNlD8-RpV-yAMcIZpO05KPwuFB7Cy0mqysmhrXPZYuoUsonlKmGql5ud006Bz4zsg6kobs_DEVO1jA1xB5Tgqrub-hbrczF3njuG-TPX-6VPtyBq8Iekd4oFaGneThvR3PZaG309sisx7_5cF3FHNeL0P_t1gOU8eKrOjpK3sYUjRtjflrLP_uGXFiVQCGmdtgcmkEIH9IA2me8xt1QSoqR-THE0xhidzh-zu9g0rDzI--qy62GbxyCVl4at1gNKCxEBNgWyy6MMmjqf1h-D4ttRzYI0fMfVCMce9afuXbeLkwcRzEgwSIpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
😟
اینتر میلان به توافقی با تاتنهام برای جذب کریستین رومرو به مبلغ تقریبی 40 میلیون یورو رسیده است.
✅
⭕️
🇪🇸
اما این بازیکن منتظر بارسلونا است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/102119" target="_blank">📅 10:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102118">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad2348e726.mp4?token=J44Z_q51vcX-qJvFRCHwiUJ6mtYqzqiVMxGUz949h9BDomRby5DLCPN5XFI3hMwcz8BhFO5mVem1UpgNkAXd28AYX49AFmKNsrozzdyr1hwje7Swsu9SvNlh-wL377ftyJcQMfaRMjyaCQiNnlHEEpPZCYeNNEAOu-2A7-lIgizLAJrm8W7pEpcHhx8-A7YzJqAhUptlkyh_Lcnydf5hzenljkqvOKPmH_ZZbeUm_pDzWQfSPfEuEKs9FvtEzhXgtWld3E6xF_RQM_TpsKjliYz5pwiTeFwq7iwNTvpjHKBRQxonvNHMSz9lDspYtZRWCE_4wCR9R-nFzRzM3L7zqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad2348e726.mp4?token=J44Z_q51vcX-qJvFRCHwiUJ6mtYqzqiVMxGUz949h9BDomRby5DLCPN5XFI3hMwcz8BhFO5mVem1UpgNkAXd28AYX49AFmKNsrozzdyr1hwje7Swsu9SvNlh-wL377ftyJcQMfaRMjyaCQiNnlHEEpPZCYeNNEAOu-2A7-lIgizLAJrm8W7pEpcHhx8-A7YzJqAhUptlkyh_Lcnydf5hzenljkqvOKPmH_ZZbeUm_pDzWQfSPfEuEKs9FvtEzhXgtWld3E6xF_RQM_TpsKjliYz5pwiTeFwq7iwNTvpjHKBRQxonvNHMSz9lDspYtZRWCE_4wCR9R-nFzRzM3L7zqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یادی‌کنیم از تقابل نوستالژی نیمار و ریورپلاته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/102118" target="_blank">📅 10:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102117">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3115e0e757.mp4?token=PUR13cSKw4p1bnXaacQ7vsKlcPa71yULQXVoMVqVNPwWkrc9_4BsxYCxZl-6GvmLJZNM4ZcgOQol18x0GVD9aT1kTrMOjHbbTrF5XJqukmMwp5QTzL0yNrwc3SfG8StZM3kMtqaq0tZ9Sm6wpEW7nG4YcWG_Kua-BBG6mN7ywMzdjkodXbB9VNr2UwOmiP1cJ8WvdWv2FlOlZxhI4pwIzL4O-R13IhAIbsCXQdfpJnJdcq5Q_gHjCR1ilRAPi-74ec-Ispr75XF1bkCEi4GVRUnnducRbGzM_RvooDQEyoxA_KRJANK9aCR5ooV7HdMFnU3EZyvobw8Wc7-wLuesDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3115e0e757.mp4?token=PUR13cSKw4p1bnXaacQ7vsKlcPa71yULQXVoMVqVNPwWkrc9_4BsxYCxZl-6GvmLJZNM4ZcgOQol18x0GVD9aT1kTrMOjHbbTrF5XJqukmMwp5QTzL0yNrwc3SfG8StZM3kMtqaq0tZ9Sm6wpEW7nG4YcWG_Kua-BBG6mN7ywMzdjkodXbB9VNr2UwOmiP1cJ8WvdWv2FlOlZxhI4pwIzL4O-R13IhAIbsCXQdfpJnJdcq5Q_gHjCR1ilRAPi-74ec-Ispr75XF1bkCEi4GVRUnnducRbGzM_RvooDQEyoxA_KRJANK9aCR5ooV7HdMFnU3EZyvobw8Wc7-wLuesDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
▶️
این فیلم مربوط به سال ۱۸۹۴ هست و رنگی و اصلاح شده. حتما ببینید واقعا جالبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/102117" target="_blank">📅 09:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102116">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52dd0bc973.mp4?token=bj92_FWcgl_fd5dQoXihTBCSxMAVXRN4-eGE7sd04tNMm4fRExn3F-31__ogymY14QwWhURYKXfwm-5tHCH9R2q_dzTCLedV_267JnbCsXceW7B7065xHHPrwdiQLD2lcTmkuZleLug7ivUsLEHbyKyXmqN5-f19My_zKFKJw1ef51i-X0GR4jVxO0GqEe17Zdd4nDX5WxELv8sHwkL2QR3jZTTV5ZRwil_hXQgk9zxZ_IX27HcYlsXFH9CgmHXsMAEUbDg8ec9k_rjN-2quex8kxWb4oOK12jK1na29p7Iush0IEVyi4MNHRspJzK39i-O6YJqafvn4kQWkrihLFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52dd0bc973.mp4?token=bj92_FWcgl_fd5dQoXihTBCSxMAVXRN4-eGE7sd04tNMm4fRExn3F-31__ogymY14QwWhURYKXfwm-5tHCH9R2q_dzTCLedV_267JnbCsXceW7B7065xHHPrwdiQLD2lcTmkuZleLug7ivUsLEHbyKyXmqN5-f19My_zKFKJw1ef51i-X0GR4jVxO0GqEe17Zdd4nDX5WxELv8sHwkL2QR3jZTTV5ZRwil_hXQgk9zxZ_IX27HcYlsXFH9CgmHXsMAEUbDg8ec9k_rjN-2quex8kxWb4oOK12jK1na29p7Iush0IEVyi4MNHRspJzK39i-O6YJqafvn4kQWkrihLFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ذهنیت برنده بودنه که آدم رو به همه چی میرسونه
🔥
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/102116" target="_blank">📅 09:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102115">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffacd8024c.mp4?token=LLNYilczuRZ4G8MOWZDdYGLrdZoGwzUaY4M_X1lvvP2JTDXG_6N56lFzgS3kxUygueeGDtc1KlbUUx6MWDd_1HasXsK7h7DOv7ChT_GN02FWsDXQBgDMq0fJKxtaQgiLXVJ2AmFqV1I2pcLjoFl4MEwLBh-3XyzwZkCGIUAeKqJBh5XICAwYgmXk5NJGRt9TKif__-34JAgVKkOgHxKC5jGZfNF59ve-cbog8aji6BtlNiEZUybh_r0lyyoWk0Us5KTuNRP3pFgA_JDOoKRYx5N4jTEgayZQD1aNe2Nxy3Zsd2UBKvfyNf2XUeY_0c7efOPxsGildv7MDMaQPNSUKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffacd8024c.mp4?token=LLNYilczuRZ4G8MOWZDdYGLrdZoGwzUaY4M_X1lvvP2JTDXG_6N56lFzgS3kxUygueeGDtc1KlbUUx6MWDd_1HasXsK7h7DOv7ChT_GN02FWsDXQBgDMq0fJKxtaQgiLXVJ2AmFqV1I2pcLjoFl4MEwLBh-3XyzwZkCGIUAeKqJBh5XICAwYgmXk5NJGRt9TKif__-34JAgVKkOgHxKC5jGZfNF59ve-cbog8aji6BtlNiEZUybh_r0lyyoWk0Us5KTuNRP3pFgA_JDOoKRYx5N4jTEgayZQD1aNe2Nxy3Zsd2UBKvfyNf2XUeY_0c7efOPxsGildv7MDMaQPNSUKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مایلی کهن و پروین و کفاشیان در خنده‌بازار
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/102115" target="_blank">📅 09:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102114">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7e0420a2b.mp4?token=fME_CHYD78urNRcBBp5OeGFNiHPmJOgKC7VrOPxNQZG5500odYAO0AOKNRd6RvvFAe8E94NU3nZQY0W2_SUKv7CERAEYgBSkstW-CY3L0uLEvTyWHJKr9HyEy1tgYiS4X3aELpR2VnijqrC0rRIZ5Wjln1vdGVrhkdvX0boGIcc7WA4hoStpn7kpYEY5IAE24pKhud_yhPQV6XUnwkjHaq2VS2xYHdR83icu1i_2SX5A0kPfQ2NKcJAzCQvfaNRo7Oub0odRXW5ZpkQavQ9j6puQmi-NO32JQ8vXBtcOj3TwakRqVacrWdhlKJ-HOmgsV-XTxc5jo4xjL3W9P14QMUeJB8S9_oFL05Q3dPi7Ecmi4zZpZouhWnnXDoeM0HFxPYAxfti7GA59vyAppUJA4PCYCRfA5vI-lK8rvhFgCIAeQ4RWb--nJQScsplXL_tyWVU5Mgce3jXxk8k5Ww1n_0pECBEk0tERLvlTWsVJYoCaDJebChKiVbxQ_0bF0Z1AGSC4o34fDRZ-SNZR2B0homo67avcN3zlLOT4vgEYQkxUJCKYx3LhfYALJVnDBe5fnW1lUYURzYiiDRPeSuR2pTRst9xTnb6DRIA1OgwdXasMxJetCW5vS51KFDRnKEVmYKIKr6gRk8fbkpf1GKvvYY9-I-wL-U8_WfBckiyQWG8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7e0420a2b.mp4?token=fME_CHYD78urNRcBBp5OeGFNiHPmJOgKC7VrOPxNQZG5500odYAO0AOKNRd6RvvFAe8E94NU3nZQY0W2_SUKv7CERAEYgBSkstW-CY3L0uLEvTyWHJKr9HyEy1tgYiS4X3aELpR2VnijqrC0rRIZ5Wjln1vdGVrhkdvX0boGIcc7WA4hoStpn7kpYEY5IAE24pKhud_yhPQV6XUnwkjHaq2VS2xYHdR83icu1i_2SX5A0kPfQ2NKcJAzCQvfaNRo7Oub0odRXW5ZpkQavQ9j6puQmi-NO32JQ8vXBtcOj3TwakRqVacrWdhlKJ-HOmgsV-XTxc5jo4xjL3W9P14QMUeJB8S9_oFL05Q3dPi7Ecmi4zZpZouhWnnXDoeM0HFxPYAxfti7GA59vyAppUJA4PCYCRfA5vI-lK8rvhFgCIAeQ4RWb--nJQScsplXL_tyWVU5Mgce3jXxk8k5Ww1n_0pECBEk0tERLvlTWsVJYoCaDJebChKiVbxQ_0bF0Z1AGSC4o34fDRZ-SNZR2B0homo67avcN3zlLOT4vgEYQkxUJCKYx3LhfYALJVnDBe5fnW1lUYURzYiiDRPeSuR2pTRst9xTnb6DRIA1OgwdXasMxJetCW5vS51KFDRnKEVmYKIKr6gRk8fbkpf1GKvvYY9-I-wL-U8_WfBckiyQWG8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
ویدئویی که صداوسیما جمهوری اسلامی تحت عنوان مستند شوک از پرونده خیابون علیخانی منتشر کرده که ساعاتی‌پیش به سبب اون سه جوون مملکت اعدام شدن!!
+ اتهام‌هایی که به این جوون‌ها زده شده:
- بستن مامورها با طناب به تابلو
- سنگ زدن به مامورها
- آتیش زدن مامورها با بنزین
- روی زمین کشیدن مامورها
-  تیکه تیکه کردن مامورها با چاقو
- فرستادن فیلم از اون لحظه به رسانه‌های معاند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102114" target="_blank">📅 08:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102113">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/508992e992.mp4?token=tMQSiHT3KNdQf2usKYuYbU44bHaWnTIBe-ZCei-mViHOXlx45acu4Mp_ztI4PGHpZPhhQuPoou1LpGddX5t7s8ZxieS8NLPJAStyvoyPGi7OiM-vlkPYvRoHWZjL4QNzIQ3EePzstQVOMwqrv-ThqIvQM6CxeRH-6DzRmU0beFmqU70_lYHENq-vQwBOWKRtK2_yrOXLZwsJnUOkBk11UigJ8UX3Uw1Yr6sef1jJ0x7qymFF9Ua76wb94DobiZgyvHmyFuoTIv_zMjxx02o49jMiz5yl7FIixOkl4RjCg8J-iGOnQwB-c46FssJVhYHJl0-fovFr5NTfSM-j0E1yFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/508992e992.mp4?token=tMQSiHT3KNdQf2usKYuYbU44bHaWnTIBe-ZCei-mViHOXlx45acu4Mp_ztI4PGHpZPhhQuPoou1LpGddX5t7s8ZxieS8NLPJAStyvoyPGi7OiM-vlkPYvRoHWZjL4QNzIQ3EePzstQVOMwqrv-ThqIvQM6CxeRH-6DzRmU0beFmqU70_lYHENq-vQwBOWKRtK2_yrOXLZwsJnUOkBk11UigJ8UX3Uw1Yr6sef1jJ0x7qymFF9Ua76wb94DobiZgyvHmyFuoTIv_zMjxx02o49jMiz5yl7FIixOkl4RjCg8J-iGOnQwB-c46FssJVhYHJl0-fovFr5NTfSM-j0E1yFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپیده دمید، اما روشنی نیاورد؛ گویی خودِ آسمان هم داغدار بود.. صبح آمد، اما هیچ‌کس از آمدنش شاد نشد؛ انگار خودِ سحر هم به سوگ نشسته بود.. ای صبحِ غم، مخند که امشب هزار شمع، در ماتمِ عزیزانِ خود اشکبار شدند...
⚽️
@Futball180TV
| Quf</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102113" target="_blank">📅 06:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102112">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKgKfgjjf72kUuTdiL2qkES6Vo6NsJghQZ_UqxpWzqAfIKa9gMv9bnz4SMwr5mdPorlquVrxEgEP9C0TNkBz4BSW3hWkS01bfVRtpQFWtipFOD0GezoMKgCsf3dSRFbQwnn2JnuPsrEh_hQAZ-4pavRWJ0h35lQ5p-hCDj43_i8BnQzKbnCWSDT_ZbUXsLJPBpkutcACWBSz1zUp-WeZ6NbD5NQz8SgXiCGfL3m3RiZiiPgGezMXfpph8yJPF10JLlCqs1LH0XkeXD8kTfBcK1mTwRXYOI6jrY3jQAnbxOxQTvXi_ieAK8u4uqVuPNHGQcc5PskquYhuZ0BkuVk26g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
#فوووووری
از رومانو: پرز مجوز مذاکره و عقد قرارداد با رودری رو تا امروز صادر نکرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/102112" target="_blank">📅 02:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102111">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N02JxZEPcBmz5_mtfLPLOTZ4_45hzww0zn0_V01eBrLW0_zdNxPpK_T9aOuhdI8ausEe2cYt9EeE13AUCi0RHN_GX8rr_jaO2SF1qOqwFmWs1WbpBOOX0HCVoFn7h0wmcPw6iw4BLYuIxTBqsqvBYl0IZBeU7gAmq8rzG1mo9gTz3tIMZPsj-xBS_a-ue9m3EcW5e1guLdo51nFDg6mvN0GdMZhk8C9Rg0EBknhQ2JlQnHy012Sx4buUlvyOCGEldUGTTx6OJwR7exJfV3SNEC7o2oBPFHJZV-uMdD_PjMpBhqtLwcC0pGZx5naryTPV2LWlaz4UpIMsyxT08vCuig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇹
افشاگری پائولو مالدینی از وضعیت وخیم فوتبال ایتالیا و دلایل استعفایش:
یکی از بزرگترین اشتباهاتم این بود که اصلاً این سمت را قبول کردم. سطح فوتبال ایتالیا به این حد سقوط کرده است، و دلیل آن فدراسیون است!
وقتی منصوب شدیم، فهرستی از سه نامزد برای تصدی سمت سرمربی تیم‌ملی تهیه کردیم. پپ گواردیولا بدون شک گزینه اول ما بود، در حالی که آندره‌آ پی‌رلو گزینه سوم ما بود.
ما مذاکرات خوبی با پپ داشتیم و به توافقی با او رسیدیم. با این حال، وقتی به فدراسیون اطلاع دادیم که به توافق رسیده‌ایم، به ما گفتند که نمی‌توانند هزینه دستمزد او را بپردازند و گفتند که باید گزینه‌ای ارزان‌تر پیدا کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/102111" target="_blank">📅 01:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102110">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c83412a5e5.mp4?token=CQCB61MtC2nAzGKWMNF9ajYK_pyaTyh9WFIGr6aENZtL-Tk3aX7c43GqmJAe6f9B3mPn8Nq23rC-NFr9D0KJTNgVsoNecl12-yZaDVuA-8RkFXKcSFmsWjVmVDxHBabAH_uBgUEdXctd4mVJcHorjkcb_aIKi_xBtzC96mHX2ySVZDLQnIcdMiECv9GHvEhVfrq8hLX-Z6DLbKal0_BZ1O7Zoeq7DaMuSwYMAqG-kIExqIsLTnAEJzw_xg0plMklTz3BhVWgn_Sbaj-0F6HKc6w9F6XLXNkLVduX59PP68WEgz1LvyISJoawUNp9CHSykf8lcMMhEVs-EpPc3IyAQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c83412a5e5.mp4?token=CQCB61MtC2nAzGKWMNF9ajYK_pyaTyh9WFIGr6aENZtL-Tk3aX7c43GqmJAe6f9B3mPn8Nq23rC-NFr9D0KJTNgVsoNecl12-yZaDVuA-8RkFXKcSFmsWjVmVDxHBabAH_uBgUEdXctd4mVJcHorjkcb_aIKi_xBtzC96mHX2ySVZDLQnIcdMiECv9GHvEhVfrq8hLX-Z6DLbKal0_BZ1O7Zoeq7DaMuSwYMAqG-kIExqIsLTnAEJzw_xg0plMklTz3BhVWgn_Sbaj-0F6HKc6w9F6XLXNkLVduX59PP68WEgz1LvyISJoawUNp9CHSykf8lcMMhEVs-EpPc3IyAQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
✨
روزی روزگاری ایوان زایتسف بزرگ و افسانه ای در خط سرویس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102110" target="_blank">📅 01:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102109">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ybq1YgKOGHULljLy9Qek0vILtHE98QARS4DjLwh7gm0cwh7q9jw7zKTiqanvTIKyIcQgg4z6NC_1YVcsXAZb8LaUPfjaG9WhaLewRFyClATUp46DUbghb8w9LJgB721redL5mX1JnH-E3nEt4mBxWw_XZ1rb_tRx-CX_GPz0AiQbNW0NQHaYyIsKz1EtAlfjbu2deCzbvGoeYYhvEc_SYUy240SHK5kLoeWk4yaSMjS_cFrE-mC7cBts-kVQ9zoWCzbDom4o0J1z1HCxEN0RMi2zzAymLW8E6oou4skMt6hF4ZYDz1dl2AhCgUoO_5MYfFazCKIeVCTVKtSCtz4k-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
‼️
لیست گران‌قیمت‌ترین نقل‌وانتقالات تاریخ که ۵ موردش مربوط به امسال هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102109" target="_blank">📅 01:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102108">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uox_YV19fAFDhI2049w9ibmGW1jnmNoY8ZivgNdSZ-sXojkWYFd7yXNc3vqm81j6b3-nSp4E4HrCQU_ORkuGVulZEbtrzJuMAEoOlpJEwXGlx600LZ0MLM2ZSQetoSylTD6VyjTJcaYGDgcWlccFN8locHJlgMTW353vavOeFwjLRWujwYaExtEPA3Fex1lz9dzMCLavy6Ut8vDbXbb9YjhJIINkDoKmIj8kulKypQXcniMe-DpLQhzPWHPUSbX9v7My60ZZfUaTBdJvsjca0dwhboMALIIO3Qliih8ZG6vFU4hTVv8vG1a9OWBEg68vsJf7toiK9nbFwAANUf7CFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پینی زهاوی ایجنت لواندوفسکی:
لوا برای اینکه بتونه برای بارسا بازی کنه قید 200 میلیون یورو رو زد، اون پیشنهاد سالانه 100 میلیون یورویی از عربستان داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102108" target="_blank">📅 01:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102107">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=JmQVm31Mn6nNGGASoVcxjRhtLdy6w8G2zd0zQVJPxvMYy9EMKPybxQd8FFDcxd0406tkCp_qya0yKLJHOCVYSXfSkxkkec92aTA-ndga5iEoITJCSL99oOeNj6trQk7Cy3RhLTWe0T4IIQiOZ7Oek5hGKfgMO7WAvHfVvSDHKstNfRguupfQWAzzJr_373ubvN-kdYBSIykTPopM53KPeONeGbe7xWvhwNSClHLkJBc-4a9TulkrL7or7LNtx-uC2wwoEBjJafMXEL3kqAOLWCL72K83TekmkOg_7l43N4AXScu_7EZPKYpqdPQ3LAVb8BNkSlhyMDhX6s5Uf8W5sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=JmQVm31Mn6nNGGASoVcxjRhtLdy6w8G2zd0zQVJPxvMYy9EMKPybxQd8FFDcxd0406tkCp_qya0yKLJHOCVYSXfSkxkkec92aTA-ndga5iEoITJCSL99oOeNj6trQk7Cy3RhLTWe0T4IIQiOZ7Oek5hGKfgMO7WAvHfVvSDHKstNfRguupfQWAzzJr_373ubvN-kdYBSIykTPopM53KPeONeGbe7xWvhwNSClHLkJBc-4a9TulkrL7or7LNtx-uC2wwoEBjJafMXEL3kqAOLWCL72K83TekmkOg_7l43N4AXScu_7EZPKYpqdPQ3LAVb8BNkSlhyMDhX6s5Uf8W5sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از آمار تا پیش‌بینی
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102107" target="_blank">📅 01:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102106">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQ5PHv0NJ8x-JaOtIAdjT9RSDzY7WNb77cBAF1dMjyETgfYC92feMGQpOxMS_lXKYsihec4QaRvJ-TkWyu_UcZFhm0sadnayH9115ncPDhohaVoCuxxliutGvWtDfdS0G6b9zknSY-WroGjNEOmvUPDQfzYb6qQLQ_rV43PJbSFAXKMv77CEauwv0jf1dX8fCfmRCMtlLeFH-XEX0GPKF2CFGuJKHx5CdKziXXYvr_wa6tl5JjwdP_D8h4uwd7Y8-POrPXyLyezcVFbhHUZOkbyEepypdHhrDzjUq8QQronXn1wVWRCzL-fLXuiUYfFstB7XtAmjoZVnWKYdPn3l_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🤍
🏴󠁧󠁢󠁥󠁮󠁧󠁿
فلوریان‌پلتنبرگ: رئال‌مادرید از علاقه آرسنال به وینیسیوس مطلع شده و اولین پیشنهاد رسمی خودش برای تمدید قرارداد رو تقدیم ستاره برزیلی خودش کرده. از طرفی آرسنال هم آماده ارائه اولین پیشنهاد خودش به رئال برای جذب وینیسیوس هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102106" target="_blank">📅 00:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102105">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvvtkGU0_NXASOWuTkYJIuuD0qA64xd6-Go08A6GmGpUtL_RLEn9Bec8IUtSVSCNUz9iTZdldWzGZzwqdoWV25jcZj0eko70uKXz4khNfLs3wgovEp1Yqc_J7Tt4Bp9uCngUii5QiJY5yOVseL6WDUDRTPnyaKC8WN9f6hnIcS0L3c3vyPX2KlybTnO9uxzNqpdc9ims-jG9QiOgBNBp_QEUzIrgraFgrMjyn1OYZyWTKVvAjIlHiQD5QsgkOSNE4qVoCAH_53UIaKe6BAAK_mNtIIQl-qbX1PM9jfEPhL5cGrwKMLvgXPj4L2pgtqzt3HMrnuE4lqC63usrrYKIDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
رومانو: باشگاه چلسی موفق به توافق شخصی با جردن هندرسون و دنی‌ولبک شده و بزودی باید شاهد عقد قرارداد با این دو بازیکن باتجربه باشیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102105" target="_blank">📅 00:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102104">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CHsMGu-BDLirHCGNBhJWcPLF2TQ_QYd3JR0Kx8bRKRve_NlkWq_22wnrR-9Hd-9ek6LMgfDhUZCsFfsv9HSyIyZHbj38Jf6UdADa_dzvrgemF9GFpVPQ15vVQPzeYAsN7lksBmmRoY3e7iByk5vS9S_r9Alau4zi6OWK7XHzVtrsBKjdpiVRK7HeGnhQPoVJKZWVocgoDtRoGk0_d5BH_wt5MGPQAyxb7hdG5w7CtB54L9bbUc8ISpWH6c7ecZqDB6ep0g0JK4hp6a_LfbFGAVelluEQXMjUDIRoB9H2S9ptaogy7Cn32lYpfwFlyEnqyQ0PsBb8XHQ1GYvLT9pBuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇩🇪
فلوریان پلتنبرگ: هیچ توافقی تا این لحظه بین رئال‌مادرید و لایپزیگ درباره دیومانده صورت نگرفته اما مذاکرات به صورت فشرده از فردا ادامه پیدا میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102104" target="_blank">📅 00:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102103">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFQKwf0uF94f8BBXeH1L2g2iyl8xPKQYn77uLysDb6a5XCCQlFV2XUeqqwQc_aqmPC50iKC7LggCdujJj1nqu7aBvYfo1H9mAeZ_PZzx6AmHodZ2t93uS9j_6NZeiunxB8jVqDpVto5BzQGkaRtX6IqID2umHOQJd02dqNtZm5cTfUbqOShIDILLS9PqXonpc_imtDykQ5eZX3KcGbKFN-YGbE4fFjLX2kghyeR7MzpJ_13v21mzsyUHZMsF0uS7bfMcaPnlb1VjjLcBaQnwYyjfr7kM02o7a2iwqRQ2U9WplxkHGGDEh4P2WUm8AivnO8f5DAIAvM3UmP6GsC2ZDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⚽️
مارکا: مورینیو درحال تلاش برای قانع کردن گونزالو گارسیا برای موندن در رئاله. مورینیو به این بازیکن قول داده که با وجود امباپه،‌ دقایق بازی مناسبی بهش میرسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102103" target="_blank">📅 00:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102102">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1pBgSJc-uJ-Gd65vg0tlWcvXcHeLlaA2WItRT6_5ASqnmpNjPs68k2z60zuJ9v-CQdpWhH60SoOf0awZMDQyhk7v0j1t8y6AO3HaZpn6Fd_4vBH7kTfhNbHUe33CvsxBroCKNlsBh9r7vZjmU9j8I6qb623djEvxajbC_hxhBv1HrwT7YVuzrwaPn5rXGKVbOl3N4nU7yPumY1Y-MK_qOGuiPVRICyzEAtEpQB16FUr2OoX3pNvoLwOMRdPVo9Esp9bqxF1QfmqHp4xBqkoZCeVdvINKm2fwcE47QinbVAw8dWIw_50WCIy2VDmJKG27dmm_8f7xChyruiouJ0cKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
✅
لباس سوم فصل‌آینده رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102102" target="_blank">📅 00:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102101">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52dfeed19b.mp4?token=OSbmreKVuYIq341Bi_KdNRIt1afzru83MHVJFys9njlTfai6s9a0pqnOAiBY4Jdv73tiXy8bnil-9UUZsTyxncKeQqAc13g4Ef0r0A8BFvcx0-eYbSKMl8LxeVNv165wckmn79Wa_zO7FhbUuHkpSUaNq8dU_59wyO7tNox_ybXf-B3ZS9L1dq_V4kO-7ARrTB42GZxZtn6JnV2SyTzA1muZOOEVc3onPhXKxZv4fjfaH3bFMUpLaoY7O9j3lqYNKVCu-IW17HmC6g2du__03p1naux3wL8V3Qsmn03BSuCoa-Y4BdumQsE6uC0CQEiDpGjXwW3w6MC-z6ZKYpF-0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52dfeed19b.mp4?token=OSbmreKVuYIq341Bi_KdNRIt1afzru83MHVJFys9njlTfai6s9a0pqnOAiBY4Jdv73tiXy8bnil-9UUZsTyxncKeQqAc13g4Ef0r0A8BFvcx0-eYbSKMl8LxeVNv165wckmn79Wa_zO7FhbUuHkpSUaNq8dU_59wyO7tNox_ybXf-B3ZS9L1dq_V4kO-7ARrTB42GZxZtn6JnV2SyTzA1muZOOEVc3onPhXKxZv4fjfaH3bFMUpLaoY7O9j3lqYNKVCu-IW17HmC6g2du__03p1naux3wL8V3Qsmn03BSuCoa-Y4BdumQsE6uC0CQEiDpGjXwW3w6MC-z6ZKYpF-0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو تموم فینال هایی که بود
میرفت تو نسخه (پرایم) خودش
و تو اون نسخه دو تا وینسیوس و یامال رو میخورد.
شاید یکی از دلایل نتیجه نگرفتن آرژانتین مقابل اسپانیا هم نبود آنخل دیماریا بود..
🥃
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102101" target="_blank">📅 00:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102100">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f39b79d0a.mp4?token=J7qlKtS6GAwiirgo-nMbE8PIO2VszLFWNyIHRc1kML4-X3qCEd2zMD_c6YLnqz0oWZVSq3ugEGQFD4p-8dzjOGFLYX9by8s6bbrU4FTQrK0TlIuAyS8aiEgcpjrOXoaFVCkgdCu62dbTwedZ32Pwk_3sB25YddAJZu-JRucrIImzvs_nWJTRYDSnPv9OY6Use6Mvu9wkZtQKgB8G2sEDIJXzLPTJT4rm-o3DiqC5GcUGVJ_dJz79AREa3FEgTmpozUYMyNutKfH5I9ppWB8JOVSo6T49ZIZEIhISpgU3RVYqPIQ2D3kkAVK5xZsLMLh17NIiMYA9lC27z0fZNEE_rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f39b79d0a.mp4?token=J7qlKtS6GAwiirgo-nMbE8PIO2VszLFWNyIHRc1kML4-X3qCEd2zMD_c6YLnqz0oWZVSq3ugEGQFD4p-8dzjOGFLYX9by8s6bbrU4FTQrK0TlIuAyS8aiEgcpjrOXoaFVCkgdCu62dbTwedZ32Pwk_3sB25YddAJZu-JRucrIImzvs_nWJTRYDSnPv9OY6Use6Mvu9wkZtQKgB8G2sEDIJXzLPTJT4rm-o3DiqC5GcUGVJ_dJz79AREa3FEgTmpozUYMyNutKfH5I9ppWB8JOVSo6T49ZIZEIhISpgU3RVYqPIQ2D3kkAVK5xZsLMLh17NIiMYA9lC27z0fZNEE_rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
گل سیدنی لوپز به آرژانتین به عنوان بهترین گل جام جهانی انتخاب شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102100" target="_blank">📅 23:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102099">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RihQhs__3R7GtCRLZ3b7oMPC9lINxhNQhMF9mJMnLABW0L8mfatevxnZdMIKlvDk17YvIWyR2K9DaVerkxnkmynesqvuwL9j-_UF1Qg4AFgfDyPLxYG921XZ3ncMaYYqCYEQI1P78JXATLTz_I2dLCJGptwez5MK_upgy2Jr-a8z46pXRYlk2T6UcMNyQq2Ef6M_kdHrBWZGr9WJ5lnXVpvJraM4u_YVi1C9O-1xLcSIo9v0o8Jw3E2ycmFxS_JliIIuPDJmGotmF24QXWDISkCtnVI5Ub-A-wIoe9RNq_pZb0wXE-lysb0V-XQTgpY1Qc678CXCvwr4vCZcyGvpFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رومانو:
جان استونز به اینترمیلان
HERE WE Go
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102099" target="_blank">📅 23:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102098">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEqE1rhQiQyLSfxIOxLNP0tLw6K18norjXPGhHerSEsk02qGBGni3DIAWBKqDsPCtB8waOvg9p7XkiXhivWVMvGu8MMM8qIuf-2tlgD4ESKVLDgbcuw8Nc7WOts4MAC4-TAXsNFWdIf7JE-AAENowr4rnD_yfC4pqimpvezUIplPFra-3Fjo6b6K_tYyQG7MlnoGhuTVsIUWz518TlPISvLSN8_pnLlKn0N2TsgHeIbMGB3FZX6Z6ztGYyfyUHoSZeBFRHaUe6v3kTK9LLp-Z1rDeJnybiCs2oFqU8dqvSUdbOneIyWcH6PeVjJPrfUYxAlkUVyHPCRpGDmIiL90Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندریک و خانومی و بچه‌شون.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102098" target="_blank">📅 22:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102097">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hl6QqPbWl7YqCzswsPqy_Qsrxk0fN9ZcBXSbHcEFBqwjEWKQkjWbIObN3p-kqngdoHpSwpKWwAOWHa8YluPlip3jHa8uKMe8yO7iOmzA6BMA3uo-YGF5vyZqNchsItyTqnBnIXKipgavDiII6qjvvtWewwcdpKWvqLxxK7HrGrn3KirCIFTblgFUvrWauNU5REn0BZ6f4nWON1fU4R8nmwXaaqir8nqFZ3D-X1M_-IvBokl03FHUJL1Cz9m6S2XT0TPcA-RyFUcpZEfUwewdHG4PrgkyOmc3D40-D-x_K6-Y2HT775h9Gq6iAIAebHuUDPnNf8CKefc6O0T3Ppc29Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فابریزیو رومانو:
جیمز ترافورد از منچسترسیتی به لیدز یونایتد پیوست. جقی 3 بار ادیت زد تا تونست درست بنویسه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102097" target="_blank">📅 22:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102096">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJw3IIvR7Sg_6yBbNbNPCcJkoutsWUvqzVqIjwnp8HuhdVlHj9gn_oFcRimM3cQXpGPbnrziLos10i_FPA1ScN5-JmOcjNxCWFt_8gp5UM3BbSR5qsI9nDybVUp714dQRwJoNNmi445OTOoMdmz4aBe9OVB-XnoLdjIR8BukhxasY4LrvyVeSHkdGFPrX2m_CE57oqEdIfrgHtkQfEAZS2Pfz6KD6Qh2Rt5soAWj-bIoxOoIruBbWX4Ckl5nDK5YjA0w9Qg4wp4ODkVhYYp-Ix-oBFVvvW3xnO8GUoW1t9-EzSRFMIMfkllNtpIkPk9r5LCkCTrBKYacKgadqljgqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
👀
تیم منتخب بازیکنان آزاد در تابستان 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102096" target="_blank">📅 22:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102095">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🔵
متئو مورتو: جان استونز در آستانه پیوستن به اینترمیلان است. دو باشگاه در حال نهایی کردن جزئیات این انتقال هستند تا آن را به طور رسمی اعلام کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102095" target="_blank">📅 21:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102094">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMHDI35b7aVIq7AxfUbrM4lsrXxP-ZBoYGQvOGYLpYeXVqHYFOcCBCRRW7VDc4MtWt-bxe-tjQg-IerhlV9fGHHhfOMYp_ybqAaOHSZ7wow4TL76zVCo6j1e4802HVL7W3IgPN-bnIrjGd1h9IbtNSBbUcZNq6CjT-ycOlHNpEicWWqr0snSF_phkP45FFxAFdm10FFjcppfW6DQXKS_b9z36owRfxPDFLNK04h1dQhu-pA1B71BOjfXQ1TuiFhPx9ihsxCfA4OKl0oXZiFJCb8xMypO1INe9O7yBFkIvCtsQT4nA_mSxB2eC3ngekkCFBhhlhVllVDnNwvKizyENA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
فلوریان پلتنبرگ:
لیورپول گفتگوهایی را با مدیر برنامه‌های برادلی بارکولا و باشگاه پاری سن ژرمن آغاز کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102094" target="_blank">📅 21:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102093">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OH2-W7fRvIzK9Wu79wytTgnU2xwRwnE74KMpUGhOJyBRKEqBiKsl1uuLmr4P7_u0k_UZ-5ilmB3iug8SHuhyBN890SBWd-0yHkhGf9EsXcJvpns7ZWCShJc3MIiZ3C2VTGsp2QTCFabRY9HHLtykOKZO3rI68Yhvd_N1Znz2Bjy5dmrCqYkoG-4HagL6vRK43nWaeewjKGaHgYpLJBbviY80jBNvsbWvslswVSA1vmILzWJGBxg0JYz5T7EI6Uml3nHoSyDT0E69aQvXpt2-_g2j57pDQy4SEjciSVjsy29Ft2T_QM6EDtSCDfGcOlj0-pHgBOzXCz46bU4Zvm6V0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رومانو: چلسی قصد داره جردن هندرسون 36 ساله رو به صورت آزاد جذب کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102093" target="_blank">📅 20:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102091">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDC3ZcEJ2gnKRi_FfQNEucxVLqT7s7yjbF8vz949Ie3WZag1Lt-vF3bt8jWVDD2evy57d0StpopOJOvt5YKqVuyGHqFFxqmkLiSUY4xdBgbgkd4T7vs_qBOhHoIO7MtOzd_NhwUFrS9SfFv1jZpH9cX1LQLcDtZR0vRiA7rM7lv5X85VOOzJD32e5H5dN-g1wp6Nk4NwTwLzF0FT4NEmHEW4VKWc_82Nrnypn5MVMuuSYhKeLER8h2Hl0RttZmwNnr2vftW8h20QCxJNRQ2O9sxWvfF-d1BgNI98Eq4M3J0IvahcEs9JgI5jwQ7CfhC6HrQjVQvCTwcxV_x0kPP4nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇮🇹
فابریزیو رومانو: پائولو مالدینی و لئوناردو از سمت‌های خود به عنوان مدیر فنی و مشاور در فدراسیون فوتبال ایتالیا استعفا دادند.
❌
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102091" target="_blank">📅 20:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102087">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aoB1q3kMznRyryeJjeQwnzF8JQBSECU1sGa8CMa2t7-Ja0oFx9UasmF67E6KswvEt-EsADMHumN7hA82FrwN8vqbTtuTmLkE_NsZoG4wJ6wizgLNdOI-pTuTz8COk9_nmOWu7VESTNwnjStPQEGoimp0a0x54oGitqtv_kpl0XTThnvYgdfYkhm4PWsxpCgUcY-_uNpm3Or1dTQCHo3IjHE8dJe0TcfjMd3BqUePCymLyTFse3Ad_ASWplF8fNmcB2M4bAPoqQEPccySk1RSvnGgQTdUutbxL1j3dQx-ZSw5OTTdy_O0vYDoEhzFN8byGGF3ZSsm3jP7Ikk-t1AERQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PnRxG3dneRZHaKe6PE-ToRSPbLYAqpxX6ZCbg8qPDATlwECuReJ04Dg-tx76umHjHQmDrxfrYGVpyXJkPGJm_HsAH2Bwye5a77r3DDDhfyNz41qyQ-1AvfbyZgvR_WuHxP10XHbcixPiEX4tV5Qw_G0vfGLPPF-8dIVkJDqO90-1Mw7pXyakPCsI9pb_jds8TIcqi-PlhDsa4ZVXFeTJBZ533OVVUBCPdUywRx3TFKf80MEI9TTcyiVlVr5mwa1AlXUhabV5y0YP0i4O-iVylSt5zbrv7OqcSo1zvxpp5oCTDDNpFDvj-UtXezCjLiU7BcAueUjFCEr_XWOWUR2sDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rhDpXUpySQh15Sh2eItdqXrsUDmoWMyRTioOEFMnr-VEVYn6QpuuO1_xCkB1g2kBxK64OdMokfzdGqda8aydWGSAs4E3lf3TRkY4q5kyqZ1sVnFGw9927BHclvidZe8WRnlm4o5jQ8pqJ1dyN-GQxDJvZEj1n9yKSxw7HYCoPyvUpYwoBVe98GtJBoMpg16oEfGs2x8G6hEW9cVrD6hjIO3yIag5_ApFRu9enXlsqkiUQ3CRnLQEu8cgLu_DK-lUInkXBhc5pwqIMEEYffno-Z2VWp5wMx4zim2L-BKYrKsQx63xycz0CjDO3qTyRqIBfjSPylKOVgxExceETvhacw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r9Xpt-HcJ6pDL8sgKeHzSlNc2SZuun6qfRYl1mK-gdwFpaCGR25eFKwcsKinNMGtRIUY-nioBOCySCk5UaT6Mpl_uNA9u3I8pU24GNmrepamJg_0a00se6BSAtbh1lF72bkQeeBB_RGJKGq6tW3JYQBnKL9RHjF8c609-fifUVNyvt8YEybFLmgDltztww2iIT-H_1WpidzkqNU8_XLOhhP3QJ3dIEfhicbJLJebI_H5nfK38UKUh5XSvzls3ki9tMnD0_uCdcWh_U08kwd8PdYiR-7_nNqMXYXCu3xifHUuX8MijQMa4LmeLXUxfBUiZdI3uX6941BKFXF9uI0wtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عشق و‌ حال وینیسیوس تو‌ جامائیکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102087" target="_blank">📅 20:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102086">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1v7-8ArdYUwClyZfiBqkX9j2laUpp8PqftAjl4uo0sKA1laBXhIdGt0zpHD2_jtP7H0UeWapIrPaQQhfe7cxyPxtxJyZPnqHYmnfZ5raRmc9lHgB8C6Pz5hKovylUjhFaZvmjtDUyUQeCn_VrdogbIOpWv0USx8r4ZjgG66PHoJFlioAoCY2HqMtl_JJ4lKkQu5BkNjpdkBepQ2E1Ne7jcy4uK1v2ANs1-JvqOMZkO1azLx5-QT3MYUaRW54-ptyyhBzCJ9dN8EP1WklV4sElgg5NxnXURXnTcSBAPH1n6AdsOj1REn5Y0EeIWpLtaE2mge_nO8W4FOmOMIVGBpPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
گلوبو برزیل:
سانتوس قصدی برای تمدید قرارداد با نیمار نداره و این بازیکن در دسامبر جدا میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102086" target="_blank">📅 20:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102084">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jyVV_ktfWSYo1Bj0qm6pPYrCoGuAxVobgs9cqIrtsxIVjD3_tk9GJnj5S_Comj1EgzKFqBLclKeCb8j169oAJfLQJOLxBkDoye3Lc5xPwwmr4FfA62lvZ-qb91TG7skO9Ai_QNl7SqciK-1FiQebf2k9ZqtyQIxQK51wcVQlseBT1Qb1QHKQsI86brw800FPlY8rckdO08LPZKRLSC-zzE7tgSuE32-tZ2-IeKniC1IvtaEFpINwAnlkHOPAZ_hb6CZo8rl2EyqJyAU4DBtGZh1WDSrTm34gVF9ibGh1MHRxIHtOe9XfNVo8NZVb_Gj-l4rNy-B1-7TOX00v73xdNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CUTumRa0NvoNtLdcVhsdUCG1Ni-pPpsVtgXguN_5BZEbZt_X17e9gN5_CjIqGPn42xL8vfhNxWwN6LTgtz5WaCafVUHK2g-Rrro-9CTi8ltj5vXMx3BNIIVM1RorjCE_kH56HP-MWJdARo4N5LkBhzZGssjlswyWHOeMlBD22FXE77p-yIEHYLCkm5doGXYYjtto08s21lOfZTZhdMrig5x5Jn-7A7FuEbzHVLHPAFYKSo5qHlF0i-4Aa15r_P3zqUol1I0Cgjm8yX0tZKmA6lxd-IXwljizEgMMdYzIHG9Of4OTTPNfVQvp0bfS_RzB2pAmX1dGxjQ_r3gn-sZC2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اشرف حکیمی درباره شایعه معروف طلاقش گفت:
اینکه همه اموالم به اسم مادرم بود، هیچ ربطی به ازدواجم نداشت. از ۱۸ سالگی که فوتبالیست شدم، مادرم همیشه مسئول مدیریت پول‌ها و دارایی‌هایم بوده، چون کاملاً به او اعتماد داشتم. حتی الان هم قبل از هر خرید یا تصمیم مالی مهم با او مشورت می‌کنم و این روند از همان اول همین‌طور بوده، نه اینکه بعد از ازدواج یا برای فرار از تقسیم اموال اتفاق افتاده باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102084" target="_blank">📅 20:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102083">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uutZFj_5SZwLqBdUfb2wK2oKrept0ou5nou6AwTItJh3fZrSeJ9ECGmVbxD_GDrzxm6Hu2YXXYPMv_XO3QB4UjEbcxRK-QBG82zlDAubaZ9acwWA1m7sRhwgny9WewxZAs2IYdhmdOj_hqLKhYrM8dT-cWe3m3QeiG-zOXKtW9x3Oo5h9NuQchOfSRq-X3NjN9t0ME5g80jAoCEjVk71bBEZik1mWufX2AyMD4Isz3j6prfJO7tIQejC02QGlt-JMIPUnsgcjXNpc5j0xTmJCgmN769o83ip2QfHfuxcdwsccEWpVvmp0U_24wNoC34M_0ip2eyGksDKP-krPRuZGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
⚽️
امار سه فصل اخیر جونیور کروپی که ظاهرا گزینه دوم بارسلونا در پست مهاجمه
جونیور کروپی ۲۰ ساله متولد فرانسه ، پا راست . پست اصلی پشت مهاجم ، مهاجم نوک هم میتونه بازی کنه.
💸
ارزش ترنسفرمارکت ۵۰ میلیون یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102083" target="_blank">📅 19:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102082">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMg4l_qE33Z3_Gsu71O8whwZd38r2sbKITjwJLnfq0T3fKN-9Ts-ISjlk6iEqQJUIRgj9iAn2eBXiHAG2R1aLkJYPriI6p5KQJFR9hPOorXPLpGe0HFcIG0rwuQzf4kvGeqZ46k6esm4SQFOFjiTiqqB1i-PEA81J4W8xm5eUPd50UObEvosDgQxIzcC68l76M0PBvVymOcM7JkqV5gbODfEWImOK-32aC35pR1ba8scBKpLSnUeOR041zVXY7VYtlcdyNy72dYYDQF3WobkNYxmGBg6CxOyM2g_sTPSC6zbFMt_7zSDhWGwkM-U9_MS-SjkkYHOC-j8oZTPQcW_9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قدرتمندترین باشگاه های جهان از نگاه اوپتا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102082" target="_blank">📅 19:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102081">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e948c535d5.mp4?token=j7PfDAWy6xvAVGwMTij-2EYw4E1byOJuzqlZp3PbWvtfGgEDchBQKd2JgeTIrNRHbmZJEQd2zNSwqDI6W32K9IXciBtqDPWECvksk3i0jujzwbCuTnZ4mvykiLp6i7zqoNwhy5Yzkwl7qPNU62TcXTAwYQHi1L0LSk993xvUrF1BS9FvGCtVjwHdXAtzzuWePpV0GKEUMJcqJang64fRVGLJv4EZxIngu7seJsBwdmiAkcKUCcFtU-Vjm3JVFVv9jDyrDddqUsA5K-Bu1JDCyAZocKD6i56bxefgmzGa-Pl4bW_Nw0iNhG0pPLeylf0AOLTkEnu6qpQywFzxufz_IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e948c535d5.mp4?token=j7PfDAWy6xvAVGwMTij-2EYw4E1byOJuzqlZp3PbWvtfGgEDchBQKd2JgeTIrNRHbmZJEQd2zNSwqDI6W32K9IXciBtqDPWECvksk3i0jujzwbCuTnZ4mvykiLp6i7zqoNwhy5Yzkwl7qPNU62TcXTAwYQHi1L0LSk993xvUrF1BS9FvGCtVjwHdXAtzzuWePpV0GKEUMJcqJang64fRVGLJv4EZxIngu7seJsBwdmiAkcKUCcFtU-Vjm3JVFVv9jDyrDddqUsA5K-Bu1JDCyAZocKD6i56bxefgmzGa-Pl4bW_Nw0iNhG0pPLeylf0AOLTkEnu6qpQywFzxufz_IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داستان کریر سرمربیگری دلافوئنته
از اخراج تو تیم دسته سومی‌ تا قهرمانی جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/102081" target="_blank">📅 19:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102080">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
فوری ترامپ: به درخواست واسطه‌ها ما در حال انجام مذاکرات فشرده‌ای هستیم. اگر این مذاکرات موفقیت‌آمیز نباشند، به اقدامات نظامی قوی بازخواهیم گشت. ایران فرصت کمی برای توافق دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102080" target="_blank">📅 18:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102079">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dln-Y8732MnCBcUZuM5FqNpOfurGzds-lBFnql6rmcrASAYjCFo9gl9SZUtT8TPIcf4AUZZ1KfII2WxYRWf6yD4muGU-gmFc7AdqM19mbYWZKgEXpTbqEKbiZ2Z-9Pu-v9sVYLnguvwRyRXjwzbeQenXQQ_MF0okapP99I55NLaRfkT4aXE4dDJ7O4vFPJ-Mo6AvlWNL12ZLW7J45beqA_FteFkTg3ObDda5ClzH9TSg6NmuRKcCnHeVg7N_gkEZtJu1OK7f_eGTa-sYKAO1L2wrPCLIBCkAcmb87LZbxr-kR5elL53RnHqr72W-WkwjpToszF47V2-ZrVA6RmkVxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
👀
چند ماه پیش الچیرینگیتو توییت زده بود بارسا به بازیکن های بالا نیاز داره، و حالا همه این بازیکنا رفتن رئال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102079" target="_blank">📅 18:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102078">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abAxzfwWA8SmKdTi920Y9S6PpqlWvE-MObIfFhqIT5YHZ0YwDCg9pmCN2Zf5JjACg2fM22nzkOmpqEOxLK4pnvxjwNQAukE1_SHfUdmh6PcaGyrSOAWFOlxrSp-T5gqETwUDaFz_NNTg1MSlWfQe6QZvCKIinQpmlJQ9AToLC1lN4vwo5nFXFeR6MXPooVJlPavXiQp9GURg--tULoDhzIcZAAm4VvRccEhk8nYIoZOHVSZRNGDe2HMH_qxc9vbZRAvTjXNaivZLjH1QDvqfeww50W-Qi--cqyK_QicD0Ordm13FnhEnoaw2NwFfmR6wGIyOrXjiIX1wuV0BiWUFoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
امباپه:
ازم میپرسن ممکنه یه روز سرمربی شم؟ نه فکر نکنم، من تو تجارت مهارت بالایی دارم و میخوام که تاجر بشم البته بچه‌های تیم میگن تو میتونی برای ریاست جمهوری کاندید بشی ولی باید بهش فکر کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102078" target="_blank">📅 18:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102077">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQ0oy4MS8Przkr9pu930P8Sx_8bd6hLzz8qPVYT0fGc_YR1iNQfk6Q7mK7RLZzzCMraTNDIPdVUmIUO0WQIJhm-v14NclH8h1om_yUtsgKNCiVji1qra1kDYy5c_4dOwsH9jRaNu12jlkmaluhCAKqQkvEF9B6JbsLhvv1EXObj2_2m0L_U5YRvPDkW6Ys1x0Bt-Z8oK5h1gvGrM-Z5B6aDub66rNgNqXGv8QDNshUlJ1zGyqg3RDUD8NEIC0Yo-qEEghC7-gnv4lzbse6RglfaHVMV2TgIIzPyaOiAACwJZ7jltoaW9st4kPERD_-9dLz8jV7ttNh82JQDx1vUnmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بی‌بی‌سی اسپورت
:
یک قانون جدید در فوتبال انگلیس در مورد مصدومیت‌های دروازه‌بان‌ها اعمال خواهد شد.
اگر داور اجازه دهد که کادر پزشکی وارد زمین بازی شود تا به دروازه‌بان مصدوم رسیدگی کند، مربی تیم 10 ثانیه فرصت خواهد داشت تا یک بازیکن از بازیکنان حاضر در زمین را انتخاب کند تا به مدت یک دقیقه از زمین خارج شود.
در صورتی که هیچ بازیکنی در طول 10 ثانیه انتخاب نشود، به طور خودکار کاپیتان تیم به مدت یک دقیقه (خروج موقت از زمین) انتخاب خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102077" target="_blank">📅 18:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102076">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8xIW2zH0Oo1NJu_kX9XK9EWsxnCbSJrT3DMr3FOMTwaXcL8Lb9TdAIGNSytSrvZOLsAIJYOIDUO0WJZB2ia1QIekDPX2V4zxWmvfhzf20s0todAxTAUI6hxfqn8xCKLA3JfVxXjT85XVmV74EkzRq5ycKNLNRyWkQQmrfD1HUj3NizZqMit0eKeaOWUyk_o247N2R5-BlgpC235MaCv_ap-QEqvO8y0GiapFVzRBZEchyppBN01EJm8yRHeenVvwqYqqFP7IEUIZ2IfQZOZZ1nrZMX3W76HaoQaw6PNEJi6beKzloBQ3IruBJSHJY4Qt65c43q2Bk4oK8ZSJ1qCEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🗞
فابریزیو رومانو:
‼️
بارسلونا با افراد نزدیک به کروپی وارد مذاکره شده.
⚠️
بارسلونا با بورنموث تماس گرفته تا درباره امکان جذب کروپی پرس‌وجو کنه. بارسا یه سری اطلاعات درباره شرایط بازیکن جمع کرده و چند تماس هم داشته تا وضعیتش رو بهتر بررسی کنه. کروپی بازیکنیه که داخل باشگاه بارسلونا خیلی مورد توجه قرار گرفته.
❌
البته این انتقال خیلی پیچیده‌ست؛ چون بورنموث نمی‌خواد تابستون امسال بازیکن رو بفروشه و منچسترسیتی هم بهش علاقه نشون داده. بنابراین، این معامله اصلا آسون نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102076" target="_blank">📅 17:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102075">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VwxGtZO8smq7yALRfkDVMAIr5KAQS_XZiFl9ffSTiCTpN2GB2dMEwdrx-poexrHqLiGGbIzh8_7Z7Vt28zye8q9Y1gHitOjboeNeMX6skIYOB9rO0lRRsA4Yur7y8tp37eqV9m1eVTcNqCzhttCSXwGmm6An2LRXA-83XWEzOpaaScvuvpdoyVAX-7-cJ3jez3D2WGXCPIiw3mfE1xTJF6z9cIQx_mK6NO8tW53_bMok0PuOEZkxy9P7UGwWT3YA1yyE7MRQBgXejz8SbMx0sdG5G43setJsU2AKuN6smOjBA4qBIETgaJrBHIgfJAVQJmWlp2-QMXIoIAgjOppM6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
فرانس فوتبال اعلام کرده که بردن توپ طلا حتی بدون کسب یک جام بزرگ تیمی هم امکان‌پذیره.
📊
این اتفاق برای این بازیکنان افتاده:
🔺
جورج وه‌آ در سال ۱۹۹۵
🔥
🔺
لوئیس فیگو در سال ۲۰۰۰
🔥
🔺
کریستیانو رونالدو در سال ۲۰۱۳
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102075" target="_blank">📅 17:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102074">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQ5ywJy1MdOD9lJ8bEveZP1DWUV5nRO3e_mt2A-qTQv6iJ1IZ1UAf1QM_B4QW99U_z2ho86UGNNCPgqOhThtdJkMbBpBID2v5VXsprnAHOKZo2PkFPNUJoEfOwzbcpyZxxcflx_IbxazjmO-tkStxenFim58EiSU646PQ-VqGEKi9amN3mNPAXIXgVJqPuTHpydms-Lfwf_wmfoHV5xq4s8cKNNFmOBkR6lAuaIFx5W3yVgpErl0kAxshGQmr-b9TPzo4tLmJVcGuZBXcQwZmMxGRj-QiV8u4y4ZxfeIzBDeJJ-kyDCR5j5tstbjtmXS-Xo3LXHkRRHvwutK3q11xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو:
یوونتوس و پاری سن ژرمن در حال مذاکره با سوزوکی دروازه بان ژاپن هستند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102074" target="_blank">📅 17:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102072">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DX8wu0b-214YUNnlt2_kD9uWVbdY6VyJIKoWlSLF8cwoucw0flcV5vtIAMa2sxYWrAfcaIKG1s9F0oGjbkjT7GpVdGk6_P3IMqfLVZEnQuGDm-p36bLXEFVfR5flx0BZZiOHKlUkahTjCDvO73gwkQYHKwg99c588F2m1GeUEO7fnZhgmer-Cec1KG-ZtvuQQzr9G8E6Vabwnc-16CPxPoo4hHNzEdT2fbNDMknWOnn133U7Ir_vTwsIm07dRO3UzZ8WluWLpyChIZLZcz3E2umap3pWML2QDzDrEeMowht-Dm-KToZkYnOdIIa6jJ373vr9SHaSu5a6FnVF2p-t5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FlBjMnDnOL1CC7HCzlGVswTzLIazJjEGBNYg7UJE_h4GSrEZtQMXohjansNBijA59RkuhSBjtvG4eQ_J4ns_lOvQ-hquIidZ10btlZFKOE2FNJfxVJ1LaBuGEcs7A6tkd7Lq7DTzQFsaQn5EUOvDsCp6vRiHeScYJcFGzCX9PHb43OIpr6T8oo9squREjxjIS1XfVhKIxlrQopSZ2e-aS1bG0Jw01_Skt9p8RFtgtjZVgo9PQsk1eMsAv5bRioEjmfhOiA4jgB1odUBWARF_VmrfunKsb8Yh2oQOj2CnheuKQxJeNbMCQ1KvNeu2qr3TV-mNUpu9n-M0Qg_Zfii0gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اشرف حکیمی درباره بهترین خاطره دوران کودکی‌اش:
روزی که رئال مادرید با من تماس گرفت و من را برای تست دعوت کرد. آن روز بهترین خاطره دوران کودکی‌ام بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102072" target="_blank">📅 17:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102071">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsVVLEndMlj6BaU20SxfjZBjO2vJoi1YkB0Zv0EPPMycwlxQvcwNe0jHXhOWidVg8apGVTRUW4XwA4ujOcVlqB0uPChd117iIKQhK706pTcoxMdy1Dc3Ix_niw6PgoiMPPUBFeeOw0qE5DK3OqiWzejTbT5w-cx89AUAjkouJe4oYDTB69LRpG462Q8-0Bim65bFqejclIaR6RhD5GilCYJ0WzFi80E6nmx9LDTxTzLoN3cBrhUualpMpcR8LYWJwlsVGLkZLjhDwSgF2-rH9SzVPRzHDrlovuPMnW56TaIkzhq30AAupF0Hkh28eEwePnqbzZUXTSj08XSjzi8Xrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حضور دیومانده در تمرینات لایپزیش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102071" target="_blank">📅 16:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102070">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3120e668b.mp4?token=b71V3an4b7uopbupL6vfHAprDqsg5lwUZNvNzCaMB4moqt23wZ0QgIIKZNniMxJ71ChkssSRmiBSMQvuMHktGsKzUktMk7Gva3idvYvkCJnqWXCdbM486yukU_FsVf6GMAjVvmJ-etauwp8nw6BB1oChMNl4qwV4JmDvwq2Wx6QmY7QcVXr_ZWA13ySfO1TM9K8j_A5o7LomDbfxIr0aM0FG6nIG-W_AqicPDrV0Q__cblmB7hEgaK3YHEGdnJ2QoFGT-f7ALLz8ZCCIm-Peh1MKLVVJBtHFpVUYF2UMDf6q-k-Ba7o87wMeiqJ3RSXs1exPZjAic7qLaOBJMrkNYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3120e668b.mp4?token=b71V3an4b7uopbupL6vfHAprDqsg5lwUZNvNzCaMB4moqt23wZ0QgIIKZNniMxJ71ChkssSRmiBSMQvuMHktGsKzUktMk7Gva3idvYvkCJnqWXCdbM486yukU_FsVf6GMAjVvmJ-etauwp8nw6BB1oChMNl4qwV4JmDvwq2Wx6QmY7QcVXr_ZWA13ySfO1TM9K8j_A5o7LomDbfxIr0aM0FG6nIG-W_AqicPDrV0Q__cblmB7hEgaK3YHEGdnJ2QoFGT-f7ALLz8ZCCIm-Peh1MKLVVJBtHFpVUYF2UMDf6q-k-Ba7o87wMeiqJ3RSXs1exPZjAic7qLaOBJMrkNYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
عاشقانه‌های رونالدو و زیدش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/102070" target="_blank">📅 16:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102067">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D9g5_itA8B9Y8wk_mn8NM8x7loZ-criNtsyXVzmC2Ju3oo7FJ7aJG0nPCy2kZCcuQIHt9wA5BImpeHp6dWZJcNrhaJ767I9tl_fSDTe9J5jorsiZFnmr7HhYl2EGl-mlMPOjRMMDqe_meeaDYVKj-z19TT8t5iwqpMrtvMUhe5Vk04yGhUM-nu-60YPb89HSB1eF2lqV8sHZFBN_P7uZ6pn5DpTsT1MY2pqEIDTDd0N73K23C8SK3Lo7MypOsTipefyfU8JRMOb4qBUQmBzXbYTXs5f4WwvQQl4U8J7Vtz4Nl4GrqEJmHrUPgcSSaIEqi2bFwzT2IFtFPDA365kwbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VPLGeYb0yO3yGo6Zz6P3uuVOuho9XEZFd6z5APdECofPhqJPw9FdrakZcDZfC9qSpLB2XMOgDWZZ3e1qT4-xPMJosOiHPLLxaC2sqBEEie0zQDGuXnlPS_bXCfwMZAde-BfF9Z-fpVs1t72j8oCAIOSqt1dgaDaGqltcmt1CIyNROEcMztdHThR1bM1WgxIC-_JIQU4_neKXZVaXeiZpQ5AHOlhSgWJU1sOhUk26qyJzYF-MZ095IKvDAoN-nDXtwUXHjT_5aOGcrQ3b6ByUS3sdMIzPIvxTXEZLK91Ce_R45t0Iv3a6VeDljdLTt5WmEHK0_j95-PEsVoJeoIRQAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qlvMX0iCTgNsQzs47qCDFRyXZ2T-fowVgjHk6fvKZxnfLymtm-oW6Z9KC3Y9JMs9Fv27xfNk-yEivvmMOaURxxxH6JmCqH1xUSzYgyLmaKABVNH-bkw9tyWOD9jidzI_j695x38Md-TRDDYDGzDB9NsZP42xThZuHYJypuP_5chJYRvx8nOxGPCVtjFZPad-W45bOc55AGOvAPSdozCmo5XEFniDoIP3h2qesKuFyIvjcHRB1GcD7ohxcGwt3u2UxaMta5icv6_dLaEu5L-bK_PCSxxRe6y-qzkZekYtS3ZC24DV1b2PvWKFkXghEpqDz9_g5ybMsAUj2ElmKzBbPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایشون که تو تصویر میبینید مارتینا گونزالس دفاع 18 ساله بارسلونا هستن؛ حالا هی برید پیگیر یامال و رافینیا باشید درحالیکه اصل داستان جای دیگست..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102067" target="_blank">📅 15:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102066">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
‼️
انتقاد شدید امیرحسین صادقی از مجری خانم شبکه دو سیما بابت انتقاد از قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102066" target="_blank">📅 15:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102065">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f32263398.mp4?token=j0GYlbZqBIcwVoL8PGN4J3B5aUo56UZUhpaDOCLaRsg5NMly8mPPJ5cIgD1qRivPbaQA8f5kDKxLhMvxAu8DXSwhT7PYGvv58tyBD8nycxCNV0M3wcchJ0TOPgZWnBgBZymd6uTbXrPsun77iccjA2GaImflXgfu3Xj5IwrErT5xr8Q5k84UAR-uo0yBjGj4rtJf2BvR-efVU9ZrjvjSKpIccRCkwYAvs7lFEaWJSHm_4KPMdjGfI7L5UzkvbH9jBtw1XIioomkDp4YfH-fUsex0wwUntMOhP8psp03HrNWvetj4ocWU4WdSS1_ZTNK1TCDYq_uHbb12kK3M1mUtRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f32263398.mp4?token=j0GYlbZqBIcwVoL8PGN4J3B5aUo56UZUhpaDOCLaRsg5NMly8mPPJ5cIgD1qRivPbaQA8f5kDKxLhMvxAu8DXSwhT7PYGvv58tyBD8nycxCNV0M3wcchJ0TOPgZWnBgBZymd6uTbXrPsun77iccjA2GaImflXgfu3Xj5IwrErT5xr8Q5k84UAR-uo0yBjGj4rtJf2BvR-efVU9ZrjvjSKpIccRCkwYAvs7lFEaWJSHm_4KPMdjGfI7L5UzkvbH9jBtw1XIioomkDp4YfH-fUsex0wwUntMOhP8psp03HrNWvetj4ocWU4WdSS1_ZTNK1TCDYq_uHbb12kK3M1mUtRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزاله اکرمی بازیگر: رضا عنایتی کراش دوران نوجوانی‌ام بود
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102065" target="_blank">📅 14:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102064">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1e8z8o2x5FB7F7AVnHvlWtpaX0I8zdMmyQFBB0AqQxA_2Q41MKXBC61-l3bdTyhqReCCzb9muAq0UNF6wZBzPZsXYLmy0buf7UBIqNE-ESXLnakrh6NAJp5_M4Jd-4NZFUa2opjfbfXCKCjwlOxRzNVlIMkUAdDQjFe2Emh_mBouYITTPhdObpAztNrI02jZanbGhEiMxcR57bD1gdqVdO6YPUzdVbaLVWXxfgbAvZWQu4gq5hMJEqd30UZyzHB1MnhIgyvx0HBUE_jKBelUXq9nd_lPFVkq-XP7MohWVYs6bJI7vLDVJbvsaE109BQLc6Mbw5muKNa47v-P3XOJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری از رودرا (ESPN): رئال مادرید نسبت به احتمال جذب رودری خوش‌بین‌تر شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102064" target="_blank">📅 14:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102063">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyZkSuEh5jiaYWQrdGpHBmPuS07-6BDmLv_3FTL22J5zCJBpwt2zUF6wUj5L2ZWwpX6mJ55mFUtyx9rc2F2LOvoZa32ooxNl67nroRZENKyBWvPk91Bp4nwDftHpTYe51z9haWlEAqemmm0Z247w3jfjqhAGTDqcG6uZhT_sP1nMauiQJpEkVoTjfKWQTa7Rx6fQclNncabdZXC02CbeXM6t6WueVF184JXes4x9HTtjvzttPiLpQg5xTbcpPhjipzivokdA1TRlRTh13lcW8kzV3R02Wf5o4nqNfQGE9uccu_3TKqX6GyP9n0VWBl7pMv7j7BUpE3Ldu2szU40Q7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
اسم کوکوریا تو لیست رئال  برای لالیگا ثبت شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102063" target="_blank">📅 14:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102062">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMKpuHup3NNmS5gtTm2hqoMzrthByD4rS0CGikxRgqnkmFyjywOzVWCc44Zuqxanq9ayoMMagzu_WDxMFOJ0iBj5bdJFUp7TQn38cQSwm4G-T7j_e5B00r5vZ9EpM4keFi7i7bNNPJHY_cm8KBDB6VupUZSj2_qISy3XK-cvcBJ_YrLf84bjJ39zSrhp_G47KeDpdP7DwE-WviffuMJtQxtDGqoi8EX4iC0dgEyPqGj-VopNbdjMW-TfWGbQfFGJ2bJ_4P5S_YiPHUXrhvyMqKZAmDvzHTUSRWctmgm1vu0iRSdVRe5nnm-BZy3sfIZT-SDKoAZr4dHLvTjh2Lblcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
مقایسه عملکرد نیمار و امباپه و هری‌کین در بازی‌های ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102062" target="_blank">📅 14:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102061">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2084d796e5.mp4?token=nJuzcpFvHl-BnWmfQZz3LNZGbXwiEr9BVfyBHBgLSHX9cG8QqZkgYZLjN7uKS0JDTCM7I_F6yB1huckmIV3fIJnlBPlX4XIbtzT_y4QTmVWBtlq6iiZtPF69gQtGTkXLcozmJ6X59-dLEil4JL2KQHNd7_wA5I03HGvoJlkk-Ji3HkoA1TxjKZEVVkPp_qUtl0wEBoNyYQnEF473zVjEptOlB3eJy98LjEJWr8_jg_TzJe4hw9C7WeEvy-CK3jKvv_kw-0PIGo3iSANzZRQtO23Ie9Aff4Q6AK8skcwii73Zwoht7gzmuRThIQmiS1U6weySZV5eOkWnpVN5w5ON9ruJ1JbclOMemDF-a1-ILQlelpTG4zLS0u3mBQiFteBm2eWETFbYtSeOF4vhyLQTNvkr0t1MwxCqAgoZZc1wmVGVCfenmJusE_1ASHqmNm8aZJsMvncccY3ugo4upYjFxahW0wJtAp-7tfX21PU40PSsPebsNRlK4g6I033AJI49COg-Rk2lgR46doHTSAVic4urmtt08lXb66qJE1FFcrt59WWfgd79EukypdVuNhRDeR_du_HH-6pLDsHkZxMOeNIxcYyvV6AT3DJOTIU0mVoiPvjDHHaQz7K4IlxIk6iVT1atrqSJ3fprPjpdBIE4oUS2AQuNZN92tMZcqBmwPmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2084d796e5.mp4?token=nJuzcpFvHl-BnWmfQZz3LNZGbXwiEr9BVfyBHBgLSHX9cG8QqZkgYZLjN7uKS0JDTCM7I_F6yB1huckmIV3fIJnlBPlX4XIbtzT_y4QTmVWBtlq6iiZtPF69gQtGTkXLcozmJ6X59-dLEil4JL2KQHNd7_wA5I03HGvoJlkk-Ji3HkoA1TxjKZEVVkPp_qUtl0wEBoNyYQnEF473zVjEptOlB3eJy98LjEJWr8_jg_TzJe4hw9C7WeEvy-CK3jKvv_kw-0PIGo3iSANzZRQtO23Ie9Aff4Q6AK8skcwii73Zwoht7gzmuRThIQmiS1U6weySZV5eOkWnpVN5w5ON9ruJ1JbclOMemDF-a1-ILQlelpTG4zLS0u3mBQiFteBm2eWETFbYtSeOF4vhyLQTNvkr0t1MwxCqAgoZZc1wmVGVCfenmJusE_1ASHqmNm8aZJsMvncccY3ugo4upYjFxahW0wJtAp-7tfX21PU40PSsPebsNRlK4g6I033AJI49COg-Rk2lgR46doHTSAVic4urmtt08lXb66qJE1FFcrt59WWfgd79EukypdVuNhRDeR_du_HH-6pLDsHkZxMOeNIxcYyvV6AT3DJOTIU0mVoiPvjDHHaQz7K4IlxIk6iVT1atrqSJ3fprPjpdBIE4oUS2AQuNZN92tMZcqBmwPmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
درخشش‌های فصل‌گذشته لامین‌یامال در بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102061" target="_blank">📅 14:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102060">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7doxcXq3mzphzMyY-wee3kjD6Am_pGoa5Ai_3Rrq420F0TDxthLnWsF0wtYz-WYpHacw-dWKdNuW-qBNoW-Q2M7ND4pd8Y-AnGdwk5sYf7ZfSajFqBRHvuBD4hVUbBlB6QsJ_kPIoE7rQsw67XxnN9Xds0gXadPBy6cUT6RSey-FvEJv9CoN4DHyTNu-klwD8fsoPCe_CEIJ9O-KSRKehjM57sHYWg-ydcsvfFtO2lXkK3bX39hYrdKf41QGm1AYwNPhV6eI-bVIZroBLcMTXNdyaqmXBCz8gLMonMr0Uco-exW66KP3V5IFfgvJnfkL4NKOwybQKHypXZM307HFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽
لیست بارسلونا برای سفر به انگلیس برای پیش فصل با حضور ترشتگن و دیونگ.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102060" target="_blank">📅 13:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102058">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k69AGFbcPXIg6zceX5sjuJAOTyRh1kcKWFzvjTqRq5thHtgexLDXnZd33ZEmBo4kRRBtBRJBcq_5IgReSo0jRdw_GXiS5_-GUjOnRkh2AQf0vKYM9dxwIHiK9izDm_ZLpyy6yGIrrt7txYAUYqoj1TJnvCNofeVgdoA9kgiEGmUsnvowcLJRtX9ZyHURDScsU96JRGLcUupX_Ln2J0fZ19zWTE-xnkSg7tHDdh09zCNWbKgCvpuqGbYAxp-Y-j1tOsx7adINJj964y6LxIF-W8uOOpL5DPnc9SsIDZjjl9f0Pp1BI-fJxPbkW-R-kTW0Zropsi2xjW4lqIVcpDymNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uTzuFaHtYo1tF-53ARZDv-0NrAAct9WM7d5IHqRoFyYk6nlrKCgOcddPzynz8vLOCxOnDWiy7MKB3kUzfktlswPc10_6S7D7zc8fVOvGA3fsdFLC69m48kicOEIJCAEzTL_6Bpo0T7Ur-DvC0Y8PpSahfOGy4C7qigT0mAJCjXqZp7V4jMkqGoiyG97V5r68kqzuUCJm2U1vFKn-SwkK130XAASjG2O6IQh15otW5mjvuwPLzbc5EesKTOr9ei1d6B2R5jpF4VPNl-9Nv8ccJxw8wJMhg0rxTpzbqasCe8ghUn8zJWeR6cxMFSywzMvkZtvhWBIwWcI6RgXa2wLhoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
نیمار:
وقتی در پاری‌سن‌ژرمن بودیم، از مسی خواستم پنالتی‌ها را بزند، اما او گفت: "نه، من برای این کار اینجا نیستم. یا خودت بزن یا بده به امباپه." او حتی برای هیچ‌چیز هم بحث و جدل نمی‌کند. آدمی فوق‌العاده آرام و صلح‌طلب است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102058" target="_blank">📅 13:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102057">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/772e430691.mp4?token=FTPHiQT3kgKo6uq1pNC7OwC7qBuXmaZKLrJPUROcwRL4lgV9YMBpFAaxW4N5tuVfLhgoVf9M-Mdt6IZ-AUG5GPk2BGbbjFXoOcQNhgAz-lwmeAu-69XZ5VMCZECzWmtfhyeLtczCWsaDbxhNy5RC7MxhmQ4Ktra6ZyCz8J4eUAO_O1ji1CjDNuousz4k1PYAwOLZplZJa1uahOA8WIdGb1qeeF02qlPxhoxbNzDEVpINEb8DfIcyJthpWz5NLwOEdMJS6knLxCSEzmhDbEkrlVCXyc08vVXATi_AEm7xgAHCLEUW7L7RNtRARM-B7RtIX2BEyLVwuMpe_Zchj-duvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/772e430691.mp4?token=FTPHiQT3kgKo6uq1pNC7OwC7qBuXmaZKLrJPUROcwRL4lgV9YMBpFAaxW4N5tuVfLhgoVf9M-Mdt6IZ-AUG5GPk2BGbbjFXoOcQNhgAz-lwmeAu-69XZ5VMCZECzWmtfhyeLtczCWsaDbxhNy5RC7MxhmQ4Ktra6ZyCz8J4eUAO_O1ji1CjDNuousz4k1PYAwOLZplZJa1uahOA8WIdGb1qeeF02qlPxhoxbNzDEVpINEb8DfIcyJthpWz5NLwOEdMJS6knLxCSEzmhDbEkrlVCXyc08vVXATi_AEm7xgAHCLEUW7L7RNtRARM-B7RtIX2BEyLVwuMpe_Zchj-duvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این جامی که داری میرینی توش آرزوی خیلیاس پسر جان نکن
🌟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102057" target="_blank">📅 12:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102056">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HhE7P4IwoswX8i4u_DX_esOflRf5gkhrL4eIg4PASskz21wuId5S8DUcpX1HRzJpma6iyX5TViZM50iCb_Y-wjSiQ0Z15-eTFpnlpe5OOUh64aiOmPNRrjIqcKPdUBTvk6qXcWVm_0hZ9nKTVELseBC-wXjXi786KVnCjvJQQpsqHonaJtS63hYe4zPAW6Is87qFRrgqha-jVK-iN6BZG1KG2j65e9gWZBZrCVjFC_OUt7b68yDDzcCjmDeBXlaDAx6hzKyYmy3LnicU1KCENl5SRSgnJJhZ_o5zmlO5DcLPdqMJ23O6JdiqnJ2SM_pAeoiTtESpHBIokNZnwao1YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇦🇷
بنر هوادارای بوکاجونیورز برای تیم ملی آرژانتین:
ممنون بابت تمام این شادی‌ ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102056" target="_blank">📅 12:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102055">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو:
🇮🇹
✅
پائولو مالدینی، به عنوان مدیر فنی جدید تیم ملی ایتالیا انتخاب شد.  HEREEE WEEE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102055" target="_blank">📅 12:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102054">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9MdQ5rh7_KhzGK0ILu5bZo3JSsd2s0FxrFyAPYzS_fh-zXEM4Y3up4OggmhDorarUfgVj6Afpftm0n7z7RwCheU5ormm1CrZB3cLzkOpHKNcqxAyqAIdkytuFrAScVjwQNHWBNstEx4K-ll1zTJ1St2AdklKNg8uTUXzB0E7BQFNGKWWD-R0exvxqgM5PAq1GnW1xf-fQ1jCgSqukyG83PKycBEUBkNp5PQcMtm8kD0EVk1QcFpnaU7Y-KBo45MzxgyD_FnBtvhGJ0_xw0fIXVzSE68oE7p0gvLVrWAvt407iEI61QaYPNVUV9EiI7Qwa_0tF6QPP9X0jkYTEn25g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
الهلال به کریم بنزما پیشنهاد داده بود که به هر باشگاهی در لیگ عربستان که میخواهد برود. اما بنزما این پیشنهاد را رد کرد. این مهاجم کاملا روشن کرده که هیچ قصدی برای ترک باشگاه ندارد و این خود الهلال است که می‌خواهد او را کنار بگذارد. در واکنش به این شرایط، بنزما خواستار نامه فسخ قراردادش و همچنین پرداخت کامل ۱۰۰٪ حقوق باقی‌مانده‌اش طبق قرارداد شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/102054" target="_blank">📅 12:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102053">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1MQmaH0f8Tu5kT4IqKIB_EFV4koTcT4e21j_-ihk4anSRIpnOiBTLpYIo0r6ig6cdZkYFH5kDs2jmAKXZnifafDhwOoLCp4929zC10TewLaP3GEo4ChOo3aMEKYJGr0y1blstiB7aABnCCdyw1p7QH5-gGyBxsjoRJQitqcb8ADh7EiYEp_kNUINFEUzY2nShXBltVcwwz7zL-BthYh0FTQ_-terIv8osOvxJuYe4uziSr8D7nJjhHIdiv9VFitS9h-jZYId4cPq_Ypb7k3CpEmRZLvpUsNntmhHEHTo7PtZrctlLecCjyZPIEkui7gabhk4ROagWKu8SgnjHIWwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جورجینا رودریگز درباره اولین دیدارش با کریستیانو رونالدو:
قد بلندش، بدنش و زیبایی‌اش توجه من را جلب کرد. جلوی او می‌لرزیدم، اما یک جرقه بین ما شکل گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/102053" target="_blank">📅 11:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102052">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZFp6ZLrC0VOk6FsLphfwM3mO-3CUn-THoC8VnpP6EBEQsQQ30aBq7IAUbL9sYekq04uSL-zHnbTTOmETS6fJT00V1KZwjar5SNJIpHctTMHJpKUeXhZWxfpDwYmt7n7fLVaV2xDnkSAVkhPic690q15MqxnnPZP0nHM8Rdgyshk6arLeNvTdBroHbSyXy0lljQ38etyL0tZCycfl_sY4qY8KXYBaJTmfiXB4PhfLSlg7cucuaHy7x4HxfXDZafR5uUVOoVo0tIs0k0NZjgj7wtYFGE8hdN1I7WY5Qpi9qXQA_7f8v-PHkaE5jYFAjidPCm_qWtVuike2dFZqRpMKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برناردو سیلوا و ژائو نوس به همراه زیدیاشون تو مراسم عروسی گونزالو راموس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102052" target="_blank">📅 11:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102051">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/809e9f523f.mp4?token=GENnxV1R_ipJqG6wyfV-D6GHBzV4RrXlHSj1ZrSaIrymXXpMCGfSpRjA2BV37Szg036XvCPifByWzCAwYFnK8dXR4ZMYJCNH4vQ1RbG8-mQ8A7hrBJDGbDTKOMmoTwyVC5A3k0I6stqsVZtmPHcbGIq37MXbPz4MrWh-cibeGuwywFOkXqyLQNiW_ujwTWph2acx-pXfs85If27mJanEJ4afoQhW-D5qsttrq7cbJuwRpO8FjinJGRvw80x_56HAvO4ZSARViVmeIYizy9h4Z5auY1Rkg8yOMDgZk3IRv67o3BEIk4nVUTq0kT0W8OtpNv_fa6f6Bka-ptM4t-uvJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/809e9f523f.mp4?token=GENnxV1R_ipJqG6wyfV-D6GHBzV4RrXlHSj1ZrSaIrymXXpMCGfSpRjA2BV37Szg036XvCPifByWzCAwYFnK8dXR4ZMYJCNH4vQ1RbG8-mQ8A7hrBJDGbDTKOMmoTwyVC5A3k0I6stqsVZtmPHcbGIq37MXbPz4MrWh-cibeGuwywFOkXqyLQNiW_ujwTWph2acx-pXfs85If27mJanEJ4afoQhW-D5qsttrq7cbJuwRpO8FjinJGRvw80x_56HAvO4ZSARViVmeIYizy9h4Z5auY1Rkg8yOMDgZk3IRv67o3BEIk4nVUTq0kT0W8OtpNv_fa6f6Bka-ptM4t-uvJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📆
🇧🇷
۱۵ سال از روزی که نیمار این گلو زد و پوشکاش گرفت گذشت:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102051" target="_blank">📅 11:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102050">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1qWeqn9HBqX9dN2WgnbOck60nbdWzd1KquwataZQpC4uSXXbTood3c23KDiK5hoDXbM6WQJE31vOk4NlPZawHBRP6rmfv3VTorwTyS2kHRSnkL52UkPfNqvZyO6hpEXhBnhdYdTUPGmoiIUbZxsfnjqB5mGuSF7tsXUSc2HasX4OeVctS7PJ0wZiJ6VH9eYpAf0-9DLGNNZzQeJIBHI9nIH638bqDS4YxJ2vGRR3h1OjoYx01ainAqHOripBJ2Lr0-lVDKuaM8B0QSd7zVf1WGYBz0QcJfcl1FAPAcTy87cHHg2ejWc2ZzK9TtIESLxq7OZnRdOBC-pIV_A3kwvsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فابریزیو رومانو:
منچسترسیتی مذاکراتشو با باشگاه لیل برای جذب ایوب بوعدی ادامه میده. مذاکرات با باشگاه و بازیکن همچنان ادامه داره و تصمیم‌گیری در مورد انتقال او، یا در حال حاضر یا در تابستان سال 2027 انجام میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/102050" target="_blank">📅 10:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102048">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rNGjid2S1nVkqdltnbhGPTGnag2rKeE22bDv7xdMnyzvttmkD6CzECU9jFov9xwBgeg9rZaOrL6W1veQGDCP213lx4kl8Pw7WcgYt5IY5CMKoVokp4uPT9rFl4Sq7cSgOHSJ8mr5q4zKMBmFptFN7TChiLLvO1cH-fb4WWQocCYFR8sIYZOHVIV7tQyvUhhziyjFpxQFv955AxZCqBSRmSKxq6Hn5hoj1Xb-UgBhvOT24NzpuKVxx5TQWs5-arcuI6mjOPjaSM7JmoJ7koscQ5B3QLzmtBU9RprTg72DZjfN4Jy0CDwoHKLE-DAVwxi-kz4j7I5sjQZ4YU31lAfvFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KV8P3reHzRlRuL9wCSoby-yB_4g3jiXdccL0RdDxLsVr8_ATb57X3OMzTxwoPAlhy0iDl62_2sLWnxzbZxDhPFIYOa4ZeqbRr0mu3HvWK_oprXNi5mhEp_PsV8fcvqnyLui_txca3kQMBLvoOOJVMFIEhotbkEcnr7XKJfcCeEWSXH3JhKlVFP6kdY6ffmuOVdMM1fgeQhViFFiLJLsrneP5kCrnerm21oeap3bKhreE15KzS85TxyiCE0uFSJOXkDH_e725WV8s4Dc_7rp8gyxnwT1xaRl0GVpSI-xTztMiTgcZeOQN-B5SzWkiHpSiNeRYNUxRQ1isyxeV0eFEAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جورجینا و پسرخونده‌ش که حسابی باهم گلف بازی میکنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102048" target="_blank">📅 10:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102047">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iiboSdTG-k5XCeeHywW0QCylS0_aOCA-uQK_DwckWc6IH0jxIavZZOylq8pik0TmNQ4nc5P1htKL7FLpenDNFq4mS-j9V_wziRsUxfCQgX6TJN_ViR7lOlUdGTyozwqvS2J5xE5elkPuynNif_-VhEGpXiSqIyNp1CCeGWeDIxLeQ2A7TZW0HikUxMr8KPyIFUr0Nqvd8dU4YVZbuHpI9_P4wYqMqoqbRjyfHSp88KIefhp0i5QUSV0x1G0nIgxVW_MqXLNUoYEyTHdYmE7cjvaODP9N1rpuIz_aUmmvvs4HLgWyqnnSomHNGaLwOoBL5X9AYKczqZ-p2wGrd3cPjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
الیور کان در مورد کلوپ و تیم ملی آلمان:
شخصا فکر نمیکنم کار در تیم ملی به آن سادگی که خیلی‌ها تصور می‌کنند باشد. من معتقدم مشکلات خیلی عمیق‌تر هستند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102047" target="_blank">📅 10:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102046">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAFm4Z0YucUaMI-hEu7nIMtAOiJyAipXcN_k25OJPbobt4MBvBxgJYoh5yk9CaPP67S_X_Uq0QHdZANyQMyAyPo62L9t5fdzSk0X1o69eyTcVBMmO4yiT03RyoTgkOnreEQXr-52fPSyhAd7ov8PGIbhM5yLkW_ic0GuI8nRDA1muNmmY4ZhkxrTEH21l-MusEqpBKEzu6DHMCrq7uOTGemYR5opuT9oebzTnImMJfP-yzDfZk8ijpxuEBJ0yQ40Nt4gs4B8p7SzO4lkphU_xnsiIHYa5hfQieiz9HoZpTSiFq6QUe2Gdu3zCG_gxBm8DSbz01mXTfwz5V_ME5Zfag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔴
وینیسیوس جونیور فصل گذشته ۱۴ گل و پاس گل بیشتر از هر مهاجم آرسنال ثبت کرد. او می‌تواند خط حمله قهرمان پریمیرلیگ را فورا یک سطح بالاتر ببرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102046" target="_blank">📅 10:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102045">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U59Tn0Wd97lUosiEOdV_4TnjsB02jcrYNOxvp0RqpuJ0yWOzR7DkbfR2DdNxTiPeXdJks58Q6N6MjZagLKyKWfS_QxM4YqnlyJhMAr1cHsTUZqkRQIq2WnKmCgXay8ZVc4DEeS9fZ5oUQW2yx4lvVrnoIL-XuG7EDVzhV0gzhX2xpEnoNg2BRteT4DUEgIRPAJFXng8UBk42l9GUqUoFKOcGEPSfwcl_BanCtA0EhkfNrgmgS0tfVEql_x-buW51DZ1mNizQW1SAD0SC5Z_M3i3Z7t3kRkOl-qC_pIdfI9yYaSDGj4Y-Eey05gF0AM9sjRzs7iFgICE2UtbHlP3qCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو: پاریسن ژرمن تلاش میکنه بین رودری و رئال مادرید مشکل به وجود بیاره
‼️
🔺
🔻
پاریس از هایجک شدن دیومانده بسیار عصبانیه برا همین با رودری تماس گرفته تا اوضاع رو برای رئال مادرید سخت تر کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/102045" target="_blank">📅 09:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102043">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n1K5l5lU_LQ9dZKDVgGvNyn3vODtzVMrj6r8ndD3eV6YgkUVzKgBJYILHWMGlkVTZuF7DdsbTIH_K-xLawQif3ZlhpUSjd8prsTW3BYrGoTscfAxq-OSNIdtef4eP_8fCSw6fIHJoFFBN6RwDV8KL1gLvz7Z3AIYZEWCdIiARMI8ZlDqxV7Ai6RE_NTu0ho9jnjQNT2hVn95L_IK4qqgPeYOUCGhBklW6Gv2XpmJOW-SIPW2qjwdZYyZvh502LJrVp74F6vTikuPizSN170IKxH1H1ZI-BqxqDMamBQJ__UcwS710sIIh5lqr6FTPNXExtTL15PCwBh6obgQf0awvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/giNP_fFioPk6iaiNpdiisFaujMtPJzfe0k00dlWpjb57Xn1xvWJkxP5kbpxA8oJMkrvi9seyRNUEztTHwpTCAg1rvlX7D5Xe_y8C4MVG_5gzMOoW8FNJrWVbdlZmcQa5JdJ4WrkgCrRNnaVLsIfsMGcN_13eGGNhmHENLz8TlaXCNso5oN_IPP2Zp97G-O6yS8VmsP_xvHT0Fb2oY1p2vCCRj37o4g3V23iSNj72_fmrXxLPHM0FNz8VJbMC3YQsu9frcgaYro4EoqQ0cWvrC3nyNo7LFdHwMrDL0mx8OLGBX-mIBEgNMqEsjcBm7ihImDJdAr7XzgBPCQ_fApqABw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
👀
طبق گزارش رسانه‌های برزیلی؛ نیمار بدون اجازه، کمپ تمرینی سانتوس را ترک کرد و بعد از برگشت هم در تمرینات تیم شرکت نکرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/102043" target="_blank">📅 09:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102042">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-4zbwB77cmPDVf136b74VSQNiM7GWA9HBFeyir_y0yBJuXjZYafopIu4VEI6KqNt_En_JHbsemI0tP_ExjRynYm3K5cpcPl9gEgjgsPyJwMo6uGaFlLL9dvehfpZaX2S81zzXzkcpa-qmSB8dR_I6tQkJMCd3A2x0jSyUEf2wOfeXS6eOS_cbuvOE6InsGfuyZ5JL4761R-b3584JtEoDpX2ONfvI162PYAAQ0lnV93TbgOi5uZXb5qkXKiPa5SV8mv5tm1g4l0YCOBilvMNjC8BE-YtnlQFbDITn4Ai5OH-oQGJjS9pFL9Sq3-DNFZs1HDze0RswnNUnumDTjk4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیکولا شیرا:
رئال مادرید آماده ارائه اولین پیشنهاد به منچسترسیتی برای جذب رودری است.  ارزش اولیه پیشنهاد بین ۵۰ تا ۶۰ میلیون یورو.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/102042" target="_blank">📅 09:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102041">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2Yt3i07b1uKRgKFsI011tEgPs9TxTgFYBYFHLVbhOKJgpm1_2hhFpOD7OXwqPMdHjfA3zLEVcAp0KSxK8WaloLf6wssiKonLN7cKcPitJGqwuZLXSQ2qoy40lom_6fB_WBazD-DhqN7P5HMB0FVyNhE3u0OIeLskpOnEwTiPU3FhzR8IXMotcfN_GNWbWFbfmBcXaTIq68y82XkJJrUJxr4Nis4rEAS86UkfdCjVzeXj-uWJBLi-mRLxnMbQLFaj-FSLax5kJn76FeLR3O0U_vlgvVR0fSqDWg8h7d5ZEeLownbcd01RsjoB0vWw5aaO0ZDfBvt6yJCzv66LwZ20A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚠️
اوه‌اوه یکی جلو فلوریان پلتنبرگ رو بگیره که ریده به سر تا پای رومانو:  حالا که ما را "دروغگو" نامیدید، شما خط قرمز را رد کردید. شما فقط یک روز پس از آن، انتقال رسمی لوزانو به آینتراخت فرانکفورت را اعلام کردید، و با این فرض که هواداران شما احمق هستند،…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/102041" target="_blank">📅 04:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102040">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vcezx6OEWhlt8_gzHdtl8GXrCNCROSkvCGTJTkdDK1mnObdeeQt9jBQwY6CGS8wX_6GIpAZ8zyMv-Pz4KKj2mWiOqvGNSr96rAbHuK8pi3hgatN1hLVuM5Z0_uFueurQ4pCaMWW03gfsxJ3OHxMuP7y_LEZ5oJUYXQ_9daOsiJE1UC1bhwpQK70DIeoMl6GC7joGJnKK6WhArF5A3nZ_4Qdzne8nk_0yWtp60KKXqJDgtpeXsD_MnutpqSbMZ7ulm87mf8Dv9DUUPj4rm2vFrU84ndWq5n6W6Td6O5CrWY8urwTZ-dziSlAr6bAS8_Q9X87DVlQg9Rzlbs7R0QDbFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
❌
🇮🇹
#فوووووری؛ حضور پیرلو به عنوان سرمربی تیم‌ملی ایتالیا بدلیل فعالیت‌های شرط‌بندی وی منتفی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/102040" target="_blank">📅 02:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102039">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCMvNZVm-VlixkUOAQGwPMAYJY6mPGJaAjAfmL6u0SUPLUEf0Hl8-AyN1T03zucKxj-MXr-omYgn4wv9EkH6225bhz8t7kHCMtu8EIlixL7wIaJ0Cwc9uwUrJdLhnAPhOsy9Xga84qLz9VOJSuxXyloh1izFNGU1cV_QknguoiJDUqyg48OYkmiHnMdDXYNGAPt3NrF53Mp61XCqFt3RLric4KGHQmqucnexZq7HJ39VAPCOj6FFKmH6zsdHG5LEEeCVbPgWPOHM3NEbkScptMAuro2mqUdEQHVg4B9kpYSSl5brTs_TtLBWI8AeimZmyFv3Lg6z2-Xt9R_Vi6lRZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
❌
🇮🇹
#فوووووری
؛ حضور پیرلو به عنوان سرمربی تیم‌ملی ایتالیا بدلیل فعالیت‌های شرط‌بندی وی منتفی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/102039" target="_blank">📅 02:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102038">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7p2n9p4TcOVO6xIm8zd4zA5DA44DXG3W4QGVncTHNZGRtf-ysBKEkuFY5Alai01ZsVbLrqRnNyJ2dUp8TdE-qjUYVbIgnWZPrdLUtYUtyaZKNAXHQiQLKRNEKQoMqN61ceu4VEOfrrIIbBSK6uT2NTiNHnjwl7GXalRCgBqSsUDCtXliz0EzeXeHG82B1CuL5ZUIED5zWEpOB4B82nJaMiDpGKj8bnwzZ9Vo6oaJ1Jr_u4VcZ2EKAlMmFUkinofVsfGSH1UuuhigI4WBTZIEo5EXSCKaT3x6JqOGovVScRqm9RgnfBqyN-MMW8mWek1PCRdIeXcEDvzRHCOJ24_Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
ماستانتاتو بازیکن آرژانتینی رئال‌مادرید قراره به صورت قرضی راهی بنفیکا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/102038" target="_blank">📅 02:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102037">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tcL4LJ-2Ddke4D57M1LUsmDTiicLNB6jRFlxmIHNOld2LfTDL22tIS40ZKXzEhyCNPNiRMbXkCWZ5Xqu1sgU8HwB6nyosGBpyTKYm3Zb1BHxEvHd9-dm75ty27e9ouT-AlTALf_EN8mv9FKQ9_AZKL6vEBmCSsl8eUyBGCdC68_EfYCD9rnboEBKBw91j3_pV6vWhy2enajSdbn0lvrura5MQySV4ogGqZWaQlYMXgPH0Uj7BqMjWnOgZc-jSGGAoiC3_9gkq3mMzdaMtXAzQ-SMX-PJabWr7os5SU5Nu2UyTwAXkko2zLg_c6clqwhAc8icKdB9ZNS_omenL5jENw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
جنگ بین خبرنگاران مطرح فوتبال اروپا بالا گرفته به طوری که دیوید اورنشتین گفته پیشنهاد رئال‌مادرید هنوز مورد موافقت لایپزیگ قرار نگرفته و نیاز به زمان داره و به نوعی گفته رومانو فعلا زر مفت زده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/102037" target="_blank">📅 01:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102036">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JQcUSXV_zfRPvqDKh1H4MdVqeuBYYz_1gd79xj1q7t2f9_zZHfzkB3sqdVFJDEXVr16ILV7kLG57NVVIAkbT43ewYlQdrO333ienipbr8HOdRQIkWRw-TCa-V6OksKYV6pQozqmMVmGzPm4HCEhPZ2ozOkrka6EudcFKf4iphg1461_Db_e9VnAOY_YRt8LWgj86noq-D3AFYDEbsa9NvXd3LlESDC-DcLeYtlnkRS-VJIbMhkW17KhezdtKKYKZk_CSREuACwA7trhdrQQ6rXp47YlV79R-xgBhnc7XjrvTlbH6xvVtc0liZZN5Zqbnsnrj0MZsMJxHG7lyaAhvfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
سرخیو والنتین خبرنگار فوتبال اروپا: ژوزه مورینیو به کاماوینگا گفته که فرصت بازی زیادی در فصل‌آینده نداره و بهتره به فکر تیم دیگه‌ای باشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/102036" target="_blank">📅 01:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102035">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vATNtZCKIyBLwwbhr-T1SotiiilxTa7SMwl4crAuwxfkqfLpnfyIjpFowsEFqptB9Ekf6hmByPiwVwual0JwuSfyvOAZQstvQnxdUabptB1ZLX_4OuDoB8s2cAD1acGzOe4AwZ0myZNQkvDtawj0FodQd6nAEmLccXmtR62gudDgRbg7Lm2Vs1Qr-Ksun5fa3cNfzK63OAH24LEqLMq0sHIWarNRe8BCVgmVrjM485hphsT0s8Kpbqp02J2ufHq7DbqBvxF1pFb8R0S9w0lkfEdErsYp6ZWKaPGv9oHRZSAksPEpVBlpwtt6ru1L_0XXW4REQoCPlOUSAp4IG0SHNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
💣
💣
#فوریییییی از رومانو:
🇨🇮
⚪️
یان دیومانده از لایپزیگ به رئال مادرید پیوست. 𝑯𝑬𝑹𝑬 𝑾𝑬 𝑮𝑶!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/102035" target="_blank">📅 01:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102034">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F51vfdA6V_V7pMnES0HtswJXak9QbsY9Q3Hqy0Ao1UTBo1LWxgkzl62Ap88-lj5WAfr8sebfHHRjSzvLS0Gnv4MJ1oSIR8uc89ZuetWTgks4GsaN6NdMW-NgBsYS3vyaEMK4nXZHnw33WtAvdTd0GLYNMmc70wCPKfTyRpLO-GQLEOuauGOBm1jJLWSZWL6ilJ1lAKqENVolHtD0eLHCt6BtfrP6Hg9A6VtALpEt-AtCiKN5wl8Yl7B8czNM3GDrIHP6Rd5B35EQ2wAkoMu5AJ1JoFVuUjtdJAiFtbCWjFIK0T1tJdPH5acz731RCxtDvbSU0bmJr7VnC9TH7_8Vvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
تلگراف:
مدیرای آرسنال معتقدن وینیسیوس جونیور همون بازیکنیه که میتونن باهاش چمپیونزلیگ بگیرن و هرچی واسش خرج کنن ارزش داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/102034" target="_blank">📅 00:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102033">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fda4a57b7.mp4?token=UvizsZ-zjbcbt5OBOM6S-IsKgoAx41aPnkUbJOu0YtHC2g9rerfilWmLWaVIKMdzJNx-lXKjcDHHdNbsxb9M1u2sQZT_ebacjDFKBeX1L-4vVcBD1BUyC8Z5wtoxYvcMA83A7KTN0XlE0fKT76EMcG2y7-qpcDRSk7RVNXcO34lMNCDwd6YxTuOIJR-IvXOCV_9n7pamWYGSnd6DuZzXbELxAFr6eN-4MLjNVeRQVbBEHQ_JtQ7Jli6cxeSoFUBe4uPxcBTCtXxAQJhuOyWlQ_9NoNBunLZXBLtzQIkUEnrPIX4JkwnpUZRB11z4wvMdl60wrQPHYzkDn0wURSQa9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fda4a57b7.mp4?token=UvizsZ-zjbcbt5OBOM6S-IsKgoAx41aPnkUbJOu0YtHC2g9rerfilWmLWaVIKMdzJNx-lXKjcDHHdNbsxb9M1u2sQZT_ebacjDFKBeX1L-4vVcBD1BUyC8Z5wtoxYvcMA83A7KTN0XlE0fKT76EMcG2y7-qpcDRSk7RVNXcO34lMNCDwd6YxTuOIJR-IvXOCV_9n7pamWYGSnd6DuZzXbELxAFr6eN-4MLjNVeRQVbBEHQ_JtQ7Jli6cxeSoFUBe4uPxcBTCtXxAQJhuOyWlQ_9NoNBunLZXBLtzQIkUEnrPIX4JkwnpUZRB11z4wvMdl60wrQPHYzkDn0wURSQa9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
وضعیت این‌روزهای لیونل‌مسی در تعطیلات:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/102033" target="_blank">📅 23:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102032">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLJQXvW_MssYNKlxhCZn4glggFhD8HtB0XQjDnnPIHNa9DeEj4z4xFifCeAWIlnlo7tmnKs_0dHvRJuNBOosyqCjpTGeYFEuSFWFSnM3Ky9LjF0odC_26pyLXQk3C8Wotp6iEiJfMHdh5t5_5BXJ6LfAdPClUlBIEBCfRn3xvuvBnBY6azfs4ZDRylGtBZhnq-fdzSTzrrvezUHAudEM7ytXJkm90Kc3VhRmK7Oy1dLR4K50R_hJHPdSygnKP2dRqsauguI3WfNN3lnEPINadwocjTOOCC43VhAgCljtuD-mTRtnFkaKe3OIK8j-n1sCI39_VC-z4GU3Dv3LavOLFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📮
🇮🇹
دیس فلوریان پلتنبرگ به رومانو: بعضیا همیشه میخوان اول باشن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/102032" target="_blank">📅 23:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102031">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhURftBPdISA143DjWSlebzi1tI88QPeRoRsOAS_WqkIuz6wAdYULh-W9WzRKe4hi3nOrDoNTahe1NavGbNKeGkNk6NqbTMs3WSZYJEV4M5sLyfIdkfeTZvZyeZLOJQYrfj1NAT0B5lxE8dAu48zx_u8atXaQjTEdkAGkeL98hJzWKFFJd9d411x8w2n2eDvD9qg7HrQoi-ApXhlNqjhFMPwimTgcmRFdOygXHXY4_pekqXcsiLj4SnEu_soRdPAQDB7j_609Tod3yiEaICYmsJtq8AkL9w-yQpVuzUpCM4yXRZMOqlEX-fi-jR7R7O9Mxi0RQHIKN3VyZMVEZNVGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😐
فلوریان پلتنبرگ اصرار داره که هنوز هیچ توافقی (حتی توافقی اولیه) بین لایپزیگ و رئال مادرید حاصل نشده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102031" target="_blank">📅 23:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102030">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
💣
💣
#فوریییییی از رومانو:
🇨🇮
⚪️
یان دیومانده از لایپزیگ به رئال مادرید پیوست. 𝑯𝑬𝑹𝑬 𝑾𝑬 𝑮𝑶!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/102030" target="_blank">📅 23:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102029">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e020f6fb8a.mp4?token=Mnil1iSBs-VzekGPPx8zePMUUAExGr_6k-5h6gmJQqs8FsSKmW7zeiQOH6tS9pmq5MniACtIy7nXH7DENszC0nleyUQNbJ2afFfs7cLd8KSW6Hyn1PCpNvEkbL4fpO_yfa5U6LW0phcrQWmC_RBgDb5oqGUPDZCkufTISqY1G4OHHBHGZ60Z5Xcj17OMcutAj-IelQzUdPm_6pHIscKuYFp4aBsz46_dnTT-MJQsbWCgmskJ2ZNgsBu2TR5MEFtjHs8mv-n6ax-XJ3TzYoe9p0sYt1GMKRoNuLOryh73FhTTtV3UsquoutWtOenXEyu6kKTQBxRvTAaul1z_XKJQUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e020f6fb8a.mp4?token=Mnil1iSBs-VzekGPPx8zePMUUAExGr_6k-5h6gmJQqs8FsSKmW7zeiQOH6tS9pmq5MniACtIy7nXH7DENszC0nleyUQNbJ2afFfs7cLd8KSW6Hyn1PCpNvEkbL4fpO_yfa5U6LW0phcrQWmC_RBgDb5oqGUPDZCkufTISqY1G4OHHBHGZ60Z5Xcj17OMcutAj-IelQzUdPm_6pHIscKuYFp4aBsz46_dnTT-MJQsbWCgmskJ2ZNgsBu2TR5MEFtjHs8mv-n6ax-XJ3TzYoe9p0sYt1GMKRoNuLOryh73FhTTtV3UsquoutWtOenXEyu6kKTQBxRvTAaul1z_XKJQUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسطوره فوتبال مملکت علی‌آقا دایی
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/102029" target="_blank">📅 23:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102028">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWZyy8aI2KcPUMuvjdPCXoIoeNRNYt9BWq1vPVipaMjZbknHHrg1SggJHQqsk6K2u5k8frrJW5M_tD7VFvBd3kf4Kim8uuJA7mTkz3_f0soCeX28_6l7QEcAUQ6KCkyXAgGFieTWyd4-cLUFkDUwYRmRl8MNKD7NJbowdXPNSzmoRH3GC21HaYTRWlbt0KQtti4TrQcksR9gVd3i1IxXGrRjvUkb_OJJPlO8WgRP_8rtEUP4TmXeg2LR5rjg76Ib-4r7tRSldJhZW4rCTVaQZeugfUEUbT2F3_0Pue2bhMGOJlvIGcNrKyEbS2lx5CHgX2Y3DVP6d5Kbi8Znl5yV4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
👀
رومانو:
🔺
خرید دیومانده بیش از 100 میلیون یورو برای رئال مادرید آب خورد.
🔺
مدت قراردادش هم تا سال 2031 هست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102028" target="_blank">📅 22:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102027">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEYKb0W7cInTol4Zik2kiyJJO8BKxHJsejspFIeFXcSv3e4mvjZglrBLVV67-sENLhbNYEtkHzIz5NnvfJfdRVUGtnsRXKv7fR1QMD78AlFFW8OOY183VJm7TXFkKmhR_k2Hb67dtp3DeIkJHBPtFt8llcS7oV9vSdPunXRoqacD_0SHPYZKhlAVNifBuHX_Ry3HOE0yj6--pEzBWaXuAGR05GuSx2OX4k0xZsoPHIekefH2LxOEJhRKwVgaJB8Yu0JAJr0cXrr8Y4PLmSJ0cJLRDjwjxFzMjQXcU7HEDr77LX_tILjuZGAEhbVCaV0ZbYd2x0EaX9rFeswOgHHNdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهکار پرز:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102027" target="_blank">📅 22:35 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

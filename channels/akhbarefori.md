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
<img src="https://cdn4.telesco.pe/file/Ps-Lj4siS2NW9JMPFU7CIEXdxb3Q91K0zBsXb-KFCuNPH09DCoNifX2ycnGuDe_RsweuG7gp57CmyJVKN2Exq-omU_RFn1ROC2WPjZSVM72y9tCYYPamNBFzu8eoSssOy3aI1RbdCvy6BFDkg3t2SX-jV09RW_a41Iz67J11xwgYeAfFI5jrGX9_mfYpk-EtDs_2eVQYQTTFuib4Kr_En4357Jw1S_bzEe2WllecsLIwGq-h0L3HmynaYUE4eX8PnhFPp-pGJFCDBIQdxbzPts7WijDpBIt8OKu0atA3QJHdVkc0qB8zBKqS95wvhzrSCSWGOFXxC2A2iZg7slvNSw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.32M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 00:16:33</div>
<hr>

<div class="tg-post" id="msg-688343">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6414c4663b.mp4?token=BR94xrbt29MSm9dFtMFotLWaA2a2Ic_eCwP7hp7QEjgPSTjyq_d8LKbfYblHQlEcm43AlYCwJNBowEAoOD8oLxKXA1cGclBSpnRwegiWlWFZtPsHyZ65ElV_aeLa4Dh-puaTnj1gu2Y2Y7geTF--m_Hz92at9BBEjsGCeYRwGY-ZraD1M3V0iioTxRofWGwL2EzoHV8eE7fy0DEtkM6Np78CQjNjHbnVQXMOqCtAowi9IraEcgCrEPRekyGRhlImXZM9BfIepcY3JxOnu-2v2BzWJDBMNMXcFxwWlrOTl9kGK-e6HV5RpAEbuvLEaM8d4yjQdH97TbeufkNn1ny7K0qR6RwBkdKJHRBCdvpZEm1rH3VA2gUOOECnfZpkFXtZ2F_Jtbciy2v28aAjteEUvqAKio5oAHOTTk_u9IrVdtH3i3oZ57lWlN-dxVwPS9X2IUABxb5KfVtJmWBXA9FbV0KLcst9k33tVCL82MykVoGQqVnYsTf9SPBwVxOpHuM_FdizTiRxrUiYeglV55GwKQQj1WG68ChNUoJgreS6pY9_Om88_gmG-42PjFqE_kOoJstnWtDRQmcA8gTzQBNRgmrvVi3RtmQkPNcQ9sSTzNZKHWeUZxfEOhexbHBNyckrMCRoq4_ENtrmdDdZ66Dr8ugI-BLlvymFEsUtIUCVVPo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6414c4663b.mp4?token=BR94xrbt29MSm9dFtMFotLWaA2a2Ic_eCwP7hp7QEjgPSTjyq_d8LKbfYblHQlEcm43AlYCwJNBowEAoOD8oLxKXA1cGclBSpnRwegiWlWFZtPsHyZ65ElV_aeLa4Dh-puaTnj1gu2Y2Y7geTF--m_Hz92at9BBEjsGCeYRwGY-ZraD1M3V0iioTxRofWGwL2EzoHV8eE7fy0DEtkM6Np78CQjNjHbnVQXMOqCtAowi9IraEcgCrEPRekyGRhlImXZM9BfIepcY3JxOnu-2v2BzWJDBMNMXcFxwWlrOTl9kGK-e6HV5RpAEbuvLEaM8d4yjQdH97TbeufkNn1ny7K0qR6RwBkdKJHRBCdvpZEm1rH3VA2gUOOECnfZpkFXtZ2F_Jtbciy2v28aAjteEUvqAKio5oAHOTTk_u9IrVdtH3i3oZ57lWlN-dxVwPS9X2IUABxb5KfVtJmWBXA9FbV0KLcst9k33tVCL82MykVoGQqVnYsTf9SPBwVxOpHuM_FdizTiRxrUiYeglV55GwKQQj1WG68ChNUoJgreS6pY9_Om88_gmG-42PjFqE_kOoJstnWtDRQmcA8gTzQBNRgmrvVi3RtmQkPNcQ9sSTzNZKHWeUZxfEOhexbHBNyckrMCRoq4_ENtrmdDdZ66Dr8ugI-BLlvymFEsUtIUCVVPo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آرامش و زیبایی در دل کوهستان زاگرس
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/akhbarefori/688343" target="_blank">📅 00:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688342">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTqK7lp0H7j0xc1nIhoZyHs8LVCzETGUi5557TSOjbIrUbIdyqPPxnnoXbw70yXu-XPCl2QyjcMT6schcvELmd6O9QchBWknL6hGFWQg0ekDzJTbWAPhWaB16TuXis3I2PFpE4_UV9qp0hBuDzFT8LjJX-1Ly-xU3Y-jmH0QkQX2p5SxOx68lOxdbrBhKe8Oiq2-jcWK4B3Xw84fxPkNeKpcZX_7cz7udxT7qzLKfnuGTsORm5MjIOkxZq5HVqbT8w3hjN7B-n2csZcrZygnbFFOrwSrROnOsjS6YHtem2vbsMitN5P-8LpLSNUn4FnZ6SVgKMo3-LZ7cFN07tYE1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توییت رئیس کمیسیون‌ امنیت‌ ملی‌ مجلس: وضعیت آمریکایی‌ها در انتظار پایین آمدن قیمت سوخت بعد از هزارمین اعلام پیروزی ترامپ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/akhbarefori/688342" target="_blank">📅 00:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688341">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1JtQAlt7XbKof1Gk7bMm7lkAvw8DxmIrYhCxBKr65mAA7b3yYch74ml3zxudL_WRVMahobDLUpPjEESDu8Q30RXb2S_DIANSP_InowMLOui4hG0lfKpzlNknSIYKNervNQC4sqXe9xGbsMnjxQ8ef0fzsP9B_bwfmjV3g-Dl3WG0PSCuVkMcYUS_qq3gDKLN-Q0A_ZLgO-MGM-6bJD500-yHPJiK3Z2N9vsKpDZ4lGTqN7q_JIZZ3QGNUxaGMFDBI6O1eeJuhgUkLslH6ILO7KwVS0VCIpDBbVDQEJW7IPElMgZ84COThxkBVGZwXZ0pvRCxquNNgBp5Kx4LtupbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازتاب صید گران‌قیمت نیروهای مسلح از خلیج‌فارس رسانه مطرح روسی‌زبان
راشاتودی:
🔹
زیردریایی ۲.۵ میلیون دلاری پنتاگون در نزدیکی تنگه هرمز توسط ایران توقیف شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/akhbarefori/688341" target="_blank">📅 00:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688340">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/570e8110a3.mp4?token=hVXObO5FSBu1dh-M5KO1U7KjeSXsQQAAY-LIqKYKlHu5YOpV__Z0FnY0VPDNMNNlAGRe8eqOwpiEuJrBCtNqdrpwEngdcXZCyoYqonD5thPWVUnqdWYsPuCw2aNvC6u56gtwqtuOp9pTuO8onqQEgSBUSdG6NCuxkkHDbNeGVOit-vDqbpyWmAsaebBT4IaKUEqXMKkhZmt4Qt1W81yrv9k0c3AP-GjSeVuTTECydyaOjzxSA9JpYRYqWe_iRanK6UEpEr8MJTXhxBZGz8Q2a_LDJZeI4pwxqf1K_j0AyTgtHTmqCV3m5_fLBQpg8r3ZXPPJx3i75sT5EyGymNDvCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/570e8110a3.mp4?token=hVXObO5FSBu1dh-M5KO1U7KjeSXsQQAAY-LIqKYKlHu5YOpV__Z0FnY0VPDNMNNlAGRe8eqOwpiEuJrBCtNqdrpwEngdcXZCyoYqonD5thPWVUnqdWYsPuCw2aNvC6u56gtwqtuOp9pTuO8onqQEgSBUSdG6NCuxkkHDbNeGVOit-vDqbpyWmAsaebBT4IaKUEqXMKkhZmt4Qt1W81yrv9k0c3AP-GjSeVuTTECydyaOjzxSA9JpYRYqWe_iRanK6UEpEr8MJTXhxBZGz8Q2a_LDJZeI4pwxqf1K_j0AyTgtHTmqCV3m5_fLBQpg8r3ZXPPJx3i75sT5EyGymNDvCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💡
چراغ قوه ۸ کاره  LED TORCH
💳
868 هزار تومان
🏠
پرداخت درب منزل
❇️
۳ روز ضمانت تست و تعویض
خرید سریع:
http://istgaharzoni.sabzgostarr.ir/FastCart/smscart/5872</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/akhbarefori/688340" target="_blank">📅 00:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688339">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پشت پرده تلاش تندروها در مجلس برای استیضاح وزیر ارتباطات؛ ستار هاشمی بزرگترین سد در برابر اجرای «طرح صیانت» توسط تندرو ها!
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/688339" target="_blank">📅 00:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688338">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tg9mBLoCWlbTYYWxLieTbSuTCkEXKMv08kjojfDlazyYsz3SqSfmo2Yv6-Mbkf7LpgdVET9ut7ldbYuVvwFRvp_x66tCb299c1UKIMsOBDnPU12K-ntZTVvmVg7ikxBscyOroCNAnyM5ZfaCUpy3-GdihK9-eKalnyfzU9jqY9_b6Gw5Km8PmDklRsbTu9Mu4NV866SgTDIANiIZGvDRJaQ18LYZtkSV8D1KpHmZa82GF478-n9ZWthJpn3QvdofhtUsKo6sHkBWKsKDZWjYHxNJLa7MZep7uZnLosv5yms2lvs54NnGxgpYU9ldoiNHwNadUKnrwJMGe3VI2eABig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/akhbarefori/688338" target="_blank">📅 00:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688337">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbUYlBaJPdslCW2VGrEY95Uky2m-1BRmGKzzpDhFDPgcXfz8Axx2g5AV3-k826cOVKUmpYpAVxN-QlLt6M_5SZdLxsDLmwx3zCg90d760F5PZdjPwQ_WQOEqZ1cd6vhkB6-Lr5UPm1Scu2VAGUKO5-UgJHEtslf6-3GbAejR2-lHx-cKI1HSD2NHObt-JvC66OArayNqha2IexdGNbJ9D6L0kI3LiPOkKEAOQwGUSAEBVAhtDMr-PTJv9tDvhM1kVzN0XTtkZ-WxT9_FHhC7CAlkBAUVCsSTcKGAh_j-b1Dk1G3y6GhbYuE89HbODIg3MAMKXMCMToV7ykXkMkmDvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بله آقای ترامپ، نیروی دریایی ایران در قعر آب‌های خلیج فارس است؛ منتظر شکار ارتش متکبر و پوشالی آمریکا
🔹
Yes, Mr. Trump, Iran’s Navy is deep beneath the waters of the Persian Gulf, waiting to hunt America’s arrogant, hollow military.
به توییتر خبرفوری بپیوندید
👇
https://x.com/akhbare_fori/status/2095856638485839910?s=46</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/688337" target="_blank">📅 23:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688336">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/206796ec3e.mp4?token=gEmNIf4wsG-e6-FM5-dvBBWAuavpV0MtAZvQjZFyWYs9QMJvne1ve39nZCFwMpXAcy45dYMsdygkyh0ZYvNzdkxp95FX5aAhi97yR-byAb5FhdgKXGEFCWnivtYmA7y3c1nPLxu5aNH5GATOnPyuCgvytkhMTfG8S9KshFGX0nYYKv3YgTtxGWCO6VW4CZs-IccGTAgy-VMppbv_PtXzHzYk5r7l8ziNWYxoTXtfk0c73N_mXtW08mRgh1KjwoYeMpjnG7fOy4L4oKdC93S8fF6uGeMI3E3L6Ur53qx_3kgjrdM-0Ryyl3p5tpZURWveOcUTTCPhFy0Nsm2JvFvH2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/206796ec3e.mp4?token=gEmNIf4wsG-e6-FM5-dvBBWAuavpV0MtAZvQjZFyWYs9QMJvne1ve39nZCFwMpXAcy45dYMsdygkyh0ZYvNzdkxp95FX5aAhi97yR-byAb5FhdgKXGEFCWnivtYmA7y3c1nPLxu5aNH5GATOnPyuCgvytkhMTfG8S9KshFGX0nYYKv3YgTtxGWCO6VW4CZs-IccGTAgy-VMppbv_PtXzHzYk5r7l8ziNWYxoTXtfk0c73N_mXtW08mRgh1KjwoYeMpjnG7fOy4L4oKdC93S8fF6uGeMI3E3L6Ur53qx_3kgjrdM-0Ryyl3p5tpZURWveOcUTTCPhFy0Nsm2JvFvH2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جزئیات عرضه اولیه اوراق سلف موازی استاندارد سکه
🔹
عرضه اولیه اوراق سلف موازی استاندارد سکه بانک مرکزی با نماد «عسکه ۲» از ۱۸ شهریور در بورس کالا انجام می‌شود. این عرضه شامل معادل ۱۰۰ هزار قطعه سکه تمام بهار آزادی در قالب ۱۰۰ میلیون ورقه است و به روش حراج تک‌قیمتی انجام خواهد شد.
🔹
دامنه نوسان روز عرضه ۵ درصد و دامنه نوسان معاملات ثانویه ۱۰ درصد است. معاملات ثانویه نیز از ۲۱ شهریور تا ۱۸ آذر ادامه خواهد داشت. خریداران می‌توانند با کد بورسی در این عرضه مشارکت کنند./فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/688336" target="_blank">📅 23:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688335">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WI-d_ZRBAafMOdmltF-OZp6h8a1FNgb6sHaN-vucUY_xZwd1I7Evt3sBJr5b-tCBXBmNXjxzKhf5S4dt84AqIBA-3dd7sxI4L_1zFqkG-T6T1b6tOmDz52j-HHL_f51-IWDOPrddeaH-eVucfQZRH1EcNsc8LnVRTkN9fYKlC5i0xRjU9d9z8Xmtx_njI97OCOnhakjIgiCiD4iV6d0PVpQugHQxqXndy5aa3eeVJe879m-DclU-AA2vA-4DceB-yiLtQ757PoRNoAAKLK55eFX9E42ZBaZv1-wNXkXXVRgYkdiy_F83vOigMnbVO5HQPZ4bvGcv_ivDOrw9Ts1ruA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تنها یک دلار تا نفت ۱۰۰ دلاری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/688335" target="_blank">📅 23:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688334">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ذخایر خون مطلوب گزارش شد
عمر علیپور اقدم، عضو کمیسیون بهداشت و درمان مجلس در
#گفتگو
با خبرفوری:
🔹
از جنگ رمضان تاکنون بیمارستان‌ها، اورژانس، هلال‌احمر و سایر دستگاه‌های خدمات‌رسان در حالت آماده‌باش کامل قرار دارند.
🔹
از نظر ذخایر خون نیز وضعیت مطلوبی داریم و با کمک مردم تاکنون کمبودی احساس نشده است.
🔹
همه دستگاه‌های خدمات‌رسان پای کار هستند و برای حوادث احتمالی آینده نیز آمادگی کامل دارند و بنابراین جای هیچ‌گونه نگرانی وجود ندارد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/688334" target="_blank">📅 23:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688333">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
حمله به دومین شناور در اطراف جزیره خارک/ هنوز اطلاعات دقیقی از شناور در دست نیست/ دانشجو
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/688333" target="_blank">📅 23:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688332">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
تایید حمله آمریکا به نفتکش ایرانی/فاکس‌نیوز به نقل از منابع آمریکایی: نفت‌کش‌های ایرانی را در نزدیکی خارک و جاسک هدف قرار دادیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/688332" target="_blank">📅 23:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688331">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
احتمال استیضاح ترامپ/ سناتور آمریکایی: اگر جمهوری‌خواهان مجلس نمایندگان را حفظ نکنند، ترامپ استیضاح خواهد شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/688331" target="_blank">📅 23:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688330">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
سپاه یک زیردریایی بدون سرنشین dive-LD آمریکا را به غنیمت گرفت/ سنتکام بیانیه داد
👇
khabarfoori.com/fa/tiny/news-3243787
🔹
هدف گیری یک نفتکش ایرانی در نزدیکی جزیره خارگ
👇
khabarfoori.com/fa/tiny/news-3243816
🔹
روضه‌خوانی فرزند آیت‌الله مجتبی خامنه‌ای برای مادرش و بی تابی برای رهبر شهید
👇
khabarfoori.com/fa/tiny/news-3243644
🔹
این مداح گم شده است!
👇
khabarfoori.com/fa/tiny/news-3243800
🔹
تصویری از وضعیت جسمانی نامناسب علی اکبر ولایتی
👇
khabarfoori.com/fa/tiny/news-3243638
🔹
صفحه ویژه اخبار پربازدید وبسایت خبرفوری را اینجا کلیک کنید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/688330" target="_blank">📅 23:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688329">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6ax8r96VPSFT2A53X64h2Z_K8RoIS5GWxra59bhUSsX5dHYTo0UBnHGPb9Gxhc9e4uxynFsxw4KQC6mZP96MFM57trkvoNaXPhXnAZISKCSvKTU0FftqCaHu0Lm5XahbuWyBgkzhht41X69G5pEELr5vqBSlpsEZtrcPYxBOwWROcAKP1ZHXODHItZLJmt2FfgEuoGiSbHt15z632np4VBe3NnbvaVtOrE-HgJ883iH7eNFaF5lU1-dSoFGTItNQq1zZSFkVe4k6rdM3k5QfuBb9AANvMOpk4quW_l8hywgTtUCIWJwfd5DYumohUqw5s6oqE3rk-ZGiDBU9stUGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فتحی: رسایی باید حد ادب را نگه دارد
محسن فتحی نماینده مجلس:
🔹
جلسه تبادل نظر نمایندگان که شب گذشته در حرم عبدالعظیم حسنی برگزار شد، موثر و مفید بود و نمایندگان در خصوص مهمترین مسائل کشور بویژه شرایط اقتصادی مردم تبادل نظر کردند.
🔹
متاسفانه از توهین آقای رسایی به همکاران محترم متعجب شدم؛ ایشان باید در گفتارش حد ادب را نگه دارد.
🔹
وقتی جلسه‌ای با استقبال همکاران و با حضور ۲۰۰ نفر از نمایندگان مردم تشکیل می‌شود باید از این فرصت استفاده کرد و به نفع مردم و کشور قدم برداشت نه اینکه با نقار، توصیه‌های رهبر شهید و رهبر معظم انقلاب در خصوص لزوم رعایت وحدت و همدلی و انسجام را زیر سوال برد./ ایلنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/688329" target="_blank">📅 23:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688327">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gv_7wEJQUPbnSmzk9pxmf3umQB0iycG8lNhAwOk-YTpSk2igVw04TRenefJ0Zps4tA5STMJifttZJxcAjRn8lfLKgGdN-dbgz7HHNx-grBzmsomJVqCl7hpJzg3Y7IFdMCq2Tc0ecs6TEyxBVblwxXJdL5jqe3r_fVRZ16Arq9BdhlGiWXpa45B_EzYlM8FWxbAVev5az3LpBWsl5bbUph322AlwhdS-G6hQHzcXlZNrBLC53hgRBGbusUMSvVTaU1qID4Hz3THLjcCGwY4tfyciM8k3rC6qrHLrG5SJFNlBmvSKK4IMm43Qj9LVucW_865p-dnDxgqxiRlVMOfB7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار فوری نیروی دریایی سپاه در پاسخ به اقدام بزدلانه ارتش تروریستی امریکا در حمله به نفتکش‌های جمهوری اسلامی ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/688327" target="_blank">📅 23:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688326">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
منشا صداهای شنیده شده در جاسک از روی دریا است
🔹
ساعتی پیش صدای انفجارهایی در شهرستان جاسک شنیده شد که طبق اعلام استانداری هرمزگان، منشأ این صداها مربوط به اتفاقاتی در دریا است و اتفاقی در سطح شهرستان رخ نداده است./ مهر
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/688326" target="_blank">📅 23:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688325">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
وقوع چند انفجار در آرامکو  فایننشال تایمز:
🔹
پالایشگاه جیزان با ظرفیت ۴۰۰ هزار بشکه در روز هفته‌هاست به‌دلیل حملات از مدار خارج شده و حمله جدید، بازگشت آن به فعالیت کامل را دشوارتر کرده است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/688325" target="_blank">📅 23:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688324">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
المیادین: عربستان ظرف سه روز بیش از ۱۳۵ حمله هوایی علیه یمن انجام داده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/688324" target="_blank">📅 23:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688323">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
حمله موشکی آمریکا به یک نفتکش ایرانی در نزدیکی جزیره خارگ
🔹
یک نفتکش کوچک ایرانی در فاصله ۴ مایلی جزیره خارگ، هدف حمله موشکی ارتش تروریستی آمریکا قرار گرفت. این نفتکش در محدوده لنگرگاه جزیره خارگ مورد اصابت پرتابه نیروهای آمریکایی واقع شد.
🔹
منابع محلی اعلام…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/688323" target="_blank">📅 23:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688322">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ذخایر سوخت مایع نیروگاه‌ها افزایش پیدا کرد
آرش نجفی، رئیس کمیسیون انرژی اتاق بازرگانی ایران در
#گفتگو
با خبرفوری:
🔹
قطعی برق در زمستان به میزان سوخت مایع بستگی دارد، زیرا شرکت پخش و پالایش فرآورده‌های نفتی ذخایر سوخت مایع نیروگاه‌ها را به سه ماه افزایش داده است، اما اگر سوخت مایع کافی نباشد یا استفاده از مازوت باعث اختلال فنی شود، ممکن است با قطعی برق مواجه شویم.
🔹
با توجه به پیش‌بینی پاییز و زمستان سرد نگرانی اصلی ما از اواخر بهمن و اسفند است که هوا گرم می‌شود و این گرما تا تابستان ادامه خواهد یافت، بنابراین باید برای مدیریت مصرف در ماه‌های گرم سال نیز برنامه‌ریزی کنیم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/688322" target="_blank">📅 23:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688321">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
شانس جنگ گسترده بین ایران، آمریکا و اسرائیل چقدر است؟ / این نقطه، محور اصلی درگیری واشنگتن و تهران خواهد بود
یک کارشناس مسائل سیاسی در گفتگو با خبرفوری:
🔹
واشنگتن پس از ناکامی در دستیابی به اهداف نظامی خود، فشار اقتصادی و تهدید نظامی را همزمان دنبال می‌کند.
مشروح گفتگو را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3242652</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/688321" target="_blank">📅 23:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688320">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
حمله موشکی آمریکا به یک نفتکش ایرانی در نزدیکی جزیره خارگ
🔹
یک نفتکش کوچک ایرانی در فاصله ۴ مایلی جزیره خارگ، هدف حمله موشکی ارتش تروریستی آمریکا قرار گرفت. این نفتکش در محدوده لنگرگاه جزیره خارگ مورد اصابت پرتابه نیروهای آمریکایی واقع شد.
🔹
منابع محلی اعلام…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/688320" target="_blank">📅 23:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688319">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/829194f886.mp4?token=Cb5H8LGlm_cubbWntssUzf2KJu4XUONq7a41gH4F1C1DhC4wtFd5-BfrWPS1lsgQlxt-ldo4rQHVif5E0HrZvEqGn77TvyJ0HXDAeCmBMwIstNySsHTymCsuxm2mkLrZUgL6K0RcFsC2U4pyUj9Zu5e4rNlh4RH68ZLkKEFvIuTzTmWa15rsJWUawhzCI50vYsFu8ct6ypQeIEYG9b-HHoLYfBOJjdg7pmV4pSSCaZ6yHYnlaUOfKbG03aPBCvRRmVq7TxRLNUghG0AjXFvcoCCIzYDVQznKoDaHLFvCmkfRVt2TXvQJPF-t0UoqSAcRsjR-lbMwotHhSXpXurpYz1F0R2W9w9Pp5K1rQzHfGqVeZN0_xwPBcpJzunb8zhxQDkksU_IhJ0SvGoAdA6J8Bl33eJqOik5wrSKhZa6yZYkiFOjwZprXzPKQbuqGI2e7iYI9ftqekjbUeC2UIenXo4LQ2W_VGSoF4o25JMsaqBWo-zWBTXhgqh9fUelwKxIkJ4dXv3zmFplR-rN55ULEUGGWBFWpPrpIpmK8H41TpthAn8ke8qJwpd2QZqTWI-ayZc08HZKjCvwwl4yK6sMg3GvbwoXUKzqAHRt6l53ap_btJV21IhDaaTE99mg0_N63mZcw3Zm3qk4s7DVCkFNUOuUdjAf9uhA9jFEogG9FHSY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/829194f886.mp4?token=Cb5H8LGlm_cubbWntssUzf2KJu4XUONq7a41gH4F1C1DhC4wtFd5-BfrWPS1lsgQlxt-ldo4rQHVif5E0HrZvEqGn77TvyJ0HXDAeCmBMwIstNySsHTymCsuxm2mkLrZUgL6K0RcFsC2U4pyUj9Zu5e4rNlh4RH68ZLkKEFvIuTzTmWa15rsJWUawhzCI50vYsFu8ct6ypQeIEYG9b-HHoLYfBOJjdg7pmV4pSSCaZ6yHYnlaUOfKbG03aPBCvRRmVq7TxRLNUghG0AjXFvcoCCIzYDVQznKoDaHLFvCmkfRVt2TXvQJPF-t0UoqSAcRsjR-lbMwotHhSXpXurpYz1F0R2W9w9Pp5K1rQzHfGqVeZN0_xwPBcpJzunb8zhxQDkksU_IhJ0SvGoAdA6J8Bl33eJqOik5wrSKhZa6yZYkiFOjwZprXzPKQbuqGI2e7iYI9ftqekjbUeC2UIenXo4LQ2W_VGSoF4o25JMsaqBWo-zWBTXhgqh9fUelwKxIkJ4dXv3zmFplR-rN55ULEUGGWBFWpPrpIpmK8H41TpthAn8ke8qJwpd2QZqTWI-ayZc08HZKjCvwwl4yK6sMg3GvbwoXUKzqAHRt6l53ap_btJV21IhDaaTE99mg0_N63mZcw3Zm3qk4s7DVCkFNUOuUdjAf9uhA9jFEogG9FHSY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای استانی که سه‌برابرِ نیازِ خود سوخت تولید می‌کند اما بنزین در خارج از آن راحت‌تر پیدا می‌شود!
/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/688319" target="_blank">📅 23:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688318">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3GkEKEG8DB3kHaypqjNSUBEoaHrtWHhleSoUniPCIXEMnkwERGS-a1mGrwKVWC51AlJmiFGxEdBq3QlrMkEHXRcjgUH4uakqSVn5vGuMqhF4noAQWN45jx2iNt2KzsbqXqlbtlL_ZkxRbHt63g0LF0YsIgMd5UgqJpy21fNgudcgm_JF4P5fTatK4zvNkSfPU7WINJJV_NZ4jOibP7kL7aFb7wXBDDG9ZDA6vijW9SJgaK0qrAzAZYfw2wSagmKZYzMsyjSFL4q-Ho521eOqsHqdMiV1EwGF1SCeakWEVkWUR82wmJLgaPCV4IVla0YlqGhOvJhtum3-nGP6wOj2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبل از اینکه یک حادثه هزینه سنگینی روی دستتان بگذارد، خانه‌تان را با «جام آسیا» بیمه کنید
آتش‌سوزی، زلزله، انفجار، سرقت، ترکیدگی لوله آب از خطراتی هستند که می‌توانند به خانه و اثاثیه شما خسارت وارد کنند.
🛡️
طرح جام آسیا؛ بیمه جان و مال
با پوشش‌های متنوع و
۵ بسته بیمه‌ای
، متناسب با نیاز و شرایط شما.
از سرمایه‌ای که برایش سال‌ها زحمت کشیده‌اید، امروز محافظت کنید
📲
برای مشاوره، استعلام و خرید بیمه جام آسیا کلیک کنید
👇
👇
https://online-li.bimehasia.ir/issue/jaam
https://online-li.bimehasia.ir/issue/jaam</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/688318" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688317">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYUsf03JPWZQ90P_vTzemf5UMZnMqS4YDpE07ktV6OM1NoNrE6G9HYZHJxqvAHOpTEMc-P0Ep8Z9ooXwpsACgVbPfKKkqULuFmbyFAh_cfFV9Zlonmb0JWoKw71qHVpfDmn0tsu7Oj2ryE3fW2lz9OByjKdvpZYZ-xJoIVYVLbS6Um6bK1peHMbvsJDCGvl0HcWybrbiHNbZCAR2D9kL8tx0kT71pX5Qamlb5cJ0z11NaLIqifgVFaE6wwJE3TtD6Oh4M3L-smr5eFj5aR11Ic5MmBrKhWE5TCT4Q4vbkh_NJVq2xv6r5WC7xoyYzaKkgmPkQ2tE2RI36iUpqHxK0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکتر محمد محسن صدر، رییس سازمان فناوری اطلاعات ایران، در شبکه اجتماعی خود با اشاره به کارت زرد مجلس به وزیر ارتباطات نوشت:
«کارت زرد مجلس، حق قانونی نمایندگان و فرصتی برای رفع کاستی‌هاست؛ اما قضاوت درباره عملکرد یک وزارتخانه باید بر پایه همه واقعیت‌ها باشد. وزارت ارتباطات در شرایطی کم‌سابقه، از حفظ پایداری شبکه در روزهای جنگ تا توسعه ارتباطات روستایی، پیشبرد فیبرنوری و بازسازی زیرساخت‌های آسیب‌دیده را دنبال کرده است. نقد منصفانه زمانی شکل می‌گیرد که موفقیت‌ها و چالش‌ها، هر دو در کنار هم دیده شوند.
ایستادگی برای دفاع از حقوق مردم اگر هزینه هم‌داشته باشد سند افتخار است.»
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/688317" target="_blank">📅 23:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688316">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
حمله موشکی آمریکا به یک نفتکش ایرانی در نزدیکی جزیره خارگ
🔹
یک نفتکش کوچک ایرانی در فاصله ۴ مایلی جزیره خارگ، هدف حمله موشکی ارتش تروریستی آمریکا قرار گرفت. این نفتکش در محدوده لنگرگاه جزیره خارگ مورد اصابت پرتابه نیروهای آمریکایی واقع شد.
🔹
منابع محلی اعلام کردند که این حادثه خوشبختانه هیچ‌گونه خسارت جانی به‌ همراه نداشته و کارکنان نفتکش در حال تخلیه هستند.
🔹
جزئیات تکمیلی درباره میزان خسارت وارده و ابعاد دقیق این حادثه توسط دستگاه‌های مسئول در حال بررسی است و اطلاعات متعاقباً منتشر خواهد شد.
جزئیات بیشتر
👇
khabarfoori.com/fa/tiny/news-3243816</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/688316" target="_blank">📅 22:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688315">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
۱۲ کشور خواستار محدودیت تجارت با شهرک‌های غیرقانونی اسرائیل شدند
🔹
فرانسه، بریتانیا، کانادا و ۹ کشور اروپایی دیگر در بیانیه‌ای مشترک از اعمال یا حمایت از محدودیت‌های تجاری علیه کالاهای شهرک‌های اسرائیلی در کرانه باختری خبر دادند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/688315" target="_blank">📅 22:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688314">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
آمریکا در حال حمله به نفتکش‌های ایران/ پایگاه صهیونیستی آی‌۲۴: نیروهای آمریکایی در حال حمله به نفتکش‌های ایران در تنگه هرمز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/688314" target="_blank">📅 22:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688313">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
سخنگوی قرارگاه مرکزی خاتم‌الانبیا: ارتش تروریست آمریکا تهدید کرده است که سه فروند نفتکش ایرانی را هدف قرار خواهد داد
🔹
در صورت هرگونه تعرض به کشتی‌های ایرانی، نیروهای مسلح جمهوری اسلامی ایران پایگاه‌ها و منافع آمریکا را در منطقه به شدت هدف قرار خواهند داد.…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/688313" target="_blank">📅 22:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688312">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32b385f32d.mp4?token=ihMnGU9XYmuL6S1XZY33rjBuyaWZEdF27FtqO_moxC6R3wNVzNEk0Es2QbLcy96dqaa2LBTPTYo7wB51XOCXZUkAX6rHakDmm-z-QzaDWT6QoFHOmMNtiz2cqcJVCNlIjT6Au3tMcUxHv7u2DY_sAIJDGlSr86W5LBdHWzeelut5RxwVnRe1eVtQYNCOJC41iqLT0M7c-Vv2iaX0SlWdKRz4ixAM8nRdygY2-tqF-oCjGgm_AVtl_UE62k-OjWmtx1DtRGoKLJkAHd_EKKwx8oPrco3TiGQac0YQUtdz6McpQSBbaXIuRBLD2cgZ8nrxoXJC5qGSOG0lENag2zyRcYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32b385f32d.mp4?token=ihMnGU9XYmuL6S1XZY33rjBuyaWZEdF27FtqO_moxC6R3wNVzNEk0Es2QbLcy96dqaa2LBTPTYo7wB51XOCXZUkAX6rHakDmm-z-QzaDWT6QoFHOmMNtiz2cqcJVCNlIjT6Au3tMcUxHv7u2DY_sAIJDGlSr86W5LBdHWzeelut5RxwVnRe1eVtQYNCOJC41iqLT0M7c-Vv2iaX0SlWdKRz4ixAM8nRdygY2-tqF-oCjGgm_AVtl_UE62k-OjWmtx1DtRGoKLJkAHd_EKKwx8oPrco3TiGQac0YQUtdz6McpQSBbaXIuRBLD2cgZ8nrxoXJC5qGSOG0lENag2zyRcYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرلشکر رضایی: تنگه هرمز، تنگه عزت ایران است...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/688312" target="_blank">📅 22:37 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688311">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e0fac0ecb.mp4?token=m7tadJBiZ8DQsfSOp8n-FNsiwfYn-yLOQTppN8C9HTjn5be0QewTlpiuM9bbqqbmw3PK96_0gwUtnVexNGdG4cgRZsZAFNSl4bY6fL4Y6ZB2LeX7h51bPvH6dJUA_mPcxLpt4rppomKzKXr-AvJEqXFrq7GyPzpKPGI4etsFqX3BRB4XdZPDmE9acnEOvEcNiahlQUhf0dZulsivs7KVKJdZh5USPSAKr9mCnj7HHuwG3fTNzrY6zNBZshxIn9XbgQwHeF9LDYf32pRNFREqP-sWLmZHciakE7CvfbE-FKWUGkoMONUMQhJxbiiY75zzizY8Urdo56fCrDtesdwKmj727yqHcqea9ZvhdgACdmpgWInuJEWso68xjI6py8lHV0qdRPeVcmfRm1RLHWguPq6wQJi7XEuF_kyK3bkm2qVapZVwKl2tvklRErHPxqx7D-V9pMz-SjpjTRfJNq17b08htZx5TQH98Se4sEq40Xnaq31ua6Pw9mc5MA27kyhqxJe5NfffNaI9kzMgCaoo9LC93NqwdDtwN4Q7GuE3f2h0V0JelXvdz9Qo4r2CTfMQtoBAgPH5vklYB4eEKAFQgGJXzIIpFxd7yCkxXC9V1ocUhP1DBVv7m4Jm_D3w57FUqYWrIftgeQbMgPlduW1tHsmyVZ7nQPezVya6joJPJzI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e0fac0ecb.mp4?token=m7tadJBiZ8DQsfSOp8n-FNsiwfYn-yLOQTppN8C9HTjn5be0QewTlpiuM9bbqqbmw3PK96_0gwUtnVexNGdG4cgRZsZAFNSl4bY6fL4Y6ZB2LeX7h51bPvH6dJUA_mPcxLpt4rppomKzKXr-AvJEqXFrq7GyPzpKPGI4etsFqX3BRB4XdZPDmE9acnEOvEcNiahlQUhf0dZulsivs7KVKJdZh5USPSAKr9mCnj7HHuwG3fTNzrY6zNBZshxIn9XbgQwHeF9LDYf32pRNFREqP-sWLmZHciakE7CvfbE-FKWUGkoMONUMQhJxbiiY75zzizY8Urdo56fCrDtesdwKmj727yqHcqea9ZvhdgACdmpgWInuJEWso68xjI6py8lHV0qdRPeVcmfRm1RLHWguPq6wQJi7XEuF_kyK3bkm2qVapZVwKl2tvklRErHPxqx7D-V9pMz-SjpjTRfJNq17b08htZx5TQH98Se4sEq40Xnaq31ua6Pw9mc5MA27kyhqxJe5NfffNaI9kzMgCaoo9LC93NqwdDtwN4Q7GuE3f2h0V0JelXvdz9Qo4r2CTfMQtoBAgPH5vklYB4eEKAFQgGJXzIIpFxd7yCkxXC9V1ocUhP1DBVv7m4Jm_D3w57FUqYWrIftgeQbMgPlduW1tHsmyVZ7nQPezVya6joJPJzI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امنیت خلیج فارس بدون همکاری کشورهای منطقه امکان‌پذیر نیست
دکتر گاردونیو، استاد روابط بین‌الملل دانشگاه UNAM در
#گفتگو
با خبرفوری:
🔹
تنگه هرمز یک اهرم مهم راهبردی برای ایران است، اما امنیت خلیج فارس تنها با همکاری کشورهای منطقه امکان‌پذیر خواهد بود.
🔹
حضور نظامی آمریکا در خلیج فارس نه‌تنها امنیت ایجاد نکرده، بلکه به افزایش تنش و درگیری در منطقه منجر شده است.
@Fori_Tv</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/688311" target="_blank">📅 22:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688310">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd71fc45ab.mp4?token=AxMRjGFt4tjqKduUoTpvLxp9vwRVq-IZ67hpilb527H4IWhO5SNa2-rR-RcD828nXxPw4rbu5AiFp-cBtTGqL5RR5NIlvPV2TWIJKUl8E3QxozzTCc2NSIYfaeGElEc1x13KXNNURHQ1JdZd0ypq09aBT-YudI6t1jnBq9zOssgjcJnYoA--E-V-OiCBzyT15bUkezSkDzZZHTDlgGuKdQKGAeoV9KwRgsdMBJ-fwWGdhnby4xS4QHCSFQEC2wdoSqVuCfytCpKsowpW8-k4usnRKA-seNXEDa5ajCc4y-H5F3b6O2LHstxD_bNEqtAyJIvSJpigQDpsTvrdv7TrJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd71fc45ab.mp4?token=AxMRjGFt4tjqKduUoTpvLxp9vwRVq-IZ67hpilb527H4IWhO5SNa2-rR-RcD828nXxPw4rbu5AiFp-cBtTGqL5RR5NIlvPV2TWIJKUl8E3QxozzTCc2NSIYfaeGElEc1x13KXNNURHQ1JdZd0ypq09aBT-YudI6t1jnBq9zOssgjcJnYoA--E-V-OiCBzyT15bUkezSkDzZZHTDlgGuKdQKGAeoV9KwRgsdMBJ-fwWGdhnby4xS4QHCSFQEC2wdoSqVuCfytCpKsowpW8-k4usnRKA-seNXEDa5ajCc4y-H5F3b6O2LHstxD_bNEqtAyJIvSJpigQDpsTvrdv7TrJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون ارتباطات و اطلاع‌رسانی دفتر رئیس‌جمهور: رسانه ملی به بلندگوی آن یک نفری تبدیل شده است که در شعام مخالف تفاهم‌نامه بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/688310" target="_blank">📅 22:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688309">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23f1d070c8.mp4?token=ayjIFJZC9urTf0NB77tmmgREMAz40Vb0cNx6SG6mSBbIKAHKJdTjfp7qlfs6jov79JzaSq2kMwJi4jVggvSpkAhlxIFYzp8gLcZYQ6M6DAXHYfEBrFo4G1i70VKAceJbj9uGpNS94I1GJGjpchVgGyMrnHn3Hxavdp9S3fsU1gJBnGuPJyMg6g1C4Gi76poo6CMUfRxYkSZANiW83HQfrkDSF4q-Nv3dnGj6D425XdKkT2MehuKpqSi5q8j_u3SkYsSdpOAMkR8UXi4PzRrZ0XRZhiYEufaSRdUAqeU6mx8WzQDt0s-ki9Vi-myOPfsWqOkQwhB4A0fnUuLKy_nSnINKLFXetgpDPu6LlmmRGfbDuXF9zQoJzwo0lBO38bcyUlGYhU1YBIDra-Dx8yFf8aE7ft3IBiunf8oldfPtqYpPfcFTJxsEKkcmcXxwFJ9ndy66eEnfdfUrK73x3YJcawQinCCdNpEfGXgF6jTyub4jHVzA4SUqE4KNp8NSeGYeKu7PkLhksFDS8LmtlFFxf3z7ZDZlaM7W4ZjGON8Ki8-TtYfQPHulMwjDzRZopiIyltm_EtznemYQMDW4Idpkq35ZWzlJEaIrok5vuF_k12O9Ua7Osy2VX_zzy-RJ8pxYY7eh1Q8INHzmozqQRUngHW6uW8YbDOyolZyhcZ1q9VI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23f1d070c8.mp4?token=ayjIFJZC9urTf0NB77tmmgREMAz40Vb0cNx6SG6mSBbIKAHKJdTjfp7qlfs6jov79JzaSq2kMwJi4jVggvSpkAhlxIFYzp8gLcZYQ6M6DAXHYfEBrFo4G1i70VKAceJbj9uGpNS94I1GJGjpchVgGyMrnHn3Hxavdp9S3fsU1gJBnGuPJyMg6g1C4Gi76poo6CMUfRxYkSZANiW83HQfrkDSF4q-Nv3dnGj6D425XdKkT2MehuKpqSi5q8j_u3SkYsSdpOAMkR8UXi4PzRrZ0XRZhiYEufaSRdUAqeU6mx8WzQDt0s-ki9Vi-myOPfsWqOkQwhB4A0fnUuLKy_nSnINKLFXetgpDPu6LlmmRGfbDuXF9zQoJzwo0lBO38bcyUlGYhU1YBIDra-Dx8yFf8aE7ft3IBiunf8oldfPtqYpPfcFTJxsEKkcmcXxwFJ9ndy66eEnfdfUrK73x3YJcawQinCCdNpEfGXgF6jTyub4jHVzA4SUqE4KNp8NSeGYeKu7PkLhksFDS8LmtlFFxf3z7ZDZlaM7W4ZjGON8Ki8-TtYfQPHulMwjDzRZopiIyltm_EtznemYQMDW4Idpkq35ZWzlJEaIrok5vuF_k12O9Ua7Osy2VX_zzy-RJ8pxYY7eh1Q8INHzmozqQRUngHW6uW8YbDOyolZyhcZ1q9VI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از طلا و نقره تا خدمات بیمه و کسب و کار، روایت مسیر تحول داریک
محمد زرین مشاور برندینگ و استراتژی داریک در
#گفتگو
با خبرفوری:
🔹
طی سه سال اخیر یکسری خدمات جدید به برند داریک اضافه شد و استراتژی‌های کسب و کار تغییر کرد.
🔹
لازم بود متناسب با این موضوع، هویت بصری داریک نیز تغییر کند تا با تغییرات استراتژی همسو باشد و به همین منظور بحث ری‌برندیگ رقم خورد.
🔹
داستان برند ما این است که در این آشفتگی و پیچیدگی‌های مالی، برند ما نقطه امنی باشد برای مخاطبان و این داستان هم در خدمات و محصولات خواهد بود و هم در هویت بصری برند آمده است.
🔹
داریک به طلا و نقره محدود نخواهد ماند و خدماتی چون بیمه، لندتک، آکادمی و ... را نیز ارائه می‎دهد و در فرآیند تغییر در حال توسعه بحث انبار فلزات هوشمند گران‌بها هستیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/688309" target="_blank">📅 22:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688308">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MT_AI1yU7PVIfTAGl-368BlE2I4M8Uvn7EgKhcGUxrky1bpTnET7Cltc3fg5wzOkxqRJ8Odoi7-zirng3gMj1HX2Ouf_FO8GVXknng8ZtTT9EjuM1yFRDZFyY8JuESSpIi3K6JHU3HBiLEpWbpLjiM_A_FiwesFlZMwBqGiJWzdo_GtsRhyEupvpZJ4GzTYmX3yIiR8WAW8WfTeGs1HoK_BnkDJcYnOp-cJCZUcX0OTy3pKzAVPYIKReczrhq3NIJrrTjExCnSS0XMxhiKx2IuWyYrBwJUqc1paO5UsNJTR0EDtn7ELB9YXVOVx8NBAgyupR514dqrO-JGyktbSb4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تو که لالایی بلدی، چرا خودت خوابت نمی‌بره؟
🔹
نتانیاهو سال گذشته وعده داده بود تجربیات اسرائیل در مدیریت آب را با مردم ایران به اشتراک بگذارد؛ حالا در سالگرد آن اظهارات، گزارش‌ها از ازکارافتادن ۵ آب‌شیرین‌کن از ۶ آب‌شیرین‌کن اسرائیل و احتمال بروز بحران آب شرب خبر می‌دهند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/688308" target="_blank">📅 22:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688307">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CY0EJ82VKfLjfmcd61Sn-UHEb1w2N12nLHwF0faH4Srs_rcoifhUvCJ2sVUtHOmG6TagpuSJ-KnqZ1UanUpctmLfsO8gkHfWqWUVhzozZ-9lP7CJx2f2cobybSFyQknrj9Udy2h_qIQ7LY52xce6WzCmRmdxNaFrwVbsKJMuuTHpljS0bMUd8JgM5_QzyISjF28ehASnF2VBwjWMvuK-CmHj_Zj_L4sTYMg5IkoJ4X8xNNiOlf1askSwYFVLaQMNkxapHj3D2HaENWioahKpYWjZdVaYqR11cv2STtsfIPZvS8fJ2vZiXNhBbO8w479QUL8Db_KVH3VlaHWN_YH2XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زیر دریایی آمریکایی در دیوار آگهی شد!
🔹
واکنش طنز کاربران فضای‌ مجازی به شکار زیرسطحی دشمن آمریکایی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/688307" target="_blank">📅 22:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688306">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
شنیده شدن صدای چند انفجار در جزیره خارگ
🔹
صدای چند انفجار دقایقی پیش در نقاطی از جزیره خارگ شنیده شده است. تاکنون اطلاعات رسمی درباره منشأ و علت این انفجارها و همچنین خسارات احتمالی آن منتشر نشده است./ مهر
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/688306" target="_blank">📅 22:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688305">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksIhexFLDxR5QJkDE_1Iw2e0jTYFTLU0PF404v2t2IDIUfoG4N5Xe8WhF7CZwI7f9Ij79zXmFDy_5H4tJOAHHDfTrjBCeBjtVog4iMsTeCuR47yhOYvDozRv1TZERNFcdt6bJvq63cQ8qFRyuDC9c3FY_YjySlyHzPxy26HyHi_ZeLslRh4b-fJ7ILPXw77PDBAeD6_L9RbiMxNVajvY4JYSCwp3OK8mjUMtOFD9unjRXQxJa9jd-2InhcjLiqBvtGnNoP8dxmMVB8Wc26GRBu9JDr2K30W4T5J4EecH6IjyTghSwdA_0hUTjg4D2q8apHsbfjhTAlHBbOCdo8vLlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی قرارگاه مرکزی خاتم‌الانبیا: ارتش تروریست آمریکا تهدید کرده است که سه فروند نفتکش ایرانی را هدف قرار خواهد داد
🔹
در صورت هرگونه تعرض به کشتی‌های ایرانی، نیروهای مسلح جمهوری اسلامی ایران پایگاه‌ها و منافع آمریکا را در منطقه به شدت هدف قرار خواهند داد.…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/688305" target="_blank">📅 22:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688304">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5GXdKMLJlqEmgaSZ5ll9JvFrUPPNW2TUKHGCQbGDn4YA7dGFY6J1Us1fJwZfdc5QhIfXGu_3SM6pTq7uVHNkSiKRwgYC-RCu62peATE9ytcHYicsLfJhVpanwYaWx9L1dWw2mdG33JkDJd9tkLePY1vPGkR4r8Dphz8tS0vGlA1CzShKmRl84MK0sNahhGg4KAuLb5pSBr6ysXYOBkcHrLdvxSUK5Fhr_KYglffCaH8TzlPLI_92EPWsd40KODtCiuiMMM6hY7nnaF6kRa2HVTDBWGTO0Mx0rWHAwxoFG6L7DdCIxie4VNcvgH0GF4QbnR4wWpDWv19ffNH3BfOSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تمجید پاتریک هنینگسن، تحلیلگر مسائل بین‌الملل از شاهکار امروز نیروهای مسلح ایران: یک غنیمت دیگر برای ایران
🔹
آنها موفق شده‌اند پیشرفته‌ترین زیردریایی بدون سرنشین آمریکا را به تصرف خود درآورند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/688304" target="_blank">📅 22:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688303">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
شنیده شدن صدای چند انفجار در جزیره خارگ
🔹
صدای چند انفجار دقایقی پیش در نقاطی از جزیره خارگ شنیده شده است. تاکنون اطلاعات رسمی درباره منشأ و علت این انفجارها و همچنین خسارات احتمالی آن منتشر نشده است./ مهر
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/688303" target="_blank">📅 22:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688302">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
ویدئو شرکت سازنده زیردریایی DIVE LD:زیردریایی شکار شده برای تولید انبوه  طراحی شده است
🔹
آمریکا برنامه داشت تا پایان سال ۲۰۲۶ تا ۲۰۰ فروند از زیردریایی بدون سرنشین DIVE LD را تولید کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/688302" target="_blank">📅 22:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688301">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
شکار یک فروند زیرسطحی هوشمند دشمن آمریکایی در تنگه هرمز   نیروی دریایی سپاه :
🔹
مردم مبعوث شده ایران عزیز؛ با عنایت خاصه خداوند متعال رزمندگان نیروی دریایی سپاه یکی از مدرن ترین زیر دریایی های هوشمند و بدون سرنشین ارتش تروریست امریکا را در ورودی تنگه هرمز…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/688301" target="_blank">📅 22:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688300">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
سخنگوی قرارگاه مرکزی خاتم‌الانبیا: ارتش تروریست آمریکا تهدید کرده است که سه فروند نفتکش ایرانی را هدف قرار خواهد داد
🔹
در صورت هرگونه تعرض به کشتی‌های ایرانی، نیروهای مسلح جمهوری اسلامی ایران پایگاه‌ها و منافع آمریکا را در منطقه به شدت هدف قرار خواهند داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/688300" target="_blank">📅 22:12 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688299">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CX4qvi1nltpRf71M3YocJJLJrOxZ0UldNswTlK-3aex89Lhk_HP6hYzJRzT2yGyizsRb9hMTQdGI4eVpX8e6mIIkJjGzdrX95GQ3d2c45uOZQRx0lHV_UVynaH_JLEg8MFdhMSE2Zo8leGdj_dce4UtfBoXt8qivCqDzHXtYJffUE4SdHKuoxdhM3fmVeOwo6H0heNbq9XFmEmJjNBUnMkUkKMcemBWg6lx0D0lcYHAFxYm91CIZxuE5I0Xxo-q-lY9q6FMxmMHmsnQzl9AZn1jHeKlbnRb1KKmVwu_GskG5tbS7eT84Hea2IZL4h34Nb3z_-5IkC8BR3vXoCZDIqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: برنامهٔ زیردریایی‌های هوشمند آمریکا ناک‌اوت شد!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/688299" target="_blank">📅 22:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688298">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4Xi1bX79RufLwMuRX2WV0yvvHsWC-aRBds9b3nc2z0tRveYfAvJeibvvR2hz1mBvJoU3guMu849kmd_xG3TXbTnFLV9bwLrkFfpGuQpKnehwXA-wE5jRf9gLVseYXvDZQxOCOh9lgfiAZp1uQZcVytZprUYmaUTYYM2MCQbhLnfnpO0fKeucUtKmN1ZHlicSUq_WCPsv3Rk2XW6ecOrNxCE-Bn9bgueaUGVEUjY5BFfxgqWccOihFN2Woc5nNJKD-xXfLfI2AXQXVzbIIiIe86QTuPeEqqpJfebT3RfU_qG2mc4zBI1HGw5Ol-04EyTSif97Bq2ItimO7RPpt2UhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اذعان صریح امارات به هماهنگی‌های امنیتی با صهیونیست‌ها
🔹
وزارت خارجه امارات در واکنش به گزارش‌ها درباره هشدار ابوظبی به رژیم صهیونیستی پیش از آغاز عملیات طوفان الاقصی، ضمن عدم تکذیب این گزارش‌ها، با افتخار از تبادل اطلاعات امنیتی با این رژیم سخن گفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/688298" target="_blank">📅 22:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688297">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/585a8df792.mp4?token=e8zsSFOe203j1F9ve_EiXQkmLO5XOwHkxLq2ydaLnlbIEqeiSYSBsuUblIGwr_0ftwl5ItT-ynfd32dyb_m--zvRVb_CNuv48sYsQc3xTt5gIGeX9ldDNkpVZxHCEwcY_FXaT7jnD3MVCvrK4abXfPGg6wuMC2x-BLM3N8K6aVfpQQMqxgTzBQb2uBncEdev7aWIjqUY9h1eXKDkup1AQr4idz9OMyWnKgnVgZnJ-FkizlVmJHKgw2ajIbdrXqLkSQQk7GwOYp7Jt-yeNlk3EDGcAoKl0iI7nftrx7xrhK7oZ17FzVsGfisdZaFNlvarWzyqkPRFQnB-KK9hd_MlsjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/585a8df792.mp4?token=e8zsSFOe203j1F9ve_EiXQkmLO5XOwHkxLq2ydaLnlbIEqeiSYSBsuUblIGwr_0ftwl5ItT-ynfd32dyb_m--zvRVb_CNuv48sYsQc3xTt5gIGeX9ldDNkpVZxHCEwcY_FXaT7jnD3MVCvrK4abXfPGg6wuMC2x-BLM3N8K6aVfpQQMqxgTzBQb2uBncEdev7aWIjqUY9h1eXKDkup1AQr4idz9OMyWnKgnVgZnJ-FkizlVmJHKgw2ajIbdrXqLkSQQk7GwOYp7Jt-yeNlk3EDGcAoKl0iI7nftrx7xrhK7oZ17FzVsGfisdZaFNlvarWzyqkPRFQnB-KK9hd_MlsjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همسر و فرزند، یا پدر و مادر؛ کدام‌یک اولویتند؟
🔹
وقتی ازدواج می‌کنیم، چطور باید تعادلی پیدا کنیم که نه حرمتِ خانواده‌ اصلی‌مان شکسته شود و نه زندگیِ مشترکمان آسیب ببیند؟/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/688297" target="_blank">📅 22:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688296">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
شکار یک فروند زیرسطحی هوشمند دشمن آمریکایی در تنگه هرمز   نیروی دریایی سپاه :
🔹
مردم مبعوث شده ایران عزیز؛ با عنایت خاصه خداوند متعال رزمندگان نیروی دریایی سپاه یکی از مدرن ترین زیر دریایی های هوشمند و بدون سرنشین ارتش تروریست امریکا را در ورودی تنگه هرمز…</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/688296" target="_blank">📅 22:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688295">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5MHyY-Tqjl2Z66QdGZ5pFsY6YhQuN2m4UiUhzBX84EV5iPri2kgTzLqaDI5mGOBn3ofQGBTT-VffGjh4kLiHYcU8QfvBSCkkV90mpjFMxADwkK2FIZnnt9Fk_EAEtnHFeIU4gLcZhQlLKiZ0D8nViSMQcV00zf4LLHj0P3dMfmVV9XekJSnWr2D9B5SJxNVwZC1WhnZ9hzZ27wxbhDXzfVv4sI7MstwKdKtkFkCepdZODNQqDv2EG-jRwzhpvDduisLPASDLH_auQy_CxBa6ImMa9_ZC57xPzerxOHW9qmNQQ9QHlX2i21feKnhGmC_QrYVhrJyCkG4jTXtzb4RNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنایه عراقچی به راه‌حل خلاقانه آمریکا پس از ۴۷ سال تحریم و جنگ
جدی می‌فرمایید؟!
وزیر امور خارجه:
🔹
پس از ۴۷ سال تحریم، آمریکا به نیابت از اسرائیل وارد جنگ با ایران شد؛ جنگی که پیامدهای فاجعه‌باری برای آمریکا، از جمله برای جایگاه و اعتبار این کشور در جهان، به همراه داشته است.
🔹
پس از آنکه واشنگتن نتوانست با تحریم یا جنگ به اهداف خود دست یابد، راه‌حل «ابتکاری‌اش» این است: تحریم‌های بیشتر!! جدی می‌فرمایید؟!!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/688295" target="_blank">📅 22:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688294">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzZ1RLRNU4JLaY9w2McbU3OCv7-DsGf-aZ5o_zJJG4RMOF5wc1e7iJnlqOyE6GWkm-GIVzzrRycfqpoAP5ACclGfWS-hv13wZgfIsvCOR6ux7K-vMUgVrlDiVsbrZ--XPeS4zBWh4LYudSaDy3iUfnG5EjufV77UuX9984js097Rg7Sa_QZ1yK4n67qymPCS_UT9M8f8Fn5i3qwuVWKUsKL9GpxGXLL6ROTo2qh17JeGeVgzFkX6QHP8HufwVcbJSWC5G2zRjv8UMhlzf1xghW-CupE-sduqgCEeH-66GOiQCbcAFh-9xqb3ukId9-lXSVcDY48UuY088QqNhIADGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صید هرمز
🔹
نیروی دریایی سپاه یکی از مدرن‌ترین زیردریایی‌های هوشمند و بدون سرنشین ارتش تروریست آمریکا را در ورودی تنگه هرمز طی یک اقدام پیچیده اشراف اطلاعاتی و عملیاتی در سحرگاه امروز به دام انداختند. این زیر سطحی هوشمند از جدیدترین تکنولوژی در حوزه زیر سطحی در دنیا برخوردار بوده، که سال ۲۰۲۵ میلادی به ناوگان ارتش آمریکا تحویل شده است. این زیر سطحی اکنون به غنیمت گرفته شده است.
🔹
هشتصدوپنجاه‌وپنجمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/688294" target="_blank">📅 21:47 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688293">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14ca1bb43f.mp4?token=b1oEA409YcwzZ0uvxW3mgxtqtZIRaG2w1U4PVPYZxky_jNm4MP5ezAVI0Ppzor1mOmcUg_1BoQzxmILzMFJRKkpWtb0-wsDqOzy9xoz1WMYoY_xALf050J2Ec7GvyBzbp-5vSK5R6pBkfJgmGSlvFizJ6tjilOqAjIYb9D8AeZuFgY5RripsrREo3TWpN9zJHtMVSdSFTpowJnORhIbhiKYs4ZCSrm-DP1UKX0CQMQ6O83ty53sTTTsnPyQOPBgm4WR8SKqOobMysMwKGDc6ntuCswiGvcyNGY1j8QkupcSopAiqlG8aU-hQ7hT5JAj5LrJkU8FMFtbdXjSe_cXSpEF82GCd8AN-0FfLKrzyaCucGW7QJurj9BHiDl3tbd2XhvtD48Tp4-sWWt-UdQ2KrjQZg1whDQ2M8odiMyP_riRUBIKEb9diWLD7QxeRFrmTAPy-SK1asGphju2FvYiXC-nUfVCLQUXyGAUohjSfJ2iFzdevTvC9axtDP-tK_WCS3qtDfhNPyfdNSI3ALZ68-kbSHuDe_u_ASe7ZYOKF131gQ4eV9dhxKA_SuT2A5CaGKp-6Y1Hqmr_HisvLk35lq5KmJ1k_8SBXK6M3UqlK_DYfhUUFSAXWMZJRKGqZ1Oc1zCE_s8g9wMgaG9xWdPotL7DT363eQpsSLpj_8ta0phc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14ca1bb43f.mp4?token=b1oEA409YcwzZ0uvxW3mgxtqtZIRaG2w1U4PVPYZxky_jNm4MP5ezAVI0Ppzor1mOmcUg_1BoQzxmILzMFJRKkpWtb0-wsDqOzy9xoz1WMYoY_xALf050J2Ec7GvyBzbp-5vSK5R6pBkfJgmGSlvFizJ6tjilOqAjIYb9D8AeZuFgY5RripsrREo3TWpN9zJHtMVSdSFTpowJnORhIbhiKYs4ZCSrm-DP1UKX0CQMQ6O83ty53sTTTsnPyQOPBgm4WR8SKqOobMysMwKGDc6ntuCswiGvcyNGY1j8QkupcSopAiqlG8aU-hQ7hT5JAj5LrJkU8FMFtbdXjSe_cXSpEF82GCd8AN-0FfLKrzyaCucGW7QJurj9BHiDl3tbd2XhvtD48Tp4-sWWt-UdQ2KrjQZg1whDQ2M8odiMyP_riRUBIKEb9diWLD7QxeRFrmTAPy-SK1asGphju2FvYiXC-nUfVCLQUXyGAUohjSfJ2iFzdevTvC9axtDP-tK_WCS3qtDfhNPyfdNSI3ALZ68-kbSHuDe_u_ASe7ZYOKF131gQ4eV9dhxKA_SuT2A5CaGKp-6Y1Hqmr_HisvLk35lq5KmJ1k_8SBXK6M3UqlK_DYfhUUFSAXWMZJRKGqZ1Oc1zCE_s8g9wMgaG9xWdPotL7DT363eQpsSLpj_8ta0phc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شروع فصل جدید داریک با توسعه و ارائه نوین محصولات
عبدالرضا عسگرخانی، مدیرعامل داریک در
#گفتگو
با خبرفوری:
🔹
هدف از ری‌برندینگ داریم، توسعه و ارائه انواع محصولات داریک و پروموت آن‌ها بود.
🔹
پس از ۱۸ سال فعالیت داریک در این اکوسیستم، اکنون وقت آن بود که محصولات این برند در بستر آنلاین نیز ارائه شود.
🔹
در داریک سبک جدیدی از توسعه محصولات را در پیش گرفتیم و از توکن‌‌هایی که بر پایه فلزات گران‌بها هستند استفاده کردیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/688293" target="_blank">📅 21:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688292">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kClSbp6HUUclqhWOSH18yiq0z7lvMAlSwsHayRFFATlZSIiWBizM37nKGvhU66vzjWGduYaQcCnd8_pkWzgqcyBKsTZ_q9TDKOHLSh6r9uTUDxaauikPETOOPE25pWgbkeDFUViQ0rYadSOg0fxCZkQnLr05Md6K5NUKUGaDMHckobqjgnX13XHqo0YAglbEe8KJwdm2f4ZooKEqF8LBloj8w2oienLvW8XMaDUu4foKiGC9zIZx-VGCmZz93sPGMPllJ-PYMzfbI293IzKcN17jvQucty5j_Fa1g1IDTrl06o4QIuS8X2eFE-9bdTW_LQtuqMR0-SzSBp4f4v3egQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مدیر سامانه هوشمند سوخت شرکت ملی پخش فرآورده‌های نفتی: کسانی که کارت سوخت ندارند با مراجعه به سامانه سوخت من، یک روزه کارت سوخت دریافت کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/688292" target="_blank">📅 21:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688291">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
۱۲ کشور خواستار محدودیت تجارت با شهرک‌های غیرقانونی اسرائیل شدند
🔹
فرانسه، بریتانیا، کانادا و ۹ کشور اروپایی دیگر در بیانیه‌ای مشترک از اعمال یا حمایت از محدودیت‌های تجاری علیه کالاهای شهرک‌های اسرائیلی در کرانه باختری خبر دادند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/688291" target="_blank">📅 21:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688290">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
پرس تیوی: نیروهای مسلح یمن کنترل منطقه الیَتَمه را دوباره به دست گرفته‌اند و ده‌ها تن از نیروهای سعودی به اسارت درآمده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/688290" target="_blank">📅 21:37 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688289">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFtSPZio7hiifVqgPzUjZwQ66dcPTjxCIYRDABfvm86PoO_31sFgRE6GyhJYlkHz0UfJJMWzKXeSL4Ymjn6mrs2ebrGGna5Nq6oTkphWPwlDRugz7BwO-QRBffMt5nHXpHsdIxi3TJnf9ufX04-rMPkr9k7sqO7AgTyystJYKdmin6HtDvAYfDLPAW5Hfo3ct89Nmq6CC-KjyYEm_zDgAdpG6ukPpmTgyDPfvaByRbRqq32svi-7_839WLmo6lFNeDamKrSKmZv-XzPWtltFjzQpgIrYST7B6PKFq184Xu3ubDKj1qZuK9OD7lDJpHyV9r2bUOp7HbY4keDMfv8jyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شکار یک فروند زیرسطحی هوشمند دشمن آمریکایی در تنگه هرمز   نیروی دریایی سپاه :
🔹
مردم مبعوث شده ایران عزیز؛ با عنایت خاصه خداوند متعال رزمندگان نیروی دریایی سپاه یکی از مدرن ترین زیر دریایی های هوشمند و بدون سرنشین ارتش تروریست امریکا را در ورودی تنگه هرمز…</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/688289" target="_blank">📅 21:37 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688283">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TYvYNls3NgRSuvPwoBtu2RfStdfiuol2gJZ47B4N9X2gSkBeAfX3NYWuwYuIQjk2bJd9-dWAvonqnvsaEAMSxsHPZgEa9F3g9ED5So1yLpsvR8gwEupXGrfCyya68jB8lIHHQVMViGg4DjywtzvBOp__bEYIQFjq-BK0379O5jJvaN1CZeBrQc2NfkDdOGh3Lp1Yhzhk9JsSX1jXjzXd2w9o3y51ZThpaCv5ogTWrDDWNJASKjdXdabkDC4VJ-GfoYRvlcaJ818ScBAQwYqevNeJ-H7oZjKwYwb2Yb3BLufXS1iHQSYNW1GABDROOZhRV-MUjrWRpxKCsYf-CfsBXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XdR0YybzPbcOTdlW-69AYc13h3inunR8bGGROuSmAMaYwzmrt4jqkDSxlkHh26fsX2mahXR8Qx2Ryz21T1fmzXJoug9NDhagMnr30laHDjHmyWGqB5715paRu82eS-tD9p85wIR7qMrxUlhU5cOwXmwkPRNbL4UeGDvnxNMz6OieKVZ3Tao8GojqBsWl43EDsJmSCngAU0dSWzN0YL9GFmCidMivd6kJACZu9MTIGpSBREHRlBGykHy8ZeAEj_VeRFaBg86dhqjfRimzEEp9zLpkjx0zLTUC64evtHNremQnUA16qyyUGJHhph_G3iwzewC1CL2GgX_4vfNv4vAJyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JkQ-ks8sjst4P3uIbwcoltGQpJ83DSGea0Bezpe_2mgLkkPut7YVa_XOjh70rS65uiYc_hnj0vZ0dAoa-4sB-YkUqI1PjyNpVdC9c15pYwbdxW2CQGtIe-XK-KPdJEBeYbBZfOrj26z77u71XarYdgiQRnoJw8yuvtXcGsEGG-eX99rhYGrLDFp-3NuBZ_pmm4ibdapDb4ITvv2vsuS_eQq1wgtI4cywynd9cYcU7eblf5pzhE_JGNoti2dDkmiff2PSMiMXTImftlmI0Xgih9UfFcrqI2crFmG-VZPl8ZKqcerwtBT2Na_fynx-cEXaB2vOcqESRSs-GxjCBuoUMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QnFtKMFPB1M0jjgDan3sXfgvfM6-1OG82lnjBZH-4k-iAiYWVK6vrsuziTkNHfrEG1cBQrJiaBNLtM-bCkD7wrK6-60nh6Rwxr-4xKEpQ6xOAzwvRrsp7QBXclrtf0y1BV4iaGpkxYfiX8ZBzcFouAJsaRc21XpCTNBdHQorVBxpHi2rm-GC9K5HOBQfgFQZfMkWSsIWDXEK6aydcCa_gbp_FmMpZHiXCh4VVZvXcyv644yMSQBwBI1hInPwf3JkNdt5TmaGYxVTX0Y_e1tTO-j3gA3oM7hQ1K5JBJi8SYK313APe9LHfXHMKiIqqKDDk2A_ctC-VlEYytnQBMhjQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D4Huso5WC-pLierXbL31JGR5LIC2KXGwjNNFOiO8uY5NlJQkt0VwYJEG-hHtf021MsCERmerUc5xHXA7f5i65Bf9dIZaJa_f3e3EtFjLieSD8FWinIyuhdvMWY_GkQK_yBncxxAEG2JHZXlsNgtNCmp9CiX90YzMy-fUduPLVtUJ3oswk-335fT4grM90PC2GpPXVpzX5ScwZrrKxhFFIz2Rg29r7qvOCyi7DVoPx6brC2_3-_aBd9iAeH6WPuq4Cs8bK6fIB1d3SPBqSRMEL5i2YIQtdGhPik64ZAWNj2I7awQ7KXwxYE1hK1S79v7tSmZRC-gy_VjVDGssdv42QQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اولین فیلم از زیرسطحیِ هوشمند آمریکا که در تنگه هرمز شکار شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/688283" target="_blank">📅 21:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688282">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afd80bc80c.mp4?token=lEAXFbeokcCVGEv8suDJGozyS1EF4X2gfGfOmq4EgAQQTsVhqicvAMwoaR9X6MMV2NmU9R9i9CrCneryJVny82Xu-jTmnCBEPt_MGgRaShBeudM_5jX5lBzpkw59Wdslgw1SYRgx4o2B8el4OEXQqcmJnSjHxroVmiMEXA29UCJkDYRgKEllTJJtTrDMN4QZlvSvurBEV81pxgWRudXbNnyhm6bnbd_Ixxrk44wI6O1rBYTtzhOIk1wvxI3jZmKI41SC3T50oyGvkoU4urJUo7Y5tdZaU7B8RUWmXI3V5f0pB6VZo2eyQs6wUnGByzfolXtiIGVbysNj2XVJQ2Znmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afd80bc80c.mp4?token=lEAXFbeokcCVGEv8suDJGozyS1EF4X2gfGfOmq4EgAQQTsVhqicvAMwoaR9X6MMV2NmU9R9i9CrCneryJVny82Xu-jTmnCBEPt_MGgRaShBeudM_5jX5lBzpkw59Wdslgw1SYRgx4o2B8el4OEXQqcmJnSjHxroVmiMEXA29UCJkDYRgKEllTJJtTrDMN4QZlvSvurBEV81pxgWRudXbNnyhm6bnbd_Ixxrk44wI6O1rBYTtzhOIk1wvxI3jZmKI41SC3T50oyGvkoU4urJUo7Y5tdZaU7B8RUWmXI3V5f0pB6VZo2eyQs6wUnGByzfolXtiIGVbysNj2XVJQ2Znmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون اطلاع رسانی دفتر‌ ریاست جمهوری: مقدمه تجاوز اسفند ۱۴۰۴، اغتشاشاتی بود که در دی‌ماه در کشور شکل گرفت / به تعبیر امام شهید، آنچه رخ داد یک کودتا بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/688282" target="_blank">📅 21:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688280">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5d5430a50.mp4?token=FGoZBlAZ1DOUEMSxK2OMCKYNrMZORCYx73knoZB977m3aPfK8ZCvzdiGOg5YB0y-xxoJ_jlFRS-qux7jqvIaRJtAqWX_DbvljklxK_8ZYNy0JSdGtiap5ZTA4nq_KfSoMQQXYWcLq-J07QeUTVNWPS_1D41rZeG4YIIQYwG6MV7IbgZO05cyGwsE6dxegXmao5tHIRCVtjDGBOENAUwy31BNnH6oMID0dgc6sMW56B-GZni6xpCG9RSeEz30DXIZQz3yMI6joADUpRWO-sFRxucID2Zz3w7lPJHXyV0iIPGEyIAuk64C8RCdW5GHv3yn0L8MDkPy_rZV96jRnAPryA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5d5430a50.mp4?token=FGoZBlAZ1DOUEMSxK2OMCKYNrMZORCYx73knoZB977m3aPfK8ZCvzdiGOg5YB0y-xxoJ_jlFRS-qux7jqvIaRJtAqWX_DbvljklxK_8ZYNy0JSdGtiap5ZTA4nq_KfSoMQQXYWcLq-J07QeUTVNWPS_1D41rZeG4YIIQYwG6MV7IbgZO05cyGwsE6dxegXmao5tHIRCVtjDGBOENAUwy31BNnH6oMID0dgc6sMW56B-GZni6xpCG9RSeEz30DXIZQz3yMI6joADUpRWO-sFRxucID2Zz3w7lPJHXyV0iIPGEyIAuk64C8RCdW5GHv3yn0L8MDkPy_rZV96jRnAPryA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا حالا دیده بودین رعد و برق از بالای ابرها چه شکلی دیده میشه
😳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/688280" target="_blank">📅 21:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688277">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
از انکار واقعیت‌های اقتصادی تا دلاریزه‌شدن انتظارات مردم؛ چرا مردم به پول ملی اعتماد نمی‌کنند؟
🔹
سال‌هاست سیاست‌گذاران وعدهٔ کاهش نرخ ارز می‌دهند و مردم را به سرمایه‌گذاری در سپرده‌های بانکی، بورس و صندوق‌های سرمایه‌گذاری دعوت می‌کنند؛ اما در تمام این سال‌ها، کسری بودجه و چاپ پول بدون پشتوانه، ارزش ریال را کاهش داده و مردم را بیش از پیش به سمت دلار سوق داده است.
🔹
در این ویدئو بررسی می‌کنیم که چگونه انکار واقعیت‌های اقتصادی به دلاریزه‌شدن انتظارات جامعه انجامیده و چرا دلار به معیار اصلی قیمت‌گذاری در کشور تبدیل شده است؟
@Tv_Fori</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/688277" target="_blank">📅 21:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688276">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/142daa5f1e.mp4?token=NC1pwAJr0XE8LGsM4niaCnEj5PV37AUAQ2BlzIkJc4MtfEmZwA5Ypd5nIiD7lHrU-aHKtVNHwbrO3OehQ4Ny4NcWyNjoFK2IhXKIOHlz5Idbs7kIqGDC3DxP8CUgDVsIUbz63B98jbndr3Duf4C74mkgTu0k3FTzNbRaaWxP2m-8jfVO-vYAkDRS3Cuf2BDe9auS0PW4yE0c1CvYq5t2dC0RuWh35J54u3B9xjDzQYDkgrAlxPLTMQpeBKwa-cJW4FmU0f72ToE2eetLTFEOqn080UT2S8pTam63LSJzNy0wKqQ37sW1GtfeT93kwBxhTjQvAEpaPFNomARGHGtugQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/142daa5f1e.mp4?token=NC1pwAJr0XE8LGsM4niaCnEj5PV37AUAQ2BlzIkJc4MtfEmZwA5Ypd5nIiD7lHrU-aHKtVNHwbrO3OehQ4Ny4NcWyNjoFK2IhXKIOHlz5Idbs7kIqGDC3DxP8CUgDVsIUbz63B98jbndr3Duf4C74mkgTu0k3FTzNbRaaWxP2m-8jfVO-vYAkDRS3Cuf2BDe9auS0PW4yE0c1CvYq5t2dC0RuWh35J54u3B9xjDzQYDkgrAlxPLTMQpeBKwa-cJW4FmU0f72ToE2eetLTFEOqn080UT2S8pTam63LSJzNy0wKqQ37sW1GtfeT93kwBxhTjQvAEpaPFNomARGHGtugQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گرانی بنزین در آمریکا صدای کامالا هریس را هم درآورد
🔹
کامالا هریس در پمپ بنزین: سلام به همه، من اینجا در شارلوت هستم. از زمان آغاز جنگی که ترامپ انتخاب کرده، هر بار که باک خودرویتان را پر می‌کنید، ۱۵ دلار بیشتر هزینه می‌پردازید
🔹
قیمت گازوئیل هم از زمان آغاز جنگ ۸۰ درصد افزایش یافته و بدون شک این افزایش قیمت روی هزینه کالاهایی که با کامیون‌های سنگین جابه‌جا می‌شوند نیز تأثیر خواهد گذاشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/688276" target="_blank">📅 21:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688275">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tz9MpRuJJffBlIX8DDZlaKbMNLdrgPp_Uwvtd8mQU_1WexMqH8tnxuI3n1r_pEgQ7C1iYeKl1ZFsjjwlpUmWxUGiQ-xE7ZNDqmonKBSGp8E6o8A6Iu2CVDvxmHt1r7BPV5FBqhVEeDJ-_QNgQGrvZKEyS_8nZ64eLPAz8G12xE3VHqz4agmdORva5tXq9sdzfEzbpmHlnZGFZ562Ch_JPig20bZ64rxViQ8hIfGORDJE3ND_9hK-R0ZPlfRglFTwphOvnd0N3AInaEqo7YOA-nAuvV_YknbAGdyljOrAjSdF9YVExyLhubvLzDdzoX9Criv0wSsP_5p83vp2txamEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
سرنوشت طلا، دلار و باقی بازارها
در ۶ ماه آینده؟
🔴
امشب اکواحسان (بزرگ‌ترین رسانه اقتصادی ایران)
🔴
برای ۴ میلیون مخاطبش لایو داره و پرده از ۲ تاریخ مهم سیاسی-اقتصادی تا پایان ۱۴۰۵ برمی‌داره
✅
این لایو حیاتی؛ امشب؛ رایگان توی اپ اکوتراست برگزار می‌شه
⏰
زمان دقیق لایو فقط توی «اپ اکوتراست» نوشته شده. همین الان نصبش کن تا جانمونی:
https://ecotrust.ir/app/live-stream?utm_source=ArshiaYar&utm_medium=TelKhabar&utm_campaign=live-ehsan-0606&utm_term=socialproof</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/688275" target="_blank">📅 21:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688274">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrCro0SkVM3D2BDT-v15kfZqT-vl0MTOUHSag4_YQYXSDqxptI9s3FC5kUXLkpU1zpDYnMNSHr8K0_WrGnMhTAJMT15EOq421Ok2mUJ1MTHiSMDjYXZSkupPnsOxCsiJ9KpiFObc4z7HnGBu_uuJVBrhESwK79QQZzepHpPcuPae2AsECRswYvR4iQm1dMKZK3J2TT-eJpiSARVeqqPcjSlyBuqsww5OgbyEIX_PqnShULu1N45EDwb4ug_cxpoVAFwhUbAmH8-l7eO5MkHb34IM88mUPv5LUnjwRkqVG2phJGkvmHByhLJ2aHvdPt0A-bw_rRlgNPuvnKUlT0xUxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با هفته دولت و در آیین «یک ایران متصل»؛
بیش از ۵ هزار پروژه شرکت مخابرات ایران با حضور رئیس‌جمهور افتتاح شد
https://www.tci.ir/portal/home/?NEWS/235300/235321/575208/
@tci_iran
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/688274" target="_blank">📅 21:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688273">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
وزیر نیرو: رفع خاموشی‌ها در جنوب کشور در اولویت است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/688273" target="_blank">📅 21:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688272">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
دستاورد تازه شرکت ارکان سازه در سریع‌سازی پروژه‌های ملی
🔹
بار دیگر بخش خصوصی در اجرای پروژه‌ای
ملی و ماندگار
، رکوردی تازه و متفاوت در سرعت ساخت، همراه با کیفیت و نوآوری به ثبت رساند. مجموعه‌ای
هوشمند با ۳۵ هزار مترمربع زیربنا
، تنها در مدت
۲۲۰ روز
، به سفارش فراجا و با اتکا به توان مهندسی و اجرایی شرکت ارکان سازه احداث و با حضور رئیس‌جمهور به بهره‌برداری رسید.
🔹
مجتمع شبانه‌روزی آموزشی و فرهنگی سپهبد شهید محمد باقری با ظرفیت
۱۲۰۰ دانش‌آموز
، مجموعه‌ای جامع از کلاس‌های هوشمند و آزمایشگاه‌های عمومی و تخصصی شامل
هوش مصنوعی، الکترونیک و مخابرات، پهپاد و رباتیک
تا مجموعه‌های فرهنگی، ورزشی، اقامتی و رفاهی را در خود جای داده و با برخورداری از فناوری‌های نوین و استانداردهای روز دنیا تجهیز شده است.
🔹
این پروژه، نمونه‌ای از
ظرفیت بخش خصوصی برای اجرای سریع، یکپارچه و باکیفیت پروژه‌های بزرگ ملی
است؛ ظرفیتی که می‌تواند در مسیر توسعه زیرساخت‌های کشور، نقش مؤثری ایفا کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/688272" target="_blank">📅 20:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688271">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
دلیل رسمی کم شدن سرعت اینترنت ایران در ساعات اخیر اعلام شد
معاون وزیر ارتباطات:
🔹
کندی اینترنت ناشی از قطعی فیبرنوری در ارمنستان است و تیم‌های فنی در حال پیگیری و رفع این مشکل هستند./ جماران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/688271" target="_blank">📅 20:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688270">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpS7ieWQtRVNd9FCtpcYYuvLh4P0uVMP01qBMazjRYuVO51oAirCfiRQS48OVrxd_zRGUFA9Z5c9jhxAPp_8L4WFtyHyd1F6tQ4wusUpJY5sSW1Y_MJXobsa67BzJYi-dcUI7GHzkVnK9KqPy_IqrJZ8zsqHoqMXr8TrCp9cvdMU7ErK-mSlhQH9ZFm9kYxVo2NvI51IGWOSv20_OGWUtRrJnMWDp6rtKTu9gMSCjhJ4vYNuKCFDo3BizaOlCvr7ZK2fFlJqNLQgm9UuTKCmYdkx_SEcM1aZTxpY51cs-RdvY2aFkoparNS6hj0swxCqeFgjcTzUVdhz0eXd1EhmvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ذخایر راهبردی نفت آمریکا باز هم کم شد
🔹
درحالی‌که قیمت نفت امروز به مرز ۱۰۰ دلار  رسید، آمار جدید ذخایر راهبردی نفت آمریکا که لحظاتی پیش منتشر شد نشان می‌دهد که این ذخایر ۱.۲ میلیون بشکه دیگر کاهش یافته و به ۲۸۵ میلیون بشکه رسیده.
🔹
میزان این ذخایر از عدد بحرانی ۳۰۰ میلیون بشکه هم عبور کرده و درحال نزدیک‌شدن به کف عملیاتی ۲۷۰ میلیون بشکه است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/688270" target="_blank">📅 20:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688269">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d03ce3a78e.mp4?token=H894K20lnruGjpFYiEdPaBT92uayfrQMfLpzYG9ieBJjYb6LJ4nMTM514jzaLeuJFWmnmlRinCBDlx8iw_HAw5j5QaPgfKflxSUs5Vq-IGwDLn1EDMqzWOIGepKftLCdZhxDEIW34Tw5nZa8TOCj1XV9a3y18u4KqjitVFXQ_KrUx-FqS2qdOPr1WOEEj3dKsUNow_aVS5IzU2gGGPgVN0DRSIXAolvL40Gpd0JejJLevJgZfJohrh2SjR8tM6tVkb29E2Wwe2lof3dcZ8BJF86wJJC3C3FwonhZcTfaqtVGkciiHOW-xWjdGqD22E0tn6LX12qXR7je19fsWpBjyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d03ce3a78e.mp4?token=H894K20lnruGjpFYiEdPaBT92uayfrQMfLpzYG9ieBJjYb6LJ4nMTM514jzaLeuJFWmnmlRinCBDlx8iw_HAw5j5QaPgfKflxSUs5Vq-IGwDLn1EDMqzWOIGepKftLCdZhxDEIW34Tw5nZa8TOCj1XV9a3y18u4KqjitVFXQ_KrUx-FqS2qdOPr1WOEEj3dKsUNow_aVS5IzU2gGGPgVN0DRSIXAolvL40Gpd0JejJLevJgZfJohrh2SjR8tM6tVkb29E2Wwe2lof3dcZ8BJF86wJJC3C3FwonhZcTfaqtVGkciiHOW-xWjdGqD22E0tn6LX12qXR7je19fsWpBjyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از لحظه رهگیری و انهدام پهپاد متخاصم MQ1 دشمن آمریکایی توسط پدافند پیشرفته نیروی دریایی و نیروی هوافضای سپاه و تحت کنترل شبکه یکپارچه پدافند هوایی کشور بر فراز آسمان تنگه هرمز
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/688269" target="_blank">📅 20:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688265">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در منطقه جازان عربستان سعودی
🔹
برخی منابع غیر رسمی از حمله موشکی یمن به این منطقه خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/688265" target="_blank">📅 20:37 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688264">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VAB2hMsWsGM2fGoyA6QEThrg6vMwE88ZYz4Nfi-VYnUIi94bvzTzRVIj5UAu3Zg3_KrG-4eSNCogE0218ixfayUKFQJAEfisQVKaHDErTc5H0cz4JQCFdS-fhGPJJh9Of5kFFdCMqTWRsIZmv-v1b2YwQghkaETKn_7KL6deTI5JpXkKuX16JoiVIw8UMsdJhX4SUdAtpm7in12ETB-HFnBqG5Q366BkbAOKGMv7n2OwXCrb0rpQSv9SkH6lXSHbglYizwxNaA-zUQIzIzQIq4LXpsN_QtU-GfKr8xyiCQiS3jiGaB1N0rUI9fxmMCZWsV6Ff0D_BI5MziaooGrygA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کمک میلیاردی یک خیر برای جبران خسارات جنگی مدارس و دانشگاه‌ها
🔹
یک خیر به صورت داوطلب با همکاری جمعیت هلال احمر متعهد شده است مدارس و مراکز دانشگاهی خسارت دیده از جنگ را تا سقف ۱۵ میلیارد ریال بازسازی و مرمت کند.
🔹
مدارس و مراکز دانشگاهی واجد شرايط می‌توانند با ارائه مستندات و مدارک مربوط به میزان و نوع خسارت های وارده درخواست خود را جهت بررسی به دفتر مدير عامل جمعیت هلال احمر استان‌های سراسر کشور ارائه نمایند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/688264" target="_blank">📅 20:37 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688263">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/632c2a3605.mp4?token=mSC6V0wmXhOF1nLDk9pOd0S4sq1ixycdG8m6Hw2Nd4P2AK92z3hDKqfS1O1cgBTuxgW1S6HBdOte6Ik9DVHO07aEtrU0469tHIJUEkJL5N5vksmvpxeypwULBdOPw1YOVFZ98G2GWBaRC_7p1xMrv96V29nKktE_5SmuG6CAb2XW-h9IhqEacPoLzZHn3vyKX2PM9D52I3Gi1eBIJTObZVfpYYvA2ZPftPYw0F9Lodk1ULsOhA4RzbkQ_63Gy30uGI0dF6AJycrR4THA7elbgHM-oFJGyFnn8EJDb4qkylf53zLR_X9ep4guFu3COn2H17_ydtRpeMbVAjVjEzKxkxP_SKmYCbLT0I4uqxx-wu0ewdswQ_YqcpbEqtLRV1K7fMMAewUAAaLJVZrMke6n5X2rkag4r_TtQLFL97Gz11KmFPDk-fMAUlVLQvAhRsYRjg4plSihF2CK7ckc5wMlc-3Dpv8pP_nGoOjZwsKhoxd-tDIhhqH6Q1CNIYd3zAY6Esj2CNr5c-Sd4LZ1Ox8B82JthPQJhxF4nwSnCiVRgneeegZugtfmwNEyi5IE4UUEASzpZhBOWiuEIJdk6La8DRZeRxSdQ2lauLGNhPdtH85mKgyfDeWcU5e_4z05Bc5KdOPDpKgHEnnC3p0G_jY84QWec6_xu1D5bgF0E_3Fo3k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/632c2a3605.mp4?token=mSC6V0wmXhOF1nLDk9pOd0S4sq1ixycdG8m6Hw2Nd4P2AK92z3hDKqfS1O1cgBTuxgW1S6HBdOte6Ik9DVHO07aEtrU0469tHIJUEkJL5N5vksmvpxeypwULBdOPw1YOVFZ98G2GWBaRC_7p1xMrv96V29nKktE_5SmuG6CAb2XW-h9IhqEacPoLzZHn3vyKX2PM9D52I3Gi1eBIJTObZVfpYYvA2ZPftPYw0F9Lodk1ULsOhA4RzbkQ_63Gy30uGI0dF6AJycrR4THA7elbgHM-oFJGyFnn8EJDb4qkylf53zLR_X9ep4guFu3COn2H17_ydtRpeMbVAjVjEzKxkxP_SKmYCbLT0I4uqxx-wu0ewdswQ_YqcpbEqtLRV1K7fMMAewUAAaLJVZrMke6n5X2rkag4r_TtQLFL97Gz11KmFPDk-fMAUlVLQvAhRsYRjg4plSihF2CK7ckc5wMlc-3Dpv8pP_nGoOjZwsKhoxd-tDIhhqH6Q1CNIYd3zAY6Esj2CNr5c-Sd4LZ1Ox8B82JthPQJhxF4nwSnCiVRgneeegZugtfmwNEyi5IE4UUEASzpZhBOWiuEIJdk6La8DRZeRxSdQ2lauLGNhPdtH85mKgyfDeWcU5e_4z05Bc5KdOPDpKgHEnnC3p0G_jY84QWec6_xu1D5bgF0E_3Fo3k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آمریکا و اسرائیل نتوانستند دستاورد راهبردی علیه ایران ایجاد کنند/ ایران همچنان یک قدرت منطقه‌ای باقی مانده است
دکتر گاردونیو، تحلیلگر و استاد روابط بین‌الملل دانشگاه UNAM در
#گفتگو
با خبرفوری:
🔹
ایران پس از ماه‌ها جنگ توانسته هدف اصلی خود یعنی حفظ ساختار سیاسی و ادامه حضور منطقه‌ای را دنبال کند.
🔹
آمریکا و اسرائیل هنوز به یک دستاورد راهبردی تعیین‌کننده در برابر ایران نرسیده‌اند و نفوذ منطقه‌ای تهران همچنان پابرجاست.
@Tv_Fori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/688263" target="_blank">📅 20:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688262">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
مدیر سامانه هوشمند سوخت شرکت ملی پخش فرآورده‌های نفتی: کسانی که کارت سوخت ندارند با مراجعه به سامانه سوخت من، یک روزه کارت سوخت دریافت کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/688262" target="_blank">📅 20:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688261">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در منطقه جازان عربستان سعودی
🔹
برخی منابع غیر رسمی از حمله موشکی یمن به این منطقه خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/688261" target="_blank">📅 20:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688259">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e52aab7547.mp4?token=dfbZc7_yRUK-gRwF_pDl99IgnP1VhsD5eunJtUFhCavqqH0cOOh7ag1A-UPYprIAJFOlgaUnwIwfMoSPXxQ8k8_W_qCi2wIjSG-Q_qEvH5bf0RJFYiDmu3mTgNqcjJDVwat_QkPSCYB1pbLkFyJ3J8shENDsCbVLQBcGEfmyEg3NbIy1xLEkfDjrVXuyg2NlNtjWEIa2aD9MrAgxcywUsrFQAHAAQKS8vRQHoVRUlRARgA5CiqSeoqlGIOkqHC5taLwVjvuA5HQgE4Ibpl66jJG0at0p8RAsBN111YC4EHR3-qYAODeJstvmnJ3CCmc8Q6-iY2QQAz9CYqarKoFUig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e52aab7547.mp4?token=dfbZc7_yRUK-gRwF_pDl99IgnP1VhsD5eunJtUFhCavqqH0cOOh7ag1A-UPYprIAJFOlgaUnwIwfMoSPXxQ8k8_W_qCi2wIjSG-Q_qEvH5bf0RJFYiDmu3mTgNqcjJDVwat_QkPSCYB1pbLkFyJ3J8shENDsCbVLQBcGEfmyEg3NbIy1xLEkfDjrVXuyg2NlNtjWEIa2aD9MrAgxcywUsrFQAHAAQKS8vRQHoVRUlRARgA5CiqSeoqlGIOkqHC5taLwVjvuA5HQgE4Ibpl66jJG0at0p8RAsBN111YC4EHR3-qYAODeJstvmnJ3CCmc8Q6-iY2QQAz9CYqarKoFUig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مدیر سامانه هوشمند سوخت: در خصوص انتقال کارت‌های سوخت به کارت بانکی، طرح شناسه‌دار کردن کارت‌های اضطراری را کلید زدیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/688259" target="_blank">📅 20:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688258">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8dcWAFSd5-9DzjYasmbM0T0LkzOA1vjRvL55rP-3AXp2wXs7J6JsaQjCsgTj4lVjIijRJkNYRUzkV5T8vt19xGG56G1-AysHgH8pCRL8XrOe191aXvQ73d0zxET8ZVzig6OP7hvPfvEjzuDRKpSYiLfkGoIw7r-9TV7YoWLWKCHQJC_KIc8uMp9N4N59JZBOjPoWof7zbEU3rF0s61uYlaF_Yha7SkUl-nZpNu7UGlRlbsYBX6TGnfGr3Op899Em-x6tsLRGcg3Y2ftZ6QPveQVlVOLJakZSA0VCD8llyLMdCh3982q3jHmlJNE4r__XtDgWc2DCRtYjoOq4jIA-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حملۀ اشتباهی جنگندۀ سعودی به مواضع خودی در یمن
🔹
وبگاه خبری «الخبر الیمنی» گزارش داد که یک جنگنده سعودی روز گذشته مواضع نیروهای «العمالقه» را در استان تعز بمباران کرده است.
🔹
طبق این گزارش، ده‌ها تن از مزدوران وابسته به ریاض در این حمله کشته و زخمی شده‌اند.…</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/688258" target="_blank">📅 20:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688257">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">13 Ane Manaee (1404-01-27)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/688257" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه سیزدهم
حجت‌الاسلام امینی‌خواه:
🔹
وقتی تقابل حق و باطل به مرحله" بود و نبود" رسید، مذاکره با قاتل یعنی ساده انگاری سیاسی!  [01:06]
🔹
تقابل نظامی و هیاهوی رسانه‌ای دشمن، نشان استیصال او و گواه قدرت ماست. [11:15]
🔹
اهمیت شناخت و مقابله با “مُرجفون” به عنوان عوامل اصلی جریان تحریف  [18:10]
🔹
مهمتر از اِذن رهبری برای مذاکرات، هشدار رهبریست درباره عدم تکرار تجربه برجام!  [31:30]
🔹
"پایتخت"، سنگر مقاومت!.. نقش رسانه  در تقویت یا تضعیف باورهای دینی و انقلابی.  [36:20]
🔹
اِهمال در تحقق خواسته‌های رهبری، گواهیست بر شکست‌های ناشی از موانع درونی و نه الزاما دشمنان بیرونی! [43:10]
🔹
مسئله فلسطین و غزه، تکرار تقابل تمام ایمان است در برابر تمام کفر، و هر اقدامی دراین میدان، معادل عبادت ثقلین! [46:30]
🔹
تبیین شرایط حساس جنگ اُحد و نقش تاثیرگذار حمایت های کوچک در میدان های بزرگ  [1:15:00]
🔹
پشتوانه الهی؛ برگ برنده جبهه حق در تقابل میان جریان‌های مختلف و تضمین ظفر نهایی [1:31:35]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/688257" target="_blank">📅 20:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688256">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4XP6QpZfK-fvviO_Ixsk5PsOR3UBaMZjuBs3WlX_wAzLuABh5mFiIoANLwK5ZXG77JtT1FiXxEX8oa-KNrDkkAInlH-EFFhKRbyFXMpTuEYR9UQWEbv9fREb258gXouImX-A8qL4_T5qXttM5ZoW4a3VFFFS29R4x0fo-p3IGYt94kzZGLoLvzsxhXjAwFB15Us54e6XCm4MGJ_SJrq8RBv37xVikk_7_l8RmAA8wxBAiCA_vrLeWo9fY3f8-NDM8fL4Oc3I5nGV6sa8W5NXNypWuRGvate8BGZnwx_YjRLbgT0Fyix8ClgFDWFyPkbUfPzWBrfEC1EA7jwhULRww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترفند پلمپ کردن برای نگهداری طولانی مدت برنج
😍
#ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/688256" target="_blank">📅 20:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688255">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UV0ZcOLF--0P7fJ7VeYaARLl7_Tq_Fh_So4N5-hU5qGGAhuAP76sCvSNfC6qkvgsbVNp5GOSPwRHSGjcy5F7uSDJwfVM_FAUGiMxdvcTZvwdz6V5_575m_2fBUr_kLORtlPjWo_abqAERDNl6A8ctPA_C6i478jgOFBdMqZZ2A0PhLDlH6Lm_dTEhQCf7TGHPuHonh0bZenT-tk38whVPWJ0IC_0xavC3B16_k-hifJ8rS4cpfSE4wEhtu0q3jmGwhL8U7VSOBOyRHxARw9yLeL8HRLo_7KnNdreJS4NUvEoVi_9KcYiPQqc09gSw34FtdPSU9dXcOCf9VCL00BQeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زیر سطحی هوشمند Dive-LD یک زیردریایی خودکار آمریکایی با توان ۱۰ روز فعالیت زیر آب و عمق عملیاتی اعلامی ۶۰۰۰ متر است که برای شناسایی، نقشه‌برداری، کشف مین و پشتیبانی ضدزیردریایی طراحی شده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/688255" target="_blank">📅 20:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688254">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7emZFsuKC1VkJ0KcxcNH2-EwuzVW7gWJRncWdyy7Yko9IJpOeqb-y5eaPlZZyM31Desp3bgwEfdXnSdyFr38CdDCrZTwJCgPRMIlgVBxqBG2kH0xBvQdse3mAn15Sqs-3nkOD8h9Cp61mN3mduv3_se1UNci9JfRIhRFH-XDNInEPVUUoMf3p8255gZBeUXso2Athwp5VdCbqDM8MDSRhcVbPaQC85g0BfX-rojU7J3dmf-WR21ERYdjj-nkvn9tYTF_wc2rT-dZiMD-X9_9VDzuG3wP8x7QSb1juJ5Rp_QggixN8PyRKVsE88Yp7MD8xCd8SnGJ98vOs_V2UsNyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون علمی ریاست جمهوری : دوران صرفا «شرکت‌سازی» تمام شد؛ فناوری باید به بازار و ثروت برسد
🔹
حسین افشین، معاون علمی رئیس‌جمهور، در نشست شورای اقتصاد دانش‌بنیان خراسان شمالی
از تغییر رویکرد معاونت علمی در حمایت از زیست‌بوم دانش‌بنیان خبر داد.
🔹
او تأکید کرد حمایت‌ها دیگر صرفاً بر افزایش تعداد شرکت‌ها و توسعه کمی متمرکز نیست و باید به سمت
شکل‌گیری زنجیره‌های ارزش و بازارسازی برای فناوری
حرکت کند.
🔹
به گفته افشین، ظرفیت‌های علمی و صنعتی باید از مرحله پژوهش و فناوری عبور کرده و به
تولید، صادرات و خلق ثروت
منجر شوند.
🔹
در این رویکرد، اتصال
شرکت‌های دانش‌بنیان به دانشگاه، صنایع بزرگ، بخش خصوصی و بازار
برای رشد شرکت‌ها و بالابردن سقف اقتصاد دانش‌بنیان کشور در اولویت قرار دارد.
🔹
پیام معاون علمی روشن است:
زیست‌بوم دانش‌بنیان با تعداد شرکت‌ها بزرگ نمی‌شود؛ با رشد شرکت‌ها، ساخت زنجیره ارزش و تبدیل فناوری به بازار و ثروت بزرگ می‌شود.
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/688254" target="_blank">📅 20:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688253">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCHUTCOswoRRuB95BIWO8H4EMa2OQwUa2Uutbomi8kUAsqMSOQTBSPTPC_Twg1Uf2FlkkPJIEmAKUipiIwpuN98X1x_pdzgCNTwSQQRIHJuLiQBPcIg245YysEpMuotoXuiuEMji2H9vtbty8zEspzkptwT1Rdk-kMx2GY31jxnDFCWI6axNkS3LNKTcnxXegdb8o-BDesFMJORRnbIUAeEu5kwESW8cMa2hANII4DWTmx2HEsRPsZMYpQgJwYmc3oyMA0w8wzQrSZyPEF1wP6onkrr3UuSTXD2ZoKJwkbvIW3H6ETBQ2OVY1i8yjDZKDsJNNZbRIPflqlvDxlk6aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشتمین نمایشگاه توانمندی‌های صادراتی جمهوری اسلامی ایران  با مجوز رسمی سازمان توسعه تجارت ایران
در شرایط کنونی اقتصاد و تجارت بین‌المللی ، مسیرهای تجارت بین‌المللی را با چالش‌هایی مواجه کرده، این نمایشگاه می‌تواند فرصتی برای حفظ ارتباط با بازارهای خارجی، یافتن بازارهای جدید و تقویت مسیرهای صادراتی کشور باشد.
با توجه به تغییر مجری این دوره، ستاد برگزاری تأکید کرده است متقاضیان حضور، ثبت‌نام خود را صرفاً از طریق مسیرهای رسمی اعلام‌شده از سوی شرکت نمایشگاهی نبراس انجام دهند .
جهت کسب اطلاعات بیشتر و ثبت نام با ستاد برگزاری نمایشگاه در ارتباط باشید
02192002799
09127989492
https://iranexportfair.com/</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/688253" target="_blank">📅 20:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688252">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pw8wuB7NXXG0AaoLQnQixaWhU3xz3eKCNCBeyntM5y3fagmzTb0S5MkcCvPQXhAbjinGrLEV5wUesdFaxwwJP8NDc6wx7THM43AUSOngo1acBBGP_sav2umbwHyLRI2D42KdM7Mfjai17tX8Uexu0dKuJPeg6Hc9aXyVZk1QfWbXDH-u-0cRvEczUFCVODxSJoVnME_59WTDQ6a-MugogJWkUWxVjNiikv0A2NgRegK0WbcYoKaxm6Vqmy7vGEAtVpW7lPRh_29ZDXX-DP2d2K0kE2tfJ4IrbPR_Mr5QJbUrLnhhBdCriachRBixVpOsDGEYLCdovbapjRovFdMQBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعال رسانه‌ای آمریکایی :چطور ممکنه چنین چیزی بشه؟ مگه ترامپ نگفته بود که تنگه هرمز در اختیار آمریکاست؟ من هم فکر می‌کردم ترامپ گفته بود توان نظامی ایران کاملاً نابود شده.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/688252" target="_blank">📅 19:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688251">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0aa8cbfc5.mp4?token=NRPQysIRMq8deBZpbRxQD7PN3MtX2JaCijGGbWcPszuBoSqqPKBZj7MvB0MOWRNyyPpvZn2WLwaomJamSzu4MnHH98Vhon9cMXIE4cmTHK1QempIVMeeA-zhPn82ENZZ9aGAUbdiOqFrVEvtBd6XctshWpszXBn2curbvs1lMgN5EFwTg4h0CdDMx-CgEH9LA0bmOS_wlB0bpspAxnaZGYehl4M9paAY2aWjIMXlMAYr69KEWpv0_oCzyC-naIIUgeU1JEXyYoQV_8Hzk5CVxGuOgGJbjMgtrFOP3_NjiOrwhDVFI927SCgxF_J04K5xOS8O9Px8S_xV_4wbOVEZng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0aa8cbfc5.mp4?token=NRPQysIRMq8deBZpbRxQD7PN3MtX2JaCijGGbWcPszuBoSqqPKBZj7MvB0MOWRNyyPpvZn2WLwaomJamSzu4MnHH98Vhon9cMXIE4cmTHK1QempIVMeeA-zhPn82ENZZ9aGAUbdiOqFrVEvtBd6XctshWpszXBn2curbvs1lMgN5EFwTg4h0CdDMx-CgEH9LA0bmOS_wlB0bpspAxnaZGYehl4M9paAY2aWjIMXlMAYr69KEWpv0_oCzyC-naIIUgeU1JEXyYoQV_8Hzk5CVxGuOgGJbjMgtrFOP3_NjiOrwhDVFI927SCgxF_J04K5xOS8O9Px8S_xV_4wbOVEZng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیشه دودی‌های جدید در چین
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/688251" target="_blank">📅 19:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688250">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
فروش برنج کم شد
محمد مختاریانی، رئیس انجمن تولیدکنندگان برنج در
#گفتگو
با خبرفوری:
🔹
برخلاف انتظار فصل برداشت قیمت برنج کاهش نیافت و همچنان حدود ۵۰۰ هزار تومان برای بهترین کیفیت برنج باقی مانده است، علت اصلی افزایش نرخ ارز و فضای تورمی است که کشاورزان را به مقاومت در برابر فروش با قیمت پایین ترغیب کرده است.
🔹
با وجود تولید خوب و واردات منظم تقاضا در بازار پایین است و مردم توان خرید ندارند، همین ضعف تقاضا باعث شده قیمت‌ها بیشتر از این افزایش نیابد، در غیر این صورت نرخ‌ها بسیار بالاتر می‌رفت.
🔹
درحال حاضر کمبود برنج نداریم ولی کشاورز تمایلی به‌فروش محصول خود ندارد، زیرا کشاورز معتقد است قیمت حال حاضر برای محصول خود کم است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/688250" target="_blank">📅 19:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688248">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjJ-vDL12N8f3FlFb86sKu3t9gEP3yjUY0QqvDqiGHy0VBJxp4MYg8NHmj_yxpaHBw_ABrmYX_nVEC5OAjV_d0QzLVpEpnA2ht-UJhfUCqck2NdpcSzjNUJ_cbNEOJVmkHarzjSKeYTack7tuJOXo5Me_NvQZlIGDmJE_IcNbVfKR9nYBfCW9xZuBnWpzOFLZ0FULBiydg9iyYvWfykZTGkVrLv0x9JYf-dNzAxgYaq45vjP3r_GPJQayvhJfjbk6lfaBo-4bcwC_y_Iqu2WYaOHLtbH-Z0i_ObnW2tYcva_-E7txgXBiEJC5XMjfDwDumWjL9o96dQppFY_5iWJNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۲ کشور خواستار محدودیت تجارت با شهرک‌های غیرقانونی اسرائیل شدند
🔹
فرانسه، بریتانیا، کانادا و ۹ کشور اروپایی دیگر در بیانیه‌ای مشترک از اعمال یا حمایت از محدودیت‌های تجاری علیه کالاهای شهرک‌های اسرائیلی در کرانه باختری خبر دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/688248" target="_blank">📅 19:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688239">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ei1sElqJV-Kr8NCe4sYVz38zu_6PemwJcCkmOICKNMotBtPRPr-YeA8wNKwuc8dm0MdTOtbTz_I3hydHkghIzNr4uZobGO5T8TgmrAv4-0RYdymN5lTKuxMEEigZ-jq41QFZTXhvirhLFoA0Zw5QG56TZU8ILyKYxBAk4q1Gh6buB6I_dzhP3UeL_QQ8D0Wrh3k8Un8FYEH9fL-0RiCbIeZo4cpvLy2pVcJxQwetylBLgb_9R7QUghrJf-_a3BaMFQzrJL0Tfs9pIpSHDkyqEPLRhVPs5yvwbDCl8XZLh-9zH8hTiAomywd7QZYLQ0wMmxbiXl3dpX7l6tHm8jO5Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tFxMa1nhgoAUvf_8p6xVXNxZH9oQ5HmfXPXAw6A7enboLjIL4WT1HL70JqlZFa2U_fIe0qzWN3pG626LFxwJtAowux_sn5nJ4140jjPXgttaKdAjfnOsG5bySq_i9xwgXvruuAeNP5RgOwZWu1Qtekwf-Yl2LUpo8tqoFxIs13rNq4tb-Y9BTPHCfvwDJjjVllupO0YAubAtVBN3rpsAuKfTmczep1vajNMo1l29q8oXqB8Kq4bJgoVNy-MALYM4OlaNXTUzN1yGqvVaWymqDcrlXFf6p-Dhu8iND4CCywYQR0cKf2Ei4rWmuMbLPvGfjHLqFskniP7y5w2SceM4cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sZKCQFe1brgBFFEq1knL4nI7arZ3QhyA7AVXlPHNpuhzG04eXHIabf9j9BwJ9ZlWrazmqEO7gDKBswweqUl6fZ2nnmJ2zqUNbeir19BLPmHK3QhuyBZlcY0sDP77WSKJFuC2jRfCTFjN7JNozX1Mk6L4ijthO-69z9x7Txgp02YHAcRZx61ezJKhHxizdU_Q0HZ-hPBk3bt1dJxtkIp9L9F4RToHELTAZHQy9ECQQx_y9J6yFBj_xptyapnReaaMPTGttOqvGyzzTzAmtMPJU_Z6yFmD80vT8eeMWbDrOZEkt6VXUkBEnqiuSl_yaqK38MJ-_GYgEiSvelxl_Gv6RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TGeleim8YrH7fP95qaXVeUNLWxQc1fetFyElhVQcE4yzHPLkVDWfzrGLiawv1mQwAi0JrGKw_P5m7PQQzgQBzxR99LtKkWIw0--ItI0scJV1I9-FXMV6nc5gIQeOeImyfuN3F-9ihUEDw6FwkEmj5-sxoYESsSNuz2EzPe2fLdsKj8ZCCwcCq0-LzR-gZ5FBZ4fVDoLfSeb15h1OwxiVXWV4IGkzVbZ1VKO27acI5Db6U5Cnfc2w6UsP1kb49uk5232lw7VXgGGWsGBHQc0RgQ65mX8GYTCDWJCzyeIJm5YmYMxF3Dpn-d7ii4DJ1G5SlhEDFXLn4-Rza-LawI_Xjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vSfSHfpCEv4g5WZR5NYcrJqUE_a6pzDTm2d_fKe-IbNZolUq-QaEFTZolTXmnv7ac9jOKhCPy_MwIB_xW8vkGtvEOcru3OqQ10s_0nsL5t81qUOFok_zjfuOiyeiUDbRHUXr6e2_nLheOAxX9ZimvgNVKzRwdQDFpHl6GYZA7CUJwptzzSAg96YALnQKwDsG2ccoHJGZhdVsW2TojF9Ozc0lVzaSGfJMkSwTYcBhigUk8YQPw_r8iEqabgRbKUrcJyBAtbOlDkdzANRwK1EM3a4sEqJhjxT-3AooOWwATsZ_VCpQYn8UsuuTR-A6hNPy6l6mpK-4cxJRmHKlRivU4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YRMDE-5Ci1YpT0BIPh-5Sr2xhyridpVP41Y7glyXDwY6iFFcEzVbssGTm8EpTrw2EUu7JNKBXT7umS6PNVKmkTPkP8pMCScvXXS7uBwcJbzNyHRWSDng1byEO1SDvxwxgs95Y2Pij8lamCMi5idQj3aZLOnXcQLuUDr6V095_EGMxx1hEw73xa-BXexseDdB9H7bg6GZH_p05I7QFjvT_PKKV47UfX5K4Io2xMzryNaiBx1xKxhFimRR8z2kM_9mmiC6rnrQozuQtPLUYmxDGpgu1sUR70mVbMDK9S5iMyCp7kw4sNsgUZ06unEkAUaVB6Yh4N6vGr6akD9xNWzHfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cwWm6Zl-Fl8CI5oRoKkGh5xaVlGCau7XzD1ixAFXMGM1XBJdXU9FFtjuk8i8xlQpUgZkRZ9tL8xjbnQWNKRr1SR9ChrogeivvgEYPr3yyFpBUmiItJ43ed3uiRvc-YSivamHH0tA2dpED4X_nk-l8jSPD4WsMhAREIah9Xp7aO3PU5XHvf7IfYXjyrCmm8HnlzEeUyQDd2Cn1yw4Nf_ivdBOJ163DUh6ArTR8SXkDtVi7vPh2TQYV09s4BDasIWpFpqEPrXOJ-pD8eiy4IJqSnM8a0b-1LClMUxikOJh4kiQdhRxTc4mChSF4922FXwIMQTYiIFsCBOdmO-Ad4sjog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dCubNeHvJBE5B4imhBBxUfKawuJaeNeitMaXG2tVS-zCQzA9BDVoRPG1-5L9hxeRHZ_Ii9uNRQvgAVK9MiZX0KVJ-87knfhCk257pMKx2H40H-wOFHbZTCIJW1sFl-iDaq-MwHgLrPwLnOezcoYz-PP-aZT3znpFZ8EmfmYTRS-shfGLQT2EC5pM8hohBjBlaGJlcs-l7kFoiv81elMhgsIy27-zLEp2KDZSZcgwOTX3j-F0H7Hz0RHI6yy_nqhyeAazFwJSvxNVQ0cAnf7Zdz_zPJ-lsHsWMiedyCatPncpAkNhc7h1BMpyuqKfL7L1ZxiAW_ej97szbVg1GQv2bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W-_oIGZgKlNbJEI--4zJNMdnseGiedfmDi5mF8Kcoe2OSz4pvHt06myoe8gdv1WLBoGmIwZ_lg2N_ixn2kwVsAbd2Yyq0XE167ulaY8KWUetiw6wr-eu4vmlX4B3w-9fLGB0jb_zT21DA6NPo1p13LSKCZ3kXWCWkQBiExatpcJCOWuAJVSdZxGPkNAaq7wfQmCQlA8Y_cH8u2OTgfAZpyDu_V3D73cx1WI-sR3KpH4qrPNqVnWjmkys4RycRz2RTaIkXr5tqZzmh6RQpZeQv8foaM3nsY8u4MEZj3Wt0yfMTz6Gg8kvN_U5fjocIhC4mOYeFgqtUEWjntGapFnogg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چالش‌های شروع سال تحصیلی
🔹
انعکاس پیام‌ها و مشکلات مخاطبین الوفوری در آستانه بازگشایی مدارس.
🔸
ما پیگیر مسائل و بازتاب‌دهنده دغدغه‌های شما مخاطبین عزیز هستیم؛الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/688239" target="_blank">📅 19:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688238">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
ایران و روسیه برای ساخت نیروگاه‌های هسته‌ای جدید همکاری می‌کنند
🔹
مدیرعامل روس‌اتم از برنامه ساخت نیروگاه‌های جدید و نیروگاه‌های هسته‌ای کوچک در ایران خبر داد؛ هم‌اکنون نیز فازهای ۲ و ۳ بوشهر در حال ساخت است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/688238" target="_blank">📅 19:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688237">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
سهمیه بنزین خودروهای نوشماره و وارداتی چگونه است؟  سخنگوی کمیسیون انرژی مجلس:
🔹
خودروهای نوشماره و وارداتی طبق روال قبل سهمیه‌های خود را دارند و برای آنها محدودیتی در نظر گرفته نشده ولی باید هزینه نرخ سوم را بپردازند.
🔹
در مناطق آزاد، نرخ سوم برای خودروهای…</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/688237" target="_blank">📅 19:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688236">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4550cf9175.mp4?token=ZaVmfbSyu8OXOat7VgOfFMD7y17drniKxKiRvA9x7MnSowjNYmH7oF_hbCAQE-ypKrPRJy7w8MsYnr3AtLQ-O12AxS1-aBlxe841y3CJ3nvFUsYo2SO0nlh8JnDsI74ehtc-dRHwsmxYpjyv8-zK1bjZe7BQKafMn3YwqioXjkSF2kss1ZrNQACG8lUPP-B5X2VjolRupUw0s4Livgc3ocYEualKXuWZ50VhNf8srSyX8sH90Y5UVqQzHaUpQ3r_Jd5pmLvm4sxgIA3LgUGb4Tf93VDxTppr479I5n9knK4Qbvqr4tLldQ-znJKAxSVCKSs6z-Msa3MJGGMfMphhIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4550cf9175.mp4?token=ZaVmfbSyu8OXOat7VgOfFMD7y17drniKxKiRvA9x7MnSowjNYmH7oF_hbCAQE-ypKrPRJy7w8MsYnr3AtLQ-O12AxS1-aBlxe841y3CJ3nvFUsYo2SO0nlh8JnDsI74ehtc-dRHwsmxYpjyv8-zK1bjZe7BQKafMn3YwqioXjkSF2kss1ZrNQACG8lUPP-B5X2VjolRupUw0s4Livgc3ocYEualKXuWZ50VhNf8srSyX8sH90Y5UVqQzHaUpQ3r_Jd5pmLvm4sxgIA3LgUGb4Tf93VDxTppr479I5n9knK4Qbvqr4tLldQ-znJKAxSVCKSs6z-Msa3MJGGMfMphhIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گران‌ترین موتورسیکلت اسکوتری در ایران BMWc400GT
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/688236" target="_blank">📅 19:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688234">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/489bbfab88.mp4?token=YtoMxidaJd6QD0uaJ2sm7OGc4A9QoWed47WCRa7DU5Bf0QcoREjYRMYIukRTM5MAHV429wYis-0KHxLC_orm7ED_oMRREbG0OloM3RXWG1UkbDF3Ka6DpyLTcLmBHrizYiJkB1V6M5iRlPd8V8wg0MARkz9nGgyBMyHxC5my1d_e_kUkQrNoAfiZAKXe7mr5R5chMPRMpzNJvD112I2iuh63t5D7mpt6phpOScbX4VtsnjXt5SmDPC8-fYjujSpcSMBlHFJ2XJOnOnrF8ObMimL2YTxQhHsApLPvfd_y1DUJRyhtRf6lHxVyATvuOEtH2wBSK0Nj2jeI80FP4Ko47A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/489bbfab88.mp4?token=YtoMxidaJd6QD0uaJ2sm7OGc4A9QoWed47WCRa7DU5Bf0QcoREjYRMYIukRTM5MAHV429wYis-0KHxLC_orm7ED_oMRREbG0OloM3RXWG1UkbDF3Ka6DpyLTcLmBHrizYiJkB1V6M5iRlPd8V8wg0MARkz9nGgyBMyHxC5my1d_e_kUkQrNoAfiZAKXe7mr5R5chMPRMpzNJvD112I2iuh63t5D7mpt6phpOScbX4VtsnjXt5SmDPC8-fYjujSpcSMBlHFJ2XJOnOnrF8ObMimL2YTxQhHsApLPvfd_y1DUJRyhtRf6lHxVyATvuOEtH2wBSK0Nj2jeI80FP4Ko47A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آبگرفتگی شدید معابر رشت| هم‌اکنون  #اخبار_گیلان در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/688234" target="_blank">📅 19:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688233">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mlHoaMKxjoqLQD1NoU1WRACLQyxqPFnRXlonaRyKhygHukzsPHtJMnVbzILOEvgz2QdK9J1Rndcl2dw0Kr-rjakurthG5_q9Uu51LcpmlVBnPtTK7-p2tirpifNDHmSe4APxvvGE_uiPuBqvWEdVL-IQ-F8Rb5-z-Ayyxo7lS7nBxPC0CvsgCAPe12oyJEMGyuQqQ1tzJZGn87s2mPuXhWFn9esBJCpx5HXWJ7r9_xtGaUu-H8MGezq_rn0xo1P4eS2pYu3uAq2SotS1lmUaRI5w-yMB1wW5kYIpxWADRe3MPgjPkWCY45ubxifBXdY16oBQ_ST2qa8aTl4ZEpH8Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار مجلس درباره وضعیت بازار لوازم خانگی: قدرت خرید مردم به شدت افت کرده است
علیرضا سلیمی، عضو هیئت رئیسه مجلس شورای اسلامی:
🔹
بازار لوازم خانگی بیش از هر چیز از افت توان خرید مردم آسیب دیده است؛ ادامه این روند مستقیماً به کاهش تولید کارخانه‌ها می‌انجامد.
🔹
مردم خرید کالای بادوام را به زمان دیگری موکول کرده‌اند. وقتی سفارش کاهش یابد، هزینه ثابت کارخانه بالا رفته و فشار به تولیدکننده مضاعف می شود
🔹
فروش اقساطی باید احیا شود؛ البته نباید به شکلی باشد که هزینه نهایی برای مردم بیش از حد افزایش یابد. منابع اعتباری باید حتماً به سمت خرید کالای تولید داخل برود.
🔹
حمایت از مصرف‌کننده فقط با کنترل و سرکوب قیمت رخ نمی‌دهد؛ اگر درآمد خانوار متناسب با هزینه‌ها رشد نکند، حتی کاهش قیمت هم مشکل را حل نمی‌کند./ خبرگزاری میزان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/688233" target="_blank">📅 19:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688232">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T59agTXvkJSr_y7cSu6SYqZ2e8ySVcS8Cjco-Ep3TBuH3tNzr-tAJB7ubDAhuB8yZ5fY0Fxo8JPIMn4Bl5RsXQ39GXWhxXtiZXQg_KNGdbMxaStnQ-mmOqdQ3mJ0EaIHJdr7aaQRRzM_CAETOwkrQqC0dBnvWtomfy5BoY7ATLoykM7c6E02QLUIWnGts086NQ4XC8cChbSTgbt0UQhf6ZxzwEEf_71xRiF8n9OTeDLqupr_jF9mswwcnUdO6lebxa4oYAPBaxotdegpr8DQcPxYnq47VVEAFtDRax54tRKu_7uF0CtfmsJlNIv1j6halJLAThLunW3bWrnC3C8P2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در فهرست تحریمی جدید آمریکا نام ۲۷ شرکت هواپیمایی مسافربری به چشم می‌خورد  وزیر خزانه‌داری آمریکا در بیانیه‌ای:
🔹
اجازه بدهید این یک هشدار برای کسانی باشد که با بقیه شرکت‌های هواپیمایی ایران کار می‌کنند: شما در معرض خطر قطع شدن از نظام مالی دنیا قرار دارید./…</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/688232" target="_blank">📅 18:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688231">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUnVmuHKWCVabwnBrMAO1FPOYRdbPzVXTWJ30XHpMgrLv5T4vTf9O8pxhUiD8CUEy0Fxpo5M6Vszc_UEWq3Xb0WPIY-nwTY5xhe3DIyXECIwGpPXK8_iVkNNMogFcrWkIxMXDpCX2wTfDCnpQgvEUeDo5yGZz1XhlX8w5z3Z-HaHzy3KiXP1K5edjiqhxjmo-qbCVlstzZTjIwCtBkb3PltnUHGY8ng_yTSeozSDjvOJn3fcFEGdAs9A3LcOPZSR24WnCyth-v4kgaV-uY9KN2PTrXjd4gyRbPUTN89ZlIGSvYfOOB6zh4cQ31xVSjkE3F4nG3y-MStv5N7cWUa2vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا حمل‌ونقل عمومی در کلان‌شهرها ناکارآمد است؟
🔸
در این نظرسنجی بیش از ۲۳ هزار نفر شرکت کردند که سهم روبیکا حدود ۵۸، بله ۲۴ و تلگرام حدود ۱۸ درصد بوده است.
🔸
حدود ۳۳ درصد شرکت‌کنندگان ضعف مدیریت و زمان‌بندی و بیش از ۲۵ درصد هم فرسودگی ناوگان را از علل مهم ناکارآمدی حمل‌ونقل عمومی در کلان‌شهرها می‌دانند.
🔸
ناکارآمدی حمل‌ونقل عمومی در کلان‌شهرها معمولاً حاصل مجموعه‌ای از چالش‌های مدیریتی، زیرساختی و عملیاتی است که موجب کاهش کیفیت خدمات و افزایش زمان و هزینه سفر شهروندان می‌شود.
@amarfact</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/688231" target="_blank">📅 18:47 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688230">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
ترامپ خطاب به ایران: آنها دیگر هیچ شانسی برای دستیابی به سلاح هسته‌ای ندارند #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/688230" target="_blank">📅 18:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688229">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65032f5532.mp4?token=fsn6TvF7_5HcupPzMv_AvcHSH57Yqc90y_OdcnuyBpUHXzyXWjV0nBB-Q7fvGifrb02q5aAjxNuUd_5X3j3m0OMNSxvt6o1P5LN-Xq4R2gptbo5f-ZASKk-wmSX1_nJCzo4I_lO8xT5x_FHUmGT62FYG3usu57dLWqahOSkviZCDInml7H0pYjS_z_17pE_Ic_H5TtaPCXLdJ_zfKYC6Jz7lJrEdQK_nqf6Q1w61XoCausx8H4tbp1dugy0ko8_VLP6uzbFaNkpzbYChhIq0wED279CNBym8bqkX71cKqvaE_XlSjwOeSnSu_JgwsYxPBzk3CHIrIIh1FzTigEkrMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65032f5532.mp4?token=fsn6TvF7_5HcupPzMv_AvcHSH57Yqc90y_OdcnuyBpUHXzyXWjV0nBB-Q7fvGifrb02q5aAjxNuUd_5X3j3m0OMNSxvt6o1P5LN-Xq4R2gptbo5f-ZASKk-wmSX1_nJCzo4I_lO8xT5x_FHUmGT62FYG3usu57dLWqahOSkviZCDInml7H0pYjS_z_17pE_Ic_H5TtaPCXLdJ_zfKYC6Jz7lJrEdQK_nqf6Q1w61XoCausx8H4tbp1dugy0ko8_VLP6uzbFaNkpzbYChhIq0wED279CNBym8bqkX71cKqvaE_XlSjwOeSnSu_JgwsYxPBzk3CHIrIIh1FzTigEkrMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ خطاب به ایران: آنها دیگر هیچ شانسی برای دستیابی به سلاح هسته‌ای ندارند
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/688229" target="_blank">📅 18:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688228">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBN3XvaQik00tqnKV3c_XvyPUGg-INjro9EcB3Moh5ziH6gwppcugKrp1rNtQ4qsPUOjNNpZnA9PeNIL8gYbkoCHO-JtkT18s35ybnsghM10E9M10-WTRGsAeJ1OaJUj4nIE_-sM04h1QnvqiThpw-f_yjmXgY18kcVYpCbH3PoKwT7ob8v4fS6qf362wGE4Yk77V8zntF5iJnqihKZbmy_4oayE4H3ILh1wh6nplCnqqagu1yeFJLxdSRGzX4C6DY7Lltraf__zTHh4Yc89Rv8ttHLAMiSxHsW-6OyZoR8IiFZZ_wH7c0xzpddhbGXDHvYJmfNheANiaSFbsMOH7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور «مسی» در بین نامزدهای بهترین بازیکن سال فوتبال مردان از سوی «فرانس فوتبال» برای مراسم توپ طلا
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/688228" target="_blank">📅 18:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688227">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
آنچه باید بدانید؛ Dive‑LD؛ زیردریایی هوشمند و بدون‌سرنشین آمریکا
🔹
زهپاد، Dive‑LD یک وسیله زیرسطحی خودکار بزرگ یا Large-Displacement AUV است که ابتدا توسط شرکت Dive Technologies ساخته شد و پس از خرید این شرکت، توسعه آن در مجموعه Anduril Industries ادامه…</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/688227" target="_blank">📅 18:37 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688226">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad3d8b7e68.mp4?token=n3KKbSepkzG4AtXePGD5FuGJ4h31fjXxd4Sp_YO-yBns-EZwAWAP-G03z1PdbMpty7q92hY3Pa3umhZoWeUBZpVHF6P3WBhZLsul73k6CeHhDDo3DYkbTPHxgEPRKzYb7xM6BfY1j7weV16zW_1NU6HG8luj-wHKHQ-mKXoO8GqcIpQ_4_oefWPcLeM4BmwUJkUBanvvpnwOzMng7TjpvNi5GFUAl9VQa6oKs6FVXfJq5aYSa02X3vFrwfGbvH6FO3ExWA3FzIP_RDG03YLL-3PCafI9IBch4qmuqj1Zy4LVpuwJ0BrrJgOJ-QRFmrnbEtv_w60-pO59a0Ru00uuYqSYW1TBbJ89NRzLroD9DLSxpvOCGgM4QoDnINm7COvhOnufD2K3QCQN7nr8kI8xqkqYztq1xonQtLapdMJ1suwGRdjvNk-wQ89H3hxv360PiZSbul_6TxvlQ3ELOXeG03-q3-p6VCSIptycl0_TR8gA8MNgikuSaJlX6uOmk2oBG4-dpWrtPzWY-v9oi_Atfnj-7JbuuChfeoqy3VbD-JgzdO8sMrZuPz8XhwFFJPQIpXFbx2-CpcdGD8jM4TGrntF2jVoZZVrC3Yh-7fIUltUZaoxUuo2yYjZw-OBQfoujTpDrjGeOHaU4DLx4IXg2Hz3zmVdC_ufNlIiG05DceoM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad3d8b7e68.mp4?token=n3KKbSepkzG4AtXePGD5FuGJ4h31fjXxd4Sp_YO-yBns-EZwAWAP-G03z1PdbMpty7q92hY3Pa3umhZoWeUBZpVHF6P3WBhZLsul73k6CeHhDDo3DYkbTPHxgEPRKzYb7xM6BfY1j7weV16zW_1NU6HG8luj-wHKHQ-mKXoO8GqcIpQ_4_oefWPcLeM4BmwUJkUBanvvpnwOzMng7TjpvNi5GFUAl9VQa6oKs6FVXfJq5aYSa02X3vFrwfGbvH6FO3ExWA3FzIP_RDG03YLL-3PCafI9IBch4qmuqj1Zy4LVpuwJ0BrrJgOJ-QRFmrnbEtv_w60-pO59a0Ru00uuYqSYW1TBbJ89NRzLroD9DLSxpvOCGgM4QoDnINm7COvhOnufD2K3QCQN7nr8kI8xqkqYztq1xonQtLapdMJ1suwGRdjvNk-wQ89H3hxv360PiZSbul_6TxvlQ3ELOXeG03-q3-p6VCSIptycl0_TR8gA8MNgikuSaJlX6uOmk2oBG4-dpWrtPzWY-v9oi_Atfnj-7JbuuChfeoqy3VbD-JgzdO8sMrZuPz8XhwFFJPQIpXFbx2-CpcdGD8jM4TGrntF2jVoZZVrC3Yh-7fIUltUZaoxUuo2yYjZw-OBQfoujTpDrjGeOHaU4DLx4IXg2Hz3zmVdC_ufNlIiG05DceoM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چجوری حافظه قوی‌تر داشته باشیم
؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/688226" target="_blank">📅 18:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688225">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UE_-D0ehDU5z-K1FKCR6cs9TeBW7dNO0Mf3eXGz0lbfuvp98-sFE6_n-ghF7qWpJPEGRiim3EzcMhCPZ-pJzD5nitz1QkJ8qgn4C-gS3ynYur7tSQN1knEehsvlffnpGqk1JHxGvWA6oxC0x5QUsosqp6n0uetuBmtoD9FGlaZpt59gP4XHg9ntkM1NOsR7CgZSLgOpvhSd_jVY0KmRN0WiWinq-CWxYnmvHTg3pLwUhGCWtksi8Wfe7YKBJrR3952BKU1wLe_jKTK1OcM4Lk4URIUkkHJ-VP54dh0nis1t0YjxTYHNEHdRdhiV5gVX9qkun0MDqZ9E9cFfDW8swXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا طلا در بازار، قیمت‌های مختلف دارد؟
🔹
دنیای اقتصاد در گزارشی به بررسی ماجرای اختلاف قیمت طلا در بسترهای مختلف نوشت: حجم معاملات، میزان عرضه و تقاضا، نقدشوندگی، موجودی فروشندگان، هزینه‌های معامله و حتی انتظارات فعالان بازار می‌تواند برای یک دارایی مشابه، قیمت‌های متفاوتی ایجاد کند.
🔹
در روزهای پرنوسان، این اختلاف بیشتر دیده می‌شود؛ چون هر بازار با سرعت متفاوتی به تغییرات واکنش نشان می‌دهد. به همین دلیل، مقایسه صرفِ قیمت‌ها بدون توجه به شرایط هر بازار، تصویر کاملی از واقعیت ارائه نمی‌دهد.
🔹
بازارهای آنلاین، یک تابلوی واحد با یک قیمت واحد نیستند؛ هر کدام بر اساس شرایط معاملاتی خود قیمت را شکل می‌دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/688225" target="_blank">📅 18:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688224">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
خزانه‌داری آمریکا: مجوز موقت برای صادرات مجدد برخی هواپیماهای مسافربری به ایران را به طور نامحدود به حالت تعلیق درآوردیم  دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری:
🔹
۳۶ نهاد و موسسه را به دلیل حمایت از بخش هوانوردی ایران تحریم کرده است.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/688224" target="_blank">📅 18:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688223">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خبرفوری
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/688223" target="_blank">📅 18:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688222">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
شکار یک فروند زیرسطحی هوشمند دشمن آمریکایی در تنگه هرمز   نیروی دریایی سپاه :
🔹
مردم مبعوث شده ایران عزیز؛ با عنایت خاصه خداوند متعال رزمندگان نیروی دریایی سپاه یکی از مدرن ترین زیر دریایی های هوشمند و بدون سرنشین ارتش تروریست امریکا را در ورودی تنگه هرمز…</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/688222" target="_blank">📅 18:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688221">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-5Hi_ZznZar8uqiTlJNAXluatr6AYovEWKRugzArkRh7CWj_rIBZsoijlWWh7m_ugp16MlaeW81loycFagSdsc5q1wFAJjmza9nepQy3OeoVYPoRWphpAd7na9sW9o-yUBLfeN_Z6BWlaCxMVm4Jevk0qpxaA4VNKmtcTvuP_8DjoZdTge6kIaAjygzSi5qF5dULYTXGuf3tnaOtIpbGVrIFuTWMbt3vKoeDGqSSGusEmfVsJeMZ39IAxc3nm5RTxUQXC6nXXBNiIQgYjtxsO7WUoJVlGJ18esc2jSBp5XrHNq7SrJEuAZVVHV06fjrFZ3e-vtOnRCf_ANFDQ5ovA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شکار یک فروند زیرسطحی هوشمند دشمن آمریکایی در تنگه هرمز
نیروی دریایی سپاه :
🔹
مردم مبعوث شده ایران عزیز؛ با عنایت خاصه خداوند متعال رزمندگان نیروی دریایی سپاه یکی از مدرن ترین زیر دریایی های هوشمند و بدون سرنشین ارتش تروریست امریکا را در ورودی تنگه هرمز طی یک اقدام پیچیده اشراف اطلاعاتی و عملیاتی در سحرگاه امروز به دام انداختند.
🔹
این زیر سطحی هوشمند از جدیدترین تکنولوژی در حوزه زیر سطحی در دنیا برخور دار بوده، که سال ۲۰۲۵ میلادی به ناوگان ارتش تروریست آمریکا تحویل شده است.
🔹
گفتنی است این زیر سطحی  اکنون به غنیمت گرفته شده و طی ساعات دیگر تصاویری از آن منتشر خواهد شد.
وما النصر الا من عند الله العزیز الحکیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/688221" target="_blank">📅 18:17 · 17 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

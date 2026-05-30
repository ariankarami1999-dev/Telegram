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
<img src="https://cdn4.telesco.pe/file/sji9SiE5wsGTNeelQ8Q9JKA8Gc6TOrFE67U7HIX51fofm727SMgGXIV3lcWkDdxdIikfDytfHPeW7cZKWzzPrbcXUfnvSImc5J5Dz9ucey-flJygwz1IMVmznAGp5FomtgXUX7c4lfHqatvzAVwSamE0w8VlSrtPCUMZQbosOg2bb8fRWM1AhbQ9tCoJpCvWVJsuQUGTGU3Wj0O8q-0Ps7K9XtqYOohqqt-ll7VjD5cx48v1Fu-OB2C87njGKjagSdB1E5fVO7f-Tc0qnlspm61-VgxkqV9kUu3qhuLnu1j868j0BAQ6wu-HtwMuYpgTrfdim0KJlQX8ZDBTayd33A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 128K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-09 18:20:33</div>
<hr>

<div class="tg-post" id="msg-90478">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pb-9OAGue9OcoYG4tY1SIUU7GRbjzMqixWLgc2X602pb6feSeZUEPbCgFkOQUa_H3rh5ms0RF26YJSg3P9qqDExp5zKmQKcs5c-Z4z9LVLvplOozgztoeDH88ieZOPxZPlktOY0MihSF2pOvolkv06Ioj8m9RVN-OmXp0uDovZOGs0fDnhKVLsjVEa-UojnBLcKrZr1iZB-3-7hZ_Mt39--23R_20FNzU7hjvafdHtHUlhdAFhhf8nNE_5u_eOkkwbz4PNSrlVIE1KsUaxXiTx38GOedJrYLFD1LLKncCt819zdtUvXguS9gTYE3Ziiv-G64dudKfrK5wwy77mz7TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tuuoF5xZSqH3xRaemvyV_9UoszaJZqaPXZH0F5W-pg5QOKGF9NravdYOCEjrpw7A46JMkBzX1BrrNV1XfiP6DiLP4HIN0ctbcQhEC6ys2Dk0oc7e5acbs4S0GZKERr4FFkdutwDBpijJHE-yy7CyQdxrvPe5SxetmvUqDL8UxXQsZ9kI6AIl1AmnUz7tfl4dugJptaizMKBIU2d_AYaZMX0EWWd-ONwWJ5LRPmv6kxlmDTLBfqXrO0vxZNFOsg9zCWDd_pk2sxUlSnAimFY9dhDfR-TKUS6qM-VhVJD79kXQVIMWUHgn4etpkhI5VUdlSakPb28CEQMe7YeH95Rb4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسکواد دو فینالیست ج.ج قبلی و مدعی های ج.ج امسال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 215 · <a href="https://t.me/Futball180TV/90478" target="_blank">📅 18:20 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90476">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VhgMv-B73FDLNWiXM3hZ2jCArF54UU9zeHkmXA3r4C9PEfKUpn1EQlTNMUkqmsNxdAN1Q-uMaVOu2R4OAezhzyo-gfg-sFdv7mc8C3etw6EIHU7B8CGdXIy3dCRhXKFpSfrFpJ7FONuVhq0uzNOQvT6ojortoqKjxfzr6C1kMEGldq-s0Jbp6E_LXTjCb0jSudrLG2ZWdQEBxpQobcE7dqDyB-AhMKeQn35ghMfz0X-uCL-TVLxrc9tSIkdAqMCPELvvdHdPwmBD48sxmLTNI2C87S3nTqtxyC93Tgl8C6Op0KQGQ9R1kOvnFA_y1ODn3BD7UrgdgAuIkg39t8nd4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j1MhvFcXu5Lggbm9jH0npklyNTPiFC1HXOOQvf3ruvaUtx0zmzP-ckznUoU7_EusCWKjhpd7fGZJTgdq2HCcXSNXifeGWfXeqX30LLZQxbCqUjqxuPrpVlwKwFq30E6OFHXRb8_FiqGPgcCGgv36cce6zvuwuPUL5_aovu5oho3jgY-4yGZEfQFSO0sZQ3M-ylYS7UB7AwKggyP5UapVTniFq-2neYQKh8e8UhYsu6NjiDcniHpZ8AvSw0wsAMDncCVD1WuGbo9T2xcHSJUPjhGGkMKpyTHvOj2KHv4r9AtOO_WM3zKmgQqHz6NlorWIumxFYQQytDkg9IG3fVEIQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
ترکیب دوتیم پاریس و آرسنال برای فیناللل
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/Futball180TV/90476" target="_blank">📅 18:14 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90475">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
❌
🇪🇺
با اعلام دبیرکل فدراسیون فوتبال، لیگ‌برتر رسما به پایان رسید و نمایندگان ایران در آسیا مطابق جدول فعلی معرفی خواهند شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/Futball180TV/90475" target="_blank">📅 17:47 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90474">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AoL2CRZ3rUshR8tz3_S7LtP2Y0-e_P3MGeqUBoKZXk49br7EsLCGEBCUOIHWsbiwUUIq1frterAXqz8IUBTeTgXh0hG69L0DZlBO6yr7uurFZthyKz2kjNLa6BBq-I0FxtwYPMbmqwtS7ympFo6Mok99D71HO7cfvEmKtv9JPeK9Le73TGXiQVhCkyOoS-qycUJm9glMXjkV3IxwUVDc07GMciMWZWPzy1Nc-kux96LgOUUcuKyrjTA32irdOlTf8i5FxBPV5_GHIpJnBEJeIvPLZBv66_BcPMQ5kplb980H4F9lUJ807VFfu1O-THIg78Cks6P04HEcJrTFhVHNrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشتک
#FreeJulian
ترند شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/Futball180TV/90474" target="_blank">📅 17:47 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90473">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a387H6Ej5MfN8wZ68wFXWoF31kDIVo-hK_C_fZeTVgXUvAH-ZSvW4ug9pqdUMKCjOCsVU4JbnxLWK88-TYaofkrYY5iIxgjQzi01DT9xdpDVYHprSZ7kxybicdx5CVQn6MWF6vjAz9iyr4JEx5oBzwvsohCoym-Y2zJL4WKd-UmPYOQui7r5mPKwAxwok5sNZ8fKizKERpJm_K2DtflqcRlFMlzkkSTWRZNUoLM3dHYmqLE0xNVuh_RvRdEq2TeHeBxjTmef1DEyBdpgtgl0eAk1_nkKwRB2zMo4VCAUYDPAkoIIdh-5KbOmLC5BZvySVrXX6kEnDuilYv9GSUAEqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
کوپه :
بارسلونا درحال مذاکره برای خرید گواردیول است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/Futball180TV/90473" target="_blank">📅 17:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90472">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46a77e89da.mp4?token=plELs9vaWvZFyadNz0IU4RyWOSON_jRk1_tLanagD5O3eav86IFieI0IimDSebKjpdHGG-YyddLXggwzE8vUDzbGWMIn1bdQHbl6cQDnKRQ6yDf8QjyKmpZ_oGVEVjgddAYHtvFBb2aFvgJG-kvo9PifhArLRWdPJp0W6QhZMatdpFfsI6cwRBslC5DDTtCOTttfrmtH86ByoT6Mn2SCwMAaaH39AWmcTUba_uv5UyB7fvSNmbtjQm-oQWH9uNo2tBryXquk4X2Pg1-luXMlOFKG2GF6cmtpVEiECzu8U5ltvAmNC3v-7inrdDjYBTWZ1xPiyXirmUXsXGxjI_KqhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46a77e89da.mp4?token=plELs9vaWvZFyadNz0IU4RyWOSON_jRk1_tLanagD5O3eav86IFieI0IimDSebKjpdHGG-YyddLXggwzE8vUDzbGWMIn1bdQHbl6cQDnKRQ6yDf8QjyKmpZ_oGVEVjgddAYHtvFBb2aFvgJG-kvo9PifhArLRWdPJp0W6QhZMatdpFfsI6cwRBslC5DDTtCOTttfrmtH86ByoT6Mn2SCwMAaaH39AWmcTUba_uv5UyB7fvSNmbtjQm-oQWH9uNo2tBryXquk4X2Pg1-luXMlOFKG2GF6cmtpVEiECzu8U5ltvAmNC3v-7inrdDjYBTWZ1xPiyXirmUXsXGxjI_KqhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای اینکه بدونید دعوای بارسلونا و اتلتیکو سر آلوارز دقیقا بخاطر چیه فقط این ویدیو رو ببینید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/Futball180TV/90472" target="_blank">📅 16:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90471">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6ScJ2Jehb0756X9uAMXJntoVfvkNKj9NUEtzQVardKxgmij2OStl-qU4-PSPWFzlVtEvW-qgLGfIMhs4P6b_tMCCElzkqA40RJF53zT6dYv6AcidLDjmz_CNun3MkxwKjeZLZsTLAiRRAOMWhuG59Ma49UsYQdZyDp-oW00gLe7b9wrEN8TbuXPd1P4z449G2HZbxOrgB-zJjQdqlJcjqfoWNxqAJ2nAzU2B7qTikkeHAjx9_f0XW060tNtI9Q52z3wjE7pASFd2XQUDdGrfEY6llaXBqcoZ6AqYvEDMPUDGbAIjXE7Er3iJIE4jyi_aDjTLzpQYSUVtAbRQbg8hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تمامی افتخارات ملی لیونل‌مسی در آرژانتین
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/Futball180TV/90471" target="_blank">📅 16:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90470">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9c775485a.mp4?token=F697EZOUg9gtZ0bGoMBZPfXCjvNSFxDpM8rtE_QzyYYq-vEQ1dTDnpEU5kBneaVwGsNWgSwyzFoWah8EvNqq9MwRQv6AM2MEEF_ASuMaOTTG2qQgUXYsbX7JX4vNBlEl35zcIh77HrkuyQWBCIiyIFcHClxs5NgoQknJL6N7RyUVVw7nUQFKvVlm7PJk7NqPZvfrQ2Vo3-KaDN9KAOVmoB4SRB6frX82XR4VsFFpPFgW_TyFdb04-eAsoDEGGtD2q59f8kVltKNKwovFsoPdG02_IsEGMd_bK3Os2RhhVzYRFDLYduFi1tYx00xsWAV7Dh2ZDdoOzePvfRpCxP0V_ISrjptM3KcgvC86-yp-EzSE5HYJng9QR_MCUOTuQAlVrXP69tRdEXcESPXwijok_Q7t9skz2DrvPljDzvqp8MGbCWYvW5cAFnn0-e7ePwbXB-MZiQCqVKeNN_kvhlPuQuvK6x9fVTIl0ebZhRZ_dhPfDCGB7ggtAbyLeVChPwH7phWcT9oYywL4tIAvrtANgBY6CfayR91auyd3W63QNxuOUvp5lv6fgw3dxV7VLWDki5BEhambtxvlCVm_kSB-gnyHvs4iAlUK03pzHtUJqJs3lC1mWrmcL3EuiN-wWuj6X546TfqJ5t2WUyh7FGJw5eb2TMWRkQvZesHV6voJ3wY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9c775485a.mp4?token=F697EZOUg9gtZ0bGoMBZPfXCjvNSFxDpM8rtE_QzyYYq-vEQ1dTDnpEU5kBneaVwGsNWgSwyzFoWah8EvNqq9MwRQv6AM2MEEF_ASuMaOTTG2qQgUXYsbX7JX4vNBlEl35zcIh77HrkuyQWBCIiyIFcHClxs5NgoQknJL6N7RyUVVw7nUQFKvVlm7PJk7NqPZvfrQ2Vo3-KaDN9KAOVmoB4SRB6frX82XR4VsFFpPFgW_TyFdb04-eAsoDEGGtD2q59f8kVltKNKwovFsoPdG02_IsEGMd_bK3Os2RhhVzYRFDLYduFi1tYx00xsWAV7Dh2ZDdoOzePvfRpCxP0V_ISrjptM3KcgvC86-yp-EzSE5HYJng9QR_MCUOTuQAlVrXP69tRdEXcESPXwijok_Q7t9skz2DrvPljDzvqp8MGbCWYvW5cAFnn0-e7ePwbXB-MZiQCqVKeNN_kvhlPuQuvK6x9fVTIl0ebZhRZ_dhPfDCGB7ggtAbyLeVChPwH7phWcT9oYywL4tIAvrtANgBY6CfayR91auyd3W63QNxuOUvp5lv6fgw3dxV7VLWDki5BEhambtxvlCVm_kSB-gnyHvs4iAlUK03pzHtUJqJs3lC1mWrmcL3EuiN-wWuj6X546TfqJ5t2WUyh7FGJw5eb2TMWRkQvZesHV6voJ3wY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
همسر پورحیدری: روز عروسی من و منصور، داریوش زندان بود، ستار برای ما خواند!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/Futball180TV/90470" target="_blank">📅 16:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90469">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09651a8d65.mp4?token=RSzJkw1K9qqcoGDrgOZEyV7ONLYbSB0EpekX2p6FcVgApBAZS93v9hAWT5nkeUvsk-n-BJYqv_K-9cf_shktidAA8P8f3MLsgiw_cQTZHfwnUTdWSUK8rigTd_9HTeA6u4uWJD6c-uyX6MNfVWqz_7UuYWMZ1mIYa37Cv5uYn7yj4Vc1TyDgGUzeXGn2qPBkf20UMUatACNNmzB1V6KNlLc-deNKOL996yYKuYKJve8mtM7P1TVQobXaE8i5elVlz2RC040ILSVP-SR1Mp9tBxS7ULvtB4xj-NCi0HpYWwMvp9VvdIis5GpKK2SQpekLa0hvvihF_mMQ9DDA1eaD4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09651a8d65.mp4?token=RSzJkw1K9qqcoGDrgOZEyV7ONLYbSB0EpekX2p6FcVgApBAZS93v9hAWT5nkeUvsk-n-BJYqv_K-9cf_shktidAA8P8f3MLsgiw_cQTZHfwnUTdWSUK8rigTd_9HTeA6u4uWJD6c-uyX6MNfVWqz_7UuYWMZ1mIYa37Cv5uYn7yj4Vc1TyDgGUzeXGn2qPBkf20UMUatACNNmzB1V6KNlLc-deNKOL996yYKuYKJve8mtM7P1TVQobXaE8i5elVlz2RC040ILSVP-SR1Mp9tBxS7ULvtB4xj-NCi0HpYWwMvp9VvdIis5GpKK2SQpekLa0hvvihF_mMQ9DDA1eaD4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
و تا ساعاتی دیگر، فینال جذاب و نفس‌گیر لیگ‌قهرمانان اروپا به میزبانی مجارستان
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/Futball180TV/90469" target="_blank">📅 15:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90468">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بهترین‌گل‌های فصل‌گذشته پریمیرلیگ انگلیس
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/Futball180TV/90468" target="_blank">📅 15:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90467">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ با اعلام‌رومانو، آرنه‌اسلوت از هدایت تیم‌فوتبال لیورپول اخراج شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/Futball180TV/90467" target="_blank">📅 14:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90466">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDGVkjS8fq9T8yMqE9X1YTC5NUNEuOE0-Vlm8vI3o6nEYqiGpVj9Bso5AHUqGKn3-Wrz6ThUObExIPJiK4u8J1Rym1LNXAnVUro-Fa2gQcp8zL4YO8yMyLLWmZQrfEdekfUkAnTteQSyYu2Yd70gy9_ISAmpuNiXp0STUYhtnrCf26nIERUDBa28r8cddnCC7GtE0QpLV0ogRx80TucDt-jM11bs-ZvHhxXqlOJaSNhEBTui1egueSRjrKdRdQs5dUMS1n4JsSiXcNoy9esprkTOP77kgNMyQqMwPVhWbTNpKqzDnzuUbw5CeVuH2f8pe_TwObp8d4ddxUjwzUyhAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ با اعلام‌رومانو، آرنه‌اسلوت از هدایت تیم‌فوتبال لیورپول اخراج شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/Futball180TV/90466" target="_blank">📅 14:47 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90465">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uyyf1Gbr80TAJ6mYjB18-AzqRNalXaYh-IYoFRMY53PjQFSi0yXcv07xlX5gVYP2QA5_6uTI5CXmDTYkkKRiGy2Lz9fDtCJ2klh0xLBNB0O0q5kEgWSyGR5U6pkWMqxJKGHNdNSG1R42lf8bleAk3Ecvxjs4kMq7iOcsqcU_oncxUOYGijS-qrbGs_PXyNOyxAxNSgszruD_VdhHvBBky8tbqnVXGxdPOsLkOJSiSixzrujo7_rJu_iQAzXryxkvF-1gAu4Xwy8sqlkxxoE9gjWW6AEHpgD7O95ORiAvV5-LSgymnR6wfsA89DSmiVOvVyZLYuH64IFQUTos-5ZsxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری
؛ با اعلام‌رومانو، آرنه‌اسلوت از هدایت تیم‌فوتبال لیورپول اخراج شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/Futball180TV/90465" target="_blank">📅 14:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90463">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H7iZPrUO8S-vEgKGmdh6PHdLfxY_IGqpWM0Yygcdh4iP0q6qsKa0bwWxACesXiwO_hza-HsUDPd0eW41wOJuIJH893RKCdmRwNDjOwrYU5g5dL4FhYDXFoUs3t80-zt6Zpp4op6xfHVrMxulDO7Gf0hDB5M9mT1aCHW859PDsVb4AS5_gbrExmx7pm70t9ntlRECXGMOXy3-mrOUqsKpHydEUBouIAyAyuy8b2sWuGKUySaJJbteuLMU2zh9aQE-NrABedmrP8-Jc1HqP9_TcYMf6apKv-cfZKuRvPNd4tjYq5lmpwPkaX4tCTazLfqICP2upfLq3YbOTBKPzC83sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ljx9bnZ5MBq1o15qtmJGj4Tmgjhv3D-kk7NMxwFj_m_IQbf8lalJLWmQHkxJRoTSmr9EM2Mkd07B69WcN0lpi88HONRIoGpqs7cf3DVBxrfLdibcv5gmirQ-JPACMJqXQcF5aNxbs99ZFCCbkloByoieDSzpJHB1SDHHku7ZNhvFRFGrWawngTUeaSDchsVAcqKL5f7NLYUcNv-jj4i_UTB8bmRxC9u2dXOJzGqznFCJdJy5C9LKB02U3ury5OO_t2wbTJnkHsW0LOuSlFh19PPPFnVS7q6bF1PcBpcC7HDlLt54wzobcQbK0TN_5md0uw3UHmHpTcOe3U0fxw_z1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
ترکیب احتمالی پاری‌سن‌ژرمن و آرسنال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/Futball180TV/90463" target="_blank">📅 14:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90462">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0ec9fa176.mp4?token=ft6WRD3TknpYo2rT14TIty1a5WtCNmRN7bBjORrE_Qw9iLU79bVCypVHjBPQ9k4-_JN5bOokvBThlyTBse_DDMaSvY3QgKBMLXFuJ822nZjhncjSU5yselBIZxOtFCBXF-yoXDZ17qrczkcguzLT7rsiNo_dQYd107dmWbDvJ5RQbTgVgXpzmZK-Q2Xe4jOU5j9TDm5HgnZCKEM-3asXw7KAW4KX_oOXWCXXGlb9TE6SiObpuPuVbk5eq2zxd-bGXYFmB1kEhfgMtYzE5NFAjAaFSHEb-D5FTwrue2Efot3pIg7vJlJLc1q-dCBUkQQP8Jq03SrYgXUu4kdt3F-GjiZ5UaEAJfWw1K5zuX32DrW2wg6Nwlr5EFROtRcEDJUzpUQWASSrW_oHZMSffRUmN0jXqXU3mdkMnmJfrfB_r6R57hxEolnYM4H2qWdSrfFCtS84-lX_-WBQCr17iZ3qhzV3RePCeo-lghN4PQKooMWJciKBnQrQJGXG0QSCbuNA4vhpR-lpyvX3awsewvNkH3e1C2X5YdVcLnRel4XmRD294uoI6bQ9YWd2opTbxx7Jc5jGJ3S11AVaUY1KVw_NuzCar3K-mRoSKQep_2_pt50NUlhe8J1DRbKkztw2OFdC6v2C7Thb7L3Tg6-jCBcMC4d_x8Xc-Vy-omhpl02IjTo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0ec9fa176.mp4?token=ft6WRD3TknpYo2rT14TIty1a5WtCNmRN7bBjORrE_Qw9iLU79bVCypVHjBPQ9k4-_JN5bOokvBThlyTBse_DDMaSvY3QgKBMLXFuJ822nZjhncjSU5yselBIZxOtFCBXF-yoXDZ17qrczkcguzLT7rsiNo_dQYd107dmWbDvJ5RQbTgVgXpzmZK-Q2Xe4jOU5j9TDm5HgnZCKEM-3asXw7KAW4KX_oOXWCXXGlb9TE6SiObpuPuVbk5eq2zxd-bGXYFmB1kEhfgMtYzE5NFAjAaFSHEb-D5FTwrue2Efot3pIg7vJlJLc1q-dCBUkQQP8Jq03SrYgXUu4kdt3F-GjiZ5UaEAJfWw1K5zuX32DrW2wg6Nwlr5EFROtRcEDJUzpUQWASSrW_oHZMSffRUmN0jXqXU3mdkMnmJfrfB_r6R57hxEolnYM4H2qWdSrfFCtS84-lX_-WBQCr17iZ3qhzV3RePCeo-lghN4PQKooMWJciKBnQrQJGXG0QSCbuNA4vhpR-lpyvX3awsewvNkH3e1C2X5YdVcLnRel4XmRD294uoI6bQ9YWd2opTbxx7Jc5jGJ3S11AVaUY1KVw_NuzCar3K-mRoSKQep_2_pt50NUlhe8J1DRbKkztw2OFdC6v2C7Thb7L3Tg6-jCBcMC4d_x8Xc-Vy-omhpl02IjTo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
به چالش كشيدن اردلان آشتيانى از حميد استيلى تا مچ پايى كه در دوران فوتبالش شكست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/Futball180TV/90462" target="_blank">📅 14:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90461">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xduqks8hYdGuONE7vanm1gB0wZCD2iJ1TVq-gTxuu0h9FNf-qCvl3T2Miu09OSFdaO4aqAmh4AAbUDaS9JGej8nMI9epHkdCT5UuHwW6XKAA-N8U2T_FGhythyrotByW3EN2tkfsDS-DmdDfbo-JXdW7WOo5dOQ5e_XWlFWZo0k0iMY5XI6v0OeAzeunCIiBjZDx95nr2JvXeUPvMwf7CprhB67FMXOBSLq14x-9ChqzRWLTBGPuTBdT2XE7cQpKf-5fZBom6G-oBEc7Ubsm4UzG93BjFYwVtFQuIUQBIbX6mm9oydRLAWNjurenhjb7hOjBHvY8ow4RfONzTQIuVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
توییت جدید باشگاه کادیز اسپانیا
😂
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/Futball180TV/90461" target="_blank">📅 14:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90460">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAPnXsdpK96idtRpuluDBkuvNoG2n94CenmhSEO4jlaCWh4AMzbe53yWkLUHLdIlnQGk8SJ30rke50M0dCQfBahefoG0vW8-TYL_oQ7In_7-UXmiZmBt2jQTvwToBbeV1zQBSVvebq5i20wCWOqyCXMzLEuuDOn_zA4CNs5I92PhGDlWEo45Dq5WpQvBhzqePkeAL4vtlE_GFa2f59NI17hROChdpVCvdHo1jk6NfgT_zZnjHme10XVrWdc6YkV4SGDhJ0KiGftAQIZ-QGCKbZUcZFfACpCouS7DGYOMtk-dkJA5QYjZKQtIIQX14Oo1FXUSfeWBfVOtoTbyhQzGPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکرد فوق‌العاده داوید رایا ستاره آرسنال در این‌فصل لیگ‌قهرمانان اروپا؛ رایا در صورت کلین‌شیت در بازی امشب، رکورددار در تاریخ اروپا خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/Futball180TV/90460" target="_blank">📅 14:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90459">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emVepJW_-MOMj9nLIMT0M4lCkhcp4YgYEdbDlbdVQrb-XinC0UZDy3-4On4nUCEDdKVilX9qDgoZnvwWACw6xX9GuFJAOQ_mBUxb0OaFSWlZcDjDyCXobWqWTTUSG0glCRoT1DMRpjdTIj9Ujb8ukRUNUkYz_dFFmygc3RiEJ0789wq-HQt0O50MmGs7CZM4A5f7P5k2di7oEj2YWr3T4oJBpGC3egAbPJpN0H2FT2-QFlj_sWg34zo1PPOw4JeD6eI9NEsZbyBw3Z4H4nZkiJRysLVRUcyXZNmQ8yJNA2ofHy8Ca3sS5hTA8RCa6FV_F1VJcjAs5EINPWyOfKaw-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🇪🇸
آخرین شایعات نقل‌وانتقالات بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/Futball180TV/90459" target="_blank">📅 13:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90458">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🔵
با حکم دادگاه تجدیدنظر، شکایت شرکت امین‌سیمای کیش از باشگاه استقلال برای دریافت غرامت ۳۸۰ میلیارد تومانی مردود و آبی‌ها تبرئه شدند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/Futball180TV/90458" target="_blank">📅 13:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90457">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
⚽️
❌
🔵
#اختصاصی_فوتبال‌180
؛ فرهاد مجیدی سرمربی سابق استقلال بدلیل موضع‌گیری در اعتراضات دی‌ماه، شرایط حضور در لیگ‌برتر و بازگشت به نیمکت تیم‌سابقش را ندارد و شایعات مطرح‌شده پیرامون حضور وی در فصل‌آینده کذب‌محض است
❌
درخصوص نیمکت‌استقلال طی روزهای آتی اخبار دقیق و کاملی ارائه خواهیم داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/Futball180TV/90457" target="_blank">📅 13:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90456">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXUJ350gLc9KtttlunSphgIKhqPM9uGz9fa3RTL2qm5prncOUfh2pfU7Wjm2WlStNq57plL3l_FNlBREXsHemA-8zl9AUalwLUKBkpFvPNfNCtEEyVXmBXnehCF8c_k8gzAA-65ZH2reKpaVV-1bCsAJ_T5fGi1DuZiPrSrMQIV9PmyvHk9uMyB75P4KvJ0KhBHYUzx8--XRx1kTWJh7yLZtH2QlQPNJu6XT4hKxi7sEPF4X7gGdzhD4rlVmP8Is52GHzNnZl7jOfRRlLG5H9L4UzAhSdwx-5G5__tirraMDhwbKGc1hJAc0J-BBTtjMNuNHBDlob7C2IMnRR61_pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|ژابی‌آلونسو سرمربی جدید چلسی خواستار جذب آردا گولر شده است هرچند رئال‌مادرید این بازیکن را غیرقابل فروش اعلام کرده مگر اینکه رقمی بسیار نجومی پرداخت شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/Futball180TV/90456" target="_blank">📅 13:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90455">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nh2tiXxgvLjPmWKYQmRCFC5oH63Lv4BQryCMl_SeG4jpP6cJuatFNn3cZd11HUXEkXPFiXnRbBNXuaNgRwa29x86Y6V8fiFoLj9rZV1R0AxenDJC9dGvFmj-pd_ZqRC_7YabKJ0AJRnBE6UM5RugfU4ZlDUNQNxpIpKhsaL_WChCN_Knhr3FpkRzk8KXhYXjV29Tg4BChyMG43q4L9hNWcZlLxrDIHs2H7s1IcDcvncYBqGtwzs4JJP4572XkDeyvv050HH5X6mHW7M9EI9Z4wkOlTYXXbaZfR7Or0FFVhCeFYcDszr44mn0BwAUE3l3AonmuwX8u2U4e_SEZ8y2xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌وانتقالات
|به گزارش منابع اسپانیا، باشگاه بارسلونا در صورت جدایی ژولزکونده به سراغ جذب کوکوریا مدافع تیم‌فوتبال چلسی خواهد رفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/Futball180TV/90455" target="_blank">📅 13:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90454">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFx28MFBJrypr0UpaxCJBjvYySjwCFxdkWG8HR5-38iob2IjbKynK1WvM70MQOww1m84sLxJJRmm8zi5ipPS8taWrzQ5W2Ykp_pSo2an9CioeyEbigKdHea3zdDIq5eTsMl-OIu_5GumlZFu_rEXjNFemjUk1qhEoaa-AMVlA5aW8zy7eKJiA04mAWitNAnLxIDouUb7UaaVvy26-kPVy2673PYJTl8G7pfKplgDSIts_bBhqEpJHDpGq3cf040nKDg_4mUxlUanMf64h9SDnxLyE8C7wBKmMBvV1sQ2PFDh3VRVBC0yfU8x5eNCrfzXGIUtUYi92w0f_DWfSfZEuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد آردا گولر و لامین‌یامال در بازی‌های‌ملی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/Futball180TV/90454" target="_blank">📅 13:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90453">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HH5LYGenwZZ32P98JdTzIp03MBr-AbIQwhMDra5Zo2aa85TjnPo9qoJhgae25ZCVhbCSzhtBNnCsHZ6rmUzWltt1fcC7ZGfAQpCM2hkmsCidzfcdvTE5UtXGeL0Rh4Tk5esORiiH3TLP2r41-AQTPP_yUh5EHliypamVSasuI-t7qXdfFW0dVPW-4aY6diWr49hpwESR4bGQVD-02Jf3-b1Fj-WJIxnD9QK7-5WZz8HjRW7TcnJm3-BasZA7UIBjF5kLmwa60TmjIxyu9XcfcvFVrj51XjUIqaoY3JAaMjzz8ybx6SKIIQkEtkF63T86eMpTh2vKG0ll0qqL7_h_tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌وانتقالات
؛ ژوزه مورینیو به سران رئال‌مادرید درخواست کرده که یک‌بازیکن بزرگ در خط دفاعی را جذب کنند. از کوناته فرانسوی تا گابریل ستاره برزیلی آرسنال، گزینه‌های اصلی هستند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/Futball180TV/90453" target="_blank">📅 12:41 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90452">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIvOHFCwFq6GjtFeQDLb9_YR0_0XVXQRlbkHvJxAvDaIs2PbOfHObgFDZ2OI8he_bWVmzs0zF2NZnuYE48_MFZTlgsoEPdESSGUfXmsTFQ3FlsX-UGGSqcYZtY-_uQFjBfRJyGHiXqolYctCrdwq3qg2GwrgpJAzCKF9fRGXdSffmJxhobJ7DlQiao2eC8Q0LrUKFwLVnbv8x4ZWqyoVzDzbTfWX1A2y445jn8eB7F941CztZ7huadKzaFqWyhGpc__fi1FHK_kAl1SB181F-sA_oJ8evL8Y2ejkuNkcCMkP0C_HbM5qfXrlsspC7SN6HHl7h_k16id371tYOE5pEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد گوردون و رشفورد در فصل‌گذشته
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/Futball180TV/90452" target="_blank">📅 12:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90451">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/90451" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
✅
🎁
کد هدیه 100 دلاری:
Sport100
🌀
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🥇
صرافی معتبر
🌐
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/Futball180TV/90451" target="_blank">📅 12:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90450">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W9BKryufdm0Qk-2EIOpmBq3pV9ntcLAVrXqIyjGsmvsvcdaiZ5Gm96JyMYDwc-PeXlQzAC_Nd24zk7vhEgdn8ERSxNgFYwjB9Ax6hylvMHkJ2TdtZty7pOsSlvwQpCWWPiXysF-1Q3a9p_AZbNS-VIVcjp4Cgs2r7zlYOtK_TTzPNnF78zp16dyuIBvJadFSb39uMgdcS5SC01XljkBWR81gVg5Cl8Bynlf7EoCsz7YjvVZDgIUpTxxrnuL5QeWY3qCU4wydONxW778JS8psmpurfd0GiorDk2yQW8WB6M-dhp1k7aGaWzuRN6iubXv83Hco2FN5UApYbJribmMFKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
فینال لیگ قهرمانان اروپا
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
⚽️
🔥
😍
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه ای، مطمئن و در کلاس جهانی پیشبینی کنید!
برای ورود به سایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/Futball180TV/90450" target="_blank">📅 12:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90449">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/584cdcb707.mp4?token=iOBy4yW-bUtoeXlmI-Bt_913Q6p5ATZij-X-0puqORXwb9Dg0FA0XjjajYHBJiiBg4UTeVGdEzzChyQkzZ8s4fIYUPupz8biJ1-M3oGHSTL7aF4_M4y1IjOfYLBQcsSrDxOnMpnlptXQKKhyDMWZogEURR3y5G4Yp6N7CuwHHcSKtvyMCkABP2eN5B1cVlSuDCpnN-VXZRc_D35B52vgDNWECiNa3r7cxdbFJD64p408TT6G43XKCxsU8YR7YwCCfPQnISwC97M_M5ZX54OguWLHN_hm6F8OQoaYpbJzQ-agmvAoXSvIFV8PK18ytVuiFkWsWh1wisO_5t5rNidrEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/584cdcb707.mp4?token=iOBy4yW-bUtoeXlmI-Bt_913Q6p5ATZij-X-0puqORXwb9Dg0FA0XjjajYHBJiiBg4UTeVGdEzzChyQkzZ8s4fIYUPupz8biJ1-M3oGHSTL7aF4_M4y1IjOfYLBQcsSrDxOnMpnlptXQKKhyDMWZogEURR3y5G4Yp6N7CuwHHcSKtvyMCkABP2eN5B1cVlSuDCpnN-VXZRc_D35B52vgDNWECiNa3r7cxdbFJD64p408TT6G43XKCxsU8YR7YwCCfPQnISwC97M_M5ZX54OguWLHN_hm6F8OQoaYpbJzQ-agmvAoXSvIFV8PK18ytVuiFkWsWh1wisO_5t5rNidrEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👀
🇪🇸
وقتی سال ۲۰۱۱ از خولیان آلوارز درباره رویاهاش پرسیدن:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/Futball180TV/90449" target="_blank">📅 12:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90448">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/628ff40327.mp4?token=p87SMkknMQ03DSWBRiBEo38360Lm0Wy6-f_dDMknQUk--dJMehwjjKCB825DAtpQtm3VPeb1PdPYGJdoEPBGPUUqvJ4wVT9qdYaM4fpyCJQzKjYrwi0N31NzxLxydjYuWkOl2L3uWASvGfItV14XELtbFTQQBduLO99m3BBKulikR0bAEAxhSY7akr4swpDc2mZgWL-nVGW8mU_AvOHGjJLL-mhzFbP5SnLakbw4NYvRGCgtxDvPMeDHkQg4valYoFnbCo9q-jdZni62tjR95iNGvfL1p7hcBDtXrLkMrNPbmZw0tFXiiWBiIuSaHzcqgpdyDSmlFDAB8SA3WDudqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/628ff40327.mp4?token=p87SMkknMQ03DSWBRiBEo38360Lm0Wy6-f_dDMknQUk--dJMehwjjKCB825DAtpQtm3VPeb1PdPYGJdoEPBGPUUqvJ4wVT9qdYaM4fpyCJQzKjYrwi0N31NzxLxydjYuWkOl2L3uWASvGfItV14XELtbFTQQBduLO99m3BBKulikR0bAEAxhSY7akr4swpDc2mZgWL-nVGW8mU_AvOHGjJLL-mhzFbP5SnLakbw4NYvRGCgtxDvPMeDHkQg4valYoFnbCo9q-jdZni62tjR95iNGvfL1p7hcBDtXrLkMrNPbmZw0tFXiiWBiIuSaHzcqgpdyDSmlFDAB8SA3WDudqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
مجسمه‌ لیونل مسی، با ارتفاع ۲۱ متر که در کلکته هند برپا شده، قرار است پایین آورده شود. این تصمیم پس از آن گرفته شد که مهندسان اعلام کردند این مجسمه در برابر وزش باد تکان می‌خورد و «به‌طور خطرناکی ناپایدار است.»
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/Futball180TV/90448" target="_blank">📅 11:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90447">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56a196e55e.mp4?token=n9lBBYWmQEkvK7JTiVMkAKnMN4sy9AYSPwy5BZj1PJPFJwU9S3gsNcbL6Ib-lr4AfaGqL0OdTnY2lI6963MGTzXZzTPiIEYOWRZYeYQlcnRl8Z5VFde7f5kCxr00fFKwjVnWrvCwYuRQGeUzxaeMfr7GpWkxZrcNdGVzf45ICKQg8-QC4Qs3LpDt_gFZo-FBjI88h2Sn2EOizpVSHvveGgOTnG-PW1UaWbrUSAAfxrRmyAlXwpQudTS9cBJCNGsSMh8KrkBsswHQsa74vpUM2t5k8OOyS6-StAJ-RDyqmZiis0TopFq9QOf8cE6uYzEDlXuPV6xhe16lV1fDdPW9Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56a196e55e.mp4?token=n9lBBYWmQEkvK7JTiVMkAKnMN4sy9AYSPwy5BZj1PJPFJwU9S3gsNcbL6Ib-lr4AfaGqL0OdTnY2lI6963MGTzXZzTPiIEYOWRZYeYQlcnRl8Z5VFde7f5kCxr00fFKwjVnWrvCwYuRQGeUzxaeMfr7GpWkxZrcNdGVzf45ICKQg8-QC4Qs3LpDt_gFZo-FBjI88h2Sn2EOizpVSHvveGgOTnG-PW1UaWbrUSAAfxrRmyAlXwpQudTS9cBJCNGsSMh8KrkBsswHQsa74vpUM2t5k8OOyS6-StAJ-RDyqmZiis0TopFq9QOf8cE6uYzEDlXuPV6xhe16lV1fDdPW9Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
👀
آخرش کی برنده میشه؟
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/Futball180TV/90447" target="_blank">📅 11:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90446">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8501f73.mp4?token=sVyCB0AgD__uQjncilmASWlrQZwQANE6um94kwffg6Z_mAAl17WavjZ_AXlAwPHTPstHdSYTGZOzQHbUF7sALt3baC9F-tH8kiAMi6ZF0URfV6u3JOr3b9ilBNGS59a0c2bpnQyOMQCJEPHG_bdVs7400pLYRKJ3QE_O5GGEHUCpqEL_OMWUVwMetpIGzzjB294cJf44KmyEBeFGV74qTsqW68WrVfoLrrzF7XO6LYgqhXREx2gpjvzhiQJ-Imc8WOrVEwB3cQdjpqcVqx7MmWP4FPjSIE0AdR-3m-ssAxtFAubWsbp0uHDC9-3H-dmnKYhhIbKsBHavbd3OJD0jxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8501f73.mp4?token=sVyCB0AgD__uQjncilmASWlrQZwQANE6um94kwffg6Z_mAAl17WavjZ_AXlAwPHTPstHdSYTGZOzQHbUF7sALt3baC9F-tH8kiAMi6ZF0URfV6u3JOr3b9ilBNGS59a0c2bpnQyOMQCJEPHG_bdVs7400pLYRKJ3QE_O5GGEHUCpqEL_OMWUVwMetpIGzzjB294cJf44KmyEBeFGV74qTsqW68WrVfoLrrzF7XO6LYgqhXREx2gpjvzhiQJ-Imc8WOrVEwB3cQdjpqcVqx7MmWP4FPjSIE0AdR-3m-ssAxtFAubWsbp0uHDC9-3H-dmnKYhhIbKsBHavbd3OJD0jxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇳🇿
مدافع نیوزلند رقیب ایران، در ۴۸ ساعت ۱.۵ میلیون فالوور گرفت!
یک اینفلوئنسر آرژانتینی پس از بررسی تمام تیم‌های جام جهانی ۲۰۲۶، "تیم پِین" مدافع نیوزیلند را بعنوان کم فالوورترین بازیکن جام معرفی کرد. اما حالا پس از چند روز، تعداد فالوورها این بازیکن نیوزیلندی از  ۴ هزار به ۱.۵ میلیون نفر رسیده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/Futball180TV/90446" target="_blank">📅 11:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90445">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIMpUXtkhC3uz5YvsFuZVvuxdSHS2ERnrFLaUdOmO_jUTFnrcnjhBS6OZNdyAa_WPAZeyvBjYYfPkbZLRNTB6CRYgUZf4rZUbMTN1pVJ2RgBxw1kg7cHcCn-BzsMswtMg885gCEtNKXlQTPzZ8vuuh7GEVZtGB7DT0XuLsg8KQQWm7v76JivRvHn4tA0IT47UZqGOwPF9m-YwSrONB9l9WvzoUKf_pYsZIAHuoI4I4hIYAmajEibkbgEIpY-oQNqaBFW41A5zLiIuC5-7eXobCgelYsIoaEY8OkafIeXSOpDOmlVN2DER70Jx77I4CfhhV46AJ42Rb75NKEDJNIwFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
کونده با پلی‌استیشن‌وان در اردوی تیم‌ملی فرانسه!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/Futball180TV/90445" target="_blank">📅 11:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90444">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
⭕️
کنکور سراسری ۱۴۰۵ در روزهای ۲۹ و ۳۰ مرداد برگزار خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/Futball180TV/90444" target="_blank">📅 11:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90443">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPQ1ulunq108Zum4ktxhU8OFYdZPdIuLx-FoLpqBnaVJOKtK__myxXaxXpbGN5mFmN2TpIxc9cEzuoZFjFsxQbHkc_zPeM39WHs1LJBSnlJcU3-J6socU1ctHwF5LlzbQmkk6vLvF6ejK-LsCEeKatld-RSjpMylI2z-fqEUkWgqQFDXdCV0ruZvOLlyqN6Zu1YvSJttq8rEP4lkNYTKpFjTuG9B8J4_Ot66_Z12jnvssFHR_6pOrwiWQh_tHGID1LP_vI7KW3FKJ0nvpNIklESgpuWjlRv3EjNrYdJMNHzmCjT15ZiOwg8gx3pcz91EGMYEkXfADZwR_NAcYJ_8kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🏆
باشگاه‌های
قهرمان UCL بدون شکست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/Futball180TV/90443" target="_blank">📅 10:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90442">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4bcf8f7c1.mp4?token=R6LqmYslyu74hWZgFhsrgrsxsWux0_cs7Auv6M2WqYPoGLOPKhY1_ru-RjAMDweNsvyGEtuGo1udgolX_v1E7MYv99IQ_G6sKoQLJLK_YD3M0mYmeU9CPd_VEqwWC_fXj6HQR-_6pCJ4wCfBva5k5OkaK7QH7ngNVGA2YSLkftt5lXjE_vX9vmwMqSJW6Cs8iYwa6cqU48QcqHSBhDUDFN11-MoCUX4y_o70vZ_6mTIZLn-McV2enxr3_Vcl_N2TRd80Krx5II6qIn4t8wTil7LmZNcXPQ7tBQWAEexgmOWeZBDKeGQvj45m-pB_GeU0kuXGN986YD_V3_6kQ1NvDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4bcf8f7c1.mp4?token=R6LqmYslyu74hWZgFhsrgrsxsWux0_cs7Auv6M2WqYPoGLOPKhY1_ru-RjAMDweNsvyGEtuGo1udgolX_v1E7MYv99IQ_G6sKoQLJLK_YD3M0mYmeU9CPd_VEqwWC_fXj6HQR-_6pCJ4wCfBva5k5OkaK7QH7ngNVGA2YSLkftt5lXjE_vX9vmwMqSJW6Cs8iYwa6cqU48QcqHSBhDUDFN11-MoCUX4y_o70vZ_6mTIZLn-McV2enxr3_Vcl_N2TRd80Krx5II6qIn4t8wTil7LmZNcXPQ7tBQWAEexgmOWeZBDKeGQvj45m-pB_GeU0kuXGN986YD_V3_6kQ1NvDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇷
اردلان‌آشتیانی کارشناس فوتبال: سن و سال تيم ملى خيلى بالاست و ريكاورى سخته
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/Futball180TV/90442" target="_blank">📅 10:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90441">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLrqzCZABlAsEgHurk38trN8c36IyOTxpDAYbcr8VsShFTg-jT_FY9BN-Mmec0dtRcqX3roS7O24GolesTd1vMMD556UK35o12SUqLmj_qxTOtDwwyCw_xma72sNud53XKp3dOtFebSzF-ObrmZLr9iPwmM5eTiAWIzTMzNkaJZtdRfyVxTKARfWzJ7A0s8AWSBNTxyAZN7YQjMXZ1WXRtQhwPCCZrGeL4_mneYA6JraVrDP1Zi1oQmUyEpkRKW4K7KFDIudkiFjxmfY1_m-wTRf8en6KshLFNq2aPVTgPfxm5VHs2D5miJHFi7u4msVmK_S42aMFKYDG2cTklxegQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
پرافتخارترین سرمربیان تاریخ لیگ‌قهرمانان
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/Futball180TV/90441" target="_blank">📅 10:07 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90440">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b6df1df4a.mp4?token=J1-UKJVVMwsWUuw7wPWhv4vs1m9GfJZpJUjrB3Fvfpf_VKXPt8FrKGfEX39KHwluOYpORYAGdaVed02UAa_0CY16fV_IvjU3ealjNJMhqU7DuSsV9uzsaw_U584PoUgqIIADikSiU73s5UxjTbbMFTkUaTYL-zPrYd3DRKezqEDv3IJ-uxlXGcpqCS3JyhhBl7DLSkI3iKRTPScNFpKsZh4UZ6VVIF3-LBePFC-hVoeFsN9HB8ybBKPW6t0_NIzzwZ6wEudFWqBzR28OJo68pjiJp9vgzRYf4EInrB-EYbIkrKdNSX3_MS5awTHGF_FA3oIuZXMP7WOotZGWGHN7nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b6df1df4a.mp4?token=J1-UKJVVMwsWUuw7wPWhv4vs1m9GfJZpJUjrB3Fvfpf_VKXPt8FrKGfEX39KHwluOYpORYAGdaVed02UAa_0CY16fV_IvjU3ealjNJMhqU7DuSsV9uzsaw_U584PoUgqIIADikSiU73s5UxjTbbMFTkUaTYL-zPrYd3DRKezqEDv3IJ-uxlXGcpqCS3JyhhBl7DLSkI3iKRTPScNFpKsZh4UZ6VVIF3-LBePFC-hVoeFsN9HB8ybBKPW6t0_NIzzwZ6wEudFWqBzR28OJo68pjiJp9vgzRYf4EInrB-EYbIkrKdNSX3_MS5awTHGF_FA3oIuZXMP7WOotZGWGHN7nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
تمرینات فوق‌تاکتیکی آرسنال برای فینال امشب:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/Futball180TV/90440" target="_blank">📅 09:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90439">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwcip0_qm6shz58rRCa4I0da6_bTWBn7Odn4BNZBClf5GD864GuJXjw6WfQeiC9QzrPK4QaxqWkflvHcMorLyKqEM5D9ZHWX-t69XcEo0PdYdcy4ONn2u0KIwT4a4emb7Ohz9Ax4HLzSb_VLnB3N3ivR2lgiqRBfvmS1dHBQLmHcNPEbCIMsqWqKuevu6n2w4MpsS8wMd_oaMtmpDsKCrhxHsplZNyT8xqZ4PcRQhREqEgM_uU3rLllpWVKficnadn4i1BlfN32u0nPn1stXThdMx8ADo1BEGSrVaKv6tbVoTSq0U3bcTULcffsmDEa-zrJysJw1s5AK0onnUIxrAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه آمار یامال و دمبله در فصل‌گذشته
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/Futball180TV/90439" target="_blank">📅 09:20 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90438">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bduePfqYt1PTJJCxn9wVaAsp2gKgKuDvlE1uqKFJz_Zky4CTyQsVetKVlU-OInMPGBzl617uRIrJO5QLIZIsLdwAUBGSi30px7BbXf-_mbnA7a9pzBwXHc-p2mCsccRf-pDK0VJPv1kL5Xomo2_gqL5OSA_Rqk4qfB1o9gGtN8YNG1JhvMxi6PHQtsWXMpMll_i1k8nW-Zb6OF2AJJ1yCG6IJik2Za2iamjRqRLDCgvIHdgq-7NY227keejqJq7pm3Pe5XyhaG203wnkQ7DyuY0A4rMe3d51bVqlQd8wNGRmbPipLFkfrV3Zj0MgLt_Y2umIuNT2nldpzwMSIF6TDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
آمار تقابل‌های دوران مربیگری فلیک‌و مورینیو
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90438" target="_blank">📅 08:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90437">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oIQkGOQ5s5t83WMaFuyYbuUBKTxo-DvJryzzr2hm9l2mx4YKHXZtU4KQ5ZHLOfS5wlL_wh_D5q6oeb9E4JkDRkBxEbGeDSMNvQwB6TdVGqKJT5KlSygkpAKAMjsHNw2Jfp_uLdlkECKTmkykh5xIELoHn-mKFhuLv5Ud_5ub3aO4YqKIebo8seb9On0GeCHjl048YRtvMyIZ2ajUPhygmKJFPUYaMHTjxgWrp_d1PfmMnAIzo_rwvup8Qk6jJ8x9MdGtljlVa3RHpt8Pd-bBMYdYwxyeqlcWUJuuU6Z9H5jrS4MKdShzCGCzoTZuXZJCNk_1mnOOiBfwSQH5N-JPKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار و عملکرد رافینیا در دوران فوتبالش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90437" target="_blank">📅 08:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90436">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">⭕️
تا حالا بدون واریزی روی فوتبال ها شرط بستی؟!
🎉
500 هزارتومن بونوس رایگان فقط با ثبت نام بدون هیچگونه واریزی!
😮
تنها سایتی که با عضویت بدون  واریز 500,000 تومان شارژ بی قیدو شرط میده #وینرو هست
💰
👑
#معتبرترین سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90436" target="_blank">📅 00:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90435">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_iSDQaNz0h0DAqU4Tj_rtxMcrOZMXmzL_0Wsz2_CGhF0pkkdctQEeBIGAKykVprcLvWXZHlO6bRoWFnVu3yq0X-YX557n8BUz_XWuQXdOmC7SCjYZCYlsbQr5MKANMLc-isNVTcAKFi2PD1XrkZdgsHLhn-nILje3uZHKuYa8Jbk7kkubVxcmhUQrBYnOqfy2hsd1MjbY7dQuf3aYbNPIUBDeJAxgG_WI590OV3EVDOS7MDAn0dC3yKiYuWdz-SP70dFAyhVgwxKSORJ5gpb_Ik-MmmSqYVzywHoCFkdvUGdSzRwNI-KCcSrZdUTmA8NaDJHDK-V0guyczCUiXUcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تا حالا بدون واریزی روی فوتبال ها شرط بستی؟!
🎉
500 هزارتومن بونوس رایگان فقط با ثبت نام بدون هیچگونه واریزی!
😮
تنها سایتی که با عضویت بدو
ن
واریز
500,000 تومان شارژ
بی قیدو شرط
میده
#وینرو
هست
💰
👑
#معتبرترین
سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال اخبار و هدایا
a8
🎁
📱
@winro_io</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90435" target="_blank">📅 00:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90434">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1XfUZvCrZPqQ8yNLb7O8x5k-F_LsUVe4zL49omSNTmW7Bz9noJdf4aNK0-xdRgfRki2CMDvozRNSSuOfFnAQAV6NSJHu_SPOECceem9giJmighsmGFr2KIp7jxgO4Mwmw3eohl_-SLI2wNX98DByW8B_tfL_sE6QytYcDPTBPDHgbDkoE-zN4jZkebyiwJf2GD7An1nrYfyGIYrPugGiOiWOyvuIO4GsvuZkFJDBs0d9PysDPQfNilUbYOE08aABzMADqkOC-VPkm41pI3ebPPyM63SBK3V47zTr50vwQDx_dsf94BdNrv1ZTq9CCWNckaWAqfEZl5BdKzDHrI7Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساپینتو با پافوس قبرس قهرمان جام حذفی شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90434" target="_blank">📅 00:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90433">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">مجوز حرفه ای سپاهان صادر شد و فردا اعلام میشود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90433" target="_blank">📅 23:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90432">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ui9DYul5YDmCDAJwx-zGEInJM6hNo6B299WWvtHhFaOOACAcXsr4IRuK7wf9jLORMzkB-HOJhNlkY8sqNh-ImyMYfb0ckds0sRyuDxTOcTWKggHKO66OMQ5QKtUhb6m8rM-s3EYVMWg8wj3_Pnq5oYuQIxl_lPr0zoisMP18_xJYwZLYok-nPb_3pNlYY37MPKLpmmcRmVUimWFeqJ-zuRSmaLVjk3vb8yHgfpSIqbk4PMNOSGOCdLLVG3EKNrwwLmx28GqA6BiCKywpqmvmPVMt6WrGg7_FGW-qYuirA4wSaTQCUOE-3huikA8Bl7yJpZt_DQljmmrggvZqXg2TrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوری و رسمی
گوردون با قرادادی تا سال ۲۰۳۱ به بارسلونا پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/90432" target="_blank">📅 22:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90431">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEwBZR6Rkrn1zZkbvSn3QQfKDv4AHzxR7fyF2KZ2-7zyqwmmZogsPk7s6ZrDkgoteQFy1XKT1g0JIGlDUlmzbhoKjgAa8CEpOVciEXKpmh5CWBlSAjZ2kMA5SQ9ciGF_K27jX-70cMuJUb9eXIUM-39f-n59wzej-U36zFIqKjry8-7fD05Lcr0tslt3aasXyHnAucjtbnK0qaWfiUJcCgPhQANxVttQI0ag_7HCxL73qIEkKBTkygoQwKMAGJXFidGR6TdxAMhSSiaJdgxX9ofTGb4RNRjO251us7y4Dfv_LdpFZMX0yFCNAyhdvyyAwl8vIyapPWL3vYc1tb2yqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست دورتمند
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/90431" target="_blank">📅 22:44 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90430">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEe5xvjXCZd20sMO4H87Cf73EYY0n1MYRuHMAkpqZZ9hILRIBFdqot03dqScC540Fy2xkJNwrTi2KCOqn79H805TsdT6oASsrhS2j8o0wcqjp_Y3UwMM8Rm2uW8RHi04oQ0bC5TxVszIFJsHb8pIADQS_HKNXmkYtFyhUexvj0_USnusErjd-cJTu0LUW5DIRd_HFr4nQ5RXsirryh1wMYhRB7qllH1nXQaqSXeEP6XnBaJ63nZIsP4sRXMfrjtPvUW9xaFsPpUnjdr4iyWCDuvwobNZ-SwPt5GIyWtOwPwVIEC3Rn7juOuBFMSPStbblgWD2PEsLn8SV8c1LfDdaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اتلتیکو مادرید بیانیه ای طولانی را برای روزنامه های اسپانیایی ارسال کرد:
خلاصه این بیانیه این است که اتلتیکو مادرید به دلیل نحوه رسیدگی به پرونده جولیان آلوارز از بارسلونا بسیار عصبانی است و معتقد است که بارسلونا به جای مذاکره رسمی با باشگاه، از رسانه ها، افشاگری ها و فشار از طریق خبرنگاران و عوامل استفاده کرده است. اتلتیکو تأیید می کند که این بازیکن برای فروش نیست مگر اینکه بند آزادسازی کامل را بپردازد: 500 میلیون یورو نقد، و او تا سال 2030 قرارداد دارد و بخشی از برنامه های تیم در فصل آینده خواهد بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/90430" target="_blank">📅 22:17 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90429">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🎙
لوئیس انریکه:
به آرتتا می‌گویم تو هنوز جوانی، پس بذار این پیرمرد دوباره قهرمان سی‌ال بشه، چون آینده بزرگی در پیش روی توست
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/90429" target="_blank">📅 21:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90428">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aso7L8-750N3LXhQxaZC8YjP6ZK5n8xNKYSH_tBIxSd3YpjpLglX7DR3y4KkaWqwMGSTTuuERk0IiXKW1Y4Z_WYgLESgiBYHOjymj9MnW2o1z4blRF3eblDbfpoCGcwBakrmYTGOeTFX0qEG2HQebxjRqwv94IO7fsyp0Oo3SzWt__anNVSeARw3usToG4aAY841xKNiiAtmi77OHig9b0uS2SU5KiUIu3G5MpKCf742dYLt-9-TcRHl0J2GCGdW7vgTwNmsSLfPfaVidSg3NKZZ-4J9heOFRo8KITHtwLY6lz1pDBoWSzHBGLtwz2rqYEkXzxATBc_Tsx2BObeaxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پاری سن ژرمن
🇫🇷
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
🏆
فینال لیگ قهرمانان اروپا‌
🇪🇺
⏰
شنبه ساعت ۱۹:۳۰
🏟
ورزشگاه پوشکاش آرنا، بوداپست
🎲
با بیش از ۶۵۰ نوع آپشن پیش‌بینی
⚡️
با بالاترین ضرایب پیش‌بینی و بیمه صد درصدی
💯
📊
نگاهی به آمار دو تیم:
✅
پاری سن ژرمن در ۹ بازی اخیر خود در لیگ قهرمانان شکست نخورده است.
✅
آرسنال در ۱۴ بازی اخیر خود در لیگ قهرمانان شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر پاری سن ژرمن در لیگ قهرمانان ۲.۹ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر آرسنال در لیگ قهرمانان ۲.۴ گل در هر بازی بوده است.
🧠
وقتی بازی با فکر انجام شود، باختی وجود ندارد.
⏩
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/CH100
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/90428" target="_blank">📅 21:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90427">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d5ed95013.mp4?token=pH9ctp3BdUbFX2ySRRB8Wyk8E3fg96JetkelKsKBJ2aaigdkt5DIPmkepRNEbDe0g-XxSCdYwypaVbwnkkAQ-N9aCBQyy0BnHb0Y_wneE0C2XG4xvmGaUU0SSy57PfloRZf9q7L1UX8yMsbsL40h95catMclRncBC66l8s62VeJCtHJYtTWCEA9VfHNngPaSH84Z1iT7pcEcWg1Dr5jmCzEgNuzPfqkqr0V9I93pA5EDR8iv-jQMuxBFnO5RsbRRrB-kofiQqSVZCkG2idOc2JymuP2Hzng6T5Pa5C920V_WHHgefRBvmmoX-58ZoG5BhrlJdLOA9OGCGvxNkd_XVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d5ed95013.mp4?token=pH9ctp3BdUbFX2ySRRB8Wyk8E3fg96JetkelKsKBJ2aaigdkt5DIPmkepRNEbDe0g-XxSCdYwypaVbwnkkAQ-N9aCBQyy0BnHb0Y_wneE0C2XG4xvmGaUU0SSy57PfloRZf9q7L1UX8yMsbsL40h95catMclRncBC66l8s62VeJCtHJYtTWCEA9VfHNngPaSH84Z1iT7pcEcWg1Dr5jmCzEgNuzPfqkqr0V9I93pA5EDR8iv-jQMuxBFnO5RsbRRrB-kofiQqSVZCkG2idOc2JymuP2Hzng6T5Pa5C920V_WHHgefRBvmmoX-58ZoG5BhrlJdLOA9OGCGvxNkd_XVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ویدیو جدید اتلتیکومادرید علیه بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/90427" target="_blank">📅 21:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90426">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQvzEwauNSiaPnQ3or3VvB1AU8o1te4xRB6y3WDTwPJmhwSIyXVbG3ZQq2T-a0Y9i37PmdO3UzduV4qr0rR6DwxJqkxJQWPPXlAlFRVeOu6YLPGPyRMoyYzJL8JdLdhm_cqu3MJDQ1J12-7UXbGjUG0JzQOnmy0Q8cX_g2qCHUQfXDyz39atmQbxokY1F51RYyeJ8PtzxZ-mzQlW9kpY_gCdW0OhvmXiVhLhxxN-juY1KBsrp5eJiMhjjLsqBRAibgSWGuf9XCct07-mGLgxO2ZU4UXrnElBfvLqN4tku5jRs92p1K9Pxb3e-D8rzt0dkOxCbN3V4uePbFnGVeRsEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانه جدید اتلتیکو:  برای این پیشنهاد مشکلی داشتیم، چون متوجه شدیم بلیت های کنسرت فردا تمام شده. پس پیشنهاد جدیدمان را با ۶ بلیت برای کنسرت یکشنبه بهبود بخشیدیم
😐
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90426" target="_blank">📅 21:27 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90425">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">تیم ملی ایران موفق شد در یک بازی دوستان ۳_۱ گامبیا رو شکست بده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/90425" target="_blank">📅 20:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90424">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34e3caa05f.mp4?token=Fm07G3BlfpF-vCSxwtrcJ3GFQ8IKGnPLykn-fGjCckaGghtwtCBvNlxUGKptWDjJdwcO4NELECzwpmRaiTrAIH83s15rFIglbxdVXOeZd9y2RwTFyiL1dcvGD4BVJN7E0JFOfWm78oWGv0mCyJnYBKxJm_YkrqSvDv9Hd1hcAts8zGV5buqARILtFK8FUyxi7480jRVv8rHpPvYTML_PQrG953qLJqA9n020B5U-Pce7DgktLui4mGm4JEnLa18X4k7Tel6EalVacSRuk1wfV8G_J1TGRg-cWf2FC2n1V1y3Q0g3JUOQbzB0AgXQufo_iZgOrmu476VTL81kWmQHyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34e3caa05f.mp4?token=Fm07G3BlfpF-vCSxwtrcJ3GFQ8IKGnPLykn-fGjCckaGghtwtCBvNlxUGKptWDjJdwcO4NELECzwpmRaiTrAIH83s15rFIglbxdVXOeZd9y2RwTFyiL1dcvGD4BVJN7E0JFOfWm78oWGv0mCyJnYBKxJm_YkrqSvDv9Hd1hcAts8zGV5buqARILtFK8FUyxi7480jRVv8rHpPvYTML_PQrG953qLJqA9n020B5U-Pce7DgktLui4mGm4JEnLa18X4k7Tel6EalVacSRuk1wfV8G_J1TGRg-cWf2FC2n1V1y3Q0g3JUOQbzB0AgXQufo_iZgOrmu476VTL81kWmQHyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل سوم ایران به گامبیا توسط طارمی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/90424" target="_blank">📅 20:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90423">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1fd30abfa.mp4?token=bVpZT36cezftsz9UkR0fJl8zNX3wevuy349wyNKogcRQj33dI_cOwdm1xW-6_8bCpAWAUKdKajI19RXcwkNNyfeb-GLs8Muxcdrf16o_qXONPRtk5iTw191YWPghvBwsgxOA63ep6jD6zAzxwdG6Lj5Y0kH7dswf6Ppn-c0uYUOapVCfEt1Sd9334Je8hkyxuE6T4PMXX-28lyEPuOP0TbHR43ZgAZtkD-2m18GHnoVw6ZfVUrXVT9RzlFVKgx7bM-v9CxuwietHUwotPBvWYh8ZpZOGgPtOwACLxgQEJXc0s2zljjgUNoULMiVVrDEra9gqZeWPX5v8fD1znzlA1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1fd30abfa.mp4?token=bVpZT36cezftsz9UkR0fJl8zNX3wevuy349wyNKogcRQj33dI_cOwdm1xW-6_8bCpAWAUKdKajI19RXcwkNNyfeb-GLs8Muxcdrf16o_qXONPRtk5iTw191YWPghvBwsgxOA63ep6jD6zAzxwdG6Lj5Y0kH7dswf6Ppn-c0uYUOapVCfEt1Sd9334Je8hkyxuE6T4PMXX-28lyEPuOP0TbHR43ZgAZtkD-2m18GHnoVw6ZfVUrXVT9RzlFVKgx7bM-v9CxuwietHUwotPBvWYh8ZpZOGgPtOwACLxgQEJXc0s2zljjgUNoULMiVVrDEra9gqZeWPX5v8fD1znzlA1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم ایران توسط رامین رضاییان در دقیقه 59
ایران 2 - گامبیا 1
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/90423" target="_blank">📅 20:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90422">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7455525379.mp4?token=Fyu65I1pf6OGaKkj_AbKHPUYjocuj1JoYbhQJ52ciBHT_gaBkQrjX4dkLv8JsSVF2HkfTu9EjAlGujz2Y_jivXuB78YJ2CkbL2LtAb7H_GMW_ORE9AZxzWApR_i3CTNJWCsupaT5-kXmE60GimL2b0vLFmFMFADGmqm9N_jiDTWifBTwj2Nhs7kCMH7DfP_IJbzlX1t9LZM260NS0TDo6WsAPtZrg5tG5O3OdGljm3NIJ5fS9CknHC5276Xj71MO8maYoslBFPPp01FaRsHy4pjX3HrmwhT4rZmvjk5K-lysEbNkbVsmbyhs6GC_g5FSjWcODqwqZadnRNmcmcmTfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7455525379.mp4?token=Fyu65I1pf6OGaKkj_AbKHPUYjocuj1JoYbhQJ52ciBHT_gaBkQrjX4dkLv8JsSVF2HkfTu9EjAlGujz2Y_jivXuB78YJ2CkbL2LtAb7H_GMW_ORE9AZxzWApR_i3CTNJWCsupaT5-kXmE60GimL2b0vLFmFMFADGmqm9N_jiDTWifBTwj2Nhs7kCMH7DfP_IJbzlX1t9LZM260NS0TDo6WsAPtZrg5tG5O3OdGljm3NIJ5fS9CknHC5276Xj71MO8maYoslBFPPp01FaRsHy4pjX3HrmwhT4rZmvjk5K-lysEbNkbVsmbyhs6GC_g5FSjWcODqwqZadnRNmcmcmTfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول ایران توسط آریا یوسفی در دقیقه 47
ایران 1 - گامبیا 1
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/90422" target="_blank">📅 20:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90421">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ روزنامه آبولا پرتغال مدعی شد که مذاکرات بارسلونا با برناردو سیلوا در مسیر بسیار خوبی قرار دارد و احتمالا بزودی منجر به عقد قراردادی دوساله خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/90421" target="_blank">📅 19:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90420">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7061278c4.mp4?token=VRkD72lR8y6-j2AhAW-94y5rKGk8_nKrhCFUBzkA3yBNm43AQXzWKDuUnZ3KKz7lc3M9uSVF-ZLH69Hv6KrjdWH6piMm8-wgDdpXJl1ryT0CbZ8wAjbLdnm8RvU7w0UagN4hi7ZougZxh7AugqrUYajTEHjwpsVg8aJ3mXT3_3I2xRPvmIwUgbWIkFzfmm3I0x5J5C1UkjVlcnl0hJVnFXcIlUrFUzdmBhisG1VhvL-UcI1018BCKdLxSul0Tr-n4tCgBvu8hfyvNYXOtajSDpr5liv557zu3-Aef8Evx348Gwrm2G4CqnD1mOXve89dZgewOLrs0gVwZaVP8OSbBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7061278c4.mp4?token=VRkD72lR8y6-j2AhAW-94y5rKGk8_nKrhCFUBzkA3yBNm43AQXzWKDuUnZ3KKz7lc3M9uSVF-ZLH69Hv6KrjdWH6piMm8-wgDdpXJl1ryT0CbZ8wAjbLdnm8RvU7w0UagN4hi7ZougZxh7AugqrUYajTEHjwpsVg8aJ3mXT3_3I2xRPvmIwUgbWIkFzfmm3I0x5J5C1UkjVlcnl0hJVnFXcIlUrFUzdmBhisG1VhvL-UcI1018BCKdLxSul0Tr-n4tCgBvu8hfyvNYXOtajSDpr5liv557zu3-Aef8Evx348Gwrm2G4CqnD1mOXve89dZgewOLrs0gVwZaVP8OSbBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌اول تیم‌ فلک‌زده گامبیا به تیم فلک‌زده تر قلعه‌نویی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/90420" target="_blank">📅 19:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90419">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syuBwYh3tA0twPsiVkLMwpA-icCCoXta_Qr79jDUVVevEgVZZgO_kemeDjyPITAXtatQCejyBJq4uPiW1lkgu0bbrGkHMpd8GEfX9yx2fuIuIqKzimd0C_H-qXo8aKRZbnAj9LzSO98Fha3iAzscVAoMC8_5sJBV9xAu5ViiMuU_fDKaVPU1XotMroCAZWecWJ3ZqSVyuw-B2BToogSj5Z7iwCEk4Wfcv3PYTZThFaYc6ohkHG_zPRIZm_qMF1OTgtAikMyOCEGUvTmVJd0NcDPu0IqbbB9pU0d-f8S4uDO83AwSkYF0w7iNWgZ37atBdKy2MPSlkSoIvi9U2ilL7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانه جدید اتلتیکو:
برای این پیشنهاد مشکلی داشتیم، چون متوجه شدیم بلیت های کنسرت فردا تمام شده. پس پیشنهاد جدیدمان را با ۶ بلیت برای کنسرت یکشنبه بهبود بخشیدیم
😐
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/90419" target="_blank">📅 19:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90418">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">⭕️
رایگان بدون واریز شرط های فوتبالی ببند از همون اول موجودی 500 هزارتومانه
❌
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی 24 ساعته
🌐
Winro.io…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90418" target="_blank">📅 19:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90417">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMpjeTGDkoMZasxy3HEwPj1k-ivfgUteihm-BlT66cKz_8CgtZC12AkIwnUj4FGEusa1x6JaML3x-8YY9lQmivO9xdYqwr8ehphXpxbcRcsLRD_eDCx95f9dbAW6XhzjSWzojri_JXefu6Bf2xuyVM3yezew7JzYCJzL0YzSt6BtclKaYjCiUfPCgn1qeCn4Hx4Di5LiKJPH83sw63uo4STTnmOdGPvqyFYbUaPn0HYjU035wnbwT3eOX4RaEedCzs9XacZljGjhCGeFohFb8lcwdn2GrH5ET5gboyRU_8_tjqPFMAJFClS6FirW68G24z5gwEtS1hOGMSUinrxl4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رایگان بدون واریز شرط های فوتبالی ببند از همون اول موجودی 500 هزارتومانه
❌
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g8
📱
@winro_io</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90417" target="_blank">📅 19:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90416">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohN-kdVMWu9PBA54muvvJtAuplr8FVo9vO6c0IbZ5MeooW8ESy05r6Qah1tyJ_vsokfm4CchqYuElWy7lSlWLI-HWgMIO6x8DPGC40lUcvVEBBOYiZz65lntZA1vhpaOApGFqiYIAx-tIcQ9VeaSNznCj3V89qAr7mjNCmpn_pI43nYrNzxRKszaHUWy9keaSyxRT_NmRSlUEl1Xfl8gPA0uFMSyT1z4nL_bc3nC6VZA0qxfV2Xj2sQGrr5bFp7HpU4N_baoA1OgPAH01FQGSv99J0uNBFFBk6vgXxpv3zaPaiZ1wOkuH18nW4Wz7GMjOE7SmgPck71dJ8zy_yBmGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‼️
حساب‌رسمی اتلتیکومادرید دست‌بردار بارسا نیست
😂
😂
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90416" target="_blank">📅 19:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90415">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYVLbPaIcBmDLZ3OD0X5esE2p0AhnzLxkcnbCsgzOyoQCwTuW5d4kXuWS3Kr40nmVNRKCV68tyP4okTgBgpHSPzpqBQyP9dKbF_hp-ReetTQmupfqDFl54bms4cN7IO1kFu8E3buwTf7udeYUFWGN7gVGeZ5ysnxrntoIx49O1wJL2u3Qtcqk3pplpEvhX71Xqwf3sXiokeNqX3X_K7ZOWf3R38zYrI_LUbQNpuvs5TLNQOJT-t8KEYE6jsabR-YzOWwu1zK7ezMeUTNBLeAFeCROfTbhFN5lihB9ztzAg-sSTr4JkI8B1DuDQMRkhQettJFO2dyyBdKd_MUfJ12Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باشگاه اتلتیکو دقایقی دیگر راجب آلوارز بیانه ای صادر میکند!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90415" target="_blank">📅 19:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90414">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMW_UEF29WSHLQ7AHmHa8Ew5COPltdvR-UgFra93Ux_1M3gU9Hxi22A7JVEzKnnIiDIZtp-Cquv-yfwVnoG5CGZCEQevwEcjLVVKMGkHFkrOxuxEQLqx_5w0rKlXw7onP0EtT7e_rztyi287XG_1CNZiOr-ROwMVc-3ajrO5xPfjhjJAeaEN10JXWE8zSUvnmveXCPjLOEzXNAmHpVnez-kdDdaPVP6SZw9-9HaMQgNL44bOUiYcdOO8X8v4Sgp3bQL6EIGknd8fSgsl-F3GlJdvE1VIcDTnqHx7v4D_Jwry0X9_J-avkAJnI3axpfCEke1Lu7lHdzw-bvAsei4q4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باشگاه اتلتیکو دقایقی دیگر راجب آلوارز بیانه ای صادر میکند!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90414" target="_blank">📅 19:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90413">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🇺🇸
⭕️
⭕️
دونالد ترامپ اعلام کرد که محاصره دریایی ایران از این لحظه به پایان می‌رسد. همچنین اعلام کرد که تا ساعاتی دیگر تصمیم نهایی درباره ایران اتخاذ خواهد شد. به گفته رئیس جمهور ترامپ، مواد هسته‌ای ایران بزودی از مکان مورد نظر خارج یا نابود خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/90413" target="_blank">📅 18:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90412">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ایجنت الهیار صیادمنش اعلام کرده در صورت تصمیم این بازیکن مبنی بر بازگشت به لیگ ایران، اولویت او بازی برای باشگاه استقلال خواهد بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/90412" target="_blank">📅 17:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90411">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RG5IE-KouwOwxQ2tYaWl6ALFkvecBUVnIkTXN4d0spt7tGtPT-kY3dMAAfqgf8Y3ZyQsF52chCu0hCASJGz6L-BotgtFyCb_hBLGCIh26V8dl7xdKQtNbOM-DILsQuajG67hSoJANc7TbokSOdjr19GqOoRHpVmAhlJv1A2PcMKn3X1zp2mHnIDtByPTgBrznP6HVtGL_sXcmT0941li57s9sbH51qqjf_Cuz8nB_arTAjd2oOlKnLb2uC42admUt4R8eeDo_iFFEVrNnKYQ0uAHFe6g14qDWRSdYjJyI1v5JxTTR-R001DTrWADbS9kcEJRmE8RNH0OvSpKunTuFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به مناسبت فینال لیگ‌قهرمانان اروپا نگاهی بر آقای‌گل‌های تاریخ ادوار این مسابقات
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/90411" target="_blank">📅 17:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90410">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">Barko VPN_v2.2.apk</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90410" target="_blank">📅 17:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90409">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Barko VPN_v2.2.apk</div>
  <div class="tg-doc-extra">61.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90409" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👈
بهترین فیلترشکن حال حاضر ایران
👉
💎
با همه نت ها پرسرعت کار میکنه بدون محدودیت
💎
👌
پیشنهاد ما دانلود این فیلترشکنه
🔧
لینک دانلود داخلی با نت ملی با سرعت بالا
👇
https://uploadb.com/plx39j7b72sy/Barko__v2.2.apk.html</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90409" target="_blank">📅 17:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90408">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97be903d17.mp4?token=SXpcpfjXMF-f2XwmT1TkBthIJ9k98HB-4BCtkdGQgIppYxab1YKVEp1RriyiOOkzqx0CSSyncqeAwxgzx0lxDHmMtHm_nwWdbDx0Mj5bGUM4L-DeTqSwy2UrX5r7dc7gbVvhG_JovtRPJ6kKpSTaI8p5HLDKwuPl0FgOIyNgyyIbhA9oUT0dgSXqMHs2Y0iqxxOhEEva2yzn3hQEGvohurxWcdwKLrXgo1MVA5I6oOrN9Ntuo3PdC47AV3rFgcVFJVFS8xmjfuRu7_KVqU0nBvELuvSMT6aK-VGEfsQs-yG-hYR0UT5cTr_WAlqRDzGBLzvP07MF8bG8VJlspkAEwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97be903d17.mp4?token=SXpcpfjXMF-f2XwmT1TkBthIJ9k98HB-4BCtkdGQgIppYxab1YKVEp1RriyiOOkzqx0CSSyncqeAwxgzx0lxDHmMtHm_nwWdbDx0Mj5bGUM4L-DeTqSwy2UrX5r7dc7gbVvhG_JovtRPJ6kKpSTaI8p5HLDKwuPl0FgOIyNgyyIbhA9oUT0dgSXqMHs2Y0iqxxOhEEva2yzn3hQEGvohurxWcdwKLrXgo1MVA5I6oOrN9Ntuo3PdC47AV3rFgcVFJVFS8xmjfuRu7_KVqU0nBvELuvSMT6aK-VGEfsQs-yG-hYR0UT5cTr_WAlqRDzGBLzvP07MF8bG8VJlspkAEwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💙
گل یاسر آسانی هافبک استقلال به الحسین نامزد بهترین گل مسابقات لیگ قهرمانان آسیا 2 شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90408" target="_blank">📅 16:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90407">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JwI6HnNmD2WdILnxwF7OXAP55m8t71MqMXd-8CR9woGG7AuQEAqw_kUEa_FLQLw46dhWnMXIF3kfnHgK5z7PPdO81WY5gqDoFmV_0J7Bk6y4Ha0Kc8En4B38yud-qFNFOqoUi3ea9AoAxbErRcWI7BBXFBJYVG3w1PwbAYVPo1mLcvdHJpWfvirUXWW79YVG1U3foL0t0hYITwDuDAHTJdsERW6Ec4wAfDbUOD-8e76mfYLvU6zVRJLxt_wAT9U7qWpa_uJDabUKtFF9I17Cag8nBI51P0vk-_0BGl23lY2kSDgmDecLjSmuoppeLC9-Nwht-Na_UX7PcKW2OaTemw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|تریپیر مدافع فصل‌قبل تیم نیوکاسل با عقد قراردادی به ولورهمپتون پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90407" target="_blank">📅 16:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90406">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTBdUv1p2u1K_Q7O-Qkw323QSiA1Nq8Wg1o9ELK4DJMjcd53kzGegBVTBpXECEPAQuJQtrUFb2XU5tVGjNm6tSWPAWQu17azTRbqNLbX_rwSb8ACTDMWOADHX4xPt4uZRQ4dvSizGBiG0KftgaeKukAmwV1Ir3q-rcov9Bnrdf2hdVCuPKw7uSabztDBbD82d7NsmVERUiV9OiiLt-f91ouvTvHOiWFbo9Pizkd6VobJGicxUSYzrBIR6SgE559zmiGl-LrEk1wZorjV6f8wMO_WrQquPK3f1J7KcrTQ6VJq4vcUwGvWaUUOa9nyz9rql-B6V5h9Rz-w38WjdtkAYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
مثلث‌های هجومی آرژانتین در ۶ دوره اخیر جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90406" target="_blank">📅 16:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90405">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCSw0mWsqKO2KkxPETEZjbSZh_xq9LyhmxAyJCOr8VBr5pdNA3SI08fWBLOEbbHg2EORczciwql2QZWAu1reg8PRDHoKj8XSCCIE-WvY9eAu5EB4WGzC1yS9JG4Twz3s4xSZ9dbIoc0CUiloCha82wotFbXHkAumU1v0u3sC-2eScSqomkfjxp930AVwagcHJSFu5h08oSOQmEUuFz0hpUyc0-gM8UImOd2rs_Q35V4o4l8EK6YmT2g_q-xTBtvLBOFKkBs8NCX75DVEELNrTuk25e-3KRtJoW0ZBMkMKYKGEZARLe17l4gop80diEMyMH8ko2ipT43IRDr-VnCdcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">↪️
🏀
سوفی رین، مدل OnlyFans، ادعا کرد که یک بازیکن بسکتبال NBA مبلغ هنگفتی را در ازای بکارت او پیشنهاد داده است.
🔍
اکنون کاربران در شبکه‌های اجتماعی تلاش می‌کنند هویت فردی که این پیشنهاد را داده پیدا کنند و تصاویر جنجالی این دختر به‌ سرعت در فضای مجازی در حال پخش شدن است.
1️⃣
داغ‌ترین عکس‌های سوفی رین در کانال ما!</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90405" target="_blank">📅 16:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90404">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/toNTsq_4Ltl0L1c202zNNyATIX8T4VvdjPytjQt4LwCUk89a1mstpVCZhCe2g1PeEeFaZ3C2ybz4U2IhdJfbkhHlZYOEs5W43J5jAEclmJKvhr65BoT1ISp7_H_A1BawHibxJ0VVjUcl0WQ9WXdUAzDQVpaLhg3Hop18--8-hA10H3fnCzBIEE7fHCoTdMSJ_WnfTWV_YZ8KPZpryP9ecDfcwNb5_YHaBHpS2jnb6CEMFyDYd5vgX7EGBJ2Ob75Q1bi5gaYrysfi3wmwJPlOzHMCFgv0KrkqupM3Do-soTzmg9qz1MUdu7PQbq2ljt0dmYBussxAOivCfhaUpsuHZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شانس‌های اصلی کسب عنوان سوپر توپ‌طلا که قرار است در سال ۲۰۲۹ اهدا شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90404" target="_blank">📅 16:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90403">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da3204b2c2.mp4?token=dfQ4ACPrUrZyctRwi1_FFuHVjXvh3S99ztn85LYmHhmCGP4EXvc2tbvC2qFL68MsgcMV3Z3aGCPEH6Kr3Ma8xq1LB636aUoWPAcSHJXtPFCBXNJ6WHxYtU_FAUq6PZbG-FuHCnZBxoTbZeSC_k-iTyDrQkPfUusG4P6LQu_2vjLEDaOHlCW41NADRq1CBhxCdyih39j4H1yQP02ePbXH785dQHO-PAtpqMHeQCnhZ6wpU6jufh-WWfvhIq41BP-yPVfA6SKwTJUKV9Tp8E6cbjr7kXlRbCPUutGVLB7bv0pVjDWkqJNKMmxuk6Oy7HjBrMMp6MZSS3mfIib_ZWKWQBHu7WAcKRh9_V8CrpXESghCViLuHTBU4RAa57KQl5jqGAlRiMM1YOHqLOE_MEZdLdhwrskWRP1CfxP61G2tgQvQG-aU04HswLDmOGO-mKZj-L7oXcy9IGU6S9OEYR2aTq6Gtu9pdAgJaY-zp6wjPq2BnqyJKpXVL_k8WdYsX1qxxNAT473pLwmhLqkPG1w5VrfSyvRhFXvSXuLFCV5kVlByWCAxFTQPPAfLZkX98-TqMQqX-pD-fsamyR-7QXqXducYX6_4AGRlHS5p0y3TdNdH22bWow8SMPSl-OopZmgO84sU-OdIG0SzIfaMdrCl14w7pnkeJ5eYnOKrVeIn2GM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da3204b2c2.mp4?token=dfQ4ACPrUrZyctRwi1_FFuHVjXvh3S99ztn85LYmHhmCGP4EXvc2tbvC2qFL68MsgcMV3Z3aGCPEH6Kr3Ma8xq1LB636aUoWPAcSHJXtPFCBXNJ6WHxYtU_FAUq6PZbG-FuHCnZBxoTbZeSC_k-iTyDrQkPfUusG4P6LQu_2vjLEDaOHlCW41NADRq1CBhxCdyih39j4H1yQP02ePbXH785dQHO-PAtpqMHeQCnhZ6wpU6jufh-WWfvhIq41BP-yPVfA6SKwTJUKV9Tp8E6cbjr7kXlRbCPUutGVLB7bv0pVjDWkqJNKMmxuk6Oy7HjBrMMp6MZSS3mfIib_ZWKWQBHu7WAcKRh9_V8CrpXESghCViLuHTBU4RAa57KQl5jqGAlRiMM1YOHqLOE_MEZdLdhwrskWRP1CfxP61G2tgQvQG-aU04HswLDmOGO-mKZj-L7oXcy9IGU6S9OEYR2aTq6Gtu9pdAgJaY-zp6wjPq2BnqyJKpXVL_k8WdYsX1qxxNAT473pLwmhLqkPG1w5VrfSyvRhFXvSXuLFCV5kVlByWCAxFTQPPAfLZkX98-TqMQqX-pD-fsamyR-7QXqXducYX6_4AGRlHS5p0y3TdNdH22bWow8SMPSl-OopZmgO84sU-OdIG0SzIfaMdrCl14w7pnkeJ5eYnOKrVeIn2GM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
روایتی عجیب از کمپ تیم‌ملی ایران در مکزیک
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90403" target="_blank">📅 16:03 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90402">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBgxLN1jFRPlNuWT-zWQjkAjrrkNLjX8AjL5qgrxkcG3hPF5yKEk-DrFz5hic7NWLMetJS-S3CeAcVhQ2jwaX8fpe16F8rUOUEeWES_5kvRuMFMyLVaL-MFam_ZPVKHX2Wipk55Ij4K-XuM4xlJw7jPwjgb_ycTlr5PIZ72xB8hCcrrsQJDpynro1TdiexRaMtn6qr8urSfduPI8wDr59hWYQLf5JV8Ptchdj3TM21ATUTPiFglNZtEK2WszCSh_HjQX3ctjIsM-_yLjMzqZDoS5dY2HzeN590yplrftZRiqgvMepvNiumeCGGNXgIOFhL49A5p1TzbVz2Hjaut3PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنانی با بیشترین پاس‌گل در قرن بیست‌ویک
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90402" target="_blank">📅 15:35 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90401">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb048df6e1.mp4?token=k07sNyYFI7MYPALb4TcKCJXD4KCot5yxysweF4ihAV3x2VmGL9BG2Q_HPtK7L4EWESvQaARhmKEkVCswkIJAEgvqQhGe0y9-qpkqEuZ3k--9Mb-UalvHHyNAmFwrLH3mXA7cJtgaMGwFH5x_UMczVlC55F07o4-Yoe5ZWvK2fE6c4kvERh5JIjHajD3mWVQgwuGeGFWtlGeWK1qCO6rcH2yMSJBb_jH79EWNW19BF47rVSSYa14itVCZPXuB3-EGWhEAzW7KoMVAW3GXJBPLFyCnJRf1dA8eUIvt1vytisaoUEA012wnwgdVd6GOB8festzpycjHhQpgV8fzijKhcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb048df6e1.mp4?token=k07sNyYFI7MYPALb4TcKCJXD4KCot5yxysweF4ihAV3x2VmGL9BG2Q_HPtK7L4EWESvQaARhmKEkVCswkIJAEgvqQhGe0y9-qpkqEuZ3k--9Mb-UalvHHyNAmFwrLH3mXA7cJtgaMGwFH5x_UMczVlC55F07o4-Yoe5ZWvK2fE6c4kvERh5JIjHajD3mWVQgwuGeGFWtlGeWK1qCO6rcH2yMSJBb_jH79EWNW19BF47rVSSYa14itVCZPXuB3-EGWhEAzW7KoMVAW3GXJBPLFyCnJRf1dA8eUIvt1vytisaoUEA012wnwgdVd6GOB8festzpycjHhQpgV8fzijKhcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
وضعیت لاپورتا رئیس بارسا در ساعات اخیر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90401" target="_blank">📅 15:10 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90400">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgkaL_BAHf1K0rE3Annw6q20oxmZl2q2G2hkL_JZS_bWDWHI1QUPNCdQjkLKOPxDcpJJTQ39MWSM6WVIxOY5TzfJpKvpTd339eDTULJzbzwB7OTkId2W7SymjkkI9NSSVEh4sldG1fdM2OVrRx-ofOzMsLhUpBwBiHMRs3kqQBT-dl6ainidSA4INjlXz2des_-if2AvQPvkoNAp8u7o-qbU037C1Ah9AZQ6ptFFgw3VAShCAhzcRWH2E7zg3yJXIIJ48LHDyX_UmTO0pTjHv8mzKctriVJ65FuqRedBmYUw8PvVmoMR2G68slFXziIKl2Mw6mEkCtZVSI4Zywu3Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇪🇸
ترکیب احتمالی بارسلونا در فصل‌آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90400" target="_blank">📅 14:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90399">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d70d85d83.mp4?token=iTsusmOliF8NGogK6Mt1wusucnGUYUNshkPNpnXvZfKDa9UdkKbI4MViqHHvxvLNL9JckkOz3Ot-InM04grB2Nt-vy-lx8PcyDBBKbsLG3jxGsuO_lLAEMCKuw9cKEWzmjpx7-k_dUPWe45TN3n0ZFr8kqjkbEaoqQJEIYwz7wYxxCbPJ8W1AHErzFRoqlvhnSWpFCQlsmhHGLNmYn250psNaxfIC4kgiMJN82tSBV65DxMrCQqR9fU_MUxkNe-RLCSXroeA4bPGN4eZ9HxSZ2reLF58y6-UzSUabJmp_GcgXTCbIDhnYCdBdD7F5oUbiiK8sQXexlRsXDrf66ikDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d70d85d83.mp4?token=iTsusmOliF8NGogK6Mt1wusucnGUYUNshkPNpnXvZfKDa9UdkKbI4MViqHHvxvLNL9JckkOz3Ot-InM04grB2Nt-vy-lx8PcyDBBKbsLG3jxGsuO_lLAEMCKuw9cKEWzmjpx7-k_dUPWe45TN3n0ZFr8kqjkbEaoqQJEIYwz7wYxxCbPJ8W1AHErzFRoqlvhnSWpFCQlsmhHGLNmYn250psNaxfIC4kgiMJN82tSBV65DxMrCQqR9fU_MUxkNe-RLCSXroeA4bPGN4eZ9HxSZ2reLF58y6-UzSUabJmp_GcgXTCbIDhnYCdBdD7F5oUbiiK8sQXexlRsXDrf66ikDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
حضور کریس‌رونالدو با جت‌شخصی خودش در پرتغال برای حضور در تمرینات کشورش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90399" target="_blank">📅 14:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90398">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HeOEhrwz8L9CkdnX7hMIyplVt43avvSVZxnoT-iIaAeW1mif5-L9ChC_MqgGbbcnA39hmC4cJsbv8xmQJBMq8_35tc3esvcC4gUmWIvRt6v1Olg8THB2Oxz9O4R1zJZBphm1YhzngqwlQ23l_xnhVSZUZ2GVDCKEteXj2C2E6Bg21Li9WyyBrT89WSKKkTM9zGpwO0wwhnkEmCWEVaRG734gi2FjctfgDSMMgSs_Mmyz1-j6c1n7p1Nj2Hka8GZpD9fhv8BNEFhK_WdXUhVkfLJz0k2EX92dCdIc0faE4wCOkEmsfAy1c-R9JbNXvZAPdB_rqtQbE_8H7d6pXZFqFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری
؛ نیکولا شیرا خبرنگار مشهور ورزشی ایتالیا اعلام کرد که قرارداد احتمالی خولیان آلوارز با بارسلونا تا سال 2031 خواهد بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90398" target="_blank">📅 13:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90397">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYKtt1hd7cI9NzdaGP8GPnSswqnfy8JqE71ZTGEFkACxK7zjjDA9SVOYXUA6C1FGbgn1PGH3U5q83gjttLlggobCtJmtz_zDfLxMT5TP9-E38mRwYjpuKgRCgHICMY_0sJRmVteR1yj5HJ8PD54k5a2OOcL-ZseluemOawsYGqAYK-A3v-GGZoFRJHGldRgKYmifl1ktmLBtKGPhwMJQ_76z-6yw8NiD6S2gEqIVEgRnd77jbrLcyzf10AZ_YgINDA8uj7641G1UCwWnpyOYEd5xvU-Io5qQt1TKBWYU5kiQ7twkSZte7_f6v3UTac3bKBSBdraChxQuBgDXDX6HBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
به نقل از مارکا، ژوزه مورینیو اعلام کرده که با توجه به نقل‌وانتقالات پربار بارسلونا، رئال‌مادرید برای رقابت با تیم هانسی‌فلیک نیاز به جذب حداقل دو ستاره تراز اول جهانی دارد و برنده انتخابات رئال‌مادرید باید در این مسیر اقدامات لازم را انجام دهد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90397" target="_blank">📅 13:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90396">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
🇪🇸
#فوری از رومانو: بارسلونا اولین پیشنهاد رسمی خود را به اتلتیکو مادرید برای خولیان آلوارز به ارزش 100 میلیون یورو ارسال کرد. بدون هیچ گونه افزونی و بازیکنی. اتلتیکو، از وضعیت 24 ساعت گذشته راضی نیست، اما خولیان درخواست جدایی داده است.
⚽️
Channel:
⚽️
…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90396" target="_blank">📅 13:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90395">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ft9JpKk0lReHhhfM34iGqtlIeWgh9FLUCIouoaSUYmMJbYil-YuePQOn5zArjVbu3TSERuOFk52b-wJPvDaUyxY3XCwOsCOVS8HcouPOE0V42vAWvHlceo9vjqjN2cKKPpbqz1smuJOyRfZ_OpjoG1QgXbrP9_TT8VCcwufTGT22T0qcq5IUf36J5BoJ3KKn3Th7ATthE4GBgyFBILmx7A3r_feZl1Sxd345gUVWWvJhcKqpZy46pQO01Qd6fyy9nstz8hBrEVkHOHv3xJMBMSK3KMqKm3m4TstgiLvIPLDD2Wn42qX6hyVSMJGWNj3cITiQ8ya5spX5Pr7OOCpa_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه‌استقلال با محمد خلیفه به توافق اولیه و شفاهی رسیده است اما این گلر جوان اعلام کرده که پس از جام‌جهانی و برحسب پیشنهادات دریافتی دیگر خود، تصمیم نهایی را خواهد گرفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/90395" target="_blank">📅 13:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90394">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2YrWUssnXAzLgpXIyfOstSD2KUiHI5-FVStx_zGqQ52SlLpfbOh8h496ntJVjHlhukgETdj32sWGZPO8AZCZwU8G2PXGu2YsiODLxmTLNmgX0oQouAcBySa7xNbWGhK16C56HyNc6F2GuoR-OX2lqfuZNqJgIwx8WvX2pSm-nwPsLbJ5EEAxaBG4Yp78Oqy9rGS9E2iBko4KwLtlOzEir_4RqgUg1WTDKJy-UAEmtytOFR-qrH_B5YiKKAP42wpNOdNvAHtzu0yhy_YjRfpcSQKjWXy_-ZfNVd4x7tIeWKpS3QTS-DJs2JWaCVUmB4byzaffdnnB0wV62xEb7anvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#نقل‌وانتقالات
؛ متئو مورتو خبرنگار اسپانیایی مدعی شد که اتلتیکومادرید به جذب تیجانی ریندرز هافبک سیتیزن‌ها علاقه‌مند است و قصد دارد بزودی با ارائه پیشنهادی این بازیکن را جذب کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90394" target="_blank">📅 13:44 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90393">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjk4TKSyVi3s1QUOe0lWdbnTOFuRg9J355kSrwI-xcr2KaKAvCH_yXJMDFrXyh83AfQ37mepAHMpNjT-Zch4fkjYhcTaB2XWPp0kaBkkZgLFi2Dukl6Nu1X11L_MAh0YczhwP_XgR3mq8Fk4Lf33hQlv886-dwtrPgP6889pxUemOLHkZf37I9yuD9wWnVMIihCF_NgA5MsjV2xNVQ3XSuIuXzhU5IppyFLQywCO6G8b3InqyhT0M3SMHJRMlRf9WKZkEZZ-w6CY1UF6UdLRpnFMvz6an-Au1JT0DHzhApADbS-3l7sDCrPESBdoCybLAbQK3MBi-TYuGXBNlHRALw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری
؛ روزنامه آبولا پرتغال مدعی شد که مذاکرات بارسلونا با برناردو سیلوا در مسیر بسیار خوبی قرار دارد و احتمالا بزودی منجر به عقد قراردادی دوساله خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90393" target="_blank">📅 13:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90392">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gErQ8arJp3gfxke2_j-UWvO4pNL8q3vyjqgRGOwgQgTpgP1kpMHrdpWuW0Nj9TsqctpIsAl7SlCD-_pYjMYWI3unYkOWzNxzeFLhk0H_lH-1-YAj7vI0ztGt54XlRxA_gE_r4GpEWrrFzocW1AnT1tDTYIgVATsx6gb3wUlztQuuEyfWPVmJo3kNujvvaK3zblX-68Fh_RRrePYv7Ibc-qhqJG5nE0rNUWs2cit7Zcc5bNtJgwAerp7Bo4Imhcdzmy7on8CWxC9y9_OlT6vCRPqdyWa7NmAHNRX8s5eMUF93-DWtWgVFo6zuZBm2gJrhHxAqAh2w449Ihc0SFr_GmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
🇪🇸
#فوری
از رومانو
: بارسلونا اولین پیشنهاد رسمی خود را به اتلتیکو مادرید برای خولیان آلوارز به ارزش 100 میلیون یورو ارسال کرد. بدون هیچ گونه افزونی و بازیکنی. اتلتیکو، از وضعیت 24 ساعت گذشته راضی نیست، اما خولیان درخواست جدایی داده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90392" target="_blank">📅 13:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90391">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSeD28JBauKNN1HUqKrZnV46WVDFGv8mHlSLJZq8JYRLzCqakdKL10M_f5pCFaTcefvgnl5eeR1xoXrjYtkOfx9b6xgxmNOGY8R7BPI2kA9u4rgSdrtw4cttU9FTtbPFjrqcKGIE6fYNpJZhiqVscX0ZnDJYI6n5Zd7LGoqV7e-WDgbNLQnJN8YgKcczqb3u5rW8Gn6YImFE9v9rV-J0sc3uxGDBoh6KWeGqm_21vASplzIVIkUckxdmY22VxVozaq30lWge6pcBcsKPqhMkX-lofTjZ29SEEA3nNnE0ojZ1HEHiTxysu2TQAK4ouSIY2V0-pZLCg6yw79DiP3H8hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
عمق‌اسکواد ترکیب آرژانتین در جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90391" target="_blank">📅 13:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90390">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/766445bcae.mp4?token=Pi4byG_tIANBwocxExR7hXNrVyLVeEH5rWjJafIBG8XLtPN0UFwtQP9-FbSCEr6z4x0nXdHDy9bJKblWbfTSXgbZ5XAVa-yA5rDQMLO6RCj_B7aEdz4MMQrRmz6LFAHjzpm_I8npnSJ9fl-GuJ4MnCghCAcDLP3tzOiLWCTCojRO9cCDdMN7aeZG_LmxK0N2CMR5V32vsxqpP9fxWlQYq9Jb05Z60y6uYI9lOJMYUc8gtRztdW_w3pkcQTL0wPhGEScyBiHN-ZA_rB04NC-Twrm9TWQZqi6JkRHPbVUqojy4nnwwzozt-M8HUoYTqH-2-LLinUtrBpQjRWu2XK5yPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/766445bcae.mp4?token=Pi4byG_tIANBwocxExR7hXNrVyLVeEH5rWjJafIBG8XLtPN0UFwtQP9-FbSCEr6z4x0nXdHDy9bJKblWbfTSXgbZ5XAVa-yA5rDQMLO6RCj_B7aEdz4MMQrRmz6LFAHjzpm_I8npnSJ9fl-GuJ4MnCghCAcDLP3tzOiLWCTCojRO9cCDdMN7aeZG_LmxK0N2CMR5V32vsxqpP9fxWlQYq9Jb05Z60y6uYI9lOJMYUc8gtRztdW_w3pkcQTL0wPhGEScyBiHN-ZA_rB04NC-Twrm9TWQZqi6JkRHPbVUqojy4nnwwzozt-M8HUoYTqH-2-LLinUtrBpQjRWu2XK5yPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
هایجک گوردون توسط بارسلونا به روایت دیگر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90390" target="_blank">📅 12:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90389">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WejMUSw6aKGfAVYqhLeFfHd9DZUI5TGBNWgnAvFyOAEBXgBJ5MxMMWtV6BE5kgTM4NlQgEsgLMrhTqySe3ri_iDAeISudNnVi_hjw4sqVSTTrnm1ueHh78djEcIJKtMSF9c_-hEii5sKEW62EsW8-f-YBcxj0u2nqSPfUV-Fii1kd8n_1bobv5OvuBKoOLuJnPdFy09i4AcCsmYsDPefamN5S6a9DZ7IHDbQqLuKgCrEiqMgNVXELd9vPitVfbwHEZP8lA_Vc1Q_FDFbOZG50Up6z-zk3EW4bjSxTArPj3EcN7Zw_ngA9ol7b6w6Wvk-hjcn-huBV-UVGtgU6RDTlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌وانتقالات
؛ باشگاه بارسلونا پس از تکمیل قرارداد با آلوارز، بدنبال جذب یوشکو گواردیول ستاره خط دفاعی باشگاه منچسترسیتی است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90389" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90388">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">⭕️
بدون واریز شرط ببند و بازی کن چون وینرو با ثبت نام و بدون نیاز به واریز
۵۰۰هزارتومان بهت میده
❌
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90388" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90387">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iccr2NkRfPcGFaxe_LSi-myNQv6NrFFw7fzC_OVPM0UAY0t-uKMfZ5LVlI2FIVViNSMkuViW-usSVz24uZJsAD1c_Vp0WrvZWjRswloiJzTXF3iqV2cDx02IKiwq1nEq86OTaPleJqrfyX0BiW34kKZQNUlnATEy3XGYvNY419CGm_Gs0tuqUn_O92qj4bSM18YwQAON_IgfKJq_o8qVYid5mIF4fxzjonZrIdbd3MXH8rpSKbVF_DNjLztuw-kh9L8kO1xdGafwIZ8rzDqCALVOn79C1X6fxESuaUvnvE4jYCr-RBA0Xqb5MxyKrl9e0ca0HusvhKZXTe2f2i2eCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بدون واریز شرط ببند و بازی کن چون وینرو با ثبت نام و بدون نیاز به واریز
۵۰۰هزارتومان بهت میده
❌
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r8
📱
@winro_io</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90387" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90385">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTFh1VkxAMc2rhGdB7igSzIXCiPbACHIzZAYrTiGua2T8Uw1vzs0Jg91351J9w5UqdxfSweDJmt4CPcJ0urX0OowHVz6YtiDuk6GGgv2MUq-NTi2apiFAK0LWylhXsBCl2Z67ER_y2k1SIAEkhfl7LNWWEgDsp5OaaghIQdwU6nHscOC_FYjzlD1ovuK25GoFZnB2d0JQepp1WM2-yKlKQuNr5-wcTac0zuCj7w8uvQFyrjciZJrzydH1uNrwu8MOk1vXi0nbUQYRi0g2WEHrZSlxVT9t_nweqQ__0OBDqGDaVDPD8rP79bgsru1u9lmjkFay1D69pPr3M92FdENgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌وانتقالات
؛ رئال‌مادرید با ارائه پیشنهاد نجومی ۱۲۰ میلیون یورویی بدنبال جذب ژائو نوس از پاری‌سن‌ژرمن است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90385" target="_blank">📅 12:24 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90384">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZTnJtMnUvZMjy8Y-XM9uZipv0QHRyQQdIKnSpB4TBQoWMtWu0dHJm_OJLt48DUYGiRx-rCglrkyaMhHRaiK2_VIWAcF5udgWt05x2cEzK6l3SBCyJGYbFmD4mDFVbV3FpVwOvoR3BHCYwo1mzm6MiyV8JSo3r5mpXyXhvskg04HWCtSRh2ghSeAYvIz8iOzoXlyriCmV4p3a8HXcIAuqCImc_VGl0QAA85UU9aBecWJj7EpLkhqS3yUXg9AvQeijf9-34RJoVxuuptYuTtnMHyoBkkz7kBA5MLNofXRtLS4aB7kxhe4BEJQGU5dJbtQaavkxBLvPYr3b7kYn_fKPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
لیست پاری‌سن‌ژرمن برای فینال UCL
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90384" target="_blank">📅 12:14 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90383">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32bcc3a9e5.mp4?token=bHgNZF9WqqfWiDEXLFjHyWMCHmexAkuIwqyJfQ1xvXMu2hK_ylda60e8o6ksTi78xO_8GWnsj758dDLrWMDxwDLDpRAQeqsMU5_xnYcqlSRMkuVYm0WIWMVciLI1Kv_yv-MpZHTa6rtSN-ayuLKxVzlNv6-sMje45_g-aUT0B5oXoDEatQWWm-9-an0LK0CuYyUDdza4jWkdDSMnDqPtZcS5C3pnH8yoJ6wp0UsqL9MmLqsxREGLT5PAwmq0fkqbWviWYUlVLs0tdvlb4Mr5cZQoAIGDpJU_uWooCZ6nH4dp9QY_M6rx3g7DgeFPxhSpjjJ57EWYixpMb8H4M1JUrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32bcc3a9e5.mp4?token=bHgNZF9WqqfWiDEXLFjHyWMCHmexAkuIwqyJfQ1xvXMu2hK_ylda60e8o6ksTi78xO_8GWnsj758dDLrWMDxwDLDpRAQeqsMU5_xnYcqlSRMkuVYm0WIWMVciLI1Kv_yv-MpZHTa6rtSN-ayuLKxVzlNv6-sMje45_g-aUT0B5oXoDEatQWWm-9-an0LK0CuYyUDdza4jWkdDSMnDqPtZcS5C3pnH8yoJ6wp0UsqL9MmLqsxREGLT5PAwmq0fkqbWviWYUlVLs0tdvlb4Mr5cZQoAIGDpJU_uWooCZ6nH4dp9QY_M6rx3g7DgeFPxhSpjjJ57EWYixpMb8H4M1JUrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خاطره مشترک رهبری‌فرد و شاهرودی برای رفتن به کنسرت ابی: پرده‌ها را گره زدیم و از پنجره...
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90383" target="_blank">📅 11:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90382">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OvyrwKzFIoOasRPuIO5l89xaiiXwJKRZbV66dTHSfNXUdwJQPczBnE-37h-woSivgJ7u0zJpqxbFnRo9b85BIQsPWIdWsXat3dDwSv2Hi7u5LdLe5y_NGluFu6_oeFnZ2xq-eCJ7EzqTcgbl7IcEcX95rgZfMyR6TAtjh-EttD6K6Th72p1wT7Z7XqpS2KMiTeIEEyZrBoEmhS0MWek2iZaeYqFkrvdHyAXwA16J_DvMrvuoZ0vvWYWgP-mc8j0Qrn5Toiqe_Zw0mV0pYpkzCNYPIjgtzNFtKIdMus4y4L4Gw5YYuDsJOW3vELtdolkZldEsZXFn8kZoRwCBFlRJJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری
؛ اسکای‌اسپورت در خبری اعلام کرد که ابراهیم‌کوناته ستاره فرانسوی لیورپول در آستانه خروج از این باشگاه قرار گرفته است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90382" target="_blank">📅 11:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90381">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O2DMA_QwRtdH6b9K1kRqdGJDnNL9u200_TybtdWtyu5ZsvSNxsX_-LGzppK24yaWH09hcCuXCQ5zH8u8WVcFeWxg0w8TVOfzxOqH-7k7IGpUVBbNPw4fgygXbGF1romscWGJ2v4rpS7iTLPi9KnkFJ-r090A-NiNwcqPjnwHvW1hs7J7wVADPV0N32j1NP3OfGHWB6LOSoY_vztQXTXNsoBARWmmneuzjFVQSJmDfD9QvxCl-xu4Z2iwJTWIwMh-hS16up3_tWTd1La1JmClict3dLQaOZs-LaS3AJoLY3_mCq-WWKGsaGe-3IuensFIB9EBbbylimAXA_4oX1dEow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#فوری
؛ باشگاه الاتحاد عربستان درحال مذاکرات فشرده با یورگن‌کلوپ است. این سرمربی اعلام کرده که در ۶ بازی اول فصل جدید، دستیارانش هدایت تیم را برعهده خواهند داشت و سپس وی به نیمکت اضافه خواهد شد. درحال‌حاضر منابع عربستانی از بررسی درخواست کلوپ توسط مدیریت الاتحاد خبر می‌دهند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90381" target="_blank">📅 11:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90380">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJuywYD9w1MAH2NPZ6J5F98lecQuXIUD69OT5d4SwKvgsrcQffgIQptV-KjJ17ONbB_npnom6vxs9htoqDmZK0E7N4BNOck_FLo8bv4dTPGedct9beljyo01TvSon1PdNyV_VJVmre7PdJuA7wF0VQJyIxJzOQ_ErNIjKG-oW3bArX86mQhY0LMWPEvOW9jgHNe-9DViUl1q7nYQuvBprVzo4-8tUlJiBdbAIwo7BkSBJXm3rDxZeeKqTiLmWYrkJbpr8CJ6d6NHCcBx4dUODLfPwYffES3FoLZOaQMX6ZA8tBhg7SH3rxkqwdZ-WclpR82Kiw276QGqlEHSfV5GHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
استوری ژائو پدرو ستاره برزیلی چلسی؛ شایعاتی پیرامون خط خوردن نیمار از فهرست این کشور و حضور این بازیکن در جام‌جهانی در ساعات اخیر منتشر شده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90380" target="_blank">📅 11:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90379">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZnvazYh2JiK3UG3ShwW1AX1zS3n1P_JrF6mBd3YmdN69-fTlKGgjRMeklHKdb7H4BHamgj5Z1FUjl06qz_rWKQf8pbkBR36b0zqd-bataCiOHmOlIbT4du4Ct2dHaKEPX1Nmw55i_E5CyHulXFsC8OoTj328wiaGSwT6V2biUpnffYz12Y_urRlwZPPV5c15q8FXagGGLEBHZY7Veapt4pBtJxAM8v5bbh8DM3JlRuPqVtkP3B8-t3ZPY-X6MQUas3zVBOit8VD6dP_sHy-NGS7MqJbE60f_hfqWRJdTvfhbqtieHYSHNvXGg3aBtii0vzEeCA-tIuaeqB_Qaty8bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🏆
ترکیب احتمالی پرتغال در جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90379" target="_blank">📅 11:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90378">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20638b4d5d.mp4?token=S94x3cugErMJoq2g10dkoVQzhRVU7t7ELc_orssfYK2pwGd69DVipDRBkq0hGjjKcrfxdVJm_BNHvykUqNzt9gyOan3OfzHMUUZVMgBp1Ok7j7RXAzaNowSOoVIt5EriivsCWXAaBfkU5B-gae9kkSMhIN0XmIMpOz2MLssUHMQmsTcAmxlJhU3CBfRQTlS64aV9Z__tJ_JWyXzYEile3tCPkZiATbbZ00Xg8X9OSniybwh8fW_DA1j6RvMomP0jZJbOpBygCHWfpPF_Wlu8OCmFTVqVbGfOa--D041RspUhYKsRFU-o_riRQWd_e6gzTb-gM4TdeLMmPgkMbxtJuzGp0j9rPZgmL1xs25UjP59BPQat6zKUlf-MXpcL3pjm118-VnGBvVnUjDLjTyNP5jzZeiziHl3Ut8YlQXxgPoWFOGoej4xvl7ES6IPVMHmdWJvP293CMXYVi1z740JQimoswpjYinwvBIG9Zmud4A_r4Xv19q4P6KSfyHcLhTNXr-9xKZd7M8cFIE_igxD_vOUv9ygWDvttaAP7NaP1N-h5lOc2PZqfMkA5tTaQcUnbOMXZX7ZRzXTIhFsmxO_Nmdz1amlkrK9hPl9xOAul6GVezQwUxSek9heLrZ2vIibyRKjKX6D44LPE1HGWob0hXEwSO_HKJiBM3X8J3UhaDsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20638b4d5d.mp4?token=S94x3cugErMJoq2g10dkoVQzhRVU7t7ELc_orssfYK2pwGd69DVipDRBkq0hGjjKcrfxdVJm_BNHvykUqNzt9gyOan3OfzHMUUZVMgBp1Ok7j7RXAzaNowSOoVIt5EriivsCWXAaBfkU5B-gae9kkSMhIN0XmIMpOz2MLssUHMQmsTcAmxlJhU3CBfRQTlS64aV9Z__tJ_JWyXzYEile3tCPkZiATbbZ00Xg8X9OSniybwh8fW_DA1j6RvMomP0jZJbOpBygCHWfpPF_Wlu8OCmFTVqVbGfOa--D041RspUhYKsRFU-o_riRQWd_e6gzTb-gM4TdeLMmPgkMbxtJuzGp0j9rPZgmL1xs25UjP59BPQat6zKUlf-MXpcL3pjm118-VnGBvVnUjDLjTyNP5jzZeiziHl3Ut8YlQXxgPoWFOGoej4xvl7ES6IPVMHmdWJvP293CMXYVi1z740JQimoswpjYinwvBIG9Zmud4A_r4Xv19q4P6KSfyHcLhTNXr-9xKZd7M8cFIE_igxD_vOUv9ygWDvttaAP7NaP1N-h5lOc2PZqfMkA5tTaQcUnbOMXZX7ZRzXTIhFsmxO_Nmdz1amlkrK9hPl9xOAul6GVezQwUxSek9heLrZ2vIibyRKjKX6D44LPE1HGWob0hXEwSO_HKJiBM3X8J3UhaDsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🏆
هواداران پرتغال در انتظار جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90378" target="_blank">📅 10:35 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90377">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5359012d10.mp4?token=MTaF2vq6wxhUBhdWUpIXVaTpjKAk59EO7YynKfWdK5I06QzwcMT219QQuebF35cjBJB18wUFWamJLOU7Jh9170PZlrLv2EKO_Mys_db-9cXiu_dgOqjMFRNdYlF6dr07oXcr8aQdK4-wAzij_1dakNBFfijJkaxZr_16-dXbaBESexoySv1cZMLzJDATD1FtPPeHYrOZPtZCPVnezR4rmykY5_IGnHf1TLQyrPCSIP6BvU1vbMystR995U3B0CbaVCzTngDL1WDpPBqZWbjN_jJjsHLn3knHuVcxK8M4DqYjEKjN2Qjj71vDloUGiJwUyzudKDEHObXVbi0j1HwS6FrEcAyaCDSWnQKO0-AW3r5genTNd-ic1E4b-i-J0nCIElkbrZkKU0ECo8GMNdNy0ozUakws0RqukFBtnE4OhZpuvZ5uNmBMp65bf0enFtoBFBoGx6RCM9Y497WK7OGqK54BVGfcxrzXh2BbNUftZ5OFPoXywrTO_q2ucaqewnqQD_QemG76Qmm-bCANtjELWwIj26hPPFvV_Qa8U6kR-Swv8J9H9JlC9NZTuGGo1LH88rQAJVbYVAmdxxZGB2YNk3o5P9N3l3u9MpV5RitUt88eG_Qfr6Jo6g7M3cdfmYcmkqsGEX9jLZeqoclsCUwBsxFrskiJFiSRwGqs2-b9d_8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5359012d10.mp4?token=MTaF2vq6wxhUBhdWUpIXVaTpjKAk59EO7YynKfWdK5I06QzwcMT219QQuebF35cjBJB18wUFWamJLOU7Jh9170PZlrLv2EKO_Mys_db-9cXiu_dgOqjMFRNdYlF6dr07oXcr8aQdK4-wAzij_1dakNBFfijJkaxZr_16-dXbaBESexoySv1cZMLzJDATD1FtPPeHYrOZPtZCPVnezR4rmykY5_IGnHf1TLQyrPCSIP6BvU1vbMystR995U3B0CbaVCzTngDL1WDpPBqZWbjN_jJjsHLn3knHuVcxK8M4DqYjEKjN2Qjj71vDloUGiJwUyzudKDEHObXVbi0j1HwS6FrEcAyaCDSWnQKO0-AW3r5genTNd-ic1E4b-i-J0nCIElkbrZkKU0ECo8GMNdNy0ozUakws0RqukFBtnE4OhZpuvZ5uNmBMp65bf0enFtoBFBoGx6RCM9Y497WK7OGqK54BVGfcxrzXh2BbNUftZ5OFPoXywrTO_q2ucaqewnqQD_QemG76Qmm-bCANtjELWwIj26hPPFvV_Qa8U6kR-Swv8J9H9JlC9NZTuGGo1LH88rQAJVbYVAmdxxZGB2YNk3o5P9N3l3u9MpV5RitUt88eG_Qfr6Jo6g7M3cdfmYcmkqsGEX9jLZeqoclsCUwBsxFrskiJFiSRwGqs2-b9d_8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
پنج‌موزیک رسمی جام‌جهانی دوره‌‌های اخیر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90377" target="_blank">📅 10:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90376">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dv82SYuoJVkbsV-iMSx_3YHPEXEYESrgb1jDZBKpiaN33xJ9fhQri0vGBDGXcwhsODIfZGQangh_XnGl39vgVDig4EQKdDWeCPj5v5CBc_gg2PP03-2VXWWL9ZWY_5MsPCwqdpEwJzWNrp5e-b1JNwuzMffCSQAhWFxiZ7nX1MOE08oPdZttUAXFzfHIEb3EOcvI1pm_pjqQOJoVGPRnBq0mXTKKH0AE0zmaIEwfwRQOmPFf22rGGx7VnROHiroZ5aMsKPzwQ3HK1X-snveAfUI6lhFHt2xQw0ZMvRx5Z-b38QHscuj5V8Z9XSoKWX19Zv49KONPVlGwHZl-Mt8uXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🔥
تصویر جدید یوفا از جانمایی ۴۳ دوربین پوشش دهنده فینال لیگ‌قهرمانان اروپا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90376" target="_blank">📅 10:07 · 08 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

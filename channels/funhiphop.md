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
<img src="https://cdn4.telesco.pe/file/gPcOaKS6DkoCkJO8nm6LnzbLNEjstiCgwbdF_LexKG6jt1sbvgKz-JcFe1Btegq7YNVEWxKki57-29DzwaKcGEk6zmH7G840f7it-CuQrgS0ITaFV7zwZfwqDs8NzagVw7BiYLquMgqlJQuifE7c7_pX7Ywl0kGcuVJ0EWCA7RZzjrJwug327-XeRFqZ1r2x3GI6K8dL8vESdysf4miQ1zgob1o00ScjCHsPMHX_X1XblonL-SLy_-KkHz63OLTZ6R7CIKp3uI6mu9DGrNtZCoJZF4rp76BoR9fJzwu9TqpQO_IXn7Sz0vpvwESTKJG9Q2IbYNN3ZmQ9vu36fJ8EyA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 182K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 15:39:41</div>
<hr>

<div class="tg-post" id="msg-79414">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwDw9fG2iR_zUWIWnBAAgrXm8PLk8XphEviFxEC8_Aqnrv9beoTsAqyPvxj9jHGd7aYSz0a6znt46YwQtD5Vhy_KYM4nub7qv4gp3kkzns2G7UduNBnMozga1fVLbv_LeDOZfMuOIv-_lFmV3TsHShMfDuGjEG-lvZxrV_HAzBgOjUxYwJNgIQyhjwUJcajE0k21Be2chFTGQxBM9OCuUH6ntPlsGVfPS2x5RQ6D-ON2_bTBiUD-fUkEc3oDY47-5nton1ocNBe1oKq_Sx12JVacQWD5AkzvSPClopd4P7kBaeFUV9m_pwSR8n-0Tq9Fp7K8pEJsA8vk4uuKsZbzGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همینو طارمی گفت مسخرش کردید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/funhiphop/79414" target="_blank">📅 15:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79413">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nymdG7VBgByAzw8n-VfE487x8NbjtojgIYWfW1BKZzeM1Zr3yW9DXRhjR-O1dumSCNGuVf0PjmWJwoESdIKuvEeJfW5qPg6A9UG6Kw6n4Nu8FejWvKeaWW6gouHCPaPb7MuihOOwgr9SGVSzqAg-wyNidbb1Oi-QhvCBe9pHMteJzNKSpg5LogH8mDyIGWQS11V4YInrmd2XkTGN4NIsxxiI6ONagHTm91M2sO8rHv2QmsjqeRWba550MzsGAwxTZ9qb8IqBpymRxPfS4usGNfLGA4prEps5Qp-qS9RfemrWXQ2aeAmj0jC1gcZqCIF0HC-aOF03WATTOYnK_aAOgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا این کصکش تو بارسا از اسپاس ۴۰ سال هم جا میموند
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/funhiphop/79413" target="_blank">📅 15:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79412">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e956f60f57.mp4?token=OwlhsWMBDCcapt3wyCUFYh0-bJR3oOYb8LV5dgUOfSoQYDzM1s42veJ0Qnnew4WfhVW55aqwrSy-Jzk0gMQMxTbWFIpsx_g15gLI1D3Xl8dqH8LJ1EBkWRolSSjXnHKCi25AxQ1i3M5s08gPKtNTERVSO184e9USBm5Akde79CmOoD8csJ5Kui82Z3km09eoo7WjhR7v9w609W5PqnntUPOoLo7__78F87lnkOgTey2orAXew6bNL2G3LY3p2Y1oYazyIiySfY2ERaUKo9q2zHgk7NZ-C5QI_fmu4Mcf71tOyxz8vC53mFlNW0HrqZwAt3s1btJJ7HyXm_LR9_0pqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e956f60f57.mp4?token=OwlhsWMBDCcapt3wyCUFYh0-bJR3oOYb8LV5dgUOfSoQYDzM1s42veJ0Qnnew4WfhVW55aqwrSy-Jzk0gMQMxTbWFIpsx_g15gLI1D3Xl8dqH8LJ1EBkWRolSSjXnHKCi25AxQ1i3M5s08gPKtNTERVSO184e9USBm5Akde79CmOoD8csJ5Kui82Z3km09eoo7WjhR7v9w609W5PqnntUPOoLo7__78F87lnkOgTey2orAXew6bNL2G3LY3p2Y1oYazyIiySfY2ERaUKo9q2zHgk7NZ-C5QI_fmu4Mcf71tOyxz8vC53mFlNW0HrqZwAt3s1btJJ7HyXm_LR9_0pqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وای خاک به سرم این چه کار زشتیه
مراسم ایرانیای کانادا برا رهبر شهیدمون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/funhiphop/79412" target="_blank">📅 14:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79411">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اومدم بگم بسه دیگه گاییدین از نسل یک مووآن کنید، نسل جدید گوش بدید، چشمم خورد به این پشیمون شدم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/funhiphop/79411" target="_blank">📅 14:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79410">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پیشرو و اوج یه داداش دیگه داشتن اسمش امید قدر بود، اون زودتر فهمید تهش چه آبروریزیه از رپ کشید بیرون
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/funhiphop/79410" target="_blank">📅 14:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79409">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">علی اوج چقد پیر شده پسر</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/funhiphop/79409" target="_blank">📅 14:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79408">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تداوم و وفاداری رو از پیشرو یاد بگیرید، ۲۵ سال گذشته از وقتی شروع کرده به موزیک خوندن، هیچوقت از کس دیگه ای جز امینم اسکی نرفته.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/funhiphop/79408" target="_blank">📅 14:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79406">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t1R1GsB_L3bobedn7AFIXXS_F9igaFokKktZywjR7UsTxATWea-0cqW0Jy3Zo7vvON8TAWyhIkHDVv9xTZdC0CTQLmEg2R4AJkT-6inJ5QaB0i_3nUId9_O0GjK2wil-MH9-__StYc10EhT5sxga_3mbEpFrDZl_QhyIeuI4Ncp1sIcVXx72aHhfip6Ox97LUE7_zmfwq3E_EhAItD5PPGpzoEgCDFlOwpSSvg5uo6xkrVQpNQ99QUb1i3GPdrqXNc89-qNh9mHXgwtcGi4Is9LF9K9T-3aqxhaty1XcA5cyfOWOWmEwf8vEy09hG1TZDJk5ivmDLrjdvXDZEWzPcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hHr20J6mvTpURhyNDXiJNndpfK-dxk30YPBhj7AwcOHQoVeev07H_eqn0plUsXgIxNlSD9SwNmXj79UZTMA-Ztce0U-h1aPdDURhiOiZPT1fP9dQi-_LD235ghJVbQ74kZajdrSuZhYF1FGyE7zoxPKkNhi_S9v7nXw5RcMS_60oRb4BoY3C5-eGDv8nKjS2C3lNLagBk4AU5TEzNdirnTyXlYFBoYHiqTTgMD8MiT9HzTsFBGhTrh21lSnSgef04sEZAHXryPxgpXD64k8K6-CZ5olnkxK3ffhMDEnmtQdaz58RRmpdRIj5LPn3_ZHbuf-bYoS4RnC_6n2_bgDZ3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترک جدید تهی، پیشرو و اوج به نام سی دی منتشر شد.  YouTube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/funhiphop/79406" target="_blank">📅 14:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79402">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یه لحظه حس کردم با ماشین زمان برگشتم سال ۸۵
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/funhiphop/79402" target="_blank">📅 14:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79401">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترک جدید تهی، پیشرو و اوج به نام سی دی منتشر شد.  YouTube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/funhiphop/79401" target="_blank">📅 14:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79400">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CoKAmW2rw75TEvIes-8LbBcm4QAss52x75rJ2ZmUwBqckP6DNEGawhyUZ_E_6sCwM3GiOdccSTKPwFEifAHi0XJ6SYRdDrtBHK6LG9KBcG5AUbqSr4FfpnB-EpqWSix7eAD1IJ53dK6_DLlru-CapmPUJmyvfoMnW-SKigvykJIfTz-jbPEvl7AVGQVArAGWXS5i3LWMAGnyJ0scoKdLSUU6l4-bhSXzWoG2CluHF1G6wvVvf_mVL4yF8BjMSrMs0kdOgK2ku3KNN7Q4mSYsT247b-mJtuRbvGlAdFy_JdicMUerBP20FcQsgwqtjiau4pHMZVVF5_dB9QquHqc-pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید تهی، پیشرو و اوج به نام سی دی منتشر شد.
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/funhiphop/79400" target="_blank">📅 14:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79399">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUHAPOYA4j58gYLXMx3HKmus92rlgg99mE_H1y2MbPjQyQJNfaHZxHtiWph7fxdBQgcRYo5oWGSXLUQxCCBpzQ24IzL28c5rC1vE7IYuGNlryaF66QLytfKlQm15vHaIra__x8zWJFYs-JrhRxc1iEhESSMe8FeU96fyN2qW9ICO-1fbtuTWzrp5DpnpYnw5T4bggZPcOyP2jwipK1FLhz4FxKLx2svl2PNzKtD4cq8XucHaOaLQ1nJv3x5DnJ63c2O92U2Lr3rE4N4A-kZqedHT57Cs9-RXBXKXXjnlHPjxOKQRouoUUimVc9-PejlBpyi7JHM4gy2aqHMtjBDJnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاربرد این اون وسط چیه؟
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/funhiphop/79399" target="_blank">📅 13:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79398">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4kKy8yVbS4I1mlrp4YqZqhcQI5HH-BQqBFWVgZWLXFmTKAHgaE50KeC8ix3H3S2Pjjq0erkfKjXfhFZvlc4HLld5wYAcJ0IT_ICxNjTxLAgN8AU9CyV-LAYlASk65rr_qcfH9drXdvFFfN9mCBUXDZGDwuAsKOX6FE7HqBlsh17VPiV3Koj_i0hqTRu8sGrTLMwUfMJr85k-TeJ17g0cHeYoO1NStUpaNsZLrsJZggx6iv-MIP4lVS_c8ZTyLg0QZVK-U8INloe3X4TWBEiUxzGeplxGdeNSx3zdIQLScMkeia778DFKryByfbygAOYN34EDMwbF-AeTRerFXhiVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلمان تصمیم گرفت یه مربی خوب دیگرم بگا بده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/funhiphop/79398" target="_blank">📅 13:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79397">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تارتار سرمربی پرسپولیس شد</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/funhiphop/79397" target="_blank">📅 13:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79396">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3DzMzer84a07V3k1fuJrpJUqCd-zTXh09d2K32ef0hh0YrpJdZwgdy_LU6BDYgky0y_OYlUAUiRbI32e66hrAx3r8I1Z2kfXiLMw0o5MJwRjm69wa4TagsE58O4e9Qow1UR2oK1PMZVZT1NagRf3u-xVY_i_e597hptW4B1QcovAhvx_NYNyFmpsgiVpDsq2yLYTn36a_GbUSLnYLUbDGI8t_AiAfoMbHeB3N8LpR5-2GMt_IkO0L0zZgRozr1eq8F3VgEb9V8MeHKlfXFdkmSyimtjJc5W9hV1WENqJpb8xEjS7mBEdtJ5_7SVT7LbyZ-z7BD80cUUGo6OdE7guQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">MEGA BANGER
😊
😄
😜
💋
🙏
🔥
💥
🌈
☀️
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/funhiphop/79396" target="_blank">📅 13:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79395">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTeA887RNk1dcwWxrRJd_C4ptIqFw0TDsuHfgxTG9v5J--GTcl29F4VgwPusrzDpvki0odMvR-2WRv7LwXoqqN30nJ4xoF_Fh9fkeYXrF6VVyr12aOi50_GWV4mib6hv8jZBQXOzP1h1_gsCkYQky7mVDCIJi4XXZSxtyJ1mO6oK1RR9rdshe02RhygDW1POrma4Qp44bRcrrB8Hr1LBIetT6bcLGAlJ417y1veIQ4r6sogEcC5wX0C2LJwazQm3LdCCv4hnfYGQaM9Lv021bTp0tlHXyr7YmPLaqYFGNcD3D4sNADWpgZjVumPlAAv5GMu8HdJEddGZzEPWLwLJHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکششش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/funhiphop/79395" target="_blank">📅 11:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79394">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">انگار بکام میخواد دروازه‌بان کیپ وردو بیاره اینترمیامی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/funhiphop/79394" target="_blank">📅 11:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79393">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/exhQF23WqsfxJQ5762Nu-GY1FwivNfi9ASkKcQnQDQE2rPjcQYuwzKnqa9Zo9-jvOdFktWThOcy4hlOFWARmskmkh-qXqcCGlHVgt7jDX9zDC-WHaxmbzGd_Ynv8UnBzi1ZwUy5giEBT_3HkF8FbJZhpdKFBeFuubba_oO_yqoFPCw37kgn81yp9_L0e4gLi6QZ6cTRy7efdbVVKV1pts6_-51fy1nP7_j2JLYF-d3touTM010LePugdeWgRlSZmd_BH25UtBo3hQEaOamEYggIbjnk78Tu4qnu93M4mhKixrWdDO_KOM_EkorBGRwO3jJimSxOJYm9NjlxnbxOrFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه کصخل اگه ایوب بوعدی رو نگه میداشت حاضر بودم سر زندگیم ببندم که سه دوره پیاپی قهرمان جهان میشدن، تنها نقطه ضعفشون همین هافبک بود که ریدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/79393" target="_blank">📅 11:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79392">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2rIbQRo6y-jBVacIYm21YzW2y6msn8iO3jGu0XlcZqhcw8fzsm6NeCOie6MnZUJ_qWbTAk-Y4XsabBRhlk8m4PYcKd5fQaDYwmsXNeZS-yehUQQFgMjTLmveJa7xA4eU2Tjn-iB0sLreeqNwIs_m46llNaEz7OVTuG0U9LHd3-37X4TMrRWfsjoYxSHPu2MakEansLZeq1JpAX0roqUXeD-k18jhZykjdREae0KMW9DUTR13VfUF2teQ3AnCElOp40NHTTYFFCN3wivMqp-7RSJmDmVG9tEaGZHdqMAO7XFcMYMEg24S-7pnjT0Cv4ntg32aDRMF2I7qQ64Pnp3LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداحافظی هادی چوپان با علی خامنه‌ای.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/79392" target="_blank">📅 11:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79391">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKqfY9wkviPTLZ9tBG6_pMo5_5WBvc3f6pMjvDvOLGeuzpVxZaV-_lOeBj3Z7GDeR90m6eUkhICkB7E81K0Ib0f1J0CP47QIXoBg6GFG35NIwdYtisA1fsbccoa4n-cOcQQh0k3UMvYryL63n0GduldtefhzLplWlE1fYSXRXYvjSGrlBEHAxDKOTQFv5Zyr5ZcDWhJhtp8qs-jIOfYaFzqB17QO3NYxKhW2DQEEd52uQg3X6NzTFCEqm4CmH8IiEchQEC2SF-0uKhvoN_BsDIbILPV0ir7kUBE_w6zzrwfBK3vh_2Oep81-HWUPqMlM12RzcOtV7HiBv-gGwqKPWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
گل یا پوچ، حالا به‌صورت زنده در بت‌فوروارد
💥
⏩
یکی از محبوب‌ترین بازی‌های سنتی، اکنون در کازینوی زنده بت‌فوروارد در دسترس شماست. اگر به هیجان این بازی علاقه‌مند هستید، حالا می‌توانید آن را به‌صورت آنلاین و در بت‌فوروارد تجربه کنید.
• با حضور اوستاهای فارسی‌زبان
• محیط کاملا آنلاین و تعاملی
• تجربه‌ای شفاف و هیجان‌انگیز
📲
برای ورود به بازی، از بخش «کازینوی زنده» در بت‌فوروارد، گل یا پوچ را انتخاب کنید.
🎯
همین حالا وارد بت‌فوروارد شوید و هیجان واقعی گل یا پوچ را در یک رقابت آنلاین تجربه کنید.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🅰
r14
💻
@BetForward</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/79391" target="_blank">📅 11:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79390">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8i_W3crV-mJiF3FuGuk-oOUe9sQgh4nBomJfIHx8NntfF_BtKLLr2q1A0OCmG8O2SEeyHWZ74GD92CHgJjPREq_vqjiyMm7PPiZ5BoZC3ERddpNn6m8RU1gcD7ScFCqbo_Iz0TsvB8Zi1IBRxIqb7Jr3JrjEw_CcfEM4sx5sT_NoLpywiZMLUiyC_nahsJt-XdoCn9Vpex5cHe70w8o5Mm1pJzIRYN4wVJYlnEQgIGEDK_aUCBelo3dtz3Za6bbjoiVYh9WuHAbK0mCVlBHtijvBIq0f6R848pOWCEVhXCW2FweM9Sg8iWrXQm57Ou71XQiLY6d5bpLqSn6JlZgEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینستا هم داره بامزه میشه ها
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/79390" target="_blank">📅 10:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79389">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">چی میگههههههه این
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/79389" target="_blank">📅 10:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79388">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">به جون خودم داور رو صفر کارت پاراگوئه بت زده بود</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/79388" target="_blank">📅 02:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79384">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Llwv2rr904e13hRmnlj9K6sRf6KUKO2ClEUFH5AM0SLjuqxFDCBm2cgUDe_B-pCcK-L7gjMtwNicX3Rqyo0DFOkb_-ZGV5cWVL9ikdMgtfgDNixIF4u0cL7Tyg02XraoHPMFmUnG0YFKp5msPWZY1sBWCEIy5QAjZk-s9TrUEFml1TUZgBPZjO1oGNiqHGDxtJkuOkHC_5FW8u2yFnZYDPaF-o6J6w-mKvOGfn-5i_6K_93vY6WiQP1G4sp7kIZ2BFDf478bIcRKIPpaGrkEbFvMLBxYU9kAQUZj9FXC_OqUFJAXxZduxUeuo-XTvh4Tp5nlzPaear1bJawEDsRWZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببخشید دوستان یاد مانی هیست افتادم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/79384" target="_blank">📅 00:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79383">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_XKumpKWKymQg95-XEv67_UR76MY0NuZO9-bxFzhunwSKkHpT5AgfQ9iboYUOwecxXqbU8diOu85LtRHSh_3ltNLN8xKgaOsV7jJm6R0dFaRk9YgZG1aE14Fses9sc9vJZwEj4xuzyNTYNYjaB27MDbcxQTFBypKd6VLxkXk_W4uPlzlbndaQF6XBv5_RNtrz1-cWzKpwmzL8zd6sVRsUDlWH28XW7SJsTKGxajERCY5FiYGwHikHE_i-FGtBP6TyS7IxazbfHodgqC-Mcz31m6A2Q2pegCYS9AHfiUaoe4ZQ1xzY1GXC2a_puX7It5xGBDtUAVy0mZcK1AcebQJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رپر ایرانی قبل از یه آهنگی که قراره نهایت دو ماه تو ماشین ملت پلی شه و بعدش به خاطرات بپیونده:
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/79383" target="_blank">📅 23:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79382">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEJtgp9eH47rNPlXkSMGddZqqliyuewiS-ydePnVGFKRkXno64sp95CLlq5gOKTuKpHRM4Vy2N3yz29BC2VEiEKIYYkVqR1E1KNZBEsAQGNexjt_gxAYSmOoQzEYulnfRCZxTP8EsQVeCe4nvhigNmuOoRpRK5locNFLYOepDLOdg1fj72d6OFg9_fRR1jAp8YgDMpEhB0-n1lm_jX6P4Q3vampQU35rp0wkTxY2IbG_WermrAbDxt_MbIAkghCyKxx5g90XhNmoBhdQCiMVNSx5O_6hgzxc7Gm06nxjNkWRyUGA2qJfo1rMhIPtgvx42V-5o9MSOFtcear4riUjaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جور و بیداد کند عمر جوانان کوتاه
ای بزرگان وطن بهر خدا داد کنید
گر شد از جور شما خانهٔ موری ویران
خانهٔ خویش محال‌است که آباد کنید</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/79382" target="_blank">📅 23:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79381">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0fc835849.mp4?token=jubipaHaqvuzmcnrS5OmUw1-pNnEsUh8rXztgm_li8lKqxPiDBYWW17sX3nsSS3eCvITT1ufcVG-RSxyLMacqKqfQ5zL3HoRC36WvFOdIDoO4Sr1N3p12BKfDq0giaf4qzg18eBCabhl8x8Z-vbYObKJ60J3zKKV24Xf_eivhGbQtNSjJCygP4CGYdLjv4ZPwU7FEFA7RCBYCnc5YmhB1Fkyilg03qSOG1OvQKKU1onph96QN2ihrrcGku2JwvErTqi-qr_9bEMtZMhJQRCoeeJqf8H2VWgPndcxA1c_rk09zIoDk1zSl3K9x9h8tZO96OwqdAJCYDkqES-vBFUsrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0fc835849.mp4?token=jubipaHaqvuzmcnrS5OmUw1-pNnEsUh8rXztgm_li8lKqxPiDBYWW17sX3nsSS3eCvITT1ufcVG-RSxyLMacqKqfQ5zL3HoRC36WvFOdIDoO4Sr1N3p12BKfDq0giaf4qzg18eBCabhl8x8Z-vbYObKJ60J3zKKV24Xf_eivhGbQtNSjJCygP4CGYdLjv4ZPwU7FEFA7RCBYCnc5YmhB1Fkyilg03qSOG1OvQKKU1onph96QN2ihrrcGku2JwvErTqi-qr_9bEMtZMhJQRCoeeJqf8H2VWgPndcxA1c_rk09zIoDk1zSl3K9x9h8tZO96OwqdAJCYDkqES-vBFUsrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/79381" target="_blank">📅 22:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79380">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کانادا پاره شد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79380" target="_blank">📅 22:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79379">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">مراکش با امید گل ۰.۰۹ جلوعه</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/79379" target="_blank">📅 22:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79378">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">یه گل فوق العاده زد مراکش
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/79378" target="_blank">📅 21:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79377">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvIdJfLV0xYrAQkIZFmmLgtSfE4xLwGEe2uO4NHqp8pnNyiXjPDFBDOr-UY0zxB7Gt1dvkXdpHwoZVVLnsWHOqrk6wDcG-gkSzV9olpJzFvCYEGjN_QPQ-4FoZxy08QzljNIs2YhOdHKcZhkIX6Bg9Dcv_V9GNiE0FD16L6j3p9LXGlc137ZURTesZQbLse2DC8gy6A6zN61cy6KkJUnpNaTL8KsEy0fK4oBwVfKNAyRK45Sfnv84GqOFdca-JTwR2ZYaSil-lk6dKQ6c0xL9OSE_NWo1T55hD8nZWaU0-CUDoZV5Ml5Cd8cY7yYlZCzr8di81r22V_rpEQCzts0xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امثال توماج عادت دارند دستی که برای کمک به سمتشون دراز شده رو گاز بگیرند
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/79377" target="_blank">📅 20:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79376">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rz0YP7Bag1sh9fM8oLRj28v8JlcutqWPksvCRzv7izrJEx91hw-vQ2vsdDxdJ0G_GzsDb4QX7uR5n112ezChCq_T4Ew2t-fzvz0z2oVGVWENuGwXGkXiMFwm5KibV05Q-ICC8QPSQ3LV51P3oo6TzKQOMU8GdCkL9oPOhuM8cuDlnxdZbT8KQrS9NgcAARDy5eJedgalnDkcgydXqjFo1w5XRmNB5GRtW5bS7SCGqUpOwZckgn4G7O_XOVi5LU0kw_juK7ezNKWchEzTB1G8hqPjWdqzp7v298mWN_BXuk0sCNoOmPGt8Qaddux2yf-lS6h-4LEWoPMxbCykPKQJyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79376" target="_blank">📅 20:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79374">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTORNADO Ping</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rSUjv2qTQrTNLd7gkEnnSPJRaBodckZ-lRGb5sIiAzYPrPY6QK1LkaqVGTgzSVmoCCwAUg4TFfTZ9H_EqjaJkFey71PLEVUUqAD9V_BrsCZy1MTWh7rYtSMbFvcO936YCQ2kw9sWNz12yKq9fLn3drfBae2HnXZa9MXDRrv9reZLvdPrwqJtm0Cy2LQZ5b51WimoLeJ5JeH1auzIJv0xJmXKAyFfell6J_g-1gGoLYmf9mXLVlXVDwg3OCJMlBrx8ExNDpbUPGktgaNLZJ6WiyvGmJG0wa9Bl7ILovaalfwRa_02thhJhwR8iCBiXlK053bW0QSz-D1FANXBsJPU-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تخفیف ویژه زیر قیمت کل تلگرام!
⭕️
سرور "تانل شده" با بالاترین کیفیت!
تخفیفای ویژمون رو تمدید کردیم!
🧃
قیمت هر گیگ فقط 2,500 تومان!
😈
( مهلت خرید تا پایان امشب! )
💥
✅
بدون ضریب و بدون محدودیت کاربر
✅
دارای لینک ساب برای مدیریت حجم
🛡
تمامی سرور ها دارای پشتیبانی می‌باشند.
🤩
@TornadoAdmin
| خرید
🤩
@Tornado_Ping
| فروشگاه</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/funhiphop/79374" target="_blank">📅 20:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79373">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkCQF5kaH2CIZpWUJ1DkEVuZq8iI-QzbcuNhbQ_H796OHkqAaMAehLRwN397l_OLVD4RC_YSpWGYqpy8GVGl8awIOpkibWGCKfgEBIv_-QQH8ZY6XyiVae2D5OnTmlkPVcKXKutUBVYVZW7s5krW22_tA7h_Vjvan9o5lCxjnf3dwW3Ex0B-JrpQMnjIpCVRKj0FrH9Y_lSeFzhMB7VQcoPatQL8Gv0QerBRJBx9libCKgcAKpBAtjOS2jVWxEP7yMcnWyPOoX_2aGsYvUL7o-fLIwvMWwWhiz5lVOvlhJ_2Csx-Nj9pXZjBONK_qFTcqxzCKeDXUosTn5hmiivFQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متین بامرام.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/79373" target="_blank">📅 19:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79372">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWK5yFnEtcEdkXWesDDA3FHiKefsL75ATXz8PlyH3mMwtElmN1CDTx3ZnZ4Yd9SdoRGP1OX2hsaZfvGs8MA62ZQG5MfmhLb6z4GuFu78T0bRcK84ZnBg-39aMI89ZRliKr9pZQonmT74MMNz5eITXZsOBZYCexi_STV5I3imFxIqn_R6S5RclMsPiPRdo8zdVkH_XvfMYXWOwprMwXLHCXnJQuFOnSw67J7vzpbK-tV_f-kyJKyszcjOYMYB2uMLRRJSA106CpqMqLlrh-sttG8ZzN4ENjpom3wcWMGeTVNRjzLwL-pzVcT29Pdh6UWUUlgQ6O6ga4DMn7BnUSSLzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت جدید رضا پهلوی:
به نمایندگان خارجی حاضر در تهران که برای سوگواری بر سر دیکتاتور درگذشته ایران، علی خامنه‌ای، گرد هم آمده‌اید: ایران در حال سوگواری برای او نیست.
ایران برای بیش از ۴۰ هزار پسر و دختر که در تاریخ‌های ۸ و ۹ ژانویه توسط خامنه‌ای، قالیباف و ماشین سرکوب آن‌ها به قتل رسیدند، در سوگ است.
این رژیم، مقادیر هنگفتی از ثروت مردم ایران را صرف برگزاری این نمایش تبلیغاتی می‌کند، در حالی که هیچ یک از رهبران دموکرات در آن حضور نداشتند.
آنچه امروز می‌بینید، ملتی نیست که برای حاکم خود در غم و اندوه است. این ملتی است که پر از خشم عادلانه‌ای است، و این خشم و شجاعت قهرمانانه، بقایای این رژیم جنایتکار را سرنگون خواهد کرد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/79372" target="_blank">📅 18:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79369">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1wyNvqu5hpBiSokxk6Rfdk8DRZIzKYMcFkPVcJaSI0BYLE8_0znbXnIReITyBwepzutFGR5zYH4IqjNg6fmjgWYdRTm2nCPgoBIge-3ZBUywCPNJm_7W2YVJnTEqWaE4E9CGFJRVk54PQxxVa_l_ybYoRTlS7_gmsII7akT3-U2qRe7jRYg5QUnqirXCWdkbtEJIArD2Ges1wz88zfm5eywm4CmSSIqWspKnT2mEiAPzzbaUk7mGVbXTptfvYE0qMnQMZ47gD-AcZ6ykS_nb7KBQtkW5dQsoXapyM22sLasFPgcQzjt-MCiYvhICK20YXA1az0gxsVhgwrGWjdeTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی اونقدرا که جَو می‌دن باهوش و فهمیده نیست واقعا.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/79369" target="_blank">📅 18:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79368">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">الان تو مراسم یهو یه پرده بزرگ و ضخیم اومد جلوی تابوت حضرت آقا، ما شروع به اعتراض کردیم که این چه وضعشه چرا تابوت رو از ما پنهان می‌کنید؟
💔
💔
💔
که مجری برامون توضیح داد به دلیل تابش آفتاب و وضعیت خیلی خاص پیکر حضرت آقا، مجبوریم فقط چند دقیقه تابوت رو به نمایش بذاریم و دوباره شب ساعت ۸ پرده‌ها کنار می‌رن تا دوباره بتونید جلوه‌ی نورانی این تابوت‌ها رو ببینید.
ما هم نگرانیمون برطرف شد و آروم شدیم:)))
🫠
🫠
🫠
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/79368" target="_blank">📅 17:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79367">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">العربیه الحدث:
دور جدید مذاکرات ایران و آمریکا ۲۰ تیر (یک روز بعد از تدفین رهبر شهیدمان
💔
) بین ویتکاف و کوشنر و باقرشاه و پروفسور عراقچی برگزار خواهد شد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/79367" target="_blank">📅 17:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79366">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سلام ببخشید من تازه آنلاین شدم  می‌خواستم بدونم خدایی نکرده اتفاقی افتاده این عزیزان اینجوری ناراحت شدن؟  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/79366" target="_blank">📅 17:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79365">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c8f58be43.mp4?token=p9sz_U6qCkPywIUfVQ_ZPt95Ei4Hx4UOadtA0xDYaFLIKZshVGIkZ951yvbA31WSIA6bhmjPDFkqgJ6fLDrvphRBfVwdjcB3eeVYxoWrOfHIxc2Cx6a3FWmvM7hB6KP6Yd2kHxAApg25YTKZa2XUatLbmCcdU4LnRhlfmDCkSX9M_plPd7da6052ZnakXxmwE13AUgQbr0FmabLxQuSlWKdLpKU6Gf2R21RftCNjCAvW6RfWZHkbqhri0fCkAoXchBhCn6mgVU9PxarZdA2Foq5A3hfw_jDBAo_Fp8a9gvv53oJG80dMAF307AYFdqu6ZDKf-3giLBzL9EEzF5w30Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c8f58be43.mp4?token=p9sz_U6qCkPywIUfVQ_ZPt95Ei4Hx4UOadtA0xDYaFLIKZshVGIkZ951yvbA31WSIA6bhmjPDFkqgJ6fLDrvphRBfVwdjcB3eeVYxoWrOfHIxc2Cx6a3FWmvM7hB6KP6Yd2kHxAApg25YTKZa2XUatLbmCcdU4LnRhlfmDCkSX9M_plPd7da6052ZnakXxmwE13AUgQbr0FmabLxQuSlWKdLpKU6Gf2R21RftCNjCAvW6RfWZHkbqhri0fCkAoXchBhCn6mgVU9PxarZdA2Foq5A3hfw_jDBAo_Fp8a9gvv53oJG80dMAF307AYFdqu6ZDKf-3giLBzL9EEzF5w30Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام ببخشید من تازه آنلاین شدم
می‌خواستم بدونم خدایی نکرده اتفاقی افتاده این عزیزان اینجوری ناراحت شدن؟
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79365" target="_blank">📅 16:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79364">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">خبر اختصاصی ایران اینترنشنال: مسعود پزشکیان استعفا داد  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/79364" target="_blank">📅 15:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79363">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4F0pWfEAE6w-WYxTNhtVOSx79PNTvwd0-cEArpnLFxjp5iEXFzJ-4EytVx0AV8WaqWBeTrl7YHopGbN3EI58zP-kZ79cy-CER-5mYkUaj1TyUpfJowIuJLn2kqN-Bh2f4M7N4QRcYcqQOHRzBugMElw242K1807FNmyFhkOSz1SGYUlTdABNDAPcwvhHjpq6YiTPg84-xCiEYeAx-v-jCgpZ9L5AzN0GSC_7GaEus5U6_QGNPQQEadFfAnNzZDqqIso0GNoXXCZe5hrrVQfHFd5Ff7Hg5ZiGRKvjr0_f82WKOWxfQvO_UisYbOjQ4pcY7VsEzi7CHYVnSHQjA7Beg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو جنگ ۴۰ روزه سپاه در ازای هر یدونه موشکی که به اسرائیل می‌زد رندوم ۱۲ تا موشک و پهپاد می‌زد تو کردستان عراق.
بعد الان رئیس اقلیم کردستان برا تشییع اومده ایران و چنین شاهکاری رو خلق کرده.
من هر چی بخوام بگم فحش می‌خورم برا همین صرفا به این بسنده می‌کنم که ببینید ترامپ عجب نابغه‌ی درجه یکیه که به اینا کاملا اعتماد کرد اون همه تجهیزات رو راحت داد دستشون.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79363" target="_blank">📅 15:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79362">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1pUyMncCiqhAIXxe-AR20PmnQgiUIDTUMUvyw5s5CtohvYOgu1azEIoRNDhoVz31r7zzlr7F9Ix9FwiveXlvyHB3EZ2d_-MbYz1cxRX6iyhQKNBD7c5eGxm0b-AU4CqfMv2GMKEiZuoNgvT0fM_lkNd0r9wvzgY3PgjM2SmKSa-Kvpv5sk7tHX7w_kNxDK5I-VM8_JKLhGy4F7iES5GB4Y4TXClvXvETHKfYKV0UrrzjeGXZSDI3V5d_v9hBxcMGMItR42ErEjwReYetSH3A02Uv_uMqboNz0PZ6yn5kDxQa-ecyUTPPJOB1aOFxpwql28Nz1yryCwsWjqZJLUrtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تسلیت به پدیده به کون ها
دریک رو صعود مراکش بت زده، کپشن زده که میخواد از نحس بودنش به نفع کانادا استفاده کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/79362" target="_blank">📅 15:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79361">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">۱۴۱۱ هم دکی پول ویناکو پس میده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/79361" target="_blank">📅 14:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79360">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCpqGvj9hzSMCAxY0K8SYHgCePgYCD1hPN8Dk9fCXJyHB6HufMbkyhKnv141an6Kiu1OIHG6byt1zewmDuDt_XiZ_ZKR0fcbK1RKcxRHRakWDc6JwLIh3Rlu_fzLd3k022xiLD6Y1zSKvoGVONCieoT1g5gFVujqNbk6o-OPpBy8JpTWXsCs9Vdedf9i8vuaQgLrHUKcifwV7QIkv1pyItjVdkT4cD-PTdnZyfW1t8vkIiVE0m7NgRHPuVGU2dXHXkHG0lusVyCPVcXrFDuRIt0be7XT98_9hvVxb0LtTV5QqL3tMHVD-IzeJr9uFp19Vvf_cQtSlYPLxkBw00njTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آره، سال ۱۴۱۰ هم امام زمان ظهور میکنه رضا پهلوی حکومتو تحویل امام زمان میده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/79360" target="_blank">📅 14:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79359">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ByMfJ7a8fTswVyvhpkGLZcaLB4irxAfGxxvFX5DXMdiy5xj5O4WXXEfv_BHYEMrcoPo3FXPAXvm_hMBbRUiigGwuuVrRh7BVaffE9u1aeSfmqYrqtK8FB8LGuVIag7K1bBg2iQvrxd0bclLhwf35kC9TWPeOfy_Y4Ga36jw80cMFHyhKwFbwgMuNfytM7j2CBwKBXyuFuXvdHRZh8DCiKOeCZDq-sZu2AxLf2Ydr_7rxfJot_DwYrwUdQIPhImeOinlazUwOgrCThV-wuGcSZe9eqwW6l34zvkAZNe2MlKgPSCZRy5j3xf5gjrkqPON4FgycrlLJqO94N_WPAbWslA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلش نمی‌زد فکرم هزار جا میرفت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/79359" target="_blank">📅 14:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79357">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">توماج صالحی از امثال شهبازی هم بیناموس تره
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/79357" target="_blank">📅 13:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79355">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eB15x70JslDT-77Y8nusLDDoFfTQMR7Lzsg-h303Da0uqPVEPJPEg-gLForKM1r8zymDVDAUEloK6_pW94jfSN1BRScd5QeUrPhgV_tK84HrMffaudoej7iY2BjLlmQ5ugX_jid8Fw_6vsQH5FOlc1oX7SuF7J6Nwa4RINRoxOLsewVZb6MqUKFmUpVGCHuzlzsaeuVgFah2P4u1OfJKMFSTKZWYuGIvBbgajz6LzTc1I1O2NIIJAR_qRmY8Lep3xCpaaB8kF46afFjmd_tEwT6yYhuaHZswMvvB53SwyRoNGEvOsFUYbWr5gAA7lniTTxwMAg2XFW-4ZUY00ppHrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lrvnkqxyVUUOeA64F9IH-M40-2uCty4NM-1pK9GPNGUSmWt1m0_rXZC0ka_MTa2YTxkaUYd3KHtbT3u2hWBMVRavwi8_pboS4G6pB7pF-GDqgKSJVuT8sakkrVDlWQRYpoLEY4C5Kvh6mESFEcvAxrB84K2MWfksI4rCUa2WmQwRagiaTZXk1nSdGk1AibT6LhgJ1zsR8V9Pdbf9PZhdD_pYgg8zW977azkOrFHK5ND1HaUfMvYM5CgzG3ehZi4D0nYqFD0VHMLRx7closB6EhiwZKIp4W6dU3Ry70UuKIJKaLQDUiZ84cyKrn25Wd2wdisIf_U3PSWjCr9a1bdHJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تو ژاپن کاملا قانونیه که خودخواسته کاملا ناپدید بشید و یه سری کمپانی وجود داره که بهتون کمک می‌کنه که هر نشونه‌ای که از خودتون و زندگی قبلیتون رو‌ پاک کنید و با هویت جدید زندگی کنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79355" target="_blank">📅 12:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79354">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">کصشعر نگید پاشید بیایید چنل آنالیزم میخوام پولاتونو بگا بدم:  https://t.me/TemSahbet</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/79354" target="_blank">📅 12:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79353">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">کصشعر نگید پاشید بیایید چنل آنالیزم میخوام پولاتونو بگا بدم:
https://t.me/TemSahbet</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/79353" target="_blank">📅 12:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79350">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">مسی چندسال جوون تر بود چه رقابتی میشد رقابت امباپه و مسی</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/79350" target="_blank">📅 12:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79349">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ما نخواییم کشورمون ۴ فصل باشه کیو باید ببینیم
پختیم بابا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/79349" target="_blank">📅 12:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79348">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کی قراره قبول کنید از وقتی تیما ایتالیایی افت کردن کیر رفت تو فوتبال
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79348" target="_blank">📅 11:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79347">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGoApX2EIxC2QvCXY5V5sQmPzU97YoYq2G-5kLBZiKRtAO7BPCSAv9MMJPSayWEvF0KSpdCj2wGxifOxwXGZIoDiIWEbaYmW_KqD4CHvIr5C6VSXqjz9lC7dphxZpb8WifmL_OzhfP4_HuwK0-_a1SZ20FrR-rMDzkplc5hzZ5TdnQMtupQXkSeHdOhFU80BE5OR_95D3Wn4vNl2RcDQfVe72A4LALTJRBPaiZrt_JijfLY3RjGQ-y0jPuAMUlrB7SVuJPL2T9sBOUL7SQnHCbuiKcktDd0pOcTIxFdLJFwzOQ8PkGIwmpAlJk3mNXZak28M3Xffese3fOW3WBkesg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب بازی مصر و استرالیا خیلی عجیب بود، یهو استرالیا برا پنالتی گلرشو تعویض کرد، گفتم دیگه هیچی سوپرایزم نمیکنه که چشمم خورد به بازیکنا مصر که داشتن قبل پنالتی هایلایت بازیا رئالو میدیدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/79347" target="_blank">📅 11:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79344">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZEMrY_nRTiIg7qrosOBJmuLKH9mQreatIrVmzqYRRcoqL-SqBfHNBCf7ejUulGxNO79L_2-t0O7qaigMUS6M0FKAtkJWm4Ts2-gwOhmgbVI7ZNhgHYS5q2GTbMBH8l9pNEBiB-idzV3Z14tso17D0G5F-d7mKWfNSDtVZR_ILWmVJrdybRZVRJPstXCgw7ZnIwk_op5u0zcO5MTIIAz0ZCg73kok6XS7M0343JAcsiM05pYCuE8okr1dJKTX7h_nSzGir3NRfGXjXXuXIDUreDXU14LWno5yqVsPSOYfSwauba15UI8rn6XObhed-6IceRs8VkeNlCVY4ykJ6ZFTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببین حرامز
هم آرژانتین برد و صعود کرد، هم مسی گل زد و هم تیم کشورت یعنی غنا باخت و حذف شد و این یعنی به فاصله چند ساعت سه تا کیر خیلی گنده خوردی.
به نظرم الان وقتشه بری صورتت رو بشوری و یه عنوان آخرین جادوت سعی کنی یه وردی چیزی بخونی که مردم جایی تو خیابون دیدنت فقط یه دور به قیافه‌ت بخندن و دیگه دلقک بازیات و کیر شدنات یادشون نباشه که یه دور دیگه به اونا هم بخندن.
موفق باشی
❤️
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/79344" target="_blank">📅 08:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79343">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af167dceef.mp4?token=ulJbpVBVtKQXGAhyHGT6yTMTt1m9BeVb4Caxs_O48lFiDNhjtZdDoA2FWvph9TGceAX-nh_GpcYxJTX51ljorCyhYBkzm3OfJwTJMUWBrufQf3tK01gZcQTLSriZH-FwAYLsoWTW-UY86tRLJHUTJ5icWz5jki0xLhv6NseXQVJw94KWWiCv5NGFKkXv5X8nimP0UUzdo3fvZsFxEbfd47tl5sMQL6OcD2K2XW8sKWrGe2wMjeNWtd8_avtTkSrhPjH7xnXVII5yy3Dl_bxkC5SgV6LOoAGOeTe74PpNQ7aJ6PKaPyNk0viMkMEfJC2MMIw0UITWKaAUN_IE3xRWWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af167dceef.mp4?token=ulJbpVBVtKQXGAhyHGT6yTMTt1m9BeVb4Caxs_O48lFiDNhjtZdDoA2FWvph9TGceAX-nh_GpcYxJTX51ljorCyhYBkzm3OfJwTJMUWBrufQf3tK01gZcQTLSriZH-FwAYLsoWTW-UY86tRLJHUTJ5icWz5jki0xLhv6NseXQVJw94KWWiCv5NGFKkXv5X8nimP0UUzdo3fvZsFxEbfd47tl5sMQL6OcD2K2XW8sKWrGe2wMjeNWtd8_avtTkSrhPjH7xnXVII5yy3Dl_bxkC5SgV6LOoAGOeTe74PpNQ7aJ6PKaPyNk0viMkMEfJC2MMIw0UITWKaAUN_IE3xRWWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام صبح زیباتون بخیر. 2
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79343" target="_blank">📅 07:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79342">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پروردگار بی همتای فوتبال، حضرت لیونل مسی بهترین بازیکن زمین شد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79342" target="_blank">📅 04:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79341">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171cc02113.mp4?token=RLi41D4c9BjHX7-s1fuyADAy7GbMFiBs0yczo1IMIv5ZFAbacnE7flVfrLKyVlf6faZL38M12d1PnVrBa0I_VGjWo1X6GIb64xYLHzRiZLP3KPtaB-4ZGP8164a-GhATuaz5nk2iHPGHyyF7_Lfa-4DFGhwxgCmEyuJIdwcxcEdq35UMuhFtwEgQvZP-AwZfyal_7agM09lQFyn-CKG-XDw3bQpXszpMZmVnNvS6dnne4AbDUNiuvc7rfIbxhpo9xNmshPD3YDoNRFISEsOHjTB3MdrZ6aUXtGfY07UD7fDvmzXyONFL4_BNlS69dJqoFgHqOMeeYFIeu-WvqA-neQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171cc02113.mp4?token=RLi41D4c9BjHX7-s1fuyADAy7GbMFiBs0yczo1IMIv5ZFAbacnE7flVfrLKyVlf6faZL38M12d1PnVrBa0I_VGjWo1X6GIb64xYLHzRiZLP3KPtaB-4ZGP8164a-GhATuaz5nk2iHPGHyyF7_Lfa-4DFGhwxgCmEyuJIdwcxcEdq35UMuhFtwEgQvZP-AwZfyal_7agM09lQFyn-CKG-XDw3bQpXszpMZmVnNvS6dnne4AbDUNiuvc7rfIbxhpo9xNmshPD3YDoNRFISEsOHjTB3MdrZ6aUXtGfY07UD7fDvmzXyONFL4_BNlS69dJqoFgHqOMeeYFIeu-WvqA-neQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جادگر کصکش من الان اینو چیکار کنم؟
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/79341" target="_blank">📅 04:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79340">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">تمام ارژانتین صعود کرد</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/79340" target="_blank">📅 04:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79330">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">جادوگر بیناموس چیشد پس</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/79330" target="_blank">📅 04:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79329">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گللل سوم هم میزنه آرژانتین
و پاس گل توسط پروردگار بی بدیل فوتبال جهان
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79329" target="_blank">📅 04:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79326">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سیمئونه لاشی از تو تماشاگرا بلند شو بیا بشین رو نیمکت
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/79326" target="_blank">📅 03:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79325">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ایفانتینو کونی کجایی پس، داریم حذف میشیم کصکش</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/79325" target="_blank">📅 03:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79324">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">این جام جهانی خیلی شبیه ۲۰۱۸ عه
عملا یک مدعی وجود داره همونم فرانسس
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/79324" target="_blank">📅 03:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79313">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">نیمه اول با درخشش پروردگار فوتبال جهان به پایان رسید
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79313" target="_blank">📅 02:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79312">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">کاش‌ میتونستم از عمر خودم کم کنم و به عمر فوتبالی حضرت لیونل مسی اضافه کنم
ولی افسوس که نمیشه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79312" target="_blank">📅 02:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79311">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">الله اکبر ازین عظمتی که پروردگار بی بدیل فوتبال جهان داره
ترجیح میدم برم وضو بگیرم تا بیشتر از دیدن بازی لیونل مسی ثواب کنم
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79311" target="_blank">📅 02:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79310">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">فرید بیا بمال</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79310" target="_blank">📅 01:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79309">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">شاهد حرکات بیرانوندی از گلر کیپ ورد هستیم
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79309" target="_blank">📅 01:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79308">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">خداوند و نویسنده تاریخ فوتبال نزدیک بود بزنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79308" target="_blank">📅 01:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79307">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خدایا شکرت که یک شب دیگه زنده موندم تا دوباره شاهد بازی پروردگار بی همتای فوتبال باشم   @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/79307" target="_blank">📅 01:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79306">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">خدایا شکرت که یک شب دیگه زنده موندم تا دوباره شاهد بازی پروردگار بی همتای فوتبال باشم
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/79306" target="_blank">📅 01:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79305">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بازی جذاب قهرمان بر حق و تنها تیم بدون باخت جام جهانی با آرژانتین شروع شد.
به امید درخشش جادوگر غنایی
❤️
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79305" target="_blank">📅 01:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79304">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پادشاه باقر امروز یه جوری تو مراسم خامنه‌ای گریه کرد و خودشو زد که انگار این منم که قاتل حضرت آقا هر شب از طریق واسطه پاکستانی بهم پیام می‌ده ?slm chi tanete
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/79304" target="_blank">📅 01:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79303">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">توماج صالحی رپر خوب مملکتمون تو رتبه بندی جهانی مادرجنده ها قرار گرفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/79303" target="_blank">📅 00:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79301">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">استرالیا با حذف مصر رفت به یک هشتم جام جهانی، حریفش برنده بازی ایران ایتالیاست که فردا ساعت سه و نیم صبح مشخص میشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/79301" target="_blank">📅 00:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79298">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">گزارشگر مادرجنده اسپویل نکن</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/79298" target="_blank">📅 00:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79296">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uF8kBYKO-_sJaOsfMOvXgsev9GycOdayN5w9v-J-ZVj9ACqleVV4PDq_6uLzVET_51R-QtUHzvslAEyVgoDOfHwro2R_1IPUEbYFb1EuwsfE7Gg2Gu00kPdtsjlEaF-W0dTWh7pW_l_XO8RJRBRZIuaAB81F3NDkNPluq9gHnhemquR-vDM-vMHMo_cJi9-syb8S-T_szOyJ-S5-oTTXj4utX1xC494ZH7tigaCNRB7OaBTIOMMlSXHi91hfxE1Yx0zSlSpldMe8IWI35fNa2sYvNyocxKpNo-csGmlew2B7Z1fRGwrnvVA7mraNg9nGzDRqbEoJyOpQ30Jdqmd79A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت عجیب اسرائیل به فارسی درمورد مراسم تشییع:
بسیاری از افراد (ما) هم می‌آیند، نه برای سوگواری، بلکه برای اینکه مطمئن شوند او واقعاً فوت کرده است.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/79296" target="_blank">📅 23:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79295">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jj-Agz833D0KnyhM79iZbXQO1Q1HIJ886Iuqqos6bHrU_ScLT_TEn2M402AwRktkHhmnlx7GkNbSAevF-wAEUY53cp-xGgByWAz9H2kI1selgekP4ir2miT8LHhsslt_xDnGe23CsJ2njF0GVHa4cD7-Z1up2r7dC3V4gzUMQ6BTmfjpGoGV_rUf0sn0NOWgnzj6odHDnKgBSo5dTNdlinHwUL3MDT7Vuz4LLvR0i1nVBf6naZf9Oy4vmyygf844nCwFKqe4MgNW6mbw7Nbg1J9NQHyYYB_Ssq-0QU70iJDG-jgVpMde5Z4HQdsMyWdm8c3LDG-NEq-cX-7lqQ3glA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باقرشاه قالیباف:
ترامپ که کشورش ۴۰ و خورده‌ای میلیون نفر گرسنه و نیازمند کمک غذایی داره حق نداره به ما بگه گرسنه و برامون دل بسوزونه.
پولای بلوکه شده هم مال خودمونه هر جور دلمون بخواد خرج می‌کنیم، آمریکایی‌ها بهتره به فکر آمار سوء تغذیه و گرسنگی تو کشور خودشون باشن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/79295" target="_blank">📅 22:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79294">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">فصل جدید سریال سایلو راجب جمهوری اسلامیه و دلیل بگا رفتن دنیا رو جمهوری اسلامی نشون میدن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79294" target="_blank">📅 22:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79293">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">فصل جدید سریال سایلو راجب جمهوری اسلامیه و دلیل بگا رفتن دنیا رو جمهوری اسلامی نشون میدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/79293" target="_blank">📅 22:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79292">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">تنها کشوری هستیم که توش
هم مرد ستیز هست
هم زن ستیز هست
هم به پسر تجاوز میشه
هم به دختر تجاوز میشه
هم به خر تجاوز میشه
هم ترنسا رو کتک میزنن هم ترنسا رو میکنن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/79292" target="_blank">📅 22:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79291">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k1_VmK4faM_7xSJ2UsI7AGStDLi_lHImPrdksiTLD_M0qB4KjnikimOD50EGdoor92YTB2mb-KDQvn3tWbtGBtCbLkeb_7L3yofaK1gH0-5SMxkYRtfrNNFAOmRF0dbxRIM-Hbc4tCB7_UZ8-fSD7OcAha_apd5Pg6fV-IhuyfuUw_QJKz8C1pIUhXhfLcrLAlsnSbGNbrvrLIuUMbSXn7GUlwA0q0h2aVeQlkj_7SBMS0q1bHAwxoKF_7DPnoyqRlg-jE-SKYYm0Oi_UwZg848lBpOufDsNUORbFfwm8pYxVghVfQzZntoF3T2NY52oPG4Hu37ojGw0kP6DOm-n2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جادوگر غنایی چرا یه جادو نمینویسه یه دکتر زیبایی بیاد صورتشو عمل کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79291" target="_blank">📅 21:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79290">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAlO9RoCfmQSfTApSle6yEr_jVSMhaho6EpUNGD4aeuvDuaXEnUobKO5knerWzXnra3ki-tHwSWQZxSywtyut7cJ7nOaJ2scnDL0g1tMEFBSvB4zU84Z8-wtp35rlm96pTnECg9sW-2hj6_2vtxFrnnQ_amyB6ZhgwxiksGd0rowxNgVJ1rZ9KlUhSTN-NkMxTzto783V3ly9nzKLAnZvIc9YMqQnl95R5q6XFP0H7ceOCa5qLRQol1XDZpGGbPtIsqDd_d9rD0fYG86ONWWGnztINGsYnQbwSiPvLyHC43x4JFMZ_lMagaqOMLJarteOfjQ3peLGtDZ8RMc--Rpeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این کی رفت
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/79290" target="_blank">📅 21:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79289">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">چندتا سریال تاریخی بگید ببینم بلدید</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79289" target="_blank">📅 21:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79288">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">با اعلام رسمی فیفا، علیرضا فغانی به عنوان داور بازی انگلیس و مکزیک انتخاب شد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79288" target="_blank">📅 20:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79287">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YISR7pumlNsgJ_lVxZ-am8vSbdtBbJq7DicBjr1Du__31fDd74mwY7z-LDIwzTEDUrXU0QDyOSSk3Ibqf6pbgxf8SdmOG7z1Od2uIKnsmGrAtnz0QxYvdD8ULCcErc4Tqv0TWFjbnW8xflJDMffyFY9tHF-tfDf9RnW_IKZs0GuC-uiW-gdVZ6G6RPSdv9MRxkLcL-wY0j1czqynkWpl117KzcPfX3ykImvzZaNaeZzRt0f10kInodM1BexFgC4vSJ0d7Jzm7f94Bi30uAK_hL3YjMQnKzp0JH6JAK3Vn9Ibdr3mChUL7I5SkoBf8o8dO83W6CelVjyl3mAFPSt8Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو نگاه عباس یه خوارتو گاییدم عجیبی دیده میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/79287" target="_blank">📅 20:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79286">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">یکی از عجیب ترین چیزایی که تو ترکیه دیدم این بود که تو کلاس دانشگاه نشسته بودیم یهو یکی از دخترا با دستش نماد گرگ رو نشون داد و کل ترکا شروع کردن به زوزه کشیدن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79286" target="_blank">📅 20:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79285">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDQt9IYpHbYfg7O1johM_I4ucqxa_GKoaLEKUr-uZuFSXfk9E84zEl_UgT1rl_W1ulWn7HwHp51iGzuiEc9JNpB00-wr4p-hIdzA7nc0n57pdr5hXC64Ps9V9JfpDw3hjJYDv_bAFcrwta5HwN3zCTWxx3sxF0sv6Vw5qYA9JBrtufZseIVd7iX9p2q5t3yKaiCJo5Oq0rV0j8hMgqEQXRSslQ6xj6CrBkrvFDdo-R_CHuwAxPzSAJyww9daIP5mlaTAhywyKPa4MnhyL9VO2ifxFE-jI4xjlN5A9QMmzOIJ9biNkdD0JBEjfNHiF8E8HtoG30f8oBurd9qB0TEUkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ژنرال مرحله بعدی با چه تیمی بازی داره؟
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79285" target="_blank">📅 19:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79283">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7B3fI4_Nm3yMHnrSgHPsb-O8JLs5sD9fJVf24v975mY0ArorO2fYUB2FZAsheF26zze4MPokZXAvY8IifKPkg7-nL34btT6_w3ff5ky0NPsnjQaUAEjF4RAwGZEgYaKcQwkltrysmXytjIOj527pGx9hY5dOpIamesMVVEUex6kpiHE_PvSisr1tpQWOY-FCiS_75-BRnctORAL3q7Hfjci7eQpm0LZQVREPoMXdWJB7i_orgUrZihtN7ibZkqe7fCU_ALYWquwXhlBNve7MCOahMDd2D1Xb72i6WOu5VqdHZOEcwA7bUmX0gzf6SImoWT1RAE61evIt9NG1NmEfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😭
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79283" target="_blank">📅 18:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79282">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_nJoqwBqQJVDuhY5fdMBHN6LUiKLKd0S8Nuj-VLUYuoEvKiLUvQg-hwEbQO-LZoE24koWFb_NTqFUuPxL-Bwfb0edqGkAiV8gp8CKoeddcPZwLsp8bVDwV4W2rczoyfX1TwhcQel16ihF7GsFqNS78gb5Hny8EpPVJ15vPhfE8dpv99b7ON2Hk0TYYKoNxDCAQSzSky_gcqBaLMZK76UbxPfpGuTRi6LuHhOegC-IgrW3AeKUdVBl4tGUXpUvtezmHjDnMlMGfE6NDaQLc92oKNMKFjh_tr41NVDAsA10maWuUCsk_2lOj7OZkCWBzTgQp0HMMAMLBohJ8kkJiEnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهر حیدری و ارام طلاق گرفتن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79282" target="_blank">📅 17:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79280">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzpBmbjSntvkKOehhwu7ugcSf1Q6XKquGRBk0JlbEbotYXyAqmIeZAWfitwj5NqbvETqpKgfOLkihnctAYxbNbGUcG8gR8stDAHmSCe9WRv967jvGCbyY3rZDZoPKBmcXPJELQ9UH7cD0FC_ge4rAC_KosQGBYaVveavMUTSNREBeG_YtokfWNGL2BvoRTSNlxP-qG98cRO_owc0YL-Q578l8gX2K5o1iNpYZOr3hZ9cAqWBEvq7bKe2ew2RBSJqBeslPd0Dfaucjry1lAiMPYpcMSHVdY5BWyd3yKOr6z1t8l9DirQ1Sq10K-KIAaINzNYj7Z_Q8j0Rb916ir-BPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه پاشون لیز میخورد میفتادن چی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/79280" target="_blank">📅 17:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79279">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAt4STHezSi2hjdf4GvSnwDKrSgZ7Br4kEFBgOP0gOGigSdOkdEUc4eqxJzMguHb_4Zrm5wrApREiwRYcf_c87MdxKjuJhu8BxKXwgG0DKGbpp4-34j7nXpN9brRpCIOBtZbL9wSEzUxH6TyzgCudXFhKOX_P5G9wEtWGbLGMhGrHXT_imeTRufFKtiL3G4SV-Gt5m9V2jfTD1Ecfu4psPZm_9t9Xan0HB91tzOIPHLUIFswZZRCcIBqDq8197RkvY6CJd8RySdi8OXAlsiKMS3yXgsL0SRpLFrXDVBYg35LtSiP5asVBhbqO2Onw4UKp97VUCTIqX7sYfjtW-kpjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت هیچکس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79279" target="_blank">📅 16:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79278">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4c7250ff.mp4?token=PcyhLcyDbZqpJDsx8x0JZchF2lFUaa_JJly4Grx3cd7NIHyjzjvJRHEDdHFR0_8pRfoXwzj51reKNw1jl16w0jXqPFK1iUrl9zyPKNt-Df6wODkF-s2Mtt9G3L86D9t7p8FDa0VwIyRW_F5bueKKgOosE34mOI-2NEw2dKW1badlXVqCXyvXQ0BCKgEaz3xRvPEk0_5kXo57JV8VGgC4mywcYoLehAWthVuwRW0E72SJ4Yv-YaDVhlVBIV2DolTJBHuwmqaOolIoK1F8btMLNI39qnUFIwsezR0cxwGfmEO9rHuG-2IAeWjq-XWSrGBkuCgsZuX8-kF7x4299QZZtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4c7250ff.mp4?token=PcyhLcyDbZqpJDsx8x0JZchF2lFUaa_JJly4Grx3cd7NIHyjzjvJRHEDdHFR0_8pRfoXwzj51reKNw1jl16w0jXqPFK1iUrl9zyPKNt-Df6wODkF-s2Mtt9G3L86D9t7p8FDa0VwIyRW_F5bueKKgOosE34mOI-2NEw2dKW1badlXVqCXyvXQ0BCKgEaz3xRvPEk0_5kXo57JV8VGgC4mywcYoLehAWthVuwRW0E72SJ4Yv-YaDVhlVBIV2DolTJBHuwmqaOolIoK1F8btMLNI39qnUFIwsezR0cxwGfmEO9rHuG-2IAeWjq-XWSrGBkuCgsZuX8-kF7x4299QZZtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فک کنم دکی پولو زد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/79278" target="_blank">📅 16:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79277">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اینستاگرام مادرجنده من علاقه ای به خداداد افغانی و خیابانی ندارم، دست از سرم بردار
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/79277" target="_blank">📅 15:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79276">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EyI5uO3ArE_XNEZ5_pALyZSYKkQGe7bkY1gNeQtCDOVbJ8v8C7n0jv-nTVlnFXZKJT_1JZiONe_iZUgIga8CWghsB2-syWmBWAj8WxFG85kIg0FWFK9XB6ryaZjoZhTpFLU5kPLywXf5zKP0CuNy8wlrqNKSG2RsdNvRx_OjmgbteP6k_rfolr6HIyueaA-lEz2GfEv1M7V--_DY-xoVoVHOS9s2l5UXvmujo2v_TZ0sW7wlG87mpUwWFygK1KdXtN-Gi4Qd-gpsZAogJXOQHo2aDuR_gA3M-k0xxElyzRWYNitEVJ2FJhBblat1Q1kn_-7uzQZhq3aqyIDktHTOlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقریبا تمام مقامات نظامی و سیاسی امروز تو مراسم بودن به جز اسی کوهن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/79276" target="_blank">📅 15:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79275">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">کاش یه مقدار از پولای بلوکه شده رو اهدا کنیم اروپا کولر بخرن باهاش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/79275" target="_blank">📅 13:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79274">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دیروز میثاقی اسنایدرو دعوت کرده بود، بعد میگفت آره ما سه تا مساوی اوردیم شایسته حذف شدیم، اسنایدر گفت خب کصخل وقتی حذف شدی چه فرقی داره سه تا باخت بیاری یا سه تا مساوی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/79274" target="_blank">📅 13:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79273">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rt2Woae-wpyzH6L8o8H58wRpgBogJUX_pm9SJhep-eQcBzSGl9-Kv1d7y9VxYWzjV3Lv6-2Ga_o6tS6BfPszcbYrrxAvghfyURzrfQMY1qTXqfOz-WFQLmCujZ0nZB6yk1jG0ewZLqiWAvSfo0RNLPBE6vYaHPmUPvh3DKdBTy5Opo4byMcBKF-J_l3mRXxr6tL5NxAiqd4TJl_dmj92Okq7WoH8HE_AI2_v8DpswEKQXL5JTFiz0COZs_bbl3vcT45O18fTU9wdi_P6Lj2yiC2KZGBdU4MK8uLiJDOLdWw2WDJxmpQypl2fM8AmdMaHSRjz-j8T7-TFHIMQf7rIoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سروش سروش ببین چی پیدا کردم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/79273" target="_blank">📅 13:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79272">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">درار از جیبت بیبی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/79272" target="_blank">📅 13:04 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

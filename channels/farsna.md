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
<img src="https://cdn4.telesco.pe/file/CU7MtUBqA8WfQ4-3LvicnP4ROL2aiIcNcLJiUis2zGk2sa7tV4cKjLUjn-EIoTwfg2C79OVibiQ0sWC5m2Xj2e-zOnPauh-oRuMIQgnPsSnkqlXAa4RXNJ5CPlmAKK2MVyzNJeMVTNvSm3HMsScj5HqO_s_zWQdkW4475BPD0MnOCKq3_Zbulju3LYiP9gkrXpc95TFhMpkT9S0Q-7ZZele_r0osN4Xi80fOcExaTS8rMjG1oqEDSPnJ7V2dgGwxpGtsxyqb2FYcqkkpSUWSBZ0tt76SWCfPqqpVQnCzShrTpPbDbRpgA6bY5_0WFUqHyAUxweYTJv9ubbOvWdoWBg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 16:41:52</div>
<hr>

<div class="tg-post" id="msg-444705">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqnZSDSYbzi1DCpc2PiN_CdBy7sPJptrievOOTLOgUECCrS1W0Uc__V8zHItcheYlauuP0lH12tWLKsjY1uALQABj3GtP0Y55XYFYvx5xJwiwIUfuFU6QVymwBheRmOY0d4fIlOVctLLqL_L8n3ES4HImnY68ftqPHRtKWdbiGdpumRGdbpI25uKD75o8yA6huZwIDqleWOq6BRAUibYEvh_86MCCJ7pcfhc8dP3PSv30TFD4b-8_SeIFQwnXhqI0PzOet8mmW9TySADW_TX5FjFuzzJjH0YvTHteCGu86g4zaLOpo-wksZfaCuPxXlK_QPAegFaUMKdYfpK7m8mDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه ایتالیا:‌ از خاک ما برای حمله به ایران استفاده نشد
🔹
آنتونیو تاجانی وزیر امور خارجه ایتالیا عصر امروز با سیدعباس عراقچی وزیر امور خارجه تلفنی گفت‌وگو کرد.
🔹
وزیر خارجه ایتالیا در این گفت‌وگوی تلفنی، اظهارات اخیر دبیرکل ناتو درباره استفاده ایالات متحده از پایگاه‌های نظامی ایتالیا در عملیات نظامی علیه ایران را قاطعانه رد کرد.
🔹
تاجانی همچنین با تأکید بر اینکه هیچ‌گونه استفاده‌ای از پایگاه‌های نظامی این کشور برای حمله به ایران صورت نگرفته و چنین اقدامی نیز در آینده انجام نخواهد شد، تصریح کرد که هواپیماهای آمریکایی برای بمباران ایران از خاک ایتالیا به پرواز درنیامده‌اند و دولت ایتالیا هرگز مجوزی برای انجام چنین عملیاتی صادر نکرده است.
🔹
عراقچی نیز ضمن قدردانی از تماس تلفنی و شفاف‌سازی انجام‌ شده از سوی همتای ایتالیایی خود، بر ضرورت تکذیب صریح و رسمی این اظهارات از سوی دولت ایتالیا تأکید کرد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 690 · <a href="https://t.me/farsna/444705" target="_blank">📅 16:38 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444700">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bqYSXjNFF2xgXMN79xIleCYuyyVKTsRzy2Np1WVTohjNmujS9DvLedqAzUlRbkuN2qoO7twWZIF2jp3bEMXN-HLjy6i_-Id13j09zuZpRGo9CNCT9sknSAxMfu0MgvIc3koE8ni847O4I3r_RYhwF6yVkIPjfOhqRgrUk-fKk95cnrJfAsbV2ur_MXN7nMp_HePeBJ3CTvRHfgggBJjS5MPPk3t-NyiQ1rGQGa2gD_VQ2FZalPfyvAFyBH9myXvew96QIJswJflPgkVIEHZgRtnyXmTNyddw75NaOoN-SKo3w6v6LfhkfttM2W9eogjm8rtVfIeLbUeoB9CNWj5z2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fUij40DVB5PF79xmsK5Ql7S_Cw0Pu7hc4PKuW6zQb8U14E7PqKnbXo9JlXAZg5fLPJL_ZdM7r_RxTfUoHSD9lFD0pqA4KkBmckqhhFn_hbmaSziWRKkoKtr-O7XSDIY1pe2Zvc5uOsIdeP_nx1RpyKVMbS-1wAJ4RLWyPkpAl4ZD9Y_tsbiCWaAMQ-RuurZ5z7OUJnLL6qhoYYfl3x1UcOc_O4eQA3qGRghwlA2XgltyKm4qKfSMf8YxLDx2XzGUa95ZO-K5SwazrPVMLTai8rE8iLoSZyOFGkgDYnLmkjQyb4WYYUCrvxdzgqFtbkXqK2W64u9Vc3fy7esS2Tx-UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vHTSyYYzlO9zLXs-gi2iTLGNiqNR_g8JRbqoHsUY0F16ERhqdOfYofZ5PBEbIR-ofSQCGnISWaPH9VdH0dMqMSeHspn86vQABXVcT6bpe5UXHsAoFQuY5vp_sYikH29gXxX6qwaOj4IX6OByU0WGADgxh216DWTT-7Dqcn0GwR_W9ff0b-JnekrE6cxJ2AFkQ4eJj8D16S9jDpdKdg-Ec9kgtC5gjZCx0eqNda3EtLDhfE3DE6aagz0sa-g1bhVpBRd8J49n7AhwgNJjgKrAZfKgnhGNSzigrdOlcJcSgXWvdbT2eFdnqxP6sPVsoRZVTIiSOXsQUVACQStOBSoCcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p3HffwLmlfL1v1JYQSRMGq66IMElah-tmCQiUPNUM50i_mZe1kK_-79TE38X4kIG2EJHfWnCKNTgdS6bjNrRik6MJzbCojCg0d7N57FrHbkKjPUB1--fZ61o5OzivoHxGX0snZo7FPqDOugl1HHap2hxNCidwOWvgpS8IP6tK8HM0XIAUXxdgtsiKsGulx-GBqhPHTg0Pv9aoYopM82AhtGN9NKmJM6zUsgpkM_NbihlBtDTx0wAQmx8Wb55T42F6J4d-oYC7QDQ9ET4-5Ld9Xe61qEozBmIqnQv-c26lJ6Z8x7srqkbkriYnMHD2o4JKsBTS08b02JLQgyTHk_W0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ez4emh_fSP5FF_xPlZthQXNkhRWTNHHD98ntQaj-hNLLGjjK74eHZVdKSBIYkk0SLBniQji1jxYi58q-81Cy84UydsFOPLoZf72m7AiT7cINszwTzz0Q2Si61Qehoyq1vibdrEbxeSL90a61aXEW81t8-HbIhZM9UZqQirp1VrIymhtPSJFAWYz8QhAsa-SacaIofAqyTsJEjlch8xwJ7XGGRYyn-YEOMUoxjtyQYOyAslpFDUxehruRZP89aDNmMHmSDKitOZnFIXp-uOKARs4iQQ8-bltY78ietEUdgLzVfKENPnTib3zCavu3UnxGgYrmFoojrU3hhURFKH2CLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عزاداری عاشورایی سمنانی‌ها در صحرا
عکس:
محمدجواد فرخاری
@Farsna</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/farsna/444700" target="_blank">📅 16:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444699">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه معلم | MIC Insurance</strong></div>
<div class="tg-text">🩸
نذری از جنس مهربانی
جایی که هر قطره خون، امیدی دوباره برای زندگی است
🛡
همزمان با ایام محرم و در راستای مسئولیت‌های اجتماعی، بیمه معلم با دعوت از تیم سیار سازمان انتقال خون در ساختمان مرکزی این شرکت، میزبان پویش «نذر خون» بود.
✅
در این برنامه، مدیرعامل و کارکنان بیمه معلم با اهدای خون در تقویت ذخایر بانک خون کشور و کمک به بیماران نیازمند مشارکت کردند.
#بیمه_معلم_همراه_هم_وطن
#اهدای_خون</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/farsna/444699" target="_blank">📅 16:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444698">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/farsna/444698" target="_blank">📅 16:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444693">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nWn45ZmfVvFRtqyaJTp8Skdeeyqo6GBfTli6aTFdrQZ6YkHQTXZ-JJyXhgaKup7flfXQd2Y1P-7hQkMXxIYoT8UM7ugbaXxOgsbi5OisIzNjn713wvj9yh0Zkymk_o3nkcwlPtNzGe6RSnxXJni9sH8VBkTouxF7B_lFPINC1fBSX6tGFmKSrzl095QgyF1ISKrgVl2H25CF9jAcds2ogkkjN02niG8PM7LkwcoiQXQrn1EO5ogs7DndsskfdgxaHj2V6xooSoJL7YBCZDiqVT0pZXYAQVIFU0FHPmjQSfKqvzQutcpjMz_4nBZvY-_nTZQ89Mu0ZsCCSJZG7shXIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gnk8-nFOdToTFOqa7OiuoaLVj0mo-tKusMvzaEY7TFvv4bCpjEGhR8-KPfaW3Fk5BCY88ZjfCaQ1AVkNm7zDUk5mq7nCRvGxRHUQO0aBHiAL_gftzmJlI6QBxd0AK_GDysMc555uboGlEJp1iKOAGcqTyPn3HjsM9XfQldokjXS4cdKiDMizwYG_IAMpVm2AzYYhaIUxDwkmxigTH7H2qzUCRsFP-mDOp-QM0zoaTZBtkUB8DyHGAFzssO4-ofiRV-pqpJB3STSMMZ0RFz6jZOV1Xa7f7uy8KOoZQFctknSOGotPlUr2JAOldy7ilzzIbgvIPeUxJHC7bCuP4xguoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kBFpAQLlpyo8wpXI2O29McegybSfW_UnSZmkv4P1zuG5bzGLbhGj_grC-U57mecWfdbxzWRih8icHRN3WM-OZdWxSGEuXfi1PFf-nda5YJQXIR8t5hK8mg92sWlnxyPw1FnCS96zbu2X3K1ySpnhSvSa1Lg-Us_ev9gQBvICV9bONQVc4VOvMe8o-bfB2XJelxUUYZwFIHZToZxj2wKsRMMFCoTQQUd7_mVq6oclk1SaGjDqba8ZubGQKZh1CjN35aPcZ1mL4M7ZjCHPAAp8tiesEqJrpGL2TzDTkBb68tnhmMKrhnokCID5eN3UxX_U3lzmy47gAXe0khOK-CDh6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SPw_jzZ7EQ69qX88EgLD077dZM990bxBM6FCcb1wDW6izlYFyZkAyEdIuweJeqJWKW-gkEefjVpW5Y229kN_vVAeQ08Ia8cYoAWbLfj4an-jYpd6n5Ty21UVAOXLj9_9YiYpQ3inFl6XpGEdmmGPafpgpnOduw1NbgM2sADszj2Swkxnp8sA2cZPlO1HvwpFUbsw2V6V_wvEUWCJhbRUxcJMH0R6BHFH8UUpeyZ-KZOAuuR_N1Orv6hwMHYD4FZhnSotv392tvtV8_dKdXROqEHWwxk0VaWyhyO5Ylp4UAJK4a3OOwcuAxYpA7TADBuDnJcrRY1Ne5aa_VWkm8Ynag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rBtMv4iSWqjU55CmjMkSrlT-3PTT1rF6FbH_4tml2bOeotFiHrPVljvUniRdBb4zxUY30tXIUeAJEwAnttiQYyLg_sRKUGCL6S3V0LvOEymw7md1PV3Xj1geEBLL8Zbqr5gFtnliipB1Jw1JqtUSJezP2ibjrfBLfbF0w3j-UmoWgtoKNEcqYSusgvAbi2sYo-dfPgTE9Tced4J0bewstUiDMngTMLfrbR0qHAvmkwOVqPTAEG3dO0JRlEKHL9ijeFOn_pZ3W9wSRSLluBPJC1kipNVYrsmnj7SkqrtWjLx9Dhn3pNLBsGttXMgzMy1FWyTBJ4VSR8YAoFDOo4lXDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آیین خیمه‌سوزان ظهر عاشورا در چهارراه گلوبندک تهران
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/farsna/444693" target="_blank">📅 16:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444692">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSbsS0P3N63E-p91BlgD7oo5BYv2zFTgx2S7g4KLFyTbCSwIG6ZNK-qU45p-O_wV5thLMwSfyJyZiIJB3BTJ9zEQqqmffj-Vec_4jUw2ZU6GEJhtWwJo7U2CLHxBMTdnOC990ATsb2dr390wwvNosR31wIMKbOjU4f2GY-xkPJQGkQp5Pm0mpj4UFv3WVSOpY-wkE-eGnIRYki56HMX8Whok9J_JnObaT8oEzSYfOnd-9qkICYYIZcE1YlsGXW44h3R42jZNZ6wdsjRfUOH_rruWbbl4F0GLM6as97tYqQUOBi6pBqttGOVSavQ6bCHlaqH2ujTSJizzGcmQ_HTz7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: پول ایران را برای کشاورزان و دامداران آمریکا آزاد می‌کنیم
🔹
ایران به ایالات متحده اطلاع داده که برخلاف گزارش‌های دروغین و فتنه‌انگیز رسانه‌های جعلی، «هیچ عوارضی، هیچ هزینه بیمه‌ای و هیچ‌گونه هزینه دیگری از سوی ایران از کشتی‌های عبوری از تنگه هرمز درخواست…</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/farsna/444692" target="_blank">📅 15:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444691">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d20af7bcf.mp4?token=Gvtvsl23EJC0Fawm015HVbiUn1JxFtVCUwbpflBg0zL_32pkfv1oXsbsZaXA8xovU2tcWxlg4LI7yKWqVlkYV6v2-RGTaXb3prXCs8OnCUwUG05aMcp0PX4qsRcz7DCoDl7NPSfPf2tBrUGjKMQD58Df4mYPqWStyvMVcqFDtXzMrNYHZHzuRpkgMCje1-x9gHyVA8LzedtPIji4vSHZUoTuQyz_7b2yJZsNiM0IXg6Yq1ZiPvzfzm5P9mTGlMaEANDoYuFUC8hUVRP7ay32CxnHQ-LoncgY1LTvvLR4xaHcSRmEQxf9kiIq8Lk8etuAeh_zrm0xa3M0T43kZ78LJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d20af7bcf.mp4?token=Gvtvsl23EJC0Fawm015HVbiUn1JxFtVCUwbpflBg0zL_32pkfv1oXsbsZaXA8xovU2tcWxlg4LI7yKWqVlkYV6v2-RGTaXb3prXCs8OnCUwUG05aMcp0PX4qsRcz7DCoDl7NPSfPf2tBrUGjKMQD58Df4mYPqWStyvMVcqFDtXzMrNYHZHzuRpkgMCje1-x9gHyVA8LzedtPIji4vSHZUoTuQyz_7b2yJZsNiM0IXg6Yq1ZiPvzfzm5P9mTGlMaEANDoYuFUC8hUVRP7ay32CxnHQ-LoncgY1LTvvLR4xaHcSRmEQxf9kiIq8Lk8etuAeh_zrm0xa3M0T43kZ78LJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
وقوع ۲ انفجار مهیب در غزه
🔹
منابع خبری گزارش دادند این انفجارها ناشی از حملات هوایی اسرائیل به غرب غزه است.
@Farsna</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/farsna/444691" target="_blank">📅 15:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444690">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkBCinJvZluoONtJ-TbGTqzWa3fOMUc-JB_s7OIEDF2MYwvta5WIIQ1oRCOnwdlhIUAq4ZkxJUnHDrF50wEgB0vQ1mPKhsJ1yI-jU1tgz9nJEzgqGH2ntXyxJJEgvVUHBvXI2sZtxoaQzu2mQpU9BIyhlBCXenRy4xaddaYMhMBlp9Jpnd8EK9Z4mtKYufjs1qmBieox9JDO9oz5Eq9z7dxtJqm5SELQMq6deoN3041oIs7gsVHG7oMf5k21FzblDARvW9BW1DkQJi2d95rczf0adY7TRB5u5EI5CV3ElEUdCzGisjh5FgplVmmvHlVBvtwFENaOGJjyLzZJkGmCTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تردد دریایی در تنگه هرمز محور تماس تلفنی عراقچی و همتای عمانی
🔹
در گفت‌وگوی تلفنی امروز وزرای خارجه ایران و عمان آخرین تحولات مربوط به تردد دریایی در تنگه هرمز و ترتیبات موقت پیش‌بینی‌شده برای دوره ۶۰ روزه بررسی و بر اهمیت تداوم هماهنگی‌ها، رایزنی‌های دوجانبه و تعاملات فنی و کارشناسی در این زمینه تأکید شد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/farsna/444690" target="_blank">📅 15:22 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444689">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ace3b66cc.mp4?token=hfamaAc4VMNdfE7rq7R7yDWSkasF3m0Sl5fm1mH69kNjbP3M5rWK_pqn3p89OEJXOEn_wwoy7b4oQHeEPflMlu3I2sR74QJbAHXrTTp3qVJqMMOf_iof_cG9wN5Vk5-m2mu1ah1AR0ixxGXv7TBbD7QGCC-bzIdbTv8nFcGwr2UBbUmo-qnRGJ6YepJNKA4SzuxgexKeXWv1GoREaB5RPutsvskpKPKXYt9WwauPQL68gBghagLL9LMSX0V8agK__yjlCi_vUPRoc6WzVLjhOBAnk-V8BFmVhwS7jzuFsHuKr4FacdhFeCDKOzxhuU1jHba6Itr5-I3LxYxOceRgR32pgXc-lIXAgiV1bs5LutA6WATA9o25JvOojjwTz9QmSsnNe3Ou_eYXo5GfWAji7GIY-sCFuRGxdn0enlSlV210ErnBhDBik0oH3-P5_s0K1cTGr8r0V3DKH2vhjkweAE_nfON1-Xn4ASjLH6J_JP27drwWookAD7eKQzAdMs4P9LV_M6siRhcL-HJDm9Ck8p1NOQtAvReLMWWF4FOTKBAn4oNGI4TXDIpmZP0sb-YX96tXh43h1X-BYwLGQGOzriIWmvfR3J8mVjmCK_LjuHnlGPB5--yiMOlzMUAf6XCGcl-fuodIzRShViAd-4HzXgmPVTTIW72PI5xb-JMEGcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ace3b66cc.mp4?token=hfamaAc4VMNdfE7rq7R7yDWSkasF3m0Sl5fm1mH69kNjbP3M5rWK_pqn3p89OEJXOEn_wwoy7b4oQHeEPflMlu3I2sR74QJbAHXrTTp3qVJqMMOf_iof_cG9wN5Vk5-m2mu1ah1AR0ixxGXv7TBbD7QGCC-bzIdbTv8nFcGwr2UBbUmo-qnRGJ6YepJNKA4SzuxgexKeXWv1GoREaB5RPutsvskpKPKXYt9WwauPQL68gBghagLL9LMSX0V8agK__yjlCi_vUPRoc6WzVLjhOBAnk-V8BFmVhwS7jzuFsHuKr4FacdhFeCDKOzxhuU1jHba6Itr5-I3LxYxOceRgR32pgXc-lIXAgiV1bs5LutA6WATA9o25JvOojjwTz9QmSsnNe3Ou_eYXo5GfWAji7GIY-sCFuRGxdn0enlSlV210ErnBhDBik0oH3-P5_s0K1cTGr8r0V3DKH2vhjkweAE_nfON1-Xn4ASjLH6J_JP27drwWookAD7eKQzAdMs4P9LV_M6siRhcL-HJDm9Ck8p1NOQtAvReLMWWF4FOTKBAn4oNGI4TXDIpmZP0sb-YX96tXh43h1X-BYwLGQGOzriIWmvfR3J8mVjmCK_LjuHnlGPB5--yiMOlzMUAf6XCGcl-fuodIzRShViAd-4HzXgmPVTTIW72PI5xb-JMEGcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
رهبر انقلاب: بنده علی‌الاصول دربارهٔ تفاهم‌نامۀ رئیس‌جمهور ایران و آمریکا نظر دیگری داشتم
🔹
بنده علی‌الاصول [دربارهٔ تفاهم‌نامه] نظر دیگری داشتم ولی از باب تعهّدی که رئیس‌جمهور محترم به‌عنوان رئیس شورای عالی امنیّت ملّی از طرف خود و سایر اعضا در پاسداشت…</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/444689" target="_blank">📅 14:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444688">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f815f0f49.mp4?token=vmswh2ULdVE-9m7ppCcVRmQLrcjYXgwRyN7LCBsGc0lEgRc2pmX2oFls25FH7oUFF1ps1tbLr1yrf488yBCv9XKTci-LnEUjmZZBAMTRnko6dtMLs1iknbDBy9nx1QCJ9yIQB8QcZmQ8hJI4U854c9rxFI1qzSgNRXy8b5V4QkeJjTnStUB0ZJOv8fR6o7_f59stOYCb7DjuERX7dgb0ZCawPYd50VWraYRhaa6LYZ00hICMOnBxnuxgNR8ohiMbdyBoTK7EfQOxh-Jx-ujGDf5yHkn0BlnGVZiOoa0v_8jo3MrUFvOsuaU5_k4dUxRqlLTc4SPUvMBErvhZVa1S-3dRwHtdVY-JI6teGNtdzwIub3SLx_ZcK-YaUgfBECM0rjXnvhpXtvpWQTr06KzFbDiFB5FxPxKkHt0x4J_7g4weyJQqeNZC1eBROxp7lF1B1SkR9HFicdhye1pOdpTVTDkX1Q6jgqZlgBxFJF02LhK1gXcjkSMMyuTdjMhGDmQezyBd1WmbHc-YdZWNMU6QaxSiJagg2pXSU3o0-xiA3weYfPZD7259KWjmUpEAPNV8n_xj9mY8ZlwwkOVG0--zaDXMB7cPNvvYvEgV4JkEpXOrmBshxUE6cQM-0ZiFFAHfrHHIHtwiAQQkEaXns1scIJv3MWhc8L3LWCe415f-w08" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f815f0f49.mp4?token=vmswh2ULdVE-9m7ppCcVRmQLrcjYXgwRyN7LCBsGc0lEgRc2pmX2oFls25FH7oUFF1ps1tbLr1yrf488yBCv9XKTci-LnEUjmZZBAMTRnko6dtMLs1iknbDBy9nx1QCJ9yIQB8QcZmQ8hJI4U854c9rxFI1qzSgNRXy8b5V4QkeJjTnStUB0ZJOv8fR6o7_f59stOYCb7DjuERX7dgb0ZCawPYd50VWraYRhaa6LYZ00hICMOnBxnuxgNR8ohiMbdyBoTK7EfQOxh-Jx-ujGDf5yHkn0BlnGVZiOoa0v_8jo3MrUFvOsuaU5_k4dUxRqlLTc4SPUvMBErvhZVa1S-3dRwHtdVY-JI6teGNtdzwIub3SLx_ZcK-YaUgfBECM0rjXnvhpXtvpWQTr06KzFbDiFB5FxPxKkHt0x4J_7g4weyJQqeNZC1eBROxp7lF1B1SkR9HFicdhye1pOdpTVTDkX1Q6jgqZlgBxFJF02LhK1gXcjkSMMyuTdjMhGDmQezyBd1WmbHc-YdZWNMU6QaxSiJagg2pXSU3o0-xiA3weYfPZD7259KWjmUpEAPNV8n_xj9mY8ZlwwkOVG0--zaDXMB7cPNvvYvEgV4JkEpXOrmBshxUE6cQM-0ZiFFAHfrHHIHtwiAQQkEaXns1scIJv3MWhc8L3LWCe415f-w08" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان در مراسم عزای عاشورای مسجد حاج‌احمد تبریز شرکت کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/444688" target="_blank">📅 14:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444687">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2wJu2qRzw58y-Qluw6TKTTwINqHUHnhoy_3qw1up2-cR_GSw0dnjU0gP_eoBqgcwmK563ac02cNNowDBDNsf9QQj2EJSYvnH030Hp-FP1jDsvXBk0D8PB7vLvCjFi3357ttdB_VDwZCU88UdjzUCKlP3PNsrUQYy3cZa4CitZ8utE2mfx1c6R5TLttnp8Q0QcchbwbWp8ztMT23VEH6MkNHOiZl9ZOWIjXwjed-P2gX2KtxvHSQeXAV6v_2MJYCU1EYPMWNRpoYMWOo7eVBUMW7puGwmjVxUzz1NfBq22Ui48BH-Uehlx6nluQ4kjHf5D_gd1yzlhktcWbXHWKWyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار قاآنی: صهیونیست‌ها باید سراسر لبنان را ترک کنند
🔹
فرمانده نیروی قدس سپاه: صهیونیست‌ها بدانند؛ آنانی که با شما یزیدیان، با روحیهٔ عاشورایی و ایمان حسینی ایستاده‌ و‌ جنگیده‌اند، همان باور جاودانه را در جان دارند که «کلُّ یومٍ عاشورا و کلُّ أرضٍ کربلا»
🔹
شما باید سراسر لبنان را ترک کنید؛ چون این سرزمین، میدان ایستادگی و مقاومت است؛ نه جولان‌گاه اشغالگران.
🔹
اگر امروز با اختیار خود عقب‌نشینی نکنید، فردا با خواری و شکست ناگزیر به فرار خواهید شد.
🔹
سال ۲۰۰۰ میلادی و وصیت تاریخی شهید سیدحسن نصرالله در بنت‌جبیل را از یاد نبرید؛ آن وعده هنوز زنده است و تردیدی نیست که بار دیگر همان صحنه تکرار خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/444687" target="_blank">📅 14:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444686">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9594452e96.mp4?token=YAWA-Q9BjJrOEBUrLX8VUWmkJw79hl95KL7Dx117CSAe5iiiT7yUO0MIpNrZgon1EORC8QibqxLg4zpWeC6JDaJATHBtaiu4ObxWRZKAwzrHjSuDkJPsF-jYUGkzH1rlCHELXf_A6qBlx7mlUg2N03BF7Ut9lV1kMCRB4oFiDDaNuYY8zqwdCBwm8xVHS0xpiV1gzNNDtez85_OON_QUjcseyxbbZUdVRVBppZ3XYL6mhKmxiGS6DAjOLqHN1FtbGLoa8x7els5vILcqd1vlL_90oGvrcJ3Mw-gMUYf9SRPawffVQiNGFRli2XP5gPG6RoB3WmKbhsdcJ_6BDemOUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9594452e96.mp4?token=YAWA-Q9BjJrOEBUrLX8VUWmkJw79hl95KL7Dx117CSAe5iiiT7yUO0MIpNrZgon1EORC8QibqxLg4zpWeC6JDaJATHBtaiu4ObxWRZKAwzrHjSuDkJPsF-jYUGkzH1rlCHELXf_A6qBlx7mlUg2N03BF7Ut9lV1kMCRB4oFiDDaNuYY8zqwdCBwm8xVHS0xpiV1gzNNDtez85_OON_QUjcseyxbbZUdVRVBppZ3XYL6mhKmxiGS6DAjOLqHN1FtbGLoa8x7els5vILcqd1vlL_90oGvrcJ3Mw-gMUYf9SRPawffVQiNGFRli2XP5gPG6RoB3WmKbhsdcJ_6BDemOUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حداقل ۳۲ کشته و صدها زخمی در زلزله‌های ونزوئلا
🔹
طبق اعلام رئیس‌جمهور موقت ونزوئلا، ۲ زلزلهٔ پیاپی ۷.۱ و ۷.۵ ریشتری در این کشور، دست‌کم ۳۲ کشته و ۷۰۰ زخمی به‌جا گذاشت. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/444686" target="_blank">📅 14:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444685">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🎥
طنین «یا حسین» و حرکت نخل‌های کهنسال در کوچه‌های کجور مازندران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/444685" target="_blank">📅 13:59 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444684">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🎥
برگزاری نماز ظهر عاشورا در کلاته‌رودبار سمنان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/444684" target="_blank">📅 13:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444682">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WmOvNSjgNWx6AvByrZKVrgzH_B9-1xNIVqTH3QF2EresOQU7slh8btmmcv16vOBFdkYVrXNC5rYMilUZPpah_E36KTAVO2bHdM7IVsqX4Eep5SjvXCXe9exTtqWDOoQk993CYhUsyQE9IEJA1hqiVEAEYqQTPMkw1S_bVcQdMZUHWH0gCmTG9WZeQthDqiTX9IljCDEAmN2fENx-dUv8ZQYOrz4MqR2_BtO63ymRrYpgf9QyP0RlQrYzkw5ZpwW5WSUFdnz7UahfZZUYizBu3_vTDJcsos4FnjZLM3-cEkhzg3RJLf9jkkPEMemCNfFczyV2KsF6-qXfgh9e-eI9Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hxXv0Z7FwS_SWSZozBGvkPIoEck6AioxmWklkVAaquNj46ZF9VlcG7_-bdWVeVzp4mruGqd04ZVB99iFZJK_8Sprn-0CxanbKsVj241T_-EDwqtjd7lA9YG_-LlILyNxD8w-RxrH9ymPUNDgJmuNyegkEvhrKl3pl3fdgruT62LLSTQkqjESG979x4TY_QFhfJXc4241KZ_I8VYahhCO41RUKzkN4J4BpaLf6gZpx3JZN66OCwQVSIPlTUm_vfOHvycRixNmsX8vGAWizOZEh8EMP9RGfxMpRt_ZUb9tu__v5L2zKAZmCsJJGyXrIZAqpm1zWBJRGeiQAbD_Y78vxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
حال‌و‌هوای مزار شهید حاجی‌زاده و شهید محمود باقری  @Farsna</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/444682" target="_blank">📅 13:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444681">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e85b59a8ec.mov?token=OkHfX9ws_EYyBuZXFrk_BX5tSFJFcYGIBCLMSRs8NIv-nlFyk8CPHSDVyfZ5Ho8V1YSvUpMio136buVIp0CNrU-Wo2qBt2KPdc2BUZxL-JJu3vL2_lUO-u03rVJ2FSCV1TnetuBHNLGpJB-XZQaJZ0SI9fFuwWqWZNin5Yih9kw0Xv1MfBWwnLLj3SOZq1cr4A1gSDWlr9-1woBBY0FtE4NOCKe-EcgSxCBZRMuJGK4JvRXDDJpeh9lJECGBzQIOJp_scjvkyl-IEwxJ-xtcOUCOPZkP9SqkIu7MqqhC-PVgPpNNAeKjtFoHIq6uJvzkHOLYvNF5TCVVUA2drlVjTpDZHPK9QUfYjhP5BTKK--PFZm4Q3iW7ceohR498i5sT7EeYh5hBXIn3YRU2nAQpsBLUsESDmm99hRdiUWpf2-lF2h1cE774mHIyZuBWW4wSxoDGR7ugHLD-5mL5J5m5ZH1E0RZf97kyYqEdkygvgRRlYmIBHbLmzrjJa_dY-oI-8c_A8dMrc6JxubocRviiC1SnBaFKfdiafyeekEj-_uuVoDN-jYgPq65gHgiT3sHLBaUvFnGX_idyeTGx7u6Ks_wy6l5In--_D3gbKKsJcudNyMo3BZhxm9sL-sv8ihIPUIX6G6cEhIXsv6wU8FbhYxMarmq3E6ttX70a5RxORQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e85b59a8ec.mov?token=OkHfX9ws_EYyBuZXFrk_BX5tSFJFcYGIBCLMSRs8NIv-nlFyk8CPHSDVyfZ5Ho8V1YSvUpMio136buVIp0CNrU-Wo2qBt2KPdc2BUZxL-JJu3vL2_lUO-u03rVJ2FSCV1TnetuBHNLGpJB-XZQaJZ0SI9fFuwWqWZNin5Yih9kw0Xv1MfBWwnLLj3SOZq1cr4A1gSDWlr9-1woBBY0FtE4NOCKe-EcgSxCBZRMuJGK4JvRXDDJpeh9lJECGBzQIOJp_scjvkyl-IEwxJ-xtcOUCOPZkP9SqkIu7MqqhC-PVgPpNNAeKjtFoHIq6uJvzkHOLYvNF5TCVVUA2drlVjTpDZHPK9QUfYjhP5BTKK--PFZm4Q3iW7ceohR498i5sT7EeYh5hBXIn3YRU2nAQpsBLUsESDmm99hRdiUWpf2-lF2h1cE774mHIyZuBWW4wSxoDGR7ugHLD-5mL5J5m5ZH1E0RZf97kyYqEdkygvgRRlYmIBHbLmzrjJa_dY-oI-8c_A8dMrc6JxubocRviiC1SnBaFKfdiafyeekEj-_uuVoDN-jYgPq65gHgiT3sHLBaUvFnGX_idyeTGx7u6Ks_wy6l5In--_D3gbKKsJcudNyMo3BZhxm9sL-sv8ihIPUIX6G6cEhIXsv6wU8FbhYxMarmq3E6ttX70a5RxORQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برپایی نماز ظهر عاشورا در جوار مقتل رهبر شهید انقلاب اسلامی
@Farsna</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/444681" target="_blank">📅 12:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444674">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VMyJIE17XJGejulO_npFCT_xpQozA0-fVEMbHbmMpEX8AKUyMGLlE4fSPnoS0o6JgTSj0sYjm5_oo3cwAi1Of93UuFJZMTjaXcVn4wwIoIGWhn0C4ILW3z_K8xworn9G2qOpN0qRJkuyKu4BcQppDMtq2qTphIyKu79oGjXm51Fxuw_L3SNYlCXk1mDg5PVH6vo3UHYilYk85lchYvefzoLSJ5COvmD3HEZfzTcNmo1zrYdgMux35J59NgsL4vfleB7IDroLgKbUvEPGZN1cWvWF-ehDk1LiZc587zezTlOs4pT33l-Tow_6EdAoKV6Y52cmapjxoNnE6cTpqSAwng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DRdEqQvZ2UlvEUJqWOfVE86EJ96YoPbR1cyelezTnQgHsEVHzwvCgRzVB6_wvr4AwFX_1bj4eN-LTYNZkYPzkKQUErBp9d0x8Utfz0jtpqLfHytsSXtA8RUt90v2SKVBHD8_kQadG2R1lLT_tqDREXalsT-aSUuGOlKDjT63yyV0bTX9BbLVhWdfQH-R0TdM0A5TH535C_0qlGZYT8Lu_Bn_gXBXSGbqUw3LbbxSKlr1MUc0BAUAIUirduyq5CV3Bto-AKcPz9EABCPIHuZslbblvx71wnZ80UyBtcm4HUBJ3Odp5PjUjYHfoM1t7cGGc7O3clQELdoKfikz8gtYgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oRGzxH28IcdH2NdsQqhoVbZO2kFWdyhYULCfqGRbpuLtzN5FnafVodUuyBAZzrstxAJLDOYx9lky67A7GAAEasGm8zDeMkKGv3qEgm77rqJhqklv3ka6ogUxB7aQBvegpORAT2ltCxRow9ExbHMbs16VVSF-0LbdZbovY79cPR7MRTl289yrK6kLYiEV4Jvu0s2EmfhXi4epNvNHCF8iXb_eMcLFiLMovvzrks-GfYnPnSXKN-Lsns5_dNZfFwrVbBXkO0Eb98meYSiJiNNqu_ebh1VZxx6U2kQPykS-gmXmM5n9gAm8otxItxstjxl3YPNyqhL8nskCfGflS7XC5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WcXUeFTFALSY190IWpXhr17WQRTNXI-4q7FDf21hUdG5aQx5xnFFIwQWXDAzIXZb6KEt7-lXZYANiexrDNGxFqt2NKOfKxBcQ6vIBjMidbzBi1zyn8CbgM1bBeph3JvIDYECuyoyC_LwmlBPmslXHTCcBgBP41ZmKQ1M9jZAUFEkRLDS002OD6TVLTEYD-2w_SIOX3OyvrydVwYFZaHCTxh4yi8aPhL3ahxtdE82mRBsP-_odMDf1iw7HdnIGQutSESXqeTFHp4-eEorR9v47O7eKXbR7nIRfII7IZNnCB-a9ZIxqrMIfSPdBNE7Rxjj_8ZRHgHKx_5O839oriA9QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/voM3iVEAQWKzh1PwCeFA3-sWEiutvnoNOSZ9FpYcTuXUOpDRHKMwAABXA-3TW1YIiBazZiZ7iUcq2QurzzAqYyR_T3Gist0ZI-n74dftS3I_moVJBIt3V-9UI18-LYaqBHN-JaYPTZryfh3DxOjyVDlXLAeCzwiVQuWT7tNh_4jJOaDUXzfTzIZSQhmAHw876csrCL1a3SvVkOarHqmqO6wsySvmLI5Y0i14oLVxvDMOvDZ09EERwX3v23wU5IPfVHVfPuAGcAmbsjTgONzD8D4z0tU6PkYfV0sijQw2gpkm7kRXZXaW0Xxmx22js2eCHPEYlpkaTh-XzqBGHUBznA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jVFkzSynjN4y2kKerDsqr9dQcsU8Q2DkPXspI8Qe4tsHy8xbAeTWUTJJ7qZZA5TtkxnRg7TUkVZ9Wxtjfkm96wxe2wl-18EQmLTzlkz1muSzK3WT_dGy-2UgBqxu7HFoTBtxbacNmu2x4hTOl2POsxQtXYpCKlJ1M69n6fmKF20138ixW1EbX_EOFeenRU810NyyYCIULJuHYRMzwXBJKzMrzVbMS1W_QYaVSBbJdb_5j4nh52SJ81fmYLLMBN-AMeqEKXgqhw4JPqEfTBnOHFBM9yabErF4hPstyYXKw6RPQpB9-dQ4hD0VRIqA7hZAL7YSIeSLj0F8siVOj6gTqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TNZESwhIWgjgJg_uzsw5O6Y7X_pDmZ782QDNVBSSrESI5yfw7Gy1B-wnXBjeezg5MD8RvKkhmUJ8hTE-vb97odaVII_sNeDtzm2vmZ7J3FYz5jynuzEkOR6FiGmtxEWlEa8FrAzLJlfHWCX3xNR0dasOTburldDW3-J3AsV8ZwcHzW2P45MWcriaoTcJ_toDSv3FYmJWuAZf0eblVwf_TShH5u1_QoDUKk6AWgiPjq5ucyoKQMMmPd9rf4e-v9bRNYv2xLpj2827TJxatNId1LAJXZZaFxQ8MhyfdZeY-ADEaDOr_xkax0LnOsfSKzZxU5U7HtaS41SbG1-4259smA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📸
آیین «گِل مالی» لرستانی های مقیم تهران
عکس:
زینب حمزه لویی
@farsimages</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/444674" target="_blank">📅 12:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444673">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e716e4e7d.mp4?token=lmUgyYfO9t-lSHtOnx56Ls1VHaiRwmTwZ-HK-Ooh6o6FyKowtqh1KolnwV8to2UIrs8eG6HA0wELmGQf0TXrnXkrW_41Oajl8R2UhrL90VsjmZZNzOXSiJzgyqJySwniQKiH8OEeo2JHb5nIl4Q0n04xJu09ZgGlbhK9dRECPrfGmTcAqMQpjxZat1hZcWww5Owp57mEAbkoolBHJ7YjXYllU89r57iafAL-Ll1fUZgHIl7BSnWwTvUqYeqmhv9EleJPziADz6Ex_X4BqalnKakXCTWkV7myFAclYqXkHlwAfqtupk8-3crt3gHE8rvp3oA0C9rwcchBK6FVGfLBRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e716e4e7d.mp4?token=lmUgyYfO9t-lSHtOnx56Ls1VHaiRwmTwZ-HK-Ooh6o6FyKowtqh1KolnwV8to2UIrs8eG6HA0wELmGQf0TXrnXkrW_41Oajl8R2UhrL90VsjmZZNzOXSiJzgyqJySwniQKiH8OEeo2JHb5nIl4Q0n04xJu09ZgGlbhK9dRECPrfGmTcAqMQpjxZat1hZcWww5Owp57mEAbkoolBHJ7YjXYllU89r57iafAL-Ll1fUZgHIl7BSnWwTvUqYeqmhv9EleJPziADz6Ex_X4BqalnKakXCTWkV7myFAclYqXkHlwAfqtupk8-3crt3gHE8rvp3oA0C9rwcchBK6FVGfLBRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شور عاشورایی در ایران اسلامی
@Farsna</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/444673" target="_blank">📅 12:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444672">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CkBB_jtW8Ve2aCLATgXkiSZ8waKFEzX7YU3qjLvFPhoryx5mQ9AXl1NGInP4qVObc2ef6RrAQxBIB9sAqIBqldNBLxAjb6KxvzCvY6z6D0J7bssno-oSCoxksiDDYHhGx7My2EcMb74dF9YELbA4Tx7EaI5fNytpPwnBHl5OkK1c7aSXaS6pz90GrTFhsEIG_2c-O_VTn-wMDQhOHhnXH7Z1XkTgSOudHZXxoR7OjOJVCe_iq0GriyOd0QnGIUFY7fedRa7waRlgOPwmYYBY7ck6zGyPwmkl53GzKWX5A5P2MyI0uUZKngKXtOr8PAyj7046_zyAVngX5Nqtiaf6Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
و جمعه بود. دهم محرّمِ سالِ شصت‌ویکم، مابینِ نمازِ ظهر و عصر. و حسین پنجاه‌وهشت سال داشت.
پس، سرش را بریدند...
@Farsna</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/444672" target="_blank">📅 12:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444671">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78488a264.mp4?token=aRoB03thaWD0Vp2TJN7acFCWGEVTaTjla28ic5D9gJfM7HlMSDrzRaiVg7gaB05LmEBMCx4h2qSYb9CkJBwXY1i6zg1KTNlnMN8VZnq4OR4JvUQ0WY2LucK-5OiVNKrKUoqDvksegHztRNB1DeM_3pue4CEHoFNqwOOkSme0Cc-o-uQBJZbd5GtlmCeR8_eRR5OAjsZ5llsURuwim4_df_lGsnChsn9fJtDqy0E5FZH2VM-WXgUEdeM8X-VJPcwGGV42AEcuqU97AQ3pse-y7ZdwC19caskGkCO5bUSfe1DIvYTFIovFFhpUCw8lra9iyNWKujqGg5M-Xt_wcThHiwA6cxZ-JwPObz6Z7Ocn6iLlj0MH8hWlt6C4vEWZfohRDbt77HWeVPiESerh8QyG_bR-h_8JMYRH4NV_Gn6zkEyfWBsIbmE7J-0akZ6KnnEmeIP0puMNjYrOIYlUE8FvHkAxW2s-gjVlrwDDwbCG2X67SPZWINDtczFGW8rOkZc-3rOBSqGJiIvhwpYMDaQ11aTZ9lcz8vQ3SzAP2yhra3JzCk93hmopZSK-3abDTnRNpWyR1B191mKrG1fRAGOUEkJIYxbVe4GGopPEXbXlJBrfSOHniT4saJHabLE1MoIt1TMqfjFHw3gLxtQQ4bWYkUPkUH3QqNfh_COqidr_gl4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78488a264.mp4?token=aRoB03thaWD0Vp2TJN7acFCWGEVTaTjla28ic5D9gJfM7HlMSDrzRaiVg7gaB05LmEBMCx4h2qSYb9CkJBwXY1i6zg1KTNlnMN8VZnq4OR4JvUQ0WY2LucK-5OiVNKrKUoqDvksegHztRNB1DeM_3pue4CEHoFNqwOOkSme0Cc-o-uQBJZbd5GtlmCeR8_eRR5OAjsZ5llsURuwim4_df_lGsnChsn9fJtDqy0E5FZH2VM-WXgUEdeM8X-VJPcwGGV42AEcuqU97AQ3pse-y7ZdwC19caskGkCO5bUSfe1DIvYTFIovFFhpUCw8lra9iyNWKujqGg5M-Xt_wcThHiwA6cxZ-JwPObz6Z7Ocn6iLlj0MH8hWlt6C4vEWZfohRDbt77HWeVPiESerh8QyG_bR-h_8JMYRH4NV_Gn6zkEyfWBsIbmE7J-0akZ6KnnEmeIP0puMNjYrOIYlUE8FvHkAxW2s-gjVlrwDDwbCG2X67SPZWINDtczFGW8rOkZc-3rOBSqGJiIvhwpYMDaQ11aTZ9lcz8vQ3SzAP2yhra3JzCk93hmopZSK-3abDTnRNpWyR1B191mKrG1fRAGOUEkJIYxbVe4GGopPEXbXlJBrfSOHniT4saJHabLE1MoIt1TMqfjFHw3gLxtQQ4bWYkUPkUH3QqNfh_COqidr_gl4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اذان ظهر عاشورا با تصاویر زنده از بین‌الحرمین
@Farsna</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/444671" target="_blank">📅 12:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444666">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UE4i49zh_6gni5U7OQk-a3XM7uWvHmvfuD0hxN6_rGfSfYXN9GT6CsFRRe7nU0xFrKvSd0_A2wc-3XkOINfuAiXf13hJGcl23vngIVFgyQAtJXL682oF2lqBARmUlPCJkp7HlPD9tFLd5kpXWD2zaeKjr7RuW-_ucb9fP-OzQ60AuiCtxPPv_9BiQ5Fbzj4hQxwcxyzDgqAXXYUvPjeSpl5vXh1zOHKUVRIgq7UeRxzCNFBxYsiZHewFCfo8G_JYdERNaGcnRzjfS_FlxapyLSC0pPYNjxCEogDbBbvPWxs_i4vJVB05P7ECaQZtLg4j6qs7qJmojJ8ZzDxdoyVk4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VmdzUzAtlXLtQNWPBnIYIixWxj4np_Qh8O1dFB1Q03N5rOVcznjF4Pij7FykQ6tL661j6BDgVyqPgvqINDmwKKdae2UgGt3u7pQKrbAX0fyf8JVp-TxNtJe6UZbkGDEYunOnLF4_02Df4gD86MiOcvpHgaR-x3AZPLAaBXNw5dxKqYriRZnZPDroIN__GI2WXa-5jXlbeEc7AcFQvKiIWxtYZ4Se5NM6gesyZnXPKiTYB6OeGEw31MXPlf5jLqwUl89ll2GFdI0tYDLQ_-yoCScvIjotplqTeHc-00_vToS6Att-B7WuLEAhkpGzsP3IoxXCpuDAHm6RwGo4ufYm0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KCGXzuOWwFFD30-Yh3kJUkDCOUtIkqBPfNqjgZKAY-Lzw42PxzhGkAgccGpqRsgLGHz3xhFEAWMkhCGQHgk3X8R8TgnIbtbi0AlalHM_fFoqgcqrs4MDo0z4OaWTZNDMui21CQKqK86OelhaXP30_-TWGFfZkW9IoWv_P2m4XMcZwegM_OpmOD_-DXY5IByh7gDd_tobXFWee928x9LV7bgkjj_wMIS_si5Nz4xqVt1ENZtN0D6Cu4rjuPRXoNnLAtR4fYJ1A3aXMFTK97eciOGxN8iiSeRTuXF068ZlqsbiFUUxvSiKpI1hfWt1weq9xZsvT1fLBIpRUKcXk-m9VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BMxaSe2mudbCvItTn1-b-GpZjjViwY4gkbR9mOTMcnIxQ5xoPbdP9fRop0NotYLqXpruucnbX1QFbpIjughvskDu24-_9w7eMb3603bPegI6pSab3jJy6dBco_E2fR1DHPUV8TobbaIPoFbGvdLMQgSws-oxuFcwRoIrtzX_o-DR9fYRXyegdRtB65180T9wnTQ6lriK3tH6Dae8L_5cqdGXQjc-Ib-OtRgAkojd02ehnYhSXe-pAaHW0VBNuclLFV1PDIx-X51j2mA3bctegMtBUGUpEsINtg6u7Ju5fm1GfXnE0D0VcEMMT5Heg631aeJlqmfUQCaBL6mWB_sjAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/itUGJ5cSaVroaw653rlzrE_Gjlzd8zTNPXWxUVLwIY3uBiR2hGiYjimCP0SA8JQF391Rw6KU6L--akHm6XRMxELIkVBX94vyt9YH0pgOSiP8j8wtCSwdZj6w6B9xpLFecmiiXc9m4-Cbu4aSEX9gQFXQr134LxOn17HQYL1H5iB0x7Ot-JFyovRIUTk_B9pcXGq3BscBA5Rf6u68nvwOxE8NLLFAUQwKwY_lOZyXCMZpDmFcDtT6FfD-CqUSpwsHKHpdWvZ2Vol5aIu3KnVP4bQVmOsB4XHl0acZMcWcwcI_c-5dZjnadop_5LNO3SMgVlXT2iSBhWQmjq0QjF3Sng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
«گِل‌مالی» خرم‌آبادی‌ها در عزای سیدالشهدا
عکس:
نگاه ده‌دهی
@Farsna</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/444666" target="_blank">📅 12:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444665">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ebe09e2b.mp4?token=B1Wp1ZrIwKmMiv2TSP315t6a8dISNx2EOxAEzHR0dx2HIdi2JTmc_f5hVxTtr-uqhdoLbD1im4KZMUSnQbUl-00LvfzPi_W8nS5RKdxOPTC80xly3P98_vZtrWDq4V9gBMPl7f2DoLJmSz0Y8Azg5K8EOLIgjnmOfH6iFzwtN_Y2ZcScLPHdA9DmFxuXZr9YPJ6zwWfq-MhjtOR4XfK0a7KpUQoOj6BnrF4WtYKys6qCxIkJBpiM9ekHmczKu5Ae6KAEaBluPERK64WgY1r8dFDCzjn55ofZrEGWs9f0T6P4t0R0fEMIE8zrAaJnnblfDHg-ByLPY1in53lx9GTD_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ebe09e2b.mp4?token=B1Wp1ZrIwKmMiv2TSP315t6a8dISNx2EOxAEzHR0dx2HIdi2JTmc_f5hVxTtr-uqhdoLbD1im4KZMUSnQbUl-00LvfzPi_W8nS5RKdxOPTC80xly3P98_vZtrWDq4V9gBMPl7f2DoLJmSz0Y8Azg5K8EOLIgjnmOfH6iFzwtN_Y2ZcScLPHdA9DmFxuXZr9YPJ6zwWfq-MhjtOR4XfK0a7KpUQoOj6BnrF4WtYKys6qCxIkJBpiM9ekHmczKu5Ae6KAEaBluPERK64WgY1r8dFDCzjn55ofZrEGWs9f0T6P4t0R0fEMIE8zrAaJnnblfDHg-ByLPY1in53lx9GTD_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سوگ سرخ گناباد در روز عاشورا با یاد رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/444665" target="_blank">📅 11:56 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444664">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7251299b78.mp4?token=Owc56WWx4XoMvVJ98BluyHv1HxN7guGJpWWTe9cRHaqk3OrjUBEVxYAk3AV9mrIgAHMhiMOq5nr9TIMYxIshVZk5p1iTLSB5qZDjKpQL5hQEupbLAHxcmD-tdvrmGq5qxqYDkHhikDGzOHmXRtavXYW0hclV1GLL6PlGp7ijUj5LgRMMKbWemZMvynyVOhDeD_96bUL0yLvo8kMOZDMWl4mVo78qfDrGx2RUUm-moEPPauAq49R6dyo-LsEi0chPBxsiyQkUiyfUBpAZGxQkcKONUyyZNSXYgjTIob5BpvP6jr7_v4quHDb5Z5dntc4aUYDleyacpmTtDrHyvQSB0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7251299b78.mp4?token=Owc56WWx4XoMvVJ98BluyHv1HxN7guGJpWWTe9cRHaqk3OrjUBEVxYAk3AV9mrIgAHMhiMOq5nr9TIMYxIshVZk5p1iTLSB5qZDjKpQL5hQEupbLAHxcmD-tdvrmGq5qxqYDkHhikDGzOHmXRtavXYW0hclV1GLL6PlGp7ijUj5LgRMMKbWemZMvynyVOhDeD_96bUL0yLvo8kMOZDMWl4mVo78qfDrGx2RUUm-moEPPauAq49R6dyo-LsEi0chPBxsiyQkUiyfUBpAZGxQkcKONUyyZNSXYgjTIob5BpvP6jr7_v4quHDb5Z5dntc4aUYDleyacpmTtDrHyvQSB0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آ
یین عاشورایی «مافی» در زیاران قزوین برگزار شد
🔹
در آیین «مافی» مردم با حمل محملی معروف به محمل اهل‌بیت امام حسین(ع) به محل تعزیه‌خوانی حرکت می‌کنند و در این محل به سینه‌زنی، عزاداری و مداحی می‌پردازند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/444664" target="_blank">📅 11:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444663">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91c12769b5.mp4?token=F40XWHn0fERRo1IsKACguAcH6DhT5jbmevhI6dLowfMsAyswclWRIHQjWMpeBruNcu4saDVwJxmxJvpg1wYErmeNOssDw0NJ2r4M8_KDREElj7TCS2ZDiIjYF-gtturiFmquFYumVUb2Bu4iPH5FdvtdufVuHIsQUEapdqjBK67L4g_m48qh2MTfObFcAl14CwpLdN1LqXXUd5E3juOrtqkFtVOdJurcFtSRTpCPvsNQT1iq5GQIxsy6JZdpuYc52ftz2CATx_VYUuKcAYUt-aQSPYV4XvtE325YMiSq5JwMdiHrQGVrHuUD_Zj-xv0omBPgtGdNNXb6KX4Y6MdijIN1y9cnmY6w0ej-xWeDpC_V_QN4YlTmjsfgoaFthr9sFQSteUfm0NW0JQh3F9S7BVmwEkuJJHQWhV2VNRis7CmLQxLQpjN5sZcZST6krhIRHmAlJQVl1reHZUahlh9CcSnYP8PFN0gIK1CwpidiftAurimQtxFofjxtiugrFgkktEQTf8tQPQFRXiuSMXk5McqwrStzYLhhtM4oPb2TX47MCc4FPIdskbZiI3NofZ4Z35mvDjeHcLYGxBa4JJHBVZWcgzag35Xc_1cugq5JBQMZwZbRGXdaxexIVORkg2hPRuRE0orjCpuUNO7h9VJe0ZfhbBz1M0UkHf0MDLW-Bpk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91c12769b5.mp4?token=F40XWHn0fERRo1IsKACguAcH6DhT5jbmevhI6dLowfMsAyswclWRIHQjWMpeBruNcu4saDVwJxmxJvpg1wYErmeNOssDw0NJ2r4M8_KDREElj7TCS2ZDiIjYF-gtturiFmquFYumVUb2Bu4iPH5FdvtdufVuHIsQUEapdqjBK67L4g_m48qh2MTfObFcAl14CwpLdN1LqXXUd5E3juOrtqkFtVOdJurcFtSRTpCPvsNQT1iq5GQIxsy6JZdpuYc52ftz2CATx_VYUuKcAYUt-aQSPYV4XvtE325YMiSq5JwMdiHrQGVrHuUD_Zj-xv0omBPgtGdNNXb6KX4Y6MdijIN1y9cnmY6w0ej-xWeDpC_V_QN4YlTmjsfgoaFthr9sFQSteUfm0NW0JQh3F9S7BVmwEkuJJHQWhV2VNRis7CmLQxLQpjN5sZcZST6krhIRHmAlJQVl1reHZUahlh9CcSnYP8PFN0gIK1CwpidiftAurimQtxFofjxtiugrFgkktEQTf8tQPQFRXiuSMXk5McqwrStzYLhhtM4oPb2TX47MCc4FPIdskbZiI3NofZ4Z35mvDjeHcLYGxBa4JJHBVZWcgzag35Xc_1cugq5JBQMZwZbRGXdaxexIVORkg2hPRuRE0orjCpuUNO7h9VJe0ZfhbBz1M0UkHf0MDLW-Bpk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شور عاشورای حسینی در جزیرهٔ هرمز
@Farsna</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/444663" target="_blank">📅 11:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444662">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ViEC5L3i9gH-WnOdtpIqaQ4y5HB8X3Ui8iUkb76Ka-GJX55_jX6OBm5-KRQtiKo3Y9WBJNSodqY64562VOlc4Sf9WV8d3I1cDDVC5qrUVjOwooAFEP4u4Nrkq35N3gZF-pgm8W8k-jZtShGhTgKWjjTnyjM0ophma6oEwelAUcIV_hC4SoreYjdtvqBf4DddW5D0xUcDu-6pQn_I3D5HPTWDZ9Hx2GxR14TBFw8nlXbdwH2E4JFQ0-tOjb8Raf-bOe1LfjhXH3TxZ_xP8ZhEpxzmYjEn4gF_QScn2Bi7lDBHXoTexx-dV6-u317hbC1w0ugmJZaiDfvUCOaXOUv70g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
برافراشته‌شدن پرچم خونخواهی رهبر شهید در «کشوردوست»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/444662" target="_blank">📅 10:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444657">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bCV0pl9hNFWT-o6zGsdySIl0T_31A-j2HAd9aDNjnk2S5wMGrtBWtI9iV7htGg-6VanfLXcikzC6rkfUUBramMHNRrnJX7rVThAWDNvLR1ue_nyktXEMqLEyNMWAUoQJP6SZNrWGQQP8kW99yOaSOVAw8ZvGl8Q3fnkWhWUmLwfY3RIm0FVnxWOx8n529yz4TP6__hTFTG85KdEypazOMPn10mWFRxfZyowJBSAtXxdyeUPHCSdmcGJ4TDGldLsrw8oOkQf-_e57o92acfuPupocADcVP4j8BnluKS-Cko9WekhIn4fEMBCt1uDADczlIgnMl7FoOFv8Ml5SVfftUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v8RSQhHxeud9ZbjpKyrxNYexo9FLKXBfjaige_BRxS3vEz_kHqSApQGaQ1gSxowSiCIth-SyDLepS5VHrIrLzYadGfswlVHsWhlc7ZLyaAUeY8snCoJ2J-REPWQ6_O9dGckJY-RNGLVWNAGyNVVtlNhkQiUXNb2g9azHKMm1xMR_1tnYMGnnKAInP2qZsGh2G-t0ojCzRysFyLvLZ-BOI-wHXEk8x94wzssQoPRD5sCICe5ygyQ5xMeNiT-At_fvsCh44ZboPi6IHmDq59-xXkRdu6Yxu6ygPG25-IQxQCIX4nTSgqqYSf1leEE50TswfHvbMWR-eS8BrFu7JYWy4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XxrDGYUnTh9juNc1d6GbPOLfFTIpp_zQBzdQ9XCv5XD56NKYye3Xw-f1_ze2JH1xK5M4K1m2RizMoAFsjxuwPZYOpFQ75GbVhUB4Zxtv3t4lLFKXFRMC2hBubyPG5kDTZVcpZ3TvZhykIZEEty5E94n3ObqNoksbLpLkeZ2p2byyxrBL6-1ENCl2qVVu2wYT4bd7D9QCtWSkUHk5FRK4xTTpN8Lvgf_w_KY3THTk7x0EPOoIro0sS-O2rhPKB5Q1044Cu0GfubMpSN5s1y5DvfsXu-qsjK38nwP7iPzOkD9rZ_kXC1pqY7DtHpHOp-wN5t5HurVbeBy4ioa9iUODvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KyWrTXryEQj3M2qz-Bm6fMvDT2UPZy3YWZrZIBhcI6ZmYWFuUiK9C6wRthJpuyyl5bdt1WK8fzA466-_2fyAhr6RXks2GUqdsf6i_fvxC_h93mtA1_jeHq6JZp_7rIb_FhOUF0DnnRiv8RtGiRxj6n-qiZmiG99kRKPIXoCzQlqgkobHbfSkSiJI3QMG55XtbTopS12qI091-q9zNv5jgK-xlwuZtmxcUW5QabwjzKISL3QuMPQnrogRkoew_OcvKxN_iI4iqIpm6F702MK0zJ8sxNp-6Sps7vj9gZ_8U26rvCdNSiwVFTTaeniN4C_mr9RmXxinRUhkggcNcs1rvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cAsu7q-6kWeoc29cCJQ6xS8uxMbqZBE0ZV6kOBfbiApfYVpykiQpnWAlAbHWQGwSDNEShj6V7m0m67_op9A7Pei1rpggNcG3-9ajCntCxTfamp0LjTv_XfIeGd-zRe97XNTWoAN86DQnc5DCN4vcbfV00mmlNOuUrar6l31RNtOHToQTzFDcczyslGh53CXpNVQAtZi3WlSs5-SDht3JXRqyYpaG8nopOrsPUyiwffVluHWfjUACy65ZRfXRd56271jwhrioA1IWFgPD2coF4Ve7Vdxlr-M_-OOxAwpF2YjPqF1O_Jy1mJWkF38gDD-MPJkpjx9G_bVV46oJxoYVLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
یزد در سوگ حسینی به یاد رهبر شهید
عکس:
علیرضا رجب‌زادگان
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/444657" target="_blank">📅 10:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444656">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
هلاکت یک نظامی صهیونیست در جنوب لبنان
🔹
ارتش صهیونیستی اذعان کرد یکی از نظامیان این رژیم در جریان «فعالیت عملیاتی» در جنوب لبنان کشته شده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/444656" target="_blank">📅 09:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444653">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad9dc303a2.mp4?token=IUJW2q2aTEOz7-1yPGK-knjN4YETa20erGr99xGx9E30hjs8oVlDvwaHf6dTAlS6faJNdALxd5Zh25C_VBbzenYoAbTjxhyT2NQKqBM9eiX8LdX4LqkDRpDSYsFWOU5OX6YihtkEy6FQS_D6QYZ6aPQGnXeftnRLDbmiJyKA2eIVqs5w42ZH-PRwgQoXXLzFrVgFwAEOETro8haKh25_VyyKtiZZ9uGujZB0cVTM-0hLOrux6zjYzEKyduRfD8k52QyU0yNSzVKv4n_pt09_aq5nCTn95eGr73HlDNHGWWMoj61C47AdCxRk9v0kVqa7vDFLuOvodGJYx2Ymtss4J3o3e01NFOjycBQ0Tb5qQejjUa8egDAcPEOv6kIr1GicWFWW5QT_Stt4J-bfoLxH2Wabu9YKMu4Lhj6fds8hJwnPzVoPjZ5TcaenIuimRjgCzZrzBv8CzfMSQSwHRT3C0HRjebVRwp8uP72v-FHHUmk67AQaGq0aw5EK1cC-VCPwS3n3kUurT48xF-O4pkcTGV1J3tW2bn0ZKE9YYd0Nj0cytZMv3G3DshVDOM_R3Fbu8aPW98iIUn4pXOpmovONzB3jYNgv4ootbrP1dKEPsnkM3MFrxvuh6UJ1D09-S7zfOI8Pn1gPJsjNm9on6rFQy_lQwOBjh9ltV1vlzneD_gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad9dc303a2.mp4?token=IUJW2q2aTEOz7-1yPGK-knjN4YETa20erGr99xGx9E30hjs8oVlDvwaHf6dTAlS6faJNdALxd5Zh25C_VBbzenYoAbTjxhyT2NQKqBM9eiX8LdX4LqkDRpDSYsFWOU5OX6YihtkEy6FQS_D6QYZ6aPQGnXeftnRLDbmiJyKA2eIVqs5w42ZH-PRwgQoXXLzFrVgFwAEOETro8haKh25_VyyKtiZZ9uGujZB0cVTM-0hLOrux6zjYzEKyduRfD8k52QyU0yNSzVKv4n_pt09_aq5nCTn95eGr73HlDNHGWWMoj61C47AdCxRk9v0kVqa7vDFLuOvodGJYx2Ymtss4J3o3e01NFOjycBQ0Tb5qQejjUa8egDAcPEOv6kIr1GicWFWW5QT_Stt4J-bfoLxH2Wabu9YKMu4Lhj6fds8hJwnPzVoPjZ5TcaenIuimRjgCzZrzBv8CzfMSQSwHRT3C0HRjebVRwp8uP72v-FHHUmk67AQaGq0aw5EK1cC-VCPwS3n3kUurT48xF-O4pkcTGV1J3tW2bn0ZKE9YYd0Nj0cytZMv3G3DshVDOM_R3Fbu8aPW98iIUn4pXOpmovONzB3jYNgv4ootbrP1dKEPsnkM3MFrxvuh6UJ1D09-S7zfOI8Pn1gPJsjNm9on6rFQy_lQwOBjh9ltV1vlzneD_gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هشدار سونامی در ونزوئلا، بعد از زمین‌لرزۀ ۷ ریشتری
🔹
سازمان زمین‌شناسی آمریکا بامداد پنجشنبه در پی وقوع زلزلۀ ۷.۱ ریشتری در شمال ونزوئلا، هشدار سونامی صادر کرد.
🔹
تصاویر منتشرشده از کاراکاس، برخاستن دود و گردوغبار از مناطق مختلفی را در پی این زمین‌لرزۀ شدید…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/444653" target="_blank">📅 09:04 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444651">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa81eb74a8.mp4?token=g5Bn124CviV5e1uO7Cv1XGigH5m_BvflxkLGuylp13MdIfHTI5d5Hpzt87-yboK30QfPgMv_wtphCPdPk5aYsaNBKvhdBVrO-prlZkSB2rAr3ciG6jmjzcRQ1WFo0U3VcSLBYUE5ZWE_pKFIaT6k9rOFKCj0LdAJON8ApifNnqv_MXI4axfN9HGnp9ctExbfbo-rMN-yeIYVPyG23Uh8LA5h9dlfIfpFLjVtNX4T5bOwBsBLR8oW2uz2SQR2z_fB-9mmuqBk7miI_-Mb27YT5ste6AHvUEg1Qk2oreF2lHbvKhyz4_Pw9S_Lnx7rFlOJ-Bou5LFLNFUJzDPJGrF1rzCStCzN1i_KrsGDCglW9XC02rVnOOaErkfHXWIEerR8tZ4xh2YWetm8yruAlMjMnM_gsEhukBczoGvM1vOBIRplJctaZp3xea78VGeZh9YFvM1h5UOVYmp2aQKrMPH9cYf4XoAovOklfcC0d3nUI41ERjeNKk7Dz3u6r6mSkgHv1ZHnBiQH0uqwYzxQYSe1qa_qrKlaLxkQ7bEmdVeDcgeQ51zQg8F-ROHnvuxoWE9sy9oE9RCBTiSCsxb3VVwZJk2NBW3mY-mj4NZxmU2lhck-yktk7wFPxLrlBQUC0hLoT0xORbvCZvedPo3sRL3iXl73p3Cu4WV_4LMCsZbGIhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa81eb74a8.mp4?token=g5Bn124CviV5e1uO7Cv1XGigH5m_BvflxkLGuylp13MdIfHTI5d5Hpzt87-yboK30QfPgMv_wtphCPdPk5aYsaNBKvhdBVrO-prlZkSB2rAr3ciG6jmjzcRQ1WFo0U3VcSLBYUE5ZWE_pKFIaT6k9rOFKCj0LdAJON8ApifNnqv_MXI4axfN9HGnp9ctExbfbo-rMN-yeIYVPyG23Uh8LA5h9dlfIfpFLjVtNX4T5bOwBsBLR8oW2uz2SQR2z_fB-9mmuqBk7miI_-Mb27YT5ste6AHvUEg1Qk2oreF2lHbvKhyz4_Pw9S_Lnx7rFlOJ-Bou5LFLNFUJzDPJGrF1rzCStCzN1i_KrsGDCglW9XC02rVnOOaErkfHXWIEerR8tZ4xh2YWetm8yruAlMjMnM_gsEhukBczoGvM1vOBIRplJctaZp3xea78VGeZh9YFvM1h5UOVYmp2aQKrMPH9cYf4XoAovOklfcC0d3nUI41ERjeNKk7Dz3u6r6mSkgHv1ZHnBiQH0uqwYzxQYSe1qa_qrKlaLxkQ7bEmdVeDcgeQ51zQg8F-ROHnvuxoWE9sy9oE9RCBTiSCsxb3VVwZJk2NBW3mY-mj4NZxmU2lhck-yktk7wFPxLrlBQUC0hLoT0xORbvCZvedPo3sRL3iXl73p3Cu4WV_4LMCsZbGIhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی مهیب در پنسیلوانیای آمریکا
🔹
آتش‌سوزی گسترده در یک کارخانۀ قدیمی، شهر آلنتاون ایالت پنسیلوانیای آمریکا را به‌طور کامل در بر گرفت و مقامات محلی از ساکنان اطراف محل حادثه خواستند فوراً منطقه را تخلیه کنند.
🔹
همچنین به شهروندان توصیه شده از انجام سفرهای غیرضروری به محدودۀ حادثه خودداری کنند. در برخی مناطق اطراف هم بهپدلیل دود غلیظ ناشی از آتش‌سوزی، دستور «پناه‌گرفتن در محل» (Shelter in Place) صادر شد.
🔹
این حادثه همچنین باعث اختلال در شبکه برق منطقه شد. براساس نقشۀ قطع برق، شمار مشترکان بدون برق در آلنتاون تا ساعت ۱۰:۱۵ شب به وقت محلی به ۳۵۰۰ رسید.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/444651" target="_blank">📅 08:46 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444641">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WKeDpBSrtY35hRJmoW9Im_ODuTfiU_9ajLTzkfvmtW-ktPT0Kf73cZOmekK8-NAPoFHlEdJeP2QASMKFD8jhBsXd_AhpbrqZGMS6WAgx1l8cjHcTfYUzFl1eG87MaV74oXGNtsjX8m9rfk4d8D0W6OgGnJC3R7Ku5SqdRLhP_QPCnVteGUG0VetTzPlYHWrd2VDU5HoeBk4eSLyW_JLIvHNbukcdX-OEkd8m1aNPB_zsN7I18vk5hx9fR2WSNqAxYa94X0zMgbkVWbDQLzspel83NsCaUl96KEQdr2gczC3hOnqfCCpq6mn8_CxNCB8esjiYUyJQfZzd0a7g3mh9sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jysM64Q6cWcWFM0pCNh9E5f8PrbrC_AYflgWcKBGqMe2fKIXkwqMx3kO_XII_5jbB9kIVdq9onGZTybLBcRxbWNrfSCWwNkh9ivkrQ7NudWMqq3FXQ4inUae_4NIzmyMBTAdpK5JPTfvQk8blD0uOFfagMbMevYSBzSOgm0K0AmvRjlQiDFQsUFpHnjRs20U7J80nufFC0DORLnYaJrY1bUbIBRK9K4inntwM8Qc--O-a2h-YYyhNhyaLEv4syr7gK4y69i76ZT6GDNHAjlaAPH8IaHX1kjMd0_KC5TXISbzeaI40d1LWkUw9luaZgi9cmkOfIbhuVbHskLudab-Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M_yIgBs51g2545dah-cPCwBtSeNge4lH0Ac9f3OHLcJuODRBQjhpBkhfahFrGCvYxKOcPlTFN_U5uL23prZTYAPUjscOUG-qQa-ePLkmVNvoeGvYi83ByfS6RvBYMfluV8Bw9prKac2BZkOQ3zdebe_HAgyeXop8mhDJUTjkTCdQgCuDYtRczfW8Alq1Kww6xN5tOTEkY-qzV2DB00LOGxschYiOAPXu4p9eZdM7YG331h7aem8rnBZAyD2p3Uxz-hdaxySFb_j_BzJ8DQA7a9lB0pB1DkFNTOT6LYdyrIUMcU5HevU4qMIXzIxAWpMFQOQhXfKgXL3iOCsJN4pN6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jzFWZe58_HYZ6qKS9Q5OfGsDFldTWUvNj8W-rzqhwyWA3tUQV3223fOT-fYuU_WEgiQyMFw-ipatk0c4gyPLiwcTcBmA3J6gFoHNTSAxDIxp8DMYiXCsFxcjGBgAQNt-6ysmqBPvMkZEoz4AcsIkrL76JAQ8qCZwOnRJUyChv2tN8pZ0cXnvKWJ1td_SwlFVbOARnQFXGkgzADtK-OKuboz-8WmZNc0W4FZbDYsf8he7qziPVBMMF9liFpPTDCX_Plk4yP04zKrgzrEfB2IUqgi9Qs-qGiPfW-0Sb5PiQBZ_M1VbQVTrgFW_k-tgjUSqIcsVw89bPQj4eH2UlXIRdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vBFJMf1KG6_oETjWx1-MZji7MfwYlknw1LOb0VoK8DdMB-hDhZwDqhr8UEN9Tk3svxyiw488enSCznELZ0f7i_L21glZqUs26J1lwcOfpsCgKyUb9CUQAzRbZ2gg-GdpkJqy6N0UzV8IRfCTzh3fMauf7kxJWe6cVBvMpvqa3ROJabHZt14ju7HG2Gsb3In6nKJ_dfknc1bFnxwB0QfpBSpCG2OjMC7KKxespqM9MkcJhLF0Voc6rCEr4RjrtrP1PD0Wzfzi8aWljC7r_xAcSaZYIQJgE4Gb2xYVkrhI2dciZmiDLpoPxBRxhX8bMNAw-5G8LYnHWewujLO6wMP61Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MJlg-nHx7iPDbNHHey7IHEnk2HEvMxsoMomZtkGFE_nZZCZ-IeQiMtBQJIqxFpApJBckGuSWOo_gyB4Xd3nyO9mxt6Iuz1ST_TZIlasxR5wwWo0gTNJQu73Ek1_yCR2o4OBhXlkzq6Rc7nUmxLCQNAdh8RFwL8FFhqsRUesf4N-TKasgJYDKM1ShxtfMsbEi5SCrkczkJiYl55oxZCgozlZB7iTH76O16Ro4mQR2tSXZDztAcdy9bdKbIo_IZ_f_AETnu-0-2Qv7mzVMkh2a6w85MaJyZgYr0TfQJww1dUJAOL5iBu6HVvndUSp7zAa2irjIrPoynsRj0-LrTuxtwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b1vzmhOpEqILweZEABxZs9UAAP7bv4nVL0z7f-EikeTjv8Wvps0IKaksHWY2nwpUq7TMFdHAGBhjPTRPbykYu_UKl2b_4CbyzHzE-eZ1ZG4hZFLHLz53yjomsHtg7P-IkKkPErFHbrX9h-C-UdvE7bnwZqCDhrHWyrwT4It8YwYr44MneJ6vAxgFu2X9MeYiwt1c80sFOQec89CK64wRUUZ6TFY95Iedzk6HO9Pmdlwthe_6FM484KuXuMzLPO6TeZWPx1zlJSSfYwfQx-hxFRMdbsPNeuO-BqQujl8k73QVBPWKW2GQVTqUVoS7q00gqrTnw1UfG-c2PK9ID0sXSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OpP56mnTYgRTbmq9TTfFcybwjac4pjf79wz0oJ8_ECWSsgnXbz7RLEyVJqsP2DYpJ-NPJaj8DQmu4imsNOgawLm041fZiLNyDrHb7zVAcPNuBjeKglxa-Js6RFGmaO5BYMng_E3TdEZuFk44z7u7Kj3nllO0yWe-K1pEquE8RCwANLecoEx_y99x_0iNUX5LwfSvTxfPWHiWtdRcJkNCuRcGK299B6N1OFkokIWLT9CsoESLqoikV64V80QF9qxyvU_QeI9y1kvCk4XBdfOLarlHJm0cy6bYe8Byf8_nl7OGP6TF6Y29F5IHavdDFlCuh32zoJSJQwzMVBtA2vVIdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pwzzvuDyVJkBMSGnE6VIWjFJ0jn2WiJJkqU_QPichqxLq2eUyXusnbDEV6yqkwb_7wJeg__RXUIu2Tp6bXzaR1O_WmdmsGAZ8uJTDBrtk8cD_7E06pU2SKzD84ymaOAiEdIO7jr89Nr-YYAMlS8CMrT89pHPAsZWMR11NHMdKH5eM9Ew0_pwxIdyEKuHvUo2oEsFz-wzbpsN03yJ2AKvazFKdTNg1BepYxFw3Z5eLNpgmJqVMEBOCwJQ-9_oe1TTdiQxVOjTITYadccDdHGk3p3HjUEHiOVWk1yTk2o8HZHKTcfRT3-aB5aaXEPCg5iYJRnNizca-k8RfAmJmP0Hvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q7pEUextoY0IJz-0hIH6iY7EX2CP7A95NANUfow7bMSxcAx_SfwphDR9FaMLkVDBUyNhEcMoskWxa2uW48D1GVKxsvfhzqSDIAoSzdxLECvAVV75MPX2KOJuS8JJB44CphFlm6K5EHEVo-tJr2ei4QphQ3slBZGjtOwzgjP28bN58FFgvUTxzYWY_WofbTvKwEXMUfhCmi4hDvX2Q_7nCIASr0JgU_dXCo-3ju69myb3NtYbQwRxKC0ngsJYO63LgwlZ3oCdvy_dCCfZukHKHOqe8S3yZALlPg5fOyEq5WSk4i2ETYvBvl08_ApzEFKu6cefDs42Z8tW_Vq95G1qxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
چشم بر دنیا، دل در مسیر ولایت
◾️
محرم، صحنۀ تجلی مردمی است که با تأسی از مکتب عاشورا، لبیک‌گوی ولی‌فقیه زمان خود هستند و گام‌هایشان را در مسیر ولایت تنظیم می‌کنند.
عکاس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/444641" target="_blank">📅 08:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444640">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WF23wf9rIW8HO2ISd6CYgkBPl4TmChQnm-zeUMYPeL5vKEKQQcHtHe9gUyqJLOB8JprjM4b-KFcDQKWXIv_uM4Lc-kjVQgzD21oKWiOXL5sci_5o8sH2iTJ3UJYzOgoxZUsdtGKD2evoQJ9BJkg4YcQu4-LjQ0UYZ7oWTEiKEFZVVBz7ZE1jQRnL1GmwxIfGmltAyEJ5UrFgMMJsjR11Jk3Ph9KoijiuBLelKHoRMi6ur2R9hae-rMAHZ-Wh8bVwUIEMPN4pd4DSy9Rlyon2AbBCr3eWv-dldvbl0zRff2ibcbxRIw7Ir1tmXRIXjCEq_lHc98wdy-XBnW59vkugDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر نوزاد ماهیانه چند قوطی شیرخشک سهمیه دارد؟
🔹
طبق اعلام سازمان غذا و دارو، جدیدترین سهمیه‌بندی توزیع شیرخشک به کودکان به این‌صورت است:
🔸
کودکان صفر تا ۶ ماه
⤴️
۱۰ قوطی یارانه‌ای و ۴ قوطی غیریارانه‌ای
🔸
کودکان ۶ ماه تا یک‌سال
⤴️
۸ قوطی یارانه‌ای و ۴ قوطی غیریارانه‌ای
🔸
کودکان یک‌سال تا  دوسال
⤴️
۴ قوطی یارانه‌ای و ۴ قوطی غیریارانه‌ای
🔹
همچنین به‌منظور مدیریت توزیع، در هر مراجعه حداکثر ۲ قوطی شیرخشک به متقاضیان تحویل داده می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/444640" target="_blank">📅 07:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444639">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CC08bZC8Y-qnY9gBJWDATe_gFuJsaMOZsKTPeZt99O6w6UGbjiFBcDkFGXZ-sGOWo6zsO83YnxVnnGVnGRNjk8FIF5QwF7IbgZEQpD0LaZaJZuIbyF1EKOJ1ev7vTS-czKD6kDA1qb9B3n95VSg8KkbeF8YWn8mzIZttK9uNJ0Kyx8xv5ZZ0DIy96eePE2hnMN13glf8t3HK5SfKGE_JehOV0ikr94zuS7BTPctsDOvxxdEltFiNJ3Kuiv0B0X8diyXONcKxcYIgniO86QsbNSzmK_g-7jL70w9Orsz0kr_v4oEq9-1HHNb-2ut1Ow7AIIIAl49-ZoWAAOEQxbID1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاسوعا فرا رسید
🔹
روز نهم محرم، کربلا وارد حساس‌ترین مرحله خود شد. روزی که در تاریخ با نام «تاسوعا» شناخته می‌شود؛ روزی که دیگر تقریباً هیچ امیدی به پایان مسالمت‌آمیز ماجرا باقی نمانده بود.
🔹
در این روز، فشار از سوی حکومت یزید به اوج رسید. عبیدالله بن زیاد…</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/444639" target="_blank">📅 07:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444636">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZsyZ4c8x5uVBs6XdcLy0Ls85vnYyp1iAX651AamcNFgenf7wbiZAseIcN9-bOIfG8CaHQ0--9oY0e6qyWK8FJorSvhn5kv3Xj93fh4p8-TeHJWC17Ups5fWu4g-9Vz8WS8kiKjxS7N4HnXDdCIgwJsguICIRBdoGyV1NW0_Z-xVjhoMxd_CztSo3sk34XCCqPUk8_9TvjqNjU7aVYSVh6Vd9zwwm8dYtBMGRt3_sKxqCiM7PeQKhANXcRL8mJAD8lijAnvQTiYQmA_j6-iomhW6lk-p6zu5Pk4bbFPp0BZXUdJa7Fq315-_q4wSuAzG51LUyoTIbL5luC06poQA6ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RszkKjPLA8LA7r3bK1OLy0_7QPHJHjj1SrNN5otjhTf3t9_CKi6oeO9uuz_ScWNfA8XDQzHlMF-fXnONntKCsdJ88JKDcz5rj6sIUnnmyUUboUuXWyvJJs2jJnQjbovs8LZPmN45UCT7175lpxe5aBFE4OzGp2A_4kRnEGfKw_xn37lQ0MWHayK01zrWHNWHvRooO-g07I9QAcXSZkmnlBkT79xBgwpaHf7TxTsJbSz2wR-y6npaDnGoIAa5jGjGF9JZjBhZbvED8Z7GluM1TQ1f81af1FxE-iptmuamNgD5yZQLbL4dCyLYxgrhCrkG5tBRKhwbOWZ3ZH1BTj302g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HwqQzMGnhTZ85GsIpWnwwWmm_oN0STRQrsSOV8Z7DLOZzD7hwYU7AfWq136PaBtTt7WdDlnyzvilCDPqhrdOegYD0jnRMY_evh-yGewaCUBzZlCRDunzg_qpv1Bf2eSOtxiCpHsi4Vjoekdu_Xcc8OGV_R_T662iIq2kOtePcvnJR8U17BNhXMfJ6vomGUW0tQ3unuxqvZKa4A9_VECdfs5bkcw83uvma8-lJ8gXdnpyih7G26hYGME975BxuCqede4pwrffxHo6QUQ9KELvmMBzHNOJfDjbakJ3zKb-hH1dDvC3bgp36S36v8-ZRslTO4sheXRyW74ICMqHy8l5IA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
اعمال روز عاشورا
@Farsna</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/444636" target="_blank">📅 06:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444635">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnGnyX-jjmLJ3D66SnRqKY_dmABkce6LtST2pmI5w2ppj8AnriSSL0PLRySVTfLc3DAvS6fBbLzxFIHzGUEgz1aIW0Itn0j-O0agEgrqoLI_OuV-Fjvg7Cgk9wv6-6glv3ph9f2sFotHrRocmA4kmCPz-NMe4zXaukEDsFbNpSCc6P8PKq7KeD1b4VMS912_XjiLkmAppC98QEdO8lfgulfoTfDmhbOaD__gk177g9YYBgn14WKIXoTkydMuqecr-ksqwuyTVFlX-wzIeBaBhR0TQiZzXVmZysYzfKWIfJf1_A-H-bS3iHX8ZKi9IWIM50AzRqy62sKGljHCzGfmsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکست کره در شب صعود مستقیم آفریقای جنوبی
@Sportfars</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/444635" target="_blank">📅 06:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444634">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMewC7XokhiFojije3nS5q-6-ml2BWBWIpf-Vijj-_MYKiRC3Fd4VXAu9j25ZL2igEYQ_o4CCzM0OXuI7tm8gPJ2wLnmE11okN9zopw4IZ1RIoIHqqLNLIndAnbcJxTCz7b7WxYUcfpulg7gbycWHZLxlW5J6wjMEuh9XXvNnhKATWI5gWaEssxIe24UO32ZNuETeFk7fRr-oMjZaJNqnnp9KgleIp48dAcvwB2JrQ3pVqefnZA_q2TWPZhPeCS027-zSxCVOukaLVf-JHBIxaIvsn4GqAOnXE6bjY1exORG385v84kZRZzXP1zVReWluOHFQBPdeVaGACI8SVbQTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشت «آقای قاضی» با فصل سوم
🔹
فصل سوم مجموعۀ نمایشی «آقای قاضی» با رویکردی آموزشی و حقوقی و در راستای افزایش آگاهی‌های قضائی مخاطبان، به‌زودی از شبکۀ دوم سیما روی آنتن می‌رود.
🔹
مجموعۀ نمایشی آقای قاضی یکی از سریال‌های پرمخاطب رسانۀ ملی طی سال‌های اخیر بوده که در قالب یک درام دادگاهی به موضوعات حقوقی و قضایی مورد یاز و موردتوجه مردم می‌پردازد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/farsna/444634" target="_blank">📅 06:05 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444632">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a32654de0a.mp4?token=cmUG8RtuEKdt86uUOb-TlulTg8wDZU1HnGz5Y0s6ZiwcGQRpD-x6EA_YDDu6hJU53Fo34S8ei-zj6Jh71IkIBaIzK13PuN9-T_dpMZcqQ63csGhFkdorzBd0s9MxeZ2VcVEqhG_UMGID4fl_b4k3J-YxYr0Joyj8Iv3xzyFVt8KoJM_9IBQPydoIrVxWTSrXUqZBMPw92CvkB48wUheyeiQi13iO0FWMKW-iIvyutP2wENrHmE-bqDNR-Mg8hQc2JFPblM1DDj3hgbWdJOS0vQcUOoCP2J0ha7YvrXdH8M1yYeDHI2RBY4ol2AdjgUdaqeAy60ptXEoOZA0o6679Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a32654de0a.mp4?token=cmUG8RtuEKdt86uUOb-TlulTg8wDZU1HnGz5Y0s6ZiwcGQRpD-x6EA_YDDu6hJU53Fo34S8ei-zj6Jh71IkIBaIzK13PuN9-T_dpMZcqQ63csGhFkdorzBd0s9MxeZ2VcVEqhG_UMGID4fl_b4k3J-YxYr0Joyj8Iv3xzyFVt8KoJM_9IBQPydoIrVxWTSrXUqZBMPw92CvkB48wUheyeiQi13iO0FWMKW-iIvyutP2wENrHmE-bqDNR-Mg8hQc2JFPblM1DDj3hgbWdJOS0vQcUOoCP2J0ha7YvrXdH8M1yYeDHI2RBY4ol2AdjgUdaqeAy60ptXEoOZA0o6679Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادعای وقیحانۀ وزیر خزانه‌داری آمریکا دربارۀ معافیت تحریمی ایران
🔹
اسکات بسنت: معافیت تحریم‌های نفتی ایران مانند دادن هویج (امتیاز) به آن‌ها است که هر لحظه می‌توان آن را پس گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/444632" target="_blank">📅 05:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444631">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
نیروی دریایی سپاه: عبور ایمن از تنگۀ هرمز تنها از مسیرهای اعلامی جمهوری اسلامی ایران ممکن است
بسم الله الرحمن الرحیم
🔹
ساعاتی قبل بدون اطلاع و هماهنگی با جمهوری اسلامی ایران از طرف برخی مراجع مسیر جدیدی برای تردد کشتی‌ها در تنگۀ هرمز اعلام شده که این مسیر غیرقابل قبول و کاملاً خطرناک است.
🔹
به اطلاع همه می‌رساند تنها مسیر مجاز برای عبور از تنگۀ هرمز همان مسیر های اعلام شده از طرف جمهوری اسلامی ایران می‌باشد، و تردد شناورها در خارج از این مسیرها بسیار خطرناک و ممنوع بوده و اخطار می‌دهیم از هرگونه تردد در خارج از مسیر های ابلاغی جدا خودداری نمایید.
🔹
هماهنگی با نیروی دریایی سپاه برای عبور از تنگۀ هرمز از طریق کانال ۱۶ الزامی است و با شناورهای متخلف برخورد خواهد شد.
نیروی دریایی سپاه پاسداران انقلاب اسلامی
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/444631" target="_blank">📅 04:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444625">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/efd-6oMtKzJdAfX-Y4_KgSaF-dGpit-mXRE0y0PE8TxYKjqJdq8tSwXfHvPKjs-XZ25EzKK65WhN6suEc714-Jb-gPNCT7klscixpECJ88p0x2lbAuk9gu716LDcVy02oDFVvpg6YoJLK8YCLHRg0kF-pLY_kLZ7B5_7RgtaRqSIVsfL235A9wuG-vAxtrhxJhmSPGOXF9JRC-ByxhKtkBSLmVno0j-c7mm03j2QNxadchQePO9ipqbEJpL40ABqurEZc9HcEx5W2ywZaDWttthL-z8SvKqjF_zNld5LCjl6b5ftma5i4KJxN2ZfNKle_vrd5QPSBoFfM6l2l1W7YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lG7j89r2alOhQm7CkkN0DHXNWpXsbrMnQ6ghde7eKTljd-fh_T04VBI6IkU0UqsW4iahicxM7mmxCKgb3axkMBuLVPprgVaEBFq7q2WVqs27TcluJg4fD6bkRmT5tMuwB4NL9V4QaruHCagWI71kPxYwlaAEn2vN1wyW3NFL-8JPQYj6ujD0Y6ZedGWYbox3hB_sbwgYV56oNZ0ovhVK1NQvqgWd3BQ0qYPgJZ40XzwJ5TMuWnj9ZLzZLrwz_7HIhTucO_h1zBlFA9CdvaAcJ6wXXqm-7SG-OXFRPg5Q8KXYhfHT-6IQQsAV0MOhF5rq9m5W77DbtP3jgnwmRDM1ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FqgWkDXuaSjhjm8nGTx60_gmS8nG_NlccQtYjDkGNWAZAHqWBfC1wL_MFOMsZVBilkG1qWI8_Deh00MlJh6ZqtkSPZF4-2TiAuCyLWHzWTgucTYp_EAsaUnxh2cuyGbPuU_becqlxD0qi5OMRZOGwX0qLFr_VCMXbgNNx284AoxthIYhbMp6sZao2DmrGyZ4LBR5lAgAcj1Ax-18qctKhKtBYulmeIp4i66cC6ay7KPPB3NQKREyg2wb6VU6zyAjqaJq8sRzRkIJIApbvMqCPWCrBYZKP6uyGzBmkqU-ySmAeC6zIyq6-3JWVSG082HP93iRpUn5TFzUCCTVE_XGQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TDSZ8bHMtaLhXnK4Y8UckwYJv6gOl31il1nk5uHaE9WyrQG_JMWqRQ9wzorHEZAF3fYOEmjwv0LfrSPrSZXOyrHYNHbD8BnY-E0g0-Kkx8QQZ16ROQh6OIMmArr0tQKjwzD4aC4zb4WUOjjhtTXOF2a6ufur825ij8egOXE4oEf0dUwwneD5OjPNUTnhaAn-S9YNsLt1DpwCW3WjX_5jsZraqcI54IgUQ8dal_uXXZ94w9k2UNAeP0DNpXn5pxyQn7gZLE7l66VF3X46p3dgoKs7xJ397pJDaR9eAD9-h6RDxxWtxl-6aMc7Yj_kbcX-celFWPpCVasrYYAEMwIsgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UJ77MRWgSA1I1An8xg6O0nKDU0j3UxSMQNZX_u7poObtC6v_4vLp9v4dShTTRZZXMFrgtAaoLcu-MPyic4p75KO6NYXMt3wb5uqXn5xVVhSw3a02KSrKJ8P8gAAueEQHmpT4bS25DlZvYU3Fee_-KzOY17i5nt5kxMf8quaI1HrzZR0LOl7IWoNZv6lbBhopiWkLcptQu0PZChEk816e0CSP2XNtN9zNqgZctrmoNqvYLPHWCqHFREDLkEHhP69fg3c78Q3Bk-o3F8NTv0ZOWBvrvGf40kjm8vN70FOAFZ9X_Tyjd8q4FbZ4nCNgLScPOMqUZZObzn-meLwmm5yDhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jpIKFGaLqMgTWG4-qhVdl1WG29TRdOX26ywJLGQEmZLXPgAZS43LM3DqWu-78FHpCcetIr37tJT9V65KCkBOj4481ynmUC7cT5Q59ZhGjI0e9ho25-ued6Tp7i1CbkDR__PkgLThdZ5XJMQNuPxGk5lyN3oKYaS1OtbxqtZTsTck8ueZSpUSJMKsLkFlCwY_36f3fnO_smLe7-ujKIv5siVUh53EXMycJQInQJbbFz51M37rjRK6qOcirDAv7blsfQswyAvYl4X7ibGnW28TtutT8qZh67spCweecoRLlUdT-ADyqMQWla3V07wd7RdJVzpwvHtnvrW7fET8wKdWcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
قابی از خطبه‌خوانی شب عاشورا در حرم امام رضا(ع)  @Farsna</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/444625" target="_blank">📅 04:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444624">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">آمادگی ۱۰۰۰ مدرسه برای اسکان زائران تشییع رهبر شهید
🔹
مدیرکل پشتیبانی آموزش‌وپرورش: ۱۰۰۰ مدرسه و ۳۰ مرکز اسکان آموزش‌وپرورش در تهران برای پذیرایی از زائران تشییع پیکر رهبر شهید آماده و تمام امکانات در اختیار ستاد متولی برگزار کنندۀ مراسم قرار گرفته است.
🔹
در مشهد و قم نیز تمام امکانات در اختیار ستادهای ویژۀ برگزاری مراسم قرار گرفته تا پذیرای زائران باشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/444624" target="_blank">📅 03:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444623">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k--EiXCrjXnv3nsh3bf862R_cnT-1NKfS3_QGLiqo-40JQiHbqULF153VUtHsSmHM62-AZahF_AIIFk97I9qnZuDPF1PjHZwDPntAj_cIISpAc0wivYRbGtWea8OngvibwTa9Bpb28r8X6qivVDtWIuvQvq7KpQ2rs4ic-NUnzUWeNk3yBcKi0fT2LPcNi2Uj9UUKoJSjIDiPrFVpC-oWs0TVtef9xPioXmh9Xm7DTTc4CiffhIZFp52lcHdyxI4IOS-_LJnU7SaKwi7Hi1LOKLe7aeTjEnQQ80C1Hxz9IWZjBocPYXaaMC32xML82qSXeRVrbvLverE447PlSdo0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیمار آمد، وینیسیوس دلبری کرد
⚽️
برزیل ۳ - ۰ اسکاتلند
@Farsna</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/444623" target="_blank">📅 03:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444622">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2hAKbHss8i3GJAD1AmXtxjuBdBKzP8Y8DjOgGNWR6D8-NgtSAdS7dIv5f27vUIyQDO0aktIL3Ye81bRu5SuzLqikgtWcFBAIJFbIQI5xZnAPocdiHc-OzfWFP-Nlq8UL1fjFiPnDvj8WacqdBzu9WjtaHiVuad_Ymi8MumvgRDWoTOWEApD_vGNSyQ8OS7amic4ZZ_cdyD6s3hVUIh-Lh3brwhYp-Ehf5Vx3pi7S_0lJrr1Y6Z7LKD5Hc5DCv0ZTF_BBp1tVYzkKvi3pE5VZtgx54HBhAxGH6L2gsOPjNijDBgjRhJqLeD3GjQQGzOvbqDG0qM5-m2gopOkZnW8Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار پرگل مراکش با هائیتی؛ کامبک مراکش و صعود به‌عنوان تیم دوم
⚽️
مراکش ۴ - ۲ هائیتی
@Farsna</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/444622" target="_blank">📅 03:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444615">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VWcSd18_4TD_-bj7QhKiaUJfj9BgSXf48SPa7glXb9k6xFCplURppRvhhJekMda7doLXNXxxs90RvsUn8cU9pw0PkjgCA4Ab_VZwf1KPcvky5ZNibtZi05jOMP2RQss0fV4B3zuLBf-UCzmHqsBJKKk8D1uX6VxAbBIX_yTa4Kn2fXr7GejjagAooI_zCf3dPJFqZHWiczxgbJkEglizxeTOtaIf2T5ZPg9cDVgQmWOD_3o2gcHg9OH4_ME-e1mKPSsvD5tq98q-yidhFkymZeRKm7DMAdr7Fa215CRUrwQ3pNK1cnYa-iP6z91ZNjhxKGXY5cXbMHl6gl-HEBbltw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/puxgP3D3-NNWmEmnw_uVvRI3C6LHsAb69iPOnNTRHrXB57AuL3CEeNDZH5HP6YtGwbcagYgn3FJk2WyuzA4gXdCK5k2U8FhX53JMkfy3kmt4bjFdbhZY9nOHO8qGG8oOr_1BNmRtvBstTut01BN2sdUkaiJLtk5mDm9KCpTmMgKbmTNYaaN-CBy9bICvkt7dNoLHL1z1-KYtsdAxftTXFtTNs6gqMtN6E2lOcsgzdGctNtO6Rx7HsNG9txF4KdQv95lCCb4kH8IrV5CkQMDM8m8Y6HKRkF1aMVxPZhuQHGDVmVGduTxoo9UV3sSBpThy-RiIakzv4JIdU6-8BjS5ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i0kFCwe4hzo31YDLEkG2h34OFN9ddjs9T-5WqosHv7cuB1X_GXGbx5CoIX3DjhEUpfnOhAXxd06KRyvBsMBq94a6cIBrfGNT7FNQjjsOeU8E0xWGrq3dIYziMU2lYOxUsialGq-SnMED9vPIkgBLxIzqCf9BtU1MTnYqWnohMcV_5Q3wkIjVswj-TyizhjyU-HywXWwZRQ7SLSiyjbJQNwdc6yQ_x88OjTx4dlAcGvNZTGjwHZwtvdUYsP_H2beOXkJGb4jcwi-ygecYYwCEawYfj2QB1kaYte0DYm_m47by0RztK7mQKdIXlj8gu5y9mPOABVlq9xj7-vPuT3x_EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KajbwnJ7sBtduqlkxWABvmH1RAXkLpjjIVWWL9uAaEYzmXbbAsc-tz3Urb1J5ALooAId53mev24zD2sMYMiM6v6se2RSNd5HfUkwCq5Ag7v9U4wD1sT97_eZGItwsQlH260ToqOHRoj2Kz3ae7a9u2-MkYrOzFhjdEsz94uTMQTSzPp4vO2wLJFjuzDIuDQO7_nloxkrh5NDAmOBWCH5l4LUpqDbK_6aV_MTc5mCL6dCJyolRtjweT743eKBgDttrfYgXgUulQU976MO5GjzO3y_nwRK7SO2YMMzHX7aVgSocu1wuoM-MDQhQC5b2LD8ohgdVv5hX5iEG8AoLivXfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZZ0tULMS9OvUGMUgkFwytqiMW5Npjf62h4fIN2X53fcHoPKCfgicuxxGO85j6wnAHZpX0ezUksh1z_1HwdxRUNtWzMCGjF9fl6pJPmxikKpN-s2eFbw-tpoTuJmgJ7pIhR02fC7ok-6rA3j6k8JXMiokfwkxUdNTUjEiSc_4eGdIbWn8jkPZYXQYucwbp1DFLL4Nof-mTwjTVeabjqsyxXCLgKOQEoz4BSlIvq6iwLzsUYuz9-jfgCyc1pDcJOVy5nAGud-dAviflLVGKRv4UUM0iOucnvRGjouKfeoftahc_hfm7H5Ufc5D-6viKEMs7ptqR2qbmizTS1-Wuu6XIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BcCvJ6L0IxJ1MOKaJZU1PZ8fmRqYH-sGJspaW_JpNP1iAMY8Sjd3SKkA19TjsAjgbIloI1j2niN9pcOPU2oacjruHNmQmZn9xSOMWcZqCNigWUy7ZSgX89cdk1MjA5xZBGKo-Lzai4-I5PphRGHBw0avW8VaeDkUilyyi557-3yTlTrhMK6QM_4evZopR3gq5WLeyRWliUAJhF9FRXlaBk277qPYUzHsjs0p6epWSuiWqoXrojNf_FchzDHYrxmC4QJG93fVDfLqbeJnszB-22xResz9kcRmG6SvK00QpT7FMaUvgef7edIFwnp4YUwodvjKmsRJ-aVDfSYe1YkRCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NFiL7dBfaSjw1ZYKhJXDAquKmybBEKp2fdGw6IrdGKw3J609eQxfS2hYwLg4eljselvs_ovZ8wkGqAffZ0x9_vUcfDJf3lviDDpvDxmH8manvV_plT_U9HSiuPB_-N7l7YcmICar7YRKMysJB0oP0qdtzY580KPqCxQS8bLquTkBq4Nfjo4_KprdcRInkGnkePcm6xw3ap1IRIqvVdHc3Buq1yTENro6PZjihbDFxSAVQYo2vIkJYgZ1QmMHhRTVtTcxunplp-zOleeWWQusX2b9u92-WTmbSw32cDvycSlO5T0Jo8x2_ClSZYyzkfFBbN_uyMrP3zZyb3GPI9takQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عزاداری عاشورای حسینی در میدان نبوت
عکاس:
میثم نهاوندی
@Farsna</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/444615" target="_blank">📅 03:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444608">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D-dKehWxkOArKEqYAQaVdOjUpR6A-B3oZQSpsCg7e6fTZXDgPuN-ZNf5h87dFh71bZeLt_HFpjwZtdrq60etpckkWOZrGawjqpoeakUAq9sWvIraDdfiqoGpgktGSwFb7UdwfdUM51BFIfPVJasV6aIzA6m5hIiVfO0N0t_M808qDDJ89kGNjXPUhXbaI1xfRl07mZ7SC7eyxAfXae7kWFqZpvbrQZKUatCzyAsW_tJc5bmEi2MLHWTmuH2pnnPD8UhlsrdmnpQtXlwLe11mrPfPRLi0YM-Wenq9oFSqO9luEs77GjpwOIkcjCKcd7hu9hIVKpSz10HuwEm15rV78g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dU4oj_gMi-eMkYjvLIDKTgcRfiEJkGzfZIRlKQfOW3ZusonipoZLyPiSZX2-NTiLi-SX9IjVBJVseh-Nnco3slQvJBsAKxtaRt3kOZRvPXc04G0-uiYPBT24ktfGpMLjrNWDNXpLr4ARSiu2cKOO9Ny3EbVx_tMwQrs4G4lUj50wP-pjFWtS2DYk0pg93WLYQxlQLhmE44uEL5oZ6rN07b17zx6XtVg1DAD29-XOWN1blyCWSWYFgUyYdoftxqWVNS8BRJf-hHyaLqlYMVylN8PJNs6uO4zD689DTZG7UwgK5Nea0NR0tt04UW8vg3FRgb2ErrfaiptfwpYDmQ4fAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I1C_pNtz0ZIagqwhXUIqNnD9cxUrSOo4-D10Gf2ErGYsQ0e8wPQEMu-frYyF_i8-l0AnPRYgFIlN1F-5ZLftbhShfXkixMtaVye_LFjSNNW25unJn6EInzduzpmuJ6YcxrNqxsSL7GfF3ducKchl_e_X2-eWXvXUj8C7k-zxdB8Cd2oROEjths_lCvDzqrqBrp6jVB04Cg1c8qJB4xd93jxFbpi6GGXPkCokuaH_IujdkXHRJMAXSvRUeB5WwKu2VdxMAjRoMXXPAQ1Uq5tHOEiDFZDYGmySoCBZCAbpnzGyk0jfnY1choAupqFwPLMUlGF1DaXQ8JRPqRwl75hFFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qdE57A9SsVNTL3cR0YbV7KUQXaWA26h_8qiO3GFb35xDz8J9DiEXphwacdYGol782z-C_HIGGUFjEhzFH2hwfU1M4SNro1Wpx9Ky4FLNU6F6Se4JQoqw_rVV2vQG4HpR-sLmpK2FKpwe_mU77NHgqfuLEGFYABzBNGOq4PAiKOWYEbK6t4FT2M-tOzE9GU_phmv2B-abce-ZVO-d50xKtylJy9w5iphILe430eTl2mA7iT2TUdUs5r4riXBB8rVxioURFgbMlNJtwWL4PBLPdoXUv-lKHSYI-IncRWTlNJ9F5KJfLui7AowEh2OuvDgldm9xzihQWp_1FzPgm2cBQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cDiSgAGxJK3bnRcB33aQLUyDC5dv9ht0crNYPjLobAwt3K1TV5uUhUUMhh2P1hk2MHB8fMW07Jp28UU6FgPaJYDUCOH148oi54AXiQ6lriFk8QjOJZLEG-R2Crf1dh5UDIqCMfJyIQoqwWjhHmgvPb1LfiLJinAANylEElU7azN41F_NiQh0Gj9ZcyJR_XMfZCM4Xf6qBvOuZukDjsfG7R3jXfwyJiTzjR-Zy9-MYrAWfxl_AkVslGDX8ooxyR6DaNtYdDkHXdAy6TsU4oliX8Eym3FqM1jPfHeI2nIWAnzsAuQwAYrM3p2jETKVCs3sdL-KE4BfaW2ZWRO5wg8JPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LFBZwqDNiU-n7ucaV-u1ptMgh9BfcJ0RwsRo9Fy_wcXmgARcX4qR5w7eeba9pE4UmJXZckZKpxslst9Z0f64oYuVpc0OLVusf-iRUh1aFGdfdp5PqcC5eCgjT_3h97WONygAEdEHNBGuCcbhMvqFjAXmButVHfhHVK4g5AwSyLtkJj_lLjUYHxZFPNdYLLC3Ymjw8e7RbAOnQ6rCpzS-ZQs5K6d9yGiRELvYyitE0raENvR199r8wvF_M31147nVA1MRYSq0IAtegLT-Vmdgu570cc6FQqoG2X9zvZmsiXFxGJLYZ3fbcdkP2LO5PEt1A8jrUwZLRjn287d68fSakA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UFWvYUIuB9egQV4V3HE4tocZqHGTRmiQ3sceRcQY7O1NrclhQ-v3VAeJ1KGvG6bqvRfbmnK6ZqWHP1cSXE2-8blnMmwRcEfv-Nq08-FVZzlU9jcYdl-gV3Xuws9gEABhBfZtUvVWigpHUSddxTNKiJEjV5oUPEruyzJJ5qnIBx7dSHtvPfXommgCSJ5JTzK8LjTbKx7vidJuwaR87ETnGMWT3Votrm_FCp-E5PhwhxnGoyBtMaMbmc_ZmB4Y6GQDsnvTmrmg1_EydI-3n2okQvM9t0EcDIXC1fyTWQJh8QxMFzZOvIJWK3Aj_GaDDKbcMLqhEptbGFaehgUXGpOuPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم شب عاشورا با حضور قالیباف و مخبر
عکس:
محمد‌حسن اصلانی
@Farsimages</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farsna/444608" target="_blank">📅 03:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444607">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jq2ToIHGBPXv6x6E4Pvdiyrn24hzIybYq9FtYHmSf4Bb47zCqpJFSJAE9LDtijUOYc9VH91Jvh0eUlXmGWz6WLYINb-Q0HZrO81_-WcBnGMSSQd8vWqPnL6Em64bdOr9Y7o-UwoNgjqYUu8tVIsmsmnHUYWkVt4sf4Bk551nKAyYz1MEw_w2x8dJ5jtkU80X_Po_ajAXUdtftEScMI92AUD_gKu8TE1hvxO-JEjA0eeQBYCTVuTCWVULJsk6tZyOwlpdPkM689QgywtiEEFt0il41l8_gM5iMSFy1PbYuk96dDdnVIuculR0Vx2Iilvy7W1Tdo0msGb6ey0tfjtsyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
گزافه‌گویی دبیرکل ناتو علیه ایران جلوی ترامپ
🔹
مارک روته: کاری که ترامپ درمورد ایران انجام داد بسیار مهم است زیرا این کشور تروریسم و هرج‌ومرج را صادر می‌کرد و نزدیک به دستیابی به توانایی‌های هسته‌ای بود.
🔹
حدود ۵ هزار هواپیمای آمریکایی در طول هفته‌های جنگ،…</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/444607" target="_blank">📅 02:56 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444606">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دانمارک به‌دنبال ممنوعیت پخش اذان در مساجد
🔹
وزیر مهاجرت دانمارک مدعی شد که پخش اذان در مساجد به این کشور تعلق ندارد و اسلام در حال غالب‌شدن در زندگی عمومی است.
🔹
هم‌اکنون نیز در بخش‌هایی از دانمارک، قوانین و آیین‌نامه‌های محلی به بهانه آلودگی صوتی، پخش اذان از بلندگوهای مساجد را ممنوع کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/444606" target="_blank">📅 02:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444599">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GEUo5YbpmvrtwuvlBGkXzGOdFZjSf3zPtQ9KU2xD5PXH7fyR9ZiWupR0uEopbVHkK2bCSdu96eMvlwWAitf7CkiSEBXvnMIUidFT3HcYfFmw1aA9cScLD-NTvg7637d5soy1JDyTLoIESaZW1_TEKFcn-SpLerE98kQZ-gDh26UQvOdn14JEnq75zt7t-H11fE8vudcgsEIYw3NPh9C_JS6FTLch99JtpUOkntFR66fgcobwwZjO7z7514693WqfznpgOGtSTV9tkwx-0874xofDOato-uJdKLgnLmuJPe91uobN3hpnG2JMbFjvLnQT8zryQeOgJf1KVZGqpurPFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fAgqJm0LDuhhX78qn1Y0Fw5GKz9FFkBSrHjXu-9LR4f8p_rNPvz1rTUttPGY57pVI2w4ZfqJx66w34EGCUyySY7Z3gkDViimfF-xK9sZFp_XPL75mvUnZBo4NgS7p0Lp2kxAh3SVCrV1Nc9fdssEaNjrdhzbnubjfRebEbY5pQ4ohD2c0rg3e9fnfZSInje4lmovqloKuHJPaMQpsx5nQ4w7w39GcOpJ70hL_SFFQAU3750pJVOIIU9E5xEgOAEOkuIx3SGXtrTsldkzSovqTjjnYoB-8exKedZv1oafUdG7y6TY2nSdPWbIlcfZYB9czLyUEuMVpi1Jdd7sOP3xVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CnMyHxAY45hgzSdBm2GZKLfKoqbqr9lWS987K1qgSkqumRqehMTTSzXACRywg_Z6AXAMXNTa0Zb-N0863qC65fWorF5BWxQ70Hmfq14FRjGlGbRRxNMwufK-7XfjwNkO1qn-CAhegWJ2sjIs_-rR7bJjphQFFqL1nXoZ3-FqtnLGcWosvr7YPUtP598ZW0NPBTvaPL1luD9dotrk6zSZQWrlof17i6dShpdLYApZ68nArQvBwt3kFndSlYQ-kLBj2-1bgyY3og4NNVLZDiB-zk26JWJrOJTOGvwYHsl2mEpK9_rTEFytc52IidHLBoHqAr2FFZWTG2q0CMxAJ115ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LA69y4rgOF3IBuyGlhw4w-r-hHt6UaYU_UmAxfga_4ox0FbDZ1EFMjFQQ2lVuMdKsrXN4QOL0vWyY8rpz0AogPCz5g_TUhVKrMkQC_BE-juM1gwgMjB2K6g5vfcb5i5_BMFApMvNpd_SdUmuwrU39W_jcia20qVP2BnSD_ENgJtBVTwDHPSdYS0SOPZ65orHZpZqCxvMgoc-Jh5sLVP70o5zffimytXFaBLz82_Gw63x_FMiFbOyVzPt3mDALfpfHdN8Vv_bIF3WufeXITuq3J_worgqw-w0EvZWG34iN3TLCeDpTqSYNjFFO6H7go2kbLDyBrddODfLiBDctorq8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I7-WKi9BYEKMNHVfMcmoknwDBMqRdga3dP3SR6GtSwEYC4ZSxYlvXSHhyURBdilA6iq0-MoqWOASP4OzNiN_iioynhLxRREDVcMFLCApJo-8dxtP2sU_yE2w1qylG3LIhx0zeKO7YeyxnFRN3Nil_jNO6lvVUlIh4TDAvMeycxJozqDD-E2yH76fQ5La4rPvVquP2OQlDHfxtSr82M5mhUFaRhvDQQBsN4sc_q-a7BU97WRAOBkXEr6DePUk43k0-B1bMwMsCIHI7U7OWYIW8dkfiI1a34ohb3Q4UQLXi8NWtC6wk74QC_e6aywQnv96uStnzdqi2zXRofMw50p-Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fHPQTPxBMlEcxKTnJ7bZfiMYuHExNZW5tLWyXCMZOOLvJjxD-GTZFZj4xOmgI7DabEvx5-bk3UMvD3vvfNMLKsI6kshqIj78-XYecaNDPIal9_sDMRs8uYuszyKpIVGbo80D1iag7HhrwD0ZvCEIVNW0FM7Uh3rWELFF1jY2y-1vARC0j6aHdXtD9F05V3oyF4Fht92qWUGwmd5nOs1DfTkw9zcNOpiChO8EiOP_pqjm4NS7xmvq_K_QqI5Ep-4ISojyapcY3q0KBWvjGIpTzrYYtuGFcT5r7N4OubRIdG7RItv3T3d2jh_RsdaqofL_vvv48C07sXWH0k022dpCxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T9-rUwNbECarQQRNmen0u56r-e5RfgTNLqkGhLEK4eRng5_aFV043roB0QcpDlt3PUQYV-vDcOwTvqeLLXSJeFtmabrRO5_CvQM7au5P-XiYUQTf0kpNNsnTmCyPWI6YevkJROZTRAkkKtfkhNupYq1o6gYdb7bmJTR_OVt0xodqOshr8VdB-YJXpFD9h6GSZIiasMH9Lo_DxIKQw3EhwXprwmxzBoEM40f2oAAs6LUoe6r0rVL_SfNAH1MqjAkug5tkp0DRsW_SrK6_4edgg9CrsPH0lekbCgr42zn-bz4QiSx_PH1nk3a-ZC8ZrImXYFzYSw86d5PwXDoT-gFAow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
آه ما ماندیم و آقا پرکشید...  @Farsna</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/444599" target="_blank">📅 02:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444598">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79843546ee.mp4?token=X_MwImpuBTh1YkAX9RfuKxhIuvS7MxTbAoWLu9r7PYVHm1Q8nA2XKB3z5AoBPgEBwJ6OqMQPb3LXjxY-k_HDPEIBXqUS32odEa-aMY1YJa3DZG7uDHt_wWWnzOWutMQRDoZ_g8JfFbShTg1xtibN0iYZzmsHNdfDsKodCZAXzF6W_kzcAch1AXiXQgrY0aWIIEp6DUbbjHjS6ToDbvCZimkpTw4Fw89-45du_p3ONdvZir3scXwrX50U7pWs-1bHjovbpO5YILeRSVkCPdNPM0Ha4vFxBkCs7TibVV10ghasWKfShw5fQJljj52USDEENUmiv3XZLSY5qCY_NBfjBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79843546ee.mp4?token=X_MwImpuBTh1YkAX9RfuKxhIuvS7MxTbAoWLu9r7PYVHm1Q8nA2XKB3z5AoBPgEBwJ6OqMQPb3LXjxY-k_HDPEIBXqUS32odEa-aMY1YJa3DZG7uDHt_wWWnzOWutMQRDoZ_g8JfFbShTg1xtibN0iYZzmsHNdfDsKodCZAXzF6W_kzcAch1AXiXQgrY0aWIIEp6DUbbjHjS6ToDbvCZimkpTw4Fw89-45du_p3ONdvZir3scXwrX50U7pWs-1bHjovbpO5YILeRSVkCPdNPM0Ha4vFxBkCs7TibVV10ghasWKfShw5fQJljj52USDEENUmiv3XZLSY5qCY_NBfjBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاطرۀ میثم مطیعی از توجه رهبر شهید انقلاب به اشعاری که در روضه‌های حسینیۀ امام خمینی(ره) خوانده می‌شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/444598" target="_blank">📅 02:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444597">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b20e55161b.mp4?token=MaJ0SimDEkPa30JCwEyMYabZCEo8TNtTG_4KKHt1-v-9-tb7DhqDQf5yvwZNLbTLAkuUiF6tBojK187lrH436xw40yYZeh2g9XQyQY_3lrZT46ZYMAc7ALDl5fHbbpOgU4YICoUtIkAhsB9GPI3Lf6vbYyQpLoIr9YbzDUjm0xVFci65WdPf39o9T0pumgQ8KwXdyXQEFjUjZZ-5iMweFVWl-0waT4HOX6jEHHuOXS9fqJzXvUHx9ke4gb7wBXZIfI7c_FY6N3PrMHDJJ1uWEkg0GYOh5nKNBqNSI5sm53PQ4o6XtKH2WwpQNC8devm4wdytBTXAdzSbCzUptUHFzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b20e55161b.mp4?token=MaJ0SimDEkPa30JCwEyMYabZCEo8TNtTG_4KKHt1-v-9-tb7DhqDQf5yvwZNLbTLAkuUiF6tBojK187lrH436xw40yYZeh2g9XQyQY_3lrZT46ZYMAc7ALDl5fHbbpOgU4YICoUtIkAhsB9GPI3Lf6vbYyQpLoIr9YbzDUjm0xVFci65WdPf39o9T0pumgQ8KwXdyXQEFjUjZZ-5iMweFVWl-0waT4HOX6jEHHuOXS9fqJzXvUHx9ke4gb7wBXZIfI7c_FY6N3PrMHDJJ1uWEkg0GYOh5nKNBqNSI5sm53PQ4o6XtKH2WwpQNC8devm4wdytBTXAdzSbCzUptUHFzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هشدار سونامی در ونزوئلا، بعد از زمین‌لرزۀ ۷ ریشتری
🔹
سازمان زمین‌شناسی آمریکا بامداد پنجشنبه در پی وقوع زلزلۀ ۷.۱ ریشتری در شمال ونزوئلا، هشدار سونامی صادر کرد.
🔹
تصاویر منتشرشده از کاراکاس، برخاستن دود و گردوغبار از مناطق مختلفی را در پی این زمین‌لرزۀ شدید نشان می‌دهد.
@Farsna</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/444597" target="_blank">📅 02:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444592">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Thzxe-WMk0lijCFaeh2SnyzvuRnEIwAxmO3BcxmK45qEQ6LIWzegzdlOI50Z5kD6In3Kb-o1ZkL6SvEq4H0gycoEHKiA-IKt_rXBOjMYIO-SDkBPWGIpAKtTP9hl1s47dfi-9TiS9laIhwhoMKfipEwg76GYh0LdqH8-3gbPL6dMYC5PeaFEsqlN5kvOZofW0yNT37qGmYOTVfF0XA2ItbSfcXNZKPTQCxqpXXTNvV6RTWf9j5VC04iYLcIEuyuoMX3pabmjq_iy0JkV7X-CZBXacgNper_zK3ixMcp8dXjbWqTHcxEkShcjykmWl8P-htw1w6IKqrSEJ0O-bTZbfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ruDYLRyC3jyaLbXwa8RiohtjC9_rmi-DXYJruMQfExSFMqIyEJdMYD25zSChPAaMdFX3q1aqN-PvSz9nDEPX7ZyW9v6VDBLqSv-PucbiihMuUg9li0w6r5fcl9ejcN_gw9b8QJbrtS2z4lpdYL8HaoDG-2hS_vwtXm6Na8_5p-Cpyy21pIcwCmr7W88sfkeuaG1i1LNZBdY1eZLIaElWB4_PWFu2XgKUzXwGeZdnYqpSLl-THIOCeb2ebjr6L_GAu0EHjmBKePcLKeMwFNrBE7_7Esd9EphZiWjyXH4MJiRULicKeUBL8pzy73sS30LQi7LD_ZwmAH05XFW3Bb4j_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DVJkYo9jDiDtgGVfin6yNIaIrIot6HadNvGnAAEsKbATxd6GW1ejfhilLIql-09fr2N9JtYlC94lAQqqxZnBEv8sLU5jL8VpW0gOGkj2aiVmdDjW1VROPe8OpYSal80ffo_1q9bC8wmSA9yV4v6APwDc9hqjouJsyzBkK6A-pLZYecVD6kxISG8t2P4vE9Nz5JpHZfEoPziFLPrF5oPTJsI4Y6HkdnMXX4pKQBskFK-uY0gCHc4WKGINJ826ajNIcn6ixhoXgE-fEoq6wrJjuQ0WOoi8dy2gKosQUfTpn3fFuLJR8UxHK9Sxw8AmqUg-8Jrtw6ZtopBsBAeCpTLWgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d9fWiMI2HudQgNYu428ACfL8x_9ghidNToXi7EFz2u8NbRfS7FYsjlsA9zTEmN7ZugzS4Z8Ms5nO1tKPBasYG2VEEUVvApXN4L18OQtj7ve-ePXE_h40XgHn_d5Xrosh2kJJ4OBhiquTsoND5YqNiFtSzAt7-P_nYMFpelW01IQBewLswo5jr3EX4wTKILLrRnfhpvkjBcz1I9MVWZ8Q_xcYZL3l4Ujcc3elhIKwyB8jY4y0NC-0_LFguHC5HVSSrkW7xae0cHtXGIwzsj5ZJ8hH2MvMpu1QEXcGEZTLtdsARP_j6gSlRHyIkoX7ZbqG8xYw1lFAX23YPAeBS-pTYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XBGuBS7Y2_TZPBL9yWh6aOU7KzsOrq20Awim-dbCWQVaFIP0YauC4o2nPJ-kG6gP9k2Ib0kqNyO2918C_0pCrBsxVfF5-1kft6GPhVpWKZRoj0xlv53MHvOMtUjl6ssxPxA4qGKqTdJDi0IQ4Sl7PYQFJt_brIWGrvohrwgR6T7lJvQUROTbGqqDQ8L6uOY4y-WLjnyf9miU59hoMO_j0oQmnzr35ha55e_aZoRGI8VVOkRKZfAUqi09TkTIrfBdKewTBymC0SdZBQhF58THfodtC3kz8GydB7bOy063KTpUeUe2Xq_KCZIZusi6WegT44NSWbSEMWHmvvOg6F7Nuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اجتماع باشکوه فاطمیون زنجان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/444592" target="_blank">📅 02:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444591">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CK3U-0SB9Tfsbj8AvVWnlxOULtl_2g3_bbmNF9PPovFPn-M9sRfV4OfQNIbmyH68J0v6b0DqNy5MZtohyzcN_kW-AJdKPyeldiWG6k1XLgScVPIM8U1Xbp4zhoF9ryqsIOtkpydJ4qZmXCplVNZotqyl3vGS6Z-yyWV-s4PrEcohbwnZvc6ewaLWzxVOLgEzXK9gky1zAL51SMkAzZE0FYjG5YXC9LKLwanJNWfVuHz37LzeNRdAzMCXaCB1DdG3-5AcleyKZ_RTyD-WOgJSa-EBnz5t8UCXkqD193R6OaSQ_TP9jacC7-84L4SOJppGMUIkMVpAJ6H0ZySQi5LoJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازدید یک میلیونی «حسینیۀ معلی» در دهۀ نخست محرم
🔹
برنامۀ تلویزیونی «حسینیۀ معلی» در فصل جدید خود پس از گذشت ۹ قسمت، به بازدید یک میلیونی در پلتفرم تلوبیون رسیده است.
🔹
«حسینیۀ معلی»، به‌عنوان ویژه‌برنامۀ محرمی و با محوریت نمایش آیین‌های عاشورایی، نخستین فصل خود را در سال ۱۴۰۱ به پخش رساند. تاکنون نیز هر سال در محرم و شعبان، فصل‌هایی را روی آنتن شبکۀ سه برده و در برخی آمارها، عنوان پرمخاطب‌ترین برنامۀ معارفی را به‌دست آورده است.
🔹
گفتنی است که در تازه‌ترین فصل آن ویژۀ ماه محرم، مداحانی چون سید مجید بنی‌فاطمه، سید مهدی رسولی، امیر برومند، حجت الاسلام آقامیری و رضا نریمانی حضور دارند و حسینیه در قسمت‌هایی شاهد حضور خانواده شهدای جنگ رمضان نیز بوده است.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/444591" target="_blank">📅 01:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444590">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1f177f01d.mp4?token=e6rG3l6KhFS8LCAeijpzWDflUTIf4wq1fPpgQ1ii31k06vz5wz4DandYKfVYaoELXdlJf41inii9gOFePNCYXAAQsZISICW_9YZmUsTKoFtF34WkiUkPl8Oq60v7f0c6hcWtT-m-2Mk0FoBux9bFFYht776VM3Iu7H7Tjs8p0dvz6d7-7OJ3Io9wSf0mPs1cXls9MqIMafve9voMOX5mpv4QuQrALfqIZq4KIgChYksFfmVQ6psq7kR8t5VuKDDjVSeHc8NB7NsUnA1odiOKnyhv1v98-T66647FDhRAVwe6UkcTBY-cEftv34HoMjybaMGtqKDazf1KpDZnVufjXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1f177f01d.mp4?token=e6rG3l6KhFS8LCAeijpzWDflUTIf4wq1fPpgQ1ii31k06vz5wz4DandYKfVYaoELXdlJf41inii9gOFePNCYXAAQsZISICW_9YZmUsTKoFtF34WkiUkPl8Oq60v7f0c6hcWtT-m-2Mk0FoBux9bFFYht776VM3Iu7H7Tjs8p0dvz6d7-7OJ3Io9wSf0mPs1cXls9MqIMafve9voMOX5mpv4QuQrALfqIZq4KIgChYksFfmVQ6psq7kR8t5VuKDDjVSeHc8NB7NsUnA1odiOKnyhv1v98-T66647FDhRAVwe6UkcTBY-cEftv34HoMjybaMGtqKDazf1KpDZnVufjXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تلاش ترامپ برای شانه‌خالی‌کردن از مسئولیت جنایت در مدرسه میناب ادامه دارد
🔹
رئیس جمهور آمریکا مدعی شد: «موشک‌ها در همه جای [ایران] پرواز می‌کردند. می‌گویند که موشک ما بوده است. شاید هم بوده، اما من چیزی ندیده‌ام که مرا به این باور برساند که موشک ما بوده…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/444590" target="_blank">📅 01:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444589">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🎥
آیین هیامظلوم بوشهری‌ها در حسینیۀ معلی
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/444589" target="_blank">📅 01:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444588">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seM-1HKSPPdu3bQRdLjRqrfx29958DRv4MKWntWaT2_LENZeSGiGHgpvs4AqLC4VsHz99LpGCSz7Kgo55_en3Ee1glpEnJOobdQBHbfMDdqiTLiuLh9tm48l2SDLxB1cskWz_sXYAEjg78UBbYvEVeJnmOnUAzhonQs7Dm83G57CWETgMFzQWEPm6hbdy_YsEZ1YMT9cXk3_7z1mKVwywAsj7PAmh00ZFSK-FLZbBguQLP-wPq_fnD0hQzMVBRHgUEadUQcYYl2VYC2nuEnOq8Mrgsmv-ULhvfKxPaDrXsAFWf552it-siHZC8pjG6dR2IC21GmFKXGnHYuCfwxyXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
آهن و مهتاب
اثر جدید حسن روح‌الامین
به‌مناسبت عاشورای حسینی
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/444588" target="_blank">📅 01:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444587">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfGQ9AjwEhqsfVWPbM-veQbihVKUA_ibheeHVqzEMBxa72hHQw-2_MeAMlREsB8dBUJIdlGahLMIsd_ExvcxnkE4HZ9IJgHSW-FJ0Klkdz01eFJHY7o5w837R6Pu1BTUkHjZDvmI0g1bAHiA8pUjP-FiOXwVZ5RAoi-DPjKi019DEX99Zs8FNklOQN-IrCDX1AQqoz0hUCXZUpX2dSsrqoSphibwRPtXjD5aZ5bL7iyGcNDNBNnIoWZfMlKo3gVX_NykCXoqapjTPaW2mOjkL9Npee6gsMsJ0n19ajQuzU71-_fJFWfvrT65-GiMcwnzdgZRwcCPgRzwtSr4_0UYmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه در لیگ ملت‌های والیبال به سختی از سد ایران گذشت
🏐
فرانسه ۳ - ۲ ایران
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/444587" target="_blank">📅 00:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444586">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f503cef268.mp4?token=JtWVrhHUzYWt6i_QJfSG1GwSgICIs6T5RLRXQXeqp92kMJfQ-1KjNpHg-1WQIREq723_6kfIhy8IAh6yNuf0bG7UWTNmD2DfU3jNEg_ty6VkYii-oyX8hERBy0znrbRCK2pKLnwdi47bE1iOBH0LSZFIcXaFFu6Mn7MXRW8gcI-9HZiS6lCNs2KGchVIxeCxsa_IKVgmgwPRJVWgSOYOPqH1z29yR-gHMaZbXtHkFVTZR7mF5E-jeW4tgbYwYR2zjiV1TZEi16r2wp79pwcjCzx-GevyTXyrXCadnfS6QeixwFrQY_S3ZcFSh_3kCfoThWVp0Vc7tqPkG9I8e9ZOMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f503cef268.mp4?token=JtWVrhHUzYWt6i_QJfSG1GwSgICIs6T5RLRXQXeqp92kMJfQ-1KjNpHg-1WQIREq723_6kfIhy8IAh6yNuf0bG7UWTNmD2DfU3jNEg_ty6VkYii-oyX8hERBy0znrbRCK2pKLnwdi47bE1iOBH0LSZFIcXaFFu6Mn7MXRW8gcI-9HZiS6lCNs2KGchVIxeCxsa_IKVgmgwPRJVWgSOYOPqH1z29yR-gHMaZbXtHkFVTZR7mF5E-jeW4tgbYwYR2zjiV1TZEi16r2wp79pwcjCzx-GevyTXyrXCadnfS6QeixwFrQY_S3ZcFSh_3kCfoThWVp0Vc7tqPkG9I8e9ZOMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: اردوغان می‌خواست برای کمک به ایران وارد جنگ شود
🔹
رئیس جمهور آمریکا بامداد پنجشنبه در دیدار با «مارک روته» دبیرکل ناتو گفت: «[اردوغان] کاندیدای اصلی برای ورود به جنگ با ایران بود. شاید، از طرف ایران، زیرا طرفدار اسرائیل نیست».
🔹
ترامپ افزود: «من از…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/444586" target="_blank">📅 00:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444585">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">ترامپ: اردوغان می‌خواست برای کمک به ایران وارد جنگ شود
🔹
رئیس جمهور آمریکا بامداد پنجشنبه در دیدار با «مارک روته» دبیرکل ناتو گفت: «[اردوغان] کاندیدای اصلی برای ورود به جنگ با ایران بود. شاید، از طرف ایران، زیرا طرفدار اسرائیل نیست».
🔹
ترامپ افزود: «من از او (اردوغان) خواستم که [در جنگ ایران] دخالت نکند و او دخالت نکرد».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/444585" target="_blank">📅 00:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444584">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سوئیس با شکست کانادا صدرنشین گروه B شد
⚽️
سوئیس ۲ - ۱ کانادا
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/444584" target="_blank">📅 00:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444582">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEodlpto72v5ssPrhhid64jcnnn6t9Q60NdMXQHbtS_oIWXWzv3nAgcZf2E3x3dIebNJW8rvPUR_oAi0uFtMjvcLFMUQSRVnQAr-I-v9oJi1SD2UJ0FgJPLDKuBv-h7pEZnip_F91svvSZKlRTWut14kzn8HrRVUxdzltjE-P6t5O5bgW5SPLNI4ozZVMtaIwuI3bpcSTbmtuQc0WiidvmH79Oq_lMV6W1s_DCyoXSSReM7WK5y_6rtc1lQ7tIGLJTn_CQwX1RsVz2XL378zzQ0XmKeS3_Py5LxzwwU0-YmKkNZhnc5YlJVbhMR38jKzrFdhTxXKistcVS1vLJcP2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بوسنی با عبور از قطر به صعود امیدوار شد
⚽️
بوسنی ۳ - ۱ قطر
@Farsna</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/444582" target="_blank">📅 00:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444581">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">کتاب آه</div>
  <div class="tg-doc-extra">قسمت ۱۰</div>
</div>
<a href="https://t.me/farsna/444581" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قسمت ۹ – کتاب آه</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/444581" target="_blank">📅 00:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444580">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAgjNFoUX5Xfb4kMSaxOXclbpwjwLzFL-hlF8_Wwdp0qQbpbBedp8bANzxtPGvJNbRGodX1S5VVK__SsAPt741Jh60KRIcN294zZZoavO6NcJb-LJyf4fY7PA6Zw_2HZuDAvL2vS96ATf36-aHnOtuPdjXtqdqbDm0giwN1hZHd92Jfk8T81AdJjzqyZKHlj45SuFc2YC7ISnygP22i4n66vlSjjiGgnYhse5yQK7o2gNvHIsquyZL3xRYqrfu9S75fMNonGRMVxHcGYFCVrSvJTp8jluVv4LfA3sB_OQEZi9Ydo3BUsWmXQm9oRoJhBSveolbocJCT_ywCz-hT90g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسم مقتل‌خوانی صبح روز عاشورا در رواق کشوردوست برگزار می‌شود
◾️
زمان: پنج‌شنبه ۴ تیر، ساعت ۹ صبح
◾️
مکان: خیابان جمهوری اسلامی، تقاطع کشوردوست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/444580" target="_blank">📅 00:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444579">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISjY6nZqiqc0-PQRkz9sNSdPdLqN_xUHyY7nDFLWkA_3VbgF4-AoKsLlcgq818UfFkM-gZ75dqN8YEqngUsc5mXZU_ILI0i6EjV4oftXE64wx02GAYRXZxfqRisPcCWAyhk50IaYOPIrbox89nUJJaC5cmhB-SIFfRYCkkErFygE1PnEhEDHMXJOV3a4ei01jQq8IYbREJUNwLQCrEWjXOGnxbSjc8gwdNuTaS57DwvQ8wsxyeR7PSRn9rRDyOtxOCFEu66tF8zbd3kBgXscN_cD_yQcFyR3DTWvitM7_UecCj2Mcme8V2E-ztIoGOn2jEOuLY6eEx7J0zqTFdwiNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستی‌ای که تمام شد
🔹
امام جعفر صادق(ع) دوستی داشتند که همیشه و در همه‌جا همراه ایشان بود و به نظر می‌رسید پیوند دوستیِ بسیار عمیقی میان آن‌ها برقرار است.
🔹
روزی این شخص به همراه امام به بازار کفاش‌ها رفتند. غلامِ سیاه‌پوستِ آن مرد نیز درپی آن‌ها قدم برمی‌داشت.
🔹
در میان شلوغی بازار، مرد ناگهان به پشت سر خود نگاه کرد و غلام را ندید. چند لحظه بعد که غلام پیدا شد، مرد با عصبانیت و تندخویی به او پرخاش کرد و گفت: «ای زنازاده! کجا بودی؟»
🔹
امام صادق(ع) با شنیدن این فحش ناموسی و زشت، به‌شدت تکان خوردند. دست خود را بالا بردند، به پیشانی خود زدند و با ناراحتی و تعجب فراوان به آن مرد فرمودند: «سبحان‌الله! به مادرش دشنام می‌دهی و تهمت می‌زنی؟ من خیال می‌کردم تو مردی باخدا و باپروا هستی، اما اکنون می‌بینم که ذره‌ای تقوا نداری!»
🔹
آن مرد برای توجیه رفتار خود گفت: «فدایت شوم، مادر این غلام یک زن سِندی (غیرمسلمان) است [و این دشنام‌ها برای آن‌ها عیب نیست].»
🔹
امام با قاطعیت فرمودند: «مگر نمی‌دانی که هر ملتی برای خود قانون و سنتی در ازدواج دارد؟ کار تو تهمت و ناروا بود. از من دور شو!»
🔹
این ماجرا باعث شد که آن رابطه نزدیک و صمیمی فوراً از هم بپاشد؛ امام صادق(ع) تا پایان عمر دیگر هرگز با آن شخص هم‌سفره نشدند، هم‌قدم نگشتند و با او رفت‌وآمد نکردند.
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/444579" target="_blank">📅 00:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444578">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4648ad25ef.mp4?token=gegVwbtmkq_2NX85yi5jGYMfsvssY8YPqtFtuvrNu3TW-sApllm5OZ-S_pvsLBp7NMU2YTVZB-7mG-LQp0lkTCTqg2_oemEQ1FPEoF0NOQpeY_OMUidFmdnvUkEFaT0bSXwutYtlkShrSHJq9RcV3kdDlKIVSVy0fWUccaaO-wDtSmiUGjfM4hWXyFO_0B-e_8BOKEiqPbM-w7p4s8RdPds9W54lOSjx1SeXgBjTXzGwGubZmcMTrt2c_Q7m-_dEbKDE5Mg_siuuwLMlOlaEqVjNlD3_jCk5AF8RnIg6315CjyMbNZa9dMupsDrNW80JScBTAKs3VwAM1bfdQ9jVTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4648ad25ef.mp4?token=gegVwbtmkq_2NX85yi5jGYMfsvssY8YPqtFtuvrNu3TW-sApllm5OZ-S_pvsLBp7NMU2YTVZB-7mG-LQp0lkTCTqg2_oemEQ1FPEoF0NOQpeY_OMUidFmdnvUkEFaT0bSXwutYtlkShrSHJq9RcV3kdDlKIVSVy0fWUccaaO-wDtSmiUGjfM4hWXyFO_0B-e_8BOKEiqPbM-w7p4s8RdPds9W54lOSjx1SeXgBjTXzGwGubZmcMTrt2c_Q7m-_dEbKDE5Mg_siuuwLMlOlaEqVjNlD3_jCk5AF8RnIg6315CjyMbNZa9dMupsDrNW80JScBTAKs3VwAM1bfdQ9jVTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: دشمن خیال می‌کرد در ۳ روز جمهوری اسلامی را از بین می‌برد اما سپاهیان و ارتشیان ما کاری کردند کارستان
🔹
کسانی‌که راه حسین(ع) را می‌روند در مقابل بمب‌ها و موشک‌های دشمنان سر خم نمی‌کنند و نخواهند کرد.
🔹
الان همه در منطقه ایران را یک قدرت باعزت می‌بینند.…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/444578" target="_blank">📅 23:49 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444577">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db91a75633.mp4?token=ufb-vD5cbbwYl0WHqx0KS93LL4ygkVLo7KbJvNUyxcq1z9GPUTJB3ORRyuNTUC3uiq-JMnawJBguioMrz91FJQfmNdFOeKt5nDxZ8WwXaFgslaOHdw__PLHUtBQAkD-w7lUxuRXxiuaJunHuBpdy5UOchczHycg7j_rh5y-U81L7Yw0d6Nq6oZz6HsHxKH5RFY6X6u2m4E-UNKpudttXC31uKCpY6S3NKOCc3yqZTsPcIJAW-fjEiEmvA-DsSbeCmHrmDlEIY8UzLF823kRWuUpVxfjmWZZGzASfDskFaS4hQeRn1KGHw75YN438rALjMv9Lh1DBS-77A0Fgt4Tofg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db91a75633.mp4?token=ufb-vD5cbbwYl0WHqx0KS93LL4ygkVLo7KbJvNUyxcq1z9GPUTJB3ORRyuNTUC3uiq-JMnawJBguioMrz91FJQfmNdFOeKt5nDxZ8WwXaFgslaOHdw__PLHUtBQAkD-w7lUxuRXxiuaJunHuBpdy5UOchczHycg7j_rh5y-U81L7Yw0d6Nq6oZz6HsHxKH5RFY6X6u2m4E-UNKpudttXC31uKCpY6S3NKOCc3yqZTsPcIJAW-fjEiEmvA-DsSbeCmHrmDlEIY8UzLF823kRWuUpVxfjmWZZGzASfDskFaS4hQeRn1KGHw75YN438rALjMv9Lh1DBS-77A0Fgt4Tofg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: از زمانی‌که ما آمده‌ایم دشمنان مدام خواسته‌اند برای ایران مشکل ایجاد کنند
🔹
روز اول اسماعیل هنیه را شهید کردند و [تا الان] پشت‌سرهم مشکل برای ما ایجاد کرده‌اند.
🔹
اما ما با وحدت و انسجام و رهبریت داهیانه‌ای که در کشور وجود دارد تاکنون توانسته‌ایم…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/444577" target="_blank">📅 23:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444576">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af8cce3443.mp4?token=PaeGrJ2iOq5h-szkdYRGffrPovCc4IkcCDunKJfeRg3Ju1VAZEFgUgR17W3mbW2XnuX85X5whBGUteay9aa7icUZg-DEukYU2k6MyFjmTzF-vKqyq9Ccl-i7JG0KUPPGxtg3FBymSJhqcYAFOzF6KkHkL5ChnLSAY2w-vup6Zf_Nxn4ZqmSCjvxkVmp64ySuqcMAOPdUFoRRro4858YVY7psodSwhauaUQl_bdUzhDjbiAYL82C_CFoX1DkLSdqLzJwy8YU5Slxa-mbq66LJ6kT1IP4HivgaIxWCQbg_TD-7mKGh9yppdQd_BkQ1hFpqfawQ_ADuoYuSZPUbvHL7BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af8cce3443.mp4?token=PaeGrJ2iOq5h-szkdYRGffrPovCc4IkcCDunKJfeRg3Ju1VAZEFgUgR17W3mbW2XnuX85X5whBGUteay9aa7icUZg-DEukYU2k6MyFjmTzF-vKqyq9Ccl-i7JG0KUPPGxtg3FBymSJhqcYAFOzF6KkHkL5ChnLSAY2w-vup6Zf_Nxn4ZqmSCjvxkVmp64ySuqcMAOPdUFoRRro4858YVY7psodSwhauaUQl_bdUzhDjbiAYL82C_CFoX1DkLSdqLzJwy8YU5Slxa-mbq66LJ6kT1IP4HivgaIxWCQbg_TD-7mKGh9yppdQd_BkQ1hFpqfawQ_ADuoYuSZPUbvHL7BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: از خدا می‌خواهم که ما را شرمندهٔ مردم ایران و شرمندهٔ خون رهبر عزیز و شهدایمان نکند
🔹
ما باید کاری کنیم که شکوفایی و عزت و سربلندی در کشور بروز پیدا کند. @Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/444576" target="_blank">📅 23:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444575">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8023403663.mp4?token=L-DnZ6ZtDreR0xVRyVj-OBUSMrFQk--5sXV06ipB3YqpyrETzw0Zx_YMGnVaoCta1Cx7jNCyUvpTx_MxguJ6FcYjVQ6mhiZR-3Gjqq21SZ06MlLMBW332TgUpOTpENgpSxbN3aJWOKES6eVUhIR214f0VCLQKN_CKKdKcizb4jbq-z8g4bcDcEiLpQwS0ew-JUwFHqZ2A_SG0TxItvy41xpUyq-5T0ZPSE4qsBTpEn5khYmJ2Swr30i3vS2HSLhtDszmuduP8XKBOwlny222t2111gLsTPzGZhB6Ha6wfB_lSGn7uIqJ8CNjnPwLzFeQ_SFALPsehcBglNuHliMKbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8023403663.mp4?token=L-DnZ6ZtDreR0xVRyVj-OBUSMrFQk--5sXV06ipB3YqpyrETzw0Zx_YMGnVaoCta1Cx7jNCyUvpTx_MxguJ6FcYjVQ6mhiZR-3Gjqq21SZ06MlLMBW332TgUpOTpENgpSxbN3aJWOKES6eVUhIR214f0VCLQKN_CKKdKcizb4jbq-z8g4bcDcEiLpQwS0ew-JUwFHqZ2A_SG0TxItvy41xpUyq-5T0ZPSE4qsBTpEn5khYmJ2Swr30i3vS2HSLhtDszmuduP8XKBOwlny222t2111gLsTPzGZhB6Ha6wfB_lSGn7uIqJ8CNjnPwLzFeQ_SFALPsehcBglNuHliMKbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: هرکس مدعی است که می‌تواند مشکلی حل کند یا راه بهتری برود ما بستر را آماده می‌کنیم که کار انجام دهد
🔹
ما با پیشنهاد کاری نداریم؛ هرکس می‌تواند این گوی و میدان. @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/444575" target="_blank">📅 23:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444574">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ab58061e5.mp4?token=RcPoSg_pHfJ4ok0KIj2LXKYQ7EiZgaUpUSEOtZx_IEGGj04utm2-1urdKlUMuG-0xWMdGHCNm9ib8zdo4OWqDjUXlHn3kZw92dC5QRB3VrEfHQFfwe2BjlqhJPTJDBfTSD-CwVp_C26Fr9397tA60aDWU8hvVv6t0Iiw8Dr1n0Ic5PdSaNj2JKWSSNZQ-SpT3DAZkI2LgXjt6s2R6YxiZ_V7DAEWuoEIf0NttiQ4R4d6W4pGDYoe5oxZGn1zV5r_V8mtTJ0wE40xzPHmiS1B8JgQokCXXGFRYswUWWyqpCgGjuUaPnUB9APrWk2V5qJJXn6gaOQ5Ahq2eu_xBAD4VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ab58061e5.mp4?token=RcPoSg_pHfJ4ok0KIj2LXKYQ7EiZgaUpUSEOtZx_IEGGj04utm2-1urdKlUMuG-0xWMdGHCNm9ib8zdo4OWqDjUXlHn3kZw92dC5QRB3VrEfHQFfwe2BjlqhJPTJDBfTSD-CwVp_C26Fr9397tA60aDWU8hvVv6t0Iiw8Dr1n0Ic5PdSaNj2JKWSSNZQ-SpT3DAZkI2LgXjt6s2R6YxiZ_V7DAEWuoEIf0NttiQ4R4d6W4pGDYoe5oxZGn1zV5r_V8mtTJ0wE40xzPHmiS1B8JgQokCXXGFRYswUWWyqpCgGjuUaPnUB9APrWk2V5qJJXn6gaOQ5Ahq2eu_xBAD4VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: با تمام وجود داریم تلاش می‌کنیم که هم عزت و سربلندی کشورمان را داشته باشیم و هم در صلح و آرامش زندگی کنیم
🔹
وحدت ما بین کشورهای اسلامی دارد مثال‌زدنی می‌شود. ما در دولت باید کاری کنیم که مشکلات مردم حل شود؛ اگر این کار را نکنیم هرچقدر سینه بزنیم…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/444574" target="_blank">📅 23:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444573">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ebb6df561.mp4?token=W04fHedX8r29VP76zmL55mdiJo7BRwBt200ooBhyXG3NfZdRi8UDJ8Er7jXGWQxrvhiKHYUdFdCZ8zUCHXjDGh66M0_69rckOu_PAYi2q4C9YOSs1m2_Ut6qPoY0Pv03kGfp98SZV2IwidF-zKWT_H_E4TTR8mWVIuwxY_idSiKsE8BcQ5Xh67huZS4cs8ufpN9RDnrT1XSSZ-LPDrfBRFAddExHdtHrQbKse-rd3y1S-liPtYFyhdTHFJDGMIU_u0JH4rJkp_jzm6YRezTyPOlM8LsiFGh2T7QVx3Yzjm6SOQ777yfMFGZa0sZpThKyoMW3tD48JDPrfgMneGfx4jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ebb6df561.mp4?token=W04fHedX8r29VP76zmL55mdiJo7BRwBt200ooBhyXG3NfZdRi8UDJ8Er7jXGWQxrvhiKHYUdFdCZ8zUCHXjDGh66M0_69rckOu_PAYi2q4C9YOSs1m2_Ut6qPoY0Pv03kGfp98SZV2IwidF-zKWT_H_E4TTR8mWVIuwxY_idSiKsE8BcQ5Xh67huZS4cs8ufpN9RDnrT1XSSZ-LPDrfBRFAddExHdtHrQbKse-rd3y1S-liPtYFyhdTHFJDGMIU_u0JH4rJkp_jzm6YRezTyPOlM8LsiFGh2T7QVx3Yzjm6SOQ777yfMFGZa0sZpThKyoMW3tD48JDPrfgMneGfx4jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: ما امروز هم در بین سران قوا، هم در شورای‌عالی امنیت ملی و هم در مجموعهٔ سیستم یک زبان و نگاه مشترک پیداکرده‌ایم
🔹
اگر دستاوردی داریم، دستاورد این مجموعه است؛ دستاورد رهبر عزیز، مردم، فرماندهان، نیروهای نظامی و امنیتی، هوافضا، دولت و همهٔ کسانی‌که…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/444573" target="_blank">📅 23:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444572">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce9e18e92a.mp4?token=f70qubN3mCAe0JsC7ImrA_MkcGZ_D-eZIcEQZN0zrk1njhNyDwq0xBmDpO42F0fEFj8Dx295p_TuKlA5645s79l7WqSHAAETa5xj3qzhE-SI9UfyqqaBUdM3RR8dTUAJiNlDJJ6AlisrtrJn0sjDZrzKiAMzUKWUBL5LH8YmUFusWKMmPzbdU39k6HRtQwZQo-wfFtpFc-b8ER1cK9Tuwr-1Bxr1-iCJGtLrzjZ9MsHusgBZuSU10tuXn9k6-ZpePRyeHD_tIom_VR3SNgH5VnuRr2C8kfEuoZL5rMHgzoBMoRw3pOhKrzLIvuYox6lS3NOtl4ihsNvnLm7SUSREYn55b8ZM8RTPlIN1Rz4fN4vnAGbCPWY6FMg-6skKxxOGbYD1XjcjuL61YQOYmAnsWv-z5UE9aVWjlpCv8Qi2bl-JnxhA7FAQwS7Mrz7x-1aeKM1QvEUDYpmbONbp1mpkU5KR1gV1zuF3L-CyTIvQHn8R_ns-tV59Ck19yEtTmnSFMnJIzKWxzN6rQ_Xh9BU4MpZTGSy6QXLJj4AoLDahqJAsQ9Vb-30i_Y60eqhHkz2qzf3QZ15VPWj4NzBbkK1cPgpD-FTV3_zDZgfD6JcPZBCNNdaFAfRAav6ZTtc77BRhoYhLQ6Lz06CxutNAWYdDki-7ZGyIoqCsBeiO46zFMBk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce9e18e92a.mp4?token=f70qubN3mCAe0JsC7ImrA_MkcGZ_D-eZIcEQZN0zrk1njhNyDwq0xBmDpO42F0fEFj8Dx295p_TuKlA5645s79l7WqSHAAETa5xj3qzhE-SI9UfyqqaBUdM3RR8dTUAJiNlDJJ6AlisrtrJn0sjDZrzKiAMzUKWUBL5LH8YmUFusWKMmPzbdU39k6HRtQwZQo-wfFtpFc-b8ER1cK9Tuwr-1Bxr1-iCJGtLrzjZ9MsHusgBZuSU10tuXn9k6-ZpePRyeHD_tIom_VR3SNgH5VnuRr2C8kfEuoZL5rMHgzoBMoRw3pOhKrzLIvuYox6lS3NOtl4ihsNvnLm7SUSREYn55b8ZM8RTPlIN1Rz4fN4vnAGbCPWY6FMg-6skKxxOGbYD1XjcjuL61YQOYmAnsWv-z5UE9aVWjlpCv8Qi2bl-JnxhA7FAQwS7Mrz7x-1aeKM1QvEUDYpmbONbp1mpkU5KR1gV1zuF3L-CyTIvQHn8R_ns-tV59Ck19yEtTmnSFMnJIzKWxzN6rQ_Xh9BU4MpZTGSy6QXLJj4AoLDahqJAsQ9Vb-30i_Y60eqhHkz2qzf3QZ15VPWj4NzBbkK1cPgpD-FTV3_zDZgfD6JcPZBCNNdaFAfRAav6ZTtc77BRhoYhLQ6Lz06CxutNAWYdDki-7ZGyIoqCsBeiO46zFMBk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: ما امروز هم در بین سران قوا، هم در شورای‌عالی امنیت ملی و هم در مجموعهٔ سیستم یک زبان و نگاه مشترک پیداکرده‌ایم
🔹
اگر دستاوردی داریم، دستاورد این مجموعه است؛ دستاورد رهبر عزیز، مردم، فرماندهان، نیروهای نظامی و امنیتی، هوافضا، دولت و همهٔ کسانی‌که دفاع می‌کنند است.
🔹
مهم‌ترین مسئله، وحدت و انسجام است. هرکسی به هر بهانه‌ای بخواهد وحدت و انسجام مردم را به‌هم بزند، آب در آسیاب دشمن ریخته است.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/444572" target="_blank">📅 23:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444571">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73fb8f2d25.mp4?token=tqLd6VY_fI1_1-EIM0hXC3gMsQCfbkQq0eZnnn06r0pHG7sDG-V8H2UNWzOYUlf8CC9IV-poBRrLHNXKijAc1bpxKzHVQHsYEf_pHKgY3kIb1Buj_En2wPm-Z9dK3HAWb9pVXDKLZaJZRmEUdo7PdctytRppe0VD8NJy7bmFmvkEpGNvB5L4RoZ4cFWSOi_VbXwmMg0Qa70N6wEgmuOd26zaSbKCoPr-6geITVr2SShe-arIHUTFCqJ3XxJTZGQ2-1o7mKO1OamsDMGpfZ-vsr1ZhZTxI5AqxeWFR48CfutHMmBZGdGSNcMLlkq_ECnPnyyrLu0UyOgYl3AnvGywXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73fb8f2d25.mp4?token=tqLd6VY_fI1_1-EIM0hXC3gMsQCfbkQq0eZnnn06r0pHG7sDG-V8H2UNWzOYUlf8CC9IV-poBRrLHNXKijAc1bpxKzHVQHsYEf_pHKgY3kIb1Buj_En2wPm-Z9dK3HAWb9pVXDKLZaJZRmEUdo7PdctytRppe0VD8NJy7bmFmvkEpGNvB5L4RoZ4cFWSOi_VbXwmMg0Qa70N6wEgmuOd26zaSbKCoPr-6geITVr2SShe-arIHUTFCqJ3XxJTZGQ2-1o7mKO1OamsDMGpfZ-vsr1ZhZTxI5AqxeWFR48CfutHMmBZGdGSNcMLlkq_ECnPnyyrLu0UyOgYl3AnvGywXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
#فیلم
|
نظر حجت‌الاسلام سیدمسعود خامنه‌ای‌ در مورد شبیه‌ترین شخص به رهبر شهید انقلاب
@rahbari_plus</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/444571" target="_blank">📅 23:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444565">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bI0Kd0iotE8dnttwcV8WqrF7t9WCkOz8kHtG-HHmp9hnK1w0PpD-wFO9xZqNtvN68heOtkMuxjAi1t1eTyf5CTNNh5Tp-D0TpUj06DeemTBqFWQ7bOg24F_FsJHw0yS--5xn7qRg5pCgp5QTpjlPukrBGU0TwMQweAySdlmfnmdzbzco-1gG_bV370E1HoxAeE6NhTYTkgFetE2_BlsPPm11WpQrOMGTlGuLZcyEBDyhbiI7GL2C97sX1zZlknDSwi3Q-yUMXZQdTZu_z9jdp3I1STNF1ykJyDhsMatN04HHlkI57IwypTG8CORopn7WzhisnBqW6oosVenO78h_eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X_m7bXsF-vpJwO-Ub3lGixE3FaFNUY_gdrGAnoBO0D5EuiUihHygD3J-KX7DGB4Y8-l5cHIPFnh6irmnxJT5Vo6nFdZhBhgPPgR_Yp4zrU26L2Ce1X5VuuLuCAxCeffx8HCvhqg5SB0jEGTvoNmIJaVUc6Ne-_4kXUXVNwp4jk5SuqKjb39XqxGoySutGjDzaofcl7YAR3FQh5HKFWaUB-sXWZ3bmJEXzzTNZrNz_SPV2ziwALBIYMHSERMn2TfEpIFXo20UQDVwunzNmthUcRx3ZxZatWNMFqVtKvOBofoY2W8wYl4Dm22xMsNikvQo5bCBXBzQsI5iFzoV_yMZJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BqJR-8Ho0EyNcw0DSDf12OuEMfZC6Cr7DO3T74YpKSd2nm8n1kAWAFt1X7Er964uHDoSc2PDtkSqT5gEUwcE-EWLHLxsVJHr0IDGESXGytfBbj8tm2DU5I2dsfIZ8exR6u0zqSsWnkCn53n9tFXJ1Wn85rpwfGRqD2YAq_My72M5DasLRKoEbHVWu8Vswas8_PS-JIwV3oumPHaFDYKKc4jkwYLkkRo0QhuS78Mmsu2_xXz-yWvEFR-lS6WZyx1Q-CksV1yRM8DI14YiGheZwPDHTXZSUkK2do_91TMu-KGJDMuAE2xNLILRLQs_zduAh6tcp3yBpm97BlqpNdNOCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z5H8VI94wsx-TyBFr57rtBGFNcDd8stWe2OWJB7S--SWilgoVQYpp39a3ITZ7jd1fCQbd9gb_HdPBvcksQinQYhgoBxPHouP1X28ncjX-n4Cx59hI-2Zd8frAAQ9JHobXD_GsJjO1L5LJTfmLpih3YP_T5IdZXzOXpfVJLkn8tcEplkAn4M8WDfNJ6YOLotmEBzQHNAEWgFRqL5NDkV_sQJLdU1-bbyp_ekRbfPCnBNpR3SVEU4Kzu7GxIv6hzzoSqu3kpiwN-kQAZ9rvMEDLEydOMMKVR7ozLvqO7-W3c7VRIxrnSqBQkHQyuLK_4hZWeJPdtF_BJnAZgkq8UcdbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bJaQo2obVkiZZn0oe-kd84BIOMydwcupyLI6OnmdNK9FgZtuNQi2tLmdtryl4uyYJSxfiRUjxiHulDLQ_1fp9J0cgLQK3Kwks94WOFPB6pw_kx31AGljLT38JfrPk_q9tHvc8X3UcknJlDa-I90eTTsU3cluthnq3Iy7kA1W-_zQQtpCh9lrnBuR44cFSkiyREHoCY86qmcWBL54tx7kei64iGZb2jgj493NXOeQKCnDSqddHi7PZdYdyvK31v5v4XnvRPPQAiSwJKJf197xs_XGMoalWJn8QMhNvaG28YEB51Pd4YYHryUBfw-N86ykJm2DUUmeiFJgQ1iF51FWDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cRELE2YfwXa848yT6aoWoSkrdKnn9DMe4LhBf004-S9Do6aK4yyuvFFCZT7igv_ss1hQkP2DDpwsFwj29TviGqpWBa2yGHU549ds2nBMtNit0RRUeWKZfUnjfKdgnpT4yEZL8YGFt4LpdslIwkMQdvkhdIpDZeF6CRldaRtTDMZ2F7KHbgLKxruI6FQgZCGyhIWkjcEYy6kHJfe_d3hlImQJH1iwJtFZjDigBaagO4fQk_FY3rQOcvxp26fUMvpM2kLuNNBD5W6kEES_rYJ-lkhjqQMxl2jE8TZiCKCDWJncfIlAHeNRMVeJiSc7neGMqEKGOgBTyX1ehFIixHzDXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جلوه‌ای از شور حسینی در اجتماع بزرگ مردم مریانج همدان
عکس:
مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/444565" target="_blank">📅 22:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444564">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6db93a3fd2.mp4?token=C00Gc6A4JCRs4dMugZDyqoGSURBFSJBWH2dy_k-mBZPOGrVzE8qwQb4KJOaamJGne6aX2Wzw3SL90uaHjjkKlzu67eYYgTvC2uv9jLxUhzP5XoV2kM-FMkx0rbGmr61H3Hh5ArhKcy5F9R_aDIyuuKvs45lH2iBjNr87k0QEkwz5IZTSMixdJG40rk9qlZ3K35z0M2Ink3zCfCcydtEU_w0evFQ7wFfab2bdnhuCN2t7G8ejEJirNQetKvAuhACbTtD_uqUaX7OLqPTkLgKaeKqTHDsQG5wL0xIHHUT0IuRqgIdtzo0oKqwRE0G66zOXRB_EAvBSiR4E4fR1cMoMRi6_nkqsNjc7HDuIpnFXG39zX12XMoYhOgpV-qAL7dI4m67pSctbCcdn0JDPSZr75SWL6olUyv-gVWjkE8f9zk9rEQkfwTVjuUnujuqKyMcXMDCFfgITs38C-H3tTGLP7yt3ziXCPjCumiT64arAvS7XfzD6orJHG8_iKJX58DIa4Q4_zgcOpwwb6Mworh5HHo6bquVx5RBcFvgGCzABGavQppoAiynboqZ4GTH6UOlIDRPnqaEyw0MTcBdm3aVYv8QYSyfVb-WNCC1yCwlATt31cgb6DzZWTRvwTnoSUwPRLG0ybLmZxam4QC64xMEoYxvomU4zr9CnQV8NVPrpDcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6db93a3fd2.mp4?token=C00Gc6A4JCRs4dMugZDyqoGSURBFSJBWH2dy_k-mBZPOGrVzE8qwQb4KJOaamJGne6aX2Wzw3SL90uaHjjkKlzu67eYYgTvC2uv9jLxUhzP5XoV2kM-FMkx0rbGmr61H3Hh5ArhKcy5F9R_aDIyuuKvs45lH2iBjNr87k0QEkwz5IZTSMixdJG40rk9qlZ3K35z0M2Ink3zCfCcydtEU_w0evFQ7wFfab2bdnhuCN2t7G8ejEJirNQetKvAuhACbTtD_uqUaX7OLqPTkLgKaeKqTHDsQG5wL0xIHHUT0IuRqgIdtzo0oKqwRE0G66zOXRB_EAvBSiR4E4fR1cMoMRi6_nkqsNjc7HDuIpnFXG39zX12XMoYhOgpV-qAL7dI4m67pSctbCcdn0JDPSZr75SWL6olUyv-gVWjkE8f9zk9rEQkfwTVjuUnujuqKyMcXMDCFfgITs38C-H3tTGLP7yt3ziXCPjCumiT64arAvS7XfzD6orJHG8_iKJX58DIa4Q4_zgcOpwwb6Mworh5HHo6bquVx5RBcFvgGCzABGavQppoAiynboqZ4GTH6UOlIDRPnqaEyw0MTcBdm3aVYv8QYSyfVb-WNCC1yCwlATt31cgb6DzZWTRvwTnoSUwPRLG0ybLmZxam4QC64xMEoYxvomU4zr9CnQV8NVPrpDcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری سنتی مردم قلعه‌نو خرقان سمنان در سوگ سیدالشهدا(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/444564" target="_blank">📅 22:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444563">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55cc5d98e8.mp4?token=RJQUhGylsyOrUBBmeuLi1WzCXxQf5XULsRMp9ws5BjEf3rSc3dKNOsabZC-Zzht28OOH3iwlP4TAlAewv94xTCW5rRx9MUomVCerECT0J4h23ktPyxL44WVxZrOGpxeBeHfCFEKmpsjyzqkSbv2JwW55-oKZNeUNzxaPyqBquc497dpWo33dY6RmWbtaBIDBQUG8b4O4qPBwy2RR06d-LNnot2uUZBwv7mbEONnLyKiFJp2Ml0PE9B_9LbtHjwetZMTCBqI6va8ccW1G0r4c1PUloWvFN3t79hr2lECyrueB5m8i2XyVMX79elqgdMMMn_K16WCmqcuK7wFUhLPSWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55cc5d98e8.mp4?token=RJQUhGylsyOrUBBmeuLi1WzCXxQf5XULsRMp9ws5BjEf3rSc3dKNOsabZC-Zzht28OOH3iwlP4TAlAewv94xTCW5rRx9MUomVCerECT0J4h23ktPyxL44WVxZrOGpxeBeHfCFEKmpsjyzqkSbv2JwW55-oKZNeUNzxaPyqBquc497dpWo33dY6RmWbtaBIDBQUG8b4O4qPBwy2RR06d-LNnot2uUZBwv7mbEONnLyKiFJp2Ml0PE9B_9LbtHjwetZMTCBqI6va8ccW1G0r4c1PUloWvFN3t79hr2lECyrueB5m8i2XyVMX79elqgdMMMn_K16WCmqcuK7wFUhLPSWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
با تبسم گفت ای ایران بخوان...  @Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/444563" target="_blank">📅 22:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444562">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e349ae8184.mp4?token=HQJkgH-ETf9CztZwHzqqAKgkptZKhnTTVLw6X5vy-nhcJ62r3zdo47oA7OWcAQjeJhDi_JkDY7uPXUn0sv7-2YH35EqJXGrf5rtbvRHAruetGrPzaCmR06Vsey_FpamBqPung9sZ6WMqukctFLtg0H4ZwJXJLeYeBJ_wHF2yQ8BwZNyAa-0U8SPaZQZyzDTu5MqzobbuSpYrKyHJ646IeWCRkiNI1NdhCAQFCOctNvyYYNbkIUkUjgPUKc1CyNaiPTIrugIBa4d8NZZSoXr9ofhNV6V-upSMF77y2-LNBDkeoqxVbBVkQV32cG-4VzlF0VgLK-gozzColoQpIee_EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e349ae8184.mp4?token=HQJkgH-ETf9CztZwHzqqAKgkptZKhnTTVLw6X5vy-nhcJ62r3zdo47oA7OWcAQjeJhDi_JkDY7uPXUn0sv7-2YH35EqJXGrf5rtbvRHAruetGrPzaCmR06Vsey_FpamBqPung9sZ6WMqukctFLtg0H4ZwJXJLeYeBJ_wHF2yQ8BwZNyAa-0U8SPaZQZyzDTu5MqzobbuSpYrKyHJ646IeWCRkiNI1NdhCAQFCOctNvyYYNbkIUkUjgPUKc1CyNaiPTIrugIBa4d8NZZSoXr9ofhNV6V-upSMF77y2-LNBDkeoqxVbBVkQV32cG-4VzlF0VgLK-gozzColoQpIee_EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هر قدم این ملت در خیابان، لبیکی روشن به سیدالشهداست
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/444562" target="_blank">📅 22:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444561">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktCOrROqi3kn0uf_cmOd63etVhD-V3Tyicdn9TKCpFok9sBYPBPEXGvs9Ra6-PwpdJkiL1_KRsjFYJfY96ESHQE0RAnnKcRMg48xCZlm37c72Nro4dYQoB-pYZhzVI5WWaisjV8nutwoU_CEdcASXvyGodDOb_YwL3nViwTJ8ppUSYdynE8KBZ9Pn1mEUGZRHJaS8kbipmPvFTnXLz4kkPuvjTZTkfpJz7ODwAL92KmgJCNwLWltfsjK7gm01aXnxxsnuuWXRmd5By57XLebqCC9Eo1vItRK-wxMmMH_xH0OL-GDFeW-oAheF7g3EiZGxmyenZ0MHXbeHrjXVTP7WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌بی‌اس: شدت جراحات نظامیان آمریکایی در جنگ ایران سانسور شده است
🔹
به گزارش رسانه آمریکایی، نظامیان مجروح و خانواده‌هایشان ارتش آمریکا را به کوچک‌نمایی جراحت‌های جنگی متهم کرده‌اند.
🔹
زمانی که در بحبوحه تجاوز نظامی به ایران از پیت هگزث، وزیر جنگ آمریکا، دربارهٔ تلفات درگیری پرسیده شد، او به خبرنگاران گفت که «تقریباً ۹۰٪» از ۴۰۰ نظامی آمریکایی مجروح، فقط آسیب‌های جزئی دیده‌اند و پس از درمان به خدمت بازگشته‌اند.
🔹
اما اکنون، برخی از نظامیان مجروح به سی‌بی‌اس نیوز می‌گویند که جراحتشان بسیار جدی‌تر از عنوان رسمی‌ای بوده که ارتش به آن‌ها داده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/444561" target="_blank">📅 21:57 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444560">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/466eda3527.mp4?token=eiRnmD-Azo6e-mJxDHpDvThdkhtksPQRKPZhOWlFymSdpGcbBUznYieNVkjdeGhcd2zPnK8iEAlJgcJGTJFvvgpi2AbsSiaqlhlsCwnrR1J4X73wF5bEKB3RRKvjIjizzNclrm3u30bCWeATkx0kQWMT3hTsEsGDB9HNTXXWHXZzSA3TYQRD7uCSwWA9hhr0ysMZCWl3_-lerMLQJO1-tnaBHQGa2VE-qe26gXTXp08h6R_Bvy32p8_ThGvGW4UtyaSAPszuv8m8JmwHUc5ffwKD9HYBivvfdbLAHfCEL2ZOnm9WG7rRSKOdSMjP1pNdaXyPu0pFQENgZUbaqcMTaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/466eda3527.mp4?token=eiRnmD-Azo6e-mJxDHpDvThdkhtksPQRKPZhOWlFymSdpGcbBUznYieNVkjdeGhcd2zPnK8iEAlJgcJGTJFvvgpi2AbsSiaqlhlsCwnrR1J4X73wF5bEKB3RRKvjIjizzNclrm3u30bCWeATkx0kQWMT3hTsEsGDB9HNTXXWHXZzSA3TYQRD7uCSwWA9hhr0ysMZCWl3_-lerMLQJO1-tnaBHQGa2VE-qe26gXTXp08h6R_Bvy32p8_ThGvGW4UtyaSAPszuv8m8JmwHUc5ffwKD9HYBivvfdbLAHfCEL2ZOnm9WG7rRSKOdSMjP1pNdaXyPu0pFQENgZUbaqcMTaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نسیم شب عاشورا در خیابان‌ها می‌وزد
@Farsna</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/444560" target="_blank">📅 21:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444559">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7a8adb86e.mp4?token=e3cgQzGRm4wvVGRoeqBy8nIfqblR-Jebu3OfhRLf5XdJZxM9-oyl8n9ASvagBOs78iayzPa-nFOcbchAoTSwLPmkPilsu8MKJPjJuGtnOoj_EL840klJ25djD5WapbiQ5rlys-39WDZzjOU6mma6KDkqu_4pGlEHmOEx-Tjwq70U2IEhlXjRsNkof12nKFiycQncViTKk1V3GTRVZIoCTp4i-T0F2GcJeEvzr1PTgEGNsy5_uIsVK4mHCtpeNdmCtulUkbfQg4BWWfURFSV5BFihMuVSPQHL6i5KNRgHYZ6ETey-H1XKqBrcMXHt4ghICKxfYbKSoqwr77ikbFS_QDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7a8adb86e.mp4?token=e3cgQzGRm4wvVGRoeqBy8nIfqblR-Jebu3OfhRLf5XdJZxM9-oyl8n9ASvagBOs78iayzPa-nFOcbchAoTSwLPmkPilsu8MKJPjJuGtnOoj_EL840klJ25djD5WapbiQ5rlys-39WDZzjOU6mma6KDkqu_4pGlEHmOEx-Tjwq70U2IEhlXjRsNkof12nKFiycQncViTKk1V3GTRVZIoCTp4i-T0F2GcJeEvzr1PTgEGNsy5_uIsVK4mHCtpeNdmCtulUkbfQg4BWWfURFSV5BFihMuVSPQHL6i5KNRgHYZ6ETey-H1XKqBrcMXHt4ghICKxfYbKSoqwr77ikbFS_QDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مداحی غلامحسین پیروانی در شب‌های محرم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/444559" target="_blank">📅 21:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444558">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53c3e8775a.mp4?token=hsxPaeRbqoeozihQieS8BxpJixi9NM-clpl4es_NWfVxxrez3kn4zd6Zj2XqP_sMAqO0SD5dnB0X3AkK7CT_g4a-XdAoMh3ZUwajcCIYCSmPLhZyDd01VU4KLHpeJvArWayZtsNW3M6STh1IhaROVFlOHmEHyOaALAsFn8N2G8nIWSNNhsnqCk-QeEVcdTBpVi-K6OS7SdfaLqnf6_oNH4o9cUiE0semfpQkMO7ZSr6b7_2FsqZK7GY3awgyJMlwFKmJXJQ8u-wdeQu833kbPXuzlVj3cCAack-PsipO_51HQ96kX_9vs8o6DCcrsiQqI8VRFK3LtSMUaxYUxUFaFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53c3e8775a.mp4?token=hsxPaeRbqoeozihQieS8BxpJixi9NM-clpl4es_NWfVxxrez3kn4zd6Zj2XqP_sMAqO0SD5dnB0X3AkK7CT_g4a-XdAoMh3ZUwajcCIYCSmPLhZyDd01VU4KLHpeJvArWayZtsNW3M6STh1IhaROVFlOHmEHyOaALAsFn8N2G8nIWSNNhsnqCk-QeEVcdTBpVi-K6OS7SdfaLqnf6_oNH4o9cUiE0semfpQkMO7ZSr6b7_2FsqZK7GY3awgyJMlwFKmJXJQ8u-wdeQu833kbPXuzlVj3cCAack-PsipO_51HQ96kX_9vs8o6DCcrsiQqI8VRFK3LtSMUaxYUxUFaFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«ای ایران بخوان...»  @Farsna</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/444558" target="_blank">📅 21:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444557">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89d773d41.mp4?token=IZvhiSd34rElQmKRyaDlA6w3WLOlXoI4N7Nz1R3cemUh643nwVwjYY3me_KAltwRVafUvmG4q3mb2bUIX640A395wF3WSZoK_LdCecmeEFtme3FZHaN3dWryfsbrjVNKAk-qDvLHfEIMTYjBTKjJnwLszq4lX21Yt3hxGi0aGU-aLdrrZNYhRDNjPmufdlhcuvxslPGc4edJACAuDD4o14DUybfF60xKRaTQ6N6xGsXtjNEVkdm0R9_iIDB-0ckz8oEKnFhIAKRrzQIFzNzffKGXj6iM07ReNJU1DKH3Uh_xjqX-oZbxy22JgaG4rGwEJAciIjGoITJrX5TQDDks6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89d773d41.mp4?token=IZvhiSd34rElQmKRyaDlA6w3WLOlXoI4N7Nz1R3cemUh643nwVwjYY3me_KAltwRVafUvmG4q3mb2bUIX640A395wF3WSZoK_LdCecmeEFtme3FZHaN3dWryfsbrjVNKAk-qDvLHfEIMTYjBTKjJnwLszq4lX21Yt3hxGi0aGU-aLdrrZNYhRDNjPmufdlhcuvxslPGc4edJACAuDD4o14DUybfF60xKRaTQ6N6xGsXtjNEVkdm0R9_iIDB-0ckz8oEKnFhIAKRrzQIFzNzffKGXj6iM07ReNJU1DKH3Uh_xjqX-oZbxy22JgaG4rGwEJAciIjGoITJrX5TQDDks6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چهارپایه‌‌خوانی در حسینیهٔ بزرگ
انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/444557" target="_blank">📅 21:36 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444552">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سخنرانی</div>
  <div class="tg-doc-extra">حجت‌الاسلام کاشانی</div>
</div>
<a href="https://t.me/farsna/444552" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
#حسینیه_فارس
|
شب عاشورا
🔗
سایر مداحی‌های امشب را
اینجا
گوش کنید
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/444552" target="_blank">📅 21:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444551">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/444551" target="_blank">📅 21:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444550">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf785ab21c.mp4?token=mkHcbL2ouz-NnDS1K7pdOsHKISIlDNpKusxewWPG8ap2YxjMLrXYBznUWPEiwObgpuCZJRmc3z3DqJz6EbCgDJ-RFQKOhIqKVH4NggVD2GjXt1gC51OgFNi3yUywq1x-HkuUuOxKAZrGVOr-DVnJZADfe-pyWRefq8SyBmuMkzeFFycsXzyzDZIPcobHlATySRwb5RqSU3xY6KiMS1Zkp5HvzYysURFAr4eAM-QEeH4YeB5lf0FgNywdX5nlLnq0sRathDbkeDRbuj_9IzUxy2UHcRT6Bep_IGdUw4azlD0nEQgBzU3tXA-ZDxniT3LSTUZPkzkrqoR2_VxRf7arxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf785ab21c.mp4?token=mkHcbL2ouz-NnDS1K7pdOsHKISIlDNpKusxewWPG8ap2YxjMLrXYBznUWPEiwObgpuCZJRmc3z3DqJz6EbCgDJ-RFQKOhIqKVH4NggVD2GjXt1gC51OgFNi3yUywq1x-HkuUuOxKAZrGVOr-DVnJZADfe-pyWRefq8SyBmuMkzeFFycsXzyzDZIPcobHlATySRwb5RqSU3xY6KiMS1Zkp5HvzYysURFAr4eAM-QEeH4YeB5lf0FgNywdX5nlLnq0sRathDbkeDRbuj_9IzUxy2UHcRT6Bep_IGdUw4azlD0nEQgBzU3tXA-ZDxniT3LSTUZPkzkrqoR2_VxRf7arxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قابی از خطبه‌خوانی شب عاشورا در حرم امام رضا(ع)
@Farsna</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/farsna/444550" target="_blank">📅 21:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444549">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e15d67975c.mp4?token=qOp9tkFlficbMreuUz4AR5ghsWG8F-73mD0zWIUm9C_npb_WPBwOeP5tTj96ezFHHbC5p7mBZuN6F7DVXD4mqtlNcTZ3VXMI2Xf5d8QJVfpnO_aGHkTKJ5OMhILj-M9-Y2Yi-nYHUxzBQz-n_stwYwqF-HP0rdZ9sXoeGzYg0Z7bC0JHpDrzEh8JQyvCSy56cGn31xk9sr0TYi-D654RUs7H-yhm1ZK7xbiuNdwIZj3vuSy5652tHMo-FxOhbW0JwJcjb5TIMosFxZPNd8TMcyE3rW_VGCEIhYJ7gUNRkXfHEU1RiHxuiCuWOY-xHjFQ7gb82RMvH0J9eDQOrPWaVzAaLgD9j_MJhVJF2SXTo-vpngO9emzjnpWlc3j3kAaNN8WcctdHfUBnfP__k0RWcECwBZVcvfVU4HqkzkTeplxmjQ0QkvUqNVGSbA2hK-lGkZao1hyHs2obGL18RCpcdsJynxyZcMub7k4sFqk-N6IqB0fMSgECPJEzF_slOBUSOsyOe5RJiIIyv5htSKSdJoNIFwXxb7FLR8T9podITyC90BSGb5ITIm0iblhz8ecD8QB8OYnAOW_uQjdAL3F_j1MObUzglACLqfgztj40qORfzcLnTPsUwFKu00no8xVTslR94PaqhGzYtTzFZptO1fdLx8E_SUtKOxCuBQa2m2o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e15d67975c.mp4?token=qOp9tkFlficbMreuUz4AR5ghsWG8F-73mD0zWIUm9C_npb_WPBwOeP5tTj96ezFHHbC5p7mBZuN6F7DVXD4mqtlNcTZ3VXMI2Xf5d8QJVfpnO_aGHkTKJ5OMhILj-M9-Y2Yi-nYHUxzBQz-n_stwYwqF-HP0rdZ9sXoeGzYg0Z7bC0JHpDrzEh8JQyvCSy56cGn31xk9sr0TYi-D654RUs7H-yhm1ZK7xbiuNdwIZj3vuSy5652tHMo-FxOhbW0JwJcjb5TIMosFxZPNd8TMcyE3rW_VGCEIhYJ7gUNRkXfHEU1RiHxuiCuWOY-xHjFQ7gb82RMvH0J9eDQOrPWaVzAaLgD9j_MJhVJF2SXTo-vpngO9emzjnpWlc3j3kAaNN8WcctdHfUBnfP__k0RWcECwBZVcvfVU4HqkzkTeplxmjQ0QkvUqNVGSbA2hK-lGkZao1hyHs2obGL18RCpcdsJynxyZcMub7k4sFqk-N6IqB0fMSgECPJEzF_slOBUSOsyOe5RJiIIyv5htSKSdJoNIFwXxb7FLR8T9podITyC90BSGb5ITIm0iblhz8ecD8QB8OYnAOW_uQjdAL3F_j1MObUzglACLqfgztj40qORfzcLnTPsUwFKu00no8xVTslR94PaqhGzYtTzFZptO1fdLx8E_SUtKOxCuBQa2m2o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پنجره‌ای به آخرین حضور رهبر شهید انقلاب در مراسم شب عاشورای حسینیه امام خمینی(ره)  @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/444549" target="_blank">📅 21:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444548">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3e289071d.mp4?token=jHIZzdNWpFiPJk5OOeAKrf_a2tRXLCiWUfpftc0k2S0CKKjc3e3Qq5K4ARDEBNfUfOvanIWlDdkKfTH8idpCQSeNC2dhFCIsF0Dhmix9anP_yr2OM1lAc5qNGFoz8GGecXlSGDIZIqGq15T134Ln8h9KZl2D_7pHuuy1Df65LO-BpO1_pWed_n-IFYA2pE6Nbsy857E2wH2UAfpKnwTK29awUYe11XalOWi9fSKg84KG7kvq7m7yTezF6oYWzj4KqLJ9T3pDakWI6CaU7x_TtaAkEpFdaUKpTFZKub7rmdB610ZaoJLJx9JinmAgadzZph64zpihfJC_RfPMK01HNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3e289071d.mp4?token=jHIZzdNWpFiPJk5OOeAKrf_a2tRXLCiWUfpftc0k2S0CKKjc3e3Qq5K4ARDEBNfUfOvanIWlDdkKfTH8idpCQSeNC2dhFCIsF0Dhmix9anP_yr2OM1lAc5qNGFoz8GGecXlSGDIZIqGq15T134Ln8h9KZl2D_7pHuuy1Df65LO-BpO1_pWed_n-IFYA2pE6Nbsy857E2wH2UAfpKnwTK29awUYe11XalOWi9fSKg84KG7kvq7m7yTezF6oYWzj4KqLJ9T3pDakWI6CaU7x_TtaAkEpFdaUKpTFZKub7rmdB610ZaoJLJx9JinmAgadzZph64zpihfJC_RfPMK01HNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
قاب ماندگار از آخرین حضور رهبر شهید انقلاب در مراسم شب عاشورای حسینیه امام خمینی.  @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/444548" target="_blank">📅 20:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444547">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWosva91JitPjYkIlUahwiAYBlrglunPzoXDC7ijg1Wy0aTaltjrKTYFvWCOMfptcax4hp0F82IaibhIQ8Vdy1wgQi14ykASaDDrstS8NcvmLkz6a19NvQaOPNq1nqrCgIoTC1U-GZOkonc9FLr00EvKWGDluCv_SNaRpaKTjpZqebt1St7FoFH1PVh9tRZ_FZISn7alyw8ypMNgfHouDV4vi1XgiGY9FFX51pS2UXaN10DeYm-lvCEPGBp0KZjPNiTmubM8Yj4JVutRBR_96yOHPpmSgHB_ZB-Cqj3Ztn2GP5AvPa2tHxYylh68Q1KRsmz2qpiKnZTRkZBNydQgnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
قاب ماندگار از آخرین حضور رهبر شهید انقلاب در مراسم شب عاشورای حسینیه امام خمینی.
@Farsna</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/444547" target="_blank">📅 20:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444540">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f84p-gBQhcBSya35V4erFfp1F-y3yjUdaukJOuEXqPDkwGVu_rBvcmBPl8v2v9x9LCGhUXlFpavN02CQCAr3naQlAbUkGVYRJ48WjDnBHSv2SxM_VUc_lGgY-uVLidyqNWY6QecFMeLSnB_kAiQze152idvxOvpwB8pt_jl5MaI2RbRMBd80ckPinQF96GwsHBeJq8itug63Xy97RrgKUGXTGH_C3MWin3VZiQHSGzjLyxGZvMqiQA0Q7z6NXOeDfDJbyRlCo_3Ekv1AtSpkRoVunWAoa3QYRef37j62Kh9kLq-JmGkey9gyv_xILBskFNG9E4HQFiy5P2CTMYUlxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o9V0B-jxYvSNkL2x1zjhhkkk1LzrTiJTVXhh0uSqVmjQ8vFImB-xwa1M7sntCtvxdA9bKi5obNz0yBEXPZBqIxUfGlx8C9hiBZE4DV-62mh6Q8n8d81ld4RkGvrkGP679xPpESAf7dPxw7-p7gCxdmhT8PHf9lXIYvRaDtEZ4QFMrubXxb4C14QWjJtg1468deA4kGbWncI2dDLXAfCidzStr6Y3lSg_ULAqNd0aXEIAJZdEmMEEzIzYVHxGBEc6RwCZaKgRGw915sAGmU8-tTT1vvR1AfP_cL279verH-kYCb-kb-4HWmxOfzjRCaZdfh5EFNn1hb-GvdYg54zbTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mqRjewuxFaL_63IZPBjyu9wWBHxy1bQEhClVmrcdpgwzJZVJN0LoEQlEDvHH91xEPElPQVBycg4d7Q3s2Va0kvONFUsMhTgQoI0cnrYmBoLe_heFascOCzI2q5YQ1MWAZHE9E3SAOI_buzLffolSZielO2Dr6FeqDmPU91UnMgUcCxS8uI3fL8kQ3-PUz04hQiHVQIjnFXBZVR2KUkYo2mI-MHog418a1AL_KBslsVDq_MWE8gT1Do5ITQWOpOHyPRGRBmMW_bPwGPBW3ManEEcvf2P5EscLYoZl0gjdI7bLUh_EQpevtZUyBLixREwEdeGrJDY1Uuhdvr6cCLt-Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H9VyXKW_UqZJdUC57blTCn3YOk1zios4-t6FbtzO5PQRJ_9WCLr189zaF5CraTYVGm6-KBoFkGJzH-NhnLkZ-TzSd1ahbutfqvj6tkSti8md0eIv_Mt5HD2MYRtm3sVwOxZTzlHj3rTzKrVlFBP1Cas5CCyhtOzKXCdSp0eVdsAp6OsfSMoG4cb1Zck7N4aWmBgYoG_x48Zh50nCFxQUHNzT6cnV5xrhuC2fEtnl8MvqVaTt3iB3k38qumH9_pn5bFWTDKy11dinl9VT_x_tOT9gLBcZkAOdsPYDodgtf5c9BH-NZPwJbucJNdO8xN-122uBGna840F1ewAUN7E1FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PUunHocGi_QGtE20L69ZQGEcTcfkEiWYHYsgYPTEMpAfhA_HFGEhpKwLU2SQ3E6_fKL9ifwuRBJqBlKTAqs4xay8lP5y5YJHfd98phfVKh-JGlNUpdiESkjO2RFuJzO8gT2qxsjO0-1GL8sn6ReQtEBwJV2PLfsg986sWx9Yn3XdKiMssp1I-eQ_k27cHJWDsaq9fCVdn2UdX8zqzuELuhE4QMlC_tdFLzEv2sgT28bK4K6CA4wHuHEsyrLruocybYis-OzX3wAAi0AvG9u1vOrM7lxTzUTbis_vTHQpXxV9cbFsalWDSxUf0KorDZF3yAM9y_xDULaunpR46BtGRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d3gwimFGpcLlCbBwoyqG9Yc6ucFUF7VjN-jyYk2eO-c1I18BSaSuWBa6r0aQ6dW-owvJRWPVGilWtUMMvaly0LWdr0S-OVRkvoChPvqmeFtbQOKxPw861YJdvdI7HBSZApEbCsrZM_tPIt4dTMZnMq1-dAik-2Fvh5GNBHMQROXa6UqMQ-4wxUtbSonc8IqvLQ9LyNx7OybGKfzIPuUzt1e4tQoP3H5T_Gyk5Hr9GlWPO_AL8TutnozvgLrqdTITfbxUwE6qTP09X7lFiWWbEfIdn6JhG6U7bdGg80iJKaU-jTLMgyKjQaGJ41dPTl0IJ8s8sZmKDqRmEPCi4I4xNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GMQz-yWZ1NwWporCd5PEWZcDHbUf1F7XmwMBHZteR3rv5_yY036lBdeAb_15oeft7fTc-NcF7aga99OpDajfKKUa9D4bkqS9EdYGyaiLa-ADIR8MW_F1EZ_Q2s6GvQFdhX26aRCMr17kqqcyzlXsMPRMCYdl8FD-pkqlX0IbtIfMem_xzqxpD-sQqaSoN9prSSfeiuoqWFEylmgdzBxDyqBIm6oPzOkjOjC1Kmc9QfyzXNGfbzjE5IRbTLs_VN2NeIL2AhTZiXRZiNx_nctD2iqWr5lma8PCTuo9apFwhE7mkMWt6LXdbk5pbCnQshlOAJWJhpfu5vqZkvrXfUHaLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عشق و ارادت زنان روستایی به سیدالشهدا(ع)
🔸
اینجا روستای آللو است در اهر آذربایجان‌شرقی است.
عکس: مهدی ایمانی
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/444540" target="_blank">📅 20:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444539">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d870dc59fd.mp4?token=k9gA6BMY2quocoecBzcbhCR8ifMrM_zKaapW6tQyNVKu9t_IjHmp0gJqhMMMK_zgGJNArSrF956B5NQCDtk6qYJx_ALlTFE2lPZFdEASN7ElqGOnTO8g-yCzkqWI0saEQvq4MEg1r83njNRUQVr41xeGNjJhf6wZ--NAVX8hXjbwUXhk1T2QmIWjwbdlgp7xgU5LOxvM6VgYPzaL16ATDVws7wf_XCP3dQeneerHgFyj7yHHtwGrCkdF9iFCL3Y2Wqw3vo6ftmC05JYsNvLDOzCnn2By7Dx6HqJZ4uaaWSXGf7tNvxLcZFu2CLrJYC1_zLAa1BLZ7g9PvCH2b7kyZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d870dc59fd.mp4?token=k9gA6BMY2quocoecBzcbhCR8ifMrM_zKaapW6tQyNVKu9t_IjHmp0gJqhMMMK_zgGJNArSrF956B5NQCDtk6qYJx_ALlTFE2lPZFdEASN7ElqGOnTO8g-yCzkqWI0saEQvq4MEg1r83njNRUQVr41xeGNjJhf6wZ--NAVX8hXjbwUXhk1T2QmIWjwbdlgp7xgU5LOxvM6VgYPzaL16ATDVws7wf_XCP3dQeneerHgFyj7yHHtwGrCkdF9iFCL3Y2Wqw3vo6ftmC05JYsNvLDOzCnn2By7Dx6HqJZ4uaaWSXGf7tNvxLcZFu2CLrJYC1_zLAa1BLZ7g9PvCH2b7kyZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر خارجهٔ آمریکا: اسرائیلی‌ها با تفاهم ما با ایران مخالف نیستند
🔹
خبرنگار: آیا شما هم مثل برخی از بخش‌های نهادهای اطلاعاتی آمریکا معتقدید که اسرائیل به دنبال تضعیف یادداشت تفاهم فعلی است؟
🔸
روبیو: من نمی‌دانم از کدام ارزیابی اطلاعاتی صحبت می‌کنید؟
🔹
خبرنگار:…</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/444539" target="_blank">📅 20:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444538">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgYxHdMZhl82DIDpBstR0puPxNu8R8spfRXoFxVcqq6yrlv2VQ8BP5qMsWnLzIEzxNl6UFiBwyFrhLBbBtdqJBVQ5CdpvSgkPj0BD2uAwRWItWZ160poyE4N8vnx2rysymXqrm-j9_dvk1FKmmP27eIX2oaWGySjU41IMB0HkyVMpjMXVEJjVt78u6VTZzNvvjJkvWTR-F-Ue94Up3KgYf4MLscPR8bknQWLuc2j7mHg_vZWEoAN8r0DZmarqojPwEODILjxiQBZNVpBzkmbHl_rl2_ndsS6YJTUFMdK9saZyXKpn5bYOVP-yvDT03suW7rEo85_T4J01autity0Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی وزارت خارجه: صلح واقعی در منطقه غرب آسیا تنها با پایان مداخلات آمریکا و خاتمه اشغالگری محقق می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/444538" target="_blank">📅 20:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444537">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70f70a036a.mp4?token=X2U0L5cjMAmxcuEliqmLPCbUw8G9v5mmssiEtJ8JRtyKF77c_h4FTSeXfkvAXLdLs7PmdCp8POvZ1kyOXxzYiZoVY7xgXFYdwP5O6TQg6MnnsGNBAQqtKjt18Z-Kj5zi5s9iFSB97udwLtmDmE0_pgY2Vh-gWcyIIeRgjpIc3SrfNwVtFmkJMHAorPPc1M0E82yilAfPPF1FtXHs_c1zTOFHTwqnRUKoPkG8Ipz1zO1y4yCJLqHKyfu7fkAQn2g-VGuosO74ly1CStLbNdmAPqU3tO9-JwJH-xMhjLI1NkM1pJGvHKGe_u-t493bf7yg_h-Dg9pZgzLsf85AlPxNmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70f70a036a.mp4?token=X2U0L5cjMAmxcuEliqmLPCbUw8G9v5mmssiEtJ8JRtyKF77c_h4FTSeXfkvAXLdLs7PmdCp8POvZ1kyOXxzYiZoVY7xgXFYdwP5O6TQg6MnnsGNBAQqtKjt18Z-Kj5zi5s9iFSB97udwLtmDmE0_pgY2Vh-gWcyIIeRgjpIc3SrfNwVtFmkJMHAorPPc1M0E82yilAfPPF1FtXHs_c1zTOFHTwqnRUKoPkG8Ipz1zO1y4yCJLqHKyfu7fkAQn2g-VGuosO74ly1CStLbNdmAPqU3tO9-JwJH-xMhjLI1NkM1pJGvHKGe_u-t493bf7yg_h-Dg9pZgzLsf85AlPxNmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر خارجهٔ آمریکا: تمام دنیا با هر سازوکاری که برای استفاده از یک آبراه بین‌المللی [یعنی تنگهٔ هرمز] هزینه دریافت کند، مخالفت خواهد کرد.  @Farsna</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/444537" target="_blank">📅 20:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444536">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbb70bb9be.mp4?token=JFibQBMCjxSyd9ox2kI1mLpTfLTF_HCx0YMuZbn4jj46MbF1wSMpbydq53Y7aVDC_kK-dHVwEzEPxQ1r1zTS3YvBObrM94EzsKzZpCaRYKuyzCwazl9kbRg-kHDdV5dm4jy9xPs1YIAXxZvx8ygxtOqcCH23ngwIV4zSGaIXVFxmDCaGWrTF8hIvR6JMmMMQ6GTDUdnbatdddP0aVQPUsFPgM1rOZBXp_L0TSnXLVmTHYyTu08LfybomcTOUWASqkMuZf1anGRCGE1BdfjCA3hjkgXtrfwOSCq7nmYprLiS64BKE5b_LliohChaVnmCYpZf3gjGt-tFEJvNcSm4GCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbb70bb9be.mp4?token=JFibQBMCjxSyd9ox2kI1mLpTfLTF_HCx0YMuZbn4jj46MbF1wSMpbydq53Y7aVDC_kK-dHVwEzEPxQ1r1zTS3YvBObrM94EzsKzZpCaRYKuyzCwazl9kbRg-kHDdV5dm4jy9xPs1YIAXxZvx8ygxtOqcCH23ngwIV4zSGaIXVFxmDCaGWrTF8hIvR6JMmMMQ6GTDUdnbatdddP0aVQPUsFPgM1rOZBXp_L0TSnXLVmTHYyTu08LfybomcTOUWASqkMuZf1anGRCGE1BdfjCA3hjkgXtrfwOSCq7nmYprLiS64BKE5b_LliohChaVnmCYpZf3gjGt-tFEJvNcSm4GCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جلوه‌ای خیره‌کننده از ارادت نجفی‌ها به سیدالشهدا(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farsna/444536" target="_blank">📅 20:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444535">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02f0694113.mp4?token=rY_0Rqv67HxXIbR04cNSbv5aZ3OmnnUMc0Dh5D_KJyJgEZmPNQYudRb9Mb818FXlMWjrr5Cd1tquSGHvaYZRBaI2EYSmsRHFnva-a88s7zX_jZtbXuq23U7_teuyzfzIG1DzHC1qr8BBSIsh1EuzHYokf0_eXGRNaQIUSkhswoOPl2iUXOl5V6nYK2RVCvQ8M6CoHNgoThYk_OMFY640d1dBxFuPpJ1qsiNyYLqPt7c5S4Q2eACY2Zo_JpYVnF_Dvea4owDWhL2T-JVl72U24MUJXhXdPm_TQUGKFirPSeUKWLIMKT66_CdURpzzw97azFek52pyskJzNMDTcJYF5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02f0694113.mp4?token=rY_0Rqv67HxXIbR04cNSbv5aZ3OmnnUMc0Dh5D_KJyJgEZmPNQYudRb9Mb818FXlMWjrr5Cd1tquSGHvaYZRBaI2EYSmsRHFnva-a88s7zX_jZtbXuq23U7_teuyzfzIG1DzHC1qr8BBSIsh1EuzHYokf0_eXGRNaQIUSkhswoOPl2iUXOl5V6nYK2RVCvQ8M6CoHNgoThYk_OMFY640d1dBxFuPpJ1qsiNyYLqPt7c5S4Q2eACY2Zo_JpYVnF_Dvea4owDWhL2T-JVl72U24MUJXhXdPm_TQUGKFirPSeUKWLIMKT66_CdURpzzw97azFek52pyskJzNMDTcJYF5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا: پول‌های آزادشدۀ ایران را ما نظارت می‌کنیم
🔹
درصد بسیار بالایی از این پول صرف خرید مواد غذایی و داروی آمریکایی خواهد شد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/444535" target="_blank">📅 19:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444534">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad5f64c27a.mp4?token=usukStEf_yE5yFCHNl_ao6qyUuvTW8qbthPk3Qy1mB2URR424YsDwCValbv4LCtMF_KGFcl6wQ4yh92Rbfz1aRGmRMys8Pt4TpbghKb15igyAV69-k4FrZ5WSXNcSb9IsIbSZkN2PIQyW9Lf-Z1S5xJ9HgWl-eacqdSOHZQF4kOUXmCPNJS4bidzAO65gXKj7f-2PPPb8rU8jIfqWOCWMNBOk6OM1cFjYJ-y-t5YNLKTk8yriz6q9CGjsLUapA1_gJ0LdeRENXKOq3dgfQihALJGrZdyIPQbUX8D3VU7VsSRfrBUa1qAC8avj4DsUvLERgeiomcPs47KisWnZV8F7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad5f64c27a.mp4?token=usukStEf_yE5yFCHNl_ao6qyUuvTW8qbthPk3Qy1mB2URR424YsDwCValbv4LCtMF_KGFcl6wQ4yh92Rbfz1aRGmRMys8Pt4TpbghKb15igyAV69-k4FrZ5WSXNcSb9IsIbSZkN2PIQyW9Lf-Z1S5xJ9HgWl-eacqdSOHZQF4kOUXmCPNJS4bidzAO65gXKj7f-2PPPb8rU8jIfqWOCWMNBOk6OM1cFjYJ-y-t5YNLKTk8yriz6q9CGjsLUapA1_gJ0LdeRENXKOq3dgfQihALJGrZdyIPQbUX8D3VU7VsSRfrBUa1qAC8avj4DsUvLERgeiomcPs47KisWnZV8F7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">◾️
ما منتقم خون امام شهداییم
◾️
شمشیر قیامیم، خون‌خواه امامیم
@Farsna</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/444534" target="_blank">📅 19:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444533">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad6c8e3e8b.mp4?token=MPvHZvYGc8TiImzPnbDuK-51P_db9dn9TDfmOIdic8xVyVa-Vxe_h9vDXY9MzIp1Y7Z8nyfHreVoopz-HLnRCqS-4RjIlBHAQR3gM5_ikYpkHY-rBAbn2sUYF-zVU8i81r81GmnHQGPu7Kk32oiJrs3m0n-K0yOuULzkgNiPnnOHEfK6DDFcF8yNJSZ8Kvts7tvneTO2HGnq2JKULMgPpwYq1bPCx2CR6ZVSdRX-aa6g6Lko9W-veSImoEIXCJkaP59TX_VinGwEBTaa8RidLn6lZEperVE58wFOIMxoxA1xGdEFgiMQyovlq8mzXzfviQI8Bf2UGEcVm4RllchasA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad6c8e3e8b.mp4?token=MPvHZvYGc8TiImzPnbDuK-51P_db9dn9TDfmOIdic8xVyVa-Vxe_h9vDXY9MzIp1Y7Z8nyfHreVoopz-HLnRCqS-4RjIlBHAQR3gM5_ikYpkHY-rBAbn2sUYF-zVU8i81r81GmnHQGPu7Kk32oiJrs3m0n-K0yOuULzkgNiPnnOHEfK6DDFcF8yNJSZ8Kvts7tvneTO2HGnq2JKULMgPpwYq1bPCx2CR6ZVSdRX-aa6g6Lko9W-veSImoEIXCJkaP59TX_VinGwEBTaa8RidLn6lZEperVE58wFOIMxoxA1xGdEFgiMQyovlq8mzXzfviQI8Bf2UGEcVm4RllchasA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری انگلیسی‌زبان‌ها در حرم رضوی
🔸
زائران خارجی حرم امام رضا(ع) در روز تاسوعا با سخنرانی و روضه انگلیسی، ارادت خود به علمدار کربلا را به نمایش گذاشتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/444533" target="_blank">📅 19:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444532">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSi-Gl57pg0dLNRyvdh_TfSd0DKBhhzvjHvEBCTcGD46EzUzRYgdgPb8VOgIdG-YoUQGwbVkY7VX3kP9hsal5c-EO0Km1CK3FI3mNboEJ9XQPaUvxbFmP-zvtfzoYPOBOppIl2dG3ITuanxtG1ruXFD4bVV0Pr12ANtbQOJVCiN7Sk2pM8UqtHaUrw4TkyOtG_KDqXfaoU3zjsMH_o6KaOM5jNNW6We_A5M0ws9sP4YSz59BrCk2GOqdCkeUoMdxdagTgADEZ_6zf91osSLVDKixiYLTjZdLheaujuzKd0uGtLXia4FDCpviuqp81JmC3OLr4eHzSgcz7u9L8gUQLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگراف: ترامپ ممکن است پس از انتخابات خواستار توافق جدیدی با ایران شود
🔹
روزنامه تلگراف به‌نقل از منابع نزدیک به ترامپ مدعی شده که رئیس‌جمهور آمریکا احتمالاً پس از انتخابات میان‌دوره‌ای کنگره، توافق فعلی با ایران را کنار می‌گذارد و به‌دنبال توافقی جدید خواهد رفت.
🔹
به‌گفته این منابع، ترامپ برای مهار فشارهای اقتصادی و حفظ موقعیت جمهوری‌خواهان در انتخابات، به توافق کنونی با ایران نیاز داشته است.
🔹
منابع آگاه به تلگراف گفته‌اند بازگشایی تنگه هرمز و دستیابی به تفاهم با تهران، نگرانی بخشی از جمهوری‌خواهان را کاهش داده.
🔹
با این حال، برخی جمهوری‌خواهان و مقامات صهیونیست از مفاد تفاهم اخیر با ایران انتقاد و آن را امتیازدهی به تهران توصیف کرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/444532" target="_blank">📅 19:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444525">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qC88KX6_DNp6sCTzPFDGbm8sOuFj5Og7XXspVzAVimkOxzsBD9zeteSAmKG-q_4H_lhc99JsxK5x8VdO9YoRdovTrA7IiBEvvVLDFewGmbphoBxY9M0KrSiZ2wh1Le3f_EW1jPnQTIoBVmaTsIrb7A5jckSVekBtOewE75Rli7Bvs15eMZr6oXs3NeShXaBtaZEluo-tXc8RTWdzx_d5XgGnzMdtIyGxUyVHp79FWH1BdzjjpPKSvkEob3Ku8woyc9M0eaGLBB16WGTOrHu_Ws_KAVSpjC3ef1i3z50vjFLqCnJ4nkks4o1eEhHofbAcnmkWwPhAHd1CsUjhRYq1-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hWm-H0Y7MNI9TDBQJ6oYKdIKNoj_ZntX2p3KcNuF-XJ4WhCMQaHeFGKXsO7cSU545f9p8zlfeYFGPk9yqTmoaFB7Zrl4FbpoPD1ZDygmIqiXODR9NB6V2cGtp6hsBlwjVbwDEJo08k1RDaCa0heO2fhZEoENrZlGYbXmGjQjCqSIPzCEyeshYLUgV8kPpfzxVwW5MlpTz4GtTsbN730uHxywGN2P2hKF8zV9iT0Nfceh9vKhhHlySUeMQCqQZDOCokLhudewhuSEJ_IQBHOxzMtt1oMQ3AGGNvk_D8aK_4ox440GLD3Dp7NqYkitKlcBWpXj66o8iF3NgozxpueQCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iHymX5_cqfHFagnK10UUBOhqy1o0TUAWHyIWCOUPkthAJPHjCM-gmJosOCgxwwFJmUHuUJ4ERYU-aX9ale4FD1p_rzmJqtU18Y4Mu7B3fWffSHJ0LWMySL-LX3I0RL0vF9FLcaBfT3vfQ6sBELKL0YnIoU_2w04YdNVGkicrEUMx_u3EMp13zksOVs89at4l-i8PGC_LPPMiJ78Ku9ANSXDF02V3om9Rz6wLtzLL2YFJlgO1OyIRwvcUW4Z8Ur2YOdA08_8rceFgHs1kN67slJieERMXgYxhXZvY42OT49NqtoauQq-EbcDUFMOwEXzTu0cCrqDOvb-PizYc1rZkJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fyAYwKEDF6Z-0Yae7nwl1IqEfFxyiuft_RlxpPRYRxY_2Zr2nR_i5RL_uoQgbOAKxWRTkDoCO7aYNuMX0xBruwO5-tLqhO1txwwjfsqMjvGRk2YQ8od2S0Tc08nnUKo7vJ8KF-N8si49zzlLA4EpXx9btwAWoSUVdIZA1aP8hSlUApsLLlAp1DnRZkfnju-9-dGmblr5hvCqg9h-8yDilmRdEt9L-fSiwylsJwH9QLpOzs-v1G5KxMbCglfE2vT5CizlYv95lkoNo4Bh2RZPLpfOH8ik9O_78-pENfPZn174Fq_8ZAzGLmxK-rhufjVp9wXY4gNT9RatqOomNptfwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/djigmPVgq3jjgvNGlbjyW8UhMickoT_-Mii6JOPstlTp6Hj1UTpZUWQJdJoCje9ctRAFmbdc9b_OZkaVGyIupXEtqZTW2DDpKNCDpXVlgMBrkpHj-MJW3FG1UqlZDi4fGzdEAv5-q3RVA3PrFHoCmT0ZnIdBf7rQx5tgxekDVk9VqkgxkW7zeJt0PDRto99OLtXxxAyJJJEBkfYTtuudlMDHk7YPhAzrHcjFu54RNUZQ_UuKU2ui7IFXGT0qQTXRGmkLEJR8ShMHNV7_BC9B-1I48HzxCl1CY04uyLvIGEQCEYkkzUz-GBMfdfP9cFse6RKf30BerfbOpUX-dK093A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A_2DULzdLVSkUg3aQEiPPfjbzKflQ68cOLFQCACjQxgDWZRTITkm61KFwESiH8Xf0z-1IPGMUCARqrmnmM7g9-W8oUeWFapV0FPMkK4hK5Jv2UHuXaHymBeGTuhsq0DyCN9HAQWqSn9jZDANU1T9ly-M8u6cCaZ5L4j9pzETMkCs57y-uD6UVUuLh9Y32dOWIciXnaq79Cmbho4WKs2NAwUKBljWCpWdqjDuRhWDbRsUPhrv_jog80JiR7ZhMRrVOJ05hv3LIskIV6UytFhczCNtkGKXo2qQv9McJyfHu6UbFwfxlsVnH6uT7KKx_IUlJolekUpSyImN6itiTPqo5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AhaXcYDb3kSUqBX9lJDAl5Vsie0IMQJ5obuOL1RerwMgEJGSXGp2wfHlV8rU4MEsKMFVgOerPVLazUv8S4uTnqR1_yhpfs8KiO_30VnDJV7SHmVPcswAJkyHedmY8js9I6hHUpKF3uFiKR-T7EmGTXs0v_P2wYW1J4fH3uLghqlXaY7CB5tlChQ3pGqMiEZ2HujiHSWf-PSnH5iN0Mcth8HLt33Mbhxdw2MJdAdNxppga2qOc4rMFroC655a0Dx5s3aR_WIM5pgfCZxaFGj6S46jnDwhoxB-9H8E5YCF9NgwgTpxmCRIVvBs2ewPk4GFktVeI9NYTC5qJZmE1yi4lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نبض اردبیل امروز با نام عباس(ع) می‌زد
عکس:
رضا خانبابائی
@Farsna</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/444525" target="_blank">📅 19:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444524">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fce2631e4.mp4?token=AF5XI7Mk4uWMywUX9JPNBJC9jySFkqP-V3_Tuh-Z_ngpYXP_NU5w-sbCfcJHQuufvm8V7ZF9dxiI45-qhPW96joFJMIL0JLtcl8Nmq9xozdBFuBcEtg4JG3Y3XZe9KE_3mYD19H7qAOPTcw7eqYF0su4c1w2ysNWqYY5CjT67mLr2mrayX-rTyqvGT4dKfDRNA5no6SOWM9Ki4xtqMXSlf1hgFjqf5oZngfGItvTtwep57FOx8oDiMl7Svkzv-iWviqrbmuU5NSOD4rzTzCiU1iiCvf8DFrRqJtncHqcAB4wPUv826YZHvM8ON_Qez263Mj7nSpNo34H84nzXFwJ0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fce2631e4.mp4?token=AF5XI7Mk4uWMywUX9JPNBJC9jySFkqP-V3_Tuh-Z_ngpYXP_NU5w-sbCfcJHQuufvm8V7ZF9dxiI45-qhPW96joFJMIL0JLtcl8Nmq9xozdBFuBcEtg4JG3Y3XZe9KE_3mYD19H7qAOPTcw7eqYF0su4c1w2ysNWqYY5CjT67mLr2mrayX-rTyqvGT4dKfDRNA5no6SOWM9Ki4xtqMXSlf1hgFjqf5oZngfGItvTtwep57FOx8oDiMl7Svkzv-iWviqrbmuU5NSOD4rzTzCiU1iiCvf8DFrRqJtncHqcAB4wPUv826YZHvM8ON_Qez263Mj7nSpNo34H84nzXFwJ0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قاب‌هایی از عزاداری تاسوعا در دیشموک کهگیلویه‌وبویراحمد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/444524" target="_blank">📅 18:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444523">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c2a7e940f.mp4?token=SeYRlekPqA42reCPcf-WYGTWojvkknAB0p-UrxYMNM-pYl0jauXpjXhVgR9o3QtOxesvzF9ZIgtRoi2xmGrnr80kvWa8nxvmS9I4Std6xQm3fZgl5GahpaZ0DfDs4lzqpHk2aBuHuHZeHy91Fo-Pkw4xAOLPHYs_nk6nLmN9vllAMinhKw-NOY_-DpvJjP2IXa-2rVBOTH7v_U5i7cH8ZsBMNVahu5UfpMxtKiJeBdkDS7sB4Qxcq43myHoRYoUUVw1q1-qcd67PKTHSpnYHsKJB_2JN3F9WCAtF-Y51OwyafGWwZ0BzeovvB75IEGF249fKERAQgRQbr4IIt4UpNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c2a7e940f.mp4?token=SeYRlekPqA42reCPcf-WYGTWojvkknAB0p-UrxYMNM-pYl0jauXpjXhVgR9o3QtOxesvzF9ZIgtRoi2xmGrnr80kvWa8nxvmS9I4Std6xQm3fZgl5GahpaZ0DfDs4lzqpHk2aBuHuHZeHy91Fo-Pkw4xAOLPHYs_nk6nLmN9vllAMinhKw-NOY_-DpvJjP2IXa-2rVBOTH7v_U5i7cH8ZsBMNVahu5UfpMxtKiJeBdkDS7sB4Qxcq43myHoRYoUUVw1q1-qcd67PKTHSpnYHsKJB_2JN3F9WCAtF-Y51OwyafGWwZ0BzeovvB75IEGF249fKERAQgRQbr4IIt4UpNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گرمای لامرد فارس حریف عشق حسینی نشد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/444523" target="_blank">📅 18:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444522">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6b5ad68ce.mp4?token=NkniNbktWNvYLg61Cpzss6_njrdrqRgqq-5nbAGlqjP-hX7NaUKxhQjM9J7zV6V5YDXWOehJqH2DhzXXuLdqMzkRZ5MC3F9x4SNjBNdNlpy8k0jDiO1uSBrZDItuhR_yIREFrhNFoD8rtFI9l-l5oJIb_qyQXReg6zX6iHGEK-arY0WF6c2afbLf5eUEj0qMB929vFiIsT7Jh8Br7yEZaZ8rHRSrnRm76G9nK08-3geWT3YsOtHiFKQdRSua8MRLfiDlpLEtrNNDZ9FMtaq0ckVP-637pUNtXzA7G2NktUWyjjnu1CFJWhIY29EjshHYXekWGFr1dqH92Nu-Ngp8JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6b5ad68ce.mp4?token=NkniNbktWNvYLg61Cpzss6_njrdrqRgqq-5nbAGlqjP-hX7NaUKxhQjM9J7zV6V5YDXWOehJqH2DhzXXuLdqMzkRZ5MC3F9x4SNjBNdNlpy8k0jDiO1uSBrZDItuhR_yIREFrhNFoD8rtFI9l-l5oJIb_qyQXReg6zX6iHGEK-arY0WF6c2afbLf5eUEj0qMB929vFiIsT7Jh8Br7yEZaZ8rHRSrnRm76G9nK08-3geWT3YsOtHiFKQdRSua8MRLfiDlpLEtrNNDZ9FMtaq0ckVP-637pUNtXzA7G2NktUWyjjnu1CFJWhIY29EjshHYXekWGFr1dqH92Nu-Ngp8JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عشق به علمدار کربلا در پل‌سفید مازندران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/444522" target="_blank">📅 18:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444521">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9XrFbzI5K3Cqrw9TyHCyV4E4uyaCLGw0g3MddjYWI0oBCvJFWg-vcHXCtkPzi0qTgMVIOs8f7-mqX7OX3yKsDW3DMIehJWy3_ef106073bw9xPnzeqUGLWMIb4h-KKyVfoYWPn0mM0TYLTKDXPSKr0bcsn9BOvOWDqIszJ8ml8k_rAuiRpfGpUipPVTv-eLv1pTT66vT0FZltOs744U1Hr-tzBhuoSJR2Of_OfrU6bUtBSqN_MIHLGsPlL8ovvlkDQArBd39gh8CFUZnUKUxjRQr8YjCooDKbhTkZ7ZJCjqdiZ1UnZxhuD5WpmUy4AmPlJKQx-9zqQY8EX-LaObnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
رفع کامل اختلال خدمات کارت‌محور بانک صادرات ایران/ تلاش شبانه‌روزی برای بازگشت فوری سایر سامانه‌ها
🔹
بانک صادرات ایران از رفع کامل اختلال خدمات کارت‌محور خود خبر داد و ضمن قدردانی از همراهی مشتریان، هدف از اعمال این محدودیت موقتی را محافظت از امنیت داده‌ها و ارتقای سطح خدمت‌رسانی عنوان کرد.
🔹
به گزارش روابط‌عمومی بانک صادرات ایران، برخی از مهم‌ترین خدمات قابل استفاده مرتبط با کارت‌ها و سایر سامانه‌ها به این شرح است:
◀️
انتقال وجه پایا
◀️
امکان کارت به کارت در کلیه درگاه ها از جمله سپینو و جابه‌جایی وجه از طریق خودپردازها تا سقف ۱۵۰ میلیون تومان در شبکه شتاب در یک روز
◀️
امکان خرید اینترنتی و خرید از طریق دستگاه‌های پوز
◀️
ارسال پیامک تراکنش‌های بانکی
◀️
خرید از درگاه‌های بانکی درون‌برنامه‌ای
◀️
واریز گروهی حقوق مشتریان و یارانه اقشار کم‌درآمد
◀️
رفع مشکل مسدودی حساب‌های وکالتی
◀️
تسویه حساب پذیرندگان پایانه‌های فروشگاهی
◀️
مشاهده فهرست حساب ها و مانده حساب ها در شعبه
◀️
برداشت نقدی در شعب
◀️
انتقال از حساب به کارت و از حساب به حساب در شعبه
🔹
بانک صادرات ایران همزمان با بروز اختلال در شبکه بانکی، برطرف‌کردن محدودیت استفاده از سامانه‌ها را در اولویت اقدامات خود قرار داده است به نحوی که تاکنون عمده خدمات مورد نیاز مشتریان به حالت عادی بازگشته و تلاش شبانه‌روزی برای رفع فوری محدودیت‌های باقی‌مانده، ادامه دارد.
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/444521" target="_blank">📅 18:49 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444520">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8xAIz_tGkEGi2xBBEX-7BmFGCYTZxETOmz-2tj7omGoRnxLmYYRbOWrWgGbPtv9IZFRvfDGSkPFd1uk1xDgOIwVjlDspWvha3ApEhwrGghiKMRlhbW_TjaZb0NuFavFMyCgb7N825FT46AjVIw6ZfpcCxkR59G9RKBixA6GuhX24lrH4MvWxwKA3QExW6YAFfWwd8itiNbUxY44o5ZTr-m2LQYklvsPOXjn3CA-qSpYHenBH5_Z3PUDFgZgab1VSPlaqSJVHLfbMpOmC2VJxIKSnA2VfbXpDgRpWhBDpODgiBy8gvUb2maaNfIBvRkgR8YEnj-5I-6WZtH357qY9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به مسابقه جام جهانی دعوت شدید!
جام دی همزمان با جام جهانی
با جوایز جذاب و متنوع
⏰
هر شب از طریق شبکه ورزش و
ویژه برنامه ۲۰۲۶، همراه بیمه دی باشید.
پیش‌بینی هر دیدار،
جایزه داره تو دی‌دار
ورود به بازی
daycup.dayins.com
#کانال
اطلاع رسانی شرکت بیمه دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/444520" target="_blank">📅 18:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444519">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/farsna/444519" target="_blank">📅 18:46 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

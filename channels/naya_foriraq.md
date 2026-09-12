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
<img src="https://cdn4.telesco.pe/file/KDIB-OpKxWbzcQ73by63KZ5p0-gH_QO0gOl7ZGP6KyJ0uR_TBdImavC3tN2lYUGtA1XqZZQljv8B3U-AAOSlN1ZtJvI2UXsMIasv737eGp6tlLaWyvDTj5gP5wbkv5qsAdeD9dYIRH3gfIR52qqaz0Uf6mv9Jdo9zwfFVfSIGkcQJBJx3Ss_ivQrEGbEPyaVhzU_pEHwvdKwWKeklafrEAlW1vTUZpX56HKBTRDwxAa7rLTWtoS2geui-QGlos9a242z_0xKvK95e6bChi_CdWgJBmPRYUTWIxdtfo4OnrmkPYZ6OLSzMxvkf2N_svoZ---czDlwOVSC4UKXHp0Kbw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 268K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 09:32:03</div>
<hr>

<div class="tg-post" id="msg-90277">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c984e675ec.mp4?token=hUuR5fYfdyAXBjLBZP0ve8vrxGJoq8CdiAeE4mfjIgkBRPez2R6sgmw0eqb9B1eMhot8vhQlMy810FpjP6PdI08CV5V_aGRi19LYBortlg5U3cWf9nA-egJrAk9nmSHJv9FAPhfoMolEPtiLVyplxa5d8NNBnDnc2l7PuYOrfmLkastYDAcaLchjWrSwKrvqmnPliarVzc_fHofLivqZYmZo2h4bWGyQA9CDGewUhaGvoB1VApXV63i2fnqEFiF5xijWghPz_XrMStN8q_Uf-Dw82l2m3hYamGrCoWQBx8D4PtHp9tecFPeiqZF9WUIkTykbmBcSzXUrwfjmNvTuLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c984e675ec.mp4?token=hUuR5fYfdyAXBjLBZP0ve8vrxGJoq8CdiAeE4mfjIgkBRPez2R6sgmw0eqb9B1eMhot8vhQlMy810FpjP6PdI08CV5V_aGRi19LYBortlg5U3cWf9nA-egJrAk9nmSHJv9FAPhfoMolEPtiLVyplxa5d8NNBnDnc2l7PuYOrfmLkastYDAcaLchjWrSwKrvqmnPliarVzc_fHofLivqZYmZo2h4bWGyQA9CDGewUhaGvoB1VApXV63i2fnqEFiF5xijWghPz_XrMStN8q_Uf-Dw82l2m3hYamGrCoWQBx8D4PtHp9tecFPeiqZF9WUIkTykbmBcSzXUrwfjmNvTuLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
استمرار إستهداف العناصر الإرهابية التي تكمن في إحدى مناطق مدينة سراوان من قبل القوات الأمنية الإيرانية.</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/naya_foriraq/90277" target="_blank">📅 09:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90276">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇷
حاكم مدينة مهران الإيرانية:
معبر مهران مفتوح، والأنشطة المتعلقة بالسفر والجمارك مستمرة فيه، ولا يوجد أي إغلاق أو توقف في عمل المعبر مع العراق.
خلال الـ 24 ساعة الماضية، عبر هذا المنفذ 17 ألف شخص، مما يدل على استمرار عمل قسم السفر في منفذ مهران.
الجمارك في مهران تعمل كالمعتاد، ولا توجد أي مشاكل في عملية تصدير البضائع.</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/naya_foriraq/90276" target="_blank">📅 09:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90275">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7eb9c722a5.mp4?token=LSnOsEVmCvZhgRBoKG73LrXGpTGZfzBloe1OYRVkwM7KbHTFPStQM6tWWIh8yjnZrOBE3YJ8XLa9iYULJkLL0g5iI2JLYMuRTHlCQZMK8KHItk3fK4SkKCqljNg5To_FPBAbaEZLj28HNympj7bzneqX299iwEbE5y57shZXnSl6JKrJXcfKU4Cx1jamlG2XaIaaXPEDQ1sBnNVIsYqh-xzvRO6j9EtpwG34DRXTuD-oMkNxDmiqofBCEuUB2X-n7Yx2CPfvBVJpTSO-VzRhwVUK-Rva4INYCStd2-zAwsKruB1bfZQnUXHeSleeJsA3nW0iTviN48UMfBs5QwI7qoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7eb9c722a5.mp4?token=LSnOsEVmCvZhgRBoKG73LrXGpTGZfzBloe1OYRVkwM7KbHTFPStQM6tWWIh8yjnZrOBE3YJ8XLa9iYULJkLL0g5iI2JLYMuRTHlCQZMK8KHItk3fK4SkKCqljNg5To_FPBAbaEZLj28HNympj7bzneqX299iwEbE5y57shZXnSl6JKrJXcfKU4Cx1jamlG2XaIaaXPEDQ1sBnNVIsYqh-xzvRO6j9EtpwG34DRXTuD-oMkNxDmiqofBCEuUB2X-n7Yx2CPfvBVJpTSO-VzRhwVUK-Rva4INYCStd2-zAwsKruB1bfZQnUXHeSleeJsA3nW0iTviN48UMfBs5QwI7qoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
نائب محافظ خوزستان الإيرانية: وفقًا لإعلان السلطات العراقية، تم إغلاق حدود الشلامچة والشيب في محافظة خوزستان اعتبارًا من صباح اليوم وحتى إشعار آخر، ولا يتم حاليًا أي حركة بضائع أو مسافرين عبر هذه الحدود.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/naya_foriraq/90275" target="_blank">📅 08:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90273">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUNaUG-SjwhZFLafxEHAx_RrYHJW_cGayYRlte0hpF7Yl3ZV1fsJW3kyRBQdQaeLfK9bOugGAn-EPErd7D1ANtQStsc9-H8oErOrt7CVoPLUaJbyxHkEDmlESp0EFh3H0Vn-yNGQMFe_2_ECjSB10saMCFdVC4bGG3zH4LJecj1e3XCWbQa-7GeEx29prrZgNL22uKFFv7hxdHOKsXHrTGOgMD4xE0coSXr2jVBYoGY1pFpk0GepRIWWH-9ctmrumkRUiI00Lk5bITqMDxnmhesxLihvcvkpQ0D4icR_oN-q_9DRjh96b64fClK6emlIb2K3537KP3-l5cIwyY_FxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a79629eb3.mp4?token=QYdZ4apMs-I_K6VqCS-86RNLaMMfOiW08D9J2sRSrjppiPlN15sKlKje3NsaBELZCtQaAnTlMajiSxJRmxyotp9flFO35y2_bGxRv-ky0EnuPYwfv3P5Hal9cSNN1Yli84Yq4M_XsQ20hN5-JFbCmchZnoenz1_D4N0c_2t0mztMV_NqggTjh2gPmxe6tACnczUhiGoihC-HapPSzNUIZHALqzl27sc6CIRWQx9YvlGz0H0Rqu1PSC0UURAiDRpe_Sl9EKJZ7rwk49sfu3pDNN8PCEojTH380WHL3myaMvimSMptVtPZIc8j4WMgyFXXkRgL9CB5Pmvpxru9NS9U9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a79629eb3.mp4?token=QYdZ4apMs-I_K6VqCS-86RNLaMMfOiW08D9J2sRSrjppiPlN15sKlKje3NsaBELZCtQaAnTlMajiSxJRmxyotp9flFO35y2_bGxRv-ky0EnuPYwfv3P5Hal9cSNN1Yli84Yq4M_XsQ20hN5-JFbCmchZnoenz1_D4N0c_2t0mztMV_NqggTjh2gPmxe6tACnczUhiGoihC-HapPSzNUIZHALqzl27sc6CIRWQx9YvlGz0H0Rqu1PSC0UURAiDRpe_Sl9EKJZ7rwk49sfu3pDNN8PCEojTH380WHL3myaMvimSMptVtPZIc8j4WMgyFXXkRgL9CB5Pmvpxru9NS9U9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
منفذ مهران الحدودي مازال مفتوحا أمام الجميع وحركة دخول وخروج المسافرين تسير بشكل طبيعي.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/naya_foriraq/90273" target="_blank">📅 08:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90272">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bfc5f64ec.mp4?token=QQ4TuCXNEcJto7eKet7ahzaumhgXcTr8qh3vVgAwoMlOshUFkXn9dwOLKofhr6RAOI5DUnsJ88rAO807brMBQJLMneLzawW93_WCI4YEeDluc-I2I8Pc44RKn5W60D4rkcZrRvIwKeLPT31aoI__SkGLrGDNLcgX540zW5RqoQ2tt8pdTNxSh9iDCsx7DIOjnDExWtNG6SPd80VAhXdHzufdTM9u1E0arnX1i0EvWJW7WXVHsvP9hbmyXH0XWCCj542bUX3ajkcHRwR3ihdhhvUxlo49St3OKV2vxLxiKE7_YCXqYnYyJ0AbvOvoXbm6Zh_HeWwg1BvGza4rTis5Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bfc5f64ec.mp4?token=QQ4TuCXNEcJto7eKet7ahzaumhgXcTr8qh3vVgAwoMlOshUFkXn9dwOLKofhr6RAOI5DUnsJ88rAO807brMBQJLMneLzawW93_WCI4YEeDluc-I2I8Pc44RKn5W60D4rkcZrRvIwKeLPT31aoI__SkGLrGDNLcgX540zW5RqoQ2tt8pdTNxSh9iDCsx7DIOjnDExWtNG6SPd80VAhXdHzufdTM9u1E0arnX1i0EvWJW7WXVHsvP9hbmyXH0XWCCj542bUX3ajkcHRwR3ihdhhvUxlo49St3OKV2vxLxiKE7_YCXqYnYyJ0AbvOvoXbm6Zh_HeWwg1BvGza4rTis5Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
نائب محافظ بلوشستان: إن المجموعات المعادية لنظام الجمهورية الإسلامية الإيرانية، والتي كانت تسعى إلى زعزعة الأمن العام وتنفيذ أعمال تخريبية وإرهابية، قد تجمعت في منطقة من مدينة سراوان، حيث تمكنت القوات الأمنية، بفضل المعلومات الاستخباراتية والدقة، من مفاجأتهم…</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/naya_foriraq/90272" target="_blank">📅 08:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90271">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇮🇷
نائب محافظ بلوشستان:
إن المجموعات المعادية لنظام الجمهورية الإسلامية الإيرانية، والتي كانت تسعى إلى زعزعة الأمن العام وتنفيذ أعمال تخريبية وإرهابية، قد تجمعت في منطقة من مدينة سراوان، حيث تمكنت القوات الأمنية، بفضل المعلومات الاستخباراتية والدقة، من مفاجأتهم وإلحاق ضربة قوية بهم.</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/naya_foriraq/90271" target="_blank">📅 07:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90270">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇶
مصدر لنايا: توجيه فوري وصل للبصرة الان من القيادة العامة للقوات المسلحة يقضي بغلق منفذ الشلامجة المتآخم لايران بشكل نهائي من الان والى إشعار اخر. الإغلاق يشمل المسافرين والبضائع.</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/naya_foriraq/90270" target="_blank">📅 07:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90267">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa850a0397.mp4?token=iByXmQXpqh5N2E8MrXpJmj2Qm8RNOp7UcqDmA0BxN8tEB0a_el2JULx0jWncatqWisJnwFKdeuC7snxXolPszP71eb0mUs6mFu9Aain_669Ws_UWSJarIxvEZ8x6Y6fO6AgoEm9hXUmGGfwdGqcIU_bZ7Sws6MFefcfNcfCcUIvjLi0o-wfrnHL11qHGNjvducdxss2U8R5Hx2oJujuKXvQTSXJ_tv6wArnTwN4_T_6wIJLm_oAxEJ9lPbNmW0_eIwQdv8sbUyiVlHU8jE1QBl6O7-wb-hyML1vocKHcjMIrsUVzfiDZoK_3OQgf0q80jlxi9wG7P2-Cx64g0ktQKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa850a0397.mp4?token=iByXmQXpqh5N2E8MrXpJmj2Qm8RNOp7UcqDmA0BxN8tEB0a_el2JULx0jWncatqWisJnwFKdeuC7snxXolPszP71eb0mUs6mFu9Aain_669Ws_UWSJarIxvEZ8x6Y6fO6AgoEm9hXUmGGfwdGqcIU_bZ7Sws6MFefcfNcfCcUIvjLi0o-wfrnHL11qHGNjvducdxss2U8R5Hx2oJujuKXvQTSXJ_tv6wArnTwN4_T_6wIJLm_oAxEJ9lPbNmW0_eIwQdv8sbUyiVlHU8jE1QBl6O7-wb-hyML1vocKHcjMIrsUVzfiDZoK_3OQgf0q80jlxi9wG7P2-Cx64g0ktQKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
استمرار الإشتباكات بين الأمن الإيراني ومجاميع إرهابية في سراوان بمحافظة بلوشستان.</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/naya_foriraq/90267" target="_blank">📅 07:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90265">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e64b1fb2b.mp4?token=WVumNFvuzF15zghGdqcWTEfuVGnMMXJGUTfyuWwsA2Dhpw0Fj2hT1u76JbBBhrgyTu8ELgqkOVuVhMGumLppJARt5eQecKfaIw-NoatzRhJv20nbfJtxEW4cxxmwN9vA3iSVLo9McOSMjpCxTnvQ-5kLxEYANmfE-xdFivn4bLBBtoyfnX9A0KanPgZbUraXrvs6yBdWx_-Zs7WVofR2uDSvK1ihMmGy_-DwstqNr-eGpoIOgvWfnA4rnpbG2ZyVbE_e3I7XV5ONsUJz3AcmfAG9aYFINfM0UH9iYNiR9AoJNdXMt6DzO6qX6DsqHdAZ4CWv6Aj6dkjUN6IVaoDToA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e64b1fb2b.mp4?token=WVumNFvuzF15zghGdqcWTEfuVGnMMXJGUTfyuWwsA2Dhpw0Fj2hT1u76JbBBhrgyTu8ELgqkOVuVhMGumLppJARt5eQecKfaIw-NoatzRhJv20nbfJtxEW4cxxmwN9vA3iSVLo9McOSMjpCxTnvQ-5kLxEYANmfE-xdFivn4bLBBtoyfnX9A0KanPgZbUraXrvs6yBdWx_-Zs7WVofR2uDSvK1ihMmGy_-DwstqNr-eGpoIOgvWfnA4rnpbG2ZyVbE_e3I7XV5ONsUJz3AcmfAG9aYFINfM0UH9iYNiR9AoJNdXMt6DzO6qX6DsqHdAZ4CWv6Aj6dkjUN6IVaoDToA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
تعزيزات إضافية للقوات الأمنية الإيرانية تصل إلى مكان الإشتباكات في سراوان جنوب شرق البلاد.</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/naya_foriraq/90265" target="_blank">📅 06:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90264">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f85ebf565a.mp4?token=VnKmmJJQeA8eK_hw0bgYnMaW4uK_q89ZFO3dV8sFXmkRhSUHEOJLDbMgrWi70u2-SkMweUX_QWiyVmD4fzE5IDZDpXVecnVssJnCP_P8GC-pcOaHw1EHKN8O271Xok-FaV_aRAF06LUPZ3HSIIXJs7MzBM1b_UzUkIEqmnSI6qxDGO4q2x-36CHEST1kW3iRMYPopK541QbDv3M3bycxug7YnuITr8_dsUA-pJZnf4pdfNPGMmz9EELP5B4MUQSl-DRb1ZlEuULN8FctpHSv1nUlZt6xROZbtFzfqKT-OemfLaldN-H1l-EoDTMRQJ48V9bcPiBfOY0GHN4CXZANxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f85ebf565a.mp4?token=VnKmmJJQeA8eK_hw0bgYnMaW4uK_q89ZFO3dV8sFXmkRhSUHEOJLDbMgrWi70u2-SkMweUX_QWiyVmD4fzE5IDZDpXVecnVssJnCP_P8GC-pcOaHw1EHKN8O271Xok-FaV_aRAF06LUPZ3HSIIXJs7MzBM1b_UzUkIEqmnSI6qxDGO4q2x-36CHEST1kW3iRMYPopK541QbDv3M3bycxug7YnuITr8_dsUA-pJZnf4pdfNPGMmz9EELP5B4MUQSl-DRb1ZlEuULN8FctpHSv1nUlZt6xROZbtFzfqKT-OemfLaldN-H1l-EoDTMRQJ48V9bcPiBfOY0GHN4CXZANxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
تعزيزات إضافية للقوات الأمنية الإيرانية تصل إلى مكان الإشتباكات في سراوان جنوب شرق البلاد.</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/naya_foriraq/90264" target="_blank">📅 06:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90260">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/839ea30161.mp4?token=jDpj9TL6rsiqxxpbmRU1TUjX0wT-8gJtz27l5KDPQzIJ-z8aiYHMdBO0jm9OdYhJGEaPKHyWXA50ZySxVOOt7EMER-f8TDN6E_2ICQtAoFeBEbTZHDWelRAS5wPg_0yENCacy_AoZYo8XZlGFGtT2mKzHfCkD2iDkqedSyNoE-Q-yfpIGdyC7iXPuOD-u2nhtozkzPWV_w92qgW1cu4tBvK0fMMVGqEFJ37o8DrAlTLmHkQ6tIS6zndcWyht3wM_nJbXfO_B4QhV8SbOObLGGRH--YGNcbXzrMVujXdGqBJPO0u4KbBdVlLbhVDuME5z_lkOxWs44Q-aJu25DGA27A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/839ea30161.mp4?token=jDpj9TL6rsiqxxpbmRU1TUjX0wT-8gJtz27l5KDPQzIJ-z8aiYHMdBO0jm9OdYhJGEaPKHyWXA50ZySxVOOt7EMER-f8TDN6E_2ICQtAoFeBEbTZHDWelRAS5wPg_0yENCacy_AoZYo8XZlGFGtT2mKzHfCkD2iDkqedSyNoE-Q-yfpIGdyC7iXPuOD-u2nhtozkzPWV_w92qgW1cu4tBvK0fMMVGqEFJ37o8DrAlTLmHkQ6tIS6zndcWyht3wM_nJbXfO_B4QhV8SbOObLGGRH--YGNcbXzrMVujXdGqBJPO0u4KbBdVlLbhVDuME5z_lkOxWs44Q-aJu25DGA27A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مشاهد أخرى من الإشتباكات العنيفة التي تدور بين القوات الأمنية ومجاميع إرهابية في مدينة سراوان بمحافظة بلوشستان الإيرانية.</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/naya_foriraq/90260" target="_blank">📅 06:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90257">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bb12d1d5.mp4?token=C4Oyc7zjjbXwiwA9NjkTko8mAxRXwbp14iVXFBYTRQtBCHcyvhg9eklRDjj6mv1g5X5YlJk6uZ7jNAiolsA-sW6VjAGzSNkpCqAKgcVtzwNcOQvWJh4Ol_ACIh9RYvWI--hb3PnwvcwlpWtqYpSlGq3O1PtzdVR3n-M5Wyw4cMM9Gd-7jDG3lPaRY_f_rTI1J82bf2DQbHxdCBpizE7CjMw8vBXmukslYfir3a0xZN4rRBYexqzxYlKdPEhBcAJf5SrqT5KWLw5GKU1wl8cHsdCz64Wzw0mlb7DTFLflAr1szZPVS0RWGi8-RB9HbNkasPZCR85KG11v_96ZjaFfHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bb12d1d5.mp4?token=C4Oyc7zjjbXwiwA9NjkTko8mAxRXwbp14iVXFBYTRQtBCHcyvhg9eklRDjj6mv1g5X5YlJk6uZ7jNAiolsA-sW6VjAGzSNkpCqAKgcVtzwNcOQvWJh4Ol_ACIh9RYvWI--hb3PnwvcwlpWtqYpSlGq3O1PtzdVR3n-M5Wyw4cMM9Gd-7jDG3lPaRY_f_rTI1J82bf2DQbHxdCBpizE7CjMw8vBXmukslYfir3a0xZN4rRBYexqzxYlKdPEhBcAJf5SrqT5KWLw5GKU1wl8cHsdCz64Wzw0mlb7DTFLflAr1szZPVS0RWGi8-RB9HbNkasPZCR85KG11v_96ZjaFfHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
اندلاع اشتباكات مسلحة بين القوات الأمنية الإيرانية وعناصر إرهابية في مدينة سراوان جنوب شرق إيران.</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/naya_foriraq/90257" target="_blank">📅 06:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90256">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇺🇸
مسؤولين أميركيين:
إيران حصلت على صور أقمار صناعية من جهات صينية قبل قصفها قاعدة بالأردن في يوليو، حيث أسفر ذلك عن مقتل 3 جنود أميركيين.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/90256" target="_blank">📅 05:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90255">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇸🇦
انفجارات عنيفة تهز محافظة شرورة جنوبي السعودية.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/90255" target="_blank">📅 04:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90254">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af37c0446.mp4?token=NJoGID6xiqyqtpfa_gYefXn1AJR0EOBgMcx4rrpf3Sn02ekONHSpXBxvkyhsGGdie1KB9P7QFXBYisU9g5_j_C7iyhK9jLpOJ_Z0tGkUQwX_VoC_PY9pkgsUgmgY5G1Gt6aDajVFjwFgzQQhx6xnlmXttLkjMZMu_h3amc2JI5QGeVSih9YYxySnI1r6x1nyVHMJxnLFtcImrRIJT1dKNCXw6kaa-RbkpTVZw9FGdrelxXXV381dK56ErLqs8Trwm6gLbKFbWz6h2QL1Ca68gqngRWpPq1M3Ocz66CPBGQcoT-Fc2llurrf8gL-BGqoxsAgH8a_TkpwNawoJho6elndWQ490Yth29x0ixZMfP2M_AWbMcvq10Mdte3PzE2Nj8Wi8WQAqM1acSGwy8UTb__G7l23JPHn2ARpD6NXWAYRGZFVQuKqgyXD16swf0W-_VsBPhJoKbcZ1JtTmSIWCMMKNWG-VskG7bFqtYryhL_SLyoGv-hsbX-4g_AmCMomTwfRQ14dP1wsr6YuO6ejAIg5476Rp9bsfUPCYD0sM-lWGusUQmwAZMsb9txx0WpO6Sv7rJhMwZMACT2jJQz2PYZsiw1rqlV_4MaNO5XYSyfjw2AXB1jZS3luaPB73OAHb21O7C9VxOApC-NSXo7hVZqIGjnVLA6hIFFaaWzauDYs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af37c0446.mp4?token=NJoGID6xiqyqtpfa_gYefXn1AJR0EOBgMcx4rrpf3Sn02ekONHSpXBxvkyhsGGdie1KB9P7QFXBYisU9g5_j_C7iyhK9jLpOJ_Z0tGkUQwX_VoC_PY9pkgsUgmgY5G1Gt6aDajVFjwFgzQQhx6xnlmXttLkjMZMu_h3amc2JI5QGeVSih9YYxySnI1r6x1nyVHMJxnLFtcImrRIJT1dKNCXw6kaa-RbkpTVZw9FGdrelxXXV381dK56ErLqs8Trwm6gLbKFbWz6h2QL1Ca68gqngRWpPq1M3Ocz66CPBGQcoT-Fc2llurrf8gL-BGqoxsAgH8a_TkpwNawoJho6elndWQ490Yth29x0ixZMfP2M_AWbMcvq10Mdte3PzE2Nj8Wi8WQAqM1acSGwy8UTb__G7l23JPHn2ARpD6NXWAYRGZFVQuKqgyXD16swf0W-_VsBPhJoKbcZ1JtTmSIWCMMKNWG-VskG7bFqtYryhL_SLyoGv-hsbX-4g_AmCMomTwfRQ14dP1wsr6YuO6ejAIg5476Rp9bsfUPCYD0sM-lWGusUQmwAZMsb9txx0WpO6Sv7rJhMwZMACT2jJQz2PYZsiw1rqlV_4MaNO5XYSyfjw2AXB1jZS3luaPB73OAHb21O7C9VxOApC-NSXo7hVZqIGjnVLA6hIFFaaWzauDYs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
مشاهد إضافية من إغلاق منفذ الشيب الحدودي مع الجمهورية الإسلامية الإيرانية من قبل الحكومة العراقية.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/90254" target="_blank">📅 03:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90253">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/367a0b2c6c.mp4?token=cmoHwd01aXzDOEUPDFBeG_c1HMcb8B_ULiyRVqB4UJAWmw8FHZIHDPKzG-W45MuBswl2miTceAEDkLpEcoJdEOKYW3xVxazashEL2x2pnodIZko4OSvBJ5bVhWZc8uGz4KvtLYBp5Nqu8B3DqaMBjmYxjt9XhRedQiWSAyDqKkZ4kBy2HUEIiWZEuFYHpmOO24Tp0OnTMajblMVnl9fNmkChduXXsK-cAMULaEazio2lnlnAwM78pt7kH4lssasHZgt9TegJAVk1Nj-UrR5wNgs4hiJJ5CZaYdAxODq0DeFTdcy8iXVObqumzNaldQ3pUKm5AyVpkBys15OI1DyDpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/367a0b2c6c.mp4?token=cmoHwd01aXzDOEUPDFBeG_c1HMcb8B_ULiyRVqB4UJAWmw8FHZIHDPKzG-W45MuBswl2miTceAEDkLpEcoJdEOKYW3xVxazashEL2x2pnodIZko4OSvBJ5bVhWZc8uGz4KvtLYBp5Nqu8B3DqaMBjmYxjt9XhRedQiWSAyDqKkZ4kBy2HUEIiWZEuFYHpmOO24Tp0OnTMajblMVnl9fNmkChduXXsK-cAMULaEazio2lnlnAwM78pt7kH4lssasHZgt9TegJAVk1Nj-UrR5wNgs4hiJJ5CZaYdAxODq0DeFTdcy8iXVObqumzNaldQ3pUKm5AyVpkBys15OI1DyDpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
عوائل عراقية تقف خلف أبواب منفذ الشيب بعد إغلاقه من قبل الحكومة العراقية.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/90253" target="_blank">📅 03:53 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90252">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91429e7bf4.mp4?token=cf3KOcn42FIF2hRl9_ku5kH8BNeibONR-5dO3eO55dZ6qZu0lrDy1jLg0n9gYcOtlz5zD8WOp1SBZBdx-iKA03SQm6ekc0rsVTPDwjUPliLomdvkD7dgwinUwCfBeDhz31DPJi_Ue1X-EGWtF5Fq4L9uCuhxTvPilLz66a6Lq6eQe6IcaXy87w9MGaRHJp04X3hgljTJcbTObFxU4OLuLhof_1kKMK7gVXOYAeCiZ733WqrT-BgRwXlPWwPHZbkvpJLkEGpXk6EfoQlyOIHb3mhsqtlxPlDtcIC5_NW6nAERICpv7QCBaOyFgu2ulGs2Au8o5MQ8YHXTlHWS9HpB9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91429e7bf4.mp4?token=cf3KOcn42FIF2hRl9_ku5kH8BNeibONR-5dO3eO55dZ6qZu0lrDy1jLg0n9gYcOtlz5zD8WOp1SBZBdx-iKA03SQm6ekc0rsVTPDwjUPliLomdvkD7dgwinUwCfBeDhz31DPJi_Ue1X-EGWtF5Fq4L9uCuhxTvPilLz66a6Lq6eQe6IcaXy87w9MGaRHJp04X3hgljTJcbTObFxU4OLuLhof_1kKMK7gVXOYAeCiZ733WqrT-BgRwXlPWwPHZbkvpJLkEGpXk6EfoQlyOIHb3mhsqtlxPlDtcIC5_NW6nAERICpv7QCBaOyFgu2ulGs2Au8o5MQ8YHXTlHWS9HpB9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مصدر لنايا: توجيه فوري وصل للبصرة الان من القيادة العامة للقوات المسلحة يقضي بغلق منفذ الشلامجة المتآخم لايران بشكل نهائي من الان والى إشعار اخر. الإغلاق يشمل المسافرين والبضائع.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/90252" target="_blank">📅 03:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90251">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q46vqLFRRcjhDFSCttbgp0yiVv8-PwBWvoU3Btdl3cbG3ZlwMz3Z2hfIi80tnkMoDPMLrqOwLsOhKWDzUAT0vURdJfefl4pDT7c4c56uIP8zmfGFrxfik-PmCUJ6lgaVip_xzOmaTZMEnH7i1YX5IS9DJw7MTM_v9V_baRD0lTkV9mYAzxTmkUcTloEOTZFJU06tpG5i1zQDhaEzGpP--bV09MKSXKsuobuENO3u02WLlrh-ZZmrBPMiuZ1MPISv3hGXSbsZ7NDrZqgcNVugy8LOtjYcecG1gYsafXepqAq-pBYBFae39aAbT5EZ499ezWa60JdrvUQ6HSDW0Bt-4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
مصدر أمني: إغلاق المنافذ الحدودية مع إيران شمل الشلامجة في البصرة والشيب في ميسان بشكل تام وقطعي، ومنع دخول وخروج الأفراد والبضائع من الليلة وحتى إشعار آخر، فيما لا يزال منفذا زرباطية في واسط والمنذرية في ديالى يعملان بشكل طبيعي.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/90251" target="_blank">📅 03:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90250">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇶
مصدر لنايا: توجيه فوري وصل للبصرة الان من القيادة العامة للقوات المسلحة يقضي بغلق منفذ الشلامجة المتآخم لايران بشكل نهائي من الان والى إشعار اخر. الإغلاق يشمل المسافرين والبضائع.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/90250" target="_blank">📅 03:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90249">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">إنفجارات تهز الطائف</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/90249" target="_blank">📅 02:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90248">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/90248" target="_blank">📅 02:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90247">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">إنفجارات تهز الطائف</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/90247" target="_blank">📅 02:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90246">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">انفجارات تهز خميس مشيط في السعودية</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/90246" target="_blank">📅 02:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90245">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">انفجارات تهز خميس مشيط في السعودية</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/90245" target="_blank">📅 02:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90244">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇶
مصدر لنايا:
توجيه فوري وصل للبصرة الان من القيادة العامة للقوات المسلحة يقضي بغلق منفذ الشلامجة المتآخم لايران بشكل نهائي من الان والى إشعار اخر. الإغلاق يشمل المسافرين والبضائع.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/90244" target="_blank">📅 02:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90243">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g7o9rptkLYC_aK2gnmBwb8FTptK9itc4YUX_vXR26H5-fCXMv6mvIvTGwpG-ACNxXCfWDvpXJsvRi98Oyjg01fsfieO7v5lcuS4Fb58e72s3l2-LXERcrOqDLcm7Dx61Z54Tem3ez-iHUfMGXRxf7wDsxaOaybKItl-7MgG3Nn6ExpfalgsBDGruhIN3Ny6ajAAo2M4b-VUtZQiJwmgFF7fqWjz7gPxs0H3hZr7vUgKcZoIwmm1kSApZG3_v4kO18QCMJ4NsAdtzTHycpVJYZCtAPQMX2WhT_Z2XrOCvLwKk1bNx3FBbI7JN12hyyMNXfCOTc3hNLPsII6YJYWLh8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇸🇦
حريق كبير في مدينة ابها بالسعودية بعد استهداف عنيف من قبل القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/90243" target="_blank">📅 02:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90242">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇾🇪
القوات اليمنية تسيطر على جبل جرداد الإستراتيجي في محافظة تعز.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/90242" target="_blank">📅 01:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90241">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cce0bc6b13.mp4?token=LbYJ4AEI-JITxhnQcxZ8FWtpaPYyUR3lVYZ-Jf9gUESychxW89k6t5wuLJ433mTk4ZHa_y6T_7Wki33Rc0CqJwpbXcXQVY7lrT6SKtyWCl6NOMD-LAqmg9UY8L-SfCKoMPVIFH5yseLecB9hy4nbCpG6BY6ClRAuxpXtQcSdJY5V2l2YP_lZnFjIfpzT7kN-BrsBLYK3heVLGQ7NUuXHYfHGRZ1r4TbdYwEdlAf0a9RWIxfWiEZS1gbh7_zh96pOd1nuAkTzzCyAOIyPsA0MR93uxzhYPBPDqCadUSRpL2BajvFeOGBkV0yjx4P4Qb46MscVbWhPm3Zp-LtMVGF5YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cce0bc6b13.mp4?token=LbYJ4AEI-JITxhnQcxZ8FWtpaPYyUR3lVYZ-Jf9gUESychxW89k6t5wuLJ433mTk4ZHa_y6T_7Wki33Rc0CqJwpbXcXQVY7lrT6SKtyWCl6NOMD-LAqmg9UY8L-SfCKoMPVIFH5yseLecB9hy4nbCpG6BY6ClRAuxpXtQcSdJY5V2l2YP_lZnFjIfpzT7kN-BrsBLYK3heVLGQ7NUuXHYfHGRZ1r4TbdYwEdlAf0a9RWIxfWiEZS1gbh7_zh96pOd1nuAkTzzCyAOIyPsA0MR93uxzhYPBPDqCadUSRpL2BajvFeOGBkV0yjx4P4Qb46MscVbWhPm3Zp-LtMVGF5YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
سماع دوي انفجار مجهول في العاصمة السورية دمشق.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/90241" target="_blank">📅 01:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90240">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e27ef9604.mp4?token=cYkDOX6RJEyBsNHi8bMr_SNXHjKtOL2Vv-ZZOy5hMlARA1p8OTmTxshkf3WxT8T5qyF9uEd3vfHxR51M8odyJuJUhVxMwnu5qOjv6ogwhk1ecAW6_H_i9WEaz2h2b4qCrXp29xN3Zneab0SE6Y2lt44nXcKmt3LG2NWQlqtMqCUBH3U8QEknOZAcA0aEUiTL8Alr3zpvxvA2jI-hny5Ghp6hspvQQOK5hIb26EgAXqPuU5h_WcivxWL_iedZeOmj6Mc3ZfECJhbqc3rtw-sDUu-MOTiRgtfssKu8H__bAnlRFmggM5TApFhcEP_Bqd6mQ-O63vHC-xC6Pbp5lLKYlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e27ef9604.mp4?token=cYkDOX6RJEyBsNHi8bMr_SNXHjKtOL2Vv-ZZOy5hMlARA1p8OTmTxshkf3WxT8T5qyF9uEd3vfHxR51M8odyJuJUhVxMwnu5qOjv6ogwhk1ecAW6_H_i9WEaz2h2b4qCrXp29xN3Zneab0SE6Y2lt44nXcKmt3LG2NWQlqtMqCUBH3U8QEknOZAcA0aEUiTL8Alr3zpvxvA2jI-hny5Ghp6hspvQQOK5hIb26EgAXqPuU5h_WcivxWL_iedZeOmj6Mc3ZfECJhbqc3rtw-sDUu-MOTiRgtfssKu8H__bAnlRFmggM5TApFhcEP_Bqd6mQ-O63vHC-xC6Pbp5lLKYlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
سماع دوي انفجار مجهول في العاصمة السورية دمشق.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/90240" target="_blank">📅 01:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90239">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‏اول موقف رسمي عراقي   تدين الحكومة العراقية الهجمات التي استهدفت المملكة العربية السعودية الشقيقة، وتؤكد رفضها لأي اعتداء يمس أمن المملكة واستقرارها، أو يسيء إلى العلاقات الأخوية الراسخة بين البلدين.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/90239" target="_blank">📅 01:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90238">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dq4vl4hMitQsAp0ybfbLEdBjPLiqKl67SKvEsLNUN8T9lCW-8bzEJCrxeZkl0bBLweSQpnOGm-ZI5tNn1INBz9wOCeMnHh6w7aYg1dxynalTTqmd3URudBkMF_RQwGralC6b8JfYEOtwovd3I82N5MiWpxjS7J4u6tlWyTrdsj7shvaUyyllKskG_qy_5MINhDyyvwiJxNh5LohrBG1qp0v_gf4Z2yWkjqFARS9cy0vTvOD4JV8I__FbWxnZrr38i0jyl3ao25uu4I1nD2_KNOps7t8ilQcczO5XPmEl_nZGrbdj5GhsstvkLFCV8oUyC3tWe_W92W3ELKe57x7XHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇸🇦
حريق كبير في مدينة ابها بالسعودية بعد استهداف عنيف من قبل القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/90238" target="_blank">📅 01:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90237">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">الخارجية الأمريكية:
نتواصل بشكل منتظم مع حلفائنا وشركائنا في المنطقة بشأن التطورات اليمن.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/90237" target="_blank">📅 01:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90236">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/90236" target="_blank">📅 00:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90235">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/90235" target="_blank">📅 00:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90234">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/90234" target="_blank">📅 00:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90233">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmSH1OzhGbPvZcju5Q_ZP_y6s7hZLQoSHNdl9PASsNXwyzNTrSDBzU7Xs924YrS67qQ1QO7W-zHkykS04n7fnvyMt_O9n__bsIPdy4Ni2zDEE2OvYA8j8cIBJHZUqnFlSBxXiP78SR3bcQWXFUwbfo2l1SvSpXv4plShcEPh8Af0cXXp9PVp5zUpJHrXY29ctF2hOlavfvGZw4sc16sVBkvVglqnjEOKhFUtTiX6nLRnXsWhhrn00laAFFZUEIUhxvvUDzm5ceFRhBbONgLtPmT280LYe5tOBOuUtoLosmfwbGhmSu4nGmnZUYwz14rguhILED7JXQz6-KkXAgSi7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🇮🇶
🇮🇷
🇺🇸
🇸🇦
بريت اركسون : إن تعرض خط أنابيب الشرق والغرب لهجوم من قبل الميليشيات العراقية يجب أن يعطي الجميع استنتاجاً واضحاً للغاية: إذا استطاعوا ضرب جوهرة التاج السعودي... فلا شك على الإطلاق في أن إيران قادرة على ضرب أي بنية تحتية تريدها في أي لحظة.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/90233" target="_blank">📅 00:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90232">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eb3a9e2c1.mp4?token=gkLgL-secOM0Z_2iRjsE1az7v1a9-8ppd1PHtrMtUHe6bPUwfuNEqL64EAGAIPpLx_MU8dQ74IJ6rsjmW4nzgX64616wiVP6LY2u0w_fzvkGtymfOpWG8kP1dN5js-JQNXptsLS5Jj5ByvLC4z5gxG6tlP9XgDTGFsE4izM0RttccKp5AUyKIoURwyBd4QA_jOhUlC5Ebb-tTZikgFmIOcDmopVfR3KMdBpdrvrIftONyAx8AVXU-QAkNtgFy_6rIGgZnh2UfiEnbN_wSKsEwB2Ekr_FjnSoJdBFFfXFkGab-FGOWWQkqPtixMdotAhBCWwCQIkylnQ25higeUS19A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eb3a9e2c1.mp4?token=gkLgL-secOM0Z_2iRjsE1az7v1a9-8ppd1PHtrMtUHe6bPUwfuNEqL64EAGAIPpLx_MU8dQ74IJ6rsjmW4nzgX64616wiVP6LY2u0w_fzvkGtymfOpWG8kP1dN5js-JQNXptsLS5Jj5ByvLC4z5gxG6tlP9XgDTGFsE4izM0RttccKp5AUyKIoURwyBd4QA_jOhUlC5Ebb-tTZikgFmIOcDmopVfR3KMdBpdrvrIftONyAx8AVXU-QAkNtgFy_6rIGgZnh2UfiEnbN_wSKsEwB2Ekr_FjnSoJdBFFfXFkGab-FGOWWQkqPtixMdotAhBCWwCQIkylnQ25higeUS19A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
وزير الحرب الاميركي: نحن ما زلنا نرسل الإرهابيين إلى مكانهم المناسب - إلى الجحيم - والسفن النفطية إلى قاع المحيط، حيث يجب أن تكون.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/90232" target="_blank">📅 00:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90231">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/524aca328c.mp4?token=na7QMeEZ9e-grew-d8T0IIte4_x4sW8XZB6CssKBFY6FMiypDOq43qt5iuoYiIDdIaDwKo2k1HZYS40vCdNcb-p0sio81v3l21saTjtUIDe_tNzW1mdEWQ4PLtG7oS0nU0Y0DVvi0Atl77pMzrf6yrsJo_P7UtwVQY29b9abrz3KFZoeQEhDWKdTHiNDYnZMRWnpvMh4W-c7cjukxv1Y3CdPSXPTCqjpZOPFEL7l9f4CkhM1D1RUl9btiC8H174PXHdvadWCZwNI8fpr1lIddcx3GPtn7lHdVTIzIOYJZjkQLtr2WB94hG5Eof61KtrsUudlDGyoY_-OR59K0PfpQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/524aca328c.mp4?token=na7QMeEZ9e-grew-d8T0IIte4_x4sW8XZB6CssKBFY6FMiypDOq43qt5iuoYiIDdIaDwKo2k1HZYS40vCdNcb-p0sio81v3l21saTjtUIDe_tNzW1mdEWQ4PLtG7oS0nU0Y0DVvi0Atl77pMzrf6yrsJo_P7UtwVQY29b9abrz3KFZoeQEhDWKdTHiNDYnZMRWnpvMh4W-c7cjukxv1Y3CdPSXPTCqjpZOPFEL7l9f4CkhM1D1RUl9btiC8H174PXHdvadWCZwNI8fpr1lIddcx3GPtn7lHdVTIzIOYJZjkQLtr2WB94hG5Eof61KtrsUudlDGyoY_-OR59K0PfpQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
وزير الحرب الاميركي:
نحن ما زلنا نرسل الإرهابيين إلى مكانهم المناسب - إلى الجحيم - والسفن النفطية إلى قاع المحيط، حيث يجب أن تكون.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/90231" target="_blank">📅 00:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90229">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-text">🏴
قطعاً بینی سعودی‌ها به خاک مالیده خواهد شد.
@Naya_Press</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/90229" target="_blank">📅 00:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90228">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6MvwFrT9CMcVD91ZFjw_Njrvm4KxUHjVB_qq8fKaLDyXq-j3HLePTl0diIPRnzxH2LfHJEW5GLDqLfO7kGgSAkHMmF4nnYsjBDLIq2PZj47_bpP3mJeTOqD52OlKhbmaVUShLMvES1PtOb4IL2Lypb2V1YJpVhAym31Xt4IHkBd5GbkjcTDYqf7PlV0uY9TXkMgreU47wBfmWX4fjQMr328rLbuxLB7c_bGSHbiRZOPOnmkXDhYEebKcegvqplEkl3JDZDytgsOahayz_TAqVoZ2dMbq-4y49NlUa9Ir3cVXNco3ic-SesJL232YG7XFi0r6DGyGnPPY4jvewy9gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇸🇦
السعودية رسميا تدعي تعرضها لهجوم بطائرات مسيرة اطلقت من العراق.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/90228" target="_blank">📅 00:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90227">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇰🇵
أطلقت جمهورية كوريا الشعبية صاروخًا باليستيًا لجهة مجهولة.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/90227" target="_blank">📅 00:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90226">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/107c7847b1.mp4?token=dTiJU4oHrKcQGeteglrlj-LSGW206dzBaJCVNbS3ImLhfpax_BeZE_3vQUaAGRRaMi_FjPxSxT_T8C6iM3QDfa2jOB41yM0Y88DrVaj_8RHqudG2a60qhFxo0WKRkmfTEnLazH-mN7Hf8nAAOtoatJ28HntV1UeEguSHct3y_9znO222TGVqQmwGIfRLKOZYaX5CcGULSeiIuLOWl6J7O3nyWp0qOtB2ZQ421pHjY0USfSfDl0I6_73aCe9YSW_AcCj4aX1r1zCmaoNf755g9yOI7deECD96Q9_RXf4-80xxlelTl6yWTyOlQXUyM8QfvmwbxJE0ywSnN2NKJqd-UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/107c7847b1.mp4?token=dTiJU4oHrKcQGeteglrlj-LSGW206dzBaJCVNbS3ImLhfpax_BeZE_3vQUaAGRRaMi_FjPxSxT_T8C6iM3QDfa2jOB41yM0Y88DrVaj_8RHqudG2a60qhFxo0WKRkmfTEnLazH-mN7Hf8nAAOtoatJ28HntV1UeEguSHct3y_9znO222TGVqQmwGIfRLKOZYaX5CcGULSeiIuLOWl6J7O3nyWp0qOtB2ZQ421pHjY0USfSfDl0I6_73aCe9YSW_AcCj4aX1r1zCmaoNf755g9yOI7deECD96Q9_RXf4-80xxlelTl6yWTyOlQXUyM8QfvmwbxJE0ywSnN2NKJqd-UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
هروب عناصر المليشيات الموالية للسعودية من ثكناتهم العسكرية وترك خلفهم كبسة بالدجاج من دون ان يأكلوها
😫</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/90226" target="_blank">📅 00:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90225">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">الاعلام الاجنبي: اصيبت شبكة خطوط أنابيب النفط السعودية بوابل من المقذوفات، مما أدى إلى اندلاع حرائق، مسؤول يقول إن الهجوم من طائرات مسيرة انطلقت من العراق.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/90225" target="_blank">📅 23:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90224">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jip1hB-3r3jyC1vEwTcUP6o0F4CPmABha6vk1sYppMzPcNAMe3PCgpVporpu4KnQCnsEehNOwojx09aCEwrfOZWUHEzH0jZLRmoYZOWbOVhikHy6nN1XgOb97Cu4PIJ9tcq3JKKFSovNTsf4SBhJOGRHL6Hl0vAFXE15BOVteHfPtWmCONiV-MynbbuSfv12PAfnLtlA2a_ucJoM-ztRbPwUYKUXYMyRwj7yQm-WVPTtpOAGl3l4uVWOCcEalL8DexFKK_UJ5KC7xLuFXdNAw6m-kQeJx2lG2ND33s0kngQPi7LLGc0OJFe4L7C7uSvmVmdWPU9qO2Rr-K3b1neR4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إن الهجوم من طائرات مسيرة انطلقت من العراق.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/90224" target="_blank">📅 23:39 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90223">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇷🇺
بوتين
: أوروبا تدفع دولها نحو الحرب مع روسيا. روسيا لا تشكل تهديدًا، وليس لديها أي نية لتهديد الدول الأوروبية.تم حل كل شيء بناءً على نتائج الحرب العالمية الثانية.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/90223" target="_blank">📅 23:38 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90220">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇾🇪
سماع دوي انفجار قوي في تعز</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/90220" target="_blank">📅 23:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90219">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-text">🔻
It seems that the US and its allies in the region are very upset about showing the losses through photos and videos. Therefore, our channel’s name will no longer appear when searched for on Telegram.
🔻
Please share our channel link as widely as possible.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/90219" target="_blank">📅 22:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90218">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اطلاق عدة صواريخ من سيريك</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/90218" target="_blank">📅 22:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90217">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇾🇪
🇸🇦
حرائق لا تتوقف في خط انابيب السعودية بعد الاستهدافات اليمنية الاخيرة.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/90217" target="_blank">📅 21:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90216">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇮🇱
محاولة دهس لمجموعة من جنود الاسرائيليين في فلسطين المحتلة.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/90216" target="_blank">📅 21:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90215">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
تعرضت حاملة الطائرات جورج واشنطن، التي تحمل حوالي 5000 بحار ، لهجوم صاروخي باليستي إيراني في نهاية الأسبوع الماضي.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/90215" target="_blank">📅 21:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90214">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqZeLCdaCdo3Ec4IvHs8KNM1lzSNPkoSu2ORUnrZj9DWh6ZFQfWKqFrOhGDkpiQOiVfFoMxkHcCNXiNX1TDsQWSdZ4HnqIVc1E2aaAZ2xZhsQYfk6hyLcCd0nnk4S-pTy-FxyH4dmsuKRhFxaP00CL_bCcit3EOm6zHc-CT1NueHrHNTuuyDh0HErWCZKvlQOSPx1N7fqTau3BZ2wOKqp4DTyvaPWUve8IHL0RD3HbPM8qeeL-OAOBNfSOxjcQK8BnHoCTgQ6wbyF3oOMLq0e58QgRxovzGceLV0ZvsMKCSgtFLDbqeqIIJIyDkViIkmjy_NkXuOaMBLeSnSJXaCTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسريب ضخم يطال وزارة التعليم السعودية
🇸🇦
أحد المخترقين يعرض على منتدى إلكتروني قاعدة بيانات تضم نحو 600 ألف سجل، مقابل 300 دولار فقط.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/90214" target="_blank">📅 21:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90213">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POSqMi3y-lQfnm43y0l_7FCl3vTDLn16oelEJkV0edtlDXl8c8_joZI4-InWKvrrlfQ2jC_sWeaMDkFP5AWp3_ksVeDTNDS7VmS22_ZKG1fh5pgBocmh1TguY_l3x3KhtKDpge5zRahSAhs8Xh6Ppx58GGp9tCKsNZiAz2tJ4kbFdAB8fYK_2Vbpds7ceHMsFcE7Cfy-BqU48H6qju4FC1GBQj8zsJ92jCPWWQo3hVKwrUMWWhfFeZ2bYs4K-d8IdwJDeA2SnVBdQzG_xJrDlvr3EifNJlfNkZW9TBFKnFQoeXhEBDWFF_J2I-vTdPZv8Wb1v6hq2TEIqBiT10Jslw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الشيخ همام حمودي في ندوة حوارية بمعرض الكتاب الدولي: الحكم في العراق ليس شيعي والنظام باقٍ، باقٍ، باقٍ
- نجحنا بشهادة دول العالم بإقامة نظام ديمقراطي تعددي، فيه حريات وتداول سلمي للسلطة، وحضور شعبي، لكننا اخفقنا في بناء دولة مؤسسات.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/90213" target="_blank">📅 21:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90212">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">وَلَا تَهِنُوا وَلَا تَحْزَنُوا وَأَنتُمُ الْأَعْلَوْنَ إِن كُنتُم مُّؤْمِنِينَ
سستى مكنيد و اندوهگين مباشيد، زيرا اگر ايمان آورده باشيد شما برترى خواهيد جست
So do not weaken and do not grieve, and you will be superior if you are [true] believers.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/90212" target="_blank">📅 21:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90211">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇾🇪
الشعب اليمني يجتمع في ميدان السبعين،
شكرًا لله على الانتصارات التي حققها الجيش اليمني ضد المليشيات الموالية للسعودية.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/90211" target="_blank">📅 21:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90210">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/90210" target="_blank">📅 21:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90209">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇮🇶
رئاسة الوزراء العراقية:
فصائل مقاومة سنجار ستباشر تسليم سلاحها إلى الدولة.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/90209" target="_blank">📅 21:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90208">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇺🇸
رويترز
:
يدرس البيت الأبيض استخدام "قانون الإنتاج الدفاعي" لتوسيع قدرات تكرير النفط في الولايات المتحدة، وذلك في ظل ارتفاع أسعار الوقود المدفوع بالتوترات المتعلقة بإيران.
ويناقش المسؤولون تقديم دعم فيدرالي لتوسيع أو تحسين المصافي القائمة بدلاً من إنشاء مصافٍ جديدة، وهي عملية قد تستغرق سنوات وتتطلب تكاليف أعلى بكثير.
يُذكر أن مصافي التكرير الأمريكية تعمل حالياً عند مستويات تقارب طاقتها القصوى، حيث تبلغ نسبة التشغيل 98%.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/90208" target="_blank">📅 21:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90207">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGELyE-wI89b7cE9TxxEv1Hr0cNdWMJ44h-H4PhvvHUpnJfjiWhAU9ktmAWF1ZZ-Fm6UhNduYzSTAXPSa-u0y34VErwcHUP_7U8tfKIg76gqCtx7jS6cVik2MflfOAwQIdeYzrsxFKVX21Lpd9WjY4dMK4HxKVen0hNYj_8J-zNs8ntm7qp3BnAOKHQlb6uuL65U5l3hTmVEXYTsaGbftgBcMttZ7YMaZ_WFYQL7vuK7M8ekrQGq2F26KQuvNCh05jKYB4ufqawxPqnGSmaX7gcbIVocavp_5f3XmSTmqv7BwhiJucs71zPMoMcA2Tra93wulSItZtKa0RPaJtcgMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🇮🇷
🇺🇸
ول ستريت جورنال : استخدم إيران نماذج الذكاء الاصطناعي التي طورتها الولايات المتحدة لمحاولة استهداف سفن البحرية الأمريكية في الشرق الأوسط، وفقًا لتقرير أنثروبيك الذي يحذر من مخاطر الأمن القومي الناشئة.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/90207" target="_blank">📅 20:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90206">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اطلاق عدة صواريخ من سيريك</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/90206" target="_blank">📅 20:41 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90205">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmUgL6TIVFlWPAZWbiBuPh0oCiTIg61OilUg0r9J3KHBpw7l6EY8kg3QcyYmgQT04ZrtxqOAZsCwQm3MUR0ChGku9KfycsNBhJhWG1NFhnBvwP0Nbr4GNNVc-VRYMRkDBbDQLkpM4C7gVzyt2rqYM_qzm2hKIBdPBAdh-S0sUcCncFzQGvKOmZKjlkMcd5p3JutfZn7YpXAXf38OCJq25Ew0i8YL3_CQWmPYRxIm9ii4Y4CQziKQ3l0gwU2aaGnWHTA8wLghFs3Ti_rOIuSDKrSrUrR-4opt42MB1K68c7t5R9Am_FEH7AEiMcvLeUagZsrYr9MOwoGZ2q0axsoL-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية:
عملية "والله أشدُّ بأساً وأشدُّ تنكيلاً" في الساحل الغربي.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/90205" target="_blank">📅 20:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90204">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jglGmyIB_LVebKSqi13lIaCACSLUnOviuk-nw5TTUAWEYIoYLqZZmlhxeVI-gquf16OByORnagk-EKSIP19Ej0R2V1h4oyg8CKZkI5_blVXpJZGBju_BtoPb4siXyuafqZbJrRv1RxRtuR8qXPXngHPMVmiOhcQjxLb0UI6DRqwcRG1oPTEX4PWwq_kRnbc-faC5mJvoJlzYBKFhionIu2vGjCGmRqwPkc7XDafDzpOe5-07McxDyOSx3jIsU938dFUcWnwc4pR3U2DWtwdj0R80Xhnoju4qdnv1ultfcErK7r_4l2YOunEyOcHX8CvCPnvdF2aNUkq_Alxm0yvWhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الاعلام الاجنبي: اصيبت شبكة خطوط أنابيب النفط السعودية بوابل من المقذوفات، مما أدى إلى اندلاع حرائق، مسؤول يقول إن الهجوم من طائرات مسيرة انطلقت من العراق.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/90204" target="_blank">📅 20:24 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90203">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b47bceab31.mp4?token=F9zcYPlH94f9F3mIHQSnkjZI82yP1vigG1Vy4qcrGZAgDERkM0bSm9Z2ZXkpqCVKaJnoAFwNpwKfdOUG6K-5K2KUvt9ybPpBLmtzFdTycbdXrQ42sU7kR4FMa4SnjO9gRul5N-kjSIZLW80XoYY-ryqw_LKhXXGagLmoXOtDCVQIdSAujQ_M7wT4-n-5U4VAmtCeTmKAHDY1dHrYKAcYkjg1rO-hReiQrP1iY-y8Vp-kJ-8FpAanLJu_eOrx2mPCLaQW6RRTips6Iw4Wk1jB0rEsXZ4okv-9FLgS6YkezaUkVXWJkGNWDYiPXzVAljhnfF84lQEfQRPL9YxuYEeuxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b47bceab31.mp4?token=F9zcYPlH94f9F3mIHQSnkjZI82yP1vigG1Vy4qcrGZAgDERkM0bSm9Z2ZXkpqCVKaJnoAFwNpwKfdOUG6K-5K2KUvt9ybPpBLmtzFdTycbdXrQ42sU7kR4FMa4SnjO9gRul5N-kjSIZLW80XoYY-ryqw_LKhXXGagLmoXOtDCVQIdSAujQ_M7wT4-n-5U4VAmtCeTmKAHDY1dHrYKAcYkjg1rO-hReiQrP1iY-y8Vp-kJ-8FpAanLJu_eOrx2mPCLaQW6RRTips6Iw4Wk1jB0rEsXZ4okv-9FLgS6YkezaUkVXWJkGNWDYiPXzVAljhnfF84lQEfQRPL9YxuYEeuxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية تغتنم اعداد كبيرة من العتاد العسكري في مدينة المخا</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/90203" target="_blank">📅 20:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90202">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇾🇪
🇸🇦
بعد القصف اليمني الاخير امتد الدخان لاكثر من 100k عبر صحراء السعودية.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/90202" target="_blank">📅 20:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90201">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇾🇪
🇸🇦
العدو السعودي يشن غارات على مدينة ذو باب.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/90201" target="_blank">📅 20:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90200">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو الاء الولائي- القناة الرسمية</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQRGRshgQ6uPMawfTHLC2uZhAombLTSxsrdlaUUCQE217LEoo_TmmgSBUIrgI04blnCKnxuFfR9MFmjXov81BSjyeyv8kDeTouzux59WPSPUncihra61KbOuvjGcjRG53HrYfrDQqvqQUvKiyRCnSkmj_o6Tlfo8Z37mejuuPQbfyNs4IX4FlDg5QmSbZGKi2PcWlRr9NgyVzcYeC7ZMX3FiLIE-zRMxcl8TRMk0Wb3QnRMzh9w7OUK-r7UCWhO0nJnbun6nnh9bv-rgmlw1EyYGkl2vRIHUANC79j0ULagm1sgwVEMy4Yz7MHS5b1OCyNvQ4N5zJtV5iUTA-JmYkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نبارك لإخوتنا في أنصار الله انتصاراتهم المؤزرة، واستعادتهم مدن الساحل الغربي بالكامل، بعد هروب الميليشيات المدعومة سعوديًا وانهيار مواقعها.
ونؤكد دعمنا لحق الشعب اليمني في استعادة سيادته وبسط سلطته على كامل أراضيه، تحت قيادة زعيم اليمن ووجهه المشرق السيد عبد الملك بدر الدين الحوثي (دام عزه).
اليمن الذي أرادوا له أن يكون خنجرًا آخر في خاصرة الأمة، يستعيد اليوم عزه وكرامته، ويمضي نحو يمنٍ حرٍّ عزيز، قراره بيد أبنائه، وسيادته مصانة، وإرادته مستقلة عن كل وصاية أو إملاء خارجي.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/90200" target="_blank">📅 19:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90199">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_DZwp22Qh4wRkEl-oe2n0nVj-uyXwujpm6Ju5hvmObNLvmK_LsQeroL5FNU8VO9bRlS3snu1B13JFNpxUkKZ4FmXyTDYlUwiQAP7Hpyq7B03tKqUKLL0yPvAABDxRRAIeUPFlJUvEX01TAG6O-czn_wRiEBUVh-Fw8ZoaRQiqj-CQhtuxM9xkcYbVBMKszpkz4yypU-vKU6giQTFC-IwFm_7pVwbgd9Z-qfSA7gIwUywOFrXpKAqA1_8GAg84sxp5BL_WozlK5UhzZmmh-_N6WVGEfIDUgZwakwRPgDQqUfLpeDNXRGp8_oVue7UNQ-IbJmkdZeGq263YTjwoJXjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
هزة ارضية في محافظة اربيل شمالي العراق تبلغ قوتها 3.1 درجة.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/90199" target="_blank">📅 19:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90198">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">القوات المسلحة اليمنية تستمع لكلمة العميد يحيى سريع من سواحل المخا المحررة</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/90198" target="_blank">📅 18:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90197">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">القوات المسلحة اليمنية تستمع لكلمة العميد يحيى سريع من سواحل المخا المحررة</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/90197" target="_blank">📅 18:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90196">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e367315034.mp4?token=bN7MXIRE8ihHFmwGoER3kTPPeivnp507LfSGn7jh41mTQc9scMDEwhR6ohRzfltCaLjf2CmwyYcu3Dy8HiMFlubIUs4Uz34eXxdxMCnKbpXhPn9UVRCYR_0A8bpgfly2gJ50Fhp_lzE35zPIdOgGUsseTw_F2pQK7bPqVgLMx84_VikV4tgrpKDSB3Vhh8aUDViZtI2GH5eOxA2Jg4uvNwhQ6Ye007mAljMj2soAwYL72Z9pSjxZQ3-TtNZUUXS_TnWkC4kePhi6u2aBFsnbOG1e4zKgeo3GKltZGG3hsgHCpZCqyX5Joq43ywPTXT6qBl6LHkHGsOCmKZEtr0HxYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e367315034.mp4?token=bN7MXIRE8ihHFmwGoER3kTPPeivnp507LfSGn7jh41mTQc9scMDEwhR6ohRzfltCaLjf2CmwyYcu3Dy8HiMFlubIUs4Uz34eXxdxMCnKbpXhPn9UVRCYR_0A8bpgfly2gJ50Fhp_lzE35zPIdOgGUsseTw_F2pQK7bPqVgLMx84_VikV4tgrpKDSB3Vhh8aUDViZtI2GH5eOxA2Jg4uvNwhQ6Ye007mAljMj2soAwYL72Z9pSjxZQ3-TtNZUUXS_TnWkC4kePhi6u2aBFsnbOG1e4zKgeo3GKltZGG3hsgHCpZCqyX5Joq43ywPTXT6qBl6LHkHGsOCmKZEtr0HxYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدرعات المرتزقة بيد القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/90196" target="_blank">📅 17:57 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90195">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🌟
🇺🇸
ترامب:
الجمهورية الإسلامية الإيرانية الراعي الأول للإرهاب في العالم.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/90195" target="_blank">📅 17:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90194">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/694eec3d51.mp4?token=arMvm99TJf9M5scjlCqw_97QmHK4UcpscF1lI2OMKcbptvKWt7G0xwrUOlhUZ25fIhnKtMvHYYBYp-3HecRitKWXEinm-pdR_1ewCHm8ibhajzyG65wqE30zKriq3-C7RDTi8M1mjd7R5yiM-XoXJvN1HqKIK7I8lvndOyX2k_8yzAixKKXLZyTSzilThPkDowp4yxaYRwU6ZIlD0ESWBGK7lyGGCGcpYHDSelBcRnBpk5hkYddL5UA6xbabAUqTLrAX3KW2LuvTZ3jnb1fcRU_yVP0bGEy3d3FAGb_2J2lNFD4SFnkIF6qn_w3CMWFBKcIFVENBJbLpzLxYdUD4lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/694eec3d51.mp4?token=arMvm99TJf9M5scjlCqw_97QmHK4UcpscF1lI2OMKcbptvKWt7G0xwrUOlhUZ25fIhnKtMvHYYBYp-3HecRitKWXEinm-pdR_1ewCHm8ibhajzyG65wqE30zKriq3-C7RDTi8M1mjd7R5yiM-XoXJvN1HqKIK7I8lvndOyX2k_8yzAixKKXLZyTSzilThPkDowp4yxaYRwU6ZIlD0ESWBGK7lyGGCGcpYHDSelBcRnBpk5hkYddL5UA6xbabAUqTLrAX3KW2LuvTZ3jnb1fcRU_yVP0bGEy3d3FAGb_2J2lNFD4SFnkIF6qn_w3CMWFBKcIFVENBJbLpzLxYdUD4lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدرعات المرتزقة بيد القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/90194" target="_blank">📅 17:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90193">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0dea1e354.mp4?token=a8kaCjt41B_1z2GEP16Rtel7OgVObapjgqw854cKmazPLtfO17vEkbrHTxh5OoaHVPqBlVP3WjrWLMrc7GXmAQ4fEBuWoaJmhEo7e-S7osKBaefOVvCQT0hGbQvZAVeYGkbTGclZXI8KU7d4-TrS6OnvDIdgxg-pwiuaU3W03Be7LkIwyRwgl4wY0XtKg5GiV9mgJzSojxAWtsk3S3iUXQbK8KwOxOCVsEOQihvwWzm_rkSrvYb_9ea2J91YazZnB7XVgg0G27K02YmViB0I-CtM67VRTSsozDwL7EgfsbI6Eadfyw0ytS8svvui2u31uPafR-9swWJiffeHsTXRrB3dkIQykQV6s1q2s0ztHPlEEOnvshwHEAaQ1u8YbdATVg6JNkVTs95U5t4n7xvvdd0Dtycv4-H-qmoDfm19Mew_8Ete04ABfNqRvgu82rDoNIIbYwuR1N9J04l6LdlGJXnf3Q4__xP05oMEtj9XIV3JrHywwUH2ZXT79NPqWoOragdliBLdWDo5vLzXjdre6435KIj_Lq3_wAKrKhiuiYE_r6JUD-JZ3SN_GeqwltNBb_FyK0EcX8ENHrARDbyrzY5v3fggp38svZilg2ZEEcZu4qhLQSCPTrkYKWk0UZo9Ea1jfsLZlayH5SOrkiSsz35BOF6ZCTrz1vIl-dnz8cM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0dea1e354.mp4?token=a8kaCjt41B_1z2GEP16Rtel7OgVObapjgqw854cKmazPLtfO17vEkbrHTxh5OoaHVPqBlVP3WjrWLMrc7GXmAQ4fEBuWoaJmhEo7e-S7osKBaefOVvCQT0hGbQvZAVeYGkbTGclZXI8KU7d4-TrS6OnvDIdgxg-pwiuaU3W03Be7LkIwyRwgl4wY0XtKg5GiV9mgJzSojxAWtsk3S3iUXQbK8KwOxOCVsEOQihvwWzm_rkSrvYb_9ea2J91YazZnB7XVgg0G27K02YmViB0I-CtM67VRTSsozDwL7EgfsbI6Eadfyw0ytS8svvui2u31uPafR-9swWJiffeHsTXRrB3dkIQykQV6s1q2s0ztHPlEEOnvshwHEAaQ1u8YbdATVg6JNkVTs95U5t4n7xvvdd0Dtycv4-H-qmoDfm19Mew_8Ete04ABfNqRvgu82rDoNIIbYwuR1N9J04l6LdlGJXnf3Q4__xP05oMEtj9XIV3JrHywwUH2ZXT79NPqWoOragdliBLdWDo5vLzXjdre6435KIj_Lq3_wAKrKhiuiYE_r6JUD-JZ3SN_GeqwltNBb_FyK0EcX8ENHrARDbyrzY5v3fggp38svZilg2ZEEcZu4qhLQSCPTrkYKWk0UZo9Ea1jfsLZlayH5SOrkiSsz35BOF6ZCTrz1vIl-dnz8cM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية من جزيرة ميون المطلة على مضيق باب المندب</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/90193" target="_blank">📅 17:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90192">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇮🇷
المتحدث باسم الخارجية الإيرانية: خطط لعقد اجتماع إقليمي يضم العراق ودول الخليج الفارسي.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/90192" target="_blank">📅 17:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90191">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇷
المتحدث باسم الخارجية الإيرانية:
خطط لعقد اجتماع إقليمي يضم العراق ودول الخليج الفارسي.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/90191" target="_blank">📅 17:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90190">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇾🇪
🇾🇪
بيان للقوات المسلحة اليمنية:
بسمِ اللهِ الرحمنِ الرحيم
قال تعالى: { وَٱللَّهُ أَشَدُّ بَأۡسࣰا وَأَشَدُّ تَنكِیلࣰا } صدق اللهُ العظيم
في إطارِ ضربِ تحشيداتِ العدوِّ السعوديِّ المجرمِ ومواجهةِ عدوانِهِ السافرِ وحصارهِ الظالمِ المستمرِّ على شعبِنا العزيزِ منذُ اثنَي عشرَ عاماً لثنيهِ عن مطالبهِ المحقةِ ومواقفهِ المشرفةِ في نُصرةِ الشعبِ الفلسطينيِّ المظلوم.
ومع استمرارِ الاعتداءاتِ من التحشيداتِ التابعةِ للعدوِّ السعوديِّ على أبناءِ وقُرى وعُزَلِ الساحلِ الغربيِّ طوالَ السنواتِ الماضيةِ وتصاعدِها في الأشهرِ الأخيرةِ، وفي ظلِّ النداءاتِ المتكررةِ لأبناءِ تلكَ المناطقِ لجيشِنا المجاهدِ بالتحركِ لإسنادِهم ورَفْعِ الظلمِ عنهم؛
أطلقتِ القواتُ المسلحةُ اليمنيةُ -بعونِ اللهِ تعالى وبمشاركةٍ كبيرةٍ من أبناءِ شعبِنا وقبائلِه الحرةِ، في الثالثِ من سبتمبرَ الجاري- عمليةَ "والله أشدُّ بأساً وأشدُّ تنكيلاً" العسكريةَ النوعيةَ الواسعةَ من عدةِ مساراتٍ؛ لطردِ التحشيداتِ السعوديةِ في بعضِ مديرياتِ الساحلِ الغربيِّ التي ترتكبُ أبشعَ الجرائمِ بحقِّ المواطنينَ، وتسعى لإخضاعِ الجغرافيا اليمنيةِ للاحتلالِ والسيطرةِ السعوديةِ.
وقد تكللتْ بالنجاحِ والتوفيقِ من اللهِ سبحانه وتعالى؛ رُغمَ الغطاءِ الجويِّ الكثيفِ من قِبَلِ العدوِّ السعوديِّ المساندِ لتحشيداتِه، إلا أنه فشلَ بفضلِ اللهِ في التأثيرِ على العمليةِ، وقد حققتِ العمليةُ النتائجَ التاليةَ:
أولاً: طردُ تحشيداتِ العدوِّ السعوديِّ من ستِّ مديرياتٍ من محافظتَي تعزَ والحديدةِ بمساحةٍ إجماليةٍ بلغتْ 5400 كيلومترٍ مربعٍ وأصبحتْ بفضلِ اللهِ آمنةً مستقرة.
ثانياً: ضربُ سبعِ فِرَقٍ عسكريةٍ من تحشيداتِ العدوِّ السعوديِّ بقوامِ 38 لواءً عسكرياً، وقَتْلُ وأَسْرُ وَجَرْحُ المئاتِ من منتسبيها.
* ثالثاً: تحريرُ عددٍ من أسرانا الأعزاءِ المتواجدين  لدى مرتزقةِ العدوِّ السعوديِّ منذُ سنواتٍ في الساحلِ الغربي.
رابعاً: تمكَّنتِ القواتُ المسلحةُ -بفضلِ اللهِ- من تنفيذِ (32) عمليةَ تصدٍ للطائراتِ الحربيةِ السعوديةِ، وإسقاطِ تسعِ طائراتٍ.
التحيةُ لجيشِنا المجاهدِ العظيمِ على جهادِه وعطائِه الكبيرِ في سبيلِ اللهِ دفاعاً عن شعبِنا وبلدِنا، والتحيةُ كُلُّ التحيةِ لشعبِنا العزيزِ المؤمنِ المجاهدِ وقبائلِه الحرةِ على ما تقدمُه من دعمٍ وإسنادٍ للقواتِ المسلحةِ في معركةِ التحررِ والاستقلالِ واستعادةِ السيادةِ الوطنيةِ، ولما يتمتعُ به من وعيٍ عالٍ في مواجهةِ الدعاياتِ والتضليلِ الإعلاميِّ الكاذبِ الذي مارسهُ العدوُّ طوالَ الأيامِ الماضية.
إنَّ القواتِ المسلحةَ اليمنيةَ تؤكدُ أنَّ الملاحةَ البحريةَ آمنةً لكلِّ الشركاتِ باستثناءِ السفنِ السعوديةِ التي سبقَ إعلانُ الحظرِ عليها، وأنَّها مستمرةٌ في تثبيتِ معادلةِ الحصارِ بالحصارِ وضربِ تحشيداتِ العدوِّ السعوديِّ والتصعيدِ بالتصعيدِ؛ حتى وَقْفِ العدوانِ ورَفْعِ الحصارِ عن شعبِنا العزيزِ.
واللهُ حسبُنا ونعمَ الوكيلُ، نعمَ المولى ونعمَ النصيرُ.
عاشَ اليمنُ حراً عزيزاً مستقلاً،
والنصرُ لليمنِ ولكلِّ أحرارِ الأمةِ.
صنعاءُ، 29 ربيع الأول 1448هـ
الموافقُ 11 سبتمبر 2026م.
صادرٌ عنِ القواتِ المسلحةِ اليمنيةِ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/90190" target="_blank">📅 16:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90189">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aedecda38d.mp4?token=CdWP0aEY2LlUN-tXC2soFBZ8sfP14bu2_S0vIKQfTbyQAnmqW0O465S5FMkvxs67HS0YmW0CwkBlE6Dpiz6LhbYBbvvMLGjVRcY5SDjXYdyUas7-C26yZnuvdYTATiMSLS5Kv0LIKyv4dFS8Sv53-t8hW9iYzwja3Cp_RmX2mNaoVspvx7vY4pYnuDAxz9y6ki8YinrWadny59OlpjxSNiIN5fxnhmu_KFkHEllu9wnsIPMv0k_iPuCYeLP5HOL4QuAE9uKIRdUYUw4gyOSoEQuQLHSvVzbYRYyzGKiHjE83fTcFtWs_86_LtddbWkfDGfeU90SjOr7TcRoG841jqoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aedecda38d.mp4?token=CdWP0aEY2LlUN-tXC2soFBZ8sfP14bu2_S0vIKQfTbyQAnmqW0O465S5FMkvxs67HS0YmW0CwkBlE6Dpiz6LhbYBbvvMLGjVRcY5SDjXYdyUas7-C26yZnuvdYTATiMSLS5Kv0LIKyv4dFS8Sv53-t8hW9iYzwja3Cp_RmX2mNaoVspvx7vY4pYnuDAxz9y6ki8YinrWadny59OlpjxSNiIN5fxnhmu_KFkHEllu9wnsIPMv0k_iPuCYeLP5HOL4QuAE9uKIRdUYUw4gyOSoEQuQLHSvVzbYRYyzGKiHjE83fTcFtWs_86_LtddbWkfDGfeU90SjOr7TcRoG841jqoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية من داخل مدينة زايد السكنية في المخا</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/90189" target="_blank">📅 16:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90188">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/650f87549f.mp4?token=OR5nPVLvagqeadCR3-2IwSOkdFzU3oR-nHiJ1IfA4oSBoEfgp48MJGbXb1heDckGPiJ_coM_aYDEFzsUpFW496fmdnOlBdtpvqnLn04yr7c28PiW7S-1Jwe-gitn39IQbGwEyehOJ2XCI44gsXCUQiNiTvPRAepewUyDH3K45R9sEijqSVvN5XGPlDIHtfjL9_-nWAY6Q8SygJR6v9Xi40ZdGSfhyjJlCRs8Nr_oj0jzAQZeJu6RQdK1QJFUiX-5bqyCPkUKwzL-iyTbNiIznysUAQmRkdqlxguP2yw3gKlg3tsOIZvOKhGABNImfD_tBxDUNe7HioYFE-Ez51XVUlpasMk638g8rXGRNvQ36XhmaO4pEZlASzUexuiKBbLLjvI7RvonKKhWwjvH6A7ruFl8uS82lOCnDG1YyRVN81lkvg3tcmBt9dDmE7n-nZefJasQleBbqlLoCPz_UxPPl_dhbA3Ye4-k6UvPb4R1YoAKPNbrlhCI9yPHur7TdgsLvS8KxRCtscxzM0inyK7S7XSRy8uT0Ai0b8mFKGZY0_l-TJVFUm0qI2bGB6lrCY9dd4b7fHosoQUV7z16q_72vceASgsGCuJAiYlKezXl5EvIfboCL6XiE4k40rCs_5Aqs6JSVmcuCKPL-EpvCSpL72JvFpwNhAAGJrdwSLHwcic" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/650f87549f.mp4?token=OR5nPVLvagqeadCR3-2IwSOkdFzU3oR-nHiJ1IfA4oSBoEfgp48MJGbXb1heDckGPiJ_coM_aYDEFzsUpFW496fmdnOlBdtpvqnLn04yr7c28PiW7S-1Jwe-gitn39IQbGwEyehOJ2XCI44gsXCUQiNiTvPRAepewUyDH3K45R9sEijqSVvN5XGPlDIHtfjL9_-nWAY6Q8SygJR6v9Xi40ZdGSfhyjJlCRs8Nr_oj0jzAQZeJu6RQdK1QJFUiX-5bqyCPkUKwzL-iyTbNiIznysUAQmRkdqlxguP2yw3gKlg3tsOIZvOKhGABNImfD_tBxDUNe7HioYFE-Ez51XVUlpasMk638g8rXGRNvQ36XhmaO4pEZlASzUexuiKBbLLjvI7RvonKKhWwjvH6A7ruFl8uS82lOCnDG1YyRVN81lkvg3tcmBt9dDmE7n-nZefJasQleBbqlLoCPz_UxPPl_dhbA3Ye4-k6UvPb4R1YoAKPNbrlhCI9yPHur7TdgsLvS8KxRCtscxzM0inyK7S7XSRy8uT0Ai0b8mFKGZY0_l-TJVFUm0qI2bGB6lrCY9dd4b7fHosoQUV7z16q_72vceASgsGCuJAiYlKezXl5EvIfboCL6XiE4k40rCs_5Aqs6JSVmcuCKPL-EpvCSpL72JvFpwNhAAGJrdwSLHwcic" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية من داخل مدينة زايد السكنية في المخا والمخصصة لسكن المرتزقة</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/90188" target="_blank">📅 16:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90187">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70538256bd.mp4?token=Uyoa3LW3Y-VzNPMAdeWgbeo9WmIN4vfdOwyCwSDxSYLKKurJ3YXdI__-97yOIsSXyIhMF5wce0ZeZjdZGyM6PL8Jf7B5lyr0iKd8UeZnodVWuhXVrttiGCKr5WHAvaX7dgVjvWBlphwJGrrBfCqcMJURqSqiIq-qWdB8N7UQWCsDdv3GL4LmYyH2I4EldQJm-cmYHgGN1BvqMpPRJ7WzV3Y_PVdkx-Lu9-P8J_eze1WKmSDeK0HmzFWimKQ5_Fu52zaQnI3TkxrLgrGfaj-xFT12LTYMxKNEBnM_kyzJoYM9emyl9fP__gEx0fJkKKfkWb0NZz-kqd7Zkmp5h1o4Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70538256bd.mp4?token=Uyoa3LW3Y-VzNPMAdeWgbeo9WmIN4vfdOwyCwSDxSYLKKurJ3YXdI__-97yOIsSXyIhMF5wce0ZeZjdZGyM6PL8Jf7B5lyr0iKd8UeZnodVWuhXVrttiGCKr5WHAvaX7dgVjvWBlphwJGrrBfCqcMJURqSqiIq-qWdB8N7UQWCsDdv3GL4LmYyH2I4EldQJm-cmYHgGN1BvqMpPRJ7WzV3Y_PVdkx-Lu9-P8J_eze1WKmSDeK0HmzFWimKQ5_Fu52zaQnI3TkxrLgrGfaj-xFT12LTYMxKNEBnM_kyzJoYM9emyl9fP__gEx0fJkKKfkWb0NZz-kqd7Zkmp5h1o4Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عناصر القوات المسلحة اليمنية يجربون صوت احدى غنائمهم من مرتزقة السعودية</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/90187" target="_blank">📅 15:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90186">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">القوات المسلحة اليمنية من داخل مدينة زايد السكنية في المخا والمخصصة لسكن المرتزقة</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/90186" target="_blank">📅 15:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90185">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">القوات المسلحة اليمنية تردد شعار الصرخة من سواحل المخا وباب المندب</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/90185" target="_blank">📅 15:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90184">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d06ad01a85.mp4?token=rZxtVDlgMlwwzyZgc6E99WYw0PFGdSWz2tVuu_24R1K9cjslxuupbtElUxu7h9zYHIO8xpT3NZIVf1mLPzvPpk8VaZTf-WTIcj9H5rOuNd82IWCa1XFZqag19tYLIsFXrqSrTNlpMY7_Ig9UFQKyO5lULinpPww7kgrPCAVY1wed-kZOZT0BzdMkBDJq4THeY6UhLYJlW1L4IbIjXOi2wtLy21LchXbDPad9gO5iRfXZJM5sgbfk1r7DqQbOO24mXJJ3w565KYfu1RcrzUqrc-37wDxP9_5w58GQDMLgnSIrmIsWL9GqcBDkLSZdM8DDEawToKh0sVIcMYFUbzSKaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d06ad01a85.mp4?token=rZxtVDlgMlwwzyZgc6E99WYw0PFGdSWz2tVuu_24R1K9cjslxuupbtElUxu7h9zYHIO8xpT3NZIVf1mLPzvPpk8VaZTf-WTIcj9H5rOuNd82IWCa1XFZqag19tYLIsFXrqSrTNlpMY7_Ig9UFQKyO5lULinpPww7kgrPCAVY1wed-kZOZT0BzdMkBDJq4THeY6UhLYJlW1L4IbIjXOi2wtLy21LchXbDPad9gO5iRfXZJM5sgbfk1r7DqQbOO24mXJJ3w565KYfu1RcrzUqrc-37wDxP9_5w58GQDMLgnSIrmIsWL9GqcBDkLSZdM8DDEawToKh0sVIcMYFUbzSKaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية تردد شعار الصرخة من سواحل المخا وباب المندب</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/90184" target="_blank">📅 15:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90183">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">القوات المسلحة اليمنية تبيد ارتال مرتزقة السعودية الفارين</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/90183" target="_blank">📅 15:41 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90182">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">من غنائم القوات المسلحة اليمنية في ذو باب</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/90182" target="_blank">📅 15:29 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90181">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">القوات المسلحة اليمنية تغتنم معدات واليات مرتزقة السعودية في ذو باب بعد فرارهم</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/90181" target="_blank">📅 15:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90180">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">القوات المسلحة اليمنية تغتنم معدات واليات مرتزقة السعودية في ذو باب بعد فرارهم</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/90180" target="_blank">📅 15:27 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90179">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">القوات المسلحة اليمنية تبيد ارتال مرتزقة السعودية على الساحل الغربي</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/90179" target="_blank">📅 15:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90178">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kyvl5Hor8OT0uVWjiBNVG_pZVG5DZPR-e6HDIubTcQ8Rjj-F2zsdCmJ5uBQM9_fNGf8sGWYs1VC9EaY4LneGjxOr-NaIPr5eWWDPr9gPKKcOApAyzOBi7UFTjyD1lSxLD1CM3SiLSObty3QrsNeyD3rjOtbEEDxN0ewZx_akD7qKBVSPGppkLzUAYudJRx_-N36KN-nNMjvgjsH3r7m5M0o0mn3quFX3ASy1s5h1rN7eDhaODeXEmX5w-Yc0iYx01J4kk7hbL7n7JXTDZDyUTJre19veKWAEfaDmRhCUuE3OwMxmTJVbBAmAYYtIfVsAqkZcCDNSs4CSOfKmm-yOow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">القوات المسلحة اليمنية من امام مركز مديرية ذو باب بعد السيطرة عليها</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/90178" target="_blank">📅 15:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90177">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‏
تلغراف:
إسرائيل
تطرد جنودا بريطانيين كانوا يراقبون عنف المستوطنين في الضفة الغربية</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/90177" target="_blank">📅 15:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90176">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇱
اعلام العدو:
المنظومة الدفاعية تتأهب بشكل استثنائي شمال ووسط البلاد.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/90176" target="_blank">📅 15:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90175">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0d1DPQZP-26MQYOatDWUg7jJUSoKiQ3DXraWOs381l2eg2eHT3VtWNDsG5W_9jTKjbY_r3Ifh7KvoI_EsZDBChFmhvRMcBHxwfeszgsOFqhujU7usY3stCnSdV6FNF51HoH0_iIOQmFfqM8SprlelLmckQosegGgnZfbUGnxGDm2YWHlBSa_Ak3m9bxn9RoCzCVDJPNVCvrJZj9ogWeYKKinH5s4gHW5xmOZVBS-L0rXRzkE1T2NbeDdCrEdvRtZss2JEMpdYLV2cvmRaW5kn9EhRDiB3XfC86Am1X4shXrc5L-vcP-6meUVo3YsmQU-Ln1GHD8DebKIIqgCXbIdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
اسعار النفط تنخفض قليلا وتصل الى 104 دولار للبرميل بعد تقرير امريكي عن مساع لاتفاق مؤقت مع إيران بشأن مضيق هرمز.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/90175" target="_blank">📅 15:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90174">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">القوات المسلحة اليمنية في باب المندب</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/90174" target="_blank">📅 14:39 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90173">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f399cdb5f0.mp4?token=lLgdOypK6JxorLKupsmYidL1zp3z8Vuw2VLDnGmPgGJ8v-TG7AgnhtKw_RcVlWrWY6LnMmy4O7pYUfwEOjAlpnw-5XkBwinEOhu6GuArD8r7rb_WAvZ7QoVETW2Jame6TkWWtIfmYwMGbJyUl5LdTyskfi8YoZ8x05BQk21_sJqAgeaobWAhQYaOcetv9m3UevxcBDlPI4LTLoPqQBLNOAnGKPLZR3tzJ4PcbH2LWlVczwGTVQHDLKx5hfOW9Sjg9nqjeMotZnOY5v_YKq5UC9H1BX2yDgOxoeXDuDHEaWsoukJRXz25neC3QI4nlswE4MR0cI-JSl-YOPh2ePeyfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f399cdb5f0.mp4?token=lLgdOypK6JxorLKupsmYidL1zp3z8Vuw2VLDnGmPgGJ8v-TG7AgnhtKw_RcVlWrWY6LnMmy4O7pYUfwEOjAlpnw-5XkBwinEOhu6GuArD8r7rb_WAvZ7QoVETW2Jame6TkWWtIfmYwMGbJyUl5LdTyskfi8YoZ8x05BQk21_sJqAgeaobWAhQYaOcetv9m3UevxcBDlPI4LTLoPqQBLNOAnGKPLZR3tzJ4PcbH2LWlVczwGTVQHDLKx5hfOW9Sjg9nqjeMotZnOY5v_YKq5UC9H1BX2yDgOxoeXDuDHEaWsoukJRXz25neC3QI4nlswE4MR0cI-JSl-YOPh2ePeyfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انصار الله يقضون ساعات مميزة في ميناء المخا بعد طرد مرتزقة السعودية منه</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/90173" target="_blank">📅 13:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90172">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQJlllDHCkWovB6CBRoOb_4PYWViAalgUER49pmREJs4EwGed9A1o8Cxm0Ty_QUL6iaU4uH_HU52dwd0bOtTBaAU29EkYyxNuLy-bIT6wkWOguKuFbPHvdj--s6NJL96UVcsyC62UAgmV7ShWO265yE2Nxob8gabXl-EXgCYP2DDCkEwFuBEzeb-wgOTHrKjTv7ATGkUv-sJuPBZwf0h1320p5AMYO83tox7jrNB4XuxvF4PzExhBHXhW1JQBd36mO97lOJ9UY0wMdeKxiuhEOSd5bXRTRJHi9OYq87-l4s4Ox8nYCKYPLLDvzUAaH72PC7sbNSQrmzZPqVTWwE47w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو انصار الله حزام الاسد:
في سياق معادلة «التصعيد بالتصعيد»، فإن أي استهدافٍ للبنية التحتية أو المطارات أو الموانئ في المخا وذوباب وميون وغيرها من المناطق اليمنية، من قِبل نظام العدو السعودي، سيُقابَل بالمثل.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/90172" target="_blank">📅 13:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90171">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">الاعلام الاجنبي: انصار الله سيطروا على جزيرة ميون واستكملوا السيطرة على مضيق باب المندب.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/90171" target="_blank">📅 13:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90170">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇺🇦
انفجارات عنيفة تهز العاصمة الاوكرانية كييف</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/90170" target="_blank">📅 13:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90169">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔻
الرئيس التنفيذي لمطارات دبي بول غريفيث:
دبي تدرس نقل أجزاء من مطارها الجديد تحت الأرض، بما في ذلك تخزين الوقود، للحماية من الضربات المحتملة بالطائرات بدون طيار والصواريخ في أعقاب الحرب الإيرانية.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/90169" target="_blank">📅 13:11 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90168">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">القوات المسلحة اليمنية تستهدف تجمعات المرتزقة في رأس العارة بثلاث صواريخ باليستية</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/90168" target="_blank">📅 13:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90167">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مسؤول باكستاني لرويترز:
باكستان تحاول التزام الصمت في الصراع السعودي الحوثي الحالي لأن مصالح باكستان الخاصة كبيرة ولا تريد إفساد العلاقات مع إيران.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/90167" target="_blank">📅 12:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90166">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">عدوان سعودي على ميناء المخا</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/90166" target="_blank">📅 12:31 · 20 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

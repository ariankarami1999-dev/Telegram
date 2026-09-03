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
<img src="https://cdn4.telesco.pe/file/oHN3QiGLRDYxAVSqUaSAM06iWOdnDDXaHZ_9ljPrJN5YvII6Twk9ip4OfBC577_Zq0bkIupPGbAJ_XoEKUDjYFmaYyT_XfAM0_Hf6MVmyNYeLZFCb5Cxqg1ssrJk_Hi1WhhtnI4-3R5H5VNtH32Ht8DCarKaAuSUH_8OaYW8ZNitdWTa5LdxtMXMwxCBotluVMg38bXwSJTeLcJ9Hh8nOkymtVZ_gSBQkiw1uqzEf45Y3cViJJbeMvdHnvqJsHk3DjiDL7itLpuJzrnbRYqTqLtzdzNpn2P1guVIPGHeE8WLEj8tTFC-WHYRR8qypdii0kduVygsHQgXYvdJUQczkw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.47M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 12:48:51</div>
<hr>

<div class="tg-post" id="msg-686856">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
استقرار نیروهای آمریکایی در خاورمیانه را تا سال ۲۰۲۷ تمدید شد
جروزالم‌پست مدعی شد:
🔹
پنتاگون استقرار نیروها در خاورمیانه را تا سال ۲۰۲۷ تمدید کرد.
🔹
منابع گفتند که حضور نظامی با هدف حفظ توانایی دونالد ترامپ، برای انتخاب بین فشار اقتصادی مداوم، عملیات نظامی محدود و تشدید گسترده‌تر تنش‌ها است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/akhbarefori/686856" target="_blank">📅 12:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686846">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bO5A5d0wB_RTaduRlKGzzyx3AYrNzg58zRnmNMP3JDtmCTd4Ab03SIkXZdoNuiT9rC0daEjOm8tS5WJDj-3L_oXCMhRUzYPXIzS8z9AaxS0mFsUw0A65W0V96yEObA5x3MWEQ7AKcplZwbh9diY-ikNGdR8cPrcTqcTFvH5VrUPZl8RntPlYbNlix33mNL1ewjHHggPg9daT9cLslIkAejDIji7tMueGl-OZNUCl-koS6vjSuVz7dKnHaJQ6_-KVqkLdeCY67PDqTbgU0WbLPTX_FCCM2Ln4i04yiTEfTy6B9PxRtRBjYm2P1bc6LJQhtyu1IDKTN3YvIVRvkwdGiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lM4t4pD12XPBK2Uk3KQ7gWRV3jWtAyMVOtaJUUfO3WnhGHrWHtbm7ChPALuh58PcDA0k0imF6OlqbAAEA2nIZFEa9fke6_0gZOQq5dpqjYfkeGjCZWcwhgmi1gbJ68qSyTZJOylTCjOM8lj-n5sKkA61m5mBbHQOKOFnYGFjlDRO5nDLOoMqMljs7Ze5bZwMaAsgKArMFO7afnfxoIPy6EXj7nuKI_A_9BuYwJlxumIjkkcYtPp3wwzJ3mLwbe-pNU7RG5agmh0a5anXxnoWaeh7G3naOJGrYB23P7uuUadm9hNhpfp6c35cxDHuPavASSKh1f_zkHwQlzFQHPpk6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mXnNPdwILQLEpbuhh3abrxw6GOD35sL5nBCp73YXbaZ3LZtJ75qAddcE0QMBhLmAoizEmEYLTJ-xLHR-eltZ4_n-FzESu60a_uOTs5wQYPXUrFZdfFAu4TM1vNYjY-aFfVTlhmR-8-xqPrs-UoEK04nCpNknjZlQp2l0GP93eTPMZ_EZPF0C1iw2s7u9d8MKbCGGH55AfaHaj7WVXdBlaJx3dfoxhzfGBvNKESOvIuB653jlSmbxsPDaxo6qQv-WsMVzCXyybeb0S1pQNMsvuuir2JuazbByyoekkL0uoKyHLxPKb5p-3gaGxcHs0D4OXV0fu2Xmn3RJ6O-3G_hhsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DmaCw-lyHoPi3gQjIykt0Wsm4OfzCC_0zXnMJpvxu1t5rRYVOm8CN0Qxffc9vbOHFBVqPYXNOPLeDZFGb16iVdvTtE07AHyND1p-H_kKVcOtWrlJ4gPJ8c5u2sEEZaYtU71oRAxtLVlOhlddE1DPxsrnFrw-N2TKqj-5XaZE5IRPMh-JSWamatvHqLkOcVCZn7k8XITThcBWHES23Y_nZ4E0TTc1W9JW6uq7yrGiM-m6tji5vESAOnM2FgCaX9UWg4n0Vg3l2598ZBv4z2M9Jpw_u7tkhjJWVuVYj0aCJg58c2O0VrjwUkh-VmbHWwdoq-8yFsVpl0gP9HY9ZgCECQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E_s6e9mcfJZt0FD9nHutIb2Kj2xKABcWTsO3yq1G7tzJAYRaVEfwoQktvsXx237O-Q0HwggkznAyvWqQu8E-uP4qTDggObmifqawccvD8Dg-3I4DtpnuaazyVQJwVEQw8cw9FxpPXx_Vpva65gh0Ol-gL4TpMHr-bryufZ5MTkgAQAs9tv1CJ24vVFp4r7Hzk4jurk1NDMe0W9mzyhf7kvDJWrTq1Gw8RgjHIhPz22wXYQ7jDuvL5fNLarunFdwODFm9x5Hw_1U7IQxvEsg46kU4g2q1GALSEwJs4faP5UmJMNxT6ilP-FthG3cToEkDwA7gMpbge1198JsXAYJfcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DAY41mUBcqUCTS2NN3iSwG499zIpmrUtT_M8ropq1st_LbIBdnYYUb6cD0WFZfunUTKkmlhTAy8nfUNPGHtmgFdMvSc7FDUbDpRVPC8KhvDTx47-ojMCZppgOMZZStynq2HD-Dy1lIHlf7s7Ps6iNoY20NEisFQ44B5rkp46cp8Na9MuVi89kzRmLqgmf08GCeKmUA_GEyl0tAnjjx3wNsWJ0t7oe6D3kSVPdjbytXT6TC1EKE9fvZLHcSh38e24vWLP6taQTCjji-oS6dRcUtXJSBUGQPIikGtk33YBpyo_r5t5W0r2aY3sHWHPaXbQbMMaxV1udOCrlTK_0zSEcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EBE57tMzzsUnRbMNGDzeXJBb2lutld9UiBc2xqx1y2tz3oMpfMX5fg2tXx8fh925_bFt33Mg-FTsPDmJqvLpM2LCfEU_3R0jqdaMu_akVFuY_M5Xzk07qH6D4uqvfiMiUSamb1iwlA3E8CU1DEoSk5EC-g1WkzGElUfsxsGc1u3oBEgKxKIGYdan44P5AKC_h0MD1MhTvk9tCJxM7kEwsDnwDAeF3Zc648qR0QDp8q4tiJT8dZ-br2c2ix48nvFU-rLC_4Ca0hAaC79bHZCN_vIPQ0wQgoFQr2HAFyUF-6DUfn4izPokUuu3qprfhSFdMKNzn2EQuJUMGag7n4T4PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aFoGBEjnCV4ypUTY0MQtdjXLNYfZ2zWslooLxxchVwpjvGQEcry8k2p66u0Oy47euABrzx6qfDUwRUR7FehpmuDhzOl9d05AzNus7ZA1EBIcHdHgwTwxgI_HBb0a9rulsGLWFkLC8A6HjexjF1ACgkT5mBfLmZvKT9DK_zqcNdxxTGqX4NA5PSVPqu3wO4Jal9vsJdihAPi1Jj8deltdVJ3XeA06oki06t6iMmueAuUvMZH9lBjQXiq8qlHi3adxsTbG1Gvsq5-uq2HG72jF23MAxqJVSm3qWMpGEPutFciwHwHUZmmmFYmFw20mPrSptd8AQZWb7YC-OngOvwQWmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a0Yu_aTOa3OeReNoZjtc33EjzdAizEZiAVnQHfXWZnn1sXKuRG3iOpLyLa4ffYKt9iazdH8dA8lycGzJluNq4-WV79_eIBG3ENFEwk6PujfT9-7Vo16pLQ-rEAvfxx7Y3TdKCobNHMmAmwJRI_O5p54tiNJJgmTuMtvzEZijzSUVVmqx5MDgvTognP5AqPtFKkWwvOsyEZNVQaEJaPThKhZK5iq_3JQEQGx3iC4zAGFup6JfB7C9Fem5JiyUitzVGAFxIWuku1SyJIACopz8f3slmMeBM2qJnkYk3-mm27LQGachxi1tUgdu-feUTIEQkNYd5e0PqDoobgpGisBFKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WUBE_P0VPdTezlck4kfs1t9Skms_ntZpoDFYY2ysgYDHCejd-FDymSK8Rnd0ZSoT6lhdrisEi__emjzk898e-5ir_462OKtgpKfcwZ-ltepTsSh9jpdCr12Kmc0XqKg_sp05DWvrU9o6XPXMrP9j_eqI2SW48iLx1vQNGvf4wWGSQZllW764fiY34Qz3we65kNZ3QvcLskfZHySbdH6JfkkzsqTkeQEwz6Ne1ZzIEeJ38uUNzh3qzLA2U-sslbuLGFAI6j4nik-kzVjETuqAWfGfxeVBUpX4ip4hJv_uskUavNc57NPyL80R7MCGDcqJaI1NzPLAvQau8G2K-IWW4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
جا دستمالی دست‌ساز؛ با یک ایده ساده خلاقیتت رو به درآمد تبدیل کن
🔹
این بار در #چرخ_زندگی سراغ ساخت جا دستمالی‌های دست‌ساز رفتیم؛ محصولی کاربردی و دکوراتیو که می‌تواند با طرح‌ها و رنگ‌های متنوع تولید شود.
🔹
با مواد اولیه و ابزارهای ساده می‌توان این محصولات…</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/akhbarefori/686846" target="_blank">📅 12:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686845">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0d184e42b.mp4?token=vsQrgY0ge2rb8MJ87yID5LZMfLGTTbHaCKDfXCmdx3b1UAzfqQRgmUgHM1jzsJg516w0PWLgEFR_OWBsVlHB1zPOjgzPOtfUFgvC5fl679eTPi53LoMeWbrBQ03hTS1DbEUiHA71ya2zt1HnH85PSIW6b981YcJriiCtmPcraTidmk6gwjJCM9IZ57Q9mzFMnQr44mWdv4249E5CL4OFTBaBEP8ch3xMgONbOpg8s6I601wrZKCg8grCOUx9LvTJ8I3ht5Aft3OXtotpE4WlrYSsE2Ne6icZDmVExyxMidcp48i3Sl6qxg5KuQ-uhlX8WaHTLvkzLljrwM3sT6FGPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0d184e42b.mp4?token=vsQrgY0ge2rb8MJ87yID5LZMfLGTTbHaCKDfXCmdx3b1UAzfqQRgmUgHM1jzsJg516w0PWLgEFR_OWBsVlHB1zPOjgzPOtfUFgvC5fl679eTPi53LoMeWbrBQ03hTS1DbEUiHA71ya2zt1HnH85PSIW6b981YcJriiCtmPcraTidmk6gwjJCM9IZ57Q9mzFMnQr44mWdv4249E5CL4OFTBaBEP8ch3xMgONbOpg8s6I601wrZKCg8grCOUx9LvTJ8I3ht5Aft3OXtotpE4WlrYSsE2Ne6icZDmVExyxMidcp48i3Sl6qxg5KuQ-uhlX8WaHTLvkzLljrwM3sT6FGPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غذای رژیمی و سیرکننده برای دوران کاهش وزن
🔹
این غذای خوشمزه با ترکیب ادویه‌هایی مثل نمک، فلفل سیاه، زیره، گشنیز، پاپریکا و آویشن، گزینه‌ای مناسب برای رژیم است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/akhbarefori/686845" target="_blank">📅 12:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686844">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96d855a310.mp4?token=qyPZnyKr7qYFtkAa48_f5hljDESsgIWhM7Sa0C8BshfS1z8QuVsUkj6dow4mJNnc29KJrusMcMJqnRUBiq3KQ5edWhl3oFTtkWfS6K7M-n9T8VbOID2K-UywYM9F38qOL3pgq45VtQoJg7jTxvQSTlLkhgmoEWVe7IUXtJe0GB0dHDoxxI4Gi7ypTZXssfHJzKLzhIuWkESWMCcvEbggUKqBisfAcNzD5-MnkrZkaOEPRpMcREKMudp8iL7luYOst4Lj6un9_jWFwahxKlOX0iw_WeEfYWuCRfYYZgSy41Z3ctKAU3Cm2o4c8JBp76FebmovlbqaFVSt5eHoJPx98Zd_bHRCjsdKwztBhns8VVaIOb3CzkdbCGCx2yEAYcHDHvadBXDz0K_NrFdkdYWigwJOfrXvJscBsb939jLIuA1CI3wN3uBt_M6fUkHMfAanBH69NTXuIPfJcOt03Jo5UspPrIExVc3zYQCPeA5QNgrxa5RS2s0L5BUvrfncQv8sE91sDRSn16wzlk6x7xYrTUWDnpM0Bkt6aHJRELPlT321_bL_v8CLjAUrx7Lsfrlv6RexAMVxcnXw-QoqpR4xS_EJXySmPSB9rIfBaXvffhLUc8gqfH8Els0MTs3IuNBdPACeBpnZIYVpH5xBLxx6_5GvNd5kqJm_v7VKL0EHgwc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96d855a310.mp4?token=qyPZnyKr7qYFtkAa48_f5hljDESsgIWhM7Sa0C8BshfS1z8QuVsUkj6dow4mJNnc29KJrusMcMJqnRUBiq3KQ5edWhl3oFTtkWfS6K7M-n9T8VbOID2K-UywYM9F38qOL3pgq45VtQoJg7jTxvQSTlLkhgmoEWVe7IUXtJe0GB0dHDoxxI4Gi7ypTZXssfHJzKLzhIuWkESWMCcvEbggUKqBisfAcNzD5-MnkrZkaOEPRpMcREKMudp8iL7luYOst4Lj6un9_jWFwahxKlOX0iw_WeEfYWuCRfYYZgSy41Z3ctKAU3Cm2o4c8JBp76FebmovlbqaFVSt5eHoJPx98Zd_bHRCjsdKwztBhns8VVaIOb3CzkdbCGCx2yEAYcHDHvadBXDz0K_NrFdkdYWigwJOfrXvJscBsb939jLIuA1CI3wN3uBt_M6fUkHMfAanBH69NTXuIPfJcOt03Jo5UspPrIExVc3zYQCPeA5QNgrxa5RS2s0L5BUvrfncQv8sE91sDRSn16wzlk6x7xYrTUWDnpM0Bkt6aHJRELPlT321_bL_v8CLjAUrx7Lsfrlv6RexAMVxcnXw-QoqpR4xS_EJXySmPSB9rIfBaXvffhLUc8gqfH8Els0MTs3IuNBdPACeBpnZIYVpH5xBLxx6_5GvNd5kqJm_v7VKL0EHgwc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شگفتی خبرنگار اینترنشنال از شدت و دقت نفوذ سایبری ایران!
اردوان روزبه، خبرنگار تلویزیون تروریستی اینترنشنال:
🔹
فقط در یک مورد در مینه‌سوتا دست‌کم ۳۰ مرکز آب‌وفاضلاب مورد حمله قرار گرفته و ۱۰۰ مرکز مرتبط با مسائل آب در آمریکا مورد حملات پی‌درپی قرار گرفته‌اند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/akhbarefori/686844" target="_blank">📅 12:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686843">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رئیس کمیسیون امنیت ملی: قفل تنگه هرمز بدون اراده ایران باز نمی‌شود.
🔹
رئیس قوه قضاییه برای نشست سران قضایی بریکس عازم هند شد.
🔹
پوتین: روسیه از احیای کامل روابط با ایالات متحده آمریکا حمایت می‌کند.
🔹
باشگاه استقلال از تیم داوری دربی شکایت کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/akhbarefori/686843" target="_blank">📅 12:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686842">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromموسسه خیریه مهرمبین</strong></div>
<div class="tg-text">✅
فراخوان کمک برای تهیه کیف و لوازم التحریر
🔹
در سالیان گذشته با یاری شما خیرین ،  برای دانش آموزان مستعد ولی بی بضاعت، کیف و لوازم التحریر تهیه کردیم.امسال نیز به آنها قول حمایت داده ایم.
🔹
هر کمک شما، امیدی تازه است، لطفاً این پیام را برای دوستانتان ارسال نمایید.
شماره کارت خیریه مهر مبین:
6063737004808968
شماره شبای مهرمبین:
IR820600260201108691003001
پرداخت آنلاین و اطلاعات بیشتر:
https://mehremobin.org/help/
📢
گزارش کمک‌ها را در تنها در کانال تلگرام خیریه ببینید:
💖
@mehremobinn</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/akhbarefori/686842" target="_blank">📅 12:24 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686841">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کسب‌وکارهای کوچک در پازل حاکمیت جا ندارند / ورشکستگی کسب‌وکار در ایران به رسمیت شناخته نمی‌شود!
هادی محضرنیا، رئیس مرکز ملی پایش و بهبود محیط کسب‌وکار در حاشیه مراسم الکامپ در
#گفتگو
با خبرفوری:
🔹
کسب‌وکار بزرگ خودش را در پازل حاکمیت جا می‌دهد، اما کسب‌وکار کوچک متأسفانه در این پازل دیده نمی‌شود.
🔹
در بحران‌ها ساختار مشخصی برای حمایت از نیروی کار داریم، اما موضوع ورشکستگی کسب‌وکار اصلاً به رسمیت شناخته نمی‌شود.
🔹
سرمایه‌گذاری که با ورشکستگی واقعی مواجه می‌شود هیچ چتر حمایتی ندارد؛ مجبور است تا فرش زیر پا، خودرو و خانه‌اش را بفروشد تا بحران را رد کند و این رویه امنیت سرمایه‌گذاری را نابود می‌کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/akhbarefori/686841" target="_blank">📅 12:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686840">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejjiDR7JfGQz3NpN-ur1uMHoM9XjKXmJMV9XBKkPgrrDegBQ8BnZ4SUORSCRK8YuHid76zhdXP1Si8oA3sxviN1yL4MRAmDGqls3DLIrS6-Zo-Jj5GddNABvIN3vQqyC8s0GhQEopSGQujmCBA444Wk1xnGP6UOs2ErlDlM6EYB0wxCvRHO5kWFM395mH799CUwcUsLS1wpY8ruP_kDjYjaeGaD4jyCLlFl_yY2ZQBl8m8IxQ6RMmAESRcC2-tmPQ7lg2utQWtjnQJC7QVe_MdAAHlds_Yip2nnVvrXkUk2d_BgZbNha3FId4Tjby0uvvmEl8bQYGTqcAgT7xdGF7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هراس از «تنش‌های ژئوپلیتیکی»؛ هلند طلاهای خود را از آمریکا خارج کرد
🔹
هلند حد فاصل ماه‌های مارس و آگوست(اسفند تا شهریور) ۸۶ تُن از نزدیک به ۳۱۳ تُن ذخایر طلای خود را که در آمریکا و کانادا نگهداری می‌شد، از نیویورک و اتاوا به لندن منتقل کرد.
🔹
در نتیجه، اکنون پایتخت انگلیس بزرگ‌ترین سهم از ذخایر طلای آمستردام را در اختیار دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/akhbarefori/686840" target="_blank">📅 12:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686839">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b110679d8.mp4?token=kKaBlNn5UUGcXi5Z8RRttkHuJUgcOM4oLcd4SgwtAW3IPeO0ecIiZR-EnPDT1I66y5vDL9RhLBe7d7lH7saivqBc8N33Rf0ouHNrAAXfD901AmHCZgyfVzuOn6Ea5kn4NbCvbfgJPq0uf-3X7esskXpCgoeX3o3Sd5JBoybQp1h3PNtIJ4Us7alQpYo7Yo6VdptW56Llm28swTqzV7rKBk8305-xt5NQL0HxrPv7Ctr6k4TWs3TTxMxR7e9VqVQj-baVrRC9zdw-i4_1Qg3jqAr7bAlmZMen8bOqqiveKqtK_WFfLkNPxaXkl1BNbi_advLutAZxA9Y7T-MkKpI1TpiAp9VhVfgU5eiHwBuirXLsJVGnP3d41bU4bSrkeA5uzzXJ76lKaMsLSfBHkdLoj8gOdpBwqTA9Imz4Xd89QX_mLrWfCFFuBYEz0QPxG7fhxFA1Ay-WGXedA7MzABVHe7ocZuXprKGeTDQVyk7B6G-xuVWonEYZCTeX9SIbmWNwONn_g0by-97oxL4j1TbxW_RQzDQlo2Q6QlUHLMAz8kK7UZnBQief2jW5UqJ-IUmYlivTjBgXHUON3-cxyqFn7bFY9SAximcGq49w9iS-Wc_J_a63qeXSay3mJfz6rccGvF9Zs9e6eNH3ZRhMIPJDqhAMigurQMXXO2gVaKPZiuk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b110679d8.mp4?token=kKaBlNn5UUGcXi5Z8RRttkHuJUgcOM4oLcd4SgwtAW3IPeO0ecIiZR-EnPDT1I66y5vDL9RhLBe7d7lH7saivqBc8N33Rf0ouHNrAAXfD901AmHCZgyfVzuOn6Ea5kn4NbCvbfgJPq0uf-3X7esskXpCgoeX3o3Sd5JBoybQp1h3PNtIJ4Us7alQpYo7Yo6VdptW56Llm28swTqzV7rKBk8305-xt5NQL0HxrPv7Ctr6k4TWs3TTxMxR7e9VqVQj-baVrRC9zdw-i4_1Qg3jqAr7bAlmZMen8bOqqiveKqtK_WFfLkNPxaXkl1BNbi_advLutAZxA9Y7T-MkKpI1TpiAp9VhVfgU5eiHwBuirXLsJVGnP3d41bU4bSrkeA5uzzXJ76lKaMsLSfBHkdLoj8gOdpBwqTA9Imz4Xd89QX_mLrWfCFFuBYEz0QPxG7fhxFA1Ay-WGXedA7MzABVHe7ocZuXprKGeTDQVyk7B6G-xuVWonEYZCTeX9SIbmWNwONn_g0by-97oxL4j1TbxW_RQzDQlo2Q6QlUHLMAz8kK7UZnBQief2jW5UqJ-IUmYlivTjBgXHUON3-cxyqFn7bFY9SAximcGq49w9iS-Wc_J_a63qeXSay3mJfz6rccGvF9Zs9e6eNH3ZRhMIPJDqhAMigurQMXXO2gVaKPZiuk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این ابزار کاربردی، شکستن و خرد کردن آجر را برای مشاغل ساختمانی و بنایی آسان‌تر می‌کند
🧱
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/akhbarefori/686839" target="_blank">📅 12:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686838">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e0ca0d63e.mp4?token=nVjhxzxPtAkYyKSZYXvG56Mqm93a5KGkyywbHhnPoVmpR7qKCCJeaMqCND-SEJsbM2MV-z7KCaS0brw0QcEYVfdSSSL2gZpwqDQVbjsSk0cEO1Kx72YcvCOhM_Dla7YUMgJmxfhbbK579Hzso269u7zQh3JUBW_RouFSPQXnGkGJE1090djAYsrM9LqvEYrGD_60DqhL20TsSyr4Ncn9DOWLk1t2oFAxOzPHGla3COwoHq2qF045gVBqDhkTTCsdg-Wh8iNUosWAu0jReU2yL6asfv2NwoEldrGtm69Zc_Y0QgiYrdPlcmKm9xoJb9qQrxZvjdJhEerG_8gdwSy8NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e0ca0d63e.mp4?token=nVjhxzxPtAkYyKSZYXvG56Mqm93a5KGkyywbHhnPoVmpR7qKCCJeaMqCND-SEJsbM2MV-z7KCaS0brw0QcEYVfdSSSL2gZpwqDQVbjsSk0cEO1Kx72YcvCOhM_Dla7YUMgJmxfhbbK579Hzso269u7zQh3JUBW_RouFSPQXnGkGJE1090djAYsrM9LqvEYrGD_60DqhL20TsSyr4Ncn9DOWLk1t2oFAxOzPHGla3COwoHq2qF045gVBqDhkTTCsdg-Wh8iNUosWAu0jReU2yL6asfv2NwoEldrGtm69Zc_Y0QgiYrdPlcmKm9xoJb9qQrxZvjdJhEerG_8gdwSy8NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر وقت ناراحت شدی یادت باشه یک پروتئین کوچولو داره تمام تلاششو می‌کنه تا تو خوشحال باشی #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/686838" target="_blank">📅 12:00 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686837">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bc5a70cae.mp4?token=eWUn0NqWn3F_jmo_eHJ14_9RV4AJiAA-dqM2vby70yAJuAZZqGgcsL_QvjhnS9kcG9zT5fwf13IsCWeCDdOIcCbrnwoWDm2SOQYFEN2kcUq2zUc6-doSw8aghHUcpBjnwjlUMWjdHVmOOHeRzrU7DK688otjKv-D0ZmTmJ-Le1JGCZVupgldTk8-bsgGLLiwl8l0iH8vxxYgx2kd4rGkYpxzWYmJdqBrYYWwzxMN470FxOYJpHPtnQcUWn3vMCjV1U7ne_obt6gfrfqT77K6zc8KHY29uyggeGSCTA2Qc71WIJsbbMpMWKub_UdCRbtRULZMNjeLG-LzZl1twUSoAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bc5a70cae.mp4?token=eWUn0NqWn3F_jmo_eHJ14_9RV4AJiAA-dqM2vby70yAJuAZZqGgcsL_QvjhnS9kcG9zT5fwf13IsCWeCDdOIcCbrnwoWDm2SOQYFEN2kcUq2zUc6-doSw8aghHUcpBjnwjlUMWjdHVmOOHeRzrU7DK688otjKv-D0ZmTmJ-Le1JGCZVupgldTk8-bsgGLLiwl8l0iH8vxxYgx2kd4rGkYpxzWYmJdqBrYYWwzxMN470FxOYJpHPtnQcUWn3vMCjV1U7ne_obt6gfrfqT77K6zc8KHY29uyggeGSCTA2Qc71WIJsbbMpMWKub_UdCRbtRULZMNjeLG-LzZl1twUSoAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت شوکه‌کننده دختر کشمیری حافظ قرآن، از کمک‌های مردم پاکستان برای خانواده‌های شهدای میناب در برنامه محفل ستاره‌‌ها
🔹
از گوشواره‌‌های دختربچه پاکستانی تا پیرزنی که از تمام داراییش که چند تا تخم مرغ بوده می‌گذرد ...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/686837" target="_blank">📅 11:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686836">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
واشنگتن‌پست: پنتاگون دسترسی به اطلاعات طبقه‌بندی‌شده را محدود کرد
🔹
پنتاگون در میان نگرانی‌های جنگ با ایران، دسترسی به اطلاعات طبقه‌بندی‌شده را محدود کرد.
🔹
به گفته سه منبع آگاه از موضوع، اسناد مرتبط با "کتاب دستورات وزیر دفاع" پس از گزارش خبری واشنگتن پست، از یک پورتال داخلی پنتاگون حذف شدند.
🔹
پنتاگون ده‌ها سند طبقه‌بندی‌شده را از یک سیستم کامپیوتری مخفی که معمولاً توسط مقامات دفاعی و نیروهای آمریکایی استفاده می‌شود، خارج کرده است.
🔹
این اقدام پس از آن صورت گرفت که واشنگتن پست داستانی را منتشر کرد که در آن نگرانی‌های افسران ارشد نظامی درباره جنگ با ایران تشریح شده بود./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/686836" target="_blank">📅 11:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686835">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmTiw09cWCRkypt5Rbgrg7iMC-DAN82nxELo7XPa9xL7yXnGWaCr65g7tCwTbakGNutvmSXKYWpIIAbHhlQWNm1mypC4536gLMSxUoDuDA-S157d39FFSDhFmRIfLdi-G-qurvVjs-J4faDQJngnxZe0hOPXg8H320YcfZ6F4jhflmLCwxncNV-mO4-a4kdmZbdUiR93Pmu2-gFbTzuBM33vDaycRoYNeOBMwjoLWuN7Wnm4TBsTP29HDev89hr27ZiQxGkZvbDgwNc85hyRkwGVeP9qF3ypkskeTHdf1bkqcwQKmXSuqkFjEJpQbUs2GMVJnmdzRyWux97bnsFCPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سایپا هم قیمت ۴ محصولش را گران کرد
🔹
شرکت سایپا در اصلاحیه جدید شرایط فروش خود، قیمت چانگان CS55 پلاس، سیتروئن C3-XR، کوییک S و سهند S را افزایش داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/akhbarefori/686835" target="_blank">📅 11:52 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686834">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10bd6530c1.mp4?token=IrFM6nv8Ls7KaiBy_DAUE-qlVHifDOfUb0QzjC1DX9r7_6EMzP6dtA4UuX_G8aXyU7DNnqnptPajVh4TsdJQlX2VAjYKZQbe5kVw0D54SsQykLzIj9NRYC-yBQ4PCyRWMRs6xA9LqaMtObwkUEyGKW6xvWNv5a2APfDbpzOEKhRFSZtlhB_qCrPboiyioBwczihPRJOpwqlSaDeR9FWY_gdhGtaJU4wTkWkEdRbdCHrwCEm4r5QESfdWOWxUG-l8RHDptrCEEapGet4LESlJRqM_qt7OIo_uAmV7zHAUzLBx_VZQti5Rsq1PqR9rVMgQNJq0nIVuZoAlN3c5GulYSolGyIhoA1HWLmvI1U18dgxoBPHvGxcCjcJpaO8GnV1_XQgKuU5dpMa2TZ-4NtdBcQUnGSQ06N5HV8ZZAH9SNSQ5wnOsjtDI346CW1APaw9HIndzlKrd2fOFck49nVrIQGsJTUtBzyaBKp9BVQ2SdAB2FvtXhIMQLv76KPab0HSqq1qcbsuv54UktGm_bYDO7qkTRs3wTiYCas5wL4icsFC2BJqmHcbDsqkBri2fd45lgFw_vkS7Kc9EZcC5sxFqGuJ-orYgnqamZ_5Qf5kMkXlP5pTnv1WTSXlBFHYrZA0vRvcA4AkUaeXsli0XSZgvm8nRpamhNnE70p3oMyk3HaM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10bd6530c1.mp4?token=IrFM6nv8Ls7KaiBy_DAUE-qlVHifDOfUb0QzjC1DX9r7_6EMzP6dtA4UuX_G8aXyU7DNnqnptPajVh4TsdJQlX2VAjYKZQbe5kVw0D54SsQykLzIj9NRYC-yBQ4PCyRWMRs6xA9LqaMtObwkUEyGKW6xvWNv5a2APfDbpzOEKhRFSZtlhB_qCrPboiyioBwczihPRJOpwqlSaDeR9FWY_gdhGtaJU4wTkWkEdRbdCHrwCEm4r5QESfdWOWxUG-l8RHDptrCEEapGet4LESlJRqM_qt7OIo_uAmV7zHAUzLBx_VZQti5Rsq1PqR9rVMgQNJq0nIVuZoAlN3c5GulYSolGyIhoA1HWLmvI1U18dgxoBPHvGxcCjcJpaO8GnV1_XQgKuU5dpMa2TZ-4NtdBcQUnGSQ06N5HV8ZZAH9SNSQ5wnOsjtDI346CW1APaw9HIndzlKrd2fOFck49nVrIQGsJTUtBzyaBKp9BVQ2SdAB2FvtXhIMQLv76KPab0HSqq1qcbsuv54UktGm_bYDO7qkTRs3wTiYCas5wL4icsFC2BJqmHcbDsqkBri2fd45lgFw_vkS7Kc9EZcC5sxFqGuJ-orYgnqamZ_5Qf5kMkXlP5pTnv1WTSXlBFHYrZA0vRvcA4AkUaeXsli0XSZgvm8nRpamhNnE70p3oMyk3HaM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استیو بالمر در سال ۱۹۸۶، در یکی از جالب‌ترین تبلیغات ویندوز ۱.۰؛ سال‌ها پیش از آنکه به چهره‌ای معروف در دنیای فناوری تبدیل شود
💻
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/686834" target="_blank">📅 11:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686833">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/162568634d.mp4?token=cp8SCdGhiaTVSRr0flPzqMJRO_BDZOBxhCdogEYk9B26AIQE2UYlmbkiCyrQcCwb6qtDG5qCcwOLEqSS8wS2dgqVc8gwA6_HLW4XJvdQpdzogrMhsLwNvNy5zz0cnlK5tzcpxd58mGM1X_QV8g9X7IdlqjQeKyTtwi7Cl6dgOEXI5uZyu7y4JFrBjGidITW0QChwiZ4-N1JUqBIPmVUsOP_McB8KKivvCsEnsjSZ530aCpXhepM50q_AYofs6sZzyEuTFj-EnxI0eSoXD554y878tFwwAxLr4YlhJwmTgkP51DukCyJbyzo8vwBqyTITFLeCvGynv16HzfU4CtRPcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/162568634d.mp4?token=cp8SCdGhiaTVSRr0flPzqMJRO_BDZOBxhCdogEYk9B26AIQE2UYlmbkiCyrQcCwb6qtDG5qCcwOLEqSS8wS2dgqVc8gwA6_HLW4XJvdQpdzogrMhsLwNvNy5zz0cnlK5tzcpxd58mGM1X_QV8g9X7IdlqjQeKyTtwi7Cl6dgOEXI5uZyu7y4JFrBjGidITW0QChwiZ4-N1JUqBIPmVUsOP_McB8KKivvCsEnsjSZ530aCpXhepM50q_AYofs6sZzyEuTFj-EnxI0eSoXD554y878tFwwAxLr4YlhJwmTgkP51DukCyJbyzo8vwBqyTITFLeCvGynv16HzfU4CtRPcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پایگاه‌های آمریکا در امارات و کویت زیر آتش حملات موشکی و پهپادی ارتش
🔹
در انتقام خون پاک مردم بی‌گناه و دلاورمردان نیروهای مسلح، بامداد امروز، ارتش «سامانه‌های ارتباطات ماهواره‌ای»، «انبارهای تجهیزات» و «آشیانه هواپیماهای جنگنده» ارتش تروریستی آمریکا در پایگاه احمدالجابر کویت را با موشک‌ها‌ و پهپادهای انهدامی، مورد اصابت قرار داد.
🔹
این حملات، موجب ایجاد خسارات و آسیب به سامانه‌های ارتباطی و آشیانه جنگنده‌ها شد.
🔹
همچنین در ادامه این عملیات کوبنده، «محل‌ استقرار نیروها» و «سامانه‌های راداری» ارتش کودک‌کش آمریکا در پایگاه‌ المنهاد امارات، مورد هجوم موشک‌ها و پهپادهای ارتش قرار گرفت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/686833" target="_blank">📅 11:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686832">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1748f13e6a.mp4?token=P0EYHHNgHzssmi3hGaSr4lcf2KusuTf5h8SSlYmXTQIEzkfutduhPYwU6JXCN_mC5i__z22YIioJLb8gbwaD4hI2oOreUxSqfCq8AMEHUSqU_s_eAv89eGYSDZ5Au8N3t8fiufWVsOAqmxQy0Jb5gPnrxWc-SftW3EHZV389r6q2DpAqA_Vf3mYOTJw9hzFM8ElVOgEfwjC1jTb8iPhBIPDYFOIpKJhxrKX0IsyXEE0f0J03EwzR3HInMLxTDji9QgEZwBmelISmxLts4SO4MbgH6mshOc4IYqbG-NAcLxBjWo3Pb-Xi6gvbkbktmanVro_SJPdqUo3iJfQ3eiHjww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1748f13e6a.mp4?token=P0EYHHNgHzssmi3hGaSr4lcf2KusuTf5h8SSlYmXTQIEzkfutduhPYwU6JXCN_mC5i__z22YIioJLb8gbwaD4hI2oOreUxSqfCq8AMEHUSqU_s_eAv89eGYSDZ5Au8N3t8fiufWVsOAqmxQy0Jb5gPnrxWc-SftW3EHZV389r6q2DpAqA_Vf3mYOTJw9hzFM8ElVOgEfwjC1jTb8iPhBIPDYFOIpKJhxrKX0IsyXEE0f0J03EwzR3HInMLxTDji9QgEZwBmelISmxLts4SO4MbgH6mshOc4IYqbG-NAcLxBjWo3Pb-Xi6gvbkbktmanVro_SJPdqUo3iJfQ3eiHjww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نقدی بر یک شبه‌پارتی با ناظرانی راضی!
🔹
جشنواره و نمایشگاه مد و لباس «همای» در تبریز در حالی برگزار شد که علاوه بر ابهام درباره چرایی صدور مجوز، حضور برخی مدیران ارشد استانی که خود از ناظران و صادرکنندگان مجوز این رویداد هستند، خبرساز شد.
🔹
این حضور در حالی است که به نظر می‌رسد به جای نظارت بر رعایت استانداردهای قانونی و عرفی، بیشتر به نظاره‌گری یک نمایشگاه شبه‌پارتی با فضایی دور از استانداردهای زیست عفیفانه تبدیل شده است.
🔹
حضور مدیرکل فرهنگ و ارشاد اسلامی استان، به‌عنوان مسئول ساماندهی مد و لباس و ناظر قانونی این حوزه، در رویدادی که بخشی از آن با مأموریت‌های نظارتی او در تعارض است، بر ابهامات این ماجرا افزوده است./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/akhbarefori/686832" target="_blank">📅 11:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686831">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmFDFsihMnq_twLQobu7X9Q-LkMB2F1tZRiqTNk9Oi_C2rmPg-Qv5pAZd6dLCo6RG8HpEoXa96lBPfF0paym-aG0KtXiCKNShyW1a-L7wrnRISNaTvhc6078cvEXCgptCbBJVwjHUkFnVzUzoUdo9b8rG35vCpf0bMl70ca8-9hCeqUvt3rr40BbfCy2pdaCtI7yfanAaBDo9hv76fJbiDDONPnGj4SZdwG3A0uer9geS4yoxLmgh8FG71c_yEDuyTBY8oL8cqhR2BZnvq6Lk6lx-Gr_wbVxduAZyrbZUJppEz1J_MbK1hve-DQ6OvyzUzv5WgW36Js6qSfVVHD0Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
قاب فرش اشک حرم حضرت عباس (ع)
یادگاری نفیس از حریمِ وفا و ادب.
این قاب، جلوه‌ای معنوی و چشم‌نواز از حال‌وهوای حرم حضرت عباس (ع) را به فضای شما می‌آورد.
✨
مشخصات محصول:
▫️
ابعاد: ۲۴.۵ × ۲۰ سانتی‌متر
▫️
جنس قاب: PVC
▫️
طراحی شکیل و مناسب دکور
▫️
انتخابی ارزشمند برای هدیه و یادمان معنوی
💰
قیمت:
۱.۳۹۰.۰۰۰ هزار تومان
✅
قیمت با تخفیف ویژه
۱,۲۹۰,۰۰۰ تومان
📩
سفارش:
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
@ghararshop
@ghararshop</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/akhbarefori/686831" target="_blank">📅 11:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686830">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff3781c6b3.mp4?token=qfMdybgkOAlxDu3rwM3ootPFTCKSosjXk2DdcC2AJeYYCtRFj1JZhh-Ot61jGi4_W2juW8xlANbt6xY-dt0IQR8_nYVHAZgKWd7HRbnRHEHtMpqeUqKDOYjN-iRdvI7DKw_U9ysW8yadSTOjwcaizFh0Z2dG_YledU93XDpZ8nrh_fpzJ1vGDBP9trZ1Q9a1oOJUU2ZOvlNAc_EHUDJwTDIT21N5t7ucL-KdXKuhx3x0EYloEywwqV2_6saDNs-O2H8JBSreBOEcwF0uuSQ3lcz2xUDqFTiwFRUstKMNfLOXqP2qyjDTpR3F4Bk2HQjBhyxtGeVmOCPzqB1IfrBESla_3R5-ixpl4xqAlcPXJKURHFTw5NgPS0fZL7RJCGyiQkyUGlnypJXsaxNKzDXN-JRhOJi-MwX9c1L8u5VAfnNHtScjp-LCGSULYCVqAnVi2HlFm_LHv-Baa5qnGopUk2ZyHUo9SiySSNOvRnmJwTmbaU_H_6kw42NmCnvl9xxTQG7Dn_gJkYsAzxD9EPCTAykOK5iaqbSpXTtB4KKIr5ZknbM80P5jqNnS1EBJ-NpW20TIzsAQ0LdlSBfkEsdd4jeAtgQanr9L33ZnUp_p60xPIp_uqj6x50tx4YXd7mZFGFfIWqg7P1duqZqnQ9sEHqWBJyAICRMB1OdE5GzZf4M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff3781c6b3.mp4?token=qfMdybgkOAlxDu3rwM3ootPFTCKSosjXk2DdcC2AJeYYCtRFj1JZhh-Ot61jGi4_W2juW8xlANbt6xY-dt0IQR8_nYVHAZgKWd7HRbnRHEHtMpqeUqKDOYjN-iRdvI7DKw_U9ysW8yadSTOjwcaizFh0Z2dG_YledU93XDpZ8nrh_fpzJ1vGDBP9trZ1Q9a1oOJUU2ZOvlNAc_EHUDJwTDIT21N5t7ucL-KdXKuhx3x0EYloEywwqV2_6saDNs-O2H8JBSreBOEcwF0uuSQ3lcz2xUDqFTiwFRUstKMNfLOXqP2qyjDTpR3F4Bk2HQjBhyxtGeVmOCPzqB1IfrBESla_3R5-ixpl4xqAlcPXJKURHFTw5NgPS0fZL7RJCGyiQkyUGlnypJXsaxNKzDXN-JRhOJi-MwX9c1L8u5VAfnNHtScjp-LCGSULYCVqAnVi2HlFm_LHv-Baa5qnGopUk2ZyHUo9SiySSNOvRnmJwTmbaU_H_6kw42NmCnvl9xxTQG7Dn_gJkYsAzxD9EPCTAykOK5iaqbSpXTtB4KKIr5ZknbM80P5jqNnS1EBJ-NpW20TIzsAQ0LdlSBfkEsdd4jeAtgQanr9L33ZnUp_p60xPIp_uqj6x50tx4YXd7mZFGFfIWqg7P1duqZqnQ9sEHqWBJyAICRMB1OdE5GzZf4M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ردبانک؛ نئوبانک هوشمند در الکامپ
🔹
ردبانک، در بیست‌ونهمین نمایشگاه الکامپ با تمرکز بر خدمات بانکی، سرمایه‌گذاری، هواداری و سبک زندگی حضور پیدا کرده است.
🔹
در غرفه ردبانک، هواداران پرسپولیس می‌توانند در کنار جام‌های قهرمانی و پیراهن امضاشده بازیکنان عکس بگیرند و با خدمات این نئوبانک آشنا شوند.
🔹
افتتاح حساب کاملاً آنلاین، طرح‌های متنوع بانکی، سرویس انتقال وجه «کارت به چند»، خدمات سرمایه‌گذاری «ردگلد» و «ردسیلور» و سرویس «سود پلاس» از جمله خدمات معرفی‌شده در این غرفه است.
🔹
یکی از بخش‌های جذاب غرفه نیز تجربه‌ای مبتنی بر هوش مصنوعی و بازی است؛ بازدیدکنندگان پس از پاسخ به چند سؤال شخصیتی و گرفتن عکس، وارد بازی می‌شوند و شانس دریافت جوایزی مانند طلا، سکه و وجه نقد یا تجربه‌هایی مانند عکس با جام و پیراهن پرسپولیس را دارند.
🔹
در پایان نیز تصویر آنها با هوش مصنوعی به یک کاراکتر اختصاصی تبدیل می‌شود.
📍
بیست‌ونهمین نمایشگاه الکامپ | غرفه ردبانک</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/686830" target="_blank">📅 11:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686829">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
وال استریت ژورنال: ترامپ در حال بررسی اعلام پایان جنگ با ایران است
🔹
مقامات آمریکایی به وال استریت ژورنال گفتند که ترامپ در حال مذاکرات خصوصی با دستیاران ارشد خود برای اعلام پایان جنگ با ایران است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/686829" target="_blank">📅 11:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686828">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c0f2cc431.mp4?token=Ay0BNfobEpFYqX8mqVHPuqo8Ru6WMiC5ltmwhUmY-vhGsI9GoRiK7hlMxmdWiJ_kBOoCXfDe4EgWjUTlrSz_VNC6fql0GbRMVzLBqmatyYm0gpu_EvwhVcTIba-NVuW0mZ7JuQyDce47sbexj6gJdBnSoo1oZSSDiecIYdXrVN558Byaii1iNP-trOLCJCabPo7B3a9mzXq0BwcE_h-co8dMBAYn4y3SBA2whAfrAe_WORbNFZSbkkdRuBNCziLbzgpBryaOn0ytKa4yjplVq0Ho9_Tu_EKfDgzvzfgvFAHRpeIct2C1v-klKTXMU__yIcGzIcnUMet4nL7e0-u6mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c0f2cc431.mp4?token=Ay0BNfobEpFYqX8mqVHPuqo8Ru6WMiC5ltmwhUmY-vhGsI9GoRiK7hlMxmdWiJ_kBOoCXfDe4EgWjUTlrSz_VNC6fql0GbRMVzLBqmatyYm0gpu_EvwhVcTIba-NVuW0mZ7JuQyDce47sbexj6gJdBnSoo1oZSSDiecIYdXrVN558Byaii1iNP-trOLCJCabPo7B3a9mzXq0BwcE_h-co8dMBAYn4y3SBA2whAfrAe_WORbNFZSbkkdRuBNCziLbzgpBryaOn0ytKa4yjplVq0Ho9_Tu_EKfDgzvzfgvFAHRpeIct2C1v-klKTXMU__yIcGzIcnUMet4nL7e0-u6mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرمانده نیروی زمینی ارتش: هرجا منافع ایران ایجاب کند با قدرت حضور خواهیم داشت
🔹
یگان‌های نیروی زمینی ارتش آمادۀ مقابله و مواجهه با هرگونه تهدید احتمالی در مناطق مرزی هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/686828" target="_blank">📅 11:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686827">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2240919c6.mp4?token=myRGF3WS4hE-YD0kK4wSoiRcO3l5Vm-aRvg8-zV-coKMnDsHpvy-46Jwd8I1-qy6mvZWJD5SYglxFfSwmUN-fWYLB4LR0-HmngvZhkdVhHTgkqsTKoNRcgQGgOsB2Cwe3qChl80GmnzBk8jgVmQK-KUepMOUg2OKUx8ONFytiKrrUvFsaorUc3VekwofajV2ACevpZieH0JZALckTGGMXu1g0lxaZWW6a_pRVZyR4aNE7Yrq6_Ppse7WoYsk7J5gOLU-V9wCyFBtBTCMpuO651ESA1YzerMIcmIFUndfcUQtrPxhxCf6xJz_u4FJQv0hdC-OP3fQfbk3Mw8ge3jBDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2240919c6.mp4?token=myRGF3WS4hE-YD0kK4wSoiRcO3l5Vm-aRvg8-zV-coKMnDsHpvy-46Jwd8I1-qy6mvZWJD5SYglxFfSwmUN-fWYLB4LR0-HmngvZhkdVhHTgkqsTKoNRcgQGgOsB2Cwe3qChl80GmnzBk8jgVmQK-KUepMOUg2OKUx8ONFytiKrrUvFsaorUc3VekwofajV2ACevpZieH0JZALckTGGMXu1g0lxaZWW6a_pRVZyR4aNE7Yrq6_Ppse7WoYsk7J5gOLU-V9wCyFBtBTCMpuO651ESA1YzerMIcmIFUndfcUQtrPxhxCf6xJz_u4FJQv0hdC-OP3fQfbk3Mw8ge3jBDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک وعده غذا میلیاردی!
🔹
در رستوران تاریخی «لا تور دارژان» پاریس، یک منوی مزه‌چشی با قیمت حدود ۳۸ هزار یورو برای هر نفر سرو می‌شود؛ جایی که قدمت، منظره نوتردام و تجربه لوکس، بخش بزرگی از هزینه را تشکیل می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/686827" target="_blank">📅 11:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686824">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siLgquU3Tj2VLh-NwAwRrpHllMamLcVWmNadywy8BwR6jBNivSxyPIS_ZiqfQJzmKqTb3C8QxkpxVyIKvAheg_ZRReBWtmQrCn17wCi88uQVyrcnSnFC_nDgH5T9mo-Vxokym4M5bLrK6k1UZq4Rfap2EoNbeZK2WiGYwFpxf0Vud66su8HVUqyCeoLfn_F_lOV77GxQj0KhPrEy0YyYu-jCKEHDePoA85F2jKD0O8nvhMkrgHTjVVwOZbOGHmBwreKdDl4lsVqruXQYcEdqE6FdPKzmZuP2SMlg9UfkMSrQej4x7vyNWIQLBx-0hDanmrgywgn1E17j2MW2qBVqKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76bc2db960.mp4?token=iYPz32Rm2NECfMn9okdI8GCrTPd1jQHSsGhKAXWRKJHZ56vjVYMVbM7tQiuTsmR2nstf6rbhDY-zO1zjBB9mWKiXN76WimCMAKNAKFswf39iU0NOuAGUJhNcbHVINSqmi7i9MErwM-wKtFEa4iZDAXcvrIfmTvv9KFEDiYSxUPZahXF7ihkU3osAZx1T5jOZmVD8WJSWq1720uzH6nVGe5M_tV5U4-YzowMUY3C81FEsU9sdFU8ym5fmy-WFKPIEWNEwcQ4UaK99JJ5FOfQx3PYmWPlBUlCSPzVYYGsR5u5GiRiRxv0g8evjz5Gz9GHTS3qw5wx5wiaF77vshdfWCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76bc2db960.mp4?token=iYPz32Rm2NECfMn9okdI8GCrTPd1jQHSsGhKAXWRKJHZ56vjVYMVbM7tQiuTsmR2nstf6rbhDY-zO1zjBB9mWKiXN76WimCMAKNAKFswf39iU0NOuAGUJhNcbHVINSqmi7i9MErwM-wKtFEa4iZDAXcvrIfmTvv9KFEDiYSxUPZahXF7ihkU3osAZx1T5jOZmVD8WJSWq1720uzH6nVGe5M_tV5U4-YzowMUY3C81FEsU9sdFU8ym5fmy-WFKPIEWNEwcQ4UaK99JJ5FOfQx3PYmWPlBUlCSPzVYYGsR5u5GiRiRxv0g8evjz5Gz9GHTS3qw5wx5wiaF77vshdfWCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اصابت پهپاد انتحاری شاهد به بالن جاسوسی آمریکا در اربیل عراق
🔹
این اصابت مربوط به شب‌های گذشته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/686824" target="_blank">📅 11:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686823">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
انتصاب فرمانده جدید ارتش اسرائیل در بحبوحه تشدید تنش‌ها در کرانه باختری
جروزالم پست:
🔹
ارتش رژیم صهیونیستی «دیوید بار خلیفه» را به عنوان فرمانده جدید فرماندهی مرکزی منصوب کرد و او احتمالا از سال ۲۰۲۷ این مسئولیت را بر عهده خواهد گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/686823" target="_blank">📅 11:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686822">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
دادستانی تهران علیه عوامل «دیدارنیوز» به‌دلیل انتشار محتوای توهین‌آمیز و کذب اعلام جرم کرد.
🔹
ترامپ با رئیس امارات درباره روابط دوجانبه و تحولات خاورمیانه گفت‌وگوی تلفنی کردند.
🔹
روسیه: دو کشتی اوکراینی را در دریای سیاه هدف قرار دادیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/686822" target="_blank">📅 11:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686819">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fMV-UPmgRGVEWi_jgsrylHADxe472k-KQUDAvP4Pvogb2PuoNs91t5r3BB6O-lHo0jUOK673StZNK8WkQUacMAYTJLKWONgCR0DxPUykJtfibW9V410281tUJ_Z-WOPidZJxl-Aa0jbm-CSQ5GF4V27Ov0a7ieDHsS2xMhypp7bIbG-uPbdGztH4nQ9_3OZdvxSbo6kxpTNDdd-8qmPFwE7XJkKhU51fu67D8rwobCUgWHAkhBHNr36WQ_WZpji_WhFe8gu6-STDPyc-CQtbXndxGC6cDwRRwO409bIL4V5QjwV12VzBF8NTWVvfpkCQYh9mTTJ2DHY-FTY2sGsLKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O--GOsXjvOlOES16k6_xFFk0RfWJK9QrouWCfQr2_P7NVrRGdI5WCFfg3VM3Uw8nRYEjvPm0y9MY_Qnz0U3mMBV94Cm8P9auNWdRhYmXdlKoc__qodaNGGERP42vYpGNpUHOKXViv_GUn8RlB_nOc-C9l8S9Vtu6b4a5osuMLj_VTV8_m9SirBjeDSoIp19nENhL9U7asqoxwRknADEEG9Pm0mRaogCRv1EbZUH-0ACmqLf7kZDRzcpVxQhGV5-0IIrYyynaOG0k_6J668oh0N8PdeOl3e95IhjBZjcv3KXiAS4amtUFo9GrXMjGxDc8Rt5HUYoKRlId409Kd3qQkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FkVbh-Zo-Ps1_5VHq0kiIV-ezJWxxCIMHNkaQprCtUQeYL5u1oXJzAine8-yamNKCtvl2JR5yFzHKat7moY_pWLIg9VjaIoP0K8v-cZ92AetDuOkHpm9bOMomd6rRNVf8IVtR-NstwzABnoepaxIkPXBMKxH5z3tecOhEvCVpc8Fsj_g96-xn05ajDkbWfooqSYjWkOqpav0JwHqhxw2_RGKKUKcsDGPmMzEUtwREgttCD-IwSaea0IIyEv1xrm9Jm9prZ_fw4BMVqIYW1I5k0NJQMFF_Khsq5B2g9LnuZ3E3QR6QyHs89gzIuBfDzNAdFEDPrGL0bieFs9eRcbPxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بازدید معاون اول رئیس‌جمهور از غرفه بانک صادرات ایران در نمایشگاه الکامپ
🔹
دکتر محمدرضا عارف، معاون اول رئیس‌جمهور، در جریان بازدید از بیست‌ونهمین نمایشگاه بین‌المللی الکامپ، در غرفه بانک صادرات ایران حضور یافت و مورد استقبال دکتر خانی، مدیرعامل این بانک قرار گرفت.
🔹
در جریان این بازدید، آخرین دستاوردهای بانک صادرات ایران و شرکت‌های تابعه در زمینه تحول دیجیتال، کاربردهای هوش مصنوعی در خدمات بانکی، پلتفرم‌های نوین مالی و اقدامات صورت‌گرفته در حوزه امنیت سایبری تشریح شد.
🔹
دکتر عارف ضمن آشنایی با تازه‌ترین سامانه‌ها و محصولات فناورانه بانک صادرات ایران، بر نقش کلیدی فناوری‌های نوین و بانکداری هوشمند در تسهیل خدمت‌رسانی به آحاد جامعه و توسعه اقتصاد دیجیتال کشور تأکید کرد.
بانک صادرات ایران، در خدمت مردم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/686819" target="_blank">📅 11:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686817">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1zInLQB5VAQPf-L3ra7KMzTWt9pWqgKPCHhWzdZ4AtJB-8ebgSSPeC2ZTKSequPWYmmbVBFCCt3lr6pczpnOvnS0juefhlvv_SEvMnqmuJIvoRwaRNBAJxa9zvQFcaG676gGS4gMdHekwR1fZpqTbVLC-QaBGnRP9HGmcvzdQ0OjCaJuTYQ2IKBUbzahHudUjhn4cQVnEC5G-8jHn8fChzeq0wjCqiL6m7EWhzKaO85I2s-eR7ii0U5cGbUNdjb1AA_OSL6RJtJCNtaytGuQ_mv5ptg8OZjV4fx8YbL8Lx26HKeC0CELUnk8aOx1Htw5beYMj5I3up0q-7v5Hg14Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران عزادار فرزندانش است
🔹
خبرفوری شهادت ۴ رزمنده نیروی هوا و فضای سپاه و ۳ رزمنده بسیجی در پی حمله آمریکا به استان کرمانشاه و جزیره لاوان را به هم‌وطنان عزیز تسلیت می‌گوید.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/686817" target="_blank">📅 11:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686816">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مجوز پلتفرم‌های طلا پس از یک‌سال‌ونیم توقف فعال شد/ صدور مجوز و تنظیم‌گری رمزارزها به‌زودی عملیاتی می‌شود
هادی محضرنیا، رئیس مرکز ملی پایش و بهبود محیط کسب‌وکار در حاشیه مراسم الکامپ در
#گفتگو
با خبرفوری:
🔹
هدف ما شفاف‌کردن فرایندهاست تا مردم بدانند در چه حوزه‌هایی حمایت وجود دارد و در چه حوزه‌هایی باید با آگاهی و مسئولیت خود تصمیم بگیرند.
🔹
برای نخستین‌بار مجوز پلتفرم‌های تخصصی معاملات خودرو و املاک صادر شده تا کارشناسی، استعلام، ثبت قرارداد و تبادل مالی در بستری امن و رقابتی انجام شود. همچنین تلاش کرده‌ایم با حذف تصدی‌گری دستگاه‌ها، مسیر فعالیت شفاف پلتفرم‌ها و ورود بازیگران جدید به بازار را هموار کنیم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/686816" target="_blank">📅 11:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686815">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0d16fae91.mp4?token=oypuN6rHVq2YNHoFGMjwjqPR-ZYqNV4BFqE8LVAZQjubbJFYzNChudywZ12rPGcnGpR1o3xuY36BQIwAL7IZSgn6rnxgPl05FTCkDRNzGreMReIRPj7F4m_yAdnzpH6bjsaSGSO439RAHhu065cyyES9ogpYnxWz01_4Saf1graAV7EDBEYuEumyMZiBTXgBRu7SGHEVklYOXxN-DFJR4XEZfias0HXgsBGYG0PBktLinom_J1asZez6dcVmsZmWJuZGAcdFXY_jC6hYDavCV_B9Wv1wIS5TtcnrtnlR3Qz8revaLrFjuP4UvAZGxNpizVGQhnADa1SPiOWF8VvaSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0d16fae91.mp4?token=oypuN6rHVq2YNHoFGMjwjqPR-ZYqNV4BFqE8LVAZQjubbJFYzNChudywZ12rPGcnGpR1o3xuY36BQIwAL7IZSgn6rnxgPl05FTCkDRNzGreMReIRPj7F4m_yAdnzpH6bjsaSGSO439RAHhu065cyyES9ogpYnxWz01_4Saf1graAV7EDBEYuEumyMZiBTXgBRu7SGHEVklYOXxN-DFJR4XEZfias0HXgsBGYG0PBktLinom_J1asZez6dcVmsZmWJuZGAcdFXY_jC6hYDavCV_B9Wv1wIS5TtcnrtnlR3Qz8revaLrFjuP4UvAZGxNpizVGQhnADa1SPiOWF8VvaSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هوادار عجیب استقلال
😂
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/686815" target="_blank">📅 11:00 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686814">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
دلار نفتیِ شهریور، وارد کشور شد
🔹
براساس اسناد رویت شده، از اول شهریور تا دیروز، بیش از یک میلیارد دلار نفتی به ذخایر ارزی کشور اضافه شد.
🔹
پیشتر در ۵ ‌ماهۀ اول سال هم رقم فروش نفت کشور، بیش از ۸۰ درصد درآمد بودجۀ سال ۱۴۰۵ را پوشش داده بود.
🔹
ارز نفتی تزریق شده در شهریور‌ماه با پر کردن دست بانک مرکزی امکان تامین نیازهای کشور را فراهم خواهد کرد./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/686814" target="_blank">📅 10:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686813">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
اعتراف شبکۀ اسرائیلی به پیوند گروه‌های تجزیه‌طلب با آمریکا و اسرائیل
شبکۀ ۱۳ اسرائیل:
🔹
موساد پیش از آغاز جنگ، طرحی با هدف براندازی جمهوری اسلامی طراحی کرده بود که یکی از محورهای آن، آموزش هزاران نیروی مسلح تجزیه طلب در سرزمین‌های اشغالی و آماده‌سازی آنها برای ورود به خاک ایران بود.
🔹
این طرح سه روز پس از آغاز جنگ و در پی پیامی از سوی آمریکا متوقف شد و طرح جایگزین برای تغییر رئیس وقت موساد نیز به نتیجه نرسید. گزارش‌های دیگری نیز از رسانه‌های اسرائیلی و ایرانی، جزئیاتی مشابه درباره این طرح منتشر کرده‌اند.
🔹
این موضوع در حالی مطرح می‌شود که دونالد ترامپ، رئیس‌جمهور آمریکا، نیز پیش‌تر گفته بود واشنگتن در مقطعی تلاش کرده است به اغتشاشگران از طریق گروهک‌های تجزیه‌طلب کرد، سلاح برساند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/686813" target="_blank">📅 10:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686812">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/739e9f635b.mp4?token=VbstLVeAl5JKVRzZRak9EzBjHPMb9V4p58-V8QbekG-Ckip5kREaDfpqv8nXnG_V5rMv4FqxV24Qs21N16AncltQJ6Oie-_eMpDluUwQMLenYyS9wAWmGwGH0wPG8j1LpBwntq0dEYn30cZy7PHiSeHoaDdU9nVERrXDdamKONYL-hiLpAn0FyzVXzzU_zCEVcO8cuFX3Y-DQATFPlAQFV0Dv5k3Gp1pVCUVWKaPj5OpZbDNO_ieIDijfu9XBRKmKhdz8HegusPNxs10b7Fb4J1SFyUYT0fIIBO-Wqs-ogKJ_z28YImtSqNlmm-mDgJKG6TfvkIhoWJL2EExZc5MmxFPBD23tTpfxlIToBYhwS7eF9c0NpkwDArvx_nbwNJkG_12uDJXVvzwSKVrGCVt3gH2ta_0kJeOTZRem2VnRFeS5Nip-EfQgInulFRnQXu9pyz8sp68LwI7DQM8ShpciuRme9L22Pojk6YNMHNzD4-inLcKuCTN6F7RXEcPtoNukWgncIdd_MDlJFQr84eIpvgqz4x_8WhVyvdQ7bkW57QizTR7eFB17a00blyyU5es81W4zBnNkBtoCBmSNqSBNeaepy29aZONf7R1shUaRKuo1OYVUYyzHEiPZbef3WmSkP9HIWELUyqIk4EBzwUrmrnhBgemxCf3q2mEQiLlOrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/739e9f635b.mp4?token=VbstLVeAl5JKVRzZRak9EzBjHPMb9V4p58-V8QbekG-Ckip5kREaDfpqv8nXnG_V5rMv4FqxV24Qs21N16AncltQJ6Oie-_eMpDluUwQMLenYyS9wAWmGwGH0wPG8j1LpBwntq0dEYn30cZy7PHiSeHoaDdU9nVERrXDdamKONYL-hiLpAn0FyzVXzzU_zCEVcO8cuFX3Y-DQATFPlAQFV0Dv5k3Gp1pVCUVWKaPj5OpZbDNO_ieIDijfu9XBRKmKhdz8HegusPNxs10b7Fb4J1SFyUYT0fIIBO-Wqs-ogKJ_z28YImtSqNlmm-mDgJKG6TfvkIhoWJL2EExZc5MmxFPBD23tTpfxlIToBYhwS7eF9c0NpkwDArvx_nbwNJkG_12uDJXVvzwSKVrGCVt3gH2ta_0kJeOTZRem2VnRFeS5Nip-EfQgInulFRnQXu9pyz8sp68LwI7DQM8ShpciuRme9L22Pojk6YNMHNzD4-inLcKuCTN6F7RXEcPtoNukWgncIdd_MDlJFQr84eIpvgqz4x_8WhVyvdQ7bkW57QizTR7eFB17a00blyyU5es81W4zBnNkBtoCBmSNqSBNeaepy29aZONf7R1shUaRKuo1OYVUYyzHEiPZbef3WmSkP9HIWELUyqIk4EBzwUrmrnhBgemxCf3q2mEQiLlOrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محدودیت ارتباط(تجاری) ما با امارات به خاطر بحث جنگ وجود دارد
هوشنگ هادیان پور، سخنگوی کمیسیون کشاورزی مجلس در
#گفتگو
با خبرفوری:
🔹
در زمینه امنیت غذایی اصلا مشکلی نداریم.
🔹
طی جلسه ای، معاون بازرگانی وزارت جهاد کشاورزی اشاره کردند که محدودیت ثبت سفارش و محدودیت سلیقه‌ها را برداشته‌ایم. در واقع، فرایند تجاری آزاد را سهل الوصول کرده‌اند.
🔹
از همه کشورهایی که از قدیم ارتباط تجاری داشتیم، در حال حاضر واردات و صادرات وجود دارد؛ مگر کشورهایی که از قدیم دشمنی داشتیم.
🔹
محدودیت ارتباط تجاری ما با امارات به خاطر بحث جنگ وجود دارد، اما قطعا اگر این جنگ به پایان برسد ما با امارات نیز مشکل خاصی در بحث صادرات و واردات نداشته‌ایم و نخواهیم داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/686812" target="_blank">📅 10:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686811">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pH5qt2e5tBgx862xBxJ0u-W6YmVEuSczQwd_Y2t1uWQqHMFKyYVUsey43_Sf9vEAIxM6cr5AL6mhRgyrpqBk9UfIAXdDfItBfMfmzt_6Ox6HDB_v4fG-qZQnjHy3MsCcMCpsAApDe9VMqVT776j3nPESI5FTEDgBVS3CzudaRTMpPfKtIIdgHoLl20UDnp-yDP2QDLWUSK_yYcyB1PXkfoauy5fJT6f94g6z_YbYVhsyoD5IVt1bOzcoLnsdurLGRRSdeIOSvCmupz0vaDqJ2N6ytQjYoroUAQrVBSaPllDuh2v37Jrd2_JjvEQCpHhNHpu95fghQFrJoOxEkP2j1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دلقکی به نام ترامپ و سیرکی به نام کاخ سفید
🔹
کاخ سفید پس از شکست‌های پیاپی و ذلیلانه در برابر ایران، نقشه تنگه هرمز را منتشر کرده و اسم تنگه هرمز را به «تنگه ترامپ» تغییر داده؛ عکس ترامپ نیز وسط تنگه است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/686811" target="_blank">📅 10:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686810">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
روزنامه هیل: استیضاح ترامپ اجتناب‌ناپذیر است
🔹
ناامیدی در میان جمهوری‌خواهان افزایش یافته و احتمال از دست رفتن اکثریت شکننده حزب در مجلس نمایندگان مطرح شده است.
🔹
برخی دموکرات‌ها نیز معتقدند به‌جای آغاز یک استیضاح ناموفق دیگر، باید از اکثریت جدید برای تمرکز بر مسائل مهم مردم آمریکا استفاده کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/686810" target="_blank">📅 10:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686809">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3c76d5528.mp4?token=PRqrOr1Bczf-cA5Hxh50quoP4YEtguLzNJ0OplfNsyLSLY12A_cHfj4T_0HWDohkq52-J1mAoN6mlPr9Xbx7eFn3LHPe9EBWlbYLwcStgeIGmc5UFEQt8VIXIZj0ZM4bYWrGPjBwmoV9xHogFfXenIUGXU5dhLgzT8TVv0bO4L9P03JQB2PAVfxdjpxzQ1j0buuBymNohT2ZHo2O-PKR6lmGENAZEQOxp9BNpb9oWrTniIP80XPlHq7eQkO945KoVUr4sog2kR8cO0-WgX1WRIGQ1nUxco2aERKDEWiI6SyssiBJQ7f1hcUB6WzFazhuhfAPQwUIjCjtY0KZ4z_0642E0iA9GCLaCV-IrZGctkvMr4cqw_EQq35_iZZCm80WmfsoaYajc42hLkx98KiKPKLrZrppTd50YJ_j9YVRSCB2J8iPQ7IGh8bh82-qpdQ1XfeuzEX0O8D_bmMQXF_RjNjaowmuh9E5lIF7IKfsnCjVFbXAJBqQCjZHf_khHVKl_kkkDvXZlSD053LAD1wd6t_7hqwt2tNzR8BQp5Cf2Adq7OW81JHFnnncch2ybtL9ftIVNpYHalL2QScd5QuR7cZBCa14jIYPM08sZUMC55270OZljUdxcArgyMH2iTaM2JaBaUE7lVNIaFl-dF_hFmGqtjJz5GTr7WxbDfM10hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3c76d5528.mp4?token=PRqrOr1Bczf-cA5Hxh50quoP4YEtguLzNJ0OplfNsyLSLY12A_cHfj4T_0HWDohkq52-J1mAoN6mlPr9Xbx7eFn3LHPe9EBWlbYLwcStgeIGmc5UFEQt8VIXIZj0ZM4bYWrGPjBwmoV9xHogFfXenIUGXU5dhLgzT8TVv0bO4L9P03JQB2PAVfxdjpxzQ1j0buuBymNohT2ZHo2O-PKR6lmGENAZEQOxp9BNpb9oWrTniIP80XPlHq7eQkO945KoVUr4sog2kR8cO0-WgX1WRIGQ1nUxco2aERKDEWiI6SyssiBJQ7f1hcUB6WzFazhuhfAPQwUIjCjtY0KZ4z_0642E0iA9GCLaCV-IrZGctkvMr4cqw_EQq35_iZZCm80WmfsoaYajc42hLkx98KiKPKLrZrppTd50YJ_j9YVRSCB2J8iPQ7IGh8bh82-qpdQ1XfeuzEX0O8D_bmMQXF_RjNjaowmuh9E5lIF7IKfsnCjVFbXAJBqQCjZHf_khHVKl_kkkDvXZlSD053LAD1wd6t_7hqwt2tNzR8BQp5Cf2Adq7OW81JHFnnncch2ybtL9ftIVNpYHalL2QScd5QuR7cZBCa14jIYPM08sZUMC55270OZljUdxcArgyMH2iTaM2JaBaUE7lVNIaFl-dF_hFmGqtjJz5GTr7WxbDfM10hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خداحافظ کار یدی؟ آینده بشریت در کارخانه‌ها شاید این شکلی باشد!
🤖
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/686809" target="_blank">📅 10:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686808">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
واکنش سازمان ملل به حمله آمریکا به مراسم عروسی در سیریک ایران  سخنگوی دبیرکل سازمان ملل:
🔹
دبیرکل سازمان ملل عمیقا از گزارش‌های مربوط به تلفات غیرنظامیان از جمله حمله‌ای که گفته می‌شود به یک مراسم عروسی در ایران اصابت کرده، نگران است و خواستار توقف فوری خصومت‌ها…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/686808" target="_blank">📅 10:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686807">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
سپاه: سران آمریکا راجع به پروندۀ سیاه حمله‌های خود به عروسی‌ها در کشورهای مختلف به افکار عمومی جهان پاسخ دهند
روابط عمومی سپاه پاسداران:
🔹
نیروهای تروریست آمریکایی نزدیک به ۷۰ نفر را مورد اصابت قرار دادند که ۴ نفر از آنان شهید شدند و حال ۷ نفر از زخمی ها وخیم گزارش شده است.
🔹
امروز برای ملتهای جهان احراز شده که حمله به غیر نظامیان برای ایجاد رعب و وحشت بخشی از دکترین ارتش ناجوانمرد آمریکاست:
🔹
۲۰۰۲ اول ژوئیه: بیش از ۱۰۰ شهید در بمباران عروسی روستای کاکرک ولایت ارزگان افغانستان
🔹
۲۰۰۳ هجدهم سپتامبر: بیش از ۵ کشته و مجروح بمباران عروسی شهر فلوجه عراق
🔹
۲۰۰۴ نونزده مه: ۴۲ شهید در بمباران عروسی روستای بکر الذیب استان انبار عراق
🔹
۲۰۰۴ هشتم اکتبر: ۱۳ شهید از جمله داماد در بمباران عروسی شهر فلوجه عراق
🔹
۲۰۰۸ ششم ژوئیه: ۴۷ شهید از جمله عروس در بمباران عروسی ده بالا ننگرهار افغانستان
🔹
۲۰۰۸ نوامبر: ۳۷ شهید از جمله ۲۳ کودک در بمباران عروسی وج بغتو قندهار افغانستان
🔹
۲۰۱۲ ژوئن: ۱۸ شهید از جمله ۹ کودک در بمباران عروسی لوگر افغانستان
🔹
۲۰۱۵ بیست و هشت سپتامبر: ۱۳۱ شهید زن و کودک در بمباران عروسی وحجه تعز یمن (ائتلاف تحت حمایت آمریکا)
🔹
۲۰۲۶ اول سپتامبر: ۷۰ شهید و مجروح در بمباران عروسی کوهستک سیریک هرمزگان ایران
🔹
سران آمریکا که بجای عذرخواهی باز هم به دروغ متوسل شده اند و همانند پرونده جنایت میناب، لامرد و قشم از پاسخگویی طفره میروند، خوبست راجع به پرونده سیاه حمله های خود به عروسی ها در کشورهای مختلف هم به افکار عمومی جهان پاسخ دهند. آیا همه این حوادث اتفاقی و به اشتباه بوده است؟
🔹
ما که قدرت نظامی داریم و همان دیشب با به هلاکت رساندن تروریستهای خونخوار سنتکام قصاص کردیم. ملت آمریکا اگر جلوی این ارتش وحشی کودک کش را نگیرند، باید از روزی بترسند که روز انتقام مظلومان فرابرسد که "یوم المظلوم علی الظالم اشد من یوم الظالم علی المظلوم"
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/686807" target="_blank">📅 10:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686806">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea1bc08ee3.mp4?token=C8k6gt4Mi_ZUEKgqhNZBmhn4MiHJs4ux5wU1z306rHz2TLAHOz4UqZXsY0suiTRFfxSml4hk0pes0DDynwtEBqEYOOLM1oHwtNKtV2876HNYJR3RdT5NcK-CQCKU2sEyTCF4okrQ6_IMe78uDwESyJrISL7ArA7J9pdGb9BB4hVYiAAIW3dbbwjDTk9mt6fSmnYKkZb8abLgXiB5urySDdZiE3jengTbPcZ8K6t-1Jrdp5_lLsiUrfNHRre5JFnKiAvagmkvUrelbLBfd5JfUaN6peAVIRyWhN0HI3Bd045pCZcSjO6MMT1aZFHywrbHXBV3qmFxIQ6Pi53yIIGx0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea1bc08ee3.mp4?token=C8k6gt4Mi_ZUEKgqhNZBmhn4MiHJs4ux5wU1z306rHz2TLAHOz4UqZXsY0suiTRFfxSml4hk0pes0DDynwtEBqEYOOLM1oHwtNKtV2876HNYJR3RdT5NcK-CQCKU2sEyTCF4okrQ6_IMe78uDwESyJrISL7ArA7J9pdGb9BB4hVYiAAIW3dbbwjDTk9mt6fSmnYKkZb8abLgXiB5urySDdZiE3jengTbPcZ8K6t-1Jrdp5_lLsiUrfNHRre5JFnKiAvagmkvUrelbLBfd5JfUaN6peAVIRyWhN0HI3Bd045pCZcSjO6MMT1aZFHywrbHXBV3qmFxIQ6Pi53yIIGx0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چیکن استراگانوف خامه‌ای و خوشمزه
😋
مواد لازم:
🔹
سینه مرغ: ۲ عدد
🔹
قارچ: ۳۰۰ گرم
🔹
پیاز: ۱ عدد
🔹
خامه: ۲۰۰ گرم
🔹
شیر: ۱ لیوان
🔹
آرد: ۱ قاشق غذاخوری
🔹
کره: ۳۰ گرم
🔹
نمک، فلفل سیاه و پاپریکا: به مقدار لازم
🔹
سیر: ۱ حبه (اختیاری)
🔹
پنیر پارمزان: ۱ قاشق غذاخوری (اختیاری)…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/686806" target="_blank">📅 10:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686805">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">در
#الکامپ۱۴۰۵
جای خالی هیچکس احساس نشد. فعالان واقعی
#اکوسیستم
فناوری اطلاعات و ارتباطات ، روزهای پر رونقی را رقم زدند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/686805" target="_blank">📅 10:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686804">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
رویترز: تنها ۶ کشتی چهارشنبه از تنگه هرمز عبور کردند
🔹
طبق داده‌های کپلر، این رقم نسبت به ۱۱ کشتی در روز سه‌شنبه کاهش یافته و بسیار پایین‌تر از میانگین ۱۰ روزه، یعنی حدود ۱۳ کشتی در روز است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/686804" target="_blank">📅 09:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686803">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a6004af77.mp4?token=LiFYNiT5SYIGzr1jjtLgsGzzvIMWHBZwJOOdSpmQEGiCqlwN75B90H9JjnJE1sT8qlbIN4WT5UQ7-13mxd-U8qREGg98m15dB17lHRr7W6D4yIshuktUYUYNUMq7EQte2RpQuE78SsMAlHsLxYZafq9box4qwmzuZ4tdCk6W72ADgi5MG5MCY9k1BkjpqN2nrS6YsG8NpzDw0eg7BeWY2uIjBXiiWORX7sXDAGh0Vwqhp4W2JbpLG_X_kBZ56Rx4YluYKBGiP-lNpJWKPTlLyHD0UJHh7lkNnF2WHOJFrs0335SxYeHY_r7lmXc572XqfQtzmeZ2ho8rfs8seGsItA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a6004af77.mp4?token=LiFYNiT5SYIGzr1jjtLgsGzzvIMWHBZwJOOdSpmQEGiCqlwN75B90H9JjnJE1sT8qlbIN4WT5UQ7-13mxd-U8qREGg98m15dB17lHRr7W6D4yIshuktUYUYNUMq7EQte2RpQuE78SsMAlHsLxYZafq9box4qwmzuZ4tdCk6W72ADgi5MG5MCY9k1BkjpqN2nrS6YsG8NpzDw0eg7BeWY2uIjBXiiWORX7sXDAGh0Vwqhp4W2JbpLG_X_kBZ56Rx4YluYKBGiP-lNpJWKPTlLyHD0UJHh7lkNnF2WHOJFrs0335SxYeHY_r7lmXc572XqfQtzmeZ2ho8rfs8seGsItA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جستجوی آب؛ رنج روزانه‌ای در غزه که پیر و جوان نمی‌شناسد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/686803" target="_blank">📅 09:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686802">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
جهاد کشاورزی: ثبت سفارش واردات حبوبات از امروز ۱۲ شهریور ۱۴۰۵ آغاز شد.
🔹
لاوروف: ناتو در پی استقرار زیرساخت‌های خود در آسیا است.
🔹
تلفات سیل نپال و چین به ۱۲۴۳ کشته رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/686802" target="_blank">📅 09:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686801">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بروکراسی علیه اقتصاد دیجیتال/ در بسیاری از موارد مشخص نیست متولی تنظیم‌گری کیست
هادی محضرنیا، رئیس مرکز ملی پایش و بهبود محیط کسب‌وکار در حاشیه مراسم الکامپ در
#گفتگو
با خبرفوری:
🔹
بروکراسی، امضاهای طلایی و فرایندهای غیرشفاف در سال‌های اخیر در بسیاری از کسب‌وکارها کاهش یافته، اما اقتصاد دیجیتال و کسب‌وکارهای پلتفرمی همچنان با چالش‌های جدی مواجه‌اند.
🔹
پیش از اصلاح فرایندها، باید مشخص شود متولی تنظیم‌گری هر پلتفرم کدام نهاد است و اساساً تنظیم‌گری از تصدی‌گری تفکیک شود؛ چراکه گاهی تنظیم‌گر به‌جای تعیین قواعد، در لایه‌های داخلی کسب‌وکارها ورود می‌کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/686801" target="_blank">📅 09:37 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686799">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XeLfBmoplD60FQiXnZOnRgz22LoVoxumy6y6tNDzLqFrsEMAvQd3j4UTLWI6R3TTv13PzJCeSCOTfwdKfhR7sanWh6oSgfhXtUYC2QwIKUgXkfVLGNCzUfEBoOfUWKkzRAIdsgyedItVLLHBi85j576gc7YDZ0HbgkEOJXILetEOna17PgTuXvMuxifp04EPMxEsSD6XGWBpFpILf5UQry-beOO6t9mZHNDNnzVd1fhGtZCJKfj2RyolB9whXMkFg_8PJn9gQS6md8wfsTZXuSAdBZb2kO47sl08gGBCU1oSnin6VRMVNbIKuVy3731CZsyEZ7ytF55N40iNqLgscg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SK2WeOiGFRS9vATZ_zsq179SrIjSLVp6yQu_Pgk6Zuzq1StKR9H0YOvCTDOCVEBN0tpTkYdB9WElHjxWI8Y5ucqxmFNaYg8x2dUbRm_xPJZgfH0HdcCW4QsO1I4zH0BJgwc57GRSbLYSKrststFQwRoFBFk1qW7zBAoIVV-6utX-r5fVj2CMdJj8oHUGjEZKFTTKy-gDomWm97KbNkLCkdRax9s4ZjQtXAmd-p_du9l1FAwv6JU_J7yJRUa5sc7C8Z7Ihm5TBSz1xp3sUhQaZoIlRNQFnm9mpr5GtwPwqyQAdiQ7AC7pO8SVVbkN6xN_1JXQpt6AH0Sg2M7UfEXhxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
منابع عربی: یک نقطه مهم در یکی از پایگاه‌های آمریکایی در کویت مورد اصابت قرار گرفته و ستون‌های دود از آن برخاسته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/686799" target="_blank">📅 09:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686797">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
لیونل مسی از بازی‌های ملی خداحافظی کرد
🔹
لیونل مسی با انتشار پستی از فوتبال ملی از تیم ملی آرژانتین خداحافظی کرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/686797" target="_blank">📅 09:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686796">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
جهانگیر: رأی مصادره اموال ساعدی‌نیا به دیوان عالی کشور ارسال شد  سخنگوی قوه قضائیه:
🔹
رأی مصادره تمام اموال منقول و غیرمنقول ساعدی‌نیا برای فرجام‌خواهی به دیوان عالی کشور ارسال شده است.
🔹
همچنین شایعه رفع پلمب کافه‌های متعلق به او تکذیب شد و وی تا اعلام نظر…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/686796" target="_blank">📅 09:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686795">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
بلوکه کردن بخشی از تسهیلات اعطایی به عنوان ضمانت ممنوع است
بانک مرکزی:
🔹
با رای هیأت عمومی دیوان عدالت اداری، بلوکه کردن تسهیلات اعطایی توسط بانک‌ها و مؤسسات اعتباری غیربانکی و یا اجبار و الزام تسهیلات گیرنده به افتتاح حساب نقدی و توثیق آن و سپس پرداخت تسهیلات، ممنوع است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/686795" target="_blank">📅 09:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686794">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
تغییر زمان دو مسابقه هفته ششم لیگ ‌برتر به خاطر تیم امید
/
هفته هفتم  لغو نشد
🔹
با توجه به اعزام تیم امید ایران به بازی‌های آسیایی زمان دو مسابقه از هفته ششم لیگ برتر به شرح زیر تغییر کرد:
دوشنبه ۱۶ شهریور
مس شهربابک - ملوان بندرانزلی ساعت ۱۸:۴۵
فولاد خوزستان - فجرشهید سپاسی ساعت۲۰
🔹
پیش از این قرار بود این دو مسابقه روز سه شنبه ۱۷ شهریور برگزار شود که تیم امید در این روز عازم بازی های آسیایی است.
🔹
دیدارهای هفته هفتم لیگ برتر نیز طبق برنامه اعلامی برگزار می شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/686794" target="_blank">📅 09:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686793">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQb32FcZsYu4jeBHpAOjbNppDoAEK5usnMHsp-Etb-hLPdjuWtthMGdPrKGyjQBc2Y638MU2Y6_Ij83YFvTUU2yJARhmmydGKZDkj1KstdV3A4oamTq_ENd7CHKxz6Ku0409bEjhzupCk_Wmhz4AA2tgby56ci4qmCSD-f7lAIWl7ktuKNOI5PoxA8lpJ1FtuIVUrFkYIUoAl7GJoqzX6tbmvBnA5MiiDOjltHZLj6erfLZatjjO704Rd-lxth8Nd0wNi7_sPUQAWPYA41auV0LfMgwFPaKCCnDg4H9QUBm0MfstSp7kpTcQ2ODjkoDfQ5sF8qmZY8C966hqrlxRyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کریستیان تریبرت، خبرنگار بخش تحقیقات تصویری روزنامه «نیویورک تایمز»: بقایای تسلیحاتی که گفته می‌شود از حمله به یک مراسم عروسی در کوهستک، ایران، به دست آمده‌اند، به‌عنوان قطعات مربوط به موشک SLAM-ER شناسایی شده‌اند. شرکت بوئینگ، سازنده این موشک کروز، آن را…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/686793" target="_blank">📅 09:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686792">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
ادعای اکسیوس به نقل از منابع: ویتکاف آخر هفته گذشته با مشاور امنیت ملی امارات دیدار کرد/ درباره گام‌های بعدی در قبال ایران ایده‌پردازی و رایزنی کردند
🔹
طی همان روز، واشنگتن دسترسی شعب اماراتی «بانک مصر» به نظام مالی آمریکا را به دلیل تجارت با تهران، قطع کرد
🔹
وزیر خزانه‌داری آمریکا هم پیش از اعلام تحریم‌های جدید علیه ایران، با طحنون گفت‌و‌گو کرده بود./ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/686792" target="_blank">📅 08:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686791">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcc75ff65f.mp4?token=sjb_k8tuIzy5T5_DzpumO9XtcJGWpIJbitKwfzj2vaB-8OzXIzhbBpcTfbpXczpw76EsXdsgbexZTCfx2EyfmwEIeQ6GikkBa7byFw6L8_NpwSud88YfRjynoHBxHGSBCRlVc3mOVPn9YVgpQFNLIatMzu0xh9KRXm02ihcO-nuPdsu_EonZqWbwVonbA1-WpVgEZtowRTvIgaBX8q7sfXGYsYev9rkfeicojts4xKZJTPoQzjgE02A4QeaSmnI0J7A7KQRBD2fIQBi9WBPdbI9EjasQ5N7rKRV2CBbDgyZ0cywhuz0L7fR3XO5AXxZgOX4-AZwzYDqJeOkGTpN2IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcc75ff65f.mp4?token=sjb_k8tuIzy5T5_DzpumO9XtcJGWpIJbitKwfzj2vaB-8OzXIzhbBpcTfbpXczpw76EsXdsgbexZTCfx2EyfmwEIeQ6GikkBa7byFw6L8_NpwSud88YfRjynoHBxHGSBCRlVc3mOVPn9YVgpQFNLIatMzu0xh9KRXm02ihcO-nuPdsu_EonZqWbwVonbA1-WpVgEZtowRTvIgaBX8q7sfXGYsYev9rkfeicojts4xKZJTPoQzjgE02A4QeaSmnI0J7A7KQRBD2fIQBi9WBPdbI9EjasQ5N7rKRV2CBbDgyZ0cywhuz0L7fR3XO5AXxZgOX4-AZwzYDqJeOkGTpN2IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک عکس، یک تخفیف وسوسه‌کننده
پلیس فتا:
🔹
کاربران موقع خرید مراقب صفحات و کانال‌های فروش محصولات قسطی باشند و پیش از اقدام به خرید اصالت و اعتبار آنها را بسنجند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/686791" target="_blank">📅 08:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686790">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b109b0dca.mp4?token=r4BpX43BzJAhFyJnhPk6NXgHumBVikwv2mmDmK5YV_ARlQ-oaXUVUVaQGwN_P9hfNAh631BVHlydeRcpxJZ_Aa0b59soulA0g_DPK5P14cl6GXMhnfpSfe0wzzEQtc5lG5TonB_KdoHdRPWS5yZ63JlESViz2pyhjiA3WhDIPGdLV29Lj3h1hnEOEVFvc8lP1XW71msrT_AokL6SkU8psI92NOmZ6ndMU_Uilz1bqY-oXS1IRrtgRpNgSLcqO-PNDRrWGcVypvyIkLbetLzYHhbC4GJegvyIjPmFa60s3BsENmC2EpEV5wK0FOZsV1-2O6HQCI2-BBK05SD8PeJeqzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b109b0dca.mp4?token=r4BpX43BzJAhFyJnhPk6NXgHumBVikwv2mmDmK5YV_ARlQ-oaXUVUVaQGwN_P9hfNAh631BVHlydeRcpxJZ_Aa0b59soulA0g_DPK5P14cl6GXMhnfpSfe0wzzEQtc5lG5TonB_KdoHdRPWS5yZ63JlESViz2pyhjiA3WhDIPGdLV29Lj3h1hnEOEVFvc8lP1XW71msrT_AokL6SkU8psI92NOmZ6ndMU_Uilz1bqY-oXS1IRrtgRpNgSLcqO-PNDRrWGcVypvyIkLbetLzYHhbC4GJegvyIjPmFa60s3BsENmC2EpEV5wK0FOZsV1-2O6HQCI2-BBK05SD8PeJeqzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ضرغامی: نفوذی، جریانی است که در میانه جنگ حرف لایحه حجاب را در دهان نماینده مجلس می‌گذارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/686790" target="_blank">📅 08:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686788">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlO_sy7wcc3K5wUrrNV4fNDiMN6rTBT1YFGSVFVYhnhkQkvaO7zX8tHZESYlB5rQ2rJuxROzgbet-Aox8B0DWr0-7aw-JKeJ4xc5fMZxGx1FtzOXn7zqwFhyQpBKOeyQyEooSOLxg6XZCE6iVnZmY2RdsiGYrAF3-9OTVH0xCKpjesRQhoXS4J04WFTHWJjEJHNTgs62KLEbpFYVD2HvjLbsmlLCOCWFnPrt_fMkMwe-veM-ypTTjx-MGOvZDvEIXnyZaP2xiekEmuJ1uUa8gcb4Rt1GqbdiKF2f98yzrWGUj2QtD_NtsQ2WKLrxH_8cBx55suHkFez7JqrLXgtofg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمد بن جاسم
،
نخست‌وزیر سابق قطر
:
به محض اینکه ما علیه ایران جنگ اعلام کنیم، آمریکا از درگیری خارج خواهد شد، سلاح به هر دو طرف می‌فروشد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/686788" target="_blank">📅 08:37 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686787">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزیر جنگ آمریکا استقرار نیروهای آمریکایی در منطقه را تمدید کرد.
🔹
گاردین: ادامه گرانی نفت می‌تواند برخی شرکت‌های هواپیمایی اروپا را از پا درآورد.
🔹
اسامی راه‌یافتگان به مرحله نهایی المپیاد دانشجویی کشور اعلام شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/686787" target="_blank">📅 08:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686786">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5118123820.mp4?token=F5XF4W1_KNo2efEN8SxBitFyz5-L8N8VrW_bM96jzoyr-_kCz_pS8WSHGf2LtVKO1ZIPRkWJCZD6y73mkM6ytQWnjelTnh8Rs3a4XqxpFoJYvKZTA3rIcyeJ30kw11rLu0ywM3RIzRNWa1U6DxDwXFOwjHBt15rUULhtkcGg6qaZlQ-z9_UaD5YAfrEcUGnqKzyW9-JPAOaOj79Jq5s--WnNu_dM5lKsptJ6jeGvqCNcevvdIvPhp8L01h96yIjShrzkMmgknl1pfTP-n3PeqQdiGMX2dCrQx8CE4CxU7j4BxByvGP_7mW3QuHasVjLbEqbfATCpHScJvo90ZxS9ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5118123820.mp4?token=F5XF4W1_KNo2efEN8SxBitFyz5-L8N8VrW_bM96jzoyr-_kCz_pS8WSHGf2LtVKO1ZIPRkWJCZD6y73mkM6ytQWnjelTnh8Rs3a4XqxpFoJYvKZTA3rIcyeJ30kw11rLu0ywM3RIzRNWa1U6DxDwXFOwjHBt15rUULhtkcGg6qaZlQ-z9_UaD5YAfrEcUGnqKzyW9-JPAOaOj79Jq5s--WnNu_dM5lKsptJ6jeGvqCNcevvdIvPhp8L01h96yIjShrzkMmgknl1pfTP-n3PeqQdiGMX2dCrQx8CE4CxU7j4BxByvGP_7mW3QuHasVjLbEqbfATCpHScJvo90ZxS9ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حماقت جدید رئیس تروریست‌های آمریکا؛ تغییرنام خلیج مکزیک به خلیج آمریکا!
ترامپ:
🔹
من نام یک دریاچه خاص را هم به «دریاچه آمریکا» تغییر دادم؛ همان‌طور که نام خلیج مکزیک را به «خلیج آمریکا» تغییر دادم. مردم این کشور عاشق این کار هستند!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/686786" target="_blank">📅 08:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686785">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
رئیس مرکز ارزشیابی و تضمین کیفیت نظام وزارت آموزش و پرورش: سال تحصیلی جدید به صورت حضوری از، اول مهر ماه با حضور دانش آموزان در تمامی مدارس کشور آغاز می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/686785" target="_blank">📅 08:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686784">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e15fc5dd5.mp4?token=UqOfxhrkZEbPBvxCG1j728FkTCTaUBXzYeTl6lcqUaF2esNS6q1wzjbk64sSWXhVzYEdcGJgIViuqTnGHVG8O4_pj7r2XtdUfYeyefzwLZn7o4sif_5fCAG8M2aKwrb-Hs0Rs4_AfwFQytiyLTWdMoXAeM7ZCW2_I47PS0HqtOKo4DJfMYWWVcKaXhw3LtYy-KlWBq_hF_lTl_pUzOQVHoMaEMmZnlLtJstNdRuBGau5NQCjr5yvjHdCwWlVrEPLegwUg9itx79r_NufplJG6jINIgVC21YyjR45NQTxeqZqY9LFywZVdaqSWP0Go2THABqTiSjLxBHV13kD1EtzXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e15fc5dd5.mp4?token=UqOfxhrkZEbPBvxCG1j728FkTCTaUBXzYeTl6lcqUaF2esNS6q1wzjbk64sSWXhVzYEdcGJgIViuqTnGHVG8O4_pj7r2XtdUfYeyefzwLZn7o4sif_5fCAG8M2aKwrb-Hs0Rs4_AfwFQytiyLTWdMoXAeM7ZCW2_I47PS0HqtOKo4DJfMYWWVcKaXhw3LtYy-KlWBq_hF_lTl_pUzOQVHoMaEMmZnlLtJstNdRuBGau5NQCjr5yvjHdCwWlVrEPLegwUg9itx79r_NufplJG6jINIgVC21YyjR45NQTxeqZqY9LFywZVdaqSWP0Go2THABqTiSjLxBHV13kD1EtzXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تورنتو زیر آب رفت
🔹
برخی شهروندان برای نجات از مناطق گرفتار سیلاب، خودروهای خود را رها کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/686784" target="_blank">📅 08:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686783">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
هوش مصنوعی در مدارس نیویورک ممنوع شد
🔹
زهران ممدانی، شهردار نیویورک، در آستانه آغاز سال تحصیلی جدید تصمیم گرفته استفاده دانش‌آموزان از بسیاری از ابزارهای هوش مصنوعی را در مدارس ابتدایی و دوره متوسطه اول محدود کند.
🔹
این ممنوعیت دانش‌آموزان تا پایان پایه هشتم را دربر می‌گیرد و حدود ۶۰۰ هزار نفر را تحت تأثیر قرار خواهد داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/686783" target="_blank">📅 08:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686782">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96e899eb18.mp4?token=K7dcQM8uF9lGyC-5ATIWbxxmFIXm_vbyXuVbUjCN8v2hwP5oUEpQPu3k_OLTUzVDcdTZqIkRzyd3_fr6Iy-5TXalQRDch1xO1XEBNuXsHD7ltRBKnNuGVgE9nOEWClLvlytIxmL7YrZ81gWSDGktuXABgQVafEZSfC7cmOmlVlQAnNzT6Gve9myLH06aTzbpHbg5lIup56ShKMVVjCxfUGKSicKs0C5xpzZKLYATORF7WTTDia42q3fAM5olOg6d4B6V0HpR6WGGTlvx4WOgN1xl8FAiWICodfGZ_PE4ghxDXcHuZBKNXiuMUzIk6GcmcCrYmEwpezavCWjHQEByqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96e899eb18.mp4?token=K7dcQM8uF9lGyC-5ATIWbxxmFIXm_vbyXuVbUjCN8v2hwP5oUEpQPu3k_OLTUzVDcdTZqIkRzyd3_fr6Iy-5TXalQRDch1xO1XEBNuXsHD7ltRBKnNuGVgE9nOEWClLvlytIxmL7YrZ81gWSDGktuXABgQVafEZSfC7cmOmlVlQAnNzT6Gve9myLH06aTzbpHbg5lIup56ShKMVVjCxfUGKSicKs0C5xpzZKLYATORF7WTTDia42q3fAM5olOg6d4B6V0HpR6WGGTlvx4WOgN1xl8FAiWICodfGZ_PE4ghxDXcHuZBKNXiuMUzIk6GcmcCrYmEwpezavCWjHQEByqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر دنبال نتیجه‌ای، لازم نیست هر روز تمرین سنگین انجام بدی
🔹
این تمرین‌ها رو می‌تونی به‌عنوان بخشی از روتین روزانه‌ات انجام بدی تا بدنت از حالت کم‌تحرکی خارج بشه و عضلاتت فعال بمونن. #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/686782" target="_blank">📅 08:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686781">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrqO4smF14PLP9OjbcEhrMdlA7c7JNu5rmWLyKmevko2wQDLNFfyTyVlfMHgwokhGPtpASABTk4iumZbRhTFHSaOg4d88wbo_C7uhDraiynPu-hKr64GQUiAUPNIkOmk_K-7q-EVcNg2SdZceMz3DYr4BczjJIrE2vzbnWriybj3jWUp84Ay4T3sejlnyJ9qy0TXrVYMFscPaOJaBfkGZ-S1gY8mPXSO-FwJNH4dO50S91QuzrxjnXUZe5GLOacCex2nSYai8PKFRLYViKCx3DFqftKBaH8HOTMUl7geLheC4VB56X7IhK7txzFGQt0WzbWI91GbOf9Qz1bXU37LDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی وزارت بهداشت: از ساعت ۲۰:۳۰ روز ۸ شهریور تا ساعت ۲۰:۳۰ روز ۱۱ شهریور، در پی حملات دشمن ۱۴۲ نفر مصدوم و ۱۸ نفر به شهادت رسیده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/686781" target="_blank">📅 07:56 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686780">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBrBCNpcXUC8cGAyfnmU_dnSIyj6r7SrGL83CLlE4bzU6psZmRSAOWl7K4iXfpMr97nHYumX4F09XcJF6-ylwNdsQqVWyNaxiFRV_62zhPcgFnWH_Xtwetff3Nuih1exXvBkXkosgeeya8cfOiwpoDcQd0YzVG5ji0rCRhIab0GGdzSKAI9wbpqTcdY7cxfUA0uBBPZcOLF_lQ6DTiX5FrukogihQIdPFy6aKYe0iT-Nm9-ahMr1v9SqcnZUnkhSR8OjcN3R9KmI2JWnYFKpidKXc3zWqGDsaCsjGeFp0J4MBwNLl5YYLNCkwocMt5XJsu_bWBVOqK9hdisNzkumng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: تا من هستم، اسرائیل نگران نباشد
رئیس‌جمهور تروریست آمریکا:
🔹
اسرائیل نباید نگران باشد. می‌دانید چرا؟ چون من رئیس‌جمهور هستم و از اسرائیل مراقبت خواهم کرد.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/686780" target="_blank">📅 07:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686779">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1717a331df.mp4?token=piGZXo3n4mTYAzYECiX1M7gWT04Un-I2sjSwxMAqDBBT5UyHYgfEIOeE6MaYRic3aF-oN6806tNOzZOYxnkP4lwSiTa3FL0DVrUny4Uk6aXI1GIiv8rLbuzQaydRL17pLj7DE9gzNuP5iIUP4JnYOvM56SAmJqIWtTO8Z0NTxDpB08Mj7zxe--uIQRHBnabLUHJU2ETo2QQPSVqkHXUsTieHGax4YEqocSm5Z2by3kyfkwJssaKv3La25pxWyWjQD40v35iDTP_xdbJvoOChuHZECQM7J2pMrvN6JFPf0UwcoXjJ0bve83orRk3tFij_IEgpDfjAuKfaX1d4kCCD2oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1717a331df.mp4?token=piGZXo3n4mTYAzYECiX1M7gWT04Un-I2sjSwxMAqDBBT5UyHYgfEIOeE6MaYRic3aF-oN6806tNOzZOYxnkP4lwSiTa3FL0DVrUny4Uk6aXI1GIiv8rLbuzQaydRL17pLj7DE9gzNuP5iIUP4JnYOvM56SAmJqIWtTO8Z0NTxDpB08Mj7zxe--uIQRHBnabLUHJU2ETo2QQPSVqkHXUsTieHGax4YEqocSm5Z2by3kyfkwJssaKv3La25pxWyWjQD40v35iDTP_xdbJvoOChuHZECQM7J2pMrvN6JFPf0UwcoXjJ0bve83orRk3tFij_IEgpDfjAuKfaX1d4kCCD2oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتانیاهو و هشدار تکراری ۳۰ ساله درباره «بمب هسته‌ای ایران»
نتانیاهو:
🔹
۱۹۹۵: «ایران در حال ساخت بمب هسته‌ای است»
🔹
۲۰۰۶: «ایران در حال ساخت بمب هسته‌ای است»
🔹
۲۰۱۲: «ایران در حال ساخت بمب هسته‌ای است»
🔹
۲۰۱۵: «ایران در حال ساخت بمب هسته‌ای است»
🔹
۲۰۱۸: «ایران در حال ساخت بمب هسته‌ای است»
🔹
۲۰۲۵: «ایران در حال ساخت بمب هسته‌ای است»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/686779" target="_blank">📅 07:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686778">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a28cd50ca9.mp4?token=AfisogZZId2NV3ADchx0zho3X4bReQI8sSNT97gHbY5gwXTl5k-txoRlxvPyYG7SEJ8lVPc7261I_O0_V08V5ddmzUGivQC5ZO3dYb0zH2IP3xG6sgim8U5aGXRKRPeeqQmQYnN8FQ5vm54-HLN61HvVNKQaHYxj2zXG5Lg_gI2v9sktRvHDrdIDFBkyriebta7JzUJl7y8gxCVxwNOGttkuH2GSHNHB8u_WTJ4evVczOsmItyNsrH07yuVD9R-ke-px2gXFu4XWdchhuIKfowVbKHEE4Kc7ZG_oNbrWqwuSryca5wMBFP-37ub-IMQE3o0nyBWDv_-yjkOLUyze7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a28cd50ca9.mp4?token=AfisogZZId2NV3ADchx0zho3X4bReQI8sSNT97gHbY5gwXTl5k-txoRlxvPyYG7SEJ8lVPc7261I_O0_V08V5ddmzUGivQC5ZO3dYb0zH2IP3xG6sgim8U5aGXRKRPeeqQmQYnN8FQ5vm54-HLN61HvVNKQaHYxj2zXG5Lg_gI2v9sktRvHDrdIDFBkyriebta7JzUJl7y8gxCVxwNOGttkuH2GSHNHB8u_WTJ4evVczOsmItyNsrH07yuVD9R-ke-px2gXFu4XWdchhuIKfowVbKHEE4Kc7ZG_oNbrWqwuSryca5wMBFP-37ub-IMQE3o0nyBWDv_-yjkOLUyze7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ جنایتکار: ایرانی‌ها درحال ساخت موشکی بودند که مین‌ریزی می‌کند
🔹
تا به‌حال شنیده بودید کسی موشکی بسازد که مین رها کند؟ من که هرگز چنین چیزی نشنیده بودم. اما آن‌ها داشتند همین کار را می‌کردند.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/686778" target="_blank">📅 07:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686777">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kM1jOB7tWeLRxdpoVw-M1Hzj1_WMMtcA6JRqXIgKGfx96a89iNx_UfVdQMV02fUs9VjfI-x8u1JwTjsvtNRloeYLrHxOdpI09BodR4oav0xhNUZuWc6fe4JPimrOgVUjRC9rgfAoWDsDteQFCwzxbilTTCqs2Jm0_A9_wKtj0F5MNZLMUWmdbB3eC2D_IBm6dTftfrymXB8PbtXhOEnV2yzUUz5L7unsAXaJs1qj3arv178mHJIL5YHrX6gmCHWkoTa2_V4EuC3pP02jnvHCxRgaYjdTQ2GTAc5oqEImTE48gr8tJltNxO7nCmc7JksGEOT-xK5pKu7McD-Wz1P1lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از محل اصابت موشک‌های ایرانی در پایگاه هوایی شاهزاده حسن در اردن
🔹
تصاویر ماهواره BJ3A، خساراتی در باند فرودگاه و آشیانه هواپیما را نشان می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/686777" target="_blank">📅 07:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686776">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
رئیس دانشگاه آزاد: نباید به بهانه حمایت، دولت را از ارائه نقدها و تحلیل‌های علمی و کارشناسی محروم کرد/ وحدت باید از سطح «همراهی در برابر تهدید» به سطح «هم‌افزایی برای ساختن آینده» ارتقا یابد
رنجبر رئیس دانشگاه آزاد:
🔹
انسجام ملی، هم در خنثی‌سازی محاسبات دشمن و هم در استمرار کارکردهای حیاتی کشور، نقشی تعیین‌کننده دارد و اکنون زمان آن است که با حفظ این مولفه، آن را در مسیر رسیدن به ایران قوی به کار گرفت. اکنون نیز تثبیت این پیروزی، بیش از هر چیز مستلزم جلوگیری از فرسایش همان سرمایه‌ای است که پیروزی را امکان‌پذیر کرد. در منظومه‌ای که رهبر انقلاب ترسیم کرده‌اند، اتحاد به دفاع متقابل و سپس همکاری و هم‌افزایی در عرصه‌های علم، امنیت، ثروت و پیشرفت منتهی می‌شود؛ بنابراین وحدت را باید از سطح «همراهی در برابر تهدید» به سطح «هم‌افزایی برای ساختن آینده» ارتقا داد. به بیان دیگر، اگر مقاومت و انسجام، پیروزی ایران را در میدان رویارویی تثبیت کرد، از این پس همین وحدت باید به پیشران بازسازی، کارآمدی، توسعه و اقتدار پایدار کشور تبدیل شود؛ و هر اقدامی که به شکاف اجتماعی، فرسایش اعتماد عمومی و تضعیف همکاری میان ارکان کشور بینجامد، در نقطه مقابل این ضرورت تاریخی قرار خواهد گرفت.
🔹
از این زاویه، مراقبت از انسجام اجتماعی و ضرورت حمایت از دولت، ممزوج یکدیگر و واجد یک دلالت روشن و فراتر از مناسبات سیاسی روزمره است. نباید به بهانه حمایت، دولت را از ارائه نقدها و تحلیل‌های علمی و کارشناسی محروم کرد؛ دستگاه‌های اجرایی برای موفقیت، بیش از هر زمان دیگری به نقد علمی، ارزیابی سیاست‌ها و مشورت نخبگان نیاز دارند. البته نباید فراموش کرد که عبور از شرایط خطیر کنونی، بدون برخورداری از دولت مقتدر ممکن نیست و از این بابت، باید همه تلاش را برای کمک به کار بست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/686776" target="_blank">📅 07:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686775">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKQH6bCbBsd0271MfC5fRpuVzjoVCbxp8nldq7yQK-NUTagAw1sZF2GnrVDnwo30X2EJ65MlZptxKVeksgQCG9tYJBljxYqvrDCHLbv8bxt9j3OIeR1wB2P9aQheldKIx9JamzExhBJK02IPk4KFEJUZcyrzHjjo-gx-XS2thogNyo3hLZWtYBUMKGxvW4zyvUm3dvEurHM8a74V8KtXvASLX3PY_YuGjU4PB0EOJavMJ8WnnOAKapoNjJ4GfQfBepB80msro3UybDsd1rjYyOgAGO4q33ZNMhHQ6QKGB2VKVEJFwkPD3LG98t5AZDNDVkP-_LgEEEyxewFKA7yCrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز پنج‌شنبه
۱۲ شهریور ماه
۲۱ ربیع‌الأول ۱۴۴۸
۳ سپتامبر ۲۰۲۶
پنج‌شنبه‌ها
#دعای_کمیل
بخوانیم
⬅️
متن و صوت دعای کمیل
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/686775" target="_blank">📅 07:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686774">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
منابع عربی: یک نقطه مهم در یکی از پایگاه‌های آمریکایی در کویت مورد اصابت قرار گرفته و ستون‌های دود از آن برخاسته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/686774" target="_blank">📅 07:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686773">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
حمله موشکی یمن علیه مواضع مزدوران سعودی
🔹
منابع عربی از شنیده شدن ۵ انفجار در ساحل غربی یمن خبر می‌دهند.
🔹
به گفته این منابع، ارتش و انصارالله یمن با موشک‌های بالستیک مواضع مزدوران سعودی را در استان إب در جنوب غربی یمن هدف قرار داده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/686773" target="_blank">📅 02:12 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686772">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">عاشقانه‌ترین کنسرت سالار عقیلی
❤️
📍
این‌بار در شمال ایران، شهر نوشهر
🌊
‌
⏳
۱۸ تا ۱۹ شهریور
🏨
هتل آراز
🔗
خرید از طریق:
honarticket.com/s.ag1</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/686772" target="_blank">📅 01:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686771">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljMbz7cfc0Rcg8Lu9zSHSDwsX_QR5btKEPwUziSVQdz8uBWTNUf3qu7AwILT56P-QeaZzCsRLjTo9zC8FtV4xIXy9kHufRGGaFL-SKO7-RfjLXtMeKme5JQgR5x_O3imJO2IdSrNekcs3Is78RTVr5iG-PNCBtCuCI9S8B_Q60AJURMBkoD5ITOLFm47mJSuWtIyJjSj9BZnfZumTLXqH6JYsH98XrXsqHzNVpyVB4v2-pu0QtMSZLgDuHi-Ynq0gMoixaSrygB8zxyic9-pfwniWD70x2fsYkrrMJeoOwwW0ar8YlqQukTF58D_vbO_-X8sxIpCVEEnR6GuuJ_V_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
نوکیا 106؛ گوشی دومِ اقتصادی و بی‌دردسر!
اگه دنبال یه گوشی ساده برای تماس، پیامک یا یه گوشی دوم دم‌دستی هستی، نوکیا 106 انتخاب خوبیه
👌
✅
دو سیم‌کارت
✅
رجیستر شده
✅
حافظه ۴ mb/ جمع‌وجور و کاربردی
پرداخت درب منزل
❌
قیمت قبل:
۲,۵۸۰,۰۰۰ تومان
🔥
قیمت با تخفیف:
۲,۱۸۰,۰۰۰ تومان
📲
همین حالا سفارشت رو ثبت کن!
https://memarket24.ir/product/brief/63667/180124/</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/686771" target="_blank">📅 01:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686770">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a89f4a76b.mp4?token=dG1vwiCauKMIFQPGjfTqt0F9nxSuTgN6lRV7KFlA5q4KI-h5njAy8Y5GSll13nN3wYchE8PlaLzmp5NEGfQ0OcyvYrLFqRFRwSY5_6-I3-rJQwNcEUZkL2CaS2IRzJYFhiFbZ9hh4CY3PxNc-QUOMIuLI0v-bmMRDfLdRDdDCXt8WqDuwgLoNuvAVssAypgM8D4SkzGID2WBAQK76plciSEq0wtFUUe5dQDqTZGrHpDYmvVBD2P8kDOl8L7XVHjlB4qbpqnT02sI_ybAK06Xf_0tJfWzURx1bKOSPn8x-OzdZnnekMoZKpI8ygBNfVV58B31-Lo_yH6tt5cmW4yX5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a89f4a76b.mp4?token=dG1vwiCauKMIFQPGjfTqt0F9nxSuTgN6lRV7KFlA5q4KI-h5njAy8Y5GSll13nN3wYchE8PlaLzmp5NEGfQ0OcyvYrLFqRFRwSY5_6-I3-rJQwNcEUZkL2CaS2IRzJYFhiFbZ9hh4CY3PxNc-QUOMIuLI0v-bmMRDfLdRDdDCXt8WqDuwgLoNuvAVssAypgM8D4SkzGID2WBAQK76plciSEq0wtFUUe5dQDqTZGrHpDYmvVBD2P8kDOl8L7XVHjlB4qbpqnT02sI_ybAK06Xf_0tJfWzURx1bKOSPn8x-OzdZnnekMoZKpI8ygBNfVV58B31-Lo_yH6tt5cmW4yX5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش سازمان ملل به حمله آمریکا به مراسم عروسی در سیریک ایران  سخنگوی دبیرکل سازمان ملل:
🔹
دبیرکل سازمان ملل عمیقا از گزارش‌های مربوط به تلفات غیرنظامیان از جمله حمله‌ای که گفته می‌شود به یک مراسم عروسی در ایران اصابت کرده، نگران است و خواستار توقف فوری خصومت‌ها…</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/686770" target="_blank">📅 01:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686769">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/806ade1008.mp4?token=UknR3gv6GLxa8pe3JHaBCdwfilRp3GGDXQORJGGDw9ej_fzSr0AIlSesNZ6U5Em7LmyrpqYDgpB7z8I34Z3YcZxZIdeXlzKQl86ZYyXWwO7XXMOGqZn3UEOmHgOLkJ9G7pj2UvRTMP0CQzJTkY9nDqaB2h78c3mlD5FPIrtZ--WmRnjgf4DD-1bF9syLR-8qFIQgCX7NMYApToHLE0Bxs0zEhk3yOMpRWMiWl1P5TNWDSC-pDUjmaceVbgC2refEMz_lpcJmiWkynn3ptIlNsdAiqeUY9R4SfQXDy_qmBIPH-snoHvjjSWKGDsfdI4MeNRYtUl_q2LX7Ekaqf3Mpkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/806ade1008.mp4?token=UknR3gv6GLxa8pe3JHaBCdwfilRp3GGDXQORJGGDw9ej_fzSr0AIlSesNZ6U5Em7LmyrpqYDgpB7z8I34Z3YcZxZIdeXlzKQl86ZYyXWwO7XXMOGqZn3UEOmHgOLkJ9G7pj2UvRTMP0CQzJTkY9nDqaB2h78c3mlD5FPIrtZ--WmRnjgf4DD-1bF9syLR-8qFIQgCX7NMYApToHLE0Bxs0zEhk3yOMpRWMiWl1P5TNWDSC-pDUjmaceVbgC2refEMz_lpcJmiWkynn3ptIlNsdAiqeUY9R4SfQXDy_qmBIPH-snoHvjjSWKGDsfdI4MeNRYtUl_q2LX7Ekaqf3Mpkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دعوای دو موش در متروی «آکسفورد سیرکوس» لندن؛ جایی که انگار موش‌ها هم بخشی از منظره عادی شهر شده‌اند!
😆
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/686769" target="_blank">📅 01:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686768">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/246f6e66f3.mp4?token=nGRtqZQWrOe3FQCBat9Z1bj3bjX0mYjAm22l4zPuwLvVS8saZs3bnaumhvETWfcS28SJmXhmZ1uVgxCrKg2sKSk--PCzGq7CPv0kZGoMeToFVnURfrOOo-saGqRUAXdohSyH1ESOxjgsFna6dBKhtOO3Y89exKonb9rUdqFfIWwpj06D1MrRrlhISr8KvVYSmgQSz1CSerDjQq4xFUmswBAdh4ZmgoypVfm3hGkvdTCTcrVa0W8tdzGW5iyhar_ZXHpJgSB-g1j3oEmdkElsaOCk39QElHVz0a8xcT9yvSnYSqIhUzl6p3Fe7kPwtIVReCGyE6Gerf_CBOJ6b4d9QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/246f6e66f3.mp4?token=nGRtqZQWrOe3FQCBat9Z1bj3bjX0mYjAm22l4zPuwLvVS8saZs3bnaumhvETWfcS28SJmXhmZ1uVgxCrKg2sKSk--PCzGq7CPv0kZGoMeToFVnURfrOOo-saGqRUAXdohSyH1ESOxjgsFna6dBKhtOO3Y89exKonb9rUdqFfIWwpj06D1MrRrlhISr8KvVYSmgQSz1CSerDjQq4xFUmswBAdh4ZmgoypVfm3hGkvdTCTcrVa0W8tdzGW5iyhar_ZXHpJgSB-g1j3oEmdkElsaOCk39QElHVz0a8xcT9yvSnYSqIhUzl6p3Fe7kPwtIVReCGyE6Gerf_CBOJ6b4d9QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دلقکی به نام ترامپ و سیرکی به نام کاخ سفید
🔹
کاخ سفید پس از شکست‌های پیاپی و ذلیلانه در برابر ایران، نقشه تنگه هرمز را منتشر کرده و اسم تنگه هرمز را به «تنگه ترامپ» تغییر داده؛ عکس ترامپ نیز وسط تنگه است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/686768" target="_blank">📅 01:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686767">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jnn9LeFd2YjlX9H-NG2ypVyduORGr2DMIXJszZz-d28hSJA6-4Z7d4Ma_W5k4H-T2EoTOKB1bXweIAlfizq1PF1x9_YbgJt6YBqHdthP1dFey3N9W8soTJ3Fv0prQXWp2h2KocOO44yPVPwT1otuXixInLGqHvtIfsGmPExj27CDnwtxOv3hUFbfkXsqHow-o1kLwT2HA8mIm42wl1jx4Uby8hNl5Z4mMQH1oEBCbztlC-UBzRcJH7iuIe_K3GjZgt_P5WG6uYTmIt7pr_n7UDVTOZpuSr0jVd33liwZWUum9jC6q-esIrR0A5_PG2OPLAm-30uO9wotCtWQLujoFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دلقکی به نام ترامپ و سیرکی به نام کاخ سفید
🔹
کاخ سفید پس از شکست‌های پیاپی و ذلیلانه در برابر ایران، نقشه تنگه هرمز را منتشر کرده و اسم تنگه هرمز را به «تنگه ترامپ» تغییر داده؛ عکس ترامپ نیز وسط تنگه است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/686767" target="_blank">📅 00:56 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686766">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
بلومبرگ: صادرات نفت عربستان به پایین‌ترین سطح ۹ سال اخیر سقوط کرد
🔹
حملات به نفتکش‌های سعودی و ناامنی دریای سرخ، صادرات نفت عربستان را کاهش داده و تردید مشتریان و کشتیرانی‌ها برای استفاده از بنادر این کشور، ریاض را به استفاده از مسیرهای طولانی‌تر دور قاره آفریقا وادار کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/686766" target="_blank">📅 00:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686764">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/avEwsyZ6FuHPL_q0BhOhmYcx4KgLnI51vDE4pohIjkoo07o_bY04BzHZRGVgZpYzPUp-gVVCVZTlVk87S8Rl6gERLzU_IvE50J-b6HUcDPH5uV8tP-m8SY9XNCikwq8ndiExLhnPA6G_7IkJuyj1urY4b3xrMcXujx8kHfjQ7_DwOAHret6zMlHa6eOHtxNnNIpiwF2hxQp5d6b1FV7CeJzqmKuvW5fMOXqaU8YRe_fTGTKwPpWU8uurkuAP5ZsO6c8KmtuaIYG_HCg99p1NfJraBO5iDUCl5R5dJ1ZFA1YcNXPbz9oWkiWXUidQ9Los2qHcT7rcwqH9LvAy7umnXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CFxBSdhLEQoq7dXC0-uHBgyDyeWYndY5XXh8qCvBtcX4fDEjEmG5_hUGacGgCB9UQRgljOcC4n2zqyKoc-JUxo-CcRZAWQUylyPOsndEuaM-rw3m0DUw2taziZDcHmYYAYm_MqmYPYSDjegenb2M5J9DMaLOuVTRbQnQKTFcckH1ZpFK4lKUFh3H9UYJGnRGsxrbtMmQlHlqR1n9kPUHeDQbfyzx3FQig5s5n0bOjggnC7tEQm_srr56YNh_8R248f-ipaBqiWgTJVfwYs8Ci3zEF9Tu2txzW6dj66zZfiij6eJuAJoPs0Oho8kG-pXasOygi-4KSePag-VIuKtqaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
سرنگونی پهپاد آمریکایی در خمین  #اخبار_مرکزی در فضای مجازی
👇
@akhbar_markazi</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/686764" target="_blank">📅 00:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686763">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
نیویورک‌تایمز: نیروی دریایی آمریکا در منطقه گرفتار «کابوس لجستیکی» شده است
🔹
ادامه جنگ با ایران، شبکه پشتیبانی نیروی دریایی آمریکا را مختل کرده و ناوگان منطقه‌ای هر هفته به بیش از ۴۲۰ هزار وعده غذا و ۸ میلیون گالن سوخت نیاز دارد؛ در حالی که حملات ایران برخی پایگاه‌ها و مسیرهای تأمین را از دسترس خارج کرده و ناوهای آمریکایی مجبور به تأمین سوخت و تدارکات در دریا، تقریباً هر ۵ تا ۶ روز یک‌بار شده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/686763" target="_blank">📅 00:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686762">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔹
خبرهای داغ امروز را در وبسایت خبرفوری کلیک‌کنید
🔹
🔹
پشت‌پرده اظهارنظر جنجالی بسنت درباره ایران | نقشه آمریکا برای آشوب دوباره در ایران؟
👇
khabarfoori.com/fa/tiny/news-3242269
🔹
۴ شرط چین برای امکان سفر قالیباف به این کشور
👇
khabarfoori.com/fa/tiny/news-3242176
🔹
دلار ۲۲۰ هزار تومان؛ زنگ خطر معیشت در تله ارزی | چرا ترمیم فوری دستمزدها دیگر یک «انتخاب» نیست؟
👇
khabarfoori.com/fa/tiny/news-3242226
🔹
پُست جنجالی پیت هگست درباره اندام یک زن سرباز + عکس
👇
khabarfoori.com/fa/tiny/news-3242175
🔹
پاسخ تند بازیگر زن به یک حاشیه جنجالی | دهان من بوی پیاز نمی‌داد!
👇
khabarfoori.com/fa/tiny/news-3242219
🔹
خبرهای جذاب هر روز را اینجا دنبال کنید
🔹
http://khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/686762" target="_blank">📅 00:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686761">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bcf3931a6.mp4?token=ItaHjOOIDjPsq7hC4ItIoa7tySY-0uDwuzL5-jwTc7Q_mwSOLEyppdpWHu7FZfKS4AZsf10BSLVhR81dWrKSebR1qFayo6VQDaBlHH1pJerkR5nlibDfaAVHSK12PxDSqKxipcOO-JQcgbvafy4RnbSC991PxRQZ8PH34HrWSOB3DZZHqQiiVBLbmKgk7t8CfTnv8nI9xrQ3z8ZBTaegeuCJWAOxm-vtKhJhZ9_Pr_rGZFasgMcbqJNM3lssSl-2BNzFz_SHksSxChGQSx_8LgCAB-DCg2iKHuz9s5kdzDggCa8_vMyVRAXLK54VV7sH9GfQ9gcMrRmaC-tY8RpjVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bcf3931a6.mp4?token=ItaHjOOIDjPsq7hC4ItIoa7tySY-0uDwuzL5-jwTc7Q_mwSOLEyppdpWHu7FZfKS4AZsf10BSLVhR81dWrKSebR1qFayo6VQDaBlHH1pJerkR5nlibDfaAVHSK12PxDSqKxipcOO-JQcgbvafy4RnbSC991PxRQZ8PH34HrWSOB3DZZHqQiiVBLbmKgk7t8CfTnv8nI9xrQ3z8ZBTaegeuCJWAOxm-vtKhJhZ9_Pr_rGZFasgMcbqJNM3lssSl-2BNzFz_SHksSxChGQSx_8LgCAB-DCg2iKHuz9s5kdzDggCa8_vMyVRAXLK54VV7sH9GfQ9gcMrRmaC-tY8RpjVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این تمرین شبانه که ۵ دقیقه بیشتر وقتتو نمیگیره زندگیت رو متحول می‌کنه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/686761" target="_blank">📅 00:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686760">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhhSSbJEuiHKSt-TMEZa2qUfyPOeDcTp_4NZVfV_EPPYK4Xq9q5xpFtPf9b4bnamUu7Esh2B0lrIHuwp3hWxIcLaK17WqTgTdjyCtrySpKbEena3GYtK9xBoR4eI-2E0ch6QIOROwETCcv1qM6D42e8AtYds4p1pCwM41XZmd0NstOuyB2EHX2AvOdS5rvkwa7YU5EygneYk8r3SFA36k-1uHbY-lqJzHFE24NJVGltalssSuOgwcqSiXcT_wK9gNswDnz4JQOMxo7njRQP_MvUCIE3kVEyxryL_eEtZ94EFuSv8nm2Lk85daP-d8MHXVnjvDxmWPE6kHm22tMuNwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/686760" target="_blank">📅 00:00 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686759">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ed9361942.mp4?token=YsLJnyGXuI3DJj0zkVs-csgHtChdfc0pslklGHUz5uBVhiMW-B0cLrrOsXBZk1NZ_Gh3T9zXeduvG0hfPyFYt8ysRZTmA9sIW8wwc3Dpbn5IDIedEZkkb3aKaUQBh8C8NlbimsI7VSKlXo9CmLo3IG5hk6gtd53ViIeoZqcrTeCIO2epkEg3UNh7wMMm9IJtr9V_zWCgb2X4KTn31khk4SEG634PHlt1OCYto2hnXiLEVbP_mfd4iap3DWSgNQ2b1n-z-hjFcVxM0SRdwnwt-CCNsg-W2unEsrjiZZ8HDdrnJiNdSuRn_80wHwMIw8YnjzqdqXNXYucrsb7l_gPcPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ed9361942.mp4?token=YsLJnyGXuI3DJj0zkVs-csgHtChdfc0pslklGHUz5uBVhiMW-B0cLrrOsXBZk1NZ_Gh3T9zXeduvG0hfPyFYt8ysRZTmA9sIW8wwc3Dpbn5IDIedEZkkb3aKaUQBh8C8NlbimsI7VSKlXo9CmLo3IG5hk6gtd53ViIeoZqcrTeCIO2epkEg3UNh7wMMm9IJtr9V_zWCgb2X4KTn31khk4SEG634PHlt1OCYto2hnXiLEVbP_mfd4iap3DWSgNQ2b1n-z-hjFcVxM0SRdwnwt-CCNsg-W2unEsrjiZZ8HDdrnJiNdSuRn_80wHwMIw8YnjzqdqXNXYucrsb7l_gPcPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهبر شهید انقلاب: آمریکا شیطان بزرگ است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/686759" target="_blank">📅 23:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686758">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28a8af5e81.mp4?token=gerfBJ2Z5S0IDCWFA4Qo8Deb2Z0GD-RZKRqipBynicspCD49y1glCrQY01R7Q-gsVGtnXapny3G7YX42L4OBjAzcuJFxdHnt_VLXw1IK-Urps0RE6RgK4y-5V-0iOnpJ3eK0aaOBx-Rpg3I6uvLota-ilBH5FpQnG52wUrqdXFSQs9qB-7udTbNnHHfr01fmugyFNI6Gbk2Olw_7TvoR2RCfeBPN67zGLmmA3btOYH3JWaEmiXtFJ_2io8bk-urkFGbb5Q8h0Pn0MDsILY1F3GlLi9tH8qxXpI5q2Eqr0Mi-_UpJ1HHTg4B1M7Lnmohd42Em4wEWf1GZp6aUP1BwFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28a8af5e81.mp4?token=gerfBJ2Z5S0IDCWFA4Qo8Deb2Z0GD-RZKRqipBynicspCD49y1glCrQY01R7Q-gsVGtnXapny3G7YX42L4OBjAzcuJFxdHnt_VLXw1IK-Urps0RE6RgK4y-5V-0iOnpJ3eK0aaOBx-Rpg3I6uvLota-ilBH5FpQnG52wUrqdXFSQs9qB-7udTbNnHHfr01fmugyFNI6Gbk2Olw_7TvoR2RCfeBPN67zGLmmA3btOYH3JWaEmiXtFJ_2io8bk-urkFGbb5Q8h0Pn0MDsILY1F3GlLi9tH8qxXpI5q2Eqr0Mi-_UpJ1HHTg4B1M7Lnmohd42Em4wEWf1GZp6aUP1BwFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش سازمان ملل به حمله آمریکا به مراسم عروسی در سیریک ایران  سخنگوی دبیرکل سازمان ملل:
🔹
دبیرکل سازمان ملل عمیقا از گزارش‌های مربوط به تلفات غیرنظامیان از جمله حمله‌ای که گفته می‌شود به یک مراسم عروسی در ایران اصابت کرده، نگران است و خواستار توقف فوری خصومت‌ها…</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/686758" target="_blank">📅 23:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686757">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c1457afab.mp4?token=EtgxhGn9u20Mi8mAgRrUMzEyrR3V_56xtua48ecYUxXK8eTVmVGcUNTsrKbsCx2GPzvrvu_4OlpSd4BVswPoBb8gtQb0eEMTkWwhSvpJQMeKNAU3nMW65Pl4DgKQ1OxERHCIufD6vUQu1X72CRXZxL_7vsUna-AyaOosw-Z_eO-sKkqX3EZHtx46xPAhXvoQsOxeRx-_Oz1oH4-dA0817XAVkaVU5r-NGKzO_lBt3YPQ9n_-WmLvYc020OA7xg7DoT825cOhvCrr1-f0P9-_zEusUfTMZNtVtHdt7wAc3sHuC5GZ9vSIhjbfo90a31PvvNh_TrEBIbqYd2QLYJKmxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c1457afab.mp4?token=EtgxhGn9u20Mi8mAgRrUMzEyrR3V_56xtua48ecYUxXK8eTVmVGcUNTsrKbsCx2GPzvrvu_4OlpSd4BVswPoBb8gtQb0eEMTkWwhSvpJQMeKNAU3nMW65Pl4DgKQ1OxERHCIufD6vUQu1X72CRXZxL_7vsUna-AyaOosw-Z_eO-sKkqX3EZHtx46xPAhXvoQsOxeRx-_Oz1oH4-dA0817XAVkaVU5r-NGKzO_lBt3YPQ9n_-WmLvYc020OA7xg7DoT825cOhvCrr1-f0P9-_zEusUfTMZNtVtHdt7wAc3sHuC5GZ9vSIhjbfo90a31PvvNh_TrEBIbqYd2QLYJKmxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انواع میکس‌های قهوه رو بشناسید
☕️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/686757" target="_blank">📅 23:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686756">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5076db8a.mp4?token=CbNaX7rqzMFgRUYlnFz9TXUGgieJ2BDw_Dr5TxW9BHvJh2RaM75p1ugBLP2N9caMJIM6lDI1KQvzHb6rQWaZPSF1E9gbOn6i4zqzMGOjbmgw37mJd9ibrLhMSo9bmVcEokeEp3I14OwL5zfqXOfitNeT9PTFt0W-WBgdM-nDzHDLlH8R6ctVrebafmGXAd1EhVcpHDXpwFtNJQCX_HT2b_mSf1CIELCSk17wRSEuV_OqerlqwkQ1KKIV_BhnPb_NCciSGGaEpVXRSpmVSti91xkr4Hf4pE1jSSiwOguSz4dumqyZGx0MOnYCgRbSOF1lzjaB7PE6tNKB6H4gvBH_taw4Ejhxa0jURkBWj38Hr7KIFEbjBlMA1OlCDQZJ5hm-9BHAZpswJX4WUfl69JaCWrmMnO2AhdJrlfie53KYTLDXM9n212UMVz6JAPscpH0MP3edgK0qznImAfj5wonjNRXd5f0gE3FlTCttH3TnrEXuu-TWOE1kt2RA0AB3TlZnHa2PUriTRxqqM1OTW3Jk1A7ierJYCfQdgm97m38f5CLcxxVREcM_XZNnfdi9lHwxHgwB6_Uu-GAuGYNff2PUW3NktwUPKdHg2uwLfHZIOtyG-Wy_rATp4J639--r1TJWAhP0o5uuopfzVAf3gl4RPsmEuG0-xQUNO53RvWZ30RU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5076db8a.mp4?token=CbNaX7rqzMFgRUYlnFz9TXUGgieJ2BDw_Dr5TxW9BHvJh2RaM75p1ugBLP2N9caMJIM6lDI1KQvzHb6rQWaZPSF1E9gbOn6i4zqzMGOjbmgw37mJd9ibrLhMSo9bmVcEokeEp3I14OwL5zfqXOfitNeT9PTFt0W-WBgdM-nDzHDLlH8R6ctVrebafmGXAd1EhVcpHDXpwFtNJQCX_HT2b_mSf1CIELCSk17wRSEuV_OqerlqwkQ1KKIV_BhnPb_NCciSGGaEpVXRSpmVSti91xkr4Hf4pE1jSSiwOguSz4dumqyZGx0MOnYCgRbSOF1lzjaB7PE6tNKB6H4gvBH_taw4Ejhxa0jURkBWj38Hr7KIFEbjBlMA1OlCDQZJ5hm-9BHAZpswJX4WUfl69JaCWrmMnO2AhdJrlfie53KYTLDXM9n212UMVz6JAPscpH0MP3edgK0qznImAfj5wonjNRXd5f0gE3FlTCttH3TnrEXuu-TWOE1kt2RA0AB3TlZnHa2PUriTRxqqM1OTW3Jk1A7ierJYCfQdgm97m38f5CLcxxVREcM_XZNnfdi9lHwxHgwB6_Uu-GAuGYNff2PUW3NktwUPKdHg2uwLfHZIOtyG-Wy_rATp4J639--r1TJWAhP0o5uuopfzVAf3gl4RPsmEuG0-xQUNO53RvWZ30RU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش خبرنگار شبکهٔ سه از قشم: احتمال دارد تعداد شهدای حملهٔ دیشب آمریکا به یک مراسم عروسی افزایش پیدا کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/686756" target="_blank">📅 23:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686754">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWCms13BE7M3_0baf9m2IL2WwGbUEQL5tOiGVUS7NNnxioXGVNoro0vET19t1-l4-J8eed6UmcbEcfh5XhsmfXXFoGcRjOjIPNOoBTtxvnHHxi99XT0gdVR0NVZoxcA16q7LVbW99ix5o4nGjDpmJWK1BVp48TSzCxzV0cTmZsbSFTq2geuhXS7KTM41xrJB9xgITax7t5kHOIeFo9u_lo3j-wiLtcjiLnyGy51QWrIkEXzRoPaC-zv74EJFJ9pgGHjkOZihPUnuvJ1NG9bCEjPLiQ0jcbnrxTMOlSfp3QNneXXTTYs-gq2PKzn4lLI-oMThhdnyODNFnD341tzHhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویری دیگر از ناو فرسوده و زنگ زده آبراهام لینکلن پس از عقب نشینی و رسیدن به تایلند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/686754" target="_blank">📅 23:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686753">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6CSw2YU2BCAeqWmUERF4UZH8GxbeOMX8ifxXyrYzti4DLq9cnu9YUgSs0LP_r9SCMRKEBtjVf10N4nZD8iY-OqIuU5fVin36FqvS2c4dWQ3JX5nai1e5ZW3_SX-2Tl80afqqYOWbWfCQdDx5FZsm2QraESH7ny1m7EjJu9iiioKj5h9fxQMBOvMZ15IXBJuH_z-ZM89nVD8b2oNI223rgh23CINLIXWfk-cD6Jj9NA7BD54QmpQB5uOEdkNZ-ubJ7GCwupJDP72-dSe-FR3HIQMqyFhYRSIhp0Y7GjK34pJ2y5pRbPz5Dv5LCqlboyZP4TR0s_IKpeHBu37b-orHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با دانستن کاربرد این ۳ پیچ، درب کابینتت رو راحت تنظیم کن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/686753" target="_blank">📅 23:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686752">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58495794f9.mp4?token=nvugTgOBbpyKQUqmCqbPNorbl6lajJOKN6ETNANbX_eu38SaONbnIMahTA1AnpuplOWSFEA2PLy8K6w5IYmo6szfwuIb8xRwszHmOVpyLhS_2lAg-jZ1_0Y7OjWUhp5zGGIlI1huE2oVLrkBGI2kjBPQ2G4X6Wfig9cTEgzyS-2j5EMmbWyRrdNiosNV3zGt0vFCVw-C68a8Jh99-Baw6zugb_gi5Pus3128SW3c-6lOXEVkRh76bEjmnW4unZLX3fsAkiStHUYLZa2XVvX4F7BwviwSERrktQdmgbUbt1kQLJ7e_Vz8IFgYYLF2YMDQxIiR-FnAMWmIMVopEmFCjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58495794f9.mp4?token=nvugTgOBbpyKQUqmCqbPNorbl6lajJOKN6ETNANbX_eu38SaONbnIMahTA1AnpuplOWSFEA2PLy8K6w5IYmo6szfwuIb8xRwszHmOVpyLhS_2lAg-jZ1_0Y7OjWUhp5zGGIlI1huE2oVLrkBGI2kjBPQ2G4X6Wfig9cTEgzyS-2j5EMmbWyRrdNiosNV3zGt0vFCVw-C68a8Jh99-Baw6zugb_gi5Pus3128SW3c-6lOXEVkRh76bEjmnW4unZLX3fsAkiStHUYLZa2XVvX4F7BwviwSERrktQdmgbUbt1kQLJ7e_Vz8IFgYYLF2YMDQxIiR-FnAMWmIMVopEmFCjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیشنهاد ۲ میلیارد دلاری بابک زنجانی برای خرید سایپا!
🔹
بابک زنجانی در حاشیه نمایشگاه الکامپ و در نشست خبری خود، پرده از یک پیشنهاد جنجالی در گذشته برداشت و گفت:
🔹
«من سایپا را قبل از جنگ درخواست دادم؛ دیدم قیمت آنجا را ۱ میلیارد دلار برای فروش گذاشته بودند که البته به خاطر بدهی‌هایش بود و می‌گفتند یکی بیاید این بدهی‌ها را تسویه کند. من همان موقع درخواست دادم که سایپا را ۲ میلیارد دلار بخرم، اما خورد به ماجرای جنگ…»
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/686752" target="_blank">📅 23:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686751">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">رونمایی از «دیماپی»؛ گامی تازه از بانک ملت در مسیر توسعه اقتصاد دیجیتال/ ویدیو
🔹
شبکه اعتباری خرد با هدف اعتباردهی هدفمند و هوشمند به مشتریان
🔹
فرشید فرخ نژاد مدیرعامل بانک ملت اعلام کرد:
بانک ملت در مسیر تبدیل‌شدن به یکی از زیرساخت‌های مالی اقتصاد دیجیتال کشور قرار دارد.
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/686751" target="_blank">📅 23:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686750">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
واکنش سازمان ملل به حمله آمریکا به مراسم عروسی در سیریک ایران  سخنگوی دبیرکل سازمان ملل:
🔹
دبیرکل سازمان ملل عمیقا از گزارش‌های مربوط به تلفات غیرنظامیان از جمله حمله‌ای که گفته می‌شود به یک مراسم عروسی در ایران اصابت کرده، نگران است و خواستار توقف فوری خصومت‌ها…</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/686750" target="_blank">📅 23:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686749">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QaqB_z5YtbMoJFDyxMuYPzi72rEoLgpy-jlVHDlir13R4xBmXUkt_7uY3bNFnLiZRUH0-Hy4b8mQsObV7nfOs4SSWyuxWXeFWW4EPuUpNRq5k16oRBF4SqwLdN_Ymv7rnu7H0lc-eqHMCpCPuSBklEZKkHeeZXkD6y6DhXQoP7SjJdVEKDI03uFrqJHIC2HZyTaZQ5yD8QL3n-EnQqv1qWfLC9MGS2JuKFQuaRIPv7Dfpcie1bjCemut_8tYwbGt47gCBMfl1rKKit91THfe5O1vMpnSIJhjLahMQbfft92FiFDQsOkFZ_WdFBcUK1I2hgzelTf8UTkW4SpugZtM2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعتراف وال‌استریت ژورنال: قیمت گاز در اروپا به دلیل حملات ایران و آمریکا، به بالاترین سطح از پایان سال ۲۰۲۲ رسیده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/686749" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686748">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNazu02a8CtuYrJqJK6ffWTvDztiW14WZ0qbUDu1wU_NCzGch6u_P4EI5Zt7Ze-naOy_aW_uhQn8REBtLrmYI6L_Z8DJWphF45H-gz_LrpPNd02ULg2DPaqnZgEQ8wNXC8LOQRu1iMU-EVzC2pkyXRO7x5dJN6-s3CMP17Db2iIjp-xEi7Tb4ix7DhTX9ipP6mZrYlm0ys86JMVO8-8yxkKERUd9w7sUT5TYIM-z7KIV4XfXQbNSX2XszBw-bY304jzCJh4zKvg1epwM7uM0StSgIl5r4PakZnqkVpcoLVX3zwR5NoHzZXCz_0S6SKsLgobh5fV9fTcijudjzyek6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انهدام چشمِ آمریکایی‌ها در آسمان اقلیم
شبکه روداو اقلیم کردستان گزارش داد:
🔹
یک بالن نظارتی آمریکا در جریان حمله دقیق سپاه منهدم شده است؛ بالن و تجهیزات مرتبط با هدایت و مدیریت آن، هدف حمله قرار گرفته‌اند.
🔹
این بالن برای رصد منطقه و جمع‌آوری اطلاعات و تصاویر هوایی استفاده می‌شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/akhbarefori/686748" target="_blank">📅 23:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686747">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/686747" target="_blank">📅 23:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686746">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
فرمانداری سیریک: صدای انفجارهای احتمالی امشب در محدودۀ بندر کوهستک، مربوط به خنثی‌سازی مهمات عمل‌نکرده دشمن آمریکایی است
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/686746" target="_blank">📅 23:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686745">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">عارف در ایران‌بوم؛ بازدید معاون اول رئیس‌جمهور از ویترین دولت هوشمند
محمدرضا عارف، معاون اول رئیس‌جمهور، به همراه سیدستار هاشمی وزیر ارتباطات، در سومین روز الکامپ ۲۹ از پاویون دولت هوشمند و پروژه ملی ایران‌بوم بازدید کرد.
در این بازدید، آخرین دستاوردهای زیست‌بوم‌های دیجیتال دولت و سامانه‌هایی از جمله ایران‌پاس توسط دکتر ستارهاشمی وزیر ارتباطات و دکتر محمدمحسن صدر معاون وزیر و رئیس سازمان فناوری اطلاعات ایران تشریح شد.
📍
سالن ۲۷ | پاویون دولت هوشمند
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/686745" target="_blank">📅 23:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686744">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
ورود دات‌وان به تجارت کالا و لجستیک
🔹
رئیس و استراتژیست ارشد گروه ارزش‌آفرینی دات‌وان از راه‌اندازی پروژه‌ای در حوزه خرید و توزیع کالا خبر داد و گفت: بخش قابل توجهی از کالاهای مورد نیاز کشور از چین وارد می‌شود و بسیاری از خانواده‌ها در شهرستان‌ها نیز به دنبال ایجاد کسب‌وکارهای کوچک هستند.
🔹
او با اشاره به پروژه «شاپکس» اظهار کرد: در روزهای آینده از این مجموعه رونمایی خواهد شد. شاپکس کالا را مستقیماً از چین خریداری می‌کند و از طریق قطارهای دات‌وان به ایران منتقل خواهد شد.
🔹
زنجانی همچنین از ایجاد یک شبکه لجستیکی رباتیک در منطقه آپریل در اسلامشهر خبر داد و گفت: کالاها پس از ورود به این مجموعه در سراسر کشور توزیع خواهند شد.
🔹
به گفته او، یکی از اهداف این طرح ایجاد فرصت برای کسب‌وکارهای کوچک در شهرستان‌هاست؛ به‌گونه‌ای که افراد بتوانند کالا را از شاپکس خریداری کرده و با فروش مجدد آن، فعالیت اقتصادی خود را توسعه دهند.
🔹
مشروح این خبر را در سایت خبرفوری بخوانید:
https://www.khabarfoori.com/fa/tiny/news-3242267
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/686744" target="_blank">📅 23:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686743">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KsPwVjcDmBPCHDHwknyXfe-RuB-h_aMb8R2e-KauGXg3Q_Fk4wbuJE9KRZZQ_NF4YFaXTLRTtNA1MGmq8U-ZO2V_dkKM-Mlstr7NosWCtDteOSyW5ZY3I6Myxwmuf5mt8jDxPhuH39uQZnt4hI_BYrSppQ7FOkGAC8Q5uixLSFi1mPT5K9jF0UJhTgA1EfcdloOe7SqQth7BMBkifcZXuFr3xkn2DuK7Q4XrP3--UnHk0CYvyodpNPTAZlwDwxr9waTHLGrveawF8hns7UgEg_cZlg1jPMno4XWtmoUBuuYdXbJ1gQDbcCMk8YciVUINT9KJz0TzOTr6jQzPTRTThg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گاردین: زورگویی‌های احمقانه ترامپ علیه کانادا، نتیجه‌ای معکوس به همراه داشته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/686743" target="_blank">📅 23:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686742">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/686742" target="_blank">📅 23:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686740">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b182ff65f.mp4?token=I2Mg-CzRWJ6rcen84PqmZm6TgvuXDce5Xu1HB61UQYOHWqvB3ySmivNXlAB2JDSITSYCaWwlMycb_rHB4SnbR2u35JwPl56FzMmNCYFACzgrIlXBYsP6Aky9X8-RCNA6A4zCvA-LXB6Y2CjyUkFkHo2Ams4Aisg7fdmUKhwRal7wSHTJn_ivTRL8jZhN8lsDUHJlWsh8ig6gi2yaBDcJ80gycDpc8BHMUymYhCyesb_ijcWa4ZnScftAQasXaDx7DnKZtFyRIMTDe-lb0QX7DSBBqNkRXlNIJpicq9_J5ODPucFpjyUrY2jHpKhyi5uFFeM2kpk6wq38V-3bbZQ5UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b182ff65f.mp4?token=I2Mg-CzRWJ6rcen84PqmZm6TgvuXDce5Xu1HB61UQYOHWqvB3ySmivNXlAB2JDSITSYCaWwlMycb_rHB4SnbR2u35JwPl56FzMmNCYFACzgrIlXBYsP6Aky9X8-RCNA6A4zCvA-LXB6Y2CjyUkFkHo2Ams4Aisg7fdmUKhwRal7wSHTJn_ivTRL8jZhN8lsDUHJlWsh8ig6gi2yaBDcJ80gycDpc8BHMUymYhCyesb_ijcWa4ZnScftAQasXaDx7DnKZtFyRIMTDe-lb0QX7DSBBqNkRXlNIJpicq9_J5ODPucFpjyUrY2jHpKhyi5uFFeM2kpk6wq38V-3bbZQ5UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: اگر شما می‌خواهید در ایران قیام کنند، آیا سازمان سیا را برای مسلح کردن ایرانی‌ها اعزام خواهید کرد؟  ترامپ شیطان زرد:
🔹
من نمی‌خواهم این را بگویم. گفتن این حرف مناسب نیست. #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/686740" target="_blank">📅 22:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686739">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2eb8ba8b4c.mp4?token=gM4tltGiUs9VjSsh9jK8b6bz7JMgrcQqpSnHg8rma8AqMFOJFjaFbVdihz6gV0UJ0t9whHRTLhEQjNyg2d9l0vY-vIb-ACebv5q48S02v0J_KTShWy_H8tlt6dbGWoKlH9wLvf1etKgFF8jtbaGHNzvSGb6igHhTWEPBJgiuXAMVJKB5ob_URtcONLAyFrHAk0DfWJPYTE-Nk5aguv85Ol2Ht59WRKNKlEDm4P2ON3paBTPw0VN_R0e7L1JpGZMWXrh44qd6CcWDmxJBxpJ2FGmEXJU2GJ74KBWV-uBkfvhPmxqn4EVHW9wPqipPr7iV25OVhxRfCLL4qK8FDIKLmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2eb8ba8b4c.mp4?token=gM4tltGiUs9VjSsh9jK8b6bz7JMgrcQqpSnHg8rma8AqMFOJFjaFbVdihz6gV0UJ0t9whHRTLhEQjNyg2d9l0vY-vIb-ACebv5q48S02v0J_KTShWy_H8tlt6dbGWoKlH9wLvf1etKgFF8jtbaGHNzvSGb6igHhTWEPBJgiuXAMVJKB5ob_URtcONLAyFrHAk0DfWJPYTE-Nk5aguv85Ol2Ht59WRKNKlEDm4P2ON3paBTPw0VN_R0e7L1JpGZMWXrh44qd6CcWDmxJBxpJ2FGmEXJU2GJ74KBWV-uBkfvhPmxqn4EVHW9wPqipPr7iV25OVhxRfCLL4qK8FDIKLmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: اگر شما می‌خواهید در ایران قیام کنند، آیا سازمان سیا را برای مسلح کردن ایرانی‌ها اعزام خواهید کرد؟
ترامپ شیطان زرد:
🔹
من نمی‌خواهم این را بگویم. گفتن این حرف مناسب نیست.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/686739" target="_blank">📅 22:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686738">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
مای‌دات، حامی مالکیت محتوا با استفاده از بلاک‌چین
🔹
در مراسم رونمایی از شبکه اجتماعی مای‌دات، بابک زنجانی با اشاره به اهمیت توجه به مالکیت تولیدکنندگان محتوا گفت: در حال حاضر اتفاقی که در رسانه رخ می‌دهد این است که محتوای تولیدشده توسط یک خبرنگار یا رسانه ممکن است توسط رسانه‌های دیگر بازنشر شود، بدون اینکه مالکیت و ارزش اقتصادی محتوای اولیه برای تولیدکننده آن حفظ شود.
🔹
او با اشاره به تجربه انتشار خبر دستگیری صدام حسین یادآوری کرد: زمانی که صدام حسین در عراق پیدا شد، نخستین خبر در یک خبرگزاری ایرانی منتشر شد؛ اما رسانه‌های دیگر آن خبر را دریافت و منتشر کردند و ارزش اقتصادی خبر برای ایران محقق نشد.
🔹
زنجانی ادامه داد: ما معتقدیم باید رسانه‌ای ایجاد شود که مالکیت ارزش محتوای تولیدشده در آن مشخص باشد. بر همین اساس، زیرساختی مبتنی بر بلاک‌چین طراحی شده تا مالکیت پست‌های منتشرشده به نام تولیدکننده آن ثبت شود.
🔹
مشروح این خبر را در سایت خبرفوری بخوانید:
https://www.khabarfoori.com/fa/tiny/news-3242267
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/686738" target="_blank">📅 22:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686737">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهای بانک | Hibank</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd0f51f783.mp4?token=TbebQAmye8kPi1b1CUog0gXBTU4VxNudPmSH33vjXNAA9P_t6HFx8RDBbuSfARE0PvwFToi1doMWqOGelcYvwBeHCElR_u_dYwHEn-W_8u33Yhuo9-Wz_H-mwrNfV6TzIz0ISj3OBgGr7W-DXDYvL2rFizzezU8BzDhoWEpCMOkFZW0ypBy8xRa1j9lTAraDl-Zlk0bUPB3nVdzWyAk_STkXwhFQC54_5LsZxpqgs6wgpvp-8-U0hkaG86e7XU1DOaqKyTFBEAsBQbH3D8hos3oI5zlQpZA7g7xuaB-BIZ-BkcgHHCJXaLwxcrka4YorrOTsuygmhnS9TG25QX2A2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd0f51f783.mp4?token=TbebQAmye8kPi1b1CUog0gXBTU4VxNudPmSH33vjXNAA9P_t6HFx8RDBbuSfARE0PvwFToi1doMWqOGelcYvwBeHCElR_u_dYwHEn-W_8u33Yhuo9-Wz_H-mwrNfV6TzIz0ISj3OBgGr7W-DXDYvL2rFizzezU8BzDhoWEpCMOkFZW0ypBy8xRa1j9lTAraDl-Zlk0bUPB3nVdzWyAk_STkXwhFQC54_5LsZxpqgs6wgpvp-8-U0hkaG86e7XU1DOaqKyTFBEAsBQbH3D8hos3oI5zlQpZA7g7xuaB-BIZ-BkcgHHCJXaLwxcrka4YorrOTsuygmhnS9TG25QX2A2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
می‌دونستی با خدمت جدید Hibank می‌تونی زودتر از موعد حقوق بگیری؟
⭕️
کارمندانی که حقوقشون به حساب
بانک کارآفرین
واریز میشه، میتونن در طول ماه بخشی از حقوقشون رو از Hibank به صورت
مساعده
دریافت کنن.
@Hibank_ir</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/686737" target="_blank">📅 22:39 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

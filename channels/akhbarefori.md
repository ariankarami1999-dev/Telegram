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
<img src="https://cdn4.telesco.pe/file/gmu0VEvnl7kkk6B3DNeqq3ZS-pldL5X1bIP7IpaMYvIuGHesme0UIMMNKxWBvnHo0VS_gDXoNGZt8PuR7wIdo-zNGnb8FBqQH-tOmqyeXzKkVHZgImNnHMbMGdvrVDMf2MS15TLYCDYfhQdY-ZFnqjZbwE71FJMg3hk0Grg_sTIIOl2uqOXHSAIA-1ai4yg2QiuC9u_hqnvIFb9i_u_2P13ju8RMktUp3Arg2N1dGg9uQUgMjYH_lkvHRLOGU5AEZcXLrg4D7K-xaijVA5his3rrIR_UwXB5lAW0oV9aRhhH6iZk4XQiHnfJw91B0kGgOAe0wpKJYTlNa0bJlclluA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.36M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 21:30:48</div>
<hr>

<div class="tg-post" id="msg-667108">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5NItlnBB_zSADIwZcRJ6hFd8VL9_1eqKmBM3HXineBrY-ZpFpCowizCb0H8Fsog9IYCucK3-9qmP5lmNDgCA1aektmM6m0inW58M0tLA6DteQgLzg6ShHU_JI8pHzuoGeh1waW4_a2DNiZqeLj3t3VBj1FzLLos1h0xsamzlEJG6yVRbtIdQkF5gKKOpipfRmg-4Lq-XRFol36abZuoRESTPaYVJC_HGBw01L0DVIVCsZ5NEqWjWXK1681-cECcbMKnilb9-qUStl-6ffIt9CFKbToiWes6aZh6m3RWb6hgS025AEVx-zMatynhIf-k8zbH59bLTf4ZUxk7LC1_zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اللهم انا لا نعلم منه الا خیرا
🔹
مردم عزادار و سوگوار ایران امروز با حضوری گسترده و آکنده از اندوه، در آیین اقامه نماز بر پیکر رهبر شهید و عزیز امت شرکت کردند. این مراسم در فضایی سرشار از معنویت، وحدت و وفاداری برگزار شد و حاضران با اقامه نماز، ضمن وداع با این شخصیت برجسته، بار دیگر بر آرمان‌ها و مسیر او تأکید کردند. حضور پرشور اقشار مختلف مردم، جلوه‌ای از همبستگی ملی و احترام عمیق به مقام شهید را به نمایش گذاشت و این آیین را به یکی از ماندگارترین صحنه‌های بدرقه رهبر شهید در حافظه تاریخی کشور تبدیل کرد.
🔹
هفتصدونودودومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/akhbarefori/667108" target="_blank">📅 21:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667107">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
قالیباف: آمادگی برای جنگ، شرط مذاکره قدرتمند است
رئیس مجلس:
🔹
تا زمانی که برای جنگ و شهادت آماده نباشیم، دیپلماسی قدرتمندی نخواهیم داشت؛ چرا که دشمنان با کوچک‌ترین نشانه‌ای از سستی، به جنگ روی می‌آورند.
🔹
وی همچنین بر لزوم همکاری کشورهای اسلامی برای خروج از سیطره آمریکا و اسرائیل جهت تأمین امنیت و اقتصاد منطقه تأکید کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/akhbarefori/667107" target="_blank">📅 21:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667106">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده مجلس از حضور ۱۰ میلیون نفر در نماز رهبر شهید انقلاب خبر داد
جواد حسینی‌کیا، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
تاکنون در تاریخ اسلام سابقه نداشته است که ده میلیون نفر همزمان در یکجا نماز برگزار کنند و این بزرگترین نماز جماعت تاریخ است.
🔹
به دنبال ثبت رسمی تشییع رهبر انقلاب در تقویم رسمی هستیم که با باز شدن مجلس پیگیر این موضوع خواهیم بود.
#بدرقه_یار
@TV_Fori</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/akhbarefori/667106" target="_blank">📅 21:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667103">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnQjLeM-4QsLOxpFmEE3glWBnsRLHKFPdBjGq4_UoTYEPCeZ9UTdHjlVtX4CXg-yZxYAcE_zAMixb7RmwR6O5CfoCFE7TrPYWw6zhQfMNEPCPFpWWJd3M3RuRWPm8GNy62pv860o_TmQCHMPeP94ApNsQwo0TcQuA1qGHe1rKro8VVFUyXrdNvZXo2ci_tA4Wmi9irzrfk6-3z00uGrROi2V7YvpWesFMuDn-rhfMxAPKBAZtlc3ZagxyeEl2uhC-AfOrbylGDFpJYhEhDgMG8RHi-Z1b-IGCWj_xoieCLp4jX1c-daS6rtWd7MloTVbI4767Sqy5lmRxti7KsX-Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
پویش ملی «آخرین دیدار»
🔻
جهت ثبتِ تاریخی وداع با رهبر شهیدمان، از کلیه علاقمندان دعوت می‌شود روایت‌های خود (عکس، فیلم و دلنوشته) را به شناسه زیر ارسال نمایند.
📬
شناسه ارسال آثار:
@akharindidar_admin
🎁
هدایا: شرکت در قرعه‌کشی ۲۰۰ جایزه نقدی + بازنشر آثار منتخب در صفحات رسمی پویش.
🇮🇷
آخرین دیدار در بدرقه آقای شهید ایران
@akharindidar_ir</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/akhbarefori/667103" target="_blank">📅 21:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667102">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
فراخوان مقاومت عراق برای تشییع رهبر شهید
🔹
ابو الاء الولائی با دعوت از مردم عراق برای حضور در مراسم تشییع، آن را ادای دینی اخلاقی به حامی همیشگی ملت‌های منطقه دانست؛ وی تأکید کرد گام برداشتن در این مراسم، پیمودن مسیر تمامی شهدای راه حق است.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/akhbarefori/667102" target="_blank">📅 21:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667092">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X7HrCaDp0EfkSoyc9Mlb7oRLueh1eWnvo8ErYHlTioZgP9H1drdOl_kW3Yo16l2wh_khQjoNxXdR5UovNi4ND7m79gniKi5p2iwArtZMQRaKdbxoa-ACfT6aZWWO8RwH7vjWjvaL63lJP_ZAZvL7p19su-DKm-ARCmQQTVXXepEIhiUtTMg4Vxg73SNl7T16_AFhI7MAyAwugpUrdV5Oq2hlRUKvg2JPDc4olLW4NICj6I7iKx3ael44hQ0Xq0V6wdhLMcM_rGa7mBOCMCxg_KA9SS7WrDxKotwt83xhRlqRucT0UID9MJbZXRaWU5GYRMQEVWfST0t6YAOB7SkRkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dv6xms9hTsFp6S7gLMyQZlEo04KGmQkZXgPNEsvPkw7c0gPo4iCa59fXvI-YAnd8fsZd2SGYgk1nqG99qXpf2B0NILocoiWyssvWl0o5OXFwg17haeiAftHT8SvnEFMMHana-HKPGUau93kcJP8SoA3eOR2iEftnkuClAsnDsFq7akP00DJgNRTDTZZ8Rd7FUSBuc7VMVq8uxvfyZiivN5gQiUUjzSOjLDaD0GpOikr9OD9zgjF0aCQplz3U1o8vcBzlVpuGzGfHnQD1uRBVLYQkBZiozeJ0KC5oZ47QgnbmjsFtUJXfSFbN7Dapa10opecVGcERrZDrtvlw-tN9uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YESQLgquApgR5Nous6mr9m-Q1gHhqZqNSvu6osc8t8iKEdJ7_BCSZyuVc8ClkMOzkQYnVoYAojyrq7a2HDdxpOLIvuuw77aD1bSjK5G1-HY8wf8MTKNNcVKMOFlNRVO9kB4SLxG247w1VSVy9gz1xZJK6k911C4OQEaT4_r4KYsuNOO1WLO-hvxPPMZ5XMRgAD2HYHHuTj9mtNrGYxQpMLNGXJTB9XqqCE9tVd0QFofzjKnfNrZ_BQzx4xbOWxoeVqgOu8ikmZW4ZBD8YTCCnpUR24jzbBc2WH9JqSAdv3B6G2k3FCf0dwo7JoEE5AY0TSyTD5YZH5uJSdlaLI2z2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OA4eiEI7KkJaiNMaViJ0H08H_EzyGch0fntl3bbZrDAZTHvZ-TLrq_ccm6NfQqYOVQcqg9fjWasaILKGxYHTEzAXrwGxCtg9z7u-Zr76RbxfZrBz6g_y1XyS7GN4M-0EenGuEwvdj2E3j9VTcal0r535C5JV5lDG0TjOzJpzYaPuGG2w8S4H9L1f31p6FJXNrZEzdAQNvJxeuHIUr-QE3Qkety-nhE0uD4DhFlKFv1egrOL19SrJghYo_STCn4A303o1KS7jeEHP00WB2nVByOGjpZkVbORF88dobdf2MK7YG37NCu376AzKWoWMn3IlToaUnnKwGIU-WciRSDR7RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HzwXcI3-7wzAvk7qN1NCs8dnb5i6MHweBGyEA6stCH0X6XdWAT3j43UVbN0ZJxaTLIUrp9ACVtg3E-JKM0Eo94pAXJKd78NqwrTk095NhErIT_SMVRja8juCd43L1KHtGj7Hyiy5IRAblnADZpaW2A6mFXw6r-8ngqUGZeVT-vW13AfOjjvpPyMZVcFn0UuSBP0RZdkGSRv2trlazjwVL5t-uyhWb-EE42SFPM7j_OSNwX3-wIlg3PKqn6z9BGINBatlOHlNegXUsanesx2ApVgpJRulZ6fEh7Ec1BjSAIa7CydlnGpn19rX_GPmXsiMB1SsnGF7ds6pg1bnPleSvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RCQ1q8tXzPKshW9BrwjQhVLARZiyemsnErU-EoxWQv__bAyLCx5ALE5RFUiU_UbNGWmonxqkFsrgCVwINzwIMfMmkwuMS2gFuqF7wazyzFaAEsEIBFZGGJSQEx1XMZTsg7A9x-vzAb0KmbuPPVZr2S6OQet-tuueMoupkCaE2vSNpG7VITIMqJ-2N1jdA0BtNyjrc2_2LeYGpP36yYuZ0vemL2vG4qLtCey8dH6_M8YpwV-23JyZK0n347PzZHrxwoHCqBGbJnx6VEw9fqZ8-H4vtrUXAUSWi_lvkynkJgd6GWw-wfkUF0iHVBZUSm0Hk9HgrDuGu3NcvTIJpCSgjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kxjy7Xvo2uf550qR_ZqQw8xdh7bt7TuTAP7UlcZPCHwfYCMKKqaLHcmlAKUlpF0gZ88G2zpGz-EGfEMD6yJKLYFacw4l7eDLOO85M2yUi9uiGEk6J_sXHwdKYRRhpi2nlDAEdZlEe_zswi_n0A-O9Pm3ooYYcEmIgmqQgicZVp8xQbktjDLtbao4enfp3euyX-kl-8rjfY5BTJNk15b__Z02TNprZCBLzPpAiponoDWuAhvS_lK6yJ6idQv8AJoCEjkdf6WiP_IsIe0I_8xeqOBq_o_97TDjfkS0PX6XX5dxb2c3w3scIzPNs0gg8SfV590FNE61MWxrAVoHM-nO6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rMmDXwbrEN4VAk1KMAVfzHp3uQJ0aPERbNOAHjYQ1eF7F-5_w37gx6cKXRxZkmC18_EFA3HEFkfE2pp8l4bNL-MoDl63OXAj0z5ZfsKBkxQDPeNZBPS6OFt7dYvM9YPfvILmLUfOiP4PfC-GtLQiO0Zu56Np0zduKBSe3HKtDx9aio_bTkNpetPBPHUbZOfWftuPDvP7OKhAN77AxoGIGVVt7Az6oGpua2nk7ZQd9GuDS-8OYSDK_47N2vpxHMMuQtU_Tvtoil4c0YQ-KDACxs-m0VNHw085uPJO5Gf044B37hYPk7-lXaiiWabKszn9J39zQJ5EYj2kTslO3inCdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vWfAkacIAdto6vw9CJrows7PM1fchVbtERt2aui-AJC3Vrx4H_DA5fqKCtzvsB5PctCaGOYk62mcgjf9eSpMOOuC2r7U6nMjNCTDnWGCFfZvuH5xWkDPD2O6LFhOeNrJ9rXLhM7soPTLRdQ0fxXeunK1lv-49BQEIxi94SyvBWC3YxUSFEsDOyiBNNL8xKgS2mdPZ8OgZAT5My_-10oRdtsRTV7uwCUk5VqxNqQZ-m6VvAyjdLLgROnH5GUrG53vkX4To86HNlSCcW8SvwWt5VXTifIEKRZMp7us4BLiLdKliER_ntwaXLHH3mzvhR-m9Q7YgOy4TRCpYnqGyYDDCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cj1tH7KDW04IhzTk--6pe_bj05m15-mOBXVagGoHsSGH3D3dN6Xm0S4wMHmQkaFqZ1PeEFvuKP57hVqkSTz9OoDMDEv8fMhvpfXplNDwRrjVliaoiqWTpVhJyiJEHO9T1SaT1EVYosXtO3u5b5sGBkz1Z-T1QLJHLpveE3d9LgXpfxxwB2N-idNeMvIhAmtnUezT5q8dxaFc37W_2NO1jRDH35JL3Zi8oz93DfdnYZAr6pC_ocDh1Fe1GTugpnvtzVoL86pp4N8P_PLwTgO86l60yPBHKTaNziXngoFRhVTeGXhmFbWLRmP_NLaIjZM--4-zVCicdteWFZxTCCIp9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر خبرفوری از دومین روز مراسم وداع با رهبر شهید
🔹
عکاس: فهیمه فرخی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/akhbarefori/667092" target="_blank">📅 21:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667091">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WewQLNVlWE_o1h7klW89EuMF-s2iO07F8fvalUHwgY2J-M9Fy6i92syDqyRwGWwxAsxKrbFq88GhsBOEVzVXv-JkTcEOeYnqWRtKtY8J5Ev8G2z5Z48pPNj-q27i753NcDg0hLlTbes2wJRJFrBDEwlVDZmT9l6pY_johoFE8etv-ZCOp8-DTbLhQ5VtCulHIW6Yb1NfebTN0P4vDJ0DwGl1cvgoudJnRvX9LjtCVsMtOsLuKgSaLA9odmM3ejYNTt9U4c7o17D9Gnw0v0d5z4AK9T32ZO6FeRXZL7mPbypUJHQRKUTEiHgnH6-XGxz_0i46TkJd_Ve4OvGgudDe4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معرفی مستند: روایت رهبری
🔹
«روایت رهبری» مستندی است که با انتشار تصاویر آرشیوی کمتر دیده‌شده، روند انتخاب حضرت آیت‌الله خامنه‌ای به رهبری انقلاب را بازگو می‌کند. این اثر با بررسی جلسات تاریخی مجلس خبرگان، استعفای آیت‌الله منتظری، نقش امام خمینی(ره) و مبانی…</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/akhbarefori/667091" target="_blank">📅 21:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667090">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CAIRRxuDovesg__AQ-tcl0ZarHanp3fSdbpigkovRlN3gDpwnZT8o-bkHgYfKE_kVkmWLOEuN38MdBi2t7tUt7RFI3bwLKe3UNMNR118TLjs33abbNmve_faaZrqS6cwjgVyRUNW7mh6wIJcr-ieRD_qoy98TxMNnHzY9DR8Crj46tJuwdGVJ0yBZC4EqP-_4cD2AODqFVbkCyoUYH0YHrjAIZA6yN2DGEqQN8KqDrowSTvTwEaNoxmokdHq2H01EOpZe0TvqnopdY-Ird1rXr-SutJNraRMNM_CoV_0M9jpf9OUDsk63LFffhiUz2a3cWoaGq1pXMbU9h5phWhwjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ از فیفا به خاطر بخشش کارت قرمز بازیکن آمریکا تشکر کرد!
#جام_تایم۲۶
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/667090" target="_blank">📅 21:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667089">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
زائر خوزستانی مصلای تهران خطاب به رهبر شهید: شما همه‌چیز تمام بودید و با اسم شهید نام‌تان کامل‌تر شد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/667089" target="_blank">📅 20:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667088">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b921d180d.mp4?token=vqMquJsn5grQVW3crd4zyRSpjEny_zsCDz6Bz0-il2uu1n-CnWzh-aK-GOAJvEvettV7LfVbnoP8GvGNooCYWE70TLzIAw6hBF2eZKAGxSEBwo_muDDUiHxm5arltIjEoZtCzJ8YwtLnOZEe4RDLPhyf6kPmYXkq08zIIbabxztxndxSSGAZntYQwOj1xn-rBb0ySVoEdMGzM6sYig1r_Bf0C8sQvH_zjHlxALwhaB63sLeYLRnDzuOGoKM9kE0rHB0dKKll8nSsafzg5q_Tc_BprtVjyJ_5QPKdiVzmDJTQSgtpn164E1ntP1x7YOkBpmKt1qB-6E9m7XXzvkLNFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b921d180d.mp4?token=vqMquJsn5grQVW3crd4zyRSpjEny_zsCDz6Bz0-il2uu1n-CnWzh-aK-GOAJvEvettV7LfVbnoP8GvGNooCYWE70TLzIAw6hBF2eZKAGxSEBwo_muDDUiHxm5arltIjEoZtCzJ8YwtLnOZEe4RDLPhyf6kPmYXkq08zIIbabxztxndxSSGAZntYQwOj1xn-rBb0ySVoEdMGzM6sYig1r_Bf0C8sQvH_zjHlxALwhaB63sLeYLRnDzuOGoKM9kE0rHB0dKKll8nSsafzg5q_Tc_BprtVjyJ_5QPKdiVzmDJTQSgtpn164E1ntP1x7YOkBpmKt1qB-6E9m7XXzvkLNFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اژه‌ای: همۀ خسارتمان را می‌گیریم و جنایتکاران را رها نمی‌کنیم
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/667088" target="_blank">📅 20:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667087">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
زائر لبنانی مراسم وداع با قائد شهید: برادرانم در راه مبارزه با  رژیم صهیونی شهید شدند؛ من هم گوش به فرمان رهبرم
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/667087" target="_blank">📅 20:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667085">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c44794ffef.mp4?token=CPYaRwWbMp5YlSm4kv6sVgsT9Cm43XUIqtW5GtIM1KbZFwtTsAiIUH0kJIPBnD4Fk9RPk3c5lE-i6ie9Kdxa39baalGSar9yp5hfyDmXoQKJ4Wmq3lrKznuOYmQw57eN41lwH7Z2TZ25yRi_7CjCjkA5s-8n35W-I1NHAENj2-Ve3oyjBARvT1QGcL46s9szT6437T4kQv_wa4S4th9PElnHeOJKlrMnkbyowzAeE16RN9177qPPq-tVotPWAarmsvHgvrEgmo5GlovD0Pk9Sy9dJk6orTksXxoRwVUUtnYQznbkDka4a97bZ2_UD7Mu33dErKNkiZk8ZUBQEo3aQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c44794ffef.mp4?token=CPYaRwWbMp5YlSm4kv6sVgsT9Cm43XUIqtW5GtIM1KbZFwtTsAiIUH0kJIPBnD4Fk9RPk3c5lE-i6ie9Kdxa39baalGSar9yp5hfyDmXoQKJ4Wmq3lrKznuOYmQw57eN41lwH7Z2TZ25yRi_7CjCjkA5s-8n35W-I1NHAENj2-Ve3oyjBARvT1QGcL46s9szT6437T4kQv_wa4S4th9PElnHeOJKlrMnkbyowzAeE16RN9177qPPq-tVotPWAarmsvHgvrEgmo5GlovD0Pk9Sy9dJk6orTksXxoRwVUUtnYQznbkDka4a97bZ2_UD7Mu33dErKNkiZk8ZUBQEo3aQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی گسترده در مجتمع تجاری در خیابان الظلالِ بغداد
🔹
به گفته برخی رسانه‌های عراقی چند کارگر در داخل ساختمان‌ها گیر افتاده‌اند و تلاش برای نجات آنها ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/667085" target="_blank">📅 20:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667084">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
از شکار بی‌رحمانه تا تحول بزرگ؛ تجربه نزدیک به مرگ یک شکارچی
🔹
00:07:00 در شکار به هیچ موجودی رحم نمی‌کردم
🔹
00:19:00 علت گریه نوزاد در هنگام متولد شدن
🔹
00:21:50 معتقد نبودن به نماز و گوش دادن به موسیقی شاد در روز عاشورا
🔹
00:29:00 رؤیت افراد جهنمی با بدن انسانی اما چهره حیوانی
🔹
00:34:00 مذمت شکار در دین برای تفریح
🔹
00:35:50 تغییرات رفتاری محسوس بعد از تجربه نزدیک به مرگ
🔹
00:44:00 متوسل شدن همسر به امام رضا(ع) در میان قطع امید شدن پزشکان
🔹
00:50:20 تطابق رؤیت‌های روح در حالت کما با واقعیت در بیمارستان
🔹
قسمت بیست‌وهشتم (شکار)، فصل چهارم
🔹
#تجربه‌گر
: محسن حسنوند
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/667084" target="_blank">📅 20:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667083">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
محسنی اژه‌ای: در برابر قاتلان آمریکایی و صهیونیستی کوتاه نمی‌آییم
🔹
محسنی اژه‌ای با تأکید بر حمایت ایران از هرگونه قیام علیه ظالمان، تصریح کرد که ایران در میدان دیپلماسی نیز رویکردی آفندی و مطالبه‌گر خواهد داشت.
🔹
وی با اشاره به روحیه شهادت‌طلبانه ملت ایران افزود: «مردم ما عزادارند، اما ماتم‌زده نیستند.»
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/667083" target="_blank">📅 20:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667078">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g_BNYgIK8Z6WIAGN1D420uey2jxMFzuxvtNvntkGo4tKx0zwku6MmPHWFTNCwY5riQNcDIciD9FWsayFAz5RydAUjz3tLaZBtFMJjkN3Qfapt9yzy1P7WGnFQqO2ESb9PpCNn60hXsjxIA7Cuf34hWQdZNNaETVrj9MEZvS5Hp3Z2D4H0XbixfMkRrgAE7YCTkq2hNr3ENdD-5LuOW4s_z69KkD88T6Oiz_BYhjQs7H2XZhu6EVFrSxEagB34sN8tt7BBJuDHqngO8gxRvFx_XGTmkFQ4aY11AfobsURlpdqVNRSlGHhfOz0hJoz1q1fOunSfrpum-PFM9m90l5CGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jk3nrxqQ9742KpYIlkiCmNQvUFCJ-UkejFq1obTvZxutPROZjLIyj_QDpRt1-X38kzjB9lkPXAe0x92DAmcbHfBbQs52DXwzs2Razp0PZyujjZDo_6CFxfaPPytoqOV4GCjfJ7sTmOk_gKMtHv7lDkARYrVEHuNhLCDK3Ox5DKFls1wygF-iUbzdXSTJBjzhlOzLkyJAQzCA6hwtng3WexmnqnreOmY7emHsmwyPILkUBB6D5d3YdvNhgeNCoACqmIkKvogmmk-ToTl0GhbeDp-ijxPeDpQsMYtrAUIqTsB3sPHZW1u8IOPJpbZ7aWsk8bOR46fpu907xrjQsh1vKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aL9-gteGjMURqgRqgPmIMYU846Vj7x1UPujB4vOOj0zEp6BAFipBlVgofTJSPcJJrkh8OBTgL4ROjPES-yWSOYn0r7nEOXKWrvb4a4LDIRreh6HwsPfEe5e8qcHe5JIGwfYmH7OUs2c-niAdfhbWNKX0Mdb3-KAnRuV-pKSlOfzTYU5s_pBChsAAHIOPnksXHEu9zqdNzLl6fzQ5DW2OkN_2jhBSFPr68vAmYhIvdyaE8FeQbcruNUp6048ocWquLwb3yRtRj_GqWmX6XJ0MJDA4DqqFsKlG6jRTBeg6bHJ3E_rpHMSrUh2vWBSGImuS4QkahHJlgTjG5CxgMqHwDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JTJsV0BH6BNoXpmqzOQ2PKa1tM0vJZTg_S6geHk2z9edq7p3t1EmqJQ7ECwWpI9Do39HCU8BQ1SyZmlwJnlw_R2jFdS6OuCGSU2Di6EMSTRz9uanAB7eLc62tj27qCxvwz4Z2joFYXkKaZ2z11x-nrLmfcBWA1fqSrSFvefBvaa2l5G_XaMR3zRQfELxcYjYYEyzv7Ztq8jSooq9GIw8FKdd4Hz40OBEKPAS1pqgPH8llDpEAhuk_x2RZj0RWF8Dlp60guhRS2j0KULd99Vk5_r2TRGZ77jRhztcb7mxg4GBbW5Ywl7ZuM5Bp3EfQo8AR8i9ILVkQbmfKOrKBqZYYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NcRc3kbm_McYUi9USLmW4NUcoNV0CarBFxgP2dZ-T-ixgPKplNfNaZO_9BuJ23MGEikelbRIlR6PtCdiWN3OjWVyz5e64kX-qRqR_A2xf9mgkLj2HO3fyO9JeSfiDE8O3T2WrQRvWkq-CN-VSbhEn9O6L39hFTedyMp1LEOXgN12ZdSgAuHwhaWSczvVQtcnhgV7CSXSHZFeMnR74VVT-uQQ7e7k0MuUwQyhW9SYS-NSki6Brz4GJjyqWDMmjq9n5K2kcJoT7AXKug3C2B2YsK0BEsYqwsQ0ejGlc6CrrnKsdBOoeE7AGXZDO4K4naVEBgcMnlq2eirPkuSUzdNANw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر خبرفوری از مراسم وداع با پیکر رهبر شهید در مصلای تهران
🔹
عکاس: محمد اکبرپور
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/667078" target="_blank">📅 20:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667077">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7582d67ba.mp4?token=aJGeaSGNvQQpFt3xWrtdsxUDrpSFoL8lnw2lgfgL5Ko3JvrA_yFg7vG7mIZn8u8SZhuWS5XPQ7F8crODa9REgOYb2_i2LvxcIysvg7PciY8MewPDCwNIpSA7Am9MwutvS8HvdPypTGmHqvpBN6jxkBh5KJfdJH2OXmvdMvVDriEqcvsr3I2DWkFOH45jKRGcTV7arJAThNrusQu9LICbVrONy8Dy401Kit7t4soFknnSKaIZuAiTDIC32LnbYYmY1k0or5A_cS9ajhEKjGxTeVt6xWJMpcmg_Ncwu4PtpRkgUwBqFARuuIFLzZRyORJbLqN94sTnyAelau-ArPd_0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7582d67ba.mp4?token=aJGeaSGNvQQpFt3xWrtdsxUDrpSFoL8lnw2lgfgL5Ko3JvrA_yFg7vG7mIZn8u8SZhuWS5XPQ7F8crODa9REgOYb2_i2LvxcIysvg7PciY8MewPDCwNIpSA7Am9MwutvS8HvdPypTGmHqvpBN6jxkBh5KJfdJH2OXmvdMvVDriEqcvsr3I2DWkFOH45jKRGcTV7arJAThNrusQu9LICbVrONy8Dy401Kit7t4soFknnSKaIZuAiTDIC32LnbYYmY1k0or5A_cS9ajhEKjGxTeVt6xWJMpcmg_Ncwu4PtpRkgUwBqFARuuIFLzZRyORJbLqN94sTnyAelau-ArPd_0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
متروی مصلی مملو از جمعیت است
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/667077" target="_blank">📅 20:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667076">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ci4o36cVBJdLNEqiLnYvT4B1r-QmlWIjSJSBs8SZVW-yEffMMudpuyNZsDV_Z-ko5wC4F1eajInuo4E82fga5No7xbhccW3Qrk-Jfng9tyTz1Cv2oM0p3ZNb-__Bw6klRC8Wqo22ccqptEK3V9Avhp1VjiXGKvtX7Bzaibsnd-VhicaLDIF5PTjLDyoFzxuvGI2OwjgbhsXkrHoXBviU7Y3sQCoeQRTAsq4_9WDC9WkzG9nAYBe75KNVWiQ6jvhatmFfQFUVynt-9wcC7AxYMN4hG43MhwN0XGqJUhSmpM_LcAkEr9UhvfBGYgNh0dnmn8q2eqSd_h3-LmKEUbqCiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استاد دانشگاه شیکاگو: ایران؛ قدرت نوظهور منطقه
رابرت ای. پاپ، استاد علوم سیاسی:
🔹
وحدت میلیونی مردم در وداع با رهبر شهید نتیجه اقدامات خصمانه ترامپ است؛ ایران اکنون قدرت نوظهور منطقه است و به‌سادگی از تنگه هرمز عقب‌نشینی نخواهد کرد.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/667076" target="_blank">📅 20:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667075">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17080c3f19.mp4?token=ODKnY10TN5XzvZw75yNbs0S8Hj9o13y7yFxnfFOTiLVPfoNdfCZ4HlWMZFMhdk7GZGK-PHDl3EwWWpj8VCKkS6DQz5gWPqNmzHCs5fUBZEpAXUz0bdoPQq5QM6vFCSJGK0Vm7EbD5DUxn8DHDPu6yq-DX1Lqdl-jcjMPWbU7Byb0XcEIN2lrTObljL_vpEdEJPdssHdwW80rFP_NNH9U7DgAWTCSDDHVAPeMjkiaJUYsxOHIEM--wxJbzKiBKB4fk2ijQeqzsTNV0mV6eVt1E1CfSiL7ODWh61YCW30QCVA9ecSQgMe9dq5l3QCNtSpdUwVHREd8VT0hQaPmgQj_hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17080c3f19.mp4?token=ODKnY10TN5XzvZw75yNbs0S8Hj9o13y7yFxnfFOTiLVPfoNdfCZ4HlWMZFMhdk7GZGK-PHDl3EwWWpj8VCKkS6DQz5gWPqNmzHCs5fUBZEpAXUz0bdoPQq5QM6vFCSJGK0Vm7EbD5DUxn8DHDPu6yq-DX1Lqdl-jcjMPWbU7Byb0XcEIN2lrTObljL_vpEdEJPdssHdwW80rFP_NNH9U7DgAWTCSDDHVAPeMjkiaJUYsxOHIEM--wxJbzKiBKB4fk2ijQeqzsTNV0mV6eVt1E1CfSiL7ODWh61YCW30QCVA9ecSQgMe9dq5l3QCNtSpdUwVHREd8VT0hQaPmgQj_hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شاید آخرین غروبی که تهران میزبان آقای شهیدمان است...
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/667075" target="_blank">📅 20:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667069">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P-yVQBRKnDZ2dTnr2AMxLisAPbpcRQf43XGlNqSdqkqxuBUAmX5TmTC1dC3tCToxcUmnebxaMbLXSBQIAT5_SaAVucAAHUbAL8pE-wFFR93za95hecIPw70_x1cHFH1g7spLc2BLm9eJvEhO5-eU5Y53-IpfeRRIpaN6J7QBtHv1uPOlqvfjlecLYi-RLiyP3pEqfG4zMRh9EzKS8kUeX8o-8iU15svE06won0uMOdPePwP63NQ5CJiIJLmpqXcVgAVj9ovVIcNnBq8YbrOqIKVMXOqfYpfa1AnZrr-jk6FDP72b96IGxctSUBOAhd7iEWwvjZDBsvYiMzD2CtJw3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vQIQoz2a2uCR0twqTOtJJWGs5r7MoA73pxaMAgRk-WtYQFgUpVg4rw3_aVk89mwjiq1SygmZdT2qfYe1f-F4chzXGrAwEhj7PcLwQPtFPht-ZaSlf6Ntb7qfD45p1H51r6moPHOYE4l9a2_rKVFGZQjsuaLIkbfwYCpEenOWYYHs-7HKg_WA7fOrv3Sm3WyH_4ues_5tWBf8KgseEziZzhRg989Rpz7ceBkn_kFtoJTTKVd4xfBBA9eVPDRH9R4MOKwIpylFooTA8JC6o_mm8dVeTi1BfSxQ9iC6fEa_btEScHakh_lydjRYpX_vxmH5X61jgswolT843842NMaa2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oEwoTtr_Ep35gjpOcOn3wAF7olJQGRf6uaRd1WWr1XxyhBtyKsXE9p3E702YrJlZVcTV4cixANDN7HCpae3xQFJAOgowmvdCJbo2pFe4xk7j3bmG0ULI4LqA5Mbn-rES4ghl1HObsMZIxMBDJVoAqlT2tvscizlsixil8gS17XkeHDH7NdHMWOdpofIyv154xA3pjLpVKOV7-FN4-bSpqJKo29aFbqE-Jk4q-Dq40wMq9wdUvdRThoTClxBF1MJFBqykoWjQ421HWSnnExYo8-cTil-AuSeRb0BfexMg-TK3EBh1spdGhyfKq6A0QtH6Gs-sjlic7us7ALQgKhg48A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j2PQvUssRZZgoSumdVH9Gh5IGAyDPdrRQJY0dpMAUuLEQVguDm68uYLY_F6wBCOU0FBOKNlh3to973V_cVaNhF_yJ6CWvZ0LgWFyBe5mptD13rZjFgj5VG6IA2ysAXKru4OvZFQt1zJn0AOBX2ZVQGgslAOciA8EbBEj0NhkTdGrUbuYC8L4kc6q4aMx6yVKWPypbbzLVYMkaeUJq-pM0QceQtpw6XF--VKVezyOiq23EroRPeiWWXtpTFoTY5sRtdGGa-GHoqRZ2TCz-VgTppregucbIGuMosKWh8nX0H7x6yU8eDY-HUWomVze5ixUEw1knVTRRR5r0bz2g9Q1eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SsjwYdXnfIkLY_itaWqE63DJ58Smjl8g2vFfe7eeT5mDJuy0aR_vdWMzr696GxvopWjUlNh5lqNwgJIxzXRcschzRnRyP7jZU1k_u1gsJZz_x9ZL6oMOxK-ejljKo_r6Fu4Lxu--2iwdgAczFXI5MtpttYIUw2q1pSijGyubM5H7HihjfU6qgxM86DTu0XuKf6ussZrZkOXKPN-NSuFjoWTCeuMeb8jyuytZ43nbg_bIZXqIJP1LNybIHRjsmgz7GUGdTetJoTV8JnhKFb1H_hXx7oVOu0v-zNOsyy9W-feqIhqTcNk9LAObsYj6hUELV-84iH60CLrZR96EptbYQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J337SwnUtKY-pY5Ju4OaW21N__daxoQ8ff9oens7eHOtP_KexwXjtIoCuFpVf2ADo3Acf7pl0-a7uDH4Fx-gJpjEsN_zxvsaNfNtapnpcWpK0Vy-gw4tvE0K1PnGjgt0YnZ1_5SlOBTGx19FKUC1Wlo9CdsncKa4aiK7_0cz_zVl_4bo4n75aE-PrGPaekRI6_kJwSXZl24GPNFu79FCqbJauU2b1EwZg6ecKKj3F8UYUjdLeWB5SJF_84O5iTV8f5RPAUq8CeWwz9PGxt5gY-BbKnCbSiUxLijkbJjyslR-0KIkrqr-hURRSU1NIcfUsRZdkbplvcUOaHxcwuyANw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پویش مچ‌بند سرخ
🔹
قاب‌هایی از حضور مردم با مچ‌بند سرخ؛ نمادی از عهد، وفاداری و خون‌خواهی امام شهید و نایب صاحب‌الزمان(عج).
🔹
این روایت همچنان ادامه دارد...
🔸
شما هم تصاویر خود با مچ‌بند سرخ را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/667069" target="_blank">📅 20:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667068">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🏆
آخرین اخبار و حواشی جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/667068" target="_blank">📅 20:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667067">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4732a72aac.mp4?token=mOCjbLV8cUC1XKMpdAuDm76SJhFgR1Cyq2ptAaNrz-T52h8trVPg3IYa614iqqyWie38q-JOLh58J9M1SXmt-0UWOpP-EbUMj_IGSbK5yodtpDdAOZXXFQd9IdWPwGGLBVlaf2-yk47ZcEUxw68IzycNoQ4GNfW6QE_7TEck9fJ_mJq3y21lqd_86rBm3p-GgX2f1DSJEZHLYaV143L2gdD9u_rce69N9mD8tzySanPNX2snaTu2Z9Jy0LGDDKlJxcfGidVPC0xZ0skmhxdB6Cp4FENH6XbCVHHpDUWmji9P2E4aCIDd6RW3dCVE5Q7YBGZCPqmp9lo7uAtM4IuHXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4732a72aac.mp4?token=mOCjbLV8cUC1XKMpdAuDm76SJhFgR1Cyq2ptAaNrz-T52h8trVPg3IYa614iqqyWie38q-JOLh58J9M1SXmt-0UWOpP-EbUMj_IGSbK5yodtpDdAOZXXFQd9IdWPwGGLBVlaf2-yk47ZcEUxw68IzycNoQ4GNfW6QE_7TEck9fJ_mJq3y21lqd_86rBm3p-GgX2f1DSJEZHLYaV143L2gdD9u_rce69N9mD8tzySanPNX2snaTu2Z9Jy0LGDDKlJxcfGidVPC0xZ0skmhxdB6Cp4FENH6XbCVHHpDUWmji9P2E4aCIDd6RW3dCVE5Q7YBGZCPqmp9lo7uAtM4IuHXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هواپیمایی در رودخانه ایست در نیویورک سقوط کرد
🔹
پلیس اعلام کرد که سرنشینان این هواپیما نجات یافته‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/667067" target="_blank">📅 20:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667066">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3Gnpe-HNzGFJnWYkyyvXMe4fUnulJUokffeRhUWHLpHpjyTMNMg1yq1fNyT2dXFo4D6sxoLH4-eBbrPE6iC3qBq77Fq9sAGH8OeaFFvfH5YzClRNCaaYYOLj_vcsePnCCG0G0_M4vYxOZoJUuluu2HAr4ygyIY3RvIifeND0gWqxN6vDXOye27EOW2iLsT8kkqOT7OtWJktKcGENrj-QMrGwOmhiToRJzoZqnFa7qLM-lqgElITLmwKHKZwP7hUoZ3zmwL3JZtnC6XOYpsUyv3gplLuyahZNXZRQRS1xtQ36ezzwAdJQGowU6WPkcTAm-g9nC_wCf7pS8-RQV49bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ننگا بما اگر که ز خونت گذر کنیم!
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/667066" target="_blank">📅 20:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667065">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/165b8123ee.mp4?token=QJKfR3lLVyf_02ijbHQUE3uvDUKe1YLMJW_MnhZjr4Zy28VulInLiDI9eqhZxasSSGky048VLqkphoPQNAjP9sw0UIrBdbXcW7R_DMXa2n-IFslvDlXfLZzh-4JYsREankTMBGfcuY5I0udqkAdEc_1h2Yq6ZyuDsqo3Qj9jKkSTtDGUluCxSv55jQD1PaWdrZyJV6rY4-KccCoF9Qd3wtO9CQf0AdYN8LeSBiU5XvVsUODxnSN0-vO5OlGZKEAvw0WirymbqgwQC8PYWaSKwH3rNMet4JnHjs7_l-DfqwoQzX8_gSN68C0zwvswH_1Aqp7oKoKVc0c47K23n6x8XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/165b8123ee.mp4?token=QJKfR3lLVyf_02ijbHQUE3uvDUKe1YLMJW_MnhZjr4Zy28VulInLiDI9eqhZxasSSGky048VLqkphoPQNAjP9sw0UIrBdbXcW7R_DMXa2n-IFslvDlXfLZzh-4JYsREankTMBGfcuY5I0udqkAdEc_1h2Yq6ZyuDsqo3Qj9jKkSTtDGUluCxSv55jQD1PaWdrZyJV6rY4-KccCoF9Qd3wtO9CQf0AdYN8LeSBiU5XvVsUODxnSN0-vO5OlGZKEAvw0WirymbqgwQC8PYWaSKwH3rNMet4JnHjs7_l-DfqwoQzX8_gSN68C0zwvswH_1Aqp7oKoKVc0c47K23n6x8XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طنین اذان مغرب در مصلای امام‌خمینی(ره)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/667065" target="_blank">📅 20:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667064">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
تعلیق پروازهای تجاری فرودگاه نجف
فرودگاه بین‌المللی نجف:
🔹
تمامی پروازهای تجاری به دلایل عملیاتی، تا صبح پنجشنبه به حالت تعلیق درآمده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/667064" target="_blank">📅 20:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667063">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42afbb9eec.mp4?token=kp-87sg3l-008eI0NW9t6bI8iu30XC139io9rXE3ipMTbtit-qk1MGJrTyy8TsEmq5EqT-FcB3zgr7IjDkOBVB0Cxcg_GoldQyl5qwjhLZ2x8buN2FVWK_YgKU96eHC3vCwBcgnpOS1Mnsy_XnaCfWmKZbEg1iH48D7jJx5TBYhM0B2J3peJ1s25v9cgHq4F8E2eqo_j4pY5S2Y3LzYPttXl0n4aKsJ9JfJXrigtWff2xV2Bqj6rj32X-aGkcLMjJJvwOJ3pofhH4zUpftyyTLvOIeTnwOOe30CFpz8K6TcZxKqkXfiVqO9OEUS27J7JiUluyA1Glg6NAcBBniw10g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42afbb9eec.mp4?token=kp-87sg3l-008eI0NW9t6bI8iu30XC139io9rXE3ipMTbtit-qk1MGJrTyy8TsEmq5EqT-FcB3zgr7IjDkOBVB0Cxcg_GoldQyl5qwjhLZ2x8buN2FVWK_YgKU96eHC3vCwBcgnpOS1Mnsy_XnaCfWmKZbEg1iH48D7jJx5TBYhM0B2J3peJ1s25v9cgHq4F8E2eqo_j4pY5S2Y3LzYPttXl0n4aKsJ9JfJXrigtWff2xV2Bqj6rj32X-aGkcLMjJJvwOJ3pofhH4zUpftyyTLvOIeTnwOOe30CFpz8K6TcZxKqkXfiVqO9OEUS27J7JiUluyA1Glg6NAcBBniw10g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
او به آرزوی‌اش رسید/ زائر رهبر‌ شهید: خوشحالم که رهبر شهید به آرزوی خود رسید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/667063" target="_blank">📅 20:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667062">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
بانگ طوفانی یا حسین (علیه‌السلام) در کنار پیکر مطهر رهبر شهید انقلاب اسلامی در مصلی تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/667062" target="_blank">📅 20:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667061">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه البرز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SopNyixTHtQ7gZUUhaBJ45WI1Eo8p9QsBZs5ESbrKtbVwzoKaXZf_cvKNsUCYbgW7Iq_bwDQtVprMluK4dmTY3wEykcdFH33c4DXkWgwvbHPFJej-A3v8HsjwUM_xvuELKTZerVWEMyliloS2kg6M-hPCr5BGvTvg8EHgj_NSczH-c-beOGmEsfw59QMY-fCxTTPKHALOes0Ie160vrik2LJmypDGYVIxnvDkLnmf1oQ_qFYlF31L6MrXGHahi16DNL4u4SauS3lsVfTdGB_9g_2T0Uy9NC7J1t1Ija-npxa3fxKPr4QZVfcVG7O0DNoXpgSbR14eED74ph2OEyo6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازدید مدیرعامل از موکب‌های خدمت‌رسانی؛ نوراللهی:
#بیمه_البرز
تمام‌قد، پشتیبان زائران است.
مدیرعامل
#بیمه_البرز
در جریان بازدید از موکب‌های این شرکت در پایتخت، بر ضرورت ارائه خدمات در کوتاه‌ترین زمان ممکن تاکید کرد. در همین راستا و با دستور وی، علاوه بر استقرار شبانه‌روزی تیم‌های تخصصی ارزیابی و پرداخت خسارت خودرو در تمامی محورهای مواصلاتی منتهی به تهران، اعضای ستاد ویژه برگزاری این مراسم نیز جهت ساماندهی فرآیند خدمت‌رسانی منصوب شدند.
مشروح خبر:
https://www.alborzinsurance.ir/PublicBlogDetail/5056</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/akhbarefori/667061" target="_blank">📅 20:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667060">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csgLazkl2uIkSb4nsYt9BWl8xBPugzz5MJ9Th4YF4cw2464weq5Zi_n_m2pouKleyZe99l78G9avNSkNgFJWnRX9vceyKNraiLN1H30cTeTnfbisq8pfBjpUHlM3qU8awZfnoTQklzMa_wKguhu3EGFiDkK4vkgagRnbM5Y2ufVrSTXxXJRK65B7DielTVvwp2PgL961kWUpu57sT6jEtow0edO5c0EEgmp4eCnezIepf6n6HlVa-Wu09fmdSx7YGBdo7g_jeYGCg5kHMg4xFdZn5TnEEIJgI96eIvapKcfE7v3k5Z4aXoe_Bhuxt6b6aq4A02kflocRna5Gd8onRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مشاور رئیس‌کل بیمه مرکزی: صنعت بیمه در آیین وداع و تشییع رهبر شهید انقلاب، تمام‌قد پای کار آمده است.
ذاکر تیموری، مشاور سیاست‌گذاری رسانه‌ای رئیس‌کل بیمه مرکزی با تأکید بر اینکه خدمات ارائه‌شده صنعت بیمه، تنها گامی کوچک برای ادای دین به غیرت بی‌نظیر مردم و ایستادگیِ رهبری شهید است گفت: خدمات‌رسانی صنعت بیمه تنها به برپایی موکب‌های متعدد، پذیرایی شبانه‌روزی و اقدامات فرهنگی محدود نمی‌شود؛ بلکه در کنار پوشش بیمه‌ای تمام شرکت‌کنندگان در قالب کنسرسیوم، تیم‌های متعدد ارزیابی و پرداخت خسارت نیز در سراسر محورهای مواصلاتی منتهی به تهران مستقر شده‌اند تا این صنعت بار دیگر تمام‌قد پشتیبان رفاه و آرامش ملت باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/667060" target="_blank">📅 20:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667059">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
پیکر رهبر شهید از جمکران تا حرم حضرت معصومه(س) تشییع می‌شود
دبیر ستاد ملی آیین تشییع و وداع با رهبر شهید:
🔹
پیکرهای قائد اُمت و خانواده ایشان، پس از اقامه نماز در مسجد جمکران، از این مکان تا حرم حضرت معصومه(س) تشییع خواهد شد.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/667059" target="_blank">📅 19:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667058">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKounasJ7oEJ1Vbb-uJ9bj4aiPEUCXKHoC20GHz6IiZMAPvy86D_pHJZiKGqIvQe6Us_SQipjqCE_-GEnYDn7TeZwymYiPMk7ztPPjlfM0aKDUOX3ra72pDX5lCQ9QSHLRQCOH9JU7UDQYakL173i8Q21Pm1gSX44HuAsSxCwW87ytB32UVJBP-z1yL-OC0rZ_fyVCFwwj-I1Uylfq3OcpB-w925QA5bkrLu-7l--im69Vj50-sWrB3j2i2ENq1hA12iAzoroT5n3yqw_R2WocQ02iYy2W_tFdSuqeBGLxXjPdzrnfAQzjz6nN44AfgefSjQ5K3ftj7P4eg_DxUZBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
‏
بنری در مراسم مصلی خطاب به ترامپ: «خواهیم دید چه خواهد شد.»
‎
#هزینه_خواهید_داد
‎
#WillPayThePrice
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/667058" target="_blank">📅 19:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667057">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syfPQDR3BKhsy_XS00SlsUyKRU3Aov7o9-BY-8jsqBonO5pDT3RO-GrI0c1FCEWRaCFeOMGMxpKz9le16FseAdPrEfKshTLEuSRS_-efIb07dmcvqLpp5ryDNrISRtcvXrfIjvYtxM7o1Yk24k6Q0JVL5Jte3nZEib3y8SflyPR-WhMp0mGV3-ZOZzmiu2ZD8_2samE39FFWZ_JZ1DSLvPRhUQMXLXKpc4I79YkN_WD9T6QYlwkDcrMtBJJ4mrV_nfOIdBWqqiyVCwXXek8rF2kW7bZrUbBG4O8AwNnp41RvkvqolpQO0IKu5oK_yyGJ0vLZJ86varmmizY9pCil9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقش شما در بدرقه (۵)
🔹
اگر نتوانستید به تهران، قم یا مشهد بروید می‌توانید با اکانت خود در شبکه های اجتماعی در این بدرقه شرکت کنید، چطور؟ در جریان تولید محتوای بین‌المللی اثر بگذارید. کافی است عکس، نماد یا جمله ای که از رهبر شهید دد خانه خود و اطرافیان هست را در شبکه های اجتماعی پست کنید. از کپشن انگلیسی و عربی هم فراموش نکنید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/667057" target="_blank">📅 19:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667056">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02c0ca481a.mp4?token=CL-XziB5NO0MaX9zeqeV-ixn-oY4qvFB1W3evzgBRvfWSdQ32l0uSpTISweXHInIIyN9NjeDwJgiZa5zbuYmQpbSBVh-k7YxLNKZQZlmsP9yuQPE0rQVoR_DLGJv9DbSO8pdzSYiz5ZVm1R3F5Kdx1mF36G9NGo92oWCcrVxKHSnNAFb85z417Go8sW9eRxKU6WnOBo_xs-TguIvIWOWHrNGBDZi5xVKfFVQhuR3B2RiMhHEu47ioRyT4W-BWs_nzekOGc_Hkylx_qNuhkYhvSNMqGVhrav8eRSrb1BS_gJev4PI4D-vSV5vuq8fLbQUVcZE9a9gu32ZONIFroWYKxuAeT8kfHG8ZVFwLy8jdXwQx_w7sKRYYNvGdvdE0WtqmZRskPNtARiceHrOEe7-QJtHDPgE2Womyph7g3ZpZU_h3lAKmgxoKRC3tdFo-TlRk9ebOU72STiv-Zfe3_XwZEeB41ILHzvnZO8bToOH_1JuM2qPqhqr3IjXjMuyUr7hufju79ZyAVC--nl5fz_doib3FvMwn7ObuI0jBxU7f1liGqp-enFTQ2g3CEPDwvYDjb9cr-G3mx9h5ghcr4_mvuL2s2SKHJCvKKkuTX4N7YSmDaMTxvU3dWDVXnRN_tfbLvfsL9t4qWXgO24NtpJRnHN5Ep5dXDtKCVhxdrDrcGk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02c0ca481a.mp4?token=CL-XziB5NO0MaX9zeqeV-ixn-oY4qvFB1W3evzgBRvfWSdQ32l0uSpTISweXHInIIyN9NjeDwJgiZa5zbuYmQpbSBVh-k7YxLNKZQZlmsP9yuQPE0rQVoR_DLGJv9DbSO8pdzSYiz5ZVm1R3F5Kdx1mF36G9NGo92oWCcrVxKHSnNAFb85z417Go8sW9eRxKU6WnOBo_xs-TguIvIWOWHrNGBDZi5xVKfFVQhuR3B2RiMhHEu47ioRyT4W-BWs_nzekOGc_Hkylx_qNuhkYhvSNMqGVhrav8eRSrb1BS_gJev4PI4D-vSV5vuq8fLbQUVcZE9a9gu32ZONIFroWYKxuAeT8kfHG8ZVFwLy8jdXwQx_w7sKRYYNvGdvdE0WtqmZRskPNtARiceHrOEe7-QJtHDPgE2Womyph7g3ZpZU_h3lAKmgxoKRC3tdFo-TlRk9ebOU72STiv-Zfe3_XwZEeB41ILHzvnZO8bToOH_1JuM2qPqhqr3IjXjMuyUr7hufju79ZyAVC--nl5fz_doib3FvMwn7ObuI0jBxU7f1liGqp-enFTQ2g3CEPDwvYDjb9cr-G3mx9h5ghcr4_mvuL2s2SKHJCvKKkuTX4N7YSmDaMTxvU3dWDVXnRN_tfbLvfsL9t4qWXgO24NtpJRnHN5Ep5dXDtKCVhxdrDrcGk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت زائر مهاجر از محدودیت‌های عزاداری برای رهبر شهید انقلاب در اروپا
زائر رهبر شهید در گفتگو با خبرفوری:
🔹
من آلمان بودم وقتی خبر شهادت رهبری را شنیدم؛ نمی توانستیم آنجا عزاداری کنیم، داشتن تصویر رهبر شهید جرم است در المان.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/667056" target="_blank">📅 19:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667055">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
نتانیاهو: با ترامپ بر سر چشم‌اندازها توافق داریم  نتانیاهو در گفتگو با فاکس‌نیوز:
🔹
شکافی در رابطه با ترامپ وجود ندارد و هر دو رهبر در راستای منافع کشور خود عمل می‌کنند.
🔹
اگرچه ممکن است اختلافاتی داشته باشند، اما همواره آن‌ها را با صراحت و باز بودن مورد…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/667055" target="_blank">📅 19:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667053">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YcPA8bHpHVnrvxsbxynKgW3o_MhWMxliqykOIcwo-nDpCbtn_vip0kHoTyzQp1vCktc8j-M0mTjgCUzGywVXohuxlekbzWDCE7UpMR127n8yI3Uytj174E55a1-PlpUpTW9xAROdNf-2RDs-6pZv8Pb_e7i9cs_VncsT24BO83_9TWRZMw_iQLAUueklVROrdJDnhK_0oHsdbM-cTT73fvOdkXJyvQrYK3E3kIYq116-hRQODAh82R9j_5VjInxSUVHcIBTqEUfv8etWJfAxTTIV9m9TKCBitydkggPsfQ8stXpsQd7PgF6VnJo2Ry7Od7D-7T6KVR02jdwxVgDLHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nyuH3tEoKYo5BN7OoGo3ZEM05Ao0ciGMT6Rau2EZNlivg41zaS6KqywI-w_dgk4oHCyTx0t6Hddg1im686_UF_9_Ww2tXEo1aVDaytX4QF_--2uIl6pbL2zArk_k4SEa80dngtIgBLdia-dlbqcuCeaod_nEvc1gfiXqTR50xUx1i0u9w-SG9Cz7s8JL_yEuOcfeLNihJdcxZ_UTLEza-_EL0lX9ogO8d1RvIzQOrEAqc0fZIAURqDd0qIqUQYbqDK0pCPgN6IvEfJC5IrLRVQPgB6RH_aDhdw4pXZq3teTIfZIPwa89mGgCWbGFaW645C0vNzugswrHcT18ZiAr3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
روایت زندگی رهبر شهید از تولد تا انقلاب اسلامی
🔹
«شرح اسم» روایتی مستند از زندگی رهبر  شهید انقلاب  از کودکی تا سال ۱۳۵۷ است. این کتاب با تکیه بر اسناد، خاطرات و روایت‌های نزدیکان، مسیر شکل‌گیری شخصیت، مبارزات سیاسی، زندگی خانوادگی و فعالیت‌های فرهنگی ایشان را به تصویری منسجم و خواندنی تبدیل کرده است.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/667053" target="_blank">📅 19:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667052">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/700dbb08b4.mp4?token=cKQDMilTBhFZboZvJLG1KabQufMOzKn0RQq92t7ySuuoMOFIIFquvZMfo8KSVGybqLMtJvE_4jhXj7cDzPMrzdsumxj2QGRvyuFepKISUpoArbfIlu1wEf6Ij0IB4oOKY4Qfvk20oXN8hdwE6pzrDq5Q7tLm8QzEm3ALNyxRzhGuqZL5qAuBdf06efl_gJVSbFhwzrvTegNIGWwBTDAsdjSb9CoB3deeceSxY0oaKg7XQfystDmRWeb4kp48RNLlbgRLF_ce0sewvs-g4vlqb8P6k60mGHxo3K0dsV8HDt4VNjTeK-7f0BNSH0vzy5TrylNv3LsL59qkR19m9uGmUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/700dbb08b4.mp4?token=cKQDMilTBhFZboZvJLG1KabQufMOzKn0RQq92t7ySuuoMOFIIFquvZMfo8KSVGybqLMtJvE_4jhXj7cDzPMrzdsumxj2QGRvyuFepKISUpoArbfIlu1wEf6Ij0IB4oOKY4Qfvk20oXN8hdwE6pzrDq5Q7tLm8QzEm3ALNyxRzhGuqZL5qAuBdf06efl_gJVSbFhwzrvTegNIGWwBTDAsdjSb9CoB3deeceSxY0oaKg7XQfystDmRWeb4kp48RNLlbgRLF_ce0sewvs-g4vlqb8P6k60mGHxo3K0dsV8HDt4VNjTeK-7f0BNSH0vzy5TrylNv3LsL59qkR19m9uGmUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرگی زاگربلنی، اسقف اعظم کلیسای ارتدوکس قرقیزستان: رهبر شهید مانند پدر امت بود و با چشمانم دیدم که ملت رهبری را مانند پدر خود بدرقه می‌کنند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/667052" target="_blank">📅 19:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667051">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1351a483e7.mp4?token=e7N3K_K1xwXw2xSAKgolt0vT2ktjWswimEpWxvHtZ-G0mVTzbLIBu2N0gmdpUV8he4shaoRow8cw3JWmk_VHhLPKAqI1mZKrkQuIJSG9lhbim2TUPBim9l0U3qqEXuW33nufpiMhhHpoowXNBNkqOVDJxpscV6soDULtr6DZSVOSeWjiE27HlpCKrnZ49HgH8U7JZBhMQua74YX41TrRMRJYcoyqRM_jc1ogqJjDBt1uvjskOoHrJWEeKEGb60TNE29A8nXlHum_yiBH24TEWLFt7-8a4PY_lkRpxrdQu2NwO6jgzZBcwk_E5H_Yer32V0WlMj0ecaPQcusFnRDPxmB4-gLgg1NZa8Oa3gEdKtkk_3p3hU6A-VV7AFdo6tw2Pocj9rA9SbHh9V-zJAB6Y6cA6bXcp_WU--OHDge7oO5IOkfLl_B1mVr3R5bhN9NVGt6VNTRsKs4IJd9UAR7vStQU6sIObrA4Tivh6FXiuPZbid81NlpRHOIMfmxv-Y18S7MpkHGBUDLAOuhQpZ6eJqOrc0MK8Cs4h_nPkfaC_InDYtDPxh76aqxJmVsIj-jfXPDHpo7vDMdCWAhV9FFX3zgjKMGJdBK1ULyXeDbetgtvZVPjzW5ykqDnZSSpZxrFNNVXE0DW2QEE1dRYg396lN2qRp8fRwrxS3aITmjlKfY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1351a483e7.mp4?token=e7N3K_K1xwXw2xSAKgolt0vT2ktjWswimEpWxvHtZ-G0mVTzbLIBu2N0gmdpUV8he4shaoRow8cw3JWmk_VHhLPKAqI1mZKrkQuIJSG9lhbim2TUPBim9l0U3qqEXuW33nufpiMhhHpoowXNBNkqOVDJxpscV6soDULtr6DZSVOSeWjiE27HlpCKrnZ49HgH8U7JZBhMQua74YX41TrRMRJYcoyqRM_jc1ogqJjDBt1uvjskOoHrJWEeKEGb60TNE29A8nXlHum_yiBH24TEWLFt7-8a4PY_lkRpxrdQu2NwO6jgzZBcwk_E5H_Yer32V0WlMj0ecaPQcusFnRDPxmB4-gLgg1NZa8Oa3gEdKtkk_3p3hU6A-VV7AFdo6tw2Pocj9rA9SbHh9V-zJAB6Y6cA6bXcp_WU--OHDge7oO5IOkfLl_B1mVr3R5bhN9NVGt6VNTRsKs4IJd9UAR7vStQU6sIObrA4Tivh6FXiuPZbid81NlpRHOIMfmxv-Y18S7MpkHGBUDLAOuhQpZ6eJqOrc0MK8Cs4h_nPkfaC_InDYtDPxh76aqxJmVsIj-jfXPDHpo7vDMdCWAhV9FFX3zgjKMGJdBK1ULyXeDbetgtvZVPjzW5ykqDnZSSpZxrFNNVXE0DW2QEE1dRYg396lN2qRp8fRwrxS3aITmjlKfY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زائر رهبر‌شهید در گفتگو با خبرفوری: وقتی خبر شهادت رهبرانقلاب را شنیدم خُرد شدم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/667051" target="_blank">📅 19:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667050">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhgeZ8aTbFN8m-ZaVOy2GHI2hvKIqJNBL0IlcIC5pd3uDDTc6BgVOe9X6s94on44BvVDNVX3ta1xfxJyFyjB8MWmp8JtNWg3XrovpcYNEPqAPYQIPyGSv08tUJG98Wt5pyYGSpEcW2vrAZ0vmWps3XSEWxHayj5-5mdV0ebg-o1OT2GHj5D0VWGl0CTIXpny5faSwCssKoYMVVl_E6P_H0Iwj0eymQKiYSphTU3UJTEVtMyD70yzIJkvtN4fik_OqSYLSvw2uogddU7ejRai0SVmdvLVxOKebKzArpNoi8UBWb7NoRRrXpzI5jXIzKSGjvZywabNxFh1d3p_aueYuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر خبرگزاری آسوشیتدپرس از مراسم روز یکشنبه در مصلای تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/667050" target="_blank">📅 19:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667049">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f306a56e29.mp4?token=WMqfR_-QqJAWv249KDugO1zaQaPG1uVyBHC330yXId8NS4s5oGUoo2J_yCY4rAiqLshzl8CKXuv0FBRuJX6soIUuVXX0nbyRJmCvCFVeAkq0tc0Qnz9HzutU3VZyz7vo2SFPho0yA26KYD-iCwWtN8Mt2INi7b8qBJVf0kMKtJpKjIaSHysfeGgoPuZPR3Q4gy1lSa2WOMisP-AZyxLuhBHzlfAAsQmbDLtOZ3KyB6Fi4QGQsTW5TnDGQed7qKSXP0hE6pOpaAJli32vs3rpAtUzIY3StHvwVOLlbKcVp-Be0CxlrCvtVrb4_1c6-vVGMXVZ51y565OhBAXtOeCtyqXlWQRXUdTHXp3L2xYV2NfbetVCUTvr6ZVbCQRBspF3owbLqOYmBLPiG2oepuM2fyU841K1riTQ4wJB0hW7m-GS-ssqvWpII_bxdKBr2WeAb-uOuXF1la38hvztZMk0_xjbRbZbr2BzjZdy_gLKwXWatXDhDB3GaqgDqWxAbso-4Z8GoV-XwqKTtNikbQSnZ_X6FKgkcT88dLAMrljTJGfJAZIHWkDQKRUehYluKaXdlE365BRV-lWAkv6ken1KSl9TFtLaMa3RY3aku75QaiKnqs3YVKzqaOort3aW_6jeAephjciRzc9kD4E5KQQCDNtRnDFRYZ5tpq8OtMdkYII" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f306a56e29.mp4?token=WMqfR_-QqJAWv249KDugO1zaQaPG1uVyBHC330yXId8NS4s5oGUoo2J_yCY4rAiqLshzl8CKXuv0FBRuJX6soIUuVXX0nbyRJmCvCFVeAkq0tc0Qnz9HzutU3VZyz7vo2SFPho0yA26KYD-iCwWtN8Mt2INi7b8qBJVf0kMKtJpKjIaSHysfeGgoPuZPR3Q4gy1lSa2WOMisP-AZyxLuhBHzlfAAsQmbDLtOZ3KyB6Fi4QGQsTW5TnDGQed7qKSXP0hE6pOpaAJli32vs3rpAtUzIY3StHvwVOLlbKcVp-Be0CxlrCvtVrb4_1c6-vVGMXVZ51y565OhBAXtOeCtyqXlWQRXUdTHXp3L2xYV2NfbetVCUTvr6ZVbCQRBspF3owbLqOYmBLPiG2oepuM2fyU841K1riTQ4wJB0hW7m-GS-ssqvWpII_bxdKBr2WeAb-uOuXF1la38hvztZMk0_xjbRbZbr2BzjZdy_gLKwXWatXDhDB3GaqgDqWxAbso-4Z8GoV-XwqKTtNikbQSnZ_X6FKgkcT88dLAMrljTJGfJAZIHWkDQKRUehYluKaXdlE365BRV-lWAkv6ken1KSl9TFtLaMa3RY3aku75QaiKnqs3YVKzqaOort3aW_6jeAephjciRzc9kD4E5KQQCDNtRnDFRYZ5tpq8OtMdkYII" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال و هوای مصلای امام خمینی(ره) در روزهای وداع با رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/667049" target="_blank">📅 19:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667048">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/594503be2b.mp4?token=RKGFYAs2VfYsbQ_utd5RuLd9ZgG7OQHU0LzFBU1BA3uL5fR7TBzNoqYuiDcFe-vJ82tuRmTPT9feFJp5O10eW4kQlouwCTgRg3qnWTjqA1u3VjU2Lhdz6Id4G08p7-7oum7MlNNyJ7kBgYFBxAESC09XLGwxK96SHi7ZXWBCCJqWzDYxNsftjW2R8RbQgxMPqIa_qmwH5Ttbzd1jXFvpnQIrMZDq9VaOfepEO62DVlhMDDU1zKgOItDclRBeoi2zBT3HTkIpCSri6GdLBUcblmHwGyw4sQUWXQJH5PYe3utluW01lPBXCYQ0gc1BHUKZjvFCRKMOeP9UQg4riVKq6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/594503be2b.mp4?token=RKGFYAs2VfYsbQ_utd5RuLd9ZgG7OQHU0LzFBU1BA3uL5fR7TBzNoqYuiDcFe-vJ82tuRmTPT9feFJp5O10eW4kQlouwCTgRg3qnWTjqA1u3VjU2Lhdz6Id4G08p7-7oum7MlNNyJ7kBgYFBxAESC09XLGwxK96SHi7ZXWBCCJqWzDYxNsftjW2R8RbQgxMPqIa_qmwH5Ttbzd1jXFvpnQIrMZDq9VaOfepEO62DVlhMDDU1zKgOItDclRBeoi2zBT3HTkIpCSri6GdLBUcblmHwGyw4sQUWXQJH5PYe3utluW01lPBXCYQ0gc1BHUKZjvFCRKMOeP9UQg4riVKq6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری شبکه سه: ملت ایران تا زمانی که نفس می‌کشد، میناب را فراموش نخواهد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/667048" target="_blank">📅 19:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667046">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
برنامه وداع در مصلی به دلیل ازدحام جمعیت تا ساعت ۲۲ تمدید شد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/667046" target="_blank">📅 19:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667045">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEDAAT-JEQ_mwCwRf8p20bsmYpgxpU4FzknnxKL32w7kTZP3H-ahQ7qwxri1oLkVmhyC0tI-DviMsXt76Iwy0dRF5KeyUa9kFrxo_N8kDPR9c6wNytGwiuVyfhkm6Zq3mYGh_iJHr6NWiPM4KoLySC6Vb_M-biqVlzVqBdNO-f4dQn83z4MqJxY-qKYrN5cLi_3_neoqLgVw3b1etjm2sNd2e60oLZ_wm8nkx5qic7Hw2KNqHlCE3ChnYRjYxZPZZWVig-WreaAUw5-5ukbPEBKu4DyvQHypzOT6D9lgVU977E9LxYLNGMqbcEzASJosZmYwahyss8ydTDWmYxnT1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عارف: فردا جهان شاهد حماسه‌ای از جنس عقلانیت انقلابی خواهد بود
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/667045" target="_blank">📅 19:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667044">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2069e9781.mp4?token=brRzr9p02YQgoLM51nNzF03ci5qqMWyn2fZU0YZUeYJFzNxBu6oA0gtsnl4mwqDZASFAydkavA-UXJPsUKLEbfiOrp87PLshtTZQ-CspmfGmYlhqKrizf-a_ebgaVd8Ba0KjnxQIYdR9KXoqMC2tlRbLCmq43SPRG2tcV-3UQR5KmT8eaVXOsYD6Kzaw_AlxH8Ys9EhPF3uL5DHAe3CbrZMdwa-viHXwYReGME0scBSui_Sn1Kd-iV4lXApRhS9mpFTNLoPQeIVDbVeBjiDwaHAySe7N5av1Y1cMGu0uZGbM2fUMQB8R3ZcjpOUeuQwZmqwLiYND2gHvt7jJdN2g0hs33gHO7Mb0LZ6wIROf3rT8r4zncExEelccmz-9bjBFhGVolCoiLVAn-bSYF4tLTKsl-FZXD0CCTAeqhsF96heWhtEJCfWjPxe3FoJmeZf34RNvZzoQh9qzVHIXP3SlGKDfXIC1-Rozgj8jqWeZk85bpeWsG3fHpdnF3gm9Sjs7z29MKLvxMiX9fe5lKT98b7L6xkhdsUp_y2AH1w36a9DpkCdZ7yHXgltGcLKfkeefaGLvC0Z56Gvz4f8rpgK8plZlBehrhBO4cHv8fLPSzvsTqq00drLN9maMgkYB-Iih3dmdiO27TlLiq7_ypDGsNkN_DRnUaQx6HDDie9aWi0Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2069e9781.mp4?token=brRzr9p02YQgoLM51nNzF03ci5qqMWyn2fZU0YZUeYJFzNxBu6oA0gtsnl4mwqDZASFAydkavA-UXJPsUKLEbfiOrp87PLshtTZQ-CspmfGmYlhqKrizf-a_ebgaVd8Ba0KjnxQIYdR9KXoqMC2tlRbLCmq43SPRG2tcV-3UQR5KmT8eaVXOsYD6Kzaw_AlxH8Ys9EhPF3uL5DHAe3CbrZMdwa-viHXwYReGME0scBSui_Sn1Kd-iV4lXApRhS9mpFTNLoPQeIVDbVeBjiDwaHAySe7N5av1Y1cMGu0uZGbM2fUMQB8R3ZcjpOUeuQwZmqwLiYND2gHvt7jJdN2g0hs33gHO7Mb0LZ6wIROf3rT8r4zncExEelccmz-9bjBFhGVolCoiLVAn-bSYF4tLTKsl-FZXD0CCTAeqhsF96heWhtEJCfWjPxe3FoJmeZf34RNvZzoQh9qzVHIXP3SlGKDfXIC1-Rozgj8jqWeZk85bpeWsG3fHpdnF3gm9Sjs7z29MKLvxMiX9fe5lKT98b7L6xkhdsUp_y2AH1w36a9DpkCdZ7yHXgltGcLKfkeefaGLvC0Z56Gvz4f8rpgK8plZlBehrhBO4cHv8fLPSzvsTqq00drLN9maMgkYB-Iih3dmdiO27TlLiq7_ypDGsNkN_DRnUaQx6HDDie9aWi0Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دقایق پایانی وداع با امام مجاهد شهید و ازدحام جمعیت در صحن مصلی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/667044" target="_blank">📅 19:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667043">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5PvhyA-O-jGnW4BVrEo02RTO-6CEVLU-u2y258eH3r2R8oL4Oi0XHLsFYY44iBlsGrEPLxWzks2t9M4zuSNlWK7OyiNE_qatp9qw4bWxN1bmdyQRdcyt0BSIPRmqL2HMRb-2gBtBHOHnIEU8CKyJjOTfh7frET2zqMdtgsc_zvZEOmLXI9m_tNd-SRKClBKgOSY6Zj11B3qCpOPLC1btQ4urypyxN8zZOjXVW799OHEwEhNirBs3sfRAMuyIq6EvEW_-yv23Td9QnV7ibXKa4M3AS1KqDSZjINtRyYtzofZic45aWjN4mmiQEzf_2If-dKblpRQSTrImj2zGpO1Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در موکب خدمات رسانه ای همراه اول صورت گرفت؛ راه اندازی استودیوی تولید محتوای هوشمند برای خبرنگاران
🔹
همزمان با برگزاری مراسم وداع با رهبر شهید انقلاب، موکب خدمات رسانه‌ای همراه اول با هدف حمایت از خبرنگاران، عکاسان، مستندسازان و فعالان فضای مجازی، امکانات تخصصی سخت‌افزاری و نرم‌افزاری خود را برای تولید و انتشار محتوای حرفه‌ای، در اختیار اهالی رسانه قرار داده است.
🔹
در این موکب، فعالان رسانه‌ای می‌توانند با بهره‌گیری از تجهیزات پیشرفته تدوین، اینترنت پرسرعت و مجموعه‌ای از ابزارهای تخصصی هوش مصنوعی، ویدئوهای خبری، گزارش‌های تصویری، پادکست‌های صوتی و سایر تولیدات رسانه‌ای خود را در کوتاه‌ترین زمان ممکن تدوین، پردازش و منتشر کنند.
🔹
این خدمات با هدف افزایش سرعت، کیفیت و دقت در پوشش رسانه‌ای مراسم و تسهیل فعالیت خبرنگاران و تولیدکنندگان محتوا ارائه شده و امکان استفاده از قابلیت‌های نوین هوش مصنوعی برای ویرایش تصویر، بهبود کیفیت صدا، تولید زیرنویس، خلاصه‌سازی و سایر خدمات تخصصی را نیز فراهم کرده است.
🔹
از تمامی خبرنگاران، تصویربرداران، مستندسازان، فعالان شبکه‌های اجتماعی و تولیدکنندگان محتوا دعوت می‌شود برای بهره‌مندی از این خدمات، با همکاران موکب خدمات رسانه‌ای همراه اول، هماهنگی لازم را به عمل آورند تا ضمن استفاده از ظرفیت‌های فنی و تخصصی موکب، تولیدات رسانه‌ای خود را با کیفیتی بالاتر و در سریع‌ترین زمان منتشر کنند.
🔹
موکب خدمات رسانه ای همراه اول، در خیابان آزادی تقاطع آذربایجان، با مجموعه ای از خدمات و پشتیبانی های تخصصی، در خدمت اهالی رسانه است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/667043" target="_blank">📅 19:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667042">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
قالیباف: صلح در لبنان جز از مسیر ایران ممکن نیست
قالیباف در دیدار با هیئت حزب‌الله:
🔹
برقراری صلح در منطقه تنها از مسیر ایران می‌گذرد و دیپلماسی ایران همواره با آمادگی دفاعی و روحیه رزمندگی همراه است.
🔹
محمد فنیش نیز تصریح کرد که توقف جنگ و پایان نهایی آن در لبنان، نتیجه‌ی دخالت جمهوری اسلامی و الزام آمریکا به اجرای توافقات است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/667042" target="_blank">📅 19:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667041">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMsKiKG_gGH_1T1HFnhcAa-ro5B9cuzKHjjuzSvQveKqaPAqqyY9dBNzSueuPBo0NxEm7ISQYSOy7E7XkhndQYiqhAYWmDaDw8QTcRIEHycjOkssoFyzBrr8A3LbrBGpcfh4GESSIHXEvNA_ZJGGHzcpSsD-5fwMgd0f7UTIAge9oHEnewp12e03l8Z6hjju0d8_neP5jebwX5uKojKQNIwECWOQ-zKKzbPYsVOb2tE_f-9xoWrk0nKjSeStQNk40TYrKa1vBB-5mqWwShQy_yzkE_1XMPgCJbZkLGqlj9N00JFFaUX1BaVbpHYlPFcG8gB8k5yZwaC0kmZq86GPLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتصاب مجدد حجت‌الاسلام والمسلمین اژه‌ای به ریاست قوه‌قضائیه
🔹
حضرت آیت‌الله سیّدمجتبی خامنه‌ای رهبر معظم انقلاب اسلامی در حکمی، حجت‌الاسلام والمسلمین محسنی اژه‌ای را بار دیگر به عنوان رئیس قوه‌ی قضائیه منصوب کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/667041" target="_blank">📅 19:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667040">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjyFG80fyTqbVkyoQEq_d6qzpcvgKia5difrLom0VbFgP7iULRzQqWQqabh9msAK0djaellfblFAiPU-ParI5ijL5IgUK9MsZEBMsrOufU3SRPQnuvoRG_-IbmsyirNWekgKjvntCBPoh2Xlm0QyTd3O_gr9jta_GRFHaRu2J9cG91pYj7nIZ7ZMmJhwiDkREtxhRj32Y1un7AnZ5wzQZY3sGQiBy-IrAWkKT8a-gtQv4_ILor-FOkxPPESOLDaOPkOxWV7MhK3n9k4IiIjeSc56g5Ei-BLXTslLR00lAn0O4C4uH6ymqVgRzQgrJDLtlqgZ5T6ovNHO6AWWtdALrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دنیا بداند انتقام قطعی است
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/667040" target="_blank">📅 19:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667039">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZ6tXyWHaLoyr2BB3tvh2KE4aVnQLf9wAOnuG72fmgFgjM-tJUJJs2bLWHcDiaQ1f3iLQDEWC_1ErxlHbk4hDpl7NeNuAtTLKDJwTa2bpRMIMB7QK8hP4I6XXEAcilu-8BFVgZYLI9qWmH26V0Y8HltGgztk0Wn4W0K7uToBF7x4Mxb3uwxuHEWKqTeXxmiX7aPvqy996uCIQzbzHDlF3lpMWal0pRdhSIh6TpVjEU_h4NKQvqvj7I1CezX_pT9bVPlLCW7RfWFlUplo3V5HG7r3wRi4hwJ2UZBYzIYHIBucpQ-hEyk889tuAIvdVFzstIYUKiNRFqvPsLfutF5T8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/667039" target="_blank">📅 19:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667028">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pZfEn0M5I_NQE3tJSC-ubtjcFtfCi4lJZc6PhnYV-rB5DZD-3z2VlIvWwGpiPADtBgYQ_Nq4JUJZgpjd6jqCdAwp9pxwPmTCdeR0Mq8iW4c-miHE1jpC3nqkFZfea24p80j67aMzd9N7eDbSdYKSoNPtYeFQkyE2TZje8c3e5DTkqmAvybUPmgtj0pv3lYti-4Z7kkPKRdhhwul2A-bk4TkQUHY3K6hqH8LAd6evdSIs5mzZw8qyyoLoqql3_o3r8jEFdnswZ_-VFnSzevXvFCmfyJvgkQGzOsOzL-wfitaGhsp-Rsx4li1NnqHAGzeMsvSu6Tu4O9M4g12oTSqVZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LSiMq4KKgMH1eh2Az-Rx687uxp5a5iDe3Ggd5GUyrlH4lQTt_ur4C_quBaMujFxOrkQeEEu2-5X_1pMNzUUzkJRKfYj39ZrDtWDehY78RiQAo21OGMfaBfSMEOb66iiGcopmvPW8CYVTooL0_c_HyVMChEwBO8X1JFE6VWFsjzBt3heh8_PztdYFcKgsmH3RMizxRqemZJBx_MJUug3hPcDdC1ZKYrdY3LS1YA5MzTNHI_xpNCktp85FfgNGBsyPAs-ZHf7i1Mnb9-hdK5KqPzsvNX9sU4S3VXa9y8mHRFxf5a5AzQL2ixDqqdh8TrD3Uy9YLrR2go7A4Q0DfTzWMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sr3YLvAHUUQt8ePQ5971GZz554tS3Ol_2o_mgZ0VKnIfLWl8YMQflbf2YwawfrnQe2ZIlIYBEHUXpl9fDMasf3vsFOsQ8fQFjq4g4PZnAoOxGRmClcTyNte_7-Hl-b-4Ta1cIrcR9KOyub55Glmvw8tjIi9t_e4voBjG1GvuXQ1jyLNSdy-Wz14AuX8mxLtcfAioj27rdyISQjgLH6BXPQwDMA0C9k6LL3-Nj87UG1oCmvKgAeUlfQ_EA0Aqx1ob3UL7NAUhhzzO055gKMPPFX4TPw0t4n4iy0abDm-pRPwJSYrAcAo5UiMDoVzQjGK2DLYv275OhVSmNB16HB0vLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j28wtBRApeV1DGaLD38lHWskOS1KDB1ijkgJx2SHdGJcFD2le6qa4GyyXYnc96WQb3tWgKgKCIgVmpzB0qR7lqhwkjjrh4gmnV1pEMrmWzgQ1qFQ51nDs7wFMWLo2zB2YOHsbXmjx2INp0iiVyDwLQKg5At9XbNA065Y9Hj7fdtdpJJAl-aOopUmKdYu-AWH2_r4FoXfJhjFqmPZ6tXWElJhkxq7FC7darvgDJVGrTTp3aV4PAZtB1Jta12M1b71jid2HpCeWTPfBSmo1p9kYVnVfXqeUquRk8yOdHZvDcYp3HRO0tzCFSZLoxEbKf24G7MgOhE5j1YYswuAbxausQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KSnj8cgfHxtGN3R9Wm7NjsMbxg7pSNSmbxftA8xspc4JmqZJakeoiOs_MvMV3VIvf3IhdpR-o8UL8KiGrXK5jJvLltU80jDPj-AuRvYCmV5ecyMwiNdt7agiLAhXZt41ME4D8DvsOYZ11aCyAUU7go3is3BA2LbackqetMN1koUK5TR_qKjMIb_O1WoYHN0M_Q5k8sIBQn5FrRWJvOxocYRggS8qXN4WTEOQnXRm9RFnMNzO7Oho0cVScZ_-bcAVrRgVUhpO1wveCx9ycqL6ne0J4Ym_Vfpz2Nm2O01CPC_RrBb1dmcKWLrqPo7rCIbrjr9yjcXEk4z_AhbwrKQ_sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iuvNflKp9AIM-W0Nud1wWmvqNMEmeA4HzA9MXqqG2c0VOhhdUgyjAY2DvDV-8tROyLA6are5aAsuCN87zQJfSrqLfNjYcEwfSbHuaMBMWUokQfVoEFx8-7GxOzDB9c74a7_msab389bwsBcUGDVtPkHBQajGKPualgbQH3c1bKepJx-i58zHdy1IqqPxzz1NCTRCBW6ok9tIJdVZkZH2se8ws7Mf0a6apYVYwoRRObcvcyf03SVvIh9jh-Be1NfrRIPAGqAffl1wV9b-4-1M80hQDYYJeNDmv3Gv1l3p8pQYsH5NWAO5Pnp3G9TLtNR6miS3qcm9RFfFEwP0xFL1Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MUozarujoOZtCVmIN3JoKaD9oRFDxycfW_fDeHgVNBTDRH9WSKYhcbehFQfOeKeLPImk4UVuxRKGhgpdrto4CWM_QXx5X_LK6xx36AryWZ84g0uzNFmNxfpwAHX9GoXuDQRcJz9rCVpOwhrXshgW67NTS8eiQnup9Wx65SDkt3gFa7WMCLf_YBnpfVzAU1yUQJ3CLteOjAyA7VH85QACK7Kwkvt2NmG06xSK3nW1url7YGfFpwtCJDsYxETux2YEUWUxPbusO-1RKoo_S9fOIfjePYcB9UggUXyj-LbwopGPrM6fiYVmrFF-7-xJzkAaa61RFNoW9hHd0qkJmd5l_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HlMAvFKRfNR475WEb4SNICZxaUFJhwkyjZXDMNB8Beu4sxKnfDOWTjCKnnLgDjCC6UkWW4pzXEYnLCtoNJvQ_v7R-m4U2CzV0nTP4KrwVYTY9d_n-9bq3QuovCy-Gzu9JC6OVW3Vn-a9wn-nhx_cw9qWGZpXOwxyelDoRPadEIFt4bkL9zvlao_pkOPxbn3jLxBRtOtP-LxWQ0Tvhw58swDcesaWgU0uuBA0pS7uPE8_u_wCp2xKJpivGv_IJiHgRrqqgQnLF63pjCRHvOMthI68XpqJ81r_w1pSwK-kyFTlVozyPn5Khj07eiYGLCZjYJey38VeZaAktysLDwLiiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DN1uzXQ7IyJlw25jm8TCBMD80vnf9u-ElY4SRqq-kdxV6ZsTi-apR3028g2YibO317pMlUU35vVCgpIuCOxj1Noq8WX5RXqbCyJWC6IA1CsTi4bCRmuUCMr48I1n3keoWjfJK27FJuJrJ0YBHrVBHcJigpSAAtE77tsevYZEi0PAc7GT3myI2CbtGUsjUCdt-M6nGiTzFjtoTc9Lo5ULAQyP_tYzo4oumgBtCKCOMX7QpytoQtd95fRzxHcywtO5HFM0fm8tjlqwcJcs7KBVvJl_Pmf_ReQ00h2UWJKEiEiptx-xf7AqO9QEtq6SdQJ4q4zcZAFITNox5Lxwt6cLqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V3iIC3108TZIHqaBBRXjQjte6ZQR-WBA7aZYAIfd_QOz9wsOdIzGm_QI4p4AlRMw4CkvCLmtATm_5WM2HsLz9bRYbGvwSm51uy3mERB92g0PSKgvcGFTyIhlyZDjTuzywZ6CuSlwN4kmF5HYwPXpCrgnxWlWxYsyW3VHOuVqdCIw-P1gj2m_33s6Iq-Tbn4iZ2VdvY4WH785PSgW5a61eSYrxu5fvVCGSmbVQUmzcyyeXj0knmMm55709U1thHOreXvkKreVfEII876K8HWlkeYuIk1bojFjP8VOE3i3fhmjCqHQzrEN7nUr0QOlMUH8F4v4ej9fI2o5Vu7OkV6OxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر خبرفوری از آخرین ساعات وداع با رهبر شهید در مصلای تهران
🔹
عکاس: سمانه صالحی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/667028" target="_blank">📅 18:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667027">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
تهران بدون آقا معنا ندارد/ زائر رهبر شهید در گفتگو با خبرفوری: تاریخ ایران مدت‌هاست مرد ایران‌دوستی مثل آقای خامنه‌ای به خود ندیده است
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/667027" target="_blank">📅 18:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667026">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7sC4saU3VHDecWZG3fCF5Ud0ixYycWFa8oSVQrDsUGVIPez-dEa4CJBV-Ee72BP6DUgtutnFuemJqWJvsS8751j-7QRWufoMNloiYXh3kEnzwT4Upqszmy4EPkSzRUFqNvjZd2kemaNeZabKKXMeKN9ZwZa4_ZKr3EmyABCW7t3J2dre-wAsS1-2HYvVZe2XWlNhc28rS4s5S4ARbh-xThmXJJgNV1eCDhGnCoofA853rOusRC0H9N_OCVd-xZ65ImkZqPVsugqWbAsElftfMA3pB8Hwemb5w0Q88nipYnUqw3zeuUxVUE-l81X-rnJAFEEJsoZcZdss9JSzcE8vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگ‌ترین تشییع‌های تاریخ جهان
🔹
تشییع «سی.ان. آنادورای» در هند با ۱۵ میلیون نفر، پرجمعیت‌ترین مراسم تاریخ از نظر تعداد مطلق افراد است.
🔹
اما از نظر نرخ مشارکت، تشییع «آیت‌الله خمینی» با حضور ۱۸ درصد از کل جمعیت کشور، بالاترین رکورد را در جهان دارد.
🔹
تشییع «سردار سلیمانی» نیز با حضور ۷ میلیون نفر، سومین بدرقه بزرگ تاریخ محسوب می‌شود.
🔹
برآوردهای اولیه نشان می‌دهد که مراسم روز دوشنبه نیز احتمالاً یکی از رکوردهای تاریخی تشییع در جهان را جابه‌جا خواهد کرد.
@amarfact</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/667026" target="_blank">📅 18:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667025">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf6bbddc91.mp4?token=TkxjEm4DOkyzlkiWIDU3Wyeoh6-vThuWAYxbyl4zUtTvdd6iMos99dV2huMuP33XXQJ-f8cTBbaIJsekMRQze7eWzdYoxTjXiRBwe41hM_zijHW4je5t_MAyOxBw_58-M8g6sheJJagptky4FVI7vtt1fevB-wHfiFtpvyU3KIETgbWpKEkUQzLe8L1kuE9W0zfBAAe2D0aigppw_YacQbaMeVOS4AWNQk0SyNOx79w26jOlyeWWzdNPlySvCtPoAwFNOCrdr3axvojE9YfhXBEsARuzlBtQqtxJ22C8--Hy_usrva-KK8Bo0RkCU-XOmiIIlub-Y4tSlKW_VrKHjQuKqlI5XfKNoc91KVr5PdgMzkGv5rd_X4qJXk7aX4VFsvOnI-usEsTdSVV5ZzlHztNcCOwOGOz-0JKgwt2u48LcFS97MUWnPFk7f01b6garCe0BOncY8xBbmmrMTZYLQ4RkyedznkwT9ppTRZGpdOYygRnhMokbgVUpsXC6ZpWG9q4sr_pcBJXkUeMCcR16MkwmZ0C2gXmE0ZkmOxKlKuVZ8wHDEQxsuhmaHQPPwe73nfNjusmnd1I4e6xQPjWx_Yb0PBaLj01jEG8Vd2szPGcc1UdHBmwvOL6sY1XmUx2LiBodzPSycYKRdeYE-ag65f0-kQR3HWAhY1YX_bRLyfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf6bbddc91.mp4?token=TkxjEm4DOkyzlkiWIDU3Wyeoh6-vThuWAYxbyl4zUtTvdd6iMos99dV2huMuP33XXQJ-f8cTBbaIJsekMRQze7eWzdYoxTjXiRBwe41hM_zijHW4je5t_MAyOxBw_58-M8g6sheJJagptky4FVI7vtt1fevB-wHfiFtpvyU3KIETgbWpKEkUQzLe8L1kuE9W0zfBAAe2D0aigppw_YacQbaMeVOS4AWNQk0SyNOx79w26jOlyeWWzdNPlySvCtPoAwFNOCrdr3axvojE9YfhXBEsARuzlBtQqtxJ22C8--Hy_usrva-KK8Bo0RkCU-XOmiIIlub-Y4tSlKW_VrKHjQuKqlI5XfKNoc91KVr5PdgMzkGv5rd_X4qJXk7aX4VFsvOnI-usEsTdSVV5ZzlHztNcCOwOGOz-0JKgwt2u48LcFS97MUWnPFk7f01b6garCe0BOncY8xBbmmrMTZYLQ4RkyedznkwT9ppTRZGpdOYygRnhMokbgVUpsXC6ZpWG9q4sr_pcBJXkUeMCcR16MkwmZ0C2gXmE0ZkmOxKlKuVZ8wHDEQxsuhmaHQPPwe73nfNjusmnd1I4e6xQPjWx_Yb0PBaLj01jEG8Vd2szPGcc1UdHBmwvOL6sY1XmUx2LiBodzPSycYKRdeYE-ag65f0-kQR3HWAhY1YX_bRLyfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهبر شهید تا لحظه آخری پای کشور ماندند/ زائر رهبر شهید در گفتگو با خبرفوری: به عشق وطنم و دیدار با رهبر شهید از زاهدان به اینجا آماده‌ام
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/667025" target="_blank">📅 18:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667024">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
نتانیاهو: با ترامپ بر سر چشم‌اندازها توافق داریم
نتانیاهو در گفتگو با فاکس‌نیوز:
🔹
شکافی در رابطه با ترامپ وجود ندارد و هر دو رهبر در راستای منافع کشور خود عمل می‌کنند.
🔹
اگرچه ممکن است اختلافاتی داشته باشند، اما همواره آن‌ها را با صراحت و باز بودن مورد بحث قرار داده و به راه‌حل می‌رسند./ خبرفوری
#Demon
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/667024" target="_blank">📅 18:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667023">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
خروج ۱۱ هواپیمای سوخت‌رسان آمریکا از منطقه
🔹
منابع نظامی خروج ۱۱ سوخت‌رسان آمریکا از غرب آسیا را تأیید کردند؛ تحلیل‌گران این عقب‌نشینی را ناشی از تغییر محاسبات واشنگتن، مشاهده انسجام ملی در مراسم تشییع رهبر شهید و نگرانی از واکنش احتمالی ایران می‌دانند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/667023" target="_blank">📅 18:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667022">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f08dd5b763.mp4?token=GNu4x8NX93CYW6ixqtGYABBHJC9bIJxczzpVFKjO6ZT4e47iN-GPoIbhi05HiiPPyLSop44ImYRT0WV4Z6q4bD-xb5U5FsCBJ7BkfbTVzuQ54CRpMLjxpB3B6SDAWzAoNpnddjhQ4c1zMRxqSlJCXDonAUx9aTT2SK3DCR1Rd1RjF9aH0k8M77G2Z9D1GXSAbD8ep2gEPwjcO73duA5WGqjEh2qPRJ8dpKvknK_IfG2kFEPI02z8-OXvMS4_-48rUJ2ECW_D8P2Wd5H8pceyKQLSeKX2Gw5dz6OprebIKPtkWBiqY2v5azGadOVPLIhCk2tRxi3AmmlEEDRwJ09Q51Bpzmpcdl7QcGv4o-6wXO1RB-LMdxdI2fHEgR4hgZUT46o90x5Qsptx2CQB2CBi3A-PZawF7aSLBJesvyxZK_kfu8FvnQkwJ2ui5aRvQcue-3MQCxGnqmhHJ-2QVAgih53p1ZLlfDJ5ud-sIxDhPSmIVGWWpEPP17yTEWbl8URBoljhbnMpTqPDYXPX0JzJGb-MbSWx1gT6V7M4G4qDTrcmjaEIkjtyE-Wlt9QEnNs8P_Ch9aLlgbdWAJ9fk35_QICBJa2RAkXvTvktMHrfqAh1nkF42oINsvwvQBGwYdavDva5R-T75bsVUFfidmF6tOwZAyfBSBek2rAObEpH5wk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f08dd5b763.mp4?token=GNu4x8NX93CYW6ixqtGYABBHJC9bIJxczzpVFKjO6ZT4e47iN-GPoIbhi05HiiPPyLSop44ImYRT0WV4Z6q4bD-xb5U5FsCBJ7BkfbTVzuQ54CRpMLjxpB3B6SDAWzAoNpnddjhQ4c1zMRxqSlJCXDonAUx9aTT2SK3DCR1Rd1RjF9aH0k8M77G2Z9D1GXSAbD8ep2gEPwjcO73duA5WGqjEh2qPRJ8dpKvknK_IfG2kFEPI02z8-OXvMS4_-48rUJ2ECW_D8P2Wd5H8pceyKQLSeKX2Gw5dz6OprebIKPtkWBiqY2v5azGadOVPLIhCk2tRxi3AmmlEEDRwJ09Q51Bpzmpcdl7QcGv4o-6wXO1RB-LMdxdI2fHEgR4hgZUT46o90x5Qsptx2CQB2CBi3A-PZawF7aSLBJesvyxZK_kfu8FvnQkwJ2ui5aRvQcue-3MQCxGnqmhHJ-2QVAgih53p1ZLlfDJ5ud-sIxDhPSmIVGWWpEPP17yTEWbl8URBoljhbnMpTqPDYXPX0JzJGb-MbSWx1gT6V7M4G4qDTrcmjaEIkjtyE-Wlt9QEnNs8P_Ch9aLlgbdWAJ9fk35_QICBJa2RAkXvTvktMHrfqAh1nkF42oINsvwvQBGwYdavDva5R-T75bsVUFfidmF6tOwZAyfBSBek2rAObEpH5wk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زائر هرمزگانی مصلای تهران خطاب به رهبر شهید: اگرهم شهید شدی راهت ادامه دارد!
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/667022" target="_blank">📅 18:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667021">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
گاردین: مصلای تهران؛ پیوند عزاداری و فریاد انتقام
🔹
گاردین نماز میت رهبر شهید را نمایشی سیاسی دانست که در آن سوگواری با شعارهای انتقام گره خورد.
🔹
این گزارش بر حضور میلیونی و فداکاری زائرانی تأکید کرد که برای شرکت در این بدرقه تاریخی، سختی اقامت در خوابگاه‌های موقت را پذیرفتند.
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/667021" target="_blank">📅 18:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667020">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUGSHO_GaT5hDjeDQ28-on5uMr4TF_cDo4yA6Y8urg5dvp_SVwOHMZeOHpRvAbHx3LRioZX6jQex_HTy0m1mTHYbO4vM8mDJSVJIxS3noiiUgo4I9023TdG2R72fOZzSDAT4ODjH1Y7qkF7B08vjUqgW7lIIvK08vD7f2MxulZ7CCdcWKBK77O4ckb3B9DVulZN6eSWg85klNeeLzmSdi63VZ4_XYzaVKX5F97kgRfc4yLmi-z1rEbjyXDEW5_mNz7i9JfubDtgm4hVBB-jtNyw_-zWHOxQvJstdAhYJwdfVJCcCBbnX9oTPc7xisFRVayzkDAEjVOC5BMgdJycdiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غریب آبادی: ایران نسبت به هر حرکت نظامی در تنگه هرمز هشدار می‌دهد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/667020" target="_blank">📅 18:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667019">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2427250249.mp4?token=cIanVyjqvKABrhYjzS2-D9ldbwpYYQkWeCc_cHfLlAYTr-uj-oDZTcfbx0c9IVjbUrOoOkNtlyn5eazS-xFVrllu6lXZbZY2cyz8L2rwbA8Ag0mt4KoM6509AaznVbAqlA-UPRG-TYQrj6rd37cQ35TFPgJgM5vn2j7UKrnSHvo0mUjK4Sh1FKLkamJJQ8HqEtkj5NGI3h0ur3Fv7p9FYCORp6O95MxrJI0sqxukhZYyOyWwTatR7GtN4SORtLlpGhXVbFajy4G_-aPF-8gk8os4jX2nfX3BTNJHCaPkXGNJdeJYlNlBGZ0p5smPsnqAT8WMQzAEe-7D5vDix5GHrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2427250249.mp4?token=cIanVyjqvKABrhYjzS2-D9ldbwpYYQkWeCc_cHfLlAYTr-uj-oDZTcfbx0c9IVjbUrOoOkNtlyn5eazS-xFVrllu6lXZbZY2cyz8L2rwbA8Ag0mt4KoM6509AaznVbAqlA-UPRG-TYQrj6rd37cQ35TFPgJgM5vn2j7UKrnSHvo0mUjK4Sh1FKLkamJJQ8HqEtkj5NGI3h0ur3Fv7p9FYCORp6O95MxrJI0sqxukhZYyOyWwTatR7GtN4SORtLlpGhXVbFajy4G_-aPF-8gk8os4jX2nfX3BTNJHCaPkXGNJdeJYlNlBGZ0p5smPsnqAT8WMQzAEe-7D5vDix5GHrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله هوایی اسرائیل به جنوب لبنان
🔹
ارتش رژیم صهیونیستی شهرک النبطیه‌ الفوقا‌ را در جنوب لبنان هدف قرار داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/667019" target="_blank">📅 18:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667017">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a564c37c16.mp4?token=s0C0z6SNrlyCuJfjCLn1fytXE-Xd40xRlbMbwTtSAri6GiIHEI_buAFfO-Ia7up3MOqpSU0McTW9hN4R-HOLxc1fgAK_Ovqt0wyYlrWEabTwsdAZWPzdjf1I6vo6iGtaHP0D65jlttXFOBx14UOym1qsp8nxj01uobbI1XG2IwVCBxevD-fURe1vPXsnwtuHpO65yFPpj9lKP9Y7heCzTniH9uN2oV2fW-tgpg8191xwphFn7Fyi2m8Rppr0-fXeItpKafTR7atY1zVlB8WylbeAwGBqclTiviqMoDe5uP_CrpxfAQBAFI5IbyXVTY6THXW5slxHi1kG98GmLJtyjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a564c37c16.mp4?token=s0C0z6SNrlyCuJfjCLn1fytXE-Xd40xRlbMbwTtSAri6GiIHEI_buAFfO-Ia7up3MOqpSU0McTW9hN4R-HOLxc1fgAK_Ovqt0wyYlrWEabTwsdAZWPzdjf1I6vo6iGtaHP0D65jlttXFOBx14UOym1qsp8nxj01uobbI1XG2IwVCBxevD-fURe1vPXsnwtuHpO65yFPpj9lKP9Y7heCzTniH9uN2oV2fW-tgpg8191xwphFn7Fyi2m8Rppr0-fXeItpKafTR7atY1zVlB8WylbeAwGBqclTiviqMoDe5uP_CrpxfAQBAFI5IbyXVTY6THXW5slxHi1kG98GmLJtyjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نماز بر پیکر رهبر شهید از زاویه‌‌ٔ خاص!
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/667017" target="_blank">📅 18:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667016">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8778a7daa8.mp4?token=YOq-eas0vtCMqSZpgpvxgEIXEQLdzVz_URDBu6Hkt_QB-A4zJThzB8a42nDkRNh0zzDKPcOZceOElXT51uq1hXw0Tm7wDafLXOI9-wwRYYYqljyLJrJ7OnsercX5Fve6RexyEmRfs2cMV5Vz_kgy2VKJLScDWk00_QuwBLr6Wm6CqaHogjJpsRUyvslPCRPSYhUf7U8mIo9kKZ-gzFEq77NybJPnJ0sGOgdtO9L5m_pJ32ndpJJEfNtbPoDxMeAa5r0RcrjSiaSXt0-J7X2WE0n9RvpGu955-YK-YC1kXXU4OwdsusS9OOu9QE5FU0GRVyt_hHkoq48h6aaaP-2vyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8778a7daa8.mp4?token=YOq-eas0vtCMqSZpgpvxgEIXEQLdzVz_URDBu6Hkt_QB-A4zJThzB8a42nDkRNh0zzDKPcOZceOElXT51uq1hXw0Tm7wDafLXOI9-wwRYYYqljyLJrJ7OnsercX5Fve6RexyEmRfs2cMV5Vz_kgy2VKJLScDWk00_QuwBLr6Wm6CqaHogjJpsRUyvslPCRPSYhUf7U8mIo9kKZ-gzFEq77NybJPnJ0sGOgdtO9L5m_pJ32ndpJJEfNtbPoDxMeAa5r0RcrjSiaSXt0-J7X2WE0n9RvpGu955-YK-YC1kXXU4OwdsusS9OOu9QE5FU0GRVyt_hHkoq48h6aaaP-2vyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غمی که تا حالا تجربه نکرده بودم/ زائر رهبر شهید: با تمام وجود پیرو راه رهبر شهید هستیم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/667016" target="_blank">📅 18:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667015">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1e80fa060.mp4?token=J73DmsUGnwy8FaJEHfDkA6QyqZZi_pBgZdqv5TdCEgI5Sqd_Q_8bSnX20y7pgV99hvXrmbnH8gdgkECW5vlOBzZVyeNnkQSkaB_91e3rHKMm-WJobjKsgI_3Pn8VUjYeo6oLHyB1VL2fBhzeHBZr0noGT5nd8cT_3_i4gG2VF8nWBAogi8kplS7spIKa_C6fhh61KTII3muWTMl9no-1VsHU987vRFpEtKr3t_psqf28rWyCK9UT682G8iwgvffGgX8YPVB6tzT_WiPcWWX-UbzrfDRBWG02E7gXdWl_NcuV9oAMXNYXgfMuvN_L0Q8Kya8t-X4FJROcN6a06TlZjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1e80fa060.mp4?token=J73DmsUGnwy8FaJEHfDkA6QyqZZi_pBgZdqv5TdCEgI5Sqd_Q_8bSnX20y7pgV99hvXrmbnH8gdgkECW5vlOBzZVyeNnkQSkaB_91e3rHKMm-WJobjKsgI_3Pn8VUjYeo6oLHyB1VL2fBhzeHBZr0noGT5nd8cT_3_i4gG2VF8nWBAogi8kplS7spIKa_C6fhh61KTII3muWTMl9no-1VsHU987vRFpEtKr3t_psqf28rWyCK9UT682G8iwgvffGgX8YPVB6tzT_WiPcWWX-UbzrfDRBWG02E7gXdWl_NcuV9oAMXNYXgfMuvN_L0Q8Kya8t-X4FJROcN6a06TlZjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زینب سلیمانی: شهادت آقا برای ما سنگین‌تر از شهادت حاج قاسم بود
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/667015" target="_blank">📅 18:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667014">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4e22e537d.mp4?token=H9OwG0uwRx7M3EdKE_eforlNa3Ohuqv9FaKYZD269rA6M8WxPkIfnNEwWUvBu3kUhhECliM-bguVaGRlQufviEpdXzQjS7oKxzKkCIr26imFAlcqOglHbrunnkgebWOVhXMcamh_6fdeV5-9e9luPnAy5Xza9BBg2XrgYN8gn__HGNuqamtAcur-QOhX-hlmw9LIbd-0TOjfj16iioA3WbOL8u5pqWYFtv9lb2kcnXViR6vkZ1Bpzpvq-4zhl7gZHZluXMNuuTXsVMjxF2_bXpq96efyePfPFI4_vS5K32swEKYrKdC-t27AJmvOhIzX1q9Mv8EiJOIzQ--W5gDNT2Gl7If5ztMaNPKUNSxyxW2T4nxs-8_Ud5fgu-iAHxzVbzv_hyJqO6n7qbkMn3gZA76l8oyuci-lHO4xQkiRGzxpPM1YPoueAaQsJlSXtA5dkQGhK_8hnjTCLObzE3PyYdfM7adRjfhldCifhp4dRLbJ74LBP2aHIKuYDqKsY_qZ81rXvJBYmfnsjgT4QpbvHVKGcY0ASvyJioPLBD5aBMd4GzS3N-OE87XBnhwMeFzn5r9c1foYIIom5BF2M52ZjJsRvQVQ4MIIgPDkdIEXRpvBYV6yYMf5V9uJBO0Y7MLhOgqO_JeG3gh2pZoj1KMd-oA8VRx3dlbNgN3WPekwiaI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4e22e537d.mp4?token=H9OwG0uwRx7M3EdKE_eforlNa3Ohuqv9FaKYZD269rA6M8WxPkIfnNEwWUvBu3kUhhECliM-bguVaGRlQufviEpdXzQjS7oKxzKkCIr26imFAlcqOglHbrunnkgebWOVhXMcamh_6fdeV5-9e9luPnAy5Xza9BBg2XrgYN8gn__HGNuqamtAcur-QOhX-hlmw9LIbd-0TOjfj16iioA3WbOL8u5pqWYFtv9lb2kcnXViR6vkZ1Bpzpvq-4zhl7gZHZluXMNuuTXsVMjxF2_bXpq96efyePfPFI4_vS5K32swEKYrKdC-t27AJmvOhIzX1q9Mv8EiJOIzQ--W5gDNT2Gl7If5ztMaNPKUNSxyxW2T4nxs-8_Ud5fgu-iAHxzVbzv_hyJqO6n7qbkMn3gZA76l8oyuci-lHO4xQkiRGzxpPM1YPoueAaQsJlSXtA5dkQGhK_8hnjTCLObzE3PyYdfM7adRjfhldCifhp4dRLbJ74LBP2aHIKuYDqKsY_qZ81rXvJBYmfnsjgT4QpbvHVKGcY0ASvyJioPLBD5aBMd4GzS3N-OE87XBnhwMeFzn5r9c1foYIIom5BF2M52ZjJsRvQVQ4MIIgPDkdIEXRpvBYV6yYMf5V9uJBO0Y7MLhOgqO_JeG3gh2pZoj1KMd-oA8VRx3dlbNgN3WPekwiaI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظر فعالان رسانه‌ای بین الملل پیرامون شخصیت قائد شهید امت و حضور میلیونی مردم در مراسم وداع
@TV_Fori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/667014" target="_blank">📅 18:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667013">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92a8bd9036.mp4?token=BWgXWOl-7GoifMoB4Irfjm_mzSLo0n1UwcmeUfXXBpgDgKAF8Saa2IgRekfVcwL6j3A5ncX95ArQ1kFwQZf_7h0hZCMqOkHdUdGTcmCXy4mvk7KiHuqPkmdCwA92r5owhBap1HSnxGNBrwjt4yJNGywJsym4WXn9YijUXoFViLl0x6cuIUkUcJZSXELPd6KJB549J9gBVWQLtb8OHzjztUfhuirWSnUQ9EFuIoLXFBixyPTyU1Lu7qTnkdIf2wUF69HdduWWmJccBy60ph9H_vQ_FcQ-9YPST4XnVwA1kMdhr07QzvF34mbgCCof4hgwx3fcPcDjQOJAxPdBp4uJJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92a8bd9036.mp4?token=BWgXWOl-7GoifMoB4Irfjm_mzSLo0n1UwcmeUfXXBpgDgKAF8Saa2IgRekfVcwL6j3A5ncX95ArQ1kFwQZf_7h0hZCMqOkHdUdGTcmCXy4mvk7KiHuqPkmdCwA92r5owhBap1HSnxGNBrwjt4yJNGywJsym4WXn9YijUXoFViLl0x6cuIUkUcJZSXELPd6KJB549J9gBVWQLtb8OHzjztUfhuirWSnUQ9EFuIoLXFBixyPTyU1Lu7qTnkdIf2wUF69HdduWWmJccBy60ph9H_vQ_FcQ-9YPST4XnVwA1kMdhr07QzvF34mbgCCof4hgwx3fcPcDjQOJAxPdBp4uJJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مترو بهشتی؛ این همه لشکر آمده، به عشق رهبر آمده...
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/667013" target="_blank">📅 18:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667012">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
آمریکا از یافتن تفنگدار مفقود شده ناامید شد
ناوگان پنجم نیروی دریایی آمریکا:
🔹
عملیات جستجو برای یافتن تفنگدار آمریکایی که در حادثه روز چهارشنبه گذشته سقوط بالگرد در دریای عرب مفقود شده بود متوقف گردید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/667012" target="_blank">📅 18:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667010">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7dfd9edeb.mp4?token=MXWN1VlsBjwa4431XxwZGDSe4ck2P5NXaXs9iViRIe_-LLmtfs3ttKPt6j9sDBPRoSHehTEV53hzYDnyf1E_oYj6Aogh56yI1GywyiUANBInb8xbnHpDk05Rzf2F0blScMvJeJKHvegKr1OSYrF3stT1QfyrCPC9eNr0UmRg4eabzV_OKqqQohVbzfBypCMErJqONb1_U80PWDkntY2tuiYL2b-xGyZOxoyir_ps1_WQ-cGo7AhkcWWz79Q1lO1pnlcx9BRgOmz2RE-7kjw3-0Z1KvgG1IlY-QJVAe9Z63-lXilFr1TwbgOMVbLQzodY1YE---KFQXjECmPoHPvLFFqJOqZcp6F4MM_6YAIgBLnKazkNaUkj7Kq1cgA4aGM5utP2hUnFi792DfrrgA4_vDQTC5K8_CbONnducb6JwA17RFqmB9ymz4KpDn51gRhgFNevBH9DdqT51Bwh1S_hQGU6fFP6CO7rhlesQDrmnaDcmaOn7K48fH5mGFc_paVPa8sQ8BIuam7KE58CEh58vcB-rOdKmbi9bWLZGQbS3Mz74eLw7MJlpHuJPyBCmMr-0dLYCLNKSEoY7-OCXkcZVU3LO7C82JCXWS_mnS50j6Yzi8HmsabMfnQ__ftodEJ-a_CsXOLKg7nr2ljtCGynw_59gLxEEP2HUc3XYVyBQqY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7dfd9edeb.mp4?token=MXWN1VlsBjwa4431XxwZGDSe4ck2P5NXaXs9iViRIe_-LLmtfs3ttKPt6j9sDBPRoSHehTEV53hzYDnyf1E_oYj6Aogh56yI1GywyiUANBInb8xbnHpDk05Rzf2F0blScMvJeJKHvegKr1OSYrF3stT1QfyrCPC9eNr0UmRg4eabzV_OKqqQohVbzfBypCMErJqONb1_U80PWDkntY2tuiYL2b-xGyZOxoyir_ps1_WQ-cGo7AhkcWWz79Q1lO1pnlcx9BRgOmz2RE-7kjw3-0Z1KvgG1IlY-QJVAe9Z63-lXilFr1TwbgOMVbLQzodY1YE---KFQXjECmPoHPvLFFqJOqZcp6F4MM_6YAIgBLnKazkNaUkj7Kq1cgA4aGM5utP2hUnFi792DfrrgA4_vDQTC5K8_CbONnducb6JwA17RFqmB9ymz4KpDn51gRhgFNevBH9DdqT51Bwh1S_hQGU6fFP6CO7rhlesQDrmnaDcmaOn7K48fH5mGFc_paVPa8sQ8BIuam7KE58CEh58vcB-rOdKmbi9bWLZGQbS3Mz74eLw7MJlpHuJPyBCmMr-0dLYCLNKSEoY7-OCXkcZVU3LO7C82JCXWS_mnS50j6Yzi8HmsabMfnQ__ftodEJ-a_CsXOLKg7nr2ljtCGynw_59gLxEEP2HUc3XYVyBQqY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار خبرفوری: احتمال دارد مراسم وداع با رهبر شهید تا ساعت ۲۴ امشب
تمدید شود
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/667010" target="_blank">📅 18:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667009">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
کپلر: تنها یک کشتی از مسیر ساحل عمان عبور کرد
🔹
روز شنبه ۱۹ کشتی از تنگه هرمز در رفت‌وبرگشت عبور کردند و فقط یک شناور مسیر نزدیک سواحل عمان را انتخاب کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/667009" target="_blank">📅 18:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667008">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d426f58a35.mp4?token=HlInNs0gBL1ix0UZGCGWdYsRmq_BZ4QqtMZAuHTmBFTO_L0i95QicgPfi2J89ON02cY87MCpj8ffKjlURnA-k7LOuvJDWPVqpjcKBl7QXdPahwaszX1QX58qoSNivfhI7agopuo-COqEVL4bVS07PJYUw-FSGE8AYf9mRxY19uRn4uBL8oI_0gscNcSBGPkBoTBvRFs6_J7hV0rsUniNRpQkLr3r-Gs95dVRARkACsrOPgOra6Be6opYuP9UeuMtYEDecCkwnGeS0OG3i13AimydcR8emf9VC64OXdYQsAVvAnEHjYCWFKYjTSI0wqDVYLyqs7OEoLfA6RLZa8NPGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d426f58a35.mp4?token=HlInNs0gBL1ix0UZGCGWdYsRmq_BZ4QqtMZAuHTmBFTO_L0i95QicgPfi2J89ON02cY87MCpj8ffKjlURnA-k7LOuvJDWPVqpjcKBl7QXdPahwaszX1QX58qoSNivfhI7agopuo-COqEVL4bVS07PJYUw-FSGE8AYf9mRxY19uRn4uBL8oI_0gscNcSBGPkBoTBvRFs6_J7hV0rsUniNRpQkLr3r-Gs95dVRARkACsrOPgOra6Be6opYuP9UeuMtYEDecCkwnGeS0OG3i13AimydcR8emf9VC64OXdYQsAVvAnEHjYCWFKYjTSI0wqDVYLyqs7OEoLfA6RLZa8NPGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار خبرفوری: در ساعات پایانی مراسم وداع قرار داریم و هنوز سیل مردم به طرف مصلای تهران ادامه دارد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/667008" target="_blank">📅 17:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667007">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84e6fda38f.mp4?token=EwWVo0BBJ3QqZEHbdZst0DRsY4ka3ArG7ovMpyRyadB0Q_mYExqGhDD6lBQHH7Nes8_U0i1YG4QJt18OXtdOiQjD3ALoxNQ-LS9gi4diNqla0x3eXsUQ2kaiUP7id3NPf3BRVUK1LKc32PY8-5PRBLE6--mKbDkd6dvStlZDutt46Rk0jrAUKRLUVRQiyNz6Z4EKsU9F7BXg3d5apNID2YiIjDbpz-0I05LnVpRPOi9UuS-A5L-GIixoeacrgCpFUS_lvrE5Rz-DkRBQeX4QrbQvqJxBy2vxxG6yb2iPSCPxjW5a-WM9xQb50OkObzwSVme0RJot7EY7do5V8VZ9eIWQpUSe5GKW6jEi33CSZpf8UhZhzkBb9rjcp8Sa46R7GeeF87nn5HJoyKFj3gaIkH42EopEYvFz8ot5vEEw7Bh41h4T-j4iKsG6Ng9Tp7phnFHCKXm9DdYVm3sSaIs3F6btzmZHy9-QYh-pFazOvnLHlV1yqVlnU9L62seBJo-1SOKAL2mVDoY3eMlT9SuO1iOLH4fvzaJhyEEZ5MV3_NJyIrGKVZzAeiVxnLNH1DnMmkgA5JbriKP6sxbXe6FodbJrLdq1ORguFf-dptKXOXObZdiNhM9FGQMR6JIQ5Jvyiw6jMH0DsP5I_DdyuSnMQ74QFlkq9NxLSyyMU9t7glI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84e6fda38f.mp4?token=EwWVo0BBJ3QqZEHbdZst0DRsY4ka3ArG7ovMpyRyadB0Q_mYExqGhDD6lBQHH7Nes8_U0i1YG4QJt18OXtdOiQjD3ALoxNQ-LS9gi4diNqla0x3eXsUQ2kaiUP7id3NPf3BRVUK1LKc32PY8-5PRBLE6--mKbDkd6dvStlZDutt46Rk0jrAUKRLUVRQiyNz6Z4EKsU9F7BXg3d5apNID2YiIjDbpz-0I05LnVpRPOi9UuS-A5L-GIixoeacrgCpFUS_lvrE5Rz-DkRBQeX4QrbQvqJxBy2vxxG6yb2iPSCPxjW5a-WM9xQb50OkObzwSVme0RJot7EY7do5V8VZ9eIWQpUSe5GKW6jEi33CSZpf8UhZhzkBb9rjcp8Sa46R7GeeF87nn5HJoyKFj3gaIkH42EopEYvFz8ot5vEEw7Bh41h4T-j4iKsG6Ng9Tp7phnFHCKXm9DdYVm3sSaIs3F6btzmZHy9-QYh-pFazOvnLHlV1yqVlnU9L62seBJo-1SOKAL2mVDoY3eMlT9SuO1iOLH4fvzaJhyEEZ5MV3_NJyIrGKVZzAeiVxnLNH1DnMmkgA5JbriKP6sxbXe6FodbJrLdq1ORguFf-dptKXOXObZdiNhM9FGQMR6JIQ5Jvyiw6jMH0DsP5I_DdyuSnMQ74QFlkq9NxLSyyMU9t7glI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
می‌مانیم تا پای جان برای ایران/ زائر رهبر شهید: هنوز باورم نمی‌شود این اتفاق افتاده است
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/667007" target="_blank">📅 17:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667006">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYiQXURU66w8iK3paaOD9yQ2-QntlUcMC8h87bGbgArOKlr7j44o37aJN5x8-y23CzmPC-N0BFtvJWij6IbKGdR94Knq4uMWAvEtHCVvHjx4xaqBAmZKUmNO4K0y56STZgL04GevZwhIhrao_djk2dlMaaEsGk8o7wvMTYcTn7OtGnoTYEL0Nb8RQh-VliSIFs1Z8vQeFmEh6OIE-bFxZAgzF3aeoVXafYMZCl24Z9Lh_E3ziBNz1ZXp8cBVJUVI3QwaU9yY_221Ttra0OTSx1PBkPQ8bqbllQS23VMZ2vKKVzmcKik5uEP7ryR9fGSpBcnUIJ4drJW0R9O6qUqSZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایجپت ایندیپندنت: خشم از آمریکا و اسرائیل در میان انبوه جمعیت حاضر در مراسم وداع با آیت‌الله خامنه‌ای موج می‌زند
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/667006" target="_blank">📅 17:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667005">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
باید برخاست...
🔹
مصاحبه خبرنگار خبرفوری با کودکان حاضر در مصلای امام خمینی(ره) تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/667005" target="_blank">📅 17:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667004">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/644005e68b.mp4?token=SMwZT2O7NEN547FrykfDFr_3lqxu-P_1avQFB6B0-yq9zSeCS6_SmGZsiU3QXcXE4MaoM-b_JdpBDO0b8tXo1VA7TF11BFRbfv5PQrp1Rbc-cjwbtqhkGG-awPRc0TYAwd5xclbPkDsf_d_uHqou6ZicvViRN1NZ--S9RVZ6_gFn4EnWvZX0VbjCGA8esxOc3RrpFk0peHPILuch7O2vLJK9KYZS3E9NIUkpNSm6YgmaxFxkJW01wwdJDx0_jrGnXIyuMduYIiqcrz_IBPay-t4qsPiGCCXx4o7ADwJUb7HOryA8qXByKauMzYIAtw7GRi1xr9w2m6rXUOxF6DiyzTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/644005e68b.mp4?token=SMwZT2O7NEN547FrykfDFr_3lqxu-P_1avQFB6B0-yq9zSeCS6_SmGZsiU3QXcXE4MaoM-b_JdpBDO0b8tXo1VA7TF11BFRbfv5PQrp1Rbc-cjwbtqhkGG-awPRc0TYAwd5xclbPkDsf_d_uHqou6ZicvViRN1NZ--S9RVZ6_gFn4EnWvZX0VbjCGA8esxOc3RrpFk0peHPILuch7O2vLJK9KYZS3E9NIUkpNSm6YgmaxFxkJW01wwdJDx0_jrGnXIyuMduYIiqcrz_IBPay-t4qsPiGCCXx4o7ADwJUb7HOryA8qXByKauMzYIAtw7GRi1xr9w2m6rXUOxF6DiyzTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فریاد‌های هیهات منا الذله عزاداران رهبر شهید انقلاب در مصلای امام خمینی(ره)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/667004" target="_blank">📅 17:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667003">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
قالیباف: خونخواهی امام شهید، آزادی قدس است
🔹
رئیس مجلس در دیدار با رئیس شورای رهبری حماس تأکید کرد دیپلماسی باید با تکیه بر توان دفاعی، دستاوردهای میدان را حفظ کند؛ وی با رد به رسمیت شناختن اسرائیل، تصریح کرد که حمایت از جبهه مقاومت ادامه دارد.
🔹
درویش نیز تفاهمنامه ایران و آمریکا را پیروزی بزرگ مقاومت دانست.
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/667003" target="_blank">📅 17:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667002">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار قم(Admin)</strong></div>
<div class="tg-text">♦️
۷ موکب، ۲۰ هیأت و اسکان ۶ هزار زائر؛ ورزش قم، پای کار خدمت‌رسانی
حسن سلطانی، مدیرکل ورزش و جوانان استان قم در گفت‌وگو با
#اخبار_قم
:
🔹
جامعه ورزش استان قم بزرگ‌ترین عملیات خدمت‌رسانی خود را در مراسم تشییع رهبر شهید آغاز کرده است. در قالب این عملیات، ۷ موکب و ایستگاه صلواتی با مشارکت ۲۰ هیأت ورزشی برپا شده است؛ به‌گونه‌ای که ۳ موکب در مبادی ورودی شهر مسئولیت استقبال، راهنمایی و بدرقه زائران را بر عهده دارند و ۴ موکب دیگر در نقاط مختلف قم، خدماتی از جمله توزیع آب، یخ، شربت، تغذیه گرم و سرد، خنک‌سازی محیط، اسکان و سایر خدمات رفاهی را به زائران ارائه می‌کنند.
🔹
همچنین اسکان بیش از ۶ هزار زائر در روزهای دوشنبه و سه‌شنبه پیش‌بینی شده است. تمامی سالن‌های ورزشی و خانه‌های تخصصی ورزش پس از بازدیدهای میدانی، تجهیز و آماده‌سازی شده‌اند تا خدمات اسکان با بهترین کیفیت به زائران ارائه شود.
🔹
در موکب‌ها و مراکز اسکان نیز ۲۵ پزشکیار مستقر شده‌اند و نیروهای تخصصی پزشکی ورزشی به‌صورت مستمر در محل‌های خدمت‌رسانی حضور دارند تا در صورت نیاز، خدمات اولیه درمانی و امدادی را در کوتاه‌ترین زمان ممکن ارائه کنند.
@akhbareghom</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/667002" target="_blank">📅 17:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667001">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
شورای هماهنگی تبلیغات اسلامی: مراسم تشییع رهبر شهید روز دوشنبه، ۱۵ تیر، رأس ساعت ۶:۰۰ آغاز می‌شود
🔹
مسیر تشییع شامل خیابان دماوند، میدان امام حسین(ع)، خیابان انقلاب، میدان انقلاب، خیابان آزادی، میدان آزادی و بزرگراه لشکری است.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/667001" target="_blank">📅 17:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667000">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9b00af8d5.mp4?token=CKYuLs4yBDFVEKz6Q4VnAJUbp2BdRVEFW8a3Tp-5yH9d_PZnzXPs6SDS1-cbUPb7bjOoMG7PblHogp4FuKFee8Sofl7MHcVXzRAhFmGMFPrbbyLv1DPKmogdJryzhNKPq5uciglT2ZQZ5qsOHIL08EnpCa3AiAntVYO7q8Bm_jKcU_p-4QabdREk-ooo2RoUZHRFqX5FyDQwtUHDCy00-tk6lyNG4LsTwlEygoFgZIeOMKIJ8X1EGUALJYVBkrSUjkpst_9jiVIaNfdro_IYsdlYsJtqllveiMaACA_5eQ-4MFHELwDYGmmIkBqvIHdSClZ7lICAmxu8ARaRyHaupXsoQbjSI1QfEA0AuL65rcPqGnvbf5SYQMGE_1RYK4mePAqTitiKtrYhi7ueZmaQVCXQCoJUBclMkIaHN0IFASktF95GL-Ihk3_JCtN8-IJ4EqJPw3eSwPGnKx4vXiyYu3dcjIDczksTpEkXrUM7m-IeUTYYBCyQmLQPltdYkserGMHVvaGi4w4AlatdtZaKSeqTIxGBhRTOEf_L3eFskiu7_bHGNzoy8ozqLKWPBS6jcoLbjBImGa08Rdz14l1anrMn2ZhMPhONHwp4n1hNruXkn8wZAUKAN8K09BANX_63YLPKZVQoXxL3uIgiarwkqCvCl-UXpynxrMqkioWFNVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9b00af8d5.mp4?token=CKYuLs4yBDFVEKz6Q4VnAJUbp2BdRVEFW8a3Tp-5yH9d_PZnzXPs6SDS1-cbUPb7bjOoMG7PblHogp4FuKFee8Sofl7MHcVXzRAhFmGMFPrbbyLv1DPKmogdJryzhNKPq5uciglT2ZQZ5qsOHIL08EnpCa3AiAntVYO7q8Bm_jKcU_p-4QabdREk-ooo2RoUZHRFqX5FyDQwtUHDCy00-tk6lyNG4LsTwlEygoFgZIeOMKIJ8X1EGUALJYVBkrSUjkpst_9jiVIaNfdro_IYsdlYsJtqllveiMaACA_5eQ-4MFHELwDYGmmIkBqvIHdSClZ7lICAmxu8ARaRyHaupXsoQbjSI1QfEA0AuL65rcPqGnvbf5SYQMGE_1RYK4mePAqTitiKtrYhi7ueZmaQVCXQCoJUBclMkIaHN0IFASktF95GL-Ihk3_JCtN8-IJ4EqJPw3eSwPGnKx4vXiyYu3dcjIDczksTpEkXrUM7m-IeUTYYBCyQmLQPltdYkserGMHVvaGi4w4AlatdtZaKSeqTIxGBhRTOEf_L3eFskiu7_bHGNzoy8ozqLKWPBS6jcoLbjBImGa08Rdz14l1anrMn2ZhMPhONHwp4n1hNruXkn8wZAUKAN8K09BANX_63YLPKZVQoXxL3uIgiarwkqCvCl-UXpynxrMqkioWFNVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یزله‌خوانی و ادای احترام عزاداران خوزستانی به پیکر رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/667000" target="_blank">📅 17:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666999">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
رسانه آلمانی: حضور میلیونی در گرمای ۴۰ درجه
🔹
دویچه‌وله با «تاریخی» خواندن این مراسم، جمعیت را «دریای سیاهی از عزاداران» توصیف کرد که با وجود گرمای ۴۰ درجه، با حضور هیئت‌های خارجی و ابعاد سیاسی برگزار شد.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/666999" target="_blank">📅 17:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666998">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9200c8b77.mp4?token=jWnX7fq4xb0M7jxnu9aIquWIwZo-PcsXH-0rkjrWABHYTP2T4Nbrp76AmV3a3hJW96iik1krNX-FAF8aBlVL6EvX0hGMK1x3Gsr6po5ckEDG_vVHMFSEqRBgd-M79CTn-TzPz8FQCGuKiTS_9fQygNI02CC5OxJ2MOsdPDwartH5wZeT2kM9NeL3P_pH5A-l5sS8AMjxnINf0IHTSlDFNrDF1u9ONjuYxJz21dO1Jr61_UXajtEJtUKRS-XPtY8sIShpOHkR7VrFZigeFvcuowK-CZmZPStZBol4D3C8MYEJ2lyKThi6njqE1WS89vY4RIZ9pKrvGcWlwrx6UFNKUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9200c8b77.mp4?token=jWnX7fq4xb0M7jxnu9aIquWIwZo-PcsXH-0rkjrWABHYTP2T4Nbrp76AmV3a3hJW96iik1krNX-FAF8aBlVL6EvX0hGMK1x3Gsr6po5ckEDG_vVHMFSEqRBgd-M79CTn-TzPz8FQCGuKiTS_9fQygNI02CC5OxJ2MOsdPDwartH5wZeT2kM9NeL3P_pH5A-l5sS8AMjxnINf0IHTSlDFNrDF1u9ONjuYxJz21dO1Jr61_UXajtEJtUKRS-XPtY8sIShpOHkR7VrFZigeFvcuowK-CZmZPStZBol4D3C8MYEJ2lyKThi6njqE1WS89vY4RIZ9pKrvGcWlwrx6UFNKUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ايمان قياسى: تمام دنیا درحال تماشاست که رهبر شهید ما چقدر طرفدار داشت/ آن آدم معلوم‌الحال توییت زد که فکر نمی‌کرد این میزان جمعیت را ببیند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/666998" target="_blank">📅 17:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666997">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqlL__vXxLx7QMOEv4qoNgR3C214uDi_-qqhgH7eZy6FSW3wJ5CZoucDz3x6Pj6QJS9X5U2bHRVjyxiKhvCRiuh-3BNZ1MfwYBRp1Tx3NL-PWtg_BVkN8_vQleBlgMhMqrcjfYBXkEEGllK4JdcAZxgiRvT1nwNAcPrfPe3rLosmnyuGkRj6IHaA3X-pyfGpjurns_22RTfix730phvh6EUk7ZderhTfiHcQGKdX2FSc1mAQfp-X6tYW5BVOWHZewrjuBXxWMBgNDrXtOm4BtYNSttfAhXBwyWhFZreaeP5Qt8KVJjRCn8r_tF4lptpEQpQ5Y_iZ_Ufiq9nYlXCiqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت مراسم تشییع رهبر شهید؛ پویش مچ‌بند سرخ
🔹
مخاطبان عزیز خبرفوری، برای شرکت در این فراخوان کافی است با یک مچ‌بند سرخ در مراسم تشییع حاضر شوید و تصویری از حضور خود با مچ بند سرخ را با ما به اشتراک بگذارید.
🔹
مچ‌بند سرخ، پارچه‌ای به رنگ خون و نمادی از عهد، وفاداری و خون‌خواهی امام‌ شهید است.
🔹
بیایید در مراسم تشییع با مچ‌بندهای سرخ حاضر شویم تا پیام ایستادگی، حق‌طلبی و عدالت‌خواهی را به نمایش بگذاریم؛ پیامی که نشان می‌دهد یاد شهیدان زنده است و جنایت و ترور از حافظه امت اسلامی پاک نخواهد شد و همواره خون شهیدان خود را مطالبه می‌کند.
🔸
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/akhbarefori/666997" target="_blank">📅 17:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666996">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
رسانه قطری: بهبود حمل‌ونقل هوایی جهانی پس از تفاهم ایران و آمریکا
الجزیره:
🔹
پس از امضای یادداشت تفاهم میان ایران و ایالات متحده و بازگشت تردد دریایی در تنگه هرمز، روند رزرو پروازها بهبود یافته و نشانه‌هایی از احیای حمل‌ونقل هوایی جهانی پدیدار شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666996" target="_blank">📅 17:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666995">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/709110060d.mp4?token=IeS8xsniS38KgxjccVhVp6P55xnERdWNKv26vneLIEIBnzEfDkTAW-zN1SBGHzDufS7LNYZP6138Rlb9LFReOAYO-eaI3IHZr6ZDiAvOssBTdjNM61GNTP8_SmFUxuhWyP2Ep91HMcBAqu0FisCT1HWtPF2YK5A4Vp9G48uwR9tBIAoNkPeULi3Ci1owC4eLSAG0eFLYNPAa6huX1uX_pXI7SAA7mikIi-XJ08HgW1lpgAwuGkMWQrjR4ILuJDBpSSwmn4h7RA7GW1OoLBJ8zPHo_tvGmaSWjqdrISxa3_IHWL93YnQrr7ofiiVyBa5l-NuL05UmcDPZwHoyFIs3Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/709110060d.mp4?token=IeS8xsniS38KgxjccVhVp6P55xnERdWNKv26vneLIEIBnzEfDkTAW-zN1SBGHzDufS7LNYZP6138Rlb9LFReOAYO-eaI3IHZr6ZDiAvOssBTdjNM61GNTP8_SmFUxuhWyP2Ep91HMcBAqu0FisCT1HWtPF2YK5A4Vp9G48uwR9tBIAoNkPeULi3Ci1owC4eLSAG0eFLYNPAa6huX1uX_pXI7SAA7mikIi-XJ08HgW1lpgAwuGkMWQrjR4ILuJDBpSSwmn4h7RA7GW1OoLBJ8zPHo_tvGmaSWjqdrISxa3_IHWL93YnQrr7ofiiVyBa5l-NuL05UmcDPZwHoyFIs3Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خونخواهی، میراث کهن ایران؛ مسئولیتی بر دوش مسئولان
🔹
طلب تقاص خونی که به جور ریخته شد صرفا مطالبه‌ای ملی نیست؛ بلکه ریشه در فرهنگ تاریخی این ملت دارد.
🔹
سیاوش در فرهنگ ایرانی با مظلومیت خود به نماد جاودان عدالت بدل می‌شود و کیخسرو با برپایی داد، نه تنها خون…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666995" target="_blank">📅 17:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666994">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
آغاز فروش بلیت قطارهای فوق‌العاده تهران-مشهد برای مراسم تشییع
شرکت راه‌آهن:
🔹
فروش بلیت‌های قطارهای فوق‌العاده‌ در مسیر تهران-مشهد از ساعت ۱۷ امروز آغاز می‌شود.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/666994" target="_blank">📅 16:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666993">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22624cd3fb.mp4?token=i7TEwbyAd3-0EItqya7z7Iue_lyD1hbY78PjT5o0DuWeb63sjk3nX2OlBuXgvMcG6sbKsGRZLQzkpxTt74X2PlONxclW1OJTWaT2yv4GnI09hxxr1dmawHr8wLpCXP-CR1dq004UQOGxaxGT-moz6wL_Ha7Po8Q29sUlTmGVrC-N-RZo1bSjHt_2oAauWOBD8s3Z2tgt_SKg-tX8OByXfF61fIwJFJ9TPfubbG6eSKf1RxZR3lKdMgkmP_1Pax8OJxHN9XsrGbxvfJYFq1zGTG8C2XDkH1e3vevapi38emyJcVQjPdD1-jJI9FNw3_OlOpRFDJu1j3ccPCw49nlOlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22624cd3fb.mp4?token=i7TEwbyAd3-0EItqya7z7Iue_lyD1hbY78PjT5o0DuWeb63sjk3nX2OlBuXgvMcG6sbKsGRZLQzkpxTt74X2PlONxclW1OJTWaT2yv4GnI09hxxr1dmawHr8wLpCXP-CR1dq004UQOGxaxGT-moz6wL_Ha7Po8Q29sUlTmGVrC-N-RZo1bSjHt_2oAauWOBD8s3Z2tgt_SKg-tX8OByXfF61fIwJFJ9TPfubbG6eSKf1RxZR3lKdMgkmP_1Pax8OJxHN9XsrGbxvfJYFq1zGTG8C2XDkH1e3vevapi38emyJcVQjPdD1-jJI9FNw3_OlOpRFDJu1j3ccPCw49nlOlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقوط چترباز آمریکایی در مراسم سالگرد استقلال
🔹
در جریان جشن دویست و پنجاهمین سالگرد استقلال آمریکا در ایالت کالیفرنیا، یک چترباز پس از اهتزاز پرچم دچار حادثه شده و سقوط کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/666993" target="_blank">📅 16:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666992">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه البرز</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09e0806ea3.mp4?token=q7rc7Gw6GHSYdJQBKhzlbD9MrAihvlZuCFV79FqSXqYLw4SUhDj-o2eVikPjo1Jbja8V5YLJG9Xd1ZKWN2JWmYF22oYMYFngVbByWEbP0Pl6DPKMUiSqUmZt2HO3ucoMO6xm1K5gMFtEXT6yUkWMdcjkiC4GZptUEw1QUOpYIl4xYVEiDS6s323IXmaPQmVnASWlK-Udd-oRHLzqbXUrtfuiWN7hDMNraOpERiSjuUpzk5lShxxcbq5LmFDjCKJfK8IdJjIZwE9MwU6J_u-P-rnbMD5qEeFZ6uu4ENV4oZp9KnsLYFdsCtKBPmQ-siCKnyhhwER26RoUOokKsMNVSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09e0806ea3.mp4?token=q7rc7Gw6GHSYdJQBKhzlbD9MrAihvlZuCFV79FqSXqYLw4SUhDj-o2eVikPjo1Jbja8V5YLJG9Xd1ZKWN2JWmYF22oYMYFngVbByWEbP0Pl6DPKMUiSqUmZt2HO3ucoMO6xm1K5gMFtEXT6yUkWMdcjkiC4GZptUEw1QUOpYIl4xYVEiDS6s323IXmaPQmVnASWlK-Udd-oRHLzqbXUrtfuiWN7hDMNraOpERiSjuUpzk5lShxxcbq5LmFDjCKJfK8IdJjIZwE9MwU6J_u-P-rnbMD5qEeFZ6uu4ENV4oZp9KnsLYFdsCtKBPmQ-siCKnyhhwER26RoUOokKsMNVSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیما نوراللهی مدیرعامل
#بیمه_البرز
:
تمام توان و سرمایه بیمه البرز در خدمت زائران آئین تشییع شهید بزرگوار ایران است؛
از برپایی موکب‌های پذیرایی تا استقرار گسترده تیم‌های تخصصی ارزیابی خسارت.
در مسیر دلداگی، همگام با دل‌های سوگوار شما، متعهدانه به خدمت‌رسانی ایستاده‌ایم.
#بيمه_البرز_توانگر_و_ماندگار
#روابط_عمومي_و_امور_بين_الملل</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666992" target="_blank">📅 16:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666991">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
روایت شیپورچی مصلای تهران؛ در روح و جان من، می‌مانی ای وطن...
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/666991" target="_blank">📅 16:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666990">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd400c4890.mp4?token=YJjRvDrhKX0bdKbA7yq2Wij5Wsb7ahJ5tmLdhPYictP-AQr38IMgCYogCeZ5usIGJmKzlOl_nRFUWavSAh_g9cgsZAhH-spILFBnbP1fIYOQicgLYg3_Vn-kwjX126Zdnzl57M__DIAMHKnNhlXrrQvM9R3NDa3NFGdy9JSA-eFO-0v-HFdNgAUGC7ew5xQ7qRy0SxJCEuIhytm6nF28Hef2FsDXoOynRCBNIEMFeQTeEaR7c3999DX-UUdb7q88axdSKv2Fk81kNSRwwRb0fB9WMorNCsvkzOhPiV4fa4yHNxQcULdEcPbLte9zb34wP-Rb28728qHkG1Tq4wN7MRymnIe_EAMZXtdYsAGdPAE2cgt1zQ_jd_iRCGIepuFfszL5E3ztdzogCbSQ1vzTmNJSopsX0dQ3m2gOwvuIUA9_YtThHctx6cONpT8B3a29D9K-Tp_JstUWURE83bl9SI3akDThZE7Ey778lUwPO6imQnpZ9Eu3ai9K-mImeS4DFaiMlic09hPJrye8T7onPRi1zvwfDYl2u6tJ1nXhwkTNarcX6EAwSoMrxG-EwB3Fso6U_-WoHC8fi3A8eEpbMSsxp7oVjJSp17skFneEJEhepKewBD71rOe7jUp3FyA3DwfjRVcrsImOPOZMbdiDt6fLX123AzCFxJVlj9iS-yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd400c4890.mp4?token=YJjRvDrhKX0bdKbA7yq2Wij5Wsb7ahJ5tmLdhPYictP-AQr38IMgCYogCeZ5usIGJmKzlOl_nRFUWavSAh_g9cgsZAhH-spILFBnbP1fIYOQicgLYg3_Vn-kwjX126Zdnzl57M__DIAMHKnNhlXrrQvM9R3NDa3NFGdy9JSA-eFO-0v-HFdNgAUGC7ew5xQ7qRy0SxJCEuIhytm6nF28Hef2FsDXoOynRCBNIEMFeQTeEaR7c3999DX-UUdb7q88axdSKv2Fk81kNSRwwRb0fB9WMorNCsvkzOhPiV4fa4yHNxQcULdEcPbLte9zb34wP-Rb28728qHkG1Tq4wN7MRymnIe_EAMZXtdYsAGdPAE2cgt1zQ_jd_iRCGIepuFfszL5E3ztdzogCbSQ1vzTmNJSopsX0dQ3m2gOwvuIUA9_YtThHctx6cONpT8B3a29D9K-Tp_JstUWURE83bl9SI3akDThZE7Ey778lUwPO6imQnpZ9Eu3ai9K-mImeS4DFaiMlic09hPJrye8T7onPRi1zvwfDYl2u6tJ1nXhwkTNarcX6EAwSoMrxG-EwB3Fso6U_-WoHC8fi3A8eEpbMSsxp7oVjJSp17skFneEJEhepKewBD71rOe7jUp3FyA3DwfjRVcrsImOPOZMbdiDt6fLX123AzCFxJVlj9iS-yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهار شگفتی عکاس مشهور استرالیایی از ارادت شهروندان و شاعران ایرانی به رهبر شهید انقلاب در مصلای امام خمینی
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/666990" target="_blank">📅 16:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666989">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
ازسرگیری تجارت دریایی ایران و قطر پس از ۵ ماه
🔹
رایزن بازرگانی ایران در دوحه از بازگشایی بندر «الرویس» قطر به روی کالاهای ایرانی و ازسرگیری تجارت دریایی میان دو کشور پس از پنج ماه وقفه خبر داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/666989" target="_blank">📅 16:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666988">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
تکذیب ادعای مداخله ترامپ در عملیات‌های لبنان توسط نتانیاهو
🔹
نتانیاهو گزارش‌های رسانه‌ای مبنی بر درخواست ترامپ برای عدم اقدام علیه تونل‌های لبنان را «افسانه» و «اخبار جعلی» خواند.
🔹
وی تأکید کرد که هیچ‌گونه درخواستی از سوی ترامپ دریافت نکرده و اسرائیل بر اساس ارزیابی‌های خود عمل می‌کند.
#Demon
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666988" target="_blank">📅 16:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666987">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
تعطیلی الدیوانیه عراق برای مراسم تشییع رهبر شهید
🔹
استانداری الدیوانیه به منظور فراهم‌سازی فرصت مشارکت شهروندان در مراسم تشییع پیکر «قائد شهید امت»، روزهای چهارشنبه و پنجشنبه هفته جاری را تعطیل رسمی اعلام کرد.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666987" target="_blank">📅 16:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666986">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10ce3f1567.mp4?token=A3PbOXGIE9xSJBgd6dSlyTKAHI7jDWpgBAfln6ZdIYVXe1ic4BVaZwXq6k2C-iGGsEkDx6R1myD6Jdc6PR8rWWMBtn6zj2lTaQJ9fr6SSDfpSOreBnMgAR8cdiAC2nlr0aBVkVuf0uZR7DnauORxKfGmevH1b1DG9vbhk91MSDFK6ip5DQi6QHIhXdQdLcGmsasbMZCC67-88sbn70lPKGsB-r9_tsUWCzYSNcd_ojCI-yBm1WItA4-cVsVWUITLqPvi6YxmUYEfLV3bWvWoi7m7_WcbXmPQdVDW2sgTCPU-xFex2_Sjo6kUaV_OsJPNWTp0byyLlAZ9Q4wf0AMS-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10ce3f1567.mp4?token=A3PbOXGIE9xSJBgd6dSlyTKAHI7jDWpgBAfln6ZdIYVXe1ic4BVaZwXq6k2C-iGGsEkDx6R1myD6Jdc6PR8rWWMBtn6zj2lTaQJ9fr6SSDfpSOreBnMgAR8cdiAC2nlr0aBVkVuf0uZR7DnauORxKfGmevH1b1DG9vbhk91MSDFK6ip5DQi6QHIhXdQdLcGmsasbMZCC67-88sbn70lPKGsB-r9_tsUWCzYSNcd_ojCI-yBm1WItA4-cVsVWUITLqPvi6YxmUYEfLV3bWvWoi7m7_WcbXmPQdVDW2sgTCPU-xFex2_Sjo6kUaV_OsJPNWTp0byyLlAZ9Q4wf0AMS-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی: ان‌شاءالله بتوانیم پرچمی را که رهبر شهید ۴۰ سال در دست داشتند با افتخار به دست بگیریم و پیش ببریم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666986" target="_blank">📅 16:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666985">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECH5pA_tqgIDcUxvqHxV0Dg90smWV_JuOPt_itNlU_JesHxCdMw_5Tkm5QgaWT3-mK2O5oKTagaRvKWlj-wulkQd-3tRRIrPkMRmQDoFjmSZixRAM8ow6KGhfaT5o9BrN1VJ9TBB8LRcbr08TLpg8Y250he5Cna1VVPvheJHbe7P451RBfLT_Vczgy2kWTUzVv2MS7Bx-vsovpJmVibbYTRGdHvw40XthwM7i7Wwvvv0teNQVGCRUNgvhUPabvd_J9wvtjd-2X4zW3_Q-iR7mgfbLTIeUNa3RrT1vlnm68HGzlVp9PAjAsx5OhJ-Ti-qP3tqD48rzThhZwy0IedeqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعتراف رسانه قطری به حضور میلیونی در مراسم تشییع
🔹
رسانه «العربی الجدید» با اشاره به حضور گسترده مردم و مقامات در مراسم رهبر شهید، به ثبت بیش از هفت میلیون سفر مترو در چند ساعت و اهمیت سیاسی و اجتماعی این رویداد اذعان کرد.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666985" target="_blank">📅 16:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666984">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9BdESwfZnDOjseDhoUWb4GxGVfcFhDoxU6AxWSrFjzu_4Tcw_f9TsJzuURQUoz2bH4-pj3YICPBhGQt7KSAXlcoaqiIBJwBwvlY6c90JBqjxNaIo2o9KgCMQdvdglAGpUDrKp0Gj0qj92Ib3bGaCc832f02FboOziXUMYKjLC2fxFNSyxJ7Alcb2QCAGmt8PTF4CflRb9dVbIuonn_aeAC2dq6uKNd86glkkpqKS7PMpWlzNeiQPSY3iyKT_LyFcaPcoq8nXpIbukXBqiPGnbYEvxWMYwA_PKW1Iur6FyUhSMs4-WS3TJVKtNu9tCjqrwwoa7xrhxwgFs-7nXlY_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حرکت مشترک سه پلتفرم نمایش خانگی همزمان با مراسم تشییع رهبر شهید انقلاب @AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666984" target="_blank">📅 16:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666983">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
پهپاد شاهد ایران، جنگ‌افزاری مدرن را دگرگون کرد
وب‌سایت نظامی Defense Post:
🔹
پهپاد شاهد به یکی از سلاح‌های تعیین‌کننده در مناقشات معاصر تبدیل شده چرا که هم کوچک است هم ارزان و مرگبار.
🔹
شاهد یک، پهپادی که کسری از هزینه یک موشک کروز متعارف را دارد، همچنان می‌تواند زیرساخت‌های انرژی، تجهیزات پدافند هوایی و گره‌های لجستیکی نظامی را نابود کند.
🔹
این پهپاد مدافعان را مجبور به صرف هزینه‌های بسیار بیشتری برای هر درگیری نسبت به هزینه‌ای که مهاجم برای هر پهپاد صرف می‌کند می‌نماید./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666983" target="_blank">📅 16:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666982">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
اینا اصلا سوشال مدیا بلد نیستن!
🔹
براندازا جمعیت ۵۰۰ نفره خودشونو در رسانه میکنن ۱۰ هزار نفر!
🔹
اونوقت ما جمعیت ۱۰ میلیونی رو ضریب که نمیدیم هیچ حتی نمیتونیم در رسانه ثبت کنیم
🔹
راه‌حل: بیا وسط و تولید محتوا بکن. راوی باش!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/666982" target="_blank">📅 16:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666981">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OiFvRCQnpOX-Pe9kEQiTC193snDXJpvCW4A6VIQ1WVwQeeobL5BhWmmJBcFzWbBZMTHLzYzhYxijUradzQNHRb10bPPKzSlxrilE1S11Nt1pOYIg-ar80k30k9nM_ijrZAFnieIntsuP5uO9qfryOpK-Z3A5PArVowqnXXsngDIhFOLZGFuup3gWknVtEkifTSIGjvvRr6yl8zObk_PkeRLyP8GyTfqkoI3TpiXVbfxQ2rJ2DZsqBKDJSiYWWSf_-VYkWnFNd6aln5tymZTr-gJAuu0IEOGPWqXiuT7DxlGfwy8QGe4R63KRWb03MDtyn_Q-L-ddgAks4JjVfmDtYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ما شیعیان قاتلان رهبرمان را مجازات می‌کنیم
🔹
دست‌نوشتهٔ مردم در مصلای امام خمینی(ره) تهران
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/666981" target="_blank">📅 16:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666980">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f11d7818c.mp4?token=m5AJxPFtKPFhJagb8jjXMTPF24vbAVQq1-AOFiEVCK3yFzGLa-K5AIwOyBinfa22nAIAmN5bb4jwG-yA2tOZ0sXca4TVfQCCAYWmg1j6c-gn-aCMHGQLZC1V1HACcoMDkRCjytrUXjT-w8CsJCP0wMP1QsgFOdJ2Yc8Vl3w-icZ_Zfsg2kfDko5jhPqbeGkKuHbLuEay6lGwtUAT6kXKSzdNP90VS7XDitlqQm-mOY0Fn-e5qGndHFtCU2nBGJddsN6H0LPR-RqG9jG5PMfvk5R7d5tculXzpKtOzeHZgi_5ZydqSCA0Niw5VUlo0bCr3ZXM92jODQiUdpsxzj9gsVwtiOYdah2je8MLHktuQcou4Im3hzWW6cBcBsS5J8uT9YJwLCdLvHIlfSnfXRn74QGO848eYN9Dzmy8aHtn-YUGsJTv-qhdxvqXMYI-i-eFAYsDvMnH8TG_rUPV1VZmEUAZzQzzBD3m0Ik0ezg1L2HOUaIy4R9r34mRZihnWcB8v_KZKJaJBYt_KZ9nsGDHPjiwTYFJXefxE6Rx29FBgPX99DevKWEd_fxnQ_f1uQlVdMkr0vBwahSUxUjL8Ujk_9O9p9ZCOPxh3OrqM2vXRgMRqVfSAd5R1vFWRH3zzfAFNpRzFpl_OygGtDQRNv56Mr4SLR2dVWV4dCbKuyRSxO4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f11d7818c.mp4?token=m5AJxPFtKPFhJagb8jjXMTPF24vbAVQq1-AOFiEVCK3yFzGLa-K5AIwOyBinfa22nAIAmN5bb4jwG-yA2tOZ0sXca4TVfQCCAYWmg1j6c-gn-aCMHGQLZC1V1HACcoMDkRCjytrUXjT-w8CsJCP0wMP1QsgFOdJ2Yc8Vl3w-icZ_Zfsg2kfDko5jhPqbeGkKuHbLuEay6lGwtUAT6kXKSzdNP90VS7XDitlqQm-mOY0Fn-e5qGndHFtCU2nBGJddsN6H0LPR-RqG9jG5PMfvk5R7d5tculXzpKtOzeHZgi_5ZydqSCA0Niw5VUlo0bCr3ZXM92jODQiUdpsxzj9gsVwtiOYdah2je8MLHktuQcou4Im3hzWW6cBcBsS5J8uT9YJwLCdLvHIlfSnfXRn74QGO848eYN9Dzmy8aHtn-YUGsJTv-qhdxvqXMYI-i-eFAYsDvMnH8TG_rUPV1VZmEUAZzQzzBD3m0Ik0ezg1L2HOUaIy4R9r34mRZihnWcB8v_KZKJaJBYt_KZ9nsGDHPjiwTYFJXefxE6Rx29FBgPX99DevKWEd_fxnQ_f1uQlVdMkr0vBwahSUxUjL8Ujk_9O9p9ZCOPxh3OrqM2vXRgMRqVfSAd5R1vFWRH3zzfAFNpRzFpl_OygGtDQRNv56Mr4SLR2dVWV4dCbKuyRSxO4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر پربازدید از بی‌تابی زائران برای امام شهید در مصلی امام خمینی (ره)
در این ویدیو تصاویری از امدادرسانی تیم های عملیاتی هلال احمر به مردمی که برای امام شهیدشان بی‌تابی می کنند در فضای مجازی پر بازدید شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/666980" target="_blank">📅 16:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666979">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aad5c3ce99.mp4?token=JukvfTLVAYYsMFjHpWRnPTOOUgl5mWUoiVBv1tvmGr9raQ28BDGbVR9XX7CtGOpepU-S5pbXOqkfKaVava9uqGAfKZXiR3nG0IO6hc7n0LvmkrcQ4N0TYQjyb8DKxtUzLBmT5K92Dd9UA1YK5XmLpZmj2gMIbKS2QmJ46PtPy40yBOhxCJKaBlNJk-y1jcxcegMoqCC83gcGOnARCX3d_6pJtfwMdZ-uTt3GHTCe7nPqAzW0H_JIzEH1Mb6Db5mCWZIYRZ8-SB7lXrzh4EekBD1OTId--vCAzj3PO23NtisAIsBKcqNonB4PpuUyQCSWD8lQprOYC_QUD-xrWFsR3KozhHVkcOMwlEat0Qcbu18D41xuRQZR9ljC8sQQdjTe6EjikGWsIC5JOCuLpBRNIuq5vz7dAimIPNJylA7dazlZbp54VwUewK8gCURShkxaNmo_GpqZyvaK94vivzGGAES2FOj3XgdHAaOubu5FpQhhcRVF6UXM4m2_D2aZIZLqx0vt5H5YRDbVoTo0sqkcl2KzWBDdCe_U3-11cQVJ1EzYCP0tBhY2iMYKMAR6IXy9b0a17L0bKTeokd85FQaAOSQxed5Z_mZ8OHze-E08m75uXZGNy65ZtVimTCVp5TBpUz--WmclQQlUEWLUujtnCnETAwLELZG_x09WjMFLWSc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aad5c3ce99.mp4?token=JukvfTLVAYYsMFjHpWRnPTOOUgl5mWUoiVBv1tvmGr9raQ28BDGbVR9XX7CtGOpepU-S5pbXOqkfKaVava9uqGAfKZXiR3nG0IO6hc7n0LvmkrcQ4N0TYQjyb8DKxtUzLBmT5K92Dd9UA1YK5XmLpZmj2gMIbKS2QmJ46PtPy40yBOhxCJKaBlNJk-y1jcxcegMoqCC83gcGOnARCX3d_6pJtfwMdZ-uTt3GHTCe7nPqAzW0H_JIzEH1Mb6Db5mCWZIYRZ8-SB7lXrzh4EekBD1OTId--vCAzj3PO23NtisAIsBKcqNonB4PpuUyQCSWD8lQprOYC_QUD-xrWFsR3KozhHVkcOMwlEat0Qcbu18D41xuRQZR9ljC8sQQdjTe6EjikGWsIC5JOCuLpBRNIuq5vz7dAimIPNJylA7dazlZbp54VwUewK8gCURShkxaNmo_GpqZyvaK94vivzGGAES2FOj3XgdHAaOubu5FpQhhcRVF6UXM4m2_D2aZIZLqx0vt5H5YRDbVoTo0sqkcl2KzWBDdCe_U3-11cQVJ1EzYCP0tBhY2iMYKMAR6IXy9b0a17L0bKTeokd85FQaAOSQxed5Z_mZ8OHze-E08m75uXZGNy65ZtVimTCVp5TBpUz--WmclQQlUEWLUujtnCnETAwLELZG_x09WjMFLWSc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاجیک، سخنگوی عملیات وعده صادق ۳: در خصوص خونخواهی رهبر شهید انقلاب همه مسئولین و مردم با هم هم‌عقیده هستند و گوش به فرمان آیت‌الله مجتبی خامنه‌ای منتظر دستور هستند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/666979" target="_blank">📅 16:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666978">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
رئیس ستاد تشییع رهبر شهید در تهران: تشییع به صورت زمینی و با خودروی مخصوص حمل پیکر انجام می‌شود
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/666978" target="_blank">📅 16:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666977">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
گزافه‌گویی لاپید: اسرائیل باید زیرساخت‌های نفت و انرژی ایران را بمباران می‌کرد!
یائیر لاپید، رهبر اپوزیسیون کنست در گفتگو با تایمز اسرائیل:
🔹
اسرائیل باید در طول جنگ اخیر با جمهوری اسلامی، زیرساخت‌های نفت و انرژی ایران را بمباران می‌کرد. نتانیاهو با خودداری از چنین حملاتی اشتباه کرده است.
🔹
اگر می‌خواهید دولت ایران را سرنگون کنید، باید اقتصاد ایران را از بین ببرید و پس از آن دولت بعدی [ایران] باید آن را در طول سال‌ها از ابتدا بسازد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/666977" target="_blank">📅 16:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666971">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/admRKy65mTsw0rHYYUhLOqirCLe83Dpqz9s6pPFWKBa4kmVIdfdu7V-_OerN_M4854KFJkKKbAnTRs1EvJJzX2wd5D3lFnpt0_NGh2BbeAQit78AibPGXi2LOFTuEQe4v9X1NH83Dc24xaXj1ojWz3qaRzhL3WM6JR2RilPRdToytuoUMu3QTquKBQm_yt-yVSG0Wajm-w0wtLxCkwrkc5kgfN7AIVf_mgbjBdIP-abunhVDABPMrfC2P_g6NKzAx9fbCeciKM3V0Z3T7phbGKN2hF0_FcgRI3JitPNzgEKcceSr8eVpyhcQohIghVQ_WZFPvP8IW-5_uRP1ySdIBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z-hWtnROe-OOm0fMiZLbxqfIFEqeCzc0WzP83SNseWICG2xEnMNTpEprBiomP0geg8M-hT6IJNyNLN7dQUoOhyVHlso8VIpyldOZ2NtEEfEP6yLKwMdHI67xBGOu-dYdH2fsP34yZ79GyhxbHLlf7ZBDtjpp2fWT2Fo7W_cVf6wiX2GBa3_-Fy22E-GStsoHL97ZFyZ2E_ZqcLfcGMz5HRoB-hUX8za65AUqA625uyOYMJzebPqYuew-yML2fZXhIAWjofJTK_1E4rvAw9PyKDFxqsCgdaLMfwOddjsjZkIcMXSawWlqJl0zZ50dnsgTFtFbtjGPNOINuiF7gfxh3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RYDOoJRrIAPLDH7oOHsYUg1mGuSwaIlcnIbhC3Xeg1sLlAVjeMTshpkfJYJCExRNfE6z1xAohbqEUgu-FXctlTl5wFcVb9t5HNBhjCrIo0rNXk-gfFCA40C2fbywrqNTlbk17LuAReGRORhVuXhJ0S9fOlkwcRLX3ZlhOCWo_u_OIfbZ99htX8ZP_cU3j96Qgxa2t6_E6klYG_-g8w49uqYxDUBWQtnA7qGCdHoxhBaKcVUEHGCIYqdxrZPU14CQ2eGWNshNfWtcdleskdjxwzV2vEuyZk9U9XjSlZzWeV5zSgq9v4wrOY9t_G879lK81sklfgTVTkJUZsfbEXf2_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KGX9pOZWxoQm7JnYzsmZjlGhuMos1iK0XR5dU48zDz8eK2xsAp-UUR8nBiYPZS8dE2ep63wJV90SWfpbOTCfBIWr8B-1uMnWq-ddRyy1Ztncx8sTmPM1tcyxVBC8vQ9seLeLo97yw3VHNIqNHiGhWnItzBIuwmSbr_hkCVWFYnmtn8Qke4tnsrdkuDaNpgeevvDRTskACOpgmAkB-PHzfXhxMv8zrJ7W0gMuLEVIL1j3N_KLLoWCSUBf-kfQ_eS8PvDpTKhyP8OToBxl5tYmYPYqSNgkgYQ58o27_Q8ofh988HQY0Vt3w3yDyYi58RFmDnKmepWCE10rnDWWOyp_lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NpfoHH94KyhEFEhE3Zljh_wtYIoPV43Vfk2__ATliLwa1VIQ0fvJN1d05APluGAbouPevL6PLFEY1UEl30RWkVqwnAyz6erQyGJtEhtj3pXR4YqzTHGEJR0Lq9by7ogPmumnIfkwt78HUzjXIEsXAoOQUUozBbfIAqRn86TzouSRqXdCpBP9om2eGC53hImJbp5Khcuc00X3TzS8CDYxNEwgZC5npOCC0ToEGnJQU-CkbHu0az_b94UZyA-3HOqMVzbQDl1KNyB_TZ1z4oqN5d0weWtmlIncxsdLb_wwSjTXOe1HxxG7HJVTvsJk0tjmxX8PgQePQCghK7wZ5WHNFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dzkdZKNa_BDms1AdYtUQX7jZPmNlRVe65oKYpkvdjYslAiEQKiOvTKqwj85Y6XYr9MiNm_Yz8RSUQQLdhEWIkWkltae7CHvZEjtvB05xHf0jvGTiOffXcWKGi9GsJlvY2U3LLnFdmEFcf5W3OBGodUq-spHWGI2-rET_BvO9yx643Z3GWszYFSQZMxxeH_7h9lGxb_LZPGHPXF5TVox3UQJOA5-Nli6vgeKQeFdAdFxh_Ed46W4ZQ0AylrvQfETS7ZWUvK1gVtbdEf2SZ5FZCMAeCNO9ExpiLBEsgEODsnGqpAGSrAbo7dJjkv357YXffqQ1KXHmOeN3rZ7yp40uhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر خبرفوری از دومین روز مراسم وداع در مصلای تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/666971" target="_blank">📅 16:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666970">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
امروز نیز باید مختارهایی در کشور باشند تا انتقام خون رهبر ما را بگیرند
رئیس کمیسیون عمران مجلس:
🔹
خونخواهی رهبر شهید نباید فراموش شود و کشورهایی که در شهادت وی نقش داشته‌اند باید پاسخگوی اقدامات خود باشند.
🔹
همان‌گونه که خون امام حسین (ع) موجب بیداری ملت‌ها شد، شهادت رهبر انقلاب نیز می‌تواند خون تازه‌ای در رگ‌ انسان‌های آزادی‌خواه و حق‌طلب حتی غیرمسلمان جاری کند و مانند مختار در خونخواهی امام حسین (ع) باید مختارهایی در کسور این جنایت را تلافی کنند./ فارس
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/666970" target="_blank">📅 15:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666969">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3uLKLAqU3D3WT0JNZUF2_KkVbbvQ4Y14mC7a3uC8mYoEFOSIdvo28rCxuTW4wr1ekhYtPXyjEFhuaB94fWHxbkCK5BgnZ5cSY4MngLYKvzYN1ZV71x6aFk6kg4AhZqanL9zaY19qeVLhIYokaklc437j9dOw-waVchb-iZ8KsfSiW-n0gVHMcVxIxQi427oI3wiTpDzMosh7uLxPKG7YD7YFKs7vC0TjPK0pR7yDsvuppB2YN6IMyNLL3xrW6UedCl5bMZZsmDgzdFAJ12wdO4J2xKlJUa08tsqn4Et3NQlxip9iQbJA-VnPTSFwy8xY4CMugEKizFtU24rmD46iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برپایی ۲۰ مرکز خدمت‌رسانی همراه اول در مسیر بدرقه رهبر شهید انقلاب
🔹
همراه اول همزمان با آیین بدرقه رهبر شهید انقلاب، با ۲۰ مرکز سیار در مسیر مراسم، آماده ارائه خدمات ارتباطی و رفاهی به عزاداران است.
🔹
این مراکز با هدف تسهیل دسترسی شهروندان به خدمات ارتباطی، در نقاط مختلف مسیر مراسم شامل مسیرهای شمالی و جنوبی میدان آزادی، تقاطع آذربایجان، خیابان شادمان، خیابان خوش، میدان توحید، میدان انقلاب، چهارراه ولیعصر، خیابان حافظ، میدان فردوسی، پیچ شمیران و میدان امام حسین(ع) مستقر شده‌اند.
🔹
این ۲۰ مرکز با پشتیبانی ۱۰ مرکز دیگر، خدماتی نظیر اطلاع‌رسانی، مدیریت سیم‌کارت، راه‌اندازی سرویس‌ها، شارژ، پاسخگویی و رفع مشکلات ارتباطی مشترکان را ارائه می‌دهند.
http://mci.ir/-NJ1Z7C
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/666969" target="_blank">📅 15:50 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

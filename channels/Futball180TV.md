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
<img src="https://cdn5.telesco.pe/file/VgNbf-e1ZHXDCRREoYooY-RC33BOoPlCj2W1jKXwT58HOf_-KZQNoJYpHJ9IMm5zr2kIbNdWaxzh_icZ3oe3DSyZJQKuT1HYmRwWlJJUYZ03VAEyesLwB-P2ep3t-KRO3LuyYSBvwa-qXVQfzRycYn5tm1xEhuLgviO-JabNdBbNAudgvMBU6c8rzK6o0FtRPvd-v0zUziZT_YTINCDe1G1xyAEChC08UbQFaBZdaPv6PkGMfZdre3Hyx9csnyZmr9pdzXvf1GguUzfBVcmZc_oTG0Udc-Tjgs9mv2BUqX6EwG8vecQR5fY3W6MKK4K-hDClRrzedsv9n7mE67iCwQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 258K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 05:08:07</div>
<hr>

<div class="tg-post" id="msg-91466">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
🚨
شنیده شدن صدای انفجار از سه شهر تبریز، اصفهان و تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 917 · <a href="https://t.me/Futball180TV/91466" target="_blank">📅 05:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91464">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NhrvMTUA5uzatoYG0CxVFZKTpzJgk8v5MIPtpOzvtO3gkhWsucxHKa-ku_hp3vmk7NkHMKDWIa7PVdA4QiPIpRCKD-nR1JIRvzrzzGDNTg0Uxu9DidPMr1rPaskyxW4WpmHolXO_R5biepK8UX4azKf87tjzl17_CExAHB0c62pGhlG08m4rroAryHP_jfxQZRVKhF0Qlsi0jlBnCWbMYdUbqKEjrFQhTI6akDOyEPcHsgTKYmCQr8dCQaSU9MT6GZx1G0BzCOleqPZIi7yDvJ5YIp2WWZ2e32MObRNaKCDg7lc2aMeFNYKURwgAE32NlOzBFkBzDw6jLFnnYjCc4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y7xg-OWu6A1Kk655NbWEmOVWDtjUl01CEzNsIcJyeiYLtNopXTE2aDL5BJbZwns7XTRO_SkaYw339F58hTGImIHbDmG8u3_-fYT03QWExgFf3s5u1GYCcmddutloGbJMNf5u4prWAlifYrhbyCVjUjKqnbYnT_003EdsoGVyhAcawsEU7CDIx38mm-3h04UnmxQ3pyC_eswFVkTeGYvkINHbQdj6SN3wBjGIXFbuUxTlzN_y5_mzDKJzxYcDTLegt4RwnggE0jUXwqoBXNunxsVsIkWoe1-y474H7n43oFsX-HTTKxBn9YhOaQOoxyY09STNPObVmUZixvBtjW-TdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اولین‌تصاویر از انفجارهای شدید در اصفهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/Futball180TV/91464" target="_blank">📅 05:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91463">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
🚨
شنیده شدن صدای انفجار از سه شهر تبریز، اصفهان و تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/Futball180TV/91463" target="_blank">📅 05:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91462">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اخبار محلی از آغاز حملات نظامی سپاه پاسداران به مواضع اسرائیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/Futball180TV/91462" target="_blank">📅 05:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91461">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-8ddiNzkupU5tCTgLFpfb3xTOTnc-iVhdE_kJOy2etMa3VKd9lmtUM6qTWH9mZiRBgJfgN1C894lE_aIbz5dMA5ad0vCmixtVb-dtMgnN-bd6fkGFAwNiJx9ZJYEgVIhMO8U1evp9L70EcqxdDMWTf7bB_MTqk4uNSJc7AeXoUrH7rzAwYOLRENJSZnE5ReZn_fy4bwB-RU04TYTkjS1iPvsOIial-Zi0Off0BKtgOT91FiiLqxr4JCk7xRr9xy_XgYda934zD1ihVMZeQbqrV-P8c1HwIV_FN5kyHrr1eZ-4s2urtAW-Fe9594I8SUU3Mr7phjGTq_xkEGPrwxfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
⭕️
ارتش‌اسرائیل از انجام عملیات نظامی در خاک ایران خبر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/Futball180TV/91461" target="_blank">📅 05:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91459">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEXQSuHIzAJxmmFQQGGowkMnuevR3KGAhtHtn6AAvOVl_wvifO9Rm3zeKqE1xvN_D1PoacI5PfmNkLIe9tLN1MQz24dfzTC3x0tUmbeCU0wRJ254XASeM8dxx_dMNgbqJchaN5Bfak8ujONiPomRTsX3Knbu-LBe8vcAC0es1VNfAqwOqP8Hz_iN9_1Wmz0EL8Nu34PFKqWd-8iwXdEhLCUAJaX9QxDqE4u_N4jIf6V6KCe4vPAJ7QgBnHGGqlOgQzv_2OOKOJI-mJnEQyepupeinhfSIvb5WIwy0Adfowow3KvCbhhTVbS1-kHlwM8HjrtrEYJDSQj5x5W2P1FxbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
👍
🏆
علیرضا فغانی شریف در مراسم تصویر برداری رسمی از داوران جام‌جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/Futball180TV/91459" target="_blank">📅 04:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91456">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nJRGMXTYpG-xzY5vl-XfeY4JfHOcyn0_KsZUEoQ_eQMJmIc-f4AL9ve1F-InQ7cvaD74PrT_hxVI-W303KL0b8qKuFabzBWdxKxHKBXXMM2H9kXLqcLRaUsIuxz0DS-kTJZtt-1uVmfZ9MZGiJcFgMWeHvCg89wYrEggRCPTmDUKxpg-0PNkL6aG4bBgTx7Kt17VxcugCf4g5b6VcB_nkFxSykQ8T3VuYrWUM1N0FUhA0UiSg9C8eozR7qZVw1o59O8GZnemB75_GUxHZVN2wiTAzpG_3OXyJHM5izKPrjvMFUMLA9rUeJZUXdv7Nhxziak_gV-wPOOKiNflmz8Jfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cysSrVgr9p4837bmLs3Z-2yiap2PjRHyzkh-fQK_OBLU8NkwzVBW4z1LvnS3VGAKhCGDtKmZp-Ao_sOjhtvvvJ_tkVr4F1P5ukgshN5Wt0hwQq4XNUe4aRI6s_EJ4JeGBMtpO23PndRF_uJbXcYZ-KAX-Tgpsi_ZJ-HyQttP82C2XNnUu1BDKJI9APRA6OLo_7dkRDGHk8LgqxdoVpDpSjyxTpUTospZg1NASdsDUN90l_THBFnzLIgaqQy7pHZaW-qHSHCwc2vBuuMBcMs-3w8CEpUTpSOsRmoIccq-zl9IYNr38VSDl4EirYqR57YY2KA15T9bF2ZrMeStsPFgJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bhGfATt8kp5PYB5X-e_qDTbuV5ZKV50-iYHtVoldLedp_YV--jlaFXTvAR-AEBMKD3AaUob3vSBh2oTqTMv-MoDZj_ydE9dt3H_Ga01km1MuuidtUZG9f3iLkZqVy2-fZ0StTWJ8hTEspqsA64lsrlApWIxzrMmT-kTZ51ljDP_xVNwsQPBmui-eSb9OLwue7AmtCmPPL3cgCoEpo8UhWTdmHjdcSfjTe40Q7VbT63jfVCEDF11QmZydJEndiM-itTMKfUJK-kkdqtfneTypnY6h_VmB0tt8df4JbuYswGKNuJu2ydbLAKnuX05MW8Gk8n7rvmoDNfWOUPbBoOEQGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
تیتر رسمی دیلی میل در ارتباط با این فاجعه اخلاقی
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/Futball180TV/91456" target="_blank">📅 03:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91455">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4yfPykKNN9d35DUGBo_p52OCxQButIpumFEYuW_yvqEzLaJ6P22xUuphXrriulKsabFay0XlfqS5F3aKKrQhEM08Wc4rczuWUTDU8-E1Q8Tr67eohQmiMxWhcjHTRoZOvX4pqXmih1SZ1gf80RFFyzPu0f3lRSmXG1vUIksmB-ftioaP0adGopkO8OD6n7ccMI-oooHeNB2ml-PCSS3ZcJh6zxh0n6AQQg_XN__9D938bmch4eVrzTKjJ_H1lmSge77g8CepJKcB5Q7U22Ti2_MLi_fGY6BV4h20OUD5vKDtNW42Qj8Z3b-7SAkOmQNo8K3CQYPbD5f3MgccIt6Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙️
فلورنتینو پرز:
آیا ریکلمه رقیب خوبی بود؟ نمیدونم اون کیه
😅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/Futball180TV/91455" target="_blank">📅 03:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91454">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbDdv3w3oGIXvrk-SBZnva85RMEpK_HqFjIQenoZWadhNcum3Oq2Bae93iEciebwb3jKaxfx38dd8QRvA1A7qi5rgoxOJXXfU7yUe7aICrd4lVfmrWJKPGDFzbqa19PQsp8jZ8jV9TjY8Ze5QKJihy0ZOGJq2Dn43ifNiqKBKMOn1094wg29ALFLbwgpwXeNTQVOSj7yAGimV2maFRFQG7mmyuJKsHtNbvv-SjFKSqf_-uADQzczSRc8OVfXrteFpMz_iGFND3KsXJ0D0gSx6JH6rjpDzzwPYvXw35wVZYVwh-Gx7so_IEMGMaxYytEZ3DViBQqkzm3XLlOy6sSKXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
فاجعه اخلاقی و آبروریزی بازیکنان هول تیم قلعه‌نویی در ترکیه
‼️
‼️
‼️
گزارش رسانه دیلی‌میل از فاجعه اخلاقی تیم جمهوری اسلامی در ترکیه  فوتبالیست یکی از تیم‌های جام جهانی که در ترکیه اردو زده بود، می‌خواست دختر ۱۴ ساله بریتانیایی را در هتل، برای تعرض به پشت…</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/Futball180TV/91454" target="_blank">📅 03:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91453">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTN4p1Thq-qOt7LdbhBsTbyJ6pBsXZZq3M0lt4kFavLdxO-zMKvig9BZ2jZhKKkjQeKwlVKCW9uN8L200J72LLQTEfvLkUb_DR-3flVCy1dLbdifyl37jS7eBCuvJtNeslrIBGY_lPdTjUbKDFJksDCRQA5nOK9ebYIvXGIrCUphqALqnuKC_FT8fTHrI7gV3jX8ux9NjsmsBJnL-HKxEnHdRrgf-sB-hRiY2CbAMG31tdHEqbnnWIbkJwBf5sxSg1n0OyUS8qSJBfF91FxAfU10z_-ELjAx5VblMmPbXeOBW_bP42Ry4XXB_wOdbSx3tnR-z-YVto1hUuMy2SEhFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
فاجعه اخلاقی و آبروریزی بازیکنان هول تیم قلعه‌نویی در ترکیه
‼️
‼️
‼️
گزارش رسانه دیلی‌میل از فاجعه اخلاقی تیم جمهوری اسلامی در ترکیه
فوتبالیست یکی از تیم‌های جام جهانی که در ترکیه اردو زده بود، می‌خواست دختر ۱۴ ساله بریتانیایی را در هتل، برای تعرض به پشت پرچین بکشاند.
این خانواده وقتی متوجه شدند در هتلی اقامت دارند که یک تیم فوتبال عازم جام جهانی است، به نظرشان هیجان‌انگیز بود. کودک بریتانیایی، با فوتبالیست سلفی گرفت.
آن بازیکن، اینستاگرام دختر را گرفت و با وجود اطلاع از ۱۴ ساله بودنش، پیام‌هایی مثل «hot» فرستاد و خواست روی پایش بنشیند. پدر این نوجوان گفت دختر وحشتزده‌ام پس از حادثه، در حالی که با خواهر ۱۰ ساله‌اش کنار استخر بود، می‌گریست.
پدر خشمگین، فوراً به هتل اطلاع داد. از پذیرش با او تماس گرفتند تا با مربی و مسئولین تیم ملاقات کند. آنها عذرخواهی کرده و گفتند بازیکن از هتل اخراج خواهد شد. پدر گفت روز بعد متوجه شدم آن بازیکن نه تنها از هتل خارج نشده، بلکه هرگونه تخلفی را انکار می‌کند!
مادر دختر می‌گوید: دختر دیگری در همین هتل، توسط همان فوتبالیست آزار دیده.
خانوادهٔ اول، نتوانستند خانوادهٔ دوم را برای شکایت به پلیس قانع کنند. از طرفی، مسئولین هتل به خانواده بریتانیایی گفتند هیچ فیلم دوربین مداربسته‌ای وجود ندارد.
باتوجه به اینکه تنها یک روز از تعطیلاتشان باقی مانده بود، پدر تصمیم گرفت در بریتانیا موضوع را بطور گسترده‌تری مطرح کند. می‌گوید «نگران بودم به محض اینکه آنجا را ترک کنیم، آن بازیکن دوباره به استخر برگردد و همین کار را با کودکان دیگر انجام دهد.
پدر از آن زمان با مقامات ترکیه و نماینده مجلس محلی خود تماس گرفته. می‌گوید: «هتل، آنها را در اولویت قرار داد. با آنها رفتار متفاوتی می‌شد و می‌توانستند از هر کاری که می‌خواهند قسر در بروند.»
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/Futball180TV/91453" target="_blank">📅 03:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91452">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SK-5lXNx-ZP_jlKy6emeomwCiHNrKfhHE7N_9S8IzVevnlnPuHPHArO9Ag1qGtOWy2XLru7mXu8ZqnbmR1oQfBE5-7NqCm5nEIeSCvzBlOLesIdA5Iii1TldXlff4R76Z1E_O4YmmRHRLUgH5hvE0fc3AnbsK0YbeAq53H21jK4fKImUr_a1J_2IH0om4kOvy79Zdrau5Qao519kYLP4c0DaP_qDGAfo-uhSTyegeM7jIDNswBGeFGMKj-L5givGEjEuy_otk7UU-Nh7JBd4-8BpmhUT-qj6q4kgwDWDxu4BIP8mqWPQ0KMLHcIdjFJHnnLvK0PixM-19U7TMFXYEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
💣
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/Futball180TV/91452" target="_blank">📅 02:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91451">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🇪🇸
#رسمییییییی؛ با اعلام باشگاه رئال‌مادرید، ژوزه‌مورینیو با عقد قرارداد دو ساله با قابلیت تمدید برای سال سوم، سرمربی کهکشانی‌ها در فصل‌آینده شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/Futball180TV/91451" target="_blank">📅 02:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91450">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGF1O9fYJvmUivMnisTBCvCzVzjrE6hIe1GD1hf6bzv5IIpqM0qepo92Yznh_KVuhWfD7hT3PkWQuK8LxJgoqpIBhZiZyCekdTuldsluMk-sV37KwP_OyZYj0R0JnExaUKZC9GSAqnGm1Y0bxXMEEFmdCCZSYy5B3tQ8HI0zBW40TP-8yduSbQPXsnHeDLZSzAz5QSOUMoyQqyYfxsgaoaCERiMfXF1r4GafsfFYc9O_aAyyFVbQEnvwtMKCGzlYLl3SUXn8MrOug7Pp1rJUg68-dQrnP-GqrRp2tFGrY2bo2v2AK7OEetl0bBdNwPG-Xc4TDAnhYj3JErOyqjiC5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚪️
فوری و رسمی:  پرز برنده انتخابات شد و تا سال 2030 رئیس باشگاه رئال‌مادرید می‌مونه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/Futball180TV/91450" target="_blank">📅 02:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91449">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BP-bDSbrkD4IWj_5iw42Wfx04dwvBMCtpQFctJJLt3QSbHwv_aqwhGrr-GDe3H5zBYEZoyD9UYpgi6e277p1lfCA8K1Tcs00ScS4kmL8erEKkgbOdCPOWqmRWkkCPjyjlioQ5RH5UuucUgoi3HrQMWDi-FzxJxXHauyLpWrT3LqQMdHuUgLgraGjkH0hM2tsYZI5suARyem96r6-CL_4G1ine72JmOsMhdM0RQXeWuqltewBXe_Bioid_iEKfm_gx2S-MPQhE1Hhk6yltwEjiLhpoIaetvchaPWFE8UBRTpN_9c9MZGQgK_t4a5qKakc_BBxqHrUXT0nI6v6DPR8Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚪️
فوری و رسمی:
پرز برنده انتخابات شد و تا سال 2030 رئیس باشگاه رئال‌مادرید می‌مونه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/Futball180TV/91449" target="_blank">📅 02:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91448">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PfPzxGx7C8SD4-bvFK8ELLxmsgzkeeAcThMsSkkKHLecKrnZStZdDMaQlmg_WD1cnPP3KFiOsyTVyDMmsoT5eBOPzoDKruWIxqw889upyT1gZIUWfutnY_dg3U1jjOqD33Kg_ZtloVh3snmYZ-4hsKvrZ3udUyxb8KgwEczSG1_jQVCkF7tM11YYw80fd1G38SEvb81vZob_0tDH91D7sCAG2i8IdqupWtcZxQahXCPEbowztXcK-rCr_POh_nIltmrpc2IuP1WEKQsVomH6dp6FM0SJLzbxMMieOGGFX1vpYTLRggxrFjrwNWG5yu521qnw7ZINKJWCC8mOyD8SmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
خوزه فلیکس دیاز: پرز در تمام 60 میز انتخاباتی مقابل ریکلمه پیروز شد.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/Futball180TV/91448" target="_blank">📅 01:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91447">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
ترامپ: نتانیاهو چاره‌ای نخواهد داشت جز اینکه توافق با ایران را بپذیرد.
من همه فرمان‌ها را صادر می‌کنم. نتانیاهو فرمان‌ها را صادر نمی‌کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/91447" target="_blank">📅 01:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91446">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fG5dgRbpFoyUs57CdM7aDqsYhJlJLPQLOBHNaEKfuxZS_x0dQXXfYR-UP5lo_qMdFgYJo8lcB9wUV_xqAgPckpydVvw3vXn2qf9ch6aIr2DEGyPFHefEEncVJpa-aCjwbqBnyx9ovAaJvTZTqLSQyCnkLrsunRu4d7NlN1UYgmF2yjp2M5d0eR-XpBY-jtIt0YvPlVzhkeuuVGQ60SyE3jlidsafAgjMb1c6p4tek1OaRJtExu2HT7-s27kG2utMejEqzpGwyhRrx-87rR3ErhNVKtHWlsmCNm-a34vFInpqhew1J3gEtNbik6JfUntDqSij6jMc3An_PjDSM-mGZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
منابع مختلف اسپانیایی مدعی شدند که پرز یه گزینه جذاب دیگه بجای اولیسه تو آب‌نمک داره که ارزش ۱۵۰ میلیون یورویی تعیین کرده و بزودی اگه اولیسه رو جذب نکنه، سراغ این بازیکن میره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/91446" target="_blank">📅 01:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91445">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/46b3a86a4f.mp4?token=s6wPggOJc3qRHyZ7zoGaKksZZVVvEvttGcD4O0DJ_gDU2nlbznxoghT6irZby2B5mLIn4fWHB5AgKVHr1AZLRZeHsSYSJuKiY2uBj0MASAB6oT5Wx4mNoK0ie1e8oCTPXYa79rOpLbI2-mFe4r9Z7hLqj5OLyeg3lKvHmEXCYXfc69f0VSbzmATy-vdFefujlOwjfX95UNJt-jYRbwOO5oI27mW8Jbga60n7Z87jPZ-eXuwEBER54atxPDgfdGEKLTcYRYuXSgAvMZoKkjTyAZauYOKB-hCguGKthzuVjFbWNPTd8jAU-iqqwOqIfSxTKdYcVekVYEzUZux6zoks3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/46b3a86a4f.mp4?token=s6wPggOJc3qRHyZ7zoGaKksZZVVvEvttGcD4O0DJ_gDU2nlbznxoghT6irZby2B5mLIn4fWHB5AgKVHr1AZLRZeHsSYSJuKiY2uBj0MASAB6oT5Wx4mNoK0ie1e8oCTPXYa79rOpLbI2-mFe4r9Z7hLqj5OLyeg3lKvHmEXCYXfc69f0VSbzmATy-vdFefujlOwjfX95UNJt-jYRbwOO5oI27mW8Jbga60n7Z87jPZ-eXuwEBER54atxPDgfdGEKLTcYRYuXSgAvMZoKkjTyAZauYOKB-hCguGKthzuVjFbWNPTd8jAU-iqqwOqIfSxTKdYcVekVYEzUZux6zoks3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این لامصب توی چهار دوره جام جهانی و در طول ۲۰ سال، انگار اصلاً پیر نشده و چهره‌اش هیچ تغییری نکرده!
🙄
کدوم آهنگش؟
۲۰۰۶
👍🏻
۲۰۱۰
❤️
۲۰۱۴
👎🏻
۲۰۲۶
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/91445" target="_blank">📅 01:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91444">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a15a206df4.mp4?token=Jf8cwTIsCX9LHFYROyJ_7ZWDTYBPhLcFT6lBqGpOHnLVTxGAzigETAmYO05VSzHib2IqybMba4lOKhGCWV4lBucnFlk-bCdeJcRdc47JeiKA6xnbuXAd6CnWti5vfdNLFehVIT1KWuK14TKdTjQgzUa-51r8O5_s8xvd2oPMj-3HHKwknNvHO8lF0xVvElVV70r5gvCnS2U48_d8SGJ9pVSOdZY_qtrSkGcLyDDYQDEP8BeA8Wg6mXqKdRdCJgkraHKpf6ueAbId6MUOBZOtbaYyEgNJbEybI2jccAqcoATvrrh-H_Tzgws-C0Qj7CSWQE3ezTTrNbeEdn14uRZURQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a15a206df4.mp4?token=Jf8cwTIsCX9LHFYROyJ_7ZWDTYBPhLcFT6lBqGpOHnLVTxGAzigETAmYO05VSzHib2IqybMba4lOKhGCWV4lBucnFlk-bCdeJcRdc47JeiKA6xnbuXAd6CnWti5vfdNLFehVIT1KWuK14TKdTjQgzUa-51r8O5_s8xvd2oPMj-3HHKwknNvHO8lF0xVvElVV70r5gvCnS2U48_d8SGJ9pVSOdZY_qtrSkGcLyDDYQDEP8BeA8Wg6mXqKdRdCJgkraHKpf6ueAbId6MUOBZOtbaYyEgNJbEybI2jccAqcoATvrrh-H_Tzgws-C0Qj7CSWQE3ezTTrNbeEdn14uRZURQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
وضعیت صداوسیما امشب:
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/91444" target="_blank">📅 01:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91440">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sWtbUsOifn1otdJC8jG3kCJLD-NqaYz6xifXrEtDKNM64FHkSKp798cySq1r6h76o_u1PqdlXvwXAuYVVWlRAut1ob7MLuGJM1oZDFZ690Y_sYoEZpzKKMjSw5wT90tTc03vcavEzON4J1PGMRs3ZZeLIs4QE0oz7DVDIOC6zxCMyqzT9rXYmWKYXGA-I7Lxhc3wMIYcu6VLH0OYG67JvEYGZPPUTBbkMLXw-iyxrqBDyvvynHwckgAcx_tstd8WUEPYKGJf64rKjihh_paazNJ9T6WuK5ZpbubEI192ivx8H19aG8bzI80JqG1WXPSCbIYSyigGpAbiP9f-w_2UGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QcDobAnXgd-Bmrvuc0zsg6llj_v86OtOpXc8JTM-bW8-ABcRmuYMnAeoaFN_1a5W9tN4ryXhSsJkTYGSQuxoIuyN3MJdCG7xFZ1k9YLP-QgDQy_FtRfvUGEwqq7YS3CQFPU5xQ95-qxARB4Wluk7B6quf89dCF3AnPkc4nBsxkAkO8qI3JvHpJAEhXFTzh741xwccoYTsc9L6T5SgwC5PxEvhAMKf1tVrpiFKqaaqX69utJlFoeoM4GgSHd3MWybg_oOz0C1D4arXmq9bb1g8wp5XzfbRLQmvXaMjIJEuBg-5zQYF6QyD48dpm9jX1jMzLE64cf0mURHzarQO4BREA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qgogB9WDEYBgYYIysycHu8ezeb8V6LHbLzWmY0I4pS_ku-CSk_PxWadlD7pUtUTT57MZVWh1vVOMOYbuDyqtsSNRu15E5sb_TprUUo4xi0Ni7qO_YLq5DzEmc2AqUEA29c2b-QElYBD5Yp1CsF7lZfaGq85er9eeJpnhmlvkqGOtnaHu5Dk4D23Tk7mGn9SnUiYDhlQfBnLgAyEdHzeiY4TFqNx8b8oyzWCMevNNR1Zpwt9kdiWWZUjZN8XMc_oPMFpWlCBtx_O_SwVNFkIjMAVRXvD66Ja-CI8iWnpv8gaDWij8rg8GLPLZij3zYch67EvSJT_6cik0EjcNtDaMCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fGIzbZ4fkq27-ANBBqNlyA_Hg5f2BQDpXh9B6fGRD9oRyi5LhqnSM1MbvQF2-RDunKTbVz4zZmaOnlHjNIUEAbi9dHAPk0F2VJTnGkuLfDItrySijVn3iauCL8YzHWLdt_a454LUAzL0_8NvD2o_MHjrGCb0FTrhbOPL9vGFbPI4n5n12hIiBfhuBCIdRGgxLcCSie6GHj-jyrsBwuVQhDoL-Cnz-HKg5NamP3lA5kcr_niFXsdW_h3gJpzFGrIVDTUdN9jnu0RxWN2ITNyNiJyVf5Kj4X9OofrqRGBJI6BT2FvpkbmkSNMB1oj0n50GQUPKfvDKzLryXhcwRAwldg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
شروعش که اینجوری بوده خدا ادامشو بخیر کنه..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/91440" target="_blank">📅 01:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91439">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
یدیعوت آحارونوت: در گفتگویی که کمی پیش به پایان رسید، نتانیاهو به ترامپ اطلاع داد که قصد حمله‌ای قدرتمند به ایران را دارد. رئیس‌جمهور آمریکا اعلام کرد که اگر چنین حمله‌ای انجام شود، آمریکایی‌ها در آن شرکت نخواهند کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/91439" target="_blank">📅 01:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91438">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: اسرائیل و ایران هر دو ضربات خودشان را دریافت کرده‌اند و منطقه به درگیری یا حملات بیشتری نیاز ندارد
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/91438" target="_blank">📅 00:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91437">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
پروازهای فرودگاه امام از امشب تا اطلاع ثانوی متوقف شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/91437" target="_blank">📅 00:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91436">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/U2i67D4Z0c7d8LFmo8Uett_-_JBGTmMeGpnTTE4S_r6rVgJAal3QZdTQfPupO0JpoRhy-HrKaQDovbD-GHBpqk2LIcu20x3gT-ipAjOKbkMqSRWwV1xCu-GSP3cNrY_rSrKJK54ae0W0aw2HxDbAVLcs4CFRhqwV03wbp1HZzW63TPIub9_Ykt6T2Naxy6yRTr3c32bXC4HhRZntwsPM4w4RNsNT6mti48J7ZOPKO2C4ayDlaFhJUEqALKoLnN_P-wRrfOcELB53d439vXPctd4cvKmaspiVlxhGLcmMlWOKRRWeoj2R7NfvvY4V3IrU_c79MLGXLXF3uhAqgBgY8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوریییی :
🇪🇸
Miguel Blazquez :
خولیان آلوارز 100 درصد به بارسلونا خواهد اومد
‼️
وقتی باشگاه پیشنهاد 130 میلیون یورویی رو ارائه کنه، او بازیکن بارسا خواهد شد
باشگاه در حال کار روی مراسم معارفه با حضور تماشاگران در نیوکمپ است
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/91436" target="_blank">📅 00:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91435">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jowdc1Ae1mF4GdbzrnxSi4CxljujnZlKFDiHbTnxJVIsorXyXpCyqPRLFojPs6IaKaPT00BOd_DzA_1TnX3DA28uTIRk1ZLf-kac5NZpSQiRGBk8JIrdluGwfFLXtmsn9B59n-NMN-sjGIklJ-kvQCJIKRimhRYHAb50nwX4U0e4m1etyjjkLgY9ItaeGQ83yDONumHX5I28nepMqrB2ixb8wT14Uee9PcgQEPuM5Clkkd7bD5KoqODVfsNtxE4Il-QXXdzjEp0vbOakN-5UtiFAXx9gdf8lkxvBnVl8ix2h61KW033VhNdyYOyX2yV-Ka9SeyqKL4kO7vtVzug9VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حرفایی که ترامپ تو تماس تلفنی به نتانیاهو میزنه تا آرومش کنه و جلوی حمله رو بگیره :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/91435" target="_blank">📅 00:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91434">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFRdRL8kGJOiUXdB16IctrzzwJKLzM_1n-R6ELZRJbKoeCDGzrEtGlfI1464bEKExvwLlHb1CTIzIQVozFIxXld6ehi4OK-jfIdNGbe_PCoUAkfIqmqryZhF6H5WZUFDe8aSAYqAxqEwUt4Qh6waWkNaURSnfwMbBXBsl6q8vbI0PpfsK6eUgOka0g5JeqSR5_GEVibG0IympZ9FRoo7lnAd_twyiaVZm2dZ7YCJMjQjvwknBUrWpDKhzYURuwZdM_Wge95oKfb0MaDfaFxdQNfSZDnXabPosV8xSHNx3w6b-wUu_xZcUGXTVoC9hnH04s8U8uLJd6kZIgIRQ7tNHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه چیز به نفع کارلتو در جریان است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/91434" target="_blank">📅 00:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91433">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc3b1eadd2.mp4?token=cvZzForzokulMT35YgwTqNn1lxttu64nAM9gJAMtojihQ4Vsw-3IyAFkcGZlOBCuWByt4cj4hlGtwh_PCQzzLHqRt9SPbV9Eq2iDpHFXt9LPi8KRdGnRacRBA-rxCoBu3lDv6v2gjMLVgj-5KEwbP_lN2fuMNLjuoDCWP7bcTBb4WxFbRipCX2KKXu4qaMjzgJFTA3KWgnzszVAgvsoMT-b4WQszAyaSTBoB1TQEB9h0jbwFO5rTUicp8Sj619Z3fEAJXcmNZ3B7EBHiCEKKquI-y8ULVCVMsjolT9DvPg-OILBOy5Uti-Vt3Tj3NgoulLkYUSZ20mTNoAqFORycLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc3b1eadd2.mp4?token=cvZzForzokulMT35YgwTqNn1lxttu64nAM9gJAMtojihQ4Vsw-3IyAFkcGZlOBCuWByt4cj4hlGtwh_PCQzzLHqRt9SPbV9Eq2iDpHFXt9LPi8KRdGnRacRBA-rxCoBu3lDv6v2gjMLVgj-5KEwbP_lN2fuMNLjuoDCWP7bcTBb4WxFbRipCX2KKXu4qaMjzgJFTA3KWgnzszVAgvsoMT-b4WQszAyaSTBoB1TQEB9h0jbwFO5rTUicp8Sj619Z3fEAJXcmNZ3B7EBHiCEKKquI-y8ULVCVMsjolT9DvPg-OILBOy5Uti-Vt3Tj3NgoulLkYUSZ20mTNoAqFORycLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
#
فوری
؛ فاکس نیوز :
با اینکه ترامپ به اسرائیل گفته پاسخ نده اما اسرائیل همین الان جلسه اضطراری تشکیل داده تا تصمیم بگیره آیا به حملات اخیر پاسخ می‌ده یا نه؛ و اگه پاسخ بده، چطور این کار رو انجام خواهد داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/91433" target="_blank">📅 00:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91432">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/paHdePMaQlL1y_gVTPUN7JcroUWOYqLXzqPJA-PiR7xLwFM7dyj1QOvqXdqBbeD0HDCB39eDgOiuKCHAwazJKrm4MrazYKIMOjpfd30P_jPzo9vumj6j8HSDNoetXjLJcwxYhbv_DWqVZfux1KO7I8CrKqUyuC9vWdvFOHEpzXsHBA1MyvH-wUxsScrLIYtvDIgWIH7aEAARZ7JLuNlNbvU0KyLxTnGAGzcXMOfa3ET1X60Ci3dLqZ8KigNCrvwr4G5ViSHY8U2V-MZmVGFEMkPsL_X0O3o83Lq9kj2jSUDCcC14E5p5Ea31QUNPK_xSSg4nFkydfjfcSmSnvy3bXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
مراکش
🇲🇦
-
🇳🇴
نروژ
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
یکشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه ردبول آرنا
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
مراکش در
۱۰
دیدار اخیر خود،
هفت
برد و
سه
تساوی کسب کرده است.
✅
نروژ در
۱۰
دیدار اخیر خود،
هفت
برد و
دو
تساوی کسب کرده و در
یک
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر مراکش
۲.۵
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر نروژ
۳
.
۸
گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از
۱.۵
- ضریب:
۱.۲۷
🧠
وقتی از بازی لذت نمی‌برید، متوقف شوید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/91432" target="_blank">📅 00:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91431">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
بیانیه رسمی ارتش اسرائیل در واکنش به حملات موشکی سپاه پاسداران
‼️
‼️
رژیم تروریستی ایران در تلاش است معادله‌ای جدید ایجاد کرده و با انجام شلیک مستقیم به خاک ما، در واکنش به حملات ارتش اسرائیل به ضاحیه ، قواعد جدیدی را تحمیل کند - ما اجازه چنین کاری را نخواهیم داد!
‼️
‼️
ما در واکنش به شلیک‌های بی‌وقفه حزب‌الله به سوی شهرک‌ها و مناطق مسکونی شمال اسرائیل دست به حمله زدیم. اجازه نخواهیم داد حملات علیه شهروندان کشور اسرائیل ادامه پیدا کند.
‼️
‼️
ارتش اسرائیل در دفاع و هم در حمله قدرتمند عمل می‌کند. سامانه‌های پدافند هوایی در سراسر کشور مستقر می باشند.
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/91431" target="_blank">📅 00:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91429">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IFU-ZEbp9QGHW9VyMccPzAebjqiiB_TJkuLIFfV7XEiqMbiP5V-C9TZ15oiglwWEBdhMQ54UrQO5F_kzjMTbZHKbTrJHApdBqbZJI2TplJh6d3RnptKjSODVdCJougwI0zjO7XeFpdu-LNpaUTLsbl9yuhsF_5VQno1jRjV3B5VhQwW0BGGAlQZSTbC4jqmhf4bXq9QyYYW9T6BojRT69F4-sfI_h6Q15I1AgAhDNn_KcIRrkzyLo7j_K2DnSo46Y75GLWYB2YsHV4B1lDzX3CCQQ54X4S-VfY6hXHx23kJsIslrT8KcXdHRDMEfHjILp5-t5hm73SLDDXZGYQsInQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h1GM_liwJeFebROJkydajNs5SMP5j_MmXwwNHbqTmWnphvDLjF--LqAG9nxTcLXEC03_WSquJoDlqsVWNHZCdDz4obfPnkKSBFGKinecerhk1z_TCFxOVzc7Icj0eF5hdUBKTrFvIZbp686YEn2qPFJSvORr_kH959-eebbZVUDKHIp05SVOPG1mLnloHSHPwV5eW6LzDSn3MUX-4BgV3TVwNEfzJ09QvrN5c4wZZqELlTTeAur7Q9KrwJIiRj8Meyv6dtUXV3rAy0c-dl5pf_02LSAbWy5RZGKTHMTxDWriEzJ6wSB924qdlMGoO110amNgY5twlGYzOrIa7GuIrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇨🇭
فدراسیون فوتبال سوئیس از وجود مارهای سمی در کنار محل تمرین شکایت دارند.
‼️
اونا در ساعات گذشته به دنبال راه حلی در سریع‌ترین زمان ممکن هستن تا به محل دیگری منتقل شوند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/91429" target="_blank">📅 00:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91428">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
ترامپ : نتانیاهو جوابمو نمی ده اس ام اس دادم‌ نگران نباشید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/91428" target="_blank">📅 00:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91427">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
ترامپ : نتانیاهو جوابمو نمی ده اس ام اس دادم‌ نگران نباشید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/91427" target="_blank">📅 00:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91425">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
فووریی ترامپ:  اگه تا آخر هفته توافق شد میام تهران تاسوعا عاشورا غذا میدم تا ۱ ماه هم سیبیل و ریشامو نمیزنم!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/91425" target="_blank">📅 00:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91424">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDU0mJeU3LTzSFDF_vyEqa0rZqTeB2_u8XcJBb-lalfmfTIZR7aTYvChmexcDdscTx-0K3dbAnyasAYoxJLOCCJJd-w7mJVCWpPu-d9VDwm8FJErstmoFSQAVRiLPIZJLSH8mxw_sUx1GS42U9pDvxkngR2VzuiOKdRdWnQm9C0mEzJ8pWkczoxK1IQaw4pUQEgYAIogDCkNVer-IQwikDt2m6c0frl5J64UpTyBmxfOrA989jACYXhMf9e9J7H-6U_BP-gZ44n4LgWynMwvlzH-tR7EbhdvgVvtiZhOp522SnvyaaPxuUgeWkqWynwYh8WS0C6cIHH7fEUPRXDizQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عزیز ییلدریم به عنوان رئیس باشگاه فنرباغچه در انتخابات پیروز شد و هاکان صافی را شکست داد؛ وعده هایی که صافی در صورت پیروزی انتخابات داده بود:
❌
لوئیس سوارز
❌
میسون گرینوود
❌
هاکان چالهان‌اوغلو
❌
مریح دمیرال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/91424" target="_blank">📅 00:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91423">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
ارتش اسرائیل : ما به عملیات خود در سراسر لبنان در واکنش به حمله جمهوری اسلامی ادامه خواهیم داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/91423" target="_blank">📅 00:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91422">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9d9632a96.mp4?token=u9OMCIzslidBuKU5Phrgc5JqdHyxNLe_8lgyXkIe8QbtJurGQEpQ3-UywLOL6aaM_zYqa4MYLLQE5h__AQWFy0JxYpaGAwF8yrNkyhvKsCgHIDvrM-NYSsADjq6Ln3Xm9mvitxvP01dMo4mW2-N_kFVGgHodxoDGs0_ipXmlHykdIa6Iq3KskVG3-MwE_dZ9q9GX2bbRzi9IrOB5vM91qpbsCkf_ecSiG0yw5wcfdzmEHisE3ex5q4mws9CBgFaFkDcKihRETnxJOe5p4syfsrQxMS77NIcobfduMCJb8ai_zGgwFBmR-8kIMdqHJE-qEfqWE9DgZI6pRZq3Ju7pbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9d9632a96.mp4?token=u9OMCIzslidBuKU5Phrgc5JqdHyxNLe_8lgyXkIe8QbtJurGQEpQ3-UywLOL6aaM_zYqa4MYLLQE5h__AQWFy0JxYpaGAwF8yrNkyhvKsCgHIDvrM-NYSsADjq6Ln3Xm9mvitxvP01dMo4mW2-N_kFVGgHodxoDGs0_ipXmlHykdIa6Iq3KskVG3-MwE_dZ9q9GX2bbRzi9IrOB5vM91qpbsCkf_ecSiG0yw5wcfdzmEHisE3ex5q4mws9CBgFaFkDcKihRETnxJOe5p4syfsrQxMS77NIcobfduMCJb8ai_zGgwFBmR-8kIMdqHJE-qEfqWE9DgZI6pRZq3Ju7pbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
این بار ۴۶۲۰۴۷۲۱ ام بود باعث صلح شدم به خودم افتخار میکنم الحق که جایزه نوبل حق منه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/91422" target="_blank">📅 00:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91421">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">خوب برگردیم به فوتبال
مراکش تا دقیقه ۷۰ یک هیچ از  وایکینگ های کله کیری پیشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/91421" target="_blank">📅 00:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91420">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
فووریی ترامپ:
اگه تا آخر هفته توافق شد میام تهران تاسوعا عاشورا غذا میدم تا ۱ ماه هم سیبیل و ریشامو نمیزنم!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/91420" target="_blank">📅 00:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91419">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
ادعای سخنگوی ارتش اسرائیل:
هم اکنون رئیس ستاد ارتش در حال تصویب طرح‌هایی برای حمله به ایران است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/91419" target="_blank">📅 00:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91417">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
ترامپ : هر کدام از آنها خوش گذراندند، اسرائیل حمله خود را داشت و ایران هم حمله خود را، ما به حمله دیگری نیاز نداریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/91417" target="_blank">📅 23:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91416">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی قرارگاه خاتم بالاخره پیداش شد: اسرائیل باید حمله به لبنان رو متوقف کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/91416" target="_blank">📅 23:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91415">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🇺🇸
🎙
ترامپ: به توافق با ایران نزدیک شده‌ایم و نمی‌خواهم اکنون در مذاکرات اختلال ایجاد کنم.   @News_hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/91415" target="_blank">📅 23:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91414">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اینترنت به شدت اختلال داره!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/91414" target="_blank">📅 23:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91413">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
فوووورییی صداسیما:
خونه نتانیاهو رو پودر کردیم!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/91413" target="_blank">📅 23:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91412">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ: حملات اسرائیل به بیرون هماهنگ نشده بود؛ اصلا از این موضوع خوشحال نیستم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/91412" target="_blank">📅 23:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91411">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ: حملات اسرائیل به بیرون هماهنگ نشده بود؛ اصلا از این موضوع خوشحال نیستم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/91411" target="_blank">📅 23:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91410">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">خلاصه اینکه بالای ۱۵تاحواشی و خبر جام جهانی توی تایمره قراربود امشب پخش بشه ، ولی حیف
💔
کاش یه قانون توی دنیا بود که ۱۰روز قبل جام‌جهانی همه جنگ ها متوقف بشه تا بعد بازی فینال 🫩
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/91410" target="_blank">📅 23:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91409">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دوستان یچیزی
محض احتیاط دیلیت اکانت تلگرامتون رو بزارید روی دوسال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/91409" target="_blank">📅 23:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91408">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
ترامپ به فاکس نیوز:  پیشنهاد من به ایران این است: موشک‌هایتان را شلیک کرده‌اید، کافی است. به میز مذاکره بازگردید و معامله‌ای انجام دهید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/91408" target="_blank">📅 23:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91407">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
ترامپ به فاکس نیوز:  پیشنهاد من به ایران این است: موشک‌هایتان را شلیک کرده‌اید، کافی است. به میز مذاکره بازگردید و معامله‌ای انجام دهید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/91407" target="_blank">📅 23:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91406">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
ترامپ به فاکس نیوز:
پیشنهاد من به ایران این است: موشک‌هایتان را شلیک کرده‌اید، کافی است. به میز مذاکره بازگردید و معامله‌ای انجام دهید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/91406" target="_blank">📅 23:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91405">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
جبهه داخلی اسرائیل اعلام کرد که رویداد در شمال کشور به پایان رسیده است. می‌توانید از پناهگاه‌ها خارج شوید
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/91405" target="_blank">📅 23:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91404">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">عجب ملتی داریم
تو نیم ساعت از اخبار جام‌ جهانی رسیدیم به اخبار جنگ‌ جهانی
هعی خداااا بگم شکرت خندت نمیگیره واقعا؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/91404" target="_blank">📅 23:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91403">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
سپاه پاسداران رسما اعلام کرد: پایگاه هوایی رامات دیوید، هدف موشک‌های بالستیک قرار گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/91403" target="_blank">📅 23:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91402">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
فوووررری
هواپیماهای سوخت‌رسان آمریکا از پایگاه اسرائیل به پرواز در آمدند!!
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/91402" target="_blank">📅 23:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91401">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">الان کادر تیم ملی رو گروگان بگیرن چی؟
😂
😐
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/91401" target="_blank">📅 23:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91400">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
#فووریییی
؛ موج بعدی حمله از قم و کرج و کرمانشاه آغاز شد!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/91400" target="_blank">📅 23:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91399">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ifRmKINl9OFcb_xU0NfIbmBVGbhQA-ifZr0L4IsWLnAeC6fLmDcDjo0xbRWvepXjLggCQfal-VFclSstljjoMT8r5WnhpgutSYvbDUpJbV17VXYI0jbe4JeqU8sH3m3fOQwT044KxtU4nFUODsn9Otzgkrv9nxfam6rP_OvneddYuoKjERaPHD5_2AB7ZA_bWRYdBkxyjtmN9xmNPapaMoCS41MolM5wZZuDsN9IAy8WROkT6K8Art2wnZRU309UP-UsjEAKb-VrGnvXaNRfUBsCW2h-tekvus1KrfGBoOgbZ00kt-RoP2-tDwoxt5iXX-v2z2azVDgaReUWYQauKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعییی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/91399" target="_blank">📅 23:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91398">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سرعت اینترنت کاهش و دچار اختلال شد!!   @Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/91398" target="_blank">📅 23:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91397">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
🚨
موج جدید حملات موشکی سپاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/91397" target="_blank">📅 23:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91396">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
کانال ۱۲ اسرائیل:
امشب اسرائیل به ایران حمله خواهد کرد!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/91396" target="_blank">📅 23:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91395">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
ایران نزدیک ۴۰ موشک شلیک کرده است!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/91395" target="_blank">📅 23:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91394">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cb2bd2c8a.mp4?token=DZl5XCgDs80z2eZP2g6r-cDLRnIFEDA5JA4IoGW3hDTPAnXBaRgfMMFYl5H4cS87DbMtHm4b83zkBo0IFBsVgtfEHORbTL2VpW99T2ZjBXGcsBb_Owols-EdWf5jSxgTXJZI_87W7QX0ii0_AaLYZ5IFgAICBtY3B20W9Lw-QvKUyKJu6rSPgqkvHuvjgbiwxmzM14lPMGL_eFoM1S9EasV2NWO6A8MTCPBtyfKIZ08GyB-qyuU8GxisPVe0z0cm0wqJiUU6awloNglpmUmNqXAZ8sFnlkO_gpE3jHX-NdUlUdXP1Z4zNjGxLHCLgk4tqPB7MQi0bVcIOyScdeNDug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cb2bd2c8a.mp4?token=DZl5XCgDs80z2eZP2g6r-cDLRnIFEDA5JA4IoGW3hDTPAnXBaRgfMMFYl5H4cS87DbMtHm4b83zkBo0IFBsVgtfEHORbTL2VpW99T2ZjBXGcsBb_Owols-EdWf5jSxgTXJZI_87W7QX0ii0_AaLYZ5IFgAICBtY3B20W9Lw-QvKUyKJu6rSPgqkvHuvjgbiwxmzM14lPMGL_eFoM1S9EasV2NWO6A8MTCPBtyfKIZ08GyB-qyuU8GxisPVe0z0cm0wqJiUU6awloNglpmUmNqXAZ8sFnlkO_gpE3jHX-NdUlUdXP1Z4zNjGxLHCLgk4tqPB7MQi0bVcIOyScdeNDug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
وضعیت کانفیگ فروشا، دانش آموزا و دانشجوها:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/91394" target="_blank">📅 23:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91393">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
والا نیوز: اسرائیل در حال درخواست چراغ سبز از آمریکا برای هدف قرار دادن تأسیسات انرژی ایران است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/91393" target="_blank">📅 23:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91392">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHCVSBXz1QHMHqCcxByFcz_EgU39WphQIFvEoln-VKcBE7VbJmmyRRc90finIAW2Fd8wwuImDB81LXX8alvuppQrzmE5IKkoLUkH9vXx4w5S_U82547P9IqWEzgkQ-p4o-sMU9sRrkVuuavNiyVAREFqEfxjfOqv-sfM5DI2I7glxE9sEzCEnIZLlaStGMJHDVJfoRYmtGrcLOnVmM31QIv31buh2bv0p4K_Ioxlr13lHCegUy0FDkxNO4HVuhydFd94dWyBBvAks4uSdEnZukdq7bFQEeb-uVarp5CmtD14zfwmmVIyoLfyFKmwj-q4Wd5GHuwY3dKbmCa0ugJUHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
آسمان ایران کلیر شد!!!
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/91392" target="_blank">📅 23:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91391">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-poll">
<h4>📊 وضعیت اینترنت شما چطوره؟</h4>
<ul>
<li>✓ مثل چند روز گذشته و تغییری نکرده</li>
<li>✓ الان داره ضعیف تر می‌شه</li>
</ul>
</div>
<div class="tg-text">سرعت اینترنت کاهش و دچار اختلال شد!!   @Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/91391" target="_blank">📅 23:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91390">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سرعت اینترنت کاهش و دچار اختلال شد!!
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/91390" target="_blank">📅 23:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91388">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a284a8676.mp4?token=Mj_La-QoaZ8qnU860KjQnfOS3kRL8eTNjDsQTFRwHUdAqHJnHfVXpyVMjGytXocZ9G-hMk6cAmbp3iTCrgb5q_lmHcdco9YuuC6Bp9jsCmDv2HDiXI_VWMNNnSYPTXhkLFK-LVkFeWU8tu1M1-SSB8k6K6DG1KSXC24LNUcmMVHOe3OX9v6XXLJZPQ_WK6F95d1wrDXJCT-klXgha5NnCEbEb0YZVsUERo5dQrACfSR4qcXC90n_bEC3VE0PVUqy8nI0KbG-cfixUgrnfWFN_GCzQx5xSYemkUUaVCiutpBu2kpl9_neNy_Fp0YCqM5N9_Cxyr4yfBgQXGYt6A0S1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a284a8676.mp4?token=Mj_La-QoaZ8qnU860KjQnfOS3kRL8eTNjDsQTFRwHUdAqHJnHfVXpyVMjGytXocZ9G-hMk6cAmbp3iTCrgb5q_lmHcdco9YuuC6Bp9jsCmDv2HDiXI_VWMNNnSYPTXhkLFK-LVkFeWU8tu1M1-SSB8k6K6DG1KSXC24LNUcmMVHOe3OX9v6XXLJZPQ_WK6F95d1wrDXJCT-klXgha5NnCEbEb0YZVsUERo5dQrACfSR4qcXC90n_bEC3VE0PVUqy8nI0KbG-cfixUgrnfWFN_GCzQx5xSYemkUUaVCiutpBu2kpl9_neNy_Fp0YCqM5N9_Cxyr4yfBgQXGYt6A0S1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
رهگیری موشک های سپاه در آسمان اسرائیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/91388" target="_blank">📅 23:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91387">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">خیلی دردناکه که تو گروه ها و کانال های ایرانی هیچکس از احتمال حمله متقابل اسرائیل نگران نیست، اون چیزی که همه رو میترسونه قطع کردن دوباره اینترنت توسط حکومت است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/91387" target="_blank">📅 22:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91386">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
فووورییی بیانه فرماندهی قرارگاه مرکزی خاتم‌الانبیا:
اسرائیل با ادامه حملات به جنوب لبنان و ضاحیه بیروت، از خطوط قرمز ایران عبور کرده است. در این بیانیه، آمریکا به حمایت از اسرائیل متهم شده و ادعا شده که از سلاح‌های ممنوعه نیز استفاده می‌شود. همچنین تأکید شده که ایران پیش‌تر هشدار داده بود در صورت گسترش حملات به ضاحیه بیروت، اهدافی در اسرائیل را هدف قرار خواهد داد. در پایان هشدار داده شده که اگر اسرائیل به حملات خود ادامه دهد یا به اقدام ایران پاسخ دهد، با حملات شدیدتر و گسترده‌تری مواجه خواهد شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/91386" target="_blank">📅 22:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91385">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fubCz7TpCliAQSjE8pQIY0BZOQAWR40SkiVUXSkHe3n1bYCfM1k-1ePDozR3Gn-zabnVVxiByHHkmOIxPpRKR0MCCizV6dGcaAXQA8U7rhcvzQGRs3VaVlGKKOtooaJm6o9XwH8vi7Mw3XRRxive10EifcU7hKdtPsgDCLLt1zUzkvUtVBXHBPovNsBsPvhT8pbYjZ6UZPDKZJEzTEWOe8O-aMY1I5AT7aq1d8uH1Da1anrLTcqpZmZDYABopMckoNBFTaK6fUqJEsjTC56mhCRvdFCzn5WyPxtw1mZ_vAZXxnmZQVkXDU8suAG5JUu2J5Z6W0r07rthry3o4DHaMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
بن گویر وزیر امنیت ملی اسرائیل: امشب تهران باید بسوزد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/91385" target="_blank">📅 22:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91384">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d76423eea.mp4?token=FG6eUMOOFg-3_N2EQ8Tv2Y6ZgmY1bXzGuiR3nC8l291dvnixxCwvsq1Geh4WO-iCVrYHTmGPCXNrfUaDX9aPF7vIAaEANOGpVuiTOLVcHsOoXWQSUTsdHHmUikqnUAInfbVJAbFGRvEe8W254_TBN_hfq3jv28pc2g058GoJGRv0rwDRWbZGJvwQTtAskbt0jP5bdrsOCc65MC_WqkbRU772ThEoKs_fNRArQAFQJFY9D3blaDTOVzlvtbo9CLNEaXIumqrMnfo1aXFN4iKarDobN0gS7t9KOKCwiOs59bPEICVehktDSD1ApiyO6WiGjLTq8Ju2E41sR7U6YUIZUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d76423eea.mp4?token=FG6eUMOOFg-3_N2EQ8Tv2Y6ZgmY1bXzGuiR3nC8l291dvnixxCwvsq1Geh4WO-iCVrYHTmGPCXNrfUaDX9aPF7vIAaEANOGpVuiTOLVcHsOoXWQSUTsdHHmUikqnUAInfbVJAbFGRvEe8W254_TBN_hfq3jv28pc2g058GoJGRv0rwDRWbZGJvwQTtAskbt0jP5bdrsOCc65MC_WqkbRU772ThEoKs_fNRArQAFQJFY9D3blaDTOVzlvtbo9CLNEaXIumqrMnfo1aXFN4iKarDobN0gS7t9KOKCwiOs59bPEICVehktDSD1ApiyO6WiGjLTq8Ju2E41sR7U6YUIZUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات جدید از اصفهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/91384" target="_blank">📅 22:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91383">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
حمله همزمان از اصفهان و تبریز!!
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/91383" target="_blank">📅 22:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91382">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
فووورریییی
موج سوم حمله از تبریزززز
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/91382" target="_blank">📅 22:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91381">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqpyO-wS-6fdwMDT-keFSKpNsA-pDkTQt9bRm-IBiHxPRUSiyNf38k4x60iExE3ZFaWXl0e8tdOE5mQse5_FsHOuRg2UHMmG0NxJ9g3LmQev_iBaNspiHlzURthbT2m44eFzijt7w_KeOXqpm97YXmcXUIFCm5yn4WDFo7ETe3r6l7C-YMXgvSzW_poH9YlSBO85hgNudj3q4H86tyvBVDxYBSmKIsIoo5IxcDnmWbRo1sdE2dwKggOWCbRPp4HsbxsuqP6g4lk58TpVjo166zurT0eorpPrcLyRf7pmqvdqbFGSQMtMDZb6610eVWs6XrPxu9yBVH_h2xmXeYe9KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
فیلتر شکن تانل شده با قیمتی
عالی
⭐
- 5 گیگ
75
60 هزار تومان
⭐
- 10 گیگ
130
104 هزار تومان
⭐
- 20 گیگ
240
192 هزار تومان
⭐
- 30 گیگ
340
272 هزار تومان
⭐
- 50 گیگ
540
432 هزار تومان
⭐
- 100 گیگ
990
792 هزار تومان
🔥
20 درصد تخفیف ویژه جام جهانی
JamJahani
👥
بدون محدودیت کاربر (999 نفر)
🔥
با خرید یک سرویس 5 کانفیگ پر سرعت
مولتی لوکیشن
دریافت کنید
🪐
|  تنها راه خرید مراجعه به ربات
🤖
| ربات :
@ActiveNet_Robot
✅
| پشتیبانی فعال تا اخرین کیلوبایت
🛍
| بهترین سرعت و کیفیت در ایران</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/91381" target="_blank">📅 22:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91378">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgBeb7kQeym6Ew7Jt60DKAq4bza6MT-Y7WWmHRxmONIeDewRHRQj6SJrn9HRf-pNOr19s84vVFzncrLrLyPC_j3bMxDiLGGt1HA15T7JsPqVACjlpLZiEQk_KzerP-fM780SgZejyfI8hlZ5-lvSGkMW5w6gIwWQjYFngtgD1Jxfaft8tG75MKAEKqEG7mFk5zYVOo1CmHy__efTrmd1N3sMDJcytyzbYHiWguPj9eeog990Uwc1P7BZuZxf44-T0fRAZh_za2WbZv199RtPxrd1GQjk7Zn2k68eKQsC9LqyrSxMrUKKy1P2cbsUpyWqoCv_U7jo7dupnUWcpLgpXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/91378" target="_blank">📅 22:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91377">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بیایین باهم یه خواهش از پرزیدنت پزشکیان بکنیم نت مارو قطع نکنه
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/91377" target="_blank">📅 22:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91376">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
مقامات ارتش اسرائیل به رادیو ارتش و کانال 14:
چیزی به نام پاسخ محدود به ایران نداریم و حمله میکنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/91376" target="_blank">📅 22:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91375">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
❌
جمهوری اسلامی لحظاتی پیش 4 موشک از کرمانشاه به سمت اسرائیل پرتاب کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/91375" target="_blank">📅 22:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91374">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
❌
جمهوری اسلامی لحظاتی پیش 4 موشک از کرمانشاه به سمت اسرائیل پرتاب کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/91374" target="_blank">📅 22:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91373">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/664dea4d38.mp4?token=j8_YvJ3yhRdp6J3ZJSJV4XrfmqBhdO4uVD0pd29yD_K9i8Fwo3MizoR3Gfj7iCQHnhR4db9S67x-pZDC7_5gxHFAPoI8psHwpjchG5GHXCGuKjf3BCz0dJOBKEbM5zupvqN2B5V9qxtPDjvB1Hcyg9F8QsvLR1PamtNna3NWFOwXyYPDuKyp6r9Om4ajhnAawTcsCvXWpvaA52SH-ps614N6g-8WBeApa3ExP296952KBvJx_it6NRDJDrdt1nR2glCYtqRATu2UR-FyzsCMebnaW2fgAhitHfmB46gaXW74QD5oNZ1cGfzWvAWxGsJld5cU0ZFg2JPYPA4nUFRdWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/664dea4d38.mp4?token=j8_YvJ3yhRdp6J3ZJSJV4XrfmqBhdO4uVD0pd29yD_K9i8Fwo3MizoR3Gfj7iCQHnhR4db9S67x-pZDC7_5gxHFAPoI8psHwpjchG5GHXCGuKjf3BCz0dJOBKEbM5zupvqN2B5V9qxtPDjvB1Hcyg9F8QsvLR1PamtNna3NWFOwXyYPDuKyp6r9Om4ajhnAawTcsCvXWpvaA52SH-ps614N6g-8WBeApa3ExP296952KBvJx_it6NRDJDrdt1nR2glCYtqRATu2UR-FyzsCMebnaW2fgAhitHfmB46gaXW74QD5oNZ1cGfzWvAWxGsJld5cU0ZFg2JPYPA4nUFRdWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت پیوی کانفینگ فروشا بعد از اولین موشک:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/91373" target="_blank">📅 22:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91372">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">بابا من تازه ۴۰۰ ۵۰۰ تومن برای نت و کانفیگ هزینه کردم
😐
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/91372" target="_blank">📅 22:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91371">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مدارس و دانشگاه ها و مراکز دولتی برای ۳ روز تعطیل شدن!
احتمال حمله اسرائیل؟🫪🫪
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/91371" target="_blank">📅 22:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91370">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">چرب کنید حداقل ۲۰۰ تومن قراره بره رو قیمت هر گیگ کانفیگ</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/91370" target="_blank">📅 22:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91369">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UITmPPJ5WdfxpPUaseqhTEysIJIlbPazDSnXGuQFVK_9Hvw8NuX5XbiH--o2-XockIsR05qFpDFr9fOVQS_MwSEii7UQ3bC_O-ycgPYhwOpX3rH2R__1kpZCgvFTDQm1Tm1zltwAF_tVqZxTFXCxURWe9h4NrjB6S-XUyVYj6oRf0aJt5kMXqZiyMc4i7kIq2Htiam5njxNLmYI7DMJwWUkc1NLdwb0xbaLaLVDM_bWaYwlYzm4j4EvyngH1_nlhr1V5a9V6JrTT20IPlZPVKPGbM9UQzs9OhQ6oh9_97WA5R5DTLQYTmd2Xls-521wPHHnSeGmbPHa3qPdMTmHaMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فووورییییی</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/91369" target="_blank">📅 22:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91368">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
فووورییییی</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/91368" target="_blank">📅 22:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91367">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15acd81b3d.mp4?token=NP-9JG7cO7148z3fHwVLFiUML1Rq0rnx5ApYMyJP2sHMAhNa3OIZSCFqCk5EXAxOLxguF8URvvrk3OJ0E6_bbbC0OS4yh8uUkYH8cZmjlAHWTJB3SJ2aHeEZStunEh4dQmwemPAIoHTgIPxMa6YS5PBNZJUc2B3jEnrsrE656KbyTF2ACuKbn-I2YCRHMjNpvmzPHUhc7LAa7-2nGqYEkuQJMA_bcvB6K4DP84tbWAdkAdiXJ9dXBkWK4UZUnO8GpCsnbNC2IJFND1S2FDR241eqHVvgiKJMk7X079eYZPx_BpjnYzdK4yam9bGjX-qqhRUUc5DpqUjcmSRCJDfNNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15acd81b3d.mp4?token=NP-9JG7cO7148z3fHwVLFiUML1Rq0rnx5ApYMyJP2sHMAhNa3OIZSCFqCk5EXAxOLxguF8URvvrk3OJ0E6_bbbC0OS4yh8uUkYH8cZmjlAHWTJB3SJ2aHeEZStunEh4dQmwemPAIoHTgIPxMa6YS5PBNZJUc2B3jEnrsrE656KbyTF2ACuKbn-I2YCRHMjNpvmzPHUhc7LAa7-2nGqYEkuQJMA_bcvB6K4DP84tbWAdkAdiXJ9dXBkWK4UZUnO8GpCsnbNC2IJFND1S2FDR241eqHVvgiKJMk7X079eYZPx_BpjnYzdK4yam9bGjX-qqhRUUc5DpqUjcmSRCJDfNNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به نظرتون کدام تیم قهرمان جام جهانی میشه
☺️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/91367" target="_blank">📅 22:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91365">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SB4YW-17dXFX-vxl6BYO1X-E-VxOzC-toiuJwgrzerGQjIZcbKpvULvtFtTJvCL1qa0m4mh18oWaxbVr7X24skA7Aox_sVf6ICATOUu-fSwHjkMZ7u14WBLfW6_gcf4Vshh3GS5bTPK4p9y0z_iablsl44qHQntdB3FBnsJLtWr6HOpQBIqDJrWXNlvM4UimMoLL4tlHpxok3pgLJ1q-aGUnBHFTumkWSjxxDflaDYPiEIMEkLEP08Ci9ICWZDYR0BCOvmE6QBbjXTp0oiU_UZzs2_ah_pIhz0gXi3Ewpxy3tr8m6UzMGVoYL7SJxYp7JzHYBMBySOrxC3YaDpfVPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/475c525760.mp4?token=KOOA3A1eKJLXT2eO1P7nlK-8HGC1OLB8CDVleQ5vXxjqWauB6zVaamMe2Bc27mBCzzK46KGitJYIJliWtrH2p91u1Wx5OLg2zIS1A-q_QZCyhWpTur1weefXrRIvxFbjO8bPE9TDSTu3-AI7gIr28l_r0XDET-AMJcFO6YoSZk2jvGOantO_onGuAIbFyFDTccSAcn0q1LbyTVaeqzMdKD7Ip51BxoHxlKaPQDtpMISy2jCjl6nGJo4VPwEQNlBZjW5VBBUuKouollBCxhXRl_vTlXqHy1JP0FadjI8myaWx-zCZV9yY4fTkaBXZ_HfI9H3nwFK7QHuO6h2eQDxa8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/475c525760.mp4?token=KOOA3A1eKJLXT2eO1P7nlK-8HGC1OLB8CDVleQ5vXxjqWauB6zVaamMe2Bc27mBCzzK46KGitJYIJliWtrH2p91u1Wx5OLg2zIS1A-q_QZCyhWpTur1weefXrRIvxFbjO8bPE9TDSTu3-AI7gIr28l_r0XDET-AMJcFO6YoSZk2jvGOantO_onGuAIbFyFDTccSAcn0q1LbyTVaeqzMdKD7Ip51BxoHxlKaPQDtpMISy2jCjl6nGJo4VPwEQNlBZjW5VBBUuKouollBCxhXRl_vTlXqHy1JP0FadjI8myaWx-zCZV9yY4fTkaBXZ_HfI9H3nwFK7QHuO6h2eQDxa8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اثر هنری خوشگل و ناز آدولف کروس تو جام جهانی مقابل سوئد
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/91365" target="_blank">📅 22:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91364">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7uy2q4g8TQ81AU7zuScR0IFXjjgLd4N-sOsBiu6u4oiWm9Q0Paw4QMt_uTdztfF42m5M-RvYYZBSHYCzItc9cZQx7s5n9kL772ebcyTrVaG7faa5va6P3n9w_CBFB6jYaG6B2FjsDynAyFL11v35VCbehVs8OIqCB94ExugWjr-jx9_t0Zee6i0HPKAuIVj3BdgrKs7vLdjohJXY7xc7ULQDFlOruqD2uurYfUKre7k93HZHx1pR5pggRWtrjAAMSgavDksVJ3q4RGScxHZT45-mD6wpyzAej6er7QCrC32OZsoBk06j3dXnKcS5pY4cTfq-zqHSZt7P-QI81Cpdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
10 شگفتی بزرگ جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/91364" target="_blank">📅 22:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91363">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GlNB1Y3qE9XNYKDLknyGP6jRvh0NvV3es-R94KL_054wUVPJGXmZfggrv_KcOyJEjXtnli0kOosimAWgF6MOgKvGQrdbsZVFB-qv-gLXfC5aSzvecozAIYWsDmNYIA1jFUIgUFQHHCrpRlG-Z-FPIcopMLRM0H1Yry_ALtLWUQ4CmKJkPdG0q04q10eENWPxzRwU9LlPCjGQIHOa4G0G72pup8dEHUoHYOSIBnH9IzQx0XvhhYqENWD8hGz0Jz74LsGzheto1BPU7Qd2wVVhFN4biv8jQtrKsbobBc4vErrGZ01FKz-pRXO3QOBX-54HfPZc-q8QjkAyMshYVNgywA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰۰۶: حذف شده توسط آلمان
❌
۲۰۱۰: حذف شده توسط آلمان
❌
۲۰۱۴: حذف شده توسط آلمان
❌
۲۰۱۸: حذف شده توسط فرانسه
❌
۲۰۲۲: قهرمان
✅
۲۰۲۶ ؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/91363" target="_blank">📅 22:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91362">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
#فووووووری؛ فدراسیون دانمارک اعلام کرد که خطر از سر اریکسن رفع شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/91362" target="_blank">📅 21:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91360">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
🚨
پشمامممممم؛ اریکسن وسط بازی دانمارک دوباره قلبش گرفت و سکته کرده
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/Futball180TV/91360" target="_blank">📅 21:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91359">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAKqJ30L-h6-hlHNeFbYs4AYuaLjJLibqKoDag9jM2B0FsKV_9zEmfv2y2N26AD12ekpS1JXU4TS9hV0CX6KstT216erYJkBQ-2W06yXEn5yyBbKYkKnPJtGp6ttUXyCxW8aDS5HA6w8x66fzRwEcQgKcV5Uz54JBjyqFluCRxkO4SVmNsspQR-hadJvtraSdOW8HBmARi8iGdmkZtUZ5B0BASExHGgZRfphxS5H7y28FvdzZTgms8iL0_rz4327D5kKwp7LQ6gwLAJXfW_AUu04ko0UiG1OfLB2vxaTsQmu9NWlepD5TJX6OBLE0WQ-T6eKH0IaDMnTcvggBXTOSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برند کیت تیم های حاضر تو جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/Futball180TV/91359" target="_blank">📅 21:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91358">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
🚨
د اتلتیک: نزدیک محل اقامت تیم انگلیس درگیری مسلحانه ای رخ داده و 9 نفر زخمی شدن!  @News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/91358" target="_blank">📅 21:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91357">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thad4hD9GNXUu8J-wJwUmMJBOdFVVc8Bm_SZ7sWY3Pxb4MlNWMPLOOR6uVvBKO0WsZP7NLblhurbkm0UFw5BnLdInjEZfVmqod-GfdEfzDIWLzbf6pw0-bRuW3E0owO8P2fK1q5OwzGuP-nPrEDrrPeoo2ophIWd3yEUOFbz3xCv9bHE7bWGRYpmn-ShQVjY5SsxbmFN_jYknW2gCUgLlS2uepkl3CA7DPvrZXtqc0_wiu4Z-uEN67EgQ4pxbI9CUWCVMQKbD_oYuQl4BvEjlaQ4kIlU52k9R1aVpm7POjQWIqt9oQqG4RbUJm-Wwcwgklvi7eA3tTtHw43zY2cs3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
‼️
داور بازی رو تموم کرد و اریکسن به بیمارستان منتقل شد!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/Futball180TV/91357" target="_blank">📅 21:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91356">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5QnCN_p1ATv3lTOAhwYh5NiV8F33l-O24dBIy0aUGxF05ANxcuWZLe-MmY3B-B6jK4ITlBNZgd2e1-8J_zUMUmdeGlFbed3oyqKri8AOg_LSJK5obJ3bfLYkRp-2oMoVUvjfrJW_HML-kigh9Ja-CWLRXWNg4hTPVtrRBLOj_Nvrs9uMzPfL6NsCNMwxldCg4aY48XbXeJVAJu3yWtxVsXuf-cxsJD5lWPLa8D1OqUdOZ1sXE1_YHzFro_qVij7XmVDUIub7Abx5njCSzJa0V4DkzTzZKPN90B3Zp3ig9zdBk50C-M31oWoW0rZQdKU-SR5KBC6PgcjIylvt_PiZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
پشمامممممم؛ اریکسن وسط بازی دانمارک دوباره قلبش گرفت و سکته کرده
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/Futball180TV/91356" target="_blank">📅 21:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91355">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf69fb6576.mp4?token=Kx2W3Ti57-zxzxnEV77GHKanBpZDg0wjNdBtdmLrYXmeW0EYDed0gjvcJtuqAeWzzDDs8JQJXXuHMOgLdiv72BZZehk3RVcMx16q5ohrdjg4vAjDaEOKteZHNzWbn-KKobhl1FG8xuTKa-0H1OpVh5Lfum1LZ3Dt4w_-B8gqoemFkDvsh4xzM1_KTyYDGk4xYCgEEuhPuV8Ej-lPb7kKVvuWHB5OSF5tqIndCja5HTT398b_73vs_LAy1WSmvPd86v_wVj-3yMHLeTu4hl91gGi3wozlxoy9zI6RkeR49lLxzhRp35SUx3yAWtP2pD91XSaXtRHCRBBWVZoEeJcj5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf69fb6576.mp4?token=Kx2W3Ti57-zxzxnEV77GHKanBpZDg0wjNdBtdmLrYXmeW0EYDed0gjvcJtuqAeWzzDDs8JQJXXuHMOgLdiv72BZZehk3RVcMx16q5ohrdjg4vAjDaEOKteZHNzWbn-KKobhl1FG8xuTKa-0H1OpVh5Lfum1LZ3Dt4w_-B8gqoemFkDvsh4xzM1_KTyYDGk4xYCgEEuhPuV8Ej-lPb7kKVvuWHB5OSF5tqIndCja5HTT398b_73vs_LAy1WSmvPd86v_wVj-3yMHLeTu4hl91gGi3wozlxoy9zI6RkeR49lLxzhRp35SUx3yAWtP2pD91XSaXtRHCRBBWVZoEeJcj5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
پشمامممممم؛ اریکسن وسط بازی دانمارک دوباره قلبش گرفت و سکته کرده
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/Futball180TV/91355" target="_blank">📅 21:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91354">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhi6mkVbX6GaF_lxALRkEqrD7ZNyFm_PLck57Tz6C29b_d2di3s6iOOROfa3LmMSEPw1m124ByrbNrqed6UpthkCP8axMC1LufxK9Yps0mNm9wrb3W-2QpaAaG1gnjM8MTzu83ZwYksRtTw1xjY2Qoh7X43g6nlJi0ztipbAJlxHdmdFfIIpC-p7dSxa2egyyo65Ahe_s6nhK96gyQRTApq-a6bt1DSl3-yt7IQ7ZhsUyJUhCXZgbewXtEQkp8qTzWlSDWa9uQo94mHABbV7rX51wccEenvakKrKcbtihqok2OkRUuajXBT26iMn9MrCjQANDoCXZcv7HF4iUEl1dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فلورنتینو پرز برای نقل‌وانتقالات تابستانی رئال رقم ۳۰۰ میلیون یورو بودجه تعیین کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/Futball180TV/91354" target="_blank">📅 21:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91353">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k81ubeZ-MqDOBf0kpW6UqjpK3mVGqmebMCog1CPdm1ty2ZriAOHYXNFhVNZ4rfC5dpNwe-zE7n65_UAaQTUcUlgcqgMBzaX6XbvFwIfmPU8Q6cSNKWx6DDEWtmr0uOTaRdulZtxlWo8LEzm2sUYWf-stoTHz2rfDFrtYqE0wrpB7uKK4KemmhrPNhh6in3SChhkAbNlwzUXXBDBYklLSD7CSTWxVVz329BRgEe57WFu-kHNwPR9czL7d-DiJ_PApXP9__qjtFTXHWJeFwTqdqibmPTeRQcIXHUl_DkdGot8loA1M_Jrp67FqzoUdeUu31iaBMtEpcvDNEgf22ID1RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسکتبال هم جذابیت خودشو داره
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/Futball180TV/91353" target="_blank">📅 21:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91352">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e07c2b244.mp4?token=b5kGyo3mMXPNtbJIFJvrMZWf3WqEZADOT9WyiAbPFcEvj6px14A3ENGBjw2ZE9itYb4_Pog05Z1NKZswLWib8b5VUgCq1DeP2nY_MeC-_mC9_JUKtbv6Xzu12Wq497dLlZloaIierwD4oBTRr2BW98dwEM9bhu_xLS8Pd0wvVrEm1ewAntcW18oXbbm2wPXe7gjsphP2unkyyhHm2o5om8rKbXjkvE1dqOJmcFlyzLm48ElxvV6ItS9l_km2WZHYXLG2ZiiOb4Ty1zkU5cO84Sqf6bowNq8ZJKNvXEC0tOe4CS1TGlGlvdTrb1DFwbs5gKgH-LiEDFAV9IWwCzdg_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e07c2b244.mp4?token=b5kGyo3mMXPNtbJIFJvrMZWf3WqEZADOT9WyiAbPFcEvj6px14A3ENGBjw2ZE9itYb4_Pog05Z1NKZswLWib8b5VUgCq1DeP2nY_MeC-_mC9_JUKtbv6Xzu12Wq497dLlZloaIierwD4oBTRr2BW98dwEM9bhu_xLS8Pd0wvVrEm1ewAntcW18oXbbm2wPXe7gjsphP2unkyyhHm2o5om8rKbXjkvE1dqOJmcFlyzLm48ElxvV6ItS9l_km2WZHYXLG2ZiiOb4Ty1zkU5cO84Sqf6bowNq8ZJKNvXEC0tOe4CS1TGlGlvdTrb1DFwbs5gKgH-LiEDFAV9IWwCzdg_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سطح میم: لجندددددددد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/Futball180TV/91352" target="_blank">📅 21:03 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
